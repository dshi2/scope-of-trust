"""Extension development cases for P2 revision 3 (six further audit families).

SYNTHETIC. All organisations and facilities are fictional. Thresholds, indicators,
audit methods and numbers are plausible placeholders and MUST be reviewed by a
welfare scientist or certification auditor before any confirmatory use
(REVISION_3_SPEC.md §8). Builder-authored, pending welfare-expert review, exactly as
the base cases in p2v3/cases.py. Every indicator is "lower is better".

This set is run separately from the base set (stimuli_ext.jsonl, written by
generate_ext.py) with the same renderer, system prompt, task text, condition matrix and
frozen model configuration. Pre-declared reporting rule: if the extension run completes
it is reported alongside the base run; otherwise only the base run is reported.
Base artifacts (cases.py, stimuli_dev.jsonl, DESIGN_MATRIX_dev.csv) are untouched.

Conventions are identical to p2v3/cases.py and enforced by the same tests
(tests/test_cases.py, tests/test_leakage.py, which run over CASES + CASES_EXT):
  * Practice and outcome claims refer only to closed periods 2024 and 2025 (PERIOD_YEARS).
  * Practice claims start "Throughout 2025,"; the practice audit covers the whole of 2025
    and its item equals the claim (claims are narrowed to what the records show, e.g.
    "monthly recorded", "at every daily check").
  * Every audit is dated in 2026 (AUDIT_YEAR).
  * R (other-topic inspection) is the only claim about 2026; its inspection is the audit itself.
  * Q_obs is about the facility's *recorded* figures; complete, matching records settle it.

Families (species / practice / indicator / outcome audit method), all distinct from the
base six and from each other:
  dev-dairy-cubicle      dairy cows / cows per cubicle / lameness / contracted mobility scorer, 6 herd sessions a year
  dev-salmon-density     Atlantic salmon / monthly stocking density / fin damage / processing-plant grading of harvest batches
  dev-turkey-darkness    turkeys / dark period in lighting programme / leg-disorder culls / daily cull sheets per bird placed
  dev-duck-water         Pekin ducks / open water troughs / eye condition / on-farm scoring at 35 days
  dev-rabbit-mats        breeding does / foot-rest mats / sore hocks / monthly whole-herd health checks
  dev-calf-colostrum     dairy calves / colostrum feeding / respiratory treatments / medicine book vs vet prescriptions
"""

from .cases import AUDIT_YEAR, PERIOD_YEARS  # noqa: F401  (same chronology as the base set)

