"""explore_flatten_dk.py -- THE INVERSE DIAL ABOVE HEIGHT 2: d_k(J) at
k >= 3, read off the chart, and whether the pure-product family stays
extremal for it.

THE OBJECT. A vector c on M atoms is the polynomial P(x) = sum_r c_r x^r
of degree < M; its FLATTENING is the multiplicity of the root 1 and its
HEIGHT is max |c_r|. h(M, J) is the least height of a nonzero M-atom
vector flattened to depth J, a shortest vector in the sup norm of the
lattice (x-1)^J Z[x] cut at degree < M (explore_flatten_lattice.py,
explore_flatten_family.py, which read it exactly by reduction plus a
bounded enumeration whose radius is the reduced basis's own). The
INVERSE DIAL d_k(J) is the least degree of a multiple of (x-1)^J of
height at most k, and the two are inverses of each other:

    h(M, J) <= k   iff   M > d_k(J),

so d_k(J) = (the least M with h(M, J) <= k) - 1. A PURE PRODUCT is
prod_i (x^{d_i} - 1) over a multiset D of positive parts, flattened to
|D| with degree sum D; the pure-product law on the inverse dial says
d_k(J) is the least degree of a pure product of height at most k with
at least J parts. It holds at k = 1 (the classical table, OEIS A059753,
extremals pure to n = 10) and at k = 2 at every J <= 8
(explore_flatten_d2.py, by a search in the height domain).

THE QUESTION. What is d_k(J) at k = 3 and above, and is the
pure-product family extremal there? The record read the k >= 3 ladder
as uncontacted; it is not. The chart h(M, J) contains every ladder by
the inversion above, and the lattice route reads a cell at these ranks
in milliseconds, so the ladders at every height are one scan each, and
the question that stays is the law.

THE HAND ATTACK, on paper before the engine.

(1) THE SCAN. h is nonincreasing in M (an M-atom vector is an
(M+1)-atom vector with a zero appended) and d_k is nondecreasing in J
(a multiple of (x-1)^{J+1} is one of (x-1)^J), so for each k the scan
runs J upward and, at each J, M upward from max(previous answer + 1,
J + 1) until h(M, J) <= k; the answer is M - 1. Resuming AT the
previous answer plus one and not past it: d_k(J) = d_k(J-1) is legal
and a scan starting higher would report it one too large while still
printing a monotone ladder. d_k is nonincreasing in k at fixed J, a
second monotonicity the print checks across ladders.

(2) THE RANK-1 CORNER. At M = J + 1 the lattice has rank 1 and
h(J+1, J) = C(J, floor(J/2)), the largest binomial coefficient of
(x-1)^J, so d_k(J) = J exactly when C(J, floor(J/2)) <= k: at k = 3
that is J <= 3 (1, 2, 3 at J = 1, 2, 3; C(4,2) = 6 > 3 stops it), at
k = 6 J <= 4, at k = 10 J <= 5, at k = 20 J <= 6. Every ladder's head is
therefore known before the run and printed as a check.

(3) THE FIRST CELL OFF THE CORNER AT k = 3. J = 4, M = 5 is the rank-1
cell at height 6; M = 6 admits (x-1)^3 (x^2-1) = x^5 - 3x^4 + 2x^3 +
2x^2 - 3x + 1 of height 3, so d_3(4) = 5 and the multiset is
(1, 1, 1, 2): three parts 1 -- as many as the height admits by the
rank-1 corner, C(3,1) = 3 -- then a fresh part. The k = 2 extremals ran
(1, 1, 2, 3, ...), two parts 1 then distinct parts, until J = 8 broke
the shape. This is the shape the k = 3 ladder is expected to open with,
and it is a lean: nothing forces it past J = 4.

(4) THE PRODUCT SIDE IS A TABLE, AND THE TABLE HAS AN EDGE. The
product table enumerates multisets with degree sum at most 44, so the
law is READ only where d_k(J) <= 44; a depth whose ladder value is past
the table's edge is printed as unread and never as a failure. A miss of
the table's witness by the lattice witness is likewise not a failure:
the table keeps one witness per (count, sum), and extremality is a
statement about the degree.

(5) THE SECOND INSTRUMENT. The height-domain ladder of
explore_flatten_d2.py -- a search over the coefficients in [-k, k]
under the propagation bound, met by a backward set over the last
positions -- runs at k = 3 as it ran at k = 2, at cost (2k+1)^(N+1)
before pruning; it reaches the small depths in minutes and is stopped
by a wall budget where it does not. Where both instruments reach, they
share no code and no cost law, and a disagreement is a bug in one of
them, decided by the witness: the lattice witness's exact divisibility
by (x-1)^J and its height are checked outside the lattice code.

(6) THE FLOOR. The cyclotomic floor of the height-domain rig -- when
J log p > phi(p^e) log(k(N+1)) the cyclotomic Phi_{p^e} is forced to
divide, and the forced degrees sum -- is a lower bound at every k and
costs nothing; a ladder value below it is a bug, never a finding.

PREDICTIONS, FIXED BEFORE THE RUN (what the engine prints).
  C1 CONTROL, k = 1: the chart-read ladder prints A059753's 1, 3, 6,
     11, 15, 22, 30, 41, 48 at J = 1..9 within the width cap. KILL:
     any disagreement.
  C2 CONTROL, k = 2: the chart-read ladder prints 1, 2, 4, 7, 11, 16,
     22, 26 at J = 1..8. KILL: any disagreement.
  E1 THE LAW AT k = 3: at every J with d_3(J) <= 44, d_3(J) equals the
     least degree of a pure product of height at most 3 with at least
     J parts. KILL K-A: a J where d_3(J) is STRICTLY BELOW the product
     least degree, the lattice witness then a multiple of (x-1)^J of
     height at most 3 shorter than every pure product -- product
     extremality refuted on the inverse dial at height 3. (A ladder
     value ABOVE the product degree is impossible, the product being a
     lattice vector, and prints as K-E, a bug.)
  E2 THE LADDERS AT k = 4..8: the same law at every J the table reads,
     each ladder to the width cap or its wall. KILL K-A as above, per k.
  E3 THE TWO INSTRUMENTS AGREE: the height-domain ladder at k = 3
     equals the chart-read ladder at every J it reaches. KILL K-B: a
     disagreement, with the witness decided outside both engines.
  E4 THE PROPERTIES: every ladder value is at or above the cyclotomic
     floor (K-D below it), equals J exactly when C(J, floor(J/2)) <= k
     (K-E otherwise), and is nonincreasing in k at fixed J (K-E
     otherwise); the lattice witness has height <= k, degree exactly
     d_k(J) and divides by (x-1)^J under synthetic division outside
     the lattice code (K-E otherwise).
  L1 LEAN, not a kill: the k = 3 extremal multiset at J = 4..7 is
     (1, 1, 1, 2, 3, ...) -- three parts 1 then distinct parts -- and
     the depth where that shape first breaks is printed.

THE DESIGN. Exact integers and Fractions throughout, the lattice route
imported from explore_flatten_family.py and the height-domain route,
the product table, the floor and the classical table from
explore_flatten_d2.py and explore_flatten_offchart.py. Ladders at
k = 1..8, J to 14, width capped at 72; each ladder stops at a wall
budget and prints its reach. The height-domain ladder at k = 3 runs
J upward under its own wall and prints where it stopped. Estimate: the
chart ladders seconds to two minutes (the k = 1 ladder's rank grows
fastest, ~40 at J = 9), the height-domain ladder a minute to five;
memory a few reduced bases and one backward set, far under the ceiling.
Stages (argv): c the controls and the chart ladders, h the height-
domain check, u every attaining product at the read cells of k = 3, 5,
8 (a claim about the multisets is a claim about all of them, where the
table keeps one witness); all by default.

FINDINGS (each at its own tier; the prints copied, the asserts read)

F1  THE CONTROLS HOLD AND REACH FURTHER THAN THEIR SOURCES. The k = 1
    chart-read ladder prints A059753 at J = 1..11 -- 1, 3, 6, 11, 15,
    22, 30, 41, 48, 61, 69 -- against the height-domain rig's own
    control at J <= 7; the k = 2 ladder prints 1, 2, 4, 7, 11, 16, 22,
    26 at J <= 8 (C1, C2 AGREE) and continues 34, 45, 51 at J = 9, 10,
    11, the J = 9 value the product (1, 1, 2, 3, 4, 5, 5, 6, 7)'s and
    J = 10, 11 past the table's edge.
F2  THE INVERSE DIAL AT k = 3..8 (rule, exact; the pure-product law
    holding at every cell the table reads, 73 cells at k >= 3, K-A
    never printed). Rows J, columns k:
       J     k=1   k=2   k=3   k=4   k=5   k=6   k=7   k=8
       1       1     1     1     1     1     1     1     1
       2       3     2     2     2     2     2     2     2
       3       6     4     3     3     3     3     3     3
       4      11     7     5     5     5     4     4     4
       5      15    11     8     8     6     6     6     6
       6      22    16    11    10     9     9     9     9
       7      30    22    17    14    14    11    11    11
       8      41    26    20    19    18    16    15    15
       9      48    34    27    22    22    21    20    19
      10      61    45    33    29    27    23    23    23
      11      69    51    43    34    30    30    25    25
      12       -     -     -    44    38    36    32    31
      13       -     -     -     -    46    46    37    37
      14       -     -     -     -     -     -    49    47
    The k = 1..6 ladders stopped at their 90 s wall at J = 12, 12, 12,
    13, 14, 14 (the exact-rational reduction past rank 30), k = 7 and 8
    ran to J = 14. Every cell passes the properties: at or above the
    cyclotomic floor (tight at the corner cells, strict at every cell
    past J = 5 and near half the ladder by J = 13), equal to J exactly where C(J, floor(J/2))
    <= k, nonincreasing in k, the witness of height <= k, degree exactly
    d_k(J) and cleared by J synthetic divisions outside the lattice
    code. The cells past the table (d > 44: k = 1 at J >= 9, k = 2 at
    J >= 10, k = 5, 6 at J = 13, k = 7, 8 at J = 14) are ladder values
    with the law unread.
F3  THE TWO INSTRUMENTS AGREE (E3). The height-domain ladder at k = 3
    prints 1, 2, 3, 5, 8, 11, 17 at J = 1..7 -- AGREE at every depth,
    the J = 7 row at 5,813,796 nodes in 6.8 s -- and at J = 8 refutes
    degree 19 (123,931,761 nodes) before its 150 s wall, consistent
    with the chart's 20 and deciding nothing at that depth.
F4  THE SHAPE LEAN FAILS EARLY, AND THE UNIT-PART COUNT IS NOT MONOTONE
    (observation; stage u enumerating EVERY attaining product at the
    read cells of k = 3, 5, 8 to J = 12, since the table keeps one
    witness per cell). At k = 3 the attaining product is UNIQUE at
    every J <= 11: (1,1,1,2), (1,1,1,2,3) at J = 4, 5, the shape
    breaking at J = 6 with (1,1,1,2,3,3) -- a repeated part two depths
    earlier than the k = 2 shape broke -- and at J = 11 the one
    attaining product, (1,1,2,2,3,4,4,5,6,7,8), carries TWO unit parts
    where the height admits three. Along the k = 5 column the greatest
    unit-part count over the attaining products runs 4, 4, 4, 4, 3, 3,
    4, 4 at J = 5..12 (two attaining products at J = 7, 8, 12, one
    with three unit parts and one with four; one at each other depth),
    and at k = 8 it reaches five at J = 12. "As many unit parts as the
    height admits" is not the rule, and no rule for the multiset is
    read. At k = 7 and 8 the ladders coincide at J <= 8 and at 10, 11,
    13 and part at 9, 12, 14 (20/19, 32/31, 49/47).
F5  THE L1 PRINT WAS WRITTEN WITH A HEAD-CASE BUG: on the first run it
    fired "first breaks at J = 1", the test asking for three unit parts
    where J < 3 admits fewer. The test was corrected to min(3, J) after
    the run and stage c re-run; the ladder values, being exact
    minima, are identical on the re-run, and the corrected line reads
    the break at J = 6, as F4 has it from the multisets.

RUN RECORD (the estimate first, then what it cost)
Stage c: estimated seconds to two minutes, cost 871.9 s wall (peak
working set 15.1 MB, memwatch's 512 MB default) -- the estimate missed
by seven times because six of the eight ladders ran to their 90 s wall
at ranks past 30, where the exact-rational reduction is the cost, and
the product table adds its own seconds; the ladders' REACH is the
wall's and the values are exact. Stage h: estimated a minute to five,
cost 159.4 s (peak working set 115.0 MB, the backward set), J = 8 at
its wall. Stage c re-run after the F5 fix: 863.7 s, peak 15.0 MB, the same
values at every cell, L1 printing the break at J = 6.
Stage u: 200.2 s, peak 14.1 MB, three ladders re-scanned to J = 12 and
the partitions walked.
"""
import os
import sys
import time
from math import comb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_flatten_family import route_h                        # noqa: E402
from explore_flatten_lattice import divide_xm1                    # noqa: E402
from explore_flatten_offchart import Products, NodeCap, mul_shift  # noqa: E402
from explore_flatten_d2 import (Route, product_least_degree,      # noqa: E402
                                as_product, cyclotomic_floor, A059753)

