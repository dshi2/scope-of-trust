"""Concurrent, resumable model runner shared by P1 and P2. Stdlib only.

Contract
- A run directory holds one frozen config. The journal header binds the config hash; resuming with a
  different config is refused, so settings never change mid-run. One runner per directory (lock file).
- A task is (key, model, fn). fn(call, skip) runs the task's stages: call(stage, messages, tools=None)
  returns a journaled result; skip(stage, reason) journals an adapter-declared skip (e.g. P1 branches
  after a turn-1 failure). Every result is appended and fsynced before fn sees it. On resume, journaled
  stages are replayed from disk with no API call, so dependent stages continue exactly.
- Terminal results are journaled once and never retried: "ok" (truncation flagged), "failed"
  (non-retryable HTTP error, empty choices, or the served provider/model differs from the pin), "skipped".
- Transient errors (429, 5xx, timeouts, connection) are retried with backoff. If retries run out the task
  is aborted, NOT journaled, and runs again on resume. halt_transient_aborts aborts halt the run, as does a
  terminal-failure rate above halt_error_rate over the last 50 results (once 20 exist).
- Concurrency per model starts at concurrency_start: halved on a 429, +1 after `limit` straight successes,
  capped at concurrency_max.
- Spend: budget must never truncate a design (that is what made the shutdown study's cells uneven).
  run() refuses to start unless spend_cap_usd covers spent + the worst case of every remaining planned
  call. Each call writes an intent with a worst-case reservation and settles to the billed cost after;
  an HTTP error response (never billed) voids its intent; on resume, unsettled intents count as spent.
  The in-run cap check is a runaway-fault guard only.
- Order: tasks are shuffled with the config seed (execution order randomized within each model).
- Routing (per "Not Pinning Your OpenRouter Provider Might Invalidate Your Research", LessWrong 2026):
  endpoint pinned by tag, quantization pinned, allow_fallbacks=false, require_parameters=true,
  data_collection=deny. The served provider name and model are journaled with every result and checked
  against provider_name and slug; a mismatch is a terminal failure. A provider outage halts the run;
  switching provider means a new config, hence a new run directory, never a silent substitution.
- The API key comes only from OPENROUTER_API_KEY and is never written anywhere.
- Ctrl-C stops scheduling, cancels queued tasks, lets in-flight calls finish and be journaled.
  Rerun the same command to resume.
"""
import hashlib
import json
import os
import random
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

RUN_KEYS = {"run_id", "allow_live", "endpoint", "spend_cap_usd", "seed", "timeout_s", "max_retries",
            "halt_error_rate", "halt_transient_aborts", "models"}
MODEL_KEYS = {"slug", "provider", "provider_name", "quantization", "params", "price_in_per_m", "price_out_per_m",
              "concurrency_start", "concurrency_max"}
TRANSIENT = {408, 409, 425, 429, 500, 502, 503, 504, 520, 522, 524, 529}


class Halt(Exception):
    pass


class Transient(Exception):
    def __init__(self, msg, retry_after=None, billed_unknown=False):
        super().__init__(msg)
        self.retry_after, self.billed_unknown = retry_after, billed_unknown


def validate_config(cfg):
    if set(cfg) != RUN_KEYS:
        raise ValueError(f"config keys must be exactly {sorted(RUN_KEYS)}; diff {sorted(set(cfg) ^ RUN_KEYS)}")
    for name, m in cfg["models"].items():
        if set(m) != MODEL_KEYS:
            raise ValueError(f"model {name}: keys must be exactly {sorted(MODEL_KEYS)}")
        if "max_tokens" not in m["params"] or {"model", "messages", "provider", "tools"} & set(m["params"]):
            raise ValueError(f"model {name}: params needs max_tokens and must not set model/messages/provider/tools")
        if not 1 <= m["concurrency_start"] <= m["concurrency_max"]:
            raise ValueError(f"model {name}: need 1 <= concurrency_start <= concurrency_max")
    return hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest()


