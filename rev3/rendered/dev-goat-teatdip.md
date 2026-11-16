# Rendered stimuli: `dev-goat-teatdip` (expansion batch ba)

Synthetic case; pending expert review. Contexts are separate conversations.
A and A0 are shown in full. Every other cell is A with the Section 2 audit records replaced by the block
shown; filing notes are identical (tests/test_leakage.py). Exact messages and hashes: stimuli_ba.jsonl.

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

### attribution context  `sha256:27e58bb05906d9f2`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Oakenshaw Goat Dairy. Animals: dairy goats.
The supplier states:
[P] Throughout 2025, the parlour log at Oakenshaw Goat Dairy recorded post-milking teat disinfection of every milking group at every milking.
[Q_obs] The recorded share of milking does at Oakenshaw Goat Dairy treated for clinical mastitis was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the goats at Oakenshaw Goat Dairy improved from 2024 to 2025.
[Q_cause] This reduction in recorded mastitis treatments was caused by the post-milking teat disinfection.
[R] Oakenshaw Goat Dairy passed its 2026 roof-structure inspection.
[S] Throughout 2025, the parlour log at Oakenshaw Fold, a sister site, also recorded post-milking teat disinfection of every milking group at every milking.

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

### belief context  `sha256:4f7223ae6b6b56f4`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Oakenshaw Goat Dairy. Animals: dairy goats.
The supplier states:
[P] Throughout 2025, the parlour log at Oakenshaw Goat Dairy recorded post-milking teat disinfection of every milking group at every milking.
[Q_obs] The recorded share of milking does at Oakenshaw Goat Dairy treated for clinical mastitis was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the goats at Oakenshaw Goat Dairy improved from 2024 to 2025.
[Q_cause] This reduction in recorded mastitis treatments was caused by the post-milking teat disinfection.
[R] Oakenshaw Goat Dairy passed its 2026 roof-structure inspection.
[S] Throughout 2025, the parlour log at Oakenshaw Fold, a sister site, also recorded post-milking teat disinfection of every milking group at every milking.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, the parlour log at Oakenshaw Goat Dairy recorded post-milking teat disinfection of every milking group at every milking." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of milking does treated for clinical mastitis between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of milking does treated for clinical mastitis.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of milking does treated for clinical mastitis at this facility.
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

### attribution context  `sha256:2ae11948122ef57e`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Oakenshaw Goat Dairy. Animals: dairy goats.
The supplier states:
[Q_obs] The recorded share of milking does at Oakenshaw Goat Dairy treated for clinical mastitis was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the goats at Oakenshaw Goat Dairy improved from 2024 to 2025.
[Q_cause] This reduction in recorded mastitis treatments was caused by the post-milking teat disinfection.
[R] Oakenshaw Goat Dairy passed its 2026 roof-structure inspection.
[S] Throughout 2025, the parlour log at Oakenshaw Fold, a sister site, also recorded post-milking teat disinfection of every milking group at every milking.

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

### belief context  `sha256:221742ce2c3afa67`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Oakenshaw Goat Dairy. Animals: dairy goats.
The supplier states:
[Q_obs] The recorded share of milking does at Oakenshaw Goat Dairy treated for clinical mastitis was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the goats at Oakenshaw Goat Dairy improved from 2024 to 2025.
[Q_cause] This reduction in recorded mastitis treatments was caused by the post-milking teat disinfection.
[R] Oakenshaw Goat Dairy passed its 2026 roof-structure inspection.
[S] Throughout 2025, the parlour log at Oakenshaw Fold, a sister site, also recorded post-milking teat disinfection of every milking group at every milking.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, the parlour log at Oakenshaw Goat Dairy recorded post-milking teat disinfection of every milking group at every milking." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of milking does treated for clinical mastitis between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of milking does treated for clinical mastitis.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of milking does treated for clinical mastitis at this facility.
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

