"""explore_ruler_gaplaw.py -- IS THE ANCHORED GAP AT GEOMETRIC WEIGHTS A
FLATTENING LAW? The gap's decline across the theta walk, measured by
explore_ruler_boundedgap.py and derived nowhere, read through one
identity: a box vector is a polynomial, its value is the polynomial at
theta, and the minimum is governed by how deeply the box lets the
polynomial vanish at 1.

(The cells, the certificate's size vector, the anchored-gap machinery
and the walk ladder are all IMPORTED from explore_ruler_boundedgap.py
and its parents. What is new here is the moment identity, the argmin
instrumentation, the flattening search, and the census that says
whether the law holds.)

THE QUESTION. At walk cell W-n (M = 15 atoms, k = 3, theta =
(n-1)/n) the atom weights are exactly geometric, w_r = theta^r
(1-theta)/(1-theta^M), and the anchored gap g_A is the least positive
|sum_r c_r w_r| over integer vectors with c_r in [s_r - k, s_r], s the
certificate's sizes. The measured g_A declines slowly in n, with one
inversion at n = 200. Is there a closed law -- and what is the
inversion?

WHOSE VOCABULARY. ATOM, SURPLUS D, ROOM D/t*, COST LATTICE, ANCHORED
GAP and COEFFICIENT BOX keep explore_ruler_surplus.py's and
explore_ruler_boundedgap.py's senses. New here: a box vector c is read
as the POLYNOMIAL P(x) = sum_r c_r x^r; its MOMENTS are the
coefficients of P in the shifted basis, P(x) = sum_j m_j (x-1)^j, i.e.
m_j = sum_r C(r,j) c_r; its FLATTENING J(c) is the least j with
m_j != 0 -- equivalently the multiplicity of the root 1, the largest J
with (x-1)^J dividing P.

THE HAND ATTACK, worked on paper before any engine code.

FIRST, THE MOMENT IDENTITY AND THE TAIL BOUND. theta - 1 = -1/n
exactly, so

    P(theta) = sum_{j >= J} m_j (-1/n)^j,

and with |m_j| <= k C(M, j+1) <= k 2^M every j,

    |P(theta)| = n^-J |m_J| (1 + eps),   |eps| <= k 2^M / (|m_J| n).

So for n past k 2^M the minimum over any box is n^-J* A, where J* is
the deepest flattening a box vector attains and A the least |m_J*|
over vectors attaining it -- a two-layer law: an ANALYTIC layer (this
identity, exact) and a COMBINATORIAL layer (J* and A, properties of
the box alone, no n in them). At walk n-values the tail bound is not
yet small; where it is weak the census decides and the ratio is
printed rather than asserted.

SECOND, THE INSTRUMENT FAMILY. Products prod_i (x^{d_i} - 1) vanish to
order J at 1 with support width sum d_i and often small coefficients
where the pure J-th difference needs C(J, J/2) > k: worked by hand,
(x-1)(x^2-1)(x^4-1) has every coefficient in {-1, 0, 1}, width 8,
m_3 = -8. Whether the product family is EXTREMAL -- whether the
deepest box flattening is always a product's -- is a prediction, not a
premise.

THIRD, THE ANCHORING AS A WINDOW. c_r in [s_r - k, s_r] is exactly
s_r in [c_r, c_r + k] per coordinate: a vector is admissible iff the
certificate's size profile threads its window. So the anchored law's
n-dependence enters ONLY through s(n): a change in J* between two
rungs must be a size profile stepping out of some minimal vector's
window, and the rig prints the blocking coordinate.

FOURTH, WHAT THE MEASURED TABLE BACK-FITS, worked before any new run
from the shipped walk table alone (the weight-units factor
(1-theta)/(1-theta^15) is near 1/15 at large n): rungs n = 200, 400,
1000 all fit A/(15 n^4) with A near 18; n = 100 fits J = 5 with A
near 31, and J = 4 is IMPOSSIBLE there (it would need A near 0.3 < 1).
So the inversion at n = 200 reads as a J-JUMP gated by the anchoring.
This back-fit is the suspicion under test, not a result.

THE SLATE, frozen before any engine code.

PREDICTIONS.
  P1. THE MOMENT LAW. At every rung the exact argmin vector satisfies
      |P(theta)| n^J / |m_J| in [1 - t, 1 + t] with t = k 2^M /
      (|m_J| n) wherever t < 1/2. (Derivation; a violation there
      refutes the identity's use, not its algebra.)
  P2. THE WALK'S LADDER. Rungs n = 200, 400, 1000 have J = 4 with
      |m_4| = 18; rung n = 100 has J = 5. The three J = 4 argmins are
      one vector family (equal up to shift and sign).
  P3. THE JUMP IS THE WINDOW'S. At n = 200 every J = 5 vector of the
      free box fails admissibility at some coordinate, and the rig
      names one; at n = 100 one threads.
  P4. STABILITY PAST THE TABLE. n = 2000 and n = 5000 keep J = 4 with
      the same |m_4| -- the law's large-n limit is one constant.
  P5. THE FREE BOX AT FULL WIDTH. The symmetric box [-3, 3]^15 has
      deepest flattening J* = 5. (The strided products reach 5 at
      width sum d_i <= 14 and coefficient growth blocks 6: a guess,
      the search is the number.)
  P6. THE PRODUCT FAMILY IS EXTREMAL AT SMALL M. For M <= 8 and
      k <= 3, the deepest flattening of the full box equals the
      deepest of the strided-product family at that width. (A guess;
      the brute force is the number.)

KILLS, as observables rather than inferences.
  K-A. Any rung with t < 1/2 where the printed ratio falls outside
       [1 - t, 1 + t].
  K-B. A nonzero vector in [-3, 3]^15 with m_0 = ... = m_5 = 0 (the
       flattening search prints it).
  K-C. Any parity failure: the argmin route's minimum differing from
       the imported anchored_gap_mim at any rung, or brute force
       differing from the moment route at M = 3.
  K-D. An argmin vector printed admissible whose window s_r in
       [c_r, c_r + k] fails at some r.

CONTROLS, run and read BEFORE any verdict, each printing how many
cases it exercised.
  C1 (POSITIVE, IDENTITY). At 1000 random box vectors across three
     rungs, P(theta) computed directly equals sum_j m_j (theta-1)^j
     computed through the moments, exactly in Fractions.
  C2 (REPRODUCTION). At every ladder rung the argmin route's minimum
     equals explore_ruler_boundedgap.py's anchored_gap_mim, Fraction
     for Fraction, before any new claim is read.

THE ARMS.
  1. The instrumented ladder: every rung of the shipped walk table,
     plus n = 110, 125, 150, 175 bracketing the jump, plus n = 2000,
     5000 -- per rung the size profile s, the exact g_A, the argmin
     vector, its moments, its flattening, the ratio of P1, and the
     admissibility recheck of K-D (P1, P2, P3, P4, C2).
  2. The free box at M = 15: deepest flattening by meet-in-the-middle
     on packed moment keys -- J = 5 keys give both the least |m_5|
     over flattening-5 vectors and, as the same pass's zero matches,
     the existence of flattening 6 (P5, K-B).
  3. Small-M chart: full brute force over [-k, k]^M for M <= 8,
     k <= 3 -- deepest flattening and least |m_J| against the strided
     products at the same width (P6).
  4. The anchored flattening spectrum, ADDED AFTER THE FIRST RUN was
     read (the first print showed the jump but nothing named its
     mechanism): per rung n >= 100, the least positive value-side
     coefficient (-1)^J m_J over admissible vectors of flattening
     exactly J, for J = 4, 5, 6, plus flattening-7 existence -- the
     law's combinatorial layer made explicit, and the discrete check
     that argmin_J of A_J n^-J reproduces the measured J. The same
     amendment took the free box to depths 6 and 7 and the ladder to
     n = 20000, 100000. A first spectrum pass tracked the least
     positive m_J and contradicted the ladder at odd J -- the value is
     m_J (-1/n)^J, so the positive-VALUE side at odd J is negative
     m_J -- and the sign was fixed before any verdict was read.

RESOURCE NOTE. Exact integer and Fraction arithmetic, no numpy. Arm 2
enumerates 7^8 vectors against a 7^7 dict of packed keys: estimated
three to eight minutes wall and two to three hundred MB peak, run
under memwatch at the 512 MB default; arms 1, 3 and 4 are seconds.
The run record below carries what it cost.

RUN RECORD (final run: wall 40.3 s, peak working set 441.6 MB against
the 512 MB default under memwatch; the three earlier runs of the
growing design cost 18.8 s to 39.6 s at 226 MB). The audit between the
third and final runs found the spectrum's candidate scan could miss
the nearest positive value behind duplicate zero-matches in a
non-deduplicated list; the join now deduplicates (the added sets are
the peak's rise) and every figure below reproduced unchanged. C1: 999
random box vectors, the direct value and the moment route agree
exactly in Fractions. C2: the argmin route's minimum equals
anchored_gap_mim at all 17 rungs. K-D fired nowhere. K-C fired
nowhere.

P1 HOLDS WHERE IT BINDS, AND THE LADDER SPLITS INTO THREE REGIMES.
At n <= 25 the argmin's flattening is 0 (m_0 = -12, -12, -3, -1) with
ratio ~ 0: the minimum is a deep cancellation ACROSS moments -- a
genuine lattice minimum the moment law does not govern. n = 50 is the
crossover (J = 2, ratio 3.0e-5). From n = 100 on the moment law
governs: ratio 0.956 at n = 100 rising to 0.999965 at n = 100000 --
within each J-branch monotonically, with one dip at the J-jump
(0.9769 at n = 150 to 0.9690 at n = 175) -- inside the tail bound
wherever t < 1/2 (n >= 20000), with zero K-A firings.

P2 HOLDS AND THE ARGMIN IS AN EXPLICIT PRODUCT. Rungs n >= 175 all
have J = 4, m_4 = +18, and the argmin vector is exactly the
coefficient vector of (x - 1)(x^2 - 1)(x^3 - 1)^2, one vector sliding
left one atom at a time as the size profile's 3s invade the tail
(a coefficient -1 needs s_r <= 2). Rungs 100-150 have J = 5,
m_5 = -30.

P3 HOLDS AND THE JUMP IS THE WINDOW'S. The spectrum: A_5 = 30 at
n = 100..150 and NONE from n = 175 on -- the flattening-5 family loses
its last threading exactly when the size profile reaches ...333 -- and
A_6 is None at every rung scored, so the anchoring denies flattening 6
everywhere. A_4 = 6 at n = 100, 110 and 18 from 125 on. At every rung
n >= 100, argmin_J A_J n^-J reproduces the measured flattening.

P4 HOLDS AND EXTENDS TWO DECADES PAST THE TABLE. The size profile is
constant at 111112222233333 from n = 2000 through n = 100000, the
argmin vector does not move, and g_A n^4 converges to 18 times the
weight normalization: the anchored gap at this walk is
18 n^-4 (1 + o(1)) in value units, with the o(1) measured at 3.5e-5 by
n = 100000. (That the profile stays constant for ALL larger n is
observed at four decades, not proved.)

P5 REFUTED -- K-B FIRED, AND THE REFUTATION SHARPENS THE PICTURE. The
free box [-3, 3]^15 reaches flattening 6 (least |m_5| = 6, least
|m_6| = 18) and flattening 7 is EMPTY. So the deepest free flattening
is exactly 6, and the strided products reach it too, at the same
constant: the width-14 product search prints (6, 18) -- a check that
refuted this record's first draft, which had inferred products stop at
5 -- and since products are box vectors, the exhaustive 18 pins the
product minimum exactly. The anchoring is
worth two orders of n: free,
the gap would fall as 18 n^-6; anchored it is pinned at 18 n^-4,
A STRONGER criterion than the free box would give -- the certificate's
own sizes deny every flattening-6 vector and, past n = 150, every
flattening-5 one.

P6 HOLDS AT EVERY (M <= 8, k <= 3): the full box's deepest flattening
and least |m_J| equal the strided-product family's at the same width,
eighteen cells, zero DIFFER rows.

WHAT THIS SETTLES AND WHAT IT LEAVES. The open sentence this rig was
built for -- the anchored gap's decline is "measured, not derived" --
closes: in the moment regime the gap is a flattening law,
min_J A_J(s) n^-J, its constants integers computed from the size
profile alone, its argmin an explicit polynomial, its jumps the size
profile stepping out of a flattener's window. Left genuinely open: a
proof that the size profile is eventually constant in n -- observed
across four decades, and NOT settled by the theta = 1 cell, whose own
profile differs (111111123333333 against the far rungs'
111112222233333, computed post-run): at theta = 1 the atom masses tie
and the certificate's strictly-above set collapses, so the profile at
the limit is not the limit of the profiles. Also open: whether the
free box's flattening ceiling (exactly 6 here) is an instance of a
general law relating coefficient height to the multiplicity of the
root 1 (since settled by explore_flatten_height.py: it is -- the
pure-product law, exhaustive over a two-dial chart in atoms and
height; what survives of this open is a proof of extremality), and
the Diophantine regime n <= 50, where the minimum has no
moment structure and is priced only by the box scan.
"""

