# The Scope of Trust: When a True Audit Licenses an Unsupported Conclusion

**Drishti Sharma**
Independent

**With** Apart Research

_Research conducted at the AI × Epistemics Research Sprint, November 2026._

---

## Abstract

A truthful audit can be over-read: a certifier may correctly confirm a housing practice without establishing that an animal-welfare outcome improved. We test whether language models reviewing a synthetic supplier file let a truthful practice audit license an unchecked claim about a recorded outcome. Supplier statements are held fixed, and only the audit section varies: no audit, a practice audit, a same-template audit of an unrelated property, the practice audit with a coverage statement, and audited outcome records. Four open-weight models answered 36 builder-written cases five times per cell, 20,160 calls in all. No model marked the unchecked outcome claim established in any audit or control cell, in any of four batches, so every primary contrast was 0.000. With zero events in 36 cases, the exact one-sided 95% upper bound on the share of cases ever showing the error is 8.0% per model and cell: a bounded null, not a precise one. Correct acceptance of audited outcomes was 100% with and without the coverage statement. In an exploratory cell with an unscoped "Verified ✓" stamp, Qwen3-235B marked the outcome claim established in 96 of 180 responses. All cases are builder-written and not expert-reviewed.

---

## 1. Introduction

The failure we study is narrow. A file contains a real, correct check of claim P, and a reader concludes that a different claim, Q, has also been checked. Nothing in the file is false; the error lies in the *scope* the reader assigns to a truthful verification. We call it *evidence-scope overreach*. It differs from hallucination, where content is unsupported by the source (Maynez et al., 2020), and from authority bias, where a false answer is accepted because a credible source is said to back it (Kumar & Chopra, 2026). Here the authority is legitimate and correct; the question is how far its endorsement travels.

Animal-welfare assurance makes the problem concrete. Schemes often audit *resource- and management-based* measures, such as stocking density or perch length, while welfare science treats *animal-based* measures, such as lameness or plumage damage, as closer to the animals' state (EFSA AHAW Panel, 2012). A supplier can truthfully pass a practice audit and, in the same file, assert unchecked outcome claims. If an AI assistant summarising such a file lets the practice audit vouch for the outcome, an unchecked claim gains credibility it has not earned, and the human reader sees no error to catch. We score four claims separately (Table 1).

**Table 1.** The four claims and what would establish each one in this design. Example wording for one case is in Appendix A.

| # | Claim (dossier label) | Established in this design by | Can the practice audit B establish it? |
|---|---|---|---|
| 1 | Verification of a **practice** (P) | a record whose item and finding cover the practice at this facility (B, C, C′) | yes, by design |
| 2 | Verification of an **outcome change** (Q_obs) | an audit confirming the 2024 and 2025 indicator records, from whose numbers the direction must be inferred (E family) | no |
| 3 | **Overall welfare** improvement (Q_welfare) | never: no record measures more than one indicator | no |
| 4 | **Causal** improvement (Q_cause) | never: no record has a comparison group | no |

**Questions.** Holding the supplier's statements fixed: does a truthful practice audit raise how often a model marks the unchecked outcome claim Q_obs as established, compared with no audit (P1: B − A)? Does that depend on *what* was checked, compared with an equally official audit of an unrelated property (P2: B − D1)? Does stating the audit's coverage reduce the error (P3: C − B) without suppressing correct acceptance when the outcome *was* audited (P4: E_scope vs. E)?

**What we found.** The primary error did not occur. Across 36 cases in four batches, no model marked the unchecked outcome claim established after a practice audit, an unrelated audit, a coverage-qualified audit or no audit. Every such cell had 0 events, which gives a case-level 95% upper bound of 8.0% per model and cell. The positive controls were passed: models accepted and refuted outcome claims from audited numbers. The only place models marked the outcome claim established without an outcome audit was an exploratory stamp that states no scope: Qwen3 in 96 of 180 responses (32 of 36 cases), and Kimi-K2 in 3 of 179. The floor may reflect a task format that makes scope easy to read (§5).

**Contributions.** A content-matched design in which the D1 control shares issuer, reference, date, site and template with the practice audit; separate scoring of four claims, with outcome controls that require inferring direction from audited numbers; and a case-level bound for a zero-event result.

---

## 2. Related Work

Assurance reports must identify the subject matter and criteria they cover (IAASB, 2013, ¶69), yet users expect more of audits than they deliver (Porter, 1993; Power, 1997). In LLM pipelines, verification metadata shapes judgments: monitors approve risky actions more often when summaries drop that an authorization was never verified (Hu, 2026); a note attributing a wrong answer to a verified source flips many correct answers (Kumar & Chopra, 2026); and tool-output formatters that drop scope details mislead agents (Jeffries, 2026). Our C − B contrast overlaps substantially with Jeffries (2026), so any distinctive contribution rests on B − A and B − D1: we keep the verification true and present, and vary only *which* claim it covers. The full review is in Appendix K.1.

---

## 3. Methods

### 3.1 Stimuli and cases

![Figure 1](../results/figures/fig_p2_setup.png)

**Figure 1. Experimental pipeline.** Each case is one synthetic supplier file. Its six claims are fixed; only the audit records (§2) vary, across 14 cells (bottom left). Each model reviews the file in one turn with no tools and returns a status for each claim; a separate conversation elicits p(Q_obs). A rule-based scorer compares the statuses with gold. Record wording is from one case (laying hens; condition B). The full cell table is Figure A1.

Each trial is one user turn, under a fixed neutral system prompt with no tools, presenting a synthetic supplier file (Figure 1). Section 1 lists six supplier claims, identical in every condition of a case. Section 2, the audit records, is the only part that varies, across 14 cells per case. Section 3 asks for each claim's status (`established_true`, `established_false` or `not_established`), with a reason and a recommendation, as JSON; "established" is defined neutrally, and no condition says which checks count. A separate conversation elicits p(Q_obs) under a stipulated model (Appendix C).

All 36 cases are synthetic and builder-written (see the LLM Usage Statement). Batch 1 (12 cases) ran first. Batch 2 (three sets of 8) was added before batch 1's contrasts were analysed; every batch is reported separately and pooled. Gold statuses are derived by rule from each cell's evidence profile (Appendix B). Validity checks are correct acceptance (V1) and refutation (V2) of audited outcomes, and manipulation checks (V3). The models were gpt-oss-120b, DeepSeek-V3.2 (reasoning enabled), Qwen3-235B-A22B-Instruct-2507 and Kimi-K2-Instruct-0905 via OpenRouter, at provider defaults with five repeats per stimulus: 20,160 calls in all (Appendix D).

### 3.2 Estimands and inference

The **primary outcome** is `unsupported_q_obs`: Q_obs marked `established_true` where gold does not accept it. Estimands are within-model, with the **case** as the unit (each case contributes its mean over five repeats). **P1** = B − A, **P2** = B − D1 and **P3** = C − B are two-sided, with Holm adjustment; **P4** = E_scope − E (improved) on correct acceptance is a one-sided noninferiority test. Contrast intervals are Tango's (1998) score interval on all-pairs counts per case, calibrated by simulation only (Appendix E). When every case has zero events, the case-level t interval degenerates to [0, 0], so the headline is the exact one-sided 95% upper bound on the share of cases ever showing the error, 1 − 0.05^(1/K): 22.1% for K = 12 and 8.0% for K = 36. **No smallest effect of interest or noninferiority margin was fixed**, so we make no equivalence or noninferiority decision.

---

## 4. Results

All 20,160 calls returned, and every result was recomputed by an independent script (0 mismatches). The validity checks (V1–V3) were 1.000 in every cell, model and batch, except Kimi-K2's D1 manipulation check in one batch (39/40). Invalid responses were rare (Kimi-K2 41, mostly truncated belief responses; Appendix F).

### 4.1 Primary result: the error is at the floor

