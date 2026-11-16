"""llmrun: resume without duplicate calls, same-experiment resume, pause, status, pinning, backoff, budget."""
import json
import os
import tempfile
import threading
import unittest

from llmrun import Halt, Limiter, Runner, dry_transport_for, status, validate_config


def cfg(**kw):
    c = {"run_id": "t", "allow_live": False, "endpoint": "x", "spend_cap_usd": 100.0, "seed": 1, "timeout_s": 5,
         "max_retries": 2, "halt_error_rate": 0.5, "halt_transient_aborts": 3,
         "models": {"A": {"slug": "lab/a", "provider": "host/fp8", "provider_name": "Host", "quantization": "fp8",
                          "params": {"temperature": 1.0, "max_tokens": 100}, "price_in_per_m": 1.0,
                          "price_out_per_m": 1.0, "concurrency_start": 2, "concurrency_max": 4}}}
    c.update(kw)
    return c


class Fake:
    """Counts calls; behaviour(n, body) -> (status, resp) or None for a normal answer."""
    def __init__(self, behaviour=None):
        self.n, self.lock, self.bodies = 0, threading.Lock(), []
        self.behaviour = behaviour

    def __call__(self, url, body, timeout):
        with self.lock:
            self.n += 1
            n = self.n
            self.bodies.append(body)
        if self.behaviour:
            out = self.behaviour(n, body)
            if out is not None:
                return out + (None,)
        text = "ans:" + body["messages"][-1]["content"]
        return 200, {"provider": "Host", "model": body["model"], "usage": {"cost": 0.001},
                     "choices": [{"finish_reason": "stop", "message": {"content": text}}]}, None


def two_stage(key):
    def fn(call, skip):
        r1 = call("t1", [{"role": "user", "content": key}])
        if r1["status"] != "ok":
            skip("t2", "turn1_failed")
            return
        call("t2", [{"role": "user", "content": r1["text"]}])
    return (key, "A", fn)


def plan(keys):
    return [(f"{k}|{s}", "A", [{"role": "user", "content": "x" * 40}]) for k in keys for s in ("t1", "t2")]


def man(keys):
    return {"experiment": "test", "planned_keys": sorted(k for k, _, _ in plan(keys))}


def results(d):
    with open(os.path.join(d, "journal.jsonl")) as f:
        return [json.loads(x) for x in f if '"type": "result"' in x]


