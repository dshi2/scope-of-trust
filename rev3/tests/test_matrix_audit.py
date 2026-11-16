"""The design-adherence checks catch the failures Gate 3 names (incl. review of 3fb2448)."""
import os
import unittest
from functools import partial

from p2v3 import render as r
from p2v3.cases import CASES
from p2v3.matrix_audit import CELL, DECLARED_CELLS, KEY, audit_planned, load, reconcile

MATRIX = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "DESIGN_MATRIX_dev.csv")


# Independent declarations: cases come from the source registry, never the matrix under test.
DEV_ITEMS = {case["id"] for case in CASES}
audit_dev = partial(audit_planned, expected_items=DEV_ITEMS,
                    expected_models={"TBD"}, expected_repeats={"TBD"})
# Test vocabulary only; production callers must supply their frozen execution statuses.
reconcile_dev = partial(reconcile, terminal_statuses={"ok", "provider_error"})


def cell(row):
    return tuple(row[k] for k in CELL)


class TestPlanned(unittest.TestCase):
    def setUp(self):
        self.rows = load(MATRIX)

    def test_declared_design_matches_renderer(self):
        self.assertEqual(DECLARED_CELLS, {(c, d, x) for c, d in r.cells() for x in r.CONTEXTS})

    def test_dev_matrix_is_complete(self):
        rep = audit_dev(self.rows)
        self.assertTrue(rep["ok"], rep["issues"])
        self.assertEqual((rep["n_items"], rep["n_cells"]), (6, 28))

    def test_one_missing_row_flagged(self):
        self.assertFalse(audit_dev(self.rows[1:])["ok"])

    def test_whole_item_missing_flagged(self):
        rows = [x for x in self.rows if x["item_id"] != self.rows[0]["item_id"]]
        self.assertFalse(audit_dev(rows)["ok"])

    def test_whole_repeat_missing_flagged(self):
        self.assertFalse(audit_dev(self.rows, expected_repeats={"TBD", "second"})["ok"])

    def test_empty_matrix_refused(self):
        self.assertFalse(audit_dev([])["ok"])

    def test_independent_declarations_required(self):
        self.assertFalse(audit_planned(self.rows)["ok"])
        for name in ("expected_items", "expected_models", "expected_repeats", "expected_cells"):
            for value in (None, set()):
                with self.subTest(name=name, value=value):
                    self.assertFalse(audit_dev(self.rows, **{name: value})["ok"])

    def test_planned_fields_required(self):
        for field in ("item_id", "stimulus_sha256", "tools"):
            rows = [dict(x) for x in self.rows]
            rows[0].pop(field)
            self.assertFalse(audit_dev(rows)["ok"])

    def test_cell_missing_for_every_item_flagged(self):
        gone = cell(self.rows[0])
        self.assertFalse(audit_dev([x for x in self.rows if cell(x) != gone])["ok"])

    def test_model_missing_from_one_cell_flagged(self):
        rows = [dict(x, model=m) for x in self.rows for m in ("m1", "m2")]
        self.assertTrue(audit_dev(rows, expected_models={"m1", "m2"})["ok"])
        gone = cell(rows[0])
        rows = [x for x in rows if not (x["model"] == "m2" and cell(x) == gone)]
        self.assertFalse(audit_dev(rows, expected_models={"m1", "m2"})["ok"])

    def test_entire_model_missing_flagged(self):
        self.assertFalse(audit_dev(self.rows, expected_models={"TBD", "m2"})["ok"])

    def test_undeclared_cell_flagged(self):
        extra = dict(self.rows[0], condition="B_new")
        self.assertFalse(audit_dev(self.rows + [extra])["ok"])

    def test_duplicate_flagged(self):
        self.assertFalse(audit_dev(self.rows + self.rows[:1])["ok"])

    def test_setting_difference_flagged(self):
        rows = [dict(x) for x in self.rows]
        rows[5]["n_user_turns"] = "2"
        self.assertIn("n_user_turns", " ".join(audit_dev(rows)["issues"]))


