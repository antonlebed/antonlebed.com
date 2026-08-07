"""Why is the containment step 3? A closed form for the carry of every
coordinate, and the dichotomy read off it.

THE QUESTION. explore_slope_window.py left one thing open and welded the
rest to it. Its L3 measured that the containing carries

    S = {C in [0, b^Delta) : sigma^{-1} C mod n <= 2 M_Delta}

are EXACTLY the multiples of their least positive member at 3508 of the
3516 non-contained pairs below mu = 0.4, that member being 3 at 3324;
and its L4 measured that those same 8 exceptions are set-equal to the 8
pairs where the middle window W holds an attainable coordinate. So the
step and the dichotomy are one fact seen twice: derive the step and the
empty window follows. Nothing there derived it. Three candidates were
named for what the 3 is a function of -- b, the ratio rho = 2a/(b-1),
or the census's own 2a + 1 >= b filter -- and this file answers with a
formula in which all three appear.

Notation is the family's, unchanged, at phase 0: L = v, N = v b^c,
q = u, g = gcd(u, N), n = N/g, sigma = u/g a unit of Z/n, r_j the
repunit, M_j = a r_j, Delta = j - i, y the coordinate of
explore_slope_empty.py's (P), C(y) = sigma.y mod n its carry, and

    CONTAINMENT   needs  y <= 2 M_Delta,
    MEETING       needs  y <= 2 M_j  or  y >= n - 2 M_j + 2 M_Delta.

THE DERIVATION, hand-attacked on paper before this engine existed, and
checked by hand at the residual cell (b, a, c, u, v) = (6, 3, 5, 9088, 7)
before a line of it was written down.

(A) THE MASTER IDENTITY, AND WHERE THE CENSUS FILTER LIVES. The span
    endpoint is E = floor(a(N - u)/(b - 1)), so with s = a(N - u) mod
    (b - 1) and the span deficit e = N - (2E + 1),

        kappa := (b - 1) N - 2a(N - u) = (b - 1)(1 + e) - 2s,

    and rearranging the left form,

        kappa = 2a.u - (2a - b + 1) N,

    whose multiplier 2a - b + 1 is non-negative EXACTLY under the
    census's own 2a + 1 >= b filter. So under that filter kappa is the
    residue 2a.u mod N, reached at a known wrap count -- the filter is
    not a convenience of the sweep, it is what makes the identity a
    reduction. The span-deficit reading D + 1 = N(1 - rho) + rho.q is this
    same quantity divided by b - 1, so rho enters here and nowhere
    else, and the exactness qualifier that reading carries is the
    s = 0 case of the second form.

(B) THE CARRY OF EVERY COORDINATE, IN CLOSED FORM. Let
    h = gcd(2a, b - 1) and tau(y) = (-y(b - 1)) mod 2a, which is a
    multiple of h for every y. Then for every y with y.kappa < N,

        C(y) = (N.tau(y) + y.kappa) / (2a g).

    Both terms are non-negative, so a SMALL carry needs a small tau AND
    a small y: the carry is a two-term cost and the coordinate pays
    both. The identity is (A) divided by 2a, which is legitimate exactly
    because tau supplies the wrap the division would otherwise lose.

(C) THE STEP. tau(y) = 0 iff y is a multiple of y* = 2a/h, and then
    C(k y*) = k.kappa/(hg). So

        step := kappa / (h g),   witnessed at  y* = 2a / h,

    and where n.h > 2a.b^Delta no coordinate with tau > 0 is attainable
    at all, whence Y_Delta cap [0, 2 M_j] = {k y* : k step < b^Delta}
    and S is the progression L3 measured. Its step is a function of
    kappa, h and g -- of the span deficit, the digit-set/radix gcd and
    the cell's own gcd -- and of b only through those.

(D) THE DICHOTOMY, READ OFF THE STEP. Containment is k <= h r_Delta and
    the lower meeting arc is k <= h r_j, so the lower arc is empty iff

        (h r_Delta + 1) . step  >=  b^Delta,

    one inequality between four small integers where a three-distance
    theorem was thought to be owed. For the upper arc, C(n - y) =
    n - C(y), so an attainable coordinate there is a y <= 2 M_j -
    2 M_Delta with N.tau'(y) - y.kappa < 2a g b^Delta, tau'(y) =
    2a - tau(y); the smallest such cost sits at tau' = h and the
    largest admissible y, which is why the upper arc is the tighter of
    the two and why it tightens as mu grows.

(E) WHAT SHOULD THEREFORE FAIL. The residual cell has b^Delta = 36,
    step 3, h = 1, r_Delta = r_2 = 7: (7 + 1).3 = 24 < 36, so the lower
    arc must hold the carries 24, 27, 30, 33 -- four of them, which is
    what L4 counted. The progression there is truncated by 2 M_Delta
    before b^Delta cuts it, which is the same fact in the C coordinate.

THE DESIGN, frozen before the engine.

E-A THE IDENTITY, as a control over every cell of the census: kappa in
    [0, N), kappa = 2a.u mod N, kappa = (b - 1)(1 + e) - 2s, and
    h g | kappa. Any miss and nothing below is read.

E-B THE STEP, predicted against measured. Over the below-cut population
    the measured least positive member of S comes from the parent's own
    loop over C in [0, b^Delta); the prediction is kappa/(hg) and the
    witness y* = 2a/h. Report agreement, and separately the population
    where S is EMPTY (no containing carry at all), where the claim is
    vacuous and must be counted rather than scored.

E-C THE CLOSED FORM AGAINST THE LOOP. The prize: predict
    |Y_Delta cap W| from (B) alone -- a loop over the at most 2a/h
    residue classes of tau, arithmetic within each -- and compare pair
    by pair with the parent's loop over all b^Delta carries. Two
    computations sharing no code path; agreement everywhere is the
    derivation, and any disagreement is reported with its cell. The
    side condition y.kappa < N is checked per pair, never assumed, over
    the range the form DECIDES rather than at the points it counts.
    And (B) is checked POINTWISE beside the aggregate -- carry_closed
    against the true carry at both ends of that range -- since a count
    can agree while the formula behind it is wrong in compensating
    directions.

E-D WHY 3. The distribution of step over the below-cut population,
    factored against b, h, e, s and g; whether step >= 3 always; and
    whether the 8 exceptions are exactly the pairs failing (D)'s
    inequality. A formula that reproduces the count but not the
    exceptions has not derived the dichotomy.

E-F, E-G and E-H were frozen LATER, each after the pass before it printed
and before it was written; each carries its own freeze in its own
function docstring, which is where the reason it exists is legible.

E-E IS THE 3 THE FILTER'S 3? The census runs at below-count >= 3 and
    the step is 3: a coincidence of two threes that a sweep settles in
    one pass. Re-run the step distribution at min_below = 2 and 4 at a
    reduced cap. (C) says the step cannot depend on min_below, since no
    term of kappa/(hg) sees it; a shift in the distribution would kill
    the derivation, and an unchanged mode kills the coincidence.

KILLS, frozen as what this rig PRINTS.

K1 A control of E-A misses -> the identity is wrong and nothing below
   is read.
K2 The predicted step differs from the measured least member at any
   pair -> (B) or (C) is wrong; the pair is printed.
K3 The closed-form window count differs from the loop count at any pair
   -> the dichotomy is NOT read off the step and the weld E-M measured
   is not a derivation. This is the kill that matters.
K4 step < 3 anywhere in the below-cut population -> "why 3" is answered
   as "it is not always 3", the constant is a census artifact, and what
   carries the dichotomy is (D)'s inequality rather than the value.
K5 The step distribution moves with min_below -> (C) is missing a term.

POSITIVE CONTROL, run and read before any verdict line: the parent's
headline reproduced through this file's own walk -- the below-cut
population and the count of pairs whose window holds an attainable
coordinate, which must print 3516 and 8.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

M1 THE CARRY HAS A CLOSED FORM AND THE STEP IS kappa/(h g), EXACTLY.
   The identity holds at 11,095 of 11,095 cells in all four of its
   forms -- kappa in [0, N), kappa = 2a.u mod N, kappa =
   (b-1)(1+e) - 2s, and h g | kappa -- and the census span is 2E + 1 at
   every one of them, so the rigidity the derivation reads off is the
   census's actual shape and not an assumption about it. The predicted
   step matches the measured least positive member of S at 3516 of
   3516 below-cut pairs, with no pair where S = {0} makes the claim
   vacuous. So the answer to "what is the 3 a function of" is: the span
   deficit through kappa, the digit-set/radix gcd h = gcd(2a, b-1), and
   the cell's own g. Of the three candidates the handoff named, rho
   enters only as kappa/(b-1), b only through h and the ceiling of M3,
   and the 2a + 1 >= b filter in the one place that matters -- it is
   what makes the multiplier 2a - b + 1 non-negative and kappa a
   residue, so the filter is load-bearing for the reduction rather than
   a convenience of the sweep.

M2 AND THE DICHOTOMY IS AN INEQUALITY BETWEEN FOUR SMALL INTEGERS. The
   closed form predicts |Y_Delta cap W| pair by pair, against the parent's
   loop over all b^Delta carries, at 3516 of 3516 with ZERO disagreements
   -- including at the 16 pairs where the closed form's own y.kappa < N
   precondition FAILS over the range it decides, by a hair (worst 2 M_j
   kappa / N = 1.0043, printed), so that is sufficient and not necessary --
   and not needed at all once the wrap is reduced explicitly (M6's settling
   pointer) and the 16 are agreement without a warrant rather than
   agreement with one. Beside the aggregate, (B) itself is checked
   pointwise against the true carry at both ends of the decided range -- 0
   misses over 230,208 coordinates -- so the count is not agreeing by two
   errors cancelling. The two computations share no code path: one walks
   the carries, the other reads at most 2a/h residue classes of tau(y) =
   (-y(b-1)) mod 2a arithmetically. So the emptiness is not measured any
   more, it is READ OFF:

       the lower arc is empty  iff  (h r_Delta + 1) . step >= b^Delta.

   Verified in BOTH directions -- the pairs failing the inequality and
   the pairs whose window is non-empty are the same 8, set-equal and
   not merely equinumerous. It carries ONE hypothesis and the
   hypothesis is the census's own: the inequality counts only the
   tau = 0 coordinates, which is the whole attainable set exactly when
   n.h > 2a.b^Delta, printed at a minimum of 5.7812 and forced rather
   than observed -- a below-count of 3 makes n > 2a.r_3 and the measure
   cut makes Delta <= 2, so n.h > 2a.b^2 . 1 with room. Outside those
   two filters the criterion is not the whole statement, which is the
   first thing to check at any wider scope.

M3 WHY 3: THE STEP HAS A CEILING AND THE CENSUS SITS AT IT WHEN IT IS
   RIGID. kappa <= (b-1) g forces step <= (b-1)/h, and step = (b-1)/h
   at 2972 of 3516 -- exactly the 2972 rigid cells, e = g-1 and s = 0,
   the biconditional holding at 3516 of 3516. E-F predicted the ceiling
   would be met "at nearly every pair" and 2972 of 3516 is 84.5%, so
   that half of its slate is WRONG as written: one pair in six sits
   below its ceiling, which is a population and not a residual, and it
   is the population that carries the 8 failures. The prediction that
   held is the other one, that the residual cell would be among the
   misses. That biconditional is
   DERIVED and the census only checks it: kappa = (b-1)g rearranges to
   (b-1)(1 + e - g) = 2s, and e <= g-1 makes the left side <= 0 while
   s >= 0 makes the right >= 0, so both vanish. Filing it as a measured
   agreement would have understated it by a tier. The below-cut radix
   census is {4: 2784, 6: 720, 10: 12} and the joint (b, h, step,
   Delta) is {(4,1,3,1): 2784, (6,1,3,1): 528, (6,1,3,2): 8,
   (6,1,5,1): 160, (6,1,5,2): 24, (10,1,5,1): 8, (10,3,3,1): 4} --
   carrying Delta because that is what separates the tight pairs from
   the failing ones and a joint without it invites reading 536 as one
   population. So the 3 is (b-1)/h at b = 4, which is where the
   population is; the 192 pairs the parent could only call "5 or more"
   are exactly 5, and there is no long tail. Two riders. The step is
   ODD at 3516 of 3516 and takes 3, 5, 7, 9 under the loosened filter
   of E-E -- an OBSERVATION with no derivation here, and only half
   explained by the ceiling, since 544 pairs sit below their ceiling
   and are odd anyway. And the 3 is NOT the census's below-count >= 3:
   at min_below = 2 the below-cut population is 1624 with steps
   {3: 1400, 5: 212, 7: 8, 9: 4}, the mode unmoved and two new values
   arriving with the wider radix population rather than with the
   filter, exactly as (C) requires -- K5 did not fire, and the
   coincidence of two threes is closed.

M4 SO THE 8 ARE NOT EXCEPTIONS, THEY ARE THE OTHER SIDE OF A CRITERION,
   AND THE LAW STOPS BEING A PATTERN. The residual cell is not rigid --
   e = 19 against g - 1 = 31, s = 2 -- so its step is 3 where its
   ceiling is 5, and (h r_Delta + 1) step = 8 . 3 = 24 < 36 = b^Delta.
   The inequality fails by exactly the carries 24, 27, 30, 33, which is
   the count of 4 the parent measured at each of the 8 classes. What
   looked like a rate of 3508/3516 with a located residual is one
   exhaustive law with no residual at all, and the split is by Delta
   and not by cell: the 536 pairs at b = 6 with step 3 below their
   ceiling divide 528 at Delta = 1, where the inequality reads
   2 . 3 >= 6 and holds with EQUALITY -- the one place in the census
   the criterion is exactly tight -- against the 8 at Delta = 2, which
   are the failures. So b = 6 with a step below its ceiling supplies
   both the tight pairs and the failing ones, and what separates them
   is the level difference alone.

M5 THE LOWER ARC IS A PROPERTY AT EVERY RIGID CELL, WHICH LEAVES THE
   UPPER ARC AS THE WHOLE REMAINING QUESTION. At step = (b-1)/h the
   inequality reads r_Delta(b-1) + (b-1)/h = b^Delta - 1 + step
   >= b^Delta, true for every b, h and Delta with margin exactly
   step - 1 and no census in the argument. Split by arc, all 32
   attainable coordinates of the residual sit in the LOWER arc and the
   upper arc holds none at 3516 of 3516, clearing by a factor of 1.0556
   at the tightest against a median of 7 -- which SPLITS E-G's frozen
   prediction rather than confirming it: "the minimum is well above 1"
   is right about the bulk and wrong about the minimum, 1.0556 being a
   margin of one part in eighteen. The half that missed is the half
   that matters, since a margin that small is what a wider census
   spends first, and reading the median as the verdict is how a
   prediction gets scored on the population instead of on its own
   claim. So the handoff's watch was
   right that the upper arc is the tighter -- its margin is measured
   and can be made small, where the lower arc's is structural -- and
   the upper arc is the half a wider census would break first.

M7 AND THE DICHOTOMY ONLY EXISTS WHERE THE CEILING EXCEEDS 1 -- WHICH
   IS WHY THE RADIX CENSUS LOOKED LIKE A CENSUS. Where h = b-1 the
   ceiling (b-1)/h is 1, so step = 1 and the containing carries run to
   h r_Delta = b^Delta - 1: S is EVERY carry, the pair contains, and
   there is no dichotomy to have. That is 1,763,726 of the census's
   1,786,658 pairs -- 98.7% -- with 0 of them failing either half, and
   it is a PROPERTY, the count being the check. b = 2 and b = 3 force
   it (h = 1 = b-1 and h = 2 = b-1 always) and supply 1,731,830 pairs
   between them, every one contained; b = 4 and b = 6 reach it too,
   whenever (b-1) | 2a, at another 31,896. So the non-contained radices
   are exactly {4, 6, 10}, the radices with ceiling-above-1 cells, and
   the below-cut census {4: 2784, 6: 720, 10: 12} is not an even-number
   fact at all: it is the ceiling's floor, and M6's "even-only with no
   reason offered" was conflating that law with a scope statement about
   b = 5, 7, 8, 9, 11 and 12, which are absent from the census outright
   at this cap. The oddness of the step is now half-derived too -- at
   the ceiling, b even makes b-1 odd, h odd and (b-1)/h odd -- with the
   544 below-ceiling pairs still unexplained.

M6 WHAT IS STILL OWED (SETTLED in explore_slope_arc.py: all three
   items below are discharged there and the first two of them changed what
   this file says. The precondition is not a condition -- reducing the wrap
   explicitly gives C(y) = ((N.tau + y.kappa)/(2a g)) mod n for EVERY y --
   so M2's "sufficient and not necessary" and its 16 warrantless pairs are
   an artefact of the unreduced form; the closed form then decides the
   above-cut population too, by floor-sum rather than loop; the upper arc
   has its criterion, n.h >= 2a b^Delta + h.step.y_max, and its first
   FAILURE at mu = 0.4597, which makes M5's emptiness a below-the-cut law;
   and the step's oddness is n's, not the step's. What survives here
   unchanged is everything at or below the cut: M1 through M4, and M7.) The
   closed form was compared against the loop on the below-cut population
   only; above the cut 6792 pairs have their own y inside W (the parent's
   control 2) and this file did not put the prediction to them, which is
   where a cheap and much larger test sits. The upper arc has a criterion
   but no ceiling argument, the oddness of the step has no derivation at
   the 544 pairs below their ceiling, and the six radices absent from the
   census entirely are a scope statement this cap cannot see past.

VERDICT, by piece.
  - THE MASTER IDENTITY (A) and THE CARRY CLOSED FORM (B) are
    PROPERTIES: derived from the span endpoint and the census filter,
    and checked by their consequences at 11,095 cells and 3516 pairs
    with 0 misses.
  - THE EMPTINESS CRITERION (M2) is a RULE: exhaustive over the
    census's below-cut population in both directions, 3516 of 3516 at
    N <= 60,000 and phase 0. It REPLACES the empty-window PATTERN,
    whose 8 exceptions it accounts for exactly.
  - THE LOWER ARC AT A RIGID CELL (M5) is a PROPERTY, holding for every
    b, h and Delta -- under the two filters that are its hypotheses,
    and with no enumeration.
  - THE STEP CEILING (M3) is a PROPERTY, and so is the biconditional
    that the ceiling is met exactly at the rigid cells: kappa = (b-1)g
    rearranges to (b-1)(1 + e - g) = 2s and e <= g-1 forces both sides
    to vanish, so the 3516 of 3516 is the check and not the ground.
    WHERE the census sits -- 2972 rigid of 3516, radices 4, 6 and 10 --
    is the census reading. The step's ODDNESS is an OBSERVATION.
  - THE VACUITY AT CEILING 1 (M7) is a PROPERTY: h = b-1 forces
    step = 1 and S = [0, b^Delta), checked at 1,763,726 pairs with 0
    misses. It is what makes the dichotomy's radix census a law rather
    than a sample.
  - THE UPPER ARC's emptiness is a RULE at this scope with a measured
    margin, and no derivation.

RUN RECORD: pure Python, integers only, standard library;
explore_slope_lattice.py's interval and repunit, explore_slope_empty.py's
pair_y and pair_report, and explore_slope_window.py's walk, window and
attainable_in_window imported rather than copied, so the census walked
and the window counted are the ones that file measured. 112.6 s wall,
peak working set 35.2 MB against the 512 MB analysis ceiling
(memwatch.py); the census is solved_cells at N <= 60,000, phase 0,
below-count >= 3, walked four times -- once per full-cap pass, since
none of them holds the census in memory -- plus three reduced walks at
N <= 20,000 for the filter sweep. Prints reproduced by:
python prime/code/explore_slope_step.py
"""

