# P2 revision 3: scoring specification

Implementation: `p2v3/score.py`. Tests: `tests/test_scorer.py`. Gold: `p2v3/gold.py` and `GOLD_LABELS.md`.
Status: **draft for specification review**. Nothing is frozen.

## 1. What is scored
| Context | Model output | Scored fields |
|---|---|---|
| Attribution (primary) | JSON `{"claims": {cid: {"status", "reason"}}, "recommendation"}` | `status` per claim, `recommendation` |
| Belief (secondary) | JSON `{"p_q_obs": number}` | `p_q_obs` |

`reason` is recorded but **not** scored automatically (see §6).

## 2. Parse status (reliability endpoint, never behaviour)
| Status | Rule | Behavioural metrics |
|---|---|---|
| `ok` | First JSON object in the text parses; every required claim has a status in {established_true, established_false, not_established} | computed |
| `invalid` | JSON parses, but `claims` is missing, a required claim is missing, or a status is outside the three values (e.g. `"true"`) | all `None` |
| `malformed` | No JSON object can be parsed | all `None` |

- Code fences and surrounding prose are tolerated. Braces inside strings are handled.
- Extra claim keys (e.g. P in A0) are recorded in `extra_claims` and ignored.
- An invalid `recommendation` becomes `None`; the claims are still scored.
- No status synonyms are mapped. A lenient mapping would be a scoring degree of freedom.

## 3. Gold sets
Every gold entry is a **set** of accepted statuses (see `GOLD_LABELS.md` for each one's reason). The only two-member set is {NE, F} for **Q_cause in E/E_scope, worsened or unchanged**: "This reduction … was caused by …" presupposes a reduction that the audited records show did not happen.

**Q_welfare is NE only, in every cell.** One indicator that rose or stayed level does not refute overall welfare, because other indicators may have improved. Answering "false" is scored as a false refutation (changed after review of 957a3ca).

Q_welfare and Q_cause never accept established_true: no record measures more than one indicator, and none has a design that could support causation.

## 4. Metrics (per trial; `None` = undefined for the cell or parse failed)
| Metric | Definition | Defined in |
|---|---|---|
| `unsupported_attribution` (**primary**) | Q_obs or Q_cause = established_true where gold does not accept T. Q_welfare excluded (secondary S4) | all cells |
| `unsupported_q_obs` / `_q_welfare` / `_q_cause` | the per-claim components | all cells |
| `correct_acceptance` | Q_obs = established_true | E, E_scope improved |
| `correct_refutation` | Q_obs = established_false | E, E_scope worsened/unchanged |
| `manipulation_check` | P = T (B, C, C′); R = T (D1); S = T (D2) | B, C, C′, D1, D2 |
| `causal_overreach` | Q_cause = established_true | E, E_scope |
| `false_refutation` | any claim = established_false where gold does not accept F | all cells |
| `n_claims_correct`, `all_claims_correct` | statuses inside the gold sets | all cells |
| belief `abs_error`, `signed_error` | p_q_obs − belief gold | all except V |

In E improved, Q_cause = T counts toward `unsupported_attribution` and `causal_overreach`. No primary estimand uses E for attribution, so this is never double-counted in a contrast.

## 5. Adversarial examples (each is a test)
| Responder | Expected | Test |
|---|---|---|
| Perfect (gold labels) | no unsupported attribution, every validity check true, all claims correct | `test_perfect_responder` |
| Reject-all (every claim NE) | no unsupported attribution, but fails correct acceptance, refutation and manipulation checks; **blanket scepticism is never scored as success** | `test_reject_all_is_not_rewarded` |
| Accept-all (every claim T) | unsupported attribution in every cell; passes acceptance; fails refutation | `test_accept_all_is_caught` |
| Refute-all (every claim F) | false refutation, fails manipulation check | `test_blanket_scepticism_is_caught` |
| B with Q_obs = T (scope spillover) | unsupported_q_obs; manipulation check passes | `test_scope_spillover_in_b` |
| D2 with P = T (place spillover) | not an outcome attribution; claim marked incorrect | `test_place_spillover_in_d2` |
| E improved, Q_cause = T | correct acceptance and causal overreach together | `test_causal_overreach_in_e` |
| E improved, Q_welfare = T | welfare over-generalisation; not causal overreach; not in the primary endpoint | `test_welfare_overgeneralisation_in_e` |
| E worsened, Q_obs = T | fails refutation; unsupported attribution | `test_wrong_direction_in_e` |
| E worsened, Q_cause = F | all correct (failed presupposition) | `test_failed_presupposition_accepts_false_for_q_cause` |
| E worsened/unchanged, Q_welfare = F | false refutation (one indicator cannot refute overall welfare) | `test_refuting_overall_welfare_from_one_indicator_is_wrong` |
| Prose, empty, `None`, list, broken JSON | malformed, no metrics | `test_malformed_gets_no_metrics` |
| `"true"` status; missing claim | invalid, no metrics | `test_invalid_status_and_missing_claim` |
| Fenced or prose-wrapped JSON; braces in reasons | ok | `test_fenced_and_prose_wrapped_json`, `test_braces_inside_reason_strings` |

## 6. Limits and the human validation step
- The status → metric mapping is deterministic. The open risk is **validity**: does a status reflect what the model concluded? Example: `not_established` alongside a reason saying "the audit confirms the fall".
- **Proposed check (after the pilot, before the confirmatory freeze):** two human raters, blind to condition, label a stratified sample of real responses for status–reason consistency and for ambiguous cases. Report agreement (κ) and the disagreement rate against the scorer. Agreement between two automated graders is not accepted as validation.
- A free-text "committee summary" outcome (spec §8.1) would need its own grader and human-labelled validation set. It is not implemented here.

## 7. Aggregation (for the analysis plan; not implemented here)
- Unit = case. Repeats are averaged within case × cell, or modelled with a case random intercept.
- Parse failures are reported per cell × model. Test whether the failure rate depends on condition. The primary analysis uses parsed trials, with a bound-style sensitivity analysis treating failures as attribution / no attribution.
- Multiplicity: Holm within the primary family (P1–P4) and, separately, within the secondary family.