class TestRunner(unittest.TestCase):
    def setUp(self):
        Runner.backoff = 0.0
        Runner.progress_every = 0
        self.d = tempfile.mkdtemp()
        self.keys = [f"k{i}" for i in range(20)]

    def go(self, transport, resume=False, keys=None, c=None, d=None):
        keys = keys or self.keys
        r = Runner(d or self.d, c or cfg(), man(keys), transport, resume=resume)
        return r, r.run([two_stage(k) for k in keys], plan(keys))

    def test_resume_no_duplicates_dependent_replay_and_same_structure(self):
        holder = {}

        def stop_after_15(n, body):
            if n == 15:
                holder["r"].stop.set()
        t1 = Fake(stop_after_15)
        r = Runner(self.d, cfg(), man(self.keys), t1)
        holder["r"] = r
        self.assertFalse(r.run([two_stage(k) for k in self.keys], plan(self.keys))["complete"])
        t2 = Fake()
        _, s2 = self.go(t2, resume=True)
        self.assertTrue(s2["complete"])
        self.assertEqual(s2["calls_pending"], 0)
        res = results(self.d)
        self.assertEqual(len({x["key"] for x in res}), len(res))  # every stage journaled exactly once
        self.assertEqual(t1.n + t2.n, 40)  # no stage ever sent twice
        for x in res:
            if x["key"].endswith("|t2"):
                self.assertEqual(x["text"], "ans:ans:" + x["key"].split("|")[0])  # t2 built on journaled t1
        clean = tempfile.mkdtemp()  # an uninterrupted run gives the identical key/status/text structure
        self.go(Fake(), d=clean)
        shape = lambda d: sorted((x["key"], x["status"], x["text"]) for x in results(d))
        self.assertEqual(shape(self.d), shape(clean))
        self.assertEqual([s["event"] for s in status(self.d)["sessions"]], ["start", "end", "resume", "end"])

    def test_new_run_refuses_existing_dir_and_resume_needs_existing(self):
        with self.assertRaises(Halt):
            Runner(self.d, cfg(), man(self.keys), Fake(), resume=True)
        self.go(Fake())
        with self.assertRaises(Halt):
            Runner(self.d, cfg(), man(self.keys), Fake())

    def test_resume_refuses_changed_config_or_matrix(self):
        self.go(Fake(), keys=["a", "b"])
        with self.assertRaises(Halt):
            Runner(self.d, cfg(seed=2), man(["a", "b"]), Fake(), resume=True)
        with self.assertRaises(Halt):
            Runner(self.d, cfg(), man(["a", "b", "c"]), Fake(), resume=True)

    def test_planned_calls_must_match_manifest(self):
        r = Runner(self.d, cfg(), man(["a"]), Fake())
        with self.assertRaises(Halt):
            r.run([two_stage("a"), two_stage("b")], plan(["a", "b"]))

    def test_pause_file_then_resume_completes(self):
        holder = {}

        def pause_at_10(n, body):
            if n == 10:
                open(os.path.join(self.d, "PAUSE"), "w").close()
        t1 = Fake(pause_at_10)
        r = Runner(self.d, cfg(), man(self.keys), t1)
        holder["r"] = r
        s1 = r.run([two_stage(k) for k in self.keys], plan(self.keys))
        self.assertTrue(s1["paused"])
        self.assertFalse(s1["complete"])
        st = status(self.d)
        self.assertTrue(st["paused"])
        self.assertEqual(st["calls_done"] + st["calls_pending"], 40)
        t2 = Fake()
        _, s2 = self.go(t2, resume=True)
        self.assertTrue(s2["complete"])
        self.assertFalse(os.path.exists(os.path.join(self.d, "PAUSE")))
        self.assertEqual(t1.n + t2.n, 40)

    def test_second_runner_on_same_dir_refused(self):
        self.go(Fake(), keys=["a"])
        r = Runner(self.d, cfg(), man(["a"]), Fake(), resume=True)
        with self.assertRaises(Halt):
            Runner(self.d, cfg(), man(["a"]), Fake(), resume=True)
        r.close()

    def test_429_backs_off_then_completes(self):
        t = Fake(lambda n, b: (429, {"error": "rate"}) if n <= 3 else None)
        # max_retries > number of 429s, so no task can exhaust its attempts whatever the interleaving
        c = cfg(max_retries=4, models={"A": dict(cfg()["models"]["A"], concurrency_start=4)})
        _, s = self.go(t, keys=self.keys[:5], c=c)
        self.assertTrue(s["complete"])
        self.assertEqual(s["spent_usd"], round(10 * 0.001, 6))  # voided 429 intents are not charged

    def test_provider_mismatch_is_terminal_and_not_retried(self):
        t = Fake(lambda n, b: (200, {"provider": "Other", "model": b["model"], "usage": {"cost": 0},
                                     "choices": [{"message": {"content": "x"}}]}))
        _, s = self.go(t, keys=["a"], c=cfg(halt_error_rate=1.0))
        res = {x["key"]: x for x in results(self.d)}
        self.assertEqual(res["a|t1"]["status"], "failed")
        self.assertEqual(res["a|t2"]["status"], "skipped")
        self.assertEqual(t.n, 1)
        self.assertTrue(s["complete"])

    def test_refuses_to_start_when_cap_cannot_cover_full_design(self):
        r = Runner(self.d, cfg(spend_cap_usd=0.0005), man(self.keys), Fake())
        with self.assertRaises(Halt):
            r.run([two_stage(k) for k in self.keys], plan(self.keys))
        self.assertEqual(results(self.d), [])  # nothing sent: never a partial design

    def test_outage_aborts_without_journaling_then_resume_completes(self):
        _, s = self.go(Fake(lambda n, b: (503, {"error": "down"})))
        self.assertTrue(s["halted"])
        self.assertEqual(results(self.d), [])
        _, s2 = self.go(Fake(), resume=True)
        self.assertTrue(s2["complete"])
        self.assertEqual(len(results(self.d)), 40)

    def test_provider_error_inside_200_is_retried_not_recorded(self):
        bad = {"provider": "Host", "model": "lab/a", "error": {"message": "upstream"}, "choices": []}
        _, s = self.go(Fake(lambda n, b: (200, dict(bad, model=b["model"])) if n <= 2 else None),
                       keys=["a"], c=cfg(max_retries=4))
        self.assertTrue(s["complete"])
        self.assertTrue(all(x["status"] == "ok" for x in results(self.d)))

    def test_out_of_credit_halts_without_recording_failures(self):
        _, s = self.go(Fake(lambda n, b: (402, {"error": "insufficient credits"}) if n > 6 else None))
        self.assertTrue(s["halted"])
        self.assertTrue(all(x["status"] == "ok" for x in results(self.d)))  # no 402 ever journaled as a failure
        _, s2 = self.go(Fake(), resume=True)
        self.assertTrue(s2["complete"])
        self.assertEqual(len(results(self.d)), 40)

    def test_timeout_keeps_reservation_as_spent_during_the_run(self):
        def t(n, b):
            if n == 1:
                raise TimeoutError("read timed out")
        _, s = self.go(Fake(t), keys=["a"], c=cfg(max_retries=3))
        self.assertTrue(s["complete"])
        self.assertGreater(s["unsettled_billing_usd"], 0)
        self.assertAlmostEqual(s["spent_usd"], round(2 * 0.001 + s["unsettled_billing_usd"], 6))
        self.assertAlmostEqual(status(self.d)["spent_usd"], s["spent_usd"])  # in-run == on-disk accounting

    def test_damaged_envelope_keeps_status_and_is_billing_unknown(self):
        _, s = self.go(Fake(lambda n, b: (200, {"_malformed_envelope": True}) if n == 1 else None),
                       keys=["a"], c=cfg(max_retries=3))
        with open(os.path.join(self.d, "journal.jsonl")) as f:
            errs = [json.loads(x) for x in f if '"attempt_error"' in x]
        self.assertEqual((errs[0]["http_status"], errs[0]["billed_unknown"]), (200, True))
        self.assertGreater(s["unsettled_billing_usd"], 0)

    def test_errors_never_grow_capacity_and_sustained_errors_halve_it(self):
        lim = Limiter(8, 16)
        for _ in range(3):
            lim.active += 1
            lim.release("error")
        self.assertEqual(lim.limit, 8)
        lim.active += 1
        lim.release("error")
        self.assertEqual(lim.limit, 4)
        for _ in range(2):
            lim.active += 1
            lim.release("ok")
        self.assertEqual(lim.limit, 5)

    def test_429_from_two_models_halves_every_model(self):
        c = cfg()
        c["models"]["B"] = dict(c["models"]["A"], slug="lab/b")
        r = Runner(self.d, c, man(["a"]), Fake())
        for lim in r.limiters.values():
            lim.limit = 8
        r._account_429("A")
        self.assertEqual([l.limit for l in r.limiters.values()], [8, 8])
        r._account_429("B")
        self.assertEqual([l.limit for l in r.limiters.values()], [4, 4])
        r.close()

    def test_nothing_dispatched_after_stop_and_in_flight_reported(self):
        holder = {}

        def stop_first(n, b):
            if n == 1:
                holder["r"]._halt("test")
        t = Fake(stop_first)
        one = cfg(models={"A": dict(cfg()["models"]["A"], concurrency_start=1, concurrency_max=1)})
        r = Runner(self.d, one, man(self.keys), t)
        holder["r"] = r
        s = r.run([two_stage(k) for k in self.keys], plan(self.keys))
        self.assertEqual(t.n, 1)
        self.assertEqual(s["stop_info"]["reason"], "test")
        self.assertEqual(s["stop_info"]["in_flight"], 1)

    def test_no_cap_runs_full_design(self):
        _, s = self.go(Fake(), c=cfg(spend_cap_usd=None))
        self.assertTrue(s["complete"])

    def test_missing_usage_is_unknown_cost_not_zero(self):
        t = Fake(lambda n, b: (200, {"provider": "Host", "model": b["model"],
                                     "choices": [{"finish_reason": "stop", "message": {"content": "x"}}]}))
        _, s = self.go(t, keys=["a"])
        res = results(self.d)
        self.assertTrue(all(r["cost_usd"] is None and r["billing_unresolved"] for r in res))
        self.assertEqual(s["results_without_billing"], 2)

    def test_unsettled_intent_counts_as_spent_on_resume(self):
        r = Runner(self.d, cfg(), man(["a"]), Fake())
        r._write({"type": "intent", "iid": "z#0#1", "key": "a|t1", "reserve_usd": 0.25})
        r.close()
        self.assertAlmostEqual(Runner(self.d, cfg(), man(["a"]), Fake(), resume=True).spent, 0.25)
        self.assertAlmostEqual(status(self.d)["spent_usd"], 0.25)

    def test_request_pins_route_and_denies_data_collection(self):
        t = Fake()
        self.go(t, keys=["a"])
        self.assertEqual(t.bodies[0]["provider"], {"order": ["host/fp8"], "allow_fallbacks": False,
                                                   "require_parameters": True, "quantizations": ["fp8"],
                                                   "data_collection": "deny"})

    def test_live_needs_flag_and_config_is_strict(self):
        with self.assertRaises(Halt):
            Runner(self.d, cfg(), man(["a"]))
        with self.assertRaises(ValueError):
            validate_config(dict(cfg(), extra=1))
        bad = cfg()
        bad["models"]["A"]["params"]["tools"] = []
        with self.assertRaises(ValueError):
            validate_config(bad)

    def test_dry_transport_matches_pin(self):
        c = cfg()
        _, s = self.go(dry_transport_for(c), keys=["a"], c=c)
        self.assertTrue(s["complete"])
        self.assertTrue(all(x["status"] == "ok" for x in results(self.d)))


if __name__ == "__main__":
    unittest.main()
