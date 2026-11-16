# Review packet: P2 statistics and independent validation (workstream B)

For the strict methodological reviewer (ChatGPT). This packet was written by the builder (Claude, session p2-stats); it is not a self-approval. Branch `p2-revision-3` of `dshi2/scope-of-trust`. Numbers: `rev3/review/P2_NUMBERS_READY.md`. Status of this packet: **batch 1 complete; batch 2 section filled when its runs complete (§6).**

## 1. Commits (all pushed)

| commit | what |
|---|---|
| [23fafe0](https://github.com/dshi2/scope-of-trust/commit/23fafe0) | Reviewed and committed the inherited `analyze_p2.py` diff:<br>– S1–S6 secondary family, Holm within S over S2 + S3 only, X1/X2 exploratory;<br>– the scheduled denominator taken from `manifest.json` `planned_keys`.<br>Added in review:<br>– a wholly absent model is reported, not dropped;<br>– `decision` fields (P1–P3 "no decision: SESOI not set", P4 "no decision: P4 margin not set");<br>– `ci95_case_t_degenerate`;<br>– per-cell zero-event bounds (case level = headline; trial level labelled "assumes independent trials");<br>– Q_obs, Q_welfare and Q_cause by cell, separately;<br>– V-cell reasons extraction.<br>Tests: wholly absent case, wholly absent cell, absent model, no decisions without thresholds, zero-event labels |
| [2deb66f](https://github.com/dshi2/scope-of-trust/commit/2deb66f) | `check_p2_independent.py`: an independent recompute from raw `responses.jsonl` that imports nothing from `p2v3/` or `analyze_p2.py` |
| [5cd347d](https://github.com/dshi2/scope-of-trust/commit/5cd347d) | Belief-shift degenerate flag and deviation from the normative value; `v_cell_reasons.md` output |
| [5871057](https://github.com/dshi2/scope-of-trust/commit/5871057) | Plot-ready `cell_case_summary` (case values, zero-event case bound), per-context `missingness` from the manifest, P4 best attainable lower bound |
| [662676c](https://github.com/dshi2/scope-of-trust/commit/662676c) | `review/P2_NUMBERS_READY.md` (batch 1) |
| [27d37ee](https://github.com/dshi2/scope-of-trust/commit/27d37ee) | `batches_p2.py`: per-batch, pooled and between-batch results (spec §7a). `cell_case_summary` carries correct acceptance (not a zero rate) in E/E_scope improved |
| [4f53ac5](https://github.com/dshi2/scope-of-trust/commit/4f53ac5) | Coverage simulation: high within-case correlation scenario; the note now says the all-pairs cross-products are not real pairs, so calibration rests on simulation only |

Validation:
- 244 unit tests OK, 1 skipped.
- Independent recompute: **478 values compared, 0 mismatches**, covering:
  - P1–P4 observed, worst and best estimates;
  - Tango-c-cc 95% interval ends and case counts;
  - per-cell unsupported-Q_obs events, trials, cases, cases with an event, equal-case rates;
  - exact zero-event case bounds.

## 2. Claim → source (batch 1; `runs/p2_batch1_combined/analysis.json`, path under `models[<model>]`)

| claim in report | value | JSON key | final / provisional |
|---|---|---|---|
| Unsupported Q_obs events in A, A0, B, C, C′, D1, D2 | 0/60 trials, 0/12 cases, every model (Kimi A 0/58) | `zero_event_bounds.per_cell[cell].events`, `.trials`, `.cases_with_event`, `.cases` | final |
| Case-level one-sided 95% upper bound (headline) | 0.221 (rule of three 0.250) | `zero_event_bounds.per_cell[cell].upper95_cases`, `.rule_of_three_cases` | final (method); assumes exchangeable cases |
| Trial-level bound (labelled "assumes independent trials") | 0.049 (Kimi A 0.050) | `.upper95_trials_assumes_independent_trials` | reference only |
| P1/P2/P3 estimates | 0.000 | `contrasts.P{1,2,3}.observed.estimate` | final |
| P1/P2/P3 all-pairs Tango-c-cc 95% interval | [−0.301, +0.301] | `contrasts.P{1,2,3}.observed.ci95` | provisional (simulation-calibrated, conservative) |
| Case-t interval | [0, 0], degenerate | `.ci95_case_t`, `.ci95_case_t_degenerate` | descriptive only |
| Holm P1–P3 | 1.0 | `.p_holm_P1_P3` | provisional |
| Worst / best bounds | 0 / 0 (Kimi P1: −0.033 / 0) | `contrasts.P1.worst.estimate`, `.best.estimate` | final |
| P4 acceptance E vs E_scope | 60/60 vs 60/60 | `validity_checks.V1_correct_acceptance` | final |
| P4 one-sided 97.5% lower bound | −0.301 (= best attainable at K = 12) | `contrasts.P4.observed.lower_975_one_sided`, `.best_attainable_lower_975_at_these_cases` | provisional |
| P4 decision | no decision: P4 margin not set | `contrasts.P4.observed.decision` | final |
| V1–V3 | 1.000 every cell, degenerate | `validity_checks.*[cell].rate`, `.degenerate` | final |
| V: Qwen Q_obs marked established | 32/60; 12/12 cases; 0.533 [0.335, 0.731] case-t | `V_cell_exploratory.q_obs_marked_established` (`rate`, `ci95_case_t`, `events`, `cases_with_event`) | final counts; interval descriptive |
| V: Kimi | 3/60; 3/12 cases; 0.050 [0.000, 0.107] | same | same |
| V: DeepSeek, gpt-oss | 0/60 | same | final |
| V − A (Qwen), exploratory | +0.533 [+0.101, +0.801], p = 0.020 unadjusted | `secondary.contrasts.X2_V_vs_A` | exploratory |
| S5 B − A belief shift | DeepSeek +0.100, gpt-oss +0.100 (degenerate), Kimi +0.104 [0.088, 0.120], Qwen +0.052 [0.016, 0.088] | `secondary.belief.shift_B_minus_A` | final; intervals descriptive |
| S5 Qwen belief error in E unchanged / worsened | MAE 0.412 / 0.251 (gold 0) | `secondary.belief.per_cell["E/unchanged"].abs_error.mean` | final; descriptive |
| S6 approve | 0 in every cell and model | `secondary.recommendation.per_cell[cell].approve.rate` | final |
| S6 association, unsupported Q_obs × approve | not estimable (DeepSeek, gpt-oss); 0.000 degenerate (Kimi, Qwen) | `secondary.recommendation.association_unsupported_q_obs_approve` | descriptive |
| S2 P spillover in D2 | Qwen 2/60 (one case); others 0 | `secondary.rates.S2_P_spillover_in_D2` | descriptive |
| Kimi parse failures | 3 invalid (attribution), 28 malformed (belief, all truncated; V 12/60) | `quality.parse`, `missingness.belief[cell]` | final |
| Qwen D2 recommendation unparsed | 44/60 (extra `}` before `"recommendation"`) | `secondary.recommendation.per_cell["D2/none"].unparsed` | final |

## 3. Deviations from the spec and ledger (explicit)

1. **No mixed-effects logistic model.** The ledger rows P1–P3 and S2–S3 list a "mixed-effects logistic (case random intercept)" beside the interval. It is not fitted: with zero events in both arms, the model separates. Spec §6 anticipates this and asks for a prespecified fallback, but none was ever specified. Only the interval and the score test are reported.
2. **The interval method was checked on a reduced grid, not the full §6 grid.**
   - Spec §6 grid: acceptance 0.80–1.00; Δ ∈ {0, −δ/2, −δ}; SD {0, 0.5, 1.5}; repeats {1, 3, 5}; cases {30, 60, 120, 240}; three missingness patterns.
   - `SIM_P2_ALLPAIRS.md` grid: acceptance 0.90/0.99/1.00; Δ ∈ {0, −0.05}; SD {0, 1.5, 3, 5}; 5 repeats; cases {6, 12, 30, 60}; no missingness, no case × arm interaction.
   - The all-pairs construction is a heuristic use of Tango's paired formula: cross-products are not real pairs. Its calibration therefore rests on that simulation alone.
3. **Holm secondary family.** Spec §6 says "Secondary family (Holm)" over S1–S6. The ledger gives Holm only to S2 and S3. S1 is a TOST with an open margin; S4–S6 have no hypothesis test. Holm is applied over exactly S2_D2_vs_A plus the four S3 contrasts.
4. **S6 is not multinomial.** The ledger method for S6 is "multinomial by cell". We report equal-case shares per category with case-t intervals, which is descriptive. No multinomial model is fitted: "approve" is 0 everywhere.
5. **Missingness is not tested.** SCORING_SPEC §2/§7 asks to test whether parse failure depends on condition. Counts are reported per cell (`missingness`), but no test is run. Kimi's belief failures cluster in V (12/60).
6. **The zero-event bound is new.** It was added at the reviewer's request; it is not in the spec. Clopper–Pearson over cases, with "event" = a case with at least one event among its repeats.
7. **The between-batch difference method is new.** Spec §7a requires a between-batch difference but names no method. Ours: batch 2 (completed sets) − batch 1, Welch t over case-level values, descriptive.
8. **The V reasons coding is new.** It is qualitative, builder-coded, by a single coder; it is neither blinded nor validated (SCORING_SPEC §6 calls for two blinded human raters).
9. **P4's lower bound** is the lower end of the two-sided 95% all-pairs interval, i.e. a one-sided 97.5% bound. The spec says one-sided noninferiority; the level matches the spec's §6 criterion ("one-sided 97.5% lower bound").

## 4. Known weaknesses

- **Uninformative intervals at this K.**
  - At 12 cases the all-pairs interval is ±0.30. The observed P4 lower bound equals the best attainable with perfect data, so the data could not have decided P4 at any margin under 30 points.
  - Pooling batch 2 (K up to 36) narrows this to about ±0.14 at best (see §6).
- **The case bound assumes exchangeability.** It treats cases as exchangeable draws, but they are builder-written in one template family. The bound is about this builder's case population, not about welfare assurance.
- **At zero events, the score p-values are trivially 1.0.** Holm adds nothing.
- **Case-t intervals are degenerate wherever every case agrees.** That covers all primary and validity cells. Where events are rare (Kimi V: 3 single events), the clipped case-t interval is rough.
- **The independent recompute covers only part of the output**: the primary contrasts and per-cell Q_obs. The secondary outputs (S1–S6, belief, recommendations) are verified by synthetic unit tests with known answers, not by an independent re-implementation.
- **Scoring is strict.** In 44 of 60 Qwen D2 responses the recommendation is lost to an extra brace (by spec, no lenient repair). The 3 invalid and 28 malformed Kimi outputs are missing; the worst/best bounds cover them.
- **Stale synthetic fixture.** `sim_out/synth_analysis/analysis.json` (a synthetic fixture used by plot tests) was generated with the pre-review code, and its figures are owned by the plots session. It is not a paper input.
- **Belief vs attribution in Qwen.** Qwen refutes Q_obs in E unchanged/worsened 100% of the time, yet states p(Q_obs) ≈ 0.25–0.44. This dissociation is reported descriptively; it is not interpreted.

## 5. Questions for the reviewer

1. Is the headline zero-event bound right: Clopper–Pearson over cases, with "event" = a case with at least one event among its repeats (22.1% at K = 12; about 8.0% at K = 36)? Or would you prefer a bound on the equal-case mean rate, e.g. beta-binomial?
2. V-cell reading. In 20/32 of Qwen's established-Q_obs responses, the stated reason attributes to the bare stamp a finding it does not contain. Is it acceptable to call those responses "unsupported on the document's own terms" while leaving the 8/32 "Verified covers the site's records" readings as contested?
3. Is Welch on case-level values (batch 2 − batch 1) an acceptable descriptive between-batch difference? Or should it be per-set estimates only, given that every primary cell is at 0?
4. Holm over S2 + S3 only (ledger reading) versus all of S1–S6 (spec §6 wording): which governs?
5. With the observed P4 lower bound equal to the best attainable at this K, should P4 appear in the main results table at all, or only as "not decidable at K = 12/36"?
6. With no fallback prespecified, should the absent mixed-effects model be listed as a protocol deviation in the paper?

## 6. Batch 2 (spec §7a)

Pending. When `summary.json` of `runs/p2_ba_v1`, `runs/p2_bb_v1` and `runs/p2_bc_v1` shows `complete: true`, this section and `P2_NUMBERS_READY.md` §8 get:
- per-batch results (`runs/p2_<batch>_analysis`);
- pooled results over all completed batches (`runs/p2_all_batches`);
- the between-batch difference (`runs/p2_all_batches/between_batch.json`);
- the independent recompute for each of them.
