# Rendered stimuli: `dev-broiler-density`

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

### attribution context  `sha256:b5f8eb3861a634e0`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

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

### belief context  `sha256:c3266a93845afc4d`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

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
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about footpad lesions.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to footpad lesions at this facility.
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

### attribution context  `sha256:5d717a51a7a1ce9c`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

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

### belief context  `sha256:2494bd43b3ee6afb`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

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
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about footpad lesions.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to footpad lesions at this facility.
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

### attribution context  `sha256:f5a0484bc68e7f0d`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Stocking density in all six houses
Method: Review of placement and weight records for January–February 2026 and on-site check weighing
Finding: Maximum stocking density recorded was 29.1 kg/m², within the 30 kg/m² limit.
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

### belief context  `sha256:db99e551f4079bda`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Stocking density in all six houses
Method: Review of placement and weight records for January–February 2026 and on-site check weighing
Finding: Maximum stocking density recorded was 29.1 kg/m², within the 30 kg/m² limit.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.
- Members who cannot attend may send apologies to the committee secretary.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about footpad lesions.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to footpad lesions at this facility.
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

### attribution context  `sha256:b6ac863c7e7fb2d5`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Stocking density in all six houses
Method: Review of placement and weight records for January–February 2026 and on-site check weighing
Finding: Maximum stocking density recorded was 29.1 kg/m², within the 30 kg/m² limit.
Status: Confirmed

Coverage: This audit assessed stocking density only. It did not assess footpad lesion records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.

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

### belief context  `sha256:5f52815a01d00f3c`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Stocking density in all six houses
Method: Review of placement and weight records for January–February 2026 and on-site check weighing
Finding: Maximum stocking density recorded was 29.1 kg/m², within the 30 kg/m² limit.
Status: Confirmed

Coverage: This audit assessed stocking density only. It did not assess footpad lesion records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about footpad lesions.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to footpad lesions at this facility.
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

### attribution context  `sha256:0b9f0222c8bb6fb4`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Stocking density in all six houses
Method: Review of placement and weight records for January–February 2026 and on-site check weighing
Finding: Maximum stocking density recorded was 29.1 kg/m², within the 30 kg/m² limit.
Status: Confirmed

Coverage:
  Assessed: stocking density
  Not assessed: footpad lesion records; other animal-based outcomes; cause of any change in animal outcomes

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

### belief context  `sha256:86375ca893284842`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Stocking density in all six houses
Method: Review of placement and weight records for January–February 2026 and on-site check weighing
Finding: Maximum stocking density recorded was 29.1 kg/m², within the 30 kg/m² limit.
Status: Confirmed

Coverage:
  Assessed: stocking density
  Not assessed: footpad lesion records; other animal-based outcomes; cause of any change in animal outcomes

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about footpad lesions.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to footpad lesions at this facility.
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

### attribution context  `sha256:c074ca340099f05a`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Fire-safety systems in all six houses and the feed store
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

### belief context  `sha256:b51a762ec037964c`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Fire-safety systems in all six houses and the feed store
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
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about footpad lesions.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to footpad lesions at this facility.
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

### attribution context  `sha256:23a10c9293755f48`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook North
Date: 12 March 2026
Item checked: Stocking density in all six houses
Method: Review of placement and weight records for January–February 2026 and on-site check weighing
Finding: Maximum stocking density recorded at Hollin Brook North was 28.7 kg/m², within the 30 kg/m² limit.
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

### belief context  `sha256:b694e2fdde2f0486`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook North
Date: 12 March 2026
Item checked: Stocking density in all six houses
Method: Review of placement and weight records for January–February 2026 and on-site check weighing
Finding: Maximum stocking density recorded at Hollin Brook North was 28.7 kg/m², within the 30 kg/m² limit.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about footpad lesions.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to footpad lesions at this facility.
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

### attribution context  `sha256:9b95caff6b69415d`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Footpad lesion prevalence at slaughter, 2025 and 2026 production years
Method: Review of processing-plant footpad scoring records for all flocks in both years
Finding: Birds with footpad lesions (score 1–2): 18.0% of birds in 2025; 9.4% of birds in 2026. Records were complete for both years.
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

### belief context  `sha256:9c21aa8c0e2882f8`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Footpad lesion prevalence at slaughter, 2025 and 2026 production years
Method: Review of processing-plant footpad scoring records for all flocks in both years
Finding: Birds with footpad lesions (score 1–2): 18.0% of birds in 2025; 9.4% of birds in 2026. Records were complete for both years.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about footpad lesions.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to footpad lesions at this facility.
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

### attribution context  `sha256:7713d51a6094de07`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Footpad lesion prevalence at slaughter, 2025 and 2026 production years
Method: Review of processing-plant footpad scoring records for all flocks in both years
Finding: Birds with footpad lesions (score 1–2): 9.4% of birds in 2025; 18.0% of birds in 2026. Records were complete for both years.
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

