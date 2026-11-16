# The Scope of Trust: Truthful Practice Audits and Out-of-Scope Endorsement by Language Models

> **Draft status (delete before submission).** Every `[[...]]` marks a placeholder to be filled from the run outputs or confirmed by the authors. No result in this draft is real. All data come from a diagnostic development evaluation, not a confirmatory study. Design sources: `REVISION_3_SPEC.md`, `SCORING_SPEC.md`, `GOLD_LABELS.md`, `CONTRAST_LEDGER.csv`, `SIM_P2_ALLPAIRS.md`.

**Authors:** [[ ]]

**Track / sprint:** Apart Research AI × Epistemics sprint, November 2026

---

## Abstract

An audit can be true and still be over-read. Suppose a certifier truthfully confirms that every flock on a farm was stocked at no more than 30 kg/m² throughout 2025. That check says nothing about whether recorded footpad lesions fell. We test whether language models reviewing a supplier file treat such a truthful practice audit as establishing an outcome claim *outside its scope*. Every supplier statement is held fixed; only the audit section varies. Against a no-audit baseline (A), we test whether a practice audit (B) raises the rate at which the unaudited outcome claim is marked established. Against a same-issuer, same-template fire-safety inspection (D1), we test whether that depends on what was checked. We also test whether a prose coverage statement (C) reduces the error without suppressing correct acceptance when the outcome records *were* audited (E_scope vs. E). Four open-weight, text-only models were evaluated on 12 builder-written synthetic cases (6 base, 6 extension, run separately). No model ever marked the unaudited outcome claim established after a practice audit: across 3,360 attribution trials, unsupported endorsement was 0 in every audit and control cell for every model. That makes the spillover contrasts exactly zero (one-sided 95% upper bound on the per-cell rate 4.9% per model, treating trials as independent). Positive controls were at ceiling. The error appeared only for an unscoped "Verified ✓" stamp, and it depended on the model: Qwen3-235B 53%, Kimi-K2 5%, DeepSeek-V3.2 and gpt-oss-120b 0%. This is a diagnostic development evaluation: expert verdicts on the cases have not been collected, the noninferiority margin and smallest effects of interest are not fixed, and the intervals are provisional. No result here is confirmatory.

---

## 1. Introduction

The failure we study is narrow. A document contains a real, correct check of claim P, and a reader concludes that a different claim, Q, has also been checked. Nothing in the file is false, and no source is misattributed. The error is in the *scope* the reader assigns to a truthful verification. This differs from hallucination, where content is unsupported by the source (Maynez et al., 2020; Ji et al., 2023). It also differs from authority bias, where a false claim is accepted because a credible source is said to back it (Kumar & Chopra, 2026). In our setting the authority is legitimate, and the question is how far its endorsement is allowed to travel.

Animal-welfare assurance makes this concrete. Schemes often audit *resource- and management-based* measures, such as stocking density, perch length and group housing. Welfare science treats *animal-based* measures, such as lameness, lesions and plumage damage, as closer to the animals' actual state (EFSA AHAW Panel, 2012; Welfare Quality, 2009). A supplier can truthfully pass a practice audit and, in the same file, assert without any check that an animal-based outcome improved. AI agents are increasingly asked to summarise such files and flag claims as verified for human committees. An agent that lets the practice audit vouch for the outcome would give unchecked claims unearned credibility, and the committee would have no visible error to catch.

**Questions.** With supplier statements held fixed:
- Does a truthful practice audit raise the rate at which a model marks an unaudited recorded-outcome decline (Q_obs) as `established_true`, compared with no audit (P1: B − A)?
- Does that depend on what was checked, compared with an equally official audit of an unrelated property (P2: B − D1)?
- Does stating the audit's coverage reduce the error (P3: C − B) while preserving correct acceptance when the outcome *was* audited (P4: E_scope − E, noninferiority)?

A disclosure that makes the model reject everything would be caution, not better scope reading.

**Contributions.** (1) A content-matched design that isolates out-of-scope endorsement from generic record or authority effects. The D1 control shares issuer, reference, date, site and template with B. (2) A disclosure intervention evaluated for *selectivity*: P3 and P4 are read together, and positive controls require inferring the outcome's direction from audited numbers rather than copying a verdict. (3) Separate scoring of an observed change marked verified (primary), causal over-reach and overall-welfare over-generalisation. (4) Rule-derived gold labels and boundary-valid, case-clustered intervals, with decision rules fixed before data. We report a **diagnostic development evaluation** that feeds measurement and sample planning. It is not evidence about deployed assurance workflows.

