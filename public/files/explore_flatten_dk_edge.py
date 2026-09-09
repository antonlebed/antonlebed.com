"""explore_flatten_dk_edge.py -- THE INVERSE DIAL PAST THE PRODUCT TABLE'S
EDGE: the pure-product law at the 9 cells the table of degree sum <= 44
left unread, and whether every cell is attained with EXACTLY J parts.

THE OBJECT. d_k(J) is the least degree of a nonzero integer polynomial
of height at most k divisible by (x-1)^J; h(M, J) the least height of a
nonzero polynomial of degree below M so divisible, a shortest vector in
the sup norm of the lattice (x-1)^J Z[x] cut at degree < M
(explore_flatten_lattice.py, explore_flatten_family.py). The two are
inverses, h(M, J) <= k iff M > d_k(J). A PURE PRODUCT is
prod_i (x^{d_i} - 1) over a multiset of positive parts; with c parts it
is divisible by (x-1)^c exactly and has degree the part sum, so a
product with at least J parts and height at most k is a lattice vector
and d_k(J) is at most its degree. THE LAW: d_k(J) equals the least
degree of a pure product of height at most k with J parts.

WHAT IS KNOWN. explore_flatten_dk.py read the ladders d_k(J) at
k = 1..8 and J to 14 off the chart, 99 cells, and read the law against
a product table enumerating multisets of degree sum <= 44: it holds at
the 90 cells the table reaches and is UNREAD at the 9 past it -- k = 1
at J = 9, 10, 11 (48, 61, 69), k = 2 at J = 10, 11 (45, 51), k = 5 and
6 at J = 13 (46, 46), k = 7 and 8 at J = 14 (49, 47). The classical row
k = 1 is read separately by explore_flatten_offchart.py, whose
attainment search runs to degree 69 and exhibits a distinct-part product
at every n <= 11, so the three k = 1 cells are unread by the TABLE and
read by that rig. That table also kept one witness per (count, sum) and
counted parts AT LEAST J, while the doc and the page state the law with
J parts; stage u of the dk rig enumerated every exact-J product at
k = 3, 5, 8 only.

THE QUESTION. (Q1) Does the law hold at the 6 unread cells past the
classical row? (Q2) At every one of the 99 cells, is d_k(J) attained by
a product with EXACTLY J parts, or does some cell need more?

THE HAND ATTACK. The law at a cell (k, J, d) is decided by a finite
walk: d is the lattice minimum, so no multiple of (x-1)^J of height
<= k has degree below d, and the law holds iff some product with at
least J parts, part sum exactly d, has height <= k. A product with
c > J parts and sum d is also divisible by (x-1)^J, so Q1 asks over
c >= J and Q2 asks whether c = J suffices. The walk is over partitions
of d into c parts, each expanded by shifted subtractions
(explore_flatten_offchart.py mul_shift); partitions of 51 into 11 parts
number in the tens of thousands, partitions of 51 into at least 11
parts in the low hundreds of thousands, so every cell is seconds. A
timing call of the exact-J walk at (45, 10, 2), (51, 11, 2) and
(47, 14, 8) was made before this file was written and printed one
product at each; the predictions below were fixed as the transplant
from the 90 read cells would have fixed them and are not sharpened by
it. The height of a partial product is not monotone in the parts (a
factor x^e - 1 can lower it), but a walk in NONDECREASING part order
prunes exactly: every factor still to come has degree at least the
next part e, and multiplying by x^m - 1 with m >= e negates the
coefficients below degree e and touches nothing else there, so the
coefficients of the final product below degree e are the partial
product's up to sign. A partial product with a coefficient beyond k
below the next part admits no completion, and since that test only
tightens as e grows the loop over e breaks at the first failure. At
k = 1 the prune already bounds the unit parts by 1 (the x^1
coefficient is the unit-part count up to sign) and the parts equal
to 2 by 1, which is what makes the classical column's walks over
every part count cheap.

The chart side is re-read rather than copied: at every cell both
h(d+1, J) <= k and h(d, J) > k are read again by the lattice route,
under a per-cell wall, so the table this rig takes from the dk rig's
print is held to the instrument in the same run. A cell whose lattice
read misses its wall is printed as such and its law read stays a read
against the copied value.

PREDICTIONS, FIXED BEFORE THE RUN (what the engine prints).
  C1 CONTROL: at k = 2, J = 8, d = 26 the exact-J walk lists
     (1, 1, 2, 3, 3, 4, 5, 7) among its products, and at k = 3, J = 11,
     d = 43 it lists exactly one product, (1, 1, 2, 2, 3, 4, 4, 5, 6, 7,
     8), the dk rig's stage u print. KILL: either missing.
  C2 CONTROL, the chart: at every cell h(d+1, J) <= k and h(d, J) > k
     (or the cell's wall is printed). KILL: a cell where the chart
     disagrees with the copied table, which is a copy error in this
     file or in the dk rig's docstring, fixed before any law is read.
  E1 THE LAW AT THE EDGE: at each of the 6 unread cells past the
     classical row, at least one product with at least J parts, sum d
     and height <= k exists (TRANSPLANT from the 90 read cells). KILL
     K-A: a cell with none -- product extremality refuted on the
     inverse dial, the lattice witness of that cell then printed with
     its height, and the doc's law rewritten to the cells that hold.
  E2 EXACTLY J PARTS SUFFICE: at every one of the 99 cells the exact-J
     walk is nonempty (TRANSPLANT from the 37 cells of stage u). KILL
     K-C: a cell attained only with more than J parts; the law's
     wording on the doc and the page then reads "at least J parts".
  E3 THE CLASSICAL CELLS: at k = 1, J = 9, 10, 11 the exact-J walk
     contains a distinct-part product (the offchart rig's witnesses).
     KILL: none found, a disagreement between two rigs decided by the
     witness.
  O1 OBSERVATION, no prediction: the number of attaining products with
     exactly J parts and with more than J parts at every cell, and the
     unit-part counts at the 6 edge cells, read against the dk rig's
     finding that the count follows no rule.

THE DESIGN. Exact integers throughout. The table is copied from the dk
rig's F2 print; stage l re-reads it from the chart (route_h, wall 120 s
per cell, the deepest cell k = 1, J = 11 at rank 59 the likely miss);
stage p walks the products at every cell over every part count
c >= J at sum d, split c = J against c > J. Estimate: stage p under
two minutes, stage l two to ten minutes
dominated by the k = 1 column's ranks; memory a few reduced bases,
far under the ceiling. Stages (argv): p the product walks, l the
lattice re-read; both by default.

FINDINGS (each at its own tier; the prints copied, the asserts read)

F1  THE CONTROLS HOLD. C1: (2, 8) lists (1, 1, 2, 3, 3, 4, 5, 7) and
    (3, 11) lists exactly (1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 8). C2: the
    chart re-read agrees with the copied table at every one of the 99
    cells, h(d+1, J) <= k < h(d, J), no cell past its wall (the slowest
    30 s, at k = 7, J = 14). E3: at k = 1 the exact-J walk finds one
    product at each of J = 9, 10, 11, distinct-part in each case --
    (1, 2, 3, 4, 5, 6, 7, 9, 11), (1, 2, 3, 4, 5, 6, 7, 9, 11, 13),
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13) -- the offchart rig's witnesses.
F2  THE LAW HOLDS AT EVERY ONE OF THE 99 CELLS (rule, exact; E1 and E2
    hold, K-A and K-C never printed). At each of the 9 edge cells a
    product of exactly J parts and sum d_k(J) has height <= k, so the
    unread cells close: (1, 1, 2, 3, 3, 4, 5, 7, 8, 11) at k = 2,
    J = 10 and (1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 11) at J = 11;
    (1, 1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 7, 11) at k = 5, J = 13 and two
    products at k = 6 there (unit-part counts 3 and 4);
    (1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 7, 11) at k = 7, J = 14 and
    (1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 7, 11) at k = 8. Exactly J
    parts attain at all 99 cells, so the law's wording stands.
F3  NO CELL IS ATTAINED WITH MORE THAN J PARTS (rule, read at all 99
    cells): the more-than-J count is 0 everywhere. Below a column's
    last row it is forced: a product with c > J parts, sum d_k(J) and
    height <= k would give d_k(c) <= d_k(J), and every column of the
    table is strictly increasing in J wherever it is read; at each
    column's last row, where d_k(J+1) is past the wall, the walk alone
    reads it.
F4  THE ATTAINING PRODUCT IS UNIQUE AT 91 OF THE 99 CELLS (observation),
    two at the other eight: (8, 6), (5, 7), (1, 8), (5, 8), (6, 9),
    (6, 11), (5, 12), (6, 13) as (k, J), and none with three or more.
    At every edge cell past the classical row an attaining product
    carries the part 11 -- at (6, 13) one of the two does, the other
    ending in 9 -- as do the classical column's witnesses at
    J = 9, 10, 11.

RUN RECORD (the estimate first, then what it cost)
Stage p: estimated under two minutes, cost 3.3 s (peak working set
13.4 MB, memwatch's 512 MB default); re-run after the print was
widened to show both products at a two-product cell, 3.3 s, the same
values -- the prune of the hand attack
makes the k = 1 column's full-part-count walks sub-second at degree
69. Stage l: estimated two to ten minutes, cost 171.6 s (peak 14.1 MB),
the k = 1 column's deep cells under 25 s each.
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_flatten_family import route_h                        # noqa: E402
from explore_flatten_offchart import mul_shift, NodeCap            # noqa: E402

# d_k(J), rows J = 1..14, columns k = 1..8; None past a ladder's wall.
# Copied from explore_flatten_dk.py F2.
TABLE = {
    1:  [1, 1, 1, 1, 1, 1, 1, 1],
    2:  [3, 2, 2, 2, 2, 2, 2, 2],
    3:  [6, 4, 3, 3, 3, 3, 3, 3],
    4:  [11, 7, 5, 5, 5, 4, 4, 4],
    5:  [15, 11, 8, 8, 6, 6, 6, 6],
    6:  [22, 16, 11, 10, 9, 9, 9, 9],
    7:  [30, 22, 17, 14, 14, 11, 11, 11],
    8:  [41, 26, 20, 19, 18, 16, 15, 15],
    9:  [48, 34, 27, 22, 22, 21, 20, 19],
    10: [61, 45, 33, 29, 27, 23, 23, 23],
    11: [69, 51, 43, 34, 30, 30, 25, 25],
    12: [None, None, None, 44, 38, 36, 32, 31],
    13: [None, None, None, None, 46, 46, 37, 37],
    14: [None, None, None, None, None, None, 49, 47],
}
K_LIST = [1, 2, 3, 4, 5, 6, 7, 8]
TABLE_EDGE = 44
WALL_L = 120.0


def cells():
    for J in sorted(TABLE):
        for i, k in enumerate(K_LIST):
            d = TABLE[J][i]
            if d is not None:
                yield k, J, d


def products_at(d, J, k):
    """Every multiset of at least J parts with sum d whose pure product
    has height <= k, by a walk over the partitions in nondecreasing
    part order with the exact prune of the hand attack; returns
    (exact-J list, more-than-J list)."""
    exact, more = [], []

    def walk(n, mn, acc, p):
        if n == 0:
            if len(acc) >= J and max(abs(x) for x in p) <= k:
                (exact if len(acc) == J else more).append(tuple(acc))
            return
        for e in range(mn, n + 1):
            if max(abs(x) for x in p[:e]) > k:
                break
            acc.append(e)
            walk(n - e, e, acc, mul_shift(p, e))
            acc.pop()

    walk(d, 1, [], [1])
    return exact, more


def stage_p():
    print("=== P: the product walks at every cell, c = J and c > J at sum d")
    kills = []
    rows = {}
    for k, J, d in cells():
        t0 = time.time()
        exact, more = products_at(d, J, k)
        rows[(k, J)] = (d, exact, more)
        edge = "EDGE" if d > TABLE_EDGE else "    "
        ones = sorted(set(D.count(1) for D in exact))
        print("  k=%d J=%2d d=%2d %s  exact-J %4d  more-than-J %4d  unit parts %s  %.1fs%s"
              % (k, J, d, edge, len(exact), len(more), ones,
                 time.time() - t0,
                 "  " + " ".join(str(D) for D in exact) if len(exact) <= 2 else ""))
        if d > TABLE_EDGE and k > 1 and not exact and not more:
            kills.append("K-A at k=%d J=%d d=%d" % (k, J, d))
        if not exact and more:
            kills.append("K-C at k=%d J=%d d=%d" % (k, J, d))
        if not exact and not more and d <= TABLE_EDGE:
            kills.append("K-E read cell empty at k=%d J=%d d=%d" % (k, J, d))
    # C1
    ok1 = (1, 1, 2, 3, 3, 4, 5, 7) in rows[(2, 8)][1]
    ok2 = rows[(3, 11)][1] == [(1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 8)]
    print("\nC1 (2, 8) lists (1,1,2,3,3,4,5,7): %s; (3, 11) lists exactly %s: %s"
          % (ok1, (1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 8), ok2))
    if not (ok1 and ok2):
        kills.append("C1")
    # E3
    for J in (9, 10, 11):
        d, exact, _ = rows[(1, J)]
        distinct = [D for D in exact if len(set(D)) == len(D)]
        print("E3 k=1 J=%d d=%d: %d exact-J products, %d with distinct parts %s"
              % (J, d, len(exact), len(distinct), distinct[:2]))
        if not distinct:
            kills.append("E3 at J=%d" % J)
    edge = [(k, J, d) for k, J, d in cells() if d > TABLE_EDGE]
    print("E1 the %d edge cells: %s" % (len(edge), [
        "k=%d J=%d d=%d %s" % (k, J, d, "holds" if rows[(k, J)][1] or rows[(k, J)][2] else "FAILS")
        for k, J, d in edge]))
    empty_exact = [(k, J) for (k, J), (d, e, m) in rows.items() if not e]
    print("E2 cells with no exact-J product: %s" % (empty_exact if empty_exact else "none of 99"))
    return kills


def stage_l():
    print("\n=== L: the chart re-read at every cell, h(d+1, J) <= k < h(d, J), wall %.0f s" % WALL_L)
    kills, missed = [], []
    for k, J, d in cells():
        t0 = time.time()
        try:
            hi = route_h(d + 1, J)[0]
            lo = route_h(d, J)[0] if d > J else None   # d = J is the rank-1 corner, h(J, J) undefined
        except NodeCap:
            missed.append((k, J))
            print("  k=%d J=%2d d=%2d  node cap" % (k, J, d))
            continue
        dt = time.time() - t0
        ok = hi <= k and (lo is None or lo > k)
        print("  k=%d J=%2d d=%2d  h(d+1)=%s h(d)=%s  %s  %.1fs"
              % (k, J, d, hi, lo, "ok" if ok else "DISAGREE", dt))
        if not ok:
            kills.append("C2 at k=%d J=%d" % (k, J))
        if dt > WALL_L:
            missed.append((k, J))
    print("C2: %s; cells past the wall: %s" % ("agree at every cell" if not kills else kills,
                                               missed if missed else "none"))
    return kills


def main():
    t0 = time.time()
    stages = sys.argv[1:] or ["p", "l"]
    kills = []
    if "p" in stages:
        kills += stage_p()
    if "l" in stages:
        kills += stage_l()
    print("\n=== KILLS: %s" % (kills if kills else "none"))
    print("wall %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
