"""THE NO-ROOT REGIME: what sets the rate at which an objective has no
solution in its own parameter box.

THE QUESTION
------------
The mixture-proportion audit's estimator minimizes a quadratic in the
forgetting rate p over [0, 1]. explore_nonidentified_statement.py maps
three shapes its solution set can take -- a displacement, a point fiber,
a twin fiber -- and measures a FOURTH it does not model: at the two ring
cells of the deletion audit the empirical objective has NO root inside
[0, 1] in 0.586 of bootstrap resamples at the smallest audit size and
still 0.286 at the largest. Every Gaussian cell of that rig's dial
reaches 0.145-0.268 at the smallest size and 0.000 at the largest. The
tool has no statement for the no-root case: it silently returns the
box-constrained argmin.

The record's standing candidate for the persistence is the FEATURE --
discrete on the ring, continuous on the dial -- with the puzzle that the
COARSER of the two ring cells carries the LOWER rate, which is the wrong
direction for a support-size reading.

TRANSPLANT, MARKED -- AND IT IS THE CANDIDATE ITSELF. The discreteness
reading is imported from the ring world's own vocabulary (window counts,
support size, level count), where it is the salient difference from a
Gaussian dial. The object here is a RATE at which a quadratic's root
leaves an interval, whose own vocabulary is coefficients and margins.
The candidate is run anyway, as a designed sweep and not a scan, because
the record froze it; but it is run BESIDE a rival written in the
object's own terms, and the two are separated by measurement.

THE HAND-ATTACK, BEFORE THE ENGINE
----------------------------------
The objective is f(p) = (A - pG + p^2 B)^2 with

    d = mu_n - mu_m,  B = d^2,  A = var_u - var_m,
    G = var_n - var_m + B.

For ANY feature distribution the audited variance is
var_u = pi*var_n + (1-pi)*var_m + pi(1-pi)d^2, so
A = pi(var_n - var_m) + pi(1-pi)B and A - pi*G + pi^2*B = 0
identically: p = pi is a root of the population objective in every
world, and the second root is p2 = A/(B*pi).

That gives the whole mechanism in one line. Hold G and B at their
population values and let A be the only thing the audited sample moves.
The set of A values admitting a root inside the box is exactly the RANGE
of

    A(p) = G*p - B*p^2  over  p in [0, 1],

an interval [lo, hi] with endpoints among A(0) = 0, A(1) = G - B and,
when the vertex G/(2B) lies inside the box, the vertex value G^2/(4B).
The population A sits inside it by construction. THE NO-ROOT EVENT IS
A-hat LEAVING THAT INTERVAL, and its rate is a normal tail at the
standardized MARGIN

    z = (distance from A to the nearer end of [lo, hi]) / sd(A-hat).

Nothing in that reading mentions the feature's support.

Run on the two ring cells, whose features are hypergeometric and whose
moments are therefore exact rationals. Writing t = a + b, the class
features are Hypergeometric(t-1, a-1, 3) and Hypergeometric(t-1, a, 3),
the audited one is Hypergeometric(t, a, 3), and pi = b/t.

  (12, 3):  var_m = 1089/2548, var_n = 198/637, d = 3/14,
            B = 9/196, G = -45/637, A = -1017/63700.
            A-range [-0.11656, 0], A = -0.01597, margin 0.015965.
            p2 = -113/65 = -1.73846.
  (2, 8):   var_m = 2/9, var_n = 7/18, d = 1/3,
            B = 1/9, G = 5/18, A = 34/225.
            A-range [0, 0.16667], A = 0.15111, margin 0.015556.
            p2 = 17/10 = 1.70000.

Three things follow on paper, and they set the design.

  1. BOTH RING CELLS ARE IDENTIFIED AT THE POPULATION. The second root
     is at -1.738 and at 1.700, sitting 1.738 and 0.700 beyond the
     nearer box end. The
     sibling rig calls their class variances "close but unequal" and
     splits their replicates by a NOMINAL twin fiber {pi, 1-pi}; the
     variances are in fact in ratio 0.727 and 1.750, and there is no
     second in-box solution to split by. Whatever the no-root
     persistence is, it is not a twin fiber.
  2. THE TWO MARGINS AGREE TO 2.6 PERCENT -- 0.015965 against 0.015556
     -- while the feature supports differ: at (12, 3) all three samples
     take four values, at (2, 8) the member sample takes two. A reading
     in which the level count sets the rate has to explain two nearly
     equal rates at two different level counts; the margin reading
     predicts them equal before either is measured.
  3. THE DIAL'S MARGIN IS TWENTY-THREE TIMES LARGER. At gamma = 0,
     pi = 1/5: B = G = 4, A = 0.64, A-range [0, 1], margin 0.36. So the
     dial and the ring differ in the margin by a factor 23 before any
     appeal to the feature, and the rate difference is what a normal
     tail does with that.

The rate is measured two ways because the record's figure is the
bootstrap one. Write sigma_u, sigma_m for the sampling sds of the two
variance estimates and s_bs for the bootstrap sd of A-hat within a
replicate (only the audited sample is resampled; var_m, G and B are held
at the replicate's own values, which is what the tool does). Then

    FRESH  A-hat = A + delta_u + delta_m,  sd^2 = sigma_u^2 + sigma_m^2
    BOOT   a*    = A-hat + eps,            sd^2 = sigma_u^2 + sigma_m^2
                                                  + mean(s_bs^2)

and each rate is the two-tail normal probability of leaving [lo, hi] at
that sd. Every ingredient is measured; only the thresholds are
hand-derived.

THE CELLS
---------
  D0, D2  the ring-free dial at pi = 1/5, gamma = 0 and 2.0 -- the
        continuous-feature reference, one non-identified and one
        identified.
  L2, L3, L4  the SAME dial at gamma = 0 with its feature QUANTIZED to
        2, 3 and 4 levels: cut points at the i/L quantiles of the
        population mixture, applied identically to all three samples, so
        the only thing that changes is the feature's discreteness. This
        is the record's own pre-registered design for the standing
        candidate. Population moments of the quantized feature are exact
        from the normal CDF, so each cell's margin is hand-derived too.
  W(12,3), W(2,8)  the ring cells of the recorded audit, at
        (a, b) = (12, 3) and (2, 8), exact pi = 1/5 and 4/5.

Audit sizes n in {50, 200, 1000}; R = 200 replicates per (cell, n);
B = 200 bootstrap resamples per replicate -- the sibling's counts, so
the ring rates are comparable to the recorded ones.

THE PREDICTIONS, FIXED BEFORE THE ENGINE WAS WRITTEN
----------------------------------------------------
  Q0  CONTROL, four parts, read before anything else. (i) The exact
      hypergeometric identity var_u = pi*var_n + (1-pi)var_m +
      pi(1-pi)d^2 holds in Fraction at both ring cells. (ii) The
      population roots computed by the engine from those exact moments
      equal the hand values {1/5, -113/65} and {4/5, 17/10} to better
      than 1e-12. (iii) A fresh draw of 100000 from each ring sampler
      reproduces the exact class variances to better than 0.005. (iv)
      The unrounded dial at gamma = 0 reproduces the sibling's
      trajectory: bootstrap no-root rate in 0.10-0.35 at n = 50 and
      below 0.02 at n = 1000.
  Q1  THE RING CELLS ARE IDENTIFIED. Exactly one in-box population root
      at each, and |p2 - nearest box end| > 0.5. Kill: a second in-box
      root, which would restore the sibling's twin reading and make the
      margin reading the wrong object.
  Q2  THE MARGIN LAW, FRESH REPLICATES. At every cell and size the
      measured fresh no-root fraction agrees with the hand margin's
      normal tail, evaluated at the measured fresh sd, to within 0.10.
  Q3  THE MARGIN LAW, BOOTSTRAP. The same, at the bootstrap sd, to
      within 0.10 at every cell and size -- so the recorded ring figures
      near 0.59 and 0.29 are reproduced from coefficients alone.
  Q4  DISCRETENESS IS NOT A TERM. Each quantized cell L2, L3, L4 is
      predicted by the margin law to the same 0.10 as the continuous
      cells. A quantized cell whose measured rate exceeds its predicted
      rate by more than 0.10 is discreteness acting BEYOND the margin
      and the candidate survives; three cells inside tolerance kill it.
      NOTE ON WHAT THE ENGINE TESTS, written at audit and not at the
      freeze: those two sentences are not the same check. The first is
      two-sided, the second one-sided, and the engine implements the
      SECOND. Q4's printed PASS is therefore the one-sided reading
      only; the two-sided sentence is failed by L2, at 0.49 BELOW its
      prediction, and that failure is Q2/Q3's tangency rather than a
      discreteness term. Both halves are reported in F4.
  Q5  THE SUPPORT-SIZE PUZZLE DISSOLVES. The two ring cells' bootstrap
      no-root fractions agree to within 0.10 at every audit size,
      as their 2.6-percent-apart margins require and their differing
      level counts do not. Kill: a gap above 0.10 at any size, which
      leaves room for a support term.

KILL-SHAPES, AS OBSERVABLES
---------------------------
  Q0 failed in any part: the rig is broken and nothing else is read.
  Q1 violated: the ring cells carry a live twin fiber after all; the
    margin reading is answering the wrong question and the sibling's
    split fiber stands.
  Q2 or Q3 violated at any cell: the margin does not set the rate, and
    the persistence needs a term the coefficients do not carry --
    which is where a feature-level reading would earn its seat.
  Q4 violated at any quantized cell: discreteness is a real term
    beside the margin, and the record's candidate survives its own
    designed sweep.
  Q5 violated: the two ring cells differ by more than their margins
    allow, and the difference is the thing to name.

The DECOMPOSITION of every no-root event is printed beside the rates --
the share with a negative discriminant against the share with real roots
both outside the box -- since the two are different failures of the same
statement and the record has never separated them.

RUN RECORD
----------
One run of the final engine, 8.0 s, single process, memory far under the
analysis ceiling. R = 200 replicates and B = 200 bootstrap resamples at
each of three audit sizes (50, 200, 1000) over seven cells -- two
continuous dial cells, three quantized ones, two ring cells -- single
seed stream (20260609). Of 9 checks 6 pass (Q0 in four parts, Q1, Q4)
and 3 fail (Q2, Q3, Q5) -- with Q4's pass being its one-sided half
only, the other half of its own wording failing at L2 for the reason
F3 gives. The post-hoc block at the end is labelled as
such: it was computed AFTER the table was read, to explain the one
catastrophic miss, and it draws no randomness.

FINDINGS
--------
F1  CONTROL, FOUR PARTS, ALL PASSED -- AND THE SECOND IS A RESULT. The
    exact hypergeometric identity holds in Fraction at both ring cells,
    the engine's population roots match the hand values {1/5, -113/65}
    and {4/5, 17/10} EXACTLY -- max |diff| 0.000e+00, the whole chain
    from hypergeometric moments to roots staying in Fraction -- the
    samplers recover the exact class
    variances to 0.0022 at n = 100000, and the continuous dial
    reproduces the sibling's trajectory (bootstrap no-root 0.266 at
    n = 50, 0.002 at n = 1000).
    SO BOTH RING CELLS ARE IDENTIFIED AT THE POPULATION (property of
    the world, exact in Fraction). Each has exactly ONE root in [0, 1],
    at pi; the second sits at -1.738 and at 1.700. The sibling rig
    describes those cells as "close but unequal" in class variance and
    splits their replicates by a nominal twin fiber {pi, 1 - pi}: the
    variances are in fact in ratio 0.727 and 1.750, and there is no
    second in-box solution to split by. Whatever the no-root
    persistence reads, it is not a twin fiber, and the record's
    standing candidate was chosen against a mis-stated background.

F2  THE MARGIN SETS THE RATE (observation, 18 cells of the 21 run --
    the three tangent ones are outside its scope by F3; Q2 and Q3 left
    FAILING as frozen). An in-box root exists exactly when A-hat lies
    in the range of A(p) = G*p - B*p^2 over [0, 1], so the no-root rate
    is a normal tail at the hand-derived margin over the measured
    spread of A-hat -- coefficients only, no term for the feature.
    Excluding the tangent cell L2, which F3 shows is outside the
    formula's scope, the largest deviation is 0.125 for the fresh arm
    and 0.114 for the bootstrap, both at n = 50, and at n >= 200 every
    cell is within 0.069 and 0.049. The recorded ring figures come out
    of coefficients at the two larger sizes and only approximately at
    the smallest: at (12, 3) the bootstrap rate runs 0.564, 0.431,
    0.301 against a predicted 0.666, 0.450, 0.287 -- the first of those
    a 0.102 miss, over tolerance -- and the sibling printed 0.586
    falling to 0.286 on its own seed stream. The frozen
    bar was a single 0.10 tolerance over ALL cells and it failed at six
    fresh and five bootstrap cells; of those, three fresh and three
    bootstrap are the tangency and the rest are n = 50. The n = 50
    misses go BOTH ways -- over by 0.125 at L4 and 0.124 at W(12, 3),
    under by 0.111 at W(2, 8) -- so it is an approximation degrading
    and not a term with a sign. WHICH approximation is NOT separated
    here, and there are two: A-hat's tail is less normal at n = 50, and
    the prediction holds G and B at their population values while the
    replicate's own fluctuate hardest there. Both act only at small n
    and this rig cannot tell them apart; see F6.

F3  THE ONE CATASTROPHIC MISS IS A TANGENCY, AND IT IS DERIVED RATHER
    THAN EXCUSED (property; post-hoc diagnostic, so labelled). At L2
    the margin is 0 to 1e-16 and the tail formula predicts 0.500 at
    every size against a measured 0.052, 0.017, 0.010. Both halves of
    that follow from one quantity. For a BINARY feature, A - p*G +
    p^2*B has a DOUBLE root at pi exactly when the audited class is
    balanced: with q the class rates, A - B*pi^2 = pi*d*(1 - q_u - q_m)
    - pi^2*d^2 vanishes iff q_u = 1/2. The L = 2 quantizer cuts at the
    mixture MEDIAN by construction, which forces exactly that -- and
    off the median the tangency is gone, the diagnostic printing
    discriminants 2.3e-2, 7.8e-2, 6.9e-2 at cuts -0.5, 1.0, 2.5 against
    -3.5e-18 at the median. The SAME q_u = 1/2 also puts var_u at the
    global maximum 1/4 of q(1 - q), so the audited variance can only
    fall while the breached edge of the window is the upper one: the
    fluctuation that would produce a no-root sample is structurally
    one-sided, and a two-sided normal tail at a zero margin cannot
    describe it. So the margin law's scope is the NON-TANGENT case, and
    a population double root is a fifth shape beside the displacement,
    the point fiber, the twin fiber and the no-root regime.

F4  AT THE NON-TANGENT CELLS DISCRETENESS ACTS ONLY THROUGH THE MARGIN,
    AND ITS DIRECTION IS NOT WHAT THE RECORD ASSUMED (observation, 9
    cells; Q4 passed). No
    quantized cell exceeds its margin prediction at all -- the standing
    candidate's own designed sweep gives it nothing to stand on beyond
    the coefficients. But discreteness is not idle either: quantizing
    the dial's continuous feature to THREE levels reproduces the ring's
    plateau inside an otherwise unchanged Gaussian world. L3's margin
    is 0.016539, within 7 percent of the ring cells' 0.015965 and
    0.015556, and its bootstrap rate runs 0.361, 0.346, 0.246 where the
    same dial's continuous version runs 0.266, 0.069, 0.002. So a
    discrete feature does cause the persistence -- by shrinking the
    margin from 0.360 to 0.0165, a factor of 22.
    SCOPE, AND Q4 IS ONE-SIDED BY CONSTRUCTION: it asks only whether
    discreteness ADDS rate beyond the margin, and no cell does. L2 sits
    0.49 BELOW its prediction, and that is a SECOND route rather than a
    third -- quantization there induces the TANGENCY of F3, where the
    margin reading voids rather than mispredicts. So "only through the
    margin" is the reading at the non-tangent cells, and inducing a
    tangency is the other thing a coarse feature can do.
    THE LEVEL COUNT IS NOT MONOTONE IN THE RATE: margins 0 (tangent),
    0.0165, 0.0567 at L = 2, 3, 4 give n = 1000 rates 0.010, 0.246,
    0.121. That is the record's wrong-direction puzzle reproduced
    INSIDE the dial, by a sweep that varies support size and nothing
    else -- so the rate is not monotone in it. The puzzle's actual
    resolution is visible in the two ring
    cells: their margins are equal to 2.6 percent, so the rate is set
    by the SPREAD, and the coarser feature has the smaller one
    (bootstrap sd 0.0201 against 0.0284 at n = 1000). A coarser feature
    moves the margin and the spread together, and the naive reading
    counts only the first.

F5  "NO SOLUTION IN THE BOX" IS TWO DIFFERENT FAILURES, AND THE MIX IS
    WORLD-DEPENDENT (observation, the 20 cells with events to
    decompose; the identified dial at n = 1000 has none). At every
    quantized dial cell 99 to 100 percent of no-root events have a
    NEGATIVE discriminant --
    complex roots, an objective with a strict interior minimum. At the
    ring cells 16 to 65 percent instead have REAL roots that both sit
    outside [0, 1] (disc < 0 share 0.387, 0.590, 0.349 at (12, 3) and
    0.835, 0.840, 0.712 at (2, 8)). The two send the tool's silent
    fallback to different places: with complex roots the argmin is the
    vertex where that is in box, with real roots outside it is a box
    ENDPOINT. At the ring cells' own population coefficients the
    diagnostic prints the vertex at -0.769 and 1.250 -- both outside --
    and the winning endpoint 0 against a truth of 0.2 at (12, 3) and 1
    against 0.8 at (2, 8): in each case the box end NEAREST the truth.
    So the no-root regime does NOT read as a flip, and it is a separate
    event from the one the deletion audit records as its flip rate,
    which counts estimates nearer 1 - pi. What the regime costs is a
    point estimate pinned to a box endpoint with no root behind it,
    and a bootstrap band built out of such points -- a failure that is
    invisible in a flip count precisely because it lands on the near
    side.

F6  WHAT THIS DOES NOT SETTLE. Q5 failed: the two ring cells' equal
    margins bind their rates together only as the normal approximation
    takes hold (gap 0.114, 0.076, 0.052 across the three sizes), so the
    prediction that equal margins give equal rates is supported in
    trend and not at the smallest size. The tangent case is named and
    derived but not modelled -- its rate is set by which side of the
    feature's own variance map the population sits on, which no
    coefficient margin carries, and no cell here dials through a
    tangency. The bootstrap holds G and B at the replicate's values
    throughout, as the tool does; a statement that resampled them too
    would have a different spread and is not measured. Nor does
    anything here separate F2's two candidate approximations at
    n = 50 -- the cheap arm that would is a SECOND predictor computed
    per replicate off that replicate's own G and B, differing from the
    printed one in exactly the ignored fluctuation; the gap between the
    two predictors is the size of that term, and it was not built.
    And every cell
    here is a variance-matching objective in one feature: nothing says
    what the window looks like when the audit matches more moments.
    The largest thing left open is what F5 opens: with both ring cells
    identified and their no-root fallback landing on the NEAR box end,
    nothing here explains the deletion audit's recorded flip rate at
    those same cells (28 percent at n = 200, 10 percent at n = 1000).
    The remaining route is the sample's own coefficients -- G changes
    sign, or the vertex enters the box -- which this rig holds at
    population values whenever it derives anything, and never measures.
    (SETTLED by explore_flip_level.py, and the route named just
    above was the wrong one: the flip is the same A-hat cut at the
    HALF-BOX value A(1/2) = G/2 - B/4 rather than at a window edge, so
    it is the in-box ROOT drifting past 1/2 -- the vertex entering the
    box wins the argmin in 7.7 percent of replicates at the smallest
    audit size and flips in 5 of 179. Everything above this
    parenthesis stands as measured; only its closing conjecture does
    not.)
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import math
from fractions import Fraction

import numpy as np

RNG = np.random.default_rng(20260609)

R_REPLICATES = 200
B_BOOTSTRAP = 200
AUDIT_SIZES = (50, 200, 1000)
WINDOW = 3
TOL = 0.10
BIG = 100000                # the moment-recovery control draw


# ------------------------------------------------------- the objective

def roots_from(a_, g_, bq):
    """Every exact-moment solution inside [0, 1], as the sibling rig
    computes it."""
    out = []
    if bq > 0.0:
        disc = g_ * g_ - 4.0 * bq * a_
        if disc >= 0.0:
            r = disc ** 0.5
            for p in ((g_ + r) / (2.0 * bq), (g_ - r) / (2.0 * bq)):
                if 0.0 <= p <= 1.0:
                    out.append(p)
    elif abs(g_) > 0.0:
        p = a_ / g_
        if 0.0 <= p <= 1.0:
            out.append(p)
    return out


def a_window(g_, bq):
    """[lo, hi]: the A values admitting a root in [0, 1], i.e. the range
    of A(p) = G*p - B*p^2 over the box."""
    ends = [0.0, g_ - bq]
    if bq > 0.0:
        v = g_ / (2.0 * bq)
        if 0.0 <= v <= 1.0:
            ends.append(g_ * v - bq * v * v)
    return min(ends), max(ends)


def phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def tail_rate(a_, lo, hi, sd):
    """Normal probability that A-hat leaves [lo, hi] at spread sd."""
    if sd <= 0.0:
        return 0.0 if lo <= a_ <= hi else 1.0
    return phi((lo - a_) / sd) + phi((a_ - hi) / sd)


def coeffs(var_m, var_n, d, pi):
    """(A, G, B) of the population objective, for any feature. The
    literal 1 is an int and not 1.0 so that Fraction inputs stay exact
    -- the ring cells' roots are a rational claim, not a float one."""
    bq = d * d
    return pi * (var_n - var_m) + pi * (1 - pi) * bq, var_n - var_m + bq, bq