CASES_EXT = [
    {
        "id": "dev-dairy-cubicle",
        "species": "dairy cows",
        "practice_type": "cubicle_ratio",
        "indicator_type": "dairy_lameness",
        "facility": "Penhallow Dairy",
        "sister": "Penhallow Moor",
        "issuer": "Fernleigh Dairy Standards Board",
        "ref": "FDSB/26/0317",
        "date": "24 February 2026",
        "practice_claim": "Throughout 2025, no housed group of lactating cows at Penhallow Dairy contained more cows than it had usable cubicles in any weekly group list.",
        "practice_item": "Cow numbers and usable cubicles in every housed lactating group in every weekly group list for 2025",
        "practice_method": "Review of the 52 weekly group lists exported from the 2025 parlour software, compared with cubicle counts from the shed plans and the 2025 cubicle repair log",
        "practice_finding": "In every weekly group list for 2025, each housed lactating group had no more cows than usable cubicles; the highest ratio in any group was 0.96 cows per cubicle.",
        "item_short": "cow numbers per cubicle",
        "indicator_short": "mobility score records",
        "indicator_name": "the recorded share of lame cows",
        "q_obs": "The recorded share of lame cows at Penhallow Dairy was lower in 2025 than in 2024.",
        "q_welfare": "The overall welfare of the cows at Penhallow Dairy improved from 2024 to 2025.",
        "q_cause": "This reduction in recorded lameness was caused by giving every cow a cubicle.",
        "outcome_item": "Mobility score records for all lactating cows in 2024 and 2025",
        "outcome_method": "Review of the contracted mobility scorer's reports from six scoring sessions per year, each covering every cow in milk on the day, checked against the milk-recording herd lists",
        "outcome_template": "Recorded share of scored cows lame (mobility score 2 or 3), mean of the six sessions: {y1} in 2024; {y2} in 2025. Records were complete and matched the herd lists for both years.",
        "better": "21%", "worse": "32%",
        "r_claim": "Penhallow Dairy passed its 2026 pressure-system inspection.",
        "r_item": "The milking-plant vacuum system, air compressor and hot-water boiler",
        "r_method": "On-site examination of pressure vessels and relief valves, and review of the written scheme of examination",
        "r_finding": "All pressure systems examined met the applicable regulatory requirements.",
        "s_claim": "Throughout 2025, no housed group of lactating cows at Penhallow Moor, a sister site, contained more cows than it had usable cubicles in any weekly group list either.",
        "s_finding": "In every weekly group list for 2025, each housed lactating group at Penhallow Moor had no more cows than usable cubicles; the highest ratio in any group was 0.98 cows per cubicle.",
    },
    {
        "id": "dev-salmon-density",
        "species": "Atlantic salmon (marine grow-out)",
        "practice_type": "fish_stocking_density",
        "indicator_type": "fin_damage",
        "facility": "Camas Ruadh Marine Site",
        "sister": "Camas Ruadh North",
        "issuer": "Nordlys Aquaculture Certification AS",
        "ref": "NAC-SAL-2026-0081",
        "date": "9 April 2026",
        "practice_claim": "Throughout 2025, the monthly recorded stocking density in every pen at Camas Ruadh Marine Site was at or below 15 kg/m³.",
        "practice_item": "Monthly recorded stocking density in every stocked pen for each month of 2025",
        "practice_method": "Review of 2025 monthly biomass estimates from fish-counter and sample-weighing records, and of pen net volumes, for every pen, checked against feed delivery and harvest weight records",
        "practice_finding": "The highest monthly stocking density recorded in any pen during 2025 was 13.6 kg/m³, at or below the 15 kg/m³ limit.",
        "item_short": "stocking density in pens",
        "indicator_short": "fin condition records",
        "indicator_name": "the recorded share of fish with severe fin damage at harvest",
        "q_obs": "The recorded share of fish from Camas Ruadh Marine Site with severe fin damage at harvest was lower for 2025 harvests than for 2024 harvests.",
        "q_welfare": "The overall welfare of the fish at Camas Ruadh Marine Site improved from 2024 to 2025.",
        "q_cause": "This reduction in recorded fin damage was caused by the lower stocking density.",
        "outcome_item": "Fin condition grading records for every harvest batch in 2024 and 2025",
        "outcome_method": "Review of the processing plant's quality grading reports (200 fish graded per harvest batch) for every batch in both years, checked against the plant's grading database",
        "outcome_template": "Recorded share of graded fish with severe fin damage (score 3 or 4 on any fin): {y1} for 2024 harvests; {y2} for 2025 harvests. Records were complete and matched the grading database for both years.",
        "better": "7.5%", "worse": "13.2%",
        "r_claim": "Camas Ruadh Marine Site passed its 2026 navigational marking inspection.",
        "r_item": "Navigation lights, marker buoys and site boundary markings",
        "r_method": "On-site inspection from a survey vessel, with review of the navigation-light maintenance log",
        "r_finding": "All navigational markings inspected met the applicable regulatory requirements.",
        "s_claim": "Throughout 2025, the monthly recorded stocking density in every pen at Camas Ruadh North, a sister site, was also at or below 15 kg/m³.",
        "s_finding": "The highest monthly stocking density recorded in any pen at Camas Ruadh North during 2025 was 14.1 kg/m³, at or below the 15 kg/m³ limit.",
    },
    {
        "id": "dev-turkey-darkness",
        "species": "turkeys",
        "practice_type": "dark_period",
        "indicator_type": "leg_culls",
        "facility": "Gorsey Bank Turkeys",
        "sister": "Gorsey Bank Top",
        "issuer": "Calloway & Reid Farm Audit LLP",
        "ref": "CR/TK/2026/22",
        "date": "18 May 2026",
        "practice_claim": "Throughout 2025, every turkey house at Gorsey Bank Turkeys gave birds older than 7 days at least 6 hours of continuous darkness in every 24 hours.",
        "practice_item": "Lighting programme in every house on every day of 2025 on which birds older than 7 days were present",
        "practice_method": "Review of lighting-controller logs downloaded from every house for the whole of 2025, checked against flock placement and depopulation dates",
        "practice_finding": "Controller logs for every house showed at least 6 hours of continuous darkness in every 24-hour period of 2025 on which birds older than 7 days were present.",
        "item_short": "lighting programmes",
        "indicator_short": "leg-disorder cull records",
        "indicator_name": "the recorded share of birds culled for leg disorders",
        "q_obs": "The recorded share of birds at Gorsey Bank Turkeys culled for leg disorders was lower for flocks depopulated in 2025 than for flocks depopulated in 2024.",
        "q_welfare": "The overall welfare of the turkeys at Gorsey Bank Turkeys improved from 2024 to 2025.",
        "q_cause": "This reduction in recorded leg-disorder culls was caused by the longer dark period.",
        "outcome_item": "Cull records for all flocks depopulated in 2024 and 2025",
        "outcome_method": "Review of daily mortality and cull sheets, with the recorded cull reason, for every flock in both years, checked against placement numbers and processing-plant intake records",
        "outcome_template": "Recorded share of placed birds culled for leg disorders: {y1} for flocks depopulated in 2024; {y2} for flocks depopulated in 2025. Records were complete and matched placement and intake records for both years.",
        "better": "2.1%", "worse": "3.8%",
        "r_claim": "Gorsey Bank Turkeys passed its 2026 LPG installation safety inspection.",
        "r_item": "LPG tanks, pipework and gas brooders in all five houses",
        "r_method": "On-site inspection of tanks, pipework, regulators and gas-detection alarms",
        "r_finding": "All LPG installations inspected met the applicable regulatory requirements.",
        "s_claim": "Throughout 2025, every turkey house at Gorsey Bank Top, a sister site, also gave birds older than 7 days at least 6 hours of continuous darkness in every 24 hours.",
        "s_finding": "Controller logs for every house at Gorsey Bank Top showed at least 6 hours of continuous darkness in every 24-hour period of 2025 on which birds older than 7 days were present.",
    },
    {
        "id": "dev-duck-water",
        "species": "Pekin ducks",
        "practice_type": "open_water",
        "indicator_type": "eye_condition",
        "facility": "Fenmoor Duck Farm",
        "sister": "Fenmoor Drove",
        "issuer": "Anglian Livestock Audit Cooperative",
        "ref": "ALAC 2026-114",
        "date": "2 June 2026",
        "practice_claim": "Throughout 2025, every house at Fenmoor Duck Farm holding ducks aged 14 days or older had open water troughs at least 10 cm deep at every daily check.",
        "practice_item": "Open water troughs in every house holding ducks aged 14 days or older during 2025",
        "practice_method": "Review of 2025 trough installation records, daily stockperson check sheets recording trough water depth, and flock placement records for every house",
        "practice_finding": "Daily check sheets for 2025 were complete and recorded open water troughs at least 10 cm deep in every house holding ducks aged 14 days or older, at every check.",
        "item_short": "open water troughs",
        "indicator_short": "eye condition records",
        "indicator_name": "the recorded share of ducks with dirty or crusted eyes",
        "q_obs": "The recorded share of ducks at Fenmoor Duck Farm with dirty or crusted eyes at 35 days of age was lower for 2025 flocks than for 2024 flocks.",
        "q_welfare": "The overall welfare of the ducks at Fenmoor Duck Farm improved from 2024 to 2025.",
        "q_cause": "This reduction in recorded eye problems was caused by the open water troughs.",
        "outcome_item": "Eye condition scores at 35 days of age for all flocks placed in 2024 and 2025",
        "outcome_method": "Review of eye and nostril scoring sheets (60 ducks scored per house per flock) for every flock in both years, checked against the farm's flock summary sheets",
        "outcome_template": "Recorded share of scored ducks with dirty or crusted eyes (score 2 or 3): {y1} for 2024 flocks; {y2} for 2025 flocks. Records were complete and matched the flock summary sheets for both years.",
        "better": "6%", "worse": "17%",
        "r_claim": "Fenmoor Duck Farm passed its 2026 lifting-equipment inspection.",
        "r_item": "Lifting equipment: the forklift, telehandler and feed-bin hoist",
        "r_method": "On-site thorough examination of chains, hydraulics, brakes and load-rating plates",
        "r_finding": "All lifting equipment examined met the applicable regulatory requirements.",
        "s_claim": "Throughout 2025, every house at Fenmoor Drove, a sister site, holding ducks aged 14 days or older also had open water troughs at least 10 cm deep at every daily check.",
        "s_finding": "Daily check sheets at Fenmoor Drove for 2025 were complete and recorded open water troughs at least 10 cm deep in every house holding ducks aged 14 days or older, at every check.",
    },
    {
        "id": "dev-rabbit-mats",
        "species": "rabbits (breeding does)",
        "practice_type": "foot_rest_mats",
        "indicator_type": "pododermatitis",
        "facility": "Larkspur Rabbitry",
        "sister": "Larkspur Hollow",
        "issuer": "Corvane Livestock Inspection Bureau",
        "ref": "CLIB-R-26-0045",
        "date": "30 March 2026",
        "practice_claim": "Throughout 2025, every breeding doe at Larkspur Rabbitry was kept in a pen with a plastic foot-rest mat covering at least 40% of the floor.",
        "practice_item": "Foot-rest mats in every pen used for breeding does during 2025",
        "practice_method": "Review of 2025 pen inventories, mat purchase invoices and the weekly pen maintenance log for every doe pen, with mat areas taken from the supplier's specifications and pen floor plans",
        "practice_finding": "Every doe pen in use during 2025 was fitted with a foot-rest mat covering at least 45% of the floor; the maintenance log recorded no doe pen without a mat at any time in 2025.",
        "item_short": "foot-rest mats",
        "indicator_short": "hock condition records",
        "indicator_name": "the recorded share of does with sore hocks",
        "q_obs": "The recorded share of does at Larkspur Rabbitry with sore hocks was lower in 2025 than in 2024.",
        "q_welfare": "The overall welfare of the rabbits at Larkspur Rabbitry improved from 2024 to 2025.",
        "q_cause": "This reduction in recorded sore hocks was caused by the foot-rest mats.",
        "outcome_item": "Hock condition records for all breeding does in 2024 and 2025",
        "outcome_method": "Review of the monthly health-check sheets, on which both hind feet of every doe present are scored, for every month of both years, checked against the doe register",
        "outcome_template": "Recorded share of does with sore hocks (lesion score 2 or higher on either hind foot), averaged over the twelve monthly checks: {y1} in 2024; {y2} in 2025. Records were complete and matched the doe register for both years.",
        "better": "9%", "worse": "16%",
        "r_claim": "Larkspur Rabbitry passed its 2026 standby-generator inspection.",
        "r_item": "The standby generator, its fuel tank and the automatic changeover switch",
        "r_method": "On-site load test of the generator and inspection of the fuel tank and changeover switch",
        "r_finding": "The generator, fuel tank and changeover switch met the applicable regulatory requirements.",
        "s_claim": "Throughout 2025, every breeding doe at Larkspur Hollow, a sister site, was also kept in a pen with a plastic foot-rest mat covering at least 40% of the floor.",
        "s_finding": "Every doe pen in use at Larkspur Hollow during 2025 was fitted with a foot-rest mat covering at least 42% of the floor; the maintenance log recorded no doe pen without a mat at any time in 2025.",
    },
    {
        "id": "dev-calf-colostrum",
        "species": "dairy calves",
        "practice_type": "colostrum_feeding",
        "indicator_type": "calf_respiratory_treatment",
        "facility": "Whitlow Cross Farm",
        "sister": "Whitlow Cross Lower",
        "issuer": "Stannary Veterinary Audit Ltd.",
        "ref": "SVA/0726/1903",
        "date": "21 July 2026",
        "practice_claim": "Throughout 2025, every calf born alive at Whitlow Cross Farm was fed at least 3 litres of colostrum within 6 hours of birth.",
        "practice_item": "Colostrum feeding of every calf born alive during 2025",
        "practice_method": "Review of 2025 calving records, colostrum feeding logs and national calf registrations for every calf born alive during 2025",
        "practice_finding": "Feeding logs for every calf born alive during 2025 recorded at least 3 litres of colostrum within 6 hours of birth; calf numbers matched calving records and registrations.",
        "item_short": "colostrum feeding",
        "indicator_short": "calf treatment records",
        "indicator_name": "the recorded share of calves treated for respiratory disease in their first 60 days",
        "q_obs": "The recorded share of calves at Whitlow Cross Farm treated for respiratory disease in their first 60 days was lower for calves born in 2025 than for calves born in 2024.",
        "q_welfare": "The overall welfare of the calves at Whitlow Cross Farm improved from 2024 to 2025.",
        "q_cause": "This reduction in recorded respiratory treatments was caused by the colostrum feeding.",
        "outcome_item": "Respiratory disease treatment records for all calves born in 2024 and 2025",
        "outcome_method": "Review of the farm medicine book and calf health records for every calf born in both years, checked against the veterinary practice's prescription records",
        "outcome_template": "Recorded share of calves treated for respiratory disease in their first 60 days: {y1} for calves born in 2024; {y2} for calves born in 2025. Records were complete and matched the prescription records for both years.",
        "better": "12%", "worse": "23%",
        "r_claim": "Whitlow Cross Farm passed its 2026 refrigerant leak-check inspection.",
        "r_item": "Refrigerant circuits of the bulk milk tank and the ice-bank cooler",
        "r_method": "On-site leak test of every refrigerant circuit and review of the equipment service record",
        "r_finding": "All refrigerant circuits tested met the applicable regulatory requirements.",
        "s_claim": "Throughout 2025, every calf born alive at Whitlow Cross Lower, a sister site, was also fed at least 3 litres of colostrum within 6 hours of birth.",
        "s_finding": "Feeding logs for every calf born alive at Whitlow Cross Lower during 2025 recorded at least 3 litres of colostrum within 6 hours of birth; calf numbers matched calving records and registrations.",
    },
]