class TestReconcile(unittest.TestCase):
    def setUp(self):
        self.plan = load(MATRIX)
        self.obs = [{**{k: x[k] for k in KEY}, "status": "ok", "attempts": 1,
                     "stimulus_sha256": x["stimulus_sha256"]} for x in self.plan]

    def test_complete_log_ok(self):
        rep = reconcile_dev(self.plan, self.obs, max_attempts=3)
        self.assertTrue(rep["ok"], rep["issues"])

    def test_missing_trial_blocks_ok(self):
        rep = reconcile_dev(self.plan, self.obs[1:], 3)
        self.assertFalse(rep["ok"])
        self.assertTrue(rep["valid_log"])
        self.assertFalse(rep["fully_observed"])
        self.assertEqual(rep["missing"], 1)

    def test_failures_are_records_not_missing(self):
        obs = [dict(o) for o in self.obs]
        obs[0]["status"] = "provider_error"
        rep = reconcile_dev(self.plan, obs, 3)
        self.assertTrue(rep["ok"], rep["issues"])
        self.assertTrue(rep["fully_observed"])
        self.assertIn("provider_error", str(rep["status_by_model_cell"]))

    def test_run_outside_matrix_refused(self):
        rep = reconcile_dev(self.plan, self.obs + [dict(self.obs[0], condition="B_new")], 3)
        self.assertFalse(rep["valid_log"])

    def test_bad_attempt_counts(self):
        for bad in (5, 0, "x", None, 1.5, 1.0, True, float("inf"), "01", "1.5"):
            obs = [dict(o) for o in self.obs]
            obs[0]["attempts"] = bad
            self.assertFalse(reconcile_dev(self.plan, obs, 3)["valid_log"], bad)

    def test_csv_integer_attempts_accepted(self):
        obs = [dict(o, attempts="1") for o in self.obs]
        self.assertTrue(reconcile_dev(self.plan, obs, 3)["ok"])

    def test_unknown_or_nonterminal_status_not_completion(self):
        for status in ("running", "", "new_unknown_status", None):
            obs = [dict(o) for o in self.obs]
            obs[0]["status"] = status
            rep = reconcile_dev(self.plan, obs, 3)
            self.assertFalse(rep["valid_log"])
            self.assertFalse(rep["fully_observed"])
            self.assertEqual(rep["missing"], 1)

    def test_hash_required(self):
        for value in (None, "", "missing"):
            obs = [dict(o) for o in self.obs]
            obs[0]["stimulus_sha256"] = value
            if value == "missing":
                obs[0].pop("stimulus_sha256")
            self.assertFalse(reconcile_dev(self.plan, obs, 3)["valid_log"])

    def test_invalid_plan_refused(self):
        for plan in ([], self.plan + self.plan[:1], [{"item_id": "incomplete"}]):
            with self.assertRaises(ValueError):
                reconcile_dev(plan, self.obs, 3)

    def test_invalid_execution_configuration_refused(self):
        for cap in (0, -1, True, 3.5, "3", None):
            with self.assertRaises(ValueError):
                reconcile_dev(self.plan, self.obs, cap)
        for statuses in (None, set(), "ok", {""}, {None}):
            with self.assertRaises(ValueError):
                reconcile(self.plan, self.obs, 3, terminal_statuses=statuses)

    def test_duplicate_observation_refused(self):
        self.assertFalse(reconcile_dev(self.plan, self.obs + self.obs[:1], 3)["valid_log"])

    def test_stimulus_drift_flagged(self):
        obs = [dict(o) for o in self.obs]
        obs[0]["stimulus_sha256"] = "0" * 64
        self.assertFalse(reconcile_dev(self.plan, obs, 3)["valid_log"])

    def test_retries_counted_by_model_and_condition(self):
        obs = [dict(o) for o in self.obs]
        obs[0]["attempts"] = 3
        rep = reconcile_dev(self.plan, obs, 3)
        self.assertEqual(rep["retries_by_model_condition"][(self.plan[0]["model"], self.plan[0]["condition"])], 2)


if __name__ == "__main__":
    unittest.main()
