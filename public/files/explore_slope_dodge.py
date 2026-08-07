"""The tree condition below depth J, in closed form: three distances,
one block, and the gap that decides whether a state can dodge.

THE QUESTION. explore_slope_tree.py proved that a state wins the
residual safety game iff its reachable tree misses the interval's
complement B at every depth, for every radix, symmetric redundant digit
set, rational slope and phase. That is a TEST. From depth J on the tree
is a full coset and the description is already closed -- saturation of a
class. Below J it is a proper sub-progression and the only description
on offer is "run the test". This asks for the DESCRIPTION: which
residues survive level j, as a formula in (b, a, j, n, the unit q/g, and
B's block inside a class), with no scan over the interval. The parent
rig measured two things a description must explain -- that all 19 of its
counterexamples sit at the redundancy floor 2a+1 <= b+1, and that every
one of them dodges at level 1 -- and it explained neither.

THE DERIVATION, hand-attacked on paper before this engine existed.
Notation is explore_slope_tree.py's: N = L b^c, q = L u / v,
g = gcd(q, N), n = N/g, I = [lo, hi] the derived interval of length
span <= N, B = Z/N \\ pi(I), A the saturated classes, f(t) = b t + kappa
the class map, r_j the repunit, J the depth at which the digit sums
cover the subgroup, and T_j(m) = b^j m - (b-1) phi r_j + q [-a r_j,
a r_j] the reachable tree.

(N) THE SUBGROUP COORDINATE. For m in I write t = m mod g and
S = (m - t)/g, s = S mod n; the pair (t, s) determines m on I because
span <= N = g n. Then b^j m = b^j t + g b^j S and g b^j S mod g n =
g (b^j s mod n), so with e_j = b^j t - (b-1) phi r_j mod N,

    c_j(m) := b^j m - (b-1) phi r_j = e_j + g (b^j s mod n)  (mod N).

Now e_j mod g = f^j(t), so writing t_j = f^j(t) and e_j = t_j + g
gamma_j, the level-j tree centre sits in CLASS t_j at POSITION

    s_j = b^j s + gamma_j   (mod n).

The class is a function of m mod g -- which is all the saturation
criterion ever read -- and the position is affine in s with multiplier
b^j, which is the coordinate the criterion has no word for.

(O) THE TREE IS A UNIT MULTIPLE OF A CENTRED INTERVAL. q = g sigma with
sigma = (q/g) a unit of Z/n, so T_j(m) is class t_j at positions
s_j + sigma [-M_j, M_j] with M_j = a r_j, and below J we have
2 M_j + 1 < n by the definition of J.

(P) B INSIDE A CLASS IS ONE BLOCK. B is the cyclic interval of
N - span residues complementary to pi(I), and s |-> t + g s is order
preserving and wraps the circle once, so B intersect class t is a cyclic
block of positions [beta_t, beta_t + lam_t - 1] -- and lam_t = 0 exactly
when t is saturated. Closed, in O(1): with B0 = (hi + 1) mod N,
lamB = N - span, A0 = (t - B0) mod N and a0 = A0 mod g, lam_t = 0 if
a0 >= lamB else (lamB - 1 - a0)//g + 1, and beta_t = ((a0 - A0)/g) mod n.

(Q) THE LEVEL LAW. Putting (N)-(P) together, m FAILS level j exactly
when, with d = (s_j - beta_{t_j}) mod n,

    d in [0, lam - 1] + sigma [-M_j, M_j]   (mod n),

the sumset of a block of length lam with the point set
P_j = sigma [-M_j, M_j], which is a translate of {0, sigma, ...,
K sigma}, K = 2 M_j. So the bad set is 2 M_j + 1 blocks of length lam
hung on P_j, and the SURVIVOR set is one interval per gap of P_j strictly
longer than lam: the interval starting lam past that gap's left point, of
length gap - lam. That is the description asked for -- at most 2 a r_j + 1
intervals, positions and lengths explicit, no reference to I at all.

(R) THREE DISTANCES MAKE IT A FORMULA. The gaps of {0, sigma, ...,
K sigma} in Z/n take at most three lengths, obtainable by the subtractive
continued fraction: p, L = 1, sigma; q', R = 1, n - sigma; while
p + q' <= K, replace (p, L) by (p+q', L-R) if L > R and else (q', R) by
(p+q', R-L). The gap multiset is then L with multiplicity K+1-p, R with
K+1-q', and L+R with p+q'-K-1, and p R + q' L = n. Hence the count of
survivors in a full class is

    n - sum_i min(gap_i, lam),

a formula in (b, a, j, n, sigma, lam) evaluated in O(log n).

(S) THE DODGE CRITERION, AND WHY IT PREDICTS BOTH MEASURED FACTS.
A position dodges at level j iff the LARGEST gap of P_j exceeds lam.
Max gap is non-increasing in K, and K = 2 a r_j grows with a and with j.
So the narrowest digit set gives the widest gap and dodges most easily
-- which is the redundancy floor the parent rig saw and could not
explain -- and level 1 is the easiest level of all, which is why every
counterexample it found dodges there. One monotonicity, two facts.

(T) WHERE THE CLOSED FORM STOPS, STATED HONESTLY. W below J is the
intersection over j < J of the pullbacks of these interval unions along
s |-> b^j s + gamma_j. Different levels carry different multipliers, so
in a common coordinate the pullbacks are arithmetic progressions rather
than intervals and do not collapse into one description. At J = 2 there
is a single level and the count IS closed: each survivor interval
receives a floor-sum count of an arithmetic progression, O(a log n) per
class and independent of span. Above J = 2 the levels are each closed
and the assembly walks the class.

THE DESIGN, frozen before the engine.

Q-A THE CONTROLS, three of them, all against brute force rather than
    against a claim. The three-distance gap multiset against a direct
    sort of the points; the block (beta, lam) against a direct scan of
    the class; and the floor-sum against a direct sum. Plus the parent
    rig's headline reproduced through the imported code path: 53
    residual cells read at N <= 4000, 19 of them with W* != W.
Q-B THE LEVEL LAW IS EXACT. At every residual cell read and every level
    j < J, the set of m in I that (Q) says fails level j equals
    explore_slope_tree.py's bad[j], which is computed from the tree
    directly. Reported as a cell/level count, not an aggregate.
Q-C THE COUNT FORMULA IS EXACT. At every (cell, level, class) with
    lam > 0, n - sum min(gap, lam) equals the size of the survivor
    interval union from (Q).
Q-D W REPRODUCED FROM THE DESCRIPTION. At every residual cell read, the
    W assembled from the closed level descriptions equals
    explore_slope_tree.py's W. This is the first of the two ways to know
    the closed form landed.
Q-E THE PREDICTION. The dodge criterion (S) gives a per-cell predicate
    with no reference to W: some class t deep-saturated, carrying at
    least one unsaturated level below J, and every one of its
    unsaturated levels having max gap > lam there. It is NECESSARY by
    construction. Report predicted-mismatch against measured-mismatch as
    a confusion count over all cells read, and for each predicted cell
    the predicted EXCESS -- how many more states W holds than W* -- for
    the cells where a prediction of the size is available (one
    unsaturated level, from the count formula) against the measured
    excess. This is the second of the two ways.
Q-F THE DIAL, MEASURED. For each residual cell read, the max gap at
    level 1 against the max gap at each deeper level, and against the
    same cell's tree width. Report whether max gap is non-increasing in
    the level at every cell read, and whether every mismatch cell sits
    at the redundancy floor.
Q-G THE J = 2 CLOSED COUNT. At every residual cell with J = 2, |W| from
    the floor-sum formula against |W| from the walk. This is the only
    place the description becomes a count with no walk at all.
Q-H THE CAPS RAISED. The parent left 2 residual cells above N = 4000
    unread and 6673 feasibility cells above N = 20000 unread. Read the
    residual cells to N <= 500000 and report the census by depth and
    the mismatch tally over the whole of it. For feasibility, the
    closed form makes the sweep an argument rather than a scan -- the
    start class is a fixed point (F7 there), so
    every level reads the SAME class, and if it is saturated every tree
    is clean while if it is not, level J alone is a full coset and meets
    B -- so re-run the tree walk at the raised cap N <= 60000 with an
    O(1) interval membership in place of the parent's residue set, and
    report the widened count. Whether N <= 500000 reaches the two
    unread residual cells is not known here; the count left above the
    cap prints either way.

KILLS, frozen as what this rig PRINTS.

K1 A control misses -> the primitives are wrong and nothing below is
   read.
K2 A (cell, level) where (Q)'s failure set differs from the tree's ->
   the coordinate change (N) or the block reading (P) is wrong.
K3 A cell where the assembled W differs from the parent's W -> (T)'s
   assembly is wrong even though its pieces are not.
K4 A measured mismatch cell the criterion (S) predicts CLEAN -> the
   criterion is not necessary, which would refute the derivation rather
   than weaken the prediction.
K5 The criterion over-predicts: cells predicted to mismatch that do not.
   Not a kill -- the criterion is necessary by construction -- but the
   count is the measurement of how sharp it is, and a large over-count
   means the intersection across levels is doing the work rather than
   the gap.
K6 A J = 2 cell where the floor-sum count differs from the walk -> the
   only fully closed count in the file is wrong.
K7 A mismatch cell above the parent's cap sitting OFF the redundancy
   floor -> the floor reading was an artifact of the old scope, and (S)'s
   monotonicity is not the whole dial.

POSITIVE CONTROL, run and read before any verdict line: Q-A whole.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

G1 THE CONTROLS HOLD. The three-distance gap multiset matches a direct
   sort of the points at every (n < 60, unit sigma, K < n-1); floor_sum
   matches a direct sum at 300/300; the block (beta, lam) matches a
   direct scan of every class at every residual cell, with lam = 0
   falling exactly on the saturated classes; and the parent's headline
   reproduces through this path -- 53 residual cells at N <= 4000, 2
   larger, 19 with W* != W. K1 never fired.

G2 THE LEVEL LAW IS EXACT. At 112/112 (cell, level) pairs below J, the
   set of states (Q) says fails level j IS the tree's own failure set.
   The subgroup coordinate is therefore the right one: the class is
   f^j(m mod g) and the position is b^j s + gamma_j, and B inside a
   class is one block. K2 never fired. The three-distance count equals
   the size of the survivor interval union at 977/977 (pair, unsaturated
   class), so (R) is a formula and not an estimate.

G3 THE DESCRIPTION REBUILDS THE WINNING SET. W assembled from the
   closed level descriptions equals the tree's W at 53/53 cells, which
   is the first of the two ways this had to land. And at the 25 cells
   with J = 2 -- one level, so (T)'s obstruction is absent -- the
   floor-sum gives |W| with NO walk over the interval at all, 25/25.
   K3 and K6 never fired.

G4 THE CRITERION IS NECESSARY, THE COUNT IS EXACT, AND THE GAP BETWEEN
   THEM IS THE INTERVAL. The dodge criterion (S) predicts every one of
   the 19 mismatches with nothing but max gap against lam: 19 caught, 0
   missed, K4 never fired. It over-calls 3, all at J = 2 (K5). The
   count then closes that gap and is the second way this had to land:
   the excess formula is AVAILABLE at 53/53 -- every deep-saturated
   class turns out to carry at most ONE unsaturated level below J, so
   there is nothing to intersect -- and it is EXACT at 53/53, giving
   |W| - |W*| as a number in advance. Its sign is the verdict at 53/53,
   the 3 over-calls coming back as excess exactly 0. The two disagree
   for a reason with a name: the criterion asks whether the FULL class
   holds a dodging position, the count asks how many lie in the range
   the interval actually gives that class, and at those 3 cells the
   range misses every one of them.

G5 THE DIAL IS ONE MONOTONICITY. P_j grows with j and with a, and a
   larger point set only SUBDIVIDES gaps, so max gap is non-increasing
   in both -- measured non-increasing in the level at 55/55, the
   complete census. That is why the mismatches sit where they do: all
   21 at the redundancy floor 2a+1 <= b+1, the narrowest tree and so the
   widest gap; and at 21 of 21, EVERY extra state's unsaturated level is
   1 -- level 1 is the only level carrying an extra state anywhere in
   the census, which is stronger than the parent's reading that the
   first such level is 1. The parent measured the floor and the level
   and could explain neither; they are the same fact about a nested
   family of point sets.

G6 THE RESIDUAL CENSUS IS NOW READ TO ITS LAST CELL -- of the parent's
   wide scope, which is what "complete" means here and nothing wider:
   radices to 12, digit sets to a = 8, slopes to 12/12, lookahead to 5.
   All 55 cells of it read, 0 left above the cap. The 2 the parent
   could not reach are BOTH mismatches, both
   predicted, and both sized exactly: (5,2) slope 5/3 phase 3/5 at
   c = 4 has |W| = 9271 against |W*| = 1871, excess predicted 7400
   against 7400 measured, and at c = 5, |W| = 46771 against 9371,
   excess predicted 37400 against 37400. So the tally over the complete
   census is 21 of 55, both new cells at the redundancy floor. And the
   floor stays where to LOOK rather than a test: 52 of the 55 sit at it,
   so it separates nothing on its own -- the widest gap against lam
   does. K7 never fired.

G7 AND THE FEASIBILITY SWEEP IS NOW AN ARGUMENT. Widened from the
   parent's 6984 cells to 7197 at N <= 60000 with the O(1) membership,
   zero disagreements. But the closed form retires the sweep rather
   than extending it: the start class is a fixed point, so every level
   reads the SAME class and therefore the same lam. Saturated gives
   lam = 0 at every level and every tree is clean; unsaturated leaves
   level J a full coset, which meets B. No dodging is available to the
   start state at any depth, and no cell count is doing any work.

VERDICT, by piece.
  - THE LEVEL LAW (Q) is a PROPERTY: it follows from the construction
    by (N)-(P), for every radix, symmetric redundant digit set,
    rational slope and phase. Checked 112/112, which is a check on the
    derivation and not evidence for it.
  - THE COUNT (R) splits in two and the halves do not share a tier.
    The identity -- survivor total in a full class = n - sum
    min(gap_i, lam) -- is a PROPERTY: it follows from the interval
    decomposition, all cases, no computation, checked 977/977. The
    subtractive recursion that DELIVERS the gaps is the classical
    three-distance structure, which this file verifies exhaustively at
    every (n < 60, unit sigma, K < n-1) rather than reproving, and so
    is a RULE over that range and not a proof.
  - THE DODGE CRITERION (S) is a CRITERION for a full class -- some
    position dodges iff max gap > lam -- and an over-calling necessary
    condition for a CELL, measured to over-call 3 of 53.
  - THE EXCESS FORMULA is PROVED under a hypothesis that is only an
    OBSERVATION: given that a class carries at most one unsaturated
    level below J, the floor-sum counts its dodging positions exactly
    and nothing is approximated. The hypothesis held at 55 of 55 cells
    and is not proved, so the pair is the honest tier and the formula
    alone is not. Above that hypothesis (T) bites and the
    levels must be intersected.
  - WHAT IS STILL OPEN is exactly (T): two unsaturated levels in one
    class would need the intersection of two arithmetic progressions
    of survivor intervals under different multipliers, and no cell of
    this census has one to look at.
    [SETTLED since by explore_slope_twolevel.py, as to EXISTENCE and not
    as to the assembly: such a class exists and is ordinary, 262
    witnesses sitting below N = 6000, the smallest at radix 2 with
    digits {-1, 0, 1}, slope 40/9 and lookahead 3. No widening of a
    census reaches one -- every sweep here and there caps the slope
    NUMERATOR, and the witness needs u = 40 at v = 9. What reaches it is
    a deficit law: wherever 2a/(b-1) is an integer, g divides the span
    deficit plus one, so a mismatch-capable cell has EXACTLY ONE
    saturated class. The hypothesis this file's OBSERVATION is
    conditioned on is therefore FALSE in general, and the surviving
    scope of the floor-sum pair is the one stated above it -- the 55
    cells of this census, where it is exact.]

RUN RECORD: pure Python, integers only, standard library; the parent
rig's cell, w_tree and wide_scope imported rather than copied, so the
control reads the same code path the comparison does. 0.8 s wall against
a ~120 s estimate -- the closed form is what makes it cheap, the parent
needing 27.8 s for a strictly smaller census -- peak working set 22.0 MB
against the 512 MB analysis ceiling (memwatch.py). The residual census
has no cells left unread; the feasibility check leaves 4376 wide-scope
keys above N = 60000, and that count prints. Prints reproduced by:
python prime/code/explore_slope_dodge.py
"""

