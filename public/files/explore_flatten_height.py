"""explore_flatten_height.py -- IS THE FREE-BOX FLATTENING CEILING AN
INSTANCE OF A GENERAL LAW tying coefficient height to the multiplicity
of the root 1? The one sentence explore_ruler_gaplaw.py left open,
asked on its own object: the free box [-k, k]^M, its vectors read as
polynomials, its deepest flattening J*(M, k) charted as a function of
BOTH dials rather than measured at the single cell (15, 3).

(FLATTENING, MOMENTS, the FREE BOX and the STRIDED-PRODUCT family keep
explore_ruler_gaplaw.py's senses: a vector c is the polynomial
P(x) = sum_r c_r x^r on M atoms, its moments m_j are its coefficients
in the (x-1)-basis, its flattening J(c) is the least j with m_j != 0
-- the multiplicity of the root 1. New here: the HEIGHT of a vector is
its sup-norm max_r |c_r|, so the free box at height k is exactly the
vectors of height <= k, and h(M, J) -- the least height of a nonzero
M-atom vector of flattening >= J -- is the inverse of the ceiling:
J*(M, k) = max { J : h(M, J) <= k }.)

THE QUESTION. The parent measured one cell: at M = 15, k = 3 the
deepest free flattening is exactly 6, with least |m_5| = 6 and least
|m_6| = 18, and its small-M chart (M <= 8, k <= 3) matched the
strided-product family cell for cell. Is there a law in (M, k) -- and
which of the three candidate shapes governs it?

THE HAND ATTACK, worked on paper before any engine code.

FIRST, THE LATTICE READING. The flattening->=J vectors form the
lattice L_{M,J} = (x-1)^J Z[x] cut at degree < M -- rank M - J, basis
(x-1)^J x^i -- so h(M, J) is a sup-norm lattice minimum and the
ceiling is where that minimum crosses the height. Two exact tails
follow at once: at rank 1, h(M, M-1) = C(M-1, floor((M-1)/2)), the
central coefficient of (x-1)^(M-1); at rank <= 4 the minimum is
exactly enumerable (each quotient coefficient is pinned to an interval
of width 2k+1 by the box constraint it completes, so the search is
(2k+1)^rank with pruning).

SECOND, THE PRODUCT IDENTITY. For P = prod_i (x^{d_i} - 1) with J
factors, P = (x-1)^J q with q(1) = prod_i d_i, so |m_J| = prod d_i
exactly -- the parent's 18 is 1*2*3*3. The product family's deepest
member at (M, k) is enumerable over partitions (repetition allowed,
sum <= M-1) with the height read off the exact convolution.

THIRD, THE PIGEONHOLE FLOOR. Two 0/1 vectors sharing all moments
j < J differ by a height-1 vector of flattening >= J, and m_j over
0/1 vectors ranges in [0, C(M, j+1)]; so h(M, J) = 1 whenever
2^M > prod_{j<J} (C(M, j+1) + 1) (property, proved by counting). The
floor grows as sqrt(2M / log2 M) in J, while the binary products
(x-1)(x^2-1)(x^4-1)... give flattening floor(log2 M) at height 1; the
floor passes the products only near M ~ 500-1000, far past any
exhaustive chart. So whatever the chart prints for the height-1
diagonal, its asymptote is NOT settled here, and the record must say
so.

FOURTH, THE DETERMINANT READ. Minkowski's heuristic for a sup-norm
minimum is det(L)^(1/rank); det(L_{M,J})^2 is the Gram determinant of
the banded binomial basis, exact in integers by fraction-free
elimination. If the ceiling is a general law, the normalized
determinant is the shape it should follow.

THE SLATE, frozen before any engine code.

PREDICTIONS.
  P1. PRODUCT EXTREMALITY (TRANSPLANT: imported from the parent's
      M <= 8, k <= 3 chart, flagged as such). At every chart cell the
      deepest free flattening equals the strided-product family's
      deepest at that (M, k), and the least |m_J*| equals the least
      product of parts over products attaining it.
  P2. THE CELL'S HEIGHT IS EXACT. h(15, 6) = 3: the chart cell
      (15, 2) prints J* <= 5, so the parent's ceiling of 6 needed the
      full height 3.
  P3. CONVEXITY. On every complete column (fixed M, all J), the
      increments of log h(M, J) in J are nondecreasing.
  P4. THE HEIGHT-1 DIAGONAL IS THE BINARY PRODUCT'S in chart range:
      J*(M, 1) = floor(log2 M) for 4 <= M <= 24. (A guess; the
      pigeonhole floor says it fails eventually, far off-chart.)
  P5. THE MINKOWSKI RATIO IS BOUNDED. Across all exactly-known
      h(M, J) with rank >= 2, the ratio h / det^(1/rank) sits inside
      [1/4, 4]. (A guess; the chart is the number.)

KILLS, as observables rather than inferences.
  K-A. A chart cell whose exhaustive deepest flattening exceeds the
       product family's at that (M, k), or whose least |m_J*| differs
       from the product minimum -- the cell and, on a rerun with
       representative tracking, the vector are printed.
  K-B. A height-2 vector at M = 15 with flattening 6 (the (15, 2)
       cell prints J* = 6).
  K-C. Any parity failure: the MIM chart differing from full brute
       force at M <= 7, or from the parent's recorded cells -- the
       eighteen-cell (M <= 8, k <= 3) chart and the (15, 3) prints
       (J* = 6, least |m_5| = 6, least |m_6| = 18, flattening 7
       empty).
  K-D. A complete column with a decreasing log-increment (the triple
       is printed).
  K-E. A rank-1 tail cell where the enumeration route differs from
       the central-binomial formula.

CONTROLS, run and read BEFORE any verdict, each printing how many
cases it exercised.
  C1 (POSITIVE, PARITY). Full brute force over [-k, k]^M at M <= 7,
     k <= 3 agrees with the MIM route on J* and least |m_J*| at every
     cell.
  C2 (REPRODUCTION). The MIM route reproduces the parent's eighteen
     small-M cells and the (15, 3) cell's four prints.
  C3 (TAIL PARITY). At M <= 10 the rank<=4 DFS route agrees with the
     MIM chart wherever both cover a cell, and the rank-1 formula
     agrees with the DFS at J = M-1.

THE ARMS.
  1. THE CHART. J*(M, k) and least |m_J*| by meet-in-the-middle on
     moment keys, over k = 1 at M <= 24, k = 2 at M <= 16, k = 3 at
     M <= 13, k = 4 at M <= 12, k = 5 at M <= 11, k = 6..8 at
     M <= 10, k = 9..10 at M <= 8; plus the (15, 2) and (15, 3)
     cells (P1, P2, P4, K-A, K-B, C2).
  2. THE PRODUCT FAMILY per cell: deepest J and least prod of parts
     over partitions of <= M-1 with exact convolution heights (P1).
  3. THE TAILS. h(M, J) exact at rank <= 4 by interval-pinned DFS
     with iterative deepening in k, and the rank-1 closed form;
     columns completed where arm 1 meets them (P3, K-E, K-D, C3).
  4. THE LAW READ. Exact det(L_{M,J})^2 by fraction-free Gram
     elimination at every exactly-known h; the Minkowski ratio table
     (P5); the pigeonhole floor's reach printed beside the height-1
     diagonal (P4's scope line).

RESOURCE NOTE. Exact integer arithmetic throughout, no numpy. The
largest MIM cell rebuilds a half-enumeration per depth: at (15, 3)
that is 7^8 vectors against a 7^7 dict, the parent's own cost -- run
under memwatch at the 512 MB default, estimated three to seven
minutes wall for the whole script; every other cell is at least an
order smaller. The run record below carries what it cost.

RUN RECORD (final run: wall 141.9 s, peak working set 285.9 MB under
memwatch's 512 MB default). Three earlier runs of the growing engine:
the first was killed at 571 MB commit (per-key dict-of-list joins;
rebuilt as one flat deduplicated (key, packed-value) list, which also
rules out duplicate join entries by construction), the second breached
between polls at 529 MB with the
same verdicts, and the third fired C3 on a REAL ENGINE BUG: the tail
DFS pinned each quotient coefficient to the +1-unit interval where
the unit coefficient is (-1)^J, so every odd-J tail searched a
negated box -- h(5, 3) printed 3 against the chart's height-2
witness (x-1)^3 (x+1) -- fixed before any verdict was read. Final
run: C1 12 brute==MIM cells equal; C2 reproduces the parent's
(15, 3) prints exactly (J* = 6, least |m_6| = 18, least |m_5| over
flattening-exactly-5 = 6) and the small-M chart; C3 274 tail/chart
comparisons coherent; K-E zero firings.

F1. P1 HOLDS -- THE CEILING IS THE PURE-PRODUCT LAW (rule,
exhaustive over the 92-cell chart plus (15, 2) and (15, 3)): at
every cell the free box's deepest flattening equals the
strided-product family's deepest at that width and height, AND the
least |m_J*| equals the least part-product over attaining products.
The free-box ceiling of 6 at (15, 3) is that law's instance, its 18
the product 1*1*1*2*3*3 -- checked post-run: that six-part product,
(x-1)^3 (x^2-1) (x^3-1)^2, has height exactly 3, and the only other
six-part partition with product 18 fitting the width, (1,1,1,1,3,6),
has height 6.

F2. P2 HOLDS: (15, 2) stops at J* = 5 (least |m_5| = 24), so
h(15, 6) = 3 exactly -- the parent's ceiling needed its full height.

F3. P4 REFUTED, AND THE DIAGONAL IS THE CLASSICAL TABLE: J*(M, 1)
steps at M = 7, 12, 16, 23 with least moments 6, 30, 120, 840 -- the
DISTINCT-part products (1,2,3), (1,2,3,5), (1,2,3,4,5), (1,2,3,4,5,7)
all keep height 1, which the binary-product guess missed (checked
post-run: each of those four expands to height exactly 1, and the
only rival partitions with the same part-product inside the width --
(2,2,2,3,5) and (2,2,2,3,5,7) -- expand to height 3). Inverted,
the diagonal is d(m) = 3, 6, 11, 15, 22 at m = 2..6: the minimal
degree of a height-1 polynomial vanishing to order m at 1, the
problem of Borwein and Mossinghoff (Experimental Mathematics 9:3,
2000), whose abstract states d(m) determined for m <= 10 with every
extremal a pure product. The full text sits behind a paywall; the
contact here is the abstract plus this rig's independent computation
of the overlap m <= 6, which agrees. (The m = 2 row needs the
off-chart M = 3 corner to pin d(2) from below; checked post-run by
the brute route, J*(3, 1) = 1.)

F4. P3 REFUTED (K-D): every complete column M = 6..11 is
non-log-convex -- h(9, J) runs 2, 3, 9, 14 at J = 4..7, increments
log2(1.5), log2(3), log2(14/9).

F5. P5 REFUTED NARROWLY, AND THE INFORMATIVE HALF SURVIVES: the
ratio h / det^(1/rank) spans [0.217, 0.933] over 114 exactly-known
cells -- below the stated [1/4, 4] band only at height-1-saturated
cells -- and it sits BELOW 1 everywhere: the sup-norm minimum
undercuts the Minkowski heuristic at every cell, by up to ~4.6x.

F6. THE PIGEONHOLE FLOOR (property, proved in the hand attack;
printed beside the diagonal) reaches only 1..3 in chart range --
vacuous against the products here, which is exactly why the
diagonal's asymptote (floor ~ sqrt(2M/log2 M) vs the products'
observed steps) stays open beyond the chart.

(SETTLED FURTHER SINCE, by explore_flatten_offchart.py: the law
below is re-established on the INVERSE dial -- h(M, J), the least height
at width M and depth J -- exhaustively at all 63 cells M <= 12 and so at
every height there, where this chart reached k <= 4 at the widest of
them and no higher than k <= 10 anywhere, and confirmed
at 18 cells out to M = 30, all at h = 2 and all past this chart's k = 2
reach of M <= 16. The incumbent contact below is superseded too: the
diagonal is OEIS A059753, known and minimal to n = 14, and pure products
attain it at every n <= 11. What stays open is what this paragraph says
stays open.)

WHAT THIS SETTLES AND WHAT IT LEAVES. The parent's open sentence
closes: the free-box flattening ceiling IS an instance of a general
law -- the pure-product law, exhaustively in range -- and the law's
constant is a part-product, giving the flattening law's
combinatorial layer a product structure on the free side. Left open:
a PROOF of product extremality (the classical determination reaches
m <= 10 at height 1; every row here, height 1 included, is
exhaustive computation in range), any closed form for h(M, J) (not
log-convex in J, and under its Minkowski read throughout the known
cells), and the height-1 diagonal's asymptote.
"""

