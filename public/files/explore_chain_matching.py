"""The matching law: is a chained on-line datapath's least delay its
units' floors less a maximum matching of its pairwise edge gains, at any
chain length, and where exactly can that fail?

THE QUESTION. explore_chain_mixed.py read three-unit chains and found
the floor NAIVE - max(g12, g23): two gains sharing a unit never both
land. Read as a law on a path of any length, a chain's least delay would
be the sum of its units' floors less a maximum matching of the path
whose edges are the pairwise gains, so gains on links sharing no unit
add. This rig asks for a proof at slack 1, for the set where the proof
does not reach, and whether that set is empty.

THE CHAIN. A head feeding n - 1 product consumers in series, every
stream on the same signed-digit window (b, am, ap), Mh = max(M-, M+),
w = M- + M+. The head is a product x y (floor least L with
b^L (w - 1) >= 2 Mh w, budget S1(L) = (w - 1) - 2 Mh w / b^L, top
A1 = Mh^2) or a sum x + y (floor the sum law, lattice budget
S1(L) = (w - 1) - (2w - 1)/b^L, top A1 = 2 Mh / b), as in
explore_chain_mixed.py. Consumer j >= 2 reads the stream of top
A(j-1) = A1 Mh^(j-2) against a fresh input:
    alive at L with inset I iff  Lam_j w - Mh I <= b^L (w - 1),
    Lam_j = Mh + A(j-1),
    leftover S_j(L, I) = (w - 1) - (Lam_j w - Mh I) / b^L,
the leftover a TRANSPLANT of the hull-overlap argument past the second
link, as in explore_chain_three.py. L*_j is the least alive L at I = 0.
D is the set of consumers below their floor, U the set of units above.

THE HAND-ATTACK, at slack 1 (am + ap = b, so w - 1 = 1/(b - 1) and
b (w - 1) = w). Lam_j never increases in j under either head.
 A (floors). L = 0 is dead at every I <= w - 1: Lam_j w - Mh I >
   Mh w - Mh (w - 1) = Mh >= b/(2(b - 1)) > w - 1 for b > 2, and at
   b = 2 Mh = w - 1 = 1 with the inequality strict. L = 1 is alive iff
   Mh I >= w (Lam_j - 1); L = 2 is alive at every I since Lam_j <= 2 <= b.
   So L*_j = 1 if Lam_j <= 1 and 2 otherwise, and a consumer in D sits
   at L = 1 with Lam_j > 1.
 B (the leftover bound). Every leftover and the head's budget is below
   w - 1. A consumer in D keeps (Mh I - w (Lam_j - 1))/b <
   (Mh (w - 1) - w (Lam_j - 1))/b. So j and j + 1 both in D force
       w (Lam_(j+1) - 1) < Mh (Mh (w - 1) - w (Lam_j - 1)) / b    (E_adj)
   and in particular Lam_(j+1) - 1 < Mh^2 / b^2 (the loose form).
 C (the crossed inset). A consumer at its floor keeps
   S_j(L*, 0) + Mh I / b^L*, so the pairwise gain of the edge (j-1, j),
   read at I = 0 into j - 1, decides j's gain at every inset outside
       Mh S_(j-1)(L*, 0) < w (Lam_j - 1) < Mh S_(j-1)(L*, w - 1),
   j >= 3                                                        (E_cross)
   a window of width Mh^2 (w - 1)/b^L*_(j-1) in the miss, O(1/b^3) since
   Lam_(j-1) >= Lam_j > 1 puts L*_(j-1) at 2.
 THE LAW. Outside E = E_adj u E_cross, CONTRACT = NAIVE - nu, nu the
 maximum matching of the path whose edge (j, j + 1) holds when the
 pairwise gain does. Below: set the downstream end of each matched edge
 to L* - 1 and every other unit to L*; a matched unit's upstream sits at
 its floor with inset >= 0, so its leftover covers the gain by
 monotonicity, and every floor unit is alive at I = 0. Above: every
 assignment costs NAIVE - |D| + (excess over U) >= NAIVE - |D| + |U|.
 Map j in D to its upstream j - 1. j - 1 is not in D (E_adj). If j - 1
 is in U, charge j to it, injectively. If j - 1 sits at its floor, the
 edge (j - 1, j) is a pairwise gain whatever inset reached j - 1 (E_cross;
 the head at its floor hands its pairwise budget exactly), and two such
 edges share no unit since D has no adjacent pair. So |D| <= nu + |U|.

 WHERE E LIVES. Lam_j - Lam_(j+1) = A(j-1)(1 - Mh). Under the product
 head at the first pair that is Mh^2 (1 - Mh), about 0.15 near the
 roots 1/phi and 0.68233, against the Mh/b the sharp form needs, so E_adj
 there is empty past radix 4. Under the sum head it is 2 Mh (1 - Mh)/b,
 O(1/b^2), and the roots 1 - 2/(b + 2k + 2) of Lam_(k+2) = 1 bunch; but
 the lattice point above the root of Lam_3 misses it by about
 (b - 6)/b^2, so the pair (2, 3) is in E only near radix 6. The
 bunching deepens along the chain: at Mh = (b - 2)/(b - 1) the
 consumers with floor 2 run to about b ln 2, and near that run's end
 consecutive misses are O(1/b^2) apart, the size of the bound. So E_adj
 should appear on long sum-fed chains at the top lattice cells.
 A WITNESS, derived before the run: (9, 2, 7), Mh = 7/8, w = 9/8, under
 the sum head. Lam_4 - 1 = 0.02387, Lam_5 - 1 = 0.00526, Lam_6 < 1. The
 sharp form reads 0.00592 < 0.00802, so the pair (4, 5) is in E_adj.
 Consumer 3 at its floor with no inset keeps 0.1105, consumer 4 at
 L = 1 then keeps 0.00776, and consumer 5 needs 0.00677 of it: both
 gain. With consumer 2 gaining off the head, the five-unit chain reads
 NAIVE - 3 = 7 against the matching's 8.

THE ARMS, per representable slack-1 cell (the sum head's cells with a
negative budget at its floor skipped, as in explore_chain_mixed.py):
  NAIVE     sum of floors.
  MATCHING  NAIVE - nu, nu the maximum-weight matching of the pairwise
            gains on the path.
  CONTRACT  the least total delay, by a dynamic programme keeping the
            largest leftover at each (cost, run of D) state, which is
            exact since every verdict is monotone in the inset; it also
            records every adjacent pair that lands together at any cost.

CONTROLS, run FIRST; nothing below is read if one is red.
 C1 at n = 3 the programme equals explore_chain_mixed.py's Chain.chain
    at every representable cell of radices 2..40, both heads, every
    slack; and the sum head reprints its 70 cells CONTRACT = NAIVE - 1
    with two pairwise gains, the product head its 26 cells below NAIVE.
 C2 lemma A at every slack-1 cell and consumer to n = 12: L* = 2 iff
    Lam > 1, else 1, and Lam nonincreasing in j.
 C3 the detector can fire: with the inset into every consumer replaced
    by w - 1, the cells where the programme lands an adjacent pair are
    exactly those with two consecutive consumers whose miss lies in
    (0, Mh/b], to n = 12 and radix 40.

PREDICTIONS, fixed before the run.
 P1 at slack 1, radices 2..40, n = 3..12, both heads: CONTRACT =
    NAIVE - nu at every cell outside E.
 P2 E_cross is empty at radices 2..40, n <= 12.
 P3 E_adj under the product head is empty at every radix read.
 P4 the sum-fed four-unit chain at (b, 2, b - 2) and its mirror reads
    NAIVE - 2 at every radix 8..40 (non-adjacent gains add) and NAIVE - 1
    at 6 and 7, where Lam_4 <= 1.
 P5 the witness: the sum-fed five-unit chain at (9, 2, 7) and its mirror
    lands the pair (4, 5) and reads 7 against MATCHING 8.
 P6 on long chains (n up to the floor-2 run plus one) the sharp E_adj
    is nonempty under the sum head at most radices from 9 to 200.

KILLS, as prints.
 K1 any control red -> nothing below is read.
 K2 THE PROOF: the count of (cell, n, pair) where the programme lands an
    adjacent pair outside the sharp E_adj; one or more kills lemma B,
    and the count outside the loose bound Mh^2/b^2 is printed beside it.
 K3 THE LAW: the count of slack-1 cells outside E with CONTRACT !=
    NAIVE - nu; one or more kills the law.
 Cells inside E where CONTRACT != NAIVE - nu scope the law and do not
 kill it.

READ AFTER THE FIRST RUN, not frozen before it: every slack-1 cell of
radices 3..24 at n = its floor-2 run plus one, the whole chain the
consumers with Lam > 1 make; and the programme at three E_cross cells.

FINDINGS (entered after the run; every number is in this file's print
at BMAX = 40, NMAX = 12, RMAX = 200).

F1 THE CONTROLS HOLD. C1: at n = 3 the programme equals
   explore_chain_mixed.py's engine at all 17305 (cell, head) pairs of
   radices 2..40, and reprints its 70 sum-fed cells at NAIVE - 1 and the
   product chain's 26 below NAIVE. C2: lemma A has 0 violations. C3:
   with the inset forced to w - 1 the detector fires at 78 cells, exactly
   the 78 predicted.
F2 THE MATCHING LAW (property at slack 1 under the closed forms, by the
   hand-attack above; every chain read agrees). K2 is 0 and K3 is 0 under
   both heads: at radices 2..40 with n = 3..12, and again at every
   slack-1 cell of radices 3..24 read along its whole floor-2 run. No
   adjacent pair lands outside the sharp E_adj, nor outside the loose
   bound Mh^2/b^2. Non-adjacent gains add: P4 held, the sum-fed
   four-unit chain at (b, 2, b - 2) reading NAIVE - 2 at every radix
   8..40 and NAIVE - 1 at 5, 6, 7. P1 and P2 held (E_cross empty there).
F3 THE EXCEPTION SET IS NOT EMPTY, AND BOTH HALVES LAND. P5 held
   exactly: at (9, 2, 7) and its mirror, Lam - 1 = 5/72, 13/288,
   55/2304, 97/18432 at consumers 2..5, the five-unit chain lands the
   pair (4, 5) with the witness (2, 1, 2, 1, 1) and reads 7 against
   MATCHING 8. That is the shortest sum-fed chain carrying a sharp E_adj
   pair to radix 200. P6 held: 174 of 198 radices 3..200 carry one under
   the sum head, at (b, 2, b - 2) near the floor-2 run's end. P3 MISSED:
   the product head carries E_adj too, on long chains only, at 96 of 198
   radices, the shortest at n = 14 (16, 3, 13) and the first radix 12 at
   n = 25; none at n <= 12 to radix 40. E_cross is realized as well:
   five cells to radix 200, all under the product head. At (31, 3, 28),
   n = 34, and (29, 2, 27), n = 74, no pairwise gain exists
   (MATCHING = NAIVE), yet the last consumer lands below its floor on an
   inset crossed from two links up, and the chain reads NAIVE - 1. At
   (24, 3, 21), n = 23, the window holds and nothing lands.
F4 INSIDE E THE MATCHING MISSES BY AT MOST ONE (pattern, radices 3..24,
   whole runs). MATCHING - CONTRACT is 0 at 8 and 1 at 12 of the 20
   sum-head cells in E, 0 at 7 and 1 at 5 of the 12 product-head cells;
   no run of three consumers ever lands below its floor. E is a scope,
   not an equivalence: at (13, 2, 11), n = 8, a pair lands and the chain
   still reads MATCHING.
F5 THE LOOSE FORM AT THE ROOTS. The loose miss under Mh^2/b^2 at consumer 2 is
   empty under both heads to radix 200; at consumer 3 it holds once
   under each, (6, 2, 4) at the sum head's root 1 - 2/(b + 4) and
   (86, 28, 58) at 0.68233, the root of M + M^3 = 1. Neither pair is in
   the sharp E_adj. The exceptions live where the tops A1 Mh^(j-2) have
   shrunk to about 1 - Mh, deep in a chain at the top lattice cells,
   and not at the named roots.

VERDICT. At slack 1 a chain's least delay is its units' floors less a
maximum matching of its pairwise gains, proved outside E_adj u E_cross,
two windows O(1/b^2) and O(1/b^3) wide in the downstream miss. Both
windows are met: where a chain runs long enough that its consumers'
misses bunch within O(1/b^2) of one another, a gaining unit's leftover
funds the next gain, or an inset crosses two links, and the chain reads
one below the matching. The exceptions scope the law and do not kill
it, and the matching's miss inside them was at most one on every chain
read.
Not walked: slack 2 and deeper, fan-in, the dense budget, a covering
check of the transplanted middle budget, and the misses inside E past
radix 24.

RUN RECORD: pure Python, exact rationals, standard library; under
memwatch, peak commit 11.6 MB, wall 47 s at (40, 12, 200). The first
full run read cells am = 0, whose digit ap = b sits outside the census,
and C2 fired on them; the generator now starts at am = 1.

Run: python prime/code/explore_chain_matching.py [BMAX] [NMAX] [RMAX]
"""

