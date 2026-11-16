# Rendered stimuli: `dev-breeder-matingratio` (batch bb)

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

### attribution context  `sha256:190d255a9b9f0bf3`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Wickerslade Breeder Farm. Animals: broiler breeders (laying flocks).
The supplier states:
[P] Throughout 2025, every laying flock at Wickerslade Breeder Farm had no more than 9 males per 100 females at every weekly bird count.
[Q_obs] The recorded share of hens at Wickerslade Breeder Farm with back or head wounds was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Wickerslade Breeder Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded hen wounds was caused by the lower mating ratio.
[R] Wickerslade Breeder Farm passed its 2026 biomass-boiler emissions inspection.
[S] Throughout 2025, every laying flock at Wickerslade Common, a sister site, also had no more than 9 males per 100 females at every weekly bird count.

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

### belief context  `sha256:c344c51ec703e6f7`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Wickerslade Breeder Farm. Animals: broiler breeders (laying flocks).
The supplier states:
[P] Throughout 2025, every laying flock at Wickerslade Breeder Farm had no more than 9 males per 100 females at every weekly bird count.
[Q_obs] The recorded share of hens at Wickerslade Breeder Farm with back or head wounds was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Wickerslade Breeder Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded hen wounds was caused by the lower mating ratio.
[R] Wickerslade Breeder Farm passed its 2026 biomass-boiler emissions inspection.
[S] Throughout 2025, every laying flock at Wickerslade Common, a sister site, also had no more than 9 males per 100 females at every weekly bird count.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every laying flock at Wickerslade Breeder Farm had no more than 9 males per 100 females at every weekly bird count." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of hens with back or head wounds between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of hens with back or head wounds.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of hens with back or head wounds at this facility.
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

### attribution context  `sha256:ab989ccd85250bde`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Wickerslade Breeder Farm. Animals: broiler breeders (laying flocks).
The supplier states:
[Q_obs] The recorded share of hens at Wickerslade Breeder Farm with back or head wounds was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Wickerslade Breeder Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded hen wounds was caused by the lower mating ratio.
[R] Wickerslade Breeder Farm passed its 2026 biomass-boiler emissions inspection.
[S] Throughout 2025, every laying flock at Wickerslade Common, a sister site, also had no more than 9 males per 100 females at every weekly bird count.

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

### belief context  `sha256:9d9cf7c429928f5f`

~~~~text
SECTION 1: SUPPLIER STATEMENTS
Supplier: Wickerslade Breeder Farm. Animals: broiler breeders (laying flocks).
The supplier states:
[Q_obs] The recorded share of hens at Wickerslade Breeder Farm with back or head wounds was lower in 2025 than in 2024.
[Q_welfare] The overall welfare of the birds at Wickerslade Breeder Farm improved from 2024 to 2025.
[Q_cause] This reduction in recorded hen wounds was caused by the lower mating ratio.
[R] Wickerslade Breeder Farm passed its 2026 biomass-boiler emissions inspection.
[S] Throughout 2025, every laying flock at Wickerslade Common, a sister site, also had no more than 9 males per 100 females at every weekly bird count.

SECTION 2: AUDIT RECORDS
No audit record is included in this file.

Filing notes:
- This file was compiled by the procurement office for the committee's autumn meeting.
- The committee meets in Room 4 of the procurement building.

SECTION 3: BACKGROUND FOR YOUR ESTIMATE
Treat the following as true facts about the population of facilities this supplier belongs to.
1. Statement P: "Throughout 2025, every laying flock at Wickerslade Breeder Farm had no more than 9 males per 100 females at every weekly bird count." Among facilities of this type, the corresponding statement is true for 50%.
2. Among facilities for which it is true, 75% show a fall in the recorded share of hens with back or head wounds between consecutive years. Among the others, 25% do.
3. When a supplier makes statement P, it is true 80% of the time.
4. Every supplier makes the statements shown as Q_obs, Q_welfare and Q_cause, whether or not they are true. Once it is known whether P is true, nothing else the supplier states carries any information about the recorded share of hens with back or head wounds.
5. Whether the corresponding statement is true at the sister site, and the results of inspections on other topics, are unrelated to whether P is true and to the recorded share of hens with back or head wounds at this facility.
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

