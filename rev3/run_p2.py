"""Run P2 stimuli through llmrun, then export responses for scoring (p2v3.score). No scoring here.

  new run:  python3 run_p2.py --config C.json --stimuli S.jsonl --repeats 3 --run-dir runs/X [--dry-run]
  resume:   same command + --resume        (refused unless config, stimuli, repeats and models are identical)
  pause:    touch runs/X/PAUSE             (in-flight calls finish; resume with --resume)
  status:   python3 run_p2.py --status --run-dir runs/X     (read-only; safe while running)

Every model runs every stimulus x repeat (the full 14-cell x 2-context design per case). Each stimulus's
hash is re-checked against its messages before anything is sent. The manifest frozen with the run lists
every planned call plus the stimuli file hash, repeats and models.
"""
import argparse
import json
import os

import hashlib

from llmrun import Halt, Runner, dry_transport_for, status
from p2v3.render import stimulus_hash


def load_stimuli(path):
    with open(path) as f:
        rows = [json.loads(x) for x in f if x.strip()]
    for s in rows:
        if stimulus_hash(s["messages"]) != s["stimulus_sha256"]:
            raise Halt(f"stimulus hash mismatch: {s['item_id']} {s['condition']} {s['direction']} {s['context']}")
    return rows


def task_key(model, s, k):
    return f"{model}|{s['item_id']}|{s['condition']}|{s['direction']}|{s['context']}|r{k}"


def build(models, stimuli, repeats):
    tasks, planned = [], []
    for m in models:
        for s in stimuli:
            for k in range(repeats):
                key = task_key(m, s, k)
                tasks.append((key, m, lambda call, skip, msgs=s["messages"]: call("main", msgs)))
                planned.append((f"{key}|main", m, s["messages"]))
    return tasks, planned


def export(run_dir, models, stimuli, repeats):
    with open(os.path.join(run_dir, "journal.jsonl")) as f:
        done = {r["key"]: r for r in map(json.loads, f) if r.get("type") == "result"}
    out, missing = [], 0
    for m in models:
        for s in stimuli:
            for k in range(repeats):
                r = done.get(task_key(m, s, k) + "|main")
                missing += r is None
                out.append({"model": m, "item_id": s["item_id"], "condition": s["condition"],
                            "direction": s["direction"], "context": s["context"], "repeat": k,
                            "stimulus_sha256": s["stimulus_sha256"],
                            "status": r["status"] if r else "not_run", "text": (r or {}).get("text"),
                            "truncated": (r or {}).get("truncated"), "served_provider": (r or {}).get("served_provider"),
                            "served_model": (r or {}).get("served_model"), "cost_usd": (r or {}).get("cost_usd"),
                            "reasoning_returned": (r or {}).get("reasoning_returned"),
                            "reasoning_tokens": (r or {}).get("reasoning_tokens"),
                            "request_params": (r or {}).get("request_params")})
    with open(os.path.join(run_dir, "responses.jsonl"), "w") as f:
        f.writelines(json.dumps(x, sort_keys=True) + "\n" for x in out)
    return len(out), missing


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config")
    ap.add_argument("--stimuli")
    ap.add_argument("--repeats", type=int)
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--dry-run", action="store_true", help="offline fake transport; no network, no cost")
    ap.add_argument("--resume", action="store_true", help="continue the existing run in --run-dir")
    ap.add_argument("--status", action="store_true", help="print progress and exit (read-only)")
    a = ap.parse_args()
    if a.status:
        print(json.dumps(status(a.run_dir), indent=1, sort_keys=True))
        return
    if not (a.config and a.stimuli and a.repeats):
        ap.error("--config, --stimuli and --repeats are required to start or resume a run")
    with open(a.config) as f:
        cfg = json.load(f)
    stimuli = load_stimuli(a.stimuli)
    models = sorted(cfg["models"])
    tasks, planned = build(models, stimuli, a.repeats)
    with open(a.stimuli, "rb") as f:
        stim_sha = hashlib.sha256(f.read()).hexdigest()
    manifest = {"experiment": "P2 scope-of-trust", "stimuli_sha256": stim_sha, "repeats": a.repeats,
                "models": models, "planned_keys": sorted(k for k, _, _ in planned)}
    runner = Runner(a.run_dir, cfg, manifest, dry_transport_for(cfg) if a.dry_run else None, resume=a.resume)
    print(f"{len(tasks)} calls planned")
    summary = runner.run(tasks, planned)
    n, missing = export(a.run_dir, models, stimuli, a.repeats)
    print(json.dumps(summary, indent=1, sort_keys=True))
    print(f"exported {n} rows; {missing} not run")


if __name__ == "__main__":
    main()