import math
import os
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_chain_delay import window, census, representable_xy, sum_law  # noqa: E402
from explore_chain_product import least_L                                    # noqa: E402
from explore_chain_mixed import Chain as Chain3                              # noqa: E402

FAILURES = []
SPAN = 4


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


class Path:
    """A head feeding consumers 2..n in series; positions are 1-based."""

    def __init__(self, b, am, ap, head, n):
        self.b, self.am, self.ap, self.head, self.n = b, am, ap, head, n
        Mm, Mp, w, Mh = window(b, am, ap)
        self.w, self.Mh, self.slack = w, Mh, am + ap + 1 - b
        if head == "product":
            self.L1s = least_L(b, w, 2 * Mh * w)
            A1 = Mh ** 2
            self.representable = representable_xy(b, am, ap)
        else:
            self.L1s = sum_law(b, am, ap)
            A1 = 2 * Mh / b
            self.representable = 2 * Mh ** 2 <= b * Mp
        self.lam = [None, None] + [Mh + A1 * Mh ** (j - 2) for j in range(2, n + 1)]
        self.Ls = [None, self.L1s] + [least_L(b, w, self.lam[j] * w) for j in range(2, n + 1)]

    def S1(self, L):
        B = Fr(self.b) ** L
        if self.head == "product":
            return (self.w - 1) - 2 * self.Mh * self.w / B
        return (self.w - 1) - (2 * self.w - 1) / B

    def S(self, j, L, I):
        return (self.w - 1) - (self.lam[j] * self.w - self.Mh * I) / Fr(self.b) ** L

    def usable(self):
        return self.representable and self.S1(self.L1s) >= 0

    def gain(self, j):
        """Pairwise gain of the edge (j, j + 1), nothing upstream of j."""
        best = None
        if j == 1:
            ups = [(L, self.S1(L)) for L in range(self.L1s, self.L1s + SPAN)]
        else:
            ups = [(L, self.S(j, L, Fr(0))) for L in range(0, self.Ls[j] + SPAN)]
        for L, I in ups:
            if I < 0:
                continue
            for L2 in range(0, self.Ls[j + 1] + 1):
                if self.S(j + 1, L2, I) >= 0 and (best is None or L + L2 < best):
                    best = L + L2
        return self.Ls[j] + self.Ls[j + 1] - best

    def programme(self, forced_inset=None):
        """Per prefix length m = 2..n: (least cost, witness); plus every
        consumer j whose pair (j - 1, j) lands together, keyed by j."""
        states = {}
        for L in range(self.L1s, self.L1s + SPAN):
            I = self.S1(L)
            if I >= 0:
                self._keep(states, (L, 0), I, (L,))
        out, adj = {}, set()
        self.triple = False
        for j in range(2, self.n + 1):
            new = {}
            for (cost, run), (I, wit) in states.items():
                Iin = I if forced_inset is None else forced_inset
                for L in range(0, self.Ls[j] + SPAN):
                    left = self.S(j, L, Iin)
                    if left < 0:
                        continue
                    down = L < self.Ls[j]
                    if down and run:
                        adj.add(j)
                    if down and run >= 2:
                        self.triple = True
                    self._keep(new, (cost + L, min(run + 1, 3) if down else 0), left, wit + (L,))
            states = new
            c = min(k[0] for k in states)
            out[j] = (c, next(v[1] for k, v in states.items() if k[0] == c))
        return out, adj

    @staticmethod
    def _keep(d, key, I, wit):
        if key not in d or I > d[key][0]:
            d[key] = (I, wit)

    def naive(self, m):
        return sum(self.Ls[1:m + 1])

    def nu(self, gains):
        """Maximum-weight matching on the path 1..m with edge weights gains."""
        take, skip = 0, 0
        for g in gains:
            take, skip = skip + g, max(take, skip)
        return max(take, skip)

    def e_adj(self, j, sharp=True):
        """Pair (j, j + 1) inside the adjacent exception set, j >= 2."""
        la, lb, w, Mh, b = self.lam[j], self.lam[j + 1], self.w, self.Mh, self.b
        if not (la > 1 and lb > 1):
            return False
        if sharp:
            return w * (lb - 1) < Mh * (Mh * (w - 1) - w * (la - 1)) / b
        return lb - 1 < Mh ** 2 / b ** 2

    def e_cross(self, j):
        """Consumer j >= 3 inside the crossed-inset window."""
        if not self.lam[j] > 1:
            return False
        miss = self.w * (self.lam[j] - 1)
        Lu = self.Ls[j - 1]
        return (self.Mh * self.S(j - 1, Lu, Fr(0)) < miss
                < self.Mh * self.S(j - 1, Lu, self.w - 1))


