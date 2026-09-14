"""The piecewise-smooth dichotomy: is a reader of a map C^2 on each of
finitely many pieces dead below the margin exactly when a curved piece
is above the law's threshold, an affine lattice fires, or a shallow
straddler kills?

THE QUESTION. The many-stream theorem (explore_manystream_delay.py)
reads every C^2 map at the margin law's L* unless it is affine, its
necessity consuming the map on one ball where the Hessian is nonzero
inside the excess region; the piecewise theorem
(explore_piecewise_delay.py) reads a continuous piecewise-affine map
off a finite clause table, a lattice per piece and a cycle per kink.
This rig joins them. Conventions as there: radix b, digits {-am..ap},
slack rho = am + ap + 1 - b >= 1, M+- = a+-/(b-1), w = M- + M+; the
prefix u of length n is the box [x_u, x_u + w/b^n], x_u = (u - M-)/b^n;
a value in units of the emitted cell is the value times b^(n-L); the
reader is dead iff some box's image STRICTLY contains a zone
[q + 1 - M-, q + M+] of length w - 1 (the cell lemma), so death is a
property of the boxes alone. The law's threshold at L is
Lam_law(L) = (w - 1) b^L / w: a box whose map has |f'| <= Lam_law over
it has an image at most w - 1 wide and never kills.

THE CLAIM, derived by hand before the engine.
  (a) A NON-AFFINE piece kills at L iff sup|f'| over the piece exceeds
      Lam_law(L). Sufficiency is the width bound. Necessity is the
      many-stream argument with the piece as the window: C the
      component of {|f'| > Lam_h} holding the peak, Lam_h the midpoint
      of the sup and the threshold; f'' = 0 on C makes f' constant
      there, a boundary point of C interior to the piece reads Lam_h,
      so C is the piece and the piece is affine; otherwise a ball in C
      with f'' one-signed, and the lattice line through it kills.
      THE TRANSPLANT from the C^1 window -- "a piece affine on its
      excess region and curved below the threshold" -- is empty: the
      excess region {|f'| > Lam_law} is relatively open and f' is
      continuous, so at a boundary point interior to the piece
      f' = Lam_law, not the sup; a piece affine on its excess region is
      affine. The per-piece and per-component readings coincide and an
      affine component owes no clause of its own.
  (b) An affine piece with |s| > Lam_law kills iff its lattice clause
      fires (explore_piecewise_delay.py THE PIECE CLAUSE).
  (c) THE CONTAINMENT LEMMA, general. A straddler's hull ends are among
      f(x1), f(x2), f(kappa); an end attained on an affine side lies on
      that side's image-end lattice at depth n. At a kink whose sides
      are affine or curved-below-threshold (a curved side above the
      threshold is (a)): if both sides are below the threshold the
      width is at most w - 1; if at an extremum kink the far end is
      attained by a below-threshold side, the width is below w - 1;
      otherwise some hull end T is attained by an affine side of slope
      magnitude s > Lam_law and the image lies within s w / b^L of T
      on the side that piece's box images extend (same sign: the other
      side contributes at most Lam_law (w - delta), and
      s delta + Lam_law (w - delta) <= s w; extremum: s delta <= s w),
      so the image sits inside the image of a box of that piece with
      the same end phase, translated by an integer number of cells --
      a box that EXISTS inside the piece once the piece holds a full
      lattice period plus w + 2 at depth n (n >= n_full). Zones are
      translation-invariant, so that piece's clause fires. Hence a
      killing straddler at depth >= n_full implies a piece clause, and
      the kink clause is a finite check over the depths BELOW n_full,
      curved sides included; at an extremum kink a below-threshold
      side never attains the far end of a killing hull.
  THE THEOREM. Dead at L iff (a) or (b) or (c); the delay of a
  piecewise-C^2 map of one stream with rational affine data and
  rational kinks is the least L at which all three are empty, at most
  the margin's L*, and below it exactly when all three are empty at
  L* - 1: (a) a sup, (b) a cycle, (c) at most ceil(w) straddlers per
  kink per depth below n_full.
  THE SHALLOW GAP. explore_piecewise_delay.py's same-sign lemma
  ("a kink between same-sign slopes never fires alone") used the box
  shifted by q b^L prefixes without asking whether it is a prefix at
  that depth: at (2,1,1), L = 0, slope 1/2, depth 1, u = 0 + 2 lies
  past umax = 1. The lemma holds at depth >= n_full by (c); P-E
  searches same-sign designs for a shallow firing.

THE SPECIMENS, one stream, kink at 0, right piece x (alive at L = 0:
the identity's lattice sits on the excluded point), Lam = 1, L* = 1 at
every cell (b rho >= am + ap always, rho >= am + ap never); the pieces
are polynomials of degree <= 3, monotone on their pieces (checked
exactly), so every hull is the values at the ends and the kinks and
every sup|f'| is exact.
  S-A ABOVE: left piece 3x/4 + x^2/4, f' in [3/4 - M-/2, 3/4], the sup
      3/4 at the kink, above Lam_law(0) = 1 - 1/w <= 1/2 at every cell:
      (a) fires, DEAD at L = 0 at 20 of 20.
  S-B BELOW: left piece x/5 + x^2/20, f' in [1/5 - M-/10, 1/5], the sup
      1/5 <= Lam_law(0) at every cell (w >= 5/4). (a) empty, (b) the
      identity empty, (c) by hand: a straddler u (u - M- < 0 < u + M+)
      has image top u + M+ and bottom (u - M-)/5 + (u - M-)^2/(20 b^n)
      in cell units; the zone [q + 1 - M-, q + M+] needs q <= u - 1 and
      q + 1 - M- > bottom, so u - M- > bottom, i.e.
      (4/5)(u - M-) > (u - M-)^2/(20 b^n), false for u - M- < 0: EMPTY
      at every cell and depth. ALIVE at L = 0 at 20 of 20, the floor 0
      (at L = -1 the identity's excess exceeds 1).
  S-T THE TRANSPLANT'S TEST: x on [-m, M+], x - (x + m)^3 on [-M-, -m],
      m = M-/2 -- a C^2 map (f'' vanishes at -m), affine on its whole
      peak set, curved below with f' in [1/4, 1), non-affine on the
      piece [-M-, 0]: (a) fires, DEAD at L = 0 at 20 of 20. Hand at
      (2,1,1): the j-th box left of -m has phase j^3/4^n mod 1 against
      1 - g' = 6 j^2/4^n, so j > 6 with j^3 < 4^n kills: n = 5, j = 7.
  The two-stream specimens |x| y and max(x, y) z: (a) is the
  many-stream theorem inside a piece (x y on x >= 0, x z on x >= y,
  both non-affine at the full Lam = 2 max(M-, M+)), so both are dead at
  L* - 1 and alive at L*, the kink irrelevant.

THE SLATE, frozen before the engine.

P-A THE ORACLE. explore_piecewise_delay.py's P-B rerun through this
    rig: [x/2 | x] at 0 as degree-1 pieces at the 20 census cells of
    radices 2..5, this table's L = 0 verdict equal to that rig's hand
    table at 20 of 20 and this engine's floor equal to that rig's
    table floor (its engine's, at 20 of 20 there) at 20 of 20; and x
    alone, this engine's floor equal to the k = 1 clause's least
    empty L at 20 of 20.
P-B S-A: the table fires (a) at 20 of 20; the engine certifies a kill
    at L = 0 at 20 of 20 and survives at L* = 1.
P-C S-B: the table is empty at L = 0 at 20 of 20 and fires at L = -1;
    the engine survives at L = 0 within budget at 20 of 20 and kills at
    L = -1: floor 0 at 20 of 20, one below the margin.
P-D S-T: the table fires (a) at 20 of 20; the engine certifies a kill
    at L = 0 at 20 of 20, inside the curved piece, at (2,1,1) at input
    depth at most 5.
P-E THE CONTAINMENT LEMMA READ: over every specimen, design and cell,
    at every L the engine read, and every depth from n_full to the end
    of the lattice cycle, a straddler kills only at a depth where an
    adjacent affine piece's clause fires at that depth; and the
    same-sign search (two affine pieces of the same sign, slopes from
    explore_piecewise_delay.py's list, kink and offset on the grid of step 1/(6(b - 1)),
    the first 3000 candidates per cell) either finds a design with
    both lattices empty at L* - 1 and a straddler killing below
    n_full -- the engine then certifying at a straddling prefix and
    surviving at L* -- or prints none within budget.
P-F TWO STREAMS: |x| y and max(x, y) z through the many-stream engine
    at the 20 cells: dead at L* - 1 (the region scan or the confined
    tree) and alive at L* within budget at every cell.

KILLS, frozen as what this rig PRINTS.

K1 P-A prints a disagreement -> the engine or the table is wrong;
   nothing below is read.
K2 A certified kill at a cell and L where the table has (a), (b) and
   (c) all empty, or no kill within budget where one fires.
K3 A kill at the law's L*.
K4 The scan and the tree disagree at a depth both reach.
K5 A straddler kills at a depth >= n_full with no adjacent affine
   piece's clause firing at that depth -> the containment lemma fails.
K6 Two streams: no kill within budget at L* - 1, or a kill at L*.

POSITIVE CONTROL: P-A whole, read before any other line.

FINDINGS (entered post-run; every number below sits in this file's
printed output at radices 2..5).

F1 THE ORACLE HOLDS. This table's L = 0 verdict equals that rig's hand
   table at 20 of 20; this engine's floor equals that rig's table's at
   20 of 20; x's floor equals the k = 1 clause's at 20 of 20. P-A held;
   K1 never fired.

F2 ABOVE THE THRESHOLD, DEAD. S-A: the table fires (a) at 20 of 20, the
   engine certifies a kill at L = 0 at 20 of 20, every kill inside the
   curved piece at input depth 1 to 4, and survives at L* = 1: floor 1
   at 20 of 20. P-B held.

F3 BELOW THE THRESHOLD, ALIVE. S-B: the table is empty at L = 0 at 20
   of 20 and the engine survives there within budget at every cell;
   at L = -1 the identity's lattice fires and the engine kills at the
   root: floor 0 at 20 of 20, one below the margin's L*. A curved
   piece below the threshold beside the identity reads at the
   identity's delay. P-C held.

F4 THE TRANSPLANT'S TEST. S-T: the table fires (a) at 20 of 20 and the
   engine certifies a kill at L = 0 at 20 of 20, every kill inside the
   curved piece at input depth 1 to 3 -- at (2,1,1) at depth 3, below
   the hand bound of 5. A C^2 map affine on its whole peak set is dead
   below the margin by its curved remainder. P-D held.

F5 THE CONTAINMENT LEMMA READ. Over every specimen and design, every
   L read and every depth from n_full to the cycle's end, no straddler
   killed without an adjacent piece's clause firing at that depth: K5
   never fired. The same-sign search finds a design at 8 of 20 cells
   -- (2,1,1), (3,1,2), (3,2,1), (3,2,2), (4,1,3), (4,2,2), (4,3,1),
   (4,3,3), every one slope 1/2 on the left and 3/2, 2 or 2/3 on the
   right, all positive -- with
   both lattices empty at L* - 1 and the kink firing at input depth 0
   at three of them and depth 1 at five, the engine certifying at a
   straddling prefix at L* - 1 and surviving at L* at all 8; none
   within 3000 designs at the other 12. A same-sign kink fires alone
   at shallow depth: the earlier lemma's shifted box is not a prefix
   there. P-E held.

F6 TWO STREAMS. |x| y and max(x, y) z are dead at L* - 1 and alive at
   L* at 20 of 20 each, L* in {1, 2}, the kills at input depth 0 to 3.
   P-F held; K6 never fired.

VERDICT. A map of one stream that is C^2 on each of finitely many
pieces is dead below the margin exactly when a non-affine piece has
sup|f'| above the law's threshold, an affine piece's lattice fires, or
a straddler kills below n_full: three clauses, a sup, a cycle and a
shallow scan, agreeing with the engine at every L read over 20 + 20 +
20 + 20 + 8 cells and 0 failures; the two-stream pieces read at the
theorem verbatim.

RUN RECORD: pure Python, exact fractions for every one-stream verdict
and exact integers for the two-stream images, standard library; under
memwatch, peak commit 146 MB against the 512 MB default; wall 213 s at
radices 2..5, the same-sign search the bulk of it. Prints reproduced
by: python prime/code/explore_piecewise_smooth.py [BMAX]
"""

