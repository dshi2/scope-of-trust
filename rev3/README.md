# P2 revision 3: specification packet

Start with `REVISION_3_SPEC.md`, then `AUDIT_REQUEST.md`.

| Path | What |
|---|---|
| `REVISION_3_SPEC.md` | Authoritative rev-3 specification, the diff from rev 2, and open decisions |
| `rendered/` | Exact model-visible messages for every case × cell × context, with gold labels |
| `GOLD_LABELS.md` | Gold labels with reasons, derived from evidence profiles |
| `CLAIM_EVIDENCE_RUBRIC.md` | Claim-evidence mapping with residual risks (generated) |
| `EXPERT_VERDICTS.csv` | Expert verdicts keyed by rubric row id; human-owned, never written by `generate.py` |
| `REVIEW_RESPONSE_2026-11-16.md` | Item-by-item response to the independent review |
| `CONTRAST_LEDGER.csv` | Every contrast: intended difference, held fixed, remaining confounds |
| `SCORING_SPEC.md` | Parse rules, metrics, adversarial examples |
| `COVERAGE_dev.md` | Case-coverage report and known gaps |
| `DESIGN_MATRIX_dev.csv` | One row per case × cell × context (models and repeats TBD) |
| `stimuli_dev.jsonl` | Every stimulus with its SHA-256 |
| `p2v3/cases_ext.py`, `generate_ext.py` | Extension set: 6 further synthetic cases in new audit families (dairy cows, salmon, turkeys, ducks, rabbits, calves), rendered with the same code |
| `stimuli_ext.jsonl`, `DESIGN_MATRIX_ext.csv`, `COVERAGE_ext.md`, `CLAIM_EVIDENCE_RUBRIC_ext.md` | Extension-set artifacts (`python3 generate_ext.py`). Run separately from the base set; reported with the base only if the extension run completes (pre-declared) |
| `BACKLOG.md` | Ideas deliberately kept out of the matrix |
| `p2v3/` | Reference renderer, gold rules, scorer (stdlib only) |
| `tests/` | Leakage, gold, scorer and freshness tests |

All cases are synthetic and pending expert review. No model has been run.
