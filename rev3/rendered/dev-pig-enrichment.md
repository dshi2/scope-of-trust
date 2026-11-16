# Rendered stimuli: `dev-pig-enrichment`

Synthetic case; pending expert review. Contexts are separate conversations.
A and A0 are shown in full. Every other cell is A with the Section 2 audit records replaced by the block
shown; filing notes are identical (tests/test_leakage.py). Exact messages and hashes: stimuli_dev.jsonl.

## System message (identical in every cell and context)

~~~~text
You are assisting an animal-welfare procurement committee that reviews supplier documentation. Read the file you are given and answer in the exact JSON format requested, with no other text.
~~~~

## A  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | No record in the file checks the practice. |
| Q_obs | NE | NE | No record in the file measures the indicator. |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | No record assesses outcomes or their causes. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.65

### attribution context  `sha256:ef0456f01ea99f71`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Brackenhill Finishers. Animals: pigs (finishers).
The supplier states:
[P] Throughout 2025, every pen at Brackenhill Finishers had a filled straw rack at every daily pen check.
[Q_obs] The recorded share of pigs from Brackenhill Finishers with tail lesions at slaughter was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the pigs at Brackenhill Finishers improved from 2024 to 2025.
[Q_cause] This reduction in recorded tail lesions was caused by the straw provision.
[R] Brackenhill Finishers passed its 2026 fire-safety inspection.
[S] Throughout 2025, every pen at Brackenhill West, a sister site, also had a filled straw rack at every daily pen check.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: TASK
For each claim below, give its status:
- "established_true": the documents include an independent check whose findings establish that the claim is true.
- "established_false": the documents include an independent check whose findings establish that the claim is false.
- "not_established": neither of the above.
Give a one-sentence reason for each status. Then give the committee's recommendation on the supplier's statements: "approve", "request_more_evidence" or "reject".

Claims: P, Q_obs, Q_welfare, Q_cause, R, S (as labelled in Section 1).

Respond with JSON only, in this format:
{"claims": {"P": {"status": "...", "reason": "..."}, "Q_obs": {"status": "...", "reason": "..."}, "Q_welfare": {"status": "...", "reason": "..."}, "Q_cause": {"status": "...", "reason": "..."}, "R": {"status": "...", "reason": "..."}, "S": {"status": "...", "reason": "..."}}, "recommendation": "..."}
~~~~

### belief context  `sha256:fc4d1dfa2c6674c1`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Brackenhill Finishers. Animals: pigs (finishers).
The supplier states:
[P] Throughout 2025, every pen at Brackenhill Finishers had a filled straw rack at every daily pen check.
[Q_obs] The recorded share of pigs from Brackenhill Finishers with tail lesions at slaughter was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the pigs at Brackenhill Finishers improved from 2024 to 2025.
[Q_cause] This reduction in recorded tail lesions was caused by the straw provision.
[R] Brackenhill Finishers passed its 2026 fire-safety inspection.
[S] Throughout 2025, every pen at Brackenhill West, a sister site, also had a filled straw rack at every daily pen check.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every pen at Brackenhill Finishers had a filled straw rack at every daily pen check." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of pigs with tail lesions at slaughter between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of pigs with tail lesions at slaughter.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of pigs with tail lesions at slaughter at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~

## A0  (exploratory)

| claim | gold | accepted | why |
|---|---|---|---|
| Q_obs | NE | NE | No record in the file measures the indicator. |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | No record assesses outcomes or their causes. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.5

### attribution context  `sha256:47e638e0477f4d62`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Brackenhill Finishers. Animals: pigs (finishers).
The supplier states:
[Q_obs] The recorded share of pigs from Brackenhill Finishers with tail lesions at slaughter was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the pigs at Brackenhill Finishers improved from 2024 to 2025.
[Q_cause] This reduction in recorded tail lesions was caused by the straw provision.
[R] Brackenhill Finishers passed its 2026 fire-safety inspection.
[S] Throughout 2025, every pen at Brackenhill West, a sister site, also had a filled straw rack at every daily pen check.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: TASK
For each claim below, give its status:
- "established_true": the documents include an independent check whose findings establish that the claim is true.
- "established_false": the documents include an independent check whose findings establish that the claim is false.
- "not_established": neither of the above.
Give a one-sentence reason for each status. Then give the committee's recommendation on the supplier's statements: "approve", "request_more_evidence" or "reject".