import itertools
import math
import sys
import time
from fractions import Fraction as Fr

import explore_manystream_delay as many
import explore_onestream_delay as one
import explore_piecewise_delay as pw
import explore_sqrt_delay as sq

FAILURES = []
SCAN_KILL, SCAN_SURV, TREE_CERT, TREE_SURV = 200_000, 120_000, 100_000, 30_000
LMIN_BELOW = 4
DESIGN_BUDGET = 3000


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


def frac(x):
    return x - math.floor(x)


# ---------------------------------------------------------- polynomials

def peval(c, x):
    v = Fr(0)
    for a in reversed(c):
        v = v * x + a
    return v


def pderiv(c):
    return [i * a for i, a in enumerate(c)][1:] or [Fr(0)]


def prange(c, x1, x2):
    """(min, max) of a polynomial of degree <= 2 over [x1, x2], exact."""
    c = list(c) + [Fr(0)] * (3 - len(c))
    assert len(c) == 3, "degree above 3"
    pts = [x1, x2]
    if c[2] != 0:
        v = -c[1] / (2 * c[2])
        if x1 < v < x2:
            pts.append(v)
    vals = [peval(c, x) for x in pts]
    return min(vals), max(vals)


# ------------------------------------------------------------- the map

class PolyPieces:
    """f = polynomial coeffs[j] (degree <= 3) on the j-th piece, the
    pieces cut by the kinks in increasing order over the window
    [-Mm, Mp]; continuity and monotonicity on each piece are checked.
    Affine pieces expose s and d for the lattice clause."""

    def __init__(self, coeffs, kinks, Mm, Mp, name):
        self.c = [[Fr(a) for a in cs] for cs in coeffs]
        self.k = [Fr(v) for v in kinks]
        self.Mm, self.Mp, self.name = Fr(Mm), Fr(Mp), name
        assert len(self.c) == len(self.k) + 1
        for j, kap in enumerate(self.k):
            assert peval(self.c[j], kap) == peval(self.c[j + 1], kap), "discontinuous"
        self.cuts = [-self.Mm] + self.k + [self.Mp]
        self.affine = [len(cs) <= 2 or all(a == 0 for a in cs[2:]) for cs in self.c]
        self.s = [cs[1] if len(cs) > 1 else Fr(0) for cs in self.c]
        self.d = [cs[0] for cs in self.c]
        self.sup = []
        for j, cs in enumerate(self.c):
            lo, hi = prange(pderiv(cs), self.cuts[j], self.cuts[j + 1])
            assert lo > 0 or hi < 0 or (lo == 0 and hi == 0) or self.affine[j], f"piece {j} not monotone"
            self.sup.append(max(abs(lo), abs(hi)))
        self.increasing = all(self.sup[j] == 0 or prange(pderiv(cs), self.cuts[j], self.cuts[j + 1])[0] >= 0
                              for j, cs in enumerate(self.c))

    def piece(self, x):
        j = 0
        while j < len(self.k) and x > self.k[j]:
            j += 1
        return j

    def f(self, x):
        return peval(self.c[self.piece(x)], x)

    def lam(self):
        return max(self.sup)

    def hull(self, x1, x2):
        vals = [self.f(x1), self.f(x2)] + [self.f(kap) for kap in self.k if x1 < kap < x2]
        return min(vals), max(vals)

    def fits(self, b, Mm, Mp, o):
        lo, hi = self.hull(-Mm, Mp)
        return -Mm * Fr(b) ** o <= lo and hi <= Mp * Fr(b) ** o

    def law_ok(self, b, rho, wsum, L):
        return Fr(b) ** L * rho >= self.lam() * wsum

    def cmp(self, C, T, X, N):
        v = Fr(C, T) - self.f(Fr(X, N))
        return (v > 0) - (v < 0)

    def approx(self, X, N):
        return float(self.f(Fr(X, N)))


