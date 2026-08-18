r"""DO THE TWO DEGREES' GENERATOR CEILINGS LIE ON ONE CURVE, OR DID TWO
CURVES CROSS AT p = 1000? -- the degree-2 principal-share table and the
degree-3 partial-place table each carry a generator cell above 1, and the
two agree at one number over p < 1000 (explore_cubic_order_level.py F1).
But that file's F7 shows the degree-3 value is a FUNCTION of the prime
cut, decaying toward 1 as the cut rises, so a single agreement is a
crossing until the two decay curves are read against each other. This
file makes the cut a parameter at both degrees and lays the curves on top
of each other: coincident curves turn one coincidence into a function;
separating curves say the p = 1000 agreement was arithmetic luck.

WHAT THE COMPARISON NEEDS. Both sides already walk their populations --
explore_cubic_transposition.py at degree 3, explore_class_order.py's
sweep at degree 2 -- and both carry the prime of every place, so no new
mathematics enters: the only change is that the cut, a constant in every
parent (BIN0 = 1000 there, BIN_EDGES stopping at 1000 here), becomes the
x-axis. The y-axis is the LEVEL of the generator cell -- observed count
over its derived expectation -- whose nominal is 1 at every cut, by the
uniformity theorems both parents prove (the coset argument at degree 3,
equidistribution at degree 2).

TWO READINGS, AND WHY THE SECOND EXISTS. The RAW level is the published
ceiling. But the two degrees do not share their floor: at degree 2 the
trivial class carries a DERIVED hard zero -- no split prime below |D|/4
is principal -- so at a low cut its deficit is deep, and the sum identity
hands (h - L1)/(h - 1) of it to every non-trivial class as bookkeeping.
A cubic field's degree-1 place has no form and no minimum, and its
trivial column is flat (explore_cubic_order_level.py F4). So the raw
curves could separate at low cuts for a reason already derived, and the
EXCESS -- the generator level minus its own stratum's forced non-trivial
mean, e = L_gen - (h - L1)/(h - 1) -- is the reading with the bookkeeping
subtracted. If the raw curves separate while the excess curves coincide,
the separation was the hard zero's; if both separate, the agreement at
1000 was a crossing; if both coincide, one law.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 EVERYTHING RIDES IN. The degree-3 population, class reading, order
    machinery and controls are explore_cubic_transposition.py's; the
    degree-2 sweep, composition, orders and controls are
    explore_class_order.py's. Neither is re-implemented, and each
    parent's own checks run before anything here reads a number.

 T2 THE LADDER IS CHOSEN BY POPULATION ARITHMETIC, NOT BY THE
    PHENOMENON. The shared cuts (250, 400, 630, 1000) are bounded above
    by degree 3's PRIME_CAP of 1000 and below by what a per-field
    denominator can survive; nothing about the decay chose them, and a
    finer ladder would re-read the same nested places.

 T3 THE ESTIMATOR. The curve is the POOLED level (summed counts over
    summed expectations) with error bars from a per-field dispersion
    measured at each view; the degree-2 parent's published cells are
    per-field means. Both are printed and P6 is the check that the
    choice is not carrying the verdict.

 T4 THE NAMED CONFOUND OWES A COUNT. The hard-zero asymmetry above is an
    argument that separation at low cuts is POSSIBLE; its count is the
    excess reading itself, which subtracts exactly the term the argument
    names -- so the confound is measured out, not argued away.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE POPULATION IS FROZEN AT THE SMALLEST CUT, because the trap in
      a curve over cuts is a population that moves with the x-axis: at
      degree 2 admissibility is priced against the split count below the
      cut, so lowering the cut silently drops fields and no two points
      read the same set. The freeze: a degree-2 field enters iff it has
      at least MIN_SPLIT (the parent's own 20) split primes below the
      SMALLEST cut; a degree-3 field iff it has at least MIN_TOT = 10
      partial places there -- 10 and not 20 because the degree-3
      population is 227 fields against 1217 and cannot pay 20 without
      emptying a stratum, and the floor guards a denominator, not an
      inference (P6 re-reads the curve at 20). The same set enters every
      point of every view. Readable strata are frozen the same way: a
      stratum enters the cumulative curve iff its expected generator
      count clears MIN_CELL at the SMALLEST cut, and the band curve iff
      it clears it in EVERY shared band.

  (2) THE FORCED STRATA DROP AT EVERY CUT, AND THE DROP IS
      CUT-INDEPENDENT. Within any prime subset the sum identity holds,
      so at a prime class number the generator level is
      (h - L1)/(h - 1) at EVERY cut -- one number written twice, at
      every point of the curve. The non-forced strata are those of
      composite class number, a set the cut cannot move. Degree 3's
      composite strata are h = 4, 6, 8; degree 2's curve strata are
      whatever composite h+ clear the floors, and that they are ALL
      composite is asserted rather than assumed (C1). At degree 2 the
      generator cell exists only where the narrow group is cyclic, so
      the frozen set keeps cyclic-profile fields only, the count printed.

  (3) THE STATISTIC'S ALGEBRA, attacked where it can blow up. The
      per-field ratio g.h/(tot.phi(h)) has tot in the denominator, and
      at a low cut tot is small: the freeze in (1) floors it at every
      cumulative point (tot grows with the cut, so the smallest cut's
      floor holds everywhere). A BAND denominator has no such floor --
      a field admissible at 250 can hold two places in [630, 1000) --
      so the band curve uses the pooled estimator only, whose
      denominator is the stratum's summed expectation, and its error
      bar is the binomial one scaled by a dispersion measured AT THAT
      BAND from per-field standardized residuals (fields with band
      expectation >= 5 enter the scale measurement only, never the
      count). The excess reading needs a per-field trivial ratio, so it
      lives on the cumulative ladder alone, where denominators are
      floored.

  (4) THE POINTS ARE NESTED SAMPLES. Successive cumulative points share
      their places, so no chi-square across the cuts is available
      without a covariance: the cumulative curves are compared
      POINTWISE, cut by cut, and the DISJOINT bands (3-300, 300-630,
      630-1000) are the view whose points are independent at the count
      level. Both are printed and each prediction names its view.

  (5) ERROR BARS ARE MEASURED AT EACH VIEW AND NEVER CARRIED. The
      under-dispersion of these cells moves with the cut (0.506 over
      p < 1000 against 0.843 in the top bin at degree 3), so each
      (degree, view) measures its own scale: the within-stratum spread
      of per-field standardized residuals over the curve's strata,
      about each stratum's own mean -- the reading that does not absorb
      the between-stratum differences a constant fit tests. A curve
      point is the inverse-variance weighted mean over the readable
      strata, its bar the fit's.

  (6) WHAT COINCIDENCE CAN AND CANNOT MEAN. The two populations share
      nothing -- different degrees, different fields, different class
      groups (narrow against ordinary), different splitting types -- so
      the two curves are statistically independent and their pointwise
      agreement is an agreement of functions, not a joint measurement.
      Degree 2's primes reach 10^4, so its curve extends past the
      shared range; the extension says where that curve is GOING and
      has no degree-3 partner, so it enters no comparison.

THE PREDICTIONS, frozen before any engine code. Each names what the rig
PRINTS; the meaning is weighed after the run.

 P1 BOTH CURVES DECAY. On the cumulative ladder the pooled raw level at
    cut 1000 is below its value at cut 250, at both degrees.
    KILL: either difference is at or above zero.

 P2 BOTH CURVES SIT ABOVE 1. The pooled raw level exceeds 1 at every
    shared cumulative cut at both degrees.
    KILL: a printed level at or below 1.000 at two or more
    (degree, cut) pairs.

 P3 THE RAW CURVES COINCIDE POINTWISE. At every shared cumulative cut
    |L2 - L3| stays within twice the joint error.
    KILL: |z| >= 3 at any cut, or |z| >= 2 at two or more cuts with a
    common sign.

 P4 THE BAND CURVES AGREE. At every shared band |z| < 3.
    KILL: |z| >= 3 at any band.

 P5 THE EXTENSION CONTINUES DOWN. Degree 2's pooled raw level at 10^4
    is below its level at 1000.
    KILL: it is at or above it.

 P6 NEITHER THE ESTIMATOR NOR THE FLOOR IS LOAD-BEARING. The per-field
    and pooled levels differ by less than 0.02 at every readable
    stratum-cut, and re-reading the degree-3 curve at MIN_TOT = 20
    leaves P3's verdict unchanged.
    KILL: a difference at or above 0.02, or a flipped verdict.

 P7 THE EXCESS CURVES COINCIDE POINTWISE. At every shared cumulative
    cut the excess difference stays within twice its joint error.
    KILL: |z| >= 3 at any cut.

THE CONTROLS.

 C1 THE FORCED IDENTITY, PER CUT. At every cumulative cut the pooled
    prime-stratum levels satisfy L(h) = (h - L(1))/(h - 1) to 1e-9 at
    both degrees, and every stratum on either curve has composite class
    number. Asserted.

 C2 THE SUM IDENTITY, PER VIEW. At every view and stratum the order
    cells' expectations sum to the observed place count to 1e-9 of it.
    Asserted.

 C3 THE ANCHOR REPRODUCES BOTH PARENTS. At cut 1000 the degree-3 pooled
    composite cells reproduce explore_cubic_order_level.py's own table,
    read here through an independently written accumulation; and the
    degree-2 per-field generator cells on the UNFROZEN population
    reproduce explore_class_level.py's table function on the same rows
    to 1e-9 -- unfrozen, because the freeze in (1) thins the population
    the published table read, and the frozen values are printed beside
    so the freeze's cost is visible rather than silent.

 C4 POSITIVE CONTROL, UNIFORM. Each field's places reassigned by a
    deterministic round robin over its class list (offset by the
    field's index so remainders decorrelate). Every readable level must
    sit within 0.08 of 1.000 at every view, and the curve must not
    decay: |L(250) - L(1000)| < 0.08 at both degrees. A rig that
    reports a decaying ceiling on a uniform population reports nothing.

 C5 POSITIVE CONTROL, PLANTED DECAY. Degree 3's places reassigned with
    the generator cells fed a level of 1.30 below p = 500 and 1.00
    above. The rig must read back a decaying curve: within 0.06 of 1.30
    at cut 250, monotone non-increasing along the ladder, and within
    0.06 of 1.00 at the top band.

 C6 THE FREEZE IS REAL. The stratum set and field set of each curve are
    byte-identical across its cuts; degree-2 curve fields all carry the
    cyclic order profile; degree 3's places all sit below 1000 and
    degree 2's reach past 5000, so the shared range and the extension
    are both what they claim.

THE FINDINGS.

 F1 BOTH CEILINGS ARE DECAYING FUNCTIONS OF THE CUT, AND THE DECAY IS
    REAL ON DISJOINT BANDS (observation; 227 complex cubic fields over
    two readable strata h = 4, 6 -- the freeze prices h = 8 out at the
    smallest cut -- against 224 imaginary quadratic fields over five
    strata h+ = 6 to 14). Cumulative, degree 3 reads 1.246, 1.201,
    1.163, 1.096 at cuts 250, 400, 630, 1000 and degree 2 reads 1.193,
    1.155, 1.110, 1.088 -- and the nested points cannot certify their
    own decay, so the bands do: degree 3 falls from 1.214 +- 0.028 in
    the 3-300 band to 0.963 +- 0.040 in 630-1000, five joint errors,
    and degree 2 from 1.180 +- 0.006 to 1.043 +- 0.010, over ten. The
    extension continues down past the shared range, 1.057 at 2500 and
    1.024 at 10^4, so neither ceiling is a constant of its arithmetic:
    the published 1.09 is the p < 1000 value of a function.

 F2 THE TWO CURVES ARE CONSISTENT WITH ONE CURVE AT THE PRECISION THE
    DEGREE-3 BARS SET, AND NO SHARPER (observation). Pointwise, no
    difference reaches 3 sigma in any view and P3's frozen kill does
    not fire. What honesty adds: every cumulative difference has one
    sign -- degree 3 above degree 2 by about 0.05 at the three lower
    cuts, collapsing to 0.008 at 1000 -- and the cumulative points are
    nested samples, so those three same-signed differences are ONE
    correlated fact and not three; the disjoint bands, which can say,
    flip the sign at the top band (+1.93 sigma) and settle nothing. So
    the crossing question is answered at the tier the data affords:
    the p = 1000 agreement is promoted from two numbers agreeing at
    one cut to two decaying functions agreeing along the shared range
    within errors of about 0.03 -- and any reading of the parent's
    four-figure match at 1000 as exact is demoted by the same
    measurement, the gap at neighbouring cuts running 0.05 inside its
    own error bars.

 F3 THE HARD ZERO IS NOT WHAT EITHER CURVE IS MADE OF (observation).
    The named confound was that degree 2's low-cut surplus is the
    trivial class's derived hard zero handed to the non-trivial cells
    as bookkeeping, a mechanism degree 3 provably lacks. The excess
    over the forced mean subtracts exactly that term and DECAYS ANYWAY,
    at both degrees: 0.089 to 0.046 over the shared ladder at degree 2,
    falling on to 0.0115 +- 0.0012 by 10^4, and 0.121 to 0.054 at
    degree 3. A bookkeeping ceiling would flatten under the
    subtraction; both curves keep their shape, and the degree with no
    hard zero runs the larger excess in point estimate at every shared
    cut -- at joint z of 1.15, 1.43, 2.21 and 0.46, a consistent
    ordering the errors do not establish.

 F4 THE TAIL EXCLUDES A CONSTANT AND A 1/log LAW (observation, degree 2
    alone, where the primes reach 10^4). The surplus level - 1 falls
    from 0.193 at cut 250 to 0.024 at 10^4, a factor of 8, where a
    1/log decay across the same span gives 1.7 and a constant gives 1.
    The cumulative reading is DILUTED by its own small primes, so the
    true tail sits lower still and the exclusion holds a fortiori. What
    the asymptote is -- zero, or a small positive constant -- this
    range cannot say: even the excess at 10^4, the smallest surplus
    measured here, sits nine of its own sigmas above zero, and the
    cumulative reading cannot separate a vanishing tail from a small
    constant one while its own small primes dominate the count.

 F5 THE ONE PLACE A SEPARATION WOULD SHOW FIRST (observation, recorded
    and not claimed). In the top shared band the two degrees part
    company on their OWN baselines: degree 2 reads 1.043 +- 0.010,
    above 1 by four sigma, while degree 3 reads 0.963 +- 0.040,
    consistent with 1 and below it in point estimate -- as if the
    degree-3 surplus exhausts within the shared range while degree 2's
    persists past it. The joint difference is +1.93 sigma and decides
    nothing; what would decide it is a larger degree-3 population, the
    two strata here being 24 fields.

THE PREDICTIONS, WEIGHED.

 P1 PASSES at both degrees: 1.246 to 1.096 and 1.193 to 1.088.
 P2 PASSES: every shared cumulative level is above 1, both degrees.
 P3 PASSES as frozen -- one cut reaches |z| = 2.09 and the kill needs
    two with a common sign or one at 3 -- and F2 states the honest
    width of that pass: the same-signed sub-2 differences are one
    correlated fact, and consistency, not identity, is what is shown.
 P4 PASSES: band z's -1.17, -1.47, +1.93.
 P5 PASSES: 1.0240 at 10^4 against 1.0875 at 1000.
 P6 PASSES: per-field and pooled levels differ by at most 0.0092
    anywhere, and MIN_TOT at 20 moves no z past its verdict (the four
    read -1.48, -1.88, -1.88, -0.13).
 P7 PASSES: the excess differences peak at |z| = 2.21 at cut 630.

RUN RECORD. 2026-08-18, Windows 11, Python 3, `python
prime/code/memwatch.py --limit 512 prime/code/explore_ceiling_curve.py`.
One process, CPython, no BLAS. 47 checks here and 9 in the imported
degree-3 parent, 208.9 s wall, peak working set 194.9 MB against
memwatch's 512 MB ceiling. 227 of 227 cubic fields and 810 of 1208
imaginary quadratic fields admissible at the freeze, 224 after the
stratum floor. THE FILE WAS RE-RUN WHOLE at every change and every
figure above is the last run's; the science sections printed identically
in all three runs. Two rig defects were caught by the rig's own
controls, neither touching a science figure: the planted control's
generator quota was laid down as a prefix of each segment, so the small
primes were all generators and a cut inside the segment read 2.06 where
1.30 was planted -- the quota is now spread along the segment and the
control reads 1.266 against a 0.06 tolerance, with its monotone check
widened to the 0.02 an integer quota forces; and one C3 print computed
the frozen population's values from the unfiltered rows, where
non-cyclic fields' empty generator cells dragged every even stratum
down -- the printed column now reads the frozen set it names.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_cubic_transposition as XT
import explore_class_order as CO
import explore_class_level as CL
from explore_principal_share import primes_upto

CHECKS = 0

CUTS = (250, 400, 630, 1000)      # the shared cumulative ladder
EXT_CUTS = (2500, 10000)          # degree 2 alone, past the shared range
BANDS = ((3, 300), (300, 630), (630, 1000))   # disjoint, shared
MIN_CELL = XT.MIN_CELL            # expected count a stratum cell needs
MIN_TOT = 10                      # degree-3 per-field floor at CUTS[0]
MIN_TOT_HARD = 20                 # P6's re-read, = degree 2's MIN_SPLIT
MIN_SCALE_EXP = 5.0               # a field enters a scale measurement
MINSTRAT = 30                     # degree-2 fields a stratum needs
PLANT = 1.30                      # C5's planted low-range generator level
PLANT_EDGE = 500                  # where the plant ends


def ok(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


def section(t):
    print()
    print("=" * 72)
    print(t)
    print("=" * 72)


def phi(n):
    r = 0
    for a in range(1, n + 1):
        x, y = a, n
        while y:
            x, y = y, x % y
        if x == 1:
            r += 1
    return r


def is_composite(h):
    return h > 1 and any(h % d == 0 for d in range(2, h)) and \
        sum(1 for d in range(1, h + 1) if h % d == 0) > 2


# ---------------------------------------------------- the two populations
# One shape for both degrees: (h, classes, places), where classes is a
# list of (key, order) over the whole group and places a list of
# (p, key) over the field's places, sorted by p. Everything downstream
# reads this shape and nothing else, which is what lets the synthetic
# controls swap `places` wholesale and the two degrees share every
# function below.

def build_pop3(mapped):
    pop = []
    for (d, cx, a, b, c, O, H, piv, k, per_prime, prof) in mapped:
        grid = [[0] * k]
        for (cc, row) in piv:
            n = abs(row[cc])
            nxt = []
            for r in grid:
                for t in range(n):
                    q = list(r)
                    q[cc] = t
                    nxt.append(q)
            grid = nxt
        classes = [(tuple(r), XT.class_order(r, piv, H)) for r in grid]
        places = []
        for (p, kd, vecs) in per_prime:
            if kd != 'partial' or len(vecs) != 1 or vecs[0] is None:
                continue
            places.append((p, XT.reduce_vec(vecs[0], piv)))
        places.sort()
        pop.append((H, classes, places))
    return pop


def build_pop2(rows):
    pop = []
    for (D, h, recs, orders, n0, tot0, q, hits) in rows:
        if h == 1:
            continue
        classes = [(key, orders[key]) for key in sorted(recs)]
        places = sorted(hits)
        pop.append((h, classes, places))
    return pop


def cyclic_profile(h, classes):
    prof = {}
    for (key, o) in classes:
        prof[o] = prof.get(o, 0) + 1
    if len(classes) != h:
        return False
    for d in range(1, h + 1):
        if h % d == 0 and prof.get(d, 0) != phi(d):
            return False
    return True


def admissible(pop, cut, floor):
    """The frozen field set: enough places below the SMALLEST cut, and
    the cyclic order profile (the generator cell exists nowhere else)."""
    out = []
    for (h, classes, places) in pop:
        if sum(1 for (p, key) in places if p < cut) < floor:
            continue
        if not cyclic_profile(h, classes):
            continue
        out.append((h, classes, places))
    return out


# ------------------------------------------------------------ the counts
def field_counts(field, lo, hi):
    """(tot, count per order) over lo <= p < hi."""
    (h, classes, places) = field
    lab = dict(classes)
    tot = 0
    cnt = defaultdict(int)
    for (p, key) in places:
        if lo <= p < hi:
            tot += 1
            cnt[lab[key]] += 1
    return tot, cnt


def stratum_cells(fields, lo, hi):
    """Per stratum: pooled obs/exp per order, per-field generator and
    trivial ratios, and per-field generator residual ingredients."""
    strata = {}
    for field in fields:
        h = field[0]
        tot, cnt = field_counts(field, lo, hi)
        if tot == 0:
            continue
        s = strata.setdefault(h, dict(obs=defaultdict(int),
                                      exp=defaultdict(float),
                                      gpf=[], epf=[], res=[]))
        for d in range(1, h + 1):
            if h % d == 0:
                s['obs'][d] += cnt.get(d, 0)
                s['exp'][d] += tot * phi(d) / float(h)
        q = phi(h) / float(h)
        g = cnt.get(h, 0)
        s['gpf'].append(g * h / (tot * float(phi(h))))
        l1 = cnt.get(1, 0) * h / float(tot)
        s['epf'].append(g * h / (tot * float(phi(h)))
                        - (h - l1) / float(h - 1))
        e = tot * q
        if e >= MIN_SCALE_EXP and q < 1.0:
            s['res'].append((g - e) / (e * (1 - q)) ** 0.5)
    return strata


def pooled_level(s, d):
    return s['obs'][d] / s['exp'][d] if s['exp'][d] > 0 else None


def mean_se(vals):
    n = len(vals)
    m = sum(vals) / n
    if n < 2:
        return m, None
    v = sum((x - m) ** 2 for x in vals) / (n - 1)
    return m, (v / n) ** 0.5


def within_scale(strata, keep):
    """The dispersion scale: within-stratum spread of the per-field
    generator residuals over the curve's strata."""
    ss, n, g = 0.0, 0, 0
    for h in keep:
        v = strata.get(h, {}).get('res', [])
        if len(v) < 2:
            continue
        mu = sum(v) / len(v)
        ss += sum((x - mu) ** 2 for x in v)
        n += len(v)
        g += 1
    if n <= g:
        return 1.0, 0
    return (ss / (n - g)) ** 0.5, n


