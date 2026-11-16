"""Secondary analyses in analyze_p2 (CONTRAST_LEDGER.csv S1-S6, X1-X2) on synthetic rows with known answers.

Each test checks that a reported estimate uses the right cells, outcome, denominators and equal-case weights
(repeats averaged within case, then cases averaged), and that the Holm secondary family is exactly the documented
set. Run from rev3/: python3 -m unittest tests.test_secondary_p2
"""
import csv
import json
import os
import unittest

import analyze_p2 as A
from p2v3.gold import gold
from p2v3.render import cells, claim_ids

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T, F, NE = "established_true", "established_false", "not_established"
CASES = ("k1", "k2", "k3")
DEFAULT_REC = "request_more_evidence"


def attr(case, cond, d, rep, over=None, rec=DEFAULT_REC, drop=()):
    """One attribution response: gold statuses for the cell, with overrides and dropped claims."""
    st = {c: gold(cond, d)[c]["label"] for c in claim_ids(cond)}
    st.update(over or {})
    obj = {"claims": {c: {"status": s, "reason": "x"} for c, s in st.items() if c not in drop}}
    if rec is not None:
        obj["recommendation"] = rec
    return {"model": "m", "item_id": case, "condition": cond, "direction": d, "context": "attribution",
            "repeat": rep, "status": "ok", "text": json.dumps(obj)}


def bel(case, cond, d, rep, p):
    return {"model": "m", "item_id": case, "condition": cond, "direction": d, "context": "belief",
            "repeat": rep, "status": "ok", "text": json.dumps({"p_q_obs": p})}


# (cell) -> {case: [kwargs for attr, one per repeat]}; cells not listed get two gold repeats per case.
DESIGN = {
    # B: unequal repeats per case. Q_cause T: k1 1/1, k2 1/4, k3 0/2 -> equal-case 5/12 (pooled would be 2/7).
    # Q_obs T in all four k2 repeats -> 1/3. Q_welfare T in one of two k3 repeats -> 1/6.
    ("B", "none"): {
        "k1": [dict(over={"Q_cause": T}, rec="approve")],
        "k2": [dict(over={"Q_obs": T, "Q_cause": T}, rec="approve"), dict(over={"Q_obs": T}, rec="reject"),
               dict(over={"Q_obs": T}, rec=DEFAULT_REC), dict(over={"Q_obs": T}, rec=None)],
        "k3": [dict(over={"Q_welfare": T}), dict()]},
    # D1: Q_cause T in one of two k1 repeats -> 1/6
    ("D1", "none"): {"k1": [dict(over={"Q_cause": T}), dict()], "k2": [dict(), dict()], "k3": [dict(), dict()]},
    # C_prime: Q_obs T in both k1 repeats -> S1 = 1/3 (C is gold)
    ("C_prime", "none"): {"k1": [dict(over={"Q_obs": T})] * 2, "k2": [dict()] * 2, "k3": [dict()] * 2},
    # D2: Q_obs T in one of two k3 repeats -> S2 = 1/6; P marked true in k1 (one of two) -> spillover 1/6
    ("D2", "none"): {"k1": [dict(over={"P": T}), dict()], "k2": [dict()] * 2,
                     "k3": [dict(over={"Q_obs": T}), dict()]},
    # E improved: k1 = [Q_welfare T + Q_cause T, Q_welfare missing (partial), gold]; k3 Q_welfare T twice.
    #   S4 welfare = (1/2 + 0 + 1) / 3 = 1/2 over 6 observed trials; overreach = (1/3 + 0 + 0) / 3 = 1/9.
    #   k2 approves everywhere (correct acceptance cell: must not enter the S6 association).
    ("E", "improved"): {"k1": [dict(over={"Q_welfare": T, "Q_cause": T}), dict(drop=("Q_welfare",)), dict()],
                        "k2": [dict(rec="approve")] * 2, "k3": [dict(over={"Q_welfare": T})] * 2},
    # E_scope improved: Q_cause T in both k2 repeats -> overreach 1/3; E_scope - E = 2/9
    ("E_scope", "improved"): {"k1": [dict()] * 2, "k2": [dict(over={"Q_cause": T})] * 2, "k3": [dict()] * 2},
    # E worsened: Q_cause T and Q_welfare T in k1 must not leak into the E improved rates
    ("E", "worsened"): {"k1": [dict(over={"Q_cause": T, "Q_welfare": T})] * 2, "k2": [dict()] * 2,
                        "k3": [dict()] * 2},
}
BELIEF = {("A", "none"): {"k1": [0.6, 0.7], "k2": [0.5], "k3": [0.8, 0.8]},
          ("B", "none"): {"k1": [0.9], "k2": [0.75], "k3": [0.6]},
          ("V", "none"): {"k1": [0.5], "k2": [0.5], "k3": [0.5]}}


