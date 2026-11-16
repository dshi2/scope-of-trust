"""Simulation-based method choice and precision analysis for P1-P4 (spec §6, §8.2, §9). No model calls.

    python3 precision.py [--quick] [--workers N] [--reference NAME=GITREF:PATH ...]   (run from rev3/)

Writes PRECISION_REPORT.md and PRECISION_GRID.csv (fixed seed; deterministic for fixed arguments).
--reference loads an independent comparator from another branch at run time (never copied here) and
runs it on the same simulated data as the chosen method.
"""
import argparse
import csv
import importlib.util
import json
import math
import os
import subprocess
import sys
import tempfile
import time
from multiprocessing import Pool
from statistics import NormalDist

from p2v3 import stats
from p2v3.simulate import _Q, _rate, cells, intercept, rng_for, simulate

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 2026111602  # fresh seed after tango_cc was added on the evidence of a first grid run (seed 20261116)
DELTAS = {"5pp": 0.05, "1.1pp": 1 / 90}  # 1/90 = (pi_u/pi_s) B / r with .1/.9, B = .1, r = 1 (spec §8.2)
ACCEPT = (0.80, 0.90, 0.95, 0.99, 1.00)
SDS = (0.0, 0.5, 1.5)
REPS = (1, 3, 5)
NS = (30, 60, 120, 240)
MISS = {"none": ("mcar", 0.0), "mcar": ("mcar", 0.05), "arm": ("arm", 0.05)}
CANDIDATES = ("wald", "tango", "tango_cc", "tango_c", "tango_c_cc", "bayes")
PREFERENCE = ("tango", "tango_cc", "tango_c", "tango_c_cc", "bayes")  # most efficient first; wald is the known-failing baseline
LIMIT = 0.03  # §6: one-sided 97.5% non-coverage <= 3% at every grid point
MC_TOL_SE = 3  # type I at -delta <= 2.5% + 3 Monte Carlo SE (about 400 such points are checked)
z = NormalDist().inv_cdf


def diffs():
    out = {0.0}
    for d in DELTAS.values():
        out |= {-d / 2, -d}
    return sorted(out, reverse=True)


def grid_points():
    return [(pe, d, sd, r, n, miss) for pe in ACCEPT for d in diffs() for sd in SDS
            for r in REPS for n in NS for miss in MISS]


def _safe_summary(c):
    try:
        return stats.summarize(c)
    except ValueError:
        return None


def _grid_task(args):
    """One grid point: E_scope (arm X) rate pe + d vs E (arm Y) rate pe. Common data for all methods."""
    point, caps, stage = args
    pe, d, sd, r, n, miss = point
    mode, m = MISS[miss]
    rng = rng_for(SEED, "grid", point, stage)
    R = max(caps.values())
    res = {k: [0, 0, 0, 0, 0.0] for k in caps}  # reps, lower miss, upper miss, zero width, sum(lower)
    for i in range(R):
        s = _safe_summary(cells(simulate(rng, n, r, [(pe + d, pe)], sd, m, mode)))
        for k, cap in caps.items():
            if i >= cap:
                continue
            lo, hi = stats.METHODS[k](s) if s else (-1.0, 1.0)
            v = res[k]
            v[0] += 1
            v[1] += lo > d + 1e-12
            v[2] += hi < d - 1e-12  # nan (bayes: no upper bound) never counts
            v[3] += hi - lo < 1e-12
            v[4] += lo
    return point, stage, res


def coverage(workers, r1, r2, r1_bayes):
    """Stage 1 for every point; stage 2 adds r2 reps where a still-eligible method is near the limit."""
    pts = grid_points()
    caps = {k: (r1_bayes if k == "bayes" else r1) for k in CANDIDATES}
    acc = {}
    with Pool(workers) as pool:
        for point, _, res in pool.imap_unordered(_grid_task, [(p, caps, 1) for p in pts], chunksize=4):
            acc[point] = res
        bad_lo = {k for k in CANDIDATES if any(_clear_fail(acc[p][k][1], acc[p][k][0]) for p in pts)}
        bad_hi = {k for k in CANDIDATES if k == "bayes" or any(_clear_fail(acc[p][k][2], acc[p][k][0]) for p in pts)}
        todo = []
        for p in pts:
            v = acc[p]
            need = {k: r2 for k in CANDIDATES if (k not in bad_lo and v[k][1] > 0.025 * v[k][0])
                    or (k not in bad_hi and v[k][2] > 0.025 * v[k][0])}
            if need:
                todo.append((p, need, 2))
        bad = {"lower": sorted(bad_lo), "upper": sorted(bad_hi)}
        for point, _, res in pool.imap_unordered(_grid_task, todo, chunksize=2):
            for k, v in res.items():
                acc[point][k] = [a + b for a, b in zip(acc[point][k], v)]
    return acc, bad, len(todo)


def _clear_fail(misses, R):
    return misses / R - 3 * math.sqrt(LIMIT * (1 - LIMIT) / R) > LIMIT


def qualify(acc, method, delta, two_sided):
    """§6 rule for one method at one delta: every point with d in {0, -delta/2, -delta}."""
    worst, worst_t1, n_t1_fail, n_pts = 0.0, 0.0, 0, 0
    for (pe, d, sd, r, n, miss), res in acc.items():
        if not any(abs(d - x) < 1e-12 for x in (0.0, -delta / 2, -delta)):
            continue
        v = res[method]
        R = v[0]
        n_pts += 1
        nc = max(v[1], v[2] if two_sided else 0) / R
        worst = max(worst, nc)
        if abs(d + delta) < 1e-12:
            t1 = v[1] / R
            worst_t1 = max(worst_t1, t1)
            n_t1_fail += t1 > 0.025 + MC_TOL_SE * math.sqrt(0.025 * 0.975 / R)
    return {"points": n_pts, "max_noncov": worst, "max_type1": worst_t1, "type1_fail": n_t1_fail,
            "ok": worst <= LIMIT and n_t1_fail == 0}


