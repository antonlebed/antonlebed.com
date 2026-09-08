"""The comparator delay: do max, min, the clamp, the rectifier and the
absolute value of signed-digit streams read at lookahead 0 at every
cell, and is a comparator FREE inside a fused unit, the fused delay the
bare unit's?

THE QUESTION. A polynomial map of D-streams (radix b, digits
D = {-am..ap}, slack rho = am + ap + 1 - b >= 1) reads at the Lebesgue
margin in its L1-Lipschitz constant wherever a term has degree two or
more, and an affine map reads at the k-sum's integer clause, one below
the margin on its wedge (explore_polynomial_delay.py). The margin law
b^c rho >= Lip1 (am + ap) never grants c = 0, yet the identity reads at
c = 0 at every cell: its wedge is every cell. max(x, y) has Lip1 = 1
like the identity, and the field's table gives it on-line delay 0
(Ercegovac and Lang, Digital Arithmetic, 2003, Table 9.1: max/min, n
in LSDF mode, 0 in MSDF mode). The question is WHY, at what scope, and
what a comparator costs once it sits inside a fused unit.

THE ROUTE (proved here on paper, the rig its check). Fix a depth n.
An input prefix of length n names the CELL [(s - M-)/b^n, (s - M-)/b^n
+ W/b^n] in window units, s the integer the digits spell, M+- =
a+-/(b-1), W = M- + M+; every cell of depth n has its lower end on the
lattice Lambda_n = (Z - M-)/b^n and the same width W/b^n, and the
output cells are the same family. Two facts:

  (1) THE CELL LEMMA. A cell C of depth n meets a cell P of depth
      n - 1 inside a child of P. The children of P are the depth-n
      cells with lower ends lo_P + j/b^n, j = 0..am+ap, the last
      ending at hi_P. If lo_C >= lo_P then j = (lo_C - lo_P) b^n is
      an integer (lo_P is on Lambda_n too: M- b^(1-n) - M- b^-n =
      am b^-n); if j <= am + ap the child at lo_C contains C, else
      C meets P inside [lo_C, hi_P], a subset of the last child. If
      lo_C < lo_P then C meets P inside [lo_P, hi_C] with hi_C <
      lo_P + W/b^n, a subset of the first child.

  (2) CELL-VALUED MAPS. Call a map of k streams cell-valued if the
      image of every depth-n box lies inside some depth-n cell. Then
      the reader at lookahead 0 survives forever: its committed
      prefix P_(n-1) contains the image at depth n - 1, which
      contains the image at depth n, which lies in a cell C_n; by (1)
      C_n meets P_(n-1) inside a child, and that child is a legal
      digit. Induction from the root cell, which is the window.

      max(x, y): the image of a box is [max lo, max hi], inside the
      input cell with the larger top (its lower end is at most the
      image's). min likewise. max and min of any number of streams,
      and compositions of them (the clamp min(max(x, y), z), the
      rectifier max(x, 0) whose image [max(lo, 0), max(hi, 0)] is
      inside x's cell when hi >= 0 and the point {0}, inside the
      committed prefix, when hi < 0): cell-valued. |x|: the image of
      a cell straddling 0 is [0, max(-lo, hi)], inside the cell or
      inside its MIRROR -C = [-hi, -lo]; the mirror is a cell iff
      -hi is on Lambda_n, i.e. iff M+ - M- is an integer, iff
      (b - 1) | (ap - am). So |x| is cell-valued exactly at those
      cells (the symmetric sets among them), and at the others the
      question is the rig's.

  (3) THE DIAGONAL. A fused unit G(w, max(y, z)) is at least as hard
      as G(w, y): the adversary plays z's digits equal to y's,
      max(y, z) = y, and the reader's information is G's own (a
      duplicated stream tells it nothing). So the fused delay is at
      least the bare unit's at every cell: max(x, y) + z at least the
      two-sum x + z (tie x = y), x max(y, z) at least the product
      x y (tie y = z). Whether the bound is met -- the
      comparator FREE inside the unit -- is not decided by (2): the
      image of the fused box sits inside G's image of (X_n, C_n), but
      C_n flips between y's cell and z's, so the pair does not refine
      the pair the reader was reading, and G's winning strategy is
      not obviously inherited.

THE ENGINE. explore_polynomial_delay.py's game, its image function
replaced by an interval evaluation of the piecewise-affine map on the
integer endpoints: the input cell of prefix u is [(b-1) u - am,
(b-1) u + ap] at scale (b-1) b^n; max, min, abs, and the rectifier
act on endpoints; a product of two intervals takes the corner
extremes at scale (b-1)^2 b^(2n); a sum adds at the common scale. The
level-t output cell is [(b-1) q - am, (b-1) q + ap] b^(o-t)/(b-1),
o the output offset (1 where the range doubles). The adversary tree
is exhaustive: a certificate at r rounds is a proof of death at that
lookahead; a survival to depth r is a survival of the search, never a
floor, and the theorems above are what make c = 0 a floor.

THE SLATE, frozen before the engine ran.

P-A THE CONTROLS. (i) The identity x at o = 0 survives the search at
    c = 0 at every cell of radices 2..5 (the k = 1 clause). (ii) x + y
    at o = 1 reproduces the lookahead criterion at every cell of
    radices 2..5: certified at L - 1, surviving at L
    (explore_lookahead_proof.py sum_law). (iii) the engine at
    max(x, y) with the adversary confined to y = x agrees with (i)
    cell for cell -- the diagonal is the identity.
P-B THE CELL-VALUED MAPS SURVIVE c = 0 [theorem (2); the print is
    the check]. max(x, y), min(x, y) at radices 2..5; max(x, y, z),
    the clamp min(max(x, y), z) at radices 2..4; the rectifier
    max(x, 0) at radices 2..5: the search survives at c = 0 at every
    cell, none certified.
P-C |x|. At every cell with (b - 1) | (ap - am) the search survives
    at c = 0 [theorem]. At the cells with (b - 1) not dividing
    (ap - am) the print decides; the intuition, marked as such and
    not derived, is that the adversary straddles 0 with the off-
    lattice mirror and certifies a death at c = 0 at some of them.
    At c = 1 the search survives at every cell (the margin law:
    b rho >= am + ap holds at every cell with rho >= 1).
P-D THE FUSED UNITS. max(x, y) + z at o = 1, radices 2..4: certified
    at the two-sum's L - 1 at every cell [theorem (3)] and -- the
    prediction, a TRANSPLANT of the cell lemma's intuition into a
    game it does not cover -- surviving at the two-sum's L at every
    cell, the comparator free. x max(y, z) at o = 0, radices 2..4:
    certified at the product's c* - 1 at every cell [theorem (3)] and
    surviving at c* at every cell, the comparator free.

KILLS, frozen as what this rig PRINTS.

K1 P-A prints a disagreement (a certificate at c = 0 on the identity,
   a cell off the sum criterion, or a diagonal cell off the identity)
   -> the engine is not the polynomial rig's; nothing below is read.
K2 Any P-B cell prints a certificate at c = 0 -> theorem (2) or the
   cell lemma is WRONG as written; the derivation is redone before
   anything below is read.
K3 An |x| cell with (b - 1) | (ap - am) prints a certificate at
   c = 0 -> the mirror clause is wrong. An |x| cell with (b - 1) not
   dividing (ap - am) printing a survival is no kill: the intuition
   was not a prediction, and the cell is recorded as it prints.
K4 A fused cell prints a certificate at the bare unit's L (or c*)
   -> the comparator is NOT free at that cell: it costs a lookahead
   inside the unit, and the transplant fails there; the cell is the
   finding, not a failure of the rig.
K5 A fused cell prints a survival at the bare unit's L - 1 (or
   c* - 1) -> impossible by theorem (3); an engine bug, nothing read.

POSITIVE CONTROL: P-A whole, before any comparator line is read.

THE SECOND FREEZE, after the first run's prints through P-C and
before P-D was read. |x| at o = 0 is representable only where
M- <= M+, i.e. a- <= a+: at the 7 cells with a- > a+ the root image
[0, M-] leaves the root cell and the reader is dead at round 0 by
the window, not the game. The first run read 14 off-mirror
certificates, those 7 among them; P-C is read over the 13
representable cells. Within the radix (1 <= a+- <= b - 1) the mirror
clause (b - 1) | (a+ - a-) forces a+ = a-, so on this census it reads:
|x| is cell-valued iff the digit set is symmetric.

THE THIRD FREEZE, after P-D's first print. The full three-stream
adversary's certificate search at x max(y, z), (4,2,3), c* - 1 = 1,
was cut by the node budget at depth 1, below the product's own
2-round certificate, and printed "survives [1]": a search cut, not a
survival, and K5 as written did not distinguish them. Theorem (3) is
made an engine move: the certificate at L* - 1 is searched with the
adversary confined to the diagonal, the comparator's two streams
tied (49 moves a round instead of 343), where the bare unit's
certificate is reachable; the survival at
L* stays against the full adversary. K5 then reads on a searched
depth at or beyond the bare unit's certificate round.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CONTROLS HOLD. The identity survives the search at c = 0 at
   20 of 20 cells of radices 2..5; x + y at o = 1 is certified at
   L* - 1 in one round at the 10 cells with L* = 2 and survives at L*
   at 20 of 20; max(x, y) against the diagonal adversary y = x agrees
   with the identity at 20 of 20. K1 never fired.

F2 THE CELL-VALUED MAPS READ AT LOOKAHEAD 0 [theorem (2); the rig
   its check]. 80 cells over five maps, 0 certified: max(x, y),
   min(x, y) and the rectifier max(x, 0) at the 20 cells of radices
   2..5 each, max(x, y, z) and the clamp min(max(x, y), z) at the 10
   cells of radices 2..4 each. K2 never fired.

F3 |x| READS AT 0 IFF THE SET IS SYMMETRIC [criterion at the 13
   representable cells: the survival half by theorem (2), the death
   half certified]. Of the 13 cells with a- <= a+, the 6 symmetric
   survive at c = 0 and the 7 asymmetric ((3,1,2), (4,1,3), (4,2,3),
   (5,1,4), (5,2,3), (5,2,4), (5,3,4)) are certified dead at c = 0,
   each in ONE round; at c = 1 all 13 survive, the margin's grant.
   The intuition held whole and sharper than written: every
   off-mirror cell dies, at once. K3 never fired.

F4 THE COMPARATOR IS FREE [theorem (4) below, found after the print;
   the rig its check at 17 cells]. max(x, y) + z at o = 1: certified
   at the two-sum's L* - 1 by the diagonal adversary at the 6 cells
   with L* = 2, one round each, and surviving at L* against the full
   adversary at 10 of 10 (radices 2..4). x max(y, z) at o = 0:
   certified at the product's c* - 1 at 7 of 7 representable cells
   (rounds 2, 1, 2, 1, 2, 2, 1 at (2,1,1), (3,1,2), (3,2,2), (4,1,3),
   (4,2,2), (4,2,3), (4,3,3)) and surviving at c* at 7 of 7. The
   survival searches reach one or two rounds only (343-ary trees);
   what makes c* a floor is the theorem, not the depth. K4 and K5
   never fired.

  (4) THE ZONE LEMMA AND THE FREE COMPARATOR (found after the run;
      the cell lemma restated). Death is a property of the image
      alone: an interval I inside the parent cell P fails every child
      iff it strictly contains an overlap zone of two consecutive
      children. Take the child with the largest lower end at or
      below I's (the first child qualifies); if it is the last child
      it contains I; otherwise I's lower end is strictly below the
      next child's, and I fails the chosen child iff I's top passes
      its top, i.e. iff I strictly contains the zone the two share.
      Hence a map G survives at lookahead L iff no box of depth n, at
      any n, has an image strictly containing a zone. The fused image
      G(W_n, max(Y_n, Z_n)) lies inside G(W_n, C_n), C_n the cell of
      Y_n, Z_n with the larger top, which is G's image of a box of
      its own inputs at the same depth: a fused death at depth n is a
      G-death at depth n, so the fused delay is at most G's, and by
      (3) at least G's. For EVERY map G of streams the delay of
      G(w, max(y, z)) equals the delay of G(w, y), and min likewise.
      A comparator on an OUTPUT, max(G(x), z), costs at most G's
      delay: its image is inside G's image or inside z's cell, and a
      cell strictly contains no zone (its lower end is a lattice
      point at or past the zone's).

VERDICT. The piecewise-affine comparators read at lookahead 0 at
every cell, because their images are cells and cells nest into
children; |x| reads at 0 iff the digit set is symmetric and at 1
otherwise; and a comparator anywhere in a datapath adds nothing to
its on-line delay -- inside a unit exactly, on an output at most. A
datapath's delay table is its arithmetic skeleton's with the
comparators deleted.

RUN RECORD: pure Python, integers only, standard library; under
memwatch, peak commit 12.0 MB against the 512 MB default; wall 113 s
at the defaults (5, 4). Reproduced by
python prime/code/explore_comparator_delay.py [BMAX_two BMAX_three]
"""