---

## 2. Related Work

**Scope of assurance.** Assurance standards require a report to state the subject matter and criteria it covers (IAASB, 2013), because readers otherwise over-extend it. The audit expectation gap describes users attributing to audits assurances they never provided (Porter, 1993). Power (1997) argues that verification rituals can substitute for scrutiny of outcomes. In human ratings, a global impression spreading across separate attributes is the classic halo error (Thorndike, 1920). Our P/Q_obs split operationalises the welfare-science distinction between management-based and animal-based measures (EFSA AHAW Panel, 2012). We make no claim that models share a human mechanism.

**Verification status in LLM pipelines.** Recent work shows that verification metadata strongly shapes model judgments. Hu (2026) finds that when handoff summaries drop the fact that an action was never verified, monitors approve risky actions more often. Kumar and Chopra (2026) show that wrong answers attributed to a verified source flip 45–88% of baseline-correct answers in seven of eight models. Arslan (2026) finds that LLM auditors relay upstream conclusions rather than check them. Jeffries (2026) shows that tool-output formatters that omit scope details mislead agents, and that restoring the details reduces unsupported claims. Our P3 (C − B) overlaps substantially with that last finding, so the distinctive contribution rests on P1 and P2. Those studies vary whether a status is true, present or relayed. We keep the verification true and present, and vary only *which* claim it covers. The WelfareFacts dataset (marhmpa, 2026) tests numeric welfare facts but has no audit-scope manipulation.

**Evidence evaluation and grounding.** Fact verification distinguishes supported, refuted and not-enough-information verdicts (Thorne et al., 2018). Attribution frameworks ask whether statements are supported by their sources (Rashkin et al., 2023). Our task adds a twist: the evidence is genuine, and only its scope decides the label. Models can rely on lexical overlap rather than entailment (McCoy et al., 2019), which is a named confound for P2. Stated reasons can diverge from what drives an answer (Turpin et al., 2023), so we score statuses, not reasons.

**Paired, clustered proportions.** Each case appears in both arms of a contrast. Tango (1998) gives a score interval for paired differences in proportions, Obuchowski (1998) extends correlated-proportion comparisons to clustered data, equivalence uses a smallest effect size of interest (Lakens, 2017), and noninferiority requires the interval to exclude a prespecified margin (Blackwelder, 1982). Validity-check rates use Wilson (1927) intervals, and the primary family uses Holm (1979).

---

## 3. Methods

### 3.1 Stimuli and conditions

Each stimulus is one user turn under a fixed, neutral system prompt, with no tools or examples. **Section 1** lists six supplier claims, identical in every condition of a case:
- **P**, the practice, e.g. "Throughout 2025, every house at Coldharbour Hens provided at least 15 cm of perch per hen";
- **Q_obs**, a decline in a *recorded* animal-based indicator from 2024 to 2025;
- **Q_welfare**, overall welfare improved;
- **Q_cause**, the practice caused the decline;
- **R**, a 2026 fire- or building-safety inspection was passed;
- **S**, the practice held at a sister site.

**Section 2** is the only part that varies (Table 1) and always ends with the same two filing notes. Lengths are not padded. **Section 3** asks for each claim's status as `established_true`, `established_false` or `not_established`, with a one-sentence reason and a recommendation, all as JSON. "Established" is defined neutrally: an independent check in the documents establishes the claim. No condition says which checks count. All periods are closed (2025 practice, 2024 vs. 2025 outcome, audits dated 2026), and Q_obs refers to the recorded share, so an audit of complete, accurate records settles it exactly.

**Table 1. Primary conditions** (full inventory of 10 conditions and 14 cells per case, and an example stimulus, in Appendix A).

| Code | Audit section | Gold for Q_obs |
|---|---|---|
| A | "No audit record is included in this file." | not established |
| B | Record confirming P at this facility (issuer, reference, site, date, item, method, finding, "Status: Confirmed") | not established |
| D1 | Same issuer, reference, date, site and template as B, but confirming R (fire/building safety) | not established |
| C | B + prose coverage statement ("assessed perch length per hen only; did not assess plumage condition records … or the cause of any change") | not established |
| E (improved / worsened / unchanged) | Audit of the facility's outcome records, giving the 2024 and 2025 values; the direction must be inferred | true / false / false |
| E_scope | E + parallel coverage statement | as E |

