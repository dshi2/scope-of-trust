#!/usr/bin/env python3
"""Check published P2 headline numbers against the committed pooled analysis.

This is an aggregate-output consistency check, not independent raw-data
rescoring, expert validation, or a model/API rerun.
"""
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / "rev3/results/p2_all_batches/analysis.json").read_text())
assert data["n_cases"] == 36, "Expected 36 builder-written cases"
models = data["models"]
want_v = {
    "deepseek-v3.2": (0, 0),
    "gpt-oss-120b": (0, 0),
    "kimi-k2-0905": (3, 3),
    "qwen3-235b-a22b-2507": (96, 32),
}
assert set(models) == set(want_v), "Model set changed"
assert sum(m["n_calls"] for m in models.values()) == 20_160
for model, (v_events, v_cases) in want_v.items():
    m = models[model]
    assert m["n_calls"] == 5040, f"{model}: wrong number of API calls"
    assert m["cell_case_summary"]["B/none"]["events"] == 0, f"{model}: primary error in B"
    for cell in ("A/none", "D1/none", "B/none", "C/none"):
        assert m["cell_case_summary"][cell]["events"] == 0, f"{model} {cell}: primary error count"
    for contrast in ("P1", "P2", "P3"):
        est = m["contrasts"][contrast]["observed"]["estimate"]
        assert math.isclose(est, 0.0, abs_tol=1e-12), f"{model}: {contrast} not zero"
    p4 = m["contrasts"]["P4"]["observed"]
    assert math.isclose(p4["estimate"], 0.0, abs_tol=1e-12), f"{model}: unexpected P4 effect"
    assert "no decision" in p4["decision"].lower(), f"{model}: unsupported P4 decision"
    for cell in ("E/improved", "E_scope/improved"):
        assert math.isclose(m["cell_case_summary"][cell]["equal_case_mean"], 1.0), f"{model}: positive control failed"
    v = m["V_cell_exploratory"]["q_obs_marked_established"]
    assert v["events"] == v_events and v["cases_with_event"] == v_cases, f"{model}: V counts changed"
    if model == "qwen3-235b-a22b-2507":
        assert v["trials"] == 180 and math.isclose(v["rate"], 96/180), "Qwen V rate changed"
assert 36 * 14 * 4 * 5 * 2 == 20_160
print("P2 aggregate headline check PASS: 36 cases, 14 cells, 4 models, 20,160 calls; P1–P4 and V counts agree.")
print("Note: aggregate-output consistency only. Raw response journals are archived separately.")