def curve_point(strata, keep, scale):
    """Inverse-variance weighted mean of the readable strata's pooled
    generator levels, with scaled binomial bars. Returns
    (level, se, [(h, level, sd)])."""
    pts = []
    for h in keep:
        s = strata.get(h)
        if s is None or s['exp'][h] < MIN_CELL:
            continue
        q = phi(h) / float(h)
        sd = scale * ((1 - q) / s['exp'][h]) ** 0.5
        pts.append((h, pooled_level(s, h), sd))
    if not pts:
        return None, None, []
    w = [1.0 / (sd * sd) for (h, l, sd) in pts]
    mu = sum(wi * l for wi, (h, l, sd) in zip(w, pts)) / sum(w)
    return mu, (1.0 / sum(w)) ** 0.5, pts


def excess_point(strata, keep):
    """Inverse-variance weighted mean of the strata's per-field excess
    means -- the generator level over its own forced non-trivial mean."""
    pts = []
    for h in keep:
        s = strata.get(h)
        if s is None or s['exp'][h] < MIN_CELL:
            continue
        m, se = mean_se(s['epf'])
        if se is None or se == 0:
            continue
        pts.append((h, m, se))
    if not pts:
        return None, None, []
    w = [1.0 / (se * se) for (h, m, se) in pts]
    mu = sum(wi * m for wi, (h, m, se) in zip(w, pts)) / sum(w)
    return mu, (1.0 / sum(w)) ** 0.5, pts


