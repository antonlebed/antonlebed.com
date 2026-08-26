"""The upper arc's ceiling, the closed form off its census, and where
the step's oddness actually lives.

THE QUESTION. explore_slope_step.py derived the carry's closed form and
read the lower arc's emptiness off it as one inequality between four
small integers, exhaustively over the 3516 below-cut pairs. Its M6 left
three things owed, and all three are answered on paper here before this
engine existed; the engine only checks them.

  1. The closed form carries a PRECONDITION, y.kappa < N, which is not
     free even below the cut -- it fails at 16 of the 3516 and the form
     agreed with the loop there anyway. Above the cut it fails at EVERY
     one of the 6792 pairs whose own y sits inside W, so the parent's
     own larger population could not be tested at all without either
     generalizing the form or reporting the whole of it as excluded.
  2. The upper arc is empty at 3516 of 3516 but by a MEASURED margin,
     1.0556 at the tightest, where the lower arc's margin is structural.
     It has a criterion and no ceiling argument.
  3. The step is ODD at 3516 of 3516 and half of that is derived -- at
     the ceiling (b-1)/h with b even -- leaving 544 below-ceiling pairs
     odd for no reason anyone has given.

Notation is the family's, unchanged, at phase 0: N = v b^c, u = q,
g = gcd(u, N), n = N/g, sigma = u/g a unit of Z/n, C(y) = sigma.y mod n,
r_j the repunit, M_j = a r_j, i = A.j, j = C.j, Delta = j - i,
kappa = (b-1)N - 2a(N-u) = 2a.u - (2a-b+1)N, h = gcd(2a, b-1),
tau(y) = (-y(b-1)) mod 2a, step = kappa/(h g), and the ceiling (b-1)/h.

THE DERIVATION, hand-attacked on paper before a line of engine, and
checked by hand at the residual cell (b, a, c, u, v) = (6, 3, 5, 9088, 7).

(F) THE PRECONDITION IS NOT A CONDITION, IT IS A WRAP COUNT THE FORM CAN
    CARRY ITSELF. Since g.C(y) = u.y mod N,

        2a g C(y) = 2a(u y mod N) = 2a u y - 2a N floor(u y / N),

    so with kappa = 2a u - (2a - b + 1) N the exact identity is
    N.tau*(y) + y.kappa = 2a g C(y) at

        tau*(y) = y(2a - b + 1) - 2a floor(u y / N)
                = 2a frac(u y / N) - y kappa / N,

    which is congruent to -y(b-1) mod 2a and lies in (-y kappa/N, 2a).
    So tau*(y) = tau(y) - 2a m(y) with m(y) >= 0 an integer, and
    dividing by 2a g,

        C(y) = [ (N tau(y) + y kappa) / (2a g) ]  mod n,
        m(y) = floor( (N tau(y) + y kappa) / (2a N) ),

    exact for EVERY y with no side condition at all: the division is
    exact because tau supplies the wrap, and the reduction mod n
    supplies the wraps tau alone cannot. The parent's y.kappa < N is the
    m = 0 case and it is loose by a factor of h, since m = 0 iff
    y kappa < N(2a - tau(y)) and tau <= 2a - h, so

        y.kappa < h.N   suffices,

    with the binding class the one at tau = 2a - h.

(G) AND THEN THE WINDOW COUNT IS A FLOOR-SUM, NOT A LOOP. Within a tau
    class the coordinates are y = y_0 + k.alpha, alpha = 2a/h, and
    adding alpha adds alpha.kappa/(2a g) = step to the carry, so along a
    class C runs as (A + k.step) mod n -- an arithmetic progression in
    Z/n, where under m = 0 it was an increasing run. So each arc of W
    contributes, per class, a count of k in an interval with
    (A + k step) mod n < b^Delta, which is a floor-sum and costs
    O(log n) rather than O(b^Delta). The whole count is
    O((2a/h) log n) and is defined wherever the census is, including
    where b^Delta puts the parent's loop out of reach.

(H) THE UPPER ARC'S CEILING. Its cost is N.tau' - y'.kappa over the
    admissible y' in [1, 2a(r_j - r_Delta)], tau' = 2a - tau, and the
    arc is empty iff every cost is >= 2a g b^Delta. Stepping tau' up by
    h costs N.h and buys back at most alpha.kappa = 2a g step; and
    N h = n g h > 2a b^Delta g >= 2a g b > 2a g step, using the lower
    arc's own hypothesis n h > 2a b^Delta and step <= (b-1)/h <= b - 1.
    So the minimum sits at tau' = h -- a PROPERTY, where (D) asserted
    it. That class is y(b-1) = h mod 2a, i.e. with b - 1 = h.beta and
    2a = h.alpha,

        y = beta^{-1} mod alpha,   beta = (b-1)/h = THE STEP'S CEILING,

    so the tightest coordinate is indexed by the same ceiling the lower
    arc's margin is. Writing y_max for the largest admissible y' in that
    class, the upper arc is empty iff

        n.h  >=  2a b^Delta + h.step.y_max,

    the lower arc's hypothesis with a second term paid to the level
    difference. At a rigid cell h.step = b - 1, and where the class
    reaches the top of the arc, y_max = 2a(r_j - r_Delta), this reads

        n.h  >=  2a b^j,

    the hypothesis with j in place of Delta -- and in clearance form,
    n h/(2a b^Delta) - b^i + 1, where the lower arc's own hypothesis is
    the first term alone. That is the ceiling argument the upper arc
    lacked, and it also says the arc is NOT protected by the census
    filters the way the lower one is: mu < 0.4 gives
    n > 10a r_j - 5a r_Delta + 2.5, which at b = 6 falls short of the
    2a b^j = 10a r_j + 2a the criterion asks for. So a failing cell
    should exist, and it should sit ABOVE the cut -- the same population
    (1) needs.

(I) THE STEP'S PARITY IS THE MODULUS'S, AND IS NOT ABOUT THE STEP.
    Dividing kappa = 2a u - (2a - b + 1) N by g,

        h.step = 2a.sigma_0 - (2a - b + 1).n,   sigma_0 = u/g,

    and for b EVEN the multiplier 2a - b + 1 is odd while h divides the
    odd b - 1, so reading mod 2 kills the first term and leaves

        step  =  n   (mod 2).

    The census's radices are {4, 6, 10}, all even, so across it the step
    is odd exactly where the modulus is odd -- the 544 below-ceiling
    pairs included, with no separate account owed. What is left is a
    question about n and not about the carry.

THE DESIGN, frozen before the engine.

E-A THE GENERALIZED FORM, POINTWISE, as a control over both target
    populations: carry_gen against sigma.y mod n at a spread of y across
    [1, n), including both ends of the range. Report the misses, and
    separately the count of probes with m(y) >= 1 -- the population the
    parent's form could not reach, which must be non-empty or the
    generalization is untested. Report also how many pairs fail
    y.kappa < N and how many fail the sharpened y.kappa < h N over the
    arcs, which is what the sharpening is worth.

E-B THE COUNT AGAINST THE LOOP, ON BOTH POPULATIONS. Below the cut, the
    3516 the parent decided; above it, the 6792 whose own y is in W and
    whose b^Delta is inside the control cap. Two computations sharing no
    code path -- one walks b^Delta carries, the other reads at most 2a/h
    floor-sums -- and the second must also SPLIT the count by arc, which
    is what (H) is scored against.

E-C THE UPPER ARC. The O(1) criterion of (H) against the arc-split count
    of E-B, pair by pair, over every non-contained pair the walk sees;
    and the clearance n h/(2a b^Delta) - b^i + 1 against the measured
    minimum cost at the rigid cells. Then the hunt: the pairs whose
    upper arc is NON-EMPTY, with mu and the cell printed, since (H)
    predicts they exist above the cut.

E-D THE PARITY. step = n mod 2 at every pair, and the joint of (n odd,
    step odd, at the ceiling) over the below-cut population -- which
    must show the 544 below-ceiling pairs carried by n's parity alone.

KILLS, frozen as what this rig PRINTS.

K1 carry_gen misses the true carry at any probed y -> (F) is wrong and
   nothing below is read.
K2 no probe has m(y) >= 1 -> the generalization is untested by this rig
   and E-B's agreement says nothing new about it.
K3 the floor-sum count differs from the loop count at any pair of either
   population -> (G) is wrong; below the cut that also retracts M2.
K4 the (H) criterion disagrees with the arc-split upper count at any
   pair where the precondition holds -> (H) is wrong.
K5 tau' = h is not the argmin of the upper cost at some pair -> (H)'s
   property claim is wrong even where its criterion happens to agree.
K6 step != n mod 2 at any pair -> (I) is wrong.

POSITIVE CONTROL, run and read before any verdict line: the parent's
headline reproduced through this file's own walk -- the below-cut
population, the count of pairs whose window holds an attainable
coordinate, and the size of the own-y-in-W population, which must print
3516, 8 and 6792.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

N1 THE PRECONDITION IS GONE, AND THE FORM'S REACH IS THE WHOLE MODULUS.
   carry_gen matches the true carry at 1,868,112 of 1,868,112 probed
   coordinates across every non-contained pair, and 379,084 of those probes
   -- one in five -- have m(y) >= 1, so they lie outside the parent form's
   reach entirely: the generalization is exercised, not merely available.
   What was a side condition to be checked per pair is a floor division
   carried inside the formula. The sharpening (F) offers for the m = 0
   case, y.kappa < h.N in place of y.kappa < N, buys NOTHING here: the
   parent's precondition fails over the arc at 7160 of the 10,852 counted
   and the sharpened one fails at the same 7160, because every pair that
   fails has h = 1 -- but that is only 7148 of the 7160, and at the other
   12 the sharpening is not empty, it is too WEAK: h > 1 and 2 M_j.kappa
   clears h.N anyway. The split that matters is 16 of the 3516 below the
   cut against EVERY ONE of the 6792 whose own y is in W. So the factor of
   h is real in the derivation, empty at 99.8% of this census and
   insufficient at the rest, and it is the reduction mod n that does all of
   the work.

N2 AND THE WINDOW COUNT IS A FLOOR-SUM. The count agrees with the
   parent's carry loop at 10,308 of 10,308 pairs of the two populations
   with ZERO disagreements -- the 3516 below the cut, which is M2's
   population re-decided by a second route, and the 6792 above it whose own
   y sits in W, which M6 named as owed and which the parent could not
   reach. (That 10,308 is NOT N5's: the rigid non-contained cells number
   10,308 too, and the two sets differ. The cross-tab prints both --
   non-contained pairs split (below the cut, own y in W, rigid) as 2972/544
   below and 6792/544 above, so this population trades the 544 below-cut
   NON-rigid pairs for 544 above-cut rigid ones whose own y misses W. Two
   unrelated 544s, and the equal totals are arithmetic and not identity.)
   One thing that split does say: every one of the 6792 own-y-in-W pairs is
   RIGID, 6792 of 6792. The two computations share no code path: one walks
   b^Delta carries, the other reads at most 2a/h floor-sums at O(log n)
   each. So the closed form is off its census: it decides pairs the loop is
   priced out of.

N3 THE ARC SPLIT IS A BELOW-THE-CUT OBJECT, AND SAYING "TWO ARCS" ABOVE
   THE CUT IS AN ERROR. W's arcs are disjoint only while
   4 M_j - 2 M_Delta < n, i.e. while mu < 1; at 3996 of the 6792
   above-cut pairs they OVERLAP on the circle, where the parent's
   in_window counts the intersection once and any per-arc sum doubles
   it. This rig's first pass did exactly that and K3 fired at 2820 of
   the 10,308 it then counted -- a number no current run prints, since
   the fix removed it and a later pass widened the population -- the
   first of them exhibited with a count of 46 against a b^Delta of 36,
   impossible for a count of carries and the tell that named the
   cause. A defect of the reading, not of (G), and the
   reason the total is reported over a merged interval and the split
   only where it exists.

N4 THE UPPER ARC HAS ITS CRITERION, AND tau' = h IS A PROPERTY. The
   cost is least at tau' = h at 10,852 of 10,852 non-contained pairs,
   as (H) derives from n h > 2a b^Delta >= 2a step; (D) had asserted
   it. With y_max the largest admissible coordinate of that class,

       the upper arc is empty  iff  n.h  >=  2a b^Delta + h.step.y_max,

   agreeing with the arc-split count at 4668 of 4668 pairs scored -- which
   is 4668 of the 10,852 non-contained pairs this pass counts, and the
   other two parts are the criterion's SCOPE and not a sample: 3996 pairs
   whose arcs overlap, where there is no upper arc to be empty (N3), and
   2188 where the tightest coordinate needs a wrap the criterion is not
   derived over. That last is what this line still owes -- the COUNT
   generalized past m = 0, the CRITERION did not, and redoing (H) over the
   reduced form is the next thing it wants (later paid, and no new form
   was needed: explore_slope_wrap.py proves the same inequality total --
   a wrapping descent deposits a landing carry below the step, itself
   below b^Delta, so every wrapped pair is non-empty while the
   inequality fails of itself). What it is already is the
   ceiling argument the upper arc lacked, in the lower arc's own shape: its
   hypothesis n h > 2a b^Delta -- printed to hold at all 10,852
   non-contained pairs, not only where the census forces it -- with a
   second term paid to the level difference.

N5 BUT THE CLEAN READING IS SUFFICIENT AND NOT THE CRITERION, AND THE
   HALF THAT WOULD MAKE IT EXACT HAS NO POPULATION. At a rigid cell
   h.step = b-1 and up_lim.kappa = 2a g (b^j - b^Delta) exactly, an
   integer identity at all 10,308 RIGID NON-CONTAINED cells -- N2's
   population is a different set of the same size -- so the clearance
   n h/(2a b^Delta) - b^i + 1 is a valid LOWER bound on the measured
   one at all of them, 0 breaks. It is the clearance itself only where
   the tightest class REACHES the top of the arc, and that happens at
   0 cells of this census -- so the exact half of the claim is
   untested here and must be written as a bound. What it costs to be
   clean is measured: over the 2972 rigid below-cut cells the bound
   gives up a clearance of 0.0521 at the least and 0.1875 at the
   median, and the resulting sufficient form n.h >= 2a b^j decides
   2956 of the 2972 while the other 16 have an empty upper arc it
   cannot see -- a different 16 from the precondition's in N1, sharing
   nothing but the number. So the criterion is the y_max form; n h >= 2a b^j is
   the reading that fits in a sentence and it leaves 16 cells behind.
   The below-cut clearance minimum reproduces the parent's 1.0556.

N6 AND THE PREDICTED FAILING CELL EXISTS, JUST ABOVE THE CUT. (H) said
   mu < 0.4 gives n > 10a r_j - 5a r_Delta + 2.5 where the criterion
   asks for 10a r_j + 2a at b = 6, so the upper arc is not protected by
   the census filters the way the lower one is and a failure should sit
   above the cut. It does: 3148 pairs with disjoint arcs have a
   NON-EMPTY upper arc -- counted over EVERY non-contained pair and not
   only the two populations the loop is compared on, since a least mu
   over a subset is not a least mu -- and the least of them sits at
   mu = 0.4597:
   N = 22032, (b, a, c, u, v) = (6, 4, 4, 8272, 17), levels 1 and 3,
   b^Delta = 36, seven attainable coordinates in the upper arc,
   step 5, h = 1, y_max = 285. The cut at 0.4 is 0.0597 below the first
   failure, so the empty-window law is a below-the-cut law and the
   thing that ends it is the upper arc, exactly where M5 said the
   margin was measured rather than structural.

N7 THE STEP'S ODDNESS IS THE MODULUS'S, AND WAS NEVER A FACT ABOUT THE
   STEP. step = n mod 2 at 1,461,524 of 1,461,524 -- every EVEN-radix
   pair of the 1,786,658 walked, which is exactly what (I) covers and
   not the below-cut population. The below-cut joint of (n odd, step odd,
   at the ceiling) is {(True, True, False): 544, (True, True, True):
   2972}: n is odd at every one of the 3516, so the 544 pairs M3 left
   "odd for no reason anyone has given" are odd for the same reason the
   other 2972 are, and the ceiling half of M3's account was never doing
   the work. What is left is a question about the modulus's parity,
   which is a census question and not a carry question -- and the
   corpus's one existing account of it does not reach: the deficit
   law's clause that rho = 2 makes n odd covers 0 of the 3516, integer
   rho above 2 covers another 0, so the whole below-cut population sits
   at FRACTIONAL rho. What does hold is sharper than the parity itself.
   n = N/g is odd exactly when g absorbs every factor of 2 in N, i.e.
   when 2^v2(N) divides u, and the joint (v2(N), v2(u)) over the
   below-cut population is {(4,4): 344, (4,5+): 296, (5,5): 36,
   (5,6+): 44, (6,6): 4, (6,7+): 8, (8,8): 1344, (8,9+): 1440} -- v2(u)
   is never once BELOW v2(N), at either of the two values it takes.
   So the open question is not "why is n odd" but "why does the
   census's u carry every factor of 2 that N does", which is a question
   about the cells and not about the carry at all. The
   oddness did not get explained, it got MOVED -- off the carry, where
   it had two half-reasons, onto the modulus, where it has none and is
   one question instead of two. (Settled by explore_slope_parity.py:
   n is odd at every cell the census forms, by property at even radix
   -- the census's gcd(u, v) = 1 puts g | b^c, an even n puts N/2 = 0
   (mod g) inside the unsaturated block, and the class map's terminal
   class is then unsaturated -- so the below-count and the measure cut
   enter nowhere.)

VERDICT, by piece.
  - THE GENERALIZED CLOSED FORM (F) is a PROPERTY: derived from
    g C(y) = u y mod N in three lines, and checked at 1,868,112
    coordinates with 0 misses, one in five of them outside the parent
    form's reach.
  - THE FLOOR-SUM COUNT (G) is a PROPERTY with a RULE's check:
    10,308 of 10,308 pairs against an independent loop, over both the
    below-cut population and the larger one above it.
  - tau' = h AS THE ARGMIN (N4) is a PROPERTY, derived and checked at
    10,852 pairs -- and its derivation's hypothesis n.h > 2a b^Delta,
    which the census forces only BELOW the cut, is printed to hold at
    all 10,852 rather than assumed to.
  - THE UPPER-ARC CRITERION (N4) is a RULE at this scope: exhaustive at
    4668 of 4668 pairs scored, N <= 60,000 and phase 0 -- with the
    scope stated, since 4668 is of 10,852 and the rest are excluded by
    overlap and by the wrap, not sampled away.
  - THE RIGID-CELL CLEARANCE BOUND (N5) is a PROPERTY as a BOUND. Its
    equality case is UNTESTED -- zero population -- and n h >= 2a b^j
    is an OBSERVATION about what the bound decides, holding at 2956 of
    2972.
  - THE STEP'S PARITY (N7) is a PROPERTY: two lines of algebra at an
    even radix, checked at the 1,461,524 even-radix pairs of the
    census with 0 misses -- the odd radices are outside the claim, not
    inside it passing. It replaces M3's OBSERVATION.
  - THE FIRST UPPER-ARC FAILURE (N6) is an OBSERVATION: one located
    cell at mu = 0.4597, at this cap.

RUN RECORD: pure Python, integers only, standard library;
explore_slope_lattice.py's repunit, explore_slope_empty.py's pair_y and
pair_report, explore_slope_step.py's kappa_of and explore_slope_window.py's
walk, window, in_window and attainable_in_window imported rather than
copied, so the census walked, the window built and the loop compared
against are the ones those files measured. 25.6 s wall, peak working set
34.9 MB against the 512 MB analysis ceiling (memwatch.py), re-measured
after the audit rounds that added counters rather than carried over;
the census is solved_cells at N <= 60,000, phase 0, below-count >= 3,
walked ONCE --
every pass shares the walk, which is what buys the whole rig for a
quarter of the parent's wall time. Prints reproduced by:
python prime/code/explore_slope_arc.py
"""

