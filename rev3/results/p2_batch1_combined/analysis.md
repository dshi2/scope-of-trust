# P2 pilot analysis

**DIAGNOSTIC PILOT on development cases (one author, one template family). Interval method provisional; P4 margin unapproved; not confirmatory evidence.**

## deepseek-v3.2

Calls 1680, spend $1.5296. Status {'ok': 1680}. Parse {'ok': 1680}. Truncated 0. Served provider {'AtlasCloud': 1680}; served model {'deepseek/deepseek-v3.2': 1680}.

| contrast | definition | estimate | 95% CI (provisional) | p vs 0 (Holm P1–P3) | worst–best bounds | cases |
|---|---|---|---|---|---|---|
| P1 | B/none - A/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (1) | +0.000 to +0.000 | 12 |
| P2 | B/none - D1/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (1) | +0.000 to +0.000 | 12 |
| P3 | C/none - B/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (1) | +0.000 to +0.000 | 12 |
| P4 | E_scope/improved - E/improved on correct_acceptance | +0.000 | [-0.301, +0.301] | no decision (margin not fixed); one-sided 97.5% LB -0.301 | +0.000 to +0.000 | 12 |

Components (spec §6; only Q_obs is confirmatory):

| contrast | unsupported_q_obs | unsupported_q_cause | unsupported_q_welfare | unsupported_obs_or_cause |
|---|---|---|---|---|
| P1 | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] |
| P2 | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] |
| P3 | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] |

Validity / positive controls (must pass before contrasts are read):

| check | cell | rate | 95% CI over cases (t, clipped) | cases | trials |
|---|---|---|---|---|---|
| V1_correct_acceptance | E/improved | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V1_correct_acceptance | E_scope/improved | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V2_correct_refutation | E/worsened | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V2_correct_refutation | E/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V2_correct_refutation | E_scope/worsened | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V2_correct_refutation | E_scope/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V3_manipulation_check | B/none | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V3_manipulation_check | C/none | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V3_manipulation_check | C_prime/none | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V3_manipulation_check | D1/none | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V3_manipulation_check | D2/none | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |

| cell | unsupported Q_obs rate | n | belief MAE | n |
|---|---|---|---|---|
| A/none | 0.000 | 60 | 0.000 | 60 |
| A0/none | 0.000 | 60 | 0.000 | 60 |
| B/none | 0.000 | 60 | 0.000 | 60 |
| C/none | 0.000 | 60 | 0.000 | 60 |
| C_prime/none | 0.000 | 60 | 0.000 | 60 |
| D1/none | 0.000 | 60 | 0.000 | 60 |
| D2/none | 0.000 | 60 | 0.000 | 60 |
| E/improved | 0.000 | 60 | 0.029 | 60 |
| E/unchanged | 0.000 | 60 | 0.011 | 60 |
| E/worsened | 0.000 | 60 | 0.022 | 60 |
| E_scope/improved | 0.000 | 60 | 0.035 | 60 |
| E_scope/unchanged | 0.000 | 60 | 0.000 | 60 |
| E_scope/worsened | 0.000 | 60 | 0.000 | 60 |
| V/none | 0.000 | 60 | nan | 0 |

## gpt-oss-120b

Calls 1680, spend $0.2255. Status {'ok': 1680}. Parse {'ok': 1680}. Truncated 0. Served provider {'DeepInfra': 1680}; served model {'openai/gpt-oss-120b': 1680}.

| contrast | definition | estimate | 95% CI (provisional) | p vs 0 (Holm P1–P3) | worst–best bounds | cases |
|---|---|---|---|---|---|---|
| P1 | B/none - A/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (1) | +0.000 to +0.000 | 12 |
| P2 | B/none - D1/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (1) | +0.000 to +0.000 | 12 |
| P3 | C/none - B/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (1) | +0.000 to +0.000 | 12 |
| P4 | E_scope/improved - E/improved on correct_acceptance | +0.000 | [-0.301, +0.301] | no decision (margin not fixed); one-sided 97.5% LB -0.301 | +0.000 to +0.000 | 12 |

Components (spec §6; only Q_obs is confirmatory):

| contrast | unsupported_q_obs | unsupported_q_cause | unsupported_q_welfare | unsupported_obs_or_cause |
|---|---|---|---|---|
| P1 | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] |
| P2 | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] |
| P3 | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] |

Validity / positive controls (must pass before contrasts are read):

| check | cell | rate | 95% CI over cases (t, clipped) | cases | trials |
|---|---|---|---|---|---|
| V1_correct_acceptance | E/improved | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V1_correct_acceptance | E_scope/improved | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V2_correct_refutation | E/worsened | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V2_correct_refutation | E/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V2_correct_refutation | E_scope/worsened | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V2_correct_refutation | E_scope/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V3_manipulation_check | B/none | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V3_manipulation_check | C/none | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V3_manipulation_check | C_prime/none | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V3_manipulation_check | D1/none | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V3_manipulation_check | D2/none | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |

| cell | unsupported Q_obs rate | n | belief MAE | n |
|---|---|---|---|---|
| A/none | 0.000 | 60 | 0.000 | 60 |
| A0/none | 0.000 | 60 | 0.000 | 60 |
| B/none | 0.000 | 60 | 0.000 | 60 |
| C/none | 0.000 | 60 | 0.000 | 60 |
| C_prime/none | 0.000 | 60 | 0.000 | 60 |
| D1/none | 0.000 | 60 | 0.000 | 60 |
| D2/none | 0.000 | 60 | 0.000 | 60 |
| E/improved | 0.000 | 60 | 0.000 | 60 |
| E/unchanged | 0.000 | 60 | 0.000 | 60 |
| E/worsened | 0.000 | 60 | 0.000 | 60 |
| E_scope/improved | 0.000 | 60 | 0.000 | 60 |
| E_scope/unchanged | 0.000 | 60 | 0.000 | 60 |
| E_scope/worsened | 0.000 | 60 | 0.000 | 60 |
| V/none | 0.000 | 60 | nan | 0 |

