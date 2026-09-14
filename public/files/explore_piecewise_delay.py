"""The piecewise theorem: does a continuous piecewise-affine map of one
signed-digit stream with rational data read at exactly the least L at
which every PIECE CLAUSE and every KINK CLAUSE is empty, below the
margin law's L* exactly when every clause at L* - 1 is empty?

THE QUESTION. The many-stream theorem (explore_manystream_delay.py,
explore_onestream_widened.py) reads every C^2 map at the margin law's
L* unless it is affine, and its component argument never crosses a
kink: a continuous piecewise-affine map has zero Hessian on every
piece. Conventions as there: radix b, digits {-am..ap}, slack
rho = am + ap + 1 - b >= 1, M+- = a+-/(b-1), w = M- + M+; the prefix u
of length n is the box [x_u, x_u + w/b^n], x_u = (u - M-)/b^n; output
cells at depth t and lead o are [(q - M-) e, (q + M+) e], e = b^(o-t);
n = t + c, L = c + o, so a value in units of e is the value times
b^(n-L). The reader is dead iff some box's image STRICTLY contains a
zone [q + 1 - M-, q + M+] (the cell lemma), so death is a property of
the boxes alone and the delay is the least L at which no box kills.

THE CLAUSES, derived before the engine.
  A PIECE of slope s = p/q and offset d, a box inside it: the image's
  lower end in units of e is s(u - M-)/b^L + d b^(n-L) for s > 0 and
  s(u + M+)/b^L + d b^(n-L) for s < 0, its width |s| w/b^L, so with
  z = lower end + M- the box kills iff z mod 1 lies in the dead arc
  (1 - g, 1), g = |s| w/b^L - (w - 1) the piece's own excess (empty at
  g <= 0, the whole circle at g > 1, the circle less the point 0 at
  g = 1). Over u the phases form a lattice of step
  gcd(p, q b^L)/(q b^L) whose offset d b^(n-L) mod 1 is eventually
  periodic in n, and at large n every residue is inside the piece: the
  piece clause is a finite check over one period.
  A KINK at kappa, a box straddling it: u = floor(kappa b^n + M-) - i,
  delta = theta_n + i in (0, w), theta_n = frac(kappa b^n + M-); the
  image is the hull of f at the box's ends and at kappa; theta_n and
  f(kappa) b^(n-L) mod 1 are eventually periodic in n, so the kink
  clause is a finite check over one period.
  THE THEOREM. Sufficiency at every L with b^L rho >= Lam (am + ap),
  Lam = max|s_j|, is Lipschitz; at any L the reader is dead iff a piece
  clause or a kink clause is non-empty; so the delay is the least L at
  which every clause is empty, at most L*, and below L* exactly when
  every clause at L* - 1 is empty. A discontinuous map is dead at
  every L (a box round the jump has an image of width at least the
  jump at every depth).
  THE CONTAINMENT LEMMA. For same-sign slopes s_r >= s_l > 0 the
  straddler's top is on the right piece's top lattice (right tops are
  top_s + s_r m/b^L, and m = q b^L lands on it mod 1) and that right
  box has bottom top_s - s_r w <= bottom_s, so it contains the
  straddler: a kink between same-sign slopes never fires alone (at a
  depth where that right box is a prefix; at shallower depths it does,
  explore_piecewise_smooth.py F5); the
  mirror for s_l >= s_r. A kink fires alone only when one end of the
  hull is f(kappa) itself (an extremum kink), the far side is the
  wider one and delta avoids the finite set where s_far (m - delta)/b^L
  is an integer. A slope of magnitude 1 with an alive lattice keeps its
  box ends on the cell lattice, so an image top never strictly exceeds
  a zone top: the firing side of P-C's design has |s| != 1.

THE SPECIMEN'S TABLE at L = 0, written from the derivation before the
engine runs: f = x/2 on x <= 0, x on x >= 0, kink 0, Lam = 1, so
L* = 1 at every cell (b rho >= am + ap always, rho >= am + ap never).
  the slope-1 piece: g = 1, arc (0, 1), z = u = 0: ALIVE at every cell;
  the slope-1/2 piece: g = 1 - w/2, empty at w >= 2, arc (w/2, 1),
    phases {M-/2, M-/2 + 1/2}: the first is never in the arc, the
    second iff M- + 1 > w and M- < 1, i.e. am < b - 1 and ap < b - 1:
    DEAD at exactly (4,2,2), (5,2,3), (5,3,2), (5,3,3);
  the kink: u = 0 alone (M-, M+ <= 1), image [-M-/2, M+] in e-units,
    the zones [1 - M-, M+] and [-M-, M+ - 1] never strictly inside:
    EMPTY at every cell, period 1.
  VERDICT: floor 0 at 16 cells, 1 at the four. Checked by hand at
  (5,2,3), u = -1, n = 1: box [-0.3, -0.05], image [-0.15, -0.025],
  zone [-0.1, -0.05] strictly inside; at (3,1,2), u = -1, n = 1: image
  [-1/4, 0] against the zone [-1/6, 0], the top ties, alive.

THE SLATE, frozen before the engine.

P-A THE ORACLE. The one-piece maps x and x/2 through the general
    engine at lead 0 at the 20 census cells of radices 2..5: x's
    certified floor equals the least L at which the k = 1 clause of
    the affine remainder is empty at 20 of 20; x/2's equals the
    rational-slope criterion's c_min (explore_slope_proof.py, which
    reads symmetric sets at lookaheads c >= 0, so the engine's floor
    is clipped at 0) at the 6 symmetric cells, the scan and the
    tree agreeing at all 20; the table's floor equals the engine's at
    all 40 pairs.
P-B THE SPECIMEN. Slopes 1/2 and 1 at kappa = 0 over the 20 cells:
    L* = 1 at every cell; the table reproduces the hand table above
    at 20 of 20 (the four dead cells, the kink empty everywhere); the
    engine's certified floor equals the table's at 20 of 20, every
    kill inside the slope-1/2 piece.
P-C THE KINK ALONE. At each cell, a two-piece map found by a search
    over the table (V or Lam shapes, slopes of magnitude 1/2, 1/3,
    2/3, 3/2, 2, 1/4, 3/4, 3, kappa and d on a grid of step
    1/(6(b - 1))) with both piece clauses empty and the kink clause
    firing at L* - 1, preferring a design whose kink first fires at a
    depth past the root (the root box straddles every kink, so a root
    kill is the degenerate case; the rehearsal at radices 2..4 found
    root kills first and depth-1 kills on a wider grid): the engine's
    certified kill at that L is at a straddling prefix at the table's
    first firing depth, and the reader survives at L*; cells where the
    search finds no design are printed as such.
P-D THE PERIOD. Every kill in P-B and P-C at an input depth n at most
    n_full + the cycle's length, n_full the depth from which every
    piece holds a full lattice period and every straddler is a prefix.

KILLS, frozen as what this rig PRINTS.

K1 P-A prints a disagreement with the affine remainder, the criterion
   or the tree -> the engine or the clause is wrong; nothing below is
   read.
K2 A certified kill at a cell and L where the table says every clause
   is empty, or no kill within budget at a cell and L where the table
   says a clause fires -> the theorem fails there; the table is
   re-derived by hand at that cell before any verdict.
K3 A kill at the law's L* -> the Lipschitz sufficiency is wrong.
K4 The scan and the tree disagree at a depth both reach.
K5 A kill past n_full + the cycle -> the period argument is wrong.

POSITIVE CONTROL: P-A whole, read before any other line.

FINDINGS (entered post-run; every number below sits in this file's
printed output at radices 2..5).

F1 THE ORACLE HOLDS. x's engine floor equals the k = 1 clause's at 20
   of 20 cells; x/2's equals the criterion's c_min at 6 of 6 symmetric
   cells (at (2,1,1) the engine reads x/2 alive at L = -1, a shift
   emitting before it reads, which the criterion's c >= 0 cannot see)
   and the table's at 20 of 20. P-A held; K1 never fired.

F2 THE SPECIMEN READS OFF THE TABLE. [x/2 | x] at 0: L* = 1 at every
   cell; the table equals the hand table at 20 of 20 (the slope-1/2
   piece dead at exactly (4,2,2), (5,2,3), (5,3,2), (5,3,3), the kink
   empty everywhere) and the engine's floor equals the table's at 20
   of 20: floor 1 at the four cells, every kill inside the slope-1/2
   piece at input depth 1 (u = -1 or -3), and floor 0 at the other 16,
   one below the margin law, the kill at L = -1 sitting at the root.
   P-B held.

F3 THE KINK FIRES ALONE. Designs on the grid at 10 of 20 cells, all
   ten cells of radices 2..4 and none of the ten of radix 5 (the grid
   exhausted there): every design is a V, a slope of -1/2 or -2 on
   the left and 1/2, 3/2, 2, 2/3 or 3 on the right, its lead 1, and
   at every one the engine's certified kill at L* - 1 is at a
   straddling prefix with both piece clauses empty and the reader
   alive at L*; 9 of the 10 fire first at input depth 1 (the
   straddler u = -1..3 beside the kink) and (4,3,3) at the root.
   P-C held.

F4 THE PERIOD. Every kill of P-B and P-C sits at input depth 0 or 1,
   inside the offset cycle at every cell (n_full 2..4, the state
   repeating by depth 6). K5 never fired; P-D held.

VERDICT. A continuous piecewise-affine map of one stream with rational
data reads at the least L at which every piece clause and every kink
clause is empty: below the margin's L* exactly when every clause at
L* - 1 is empty (the specimen at 16 of 20 cells), the kink clause a
third source of death that fires with both pieces alive (10 cells,
every design a valley). The engine and the
table agree at every L read, 20 + 20 + 20 + 10 cells and 0 failures.

RUN RECORD: pure Python, exact fractions for every verdict, standard
library; under memwatch, peak commit 113 MB against the 512 MB
default; wall 338 s at radices 2..5, the design search's exhausted grid
at radix 5 the bulk of it. Prints reproduced by:
python prime/code/explore_piecewise_delay.py [BMAX]
"""

