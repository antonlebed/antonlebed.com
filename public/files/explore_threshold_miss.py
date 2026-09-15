"""The threshold-miss law: is the golden window a Diophantine fact about
the product consumer's root 1/phi, or the general shape of a chain's
gain at slack 1 -- a threshold missed by less than the budget -- with
the root whatever the consumer's own box width rate makes it?

THE QUESTION. The escape law reads the chain (x y) z below the sum of
its units' floors at exactly the slack-1 cells whose hull height Mh
sits just above 1/phi -- the golden convergents from above and their
mediants, nine of the 37 radices to 40 (explore_chain_cells.py F3,
the golden window). The hypothesis under test is that the
gain is a DIOPHANTINE condition of the hull height against the
consumer's threshold root, so that a numeration is designed for
latency by choosing Mh as a convergent of that root and a mixed
datapath by simultaneous approximation of several algebraic numbers.
Its own kill: a second consumer whose threshold root is RATIONAL and
whose gains still recur. This rig runs the closed forms for the
sum-into-product chain z (x + y).

THE DERIVATION, written before the engine. A producer emitting a
D-stream at floor L1* has a slack budget S(L1) for its hull insets; a
product-type consumer reading that stream and a fresh stream z is
alive at L2 with insets (alpha, beta) iff

    A w + Mh (w - alpha - beta) <= b^L2 (w - 1),

A the producer stream's top in cell units (the product's Mh^2, the sum
stream's 2 Mh / b), so its box width rate is Lam2 = A + Mh and its
escape cost is

    E2(L2) = max(0, Lam2 w - b^L2 (w - 1)) / Mh,

THE THRESHOLD MISS of the consumer's own margin law, read in the
producer's coordinate (divided by the consumer's gradient |z| <= Mh
along that stream). At slack rho = 1, w - 1 = w/b, so the consumer's
floor is 2 exactly when Lam2 > 1 -- the THRESHOLD ROOT is the Mh
solving Lam2(Mh) = 1 -- and E2(1) = w (Lam2 - 1)/Mh. The chain gains
one lookahead, (L1*, L2* - 1) below the naive L1* + L2*, iff

    0 < Lam2 - 1 <= (Mh / w) S(L1*),        THE THRESHOLD-MISS LAW,

the miss above the root at most the budget, itself O(1/b) at slack 1.
For the product consumer, Lam2 = Mh + Mh^2, the root 1/phi, and
S(2) = (w/b)(1 - 2 Mh/b), which rearranges to explore_chain_cells.py's
alive condition. For the SUM-FED consumer the sum x + y has range
[-2 M-, 2 M+], lead 1, its stream S/b in [-2 M-/b, 2 M+/b]; the
consumer z (S/b) has range 2 Mh^2 / b inside the cell whenever
2 Mh^2 <= b M+ (the representability of the chain), lead 0; A = 2 Mh/b,
Lam2 = Mh (1 + 2/b), THE ROOT b/(b + 2), RATIONAL and moving with the
radix. The sum's floor is explore_chain_delay.py's sum_law (2 at every
slack-1 cell with a- , a+ >= 1). Its budget: the sum's images at level
n + L1 - 1 of the inputs sit on a LATTICE of pitch 1/b^L1 in cell
units, width 2w/b^L1, so a hull's tight right end is an image's right
end and the next hull must start at or before the next lattice point:
consecutive hulls overlap by at least the width less the pitch, and

    S_sum(L1) = (w - 1) - (2w - 1)/b^L1,

above the dense producer's (w - 1) - 2w/b^L1 by the pitch; both are
printed. At slack 1 with L1* = 2 the law reads, in 1/Mh,

    1 + 1/b + (b + 1)/b^3  <=  1/Mh  <  1 + 2/b        (lattice budget)
    1 + 1/b + 2/b^2        <=  1/Mh  <  1 + 2/b        (dense budget),

and the slack-1 heights are j/(b - 1): j = b - 2 gives 1/Mh = 1 +
1/(b - 2), inside both windows for every b >= 5 (1/(b - 2) - 1/b =
2/(b (b - 2)) clears (b + 1)/b^3 and 2/b^2; 1/(b - 2) < 2/b needs
b > 4), while j = b - 1 (Mh = 1) misses the lower bound and j = b - 3
has Lam2 <= 1. The cell (b, 2, b - 2) is representable (2 Mh^2 =
2 (b - 2)^2/(b - 1)^2 <= b (b - 2)/(b - 1)) and so is its mirror
(b, b - 2, 2), whose test 2 (b - 2)^2/(b - 1)^2 <= 2b/(b - 1) reads
(b - 2)^2 <= b (b - 1), true at every b. So the closed forms should
print one gaining cell and its mirror at every radix from 5, at
(2, 1), with no Diophantine structure: the least lattice point above
a rational root.

THE SLATE, frozen before the engine. Every cell with rho >= 1 of
radices 2..40, each consumer at its own representable cells; the gain
search over L1 in [L1*, L1* + 6), L2 in [0, 6).

P1 THE CONTROL. The product consumer reprints explore_chain_cells.py
   F3: gains at (4,2,2), (9,4,5), (12,5,7), (17,7,10), (22,9,13),
   (25,10,15), (30,12,18), (33,13,20), (38,15,23) and their mirrors,
   all at (2, 1), and nowhere else to radix 40.
P2 THE LAW. At every slack-1 cell of both consumers the search's gain
   verdict equals the threshold-miss law's (property; the print its
   check).
P3 THE SUM-FED CONSUMER. Under the lattice budget: a gain at (b, 2,
   b - 2) and its mirror at (2, 1) at every radix 5..40 (36 radices)
   and at no other slack-1 cell; none at radices 2..4. Under the dense
   budget the same set.
P4 (a TRANSPLANT from the product consumer): no slack-2 or deeper cell
   gains for the sum-fed consumer to radix 40.
P5 THE CERTIFIER at (5,2,3). The covering search with the sum's images
   (explore_chain_product.py's covering_exists and product_safe) at
   (L1, L2) = (2, 1) finds an assignment at every level it reaches; at
   (2, 0), law-dead by E2(0) = 17/12 against S = 3/20, it dies at
   level 1 or 2; at (1, 1), the producer below its floor, it dies at
   level 1.

KILLS, frozen as what this rig PRINTS.

K1 P1's cell set differs from the record -> the forms are miswired;
   nothing below is read.
K2 THE HYPOTHESIS'S OWN KILL: the sum-fed consumer, root rational,
   printing gains at two or more radices -> the Diophantine reading
   is dead. One radix or none -> it survives this consumer.
K3 The certifier at (5,2,3) (2, 1) printing a death -> the law's call
   at the sum-fed cells is not the chain's, and the gain there is the
   law's alone.
K4 The certifier at (5,2,3) (2, 0) alive at every level reached -> the
   consumer's death clause is misapplied to the sum-fed chain.

POSITIVE CONTROL: P1, read before any other line.

FINDINGS (entered after the run; every number below is in this file's
print at BMAX = 40, NMAX = 6).

F1 THE CONTROL HOLDS. The product consumer gains at 17 cells, the
   nine canonical cells of the record and their mirrors, all at (2, 1),
   all at slack 1. K1 never fired.
F2 THE LAW [property; the print its check]. The search's verdict
   equals the threshold-miss law's at 480 slack-1 cells of the product
   consumer and 742 of the sum-fed one.
F3 THE SUM-FED CONSUMER [rule to radix 40 by the closed forms]. 72
   gaining cells at 36 radices, every radix from 5 to 40, none below:
   (b, 2, b - 2) and its mirror at every one, all at (2, 1), all at
   slack 1, the SAME set under the lattice and the dense budget; Mh
   above the root b/(b + 2) by 0.0568 at radix 9 falling to 0.0220 at
   radix 40 -- O(1/b), as the law says, and at every radix. The
   nearest slack-1 miss where no cell gains: (2,1,1) by 7/4, (3,1,2)
   by 13/18, (4,1,3) by 7/16 (lattice budget; 2, 5/6, 1/2 dense).
   K2: gains at 36 radices with a rational root -- THE DIOPHANTINE
   READING IS KILLED. The first run of this rig fired P3 because the
   derivation's mirror clause was wrong (it tested 2 M-^2 against M+
   rather than b M+); the clause was corrected to the representable
   mirror and the expected set widened, the kill unchanged.
F4 P4 HELD: no slack-2 or deeper cell gains for the sum-fed consumer
   to radix 40.
F5 THE CERTIFIER at (5,2,3) (Mh = 3/4, above the root 5/7 by 0.0357;
   E2 = 1/12 against S = 19/100). At (2, 1) an assignment at every
   level to 4 (capped at level 5, 8.6 s); at (2, 0) dead at level 1;
   at (1, 1) dead at level 2 (P5 said 1; the producer's own death
   needs the second level to show). K3 and K4 never fired.

VERDICT. The golden window is one instance of THE THRESHOLD-MISS LAW:
at slack 1 a product-type consumer gains one lookahead over the sum of
floors exactly when its own margin threshold is missed by at most the
producer's budget, 0 < Lam2 - 1 <= (Mh/w) S(L1*), and the root is
whatever Lam2(Mh) = 1 makes it -- 1/phi for a product-fed consumer,
where the lattice j/(b - 1) lands inside the O(1/b) window at nine
radices to 40, and b/(b + 2) for a sum-fed one, where it lands at
every radix from 5. The Diophantine reading is dead; the design rule
is the least lattice point above the root, checked against the
budget. The sum-fed gain is the law's call, supported by the covering
search at (5,2,3) to level 4 and certified at no cell.

RUN RECORD: pure Python, exact rationals; under memwatch, peak commit
23.1 MB against the 512 MB default, wall 12.9 s.
Run: python prime/code/explore_threshold_miss.py [BMAX NMAX]
"""

