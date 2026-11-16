"""Score and analyse a P2 run's responses.jsonl. DIAGNOSTIC PILOT ONLY on dev cases.

  python3 analyze_p2.py --run-dir runs/X                   -> runs/X/analysis.json and runs/X/analysis.md
  python3 analyze_p2.py --run-dir runs/A runs/B --out DIR    (base + extension cases together)

Per model, never pooled across models (spec: model-specific effects first; pooling needs a prespecified rule):
- data quality: call status, parse status, truncation, served provider/model actually seen;
- per-cell rates of the primary endpoint unsupported_q_obs (attribution context);
- primary contrasts P1 B-A, P2 B-D1, P3 C-B (unsupported_q_obs) and P4 E_scope-E (correct acceptance,
  improved direction), each with the equal-case estimate, a provisional conservative interval
  (tango_c_cc, 95% two-sided), and scheduled-denominator bounds with missing outcomes imputed worst/best;
- component table fixed by spec §6: P1-P3 also on unsupported Q_cause, Q_welfare and the Q_obs-or-Q_cause
  composite, each with its interval (only Q_obs is confirmatory);
- two-sided score-test p-values (same Tango variant as the interval, at Delta = 0) for P1-P3, Holm-adjusted
  across P1-P3 on the primary outcome (P4 joins the family once its margin is fixed; until then it has only
  its lower bound);
- validity / positive-control checks V1 (correct acceptance, E and E_scope improved), V2 (correct
  refutation, worsened / unchanged) and V3 (manipulation checks B, C, C_prime, D1, D2): equal-case mean of
  case-level rates with a t interval over cases (df = cases - 1), clipped to [0, 1]; `degenerate` when every
  case has the same rate (zero width is not precision);
- belief context: mean absolute error of p(Q_obs) per cell.
The interval method and the P4 margin are not yet approved, so no hypothesis decisions are made here.
"""
import argparse
import json
import math
import os
from collections import defaultdict
from statistics import NormalDist

from p2v3 import stats
from p2v3.score import score_attribution, score_belief

CONTRASTS = [("P1", "B", "none", "A", "none", "unsupported_q_obs"),
             ("P2", "B", "none", "D1", "none", "unsupported_q_obs"),
             ("P3", "C", "none", "B", "none", "unsupported_q_obs"),
             ("P4", "E_scope", "improved", "E", "improved", "correct_acceptance")]
COMPONENTS = ("unsupported_q_obs", "unsupported_q_cause", "unsupported_q_welfare", "unsupported_obs_or_cause")
VALIDITY = {"V1_correct_acceptance": ("correct_acceptance", [("E", "improved"), ("E_scope", "improved")]),
            "V2_correct_refutation": ("correct_refutation", [(c, d) for c in ("E", "E_scope")
                                                             for d in ("worsened", "unchanged")]),
            "V3_manipulation_check": ("manipulation_check", [(c, "none") for c in ("B", "C", "C_prime", "D1", "D2")])}
ROLES = {}  # every configuration is primary
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
            cells.append(stats.all_pairs_counts(list(ax.values()), list(ay.values()), fill))
        try:
            s = stats.summarize(cells)
            lo, hi = stats.tango(s, 0.025, conservative=True, cc=0.5)
            z0 = stats.tango_z(s, 0.0, conservative=True, cc=0.5)
            lo1, _ = stats.tango(s, 0.025, conservative=True, cc=0.5)  # one-sided 97.5% lower bound (P4)
            d_case = [(a10 - a01) / (a11 + a10 + a01 + a00) for a11, a10, a01, a00 in cells if a11 + a10 + a01 + a00]
            out[name] = {"estimate": stats.estimate(s), "ci95": [lo, hi], "lower_975_one_sided": lo1,
                         "cases": s.K, "cases_dropped": s.dropped,
                         "p_two_sided_vs_0": min(1.0, 2 * (1 - NormalDist().cdf(abs(z0)))),
                         "ci95_case_t": case_t(d_case), "case_differences": d_case}
        except ValueError as e:
            out[name] = {"estimate": None, "note": f"not estimable: {e}"}
    return out


def case_t(d):
    """Comparison interval: t over case-level differences (df = cases - 1); zero width if all equal."""
    if len(d) < 2:
        return None
    from statistics import mean, stdev
    from p2v3.tdist import t_quantile
    h = t_quantile(0.975, len(d) - 1) * stdev(d) / math.sqrt(len(d))
    return [mean(d) - h, mean(d) + h]


def decide(ci, sesoi):
    """Spec §1 rule, fixed before data: needs a prespecified SESOI; otherwise says so."""
    if not ci:
        return "not estimable"
    if sesoi is None:
        return "no decision: SESOI not set"
    lo, hi = ci
    if lo > sesoi:
        return "meaningful positive"
    if hi < -sesoi:
        return "meaningful negative"
    if -sesoi < lo and hi < sesoi:
        return "equivalent within SESOI"
    return "inconclusive"


def decide_ni(lower, margin):
    if lower is None:
        return "not estimable"
    if margin is None:
        return "no decision: P4 margin not set"
    return "noninferior" if lower > -margin else "noninferiority not shown"


def wilson(k, n, z=1.959964):
    if n == 0:
        return None
    p = k / n
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return [max(0.0, c - h), min(1.0, c + h)]


