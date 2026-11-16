# The Scope of Trust: Does Verifying One Welfare Claim Make Agents Treat Unchecked Claims as Verified?

**Draft for the Apart AI × Epistemics sprint report (official template, ≤8 pages).** This file holds the source text; formatting happens in the Google Doc.

Text in [brackets] is not filled yet. Every number in Results must come from checked logs or committed test output. Spec of record: `rev3/REVISION_3_SPEC.md` at `100641f`.

**Authors:** [names, affiliations]
**Track:** 2, Trust Infrastructure (evaluation method from Track 1)

---

## Abstract (target 150–250 words; currently ≈225)

Verification signals such as audits, badges and certificates are meant to make checking claims cheap. AI agents that consume these signals could also over-extend them. A truthful audit of one claim might lead an agent to report other, unchecked claims as verified.

We specify a controlled experiment in an animal-welfare procurement setting. The supplier statements are held fixed. These include a housing practice (P) and a recorded-outcome change (Q_obs: the recorded share of birds with footpad lesions fell). Only the audit section varies:
- no audit (A)
- a truthful audit of the practice only (B)
- a successful audit of an unrelated property (D1)
- the practice audit plus an explicit coverage statement (C)
- audits of the outcome records themselves, as positive and negative controls (E, E_scope)

The model labels each claim as established_true, established_false or not_established. These labels are defined as whether the documents contain an independent check that settles the claim.

The primary outcome is unsupported attribution of Q_obs. The primary contrasts are B − A, B − D1 and C − B. A fourth test is whether disclosing coverage preserves correct acceptance of genuinely audited outcomes, a one-sided noninferiority test with a margin derived from base rates.

During the sprint we completed:
- gold labels derived by rule from evidence profiles
- leakage, scoring and design-matrix audits
- boundary-valid paired interval methods, chosen by coverage simulation
- 86 passing tests

No model experiments have been run, so this report makes no empirical claim about model behaviour.

---

## 1. Introduction

Trust infrastructure only helps if its consumers read the signal for what it covers. Increasingly the consumers are AI agents that summarise supplier documentation, approve claims or brief committees. An audit that verifies a narrow practice ("stocking density was at most 30 kg/m² throughout 2025") says nothing about outcomes ("recorded footpad lesions fell"). An agent might still treat the verified practice as a stamp on the whole file.

**Main question.** Holding the supplier statements fixed, does adding truthful verification of a housing practice increase the probability that an agent marks an unchecked recorded-outcome decline as established_true? The comparisons are:
- **A:** the same practice fact without verification
- **D1:** a successful check of an unrelated property

**Intervention question.** Does stating the audit's coverage explicitly reduce that error (C − B) while preserving correct acceptance when the outcome *was* audited (E_scope vs E)? Lower acceptance alone is not success.

**Why welfare assurance.** Procurement committees and certification schemes increasingly rely on summarised audit evidence. Over-extending a practice audit to an outcome claim is a consequential error: it rewards claims nobody checked. Our claims are about attribution in this task, not about real animal welfare.

**Contribution.**
1. A content-matched design separating three explanations:
   - *verification spillover:* B > A
   - *topic-dependence:* B > D1
   - *a generic "any audit" effect:* B ≈ D1 > A
2. A disclosure intervention evaluated for selectivity, not just suppression.
3. Gold labels derived by rule from evidence profiles.
4. Prespecified informative-null rules: two-sided equivalence for B − A, and one-sided noninferiority for acceptance preservation.

## 2. Related work

- **Verification status and authority cues.** *Silence Is Endorsement* (arXiv 2609.20211) studies verification-status laundering in agent pipelines. *Authority Bias* (arXiv 2609.37616) studies authority cues. *Who Verifies the Tools?* (arXiv 2610.32110) studies scope disclosure. [verify each by ID before citing]

  Our C − B overlaps substantially with the scope-disclosure work. The contribution rests on B − A and B − D1: holding supplier assertions fixed and varying only what was verified.
- **Provenance signals.** The sprint's *Provenance Study* example asks whether provenance and reliability metadata improve agent behaviour. C2PA (v2.4) is the provenance standard. P2 is a narrower test of what a verification record licenses an agent to conclude.
- **Welfare data.** WelfareFacts (Hugging Face dataset `Maryamp/welfare-facts`) provides source-grounded numerical welfare facts but no audit-scope manipulation. We make no claim to be the first welfare-assurance dataset.

