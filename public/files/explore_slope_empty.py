"""Why does a width-3 family always carry an empty pair? The meeting
test turns out to be the containment test at a second radius.

THE QUESTION. explore_slope_width.py exhibited containment width 3 --
812 classes over 11095 cells -- and the two-level closed form of
explore_slope_assemble.py's (D) survived it only because the term it
has no formula for is empty at 812 of 812. Its I2 located the reason
one level down and named it precisely: of the three PAIRWISE terms
among the three maximal levels, the SHALLOW pair -- the two shallowest
-- is empty at 812 of 812, against 64 for the mid pair and 32 for the
deep, while at width 2 over the same census a pair vanishes at only
128 of 3824. So the load-bearing clause is "the two shallowest maximal
levels never meet", filed as a PATTERN with no proof. This asks what
makes it true, and what it would take to break it.

Notation is the family's: N = L b^c, g = gcd(q, N), n = N/g,
sigma = q/g a unit of Z/n, r_j the repunit, M_j = a r_j, J the least j
with 2 M_j + 1 >= n, and at lam = 1 (forced, explore_slope_width.py's
(F)) the level set is

    B_j = {w in Z/n : (b^j w + d_j) mod n in [-M_j, M_j]}.

THE DERIVATION, hand-attacked on paper before this engine existed.

(P) THE MEETING TEST IS THE CONTAINMENT TEST AT A SECOND RADIUS. Fix
    levels i < j, Delta = j - i, and substitute v = b^i w + d_i, which
    ranges over the coset d_i + kappa_i Z of Z/n, kappa_i = gcd(b^i, n).
    Then b^j w + d_j = b^Delta v + e with e = d_j - b^Delta d_i, so

        B_i cap B_j =/= 0  iff  some v with |v| <= M_i, v = d_i mod
        kappa_i, has b^Delta v + e in [-M_j, M_j] (mod n).

    Two facts make this an interval statement rather than a lattice one.
    r_j = b^Delta r_i + r_Delta gives M_j = b^Delta M_i + M_Delta
    EXACTLY, so the image interval is longer than the source's by
    2 M_Delta; and b^Delta M_i <= M_j < n/2, so b^Delta v never wraps
    and the whole span sits inside (-n, n) -- k in {-1, 0, +1} covers
    every wrap of b^Delta v + e. Writing y = (e + M_Delta) mod n, the
    same coordinate explore_slope_width.py's (H) reads off the class
    orbit's own carry:

        CONTAINMENT   B_i subset B_j   needs  y <= 2 M_Delta,
        MEETING       B_i cap B_j =/= 0 needs y <= 2 M_j  or
                      y >= n - 2 M_j + 2 M_Delta.

    One quantity, two radii: the containment radius is set by the
    DIFFERENCE of the levels and the meeting radius by the DEEPER level
    alone. Both are NECESSARY conditions read off an interval; the first
    is also sufficient (that is (E)'s forward half, a property), the
    second is not, since v is discrete with step b^Delta. So the exact
    meeting test is the same statement with the integers put back: for
    each k, intersect [ceil((-M_j + kn - e)/b^Delta),
    floor((M_j + kn - e)/b^Delta)] with [-M_i, M_i] and ask for a
    member congruent to d_i mod kappa_i.

(Q) THE MEETING MEASURE, and why the SHALLOW pair. The y admitted by
    (P) number 4 M_j - 2 M_Delta + 1 of the n available, so the pair's
    meeting measure is mu = (4 M_j - 2 M_Delta + 1) / n -- a number
    attached to the pair before any y is looked at, and an upper bound
    on how often the pair can meet. Once that count reaches n the two
    arcs have overlapped and it double-reads the circle, so mu is
    CLAMPED at 1 wherever it is reported: it is a fraction, not a
    tally. It is a function of the DEEPER
    level, and that is what singles out the shallow pair: at a width-3
    class with maximal levels i1 < i2 < i3, level i3 is a level, so
    2 M_i3 + 1 <= n; and M_i3 = b^(i3-i2) M_i2 + M_(i3-i2) >
    b^(i3-i2) M_i2. Hence

        2 M_i2 < n / b^(i3 - i2)   and   mu_shallow < 2 / b^(i3 - i2).

    The third maximal level buys the shallow pair a factor of b. At
    width 2 there is no third level to buy it: the deeper level may sit
    at J - 1, where 2 M_j + 1 <= n is the only bound and the admitted
    count reaches the whole circle. That is the asymmetry the 812-of-812 against 128-of-3824 should
    be made of, and it is a DERIVED cap rather than a law -- a cap is
    not a proof that no y lands inside it, so the honest reading of a
    perfect column is a bound plus a residual, and the residual is what
    a wider census puts to the question.

THE DESIGN, frozen before the engine.

E-A THE CONTROLS, four, run and read before any verdict.
    (1) EXACT WIDTH WITHOUT SETS. Containment is |B_i cap B_j| =
        |B_i| and meeting is |B_i cap B_j| > 0, both from the parent's
        own count_single/count_pair floor-sums, so a width costs
        O(width^2) counts rather than an n-sized set. That measurement
        must equal explore_slope_width.py's set-based measured_width at
        every class of the control census, and the per-pair containment
        and meeting verdicts must equal direct set containment and
        direct set intersection, both directions.
    (2) (P)'s exact interval test against count_pair > 0 at every pair
        of every census -- two computations sharing nothing, one
        interval arithmetic and one floor-sum, so agreement is a real
        control and not a restatement.
    (3) (P)'s MEETING arc is necessary and cannot fail without the
        derivation being wrong: no pair may meet with y outside the two
        arcs. That is the half this file adds and the only half
        asserted. Its containment sibling -- "contained implies
        y <= 2 M_Delta" -- is NOT a control here and must not be
        written as one: it is the criterion's CONVERSE, which
        explore_slope_width.py's I3 falsified at 284 pairs, and its
        forward direction (y <= 2 M_Delta implies containment) is the
        property I3 leaves standing. So the converse is COUNTED beside
        the control and never asserted; a control census small enough
        to read 0 for it is reading its own scope.
    (4) THE PARENT'S HEADLINE reproduced through this file's own path:
        the width distribution at N <= 60000 and the which-pair census
        {shallow: 812, mid: 64, deep: 32}. A mechanism explained
        against numbers this file did not reproduce is a mechanism for
        somebody else's census.

E-B HOW THE SHALLOW PAIR IS EMPTY. At every width-3 class, classify the
    shallow pair's emptiness: BY REACH (y outside both arcs of (P), so
    the interval bound alone settles it) or BY DISCRETENESS (y inside an
    arc, no admissible v). The two are different laws and only the first
    is what (Q) bounds. Same for the mid and deep pairs, whose empty
    counts of 64 and 32 are the internal control on the split.

E-C THE MEETING MEASURE MEASURED. Report the distribution of mu over
    the shallow, mid and deep pairs of the width-3 population and over
    the width-2 population's single pair, with the max and the median
    of each, beside the observed empty fractions. Check (Q)'s cap
    mu_shallow < 2 / b^(i3-i2) at every width-3 class. If the shallow
    mu is small where the width-2 mu is large, the asymmetry is
    explained by the cap and the perfect column is a residual; if the
    shallow mu is often near its cap and the column is still perfect,
    the cap is not the mechanism and something forces y.

E-D THE RESIDUAL PUT TO THE QUESTION. Push the width-3 census past the
    parent's N <= 60000 with the cheap width of (1), and ask the two
    questions a residual owes: does any width-3 class have its shallow
    pair MEET, and does any have all three pairs non-empty -- the
    second being the one that would make the parent's (D) return a
    wrong number rather than an unjustified one. Report the largest
    mu_shallow found and the class carrying it, since that is where the
    residual is largest and where the next census should aim.

KILLS, frozen as what this rig PRINTS.

K1 A control of E-A misses -> the cheap width, (P), or the reproduction
   is wrong and nothing below is read.
K2 A width-3 class whose SHALLOW pair meets -> "the two shallowest
   maximal levels never meet" is FALSE, and what survives is (Q)'s cap.
K3 A width-3 class with all three pairs non-empty -> the triple term is
   owed and the parent's (D) is WRONG there, not merely unjustified.
   K2 is necessary for K3 and not sufficient: a triple can still be
   empty with three non-empty pairs, so the triple is measured at any
   such class before anything is claimed.
K4 mu_shallow at or above 1 -> (Q)'s cap is wrong, since the cap says
   the shallow pair cannot even reach half the circle once a third
   maximal level exists. AS FIRST FROZEN this kill said "mu at or above
   1 ANYWHERE", which is not a claim (Q) makes: (Q) bounds the SHALLOW
   pair, whose deeper level has a third maximal level under it, and says
   nothing about the mid and deep pairs, whose deeper level is i3 with
   nothing under it. It fired at once on exactly those, and the scope is
   corrected here rather than the finding written around it -- a mid or
   deep mu at 1 is what the derivation PREDICTS.
K5 A shallow pair empty BY DISCRETENESS -> (Q) does not bound the
   phenomenon and the interval reading is the wrong frame for it.

POSITIVE CONTROL, run and read before any verdict line: E-A whole.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

J1 THE MEETING TEST IS THE CONTAINMENT TEST AT A SECOND RADIUS. (P)
   holds as derived. Its exact interval form agrees with the parent's
   floor-sum count_pair at 3766 of 3766 pairs of the control census,
   two computations sharing nothing; the count-based width agrees with
   explore_slope_width.py's set-based one at 2346 of 2346 classes and
   the per-pair size, containment and meeting verdicts with direct sets
   at all 3766; and (P)'s MEETING arc -- no pair meets with y outside
   it -- is violated at 0 of 1,786,658 pairs of the wide census. Its
   containment sibling is NOT a control and is counted rather than
   asserted, because it is the criterion's converse: measured
   containments with y > 2 M_Delta number 284 over the same census,
   which is explore_slope_width.py's I3 reproduced independently in
   this coordinate. Reading 0 for it, as the N <= 3000 control census
   does, is reading a scope and not a law. So the level
   order and the level MEETINGS are one coordinate read at two radii:
   2 M_Delta, set by the level difference, and 2 M_j, set by the deeper
   level alone. The containment radius was already the parent's (H);
   the meeting radius is what this file adds, and it is what makes a
   pair's fate legible before its y is looked at.

J2 THE THIRD MAXIMAL LEVEL CAPS THE SHALLOW PAIR, AND THAT IS WHY IT IS
   THE SHALLOW PAIR. (Q)'s cap mu_shallow < 2/b^(i3-i2) is violated at
   0 of 812 and 0 of 4844 over the two censuses, with the largest
   mu_shallow 0.4118 at N = 56576, (b, a, c, u, v) = (4, 5, 4, 39680,
   221), class 21, against its own cap of 0.5 -- and that same class
   remains the largest when the census is pushed 2.5x, so the cap binds
   near 0.41 rather than at its stated 2/b. The asymmetry the parent
   reported is exactly this: the width-3 shallow pair has a median mu
   of 0.178 while the width-2 population's single pair, with no third
   level to buy it a factor of b, has a median of 0.892 and a max of 1.
   The cap is a PROPERTY, derived from 2 M_i3 + 1 <= n and
   M_i3 > b^(i3-i2) M_i2 and checked rather than evidenced.

J3 THE LAW IS NOT ABOUT WIDTH 3 -- IT IS A DICHOTOMY AT A MEASURE, AND
   THAT IS THE REAL FIND. Bucketing every pair of the N <= 60,000
   census by its own mu and reading the meeting rate against it (E-F)
   gives, for the NON-CONTAINED pairs, 0.0000 at every bucket below
   mu = 0.4 -- 3516 of 3516 -- then 0.0556, 0.2500, 0.4918, 0.9500, 1.0000, 0.9992. So
   beneath that measure a pair CONTAINS or MISSES and there is no
   middle, and width 3 enters only through J2. The buckets do not
   locate the threshold, so it is measured directly rather than read
   off them: the SMALLEST mu at which any non-contained pair of the
   census is observed to meet is 0.4733, at N = 42768,
   (b, a, c, u, v) = (6, 8, 4, 29408, 33), class 1, levels 1 and 3.
   THAT is the number the composition turns on, and AT THIS CENSUS it
   closes: 0.4118 < 0.4733 puts (Q)'s cap below the meeting floor with
   room to spare. But the margin is two measured extremes with no
   derivation between them, so the same census widened is exactly what
   it owes -- and J7 is that it does not survive it.

J4 THE MIDDLE IS A GAP IN y, NOT A SPARSE SOURCE. Of the two mechanisms
   E-G separates, (i) carries it and (ii) does not. Over the 3516
   non-contained pairs below the cut, y clears the meeting radius by a
   factor of 1.098 at the tightest, 2.938 at the median and 33.639 at
   the widest -- so the coordinate is not near the boundary and no
   discreteness argument is needed. Meanwhile the progression that
   would have to hit the target carries 3, 5, 6, 7 or nine-or-more
   admissible points (never one) and is unrestricted, kappa_i = 1, at
   2784 of the 3516. So what wants deriving is why the window
   (2 M_Delta, 2 M_j] holds no attainable y, and (H)'s carry form says
   what attainable MEANS: y qualifies iff sigma.y mod n < b^Delta, so
   the attainable y are a Steinhaus set of b^Delta points and the
   window's emptiness is a THREE-DISTANCE statement about sigma/n --
   the instrument explore_slope_dodge.py already reads its survivors
   with, one level up. This file does not take that step.

J5 THE CENSUS PUSHED 2.5x AND NEITHER KILL FIRED. At N <= 150,000:
   29233 cells, a width distribution of {1: 1057482, 2: 23996,
   3: 4844}, and the shallow pair empty at 4844 of 4844 -- K2 never
   fires, so "the two shallowest maximal levels never meet" survives a
   census 6x the population it was minted on. K3 never fires either:
   no class anywhere has all three pairs non-empty, so the triple term
   the parent's (D) lacks is still empty before it is reached and the
   assembly is unjustified at width 3 and wrong nowhere. What the wider
   census DOES break is the completeness of the interval reading: K5
   fired at 48 pairs, empty with y INSIDE an arc, and all 48 are mid or
   deep pairs -- 24 each -- while the shallow pair is empty by the
   interval bound at 4844 of 4844 and 812 of 812. So discreteness is a
   real second mechanism for the pairs J2's cap does not cover, and a
   derivation resting on the reach bound alone owes those 48 a word.

J6 K4 WAS MIS-SCOPED AT THE FREEZE AND FIRED ON A PREDICTION. As first
   frozen it read "mu at or above 1 ANYWHERE", which asserts more than
   (Q) claims: (Q) bounds the pair whose deeper level has a third
   maximal level under it, and the mid and deep pairs have i3 as their
   deeper level with nothing under it, so their mu reaching 1 is what
   the derivation predicts and not a violation of it. It fired
   immediately on exactly those. The kill's SCOPE is corrected rather
   than the finding written around it -- a kill that fires on a
   prediction is a defect in the slate, and the tell is that its
   subject ("mu") was written wider than the derivation's ("the shallow
   pair's mu"). A second reporting defect rode with it: mu was printed
   as a count over n and read above 1 at the mid and deep pairs, where
   the two arcs have overlapped and the count double-reads the circle;
   it is a FRACTION and is now clamped, which is why the mid and deep
   maxima read 1.0000 rather than 1.7154 and 1.8597.

VERDICT, by piece.
  - (P), THE TWO RADII, is a PROPERTY: an identity on the repunits plus
    b^Delta M_i < n/2, all cases, nothing asked about which residues
    are attained. Checked at 3766 pairs against sets and floor-sums,
    and its meeting arc at 1,786,658. The containment radius is
    SUFFICIENT and not necessary, the converse failing at 284 of those.
  - (Q), THE CAP, is a PROPERTY: it follows from i3 being a level and
    the repunit ratio. Checked 0 violations over 5656 width-3 classes.
  - THE DICHOTOMY (J3) is a PATTERN whose THRESHOLD IS NOT A CONSTANT:
    the meeting floor reads 0.4733 at N <= 60,000 and 0.3602 at
    N <= 150,000, so it is a property of the census reached and not yet
    of the object.
  - THE EMPTY SHALLOW PAIR (J5) is a RULE at the scope stated,
    N <= 150,000 at phase 0, and it is NOT explained here. (Q)'s cap
    plus the dichotomy accounts for it only at the narrower census; at
    the wider one the floor drops under the cap and at least 48 shallow
    pairs are empty with no reason on offer. That gap is the finding
    this file hands on, and it is sharper than the column it replaced
    because it names the exact 48 places to look.
  - THE THREE-DISTANCE READING of the window (J4) is a FRAME and not a
    result: sigma.y mod n < b^Delta is derived, the gap statement it
    would need is not attempted here.

J7 AND THE COMPOSITION DOES NOT SURVIVE THE WIDER CENSUS. Run at
   N <= 150,000 -- the scope the cap was already asserted over -- the
   meeting floor FALLS to 0.3602, at N = 150000,
   (b, a, c, u, v) = (10, 8, 4, 65632, 15), class 3, levels 1 and 3.
   That is BELOW the cap's 0.4118, so the margin J3 closed on is a
   narrow-census artefact and the cap does NOT by itself keep the
   shallow pair under the meeting floor: at least 48 of the 4844
   shallow pairs sit above 0.4 and therefore above the floor, and every
   one of them is empty anyway. So the honest account is a PARTIAL one.
   (Q)'s cap is a property and holds; the dichotomy is real but its
   threshold MOVES with scope rather than being a constant of the
   object; and what is left over -- shallow pairs whose measure exceeds
   the observed meeting floor and which miss regardless -- is
   unexplained and is the residual (Q)'s own design text said a wider
   census would put to the question. It did, and the answer was no.
   What did NOT move is the phenomenon: at the wider census the
   non-contained meeting rate is still 0.0000 across every bucket below
   mu = 0.3, which is 20,128 pairs, and only 0.0017 in [0.3, 0.4). So
   the dichotomy has a SOFT edge rather than a hard threshold, the cap
   still covers the bulk -- the shallow median is 0.1781, deep inside
   the exactly-zero region -- and what is bare is the tail above about
   0.3. That is the difference between a law that collapsed and an
   account that is incomplete at a located margin, and this is the
   second.
   The criterion's converse widens with it: 1436 measured containments
   with y > 2 M_Delta over the wider census against 284 over the
   narrower, so I3's failure is not a small fixed set either.

RUN RECORD: pure Python, integers only, standard library;
explore_slope_tree.py's cell and repunit, explore_slope_assemble.py's
level_data, count_single, count_pair and two_level_cells, and
explore_slope_width.py's solved_cells, level_sets and measured_width
imported rather than copied, so every control reads the same code path
the comparison does. 230.7 s wall, peak working set 113.0 MB against
the 512 MB analysis ceiling (memwatch.py) -- the width measurement
costs O(width^2) floor-sums rather than an n-sized set per class, which
is what lets the census reach N = 150,000 in under a minute. The
censuses: the control at N <= 3000 through the parent's swept
two_level_cells (219 cells), and phase 0 with u SOLVED over radices to
12, digit sets to a = 8, lookahead to 8 at N <= 60,000 (11095 cells)
and N <= 150,000 (29233 cells), both at below-count >= 3, with the mu
curve read over every pair of both (1,786,658 and 6,722,358). Phase 0 only:
(G)'s solver does not solve for phi, so the phase axis is untested here
as it was in the parent. Prints reproduced by:
python prime/code/explore_slope_empty.py
"""