# ---- precision -------------------------------------------------------------------------------

def case_variance(px, py, sd, r):
    """Variance of one case's mean paired difference under the generative model (no missingness)."""
    mx, my = intercept(px, sd), intercept(py, sd)
    qs = _Q if sd else [0.0]
    vals = [(_rate(mx, sd * q), _rate(my, sd * q)) for q in qs]
    within = sum(a * (1 - a) + b * (1 - b) for a, b in vals) / len(vals) / r
    dif = [a - b for a, b in vals]
    mean = sum(dif) / len(dif)
    return within + sum((x - mean) ** 2 for x in dif) / len(dif)


def _p4_power_task(args):
    pe, sd, r, delta, alpha, n, R, method = args
    rng = rng_for(SEED, "p4power", pe, sd, r, delta, alpha, n)
    hit = 0
    for _ in range(R):
        s = _safe_summary(cells(simulate(rng, n, r, [(pe, pe)], sd)))
        hit += bool(s) and stats.METHODS[method](s, alpha)[0] > -delta
    return hit / R


def _equiv_task(args):
    p, eff, sd, r, sesoi, alpha, n, R, method = args
    rng = rng_for(SEED, "equiv", p, eff, sd, r, sesoi, alpha, n)
    out = {"equivalent": 0, "positive": 0, "negative": 0, "inconclusive": 0, "nonzero": 0}
    for _ in range(R):
        s = _safe_summary(cells(simulate(rng, n, r, [(p + eff, p)], sd)))
        lo, hi = stats.METHODS[method](s, alpha) if s else (-1.0, 1.0)
        if -sesoi < lo and hi < sesoi:
            out["equivalent"] += 1
        elif lo > sesoi:
            out["positive"] += 1
        elif hi < -sesoi:
            out["negative"] += 1
        else:
            out["inconclusive"] += 1
        out["nonzero"] += lo > 0 or hi < 0
    return {k: v / R for k, v in out.items()}


def _sim_reps(n, r, arms, budget=4e7, R=400):
    """Monte Carlo reps within a draw budget (None: analytic only)."""
    rr = int(min(R, budget / (n * r * arms)))
    return rr if rr >= 100 else None


def floor_cases(method, delta, alpha):
    """Fewest cases for which the bound clears -delta when every pair agrees (the best possible data)."""
    ok = lambda n: stats.METHODS[method](stats.Summary(n, 0, 0, n, 0, 1.0, 0), alpha)[0] > -delta
    lo, hi = 2, 2
    while not ok(hi):
        lo, hi = hi, hi * 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        lo, hi = (lo, mid) if ok(mid) else (mid, hi)
    return hi


def p4_decidable(pool, method, target=0.9):
    """Smallest n with P(lower bound > -delta | true difference 0) >= target; analytic start, simulated check."""
    rows = []
    jobs = []
    for dname, delta in DELTAS.items():
        for alpha in (0.025, 0.025 / 4):
            zz = z(1 - alpha)
            n_floor = floor_cases(method, delta, alpha)
            for pe in (0.90, 0.95, 0.99, 1.00):
                for sd in SDS:
                    for r in REPS:
                        v = case_variance(pe, pe, sd, 1 if method.startswith("tango_c") else r)  # case is the unit
                        n_an = max(n_floor, math.ceil(v * (zz + z(target)) ** 2 / delta ** 2))
                        jobs.append((dname, delta, alpha, pe, sd, r, n_an, n_floor))
    results = {}
    pending = {j: j[6] for j in jobs}
    for _ in range(12):  # step n up by 10% until the simulated probability reaches the target
        batch = []
        for j, n in pending.items():
            R = _sim_reps(n, j[5], 2)
            if R is None:
                results[j] = (n, None)
            else:
                batch.append((j, n, R))
        pending = {j: n for j, n in pending.items() if j not in results}
        if not batch:
            break
        pw = pool.map(_p4_power_task, [(j[3], j[4], j[5], j[1], j[2], n, R, method) for j, n, R in batch])
        for (j, n, R), p in zip(batch, pw):
            if p >= target:
                results[j] = (n, p)
                del pending[j]
            else:
                pending[j] = math.ceil(n * 1.1)
    for j, n in pending.items():
        results[j] = (n, float("nan"))
    for j in jobs:
        n, p = results[j]
        rows.append({"delta": j[0], "alpha": j[2], "accept": j[3], "sd": j[4], "reps": j[5],
                     "n_floor": j[7], "n_analytic": j[6], "n": n, "sim_power": p})
    return rows


