"""The monomial delay: does every monomial map of signed-digit streams
read at exactly the Lebesgue margin, as the product of two streams
does, with the total degree its only parameter?

THE QUESTION. explore_product_delay.py and
explore_product_necessity.py prove that the product X * Y of two
D-streams (radix b, D = {-am..ap}, slack rho = am + ap + 1 - b >= 1,
the output aligned with the inputs) is readable at lookahead c iff

    b^c (b-1) rho >= 2 max(am, ap) (am + ap),

the Lebesgue margin verbatim: the image's largest width against the
level cover's Lebesgue number, with the stream correction zero
because the product's reachable image endpoints are dense at the
emitted scale, where the sum's form a lattice and the exact law sits
one digit above the margin. The field derives an on-line unit's delay
per algorithm from a range analysis of that unit's residual. If every
non-affine map reads at the margin, the delay is one formula in the
map's derivative and no range analysis is owed. This rig asks it of
the monomials: x^2 and x^3 of one stream, x^2 y of two, x y z of
three, beside x y as the control and the identity x as the affine
control.

THE DERIVATION, in units of b^-(t+1) at the emitted level, with
n = t + 1 + c the input length, M- = am/(b-1), M+ = ap/(b-1),
W = M- + M+, Mh = max(M-, M+). For a monomial of total degree d over
k streams the image of the k input boxes is an interval — each
stream's power image is an interval and interval products are exact
— lying in the parent cell when the history was legal, so THE DEATH
CRITERION of explore_product_necessity.py holds verbatim: the reader
has no legal digit iff the image STRICTLY CONTAINS an overlap zone
[m + 1 - M-, m + M+] of two consecutive cells, length W - 1. The
scale is K_d = b^((d-1) n + c).

SUFFICIENCY. At the corner where every stream sits at its largest
magnitude the box ends are A = Mh b^n and A - W (one stream) or their
products, and the width in emitted units is

    (A^d - (A - W)^d) / K_d  <=  d A^(d-1) W / K_d  =  d Mh^(d-1) W / b^c

by Bernoulli ((A - W)^d >= A^d - d A^(d-1) W for A >= W), at every n,
and every other box has a smaller width (the gradient's L1 norm is
largest there). So no image strictly contains a zone whenever
d Mh^(d-1) W <= W - 1 in emitted units, which clears denominators to

    THE MONOMIAL LAW:  b^c (b-1)^(d-1) rho >= d ah^(d-1) (am + ap),
    ah = max(am, ap),

the product's law at d = 2 and a law in the DEGREE alone: x^2 and
x y share it, x^3, x^2 y and x y z share it.

NECESSITY (the floor's mechanism, what the rig reads and the proof
owes). When the law fails by the integer excess
E = d ah^(d-1)(am + ap) - b^c (b-1)^(d-1) rho >= 1 the corner image
exceeds the zone by g = E / ((b-1)^d b^c) in the limit and the excess
persists over a range of top prefixes of length proportional to
b^(n+c). Where two streams enter linearly the split line of the
product's proof runs with the other streams held at the corner (a
constant multiplier on the parabola's step). For one stream the
endpoints are (u - M-)^d / K_d as u runs over that range: at d = 2
the progression u = u0 + j (b-1)^(d-2) b^h with 2h >= (d-1) n + c
makes the phase LINEAR in j (the j^2 term is a multiple of K_d), a
split line of the product's shape whose step is set by u0's low
digits; at d >= 3 the phases of a range of length ~ b^(n+c) modulo
b^((d-1)n+c) equidistribute by Weyl's inequality (the range exceeds
the modulus's (1/d)-th power), so a dead arc of fixed length is hit
once n is large. Neither line is run here; the engine's exhaustive
adversary tree is the certificate, and a certificate's DEPTH is
what the rig reads about the mechanism.

THE SLATE, frozen before the engine.

P-A THE CONTROL. At exponents (1, 1) the k-stream engine reproduces
    explore_product_delay.py: at every representable cell of radices
    2..5 with c* >= 1 the adversary certifies c* - 1 failing within
    2 rounds, and the exact reader survives the search at c*.
P-B THE IDENTITY IS THE AFFINE CONTROL. At exponents (1,) the reader
    survives the search at c = 0 at every cell, where the margin law
    reads c* >= 1 at every cell with rho < am + ap: the margin is not
    the floor at degree 1, the lattice clause is.
P-C x^2 READS AT THE MARGIN, ONE DIGIT AT A TIME. At exponents (2,)
    the law is the product's; the reader survives the search at c*
    at every representable cell, and the adversary certifies c* - 1
    failing at every cell with c* >= 1, at a depth >= the product's
    at the same cell and strictly greater at some (one digit per
    round in place of two; no split move).
P-D DEGREE 3, THREE SHAPES, ONE LAW. At exponents (3,), (2, 1) and
    (1, 1, 1) the law's c* agrees at every cell (the law reads the
    degree alone), the reader survives the search at c* at every
    representable cell, and the adversary certifies c* - 1 failing
    at every cell with c* >= 1 the search reaches — x y z within 2
    rounds (the split line with the third stream held), x^3 and
    x^2 y at a depth the rig reads. A survival at c* - 1 to the
    budget depth is not a kill and is printed as such.
P-E THE FLOORS AGREE ACROSS SHAPES. Where the engine certifies, the
    certified floor is the same at x^3, x^2 y and x y z cell for
    cell, so the degree and not the stream count sets the delay.

KILLS, frozen as what this rig PRINTS.

K1 P-A prints a cell disagreeing with explore_product_delay.py (a
   certificate at c*, or none at c* - 1 within 2 rounds) -> the
   k-stream engine is not the two-stream engine; nothing downstream
   is read.
K2 Any monomial cell prints a certificate at the law's c* -> the
   sufficiency derivation is wrong (the Bernoulli step or the
   corner's maximality), and the moonshot's delay-table line is
   killed on the spot: the margin is not the floor.
K3 A cell prints "survives to depth r at c* - 1" -> no kill, the
   mechanism there is deeper than the search; printed and counted.
K4 P-B prints a certificate at c = 0 for the identity -> the engine's
   legality or scale is wrong.

POSITIVE CONTROL: P-A and P-B whole, read before any monomial line.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CONTROL HOLDS. x y through the k-stream engine: 13
   representable cells at radices 2..5, c* >= 1 at all, the adversary
   certifying c* - 1 in 1 or 2 rounds at every one and the reader
   surviving the search at c* at 13/13, explore_product_delay.py's
   census cell for cell. P-A held; K1 never fired.

F2 THE IDENTITY SURVIVES BELOW THE MARGIN. At all 20 census cells the
   margin law reads c* = 1 for x and the reader survives c = 0 to the
   budget depth (5 to 11 rounds): the margin is not the floor at
   degree 1. P-B held; K4 never fired.

F3 x^2 READS AT THE MARGIN [criterion at the certified cells, the
   proof in explore_square_line.py]. 13 representable cells, the
   product's law at every one; certified c* - 1 failing at 13/13, in
   1 to 4 rounds ((4,2,2) at 4), and surviving the search at c* at
   13/13. Against x y on the same cells the certificate is deeper at
   2 and equal at 11, shallower at 0. P-C held; K2 never fired.

F4 DEGREE 3, ONE LAW, THREE SHAPES. x^3: 20 representable cells,
   certified 20/20 (c* = 3 at (2,1,1), 2 elsewhere; 1 to 6 rounds,
   the 6 at (5,3,3), the cell of least excess E = 2), surviving at c*
   at 20/20. x^2 y: 20 cells, certified 19/20 in 1 or 2 rounds,
   surviving at c* at 20/20; the one hold-out is (5,3,3) at the
   2-round budget (K3, printed; a separate 3-round search, 49^4
   nodes, also survives). x y z at radices 2..3: 4 cells, certified
   4/4 in 1 or 2 rounds, surviving at c* at 4/4. P-D held with the
   one K3; K2 never fired at any of the 57 monomial cells.

F5 THE FLOORS AGREE. On the 20 cells the three degree-3 shapes
   share, the certified floors agree at 20, disagree at 0: the degree
   and not the stream count sets the delay. P-E held.

VERDICT. The margin is the floor from degree 2 on and the degree is
the law's only parameter; the moonshot's kill (a certificate at the
law's c) missed at every one of 57 cells. The affine case is the
exception: the identity's lattice of endpoints threads the zones.

RUN RECORD: pure Python, integers only, standard library; under
memwatch, peak commit 9.2 MB against the 512 MB default; wall 61 s
at the defaults (5, 5, 3). Prints reproduced by:
python prime/code/explore_monomial_delay.py [BMAX_one BMAX_two BMAX_three]
"""

