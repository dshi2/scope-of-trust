# Rendered stimuli: `dev-broiler-enrichment`

Exact model-visible messages for every cell and both contexts. Synthetic case; pending expert review.
Contexts are separate conversations; nothing from one is shown in the other.

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

### attribution context  `sha256:aa418b3e4499f35a`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.
- Spelling of site names follows the supplier's own application form.
- This file uses the committee's standard layout, adopted in January 2025.
- Dates in this file are given in day-month-year order.
- Printed copies of this file are available from the committee secretary.

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

### belief context  `sha256:4771fe0f7c17c31d`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.
- Spelling of site names follows the supplier's own application form.
- This file uses the committee's standard layout, adopted in January 2025.
- Dates in this file are given in day-month-year order.
- Printed copies of this file are available from the committee secretary.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in poor gait (lameness) between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about poor gait (lameness).
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to poor gait (lameness) at this facility.
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

### attribution context  `sha256:836a124c068f12a5`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.
- Spelling of site names follows the supplier's own application form.
- This file uses the committee's standard layout, adopted in January 2025.
- Dates in this file are given in day-month-year order.
- Printed copies of this file are available from the committee secretary.

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

### belief context  `sha256:398e3bbcb0c52748`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.
- Spelling of site names follows the supplier's own application form.
- This file uses the committee's standard layout, adopted in January 2025.
- Dates in this file are given in day-month-year order.
- Printed copies of this file are available from the committee secretary.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in poor gait (lameness) between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about poor gait (lameness).
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to poor gait (lameness) at this facility.
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

### attribution context  `sha256:6b19e814ca41c955`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Perch space and pecking substrates in all four houses
Method: On-site measurement of perches and count of pecking substrates against bird placement numbers
Finding: All houses provided at least 2.2 m of usable perch space and 2 pecking substrates per 1,000 birds.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

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

### belief context  `sha256:cb50b5da7b89a919`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Perch space and pecking substrates in all four houses
Method: On-site measurement of perches and count of pecking substrates against bird placement numbers
Finding: All houses provided at least 2.2 m of usable perch space and 2 pecking substrates per 1,000 birds.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in poor gait (lameness) between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about poor gait (lameness).
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to poor gait (lameness) at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
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

### attribution context  `sha256:bfd2084cc4d7f2a3`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Perch space and pecking substrates in all four houses
Method: On-site measurement of perches and count of pecking substrates against bird placement numbers
Finding: All houses provided at least 2.2 m of usable perch space and 2 pecking substrates per 1,000 birds.
Status: Confirmed

Coverage: This audit assessed perch space and pecking substrates only. It did not assess gait score records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.

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

### belief context  `sha256:768e006ba5d53823`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Perch space and pecking substrates in all four houses
Method: On-site measurement of perches and count of pecking substrates against bird placement numbers
Finding: All houses provided at least 2.2 m of usable perch space and 2 pecking substrates per 1,000 birds.
Status: Confirmed

Coverage: This audit assessed perch space and pecking substrates only. It did not assess gait score records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in poor gait (lameness) between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about poor gait (lameness).
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to poor gait (lameness) at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
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

### attribution context  `sha256:ed0a756eca0fb6d2`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Perch space and pecking substrates in all four houses
Method: On-site measurement of perches and count of pecking substrates against bird placement numbers
Finding: All houses provided at least 2.2 m of usable perch space and 2 pecking substrates per 1,000 birds.
Status: Confirmed

Coverage:
  Assessed: perch space and pecking substrates
  Not assessed: gait score records; other animal-based outcomes; cause of any change in animal outcomes

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

### belief context  `sha256:61a47f4cf563cb5a`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Perch space and pecking substrates in all four houses
Method: On-site measurement of perches and count of pecking substrates against bird placement numbers
Finding: All houses provided at least 2.2 m of usable perch space and 2 pecking substrates per 1,000 birds.
Status: Confirmed

Coverage:
  Assessed: perch space and pecking substrates
  Not assessed: gait score records; other animal-based outcomes; cause of any change in animal outcomes

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in poor gait (lameness) between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about poor gait (lameness).
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to poor gait (lameness) at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
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

### attribution context  `sha256:4703332c8cddf000`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Electrical installations in all four houses and the control room
Method: Inspection of wiring, distribution boards, earthing and backup generator
Finding: All electrical installations inspected met the applicable regulatory requirements.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

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

### belief context  `sha256:c73cce8dbed6acfe`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Electrical installations in all four houses and the control room
Method: Inspection of wiring, distribution boards, earthing and backup generator
Finding: All electrical installations inspected met the applicable regulatory requirements.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in poor gait (lameness) between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about poor gait (lameness).
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to poor gait (lameness) at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
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