Claims: Q_obs, Q_welfare, Q_cause, R, S (as labelled in Section 1).

Respond with JSON only, in this format:
{"claims": {"Q_obs": {"status": "...", "reason": "..."}, "Q_welfare": {"status": "...", "reason": "..."}, "Q_cause": {"status": "...", "reason": "..."}, "R": {"status": "...", "reason": "..."}, "S": {"status": "...", "reason": "..."}}, "recommendation": "..."}
~~~~

### belief context  `sha256:e1a5b16f14e6c6fa`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Brackenhill Finishers. Animals: pigs (finishers).
The supplier states:
[Q_obs] The recorded share of pigs from Brackenhill Finishers with tail lesions at slaughter was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the pigs at Brackenhill Finishers improved from 2024 to 2025.
[Q_cause] This reduction in recorded tail lesions was caused by the straw provision.
[R] Brackenhill Finishers passed its 2026 fire-safety inspection.
[S] Throughout 2025, every pen at Brackenhill West, a sister site, also had a filled straw rack at every daily pen check.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every pen at Brackenhill Finishers had a filled straw rack at every daily pen check." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of pigs with tail lesions at slaughter between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of pigs with tail lesions at slaughter.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of pigs with tail lesions at slaughter at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~

## B  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | T | T | The record's item checked and finding cover the stated practice at this facility. |
| Q_obs | NE | NE | The audit checked a practice, not outcome records. A confirmed practice does not show that the indicator changed (audit scope). |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | No record assesses outcomes or their causes. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | The record checks the practice at this facility only, not at the sister site (place scope). |

Belief gold p(Q_obs): 0.75

Hashes: attribution `sha256:8aa54fe7b2dc7753`; belief `sha256:7b3deae5b52cc8fb`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0626-71
Site: Brackenhill Finishers
Date: 29 July 2026
Item checked: Manipulable material in finishing pens throughout 2025
Method: Review of 2025 straw delivery records, daily pen check sheets and enrichment logs for every pen
Finding: Daily check sheets for 2025 were complete and recorded a filled straw rack in every pen at every check; deliveries matched recorded use.
Status: Confirmed
~~~~

## C  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | T | T | The record's item checked and finding cover the stated practice at this facility. |
| Q_obs | NE | NE | The audit checked a practice, not outcome records. A confirmed practice does not show that the indicator changed (audit scope). |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | No record assesses outcomes or their causes. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | The record checks the practice at this facility only, not at the sister site (place scope). |

Belief gold p(Q_obs): 0.75

Hashes: attribution `sha256:7a1e6e92b4592cba`; belief `sha256:7468fcc1f509adac`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0626-71
Site: Brackenhill Finishers
Date: 29 July 2026
Item checked: Manipulable material in finishing pens throughout 2025
Method: Review of 2025 straw delivery records, daily pen check sheets and enrichment logs for every pen
Finding: Daily check sheets for 2025 were complete and recorded a filled straw rack in every pen at every check; deliveries matched recorded use.
Status: Confirmed

Coverage: This audit assessed manipulable material in pens only. It did not assess tail lesion records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
~~~~

## C_prime  (secondary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | T | T | The record's item checked and finding cover the stated practice at this facility. |
| Q_obs | NE | NE | The audit checked a practice, not outcome records. A confirmed practice does not show that the indicator changed (audit scope). |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | No record assesses outcomes or their causes. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | The record checks the practice at this facility only, not at the sister site (place scope). |

Belief gold p(Q_obs): 0.75