def validity_checks(mr):
    """Equal-case rate per cell for V1-V3; Wilson interval with n = cases (conservative)."""
    out = {}
    for name, (metric, cells) in VALIDITY.items():
        out[name] = {}
        for c, d in cells:
            per_case = defaultdict(list)
            for r in mr:
                if r["context"] == "attribution" and (r["condition"], r["direction"]) == (c, d):
                    v = (r["metrics"] or {}).get(metric)
                    if v is not None:
                        per_case[r["item_id"]].append(int(bool(v)))
            rates = [sum(v) / len(v) for v in per_case.values()]
            k = len(rates)
            rate = sum(rates) / k if k else None
            ci = case_t(rates) if k > 1 else None
            out[name][f"{c}/{d}"] = {"rate": rate, "cases": k, "trials": sum(map(len, per_case.values())),
                                     "ci95_case_t": [max(0.0, ci[0]), min(1.0, ci[1])] if ci else None,
                                     "degenerate": k > 1 and len(set(rates)) == 1}
    return out


def holm(pvals):
    named = sorted((p, k) for k, p in pvals.items() if p is not None)
    adj, run, m = {}, 0.0, len(named)
    for j, (p, k) in enumerate(named):
        run = max(run, min(1.0, (m - j) * p))
        adj[k] = run
    return adj


def analyse(rows):
    res = {"label": LABEL, "roles": ROLES, "models": {}}
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
            rt = r.get("reasoning_tokens")
            q["reasoning_tokens"]["none_reported" if rt is None else ("0" if rt == 0 else ">0")] += 1
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
                          for n, x, dx, y, dy, met in CONTRASTS},
            "components": {n: {comp: contrast(mr, x, dx, y, dy, comp)["observed"] for comp in COMPONENTS}
                           for n, x, dx, y, dy, met in CONTRASTS if met == "unsupported_q_obs"},
            "validity_checks": validity_checks(mr)}
        cs = res["models"][m]["contrasts"]
        adj = holm({n: cs[n]["observed"].get("p_two_sided_vs_0") for n in ("P1", "P2", "P3")})
        for n in ("P1", "P2", "P3"):
            cs[n]["observed"]["p_holm_P1_P3"] = adj.get(n)
    return res


def fmt3(v):
    return "–" if v is None else f"{v:.3f}"


def fmt(v):
    return "–" if v is None else f"{v:+.3f}"


def markdown(res):
    out = [f"# P2 pilot analysis", "", f"**{res['label']}**", ""]
    for m, r in res["models"].items():
        q = r["quality"]
        out += [f"## {m}" + (f" — {ROLES[m]}" if m in ROLES else ""), "", f"Calls {r['n_calls']}, spend ${r['spent_usd']:.4f}. Status {q['status']}. "
                f"Parse {q['parse']}. Truncated {q['truncated'].get('True', 0)}. "
                f"Served provider {q['served_provider']}; served model {q['served_model']}.", "",
                "| contrast | definition | estimate | 95% CI (provisional) | p vs 0 (Holm P1–P3) | worst–best bounds | cases |",
                "|---|---|---|---|---|---|---|"]
        for n, c in r["contrasts"].items():
            o, w, b = c["observed"], c["worst"], c["best"]
            ci = f"[{o['ci95'][0]:+.3f}, {o['ci95'][1]:+.3f}]" if o.get("ci95") else o.get("note", "–")
            pv = "lower bound only (margin open)" if n == "P4" else (
                "–" if o.get("p_two_sided_vs_0") is None else f"{o['p_two_sided_vs_0']:.2g} ({o.get('p_holm_P1_P3', float('nan')):.2g})")
            out.append(f"| {n} | {c['definition']} | {fmt(o.get('estimate'))} | {ci} | {pv} | "
                       f"{fmt(w.get('estimate'))} to {fmt(b.get('estimate'))} | {o.get('cases', '–')} |")
        out += ["", "Components (spec §6; only Q_obs is confirmatory):", "",
                "| contrast | " + " | ".join(COMPONENTS) + " |", "|---|" + "---|" * len(COMPONENTS)]
        for n, comps in r["components"].items():
            cellf = lambda o: (f"{fmt(o.get('estimate'))} [{o['ci95'][0]:+.3f}, {o['ci95'][1]:+.3f}]"
                               if o.get("ci95") else "–")
            out.append(f"| {n} | " + " | ".join(cellf(comps[k]) for k in COMPONENTS) + " |")
        out += ["", "Validity / positive controls (must pass before contrasts are read):", "",
                "| check | cell | rate | 95% CI over cases (t, clipped) | cases | trials |", "|---|---|---|---|---|---|"]
        for name, cells in r["validity_checks"].items():
            for cell, v in cells.items():
                ci = v["ci95_case_t"]
                out.append(f"| {name} | {cell} | {fmt3(v['rate'])} | "
                           f"{'–' if not ci else f'[{ci[0]:.3f}, {ci[1]:.3f}]' + (' (degenerate)' if v.get('degenerate') else '')} | {v['cases']} | {v['trials']} |")
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
    ap.add_argument("--run-dir", required=True, nargs="+")
    ap.add_argument("--out", help="output directory (default: the single --run-dir)")
    a = ap.parse_args()
    if len(a.run_dir) > 1 and not a.out:
        ap.error("--out is required with several --run-dir")
    out_dir = a.out or a.run_dir[0]
    os.makedirs(out_dir, exist_ok=True)
    rows = []
    for d in a.run_dir:
        with open(os.path.join(d, "responses.jsonl")) as f:
            rows += [json.loads(x) for x in f if x.strip()]
    rows = score_rows(rows)
    res = analyse(rows)
    res["run_dirs"], res["n_cases"] = a.run_dir, len({r["item_id"] for r in rows})
    with open(os.path.join(out_dir, "analysis.json"), "w") as f:
        json.dump(res, f, indent=1, sort_keys=True)
    with open(os.path.join(out_dir, "analysis.md"), "w") as f:
        f.write(markdown(res))
    print(markdown(res))


if __name__ == "__main__":
    main()
