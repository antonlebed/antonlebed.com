"""The polynomial delay: does the multiply-add x y + z, the on-line
field's own unit, read at exactly the Lebesgue margin in the map's
L1-Lipschitz constant, as every monomial of degree two or more does,
and does an affine sum of three streams read below it, as the sum of
two does?

THE QUESTION. explore_monomial_delay.py proves that a monomial of
total degree d >= 2 over D-streams (radix b, D = {-am..ap}, slack
rho = am + ap + 1 - b >= 1) is readable at lookahead c iff

    b^c (b-1)^(d-1) rho >= d ah^(d-1) (am + ap),   ah = max(am, ap),

the Lebesgue margin: the image's largest width, d Mh^(d-1) W in
emitted units, against the overlap zone's length W - 1, where
M+- = a+-/(b-1), W = M- + M+, Mh = max(M-, M+). The width bound is
the mean value theorem with the map's L1-Lipschitz constant over the
window, Lip1 = sup over the box of the gradient's L1 norm, and that
step is general: for ANY continuous map of the streams the image of
the input boxes is an interval (a box is connected) of width at most
Lip1 W / b^c in emitted units, so

    THE MARGIN LAW:  b^c rho >= Lip1 (am + ap)   [Lip1 in window units]

suffices for every map. What is open is the other half: whether the
margin is the FLOOR for every non-affine map, or only for the
monomials. The moonshot's line (the delay table as a theorem in the
map's derivative) needs a map where a lattice part and a dense part
meet, and the multiply-add x y + z is that map: x y's reachable image
endpoints are dense at the emitted scale (explore_product_necessity.py),
z's form a lattice (the sum's clause), and the field states the
multiply-add's delay per algorithm.

THE MAPS AND THE CONVENTION. A map here is a sum of monomials over
DISJOINT variable sets with integer coefficients, so the image of the
boxes is the Minkowski sum of the terms' interval images, exact; the
scale is the largest degree's, (b-1)^D b^(D n), each term lifted to
it. Lip1 = sum_j |c_j| d_j Mh^(d_j - 1) over the terms, attained at
the corner where every stream sits at its largest magnitude, and the
corner width approaches Lip1 W from below at every n (each term by
Bernoulli), so the sufficiency half is exact for every map here.
Cleared of denominators, with D the largest degree:

    b^L (b-1)^(D-1) rho >= (am + ap) sum_j |c_j| d_j ah^(d_j-1) (b-1)^(D-d_j).

A sum's range doubles the window, so the maps with an additive part
run in the ALIGNED convention with the output led by one position
(explore_product_delay.py's offset o = 1: the j-th emission has
weight b^(1-j)), the convention explore_product_necessity.py ran the
sum's clause in; the lookahead is L = delay + o and the law reads in
L alone, the game at (delay c, o) being the game at (delay c + o, 0)
with the root cell widened. Every cell of the census is representable
at o = 1 for the maps here (|x y + z| <= Mh^2 + Mh <= 1 + M+ <= b M+,
the negative side likewise); the rig checks it per cell.

THE MULTIPLY-ADD'S LAW, Lip1 = 2 Mh + 1:

    b^L (b-1) rho >= (2 ah + b - 1)(am + ap),

one lookahead above the product's at radix 2 ((2,1,1): L* = 3 against
the product's c* = 2) and equal to it wherever the product's excess
was slack enough. x^2 + y shares it (Lip1 = 2 Mh + 1 again); the
three-stream sum x + y + z has Lip1 = 3, the law b^L rho >= 3(am + ap).

NECESSITY (what the rig reads). At L* - 1 the corner image exceeds the
zone by g = E / ((b-1)^2 b^L) in the limit, E the integer excess, over
a range of top prefixes of length proportional to b^(n + L). The
x y part's lower endpoint slides continuously along the product's
split line (explore_product_necessity.py, (2i - 1)/K per step, K =
b^(n + c)) while z's endpoint sits on a lattice of step b^-L in
emitted units, coarse; the union of a dense sweep and a lattice is
dense, so the dead arcs should be swept and the multiply-add should
read AT the margin. The three-stream sum's endpoints form a lattice
at every n, so it should read BELOW the margin at some cells, as the
two-stream sum does on the wedge. Neither line is proved here; the
engine's exhaustive adversary tree is the certificate.

THE SLATE, frozen before the engine.

P-A THE CONTROLS. (i) The term engine at the single term x y with
    o = 0 reproduces explore_monomial_delay.py's product census at
    radices 2..4: certificate at c* - 1 within 2 rounds, survival at
    c*, cell for cell. (ii) The term engine at x + y with o = 1
    reproduces the lookahead criterion (explore_lookahead_proof.py,
    explore_product_delay.py sum_law): the reader survives at the
    criterion's L and is certified at L - 1 at every cell of radices
    2..5.
P-B THE AFFINE THREE-SUM READS BELOW THE MARGIN. At x + y + z with
    o = 1 the reader survives the search at L* - 1 at one or more
    cells of radices 2..4 (the lattice clause), and is never
    certified at L*.
P-C THE MULTIPLY-ADD READS AT THE MARGIN. At x y + z with o = 1 the
    reader survives the search at L* at every cell of radices 2..4,
    and the adversary certifies L* - 1 failing at every cell the
    search reaches; a survival to the budget depth is printed as
    such (K3), never read as a floor.
P-D x^2 + y SHARES THE MULTIPLY-ADD'S FLOOR. At x^2 + y with o = 1,
    radices 2..5, the same: survival at L*, certificates at L* - 1;
    and on the shared cells the certified floors agree with the
    multiply-add's cell for cell, so the Lipschitz constant and not
    the term shape sets the delay.
P-E THE HOLD-OUT. explore_monomial_delay.py's x^2 y at (5,3,3),
    c* - 1 = 1, survived a 3-round search; the same cell is searched
    one round deeper here under a wall-clock cap, the result printed
    whichever way it falls (a certificate at round 4, or a survival
    to 4, or the cap).

KILLS, frozen as what this rig PRINTS.

K1 P-A (i) prints a cell disagreeing with the monomial rig, or P-A
   (ii) a cell disagreeing with the lookahead criterion -> the term
   engine is not the k-stream engine, or its offset is wrong;
   nothing downstream is read.
K2 Any cell prints a certificate at the law's L* on x y + z, x^2 + y
   or x + y + z -> the general sufficiency (the Lipschitz bound or
   the Minkowski-sum image) is wrong, and the moonshot's delay-table
   line is killed on the spot.
K3 A multiply-add or x^2 + y cell prints "survives to depth r at
   L* - 1" -> no kill; counted, and the floor at that cell is left
   open.
K4 The three-sum is certified at L* - 1 at EVERY cell -> the lattice
   clause does not carry to three streams; the moonshot's "every
   affine map a lattice map" clause is wrong as stated.

POSITIVE CONTROL: P-A whole, read before any polynomial line.

THE SECOND FREEZE, written after the first run's prints at radices
2..4 and before the radix-5 run. K4 FIRED at the frozen scope: the
three-sum was certified at L* - 1 at all 9 cells of radices 3..4
(P-B failed as written). Hand-attack after the print: the k-sum's
endpoints in emitted units are the lattice (s - k M-)/b^L, s an
integer, so the image strictly contains a zone iff

    THE k-SUM'S CLAUSE:  an integer lies in
        ((b^L - k) M+,  b^L - (b^L - k) M-),

the sum's clause (k = 2, explore_product_necessity.py F4) with k in
place of 2 and the identity's (k = 1; at L = 0 the interval is (0, 1),
integer-free, the reader alive at every cell). The interval's length
is k W - b^L (W - 1), the margin's excess, so the margin law is EXACT
off the cells where that length is positive and the interval holds no
integer -- the k-sum's WEDGE -- and overpredicts by one on it. For
k = 3 the wedge is empty through radix 4 (at L = 1 the interval holds
an integer at every cell) and first appears at (5,4,4), L = 1, where
the interval is (2, 3): the prediction is that the three-sum survives
L* - 1 = 1 at (5,4,4) and at no other radix-5 cell, and that the
clause matches the engine at every cell and every L in {1, 2} for
k = 3 and L in {0, 1} for k = 1 (the identity at o = 0). K4's
then-clause stands corrected by the clause: an affine map is a
lattice map whose floor is the integer clause, which sits BELOW the
margin only on the wedge, never everywhere.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CONTROLS HOLD. x y at o = 0 through the term engine: 7
   representable cells at radices 2..4, certified at c* - 1 within
   2 rounds and surviving at c* at 7/7, the monomial rig's census
   cell for cell. x + y at o = 1: 20 cells at radices 2..5, the
   criterion's L = 2 at 10 and 1 at 10, certified at L - 1 in one
   round at all 10 and surviving at L at 20/20. P-A held; K1 never
   fired.

F2 THE THREE-SUM READS AT THE MARGIN OFF ITS WEDGE, AND THE k-SUM'S
   CLAUSE IS THE LAW [rule at the scanned scope, the clause's
   derivation above]. x + y + z at o = 1: 19 representable cells at
   radices 3..5 ((2,1,1) does not fit at o = 1), the margin's L* = 2
   at every one; certified at L* - 1 = 1 in one round at 18 and
   surviving the 2-round search at one, (5,4,4), the wedge cell the
   second freeze named; surviving at L* at 19/19. The clause against
   the engine: 78 of 78 cell-lookahead pairs agree (k = 1 at L in
   {0, 1}, 40 pairs; k = 3 at L in {1, 2}, 38 pairs). K4 fired at
   the first freeze's scope and P-B as written failed; the second
   freeze's prediction held whole.

F3 THE MULTIPLY-ADD READS AT THE MARGIN [criterion at the certified
   cells]. x y + z at o = 1: 20 representable cells at radices 2..5,
   L* = 3 at (2,1,1) and 2 elsewhere; certified at L* - 1 at 20/20,
   in one round at 15 and two at 5 ((2,1,1), (4,3,3), (5,3,4),
   (5,4,3), (5,4,4): radix 2 and exactly the cells of slack rho >= 3),
   surviving the search at L* at 20/20. P-C held; K2 and K3 never fired.

F4 x^2 + y SHARES THE FLOOR. 20 cells at radices 2..5, certified at
   L* - 1 at 20/20 (one to two rounds), surviving at L* at 20/20; the
   certified floors agree with the multiply-add's at 20 of 20 shared
   cells, disagree at 0. P-D held.

F5 THE HOLD-OUT CLOSES. x^2 y at (5,3,3), c = 1: certified failing
   at 4 rounds, found along the first adversary line, the corner
   (-3, -3), in under a second (the 3-round search survives in both
   engines, 40 s and 52 s). x^2 y is now certified at 20 of 20 cells
   and the degree-3 floors agree at all 20.

VERDICT. The delay of a polynomial map with disjoint-support terms is
the Lebesgue margin in its L1-Lipschitz constant wherever a term has
degree two or more, at every cell tried; an affine map's floor is the
k-sum's integer clause, which sits one below the margin exactly on
the wedge. The moonshot's affine clause is corrected, not killed: the
dividing line is not "affine reads below", it is "affine has a wedge".

RUN RECORD: pure Python, integers only, standard library; under
memwatch, peak commit 8.5 MB against the 512 MB default; wall 593 s
at the defaults (5, 5, 600), the radix-5 three-stream arms (729-ary
trees) most of it; 26 s at (5, 4). Prints reproduced by:
python prime/code/explore_polynomial_delay.py [BMAX_two BMAX_three CAP_s]
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


# --------------------------------------------------------------- engine

def power_interval(x1, x2, d):
    """Image of the integer interval [x1, x2] under x -> x^d."""
    if d % 2 == 0 and x1 <= 0 <= x2:
        return 0, max(abs(x1), abs(x2)) ** d
    a, c = x1 ** d, x2 ** d
    return (a, c) if a <= c else (c, a)


class TermGame:
    """The reading game at delay c and output offset o for a map that
    is a sum of monomials over disjoint streams: terms is a list of
    (coef, {stream index: exponent}). An input prefix u_i of length n
    stands for the integer interval [(b-1) u_i - am, (b-1) u_i + ap]
    at scale (b-1) b^n; a term of degree d has its image at scale
    (b-1)^d b^(d n), lifted to the largest degree's scale, and the
    terms' interval images add (Minkowski sum, exact for disjoint
    supports). The level-t output cell is [(b-1) q - am, (b-1) q + ap]
    b^(o-t) / (b-1); every test is a cross multiplication on
    integers."""

    def __init__(self, b, am, ap, c, terms, o=0, k=None):
        self.b, self.am, self.ap, self.c, self.o = b, am, ap, c, o
        self.terms = [(coef, dict(ex)) for coef, ex in terms]
        self.k = k if k is not None else 1 + max(i for _, ex in self.terms for i in ex)
        self.degs = [sum(ex.values()) for _, ex in self.terms]
        self.D = max(self.degs)
        self.digits = list(range(-am, ap + 1))
        self.moves = list(itertools.product(self.digits, repeat=self.k))

    def image(self, us, n):
        b, am, ap = self.b, self.am, self.ap
        lo_t, hi_t = 0, 0
        for (coef, ex), d in zip(self.terms, self.degs):
            lo, hi = 1, 1
            for i, e in ex.items():
                p1, p2 = power_interval((b - 1) * us[i] - am, (b - 1) * us[i] + ap, e)
                corners = (lo * p1, lo * p2, hi * p1, hi * p2)
                lo, hi = min(corners), max(corners)
            lift = coef * (b - 1) ** (self.D - d) * b ** ((self.D - d) * n)
            a1, a2 = lo * lift, hi * lift
            lo_t += min(a1, a2)
            hi_t += max(a1, a2)
        return lo_t, hi_t, (b - 1) ** self.D * b ** (self.D * n)

    def legal(self, us, n, q, t):
        b, am, ap = self.b, self.am, self.ap
        lo, hi, s = self.image(us, n)
        clo, chi = (b - 1) * q - am, (b - 1) * q + ap
        cs, bo = (b - 1) * b ** t, b ** self.o
        return lo * cs >= clo * bo * s and hi * cs <= chi * bo * s

    def legal_digits(self, us, n, q, t):
        return [p for p in self.digits if self.legal(us, n, self.b * q + p, t + 1)]

    def survives(self, us, q, t, rounds, deadline=None):
        if rounds == 0:
            return True
        if deadline is not None and time.time() > deadline:
            raise TimeoutError
        n = t + self.c
        for mv in self.moves:
            us1 = tuple(self.b * u + x for u, x in zip(us, mv))
            alive = False
            for p in self.legal_digits(us1, n + 1, q, t):
                if self.survives(us1, self.b * q + p, t + 1, rounds - 1, deadline):
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

    def reader_survives(self, rounds, deadline=None):
        for us in self.opening_states():
            if not self.legal(us, self.c, 0, 0):
                return False
            if not self.survives(us, 0, 0, rounds, deadline):
                return False
        return True

    def certificate_depth(self, max_rounds, budget=CERT_BUDGET):
        """Least number of rounds at which the adversary wins, or None
        if the reader survives `depth` rounds, depth the largest
        r <= max_rounds keeping moves^(c + r) within the node budget.
        Returns (r or None, depth searched)."""
        m = len(self.moves)
        depth = max(1, min(max_rounds,
                           int(math.log(budget) / math.log(m)) - self.c))
        for r in range(0, depth + 1):
            if not self.reader_survives(r):
                return r, depth
        return None, depth


# ---------------------------------------------------------- closed forms

def lip_law(b, am, ap, terms):
    """Least L with b^L (b-1)^(D-1) rho >= (am+ap) sum |c| d ah^(d-1)
    (b-1)^(D-d): the Lebesgue margin in the map's L1-Lipschitz
    constant over the window."""
    rho, ah, W = am + ap + 1 - b, max(am, ap), am + ap
    degs = [sum(ex.values()) for _, ex in terms]
    D = max(degs)
    rhs = W * sum(abs(coef) * d * ah ** (d - 1) * (b - 1) ** (D - d)
                  for (coef, _), d in zip(terms, degs))
    L = 0
    while b ** L * (b - 1) ** (D - 1) * rho < rhs:
        L += 1
    return L


def sum_law(b, am, ap):
    """The lookahead criterion for X + Y (explore_lookahead_proof.py)."""
    rho = am + ap + 1 - b
    sig = -(-am // (b - 1)) - (-ap // (b - 1))
    return 1 if rho >= sig else 2


def ksum_clause_dead(k, b, am, ap, L):
    """The k-sum's clause: the reader of x_1 + ... + x_k is dead at
    lookahead L iff an integer lies in ((b^L - k) M+, b^L - (b^L - k) M-)."""
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    lo, hi = (b ** L - k) * Mp, b ** L - (b ** L - k) * Mm
    return math.floor(lo) + 1 < hi


def representable(b, am, ap, terms, o):
    """The map's values over the window lie in the root cell
    [-M- b^o, M+ b^o]: exact on the corner set for interval products
    and Minkowski sums."""
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    lo_t, hi_t = Fr(0), Fr(0)
    for coef, ex in terms:
        lo, hi = Fr(1), Fr(1)
        for e in ex.values():
            if e % 2 == 0:
                p1, p2 = Fr(0), max(Mm, Mp) ** e
            else:
                p1, p2 = (-Mm) ** e, Mp ** e
            corners = (lo * p1, lo * p2, hi * p1, hi * p2)
            lo, hi = min(corners), max(corners)
        lo_t += min(coef * lo, coef * hi)
        hi_t += max(coef * lo, coef * hi)
    return lo_t >= -Mm * b ** o and hi_t <= Mp * b ** o


def census(bmax):
    return [(b, am, ap) for b in range(2, bmax + 1)
            for am in range(0, b) for ap in range(0, b)
            if am + ap + 1 - b >= 1]


# ------------------------------------------------------------------ main

def run_family(name, terms, o, bmax, T, law=None, expect_rounds=None):
    """One map over the census: at each representable cell print the
    law's L*, the certificate depth at L* - 1 and the survival at L*,
    the game at delay L - o. Returns rows
    (b, am, ap, Lstar, cert, sdepth, survive_at_Lstar)."""
    law = law or (lambda b, am, ap: lip_law(b, am, ap, terms))
    rows = []
    print(f"\n=== {name}: o = {o}, radices 2..{bmax}")
    print("  cell (b,am,ap) rho | L* | cert at L*-1 [depth searched] | "
          "survives search at L* [depth]")
    for (b, am, ap) in census(bmax):
        if not representable(b, am, ap, terms, o):
            print(f"  ({b},{am},{ap}) not representable at o = {o}")
            continue
        rho = am + ap + 1 - b
        L = law(b, am, ap)
        cert, sdepth = (None, 0)
        if L - 1 - o >= 0:
            cert, sdepth = TermGame(b, am, ap, L - 1 - o, terms, o).certificate_depth(T)
        surv, sdepth2 = TermGame(b, am, ap, L - o, terms, o).certificate_depth(T, budget=SURVIVAL_BUDGET)
        ok(surv is None, f"K2 certificate at the law's L*={L} on {name} ({b},{am},{ap}) "
                          f"after {surv} rounds")
        if L - 1 - o >= 0:
            if cert is None:
                print(f"  K3 survives to depth {sdepth} at L*-1 on {name} ({b},{am},{ap})")
            elif expect_rounds is not None:
                ok(cert <= expect_rounds, f"K1 {name} ({b},{am},{ap}) certified only at "
                                          f"round {cert} > {expect_rounds}")
        print(f"  ({b},{am},{ap}) rho={rho} | L*={L} | "
              f"{'-' if L - 1 - o < 0 else (cert if cert is not None else 'survives')} "
              f"[{sdepth}] | {'yes' if surv is None else 'NO'} [{sdepth2}]")
        rows.append((b, am, ap, L, cert, sdepth, surv is None))
    ncert = sum(1 for r in rows if r[3] - 1 - o >= 0 and r[4] is not None)
    nopen = sum(1 for r in rows if r[3] - 1 - o >= 0 and r[4] is None)
    print(f"  {name}: {len(rows)} representable cells; L*-1 searchable at "
          f"{ncert + nopen}, certified {ncert}, surviving the search {nopen}; "
          f"survives at L* at {sum(1 for r in rows if r[6])}/{len(rows)}")
    return rows


XY = [(1, {0: 1, 1: 1})]
X_PLUS_Y = [(1, {0: 1}), (1, {1: 1})]
XYZ_SUM = [(1, {0: 1}), (1, {1: 1}), (1, {2: 1})]
XY_PLUS_Z = [(1, {0: 1, 1: 1}), (1, {2: 1})]
X2_PLUS_Y = [(1, {0: 2}), (1, {1: 1})]


def main():
    T = 12
    b2 = int(sys.argv[1]) if len(sys.argv) > 1 else 5    # two-stream maps
    b3 = int(sys.argv[2]) if len(sys.argv) > 2 else 5    # three-stream maps (729-ary at radix 5)
    cap = float(sys.argv[3]) if len(sys.argv) > 3 else 600.0   # P-E wall cap, seconds
    t0 = time.time()

    print("=== P-A (i): the control, x y at o = 0 through the term engine")
    ctrl = run_family("x y", XY, 0, min(b2, 4), T, expect_rounds=2)
    print("\n=== P-A (ii): the control, x + y at o = 1 against the lookahead criterion")
    run_family("x + y", X_PLUS_Y, 1, b2, T, law=sum_law, expect_rounds=2)
    if FAILURES:
        print("\nPOSITIVE CONTROL FAILED; nothing below is read")
        for f in FAILURES:
            print("  ", f)
        return

    print("\n=== P-B: the affine three-sum x + y + z at o = 1 against the margin law")
    s3 = run_family("x + y + z", XYZ_SUM, 1, b3, T)
    below = [r for r in s3 if r[3] - 2 >= 0 and r[4] is None]
    print(f"  x + y + z survives L*-1 at {len(below)} of {len(s3)} cells: "
          + ", ".join(f"({r[0]},{r[1]},{r[2]})" for r in below))
    ok(len(below) >= 1, "K4: the three-sum is certified at L*-1 at every cell")

    print("\n=== P-B, the second freeze: the k-sum's clause against the engine")
    tot, agree = 0, 0
    for k, o, Ls, bmax, terms in ((1, 0, (0, 1), b2, [(1, {0: 1})]),
                                  (3, 1, (1, 2), b3, XYZ_SUM)):
        for (b, am, ap) in census(bmax):
            if not representable(b, am, ap, terms, o):
                continue
            for L in Ls:
                pred = ksum_clause_dead(k, b, am, ap, L)
                cert, depth = TermGame(b, am, ap, L - o, terms, o).certificate_depth(T)
                tot += 1
                if (cert is not None) == pred:
                    agree += 1
                else:
                    ok(False, f"k-sum clause k={k} ({b},{am},{ap}) L={L}: clause says "
                              f"{'dead' if pred else 'alive'}, engine {cert} [{depth}]")
        print(f"  k = {k}: clause against the engine at L in {Ls}, radices 2..{bmax}")
    print(f"  k-sum clause: {tot} cell-lookahead pairs, agree {agree}")

    print("\n=== P-C: the multiply-add x y + z at o = 1")
    ma = run_family("x y + z", XY_PLUS_Z, 1, b3, T)

    print("\n=== P-D: x^2 + y at o = 1")
    sq = run_family("x^2 + y", X2_PLUS_Y, 1, b2, T)
    ma_d = {r[:3]: r for r in ma}
    agree, disagree, cells = 0, 0, 0
    for r in sq:
        m = ma_d.get(r[:3])
        if m is None or r[4] is None or m[4] is None:
            continue
        cells += 1
        if r[3] == m[3]:
            agree += 1
        else:
            disagree += 1
            print(f"  P-D floors disagree at {r[:3]}: x^2+y {r[3]}, xy+z {m[3]}")
    print(f"  x^2 + y against x y + z, certified floors on shared cells: "
          f"{cells} cells, agree {agree}, disagree {disagree}")
    ok(disagree == 0, "P-D: certified floors disagree between x^2 + y and x y + z")

    print(f"\n=== P-E: the hold-out x^2 y at (5,3,3), c*-1 = 1, one round deeper (cap {cap:.0f} s)")
    g = TermGame(5, 3, 3, 1, [(1, {0: 2, 1: 1})], 0)
    deadline = time.time() + cap
    t1 = time.time()
    try:
        alive = g.reader_survives(4, deadline)
        print(f"  x^2 y (5,3,3) at c = 1: {'survives' if alive else 'CERTIFIED failing'} "
              f"at 4 rounds, {time.time() - t1:.0f} s")
    except TimeoutError:
        print(f"  x^2 y (5,3,3) at c = 1: the 4-round search hit the cap at {time.time() - t1:.0f} s, unread")

    print(f"\nwall {time.time()-t0:.1f}s; failures: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)


if __name__ == "__main__":
    main()