K_LIST = [1, 2, 3, 4, 5, 6, 7, 8]
J_MAX = 14
W_MAX = 72
WALL_K = 90.0
PRODUCT_BUDGET = 44
HD_K = 3
HD_J_MAX = 8
HD_WALL_J = 150.0
D2_KNOWN = [1, 2, 4, 7, 11, 16, 22, 26]


def check_witness(v, J, k, degree):
    """Height, exact degree and divisibility, outside the lattice code."""
    p = list(v)
    while p and p[-1] == 0:
        p.pop()
    if len(p) - 1 != degree:
        return "degree %d, ladder says %d" % (len(p) - 1, degree)
    if max(abs(c) for c in p) > k:
        return "height %d > %d" % (max(abs(c) for c in p), k)
    q = p
    for _ in range(J):
        q, rem = divide_xm1(q)
        if rem != 0:
            return "not divisible by (x-1)^%d" % J
    return None


def chart_ladder(k, jmax, wall):
    """d_k(J) by the scan of hand attack (1); (ladder dict, reach)."""
    out, prev, t0 = {}, 0, time.time()
    for J in range(1, jmax + 1):
        M = max(prev + 1, J + 1)
        while True:
            if M > W_MAX:
                return out, "width cap %d at J = %d" % (W_MAX, J)
            if time.time() - t0 > wall:
                return out, "wall %.0f s at J = %d" % (wall, J)
            try:
                h, v, nodes, _ = route_h(M, J)
            except NodeCap:
                return out, "node cap at M = %d, J = %d" % (M, J)
            if h <= k:
                break
            M += 1
        prev = M - 1
        out[J] = (prev, v)
    return out, "complete to J = %d" % jmax