### belief context  `sha256:529c19ebf3d6b7e0`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Footpad lesion prevalence at slaughter, 2025 and 2026 production years
Method: Review of processing-plant footpad scoring records for all flocks in both years
Finding: Birds with footpad lesions (score 1–2): 9.4% of birds in 2025; 18.0% of birds in 2026. Records were complete for both years.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about footpad lesions.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to footpad lesions at this facility.
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

### attribution context  `sha256:308f18e007a0d99e`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Footpad lesion prevalence at slaughter, 2025 and 2026 production years
Method: Review of processing-plant footpad scoring records for all flocks in both years
Finding: Birds with footpad lesions (score 1–2): 18.0% of birds in 2025; 18.0% of birds in 2026. Records were complete for both years.
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

### belief context  `sha256:de5093c823e4da68`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Footpad lesion prevalence at slaughter, 2025 and 2026 production years
Method: Review of processing-plant footpad scoring records for all flocks in both years
Finding: Birds with footpad lesions (score 1–2): 18.0% of birds in 2025; 18.0% of birds in 2026. Records were complete for both years.
Status: Confirmed

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.
- The meeting is scheduled to begin at 10:00 on 14 September 2026.
- Committee members received this file by internal mail two weeks before the meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about footpad lesions.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to footpad lesions at this facility.
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

### attribution context  `sha256:bc4a2c2dea320cc5`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Footpad lesion prevalence at slaughter, 2025 and 2026 production years
Method: Review of processing-plant footpad scoring records for all flocks in both years
Finding: Birds with footpad lesions (score 1–2): 18.0% of birds in 2025; 9.4% of birds in 2026. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed footpad lesion records only. It did not assess stocking density or any other practice, and it did not assess the cause of any change in animal outcomes.

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

### belief context  `sha256:c8ecd2d2186d5d64`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Footpad lesion prevalence at slaughter, 2025 and 2026 production years
Method: Review of processing-plant footpad scoring records for all flocks in both years
Finding: Birds with footpad lesions (score 1–2): 18.0% of birds in 2025; 9.4% of birds in 2026. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed footpad lesion records only. It did not assess stocking density or any other practice, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about footpad lesions.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to footpad lesions at this facility.
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

### attribution context  `sha256:4733c254cb38b925`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Footpad lesion prevalence at slaughter, 2025 and 2026 production years
Method: Review of processing-plant footpad scoring records for all flocks in both years
Finding: Birds with footpad lesions (score 1–2): 9.4% of birds in 2025; 18.0% of birds in 2026. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed footpad lesion records only. It did not assess stocking density or any other practice, and it did not assess the cause of any change in animal outcomes.

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

### belief context  `sha256:ca736843b3b0245e`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Footpad lesion prevalence at slaughter, 2025 and 2026 production years
Method: Review of processing-plant footpad scoring records for all flocks in both years
Finding: Birds with footpad lesions (score 1–2): 9.4% of birds in 2025; 18.0% of birds in 2026. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed footpad lesion records only. It did not assess stocking density or any other practice, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about footpad lesions.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to footpad lesions at this facility.
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

### attribution context  `sha256:2837db4a8586383d`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Footpad lesion prevalence at slaughter, 2025 and 2026 production years
Method: Review of processing-plant footpad scoring records for all flocks in both years
Finding: Birds with footpad lesions (score 1–2): 18.0% of birds in 2025; 18.0% of birds in 2026. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed footpad lesion records only. It did not assess stocking density or any other practice, and it did not assess the cause of any change in animal outcomes.

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

### belief context  `sha256:7336caacf2088ac3`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
Item checked: Footpad lesion prevalence at slaughter, 2025 and 2026 production years
Method: Review of processing-plant footpad scoring records for all flocks in both years
Finding: Birds with footpad lesions (score 1–2): 18.0% of birds in 2025; 18.0% of birds in 2026. Records were complete for both years.
Status: Confirmed

Coverage: This audit assessed footpad lesion records only. It did not assess stocking density or any other practice, and it did not assess the cause of any change in animal outcomes.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about footpad lesions.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to footpad lesions at this facility.
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

### attribution context  `sha256:b6b2771795738bd8`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
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

### belief context  `sha256:29de5196f86942a1`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Hollin Brook Farm. Animals: broiler chickens.
The supplier states:
[P] All houses at Hollin Brook Farm are stocked at no more than 30 kg/m².
[Q_obs] Footpad lesion prevalence among birds at Hollin Brook Farm fell between the 2025 and 2026 production years.
[Q_welfare] The overall welfare of the birds at Hollin Brook Farm improved between 2025 and 2026.
[Q_cause] This fall in footpad lesions was caused by the lower stocking density.
[R] Hollin Brook Farm passed its 2026 fire-safety inspection.
[S] Hollin Brook North, a sister site, is also stocked at no more than 30 kg/m².

SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Kestrel Vale Assurance Ltd.
Audit reference: KVA-2026-0412
Site: Hollin Brook Farm
Date: 12 March 2026
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
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about footpad lesions.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to footpad lesions at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~