import os
import sys
import time
from math import gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_slope_lattice import repunit  # noqa: E402
from explore_slope_empty import pair_y, pair_report  # noqa: E402
from explore_slope_step import kappa_of  # noqa: E402
from explore_slope_window import (  # noqa: E402
    CTRL_CAP, MU_CUT, attainable_in_window, in_window, walk, window,
)

FAILURES = []


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


# ------------------------------------------------ (F) and (G), the tools

def carry_gen(b, a, N, g, n, y, kap):
    """(F): C(y) for EVERY y, the wrap reduced explicitly."""
    tau = (-y * (b - 1)) % (2 * a)
    return ((N * tau + y * kap) // (2 * a * g)) % n


def wraps(b, a, N, y, kap):
    """(F): m(y), the wraps tau alone does not carry."""
    tau = (-y * (b - 1)) % (2 * a)
    return (N * tau + y * kap) // (2 * a * N)


def floor_sum(k, m, s, c):
    """sum_{t=0}^{k-1} floor((s t + c)/m), for s, c >= 0 and m > 0."""
    ans = 0
    while True:
        if s >= m:
            ans += (k - 1) * k // 2 * (s // m)
            s %= m
        if c >= m:
            ans += k * (c // m)
            c %= m
        top = s * k + c
        if top < m:
            return ans
        k = top // m
        c = top % m
        m, s = s, m


def count_prog(k, A, step, n, T):
    """#{t in [0, k) : (A + t.step) mod n < T}, by (G)'s floor-sum."""
    if k <= 0:
        return 0
    if T >= n:
        return k
    if T <= 0:
        return 0
    s = step % n
    if s == 0:
        return k if A < T else 0
    return k - (floor_sum(k, n, s, A + n - T) - floor_sum(k, n, s, A))


def class_reps(b, a, h):
    """(y_0, tau) for each tau class, y_0 the least positive coordinate
    with tau(y_0) = tau, reduced mod alpha = 2a/h."""
    alpha = 2 * a // h
    out = []
    for tau in range(0, 2 * a, h):
        for y in range(1, alpha + 1):
            if (-y * (b - 1)) % (2 * a) == tau:
                out.append((y % alpha, tau))
                break
    return out


def count_arcs(b, a, N, g, n, kap, MD, Mj, bd, h, step):
    """(G): |Y_Delta cap W| by floor-sum, with no precondition, split by
    arc where the split exists. Returns (total, lower, upper, disjoint).

    W's two arcs are disjoint only while 4 M_j - 2 M_Delta < n, i.e.
    while mu < 1: above that they overlap on the circle and in_window's
    OR counts the intersection once, so a per-arc sum would double it.
    Where they overlap only the TOTAL is defined, over the merged
    interval, and disjoint is False -- the arc split is a below-the-cut
    object and the flag is what says so. Both ends are clamped to
    [0, n), which is in_window's own reading of them."""
    alpha = 2 * a // h
    lo1, hi1 = max(0, 2 * MD + 1), min(n - 1, 2 * Mj)
    lo2, hi2 = max(0, n - 2 * Mj + 2 * MD), n - 1
    a1, a2 = (lo1 <= hi1), (lo2 <= hi2)
    disjoint = not (a1 and a2) or hi1 < lo2
    if not disjoint:
        spans = [(min(lo1, lo2), max(hi1, hi2), 0)]
    else:
        spans = ([(lo1, hi1, 0)] if a1 else []) \
            + ([(lo2, hi2, 1)] if a2 else [])
    tot = low = up = 0
    for y0, _tau in class_reps(b, a, h):
        for (lo, hi, which) in spans:
            if hi < lo:
                continue
            first = lo + ((y0 - lo) % alpha)
            if first > hi:
                continue
            k = (hi - first) // alpha + 1
            A = carry_gen(b, a, N, g, n, first, kap)
            c = count_prog(k, A, step, n, bd)
            tot += c
            if which:
                up += c
            else:
                low += c
    if not disjoint:
        low = up = None
    return tot, low, up, disjoint


# ------------------------------------------------------- (H), the ceiling

def upper_ymax(b, a, h, up_lim):
    """(H): the largest admissible y' in the tightest class tau' = h,
    which is y = beta^{-1} mod alpha with beta the step's ceiling."""
    alpha = 2 * a // h
    beta = (b - 1) // h
    y0 = pow(beta % alpha, -1, alpha) if alpha > 1 else 0
    if up_lim < 1:
        return None
    ymax = up_lim - ((up_lim - y0) % alpha)
    return ymax if ymax >= 1 else None


def upper_empty(b, a, n, h, step, bd, up_lim):
    """(H): n.h >= 2a b^Delta + h.step.y_max, the criterion."""
    ymax = upper_ymax(b, a, h, up_lim)
    if ymax is None:
        return True, None
    return n * h >= 2 * a * bd + h * step * ymax, ymax


def upper_cost_argmin(b, a, N, kap, h, up_lim):
    """(H)'s property: the least cost N.tau' - y'.kappa over all classes,
    returned with the tau' that achieves it."""
    alpha = 2 * a // h
    best = None
    for y0, tau in class_reps(b, a, h):
        taup = 2 * a - tau
        ymax = up_lim - ((up_lim - y0) % alpha)
        if ymax < 1:
            continue
        cost = N * taup - ymax * kap
        if best is None or cost < best[0]:
            best = (cost, taup)
    return best


# ------------------------------------------------------------- the passes

def run(cap, min_below=3):
    """E-A through E-D in one walk of the census."""
    print(f"THE CENSUS, N <= {cap}, below-count >= {min_below}, phase 0; "
          f"the cut every population is read against is mu < {MU_CUT}, "
          f"and the own-y-in-W loop cap is b^Delta <= {CTRL_CAP}")
    t0 = time.time()
    pairs = below = cross = cross_skip = 0
    nonzero_w = 0
    # E-A
    probes = bad_pw = with_wrap = 0
    pre_N = pre_hN = pre_N_h1 = pre_N_below = pre_N_cross = 0
    # E-B
    bad_lo = 0
    first_bad = None
    lo_tot = up_tot = overlapped = 0
    cmp_pop = extra_pop = 0
    # E-C
    bad_crit = 0
    first_bad_crit = 0
    bad_argmin = 0
    crit_seen = crit_scored = 0
    nh_fail = nh_fail_scored = 0
    crit_skip_ovl = crit_skip_pre = 0
    up_nonempty = []
    clear_rigid = []
    bad_clear_eq = bad_clear_bound = rigid_top = 0
    suff_seen = suff_ok = 0
    gaps = []
    # E-D
    bad_par = par_seen = 0
    par_joint = {}
    rho2 = rho_int = 0
    twos = {}
    nc_joint = {}
    for (N, key, t, b, a, n, sigma, sigma_inv, A, C) in walk(cap,
                                                             min_below):
        pairs += 1
        b, a, c, u, v = key
        g = N // n
        kap = kappa_of(b, a, N, u)
        h = gcd(2 * a, b - 1)
        step = kap // (h * g)
        # E-D, over every pair the walk sees
        if b % 2 == 0:
            par_seen += 1
            if (step - n) % 2:
                bad_par += 1
        r = pair_report(b, a, n, A, C)
        y, _, MD, bd = pair_y(b, a, n, A, C)
        Mj = C["M"]
        w = window(n, MD, Mj)
        is_below = (not r["contained"]) and r["mu"] < MU_CUT
        is_cross = in_window(y, w)
        if is_below:
            below += 1
        if is_cross:
            cross += 1
        # the three populations this file reports are different sets
        # that turn out to print equal SIZES, so their cross-tab is
        # printed too rather than left to be inferred from the totals
        if not r["contained"]:
            e_ = N - (2 * ((a * (N - u)) // (b - 1)) + 1)
            s_ = (a * (N - u)) % (b - 1)
            kk = (is_below, is_cross, e_ == g - 1 and s_ == 0)
            nc_joint[kk] = nc_joint.get(kk, 0) + 1
        # E-C's criterion, over every non-contained pair
        if not r["contained"]:
            up_lim = 2 * Mj - 2 * MD
            crit, _ = upper_empty(b, a, n, h, step, bd, up_lim)
            crit_seen += 1
            if n * h <= 2 * a * bd:
                nh_fail += 1
            am = upper_cost_argmin(b, a, N, kap, h, up_lim)
            if am is not None and am[1] != h:
                bad_argmin += 1
            i = A["j"]
            e = N - (2 * ((a * (N - u)) // (b - 1)) + 1)
            s = (a * (N - u)) % (b - 1)
            if e == g - 1 and s == 0 and am is not None:
                # at a rigid cell h.step = b-1, so N h - up_lim.kappa is
                # exactly (2a g b^Delta)(n h/(2a b^Delta) - b^i + 1) --
                # an integer identity, checked as one. It is the cost
                # only where the tightest class REACHES the top of the
                # arc; elsewhere it is a strict lower bound on it
                pred_cost = N * h - up_lim * kap
                if up_lim * kap != 2 * a * g * (b ** C["j"] - bd):
                    bad_clear_eq += 1
                ym = upper_ymax(b, a, h, up_lim)
                if ym == up_lim:
                    rigid_top += 1
                    if am[0] != pred_cost:
                        bad_clear_eq += 1
                elif am[0] < pred_cost:
                    bad_clear_bound += 1
                clear_rigid.append((am[0] / (2 * a * g * bd),
                                    r["mu"] < MU_CUT))
                # and what the CLEAN reading n h >= 2a b^j decides on
                # its own, beside the gap it pays for being clean
                if r["mu"] < MU_CUT:
                    suff_seen += 1
                    if n * h >= 2 * a * b ** C["j"]:
                        suff_ok += 1
                    gaps.append((am[0] - pred_cost) / (2 * a * g * bd))
        # the counted population is EVERY non-contained pair, not just
        # the two the parent named: the least mu with a non-empty upper
        # arc is a minimum, and a minimum over a subset is not one.
        # The LOOP comparison still runs only on the parent's two, which
        # is what "10,308" means wherever it appears
        if r["contained"]:
            continue
        if bd > CTRL_CAP:
            if is_cross:
                cross_skip += 1
            continue
        compared = is_below or is_cross
        if compared:
            cmp_pop += 1
        else:
            extra_pop += 1
        # E-A the pointwise control, over a spread of the whole range
        stride = max(1, (n - 1) // 200)
        pts = list(range(1, n, stride))[:200]
        pts += [n - 1, n - 2, 2 * Mj, max(1, 2 * MD + 1)]
        for yy in pts:
            if yy < 1 or yy >= n:
                continue
            probes += 1
            if wraps(b, a, N, yy, kap) >= 1:
                with_wrap += 1
            if carry_gen(b, a, N, g, n, yy, kap) != (sigma * yy) % n:
                bad_pw += 1
        if 2 * Mj * kap >= N:
            pre_N += 1
            if h == 1:
                pre_N_h1 += 1
            if is_below:
                pre_N_below += 1
            if is_cross:
                pre_N_cross += 1
        if 2 * Mj * kap >= h * N:
            pre_hN += 1
        # E-B the floor-sum count against the loop
        tot, low, up, disj = count_arcs(b, a, N, g, n, kap, MD, Mj, bd,
                                        h, step)
        meas = (attainable_in_window(n, sigma_inv, bd, w, cap=CTRL_CAP)
                if compared else None)
        if not disj:
            overlapped += 1
        else:
            lo_tot += low
            up_tot += up
        if compared and meas != tot:
            bad_lo += 1
            if first_bad is None:
                first_bad = (N, key, t, A["j"], C["j"], bd, meas, tot,
                             disj)
        if is_below and meas:
            nonzero_w += 1
        # E-C the criterion against the arc-split count, where the split
        # exists and the tightest coordinate is inside the form's reach
        up_lim = 2 * Mj - 2 * MD
        crit, ymax = upper_empty(b, a, n, h, step, bd, up_lim)
        if not disj:
            crit_skip_ovl += 1
        elif up_lim * kap >= h * N:
            crit_skip_pre += 1
        if disj and up_lim * kap < h * N:
            crit_scored += 1
            if n * h <= 2 * a * bd:
                nh_fail_scored += 1
            if crit != (up == 0):
                bad_crit += 1
                if not first_bad_crit:
                    first_bad_crit = (N, key, t, A["j"], C["j"], bd, up,
                                      crit)
        if disj and up:
            up_nonempty.append((N, key, t, A["j"], C["j"], bd, up,
                                round(r["mu"], 4), step, h, ymax))
        if is_below:
            ceil_ = (b - 1) // h
            kk = (n % 2 == 1, step % 2 == 1, step == ceil_)
            par_joint[kk] = par_joint.get(kk, 0) + 1
            # what the corpus already has for n's parity is a clause at
            # rho = 2, so how much of this population does it cover
            if 2 * a == 2 * (b - 1):
                rho2 += 1
            elif 2 * a % (b - 1) == 0:
                rho_int += 1
            # n odd means g absorbs every factor of 2 in N, i.e.
            # 2^v2(N) | u -- so the question is about u, not about n
            v2N = (N & -N).bit_length() - 1
            v2u = (u & -u).bit_length() - 1
            twos[(v2N, min(v2u, v2N + 1))] = twos.get(
                (v2N, min(v2u, v2N + 1)), 0) + 1
    el = time.time() - t0
    print(f"POSITIVE CONTROL  pairs read {pairs}; below-cut population "
          f"{below} (parent: 3516); pairs whose W holds an attainable "
          f"coordinate {nonzero_w} (parent: 8); pairs whose own y is in "
          f"W {cross} (parent: 6792), of which {cross_skip} skipped by "
          f"b^Delta > {CTRL_CAP}   [{el:.1f} s]")
    # the control ADJUDICATES rather than merely printing beside the
    # parent's figures: at the census this file is written for, a walk
    # that drifted would otherwise be read past
    if cap == 60000 and min_below == 3:
        ok(below == 3516, "control: the below-cut population is 3516")
        ok(nonzero_w == 8, "control: 8 pairs whose W holds an "
                           "attainable coordinate")
        ok(cross == 6792, "control: 6792 pairs whose own y is in W")
        ok(cross_skip == 0, "control: no own-y-in-W pair skipped")
    print("E-A  THE GENERALIZED FORM, POINTWISE")
    print(f"  misses: {bad_pw} over {probes} coordinates")
    print(f"  probes with m(y) >= 1, out of the parent form's reach: "
          f"{with_wrap}")
    print(f"  pairs where 2 M_j.kappa >= N, the parent's precondition "
          f"failing over the arc: {pre_N} of the {cmp_pop + extra_pop} "
          f"counted -- {pre_N_below} of the {below} below the cut, and "
          f"above it {pre_N_cross} of the {cross} whose own y is in W, "
          f"which is why the old form could not test that population "
          f"at all, out of {pre_N - pre_N_below} above-cut failures "
          f"overall; where it fails the sharpened "
          f"2 M_j.kappa >= h N: {pre_hN}, of which h = 1 at "
          f"{pre_N_h1} -- which is whether the two counts coincide "
          f"because the sharpening is EMPTY here or because it is "
          f"weak")
    ok(bad_pw == 0, "K1 (F): the generalized form is the carry")
    ok(with_wrap > 0, "K2: the generalization is exercised")
    if FAILURES:
        print("\nthe positive control, K1 or K2 failed -- nothing "
              "below is read.")
        return
    print("E-B  THE FLOOR-SUM COUNT AGAINST THE LOOP")
    print(f"  the loop comparison runs on the parent's two "
          f"populations, {cmp_pop} pairs; the count also runs on "
          f"{extra_pop} further non-contained pairs the loop is not "
          f"asked about, so the upper-arc minimum below is over every "
          f"non-contained pair and not a subset")
    print(f"  disagreements: {bad_lo}"
          + (f"; first {first_bad}" if first_bad else ""))
    print(f"  attainable coordinates found over the pairs whose arcs "
          f"are DISJOINT: lower {lo_tot}, upper {up_tot}; pairs whose "
          f"arcs OVERLAP, where only the total is defined: {overlapped}")
    ok(bad_lo == 0, "K3 (G): the floor-sum count reproduces the loop")
    print("E-C  THE UPPER ARC")
    print(f"  criterion n.h >= 2a b^Delta + h.step.y_max against the "
          f"arc-split count: {bad_crit} disagreements over "
          f"{crit_scored} pairs scored, of the {cmp_pop + extra_pop}"
          f" non-contained pairs this pass counts -- {crit_skip_ovl} "
          f"not scored because the arcs overlap and {crit_skip_pre} "
          f"because the tightest "
          f"coordinate needs a wrap the criterion is not derived over, "
          f"which is the criterion's own remaining scope"
          + (f"; first {first_bad_crit}" if first_bad_crit else ""))
    print(f"  tau' = h is NOT the argmin of the cost: {bad_argmin} of "
          f"{crit_seen} non-contained pairs -- of which {nh_fail} do "
          f"NOT satisfy the derivation's own hypothesis n.h > 2a "
          f"b^Delta, so there the agreement is measured and not "
          f"derived ({nh_fail_scored} of the {crit_scored} scored "
          f"for the criterion)")
    ok(bad_crit == 0, "K4 (H): the upper-arc criterion")
    ok(bad_argmin == 0, "K5 (H): the cost is least at tau' = h")
    if clear_rigid:
        cl = sorted(x[0] for x in clear_rigid)
        cb = sorted(x[0] for x in clear_rigid if x[1])
        print(f"  rigid non-contained cells {len(clear_rigid)}: "
              f"clearance min {cl[0]:.4f}, median "
              f"{cl[len(cl) // 2]:.4f}, max {cl[-1]:.4f}")
        if cb:
            print(f"  of those, the {len(cb)} BELOW the cut: min "
                  f"{cb[0]:.4f}, median {cb[len(cb) // 2]:.4f} -- the "
                  f"parent measured 1.0556 at the tightest over all "
                  f"3516, rigid and not")
        print(f"  the clearance closed form n h/(2a b^Delta) - b^i + 1: "
              f"{bad_clear_eq} breaks of the integer identity, "
              f"{bad_clear_bound} cells where it is not a lower bound; "
              f"cells where it is EXACT rather than a bound -- the "
              f"tightest class reaching the top of the arc -- "
              f"{rigid_top}, so that half of the claim has no "
              f"population here and is untested")
        if gaps:
            gs = sorted(gaps)
            print(f"  the clean reading n h >= 2a b^j, over the "
                  f"{suff_seen} rigid below-cut cells: holds at "
                  f"{suff_ok}; the clearance it gives up against the "
                  f"exact criterion is min {gs[0]:.4f}, median "
                  f"{gs[len(gs) // 2]:.4f}, max {gs[-1]:.4f}")
        ok(bad_clear_eq == 0 and bad_clear_bound == 0,
           "(H): the rigid-cell clearance")
    print(f"  pairs with a NON-EMPTY upper arc, disjoint arcs only: "
          f"{len(up_nonempty)}"
          + (f"; least mu among them {min(x[7] for x in up_nonempty)}"
             if up_nonempty else ""))
    for x in sorted(up_nonempty, key=lambda z: z[7])[:10]:
        print(f"    N={x[0]} {x[1]} t={x[2]} levels {x[3]},{x[4]}: "
              f"b^Delta={x[5]}, upper={x[6]}, mu={x[7]}, step={x[8]}, "
              f"h={x[9]}, y_max={x[10]}")
    print("E-D  THE PARITY")
    print(f"  step != n mod 2: {bad_par} of the {par_seen} "
          f"EVEN-radix pairs, which is what the derivation covers, out "
          f"of {pairs} walked")
    ok(bad_par == 0, "K6 (I): step = n mod 2")
    print(f"  below-cut joint (n odd, step odd, at the ceiling): "
          f"{dict(sorted(par_joint.items()))}")
    print(f"  non-contained cross-tab (below the cut, own y in W, "
          f"rigid): {dict(sorted(nc_joint.items()))}")
    print(f"  below-cut (v2(N), v2(u) capped at v2(N)+1): "
          f"{dict(sorted(twos.items()))} -- n is odd iff v2(u) >= v2(N), "
          f"so this is where the modulus's parity is actually decided")
    print(f"  below-cut pairs at rho = 2, where the corpus already has "
          f"n odd: {rho2}; at integer rho above 2: {rho_int}; the rest, "
          f"where n's parity has no account yet: "
          f"{below - rho2 - rho_int}")


def main():
    run(60000)
    if FAILURES:
        print(f"\nFAILURES: {len(FAILURES)}")
        return
    print("\nall checks passed")


if __name__ == "__main__":
    main()
