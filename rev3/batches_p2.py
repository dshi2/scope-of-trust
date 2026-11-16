"""Per-batch, pooled and between-batch P2 summary (spec §7a). Reads analysis.json files written by analyze_p2.py.

  python3 batches_p2.py --batch batch1=runs/p2_batch1_combined --batch ba=runs/p2_ba_analysis \
      --batch bb=runs/p2_bb_analysis --batch bc=runs/p2_bc_analysis --pooled runs/p2_all_batches \
      [--incomplete bc] --out runs/p2_all_batches

Spec §7a: every batch that completes is reported; the pooled estimate covers all completed batches and is read
only together with the per-batch estimates and a between-batch difference; an incomplete batch is reported as
incomplete and excluded. Batch 2 sets are later development batches, not replications.

Between-batch difference (descriptive): batch 2 (all completed batch-2 sets, cases concatenated) minus batch 1, on
case-level values (per-cell case rates from `cell_case_summary[cell].case_values`; per-contrast case differences
from `contrasts[P].observed.case_differences`). Cases are independent across batches, so the interval is Welch's t
over case-level values; `degenerate` when both groups have zero spread (zero width is not precision). Per-set
estimates are listed beside it. No test, no Holm: this is a consistency check, not a hypothesis.
"""
import argparse
import json
import math
import os
from statistics import mean, variance

from p2v3.tdist import t_quantile

CONTRASTS = ("P1", "P2", "P3", "P4")


def welch(x, y):
    """mean(y) - mean(x) with a Welch t 95% interval; x = batch 1 case values, y = batch 2 case values."""
    if len(x) < 2 or len(y) < 2:
        return {"difference": None, "note": "fewer than two cases in a group"}
    d = mean(y) - mean(x)
    vx, vy = variance(x) / len(x), variance(y) / len(y)
    se2 = vx + vy
    if se2 == 0:
        return {"difference": d, "ci95_welch": [d, d], "degenerate": True, "cases_batch1": len(x),
                "cases_batch2": len(y)}
    df = se2 ** 2 / ((vx ** 2 / (len(x) - 1) if vx else 0) + (vy ** 2 / (len(y) - 1) if vy else 0))
    h = t_quantile(0.975, df) * math.sqrt(se2)
    return {"difference": d, "ci95_welch": [d - h, d + h], "df": df, "degenerate": False,
            "cases_batch1": len(x), "cases_batch2": len(y)}


def cell_view(c):
    return {k: c.get(k) for k in ("equal_case_mean", "cases", "cases_scheduled", "events", "cases_with_event",
                                  "scored", "scheduled", "ci95_case_t", "degenerate", "zero_event_upper_case",
                                  "correct_here", "metric")}


def contrast_view(o):
    o = o["observed"]
    keep = ("estimate", "ci95", "lower_975_one_sided", "cases", "cases_dropped", "p_two_sided_vs_0", "p_holm_P1_P3",
            "ci95_case_t", "ci95_case_t_degenerate", "decision", "best_attainable_lower_975_at_these_cases")
    return {k: o.get(k) for k in keep}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", action="append", required=True, help="NAME=ANALYSIS_DIR; first is batch 1")
    ap.add_argument("--pooled", required=True)
    ap.add_argument("--incomplete", nargs="*", default=[], help="batch names that did not complete (excluded)")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    batches = [tuple(b.split("=", 1)) for b in a.batch]
    load = lambda d: json.load(open(os.path.join(d, "analysis.json")))
    data = {n: load(d) for n, d in batches if n not in a.incomplete}
    pooled = load(a.pooled)
    first = batches[0][0]
    later = [n for n, _ in batches[1:] if n not in a.incomplete]
    res = {"label": ("Spec §7a. Per-batch, pooled (completed batches only) and between-batch (batch 2 completed sets "
                     "- batch 1; Welch t over case-level values; descriptive). Development cases, not confirmatory; "
                     "batch 2 is later development batches, not replication."),
           "batches": {n: d for n, d in batches}, "completed": [first] + later, "incomplete": a.incomplete,
           "pooled_dir": a.pooled, "pooled_run_dirs": pooled.get("run_dirs"), "pooled_n_cases": pooled.get("n_cases"),
           "models": {}}
    for m in sorted(pooled["models"]):
        mm = {"per_batch": {}, "pooled": {}, "between_batch": {"cells": {}, "contrasts": {}}}
        for n, an in data.items():
            r = an["models"].get(m)
            if r is None:
                continue
            mm["per_batch"][n] = {"n_cases": an.get("n_cases"),
                                  "contrasts": {p: contrast_view(r["contrasts"][p]) for p in CONTRASTS},
                                  "cells": {c: cell_view(v) for c, v in r["cell_case_summary"].items()}}
        pr = pooled["models"][m]
        mm["pooled"] = {"contrasts": {p: contrast_view(pr["contrasts"][p]) for p in CONTRASTS},
                        "cells": {c: cell_view(v) for c, v in pr["cell_case_summary"].items()}}
        b1 = data[first]["models"].get(m)
        b2 = [data[n]["models"].get(m) for n in later if data[n]["models"].get(m)]
        if b1 and b2:
            for c in b1["cell_case_summary"]:
                x = list(b1["cell_case_summary"][c]["case_values"].values())
                y = [v for r in b2 for v in r["cell_case_summary"][c]["case_values"].values()]
                mm["between_batch"]["cells"][c] = welch(x, y)
            for p in CONTRASTS:
                x = b1["contrasts"][p]["observed"].get("case_differences") or []
                y = [v for r in b2 for v in (r["contrasts"][p]["observed"].get("case_differences") or [])]
                mm["between_batch"]["contrasts"][p] = welch(x, y)
        res["models"][m] = mm
    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, "between_batch.json"), "w") as f:
        json.dump(res, f, indent=1, sort_keys=True)
    md = markdown(res)
    with open(os.path.join(a.out, "between_batch.md"), "w") as f:
        f.write(md)
    print(md)


