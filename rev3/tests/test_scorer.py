"""Adversarial scorer tests (SCORING_SPEC.md §5): each canned responder must get the
metrics a correct scorer would assign."""
import json
import unittest

from p2v3 import render as r
from p2v3.gold import F, NE, T, gold
from p2v3.score import score_attribution, score_belief


def resp(statuses, rec="request_more_evidence", wrap=None):
    obj = {"claims": {k: {"status": v, "reason": "x"} for k, v in statuses.items()}, "recommendation": rec}
    s = json.dumps(obj)
    return wrap.format(s) if wrap else s


def constant(c, status):
    return resp({k: status for k in r.claim_ids(c)})


def perfect(c, d):
    return resp({k: v["label"] for k, v in gold(c, d).items()})


class TestResponders(unittest.TestCase):
    def test_perfect_responder(self):
        for c, d in r.cells():
            m = score_attribution(perfect(c, d), c, d)
            self.assertEqual(m["parse"], "ok")
            self.assertFalse(m["unsupported_attribution"], c)
            self.assertFalse(m["false_refutation"])
            self.assertTrue(m["all_claims_correct"])
            for k in ("correct_acceptance", "correct_refutation", "manipulation_check"):
                self.assertIn(m[k], (True, None), f"{c} {d} {k}")
            if c in r.E_FAMILY:
                self.assertFalse(m["causal_overreach"])

    def test_reject_all_is_not_rewarded(self):
        """Blanket 'not_established' avoids attribution but fails every validity check."""
        for c, d in r.cells():
            m = score_attribution(constant(c, NE), c, d)
            self.assertFalse(m["unsupported_attribution"])
            for k in ("correct_acceptance", "correct_refutation", "manipulation_check"):
                self.assertIn(m[k], (False, None), f"{c} {d} {k}")
        self.assertFalse(score_attribution(constant("E", NE), "E", "improved")["correct_acceptance"])
        self.assertFalse(score_attribution(constant("B", NE), "B")["manipulation_check"])

    def test_accept_all_is_caught(self):
        for c, d in r.cells():
            m = score_attribution(constant(c, T), c, d)
            self.assertTrue(m["unsupported_attribution"], c)
            self.assertTrue(m["unsupported_q_welfare"])
            self.assertTrue(m["unsupported_q_cause"])
        self.assertTrue(score_attribution(constant("E", T), "E", "improved")["correct_acceptance"])
        self.assertFalse(score_attribution(constant("E", T), "E", "worsened")["correct_refutation"])

    def test_blanket_scepticism_is_caught(self):
        m = score_attribution(constant("B", F), "B")
        self.assertTrue(m["false_refutation"])
        self.assertFalse(m["unsupported_attribution"])
        self.assertFalse(m["manipulation_check"])


class TestTargetedErrors(unittest.TestCase):
    def test_scope_spillover_in_b(self):
        g = {k: v["label"] for k, v in gold("B").items()} | {"Q_obs": T}
        m = score_attribution(resp(g), "B")
        self.assertTrue(m["unsupported_attribution"])
        self.assertTrue(m["unsupported_q_obs"])
        self.assertTrue(m["manipulation_check"])

    def test_place_spillover_in_d2(self):
        g = {k: v["label"] for k, v in gold("D2").items()} | {"P": T}
        m = score_attribution(resp(g), "D2")
        self.assertFalse(m["unsupported_attribution"])  # P is not an outcome claim
        self.assertFalse(m["all_claims_correct"])

    def test_causal_overreach_in_e(self):
        g = {k: v["label"] for k, v in gold("E", "improved").items()} | {"Q_cause": T}
        m = score_attribution(resp(g), "E", "improved")
        self.assertTrue(m["correct_acceptance"])
        self.assertTrue(m["causal_overreach"])
        self.assertTrue(m["unsupported_q_cause"])

    def test_welfare_overgeneralisation_in_e(self):
        g = {k: v["label"] for k, v in gold("E", "improved").items()} | {"Q_welfare": T}
        m = score_attribution(resp(g), "E", "improved")
        self.assertTrue(m["unsupported_q_welfare"])
        self.assertFalse(m["causal_overreach"])
        self.assertFalse(m["unsupported_attribution"])  # Q_welfare is secondary, not in the primary endpoint

    def test_failed_presupposition_accepts_false_for_q_cause(self):
        g = {k: v["label"] for k, v in gold("E", "worsened").items()} | {"Q_cause": F}
        m = score_attribution(resp(g), "E", "worsened")
        self.assertTrue(m["all_claims_correct"])
        self.assertTrue(m["correct_refutation"])
        self.assertFalse(m["false_refutation"])

    def test_refuting_overall_welfare_from_one_indicator_is_wrong(self):
        for d in ("worsened", "unchanged"):
            g = {k: v["label"] for k, v in gold("E", d).items()} | {"Q_welfare": F}
            m = score_attribution(resp(g), "E", d)
            self.assertTrue(m["false_refutation"], d)
            self.assertFalse(m["all_claims_correct"])

    def test_wrong_direction_in_e(self):
        g = {k: v["label"] for k, v in gold("E", "worsened").items()} | {"Q_obs": T}
        m = score_attribution(resp(g), "E", "worsened")
        self.assertFalse(m["correct_refutation"])
        self.assertTrue(m["unsupported_q_obs"])