# ---------------------------------------------------------- the worlds

def gaussian_dial(gamma, pi, n, rng):
    sd_n = math.sqrt(1.0 + gamma)
    feat_m = rng.normal(0.0, 1.0, n)
    feat_n = rng.normal(2.0, sd_n, n)
    from_n = rng.random(n) < pi
    feat_u = np.where(from_n, rng.normal(2.0, sd_n, n),
                      rng.normal(0.0, 1.0, n))
    return feat_m, feat_n, feat_u


def mixture_cuts(pi, levels):
    """The L-1 interior i/L quantiles of the gamma = 0 mixture
    (1-pi)N(0,1) + pi*N(2,1), by bisection -- deterministic, no draw."""
    def cdf(x):
        return (1.0 - pi) * phi(x) + pi * phi(x - 2.0)
    cuts = []
    for i in range(1, levels):
        target = i / levels
        lo, hi = -12.0, 14.0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if cdf(mid) < target:
                lo = mid
            else:
                hi = mid
        cuts.append(0.5 * (lo + hi))
    return np.array(cuts)


def quantized_moments(cuts, mu, sd):
    """(mean, var) of the bin index under N(mu, sd)."""
    edges = [phi((c - mu) / sd) for c in cuts]
    probs = []
    prev = 0.0
    for e in edges:
        probs.append(e - prev)
        prev = e
    probs.append(1.0 - prev)
    m1 = sum(i * p for i, p in enumerate(probs))
    m2 = sum(i * i * p for i, p in enumerate(probs))
    return m1, m2 - m1 * m1


