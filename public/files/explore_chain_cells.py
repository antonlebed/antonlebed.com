"""The cell classification across radices: does any digit-set cell at
radix 6 or above admit an aligned chain reading below the sum of its
units' floors under the escape law, or is the radix-4 gain an
accident of one cell?

THE QUESTION. explore_chain_product.py prices the aligned chain
(x y) z by the escape law: the chain survives at lookaheads (L1, L2)
iff the product consumer's escape cost
    E2(L2) = max(0, w (1 + Mh) - b^L2 (w - 1) / Mh)
fits the producer's slack budget
    S(L1) = w - 1 - 2 Mh w / b^L1,
and at the 13 representable cells of radices 2..5 the chain reads
below the naive sum L1* + L2* at exactly one, (4,2,2) at (2, 1),
where E2 = S = 2/9. If cells with a gain recur at higher radices, the
gain is a classification of (radix, digit set) cells by two closed
forms and the digit set is a design axis for latency; if none recurs,
the radix-4 gain is one cell's accident. This rig prints the closed
forms at every representable cell of radices 2..16.

CONVENTIONS, as in explore_chain_product.py: digit set {-am..ap},
M-+ = a-+/(b - 1), w = M- + M+, Mh = max(M-, M+), rho = am + ap + 1 - b
>= 1, w - 1 = rho/(b - 1); a cell is representable iff
am^2 <= ap (b - 1); L1* is the least L with b^L (w - 1) >= 2 Mh w and
L2* the least with b^L (w - 1) >= (Mh + Mh^2) w.

THE REDUCTION, derived before the run. A pair (L1, L2) below the
naive sum with S(L1) >= 0 needs L1 >= L1*, hence
L2 <= L2* - 1 - (L1 - L1*), and E2(L2) > 0 there. At radices b >= 6
the slack w - 1 >= 1/(b - 1) gives b^2 (w - 1) >= b^2/(b - 1) > 4 >=
2 w >= (Mh + Mh^2) w, so L2* <= 2 at every cell, and the only
candidate pair is (L1*, L2* - 1) at a cell with L2* = 2, alive iff
    w Mh + 1 + 2 Mh w / b^L1*  <=  b (w - 1) / Mh.
By hand at radix 6, nine representable cells: L2* = 1 at (6,3,3),
(6,3,4), (6,3,5), (6,4,4), (6,4,5) and (6,5,5); L2* = 2 at (6,1,5),
(6,2,4) and (6,2,5), where E2(1) - S(2) is 6/5 - 2/15, 33/50 - 11/75
and 2/5 - 29/90 = 7/90, the last the nearest miss.

PREDICTIONS, fixed before the run.
 P1 (the control): radices 2..5 reprint explore_chain_product.py's
    table, 13 cells, one alive pair below the naive sum, (4,2,2) at
    (2, 1) with E2 = S = 2/9.
 P2: radices 6..9 print NO alive pair below the naive sum at any
    cell; the nearest miss at radix 6 is (6,2,5) at (2, 1), by 7/90.
 P3 (a transplant from the radix-4 symmetric cell): at the symmetric
    minimal-redundancy cells (b, b/2, b/2), b even >= 6, L2* = 1,
    since (Mh + Mh^2) w = 2 m^2 (1 + m) with m = b/(2 (b - 1)) falls
    toward 3/4 while b (w - 1) = b/(b - 1) stays above 1.

KILLS, as prints.
 K1: P1's reprint differs from the recorded table -> the closed forms
     are miswired; nothing below is read.
 K2: an alive pair below the naive sum at any cell of radices 6..9 ->
     the classification hypothesis survives its first kill and owes
     the covering search at that pair
     (explore_chain_product.py's certify_product_chain).
     No alive pair -> the hypothesis is killed: the radix-4 gain is one
     cell's accident, and every cell above radix 5 classifies as no
     gain.

FINDINGS (entered after the run; every number below is in this
file's print at BMAX = 40).

F1 THE CONTROL HOLDS. 13 cells at radices 2..5, one alive pair below
   the naive sum, (4,2,2) at (2, 1), E2 = S = 2/9. K1 never fired.
F2 P2 MISSED: THE GAIN RECURS. Radices 6..9 print two alive pairs,
   (9,4,5) and its mirror (9,5,4) at (2, 1), with E2 = 9/320 against
   S = 31/288 -- not a knife edge, a margin of 916/11520 of a cell;
   the chain reads (x y) z at 3 against the naive 4 and the fused 2.
   K2 fired: the hypothesis survives its first kill half and owes the
   covering search, which the certifier cannot reach at this radix:
   its first level (n = 2, images at level 4) is 54 million (x, y)
   prefix pairs against a cap of one million. The box model supports
   what it reaches: the consumer at the escape insets (9/640, 9/640)
   is clear at level 2 (its budget), the narrowed producer kills at
   L - 1 at level 2 and is unreached at L = 2.
F3 THE GOLDEN WINDOW [rule to radix 40; the reduction proved]. The
   alive pairs to radix 40 are all at (2, 1) and all at slack rho = 1:
   (4,2,2), (9,4,5), (12,5,7), (17,7,10), (22,9,13), (25,10,15),
   (30,12,18), (33,13,20), (38,15,23) and their mirrors, nine of the
   37 radices 4..40, and no slack-2 cell gains anywhere. At rho = 1,
   w = b/(b - 1) makes b (w - 1) = w, so the consumer's floor is
   L2* = 2 iff Mh + Mh^2 > 1, iff Mh exceeds 1/phi = 0.618 -- the
   criterion agrees at all 480 slack-1 cells -- and the alive
   condition w Mh + 1 + 2 Mh w / b^2 <= b (w - 1)/Mh reads
   b (Mh + 1 - 1/Mh) <= 1 - 2 Mh / b: the hull height must sit
   ABOVE 1/phi and within about 0.28/b of it. The gaining heights are
   the rationals j/(b - 1) just above 1/phi: 2/3, 5/8 (at b = 9, 17,
   25, 33), 7/11, 13/21, 18/29, 23/37 -- the golden convergents from
   above and their mediants -- with Mh - 1/phi from +0.048 at radix 4
   down to +0.001 at (22,9,13). The nearest miss at every other radix
   but 20 is the cell (b, 2, b - 1), slack 2 and Mh = 1, where
   E2(1) = w - 1 and E2 - S = 2w/b^2 exactly, a miss that shrinks as
   1/b^2 and never closes (radix 2 has no such cell); at radix 20 the slack-1 cell (20,8,12),
   Mh = 12/19 just outside the window, misses by 8/5415.
F4 P3 HELD: the symmetric cells (b, b/2, b/2) have L2* = 1 at every
   even b from 6 to 40, their Mh = b/(2 (b - 1)) below 1/phi from
   b = 6 on.

VERDICT. The radix-4 gain is not one cell's accident: it is the first
member of a golden window, the slack-1 cells whose hull height is a
rational just above 1/phi, recurring at about a quarter of the
radices to 40 and at (2, 1) every time. What the law promises at
those cells past radix 4 is uncertified: the covering certificate at
(9,4,5) needs a certifier that streams the product's image set (its
sign symmetry cuts the 54 million to 14 million intervals, and the
covering is a sorted one-dimensional assignment), and the rig above
records the box-model support only to the depth its budgets reach.

RUN RECORD: pure Python, exact rationals, standard library; under
memwatch, peak commit 8.3 MB, wall 1.5 s at BMAX = 40.
Run: python prime/code/explore_chain_cells.py [BMAX]
"""