import os
import sys
from itertools import product as iproduct
from math import comb, log2
from fractions import Fraction

M_CHART = {1: 24, 2: 16, 3: 13, 4: 12, 5: 11, 6: 10, 7: 10, 8: 10,
           9: 8, 10: 8}
EXTRA_CELLS = [(15, 2), (15, 3)]


def moments_of(vec, depth):
    """First `depth` moments m_j = sum_r C(r,j) c_r of an atom vector."""
    return tuple(sum(comb(r, j) * c for r, c in enumerate(vec))
                 for j in range(depth))


def flattening(vec):
    """Least j with m_j != 0, or None for the zero vector."""
    M = len(vec)
    for j in range(M):
        if sum(comb(r, j) * c for r, c in enumerate(vec)):
            return j
    return None


# ---------------------------------------------------------------- MIM

def _radix(M, k, depth):
    """Mixed-radix packing of a moment tuple into one exact int:
    |m_j| <= k C(M, j+1) for any M-atom height-k vector, so
    key = sum (m_j + B_j) R_j with R the running product is a
    bijection. ZERO is the packed all-zero tuple's key."""
    bounds = [k * comb(M, j + 1) for j in range(depth)]
    radii, r = [], 1
    for b in bounds:
        radii.append(r)
        r *= 2 * b + 1
    zero = sum(b * rr for b, rr in zip(bounds, radii))
    return bounds, radii, zero