Hashes: attribution `sha256:9c5c23b1e5fe9f03`; belief `sha256:cdbf1870d785db19`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Severnside Dairy Audit Ltd.
Audit reference: SDA/G/2026/058
Site: Oakenshaw Goat Dairy
Date: 5 May 2026
Item checked: Post-milking teat disinfection of every milking group at every milking recorded in the 2025 parlour log
Method: Review of the 2025 parlour log (two milkings a day), compared with the parlour software's 2025 milking-session list and with teat-disinfectant purchase and stock records for 2025
Finding: The 2025 parlour log recorded post-milking teat disinfection of every milking group at each of the 730 milkings in the session list; disinfectant purchases matched recorded use.
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

Hashes: attribution `sha256:f55c37f00b40f039`; belief `sha256:4f0ecd42fa6e2546`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Severnside Dairy Audit Ltd.
Audit reference: SDA/G/2026/058
Site: Oakenshaw Goat Dairy
Date: 5 May 2026
Item checked: Post-milking teat disinfection of every milking group at every milking recorded in the 2025 parlour log
Method: Review of the 2025 parlour log (two milkings a day), compared with the parlour software's 2025 milking-session list and with teat-disinfectant purchase and stock records for 2025
Finding: The 2025 parlour log recorded post-milking teat disinfection of every milking group at each of the 730 milkings in the session list; disinfectant purchases matched recorded use.
Status: Confirmed

Coverage: This audit assessed post-milking teat disinfection only. It did not assess mastitis treatment records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:5c7735e3fb5db2ab`; belief `sha256:e4428372e6f5c986`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Severnside Dairy Audit Ltd.
Audit reference: SDA/G/2026/058
Site: Oakenshaw Goat Dairy
Date: 5 May 2026
Item checked: Post-milking teat disinfection of every milking group at every milking recorded in the 2025 parlour log
Method: Review of the 2025 parlour log (two milkings a day), compared with the parlour software's 2025 milking-session list and with teat-disinfectant purchase and stock records for 2025
Finding: The 2025 parlour log recorded post-milking teat disinfection of every milking group at each of the 730 milkings in the session list; disinfectant purchases matched recorded use.
Status: Confirmed

Coverage:
  Assessed: post-milking teat disinfection
  Not assessed: mastitis treatment records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:88e19e9d30bf4ba4`; belief `sha256:0b38b69418a7ecd3`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Severnside Dairy Audit Ltd.
Audit reference: SDA/G/2026/058
Site: Oakenshaw Goat Dairy
Date: 5 May 2026
Item checked: Roof structures of the goat barn, the parlour building and the hay store
Method: On-site inspection of trusses, purlins, cladding fixings and roof-light panels
Finding: All roof structures inspected met the applicable regulatory requirements.
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

Hashes: attribution `sha256:5c0f2c5ed28c46d7`; belief `sha256:3aa402945ab990b7`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Severnside Dairy Audit Ltd.
Audit reference: SDA/G/2026/058
Site: Oakenshaw Fold
Date: 5 May 2026
Item checked: Post-milking teat disinfection of every milking group at every milking recorded in the 2025 parlour log
Method: Review of the 2025 parlour log (two milkings a day), compared with the parlour software's 2025 milking-session list and with teat-disinfectant purchase and stock records for 2025
Finding: The 2025 parlour log at Oakenshaw Fold recorded post-milking teat disinfection of every milking group at each of the 730 milkings in the session list; disinfectant purchases matched recorded use.
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

Hashes: attribution `sha256:982e66bf1789ef86`; belief `sha256:180fcf20d94df115`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Severnside Dairy Audit Ltd.
Audit reference: SDA/G/2026/058
Site: Oakenshaw Goat Dairy
Date: 5 May 2026
Item checked: Clinical mastitis treatment records for every doe in milk in 2024 and 2025
Method: Review of the farm medicine book and the herd vet's clinical visit notes for every doe in milk in both years, checked against the veterinary practice's prescription records and the milk-withdrawal log
Finding: Recorded share of does in milk treated at least once for clinical mastitis: 7.9% in 2024; 4.2% in 2025. Records were complete and matched the prescription records and withdrawal log for both years.
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