## kimi-k2-0905

Calls 1680, spend $4.3767. Status {'ok': 1680}. Parse {'ok': 1649, 'malformed': 28, 'invalid': 3}. Truncated 28. Served provider {'Novita': 1680}; served model {'moonshotai/kimi-k2-0905': 1680}.

| contrast | definition | estimate | 95% CI (provisional) | p vs 0 (Holm P1–P3) | worst–best bounds | cases |
|---|---|---|---|---|---|---|
| P1 | B/none - A/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (1) | -0.033 to +0.000 | 12 |
| P2 | B/none - D1/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (1) | +0.000 to +0.000 | 12 |
| P3 | C/none - B/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (1) | +0.000 to +0.000 | 12 |
| P4 | E_scope/improved - E/improved on correct_acceptance | +0.000 | [-0.301, +0.301] | no decision (margin not fixed); one-sided 97.5% LB -0.301 | +0.000 to +0.000 | 12 |

Components (spec §6; only Q_obs is confirmatory):

| contrast | unsupported_q_obs | unsupported_q_cause | unsupported_q_welfare | unsupported_obs_or_cause |
|---|---|---|---|---|
| P1 | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] |
| P2 | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] |
| P3 | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] |

Validity / positive controls (must pass before contrasts are read):

| check | cell | rate | 95% CI over cases (t, clipped) | cases | trials |
|---|---|---|---|---|---|
| V1_correct_acceptance | E/improved | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V1_correct_acceptance | E_scope/improved | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V2_correct_refutation | E/worsened | 1.000 | [1.000, 1.000] (degenerate) | 12 | 59 |
| V2_correct_refutation | E/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V2_correct_refutation | E_scope/worsened | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V2_correct_refutation | E_scope/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V3_manipulation_check | B/none | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V3_manipulation_check | C/none | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V3_manipulation_check | C_prime/none | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V3_manipulation_check | D1/none | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V3_manipulation_check | D2/none | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |

| cell | unsupported Q_obs rate | n | belief MAE | n |
|---|---|---|---|---|
| A/none | 0.000 | 58 | 0.023 | 60 |
| A0/none | 0.000 | 60 | 0.037 | 56 |
| B/none | 0.000 | 60 | 0.018 | 60 |
| C/none | 0.000 | 60 | 0.033 | 60 |
| C_prime/none | 0.000 | 60 | 0.021 | 60 |
| D1/none | 0.000 | 60 | 0.013 | 60 |
| D2/none | 0.000 | 60 | 0.010 | 59 |
| E/improved | 0.000 | 60 | 0.032 | 58 |
| E/unchanged | 0.000 | 60 | 0.147 | 58 |
| E/worsened | 0.000 | 59 | 0.078 | 59 |
| E_scope/improved | 0.000 | 60 | 0.068 | 60 |
| E_scope/unchanged | 0.000 | 60 | 0.166 | 58 |
| E_scope/worsened | 0.000 | 60 | 0.127 | 56 |
| V/none | 0.050 | 60 | nan | 0 |

## qwen3-235b-a22b-2507

Calls 1680, spend $0.2822. Status {'ok': 1680}. Parse {'ok': 1680}. Truncated 0. Served provider {'DeepInfra': 1680}; served model {'qwen/qwen3-235b-a22b-2507': 1680}.

| contrast | definition | estimate | 95% CI (provisional) | p vs 0 (Holm P1–P3) | worst–best bounds | cases |
|---|---|---|---|---|---|---|
| P1 | B/none - A/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (1) | +0.000 to +0.000 | 12 |
| P2 | B/none - D1/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (1) | +0.000 to +0.000 | 12 |
| P3 | C/none - B/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (1) | +0.000 to +0.000 | 12 |
| P4 | E_scope/improved - E/improved on correct_acceptance | +0.000 | [-0.301, +0.301] | no decision (margin not fixed); one-sided 97.5% LB -0.301 | +0.000 to +0.000 | 12 |

Components (spec §6; only Q_obs is confirmatory):

| contrast | unsupported_q_obs | unsupported_q_cause | unsupported_q_welfare | unsupported_obs_or_cause |
|---|---|---|---|---|
| P1 | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] |
| P2 | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] |
| P3 | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] | +0.000 [-0.301, +0.301] |

Validity / positive controls (must pass before contrasts are read):

| check | cell | rate | 95% CI over cases (t, clipped) | cases | trials |
|---|---|---|---|---|---|
| V1_correct_acceptance | E/improved | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V1_correct_acceptance | E_scope/improved | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V2_correct_refutation | E/worsened | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V2_correct_refutation | E/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V2_correct_refutation | E_scope/worsened | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V2_correct_refutation | E_scope/unchanged | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V3_manipulation_check | B/none | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V3_manipulation_check | C/none | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V3_manipulation_check | C_prime/none | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V3_manipulation_check | D1/none | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |
| V3_manipulation_check | D2/none | 1.000 | [1.000, 1.000] (degenerate) | 12 | 60 |