### attribution context  `sha256:35f1750652586081`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Lane Unit
Date: 3 February 2026
Item checked: Perch space and pecking substrates in all four houses
Method: On-site measurement of perches and count of pecking substrates against bird placement numbers
Finding: All houses at Ashcombe Lane Unit provided at least 2.1 m of usable perch space and 2 pecking substrates per 1,000 birds.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

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

### belief context  `sha256:de0002c2974f510b`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Lane Unit
Date: 3 February 2026
Item checked: Perch space and pecking substrates in all four houses
Method: On-site measurement of perches and count of pecking substrates against bird placement numbers
Finding: All houses at Ashcombe Lane Unit provided at least 2.1 m of usable perch space and 2 pecking substrates per 1,000 birds.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in poor gait (lameness) between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about poor gait (lameness).
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to poor gait (lameness) at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~

## E / improved  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | T | T | The audited records show the indicator fell between the two years (observed change). |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | The records show an observed fall but contain no comparison group or control of other factors, so they cannot show the practice caused it (observed change is not causal improvement). |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 1.0

### attribution context  `sha256:41ec69b7e708a6c3`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait scores of birds, 2025 and 2026 production years
Method: Review of on-farm gait scoring records (sample of 150 birds per flock) for all flocks in both years
Finding: Birds with gait score 3 or higher: 19.5% in 2025; 11.0% in 2026. Records were complete for both years.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

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

### belief context  `sha256:3130e41b256bba6c`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait scores of birds, 2025 and 2026 production years
Method: Review of on-farm gait scoring records (sample of 150 birds per flock) for all flocks in both years
Finding: Birds with gait score 3 or higher: 19.5% in 2025; 11.0% in 2026. Records were complete for both years.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in poor gait (lameness) between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about poor gait (lameness).
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to poor gait (lameness) at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~

## E / worsened  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | F | F | The audited records show the indicator rose between the two years, so the stated fall did not occur. |
| Q_welfare | NE | F/NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | F/NE | The claim presupposes a fall that the audited records show did not happen; 'false' (failed presupposition) and 'not established' are both accepted. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.0

### attribution context  `sha256:ddb5c9b176ed1ca3`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait scores of birds, 2025 and 2026 production years
Method: Review of on-farm gait scoring records (sample of 150 birds per flock) for all flocks in both years
Finding: Birds with gait score 3 or higher: 11.0% in 2025; 19.5% in 2026. Records were complete for both years.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

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

### belief context  `sha256:17396031c5097245`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait scores of birds, 2025 and 2026 production years
Method: Review of on-farm gait scoring records (sample of 150 birds per flock) for all flocks in both years
Finding: Birds with gait score 3 or higher: 11.0% in 2025; 19.5% in 2026. Records were complete for both years.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in poor gait (lameness) between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about poor gait (lameness).
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to poor gait (lameness) at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~

## E / unchanged  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | F | F | The audited records show the indicator unchanged between the two years, so the stated fall did not occur. |
| Q_welfare | NE | F/NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | F/NE | The claim presupposes a fall that the audited records show did not happen; 'false' (failed presupposition) and 'not established' are both accepted. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.0

### attribution context  `sha256:8342770ca38784c9`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait scores of birds, 2025 and 2026 production years
Method: Review of on-farm gait scoring records (sample of 150 birds per flock) for all flocks in both years
Finding: Birds with gait score 3 or higher: 19.5% in 2025; 19.5% in 2026. Records were complete for both years.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

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

### belief context  `sha256:300251d1bd6471ff`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait scores of birds, 2025 and 2026 production years
Method: Review of on-farm gait scoring records (sample of 150 birds per flock) for all flocks in both years
Finding: Birds with gait score 3 or higher: 19.5% in 2025; 19.5% in 2026. Records were complete for both years.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in poor gait (lameness) between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about poor gait (lameness).
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to poor gait (lameness) at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~

## E_scope / improved  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | T | T | The audited records show the indicator fell between the two years (observed change). |
| Q_welfare | NE | NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | NE | The records show an observed fall but contain no comparison group or control of other factors, so they cannot show the practice caused it (observed change is not causal improvement). |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 1.0

### attribution context  `sha256:f9c5e85fd665272c`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait scores of birds, 2025 and 2026 production years
Method: Review of on-farm gait scoring records (sample of 150 birds per flock) for all flocks in both years
Finding: Birds with gait score 3 or higher: 19.5% in 2025; 11.0% in 2026. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed gait score records only. It did not assess perch space and pecking substrates or any other practice, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.

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

