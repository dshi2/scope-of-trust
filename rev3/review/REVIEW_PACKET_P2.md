# Review packet: P2 manuscript (workstream E)

**For:** ChatGPT, acting as strict, independent methodological reviewer. The user pastes this packet and `report/REPORT_P2_FINAL.md`.
**From:** Claude, workstream E (P2 report). No self-approval: E does not consider the manuscript done until the blocking points in your review are fixed or rebutted in writing.
**Repo:** https://github.com/dshi2/scope-of-trust/tree/p2-revision-3/rev3 (branch `p2-revision-3`).

> Status: SKELETON (16:32 IST). Sections 2 and 3 are completed once `review/P2_NUMBERS_READY.md` (workstream B) and `review/FIGURES_READY.md` (workstream C) exist.

## 1. Commits (E-owned files only)

| Commit | What | Link |
|---|---|---|
| 3121695 | Snapshot of the earlier session's uncommitted batch-1 fill of `REPORT_DRAFT.md`, before revision (unreviewed, contains the unsafe claims fixed below) | https://github.com/dshi2/scope-of-trust/commit/3121695 |
| 9abab07 | Revised draft: new title, four-claim framing, verified references, case-level zero-event bound, floor discussion, P4 "no decision"; numbers pending | https://github.com/dshi2/scope-of-trust/commit/9abab07 |

## 2. The strongest claims, verbatim

[filled at final]

## 3. Claim → source table

[filled at final: each number in the report → file, JSON key, value]

## 4. Unsafe claims found in the earlier draft, and the fix

| Earlier wording (commit 3121695) | Problem | Now |
|---|---|---|
| Abstract and Table 2: "one-sided 95% upper bound on the per-cell rate 4.9% per model, treating trials as independent" | Treats 60 repeats of 12 cases as 60 independent observations | Headline is the case-level bound, 1 − 0.05^(1/K) on the share of cases with ≥ 1 error. The trial-level bound appears only in Appendix F, labelled "assumes independent trials" |
| Discussion: "the per-model rate in B is below about 5% at the trial level" | Same | Removed |
| Table 2, P4: "0.000; LB −0.30", with the text "no loss was observed" | Invites a noninferiority reading | "P4 decision: no decision (δ not fixed)", plus the statement that the LB would fail any plausible margin and that 92 cases is the minimum for 5 pp even with perfect data |
| "Positive-control (V1–V3) intervals are case-level Wilson intervals" | The code changed to a case-level t interval (commit 6c0afb3) | Methods describe the case-t interval, clipped, with a degenerate flag. Wilson (1927) removed from the references |
| "It read the stamp as covering every concrete claim" (Qwen, V) | A mechanism claim from status counts | Replaced by status counts plus verbatim reasons; the wording is "marked established after an unscoped stamp", not "error" |
| "the two reasoning-enabled models never did" | Reasoning is confounded with model family | Kept as a description, with the explicit statement that it is not evidence that reasoning prevents it |
| "Batch 2 … will test whether the null holds on new cases" | Implies replication | "Later development batches from the same builder, not replication" |
| "models scope practice audits correctly" / "tight bound" (HANDOFF §4 wording) | Overclaims | Not used. The null is "a null with wide case-level uncertainty, not a precise null" and "not evidence that models cannot make the error" |

## 5. Deviations from the spec and contrast ledger

1. **No mixed-effects logistic model.** The ledger lists "mixed-effects logistic (case random intercept)" beside the interval for P1–P3 and S2/S3. `analyze_p2.py` does not fit one, and with zero events in both arms it would not be estimable.
2. **The coverage simulation is reduced.** The spec §6 grid (30–240 cases; 1, 3 and 5 repeats; missingness) was not run. The reduced grid in `SIM_P2_ALLPAIRS.md` has 6–60 cases, 5 repeats, no missingness, no model heterogeneity and no arm-specific case effect.
3. **No SESOI and no δ.** So there are no decisions: equivalence for P1–P3, noninferiority for P4, and TOST for S1. P4 is outside the Holm family until δ is fixed.
4. **Spec §9 sequence not followed.** The precision simulation before the pilot, the fixed SESOIs, and the stage-3 "diagnostic pilot only" framing were not followed: these runs are a development evaluation at full repeat count on builder cases. They are reported as development data, not as the pilot of §9.
5. **Batch 2 was added after batch 1 ran.** The rule (spec §7a, c22ff29) was fixed before any batch-2 output and before batch-1 contrasts were analysed.
6. **Human checks not done.** The human status–reason check (SCORING_SPEC §6) and expert verdicts (`EXPERT_VERDICTS.csv`) were not done.
7. **Title.** It changed from the earlier draft title to "The Scope of Trust: When a True Audit Licenses an Unsupported Conclusion" (PI instruction).

## 6. Known weaknesses

- The primary is a floor in every model, so the paper's main result is a bounded null. Its interpretation (scope discrimination vs. task explicitness) is not resolved by this design.
- All cases are builder-written by an LLM (Claude), in one template family, and not reviewed by experts. The case-level bound assumes exchangeable cases, which is not true in any sampling sense.
- The interval calibration rests on simulation only.
- The V cell is the only positive signal. Its gold label is contested, and it was not a primary hypothesis.

## 7. Questions for the reviewer

[filled at final]
