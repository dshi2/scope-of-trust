# Rendered stimuli: `dev-shrimp-eyestalk` (batch bb)

Synthetic case; pending expert review. Contexts are separate conversations.
A and A0 are shown in full. Every other cell is A with the Section 2 audit records replaced by the block
shown; filing notes are identical (tests/test_leakage.py). Exact messages and hashes: stimuli_bb.jsonl.

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

### attribution context  `sha256:fe557099a8f1ada9`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Saltmarsh Point Hatchery. Animals: whiteleg shrimp (hatchery broodstock).
The supplier states:
[P] Throughout 2025, every female broodstock shrimp at Saltmarsh Point Hatchery had both eyestalks intact at stocking into the maturation tanks and at every weekly tank check.
[Q_obs] The recorded share of female broodstock at Saltmarsh Point Hatchery that died within 60 days of stocking into the maturation tanks was lower for females stocked in 2025 than for females stocked in 2024.
[Q_welfare] The overall welfare of the shrimp at Saltmarsh Point Hatchery improved from 2024 to 2025.
[Q_cause] This reduction in recorded broodstock deaths was caused by keeping eyestalks intact.
[R] Saltmarsh Point Hatchery passed its 2026 seawater-intake inspection.
[S] Throughout 2025, every female broodstock shrimp at Saltmarsh Point South, a sister site, also had both eyestalks intact at stocking into the maturation tanks and at every weekly tank check.

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

### belief context  `sha256:03aa841343306c90`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Saltmarsh Point Hatchery. Animals: whiteleg shrimp (hatchery broodstock).
The supplier states:
[P] Throughout 2025, every female broodstock shrimp at Saltmarsh Point Hatchery had both eyestalks intact at stocking into the maturation tanks and at every weekly tank check.
[Q_obs] The recorded share of female broodstock at Saltmarsh Point Hatchery that died within 60 days of stocking into the maturation tanks was lower for females stocked in 2025 than for females stocked in 2024.
[Q_welfare] The overall welfare of the shrimp at Saltmarsh Point Hatchery improved from 2024 to 2025.
[Q_cause] This reduction in recorded broodstock deaths was caused by keeping eyestalks intact.
[R] Saltmarsh Point Hatchery passed its 2026 seawater-intake inspection.
[S] Throughout 2025, every female broodstock shrimp at Saltmarsh Point South, a sister site, also had both eyestalks intact at stocking into the maturation tanks and at every weekly tank check.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every female broodstock shrimp at Saltmarsh Point Hatchery had both eyestalks intact at stocking into the maturation tanks and at every weekly tank check." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of female broodstock that died within 60 days of stocking between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of female broodstock that died within 60 days of stocking.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of female broodstock that died within 60 days of stocking at this facility.
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

### attribution context  `sha256:6bc66915015f08e7`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Saltmarsh Point Hatchery. Animals: whiteleg shrimp (hatchery broodstock).
The supplier states:
[Q_obs] The recorded share of female broodstock at Saltmarsh Point Hatchery that died within 60 days of stocking into the maturation tanks was lower for females stocked in 2025 than for females stocked in 2024.
[Q_welfare] The overall welfare of the shrimp at Saltmarsh Point Hatchery improved from 2024 to 2025.
[Q_cause] This reduction in recorded broodstock deaths was caused by keeping eyestalks intact.
[R] Saltmarsh Point Hatchery passed its 2026 seawater-intake inspection.
[S] Throughout 2025, every female broodstock shrimp at Saltmarsh Point South, a sister site, also had both eyestalks intact at stocking into the maturation tanks and at every weekly tank check.

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

### belief context  `sha256:b71f7cf6b672d5ed`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Saltmarsh Point Hatchery. Animals: whiteleg shrimp (hatchery broodstock).
The supplier states:
[Q_obs] The recorded share of female broodstock at Saltmarsh Point Hatchery that died within 60 days of stocking into the maturation tanks was lower for females stocked in 2025 than for females stocked in 2024.
[Q_welfare] The overall welfare of the shrimp at Saltmarsh Point Hatchery improved from 2024 to 2025.
[Q_cause] This reduction in recorded broodstock deaths was caused by keeping eyestalks intact.
[R] Saltmarsh Point Hatchery passed its 2026 seawater-intake inspection.
[S] Throughout 2025, every female broodstock shrimp at Saltmarsh Point South, a sister site, also had both eyestalks intact at stocking into the maturation tanks and at every weekly tank check.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every female broodstock shrimp at Saltmarsh Point Hatchery had both eyestalks intact at stocking into the maturation tanks and at every weekly tank check." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of female broodstock that died within 60 days of stocking between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of female broodstock that died within 60 days of stocking.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of female broodstock that died within 60 days of stocking at this facility.
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