import os
import sys
import time
from bisect import bisect_left
from fractions import Fraction
from itertools import product as iproduct
from math import comb
from random import Random

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_ruler_setvalued import Cell  # noqa: E402
from explore_ruler_exchange import ALPHA  # noqa: E402
from explore_ruler_optimum import integerize  # noqa: E402
from explore_ruler_surplus import LADDER, ring_truth  # noqa: E402
from explore_ruler_boundedgap import (  # noqa: E402
    anchored_gap_mim, cert_sizes,
)

F = Fraction

M = 15
K = 3


# ------------------------------------------------------------- moments

def moments(c, upto=None):
    """m_j = sum_r C(r,j) c_r for j = 0..upto (default len(c)-1)."""
    top = len(c) - 1 if upto is None else upto
    return [sum(comb(r, j) * c[r] for r in range(len(c)))
            for j in range(top + 1)]


def flattening(c):
    """(J, m_J) for the least j with m_j != 0, or (None, 0) at c = 0."""
    for j in range(len(c)):
        m = sum(comb(r, j) * c[r] for r in range(len(c)))
        if m:
            return j, m
    return None, 0


# ------------------------------------------- the argmin anchored gap

def anchored_argmin(cost, sizes, k, m):
    """(min positive box value, its vector) by meet-in-the-middle,
    exact in integers, one witness vector kept per distinct sum."""
    half = m // 2

    def sums_vec(lo, hi):
        acc = {0: ()}
        for r in range(lo, hi):
            nxt = {}
            for s, vec in acc.items():
                for c in range(sizes[r] - k, sizes[r] + 1):
                    v = s + c * cost[r]
                    if v not in nxt:
                        nxt[v] = vec + (c,)
            acc = nxt
        return acc

    a = sums_vec(0, half)
    b = sums_vec(half, m)
    keys = sorted(b)
    best = None
    bvec = None
    for x, va in a.items():
        i = bisect_left(keys, -x + 1)
        if i < len(keys):
            v = x + keys[i]
            if best is None or v < best:
                best = v
                bvec = va + b[keys[i]]
    return best, bvec