import os
import sys
import time
from math import gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_slope_lattice import interval, repunit  # noqa: E402
from explore_slope_empty import pair_y, pair_report  # noqa: E402
from explore_slope_window import (  # noqa: E402
    LOOP_CAP, MU_CUT, attainable_in_window, in_window, walk, window,
)

FAILURES = []


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


def kappa_of(b, a, N, u):
    """(A): kappa = (b-1)N - 2a(N-u), the residue of 2a.u mod N."""
    return (b - 1) * N - 2 * a * (N - u)


def carry_closed(b, a, N, g, y, kap):
    """(B): C(y) in closed form, pointwise. Caller checks y.kappa < N."""
    tau = (-y * (b - 1)) % (2 * a)
    return (N * tau + y * kap) // (2 * a * g)


def predicted_window_count(b, a, N, g, n, kap, MD, Mj, bd):
    """(D): |Y_Delta cap W| from (B) alone, by tau class.

    Lower arc, y in (2 M_Delta, 2 M_j]: attainable iff
    N.tau + y.kappa < 2a g b^Delta, so within a tau class y is bounded
    ABOVE and the class contributes an initial run.
    Upper arc, y' in [1, 2 M_j - 2 M_Delta] with the coordinate n - y':
    attainable iff N.tau' - y'.kappa < 2a g b^Delta with tau' = 2a - tau,
    so y' is bounded BELOW and the class contributes a final run.
    Returns (count, ok_lower, ok_upper) where the flags record whether
    the closed form's y.kappa < N precondition held on the range used.
    """
    h = gcd(2 * a, b - 1)
    step2 = 2 * a // h
    budget = 2 * a * g * bd
    lo_lim, hi_lim = 2 * MD + 1, 2 * Mj
    up_lim = 2 * Mj - 2 * MD
    cnt = 0
    # the closed form needs y.kappa < N over the RANGE it decides, not
    # merely at the points it counts: checked at the largest y of each
    # arc, since a check at the smallest could pass for the wrong reason
    fine_lo = hi_lim * kap < N
    fine_up = up_lim * kap < N
    for tau in range(0, 2 * a, h):
        # the y with (-y(b-1)) mod 2a == tau form one class mod step2
        y0 = None
        for y in range(1, step2 + 1):
            if (-y * (b - 1)) % (2 * a) == tau:
                y0 = y % step2
                break
        if y0 is None:
            continue
        # ---- lower arc: N.tau + y.kappa < budget
        if kap > 0:
            ybound = (budget - N * tau - 1) // kap if budget > N * tau else -1
        else:
            ybound = hi_lim if N * tau < budget else -1
        hi = min(hi_lim, ybound)
        if hi >= lo_lim:
            first = lo_lim + ((y0 - lo_lim) % step2)
            if first <= hi:
                cnt += (hi - first) // step2 + 1
        # ---- upper arc: N.tau' - y'.kappa < budget, tau' = 2a - tau
        taup = 2 * a - tau
        if kap > 0:
            need = (N * taup - budget) // kap + 1 if N * taup > budget else 1
        else:
            need = 1 if N * taup < budget else up_lim + 1
        lo = max(1, need)
        if lo <= up_lim:
            # y' in this class: (-y'(b-1)) mod 2a == tau
            first = lo + ((y0 - lo) % step2)
            if first <= up_lim:
                cnt += (up_lim - first) // step2 + 1
    return cnt, fine_lo, fine_up


