# The Scope of Trust (P2)

Does verifying a welfare practice make an agent attribute verification to an unchecked outcome claim? Can stating audit coverage reduce that error while preserving correct acceptance?

## Current development

Work is on `p2-revision-3`. The [revision-3 specification](rev3/REVISION_3_SPEC.md) describes the current design. Development cases, renderers, scoring and tests exist. Independent welfare validation, statistical precision/coverage validation and execution readiness remain required. Confirmatory experiments, paid runs and public release are not authorized.

- [Specification](rev3/REVISION_3_SPEC.md), [contrast ledger](rev3/CONTRAST_LEDGER.csv) and [scoring specification](rev3/SCORING_SPEC.md)
- [Source and development cases](rev3/p2v3/) and [tests](rev3/tests/)
- [Rendered review packets](rev3/rendered/) and [exact stimulus messages](rev3/stimuli_dev.jsonl)
- [Expert review rubric](rev3/CLAIM_EVIDENCE_RUBRIC.md) and [human-owned verdicts](rev3/EXPERT_VERDICTS.csv)
- [Commit-specific reviews](reviews/)

From `rev3/`:

```sh
python3 generate.py
python3 -m unittest discover -s tests -t . -q
```

Edit source cases and renderers, then regenerate derived artifacts. Do not hand-edit generated stimuli. `EXPERT_VERDICTS.csv` is human-owned and is never regenerated; a blank verdict is not approval.

## Historical material

`archive/codex-baseline-2026-11-16/` preserves the original combined P1/P2 diagnostic harness and its hashes. Do not edit it in place or use it as the current runner. `docs/` contains earlier protocols, checklists and handoffs; consult their revision status before applying them.

## Rules
- **Handoffs:** every handoff and review names repository · branch · commit · changes · checks performed · open issues. A review applies only to the commit it inspected.
- **No self-approval:** whoever wrote a component cannot approve it. Human/domain validation is required where the protocol says so.
- **Secrets:** never committed (see `.gitignore`). API keys stay in local environment variables.
- **Held-out confirmatory items** are kept outside development repos. Validators may inspect them under a fixed rubric; they and their results are never used for tuning, model choice, scoring changes or hypothesis selection.
- **Spending:** all projects share one ceiling and one ledger outside the repos (`~/Documents/research_active/ai-epistemics/budget/`, not yet created). Never one ledger per repo.
