"""What the covariance-matching audit's FLIP actually is, at two cells
where nothing can compete for the minimum.

THE QUESTION. A moment-matching membership audit (the covariance-only
variant: minimize (A - pi*G + pi^2*B)^2 over pi in [0, 1], with
d = mean_n - mean_m, B = d^2, A = var_u - var_m, G = var_n - var_m + B)
was measured on a depth world by explore_deletion_ruler.py, which
records a FLIP RATE -- the fraction of replicates whose estimate lands
nearer 1 - pi than pi. At two of its cells that rate is large: 28
percent at n = 200 and still 10 percent at n = 1000 for (a, b) =
(12, 3), 13 and 1 percent for (2, 8).

Both cells are IDENTIFIED. The exact hypergeometric moments give the
population objective second roots -113/65 and 17/10, so there is no
rival minimum in the box to land on, and explore_noroot_margin.py F5
closes the other obvious reading: at both cells the population
coefficients send the no-root fallback to the box end NEAREST the
truth -- endpoint 0 against a truth of 1/5, endpoint 1 against 4/5 --
so the no-root regime does not read as a flip either. Nothing in the
corpus explains the recorded rate.

THE HAND-ATTACK (paper, before this engine; it answers the question,
and the rig below is the check rather than the discovery). Hold G and
B at their population values, which is where the sibling rig holds
them whenever it derives anything, and let only A move. Write
A(p) = G*p - B*p^2 for the level the objective needs at p. Then:

  (1) At BOTH cells the population vertex G/(2B) lies outside [0, 1]
      (-0.769 at (12, 3), 1.250 at (2, 8)). So A(p) is MONOTONE on the
      box -- decreasing at (12, 3) where G < 0, increasing at (2, 8)
      where G > 0 -- and the whole estimator collapses to a monotone
      function of the single scalar A-hat. There is nothing else for
      it to depend on.

  (2) Monotone means the in-box root, when there is one, is a monotone
      function of A-hat, and the two no-root fallbacks sit at the two
      ends of that same monotone sweep: A-hat past the NEAR window edge
      pins the estimate at the near endpoint, A-hat past the FAR edge
      pins it at the far one. So estimate and A-hat move together
      across the entire box INCLUDING both fallbacks, and the flip
      event pi-hat on the far side of 1/2 is EXACTLY the level set

          A-hat  <  A(1/2)  =  G/2 - B/4

      at both cells. This is exact given G and B, not an
      approximation. THE DIRECTION IS NOT A CONSTANT, and it is the
      one place this is easy to get wrong: the inequality reverses
      with the side the vertex sits on (A increasing on the box when
      the vertex is above it, decreasing when below) and reverses
      AGAIN with the side of 1/2 the truth sits on, the flip being a
      comparison against 1 - pi. At the two cells' POPULATION
      coefficients those two reversals cancel, which is why the
      inequality reads the same way at each -- but a replicate whose
      own vertex crosses to the other side of the box has the other
      direction, and scoring it with this one would score the coding
      rather than the law.

  (3) So the flip is not the no-root regime and not a tie-break: the
      no-root cut sits at a WINDOW EDGE of the same scalar and the flip
      cut sits at its HALF-BOX value, two different level sets of one
      quantity. At (12, 3) the window is [G - B, 0] = [-0.1165, 0] and
      A(1/2) = -0.0468 sits strictly INSIDE it, so the typical flip has
      a perfectly good in-box root -- it has just drifted past 1/2.

  (4) The rate follows with no free parameter, A-hat being a difference
      of two independent sample variances with
      var(A-hat) = ((mu4_u - var_u^2) + (mu4_m - var_m^2)) / n from the
      exact class moments. Hand values, Phi((A(1/2) - A)/sd):

          (12, 3): A = -0.0159655, A(1/2) = -0.0468015, gap -0.0308360
                   sd 0.10732 / 0.05366 / 0.02400 at n = 50/200/1000
                   -> 0.387, 0.283, 0.099   (recorded 0.385, 0.280, 0.100)
          (2, 8):  A =  0.1511111, A(1/2) =  0.1111111, gap -0.0400000
                   sd 0.06540 / 0.03270 / 0.01462
                   -> 0.270, 0.111, 0.003   (recorded 0.295, 0.130, 0.010)

      The (12, 3) column reproduces all three recorded rates to within
      0.003 off two exact rationals and a fourth moment. That is the
      claim this rig exists to break or confirm on printed output.

THE TRANSPLANTS, marked. Two. "Flip" is the deletion audit's word for
a TWIN-MINIMUM world (its cell S, where pi and 1 - pi are both exact
minimizers) and it is being carried to cells now known to have no
twin -- so the word names a distance comparison here and not a mode,
and (2) above is what that costs. And the margin machinery of
explore_noroot_margin.py is a normal tail read at an EDGE of the
A-window; (4) reads the same A-hat distribution at an INTERIOR level,
which reuses the distribution and drops the edge.

THE CELLS. W2 = (a, b) = (12, 3), pi = b/(a+b) = 1/5; W3 = (2, 8),
pi = 4/5. Same world, sampler and estimator as
explore_deletion_ruler.py: menu {2, 3} at every state, the audit
feature is the count of 2-moves in the WINDOW = 3 positions after the
first, class m = first move 2, class n = first move 3, and the
unconditioned fiber is a uniform arrangement. Population moments are
exact hypergeometric: feat_m ~ HG(T-1, a-1, W), feat_n ~ HG(T-1, a, W),
feat_u ~ HG(T, a, W), all computed in Fraction here so no coefficient
enters by hand.

THE MEASUREMENT. R = 400 replicates at each of n = 50, 200, 1000 for
each cell. Per replicate, record A-hat, G-hat, B-hat, the estimate,
WHICH CANDIDATE the argmin came from (one of the two endpoints, the
vertex, or one of the two roots), whether the sample had an in-box
root at all, and whether it flipped. Printed per (cell, n): the joint
table of winning candidate against flip, the flip rate, the flip rate
restricted to no-root replicates, the vertex-win rate, the measured
and predicted sd of A-hat, the predicted flip rate from (4), and the
AGREEMENT rate between the actual flip indicator and the hand-attack's
indicator, at population G and B (agr_pop) and at the replicate's own
coefficients with the direction read off its own vertex (agr_own --
a second column added after the first run, scored only on the
replicates the derivation covers; see PR4 and F2).

PREDICTIONS (fixed before the run).

  PR1  POSITIVE CONTROL, read before anything else. This file
       re-implements the sibling's estimator and sampler, so it must
       reproduce the sibling's recorded flip rates on its own seed
       stream: W2 0.385 / 0.280 / 0.100 and W3 0.295 / 0.130 / 0.010
       at n = 50 / 200 / 1000, each within 0.07. A miss anywhere means
       the harness differs from the tool being described and no other
       line here is readable.

  PR2  THE HANDOFF'S CANDIDATE DIES. The route on record for these
       flips was the vertex walking into the box under sampling noise.
       Observable: the vertex wins the argmin in fewer than 5 percent
       of replicates at W2, at every n.

  PR3  THE NO-ROOT REGIME DOES NOT CARRY THE FLIP. Observable: at W2
       the flip rate among replicates with no in-box root is below
       0.15 at n = 200 and at n = 1000. Hand expectation is about
       0.08 -- the no-root replicates split between the two window
       edges and only the far-edge minority flips.

  PR4  THE LAW. Observable: the agreement rate between the actual flip
       indicator and [A-hat < G/2 - B/4] at population G, B exceeds
       0.90 at every one of the six (cell, n) pairs. (The frozen form
       plugs POPULATION coefficients in; reading the law at each
       replicate's own is a second column the run added, and F2 is
       stated on that one.)

  PR5  THE PREDICTOR. Observable: Phi((A(1/2) - A)/sd) from exact
       moments is within 0.05 of the measured flip rate at n = 200 and
       n = 1000, both cells. The n = 50 column is printed and weighed
       after the run, not gated: explore_noroot_margin.py F2 already
       records the normal reading degrading there.

  PR6  WHERE THE FLIP LIVES, printed and weighed. Among flipped
       replicates at W2, the share whose argmin came from a ROOT
       rather than an endpoint. The hand-attack expects a majority at
       n = 200; a minority would put the mass in the far-edge fallback
       instead and change what (3) says a flip IS, without touching
       the law in (2).

RUN. python explore_flip_level.py   (estimated ~20 s; MEASURED 0.5 s,
the estimate 40x high -- single process, memory far under the analysis
ceiling, the largest array a 400-row shuffle of 15 keys.)

FINDINGS (from the printed run below; R = 400 replicates per row).

F1  PR1 PASS, and it is the only reason the rest is readable. This
    file's flip column tracks the sibling's recorded rates within
    0.063 at every one of the six rows (W2 0.448/0.245/0.075 against
    0.385/0.280/0.100, W3 0.355/0.168/0.003 against 0.295/0.130/0.010)
    on an independent seed stream. The two n = 50 rows sit high in
    both cells and are the two nearest the bar; see F5.

F2  THE FLIP IS A LEVEL SET OF A-hat, AND THE LAW IS EXACT (rule,
    derived algebraically then verified on all 2174 covered replicates
    of the 2400 run). Whenever the replicate's OWN vertex G/(2B) lies
    outside [0, 1], A(p) = G*p - B*p^2 is monotone on the box, the
    estimate is a monotone continuous function of A-hat alone that
    carries the two no-root fallbacks as its own endpoint values, and

        the replicate flips  <=>  A-hat  <  G/2 - B/4

    at that replicate's coefficients, with the direction read off that
    replicate's own vertex. Scored ONLY where it is derived -- the
    vertex-inside replicates are counted and set aside, since `above`
    has no derived value there and scoring them would report the
    coding -- the law is broken by NONE of the 2174 scored replicates
    across the six rows (330 / 385 / 400 scored at W2, 289 / 371 / 399
    at W3). It is an exact statement about the estimator and it holds
    exactly, with no residue to explain. Getting there took two
    direction bugs out of this rig, both in the same place and both
    invisible in a rate column: hard-coding the population's own
    direction for every replicate, and reading a vertex of +infinity
    when B-hat is exactly 0 -- which is a REAL case at n = 50, d-hat
    being a difference of integer-count means, and which makes the
    objective linear with direction set by the sign of G alone.
    THE UNSCORED CASE IS NOT RARE and it is the honest limit here: the
    vertex enters the box in 70 / 15 / 0 replicates at W2 and
    111 / 29 / 1 at W3, so at the smallest audit size more than a
    quarter of W3's replicates sit outside the derivation entirely.
    What happens there is not measured -- an earlier column that
    appeared to measure it was reporting its own arbitrary direction
    coding, which is why the split is printed as scored/unscored and
    not as one agreement rate.

F3  WHAT A FLIP IS: THE IN-BOX ROOT DRIFTING PAST 1/2, NOT THE SILENT
    FALLBACK (observation, both cells). PR6 confirmed and then some --
    among flipped replicates the share whose argmin came from a ROOT
    is 0.929 and 1.000 at W2 for n = 200, 1000, and 1.000 at W3 for
    both. PR3 confirmed on its stated scope: the flip rate among
    no-root replicates is 0.044 at W2 n = 200 and 0.000 at n = 1000,
    against a no-root rate of 0.400 and 0.237. So the no-root regime
    and the flip are two DIFFERENT level sets of the same scalar --
    the no-root cut at a window EDGE, the flip cut at the HALF-BOX
    value A(1/2). That value lies strictly inside the window whenever
    the vertex is outside the box -- by CONSTRUCTION and not by
    measurement, 1/2 being interior to the box and the window A's
    range over it -- so the two events can overlap only beyond the FAR
    edge, which is why F5 of explore_noroot_margin.py could find the
    fallback landing on the near box end and still leave the flip rate
    unexplained.
    THE OVERLAP'S SIZE IS NOT CONSTRUCTION AND IS NOT UNIFORMLY SMALL:
    at W2 it is 1.8 percent of replicates and 7 percent of flips at
    n = 200, against 16.5 and 37 percent at n = 50, where the far-edge
    fallback is fat -- 0.314 of that row's no-root replicates flip,
    63 of them landing at endpoint 1.

F4  THE ROUTE ON RECORD IS DEAD AS AN EXPLANATION AND PR2 FAILED AS AN
    OBSERVABLE. The frozen bar was a vertex-win rate below 0.05 at W2
    at every n; measured 0.077 / 0.028 / 0.000, so the bar fails at
    n = 50, and W3 is worse at 0.142. The vertex does walk into the
    box under sampling noise, exactly as the route on record said. But
    the joint table settles what that buys: of W2's 179 flips at
    n = 50 the vertex won 5, and at n = 200 and n = 1000 it won 11 and
    0 replicates and flipped in none of them. The candidate is alive
    and it carries nothing.

F5  THE PREDICTOR, AND PR5 IS 3 OF 4. Phi((A(1/2) - A)/sd) with sd
    from the exact fourth moments and no fitted quantity gives 0.387 /
    0.283 / 0.099 at W2 and 0.270 / 0.111 / 0.003 at W3. Against THIS
    run it is within 0.038 at the two gated W2 rows and 0.000 at W3
    n = 1000, and misses W3 n = 200 by 0.057, over the 0.05 bar.
    Against the sibling's independently seeded recorded rates the same
    six numbers are within 0.003, 0.003, 0.001, 0.025, 0.019, 0.007 --
    tighter at every row, and to three decimals at all three W2 sizes.
    Two runs straddle the prediction rather than agreeing on a
    deviation from it, so the misses here are not a term with a sign
    and nothing is inferred from them. The sd itself is predicted
    outright: measured 0.10795 / 0.05294 / 0.02431 against 0.10732 /
    0.05366 / 0.02400 at W2, so the fourth-moment plug is not what
    moves.

F6  WHAT THIS DOES NOT SETTLE, and the one thing it hands forward. Two
    cells of one world, one audit tool, scalar window features. The
    n = 50 gap in F1 and F5 is unexplained and this rig cannot source
    it: coefficient fluctuation is the visible candidate (the
    population-plug agreement column falls to 0.825 and 0.810 exactly
    there while the own-coefficient column holds), but the sibling's
    own n = 50 rows sit ON the prediction, and separating those needs
    a seed sweep this does not run. Nothing here measures the law at a
    cell whose POPULATION vertex is inside the box, where F2's unscored
    case is the generic one rather than a tail -- that is the cell
    where the flip stops being a level set at all, and no cell in
    either rig is one.
    THE HANDOFF, and its one limit stated first. F2's law has FOUR
    inputs and only three are truth-free: A-hat from the audited
    sample, G-hat and B-hat from the two class samples, and the
    direction, which turns on whether pi is above or below 1/2 -- the
    one thing an auditor does not have. So what an auditor can compute
    is not a directed flip rate. It is the distance from A-hat to the
    half-box cut in units of sd(A-hat), hence the probability that a
    fresh sample's estimate lands on the OTHER SIDE OF 1/2 from the
    one they are holding: an instability of their own number, which
    equals the flip risk exactly when their estimate is on the truth's
    side and is its complement when it is not. That is still the
    useful statement -- an auditor reporting 0.2 learns the number had
    a 28 percent chance of being 0.8 -- and it needs no oracle. The
    margin
    (G/2 - B/4 - A)/sd(A-hat) -- with sd from the same plug-in fourth
    moments verified in F5, or from a bootstrap -- is a self-reported
    flip risk available at audit time. That is derived here and NOT
    measured: whether it calibrates on samples, and what it says at
    the tangent and vertex-inside cells, is the next rig.

PRINTED OUTPUT (verbatim). Row 1 per size: n, measured flip rate, the
sibling's recorded rate, the predicted rate, measured and predicted sd
of A-hat, and the flip/law agreement at population and at own
coefficients. Row 2: in-box-vertex rate, vertex-win rate, no-root
rate, flip rate among no-root replicates, root share among flips. Row
3: the argmin source counts.

  == cell (a,b) = (12,3)   pi = 1/5 = 0.2000
     A = -0.0159655  G = -0.0706436  B = 0.0459184   vertex = -0.7692
     A-window [-0.116562, 0.000000]   A(1/2) = -0.0468014   gap A(1/2)-A = -0.0308359
       n   flip    rec   pred   sd_hat  sd_pred   agr_pop agr_own
           v_in  vert% noroot  flip|nr  root|fl   then argmin source, no-flip/flip
      50  0.448  0.385  0.387  0.10795  0.10732     0.825   1.000
          0.175  0.077  0.525    0.314    0.620   law broken 0 of 330 scored (70 unscored)
           end0 121/0  end1 0/63  vert 26/5  root+ 66/109  root- 8/2
     200  0.245  0.280  0.283  0.05294  0.05366     0.915   1.000
          0.037  0.028  0.400    0.044    0.929   law broken 0 of 385 scored (15 unscored)
           end0 143/0  end1 0/7  vert 11/0  root+ 148/91
    1000  0.075  0.100  0.099  0.02431  0.02400     0.953   1.000
          0.000  0.000  0.237    0.000    1.000   law broken 0 of 400 scored (0 unscored)
           end0 95/0  root+ 275/30

  == cell (a,b) = (2,8)   pi = 4/5 = 0.8000
     A = 0.1511111  G = 0.2777778  B = 0.1111111   vertex = 1.2500
     A-window [0.000000, 0.166667]   A(1/2) = 0.1111111   gap A(1/2)-A = -0.0400000
       n   flip    rec   pred   sd_hat  sd_pred   agr_pop agr_own
           v_in  vert% noroot  flip|nr  root|fl   then argmin source, no-flip/flip
      50  0.355  0.295  0.270  0.06758  0.06540     0.810   1.000
          0.278  0.142  0.398    0.019    0.979   law broken 0 of 289 scored (111 unscored)
           end0 0/1  end1 103/0  vert 55/2  root- 100/139
     200  0.168  0.130  0.111  0.03268  0.03270     0.887   1.000
          0.072  0.040  0.318    0.000    1.000   law broken 0 of 371 scored (29 unscored)
           end1 113/0  vert 16/0  root- 204/67
    1000  0.003  0.010  0.003  0.01496  0.01462     1.000   1.000
          0.003  0.003  0.185    0.000    1.000   law broken 0 of 399 scored (1 unscored)
           end1 73/0  vert 1/0  root- 325/1
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import math
from fractions import Fraction

import numpy as np

RNG = np.random.default_rng(20260609)

R_REPLICATES = 400
AUDIT_SIZES = (50, 200, 1000)
WINDOW = 3

# The sibling's recorded flip rates, for PR1. Source:
# explore_deletion_ruler.py PRINTED OUTPUT, cells (12,3) and (2,8).
RECORDED = {(12, 3): (0.385, 0.280, 0.100),
            (2, 8): (0.295, 0.130, 0.010)}
PC_TOL = 0.07

CANDS = ("end0", "end1", "vert", "root+", "root-")


# ------------------------------------------------------- exact moments

def hyper_pmf(big_n, k, draw=WINDOW):
    """Exact pmf of Hypergeometric(N, K, n) as a dict x -> Fraction."""
    def binom(n, r):
        if r < 0 or r > n:
            return 0
        out = 1
        for i in range(r):
            out = out * (n - i) // (i + 1)
        return out
    total = binom(big_n, draw)
    out = {}
    for x in range(0, draw + 1):
        w = binom(k, x) * binom(big_n - k, draw - x)
        if w:
            out[x] = Fraction(w, total)
    return out


def central_moments(pmf):
    """(mean, var, mu4) of a pmf, exact."""
    mean = sum(x * p for x, p in pmf.items())
    var = sum((x - mean) ** 2 * p for x, p in pmf.items())
    mu4 = sum((x - mean) ** 4 * p for x, p in pmf.items())
    return mean, var, mu4


def cell_population(a, b):
    """Exact (pi, A, G, B, mu4-terms) for the depth cell 2^a 3^b."""
    t = a + b
    pm = hyper_pmf(t - 1, a - 1)
    pn = hyper_pmf(t - 1, a)
    pu = hyper_pmf(t, a)
    mean_m, var_m, mu4_m = central_moments(pm)
    mean_n, var_n, _ = central_moments(pn)
    _, var_u, mu4_u = central_moments(pu)
    pi = Fraction(b, t)
    d = mean_n - mean_m
    bq = d * d
    g_ = var_n - var_m + bq
    a_ = var_u - var_m
    # The kurtosis term of var(A-hat) at n = 1, both samples.
    kurt = (mu4_u - var_u * var_u) + (mu4_m - var_m * var_m)
    return pi, a_, g_, bq, kurt


# ------------------------------------------------------- the estimator

def smi_labelled(feat_m, feat_n, feat_u):
    """The covariance-matching point estimate, with the label of the
    candidate the argmin came from and whether any root was in box.

    Candidate list and the strict-< first-wins tie-break are the
    sibling's, so the returned estimate is its estimate."""
    d = float(np.mean(feat_n) - np.mean(feat_m))
    bq = d * d
    a_ = float(np.var(feat_u) - np.var(feat_m))
    g_ = float(np.var(feat_n) - np.var(feat_m)) + bq

    cands = [(0.0, "end0"), (1.0, "end1")]
    in_box_root = False
    if bq > 0.0:
        cands.append((g_ / (2.0 * bq), "vert"))
        disc = g_ * g_ - 4.0 * bq * a_
        if disc >= 0.0:
            r = disc ** 0.5
            for p, tag in (((g_ + r) / (2.0 * bq), "root+"),
                           ((g_ - r) / (2.0 * bq), "root-")):
                cands.append((p, tag))
                if 0.0 <= p <= 1.0:
                    in_box_root = True
    elif abs(g_) > 0.0:
        cands.append((a_ / g_, "root+"))
        if 0.0 <= a_ / g_ <= 1.0:
            in_box_root = True

    best, best_f, best_tag = 0.0, None, "end0"
    for p, tag in cands:
        if 0.0 <= p <= 1.0:
            f = (a_ - p * g_ + p * p * bq) ** 2
            if best_f is None or f < best_f:
                best, best_f, best_tag = p, f, tag
    return best, best_tag, in_box_root, a_, g_, bq