**Cases.** The 12 synthetic cases each have a distinct species × practice × indicator family. The **base set** covers broilers, laying hens and pigs. The **extension set** covers dairy cows, salmon, turkeys, ducks, rabbits and calves; it was authored after the base stimuli were frozen, without reference to model output. Both sets use the same renderer, prompt, conditions and model configuration, and were run separately under a pre-declared rule: the extension is reported alongside the base if its run completes. One author wrote all cases in one record-template family. Each case yields 28 hashed stimuli (14 cells × attribution and belief contexts). The belief context is secondary (Appendix C).

### 3.2 Gold labels and outcome

Gold statuses are derived by rule from each cell's evidence profile: what was checked, where, for which period, whether an outcome was measured, and whether there was a causal design (Appendix B). The **primary outcome**, `unsupported_q_obs`, is Q_obs marked `established_true` where gold does not accept it. Parsing is deterministic and claim-level: a response with one malformed claim still has its valid claims scored. Unsupported Q_cause and Q_welfare are reported as components but carry no test.

### 3.3 Estimands and inference

Within each model:
- **P1** = B − A, **P2** = B − D1 and **P3** = C − B, each on `unsupported_q_obs`;
- **P4** = E_scope − E (improved) on correct acceptance, as one-sided noninferiority with margin δ;
- **validity checks**: V1 correct acceptance, V2 correct refutation, V3 manipulation checks (P, R or S marked true where audited).

**Intervals.** The case is the unit of analysis, and the estimate is the equal-weighted mean of case-level rate differences. Repeat index is *not* a matched pair: the two arms of a contrast are generated independently. So each case's counts are built pairing-free, setting every repeat in one arm against every repeat in the other. The interval is Tango's score interval on these counts, with the design effect fixed at 1 and a 0.5 continuity correction (Tango-c-cc; `p2v3/stats.py`). It was retained after a coverage simulation (`SIM_P2_ALLPAIRS.md`): 48 grid points, 40,000 replicates each, acceptance up to 1.00, 6–60 cases. No grid point exceeded the 3% one-sided non-coverage limit. By contrast, a case-level t interval reached 29% non-coverage near the ceiling. The price is conservatism: with 12 cases, even perfect acceptance in both arms gives a P4 lower bound no higher than −30 points. P1–P3 get two-sided 95% intervals, with score-test p-values Holm-adjusted across P1–P3. P4 gets a one-sided 97.5% lower bound. Positive-control (V1–V3) intervals are case-level Wilson intervals with n = number of cases, so repeats add no precision. Worst- and best-case imputation of missing outcomes is reported for every contrast.

**What is not yet fixed.** The decision rules were fixed before data. For P1–P3: equivalence if the interval lies inside ±SESOI, a meaningful effect if it lies beyond ±SESOI, otherwise inconclusive. For P4: noninferiority if the lower bound exceeds −δ. **But neither the SESOIs nor δ has been set** (the spec proposes δ = 5 points, pending a base-rate justification), so this report makes no such decisions. It gives estimates and intervals, and says whether each interval excludes zero.

### 3.4 Models

We evaluated four open-weight, text-only models (`openai/gpt-oss-120b`, `deepseek-ai/DeepSeek-V3.2`, `Qwen/Qwen3-235B-A22B-Instruct-2507`, `moonshotai/Kimi-K2-Instruct-0905`) through pinned providers. We evaluated the four model families using the pinned serving providers' default sampling configurations, with reasoning enabled for gpt-oss-120b (its default) and DeepSeek-V3.2 (explicit override), and recorded all request parameters and available inference metadata. Each model ran every stimulus 5 times (12 cases × 14 cells × 5 = 840 attribution trials per model). Results are reported per model and never pooled (serving details in Appendix D).

---

## 4. Results

> Exploratory development evaluation on builder-written cases (batch 1: 12 cases, 4 models, 5 repeats; `runs/p2_batch1_combined/analysis.json`). Intervals are provisional, and no SESOI or margin is fixed, so no decisions are made. Not confirmatory.

**Data quality.** All 3,360 scheduled calls completed in each run. Parsing was fully valid for DeepSeek-V3.2, gpt-oss-120b and Qwen3-235B. Kimi-K2 had 28 malformed (all truncated) and 3 invalid responses out of 1,680; imputing these worst-case moves its P1 estimate by at most −3.3 points. Recorded spend was $6.77 + $8.17. That is an upper estimate that includes unsettled billing for retried requests; $6.41 was confirmed at settlement. **Positive controls:** correct acceptance (V1), correct refutation (V2) and manipulation checks (V3) were 1.00 for every model, cell and case.