# --------------------------------------------- the flattening search

def _packed_partials(rlo, rhi, ranges, depth):
    """Every vector on atoms rlo..rhi-1 with entries in the per-atom
    ranges: a dict packed(m_0..m_{depth-1}) -> sorted list of
    (m_depth, is_zero) pairs, moments taken with the GLOBAL atom
    indices. Packing uses 24 bits per field, offset so every partial
    fits."""
    rows = [[comb(r, j) for j in range(depth + 1)] for r in range(rlo, rhi)]
    out = {}
    for vec in iproduct(*[range(lo, hi + 1) for lo, hi in ranges[rlo:rhi]]):
        ms = [0] * (depth + 1)
        for i, c in enumerate(vec):
            if c:
                row = rows[i]
                for j in range(depth + 1):
                    ms[j] += c * row[j]
        key = 0
        for j in range(depth):
            key = (key << 24) | (ms[j] + (1 << 23))
        out.setdefault(key, set()).add(
            (ms[depth], not any(vec)))
    return {k: sorted(v) for k, v in out.items()}


def deepest_flattening_15(ranges, depth):
    """Over the box given by per-atom ranges (15 atoms): (least
    |m_depth| over vectors with m_0..m_{depth-1} = 0 and m_depth != 0,
    a count of zero-sum matches at depth -- positive iff a nonzero
    vector has m_0..m_depth ALL zero, i.e. iff flattening depth+1
    exists; not a census of them -- and the least POSITIVE value-side
    coefficient (-1)^depth m_depth: the value in the moment regime is
    m_J (-1/n)^J, so the positive-VALUE side is positive m at even
    depth and negative m at odd, and the box is unsymmetric in
    general. All read from one join."""
    a = _packed_partials(0, 7, ranges, depth)
    best = None
    best_pos = None
    deeper = 0
    rows = [[comb(r, j) for j in range(depth + 1)] for r in range(7, 15)]
    for vec in iproduct(*[range(lo, hi + 1) for lo, hi in ranges[7:15]]):
        ms = [0] * (depth + 1)
        for i, c in enumerate(vec):
            if c:
                row = rows[i]
                for j in range(depth + 1):
                    ms[j] += c * row[j]
        key = 0
        for j in range(depth):
            key = (key << 24) | (-ms[j] + (1 << 23))
        hit = a.get(key)
        if hit is None:
            continue
        iszero_b = not any(vec)
        target = -ms[depth]
        i = bisect_left(hit, (target, False))
        # The list is deduplicated, so around the target at most two
        # entries share its value (the two flags); the nearest below
        # and the two nearest strictly-above values are inside this
        # window, which is what the three minima below need.
        for cand in [hit[j] for j in range(max(i - 1, 0),
                                           min(i + 3, len(hit)))]:
            m_tot = cand[0] + ms[depth]
            if m_tot == 0:
                if not (cand[1] and iszero_b):
                    deeper += 1
            else:
                v = abs(m_tot)
                if best is None or v < best:
                    best = v
                vs = m_tot if depth % 2 == 0 else -m_tot
                if vs > 0 and (best_pos is None or vs < best_pos):
                    best_pos = vs
    return best, best_pos, deeper