import itertools
import math
import sys
import time
from fractions import Fraction as Fr

import explore_onestream_delay as one
import explore_slope_proof as slope
import explore_sqrt_delay as sq

FAILURES = []
SCAN_KILL, SCAN_SURV, TREE_CERT, TREE_SURV = 200_000, 120_000, 100_000, 30_000
LMIN_BELOW = 4                     # how far below L* the floor search goes


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


def frac(x):
    return x - math.floor(x)


# ------------------------------------------------------------ the map

class Piecewise:
    """f(x) = slopes[j] x + offsets[j] on the j-th piece, the pieces cut
    by the kinks in increasing order; continuity is checked."""

    def __init__(self, slopes, offsets, kinks, name):
        self.s = [Fr(v) for v in slopes]
        self.d = [Fr(v) for v in offsets]
        self.k = [Fr(v) for v in kinks]
        self.name = name
        assert len(self.s) == len(self.d) == len(self.k) + 1
        for j, kap in enumerate(self.k):
            assert self.s[j] * kap + self.d[j] == self.s[j + 1] * kap + self.d[j + 1], "discontinuous"
        self.increasing = all(v > 0 for v in self.s)

    def piece(self, x):
        j = 0
        while j < len(self.k) and x > self.k[j]:
            j += 1
        return j

    def f(self, x):
        j = self.piece(x)
        return self.s[j] * x + self.d[j]

    def lam(self):
        return max(abs(v) for v in self.s)

    def hull(self, x1, x2):
        vals = [self.f(x1), self.f(x2)] + [self.f(kap) for kap in self.k if x1 < kap < x2]
        return min(vals), max(vals)

    def fits(self, b, Mm, Mp, o):
        lo, hi = self.hull(-Mm, Mp)
        return -Mm * Fr(b) ** o <= lo and hi <= Mp * Fr(b) ** o

    def law_ok(self, b, rho, wsum, L):
        return Fr(b) ** L * rho >= self.lam() * wsum

    def cmp(self, C, T, X, N):                 # unused by PReader; the base API
        v = Fr(C, T) - self.f(Fr(X, N))
        return (v > 0) - (v < 0)

    def approx(self, X, N):
        return float(self.f(Fr(X, N)))


