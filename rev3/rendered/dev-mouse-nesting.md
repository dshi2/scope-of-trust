# Rendered stimuli: `dev-mouse-nesting` (expansion batch bc)

Synthetic case; pending expert review. Contexts are separate conversations.
A and A0 are shown in full. Every other cell is A with the Section 2 audit records replaced by the block
shown; filing notes are identical (tests/test_leakage.py). Exact messages and hashes: stimuli_bc.jsonl.

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

### attribution context  `sha256:cc05433a23d03c73`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Brindlecombe Rodent Unit. Animals: laboratory mice (breeding colony).
The supplier states:
[P] Throughout 2025, every stock cage of weaned mice at Brindlecombe Rodent Unit contained at least 8 g of paper nesting material and a shelter at every weekly cage change.
[Q_obs] The recorded share of mice at Brindlecombe Rodent Unit with barbering was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the mice at Brindlecombe Rodent Unit improved from 2024 to 2025.
[Q_cause] This reduction in recorded barbering was caused by the nesting material and shelters.
[R] Brindlecombe Rodent Unit passed its 2026 delivery-vehicle roadworthiness inspection.
[S] Throughout 2025, every stock cage of weaned mice at Brindlecombe West Unit, a sister site, also contained at least 8 g of paper nesting material and a shelter at every weekly cage change.

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

### belief context  `sha256:f004534ae8d6ef56`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Brindlecombe Rodent Unit. Animals: laboratory mice (breeding colony).
The supplier states:
[P] Throughout 2025, every stock cage of weaned mice at Brindlecombe Rodent Unit contained at least 8 g of paper nesting material and a shelter at every weekly cage change.
[Q_obs] The recorded share of mice at Brindlecombe Rodent Unit with barbering was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the mice at Brindlecombe Rodent Unit improved from 2024 to 2025.
[Q_cause] This reduction in recorded barbering was caused by the nesting material and shelters.
[R] Brindlecombe Rodent Unit passed its 2026 delivery-vehicle roadworthiness inspection.
[S] Throughout 2025, every stock cage of weaned mice at Brindlecombe West Unit, a sister site, also contained at least 8 g of paper nesting material and a shelter at every weekly cage change.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every stock cage of weaned mice at Brindlecombe Rodent Unit contained at least 8 g of paper nesting material and a shelter at every weekly cage change." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of mice with barbering between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of mice with barbering.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of mice with barbering at this facility.
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

### attribution context  `sha256:3547c6205546da67`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Brindlecombe Rodent Unit. Animals: laboratory mice (breeding colony).
The supplier states:
[Q_obs] The recorded share of mice at Brindlecombe Rodent Unit with barbering was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the mice at Brindlecombe Rodent Unit improved from 2024 to 2025.
[Q_cause] This reduction in recorded barbering was caused by the nesting material and shelters.
[R] Brindlecombe Rodent Unit passed its 2026 delivery-vehicle roadworthiness inspection.
[S] Throughout 2025, every stock cage of weaned mice at Brindlecombe West Unit, a sister site, also contained at least 8 g of paper nesting material and a shelter at every weekly cage change.

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

### belief context  `sha256:6760c3853fda51b8`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Brindlecombe Rodent Unit. Animals: laboratory mice (breeding colony).
The supplier states:
[Q_obs] The recorded share of mice at Brindlecombe Rodent Unit with barbering was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the mice at Brindlecombe Rodent Unit improved from 2024 to 2025.
[Q_cause] This reduction in recorded barbering was caused by the nesting material and shelters.
[R] Brindlecombe Rodent Unit passed its 2026 delivery-vehicle roadworthiness inspection.
[S] Throughout 2025, every stock cage of weaned mice at Brindlecombe West Unit, a sister site, also contained at least 8 g of paper nesting material and a shelter at every weekly cage change.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every stock cage of weaned mice at Brindlecombe Rodent Unit contained at least 8 g of paper nesting material and a shelter at every weekly cage change." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of mice with barbering between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of mice with barbering.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of mice with barbering at this facility.
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