class TestParsing(unittest.TestCase):
    def test_malformed_gets_no_metrics(self):
        for text in ["I would approve.", "", None, "{not json", '["P","T"]']:
            m = score_attribution(text, "B")
            self.assertEqual(m["parse"], "malformed")
            self.assertIsNone(m["unsupported_attribution"])
            self.assertIsNone(m["manipulation_check"])

    def test_no_claims_object_is_invalid(self):
        m = score_attribution('{"recommendation": "approve"}', "B")
        self.assertEqual(m["parse"], "invalid")
        self.assertIsNone(m["unsupported_attribution"])
        self.assertEqual(m["recommendation"], "approve")

    def test_all_statuses_invalid_is_invalid(self):
        bad = {k: "true" for k in r.claim_ids("B")}
        self.assertEqual(score_attribution(resp(bad), "B")["parse"], "invalid")

    def test_observed_endorsement_survives_missing_claim(self):
        """Reviewer probe (957a3ca): Q_obs endorsed, S missing. The endorsement must be scored."""
        claims = {k: NE for k in r.claim_ids("B")} | {"Q_obs": T}
        del claims["S"]
        m = score_attribution(resp(claims), "B")
        self.assertEqual(m["parse"], "partial")
        self.assertEqual(m["missing_claims"], ["S"])
        self.assertTrue(m["unsupported_q_obs"])
        self.assertTrue(m["unsupported_attribution"])

    def test_composite_undecided_when_component_missing(self):
        claims = {k: NE for k in r.claim_ids("B")}
        del claims["Q_cause"]
        m = score_attribution(resp(claims), "B")
        self.assertEqual(m["parse"], "partial")
        self.assertFalse(m["unsupported_q_obs"])
        self.assertIsNone(m["unsupported_q_cause"])
        self.assertIsNone(m["unsupported_attribution"])

    def test_invalid_status_on_one_claim_is_partial(self):
        bad = {k: v["label"] for k, v in gold("B").items()} | {"Q_obs": "true"}
        m = score_attribution(resp(bad), "B")
        self.assertEqual(m["parse"], "partial")
        self.assertIsNone(m["unsupported_q_obs"])
        self.assertTrue(m["manipulation_check"])

    def test_fenced_and_prose_wrapped_json(self):
        text = perfect("C", "none")
        for wrap in ["```json\n{}\n```", "Here is my answer: {} Thanks.", "Note {{braces}} first. {}"]:
            self.assertEqual(score_attribution(wrap.format(text), "C")["parse"], "ok", wrap)

    def test_braces_inside_reason_strings(self):
        obj = {"claims": {k: {"status": v["label"], "reason": "see {record} }"} for k, v in gold("B").items()},
               "recommendation": "approve"}
        self.assertEqual(score_attribution(json.dumps(obj), "B")["parse"], "ok")

    def test_a0_extra_p_is_flagged_not_fatal(self):
        g = {k: v["label"] for k, v in gold("A0").items()} | {"P": T}
        m = score_attribution(resp(g), "A0")
        self.assertEqual(m["parse"], "ok")
        self.assertEqual(m["extra_claims"], ["P"])

    def test_invalid_recommendation_is_none(self):
        self.assertIsNone(score_attribution(resp({k: NE for k in r.claim_ids("A")}, rec="maybe"), "A")["recommendation"])


class TestBelief(unittest.TestCase):
    def test_belief_scoring(self):
        self.assertAlmostEqual(score_belief('{"p_q_obs": 0.7}', "A")["abs_error"], 0.05)
        self.assertAlmostEqual(score_belief('{"p_q_obs": 0.9}', "E", "worsened")["abs_error"], 0.9)
        self.assertIsNone(score_belief('{"p_q_obs": 0.7}', "V")["abs_error"])
        for bad in ['{"p_q_obs": 1.2}', '{"p_q_obs": true}', '{"p_q_obs": "0.7"}', '{"p": 0.7}']:
            self.assertEqual(score_belief(bad, "A")["parse"], "invalid", bad)
        self.assertEqual(score_belief("about 70%", "A")["parse"], "malformed")


if __name__ == "__main__":
    unittest.main()