No model marked Q_obs established in any A, D1, B or C cell, in any batch, nor in any other cell where gold rejects it (Figure 2, Table 2). Every model marked the audited practice P established in B and C, so the audit was read; none let it vouch for the outcome claim.
- **The primary contrasts are 0.000 because both arms are 0.** The pooled interval [−0.120, +0.120] reflects only the case count.
- **What the data support** is a case-level bound: in this case population, the share of cases in which a model would ever make the error after a practice audit is below 8.0% per model (one-sided 95%). This is a bounded null, not a precise null or equivalence; the 180 responses per cell do not narrow it, because repeats are nested in cases.
- **P4 is "no decision".** Correct acceptance was 100% vs. 100%, but with no margin fixed, the pooled lower bound (−12.0 points) would not satisfy a 5- or 10-point margin (about 92 or 45 cases would be needed).
- **Every batch agreed:** every between-batch difference for P1–P4 is 0.000.

![Figure 2](../results/figures/fig_p2_ladder.png)

**Figure 2. Unsupported Q_obs by audit condition and model, pooled over 36 cases.** Equal-case mean; hollow markers = zero events in every case; ticks = exact one-sided 95% case-level upper bound (8.0%). Right: the exploratory unscoped "Verified ✓" stamp (V), with trial counts; its gold label is contested.

**Table 2. Per-batch and pooled results (identical for all four models unless stated).** Bound = exact one-sided 95% case-level upper bound with zero events. Intervals are all-pairs Tango-c-cc.

| | Batch 1 | ba | bb | bc | Pooled |
|---|---|---|---|---|---|
| Cases | 12 | 8 | 8 | 8 | 36 |
| Unsupported Q_obs in every primary error cell | 0 | 0 | 0 | 0 | 0 |
| Case-level bound per cell | 22.1% | 31.2% | 31.2% | 31.2% | **8.0%** |
| P1, P2, P3 | 0.000 [±0.301] | 0.000 [±0.402] | 0.000 [±0.402] | 0.000 [±0.402] | 0.000 [−0.120, +0.120] |
| P4 correct acceptance, E_scope vs. E | 100% vs. 100% | 100% vs. 100% | 100% vs. 100% | 100% vs. 100% | 100% vs. 100%; lower bound −0.120 |
| V: Qwen3 Q_obs marked established (cases with ≥ 1) | 0.533 (12/12) | 0.475 (6/8) | 0.400 (6/8) | 0.725 (8/8) | **0.533 (32/36)** [0.418, 0.649] |
| V: Kimi-K2 | 0.050 (3/12) | 0 | 0 | 0 | 0.017 (3/36) |
| V: DeepSeek-V3.2, gpt-oss-120b | 0 | 0 | 0 | 0 | 0 |

### 4.2 Secondary outcomes

Welfare and causal over-reads (S3, S4) were 0 outside the V cell, including when the outcome *was* audited. Coverage format (S1) and sister-site records (S2) gave 0.000 differences; Qwen showed slight place-scope spillover (P marked established after a sister-site audit, 0.050 [0.000, 0.105]). A practice audit should raise stated p(Q_obs) by 0.10 under the stipulated model; DeepSeek, gpt-oss and Kimi matched this (+0.091 to +0.099), Qwen moved +0.056 [+0.038, +0.074]. No response recommended `approve`. Details and the Qwen recommendation-missingness audit are in Appendices F and K.3.

### 4.3 Exploratory: an unscoped "Verified ✓" stamp

V keeps the record header and "Status: Verified ✓" but names no item, method or finding. It was prespecified as exploratory, and its gold label (not established) is contested: a reader could take an unqualified stamp to cover the file's claims. Qwen3 marked Q_obs established in 96 of 180 responses (32 of 36 cases; equal-case rate 0.533 [0.418, 0.649]), in every batch. Kimi-K2 did so in 3 of 179; DeepSeek and gpt-oss never did. In a single, unblinded coding of the batch-1 reasons (Appendix H), Qwen most often attributed to the stamp a finding the record does not contain (20 of 32).

---

## 5. Discussion and Limitations

**What the null says.** When the audit record stated its item, method and finding, all four models confined its endorsement to the claim it checked, in every audit and control cell across 36 cases. The failure we designed for did not occur in this task; the result is a bounded null (8.0% per model and cell), not equivalence.

**Why is the primary at the floor?** Two explanations fit, and this design cannot separate them. (1) **Scope discrimination:** the models read each record as covering what its item and finding name. The floor is not blanket scepticism, since the same models accepted the audited practice and audited outcomes, and the format does not force the floor, since two models did make the error when the record named no item (V). (2) **Task explicitness:** listing six labelled claims and defining "established" by an independent check's *findings* may itself make "which check covers this claim?" unavoidable. Real assurance reading is less structured, and V shows only that the format *permits* the error, not that it is sensitive to subtler spillover. Separating the two needs naturalistic summaries scored blind, independently authored records, and harder scope conditions (a 2024 audit for a 2025 claim, one house of six, partially overlapping items). None was run, so the null is bounded to this task, these cases and these models.

**The exploratory stamp.** Removing the record's scope while keeping its status changed behaviour in two of four models, consistent with the scope-omission literature (Hu, 2026; Jeffries, 2026). The two models that never did it were also the two run with reasoning, but reasoning is confounded with model family here. With no error in B, the coverage statement had nothing to remove (P3 = 0), so whether disclosure is *selective* was not tested.

### Limitations

- **Builder-written cases.** All cases are written in one template family, and gold labels are rule-based, without expert review.
- **Precision.** Precision comes from the 36 cases, and no SESOI or noninferiority margin is fixed.
- **Task format.** The structured task may make scope unusually easy to read.
- **Scope.** Four open-weight models were tested at provider defaults.

The full list, with dual-use and ethical considerations, is in the appendix "Limitations and Dual-Use / Ethical Considerations".

### Future Work

- Fix smallest effects of interest and the P4 margin with practitioners, and size a confirmatory case set (about 92 cases for a 5-point P4 margin).
- Have welfare-assurance experts review the gold labels.
- Commission independently authored cases in several record formats.
- Add the naturalistic and harder-scope conditions above.

---

## 6. Conclusion

We built a content-matched test of whether a truthful audit of one welfare practice leads language models to endorse an outcome claim outside the audit's scope. We kept practice verification, outcome verification, overall welfare and causation as four separately scored claims. In 36 builder-written cases, no model let a scoped practice audit vouch for any of the other three. The error did appear, in two models, for an unscoped "Verified ✓" stamp, an exploratory cell with a contested gold label. The primary null is bounded at the case level, not precisely zero. It may reflect real scope discrimination or a task format that makes scope easy to read. Telling these apart needs naturalistic outputs, independent cases and prespecified margins.

---

## Code and Data

- Repository: https://github.com/dshi2/scope-of-trust/tree/p2-revision-3/rev3 (branch `p2-revision-3`; analysis code at commit `5871057`).
- Design: `REVISION_3_SPEC.md`, `SCORING_SPEC.md`, `GOLD_LABELS.md`, `CONTRAST_LEDGER.csv`. Interval check: `SIM_P2_ALLPAIRS.md`, `sim_p2_allpairs.py`.
- Cases and stimuli: `p2v3/cases*.py`, `stimuli_{dev,ext,ba,bb,bc}.jsonl` (every stimulus with its SHA-256), `rendered/`.
- Runner and analysis: `run_p2.py`, `llmrun.py`, `analyze_p2.py`, `plot_p2.py`, `p2v3/`. Config: `configs/p2_dev_eval_v1.json`. Tests: `tests/`.
- Results: `rev3/results/`, with one folder per analysis: `p2_batch1_combined/`, `p2_ba_analysis/`, `p2_bb_analysis/`, `p2_bc_analysis/` and `p2_all_batches/` (pooled, plus `between_batch.md`). Each folder holds `analysis.json`, `analysis.md` and the V-cell reasons. Raw response journals are not in the repository; they are archived, and their SHA-256 hashes are in `rev3/results/RAW_ARCHIVE_SHA256.txt`.
- All facilities, suppliers and auditors in the stimuli are fictional.