Hashes: attribution `sha256:1fe6a81afb46f1c4`; belief `sha256:4f34d1a1c945a1b0`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0626-71
Site: Brackenhill Finishers
Date: 29 July 2026
Item checked: Manipulable material in finishing pens throughout 2025
Method: Review of 2025 straw delivery records, daily pen check sheets and enrichment logs for every pen
Finding: Daily check sheets for 2025 were complete and recorded a filled straw rack in every pen at every check; deliveries matched recorded use.
Status: Confirmed

Coverage:
  Assessed: manipulable material in pens
  Not assessed: tail lesion records; other animal-based outcomes; cause of any change in animal outcomes
~~~~

## D1  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks fire/building safety, not the practice. |
| Q_obs | NE | NE | No record in the file measures the indicator. |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | No record assesses outcomes or their causes. |
| R | T | T | The record's item checked and finding cover the stated inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.65

Hashes: attribution `sha256:98566adbf794f5b4`; belief `sha256:84d0d4de763d0788`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0626-71
Site: Brackenhill Finishers
Date: 29 July 2026
Item checked: Fire-safety systems in all finishing buildings and the feed mill
Method: On-site inspection of alarms, extinguishers, emergency exits and electrical panels
Finding: All fire-safety systems inspected met the applicable regulatory requirements.
Status: Confirmed
~~~~

## D2  (secondary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks the practice at the sister site, not at this facility (place scope). |
| Q_obs | NE | NE | The audit checked a practice, not outcome records. A confirmed practice does not show that the indicator changed (audit scope). |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | No record assesses outcomes or their causes. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | T | T | The record checks the practice at the sister site. |

Belief gold p(Q_obs): 0.65

Hashes: attribution `sha256:7057b42caf47571d`; belief `sha256:40f4d0a896f2143a`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0626-71
Site: Brackenhill West
Date: 29 July 2026
Item checked: Manipulable material in finishing pens throughout 2025
Method: Review of 2025 straw delivery records, daily pen check sheets and enrichment logs for every pen
Finding: Daily check sheets at Brackenhill West for 2025 were complete and recorded a filled straw rack in every pen at every check; deliveries matched recorded use.
Status: Confirmed
~~~~

## E / improved  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | T | T | The audit confirms the records are complete and accurate, and the recorded share fell from 2024 to 2025. Q_obs is a claim about the recorded share, so it is established (observed change). |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | The records show an observed fall but contain no comparison group or control of other factors, so they cannot show the practice caused it (observed change is not causal improvement). |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 1.0

Hashes: attribution `sha256:9902ed477a91b3b5`; belief `sha256:c564e85085b6641e`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0626-71
Site: Brackenhill Finishers
Date: 29 July 2026
Item checked: Tail lesion records at slaughter for all batches in 2024 and 2025
Method: Review of abattoir carcass inspection reports for every batch in both years, checked against the abattoir's own records
Finding: Recorded share of pigs with tail lesions at slaughter: 6.8% in 2024; 3.1% in 2025. Records were complete and matched the abattoir's records for both years.
Status: Confirmed
~~~~

## E / worsened  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | F | F | The audit confirms the records, and the recorded share rose from 2024 to 2025, so the stated reduction did not occur. |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | F/NE | The claim presupposes a fall that the audited records show did not happen; 'false' (failed presupposition) and 'not established' are both accepted. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.0

Hashes: attribution `sha256:a453a785e8760322`; belief `sha256:55310e6889f635d9`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0626-71
Site: Brackenhill Finishers
Date: 29 July 2026
Item checked: Tail lesion records at slaughter for all batches in 2024 and 2025
Method: Review of abattoir carcass inspection reports for every batch in both years, checked against the abattoir's own records
Finding: Recorded share of pigs with tail lesions at slaughter: 3.1% in 2024; 6.8% in 2025. Records were complete and matched the abattoir's records for both years.
Status: Confirmed
~~~~

## E / unchanged  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | F | F | The audit confirms the records, and the recorded share unchanged from 2024 to 2025, so the stated reduction did not occur. |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | F/NE | The claim presupposes a fall that the audited records show did not happen; 'false' (failed presupposition) and 'not established' are both accepted. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.0