Hashes: attribution `sha256:a5980339691ee0e8`; belief `sha256:e1d0ca27917a7044`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Brantwood Poultry Audit Services
Audit reference: BPAS-BB-26-0388
Site: Wickerslade Breeder Farm
Date: 16 March 2026
Item checked: Male and female numbers in every laying flock at every weekly bird count in 2025
Method: Review of the 2025 weekly bird-count sheets and male placement and removal records for every house, checked against the hatchery's 2025 placement records
Finding: Weekly bird-count sheets for 2025 were complete; the highest ratio recorded in any laying flock at any count in 2025 was 8.6 males per 100 females.
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

Hashes: attribution `sha256:8130dc626d0eb44e`; belief `sha256:46443707cbb4a843`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Brantwood Poultry Audit Services
Audit reference: BPAS-BB-26-0388
Site: Wickerslade Breeder Farm
Date: 16 March 2026
Item checked: Male and female numbers in every laying flock at every weekly bird count in 2025
Method: Review of the 2025 weekly bird-count sheets and male placement and removal records for every house, checked against the hatchery's 2025 placement records
Finding: Weekly bird-count sheets for 2025 were complete; the highest ratio recorded in any laying flock at any count in 2025 was 8.6 males per 100 females.
Status: Confirmed

Coverage: This audit assessed mating ratio only. It did not assess hen injury records or any other animal-based outcome, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:0a03c4a2bea3169f`; belief `sha256:2d408ae954a59f40`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Brantwood Poultry Audit Services
Audit reference: BPAS-BB-26-0388
Site: Wickerslade Breeder Farm
Date: 16 March 2026
Item checked: Male and female numbers in every laying flock at every weekly bird count in 2025
Method: Review of the 2025 weekly bird-count sheets and male placement and removal records for every house, checked against the hatchery's 2025 placement records
Finding: Weekly bird-count sheets for 2025 were complete; the highest ratio recorded in any laying flock at any count in 2025 was 8.6 males per 100 females.
Status: Confirmed

Coverage:
  Assessed: mating ratio
  Not assessed: hen injury records; other animal-based outcomes; cause of any change in animal outcomes
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

Hashes: attribution `sha256:243b58d35309aab4`; belief `sha256:3b1a29f0469242db`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Brantwood Poultry Audit Services
Audit reference: BPAS-BB-26-0388
Site: Wickerslade Breeder Farm
Date: 16 March 2026
Item checked: The biomass boiler, its flue and the wood-chip store
Method: On-site emissions test and inspection of the flue and fuel store
Finding: The boiler, flue and fuel store met the applicable regulatory requirements.
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

Hashes: attribution `sha256:d39e60e731063cd3`; belief `sha256:6690c3ccced00999`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Brantwood Poultry Audit Services
Audit reference: BPAS-BB-26-0388
Site: Wickerslade Common
Date: 16 March 2026
Item checked: Male and female numbers in every laying flock at every weekly bird count in 2025
Method: Review of the 2025 weekly bird-count sheets and male placement and removal records for every house, checked against the hatchery's 2025 placement records
Finding: Weekly bird-count sheets at Wickerslade Common for 2025 were complete; the highest ratio recorded in any laying flock at any count in 2025 was 8.9 males per 100 females.
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

Hashes: attribution `sha256:bc176c1003798a86`; belief `sha256:02e1e8d260c0a2fa`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Brantwood Poultry Audit Services
Audit reference: BPAS-BB-26-0388
Site: Wickerslade Breeder Farm
Date: 16 March 2026
Item checked: Hen injury records for every laying flock in 2024 and 2025
Method: Review of the attending veterinarian's monthly flock visit reports, at each of which 50 hens per house were examined for back and head wounds, checked against the veterinary practice's visit records
Finding: Recorded share of examined hens with back or head wounds, averaged over the monthly visits: 15% in 2024; 7% in 2025. Records were complete and matched the practice's visit records for both years.
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

Hashes: attribution `sha256:b628abada84bdf76`; belief `sha256:00a89d2ec9e3905d`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Brantwood Poultry Audit Services
Audit reference: BPAS-BB-26-0388
Site: Wickerslade Breeder Farm
Date: 16 March 2026
Item checked: Hen injury records for every laying flock in 2024 and 2025
Method: Review of the attending veterinarian's monthly flock visit reports, at each of which 50 hens per house were examined for back and head wounds, checked against the veterinary practice's visit records
Finding: Recorded share of examined hens with back or head wounds, averaged over the monthly visits: 7% in 2024; 15% in 2025. Records were complete and matched the practice's visit records for both years.
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

Hashes: attribution `sha256:1f997e205f792938`; belief `sha256:f324d9344e878079`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Brantwood Poultry Audit Services
Audit reference: BPAS-BB-26-0388
Site: Wickerslade Breeder Farm
Date: 16 March 2026
Item checked: Hen injury records for every laying flock in 2024 and 2025
Method: Review of the attending veterinarian's monthly flock visit reports, at each of which 50 hens per house were examined for back and head wounds, checked against the veterinary practice's visit records
Finding: Recorded share of examined hens with back or head wounds, averaged over the monthly visits: 15% in 2024; 15% in 2025. Records were complete and matched the practice's visit records for both years.
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

Hashes: attribution `sha256:504309df73da2f79`; belief `sha256:d23011e4cbde93ff`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Brantwood Poultry Audit Services
Audit reference: BPAS-BB-26-0388
Site: Wickerslade Breeder Farm
Date: 16 March 2026
Item checked: Hen injury records for every laying flock in 2024 and 2025
Method: Review of the attending veterinarian's monthly flock visit reports, at each of which 50 hens per house were examined for back and head wounds, checked against the veterinary practice's visit records
Finding: Recorded share of examined hens with back or head wounds, averaged over the monthly visits: 15% in 2024; 7% in 2025. Records were complete and matched the practice's visit records for both years.
Status: Confirmed

Coverage: This audit assessed hen injury records only. It did not assess mating ratio or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:85b84fedf3b2bfd6`; belief `sha256:4b3aff36103cf879`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Brantwood Poultry Audit Services
Audit reference: BPAS-BB-26-0388
Site: Wickerslade Breeder Farm
Date: 16 March 2026
Item checked: Hen injury records for every laying flock in 2024 and 2025
Method: Review of the attending veterinarian's monthly flock visit reports, at each of which 50 hens per house were examined for back and head wounds, checked against the veterinary practice's visit records
Finding: Recorded share of examined hens with back or head wounds, averaged over the monthly visits: 7% in 2024; 15% in 2025. Records were complete and matched the practice's visit records for both years.
Status: Confirmed