| cell | unsupported Q_obs rate | n | belief MAE | n |
|---|---|---|---|---|
| A/none | 0.000 | 60 | 0.033 | 60 |
| A0/none | 0.000 | 60 | 0.148 | 60 |
| B/none | 0.000 | 60 | 0.065 | 60 |
| C/none | 0.000 | 60 | 0.087 | 60 |
| C_prime/none | 0.000 | 60 | 0.084 | 60 |
| D1/none | 0.000 | 60 | 0.025 | 60 |
| D2/none | 0.000 | 60 | 0.035 | 60 |
| E/improved | 0.000 | 60 | 0.067 | 60 |
| E/unchanged | 0.000 | 60 | 0.412 | 60 |
| E/worsened | 0.000 | 60 | 0.251 | 60 |
| E_scope/improved | 0.000 | 60 | 0.064 | 60 |
| E_scope/unchanged | 0.000 | 60 | 0.443 | 60 |
| E_scope/worsened | 0.000 | 60 | 0.244 | 60 |
| V/none | 0.533 | 60 | nan | 0 |

## deepseek-v3.2: secondary family (S, ledger) and exploratory (X)

Q_obs stays the primary endpoint; nothing below substitutes for it. Holm runs within the S family over exactly: S2_D2_vs_A, S3_cause_B_vs_A, S3_cause_B_vs_D1, S3_cause_C_vs_B, S3_overreach_Escope_vs_E. Everything else is descriptive, equivalence-only (S1) or exploratory (X, never in Holm).

Evidence hierarchy (equal-case rates, 95% case t interval clipped to [0, 1]):

| cell | unsupported Q_obs (primary) | unsupported Q_welfare (S4) | unsupported Q_cause (S3) | cases |
|---|---|---|---|---|
| A | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| B | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| D1 | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| C | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |

| contrast | ledger | role | definition | estimate | 95% CI | p vs 0 (Holm S) | cases |
|---|---|---|---|---|---|---|---|
| S1_Cprime_vs_C | S1 | equivalence (TOST margin open): decide() with a SESOI only; not in Holm | C_prime/none - C/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (not in Holm) | 12 |
| S2_D2_vs_A | S2 | formal secondary test (Holm within S) | D2/none - A/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (1) | 12 |
| S3_cause_B_vs_A | S3 | formal secondary test (Holm within S) | B/none - A/none on unsupported_q_cause | +0.000 | [-0.301, +0.301] | 1 (1) | 12 |
| S3_cause_B_vs_D1 | S3 | formal secondary test (Holm within S) | B/none - D1/none on unsupported_q_cause | +0.000 | [-0.301, +0.301] | 1 (1) | 12 |
| S3_cause_C_vs_B | S3 | formal secondary test (Holm within S) | C/none - B/none on unsupported_q_cause | +0.000 | [-0.301, +0.301] | 1 (1) | 12 |
| S3_overreach_Escope_vs_E | S3 | formal secondary test (Holm within S) | E_scope/improved - E/improved on causal_overreach | +0.000 | [-0.301, +0.301] | 1 (1) | 12 |
| X1_A0_vs_A | X1 | exploratory (never in Holm) | A0/none - A/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (not in Holm) | 12 |
| X2_V_vs_A | X2 | exploratory (never in Holm) | V/none - A/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (not in Holm) | 12 |
| X2_V_vs_B | X2 | exploratory (never in Holm) | V/none - B/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (not in Holm) | 12 |

S1 C_prime − C (equivalence; SESOI None): no decision: SESOI not set. Case t comparison interval [+0.000, +0.000].

| rate | ledger | role | definition | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|---|---|---|
| S2_P_spillover_in_D2 | S2 | descriptive (named in the ledger; no test) | D2/none on p_marked_true | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| S3_causal_overreach_E_improved | S3 | descriptive (named in the ledger; no test) | E/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| S3_causal_overreach_Escope_improved | S3 | descriptive (named in the ledger; no test) | E_scope/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| S4_welfare_overgeneralisation_E_improved | S4 | descriptive (named in the ledger; no test) | E/improved on unsupported_q_welfare | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |

S4 unsupported Q_welfare by cell (E/improved is the ledger rate; the rest descriptive):

| cell | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|
| A/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| A0/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| B/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| C/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| C_prime/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| D1/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| D2/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E/improved | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E/worsened | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E_scope/improved | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E_scope/worsened | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E_scope/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| V/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |

S5: separate belief elicitation (context 2, with the stipulated population model and the independence statements); not the attribution judgment and never pooled with it.

| cell | gold | mean p(Q_obs) [CI] | signed error [CI] | abs error [CI] | cases |
|---|---|---|---|---|---|
| A/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| A0/none | 0.500 | 0.500 [0.500, 0.500] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| B/none | 0.750 | 0.750 [0.750, 0.750] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| C/none | 0.750 | 0.750 [0.750, 0.750] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| C_prime/none | 0.750 | 0.750 [0.750, 0.750] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| D1/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| D2/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| E/improved | 1.000 | 0.971 [0.941, 1.000] | -0.029 [-0.059, +0.001] | 0.029 [-0.001, 0.059] | 12 |
| E/worsened | 0.000 | 0.022 [0.000, 0.054] | +0.022 [-0.010, +0.054] | 0.022 [-0.010, 0.054] | 12 |
| E/unchanged | 0.000 | 0.011 [0.000, 0.035] | +0.011 [-0.013, +0.035] | 0.011 [-0.013, 0.035] | 12 |
| E_scope/improved | 1.000 | 0.965 [0.930, 1.000] | -0.035 [-0.070, +0.000] | 0.035 [-0.000, 0.070] | 12 |
| E_scope/worsened | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| E_scope/unchanged | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| V/none | – | 0.652 [0.648, 0.655] | excluded from error (no belief gold; ledger S5) | – | 12 |