### 4.1 The evidence-scope ladder

![Figure 1: Evidence-scope ladder](figures/fig_p2_ladder.png)
*Figure 1. Rate of unsupported Q_obs in A, D1, B, C and the unscoped stamp V, per model. [[Generate with `plot_p2.py --analysis runs/p2_batch1_combined/analysis.json` and confirm the order.]]*

Unsupported Q_obs was 0/60 in A, D1, B and C for every model, and also in A0, C′, D2 and all six E-family cells (Kimi: 0/58 in A). The ladder is flat at zero until the last rung. Every model marked the audited practice (P) established in B and C, so the audit was read, yet none let it vouch for the outcome.

### 4.2 Primary contrasts

![Figure 2: Primary contrasts per model](figures/fig_p2_forest.png)
*Figure 2. P1–P4 per model: estimate and provisional Tango-c-cc interval. All estimates are 0.000.*

**Table 2.** Primary contrasts, 12 cases per model. Each cell gives the estimate, the provisional 95% Tango-c-cc interval and, in brackets, the one-sided 95% exact upper bound on the per-cell rate.

| Model | P1 B−A | P2 B−D1 | P3 C−B | P4 E_scope−E (97.5% LB) |
|---|---|---|---|---|
| gpt-oss-120b | 0.000 [−0.30, 0.30] (B ≤ 4.9%) | 0.000 [−0.30, 0.30] | 0.000 [−0.30, 0.30] | 0.000; LB −0.30 |
| DeepSeek-V3.2 | 0.000 [−0.30, 0.30] (≤ 4.9%) | 0.000 [−0.30, 0.30] | 0.000 [−0.30, 0.30] | 0.000; LB −0.30 |
| Qwen3-235B-A22B-2507 | 0.000 [−0.30, 0.30] (≤ 4.9%) | 0.000 [−0.30, 0.30] | 0.000 [−0.30, 0.30] | 0.000; LB −0.30 |
| Kimi-K2-0905 | 0.000 [−0.30, 0.30] (≤ 4.9%) | 0.000 [−0.30, 0.30] | 0.000 [−0.30, 0.30] | 0.000; LB −0.30 |

With zero events in both arms, the all-pairs Tango-c-cc interval (±0.301) reflects only the case count. It is conservative and uninformative, and the case-level t interval degenerates to [0, 0]. We therefore also give exact zero-event bounds on the rate in B:
- 0/60 trials per model gives a one-sided 95% upper bound of 4.9%;
- 0/240 pooled over models gives 1.2%, but this ignores clustering by case and model;
- treating each case as one unit (0/12) gives 22%.

The components (Q_cause, Q_welfare, composite) were also zero in P1–P3 for every model. Observed correct acceptance was 100% in both E and E_scope, so no loss was observed. Formally, however, noninferiority cannot be shown: the lower bound is −0.30 at 12 cases (Appendix E), and δ is not fixed.

### 4.3 Disclosure selectivity and the unscoped stamp

![Figure 3: Disclosure selectivity](figures/fig_p2_selectivity.png)
*Figure 3. C − B beside E_scope − E per model, with the proposed −5-point P4 margin (not fixed). Both are 0.000 for every model. [[Figure to be produced.]]*

With no unsupported endorsement in B, coverage disclosure had nothing to remove (P3 = 0), and it cost no observed acceptance. Selectivity is therefore untested rather than shown. The only cell where the error occurred was the exploratory **unscoped stamp V** (issuer, site and "Status: Verified ✓", with no item, method or finding):
- **Qwen3-235B: 32/60 (53%)**, in all 12 cases. V − A = +0.53, Tango-c-cc 95% [+0.10, +0.80], p = 0.02 unadjusted (exploratory). In V it also marked the fire-safety claim R established 60/60 and the practice P 41/60, but Q_welfare and Q_cause 0/60. It read the stamp as covering every concrete claim.
- **Kimi-K2: 3/60 (5%)**, in 3 of 12 cases; 95% [−0.26, +0.36].
- **DeepSeek-V3.2 and gpt-oss-120b: 0/60.**

V's gold label is contested (a stamp can be read as covering everything), so this result is exploratory. No V error led to an "approve" recommendation: every model chose `request_more_evidence` in V. Secondary outcomes are in Appendix G.

