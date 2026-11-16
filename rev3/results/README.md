# P2 results (published analysis outputs)

These are the aggregated analysis outputs behind `report/REPORT_P2_FINAL.md`, copied from the gitignored `runs/` directories.

- `p2_batch1_combined/`: batch 1, with 12 cases.
- `p2_ba_analysis/`, `p2_bb_analysis/`, `p2_bc_analysis/`: the three batch-2 sets, with 8 cases each.
- `p2_all_batches/`: all 36 cases pooled. `between_batch.md` / `.json` give the per-batch, pooled and between-batch tables (spec §7a).

Each folder holds `analysis.json` (the numerical source), `analysis.md` and `v_cell_reasons.md`, which has the verbatim stated reasons from the exploratory V cell. Every analysis was recomputed by `check_p2_independent.py`, with 0 mismatches. `RAW_ARCHIVE_SHA256.txt` has the SHA-256 hashes of the archived raw journals.

Regenerate from `rev3/` with, for example, `python3 analyze_p2.py --run-dir runs/p2_dev_eval_v1 runs/p2_ext_v1 runs/p2_ba_v1 runs/p2_bb_v1 runs/p2_bc_v1 --out runs/p2_all_batches`.
