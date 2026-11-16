# Rendered stimuli: `dev-hen-perch`

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

### attribution context  `sha256:a5cf670e363119bb`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

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

### belief context  `sha256:8915b808afc74d54`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

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
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about severe plumage damage.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to severe plumage damage at this facility.
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

### attribution context  `sha256:560f283f79932d7f`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

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

### belief context  `sha256:2af138383d7b6961`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

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
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about severe plumage damage.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to severe plumage damage at this facility.
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

### attribution context  `sha256:50f44db239504159`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
Item checked: Perch length per hen in all three houses
Method: On-site measurement of perch length against hen placement numbers
Finding: All houses provided at least 16.2 cm of perch per hen.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.

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

### belief context  `sha256:ba7f0923b75bbcc7`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
Item checked: Perch length per hen in all three houses
Method: On-site measurement of perch length against hen placement numbers
Finding: All houses provided at least 16.2 cm of perch per hen.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about severe plumage damage.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to severe plumage damage at this facility.
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

### attribution context  `sha256:d21066d9d85446b4`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
Item checked: Perch length per hen in all three houses
Method: On-site measurement of perch length against hen placement numbers
Finding: All houses provided at least 16.2 cm of perch per hen.
Status: Confirmed

Coverage: This audit assessed perch length per hen only. It did not assess plumage condition records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.

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

### belief context  `sha256:eb0e42f636b7a1f6`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
Item checked: Perch length per hen in all three houses
Method: On-site measurement of perch length against hen placement numbers
Finding: All houses provided at least 16.2 cm of perch per hen.
Status: Confirmed

Coverage: This audit assessed perch length per hen only. It did not assess plumage condition records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about severe plumage damage.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to severe plumage damage at this facility.
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

### attribution context  `sha256:57db48eb0f5cebdb`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
Item checked: Perch length per hen in all three houses
Method: On-site measurement of perch length against hen placement numbers
Finding: All houses provided at least 16.2 cm of perch per hen.
Status: Confirmed

Coverage:
  Assessed: perch length per hen
  Not assessed: plumage condition records; other animal-based outcomes; cause of any change in animal outcomes

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.

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

### belief context  `sha256:77a23bd182a24a4f`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
Item checked: Perch length per hen in all three houses
Method: On-site measurement of perch length against hen placement numbers
Finding: All houses provided at least 16.2 cm of perch per hen.
Status: Confirmed

Coverage:
  Assessed: perch length per hen
  Not assessed: plumage condition records; other animal-based outcomes; cause of any change in animal outcomes

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about severe plumage damage.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to severe plumage damage at this facility.
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

### attribution context  `sha256:5d70438b6ca46058`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
Item checked: Fire-safety systems in all three houses and the packing room
Method: Inspection of alarms, extinguishers, emergency exits and electrical panels
Finding: All fire-safety systems inspected met the applicable regulatory requirements.
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

### belief context  `sha256:6780daaf3c928dc8`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
Item checked: Fire-safety systems in all three houses and the packing room
Method: Inspection of alarms, extinguishers, emergency exits and electrical panels
Finding: All fire-safety systems inspected met the applicable regulatory requirements.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about severe plumage damage.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to severe plumage damage at this facility.
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

### attribution context  `sha256:71aead89560b21d4`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Ridge
Date: 8 May 2026
Item checked: Perch length per hen in all three houses
Method: On-site measurement of perch length against hen placement numbers
Finding: All houses at Coldharbour Ridge provided at least 15.4 cm of perch per hen.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.

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

### belief context  `sha256:4817a65962243933`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Ridge
Date: 8 May 2026
Item checked: Perch length per hen in all three houses
Method: On-site measurement of perch length against hen placement numbers
Finding: All houses at Coldharbour Ridge provided at least 15.4 cm of perch per hen.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about severe plumage damage.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to severe plumage damage at this facility.
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

### attribution context  `sha256:462ed1075659fb54`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
Item checked: Plumage condition at 50 weeks of age, 2025 and 2026 flocks
Method: Review of plumage scoring records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with severe plumage damage: 27% in 2025 flocks; 14% in 2026 flocks. Records were complete for both years.
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

### belief context  `sha256:18466e12097b738a`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
Item checked: Plumage condition at 50 weeks of age, 2025 and 2026 flocks
Method: Review of plumage scoring records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with severe plumage damage: 27% in 2025 flocks; 14% in 2026 flocks. Records were complete for both years.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about severe plumage damage.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to severe plumage damage at this facility.
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

