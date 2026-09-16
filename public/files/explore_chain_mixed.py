"""The mixed chain: is a chained on-line datapath's least delay a sum
over its edges of one table entry each, or can two edge gains that
each hold alone fail to hold together?

THE QUESTION. Two rigs read chains under the escape law's closed forms.
explore_threshold_miss.py prices a two-unit chain's gain as a
threshold miss at the consumer's own root: 1/phi for a product fed by
a product, b/(b + 2) for a product fed by a sum. explore_chain_three.py
prices the three-product chain (x y) z u and finds it decided link by
link: 26 cells below the naive sum of floors, none gaining at two
links. If that composition held for every consumer family, a
datapath's least delay would be the sum of its units' floors less one
table entry per edge (the edge's pairwise gain, keyed by radix, digit
set and consumer root), and digit-serial synthesis would be a lookup.
But the three-product chain never TESTED the sum: its second link's
window sits above 1/phi = 0.618 and its third link's above 0.682, the
root of M + M^3 = 1, and no slack-1 lattice height j/(b - 1) lands
inside both windows, so no cell there had two pairwise gains to add.
This rig reads a chain whose two windows overlap.

THE CHAIN. S = x + y (the sum, lead 1, lattice images), P = z (S/b)
(the middle product), Q = P u (the third product), every stream on the
same signed-digit window (b, am, ap), Mh = max(M-, M+), w = M- + M+.
  the sum      floor L1* = sum_law, budget S1(L1) = (w - 1) - (2w - 1)/b^L1
               (the lattice budget; the dense one, pitch 0, is the
               second arm, read only at the cells where it is
               nonnegative at L1*), its stream's top A1 = 2 Mh / b;
  the middle   alive at L2 with upstream inset I1 iff
               A1 w + Mh (w - I1) <= b^L2 (w - 1), its leftover (a
               TRANSPLANT of the hull-overlap argument, as in
               explore_chain_three.py)
               S2(L2, I1) = (w - 1) - (A1 w + Mh (w - I1)) / b^L2,
               its stream's top A2 = Mh A1 = 2 Mh^2 / b;
  the third    alive at L3 with inset I2 iff
               A2 w + Mh (w - I2) <= b^L3 (w - 1).
Representable where both products fit the cell: 2 Mh^2 <= b M+ and
2 Mh^3 <= b M+ (the second implied by the first when Mh <= 1).

THE HAND-ATTACK. The middle's threshold is Lam2 = Mh (1 + 2/b) = 1,
root b/(b + 2); the third's is Lam3 = Mh + 2 Mh^2 / b = 1, root near
1 - 2/(b + 4), ABOVE the middle's by about 4/b^2. The middle gains at
(b, 2, b - 2), Mh = (b - 2)/(b - 1), at every radix 5..40
(explore_threshold_miss.py F3). At that height
    Lam3 - 1 = (b^2 - 7b + 8) / (b (b - 1)^2),
negative at b = 5 and positive from b = 6, so the third's floor is 2
there from radix 6. Its pairwise gain with the middle at its floor 2
and no upstream inset needs Lam3 - 1 <= (Mh/w) S2(2, 0) =
(Mh/b)(1 - Lam2/b); at b = 7 that is 2/63 = 0.032 against
415/4116 = 0.101, and asymptotically (1 - 5/b)/b against (1 - 2/b)/b,
so it holds at every radix past a small one. So from radix 6 the cell
and its mirror carry TWO pairwise gains, g12 = g23 = 1, and the table
reads the chain at L1* + L2* + L3* - 2 = 4.
The chain at (2, 1, 1): I1 = S1(2) = 41/294 at b = 7, the middle's
leftover at L2 = 1 is (1/b)(w (1 - Lam2) + Mh I1) = 58/12348 = 0.0047,
and the third at L3 = 1 needs Mh I2 >= w (Lam3 - 1) = 1/27, I2 >=
0.044, ten times the leftover. Every other triple summing to 4 puts a
unit two below its floor or the sum below its own. So the chain reads
5 there: the middle that gains spends the leftover the third's gain
needs. The prediction is structural, not a b = 7 accident: a middle
unit below its floor at slack 1 has leftover at most Mh I1 / b =
O(1/b^2), while the third's need is w (Lam3 - 1) / Mh = Theta(1/b).

THE ARMS, per representable cell of radices 2..BMAX:
  NAIVE     L1* + L2* + L3*.
  TABLE     NAIVE - g12 - g23, the edges' pairwise gains: g12 from the
            sum and middle alone (the middle's inputs at their plain
            width downstream of nothing), g23 from the middle and third
            alone (the middle's input inset I1 = 0).
  CONTRACT  the least L1 + L2 + L3 with every budget passed down the
            chain at its maximum, I1 = S1(L1), I2 = max(0, S2(L2, I1)).
  MATCHING  NAIVE - max(g12, g23): the reading in which two gains
            sharing a unit exclude each other. Printed beside the kill,
            never part of it.

CONTROLS, run FIRST; nothing below is read if one is red.
 C1 the two-unit sum-fed gains reproduce explore_threshold_miss.py F3:
    under the lattice budget, 72 cells, (b, 2, b - 2) and its mirror at
    every radix 5..40, and the same set under the dense budget.
 C2 the generic engine, handed the product chain's forms (budget
    (w - 1) - 2 Mh w / b^L1, A1 = Mh^2, A2 = Mh^3, representable_xy),
    reprints explore_chain_three.py F2 and F3: 26 cells below NAIVE, 0
    cells with CONTRACT < LOCAL, none gaining at two links.
 C3 the knife edge at (4,2,2): the product chain's middle leftover at
    L1 = 2, L2 = 1 is exactly 0.

PREDICTIONS, fixed before the run.
 P1 g12 = g23 = 1 at (b, 2, b - 2) and its mirror at every radix from
    6 to 40 whose representability holds, and CONTRACT = NAIVE - 1 =
    TABLE + 1 at every one of them: 70 cells.
 P2 CONTRACT = MATCHING at every representable cell of the mixed chain
    under both budgets.
 P3 at b = 5 the third's floor is 1 at (5, 2, 3), so g23 = 0 and
    CONTRACT = TABLE there.

KILLS, as prints.
 K1 any control red -> nothing below is read.
 K2 THE DELAY TABLE (the moonshot list): the count of cells with
    CONTRACT != TABLE is printed; one or more kills it and names the
    cells. Zero keeps it on this chain.

FINDINGS (entered after the run; every number is in this file's print
at BMAX = 40).

F1 THE CONTROLS HOLD. C1: the sum-fed two-unit gains are 72 cells at
   radices 5..40 under both budgets, explore_threshold_miss.py F3's
   set. C2: the generic engine on the product chain prints 26 cells
   below NAIVE, 0 with CONTRACT < LOCAL, 0 gaining at two links. C3:
   S1(2) = 2/9 and the middle leftover at (4,2,2), L2 = 1, is 0.
F2 THE TABLE DIES (rule to radix 40 under the closed forms, the middle
   budget the transplant above). 70 of 10622 representable cells carry
   two pairwise gains, and CONTRACT != TABLE at exactly those 70:
   (b, 2, b - 2) and its mirror at every radix 6..40, each reading
   CONTRACT 5 = NAIVE 6 - 1 against TABLE 4, alive at (2, 1, 2) and
   (2, 2, 1) alike at all 70: either gain lands, never both.
   K2 fired; P1 held, the predicted set equal to the kill set. The
   dense budget, read at the 9881 cells where it is nonnegative at L1*
   (741 slack-2-or-deeper cells skipped), prints the same 70.
F3 ADJACENT GAINS EXCLUDE EACH OTHER (pattern; on the product chain
   only vacuously, no cell there carrying two pairwise gains). CONTRACT = NAIVE - max(g12, g23) at every read cell
   under both budgets, 0 exceptions: P2 held. At (7,2,5) the gaining
   middle's leftover is 29/6174 = 0.0047 against the third's need
   2/45 = 0.044, as the hand-attack said.
F4 THE ROOTS DECIDE THE OVERLAP. At (5, 2, 3) the third's floor is 1
   (Lam3 < 1 there) and the chain gains once, at the second link:
   P3 held. The product chain never met F2 because its two roots,
   0.618 and 0.682, are 0.064 apart and no slack-1 height sits in both
   windows; here they are about 4/b^2 apart and the cell (b, 2, b - 2)
   sits in both from radix 6.
F5 A SLACK-2 GAIN (observation, one cell). (3,2,2), Mh = 1, rho = 2,
   gains at the third link: floors (1, 2, 2), the chain at (1, 2, 1).
   The product chain has no slack-2 gain to radix 40; this one rides
   the middle's transplanted leftover and no covering search has
   checked it.

VERDICT. A chained datapath's least delay is not a sum of per-edge
table entries: where the sum-fed consumer's root b/(b + 2) and the
next product's root sit within one lattice step, one cell carries two
pairwise gains and the chain takes one, since a middle unit below its
floor keeps a leftover O(1/b^2) while the next gain there needs Theta(1/b).
What the two chains read is a MATCHING: on a path, the gains taken are
edges sharing no unit. Not walked: chains past three units, where
non-adjacent gains would test the matching reading, fan-in, and a
covering check of the middle budget.

RUN RECORD: pure Python, exact rationals, standard library; under
memwatch, peak commit 8.7 MB, wall 19.8 s at BMAX = 40. The first run
read the dense arm at every cell and printed negative gains at the
slack-2 cells where the dense budget is negative at the sum's floor;
the arm now skips those cells and says how many. The tie line (both
minimal triples alive) was added at the audit and the run repeated,
every other print unchanged.
Run: python prime/code/explore_chain_mixed.py [BMAX]
"""