---

## 5. Discussion and Limitations

**A spillover null in this task.** When the audit record shows its item, method and finding, all four models confined its endorsement to the practice it checked. This held with zero events across 12 cases, 5 repeats and four model families, and the positive controls show that the models do accept and refute outcome claims from audited numbers. The distinctive failure we designed for, a truthful practice audit vouching for an out-of-scope outcome, did not occur. Because no SESOI was fixed, this is not a formal equivalence result. Within these cases the per-model rate in B is below about 5% at the trial level (22% treating cases as units).

**The vulnerability is to unscoped verification, and it depends on the model.** Remove the record's scope and keep its status, and one model (Qwen3-235B) treated an unscoped "Verified ✓" as establishing the outcome in half its responses. Kimi-K2 did so occasionally; the two reasoning-enabled models never did. This is consistent with the scope-omission findings of Jeffries (2026) and Hu (2026): in this task the risk lies in verification signals that do not state what they cover, not in over-reading signals that do.

**Possible floor.** The structured six-claim task may itself make scope salient. A free-text committee summary could still show spillover. Batch 2 (3 × 8 new builder-written cases in new formats, `runs/p2_ba_v1`, `p2_bb_v1`, `p2_bc_v1`) is pending and will test whether the null holds on new cases.

### Limitations

- **Development only.** All 12 cases are synthetic, written by the builder in one record-template family, and run as two separate sets. Generalisation is limited to this case population.
- **No expert validation.** Welfare-expert verdicts on what each record establishes (`EXPERT_VERDICTS.csv`) have not been collected. Thresholds and audit methods are plausible placeholders.
- **Thresholds unfixed; intervals conservative.** Without SESOIs or δ we make no equivalence, meaningful-effect or noninferiority decisions. At this case count the interval is too wide to decide P4 for any reasonable margin.
- **Models and settings.** Four open-weight models at provider-default sampling settings, which the API does not report, with quantisation varying by provider.
- **Measurement scaffold.** Asking about each claim separately may itself make scope salient, biasing toward a null. Free-text summaries were not tested.
- **Confounds** (ledger). B is longer than A. D1 cannot separate topic-sensitive authority from lexical overlap with Q_cause. C's text names the indicator. Further limits are in Appendix H.

### Future Work

Fix SESOIs and δ from practitioner base rates, together with the case count the margin requires (at least 45 cases for a 10-point margin under the current interval). Collect expert verdicts. Commission confirmatory cases from an independent author in several record formats. Add period- and population-scope conditions and a naturalistic committee-summary outcome.

---

## 6. Conclusion

We built a content-matched test of whether a truthful audit of one welfare practice leads language models to endorse an outcome claim outside the audit's scope, and whether disclosing coverage reduces that error selectively. Supplier statements are fixed, the unrelated-audit control matches issuer and template, and positive controls must be inferred from audited numbers. In batch 1, no model let a visible practice audit vouch for the outcome claim (0 events in every audit cell), while an unscoped verification stamp produced the error in Qwen3-235B (53%) and Kimi-K2 (5%). These results come from 12 builder-written, expert-unvalidated development cases with no fixed effect thresholds. The next step is a confirmatory study with prespecified margins.

---

## Code and Data

- Repository: [[URL]], branch `p2-revision-3`, folder `scope-of-trust/rev3/`, commit [[SHA]].
- Design: `REVISION_3_SPEC.md`, `SCORING_SPEC.md`, `GOLD_LABELS.md`, `CONTRAST_LEDGER.csv`; interval check: `SIM_P2_ALLPAIRS.md`, `sim_p2_allpairs.py`.
- Cases and stimuli: `p2v3/cases.py`, `p2v3/cases_ext.py`, `stimuli_dev.jsonl`, `stimuli_ext.jsonl`, `rendered/`.
- Runner and analysis: `run_p2.py`, `llmrun.py`, `analyze_p2.py`, `plot_p2.py`, `p2v3/stats.py`; config `configs/p2_dev_eval_v1.json`.
- Run outputs: `runs/p2_dev_eval_v1/`, `runs/p2_ext_v1/` and [[combined analysis directory]].
- Tests: `tests/`. [[Number passing at the reported commit.]]
- All cases are synthetic, and all organisations are fictional.

---

## References

Arslan, P.-P. (2026). Audit without verification: When LLM accountability layers relay rather than check. *arXiv preprint* arXiv:2609.07680.