import itertools
import math
import sys
import time
from fractions import Fraction as Fr

FAILURES = []
SURVIVAL_BUDGET = 200_000
CERT_BUDGET = 2_000_000


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


# ------------------------------------------------------------ interval maps
# Each map takes the list of input intervals (integer endpoints at scale
# (b-1) b^n) and the scale, and returns (lo, hi, scale) of the image.

def iv_max(ivs, s):
    return max(l for l, _ in ivs), max(h for _, h in ivs), s


def iv_min(ivs, s):
    return min(l for l, _ in ivs), min(h for _, h in ivs), s


def iv_clamp(ivs, s):          # min(max(x, y), z)
    (l0, h0), (l1, h1), (l2, h2) = ivs
    return min(max(l0, l1), l2), min(max(h0, h1), h2), s


def iv_relu(ivs, s):           # max(x, 0)
    (l, h), = ivs
    return max(l, 0), max(h, 0), s


def iv_abs(ivs, s):
    (l, h), = ivs
    if l <= 0 <= h:
        return 0, max(-l, h), s
    return min(abs(l), abs(h)), max(abs(l), abs(h)), s


def iv_id(ivs, s):
    (l, h), = ivs
    return l, h, s


def iv_maxplus(ivs, s):        # max(x, y) + z
    (l0, h0), (l1, h1), (l2, h2) = ivs
    return max(l0, l1) + l2, max(h0, h1) + h2, s