Hashes: attribution `sha256:d82f7cf11ca9b080`; belief `sha256:ac057468cf39571e`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Severnside Dairy Audit Ltd.
Audit reference: SDA/G/2026/058
Site: Oakenshaw Goat Dairy
Date: 5 May 2026
Item checked: Clinical mastitis treatment records for every doe in milk in 2024 and 2025
Method: Review of the farm medicine book and the herd vet's clinical visit notes for every doe in milk in both years, checked against the veterinary practice's prescription records and the milk-withdrawal log
Finding: Recorded share of does in milk treated at least once for clinical mastitis: 4.2% in 2024; 7.9% in 2025. Records were complete and matched the prescription records and withdrawal log for both years.
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

Hashes: attribution `sha256:a67f56994dcbebbf`; belief `sha256:5c40c57c70017d85`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Severnside Dairy Audit Ltd.
Audit reference: SDA/G/2026/058
Site: Oakenshaw Goat Dairy
Date: 5 May 2026
Item checked: Clinical mastitis treatment records for every doe in milk in 2024 and 2025
Method: Review of the farm medicine book and the herd vet's clinical visit notes for every doe in milk in both years, checked against the veterinary practice's prescription records and the milk-withdrawal log
Finding: Recorded share of does in milk treated at least once for clinical mastitis: 7.9% in 2024; 7.9% in 2025. Records were complete and matched the prescription records and withdrawal log for both years.
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

Hashes: attribution `sha256:b0189f6f012433ce`; belief `sha256:ba651fa71071ab99`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Severnside Dairy Audit Ltd.
Audit reference: SDA/G/2026/058
Site: Oakenshaw Goat Dairy
Date: 5 May 2026
Item checked: Clinical mastitis treatment records for every doe in milk in 2024 and 2025
Method: Review of the farm medicine book and the herd vet's clinical visit notes for every doe in milk in both years, checked against the veterinary practice's prescription records and the milk-withdrawal log
Finding: Recorded share of does in milk treated at least once for clinical mastitis: 7.9% in 2024; 4.2% in 2025. Records were complete and matched the prescription records and withdrawal log for both years.
Status: Confirmed

Coverage: This audit assessed mastitis treatment records only. It did not assess post-milking teat disinfection or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:6d95c49520f46855`; belief `sha256:0f41f66a01ae9ec7`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Severnside Dairy Audit Ltd.
Audit reference: SDA/G/2026/058
Site: Oakenshaw Goat Dairy
Date: 5 May 2026
Item checked: Clinical mastitis treatment records for every doe in milk in 2024 and 2025
Method: Review of the farm medicine book and the herd vet's clinical visit notes for every doe in milk in both years, checked against the veterinary practice's prescription records and the milk-withdrawal log
Finding: Recorded share of does in milk treated at least once for clinical mastitis: 4.2% in 2024; 7.9% in 2025. Records were complete and matched the prescription records and withdrawal log for both years.
Status: Confirmed

Coverage: This audit assessed mastitis treatment records only. It did not assess post-milking teat disinfection or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:2606ef6be5ae978b`; belief `sha256:e217b6d594ecaa7d`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Severnside Dairy Audit Ltd.
Audit reference: SDA/G/2026/058
Site: Oakenshaw Goat Dairy
Date: 5 May 2026
Item checked: Clinical mastitis treatment records for every doe in milk in 2024 and 2025
Method: Review of the farm medicine book and the herd vet's clinical visit notes for every doe in milk in both years, checked against the veterinary practice's prescription records and the milk-withdrawal log
Finding: Recorded share of does in milk treated at least once for clinical mastitis: 7.9% in 2024; 7.9% in 2025. Records were complete and matched the prescription records and withdrawal log for both years.
Status: Confirmed

Coverage: This audit assessed mastitis treatment records only. It did not assess post-milking teat disinfection or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:e671ba4aec9a8aef`; belief `sha256:7a05cf6b5fe7764a`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Severnside Dairy Audit Ltd.
Audit reference: SDA/G/2026/058
Site: Oakenshaw Goat Dairy
Date: 5 May 2026
Status: Verified ✓
~~~~
