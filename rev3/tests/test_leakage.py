"""Stimulus invariants. Necessary, not sufficient: passing these does NOT show the
prompts are leak-free. A human reviewer must still read rendered/ (AUDIT_REQUEST.md)."""
import re
import unittest

from p2v3 import render as r
from p2v3.cases import CASES

SECTION_SPLIT = "\n\nSECTION "


def sections(msg):
    """Split a user message into its numbered sections."""
    parts = msg.split(SECTION_SPLIT)
    return [parts[0]] + ["SECTION " + p for p in parts[1:]]


def user(case, c, d, ctx):
    return r.render(case, c, d, ctx)[1]["content"]


# Verdict, scope-rule or probability language that must not appear in sections 1-2.
FORBIDDEN_12 = [r"establish", r"support", r"refut", r"not performed", r"scope", r"probab",
                r"independent", r"unrelated", r"perfect", r"\bPr\(", r"different question",
                r"\btrue\b", r"\bfalse\b", r"caus(?!e of any change)", r"welfare"]
# 'verif' is allowed only as the V stamp.


class TestInvariants(unittest.TestCase):
    def test_system_identical_everywhere(self):
        systems = {r.render(k, c, d, x)[0]["content"] for k in CASES for c, d in r.cells() for x in r.CONTEXTS}
        self.assertEqual(systems, {r.SYSTEM})

    def test_dossier_and_task_identical_except_a0(self):
        for k in CASES:
            for x in r.CONTEXTS:
                stripped = set()
                for c, d in r.cells():
                    s = sections(user(k, c, d, x))
                    if c == "A0":
                        continue
                    stripped.add("\n\n".join([s[0]] + s[2:]))
                self.assertEqual(len(stripped), 1, f"{k['id']} {x}: conditions differ outside section 2")

    def test_a0_only_drops_p(self):
        for k in CASES:
            a = sections(user(k, "A", "none", "attribution"))
            a0 = sections(user(k, "A0", "none", "attribution"))
            self.assertEqual(a[1], a0[1])
            self.assertEqual(a0[0], "\n".join(l for l in a[0].split("\n") if not l.startswith("[P]")))
            self.assertNotIn('"P"', a0[2])

    def test_no_forbidden_language_in_dossier_or_audit(self):
        for k in CASES:
            for c, d in r.cells():
                s = sections(user(k, c, d, "attribution"))
                text = (s[0] + "\n" + s[1])
                audit = s[1]
                for pat in FORBIDDEN_12:
                    # dossier claims may contain 'caus'/'welfare' (they are the claims); check audit only for those
                    target = audit if pat in (r"caus(?!e of any change)", r"welfare") else text
                    self.assertIsNone(re.search(pat, target, re.I), f"{k['id']} {c} {d}: /{pat}/")
                n_verif = len(re.findall(r"verif", audit, re.I))
                self.assertEqual(n_verif, 1 if c == "V" else 0, f"{k['id']} {c}: verif count")

    def test_attribution_context_has_no_belief_model(self):
        for k in CASES:
            for c, d in r.cells():
                u = user(k, c, d, "attribution")
                self.assertNotIn("BACKGROUND", u)
                self.assertNotIn("Treat the following as true", u)
                self.assertNotIn("p_q_obs", u)
                self.assertNotIn(r.belief_model(k), u)

    def test_belief_context_shares_sections_1_2(self):
        for k in CASES:
            for c, d in r.cells():
                a, b = sections(user(k, c, d, "attribution")), sections(user(k, c, d, "belief"))
                self.assertEqual(a[:2], b[:2])
                self.assertIn(r.belief_model(k), b[2])

    def test_filing_notes_identical_in_every_cell(self):
        """Filler is fixed, not used to pad: variable filler was a treatment cue."""
        tail = "\n\nFiling notes:\n" + "\n".join(f"- {n}" for n in r.FILING_NOTES)
        for k in CASES:
            for c, d in r.cells():
                sec = r.audit_section(k, c, d)
                self.assertTrue(sec.endswith(tail))
                self.assertEqual(sec, r.audit_core(k, c, d) + tail)

    def test_e_directions_differ_only_in_finding(self):
        for k in CASES:
            for c in r.E_FAMILY:
                cores = [r.audit_core(k, c, d).split("\n") for d in r.DIRECTIONS]
                for other in cores[1:]:
                    diff = [i for i, (x, y) in enumerate(zip(cores[0], other)) if x != y]
                    self.assertEqual(len(cores[0]), len(other))
                    self.assertTrue(all(cores[0][i].startswith("Finding:") for i in diff))

    def test_coverage_conditions_are_base_plus_coverage(self):
        pairs = [("C", "B", "none"), ("C_prime", "B", "none")] + [("E_scope", "E", d) for d in r.DIRECTIONS]
        for k in CASES:
            for treat, base, d in pairs:
                t, b = r.audit_core(k, treat, d), r.audit_core(k, base, d)
                self.assertTrue(t.startswith(b + "\n\nCoverage:"), f"{k['id']} {treat} vs {base}")

    def test_specificity_and_place_controls_share_template(self):
        field = lambda core: [l.split(":")[0] for l in core.split("\n")]
        line = lambda core, key: next(l for l in core.split("\n") if l.startswith(key + ":"))
        for k in CASES:
            b, d1, d2 = (r.audit_core(k, c, "none") for c in ("B", "D1", "D2"))
            self.assertEqual(field(b), field(d1))
            self.assertEqual(field(b), field(d2))
            for key in ("Issued by", "Audit reference", "Date", "Status"):
                self.assertEqual(line(b, key), line(d1, key))
                self.assertEqual(line(b, key), line(d2, key))
            self.assertEqual(line(b, "Site"), line(d1, "Site"))
            self.assertNotEqual(line(b, "Site"), line(d2, "Site"))
            for key in ("Item checked", "Method"):
                self.assertEqual(line(b, key), line(d2, key))

    def test_filing_notes_are_neutral(self):
        content_words = r"complete|withheld|translat|letterhead|original|authentic|density|lesion|gait|keel|plumage|lame|tail|perch|cage|straw|stall|outcome|record checked|assess|audit"
        for note in r.FILING_NOTES:
            for pat in FORBIDDEN_12 + [r"verif", content_words]:
                self.assertIsNone(re.search(pat, note, re.I), f"filler /{pat}/: {note}")

    def test_no_cross_case_leak(self):
        for k in CASES:
            u = "".join(user(k, c, d, x) for c, d in r.cells() for x in r.CONTEXTS)
            for other in CASES:
                if other is not k:
                    self.assertNotIn(other["facility"], u)


    def test_detectors_fire_on_known_v2_leaks(self):
        """Mutation check: the actual revision-2 leak strings must be caught."""
        v2_leaks = ["A check supports only the claim and facility it assessed.",
                    "Checks are perfect for precisely the claim and facility checked.",
                    "R and the other facility are independent of target P and Q.",
                    "Assessment of Q: not performed. Q support: not established.",
                    "Result: supports Q", "These are different questions.",
                    "An unscoped label has no checked claim."]
        for leak in v2_leaks:
            self.assertTrue(any(re.search(p, leak, re.I) for p in FORBIDDEN_12), leak)

    def test_deterministic(self):
        for k in CASES:
            for c, d in r.cells():
                self.assertEqual(r.render(k, c, d, "attribution"), r.render(k, c, d, "attribution"))


if __name__ == "__main__":
    unittest.main()
