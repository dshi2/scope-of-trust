# The Scope of Trust: Does a Truthful Practice Audit Make LLMs Treat an Unaudited Outcome Claim as Verified?

> **Draft status (delete before submission).** Every `[[...]]` marks a placeholder to be filled from the run outputs or confirmed by the authors. No result in this draft is real. All data are from a diagnostic development evaluation, not a confirmatory study. Source of truth for design: `REVISION_3_SPEC.md`, `SCORING_SPEC.md`, `GOLD_LABELS.md`, `CONTRAST_LEDGER.csv`.

**Authors:** [[ ]]

**Track / sprint:** Apart Research AI × Epistemics sprint, November 2026

---

## Abstract

AI agents increasingly read supplier documentation and audit records on behalf of procurement and assurance committees. An audit that truthfully confirms a narrow housing practice ("every flock was stocked at no more than 30 kg/m² throughout 2025") says nothing about whether an animal-based outcome changed. We ask whether such an audit nonetheless makes language models mark an unaudited outcome claim (Q_obs: "the recorded share of birds with footpad lesions was lower in 2025 than in 2024") as *established*, holding every supplier statement fixed. A content-matched design separates three readings: spillover from the verified practice (B vs. no audit, A), dependence on the checked topic (B vs. a same-template fire-safety inspection, D1), and the effect of a prose coverage statement (C vs. B). That last contrast is paired with a noninferiority check that coverage statements do not suppress correct acceptance when the outcome *was* audited (E_scope vs. E). Gold labels follow from rule-based evidence profiles. We report a diagnostic development evaluation of four open-weight, text-only models on 12 builder-written synthetic cases (6 base and 6 extension, run separately). [[One to two sentences: P1 B−A, P2 B−D1, P3 C−B direction and per-model range of estimates with provisional 95% intervals; P4 lower bounds; whether V1–V3 positive controls behaved as expected.]] Expert verdicts on the cases have not been collected, the noninferiority margin and smallest effects of interest are not yet fixed, and intervals are provisional. These results are for development only and do not support confirmatory claims.

---

## 1. Introduction

Assurance only helps if its readers take a check to cover what it checked and nothing more. Those readers are increasingly AI agents that summarise supplier files, flag claims as verified and draft recommendations for human committees. Animal-welfare assurance makes the risk concrete. Many schemes audit *resource- and management-based* measures, such as stocking density, perch length or group housing, because these are cheap to verify. Welfare science treats *animal-based* measures (lameness, lesions, plumage damage) as closer to the animals' actual state (EFSA AHAW Panel, 2012; Welfare Quality, 2009). A supplier can truthfully pass a practice audit and also assert, without any check, that an animal-based outcome improved. If an agent reads the passed audit as if it vouched for the outcome, unchecked claims gain unearned credibility. Agents are being asked to evaluate this kind of file.

**Main question.** Holding the supplier statements fixed, does adding a truthful audit of a housing practice (P) increase the probability that a model marks an unaudited recorded-outcome decline (Q_obs) as `established_true`? We compare it with (A) the same file with no audit record and (D1) a successful audit of an unrelated property (fire or building safety) from the same issuer, with the same reference, date, site and template.

**Intervention question.** Does stating the audit's coverage in prose ("This audit assessed perch length per hen only. It did not assess plumage condition records …") reduce that error (C vs. B)? And does it do so *without* suppressing correct acceptance when the outcome records were the thing audited (E_scope vs. E)? Lower acceptance alone is not success: a disclosure that makes the model reject everything is caution, not better scope reading.

**Contributions.**
1. A content-matched design in which supplier assertions are identical across conditions and only the audit section varies. It separates *practice-to-outcome spillover* (B > A), *dependence on what was checked* (B > D1) and *a generic effect of any official record* (B ≈ D1 > A).
2. A coverage-disclosure intervention that is evaluated for *selectivity*: P3 (C − B) is paired with a one-sided noninferiority test on correct acceptance (P4). Positive controls require the model to infer an outcome's direction from audited numbers rather than copy a verdict.
3. Separate scoring of three distinct over-reach errors: an observed change marked verified (Q_obs, primary), causal improvement (Q_cause) and overall welfare improvement from one indicator (Q_welfare).
4. Rule-derived gold labels, a deterministic scorer with adversarial tests, and boundary-aware paired, case-clustered inference with informative-null rules fixed before data.

We report a **diagnostic development evaluation** on builder-written synthetic cases not yet checked by a welfare expert: inputs to measurement and sample planning, not evidence about deployed assurance workflows.

---

## 2. Related Work