Belief shift B − A = +0.100 (normative +0.10), case t CI [+0.100, +0.100] (degenerate), 12 cases.

S6: recommendation shares are descriptive; the association with unsupported Q_obs is descriptive (case level, pooled over cells, confounded by cell), not mediation.

| cell | approve [CI] | request_more_evidence [CI] | reject [CI] | cases | unparsed |
|---|---|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| B/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| C/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.050 [0.000, 0.129] | 0.950 [0.871, 1.000] | 12 | 0 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.117 [0.032, 0.202] | 0.883 [0.798, 0.968] | 12 | 0 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.083 [0.000, 0.168] | 0.917 [0.832, 1.000] | 12 | 0 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.167 [0.061, 0.273] | 0.833 [0.727, 0.939] | 12 | 0 |
| V/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |

Association (descriptive association, not mediation): per case: approve rate among trials with unsupported Q_obs minus among trials without, over cells other than E/E_scope improved; equal-case mean over cases with both: not estimable (no case has trials of both kinds) over 0 of 12 cases; trial table [approve, not] {'unsupported': [0, 0], 'supported_or_not_marked': [0, 720]}.

## gpt-oss-120b: secondary family (S, ledger) and exploratory (X)

Q_obs stays the primary endpoint; nothing below substitutes for it. Holm runs within the S family over exactly: S2_D2_vs_A, S3_cause_B_vs_A, S3_cause_B_vs_D1, S3_cause_C_vs_B, S3_overreach_Escope_vs_E. Everything else is descriptive, equivalence-only (S1) or exploratory (X, never in Holm).

Evidence hierarchy (equal-case rates, 95% case t interval clipped to [0, 1]):

| cell | unsupported Q_obs (primary) | unsupported Q_welfare (S4) | unsupported Q_cause (S3) | cases |
|---|---|---|---|---|
| A | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| B | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| D1 | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| C | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |

| contrast | ledger | role | definition | estimate | 95% CI | p vs 0 (Holm S) | cases |
|---|---|---|---|---|---|---|---|
| S1_Cprime_vs_C | S1 | equivalence (TOST margin open): decide() with a SESOI only; not in Holm | C_prime/none - C/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (not in Holm) | 12 |
| S2_D2_vs_A | S2 | formal secondary test (Holm within S) | D2/none - A/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (1) | 12 |
| S3_cause_B_vs_A | S3 | formal secondary test (Holm within S) | B/none - A/none on unsupported_q_cause | +0.000 | [-0.301, +0.301] | 1 (1) | 12 |
| S3_cause_B_vs_D1 | S3 | formal secondary test (Holm within S) | B/none - D1/none on unsupported_q_cause | +0.000 | [-0.301, +0.301] | 1 (1) | 12 |
| S3_cause_C_vs_B | S3 | formal secondary test (Holm within S) | C/none - B/none on unsupported_q_cause | +0.000 | [-0.301, +0.301] | 1 (1) | 12 |
| S3_overreach_Escope_vs_E | S3 | formal secondary test (Holm within S) | E_scope/improved - E/improved on causal_overreach | +0.000 | [-0.301, +0.301] | 1 (1) | 12 |
| X1_A0_vs_A | X1 | exploratory (never in Holm) | A0/none - A/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (not in Holm) | 12 |
| X2_V_vs_A | X2 | exploratory (never in Holm) | V/none - A/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (not in Holm) | 12 |
| X2_V_vs_B | X2 | exploratory (never in Holm) | V/none - B/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (not in Holm) | 12 |

S1 C_prime − C (equivalence; SESOI None): no decision: SESOI not set. Case t comparison interval [+0.000, +0.000].

| rate | ledger | role | definition | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|---|---|---|
| S2_P_spillover_in_D2 | S2 | descriptive (named in the ledger; no test) | D2/none on p_marked_true | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| S3_causal_overreach_E_improved | S3 | descriptive (named in the ledger; no test) | E/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| S3_causal_overreach_Escope_improved | S3 | descriptive (named in the ledger; no test) | E_scope/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| S4_welfare_overgeneralisation_E_improved | S4 | descriptive (named in the ledger; no test) | E/improved on unsupported_q_welfare | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |

S4 unsupported Q_welfare by cell (E/improved is the ledger rate; the rest descriptive):

| cell | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|
| A/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| A0/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| B/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| C/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| C_prime/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| D1/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| D2/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E/improved | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E/worsened | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E_scope/improved | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E_scope/worsened | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E_scope/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| V/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |

S5: separate belief elicitation (context 2, with the stipulated population model and the independence statements); not the attribution judgment and never pooled with it.