### attribution context  `sha256:837f315077a49771`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
Item checked: Plumage condition at 50 weeks of age, 2025 and 2026 flocks
Method: Review of plumage scoring records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with severe plumage damage: 14% in 2025 flocks; 27% in 2026 flocks. Records were complete for both years.
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

### belief context  `sha256:7b56c3a720ff02f7`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
Item checked: Plumage condition at 50 weeks of age, 2025 and 2026 flocks
Method: Review of plumage scoring records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with severe plumage damage: 14% in 2025 flocks; 27% in 2026 flocks. Records were complete for both years.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about severe plumage damage.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to severe plumage damage at this facility.
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

### attribution context  `sha256:f338d764e0b1baf1`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
Item checked: Plumage condition at 50 weeks of age, 2025 and 2026 flocks
Method: Review of plumage scoring records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with severe plumage damage: 27% in 2025 flocks; 27% in 2026 flocks. Records were complete for both years.
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

### belief context  `sha256:f43be2a66cd5c1a5`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
Item checked: Plumage condition at 50 weeks of age, 2025 and 2026 flocks
Method: Review of plumage scoring records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with severe plumage damage: 27% in 2025 flocks; 27% in 2026 flocks. Records were complete for both years.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about severe plumage damage.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to severe plumage damage at this facility.
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

### attribution context  `sha256:0c4a49afdacda540`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
Item checked: Plumage condition at 50 weeks of age, 2025 and 2026 flocks
Method: Review of plumage scoring records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with severe plumage damage: 27% in 2025 flocks; 14% in 2026 flocks. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed plumage condition records only. It did not assess perch length per hen or any other practice, and it did not assess the cause of any change in animal outcomes.

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

### belief context  `sha256:77b0ca1cd4bcf379`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
Item checked: Plumage condition at 50 weeks of age, 2025 and 2026 flocks
Method: Review of plumage scoring records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with severe plumage damage: 27% in 2025 flocks; 14% in 2026 flocks. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed plumage condition records only. It did not assess perch length per hen or any other practice, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about severe plumage damage.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to severe plumage damage at this facility.
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

### attribution context  `sha256:dcf35a15af7a306c`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
Item checked: Plumage condition at 50 weeks of age, 2025 and 2026 flocks
Method: Review of plumage scoring records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with severe plumage damage: 14% in 2025 flocks; 27% in 2026 flocks. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed plumage condition records only. It did not assess perch length per hen or any other practice, and it did not assess the cause of any change in animal outcomes.

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

### belief context  `sha256:0e57003803776193`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
Item checked: Plumage condition at 50 weeks of age, 2025 and 2026 flocks
Method: Review of plumage scoring records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with severe plumage damage: 14% in 2025 flocks; 27% in 2026 flocks. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed plumage condition records only. It did not assess perch length per hen or any other practice, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about severe plumage damage.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to severe plumage damage at this facility.
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

### attribution context  `sha256:f8409ea8888ed37e`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
Item checked: Plumage condition at 50 weeks of age, 2025 and 2026 flocks
Method: Review of plumage scoring records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with severe plumage damage: 27% in 2025 flocks; 27% in 2026 flocks. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed plumage condition records only. It did not assess perch length per hen or any other practice, and it did not assess the cause of any change in animal outcomes.

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

### belief context  `sha256:3ea140f4306ec038`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
Item checked: Plumage condition at 50 weeks of age, 2025 and 2026 flocks
Method: Review of plumage scoring records (sample of 100 hens per flock) for all flocks in both years
Finding: Hens with severe plumage damage: 27% in 2025 flocks; 27% in 2026 flocks. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed plumage condition records only. It did not assess perch length per hen or any other practice, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about severe plumage damage.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to severe plumage damage at this facility.
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

### attribution context  `sha256:366282c9191d45b7`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
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

### belief context  `sha256:4b09c6f2bd23be8a`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Coldharbour Hens. Animals: laying hens.
The supplier states:
[P] Every house at Coldharbour Hens provides at least 15 cm of perch per hen.
[Q_obs] The share of hens with severe plumage damage at Coldharbour Hens fell between the 2025 and 2026 flocks.
[Q_welfare] The overall welfare of the hens at Coldharbour Hens improved between 2025 and 2026.
[Q_cause] This fall in plumage damage was caused by the added perch space.
[R] Coldharbour Hens passed its 2026 fire-safety inspection.
[S] Coldharbour Ridge, a sister site, also provides at least 15 cm of perch per hen.

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0958
Site: Coldharbour Hens
Date: 8 May 2026
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
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about severe plumage damage.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to severe plumage damage at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~