import os
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_chain_delay import (window, margin_L, slack_budget,   # noqa: E402
                                 census, representable_xy)
from explore_chain_product import (least_L, escape_cost_product,   # noqa: E402
                                   chain_floor_product, boxes_at, plain_boxes,
                                   scan_levels, prod_interval, fmt)
from explore_chain_delay import narrowed_L   # noqa: E402

FAILURES = []


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


def cell_row(b, am, ap):
    Mm, Mp, w, Mh = window(b, am, ap)
    L1s = margin_L(b, am, ap, 2 * Mh)
    L2s = least_L(b, w, (Mh + Mh * Mh) * w)
    naive = L1s + L2s
    best = chain_floor_product(b, am, ap)
    # the nearest miss: the least E2 - S over the pairs below the naive sum
    miss = None
    for L1 in range(L1s, naive):
        for L2 in range(0, naive - L1):
            gap = escape_cost_product(b, am, ap, L2) - slack_budget(b, am, ap, L1)
            if miss is None or gap < miss[0]:
                miss = (gap, L1, L2)
    return L1s, L2s, naive, best, miss


def main():
    bmax = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    t0 = time.time()
    alive = {}
    nearest = {}
    print("=== the closed forms per cell: L1* L2* | naive | informed (L1,L2,E2,S) | nearest miss below naive (E2-S at (L1,L2))")
    for b in range(2, bmax + 1):
        cells = [(bb, am, ap) for (bb, am, ap) in census(b) if bb == b and representable_xy(bb, am, ap)]
        n2 = 0
        for (bb, am, ap) in cells:
            L1s, L2s, naive, best, miss = cell_row(b, am, ap)
            n2 += L2s >= 2
            if best[0] < naive:
                alive.setdefault(b, []).append(((b, am, ap), best))
            if miss is not None and (b not in nearest or miss[0] < nearest[b][0]):
                nearest[b] = (miss[0], (b, am, ap), miss[1], miss[2])
            if b <= 9:
                m = f"{miss[0]} at ({miss[1]},{miss[2]})" if miss else "-"
                print(f"  ({b},{am},{ap}) | {L1s} {L2s} | {naive} | {best[0]} ({best[1]},{best[2]},{best[3]},{best[4]}) | {m}")
        na = len(alive.get(b, []))
        nm = nearest.get(b)
        print(f"  radix {b}: {len(cells)} cells, L2* >= 2 at {n2}, alive below naive at {na}"
              + (f"; nearest miss {nm[0]} at {nm[1]} ({nm[2]},{nm[3]})" if nm else ""))

    print("\n=== P1, the control: radices 2..5")
    low = [(c, best) for b in range(2, 6) for (c, best) in alive.get(b, [])]
    n_cells = sum(1 for (b, am, ap) in census(5) if representable_xy(b, am, ap))
    print(f"  {n_cells} cells; alive below naive: {low}")
    ok(n_cells == 13 and len(low) == 1 and low[0][0] == (4, 2, 2)
       and low[0][1][1:3] == (2, 1) and low[0][1][3] == Fr(2, 9) and low[0][1][4] == Fr(2, 9),
       f"K1 the control differs from the recorded table: {n_cells} cells, {low}")
    if FAILURES:
        print("POSITIVE CONTROL FAILED; nothing below is read")
        return

    print("\n=== P2, the kill: radices 6..9")
    high = [(c, best) for b in range(6, 10) for (c, best) in alive.get(b, [])]
    print(f"  alive below naive at radices 6..9: {high if high else 'none'}")
    print(f"  nearest miss at radix 6: {nearest[6]}")
    print("  " + ("K2: an alive pair; the hypothesis survives and owes the covering search"
                  if high else "no alive pair: the radix-4 gain is one cell's accident"))
    beyond = [(c, best) for b in range(10, bmax + 1) for (c, best) in alive.get(b, [])]
    print(f"  alive below naive at radices 10..{bmax}: {beyond if beyond else 'none'}")

    print("\n=== P3, the symmetric minimal-redundancy cells (b, b/2, b/2)")
    for b in range(4, bmax + 1, 2):
        L1s, L2s, naive, best, miss = cell_row(b, b // 2, b // 2)
        print(f"  ({b},{b // 2},{b // 2}) L1*={L1s} L2*={L2s}")

    print("\n=== the gaining cells to radix {}: slack rho, Mh, Mh - 1/phi, (L1,L2), E2, S".format(bmax))
    inv_phi = (5 ** 0.5 - 1) / 2
    rhos = set()
    for b in range(2, bmax + 1):
        for ((bb, am, ap), best) in alive.get(b, []):
            rho = am + ap + 1 - b
            Mh = max(Fr(am, b - 1), Fr(ap, b - 1))
            rhos.add(rho)
            print(f"  ({b},{am},{ap}) rho={rho} Mh={Mh}={float(Mh):.4f} Mh-1/phi={float(Mh) - inv_phi:+.4f} "
                  f"({best[1]},{best[2]}) E2={best[3]} S={best[4]}")
    print(f"  slacks of the gaining cells: {sorted(rhos)}")

    print("\n=== the golden criterion at every slack-1 cell to radix {}: L2* = 2 iff Mh + Mh^2 > 1".format(bmax))
    agree = tot = 0
    for b in range(2, bmax + 1):
        for (bb, am, ap) in census(b):
            if bb != b or not representable_xy(b, am, ap) or am + ap + 1 - b != 1:
                continue
            Mm, Mp, w, Mh = window(b, am, ap)
            L2s = least_L(b, w, (Mh + Mh * Mh) * w)
            tot += 1
            agree += (L2s == 2) == (Mh + Mh * Mh > 1)
    print(f"  {tot} slack-1 cells, criterion agrees at {agree}")
    ok(agree == tot, "the golden criterion fails at a slack-1 cell")

    print("\n=== the box-model support at (9,4,5) (2,1), nmax 3: the consumer at the escape insets, the producer narrowed")
    b, am, ap = 9, 4, 5
    Mm, Mp, w, Mh = window(b, am, ap)
    E = escape_cost_product(b, am, ap, 1)
    half = E / 2
    rng = (-Mm * Mp, Mh * Mh)
    mk1 = lambda n: boxes_at(b, am, ap, n, (half, half), rng)
    mk2 = lambda n: plain_boxes(b, am, ap, n)
    cs = scan_levels(b, am, ap, 1, 0, mk1, mk2, prod_interval, 2, 4)
    Ln = narrowed_L(b, am, ap, half, half)
    pk = scan_levels(b, am, ap, Ln - 1, 0, mk2, mk2, prod_interval, Ln, Ln + 3, cell=(half, half))
    ps = scan_levels(b, am, ap, Ln, 0, mk2, mk2, prod_interval, Ln + 1, Ln + 3, cell=(half, half))
    print(f"  insets ({half},{half}); consumer at L2=1: {fmt(cs)}; producer narrowed L={Ln}: at L-1 {fmt(pk)}, at L {fmt(ps)}")
    print("  the covering certificate at this pair is beyond the certifier's image cap (54 million images at its first level)")
    print(f"\nwall {time.time() - t0:.1f}s; failures: {len(FAILURES)}")


if __name__ == "__main__":
    main()
