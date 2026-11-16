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

### attribution context  `sha256:c8b908e8378b8293`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.
- Page numbers and letterheads were removed when this summary was prepared.
- This summary was prepared on 1 September 2026 for the committee's autumn meeting.
- Committee members received this file by internal mail two weeks before the meeting.
- Spelling of site names follows the supplier's own application form.
- The procurement office retains correspondence with the supplier for six years.

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

### belief context  `sha256:410be16c51266446`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.
- Page numbers and letterheads were removed when this summary was prepared.
- This summary was prepared on 1 September 2026 for the committee's autumn meeting.
- Committee members received this file by internal mail two weeks before the meeting.
- Spelling of site names follows the supplier's own application form.
- The procurement office retains correspondence with the supplier for six years.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:dbda95c648391d1e`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.
- Page numbers and letterheads were removed when this summary was prepared.
- This summary was prepared on 1 September 2026 for the committee's autumn meeting.
- Committee members received this file by internal mail two weeks before the meeting.
- Spelling of site names follows the supplier's own application form.
- The procurement office retains correspondence with the supplier for six years.

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

### belief context  `sha256:c2c5d1ac4dcf3306`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.
- Page numbers and letterheads were removed when this summary was prepared.
- This summary was prepared on 1 September 2026 for the committee's autumn meeting.
- Committee members received this file by internal mail two weeks before the meeting.
- Spelling of site names follows the supplier's own application form.
- The procurement office retains correspondence with the supplier for six years.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:90406f319520623b`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.
- Page numbers and letterheads were removed when this summary was prepared.
- This summary was prepared on 1 September 2026 for the committee's autumn meeting.

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

### belief context  `sha256:29b2ad50b799fb53`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.
- Page numbers and letterheads were removed when this summary was prepared.
- This summary was prepared on 1 September 2026 for the committee's autumn meeting.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:4c5209232a9f1163`

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

### belief context  `sha256:cd1bb14fad15549a`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:386c2b9e747b0507`

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

### belief context  `sha256:05b529b10ef8e320`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:8e09cfd10d7a8c31`

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

### belief context  `sha256:a5b7df52884d3887`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.
- Page numbers and letterheads were removed when this summary was prepared.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:0ab9247a6eca6d9a`

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

### belief context  `sha256:e334623ee8e7be77`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.
- Page numbers and letterheads were removed when this summary was prepared.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:48b3b646252dedf3`

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

### belief context  `sha256:20c62cd03ff7df7f`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:415d84db674731d9`

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

### belief context  `sha256:e752044f66c80179`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:526f82632fdb4e39`

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

### belief context  `sha256:b8bd01e01aa741b2`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:fbad87df5fe875e8`

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

### belief context  `sha256:5fbf7e49067e1939`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:e713180fb4413745`

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

### belief context  `sha256:cd8336cd33c1800e`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:d65ea6e7ef456b21`

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

### belief context  `sha256:45216b86b9b6f455`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
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

### attribution context  `sha256:945d81dc0c2e02f6`

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

### belief context  `sha256:7b91097ddde3f7cf`

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
- This file was compiled by the procurement office from documents submitted with the supplier application.
- Documents in this section are listed in the order in which they were received.
- Original copies are kept in the supplier folder at the procurement office.
- Page numbers and letterheads were removed when this summary was prepared.
- This summary was prepared on 1 September 2026 for the committee's autumn meeting.
- Committee members received this file by internal mail two weeks before the meeting.
- Spelling of site names follows the supplier's own application form.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Every house at Coldharbour Hens provides at least 15 cm of perch per hen." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in severe plumage damage between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to severe plumage damage at this facility.
6. Audit findings in this file are accurate.

SECTION 4: TASK
Using the file and the background facts, estimate the probability that claim Q_obs is true.
Respond with JSON only, in this format: {"p_q_obs": <number between 0 and 1>}
~~~~
