# Rendered stimuli: `dev-sow-farrowing` (expansion batch ba)

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

### attribution context  `sha256:937fb61df0df7aa4`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Cotterdale Breeding Unit. Animals: pigs (farrowing sows and litters).
The supplier states:
[P] Throughout 2025, every sow that farrowed at Cotterdale Breeding Unit did so in a free-farrowing pen fitted with sloped anti-crush walls and a heated creep area.
[Q_obs] The recorded share of liveborn piglets at Cotterdale Breeding Unit crushed before weaning was lower for litters born in 2025 than for litters born in 2024.
[Q_welfare] The overall welfare of the sows and piglets at Cotterdale Breeding Unit improved from 2024 to 2025.
[Q_cause] This reduction in recorded crushing was caused by the anti-crush pen design.
[R] Cotterdale Breeding Unit passed its 2026 water-abstraction licence inspection.
[S] Throughout 2025, every sow that farrowed at Cotterdale Moor Unit, a sister site, also did so in a free-farrowing pen fitted with sloped anti-crush walls and a heated creep area.

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

### belief context  `sha256:8d0e81e6a042f845`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Cotterdale Breeding Unit. Animals: pigs (farrowing sows and litters).
The supplier states:
[P] Throughout 2025, every sow that farrowed at Cotterdale Breeding Unit did so in a free-farrowing pen fitted with sloped anti-crush walls and a heated creep area.
[Q_obs] The recorded share of liveborn piglets at Cotterdale Breeding Unit crushed before weaning was lower for litters born in 2025 than for litters born in 2024.
[Q_welfare] The overall welfare of the sows and piglets at Cotterdale Breeding Unit improved from 2024 to 2025.
[Q_cause] This reduction in recorded crushing was caused by the anti-crush pen design.
[R] Cotterdale Breeding Unit passed its 2026 water-abstraction licence inspection.
[S] Throughout 2025, every sow that farrowed at Cotterdale Moor Unit, a sister site, also did so in a free-farrowing pen fitted with sloped anti-crush walls and a heated creep area.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every sow that farrowed at Cotterdale Breeding Unit did so in a free-farrowing pen fitted with sloped anti-crush walls and a heated creep area." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of liveborn piglets crushed before weaning between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of liveborn piglets crushed before weaning.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of liveborn piglets crushed before weaning at this facility.
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

### attribution context  `sha256:cc06d4f606349702`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Cotterdale Breeding Unit. Animals: pigs (farrowing sows and litters).
The supplier states:
[Q_obs] The recorded share of liveborn piglets at Cotterdale Breeding Unit crushed before weaning was lower for litters born in 2025 than for litters born in 2024.
[Q_welfare] The overall welfare of the sows and piglets at Cotterdale Breeding Unit improved from 2024 to 2025.
[Q_cause] This reduction in recorded crushing was caused by the anti-crush pen design.
[R] Cotterdale Breeding Unit passed its 2026 water-abstraction licence inspection.
[S] Throughout 2025, every sow that farrowed at Cotterdale Moor Unit, a sister site, also did so in a free-farrowing pen fitted with sloped anti-crush walls and a heated creep area.

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

### belief context  `sha256:a7620fd36f85a169`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Cotterdale Breeding Unit. Animals: pigs (farrowing sows and litters).
The supplier states:
[Q_obs] The recorded share of liveborn piglets at Cotterdale Breeding Unit crushed before weaning was lower for litters born in 2025 than for litters born in 2024.
[Q_welfare] The overall welfare of the sows and piglets at Cotterdale Breeding Unit improved from 2024 to 2025.
[Q_cause] This reduction in recorded crushing was caused by the anti-crush pen design.
[R] Cotterdale Breeding Unit passed its 2026 water-abstraction licence inspection.
[S] Throughout 2025, every sow that farrowed at Cotterdale Moor Unit, a sister site, also did so in a free-farrowing pen fitted with sloped anti-crush walls and a heated creep area.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every sow that farrowed at Cotterdale Breeding Unit did so in a free-farrowing pen fitted with sloped anti-crush walls and a heated creep area." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of liveborn piglets crushed before weaning between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of liveborn piglets crushed before weaning.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of liveborn piglets crushed before weaning at this facility.
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