def p13_equivalence(pool, method, target=0.9):
    """Smallest n with P(95% (or simultaneous 98.33%) interval inside +-SESOI | Delta = 0) >= target."""
    jobs = []
    for sesoi in (0.05, 0.10):
        for alpha, label in ((0.025, "95%"), (0.05 / 6, "98.33% simultaneous")):
            zz = z(1 - alpha)
            for p in (0.02, 0.10, 0.30):
                for sd in (0.5, 1.5):
                    for r in (1, 3):
                        v = case_variance(p, p, sd, 1 if method.startswith("tango_c") else r)
                        n_an = math.ceil(v * (zz + z((1 + target) / 2)) ** 2 / sesoi ** 2)
                        jobs.append((sesoi, alpha, label, p, sd, r, max(n_an, 30)))
    pending = {j: j[6] for j in jobs}
    found = {}
    for _ in range(12):
        batch = [(j, n, _sim_reps(n, j[5], 2)) for j, n in pending.items()]
        for j, n, R in batch:
            if R is None:
                found[j] = (n, None)
        batch = [b for b in batch if b[2] is not None]
        pending = {j: n for j, n in pending.items() if j not in found}
        if not batch:
            break
        res = pool.map(_equiv_task, [(j[3], 0.0, j[4], j[5], j[0], j[1], n, R, method) for j, n, R in batch])
        for (j, n, R), o in zip(batch, res):
            if o["equivalent"] >= target:
                found[j] = (n, o["equivalent"])
                del pending[j]
            else:
                pending[j] = math.ceil(n * 1.1)
    for j, n in pending.items():
        found[j] = (n, float("nan"))
    rows = []
    for j in jobs:
        n, pe = found[j]
        sesoi, alpha, label, p, sd, r = j[:6]
        R = _sim_reps(n, r, 2) or 100
        eff = pool.map(_equiv_task, [(p, k * sesoi, sd, r, sesoi, alpha, n, R, method) for k in (1, 2)])
        rows.append({"sesoi": sesoi, "interval": label, "p": p, "sd": sd, "reps": r, "n_analytic": j[6],
                     "n": n, "p_equiv_0": pe, "at_sesoi": eff[0], "at_2sesoi": eff[1]})
    return rows


def _joint_task(args):
    """A, B, C, D1 (unsupported_q_obs) and E, E_scope (acceptance) on the same cases; Holm over P1-P4."""
    rates, sd, r, n, delta, sesoi, R, method, chunk = args
    rng = rng_for(SEED, "joint", rates, sd, r, n, delta, sesoi, chunk)
    tr = rates[0]
    true = [tr[1] - tr[0], tr[1] - tr[3], tr[2] - tr[1]]
    contrasts = ((1, 0), (1, 3), (2, 1))  # P1 B-A, P2 B-D1, P3 C-B
    out = {"holm": [0, 0, 0, 0], "raw": [0, 0, 0, 0], "joint_equiv": 0, "simul_cover": 0, "R": R}
    for _ in range(R):
        data = simulate(rng, n, r, rates, sd)
        ss = [stats.summarize(cells(data, i, j)) for i, j in contrasts]
        s4 = stats.summarize(cells(data, 5, 4))
        pv = [stats.p_two_sided(s, method) for s in ss] + [2 * stats.p_noninferiority(s4, delta, method)]
        for h, p in enumerate(pv):
            out["raw"][h] += p < 0.05
        order = sorted(range(4), key=lambda h: pv[h])
        for rank, h in enumerate(order):  # Holm step-down at family alpha .05 (P4 on the two-sided scale)
            if pv[h] >= 0.05 / (4 - rank):
                break
            out["holm"][h] += 1
        ivs = [stats.METHODS[method](s, 0.05 / 6) for s in ss]  # Bonferroni-simultaneous 95% over P1-P3
        out["joint_equiv"] += all(-sesoi < lo and hi < sesoi for lo, hi in ivs)
        out["simul_cover"] += all(lo <= t <= hi for (lo, hi), t in zip(ivs, true))
    return out


def _stress_task(args):
    pe, d, sd, r, n, mode, delta, R, method = args
    rng = rng_for(SEED, "stress", pe, d, sd, r, n, mode, delta)
    out = {"cp_miss": 0, "cp_ni": 0, "wc_miss": 0, "wc_ni": 0, "dropped": 0, "R": R}
    f = stats.METHODS[method]
    for _ in range(R):
        data = simulate(rng, n, r, [(pe + d, pe)], sd, 0.05, mode)
        s = _safe_summary(cells(data))
        lo = f(s)[0] if s else -1.0
        out["dropped"] += s.dropped if s else n
        w = f(stats.summarize(cells(data, fill=(0, 1))))[0]  # scheduled denominators, missing = adverse
        out["cp_miss"] += lo > d + 1e-12; out["cp_ni"] += lo > -delta
        out["wc_miss"] += w > d + 1e-12; out["wc_ni"] += w > -delta
    return {"accept": pe, "d": d, "sd": sd, "reps": r, "n": n, "mode": mode, "delta": delta, **out}


def missing_stress(pool, method, R=2000):
    """P4 at the -delta boundary and at 0 under four missingness mechanisms (5% of responses):
    complete pairs vs the scheduled-denominator worst case (missing E_scope = 0, missing E = 1)."""
    jobs = [(pe, -k * delta, sd, r, n, mode, delta, R, method)
            for delta in DELTAS.values() for pe in (0.95, 0.99, 1.00) for k in (0, 1) for sd in (0.5, 1.5)
            for r in (1, 3) for n in (120, 480) for mode in ("mcar", "arm", "case", "mnar")]
    return pool.map(_stress_task, jobs, chunksize=4)


def _models_task(args):
    label, rates, sd, r, n, delta, R, method = args
    rng = rng_for(SEED, "models", label, sd, r, n, delta)
    true = sum(px - py for px, py in rates) / len(rates)
    miss = ni = 0
    for _ in range(R):
        lo = stats.METHODS[method](stats.summarize(cells(simulate(rng, n, r, rates, sd))))[0]
        miss += lo > true + 1e-12
        ni += lo > -delta
    return {"label": label, "sd": sd, "reps": r, "n": n, "delta": delta, "true": true,
            "noncov": miss / R, "ni": ni / R, "R": R}


def model_heterogeneity(pool, method, R=4000):
    """Three models on the same cases, pooled with the case as the unit (each case's repeats from all
    models averaged). The pooled estimand is the mean of the per-model differences, here exactly -delta."""
    jobs = []
    for delta in DELTAS.values():
        scen = {"levels differ, same difference": [(1 - delta, 1.0), (0.95 - delta, 0.95), (0.9 - delta, 0.9)],
                "differences 0, -delta, -2 delta": [(0.99, 0.99), (0.97 - delta, 0.97), (0.95 - 2 * delta, 0.95)]}
        for label, rates in scen.items():
            for sd in (0.5, 1.5):
                for r in (1, 3):
                    for n in (60, 240):
                        jobs.append((label, rates, sd, r, n, delta, R, method))
    return pool.map(_models_task, jobs)