import os
import sys
import time
from math import gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_slope_tree import cell, repunit  # noqa: E402
from explore_slope_assemble import (  # noqa: E402
    level_data, count_single, count_pair, two_level_cells,
)
from explore_slope_width import (  # noqa: E402
    solved_cells, level_sets, measured_width,
)

FAILURES = []


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


# --------------------------------------------- the pair, three ways

def pair_counts(b, n, A, C):
    """|B_A|, |B_C|, |B_A cap B_C| by the parent's floor-sums."""
    dm = pow(b, C["j"] - A["j"], n)
    inter = count_pair(n, A["mult"], dm, A["d"], A["runs"],
                       C["d"], C["runs"])
    return (count_single(n, A["mult"], A["d"], A["runs"]),
            count_single(n, C["mult"], C["d"], C["runs"]),
            inter)


def pair_y(b, a, n, A, C):
    """(P)'s coordinate y = (e + M_Delta) mod n, with the centered e and
    the radii. Delta = C.j - A.j."""
    dl = C["j"] - A["j"]
    bd = b ** dl
    MD = a * repunit(b, dl)
    e = (C["d"] - bd * A["d"]) % n
    if e > n // 2:
        e -= n
    return (e + MD) % n, e, MD, bd


def meets_interval(b, a, n, A, C):
    """(P)'s exact meeting test: an admissible integer v in some wrap."""
    _, e, _, bd = pair_y(b, a, n, A, C)
    Mi, Mj = A["M"], C["M"]
    kap = gcd(A["mult"], n) if A["mult"] % n else n
    d = A["d"] % kap
    for k in (-1, 0, 1):
        lo = -((-(-Mj + k * n - e)) // bd)          # ceil
        hi = (Mj + k * n - e) // bd                 # floor
        lo, hi = max(lo, -Mi), min(hi, Mi)
        if lo > hi:
            continue
        v = lo + ((d - lo) % kap)
        if v <= hi:
            return True
    return False


def reach(b, a, n, A, C):
    """(P)'s necessary arcs: (y admitted for meeting, y admitted for
    containment, the meeting measure mu as a count)."""
    y, _, MD, _ = pair_y(b, a, n, A, C)
    Mj = C["M"]
    may_meet = y <= 2 * Mj or y >= n - 2 * Mj + 2 * MD
    return may_meet, y <= 2 * MD, 4 * Mj - 2 * MD + 1, y


def cheap_width(b, a, n, deep):
    """The maximal levels under EXACT containment, equal sets collapsed,
    from counts alone. Returns the maximal level dicts in ascending
    level order."""
    inc = {}
    for i in range(len(deep)):
        for k in range(i + 1, len(deep)):
            si, sk, it = pair_counts(b, n, deep[i], deep[k])
            inc[(i, k)] = si == it                    # B_i subset B_k
            inc[(k, i)] = sk == it                    # B_k subset B_i
    keep = []
    for i in range(len(deep)):
        # dropped if some other level contains it, EQUAL sets aside,
        # where only the shallowest representative survives
        if any(inc[(i, k)] and (not inc[(k, i)] or k < i)
               for k in range(len(deep)) if k != i):
            continue
        keep.append(deep[i])
    return keep


# ---------------------------------------------------------- E-A

def e_a_controls(cap=3000):
    print(f"E-A  THE CONTROLS, N <= {cap}")
    t0 = time.time()
    cells = two_level_cells(cap, 2)
    classes = wid_ok = pair_ok = interval_ok = 0
    bad_reach_meet = bad_reach_cont = 0
    for N, key, ce, two in cells:
        b, a = key[0], key[1]
        n = ce["n"]
        for t in two:
            lv, _ = level_data(b, a, ce, t)
            deep = [x for x in lv if x["j"] > 0]
            if len(deep) < 2:
                continue
            classes += 1
            mw, sets = measured_width(ce, deep)
            keep = cheap_width(b, a, n, deep)
            if len(keep) == mw:
                wid_ok += 1
            else:
                ok(False, f"cheap width {len(keep)} vs measured {mw} "
                          f"at N={N} {key} t={t}")
            for i in range(len(deep)):
                for k in range(i + 1, len(deep)):
                    si, sk, it = pair_counts(b, n, deep[i], deep[k])
                    truth_in = sets[i] <= sets[k]
                    truth_meet = bool(sets[i] & sets[k])
                    if (si == it) == truth_in and (it > 0) == truth_meet \
                            and si == len(sets[i]) and sk == len(sets[k]):
                        pair_ok += 1
                    else:
                        ok(False, f"counts vs sets at N={N} {key} t={t} "
                                  f"levels {deep[i]['j']},{deep[k]['j']}")
                    if meets_interval(b, a, n, deep[i], deep[k]) == (it > 0):
                        interval_ok += 1
                    else:
                        ok(False, f"(P) interval vs count at N={N} {key} "
                                  f"t={t} levels {deep[i]['j']},"
                                  f"{deep[k]['j']}")
                    may_meet, may_cont, _, _ = reach(b, a, n, deep[i],
                                                     deep[k])
                    if it > 0 and not may_meet:
                        bad_reach_meet += 1
                    if si == it and not may_cont:
                        # the criterion's converse, measured and not
                        # asserted: it is FALSE off this census's scope
                        bad_reach_cont += 1
    print(f"  cells {len(cells)}, classes with 2+ lost levels {classes}")
    print(f"  cheap width == set-measured width: {wid_ok} of {classes}")
    print(f"  per-pair counts == direct sets (size, containment, "
          f"meeting): {pair_ok}")
    print(f"  (P)'s interval test == count_pair > 0: {interval_ok}")
    print(f"  (P)'s meeting arc violated at {bad_reach_meet}; measured "
          f"containments with y > 2 M_Delta (the criterion's CONVERSE, "
          f"measured not asserted): {bad_reach_cont}")
    ok(bad_reach_meet == 0, "(P) meeting arc is necessary")
    print(f"  control failures: {len(FAILURES)}  [{time.time() - t0:.1f} s]")


# ------------------------------------------------------ the census

def census(cap, label, min_below=3):
    """Every width-3 class at N <= cap, with the three maximal levels
    and the per-pair verdicts. Widths measured exactly by counts."""
    t0 = time.time()
    cells = solved_cells(cap, min_below)
    print(f"  {label}: cells {len(cells)}  [{time.time() - t0:.1f} s]")
    widths, w3, w2 = {}, [], []
    for N, key, ce, two in cells:
        b, a = key[0], key[1]
        n = ce["n"]
        for t in two:
            lv, _ = level_data(b, a, ce, t)
            deep = [x for x in lv if x["j"] > 0]
            if len(deep) < 2:
                continue
            keep = cheap_width(b, a, n, deep)
            wd = len(keep)
            widths[wd] = widths.get(wd, 0) + 1
            if wd == 2:
                w2.append((N, key, t, ce, keep))
            elif wd == 3:
                w3.append((N, key, t, ce, keep))
    print(f"    width distribution (exact): {dict(sorted(widths.items()))}")
    over = sum(v for k, v in widths.items() if k > 3)
    if over:
        print(f"    width ABOVE 3: {over} classes -- the shallow/mid/deep "
              f"labelling is a width-3 statement and does not cover them")
    return widths, w2, w3


def pair_report(b, a, n, A, C):
    """Everything (P) and (Q) say about one pair."""
    si, _, it = pair_counts(b, n, A, C)
    may_meet, may_cont, mu_cnt, y = reach(b, a, n, A, C)
    # the two arcs overlap once the count reaches n, so the FRACTION is
    # clamped: an unclamped mu above 1 is a double count, not a measure
    return {"meets": it > 0, "size": it, "y": y, "may_meet": may_meet,
            "contained": may_cont, "mu": min(1.0, mu_cnt / n),
            "measured_in": si == it,
            "by_reach": (it == 0 and not may_meet)}


def e_b_c(w3, w2, label):
    print(f"E-B  HOW THE SHALLOW PAIR IS EMPTY  ({label})")
    tags = ("shallow", "mid", "deep")
    idx = ((0, 1), (0, 2), (1, 2))
    empty = {g: 0 for g in tags}
    by_reach = {g: 0 for g in tags}
    by_disc = {g: 0 for g in tags}
    mus = {g: [] for g in tags}
    cap_bad = worst = None
    cap_viol = k4 = all_full = 0
    meets_shallow = []
    triples_owed = []
    for N, key, t, ce, keep in w3:
        b, a = key[0], key[1]
        n = ce["n"]
        reps = [pair_report(b, a, n, keep[i], keep[k]) for i, k in idx]
        for g, r in zip(tags, reps):
            mus[g].append(r["mu"])
            if g == "shallow" and r["mu"] >= 1.0:
                k4 += 1
            if not r["meets"]:
                empty[g] += 1
                if r["by_reach"]:
                    by_reach[g] += 1
                else:
                    by_disc[g] += 1
        # (Q)'s cap on the shallow pair
        d23 = keep[2]["j"] - keep[1]["j"]
        cap = 2.0 / b ** d23
        if reps[0]["mu"] >= cap:
            cap_viol += 1
            if cap_bad is None:
                cap_bad = (N, key, t, reps[0]["mu"], cap)
        if worst is None or reps[0]["mu"] > worst[3]:
            worst = (N, key, t, reps[0]["mu"], cap)
        if reps[0]["meets"]:
            meets_shallow.append((N, key, t, reps[0]["size"]))
        if all(r["meets"] for r in reps):
            all_full += 1
            triples_owed.append((N, key, t, ce, keep))
    tot = len(w3)
    print(f"  width-3 classes: {tot}")
    for g in tags:
        print(f"    {g:8s} pair empty at {empty[g]:5d} of {tot}"
              f"  -- by reach {by_reach[g]}, by discreteness {by_disc[g]}")
    print(f"  K5 (empty by discreteness anywhere): "
          f"{sum(by_disc.values())}")
    print(f"  K2 (shallow pair MEETS): {len(meets_shallow)}"
          + (f"; smallest {meets_shallow[0]}" if meets_shallow else ""))
    print(f"  K3 (all three pairs non-empty): {all_full}")
    print("E-C  THE MEETING MEASURE")
    for g in tags:
        v = sorted(mus[g])
        if not v:
            continue
        print(f"    {g:8s} mu: max {v[-1]:.4f}, median "
              f"{v[len(v) // 2]:.4f}, min {v[0]:.4f}")
    if w2:
        v2 = []
        for N, key, t, ce, keep in w2:
            b, a = key[0], key[1]
            r = pair_report(b, a, ce["n"], keep[0], keep[1])
            v2.append((r["mu"], not r["meets"], r["by_reach"]))
        v2.sort()
        mv = [x[0] for x in v2]
        e2 = sum(1 for x in v2 if x[1])
        r2 = sum(1 for x in v2 if x[2])
        print(f"    BASELINE width-2 single pair: {len(v2)} classes, "
              f"empty at {e2} (by reach {r2}); mu max {mv[-1]:.4f}, "
              f"median {mv[len(mv) // 2]:.4f}, min {mv[0]:.4f}")
    above = sum(1 for m in mus["shallow"] if m >= 0.4)
    print(f"  shallow pairs with mu >= 0.4: {above} of {tot}  (0.4 is a "
          f"fixed reference, NOT the meeting floor -- that floor is "
          f"measured per census by E-F and moves)")
    print(f"  (Q)'s cap mu_shallow < 2/b^(i3-i2) violated at "
          f"{cap_viol} of {tot} (K4, mu_shallow >= 1, at {k4})")
    ok(cap_viol == 0, "(Q)'s cap on the shallow meeting measure")
    ok(k4 == 0, "K4: the shallow pair's mu below 1")
    if worst:
        print(f"  largest mu_shallow: N={worst[0]} {worst[1]} t={worst[2]} "
              f"mu={worst[3]:.4f} against the cap {worst[4]:.4f}")
    return triples_owed


def e_f_mu_curve(cap, min_below=3):
    """E-F, frozen after E-B and E-C printed and before this pass was
    written. They left one thing unexplained: the cap of (Q) holds and
    every emptiness is by reach, but mu_shallow has a MEDIAN near a
    quarter, so a y spread evenly over Z/n would have let a quarter of
    the 812 meet. Either y is not spread, or the cap is not the
    mechanism. The counterfactual settles it without any appeal to
    width: bucket EVERY pair of lost levels of the census by its own mu
    and read the meeting rate against it. Under a spread y the rate is
    the diagonal; a step function at some mu says y is placed, and where
    the step sits is then the object to derive."""
    print(f"E-F  THE MU CURVE over every pair, N <= {cap}")
    t0 = time.time()
    cells = solved_cells(cap, min_below)
    buckets = {}
    nc_buckets = {}
    pairs = bad = conv = 0
    meet_min = None
    for N, key, ce, two in cells:
        b, a = key[0], key[1]
        n = ce["n"]
        for t in two:
            lv, _ = level_data(b, a, ce, t)
            deep = [x for x in lv if x["j"] > 0]
            for i in range(len(deep)):
                for k in range(i + 1, len(deep)):
                    r = pair_report(b, a, n, deep[i], deep[k])
                    pairs += 1
                    # (P)'s MEETING half, the one this file adds,
                    # re-tested at census scale: E-A checks it at 3766
                    # pairs and every verdict below rests on it. The
                    # containment half is not tested beside it, because
                    # "contained implies y <= 2 M_Delta" is the
                    # criterion's CONVERSE and the parent already
                    # falsified it (explore_slope_width.py's I3, 284
                    # pairs) -- it is counted below as what it is, a
                    # measurement, and never asserted
                    if r["meets"] and not r["may_meet"]:
                        bad += 1
                    if r["measured_in"] and not r["contained"]:
                        conv += 1
                    # THE number the composition turns on: the smallest
                    # measure at which a non-contained pair is observed
                    # to meet. The cap of (Q) closes the empty-pair law
                    # only if it sits BELOW this
                    if r["meets"] and not r["contained"]:
                        if meet_min is None or r["mu"] < meet_min[0]:
                            meet_min = (r["mu"], N, key, t,
                                        deep[i]["j"], deep[k]["j"])
                    bk = min(9, int(r["mu"] * 10))
                    m, tt = buckets.get(bk, (0, 0))
                    buckets[bk] = (m + (1 if r["meets"] else 0), tt + 1)
                    if not r["contained"]:
                        m, tt = nc_buckets.get(bk, (0, 0))
                        nc_buckets[bk] = (m + (1 if r["meets"] else 0),
                                          tt + 1)
    print(f"  pairs read: {pairs}; (P)'s MEETING half violated at "
          f"{bad}  [{time.time() - t0:.1f} s]")
    ok(bad == 0, "(P)'s meeting arc is necessary, at census scale")
    print(f"  measured containments with y > 2 M_Delta (the criterion's "
          f"CONVERSE, a measurement and not a control): {conv}")
    print(f"  SMALLEST mu at which a non-contained pair MEETS: "
          f"{meet_min}")
    print("    mu bucket | pairs | meet | rate  || non-contained only")
    for bk in sorted(buckets):
        m, tt = buckets[bk]
        nm, nt = nc_buckets.get(bk, (0, 0))
        print(f"    [{bk / 10:.1f},{(bk + 1) / 10:.1f}) | {tt:7d} | "
              f"{m:7d} | {m / tt:.4f} || {nt:7d} pairs, "
              f"{(nm / nt if nt else 0):.4f}")


def e_g_middle(cap, mu_cut=0.4, min_below=3):
    """E-G, frozen after E-F printed. The curve says a NON-CONTAINED
    pair below mu = 0.4 never meets, 3516 of 3516, which is a
    dichotomy -- contain or miss, no middle -- and is what the width-3
    law is actually made of. Two mechanisms could produce it and they
    are told apart by measurement, not by preference.
    (i) A GAP IN y: containment ends at y = 2 M_Delta and the next
        attainable y is already past 2 M_j, so the middle window
        (2 M_Delta, 2 M_j] holds no y at all. Tell: y / (2 M_j) bounded
        away from 1 from above at every such pair.
    (ii) A SPARSE SOURCE: v is not free but runs over a coset of
        kappa_i = gcd(b^i, n) inside [-M_i, M_i], so the progression
        that has to hit the target has effective step b^Delta kappa_i
        and may hold FEW points -- at 2 M_i < kappa_i, exactly one.
        Tell: the admissible-v count at 1 or near it.
    Both are printed for the same pairs, so whichever is doing the work
    says so."""
    print(f"E-G  WHAT THE MIDDLE IS MADE OF, mu < {mu_cut}, N <= {cap}")
    t0 = time.time()
    cells = solved_cells(cap, min_below)
    ratios, vcounts, kap1 = [], {}, 0
    tot = 0
    for N, key, ce, two in cells:
        b, a = key[0], key[1]
        n = ce["n"]
        for t in two:
            lv, _ = level_data(b, a, ce, t)
            deep = [x for x in lv if x["j"] > 0]
            for i in range(len(deep)):
                for k in range(i + 1, len(deep)):
                    A, C = deep[i], deep[k]
                    r = pair_report(b, a, n, A, C)
                    if r["contained"] or r["mu"] >= mu_cut:
                        continue
                    tot += 1
                    y, _, MD, _ = pair_y(b, a, n, A, C)
                    # how far past the meeting radius, on whichever side
                    up = y / (2 * C["M"])
                    dn = (n - y) / (2 * C["M"] - 2 * MD)
                    ratios.append(min(up, dn))
                    kp = gcd(A["mult"], n) if A["mult"] % n else n
                    nv = (2 * A["M"]) // kp + 1
                    vcounts[min(nv, 9)] = vcounts.get(min(nv, 9), 0) + 1
                    if kp == 1:
                        kap1 += 1
    ratios.sort()
    print(f"  non-contained pairs below the cut: {tot}  "
          f"[{time.time() - t0:.1f} s]")
    if ratios:
        print(f"  (i) distance past the meeting radius, as a multiple of "
              f"it: min {ratios[0]:.3f}, median "
              f"{ratios[len(ratios) // 2]:.3f}, max {ratios[-1]:.3f}")
    print(f"  (ii) admissible v in [-M_i, M_i] (9 = nine or more): "
          f"{dict(sorted(vcounts.items()))}; kappa_i = 1 at {kap1}")


def e_d_triples(triples_owed):
    """K3's follow-through: a triple can still be empty with three
    non-empty pairs, so it is MEASURED before anything is claimed."""
    if not triples_owed:
        print("E-D  no class with three non-empty pairs -- the triple "
              "term is empty before it is reached, everywhere measured")
        return
    print(f"E-D  {len(triples_owed)} classes with three non-empty pairs; "
          f"the triple term MEASURED at each")
    for N, key, t, ce, keep in triples_owed[:5]:
        sets = level_sets(ce, keep)
        tri = sets[0] & sets[1] & sets[2]
        print(f"    N={N} {key} t={t} levels {[x['j'] for x in keep]}: "
              f"|triple| = {len(tri)}")


def main():
    t0 = time.time()
    e_a_controls()
    if FAILURES:
        print("\nK1: controls failed -- nothing below is read.")
        return
    print()
    _, w2, w3 = census(60000, "THE PARENT'S SCOPE, N <= 60000")
    owed = e_b_c(w3, w2, "N <= 60000")
    e_d_triples(owed)
    print()
    e_f_mu_curve(60000)
    print()
    e_g_middle(60000)
    print()
    _, w2b, w3b = census(WIDE_CAP, f"E-D  THE WIDER CENSUS, "
                                   f"N <= {WIDE_CAP}")
    owed_b = e_b_c(w3b, w2b, f"N <= {WIDE_CAP}")
    e_d_triples(owed_b)
    print()
    # the meeting FLOOR read at the same scope as the cap: a floor from
    # the narrow census composed with a cap from the wide one is a
    # comparison neither census made
    e_f_mu_curve(WIDE_CAP)
    print(f"\ntotal failures: {len(FAILURES)}  "
          f"[{time.time() - t0:.1f} s]")


WIDE_CAP = 150000

if __name__ == "__main__":
    main()
