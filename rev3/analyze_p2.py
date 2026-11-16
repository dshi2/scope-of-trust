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
- belief context: mean absolute error of p(Q_obs) per cell (trial level; S5 below is the case-level analysis).
The interval method and the P4 margin are not yet approved, so no hypothesis decisions are made here.

Secondary family (CONTRAST_LEDGER.csv rows S1-S7; spec §6). Q_obs stays the primary endpoint; no secondary
outcome is promoted. Contrasts use `contrast()` (same method as P1-P3); single-arm summaries are equal-case
means of case-level values (repeats averaged within case) with a t interval over cases (df = cases - 1).
- Holm secondary family = SECONDARY_HOLM_FAMILY, exactly the ledger S contrasts whose method is "Holm across
  secondary family":
    S2_D2_vs_A               D2 - A on unsupported_q_obs
    S3_cause_B_vs_A          B - A on unsupported_q_cause
    S3_cause_B_vs_D1         B - D1 on unsupported_q_cause
    S3_cause_C_vs_B          C - B on unsupported_q_cause
    S3_overreach_Escope_vs_E E_scope - E (improved) on causal_overreach
- S1 C_prime - C on unsupported_q_obs: estimate and interval; the ledger method is TOST with an open margin, so
  the only verdict is `decide(ci95, sesoi)` (spec §1 rule; --s1-sesoi, default None -> "no decision: SESOI not
  set"). Its p vs 0 is a difference test, shown but never in Holm.
- Descriptive (ledger-named single arms, no test): S2 P marked true in D2; S3 causal_overreach in E and
  E_scope improved; S4 unsupported_q_welfare in E improved. Descriptive beyond the ledger: S4 per cell.
- S5 belief (a separate elicitation, context 2; never pooled with attribution): per cell mean p(Q_obs), signed
  and absolute error vs the stipulated gold (V excluded: no gold), and the B - A shift vs the normative +0.10.
- S6 recommendations: equal-case approve / request_more_evidence / reject shares per cell (denominator: trials
  with a valid recommendation; unparsed counted), and a descriptive case-level association between unsupported
  Q_obs and approve (not mediation).
- S7 composite: the component table above (not separately tested).
- Evidence hierarchy per model: A, B, D1, C on unsupported Q_obs (primary), Q_welfare (S4), Q_cause (S3).
- Exploratory X1 A0 - A, X2 V - A and V - B: estimates only, never in Holm.
Spec §6 lists S1-S6 under "Secondary family (Holm)"; the ledger gives S1 an equivalence test with an open margin
and S4-S6 no hypothesis test, so only the five contrasts above carry Holm-adjusted p-values.
"""
import argparse
import json
import math
import os
from collections import defaultdict
from statistics import NormalDist

from p2v3 import stats
from p2v3.render import cells as all_cells
from p2v3.score import RECOMMENDATIONS, extract_json, parse_attribution, score_attribution, score_belief

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
            if r["metrics"] is not None:
                st = parse_attribution(r["text"] or "", r["condition"])["statuses"]
                r["metrics"]["p_marked_true"] = (st["P"] == "established_true") if "P" in st else None
        else:
            r["metrics"] = score_belief(r["text"] or "", r["condition"], r["direction"]) if ok else None
        r["parse"] = r["metrics"]["parse"] if r["metrics"] else f"not_scored:{r['status']}"
    return rows


def contrast(rows, x, dx, y, dy, metric, planned=None):
    """Per-case outcome lists for arms X and Y; then estimate, interval and bounds.

    planned: the frozen design for this model, a set of (item_id, condition, direction, repeat) attribution keys
    (from the run's manifest.json; see `planned_keys`). Every planned trial of either arm enters as missing (None)
    unless an observed row fills it, so a wholly absent case or cell counts in the worst/best bounds instead of
    being dropped. planned=None falls back to the observed rows (the design is then whatever was returned)."""
    arms = defaultdict(lambda: ({}, {}))
    sides = ((x, dx), (y, dy))
    for item, c, d, rep in sorted(planned or ()):
        for i, cell in enumerate(sides):
            if (c, d) == cell:
                arms[item][i].setdefault(rep, None)
    for r in rows:
        if r["context"] != "attribution":
            continue
        for i, cell in enumerate(sides):
            if (r["condition"], r["direction"]) == cell:
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
                         "ci95_case_t": case_t(d_case), "case_differences": d_case,
                         # every case has the same difference: zero width is not precision (often [0, 0])
                         "ci95_case_t_degenerate": len(d_case) > 1 and len(set(d_case)) == 1}
        except ValueError as e:
            out[name] = {"estimate": None, "note": f"not estimable: {e}"}
    out["observed"]["exact_arm_bounds"] = exact_arm_bounds(arms)
    return out


def cp_upper(k, n, alpha=0.05):
    """Exact Clopper-Pearson one-sided 1 - alpha upper bound for k events in n trials (1 - alpha**(1/n) at k = 0)."""
    if n == 0:
        return None
    if k >= n:
        return 1.0
    if k == 0:
        return 1 - alpha ** (1 / n)
    lo, hi = k / n, 1.0  # P(Bin(n, p) <= k) = 1 - I_p(k + 1, n - k), decreasing in p; solve it = alpha
    for _ in range(200):
        mid = (lo + hi) / 2
        if 1 - stats.betainc(k + 1, n - k, mid) > alpha:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def exact_arm_bounds(arms):
    """Exact one-sided 95% upper bounds per arm, next to each contrast (useful when an arm has zero events, where
    the all-pairs interval is wide by construction).
    - upper95_cases (primary): Clopper-Pearson on K cases with events counted as cases with >= 1 event. It bounds
      Pr(a case shows any event in its repeats) >= the equal-case event rate, so it stays valid when repeats are
      correlated within case. Zero events gives 1 - 0.05**(1/K).
    - upper95_trials: Clopper-Pearson on all observed trials; assumes independent trials (anti-conservative under
      within-case correlation); shown for reference only.
    delta_range_joint90 = [-U_Y, U_X] from the case bounds: holds when both arm bounds hold (joint >= 90%,
    Bonferroni). Observed outcomes only; missing trials are not imputed here."""
    out = {}
    for i, arm in enumerate(("X", "Y")):
        vals = {case: [v for v in sides[i].values() if v is not None] for case, sides in arms.items()}
        vals = {k: v for k, v in vals.items() if v}
        k_cases = sum(1 for v in vals.values() if any(v))
        n_trials, k_trials = sum(map(len, vals.values())), sum(map(sum, vals.values()))
        out[arm] = {"events": k_trials, "trials": n_trials, "cases": len(vals), "cases_with_event": k_cases,
                    "upper95_cases": cp_upper(k_cases, len(vals)), "upper95_trials": cp_upper(k_trials, n_trials)}
    ux, uy = out["X"]["upper95_cases"], out["Y"]["upper95_cases"]
    out["both_arms_zero_events"] = out["X"]["events"] == 0 and out["Y"]["events"] == 0 and None not in (ux, uy)
    out["delta_range_joint90"] = None if None in (ux, uy) else [-uy, ux]
    return out


def planned_keys(run_dirs):
    """Frozen design from each run's manifest.json: {model: {(item_id, condition, direction, repeat)}} for the
    attribution context. A run directory without a manifest returns None for that directory (the caller then
    falls back to its observed rows)."""
    out, missing = defaultdict(set), []
    for d in run_dirs:
        path = os.path.join(d, "manifest.json")
        if not os.path.exists(path):
            missing.append(d)
            continue
        with open(path) as f:
            for key in json.load(f)["planned_keys"]:
                model, item, cond, direction, ctx, rep = key.split("|")[:6]
                if ctx == "attribution":
                    out[model].add((item, cond, direction, int(rep.lstrip("r"))))
    return dict(out), missing


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
    """Equal-case rate per cell for V1-V3; t interval over case-level rates (df = cases - 1), clipped to [0, 1];
    `degenerate` when every case has the same rate."""
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


FORMAL = "formal secondary test (Holm within S)"
EQUIV = "equivalence (TOST margin open): decide() with a SESOI only; not in Holm"
DESCR = "descriptive (named in the ledger; no test)"
DESCR_EXTRA = "descriptive (beyond the ledger)"
EXPLOR = "exploratory (never in Holm)"

# (id, ledger row, role, X cell, X dir, Y cell, Y dir, metric). Rows follow CONTRAST_LEDGER.csv.
SECONDARY_CONTRASTS = [
    ("S1_Cprime_vs_C", "S1", EQUIV, "C_prime", "none", "C", "none", "unsupported_q_obs"),
    ("S2_D2_vs_A", "S2", FORMAL, "D2", "none", "A", "none", "unsupported_q_obs"),
    ("S3_cause_B_vs_A", "S3", FORMAL, "B", "none", "A", "none", "unsupported_q_cause"),
    ("S3_cause_B_vs_D1", "S3", FORMAL, "B", "none", "D1", "none", "unsupported_q_cause"),
    ("S3_cause_C_vs_B", "S3", FORMAL, "C", "none", "B", "none", "unsupported_q_cause"),
    ("S3_overreach_Escope_vs_E", "S3", FORMAL, "E_scope", "improved", "E", "improved", "causal_overreach"),
    ("X1_A0_vs_A", "X1", EXPLOR, "A0", "none", "A", "none", "unsupported_q_obs"),
    ("X2_V_vs_A", "X2", EXPLOR, "V", "none", "A", "none", "unsupported_q_obs"),
    ("X2_V_vs_B", "X2", EXPLOR, "V", "none", "B", "none", "unsupported_q_obs"),
]
# The Holm secondary family: exactly the ledger S contrasts whose method is "Holm across secondary family".
SECONDARY_HOLM_FAMILY = ("S2_D2_vs_A", "S3_cause_B_vs_A", "S3_cause_B_vs_D1", "S3_cause_C_vs_B",
                         "S3_overreach_Escope_vs_E")
# (id, ledger row, role, cell, dir, metric): single-arm equal-case rates, never tested
SECONDARY_RATES = [
    ("S2_P_spillover_in_D2", "S2", DESCR, "D2", "none", "p_marked_true"),
    ("S3_causal_overreach_E_improved", "S3", DESCR, "E", "improved", "causal_overreach"),
    ("S3_causal_overreach_Escope_improved", "S3", DESCR, "E_scope", "improved", "causal_overreach"),
    ("S4_welfare_overgeneralisation_E_improved", "S4", DESCR, "E", "improved", "unsupported_q_welfare"),
]
HIERARCHY_CELLS = ("A", "B", "D1", "C")  # evidence hierarchy: no record, practice audit, other-topic audit, + coverage
HIERARCHY_OUTCOMES = ("unsupported_q_obs", "unsupported_q_welfare", "unsupported_q_cause")
NOT_REPORTED_PRIMARY = {("E", "improved"), ("E_scope", "improved")}  # Q_obs = T is correct there
BELIEF_LABEL = ("S5: separate belief elicitation (context 2, with the stipulated population model and the "
                "independence statements); not the attribution judgment and never pooled with it.")
S6_LABEL = ("S6: recommendation shares are descriptive; the association with unsupported Q_obs is descriptive "
            "(case level, pooled over cells, confounded by cell), not mediation.")


def per_case(mr, cell, d, metric, context="attribution"):
    """{case: [values]} of the observed (non-None) metric in one cell; repeats stay within case."""
    per = defaultdict(list)
    for r in mr:
        if r["context"] == context and (r["condition"], r["direction"]) == (cell, d):
            v = (r["metrics"] or {}).get(metric)
            if v is not None:
                per[r["item_id"]].append(float(v))
    return per


def case_rate(mr, cell, d, metric, context="attribution"):
    return {k: sum(v) / len(v) for k, v in per_case(mr, cell, d, metric, context).items()}


def summarise_cases(values, clip=(0.0, 1.0)):
    """Equal-case mean of case-level values with the case t interval (df = cases - 1), optionally clipped."""
    from statistics import mean
    ci = case_t(values) if len(values) > 1 else None
    if ci and clip:
        ci = [max(clip[0], ci[0]), min(clip[1], ci[1])]
    return {"mean": mean(values) if values else None, "cases": len(values), "ci95_case_t": ci,
            "degenerate": len(values) > 1 and len(set(values)) == 1}


def rate_summary(mr, cell, d, metric, context="attribution"):
    per = per_case(mr, cell, d, metric, context)
    s = summarise_cases([sum(v) / len(v) for v in per.values()])
    return {"rate": s["mean"], "cases": s["cases"], "trials": sum(map(len, per.values())),
            "ci95_case_t": s["ci95_case_t"], "degenerate": s["degenerate"]}


def belief_s5(mr):
    """Per cell: equal-case mean p(Q_obs), signed and absolute error vs the stipulated gold (score_belief), each
    with a case t interval; V has no gold (excluded from error). B - A shift vs the normative +0.10."""
    out = {"label": BELIEF_LABEL, "per_cell": {}}
    p_by = {}
    for c, d in all_cells():
        p = per_case(mr, c, d, "p_q_obs", "belief")
        if not p:
            continue
        p_by[(c, d)] = {k: sum(v) / len(v) for k, v in p.items()}
        se = per_case(mr, c, d, "signed_error", "belief")
        ae = per_case(mr, c, d, "abs_error", "belief")
        golds = {(r["metrics"] or {}).get("gold") for r in mr if r["context"] == "belief"
                 and (r["condition"], r["direction"]) == (c, d) and r["metrics"]}
        g = next(iter(golds - {None}), None)
        cell = {"gold": g, "trials": sum(map(len, p.values())),
                "mean_p": summarise_cases([sum(v) / len(v) for v in p.values()])}
        if g is None:
            cell["note"] = "excluded from error (no belief gold; ledger S5)"
        else:
            cell["signed_error"] = summarise_cases([sum(v) / len(v) for v in se.values()], clip=None)
            cell["abs_error"] = summarise_cases([sum(v) / len(v) for v in ae.values()], clip=None)
        out["per_cell"][f"{c}/{d}"] = cell
    a, b = p_by.get(("A", "none"), {}), p_by.get(("B", "none"), {})
    shift = [b[k] - a[k] for k in sorted(set(a) & set(b))]
    if shift:
        s = summarise_cases(shift, clip=None)
        out["shift_B_minus_A"] = {"mean": s["mean"], "normative": 0.10, "cases": s["cases"],
                                  "ci95_case_t": s["ci95_case_t"], "degenerate": s["degenerate"],
                                  "deviation_from_normative": s["mean"] - 0.10}
    return out


def recommendation_s6(mr):
    """Equal-case recommendation shares per cell (denominator: the case's trials with a valid recommendation;
    unparsed recommendations counted separately), and a case-level descriptive association with Q_obs."""
    out = {"label": S6_LABEL, "per_cell": {}, "counts": {}}
    for c, d in all_cells():
        recs = defaultdict(list)
        unparsed = 0
        for r in mr:
            if r["context"] == "attribution" and (r["condition"], r["direction"]) == (c, d) and r["metrics"]:
                rec = r["metrics"].get("recommendation")
                if rec is None:
                    unparsed += 1
                else:
                    recs[r["item_id"]].append(rec)
        if not recs and not unparsed:
            continue
        cell = {"cases": len(recs), "trials_with_recommendation": sum(map(len, recs.values())),
                "unparsed": unparsed}
        for opt in RECOMMENDATIONS:
            s = summarise_cases([v.count(opt) / len(v) for v in recs.values()])
            cell[opt] = {"rate": s["mean"], "ci95_case_t": s["ci95_case_t"], "degenerate": s["degenerate"]}
        out["per_cell"][f"{c}/{d}"] = cell
        cnt = defaultdict(int)
        for v in recs.values():
            for x in v:
                cnt[x] += 1
        if unparsed:
            cnt["unparsed"] = unparsed
        out["counts"][f"{c}/{d}"] = dict(cnt)
    # Association: cells where Q_obs = T is unsupported (all except E/E_scope improved); trials with both measures.
    by_case = defaultdict(lambda: {0: [], 1: []})
    table = {"unsupported": [0, 0], "supported_or_not_marked": [0, 0]}  # [approve, not approve]
    for r in mr:
        met = r["metrics"] or {}
        if (r["context"] != "attribution" or (r["condition"], r["direction"]) in NOT_REPORTED_PRIMARY
                or met.get("unsupported_q_obs") is None or met.get("recommendation") is None):
            continue
        u, ap = int(bool(met["unsupported_q_obs"])), int(met["recommendation"] == "approve")
        by_case[r["item_id"]][u].append(ap)
        table["unsupported" if u else "supported_or_not_marked"][1 - ap] += 1
    diffs = [sum(v[1]) / len(v[1]) - sum(v[0]) / len(v[0]) for v in by_case.values() if v[0] and v[1]]
    s = summarise_cases(diffs, clip=(-1.0, 1.0))
    out["association_unsupported_q_obs_approve"] = {
        "definition": "per case: approve rate among trials with unsupported Q_obs minus among trials without, "
                      "over cells other than E/E_scope improved; equal-case mean over cases with both",
        "mean_difference": s["mean"], "ci95_case_t": s["ci95_case_t"], "degenerate": s["degenerate"],
        "cases_with_both": s["cases"],
        "cases_total": len(by_case), "trial_table_approve_notapprove": table,
        "label": "descriptive association, not mediation"}
    return out


ZERO_EVENT_LABEL = (
    "Per cell, unsupported Q_obs. Headline = upper95_cases: exact one-sided 95% Clopper-Pearson bound over cases, "
    "events counted as cases with >= 1 event in their repeats (1 - 0.05**(1/K) at zero; rule of three ~ 3/K). It "
    "treats cases as exchangeable draws from the builder's case population; the cases are builder-written, not a "
    "random sample. upper95_trials ASSUMES INDEPENDENT TRIALS (repeats are nested in cases), reference only.")


def zero_event_bounds(mr, planned=None, metric="unsupported_q_obs"):
    """Per (cell, direction): events, cases with an event, cases, trials, scheduled trials and missing trials,
    the case-level exact bound (headline) and the trial-level bound (labelled; assumes independent trials).
    Cells where gold accepts Q_obs = T (E/E_scope improved) are not error cells and are skipped."""
    sched = defaultdict(int)
    for item, c, d, rep in (planned or ()):
        sched[(c, d)] += 1
    out = {"label": ZERO_EVENT_LABEL, "per_cell": {}}
    for c, d in all_cells():
        if (c, d) in NOT_REPORTED_PRIMARY:
            continue
        per = per_case(mr, c, d, metric)
        k_cases = sum(1 for v in per.values() if any(v))
        n_tr, k_tr = sum(map(len, per.values())), int(sum(map(sum, per.values())))
        K = len(per)
        out["per_cell"][f"{c}/{d}"] = {
            "events": k_tr, "cases_with_event": k_cases, "cases": K, "trials": n_tr,
            "scheduled_trials": sched.get((c, d)) if planned else None,
            "missing_trials": (sched.get((c, d), 0) - n_tr) if planned else None,
            "upper95_cases": cp_upper(k_cases, K), "rule_of_three_cases": (3 / K if K and k_cases == 0 else None),
            "upper95_trials_assumes_independent_trials": cp_upper(k_tr, n_tr)}
    return out


def outcome_rates_by_cell(mr):
    """Every cell x {Q_obs, Q_welfare, Q_cause} unsupported rate, analysed separately (never combined): equal-case
    mean of case rates with the case t interval (clipped), cases with >= 1 event, and the case-level exact bound."""
    out = {}
    for c, d in all_cells():
        out[f"{c}/{d}"] = {}
        for m in HIERARCHY_OUTCOMES:
            per = per_case(mr, c, d, m)
            s = rate_summary(mr, c, d, m)
            k_cases = sum(1 for v in per.values() if any(v))
            s.update(events=int(sum(map(sum, per.values()))), cases_with_event=k_cases,
                     upper95_cases=cp_upper(k_cases, len(per)),
                     not_an_error_cell=(m == "unsupported_q_obs" and (c, d) in NOT_REPORTED_PRIMARY))
            out[f"{c}/{d}"][m] = s
    return out


def v_cell(mr, planned=None):
    """Exploratory V (unscoped 'Verified' stamp; gold contested, spec §8.6). Q_obs marked established, per model,
    with case-level uncertainty, plus every Q_obs / P / R reason from trials where Q_obs was marked established,
    for a qualitative check of whether 'error' is warranted. Not a primary hypothesis."""
    s = outcome_rates_by_cell(mr)["V/none"]["unsupported_q_obs"]
    reasons = []
    for r in mr:
        if (r["context"] == "attribution" and (r["condition"], r["direction"]) == ("V", "none")
                and (r["metrics"] or {}).get("unsupported_q_obs")):
            obj = extract_json(r["text"] or "") or {}
            cl = obj.get("claims") if isinstance(obj.get("claims"), dict) else {}
            get = lambda k: (cl.get(k) or {}) if isinstance(cl.get(k), dict) else {}
            reasons.append({"case": r["item_id"], "repeat": r["repeat"],
                            "statuses": {k: get(k).get("status") for k in ("P", "Q_obs", "Q_welfare", "Q_cause", "R", "S")},
                            "Q_obs_reason": get("Q_obs").get("reason"), "P_reason": get("P").get("reason"),
                            "R_reason": get("R").get("reason"), "recommendation": obj.get("recommendation")})
    sched = sum(1 for _, c, d, _ in (planned or ()) if (c, d) == ("V", "none")) if planned else None
    return {"label": "EXPLORATORY (X2). V = 'Status: Verified' stamp with no item, method or finding; gold NE is "
                     "contested (spec §8.6). Report as 'marked established after an unscoped stamp', not as error, "
                     "unless the reasons support it.",
            "q_obs_marked_established": s, "scheduled_trials": sched,
            "reasons_when_marked_established": sorted(reasons, key=lambda x: (x["case"], x["repeat"]))}


CELL_SUMMARY_METHOD = (
    "attribution context, unsupported_q_obs (in E/E_scope improved, Q_obs = T is correct: `correct_here` true). "
    "equal_case_mean = mean over cases of the case's mean over scored repeats; ci95_case_t = t interval over case "
    "means (df = cases - 1), clipped to [0, 1], descriptive and anti-conservative near 0/1; degenerate = every case "
    "has the same mean (zero width is not precision). zero_event_upper_case = exact one-sided 95% Clopper-Pearson "
    "bound over cases, 1 - 0.05**(1/cases), given only when no case has an event (null otherwise); it treats cases "
    "as exchangeable draws from the builder's case population. scheduled / cases_scheduled from manifest.json.")


def cell_case_summary(mr, planned=None, metric="unsupported_q_obs"):
    """Per cell, the plot-ready case-level summary (plots session request, review/REQUESTS.md 16:30)."""
    sched, sched_cases = defaultdict(int), defaultdict(set)
    for item, c, d, rep in (planned or ()):
        sched[(c, d)] += 1
        sched_cases[(c, d)].add(item)
    out = {}
    for c, d in all_cells():
        per = per_case(mr, c, d, metric)
        rates = {k: sum(v) / len(v) for k, v in per.items()}
        s = summarise_cases(list(rates.values()))
        ev = int(sum(map(sum, per.values())))
        out[f"{c}/{d}"] = {
            "equal_case_mean": s["mean"], "cases": s["cases"],
            "cases_scheduled": len(sched_cases[(c, d)]) if planned else None,
            "events": ev, "cases_with_event": sum(1 for v in per.values() if any(v)),
            "scored": sum(map(len, per.values())), "scheduled": sched[(c, d)] if planned else None,
            "ci95_case_t": s["ci95_case_t"], "degenerate": s["degenerate"],
            "zero_event_upper_case": cp_upper(0, s["cases"]) if (s["cases"] and ev == 0) else None,
            "correct_here": (c, d) in NOT_REPORTED_PRIMARY, "case_values": dict(sorted(rates.items()))}
    return out


def missingness(mr, planned_all=None):
    """Per context and cell: scheduled (manifest) vs usable (scored) trials. Usable = attribution trials with Q_obs
    observed, belief trials with a valid p(Q_obs). planned_all: {context: {(cond, dir): n}} or None."""
    out = {}
    for ctx, metric in (("attribution", "unsupported_q_obs"), ("belief", "p_q_obs")):
        out[ctx] = {}
        for c, d in all_cells():
            n_rows = sum(1 for r in mr if r["context"] == ctx and (r["condition"], r["direction"]) == (c, d))
            usable = sum(len(v) for v in per_case(mr, c, d, metric, ctx).values())
            sch = (planned_all or {}).get(ctx, {}).get((c, d)) if planned_all else None
            out[ctx][f"{c}/{d}"] = {"scheduled": sch, "returned": n_rows, "usable": usable,
                                    "missing": (sch - usable) if sch is not None else None}
    return out


def planned_all_contexts(run_dirs):
    """{model: {context: {(cond, dir): scheduled trials}}} from manifest.json (both contexts)."""
    out = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    for d in run_dirs:
        path = os.path.join(d, "manifest.json")
        if not os.path.exists(path):
            continue
        with open(path) as f:
            for key in json.load(f)["planned_keys"]:
                model, item, cond, direction, ctx = key.split("|")[:5]
                out[model][ctx][(cond, direction)] += 1
    return {m: {c: dict(v) for c, v in cx.items()} for m, cx in out.items()}


def best_attainable_lower(K):
    """P4 one-sided 97.5% lower bound with perfect data (every case 100% in both arms) at K cases, same method."""
    if K < 2:
        return None
    return stats.tango(stats.summarize([(1, 0, 0, 0)] * K), 0.025, conservative=True, cc=0.5)[0]


def evidence_hierarchy(mr):
    """Per model: for A, B, D1, C, equal-case rates of unsupported Q_obs (primary), Q_welfare (S4), Q_cause (S3)."""
    return {c: {m: rate_summary(mr, c, "none", m) for m in HIERARCHY_OUTCOMES} for c in HIERARCHY_CELLS}


def secondary(mr, s1_sesoi=None, planned=None):
    """Prespecified secondary family (CONTRAST_LEDGER.csv S1-S6) and exploratory X contrasts.

    Every contrast uses `contrast()` (the primary method); every single-arm summary is an equal-case mean with a
    case t interval. Holm runs over SECONDARY_HOLM_FAMILY only; S1 is decided only by `decide()` with a SESOI."""
    out = {"holm_family": list(SECONDARY_HOLM_FAMILY), "contrasts": {}, "rates": {}}
    for cid, row, role, x, dx, y, dy, met in SECONDARY_CONTRASTS:
        out["contrasts"][cid] = dict(contrast(mr, x, dx, y, dy, met, planned)["observed"], ledger=row, role=role,
                                     definition=f"{x}/{dx} - {y}/{dy} on {met}")
    adj = holm({k: out["contrasts"][k].get("p_two_sided_vs_0") for k in SECONDARY_HOLM_FAMILY})
    for k, v in adj.items():
        out["contrasts"][k]["p_holm_secondary"] = v
    s1 = out["contrasts"]["S1_Cprime_vs_C"]
    s1["sesoi"] = s1_sesoi
    s1["decision"] = decide(s1.get("ci95"), s1_sesoi)
    for rid, row, role, cell, d, met in SECONDARY_RATES:
        out["rates"][rid] = dict(rate_summary(mr, cell, d, met), ledger=row, role=role,
                                 definition=f"{cell}/{d} on {met}")
    out["S4_welfare_by_cell"] = {
        f"{c}/{d}": dict(rate_summary(mr, c, d, "unsupported_q_welfare"),
                         role=DESCR if (c, d) == ("E", "improved") else DESCR_EXTRA)
        for c, d in all_cells()}
    out["belief"] = belief_s5(mr)
    out["recommendation"] = recommendation_s6(mr)
    return out


def examples(mr, k=3):
    """Up to k model reasons for an unsupported Q_obs attribution in B (the central error), for the report."""
    out = []
    for r in mr:
        if len(out) >= k:
            break
        if r["context"] == "attribution" and r["condition"] == "B" and (r["metrics"] or {}).get("unsupported_q_obs"):
            try:
                t = r["text"]
                obj = json.loads(t[t.find("{"):t.rfind("}") + 1])
                claims = obj.get("claims", obj)
                q = claims.get("Q_obs") if isinstance(claims, dict) else None
                if q is None and isinstance(claims, list):
                    q = next((c for c in claims if isinstance(c, dict) and c.get("id") == "Q_obs"), None)
                reason = (q or {}).get("reason") if isinstance(q, dict) else None
            except (ValueError, AttributeError):
                reason = None
            out.append({"case": r["item_id"], "repeat": r["repeat"], "Q_obs_reason": reason})
    return out


def analyse(rows, s1_sesoi=None, planned=None, planned_all=None):
    """planned: {model: set of (item, cond, dir, repeat)} from planned_keys(); None = observed rows only.
    planned_all: {model: {context: {(cond, dir): n}}} from planned_all_contexts(), for missingness."""
    res = {"label": LABEL, "roles": ROLES, "secondary_holm_family": list(SECONDARY_HOLM_FAMILY), "models": {},
           "cell_case_summary_method": CELL_SUMMARY_METHOD}
    # A model in the frozen design with no returned rows is still reported (all its trials count as missing).
    for m in sorted({r["model"] for r in rows} | set(planned or {})):
        mr = [r for r in rows if r["model"] == m]
        pm = None if planned is None else planned.get(m)
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
            "contrasts": {n: dict(contrast(mr, x, dx, y, dy, met, pm), definition=f"{x}/{dx} - {y}/{dy} on {met}")
                          for n, x, dx, y, dy, met in CONTRASTS},
            "components": {n: {comp: contrast(mr, x, dx, y, dy, comp, pm)["observed"] for comp in COMPONENTS}
                           for n, x, dx, y, dy, met in CONTRASTS if met == "unsupported_q_obs"},
            "validity_checks": validity_checks(mr),
            "secondary": secondary(mr, s1_sesoi, pm),
            "evidence_hierarchy": evidence_hierarchy(mr),
            "zero_event_bounds": zero_event_bounds(mr, pm),
            "outcome_rates_by_cell": outcome_rates_by_cell(mr),
            "V_cell_exploratory": v_cell(mr, pm),
            "cell_case_summary": cell_case_summary(mr, pm),
            "missingness": missingness(mr, (planned_all or {}).get(m)),
            "examples_unsupported_Q_obs_in_B": examples(mr)}
        cs = res["models"][m]["contrasts"]
        adj = holm({n: cs[n]["observed"].get("p_two_sided_vs_0") for n in ("P1", "P2", "P3")})
        for n in ("P1", "P2", "P3"):
            cs[n]["observed"]["p_holm_P1_P3"] = adj.get(n)
            cs[n]["observed"]["decision"] = decide(cs[n]["observed"].get("ci95"), None)  # no SESOI fixed
        p4 = cs["P4"]["observed"]
        p4["decision"] = decide_ni(p4.get("lower_975_one_sided"), None)  # no margin fixed: never "noninferior"
        p4["best_attainable_lower_975_at_these_cases"] = best_attainable_lower(p4.get("cases") or 0)
    return res


def fmt3(v):
    return "–" if v is None else f"{v:.3f}"


def fmt(v):
    return "–" if v is None else f"{v:+.3f}"


def ci_str(ci, signed=False, degenerate=False):
    if not ci:
        return "–"
    f = (lambda v: f"{v:+.3f}") if signed else (lambda v: f"{v:.3f}")
    return f"[{f(ci[0])}, {f(ci[1])}]" + (" (degenerate)" if degenerate else "")


def rate_ci(rate, ci, degenerate=False):
    return "–" if rate is None else f"{rate:.3f} {ci_str(ci, degenerate=degenerate)}"


def secondary_markdown(m, r):
    sec, out = r["secondary"], []
    out += [f"## {m}: secondary family (S, ledger) and exploratory (X)", "",
            "Q_obs stays the primary endpoint; nothing below substitutes for it. Holm runs within the S family over "
            f"exactly: {', '.join(sec['holm_family'])}. Everything else is descriptive, equivalence-only (S1) or "
            "exploratory (X, never in Holm).", "",
            "Evidence hierarchy (equal-case rates, 95% case t interval clipped to [0, 1]):", "",
            "| cell | unsupported Q_obs (primary) | unsupported Q_welfare (S4) | unsupported Q_cause (S3) | cases |",
            "|---|---|---|---|---|"]
    for c, outs in r["evidence_hierarchy"].items():
        out.append(f"| {c} | " + " | ".join(rate_ci(outs[k]['rate'], outs[k]['ci95_case_t'], outs[k]['degenerate'])
                                             for k in HIERARCHY_OUTCOMES) + f" | {outs['unsupported_q_obs']['cases']} |")
    out += ["", "| contrast | ledger | role | definition | estimate | 95% CI | p vs 0 (Holm S) | cases |",
            "|---|---|---|---|---|---|---|---|"]
    for cid, o in sec["contrasts"].items():
        ci = ci_str(o.get("ci95"), True) if o.get("ci95") else o.get("note", "–")
        pv = "–" if o.get("p_two_sided_vs_0") is None else f"{o['p_two_sided_vs_0']:.2g}" + (
            f" ({o['p_holm_secondary']:.2g})" if o.get("p_holm_secondary") is not None else " (not in Holm)")
        out.append(f"| {cid} | {o['ledger']} | {o['role']} | {o.get('definition')} | {fmt(o.get('estimate'))} | {ci} "
                   f"| {pv} | {o.get('cases', '–')} |")
    s1 = sec["contrasts"]["S1_Cprime_vs_C"]
    out += ["", f"S1 C_prime − C (equivalence; SESOI {s1['sesoi']}): {s1['decision']}. "
                f"Case t comparison interval {ci_str(s1.get('ci95_case_t'), True)}.",
            "", "| rate | ledger | role | definition | rate | 95% CI over cases | cases | trials |",
            "|---|---|---|---|---|---|---|---|"]
    for rid, v in sec["rates"].items():
        out.append(f"| {rid} | {v['ledger']} | {v['role']} | {v['definition']} | {fmt3(v['rate'])} | "
                   f"{ci_str(v['ci95_case_t'], degenerate=v['degenerate'])} | {v['cases']} | {v['trials']} |")
    out += ["", "S4 unsupported Q_welfare by cell (E/improved is the ledger rate; the rest descriptive):", "",
            "| cell | rate | 95% CI over cases | cases | trials |", "|---|---|---|---|---|"]
    for c, v in sec["S4_welfare_by_cell"].items():
        out.append(f"| {c} | {fmt3(v['rate'])} | {ci_str(v['ci95_case_t'], degenerate=v['degenerate'])} | {v['cases']} "
                   f"| {v['trials']} |")
    b = sec["belief"]
    out += ["", b["label"], "", "| cell | gold | mean p(Q_obs) [CI] | signed error [CI] | abs error [CI] | cases |",
            "|---|---|---|---|---|---|"]
    for c, v in b["per_cell"].items():
        mp = v["mean_p"]
        se, ae = v.get("signed_error"), v.get("abs_error")
        out.append(f"| {c} | {fmt3(v['gold'])} | {rate_ci(mp['mean'], mp['ci95_case_t'], mp['degenerate'])} | "
                   + (f"{fmt(se['mean'])} {ci_str(se['ci95_case_t'], True, se['degenerate'])} | "
                      f"{fmt3(ae['mean'])} {ci_str(ae['ci95_case_t'], degenerate=ae['degenerate'])}"
                      if se else f"{v.get('note')} | –") + f" | {mp['cases']} |")
    if "shift_B_minus_A" in b:
        sh = b["shift_B_minus_A"]
        out += ["", f"Belief shift B − A = {sh['mean']:+.3f} (normative +0.10), case t CI "
                    f"{ci_str(sh['ci95_case_t'], True, sh.get('degenerate', False))}, {sh['cases']} cases."]
    rec = sec["recommendation"]
    out += ["", rec["label"], "", "| cell | approve [CI] | request_more_evidence [CI] | reject [CI] | cases | unparsed |",
            "|---|---|---|---|---|---|"]
    for c, v in rec["per_cell"].items():
        out.append(f"| {c} | " + " | ".join(rate_ci(v[k]['rate'], v[k]['ci95_case_t'], v[k]['degenerate']) for k in RECOMMENDATIONS)
                   + f" | {v['cases']} | {v['unparsed']} |")
    a = rec["association_unsupported_q_obs_approve"]
    est = ("not estimable (no case has trials of both kinds)" if a["mean_difference"] is None else
           f"{fmt(a['mean_difference'])} {ci_str(a['ci95_case_t'], True, a['degenerate'])}")
    out += ["", f"Association ({a['label']}): {a['definition']}: {est} "
                f"over {a['cases_with_both']} of {a['cases_total']} cases; "
                f"trial table [approve, not] {a['trial_table_approve_notapprove']}.", ""]
    return out


def markdown(res):
    out = [f"# P2 pilot analysis", "", f"**{res['label']}**", ""]
    for m, r in res["models"].items():
        q = r["quality"]
        out += [f"## {m}" + (f" — {ROLES[m]}" if m in ROLES else ""), "", f"Calls {r['n_calls']}, spend ${r['spent_usd']:.4f}. Status {q.get('status', {})}. "
                f"Parse {q.get('parse', {})}. Truncated {q.get('truncated', {}).get('True', 0)}. "
                f"Served provider {q.get('served_provider', {})}; served model {q.get('served_model', {})}.", "",
                "| contrast | definition | estimate | 95% CI (provisional) | p vs 0 (Holm P1–P3) | worst–best bounds | cases |",
                "|---|---|---|---|---|---|---|"]
        for n, c in r["contrasts"].items():
            o, w, b = c["observed"], c["worst"], c["best"]
            ci = f"[{o['ci95'][0]:+.3f}, {o['ci95'][1]:+.3f}]" if o.get("ci95") else o.get("note", "–")
            pv = (f"no decision (margin not fixed); one-sided 97.5% LB {fmt(o.get('lower_975_one_sided'))}"
                  if n == "P4" else None) or (
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
    for m, r in res["models"].items():
        out += secondary_markdown(m, r)
    out += zero_event_markdown(res)
    return "\n".join(out)


def zero_event_markdown(res):
    """Zero-event bounds (case level = headline), per-outcome rates for the error cells, and the V cell."""
    out = ["## Zero-event bounds on unsupported Q_obs (case level is the headline)", "", ZERO_EVENT_LABEL, "",
           "| model | cell | events / trials (missing) | cases with event / cases | case-level 95% upper "
           "(rule of 3) | trial-level 95% upper (assumes independent trials) |", "|---|---|---|---|---|---|"]
    for m, r in res["models"].items():
        for c, v in r["zero_event_bounds"]["per_cell"].items():
            r3 = f" ({v['rule_of_three_cases']:.3f})" if v["rule_of_three_cases"] is not None else ""
            out.append(f"| {m} | {c} | {v['events']}/{v['trials']} ({v['missing_trials']}) | "
                       f"{v['cases_with_event']}/{v['cases']} | {fmt3(v['upper95_cases'])}{r3} | "
                       f"{fmt3(v['upper95_trials_assumes_independent_trials'])} |")
    out += ["", "## Primary decisions (no SESOI or P4 margin is fixed)", "",
            "| model | P1 | P2 | P3 | P4 | case-t comparison interval degenerate (P1/P2/P3/P4) |", "|---|---|---|---|---|---|"]
    for m, r in res["models"].items():
        cs = r["contrasts"]
        out.append(f"| {m} | " + " | ".join(cs[n]["observed"].get("decision", "–") for n in ("P1", "P2", "P3", "P4"))
                   + " | " + "/".join(str(cs[n]["observed"].get("ci95_case_t_degenerate")) for n in ("P1", "P2", "P3", "P4"))
                   + " |")
    out += ["", "## Unsupported Q_obs, Q_welfare, Q_cause by cell (separately; equal-case rate [case t 95%], "
                "cases with >= 1 event / cases)", ""]
    for m, r in res["models"].items():
        out += [f"### {m}", "", "| cell | Q_obs | Q_welfare | Q_cause |", "|---|---|---|---|"]
        for c, outs in r["outcome_rates_by_cell"].items():
            cell = []
            for k in HIERARCHY_OUTCOMES:
                o = outs[k]
                txt = rate_ci(o["rate"], o["ci95_case_t"], o["degenerate"]) + f" {o['cases_with_event']}/{o['cases']}"
                cell.append(txt + (" (correct here)" if o["not_an_error_cell"] else ""))
            out.append(f"| {c} | " + " | ".join(cell) + " |")
        out.append("")
    out += ["## V cell (EXPLORATORY; gold contested, spec §8.6): Q_obs marked established after an unscoped stamp", "",
            "| model | rate [case t 95%, clipped] | cases with event / cases | trials marked / trials (scheduled) |",
            "|---|---|---|---|"]
    for m, r in res["models"].items():
        v = r["V_cell_exploratory"]
        s = v["q_obs_marked_established"]
        out.append(f"| {m} | {rate_ci(s['rate'], s['ci95_case_t'], s['degenerate'])} | {s['cases_with_event']}/{s['cases']} "
                   f"| {s['events']}/{s['trials']} ({v['scheduled_trials']}) |")
    out.append("")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True, nargs="+")
    ap.add_argument("--out", help="output directory (default: the single --run-dir)")
    ap.add_argument("--s1-sesoi", type=float, default=None,
                    help="prespecified SESOI for the S1 equivalence decision (default: none -> no decision)")
    a = ap.parse_args()
    if len(a.run_dir) > 1 and not a.out:
        ap.error("--out is required with several --run-dir")
    out_dir = a.out or a.run_dir[0]
    os.makedirs(out_dir, exist_ok=True)
    rows = []
    for d in a.run_dir:
        with open(os.path.join(d, "responses.jsonl")) as f:
            rows += [dict(json.loads(x), run_dir_=d) for x in f if x.strip()]
    rows = score_rows(rows)
    planned, no_manifest = planned_keys(a.run_dir)
    if no_manifest:  # a directory without a frozen manifest: its observed rows stand in for its design
        for r in rows:
            if r["run_dir_"] in no_manifest and r["context"] == "attribution":
                planned.setdefault(r["model"], set()).add((r["item_id"], r["condition"], r["direction"], r["repeat"]))
    res = analyse(rows, a.s1_sesoi, planned, planned_all_contexts(a.run_dir))
    res["design_source"] = {"manifest": [d for d in a.run_dir if d not in no_manifest], "observed_rows": no_manifest}
    res["run_dirs"], res["n_cases"] = a.run_dir, len({r["item_id"] for r in rows})
    with open(os.path.join(out_dir, "analysis.json"), "w") as f:
        json.dump(res, f, indent=1, sort_keys=True)
    with open(os.path.join(out_dir, "analysis.md"), "w") as f:
        f.write(markdown(res))
    with open(os.path.join(out_dir, "v_cell_reasons.md"), "w") as f:
        f.write(v_reasons_markdown(res))
    print(markdown(res))


def v_reasons_markdown(res):
    """Every V-cell response where Q_obs was marked established, with its Q_obs reason (verbatim), for the
    qualitative check. Exploratory; the V stamp states issuer, reference, site, date and 'Status: Verified' only."""
    out = ["# V cell: Q_obs marked established after an unscoped stamp (EXPLORATORY; gold contested, spec §8.6)", "",
           "The V record states issuer, audit reference, site, date and 'Status: Verified ✓'; it names no item "
           "checked, method or finding. Reasons are verbatim model output.", ""]
    for m, r in res["models"].items():
        rs = r["V_cell_exploratory"]["reasons_when_marked_established"]
        out += [f"## {m}: {len(rs)} responses", "", "| case | repeat | P | R | Q_welfare | Q_cause | Q_obs reason |",
                "|---|---|---|---|---|---|---|"]
        ab = {"established_true": "T", "established_false": "F", "not_established": "NE", None: "–"}
        for x in rs:
            s = x["statuses"]
            reason = (x["Q_obs_reason"] or "").replace("|", "\\|").replace("\n", " ")
            out.append(f"| {x['case']} | {x['repeat']} | {ab.get(s['P'], s['P'])} | {ab.get(s['R'], s['R'])} | "
                       f"{ab.get(s['Q_welfare'], s['Q_welfare'])} | {ab.get(s['Q_cause'], s['Q_cause'])} | {reason} |")
        out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    main()