def quantized_dial(cuts, pi, n, rng):
    fm, fn, fu = gaussian_dial(0.0, pi, n, rng)
    q = lambda x: np.searchsorted(cuts, x, side="right").astype(float)
    return q(fm), q(fn), q(fu)


def hyper_moments(big_n, k, draw=WINDOW):
    """Exact (mean, var) of Hypergeometric(N, K, n)."""
    mean = Fraction(draw * k, big_n)
    var = Fraction(draw * k * (big_n - k) * (big_n - draw),
                   big_n * big_n * (big_n - 1))
    return mean, var


def world_features(a, b, n, rng):
    """The constant-menu depth world at 2^a 3^b, as the sibling samples
    it: class-conditional and unconditioned window-count features."""
    t = a + b

    def window_counts(twos, total, m):
        keys = rng.random((m, total))
        order = np.argsort(keys, axis=1)
        is_two = order < twos
        return is_two[:, :WINDOW].sum(axis=1).astype(float)

    feat_m = window_counts(a - 1, t - 1, n)
    feat_n = window_counts(a, t - 1, n)
    keys = rng.random((n, t))
    order = np.argsort(keys, axis=1)
    is_two = order < a
    feat_u = is_two[:, 1:1 + WINDOW].sum(axis=1).astype(float)
    return feat_m, feat_n, feat_u


