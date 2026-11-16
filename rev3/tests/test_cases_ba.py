"""Expansion batch `ba`: rerun the existing case-convention and leakage checks over CASES_BA.

Reuses tests/test_cases.py and tests/test_leakage.py unchanged: each of their test classes is
subclassed here and run with the module-level CASES list temporarily set to base + extension +
batch ba, so uniqueness and cross-case leak checks span all 20 cases. Adds artifact freshness for
stimuli_ba.jsonl and, when sibling batch modules (cases_bb, cases_bc) are importable, uniqueness
and facility-name leak checks across batches.
"""
import importlib
import json
import os
import unittest
from unittest import mock

try:  # `python3 -m unittest discover -s tests` puts tests/ on sys.path
    import test_cases as tc
    import test_leakage as tl
except ImportError:  # `python3 -m unittest tests.test_cases_ba`
    from tests import test_cases as tc
    from tests import test_leakage as tl

from p2v3 import render as r
from p2v3.cases import CASES as BASE_CASES
from p2v3.cases_ba import CASES_BA, PRACTICE_NOTES_BA
from p2v3.cases_ext import CASES_EXT

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALL = BASE_CASES + CASES_EXT + CASES_BA


class _WithBatch:
    """Run the inherited tests with the source module's CASES set to base + ext + ba."""
    MODULE = None

    @classmethod
    def setUpClass(cls):
        cls._patch = mock.patch.object(cls.MODULE, "CASES", ALL)
        cls._patch.start()

    @classmethod
    def tearDownClass(cls):
        cls._patch.stop()


class TestChronologyBA(_WithBatch, tc.TestChronology):
    MODULE = tc


class TestFieldsBA(_WithBatch, tc.TestFields):
    MODULE = tc


class TestInvariantsBA(_WithBatch, tl.TestInvariants):
    MODULE = tl


class TestBatchBA(unittest.TestCase):
    def test_batch_size_and_distinct_families(self):
        self.assertEqual(len(CASES_BA), 8)
        fam = lambda ks: {(k["species"], k["practice_type"], k["indicator_type"]) for k in ks}
        self.assertEqual(len(fam(CASES_BA)), 8)
        self.assertFalse(fam(CASES_BA) & fam(BASE_CASES + CASES_EXT))
        for dim in ("species", "issuer"):
            prior = {k[dim] for k in BASE_CASES + CASES_EXT}
            for k in CASES_BA:
                self.assertNotIn(k[dim], prior, f"{k['id']}.{dim}")

    def test_practice_notes_cover_batch(self):
        self.assertEqual(set(PRACTICE_NOTES_BA), {k["id"] for k in CASES_BA})
        for v in PRACTICE_NOTES_BA.values():
            self.assertEqual(len(v), 3)
            self.assertTrue(all(v))

    def test_stimuli_ba_jsonl_matches_renderer(self):
        by_id = {k["id"]: k for k in CASES_BA}
        with open(os.path.join(HERE, "stimuli_ba.jsonl")) as f:
            rows = [json.loads(l) for l in f]
        self.assertEqual(len(rows), len(CASES_BA) * len(r.cells()) * len(r.CONTEXTS))
        self.assertEqual({row["item_id"] for row in rows}, set(by_id))
        for row in rows:
            msgs = r.render(by_id[row["item_id"]], row["condition"], row["direction"], row["context"])
            self.assertEqual(row["messages"], msgs)
            self.assertEqual(row["stimulus_sha256"], r.stimulus_hash(msgs))

    def test_batch_stimuli_disjoint_from_base_and_ext(self):
        ids = lambda name: {json.loads(l)["item_id"] for l in open(os.path.join(HERE, name))}
        ba = ids("stimuli_ba.jsonl")
        self.assertFalse(ba & ids("stimuli_dev.jsonl"))
        self.assertFalse(ba & ids("stimuli_ext.jsonl"))

    def test_generator_never_writes_verdicts(self):
        path = os.path.join(HERE, "EXPERT_VERDICTS.csv")
        before = open(path, "rb").read()
        import generate_ba
        generate_ba.write_rubric()
        self.assertEqual(open(path, "rb").read(), before)


def _sibling_batches():
    out = {}
    for tag in ("bb", "bc"):
        try:
            mod = importlib.import_module(f"p2v3.cases_{tag}")
            out[tag] = getattr(mod, f"CASES_{tag.upper()}")
        except Exception:  # sibling batch not written yet (or mid-edit): its own tests cover it
            pass
    return out


class TestAcrossSiblingBatches(unittest.TestCase):
    def test_unique_names_across_batches(self):
        siblings = _sibling_batches()
        if not siblings:
            self.skipTest("no sibling batch module importable")
        cases = ALL + [k for ks in siblings.values() for k in ks]
        for f in ("id", "facility", "sister", "ref"):
            vals = [k[f] for k in cases]
            dupes = sorted({v for v in vals if vals.count(v) > 1})
            self.assertFalse(dupes, f"{f} shared across batches: {dupes}")

    def test_no_facility_leak_across_batches(self):
        siblings = _sibling_batches()
        if not siblings:
            self.skipTest("no sibling batch module importable")
        others = [k for ks in siblings.values() for k in ks]
        text = lambda k: " ".join(v for v in k.values() if isinstance(v, str))
        for k in CASES_BA:
            for o in others:
                self.assertNotIn(o["facility"], text(k), f"{o['id']} facility in {k['id']}")
                self.assertNotIn(k["facility"], text(o), f"{k['id']} facility in {o['id']}")


if __name__ == "__main__":
    unittest.main()
