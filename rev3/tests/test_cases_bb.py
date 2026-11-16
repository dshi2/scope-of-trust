"""Batch bb (p2v3/cases_bb.py): the same convention and leakage checks as the base and extension sets.

The checks in tests/test_cases.py and tests/test_leakage.py read their module-level CASES. Rather than
editing those files, this module subclasses their test classes and swaps the module's CASES for
BASE + EXT + BB while each subclass runs (restored afterwards), so every per-case check covers the
batch and every uniqueness / cross-case-leak check runs across all 20 cases. Batch-specific checks
(family novelty, artifact freshness, rubric notes) follow.
"""
import importlib
import json
import os
import unittest

try:  # discovered as a top-level module (python3 -m unittest discover -s tests)
    import test_cases as tc
    import test_leakage as tl
except ImportError:  # imported as part of the tests package
    from tests import test_cases as tc
    from tests import test_leakage as tl

from p2v3 import render as r
from p2v3.cases import CASES as BASE_CASES
from p2v3.cases_bb import CASES_BB, PRACTICE_NOTES_BB
from p2v3.cases_ext import CASES_EXT

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRIOR = BASE_CASES + CASES_EXT
ALL = PRIOR + CASES_BB


class _WithBatchCases:
    """Mixin: run the inherited checks with the helper module's CASES = base + extension + batch bb."""
    module = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls._saved_cases = cls.module.CASES
        cls.module.CASES = ALL

    @classmethod
    def tearDownClass(cls):
        cls.module.CASES = cls._saved_cases
        super().tearDownClass()


class TestChronologyBB(_WithBatchCases, tc.TestChronology):
    module = tc


class TestFieldsBB(_WithBatchCases, tc.TestFields):
    module = tc


class TestInvariantsBB(_WithBatchCases, tl.TestInvariants):
    module = tl


class TestBatchBB(unittest.TestCase):
    def test_patch_is_effective(self):
        """Guard against the subclasses silently testing only the original 12 cases."""
        TestChronologyBB.setUpClass()
        try:
            self.assertIs(tc.CASES, ALL)
        finally:
            TestChronologyBB.tearDownClass()
        self.assertEqual(len(tc.CASES), len(PRIOR))

    def test_eight_cases_with_dev_ids(self):
        self.assertEqual(len(CASES_BB), 8)
        for k in CASES_BB:
            self.assertTrue(k["id"].startswith("dev-"), k["id"])

    def test_families_species_and_issuers_are_new(self):
        fam = lambda k: (k["species"], k["practice_type"], k["indicator_type"])
        prior_fams = {fam(k) for k in PRIOR}
        for f in ("species", "practice_type", "indicator_type", "issuer"):
            prior_vals = {k[f] for k in PRIOR}
            vals = [k[f] for k in CASES_BB]
            self.assertEqual(len(vals), len(set(vals)), f"duplicate {f} within batch")
            self.assertFalse(set(vals) & prior_vals, f"{f} shared with base/extension")
        self.assertFalse({fam(k) for k in CASES_BB} & prior_fams)

    def test_practice_notes_cover_batch(self):
        self.assertEqual(set(PRACTICE_NOTES_BB), {k["id"] for k in CASES_BB})
        for v in PRACTICE_NOTES_BB.values():
            self.assertEqual(len(v), 3)
            self.assertTrue(all(v))

    def test_rubric_rows_build_without_mutating_notes(self):
        import generate
        import generate_bb
        before = dict(generate.PRACTICE_NOTES)
        for k in CASES_BB:
            rows = generate_bb.rubric_rows(k)
            self.assertEqual([row[0] for row in rows], [f"{k['id']}:{c}" for c in generate.RUBRIC_CLAIMS])
        self.assertEqual(generate.PRACTICE_NOTES, before)

    def test_stimuli_bb_jsonl_matches_renderer(self):
        by_id = {k["id"]: k for k in CASES_BB}
        with open(os.path.join(HERE, "stimuli_bb.jsonl")) as f:
            rows = [json.loads(l) for l in f]
        self.assertEqual(len(rows), len(CASES_BB) * len(r.cells()) * len(r.CONTEXTS))
        self.assertEqual({row["item_id"] for row in rows}, set(by_id))
        for row in rows:
            msgs = r.render(by_id[row["item_id"]], row["condition"], row["direction"], row["context"])
            self.assertEqual(row["messages"], msgs)
            self.assertEqual(row["stimulus_sha256"], r.stimulus_hash(msgs))

    def test_bb_stimuli_disjoint_from_base_and_ext(self):
        ids = lambda name: {json.loads(l)["item_id"] for l in open(os.path.join(HERE, name))}
        bb = ids("stimuli_bb.jsonl")
        self.assertFalse(bb & ids("stimuli_dev.jsonl"))
        self.assertFalse(bb & ids("stimuli_ext.jsonl"))

    def test_unique_across_sibling_batches_if_present(self):
        """Batches ba and bc are written in parallel; once they exist, names must not collide with bb."""
        others = []
        for name, attr in (("p2v3.cases_ba", "CASES_BA"), ("p2v3.cases_bc", "CASES_BC")):
            try:
                others += getattr(importlib.import_module(name), attr)
            except (ImportError, AttributeError):
                continue
        if not others:
            self.skipTest("no sibling batch present")
        for f in ("id", "facility", "sister", "ref"):
            self.assertFalse({k[f] for k in CASES_BB} & {k[f] for k in others}, f)
        for k in CASES_BB:
            for o in others:
                self.assertNotIn(o["facility"], " ".join(str(v) for v in k.values()), (k["id"], o["id"]))


if __name__ == "__main__":
    unittest.main()