def lam_law(b, am, ap, L):
    w = Fr(am + ap, b - 1)
    return (w - 1) * Fr(b) ** L / w


def two_piece(left, right, kappa, Mm, Mp, name):
    return PolyPieces([left, right], [kappa], Mm, Mp, name)


def specimen_half(Mm, Mp):
    return two_piece([0, Fr(1, 2)], [0, 1], 0, Mm, Mp, "[x/2 | x] at 0")


def specimen_above(Mm, Mp):
    return two_piece([0, Fr(3, 4), Fr(1, 4)], [0, 1], 0, Mm, Mp, "[3x/4 + x^2/4 | x] at 0")


def specimen_below(Mm, Mp):
    return two_piece([0, Fr(1, 5), Fr(1, 20)], [0, 1], 0, Mm, Mp, "[x/5 + x^2/20 | x] at 0")


def specimen_transplant(Mm, Mp):
    m = Mm / 2                                    # x - (x + m)^3 on [-Mm, -m]
    left = [-m ** 3, 1 - 3 * m ** 2, -3 * m, Fr(-1)]
    return two_piece(left, [0, 1], -m, Mm, Mp, f"[x - (x + {m})^3 | x] at {-m}")


def affine_design(sl, dl, sr, kappa, Mm, Mp):
    dr = sl * kappa + dl - sr * kappa
    return two_piece([dl, sl], [dr, sr], kappa, Mm, Mp, f"[{sl}x+{dl} | {sr}x+{dr}] at {kappa}")