import itertools
import math
import sys
import time
from fractions import Fraction as Fr

FAILURES = []
SURVIVAL_BUDGET = 200_000   # a survival is a sanity print, never a proof; the certificate search keeps 2M


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


class KGame:
    """The reading game at lookahead c for a monomial prod X_i^(d_i) of
    k streams. An input prefix u_i of length n stands for the box
    (u_i - M-, u_i + M+) b^-n, the integer interval
    [(b-1) u_i - am, (b-1) u_i + ap] at scale (b-1) b^n; the image is
    at scale (b-1)^d b^(d n), d the total degree, and is compared with
    the level-t cell [(b-1) q - am, (b-1) q + ap] b^-t / (b-1) by cross
    multiplication, every test on integers. The output is aligned
    with the inputs (offset 0), the product game's convention."""

    def __init__(self, b, am, ap, c, exps):
        self.b, self.am, self.ap, self.c = b, am, ap, c
        self.exps = tuple(exps)
        self.k = len(self.exps)
        self.d = sum(self.exps)
        self.D = list(range(-am, ap + 1))
        self.moves = list(itertools.product(self.D, repeat=self.k))

    def image(self, us, n):
        b, am, ap = self.b, self.am, self.ap
        lo, hi = 1, 1
        for u, e in zip(us, self.exps):
            p1, p2 = power_interval((b - 1) * u - am, (b - 1) * u + ap, e)
            corners = (lo * p1, lo * p2, hi * p1, hi * p2)
            lo, hi = min(corners), max(corners)
        return lo, hi, (b - 1) ** self.d * b ** (self.d * n)

    def legal(self, us, n, q, t):
        b, am, ap = self.b, self.am, self.ap
        lo, hi, s = self.image(us, n)
        clo, chi = (b - 1) * q - am, (b - 1) * q + ap
        cs = (b - 1) * b ** t
        return lo * cs >= clo * s and hi * cs <= chi * s

    def legal_digits(self, us, n, q, t):
        return [p for p in self.D if self.legal(us, n, self.b * q + p, t + 1)]

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

    def certificate_depth(self, max_rounds, budget=2_000_000):
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

