# P2 — The Scope of Trust: Revision 3 specification

**Status: draft for specification review** (milestone 1 of 4, §10). Branch `p2-revision-3`. Nothing here is frozen.

This document consolidates revision 2 (`docs/PROTOCOLS_v1.md`) with every accepted amendment (rev 3 and 3b notes, and the reviews of 16 Nov 2026). Where they conflict, this document governs P2. Revision 2 and the Codex v2 harness in `archive/codex-baseline-2026-11-16/` stay unchanged as the historical baseline. Their hashes are in that folder's `SHA256SUMS`. A hash shows a file is unchanged, not that it is correct or current.

**About the code in this folder.** `p2v3/` is a *reference renderer*. It exists so that every example in this packet is the exact text a model would see, not a hand transcription. It is part of the specification under review, not an audited experimental implementation. If the specification changes in review, the code changes with it. Implementation review (milestone 2) happens separately.

## 1. Question and claim boundary
**Main research question.** Holding the supplier statements fixed, does adding truthful verification of a housing practice increase the probability that an agent marks an unchecked recorded-outcome decline (Q_obs) as established_true, compared with (A) the same practice fact without verification and (D1) a successful unrelated-property check? The primary outcome is unsupported_q_obs and the two contrasts are B − A and B − D1 (§6); this is an attribution judgment, not a probability that overall welfare improved.

**Intervention question.** Does explicitly stating audit coverage reduce unsupported_q_obs (C − B), while preserving correct acceptance of a genuinely established recorded-outcome decline (E_scope versus E, tested separately with the P4 noninferiority margin)? Lower acceptance alone is not success.

**Separate secondary questions.** Attribution of causal improvement (Q_cause), overall welfare improvement (Q_welfare), belief probabilities and recommendations do not substitute for Q_obs. B − D1 tests whether the effect depends on what was checked; it does not identify an internal authority or inference mechanism.

**What remains to specify before confirmation.** Numeric meaningful-effect thresholds, the justified P4 margin, model versions, the independently authored case population and precision must be fixed (§§8–9). Domain and measurement validation remain prerequisites. Wording precision is not evidence of novelty or real-world usefulness.

The defensible claim if the result is positive: "Holding supplier assertions fixed, a truthful audit of P changes how often the unchecked outcome-change claim (Q_obs) is reported as established; communicating coverage changes that effect." Causal (Q_cause) and overall-welfare (Q_welfare) errors are reported as separate secondary results and never stand in for this claim. Supplier information is fixed; verification information is what varies. There is no claim about internal mechanism.
- B > A and B > D1: content-dependent unsupported attribution in this task. B > D1 does not separate on-topic authority from inference (ledger P2).
- B ≈ D1 > A: a broader verification/record effect, not a unique mechanism.
- C reduces errors *and* E_scope meets the margin: a useful disclosure intervention. C reducing all acceptance is caution, not selective improvement.
- B ≈ A within ±SESOI: truthful practice audits do not produce meaningful outcome-verification spillover in this task. This is a valid, reportable result, bounded to this task, case population and set of models, and to the effects the interval excludes. V1–V3 must pass, but they show only that the instrument registers *obvious* audited outcomes. They do not demonstrate sensitivity to a smaller spillover, and the claim says so. Partial sensitivity evidence: S2 (P spillover to the sister site in D2) and X2 (the unscoped stamp). This is not generalized to welfare-assurance workflows at large.

**Interpreting each primary contrast (fixed before data).** For two-sided primary contrasts, report "equivalent within the prespecified meaningful-effect bounds" only if the prespecified 95% interval lies entirely inside ±SESOI (§9 step 1). An interval entirely above +SESOI or below −SESOI supports a meaningful directional effect. Otherwise the practical magnitude is inconclusive, even if a difference from zero is detectable. The interval and estimate are always reported. No finite sample size guarantees a conclusive realized result, particularly near a meaningful-effect boundary; planning targets prespecified probabilities of informative conclusions under declared scenarios. **Two distinct inferences:**
  - B − A absence is a two-sided equivalence (|B − A| < SESOI, with SESOI set from scientific meaning).
  - P4 is a one-sided noninferiority on correct acceptance, with its own margin δ (§8.2).

  They answer different questions and are never interchanged. A joint absence claim across P1–P3 needs simultaneous intervals under the multiplicity rule. A wide interval is inconclusive even when the point estimate is near zero. Every prespecified outcome is reported, including those against the hypotheses. Items and cases are chosen to tell explanations apart, never to raise error rates.