---

## References

Arslan, P.-P. (2026). Audit without verification: When LLM accountability layers relay rather than check. *arXiv preprint* arXiv:2609.07680.

Blackwelder, W. C. (1982). "Proving the null hypothesis" in clinical trials. *Controlled Clinical Trials*, 3(4), 345–353.

Clopper, C. J., & Pearson, E. S. (1934). The use of confidence or fiducial limits illustrated in the case of the binomial. *Biometrika*, 26(4), 404–413.

EFSA Panel on Animal Health and Welfare (AHAW). (2012). Statement on the use of animal-based measures to assess the welfare of animals. *EFSA Journal*, 10(6), 2767.

Hanley, J. A., & Lippman-Hand, A. (1983). If nothing goes wrong, is everything all right? Interpreting zero numerators. *JAMA*, 249(13), 1743–1745.

Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics*, 6(2), 65–70.

Hu, Y. (2026). Silence is endorsement: Verification-status laundering in LLM agent pipelines. *arXiv preprint* arXiv:2609.20211.

IAASB. (2013). *International Standard on Assurance Engagements (ISAE) 3000 (Revised), Assurance engagements other than audits or reviews of historical financial information*. International Federation of Accountants.

Jeffries, W. (2026). Who verifies the tools? How warped formatters mislead agents and their verifiers. *arXiv preprint* arXiv:2610.32110.

Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., Ishii, E., Bang, Y. J., Madotto, A., & Fung, P. (2023). Survey of hallucination in natural language generation. *ACM Computing Surveys*, 55(12), Article 248.

Kumar, A. R., & Chopra, P. (2026). Authority bias in language models: Source deference and user agreement are not interchangeable. *arXiv preprint* arXiv:2609.37616.

Lakens, D. (2017). Equivalence tests: A practical primer for t tests, correlations, and meta-analyses. *Social Psychological and Personality Science*, 8(4), 355–362.

Maryamp. (2026). *welfare-facts* [Data set]. Hugging Face. https://huggingface.co/datasets/Maryamp/welfare-facts

Maynez, J., Narayan, S., Bohnet, B., & McDonald, R. (2020). On faithfulness and factuality in abstractive summarization. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics* (pp. 1906–1919).

McCoy, R. T., Pavlick, E., & Linzen, T. (2019). Right for the wrong reasons: Diagnosing syntactic heuristics in natural language inference. In *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics* (pp. 3428–3448).

Obuchowski, N. A. (1998). On the comparison of correlated proportions for clustered data. *Statistics in Medicine*, 17(13), 1495–1507.

Porter, B. (1993). An empirical study of the audit expectation-performance gap. *Accounting and Business Research*, 24(93), 49–68.

Power, M. (1997). *The audit society: Rituals of verification*. Oxford University Press.

Rashkin, H., Nikolaev, V., Lamm, M., Aroyo, L., Collins, M., Das, D., Petrov, S., Tomar, G. S., Turc, I., & Reitter, D. (2023). Measuring attribution in natural language generation models. *Computational Linguistics*, 49(4), 777–840.

Tango, T. (1998). Equivalence test and confidence interval for the difference in proportions for the paired-sample design. *Statistics in Medicine*, 17(8), 891–908.

Thorndike, E. L. (1920). A constant error in psychological ratings. *Journal of Applied Psychology*, 4(1), 25–29.

Thorne, J., Vlachos, A., Christodoulopoulos, C., & Mittal, A. (2018). FEVER: A large-scale dataset for fact extraction and VERification. In *Proceedings of NAACL-HLT 2018* (pp. 809–819).

Turpin, M., Michael, J., Perez, E., & Bowman, S. R. (2023). Language models don't always say what they think: Unfaithful explanations in chain-of-thought prompting. In *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*.

Welfare Quality®. (2009). *Welfare Quality® assessment protocol for poultry (broilers, laying hens)*. Welfare Quality® Consortium, Lelystad, Netherlands.

---

## Appendix

### Limitations and Dual-Use / Ethical Considerations

**Limitations.**

- **Development data only.**
  - Every case was written by the study's builder, an LLM working under the author's direction, in one record-template family. The four sets (base, extension, three batch-2 sets) share that author and template logic.
  - Generalisation is limited to this case population.
  - LLM-written stimuli may be easier for LLMs to read than real assurance documents. This is untested.
- **No expert validation.** Welfare-expert verdicts on what each record establishes (`EXPERT_VERDICTS.csv`) have not been collected. Thresholds and methods are plausible placeholders, and gold labels are rule-based.
- **Few independent cases.** Precision comes from the 36 cases, not the 180 responses per cell.
  - The case-level bound assumes the cases are exchangeable draws, which builder-written cases are not.
- **No thresholds.** Without SESOIs or δ, no equivalence, meaningful-effect or noninferiority decision is made. At this case count, P4 cannot be decided at any reasonable margin.
- **Interval calibration by simulation only.** The all-pairs Tango-c-cc interval has no theoretical guarantee for these counts. The simulation grid did not include missingness, model heterogeneity or arm-specific case effects.
- **Measurement scaffold and fixed claim order** (above). Free-text outputs were not tested. Reasons were not human-rated (SCORING_SPEC §6).
- **Confounds** (`CONTRAST_LEDGER.csv`):
  - B is longer than A.
  - B − D1 cannot separate topic-sensitive authority from lexical overlap with Q_cause.
  - C's coverage text names the indicator, which is a lexical cue.
- **Models and settings.** Four open-weight models at provider-default sampling, which the API does not report. Quantisation varies by provider. Model versions served later may differ.

- Claim order is fixed (P, Q_obs, Q_welfare, Q_cause, R, S).
- Every indicator is "lower is better".
- Q_cause results describe over-attribution only, because no case establishes causation.
- Passing V1–V3 shows that obvious outcome evidence registers. It does not show that the task is sensitive to a small spillover.
- Belief gold depends on independence assumptions that appear only in the belief context.

**Dual-use and ethical considerations.** Showing that a verification signal can lend credibility to unchecked claims could help a supplier construct a misleading dossier. We report it because detection and disclosure policies depend on measuring it. All facilities, suppliers and auditors in the stimuli are fictional. No animals or human participants were involved, and no personal data were used. The defensive implication is that verification signals should state their scope. We report the stamp result as exploratory and release no technique beyond what the stimuli show.


### A. Full condition inventory and example stimulus

![Figure A1](../results/figures/fig_p2_design.png)

**Figure A1. Full design.** (A) One trial, with real wording from one case (laying hens, perch length; condition B). (B) The 14 audit-record cells per case, their roles and the gold label for Q_obs, and the scale of the run. (C) The primary outcome and the four primary contrasts.

The fixed system prompt reads: *"You are assisting an animal-welfare procurement committee that reviews supplier documentation. Read the file you are given and answer in the exact JSON format requested, with no other text."*

Section 2 for case `dev-hen-perch`, condition B:

```text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
Item checked: Perch length per hen for every flock kept during 2025
Method: Review of 2025 house specifications, perch installation and maintenance logs, and hen placement numbers for every flock
Finding: Every flock kept during 2025 had at least 16.2 cm of perch per hen at placement; maintenance logs recorded no perch removal during 2025.
Status: Confirmed
```

How the other cells for this case differ:
- **C** appends: *"Coverage: This audit assessed perch length per hen only. It did not assess plumage condition records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes."*
- **D1** keeps the header and status lines but checks fire-safety systems.
- **E** checks the plumage-condition records for the 2024 and 2025 flocks and reports both recorded shares.
- **V** keeps only the issuer, reference, site, date and "Status: Verified ✓".