def affine(s, d=0, name=None):
    return Piecewise([s], [d], [], name or f"{s}x" + (f"+{d}" if d else ""))


def two_piece(s_left, s_right, kappa, d_left, name=None):
    """Continuous: the right offset is forced by the kink."""
    kappa, d_left = Fr(kappa), Fr(d_left)
    d_right = Fr(s_left) * kappa + d_left - Fr(s_right) * kappa
    return Piecewise([s_left, s_right], [d_left, d_right], [kappa],
                     name or f"[{s_left}x+{d_left} | {s_right}x+{d_right}] at {kappa}")


# ---------------------------------------------------------- the engine

class PReader(one.Reader):
    """The one-stream reader with exact images: the hull of the map
    over the box, kinks included."""

    def __init__(self, b, am, ap, c, fmap, o):
        super().__init__(b, am, ap, c, fmap, o)
        self.Mm, self.Mp = Fr(am, b - 1), Fr(ap, b - 1)
        self.w = self.Mm + self.Mp

    def box(self, u, n):
        D = (self.b - 1) * self.b ** n
        return Fr((self.b - 1) * u - self.am, D), Fr((self.b - 1) * u + self.ap, D)

    def image(self, u, n):
        return self.f.hull(*self.box(u, n))

    def legal(self, u, n, q, t):
        C1, C2, T = self.cell(q, t)
        lo, hi = self.image(u, n)
        return Fr(C1, T) <= lo and hi <= Fr(C2, T)

    def straddles(self, u, n, t):
        lo, hi = self.image(u, n)
        scale = Fr(self.b) ** (t - self.o)          # 1/e
        return math.ceil(hi * scale - self.Mp) > lo * scale + self.Mm

    def is_straddler(self, u, n):
        x1, x2 = self.box(u, n)
        return any(x1 < kap < x2 for kap in self.f.k)

    def region_prefixes(self, n, L):
        """Every prefix of length n whose box lies inside a piece with
        positive excess at L, plus every straddler; sorted."""
        b, f = self.b, self.f
        umin, umax = self.prefixes(n)
        bn = Fr(b) ** n
        cuts = [-self.Mm] + f.k + [self.Mp]
        out = set()
        for j, s in enumerate(f.s):
            g = abs(s) * self.w / Fr(b) ** L - (self.w - 1)
            if g <= 0:
                continue
            lo = math.ceil(cuts[j] * bn + self.Mm)
            hi = math.floor(cuts[j + 1] * bn - self.Mp)
            out.update(range(max(lo, umin), min(hi, umax) + 1))
        for kap in f.k:
            lo = math.floor(kap * bn - self.Mp) + 1
            hi = math.ceil(kap * bn + self.Mm) - 1
            out.update(range(max(lo, umin), min(hi, umax) + 1))
        return sorted(out)

    def scan_region(self, budget, L):
        """(t, n, u, straddler?) at the least output depth with a kill,
        or (None, last n, None, None); plus prefixes seen."""
        t, seen, last_n = 0, 0, -1
        while True:
            t += 1
            n = max(0, t + self.c)
            us = self.region_prefixes(n, L)
            if (not us and n >= 1) or t > 80:      # an empty region stays empty
                return None, last_n, None, None, seen
            if seen + len(us) > budget:
                return None, last_n, None, None, seen
            for u in us:
                if self.straddles(u, n, t):
                    return t, n, u, self.is_straddler(u, n), seen
            seen += len(us)
            last_n = n