def _half_enum(atoms, k, depth, bounds, radii):
    """Yield (packed key, packed negated key, is_nonzero) over all
    vectors on `atoms`."""
    contrib = [[tuple(comb(r, j) * c for j in range(depth))
                for c in range(-k, k + 1)] for r in atoms]
    width = 2 * k + 1
    for choice in iproduct(range(width), repeat=len(atoms)):
        sums = [0] * depth
        nz = False
        for i, ci in enumerate(choice):
            if ci != k:
                nz = True
            t = contrib[i][ci]
            for j in range(depth):
                sums[j] += t[j]
        key = neg = 0
        for j in range(depth):
            key += (sums[j] + bounds[j]) * radii[j]
            neg += (bounds[j] - sums[j]) * radii[j]
        yield key, neg, nz


def mim_exists(M, k, depth):
    """Is there a nonzero height-<=k vector with m_0..m_{depth-1} = 0?
    The dict sits on the smaller (trailing) half; the larger half is
    enumerated against it."""
    a = (M + 1) // 2
    atoms_a, atoms_b = list(range(a)), list(range(a, M))
    bounds, radii, zero = _radix(M, k, depth)
    seen = {}
    for key, _neg, nz in _half_enum(atoms_b, k, depth, bounds, radii):
        if nz and key == zero:
            return True          # B-half alone flattens
        if nz or key not in seen:
            seen[key] = seen.get(key, 0) + (1 if nz else 0)
    for key, neg, nz in _half_enum(atoms_a, k, depth, bounds, radii):
        if nz:
            if neg in seen:
                return True      # nonzero A + any B
        else:
            if seen.get(neg, 0) > 0:
                return True      # zero A + nonzero B (key 0 case)
    return False