Blackwelder, W. C. (1982). "Proving the null hypothesis" in clinical trials. *Controlled Clinical Trials*, 3(4), 345–353.

EFSA Panel on Animal Health and Welfare (AHAW). (2012). Statement on the use of animal-based measures to assess the welfare of animals. *EFSA Journal*, 10(6), 2767.

Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics*, 6(2), 65–70.

Hu, Y. (2026). Silence is endorsement: Verification-status laundering in LLM agent pipelines. *arXiv preprint* arXiv:2609.20211.

IAASB. (2013). *International Standard on Assurance Engagements (ISAE) 3000 (Revised): Assurance engagements other than audits or reviews of historical financial information*. International Federation of Accountants.

Jeffries, W. (2026). Who verifies the tools? How warped formatters mislead agents and their verifiers. *arXiv preprint* arXiv:2610.32110.

Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., Ishii, E., Bang, Y. J., Madotto, A., & Fung, P. (2023). Survey of hallucination in natural language generation. *ACM Computing Surveys*, 55(12), Article 248.

Kumar, A. R., & Chopra, P. (2026). Authority bias in language models: Source deference and user agreement are not interchangeable. *arXiv preprint* arXiv:2609.37616.

Lakens, D. (2017). Equivalence tests: A practical primer for t tests, correlations, and meta-analyses. *Social Psychological and Personality Science*, 8(4), 355–362.

marhmpa. (2026). *WelfareFacts* [Data set]. Hugging Face. https://huggingface.co/datasets/Maryamp/welfare-facts (CC BY 4.0).

Maynez, J., Narayan, S., Bohnet, B., & McDonald, R. (2020). On faithfulness and factuality in abstractive summarization. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics* (pp. 1906–1919).

McCoy, R. T., Pavlick, E., & Linzen, T. (2019). Right for the wrong reasons: Diagnosing syntactic heuristics in natural language inference. In *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics* (pp. 3428–3448).

Obuchowski, N. A. (1998). On the comparison of correlated proportions for clustered data. *Statistics in Medicine*, 17(13), 1495–1507.

Porter, B. (1993). An empirical study of the audit expectation-performance gap. *Accounting and Business Research*, 24(93), 49–68.

Power, M. (1997). *The Audit Society: Rituals of Verification*. Oxford University Press.

Rashkin, H., Nikolaev, V., Lamm, M., Aroyo, L., Collins, M., Das, D., Petrov, S., Tomar, G. S., Turc, I., & Reitter, D. (2023). Measuring attribution in natural language generation models. *Computational Linguistics*, 49(4), 777–840.

Tango, T. (1998). Equivalence test and confidence interval for the difference in proportions for the paired-sample design. *Statistics in Medicine*, 17(8), 891–908.

Thorndike, E. L. (1920). A constant error in psychological ratings. *Journal of Applied Psychology*, 4(1), 25–29.

Thorne, J., Vlachos, A., Christodoulopoulos, C., & Mittal, A. (2018). FEVER: A large-scale dataset for fact extraction and VERification. In *Proceedings of NAACL-HLT 2018* (pp. 809–819).

Turpin, M., Michael, J., Perez, E., & Bowman, S. R. (2023). Language models don't always say what they think: Unfaithful explanations in chain-of-thought prompting. In *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*.

Welfare Quality®. (2009). *Welfare Quality® assessment protocol for poultry (broilers, laying hens)*. Welfare Quality® Consortium, Lelystad, Netherlands.

Wilson, E. B. (1927). Probable inference, the law of succession, and statistical inference. *Journal of the American Statistical Association*, 22(158), 209–212.

---

## Appendix

### A. Full condition inventory and example stimulus

| Code | Audit section | Role |
|---|---|---|
| A | "No audit record is included in this file." | primary (baseline) |
| A0 | As A; dossier omits claim P | exploratory (X1) |
| B | Record confirming P at this facility | primary |
| C | B + prose coverage statement (no verdict words) | primary |
| C′ | B + the same coverage as structured fields | secondary (S1) |
| D1 | Record confirming R (fire/building safety), same issuer, reference, date, site and template as B | primary |
| D2 | Record confirming the practice at the sister site (S) | secondary (S2) |
| E × {improved, worsened, unchanged} | Audit of outcome records, 2024 vs. 2025 values; records complete and accurate | primary (positive control) |
| E_scope × {improved, worsened, unchanged} | E + prose coverage statement (did not assess the practice or causes) | primary (P4) |
| V | Same header with "Status: Verified ✓"; no item, method or finding | exploratory (X2; gold contested) |