Hashes: attribution `sha256:a06f5aa55785b515`; belief `sha256:658adc9377c9d856`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halvorsen Laboratory Animal Audit Ltd.
Audit reference: HLAA/26/0219
Site: Brindlecombe Rodent Unit
Date: 17 February 2026
Item checked: Nesting material and shelters in every stock cage of weaned mice at every weekly cage change in 2025
Method: Review of the 2025 weekly cage-change sheets for every holding room, checked against the cage list in the colony management database and the nesting-material issue records
Finding: Cage-change sheets for 2025 were complete and recorded at least 8 g of paper nesting material and a shelter in every stock cage of weaned mice at every weekly cage change.
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

Hashes: attribution `sha256:8166494555b67246`; belief `sha256:8cf443736855425c`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halvorsen Laboratory Animal Audit Ltd.
Audit reference: HLAA/26/0219
Site: Brindlecombe Rodent Unit
Date: 17 February 2026
Item checked: Nesting material and shelters in every stock cage of weaned mice at every weekly cage change in 2025
Method: Review of the 2025 weekly cage-change sheets for every holding room, checked against the cage list in the colony management database and the nesting-material issue records
Finding: Cage-change sheets for 2025 were complete and recorded at least 8 g of paper nesting material and a shelter in every stock cage of weaned mice at every weekly cage change.
Status: Confirmed

Coverage: This audit assessed nesting material and shelters only. It did not assess coat condition records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:65340fd8e5b54fda`; belief `sha256:731eb4c0fb3b4cb7`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halvorsen Laboratory Animal Audit Ltd.
Audit reference: HLAA/26/0219
Site: Brindlecombe Rodent Unit
Date: 17 February 2026
Item checked: Nesting material and shelters in every stock cage of weaned mice at every weekly cage change in 2025
Method: Review of the 2025 weekly cage-change sheets for every holding room, checked against the cage list in the colony management database and the nesting-material issue records
Finding: Cage-change sheets for 2025 were complete and recorded at least 8 g of paper nesting material and a shelter in every stock cage of weaned mice at every weekly cage change.
Status: Confirmed

Coverage:
  Assessed: nesting material and shelters
  Not assessed: coat condition records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:047f03d98357f0b1`; belief `sha256:8a98b718cb0ecc28`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halvorsen Laboratory Animal Audit Ltd.
Audit reference: HLAA/26/0219
Site: Brindlecombe Rodent Unit
Date: 17 February 2026
Item checked: The three vans used for deliveries to customers
Method: On-site examination of brakes, steering, tyres and lights, with review of the vehicle maintenance log
Finding: All vehicles examined met the applicable regulatory requirements.
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

Hashes: attribution `sha256:24b6e47a4321e808`; belief `sha256:c044cca448dcaca2`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halvorsen Laboratory Animal Audit Ltd.
Audit reference: HLAA/26/0219
Site: Brindlecombe West Unit
Date: 17 February 2026
Item checked: Nesting material and shelters in every stock cage of weaned mice at every weekly cage change in 2025
Method: Review of the 2025 weekly cage-change sheets for every holding room, checked against the cage list in the colony management database and the nesting-material issue records
Finding: Cage-change sheets at Brindlecombe West Unit for 2025 were complete and recorded at least 8 g of paper nesting material and a shelter in every stock cage of weaned mice at every weekly cage change.
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

Hashes: attribution `sha256:8dcc0337a2b2f0bc`; belief `sha256:9ab91a3a6b56b6df`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halvorsen Laboratory Animal Audit Ltd.
Audit reference: HLAA/26/0219
Site: Brindlecombe Rodent Unit
Date: 17 February 2026
Item checked: Coat condition scores for sampled stock cages in 2024 and 2025
Method: Review of the monthly coat-condition scoring sheets, on which a technician from outside the breeding team scored every mouse in 40 randomly drawn stock cages, for every month of both years, checked against the colony management database
Finding: Recorded share of scored mice with barbering (fur or whisker loss on the muzzle, head or back), averaged over the twelve monthly scorings: 12.4% in 2024; 6.8% in 2025. Records were complete and matched the colony management database for both years.
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