**Audit, assurance and the scope of verification claims.** Assurance standards require a report to identify the subject matter and criteria it covers (IAASB, 2013), and the "audit expectation gap" literature documents users attributing to audits assurances they do not provide (Porter, 1993). Power (1997) argues that verification rituals can stand in for scrutiny of outcomes; Lyon and Maxwell (2011) model selective disclosure under threat of audit. In farm-animal welfare, the distinction between resource/management-based and animal-based measures is central to assessment protocols (Blokhuis et al., 2010; EFSA AHAW Panel, 2012; Welfare Quality, 2009). Our P/Q_obs split operationalises exactly that distinction. In human judgment, global impressions spilling across separate attributes (Thorndike, 1920) and the substitution of an easy question for a hard one (Kahneman & Frederick, 2002) predict the error we test for. We make no claim that models share the human mechanism.

**LLM evidence evaluation and over-attribution.** Fact-verification benchmarks separate supported, refuted and not-enough-information verdicts (Thorne et al., 2018). Our three statuses mirror that, but the evidence is a document whose *scope* determines the label. Attribution frameworks ask whether generated statements are supported by cited sources (Rashkin et al., 2023; Gao et al., 2023). Audits of generative search find that many statements are not fully supported by their citations (Liu et al., 2023). Models can be distracted by irrelevant context (Shi et al., 2023), can exploit lexical overlap rather than entailment (McCoy et al., 2019), and shift answers toward perceived user or authority preferences (Sharma et al., 2024). Lexical overlap between the audited practice and the causal claim is a confound we name for P2 and cannot remove in this design. [[AUTHORS TO VERIFY AND ADD, or delete: concurrent 2026 work identified in the project's novelty check (`../NOVELTY_GATE_FINAL.md`): "Silence Is Endorsement" (arXiv 2609.20211), "Authority Bias" (arXiv 2609.37616), "Who Verifies the Tools?" (arXiv 2610.32110 / NeurIPS 2026), "Audit Without Verification" (arXiv 2609.07680), and the WelfareFacts dataset (Hugging Face `Maryamp/welfare-facts`). Each must be checked against its arXiv/Hugging Face page and given a full reference before it is cited. If kept, state that C − B overlaps substantially with "Who Verifies the Tools?" and that the contribution rests on B − A and B − D1.]]

**Faithfulness and grounding.** Hallucination and faithfulness research distinguishes content supported by a source from content that merely sounds consistent with it (Maynez et al., 2020; Ji et al., 2023). Atomic-fact evaluation scores support claim by claim (Min et al., 2023), as our per-claim statuses do. Models' stated reasons can diverge from the factors that drive their answers (Turpin et al., 2023). For that reason we score statuses, not reasons, and plan a blinded human check of status–reason consistency before any confirmatory freeze.

**Paired-proportion and noninferiority statistics.** Each case is seen in both arms of a contrast, so contrasts are differences of paired proportions (McNemar, 1947). Tango (1998) gives a score-based interval and equivalence test for this design. Newcombe (1998) compares interval methods for paired differences, and Wald intervals perform poorly near 0 and 1. Obuchowski (1998) extends the comparison of correlated proportions to clustered data, which here means repeated responses within a case. Equivalence is tested by two one-sided tests against a smallest effect size of interest (Schuirmann, 1987; Lakens, 2017). Noninferiority asks whether an interval excludes a prespecified margin, and a nonsignificant difference is not evidence of equivalence (Blackwelder, 1982). Validity-check rates use Wilson (1927) intervals, and multiplicity across the primary family uses Holm (1979).

---

## 3. Methods

### 3.1 Task and stimuli

Each stimulus is a single user turn under a fixed system prompt ("You are assisting an animal-welfare procurement committee that reviews supplier documentation…"). No tools, examples or prior turns are included. The file has three sections:

- **Section 1: supplier statements**, identical in every condition of a case, with six labelled claims: **P**, the practice ("Throughout 2025, every house at Coldharbour Hens provided at least 15 cm of perch per hen."); **Q_obs**, an observed decline in a *recorded* animal-based indicator from 2024 to 2025; **Q_welfare**, overall welfare improved; **Q_cause**, the decline was caused by the practice; **R**, the facility passed a 2026 fire- or building-safety inspection; and **S**, the practice also held at a named sister site.
- **Section 2: audit records**, the only part that varies (Table 1). Each cell ends with the same two meeting-logistics filing notes. Lengths are not padded, so length differences equal the treatment content; per-cell lengths are in `COVERAGE_dev.md` and `COVERAGE_ext.md`.
- **Section 3: task.** For each claim, the model returns `established_true`, `established_false` or `not_established`, with a one-sentence reason, plus a recommendation (`approve`, `request_more_evidence`, `reject`), as JSON. "Established" is defined neutrally ("the documents include an independent check whose findings establish the claim"). Neither the system prompt nor the task says which checks count, and no condition carries a scope rule.

All periods are closed: claims compare 2024 with 2025, practice claims say "Throughout 2025", practice audits review records for all of 2025, and every audit is dated 2026. Q_obs concerns the *recorded* share, so an audit confirming that the records are complete and accurate settles it exactly. Unit tests enforce these conventions.

**Table 1. Conditions (Section 2 only; 10 conditions, 14 cells per case).**

| Code | Audit section | Role |
|---|---|---|
| A | "No audit record is included in this file." | primary (baseline) |
| A0 | As A; dossier omits claim P | exploratory |
| B | Record confirming P at this facility (issuer, reference, site, date, item checked, method, finding, "Status: Confirmed") | primary |
| C | B + prose coverage statement (what was and was not assessed; no verdict words) | primary |
| C′ | B + the same coverage as structured fields | secondary |
| D1 | Record confirming R (fire/building safety), same issuer, reference, date, site and template as B | primary |
| D2 | Record confirming the practice at the sister site (S) | secondary |
| E × {improved, worsened, unchanged} | Record of the facility's outcome records: indicator values for 2024 and 2025, records complete and accurate; direction must be inferred from the numbers | primary (positive control) |
| E_scope × {improved, worsened, unchanged} | E + prose coverage statement (did not assess the practice or causes) | primary (P4) |
| V | Same header with "Status: Verified ✓"; no item, method or finding | exploratory |

**Cases.** A case is a facility × practice × indicator × numbers scenario. The **base set** has six cases: broilers (stocking density/footpad lesions; enrichment/gait), laying hens (cage-free/keel fractures; perch space/plumage damage) and pigs (sow group housing/lameness; manipulable material/tail lesions). The **extension set** has six further cases, each its own species × practice × indicator × outcome-audit-method family: dairy cows (cubicle ratio/lameness), Atlantic salmon (stocking density/fin damage), turkeys (dark period/leg-disorder culls), Pekin ducks (open water/eye condition), breeding rabbits (foot-rest mats/pododermatitis) and dairy calves (colostrum feeding/respiratory treatments). The extension set was authored after the base stimuli were frozen, without reference to any model output. It is rendered by the same code with the same prompt, task, conditions and model configuration, and run separately. Pre-declared rule: if the extension run completes, it is reported alongside the base run. All 12 cases are synthetic and fictional, written by one author in one record-template family. Every indicator is "lower is better", and no case establishes causation. Each case contributes 14 cells × 2 contexts = 28 stimuli (168 per set), each stored with its SHA-256 hash, and the hash is re-checked before every call.

**Belief context (secondary).** In a fresh conversation, the same file is followed by a stipulated population model (Pr(P) = 0.5; Pr(fall | P) = 0.75; Pr(fall | ¬P) = 0.25; supplier statements of P true 80% of the time; two conditional-independence statements). The model returns `p_q_obs`. Gold beliefs are 0.65 (A, D1, D2), 0.75 (B, C, C′), 0.5 (A0), and 1 or 0 in the E family. The belief context never shares a conversation with the attribution context.

### 3.2 Gold labels and scoring

Each cell has an evidence profile: which proposition the record checked, at which site, for which period, whether an outcome was measured and in which direction, and whether there is a causal design. Gold statuses are derived from the profile by rule and cross-checked against an independently written hand table, though by the same author, so this is a consistency check, not semantic validation. The key labels: Q_obs is `not_established` everywhere except the E family, where it is `established_true` (improved) or `established_false` (worsened, unchanged). P is `established_true` only in B, C and C′. Q_welfare is `not_established` in every cell, because one indicator neither establishes nor refutes overall welfare. Q_cause never accepts `established_true`, since no record has a comparison group. In E-worsened and E-unchanged, Q_cause also accepts `established_false`, because its presupposed reduction did not occur.

Parsing is deterministic. A response is `ok`, `partial` (some valid claims; each valid claim is still scored), `invalid` or `malformed`. No status synonyms are mapped, and transport failures, timeouts and refusals are harness statuses, kept separate from parse status. Per-trial metrics include:
- **`unsupported_q_obs`**, the **primary outcome**: Q_obs marked `established_true` where gold does not accept it;
- `unsupported_q_cause`, `unsupported_q_welfare` and their composite with Q_obs (descriptive);
- `correct_acceptance` (Q_obs true in E/E_scope improved);
- `correct_refutation` (Q_obs false in worsened/unchanged);
- `manipulation_check` (P true in B/C/C′, R in D1, S in D2);
- `false_refutation`;
- belief absolute error.

Adversarial responders are unit tests: reject-all fails acceptance and manipulation checks, so blanket scepticism is never scored as success; accept-all is caught in every cell. Reasons are recorded but not scored.

### 3.3 Estimands and inference

**Primary family** (`CONTRAST_LEDGER.csv`), each estimated within model:
- **P1** B − A on `unsupported_q_obs`;
- **P2** B − D1 on `unsupported_q_obs`;
- **P3** C − B on `unsupported_q_obs`;
- **P4** E_scope − E (improved) on `correct_acceptance`, one-sided noninferiority with margin δ.

**Validity checks** V1 (correct acceptance), V2 (correct refutation) and V3 (manipulation checks) must hold before any contrast is interpreted. Because no numeric floor was fixed before the runs, we report V1–V3 rates and intervals and flag low values; we do not apply a post-hoc threshold. For P1–P3 we also report the Q_cause, Q_welfare and composite components, each with its interval. Only Q_obs carries the test.

**Estimator.** The case is the unit of analysis. Each case's rate difference between the two arms is computed from all pairings of its repeats in the two arms, so repeat labels carry no matching. The estimate is the equal-weighted mean of case-level differences.

**Interval (provisional).** We use Tango's (1998) score interval for paired proportions applied to case-level cell proportions, with the design effect fixed at 1, so repeats never narrow the interval below what one response per case would give, and a continuity correction of 0.5 (`p2v3/stats.py`, variant `tango_c_cc`). Two-sided 95% intervals are reported for P1–P3 and a one-sided 97.5% lower bound for P4. This variant is conservative near 0 and 1, where Wald or bootstrap intervals collapse to zero width when all pairs agree. The coverage simulation that is to qualify a confirmatory method (non-coverage ≤ 3% across a grid of acceptance rates 0.80–1.00, case random-effect SDs, repeats, case counts and missingness) is implemented (`precision.py`) [[confirm status: results not used in this report / summary of qualifying method]]. Score-test p-values against zero are Holm-adjusted across P1–P3 within each model; P4 joins the family once δ is fixed. Every contrast is also recomputed with missing outcomes imputed worst- and best-case (scheduled-denominator bounds).

**Decision rules (fixed before data, not applicable yet).** For P1–P3, an interval entirely inside ±SESOI would mean equivalence. An interval entirely beyond +SESOI or −SESOI would mean a meaningful directional effect. Anything else is inconclusive in magnitude. P4 shows noninferiority only if its lower bound exceeds −δ. B − A equivalence and P4 noninferiority are different inferences and are never interchanged. **Neither the SESOIs nor δ has been fixed.** The spec proposes δ = 5 points, but derives δ from base rates as δ = (π_u/π_s)·B/r, which can be far smaller. So this report makes no equivalence, meaningful-effect or noninferiority decisions. It reports estimates and intervals, and says whether an interval excludes zero.

### 3.4 Models and generation settings

We evaluated four open-weight, text-only models from different families. Each was verified as having no vision or audio components from its `config.json`:
- `openai/gpt-oss-120b` (served by DeepInfra, bf16);
- `deepseek-ai/DeepSeek-V3.2` (AtlasCloud, fp8);
- `Qwen/Qwen3-235B-A22B-Instruct-2507` (DeepInfra, fp8);
- `moonshotai/Kimi-K2-Instruct-0905` (Novita, fp8).

All were accessed through OpenRouter with the provider pinned (`configs/p2_dev_eval_v1.json`). We evaluated the four model families using the pinned serving providers' default sampling configurations, with reasoning enabled for gpt-oss-120b (its default) and DeepSeek-V3.2 (explicit override), and recorded all request parameters and available inference metadata. No sampling parameter is sent. The only request fields set are `max_tokens` = 8192 for every model and condition and, for DeepSeek-V3.2, `reasoning.enabled = true`. Qwen3-235B-2507 Instruct and Kimi-K2-Instruct-0905 are non-thinking checkpoints. The API does not return the sampling values a provider applied, so we state only "provider default generation settings". Every call journals the exact request fields, the served provider and model, whether reasoning text was returned, reasoning-token counts and truncation. Every model runs every stimulus [[R]] times. Results are reported within model and are never pooled across models.

---

## 4. Results

> All numbers below come from a diagnostic development evaluation on builder-written cases. Intervals are provisional, and no SESOI or margin is fixed. None of these results is confirmatory.

### 4.1 Data quality

[[Per model: calls completed / scheduled, harness failures (timeouts, refusals, provider errors), parse status counts (ok / partial / invalid / malformed), truncation count, served provider and model as observed, reasoning returned (yes/no), spend. Source: `runs/p2_dev_eval_v1/analysis.md` (base) and `runs/p2_ext_v1/analysis.md` (path to confirm) (extension), "Calls … Status … Parse … Truncated … Served provider" lines.]]

[[One sentence on whether parse failure or missingness depends on condition (SCORING_SPEC §2), with the cells concerned.]]

### 4.2 Validity checks (V1–V3)

[[Per model: V1 correct acceptance in E/improved and E_scope/improved; V2 correct refutation in E and E_scope worsened/unchanged; V3 manipulation checks in B, C, C′, D1, D2. Equal-case rate with Wilson 95% interval on the number of cases. Source: "Validity / positive controls" tables in analysis.md.]]

[[State plainly any model or cell with low validity rates and that its contrasts are not interpreted; no post-hoc threshold.]]

![Figure 1: Validity checks per model and cell](figures/fig_p2_validity.png)
*Figure 1. [[Caption: V1–V3 rates per cell and model, equal-case rate with Wilson 95% interval over cases.]]*

### 4.3 Unsupported outcome attribution by condition

![Figure 2: Unsupported Q_obs rate by condition and model](figures/fig_p2_ladder.png)
*Figure 2. [[Caption: evidence ladder — rate of `unsupported_q_obs` by condition (E and E_scope split by direction) for each model.]]*

[[Two to three sentences describing the cell-rate pattern per model: baseline A (floor?), B, D1, C, D2, V. Source: "cell | unsupported Q_obs rate | n" table.]]

### 4.4 Primary contrasts

**Table 2. Primary contrasts per model ([[12 cases: base + extension combined, if the extension run completed; otherwise 6 base cases]]). Estimate = equal-case mean difference; 95% CI = provisional Tango score interval (design effect 1, continuity correction 0.5); p = two-sided score test vs. 0, Holm-adjusted across P1–P3; bounds = missing outcomes imputed worst/best.**

| Model | P1 B−A | P2 B−D1 | P3 C−B | P4 E_scope−E (97.5% lower bound) | Cases |
|---|---|---|---|---|---|
| gpt-oss-120b | [[est, 95% CI; p (Holm); bounds]] | [[…]] | [[…]] | [[est; lower bound; bounds]] | [[K]] |
| DeepSeek-V3.2 | [[…]] | [[…]] | [[…]] | [[…]] | [[K]] |
| Qwen3-235B-A22B-2507 | [[…]] | [[…]] | [[…]] | [[…]] | [[K]] |
| Kimi-K2-0905 | [[…]] | [[…]] | [[…]] | [[…]] | [[K]] |

Source: `runs/p2_dev_eval_v1/analysis.md` (base), `runs/p2_ext_v1/analysis.md` (path to confirm), and the combined run written with `analyze_p2.py --run-dir <base> <ext> --out [[combined directory]]`. Base-only and extension-only tables are in Appendix A.

![Figure 3: Primary contrasts per model](figures/fig_p2_forest.png)
*Figure 3. [[Caption: forest plot of P1–P3 estimates with provisional 95% intervals and P4 estimates with one-sided 97.5% lower bounds, per model. No SESOI or δ lines are drawn because none is fixed.]]*

[[P1 B−A per model: estimate, 95% CI — from runs/p2_dev_eval_v1/analysis.md]]

[[P2 B−D1 per model: estimate, 95% CI; whether the pattern looks like B > D1 (topic-dependent) or B ≈ D1 > A (generic record effect), stated as descriptive only]]

[[P3 C−B per model: estimate, 95% CI; read together with P4 and with `false_refutation`]]

[[P4 E_scope−E per model: estimate and one-sided 97.5% lower bound; explicitly "no noninferiority decision: δ not fixed"]]

[[Cross-model heterogeneity: whether any contrast reverses direction across models; if so, it is not reported as general.]]

### 4.5 Components and secondary outcomes

[[Component table for P1–P3: unsupported Q_obs, Q_cause, Q_welfare and the Q_obs-or-Q_cause composite per model, each with its interval (Appendix A has the full table; small multiples in `figures/fig_p2_components.png`, Appendix Figure A1). One sentence on whether any B − A difference is carried by Q_cause or Q_welfare rather than Q_obs.]]

[[Secondary, descriptive: D2 − A and P spillover in D2 (S2); causal overreach in E/E_scope improved (S3); welfare over-generalisation in E improved (S4); belief mean absolute error by cell (S5); recommendation distribution (S6). Exploratory: A0 vs A (X1), V vs A and V vs B (X2).]]

---

## 5. Discussion and Limitations

The design separates readings that a single "audit vs. no audit" comparison would conflate. B > A with B > D1 would indicate content-dependent unsupported attribution in this task. B ≈ D1 > A would indicate a broader verification or record effect. B ≈ A within a meaningful bound would be an informative null: truthful practice audits would not produce meaningful outcome-verification spillover in this task, for these cases and models. P3 is useful only when read with P4. A coverage statement that lowers unsupported attribution and also lowers correct acceptance is caution, not selective improvement.

[[Two to four sentences interpreting the development results against those readings, per model, using only "estimate / interval excludes or includes zero" language. No equivalence, meaningful-effect or noninferiority claims (SESOIs and δ unfixed). Note any floor in A or B that limits sensitivity.]]

### Limitations

- **Development evaluation, not confirmation.** All 12 cases were written by the study builder in one record-template family and were not independently authored. Six were run as a base set and six as a separately run extension. Generalisation is limited to this case population, and the cases were not sampled from real assurance files.
- **No expert validation yet.** Welfare-expert verdicts on what each record establishes (`EXPERT_VERDICTS.csv`) have not been collected. Thresholds, indicators, sampling methods and audit methods are plausible placeholders. Gold labels are rule-based and checked only against a hand table by the same author.
- **Unfixed decision thresholds.** The SESOIs for P1–P3 and the noninferiority margin δ for P4 are not fixed. We therefore make no equivalence, meaningful-effect or noninferiority decisions. The interval method is provisional pending the coverage simulation, and with [[K]] cases per model, intervals are wide.
- **Models and settings.** Four open-weight, text-only models, accessed through pinned third-party providers at provider-default sampling settings that the API does not report. Quantisation varies by provider (bf16 or fp8). Results may not hold for other checkpoints, providers, settings or proprietary models.
- **Measurement scaffold.** Asking for a separate status for each of six claims may itself make scope boundaries salient. That would push spillover toward a floor, and so would bias toward a null. A naturalistic committee-summary format would be needed before any claim about real workflows.
- **Confounds named in the ledger.** B is longer and more document-like than A. D1 cannot separate topic-sensitive authority from lexical overlap between the record and Q_cause. C's coverage text names the indicator, a possible lexical cue. Claim order is fixed. Every indicator is "lower is better". No case establishes causation, so Q_cause results describe over-attribution only.
- **Validity checks show only that obvious outcome evidence registers.** Passing V1–V3 does not show sensitivity to a smaller spillover effect.
- **Reasons are not scored.** A status may not reflect the model's stated reasoning. Blinded human status–reason checks are planned but have not been done.

### Future Work

1. Fix SESOIs and δ from practitioner and expert inputs (π_u, π_s, r) and complete the coverage simulation that selects the confirmatory interval method.
2. Collect welfare-expert verdicts on every claim–evidence row and practitioner review of the decision context.
3. Commission confirmatory cases from a different author, in several independently designed record formats, stored outside the repository, and size the case count by simulation of the paired, case-clustered design.
4. Add period-scope and population-scope conditions, higher-is-better indicators, counterbalanced claim order and a separate causal positive-control panel.
5. Validate a naturalistic committee-summary outcome with blinded human scoring.

---

## 6. Conclusion

We built a content-matched test of whether a truthful audit of a welfare practice leads language models to treat an unaudited outcome claim as verified, and whether stating audit coverage reduces that error without suppressing correct acceptance. The design fixes supplier statements across conditions, matches the unrelated-check control on issuer and template, requires positive controls to be inferred from audited numbers, and scores outcome, causal and overall-welfare over-reach separately. [[One to two sentences summarising the development results per model without confirmatory language.]] These results come from 12 builder-written development cases without expert validation and with no fixed effect thresholds. They are for development only, and the next step is a confirmatory study on independently authored, expert-validated cases with prespecified margins.

---

## Code and Data

- Repository: [[URL]], branch `p2-revision-3`, folder `scope-of-trust/rev3/`, commit [[SHA]].
- Specification: `REVISION_3_SPEC.md`; scoring: `SCORING_SPEC.md`; gold: `GOLD_LABELS.md`, `p2v3/gold.py`; contrasts: `CONTRAST_LEDGER.csv`.
- Cases: `p2v3/cases.py` (base), `p2v3/cases_ext.py` (extension). Rendered stimuli with hashes: `stimuli_dev.jsonl`, `stimuli_ext.jsonl`; human-readable renderings with gold: `rendered/`.
- Runner and analysis: `run_p2.py`, `llmrun.py`, `analyze_p2.py`, `p2v3/stats.py`; config `configs/p2_dev_eval_v1.json`.
- Run outputs: `runs/p2_dev_eval_v1/` (manifest, journal, responses, analysis), `runs/p2_ext_v1/` (extension) and [[combined analysis directory]].
- Tests: `tests/` (gold, leakage, chronology, scorer, matrix audit, statistics). [[Number of tests passing at the reported commit.]]
- All cases are synthetic; organisations and facilities are fictional. No personal data.

---

## References

Blackwelder, W. C. (1982). "Proving the null hypothesis" in clinical trials. *Controlled Clinical Trials*, 3(4), 345–353.

Blokhuis, H. J., Veissier, I., Miele, M., & Jones, B. (2010). The Welfare Quality® project and beyond: Safeguarding farm animal well-being. *Acta Agriculturae Scandinavica, Section A — Animal Science*, 60(3), 129–140.

EFSA Panel on Animal Health and Welfare (AHAW). (2012). Statement on the use of animal-based measures to assess the welfare of animals. *EFSA Journal*, 10(6), 2767.

Gao, T., Yen, H., Yu, J., & Chen, D. (2023). Enabling large language models to generate text with citations. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing* (pp. 6465–6488).

Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics*, 6(2), 65–70.

IAASB. (2013). *International Standard on Assurance Engagements (ISAE) 3000 (Revised): Assurance engagements other than audits or reviews of historical financial information*. International Federation of Accountants.

Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., Ishii, E., Bang, Y. J., Madotto, A., & Fung, P. (2023). Survey of hallucination in natural language generation. *ACM Computing Surveys*, 55(12), Article 248.

Kahneman, D., & Frederick, S. (2002). Representativeness revisited: Attribute substitution in intuitive judgment. In T. Gilovich, D. Griffin, & D. Kahneman (Eds.), *Heuristics and Biases: The Psychology of Intuitive Judgment* (pp. 49–81). Cambridge University Press.

Lakens, D. (2017). Equivalence tests: A practical primer for t tests, correlations, and meta-analyses. *Social Psychological and Personality Science*, 8(4), 355–362.

Liu, N. F., Zhang, T., & Liang, P. (2023). Evaluating verifiability in generative search engines. In *Findings of the Association for Computational Linguistics: EMNLP 2023*.

Lyon, T. P., & Maxwell, J. W. (2011). Greenwash: Corporate environmental disclosure under threat of audit. *Journal of Economics & Management Strategy*, 20(1), 3–41.

Maynez, J., Narayan, S., Bohnet, B., & McDonald, R. (2020). On faithfulness and factuality in abstractive summarization. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics* (pp. 1906–1919).

McCoy, R. T., Pavlick, E., & Linzen, T. (2019). Right for the wrong reasons: Diagnosing syntactic heuristics in natural language inference. In *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics* (pp. 3428–3448).

McNemar, Q. (1947). Note on the sampling error of the difference between correlated proportions or percentages. *Psychometrika*, 12(2), 153–157.

Min, S., Krishna, K., Lyu, X., Lewis, M., Yih, W., Koh, P. W., Iyyer, M., Zettlemoyer, L., & Hajishirzi, H. (2023). FActScore: Fine-grained atomic evaluation of factual precision in long form text generation. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing*.

Newcombe, R. G. (1998). Improved confidence intervals for the difference between binomial proportions based on paired data. *Statistics in Medicine*, 17(22), 2635–2650.

Obuchowski, N. A. (1998). On the comparison of correlated proportions for clustered data. *Statistics in Medicine*, 17(13), 1495–1507.

Porter, B. (1993). An empirical study of the audit expectation-performance gap. *Accounting and Business Research*, 24(93), 49–68.

Power, M. (1997). *The Audit Society: Rituals of Verification*. Oxford University Press.

Rashkin, H., Nikolaev, V., Lamm, M., Aroyo, L., Collins, M., Das, D., Petrov, S., Tomar, G. S., Turc, I., & Reitter, D. (2023). Measuring attribution in natural language generation models. *Computational Linguistics*, 49(4), 777–840.

Schuirmann, D. J. (1987). A comparison of the two one-sided tests procedure and the power approach for assessing the equivalence of average bioavailability. *Journal of Pharmacokinetics and Biopharmaceutics*, 15(6), 657–680.

Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., et al. (2024). Towards understanding sycophancy in language models. In *International Conference on Learning Representations (ICLR 2024)*.

Shi, F., Chen, X., Misra, K., Scales, N., Dohan, D., Chi, E. H., Schärli, N., & Zhou, D. (2023). Large language models can be easily distracted by irrelevant context. In *Proceedings of the 40th International Conference on Machine Learning* (PMLR 202).

Tango, T. (1998). Equivalence test and confidence interval for the difference in proportions for the paired-sample design. *Statistics in Medicine*, 17(8), 891–908.

Thorndike, E. L. (1920). A constant error in psychological ratings. *Journal of Applied Psychology*, 4(1), 25–29.

Thorne, J., Vlachos, A., Christodoulopoulos, C., & Mittal, A. (2018). FEVER: A large-scale dataset for fact extraction and VERification. In *Proceedings of NAACL-HLT 2018* (pp. 809–819).

Turpin, M., Michael, J., Perez, E., & Bowman, S. R. (2023). Language models don't always say what they think: Unfaithful explanations in chain-of-thought prompting. In *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*.

Welfare Quality®. (2009). *Welfare Quality® assessment protocol for poultry (broilers, laying hens)*. Welfare Quality® Consortium, Lelystad, Netherlands.

Wilson, E. B. (1927). Probable inference, the law of succession, and statistical inference. *Journal of the American Statistical Association*, 22(158), 209–212.

[[Concurrent 2026 work from §2, if kept after verification, with full references.]]

---

## Appendix

### A. Per-set results

[[A.1 Base set (6 cases): full contrast table per model, including worst/best bounds, Holm-adjusted p and comparison case-t interval. Source: `runs/p2_dev_eval_v1/analysis.md`.]]

[[A.2 Extension set (6 cases): same table. Source: `runs/p2_ext_v1/analysis.md` (path to confirm). If the extension run did not complete, state so here, and per the pre-declared rule report the base set only.]]

[[A.3 Component table (P1–P3 × unsupported Q_obs, Q_cause, Q_welfare, composite) per model and set.]]

![Figure A1: Component contrasts per model](figures/fig_p2_components.png)
*Figure A1. [[Caption: P1–P3 on unsupported Q_obs, Q_cause, Q_welfare and the composite, per model, with provisional 95% intervals; only Q_obs carries the test.]]*

[[A.4 Per-cell `unsupported_q_obs` rates and belief mean absolute error per model.]]

### B. Example stimulus (case `dev-hen-perch`, condition B, attribution context, Section 2)

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

Condition C appends: *"Coverage: This audit assessed perch length per hen only. It did not assess plumage condition records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes."* D1 keeps the issuer, reference, site, date and "Status: Confirmed" lines but checks fire-safety systems. E replaces the item with plumage condition records for 2024 and 2025 flocks and reports both years' recorded shares (27% → 14% in E/improved). Full renderings of all 14 cells and both contexts, with gold, are in `rendered/dev-hen-perch.md`.

### C. Gold labels by condition

| Condition | P | Q_obs | Q_welfare | Q_cause | R | S |
|---|---|---|---|---|---|---|
| A, A0, V | NE | NE | NE | NE | NE | NE |
| B, C, C′ | **T** | NE | NE | NE | NE | NE |
| D1 | NE | NE | NE | NE | **T** | NE |
| D2 | NE | NE | NE | NE | NE | **T** |
| E, E_scope improved | NE | **T** | NE | NE | NE | NE |
| E, E_scope worsened / unchanged | NE | **F** | NE | NE (F accepted) | NE | NE |

T = `established_true`, F = `established_false`, NE = `not_established`. A0 has no P claim. V's gold is contested, so V is exploratory.

### D. Changes during the sprint

All revision-3 materials (specification, renderer, cases, scorer, statistics, runner, analysis) were created during the sprint on branch `p2-revision-3`. Revision 2 and an earlier harness are preserved unchanged as a checksummed baseline in `archive/` [[confirm origin and date]]. Design reviews by other models (ChatGPT, Codex) and the responses to them are tabulated in `REVISION_3_SPEC.md` §11 and `REVIEW_RESPONSE_2026-11-16.md`.

### E. Dual use and ethics

Knowing that narrow verification can lend credibility to unchecked claims could help a supplier construct a misleading dossier. We report it because detection and disclosure policies depend on measuring it. All facilities, suppliers and auditors in the stimuli are fictional, and no animals or human participants were involved.

---

## LLM Usage Statement

Large language models were used in three roles. (1) **As study subjects:** the four open-weight models in §3.4. (2) **As engineering and writing assistants:** Claude (Anthropic) through Claude Code helped write the specification, renderer, scorer, statistics and analysis code, and drafted this report from the project's specification files. [[Authors: list any other assistants used.]] (3) **As design reviewers:** ChatGPT and Codex (OpenAI) reviewed the specification and code, and their findings and our responses are logged in the repository. The authors [[ ]] checked every claim, number and reference in this report against the code, run outputs and cited sources, and take responsibility for the content. No model output was used as a gold label.