def slack1_cells(bmax):
    for b in range(2, bmax + 1):
        for am in range(1, b):
            yield (b, am, b - am)


def floor2_run(b, am, ap, head, cap):
    """Last consumer position with Lam > 1, by floats, capped."""
    Mh = max(am, ap) / (b - 1)
    A1 = Mh * Mh if head == "product" else 2 * Mh / b
    j = 1
    while j < cap and Mh + A1 * Mh ** (j - 1) > 1 - 1e-12:
        j += 1
    return j


def main():
    bmax = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    rmax = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    t0 = time.time()

    print("=== C1 n = 3 against explore_chain_mixed.py, every representable cell")
    diff, sum_two, prod_below, cells = 0, 0, 0, 0
    for (b, am, ap) in census(bmax):
        for head in ("sum", "product"):
            p = Path(b, am, ap, head, 3)
            if not p.usable():
                continue
            cells += 1
            c3 = Chain3(b, am, ap, head)
            ref = c3.chain()[0]
            got = p.programme()[0][3][0]
            diff += got != ref
            if head == "sum" and c3.g12() and c3.g23():
                sum_two += got == p.naive(3) - 1
            if head == "product":
                prod_below += got < p.naive(3)
    print(f"  cells {cells}, programme != Chain.chain at {diff}; sum head two-gain cells at "
          f"NAIVE - 1: {sum_two}; product head below NAIVE: {prod_below}")
    ok(diff == 0, "C1 the programme disagrees with explore_chain_mixed.py")
    ok(bmax != 40 or (sum_two, prod_below) == (70, 26), "C1 the 70 / 26 counts do not reprint")

    print("\n=== C2 lemma A at slack 1")
    badA = 0
    for (b, am, ap) in slack1_cells(bmax):
        for head in ("sum", "product"):
            p = Path(b, am, ap, head, nmax)
            if not p.usable():
                continue
            for j in range(2, nmax + 1):
                badA += p.Ls[j] != (2 if p.lam[j] > 1 else 1)
                if j > 2:
                    badA += p.lam[j] > p.lam[j - 1]
    print(f"  violations: {badA}")
    ok(badA == 0, "C2 lemma A fails")

    print("\n=== C3 the detector with every inset forced to w - 1")
    fired, predicted = set(), set()
    for (b, am, ap) in slack1_cells(bmax):
        for head in ("sum", "product"):
            p = Path(b, am, ap, head, nmax)
            if not p.usable():
                continue
            _, adj = p.programme(forced_inset=p.w - 1)
            if adj:
                fired.add((head, b, am))
            win = [0 < p.lam[j] - 1 <= p.Mh / b for j in range(2, nmax + 1)]
            if any(win[i] and win[i + 1] for i in range(len(win) - 1)):
                predicted.add((head, b, am))
    print(f"  cells fired {len(fired)}, predicted {len(predicted)}, equal {fired == predicted}")
    ok(fired and fired == predicted, "C3 the detector does not fire where it must")

    if FAILURES:
        print("\nCONTROLS RED; nothing below is read")
        sys.exit(1)

    print(f"\n=== the law at slack 1, radices 2..{bmax}, n = 3..{nmax}")
    for head in ("sum", "product"):
        k2 = k2loose = k3 = 0
        in_e, in_e_off, e_adj_n, e_cross_n, two_nu = 0, [], 0, 0, 0
        for (b, am, ap) in slack1_cells(bmax):
            p = Path(b, am, ap, head, nmax)
            if not p.usable():
                continue
            prog, adj = p.programme()
            gains = [p.gain(j) for j in range(1, nmax)]
            for m in range(3, nmax + 1):
                E = (any(p.e_adj(j) for j in range(2, m))
                     or any(p.e_cross(j) for j in range(3, m + 1)))
                e_adj_n += any(p.e_adj(j) for j in range(2, m))
                e_cross_n += any(p.e_cross(j) for j in range(3, m + 1))
                law = p.naive(m) - p.nu(gains[:m - 1])
                two_nu += p.nu(gains[:m - 1]) >= 2
                con = prog[m][0]
                if E:
                    in_e += 1
                    if con != law:
                        in_e_off.append((b, am, ap, m, con, law))
                elif con != law:
                    k3 += 1
                    print(f"  K3 ({b},{am},{ap}) n={m} CONTRACT {con} law {law} {prog[m][1]}")
                for j in adj:
                    if j <= m:
                        k2 += not p.e_adj(j - 1)
                        k2loose += not p.e_adj(j - 1, sharp=False)
        print(f"  {head} head: K2 adjacent landings outside sharp E_adj {k2} (outside the "
              f"loose bound {k2loose}); K3 {k3}")
        print(f"    (cell, n) pairs in E {in_e} [E_adj {e_adj_n}, E_cross {e_cross_n}], "
              f"off the law inside E {len(in_e_off)}: {in_e_off[:8]}")
        print(f"    (cell, n) pairs with nu >= 2: {two_nu}")

    print("\n=== P4 the sum-fed four-unit chain at (b, 2, b - 2)")
    rows = []
    for b in range(5, bmax + 1):
        for am in (2, b - 2):
            p = Path(b, am, b - am, "sum", 4)
            if p.usable():
                rows.append((b, am, p.naive(4) - p.programme()[0][4][0]))
    print("  (b, am, NAIVE - CONTRACT): " + " ".join(f"{r}" for r in rows if r[0] <= 10 or r[0] == bmax))
    ok4 = all(g == (2 if b >= 8 else 1 if b >= 6 else g) for b, am, g in rows)
    print(f"  P4 holds: {ok4}")

    print("\n=== P5 the witness (9, 2, 7), sum head, n = 5")
    for am in (2, 7):
        p = Path(9, am, 9 - am, "sum", 5)
        prog, adj = p.programme()
        gains = [p.gain(j) for j in range(1, 5)]
        print(f"  (9,{am},{9 - am}) floors {p.Ls[1:]} gains {gains} NAIVE {p.naive(5)} "
              f"MATCHING {p.naive(5) - p.nu(gains)} CONTRACT {prog[5][0]} witness {prog[5][1]} "
              f"adjacent pairs landed at {sorted((j - 1, j) for j in adj)}; "
              f"E_adj(4) {p.e_adj(4)}")
        print(f"    Lam - 1: {[str(p.lam[j] - 1) for j in range(2, 6)]}")

    print(f"\n=== P6 and the roots: the exception sets on long chains, radices 2..{rmax}")
    for head in ("sum", "product"):
        by_radix, first, loose23, loose2, cross, samples = {}, [], [], [], [], []
        shortest = None
        for b in range(3, rmax + 1):
            for am in range(1, b):
                ap = b - am
                if am > ap:
                    continue
                run = floor2_run(b, am, ap, head, 4 * b)
                n = min(run + 2, 4 * b)
                if n < 3:
                    continue
                p = Path(b, am, ap, head, n)
                if not p.usable():
                    continue
                for j in (2, 3):
                    if j <= n and p.lam[j] > 1 and p.lam[j] - 1 < p.Mh ** 2 / b ** 2:
                        (loose2 if j == 2 else loose23).append((b, am, ap))
                hits = [j for j in range(2, n) if p.e_adj(j)]
                crosses = [j for j in range(3, n + 1) if p.e_cross(j)]
                if crosses:
                    cross.append((b, am, ap, crosses))
                if hits:
                    if shortest is None or hits[0] + 1 < shortest[0]:
                        shortest = (hits[0] + 1, b, am, ap)
                    by_radix[b] = by_radix.get(b, 0) + 1
                    if len(first) < 12:
                        first.append((b, am, ap, hits))
                    if len(samples) < 6 and n <= 40:
                        samples.append((p, hits[0] + 1))
        radices = sorted(by_radix)
        print(f"  {head} head: radices with a sharp E_adj cell {len(radices)} of {rmax - 2}"
              + (f", first {radices[:10]}" if radices else ""))
        print(f"    first cells (b, am, ap, pairs (j, j+1) by j): {first}")
        print(f"    shortest chain carrying a sharp E_adj pair (n, cell): {shortest}; "
              f"shortest carrying E_cross: {min(((c[3][0], c[:3]) for c in cross), default=None)}")
        print(f"    radices 9..{rmax} missing: {[b for b in range(9, rmax + 1) if b not in by_radix][:20]}")
        print(f"    loose miss under Mh^2/b^2 at consumer 2: {loose2[:8]} ({len(loose2)}); "
              f"at consumer 3: {loose23[:8]} ({len(loose23)})")
        print(f"    E_cross cells: {len(cross)} {cross[:6]}")
        for p, m in samples:
            prog, adj = p.programme()
            gains = [p.gain(j) for j in range(1, m)]
            print(f"    programme at ({p.b},{p.am},{p.ap}) n={m}: NAIVE {p.naive(m)} MATCHING "
                  f"{p.naive(m) - p.nu(gains)} CONTRACT {prog[m][0]} landed "
                  f"{sorted((j - 1, j) for j in adj if j <= m)}")

    lmax = min(24, rmax)
    print(f"\n=== the long chains in full: every slack-1 cell of radices 3..{lmax}, "
          f"n = the floor-2 run plus one (added after the first run)")
    for head in ("sum", "product"):
        k2 = k3 = cells = inE = triples = 0
        deficit = {}
        for b in range(3, lmax + 1):
            for am in range(1, b):
                n = max(3, min(floor2_run(b, am, b - am, head, 4 * b) + 1, 4 * b))
                p = Path(b, am, b - am, head, n)
                if not p.usable():
                    continue
                cells += 1
                prog, adj = p.programme()
                triples += p.triple
                gains = [p.gain(j) for j in range(1, n)]
                law = p.naive(n) - p.nu(gains)
                E = (any(p.e_adj(j) for j in range(2, n))
                     or any(p.e_cross(j) for j in range(3, n + 1)))
                k2 += sum(1 for j in adj if not p.e_adj(j - 1))
                if E:
                    inE += 1
                    d = law - prog[n][0]
                    deficit[d] = deficit.get(d, 0) + 1
                elif prog[n][0] != law:
                    k3 += 1
                    print(f"  K3 ({b},{am},{b - am}) n={n} CONTRACT {prog[n][0]} law {law}")
        print(f"  {head} head: cells {cells}, K2 {k2}, K3 {k3}, in E {inE}, "
              f"MATCHING - CONTRACT inside E {dict(sorted(deficit.items()))}, "
              f"triple landings {triples}")

    print("\n=== the crossed-inset cells, programme against the law")
    for (b, am, ap, m) in ((24, 3, 21, 23), (31, 3, 28, 34), (29, 2, 27, 74)):
        p = Path(b, am, ap, "product", m)
        prog, adj = p.programme()
        gains = [p.gain(j) for j in range(1, m)]
        print(f"  ({b},{am},{ap}) n={m}: E_cross({m}) {p.e_cross(m)}, E_adj anywhere "
              f"{any(p.e_adj(j) for j in range(2, m))}, NAIVE {p.naive(m)} MATCHING "
              f"{p.naive(m) - p.nu(gains)} CONTRACT {prog[m][0]}, consumer {m} below its "
              f"floor in the witness: {prog[m][1][-1] < p.Ls[m]}")

    print(f"\nwall {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