import os
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_chain_delay import (window, margin_L, slack_budget,   # noqa: E402
                                 census, representable_xy, sum_law)
from explore_chain_product import (least_L, escape_cost_product,   # noqa: E402
                                   covering_exists, product_safe, plain_boxes,
                                   prefix_range, COVER_CAP)

FAILURES = []
PHI_INV = (5 ** 0.5 - 1) / 2
RECORD = {(4, 2, 2), (9, 4, 5), (12, 5, 7), (17, 7, 10), (22, 9, 13),
          (25, 10, 15), (30, 12, 18), (33, 13, 20), (38, 15, 23)}


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


# ------------------------------------------------------------ the consumers

class ProductFed:
    """(x y) z: the product producer, dense images."""
    name = "(x y) z"

    def __init__(self, b, am, ap):
        self.b, self.am, self.ap = b, am, ap
        Mm, Mp, w, Mh = window(b, am, ap)
        self.w, self.Mh = w, Mh
        self.lam2 = Mh + Mh * Mh
        self.root = PHI_INV
        self.L1s = margin_L(b, am, ap, 2 * Mh)
        self.representable = representable_xy(b, am, ap)

    def E2(self, L2):
        return escape_cost_product(self.b, self.am, self.ap, L2)

    def S(self, L1):
        return slack_budget(self.b, self.am, self.ap, L1)