def small_m_chart(mmax=8, kmax=3):
    """Full brute force: for each (M', k') the deepest flattening of
    [-k', k']^M' and the least |m_J| there."""
    chart = {}
    for mm in range(3, mmax + 1):
        for kk in range(1, kmax + 1):
            bestJ = -1
            bestA = None
            for vec in iproduct(range(-kk, kk + 1), repeat=mm):
                j, m = flattening(vec)
                if j is None:
                    continue
                if j > bestJ:
                    bestJ, bestA = j, abs(m)
                elif j == bestJ and abs(m) < bestA:
                    bestA = abs(m)
            chart[(mm, kk)] = (bestJ, bestA)
    return chart


def strided_product_depth(width, k):
    """Deepest strided product prod (x^{d_i} - 1) with sum d_i <=
    width and every coefficient in [-k, k], by exhaustive search over
    stride multisets; returns (J, least |m_J| over the deepest)."""
    best = (0, 1)  # the vector (1): J = 0, m_0 = 1
    stack = [((), [1])]
    while stack:
        ds, poly = stack.pop()
        used = sum(ds)
        j = len(ds)
        if j > 0 and max(abs(x) for x in poly) <= k:
            mj = abs(moments(poly, j)[j])
            if j > best[0] or (j == best[0] and mj < best[1]):
                best = (j, mj)
        start = ds[-1] if ds else 1
        for d in range(start, width - used + 1):
            new = [0] * (len(poly) + d)
            for i, cc in enumerate(poly):
                new[i] -= cc
                new[i + d] += cc
            if max(abs(x) for x in new) <= 3 * k:
                stack.append((ds + (d,), new))
    return best