# ---------------------------------------------------------- the engine

class SReader(pw.PReader):
    """explore_piecewise_delay.py's exact-hull reader with the excess
    region read off each piece's sup|f'|."""

    def region_prefixes(self, n, L):
        b, f = self.b, self.f
        umin, umax = self.prefixes(n)
        bn = Fr(b) ** n
        out = set()
        for j in range(len(f.c)):
            g = f.sup[j] * self.w / Fr(b) ** L - (self.w - 1)
            if g <= 0:
                continue
            lo = math.ceil(f.cuts[j] * bn + self.Mm)
            hi = math.floor(f.cuts[j + 1] * bn - self.Mp)
            out.update(range(max(lo, umin), min(hi, umax) + 1))
        for kap in f.k:
            lo = math.floor(kap * bn - self.Mp) + 1
            hi = math.ceil(kap * bn + self.Mm) - 1
            out.update(range(max(lo, umin), min(hi, umax) + 1))
        return sorted(out)


def engine_at(b, am, ap, fmap, o, L, kill_budget, tree_budget):
    rd = SReader(b, am, ap, L - o, fmap, o)
    tk, nk, uk, strad, _ = rd.scan_region(kill_budget, L)
    rt, depth = rd.certificate_depth(tree_budget)
    tag = f"({b},{am},{ap}) {fmap.name} L={L}"
    if tk is not None:
        if tk <= depth:
            ok(rt == tk, f"K4 {tag}: scan kills at t={tk}, tree says {rt} [depth {depth}]")
        elif rt is not None:
            ok(rt == tk, f"K4 {tag}: tree certifies at round {rt} short of the scan's t={tk}")
        return ("dead", tk, nk, uk, strad)
    ok(rt is None or max(0, rt + L - o) > nk, f"K4 {tag}: tree certifies at round {rt} inside the scan's reach n<={nk}")
    if rt is not None:
        return ("dead", rt, max(0, rt + L - o), None, None)
    return ("alive", nk, depth)