| cell | gold | mean p(Q_obs) [CI] | signed error [CI] | abs error [CI] | cases |
|---|---|---|---|---|---|
| A/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| A0/none | 0.500 | 0.500 [0.500, 0.500] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| B/none | 0.750 | 0.750 [0.750, 0.750] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| C/none | 0.750 | 0.750 [0.750, 0.750] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| C_prime/none | 0.750 | 0.750 [0.750, 0.750] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| D1/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| D2/none | 0.650 | 0.650 [0.650, 0.650] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| E/improved | 1.000 | 1.000 [1.000, 1.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| E/worsened | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| E/unchanged | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| E_scope/improved | 1.000 | 1.000 [1.000, 1.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| E_scope/worsened | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| E_scope/unchanged | 0.000 | 0.000 [0.000, 0.000] (degenerate) | +0.000 [+0.000, +0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| V/none | – | 0.650 [0.650, 0.650] (degenerate) | excluded from error (no belief gold; ledger S5) | – | 12 |

Belief shift B − A = +0.100 (normative +0.10), case t CI [+0.100, +0.100] (degenerate), 12 cases.

S6: recommendation shares are descriptive; the association with unsupported Q_obs is descriptive (case level, pooled over cells, confounded by cell), not mediation.

| cell | approve [CI] | request_more_evidence [CI] | reject [CI] | cases | unparsed |
|---|---|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| B/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| C/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.200 [0.000, 0.403] | 0.800 [0.597, 1.000] | 12 | 0 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.417 [0.184, 0.649] | 0.583 [0.351, 0.816] | 12 | 0 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.250 [0.086, 0.414] | 0.750 [0.586, 0.914] | 12 | 0 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.633 [0.398, 0.868] | 0.367 [0.132, 0.602] | 12 | 0 |
| V/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |

Association (descriptive association, not mediation): per case: approve rate among trials with unsupported Q_obs minus among trials without, over cells other than E/E_scope improved; equal-case mean over cases with both: not estimable (no case has trials of both kinds) over 0 of 12 cases; trial table [approve, not] {'unsupported': [0, 0], 'supported_or_not_marked': [0, 720]}.

## kimi-k2-0905: secondary family (S, ledger) and exploratory (X)

Q_obs stays the primary endpoint; nothing below substitutes for it. Holm runs within the S family over exactly: S2_D2_vs_A, S3_cause_B_vs_A, S3_cause_B_vs_D1, S3_cause_C_vs_B, S3_overreach_Escope_vs_E. Everything else is descriptive, equivalence-only (S1) or exploratory (X, never in Holm).

Evidence hierarchy (equal-case rates, 95% case t interval clipped to [0, 1]):

| cell | unsupported Q_obs (primary) | unsupported Q_welfare (S4) | unsupported Q_cause (S3) | cases |
|---|---|---|---|---|
| A | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| B | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| D1 | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| C | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |

| contrast | ledger | role | definition | estimate | 95% CI | p vs 0 (Holm S) | cases |
|---|---|---|---|---|---|---|---|
| S1_Cprime_vs_C | S1 | equivalence (TOST margin open): decide() with a SESOI only; not in Holm | C_prime/none - C/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (not in Holm) | 12 |
| S2_D2_vs_A | S2 | formal secondary test (Holm within S) | D2/none - A/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (1) | 12 |
| S3_cause_B_vs_A | S3 | formal secondary test (Holm within S) | B/none - A/none on unsupported_q_cause | +0.000 | [-0.301, +0.301] | 1 (1) | 12 |
| S3_cause_B_vs_D1 | S3 | formal secondary test (Holm within S) | B/none - D1/none on unsupported_q_cause | +0.000 | [-0.301, +0.301] | 1 (1) | 12 |
| S3_cause_C_vs_B | S3 | formal secondary test (Holm within S) | C/none - B/none on unsupported_q_cause | +0.000 | [-0.301, +0.301] | 1 (1) | 12 |
| S3_overreach_Escope_vs_E | S3 | formal secondary test (Holm within S) | E_scope/improved - E/improved on causal_overreach | +0.000 | [-0.301, +0.301] | 1 (1) | 12 |
| X1_A0_vs_A | X1 | exploratory (never in Holm) | A0/none - A/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (not in Holm) | 12 |
| X2_V_vs_A | X2 | exploratory (never in Holm) | V/none - A/none on unsupported_q_obs | +0.050 | [-0.264, +0.364] | 0.9 (not in Holm) | 12 |
| X2_V_vs_B | X2 | exploratory (never in Holm) | V/none - B/none on unsupported_q_obs | +0.050 | [-0.264, +0.364] | 0.9 (not in Holm) | 12 |

S1 C_prime − C (equivalence; SESOI None): no decision: SESOI not set. Case t comparison interval [+0.000, +0.000].

| rate | ledger | role | definition | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|---|---|---|
| S2_P_spillover_in_D2 | S2 | descriptive (named in the ledger; no test) | D2/none on p_marked_true | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| S3_causal_overreach_E_improved | S3 | descriptive (named in the ledger; no test) | E/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| S3_causal_overreach_Escope_improved | S3 | descriptive (named in the ledger; no test) | E_scope/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| S4_welfare_overgeneralisation_E_improved | S4 | descriptive (named in the ledger; no test) | E/improved on unsupported_q_welfare | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |

S4 unsupported Q_welfare by cell (E/improved is the ledger rate; the rest descriptive):

| cell | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|
| A/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 58 |
| A0/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| B/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| C/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| C_prime/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| D1/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| D2/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E/improved | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E/worsened | 0.000 | [0.000, 0.000] (degenerate) | 12 | 59 |
| E/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E_scope/improved | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E_scope/worsened | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E_scope/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| V/none | 0.017 | [0.000, 0.053] | 12 | 60 |

S5: separate belief elicitation (context 2, with the stipulated population model and the independence statements); not the attribution judgment and never pooled with it.

| cell | gold | mean p(Q_obs) [CI] | signed error [CI] | abs error [CI] | cases |
|---|---|---|---|---|---|
| A/none | 0.650 | 0.629 [0.618, 0.639] | -0.021 [-0.032, -0.011] | 0.023 [0.013, 0.033] | 12 |
| A0/none | 0.500 | 0.536 [0.518, 0.554] | +0.036 [+0.018, +0.054] | 0.036 [0.018, 0.054] | 12 |
| B/none | 0.750 | 0.732 [0.724, 0.741] | -0.018 [-0.026, -0.009] | 0.018 [0.009, 0.026] | 12 |
| C/none | 0.750 | 0.719 [0.704, 0.734] | -0.031 [-0.046, -0.016] | 0.033 [0.019, 0.046] | 12 |
| C_prime/none | 0.750 | 0.729 [0.717, 0.741] | -0.021 [-0.033, -0.009] | 0.021 [0.009, 0.033] | 12 |
| D1/none | 0.650 | 0.640 [0.631, 0.650] | -0.010 [-0.019, -0.000] | 0.013 [0.004, 0.022] | 12 |
| D2/none | 0.650 | 0.645 [0.637, 0.654] | -0.005 [-0.013, +0.004] | 0.010 [0.003, 0.016] | 12 |
| E/improved | 1.000 | 0.968 [0.951, 0.985] | -0.032 [-0.049, -0.015] | 0.032 [0.015, 0.049] | 12 |
| E/worsened | 0.000 | 0.078 [0.042, 0.114] | +0.078 [+0.042, +0.114] | 0.078 [0.042, 0.114] | 12 |
| E/unchanged | 0.000 | 0.145 [0.093, 0.197] | +0.145 [+0.093, +0.197] | 0.145 [0.093, 0.197] | 12 |
| E_scope/improved | 1.000 | 0.932 [0.904, 0.961] | -0.068 [-0.096, -0.039] | 0.068 [0.039, 0.096] | 12 |
| E_scope/worsened | 0.000 | 0.127 [0.095, 0.159] | +0.127 [+0.095, +0.159] | 0.127 [0.095, 0.159] | 12 |
| E_scope/unchanged | 0.000 | 0.167 [0.099, 0.235] | +0.167 [+0.099, +0.235] | 0.167 [0.099, 0.235] | 12 |
| V/none | – | 0.652 [0.638, 0.665] | excluded from error (no belief gold; ledger S5) | – | 12 |

Belief shift B − A = +0.104 (normative +0.10), case t CI [+0.088, +0.120], 12 cases.

S6: recommendation shares are descriptive; the association with unsupported Q_obs is descriptive (case level, pooled over cells, confounded by cell), not mediation.

| cell | approve [CI] | request_more_evidence [CI] | reject [CI] | cases | unparsed |
|---|---|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| B/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| C/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.067 [0.004, 0.129] | 0.933 [0.871, 0.996] | 12 | 0 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.300 [0.133, 0.467] | 0.700 [0.533, 0.867] | 12 | 0 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.067 [0.004, 0.129] | 0.933 [0.871, 0.996] | 12 | 0 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.333 [0.197, 0.470] | 0.667 [0.530, 0.803] | 12 | 0 |
| V/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |

Association (descriptive association, not mediation): per case: approve rate among trials with unsupported Q_obs minus among trials without, over cells other than E/E_scope improved; equal-case mean over cases with both: +0.000 [+0.000, +0.000] (degenerate) over 3 of 12 cases; trial table [approve, not] {'unsupported': [0, 3], 'supported_or_not_marked': [0, 714]}.

## qwen3-235b-a22b-2507: secondary family (S, ledger) and exploratory (X)

Q_obs stays the primary endpoint; nothing below substitutes for it. Holm runs within the S family over exactly: S2_D2_vs_A, S3_cause_B_vs_A, S3_cause_B_vs_D1, S3_cause_C_vs_B, S3_overreach_Escope_vs_E. Everything else is descriptive, equivalence-only (S1) or exploratory (X, never in Holm).

Evidence hierarchy (equal-case rates, 95% case t interval clipped to [0, 1]):

| cell | unsupported Q_obs (primary) | unsupported Q_welfare (S4) | unsupported Q_cause (S3) | cases |
|---|---|---|---|---|
| A | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| B | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| D1 | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |
| C | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 |

| contrast | ledger | role | definition | estimate | 95% CI | p vs 0 (Holm S) | cases |
|---|---|---|---|---|---|---|---|
| S1_Cprime_vs_C | S1 | equivalence (TOST margin open): decide() with a SESOI only; not in Holm | C_prime/none - C/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (not in Holm) | 12 |
| S2_D2_vs_A | S2 | formal secondary test (Holm within S) | D2/none - A/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (1) | 12 |
| S3_cause_B_vs_A | S3 | formal secondary test (Holm within S) | B/none - A/none on unsupported_q_cause | +0.000 | [-0.301, +0.301] | 1 (1) | 12 |
| S3_cause_B_vs_D1 | S3 | formal secondary test (Holm within S) | B/none - D1/none on unsupported_q_cause | +0.000 | [-0.301, +0.301] | 1 (1) | 12 |
| S3_cause_C_vs_B | S3 | formal secondary test (Holm within S) | C/none - B/none on unsupported_q_cause | +0.000 | [-0.301, +0.301] | 1 (1) | 12 |
| S3_overreach_Escope_vs_E | S3 | formal secondary test (Holm within S) | E_scope/improved - E/improved on causal_overreach | +0.000 | [-0.301, +0.301] | 1 (1) | 12 |
| X1_A0_vs_A | X1 | exploratory (never in Holm) | A0/none - A/none on unsupported_q_obs | +0.000 | [-0.301, +0.301] | 1 (not in Holm) | 12 |
| X2_V_vs_A | X2 | exploratory (never in Holm) | V/none - A/none on unsupported_q_obs | +0.533 | [+0.101, +0.801] | 0.02 (not in Holm) | 12 |
| X2_V_vs_B | X2 | exploratory (never in Holm) | V/none - B/none on unsupported_q_obs | +0.533 | [+0.101, +0.801] | 0.02 (not in Holm) | 12 |

S1 C_prime − C (equivalence; SESOI None): no decision: SESOI not set. Case t comparison interval [+0.000, +0.000].

| rate | ledger | role | definition | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|---|---|---|
| S2_P_spillover_in_D2 | S2 | descriptive (named in the ledger; no test) | D2/none on p_marked_true | 0.033 | [0.000, 0.107] | 12 | 60 |
| S3_causal_overreach_E_improved | S3 | descriptive (named in the ledger; no test) | E/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| S3_causal_overreach_Escope_improved | S3 | descriptive (named in the ledger; no test) | E_scope/improved on causal_overreach | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| S4_welfare_overgeneralisation_E_improved | S4 | descriptive (named in the ledger; no test) | E/improved on unsupported_q_welfare | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |

S4 unsupported Q_welfare by cell (E/improved is the ledger rate; the rest descriptive):

| cell | rate | 95% CI over cases | cases | trials |
|---|---|---|---|---|
| A/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| A0/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| B/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| C/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| C_prime/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| D1/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| D2/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E/improved | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E/worsened | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E_scope/improved | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E_scope/worsened | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| E_scope/unchanged | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |
| V/none | 0.000 | [0.000, 0.000] (degenerate) | 12 | 60 |

S5: separate belief elicitation (context 2, with the stipulated population model and the independence statements); not the attribution judgment and never pooled with it.

| cell | gold | mean p(Q_obs) [CI] | signed error [CI] | abs error [CI] | cases |
|---|---|---|---|---|---|
| A/none | 0.650 | 0.633 [0.619, 0.648] | -0.017 [-0.031, -0.002] | 0.033 [0.024, 0.043] | 12 |
| A0/none | 0.500 | 0.648 [0.617, 0.680] | +0.148 [+0.117, +0.180] | 0.148 [0.117, 0.180] | 12 |
| B/none | 0.750 | 0.685 [0.655, 0.716] | -0.065 [-0.095, -0.034] | 0.065 [0.034, 0.095] | 12 |
| C/none | 0.750 | 0.662 [0.640, 0.685] | -0.087 [-0.110, -0.065] | 0.087 [0.065, 0.110] | 12 |
| C_prime/none | 0.750 | 0.668 [0.643, 0.693] | -0.082 [-0.107, -0.057] | 0.084 [0.061, 0.107] | 12 |
| D1/none | 0.650 | 0.625 [0.624, 0.626] | -0.025 [-0.026, -0.024] | 0.025 [0.024, 0.026] | 12 |
| D2/none | 0.650 | 0.635 [0.624, 0.646] | -0.015 [-0.026, -0.004] | 0.035 [0.026, 0.043] | 12 |
| E/improved | 1.000 | 0.933 [0.894, 0.971] | -0.067 [-0.106, -0.029] | 0.067 [0.029, 0.106] | 12 |
| E/worsened | 0.000 | 0.251 [0.236, 0.266] | +0.251 [+0.236, +0.266] | 0.251 [0.236, 0.266] | 12 |
| E/unchanged | 0.000 | 0.412 [0.367, 0.458] | +0.412 [+0.367, +0.458] | 0.412 [0.367, 0.458] | 12 |
| E_scope/improved | 1.000 | 0.936 [0.892, 0.980] | -0.064 [-0.108, -0.020] | 0.064 [0.020, 0.108] | 12 |
| E_scope/worsened | 0.000 | 0.244 [0.209, 0.279] | +0.244 [+0.209, +0.279] | 0.244 [0.209, 0.279] | 12 |
| E_scope/unchanged | 0.000 | 0.443 [0.394, 0.493] | +0.443 [+0.394, +0.493] | 0.443 [0.394, 0.493] | 12 |
| V/none | – | 0.650 [0.634, 0.667] | excluded from error (no belief gold; ledger S5) | – | 12 |

Belief shift B − A = +0.052 (normative +0.10), case t CI [+0.016, +0.088], 12 cases.

S6: recommendation shares are descriptive; the association with unsupported Q_obs is descriptive (case level, pooled over cells, confounded by cell), not mediation.

| cell | approve [CI] | request_more_evidence [CI] | reject [CI] | cases | unparsed |
|---|---|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| B/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| C/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 1 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 8 | 44 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 1 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.500 [0.287, 0.713] | 0.500 [0.287, 0.713] | 12 | 0 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.950 [0.893, 1.000] | 0.050 [0.000, 0.107] | 12 | 0 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) | 0.767 [0.573, 0.961] | 0.233 [0.039, 0.427] | 12 | 0 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) | 0.967 [0.893, 1.000] | 0.033 [0.000, 0.107] | 12 | 0 |
| V/none | 0.000 [0.000, 0.000] (degenerate) | 1.000 [1.000, 1.000] (degenerate) | 0.000 [0.000, 0.000] (degenerate) | 12 | 0 |

Association (descriptive association, not mediation): per case: approve rate among trials with unsupported Q_obs minus among trials without, over cells other than E/E_scope improved; equal-case mean over cases with both: +0.000 [+0.000, +0.000] (degenerate) over 12 of 12 cases; trial table [approve, not] {'unsupported': [0, 32], 'supported_or_not_marked': [0, 643]}.

## Zero-event bounds on unsupported Q_obs (case level is the headline)

Per cell, unsupported Q_obs. Headline = upper95_cases: exact one-sided 95% Clopper-Pearson bound over cases, events counted as cases with >= 1 event in their repeats (1 - 0.05**(1/K) at zero; rule of three ~ 3/K). It treats cases as exchangeable draws from the builder's case population; the cases are builder-written, not a random sample. upper95_trials ASSUMES INDEPENDENT TRIALS (repeats are nested in cases), reference only.

| model | cell | events / trials (missing) | cases with event / cases | case-level 95% upper (rule of 3) | trial-level 95% upper (assumes independent trials) |
|---|---|---|---|---|---|
| deepseek-v3.2 | A/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| deepseek-v3.2 | A0/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| deepseek-v3.2 | B/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| deepseek-v3.2 | C/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| deepseek-v3.2 | C_prime/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| deepseek-v3.2 | D1/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| deepseek-v3.2 | D2/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| deepseek-v3.2 | E/worsened | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| deepseek-v3.2 | E/unchanged | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| deepseek-v3.2 | E_scope/worsened | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| deepseek-v3.2 | E_scope/unchanged | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| deepseek-v3.2 | V/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| gpt-oss-120b | A/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| gpt-oss-120b | A0/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| gpt-oss-120b | B/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| gpt-oss-120b | C/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| gpt-oss-120b | C_prime/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| gpt-oss-120b | D1/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| gpt-oss-120b | D2/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| gpt-oss-120b | E/worsened | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| gpt-oss-120b | E/unchanged | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| gpt-oss-120b | E_scope/worsened | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| gpt-oss-120b | E_scope/unchanged | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| gpt-oss-120b | V/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| kimi-k2-0905 | A/none | 0/58 (2) | 0/12 | 0.221 (0.250) | 0.050 |
| kimi-k2-0905 | A0/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| kimi-k2-0905 | B/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| kimi-k2-0905 | C/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| kimi-k2-0905 | C_prime/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| kimi-k2-0905 | D1/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| kimi-k2-0905 | D2/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| kimi-k2-0905 | E/worsened | 0/59 (1) | 0/12 | 0.221 (0.250) | 0.050 |
| kimi-k2-0905 | E/unchanged | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| kimi-k2-0905 | E_scope/worsened | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| kimi-k2-0905 | E_scope/unchanged | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| kimi-k2-0905 | V/none | 3/60 (0) | 3/12 | 0.527 | 0.124 |
| qwen3-235b-a22b-2507 | A/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| qwen3-235b-a22b-2507 | A0/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| qwen3-235b-a22b-2507 | B/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| qwen3-235b-a22b-2507 | C/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| qwen3-235b-a22b-2507 | C_prime/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| qwen3-235b-a22b-2507 | D1/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| qwen3-235b-a22b-2507 | D2/none | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| qwen3-235b-a22b-2507 | E/worsened | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| qwen3-235b-a22b-2507 | E/unchanged | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| qwen3-235b-a22b-2507 | E_scope/worsened | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| qwen3-235b-a22b-2507 | E_scope/unchanged | 0/60 (0) | 0/12 | 0.221 (0.250) | 0.049 |
| qwen3-235b-a22b-2507 | V/none | 32/60 (0) | 12/12 | 1.000 | 0.644 |

## Primary decisions (no SESOI or P4 margin is fixed)

| model | P1 | P2 | P3 | P4 | case-t comparison interval degenerate (P1/P2/P3/P4) |
|---|---|---|---|---|---|
| deepseek-v3.2 | no decision: SESOI not set | no decision: SESOI not set | no decision: SESOI not set | no decision: P4 margin not set | True/True/True/True |
| gpt-oss-120b | no decision: SESOI not set | no decision: SESOI not set | no decision: SESOI not set | no decision: P4 margin not set | True/True/True/True |
| kimi-k2-0905 | no decision: SESOI not set | no decision: SESOI not set | no decision: SESOI not set | no decision: P4 margin not set | True/True/True/True |
| qwen3-235b-a22b-2507 | no decision: SESOI not set | no decision: SESOI not set | no decision: SESOI not set | no decision: P4 margin not set | True/True/True/True |

## Unsupported Q_obs, Q_welfare, Q_cause by cell (separately; equal-case rate [case t 95%], cases with >= 1 event / cases)

### deepseek-v3.2

| cell | Q_obs | Q_welfare | Q_cause |
|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| B/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| C/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) 0/12 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) 0/12 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| V/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |

