"""Coverage re-check for the all-pairs per-case counts used by analyze_p2.py (no model calls).

    python3 sim_p2_allpairs.py [--reps 20000] [--workers 8] [--out sim_out]     (run from rev3/)

analyze_p2.py now builds each case's counts with stats.all_pairs_counts (every X repeat against every Y
repeat; repeat index carries no matching) and reads the interval from Tango-c with continuity correction
(stats.tango(s, 0.025, conservative=True, cc=0.5)). This script checks, on a reduced grid, that interval's
one-sided 97.5% lower-bound non-coverage (target <= 3%) and two-sided 95% coverage, against
  case_t        the case-level t interval over per-case differences (analyze_p2.case_t; df = cases - 1),
  index_tcc     Tango-c-cc on index-paired counts (stats.pair_counts; the superseded construction),
all on the same simulated data.

Data model (p2v3/simulate.py): case logit effect u_i ~ N(0, sd^2) shared by both arms; arm X (E_scope) and
arm Y (E) repeats are independent Bernoulli(expit(mu_a + u_i)) given u_i, with mu_a calibrated so the
marginal rate is exact. True Delta = p_X - p_Y. No missing outcomes on this grid.

Grid: Y acceptance 0.90 / 0.99 / 1.00; Delta 0 and -0.05 (X = Y + Delta); sd 0 / 1.5; 5 repeats;
cases 6 / 12 / 30 / 60. Fixed seed; deterministic for fixed --reps.
Writes <out>/sim_p2_allpairs<tag>.csv and <out>/sim_p2_allpairs<tag>_tables.md.
High within-case correlation scenario: --sds 3 5 --tag _highcorr (latent ICC sd^2 / (sd^2 + pi^2/3) = 0.73, 0.88).
"""
import argparse
import csv
import math
import os
import time
from multiprocessing import Pool
from statistics import mean, stdev

from p2v3 import stats
from p2v3.simulate import rng_for, simulate
from p2v3.tdist import t_quantile

SEED = 2026111661
ACCEPT = (0.90, 0.99, 1.00)
DELTAS = (0.0, -0.05)
SDS = (0.0, 1.5)
REPS = 5
CASES = (6, 12, 30, 60)
METHODS = ("allpairs_tcc", "case_t", "index_tcc")
LIMIT = 0.03
TQ = {k: t_quantile(0.975, k - 1) for k in CASES}


def case_t(d):
    h = TQ[len(d)] * stdev(d) / math.sqrt(len(d))
    m = mean(d)
    return m - h, m + h


def tcc(cells):
    try:
        s = stats.summarize(cells)
    except ValueError:
        return -1.0, 1.0
    return stats.tango(s, 0.025, conservative=True, cc=0.5)


def task(args):
    point, R = args
    pe, d, sd, n = point
    rng = rng_for(SEED, point)
    acc = {k: [0, 0, 0, 0.0, 0] for k in METHODS}  # lower miss, upper miss, both-cover, sum width, zero width
    for _ in range(R):
        data = simulate(rng, n, REPS, [(pe + d, pe)], sd)
        ap = [stats.all_pairs_counts(x, y) for x, y in data]
        ix = [stats.pair_counts(x, y) for x, y in data]
        diffs = [sum(x) / len(x) - sum(y) / len(y) for x, y in data]
        for k, (lo, hi) in (("allpairs_tcc", tcc(ap)), ("case_t", case_t(diffs)), ("index_tcc", tcc(ix))):
            v = acc[k]
            lm, um = lo > d + 1e-12, hi < d - 1e-12
            v[0] += lm
            v[1] += um
            v[2] += not (lm or um)
            v[3] += hi - lo
            v[4] += hi - lo < 1e-12
    return point, R, acc


def pct(x):
    return f"{100 * x:.2f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reps", type=int, default=20000)
    ap.add_argument("--workers", type=int, default=os.cpu_count())
    ap.add_argument("--out", default="sim_out")
    ap.add_argument("--sds", type=float, nargs="+", default=list(SDS),
                    help="case logit random-effect SDs (high within-case correlation: e.g. 3 5)")
    ap.add_argument("--tag", default="", help="suffix for output file names")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    points = [(pe, d, sd, n) for pe in ACCEPT for d in DELTAS for sd in a.sds for n in CASES]
    t0 = time.time()
    with Pool(a.workers) as pool:
        res = sorted(pool.map(task, [(p, a.reps) for p in points], chunksize=1))
    rows = []
    for (pe, d, sd, n), R, acc in res:
        for k in METHODS:
            lm, um, cov, w, z0 = acc[k]
            se = math.sqrt(max(lm / R * (1 - lm / R), 1e-12) / R)
            rows.append({"p_E": pe, "p_Escope": round(pe + d, 4), "delta": d, "sd": sd, "repeats": REPS, "cases": n,
                         "method": k, "R": R, "lower_noncov": lm / R, "lower_noncov_mcse": se,
                         "upper_noncov": um / R, "two_sided_cov": cov / R, "mean_width": w / R, "zero_width": z0 / R,
                         "lower_ok": lm / R <= LIMIT})
    with open(os.path.join(a.out, f"sim_p2_allpairs{a.tag}.csv"), "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=list(rows[0]))
        wr.writeheader()
        wr.writerows(rows)
    by = {(r["p_E"], r["delta"], r["sd"], r["cases"], r["method"]): r for r in rows}
    out = [f"Reps per point: {a.reps}; seed {SEED}; {len(points)} points; {time.time() - t0:.0f} s.", "",
           "One-sided 97.5% lower-bound non-coverage (%), target <= 3; two-sided 95% coverage (%) in brackets; "
           "mean width (pp) after the slash.", "",
           "| p_E | Δ | sd | cases | all-pairs Tango-c-cc | case t | index-paired Tango-c-cc |", "|---|---|---|---|---|---|---|"]
    for pe in ACCEPT:
        for d in DELTAS:
            for sd in a.sds:
                for n in CASES:
                    cells = []
                    for k in METHODS:
                        r = by[(pe, d, sd, n, k)]
                        flag = "**" if not r["lower_ok"] else ""
                        cells.append(f"{flag}{pct(r['lower_noncov'])}{flag} [{pct(r['two_sided_cov'])}] / "
                                     f"{100 * r['mean_width']:.1f}")
                    out.append(f"| {pe:.2f} | {d:+.2f} | {sd} | {n} | " + " | ".join(cells) + " |")
    out += ["", "Worst case per method over the grid:", "", "| method | max lower non-cov % (point) | "
            "min two-sided cov % (point) | points over 3% | zero-width share, max % |", "|---|---|---|---|---|"]
    for k in METHODS:
        rk = [r for r in rows if r["method"] == k]
        worst = max(rk, key=lambda r: r["lower_noncov"])
        low = min(rk, key=lambda r: r["two_sided_cov"])
        tag = lambda r: f"p_E {r['p_E']}, Δ {r['delta']:+}, sd {r['sd']}, K {r['cases']}"
        out.append(f"| {k} | {pct(worst['lower_noncov'])} ({tag(worst)}) | {pct(low['two_sided_cov'])} ({tag(low)}) | "
                   f"{sum(not r['lower_ok'] for r in rk)} / {len(rk)} | {pct(max(r['zero_width'] for r in rk))} |")
    with open(os.path.join(a.out, f"sim_p2_allpairs{a.tag}_tables.md"), "w") as f:
        f.write("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
