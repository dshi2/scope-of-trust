# P2 numbers ready: workstream B (p2-stats)

Status at 16:35 IST, 16 Nov 2026. **Batch 1 is ready.** Batch 2 (ba, bb, bc) is still running: see §8 (it is appended when `summary.json` shows `complete: true`).

## 0. Provenance

| What | Where |
|---|---|
| Code commit for these numbers | `5871057` (branch `p2-revision-3`): `analyze_p2.py`, `check_p2_independent.py`, `tests/test_secondary_p2.py` |
| Command | `python3 analyze_p2.py --run-dir runs/p2_dev_eval_v1 runs/p2_ext_v1 --out runs/p2_batch1_combined` |
| Analysis (single numerical source) | `rev3/runs/p2_batch1_combined/analysis.json` (+ `analysis.md`, `v_cell_reasons.md`). `runs/` is gitignored; WS-F publishes a tracked copy under `rev3/results/` |
| Independent check | `python3 check_p2_independent.py --run-dir runs/p2_dev_eval_v1 runs/p2_ext_v1 --analysis runs/p2_batch1_combined` → **478 values compared, 0 mismatches** (`runs/p2_batch1_combined/independent_check.json`). It shares no code with the analysis module (own JSON extraction, own Q_obs gold rule, own case aggregation, own all-pairs Tango-c-cc). It covers P1–P4 observed/worst/best estimates, intervals and case counts, and per-cell unsupported-Q_obs events, trials, cases, rates and zero-event case bounds. Secondary outputs (S1–S6) are checked by unit tests on synthetic data with known answers (`tests/test_secondary_p2.py`), not by the independent script |
| Design denominator | `manifest.json` `planned_keys` of both runs (3,360 + 3,360). Planned = returned for every key. Tests: a wholly absent case, cell or model is counted as missing in the worst/best bounds, not dropped |
| Tests | 244 OK, 1 skipped (`python3 -m unittest discover -s tests`, from `rev3/`) |

JSON paths below are relative to `analysis.json` → `models[<model>]`. Models: `deepseek-v3.2`, `gpt-oss-120b`, `kimi-k2-0905`, `qwen3-235b-a22b-2507`.

**Final vs provisional.**
- **Final (for batch 1, pending ChatGPT review):** counts, rates, case counts, exact zero-event case bounds, validity rates, belief means and errors, recommendation shares, V counts.
- **Provisional:**
  - every interval. The all-pairs Tango-c-cc interval is calibrated by simulation only (`SIM_P2_ALLPAIRS.md`) and is conservative. The case-t interval is descriptive, and degenerate wherever every case agrees.
  - every p-value.
- **No decision anywhere:** no SESOI and no P4 margin are fixed.

## 1. Data quality (batch 1; `quality`, `missingness`)

- **Calls.** 1,680 per model (840 attribution + 840 belief), all with transport status `ok`.
- **Parse:**
  - DeepSeek, gpt-oss and Qwen: 1,680 ok.
  - Kimi: 1,649 ok, 28 malformed, 3 invalid; 28 truncated.
- **Kimi's failures by context:**
  - Attribution: 3 invalid (A: 2, E/worsened: 1), so Q_obs is usable in 837/840.
  - Belief: 28 malformed, all truncated at the length cap: V 12, A0 4, E_scope/worsened 4, E/improved 2, E/unchanged 2, E_scope/unchanged 2, E/worsened 1, D2 1. Belief missingness depends on cell for Kimi (V 12/60 against ≤ 4/60 elsewhere). This is descriptive; no test is run.
  - Path: `missingness.belief[cell].missing`.
- **Qwen recommendation.** For Qwen, 44/60 D2 attribution responses have **no parseable recommendation** (`secondary.recommendation.per_cell["D2/none"].unparsed` = 44).
  - Cause: Qwen emitted one extra `}` after the `claims` object, so `"recommendation"` falls outside the first JSON object. The claims are intact and the parse is `ok`.
  - Per the scoring spec there is no lenient repair, so these recommendations count as missing.
  - A text search finds `"request_more_evidence"` in all 60, so S6 conclusions do not change.
- **Served provider and model:** one per model (`quality.served_provider`, `quality.served_model`).