def engine_at(b, am, ap, fmap, o, L, kill_budget, surv_budget, tree_budget):
    """The engine's verdict at one L: ('dead', t, n, u, straddler?) or
    ('alive', n reached, tree depth); K4 checked."""
    rd = PReader(b, am, ap, L - o, fmap, o)
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
    """The least L alive by the engine, searching down from L*; returns
    (floor, the verdict at each L)."""
    verdicts = {}
    v = engine_at(b, am, ap, fmap, o, Lstar, SCAN_KILL, SCAN_SURV, TREE_SURV)
    verdicts[Lstar] = v
    ok(v[0] == "alive", f"K3 kill at the law's L*={Lstar} at ({b},{am},{ap}) {fmap.name}: {v}")
    L = Lstar
    while L > Lstar - LMIN_BELOW:
        v = engine_at(b, am, ap, fmap, o, L - 1, SCAN_KILL, SCAN_SURV, TREE_CERT)
        verdicts[L - 1] = v
        if v[0] == "dead":
            return L, verdicts
        L -= 1
    return None, verdicts


# ----------------------------------------------------------- the table

class Table:
    """The clauses of a piecewise map at one cell: per L, the verdict of
    every piece and every kink over the offset cycle."""

    def __init__(self, b, am, ap, fmap):
        self.b, self.am, self.ap, self.f = b, am, ap, fmap
        self.Mm, self.Mp = Fr(am, b - 1), Fr(ap, b - 1)
        self.w = self.Mm + self.Mp
        self.cuts = [-self.Mm] + fmap.k + [self.Mp]

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
        """The depth from which every piece holds a full lattice period
        and every straddler of every kink is a prefix."""
        P = max(self.lattice_period(j, L) for j in range(len(self.f.s)))
        n = 0
        while True:
            bn = Fr(self.b) ** n
            good = all((self.cuts[j + 1] - self.cuts[j]) * bn >= P + self.w + 2 for j in range(len(self.f.s)))
            good = good and all(min(kap + self.Mm, self.Mp - kap) * bn >= self.w + 2 for kap in self.f.k)
            if good:
                return n
            n += 1

    def state(self, n, L):
        f, bnL = self.f, Fr(self.b) ** (n - L)
        return (tuple(frac(d * bnL) for d in f.d)
                + tuple(frac(kap * Fr(self.b) ** n + self.Mm) for kap in f.k)
                + tuple(frac(f.f(kap) * bnL) for kap in f.k))

    def cycle(self, L):
        """The depths 0..n_end whose states cover every state: n_full,
        then on until a state repeats."""
        nf = self.n_full(L)
        seen, n = {}, nf
        while True:
            st = self.state(n, L)
            if st in seen:
                return nf, n - 1, seen[st]
            seen[st] = n
            n += 1

    def piece_phases(self, j, n, L, full):
        """The lower-end phases of the boxes inside piece j at depth n:
        the actual prefixes below n_full, one full lattice period above."""
        s, d = self.f.s[j], self.f.d[j]
        bn, bL = Fr(self.b) ** n, Fr(self.b) ** L
        if full:
            us = range(self.lattice_period(j, L))
        else:
            umin, umax = -self.am * (self.b ** n - 1) // (self.b - 1), self.ap * (self.b ** n - 1) // (self.b - 1)
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
        umin, umax = -self.am * (self.b ** n - 1) // (self.b - 1), self.ap * (self.b ** n - 1) // (self.b - 1)
        lo = math.floor(kap * bn - self.Mp) + 1
        hi = math.ceil(kap * bn + self.Mm) - 1
        return range(max(lo, umin), min(hi, umax) + 1)

    def kink_dead(self, i, n, L):
        bn, scale = Fr(self.b) ** n, Fr(self.b) ** (n - L)
        D = (self.b - 1) * self.b ** n
        for u in self.straddlers(i, n):
            x1, x2 = Fr((self.b - 1) * u - self.am, D), Fr((self.b - 1) * u + self.ap, D)
            lo, hi = self.f.hull(x1, x2)
            if math.ceil(hi * scale - self.Mp) > lo * scale + self.Mm:
                return True
        return False

    def verdict(self, L):
        """({piece j: dead?}, {kink i: dead?}, (n_full, n_end, n_back))."""
        nf, n_end, back = self.cycle(L)
        pieces = {j: any(self.piece_dead(j, n, L, n >= nf) for n in range(0, n_end + 1))
                  for j in range(len(self.f.s))}
        kinks = {i: any(self.kink_dead(i, n, L) for n in range(0, n_end + 1))
                 for i in range(len(self.f.k))}
        return pieces, kinks, (nf, n_end, back)

    def dead(self, L):
        p, k, _ = self.verdict(L)
        return any(p.values()) or any(k.values())

    def floor(self, Lstar):
        L = Lstar
        while L > Lstar - LMIN_BELOW:
            if self.dead(L - 1):
                return L
            L -= 1
        return None