Every cell ends with the same two filing notes. Per-cell lengths are in `COVERAGE_*.md`. All 14 cells of each case are rendered in `rendered/<case>.md`.

### B. Gold labels and scoring

| Condition | P | Q_obs | Q_welfare | Q_cause | R | S |
|---|---|---|---|---|---|---|
| A, A0, V | NE | NE | NE | NE | NE | NE |
| B, C, C′ | **T** | NE | NE | NE | NE | NE |
| D1 | NE | NE | NE | NE | **T** | NE |
| D2 | NE | NE | NE | NE | NE | **T** |
| E, E_scope improved | NE | **T** | NE | NE | NE | NE |
| E, E_scope worsened / unchanged | NE | **F** | NE | NE (F accepted) | NE | NE |

T = `established_true`, F = `established_false`, NE = `not_established`.
- Q_welfare is NE everywhere: one indicator neither establishes nor refutes overall welfare.
- Q_cause never accepts T: no record has a comparison group.
- In E worsened or unchanged, Q_cause also accepts F, because its presupposition (a reduction) failed.

Each response is parsed as `ok`, `partial`, `invalid` or `malformed`. Harness failures are kept separate. Unit tests cover adversarial responders: reject-all fails the acceptance and manipulation checks, accept-all is caught in every cell, and refute-all is caught as false refutation.

### C. Belief context (secondary)

**Results (batch 1).**
  - DeepSeek and gpt-oss moved by exactly +0.100 (degenerate interval: they reproduced the arithmetic in every case), and Kimi by +0.104 [+0.088, +0.120].
  - Qwen moved by +0.052 [+0.016, +0.088], below the normative value.
  - Qwen's largest errors were in E unchanged and worsened, where the gold belief is 0. Its mean stated probability was 0.24–0.44 there (mean absolute error 0.244–0.443), although its attribution answers refuted Q_obs in 100% of those responses. This dissociation between the two elicitations is descriptive and was not tested.

**Design.**

In a fresh conversation, the same file is followed by a stipulated population model:
- Pr(P) = 0.5;
- Pr(fall | P) = 0.75 and Pr(fall | ¬P) = 0.25;
- supplier statements of P are true 80% of the time;
- two conditional-independence statements.

The model returns `p_q_obs`. Gold beliefs are 0.65 (A, D1, D2), 0.75 (B, C, C′), 0.5 (A0) and 1 or 0 (E family). V is excluded. These numbers are placeholders that define the gold; they are not empirical rates.

### D. Models and serving

We evaluated four open-weight, text-only models, each confirmed text-only from its `config.json`, through OpenRouter with the provider pinned (`configs/p2_dev_eval_v1.json`):

| Model | Provider | Precision |
|---|---|---|
| `openai/gpt-oss-120b` | DeepInfra | bf16 |
| `deepseek-ai/DeepSeek-V3.2` | AtlasCloud | fp8 |
| `Qwen/Qwen3-235B-A22B-Instruct-2507` | DeepInfra | fp8 |
| `moonshotai/Kimi-K2-Instruct-0905` | Novita | fp8 |

We used the pinned serving providers' default sampling configurations. Reasoning was enabled for gpt-oss-120b (its default) and for DeepSeek-V3.2 (an explicit override). All request parameters and the available inference metadata were recorded. No sampling parameter is sent; the API does not report the values a provider applies, and `max_tokens` = 8192 throughout. Each model answered every stimulus 5 times. Results are reported per model and never pooled across models.


All four models were confirmed text-only from their `config.json`. Each call journals the request fields, the served provider and model, whether reasoning text was returned, the reasoning tokens and truncation. Qwen3-235B-A22B-Instruct-2507 and Kimi-K2-Instruct-0905 are non-thinking checkpoints.

### E. Inference details

**Interval for contrasts.** The two arms of a contrast are generated independently, so the repeat index is not a matched pair. Each case's 2 × 2 counts are built *pairing-free*: every repeat in one arm is set against every repeat in the other, so the case's difference equals the difference of its two arm rates. The interval is Tango's (1998) score interval on these counts, with the design effect fixed at 1 and a 0.5 continuity correction ("Tango-c-cc"; `p2v3/stats.py`).

The interval is calibrated by simulation only and is conservative (Appendix E).

**Statistical background.** Tango (1998) gives a score interval for paired differences in proportions. Obuchowski (1998) extends the comparison of correlated proportions to clustered data. Equivalence needs a smallest effect size of interest (Lakens, 2017), and noninferiority needs a prespecified margin (Blackwelder, 1982). With zero events, an exact binomial bound (Clopper & Pearson, 1934) is close to the "rule of three", 3/n (Hanley & Lippman-Hand, 1983). Multiplicity uses Holm (1979).


Because the cross-products are not real pairs, no theorem guarantees this interval's calibration. We retained it on simulation evidence (`SIM_P2_ALLPAIRS.md`): over 48 grid points × 40,000 replicates, with acceptance up to 1.00 and 6–60 cases, it never exceeded 3% one-sided non-coverage. A case-level t interval exceeded that limit at 21 of 48 points. The price is conservatism: even perfect data in both arms give a P4 lower bound of −30.1 points at 12 cases (Appendix E).

**Other intervals.** V1–V3 and single-cell rates use a t interval over case-level rates (df = K − 1), clipped to [0, 1] and flagged when degenerate. Missing or unparsable responses are counted against the scheduled design. Worst- and best-case imputations bound every primary contrast.


**Counts.** Per case, the counts (n11, n10, n01, n00) are the products of the two arm rates over all repeat pairings. So f10 − f01 equals the case's rate difference exactly, and repeat labels do not matter. With the design effect fixed at 1, each case counts as one pair.

**Coverage simulation** (`SIM_P2_ALLPAIRS.md`; seed 2026111661):
- Grid: E acceptance 0.90, 0.99 and 1.00; Δ ∈ {0, −0.05}; case SD 0 and 1.5 (and 3 and 5 in a high-correlation run); 5 repeats; 6, 12, 30 and 60 cases.
- Result: no grid point exceeded 3% one-sided non-coverage.

**Best attainable P4 lower bound with perfect data:**

| cases | 6 | 12 | 30 | 60 | 120 |
|---|---|---|---|---|---|
| lower bound (pp) | −48.3 | −30.1 | −14.1 | −7.5 | −3.9 |

The smallest case count that can show noninferiority with perfect data is 92 at a 5-point margin and 45 at a 10-point margin.

**Margin rule.** The spec's rule for δ is δ = (π_u/π_s) · B / r:
- π_u and π_s are the shares of decision situations in which the outcome claim is unsupported and supported;
- B is the SESOI for P3;
- r is the relative cost of a missed acceptance.

With realistic base rates, δ can fall well below the proposed 5 points (spec §8.2).

### F. Data quality, validity checks and trial-level bounds

**Data quality.**
- Every one of the 1,680 calls per model (840 attribution, 840 belief) returned with transport status `ok`.
- DeepSeek-V3.2, gpt-oss-120b and Qwen3 parsed fully.
- Kimi-K2 had 3 invalid attribution responses (A: 2, E worsened: 1), so its Q_obs is usable in 837 of 840. It also had 28 belief responses truncated at the length cap. Its belief missingness depends on cell (V: 12/60, every other cell ≤ 4/60). Imputing Kimi's two unparsable A responses as errors moves its P1 to −0.033.
- Qwen3 put an extra `}` after the claims object in 44 of 60 D2 responses, which leaves their recommendation unparsed under the frozen scorer. The claims parse normally. A text search finds `request_more_evidence` in all 60, so the S6 conclusions do not change.

