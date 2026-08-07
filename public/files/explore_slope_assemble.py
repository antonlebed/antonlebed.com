"""Assembling W below J when a class loses TWO levels: the intersection
is a floor-sum, and the boundary moves to three.

THE QUESTION. explore_slope_dodge.py closes the tree condition one level
at a time and its (T) leaves the ASSEMBLY open: different levels carry
different multipliers b^j, so in a common coordinate the survivor sets
are progressions rather than intervals and were not collapsed into one
description. explore_slope_twolevel.py then showed the open case is real
and ordinary -- a class losing two levels below J exists, 262 witnesses
below N = 6000, the smallest at radix 2, digits {-1, 0, 1}, slope 40/9,
lookahead 3. This asks for the description (T) stopped short of: |W| in
one class, closed, when two levels are lost -- or the exact price of its
resisting.

THE DERIVATION, hand-attacked on paper before this engine existed.
Notation is explore_slope_tree.py's: N = L b^c, q = L u / v,
g = gcd(q, N), n = N/g, I = [lo, hi], B = Z/N \\ pi(I) the cyclic block
of D = N - span residues from B0 = (hi + 1) mod N, sigma = q/g a unit of
Z/n, f(t) = b t - (b-1) phi (mod g), r_j the repunit, M_j = a r_j, and J
the least j with 2 M_j + 1 >= n.

(A) EVERY LEVEL HAS THE SAME SHAPE, INCLUDING LEVEL 0. Fix a class t of
I and write m = t + g s. explore_slope_tree.py's w_tree calls m bad at
level j when b^j m mod N lies in B + (b-1) phi r_j - q [-M_j, M_j].
Reducing mod g picks out the single class t_j = f^j(t), so with
h_j = ((b^j t - (b-1) phi r_j - t_j) mod N)/g and (beta_j, lam_j) the
block of B inside class t_j from dodge's (P),

    m is bad at level j  iff  b^j s + c_j  in  D_j   (mod n),
    c_j = (h_j - beta_j) mod n,  D_j = [0, lam_j) + sigma [-M_j, M_j].

At j = 0 this reads r_0 = 0, M_0 = 0, t_0 = t, h_0 = 0, so D_0 is the
block itself and "bad at level 0" is exactly m NOT in I. The ambient
interval is therefore not a separate kind of constraint: it is level 0
of the same family, and the whole condition is

    W_t  =  Z/n  minus  union over j in Lambda of B_j,
    Lambda = {0} union {1 <= j < J : lam_j > 0},
    B_j = {s : b^j s + c_j in D_j}.

(B) THE RIGHT COORDINATE IS sigma^{-1}, NOT sigma. Put w = sigma^{-1} s.
Then B_j = {w : b^j w + d_j in D'_j} with d_j = sigma^{-1} c_j and

    D'_j = [-M_j, M_j] + sigma^{-1} [0, lam_j),

a union of at most lam_j runs of length 2 M_j + 1 -- where dodge's
s-coordinate makes D_j a union of up to 2 M_j + 1 runs of length lam_j.
Same set, and the run count falls from the tree width to the block
length. Below J we have 2 M_j + 1 < n, so no run is the whole circle.

(C) THE PAIR COUNT IS A FLOOR-SUM, WITH NO UNIT ASSUMED. For i < j and
Delta = j - i, b^j w = b^Delta (b^i w), so the level-j value is a
function of the level-i value whether or not b is invertible mod n. Let
kappa = gcd(b^i mod n, n), n2 = n/kappa, mu = (b^i mod n)/kappa, which
is a unit mod n2. Then w -> y = mu w (mod n2) is kappa-to-1 onto Z/n2
and carries b^i w to kappa y, b^j w to kappa (b^Delta y mod n2). A run
condition on b^i w becomes a run condition on y in Z/n2 -- the multiples
of kappa inside a cyclic interval are an interval of y -- and the
level-j run becomes a run condition on b^Delta y. So for one run of D'_i
against one run of D'_j,

    |B_i cap B_j|  =  kappa * #{y in [A, A+len) : (b^Delta y + e) mod n2
                                                  < len'},

which is two floor-sums by [x mod n < l] = floor(x/n) - floor((x-l)/n),
O(log n) each. The whole pair costs at most lam_i lam_j of them.

(D) SO TWO LOST LEVELS ASSEMBLE, AND THREE DO NOT. With Lambda =
{0, j1, j2}, inclusion-exclusion needs three singles, three pairs and
one triple. The singles are O(1): the values b^j w hit each element of
one coset of kappa Z exactly kappa times, so |B_j| = kappa times the
count of run elements in that coset. The pairs are (C). And every
intersection containing B_0 is settled by ENUMERATING B_0, which has
lam_t <= g - 1 elements and is the block itself -- so the triple costs
O(lam) membership tests, not a lattice count. Nothing in the assembly is
a walk over the interval. With THREE lost levels the term
|B_j1 cap B_j2 cap B_j3| survives with no B_0 in it: three runs under
three multipliers, a rank-3 lattice point count with no Euclidean
descent. The boundary (T) drew at ONE lost level therefore sits at TWO,
and what is open is the three-level class.

(E) WHY THE DEEPEST LEVEL USUALLY SUFFICES. twolevel's R-M measured the
deepest lost level alone giving the whole intersection at 2290 of 2346
class tests. Where lam_i = lam_j = 1 -- which its G4 forces at every
mismatch-capable cell of integer rho = 2a/(b-1), since there the span
deficit is exactly g - 1 and the g - 1 bad residues fall one per class
-- D'_j is the single run [-M_j, M_j] and B_j = {w : b^j w + d_j in
[-M_j, M_j]}. For w in B_i write x = b^i w + d_i, so |x| <= M_i and the
level-j value is b^Delta x + eps with eps = (d_j - b^Delta d_i) mod n
taken in (-n/2, n/2]. Since b^Delta M_i = M_j - a r_Delta,

    |eps| <= a r_{j-i}   FORCES   B_i subset B_j,

the level-j value having absolute value at most M_j and 2 M_j + 1 < n
below J leaving no wraparound. That direction is a derivation and costs
nothing: it never asks which x are attained. THE CONVERSE DOES, and is
NOT derived here. It needs the extreme x = +-M_i to be reached by some
w, which holds where b^i is a unit mod n -- and gcd(b^i, n) > 1 is
ordinary at these cells, so where the map is not onto the run, an eps
past a r_Delta may still miss every attained x. S-D therefore measures
the converse rather than assuming it, and reduce_levels uses only the
derived direction: it drops a level the inequality CERTIFIES contained
and keeps every level it does not. A criterion that failed the converse
would cost coverage, never soundness.
Equivalently, in terms of the bad residues alone,
eps = sigma^{-1} (b^Delta x_i - x_j - (b-1) phi r_Delta) / g, where x_j
is the unique element of B in class t_j.

THE DESIGN, frozen before the engine.

S-A THE CONTROLS, three, all against explore_slope_tree.py's own tree
    walk rather than against a claim. (A)'s per-level bad set, converted
    back to states, must equal w_tree's bad[j] restricted to the class,
    in BOTH directions, at every (cell, level, deep-saturated class) of
    the census. The closed run decomposition of D'_j from (B) must equal
    a direct mask build of the same set. And count_pair from (C) must
    equal a direct walk over Z/n at every pair it is asked for. Plus the
    parent's own headline through the imported path: the witness cell
    printing |W| = 37 against |W*| = 17.
S-B THE CLOSED COUNT. Over every two-level cell with N <= 3000 -- R-M's
    scope, so the two passes are comparable cell for cell -- assemble
    |W_t| for every deep-saturated class by the inclusion-exclusion of
    (D) and compare against w_tree's own W restricted to that class.
    Report agreement as a class count and a cell count, and print the
    first disagreement in full. This is the whole claim: a count with no
    walk over the interval, at the cells (T) said it had none for.
S-C THE PAIR TERM ALONE. For the same classes, report how large the
    pairwise intersection |B_j1 cap B_j2| actually is against the
    product of its factors -- the quantity (T) called an obstruction --
    and how many classes have it EMPTY. An intersection that is almost
    always empty says the term is cheap in practice as well as closed.
S-D THE SUBSUMPTION CRITERION. At every class where both lost levels
    have lam = 1, compare |eps| <= a r_Delta against measured set
    containment B_i subset B_j, both directions, as a confusion count.
    Then report how many of R-M's agreements the criterion explains:
    where the deepest level subsumes every shallower lost level the
    assembly collapses to a single level and the pair term is not
    needed at all.
S-E THE lam CENSUS, integer rho against fractional. Over the same
    cells, report the distribution of lam over unsaturated classes,
    split by whether rho = 2a/(b-1) is an integer. G4 predicts lam = 1
    throughout the integer rows; R-M's 56 disagreements all sit at
    (b, a, c, u, v) = (4, 2, 3, 448, 25) where rho = 4/3, and the
    prediction is that lam > 1 is what distinguishes that cell. If it
    holds, the criterion of (E) is not merely unverified there, it is
    inapplicable, and (C) is what covers it. That cell is read
    explicitly whether or not it falls under the N cap.
S-F THE THREE-LEVEL FRONTIER. Sweep for a class with below-count >= 3
    over the R-L scope (N <= 6000, radices to 12, digit sets to a = 8,
    lookahead to 8, slopes u to 600 over v to 80, phase 0) using the
    cheap class-map predicate only, and report the smallest by N with
    its lost levels. G4 reports below-counts to 6 inside a CONSTRUCTED
    family, which is selected evidence; this asks whether an unselected
    ordering reaches one, and how far below the first three-level cell
    the closed form of (D) is complete.

S-G IS THE COUNT REALLY TWO LEVELS, OR IS IT TWO INCOMPARABLE ONES,
    frozen after S-A..S-F printed and before this pass was written. Two
    of those prints together say the boundary was drawn in the wrong
    place. S-D's criterion is exact and finds the shallower level
    CONTAINED in the deeper at 1628 of 1684 classes; S-F finds classes
    with three lost levels ordinary, 662 of them inside this very
    census. But containment does not care how many levels there are: if
    B_i is inside B_j the union forgets B_i, so a family of any size
    reduces to its maximal elements under the criterion, and (D)'s
    inclusion-exclusion is closed as soon as at most TWO survive. The
    quantity that decides is the WIDTH of the containment order, not
    the number of lost levels. So: over every class of this census with
    three or more lost levels, reduce by the O(1) criterion, report the
    distribution of the surviving width, and where it is at most 2 run
    the closed count of (D) against w_tree's own per-class count. The
    criterion is only proved for lam = 1 at both levels, so a class
    with any lam > 1 on a lost level is excluded and counted. What
    prints is how much of the three-level population the closed form
    already covers and what the residue actually is.

KILLS, frozen as what this rig PRINTS.

M1 A control misses -> the coordinate change (A), the run
   decomposition (B) or the pair count (C) is wrong, and nothing below
   is read.
M2 A class where the inclusion-exclusion count differs from w_tree's own
   per-class count -> (D)'s assembly is wrong even if its pieces are
   not, and the two-level case is NOT closed.
M3 A class with lam = 1 at both lost levels where |eps| <= a r_Delta
   disagrees with measured containment -> (E) is wrong; not a kill for
   the closed count, which never uses it.
M4 A two-level class carrying THREE or more lost levels inside the
   census -> S-B's inclusion-exclusion is being asked for a triple term
   it has no closed form for; it prints and is excluded from the
   closed-count tally rather than silently counted.
M5 A class S-G reduces to width <= 2 whose closed count differs from
   the tree walk -> the containment reduction is unsound and the
   criterion cannot be used to drop a level, whatever S-D measured
   about it pairwise.

POSITIVE CONTROL, run and read before any verdict line: S-A whole.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

H1 THE CONTROLS HOLD. (A)'s per-level bad set, converted back to
   states, is w_tree's own bad[j] restricted to the class at 5386
   (cell, level, class) triples in both directions; the closed run
   decomposition of (B) matches a direct mask build at every one of
   them; count_pair matches a direct walk over Z/n at 3766 pairs; and
   the witness reproduces |W| = 37 against |W*| = 17 through the
   imported path. M1 fired once during development and is what caught
   the only error in this file: count_single selected the residue class
   of the run's START against the offset rather than the offset against
   the start, which is invisible wherever gcd(b^j, n) = 1 and wrong at
   116 (cell, class, level) singles where it is not -- fewer classes
   than that, a two-level class firing once per lost level. The
   general reduction of (C) was not decoration: gcd(b^j, n) > 1 is
   ordinary here, and that branch is the only one the error lived in.

H2 (T) IS CLOSED, NOT A BOUNDARY. The inclusion-exclusion of (D) gives
   |W_t| with no walk over the interval at 1684 of 1684 two-lost-level
   classes over all 219 two-level cells with N <= 3000, and differs
   nowhere. M2 never fired. The assembly dodge's (T) left open is a
   single floor-sum: the ambient interval is level 0 of the same
   family, its bad set is the block itself, and every inclusion-
   exclusion term containing it is settled by enumerating at most
   lam <= g - 1 positions -- so the only lattice term is the one
   pairwise intersection, and (C) reduces that to two floor-sums in
   O(log n) whether or not b is a unit mod n.

H3 AND THE LEVEL COUNT WAS NEVER THE RIGHT QUANTITY -- THE WIDTH IS.
   Containment lets a union forget a level, so a family of any size
   reduces to the maximal levels under (E)'s criterion, and (D) closes
   as soon as at most two survive. Over the same census the 662 classes
   carrying THREE or more lost levels -- the case S-B had to exclude,
   and 662 against 1684 is not a fringe -- reduce to width ONE at 662
   of 662, and the closed count on the reduced family equals the tree
   walk at 662 of 662. M5 never fired. Summed over both passes the
   width distribution across the whole census is {1: 2290, 2: 56} over
   2346 class tests -- and it is EXACT rather than an upper bound,
   though reduce_levels only tests shallower-inside-deeper: the reverse
   containment is measured and occurs at 0 of 1684, so no antichain is
   missed at width 2, and a bound of 1 is exact for the rest since no
   width is smaller. The reverse having no instances is not an accident
   of the census either -- |B_j| runs with 2 M_j + 1 and M_j grows with
   j, so a deeper level is the larger set and cannot sit inside a
   shallower one except by coincidence of the kappa factors -- so every one is closed, the three-level case
   never became a rank-3 count at any cell measured, and that 2290 is
   R-M's own agreement count arrived at by a different route: what it
   was measuring was width 1. What would leave the closed form is
   width 3, which this census does not contain.

H4 THE SUBSUMPTION CRITERION IS EXACT, AND IT EXPLAINS R-M'S SPLIT
   EXACTLY. |eps| <= a r_{j2-j1} agrees with measured set containment
   at 1684 of 1684 classes, 1628 contained and 56 not, with ZERO errors
   in either direction. M3 never fired. (Superseded in scope by
   explore_slope_width.py: the forward half is a property and holds
   with no counterexample at a census 400 times wider, but the converse
   FAILS at 284 pairs above N = 3000, always declining a containment
   that holds. "Exact" is a statement about this census.) The 56 are precisely R-M's 56
   class tests where the deepest lost level alone is strictly larger
   than the intersection -- so that measurement was never about a
   census shortfall or about a special cell; it is this O(1) inequality
   failing, and where it holds the assembly collapses to ONE level and
   the pair term is not computed at all.

H5 THE PAIR TERM IS NEVER EMPTY AND USUALLY EVERYTHING. (Superseded
   in scope by explore_slope_width.py, where empty pairs are ordinary
   above this census's N cap and are what keeps the closed form correct
   at width 3.) |B_i cap B_j|
   is non-empty at 1684 of 1684 two-lost-level classes -- the two
   levels always share states -- and at 1628 of them the intersection
   IS the shallower set entire, which is H4 read as a count. The
   largest recorded is 17 against factors 17 and 49 at
   (b,a,c,u,v) = (2,8,3,488,65). A term that is never empty and almost
   always total is the opposite of an obstruction.

H6 TWO CORRECTIONS TO THE RECORD THIS FILE INHERITED. First, the 56
   non-collapsing classes do NOT all sit at (4,2,3,448,25): they sit at
   four cells -- (4,2,3,448,25) and (4,2,3,512,29) with 24 each,
   (6,4,3,248,3) and (6,4,4,496,1) with 4 each. R-M printed its first
   three examples and its finding read that truncated list as the
   population; explore_slope_twolevel.py's G7 is corrected to match.
   All four do carry fractional rho, 4/3 and 8/5. Second, fractional
   rho is NOT what distinguishes them by way of lam: lam = 1 at every
   binding level of every class of this census, 7072 at integer rho and
   610 at fractional -- and lam = 1 is FORCED rather than measured, a
   cell with deficit >= g having no saturated class at all
   (explore_slope_width.py (F)), so there was no discriminator to hunt
   -- and (4,2,3,448,25) carries deficit 63 against
   g - 1 = 63 despite rho = 4/3 -- G4's deficit law is sufficient for
   lam = 1 and not necessary. Nothing in the assembly turns on rho; the
   discriminator is |eps| against a r_Delta and nothing else.

H7 THE FRONTIER THAT REPLACES (T). Three-lost-level classes are
   ordinary rather than exotic -- 68 cells carry one over S-F's sweep,
   and the smallest by N there sits at N = 272,
   (b,a,c,u,v) = (2,1,4,144,17), g = 16, n = 17, J = 4, whose class 1
   binds at levels 0, 1, 2 and 3. Both numbers are the SWEEP's and not
   the object's: N <= 6000 at radices to 12, digit sets to a = 8,
   lookahead to 8, slopes u to 600 over v to 80, phase 0 -- and the cap
   that hid the two-level case from every census before it was the
   slope numerator inside exactly such a list, so "the smallest" is a
   statement about this scope until a wider one agrees. But
   level count is not what opens the case (H3). What is open is a class
   of containment WIDTH 3, where inclusion-exclusion needs
   |B_i cap B_j cap B_k| with no level-0 factor in it: three runs under
   three multipliers, a rank-3 lattice count with no Euclidean descent.
   No cell of this census has one, so the width-3 case is the object to
   hunt next and it is not known to be inhabited.

VERDICT, by piece.
  - THE LEVEL FAMILY (A) -- every level including level 0 is one run
    condition b^j s + c_j in D_j -- is a PROPERTY: it follows from
    w_tree's own definition by reduction mod g, for every radix,
    symmetric redundant digit set, rational slope and phase. Checked
    5386/5386, which is a check on the derivation and not evidence for
    it.
  - THE PAIR COUNT (C) is a PROPERTY: b^j w is a function of b^i w
    whether or not b is invertible, the kappa-reduction is exact, and
    the floor-sum identity is exact. Checked 3766/3766 against a walk.
  - THE ASSEMBLY (D) is a RULE at the scope measured -- |W_t| closed,
    2346 of 2346 class tests over the 219 two-level cells with
    N <= 3000, no walk over the interval anywhere in it. It is a
    PROPERTY conditional on width <= 2, which is the honest split: the
    formula is derived, its APPLICABILITY at every class measured is
    not.
  - THE SUBSUMPTION CRITERION (E) splits, and the halves do not share
    a tier. Under lam = 1 at both levels, |eps| <= a r_Delta IMPLIES
    containment as a PROPERTY -- it follows from the arithmetic, all
    cases, nothing asked about which residues b^i reaches. The
    CONVERSE is a RULE at the scope measured, 1684 of 1684 classes
    below N = 3000 with no disagreement: its endpoint argument needs
    b^i onto the run, which gcd(b^i, n) > 1 denies at ordinary cells
    here. (That scope line is short two qualifiers, both load-bearing
    and both measured by explore_slope_width.py: it is PHASE 0, where
    off it the converse already fails at N = 1160, and it is classes
    with exactly TWO lost levels, which is all this census tested --
    every one of the 284 failures found above sits in a class with
    three or more.) The closed count uses the property half only, so H2 and H3
    do not rest on the rule half. The lam > 1 form is not derived at
    all and this census never needed it.

RUN RECORD: pure Python, integers only, standard library;
explore_slope_tree.py's cell, w_tree and interval, dodge's bblock and
floor_sum, and twolevel's below_counts imported rather than copied, so
every control reads the same code path the comparison does. 6.0 s wall
against a ~60 s estimate, peak working set 15.0 MB against the 512 MB
analysis ceiling (memwatch.py). The census is every two-level cell with
N <= 3000 (R-M's scope, so the two are comparable cell for cell) plus
an N <= 6000 sweep for the three-level frontier. Prints reproduced by:
python prime/code/explore_slope_assemble.py
"""

