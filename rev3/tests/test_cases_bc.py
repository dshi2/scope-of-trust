"""Batch bc (p2v3/cases_bc.py): the same convention and leakage checks as the base and extension sets.

Reuses the existing test classes unchanged: each subclass below swaps the module-level CASES of
tests/test_cases.py or tests/test_leakage.py for BASE + EXT + BC while its tests run, then restores it.
Uniqueness and cross-case leak checks therefore run across all 20 cases. Plus artifact freshness for
stimuli_bc.jsonl and the rubric/verdicts guard, mirroring tests/test_artifacts.py and tests/test_rubric.py.
"""
import hashlib
import json
import os
import unittest

import generate
from p2v3 import render as r
from p2v3.cases import CASES as BASE_CASES
from p2v3.cases_bc import BATCH, CASES_BC, PRACTICE_NOTES_BC
from p2v3.cases_ext import CASES_EXT
from tests import test_cases as tc
from tests import test_leakage as tl

ALL_CASES = BASE_CASES + CASES_EXT + CASES_BC
HERE = generate.HERE
FROZEN = {"stimuli_dev.jsonl": "368e1d0eeb5a56ef0a093f71d2655419ec1372925057f5ad875890cf624c8e67",
          "stimuli_ext.jsonl": "c9d92a016db4ba9b31039ab2371ba6b221d8bbcd3b300fd994fade4b39b063d0"}


class _WithBatch:
    """Mixin: run an existing TestCase's checks over ALL_CASES."""
    module = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls._saved = cls.module.CASES
        cls.module.CASES = ALL_CASES

    @classmethod
    def tearDownClass(cls):
        cls.module.CASES = cls._saved
        super().tearDownClass()


class TestChronologyBC(_WithBatch, tc.TestChronology):
    module = tc


class TestFieldsBC(_WithBatch, tc.TestFields):
    module = tc


class TestInvariantsBC(_WithBatch, tl.TestInvariants):
    module = tl


class TestBatchBC(unittest.TestCase):
    def test_batch_shape(self):
        self.assertEqual(len(CASES_BC), 8)
        self.assertEqual(set(PRACTICE_NOTES_BC), {k["id"] for k in CASES_BC})
        families = {(k["species"], k["practice_type"], k["indicator_type"]) for k in ALL_CASES}
        self.assertEqual(len(families), len(ALL_CASES))
        prior = {k["issuer"] for k in BASE_CASES + CASES_EXT}
        self.assertFalse(prior & {k["issuer"] for k in CASES_BC})

    def test_stimuli_bc_jsonl_matches_renderer(self):
        by_id = {k["id"]: k for k in CASES_BC}
        with open(os.path.join(HERE, f"stimuli_{BATCH}.jsonl")) as f:
            rows = [json.loads(l) for l in f]
        self.assertEqual(len(rows), len(CASES_BC) * len(r.cells()) * len(r.CONTEXTS))
        self.assertEqual({row["item_id"] for row in rows}, set(by_id))
        for row in rows:
            msgs = r.render(by_id[row["item_id"]], row["condition"], row["direction"], row["context"])
            self.assertEqual(row["messages"], msgs)
            self.assertEqual(row["stimulus_sha256"], r.stimulus_hash(msgs))

    def test_bc_stimuli_disjoint_from_frozen_sets(self):
        ids = lambda name: {json.loads(l)["item_id"] for l in open(os.path.join(HERE, name))}
        bc = ids(f"stimuli_{BATCH}.jsonl")
        for name in FROZEN:
            self.assertFalse(ids(name) & bc, name)

    def test_frozen_stimuli_unchanged(self):
        for name, sha in FROZEN.items():
            with open(os.path.join(HERE, name), "rb") as f:
                self.assertEqual(hashlib.sha256(f.read()).hexdigest(), sha, name)

    def test_rubric_does_not_touch_verdicts_or_shared_notes(self):
        import generate_bc
        verdicts = os.path.join(HERE, "EXPERT_VERDICTS.csv")
        before = open(verdicts, "rb").read()
        notes_before = dict(generate.PRACTICE_NOTES)
        generate_bc.write_rubric()
        self.assertEqual(open(verdicts, "rb").read(), before)
        self.assertEqual(generate.PRACTICE_NOTES, notes_before)
        text = open(os.path.join(HERE, f"CLAIM_EVIDENCE_RUBRIC_{BATCH}.md")).read()
        for k in CASES_BC:
            self.assertIn(f"| {k['id']}:P |", text)


if __name__ == "__main__":
    unittest.main()
