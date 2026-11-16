# Rendered stimuli: `dev-sleddog-rest` (expansion batch bc)

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

### attribution context  `sha256:57de483e9d1ec193`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Tornfjell Husky Tours. Animals: working sled dogs.
The supplier states:
[P] Throughout 2025, every dog on the working roster at Tornfjell Husky Tours ran on no more than five days in any week.
[Q_obs] The recorded share of rostered dogs at Tornfjell Husky Tours treated for lameness or muscle strain was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the dogs at Tornfjell Husky Tours improved from 2024 to 2025.
[Q_cause] This reduction in recorded lameness and muscle-strain treatments was caused by the limit on running days.
[R] Tornfjell Husky Tours passed its 2026 snowmobile safety inspection.
[S] Throughout 2025, every dog on the working roster at Tornfjell Lower Yard, a sister site, also ran on no more than five days in any week.

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

### belief context  `sha256:a4d6ea440adcc814`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Tornfjell Husky Tours. Animals: working sled dogs.
The supplier states:
[P] Throughout 2025, every dog on the working roster at Tornfjell Husky Tours ran on no more than five days in any week.
[Q_obs] The recorded share of rostered dogs at Tornfjell Husky Tours treated for lameness or muscle strain was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the dogs at Tornfjell Husky Tours improved from 2024 to 2025.
[Q_cause] This reduction in recorded lameness and muscle-strain treatments was caused by the limit on running days.
[R] Tornfjell Husky Tours passed its 2026 snowmobile safety inspection.
[S] Throughout 2025, every dog on the working roster at Tornfjell Lower Yard, a sister site, also ran on no more than five days in any week.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every dog on the working roster at Tornfjell Husky Tours ran on no more than five days in any week." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of rostered dogs treated for lameness or muscle strain between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of rostered dogs treated for lameness or muscle strain.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of rostered dogs treated for lameness or muscle strain at this facility.
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

### attribution context  `sha256:9c66cf258d47b07a`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Tornfjell Husky Tours. Animals: working sled dogs.
The supplier states:
[Q_obs] The recorded share of rostered dogs at Tornfjell Husky Tours treated for lameness or muscle strain was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the dogs at Tornfjell Husky Tours improved from 2024 to 2025.
[Q_cause] This reduction in recorded lameness and muscle-strain treatments was caused by the limit on running days.
[R] Tornfjell Husky Tours passed its 2026 snowmobile safety inspection.
[S] Throughout 2025, every dog on the working roster at Tornfjell Lower Yard, a sister site, also ran on no more than five days in any week.

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

### belief context  `sha256:8a27c7d3edaed5c3`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Tornfjell Husky Tours. Animals: working sled dogs.
The supplier states:
[Q_obs] The recorded share of rostered dogs at Tornfjell Husky Tours treated for lameness or muscle strain was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the dogs at Tornfjell Husky Tours improved from 2024 to 2025.
[Q_cause] This reduction in recorded lameness and muscle-strain treatments was caused by the limit on running days.
[R] Tornfjell Husky Tours passed its 2026 snowmobile safety inspection.
[S] Throughout 2025, every dog on the working roster at Tornfjell Lower Yard, a sister site, also ran on no more than five days in any week.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every dog on the working roster at Tornfjell Husky Tours ran on no more than five days in any week." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of rostered dogs treated for lameness or muscle strain between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of rostered dogs treated for lameness or muscle strain.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of rostered dogs treated for lameness or muscle strain at this facility.
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

Hashes: attribution `sha256:1a7f43074c3fdcf8`; belief `sha256:95d13fe5f1ff85fa`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordkalott Tourism Animal Audit AB
Audit reference: NTAA-26-0158
Site: Tornfjell Husky Tours
Date: 14 August 2026
Item checked: Running days of every dog on the working roster in every week of 2025
Method: Review of the 2025 daily run sheets listing the dogs in every team, for every week of the year, checked against the kennel roster and the GPS logs of every run
Finding: Run sheets for 2025 were complete; no dog on the working roster ran on more than five days in any week of 2025.
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

Hashes: attribution `sha256:4fe9a49f21d34bcd`; belief `sha256:74920d21d9035849`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordkalott Tourism Animal Audit AB
Audit reference: NTAA-26-0158
Site: Tornfjell Husky Tours
Date: 14 August 2026
Item checked: Running days of every dog on the working roster in every week of 2025
Method: Review of the 2025 daily run sheets listing the dogs in every team, for every week of the year, checked against the kennel roster and the GPS logs of every run
Finding: Run sheets for 2025 were complete; no dog on the working roster ran on more than five days in any week of 2025.
Status: Confirmed

Coverage: This audit assessed running days on the working roster only. It did not assess veterinary treatment records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:4e781c9891d72ff6`; belief `sha256:7de8917ca92f870d`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordkalott Tourism Animal Audit AB
Audit reference: NTAA-26-0158
Site: Tornfjell Husky Tours
Date: 14 August 2026
Item checked: Running days of every dog on the working roster in every week of 2025
Method: Review of the 2025 daily run sheets listing the dogs in every team, for every week of the year, checked against the kennel roster and the GPS logs of every run
Finding: Run sheets for 2025 were complete; no dog on the working roster ran on more than five days in any week of 2025.
Status: Confirmed

Coverage:
  Assessed: running days on the working roster
  Not assessed: veterinary treatment records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:c293096e7b908275`; belief `sha256:410a027ee154e110`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordkalott Tourism Animal Audit AB