# ---------------------------------------------------------- the world

def world_features(a, b, n, rng):
    """The sibling's fiber sampler, verbatim in behaviour: window
    counts of 2-moves in the WINDOW positions after the first, for
    class-conditional member (first move 2), non-member (first move 3),
    and unconditioned fiber samples."""
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


def phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


# --------------------------------------------------------- measurement

def run_cell(a, b):
    pi_x, a_x, g_x, b_x, kurt_x = cell_population(a, b)
    pi_f, a_p, g_p, b_p = (float(pi_x), float(a_x), float(g_x),
                           float(b_x))
    half = g_p / 2.0 - b_p / 4.0
    vert = g_p / (2.0 * b_p)
    lo = min(0.0, g_p - b_p)
    hi = max(0.0, g_p - b_p)
    if 0.0 <= vert <= 1.0:
        v = g_p * vert - b_p * vert * vert
        lo, hi = min(lo, v), max(hi, v)

    print(f"\n== cell (a,b) = ({a},{b})   pi = {pi_x} = {pi_f:.4f}")
    print(f"   A = {a_p:.7f}  G = {g_p:.7f}  B = {b_p:.7f}"
          f"   vertex = {vert:.4f}")
    print(f"   A-window [{lo:.6f}, {hi:.6f}]   A(1/2) = {half:.7f}"
          f"   gap A(1/2)-A = {half - a_p:.7f}")
    print(f"{'n':>6} {'flip':>6} {'rec':>6} {'pred':>6} {'sd_hat':>8}"
          f" {'sd_pred':>8}   {'agr_pop':>7} {'agr_own':>7}")
    print(f"{'':>6} {'v_in':>6} {'vert%':>6} {'noroot':>6}"
          f" {'flip|nr':>8} {'root|fl':>8}"
          f"   then argmin source, no-flip/flip")

    for idx, n in enumerate(AUDIT_SIZES):
        ests = np.empty(R_REPLICATES)
        avals = np.empty(R_REPLICATES)
        halves = np.empty(R_REPLICATES)
        vin = np.zeros(R_REPLICATES, dtype=bool)
        above = np.zeros(R_REPLICATES, dtype=bool)
        degen = np.zeros(R_REPLICATES, dtype=bool)
        tags = []
        noroot = np.zeros(R_REPLICATES, dtype=bool)
        for r in range(R_REPLICATES):
            fm, fn, fu = world_features(a, b, n, RNG)
            p, tag, has_root, a_h, g_h, b_h = smi_labelled(fm, fn, fu)
            ests[r] = p
            avals[r] = a_h
            # The law at the REPLICATE's own coefficients, which is
            # where the hand-attack derives it; the population plug is
            # the separate approximation.
            halves[r] = g_h / 2.0 - b_h / 4.0
            # A(p) is INCREASING on the box when the vertex sits above
            # it and decreasing when below, so the law's inequality
            # reverses with the vertex's side -- and again with the
            # side of 1/2 the truth sits on, since the flip is a
            # comparison against 1 - pi. B-hat = 0 is a REAL case here
            # (d-hat is a difference of integer-count means and hits 0
            # exactly at the smallest audit size): the objective is
            # linear, there is no vertex, and A(p) = G*p is increasing
            # iff G > 0. Reading a vertex of +inf there would code
            # every such replicate as increasing and invert the law
            # wherever G < 0.
            if b_h > 0.0:
                v_h = g_h / (2.0 * b_h)
                vin[r] = 0.0 <= v_h <= 1.0
                above[r] = v_h > 1.0
            elif g_h != 0.0:
                above[r] = g_h > 0.0
            else:
                # A(p) is identically 0: no direction exists at all.
                degen[r] = True
            tags.append(tag)
            noroot[r] = not has_root
        tags = np.array(tags)
        flip = np.abs(ests - (1.0 - pi_f)) < np.abs(ests - pi_f)
        law = avals < half
        law_own = (avals < halves) ^ above ^ (pi_f > 0.5)
        vin_rate = float(np.mean(vin))
        # The law is derived ONLY for vertex-outside replicates, so it
        # is scored only there: dis_out is the test and must be 0. A
        # vertex-inside replicate has no derived direction at all --
        # `above` is False there by arbitrary coding, so scoring those
        # would report that coding and not the law. Counted directly,
        # never inferred from the rate columns.
        broke = flip != law_own
        unscored = vin | degen
        n_in = int(unscored.sum())
        dis_out = int((broke & ~unscored).sum())
        n_out = R_REPLICATES - n_in
        agree_own = float(1.0 - dis_out / n_out) if n_out else float("nan")
        sd_hat = float(np.std(avals))
        sd_pred = math.sqrt(float(kurt_x) / n)
        pred = phi((half - a_p) / sd_pred)
        agree = float(np.mean(flip == law))
        vert_rate = float(np.mean(tags == "vert"))
        nr_rate = float(np.mean(noroot))
        flip_nr = (float(np.mean(flip[noroot])) if noroot.any()
                   else float("nan"))
        root_fl = (float(np.mean(np.isin(tags[flip], ("root+", "root-"))))
                   if flip.any() else float("nan"))
        counts = {}
        for t_, f_ in zip(tags, flip):
            counts[(t_, bool(f_))] = counts.get((t_, bool(f_)), 0) + 1
        parts = []
        for c in CANDS:
            nf = counts.get((c, False), 0)
            yf = counts.get((c, True), 0)
            if nf or yf:
                parts.append(f"{c} {nf}/{yf}")

        print(f"{n:>6} {float(np.mean(flip)):>6.3f}"
              f" {RECORDED[(a, b)][idx]:>6.3f} {pred:>6.3f}"
              f" {sd_hat:>8.5f} {sd_pred:>8.5f}   {agree:>7.3f}"
              f" {agree_own:>7.3f}")
        print(f"{'':>6} {vin_rate:>6.3f}"
              f" {vert_rate:>6.3f} {nr_rate:>6.3f}"
              f" {flip_nr:>8.3f} {root_fl:>8.3f}"
              f"   law broken {dis_out} of {n_out} scored"
              f" ({n_in} unscored)")
        print("         " + "  ".join(parts))


def main():
    print("THE FLIP AS A LEVEL SET OF A-hat -- "
          "cells the deletion audit records as flipping")
    print("PR1 is the gate: the 'flip' column must track 'rec' "
          f"within {PC_TOL:.2f} at every row.")
    for a, b in ((12, 3), (2, 8)):
        run_cell(a, b)


if __name__ == "__main__":
    main()
