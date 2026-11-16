# Audit request: P2 revision 3, specification review (milestone 1)

**Repo:** `dshi2/scope-of-trust` · **branch:** `p2-revision-3` · **commit:** the PR head (quote the hash you inspected in your report).
**Builder:** Claude. **Reviewers:** ChatGPT and Codex, independently. The builder does not approve its own work.
**Scope:** specification only. Not under review yet: the execution harness, model adapter and logging (milestone 2).

## Reproduce
```bash
cd rev3
python3 -m unittest discover -s tests -t .     # expect 36 tests, OK
python3 generate.py && git diff --exit-code    # derived files must be unchanged
```
Python 3.9+ standard library only. No network, no model calls.

## What to inspect
| File | Question |
|---|---|
| `REVISION_3_SPEC.md` | Is it a complete, consistent consolidation of rev 2 + amendments? Is anything adopted silently? |
| `rendered/*.md` | **Read the full model-visible text.** Is there any answer leakage or scope coaching shared across conditions, through instructions, output schema, claim wording, filler or record layout? Forbidden-word tests are necessary but not sufficient. |
| `GOLD_LABELS.md`, `p2v3/gold.py` | Is any gold label wrong or contestable? Are scope, observed change, overall welfare and causal improvement kept apart? |
| `CONTRAST_LEDGER.csv` | For each contrast: is the intended difference the only systematic one? Which confounds are missing? |
| `SCORING_SPEC.md`, `p2v3/score.py`, `tests/test_scorer.py` | Can a degenerate responder (reject-all, accept-all) score well on any primary or validity metric? Any parsing path that misclassifies? |
| `COVERAGE_dev.md` | Is the case population adequately described, and are the gaps honest? |
| Spec §8 | Your recommendation on each open decision. |

## Specific risks the builder is unsure about
1. The coverage statement in C names "the cause of any change", which may be a lexical cue for Q_cause (ledger P3).
2. Filler imbalance: A has 9 filing notes, B 4–5 (`COVERAGE_dev.md`). Is a long run of notes with no record itself a cue?
3. Belief-context item 5 (independence) is scope-like, but it is needed to define the gold.
4. Q_cause wording ("the lower stocking density") names the practice in every condition, including A0.
5. The task's definition of "established" ("an independent check whose findings establish…") could be read as coaching.
6. Synthetic cases: are the thresholds, indicators and methods realistic? A welfare expert is still needed.

## Report format
For each finding: **severity** (blocker / major / minor), **file:line or rendered cell**, **evidence** (quote), and **proposed fix**. End with a go/no-go verdict on milestone 1 only.
