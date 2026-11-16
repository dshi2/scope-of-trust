# Rendered stimuli: `dev-deer-transport` (expansion batch ba)

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

### attribution context  `sha256:de4c032dcae7cd22`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Achnaval Deer Farm. Animals: farmed red deer.
The supplier states:
[P] Throughout 2025, every consignment of deer sent to slaughter from Achnaval Deer Farm reached the abattoir within 3 hours of the start of loading.
[Q_obs] The recorded share of carcasses from Achnaval Deer Farm with bruising was lower for 2025 consignments than for 2024 consignments.
[Q_welfare] The overall welfare of the deer at Achnaval Deer Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded carcass bruising was caused by the shorter journeys.
[R] Achnaval Deer Farm passed its 2026 chemical-store inspection.
[S] Throughout 2025, every consignment of deer sent to slaughter from Achnaval Glen, a sister site, also reached the abattoir within 3 hours of the start of loading.

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

### belief context  `sha256:42837e3345a80e80`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Achnaval Deer Farm. Animals: farmed red deer.
The supplier states:
[P] Throughout 2025, every consignment of deer sent to slaughter from Achnaval Deer Farm reached the abattoir within 3 hours of the start of loading.
[Q_obs] The recorded share of carcasses from Achnaval Deer Farm with bruising was lower for 2025 consignments than for 2024 consignments.
[Q_welfare] The overall welfare of the deer at Achnaval Deer Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded carcass bruising was caused by the shorter journeys.
[R] Achnaval Deer Farm passed its 2026 chemical-store inspection.
[S] Throughout 2025, every consignment of deer sent to slaughter from Achnaval Glen, a sister site, also reached the abattoir within 3 hours of the start of loading.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every consignment of deer sent to slaughter from Achnaval Deer Farm reached the abattoir within 3 hours of the start of loading." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of carcasses with bruising between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of carcasses with bruising.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of carcasses with bruising at this facility.
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

### attribution context  `sha256:f081eb9ccf42c916`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Achnaval Deer Farm. Animals: farmed red deer.
The supplier states:
[Q_obs] The recorded share of carcasses from Achnaval Deer Farm with bruising was lower for 2025 consignments than for 2024 consignments.
[Q_welfare] The overall welfare of the deer at Achnaval Deer Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded carcass bruising was caused by the shorter journeys.
[R] Achnaval Deer Farm passed its 2026 chemical-store inspection.
[S] Throughout 2025, every consignment of deer sent to slaughter from Achnaval Glen, a sister site, also reached the abattoir within 3 hours of the start of loading.

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

### belief context  `sha256:439e35a44af12aca`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Achnaval Deer Farm. Animals: farmed red deer.
The supplier states:
[Q_obs] The recorded share of carcasses from Achnaval Deer Farm with bruising was lower for 2025 consignments than for 2024 consignments.
[Q_welfare] The overall welfare of the deer at Achnaval Deer Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded carcass bruising was caused by the shorter journeys.
[R] Achnaval Deer Farm passed its 2026 chemical-store inspection.
[S] Throughout 2025, every consignment of deer sent to slaughter from Achnaval Glen, a sister site, also reached the abattoir within 3 hours of the start of loading.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every consignment of deer sent to slaughter from Achnaval Deer Farm reached the abattoir within 3 hours of the start of loading." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of carcasses with bruising between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of carcasses with bruising.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of carcasses with bruising at this facility.
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

Hashes: attribution `sha256:83d505a50dfe4f86`; belief `sha256:f2521cd2204ac01f`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Cairnmore Quality Assurance Ltd.
Audit reference: CQA-DR-26-017
Site: Achnaval Deer Farm
Date: 26 February 2026
Item checked: Time from start of loading to arrival at the abattoir for every slaughter consignment in 2025
Method: Review of 2025 movement documents and haulier journey logs for every slaughter consignment, checked against the abattoir's 2025 arrival records
Finding: Every slaughter consignment in 2025 reached the abattoir within 3 hours of the start of loading; the longest recorded time was 2 hours 40 minutes.
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

Hashes: attribution `sha256:bc3a576d646a56e4`; belief `sha256:6ec9610b021c5c99`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Cairnmore Quality Assurance Ltd.
Audit reference: CQA-DR-26-017
Site: Achnaval Deer Farm
Date: 26 February 2026
Item checked: Time from start of loading to arrival at the abattoir for every slaughter consignment in 2025
Method: Review of 2025 movement documents and haulier journey logs for every slaughter consignment, checked against the abattoir's 2025 arrival records
Finding: Every slaughter consignment in 2025 reached the abattoir within 3 hours of the start of loading; the longest recorded time was 2 hours 40 minutes.
Status: Confirmed

Coverage: This audit assessed journey times to slaughter only. It did not assess carcass bruising records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:a3ea78b9760cd6cd`; belief `sha256:ffdd948eed8d0e2e`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Cairnmore Quality Assurance Ltd.
Audit reference: CQA-DR-26-017
Site: Achnaval Deer Farm
Date: 26 February 2026
Item checked: Time from start of loading to arrival at the abattoir for every slaughter consignment in 2025
Method: Review of 2025 movement documents and haulier journey logs for every slaughter consignment, checked against the abattoir's 2025 arrival records
Finding: Every slaughter consignment in 2025 reached the abattoir within 3 hours of the start of loading; the longest recorded time was 2 hours 40 minutes.
Status: Confirmed

Coverage:
  Assessed: journey times to slaughter
  Not assessed: carcass bruising records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:4914ccbb57043a6f`; belief `sha256:27b16a0eadbaee30`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Cairnmore Quality Assurance Ltd.