Hashes: attribution `sha256:7afcb2a91be6be78`; belief `sha256:312cc3bbcf8efefc`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wealden Pig Assurance Ltd.
Audit reference: WPA-26-0784
Site: Cotterdale Breeding Unit
Date: 23 March 2026
Item checked: Farrowing pen used for every farrowing during 2025
Method: Review of 2025 farrowing records and pen allocation sheets for every farrowing, compared with the farrowing-house plans and the 2025 pen maintenance log
Finding: Every farrowing recorded during 2025 took place in a free-farrowing pen fitted with sloped anti-crush walls and a heated creep area; no use of a farrowing crate was recorded.
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

Hashes: attribution `sha256:133779df13c593d0`; belief `sha256:054210136dca9a95`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wealden Pig Assurance Ltd.
Audit reference: WPA-26-0784
Site: Cotterdale Breeding Unit
Date: 23 March 2026
Item checked: Farrowing pen used for every farrowing during 2025
Method: Review of 2025 farrowing records and pen allocation sheets for every farrowing, compared with the farrowing-house plans and the 2025 pen maintenance log
Finding: Every farrowing recorded during 2025 took place in a free-farrowing pen fitted with sloped anti-crush walls and a heated creep area; no use of a farrowing crate was recorded.
Status: Confirmed

Coverage: This audit assessed farrowing pen design only. It did not assess piglet crushing records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:a5c6f9df8dc90403`; belief `sha256:aad266075897b6e4`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wealden Pig Assurance Ltd.
Audit reference: WPA-26-0784
Site: Cotterdale Breeding Unit
Date: 23 March 2026
Item checked: Farrowing pen used for every farrowing during 2025
Method: Review of 2025 farrowing records and pen allocation sheets for every farrowing, compared with the farrowing-house plans and the 2025 pen maintenance log
Finding: Every farrowing recorded during 2025 took place in a free-farrowing pen fitted with sloped anti-crush walls and a heated creep area; no use of a farrowing crate was recorded.
Status: Confirmed

Coverage:
  Assessed: farrowing pen design
  Not assessed: piglet crushing records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:5af1e3abc6a42327`; belief `sha256:87bee4e99945aa21`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wealden Pig Assurance Ltd.
Audit reference: WPA-26-0784
Site: Cotterdale Breeding Unit
Date: 23 March 2026
Item checked: The borehole abstraction point, its meter and the abstraction returns
Method: On-site inspection of the borehole headworks and meter, and review of the abstraction returns
Finding: The abstraction point, meter and returns met the applicable regulatory requirements.
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

Hashes: attribution `sha256:eaca3464206bc9c0`; belief `sha256:d5de9185b97c17ff`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wealden Pig Assurance Ltd.
Audit reference: WPA-26-0784
Site: Cotterdale Moor Unit
Date: 23 March 2026
Item checked: Farrowing pen used for every farrowing during 2025
Method: Review of 2025 farrowing records and pen allocation sheets for every farrowing, compared with the farrowing-house plans and the 2025 pen maintenance log
Finding: Every farrowing recorded at Cotterdale Moor Unit during 2025 took place in a free-farrowing pen fitted with sloped anti-crush walls and a heated creep area; no use of a farrowing crate was recorded.
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

Hashes: attribution `sha256:19bb62a0e21adcf1`; belief `sha256:c3c689486ee72f2c`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wealden Pig Assurance Ltd.
Audit reference: WPA-26-0784
Site: Cotterdale Breeding Unit
Date: 23 March 2026
Item checked: Pre-weaning mortality records for every litter born in 2024 and 2025
Method: Review of the litter records in the herd-management software, with the recorded reason for each piglet death, for every litter in both years, checked against the daily farrowing-house sheets and fallen-stock collection tickets
Finding: Recorded share of liveborn piglets crushed before weaning: 7.3% for litters born in 2024; 4.6% for litters born in 2025. Records were complete and matched the daily sheets and collection tickets for both years.
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

