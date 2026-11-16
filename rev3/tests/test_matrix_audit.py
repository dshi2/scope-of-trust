"""The design-adherence checks catch the failures Gate 3 names."""
import os
import unittest

from p2v3.matrix_audit import KEY, audit_planned, load, reconcile

MATRIX = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "DESIGN_MATRIX_dev.csv")


class TestPlanned(unittest.TestCase):
    def setUp(self):
        self.rows = load(MATRIX)

    def test_dev_matrix_is_complete_and_balanced(self):
        rep = audit_planned(self.rows)
        self.assertTrue(rep["ok"], rep["issues"])
        self.assertEqual((rep["n_items"], rep["n_cells"]), (6, 28))

    def test_missing_cell_flagged(self):
        self.assertFalse(audit_planned(self.rows[1:])["ok"])

    def test_duplicate_flagged(self):
        self.assertFalse(audit_planned(self.rows + self.rows[:1])["ok"])

    def test_setting_difference_flagged(self):
        rows = [dict(r) for r in self.rows]
        rows[5]["n_user_turns"] = "2"
        self.assertIn("n_user_turns", " ".join(audit_planned(rows)["issues"]))


class TestReconcile(unittest.TestCase):
    def setUp(self):
        self.plan = load(MATRIX)
        self.obs = [{**{k: r[k] for k in KEY}, "status": "ok", "attempts": 1} for r in self.plan]

    def test_complete_log_ok(self):
        rep = reconcile(self.plan, self.obs, max_attempts=3)
        self.assertTrue(rep["ok"], rep["issues"])
        self.assertEqual(rep["missing"], 0)

    def test_missing_trial_counted(self):
        self.assertEqual(reconcile(self.plan, self.obs[1:], 3)["missing"], 1)

    def test_run_outside_matrix_refused(self):
        extra = dict(self.obs[0], condition="B_new")
        self.assertFalse(reconcile(self.plan, self.obs + [extra], 3)["ok"])

    def test_retry_limit_and_counts(self):
        obs = [dict(o) for o in self.obs]
        obs[0]["attempts"] = 5
        rep = reconcile(self.plan, obs, 3)
        self.assertFalse(rep["ok"])
        self.assertEqual(rep["retries_by_condition"][self.plan[0]["condition"]], 4)


if __name__ == "__main__":
    unittest.main()