## 2. Primary endpoint: unsupported Q_obs (batch 1, 12 cases × 5 repeats)

**Every model × every error cell had 0 events.**
- Cells covered: A, A0, B, C, C′, D1, D2, E/E_scope worsened and unchanged, and (for DeepSeek and gpt-oss) V.
- Counts: 0/60 per model per cell, except Kimi A (0/58, 2 unparsable) and Kimi E/worsened (0/59).
- Path: `zero_event_bounds.per_cell[cell]`.

**Zero-event bound (headline = case level):**

| quantity | value | JSON key | status |
|---|---|---|---|
| cases with an event / cases, each error cell | 0/12 | `zero_event_bounds.per_cell[cell].cases_with_event`, `.cases` | final |
| exact one-sided 95% upper bound, case level | **22.1%** (= 1 − 0.05^(1/12)) | `.upper95_cases` | final (method); interpretation below |
| rule of three (≈ 3/K) | 25% | `.rule_of_three_cases` | approximation |
| trial-level bound, **assumes independent trials** | 4.9% (0/60); Kimi A 5.0% (0/58) | `.upper95_trials_assumes_independent_trials` | reference only; must carry the label |

- **Interpretation of 22.1%.** It bounds the probability that a case drawn from the builder's case population shows the error in any of its 5 repeats, and so it also bounds the equal-case rate. It treats the 12 cases as exchangeable draws, but they are builder-written, not sampled. Repeats are nested in cases, so 5 × 12 is not 60 independent units.
- **Joint 90% range for a contrast's difference**, from the two arms' case bounds: [−0.221, +0.221] for each of P1–P3 (`contrasts.P1.observed.exact_arm_bounds.delta_range_joint90`).

**Contrasts P1–P3 (`contrasts.P{1,2,3}.observed`), identical for all four models:**

| contrast | estimate | all-pairs Tango-c-cc 95% CI (provisional) | case-t 95% CI | p vs 0 (Holm P1–P3) | worst / best bounds | cases | decision |
|---|---|---|---|---|---|---|---|
| P1 B − A | 0.000 | [−0.301, +0.301] | [0, 0] **degenerate** | 1.0 (1.0) | 0.000 / 0.000 (Kimi −0.033 / 0.000) | 12 | no decision: SESOI not set |
| P2 B − D1 | 0.000 | [−0.301, +0.301] | [0, 0] degenerate | 1.0 (1.0) | 0.000 / 0.000 | 12 | no decision: SESOI not set |
| P3 C − B | 0.000 | [−0.301, +0.301] | [0, 0] degenerate | 1.0 (1.0) | 0.000 / 0.000 | 12 | no decision: SESOI not set |

Keys:
- `estimate`, `ci95`, `ci95_case_t`, `ci95_case_t_degenerate`, `p_two_sided_vs_0`, `p_holm_P1_P3`, `cases`, `decision`;
- bounds: `contrasts.P1.worst.estimate` and `contrasts.P1.best.estimate`.

Kimi's P1 worst case (−0.033) imputes its 2 unparsable A trials as errors (one case, 2/5 → −0.4/12).

**The components are also all zero**: Q_cause, Q_welfare and the Q_obs-or-Q_cause composite are 0.000 [−0.301, +0.301] for P1–P3 and every model (`components.P{1,2,3}.<component>`). Only Q_obs is confirmatory.

**P4 (E_scope − E, improved; correct acceptance), `contrasts.P4.observed`:**
- Acceptance was 60/60 in both arms for every model (V1).
- Estimate 0.000; one-sided 97.5% lower bound **−0.301** (`lower_975_one_sided`).
- −0.301 is also the **best attainable** lower bound with perfect data at 12 cases (`best_attainable_lower_975_at_these_cases`). The data could not have shown more.
- `decision` = "no decision: P4 margin not set". **Not noninferior.** −0.301 fails any margin under 30 points. Per `SIM_P2_ALLPAIRS.md`, a 5-point margin needs at least 92 cases, even with perfect data.
- `exact_arm_bounds.delta_range_joint90` for P4 is [−1, 1]. That is an upper-bound construction for error rates; it is meaningless at 100% acceptance, so do not cite it.

## 3. Validity / positive controls (`validity_checks`)