Hashes: attribution `sha256:fb15b0a8f60d72f4`; belief `sha256:8bd81a2307f2f8e0`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wealden Pig Assurance Ltd.
Audit reference: WPA-26-0784
Site: Cotterdale Breeding Unit
Date: 23 March 2026
Item checked: Pre-weaning mortality records for every litter born in 2024 and 2025
Method: Review of the litter records in the herd-management software, with the recorded reason for each piglet death, for every litter in both years, checked against the daily farrowing-house sheets and fallen-stock collection tickets
Finding: Recorded share of liveborn piglets crushed before weaning: 4.6% for litters born in 2024; 7.3% for litters born in 2025. Records were complete and matched the daily sheets and collection tickets for both years.
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

Hashes: attribution `sha256:16e01abeea19c592`; belief `sha256:59f5cb782867e776`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wealden Pig Assurance Ltd.
Audit reference: WPA-26-0784
Site: Cotterdale Breeding Unit
Date: 23 March 2026
Item checked: Pre-weaning mortality records for every litter born in 2024 and 2025
Method: Review of the litter records in the herd-management software, with the recorded reason for each piglet death, for every litter in both years, checked against the daily farrowing-house sheets and fallen-stock collection tickets
Finding: Recorded share of liveborn piglets crushed before weaning: 7.3% for litters born in 2024; 7.3% for litters born in 2025. Records were complete and matched the daily sheets and collection tickets for both years.
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

Hashes: attribution `sha256:be2e228af0d265e3`; belief `sha256:3bc805e95a3834b3`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wealden Pig Assurance Ltd.
Audit reference: WPA-26-0784
Site: Cotterdale Breeding Unit
Date: 23 March 2026
Item checked: Pre-weaning mortality records for every litter born in 2024 and 2025
Method: Review of the litter records in the herd-management software, with the recorded reason for each piglet death, for every litter in both years, checked against the daily farrowing-house sheets and fallen-stock collection tickets
Finding: Recorded share of liveborn piglets crushed before weaning: 7.3% for litters born in 2024; 4.6% for litters born in 2025. Records were complete and matched the daily sheets and collection tickets for both years.
Status: Confirmed

Coverage: This audit assessed piglet crushing records only. It did not assess farrowing pen design or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:b2e4f15c725f6888`; belief `sha256:91fb7eea09f63e52`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wealden Pig Assurance Ltd.
Audit reference: WPA-26-0784
Site: Cotterdale Breeding Unit
Date: 23 March 2026
Item checked: Pre-weaning mortality records for every litter born in 2024 and 2025
Method: Review of the litter records in the herd-management software, with the recorded reason for each piglet death, for every litter in both years, checked against the daily farrowing-house sheets and fallen-stock collection tickets
Finding: Recorded share of liveborn piglets crushed before weaning: 4.6% for litters born in 2024; 7.3% for litters born in 2025. Records were complete and matched the daily sheets and collection tickets for both years.
Status: Confirmed

Coverage: This audit assessed piglet crushing records only. It did not assess farrowing pen design or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:1077e35d7353e086`; belief `sha256:b4594794cfe7a63c`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wealden Pig Assurance Ltd.
Audit reference: WPA-26-0784
Site: Cotterdale Breeding Unit
Date: 23 March 2026
Item checked: Pre-weaning mortality records for every litter born in 2024 and 2025
Method: Review of the litter records in the herd-management software, with the recorded reason for each piglet death, for every litter in both years, checked against the daily farrowing-house sheets and fallen-stock collection tickets
Finding: Recorded share of liveborn piglets crushed before weaning: 7.3% for litters born in 2024; 7.3% for litters born in 2025. Records were complete and matched the daily sheets and collection tickets for both years.
Status: Confirmed

Coverage: This audit assessed piglet crushing records only. It did not assess farrowing pen design or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:fd2be761ea8e099e`; belief `sha256:abc942bed08f96d7`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Wealden Pig Assurance Ltd.
Audit reference: WPA-26-0784
Site: Cotterdale Breeding Unit
Date: 23 March 2026
Status: Verified ✓
~~~~