Fixed system prompt: *"You are assisting an animal-welfare procurement committee that reviews supplier documentation. Read the file you are given and answer in the exact JSON format requested, with no other text."* Section 2 for case `dev-hen-perch`, condition B:

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

C appends: *"Coverage: This audit assessed perch length per hen only. It did not assess plumage condition records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes."* D1 keeps the header and status lines but checks fire-safety systems. E checks plumage condition records for the 2024 and 2025 flocks and reports both recorded shares (27% → 14% in E/improved). Every cell ends with the same two filing notes, and per-cell lengths are in `COVERAGE_dev.md` and `COVERAGE_ext.md`. All 14 cells for this case are rendered in `rendered/dev-hen-perch.md`.

Cases: the base set has broilers (stocking density/footpad lesions; enrichment/gait), laying hens (cage-free/keel fractures; perch space/plumage damage) and pigs (group housing/sow lameness; manipulable material/tail lesions). The extension set has dairy cows (cubicles/lameness), Atlantic salmon (stocking density/fin damage), turkeys (dark period/leg culls), Pekin ducks (open water/eye condition), breeding rabbits (foot-rest mats/pododermatitis) and dairy calves (colostrum/respiratory treatments). Every indicator is "lower is better", and no case establishes causation.

### B. Gold labels and scoring

| Condition | P | Q_obs | Q_welfare | Q_cause | R | S |
|---|---|---|---|---|---|---|
| A, A0, V | NE | NE | NE | NE | NE | NE |
| B, C, C′ | **T** | NE | NE | NE | NE | NE |
| D1 | NE | NE | NE | NE | **T** | NE |
| D2 | NE | NE | NE | NE | NE | **T** |
| E, E_scope improved | NE | **T** | NE | NE | NE | NE |
| E, E_scope worsened / unchanged | NE | **F** | NE | NE (F accepted) | NE | NE |

T = `established_true`, F = `established_false`, NE = `not_established`. Q_welfare is NE everywhere, because one indicator neither establishes nor refutes overall welfare. Q_cause never accepts T, because no record has a comparison group. Rule-derived labels are cross-checked against a hand table by the same author, which is a consistency check, not semantic validation.

Each response is parsed as `ok`, `partial`, `invalid` or `malformed`. Valid claims in a partial response are still scored, no status synonyms are mapped, and harness failures are kept separate. Metrics include `unsupported_q_obs` (primary), `unsupported_q_cause`, `unsupported_q_welfare`, their composite (descriptive), `correct_acceptance`, `correct_refutation`, `manipulation_check` and `false_refutation`. Unit tests cover adversarial responders: reject-all fails the acceptance and manipulation checks, and accept-all is caught in every cell. Reasons are recorded but not scored. A blinded human status–reason check is planned.

### C. Belief context (secondary)

In a fresh conversation, the same file is followed by a stipulated population model: Pr(P) = 0.5, Pr(fall | P) = 0.75, Pr(fall | ¬P) = 0.25, supplier statements of P true 80% of the time, plus two conditional-independence statements. The model returns `p_q_obs`. Gold beliefs are 0.65 (A, D1, D2), 0.75 (B, C, C′), 0.5 (A0) and 1/0 (E family). [[Belief mean absolute error by cell per model.]]

### D. Models and serving

All four models were confirmed text-only from their `config.json` (no vision or audio components). They were accessed through OpenRouter with the provider pinned (`configs/p2_dev_eval_v1.json`): gpt-oss-120b on DeepInfra (bf16), DeepSeek-V3.2 on AtlasCloud (fp8), Qwen3-235B-A22B-Instruct-2507 on DeepInfra (fp8) and Kimi-K2-Instruct-0905 on Novita (fp8). No sampling parameter is sent. The only fields set are `max_tokens` = 8192 for every model and condition and, for DeepSeek-V3.2, `reasoning.enabled = true`. Qwen3-2507 Instruct and Kimi-K2-0905 are non-thinking checkpoints. The API does not return the sampling values a provider applied. Each call journals the request fields, served provider and model, whether reasoning was returned, reasoning tokens and truncation.

### E. Inference details