def f3(v, signed=False):
    return "–" if v is None else (f"{v:+.3f}" if signed else f"{v:.3f}")


def ci(c, signed=False):
    return "–" if not c else f"[{f3(c[0], signed)}, {f3(c[1], signed)}]"


def markdown(res):
    names = res["completed"]
    out = ["# P2 per-batch, pooled and between-batch (spec §7a)", "", res["label"], "",
           f"Completed: {', '.join(names)}. Incomplete (excluded): {', '.join(res['incomplete']) or 'none'}. "
           f"Pooled cases: {res['pooled_n_cases']}.", ""]
    for m, mm in res["models"].items():
        out += [f"## {m}", "", "Contrasts (estimate, all-pairs Tango-c-cc 95% CI provisional, cases):", "",
                "| contrast | " + " | ".join(names) + " | pooled | batch 2 − batch 1 (Welch, case level) |",
                "|---|" + "---|" * (len(names) + 2)]
        for p in CONTRASTS:
            cells = []
            for n in names + ["pooled"]:
                o = (mm["pooled"] if n == "pooled" else mm["per_batch"].get(n, {})).get("contrasts", {}).get(p)
                cells.append("–" if not o or o.get("estimate") is None else
                             f"{f3(o['estimate'], True)} {ci(o['ci95'], True)} K={o['cases']}")
            w = mm["between_batch"]["contrasts"].get(p, {})
            wb = "–" if w.get("difference") is None else (f"{f3(w['difference'], True)} {ci(w['ci95_welch'], True)}"
                                                         + (" (degenerate)" if w.get("degenerate") else ""))
            out.append(f"| {p} | " + " | ".join(cells) + f" | {wb} |")
        out += ["", "Unsupported Q_obs by cell (equal-case rate; cases with ≥ 1 event / cases; zero-event case bound). "
                "E/E_scope improved rows show correct acceptance instead:", "",
                "| cell | " + " | ".join(names) + " | pooled | batch 2 − batch 1 (Welch, case level) |",
                "|---|" + "---|" * (len(names) + 2)]
        for c in mm["pooled"]["cells"]:
            cells = []
            for n in names + ["pooled"]:
                v = (mm["pooled"] if n == "pooled" else mm["per_batch"].get(n, {})).get("cells", {}).get(c)
                if not v or v["equal_case_mean"] is None:
                    cells.append("–")
                    continue
                z = f"; ≤ {v['zero_event_upper_case']:.3f}" if v.get("zero_event_upper_case") is not None else ""
                cells.append(f"{v['equal_case_mean']:.3f} ({v['cases_with_event']}/{v['cases']}{z})"
                             + (" (correct acceptance)" if v.get("correct_here") else ""))
            w = mm["between_batch"]["cells"].get(c, {})
            wb = "–" if w.get("difference") is None else (f"{f3(w['difference'], True)} {ci(w['ci95_welch'], True)}"
                                                         + (" (degenerate)" if w.get("degenerate") else ""))
            out.append(f"| {c} | " + " | ".join(cells) + f" | {wb} |")
        out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    main()