import os
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_chain_delay import window, census, representable_xy, sum_law  # noqa: E402
from explore_chain_product import least_L                                    # noqa: E402

FAILURES = []
SPAN = 6


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


class Chain:
    """A producer feeding a middle product feeding a third product."""

    def __init__(self, b, am, ap, kind, lattice=True):
        self.b = b
        Mm, Mp, w, Mh = window(b, am, ap)
        self.w, self.Mh = w, Mh
        self.kind = kind
        if kind == "product":
            self.pitch = None
            self.L1s = least_L(b, w, 2 * Mh * w)
            self.A1, self.A2 = Mh ** 2, Mh ** 3
            self.representable = representable_xy(b, am, ap)
        else:
            self.pitch = Fr(1) if lattice else Fr(0)
            self.L1s = sum_law(b, am, ap)
            self.A1, self.A2 = 2 * Mh / b, 2 * Mh ** 2 / b
            self.representable = 2 * Mh ** 2 <= b * Mp and 2 * Mh ** 3 <= b * Mp
        self.L2s = least_L(b, w, (self.A1 + Mh) * w)
        self.L3s = least_L(b, w, (self.A2 + Mh) * w)

    def S1(self, L1):
        B = Fr(self.b) ** L1
        if self.pitch is None:
            return (self.w - 1) - 2 * self.Mh * self.w / B
        return (self.w - 1) - (2 * self.w - self.pitch) / B

    def S2(self, L2, I1):
        return (self.w - 1) - (self.A1 * self.w + self.Mh * (self.w - I1)) / Fr(self.b) ** L2

    def alive3(self, L3, I2):
        return self.A2 * self.w + self.Mh * (self.w - I2) <= Fr(self.b) ** L3 * (self.w - 1)

    def naive(self):
        return self.L1s + self.L2s + self.L3s

    def g12(self):
        best = None
        for L1 in range(self.L1s, self.L1s + SPAN):
            I1 = self.S1(L1)
            if I1 < 0:
                continue
            for L2 in range(0, self.L2s + 1):
                if self.S2(L2, I1) >= 0 and (best is None or L1 + L2 < best):
                    best = L1 + L2
        return self.L1s + self.L2s - best

    def g23(self):
        best = None
        for L2 in range(0, self.L2s + SPAN):
            I2 = self.S2(L2, Fr(0))
            if I2 < 0:
                continue
            for L3 in range(0, self.L3s + 1):
                if self.alive3(L3, I2) and (best is None or L2 + L3 < best):
                    best = L2 + L3
        return self.L2s + self.L3s - best

    def chain(self, local=False):
        best = None
        for L1 in range(self.L1s, self.L1s + SPAN):
            I1 = self.S1(L1)
            if I1 < 0:
                continue
            for L2 in range(0, self.L2s + SPAN):
                left = self.S2(L2, I1)
                if left < 0:
                    continue
                I2 = max(Fr(0), self.S2(L2, Fr(0)) if local else left)
                for L3 in range(0, self.L3s + 1):
                    if self.alive3(L3, I2):
                        if best is None or L1 + L2 + L3 < best[0]:
                            best = (L1 + L2 + L3, L1, L2, L3)
                        break
        return best