import os
import sys
from math import gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_slope_tree import (  # noqa: E402
    cell, params, interval, depth_J, repunit, w_tree,
)
from explore_slope_dodge import bblock, floor_sum  # noqa: E402
from explore_slope_twolevel import (  # noqa: E402
    below_counts, preperiod_ceiling,
)

FAILURES = []


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


# --------------------------------------------------- (B) runs in Z/n
# A run is (start, length) with 0 <= start < n and 1 <= length <= n,
# read cyclically. norm_runs returns disjoint runs sorted by start.


def norm_runs(runs, n):
    """Merge a list of cyclic runs into disjoint ones, sorted."""
    runs = [(s % n, ln) for s, ln in runs if ln > 0]
    if not runs:
        return []
    if any(ln >= n for _, ln in runs):
        return [(0, n)]
    # split each wrapping run at 0, then sweep as intervals of [0, n)
    flat = []
    for s, ln in runs:
        if s + ln <= n:
            flat.append((s, s + ln))
        else:
            flat.append((s, n))
            flat.append((0, s + ln - n))
    flat.sort()
    merged = []
    for lo, hi in flat:
        if merged and lo <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], hi)
        else:
            merged.append([lo, hi])
    # close the seam at 0 if both ends are covered
    if len(merged) > 1 and merged[0][0] == 0 and merged[-1][1] == n:
        lo, hi = merged.pop(0)
        merged[-1][1] = n + hi
    out = [(lo % n, hi - lo) for lo, hi in merged]
    if len(out) == 1 and out[0][1] >= n:
        return [(0, n)]
    return sorted(out)