# --------------------------------------------------------- measurement

def run_cell(name, sampler, pi, a_pop, g_pop, b_pop, sizes=AUDIT_SIZES):
    lo, hi = a_window(g_pop, b_pop)
    margin = min(a_pop - lo, hi - a_pop)
    p2 = a_pop / (b_pop * pi) if b_pop * pi != 0 else float("nan")
    print(f"\n== {name}   pi = {pi:.4f}   A = {a_pop:.5f}  G = {g_pop:.5f}"
          f"  B = {b_pop:.5f}")
    print(f"   A-window [{lo:.5f}, {hi:.5f}]   margin {margin:.6f}"
          f"   p2 = {p2:.5f}")
    print(f"{'n':>6} | {'fresh':>6} {'pred':>6} {'dev':>6} | "
          f"{'boot':>6} {'pred':>6} {'dev':>6} | {'sd_f':>7} {'sd_b':>7} | "
          f"{'disc<0':>6} {'out':>5}")
    rows = []
    for n in sizes:
        vu = np.empty(R_REPLICATES)
        vm = np.empty(R_REPLICATES)
        bsvar = np.empty(R_REPLICATES)
        fresh_nr = 0
        fresh_neg = 0
        boot_nr = 0.0
        boot_neg = 0.0
        for r in range(R_REPLICATES):
            fm, fn, fu = sampler(n, RNG)
            v_m = float(np.var(fm))
            d = float(np.mean(fn) - np.mean(fm))
            bq = d * d
            g_ = float(np.var(fn)) - v_m + bq
            v_u = float(np.var(fu))
            a_ = v_u - v_m
            vu[r], vm[r] = v_u, v_m
            if not roots_from(a_, g_, bq):
                fresh_nr += 1
                if g_ * g_ - 4.0 * bq * a_ < 0.0:
                    fresh_neg += 1
            ab = np.empty(B_BOOTSTRAP)
            nr = 0
            neg = 0
            for j in range(B_BOOTSTRAP):
                res = fu[RNG.integers(0, n, size=n)]
                aj = float(np.var(res)) - v_m
                ab[j] = aj
                if not roots_from(aj, g_, bq):
                    nr += 1
                    if g_ * g_ - 4.0 * bq * aj < 0.0:
                        neg += 1
            bsvar[r] = float(np.var(ab))
            boot_nr += nr / B_BOOTSTRAP
            boot_neg += neg / B_BOOTSTRAP
        fresh = fresh_nr / R_REPLICATES
        boot = boot_nr / R_REPLICATES
        bneg = boot_neg / boot_nr if boot_nr else 0.0

        ahat = vu - vm
        sd_f = float(np.std(ahat))
        sd_b = math.sqrt(sd_f * sd_f + float(np.mean(bsvar)))
        pf = tail_rate(a_pop, lo, hi, sd_f)
        pb = tail_rate(a_pop, lo, hi, sd_b)

        share = (f"{bneg:>6.3f} {1 - bneg:>5.3f}" if boot > 0.0
                 else f"{'--':>6} {'--':>5}")
        print(f"{n:>6} | {fresh:>6.3f} {pf:>6.3f} {abs(fresh - pf):>6.3f} | "
              f"{boot:>6.3f} {pb:>6.3f} {abs(boot - pb):>6.3f} | "
              f"{sd_f:>7.4f} {sd_b:>7.4f} | {share}")
        rows.append(dict(n=n, fresh=fresh, pf=pf, boot=boot, pb=pb,
                         sd_f=sd_f, sd_b=sd_b, margin=margin,
                         bneg=bneg))
    return rows