import os
import sys
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_slope_tree import (  # noqa: E402
    cell, is_residual, orbit, repunit, rgame, w_tree, wide_scope,
)

FAILURES = []


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


# ------------------------------------------------- (R) the three gaps

def three_gaps(n, sigma, K):
    """(R): the gap multiset of {0, sigma, ..., K sigma} in Z/n, as
    [(length, multiplicity), ...], by the subtractive continued
    fraction. Requires gcd(sigma, n) = 1 and K + 1 <= n."""
    sigma %= n
    p, gl = 1, sigma
    qq, gr = 1, n - sigma
    while p + qq <= K:
        if gl > gr:
            p, gl = p + qq, gl - gr
        else:
            qq, gr = p + qq, gr - gl
    out = []
    for (ln, mult) in ((gl, K + 1 - p), (gr, K + 1 - qq),
                       (gl + gr, p + qq - K - 1)):
        if mult > 0:
            out.append((ln, mult))
    return out


def max_gap(n, sigma, K):
    return max(ln for ln, _ in three_gaps(n, sigma, K))


def surv_count(n, sigma, K, lam):
    """(R): survivors in a full class, closed."""
    if lam == 0:
        return n
    return n - sum(mult * min(ln, lam) for ln, mult in three_gaps(n, sigma, K))