def stage_c():
    print("=== C: the chart-read ladders, k = %s, J <= %d" % (K_LIST, J_MAX))
    prods = Products(PRODUCT_BUDGET)
    ladders, kills, shape_break = {}, [], {}
    for k in K_LIST:
        lad, reach = chart_ladder(k, J_MAX, WALL_K)
        ladders[k] = lad
        print("\nk = %d  (%s)" % (k, reach))
        print("  d_%d(J) = %s" % (k, [lad[J][0] for J in sorted(lad)]))
        for J in sorted(lad):
            d, v = lad[J]
            err = check_witness(v, J, k, d)
            if err:
                kills.append("K-E k=%d J=%d witness: %s" % (k, J, err))
            fl = cyclotomic_floor(J, k)
            if d < fl:
                kills.append("K-D k=%d J=%d: %d below floor %d" % (k, J, d, fl))
            corner = comb(J, J // 2) <= k
            if (d == J) != corner:
                kills.append("K-E k=%d J=%d: d = %d, corner says %s"
                             % (k, J, d, corner))
            pd, pw = product_least_degree(prods, J, k)
            if pd is None or d > PRODUCT_BUDGET:
                law = "table short (no product of height <= %d and %d parts within sum %d)" % (k, J, PRODUCT_BUDGET) if pd is None else "table short"
            elif d < pd:
                law = "K-A: %d < product %d %s" % (d, pd, pw)
                kills.append("K-A k=%d J=%d: d = %d below product %d, witness %s"
                             % (k, J, d, pd, v))
            elif d > pd:
                law = "K-E: %d > product %d" % (d, pd)
                kills.append("K-E k=%d J=%d: d = %d above product %d %s"
                             % (k, J, d, pd, pw))
            else:
                D = as_product(v, prods)
                law = "= product %d, multiset %s%s" % (
                    pd, pw, "" if D else " (lattice witness not the table's)")
                if k == 3:
                    parts = list(pw)
                    ones = parts.count(1)
                    rest = parts[ones:]
                    fits = (ones == min(3, J) and len(rest) == len(set(rest))
                            and rest == sorted(rest))
                    if not fits and 3 not in shape_break:
                        shape_break[3] = (J, pw)
            print("  J=%2d  d=%3d  floor %3d  %s" % (J, d, fl, law))
    # monotone in k at fixed J
    for J in range(1, J_MAX + 1):
        col = [(k, ladders[k][J][0]) for k in K_LIST if J in ladders[k]]
        for (k1, d1), (k2, d2) in zip(col, col[1:]):
            if d2 > d1:
                kills.append("K-E J=%d: d_%d = %d > d_%d = %d" % (J, k2, d2, k1, d1))
    # controls
    a = [ladders[1][J][0] for J in sorted(ladders[1])]
    print("\nC1 k = 1 against A059753: %s vs %s -> %s"
          % (a, A059753[:len(a)], "AGREE" if a == A059753[:len(a)] else "KILL"))
    if a != A059753[:len(a)]:
        kills.append("C1 k=1 ladder %s != A059753" % a)
    b = [ladders[2][J][0] for J in sorted(ladders[2])]
    n = min(len(b), len(D2_KNOWN))
    print("C2 k = 2 against the height-domain ladder: %s vs %s -> %s"
          % (b[:n], D2_KNOWN[:n], "AGREE" if b[:n] == D2_KNOWN[:n] else "KILL"))
    if b[:n] != D2_KNOWN[:n]:
        kills.append("C2 k=2 ladder %s != %s" % (b[:n], D2_KNOWN[:n]))
    print("\nthe ladders side by side (rows J, columns k):")
    print("   J  " + "".join("%6s" % ("k=%d" % k) for k in K_LIST))
    for J in range(1, J_MAX + 1):
        print("  %2d  " % J + "".join(
            "%6s" % (ladders[k][J][0] if J in ladders[k] else "-") for k in K_LIST))
    if 3 in shape_break:
        print("\nL1 the k = 3 shape (1,1,1, distinct...) first breaks at J = %d: %s"
              % shape_break[3])
    else:
        print("\nL1 the k = 3 shape (1,1,1, distinct...) holds at every J read")
    return ladders, kills


def stage_h(ladders):
    print("\n=== H: the height-domain ladder at k = %d, J <= %d, wall %.0f s per depth"
          % (HD_K, HD_J_MAX, HD_WALL_J))
    route = Route()
    kills, prev, got = [], 0, {}
    for J in range(1, HD_J_MAX + 1):
        N = max(prev, J - 1)
        t0 = time.time()
        nodes = 0
        while True:
            found, n, _ = route.run(N, J, HD_K)
            nodes += n
            if found:
                break
            if time.time() - t0 > HD_WALL_J:
                print("  J=%2d  stopped at wall (degree %d refuted so far, %d nodes)"
                      % (J, N, nodes))
                print("  reach: J = %d" % (J - 1))
                return got, kills
            N += 1
        prev = N
        got[J] = N
        chart = ladders.get(HD_K, {}).get(J, (None,))[0]
        verdict = ("AGREE" if chart == N else
                   "KILL K-B (chart %s)" % chart if chart is not None else "chart unread")
        if chart is not None and chart != N:
            kills.append("K-B J=%d: height-domain %d, chart %d" % (J, N, chart))
        print("  J=%2d  d_%d = %3d  %8d nodes  %6.1f s  %s"
              % (J, HD_K, N, nodes, time.time() - t0, verdict))
    print("  reach: J = %d" % HD_J_MAX)
    return got, kills


def attaining_products(d, J, k):
    """Every multiset of J parts with degree sum d whose pure product
    has height <= k, by an exhaustive walk over the partitions of d
    into J parts."""
    out = []

    def walk(n, parts, mx, acc):
        if parts == 0:
            if n == 0:
                p = [1]
                for e in acc:
                    p = mul_shift(p, e)
                if max(abs(c) for c in p) <= k:
                    out.append(tuple(sorted(acc)))
            return
        for e in range(1, min(mx, n - (parts - 1)) + 1):
            acc.append(e)
            walk(n - e, parts - 1, e, acc)
            acc.pop()

    walk(d, J, d, [])
    return out


def stage_u():
    """The unit-part count over EVERY attaining product, not the
    table's one witness, at the read cells of k = 3, 5 and 8 to J = 12:
    a claim about the multisets is a claim about all of them."""
    print(chr(10) + "=== U: every attaining product at k = 3, 5, 8, J <= 12")
    for k in (3, 5, 8):
        lad, reach = chart_ladder(k, 12, WALL_K)
        print("k = %d (%s)" % (k, reach))
        for J in sorted(lad):
            d = lad[J][0]
            if d > PRODUCT_BUDGET:
                continue
            prods = attaining_products(d, J, k)
            ones = sorted(set(D.count(1) for D in prods))
            print("  J=%2d  d=%2d  attaining products %3d  unit-part counts %s%s"
                  % (J, d, len(prods), ones,
                     "  " + str(prods[0]) if len(prods) == 1 else ""))


def main():
    t0 = time.time()
    stages = sys.argv[1:] or ["c", "h", "u"]
    ladders, kills = {}, []
    if "c" in stages:
        ladders, k1 = stage_c()
        kills += k1
    if "h" in stages:
        if not ladders:
            ladders[3], _ = chart_ladder(3, HD_J_MAX, WALL_K)
        _, k2 = stage_h(ladders)
        kills += k2
    if "u" in stages:
        stage_u()
    print("\n=== KILLS: %s" % (kills if kills else "none"))
    print("wall %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