def engine_floor(b, am, ap, fmap, o, Lstar):
    verdicts = {Lstar: engine_at(b, am, ap, fmap, o, Lstar, SCAN_SURV, TREE_SURV)}
    ok(verdicts[Lstar][0] == "alive", f"K3 kill at the law's L*={Lstar} at ({b},{am},{ap}) {fmap.name}: {verdicts[Lstar]}")
    L = Lstar
    while L > Lstar - LMIN_BELOW:
        v = engine_at(b, am, ap, fmap, o, L - 1, SCAN_KILL, TREE_CERT)
        verdicts[L - 1] = v
        if v[0] == "dead":
            return L, verdicts
        L -= 1
    return None, verdicts


# ----------------------------------------------------------- the table

class TableS:
    """The three clauses at one cell: (a) per non-affine piece, a sup;
    (b) per affine piece, the lattice over the offset cycle; (c) per
    kink, the straddlers at the depths below n_full, exact hulls. The
    straddlers are also read from n_full to the cycle's end for K5."""

    def __init__(self, b, am, ap, fmap):
        self.b, self.am, self.ap, self.f = b, am, ap, fmap
        self.Mm, self.Mp = Fr(am, b - 1), Fr(ap, b - 1)
        self.w = self.Mm + self.Mp
        self.cuts = fmap.cuts

    def lattice_period(self, j, L):
        s = self.f.s[j]
        p, q = abs(s.numerator), s.denominator
        if not p:
            return 1
        if L >= 0:
            m = q * self.b ** L
            return m // math.gcd(p, m)
        return q // math.gcd(p * self.b ** (-L), q)

    def n_full(self, L):
        per = [self.lattice_period(j, L) if self.f.affine[j] else 1 for j in range(len(self.f.c))]
        n = 0
        while True:
            bn = Fr(self.b) ** n
            good = all((self.cuts[j + 1] - self.cuts[j]) * bn >= per[j] + self.w + 2 for j in range(len(self.f.c)))
            good = good and all(min(kap + self.Mm, self.Mp - kap) * bn >= self.w + 2 for kap in self.f.k)
            if good:
                return n
            n += 1

    def state(self, n, L):
        bnL = Fr(self.b) ** (n - L)
        return tuple(frac(self.f.d[j] * bnL) for j in range(len(self.f.c)) if self.f.affine[j])

    def cycle(self, L):
        nf = self.n_full(L)
        seen, n = {}, nf
        while True:
            st = self.state(n, L)
            if st in seen:
                return nf, n - 1
            seen[st] = n
            n += 1

    def prefix_range(self, n):
        return -self.am * (self.b ** n - 1) // (self.b - 1), self.ap * (self.b ** n - 1) // (self.b - 1)

    def piece_phases(self, j, n, L, full):
        s, d = self.f.s[j], self.f.d[j]
        bn, bL = Fr(self.b) ** n, Fr(self.b) ** L
        if full:
            us = range(self.lattice_period(j, L))
        else:
            umin, umax = self.prefix_range(n)
            lo = math.ceil(self.cuts[j] * bn + self.Mm)
            hi = math.floor(self.cuts[j + 1] * bn - self.Mp)
            us = range(max(lo, umin), min(hi, umax) + 1)
        end = -self.Mm if s > 0 else self.Mp
        return [frac(s * (u + end) / bL + d * bn / bL + self.Mm) for u in us]

    def piece_dead(self, j, n, L, full):
        g = abs(self.f.s[j]) * self.w / Fr(self.b) ** L - (self.w - 1)
        if g <= 0:
            return False
        if g > 1:
            return len(self.piece_phases(j, n, L, full)) > 0
        return any((z != 0) if g == 1 else (z > 1 - g) for z in self.piece_phases(j, n, L, full))

    def straddlers(self, i, n):
        kap, bn = self.f.k[i], Fr(self.b) ** n
        umin, umax = self.prefix_range(n)
        lo = math.floor(kap * bn - self.Mp) + 1
        hi = math.ceil(kap * bn + self.Mm) - 1
        return range(max(lo, umin), min(hi, umax) + 1)

    def kink_dead(self, i, n, L):
        scale = Fr(self.b) ** (n - L)
        D = (self.b - 1) * self.b ** n
        for u in self.straddlers(i, n):
            x1, x2 = Fr((self.b - 1) * u - self.am, D), Fr((self.b - 1) * u + self.ap, D)
            lo, hi = self.f.hull(x1, x2)
            if math.ceil(hi * scale - self.Mp) > lo * scale + self.Mm:
                return True
        return False

    def verdict(self, L):
        """({piece: 'a'|'b'|None dead-by}, {kink: first firing depth or
        None}, (n_full, n_end), K5 violations)."""
        nf, n_end = self.cycle(L)
        lam = lam_law(self.b, self.am, self.ap, L)
        pieces = {}
        for j in range(len(self.f.c)):
            if not self.f.affine[j]:
                pieces[j] = "a" if self.f.sup[j] > lam else None
            else:
                pieces[j] = "b" if any(self.piece_dead(j, n, L, n >= nf) for n in range(0, n_end + 1)) else None
        kinks = {i: next((n for n in range(0, nf) if self.kink_dead(i, n, L)), None) for i in range(len(self.f.k))}
        deep = []
        for i in range(len(self.f.k)):
            for n in range(nf, n_end + 1):
                if self.kink_dead(i, n, L):
                    side = [j for j in (i, i + 1)
                            if pieces[j] == "a" or (self.f.affine[j] and self.piece_dead(j, n, L, True))]
                    if not side:
                        deep.append((i, n))
        return pieces, kinks, (nf, n_end), deep

    def dead(self, L):
        p, k, _, _ = self.verdict(L)
        return any(v for v in p.values()) or any(v is not None for v in k.values())

    def floor(self, Lstar):
        L = Lstar
        while L > Lstar - LMIN_BELOW:
            if self.dead(L - 1):
                return L
            L -= 1
        return None


