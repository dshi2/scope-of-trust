"""Case integrity: chronology, claim/audit period matching, field completeness."""
import re
import unittest
from datetime import date

from p2v3.cases import AUDIT_YEAR, PERIOD_YEARS
from p2v3.cases import CASES as BASE_CASES
from p2v3.cases_ext import CASES_EXT

# Every check runs over the base set and the extension set; uniqueness is checked across all 12.
CASES = BASE_CASES + CASES_EXT

MONTHS = {m: i for i, m in enumerate(["January", "February", "March", "April", "May", "June", "July",
                                       "August", "September", "October", "November", "December"], 1)}
PERIOD_FIELDS = ("practice_claim", "practice_item", "practice_method", "practice_finding", "q_obs", "q_welfare",
                 "outcome_item", "outcome_method", "s_claim", "s_finding")
R_FIELDS = ("r_claim", "r_item", "r_method", "r_finding")
REQUIRED = PERIOD_FIELDS + R_FIELDS + ("id", "species", "practice_type", "indicator_type", "facility", "sister",
                                       "issuer", "ref", "date", "item_short", "indicator_short", "indicator_name",
                                       "q_cause", "outcome_template", "better", "worse")
years = lambda text: {int(y) for y in re.findall(r"\b(20\d\d)\b", text)}


def audit_date(case):
    d, m, y = case["date"].split()
    return date(int(y), MONTHS[m], int(d))


class TestChronology(unittest.TestCase):
    def test_audits_dated_after_periods_close(self):
        for k in CASES:
            self.assertEqual(audit_date(k).year, AUDIT_YEAR, k["id"])
            self.assertGreater(audit_date(k), date(max(PERIOD_YEARS), 12, 31))

    def test_practice_and_outcome_fields_use_closed_periods_only(self):
        for k in CASES:
            for f in PERIOD_FIELDS:
                self.assertLessEqual(years(k[f]), set(PERIOD_YEARS), f"{k['id']}.{f}: {k[f]}")
            self.assertEqual(years(k["outcome_template"].format(y1="x", y2="y")), set(PERIOD_YEARS), k["id"])

    def test_practice_claims_time_bounded_and_audit_covers_same_period(self):
        last = max(PERIOD_YEARS)
        for k in CASES:
            for f in ("practice_claim", "s_claim"):
                self.assertTrue(k[f].startswith(f"Throughout {last},"), f"{k['id']}.{f}")
            for f in ("practice_item", "practice_method", "practice_finding", "s_finding"):
                self.assertIn(str(last), k[f], f"{k['id']}.{f}: audit must cover the whole claimed year")

    def test_other_topic_claim_is_about_the_audit_year(self):
        for k in CASES:
            self.assertEqual(years(k["r_claim"]), {AUDIT_YEAR}, k["id"])
            for f in R_FIELDS[1:]:
                self.assertLessEqual(years(k[f]), {AUDIT_YEAR}, f"{k['id']}.{f}")

    def test_q_obs_is_about_recorded_share(self):
        for k in CASES:
            self.assertIn("recorded share", k["q_obs"])
            self.assertIn("recorded share", k["indicator_name"])
            self.assertIn("Records were complete", k["outcome_template"])


class TestFields(unittest.TestCase):
    def test_required_fields(self):
        for k in CASES:
            for f in REQUIRED:
                self.assertTrue(k.get(f), f"{k['id']} missing {f}")

    def test_better_is_lower(self):
        num = lambda s: float(s.rstrip("%"))
        for k in CASES:
            self.assertLess(num(k["better"]), num(k["worse"]), k["id"])

    def test_unique_names(self):
        for f in ("id", "facility", "sister", "ref"):
            vals = [k[f] for k in CASES]
            self.assertEqual(len(vals), len(set(vals)), f)


if __name__ == "__main__":
    unittest.main()