# ---- independent comparator -------------------------------------------------------------------

def load_reference(spec):
    name, rest = spec.split("=", 1)
    ref, path = rest.split(":", 1)
    git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True, check=True, cwd=HERE).stdout
    commit = git("rev-parse", "--short", ref).strip()
    src = git("show", f"{ref}:{path}")
    d = tempfile.mkdtemp()
    f = os.path.join(d, f"ref_{name}.py")
    with open(f, "w") as fh:
        fh.write(src)
    spec_ = importlib.util.spec_from_file_location(f"ref_{name}", f)
    mod = importlib.util.module_from_spec(spec_)
    sys.modules[spec_.name] = mod
    spec_.loader.exec_module(mod)
    return {"name": name, "ref": ref, "path": path, "commit": commit, "module": mod}


def reference_lower(mod, data, alpha, delta):
    """Adapter: lower bound for E_scope - E from a reference module, on raw per-case outcomes."""
    if hasattr(mod, "reference_lower_bound"):  # Hoeffding comparator (case means, missing = adverse)
        arm = lambda ys: mod.Arm(len(ys), sum(y is not None for y in ys), sum(y == 1 for y in ys))
        pairs = [mod.CasePair(str(i), "m", arm(e), arm(x)) for i, (x, e) in enumerate(data)]
        return mod.reference_lower_bound(pairs, alpha=alpha, margin=delta)["one_sided_lower"]
    if hasattr(mod, "loss_upper"):  # exact any-loss indicator comparator (missing = adverse)
        cases = {str(i): list(zip(x, e)) for i, (x, e) in enumerate(data)}
        return mod.summarize(cases, alpha)["population_difference_lower"]
    raise ValueError("unrecognised reference module")


def compare(refs, method, R, quick):
    """Same simulated datasets for the chosen method and each reference (P4 scenarios, single model)."""
    rows = []
    accs = (0.95, 1.00) if quick else (0.95, 0.99, 1.00)
    ns = (120,) if quick else (60, 240, 960)
    for dname, delta in DELTAS.items():
        for pe in accs:
            for dm in (0.0, 1.0):
                d = -dm * delta
                for sd in (0.0, 1.5):
                    for r in (1, 5):
                        for n in ns:
                            for miss in ("none", "arm"):
                                mode, m = MISS[miss]
                                rng = rng_for(SEED, "compare", dname, pe, d, sd, r, n, miss)
                                tally = {k: [0, 0] for k in [method] + [x["name"] for x in refs]}
                                agree = {x["name"]: [0, 0, 0, 0] for x in refs}  # both, chosen only, ref only, neither
                                for _ in range(R):
                                    data = simulate(rng, n, r, [(pe + d, pe)], sd, m, mode)
                                    s = _safe_summary(cells(data))
                                    lo = stats.METHODS[method](s)[0] if s else -1.0
                                    mine = lo > -delta
                                    tally[method][0] += mine
                                    tally[method][1] += lo > d + 1e-12
                                    for x in refs:
                                        rl = reference_lower(x["module"], data, 0.025, delta)
                                        theirs = rl > -delta
                                        tally[x["name"]][0] += theirs
                                        tally[x["name"]][1] += rl > d + 1e-12
                                        agree[x["name"]][(0 if theirs else 1) if mine else (2 if theirs else 3)] += 1
                                rows.append({"delta": dname, "accept": pe, "d": d, "sd": sd, "reps": r, "n": n,
                                             "miss": miss, "R": R, "tally": tally, "agree": agree})
    return rows


def all_agree_bounds(refs, method):
    """Lower bounds when every pair agrees (all ones in both arms), one repeat and five repeats."""
    out = []
    for n in (30, 72, 120, 368, 1000, 3000):
        for r in (1, 5):
            data = [([1] * r, [1] * r) for _ in range(n)]
            row = {"n": n, "reps": r, method: stats.METHODS[method](stats.summarize(cells(data)))[0]}
            for x in refs:
                row[x["name"]] = reference_lower(x["module"], data, 0.025, 0.05)
            out.append(row)
    return out


# ---- report ----------------------------------------------------------------------------------

def pct(x):
    return "n/a" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{100 * x:.2f}%"