All four models, all cells: rate **1.000**, 12 cases, 60 trials (Kimi E/worsened 59). The case-t interval is [1, 1], flagged **degenerate** (`degenerate: true`): zero width is not precision.
- V1 correct acceptance: E/improved, E_scope/improved.
- V2 correct refutation: E and E_scope, worsened and unchanged.
- V3 manipulation check: B, C, C′ (P marked true), D1 (R), D2 (S).

The positive controls pass. As the spec says, they show only that the instrument registers obvious audited outcomes, not that it is sensitive to subtle spillover.

## 4. Secondary family (S1–S6), batch 1; `secondary`

The Holm S family is exactly S2_D2_vs_A, S3_cause_B_vs_A, S3_cause_B_vs_D1, S3_cause_C_vs_B and S3_overreach_Escope_vs_E (`secondary_holm_family`).

- **S1–S3 contrasts:** every S contrast is **0.000 [−0.301, +0.301], p = 1.0, Holm p = 1.0**, for all models (`secondary.contrasts.<id>`). S1 C′ − C: `decision` "no decision: SESOI not set". S1 is a TOST with an open margin and is not in Holm.
- **Q_obs, Q_welfare and Q_cause, analysed separately** for all 14 cells (`outcome_rates_by_cell[cell][unsupported_q_obs|unsupported_q_welfare|unsupported_q_cause]`):
  - All are 0.000 with 0/12 cases with an event, except in V: Qwen Q_obs 0.533, Kimi Q_obs 0.050 and Kimi Q_welfare 0.017 (1/60, 1 case).
  - Evidence hierarchy A / B / D1 / C: all three outcomes are 0.000 for every model (`evidence_hierarchy`).
- **Single-arm S rates** (`secondary.rates`):
  - S2 P marked true in D2 (place spillover): DeepSeek, gpt-oss and Kimi 0.000. Qwen **0.033** (2/60, both in one case, `dev-hen-cagefree`) [0.000, 0.107], descriptive.
  - S3 causal overreach in E improved and E_scope improved: 0.000 for all models.
  - S4 Q_welfare in E improved: 0.000 for all models.
- **S5 belief** (separate elicitation, context 2, with the stipulated model; never pooled with attribution; `secondary.belief`). B − A shift against the normative +0.10 (`shift_B_minus_A`):

  | model | mean shift | case-t 95% CI | note |
  |---|---|---|---|
  | DeepSeek | +0.100 | [0.100, 0.100] **degenerate** | reproduces the stipulated arithmetic in every case |
  | gpt-oss | +0.100 | [0.100, 0.100] degenerate | MAE 0.000 in every cell |
  | Kimi | +0.104 | [+0.088, +0.120] | |
  | Qwen | **+0.052** | [+0.016, +0.088] | below normative (interval excludes +0.10); `deviation_from_normative` −0.048 |

  Mean absolute error by cell (`per_cell[cell].abs_error.mean`), with signed error and its interval under `.signed_error`:
  - DeepSeek: 0 in A–D2; ≤ 0.035 in the E family.
  - gpt-oss: 0 everywhere.
  - Kimi: 0.010–0.036 in A–D2; E/unchanged 0.145, E_scope/unchanged 0.167, E_scope/worsened 0.127.
  - Qwen: A 0.033, A0 0.148 (signed +0.148), B 0.065, C 0.087; **E/unchanged 0.412, E_scope/unchanged 0.443, E/worsened 0.251, E_scope/worsened 0.244** (gold 0).

  Qwen's attribution refutes Q_obs 100% in those cells (V2), but its stated probability stays 0.24–0.44. This is a descriptive dissociation between the two elicitations, not a tested claim.
- **S6 recommendations** (equal-case shares; `secondary.recommendation.per_cell`):
  - "approve" = 0.000 in every cell for every model.
  - "request_more_evidence" = 1.000 in A, A0, B, C, C′, D1, D2, E/E_scope improved and V.
  - "reject" appears only in E/E_scope worsened and unchanged. For example, E/worsened reject: DeepSeek 0.95, gpt-oss 0.80, Kimi 0.93, Qwen 0.50.
  - Counts per cell: `secondary.recommendation.counts`.
