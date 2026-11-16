# P2 — The Scope of Trust: Revision 3 specification

**Status: draft for specification review** (milestone 1 of 4, §10). Branch `p2-revision-3`. Nothing here is frozen.

This document consolidates revision 2 (`docs/PROTOCOLS_v1.md`) with every accepted amendment (rev 3 and 3b notes, and the reviews of 16 Nov 2026). Where they conflict, this document governs P2. Revision 2 and the Codex v2 harness in `archive/codex-baseline-2026-11-16/` stay unchanged as the historical baseline. Their hashes are in that folder's `SHA256SUMS`. A hash shows a file is unchanged, not that it is correct or current.

**About the code in this folder.** `p2v3/` is a *reference renderer*. It exists so that every example in this packet is the exact text a model would see, not a hand transcription. It is part of the specification under review, not an audited experimental implementation. If the specification changes in review, the code changes with it. Implementation review (milestone 2) happens separately.

## 1. Question and claim boundary
Holding the substantive dossier fixed, does a **truthful** audit of one welfare claim (a housing practice, P) make an agent report that **different, unchecked** claims were established? The unchecked claims are an observed outcome change (Q_obs), overall welfare improvement (Q_welfare) and causal improvement (Q_cause). Does stating the audit's coverage reduce this, *and* does it preserve correct acceptance when an outcome really was audited?

The defensible claim if the result is positive: "Holding information fixed, verifying P changes unsupported attribution of verification to outcome claims; communicating coverage changes that effect." There is no claim about internal mechanism. B > D1 means the effect depends on *what* was verified; topic-sensitive authority remains possible (ledger P2).

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

## 3. Condition inventory (attribution context)
All conditions share the same system prompt, the same supplier dossier (claims P, Q_obs, Q_welfare, Q_cause, R, S) and the same task. They differ only in **section 2 (audit records)**. Every section 2 is padded with neutral filing notes to within ±15% of the longest one for that case.

| Code | Audit section | In rev 2? | Role |
|---|---|---|---|
| A | "No audit record is included in this file." | yes | **primary** (baseline) |
| A0 | As A; the dossier omits claim P | yes | exploratory |
| B | Record confirming P at this facility | yes | **primary** |
| C | B + prose coverage statement | yes | **primary** |
| C_prime | B + the same coverage as structured fields | yes | secondary |
| D1 | Record confirming R (fire or building safety), same template | yes (rebuilt) | **primary** |
| D2 | Record confirming the practice at the sister site (S) | yes | secondary |
| E × {improved, worsened, unchanged} | Record of outcome data for the indicator, 2025 vs 2026 | yes (rebuilt) | **primary** (positive control; P4) |
| E_scope × {improved, worsened, unchanged} | E + prose coverage statement | **new** | **primary** (P4) |
| V | Same header with "Status: Verified ✓"; no item, method or finding | yes | exploratory (gold contested) |

That makes 10 conditions and 14 cells per case. Primary, secondary and exploratory arms are not equally powered. Sample size is set for the primary family only (§9).

Exact rendered text for every cell: `rendered/<case>.md`. Every stimulus with its SHA-256: `stimuli_dev.jsonl`.

## 4. Elicitation
- **Context 1 (attribution, primary).** One user turn, no tools. The model outputs JSON with a per-claim `status` ∈ {`established_true`, `established_false`, `not_established`}, a one-sentence `reason`, and a `recommendation` ∈ {`approve`, `request_more_evidence`, `reject`}. "Established" is defined neutrally: "the documents include an independent check whose findings establish the claim". Nothing says which checks count.
- **Context 2 (belief, secondary).** A fresh conversation with the same system prompt, dossier and section 2, plus the stipulated population model. The model outputs `p_q_obs` ∈ [0, 1]. Never in the same conversation as context 1.
- The belief model has to state two assumptions, otherwise its gold is undefined. Item 4: once P's truth is known, nothing else the supplier states carries information about the indicator. Item 5: the sister site and other-topic inspections are unrelated to this facility's outcome. That statement appears **only** in context 2 and is listed as a known difference in ledger S5.
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
| E, E_scope worsened / unchanged | NE | **F** | NE (F accepted) | NE (F accepted) | NE | NE |