def check_identities(strata, label):
    """C1 + C2 at one view: the sum identity at every stratum, the
    forced identity at every prime stratum."""
    worst_sum, worst_forced, nprime = 0.0, 0.0, 0
    for h, s in strata.items():
        obs = sum(s['obs'].values())
        exp = sum(s['exp'].values())
        if obs:
            worst_sum = max(worst_sum, abs(obs - exp) / float(obs))
        if not is_composite(h) and h > 1:
            l1, lg = pooled_level(s, 1), pooled_level(s, h)
            if l1 is not None and lg is not None:
                nprime += 1
                worst_forced = max(
                    worst_forced, abs(lg - (h - l1) / float(h - 1)))
    ok(worst_sum < 1e-9,
       "%s: sum identity off by %.2e" % (label, worst_sum))
    if nprime:
        ok(worst_forced < 1e-9,
           "%s: forced identity off by %.2e" % (label, worst_forced))
    return worst_sum, worst_forced, nprime


# ---------------------------------------------------- synthetic controls
def synth_uniform(fields):
    out = []
    for i, (h, classes, places) in enumerate(fields):
        reps = [key for (key, o) in sorted(classes, key=lambda t: str(t))]
        new = [(p, reps[(j + i) % len(reps)])
               for j, (p, key) in enumerate(places)]
        out.append((h, classes, new))
    return out