def two_unit_gains(bmax, lattice):
    got = set()
    for (b, am, ap) in census(bmax):
        c = Chain(b, am, ap, "sum", lattice)
        if 2 * c.Mh ** 2 <= b * Fr(ap, b - 1) and c.g12() > 0:
            got.add((b, am, ap))
    return got


def main():
    bmax = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    t0 = time.time()

    print("=== C1 the sum-fed two-unit gains against explore_threshold_miss.py F3")
    expect = set()
    for b in range(5, bmax + 1):
        expect |= {(b, 2, b - 2), (b, b - 2, 2)}
    for lattice in (True, False):
        got = two_unit_gains(bmax, lattice)
        name = "lattice" if lattice else "dense"
        print(f"  {name} budget: {len(got)} gaining cells, "
              f"radices {min(c[0] for c in got)}..{max(c[0] for c in got)}")
        ok(got == expect, f"C1 {name} gain set differs: {sorted(got ^ expect)[:6]}")

    print("\n=== C2 the generic engine on the product chain against explore_chain_three.py")
    below, split, double = 0, 0, 0
    for (b, am, ap) in census(bmax):
        c = Chain(b, am, ap, "product")
        if not c.representable:
            continue
        con, loc = c.chain(), c.chain(local=True)
        below += con[0] < c.naive()
        split += con[0] < loc[0]
        double += con[2] < c.L2s and con[3] < c.L3s
    print(f"  below NAIVE {below}, CONTRACT < LOCAL {split}, gaining at two links {double}")
    ok((below, split, double) == (26, 0, 0) or bmax != 40,
       f"C2 the product chain reprints ({below}, {split}, {double}), not (26, 0, 0)")

    print("\n=== C3 the knife edge at (4,2,2)")
    c = Chain(4, 2, 2, "product")
    left = c.S2(1, c.S1(2))
    print(f"  S1(2) = {c.S1(2)}, middle leftover at L2 = 1: {left}")
    ok(c.S1(2) == Fr(2, 9) and left == 0, "C3 the knife edge is not exact")

    if FAILURES:
        print("\nCONTROLS RED; nothing below is read")
        sys.exit(1)

    for lattice in (True, False):
        name = "lattice" if lattice else "dense"
        print(f"\n=== the mixed chain z (x + y) u, {name} budget")
        print("  cell | L1* L2* L3* | g12 g23 | NAIVE TABLE MATCHING | CONTRACT (sum, L1, L2, L3)")
        cells, skipped = 0, 0
        kill, off_match, two_gain = [], [], []
        for (b, am, ap) in census(bmax):
            c = Chain(b, am, ap, "sum", lattice)
            if not c.representable:
                continue
            if c.S1(c.L1s) < 0:
                skipped += 1
                continue
            cells += 1
            g12, g23 = c.g12(), c.g23()
            naive = c.naive()
            table = naive - g12 - g23
            match = naive - max(g12, g23)
            con = c.chain()
            if g12 and g23:
                two_gain.append((b, am, ap))
            if con[0] != table:
                kill.append((b, am, ap))
            if con[0] != match:
                off_match.append((b, am, ap))
            if g12 or g23 or con[0] != naive:
                if b <= 8 or b in (20, 40) or con[0] not in (table, match):
                    print(f"  ({b},{am},{ap}) | {c.L1s} {c.L2s} {c.L3s} | {g12} {g23} | "
                          f"{naive} {table} {match} | {con}  rho {am + ap + 1 - b} Mh {float(c.Mh):.4f}")
        radices = sorted({k[0] for k in kill})
        print(f"  representable cells read: {cells}, skipped with a negative budget at L1*: {skipped}")
        print(f"  cells with two pairwise gains: {len(two_gain)}")
        print(f"  K2 cells with CONTRACT != TABLE: {len(kill)}"
              + (f", radices {radices[0]}..{radices[-1]} ({len(radices)} radices)" if kill else ""))
        print(f"  first: {kill[:6]}")
        print(f"  P2 cells with CONTRACT != MATCHING: {len(off_match)} {off_match[:6]}")
        ties = sum(1 for (b, am, ap) in kill
                   if (lambda c: all(c.S2(L2, c.S1(2)) >= 0 and
                                     c.alive3(3 - L2, max(Fr(0), c.S2(L2, c.S1(2))))
                                     for L2 in (1, 2)))(Chain(b, am, ap, "sum", lattice)))
        print(f"  kill cells alive at both (2, 1, 2) and (2, 2, 1): {ties} of {len(kill)}")
        print(f"  P1 the predicted set equals the kill set: "
              f"{set(kill) == {(b, 2, b - 2) for b in range(6, bmax + 1)} | {(b, b - 2, 2) for b in range(6, bmax + 1)}}")

    c = Chain(7, 2, 5, "sum")
    I1 = c.S1(2)
    print(f"\n=== the hand-attack's numbers at (7,2,5): S1(2) = {I1}, middle leftover at L2 = 1 "
          f"{c.S2(1, I1)}, third's need w (Lam3 - 1) / Mh = {c.w * (c.A2 + c.Mh - 1) / c.Mh}")
    print(f"\nwall {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