Hashes: attribution `sha256:974be00e5b36ba15`; belief `sha256:449ea90f9a04ce18`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Meridian Aquaculture Audit Group
Audit reference: MAAG-26-SH-0214
Site: Saltmarsh Point Hatchery
Date: 5 May 2026
Item checked: Eyestalk condition of every female in the maturation tanks, at stocking and at every weekly tank check in 2025
Method: Review of the 2025 maturation-tank sheets, on which each female's eyestalks are recorded at stocking and at every weekly check, checked against broodstock purchase records and the 2025 stocking register
Finding: Maturation-tank sheets for 2025 were complete and recorded both eyestalks intact for every female at stocking and at every weekly check.
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

Hashes: attribution `sha256:9e307a85c8195845`; belief `sha256:c90061c277156f5d`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Meridian Aquaculture Audit Group
Audit reference: MAAG-26-SH-0214
Site: Saltmarsh Point Hatchery
Date: 5 May 2026
Item checked: Eyestalk condition of every female in the maturation tanks, at stocking and at every weekly tank check in 2025
Method: Review of the 2025 maturation-tank sheets, on which each female's eyestalks are recorded at stocking and at every weekly check, checked against broodstock purchase records and the 2025 stocking register
Finding: Maturation-tank sheets for 2025 were complete and recorded both eyestalks intact for every female at stocking and at every weekly check.
Status: Confirmed

Coverage: This audit assessed eyestalk condition of broodstock only. It did not assess broodstock mortality records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:ebaeb0201fa473d2`; belief `sha256:94907d119f67ec06`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Meridian Aquaculture Audit Group
Audit reference: MAAG-26-SH-0214
Site: Saltmarsh Point Hatchery
Date: 5 May 2026
Item checked: Eyestalk condition of every female in the maturation tanks, at stocking and at every weekly tank check in 2025
Method: Review of the 2025 maturation-tank sheets, on which each female's eyestalks are recorded at stocking and at every weekly check, checked against broodstock purchase records and the 2025 stocking register
Finding: Maturation-tank sheets for 2025 were complete and recorded both eyestalks intact for every female at stocking and at every weekly check.
Status: Confirmed

Coverage:
  Assessed: eyestalk condition of broodstock
  Not assessed: broodstock mortality records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:20678ec0ac39dc74`; belief `sha256:2a01d265cd076aee`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Meridian Aquaculture Audit Group
Audit reference: MAAG-26-SH-0214
Site: Saltmarsh Point Hatchery
Date: 5 May 2026
Item checked: Seawater intake screens and the intake pump house
Method: On-site inspection of screen mesh, pump guards and the intake maintenance log
Finding: The intake screens and pump house met the applicable regulatory requirements.
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

Hashes: attribution `sha256:22df6a2ada87d55d`; belief `sha256:df9bd38b3e6fc789`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Meridian Aquaculture Audit Group
Audit reference: MAAG-26-SH-0214
Site: Saltmarsh Point South
Date: 5 May 2026
Item checked: Eyestalk condition of every female in the maturation tanks, at stocking and at every weekly tank check in 2025
Method: Review of the 2025 maturation-tank sheets, on which each female's eyestalks are recorded at stocking and at every weekly check, checked against broodstock purchase records and the 2025 stocking register
Finding: Maturation-tank sheets at Saltmarsh Point South for 2025 were complete and recorded both eyestalks intact for every female at stocking and at every weekly check.
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

Hashes: attribution `sha256:3b6bb8085308b1e8`; belief `sha256:ec938485ec8098a9`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Meridian Aquaculture Audit Group
Audit reference: MAAG-26-SH-0214
Site: Saltmarsh Point Hatchery
Date: 5 May 2026
Item checked: Mortality records for every female stocked into the maturation tanks in 2024 and 2025
Method: Review of daily maturation-tank mortality logs for every female in both years, checked against the stocking register and the attending aquatic veterinarian's monthly health reports
Finding: Recorded share of stocked females that died within 60 days of stocking: 26% for females stocked in 2024; 14% for females stocked in 2025. Records were complete and matched the stocking register and veterinary reports for both years.
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