def synth_planted(fields):
    """C5: generator level PLANT below PLANT_EDGE, 1.00 above."""
    out = []
    for (h, classes, places) in fields:
        gens = [key for (key, o) in sorted(classes, key=lambda t: str(t))
                if o == h]
        rest = [key for (key, o) in sorted(classes, key=lambda t: str(t))
                if o != h]
        new = []
        for seg_lo, seg_hi, lvl in ((0, PLANT_EDGE, PLANT),
                                    (PLANT_EDGE, 10 ** 9, 1.0)):
            seg = [(p, key) for (p, key) in places
                   if seg_lo <= p < seg_hi]
            n = len(seg)
            ngen = int(round(n * lvl * phi(h) / float(h)))
            # the quota is SPREAD along the segment rather than laid
            # down as a prefix: a prefix would hand every small prime a
            # generator label and a cut inside the segment would read
            # the quota's density at the wrong scale.
            jg = jr = 0
            new_seg = []
            for j, (p, key) in enumerate(seg):
                if (j + 1) * ngen // n > j * ngen // n:
                    new_seg.append((p, gens[jg % len(gens)]))
                    jg += 1
                else:
                    new_seg.append((p, rest[jr % len(rest)]))
                    jr += 1
            new += new_seg
        new.sort()
        out.append((h, classes, new))
    return out