class SumFed:
    """z (x + y): the sum producer at lead 1, lattice images."""

    def __init__(self, b, am, ap, lattice=True):
        self.b, self.am, self.ap = b, am, ap
        Mm, Mp, w, Mh = window(b, am, ap)
        self.w, self.Mh = w, Mh
        self.lam2 = Mh * (1 + Fr(2, b))
        self.root = b / (b + 2)
        self.L1s = sum_law(b, am, ap)
        self.representable = 2 * Mh * Mh <= b * Mp
        self.lattice = lattice
        self.name = "z (x + y)" + (" [lattice budget]" if lattice else " [dense budget]")

    def E2(self, L2):
        return max(Fr(0), self.lam2 * self.w - Fr(self.b) ** L2 * (self.w - 1)) / self.Mh

    def S(self, L1):
        pitch = Fr(1) if self.lattice else Fr(0)
        return (self.w - 1) - (2 * self.w - pitch) / Fr(self.b) ** L1


def gain(u, span=6):
    """(naive, best) with best = (L1 + L2, L1, L2, E2, S) the least pair
    the escape law admits; a gain is best[0] < naive."""
    L2s = least_L(u.b, u.w, u.lam2 * u.w)
    naive = u.L1s + L2s
    best = None
    for L1 in range(u.L1s, u.L1s + span):
        S = u.S(L1)
        if S < 0:
            continue
        for L2 in range(0, span):
            E = u.E2(L2)
            if E <= S and (best is None or L1 + L2 < best[0]):
                best = (L1 + L2, L1, L2, E, S)
    return naive, L2s, best