def hand_table_specimen(b, am, ap):
    """The specimen's L = 0 verdict from the derivation in the docstring:
    (slope-1/2 piece dead?, slope-1 piece dead?, kink dead?)."""
    w = Fr(am + ap, b - 1)
    return (w < 2 and am < b - 1 and ap < b - 1, False, False)


def specimen():
    return two_piece(Fr(1, 2), 1, 0, 0, name="[x/2 | x] at 0")


# ------------------------------------------------------------------ runs

def cells(bmax):
    return sq.census(bmax)


def law_L(b, am, ap, fmap):
    return one.law_L(b, am, ap, fmap)


def run_map(b, am, ap, fmap, o=None, want=None):
    """One cell: the law's L*, the table's floor, the engine's floor; K2
    on their agreement at every L the engine read; returns the row."""
    if o is None:
        o = one.least_lead(b, am, ap, fmap)
    Ls = law_L(b, am, ap, fmap)
    tab = Table(b, am, ap, fmap)
    tfloor = tab.floor(Ls)
    efloor, verdicts = engine_floor(b, am, ap, fmap, o, Ls)
    tag = f"({b},{am},{ap}) {fmap.name}"
    ok(tfloor == efloor, f"K2 {tag}: table floor {tfloor}, engine floor {efloor}")
    for L, v in verdicts.items():
        ok((v[0] == "dead") == tab.dead(L), f"K2 {tag} at L={L}: engine {v[0]}, table {'dead' if tab.dead(L) else 'alive'}")
    kill = verdicts.get(efloor - 1) if efloor is not None else None
    row = dict(cell=(b, am, ap), o=o, Ls=Ls, tfloor=tfloor, efloor=efloor, kill=kill)
    if kill is not None and kill[0] == "dead":
        pieces, kinks, (nf, n_end, back) = tab.verdict(efloor - 1)
        row["clauses"] = (pieces, kinks)
        row["cycle"] = (nf, n_end, back)
        ok(kill[2] <= n_end + 1, f"K5 {tag}: kill at n={kill[2]} past the cycle (n_full {nf}, repeat at {n_end + 1})")
        where = "STRADDLER" if kill[4] else f"piece {fmap.piece(Fr((b - 1) * kill[3] - am, (b - 1) * b ** kill[2]))}" if kill[3] is not None else "tree"
        cl = ",".join(f"p{j}:{'D' if d else '-'}" for j, d in pieces.items()) + " " + \
             ",".join(f"k{i}:{'D' if d else '-'}" for i, d in kinks.items())
        print(f"  ({b},{am},{ap}) o={o} L*={Ls}: floor table {tfloor} engine {efloor}; kill at L={efloor - 1}: t={kill[1]} n={kill[2]} "
              f"u={kill[3]} at {where}; clauses [{cl}]; cycle n_full={nf} repeat {n_end + 1}->{back}")
    else:
        print(f"  ({b},{am},{ap}) o={o} L*={Ls}: floor table {tfloor} engine {efloor} (no kill found down to L*-{LMIN_BELOW})")
    return row