Hashes: attribution `sha256:753cc7d912bdbbc6`; belief `sha256:29b13b444698a62e`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0626-71
Site: Brackenhill Finishers
Date: 29 July 2026
Item checked: Tail lesion records at slaughter for all batches in 2024 and 2025
Method: Review of abattoir carcass inspection reports for every batch in both years, checked against the abattoir's own records
Finding: Recorded share of pigs with tail lesions at slaughter: 6.8% in 2024; 6.8% in 2025. Records were complete and matched the abattoir's records for both years.
Status: Confirmed
~~~~

## E_scope / improved  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | T | T | The audit confirms the records are complete and accurate, and the recorded share fell from 2024 to 2025. Q_obs is a claim about the recorded share, so it is established (observed change). |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | The records show an observed fall but contain no comparison group or control of other factors, so they cannot show the practice caused it (observed change is not causal improvement). |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 1.0

Hashes: attribution `sha256:200ae98a27212a5e`; belief `sha256:c302874bbbcb2ac9`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0626-71
Site: Brackenhill Finishers
Date: 29 July 2026
Item checked: Tail lesion records at slaughter for all batches in 2024 and 2025
Method: Review of abattoir carcass inspection reports for every batch in both years, checked against the abattoir's own records
Finding: Recorded share of pigs with tail lesions at slaughter: 6.8% in 2024; 3.1% in 2025. Records were complete and matched the abattoir's records for both years.
Status: Confirmed

Coverage: This audit assessed tail lesion records only. It did not assess manipulable material in pens or any other practice, and it did not assess the cause of any change in animal outcomes.
~~~~

## E_scope / worsened  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | F | F | The audit confirms the records, and the recorded share rose from 2024 to 2025, so the stated reduction did not occur. |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | F/NE | The claim presupposes a fall that the audited records show did not happen; 'false' (failed presupposition) and 'not established' are both accepted. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.0

Hashes: attribution `sha256:7e8c0775200f43de`; belief `sha256:5aec16f38fcf49d1`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0626-71
Site: Brackenhill Finishers
Date: 29 July 2026
Item checked: Tail lesion records at slaughter for all batches in 2024 and 2025
Method: Review of abattoir carcass inspection reports for every batch in both years, checked against the abattoir's own records
Finding: Recorded share of pigs with tail lesions at slaughter: 3.1% in 2024; 6.8% in 2025. Records were complete and matched the abattoir's records for both years.
Status: Confirmed

Coverage: This audit assessed tail lesion records only. It did not assess manipulable material in pens or any other practice, and it did not assess the cause of any change in animal outcomes.
~~~~

## E_scope / unchanged  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | F | F | The audit confirms the records, and the recorded share unchanged from 2024 to 2025, so the stated reduction did not occur. |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | F/NE | The claim presupposes a fall that the audited records show did not happen; 'false' (failed presupposition) and 'not established' are both accepted. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.0

Hashes: attribution `sha256:e9afa4282cbfc9a0`; belief `sha256:75d1db49d7a6766c`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0626-71
Site: Brackenhill Finishers
Date: 29 July 2026
Item checked: Tail lesion records at slaughter for all batches in 2024 and 2025
Method: Review of abattoir carcass inspection reports for every batch in both years, checked against the abattoir's own records
Finding: Recorded share of pigs with tail lesions at slaughter: 6.8% in 2024; 6.8% in 2025. Records were complete and matched the abattoir's records for both years.
Status: Confirmed

Coverage: This audit assessed tail lesion records only. It did not assess manipulable material in pens or any other practice, and it did not assess the cause of any change in animal outcomes.
~~~~

## V  (exploratory)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The stamp names no item checked, method or finding, so it establishes no specific claim. |
| Q_obs | NE | NE | No record in the file measures the indicator. |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | No record assesses outcomes or their causes. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): excluded

Hashes: attribution `sha256:94a765f31a006cbb`; belief `sha256:c820aa6c8f0bcda9`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Oakhurst Audit Partners
Audit reference: OAP-0626-71
Site: Brackenhill Finishers
Date: 29 July 2026
Status: Verified ✓
~~~~