def monomial_law(b, am, ap, d):
    """Least c with b^c (b-1)^(d-1) rho >= d ah^(d-1) (am + ap)."""
    rho, ah, W = am + ap + 1 - b, max(am, ap), am + ap
    c = 0
    while b ** c * (b - 1) ** (d - 1) * rho < d * ah ** (d - 1) * W:
        c += 1
    return c


def representable(b, am, ap, exps):
    """The monomial's values over the window [-M-, M+]^k lie in the
    window: computed on the corner set, exact for interval products."""
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    lo, hi = Fr(1), Fr(1)
    for e in exps:
        if e % 2 == 0:
            p1, p2 = Fr(0), max(Mm, Mp) ** e
        else:
            p1, p2 = (-Mm) ** e, Mp ** e
        corners = (lo * p1, lo * p2, hi * p1, hi * p2)
        lo, hi = min(corners), max(corners)
    return lo >= -Mm and hi <= Mp


def census(bmax):
    return [(b, am, ap) for b in range(2, bmax + 1)
            for am in range(0, b) for ap in range(0, b)
            if am + ap + 1 - b >= 1]


# ------------------------------------------------------------------ main

def run_family(name, exps, bmax, T, expect_rounds=None):
    """One monomial over the census: at each representable cell print
    the law's c*, the certificate depth at c* - 1 and the survival at
    c*. Returns rows (b, am, ap, cstar, cert, sdepth, survive_at_cstar)."""
    d = sum(exps)
    rows = []
    print(f"\n=== {name}: exponents {exps}, degree {d}, radices 2..{bmax}")
    print("  cell (b,am,ap) rho | c* | cert at c*-1 [depth searched] | "
          "survives search at c* [depth]")
    for (b, am, ap) in census(bmax):
        if not representable(b, am, ap, exps):
            continue
        rho = am + ap + 1 - b
        cstar = monomial_law(b, am, ap, d)
        cert, sdepth = (None, 0)
        if cstar >= 1:
            cert, sdepth = KGame(b, am, ap, cstar - 1, exps).certificate_depth(T)
        surv, sdepth2 = KGame(b, am, ap, cstar, exps).certificate_depth(T, budget=SURVIVAL_BUDGET)
        ok(surv is None, f"K2 certificate at the law's c*={cstar} on {name} ({b},{am},{ap}) "
                          f"after {surv} rounds")
        if cstar >= 1:
            if cert is None:
                print(f"  K3 survives to depth {sdepth} at c*-1 on {name} ({b},{am},{ap})")
            elif expect_rounds is not None:
                ok(cert <= expect_rounds, f"K1 {name} ({b},{am},{ap}) certified only at "
                                          f"round {cert} > {expect_rounds}")
        print(f"  ({b},{am},{ap}) rho={rho} | c*={cstar} | "
              f"{'-' if cstar == 0 else (cert if cert is not None else 'survives')} "
              f"[{sdepth}] | {'yes' if surv is None else 'NO'} [{sdepth2}]")
        rows.append((b, am, ap, cstar, cert, sdepth, surv is None))
    ncert = sum(1 for r in rows if r[3] >= 1 and r[4] is not None)
    nopen = sum(1 for r in rows if r[3] >= 1 and r[4] is None)
    print(f"  {name}: {len(rows)} representable cells; c* >= 1 at "
          f"{ncert + nopen}, certified {ncert}, surviving the search {nopen}; "
          f"survives at c* at {sum(1 for r in rows if r[6])}/{len(rows)}")
    return rows