Hashes: attribution `sha256:2ecf3191be426198`; belief `sha256:60c462d381642894`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Meridian Aquaculture Audit Group
Audit reference: MAAG-26-SH-0214
Site: Saltmarsh Point Hatchery
Date: 5 May 2026
Item checked: Mortality records for every female stocked into the maturation tanks in 2024 and 2025
Method: Review of daily maturation-tank mortality logs for every female in both years, checked against the stocking register and the attending aquatic veterinarian's monthly health reports
Finding: Recorded share of stocked females that died within 60 days of stocking: 14% for females stocked in 2024; 26% for females stocked in 2025. Records were complete and matched the stocking register and veterinary reports for both years.
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

Hashes: attribution `sha256:8134ff7e07646517`; belief `sha256:52872f75baca9a8f`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Meridian Aquaculture Audit Group
Audit reference: MAAG-26-SH-0214
Site: Saltmarsh Point Hatchery
Date: 5 May 2026
Item checked: Mortality records for every female stocked into the maturation tanks in 2024 and 2025
Method: Review of daily maturation-tank mortality logs for every female in both years, checked against the stocking register and the attending aquatic veterinarian's monthly health reports
Finding: Recorded share of stocked females that died within 60 days of stocking: 26% for females stocked in 2024; 26% for females stocked in 2025. Records were complete and matched the stocking register and veterinary reports for both years.
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

Hashes: attribution `sha256:7856fefde779aeeb`; belief `sha256:005de5fe9d637549`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Meridian Aquaculture Audit Group
Audit reference: MAAG-26-SH-0214
Site: Saltmarsh Point Hatchery
Date: 5 May 2026
Item checked: Mortality records for every female stocked into the maturation tanks in 2024 and 2025
Method: Review of daily maturation-tank mortality logs for every female in both years, checked against the stocking register and the attending aquatic veterinarian's monthly health reports
Finding: Recorded share of stocked females that died within 60 days of stocking: 26% for females stocked in 2024; 14% for females stocked in 2025. Records were complete and matched the stocking register and veterinary reports for both years.
Status: Confirmed

Coverage: This audit assessed broodstock mortality records only. It did not assess eyestalk condition of broodstock or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:06844c37b0fe0549`; belief `sha256:5c656a00ace54652`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Meridian Aquaculture Audit Group
Audit reference: MAAG-26-SH-0214
Site: Saltmarsh Point Hatchery
Date: 5 May 2026
Item checked: Mortality records for every female stocked into the maturation tanks in 2024 and 2025
Method: Review of daily maturation-tank mortality logs for every female in both years, checked against the stocking register and the attending aquatic veterinarian's monthly health reports
Finding: Recorded share of stocked females that died within 60 days of stocking: 14% for females stocked in 2024; 26% for females stocked in 2025. Records were complete and matched the stocking register and veterinary reports for both years.
Status: Confirmed

Coverage: This audit assessed broodstock mortality records only. It did not assess eyestalk condition of broodstock or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:3f62cdbbf616fd40`; belief `sha256:0f5f9875354c6d73`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Meridian Aquaculture Audit Group
Audit reference: MAAG-26-SH-0214
Site: Saltmarsh Point Hatchery
Date: 5 May 2026
Item checked: Mortality records for every female stocked into the maturation tanks in 2024 and 2025
Method: Review of daily maturation-tank mortality logs for every female in both years, checked against the stocking register and the attending aquatic veterinarian's monthly health reports
Finding: Recorded share of stocked females that died within 60 days of stocking: 26% for females stocked in 2024; 26% for females stocked in 2025. Records were complete and matched the stocking register and veterinary reports for both years.
Status: Confirmed

Coverage: This audit assessed broodstock mortality records only. It did not assess eyestalk condition of broodstock or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:7ffcfe17a3bbff23`; belief `sha256:316b51bbfbd34e83`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Meridian Aquaculture Audit Group
Audit reference: MAAG-26-SH-0214
Site: Saltmarsh Point Hatchery
Date: 5 May 2026
Status: Verified ✓
~~~~