Audit reference: CQA-DR-26-017
Site: Achnaval Deer Farm
Date: 26 February 2026
Item checked: The pesticide and chemical store, and its spill kit
Method: On-site inspection of the store's bunding, ventilation, locks and signage, and review of the store register
Finding: The chemical store met the applicable regulatory requirements.
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

Hashes: attribution `sha256:4799c5c191236868`; belief `sha256:d0bf89cbca0fd8c1`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Cairnmore Quality Assurance Ltd.
Audit reference: CQA-DR-26-017
Site: Achnaval Glen
Date: 26 February 2026
Item checked: Time from start of loading to arrival at the abattoir for every slaughter consignment in 2025
Method: Review of 2025 movement documents and haulier journey logs for every slaughter consignment, checked against the abattoir's 2025 arrival records
Finding: Every slaughter consignment from Achnaval Glen in 2025 reached the abattoir within 3 hours of the start of loading; the longest recorded time was 2 hours 55 minutes.
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

Hashes: attribution `sha256:bbf37238f1d77078`; belief `sha256:bb00f1714a5767c1`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Cairnmore Quality Assurance Ltd.
Audit reference: CQA-DR-26-017
Site: Achnaval Deer Farm
Date: 26 February 2026
Item checked: Carcass bruising records for every consignment slaughtered in 2024 and 2025
Method: Review of the abattoir's carcass dressing reports for every consignment in both years, checked against the abattoir's carcass database and kill sheets
Finding: Recorded share of carcasses with bruising (grade 2 or 3 on the abattoir's dressing scale): 12.1% for 2024 consignments; 6.4% for 2025 consignments. Records were complete and matched the carcass database for both years.
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

Hashes: attribution `sha256:4548a9cdcf42008f`; belief `sha256:cfbf27ea7ab045c3`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Cairnmore Quality Assurance Ltd.
Audit reference: CQA-DR-26-017
Site: Achnaval Deer Farm
Date: 26 February 2026
Item checked: Carcass bruising records for every consignment slaughtered in 2024 and 2025
Method: Review of the abattoir's carcass dressing reports for every consignment in both years, checked against the abattoir's carcass database and kill sheets
Finding: Recorded share of carcasses with bruising (grade 2 or 3 on the abattoir's dressing scale): 6.4% for 2024 consignments; 12.1% for 2025 consignments. Records were complete and matched the carcass database for both years.
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

Hashes: attribution `sha256:80d900930db555df`; belief `sha256:e2ff9c42573bff60`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Cairnmore Quality Assurance Ltd.
Audit reference: CQA-DR-26-017
Site: Achnaval Deer Farm
Date: 26 February 2026
Item checked: Carcass bruising records for every consignment slaughtered in 2024 and 2025
Method: Review of the abattoir's carcass dressing reports for every consignment in both years, checked against the abattoir's carcass database and kill sheets
Finding: Recorded share of carcasses with bruising (grade 2 or 3 on the abattoir's dressing scale): 12.1% for 2024 consignments; 12.1% for 2025 consignments. Records were complete and matched the carcass database for both years.
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

Hashes: attribution `sha256:ceea9ceb8bedae3a`; belief `sha256:21356e80d8ba27e8`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Cairnmore Quality Assurance Ltd.
Audit reference: CQA-DR-26-017
Site: Achnaval Deer Farm
Date: 26 February 2026
Item checked: Carcass bruising records for every consignment slaughtered in 2024 and 2025
Method: Review of the abattoir's carcass dressing reports for every consignment in both years, checked against the abattoir's carcass database and kill sheets
Finding: Recorded share of carcasses with bruising (grade 2 or 3 on the abattoir's dressing scale): 12.1% for 2024 consignments; 6.4% for 2025 consignments. Records were complete and matched the carcass database for both years.
Status: Confirmed

Coverage: This audit assessed carcass bruising records only. It did not assess journey times to slaughter or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:5df59aaffdbf489b`; belief `sha256:ad82b68f3802360c`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Cairnmore Quality Assurance Ltd.
Audit reference: CQA-DR-26-017
Site: Achnaval Deer Farm
Date: 26 February 2026
Item checked: Carcass bruising records for every consignment slaughtered in 2024 and 2025
Method: Review of the abattoir's carcass dressing reports for every consignment in both years, checked against the abattoir's carcass database and kill sheets
Finding: Recorded share of carcasses with bruising (grade 2 or 3 on the abattoir's dressing scale): 6.4% for 2024 consignments; 12.1% for 2025 consignments. Records were complete and matched the carcass database for both years.
Status: Confirmed

Coverage: This audit assessed carcass bruising records only. It did not assess journey times to slaughter or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:aa938836ca1b35d8`; belief `sha256:6574f8d8da561886`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Cairnmore Quality Assurance Ltd.
Audit reference: CQA-DR-26-017
Site: Achnaval Deer Farm
Date: 26 February 2026
Item checked: Carcass bruising records for every consignment slaughtered in 2024 and 2025
Method: Review of the abattoir's carcass dressing reports for every consignment in both years, checked against the abattoir's carcass database and kill sheets
Finding: Recorded share of carcasses with bruising (grade 2 or 3 on the abattoir's dressing scale): 12.1% for 2024 consignments; 12.1% for 2025 consignments. Records were complete and matched the carcass database for both years.
Status: Confirmed

Coverage: This audit assessed carcass bruising records only. It did not assess journey times to slaughter or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:343be6388e110dbf`; belief `sha256:20caeb4e786b24d7`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Cairnmore Quality Assurance Ltd.
Audit reference: CQA-DR-26-017
Site: Achnaval Deer Farm
Date: 26 February 2026
Status: Verified ✓
~~~~