def main():
    T = 12
    b1 = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    b2 = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    b3 = int(sys.argv[3]) if len(sys.argv) > 3 else 3   # the three-stream tree is 343-ary at radix 4
    t0 = time.time()

    print("=== P-A: the control, x y through the k-stream engine")
    ctrl = run_family("x y", (1, 1), b2, T, expect_rounds=2)

    print("\n=== P-B: the affine control, the identity x at c = 0")
    for (b, am, ap) in census(b1):
        cstar = monomial_law(b, am, ap, 1)
        surv, sd = KGame(b, am, ap, 0, (1,)).certificate_depth(T, budget=SURVIVAL_BUDGET)
        ok(surv is None, f"K4 identity certified failing at c=0 on ({b},{am},{ap})")
        print(f"  ({b},{am},{ap}) margin law c*={cstar} | identity at c=0: "
              f"{'survives' if surv is None else 'NO'} [{sd}]")
    print("  identity survives c = 0 at every cell; margin law c* >= 1 at "
          f"{sum(1 for c in census(b1) if monomial_law(*c, 1) >= 1)}/{len(census(b1))}")

    if FAILURES:
        print("\nPOSITIVE CONTROL FAILED; nothing below is read")
        for f in FAILURES:
            print("  ", f)
        return

    print("\n=== P-C: x^2")
    sq = run_family("x^2", (2,), b1, T)
    ctrl_d = {(r[0], r[1], r[2]): r for r in ctrl}
    deeper, same, shallower = 0, 0, 0
    for r in sq:
        key = r[:3]
        if r[3] >= 1 and r[4] is not None and key in ctrl_d and ctrl_d[key][4] is not None:
            if r[4] > ctrl_d[key][4]:
                deeper += 1
            elif r[4] == ctrl_d[key][4]:
                same += 1
            else:
                shallower += 1
    print(f"  x^2 against x y, certificate depth at c*-1 on shared cells: "
          f"deeper {deeper}, same {same}, shallower {shallower}")
    ok(shallower == 0, "P-C: x^2 certified shallower than x y at some cell")

    print("\n=== P-D, P-E: degree 3 in three shapes")
    cube = run_family("x^3", (3,), b1, T)
    sqy = run_family("x^2 y", (2, 1), b2, T)
    xyz = run_family("x y z", (1, 1, 1), b3, T, expect_rounds=None)
    by = {}
    for name, rows in (("x^3", cube), ("x^2 y", sqy), ("x y z", xyz)):
        for r in rows:
            by.setdefault(r[:3], {})[name] = r
    agree, disagree, cells = 0, 0, 0
    for key, m in sorted(by.items()):
        if len(m) < 2:
            continue
        cells += 1
        floors = {name: (r[3] if r[4] is not None else None) for name, r in m.items()}
        certified = {name: f for name, f in floors.items() if f is not None}
        if len(set(certified.values())) <= 1:
            agree += 1
        else:
            disagree += 1
            print(f"  P-E floors disagree at {key}: {certified}")
    print(f"  degree-3 shapes on shared cells: {cells} cells, certified floors "
          f"agree at {agree}, disagree at {disagree}")
    ok(disagree == 0, "P-E: certified floors disagree across degree-3 shapes")

    print(f"\nwall {time.time()-t0:.1f}s; failures: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)


if __name__ == "__main__":
    main()
