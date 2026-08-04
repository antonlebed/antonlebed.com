"""CAN AN UNCOUNTED TERM BE SEEN FROM INSIDE?

THE QUESTION
------------
A companion rig (explore_uncounted_term.py) established that an
interval's coverage is a function of two ratios and nothing else: the
uncounted term b against the true dispersion sigma, and the stated
half-width h against that same sigma. Every arm there carried a bias
with a KNOWN cause and was scored against a target known exactly in
Fraction --- which is the one thing a real auditor does not have. The
task people actually hold is "I ran this audit and it printed an error
bar; should I believe it?"

So: is there a statistic computable from the estimator's OWN output
that separates the three regimes without knowing the target?

Half the plane is free. sigma is the dispersion of the estimate, which
resampling estimates without reference to any truth, so h/sigma is
computable from inside. The whole question is the other coordinate.
Two instruments can be built for it, and both read b through its
n-DEPENDENCE:

  THE BOOTSTRAP TERM.  bhat = mean over resamples of Ehat* minus Ehat,
    the estimator's own bias against its own fitted world.
  THE DRIFT TERM.  Ehat on the full sample minus Ehat on a random half,
    which reads b(n) - b(n/2) directly.

A NO here is as informative as a YES: it says the direction is knowable
only from outside, which is what makes an exact-truth ruler worth
building at all.

THE HAND-ATTACK, BEFORE THE ENGINE
----------------------------------
At the knife cell both instruments are derivable, and they give the
same number. Write d_r = etahat_r - 1/2, which is about N(0, tau^2)
with tau = 1/(2 sqrt(n_r)); the estimate is Ehat = sum_r (n_r/n)(1/2 -
|d_r|), so the true bias per cell is -E|d_r| = -tau sqrt(2/pi).

  THE BOOTSTRAP.  A resampled cell rate is about d_r + Z with Z an
  independent N(0, tau^2), so E|d + Z| = E|N(0, 2 tau^2)| = 2 tau /
  sqrt(pi), against E|d| = tau sqrt(2/pi). The difference is
  tau sqrt(2/pi) (sqrt(2) - 1). So

      bhat / b  =  sqrt(2) - 1  =  0.41421      --- free of n

  The bootstrap SEES the term and UNDERSTATES it by a fixed factor.
  The absolute value is not differentiable at the truth, which is
  exactly where the knife puts it.

  THE DRIFT.  With b(n) = -c/sqrt(n), the full-minus-half difference is
  -c/sqrt(n) + c/sqrt(n/2) = c (sqrt(2) - 1)/sqrt(n). The SAME factor,
  and for the same reason: both instruments read the 1/sqrt(n)
  curvature and nothing else.

Against the companion rig's knife constant |b|/h = sqrt(2M/pi)/z =
1.5766, both inside ratios therefore land at 0.41421 * 1.5766 = 0.6531.

AND THE CONSEQUENCE THAT MAKES THIS MORE THAN TWO INSTRUMENTS.  Both
statistics are differences of b at two sample sizes, so a bias that has
CONVERGED to a constant lies in their common kernel. Coverage falls to
zero exactly when b/h diverges, h shrinks like 1/sqrt(n), and a
constant b is the plainest way to make b/h diverge. The dangerous
regime is then structurally the invisible one --- for the whole CLASS
of subsampling instruments, not for these two.

  [THE SLATE IS LEFT AS FROZEN, AND THIS PARAGRAPH'S REASON IS WRONG.
  "Differences of b at two sample sizes" is true of the drift term and
  FALSE of the bootstrap term, which estimates the estimator's bias
  against its own estimand under the fitted distribution. The kernel
  and everything downstream of it survive; what carries them is the
  MODEL CLASS, not the resampling. See F3, which states the repaired
  argument and the sense in which the class-level claim holds.]

The rival instrument is a goodness-of-fit test, which reads the model
rather than the estimate and so escapes that kernel. It gets a world
built to defeat it (below).

THE WORLDS
----------
The companion rig's three, kept exact, plus one new. M = 15 cells,
uniform cell prior, cell r carrying a label rate eta_r as a Fraction;
the target is the Bayes error sum_r P(r) min(eta_r, 1 - eta_r), a
closed form. The misspecified model pools the cells into three groups
of five.

  W_CLEAR --- none closer than 1/10 to 1/2, each group straddling it.
  W_KNIFE --- every eta_r = 1/2.
  W_MILD  --- four cells well off 1/2 and one just past it per group,
    so the pooling gap is a small exact 7/750 and the crossing falls
    inside the sample-size range.
  W_SAME  --- NEW, and the negative control for the goodness-of-fit
    instrument: three groups of five, every cell heterogeneous but
    every cell strictly BELOW 1/2. Then each group's mean is below 1/2,
    so min of the mean is the mean of the mins and THE POOLING GAP IS
    EXACTLY ZERO (checked in Fraction, printed by the rig). The model
    is flagrantly misspecified and the uncounted term is 0.

THE ARMS
--------
Fit statements only --- the bound kind is settled by the companion rig
and is not what an auditor is asking about here.

  B1 per-cell fit on W_CLEAR       (well-specified)
  B2 per-cell fit on W_KNIFE       (the knife: in-model, non-smooth)
  B3 pooled  fit on W_CLEAR        (a large converged gap)
  B4 per-cell fit on W_MILD        (the mild world's own control)
  B5 pooled  fit on W_MILD         (a small converged gap; spans the
                                    crossing across the four sizes)
  B6 pooled  fit on W_SAME         (misspecified, zero term)
  B7 per-cell fit on W_SAME        (that world's own control)

Each trial draws once, states the model-implied half-width h = z
sqrt(Ehat (1 - Ehat)/n) at z = 1.96, and computes, from that ONE sample
and nothing else: the bootstrap term bhat over B resamples of the
empirical distribution over the 2M (cell, label) categories; the
bootstrap dispersion sigmahat and the ratio h/sigmahat; the drift term
against an exact half-sample drawn without replacement; and, for the
pooled arms, the within-group Pearson statistic against the saturated
per-cell model, standardized as (X2 - dof)/sqrt(2 dof) at dof = M - 3.
For the per-cell arms that test does not exist: the model IS the
saturated one, and having no richer model to test against is the
auditor's ordinary situation rather than a gap in the rig.

A cell is scored by its MEASURED coverage against the exact target:
GOOD at 0.90 or above, BAD below 0.80, GREY between and reported
separately. A detector is a per-trial statistic with a threshold, so it
is read as a single-sample rule: the threshold is set to hold the false
alarm rate at 0.10 or below over the GOOD cells' trials, and what is
reported is the detection rate over the BAD cells' trials.

THE PREDICTIONS, FIXED BEFORE THE ENGINE WAS WRITTEN
----------------------------------------------------
  P1  CONTROL, read before anything else. The arms reproduce the
      companion rig: B2's true |b|/h in 1.55 to 1.60 at every n, and
      B1's coverage within Monte-Carlo noise of the nominal 0.95.
  P2  HAND. At the knife, bhat/b is flat in n and inside 0.35 to 0.48
      (hand value sqrt(2) - 1 = 0.4142).
  P3  HAND. At the knife, the drift ratio and the bootstrap ratio
      |.|/h agree to within 0.15 of each other, both inside 0.50 to
      0.80 (hand value 0.6531).
  P4  THE KERNEL. On B3 and on B5 at the largest n --- converged
      gaps, true |b|/h above 1 --- both inside ratios stay below 0.25.
  P5  CONTROL, negative. W_SAME's pooling gap is exactly 0 in
      Fraction; B6's coverage is within Monte-Carlo noise of nominal
      at every n; and B6's standardized goodness-of-fit statistic
      exceeds 3 at the smallest n and 50 at the largest. A
      misspecification detector firing hardest where the uncounted
      term is exactly zero.
  P6  THE FREE COORDINATE IS UNINFORMATIVE. h/sigmahat on B5 (pooled,
      bad at large n) stays within 0.30 of h/sigmahat on B4 (per-cell,
      good) at every n --- same world, same sample sizes, opposite
      verdicts, indistinguishable on the coordinate the auditor can
      see.
  P7  THE INSTRUMENT READING. At a threshold holding false alarms to
      0.10 or below on the GOOD cells, the best single-sample rule
      among the three detects below 0.5 of the BAD cells' trials.

KILL-SHAPES, AS OBSERVABLES
---------------------------
  [P1's kill FIRED AND WAS WRONG, and this block is left as frozen. P1
  did land outside its band and the rig is NOT broken: the band was
  narrower than the sampling spread of the quantity it gates, so it
  discriminated nothing. F1 carries the diagnosis and the repaired
  gate. The other kill-shapes below stand as written.]
  P1 outside its bands: the rig is broken and nothing else is read.
  P7's detection rate at or above 0.9 with false alarms at or below
    0.10: the term IS visible from inside, the answer is YES, and what
    an exact-truth ruler is FOR has to be restated.
  P5's coverage significantly below nominal: W_SAME is not a zero-term
    world, the negative control is void, and P5 is reported as a miss
    rather than restated.
  P2 outside its band: the hand-attack is wrong about the bootstrap at
    a non-differentiable point, and P3's shared-mechanism reading goes
    with it.

RUN RECORD
----------
400 trials at each of four sample sizes (500, 2000, 8000, 32000), 150
bootstrap resamples per trial, seven arms across four worlds, single
seed stream (640021). 3.8 s, peak working set 30.8 MB under the 512 MB
default. 13 of 14 checks pass; the one FAIL is P1 as frozen and is
reported below rather than restated. Exact targets in Fraction: 19/75
on W_CLEAR, 1/2 on W_KNIFE, 523/1500 on W_MILD, 77/300 on W_SAME;
pooling gaps 29/150, 0, 7/750, 0.

FINDINGS
--------
F1  CONTROL, AND THE FROZEN BAND WAS THE WRONG INSTRUMENT (P1 failed,
    P1c passed). The knife arm printed |b|/h = 1.6125, 1.5733, 1.5856,
    1.6054 against the companion rig's hand value sqrt(2M/pi)/z =
    1.5766, and the well-specified arm covered at 0.953, 0.940, 0.938,
    0.943 against a nominal 0.95 with a 3-sigma band of 0.033. So the
    arms are the companion's arms and what follows can be read.
    But P1's band of 1.55 to 1.60 FAILED at two of the four n, and the
    cause is the band and not the rig: the ratio's own standard error
    is sd(dev)/(sqrt(TRIALS) h), and three of those is 0.0454 to
    0.0485 --- WIDER than the band's half-width of 0.025. P1 was a
    HAND-VALUE band gating a MEASUREMENT, so an entirely correct run
    clears it about five times in eight (0.89 at one sample size, four
    of them independent) --- a coin the companion rig won and this one
    lost, and not a verdict either time. Tested at the
    precision the measurement actually has, every n is inside. The
    frozen check is left FAILING; the abort gate was rebuilt on P1c.
    The species is a control frozen at a tolerance nobody measured,
    and it is not a sibling of the companion rig's kill frozen on a
    saturating observable but the SAME shape: there the observable sat
    against its floor, here the tolerance sits inside the noise, and
    either way the criterion's arithmetic was never evaluated at the
    design point before the run. That is what P1c does differently ---
    it states its band as three standard errors computed from the run
    rather than as a number carried in from elsewhere.
    (A first run at 200 trials tripped the same band at
    one n; raising the trial count to the band's own did not fix it,
    which is what pointed at the band.)

F2  THE BOOTSTRAP SEES THE KNIFE TERM AND UNDERSTATES IT BY A FIXED
    FACTOR (observation, four n; the factor is hand-derived
    asymptotically before the run). bhat/b printed 0.3987, 0.4199,
    0.4113, 0.4011 across a 64-fold range of n against the pre-engine
    sqrt(2) - 1 = 0.41421 --- flat, as the derivation says it must be,
    the resampled cell rate carrying twice the variance of the fitted
    one at a point where the functional is not differentiable. The
    drift instrument lands in the same place for the same reason:
    boot/h 0.643 to 0.661 against drift/h 0.630 to 0.676, both against
    a hand 0.6530. So at the knife the inside view is not blind --- it
    is off by a knowable 2.4x, and an auditor who bootstrap-corrected
    there would remove two fifths of the term and keep three.

F3  A CONVERGED TERM IS IN THE KERNEL OF BOTH INSTRUMENTS (property
    for the construction, measured at five cells). NEITHER instrument
    has access to the target, and each replaces it differently. The
    drift term differences it away outright, reading b(n) - b(n/2).
    The bootstrap term does something subtler and more damaging: it
    measures the estimator's bias against ITS OWN estimand --- the
    number its arithmetic returns on the whole population --- which
    for a misspecified model is the model's limit and not the truth.
    Note WHERE that comes from, since the natural reading is wrong: the
    resampling here is from the RAW EMPIRICAL distribution over the 2M
    (cell, label) categories, which is saturated and not pooled. What
    drops the gap is the ESTIMAND, not what is resampled --- which is
    the same point this finding's headline makes.
    Split b(n) into the part that decays and
    the gap between the model's limit and the target --- the bootstrap
    reports the first and drops the second by construction, the drift
    differences the second away, and the two arrive at one kernel from
    two directions: a b that has stopped moving is invisible to both.
    Measured: at the five converged-gap cells
    the true |b|/h runs 4.328, 8.836, 17.706, 35.500 and 1.778, while
    the bootstrap term reports 0.148, 0.032, 0.003, 0.002, 0.001 and
    the drift term 0.140, 0.008, 0.026, 0.012, 0.036. What the reach
    actually rests on is the MODEL CLASS and not the resampling: the
    converged part of b is the gap between what the class can express
    and the target, and no statistic whose ESTIMAND is the class's own
    functional can identify it, there being nothing in the class that
    names the target. So the kernel is not a property of
    these two arithmetics but of staying inside --- which is exactly
    why the one instrument that escapes it, in F4, escapes by fitting a
    RICHER model, and why the escape buys detection of the MODEL rather
    than of the term. And the bite is that the invisible case is the
    dangerous one --- h shrinks like 1/sqrt(n), so a constant b is the
    plainest way to send b/h to infinity, and coverage to zero.

F4  THE RIVAL INSTRUMENT FIRES HARDEST WHERE THE TERM IS EXACTLY ZERO
    (the negative control, passed). On W_SAME the pooled model is
    flagrantly wrong about every cell and exactly right about the
    target --- pooling gap 0 in Fraction, and the arm covered at
    0.935, 0.955, 0.940, 0.955 --- while its standardized
    goodness-of-fit statistic read 8.0, 33.8, 136.2, 548.5, growing
    without bound in n. A goodness-of-fit test escapes F3's kernel by
    reading the MODEL rather than the estimate, and pays for it by
    detecting misspecification rather than the term: the two come
    apart completely here, because min of a group mean equals the mean
    of the mins whenever a group sits on one side of 1/2. Its cost is
    paid in the instrument reading below, where holding false alarms
    to 10% forces a threshold of 549 --- set by this world.

F5  THE COORDINATE THE AUDITOR CAN SEE IS THE ONE THAT CARRIES NO
    VERDICT (observation, four paired cells). h/sigmahat is free from
    inside, sigma being estimable by resampling with no reference to
    any truth. On one world, at the same four sample sizes, the
    per-cell arm and the pooled arm printed h/sigmahat 2.21 vs 2.01,
    2.09 vs 1.96, 2.03 vs 1.96, 2.00 vs 1.97 --- indistinguishable ---
    while their coverages went 0.920 vs 0.945, 0.930 vs 0.828, 0.955
    vs 0.562, 0.920 vs 0.065. The plane has two coordinates, exactly
    one is observable, and it is not the one that decides. And the
    observable one is not faithful everywhere, which was not predicted
    and is read against this rig's OWN true sd rather than a
    companion's: sigmahat/sd runs 0.966, 0.989, 0.965, 0.985 at the
    well-specified arm and 1.226, 1.182, 1.235, 1.268 at the knife. So
    the resampled dispersion is honest where the functional is smooth
    --- which is the control that makes the other reading mean
    something --- and overstates it by about a fifth where it is not.
    The same non-differentiability that costs F2 its factor bends the
    free coordinate too, and bends it the flattering way: a bar
    divided by an inflated sd looks better sized than it is.

F6  THE ANSWER IS NO, AND THE FAILURE IS ANTI-MONOTONE IN THE DAMAGE
    (observation, 27 cells: 17 GOOD at coverage 0.90 or above, 10 BAD
    below 0.80, one grey excluded at 0.828). As single-sample rules at
    a threshold holding false alarms to 0.10 over the GOOD cells'
    trials, the bootstrap term caught 0.432 and the drift term 0.196 of
    the BAD cells' 4000 trials. The goodness-of-fit statistic is defined
    only on the pooled arms, so its 0.167 is read over the 6 BAD cells
    it exists on --- 2400 trials, a pool excluding all four knife cells,
    which is where the bootstrap scores 1.000. The three rates are
    therefore three readings and not one comparison. The bootstrap term
    is not weakly informative but SPECIFIC: cell by cell
    it detected 1.000, 1.000, 1.000, 1.000 at the four knife cells and
    then 0.302, 0.022, 0.000, 0.000 as the true |b|/h rose 4.328,
    8.836, 17.706, 35.500, and 0.000 at both bad cells of the mild
    world. Its power is DECREASING in the severity of what it is meant
    to detect --- not a weak instrument but one pointed the wrong way,
    since severity here is bought by the bias converging, which is
    exactly F3's kernel. Where the threshold comes from is worth
    naming, since it is the same fact once more: at 0.207 it is set by
    the well-specified arm on the mild world at the smallest sample
    size, whose bootstrap term reads 0.276 for an entirely benign
    small-sample nonlinearity. At one n the instrument cannot tell a
    decaying term from a persistent one --- it reads b, never db/dn ---
    so the price of not alarming there is the threshold that lets the
    converged gaps through. The 0.432 is then not a partial success but
    the knife cells whole plus a residue: 130 detections across the
    2400 non-knife bad trials, every one of them at the two smallest
    sample sizes of one arm, where that arm's b had not yet settled
    onto its gap --- the gap being an exact constant, 29/150 =
    0.19333 on W_CLEAR, while b reads 0.18971 at n = 500 and 0.19344 at
    n = 32000 (4000 draws each, standard errors 0.00031 and 0.00004,
    computed separately from the run above). It is b that converges
    here and never the gap, which is what "converged gap" abbreviates.
    So the direction is knowable from inside only where the uncounted
    term is still MOVING. That is what an exact-truth ruler is for,
    and it is why the companion rig's plane had to be measured against
    closed forms rather than against an estimate of itself.

    F7 WHAT THIS DOES NOT SETTLE. Scope is one estimator family, one
    target, four worlds, and three detectors. Two of the four documented
    overconfidence mechanisms are instantiated, as in the companion rig;
    the non-identification specimen is absent here too, having no bias
    coordinate. THE FIT TEST NEVER SHOWS ITS NULL: every cell where that
    statistic is defined runs a pooled model on a world that model is
    wrong about, so its false-alarm threshold in F6 is set entirely by
    W_SAME and its 0.167 is a reading of it as a detector of the TERM,
    never of misspecification, which it detects perfectly. The missing
    arm is the cheap one --- pooling on W_KNIFE, where every cell is 1/2
    and the pooled model is therefore CORRECT --- and it would exhibit
    the null the standardization assumes (mean 0, sd 1 at dof = M - 3)
    beside a knife bias shrunk to sqrt(2*3/pi)/z = 0.705 by the coarser
    model. It is not run here. A bias decaying SLOWER than 1/sqrt(n) but
    not converged would be divergent AND visible, and no arm here
    occupies that corner --- building one needs a model class that grows
    with n, and it is the case that would separate F3's law from its
    specimens. And F4's separation of misspecification from the term is
    shown by one construction; whether a goodness-of-fit statistic can
    be REWEIGHTED into the functional's own coordinates --- testing not
    whether the model is wrong but whether it is wrong where the target
    reads it --- is the live repair this leaves.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import math
from fractions import Fraction

import numpy as np

Z = 1.96
NOMINAL = 0.95
TRIALS = 400
BOOT = 150
SIZES = (500, 2000, 8000, 32000)
SEED = 640021
FALSE_ALARM_TARGET = 0.10

W_CLEAR = [
    Fraction(1, 10), Fraction(3, 10), Fraction(2, 5), Fraction(3, 5), Fraction(4, 5),
    Fraction(1, 5), Fraction(1, 4), Fraction(7, 10), Fraction(3, 4), Fraction(9, 10),
    Fraction(1, 10), Fraction(2, 5), Fraction(3, 5), Fraction(7, 10), Fraction(9, 10),
]
W_KNIFE = [Fraction(1, 2)] * 15
W_MILD = [
    Fraction(3, 10), Fraction(3, 10), Fraction(3, 10), Fraction(3, 10), Fraction(13, 25),
    Fraction(1, 4), Fraction(1, 4), Fraction(1, 4), Fraction(1, 4), Fraction(27, 50),
    Fraction(2, 5), Fraction(2, 5), Fraction(2, 5), Fraction(2, 5), Fraction(51, 100),
]
# every cell strictly below 1/2 and heterogeneous: the pooled model is
# wrong about the cells and exactly right about the target.
W_SAME = [
    Fraction(1, 10), Fraction(1, 5), Fraction(3, 10), Fraction(2, 5), Fraction(9, 20),
    Fraction(1, 20), Fraction(3, 20), Fraction(1, 4), Fraction(7, 20), Fraction(9, 20),
    Fraction(1, 10), Fraction(3, 20), Fraction(1, 5), Fraction(3, 10), Fraction(2, 5),
]

M = len(W_CLEAR)
GROUP = np.array([r // 5 for r in range(M)])
NGROUP = 3
GOF_DOF = M - NGROUP


def bayes_error(etas):
    """Exact target: sum_r P(r) min(eta_r, 1-eta_r), uniform P."""
    return sum((min(e, 1 - e) for e in etas), Fraction(0)) / len(etas)


def group_truth(etas):
    """Exact value the POOLED model converges to."""
    tot = Fraction(0)
    for g in range(NGROUP):
        members = [etas[r] for r in range(len(etas)) if GROUP[r] == g]
        bar = sum(members, Fraction(0)) / len(members)
        tot += min(bar, 1 - bar) * Fraction(len(members), len(etas))
    return tot


def est_percell(counts, ones):
    """Per-cell plug-in, vectorized over a leading resample axis."""
    n = counts.sum(axis=-1, keepdims=True)
    eta = np.where(counts > 0, ones / np.maximum(counts, 1), 0.5)
    return np.sum((counts / n) * np.minimum(eta, 1.0 - eta), axis=-1)


def est_pooled(counts, ones):
    """The same plug-in with the cells pooled into the three groups."""
    n = counts.sum(axis=-1, keepdims=True)
    shape = counts.shape[:-1] + (NGROUP,)
    gc = np.zeros(shape)
    go = np.zeros(shape)
    for g in range(NGROUP):
        sel = (GROUP == g)
        gc[..., g] = counts[..., sel].sum(axis=-1)
        go[..., g] = ones[..., sel].sum(axis=-1)
    eta = np.where(gc > 0, go / np.maximum(gc, 1), 0.5)
    return np.sum((gc / n) * np.minimum(eta, 1.0 - eta), axis=-1)


def half_width(est, n):
    return Z * np.sqrt(np.maximum(est * (1.0 - est), 0.0) / n)


def gof_stat(counts, ones):
    """Within-group Pearson against the saturated model, standardized."""
    eta = np.where(counts > 0, ones / np.maximum(counts, 1), 0.5)
    x2 = 0.0
    for g in range(NGROUP):
        sel = (GROUP == g)
        gc = counts[sel].sum()
        go = ones[sel].sum()
        bar = go / gc if gc > 0 else 0.5
        v = bar * (1.0 - bar)
        if v <= 0:
            continue
        x2 += float(np.sum(counts[sel] * (eta[sel] - bar) ** 2) / v)
    return (x2 - GOF_DOF) / math.sqrt(2.0 * GOF_DOF)


def run_arm(name, etas, estimator, n, rng, pooled):
    """One (arm, n) cell: outside truth and the inside statistics."""
    truth = float(bayes_error(etas))
    etaf = np.array([float(e) for e in etas])
    cellp = np.full(M, 1.0 / M)

    ests = np.empty(TRIALS)
    halves = np.empty(TRIALS)
    boot_b = np.empty(TRIALS)
    boot_sd = np.empty(TRIALS)
    drift = np.empty(TRIALS)
    gofs = np.empty(TRIALS)

    for t in range(TRIALS):
        counts = rng.multinomial(n, cellp)
        ones = rng.binomial(counts, etaf)
        est = float(estimator(counts, ones))
        ests[t] = est
        halves[t] = float(half_width(est, n))

        # the bootstrap: resample the 2M (cell, label) categories.
        cats = np.concatenate([ones, counts - ones]).astype(np.int64)
        p = cats / float(n)
        bs = rng.multinomial(n, p, size=BOOT)
        b_ones = bs[:, :M]
        b_counts = b_ones + bs[:, M:]
        b_est = estimator(b_counts, b_ones)
        boot_b[t] = float(np.mean(b_est)) - est
        boot_sd[t] = float(np.std(b_est, ddof=1))

        # the drift: an exact half-sample, drawn without replacement.
        h_cats = rng.multivariate_hypergeometric(cats, n // 2)
        h_ones = h_cats[:M]
        h_counts = h_ones + h_cats[M:]
        drift[t] = est - float(estimator(h_counts, h_ones))

        gofs[t] = gof_stat(counts, ones) if pooled else float("nan")

    dev = ests - truth
    cov = float(np.mean(np.abs(dev) <= halves))
    b = float(np.mean(dev))
    h = float(np.mean(halves))
    sd = float(np.std(dev, ddof=1))
    return dict(
        arm=name, n=n, truth=truth, cov=cov, b=b, h=h, sd=sd,
        ratio=abs(b) / h,
        boot_ratio=abs(float(np.mean(boot_b))) / h,
        boot_over_b=(float(np.mean(boot_b)) / b) if b != 0 else float("nan"),
        drift_ratio=abs(float(np.mean(drift))) / h,
        h_over_sdhat=h / float(np.mean(boot_sd)),
        h_over_sd=h / sd,
        gof=float(np.mean(gofs)) if pooled else float("nan"),
        # per-trial detector statistics, kept for the single-sample rule
        t_boot=np.abs(boot_b) / halves,
        t_drift=np.abs(drift) / halves,
        t_gof=gofs,
    )


def rate_at_threshold(good, bad, key, target):
    """Smallest threshold holding false alarms at or below target, and the
    detection rate there. Statistics are one-sided and large-is-alarming."""
    pool_good = np.concatenate([r[key] for r in good])
    pool_bad = np.concatenate([r[key] for r in bad])
    if np.all(np.isnan(pool_good)) or np.all(np.isnan(pool_bad)):
        return None
    gs = np.sort(pool_good[~np.isnan(pool_good)])
    k = int(math.ceil((1.0 - target) * len(gs))) - 1
    thr = float(gs[min(max(k, 0), len(gs) - 1)])
    fa = float(np.mean(pool_good[~np.isnan(pool_good)] > thr))
    det = float(np.mean(pool_bad[~np.isnan(pool_bad)] > thr))
    return thr, fa, det


def main():
    rng = np.random.default_rng(SEED)
    print("CAN AN UNCOUNTED TERM BE SEEN FROM INSIDE?")
    print("=" * 74)
    for label, w in (("W_CLEAR", W_CLEAR), ("W_KNIFE", W_KNIFE),
                     ("W_MILD", W_MILD), ("W_SAME", W_SAME)):
        e = bayes_error(w)
        g = group_truth(w) - e
        print("%-8s exact Bayes error = %-8s = %.6f   pooling gap = %-8s = %.6f"
              % (label, e, float(e), g, float(g)))
    print("M = %d cells, %d trials, %d resamples, z = %.2f, nominal %.2f"
          % (M, TRIALS, BOOT, Z, NOMINAL))
    print()

    arms = [
        ("B1 per-cell clear", W_CLEAR, est_percell, False),
        ("B2 per-cell knife", W_KNIFE, est_percell, False),
        ("B3 pooled clear", W_CLEAR, est_pooled, True),
        ("B4 per-cell mild", W_MILD, est_percell, False),
        ("B5 pooled mild", W_MILD, est_pooled, True),
        ("B6 pooled same", W_SAME, est_pooled, True),
        ("B7 per-cell same", W_SAME, est_percell, False),
    ]
    rows = []
    for name, w, f, pooled in arms:
        for n in SIZES:
            rows.append(run_arm(name, w, f, n, rng, pooled))

    print("%-18s %6s %6s %7s %8s %8s %8s %8s" %
          ("arm", "n", "cover", "|b|/h", "boot/h", "drift/h", "h/sdhat", "gof"))
    print("-" * 74)
    last = None
    for r in rows:
        if last is not None and r["arm"] != last:
            print("-" * 74)
        last = r["arm"]
        print("%-18s %6d %6.3f %7.3f %8.3f %8.3f %8.2f %8s" %
              (r["arm"], r["n"], r["cov"], r["ratio"], r["boot_ratio"],
               r["drift_ratio"], r["h_over_sdhat"],
               "n/a" if math.isnan(r["gof"]) else "%.1f" % r["gof"]))
    print()

    checks = []

    # P1 --- the control, read first.
    b2 = [r for r in rows if r["arm"] == "B2 per-cell knife"]
    b1 = [r for r in rows if r["arm"] == "B1 per-cell clear"]
    tol = 3.0 * math.sqrt(NOMINAL * (1 - NOMINAL) / TRIALS)
    print("P1 CONTROL  companion constant sqrt(2M/pi)/z = %.4f" %
          (math.sqrt(2 * M / math.pi) / Z))
    for r in b2:
        print("            knife n = %6d  |b|/h %.4f" % (r["n"], r["ratio"]))
    for r in b1:
        print("            clear n = %6d  coverage %.3f" % (r["n"], r["cov"]))
    ok1 = all(1.55 <= r["ratio"] <= 1.60 for r in b2)
    ok2 = all(abs(r["cov"] - NOMINAL) <= tol for r in b1)
    checks.append(("P1 knife |b|/h in [1.55, 1.60] at every n", ok1))
    checks.append(("P1b clear coverage within MC noise of nominal (%.3f)" % tol, ok2))

    # P1 as frozen is a HAND-VALUE band, not a measurement band: the
    # ratio's own standard error is sd(dev)/(sqrt(TRIALS) h), and three
    # of those is wider than the band's half-width. A control cannot
    # gate at a precision it does not have, so the frozen check is left
    # FAILING and reported, and the abort runs off the same agreement
    # tested at the measurement's own precision.
    hand = math.sqrt(2 * M / math.pi) / Z
    print("            (P1's band is +/- %.3f around the hand value; the"
          " ratio's own 3 s.e.:)" % 0.025)
    ok1c = True
    for r in b2:
        se = 3.0 * (r["sd"] / math.sqrt(TRIALS)) / r["h"]
        inside = abs(r["ratio"] - hand) <= se
        ok1c = ok1c and inside
        print("            n = %6d  |b|/h %.4f  hand %.4f  3 s.e. %.4f  %s"
              % (r["n"], r["ratio"], hand, se, "in" if inside else "OUT"))
    checks.append(("P1c knife |b|/h within 3 s.e. of the hand value at every n",
                   ok1c))
    if not (ok1c and ok2):
        print("\nCONTROL FAILED --- the rig is broken; no result below is read.")
        for label, good in checks:
            print("  %-64s %s" % (label, "PASS" if good else "FAIL"))
        return

    # P2/P3 --- the hand-derived constants at the knife.
    print("\nP2/P3  the knife, against the hand: bhat/b = sqrt(2)-1 = %.4f,"
          " both ratios %.4f" % (math.sqrt(2) - 1, (math.sqrt(2) - 1) * 1.5766))
    for r in b2:
        print("    n = %6d  bhat/b %7.4f   boot/h %.4f   drift/h %.4f"
              % (r["n"], r["boot_over_b"], r["boot_ratio"], r["drift_ratio"]))
    checks.append(("P2 knife bhat/b in [0.35, 0.48] at every n",
                   all(0.35 <= r["boot_over_b"] <= 0.48 for r in b2)))
    checks.append(("P3 knife boot/h and drift/h agree within 0.15",
                   all(abs(r["boot_ratio"] - r["drift_ratio"]) <= 0.15 for r in b2)))
    checks.append(("P3b both knife ratios in [0.50, 0.80] at every n",
                   all(0.50 <= r["boot_ratio"] <= 0.80 and
                       0.50 <= r["drift_ratio"] <= 0.80 for r in b2)))

    # P4 --- the kernel: a converged bias is invisible to both.
    b3 = [r for r in rows if r["arm"] == "B3 pooled clear"]
    b5 = [r for r in rows if r["arm"] == "B5 pooled mild"]
    conv = b3 + [r for r in b5 if r["n"] == SIZES[-1]]
    print("\nP4  converged gaps: what the inside instruments report")
    for r in conv:
        print("    %-18s n = %6d  true |b|/h %8.3f   boot/h %.3f   drift/h %.3f"
              % (r["arm"], r["n"], r["ratio"], r["boot_ratio"], r["drift_ratio"]))
    checks.append(("P4 true |b|/h > 1 at every converged-gap cell",
                   all(r["ratio"] > 1.0 for r in conv)))
    checks.append(("P4b both inside ratios < 0.25 at every converged-gap cell",
                   all(r["boot_ratio"] < 0.25 and r["drift_ratio"] < 0.25
                       for r in conv)))

    # P5 --- the negative control for goodness of fit.
    b6 = [r for r in rows if r["arm"] == "B6 pooled same"]
    print("\nP5  W_SAME: pooling gap exactly %s" %
          (group_truth(W_SAME) - bayes_error(W_SAME)))
    for r in b6:
        print("    n = %6d  coverage %.3f   gof %8.1f   true |b|/h %.3f"
              % (r["n"], r["cov"], r["gof"], r["ratio"]))
    checks.append(("P5 exact zero pooling gap on W_SAME",
                   group_truth(W_SAME) == bayes_error(W_SAME)))
    checks.append(("P5b B6 coverage within MC noise of nominal at every n",
                   all(abs(r["cov"] - NOMINAL) <= tol for r in b6)))
    checks.append(("P5c B6 gof > 3 at the smallest n", b6[0]["gof"] > 3.0))
    checks.append(("P5d B6 gof > 50 at the largest n", b6[-1]["gof"] > 50.0))

    # P6 --- the free coordinate carries no verdict.
    b4 = [r for r in rows if r["arm"] == "B4 per-cell mild"]
    print("\nP6  the free coordinate, same world, opposite verdicts")
    for good, bad in zip(b4, b5):
        print("    n = %6d  per-cell h/sdhat %.2f (cover %.3f)   pooled %.2f"
              " (cover %.3f)" % (good["n"], good["h_over_sdhat"], good["cov"],
                                 bad["h_over_sdhat"], bad["cov"]))
    checks.append(("P6 h/sdhat differs by < 0.30 between B4 and B5 at every n",
                   all(abs(g["h_over_sdhat"] - b["h_over_sdhat"]) < 0.30
                       for g, b in zip(b4, b5))))
    # is the free coordinate itself faithful? the resampled sd against
    # the true one, in this rig's own numbers rather than a companion's.
    print("    the free coordinate's own fidelity, sdhat/sd:")
    for name in ("B1 per-cell clear", "B2 per-cell knife"):
        for r in [x for x in rows if x["arm"] == name]:
            print("      %-18s n = %6d  h/sd %.2f  h/sdhat %.2f  sdhat/sd %.3f"
                  % (r["arm"], r["n"], r["h_over_sd"], r["h_over_sdhat"],
                     r["h_over_sd"] / r["h_over_sdhat"]))

    # P7 --- the single-sample instrument reading.
    good = [r for r in rows if r["cov"] >= 0.90]
    bad = [r for r in rows if r["cov"] < 0.80]
    grey = [r for r in rows if 0.80 <= r["cov"] < 0.90]
    print("\nP7  the single-sample rule: %d GOOD cells, %d BAD, %d grey"
          " (excluded)" % (len(good), len(bad), len(grey)))
    for r in grey:
        print("    grey: %-18s n = %6d  coverage %.3f" % (r["arm"], r["n"], r["cov"]))
    best, best_key, best_thr = -1.0, None, None
    for key, label in (("t_boot", "bootstrap term"), ("t_drift", "drift term"),
                       ("t_gof", "goodness of fit")):
        if key == "t_gof":
            g2 = [r for r in good if not math.isnan(r["gof"])]
            b2b = [r for r in bad if not math.isnan(r["gof"])]
        else:
            g2, b2b = good, bad
        if not g2 or not b2b:
            print("    %-16s not applicable (no cells on one side)" % label)
            continue
        thr, fa, det = rate_at_threshold(g2, b2b, key, FALSE_ALARM_TARGET)
        if det > best:
            best, best_key, best_thr = det, key, thr
        print("    %-16s threshold %8.3f   false alarm %.3f   detection %.3f"
              % (label, thr, fa, det))

    # which BAD cells the best rule actually catches --- an observable,
    # so the regime reading is read off the rig and not inferred.
    if best_key is not None:
        print("    the best rule (%s) cell by cell over the BAD cells:" % best_key)
        knife_hits = other_hits = other_trials = 0
        for r in bad:
            s = r[best_key]
            s = s[~np.isnan(s)]
            hits = int(np.sum(s > best_thr))
            if r["arm"].startswith("B2"):
                knife_hits += hits
            else:
                other_hits += hits
                other_trials += len(s)
            print("      %-18s n = %6d  true |b|/h %8.3f  detected %.3f"
                  % (r["arm"], r["n"], r["ratio"], hits / len(s)))
        print("      detections off the knife: %d of %d non-knife trials"
              % (other_hits, other_trials))
    checks.append(("P7 best detection rate < 0.5 at false alarms <= 0.10",
                   best < 0.5))

    print("\n" + "=" * 74)
    for label, ok in checks:
        print("  %-64s %s" % (label, "PASS" if ok else "FAIL"))
    print("\n%d/%d checks pass" % (sum(1 for _, o in checks if o), len(checks)))


if __name__ == "__main__":
    main()
