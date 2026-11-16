"""Independent recomputation of the P2 primary contrasts from raw responses.jsonl (workstream B check).

Deliberately imports nothing from p2v3/ or analyze_p2.py: its own JSON extraction, its own Q_obs scoring rule
(Q_obs = established_true is unsupported everywhere except E/E_scope improved, GOLD_LABELS.md), its own case
aggregation and its own implementation of the all-pairs Tango score interval (deff = 1, continuity correction
0.5 on the count scale), written from Tango (1998). It then compares every number against analysis.json.

  python3 check_p2_independent.py --run-dir runs/p2_dev_eval_v1 runs/p2_ext_v1 --analysis runs/p2_batch1_combined

Exit status 0 if every compared value matches (tolerance 1e-9 for rates/estimates, 1e-6 for interval ends).
"""
import argparse
import json
import math
import os
import re
import sys
from collections import defaultdict
from statistics import NormalDist

ACCEPT_T = {("E", "improved"), ("E_scope", "improved")}
CONTRASTS = {"P1": (("B", "none"), ("A", "none"), "u"), "P2": (("B", "none"), ("D1", "none"), "u"),
             "P3": (("C", "none"), ("B", "none"), "u"), "P4": (("E_scope", "improved"), ("E", "improved"), "acc")}
VALID = ("established_true", "established_false", "not_established")


def first_json_object(text):
    """Different approach from p2v3.score.extract_json: raw_decode from every '{' after removing fences."""
    if not isinstance(text, str):
        return None
    t = re.sub(r"```(?:json)?", "", text)
    dec = json.JSONDecoder()
    for i, ch in enumerate(t):
        if ch == "{":
            try:
                obj, _ = dec.raw_decode(t, i)
            except ValueError:
                continue
            if isinstance(obj, dict):
                return obj
    return None


def q_obs_status(text):
    obj = first_json_object(text)
    if obj is None or not isinstance(obj.get("claims"), dict):
        return None
    e = obj["claims"].get("Q_obs")
    st = e.get("status") if isinstance(e, dict) else None
    return st if st in VALID else None


def outcome(row, kind):
    """kind 'u': unsupported Q_obs (1/0/None); 'acc': correct acceptance (Q_obs = T) in E/E_scope improved."""
    if row["status"] != "ok":
        return None
    st = q_obs_status(row["text"])
    if st is None:
        return None
    if kind == "acc":
        return int(st == "established_true")
    return int(st == "established_true" and (row["condition"], row["direction"]) not in ACCEPT_T)


def tango_cc_interval(rates, alpha=0.025, cc=0.5):
    """rates: list of (rate_x, rate_y) per case. All-pairs cells f10 = rx(1-ry), f01 = (1-rx)ry; N = cases."""
    n = len(rates)
    b = sum(x * (1 - y) for x, y in rates)
    c = sum((1 - x) * y for x, y in rates)

    def z(d0):
        a2 = 2 * n
        a1 = -b - c + (2 * n - b + c) * d0
        a0 = -c * d0 * (1 - d0)
        p01 = (-a1 + math.sqrt(max(a1 * a1 - 4 * a2 * a0, 0.0))) / (2 * a2)
        var = n * (2 * p01 + d0 - d0 * d0)
        num = b - c - n * d0
        num = math.copysign(max(abs(num) - cc, 0.0), num)
        if var <= 0:
            return math.copysign(math.inf, num) if num else 0.0
        return num / math.sqrt(var)

    zc = NormalDist().inv_cdf(1 - alpha)
    est = (b - c) / n

    def root(lo, hi, target):  # z is decreasing in d0
        for _ in range(200):
            mid = (lo + hi) / 2
            if z(mid) > target:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2

    e = 1e-12
    lo = -1.0 if z(-1 + e) <= zc else root(-1 + e, est, zc)
    hi = 1.0 if z(1 - e) >= -zc else root(est, 1 - e, -zc)
    return est, [lo, hi]


def load(run_dirs):
    rows, planned = [], defaultdict(set)
    for d in run_dirs:
        with open(os.path.join(d, "responses.jsonl")) as f:
            rows += [json.loads(x) for x in f if x.strip()]
        with open(os.path.join(d, "manifest.json")) as f:
            for k in json.load(f)["planned_keys"]:
                m, item, cond, dirn, ctx, rep = k.split("|")[:6]
                if ctx == "attribution":
                    planned[m].add((item, cond, dirn, int(rep[1:])))
    return rows, planned