def mim_least(M, k, depth, allow_deeper=False):
    """Least |m_depth| over nonzero height-<=k vectors with
    m_0..m_{depth-1} = 0. At depth = J* no such vector has
    m_depth = 0 (the deepest pass excluded depth+1) and a zero sum
    ASSERTS; with allow_deeper=True (probing a non-deepest depth,
    where deeper vectors legitimately zero the sum) zero sums are
    skipped and the least is over flattening EXACTLY depth.

    One flat sorted (key, packed) list, deduplicated -- no per-key
    containers: the memory shape that kept the first run's peak over
    the 512 MB line, and duplicate join entries, are both ruled out
    by the same structure."""
    import bisect
    a = (M + 1) // 2
    atoms_a, atoms_b = list(range(a)), list(range(a, M))
    bounds, radii, _zero = _radix(M, k, depth)
    width = 2 * k + 1
    contrib_b = [[tuple(comb(r, j) * c for j in range(depth + 1))
                  for c in range(-k, k + 1)] for r in atoms_b]
    pairs = set()
    for choice in iproduct(range(width), repeat=len(atoms_b)):
        sums = [0] * (depth + 1)
        nz = False
        for i, ci in enumerate(choice):
            if ci != k:
                nz = True
            t = contrib_b[i][ci]
            for j in range(depth + 1):
                sums[j] += t[j]
        key = 0
        for j in range(depth):
            key += (sums[j] + bounds[j]) * radii[j]
        # 2*value + flag packs each (tail moment, nonzero) pair;
        # nz=False only ever the all-zero half-vector
        pairs.add((key, 2 * sums[depth] + (1 if nz else 0)))
    pairs = sorted(pairs)
    best = None
    contrib_a = [[tuple(comb(r, j) * c for j in range(depth + 1))
                  for c in range(-k, k + 1)] for r in atoms_a]
    for choice in iproduct(range(width), repeat=len(atoms_a)):
        sums = [0] * (depth + 1)
        nz = False
        for i, ci in enumerate(choice):
            if ci != k:
                nz = True
            t = contrib_a[i][ci]
            for j in range(depth + 1):
                sums[j] += t[j]
        neg = 0
        for j in range(depth):
            neg += (bounds[j] - sums[j]) * radii[j]
        target = -2 * sums[depth]
        pos = bisect.bisect_left(pairs, (neg, target))
        for idx in (pos - 2, pos - 1, pos, pos + 1, pos + 2):
            if 0 <= idx < len(pairs):
                bkey, packed = pairs[idx]
                if bkey != neg:
                    continue
                v, bnz = packed >> 1, packed & 1
                if not (nz or bnz):
                    continue     # the all-zero pairing
                s = abs(sums[depth] + v)
                if s == 0:
                    if allow_deeper:
                        continue
                    raise AssertionError((M, k, depth))
                if best is None or s < best:
                    best = s
    return best


