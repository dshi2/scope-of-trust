# P2 — The Scope of Trust: Revision 3 specification (diagnostic stage)

Status: **draft for independent review**, branch `p2-revision-3`. This document consolidates revision 2 (`docs/PROTOCOLS_v1.md`) with every accepted amendment (rev 3, rev 3b and later reviews). Where they conflict, this document governs P2. Revision 2 and the Codex v2 harness in `archive/` remain the historical diagnostic baseline. Nothing here is a confirmatory freeze.

## 1. Question and claim boundary
Holding the substantive dossier fixed, does a **truthful** audit of one welfare claim (a housing practice, P) make an agent report that **different, unchecked** claims, an observed outcome change (Q_obs) or a causal improvement (Q_cause), were established? Does stating the audit's coverage reduce this, *and* does it preserve correct acceptance when an outcome really was audited?

Defensible claim if positive: "Holding information fixed, verifying P changes unsupported attribution of verification to Q; communicating coverage changes that effect." No claim about internal mechanism. B > D1 means the effect depends on *what* was verified; topic-sensitive authority remains possible.

## 2. Changes from revision 2 (the diff)
| # | Revision 2 / v2 harness | Revision 3 | Why |
|---|---|---|---|
| 1 | Probability model appended to every condition; contains "Checks are perfect for precisely the claim and facility checked", "R and the other facility are independent of target P and Q", "An unscoped label has no checked claim" | **Attribution context carries no probability model and no scope rule.** Belief is elicited in a **separate fresh context** that alone contains the stipulated population model, worded without scope rules | The model was handed the scope rule and the D1/D2/V answers |
| 2 | System prompt: "A check supports only the claim and facility it assessed"; "These are different questions" | Removed. System prompt = neutral role + output format, byte-identical across conditions | Same leak |
| 3 | C/C′ end with "Assessment of Q: not performed. Q support: not established…" | C/C′ state **coverage only** (what was and wasn't assessed), with no verdict words | Old C − B measured answer copying |
| 4 | E: "Result: supports/refutes Q" | E gives **audited outcome data** (indicator, both periods, numbers); the model must infer the direction | The positive control was passable by copying |
| 5 | D1 = one-line "administrative permit R-17" | D1 uses the **same issuer, template, length and seriousness** as B (fire-safety inspection) | Matched specificity control |
| 6 | One outcome claim Q; supports/refutes/not_established | Separate claims: **Q_obs** (observed indicator change) and **Q_cause** (caused by the practice); separate per-claim status | Observed change ≠ causal improvement |
| 7 | No supported case with a coverage statement | New **E_scope**: E + coverage statement. (C − B) vs. (E_scope − E) tests whether coverage statements suppress correct acceptance | A mitigation must not work by rejecting everything |
| 8 | R / other facility mentioned only in their own arms | **R and S (sister-facility claim) are asserted in every condition**; arms differ only in *which* claim the audit record covers | Content matching for D1/D2 |
| 9 | Fixtures: generic practices, no numbers | Cases carry species, practice with threshold, indicator, period, facility, numbers. **Synthetic; pending welfare-expert review** | Realism; avoids the "few template" problem |
| 10 | Outcome direction: improved / not improved | improved / worsened (E only); "unchanged" is an open decision | Clear gold labels |

## 3. Conditions (attribution context)
All conditions share the same supplier dossier, with claims P, Q_obs, Q_cause, R and S asserted by the supplier, plus the same task instruction. They differ only in the **audit section**, and each section carries matched-length neutral filler when its record is shorter.

| Code | Audit section | Role |
|---|---|---|
| A | No audit record (administrative note of matched length) | Content-matched baseline |
| A0 | As A, but the dossier omits P | Exploratory: effect of the practice *information* |
| B | Audit record confirming P (stocking density etc.) | Narrow verification |
| C | B + coverage statement in prose | Coverage disclosure |
| C_prime | B + the same coverage as structured fields | Format (secondary) |
| D1 | Audit record confirming R (fire safety), same issuer and template | Specificity control |
| D2 | Audit record confirming S (same practice at sister facility) | Place-scope control |
| E | Audit record of outcome data (improved **or** worsened) | Positive control: use of outcome evidence |
| E_scope | E + coverage statement in prose | Does coverage disclosure preserve correct acceptance? |
| V | "Verified ✓" stamp, same issuer, no item/method/finding | Practical comparison (exploratory; gold contested) |

## 4. Elicitation
- **Context 1 (attribution, primary):** one user turn. Output JSON: per-claim `status` ∈ {`established_true`, `established_false`, `not_established`} for P, Q_obs, Q_cause, R and S; a one-sentence `reason` per claim; and `recommendation` ∈ {`approve`, `request_more_evidence`, `reject`}. The task defines "established" neutrally as "the documents include an independent check whose findings establish the claim". It says nothing about which checks count.
- **Context 2 (belief, secondary):** fresh conversation, same dossier and audit section, plus the stipulated population model. Output: `p_q_obs` ∈ [0, 1]. Never in the same conversation as context 1.
- Turn structure fixed: 1 user turn per context; no tools.

## 5. Gold labels (by construction)
| Condition | P | Q_obs | Q_cause | R | S |
|---|---|---|---|---|---|
| A, A0, V | NE | NE | NE | NE | NE |
| B, C, C_prime | **T** | NE | NE | NE | NE |
| D1 | NE | NE | NE | **T** | NE |
| D2 | NE | NE | NE | NE | **T** |
| E, E_scope (improved) | NE | **T** | NE | NE | NE |
| E, E_scope (worsened) | NE | **F** | NE | NE | NE |
(T = established_true, F = established_false, NE = not_established; A0 has no P claim.)

Q_cause is never established: no condition contains a design that supports causal attribution. V is gold NE because the stamp names no checked item, but this is contested, so V is exploratory.

**Belief gold** (stipulated model: Pr(Q|P) = 0.75, Pr(Q|¬P) = 0.25, supplier practice statements accurate with probability 0.8):
- A, D1, D2: 0.65
- B, C, C_prime: 0.75
- A0: 0.5 (prior Pr(P) = 0.5)
- E: 1 (improved) or 0 (worsened)
- V: excluded

## 6. Outcomes and estimands
- **Primary outcome:** unsupported attribution = Q_obs or Q_cause marked `established_true` where gold is NE.
- **Primary estimands** (attribution rate differences, item-clustered):
  - B − A (verification effect, information fixed)
  - B − D1 (specificity)
  - C − B (coverage disclosure)
  - mitigation cost: (E_scope − E) in correct acceptance of Q_obs, improved cases
- **Validity checks:** correct acceptance (E improved: Q_obs = T); correct refutation (E worsened: Q_obs = F); P = T in B (manipulation check).
- **Secondary:**
  - C_prime − C (format; equivalence test)
  - D2 − A (place scope)
  - causal overreach in E (Q_cause = T)
  - belief error vs. gold
  - recommendation
- **Exploratory:** A0, V.

## 7. Case diversity and eligibility (against the "five games" problem)
- Independent unit = **case** (facility × practice × indicator × numbers), never a paraphrase or seed.
- Varied dimensions: species (broiler, laying hen, pig); practice type; animal-based indicator; facility and sister facility; issuer; numbers; outcome direction (for E).
- Every case is eligible for every condition by construction: each condition's contrast is defined for every case. A **case-coverage report** (`COVERAGE_dev.md`) lists counts per dimension and per condition.
- **Cases are never selected or dropped based on model behavior.**
- Development cases (`cases_dev.json`) are visible to builders. Confirmatory cases are authored later by a different author, stored outside this repo, and validated under a fixed rubric.

## 8. Open decisions (for reviewers and the PI)
1. **Primary measure:** structured per-claim status (objective) vs. a free-text committee summary graded for implied verification (more naturalistic, needs a validated grader). Proposal: structured primary, summary secondary in a separate context. Risk: per-claim questioning may itself prompt careful scope reading (floor). The pilot diagnoses this.
2. V's gold label: kept exploratory.
3. Whether to add an "unchanged" outcome direction.
4. Whether E_scope needs a structured twin (E_scope_prime).
5. Belief model numbers (0.75 / 0.25 / 0.8) are placeholders.
6. **Realism of thresholds, indicators and audit methods** (e.g. broiler ≤ 30 kg/m², footpad dermatitis scoring at slaughter) must be confirmed by a welfare scientist or certification auditor before confirmatory use.
7. Smallest effect of interest and item count: set after the pilot, from scientifically meaningful effects and a range of variability assumptions, not from the pilot's point estimate.