# --------------------------------------------------------------- arms

def walk_cell(n):
    return Cell("W-%d" % n, (3, 5, 7), (3, 5), 3, F(n - 1, n))


def control_identity(rungs, trials=1000, seed=20260817):
    rng = Random(seed)
    checked = 0
    for n in rungs:
        cell = walk_cell(n)
        got = cert_sizes(cell, ALPHA)
        assert got is not None
        sizes = got[0]
        theta = cell.theta
        for _ in range(trials // len(rungs)):
            c = [rng.randint(sizes[r] - K, sizes[r]) for r in range(M)]
            direct = sum(c[r] * theta ** r for r in range(M))
            ms = moments(c)
            viamom = sum(ms[j] * (theta - 1) ** j for j in range(M))
            assert direct == viamom, (n, c)
            checked += 1
    print("C1 identity: %d random box vectors, exact agreement" % checked)


def arm_ladder(rungs):
    print("ARM 1 -- the instrumented ladder")
    print("  %-7s %-9s %2s %6s %10s %8s  argmin (nonzero coords)"
          % ("cell", "g_A", "J", "m_J", "ratio", "t-bound"))
    reproduced = 0
    for n in rungs:
        cell = walk_cell(n)
        t0 = time.time()
        assert ring_truth(cell), n
        cost, _cover, _target, den = integerize(cell, ALPHA)
        got = cert_sizes(cell, ALPHA)
        assert got is not None, n
        sizes = got[0]
        best, vec = anchored_argmin(cost, sizes, K, M)
        ref = anchored_gap_mim(cost, sizes, K, M)
        assert best == ref, (n, "K-C parity", best, ref)  # C2
        reproduced += 1
        for r in range(M):  # K-D window recheck
            assert vec[r] <= sizes[r] <= vec[r] + K, (n, r, "K-D")
        gap = F(best, den)
        j, mj = flattening(vec)
        theta = cell.theta
        ptheta = sum(vec[r] * theta ** r for r in range(M))
        ratio = abs(ptheta) * n ** j / abs(mj)
        tb = F(K * 2 ** M, abs(mj) * n)
        if tb < F(1, 2):
            assert 1 - tb <= ratio <= 1 + tb, (n, "K-A", float(ratio))
        nz = ["%+d@%d" % (vec[r], r) for r in range(M) if vec[r]]
        print("  W-%-5d %.3e %2d %6d %10.6f %8.4f  %s  s=%s  (%.1fs)"
              % (n, float(gap), j, mj, float(ratio), float(tb),
                 " ".join(nz), "".join(str(x) for x in sizes),
                 time.time() - t0))
    print("C2 reproduction: argmin minimum = anchored_gap_mim at "
          "%d rungs" % reproduced)
    print()


def arm_freebox():
    print("ARM 2 -- the free box [-3,3]^15, deepest flattening")
    free = [(-K, K)] * M
    for depth in (5, 6, 7):
        t0 = time.time()
        best, _pos, deeper = deepest_flattening_15(free, depth)
        print("  flattening %d: least |m_%d| = %s;  flattening-%d "
              "vectors found: %d  (%.1fs)"
              % (depth, depth, best, depth + 1, deeper,
                 time.time() - t0))
        if depth == 5 and deeper:
            print("  K-B FIRES: flattening 6 exists in the free box")
        if not deeper:
            break
    pj, pa = strided_product_depth(M - 1, K)
    print("  strided products at width %d: deepest (%d, %d)"
          % (M - 1, pj, pa))
    print()


def arm_anchored_spectrum(rungs):
    """Per rung, the least |m_J| over ADMISSIBLE vectors of flattening
    exactly J, for J = 4, 5, 6 -- the anchored law's combinatorial
    layer, and the jump's mechanism: J drops where the deeper
    spectrum empties or exceeds n times the shallower one."""
    print("ARM 4 -- the anchored flattening spectrum")
    print("  %-7s %8s %8s %8s   law argmin J" % ("cell", "A_4", "A_5", "A_6"))
    for n in rungs:
        cell = walk_cell(n)
        got = cert_sizes(cell, ALPHA)
        assert got is not None, n
        sizes = got[0]
        ranges = [(sizes[r] - K, sizes[r]) for r in range(M)]
        spec = {}
        for depth in (4, 5, 6):
            _best, pos, deeper = deepest_flattening_15(ranges, depth)
            spec[depth] = pos
            if depth == 6:
                spec["deeper"] = deeper
        cands = [(F(spec[d], n ** d), d) for d in (4, 5, 6)
                 if spec[d] is not None]
        law_j = min(cands)[1] if cands else None
        print("  W-%-5d %8s %8s %8s   %s%s"
              % (n, spec[4], spec[5], spec[6], law_j,
                 "  (flattening-7 admissible exists)" if spec["deeper"]
                 else ""))
    print()


def arm_smallm():
    print("ARM 3 -- small-M chart: full box vs strided products")
    print("  %-6s %-3s %14s %14s" % ("M", "k", "box (J, A)", "products"))
    chart = small_m_chart()
    for (mm, kk), (j, a) in sorted(chart.items()):
        pj, pa = strided_product_depth(mm - 1, kk)
        flag = "" if (pj, pa) == (j, a) else "   <- DIFFER"
        print("  %-6d %-3d %14s %14s%s"
              % (mm, kk, (j, a), (pj, pa), flag))
    print()


def main():
    rungs = list(LADDER) + [110, 125, 150, 175, 2000, 5000, 20000,
                            100000]
    rungs.sort()
    control_identity([10, 200, 1000])
    print()
    arm_ladder(rungs)
    arm_smallm()
    arm_freebox()
    arm_anchored_spectrum([n for n in rungs if n >= 100])


if __name__ == "__main__":
    main()
