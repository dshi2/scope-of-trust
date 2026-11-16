# All-pairs Tango-c-cc: coverage re-check (P2, 2026-11-16)

**Question.** `analyze_p2.py` now builds each case's counts with `stats.all_pairs_counts`: every X repeat is paired with every Y repeat, so repeat index carries no matching. The interval is still Tango-c with a continuity correction, `stats.tango(s, 0.025, conservative=True, cc=0.5)`. A reviewer pointed out that the old index pairing was not a real matched pair. This note checks whether the new construction still covers, and compares it with the case-level t interval (`analyze_p2.case_t`).

**How it was run.** `python3 sim_p2_allpairs.py --reps 40000 --out sim_out`, using the existing generator `p2v3/simulate.py`. Arms X (E_scope) and Y (E) are independent Bernoulli draws given a shared case logit effect, with marginal rates calibrated exactly. There are no missing outcomes. Seed 2026111661; 48 points; 40,000 replicates per point; run time 136 s. Monte Carlo SE at 2.5% non-coverage is 0.08 pp, and 0 misses in 40,000 means the true rate is ≤ 0.0075% (95%). Full table: `sim_out/sim_p2_allpairs_tables.md`; CSV: `sim_out/sim_p2_allpairs.csv`. (`PRECISION_REPORT.md` is not present in rev3, so this note does not depend on it.)

**Grid.** E acceptance 0.90 / 0.99 / 1.00; Δ = E_scope − E ∈ {0, −0.05}; case random-effect SD 0 / 1.5; 5 repeats; 6 / 12 / 30 / 60 cases.

## Headline

| method | max one-sided 97.5% lower non-coverage | min two-sided 95% coverage | points over 3% | widths (pp) |
|---|---|---|---|---|
| **all-pairs Tango-c-cc** (current) | **0.00%** at every point | **100.0%** at every point | **0 / 48** | 15–105 |
| case-level t | 29.2% (p_E 1.00, Δ −0.05, SD 1.5, K 6) | 70.7% (same point) | 21 / 48 | 0–41 |
| index-paired Tango-c-cc (old) | 0.00% | 100.0% | 0 / 48 | same as all-pairs |

1. **All-pairs Tango-c-cc is valid on this grid, with a wide margin.** It had no lower-bound miss and no upper-bound miss in 1.92 M replicates. It meets the ≤ 3% target everywhere, including at the ceiling (p_E = 1.00) and with only 6 cases.
2. **The case-level t interval fails exactly where P4 lives.** Near the ceiling with Δ = −0.05, its one-sided non-coverage is 13–29% at K = 6, 4–9% at K = 12–30, and still 3.8–7.4% at K = 60 (p_E 0.99 and 1.00). At p_E = 1.00 and Δ = 0 it has zero width in 100% of replicates. Its coverage is acceptable only away from the boundary (p_E 0.90, Δ = 0: 0.7–2.6%).
3. **Switching from index pairs to all pairs costs nothing.** Coverage and mean width are the same to 0.1 pp. Per replicate, the lower bound moves by up to about 2 pp (mean shift < 0.04 pp), because b − c is identical under both constructions and only b + c changes. The all-pairs version removes the dependence on arbitrary repeat labels and keeps the same guarantees. This answers the reviewer.
4. **The price is precision: the interval is very conservative.** Its realised non-coverage is 0% against a nominal 2.5%. With deff fixed at 1, each case counts as one pair, so the 5 repeats add no precision; the continuity correction widens it further. Even with perfect acceptance in both arms on every case, the best attainable P4 lower bound is:

| cases | 6 | 12 | 30 | 60 | 120 |
|---|---|---|---|---|---|
| best possible lower bound (pp), perfect data | −48.3 | −30.1 | −14.1 | −7.5 | −3.9 |

The smallest K that can show noninferiority with perfect data is **92 cases for a 5 pp margin, 45 for 10 pp, and 29 for 15 pp**. With real errors it takes more. One E_scope failure in one case's 5 repeats moves the bound by about 0.6–3 pp.

## Recommendation for the PI

- **Keep all-pairs Tango-c-cc as the reported interval for P1–P4.** It is pairing-free, label-invariant, and meets the §6 coverage requirement with room to spare. Do not use the case-level t interval for any decision. Show it at most as a descriptive comparison, labelled anti-conservative near the ceiling and degenerate when every case agrees.
- **Fix the P4 margin with the case count in view, before reading data.** At 6 development cases, no sensible margin is decidable: the interval spans about ±48 pp even with perfect data. The figures and `analysis.md` should present P4 as descriptive until K is large enough for the chosen margin. For example, a 10 pp margin needs K ≥ 45 at the very least, and realistically more.
- **Optional, if time allows after the deadline:** recover some power by re-checking a less conservative variant on all-pairs counts, such as Tango with estimated deff (`stats.tango(s, conservative=False, cc=0.5)`). With all-pairs cells, the within-case cell proportions are products of the arm rates, so the deff estimate behaves differently from the index-paired case and needs its own coverage run. Do not switch without that run. On today's evidence, the conservative method is the safe choice.

## Limits of this check

This is a reduced grid: one Y baseline per row, Δ only 0 and −0.05, 5 repeats, no missing or parse-failure outcomes, one model per analysis, and no model heterogeneity. Missingness enters `analyze_p2.py` through per-arm dropping plus worst/best imputation. That path was not simulated here. The earlier precision grid covered it only for index-paired counts.