def main():
    pi = 0.2

    # -------------------------------------------------- Q0, four parts
    hand = {(12, 3): (Fraction(1, 5), Fraction(-113, 65)),
            (2, 8): (Fraction(4, 5), Fraction(17, 10))}
    ring_pop = {}
    ok_id = True
    worst_root = 0.0
    for (a, b) in ((12, 3), (2, 8)):
        t = a + b
        mm, v_m = hyper_moments(t - 1, a - 1)
        mn, v_n = hyper_moments(t - 1, a)
        mu, v_u = hyper_moments(t, a)
        p_ex = Fraction(b, t)
        d = mn - mm
        ok_id &= (v_u == p_ex * v_n + (1 - p_ex) * v_m
                  + p_ex * (1 - p_ex) * d * d)
        A, G, B = coeffs(v_m, v_n, d, p_ex)
        eng = sorted([p_ex, A / (B * p_ex)])
        want = sorted(hand[(a, b)])
        worst_root = max(worst_root,
                         max(abs(float(e - w)) for e, w in zip(eng, want)))
        ring_pop[(a, b)] = (float(A), float(G), float(B), float(p_ex),
                            float(v_m), float(v_n))
    print(f"Q0(i)  exact var_u identity at both ring cells: "
          f"{'PASS' if ok_id else 'FAIL'}")
    print(f"Q0(ii) engine roots vs hand {{1/5, -113/65}}, {{4/5, 17/10}}: "
          f"max |diff| = {worst_root:.3e} -> "
          f"{'PASS' if worst_root < 1e-12 else 'FAIL'}")
    if not (ok_id and worst_root < 1e-12):
        print("POPULATION ALGEBRA DISAGREES WITH THE HAND -- nothing read.")
        return

    worst_mom = 0.0
    for (a, b), (_A, _G, _B, _p, v_m, v_n) in ring_pop.items():
        fm, fn, _fu = world_features(a, b, BIG, RNG)
        worst_mom = max(worst_mom, abs(float(np.var(fm)) - v_m),
                        abs(float(np.var(fn)) - v_n))
    print(f"Q0(iii) ring samplers recover exact variances at n={BIG}: "
          f"max |diff| = {worst_mom:.4f} -> "
          f"{'PASS' if worst_mom < 0.005 else 'FAIL'}")

    # -------------------------------------------------------- the cells
    cells = {}

    for gamma, tag in ((0.0, "D0"), (2.0, "D2")):
        A, G, B = coeffs(1.0, 1.0 + gamma, 2.0, pi)
        cells[tag] = run_cell(
            f"{tag}  ring-free dial, gamma={gamma:.2f} (continuous)",
            lambda n, rng, gm=gamma: gaussian_dial(gm, pi, n, rng),
            pi, A, G, B)

    for levels in (2, 3, 4):
        cuts = mixture_cuts(pi, levels)
        _mm, v_m = quantized_moments(cuts, 0.0, 1.0)
        mn, v_n = quantized_moments(cuts, 2.0, 1.0)
        d = mn - _mm
        A, G, B = coeffs(v_m, v_n, d, pi)
        cells[f"L{levels}"] = run_cell(
            f"L{levels}  the same dial, feature quantized to {levels} "
            f"levels   cuts {[round(c, 3) for c in cuts]}",
            lambda n, rng, c=cuts: quantized_dial(c, pi, n, rng),
            pi, A, G, B)

    for (a, b) in ((12, 3), (2, 8)):
        A, G, B, p_ex, _v_m, _v_n = ring_pop[(a, b)]
        cells[f"W({a},{b})"] = run_cell(
            f"W({a},{b})  constant-menu depth world (discrete feature)",
            lambda n, rng, aa=a, bb=b: world_features(aa, bb, n, rng),
            p_ex, A, G, B)

    # ------------------------------------------------------- the verdicts
    print("\n" + "=" * 70)
    d0 = cells["D0"]
    q0iv = 0.10 <= d0[0]["boot"] <= 0.35 and d0[-1]["boot"] < 0.02
    print(f"Q0(iv) D0 reproduces the sibling's trajectory "
          f"({d0[0]['boot']:.3f} at n=50, {d0[-1]['boot']:.3f} at n=1000): "
          f"{'PASS' if q0iv else 'FAIL'}")

    idbad = []
    for (a, b) in ((12, 3), (2, 8)):
        A, G, B, p_ex, _vm, _vn = ring_pop[(a, b)]
        p2 = A / (B * p_ex)
        if 0.0 <= p2 <= 1.0 or min(abs(p2), abs(p2 - 1.0)) <= 0.5:
            idbad.append((f"W({a},{b})", round(p2, 4)))
    print(f"Q1  both ring cells identified, second root > 0.5 outside the "
          f"box: {'PASS' if not idbad else 'FAIL ' + str(idbad)}")

    allrows = [(nm, r) for nm, rs in cells.items() for r in rs]
    fbad = [(nm, r["n"], round(abs(r["fresh"] - r["pf"]), 3))
            for nm, r in allrows if abs(r["fresh"] - r["pf"]) > TOL]
    print(f"Q2  margin law, FRESH replicates, within {TOL} everywhere: "
          f"{'PASS' if not fbad else 'FAIL ' + str(fbad)}")
    bbad = [(nm, r["n"], round(abs(r["boot"] - r["pb"]), 3))
            for nm, r in allrows if abs(r["boot"] - r["pb"]) > TOL]
    print(f"Q3  margin law, BOOTSTRAP, within {TOL} everywhere: "
          f"{'PASS' if not bbad else 'FAIL ' + str(bbad)}")

    qrows = [(nm, r) for nm, r in allrows if nm.startswith("L")]
    qbad = [(nm, r["n"], round(r["boot"] - r["pb"], 3))
            for nm, r in qrows if r["boot"] - r["pb"] > TOL]
    print(f"Q4  discreteness is not a term (no quantized cell exceeds its "
          f"prediction by {TOL}, the one-sided half of its wording): "
          f"{'PASS' if not qbad else 'FAIL ' + str(qbad)}")
    qmarg = [(nm, round(rs[0]["margin"], 5))
             for nm, rs in cells.items() if nm.startswith("L")]
    print(f"      quantized margins: {qmarg}")

    gaps = [(r1["n"], round(abs(r1["boot"] - r2["boot"]), 3))
            for r1, r2 in zip(cells["W(12,3)"], cells["W(2,8)"])]
    q5 = all(g <= TOL for _n, g in gaps)
    print(f"Q5  the two ring cells agree within {TOL} at every size "
          f"{gaps}: {'PASS' if q5 else 'FAIL'}")

    print("\n--- POST-HOC, NOT PRE-REGISTERED: why L2 misses, and what "
          "the tool returns when there is no in-box root ---")
    print("  a binary feature is tangent (double root at pi) exactly when "
          "the audited class is balanced:")
    for cut in (float(mixture_cuts(pi, 2)[0]), -0.5, 1.0, 2.5):
        q_m = 1.0 - phi(cut)
        q_n = 1.0 - phi(cut - 2.0)
        q_u = pi * q_n + (1.0 - pi) * q_m
        A, G, B = coeffs(q_m * (1 - q_m), q_n * (1 - q_n), q_n - q_m, pi)
        lo, hi = a_window(G, B)
        print(f"    cut {cut:>6.3f}  q_u = {q_u:.4f}  disc = "
              f"{G * G - 4 * A * B:>9.3e}  margin = {min(A - lo, hi - A):.6f}")
    print("  the argmin the tool falls back to, at the ring cells' own "
          "population coefficients:")
    for (a, b) in ((12, 3), (2, 8)):
        A, G, B, p_ex, _vm, _vn = ring_pop[(a, b)]
        f0, f1 = A * A, (A - G + B) ** 2
        print(f"    W({a},{b})  vertex G/2B = {G / (2 * B):>8.4f}  "
              f"f(0) = {f0:.3e}  f(1) = {f1:.3e}  -> endpoint "
              f"{0.0 if f0 < f1 else 1.0:.1f}  against pi = {p_ex:.1f}")

    print("\n--- the no-root event, decomposed (bootstrap share with a "
          "negative discriminant) ---")
    for nm, rs in cells.items():
        print(f"  {nm:>5}  " + "  ".join(
            f"n={r['n']}: rate {r['boot']:.3f} disc<0 "
            + (f"{r['bneg']:.3f}" if r["boot"] > 0.0 else "--")
            for r in rs))


if __name__ == "__main__":
    main()