# ------------------------------------------------------------------ runs

def cells(bmax):
    return sq.census(bmax)


def run_map(b, am, ap, fmap, o=None):
    """One cell: L*, the table's floor, the engine's floor; K2 at every L
    the engine read; K5 over the cycle; returns the row."""
    if o is None:
        o = one.least_lead(b, am, ap, fmap)
    Ls = one.law_L(b, am, ap, fmap)
    tab = TableS(b, am, ap, fmap)
    tfloor = tab.floor(Ls)
    efloor, verdicts = engine_floor(b, am, ap, fmap, o, Ls)
    tag = f"({b},{am},{ap}) {fmap.name}"
    ok(tfloor == efloor, f"K2 {tag}: table floor {tfloor}, engine floor {efloor}")
    deep_all = []
    for L, v in verdicts.items():
        pieces, kinks, (nf, n_end), deep = tab.verdict(L)
        td = any(pieces.values()) or any(k is not None for k in kinks.values())
        ok((v[0] == "dead") == td, f"K2 {tag} at L={L}: engine {v[0]}, table {'dead' if td else 'alive'}")
        ok(not deep, f"K5 {tag} at L={L}: a straddler kills at depth {deep} (n_full {nf}) with no adjacent lattice firing")
        deep_all += deep
    kill = verdicts.get(efloor - 1) if efloor is not None else None
    row = dict(cell=(b, am, ap), o=o, Ls=Ls, tfloor=tfloor, efloor=efloor, kill=kill, deep=deep_all)
    if kill is not None and kill[0] == "dead":
        pieces, kinks, (nf, n_end), _ = tab.verdict(efloor - 1)
        row["clauses"] = (pieces, kinks)
        if kill[3] is not None:
            x1 = Fr((b - 1) * kill[3] - am, (b - 1) * b ** kill[2])
            where = "STRADDLER" if kill[4] else f"piece {fmap.piece(x1)}"
        else:
            where = "tree"
        row["where"] = where
        cl = ",".join(f"p{j}:{v or '-'}" for j, v in pieces.items()) + " " + \
             ",".join(f"k{i}:{'D@' + str(v) if v is not None else '-'}" for i, v in kinks.items())
        print(f"  ({b},{am},{ap}) o={o} L*={Ls}: floor table {tfloor} engine {efloor}; kill at L={efloor - 1}: t={kill[1]} n={kill[2]} "
              f"u={kill[3]} at {where}; clauses [{cl}]; n_full={nf} cycle to {n_end}")
    else:
        print(f"  ({b},{am},{ap}) o={o} L*={Ls}: floor table {tfloor} engine {efloor} (no kill found down to L*-{LMIN_BELOW})")
    return row


def oracle(bmax):
    print(f"\n=== P-A the oracle: [x/2 | x] and x through this rig, radices 2..{bmax}")
    n_hand = n_floor = n_id = 0
    for (b, am, ap) in cells(bmax):
        Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
        f = specimen_half(Mm, Mp)
        tab = TableS(b, am, ap, f)
        pieces, kinks, _, _ = tab.verdict(0)
        got = (pieces[0] == "b", pieces[1] == "b", kinks[0] is not None)
        hand = pw.hand_table_specimen(b, am, ap)
        ok(got == hand, f"K1 table at ({b},{am},{ap}) L=0: {got}, the hand table {hand}")
        n_hand += got == hand
        r = run_map(b, am, ap, f)
        old = pw.Table(b, am, ap, pw.specimen()).floor(r["Ls"])
        ok(r["efloor"] == old, f"K1 ({b},{am},{ap}): engine floor {r['efloor']}, the affine rig's table's {old}")
        n_floor += r["efloor"] == old
        ident = PolyPieces([[0, 1]], [], Mm, Mp, "x")
        r = run_map(b, am, ap, ident, o=0)
        clause_floor = next(L for L in range(-LMIN_BELOW, 6) if not sq.ksum_clause_dead(1, b, am, ap, L))
        ok(r["efloor"] == clause_floor, f"K1 x ({b},{am},{ap}): engine floor {r['efloor']}, the k=1 clause's {clause_floor}")
        n_id += r["efloor"] == clause_floor
    N = len(cells(bmax))
    print(f"  table = the affine rig's hand table at {n_hand} of {N}; engine floor = its table floor at {n_floor} of {N}; "
          f"x = the k = 1 clause at {n_id} of {N}")


