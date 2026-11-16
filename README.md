# The Scope of Trust (P2): verification-scope spillover in animal-welfare assurance

**Question.** Holding the facts fixed, does truthfully verifying one welfare claim (e.g. a housing practice) make an AI agent say a different, unchecked claim (e.g. improved welfare outcomes) was verified? Does stating the audit's coverage reduce this without suppressing correct acceptance?

## Status (2026-11-16)
| Item | Status |
|---|---|
| Specification and offline implementation | **Proceeding.** Revision 3 work on branch `p2-revision-3` |
| Novelty and practical relevance | Under evaluation. The use case needs confirming by a welfare expert |
| Diagnostic pilot | Not yet. Needs revision 3 implemented, independent review, and models + spending ceiling set |
| Confirmatory study | **Not approved** |
| Public dataset release | Not approved (after validation, permission checks and the PI's approval) |
| Authorized paid runs | **None** |

## Contents
- `archive/codex-baseline-2026-11-16/`: the Codex offline harness and reviews, preserved unchanged, with `SHA256SUMS`. **Historical diagnostic baseline (revision 2), not a confirmatory freeze.** The harness is shared with P1. Do not edit it in place.
- `docs/`: governing documents.

## Component ownership
The baseline is one combined P1+P2 codebase. Under revision 3, P2-specific code (`p2.py`, the P2 parts of the runner, scoring) moves here. Shared infrastructure (budget ledger, model adapter, analysis utilities) is owned by `verification-under-pressure/common/` and copied in with its source commit hash recorded.

## Known blockers (found in the baseline; fixes go in revision 3)
- The stimuli give away the answer: a scope rule appears in the shared probability model and system prompt; C/C′ include "Q support: not established"; E states a verdict.
- D1 is not matched to B in issuer, template or seriousness.
- Outcome levels are not separated (measurement verified / improvement verified / causal / belief). Attribution and belief must be asked in separate fresh contexts.
- Scope clarification needs supported cases with and without the clarification, to show it preserves correct acceptance.

## Governing documents (`docs/`)
- `PROTOCOLS_v1.md`: revision 2 plus revision 3 / 3b amendment notes. A consolidated revision 3 specification is in progress; until then, revision 2 + the amendment notes apply.
- `NOVELTY_GATE_FINAL.md`: §2.2 novelty and contribution gate (round 2).
- `MASTER_CHECKLIST_ADDENDUM.md`: amendments to the 10-gate Research Quality Protocol (Master Checklist v3). **The v3 checklist text itself still needs adding.**
- `EXECUTION_CHECKLIST.md`: superseded; kept for history.
- `NOVELTY_CHECK*.md`, `HANDOFF_TO_CODEX.md`: history.
- `SHA256SUMS`: hashes of these documents as first committed.

## Rules
- **Handoffs:** every handoff and review names repository · branch · commit · changes · checks performed · open issues. A review applies only to the commit it inspected.
- **No self-approval:** whoever wrote a component cannot approve it. Human/domain validation is required where the protocol says so.
- **Secrets:** never committed (see `.gitignore`). API keys stay in local environment variables.
- **Held-out confirmatory items** are kept outside development repos. Validators may inspect them under a fixed rubric; they and their results are never used for tuning, model choice, scoring changes or hypothesis selection.
- **Spending:** all projects share one ceiling and one ledger outside the repos (`~/Documents/research_active/ai-epistemics/budget/`, not yet created). Never one ledger per repo.

**Governing checklist:** Master Checklist v3, canonical copy at [dshi2/research-candidates@396e29d/docs/MASTER_CHECKLIST_v3.md](https://github.com/dshi2/research-candidates/blob/396e29d/docs/MASTER_CHECKLIST_v3.md) (SHA-256 `8e4ba457b2e04775…`), with `docs/MASTER_CHECKLIST_ADDENDUM.md` taking precedence. It is pinned rather than copied.