- **Within-response association, unsupported Q_obs × approve** (`secondary.recommendation.association_unsupported_q_obs_approve`; descriptive, not mediation):
  - Not estimable for DeepSeek and gpt-oss (no unsupported trial).
  - Degenerate 0.000 for Kimi (3 unsupported trials, 0 approve) and for Qwen (32 unsupported trials, 0 approve).
  - Report: "no response approved, so there is no association to estimate."

## 5. Exploratory X1 / X2, and the V cell

- **X1 A0 − A:** 0.000 [−0.301, +0.301] for all models.
- **V cell (exploratory; gold contested, spec §8.6).** Q_obs marked established after an unscoped stamp. Keys: `V_cell_exploratory.q_obs_marked_established`, `cell_case_summary["V/none"]`.

  | model | trials marked / 60 | cases with ≥ 1 / 12 | equal-case rate [case-t 95%, clipped] | V − A all-pairs Tango-c-cc 95% (unadjusted p) |
  |---|---|---|---|---|
  | Qwen3-235B | 32 | **12** | **0.533 [0.335, 0.731]** | +0.533 [+0.101, +0.801] (p = 0.020) |
  | Kimi-K2 | 3 | 3 | 0.050 [0.000, 0.107] (lower end clipped; 3 single events, so the t interval is rough) | +0.050 [−0.264, +0.364] (p = 0.90) |
  | DeepSeek-V3.2 | 0 | 0 | 0.000 (case bound 22.1%) | 0.000 [−0.301, +0.301] |
  | gpt-oss-120b | 0 | 0 | 0.000 (case bound 22.1%) | 0.000 [−0.301, +0.301] |

  - V − B gives identical numbers, because B is 0 (`secondary.contrasts.X2_V_vs_A`, `X2_V_vs_B`).
  - X contrasts are never in Holm.
  - The p-value is from the same simulation-calibrated method and is exploratory.

- **Other claims marked established in V** (all 60 trials):

  | model | P | R (fire/building safety) | Q_welfare | Q_cause | recommendation |
  |---|---|---|---|---|---|
  | Qwen | 41/60 | **60/60** | 0 | 0 | request_more_evidence 60/60 |
  | Kimi | 19/60 | 4/60 | 1/60 | 0 | request_more_evidence 60/60 |
  | DeepSeek | 0 | 19/60 | 0 | 0 | request_more_evidence 60/60 |
  | gpt-oss | 0 | 21/60 | 0 | 0 | request_more_evidence 60/60 |

  So DeepSeek and gpt-oss also credit the bare stamp, but only for the inspection-type claim R, never for Q_obs.

- **What the V record contains.** Issuer, audit reference, site, date, and "Status: Verified ✓". There is no item checked, no method and no finding (checked against `stimuli_dev.jsonl`).

- **Qualitative check of the reasons.** All 35 reasons are in `runs/p2_batch1_combined/v_cell_reasons.md` (verbatim). This coding is by the builder (Claude), a single coder, not blinded and not validated; it is a reading aid, not a measurement.
  - **(a) The reason attributes a finding to the stamp that the record does not contain** ("the audit confirms the recorded share decreased"): Qwen 20/32, Kimi 1/3.
  - **(b) The reason reads "Verified" as covering the site's records or data in general**, so the recorded share follows. This is the contested blanket reading that spec §8.6 leaves open: Qwen 8/32, Kimi 2/3.
  - **(c) The reason treats the claim as checkable, or as checked against sources not in the file** ("can be independently checked", "routine slaughterhouse records"): Qwen 4/32.

  Excerpts (verbatim, with case and repeat):
  1. Qwen, `dev-dairy-cubicle` r2 (a): "The audit record confirms the recorded share of lame cows decreased from 2024 to 2025."
  2. Qwen, `dev-hen-cagefree` r1 (a): "The audit includes verified observational data showing a lower recorded share of keel bone fractures … which has been independently confirmed."
  3. Qwen, `dev-rabbit-mats` r4 (b): "The audit status is verified and the statement reports a recorded observation, which implies documentation that has been checked by the inspecting body."
  4. Qwen, `dev-turkey-darkness` r2 (c): "… is an observable metric that can be independently checked and confirmed."
  5. Kimi, `dev-turkey-darkness` r2 (b): "The audit record from Calloway & Reid Farm Audit LLP with status 'Verified' provides independent verification of this claim."

  **Reading.**
  - For responses of type (a), "unsupported" is warranted on the document's own terms: the stated reason cites findings the record does not contain.
  - Type (b) depends on the contested gold for V.
  - Recommended wording: "marked established after an unscoped stamp; in most of Qwen's responses the stated reason attributes to the stamp a finding it does not contain". Do not write "error" without that qualifier, and do not present V as a confirmed hypothesis.