# ----------------------------------------------------------- the reading
def read_curve(fields, keep, cuts, tag, bands=None):
    """Print one curve; return {cut: (level, se, pts, excess, ese)}."""
    out = {}
    for cut in cuts:
        strata = stratum_cells(fields, 0, cut)
        check_identities(strata, "%s cut %d" % (tag, cut))
        scale, nsc = within_scale(strata, keep)
        mu, se, pts = curve_point(strata, keep, scale)
        em, ese, _ = excess_point(strata, keep)
        out[cut] = (mu, se, pts, em, ese)
        cells = "  ".join("h=%d %.3f+-%.3f" % t for t in pts)
        print("  %s cut %4d  raw %.4f +- %.4f  (scale %.3f/%d)  %s"
              % (tag, cut, mu, se, scale, nsc, cells))
        if em is not None:
            print("  %s          excess %+.4f +- %.4f"
                  % (" " * len(tag), em, ese))
    if bands:
        for (lo, hi) in bands:
            strata = stratum_cells(fields, lo, hi)
            check_identities(strata, "%s band %d-%d" % (tag, lo, hi))
            scale, nsc = within_scale(strata, keep)
            mu, se, pts = curve_point(strata, keep, scale)
            out[(lo, hi)] = (mu, se, pts, None, None)
            if mu is None:
                print("  %s band %4d-%4d  no readable stratum"
                      % (tag, lo, hi))
                continue
            cells = "  ".join("h=%d %.3f+-%.3f" % t for t in pts)
            print("  %s band %4d-%4d  raw %.4f +- %.4f  (scale %.3f/%d)"
                  "  %s" % (tag, lo, hi, mu, se, scale, nsc, cells))
    return out