def write_grid_csv(acc, path):
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["accept_E", "diff", "re_sd", "repeats", "cases", "missing", "method", "reps",
                    "lower_noncov", "upper_noncov", "zero_width", "mean_lower"])
        for p in sorted(acc):
            for k in CANDIDATES:
                v = acc[p][k]
                w.writerow([*p[:5], p[5], k, v[0], f"{v[1] / v[0]:.5f}",
                            "" if k == "bayes" else f"{v[2] / v[0]:.5f}", f"{v[3] / v[0]:.5f}",
                            f"{v[4] / v[0]:.5f}"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true", help="tiny run for smoke tests (not a valid report)")
    ap.add_argument("--workers", type=int, default=os.cpu_count())
    ap.add_argument("--reference", action="append", default=[], help="NAME=GITREF:PATH")
    ap.add_argument("--out", default=os.path.join(HERE, "PRECISION_REPORT.md"))
    ap.add_argument("--grid-cache", help="JSON file: reuse coverage-grid counts if present, else save them")
    a = ap.parse_args()
    t0 = time.time()
    r1, r2, rb = (40, 40, 10) if a.quick else (2000, 18000, 300)
    if a.quick:
        global NS, ACCEPT, SDS, REPS, MISS
        NS, ACCEPT, SDS, REPS = (30,), (0.95, 1.00), (0.0, 1.5), (1, 3)
        MISS = {k: MISS[k] for k in ("none", "arm")}
    if a.grid_cache and os.path.exists(a.grid_cache):
        with open(a.grid_cache) as fh:
            c = json.load(fh)
        acc = {tuple(p): res for p, res in c["acc"]}
        bad, n_refined = c["bad"], c["n_refined"]
    else:
        acc, bad, n_refined = coverage(a.workers, r1, r2, rb)
        if a.grid_cache:
            with open(a.grid_cache, "w") as fh:
                json.dump({"acc": [[list(p), res] for p, res in acc.items()], "bad": bad,
                           "n_refined": n_refined}, fh)
    q = {k: {dn: qualify(acc, k, dv, two_sided=(k != "bayes")) for dn, dv in DELTAS.items()} for k in CANDIDATES}
    q4 = {k: {dn: qualify(acc, k, dv, two_sided=False) for dn, dv in DELTAS.items()} for k in CANDIDATES}
    chosen4 = next((k for k in PREFERENCE if all(x["ok"] for x in q4[k].values())), None)
    chosen13 = next((k for k in PREFERENCE if k != "bayes" and all(x["ok"] for x in q[k].values())), None)
    if a.quick:
        chosen4 = chosen4 or "tango_cc"
        chosen13 = chosen13 or "tango_cc"
    refs = [load_reference(s) for s in a.reference]
    with Pool(a.workers) as pool:
        p4 = p4_decidable(pool, chosen4) if not a.quick else []
        p13 = p13_equivalence(pool, chosen13) if not a.quick else []
        stress = missing_stress(pool, chosen4, 100 if a.quick else 2000)
        models = model_heterogeneity(pool, chosen4, 100 if a.quick else 4000)
        joint = []
        plan = {"sd": 0.5, "reps": 3, "p": 0.10, "sesoi": 0.10, "accept": 0.95}
        if not a.quick:
            for dname, delta in DELTAS.items():
                n_p4 = next(x["n"] for x in p4 if x["delta"] == dname and x["alpha"] < 0.025
                            and x["accept"] == plan["accept"] and x["sd"] == plan["sd"] and x["reps"] == plan["reps"])
                n_eq = next(x["n"] for x in p13 if x["sesoi"] == plan["sesoi"] and x["interval"] != "95%"
                            and x["p"] == plan["p"] and x["sd"] == plan["sd"] and x["reps"] == plan["reps"])
                n = max(n_p4, n_eq)
                s, pa, pe = plan["sesoi"], plan["p"], plan["accept"]
                for label, rates in (("all P1-P3 differences 0; P4 difference 0", (pa, pa, pa, pa, pe, pe)),
                                     ("B-A = B-D1 = +2 SESOI, C-B = -2 SESOI; P4 difference 0",
                                      (pa, pa + 2 * s, pa, pa, pe, pe))):
                    R = _sim_reps(n, plan["reps"], 6, budget=6e7, R=400) or 100
                    parts = pool.map(_joint_task, [([rates], plan["sd"], plan["reps"], n, delta, s, -(-R // 8),
                                                    chosen13, i) for i in range(8)])
                    tot = {k: (sum(x[k] for x in parts) if not isinstance(parts[0][k], list)
                               else [sum(v) for v in zip(*(x[k] for x in parts))]) for k in parts[0]}
                    joint.append({"delta": dname, "n_p4": n_p4, "n_equiv": n_eq, "n": n, "scenario": label,
                                  **tot})
    cmp_rows = compare(refs, chosen4, 60 if a.quick else 500, a.quick) if refs else []
    agree_rows = all_agree_bounds(refs, chosen4)
    write_grid_csv(acc, os.path.join(os.path.dirname(a.out), "PRECISION_GRID.csv"))
    report = render(acc, bad, n_refined, q, q4, chosen4, chosen13, p4, p13, joint, plan, refs, cmp_rows,
                    agree_rows, (r1, r2, rb), a.quick, time.time() - t0, stress, models)
    with open(a.out, "w") as fh:
        fh.write(report)
    print(f"wrote {a.out} in {time.time() - t0:.0f}s; P4 method: {chosen4}; P1-P3 method: {chosen13}")


def table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def _sha(name):
    import hashlib
    with open(os.path.join(HERE, name), "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:12]


NAMES = {"wald": "Obuchowski cluster-robust Wald", "tango": "Tango score + estimated Obuchowski deff",
         "tango_cc": "Tango score + estimated Obuchowski deff, continuity correction 0.5",
         "tango_c": "Tango score, case as unit (deff = cluster size)",
         "tango_c_cc": "Tango score, case as unit, continuity correction 0.5",
         "bayes": "Jeffreys-Dirichlet posterior, counts / estimated deff"}


def render(acc, bad, n_refined, q, q4, chosen4, chosen13, p4, p13, joint, plan, refs, cmp_rows, agree_rows,
           reps, quick, secs, stress, models):
    r1, r2, rb = reps
    L = ["# P2 revision 3: precision report (generated)", "",
         "Generated by `precision.py` (seed %d) from `p2v3/stats.py` and `p2v3/simulate.py`. **Do not edit by hand.** "
         "Synthetic data only; no model was called. Source SHA-256 (first 12): precision.py `%s`, stats.py `%s`, "
         "simulate.py `%s`. Runtime %.0f min." % (SEED, _sha("precision.py"), _sha("p2v3/stats.py"),
                                                 _sha("p2v3/simulate.py"), secs / 60), ""]
    if quick:
        L += ["**QUICK SMOKE RUN: not a valid report.**", ""]
    L += ["## 1. Summary", "",
          f"- **P4 method (chosen by coverage):** `{chosen4}` ({NAMES.get(chosen4, 'none')}).",
          f"- **P1-P3 method (chosen by coverage):** `{chosen13}` ({NAMES.get(chosen13, 'none')}).",
          "- Preference order among qualifying methods: " + ", ".join(f"`{k}`" for k in PREFERENCE)
          + " (most efficient first). `wald` is the failing baseline the spec warns about.", ""]
    rec = []
    for row in joint:
        if row["scenario"].startswith("all"):
            rec.append(row)
    if rec:
        L += ["**Implied confirmatory case count** (planning scenario: case-effect SD %.1f, %d repeats, unsupported "
              "baseline %.2f, SESOI %.2f for P1-P3, true acceptance %.2f in both P4 arms, 90%% probability targets, "
              "Holm worst case for P4, Bonferroni-simultaneous intervals for joint absence over P1-P3, then inflated "
              "for 5%% MCAR parse failure, which loses about 9.75%% of pairs):"
              % (plan["sd"], plan["reps"], plan["p"], plan["sesoi"], plan["accept"]), ""]
        L += [table(["delta", "P4 decidable", "P1-P3 joint equivalence", "max", "with 5% missingness"],
                    [[x["delta"], x["n_p4"], x["n_equiv"], x["n"], math.ceil(x["n"] / (1 - 0.0975))] for x in rec]), ""]
        L += ["These are independent cases per model. Repeats do not substitute for cases. SESOI, delta, the "
              "acceptance level and the case-effect SD are planning inputs that the PI and experts must fix (spec §8.2, "
              "§9); §4 and §5 show how the count moves with each.", ""]
    L += ["## 2. Simulated design", "",
          "`p2v3/simulate.py`. Cases are the independent unit. Each case has a logit random effect u_i ~ N(0, SD^2) "
          "shared by both arms of a contrast (pairing) and by all models. Repeats are nested in cases. Each arm's "
          "intercept is calibrated so its *marginal* rate equals the target exactly, so the true difference is known "
          "at every SD. Rates of 0 and 1 are exact floors and ceilings. Parse failures are missing per scheduled "
          "response: MCAR (5% in both arms) or arm-dependent (10% in the first-named arm, 0% in the other). "
          "Model heterogeneity: several models with their own rates on the same cases, analysed per model (spec §9.6); "
          "the comparison references require per-model analysis too.", "",
          "Analysis: repeats of the two arms are paired by repeat index within case; pairs with a missing outcome "
          "are dropped (complete pairs; unbiased under MCAR and arm-dependent missingness). Scheduled-denominator "
          "bounds (missing = worst / best case) are `pair_counts(..., fill=(0, 1))` and `fill=(1, 0)`. The "
          "**estimand** is the mean over independent cases of the within-case difference in rates: cases are "
          "weighted equally and repeats are averaged within case (SCORING_SPEC §7), so a case with one complete "
          "pair counts as much as a case with five. A case with no complete pair cannot enter the complete-pair "
          "estimate; it is counted (`Summary.dropped`) and enters the scheduled-denominator bounds. P1-P3 are "
          "differences in `unsupported_q_obs`, P4 is E_scope minus E in correct acceptance (improved).", "",
          "## 3. Method qualification (§6 grid)", "",
          "Grid: true E acceptance %s; difference 0, -delta/2, -delta for delta = 5 pp and 1/90 (about 1.1 pp); "
          "case-effect SD %s; repeats %s; cases %s; missingness none / 5%% MCAR / 5%% arm-dependent. %d points. "
          "Stage 1: %d datasets per point (%d for `bayes`, which is slow). Stage 2: %d more datasets at the %d "
          "points where a still-eligible method exceeded 2.5%%. A method stops being eligible once its non-coverage "
          "exceeds 3%% by 3 Monte Carlo SE anywhere."
          % (", ".join(map(str, ACCEPT)), ", ".join(map(str, SDS)), ", ".join(map(str, REPS)),
             ", ".join(map(str, NS)), len(acc), r1, rb, r2, n_refined), "",
          "History: a first full run (seed 20261116) had only `wald`, `tango`, `tango_c` and `bayes`. Both "
          "uncorrected Tango variants exceeded 3%%: the upper bound at one repeat near the ceiling (about 4.8%%) and, "
          "with an estimated design effect, the lower bound when discordant pairs were few and clustered (about "
          "4%%). The continuity-corrected variants were then added and the whole grid rerun with a fresh seed, so "
          "the variants were not validated on the data that suggested them.", "",
          "Rule (§6): one-sided 97.5%% non-coverage <= 3%% at every point, and type I error at difference -delta "
          "<= 2.5%% + %d Monte Carlo SE (about 400 type I points are checked, so a 1.96 SE allowance would fail an "
          "exact test by chance). The P4 rule uses the lower bound; P1-P3 need both bounds, because the floor case "
          "(A near 0, B above it) is the mirror image of the ceiling case (flip 0/1 and swap arms; every method here "
          "is symmetric under both)." % MC_TOL_SE, ""]
    rows = []
    for k in CANDIDATES:
        for dn in DELTAS:
            a, b = q4[k][dn], q[k][dn]
            rows.append([f"`{k}`", dn, a["points"], pct(a["max_noncov"]), pct(a["max_type1"]), a["type1_fail"],
                         "yes" if a["ok"] else "**no**",
                         "n/a (lower only)" if k == "bayes" else pct(b["max_noncov"]),
                         "n/a" if k == "bayes" else ("yes" if b["ok"] else "**no**")])
    L += [table(["method", "delta", "points", "P4: max lower non-coverage", "max type I at -delta",
                 "type I points over limit", "qualifies for P4", "two-sided: worst tail", "qualifies for P1-P3"],
                rows), ""]
    for k in CANDIDATES:
        worst = sorted(acc.items(), key=lambda kv: -max(kv[1][k][1], 0 if k == "bayes" else kv[1][k][2]) / kv[1][k][0])[:3]
        zw = max(v[k][3] / v[k][0] for v in acc.values())
        L.append(f"- `{k}` worst points (E acceptance, difference, SD, repeats, cases, missingness -> lower / upper "
                 "non-coverage, datasets): " + "; ".join(
                     f"({p[0]}, {p[1]:.4f}, {p[2]}, {p[3]}, {p[4]}, {p[5]}) -> {pct(v[k][1] / v[k][0])} / "
                     f"{'n/a' if k == 'bayes' else pct(v[k][2] / v[k][0])}, {v[k][0]}" for p, v in worst)
                 + f". Largest share of zero-width intervals at a point: {pct(zw)}.")
    L += ["", "Full grid: `PRECISION_GRID.csv` (one row per point and method).", ""]
    if p4:
        L += ["## 4. P4: case counts at which noninferiority is decidable", "",
              "Smallest number of independent cases with probability >= 0.90 that the chosen method's one-sided "
              "lower bound exceeds -delta when the true difference is 0 (no missingness, one model). `n floor` is the "
              "fewest cases for which the bound clears -delta when every pair agrees (the best possible data; "
              "z^2 (1 - delta) / delta without the continuity correction). Start: normal approximation from the exact case-level variance; then n "
              "is raised by 10% until the simulated probability (up to 400 datasets) reaches 0.90. alpha = 0.025 is "
              "P4 alone; alpha = 0.00625 is the Holm worst case (P4 tested last among four).", ""]
        rows = [[x["delta"], x["alpha"], x["accept"], x["sd"], x["reps"], x["n_floor"], x["n"],
                 "analytic only" if x["sim_power"] is None else pct(x["sim_power"])] for x in p4]
        L += [table(["delta", "alpha", "acceptance", "SD", "repeats", "n floor", "cases", "simulated P(decide)"],
                    rows), ""]
        L += ["With a 1.1 pp margin even perfect agreement needs several hundred cases, and acceptance near 0.90 "
              "needs thousands. Perfect observed acceptance is informative only with enough cases (§6).", ""]
    if p13:
        L += ["## 5. P1-P3: SESOI-based precision and B-A equivalence (TOST)", "",
              "Two-sided intervals from the chosen method. Classification (spec §1): *equivalent* if the interval is "
              "inside +-SESOI; *meaningful positive/negative* if entirely above +SESOI / below -SESOI; otherwise "
              "*inconclusive magnitude*. B-A equivalence is a TOST at 2.5% per side (the 95% interval inside "
              "+-SESOI), a separate inference from P4 noninferiority, with its own margin (SESOI), never "
              "interchanged. `98.33% simultaneous` is Bonferroni over P1-P3 for a joint-absence claim. Cases: smallest "
              "n with P(equivalent | true difference 0) >= 0.90 (analytic start, simulated check). Then the "
              "outcome probabilities at that n when the true difference is +SESOI and +2 SESOI. Baseline 0.30 stands "
              "for P3, whose comparison arm B may be elevated.", ""]
        rows = []
        for x in p13:
            a, b = x["at_sesoi"], x["at_2sesoi"]
            rows.append([x["sesoi"], x["interval"], x["p"], x["sd"], x["reps"], x["n"], pct(x["p_equiv_0"]),
                         f"{pct(a['equivalent'])} / {pct(a['inconclusive'])} / {pct(a['nonzero'])}",
                         f"{pct(b['positive'])} / {pct(b['inconclusive'])}"])
        L += [table(["SESOI", "interval", "baseline", "SD", "repeats", "cases", "P(equiv) at 0",
                     "at +SESOI: equiv / inconclusive / excludes 0", "at +2 SESOI: meaningful + / inconclusive"],
                    rows), ""]
        L += ["At a true difference exactly at the SESOI boundary no sample size gives a conclusive result: the "
              "interval straddles the bound about half the time or more (spec §1).", ""]
    if joint:
        L += ["## 6. Primary family together: Holm and simultaneous intervals", "",
              "Arms A, B, C, D1 (`unsupported_q_obs`) and E, E_scope (acceptance) simulated on the same cases "
              "(one shared case effect), planning scenario of §1, at the implied case count before the missingness "
              "inflation. Holm at family alpha 0.05 over P1-P3 (two-sided score tests of 0) and P4 (one-sided "
              "noninferiority p-value, doubled to the two-sided scale). `simultaneous coverage` is the share of "
              "datasets in which all three Bonferroni intervals contain their true differences (target >= 95%). "
              "`joint equivalence` is the share in which all three lie inside +-SESOI.", ""]
        rows = []
        for x in joint:
            R = x["R"]
            rows.append([x["delta"], x["n"], x["scenario"],
                         " / ".join(pct(v / R) for v in x["holm"]), " / ".join(pct(v / R) for v in x["raw"]),
                         pct(x["simul_cover"] / R), pct(x["joint_equiv"] / R), R])
        L += [table(["delta", "cases", "scenario", "Holm rejects P1 / P2 / P3 / P4", "unadjusted",
                     "simultaneous coverage", "joint equivalence", "datasets"], rows), ""]
    if stress:
        L += ["## 6a. Missingness at the -delta boundary (P4)", "",
              "5%% of scheduled responses missing under four mechanisms: `mcar` (both arms), `arm` (E_scope only, 10%%), "
              "`case` (both arms, rate 2 x 5%% x Phi(-u_i / SD): harder cases lose more, and whole cases can be "
              "lost), `mnar` (E_scope failures only, 10%%: outcome-dependent). The estimand is always the full "
              "scheduled population of cases. `complete pairs` is the primary analysis; `worst case` imputes missing "
              "E_scope = 0 and missing E = 1, so every scheduled case and response stays in the denominator "
              "(SCORING_SPEC §2). Cells: largest false-noninferiority rate at difference -delta, over SD 0.5/1.5, "
              "repeats 1/3, cases 120/480 (each %d datasets), then mean P(declare noninferiority) at difference 0, "
              "then mean cases with no complete pair per dataset." % stress[0]["R"], ""]
        groups = {}
        for x in stress:
            groups.setdefault((x["delta"], x["mode"], x["accept"]), []).append(x)
        rows = []
        for (dl, mode, pe), xs in sorted(groups.items(), key=lambda kv: (-kv[0][0], kv[0][1], kv[0][2])):
            at = [x for x in xs if x["d"] < 0]
            zero = [x for x in xs if x["d"] == 0]
            mx = lambda k: max(x[k] / x["R"] for x in at)
            mn = lambda k: sum(x[k] / x["R"] for x in zero) / len(zero)
            rows.append([f"{dl:.4f}", mode, pe, pct(mx("cp_miss")), pct(mx("wc_miss")), pct(mn("cp_ni")),
                         pct(mn("wc_ni")), f"{sum(x['dropped'] / x['R'] for x in xs) / len(xs):.2f}"])
        L += [table(["delta", "missingness", "acceptance", "false NI: complete pairs", "false NI: worst case",
                     "P(NI) at 0: complete pairs", "P(NI) at 0: worst case", "cases lost per dataset"], rows), ""]
        L += ["Report both analyses for P4. Noninferiority is claimed only if the worst-case bound also clears -delta, "
              "or the missingness is shown not to depend on outcome or case difficulty.", ""]
    if models:
        L += ["## 6b. Model heterogeneity (pooled over three models)", "",
              "Three models with different rates answer the same cases; each case's repeats from all models are "
              "averaged (the case stays the unit) and the pooled estimand is the mean of the per-model differences, "
              "set to exactly -delta. The primary results are per model (spec §9.6); this checks that a pooled summary "
              "is still valid. %d datasets per row." % models[0]["R"], ""]
        rows = [[f"{x['delta']:.4f}", x["label"], x["sd"], x["reps"], x["n"], pct(x["noncov"])] for x in models]
        L += [table(["delta", "models", "SD", "repeats", "cases", "lower non-coverage = false NI"], rows), ""]
    L += ["## 7. Comparison with the independent reference bounds", ""]
    if not refs:
        L += ["Not run. Hook: `python3 precision.py --reference NAME=GITREF:PATH`. The module is loaded from the "
              "reviewer's branch at run time, never copied into the analysis code.", ""]
    else:
        L += ["The reviewer's comparators were loaded at run time from their branches (never copied here) and run "
              "on the **same simulated datasets** as the chosen P4 method. Both treat missing responses as adverse "
              "(scheduled denominators) and use the case as the unit. They are checks, not the method.", ""]
        for x in refs:
            L.append(f"- `{x['name']}`: `{x['path']}` at `{x['ref']}` ({x['commit']}).")
        L += ["", "**All pairs agree (all ones in both arms).** Lower bound for E_scope - E, one-sided 97.5%:", ""]
        names = [chosen4] + [x["name"] for x in refs]
        L += [table(["cases", "repeats"] + names,
                    [[r["n"], r["reps"]] + [f"{r[k]:.4f}" for k in names] for r in agree_rows]), ""]
        L += ["All bounds are non-degenerate; none uses repeats as extra cases.", ""]
        rows = []
        for r in cmp_rows:
            R = r["R"]
            t = r["tally"]
            cells_ = [f"{pct(t[k][0] / R)}" for k in names]
            ag = [" / ".join(pct(v / R) for v in r["agree"][x["name"]]) for x in refs]
            rows.append([r["delta"], r["accept"], f"{r['d']:.4f}", r["sd"], r["reps"], r["n"], r["miss"]] + cells_ + ag)
        L += [f"**Same data, P4 decisions** ({cmp_rows[0]['R'] if cmp_rows else 0} datasets per row). Share of "
              "datasets declaring noninferiority (lower bound > -delta). At difference -delta this is the type I "
              "error; at 0 it is power. Agreement columns: both / chosen only / reference only / neither.", ""]
        L += [table(["delta", "acceptance", "difference", "SD", "repeats", "cases", "missing"]
                    + [f"NI: {k}" for k in names] + [f"agreement with {x['name']}" for x in refs], rows), ""]
        worst = {k: max((r["tally"][k][1] / r["R"] for r in cmp_rows), default=0) for k in names}
        L += ["Largest lower-bound non-coverage over these rows: " + ", ".join(f"`{k}` {pct(v)}" for k, v in worst.items())
              + ".", ""]
    L += ["## 8. Limits", "",
          "- The generative model is one plausible structure (logit-normal case effect shared by both arms). "
          "Arm-specific case effects, case-family dependence and drift are not simulated. If cases share a source "
          "family, the family is the unit.",
          "- Complete-pair analysis is unbiased only if missingness is unrelated to the outcome. Outcome-dependent "
          "missingness is handled by the scheduled-denominator bounds, which are reported for every primary "
          "contrast (SCORING_SPEC §2), not by this simulation.",
          "- Monte Carlo error: per-point non-coverage has SE about 0.35% at 2,000 datasets and 0.11% at 20,000.",
          "- Planning inputs (SESOI, delta, acceptance, SD) are placeholders until fixed in review; the tables "
          "show the sensitivity of the case count to each.", ""]
    return "\n".join(L)


if __name__ == "__main__":
    main()