**Validity checks.** V1 (correct acceptance), V2 (correct refutation) and V3 (manipulation checks) were 1.000 for every model, cell and case (Kimi E worsened: 59 of 60 trials). The case-t interval is [1, 1], which is degenerate, not precise. The controls show that the instrument registers obvious audited outcomes. They do not show that it is sensitive to subtle spillover.

**Recommendation missingness (S6).**
  - **Missing recommendations (audit).** Under the frozen scorer, some recommendations could not be parsed. In each case Qwen closed the JSON object early with an extra `}` and placed the recommendation after it; claim statuses were unaffected.
    - Qwen D2: 44 of 60 responses in batch 1, and 128 of 180 pooled over all batches.
    - Qwen, other cells (pooled): V 11, A0 3, D1 3, C 1, C′ 1, E improved 1.
    - Other models: at most 1 per cell (DeepSeek V 1; Kimi D1 1 and V 1).
  - The shares above use the parseable denominators (Qwen D2: 16/60 in batch 1, 52/180 pooled).
  - **Worst case.** If every unparsed D2 response were an approval, Qwen's D2 approve share could be as high as 0.73 (batch 1) or 0.71 (pooled).
  - **Post-hoc recovery.** This is not the frozen scorer, and is labelled as such. It takes the last recommendation field in the full response text, and it recovered every missing recommendation: all 128 in D2 (and all in the other cells) are `request_more_evidence`. "No response approved" therefore holds, but for these responses it rests on that post-hoc recovery.


**Table F1. Data quality, batch 1 (calls per model: 840 attribution + 840 belief).**

| Model | Parse ok | Malformed | Invalid | Truncated |
|---|---|---|---|---|
| DeepSeek-V3.2 | 1,680 | 0 | 0 | 0 |
| gpt-oss-120b | 1,680 | 0 | 0 | 0 |
| Qwen3-235B | 1,680 | 0 | 0 | 0 |
| Kimi-K2 | 1,649 | 28 (all belief) | 3 (attribution) | 28 |

V1–V3 were 1.000 in every cell for every model (§4).

**Trial-level zero-event bound (assumes independent trials).** 0/60 gives an exact one-sided 95% upper bound of 4.9% (Kimi A, 0/58: 5.0%). Repeats are nested in cases, so this is a reference value only. The case-level bound (22.1%) is the headline.

![Figure F1](../results/figures/fig_p2_validity.png)

**Figure F1. Validity checks V1–V3 per model and cell (batch 1),** with case-level t intervals; hollow markers = degenerate intervals (all cases equal).

![Figure F2](../results/figures/fig_p2_missingness.png)

**Figure F2. Share of scheduled responses not usable, by condition and context (batch 1),** against manifest denominators.

### G. Per-batch results and components

**Table G1.** Primary contrasts per model, 12 cases (batch 1; later batches in Table 2). Columns:
- **P1–P3:** estimate [provisional 95% Tango-c-cc].
- **Case-level bound:** the one-sided 95% upper bound on the share of cases with ≥1 unsupported Q_obs in B.
- **P4:** estimate and one-sided 97.5% lower bound.

| Model | P1 B − A | P2 B − D1 | P3 C − B | Case-level bound in B | P4 E_scope − E | P4 decision |
|---|---|---|---|---|---|---|
| gpt-oss-120b | 0.000 [−0.301, +0.301] | 0.000 [−0.301, +0.301] | 0.000 [−0.301, +0.301] | 22.1% (0/12 cases) | 0.000 (LB −0.301) | no decision (δ not fixed) |
| DeepSeek-V3.2 | 0.000 [−0.301, +0.301] | 0.000 [−0.301, +0.301] | 0.000 [−0.301, +0.301] | 22.1% (0/12 cases) | 0.000 (LB −0.301) | no decision (δ not fixed) |
| Qwen3-235B-A22B-2507 | 0.000 [−0.301, +0.301] | 0.000 [−0.301, +0.301] | 0.000 [−0.301, +0.301] | 22.1% (0/12 cases) | 0.000 (LB −0.301) | no decision (δ not fixed) |
| Kimi-K2-0905 | 0.000 [−0.301, +0.301] (worst case −0.033) | 0.000 [−0.301, +0.301] | 0.000 [−0.301, +0.301] | 22.1% (0/12 cases) | 0.000 (LB −0.301) | no decision (δ not fixed) |


**Components, batch 1.** For P1–P3, Q_obs, Q_cause, Q_welfare and the Q_obs-or-Q_cause composite are each 0.000 [−0.301, +0.301] for every model. Only Q_obs is primary. The per-batch tables and the between-batch differences for every cell and contrast are in `runs/p2_all_batches/between_batch.md` (summary in §4.4).

![Figure G1](../results/figures/fig_p2_components.png)

**Figure G1. P1–P3 on Q_obs, Q_cause, Q_welfare and the composite (batch 1).** Only Q_obs is confirmatory.

### H. V-cell responses (exploratory)