# --------------------------------------------------- (P) B in a class

def bblock(N, g, n, span, hi, t):
    """(P): (beta, lam) for class t -- the start position and length of
    the cyclic block of positions whose element lies in B."""
    lamB = N - span
    if lamB <= 0:
        return (0, 0)
    b0 = (hi + 1) % N
    a0full = (t - b0) % N
    a0 = a0full % g
    if a0 >= lamB:
        return (0, 0)
    lam = (lamB - 1 - a0) // g + 1
    return (((a0 - a0full) // g) % n, lam)


# ------------------------------------------------- (Q) the level law

def surv_intervals(n, sigma, M, lam):
    """(Q): the survivor positions d, as non-wrapping [x, y] intervals
    in [0, n) -- one per gap of P_j strictly longer than lam."""
    if lam == 0:
        return [[0, n - 1]]
    pts = sorted({(sigma * y) % n for y in range(-M, M + 1)})
    out = []
    for i, p in enumerate(pts):
        nxt = pts[i + 1] if i + 1 < len(pts) else pts[0] + n
        if nxt - p > lam:
            x, y = p + lam, nxt - 1
            if y < n:
                out.append([x, y])
            elif x >= n:
                out.append([x - n, y - n])
            else:
                out.append([x, n - 1])
                out.append([0, y - n])
    return out


def surv_mask(n, sigma, M, lam):
    mask = bytearray(n)
    for x, y in surv_intervals(n, sigma, M, lam):
        mask[x:y + 1] = b"\x01" * (y - x + 1)
    return mask


# ------------------------------------------- (T) the assembly, and J=2

def floor_sum(cnt, m, aa, bb):
    """sum_{i=0}^{cnt-1} floor((aa i + bb) / m), m > 0, cnt >= 0."""
    ans = 0
    if aa < 0:
        aa2 = aa % m
        ans -= cnt * (cnt - 1) // 2 * ((aa2 - aa) // m)
        aa = aa2
    if bb < 0:
        bb2 = bb % m
        ans -= cnt * ((bb2 - bb) // m)
        bb = bb2
    while True:
        if aa >= m:
            ans += cnt * (cnt - 1) // 2 * (aa // m)
            aa %= m
        if bb >= m:
            ans += cnt * (bb // m)
            bb %= m
        ymax = aa * cnt + bb
        if ymax < m:
            return ans
        cnt = ymax // m
        bb = ymax % m
        m, aa = aa, m


def count_lt(cnt, mul, add, n, z):
    """#{ i in [0, cnt) : (mul i + add) mod n < z }, 0 <= z <= n."""
    if z <= 0:
        return 0
    return floor_sum(cnt, n, mul, add) - floor_sum(cnt, n, mul, add - z)


def count_in(cnt, mul, add, n, x, y):
    return count_lt(cnt, mul, add, n, y + 1) - count_lt(cnt, mul, add, n, x)


def classes(ce):
    """Per class t: (first m in I of that class, count, s of that m)."""
    lo, hi, g, n = ce["lo"], ce["hi"], ce["g"], ce["n"]
    out = {}
    for t in range(g):
        first = lo + ((t - lo) % g)
        if first > hi:
            continue
        out[t] = (first, (hi - first) // g + 1, ((first - t) // g) % n)
    return out


def levels(b, a, ce, t):
    """Per level j < J for a class t: (t_j, mult b^j mod n, gamma_j,
    beta, lam, M_j) -- only the levels whose class is unsaturated."""
    N, g, n, J, phi = ce["N"], ce["g"], ce["n"], ce["J"], ce["phi"]
    span, hi = ce["span"], ce["hi"]
    orb = orbit(ce["f"], t, J + g)
    out = []
    for j in range(1, J):
        tj = orb[j - 1]
        beta, lam = bblock(N, g, n, span, hi, tj)
        if lam == 0:
            continue
        rj = repunit(b, j)
        ej = (pow(b, j) * t - (b - 1) * phi * rj) % N
        out.append((tj, pow(b, j, n), ((ej - tj) // g) % n, beta, lam, a * rj))
    return out


def deep_ok(ce, t):
    return all(x in ce["A"]
               for x in orbit(ce["f"], t, ce["J"] + ce["g"])[ce["J"] - 1:])


def w_from_description(b, a, ce):
    """(T): W assembled from the closed level descriptions -- each level
    an O(1) query, the class range walked."""
    n, g, sigma = ce["n"], ce["g"], (ce["q"] // ce["g"]) % ce["n"]
    masks, W = {}, set()
    for t, (first, cnt, s0) in classes(ce).items():
        if not deep_ok(ce, t):
            continue
        lv = []
        for (tj, mul, gam, beta, lam, M) in levels(b, a, ce, t):
            key = (M, lam)
            if key not in masks:
                masks[key] = surv_mask(n, sigma, M, lam)
            lv.append((mul, gam, beta, masks[key]))
        if not lv:
            W.update(first + g * i for i in range(cnt))
            continue
        for i in range(cnt):
            s = (s0 + i) % n
            if all(mask[(mul * s + gam - beta) % n]
                   for mul, gam, beta, mask in lv):
                W.add(first + g * i)
    return W


def w_size_closed(b, a, ce):
    """Q-G: |W| with no walk. Only valid where J = 2 (one level)."""
    n, sigma = ce["n"], (ce["q"] // ce["g"]) % ce["n"]
    total = 0
    for t, (first, cnt, s0) in classes(ce).items():
        if not deep_ok(ce, t):
            continue
        lv = levels(b, a, ce, t)
        if not lv:
            total += cnt
            continue
        (tj, mul, gam, beta, lam, M) = lv[0]
        add = (mul * s0 + gam - beta) % n
        for x, y in surv_intervals(n, sigma, M, lam):
            total += count_in(cnt, mul % n, add, n, x, y)
    return total


def predict(b, a, ce):
    """Q-E: the dodge criterion as a per-cell predicate, plus the
    predicted excess where one unsaturated level makes it a count."""
    n, sigma = ce["n"], (ce["q"] // ce["g"]) % ce["n"]
    flagged, excess, sized = False, 0, True
    for t, (first, cnt, s0) in classes(ce).items():
        if not deep_ok(ce, t):
            continue
        lv = levels(b, a, ce, t)
        if not lv:
            continue
        if all(max_gap(n, sigma, 2 * M) > lam for *_, lam, M in lv):
            flagged = True
        if len(lv) == 1:
            (tj, mul, gam, beta, lam, M) = lv[0]
            add = (mul * s0 + gam - beta) % n
            for x, y in surv_intervals(n, sigma, M, lam):
                excess += count_in(cnt, mul % n, add, n, x, y)
        else:
            sized = False
    return flagged, (excess if sized else None)


# ------------------------------------------------------------ the runs

def residual_cells(cap_N):
    """Every residual cell of the parent's wide scope with N <= cap_N,
    plus the count of those above it."""
    seen, out, skipped, by_depth = set(), [], 0, {}
    for (b, a, u, v, w, z, c) in wide_scope():
        key = (b, a, u, v, w, z, c)
        if key in seen:
            continue
        seen.add(key)
        ce = cell(b, a, c, u, v, w, z)
        if ce is None or ce["n"] <= 2 * a + 1 or not is_residual(b, a, ce):
            continue
        by_depth[ce["J"]] = by_depth.get(ce["J"], 0) + 1
        if ce["N"] > cap_N:
            skipped += 1
            continue
        out.append((b, a, u, v, w, z, c, ce))
    return out, skipped, by_depth


def s0_control():
    print("== POSITIVE CONTROL (Q-A) ==")
    bad = []
    for n in range(2, 60):
        for sigma in range(1, n):
            if gcd(sigma, n) != 1:
                continue
            for K in range(0, n - 1):
                pts = sorted((sigma * i) % n for i in range(K + 1))
                gaps = [pts[(i + 1) % len(pts)] - p
                        + (n if i + 1 == len(pts) else 0)
                        for i, p in enumerate(pts)]
                want = sorted(gaps)
                got = sorted(ln for ln, m in three_gaps(n, sigma, K)
                             for _ in range(m))
                if got != want:
                    bad.append((n, sigma, K, got[:6], want[:6]))
    print(f"  three-distance gaps vs a direct sort: "
          f"{'exact' if not bad else bad[:2]} "
          f"over every (n<60, unit sigma, K<n-1)")
    ok(not bad, f"K1: three_gaps differs at {bad[:2]}")
    fs = [(cnt, m, aa, bb)
          for cnt in (0, 1, 5, 17) for m in (1, 3, 10)
          for aa in (-7, -1, 0, 2, 11) for bb in (-9, -1, 0, 4, 23)]
    bad = [t for t in fs
           if floor_sum(*t) != sum((t[2] * i + t[3]) // t[1]
                                   for i in range(t[0]))]
    print(f"  floor_sum vs a direct sum: {len(fs) - len(bad)}/{len(fs)}")
    ok(not bad, f"K1: floor_sum differs at {bad[:2]}")
    cells, skipped, _ = residual_cells(4000)
    bad = []
    for (b, a, u, v, w, z, c, ce) in cells:
        N, g, n, span, hi = ce["N"], ce["g"], ce["n"], ce["span"], ce["hi"]
        for t in range(g):
            pos = sorted(s for s in range(n)
                         if not (((t + g * s) - ce["lo"]) % N < span))
            beta, lam = bblock(N, g, n, span, hi, t)
            want = sorted((beta + i) % n for i in range(lam))
            if want != pos or (lam == 0) != (t in ce["A"]):
                bad.append((b, a, u, v, c, t))
    print(f"  B-block (beta, lam) vs a direct scan of every class at "
          f"every residual cell: {'exact' if not bad else bad[:2]}")
    ok(not bad, f"K1: bblock differs at {bad[:2]}")
    mis = 0
    for (b, a, u, v, w, z, c, ce) in cells:
        W, star, _ = w_tree(b, a, c, u, v, ce, w, z)
        if W != star:
            mis += 1
    print(f"  parent headline through this path: {len(cells)} residual "
          f"cells at N <= 4000 ({skipped} larger), {mis} with W* != W")
    ok(len(cells) == 53, f"K1: {len(cells)} residual cells read, not 53")
    ok(mis == 19, f"K1: {mis} mismatches, not 19")
    return cells


def s1_level_law(cells):
    print("\n== Q-B THE LEVEL LAW, Q-C THE COUNT FORMULA ==")
    pairs, badL, ccheck, badC = 0, [], 0, []
    for (b, a, u, v, w, z, c, ce) in cells:
        N, g, n = ce["N"], ce["g"], ce["n"]
        sigma = (ce["q"] // g) % n
        _, _, bad = w_tree(b, a, c, u, v, ce, w, z)
        for j in range(1, ce["J"]):
            pairs += 1
            rj, Mj = repunit(b, j), a * repunit(b, j)
            said = set()
            for t, (first, cnt, s0) in classes(ce).items():
                tj = orbit(ce["f"], t, j)[-1]
                beta, lam = bblock(N, g, n, ce["span"], ce["hi"], tj)
                if lam == 0:
                    continue
                mask = surv_mask(n, sigma, Mj, lam)
                ej = (pow(b, j) * t - (b - 1) * ce["phi"] * rj) % N
                gam = ((ej - tj) // g) % n
                mul = pow(b, j, n)
                for i in range(cnt):
                    s = (s0 + i) % n
                    if not mask[(mul * s + gam - beta) % n]:
                        said.add(first + g * i)
            if said != bad[j]:
                badL.append((b, a, u, v, w, z, c, j, len(said), len(bad[j])))
            for t in range(g):
                beta, lam = bblock(N, g, n, ce["span"], ce["hi"], t)
                if lam == 0:
                    continue
                ccheck += 1
                direct = sum(y - x + 1
                             for x, y in surv_intervals(n, sigma, Mj, lam))
                if direct != surv_count(n, sigma, 2 * Mj, lam):
                    badC.append((b, a, u, v, c, j, t))
    print(f"  (cell, level) pairs below J: {pairs}")
    print(f"  (Q)'s failure set == the tree's, per pair: "
          f"{pairs - len(badL)}/{pairs}")
    print(f"  (R)'s count == the interval union's size, per "
          f"(pair, unsaturated class): {ccheck - len(badC)}/{ccheck}")
    ok(not badL, f"K2: the level law differs at {badL[:3]}")
    ok(not badC, f"K1: the count formula differs at {badC[:3]}")


def s2_assemble(cells):
    print("\n== Q-D W FROM THE DESCRIPTION, Q-G THE J=2 CLOSED COUNT ==")
    bad, j2, badj2 = [], 0, []
    for (b, a, u, v, w, z, c, ce) in cells:
        W, star, _ = w_tree(b, a, c, u, v, ce, w, z)
        got = w_from_description(b, a, ce)
        if got != W:
            bad.append((b, a, u, v, w, z, c, len(got), len(W)))
        if ce["J"] == 2:
            j2 += 1
            if w_size_closed(b, a, ce) != len(W):
                badj2.append((b, a, u, v, w, z, c,
                              w_size_closed(b, a, ce), len(W)))
    print(f"  assembled W == the tree's W: "
          f"{len(cells) - len(bad)}/{len(cells)}")
    print(f"  J = 2 cells: {j2}; floor-sum |W| == the walk's: "
          f"{j2 - len(badj2)}/{j2}")
    ok(not bad, f"K3: assembled W differs at {bad[:3]}")
    ok(not badj2, f"K6: the J=2 closed count differs at {badj2[:3]}")


def s3_prediction(cells):
    print("\n== Q-E THE DODGE CRITERION AS A PREDICTION ==")
    tp = fp = fn = tn = 0
    sized, sized_ok, sized_bad, cnt_bad = 0, 0, [], []
    misses, overs = [], []
    for (b, a, u, v, w, z, c, ce) in cells:
        W, star, _ = w_tree(b, a, c, u, v, ce, w, z)
        real = (W != star)
        got = len(W) - len(star)
        flag, exc = predict(b, a, ce)
        if flag and real:
            tp += 1
        elif flag:
            fp += 1
            overs.append((b, a, u, v, w, z, c, ce["J"], exc))
        elif real:
            fn += 1
            misses.append((b, a, u, v, w, z, c, ce["J"], got))
        else:
            tn += 1
        if exc is not None:
            sized += 1
            if exc == got:
                sized_ok += 1
            else:
                sized_bad.append((b, a, u, v, w, z, c, exc, got))
            if (exc > 0) != real:
                cnt_bad.append((b, a, u, v, w, z, c, exc, got))
    print(f"  cells: {len(cells)}; predicted mismatch and mismatched: {tp}; "
          f"predicted clean and clean: {tn}")
    print(f"  predicted CLEAN but mismatched (K4): {fn} {misses[:3]}")
    print(f"  predicted mismatch but clean (K5): {fp} {overs[:3]}")
    print(f"  excess predicted as a NUMBER where one level carries it: "
          f"{sized_ok}/{sized} exact {sized_bad[:2]}")
    print(f"  and that number's sign as the verdict, over those {sized}: "
          f"{sized - len(cnt_bad)} agree {cnt_bad[:2]}")
    ok(not misses, f"K4: the dodge criterion is not necessary at {misses[:3]}")


def s4_dial(cells):
    """Q-F, over the COMPLETE census rather than the parent's readable
    slice -- the claims it feeds are about all of it. W comes from the
    description, which Q-D has already matched to the game."""
    print("\n== Q-F THE DIAL ==")
    mono, nonmono, mis, floor_mis, off_floor = 0, [], 0, 0, []
    lvl1, levels_seen = 0, set()
    for (b, a, u, v, w, z, c, ce) in cells:
        N, g, n = ce["N"], ce["g"], ce["n"]
        sigma, span, hi = (ce["q"] // g) % n, ce["span"], ce["hi"]
        gs = [max_gap(n, sigma, 2 * a * repunit(b, j))
              for j in range(1, ce["J"])]
        if all(gs[i] >= gs[i + 1] for i in range(len(gs) - 1)):
            mono += 1
        else:
            nonmono.append((b, a, u, v, c, gs))
        W = w_from_description(b, a, ce)
        star = {m for m in range(ce["lo"], hi + 1)
                if all(x in ce["A"]
                       for x in orbit(ce["f"], m % g, ce["J"] + g))}
        if W == star:
            continue
        mis += 1
        if 2 * a + 1 <= b + 1:
            floor_mis += 1
        else:
            off_floor.append((b, a, u, v, w, z, c))
        here = {j for m in W - star for j in range(1, ce["J"])
                if bblock(N, g, n, span, hi,
                          orbit(ce["f"], m % g, j)[-1])[1] > 0}
        levels_seen |= here
        if here == {1}:
            lvl1 += 1
    print(f"  max gap non-increasing in the level: {mono}/{len(cells)} "
          f"{nonmono[:2]}")
    print(f"  mismatch cells over the complete census: {mis} of {len(cells)}; "
          f"at the redundancy floor 2a+1 <= b+1: {floor_mis}; off it: "
          f"{len(off_floor)} {off_floor[:3]}")
    print(f"  mismatch cells where EVERY extra state's unsaturated level "
          f"is 1: {lvl1} of {mis}; levels carrying an extra state anywhere: "
          f"{sorted(levels_seen)}")
    ok(not off_floor, f"K7: a mismatch cell off the redundancy floor at "
                      f"{off_floor[:3]}")


def s5_caps(cap_N=500000):
    print(f"\n== Q-H THE CAPS RAISED (residual, N <= {cap_N}) ==")
    cells, skipped, by_depth = residual_cells(cap_N)
    print(f"  residual cells by depth J: "
          f"{ {j: by_depth[j] for j in sorted(by_depth)} }")
    print(f"  read: {len(cells)}; above the cap and still unread: {skipped}")
    print(f"  of them at the redundancy floor 2a+1 <= b+1: "
          f"{sum(1 for r in cells if 2 * r[1] + 1 <= r[0] + 1)}")
    new, mis = [], 0
    for (b, a, u, v, w, z, c, ce) in cells:
        if ce["N"] <= 4000:
            continue
        W = w_from_description(b, a, ce)
        star = {m for m in range(ce["lo"], ce["hi"] + 1)
                if all(x in ce["A"]
                       for x in orbit(ce["f"], m % ce["g"],
                                      ce["J"] + ce["g"]))}
        flag, exc = predict(b, a, ce)
        new.append((b, a, u, v, w, z, c, ce["N"], ce["J"], len(W), len(star),
                    flag, exc, W != star))
        if W != star:
            mis += 1
    print(f"  cells the parent could not read: {len(new)}; mismatched: {mis}")
    for row in new:
        b, a, u, v, w, z, c, N, J, nW, nS, flag, exc, real = row
        print(f"    (b={b},a={a}) slope {u}/{v} phase {w}/{z} c={c}: "
              f"N={N} J={J} |W|={nW} |W*|={nS} predicted={flag} "
              f"excess said {exc} against {nW - nS} floor={2*a+1 <= b+1}")
    off = [r for r in new if r[13] and not (2 * r[1] + 1 <= r[0] + 1)]
    ok(not off, f"K7: a new mismatch off the redundancy floor at {off[:2]}")


def s6_feasibility(cap_N=60000):
    print(f"\n== Q-H THE CAPS RAISED (feasibility, N <= {cap_N}) ==")
    seen, read, skipped, disagree = set(), 0, 0, []
    for (b, a, u, v, w, z, c) in wide_scope():
        key = (b, a, u, v, w, z, c)
        if key in seen:
            continue
        seen.add(key)
        L = v * z // gcd(v, z)
        if L * b ** c > cap_N:
            skipped += 1
            continue
        ce = cell(b, a, c, u, v, w, z)
        if ce is None:
            continue
        read += 1
        N, g, n, J = ce["N"], ce["g"], ce["n"], ce["J"]
        phi, lo, hi, span = ce["phi"], ce["lo"], ce["hi"], ce["span"]
        crit = (phi % g) in ce["A"] and lo <= phi <= hi
        true_f = lo <= phi <= hi and all(
            x in ce["A"] for x in orbit(ce["f"], phi % g, J + g)[J - 1:])
        if true_f:
            q = ce["q"]
            for j in range(1, J):
                rj = repunit(b, j)
                base = (pow(b, j) * phi - (b - 1) * phi * rj) % N
                if any(((base + q * y) % N - lo) % N >= span
                       for y in range(-a * rj, a * rj + 1)):
                    true_f = False
                    break
        if true_f != crit:
            disagree.append((b, a, u, v, w, z, c, true_f, crit))
    print(f"  cells read: {read} (N <= {cap_N}; {skipped} larger not read)")
    print(f"  the tree walk's feasibility verdict differs from 'the start "
          f"class is saturated': {len(disagree)} {disagree[:3]}")
    ok(not disagree, f"K1: feasibility disagrees at {disagree[:3]}")
    if disagree:
        b, a, u, v, w, z, c = disagree[0][:7]
        print(f"  rgame replay: {rgame(b, a, c, u, v, w, z)[0]}")


def main():
    cells = s0_control()
    if FAILURES:
        print("\nCONTROL FAILED -- nothing below is read.")
        return 1
    s1_level_law(cells)
    s2_assemble(cells)
    s3_prediction(cells)
    s4_dial(residual_cells(500000)[0])
    s5_caps()
    s6_feasibility()
    print()
    if FAILURES:
        print(f"FAILURES: {len(FAILURES)}")
        for f in FAILURES:
            print(f"  {f}")
        return 1
    print("ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