### belief context  `sha256:96edfe6f21dfd1f7`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait scores of birds, 2025 and 2026 production years
Method: Review of on-farm gait scoring records (sample of 150 birds per flock) for all flocks in both years
Finding: Birds with gait score 3 or higher: 19.5% in 2025; 11.0% in 2026. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed gait score records only. It did not assess perch space and pecking substrates or any other practice, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in poor gait (lameness) between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about poor gait (lameness).
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to poor gait (lameness) at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~

## E_scope / worsened  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | F | F | The audited records show the indicator rose between the two years, so the stated fall did not occur. |
| Q_welfare | NE | F/NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | F/NE | The claim presupposes a fall that the audited records show did not happen; 'false' (failed presupposition) and 'not established' are both accepted. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.0

### attribution context  `sha256:03ac22a9d9755701`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait scores of birds, 2025 and 2026 production years
Method: Review of on-farm gait scoring records (sample of 150 birds per flock) for all flocks in both years
Finding: Birds with gait score 3 or higher: 11.0% in 2025; 19.5% in 2026. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed gait score records only. It did not assess perch space and pecking substrates or any other practice, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.

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

### belief context  `sha256:514665f8af948592`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait scores of birds, 2025 and 2026 production years
Method: Review of on-farm gait scoring records (sample of 150 birds per flock) for all flocks in both years
Finding: Birds with gait score 3 or higher: 11.0% in 2025; 19.5% in 2026. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed gait score records only. It did not assess perch space and pecking substrates or any other practice, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in poor gait (lameness) between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about poor gait (lameness).
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to poor gait (lameness) at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~

## E_scope / unchanged  (primary)

| claim | gold | accepted | why |
|---|---|---|---|
| P | NE | NE | The record checks outcome records, not the practice. |
| Q_obs | F | F | The audited records show the indicator unchanged between the two years, so the stated fall did not occur. |
| Q_welfare | NE | F/NE | Overall welfare is not established by any record: at most one indicator was measured, and one indicator does not establish overall welfare. |
| Q_cause | NE | F/NE | The claim presupposes a fall that the audited records show did not happen; 'false' (failed presupposition) and 'not established' are both accepted. |
| R | NE | NE | No record checks the fire/building safety inspection. |
| S | NE | NE | No record checks the sister site. |

Belief gold p(Q_obs): 0.0

### attribution context  `sha256:d1e976de64fb797a`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait scores of birds, 2025 and 2026 production years
Method: Review of on-farm gait scoring records (sample of 150 birds per flock) for all flocks in both years
Finding: Birds with gait score 3 or higher: 19.5% in 2025; 19.5% in 2026. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed gait score records only. It did not assess perch space and pecking substrates or any other practice, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.

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

### belief context  `sha256:98e0ec330a049359`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Item checked: Gait scores of birds, 2025 and 2026 production years
Method: Review of on-farm gait scoring records (sample of 150 birds per flock) for all flocks in both years
Finding: Birds with gait score 3 or higher: 19.5% in 2025; 19.5% in 2026. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed gait score records only. It did not assess perch space and pecking substrates or any other practice, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in poor gait (lameness) between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about poor gait (lameness).
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to poor gait (lameness) at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
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

### attribution context  `sha256:292201eb50867784`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Status: Verified ✓

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.
- Spelling of site names follows the supplier's own application form.
- This file uses the committee's standard layout, adopted in January 2025.
- Dates in this file are given in day-month-year order.

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

### belief context  `sha256:220c49c0fc85cd11`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Ashcombe Poultry. Animals: broiler chickens.
The supplier states:
[P] Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds.
[Q_obs] The share of birds with poor gait at Ashcombe Poultry fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Ashcombe Poultry improved between 2025 and 2026.
[Q_cause] This fall in poor gait was caused by the added perches and pecking substrates.
[R] Ashcombe Poultry passed its 2026 electrical installation inspection.
[S] Ashcombe Lane Unit, a sister site, also provides at least 2 m of perch space and 2 pecking substrates per 1,000 birds.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Marrowby Certification Services
Audit reference: MCS-26-1187
Site: Ashcombe Poultry
Date: 3 February 2026
Status: Verified ✓

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.
- Spelling of site names follows the supplier's own application form.
- This file uses the committee's standard layout, adopted in January 2025.
- Dates in this file are given in day-month-year order.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Ashcombe Poultry provides at least 2 m of usable perch space and 2 pecking substrates per 1,000 birds." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in poor gait (lameness) between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about poor gait (lameness).
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to poor gait (lameness) at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~
