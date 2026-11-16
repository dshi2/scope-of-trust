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
| `BACKLOG.md` | Ideas deliberately kept out of the matrix |
| `p2v3/` | Reference renderer, gold rules, scorer (stdlib only) |
| `tests/` | Leakage, gold, scorer and freshness tests |

All cases are synthetic and pending expert review. No model has been run.

## Matrix audit contract

`audit_planned` requires nonempty `expected_items`, `expected_models` and
`expected_repeats` declared independently of the matrix it checks. For development,
the case registry supplies item IDs and model/repeat are explicitly `TBD`.
Confirmatory callers must use the frozen eligibility list, pinned models and repeats.
An empty matrix or a wholly missing item, model or repeat must fail.

`reconcile` requires `terminal_statuses` from the frozen execution specification,
a positive integer `max_attempts`, and a stimulus hash on every observed record.
Attempts accept positive integers or canonical decimal CSV strings. Provider errors
can be terminal records; they are not successful model responses. Grader parse
statuses are a separate field. `fully_observed` means all planned trials have a
declared terminal record; `valid_log` also checks duplicates, attempts and hashes.
Neither flag alone establishes that the data are suitable for primary analysis.

Both audits must pass their applicable gates. These helpers do not enforce dispatch,
verify full run-manifest/model-setting identity, authorize live execution, validate
sample size, or replace the prespecified missing-data analysis. No production caller
is connected to them yet. The development matrix remains an engineering fixture.

From `rev3`, run `python3 -m unittest discover -s tests -q`.