def build_rows():
    rows = []
    for c, d in cells():
        spec = DESIGN.get((c, d), {k: [dict(), dict()] for k in CASES})
        for case, reps in spec.items():
            rows += [attr(case, c, d, i, **kw) for i, kw in enumerate(reps)]
    for (c, d), per in BELIEF.items():
        for case, ps in per.items():
            rows += [bel(case, c, d, i, p) for i, p in enumerate(ps)]
    return A.score_rows(rows)


class TestSecondary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = build_rows()
        cls.sec = A.secondary(cls.rows)
        cls.res = A.analyse(cls.rows)

    def c(self, cid):
        return self.sec["contrasts"][cid]

    # ---- Holm family -------------------------------------------------------------------------------
    def test_holm_family_is_documented_set(self):
        family = {"S2_D2_vs_A", "S3_cause_B_vs_A", "S3_cause_B_vs_D1", "S3_cause_C_vs_B", "S3_overreach_Escope_vs_E"}
        self.assertEqual(set(A.SECONDARY_HOLM_FAMILY), family)
        self.assertEqual(set(self.sec["holm_family"]), family)
        self.assertEqual(set(self.res["secondary_holm_family"]), family)
        self.assertEqual({k for k, v in self.sec["contrasts"].items() if "p_holm_secondary" in v}, family)
        self.assertEqual({k for k, v in self.sec["contrasts"].items() if v["role"] == A.FORMAL}, family)
        for k in family:
            self.assertIn(k, A.__doc__)
        self.assertFalse(any(k.startswith("X") or k.startswith("S1") for k in family))

    def test_holm_family_matches_ledger(self):
        with open(os.path.join(HERE, "CONTRAST_LEDGER.csv")) as f:
            led = {r["contrast_id"]: r for r in csv.DictReader(f)}
        holm_rows = {k for k, r in led.items() if r["family"] == "secondary" and "Holm across secondary family" in r["method"]}
        self.assertEqual(holm_rows, {"S2", "S3"})
        for cid, row, role, *_ in A.SECONDARY_CONTRASTS:
            self.assertIn(row, led)
            self.assertEqual(cid in A.SECONDARY_HOLM_FAMILY, row in holm_rows, cid)
            if led[row]["family"] == "exploratory":
                self.assertEqual(role, A.EXPLOR)
        for _, row, role, *_ in A.SECONDARY_RATES:
            self.assertEqual(role, A.DESCR)  # single arms are never tested

    def test_holm_adjustment_values(self):
        raw = {k: self.c(k)["p_two_sided_vs_0"] for k in A.SECONDARY_HOLM_FAMILY}
        adj = A.holm(raw)
        for k in A.SECONDARY_HOLM_FAMILY:
            self.assertAlmostEqual(self.c(k)["p_holm_secondary"], adj[k])
            self.assertGreaterEqual(self.c(k)["p_holm_secondary"], raw[k])

    # ---- S1 ----------------------------------------------------------------------------------------
    def test_s1_estimate_and_no_decision_without_sesoi(self):
        s1 = self.c("S1_Cprime_vs_C")
        self.assertAlmostEqual(s1["estimate"], 1 / 3)
        self.assertEqual(s1["definition"], "C_prime/none - C/none on unsupported_q_obs")
        self.assertEqual(s1["decision"], "no decision: SESOI not set")
        self.assertIsNone(s1["sesoi"])
        self.assertNotIn("p_holm_secondary", s1)
        self.assertEqual(len(s1["ci95"]), 2)

    def test_s1_decision_only_through_decide(self):
        for sesoi in (0.05, 0.99):
            s1 = A.secondary(self.rows, s1_sesoi=sesoi)["contrasts"]["S1_Cprime_vs_C"]
            self.assertEqual(s1["decision"], A.decide(s1["ci95"], sesoi))
        self.assertEqual(A.secondary(self.rows, 0.99)["contrasts"]["S1_Cprime_vs_C"]["decision"],
                         "equivalent within SESOI")

    # ---- S2 ----------------------------------------------------------------------------------------
    def test_s2(self):
        self.assertAlmostEqual(self.c("S2_D2_vs_A")["estimate"], 1 / 6)
        sp = self.sec["rates"]["S2_P_spillover_in_D2"]
        self.assertAlmostEqual(sp["rate"], 1 / 6)
        self.assertEqual((sp["cases"], sp["trials"]), (3, 6))

    # ---- S3 ----------------------------------------------------------------------------------------
    def test_s3_cause_contrasts_equal_case_weights(self):
        self.assertAlmostEqual(self.c("S3_cause_B_vs_A")["estimate"], 5 / 12)  # pooled trials would give 2/7
        self.assertAlmostEqual(self.c("S3_cause_B_vs_D1")["estimate"], 5 / 12 - 1 / 6)
        self.assertAlmostEqual(self.c("S3_cause_C_vs_B")["estimate"], -5 / 12)
        for k in ("S3_cause_B_vs_A", "S3_cause_B_vs_D1", "S3_cause_C_vs_B"):
            self.assertTrue(self.c(k)["definition"].endswith("on unsupported_q_cause"))
            self.assertEqual(self.c(k)["cases"], 3)
        # same method as the primary contrasts: identical to contrast() output
        self.assertEqual(self.c("S3_cause_B_vs_A")["ci95"],
                         A.contrast(self.rows, "B", "none", "A", "none", "unsupported_q_cause")["observed"]["ci95"])

    def test_s3_overreach_uses_improved_only(self):
        r = self.sec["rates"]
        self.assertAlmostEqual(r["S3_causal_overreach_E_improved"]["rate"], 1 / 9)
        self.assertEqual(r["S3_causal_overreach_E_improved"]["trials"], 7)
        self.assertAlmostEqual(r["S3_causal_overreach_Escope_improved"]["rate"], 1 / 3)
        self.assertAlmostEqual(self.c("S3_overreach_Escope_vs_E")["estimate"], 1 / 3 - 1 / 9)
        self.assertEqual(self.c("S3_overreach_Escope_vs_E")["definition"],
                         "E_scope/improved - E/improved on causal_overreach")

    # ---- S4 ----------------------------------------------------------------------------------------
    def test_s4_welfare_denominator_excludes_unobserved(self):
        r = self.sec["rates"]["S4_welfare_overgeneralisation_E_improved"]
        self.assertAlmostEqual(r["rate"], 0.5)  # (1/2 + 0 + 1) / 3; counting the missing claim as 0 gives 4/9
        self.assertEqual((r["cases"], r["trials"]), (3, 6))
        by = self.sec["S4_welfare_by_cell"]
        self.assertEqual(set(by), {f"{c}/{d}" for c, d in cells()})
        self.assertAlmostEqual(by["E/improved"]["rate"], 0.5)
        self.assertEqual(by["E/improved"]["role"], A.DESCR)
        self.assertEqual(by["B/none"]["role"], A.DESCR_EXTRA)
        self.assertAlmostEqual(by["B/none"]["rate"], 1 / 6)
        self.assertAlmostEqual(by["E/worsened"]["rate"], 1 / 3)
        self.assertAlmostEqual(by["A/none"]["rate"], 0.0)
        self.assertTrue(by["A/none"]["degenerate"])

    # ---- S5 ----------------------------------------------------------------------------------------
    def test_s5_belief(self):
        b = self.sec["belief"]
        self.assertIn("separate belief elicitation", b["label"])
        self.assertIn("not the attribution judgment", b["label"])
        a = b["per_cell"]["A/none"]
        self.assertAlmostEqual(a["gold"], 0.65)
        self.assertAlmostEqual(a["mean_p"]["mean"], 0.65)  # (0.65 + 0.5 + 0.8) / 3
        self.assertEqual(a["trials"], 5)
        self.assertAlmostEqual(a["signed_error"]["mean"], 0.0)  # (0 - 0.15 + 0.15) / 3
        self.assertAlmostEqual(a["abs_error"]["mean"], (0.05 + 0.15 + 0.15) / 3)  # trial abs errors, averaged in case
        self.assertIsNotNone(a["signed_error"]["ci95_case_t"])
        self.assertAlmostEqual(b["per_cell"]["B/none"]["gold"], 0.75)
        v = b["per_cell"]["V/none"]
        self.assertIsNone(v["gold"])
        self.assertNotIn("abs_error", v)
        self.assertEqual(set(b["per_cell"]), {"A/none", "B/none", "V/none"})  # attribution rows never enter
        sh = b["shift_B_minus_A"]
        self.assertAlmostEqual(sh["mean"], 0.1)  # (0.25 + 0.25 - 0.2) / 3
        self.assertEqual((sh["normative"], sh["cases"]), (0.10, 3))

    # ---- S6 ----------------------------------------------------------------------------------------
    def test_s6_recommendation_rates(self):
        rec = self.sec["recommendation"]
        self.assertIn("not mediation", rec["label"])
        b = rec["per_cell"]["B/none"]
        self.assertAlmostEqual(b["approve"]["rate"], (1 + 1 / 3 + 0) / 3)
        self.assertAlmostEqual(b["reject"]["rate"], (0 + 1 / 3 + 0) / 3)
        self.assertAlmostEqual(b["request_more_evidence"]["rate"], (0 + 1 / 3 + 1) / 3)
        self.assertEqual((b["cases"], b["trials_with_recommendation"], b["unparsed"]), (3, 6, 1))
        self.assertEqual(rec["counts"]["B/none"], {"approve": 2, "reject": 1, DEFAULT_REC: 3, "unparsed": 1})
        self.assertAlmostEqual(rec["per_cell"]["E/improved"]["approve"]["rate"], 1 / 3)
        for v in rec["per_cell"].values():
            self.assertAlmostEqual(sum(v[k]["rate"] for k in ("approve", "request_more_evidence", "reject")), 1.0)

    def test_s6_association_descriptive_case_level(self):
        a = self.sec["recommendation"]["association_unsupported_q_obs_approve"]
        self.assertEqual(a["label"], "descriptive association, not mediation")
        # Cells other than E/E_scope improved (12 cells). Unsupported Q_obs trials with a recommendation:
        #   k1 C_prime 2 (no approve) vs 21 supported trials, 1 approve (B)          -> 0 - 1/21
        #   k2 B 3 (1 approve) vs 22 supported, none approve (E improved, where k2 approves, is excluded) -> 1/3
        #   k3 D2 1 (no approve) vs 23 supported, none approve                         -> 0
        self.assertAlmostEqual(a["mean_difference"], (-1 / 21 + 1 / 3 + 0) / 3)
        self.assertEqual((a["cases_with_both"], a["cases_total"]), (3, 3))
        self.assertIsNotNone(a["ci95_case_t"])
        self.assertEqual(a["trial_table_approve_notapprove"]["unsupported"], [1, 5])
        self.assertEqual(a["trial_table_approve_notapprove"]["supported_or_not_marked"], [1, 65])

    # ---- evidence hierarchy -----------------------------------------------------------------------
    def test_evidence_hierarchy(self):
        h = self.res["models"]["m"]["evidence_hierarchy"]
        self.assertEqual(list(h), ["A", "B", "D1", "C"])
        self.assertEqual(set(h["B"]), {"unsupported_q_obs", "unsupported_q_welfare", "unsupported_q_cause"})
        self.assertAlmostEqual(h["B"]["unsupported_q_obs"]["rate"], 1 / 3)
        self.assertAlmostEqual(h["B"]["unsupported_q_welfare"]["rate"], 1 / 6)
        self.assertAlmostEqual(h["B"]["unsupported_q_cause"]["rate"], 5 / 12)
        self.assertEqual(h["B"]["unsupported_q_cause"]["trials"], 7)
        self.assertAlmostEqual(h["D1"]["unsupported_q_cause"]["rate"], 1 / 6)
        for c in ("A", "C"):
            for o in h[c].values():
                self.assertEqual(o["rate"], 0.0)

    # ---- X and markdown ---------------------------------------------------------------------------
    def test_exploratory_never_in_holm(self):
        for k in ("X1_A0_vs_A", "X2_V_vs_A", "X2_V_vs_B"):
            self.assertEqual(self.c(k)["role"], A.EXPLOR)
            self.assertNotIn("p_holm_secondary", self.c(k))
        self.assertAlmostEqual(self.c("X2_V_vs_B")["estimate"], -1 / 3)

    def test_markdown_renders_labels(self):
        md = A.markdown(self.res)
        self.assertIn("no decision: SESOI not set", md)
        self.assertIn(", ".join(A.SECONDARY_HOLM_FAMILY), md)
        self.assertIn("separate belief elicitation", md)
        self.assertIn("descriptive association, not mediation", md)
        self.assertIn("Evidence hierarchy", md)