Audit reference: NTAA-26-0158
Site: Tornfjell Husky Tours
Date: 14 August 2026
Item checked: The four guide snowmobiles and their passenger trailers
Method: On-site examination of brakes, lights, throttle cut-outs and trailer hitches
Finding: All snowmobiles and trailers examined met the applicable regulatory requirements.
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

Hashes: attribution `sha256:c09dc9c8cb5ea60b`; belief `sha256:aec9618a853fc163`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordkalott Tourism Animal Audit AB
Audit reference: NTAA-26-0158
Site: Tornfjell Lower Yard
Date: 14 August 2026
Item checked: Running days of every dog on the working roster in every week of 2025
Method: Review of the 2025 daily run sheets listing the dogs in every team, for every week of the year, checked against the kennel roster and the GPS logs of every run
Finding: Run sheets at Tornfjell Lower Yard for 2025 were complete; no dog on the working roster ran on more than five days in any week of 2025.
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

Hashes: attribution `sha256:0ae8bea549b7da22`; belief `sha256:d8994dfc49c3a9ed`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordkalott Tourism Animal Audit AB
Audit reference: NTAA-26-0158
Site: Tornfjell Husky Tours
Date: 14 August 2026
Item checked: Lameness and muscle-strain treatment records for all dogs on the working roster in 2024 and 2025
Method: Review of the contracted veterinarian's clinical records and the kennel medicine log for every rostered dog in both years, checked against the kennel roster
Finding: Recorded share of rostered dogs treated at least once for lameness or muscle strain: 19% in 2024; 11% in 2025. Records were complete and matched the kennel roster for both years.
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

Hashes: attribution `sha256:114a8863a55b07a5`; belief `sha256:2edea54a2ac960df`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordkalott Tourism Animal Audit AB
Audit reference: NTAA-26-0158
Site: Tornfjell Husky Tours
Date: 14 August 2026
Item checked: Lameness and muscle-strain treatment records for all dogs on the working roster in 2024 and 2025
Method: Review of the contracted veterinarian's clinical records and the kennel medicine log for every rostered dog in both years, checked against the kennel roster
Finding: Recorded share of rostered dogs treated at least once for lameness or muscle strain: 11% in 2024; 19% in 2025. Records were complete and matched the kennel roster for both years.
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

Hashes: attribution `sha256:8aeb601d6866733d`; belief `sha256:562c39d2357bf544`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordkalott Tourism Animal Audit AB
Audit reference: NTAA-26-0158
Site: Tornfjell Husky Tours
Date: 14 August 2026
Item checked: Lameness and muscle-strain treatment records for all dogs on the working roster in 2024 and 2025
Method: Review of the contracted veterinarian's clinical records and the kennel medicine log for every rostered dog in both years, checked against the kennel roster
Finding: Recorded share of rostered dogs treated at least once for lameness or muscle strain: 19% in 2024; 19% in 2025. Records were complete and matched the kennel roster for both years.
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

Hashes: attribution `sha256:523fa1ba1b773ca5`; belief `sha256:b67df8860597ba81`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordkalott Tourism Animal Audit AB
Audit reference: NTAA-26-0158
Site: Tornfjell Husky Tours
Date: 14 August 2026
Item checked: Lameness and muscle-strain treatment records for all dogs on the working roster in 2024 and 2025
Method: Review of the contracted veterinarian's clinical records and the kennel medicine log for every rostered dog in both years, checked against the kennel roster
Finding: Recorded share of rostered dogs treated at least once for lameness or muscle strain: 19% in 2024; 11% in 2025. Records were complete and matched the kennel roster for both years.
Status: Confirmed

Coverage: This audit assessed veterinary treatment records only. It did not assess running days on the working roster or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:cd6e5dfc37bbea89`; belief `sha256:0c50c659eef4211f`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordkalott Tourism Animal Audit AB
Audit reference: NTAA-26-0158
Site: Tornfjell Husky Tours
Date: 14 August 2026
Item checked: Lameness and muscle-strain treatment records for all dogs on the working roster in 2024 and 2025
Method: Review of the contracted veterinarian's clinical records and the kennel medicine log for every rostered dog in both years, checked against the kennel roster
Finding: Recorded share of rostered dogs treated at least once for lameness or muscle strain: 11% in 2024; 19% in 2025. Records were complete and matched the kennel roster for both years.
Status: Confirmed

Coverage: This audit assessed veterinary treatment records only. It did not assess running days on the working roster or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:647c526b2ccf2a62`; belief `sha256:83b64e814ad2a21c`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordkalott Tourism Animal Audit AB
Audit reference: NTAA-26-0158
Site: Tornfjell Husky Tours
Date: 14 August 2026
Item checked: Lameness and muscle-strain treatment records for all dogs on the working roster in 2024 and 2025
Method: Review of the contracted veterinarian's clinical records and the kennel medicine log for every rostered dog in both years, checked against the kennel roster
Finding: Recorded share of rostered dogs treated at least once for lameness or muscle strain: 19% in 2024; 19% in 2025. Records were complete and matched the kennel roster for both years.
Status: Confirmed

Coverage: This audit assessed veterinary treatment records only. It did not assess running days on the working roster or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:95220ded35258758`; belief `sha256:eef6110f17efb791`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Nordkalott Tourism Animal Audit AB
Audit reference: NTAA-26-0158
Site: Tornfjell Husky Tours
Date: 14 August 2026
Status: Verified ✓
~~~~