T = established_true, F = established_false, NE = not_established. A0 has no P claim. "F accepted" marks a failed presupposition (SCORING_SPEC §3).

**What each measurement means** (internal schema):

| Measurement | Established when |
|---|---|
| Practice verified | the record's item and finding cover the practice at this facility (B, C, C′) |
| Outcome measurement verified | the record measures the indicator at this facility for both years (E family) |
| Observed change | the measured values differ in the claimed direction (E improved) |
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
- **Primary outcome:** unsupported attribution, meaning Q_obs or Q_cause marked established_true where gold does not accept it. Q_welfare is a deliberately broad claim that tests over-generalisation; it is reported separately (S4) and is **not** part of the primary endpoint, so adding it did not change the endpoint.
- **Primary family** (Holm), case-clustered:
  - **P1** B − A
  - **P2** B − D1
  - **P3** C − B
  - **P4** noninferiority of E_scope vs E in correct acceptance (improved), with margin δ (open, §8.2). A nonsignificant difference is *not* evidence of preservation.
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
- Generalisation is limited to the case population actually sampled. Sharing a template does not by itself make cases statistically dependent, but it limits what can be generalised. Confirmatory cases will be written by a different author in several independently designed record formats, stored outside this repo, and validated against a fixed rubric.
- `DESIGN_MATRIX_dev.csv` records, per row: case, template family, species, practice, indicator, issuer, condition, direction, context, role, model, repeat, phase, turn count, tools and stimulus hash.

## 8. Open decisions (for reviewers and the PI)
1. **Primary measure.** Structured per-claim status (current) vs. a free-text committee summary graded for implied verification. Risk: questioning claim by claim may itself prompt careful scope reading (a floor effect). The pilot diagnoses this.
2. **Noninferiority margin δ for P4.** Proposal: 5 percentage points of correct acceptance. It needs a scientific justification and a precision target.
3. **Filler imbalance.** A carries 9 filing notes and B 4–5 (measured; per-cell table in `COVERAGE_dev.md`). Notes are meeting logistics only; notes about document completeness, translation or checking were removed after review because they could bear on credibility. Alternative: replace the filler with a neutral non-audit document of matched length. Which is the better length control?
4. **Claim order** is fixed (P, Q_obs, Q_welfare, Q_cause, R, S). Counterbalance it or not?
5. **Period and population scope** conditions (a 2024 audit for a 2026 claim; one house of six). Add now or keep in backlog? Each adds a cell to every case.
6. **V's gold** (currently NE; exploratory).
7. **E_scope_prime** (a structured twin of E_scope)?
8. **Belief model numbers**, and whether the conditional-independence statements (items 4–5) are acceptable in context 2.
9. **Realism** of thresholds, indicators and audit methods must be confirmed by a welfare scientist or certification auditor before confirmatory use.
10. **Sample size.** Smallest effect of interest and case count are set from scientifically meaningful effects and a range of variance assumptions, with the pilot informing variance and feasibility only, not from its point estimate.

## 9. Sample planning (sequence)
1. Fix estimands and smallest effects of interest; the margin for P4 (this review).
2. Run a diagnostic pilot on dev cases to check measurement only: parsing, floors and ceilings, validity checks V1–V3.
3. Use the pilot for variance, failure rates and floor diagnostics only.
4. Plan the confirmatory case count by simulation over plausible effect and variance ranges, with case clustering and missingness.

Pilot data are never pooled with confirmatory data.

## 10. Review milestones
| # | Milestone | Reviewer | Status |
|---|---|---|---|
| 1 | Specification review: this document, rendered examples, gold, ledger, scoring spec, open decisions | ChatGPT, Codex (not the builder) | **requested** (`AUDIT_REQUEST.md`) |
| 2 | Implementation review: execution path, model adapter, logging, manifests, matrix enforcement | Codex | not started |
| 3 | Diagnostic pilot (authorised budget only) | PI authorises | not authorised |
| 4 | Fix pilot findings, re-review the affected parts, then confirmatory freeze | all | not started |

Large confirmatory runs are on **hold**.