def run_specimen(bmax, make, title, want_floor, want_clause):
    print(f"\n=== {title}, radices 2..{bmax}")
    rows = []
    for (b, am, ap) in cells(bmax):
        f = make(Fr(am, b - 1), Fr(ap, b - 1))
        r = run_map(b, am, ap, f)
        ok(r["Ls"] == 1, f"L*={r['Ls']} at ({b},{am},{ap}) {f.name}")
        ok(r["efloor"] == want_floor, f"{title} ({b},{am},{ap}): floor {r['efloor']}, predicted {want_floor}")
        if want_clause is not None and r.get("clauses"):
            ok(r["clauses"][0][0] == want_clause, f"{title} ({b},{am},{ap}): piece 0 dead by {r['clauses'][0][0]}, predicted {want_clause}")
        rows.append(r)
    n_ok = sum(1 for r in rows if r["efloor"] == want_floor)
    where = sorted(set(r.get("where", "-") for r in rows))
    ns = sorted(set(r["kill"][2] for r in rows if r.get("kill") and r["kill"][0] == "dead"))
    print(f"  floor {want_floor} at {n_ok} of {len(rows)}; kills at {where}, input depths {ns}; "
          f"K5 depths {[r['deep'] for r in rows if r['deep']] or 'none'}")
    return rows


def design_same_sign(b, am, ap):
    """The first same-sign two-piece affine map on the grid whose table
    at L* - 1 has both lattices empty and the kink killing below
    n_full, preferring one whose kink first fires past the root (the
    root box straddles every kink); (map, depth) or (None, tried)."""
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    den = 6 * (b - 1)
    kappas = [Fr(j, den) for j in range(-am * 6 + 1, ap * 6)]
    ds = [Fr(j, den) for j in range(-9, 10)]
    tried, root = 0, None
    for sl, sr in itertools.permutations(pw.SLOPES, 2):
        for sign in (1, -1):
            for kap in kappas:
                for d in ds:
                    tried += 1
                    if tried > DESIGN_BUDGET:
                        return root if root else (None, tried - 1)
                    f = affine_design(sign * sl, d, sign * sr, kap, Mm, Mp)
                    L = one.law_L(b, am, ap, f) - 1
                    tab = TableS(b, am, ap, f)
                    if tab.kink_dead(0, 0, L) and root is not None:
                        continue
                    pieces, kinks, _, _ = tab.verdict(L)
                    if any(pieces.values()) or kinks[0] is None:
                        continue
                    if kinks[0] >= 1:
                        return f, kinks[0]
                    root = (f, 0)
    return root if root else (None, tried)


def run_same_sign(bmax):
    print(f"\n=== P-E the same-sign kink alone: the first {DESIGN_BUDGET} grid designs per cell, radices 2..{bmax}")
    found = good = 0
    for (b, am, ap) in cells(bmax):
        f, info = design_same_sign(b, am, ap)
        if f is None:
            print(f"  ({b},{am},{ap}): none within {info} designs")
            continue
        found += 1
        print(f"  design {f.name}, the kink's first firing depth n={info}")
        r = run_map(b, am, ap, f)
        k = r["kill"]
        g = r["efloor"] == r["Ls"] and k is not None and k[0] == "dead" and k[4]
        ok(g, f"P-E ({b},{am},{ap}) {f.name}: floor {r['efloor']} against L*={r['Ls']}, kill {k}")
        good += g
    print(f"  same-sign designs at {found} of {len(cells(bmax))} cells; certified at a straddling prefix at L*-1 and alive at L* at {good}")


# --------------------------------------------------------- two streams

class AbsProduct:
    name, d, e = "|x| y", 2, (1, 1)

    def __init__(self, b, am, ap):
        self.b, self.am, self.ap = b, am, ap
        self.Mm, self.Mp = Fr(am, b - 1), Fr(ap, b - 1)
        self.Mh = max(self.Mm, self.Mp)

    def image(self, us, n):
        b, am, ap = self.b, self.am, self.ap
        N = (b - 1) * b ** n
        X1, X2 = (b - 1) * us[0] - am, (b - 1) * us[0] + ap
        Y1, Y2 = (b - 1) * us[1] - am, (b - 1) * us[1] + ap
        A1, A2 = (X1, X2) if X1 >= 0 else (-X2, -X1) if X2 <= 0 else (0, max(-X1, X2))
        c = (A1 * Y1, A1 * Y2, A2 * Y1, A2 * Y2)
        return min(c), max(c), N * N

    def window_range(self, Mm, Mp):
        return -self.Mh * Mm, self.Mh * Mp

    def law_ok(self, b, rho, wsum, L):
        return Fr(b) ** L * rho * (b - 1) >= 2 * max(self.am, self.ap) * wsum

    def lam(self):
        return 2 * float(self.Mh)

    def grad_iv(self, box):
        return [box[1], box[0]]