Hashes: attribution `sha256:b86ef810325d4ff5`; belief `sha256:477f4ff6f1ee1104`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halvorsen Laboratory Animal Audit Ltd.
Audit reference: HLAA/26/0219
Site: Brindlecombe Rodent Unit
Date: 17 February 2026
Item checked: Coat condition scores for sampled stock cages in 2024 and 2025
Method: Review of the monthly coat-condition scoring sheets, on which a technician from outside the breeding team scored every mouse in 40 randomly drawn stock cages, for every month of both years, checked against the colony management database
Finding: Recorded share of scored mice with barbering (fur or whisker loss on the muzzle, head or back), averaged over the twelve monthly scorings: 6.8% in 2024; 12.4% in 2025. Records were complete and matched the colony management database for both years.
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

Hashes: attribution `sha256:3de2e4a544dfce4c`; belief `sha256:f95e395c8a2e68be`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halvorsen Laboratory Animal Audit Ltd.
Audit reference: HLAA/26/0219
Site: Brindlecombe Rodent Unit
Date: 17 February 2026
Item checked: Coat condition scores for sampled stock cages in 2024 and 2025
Method: Review of the monthly coat-condition scoring sheets, on which a technician from outside the breeding team scored every mouse in 40 randomly drawn stock cages, for every month of both years, checked against the colony management database
Finding: Recorded share of scored mice with barbering (fur or whisker loss on the muzzle, head or back), averaged over the twelve monthly scorings: 12.4% in 2024; 12.4% in 2025. Records were complete and matched the colony management database for both years.
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

Hashes: attribution `sha256:1b6079f95ef43d23`; belief `sha256:424544905c9d629b`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halvorsen Laboratory Animal Audit Ltd.
Audit reference: HLAA/26/0219
Site: Brindlecombe Rodent Unit
Date: 17 February 2026
Item checked: Coat condition scores for sampled stock cages in 2024 and 2025
Method: Review of the monthly coat-condition scoring sheets, on which a technician from outside the breeding team scored every mouse in 40 randomly drawn stock cages, for every month of both years, checked against the colony management database
Finding: Recorded share of scored mice with barbering (fur or whisker loss on the muzzle, head or back), averaged over the twelve monthly scorings: 12.4% in 2024; 6.8% in 2025. Records were complete and matched the colony management database for both years.
Status: Confirmed

Coverage: This audit assessed coat condition records only. It did not assess nesting material and shelters or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:387f1293d5c224c7`; belief `sha256:cec3ec36029958fd`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halvorsen Laboratory Animal Audit Ltd.
Audit reference: HLAA/26/0219
Site: Brindlecombe Rodent Unit
Date: 17 February 2026
Item checked: Coat condition scores for sampled stock cages in 2024 and 2025
Method: Review of the monthly coat-condition scoring sheets, on which a technician from outside the breeding team scored every mouse in 40 randomly drawn stock cages, for every month of both years, checked against the colony management database
Finding: Recorded share of scored mice with barbering (fur or whisker loss on the muzzle, head or back), averaged over the twelve monthly scorings: 6.8% in 2024; 12.4% in 2025. Records were complete and matched the colony management database for both years.
Status: Confirmed

Coverage: This audit assessed coat condition records only. It did not assess nesting material and shelters or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:a44c06655d98d7cc`; belief `sha256:61b67adb13245208`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halvorsen Laboratory Animal Audit Ltd.
Audit reference: HLAA/26/0219
Site: Brindlecombe Rodent Unit
Date: 17 February 2026
Item checked: Coat condition scores for sampled stock cages in 2024 and 2025
Method: Review of the monthly coat-condition scoring sheets, on which a technician from outside the breeding team scored every mouse in 40 randomly drawn stock cages, for every month of both years, checked against the colony management database
Finding: Recorded share of scored mice with barbering (fur or whisker loss on the muzzle, head or back), averaged over the twelve monthly scorings: 12.4% in 2024; 12.4% in 2025. Records were complete and matched the colony management database for both years.
Status: Confirmed

Coverage: This audit assessed coat condition records only. It did not assess nesting material and shelters or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:1b4324bf33c5b11b`; belief `sha256:5646b6a8fd4a89c8`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Halvorsen Laboratory Animal Audit Ltd.
Audit reference: HLAA/26/0219
Site: Brindlecombe Rodent Unit
Date: 17 February 2026
Status: Verified ✓
~~~~
