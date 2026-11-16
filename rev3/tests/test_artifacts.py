"""Committed derived artifacts must match what the code renders now (run generate.py if this fails)."""
import json
import os
import unittest

from p2v3 import render as r
from p2v3.cases import CASES
from p2v3.cases_ext import CASES_EXT

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestArtifactsFresh(unittest.TestCase):
    def test_stimuli_jsonl_matches_renderer(self):
        by_id = {k["id"]: k for k in CASES}
        with open(os.path.join(HERE, "stimuli_dev.jsonl")) as f:
            rows = [json.loads(l) for l in f]
        self.assertEqual(len(rows), len(CASES) * len(r.cells()) * len(r.CONTEXTS))
        for row in rows:
            msgs = r.render(by_id[row["item_id"]], row["condition"], row["direction"], row["context"])
            self.assertEqual(row["messages"], msgs)
            self.assertEqual(row["stimulus_sha256"], r.stimulus_hash(msgs))

    def test_stimuli_ext_jsonl_matches_renderer(self):
        by_id = {k["id"]: k for k in CASES_EXT}
        with open(os.path.join(HERE, "stimuli_ext.jsonl")) as f:
            rows = [json.loads(l) for l in f]
        self.assertEqual(len(rows), len(CASES_EXT) * len(r.cells()) * len(r.CONTEXTS))
        self.assertEqual({row["item_id"] for row in rows}, set(by_id))
        for row in rows:
            msgs = r.render(by_id[row["item_id"]], row["condition"], row["direction"], row["context"])
            self.assertEqual(row["messages"], msgs)
            self.assertEqual(row["stimulus_sha256"], r.stimulus_hash(msgs))

    def test_base_and_ext_stimuli_disjoint(self):
        ids = lambda name: {json.loads(l)["item_id"] for l in open(os.path.join(HERE, name))}
        self.assertFalse(ids("stimuli_dev.jsonl") & ids("stimuli_ext.jsonl"))


if __name__ == "__main__":
    unittest.main()
