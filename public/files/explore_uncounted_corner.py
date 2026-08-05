"""THE CORNER ARM: a bias that diverges against the bar while still moving.

THE QUESTION
------------
Two companion rigs left one corner of the uncounted-term plane empty.
explore_uncounted_term.py established that an interval's coverage is a
function of two ratios alone -- the uncounted term b against the true
dispersion sigma, and the stated half-width h against that same sigma --
and that the divergent regime b/h -> infinity is where more data makes a
stated uncertainty worse. explore_uncounted_inside.py asked whether the
divergence is visible from inside, with no exact truth to score against,
and answered NO for the arms it ran: both subsampling instruments read b
through its n-DEPENDENCE, so a bias that has CONVERGED lies in their
kernel, and a constant b is the plainest way to send b/h to infinity.
Every arm there was one of two kinds: bias decaying at 1/sqrt(n) (the
knife -- visible, constant ratio) or bias converged to a constant
(divergent, invisible).

Between them sits a corner no arm occupied: a bias decaying SLOWER than
1/sqrt(n) but not converged. There b/h ~ n^(1/2 - a) with 0 < a < 1/2
still diverges -- more data still makes the statement worse -- while the
term still MOVES, so an instrument reading n-dependence has something
to read. Two questions, each with a named repair attempt riding along:

  ONE. Is the corner OCCUPIABLE, and which inside instruments see an
  occupant? (If every construction either converges or goes invisible,
  the corner is empty and the companion rig's NO is total.)

  TWO. Can the goodness-of-fit instrument -- which escaped the kernel by
  fitting a richer class, and paid by detecting the MODEL rather than
  the term -- be REWEIGHTED into the functional's own coordinates, so it
  alarms on what the model COSTS and stays silent where flagrant
  misspecification costs nothing?

THE CORNER ARM, BY CONSTRUCTION
-------------------------------
Per-cell plug-in, then shrink every cell rate toward 1/2 with a weight
that decays slower than the bar: eta_r -> (1 - lam) eta_r + lam/2 at
lam(n) = n^(-1/4). Shrinking toward 1/2 never moves a rate across 1/2,
and min(x, 1-x) is linear on each side, so the shrunk estimate obeys an
exact identity:

    Etilde = (1 - lam) Ehat + lam/2

The bias against the target E is therefore

    b(n) = (1 - lam) b_plug(n) + lam(n) (1/2 - E)

whose second term decays as n^(-1/4): slower than h ~ n^(-1/2), so b/h
~ n^(1/4) diverges, while b still moves at every n. This is also the
SMOOTHING mechanism of the statement-law corpus made concrete -- an
atomic truth pulled toward the no-evidence value by a data-thinning
prior weight -- so the arm doubles as that mechanism's specimen on the
(b/sigma, h/sigma) plane.

THE HAND-ATTACK, BEFORE THE ENGINE
----------------------------------
On W_CLEAR (the companion rigs' world), E = 19/75 and 1/2 - E = 37/150.

  THE BIAS AND ITS RATIO. b ~ lam(n) * 37/150 = 0.0522, 0.0369,
  0.0261, 0.0184 at n = 500, 2000, 8000, 32000, up to a plug-in part
  that is small and negative at the smallest n. Against the stated
  half-width computed at Etilde ~ E + b, the ratio |b|/h runs about
  1.29, 1.85, 2.65, 3.78 -- divergent, factor 64^(1/4) = 2.83 across
  the 64-fold n, slightly inflated by the shrinking Etilde in h.

  THE BOOTSTRAP IS BLIND, AND THE REASON NAMES THE KERNEL. The
  bootstrap term compares the estimator on a resample to the estimator
  on the sample, BOTH at the same n, so by the identity the lam/2 parts
  cancel exactly:

      bhat_boot = (1 - lam) * (bootstrap term of the plain plug-in)

  The shrinkage bias -- the whole corner-occupying term -- drops out.
  This sharpens the companion rig's kernel: what the bootstrap loses is
  not "converged bias" but the gap between its own ESTIMAND at n and
  the target, and a deterministic-in-n shrinkage is such a gap while
  still moving. The drift term is NOT blind: the half-sample runs the
  estimator as it would run at n/2, weight lam(n/2), so

      E[drift] = b(n) - b(n/2) = -(2^(1/4) - 1) lam(n) (1/2 - E)

  a KNOWN sign (the estimate falls as n grows) and magnitude 0.189 |b|,
  giving hand ratios |drift|/h of about 0.24, 0.35, 0.50, 0.72 --
  GROWING with n, where on the converged arms the same instrument's
  power fell as the damage grew.

  THE WIDE LEVER. An auditor who runs the audit at two sizes reads
  b(n2) - b(n1) directly. Nested 500 inside 32000: signal b(32000) -
  b(500) = -0.034 against a dispersion of about sigma(500) = 0.015, a
  2-sigma effect where the same-trial half-lever at 32000 is about
  1.4 sigma.

  THE REWEIGHTED FIT TEST. For a pooled model the richer (per-cell)
  class is available, and the repair is to read the two fits' DIFFERENCE
  IN THE FUNCTIONAL:

      Dhat = Ehat_pooled - Ehat_percell

  min is concave, so Dhat >= 0 always, with equality iff every group's
  cells sit on one side of 1/2 in the sample. Its mean is the pooling
  gap -- the converged part of the uncounted term, the exact quantity
  the kernel hides -- and on the zero-gap world W_SAME it vanishes
  identically up to cells crossing 1/2 by sampling noise, EXACTLY where
  the raw within-group Pearson statistic fires loudest. Wrong where the
  TARGET reads it, rather than wrong. What it cannot do is also known
  in advance: it reads the gap between two classes the auditor can
  NEST, so error outside every available class stays uncounted -- the
  kernel narrows, it does not empty.

THE WORLDS
----------
The companion rigs' three, kept exact (M = 15, uniform cell prior,
rates as Fractions; the target is the Bayes error, a closed form), plus
one imported: W_CLEAR, W_MILD, W_SAME as in explore_uncounted_inside.py,
and W_NEAR105 -- 105 cells all at eta = 6/11, the world on which
explore_ceiling_ruler.py measured a held-out interval's coverage falling
monotonically in n (0.90, 0.50, 0.25, 0.15). Here it is rerun as the
HELD-OUT-PRECISION mechanism's specimen: the statement claims the Bayes
error 5/11 while scoring a FITTED rule, whose excess -- the uncounted
term -- decays with the flip probability of 105 near-half cells, slower
than the bar over this window (and exponentially beyond it: a
TEMPORARY resident of the corner, where the shrinkage arm is a
permanent one).

THE ARMS
--------
  PLAIN per-cell fit on W_CLEAR           (control: nominal)
  C0    shrinkage at lam = 1/n, W_CLEAR   (rate control: fast-decay
                                           shrinkage changes nothing)
  C1    shrinkage at lam = n^(-1/4)       (THE CORNER ARM)
  G3    pooled fit on W_CLEAR             (converged gap 29/150)
  G4    per-cell fit on W_MILD            (control for G5)
  G5    pooled fit on W_MILD              (converged gap 7/750)
  G6    pooled fit on W_SAME              (misspecified, gap exactly 0)
  H1    held-out majority rule on W_NEAR105, fit on half, scored on
        half, two-sided interval claimed for the Bayes error

Per trial and arm (except H1): the stated interval at z = 1.96; the
bootstrap term and dispersion over B resamples of the empirical
(cell, label) categories; the drift term against an exact half-sample
(the estimator run at the half's own size, weight and all); for pooled
arms the raw standardized within-group Pearson statistic and the
reweighted statistic Dhat / h. A separate nested loop reads the wide
lever on PLAIN, C0, C1: one draw at 32000, an exact nested subsample at
500, statistic the two estimates' difference. Coverage cells are scored
GOOD at 0.90 or above, BAD below 0.80, GREY between; every detector is
a single-sample rule with its threshold set to hold false alarms at or
below 0.10 over the GOOD cells' trials.

THE PREDICTIONS, FIXED BEFORE THE ENGINE WAS WRITTEN
----------------------------------------------------
  V1  CONTROL, read before anything else. PLAIN and C0 coverage within
      Monte-Carlo noise of 0.95 at every n; the exact pooling gaps
      print 29/150 (W_CLEAR), 7/750 (W_MILD), 0 (W_SAME).
  V2  THE CORNER IS OCCUPIED. C1 coverage strictly decreasing until it
      floors: below 0.40 at n = 500, below 0.10 at n = 2000, at most
      0.01 at the two largest; measured |b|/h strictly increasing,
      above 3.0 at n = 32000, its end-to-end growth within [2.3, 3.5]
      (hand 2.9).
  V3  THE BOOTSTRAP IS BLIND. On C1, |bhat_boot|/h stays below 0.25 at
      every n (the companion's kernel band) while |b|/h runs above 1.2
      -- and |bhat_boot / b| is at most 0.2 everywhere, at most 0.1 at
      the two largest n.
  V4  THE DRIFT SEES IT. C1's mean drift is NEGATIVE at every n, its
      |drift|/h strictly increasing, within 0.15 of the hand values
      (0.24, 0.35, 0.50, 0.72) at each n.
  V5  MOTION IS POWER. As a single-sample rule at false alarms at or
      below 0.10, the drift's detection rate over C1's trials INCREASES
      across the four n and ends above 0.35 at n = 32000; the wide
      lever detects above 0.40, at or above the half-lever's rate at
      n = 32000.
  V6  THE REWEIGHTED TEST DETECTS THE TERM, NOT THE MODEL. At its
      false-alarm threshold: detection 1.00 on G3 at every n, at least
      0.75 on G5 at n = 8000 and at least 0.95 at n = 32000; while on
      G6 -- flagrantly misspecified, term exactly zero -- its own
      false-alarm rate stays at or below 0.15 at every n even as the
      raw Pearson statistic's mean exceeds 3 at the smallest n and 50
      at the largest.
  V7  THE PLANE EXTENDS. At every (arm, n) cell including C1 and H1,
      measured coverage agrees with the two-ratio Gaussian prediction
      computed from measured b, mean h, measured sigma, to within 0.08
      at 400 trials -- the two-laws-are-one-fact reading now covering
      all four documented mechanism kinds.
  V8  THE HELD-OUT SPECIMEN LANDS IN THE CORNER'S WINDOW. H1 coverage
      strictly decreasing across the four n and below 0.25 at the
      largest; its |b|/h strictly increasing and above 1.2 at the
      largest; its |b| sqrt(n) strictly increasing (slower-than-
      1/sqrt(n) decay over this window).

KILL-SHAPES, AS OBSERVABLES
---------------------------
  V1 outside its bands: the rig is broken and nothing else is read.
  V2 failing (coverage not decreasing, or |b|/h not increasing): this
    construction does not occupy the corner; the corner question stays
    open and the construction is reported as a miss.
  V3 failing high (|bhat_boot / b| above 0.5 at any n): the bootstrap
    is NOT blind, the estimand-gap reading of the kernel is wrong, and
    the companion rig's kernel paragraph needs a settling pointer.
  V6's false-alarm rate on G6 above 0.25 at any n: the reweighting
    still reads the model; the repair fails and the second open closes
    NO.
  V7's largest deviation above 0.08: the plane does not extend to the
    new mechanisms and the one-fact law gains a scope clause.

RUN RECORD
----------
One run at seed 663001, 400 trials per (arm, n) cell, n = 500, 2000,
8000, 32000, about four seconds. After the first run the drift column
was changed to print its SIGN (V4's clause); same seed, every other
number reproduced identically.

THE FINDINGS
------------
Seven of the eight predictions passed as frozen; V8 missed in FORM at
its largest size, and the miss is itself the reading.

V1 PASS. PLAIN covers 0.970/0.948/0.950/0.950 and C0 covers
0.958/0.953/0.945/0.965 across the four n; the exact pooling gaps
printed 29/150, 7/750, and 0.

V2 PASS -- THE CORNER IS OCCUPIED (property for the divergence, from
the construction; measured throughout). C1's coverage runs 0.255,
0.015, 0.000, 0.000; |b|/h runs 1.22, 1.86, 2.67, 3.75, end-to-end
growth 3.07 against the hand 2.9; measured b = 0.0489 at n = 500
against the hand lam * 37/150 + (1 - lam) b_plug = 0.0495.

V3 PASS -- THE BOOTSTRAP IS BLIND, BY THE IDENTITY (property,
measured). Its term runs 0.110, 0.025, 0.003, 0.001 of h while |b|/h
runs 1.22 to 3.75; against b itself it is at most 0.091 and at most
0.014 beyond the smallest n. The n = 500 residue is the plain
plug-in's own bootstrap term (PLAIN prints 0.149 there) scaled by
1 - lam: the shrinkage contributes nothing at any n. So the kernel of
these instruments is the ESTIMAND GAP -- the distance from the
estimator's own estimand at n to the target -- and not "converged
bias": a deterministic-in-n weight sits in the bootstrap's kernel
while still moving, and only an instrument that RERUNS the estimator
at another size can see it.

V4 PASS. Signed drift on C1: -0.153, -0.323, -0.497, -0.688 of h,
against the hand -0.189 |b|/h = -0.24, -0.35, -0.50, -0.72: within
0.15 at every n, strictly growing, the sign as derived.

V5 PASS -- MOTION IS POWER, AND THE ANTI-MONOTONE FAILURE INVERTS.
Drift detection on C1 at false alarms 0.10: 0.028, 0.113, 0.193,
0.362 -- RISING as the damage grows, where the companion rig's
bootstrap fell 1.000 to 0.000 on the converged gaps as theirs grew.
The wide lever (nested 500 inside 32000) detects 0.522, the best
single instrument on the corner and the only one an auditor gets by
design rather than luck: run the audit at two sizes and subtract.

V6 PASS -- THE REWEIGHTED TEST DETECTS THE TERM AND NOT THE MODEL.
Detection 1.000 on G3 at every n, 0.875 and 1.000 on G5 at its two
bad sizes, 0.979 overall where defined; false alarms on the
flagrantly misspecified zero-term world G6 run 0.033, 0.000, 0.000,
0.000 while the RAW within-group Pearson mean on that same world runs
8.3, 34.1, 136.3, 546.9 -- the raw instrument's threshold is pushed
to 546 by that world's own good trials and its overall detection
collapses to 0.167 (G3 at the largest n and nothing else), the
companion rig's number reproduced from the same mechanism. AND THE
EARLY ALARM IS REAL: on G5 at n = 500 -- a GOOD cell, coverage 0.935,
carrying the real gap 7/750 not yet fatal at that bar -- the
reweighted statistic alarms at 0.468. It reads the TERM'S SIZE and
never its lethality: as a detector of "coverage already broken" that
is a false-alarm cluster; as an instrument for "this model costs
7/750 where the target reads it" it is correct at every size, and h
alone decides when the cost becomes fatal.

V7 PASS -- THE PLANE EXTENDS TO ALL FOUR MECHANISM KINDS (observation,
32 cells). Worst |measured - predicted| coverage 0.023 (H1 at
n = 2000), with the smoothing kind (C1) and the held-out kind (H1)
now on the plane beside the knife and class-gap kinds.

V8 MISS IN FORM, AND THE MISS IS THE READING. H1's coverage runs
0.863, 0.495, 0.152, 0.278 and its b sqrt(n) runs 0.643, 1.352,
2.195, 1.964: both turn at n = 32000. The held-out specimen is a
TEMPORARY resident of the corner -- its term decays with the flip
probability of 105 near-half cells, slower than 1/sqrt(n) only while
those margins stay unresolved, exponentially after -- and the exit
happened inside this window, one size beyond the recorded monotone
series (about 40 trials, whose own stream-to-stream spread the source
rig documents at up to 0.12). The frozen prediction bought
monotonicity through the fourth size and the world only owed three.

THE CLOSE
---------
The corner is occupied, and by a designed permanent resident: a
shrinkage weight decaying at n^(-1/4) puts an interval in the regime
where more data strictly worsens the statement while every term still
moves. Visibility there SPLITS the subsampling family -- the bootstrap
blind by an exact identity, the drift's power rising with n, the
two-size lever strongest -- so the divergent regime is knowable from
inside precisely on its moving boundary, and the companion rig's NO
stands only for the converged interior. The reweighted fit test closes
its own open with a YES: read the two nested fits' difference in the
functional and the instrument detects what the model costs where the
target reads it, silent on flagrant-but-free misspecification. What
remains uncounted after both: error outside every class the auditor
can nest -- the kernel narrows, it does not empty.
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
SEED = 663001
FALSE_ALARM_TARGET = 0.10

M = 15
GROUP = np.array([r // 5 for r in range(M)])
NGROUP = 3
GOF_DOF = M - NGROUP

W_CLEAR = [
    Fraction(1, 10), Fraction(3, 10), Fraction(2, 5), Fraction(3, 5), Fraction(4, 5),
    Fraction(1, 5), Fraction(1, 4), Fraction(7, 10), Fraction(3, 4), Fraction(9, 10),
    Fraction(1, 10), Fraction(2, 5), Fraction(3, 5), Fraction(7, 10), Fraction(9, 10),
]
W_MILD = [
    Fraction(3, 10), Fraction(3, 10), Fraction(3, 10), Fraction(3, 10), Fraction(13, 25),
    Fraction(1, 4), Fraction(1, 4), Fraction(1, 4), Fraction(1, 4), Fraction(27, 50),
    Fraction(2, 5), Fraction(2, 5), Fraction(2, 5), Fraction(2, 5), Fraction(51, 100),
]
W_SAME = [
    Fraction(1, 10), Fraction(1, 5), Fraction(3, 10), Fraction(2, 5), Fraction(9, 20),
    Fraction(1, 20), Fraction(3, 20), Fraction(1, 4), Fraction(7, 20), Fraction(9, 20),
    Fraction(1, 10), Fraction(3, 20), Fraction(1, 5), Fraction(3, 10), Fraction(2, 5),
]
M_NEAR = 105
W_NEAR105 = [Fraction(6, 11)] * M_NEAR


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


def make_shrunk(alpha):
    """Shrinkage estimator: exact identity (1-lam) Ehat + lam/2 at
    lam = n^(-alpha); shrinking toward 1/2 preserves each cell's side,
    so this equals the plug-in on the shrunk rates."""
    def est(counts, ones, n_eff):
        lam = float(n_eff) ** (-alpha)
        return (1.0 - lam) * est_percell(counts, ones) + lam / 2.0
    return est


def est_plain(counts, ones, n_eff):
    return est_percell(counts, ones)


def est_pool(counts, ones, n_eff):
    return est_pooled(counts, ones)


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


def run_arm(name, etas, est_fn, n, rng, pooled):
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
    gaps = np.empty(TRIALS)

    for t in range(TRIALS):
        counts = rng.multinomial(n, cellp)
        ones = rng.binomial(counts, etaf)
        est = float(est_fn(counts, ones, n))
        ests[t] = est
        halves[t] = float(half_width(est, n))

        # the bootstrap: resample the 2M (cell, label) categories at the
        # SAME n, so an n-indexed estimator runs at its own weight.
        cats = np.concatenate([ones, counts - ones]).astype(np.int64)
        p = cats / float(n)
        bs = rng.multinomial(n, p, size=BOOT)
        b_ones = bs[:, :M]
        b_counts = b_ones + bs[:, M:]
        b_est = est_fn(b_counts, b_ones, n)
        boot_b[t] = float(np.mean(b_est)) - est
        boot_sd[t] = float(np.std(b_est, ddof=1))

        # the drift: an exact half-sample, the estimator run at the
        # half's own size (weight included).
        h_cats = rng.multivariate_hypergeometric(cats, n // 2)
        h_ones = h_cats[:M]
        h_counts = h_ones + h_cats[M:]
        drift[t] = est - float(est_fn(h_counts, h_ones, n // 2))

        if pooled:
            gofs[t] = gof_stat(counts, ones)
            gaps[t] = (est - float(est_percell(counts, ones))) / halves[t]
        else:
            gofs[t] = float("nan")
            gaps[t] = float("nan")

    dev = ests - truth
    cov = float(np.mean(np.abs(dev) <= halves))
    b = float(np.mean(dev))
    h = float(np.mean(halves))
    sd = float(np.std(dev, ddof=1))
    return dict(
        arm=name, n=n, truth=truth, cov=cov, b=b, h=h, sd=sd,
        ratio=abs(b) / h,
        boot_mean=float(np.mean(boot_b)),
        boot_ratio=abs(float(np.mean(boot_b))) / h,
        boot_over_b=(float(np.mean(boot_b)) / b) if b != 0 else float("nan"),
        drift_mean=float(np.mean(drift)),
        drift_ratio=abs(float(np.mean(drift))) / h,
        h_over_sd=h / sd,
        gof=float(np.mean(gofs)) if pooled else float("nan"),
        gap=float(np.mean(gaps)) if pooled else float("nan"),
        t_boot=np.abs(boot_b) / halves,
        t_drift=np.abs(drift) / halves,
        t_gof=gofs,
        t_gap=gaps,
    )


def run_heldout(n, rng):
    """H1: majority rule fitted on half, scored on half, the interval
    claimed for the Bayes error 5/11. Ties (empty cells included) go to
    label 1, the friendliest choice on this world."""
    truth = float(bayes_error(W_NEAR105))
    etaf = np.array([float(e) for e in W_NEAR105])
    cellp = np.full(M_NEAR, 1.0 / M_NEAR)
    ests = np.empty(TRIALS)
    halves = np.empty(TRIALS)
    for t in range(TRIALS):
        ntr = n // 2
        nte = n - ntr
        trc = rng.multinomial(ntr, cellp)
        tro = rng.binomial(trc, etaf)
        rule1 = tro >= (trc - tro)  # majority, ties to 1
        tec = rng.multinomial(nte, cellp)
        teo = rng.binomial(tec, etaf)
        err = np.where(rule1, tec - teo, teo).sum()
        rhat = err / nte
        ests[t] = rhat
        halves[t] = float(Z * math.sqrt(max(rhat * (1 - rhat), 0.0) / nte))
    dev = ests - truth
    cov = float(np.mean(np.abs(dev) <= halves))
    b = float(np.mean(dev))
    h = float(np.mean(halves))
    sd = float(np.std(dev, ddof=1))
    return dict(arm="H1", n=n, truth=truth, cov=cov, b=b, h=h, sd=sd,
                ratio=abs(b) / h)


def run_wide_lever(est_fn, rng, n_big=32000, n_small=500):
    """One draw at n_big, an exact nested subsample at n_small; the
    statistic is the large estimate minus the small one."""
    etaf = np.array([float(e) for e in W_CLEAR])
    cellp = np.full(M, 1.0 / M)
    out = np.empty(TRIALS)
    for t in range(TRIALS):
        counts = rng.multinomial(n_big, cellp)
        ones = rng.binomial(counts, etaf)
        cats = np.concatenate([ones, counts - ones]).astype(np.int64)
        s_cats = rng.multivariate_hypergeometric(cats, n_small)
        s_ones = s_cats[:M]
        s_counts = s_ones + s_cats[M:]
        big = float(est_fn(counts, ones, n_big))
        small = float(est_fn(s_counts, s_ones, n_small))
        out[t] = big - small
    return out


def phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def cov_pred(b, h, sd):
    """The two-ratio Gaussian prediction, two-sided."""
    return phi((h - b) / sd) - phi((-h - b) / sd)


def rate_at_threshold(good, bad, key, target):
    """Smallest threshold holding false alarms at or below target, and
    the detection rate there. One-sided, large is alarming."""
    pool_good = np.concatenate([r[key] for r in good])
    pool_bad = np.concatenate([r[key] for r in bad])
    pg = pool_good[~np.isnan(pool_good)]
    pb = pool_bad[~np.isnan(pool_bad)]
    if len(pg) == 0 or len(pb) == 0:
        return None
    gs = np.sort(pg)
    k = int(math.ceil((1.0 - target) * len(gs))) - 1
    thr = float(gs[min(max(k, 0), len(gs) - 1)])
    fa = float(np.mean(pg > thr))
    det = float(np.mean(pb > thr))
    return thr, fa, det


def main():
    rng = np.random.default_rng(SEED)
    print("THE CORNER ARM: divergent against the bar, still moving")
    print("=" * 74)
    for label, w in (("W_CLEAR", W_CLEAR), ("W_MILD", W_MILD),
                     ("W_SAME", W_SAME)):
        e = bayes_error(w)
        g = group_truth(w) - e
        print(f"  {label}: E = {e} = {float(e):.6f}   pooling gap = {g} "
              f"= {float(g):.6f}")
    e = bayes_error(W_NEAR105)
    print(f"  W_NEAR105: E = {e} = {float(e):.6f}   (105 cells at 6/11)")

    shrunk_slow = make_shrunk(0.25)
    shrunk_fast = make_shrunk(1.0)
    arms = (
        ("PLAIN", W_CLEAR, est_plain, False),
        ("C0", W_CLEAR, shrunk_fast, False),
        ("C1", W_CLEAR, shrunk_slow, False),
        ("G3", W_CLEAR, est_pool, True),
        ("G4", W_MILD, est_plain, False),
        ("G5", W_MILD, est_pool, True),
        ("G6", W_SAME, est_pool, True),
    )

    results = []
    print()
    print(f"{'arm':6s}{'n':>7s}{'cov':>7s}{'b':>9s}{'h':>8s}{'|b|/h':>7s}"
          f"{'boot/h':>8s}{'boot/b':>8s}{'drftm/h':>9s}{'h/sd':>6s}"
          f"{'gof':>7s}{'gap/h':>7s}")
    for name, w, fn, pooled in arms:
        for n in SIZES:
            r = run_arm(name, w, fn, n, rng, pooled)
            results.append(r)
            print(f"{name:6s}{n:>7d}{r['cov']:>7.3f}{r['b']:>9.4f}"
                  f"{r['h']:>8.4f}{r['ratio']:>7.2f}{r['boot_ratio']:>8.3f}"
                  f"{r['boot_over_b']:>8.3f}{r['drift_mean'] / r['h']:>+9.3f}"
                  f"{r['h_over_sd']:>6.2f}"
                  f"{r['gof']:>7.1f}{r['gap']:>7.2f}")

    heldout = []
    print()
    print("H1: held-out claimed as the Bayes error, W_NEAR105")
    print(f"{'n':>7s}{'cov':>7s}{'b':>9s}{'h':>8s}{'|b|/h':>7s}"
          f"{'b*sqrt(n)':>10s}")
    for n in SIZES:
        r = run_heldout(n, rng)
        heldout.append(r)
        print(f"{n:>7d}{r['cov']:>7.3f}{r['b']:>9.4f}{r['h']:>8.4f}"
              f"{r['ratio']:>7.2f}{r['b'] * math.sqrt(n):>10.3f}")

    # coverage census and the single-sample detectors
    good = [r for r in results if r["cov"] >= 0.90]
    bad = [r for r in results if r["cov"] < 0.80]
    grey = [r for r in results if 0.80 <= r["cov"] < 0.90]
    print()
    grey_names = ", ".join("{}@{}".format(r["arm"], r["n"]) for r in grey)
    print(f"census: GOOD {len(good)}  BAD {len(bad)}  GREY {len(grey)}"
          f"   (GREY: {grey_names})")

    print()
    print("single-sample detectors, false alarms held at or below "
          f"{FALSE_ALARM_TARGET} on GOOD trials:")
    for key, label in (("t_boot", "bootstrap"), ("t_drift", "drift"),
                       ("t_gof", "raw fit"), ("t_gap", "reweighted")):
        out = rate_at_threshold(good, bad, key, FALSE_ALARM_TARGET)
        if out is None:
            print(f"  {label:11s} undefined on this pool")
            continue
        thr, fa, det = out
        print(f"  {label:11s} thr {thr:7.3f}  fa {fa:.3f}  det {det:.3f}")
        for r in bad:
            v = r[key]
            v = v[~np.isnan(v)]
            if len(v):
                print(f"     {r['arm']:5s}@{r['n']:<6d} det "
                      f"{float(np.mean(v > thr)):.3f}")
        # per-GOOD-arm false alarms for the reweighted test's G6 clause
        if key == "t_gap":
            for r in good:
                v = r[key]
                v = v[~np.isnan(v)]
                if len(v):
                    print(f"     FA {r['arm']:5s}@{r['n']:<6d} "
                          f"{float(np.mean(v > thr)):.3f}")

    # the wide lever on the three W_CLEAR per-cell arms
    print()
    print("wide lever (nested 500 inside 32000), statistic est_big - "
          "est_small:")
    lever = {}
    for name, fn in (("PLAIN", est_plain), ("C0", shrunk_fast),
                     ("C1", shrunk_slow)):
        lever[name] = run_wide_lever(fn, rng)
        print(f"  {name:6s} mean {float(np.mean(lever[name])):+.4f}  "
              f"sd {float(np.std(lever[name], ddof=1)):.4f}")
    pool_good = np.abs(np.concatenate([lever["PLAIN"], lever["C0"]]))
    gs = np.sort(pool_good)
    k = int(math.ceil((1.0 - FALSE_ALARM_TARGET) * len(gs))) - 1
    thr = float(gs[min(max(k, 0), len(gs) - 1)])
    det = float(np.mean(np.abs(lever["C1"]) > thr))
    fa = float(np.mean(pool_good > thr))
    print(f"  detector thr {thr:.4f}  fa {fa:.3f}  det on C1 {det:.3f}")

    # the two-ratio formula across every cell
    print()
    print("two-ratio formula check, |measured - predicted| coverage:")
    worst = ("", 0.0)
    for r in results + heldout:
        p = cov_pred(r["b"], r["h"], r["sd"])
        d = abs(r["cov"] - p)
        if d > worst[1]:
            worst = (f"{r['arm']}@{r['n']}", d)
    print(f"  worst cell {worst[0]}  deviation {worst[1]:.4f}")

    print()
    print("done.")


if __name__ == "__main__":
    main()