def oracle(bmax):
    print(f"\n=== P-A the oracle: x and x/2 at lead 0, radices 2..{bmax}")
    ident, half = affine(1, name="x"), affine(Fr(1, 2), name="x/2")
    n_id = n_half = n_sym = 0
    for (b, am, ap) in cells(bmax):
        r = run_map(b, am, ap, ident, o=0)
        clause_floor = next(L for L in range(-LMIN_BELOW, 6) if not sq.ksum_clause_dead(1, b, am, ap, L))
        good = r["efloor"] == clause_floor
        ok(good, f"K1 x ({b},{am},{ap}): engine floor {r['efloor']}, the k=1 clause's {clause_floor}")
        n_id += good
        r = run_map(b, am, ap, half, o=0)
        n_half += r["efloor"] == r["tfloor"]
        if am == ap:
            cmin = slope.cmin_derived(b, am, 1, 2)   # the criterion reads c >= 0 only
            good = max(r["efloor"], 0) == cmin
            ok(good, f"K1 x/2 ({b},{am},{ap}): engine floor {r['efloor']}, the criterion's c_min {cmin}")
            n_sym += good
    print(f"  x agrees with the k = 1 clause at {n_id} of {len(cells(bmax))}; x/2 with the criterion at {n_sym} of "
          f"{sum(1 for (b, am, ap) in cells(bmax) if am == ap)} symmetric cells and with the table at {n_half} of {len(cells(bmax))}")