# Builder's claim-evidence notes for expert review (same shape as p2v3/rubric.PRACTICE_NOTES):
# (claim quantifier/population/period, what the record shows, residual risk). NOT validation.
PRACTICE_NOTES_EXT = {
    "dev-dairy-cubicle": ("every housed lactating group, in every weekly group list for 2025", "52 weekly group lists against shed-plan cubicle counts and the repair log",
                          "Claim narrowed to weekly snapshots; does not show within-week regrouping or cubicles that were present but unusable for reasons not logged."),
    "dev-salmon-density": ("every stocked pen, monthly recorded density, every month of 2025", "monthly biomass estimates and net volumes, cross-checked against feed and harvest weights",
                           "Biomass between harvests is estimated from counts and sample weights; claim narrowed to the monthly recorded figure, not instantaneous density."),
    "dev-turkey-darkness": ("every house, every 24 h of 2025 with birds older than 7 days", "controller logs for every house for all of 2025 against placement/depopulation dates",
                            "Controller logs show programmed and switched lighting; light leakage into the house during the dark period is not measured."),
    "dev-duck-water": ("every house with ducks aged 14 days or older, at every daily check in 2025", "complete daily check sheets recording trough depth, plus installation and placement records",
                       "Claim narrowed to what daily checks show; does not establish continuous access or water cleanliness between checks."),
    "dev-rabbit-mats": ("every breeding doe kept at any time in 2025", "pen inventories, invoices, weekly maintenance log; mat areas from supplier specification and floor plans",
                        "Coverage percentage is computed from specifications, not measured in each pen; relies on the maintenance log recording any pen without a mat."),
    "dev-calf-colostrum": ("every calf born alive in 2025", "feeding logs for every calf, reconciled with calving records and national registrations",
                           "Volume and timing are as logged by staff; colostrum quality (e.g. Brix) and passive transfer are not part of the claim or the record."),
}