### gpt-oss-120b

| cell | Q_obs | Q_welfare | Q_cause |
|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| B/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| C/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) 0/12 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) 0/12 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| V/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |

### kimi-k2-0905

| cell | Q_obs | Q_welfare | Q_cause |
|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| B/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| C/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) 0/12 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) 0/12 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| V/none | 0.050 [0.000, 0.107] 3/12 | 0.017 [0.000, 0.053] 1/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |

### qwen3-235b-a22b-2507

| cell | Q_obs | Q_welfare | Q_cause |
|---|---|---|---|
| A/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| A0/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| B/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| C/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| C_prime/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| D1/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| D2/none | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E/improved | 0.000 [0.000, 0.000] (degenerate) 0/12 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E/worsened | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E_scope/improved | 0.000 [0.000, 0.000] (degenerate) 0/12 (correct here) | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E_scope/worsened | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| E_scope/unchanged | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |
| V/none | 0.533 [0.335, 0.731] 12/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 | 0.000 [0.000, 0.000] (degenerate) 0/12 |

## V cell (EXPLORATORY; gold contested, spec §8.6): Q_obs marked established after an unscoped stamp

| model | rate [case t 95%, clipped] | cases with event / cases | trials marked / trials (scheduled) |
|---|---|---|---|
| deepseek-v3.2 | 0.000 [0.000, 0.000] (degenerate) | 0/12 | 0/60 (60) |
| gpt-oss-120b | 0.000 [0.000, 0.000] (degenerate) | 0/12 | 0/60 (60) |
| kimi-k2-0905 | 0.050 [0.000, 0.107] | 3/12 | 3/60 (60) |
| qwen3-235b-a22b-2507 | 0.533 [0.335, 0.731] | 12/12 | 32/60 (60) |