def run_specimen(bmax):
    print(f"\n=== P-B the specimen [x/2 | x] at 0, radices 2..{bmax}")
    f = specimen()
    agree_hand = agree = 0
    rows = []
    for (b, am, ap) in cells(bmax):
        tab = Table(b, am, ap, f)
        pieces, kinks, _ = tab.verdict(0)
        hand = hand_table_specimen(b, am, ap)
        got = (pieces[0], pieces[1], kinks[0])
        ok(got == hand, f"P-B table at ({b},{am},{ap}) L=0: {got}, the hand table {hand}")
        agree_hand += got == hand
        r = run_map(b, am, ap, f)
        ok(r["Ls"] == 1, f"P-B L*={r['Ls']} at ({b},{am},{ap})")
        agree += r["efloor"] == r["tfloor"]
        rows.append(r)
    dead0 = [r["cell"] for r in rows if r["efloor"] == 1]
    print(f"  table = hand table at {agree_hand} of {len(rows)}; engine floor = table floor at {agree} of {len(rows)}; "
          f"floor 1 at {dead0}, floor 0 at the other {len(rows) - len(dead0)}")
    return rows


SLOPES = [Fr(1, 2), Fr(1, 3), Fr(2, 3), Fr(3, 2), Fr(2), Fr(1, 4), Fr(3, 4), Fr(3)]
DESIGN_BUDGET = 10 ** 9            # the grid is exhausted at every cell


def design_kink(b, am, ap):
    """The first two-piece map on the grid whose table at L* - 1 has both
    pieces empty and the kink firing, preferring one whose kink first
    fires at a depth past the root (the root box straddles every kink);
    returns (map, first firing depth) or (None, None)."""
    den = 6 * (b - 1)
    kappas = [Fr(j, den) for j in range(-am * 6 + 1, ap * 6)]
    ds = [Fr(j, den) for j in range(-9, 10)]
    root = None
    tried = 0
    for sl, sr in itertools.product(SLOPES, repeat=2):
        for sign in (1, -1):                       # V: left down, right up; Lam: the mirror
            for kap in kappas:
                for d in ds:
                    tried += 1
                    if tried > DESIGN_BUDGET:
                        return root if root else (None, None)
                    f = two_piece(-sign * sl, sign * sr, kap, d)
                    L = law_L(b, am, ap, f) - 1
                    tab = Table(b, am, ap, f)
                    at_root = tab.kink_dead(0, 0, L)
                    if at_root and root is not None:
                        continue
                    pieces, kinks, (nf, n_end, back) = tab.verdict(L)
                    if any(pieces.values()) or not kinks[0]:
                        continue
                    first = next(n for n in range(0, n_end + 1) if tab.kink_dead(0, n, L))
                    if first >= 1:
                        return f, first
                    root = (f, 0)
    return root if root else (None, None)


def run_kink(bmax):
    print(f"\n=== P-C the kink alone: a design per cell from the table, radices 2..{bmax}")
    found = strad = deep = 0
    for (b, am, ap) in cells(bmax):
        f, first = design_kink(b, am, ap)
        if f is None:
            print(f"  ({b},{am},{ap}): no design on the grid")
            continue
        found += 1
        deep += first >= 1
        print(f"  design {f.name}, the kink's first firing depth n={first}")
        r = run_map(b, am, ap, f)
        k = r["kill"]
        good = r["efloor"] == r["Ls"] and k is not None and k[0] == "dead" and k[4]
        ok(good, f"P-C ({b},{am},{ap}) {f.name}: floor {r['efloor']} against L*={r['Ls']}, kill {k}")
        ok(k is None or k[2] == first, f"P-C ({b},{am},{ap}): the engine's kill at n={k[2]}, the table's first firing at n={first}")
        strad += good
    print(f"  designs at {found} of {len(cells(bmax))} cells, {deep} of them firing first past the root; "
          f"certified at a straddling prefix at L*-1 and alive at L* at {strad}")


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
    run_specimen(bmax)
    run_kink(bmax)
    print(f"\nwall {time.time() - t0:.1f}s; failures: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)


if __name__ == "__main__":
    main()
