# P2 reference check (workstream E, 16 Nov 2026, 16:20–16:30 IST)

Every reference in `REPORT_DRAFT.md` and `report/REPORT_P2_FINAL.md` was checked on the web: its existence, its bibliographic details, and whether it supports the sentence that cites it. Verification was done by Claude (web search and fetch of arXiv, publisher or index pages). This is a builder check, not an independent one. Where the full text was not read, the "Supports" column says what was checked.

| Reference | Checked at | Bibliographic details confirmed | What the report cites it for | Supports? |
|---|---|---|---|---|
| Arslan (2026) arXiv:2609.07680 | arxiv.org/abs/2609.07680 | title, sole author, v1 7 Sep 2026 | LLM auditors relay upstream conclusions rather than check them | yes (abstract: deleting the conclusion field raises auditor accuracy; adherence 94.4% → 3.4%) |
| Blackwelder (1982) | Scilit / NCI pages | Controlled Clinical Trials 3(4):345–353 | noninferiority requires a prespecified margin | yes (standard citation for "proving the null hypothesis") |
| Clopper & Pearson (1934) | Scilit, bibbase | Biometrika 26(4):404–413 | exact binomial bound | yes |
| EFSA AHAW Panel (2012) | efsa.europa.eu/en/efsajournal/pub/2767 | EFSA Journal 10(6):2767 | animal-based vs. resource/management-based measures | yes (statement on ABMs; terminology and links between input factors and welfare outcomes) |
| Hanley & Lippman-Hand (1983) | JAMA abstract page, PMC citations | JAMA 249(13):1743–1745 | rule of three, 3/n | yes |
| Holm (1979) | bibliographic indexes | Scand. J. Statist. 6(2):65–70 | Holm adjustment | yes |
| Hu (2026) arXiv:2609.20211 | arxiv.org/abs/2609.20211 | title, sole author Yibo Hu (page lists v1 25 Jul 2026) | monitors approve risky actions more often when handoffs drop the "unverified" status | yes (abstract: e.g. 5% → 60%, 9% → 98% risky approval) |
| IAASB (2013) ISAE 3000 (Revised) | IAASB PDF, ¶69 read in full; approved Sep 2013 | standard title | report must identify the subject matter information and the applicable criteria | yes (¶69(c), (d)) |
| Jeffries (2026) arXiv:2610.32110 | arxiv.org/abs/2610.32110 | title, sole author, v1 23 Oct 2026 | formatters that drop scope details mislead agents and verifiers; restoring them reduces unsupported claims | yes (abstract: "substantially for three of the four failure types") |
| Ji et al. (2023) | arXiv 2202.03629, ACM listing | ACM CSUR 55(12), Art. 248 | definition of hallucination | yes |
| Kumar & Chopra (2026) arXiv:2609.37616 | arxiv.org/abs/2609.37616 | title, authors, v1 29 Sep 2026 | a verified-source note flips 45–88% of baseline-correct answers in 7 of 8 models | yes (quoted in abstract) |
| Lakens (2017) | PMC5502906 | SPPS 8(4):355–362 | equivalence needs a SESOI | yes |
| marhmpa (2026) WelfareFacts | huggingface.co/datasets/Maryamp/welfare-facts | 35 source-grounded numeric welfare facts, CC BY 4.0, 2026 | numeric welfare facts, no audit-scope manipulation | yes |
| Maynez et al. (2020) | aclanthology.org/2020.acl-main.173 | ACL 2020, pp. 1906–1919 | hallucination as content unsupported by the source | yes |
| McCoy et al. (2019) | ACL Anthology P19-1334 | ACL 2019, pp. 3428–3448 | lexical-overlap heuristics | yes |
| Obuchowski (1998) | Scilit | Stat. Med. 17(13):1495–1507 | correlated proportions with clustered data | yes |
| Porter (1993) | ProQuest listing, secondary sources | ABR 24(93):49–68 | audit expectation–performance gap | yes (secondary descriptions; full text not read) |
| Power (1997) | publisher and library records | OUP, 1997 | audit as "rituals of verification" | yes (book's thesis; full text not read) |
| Rashkin et al. (2023) | aclanthology.org/2023.cl-4.2 | Comput. Linguist. 49(4):777–840 | attribution to identified sources (AIS) | yes |
| Tango (1998) | uottawa PDF, NIPH page | Stat. Med. 17(8):891–908 | score interval for paired proportion differences | yes |
| Thorndike (1920) | scanned PDF, catalogue | J. Appl. Psychol. 4(1):25–29 | halo error | yes |
| Thorne et al. (2018) | ACL Anthology N18-1074 | NAACL 2018, pp. 809–819 | supported / refuted / NEI verdicts | yes |
| Turpin et al. (2023) | NeurIPS 2023 poster page, arXiv 2305.04388 | NeurIPS 2023 | stated reasons can diverge from what drives answers | yes |
| Welfare Quality® (2009) | WUR e-depot | poultry protocol, Lelystad, 2009 | animal-based welfare measures | yes |

**Removed:** Wilson (1927). The analysis no longer uses Wilson intervals; V1–V3 use a case-level t interval (`analyze_p2.py`, commit 6c0afb3).