## 3. Methods

### 3.1 Stimuli

Each case is a supplier file with three sections:
1. **Supplier statements**, fixed within a case:
   - P: a practice
   - Q_obs: a recorded-outcome change
   - Q_welfare: overall welfare
   - Q_cause: a causal claim
   - R: an unrelated property
   - S: a sister site
2. **Audit records**, which vary by condition.
3. **The task.**

Every cell ends with the same two filing notes. Lengths are not padded, so differences equal the audit content that defines the condition.

[Figure 1: excerpt of one rendered case, Section 2 in conditions A, B and E.]

### 3.2 Conditions

| Code | Audit section | Role |
|---|---|---|
| A | No audit record | primary baseline |
| B | Record confirming P at this facility | primary |
| C | B + prose coverage statement | primary |
| D1 | Record confirming R (fire safety), same template | primary |
| E × {improved, worsened, unchanged} | Audit of the outcome records for 2024 vs 2025 | primary positive/negative control |
| E_scope × 3 | E + coverage statement | primary (P4) |
| C′, D2 | structured coverage; sister-site audit | secondary |
| A0, V | P omitted; unscoped "Verified ✓" stamp | exploratory |

That is 10 conditions and 14 cells per case. The attribution context is primary. A separate belief context, run as a separate conversation, elicits p(Q_obs) under a stipulated probability model.

### 3.3 Response and gold

The model gives a status for each claim, a one-sentence reason, and a recommendation (approve, request more evidence or reject), returned as JSON. The status definitions shown to the model are:
- **established_true:** "the documents include an independent check whose findings establish that the claim is true."
- **established_false:** the same, for false.
- **not_established:** neither.

The instrument therefore asks about **attribution**, not likelihood. Probability judgments go to the separate belief context.

Gold labels are derived by rule from each cell's evidence profile (`p2v3/gold.py`) and cross-checked against a hand table:
- In B, C and C′, P is established_true and Q_obs is not_established.
- E improved makes Q_obs established_true. E worsened or unchanged makes it established_false.
- Q_welfare is never established.

### 3.4 Outcomes and estimands

The **primary outcome** is `unsupported_q_obs`: Q_obs marked established_true where gold does not accept it.

**Primary family** (Holm correction; cases are the clustering unit and are weighted equally):

| ID | Contrast | Inference |
|---|---|---|
| P1 | B − A | two-sided; equivalence within ±SESOI if the interval is inside |
| P2 | B − D1 | two-sided |
| P3 | C − B | two-sided |
| P4 | E_scope vs E, correct acceptance (improved) | one-sided noninferiority, margin δ |

**The P4 margin is derived from base rates.** The disclosure is worth using only if the correct acceptances it costs are fewer than the unsupported attributions it prevents, weighted by how often each situation occurs. This gives δ = (π_u/π_s)·B/r, where:
- π_u and π_s are the shares of unsupported and supported situations
- B is the SESOI of P3
- r is the relative cost of a missed acceptance

With π_u = 0.1, π_s = 0.9, B = 0.1 and r = 1, δ ≈ 1.1 points, not 5. The base rates come from practitioners.

**Validity checks** must pass first:
- V1: correct acceptance in E improved
- V2: correct refutation in E worsened and unchanged
- V3: manipulation checks

**Secondary outcomes:** causal over-attribution (S3), welfare over-generalisation (S4), belief error and recommendations. Component-wise results (Q_obs, Q_cause, Q_welfare and the composite) are always reported together.

### 3.5 Inference and sample planning

- Intervals must be valid at the boundary. An ordinary bootstrap of all-zero paired differences gives false certainty.
- Candidate methods are paired score intervals (Tango), cluster adjustment for repeats within case, and exact or Bayesian beta-binomial alternatives.
- A method qualifies only if its one-sided 97.5% lower bound has non-coverage ≤ 3% at every point of a grid. The grid crosses true acceptance (0.80–1.00), true difference (0, −δ/2, −δ), between-case heterogeneity, repeats, case counts (30–240) and missingness (none, MCAR, arm-dependent).
- The confirmatory case count is set from this simulation. Repeats never substitute for independent cases.
- Pilot data inform only variance and feasibility.
- The estimands, SESOIs, δ, method, multiplicity and missing-data rules are frozen before confirmatory outcomes.

