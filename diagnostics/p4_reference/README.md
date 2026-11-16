# P4 finite-sample reference

Offline statistical diagnostic based on P2 revision 3 at
`7bf0e8e3a0bd5db280abda7dec26cbd56ea59760`. No model outputs, paid calls,
confirmatory analysis, sample-size approval or protocol changes are included.
This is a conservative comparator for the proposed paired noninferiority
analysis, not a replacement for that analysis. Independent review is pending.

## Why this exists

P4 asks whether scope clarification preserves correct acceptance, with a
prespecified tolerable decrease. An all-agree sample must not produce an
interval of zero width. More repeated calls must not masquerade as more
independent cases. Missing responses must not be silently discarded.

## Bound and assumptions

For each independent case i, let D_i be the mean of scheduled binary
scope-minus-base acceptance differences across its repeats. Let L_i be one
if any repeat could have scope < base. Complete missing scope responses as 0
and missing base responses as 1 to obtain this indicator conservatively.
For every possible completion, D_i >= -L_i. Consequently the population
mean difference Delta >= -P(L_i=1).

For n IID cases and K such indicators, a one-sided Clopper-Pearson upper
confidence bound U on P(L_i=1) gives the conservative lower bound -U for
Delta. Noninferiority requires -U > -delta. Dependence within a case is
allowed; dependence between cases is not. Analyze models separately.
The reference does not certify that generated cases are IID or representative.
If cases are dependent within a source cohort, that cohort needs to be the
independent unit or another justified analysis is needed.

Every case must have the same prespecified repeat count. The caller must
validate scheduled IDs and completeness against the run matrix. A missing
case cannot be detected from an absent dictionary entry. Missing outcomes
are conservatively bounded, not attributed to model behavior. Infrastructure
reliability must still be reported separately.

This bound ignores gains. It can be extremely conservative, particularly
with many repeats. Zero difference does not guarantee useful power: equal
gain and loss rates can make this reference unable to establish
noninferiority even with very large n. It is a guardrail and comparison
method, not an efficient paired estimator. A separate positive-control gate
is necessary: agreeing on incorrect rejections is not useful acceptance.

## Reproduce

From this directory, using an environment with NumPy and SciPy:

```sh
python3 -m unittest -v test_reference
python3 reference.py > validation.json
```

Eight tests cover boundary uncertainty, agreement with SciPy's exact
binomial interval, exhaustive missing-pair completions, repeat counting,
input validation, dependence limits and exact small-n coverage.

The synthetic grid has 2,160 points, each with exact binomial probabilities
and 20,000 Monte Carlo draws as a numerical cross-check. It varies margin,
loss/gain rates, independent case count, repeats, dependence and missingness.
The beta-Bernoulli model is imposed on the derived possible-loss indicator.
It is not the full protocol's proposed logit random-effects simulation, a
calibration to pilot data, or a test of arm-dependent missingness. The output
records its seed, source hash and dependency versions. No synthetic output
belongs in real-run analysis directories.

The checked grid satisfies its nominal noncoverage and null rejection
constraints at each alpha. These checks supplement the bound's argument;
they do not establish validity of another method or the real experimental
sampling process.

## What the numbers do and do not establish

With zero observed possible-loss cases, U = 1 - alpha**(1/n). The smallest
n that can certify noninferiority in that best-case sample is:

| One-sided alpha | 5-point margin | 1-point margin |
|---|---:|---:|
| .025 | 72 | 368 |
| .00625 | 99 | 505 |

These are best-case thresholds for this reference, **not powered sample-size
recommendations**. The second row uses a conservative four-test Bonferroni
planning allocation; it neither implements Holm nor freezes the study's
alpha allocation. Model multiplicity needs its own declared treatment.

For example, at n=1,000, delta=.05 and alpha=.025, the synthetic equal
gain/loss scenario (.01 each) has essentially 100% rejection probability
with one repeat but only about 2.9% with five independent repeats under
this intentionally blunt bound. This is a limitation of the reference,
not evidence that collecting repeats is generally harmful.

## Required next comparison

An independent methods reviewer should check the derivation and missingness
envelope. Compare an efficient paired method with this reference on the
same declared estimand, including boundary cases and informative missingness.
Then simulate the actual planned design over plausible paired discordance,
case dependence and acceptance rates. Freeze the margin based on its
practical meaning and choose n from a prespecified power/precision target.
This file does not authorize a pilot or confirmatory run.

Reference: [SciPy exact binomial proportion intervals](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats._result_classes.BinomTestResult.proportion_ci.html).
