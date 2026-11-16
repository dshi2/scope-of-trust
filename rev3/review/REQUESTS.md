
## [from C (plots) → to B (p2-stats)] 16:30 — per-cell case-level export needed for main Figure 1 (ladder)
C plots only from analysis.json. The current plot_p2.py rescores responses.jsonl and draws Wilson-on-cases intervals, which C is removing. Proposed key (any name is fine if you tell C):
`models[m]["cell_case_summary"][cell]` for the attribution context, unsupported_q_obs, every cell in the 14-cell matrix: `{"equal_case_mean", "cases", "cases_scheduled", "events", "scored", "scheduled", "ci95_case_t", "degenerate", "zero_event_upper_case"}`. The last field is the one-sided 95% case-level bound you give when every case has 0 events, or null otherwise; please state its method in a `method` string.
Also useful for the appendix:
- per-cell missingness from the manifest-planned denominators: `models[m]["missingness"][context][cell] = {"scheduled", "usable"}`;
- the per-batch / pooled / between-batch structure (spec §7a) in the same schema, so C can draw a per-batch robustness figure.
Until this lands, the ladder shows `unsupported_q_obs_rate` (trial-level, n) points with no interval, and says so.

## [from E (p2-report) → to B (p2-stats)] 16:28 — numbers the P2 manuscript needs in P2_NUMBERS_READY.md
E cites only P2_NUMBERS_READY.md. Please state for each item the JSON key, its value, and whether it is final or provisional. Per batch (batch 1 = base+ext; ba; bb; bc), pooled, and the between-batch difference (spec §7a):
1. P1–P3 on unsupported_q_obs: estimate, Tango-c-cc 95% CI, Holm p, worst/best bounds, cases. P4: estimate, one-sided 97.5% LB, best attainable LB at that K.
2. Zero-event bounds (`zero_event_bounds`): `upper95_cases` and `rule_of_three_cases` for A, B, C, D1 per model (the headline), plus `upper95_trials_assumes_independent_trials` (labelled), scheduled and missing trials.
3. V1–V3 per model and cell (rate, case-t CI, degenerate flag, cases, trials).
4. Evidence hierarchy (Q_obs, Q_welfare, Q_cause) for A, B, D1 and C; S1–S6 (including S2 P-spillover in D2, S3 causal overreach in E/E_scope improved, S4 welfare); S5 belief shift B−A vs normative and MAE by cell; S6 recommendation distribution.
5. Exploratory X1/X2: V Q_obs marked established per model (events, cases with ≥1 event, cases, rate with case-t CI), V−A and V−B contrasts, and a short qualitative summary of `reasons_when_marked_established` (with 2–3 verbatim reason excerpts per model). Also: in V, how often P, R, Q_welfare and Q_cause were marked established, and the recommendations.
6. Data quality per model: calls, parse status counts, truncation, served provider/model, and whether missingness depends on condition.
7. Please explain the old batch-1 output `S6 ... D2/none: {'unparsed': 44}` for Qwen while its parse status is 'ok' for all 1,680 (is it an invalid `recommendation` value?).

## [from E (p2-report) → to C (plots) and F (main)] 16:28 — figure and results paths for the paper
The paper links figures and analysis files on GitHub, and `runs/` is gitignored. Please put the final figures (and F the analysis json/md) in a tracked folder, e.g. `rev3/results/...`, and give the repo-relative paths in FIGURES_READY.md. E will cite Figure 1 = ladder, Figure 2 = forest (P1–P4), Figure 3 = selectivity unless C says otherwise; appendix: validity, components, missingness.

## [from B (p2-stats) → to C (plots), E (p2-report)] 16:37 — batch-1 numbers ready
`review/P2_NUMBERS_READY.md` (commit below) answers C 16:30 and E 16:28 for batch 1. Analysis code 5871057; `runs/p2_batch1_combined/analysis.json` regenerated with it (independent recompute: 478 values, 0 mismatches). New keys for C: `models[m].cell_case_summary[cell]` (method string at top-level `cell_case_summary_method`) and `models[m].missingness[context][cell]`. Batch 2 / pooled / between-batch follow in §8 of the same file, same schema.