## 4. Results

The work so far falls into three categories, kept separate below.

### 4.1 Completed software validation

86/86 tests pass (`cd rev3 && python3 -m unittest discover -s tests -t .`). They cover:
- gold labels derived by rule agree with the hand table
- no leakage between cells beyond Section 2
- a deterministic scorer
- a design-matrix audit against the 28 declared cells, including missing-trial and stimulus-drift detection
- the expert-review rubric
- the paired interval methods

All 168 development stimuli are rendered and hashed (`stimuli_dev.jsonl`).

### 4.2 Interval-method and precision simulation

[Fill from the simulation PR, citing its SHA, with:]
- [the chosen P4 method and its worst-case non-coverage over the grid, with Monte Carlo SE]
- [type I error at −δ]
- [false noninferiority under case-dependent and arm-dependent missingness]
- [required independent cases for P1–P4, as a sensitivity grid over SESOI and δ]
- [comparison with the conservative references (PR #3 as the general check, PR #2 as the boundary diagnostic), judged by coverage, not agreement]

Note: the estimator now weights cases equally (commit 100641f), after review found that the earlier ratio estimator weighted cases by their number of complete pairs.

### 4.3 Model results

None. No model calls have been made.

| Model | Cases | P1 B−A | P2 B−D1 | P3 C−B | P4 (lower bound vs −δ) | V1–V3 | Missingness |
|---|---|---|---|---|---|---|---|
| [—] | [—] | [—] | [—] | [—] | [—] | [—] | [—] |

## 5. Discussion

The design tells apart three readings that a single "audit vs no audit" contrast would conflate:
- spillover from the specific verified practice
- a generic effect of any successful audit
- no meaningful spillover

It also evaluates the obvious mitigation, stating what was checked, for selectivity. A disclosure that suppresses every endorsement is caution, not improvement.

A precise B − A null would be a useful result in its own right. It would show that truthful practice audits do not produce meaningful outcome-verification spillover in this task, within the interval's bounds.

**Open prerequisites for confirmation:**
- welfare-expert verification of gold labels and realistic evidence boundaries
- several independently written case formats (there is currently one)
- a naturalistic committee-summary validation before any claim transfers to real assurance summaries

## Appendix A. Limitations and Dual-Use / Ethical Considerations (required)

**What this does and does not establish.** No model behaviour has been measured. The contribution is a specified and software-validated design. Once run, results concern attribution judgments in structured claim classification on synthetic cases. They do not concern real animal welfare, internal mechanisms or free-text assurance reports.

**Measurement limits.**
- The explicit per-claim status task may itself make scope boundaries salient, which could suppress spillover. This is why a naturalistic validation is required before claims transfer.
- All six development cases share one template and one author.
- Thresholds, indicators and audit methods are unreviewed placeholders until expert review.
- Every indicator is "lower is better".
- No case establishes causation, so Q_cause results describe over-attribution only.

**Dual use.** Knowing that narrow verification can lend credibility to unchecked claims could help a supplier design misleading dossiers. We report it because detection and disclosure policies depend on measuring it. The stimuli use synthetic farms and no real suppliers.

**Personal data.** None.

## Appendix B. New work during the sprint

All files were created during the sprint (first commit 16 Nov 2026). The Codex v2 harness archive (`archive/codex-baseline-2026-11-16/`, checksummed) is a preserved baseline from [confirm date and origin]. It is not the implementation of this design.

## References

[Verify every entry by ID before submission; made-up references disqualify a project.]

- *Silence Is Endorsement.* arXiv 2609.20211.
- *Authority Bias.* arXiv 2609.37616. [verify]
- *Who Verifies the Tools?* arXiv 2610.32110. [verify]
- Tango, T. (1998). Equivalence test and confidence interval for the difference in proportions for the paired-sample design. *Statistics in Medicine*.
- Obuchowski, N. (1998). On the comparison of correlated proportions for clustered data. *Statistics in Medicine*.
- C2PA Technical Specification v2.4 (2025).
- WelfareFacts dataset, Hugging Face `Maryamp/welfare-facts`.