def law_gain(u):
    """The threshold-miss law at slack 1: 0 < lam2 - 1 <= (Mh/w) S(L1*)."""
    miss = u.lam2 - 1
    return 0 < miss <= (u.Mh / u.w) * u.S(u.L1s)


def sweep(bmax, make):
    gains, misses = [], {}
    checked = 0
    for (b, am, ap) in census(bmax):
        u = make(b, am, ap)
        if not u.representable:
            continue
        naive, L2s, best = gain(u)
        rho = am + ap + 1 - b
        got = best is not None and best[0] < naive
        if rho == 1:
            checked += 1
            ok(got == law_gain(u), f"P2 {u.name} ({b},{am},{ap}): search {got}, law {law_gain(u)}")
        if got:
            gains.append((b, am, ap, rho, u.Mh, float(u.Mh) - u.root, best))
        elif L2s >= 1 and rho == 1:
            e = u.E2(L2s - 1) - u.S(u.L1s)
            if b not in misses or e < misses[b][1]:
                misses[b] = ((b, am, ap), e)
    return gains, misses, checked


def sum_images(b, am, ap, m):
    """The sum's images of every (x, y) prefix pair of length m, in
    the stream's units (x + y)/b: an interval per value of the lattice
    sum, width 2w/b^(m+1)."""
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    s = Fr(1, b ** m)
    lo_u, hi_u = prefix_range(b, am, ap, m)
    return sorted(((v - 2 * Mm) * s / b, (v + 2 * Mp) * s / b)
                  for v in range(2 * lo_u, 2 * hi_u + 1))


def certify_sum_chain(b, am, ap, L1, L2, nmax):
    """No assignment of the level-(n + L1 - 1) sum images to level-n
    hulls safe against the z boxes at level n, output level n - L2."""
    for n in range(max(1, L2 + 1), nmax + 1):
        zl, zh = prefix_range(b, am, ap, n)
        if (zh - zl + 1) ** 2 > 2 * COVER_CAP:
            return ('capped', n)
        imgs = sum_images(b, am, ap, n + L1 - 1)
        safe = product_safe(b, am, ap, L2, 0, plain_boxes(b, am, ap, n), n - L2)
        if not covering_exists(b, am, ap, imgs, n, safe):
            return ('dead', n)
    return ('open', nmax)


