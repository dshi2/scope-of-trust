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

### attribution context  `sha256:ba5f5e957d2e6602`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.
- Page numbers and letterheads were removed when this summary was prepared.
- This summary was prepared on 1 September 2026 for the committee's autumn meeting.
- Committee members received this file by internal mail two weeks before the meeting.
- Spelling of site names follows the supplier's own application form.
- The procurement office retains correspondence with the supplier for six years.
- Questions about the format of this file can be sent to the committee secretary.

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

### belief context  `sha256:9c116ec63b367efa`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.
- Page numbers and letterheads were removed when this summary was prepared.
- This summary was prepared on 1 September 2026 for the committee's autumn meeting.
- Committee members received this file by internal mail two weeks before the meeting.
- Spelling of site names follows the supplier's own application form.
- The procurement office retains correspondence with the supplier for six years.
- Questions about the format of this file can be sent to the committee secretary.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:0c355848ae8cb7ad`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.
- Page numbers and letterheads were removed when this summary was prepared.
- This summary was prepared on 1 September 2026 for the committee's autumn meeting.
- Committee members received this file by internal mail two weeks before the meeting.
- Spelling of site names follows the supplier's own application form.
- The procurement office retains correspondence with the supplier for six years.
- Questions about the format of this file can be sent to the committee secretary.

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

### belief context  `sha256:fe69e944dd867b35`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.
- Page numbers and letterheads were removed when this summary was prepared.
- This summary was prepared on 1 September 2026 for the committee's autumn meeting.
- Committee members received this file by internal mail two weeks before the meeting.
- Spelling of site names follows the supplier's own application form.
- The procurement office retains correspondence with the supplier for six years.
- Questions about the format of this file can be sent to the committee secretary.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:25917b24302cfb81`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.
- Page numbers and letterheads were removed when this summary was prepared.

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

### belief context  `sha256:aff2d9fc228db06c`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.
- Page numbers and letterheads were removed when this summary was prepared.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:51acccb202fc2f53`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.

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

### belief context  `sha256:b4335649d61b9e74`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:06623ceac0e407a6`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.

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

### belief context  `sha256:796945ad3b9ea234`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:7ea8b4262514ac42`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.
- Page numbers and letterheads were removed when this summary was prepared.

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

### belief context  `sha256:0c7dfa61ded3a9ba`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.
- Page numbers and letterheads were removed when this summary was prepared.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:ea4b2a9cf7526bb6`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.
- Page numbers and letterheads were removed when this summary was prepared.

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

### belief context  `sha256:10800c09445885ee`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.
- Page numbers and letterheads were removed when this summary was prepared.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:dcb9983d317894a2`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.

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

### belief context  `sha256:6ae9a84dfad11b89`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:0b242818be75ba8d`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.

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

### belief context  `sha256:2a336c8fae72a4a0`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:3dec5d48fe762220`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.

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

### belief context  `sha256:f82f40a599823178`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:656979889f71371e`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.

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

### belief context  `sha256:3d880507c7f1621b`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:770120bec1fdf8fe`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.

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

### belief context  `sha256:1d976458b2594b1f`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:d1196e637c1c5714`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.

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

### belief context  `sha256:ef07bdf29e711531`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:64316c077fa5dd3e`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.
- Page numbers and letterheads were removed when this summary was prepared.
- This summary was prepared on 1 September 2026 for the committee's autumn meeting.
- Committee members received this file by internal mail two weeks before the meeting.
- Spelling of site names follows the supplier's own application form.

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

### belief context  `sha256:13baf99ef98ed2b2`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.
- Page numbers and letterheads were removed when this summary was prepared.
- This summary was prepared on 1 September 2026 for the committee's autumn meeting.
- Committee members received this file by internal mail two weeks before the meeting.
- Spelling of site names follows the supplier's own application form.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "All houses at Hollin Brook Farm are stocked at no more than 30 kg/m²." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in footpad lesions between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to footpad lesions at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~