def iv_sum2(ivs, s):           # x + y
    (l0, h0), (l1, h1) = ivs
    return l0 + l1, h0 + h1, s


def _prod(a, b):
    c = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return min(c), max(c)


def iv_xmax(ivs, s):           # x * max(y, z), scale s^2
    (l0, h0), (l1, h1), (l2, h2) = ivs
    lo, hi = _prod((l0, h0), (max(l1, l2), max(h1, h2)))
    return lo, hi, s * s


def iv_xy(ivs, s):             # x * y, scale s^2
    lo, hi = _prod(ivs[0], ivs[1])
    return lo, hi, s * s


# ------------------------------------------------------------------- game

class PieceGame:
    """The reading game at delay c and output offset o for a map given
    as an interval evaluation on the input cells. An input prefix u of
    length n is the integer interval [(b-1) u - am, (b-1) u + ap] at
    scale (b-1) b^n. `diag` confines the adversary to moves with all
    streams equal (the diagonal control)."""

    def __init__(self, b, am, ap, c, k, fmap, o=0, diag=False):
        self.b, self.am, self.ap, self.c, self.o, self.k = b, am, ap, c, o, k
        self.fmap = fmap
        self.digits = list(range(-am, ap + 1))
        if diag:
            # diag = the indices of the streams tied to one digit
            free = [i for i in range(k) if i not in diag]
            self.moves = []
            for d in self.digits:
                for rest in itertools.product(self.digits, repeat=len(free)):
                    mv = [d] * k
                    for i, x in zip(free, rest):
                        mv[i] = x
                    self.moves.append(tuple(mv))
        else:
            self.moves = list(itertools.product(self.digits, repeat=k))

    def image(self, us, n):
        b, am, ap = self.b, self.am, self.ap
        s = (b - 1) * b ** n
        ivs = [((b - 1) * u - am, (b - 1) * u + ap) for u in us]
        return self.fmap(ivs, s)

    def legal(self, us, n, q, t):
        b, am, ap = self.b, self.am, self.ap
        lo, hi, s = self.image(us, n)
        clo, chi = (b - 1) * q - am, (b - 1) * q + ap
        cs, bo = (b - 1) * b ** t, b ** self.o
        return lo * cs >= clo * bo * s and hi * cs <= chi * bo * s

    def legal_digits(self, us, n, q, t):
        return [p for p in self.digits if self.legal(us, n, self.b * q + p, t + 1)]

    def survives(self, us, q, t, rounds):
        if rounds == 0:
            return True
        n = t + self.c
        for mv in self.moves:
            us1 = tuple(self.b * u + x for u, x in zip(us, mv))
            alive = False
            for p in self.legal_digits(us1, n + 1, q, t):
                if self.survives(us1, self.b * q + p, t + 1, rounds - 1):
                    alive = True
                    break
            if not alive:
                return False
        return True

    def opening_states(self):
        states = [tuple([0] * self.k)]
        for _ in range(self.c):
            states = [tuple(self.b * u + x for u, x in zip(us, mv))
                      for us in states for mv in self.moves]
        return states

    def reader_survives(self, rounds):
        for us in self.opening_states():
            if not self.legal(us, self.c, 0, 0):
                return False
            if not self.survives(us, 0, 0, rounds):
                return False
        return True

    def certificate_depth(self, max_rounds, budget=CERT_BUDGET):
        m = len(self.moves)
        depth = max(1, min(max_rounds,
                           int(math.log(budget) / math.log(m)) - self.c))
        for r in range(0, depth + 1):
            if not self.reader_survives(r):
                return r, depth
        return None, depth