def deepest(M, k, start_j=0):
    """(J*, least |m_J*|) for the free box [-k, k]^M. A caller holding
    a witness of flattening >= start_j (a product vector) lets the
    existence search begin above it."""
    depth = start_j + 1
    while depth < M and mim_exists(M, k, depth):
        depth += 1
    jstar = depth - 1
    return jstar, mim_least(M, k, jstar)


# ------------------------------------------------------- brute force

def brute(M, k):
    best_j, best_m = -1, None
    for vec in iproduct(range(-k, k + 1), repeat=M):
        if not any(vec):
            continue
        j = flattening(vec)
        m = abs(sum(comb(r, j) * c for r, c in enumerate(vec)))
        if j > best_j:
            best_j, best_m = j, m
        elif j == best_j and m < best_m:
            best_m = m
    return best_j, best_m


# ---------------------------------------------------- product family

def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return out


def partitions_upto(total, largest=None):
    """All partitions (nonincreasing part tuples) of every n <= total."""
    if largest is None:
        largest = total
    yield ()
    for first in range(min(largest, total), 0, -1):
        for rest in partitions_upto(total - first, first):
            yield (first,) + rest


def product_family(M, k):
    """Deepest J with a product prod (x^{d_i}-1), sum d_i <= M-1, of
    height <= k; and the least prod d_i among those attaining it."""
    best_j, best_m = 0, None
    for parts in partitions_upto(M - 1):
        if not parts:
            continue
        poly = [1]
        for d in parts:
            f = [-1] + [0] * (d - 1) + [1]
            poly = poly_mul(poly, f)
        if max(abs(c) for c in poly) > k:
            continue
        j, m = len(parts), 1
        for d in parts:
            m *= d
        if j > best_j or (j == best_j and (best_m is None or m < best_m)):
            best_j, best_m = j, m
    return best_j, best_m


# ------------------------------------------------------- exact tails

def binom_vec(J, M):
    """Coefficient vector of (x-1)^J on M atoms."""
    return [((-1) ** (J - r)) * comb(J, r) if r <= J else 0
            for r in range(M)]