def recompute(rows, planned):
    out = {}
    for m in sorted(planned):
        vals = defaultdict(dict)  # (cell) -> {(case, rep): outcome}
        for item, cond, dirn, rep in planned[m]:
            for kind in ("u", "acc"):
                vals[(cond, dirn, kind)][(item, rep)] = None
        for r in rows:
            if r["model"] != m or r["context"] != "attribution":
                continue
            for kind in ("u", "acc"):
                vals[(r["condition"], r["direction"], kind)][(r["item_id"], r["repeat"])] = outcome(r, kind)

        def case_rates(cell, kind, fill=None):
            per = defaultdict(list)
            for (case, rep), v in vals[(cell[0], cell[1], kind)].items():
                v = fill if v is None else v
                if v is not None:
                    per[case].append(v)
            return {k: sum(v) / len(v) for k, v in per.items() if v}

        res = {"contrasts": {}, "cells": {}}
        for name, (x, y, kind) in CONTRASTS.items():
            o = {}
            for label, fx, fy in (("observed", None, None), ("worst", 0, 1), ("best", 1, 0)):
                rx, ry = case_rates(x, kind, fx), case_rates(y, kind, fy)
                both = sorted(set(rx) & set(ry))
                if len(both) < 2:
                    o[label] = None
                    continue
                est, ci = tango_cc_interval([(rx[k], ry[k]) for k in both])
                o[label] = {"estimate": est, "ci95": ci, "cases": len(both)}
            res["contrasts"][name] = o
        for (cond, dirn, kind) in list(vals):
            if kind != "u":
                continue
            per = defaultdict(list)
            for (case, rep), v in vals[(cond, dirn, kind)].items():
                if v is not None:
                    per[case].append(v)
            K = len(per)
            ev = sum(map(sum, per.values()))
            kc = sum(1 for v in per.values() if any(v))
            res["cells"][f"{cond}/{dirn}"] = {
                "events": ev, "trials": sum(map(len, per.values())), "cases": K, "cases_with_event": kc,
                "rate": (sum(sum(v) / len(v) for v in per.values()) / K) if K else None,
                "upper95_cases_if_zero": (1 - 0.05 ** (1 / K)) if K and kc == 0 else None}
        out[m] = res
    return out


def compare(mine, analysis):
    bad, n = [], 0

    def chk(label, a, b, tol):
        nonlocal n
        n += 1
        if a is None or b is None:
            if a is not b:
                bad.append(f"{label}: independent {a} vs analysis {b}")
            return
        if abs(a - b) > tol:
            bad.append(f"{label}: independent {a} vs analysis {b}")

    for m, r in mine.items():
        am = analysis["models"][m]
        for name, o in r["contrasts"].items():
            for label in ("observed", "worst", "best"):
                a = am["contrasts"][name][label]
                if o[label] is None:
                    chk(f"{m} {name} {label} estimate", None, a.get("estimate"), 0)
                    continue
                chk(f"{m} {name} {label} estimate", o[label]["estimate"], a.get("estimate"), 1e-9)
                chk(f"{m} {name} {label} cases", o[label]["cases"], a.get("cases"), 0)
                for i in (0, 1):
                    chk(f"{m} {name} {label} ci95[{i}]", o[label]["ci95"][i], (a.get("ci95") or [None, None])[i], 1e-6)
        zb = am["zero_event_bounds"]["per_cell"]
        for cell, v in r["cells"].items():
            ar = am["outcome_rates_by_cell"][cell]["unsupported_q_obs"]
            if cell in ("E/improved", "E_scope/improved"):
                continue
            chk(f"{m} {cell} rate", v["rate"], ar["rate"], 1e-9)
            chk(f"{m} {cell} events", v["events"], zb[cell]["events"], 0)
            chk(f"{m} {cell} trials", v["trials"], zb[cell]["trials"], 0)
            chk(f"{m} {cell} cases", v["cases"], zb[cell]["cases"], 0)
            chk(f"{m} {cell} cases_with_event", v["cases_with_event"], zb[cell]["cases_with_event"], 0)
            if v["upper95_cases_if_zero"] is not None:
                chk(f"{m} {cell} upper95_cases", v["upper95_cases_if_zero"], zb[cell]["upper95_cases"], 1e-9)
    return n, bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", nargs="+", required=True)
    ap.add_argument("--analysis", required=True, help="directory with the analysis.json to check")
    ap.add_argument("--out", help="write the independent numbers here (json)")
    a = ap.parse_args()
    rows, planned = load(a.run_dir)
    mine = recompute(rows, planned)
    with open(os.path.join(a.analysis, "analysis.json")) as f:
        analysis = json.load(f)
    n, bad = compare(mine, analysis)
    for m, r in mine.items():
        line = "; ".join(f"{k} {v['observed']['estimate']:+.3f} [{v['observed']['ci95'][0]:+.3f}, "
                         f"{v['observed']['ci95'][1]:+.3f}] (worst {v['worst']['estimate']:+.3f}, best "
                         f"{v['best']['estimate']:+.3f})" if v["observed"] else f"{k} not estimable"
                         for k, v in r["contrasts"].items())
        print(f"{m}: {line}; V {r['cells']['V/none']['events']}/{r['cells']['V/none']['trials']} "
              f"rate {r['cells']['V/none']['rate']:.3f}")
    print(f"compared {n} values; mismatches {len(bad)}")
    for b in bad:
        print("  MISMATCH", b)
    if a.out:
        with open(a.out, "w") as f:
            json.dump({"compared": n, "mismatches": bad, "independent": mine}, f, indent=1, sort_keys=True)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