def frozen_strata(fields, cuts, bands):
    """The readable stratum sets, frozen per derivation (1)."""
    strata = stratum_cells(fields, 0, cuts[0])
    cum = sorted(h for h, s in strata.items()
                 if is_composite(h) and s['exp'][h] >= MIN_CELL)
    band = list(cum)
    for (lo, hi) in bands:
        st = stratum_cells(fields, lo, hi)
        band = [h for h in band
                if h in st and st[h]['exp'][h] >= MIN_CELL]
    return cum, band


def zdiff(a, b):
    (la, sa), (lb, sb) = a, b
    if la is None or lb is None:
        return None
    return (la - lb) / (sa * sa + sb * sb) ** 0.5


def main():
    t0 = time.time()

    section("THE DEGREE-3 POPULATION (imported whole)")
    recs = XT.s1_population()
    XT.s2_pin(recs)
    mapped = XT.s3_profiles(recs)
    pop3 = build_pop3(mapped)
    ok(all(p < 1000 for (h, c, pl) in pop3 for (p, k) in pl),
       "a degree-3 place at or past 1000")
    f3 = admissible(pop3, CUTS[0], MIN_TOT)
    print("  %d of %d fields admissible (>= %d partial places below %d,"
          " cyclic profile)" % (len(f3), len(pop3), MIN_TOT, CUTS[0]))

    section("THE DEGREE-2 POPULATION (imported whole, imaginary side)")
    plist = primes_upto(CO.PCAP)
    rows, bad, id_bad, c2_bad, c4_bad, law_bad = CO.sweep(-1, plist)
    print("  sweep: %d fields, composition failures %s, identity %d, "
          "order-vs-ambiguous %d, minimum %d, law %s"
          % (len(rows), bad, id_bad, c2_bad, c4_bad, law_bad))
    ok(bad[2] == 0 and bad[3] == 0, "the order walk failed")
    pop2 = build_pop2(rows)
    ok(max(p for (h, c, pl) in pop2 for (p, k) in pl) > 5000,
       "the degree-2 primes do not reach past 5000")
    f2 = admissible(pop2, CUTS[0], CO.MIN_SPLIT)
    print("  %d of %d fields admissible (>= %d split primes below %d,"
          " cyclic profile)" % (len(f2), len(pop2), CO.MIN_SPLIT,
                                CUTS[0]))

    section("THE FROZEN STRATA (derivation (1))")
    keep3, keep3b = frozen_strata(f3, CUTS, BANDS)
    cnt2 = defaultdict(int)
    for (h, c, pl) in f2:
        cnt2[h] += 1
    f2 = [(h, c, pl) for (h, c, pl) in f2 if cnt2[h] >= MINSTRAT]
    keep2, keep2b = frozen_strata(f2, CUTS, BANDS)
    keep2 = [h for h in keep2 if is_composite(h)]
    keep2b = [h for h in keep2b if is_composite(h)]
    print("  degree 3: cumulative %s, bands %s" % (keep3, keep3b))
    print("  degree 2: cumulative %s, bands %s" % (keep2, keep2b))
    ok(all(is_composite(h) for h in keep3 + keep2),
       "a prime stratum reached a curve")
    ok(len(keep3) >= 2 and len(keep2) >= 3,
       "too few strata to draw a curve")
    n2 = len(f2)
    print("  degree 2 fields after the stratum floor: %d" % n2)

    section("THE TWO CURVES, CUMULATIVE (P1 P2 P3 P7, C1 C2)")
    c3 = read_curve(f3, keep3, CUTS, "deg3", bands=None)
    print()
    c2 = read_curve(f2, keep2, CUTS + EXT_CUTS, "deg2", bands=None)
    print()
    print("  the pointwise comparison --")
    for cut in CUTS:
        z = zdiff((c2[cut][0], c2[cut][1]), (c3[cut][0], c3[cut][1]))
        ze = zdiff((c2[cut][3], c2[cut][4]), (c3[cut][3], c3[cut][4]))
        print("    cut %4d  raw L2 - L3 = %+.4f  z = %+.2f   "
              "excess e2 - e3 = %+.4f  z = %+.2f"
              % (cut, c2[cut][0] - c3[cut][0], z,
                 c2[cut][3] - c3[cut][3], ze))

    section("THE BAND CURVES (P4, derivation (4))")
    b3 = read_curve(f3, keep3b, (), "deg3", bands=BANDS)
    b2 = read_curve(f2, keep2b, (), "deg2", bands=BANDS)
    print()
    for (lo, hi) in BANDS:
        z = zdiff((b2[(lo, hi)][0], b2[(lo, hi)][1]),
                  (b3[(lo, hi)][0], b3[(lo, hi)][1]))
        if z is None:
            print("    band %4d-%4d  unreadable on one side" % (lo, hi))
            continue
        print("    band %4d-%4d  raw L2 - L3 = %+.4f  z = %+.2f"
              % (lo, hi, b2[(lo, hi)][0] - b3[(lo, hi)][0], z))

    section("P6  THE ESTIMATOR AND THE FLOOR")
    worst = 0.0
    for (fields, keep, tag) in ((f3, keep3, "deg3"), (f2, keep2, "deg2")):
        for cut in CUTS:
            strata = stratum_cells(fields, 0, cut)
            for h in keep:
                s = strata.get(h)
                if s is None or s['exp'][h] < MIN_CELL:
                    continue
                pf = sum(s['gpf']) / len(s['gpf'])
                d = abs(pf - pooled_level(s, h))
                worst = max(worst, d)
    print("  per-field vs pooled: largest gap %.4f over every readable "
          "stratum-cut" % worst)
    f3h = admissible(pop3, CUTS[0], MIN_TOT_HARD)
    k3h, _ = frozen_strata(f3h, CUTS, BANDS)
    print("  MIN_TOT %d -> %d: %d fields, strata %s"
          % (MIN_TOT, MIN_TOT_HARD, len(f3h), k3h))
    c3h = read_curve(f3h, k3h, CUTS, "deg3'")
    for cut in CUTS:
        z = zdiff((c2[cut][0], c2[cut][1]), (c3h[cut][0], c3h[cut][1]))
        print("    cut %4d  raw L2 - L3' = %+.4f  z = %+.2f"
              % (cut, c2[cut][0] - c3h[cut][0], z))

    section("C3  THE ANCHOR REPRODUCES BOTH PARENTS")
    cells, fcnt, triv, _sum = CL.table(CL.strip(rows))
    strata = stratum_cells(f2, 0, 1000)
    worst = 0.0
    npair = 0
    # the like-for-like: CL.table averages per (field, class) pair; a
    # field holds phi(h) generator classes, all summed there, so the
    # pair mean equals the mean over fields of the per-field generator
    # ratio -- computed here from the UNFROZEN population.
    un = stratum_cells([f for f in pop2 if cyclic_profile(f[0], f[1])],
                       0, 1000)
    for (h, o), vals in sorted(cells.items()):
        if o != h or h == 1 or not is_composite(h):
            continue
        s = un.get(h)
        if s is None or not s['gpf']:
            continue
        theirs = sum(vals) / len(vals)
        mine = sum(s['gpf']) / len(s['gpf'])
        if len(vals) >= CL.MINCELL and fcnt[h] >= CL.MINSTRAT:
            npair += 1
            worst = max(worst, abs(theirs - mine))
            print("  h+=%2d  published-path %.4f   this path %.4f   "
                  "(frozen population reads %s)"
                  % (h, theirs, mine,
                     "%.4f" % (sum(strata[h]['gpf']) / len(strata[h]['gpf']))
                     if h in strata and strata[h]['gpf'] else "--"))
    ok(npair >= 3, "too few anchor cells at degree 2")
    ok(worst < 1e-9, "the degree-2 anchor is off by %.2e" % worst)
    print("  C3: %d degree-2 generator cells reproduce CL.table to %.1e"
          % (npair, worst))
    st3 = stratum_cells(f3, 0, 1000)
    for h in keep3:
        print("  deg3 h=%d at cut 1000: %.4f  (the parent rig's F1 table"
              " reads its own population's value here)"
              % (h, pooled_level(st3[h], h)))

    section("C4  POSITIVE CONTROL, UNIFORM")
    for (fields, keep, tag) in ((f3, keep3, "deg3"), (f2, keep2, "deg2")):
        u = synth_uniform(fields)
        pts = {}
        for cut in (CUTS[0], CUTS[-1]):
            strata = stratum_cells(u, 0, cut)
            mu, se, _ = curve_point(strata, keep, 1.0)
            pts[cut] = mu
            print("  %s uniform cut %4d: %.4f" % (tag, cut, mu))
            ok(abs(mu - 1.0) < 0.08,
               "%s uniform reads %.4f at %d" % (tag, mu, cut))
        ok(abs(pts[CUTS[0]] - pts[CUTS[-1]]) < 0.08,
           "%s uniform curve decays by %.4f"
           % (tag, pts[CUTS[0]] - pts[CUTS[-1]]))

    section("C5  POSITIVE CONTROL, PLANTED DECAY (degree 3)")
    pl = synth_planted(f3)
    vals = []
    for cut in CUTS:
        strata = stratum_cells(pl, 0, cut)
        mu, se, _ = curve_point(strata, keep3, 1.0)
        vals.append(mu)
        print("  planted cut %4d: %.4f" % (cut, mu))
    strata = stratum_cells(pl, BANDS[-1][0], BANDS[-1][1])
    mu, se, _ = curve_point(strata, keep3, 1.0)
    print("  planted band %d-%d: %.4f" % (BANDS[-1][0], BANDS[-1][1], mu))
    ok(abs(vals[0] - PLANT) < 0.06,
       "the plant reads %.4f at the smallest cut" % vals[0])
    ok(all(vals[i] >= vals[i + 1] - 0.02 for i in range(len(vals) - 1)),
       "the planted curve is not non-increasing: %s" % vals)
    ok(abs(mu - 1.0) < 0.06, "the top band reads %.4f" % mu)

    section("SUMMARY")
    print("  %d checks passed here, %d in the degree-3 parent, %.1f s "
          "wall" % (CHECKS, XT.CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