def tail_exists(M, J, k):
    """Rank<=4 route: is there a nonzero q of degree < M-J with
    (x-1)^J q of height <= k?  DFS over the coefficients of
    P = (x-1)^J q: choosing q_i pins P_i (unit coefficient), so each
    q_i ranges over an interval of width 2k+1; the trailing J
    coefficients of P are then forced and checked."""
    rank = M - J
    base = binom_vec(J, M)

    def rec(qs):
        i = len(qs)
        if i == rank:
            for r in range(rank, M):
                s = 0
                for t, q in enumerate(qs):
                    if 0 <= r - t <= J:
                        s += q * base[r - t]
                if abs(s) > k:
                    return False
            return any(qs)
        s = 0
        for t, q in enumerate(qs):
            if 0 <= i - t <= J:
                s += q * base[i - t]
        # P_i = s + c0 q_i with c0 = base[0] = (-1)^J: the unit
        # coefficient's SIGN sets which interval pins q_i
        if base[0] == 1:
            lo, hi = -k - s, k - s
        else:
            lo, hi = s - k, s + k
        for q in range(lo, hi + 1):
            if rec(qs + [q]):
                return True
        return False

    return rec([])


def tail_height(M, J, cap=None):
    """Exact h(M, J) by iterative deepening on k (rank <= 4 only)."""
    k = 1
    while cap is None or k <= cap:
        if tail_exists(M, J, k):
            return k
        k += 1
    return None


# ------------------------------------------------- Gram determinants

def gram_det_sq(M, J):
    """det(L_{M,J})^2 as an exact integer: Gram determinant of the
    basis (x-1)^J x^i, i < M-J, by Fraction elimination."""
    rank = M - J
    rows = []
    for i in range(rank):
        v = [0] * M
        for r, c in enumerate(binom_vec(J, M - i)):
            v[r + i] = c
        rows.append(v)
    G = [[Fraction(sum(a * b for a, b in zip(rows[i], rows[j])))
          for j in range(rank)] for i in range(rank)]
    det = Fraction(1)
    for col in range(rank):
        piv = next((r for r in range(col, rank) if G[r][col]), None)
        assert piv is not None
        if piv != col:
            G[col], G[piv] = G[piv], G[col]
            det = -det
        det *= G[col][col]
        inv = 1 / G[col][col]
        for r in range(col + 1, rank):
            f = G[r][col] * inv
            for c in range(col, rank):
                G[r][c] -= f * G[col][c]
    assert det.denominator == 1
    return int(det)


# ------------------------------------------------------------- main