# ---------------------------------------------------------- closed forms

def sum_law(b, am, ap):
    rho = am + ap + 1 - b
    sig = -(-am // (b - 1)) - (-ap // (b - 1))
    return 1 if rho >= sig else 2


def product_law(b, am, ap):
    """The product's floor, the monomial law at d = 2:
    b^c (b-1) rho >= 2 ah (am + ap)."""
    rho, ah, W = am + ap + 1 - b, max(am, ap), am + ap
    c = 0
    while b ** c * (b - 1) * rho < 2 * ah * W:
        c += 1
    return c


def product_representable(b, am, ap):
    """x y over the window lies in the root cell at o = 0: the range is
    [-M- M+, max(M-, M+)^2] against [-M-, M+]."""
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    return -Mm * Mp >= -Mm and max(Mm, Mp) ** 2 <= Mp


def census(bmax):
    return [(b, am, ap) for b in range(2, bmax + 1)
            for am in range(0, b) for ap in range(0, b)
            if am + ap + 1 - b >= 1]


# ------------------------------------------------------------------ runs

def run_zero(name, k, fmap, bmax, T, cells=None, diag=None):
    """Every cell: the search at c = 0, o = 0. Returns
    {cell: (cert or None, depth)}."""
    out = {}
    print(f"\n=== {name}: c = 0, radices 2..{bmax}"
          + (" (diagonal adversary)" if diag else ""))
    for cell in (cells or census(bmax)):
        b, am, ap = cell
        g = PieceGame(b, am, ap, 0, k, fmap, 0, diag)
        cert, depth = g.certificate_depth(T, budget=SURVIVAL_BUDGET)
        out[cell] = (cert, depth)
        print(f"  ({b},{am},{ap}) rho={am+ap+1-b} | c = 0: "
              f"{'survives' if cert is None else 'CERTIFIED dead at round ' + str(cert)} [{depth}]")
    n = len(out)
    nc = sum(1 for v in out.values() if v[0] is not None)
    print(f"  {name}: {n} cells, {n - nc} survive the search at c = 0, {nc} certified")
    return out


def run_floor(name, k, fmap, o, law, bmax, T, rep=None, cert_diag=None):
    """Every representable cell: the certificate at law - 1 and the
    survival at law, the game at delay L - o. Returns rows
    (cell, L, cert, depth, survives_at_L, depth2)."""
    rows = []
    print(f"\n=== {name}: o = {o}, radices 2..{bmax}")
    print("  cell rho | L* | cert at L*-1 [depth] | survives at L* [depth]")
    for (b, am, ap) in census(bmax):
        if rep is not None and not rep(b, am, ap):
            print(f"  ({b},{am},{ap}) not representable at o = {o}")
            continue
        L = law(b, am, ap)
        cert, d1 = (None, 0)
        if L - 1 - o >= 0:
            cert, d1 = PieceGame(b, am, ap, L - 1 - o, k, fmap, o,
                                 diag=cert_diag).certificate_depth(T)
        surv, d2 = PieceGame(b, am, ap, L - o, k, fmap, o).certificate_depth(
            T, budget=SURVIVAL_BUDGET)
        print(f"  ({b},{am},{ap}) rho={am+ap+1-b} | L*={L} | "
              f"{'-' if L - 1 - o < 0 else (cert if cert is not None else 'survives')} [{d1}] | "
              f"{'yes' if surv is None else 'NO at round ' + str(surv)} [{d2}]")
        rows.append(((b, am, ap), L, cert, d1, surv is None, d2))
    return rows


def main():
    T = 12
    b2 = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    b3 = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    t0 = time.time()

    print("=== P-A (i): the identity at c = 0")
    ident = run_zero("x", 1, iv_id, b2, T)
    for cell, (cert, _) in ident.items():
        ok(cert is None, f"K1 identity certified dead at c = 0 at {cell}")

    print("\n=== P-A (ii): x + y at o = 1 against the lookahead criterion")
    s2 = run_floor("x + y", 2, iv_sum2, 1, sum_law, b2, T)
    for cell, L, cert, d1, surv, d2 in s2:
        if L - 2 >= 0:
            ok(cert is not None, f"K1 x + y survives L*-1 at {cell}")
        ok(surv, f"K1 x + y certified at L* at {cell}")

    print("\n=== P-A (iii): max(x, y) with the adversary on the diagonal y = x")
    dmax = run_zero("max(x, y) | y = x", 2, iv_max, b2, T, diag=(0, 1))
    for cell in ident:
        ok((dmax[cell][0] is None) == (ident[cell][0] is None),
           f"K1 diagonal max differs from the identity at {cell}")

    if FAILURES:
        print("\nPOSITIVE CONTROL FAILED; nothing below is read")
        for f in FAILURES:
            print("  ", f)
        return

    print("\n=== P-B: the cell-valued maps at c = 0")
    pb = {}
    pb["max(x, y)"] = run_zero("max(x, y)", 2, iv_max, b2, T)
    pb["min(x, y)"] = run_zero("min(x, y)", 2, iv_min, b2, T)
    pb["max(x, 0)"] = run_zero("max(x, 0)", 1, iv_relu, b2, T)
    pb["max(x, y, z)"] = run_zero("max(x, y, z)", 3, iv_max, b3, T)
    pb["min(max(x, y), z)"] = run_zero("min(max(x, y), z)", 3, iv_clamp, b3, T)
    for name, res in pb.items():
        for cell, (cert, _) in res.items():
            ok(cert is None, f"K2 {name} certified dead at c = 0 at {cell}")
    print(f"  P-B: {sum(len(r) for r in pb.values())} cells over five maps, "
          f"{sum(1 for r in pb.values() for v in r.values() if v[0] is not None)} certified")

    print("\n=== P-C: |x| at c = 0, the mirror clause (b - 1) | (ap - am)")
    rep_cells = [c for c in census(b2) if c[1] <= c[2]]
    print("  not representable at o = 0 (a- > a+): "
          + ", ".join(f"({b},{am},{ap})" for (b, am, ap) in census(b2) if am > ap))
    ab = run_zero("|x|", 1, iv_abs, b2, T, cells=rep_cells)
    sym_alive = sym_dead = asym_alive = asym_dead = 0
    for (b, am, ap), (cert, _) in ab.items():
        mirror = (ap - am) % (b - 1) == 0
        if mirror:
            ok(cert is None, f"K3 |x| certified dead at c = 0 at the mirror cell ({b},{am},{ap})")
            if cert is None:
                sym_alive += 1
            else:
                sym_dead += 1
        else:
            if cert is None:
                asym_alive += 1
            else:
                asym_dead += 1
    print(f"  |x| mirror cells: {sym_alive} survive, {sym_dead} certified; "
          f"off-mirror cells: {asym_alive} survive, {asym_dead} certified")
    print("  |x| at c = 1:")
    c1 = {}
    for (b, am, ap) in rep_cells:
        cert, depth = PieceGame(b, am, ap, 1, 1, iv_abs, 0).certificate_depth(T, budget=SURVIVAL_BUDGET)
        c1[(b, am, ap)] = cert
        ok(cert is None, f"|x| certified dead at c = 1 at ({b},{am},{ap}) against the margin law")
    print(f"  |x| at c = 1: {sum(1 for v in c1.values() if v is None)} of {len(c1)} survive")

    print("\n=== P-D: the fused units")
    print("  (the certificate at L*-1 by the DIAGONAL adversary, the comparator's two"
          " streams tied, theorem (3);"
          " the survival at L* against the full adversary)")
    mp = run_floor("max(x, y) + z", 3, iv_maxplus, 1, sum_law, b3, T, cert_diag=(0, 1))
    free_mp = sum(1 for r in mp if r[4])
    for cell, L, cert, d1, surv, d2 in mp:
        if L - 2 >= 0:
            ok(cert is not None, f"K5 max(x, y) + z survives the two-sum's L*-1 at {cell}")
        if not surv:
            print(f"  K4 max(x, y) + z certified at the two-sum's L* = {L} at {cell}: NOT free")
    print(f"  max(x, y) + z: {len(mp)} cells, the comparator free at {free_mp}, "
          f"not free at {sum(1 for r in mp if not r[4])}")

    xm = run_floor("x max(y, z)", 3, iv_xmax, 0, product_law, b3, T,
                   rep=product_representable, cert_diag=(1, 2))
    free_xm = sum(1 for r in xm if (r[1] == 0 or r[2] is not None) and r[4])
    for cell, L, cert, d1, surv, d2 in xm:
        if L - 1 >= 0:
            ok(cert is not None, f"K5 x max(y, z) survives the product's c*-1 at {cell}")
        if not surv:
            print(f"  K4 x max(y, z) certified at the product's c* = {L} at {cell}: NOT free")
    print(f"  x max(y, z): {len(xm)} cells, the comparator free at {free_xm}, "
          f"not free at {sum(1 for r in xm if not r[4])}")

    print(f"\nwall {time.time()-t0:.1f}s; failures: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)


if __name__ == "__main__":
    main()
