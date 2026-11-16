# Response to attached review — P2

Reviewed head: **12cd2a73ac81f74b186136507429d9c284ea839a**, PR #1, branch p2-revision-3. The attached review examined 015edae. This response distinguishes completed changes from specifications that still need implementation.

## Finding disposition

| Attached finding | Current files and change | Disposition |
|---|---|---|
| Composite confounds outcome verification with causal attribution | REVISION_3_SPEC §§1,6; SCORING_SPEC §4; CONTRAST_LEDGER.csv; p2v3/score.py; test_causal_only_error_does_not_move_primary. Changed in **6e67eca4afc6680e3d9d80b8f60bc86958497537**. | **Resolved.** Q_obs alone carries the primary claim. Q_cause and Q_welfare are separate; the OR composite is descriptive S7. |
| Explain exclusion of Q_welfare before results | §6 explicitly fixes exclusion and component-wise reporting. | Resolved at specification level. No outcome-dependent switching permitted. |
| P4 needs boundary-safe inference | §6 now rejects collapsing bootstrap intervals and requires coverage/type-I-error simulation. Initially corrected at 11fc58c; expanded at 6e67eca. | Requirement improved; **method selection, implementation and validation are unfinished**. |
| Expert review and naturalistic transfer | §§7–9a retain independent case review and separate transfer prerequisites; CLAIM_EVIDENCE_RUBRIC.md and human-owned EXPERT_VERDICTS.csv exist. Human file preserved by generator since **12cd2a7**. | Correctly pending. Blank expert verdicts are not approval. |
| No independently executed tests / no CI | This reviewer executed **53 tests**, all passed; current CI unittest run 43805123929 is successful. | Historical status superseded. Unit tests do not establish domain validity. |

A direct partial-response probe confirms that Q_obs=NE plus Q_cause=T in B produces primary unsupported_q_obs=False, causal component=True and composite=True. The central measurement correction is real.

## Remaining correction to the margin justification

§8.2 proposes delta <= SESOI(P3)/(2r), where r is the relative cost of missed correct acceptance, and says prevention of more unsupported acceptances than lost correct acceptances makes disclosure worthwhile.

These are **conditional rates on different evidence populations**. A deployment benefit statement also needs the frequency of each type of opportunity, and must establish that the two experimental contexts transport to that workflow.

If pi_U is the frequency of unsupported-claim opportunities, pi_V the frequency of genuinely supported ones, b the reduction in unsupported acceptance, l the loss of correct acceptance, and error-cost ratio r, the simple two-error accounting is:

**net benefit = pi_U b − pi_V r l.**

Example: pi_U=.1, pi_V=.9, b=.1, l=.05, r=1. The benefit is .01 and the loss .045, for net −.035. A 5-point margin derived from a 10-point conditional benefit does not guarantee a worthwhile deployed trade-off.

Options:
- explicitly assume and justify a balanced target mixture, with sensitivity analyses; or
- choose a standalone acceptable-loss margin from practitioner judgment and treat deployed net benefit as a separate question; or
- include prespecified prevalence/cost scenarios. With the current factor-of-two safety convention and pi_V>0, the corresponding inequality is delta <= pi_U*b/(2*pi_V*r).

The factor two is a policy convention, not a theorem. Fix assumptions before pilot outcome inspection. The audit is not requesting a larger sample merely to rescue an unjustified margin.

## Precision grid must match the intended claims

The listed acceptance grid spans .80–1.00, but §6 also says it will choose P1–P3 attribution intervals with baselines near zero. Add explicit low-rate cells for that purpose. Specify a reference-arm probability plus difference and restrict to feasible joint Bernoulli distributions; “per-arm acceptance × difference” must not create impossible cells. Exact probability-one cases need an explicit structural generator rather than a finite-logit approximation.

The current n grid stops at 240. That can diagnose small-sample coverage, but it must not cap the precision search if larger independent samples are necessary. Use a held-out validation grid or fresh Monte Carlo simulations after choosing a method, so tuning to simulated results is not mistaken for independent coverage verification.

## Minor documentation cleanup

SCORING_SPEC §2 says the composite is false only when both claims are “supported”. The code correctly returns false whenever both components are observed and neither is an unsupported endorsement, including NE. Correct that sentence. §7's “parsed trials” also needs endpoint-specific observed denominators because partial responses can contribute to Q_obs without contributing to the composite.

The test run emitted ResourceWarnings for unclosed file reads in test_rubric.py; tests passed. Routine context-manager cleanup suffices; this is not a scientific blocker.

## Decision

Accept the primary-endpoint repair. Continue offline statistical development and independent welfare validation. Do not mark boundary inference or practical benefit established until the method and assumptions are tested. No paid runs, merge or confirmatory freeze were performed in this response.
