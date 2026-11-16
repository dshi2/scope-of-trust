"""Expert verdicts are human-owned: regeneration must never touch them, and every verdict row
must still point at a rubric row."""
import csv
import os
import unittest

import generate
from p2v3.cases import CASES

VERDICTS = os.path.join(generate.HERE, "EXPERT_VERDICTS.csv")
VALID = {"", "agree", "dispute"}


class TestRubric(unittest.TestCase):
    def test_generate_never_writes_verdicts(self):
        before = open(VERDICTS, "rb").read()
        generate.write_rubric()
        self.assertEqual(open(VERDICTS, "rb").read(), before)

    def test_verdict_ids_match_rubric(self):
        ids = {row[0] for k in CASES for row in generate.rubric_rows(k)}
        rows = list(csv.DictReader(open(VERDICTS)))
        self.assertEqual({r["row_id"] for r in rows}, ids)
        for r in rows:
            self.assertIn(r["verdict"], VALID, r["row_id"])


if __name__ == "__main__":
    unittest.main()