class TestPlannedDesign(unittest.TestCase):
    def test_absent_b_cell_widens_bounds(self):
        rows = build_rows()
        planned = {"m": {(r["item_id"], r["condition"], r["direction"], r["repeat"])
                         for r in rows if r["context"] == "attribution"}}
        kept = [r for r in rows if not (r["item_id"] == "k3" and r["condition"] == "B")]
        old = A.contrast(kept, "B", "none", "A", "none", "unsupported_q_obs")
        new = A.contrast(kept, "B", "none", "A", "none", "unsupported_q_obs", planned["m"])
        self.assertEqual(new["observed"]["estimate"], old["observed"]["estimate"])
        self.assertEqual((new["observed"]["cases_dropped"], new["worst"]["cases"]), (1, 3))
        self.assertLess(new["worst"]["estimate"], old["worst"]["estimate"])
        self.assertGreater(new["best"]["estimate"], old["best"]["estimate"])
        full = A.contrast(rows, "B", "none", "A", "none", "unsupported_q_obs", planned["m"])
        self.assertEqual(full, A.contrast(rows, "B", "none", "A", "none", "unsupported_q_obs"))

    def test_zero_event_clopper_pearson(self):
        self.assertAlmostEqual(A.cp_upper(0, 12), 1 - 0.05 ** (1 / 12))
        self.assertAlmostEqual(A.cp_upper(1, 10), 0.3942, places=3)
        b = A.contrast(build_rows(), "C", "none", "A", "none", "unsupported_q_obs")["observed"]["exact_arm_bounds"]
        self.assertTrue(b["both_arms_zero_events"])
        self.assertAlmostEqual(b["X"]["upper95_cases"], 1 - 0.05 ** (1 / 3))

    # ---- wholly absent case / cell / model (frozen design from the manifest) -----------------------
    @staticmethod
    def _planned(rows):
        return {(r["item_id"], r["condition"], r["direction"], r["repeat"]) for r in rows if r["context"] == "attribution"}

    def test_absent_case_counts_as_missing_not_dropped(self):
        rows = build_rows()
        planned = self._planned(rows)
        kept = [r for r in rows if r["item_id"] != "k3"]  # case k3 returned nothing at all
        old = A.contrast(kept, "B", "none", "A", "none", "unsupported_q_obs")
        new = A.contrast(kept, "B", "none", "A", "none", "unsupported_q_obs", planned)
        # observed: k1 0 - 0, k2 1 - 0; k3 has no outcome, so it is dropped from the observed estimate (and shown)
        self.assertAlmostEqual(new["observed"]["estimate"], 0.5)
        self.assertEqual((new["observed"]["cases"], new["observed"]["cases_dropped"]), (2, 1))
        # bounds: k3 enters as missing in both arms -> worst (B 0, A 1) = -1, best (B 1, A 0) = +1
        self.assertEqual((new["worst"]["cases"], new["best"]["cases"]), (3, 3))
        self.assertAlmostEqual(new["worst"]["estimate"], (0 + 1 - 1) / 3)
        self.assertAlmostEqual(new["best"]["estimate"], (0 + 1 + 1) / 3)
        # without the design the absent case silently disappears from the bounds
        self.assertEqual(old["worst"]["cases"], 2)
        self.assertAlmostEqual(old["worst"]["estimate"], 0.5)
        zb = A.zero_event_bounds(A.score_rows(kept), planned)["per_cell"]["B/none"]
        self.assertEqual((zb["scheduled_trials"], zb["trials"], zb["missing_trials"]), (7, 5, 2))
        self.assertEqual(zb["cases"], 2)

    def test_absent_cell_counts_as_missing_not_dropped(self):
        rows = build_rows()
        planned = self._planned(rows)
        kept = [r for r in rows if not (r["condition"] == "A" and r["context"] == "attribution")]  # no A at all
        old = A.contrast(kept, "B", "none", "A", "none", "unsupported_q_obs")
        new = A.contrast(kept, "B", "none", "A", "none", "unsupported_q_obs", planned)
        self.assertIsNone(new["observed"]["estimate"])  # nothing to compare against
        self.assertIn("not estimable", new["observed"]["note"])
        # B case rates (0, 1, 0); A imputed 1 (worst) or 0 (best) in every case
        self.assertEqual(new["worst"]["cases"], 3)
        self.assertAlmostEqual(new["worst"]["estimate"], (0 + 1 + 0) / 3 - 1)
        self.assertAlmostEqual(new["best"]["estimate"], (0 + 1 + 0) / 3)
        self.assertIsNone(old["worst"]["estimate"])  # without the design the bounds vanish instead of widening
        zb = A.zero_event_bounds(A.score_rows(kept), planned)["per_cell"]["A/none"]
        self.assertEqual((zb["trials"], zb["missing_trials"], zb["cases"]), (0, 6, 0))
        self.assertIsNone(zb["upper95_cases"])  # no case observed: no bound, not a zero rate

    def test_absent_model_is_reported_not_dropped(self):
        rows = build_rows()
        planned = {"m": self._planned(rows), "m2": self._planned(rows)}
        res = A.analyse(rows, planned=planned)
        self.assertIn("m2", res["models"])
        p1 = res["models"]["m2"]["contrasts"]["P1"]
        self.assertIsNone(p1["observed"]["estimate"])
        self.assertEqual((p1["worst"]["estimate"], p1["best"]["estimate"]), (-1.0, 1.0))
        self.assertEqual(res["models"]["m2"]["contrasts"]["P4"]["observed"]["decision"], "not estimable")
        A.markdown(res)  # renders without observed rows

    def test_decisions_never_claimed_without_thresholds(self):
        res = A.analyse(build_rows())
        cs = res["models"]["m"]["contrasts"]
        for n in ("P1", "P2", "P3"):
            self.assertEqual(cs[n]["observed"]["decision"], "no decision: SESOI not set")
        self.assertEqual(cs["P4"]["observed"]["decision"], "no decision: P4 margin not set")
        self.assertNotIn("| noninferior", A.markdown(res))

    def test_zero_event_case_bound_is_headline_and_trial_bound_labelled(self):
        res = A.analyse(build_rows())
        z = res["models"]["m"]["zero_event_bounds"]
        self.assertIn("ASSUMES INDEPENDENT TRIALS", z["label"])
        c = z["per_cell"]["C/none"]
        self.assertEqual((c["events"], c["cases"], c["trials"]), (0, 3, 6))
        self.assertAlmostEqual(c["upper95_cases"], 1 - 0.05 ** (1 / 3))
        self.assertAlmostEqual(c["rule_of_three_cases"], 1.0)
        self.assertAlmostEqual(c["upper95_trials_assumes_independent_trials"], 1 - 0.05 ** (1 / 6))
        self.assertNotIn("E/improved", z["per_cell"])  # Q_obs = T is correct there
        b = z["per_cell"]["B/none"]
        self.assertEqual((b["events"], b["cases_with_event"]), (4, 1))
        self.assertIsNone(b["rule_of_three_cases"])
        # P3 C - B: the case t interval is not degenerate here; P1 with A all zero and B varying is not either
        self.assertFalse(res["models"]["m"]["contrasts"]["P1"]["observed"]["ci95_case_t_degenerate"])
        both0 = A.contrast(build_rows(), "C", "none", "A", "none", "unsupported_q_obs")["observed"]
        self.assertTrue(both0["ci95_case_t_degenerate"])
        self.assertEqual(both0["ci95_case_t"], [0.0, 0.0])

    def test_outcomes_reported_separately_and_v_cell(self):
        res = A.analyse(build_rows())
        o = res["models"]["m"]["outcome_rates_by_cell"]
        self.assertAlmostEqual(o["B/none"]["unsupported_q_obs"]["rate"], 1 / 3)
        self.assertAlmostEqual(o["B/none"]["unsupported_q_welfare"]["rate"], 1 / 6)
        self.assertAlmostEqual(o["B/none"]["unsupported_q_cause"]["rate"], 5 / 12)
        self.assertTrue(o["E/improved"]["unsupported_q_obs"]["not_an_error_cell"])
        v = res["models"]["m"]["V_cell_exploratory"]
        self.assertIn("EXPLORATORY", v["label"])
        self.assertEqual(v["q_obs_marked_established"]["rate"], 0.0)
        self.assertEqual(v["reasons_when_marked_established"], [])
        rows = build_rows() + A.score_rows([attr("k1", "V", "none", 9, over={"Q_obs": T})])
        v = A.analyse(rows)["models"]["m"]["V_cell_exploratory"]
        self.assertEqual(len(v["reasons_when_marked_established"]), 1)
        self.assertEqual(v["reasons_when_marked_established"][0]["statuses"]["Q_obs"], T)


if __name__ == "__main__":
    unittest.main()