def main():
    bmax = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    t0 = time.time()
    print(f"THE THRESHOLD-MISS LAW: radices 2..{bmax}, two consumers")

    print("\n=== P1 THE CONTROL: the product consumer's gaining cells to radix", bmax)
    g, m, n1 = sweep(bmax, ProductFed)
    cells = {(b, am, ap) for (b, am, ap, *_) in g}
    canon = {(b, min(am, ap), max(am, ap)) for (b, am, ap) in cells}
    print(f"  {len(cells)} cells (with mirrors), canonical: {sorted(canon)}")
    print(f"  pairs: {sorted({(r[6][1], r[6][2]) for r in g})}; slacks: {sorted({r[3] for r in g})}")
    ok(canon == RECORD, f"K1 the product consumer's gaining cells are {sorted(canon)}")
    if FAILURES:
        print("  CONTROL FAILED; nothing below is read.")
        return

    for lattice in (True, False):
        label = "lattice" if lattice else "dense"
        print(f"\n=== P3/P4 THE SUM-FED CONSUMER z (x + y), {label} budget: gaining cells to radix {bmax}")
        g, m, n2 = sweep(bmax, lambda b, am, ap: SumFed(b, am, ap, lattice))
        radices = sorted({r[0] for r in g})
        print(f"  {len(g)} gaining cells at {len(radices)} radices: {radices}")
        for (b, am, ap, rho, Mh, gap, best) in g:
            print(f"    ({b},{am},{ap}) rho={rho} Mh={Mh} root={b}/{b + 2} Mh-root={gap:+.4f} "
                  f"({best[1]},{best[2]}) E2={best[3]} S={best[4]}")
        print(f"  slacks among the gains: {sorted({r[3] for r in g})}; pairs: {sorted({(r[6][1], r[6][2]) for r in g})}")
        print(f"  the nearest slack-1 miss per radix (E2 - S at (L1*, L2* - 1)), radices with no gain:")
        for b in sorted(m):
            if b not in radices:
                print(f"    radix {b}: {m[b][0]} by {m[b][1]} = {float(m[b][1]):.4f}")
        if lattice:
            exp = {(b, 2, b - 2) for b in range(5, bmax + 1)} | {(b, b - 2, 2) for b in range(5, bmax + 1)}
            got = {(b, am, ap) for (b, am, ap, *_) in g}
            ok(got == exp, f"P3 the lattice-budget gain set differs from (b, 2, b - 2) and mirrors, b = 5..{bmax}: "
                           f"extra {sorted(got - exp)}, missing {sorted(exp - got)}")
            ok(all(r[3] == 1 for r in g), "P4 a slack >= 2 cell gains")
            n_rad = len(radices)
            print(f"  K2: gains at {n_rad} radices with a rational root -> "
                  + ("THE DIOPHANTINE READING IS KILLED" if n_rad >= 2 else "the reading survives this consumer"))
            ok(n_rad >= 2, "K2 fewer than two radices gain at the sum-fed consumer")
    print(f"  P2 checked at {n1} + {n2} slack-1 cells")

    print(f"\n=== P5 THE CERTIFIER at (5,2,3): the covering search with the sum's images, levels to {nmax}")
    for (L1, L2, tag) in ((2, 1, "law-alive, the gain pair"), (2, 0, "law-dead"), (1, 1, "producer below its floor")):
        u = SumFed(5, 2, 3)
        t1 = time.time()
        res = certify_sum_chain(5, 2, 3, L1, L2, nmax)
        print(f"  ({L1},{L2}) [{tag}]: E2={u.E2(L2)} S={u.S(L1)} -> {res} ({time.time() - t1:.1f}s)")
        if (L1, L2) == (2, 1):
            ok(res[0] != 'dead', f"K3 the certifier kills the law-alive pair at level {res[1]}")
        if (L1, L2) == (2, 0):
            ok(res[0] == 'dead', f"K4 the law-dead pair is {res}")

    print("\n=== VERDICT")
    print("  " + ("THE DIOPHANTINE READING IS DEAD: the gain at slack 1 is a threshold miss under the budget, "
                  "and a rational root gains at every radix from 5" if not any(f.startswith("K2") for f in FAILURES)
                  else "the reading survives the sum-fed consumer"))
    print(f"\n{len(FAILURES)} failures; wall {time.time() - t0:.1f} s")


if __name__ == "__main__":
    main()
