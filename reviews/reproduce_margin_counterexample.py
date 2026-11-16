"""Check primary/component separation and margin arithmetic. No model calls."""
from pathlib import Path
from fractions import Fraction as F
import json
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "rev3"))
from p2v3.score import score_attribution

result = score_attribution(json.dumps({"claims": {
    "Q_obs": {"status": "not_established"},
    "Q_cause": {"status": "established_true"},
}}), "B")
assert result["unsupported_q_obs"] is False
assert result["unsupported_q_cause"] is True
assert result["unsupported_obs_or_cause"] is True
print(json.dumps({k:result[k] for k in (
    "parse","unsupported_q_obs","unsupported_q_cause","unsupported_obs_or_cause")}, indent=2))

benefit = F(1,10) * F(1,10)
cost = F(9,10) * F(1,20)
net = benefit - cost
assert net == F(-7,200)
print("Illustrative weighted benefit:", float(benefit), "cost:", float(cost), "net:", float(net))
print("A conditional-rate margin alone does not establish deployed net benefit.")
