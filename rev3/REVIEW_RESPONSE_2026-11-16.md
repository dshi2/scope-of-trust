# Response to the independent review of 957a3ca

Review: branch `audit/deep-review-2026-11-16`, `reviews/2026-11-16-independent-review.md` (commits 2a2c89c, e5e7a70).
Response head: the commit that adds this file. The item-by-item table is also in `REVISION_3_SPEC.md` §11.

| # | Finding | Response | Commit | Evidence |
|---|---|---|---|---|
| 1 | Q_welfare accepted `established_false` | Agree. Gold is NE only; refuting it counts as false refutation | 551afd5 | `test_refuting_overall_welfare_from_one_indicator_is_wrong`; probe 1 rerun below |
| 2 | Audit dates inside the claimed periods | Agree. Closed windows 2024/2025, practice claims "Throughout 2025", audits dated 2026 after closure | 551afd5 | `tests/test_cases.py` (chronology, period matching) |
| 3 | Sample records treated as population certainty; straw "permanent access" | Agree. Q_obs is the *recorded* share with matched cohorts; the straw claim is narrowed to a filled rack at every daily check, with complete check sheets | 551afd5, 2cb0429 | `cases.py` docstring; `test_q_obs_is_about_recorded_share` |
| 4 | C′ had one more filing note than C | Agree. Filler is identical in every cell (no padding). C and C′ differ only in coverage layout, with equivalent facts | 551afd5, 2cb0429 | `test_c_and_c_prime_carry_equivalent_coverage_content`; probe 3 rerun |
| 5 | Bootstrap invalid at the boundary; "100% is uninformative" is wrong | Agree on both. P4 requires a boundary-valid paired method chosen by simulated coverage; the ledger is corrected | this commit | spec §6 P4, §9; ledger P4 |
| 6 | One missing claim discarded an observed endorsement | Agree. Claim-level scoring with `partial` status and three-valued composites; harness-level failures kept separate | 2cb0429 | `test_observed_endorsement_survives_missing_claim`; probe 2 rerun |
| 7 | Coverage, blinding, causal-positive bounds | Agree. Gaps listed (lower-is-better only; no causal positive case); validation roles and blinding protocol added; causal panel in backlog | this commit | spec §7, §9a; `BACKLOG.md` |
| N | "Holding information fixed" too broad; C − B overlaps Who Verifies the Tools? | Agree. Reworded to "holding supplier assertions fixed"; contribution sentence rests on B − A and B − D1; WelfareFacts noted | this commit | spec §1 |

**Reviewer probes rerun on 2cb0429** (the logic of `reviews/reproduce_spec_findings.py`, without its assertions):
```
probe1_welfare_false_accepted: false      (was true)
probe1_false_refutation_flagged: true      (was false)
probe2_parse: partial, unsupported_q_obs: true   (was invalid / None)
probe3_C_Cprime_notes: [2, 2] in all six cases   (was [3,2] or [2,1])
```

**Still open, not claimed as done:**
- the boundary-tested statistical code and the sample-planning simulation (next deliverable)
- expert-reviewed case rubric (needs a welfare expert)
- practitioner validation
- the open decisions in spec §8