class MaxProduct:
    name, d, e = "max(x, y) z", 3, (1, 1, 1)

    def __init__(self, b, am, ap):
        self.b, self.am, self.ap = b, am, ap
        self.Mm, self.Mp = Fr(am, b - 1), Fr(ap, b - 1)
        self.Mh = max(self.Mm, self.Mp)

    def image(self, us, n):
        b, am, ap = self.b, self.am, self.ap
        N = (b - 1) * b ** n
        X1, X2 = (b - 1) * us[0] - am, (b - 1) * us[0] + ap
        Y1, Y2 = (b - 1) * us[1] - am, (b - 1) * us[1] + ap
        Z1, Z2 = (b - 1) * us[2] - am, (b - 1) * us[2] + ap
        A1, A2 = max(X1, Y1), max(X2, Y2)
        c = (A1 * Z1, A1 * Z2, A2 * Z1, A2 * Z2)
        return min(c), max(c), N * N

    def window_range(self, Mm, Mp):
        return -Mm * Mp, max(Mm, Mp) ** 2

    def law_ok(self, b, rho, wsum, L):
        return Fr(b) ** L * rho * (b - 1) >= 2 * max(self.am, self.ap) * wsum

    def lam(self):
        return 2 * float(self.Mh)

    def grad_iv(self, box):
        mx = (max(box[0][0], box[1][0]), max(box[0][1], box[1][1]))
        return [box[2], mx]


def two_stream_pair(b, am, ap, fmap):
    """Dead at L* - 1 (the region scan or the confined tree), alive at L*
    within budget; the theorem's (a) inside a piece."""
    o = many.least_lead(b, am, ap, fmap)
    L = many.law_L(b, am, ap, fmap)
    c = L - o
    W = (am + ap) / (b - 1)
    lam_law_f = (W - 1) * float(b) ** (L - 1) / W
    tag = f"({b},{am},{ap}) {fmap.name}"
    rd = many.ReaderD(b, am, ap, c - 1, fmap, o, lam_law_f)
    tk, nk, seen, rcnt = rd.scan(many.SCAN_KILL, region=True)
    rt, rdepth = rd.certificate_depth(many.TREE_CERT, confined=True)
    rd2 = many.ReaderD(b, am, ap, c, fmap, o)
    ts, ns, _, _ = rd2.scan(many.SCAN_SURV, region=False)
    rs, rdepth2 = rd2.certificate_depth(many.TREE_SURV)
    ok(ts is None and rs is None, f"K6 kill at the law's L*={L} at {tag}: scan t={ts}, tree round {rs}")
    if tk is not None and tk <= rdepth:
        ok(rt == tk, f"K4 {tag} at L*-1: scan kills at t={tk}, tree at {rt} [depth {rdepth}]")
    ok(tk is not None or rt is not None, f"K6 {tag}: no kill within budget at L*-1 (region to n={nk}, {rcnt} boxes; tree survives {rdepth})")
    print(f"  {tag}: o={o} L*={L} c*={c} | L*-1: {'kill t=%d n=%d (region %d)' % (tk, nk, rcnt) if tk is not None else 'scan clean to n=%d' % nk}, "
          f"tree {many.tree_word(rt, rdepth)} | L*: scan {'clean n<=%d' % ns if ns >= 0 else 'reached nothing'}, tree {many.tree_word(rs, rdepth2)}")
    return dict(cell=(b, am, ap), o=o, L=L, tk=tk, nk=nk, rt=rt, dead=(tk is not None or rt is not None),
                alive=(ts is None and rs is None))


def run_two_streams(bmax):
    for make in (AbsProduct, MaxProduct):
        print(f"\n=== P-F {make.name} through the many-stream engine, radices 2..{bmax}")
        rows = [two_stream_pair(b, am, ap, make(b, am, ap)) for (b, am, ap) in cells(bmax)]
        print(f"  {make.name}: dead at L*-1 at {sum(r['dead'] for r in rows)} of {len(rows)}, alive at L* at "
              f"{sum(r['alive'] for r in rows)}; L* in {sorted(set(r['L'] for r in rows))}, "
              f"kills at input depth n in {sorted(set(r['nk'] for r in rows if r['tk'] is not None))}")


def main():
    bmax = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    t0 = time.time()
    oracle(bmax)
    if FAILURES:
        print("\nPOSITIVE CONTROL FAILED; nothing below is read")
        for f in FAILURES:
            print("  ", f)
        return
    print(f"  controls: {time.time() - t0:.1f}s")
    run_specimen(bmax, specimen_above, "P-B S-A above the threshold", 1, "a")
    run_specimen(bmax, specimen_below, "P-C S-B below the threshold", 0, None)
    run_specimen(bmax, specimen_transplant, "P-D S-T the transplant's test", 1, "a")
    run_same_sign(bmax)
    run_two_streams(bmax)
    print(f"\nwall {time.time() - t0:.1f}s; failures: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)


if __name__ == "__main__":
    main()
