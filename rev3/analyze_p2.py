"""Score and analyse a P2 run's responses.jsonl. DIAGNOSTIC PILOT ONLY on dev cases.

  python3 analyze_p2.py --run-dir runs/X        -> runs/X/analysis.json and runs/X/analysis.md

Per model, never pooled across models (spec: model-specific effects first; pooling needs a prespecified rule):
- data quality: call status, parse status, truncation, served provider/model actually seen;
- per-cell rates of the primary endpoint unsupported_q_obs (attribution context);
- primary contrasts P1 B-A, P2 B-D1, P3 C-B (unsupported_q_obs) and P4 E_scope-E (correct acceptance,
  improved direction), each with the equal-case estimate, a provisional conservative interval
  (tango_c_cc, 95% two-sided), and scheduled-denominator bounds with missing outcomes imputed worst/best;
- belief context: mean absolute error of p(Q_obs) per cell.
The interval method and the P4 margin are not yet approved, so no hypothesis decisions are made here.
"""
import argparse
import json
import os
from collections import defaultdict

from p2v3 import stats
from p2v3.score import score_attribution, score_belief

CONTRASTS = [("P1", "B", "none", "A", "none", "unsupported_q_obs"),
             ("P2", "B", "none", "D1", "none", "unsupported_q_obs"),
             ("P3", "C", "none", "B", "none", "unsupported_q_obs"),
             ("P4", "E_scope", "improved", "E", "improved", "correct_acceptance")]
LABEL = ("DIAGNOSTIC PILOT on development cases (one author, one template family). Interval method "
         "provisional; P4 margin unapproved; not confirmatory evidence.")


def b01(v):
    return None if v is None else int(bool(v))


def score_rows(rows):
    for r in rows:
        ok = r["status"] == "ok"
        if r["context"] == "attribution":
            r["metrics"] = score_attribution(r["text"] or "", r["condition"], r["direction"]) if ok else None
        else:
            r["metrics"] = score_belief(r["text"] or "", r["condition"], r["direction"]) if ok else None
        r["parse"] = r["metrics"]["parse"] if r["metrics"] else f"not_scored:{r['status']}"
    return rows


def contrast(rows, x, dx, y, dy, metric):
    """Per-case outcome lists for arms X and Y, paired by repeat; then estimate, interval and bounds."""
    arms = defaultdict(lambda: ({}, {}))
    for r in rows:
        if r["context"] != "attribution":
            continue
        for i, (c, d) in enumerate(((x, dx), (y, dy))):
            if (r["condition"], r["direction"]) == (c, d):
                arms[r["item_id"]][i][r["repeat"]] = b01((r["metrics"] or {}).get(metric))
    out = {}
    for name, fill in (("observed", None), ("worst", (0, 1)), ("best", (1, 0))):
        cells = []
        for case, (ax, ay) in sorted(arms.items()):
            reps = sorted(set(ax) | set(ay))
            cells.append(stats.pair_counts([ax.get(k) for k in reps], [ay.get(k) for k in reps], fill))
        try:
            s = stats.summarize(cells)
            lo, hi = stats.tango(s, 0.025, conservative=True, cc=0.5)
            out[name] = {"estimate": stats.estimate(s), "ci95": [lo, hi], "cases": s.K, "cases_dropped": s.dropped}
        except ValueError as e:
            out[name] = {"estimate": None, "note": f"not estimable: {e}"}
    return out


def analyse(rows):
    res = {"label": LABEL, "models": {}}
    for m in sorted({r["model"] for r in rows}):
        mr = [r for r in rows if r["model"] == m]
        q = defaultdict(lambda: defaultdict(int))
        for r in mr:
            q["status"][r["status"]] += 1
            q["parse"][r["parse"]] += 1
            q["truncated"][str(bool(r.get("truncated")))] += 1
            q["served_provider"][str(r.get("served_provider"))] += 1
            q["served_model"][str(r.get("served_model"))] += 1
            q["reasoning_returned"][str(r.get("reasoning_returned"))] += 1
            q["request_params"][json.dumps({k: v for k, v in (r.get("request_params") or {}).items()
                                            if k not in ("model", "usage", "provider")}, sort_keys=True)] += 1
        rates = defaultdict(list)
        belief = defaultdict(list)
        for r in mr:
            met = r["metrics"] or {}
            cell = f"{r['condition']}/{r['direction']}"
            if r["context"] == "attribution" and met.get("unsupported_q_obs") is not None:
                rates[cell].append(int(met["unsupported_q_obs"]))
            if r["context"] == "belief" and met.get("abs_error") is not None:
                belief[cell].append(met["abs_error"])
        res["models"][m] = {
            "n_calls": len(mr), "spent_usd": round(sum(r.get("cost_usd") or 0 for r in mr), 6),
            "quality": {k: dict(v) for k, v in q.items()},
            "unsupported_q_obs_rate": {c: {"rate": sum(v) / len(v), "n": len(v)} for c, v in sorted(rates.items())},
            "belief_mean_abs_error": {c: {"mae": sum(v) / len(v), "n": len(v)} for c, v in sorted(belief.items())},
            "contrasts": {n: dict(contrast(mr, x, dx, y, dy, met), definition=f"{x}/{dx} - {y}/{dy} on {met}")
                          for n, x, dx, y, dy, met in CONTRASTS}}
    return res


def fmt(v):
    return "–" if v is None else f"{v:+.3f}"


def markdown(res):
    out = [f"# P2 pilot analysis", "", f"**{res['label']}**", ""]
    for m, r in res["models"].items():
        q = r["quality"]
        out += [f"## {m}", "", f"Calls {r['n_calls']}, spend ${r['spent_usd']:.4f}. Status {q['status']}. "
                f"Parse {q['parse']}. Truncated {q['truncated'].get('True', 0)}. "
                f"Served provider {q['served_provider']}; served model {q['served_model']}.", "",
                "| contrast | definition | estimate | 95% CI (provisional) | worst–best bounds | cases |",
                "|---|---|---|---|---|---|"]
        for n, c in r["contrasts"].items():
            o, w, b = c["observed"], c["worst"], c["best"]
            ci = f"[{o['ci95'][0]:+.3f}, {o['ci95'][1]:+.3f}]" if o.get("ci95") else o.get("note", "–")
            out.append(f"| {n} | {c['definition']} | {fmt(o.get('estimate'))} | {ci} | "
                       f"{fmt(w.get('estimate'))} to {fmt(b.get('estimate'))} | {o.get('cases', '–')} |")
        out += ["", "| cell | unsupported Q_obs rate | n | belief MAE | n |", "|---|---|---|---|---|"]
        cells = sorted(set(r["unsupported_q_obs_rate"]) | set(r["belief_mean_abs_error"]))
        for c in cells:
            u, bm = r["unsupported_q_obs_rate"].get(c, {}), r["belief_mean_abs_error"].get(c, {})
            out.append(f"| {c} | {u.get('rate', float('nan')):.3f} | {u.get('n', 0)} | "
                       f"{bm.get('mae', float('nan')):.3f} | {bm.get('n', 0)} |")
        out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    a = ap.parse_args()
    with open(os.path.join(a.run_dir, "responses.jsonl")) as f:
        rows = score_rows([json.loads(x) for x in f if x.strip()])
    res = analyse(rows)
    with open(os.path.join(a.run_dir, "analysis.json"), "w") as f:
        json.dump(res, f, indent=1, sort_keys=True)
    with open(os.path.join(a.run_dir, "analysis.md"), "w") as f:
        f.write(markdown(res))
    print(markdown(res))


if __name__ == "__main__":
    main()