Coverage: This audit assessed hen injury records only. It did not assess mating ratio or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:2e9ae53932deafa8`; belief `sha256:e165b5f078f1d0ed`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Brantwood Poultry Audit Services
Audit reference: BPAS-BB-26-0388
Site: Wickerslade Breeder Farm
Date: 16 March 2026
Item checked: Hen injury records for every laying flock in 2024 and 2025
Method: Review of the attending veterinarian's monthly flock visit reports, at each of which 50 hens per house were examined for back and head wounds, checked against the veterinary practice's visit records
Finding: Recorded share of examined hens with back or head wounds, averaged over the monthly visits: 15% in 2024; 15% in 2025. Records were complete and matched the practice's visit records for both years.
Status: Confirmed

Coverage: This audit assessed hen injury records only. It did not assess mating ratio or any other practice, and it did not assess the cause of any change in animal outcomes.
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

Hashes: attribution `sha256:cb003183080aa321`; belief `sha256:c82ac83d57fa7c8b`

~~~~text
SECTION 2: AUDIT RECORDS
AUDIT RECORD
Issued by: Brantwood Poultry Audit Services
Audit reference: BPAS-BB-26-0388
Site: Wickerslade Breeder Farm
Date: 16 March 2026
Status: Verified ✓
~~~~