def http_transport(url, body, timeout):
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        raise Halt("OPENROUTER_API_KEY is not set")
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
                                 headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, json.loads(r.read()), r.headers.get("Retry-After")
    except urllib.error.HTTPError as e:
        try:
            payload = json.loads(e.read())
        except Exception:
            payload = {"error": str(e)}
        return e.code, payload, e.headers.get("Retry-After")


def dry_transport_for(cfg):
    """Offline stand-in that answers as the pinned endpoint would; no network call, zero cost."""
    names = {m["slug"]: m["provider_name"] for m in cfg["models"].values()}

    def t(url, body, timeout):
        return 200, {"provider": names[body["model"]], "model": body["model"],
                     "choices": [{"finish_reason": "stop", "message": {"role": "assistant", "content": "{}"}}],
                     "usage": {"prompt_tokens": 100, "completion_tokens": 10, "cost": 0.0}}, None
    return t


class Limiter:
    def __init__(self, start, cap):
        self.limit, self.cap, self.active, self.streak = start, cap, 0, 0
        self.cv = threading.Condition()

    def acquire(self):
        with self.cv:
            while self.active >= self.limit:
                self.cv.wait()
            self.active += 1

    def release(self, throttled=False):
        with self.cv:
            self.active -= 1
            if throttled:
                self.limit, self.streak = max(1, self.limit // 2), 0
            else:
                self.streak += 1
                if self.streak >= self.limit and self.limit < self.cap:
                    self.limit, self.streak = self.limit + 1, 0
            self.cv.notify_all()


class Runner:
    backoff = 1.0  # seconds scale for retry waits (tests set 0)

    def __init__(self, run_dir, cfg, transport=None):
        self.cfg, self.dir = cfg, run_dir
        self.hash = validate_config(cfg)
        if transport is None:
            if not cfg["allow_live"]:
                raise Halt("allow_live is false: pass dry_transport_for(cfg) for an offline run")
            transport = http_transport
        self.transport = transport
        self.lock = threading.Lock()
        self.stop = threading.Event()
        self.done, self.spent, self.reserved, self.aborts, self.recent = {}, 0.0, 0.0, 0, []
        self.limiters = {n: Limiter(m["concurrency_start"], m["concurrency_max"]) for n, m in cfg["models"].items()}
        os.makedirs(run_dir, exist_ok=True)
        self._lock_dir()
        self.path = os.path.join(run_dir, "journal.jsonl")
        self._open()

    def _lock_dir(self):
        self.lockfile = os.path.join(self.dir, "run.lock")
        try:
            fd = os.open(self.lockfile, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            try:
                pid = int(open(self.lockfile).read() or 0)
                os.kill(pid, 0)
                raise Halt(f"another runner (pid {pid}) holds {self.dir}")
            except (ValueError, ProcessLookupError):
                os.remove(self.lockfile)  # stale lock from a dead process
                fd = os.open(self.lockfile, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(fd, str(os.getpid()).encode())
        os.close(fd)

    def close(self):
        f = getattr(self, "f", None)
        if f and not f.closed:
            f.close()
        if os.path.exists(self.lockfile):
            os.remove(self.lockfile)

    # ---- journal -------------------------------------------------------------------------------
    def _open(self):
        intents, fresh = {}, not os.path.exists(self.path) or os.path.getsize(self.path) == 0
        if not fresh:
            with open(self.path) as f:
                lines = [json.loads(x) for x in f if x.strip()]
            if lines[0].get("type") != "header" or lines[0]["config_sha256"] != self.hash:
                self.close()
                raise Halt("run directory belongs to a different config; use a new run directory")
            for r in lines[1:]:
                if r["type"] == "intent":
                    intents[r["iid"]] = r["reserve_usd"]
                elif r["type"] in ("result", "void"):
                    intents.pop(r.get("iid"), None)
                    if r["type"] == "result":
                        self.done[r["key"]] = r
                        self.spent += r.get("cost_usd") or 0.0
            self.spent += sum(intents.values())  # possibly billed, never settled: count conservatively
        self.f = open(self.path, "a")
        if fresh:
            self._write({"type": "header", "config_sha256": self.hash, "config": self.cfg, "t": time.time()})

    def _write(self, rec):
        self.f.write(json.dumps(rec, sort_keys=True) + "\n")
        self.f.flush()
        os.fsync(self.f.fileno())

    # ---- one stage -----------------------------------------------------------------------------
    def _body(self, model, messages, tools):
        m = self.cfg["models"][model]
        body = dict(m["params"], model=m["slug"], messages=messages, usage={"include": True},
                    provider={"order": [m["provider"]], "allow_fallbacks": False, "require_parameters": True,
                              "quantizations": [m["quantization"]], "data_collection": "deny"})
        if tools:
            body["tools"] = tools
        return body

    def _reserve(self, model, body):
        m = self.cfg["models"][model]
        tokens_in = len(json.dumps(body["messages"])) / 2  # deliberately high: real ratio is ~4 chars/token
        return (tokens_in * m["price_in_per_m"] + m["params"]["max_tokens"] * m["price_out_per_m"]) / 1e6

    def _result(self, key, model, status, iid=None, **kw):
        rec = dict(type="result", key=key, model=model, status=status, iid=iid, t=time.time(), **kw)
        with self.lock:
            self._write(rec)
            self.done[key] = rec
            self.spent += rec.get("cost_usd") or 0.0
            if status != "skipped":
                self.recent = (self.recent + [status == "failed"])[-50:]
                if len(self.recent) >= 20 and sum(self.recent) / len(self.recent) > self.cfg["halt_error_rate"]:
                    self.stop.set()
        return rec

    def call(self, key, model, messages, tools=None):
        if key in self.done:
            return self.done[key]
        if self.stop.is_set():
            raise Halt("stopping")
        body = self._body(model, messages, tools)
        req_sha = hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()
        lim = self.limiters[model]
        for attempt in range(self.cfg["max_retries"] + 1):
            reserve, iid = self._reserve(model, body), f"{key}#{attempt}#{time.time_ns()}"
            with self.lock:
                if self.spent + self.reserved + reserve > self.cfg["spend_cap_usd"]:
                    self.stop.set()
                    raise Halt("spend cap reached")
                self.reserved += reserve
                self._write({"type": "intent", "iid": iid, "key": key, "reserve_usd": reserve, "t": time.time()})
            lim.acquire()
            status = None
            try:
                status, resp, retry_after = self.transport(self.cfg["endpoint"], body, self.cfg["timeout_s"])
                if status in TRANSIENT:
                    raise Transient(f"HTTP {status}", retry_after)
                return self._settle(key, model, iid, req_sha, status, resp)
            except (Transient, TimeoutError, ConnectionError, OSError) as e:
                billed_unknown = status is None  # no HTTP response: the provider may have billed
                with self.lock:
                    if not billed_unknown:
                        self._write({"type": "void", "iid": iid, "key": key, "t": time.time()})
                if attempt == self.cfg["max_retries"] or self.stop.is_set():
                    raise Transient(str(e), billed_unknown=billed_unknown) from e
                ra = getattr(e, "retry_after", None)
                wait = float(ra) if ra and str(ra).replace(".", "", 1).isdigit() else 2 ** attempt
                time.sleep(min(60.0, wait) * self.backoff * (0.5 + random.random()))
            finally:
                lim.release(throttled=status == 429)
                with self.lock:
                    self.reserved -= reserve

    def _settle(self, key, model, iid, req_sha, status, resp):
        m = self.cfg["models"][model]
        usage = resp.get("usage") or {}
        cost = usage.get("cost")
        if cost is None:
            cost = (usage.get("prompt_tokens", 0) * m["price_in_per_m"]
                    + usage.get("completion_tokens", 0) * m["price_out_per_m"]) / 1e6
        common = dict(iid=iid, request_sha256=req_sha, http_status=status, response=resp, usage=usage,
                      cost_usd=cost, served_provider=resp.get("provider"), served_model=resp.get("model"))
        if status != 200 or not resp.get("choices"):
            return self._result(key, model, "failed", error=f"HTTP {status}", **common)
        if resp.get("provider") != m["provider_name"] or not str(resp.get("model", "")).startswith(m["slug"]):
            return self._result(key, model, "failed", error="served provider/model differs from pin", **common)
        ch = resp["choices"][0]
        msg = ch.get("message") or {}
        return self._result(key, model, "ok", text=msg.get("content") or "", tool_calls=msg.get("tool_calls"),
                            message=msg, truncated=ch.get("finish_reason") == "length", **common)

    def skip(self, key, model, reason):
        if key in self.done:
            return self.done[key]
        return self._result(key, model, "skipped", error=reason, cost_usd=0.0)

    # ---- tasks ---------------------------------------------------------------------------------
    def worst_case_usd(self, planned):
        """Worst-case cost of every planned call not yet journaled. planned: [(full_key, model, messages)],
        one entry per call the frozen design can make (P1: include every possible lookup continuation)."""
        return sum(self._reserve(m, self._body(m, msgs, None)) for k, m, msgs in planned if k not in self.done)

    def run(self, tasks, planned):
        """tasks: iterable of (task_key, model, fn); planned: see worst_case_usd. Writes summary.json.

        Budget never truncates a design: the run refuses to START unless spend_cap_usd covers the money
        already spent plus the worst case of everything remaining. The in-run cap check then only fires on
        a runaway fault (retry storm, price change), never as a planned stopping rule."""
        need = self.spent + self.worst_case_usd(planned)
        if need > self.cfg["spend_cap_usd"]:
            self.close()
            raise Halt(f"spend_cap_usd {self.cfg['spend_cap_usd']} < worst case for the full design {need:.2f}; "
                       "raise the cap or shrink the design BEFORE starting")
        tasks = list(tasks)
        random.Random(self.cfg["seed"]).shuffle(tasks)
        state = {"finished": 0, "aborted": 0}

        def one(task):
            tkey, model, fn = task
            if self.stop.is_set():
                return
            try:
                fn(lambda stage, messages, tools=None: self.call(f"{tkey}|{stage}", model, messages, tools),
                   lambda stage, reason: self.skip(f"{tkey}|{stage}", model, reason))
                with self.lock:
                    state["finished"] += 1
            except Transient:
                with self.lock:
                    state["aborted"] += 1
                    self.aborts += 1
                    if self.aborts >= self.cfg["halt_transient_aborts"]:
                        self.stop.set()
            except Halt:
                pass

        ex = ThreadPoolExecutor(max_workers=sum(m["concurrency_max"] for m in self.cfg["models"].values()))
        try:
            futures = [ex.submit(one, t) for t in tasks]
            for fu in futures:
                fu.result()
        except KeyboardInterrupt:
            self.stop.set()
            ex.shutdown(wait=True, cancel_futures=True)
            raise
        finally:
            ex.shutdown(wait=True)
            summary = self._summary(state, len(tasks))
            self.close()
        return summary

    def _summary(self, state, n):
        by = {}
        for r in self.done.values():
            by.setdefault(r["model"], {}).setdefault(r["status"], 0)
            by[r["model"]][r["status"]] += 1
        s = dict(state, tasks=n, not_run=n - state["finished"] - state["aborted"], halted=self.stop.is_set(),
                 complete=state["finished"] == n, spent_usd=round(self.spent, 6), journal_by_model=by)
        with open(os.path.join(self.dir, "summary.json"), "w") as f:
            json.dump(s, f, indent=1, sort_keys=True)
        return s