def main():
    print("explore_flatten_height.py -- the free-box ceiling in (M, k)")

    # C1: brute-force parity at M <= 7, k <= 3.
    n_par = 0
    for M in range(4, 8):
        for k in (1, 2, 3):
            bj, bm = brute(M, k)
            mj, mm = deepest(M, k)
            assert (bj, bm) == (mj, mm), ("C1", M, k, bj, bm, mj, mm)
            n_par += 1
    print(f"C1 parity brute==MIM: {n_par} cells, all equal")

    # The chart + product family (P1, P4, K-A; C2 covers M=8, k<=3).
    print("\nCHART  M  k  J*  least|m|  product(J, m)  agree")
    chart = {}
    for k in sorted(M_CHART):
        for M in range(4, M_CHART[k] + 1):
            pj, pm = product_family(M, k)
            jstar, least = deepest(M, k, start_j=pj)
            chart[(M, k)] = (jstar, least)
            agree = "SAME" if (jstar, least) == (pj, pm) else "DIFFER"
            print(f"  {M:3d} {k:2d} {jstar:3d} {least:9d}   "
                  f"({pj}, {pm})   {agree}")

    for (M, k) in EXTRA_CELLS:
        pj, pm = product_family(M, k)
        jstar, least = deepest(M, k, start_j=pj)
        chart[(M, k)] = (jstar, least)
        agree = "SAME" if (jstar, least) == (pj, pm) else "DIFFER"
        print(f"  {M:3d} {k:2d} {jstar:3d} {least:9d}   "
              f"({pj}, {pm})   {agree}  [extra]")

    # C2: the parent's cells.
    jstar, least = chart[(15, 3)]
    print(f"\nC2 (15,3): J* = {jstar}, least|m_{jstar}| = {least} "
          f"(parent: 6 and 18); least|m_5| over flattening-5 = "
          f"{mim_least(15, 3, 5, allow_deeper=True)} (parent: 6)")

    # Height-1 diagonal vs binary product and the pigeonhole floor (P4).
    print("\nDIAGONAL  M  J*(M,1)  floor(log2 M)  pigeonhole floor")
    for M in range(4, M_CHART[1] + 1):
        j1 = chart[(M, 1)][0]
        floor_j = 0
        prod_bound = 1
        for j in range(M):
            prod_bound *= comb(M, j + 1) + 1
            if 2 ** M > prod_bound:
                floor_j = j + 1
            else:
                break
        print(f"  {M:3d} {j1:5d} {int(log2(M)):8d} {floor_j:10d}")

    # The tails and complete columns (P3, C3, K-E).
    print("\nTAILS h(M, J) at rank <= 4, with rank-1 formula parity")
    tails = {}
    for M in range(4, 12):
        for J in range(max(1, M - 4), M):
            h = tail_height(M, J)
            tails[(M, J)] = h
            if J == M - 1:
                formula = comb(M - 1, (M - 1) // 2)
                assert h == formula, ("K-E", M, J, h, formula)
        row = "  ".join(f"J={J}:{tails[(M, J)]}"
                        for J in range(max(1, M - 4), M))
        print(f"  M={M:2d}  {row}")

    # C3: tails vs chart where both cover a cell.
    n_c3 = 0
    for (M, J), h in tails.items():
        ks = [k for (m2, k) in chart if m2 == M]
        for k in ks:
            jstar = chart[(M, k)][0]
            if jstar >= J:
                assert h <= k, ("C3", M, J, h, k)
            if h <= k:
                assert jstar >= J, ("C3", M, J, h, k, jstar)
            n_c3 += 1
    print(f"C3 tail/chart coherence: {n_c3} comparisons, all coherent")

    # Complete columns: h(M, J) for every J, where chart + tails meet.
    print("\nCOLUMNS  h(M, J) complete where swept k + rank<=4 meet")
    for M in range(6, 12):
        col = {}
        for J in range(1, M):
            hs = [k for (m2, k) in chart
                  if m2 == M and chart[(m2, k)][0] >= J]
            if hs:
                col[J] = min(hs)
            elif (M, J) in tails:
                col[J] = tails[(M, J)]
        # verify chart-derived h against tails where both exist
        for J in col:
            if (M, J) in tails:
                hs = [k for (m2, k) in chart
                      if m2 == M and chart[(m2, k)][0] >= J]
                if hs:
                    assert min(hs) == tails[(M, J)], (M, J)
        if len(col) == M - 1:
            row = "  ".join(f"{J}:{col[J]}" for J in sorted(col))
            incs = [log2(col[J + 1]) - log2(col[J])
                    for J in range(1, M - 1)]
            convex = all(incs[i + 1] >= incs[i] - 1e-12
                         for i in range(len(incs) - 1))
            print(f"  M={M:2d} COMPLETE  {row}   "
                  f"log2-increments nondecreasing: {convex}")
        else:
            row = "  ".join(f"{J}:{col[J]}" for J in sorted(col))
            missing = [J for J in range(1, M) if J not in col]
            print(f"  M={M:2d} partial   {row}   missing J={missing}")

    # The Minkowski ratio (P5) over every exactly-known h.
    print("\nMINKOWSKI  M  J  h  det^(1/rank)  ratio")
    known = dict(tails)
    for (M, k), (jstar, _) in chart.items():
        for J in range(1, jstar + 1):
            hs = [k2 for (m2, k2) in chart
                  if m2 == M and chart[(m2, k2)][0] >= J]
            if hs:
                known[(M, J)] = min(known.get((M, J), min(hs)), min(hs))
    ratios = []
    for (M, J) in sorted(known):
        if M - J < 2:
            continue
        h = known[(M, J)]
        d2 = gram_det_sq(M, J)
        dn = d2 ** (1 / (2 * (M - J)))
        ratios.append(h / dn)
        print(f"  {M:3d} {J:2d} {h:5d} {dn:12.3f} {h / dn:8.3f}")
    print(f"MINKOWSKI ratio range: [{min(ratios):.3f}, {max(ratios):.3f}] "
          f"over {len(ratios)} cells")


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