def d_runs(n, sigma_inv, M, lam):
    """(B): D'_j = [-M, M] + sigma^{-1} [0, lam) as disjoint runs."""
    if lam <= 0:
        return []
    return norm_runs([((-M + sigma_inv * i) % n, 2 * M + 1)
                      for i in range(lam)], n)


def mask_of(runs, n):
    mk = bytearray(n)
    for s, ln in runs:
        for i in range(ln):
            mk[(s + i) % n] = 1
    return mk


# ------------------------------------- (C)/(D) the closed counts

def count_single(n, mult, e, runs):
    """#{w in Z/n : (mult w + e) mod n in runs}. The values hit one
    coset of kappa Z, each kappa times."""
    mult %= n
    kappa = gcd(mult, n) if mult else n
    tot = 0
    for s, ln in runs:
        # elements x of the run with x congruent to e mod kappa: the
        # run is s, s+1, ..., s+ln-1, so the offset solves s + i = e
        lo = (e - s) % kappa
        tot += (ln - lo + kappa - 1) // kappa if ln > lo else 0
    return kappa * tot


def _run_pullback(n, kappa, e, s, ln):
    """Condition (kappa*y + e) mod n in run (s, ln), as a run of y in
    Z/(n/kappa)."""
    n2 = n // kappa
    S = (s - e) % n
    a0 = -(-S // kappa)                      # ceil(S / kappa)
    a1 = -(-(S + ln) // kappa)
    return (a0 % n2, min(a1 - a0, n2))


def count_pair_runs(n, mi, delta_mult, ei, ri, ej, rj):
    """(C): #{w : (mi w + ei) mod n in run ri, (mj w + ej) mod n in run
    rj}, where mj = delta_mult * mi. delta_mult is b^Delta mod n."""
    mi %= n
    kappa = gcd(mi, n) if mi else n
    n2 = n // kappa
    si, li = _run_pullback(n, kappa, ei, ri[0], ri[1])
    sj, lj = _run_pullback(n, kappa, ej, rj[0], rj[1])
    if li <= 0 or lj <= 0:
        return 0
    if lj >= n2:
        return kappa * li
    dm = delta_mult % n2
    C = (dm * si - sj) % n2
    hits = (floor_sum(li, n2, dm, C) - floor_sum(li, n2, dm, C - lj))
    return kappa * hits


def count_pair(n, mi, delta_mult, ei, runs_i, ej, runs_j):
    return sum(count_pair_runs(n, mi, delta_mult, ei, ri, ej, rj)
               for ri in runs_i for rj in runs_j)


def in_runs(x, runs, n):
    x %= n
    return any(((x - s) % n) < ln for s, ln in runs)


# ------------------------------------------- (A) the per-level data

def level_data(b, a, ce, t):
    """Lambda for class t: per level j in [0, J), the multiplier b^j
    mod n, the offset d_j, the runs D'_j, and lam_j. Levels with
    lam_j = 0 are dropped."""
    N, g, n, J = ce["N"], ce["g"], ce["n"], ce["J"]
    phi, f, q = ce["phi"], ce["f"], ce["q"]
    sigma_inv = pow((q // g) % n, -1, n)
    out, tj = [], t
    for j in range(J):
        if j:
            tj = f(tj)
        rj = repunit(b, j)
        beta, lam = bblock(N, g, n, ce["span"], ce["hi"], tj)
        if lam == 0:
            continue
        M = a * rj
        h = ((b ** j * t - (b - 1) * phi * rj - tj) % N) // g
        c = (h - beta) % n
        out.append({"j": j, "mult": pow(b, j, n), "d": (sigma_inv * c) % n,
                    "runs": d_runs(n, sigma_inv, M, lam), "lam": lam,
                    "M": M, "tj": tj})
    return out, sigma_inv


def w_count_closed(b, ce, lv):
    """(D): |W_t| by inclusion-exclusion, for a family of containment
    width at most 2. Beyond that the term |B_i cap B_j cap B_k| has no
    level-0 factor to enumerate and no closed form here, so this
    REFUSES rather than returning a plausible number: the caller is
    hunting width 3 and a silent wrong count is the trap."""
    n = ce["n"]
    zero = [x for x in lv if x["j"] == 0]
    deep = [x for x in lv if x["j"] > 0]
    if len(deep) > 2:
        raise ValueError(f"width {len(deep)} exceeds the closed form's 2")
    tot = n
    for x in lv:
        tot -= count_single(n, x["mult"], x["d"], x["runs"])
    for i in range(len(deep)):
        for k in range(i + 1, len(deep)):
            A, C = deep[i], deep[k]
            dm = pow(b, C["j"] - A["j"], n)
            tot += count_pair(n, A["mult"], dm, A["d"], A["runs"],
                              C["d"], C["runs"])
    if zero:
        z = zero[0]
        # B_0 enumerated: multiplier b^0 = 1, so it is D'_0 translated
        # by -d_0 and reads off the runs directly -- lam elements, no
        # scan of Z/n, which is what makes (D)'s level-0 terms O(lam)
        pts = [(s + i - z["d"]) % n
               for (s, ln) in z["runs"] for i in range(ln)]
        for r in range(1, len(deep) + 1):
            # the term is B_0 with r deep levels, so |S| = r + 1 and it
            # enters n - |union| with sign (-1)^(r+1)
            sign = 1 if r % 2 else -1
            for combo in _combos(deep, r):
                hit = sum(1 for w in pts
                          if all(in_runs(x["mult"] * w + x["d"], x["runs"], n)
                                 for x in combo))
                tot += sign * hit
    return tot


def _combos(seq, r):
    if r == 0:
        yield []
        return
    for i in range(len(seq) - r + 1):
        for rest in _combos(seq[i + 1:], r - 1):
            yield [seq[i]] + rest


def subsumes(b, a, n, A, C):
    """(E): is B_A contained in B_C? Only valid at lam = 1 on both,
    and only for A shallower than C."""
    delta = C["j"] - A["j"]
    eps = (C["d"] - pow(b, delta, n) * A["d"]) % n
    if eps > n // 2:
        eps -= n
    return abs(eps) <= a * repunit(b, delta)


def reduce_levels(b, a, n, deep):
    """(S-G): drop every lost level contained in a deeper one. Returns
    the maximal levels, or None if any lam > 1 puts the criterion out
    of its proved scope."""
    if any(x["lam"] != 1 for x in deep):
        return None
    keep = []
    for i, A in enumerate(deep):
        if any(subsumes(b, a, n, A, C) for k, C in enumerate(deep) if k > i):
            continue
        keep.append(A)
    return keep


# --------------------------------------------------- the cell sweeps

def two_level_cells(cap, min_below=2):
    """Every cell with N <= cap carrying a deep-saturated class of
    below-count >= min_below. R-L's scope."""
    out = []
    for b in range(2, 13):
        for a in range(1, 9):
            if 2 * a + 1 < b:
                continue
            for v in range(1, 81):
                for c in range(1, 9):
                    if v * b ** c > cap:
                        break
                    for u in range(1, 601):
                        if gcd(u, v) != 1:
                            continue
                        L, phi, N, q, g = params(b, a, c, u, v, 0, 1)
                        if gcd(b, g) == 1:
                            continue
                        lo, hi, span, _ = interval(b, a, c, u, v, 0, 1)
                        if lo > hi or span > N:
                            continue
                        if not (0 < N - span < g):
                            continue
                        n = N // g
                        if depth_J(b, a, n) < 3:
                            continue
                        if preperiod_ceiling(b, g) < min_below + 1:
                            continue
                        ce = cell(b, a, c, u, v, 0, 1)
                        cnt, _ = below_counts(ce)
                        two = sorted(t for t, k in cnt.items()
                                     if k >= min_below)
                        if two:
                            out.append((N, (b, a, c, u, v), ce, two))
    out.sort(key=lambda r: (r[0], r[1]))
    return out


def rho_is_int(b, a):
    return (2 * a) % (b - 1) == 0


# ------------------------------------------------------------- passes

def s_a_controls(cells):
    print("S-A  THE CONTROLS")
    pairs = lvl = 0
    for N, key, ce, two in cells:
        b, a, c, u, v = key
        W, star, bad = w_tree(b, a, c, u, v, ce, 0, 1)
        g, n = ce["g"], ce["n"]
        for t in two:
            lv, sinv = level_data(b, a, ce, t)
            cls = [m for m in range(ce["lo"], ce["hi"] + 1) if m % g == t]
            for x in lv:
                # closed run decomposition against a direct mask build
                direct = bytearray(n)
                for i in range(x["lam"]):
                    for y in range(-x["M"], x["M"] + 1):
                        direct[(-x["M"] + sinv * i + (y + x["M"])) % n] = 1
                ok(bytes(mask_of(x["runs"], n)) == bytes(direct),
                   f"run decomposition {key} t={t} j={x['j']}")
                if x["j"] == 0:
                    continue
                got = {m for m in cls
                       if in_runs(x["mult"] * (sinv * ((m - t) // g)) + x["d"],
                                  x["runs"], n)}
                want = {m for m in cls if m in bad[x["j"]]}
                ok(got == want, f"level law {key} t={t} j={x['j']}")
                lvl += 1
            deep = [x for x in lv if x["j"] > 0]
            for i in range(len(deep)):
                for k in range(i + 1, len(deep)):
                    A, C = deep[i], deep[k]
                    dm = pow(b, C["j"] - A["j"], n)
                    got = count_pair(n, A["mult"], dm, A["d"], A["runs"],
                                     C["d"], C["runs"])
                    want = sum(1 for w in range(n)
                               if in_runs(A["mult"] * w + A["d"], A["runs"], n)
                               and in_runs(C["mult"] * w + C["d"],
                                           C["runs"], n))
                    ok(got == want, f"pair count {key} t={t} "
                                    f"j={A['j']},{C['j']}: {got} vs {want}")
                    pairs += 1
            for x in lv:
                got = count_single(n, x["mult"], x["d"], x["runs"])
                want = sum(1 for w in range(n)
                           if in_runs(x["mult"] * w + x["d"], x["runs"], n))
                ok(got == want, f"single count {key} t={t} j={x['j']}")
    print(f"  level law against the tree's own bad sets: {lvl} (cell, "
          f"level, class) triples")
    print(f"  pair counts against a direct walk: {pairs}")
    wce = cell(2, 1, 3, 40, 9, 0, 1)
    W, star, _ = w_tree(2, 1, 3, 40, 9, wce, 0, 1)
    print(f"  the witness through the imported path: |W| = {len(W)}, "
          f"|W*| = {len(star)}")
    ok(len(W) == 37 and len(star) == 17, "witness headline")
    print(f"  control failures: {len(FAILURES)}")


def s_b_closed(cells):
    print("S-B  THE CLOSED COUNT AGAINST THE TREE WALK")
    agree = dis = classes = 0
    three = []
    seen_cells = set()
    firstbad = None
    for N, key, ce, two in cells:
        b, a, c, u, v = key
        W, _, _ = w_tree(b, a, c, u, v, ce, 0, 1)
        g = ce["g"]
        for t in two:
            lv, _ = level_data(b, a, ce, t)
            if len([x for x in lv if x["j"] > 0]) >= 3:
                three.append((key, t, [x["j"] for x in lv if x["j"] > 0]))
                continue
            got = w_count_closed(b, ce, lv)
            want = sum(1 for m in W if m % g == t)
            classes += 1
            seen_cells.add(key)
            if got == want:
                agree += 1
            else:
                dis += 1
                if firstbad is None:
                    firstbad = (key, t, got, want,
                                [x["j"] for x in lv])
    print(f"  two-level cells read: {len(cells)}; classes counted: "
          f"{classes} over {len(seen_cells)} cells")
    print(f"  closed |W_t| equals the tree walk's: {agree}; differs: {dis}")
    if firstbad:
        print(f"    first disagreement {firstbad}")
    print(f"  classes with three or more lost levels (M4, excluded): "
          f"{len(three)}")
    for e in three[:3]:
        print(f"    {e}")
    return agree, dis, three


def s_c_pairterm(cells):
    print("S-C  THE PAIR TERM ITSELF")
    empty = nonempty = 0
    sizes = []
    for N, key, ce, two in cells:
        b, a, c, u, v = key
        n = ce["n"]
        for t in two:
            lv, _ = level_data(b, a, ce, t)
            deep = [x for x in lv if x["j"] > 0]
            if len(deep) != 2:
                continue
            A, C = deep
            dm = pow(b, C["j"] - A["j"], n)
            val = count_pair(n, A["mult"], dm, A["d"], A["runs"],
                             C["d"], C["runs"])
            if val == 0:
                empty += 1
            else:
                nonempty += 1
                sizes.append((val, count_single(n, A["mult"], A["d"],
                                                A["runs"]),
                              count_single(n, C["mult"], C["d"], C["runs"]),
                              key, t))
    print(f"  two-lost-level classes: {empty + nonempty}; pairwise "
          f"intersection EMPTY at {empty}, non-empty at {nonempty}")
    if sizes:
        sizes.sort(reverse=True)
        print(f"    largest: |B_i cap B_j| = {sizes[0][0]} against "
              f"|B_i| = {sizes[0][1]}, |B_j| = {sizes[0][2]} at "
              f"{sizes[0][3]} class {sizes[0][4]}")
    return empty, nonempty


def s_d_subsumption(cells):
    print("S-D  THE SUBSUMPTION CRITERION")
    conf = {(True, True): 0, (True, False): 0,
            (False, True): 0, (False, False): 0}
    skipped = collapse = tested = 0
    where, reverse = {}, [0]
    for N, key, ce, two in cells:
        b, a, c, u, v = key
        n = ce["n"]
        for t in two:
            lv, _ = level_data(b, a, ce, t)
            deep = [x for x in lv if x["j"] > 0]
            if len(deep) != 2:
                continue
            A, C = deep
            if A["lam"] != 1 or C["lam"] != 1:
                skipped += 1
                continue
            delta = C["j"] - A["j"]
            eps = (C["d"] - pow(b, delta, n) * A["d"]) % n
            if eps > n // 2:
                eps -= n
            pred = abs(eps) <= a * repunit(b, delta)
            setA = {w for w in range(n)
                    if in_runs(A["mult"] * w + A["d"], A["runs"], n)}
            setC = {w for w in range(n)
                    if in_runs(C["mult"] * w + C["d"], C["runs"], n)}
            meas = setA <= setC
            # the reduction only tests SHALLOWER inside DEEPER, so the
            # count it calls a width is an upper bound until the other
            # direction is measured too
            if setC <= setA:
                reverse[0] += 1
            conf[(pred, meas)] += 1
            tested += 1
            if meas:
                collapse += 1
            else:
                where[key] = where.get(key, 0) + 1
    print(f"  classes with lam = 1 at both lost levels: {tested}; "
          f"skipped for lam > 1: {skipped}")
    print(f"  criterion vs measured containment: "
          f"both true {conf[(True, True)]}, both false "
          f"{conf[(False, False)]}, criterion says yes and it is no "
          f"{conf[(True, False)]}, criterion says no and it is yes "
          f"{conf[(False, True)]}")
    print(f"  shallower level subsumed by the deeper (assembly collapses "
          f"to one level): {collapse} of {tested}")
    print(f"  the classes it does NOT collapse, by cell: "
          f"{dict(sorted(where.items()))}")
    print(f"  the REVERSE containment, deeper inside shallower, which "
          f"the reduction never tests: {reverse[0]} of {tested}")
    return {1: collapse, 2: tested - collapse}


def s_e_lam(cells):
    print("S-E  THE lam CENSUS, INTEGER rho AGAINST FRACTIONAL")
    dist = {True: {}, False: {}}
    for N, key, ce, two in cells:
        b, a, c, u, v = key
        r = rho_is_int(b, a)
        for t in two:
            lv, _ = level_data(b, a, ce, t)
            for x in lv:
                dist[r][x["lam"]] = dist[r].get(x["lam"], 0) + 1
    for r in (True, False):
        lab = "integer" if r else "fractional"
        print(f"  rho {lab}: lam distribution over binding levels "
              f"{dict(sorted(dist[r].items()))}")
    # the cell R-M's disagreements all sit at, read explicitly
    key = (4, 2, 3, 448, 25)
    ce = cell(*key, 0, 1)
    if ce is None:
        print(f"  {key}: no cell")
        return dist
    cnt, _ = below_counts(ce)
    two = sorted(t for t, k in cnt.items() if k >= 2)
    lams = set()
    for t in two:
        lv, _ = level_data(4, 2, ce, t)
        lams |= {x["lam"] for x in lv}
    print(f"  {key}: N = {ce['N']}, g = {ce['g']}, n = {ce['n']}, "
          f"J = {ce['J']}, rho = {2 * 2}/{4 - 1}, deficit "
          f"{ce['N'] - ce['span']} against g - 1 = {ce['g'] - 1}, "
          f"two-level classes {len(two)}, lam values on binding levels "
          f"{sorted(lams)}")
    return dist


def s_f_three(cap=6000):
    print("S-F  THE THREE-LEVEL FRONTIER")
    found = two_level_cells(cap, min_below=3)
    print(f"  cells with N <= {cap} carrying a class of below-count "
          f">= 3: {len(found)}")
    for N, key, ce, two in found[:3]:
        t = two[0]
        lv, _ = level_data(key[0], key[1], ce, t)
        print(f"    N={N} (b,a,c,u,v)={key} g={ce['g']} n={ce['n']} "
              f"J={ce['J']} class {t} binding levels "
              f"{[x['j'] for x in lv]}")
    return found


def s_g_width(cells):
    print("S-G  THE WIDTH OF THE CONTAINMENT ORDER, NOT THE LEVEL COUNT")
    widths, agree, dis, skipped = {}, 0, 0, 0
    firstbad = None
    for N, key, ce, two in cells:
        b, a, c, u, v = key
        n, g = ce["n"], ce["g"]
        W = None
        for t in two:
            lv, _ = level_data(b, a, ce, t)
            deep = [x for x in lv if x["j"] > 0]
            if len(deep) < 3:
                continue
            keep = reduce_levels(b, a, n, deep)
            if keep is None:
                skipped += 1
                continue
            wd = len(keep)
            widths[wd] = widths.get(wd, 0) + 1
            if wd > 2:
                continue
            if W is None:
                W, _, _ = w_tree(b, a, c, u, v, ce, 0, 1)
            got = w_count_closed(b, ce, [x for x in lv if x["j"] == 0] + keep)
            want = sum(1 for m in W if m % g == t)
            if got == want:
                agree += 1
            else:
                dis += 1
                if firstbad is None:
                    firstbad = (key, t, [x["j"] for x in deep],
                                [x["j"] for x in keep], got, want)
    tot = sum(widths.values())
    print(f"  classes with three or more lost levels: {tot}; excluded for "
          f"lam > 1: {skipped}")
    print(f"  surviving width after the criterion: "
          f"{dict(sorted(widths.items()))}")
    print(f"  closed |W_t| on the reduced family equals the tree walk's: "
          f"{agree}; differs: {dis}")
    if firstbad:
        print(f"    first disagreement {firstbad}")
    return widths, agree, dis


def main():
    cells = two_level_cells(3000)
    s_a_controls(cells)
    if FAILURES:
        print(f"\nCONTROL FAILURES: {len(FAILURES)} -- nothing below read")
        return
    print()
    s_b_closed(cells)
    print()
    s_c_pairterm(cells)
    print()
    w2 = s_d_subsumption(cells)
    print()
    s_e_lam(cells)
    print()
    s_f_three()
    print()
    w3, _, _ = s_g_width(cells)
    total = dict(w2)
    for k, val in w3.items():
        total[k] = total.get(k, 0) + val
    print(f"\n  containment width over the WHOLE census, both passes "
          f"summed: {dict(sorted(total.items()))} over "
          f"{sum(total.values())} class tests")
    print(f"\nfailures: {len(FAILURES)}")


if __name__ == "__main__":
    main()
