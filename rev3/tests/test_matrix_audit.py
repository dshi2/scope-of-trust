"""The design-adherence checks catch the failures Gate 3 names (incl. review of 3fb2448)."""
import os
import unittest

from p2v3 import render as r
from p2v3.matrix_audit import CELL, DECLARED_CELLS, KEY, audit_planned, load, reconcile

MATRIX = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "DESIGN_MATRIX_dev.csv")


def cell(row):
    return tuple(row[k] for k in CELL)


class TestPlanned(unittest.TestCase):
    def setUp(self):
        self.rows = load(MATRIX)

    def test_declared_design_matches_renderer(self):
        self.assertEqual(DECLARED_CELLS, {(c, d, x) for c, d in r.cells() for x in r.CONTEXTS})

    def test_dev_matrix_is_complete(self):
        rep = audit_planned(self.rows)
        self.assertTrue(rep["ok"], rep["issues"])
        self.assertEqual((rep["n_items"], rep["n_cells"]), (6, 28))

    def test_one_missing_row_flagged(self):
        self.assertFalse(audit_planned(self.rows[1:])["ok"])

    def test_cell_missing_for_every_item_flagged(self):
        gone = cell(self.rows[0])
        self.assertFalse(audit_planned([x for x in self.rows if cell(x) != gone])["ok"])

    def test_model_missing_from_one_cell_flagged(self):
        rows = [dict(x, model=m) for x in self.rows for m in ("m1", "m2")]
        gone = cell(rows[0])
        rows = [x for x in rows if not (x["model"] == "m2" and cell(x) == gone)]
        self.assertFalse(audit_planned(rows)["ok"])

    def test_entire_model_missing_flagged(self):
        self.assertFalse(audit_planned(self.rows, expected_models={"TBD", "m2"})["ok"])

    def test_undeclared_cell_flagged(self):
        extra = dict(self.rows[0], condition="B_new")
        self.assertFalse(audit_planned(self.rows + [extra])["ok"])

    def test_duplicate_flagged(self):
        self.assertFalse(audit_planned(self.rows + self.rows[:1])["ok"])

    def test_setting_difference_flagged(self):
        rows = [dict(x) for x in self.rows]
        rows[5]["n_user_turns"] = "2"
        self.assertIn("n_user_turns", " ".join(audit_planned(rows)["issues"]))


class TestReconcile(unittest.TestCase):
    def setUp(self):
        self.plan = load(MATRIX)
        self.obs = [{**{k: x[k] for k in KEY}, "status": "ok", "attempts": 1,
                     "stimulus_sha256": x["stimulus_sha256"]} for x in self.plan]

    def test_complete_log_ok(self):
        rep = reconcile(self.plan, self.obs, max_attempts=3)
        self.assertTrue(rep["ok"], rep["issues"])

    def test_missing_trial_blocks_ok(self):
        rep = reconcile(self.plan, self.obs[1:], 3)
        self.assertFalse(rep["ok"])
        self.assertTrue(rep["valid_log"])
        self.assertFalse(rep["fully_observed"])
        self.assertEqual(rep["missing"], 1)

    def test_failures_are_records_not_missing(self):
        obs = [dict(o) for o in self.obs]
        obs[0]["status"] = "provider_error"
        rep = reconcile(self.plan, obs, 3)
        self.assertTrue(rep["fully_observed"])
        self.assertIn("provider_error", str(rep["status_by_model_cell"]))

    def test_run_outside_matrix_refused(self):
        rep = reconcile(self.plan, self.obs + [dict(self.obs[0], condition="B_new")], 3)
        self.assertFalse(rep["valid_log"])

    def test_bad_attempt_counts(self):
        for bad in (5, 0, "x", None):
            obs = [dict(o) for o in self.obs]
            obs[0]["attempts"] = bad
            self.assertFalse(reconcile(self.plan, obs, 3)["valid_log"], bad)

    def test_stimulus_drift_flagged(self):
        obs = [dict(o) for o in self.obs]
        obs[0]["stimulus_sha256"] = "0" * 64
        self.assertFalse(reconcile(self.plan, obs, 3)["valid_log"])

    def test_retries_counted_by_model_and_condition(self):
        obs = [dict(o) for o in self.obs]
        obs[0]["attempts"] = 3
        rep = reconcile(self.plan, obs, 3)
        self.assertEqual(rep["retries_by_model_condition"][(self.plan[0]["model"], self.plan[0]["condition"])], 2)


if __name__ == "__main__":
    unittest.main()