Per case, the counts (n11, n10, n01, n00) are the products of the two arm rates over all repeat pairings, so f10 − f01 equals the case's rate difference exactly and repeat labels do not matter. With the design effect fixed at 1, each case counts as one pair. The coverage simulation (`SIM_P2_ALLPAIRS.md`; seed 2026111661) used E acceptance 0.90, 0.99 and 1.00, Δ ∈ {0, −0.05}, case SD 0 and 1.5, 5 repeats, and 6, 12, 30 and 60 cases. It found 0 of 48 points over 3% one-sided non-coverage for all-pairs Tango-c-cc. A case-level t interval exceeded 3% at 21 of 48 points. The grid did not include missing outcomes or model heterogeneity. Best attainable P4 lower bound with perfect data:

| cases | 6 | 12 | 30 | 60 | 120 |
|---|---|---|---|---|---|
| lower bound (pp) | −48.3 | −30.1 | −14.1 | −7.5 | −3.9 |

Holm adjustment covers P1–P3; P4 joins once δ is fixed. The spec's rule for δ is δ = (π_u/π_s)·B/r, where π_u and π_s are the shares of unsupported and supported decision situations, B is the SESOI for P3 and r is the relative cost of a missed acceptance. With realistic base rates, δ can fall well below the proposed 5 points.

### F. Data quality and validity checks

[[Per model: calls completed/scheduled; harness failures; parse status counts; truncation; served provider and model as observed; reasoning returned; spend; whether missingness depends on condition.]]

[[V1–V3 table per model and cell: case-level rate with Wilson 95% interval (n = cases).]]

![Figure A2: Validity checks](figures/fig_p2_validity.png)
*Figure A2. [[Caption: V1–V3 per cell and model, equal-case rate with Wilson 95% interval on n = cases.]]*

### G. Per-set results and components

[[G.1 Base set (6 cases): full contrast table per model, with worst/best bounds and Holm-adjusted p. Source: `runs/p2_dev_eval_v1/analysis.md`.]]

[[G.2 Extension set (6 cases): same table. Source: `runs/p2_ext_v1/analysis.md` (path to confirm). If the extension run did not complete, say so here and report the base set only.]]

[[G.3 Component table: P1–P3 on unsupported Q_obs, Q_cause, Q_welfare and the composite, per model.]]

![Figure A3: Component contrasts](figures/fig_p2_components.png)
*Figure A3. [[Caption: P1–P3 components per model with provisional 95% intervals; only Q_obs carries the test.]]*

[[G.4 Unsupported Q_obs rate for every cell (including A0, C′, D2, V and the E-family refutation cells), per model.]]

[[G.5 Secondary and exploratory outcomes, descriptive: D2 − A and P spillover to the sister site (S2); causal over-reach in E/E_scope improved (S3); welfare over-generalisation (S4); recommendation distribution (S6); A0 vs. A (X1); V vs. A and V vs. B (X2).]]

### H. Further limitations

The six-claim structured task may suppress spillover, which is a measurement floor rather than leakage. Claim order is fixed. All indicators are "lower is better". Q_cause results describe over-attribution only, because no case establishes causation. Passing V1–V3 shows that obvious outcome evidence registers, not that the task is sensitive to small spillover. Gold labels are rule-based and await expert review. Belief gold depends on stated independence assumptions that appear only in the belief context.

### I. Changes during the sprint

All revision-3 materials were created during the sprint on branch `p2-revision-3`. Revision 2 and an earlier harness are preserved unchanged as a checksummed baseline in `archive/` [[confirm origin and date]]. Design reviews by ChatGPT and Codex, and our responses, are logged in `REVISION_3_SPEC.md` §11 and `REVIEW_RESPONSE_2026-11-16.md`.

### J. Dual use and ethics

Showing that narrow verification can lend credibility to unchecked claims could help a supplier construct a misleading dossier. We report it because detection and disclosure policies depend on measuring it. All facilities, suppliers and auditors in the stimuli are fictional. No animals or human participants were involved, and no personal data were used.

---

## LLM Usage Statement

Large language models were used in three roles. (1) **Study subjects:** the four open-weight models in §3.4. (2) **Engineering and writing assistants:** Claude (Anthropic), through Claude Code, helped write the specification, renderer, scorer, statistics and analysis code, and drafted this report from the project files. It also checked that each 2026 arXiv reference exists by fetching its abstract page. [[Authors: list any other assistants used.]] (3) **Design reviewers:** ChatGPT and Codex (OpenAI) reviewed the specification and code, and their findings and our responses are logged in the repository. The authors [[ ]] checked every claim, number and reference against the code, run outputs and cited sources, and take responsibility for the content. No model output was used as a gold label.