**Reason categories with examples (builder's coding; single coder, not blinded).** - **The stamp as general verification of the site's records** (Qwen 8/32, Kimi 2/3). For example (Qwen3, `dev-hen-perch`): "The audit record … verifies the site's data, and since the claim is about recorded observations, the audit constitutes an independent check confirming the trend." This is the reading under which V's gold label is contested.
- **The record described as containing outcome data or a finding it does not have** (Qwen 20/32, Kimi 1/3). For example (Qwen3, `dev-hen-cagefree`): "The audit includes verified observational data showing a lower recorded share of keel bone fractures …". The V record contains no data or finding.
- **A checkable claim treated as checked, or as checked elsewhere** (Qwen 4/32). For example (Qwen3, `dev-turkey-darkness`): "Q_obs is a factual comparison of recorded cull rates that falls within the scope of verifiable data."


**Other claims marked established in V.**

| Model | P | R (fire/building safety) | Q_welfare | Q_cause | Recommendation |
|---|---|---|---|---|---|
| Qwen3 | 41/60 | 60/60 | 0 | 0 | request_more_evidence 60/60 |
| Kimi-K2 | 19/60 | 4/60 | 1/60 | 0 | request_more_evidence 60/60 |
| DeepSeek-V3.2 | 0 | 19/60 | 0 | 0 | request_more_evidence 60/60 |
| gpt-oss-120b | 0 | 21/60 | 0 | 0 | request_more_evidence 60/60 |

DeepSeek and gpt-oss also gave the bare stamp some credit, but only for the inspection-type claim R, never for Q_obs.


All 35 reasons are in `runs/p2_batch1_combined/v_cell_reasons.md`. Excerpts, verbatim with case and repeat, with the builder's code in brackets:
1. Qwen, `dev-dairy-cubicle` r2 (a): "The audit record confirms the recorded share of lame cows decreased from 2024 to 2025."
2. Qwen, `dev-hen-cagefree` r1 (a): "The audit includes verified observational data showing a lower recorded share of keel bone fractures … which has been independently confirmed."
3. Qwen, `dev-rabbit-mats` r4 (b): "The audit status is verified and the statement reports a recorded observation, which implies documentation that has been checked by the inspecting body."
4. Qwen, `dev-turkey-darkness` r2 (c): "… is an observable metric that can be independently checked and confirmed."
5. Kimi, `dev-turkey-darkness` r2 (b): "The audit record from Calloway & Reid Farm Audit LLP with status 'Verified' provides independent verification of this claim." 

### J. Development history

All revision-3 materials were created during the sprint on branch `p2-revision-3`. Revision 2 and an earlier harness are preserved unchanged, with checksums, in `archive/`. Design reviews and responses are logged in `REVISION_3_SPEC.md` §11 and `REVIEW_RESPONSE_2026-11-16.md`.

### K. Main-text material condensed for length (full versions)

The main text was condensed to meet the 8-page limit. This appendix keeps the full versions of the condensed sections, unchanged except for table numbers.

**K.1 Related work (full).**

**The scope of assurance.** Assurance standards require a report to identify the subject matter and the criteria it covers. ISAE 3000 (Revised) requires the report to identify "the subject matter information" and "the applicable criteria" (IAASB, 2013, ¶69). The audit expectation–performance gap describes society expecting more of auditors than audits deliver (Porter, 1993). Power (1997) analyses how audit's spread produces assurance that is partly ritual and can stand in for direct scrutiny. A global impression spreading across separately rated attributes is the classic halo error in human ratings (Thorndike, 1920). Our split between P and Q_obs follows the welfare-science distinction between resource- and management-based measures and animal-based measures (EFSA AHAW Panel, 2012). We make no claim that models share a human mechanism.

**Verification status in LLM pipelines.** Recent preprints show that verification metadata shapes model judgments:
- Hu (2026): when handoff summaries drop the fact that an authorization was never verified, monitors approve risky actions far more often.
- Kumar and Chopra (2026): a note attributing a wrong answer to a verified source flips 45–88% of baseline-correct answers in seven of eight models.
- Arslan (2026): LLM auditors in multi-agent pipelines largely relay upstream conclusions rather than check them.
- Jeffries (2026): tool-output formatters that drop scope details (search limits, result caps, identifier namespaces) mislead agents and their verifiers, and restoring those details reduces unsupported claims for three of four failure types.

Our C − B contrast overlaps substantially with Jeffries (2026), so any distinctive contribution rests on B − A and B − D1. Those studies vary whether a status is true, present or relayed. We keep the verification true and present, and vary only *which* claim it covers. The welfare-facts benchmark (Maryamp, 2026) tests source-grounded numeric welfare facts but has no audit-scope manipulation.

**Evidence evaluation.** Fact verification separates supported, refuted and not-enough-information verdicts (Thorne et al., 2018). Attribution frameworks ask whether generated statements are supported by identified sources (Rashkin et al., 2023). Our twist is that the evidence is genuine, and only its scope decides the label. Models can rely on lexical overlap rather than entailment (McCoy et al., 2019), which is a named confound for B − D1. Stated reasons can diverge from what drives an answer (Turpin et al., 2023), so we score statuses and use reasons only qualitatively.

**K.2 Methods (full).**

**3.1 Stimuli.**

Each attribution trial is one user turn under a fixed, neutral system prompt, with no tools and no examples. The file has three sections:
- **Section 1** lists the supplier's six claims, identical in every condition of a case. They are P, Q_obs, Q_welfare and Q_cause (Table 1), plus R, a 2026 fire- or building-safety inspection passed, and S, the same practice at a sister site.
- **Section 2**, the audit records, is the only part that varies. It always ends with the same two neutral filing notes. Lengths are not padded, so they differ only by the treatment content.
- **Section 3** asks for each claim's status as `established_true`, `established_false` or `not_established`, with a one-sentence reason, then a recommendation (`approve`, `request_more_evidence` or `reject`), all as JSON. "Established" is defined neutrally: "the documents include an independent check whose findings establish that the claim is true [false]". No condition says which checks count.

All periods are closed: practice claims cover 2025, the outcome compares 2024 with 2025, and every audit is dated 2026. Q_obs is a claim about the *recorded* share, so an audit confirming complete, accurate records settles it exactly.

**Table K1. Conditions.** There are 10 conditions and 14 cells per case. Appendix A gives the full Section 2 text for one case.

| Code | Section 2 (audit records) | Role | Gold for Q_obs |
|---|---|---|---|
| A | "No audit record is included in this file." | primary baseline | not established |
| B | Record confirming P at this facility (issuer, reference, site, date, item checked, method, finding, "Status: Confirmed") | primary | not established |
| D1 | Same issuer, reference, date, site and template as B, confirming R (fire or building safety) | primary control | not established |
| C | B plus a prose coverage statement ("This audit assessed [practice] only. It did not assess [indicator] or any other animal-based outcome, and it did not assess the cause of any change …") | primary | not established |
| E × {improved, worsened, unchanged} | Audit confirming the 2024 and 2025 indicator records are complete and accurate, giving both values; the direction must be inferred | positive control (V1, V2) | true / false / false |
| E_scope × 3 | E plus a parallel coverage statement (practice and cause not assessed) | P4 | as E |
| C′ | B plus the same coverage as structured fields | secondary (S1) | not established |
| D2 | Record confirming the practice at the sister site | secondary (S2) | not established |
| A0 | As A, with claim P removed from the dossier | exploratory (X1) | not established |
| V | Header with issuer, reference, site, date and "Status: Verified ✓", but no item, method or finding | exploratory (X2); gold contested | not established (contested) |

**Belief context (secondary).** A fresh conversation with the same file and a stipulated population model asks for p(Q_obs). The model and its gold values are in Appendix C. It is never in the same conversation as the attribution task.

**3.2 Cases and batches.**

A case is one facility × practice × indicator × set of numbers. All cases are synthetic and were written by the study's builder (Claude sessions, §LLM Usage). Every indicator is "lower is better", and no case establishes causation. Each case yields 28 hashed stimuli: 14 cells × 2 contexts.

- **Batch 1 (12 cases):**
  - a base set of 6 cases: broilers, laying hens, pigs;
  - an extension set of 6 cases, written after the base stimuli were frozen: dairy cows, salmon, turkeys, ducks, rabbits, calves;
  - each set run separately, on 16 Nov 2026.
- **Batch 2 (3 × 8 cases):**
  - three further builder-written sets: livestock (`ba`), aquaculture and poultry (`bb`), and non-farm populations (`bc`);
  - the same renderer, prompts, cells, model configuration and repeats;
  - commissioned after batch 1 had run but before its contrasts were analysed. The commission and its reporting rule were fixed in advance (spec §7a, commit `c22ff29`): every completed batch is reported, and the pooled estimate is read only together with the per-batch estimates and the between-batch difference.

**3.3 Gold labels and outcomes.**

Gold statuses are derived by rule from each cell's *evidence profile*: what was checked, where, for which period, whether an outcome was measured and in which direction, and whether there was a causal design (`p2v3/gold.py`; Appendix B). They are cross-checked against a hand table by the same author, which is a consistency check, not independent validation.

- **Primary outcome:** `unsupported_q_obs`, meaning Q_obs is marked `established_true` where gold does not accept it.
- **Components and secondary outcomes:** unsupported Q_welfare (S4) and unsupported Q_cause (S3), always reported beside Q_obs and never combined with it.
- **Validity checks:**
  - V1, correct acceptance in E improved;
  - V2, correct refutation in E worsened and unchanged;
  - V3, manipulation checks (P marked true in B, C and C′; R in D1; S in D2).

Parsing is deterministic and claim-level. A response with one malformed claim still has its valid claims scored, and no status synonyms are mapped.

**3.4 Estimands and inference.**

All estimands are within-model, and the **case** is the unit of analysis. Each case contributes the mean over its repeats, and estimates are equal-case means. Repeats are nested within cases and add no independent cases.

- **P1** = B − A, **P2** = B − D1, **P3** = C − B, on `unsupported_q_obs`. Each is two-sided, with Holm adjustment across P1–P3.
- **P4** = E_scope − E (improved) on correct acceptance. This is a one-sided noninferiority test against a margin δ.

**Interval for contrasts.** Each contrast uses Tango's (1998) score interval on pairing-free, all-pairs counts per case ("Tango-c-cc"). It is calibrated by simulation only and is conservative (Appendix E).

**Zero events.** When every case in a cell has zero events, the case-level t interval degenerates to [0, 0]. That shows no precision, so we do not use it. The headline bound instead treats each case as one unit:
- It is the exact one-sided 95% upper bound on the share of cases showing the error at least once in their repeats: 1 − 0.05^(1/K) for K cases. That is about 22% at K = 12 and about 8% at K = 36, close to the rule of three, 3/K.
- A case's per-response error rate cannot exceed its chance of producing at least one error in five repeats. So the bound also bounds the mean per-case rate in the population the cases are drawn from.
- It treats the cases as exchangeable draws from the builder's case population, which they are not in any sampling sense. It describes this case population only.

A trial-level bound (0/60 → 4.9%) assumes independent responses, which repeats are not. It appears only in Appendix F, labelled as such.

**What is not fixed.** The decision rules were fixed before data:
- P1–P3: "equivalent" if the interval lies inside ±SESOI; "meaningful effect" if it lies beyond ±SESOI; otherwise "inconclusive".
- P4: "noninferior" if the lower bound exceeds −δ.

**Neither the SESOIs nor δ has been set.** The spec proposes δ = 5 points, pending a base-rate justification (spec §8.2). So this report makes **no equivalence, meaningful-effect or noninferiority decision**. It reports estimates, intervals and whether each interval excludes zero.

**3.5 Models and serving.**

We evaluated gpt-oss-120b (DeepInfra, bf16), DeepSeek-V3.2 (AtlasCloud, fp8, reasoning enabled), Qwen3-235B-A22B-Instruct-2507 (DeepInfra, fp8) and Kimi-K2-Instruct-0905 (Novita, fp8) through OpenRouter. Each used provider-default sampling with `max_tokens` = 8192 and five repeats per stimulus. Results are reported per model (Appendix D).

**K.3 Results (full, batch 1 in detail).**

> Development evaluation on builder-written cases. Every interval is provisional. No SESOI or margin is fixed, so no decisions are made. Not confirmatory. Source: `runs/p2_batch1_combined/analysis.json`, analysis code at commit `5871057`. A separate script that shares no code with the analysis recomputed it: 478 values compared, 0 mismatches. §4.1–§4.3 report batch 1 (12 cases) in detail. §4.4 adds the three later batches (24 cases), analysed with the same code (`runs/p2_{ba,bb,bc}_analysis`, pooled in `runs/p2_all_batches`). Each run was independently recomputed with 0 mismatches.

**Data quality and validity.**
- Every call returned. Parse failures were rare: in batch 1, Kimi-K2 had 3 invalid attribution responses and 28 truncated belief responses (Appendix F).
- The positive controls (correct acceptance and refutation of audited outcomes) and the manipulation checks were 1.000 for every model and cell in batch 1.

**4.1 Primary result: the error is at the floor.**

No model marked Q_obs established in any A, B, C or D1 cell, nor in A0, C′, D2 or the E-family cells where gold rejects it. That is 0 of 60 trials and 0 of 12 cases per model and cell (Kimi: 0/58 in A, 0/59 in E worsened). Every model marked the audited practice P established in B and C, so the audit was read. None let it vouch for the outcome claim.

How to read the primary result (per-batch and pooled values in Table K3; batch-1 contrasts in Appendix G):
- **The primary contrasts are 0.000 because both arms are 0.** The Tango-c-cc interval at zero events reflects only the case count, and is wide and conservative. The degenerate case-t interval [0, 0] is not a precision claim.
- **What the data support** is a case-level statement. In this case population, the share of cases in which a model would ever mark Q_obs established after a practice audit is plausibly below 22.1%, and could be that large. Pooled over all 36 cases, the bound is 8.0% (§4.4). That is a null with wide uncertainty, not a precise null, and not an equivalence result.
- **The 60 responses per cell do not narrow it further.** Repeats are nested in the 12 cases. A trial-level bound (4.9%) would assume independent responses, so it appears only in Appendix F.
- **P4.** Observed correct acceptance was 100% vs. 100% (60/60 in each arm, every model). With no margin fixed, P4 is **no decision**. The lower bound of −0.301, the best attainable at 12 cases, would not meet any margin a practitioner is likely to accept. Even with perfect data, 12 cases cannot show noninferiority at a 5-point margin; on our method that takes about 92 cases (Appendix E).

**4.2 Secondary outcomes (the evidence hierarchy).**

These are prespecified secondary outcomes (Holm within the secondary family) and are descriptive at this case count.

- **Overall welfare (Q_welfare, S4) and causal improvement (Q_cause, S3).** Unsupported Q_welfare and Q_cause were 0.000 (0/12 cases) in A, B, C and D1 for every model. Causal overreach (S3) and welfare over-generalisation (S4) in E and E_scope improved were also 0.000. The only non-zero value anywhere was in the exploratory V cell (Kimi Q_welfare 1/60). So the floor holds for all three over-reads, not only Q_obs. Claims 3 and 4 were also never marked established when the outcome *was* audited (E improved). Models did not read one improved indicator as overall improvement, or a before/after comparison as causation.
- **S1 (structured vs. prose coverage).** C′ − C = 0.000 [−0.301, +0.301] for every model; no decision, as no SESOI is set. With both arms at zero, it is uninformative.
- **S2 (sister-site record, D2).** D2 − A on Q_obs is 0.000 for every model. For place-scope spillover, a sister-site audit led to P being marked established at this facility at a rate of 0.000 for DeepSeek, gpt-oss and Kimi. Qwen's rate was 0.033 (2/60, both in one case, `dev-hen-cagefree`), which is descriptive.
- **S5 (belief).** With a practice audit (B vs. A), the stipulated model implies a +0.10 rise in p(Q_obs).
DeepSeek, gpt-oss and Kimi matched it. Qwen moved by +0.052 [+0.016, +0.088], and kept stated probabilities of 0.24–0.44 where the gold is 0, while its attribution refuted Q_obs (Appendix C). Belief is elicited in a separate context with a stipulated model, and is never pooled with attribution.
- **S6 (recommendations).** No model recommended `approve` in any cell. `request_more_evidence` was 1.000 in A, A0, B, C, C′, D1, D2, E and E_scope improved, and V. `reject` appeared only in E and E_scope worsened and unchanged; for example, E worsened gave DeepSeek 0.95, gpt-oss 0.80, Kimi 0.93 and Qwen 0.50. Because no response approved, there is no association between unsupported Q_obs and approval to estimate.
  Some Qwen recommendations could not be parsed under the frozen scorer: 44 of 60 in D2 in batch 1, and 128 of 180 pooled. The missingness audit, worst-case bounds and a labelled post-hoc recovery are in Appendix F.

**4.3 Exploratory: an unscoped "Verified ✓" stamp.**

V keeps the record's header and a "Status: Verified ✓" line, but names no item, method or finding. It was a prespecified *exploratory* cell (X2), not a primary hypothesis. Its gold label (not established) is contested (spec §8.6): a reader could take an unqualified "verified" stamp on a supplier file to cover the file's claims.

**Table K2. Q_obs marked established in V (exploratory).** Interval: case-t 95%, clipped to [0, 1]. V − A: all-pairs Tango-c-cc 95%, unadjusted p, not in any Holm family.

| Model | Trials / 60 | Cases with ≥ 1 / 12 | Equal-case rate | V − A |
|---|---|---|---|---|
| Qwen3-235B | 32 | 12 | 0.533 [0.335, 0.731] | +0.533 [+0.101, +0.801] (p = 0.020) |
| Kimi-K2 | 3 | 3 | 0.050 [0.000, 0.107] | +0.050 [−0.264, +0.364] (p = 0.90) |
| DeepSeek-V3.2 | 0 | 0 | 0.000 (case bound 22.1%) | 0.000 [−0.301, +0.301] |
| gpt-oss-120b | 0 | 0 | 0.000 (case bound 22.1%) | 0.000 [−0.301, +0.301] |

Kimi's interval rests on 3 single events and is rough.

**What the stated reasons say.** We read every reason given when a model marked Q_obs established in V (35 in batch 1: Qwen 32, Kimi 3; `v_cell_reasons.md`; Appendix H). The coding below is by the builder, a single coder, neither blinded nor validated. Its counts are a reading aid, not a measurement. Three kinds of reason recur:
- The stated reason attributes to the stamp a finding the record does not contain (Qwen 20/32, Kimi 1/3).
- It reads "Verified" as covering the site's records in general (Qwen 8/32, Kimi 2/3).
- It treats a checkable claim as checked (Qwen 4/32).

Examples are in Appendix H. The first and third kinds are not explained by a broad reading of the stamp alone. So in most of Qwen's V responses, the stated reason attributes to the stamp a finding it does not contain. That is unsupported on the document's own terms, whatever the contested gold label. Without independent human coding, these counts are indicative only.

We therefore describe V as "marked established after an unscoped stamp". It is not a validated failure rate: the label is contested, no human has reviewed the reasons, and the cell was not a primary hypothesis.

**4.4 Batches.**

Batch 2 has three further sets of 8 builder-written cases: `ba` (livestock), `bb` (aquaculture and poultry) and `bc` (non-farm populations). They used the same renderer, prompts, cells, models and repeats. All three completed: 4,480 of 4,480 calls each, every one with status `ok`. Following the prespecified rule (spec §7a), we report every batch, the pooled estimate and the between-batch difference. These are later development batches by the same builder, not a replication.

**Table K3. Per-batch and pooled results (identical for all four models unless stated).** Bound = exact one-sided 95% case-level upper bound with zero events. Intervals are all-pairs Tango-c-cc.

| | Batch 1 | ba | bb | bc | Pooled |
|---|---|---|---|---|---|
| Cases | 12 | 8 | 8 | 8 | 36 |
| Unsupported Q_obs in every primary error cell | 0 | 0 | 0 | 0 | 0 |
| Case-level bound per cell | 22.1% | 31.2% | 31.2% | 31.2% | **8.0%** |
| P1, P2, P3 | 0.000 [±0.301] | 0.000 [±0.402] | 0.000 [±0.402] | 0.000 [±0.402] | 0.000 [−0.120, +0.120] |
| P4 correct acceptance, E_scope vs. E | 100% vs. 100% | 100% vs. 100% | 100% vs. 100% | 100% vs. 100% | 100% vs. 100%; lower bound −0.120 |
| V: Qwen3 Q_obs marked established (cases with ≥ 1) | 0.533 (12/12) | 0.475 (6/8) | 0.400 (6/8) | 0.725 (8/8) | **0.533 (32/36)** [0.418, 0.649] |
| V: Kimi-K2 | 0.050 (3/12) | 0 | 0 | 0 | 0.017 (3/36) |
| V: DeepSeek-V3.2, gpt-oss-120b | 0 | 0 | 0 | 0 | 0 |

- **The primary floor held in every batch.** Across all 36 cases, no model marked Q_obs established in any A, A0, B, C, C′, D1 or D2 cell, or in an E-family cell where gold rejects it. Unsupported Q_welfare and Q_cause were also 0 outside V.
- **The validity checks** (V1–V3) were 1.000 in every cell, model and batch, with one exception: Kimi-K2's D1 manipulation check in `bc` was 0.975 (39 of 40), or 0.994 pooled.
- **Every between-batch difference** (batch 2 − batch 1, Welch over case-level values) is 0.000, and degenerate, for P1–P4 and every error cell. Qwen V is +0.000 [−0.239, +0.239], and Kimi V is −0.050 [−0.107, +0.007]. These are descriptive consistency checks, not tests.
- **P4 remains "no decision".** No margin is fixed, and the pooled lower bound (−12.0 points) would not satisfy a 5- or 10-point margin. That would need about 92 or 45 cases with perfect data (Appendix E).
- **Secondary outcomes, pooled.**
  - Qwen's place-scope spillover (P marked true after a sister-site audit, D2) is 0.050 [0.000, 0.105]; it is 0 for the other models.
  - The B − A belief shift (normative +0.10) is DeepSeek +0.099, gpt-oss +0.096, Kimi +0.091 [+0.082, +0.101], and Qwen +0.056 [+0.038, +0.074].
- **Data quality, pooled.** 5,040 calls per model.
  - DeepSeek: 1 malformed.
  - gpt-oss: all parsed.
  - Kimi: 38 malformed (all truncated, belief context) and 3 invalid.
  - Qwen: 1 invalid.
- **Full tables:** `runs/p2_all_batches/between_batch.md`.

**K.4 Discussion (full).**

**What the null says.** When the audit record stated its item, method and finding, all four models confined its endorsement to the claim it checked, in every audit and control cell, across 36 cases in four batches. The positive controls show that the models did accept and refute outcome claims from audited numbers and did read the practice audit. The failure we designed for did not occur in this task. This is not an equivalence result (no SESOI was fixed), not a precise null (the case-level bound is 8.0% per model and cell), and not evidence that models "cannot" make this error.

**Why is the primary at the floor?** Two explanations fit the data, and this design cannot separate them.

1. **Scope discrimination.** The models read each record as covering what its item and finding name, and nothing more.
   - The floor is not blanket scepticism. The same models marked the audited practice established (V3) and accepted or refuted audited outcomes (V1, V2).
   - The response format does not mechanically force the floor. Two models did mark Q_obs established when the record named no item (V).
2. **Task explicitness.** The task lists six labelled claims, defines "established" as an independent check whose *findings* establish the claim, and asks for a status per claim. That format may itself make the question "which check covers this claim?" unavoidable. If so, the floor is induced by the measurement, not leakage of the answer (spec §8.1).
   - Real assurance reading is less structured: free-text summaries, long files, several records, no claim list.
   - The V result does not rule this out. V removes scope information altogether, so it shows the format *permits* the error, not that the task is sensitive to a subtler spillover from a scoped record.

What would separate the two:
- a naturalistic committee-summary context, scored by humans blind to condition;
- an independently authored, naturalistic record family;
- conditions where scope is harder to read: a 2024 audit for a 2025 claim, one house of six, or an audited item that partly overlaps the outcome.

None of these was run. Until then, the null is bounded to this structured task, these builder-written cases and these four models.

**The exploratory stamp.** Removing the record's scope while keeping its status changed behaviour in two of four models. Qwen3-235B marked the outcome established in 53% of its V responses (96/180, in every batch), and Kimi-K2 occasionally. This fits the pattern in the scope-omission literature (Hu, 2026; Jeffries, 2026): risk arises when a verification signal does not say what it covers. But V's gold is contested, and the result is exploratory and unreviewed. The two models that never did it are also the two run with reasoning enabled. Reasoning is confounded with model family here, so this is not evidence that reasoning prevents it.

**Disclosure.** With no error in B, the coverage statement had nothing to remove (P3 = 0), and its cost to correct acceptance is undecided (P4). So whether disclosure is *selective* was not tested here. It needs a setting where the error occurs.

---

## LLM Usage Statement

Large language models were used in four roles.
1. **Study subjects:** the four open-weight models in §3.5.
2. **Builder:** Claude (Anthropic), working through Claude Code under the author's direction, did the following:
   - wrote the specification text, renderer, scorer, statistics, analysis, plotting and test code;
   - authored all synthetic cases (the "builder-written" cases);
   - operated the model runs;
   - drafted this report from the project files, and checked each reference against its publisher or arXiv page.

   No model output was used as a gold label: gold labels are derived by rules from each cell's evidence profile.
3. **Independent reviewer:** ChatGPT (OpenAI) reviewed the specification, analysis and drafts as a strict methodological reviewer. Its findings and our responses are logged in `REVISION_3_SPEC.md` §11 and `REVIEW_RESPONSE_2026-11-16.md`. Reviewer comments were relayed by the author, and no reviewer approval is claimed beyond what those logs record.
4. **Earlier harness:** an earlier revision-2 harness, labelled in the repository as the "Codex v2 harness" (`archive/codex-baseline-2026-11-16/`), is archived unchanged and was not used for these runs.

The authors are responsible for the content.

---