def measured_S(n, sigma_inv, bd, cont_hi):
    """The containing carries in the C coordinate, by the parent's loop
    SHAPE re-implemented here rather than imported -- the parent's own
    S loop is inside a print pass and has no callable form.
    Returns the list of C with y_C <= 2 M_Delta."""
    S = []
    y = 0
    for c in range(bd):
        if y <= cont_hi:
            S.append(c)
        y += sigma_inv
        if y >= n:
            y -= n
    return S


def run(cap, min_below=3, verbose=True):
    """E-A through E-D in one walk of the census."""
    if verbose:
        print(f"THE CENSUS, N <= {cap}, below-count >= {min_below}, "
              f"phase 0; the cut every population below is read against "
              f"is mu < {MU_CUT}")
    t0 = time.time()
    cells_seen = set()
    bad_id = bad_res = bad_div = bad_deficit = bad_span = 0
    first_bad = None
    pairs = below = 0
    bad_step = 0
    first_bad_step = None
    empty_S = 0
    bad_cnt = 0
    first_bad_cnt = None
    pre_lo = pre_up = 0
    pre_worst = 0.0
    pw_seen = bad_pw = capped = 0
    nonzero_w = 0
    sc_min = None
    steps = {}
    step_ge3 = 0
    ineq_fail = []
    exc = []
    for (N, key, t, b, a, n, sigma, sigma_inv, A, C) in walk(cap,
                                                             min_below):
        pairs += 1
        b, a, c, u, v = key
        g = N // n
        kap = kappa_of(b, a, N, u)
        h = gcd(2 * a, b - 1)
        if key not in cells_seen:
            cells_seen.add(key)
            # E-A the identity, once per cell
            if not (0 <= kap < N):
                bad_res += 1
            if kap != (2 * a * u) % N:
                bad_id += 1
                if first_bad is None:
                    first_bad = (N, key, kap, (2 * a * u) % N)
            d = N - u
            E = (a * d) // (b - 1)
            s = (a * d) % (b - 1)
            if interval(b, a, c, u, v)[2] != 2 * E + 1:
                bad_span += 1
            if kap != (b - 1) * (1 + (N - 2 * E - 1)) - 2 * s:
                bad_deficit += 1
            if kap % (h * g):
                bad_div += 1
        r = pair_report(b, a, n, A, C)
        if r["contained"] or r["mu"] >= MU_CUT:
            continue
        below += 1
        y, _, MD, bd = pair_y(b, a, n, A, C)
        if bd > LOOP_CAP:
            capped += 1
            continue
        Mj = C["M"]
        # E-B the step
        S = measured_S(n, sigma_inv, bd, 2 * MD)
        pred_step = kap // (h * g)
        if len(S) > 1:
            if S[1] != pred_step:
                bad_step += 1
                if first_bad_step is None:
                    first_bad_step = (N, key, t, A["j"], C["j"], S[1],
                                      pred_step)
            steps[min(S[1], 9)] = steps.get(min(S[1], 9), 0) + 1
            if S[1] >= 3:
                step_ge3 += 1
        else:
            empty_S += 1
        # E-C the closed form against the loop
        w = window(n, MD, Mj)
        # (B) POINTWISE, not only through the aggregate count. NOT at
        # the class's own y: that coordinate sits near n/2, so y.kappa
        # < N fails there and the check would run on an empty
        # population -- a control emptied by its own precondition. Over
        # the range the form DECIDES instead, ends first, since the top
        # is where the precondition binds
        ylim = min(2 * Mj, (N - 1) // kap if kap else 2 * Mj)
        probe = list(range(1, min(ylim, 200) + 1))
        probe += [yy for yy in range(max(1, ylim - 199), ylim + 1)]
        for yy in probe:
            pw_seen += 1
            if carry_closed(b, a, N, g, yy, kap) != (sigma * yy) % n:
                bad_pw += 1
        meas = attainable_in_window(n, sigma_inv, bd, w)
        pred, fl, fu = predicted_window_count(b, a, N, g, n, kap, MD,
                                              Mj, bd)
        pre_lo += 0 if fl else 1
        pre_up += 0 if fu else 1
        pre_worst = max(pre_worst, 2 * Mj * kap / N)
        if meas != pred:
            bad_cnt += 1
            if first_bad_cnt is None:
                first_bad_cnt = (N, key, t, A["j"], C["j"], bd, meas,
                                 pred)
        if meas:
            nonzero_w += 1
            dd = N - u
            exc.append((N, key, t, A["j"], C["j"], bd, meas,
                        pred_step, h, repunit(b, C["j"] - A["j"]),
                        N - 2 * ((a * dd) // (b - 1)) - 1, g - 1,
                        (a * dd) % (b - 1)))
        # E-D the inequality, and the hypothesis it rests on: only
        # tau = 0 coordinates are attainable, which needs n.h > 2a.b^Delta
        sc = n * h / (2 * a * bd)
        sc_min = sc if sc_min is None else min(sc_min, sc)
        if len(S) > 1:
            rD = repunit(b, C["j"] - A["j"])
            if (h * rD + 1) * S[1] < bd:
                ineq_fail.append((N, key, t, A["j"], C["j"], bd, meas))
    el = time.time() - t0
    if not verbose:
        return steps
    print(f"E-A  THE IDENTITY, over {len(cells_seen)} cells  "
          f"[{el:.1f} s]")
    print(f"  kappa outside [0, N): {bad_res}")
    print(f"  kappa != 2a.u mod N: {bad_id}"
          + (f"; first {first_bad}" if first_bad else ""))
    print(f"  kappa != (b-1)(1+e) - 2s: {bad_deficit}")
    print(f"  the census span is not 2E + 1: {bad_span}")
    print(f"  h.g does not divide kappa: {bad_div}")
    ok(bad_res == 0, "(A): kappa is a residue mod N")
    ok(bad_id == 0, "(A): kappa = 2a.u mod N")
    ok(bad_deficit == 0, "(A): the span-deficit form of kappa")
    ok(bad_div == 0, "(C): h.g divides kappa")
    print(f"  below-cut pairs dropped by the b^Delta loop cap "
          f"({LOOP_CAP}): {capped} -- printed because a cap that drops "
          f"nothing and says nothing reads the same as no cap")
    print(f"POSITIVE CONTROL  pairs read {pairs}; below-cut population "
          f"{below} (parent: 3516); pairs whose W holds an attainable "
          f"coordinate {nonzero_w} (parent: 8)")
    if FAILURES:
        print("\nK1: the identity failed -- nothing below is read.")
        return steps
    print("E-B  THE STEP, predicted kappa/(h g) against measured")
    print(f"  disagreements: {bad_step}"
          + (f"; first {first_bad_step}" if first_bad_step else ""))
    print(f"  pairs with S = {{0}} only, where the claim is vacuous: "
          f"{empty_S}")
    print(f"  step distribution (9 = nine or more): "
          f"{dict(sorted(steps.items()))}")
    print(f"  K4  step >= 3: {step_ge3} of {sum(steps.values())}")
    print("E-C  THE CLOSED FORM AGAINST THE LOOP")
    print(f"  (B) pointwise over the decided range, both ends: "
          f"{bad_pw} misses over {pw_seen} coordinates")
    ok(bad_pw == 0, "(B): the closed form is the carry, pointwise")
    print(f"  |Y_Delta cap W| disagreements: {bad_cnt}"
          + (f"; first {first_bad_cnt}" if first_bad_cnt else ""))
    print(f"  precondition y.kappa < N violated over the DECIDED range "
          f"at {pre_lo} pairs on the lower arc, {pre_up} on the upper -- "
          f"where it fails the closed form is unjustified and agreed with "
          f"the loop anyway, so it is sufficient and not necessary; "
          f"worst 2 M_j kappa / N = {pre_worst:.4f}")
    ok(bad_step == 0, "K2: the predicted step is the measured step")
    ok(bad_cnt == 0, "K3: the closed form reproduces the window count")
    print("E-D  THE INEQUALITY (h r_Delta + 1) step >= b^Delta")
    print(f"  its hypothesis, that no tau > 0 coordinate is attainable: "
          f"min n.h/(2a b^Delta) = {sc_min:.4f}, which must exceed 1 -- "
          f"and does so by the census's own filters, since a below-count "
          f">= {min_below} forces n > 2a r_{min_below} and the cut forces "
          f"Delta <= {min_below - 1}")
    print(f"  pairs failing it: {len(ineq_fail)}; pairs whose window is "
          f"non-empty: {nonzero_w}")
    same = sorted(x[:5] for x in ineq_fail) == sorted(x[:5] for x in exc)
    print(f"  the two sets are EQUAL: {same}")
    for x in exc[:10]:
        print(f"    N={x[0]} {x[1]} t={x[2]} levels {x[3]},{x[4]}: "
              f"b^Delta={x[5]}, |Y cap W|={x[6]}, step={x[7]}, h={x[8]},"
              f" r_Delta={x[9]}; NOT rigid: e={x[10]} against "
              f"g-1={x[11]}, s={x[12]}")
    return steps


def e_f_ceiling(cap, min_below=3):
    """E-F, frozen after E-A..E-E printed and before this pass was
    written, because two things in that output are not explained by
    kappa/(h g) alone.

    First, kappa = (b - 1)(1 + e) - 2s with the census's own rigidity
    0 < e < g and s >= 0 gives kappa <= (b - 1) g, hence

        step <= (b - 1) / h,

    with equality exactly when e = g - 1 AND s = 0 -- which is the
    rigid corner, the D = g - 1 the mismatch condition forces wherever
    rho = 2a/(b - 1) is an integer, together with the exactness that
    reading's own qualifier asks for. So the step has a CEILING set by
    the radix and the digit set, and the question "why 3" splits in two:
    why the ceiling is 3, and whether the census sits at it.

    Second, the printed steps are 3, 5, 7 and 9 and never 1, 2, 4, 6 or
    8. Odd values only. If the census sits at the ceiling and every b
    below the cut is even, both facts have the same one-line cause and
    neither is about the carry at all.

    So: the joint distribution of (b, h, step) over the below-cut
    population, the fraction sitting at the ceiling, whether the
    non-ceiling pairs are exactly the non-rigid cells, and the radix
    census. Predictions, fixed here: the ceiling is met at nearly every
    pair; the residual cell (6, 3, 5, 9088, 7) is one of the misses,
    having e = 19 against g - 1 = 31 and s = 2, so its step is 3 where
    its ceiling is 5; and every b below the cut is even."""
    print(f"E-F  THE CEILING (b-1)/h, N <= {cap}")
    t0 = time.time()
    joint = {}
    at_ceil = rigid = tot = 0
    radix = {}
    ceil_rigid_same = 0
    odd = 0
    for (N, key, t, b, a, n, sigma, sigma_inv, A, C) in walk(cap,
                                                             min_below):
        r = pair_report(b, a, n, A, C)
        if r["contained"] or r["mu"] >= MU_CUT:
            continue
        b, a, c, u, v = key
        g = N // n
        kap = kappa_of(b, a, N, u)
        h = gcd(2 * a, b - 1)
        step = kap // (h * g)
        tot += 1
        radix[b] = radix.get(b, 0) + 1
        D = C["j"] - A["j"]
        joint[(b, h, step, D)] = joint.get((b, h, step, D), 0) + 1
        ceil_ = (b - 1) // h
        d = N - u
        s = (a * d) % (b - 1)
        e = N - (2 * ((a * d) // (b - 1)) + 1)
        is_r = (e == g - 1 and s == 0)
        at_ceil += step == ceil_
        rigid += is_r
        ceil_rigid_same += (step == ceil_) == is_r
        odd += step % 2
    print(f"  population {tot}  [{time.time() - t0:.1f} s]")
    print(f"  (b, h, step, Delta) joint -- Delta is what splits the "
          f"below-ceiling pairs into the tight and the failing: "
          f"{dict(sorted(joint.items()))}")
    print(f"  radix census below the cut: {dict(sorted(radix.items()))}")
    print(f"  step = (b-1)/h, the ceiling: {at_ceil} of {tot}")
    print(f"  the cell is rigid (e = g-1 and s = 0): {rigid} of {tot}")
    print(f"  ceiling met IFF rigid: {ceil_rigid_same} of {tot}")
    print(f"  step odd: {odd} of {tot}")


def e_g_arcs(cap, min_below=3):
    """E-G, frozen after E-F printed and before this pass was written.

    E-C compared a TOTAL against a total, and the window is two arcs
    (explore_slope_window.py's (S)): a total agreeing pair by pair does
    not say the two halves agree, and the handoff's own watch says the
    upper arc is the tighter of the two. Worse, E-F hands the lower arc
    a proof and leaves the upper one with nothing: at a rigid cell
    step = (b - 1)/h, so

        (h r_Delta + 1) step  =  r_Delta (b - 1) + (b - 1)/h
                              =  b^Delta - 1 + (b - 1)/h  >=  b^Delta,

    with margin exactly step - 1 -- the lower arc is empty at every
    rigid cell, at every Delta, with no census in the argument. That
    makes the upper arc the whole remaining question, and it needs its
    own margin.

    So: split the predicted count by arc, and report the upper arc's
    clearance in the CARRY coordinate -- (N tau' - y' kappa)/(2a g b^Delta)
    minimised over the admissible y', which exceeds 1 exactly when the
    arc is empty. This is a different normalisation from the parent's
    E-K hi ratio, which is measured in y against the arc WIDTH, so the
    two numbers are not comparable and the tightest need not agree.
    Prediction: every pair clears, the lower arc carries all 32
    attainable coordinates of the residual, and the upper clearance's
    minimum is well above 1 -- if it is not, the upper arc is the half
    a wider census breaks first."""
    print(f"E-G  THE TWO ARCS SPLIT, N <= {cap}")
    t0 = time.time()
    lo_tot = up_tot = tot = 0
    clear = []
    for (N, key, t, b, a, n, sigma, sigma_inv, A, C) in walk(cap,
                                                             min_below):
        r = pair_report(b, a, n, A, C)
        if r["contained"] or r["mu"] >= MU_CUT:
            continue
        b, a, c, u, v = key
        g = N // n
        kap = kappa_of(b, a, N, u)
        h = gcd(2 * a, b - 1)
        step = kap // (h * g)
        _, _, MD, bd = pair_y(b, a, n, A, C)
        rD = repunit(b, C["j"] - A["j"])
        rj = repunit(b, C["j"])
        tot += 1
        # lower arc: k y* with h r_Delta < k <= h r_j and k step < b^Delta
        lo_tot += sum(1 for k in range(h * rD + 1, h * rj + 1)
                      if k * step < bd)
        # upper arc: the least carry cost over the admissible y'
        up_lim = 2 * C["M"] - 2 * MD
        best = None
        for tau in range(0, 2 * a, h):
            taup = 2 * a - tau
            y0 = next(y % (2 * a // h) for y in range(1, 2 * a // h + 1)
                      if (-y * (b - 1)) % (2 * a) == tau)
            ymax = up_lim - ((up_lim - y0) % (2 * a // h))
            if ymax < 1:
                continue
            cost = N * taup - ymax * kap
            if best is None or cost < best:
                best = cost
        if best is not None:
            up_tot += 1 if best < 2 * a * g * bd else 0
            clear.append(best / (2 * a * g * bd))
    clear.sort()
    print(f"  population {tot}  [{time.time() - t0:.1f} s]")
    print(f"  attainable coordinates in the LOWER arc: {lo_tot}")
    print(f"  pairs with an attainable coordinate in the UPPER arc: "
          f"{up_tot}")
    print(f"  upper clearance (N tau' - y' kappa)/(2a g b^Delta), "
          f"empty iff > 1: min {clear[0]:.4f}, q1 "
          f"{clear[len(clear) // 4]:.4f}, median "
          f"{clear[len(clear) // 2]:.4f}, max {clear[-1]:.4f}")
    print(f"  at or below 1: {sum(1 for x in clear if x <= 1.0)} of "
          f"{len(clear)}")


def e_h_vacuous(cap, min_below=3):
    """E-H, frozen at the close after E-A..E-G printed, because M6 left
    the below-cut radix census -- {4, 6, 10}, even only -- with no
    reason offered, and a census that names three radices out of eleven
    is either a scope statement or a law.

    The derivation is the ceiling read at its floor. h = gcd(2a, b-1)
    divides b-1, and where it EQUALS b-1 the ceiling (b-1)/h is 1, so
    step = 1 and the containing carries are the multiples of 1 up to
    h r_Delta = (b-1) r_Delta = b^Delta - 1 -- which is every carry
    there is. Then S = [0, b^Delta), every pair CONTAINS, and the
    dichotomy has no instance to speak about. b = 2 makes h = 1 = b-1
    always; b = 3 makes h = 2 = b-1 always; b = 4 needs 3 | a.

    So the prediction, fixed here: the radices missing from the
    below-cut census are missing for TWO different reasons and M6
    conflated them. b = 2 and b = 3 are present in the
    census in force and carry NO non-contained pair at all, by the
    argument above; the rest (5, 7, 8, 9, 11, 12) are absent from the
    census outright at this cap, which is scope and nothing else.
    Report the radix census at all three stages -- every pair,
    non-contained, below the cut -- with the ceiling beside it, and
    check at every b <= 3 pair that S covers every carry."""
    print(f"E-H  WHERE THE DICHOTOMY HAS NO INSTANCE, N <= {cap}")
    t0 = time.time()
    allr, nc, below, ceil_seen = {}, {}, {}, {}
    bad_cover = small = 0
    for (N, key, t, b, a, n, sigma, sigma_inv, A, C) in walk(cap,
                                                             min_below):
        r = pair_report(b, a, n, A, C)
        allr[b] = allr.get(b, 0) + 1
        if not r["contained"]:
            nc[b] = nc.get(b, 0) + 1
            if r["mu"] < MU_CUT:
                below[b] = below.get(b, 0) + 1
        b, a, c, u, v = key
        g = N // n
        h = gcd(2 * a, b - 1)
        ceil_seen[(b, (b - 1) // h)] = ceil_seen.get((b, (b - 1) // h),
                                                     0) + 1
        if (b - 1) // h == 1:
            small += 1
            step = kappa_of(b, a, N, u) // (h * g)
            D = C["j"] - A["j"]
            if step != 1 or h * repunit(b, D) * step < b ** D - 1:
                bad_cover += 1
    print(f"  radix census, EVERY pair:      "
          f"{dict(sorted(allr.items()))}  [{time.time() - t0:.1f} s]")
    print(f"  radix census, NON-CONTAINED:   {dict(sorted(nc.items()))}")
    print(f"  radix census, BELOW THE CUT:   "
          f"{dict(sorted(below.items()))}")
    print(f"  (b, ceiling) joint: {dict(sorted(ceil_seen.items()))}")
    print(f"  pairs at ceiling 1: {small}; of those, pairs where the "
          f"step is not 1 or S misses a carry: {bad_cover}")
    ok(bad_cover == 0, "ceiling 1 => S covers every carry")


def e_e_sweep(cap):
    """E-E, frozen with the rest: is the step's 3 the census filter's 3?"""
    print(f"E-E  THE min_below SWEEP, N <= {cap}")
    for mb in (2, 3, 4):
        t0 = time.time()
        st = run(cap, min_below=mb, verbose=False)
        tot = sum(st.values())
        print(f"  below-count >= {mb}: population {tot}, steps "
              f"{dict(sorted(st.items()))}  [{time.time() - t0:.1f} s]")


def main():
    steps = run(60000)
    if FAILURES:
        print(f"\nFAILURES: {len(FAILURES)}")
        return
    e_f_ceiling(60000)
    e_g_arcs(60000)
    e_h_vacuous(60000)
    e_e_sweep(20000)
    print(f"\nall checks passed; below-cut steps "
          f"{dict(sorted(steps.items()))}")


if __name__ == "__main__":
    main()