## 6. Recommended wording (batch 1)

> In batch 1 (12 builder-written development cases, 5 repeats each, four models), no model marked the unaudited outcome claim Q_obs as established after a practice audit, an other-topic audit, a sister-site audit or no audit: 0 events in every such cell for every model (0/60 trials, 0/12 cases per cell). With zero events in all 12 cases, the exact one-sided 95% upper bound on the per-case probability of the error is 22.1% per model and cell (rule of three ≈ 25%), treating the cases as exchangeable draws from the builder's case population. The contrasts P1 (B − A), P2 (B − D1) and P3 (C − B) are therefore 0.000, with all-pairs Tango-c-cc 95% intervals of [−0.30, +0.30]. These intervals are calibrated by simulation only and are conservative. The case-level t interval collapses to [0, 0] and is degenerate, not precise. No smallest effect of interest is fixed, so we make no equivalence claim: the data are compatible with no spillover, and do not exclude a per-case error probability up to about 22%. Correct acceptance of audited outcome evidence was 100% with and without the coverage statement. With no margin fixed, P4 is "no decision": its lower bound of −0.30 is the best attainable at 12 cases and does not show noninferiority.

**Safe headline claims:**
- "0 of 12 cases (0/60 trials) per model in every practice-audit and control cell; case-level 95% upper bound 22%."
- "Positive controls at ceiling (V1–V3 = 1.00 in every cell and model); degenerate intervals."
- "Exploratory: after an unscoped 'Verified' stamp, Qwen3-235B marked Q_obs established in 32/60 trials, in all 12 cases (0.53, case-t 95% 0.34–0.73); Kimi-K2 3/60; DeepSeek and gpt-oss 0/60."
- "No model recommended approval in any cell."

**Unsafe (do not write):**
- "upper bound 4.9%" without "assumes independent trials", or as the headline;
- "60 cases";
- "equivalent", "no effect", "models do not / cannot make this error";
- "P4 noninferior", "coverage statements preserve acceptance";
- "V error rate" as a confirmed finding, or "the stamp causes errors" as a primary result;
- any pooled-across-model estimate;
- "replicated" for batch 2 (it is later development batches);
- any confirmatory language.

## 7. Requests from other workstreams (`review/REQUESTS.md`), status

- **C, 16:30.** Done in `5871057`.
  - `models[m].cell_case_summary[cell]` has `equal_case_mean`, `cases`, `cases_scheduled`, `events`, `cases_with_event`, `scored`, `scheduled`, `ci95_case_t`, `degenerate`, `zero_event_upper_case`, `correct_here` and `case_values`; the method is in the top-level `cell_case_summary_method`.
  - `models[m].missingness[context][cell]` has `scheduled`, `returned`, `usable` and `missing`.
  - The per-batch, pooled and between-batch outputs use the same schema (§8).
- **E, 16:28.** Items 1–7 are answered in §§1–5 above for batch 1. Item 7 (Qwen D2 unparsed 44) is in §1. Batch-2, pooled and between-batch numbers follow in §8.

## 8. Batch 2, pooled and between-batch (spec §7a)

Pending: ba, bb and bc were still running at 16:35 (`python3 run_p2.py --status --run-dir runs/p2_b?_v1`). The plan, fixed now, before the batch-2 analysis:
- **Per batch:** `runs/p2_ba_analysis`, `runs/p2_bb_analysis`, `runs/p2_bc_analysis`, each a single-run `analyze_p2.py`.
- **Pooled over every completed batch:** `runs/p2_all_batches` (batch 1 + every complete batch-2 set).
- **Between-batch difference:** batch 2 (completed sets) − batch 1, for each per-cell rate and each contrast. Welch t over case-level values; cases are independent across batches. Descriptive.
- A batch that is not complete is listed as incomplete and excluded.