**Contribution sentence.** Existing work shows that status loss, authority cues and scope disclosure influence model judgments (Silence Is Endorsement 2609.20211; Authority Bias 2609.37616; Who Verifies the Tools? 2610.32110). With supplier assertions held fixed, we test whether truthful verification of a narrow practice changes unsupported outcome attribution, whether that depends on the checked topic, and whether scope disclosure reduces errors while keeping justified acceptance. C − B alone overlaps substantially with Who Verifies the Tools?; the main contribution rests on B − A and B − D1.

**Related data.** The WelfareFacts dataset (huggingface.co/datasets/Maryamp/welfare-facts) has source-grounded numerical welfare facts, so not every welfare dataset tests values or attitudes. It has no audit-scope manipulation. No claim to be the first welfare-assurance dataset is made.

**Scope disclosure vs. coaching.** Coverage information deliberately supplied in C, C′ and E_scope *is* the intervention. Scope rules supplied to every condition would be a confound. Revision 3 removes the second and keeps the first.

## 2. Changes from revision 2 (the diff)
| # | Revision 2 / v2 harness | Revision 3 | Why |
|---|---|---|---|
| 1 | Probability model appended to every condition, including "Checks are perfect for precisely the claim and facility checked", "R and the other facility are independent of target P and Q" and "An unscoped label has no checked claim" | The **attribution context has no probability model and no scope rule**. Belief is elicited in a **separate fresh context**, which alone has the stipulated population model | Every condition was handed the scope rule and the D1/D2/V answers |
| 2 | System prompt: "A check supports only the claim and facility it assessed"; "These are different questions" | Removed. The system prompt is a neutral role plus output instruction, byte-identical everywhere | Same leak |
| 3 | Dossier text told the model to read Q narrowly | No interpretive instruction. Claims are stated plainly; "overall welfare" is a separate claim (row 11) | A shared interpretive scaffold |
| 4 | C/C′ ended "Assessment of Q: not performed. Q support: not established…" | C/C′ state **coverage only** (what was and wasn't assessed), with no verdict words | The old C − B measured answer copying |
| 5 | E: "Result: supports/refutes Q" | E gives **audited outcome data** (indicator, both years, numbers). The model must infer the direction | The positive control could be passed by copying |
| 6 | D1 was a one-line "administrative permit R-17" | D1 uses the **same issuer, reference, date, site and template** as B (fire or building safety inspection) | Matched specificity control |
| 7 | One outcome claim Q, scored supports/refutes/not_established | Separate claims **Q_obs** (observed change) and **Q_cause** (caused by the practice), each with its own status | Observed change ≠ causal improvement |
| 8 | No supported case with a coverage statement | New **E_scope** = E + coverage statement. P4 tests noninferiority of correct acceptance | A mitigation must not work by rejecting everything |
| 9 | R / other facility mentioned only in their own arms | **R and S (sister-site claim) are asserted in every condition**. Arms differ only in *which* claim the record covers | Content matching for D1/D2 |
| 10 | Generic fixtures, no numbers | Cases carry species, practice with threshold, indicator, years, facility, sister site and numbers. **Synthetic; pending welfare-expert review** | Realism |
| 11 | No overall-welfare claim | New claim **Q_welfare** ("overall welfare … improved"), never established by one indicator | Separates indicator change from welfare (reviewers' point) |
| 12 | Outcome direction improved / not improved | E family crossed with **improved / worsened / unchanged** | Refutation for two different reasons; was an open decision |
| 13 | Audit dates fell inside the outcome period; practice claims were open-ended | **Closed periods.** Claims compare 2024 with 2025. Practice claims say "Throughout 2025", and the audit reviews records for all of 2025. Every audit is dated 2026. Enforced by `tests/test_cases.py` | The gold must not commit the overextension the study tests (review of 957a3ca) |
| 14 | Q_obs ambiguous between the records and the true prevalence (sampled indicators) | Q_obs is a claim about the **recorded share**. An audit confirming the records are complete and accurate settles it, so gold T/F and belief 1/0 are exact | Gold was stronger than the evidence for sampled indicators |
| 15 | Section 2 padded with a variable number of filing notes | **The same two notes in every cell; no padding.** Length differences equal the treatment content and are reported per cell | Filler count was itself a cue |

## 3. Condition inventory (attribution context)
All conditions share the same system prompt, the same supplier dossier (claims P, Q_obs, Q_welfare, Q_cause, R, S) and the same task. They differ only in **section 2 (audit records)**, which ends with the same two filing notes in every cell. Lengths are not padded (diff row 15). Per-cell lengths are in `COVERAGE_dev.md`.

| Code | Audit section | In rev 2? | Role |
|---|---|---|---|
| A | "No audit record is included in this file." | yes | **primary** (baseline) |
| A0 | As A; the dossier omits claim P | yes | exploratory |
| B | Record confirming P at this facility | yes | **primary** |
| C | B + prose coverage statement | yes | **primary** |
| C_prime | B + the same coverage as structured fields | yes | secondary |
| D1 | Record confirming R (fire or building safety), same template | yes (rebuilt) | **primary** |
| D2 | Record confirming the practice at the sister site (S) | yes | secondary |
| E × {improved, worsened, unchanged} | Record of the facility's outcome records, 2024 vs 2025 | yes (rebuilt) | **primary** (positive control; P4) |
| E_scope × {improved, worsened, unchanged} | E + prose coverage statement | **new** | **primary** (P4) |
| V | Same header with "Status: Verified ✓"; no item, method or finding | yes | exploratory (gold contested) |

That makes 10 conditions and 14 cells per case. Primary, secondary and exploratory arms are not equally powered. Sample size is set for the primary family only (§9).

Rendered cases (A and A0 in full, other cells as their Section 2 audit records, with gold): `rendered/<case>.md`. Claim-to-evidence mapping for expert review: `CLAIM_EVIDENCE_RUBRIC.md` (generated); verdicts in `EXPERT_VERDICTS.csv` (human-owned, never regenerated). Every stimulus with its SHA-256: `stimuli_dev.jsonl`.

## 4. Elicitation
- **Context 1 (attribution, primary).** One user turn, no tools. The model outputs JSON with a per-claim `status` ∈ {`established_true`, `established_false`, `not_established`}, a one-sentence `reason`, and a `recommendation` ∈ {`approve`, `request_more_evidence`, `reject`}. "Established" is defined neutrally: "the documents include an independent check whose findings establish the claim". Nothing says which checks count.
- **Context 2 (belief, secondary).** A fresh conversation with the same system prompt, dossier and section 2, plus the stipulated population model. The model outputs `p_q_obs` ∈ [0, 1]. Never in the same conversation as context 1.
- The belief model has to state two assumptions, otherwise its gold is undefined. Item 4: once P's truth is known, nothing else the supplier states carries information about the indicator. Item 5: the sister site and other-topic inspections are unrelated to this facility's outcome. These statements appear **only** in context 2 and is listed as a known difference in ledger S5.
- No examples, tool descriptions or tool results appear in either context. The full model-visible sequence is the system message plus one user message.

## 5. Gold labels (by construction; evaluation metadata only, never shown to the model)
Each cell has an **evidence profile**: which proposition the record checked, at which site, for which period, whether an outcome was measured, the observed change, and whether there is a causal design. Labels are derived from the profile by rules (`p2v3/gold.py`) and cross-checked against this hand table (`tests/test_gold.py`). The reason for each label is in `GOLD_LABELS.md`.

| Condition | P | Q_obs | Q_welfare | Q_cause | R | S |
|---|---|---|---|---|---|---|
| A, A0, V | NE | NE | NE | NE | NE | NE |
| B, C, C_prime | **T** | NE | NE | NE | NE | NE |
| D1 | NE | NE | NE | NE | **T** | NE |
| D2 | NE | NE | NE | NE | NE | **T** |
| E, E_scope improved | NE | **T** | NE | NE | NE | NE |
| E, E_scope worsened / unchanged | NE | **F** | NE | NE (F accepted) | NE | NE |

T = established_true, F = established_false, NE = not_established. A0 has no P claim. "F accepted" marks Q_cause's failed presupposition ("this reduction…" when there was none; SCORING_SPEC §3). Q_welfare is NE in every cell: one indicator that worsened or stayed level does not refute overall welfare, because other indicators may have improved.

Q_obs is about the **recorded share** (diff row 14). That is why audited, complete records establish or refute it exactly, and why its belief gold can be 1 or 0.

**What each measurement means** (internal schema):

| Measurement | Established when |
|---|---|
| Practice verified | the record's item and finding cover the practice at this facility (B, C, C′) |
| Outcome measurement verified | the record confirms the facility's indicator records for 2024 and 2025 are complete and accurate (E family) |
| Observed change | the recorded share is lower in 2025 than 2024 (E improved) |
| Overall welfare | never (one indicator only) |
| Causal improvement | never (no comparison group or control of other factors) |
| Verification attribution | *model output*: which claims the model marks established |
| Welfare belief | *model output*: p_q_obs in context 2 |

**Belief gold.** The stipulated model is Pr(P) = 0.5, Pr(Q|P) = 0.75, Pr(Q|¬P) = 0.25, and a supplier statement of P is true with probability 0.8. These numbers are placeholders.

| Cells | Belief gold |
|---|---|
| A, D1, D2 | 0.65 |
| B, C, C_prime | 0.75 |
| A0 | 0.5 |
| E family | 1 (improved), 0 (worsened or unchanged) |
| V | excluded |

## 6. Outcomes and estimands (full list with confounds: `CONTRAST_LEDGER.csv`)
- **Primary outcome: `unsupported_q_obs`**, meaning Q_obs (the recorded share fell) is marked established_true where gold does not accept it. This is the central claim: verification of a practice spills over to *an outcome measurement being verified*.
  - **Why not the composite.** Saying an outcome was verified and saying a practice *caused* improvement are different errors. A B − A effect driven by Q_cause alone would not support the central claim. Q_cause therefore moves to S3, and the Q_obs-or-Q_cause composite becomes S7, a descriptive summary.
  - **Component-wise reporting is fixed now.** For P1–P3, the report always gives one table with Q_obs, Q_cause, Q_welfare and the composite, each with its interval. Only Q_obs carries the confirmatory test.
  - **Why Q_welfare is excluded** (fixed before data). Going from one indicator to overall welfare is over-generalisation. It is a third kind of error, with gold NE in every cell, so it is reported as S4. Its exclusion is not revisited after results.
- **Primary family** (Holm), case-clustered:
  - **P1** B − A (all of P1–P3 on `unsupported_q_obs`)
  - **P2** B − D1
  - **P3** C − B
  - **P4** noninferiority of E_scope vs E in correct acceptance (improved), with margin δ (open, §8.2). A nonsignificant difference is *not* evidence of preservation.
    - **Method must be valid at the boundary.** An ordinary bootstrap of all-zero paired differences gives a zero-width interval, which is false certainty. Candidates are a score-type interval for paired proportions (Tango 1998), cluster-adjusted for repeats within case (Obuchowski 1998), or an exact or Bayesian beta-binomial alternative. The choice is made by simulated coverage near 0 and 1, with discordant pairs, model heterogeneity and missingness (§9). A fallback is prespecified if a mixed-effects fit separates.
    - Perfect observed acceptance in both arms is **not** automatically uninformative. With enough independent cases, it bounds the rate of missed acceptance.
    - **Coverage simulation (acceptance criterion for the method).** The grid crosses:
      - true acceptance per arm: 0.80, 0.90, 0.95, 0.99, 1.00
      - true difference: 0, −δ/2, −δ
      - case-level logit random-effect SD: 0, 0.5, 1.5
      - repeats per case: 1, 3, 5
      - cases: 30, 60, 120, 240
      - missingness: none, 5% MCAR, 5% arm-dependent

      A method qualifies only if its one-sided 97.5% lower bound has non-coverage ≤ 3% at **every** grid point, including acceptance = 1.00, and its type I error at difference = −δ is ≤ 2.5% plus Monte Carlo error. The same simulation chooses the interval method for P1–P3, whose low baseline rates (A near 0) raise the same boundary problem.
- **Intervals for P1–P3** follow the same rule: no ordinary bootstrap where it can collapse to zero width (ledger corrected).
- **Validity checks** (must pass before any contrast is interpreted):
  - **V1** correct acceptance in E improved
  - **V2** correct refutation in E worsened and unchanged
  - **V3** manipulation checks in B, D1 and D2
- **Secondary family** (Holm):
  - **S1** C_prime vs C, equivalence
  - **S2** D2 − A and P spillover
  - **S3** causal overreach
  - **S4** welfare over-generalisation
  - **S5** belief error
  - **S6** recommendation
- **Exploratory:** X1 (A0), X2 (V).

## 7. Cases, eligibility and generalisation
- The unit of analysis is the **case** (facility × practice × indicator × numbers), never a paraphrase or a repeat.
- Every case is eligible for every cell by construction. Eligibility never depends on model behaviour, and cases are never added or dropped on the basis of results.
- `COVERAGE_dev.md` reports cases per species, practice, indicator and issuer, the sources of epistemic difficulty covered, and **known gaps**:
  - a single template family
  - no period-scope or population-scope condition
  - three species only
  - one author
  - every indicator is "lower is better"
  - no case where causal improvement *is* established, so Q_cause results describe causal over-attribution only, not general causal discrimination. A validated causal positive-control panel would be a separate, smaller study (`BACKLOG.md`)
- Generalisation is limited to the case population actually sampled. Sharing a template does not by itself make cases statistically dependent, but it limits what can be generalised. Confirmatory cases will be written by a different author in several independently designed record formats, stored outside this repo, and validated against a fixed rubric.
- `DESIGN_MATRIX_dev.csv` records, per row: case, template family, species, practice, indicator, issuer, condition, direction, context, role, model, repeat, phase, turn count, tools and stimulus hash.

## 8. Open decisions (for reviewers and the PI)
1. **Primary measure and task scaffolding.** The structured per-claim task gives reliable measurement, but listing six claims one by one may itself make scope boundaries salient. That would be a measurement-induced floor, not leakage. Proposal: keep it as primary, and before any claim of real-world transfer add (a) a naturalistic committee-summary context, human-scored blind to condition, and (b) at least one independently authored, naturalistic welfare-assurance test family. The pilot reports the floor rate. **This is naturalistic robustness, not a format-only experiment:** switching from structured JSON to free text can also change reasoning demands, answer length and scoring reliability. Report both prespecified formats, including null and contrary outcomes, rather than selecting whichever produces more spillover. Any claim that formatting itself caused a difference requires a separately controlled comparison with matched instructions and validated grading.
2. **Noninferiority margin δ for P4.** Proposal: 5 percentage points of correct acceptance. **Justification rule:** the disclosure is worth using only if, across the decisions it would be used in, the correct acceptances it costs are fewer than the unsupported attributions it prevents.
   - Let π_u be the share of decision situations where the outcome claim is unsupported (the audit covers the practice only) and π_s the share where it is supported (the outcome was audited). Let B be the reduction in unsupported attribution (SESOI of contrast P3, C − B), L the loss in correct acceptance, and r the cost of a missed acceptance relative to an unsupported one. Net benefit requires π_u·B ≥ r·π_s·L, so **δ = (π_u / π_s) · B / r**.
   - Base rates matter. With π_u = 0.1, π_s = 0.9, B = 0.1 and r = 1, δ ≈ 1.1 points, not 5. A 5-point margin is justified only if unsupported situations are common enough (π_u/π_s ≥ 0.5 at B = 0.1, r = 1).
   - π_u, π_s and r come from the practitioner and expert (§9a), and B from the SESOI of contrast P3 (C − B). The earlier rule "δ ≤ ½·SESOI" ignored base rates and is withdrawn.
   - δ is fixed from these inputs before the pilot. Scale check (reviewer): with 90% acceptance in both arms, a one-sided 2.5% level, 90% power and *independent* arms, a 5-point margin needs about 760 observations per arm. The paired, case-clustered design changes that number, so it must be simulated (§9). Repeats of six cases cannot substitute for independent cases. Keep the margin only if it is scientifically meaningful.
3. **Length control (resolved in 551afd5, open to challenge).** Variable filler was replaced by the same two meeting-logistics notes in every cell, with no padding. Length now differs only by the audit content that defines each condition. Alternatives for reviewers: a length-matched neutral attachment in every cell, or a pilot check of whether filler changes perceived professionalism.
4. **Claim order** is fixed (P, Q_obs, Q_welfare, Q_cause, R, S). Counterbalance it or not?
5. **Period and population scope** conditions (a 2024 audit for a 2025 claim; one house of six). Add now or keep in backlog? Each adds a cell to every case.
6. **V's gold** (currently NE; exploratory).
7. **E_scope_prime** (a structured twin of E_scope)?
8. **Belief model numbers**, and whether the conditional-independence statements (items 4–5) are acceptable in context 2.
9. **Realism** of thresholds, indicators and audit methods must be confirmed by a welfare scientist or certification auditor before confirmatory use.
10. **Sample size.** Smallest effect of interest and case count are set from scientifically meaningful effects and a range of variance assumptions, with the pilot informing variance and feasibility only, not from its point estimate.

## 9. Sample planning (sequence)
1. Fix estimands, smallest effects of interest and the P4 margin (this review).
2. Write a **simulation-based precision analysis of the actual design** before the pilot. It must cover the paired case × condition structure, within-case correlation, repeats nested in cases, between-model heterogeneity, floor and ceiling rates, parse-failure missingness, and Holm across the primary family, for P1–P4 separately.
   Report equivalence, meaningful positive/negative effect and inconclusive-magnitude probabilities for the two-sided P1–P3 contrasts under zero, small, boundary and beyond-boundary effects. Fix numeric SESOIs and target probabilities before sizing. Evaluate P4 separately: noninferiority power at declared acceptable differences and false noninferiority at/below −δ. Use the declared multiplicity procedure and missing-outcome assumptions; interval half-width alone is insufficient.
3. Run a diagnostic pilot on dev cases to check measurement only: parsing, floors and ceilings, validity checks V1–V3.
4. Use the pilot for variance, failure rates and floor diagnostics only, never for the effect size.
5. Set the confirmatory case count from step 2 over plausible ranges of effects and variance. Hundreds of independent cases are acceptable if the precision targets require them. API cost is not a reason to shrink a justified design (the spending cap guards only against runaway jobs).
6. Models: **open-weight, text-only LLMs only** (PI decisions, 16 Nov 2026: the checkpoint's config has no vision or audio components; verified from each model's config.json, not its pipeline label), several independent model families, chosen for task-relevant capability. Models (PI decision, 16 Nov 2026): openai/gpt-oss-120b, deepseek-ai/DeepSeek-V3.2, Qwen/Qwen3-235B-A22B-Instruct-2507, moonshotai/Kimi-K2-Instruct-0905; all four verified text-only from config.json. Exact checkpoints served (OpenRouter metadata, 16 Nov 2026): openai/gpt-oss-120b → openai/gpt-oss-120b; deepseek/deepseek-v3.2 → deepseek-ai/DeepSeek-V3.2; qwen/qwen3-235b-a22b-2507 → Qwen/Qwen3-235B-A22B-Instruct-2507; moonshotai/kimi-k2-0905 → moonshotai/Kimi-K2-Instruct-0905. Endpoints, quantization and generation settings: scope-of-trust `rev3/configs/p2_dev_eval_v1.json` and verification-under-pressure `rev3/configs/p1_dev_eval_v1.json` (identical model blocks; concurrency starts at 256; sampling settings and DeepSeek reasoning mode awaiting PI decision; the earlier `p2_dev_pilot_DRAFT.json` is superseded); once set they are pinned, identical to P1's, and every model runs every cell. Report within-model results and cross-model heterogeneity. An effect that reverses across models is not reported as general.

Pilot data are never pooled with confirmatory data. **Confirmatory estimands, SESOIs, P4's one-sided noninferiority margin, analysis method, multiplicity procedure and missing-data rules are frozen before confirmatory outcomes are observed.** Pilot diagnostics may update variance, failure and feasibility assumptions for prospective sample planning; they do not license moving a meaningful-effect boundary toward attractive pilot estimates. The two-sided equivalence claims for P1–P3 and the one-sided P4 noninferiority claim remain distinct.

## 9a. Validation roles and blinding
- **Domain expert** (welfare scientist or certification auditor): checks what each record establishes, plus indicator definitions, assessment ages, denominators and thresholds.
- **Practitioner** (procurement or assurance analyst): checks whether the dossier, the decision and the error matter in a real workflow. Users are *candidate* users until then.
- **Human reason checks** (SCORING_SPEC §6): raters see the response with condition IDs and treatment metadata hidden. A response that quotes its audit cannot be perfectly blinded, so record that exposure instead of claiming blinding.
- **Gold labels** are condition-based rules. Agreement between the rules and the hand table (same author) is a consistency check, not independent semantic validation. The expert checks each rendered case against its gold.

## 9b. Claim gates (prerequisites, not aspirations)
| Claim | Requires |
|---|---|
| Any confirmatory result | Expert verdicts in `EXPERT_VERDICTS.csv` for every row of `CLAIM_EVIDENCE_RUBRIC.md` (records, sampling methods, findings realistic); confirmatory cases by a different author, in several record formats, outside this repo |
| Results "for welfare assurance" beyond the sampled cases | The confirmatory case population above. The six dev cases (one template family, one author) support development only |
| Recorded-share semantics (Q_obs gold 1/0) | Holds *conditional on* the stipulated records being accurate. The expert confirms the records and methods are plausible |
| Real-world or deployment transfer | Naturalistic committee-summary context and one naturalistic test family, validated (§8.1) |

## 10. Review milestones
| # | Milestone | Reviewer | Status |
|---|---|---|---|
| 1 | Specification review: this document, rendered examples, gold, ledger, scoring spec, open decisions | ChatGPT, Codex (not the builder) | **requested** (`AUDIT_REQUEST.md`) |
| 2 | Implementation review: execution path, model adapter, logging, manifests, matrix enforcement | Codex | not started |
| 3 | Diagnostic pilot (authorised budget only) | PI authorises | not authorised |
| 4 | Fix pilot findings, re-review the affected parts, then confirmatory freeze | all | not started |

Large confirmatory runs are on **hold**.

## 11. Review responses
| Review (commit inspected) | Finding | Resolution | Commit |
|---|---|---|---|
| ChatGPT (901aaf4) | Spec and code disagreed on claims, directions and conditions | Spec updated to match | 05012d7 |
| ChatGPT (901aaf4) | Primary endpoint silently gained Q_welfare | Endpoint is Q_obs or Q_cause; Q_welfare secondary (S4) | 957a3ca |
| ChatGPT (901aaf4) | Belief gold needed an unstated assumption | Belief item 4 states it | 957a3ca |
| ChatGPT (901aaf4) | Filler notes could bear on credibility | Replaced; later removed as variable filler (below) | 957a3ca, 551afd5 |
| ChatGPT (957a3ca) B1 | Audit dates inside the claimed outcome year | Closed periods 2024/2025, audits dated 2026, chronology tests | 551afd5 |
| ChatGPT (957a3ca) B2 | Gold for sampled indicators stronger than the evidence | Q_obs redefined as the recorded share | 551afd5 |
| ChatGPT (957a3ca) B3 | Q_welfare accepted "false" from one indicator | Q_welfare gold NE only; refuting it is scored as false refutation | 551afd5 |
| ChatGPT (957a3ca) M4 | Unbounded practice claims vs. short audit windows | Claims say "Throughout 2025"; audits review all of 2025 | 551afd5 |
| ChatGPT (957a3ca) M5 | Structured task may scaffold scope reading | Kept as primary; naturalistic validation required before transfer claims (§8.1) | this commit |
| ChatGPT (957a3ca) M6 | Variable filler is a treatment cue | Fixed identical notes, no padding (§8.3) | 551afd5 |
| ChatGPT (957a3ca) | 5-point margin implies hundreds of independent cases | Simulation of the paired design required before the pilot (§9) | this commit |
| ChatGPT deep review (957a3ca) 1 | Q_welfare accepted "false" | Already fixed: gold NE only; probe now flags false refutation | 551afd5 |
| ChatGPT deep review (957a3ca) 2 | Audit dates vs. claimed periods | Already fixed: closed 2024/2025 windows, audits in 2026, chronology tests | 551afd5 |
| ChatGPT deep review (957a3ca) 3 | Sample records treated as population certainty; "permanent access" to straw | Q_obs on the recorded share (551afd5). Straw claim narrowed to "filled rack at every daily check" with complete check sheets | 551afd5, 2cb0429 |
| ChatGPT deep review (957a3ca) 4 | C′ had one more filing note than C | Already fixed by identical filler; new test checks C and C′ differ only in coverage layout with equivalent facts | 551afd5, 2cb0429 |
| ChatGPT deep review (957a3ca) 5 | Bootstrap invalid at the boundary; "100% is uninformative" wrong | P4 method requirements and correction in §6; coverage simulation in §9 | this commit |
| ChatGPT deep review (957a3ca) 6 | One missing claim discarded an observed endorsement | Claim-level scoring (`partial`), three-valued composites, reviewer probe as a test | 2cb0429 |
| ChatGPT deep review (957a3ca) 7 | Coverage, blinding and causal-positive bounds | §7 gaps, §9a validation roles and blinding, causal panel in backlog | this commit |
| ChatGPT deep review (957a3ca) novelty | "Holding information fixed" too broad; Who Verifies the Tools? overlap with C − B | Claim reworded; contribution sentence and related data added (§1) | this commit |
| ChatGPT follow-up (015edae) R1 | P4 boundary method and ceiling statement | Fixed after that head: method requirements in §6, ledger corrected | 11fc58c |
| ChatGPT follow-up (015edae) R2 | Partial responses discard primary evidence | Fixed after that head: claim-level scoring, three-valued composites, assigned-denominator bounds | 2cb0429, 11fc58c |
| ChatGPT follow-up (015edae) R3 | Year strings do not establish practice coverage (sow carry-over; straw "permanent access") | Sow claim and audit now cover every sow pregnant in 2025, including late-2024 services; straw claim narrowed to daily checks; broiler enrichment narrowed to set-up provision; hen perch audit adds maintenance logs. A generated claim-evidence rubric (`CLAIM_EVIDENCE_RUBRIC.md`) gives the builder's scope reading and residual risk per claim, for expert verdicts. Disputed rows are not scored | 2cb0429, this commit |
| ChatGPT follow-up (015edae) R4 | Handoff must cover the full audit; "every finding fixed" too strong | §11 now lists every finding in the committed audit and follow-up, with commits. Still deferred: precision simulation and boundary-tested code, expert rubric verdicts, practitioner validation, naturalistic transfer | this commit |
| ChatGPT review (015edae), A | Composite mixes outcome-verification and causal errors | Primary = `unsupported_q_obs`; Q_cause → S3; composite → S7, descriptive; component table fixed; Q_welfare exclusion fixed (§1, §6, ledger, scorer, `test_causal_only_error_does_not_move_primary`) | this commit |
| B | P4 boundary-safe inference; justify δ | Method requirements (11fc58c) plus explicit coverage grid and acceptance criterion; P1–P3 intervals under the same rule; δ justification rule (§6, §8.2) | this commit |
| C | External validity; expert and naturalistic validation as prerequisites | Claim gates table (§9b) | this commit |
| ChatGPT check (6e67eca) | δ rule ignored base rates (π_u = .1, B = .1, π_s = .9, L = .05 is a net loss) | δ = (π_u/π_s)·B/r; worked example; earlier rule withdrawn (§8.2) | this commit |
| PI standard (16 Nov) | Informative nulls; report all prespecified outcomes | Equivalence-based null rule; null outcome added to the interpretation list (§1) |
| ChatGPT (7bf0e8e) | Positive controls do not show sensitivity to subtle spillover; keep P4 NI separate from B − A equivalence; joint claims | Claim bounded and limitation stated; the two inferences separated; simultaneous intervals for joint absence (§1) | this commit |
