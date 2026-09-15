"""The lookahead table: an on-line unit's delay read off two numbers of
its map -- the box width rate and its range's top -- tabulated by
operand range for the field's units, with the chain, the Pisot-base
and the gap-set columns beside it.

THE QUESTION. The delay of an on-line unit -- how many input digits a
most-significant-first reader must see past the output digit it emits
-- is derived unit by unit in the hardware literature: one derivation
for the multiplier, another for the square root, another for the
divider, each from the unit's own selection rule. The margin law reads
all of them from one inequality: for a C^2 map of any number of
streams over the window [-M-, M+]^d, M+- = a+-/(b - 1), not affine on
the window, the delay is exactly the least L with

    b^L rho >= Lam (a- + a+),

Lam the BOX WIDTH RATE (the sup over the window of the gradient's L1
norm), rho = a- + a+ + 1 - b the digit set's slack, the lookahead c* =
L* - o with o the LEAD, the least integer with the range inside the
root cell [-M- b^o, M+ b^o] (explore_manystream_delay.py). So a unit's
delay is a function of two numbers of its map, Lam and its range's
ends, and this file is the table: the closed forms unit_c-style for
the product, the multiply-add, x^2 + y, the reciprocal, the square
root and the divider, at every contiguous digit set of radices 2..5
and, for the pole units, at a pole distance P handed in. Beside it
three columns the same laws give: THE LEAD LAW, that c* sits within one
digit of log_b(Lam M+ (a- + a+) / (G rho)), G the range's top, so the
map enters only through its relative gradient Lam/G
(explore_lead_law.py); THE CHAIN COLUMN, the escape law's floor for a
unit feeding a consumer and the threshold-miss law at slack 1
(explore_chain_delay.py, explore_threshold_miss.py); THE PISOT COLUMN,
the law in a base beta with the level walk as its certifier
(explore_beta_delay.py, explore_covering_lag.py); and THE GAP-SET
COLUMN, the generalized law over a digit set with a gap with the
confined tree as its certifier (explore_gap_lattice.py,
explore_beta_delay.py). Nothing here is a new measurement: every entry
is a closed form or a certifier the cited scripts already run, brought
to one front.

THE DESIGN. A unit is (name, Lam, lo, hi): the box width rate and the
range's ends over the window, exact rationals except the root's, whose
forms are squared. The lead is the least o with lo >= -M- b^o and
hi <= M+ b^o; L* the least L with b^L rho >= Lam (a- + a+); both are
ceilings of logarithms of rationals taken exactly. The six units:
  product x y:          Lam = 2 Mh,     range [-M- M+, Mh^2]
  multiply-add x y + z: Lam = 2 Mh + 1, range [-M- M+ - M-, Mh^2 + M+]
  x^2 + y:              Lam = 2 Mh + 1, range [-M-, Mh^2 + M+]
  reciprocal 1/(s + x): Lam = 1/P^2,    range [1/(P + w), 1/P]
  root sqrt(s + x):     Lam = 1/(2 sqrt P), range [sqrt P, sqrt(P + w)]
  divider x/(s + y):    Lam = (P + Mh)/P^2, range [-M-/P, M+/P]
with Mh = max(M-, M+), w = M- + M+, s = M- + P, P > 0 the pole
distance (the operand's distance from the pole, which the field's
operand normalisation fixes). THE CHAIN COLUMN at a cell: the aligned
adder (x y) + z by the escape law (chain_floor), the product consumer
(x y) z and the sum-fed consumer z (x + y) by the escape law's search
and, at slack 1, the threshold-miss law; a row prints the naive sum of
the two units' floors, the law's floor and whether the chain gains.
THE PISOT COLUMN: the law beta^L (w - 1) >= Lam w in the base, the
lead the least o with the range inside the root cell, at the five
Pisot units of the record (golden, Narayana, silver, tribonacci,
plastic) over {-a..a}; the certifier is the level walk at L* - 1, the
forced reader's kill round. THE GAP-SET COLUMN: b^L z_min >= Lam w
with z_min the least overlap zone of the set's cells; the certifier is
the confined tree at L* - 1.

THE SLATE, frozen before the engine.

P-A THE CONTROL. The closed forms agree with the engines' integer
    loops (explore_manystream_delay.py least_lead and law_L for the
    product, the multiply-add, x^2 + y and the divider;
    explore_onestream_delay.py's for the reciprocal and the root) at
    every one of the 20 cells of radices 2..5, at P in {1/(b - 1), 1,
    8/(b - 1)} for the pole units: 20 + 20 + 20 + 3 x 20 x 3 = 240
    pairs, 240 agreements.
P-B THE TABLE. At the 20 cells: c* of the product is 1 or 2 (2 at
    radix 2 and at the slack-1 cells of radix 3, the record's census);
    the multiply-add and x^2 + y read one lookahead above the product
    at (2,1,1) and level with it elsewhere; the reciprocal and the root
    at P = 8/(b - 1) read below their P = 1/(b - 1) value; the divider
    reads c* in {0, 1, 2} at every P (a property). The lead law's band
    |c* - log_b(Lam M+ wsum/(G rho))| < 1 at every row.
P-C THE CHAIN. At radices 2..5 the aligned adder (x y) + z gains
    nowhere (the chain's floor is L1* + L2* at all 20 cells); the
    product consumer (x y) z gains at (4,2,2) alone; the sum-fed
    consumer z (x + y) gains at (5,2,3) and (5,3,2) alone; at every
    slack-1 cell the search's verdict equals the threshold-miss law's.
P-D THE PISOT COLUMN. At a = 1: golden x y L* = 4 at o = 1, the golden
    divider 3 at 0, Narayana x y 5 at 2, the Narayana divider 4 at 0
    (the record); the level walk at L* - 1 kills golden x y at round 5
    and the golden divider at round 4.
P-E THE GAP-SET COLUMN. At radix 3 over {-3, -1, 0, 1, 2}: x y has
    L* = 3 by the generalized law and the confined tree at L = 2 kills
    at round 4; over {-3, -2, -1, 0, 2} the divider at P = 1/2 has
    L* = 4 and the confined tree at L = 3 kills at round 4 (the record).

KILLS, frozen as what this rig PRINTS.

K1 A closed form differing from an engine loop at any pair -> the
   table is not the engines'; nothing below is read.
K2 The lead law's band violated at any row -> the column is wrong.
K3 A chain verdict differing from the threshold-miss law's at a slack-1
   cell, or a gain set differing from the record's.
K4 A certifier's round differing from the record's at any of the four
   certified pairs.

POSITIVE CONTROL: P-A, read before any other line.

FINDINGS (entered after the run; every number below sits in this
file's printed output at BMAX = 5).

F1 THE CONTROL HOLDS. 243 of 243 pairs agree with the engines' loops;
   the slate's 240 miscounted radix 2, where the pole distances
   1/(b - 1) and 1 coincide and the three polynomial units are
   compared at both. K1 never fired.
F2 THE TABLE [property; the print its check]. The product's c* is 2 at
   9 cells, 1 at 10 and 0 at (5,4,3) (o = 1, L* = 1): the slate's "1 or
   2", carried over from the pole sweep's census, fails at one cell.
   The multiply-add and x^2 + y print identical rows at all 20 cells,
   (o, L*, c*) = (1, 3, 2) at (2,1,1) and (1, 2, 1) elsewhere: against
   the product their L* is one above at (2,1,1) and at the five cells
   where the product's L* is 1, level at the other 14, and their
   lookahead is equal at 11 cells, one below the product's at 8 (the
   lead 1 against 0) and one above at (5,4,3). The reciprocal's c* at
   P = 8/(b - 1) sits 0 to 3 below its value at P = 1/(b - 1) (3 at
   (2,1,1), 0 at (5,2,3) and (5,3,2)), the root's 0 to 2 below; the
   divider reads c* = 2 at P = 1/(b - 1) at all 20 cells and 1 at
   P = 8/(b - 1) at 19, 2 at (2,1,1). The lead law's band holds at all
   180 rows, greatest deviation 0.89 at (5,2,4), the product. K2 never
   fired.
F3 THE CHAIN [rule at radices 2..5 by the closed forms]. The aligned
   adder gains at no cell (floor = naive at 20 of 20); (x y) z gains at
   (4,2,2) alone, 3 against the naive 4; z (x + y) at (5,2,3) and
   (5,3,2) alone, 3 against 4; the search's verdict equals the law's at
   all 13 slack-1 rows (6 product-fed, 7 sum-fed). K3 never fired.
F4 THE PISOT COLUMN. The record's four values reprint (golden x y
   (4, 1, 3), divider (3, 0, 3); Narayana x y (5, 2, 3), divider
   (4, 0, 4)), with silver x y (2, 0, 2), x^2 + y (3, 1, 2), divider
   (2, 0, 2); tribonacci (3, 1, 2), (3, 2, 1), (3, 0, 3); plastic
   (8, 4, 4), (8, 5, 3), (6, 0, 6). The level walk at L* - 1 kills
   golden x y at round 5 (1,976 boxes, the record's count, 0.2 s) and
   the golden divider at round 4 (950 boxes, 0.1 s). K4 never fired.
   The first run of this rig walked past the kill to the round cap
   (362,177 boxes, 31.5 s at golden x y); the walk gained a stop at
   its first dead round and the run was repeated, no verdict changed.
F5 THE GAP-SET COLUMN. x y over {-3, -1, 0, 1, 2} at radix 3: L* = 3,
   o = 1, z_min = 1/2, the confined tree at L = 2 dead at round 4
   (36,539 nodes, 0.2 s); the divider at P = 1/2 over {-3, -2, -1, 0,
   2}: L* = 4, o = 1, dead at L = 3 at round 4 (36,708 nodes, 0.3 s),
   both the record's rounds and node counts. K4 never fired.

VERDICT. Six units, one inequality, one front: the table reprints the
field's per-unit delays from Lam and the range's ends and adds what
the per-unit derivations never state -- the lead, the lookahead's
sign and its band, the chain's gain cells, and the delay in a base
that is not an integer or over a digit set with a gap, each with the
certifier that decides it below the law.

RUN RECORD: pure Python, exact rationals in every ceiling; the shipped
engines imported for the control and the two certifiers; under
memwatch, peak commit 73.7 MB against the 512 MB default, wall 1.0 s.
Run: python prime/code/explore_lookahead_table.py [BMAX]
"""

import os
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_manystream_delay as ms                      # noqa: E402
import explore_onestream_delay as os1                      # noqa: E402
import explore_chain_delay as cd                           # noqa: E402
import explore_threshold_miss as tm                        # noqa: E402
import explore_beta_delay as bd                            # noqa: E402
import explore_delay_sweep as ds                           # noqa: E402
import explore_gap_lattice as gl                           # noqa: E402
import explore_covering_lag as cl                          # noqa: E402

FAILURES = []


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print("  KILL:", msg)


# ------------------------------------------------------------ closed forms

def ceil_log(b, q):
    """ceil(log_b q) for a positive rational q, exactly."""
    k = 0
    while Fr(b) ** k < q:
        k += 1
    while Fr(b) ** (k - 1) >= q:
        k -= 1
    return k


def ceil_log_sq(b, r):
    """Least k with b^(2k) >= r, r a positive rational: ceil(log_b sqrt r)."""
    k = 0
    while Fr(b) ** (2 * k) < r:
        k += 1
    while Fr(b) ** (2 * (k - 1)) >= r:
        k -= 1
    return k


def params(b, am, ap):
    """(M-, M+, Mh, wsum, rho) of the digit set {-am, ..., ap} at radix b."""
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    return Mm, Mp, max(Mm, Mp), am + ap, am + ap + 1 - b


class Unit:
    """An on-line unit as the two numbers the law reads: its box width
    rate `lam` and its range [lo, hi] over the window. `sq` marks a unit
    whose forms are squared (the root): then lam2 = Lam^2, lo2 = lo^2,
    hi2 = hi^2 and lo > 0."""

    def __init__(self, name, lam, lo, hi, sq=False):
        self.name, self.lam, self.lo, self.hi, self.sq = name, lam, lo, hi, sq

    def lead(self, b, am, ap):
        """The least o with the range inside [-M- b^o, M+ b^o]."""
        Mm, Mp, Mh, wsum, rho = params(b, am, ap)
        if self.sq:
            return ceil_log_sq(b, self.hi / (Mp * Mp))
        top = self.hi / Mp
        if self.lo < 0:
            top = max(top, -self.lo / Mm)
        return ceil_log(b, top)

    def L(self, b, am, ap):
        """The least L with b^L rho >= Lam wsum."""
        Mm, Mp, Mh, wsum, rho = params(b, am, ap)
        if self.sq:
            return ceil_log_sq(b, self.lam * wsum * wsum / (rho * rho))
        return ceil_log(b, self.lam * wsum / rho)

    def gamma(self):
        """The relative gradient Lam / G, G the range's top, as a float."""
        if self.sq:
            return (float(self.lam) / float(self.hi)) ** 0.5
        return float(self.lam) / float(self.hi)


def units(b, am, ap, P):
    """The six units at the cell, the pole units at pole distance P."""
    Mm, Mp, Mh, wsum, rho = params(b, am, ap)
    P = Fr(P)
    w = Mm + Mp
    return [
        Unit("x y", 2 * Mh, -Mm * Mp, Mh * Mh),
        Unit("x y + z", 2 * Mh + 1, -Mm * Mp - Mm, Mh * Mh + Mp),
        Unit("x^2 + y", 2 * Mh + 1, -Mm, Mh * Mh + Mp),
        Unit("1/(s+x)", 1 / (P * P), 1 / (P + w), 1 / P),
        Unit("sqrt(s+x)", 1 / (4 * P), P, P + w, sq=True),
        Unit("x/(s+y)", (P + Mh) / (P * P), -Mm / P, Mp / P),
    ]


def unit_row(b, am, ap, u):
    """(o, L*, c*, the lead law's value) of one unit at one cell."""
    import math
    Mm, Mp, Mh, wsum, rho = params(b, am, ap)
    o, L = u.lead(b, am, ap), u.L(b, am, ap)
    law = math.log(u.gamma() * float(Mp * wsum / rho)) / math.log(b)
    return o, L, L - o, law


def table(b, am, ap, P):
    """The six rows at one cell: name -> (o, L*, c*, law value)."""
    return {u.name: unit_row(b, am, ap, u) for u in units(b, am, ap, P)}


def census(bmax):
    return [(b, am, ap) for b in range(2, bmax + 1)
            for am in range(0, b) for ap in range(0, b)
            if am + ap + 1 - b >= 1]


# ------------------------------------------------------------- the chain

def chain_rows(b, am, ap):
    """The chain column at a cell: name -> (naive, floor, gain, law) for
    the aligned adder (x y) + z, the product consumer (x y) z and the
    sum-fed consumer z (x + y); `law` is the threshold-miss law's
    verdict at a slack-1 cell and None elsewhere; a consumer whose
    range does not fit the cell is absent."""
    rho = am + ap + 1 - b
    out = {}
    Mm, Mp, w, Mh = cd.window(b, am, ap)
    L1s = cd.margin_L(b, am, ap, 2 * Mh)
    L2s = cd.sum_law(b, am, ap)
    best = cd.chain_floor(b, am, ap)
    out["(x y) + z"] = (L1s + L2s, best[0], best[0] < L1s + L2s, None)
    for name, u in (("(x y) z", tm.ProductFed(b, am, ap)),
                    ("z (x + y)", tm.SumFed(b, am, ap, lattice=True))):
        if not u.representable:
            continue
        naive, L2s_u, best_u = tm.gain(u)
        got = best_u is not None and best_u[0] < naive
        out[name] = (naive, best_u[0] if best_u else None, got,
                     tm.law_gain(u) if rho == 1 else None)
    return out


# ------------------------------------------------------- the Pisot column

def beta_base(name):
    for B in ds.beta_bases():
        if B.name.startswith(name):
            return B
    raise KeyError(name)


def beta_row(B, fmap, a=1):
    """(L*, o, c*) of a map in base beta over {-a..a}, by the law."""
    L = bd.law_L(B, fmap, a)[0]
    o = bd.least_lead(B, fmap, a)
    return L, o, L - o


def certify_beta(B, fmap, a=1, max_round=8, cap=300_000, wall=60.0):
    """The level walk at L* - 1: (kill round or None, boxes walked,
    round reached). The forced reader's death round, the record's
    certificate round at 22 of 23 decided pairs."""
    L, o, c = beta_row(B, fmap, a)
    wk = cl.Walk(B, fmap, c - 1, o, a=a)
    rounds, r_open, reached, total = wk.walk(max_round, cap, wall, stop_dead=True)
    r = next((x['r'] for x in rounds if x['dead'] > 0), None)
    return r, total, reached


# ----------------------------------------------------- the gap-set column

def gap_row(b, D, fmap):
    """(L* by the generalized law or None at a touching set, o, z_min)."""
    interval, w, gmax, zmin = gl.tail_verdict(b, D)
    L = gl.law_gen(b, D, fmap)
    o = ms.least_lead(b, -min(D), max(D), fmap)
    return L, o, zmin


def certify_gap(b, D, fmap, L, budget=3_000_000, wall=240.0):
    """The confined tree at lookahead L - o: (kill round or None, the
    round reached, nodes)."""
    o = ms.least_lead(b, -min(D), max(D), fmap)
    rd = bd.ConfinedGap(b, D, L - o, fmap, o)
    r, depth = rd.certificate(budget, wall=wall)
    return r, depth, rd.nodes


# -------------------------------------------------------------------- runs

def control(bmax):
    print("\n=== P-A THE CONTROL: the closed forms against the engines' loops")
    agree = tot = 0
    for (b, am, ap) in census(bmax):
        Mm, Mp, Mh, wsum, rho = params(b, am, ap)
        for j in (Fr(1, b - 1), Fr(1), Fr(8, b - 1)):
            P = Fr(j)
            us = {u.name: u for u in units(b, am, ap, P)}
            pairs = [("x/(s+y)", ms.Division(b, am, ap, P), ms)]
            if j == Fr(1, b - 1):
                pairs += [("x y", ms.Product(b, am, ap), ms),
                          ("x y + z", ms.MulAdd(b, am, ap), ms),
                          ("x^2 + y", ms.SquarePlus(b, am, ap), ms)]
            s = Mm + P
            pairs += [("1/(s+x)", os1.Recip(s.numerator, s.denominator, P), os1),
                      ("sqrt(s+x)", os1.Root(s.numerator, s.denominator, P), os1)]
            for name, fmap, eng in pairs:
                u = us[name]
                o, L = u.lead(b, am, ap), u.L(b, am, ap)
                oe, Le = eng.least_lead(b, am, ap, fmap), eng.law_L(b, am, ap, fmap)
                tot += 1
                good = (o, L) == (oe, Le)
                agree += good
                ok(good, f"K1 ({b},{am},{ap}) P={P} {name}: closed (o,L*)=({o},{L}), engine ({oe},{Le})")
    print(f"  {agree} of {tot} pairs agree")


def print_table(bmax, Ps=(None, None)):
    """P-B: the table at radices 2..bmax, the pole units at two pole
    distances P1 = 1/(b - 1) and P2 = 8/(b - 1) by default."""
    print(f"\n=== P-B THE TABLE, radices 2..{bmax}: per unit (o, L*, c*); the pole units at "
          "P1 = 1/(b-1) and P2 = 8/(b-1); the lead law's value in brackets")
    print("  cell      | x y       | x y + z   | x^2 + y   | 1/(s+x) P1     P2      | sqrt(s+x) P1   P2      | x/(s+y) P1     P2")
    worst = (0.0, None)
    rows = 0
    for (b, am, ap) in census(bmax):
        P1, P2 = (Fr(1, b - 1), Fr(8, b - 1)) if Ps == (None, None) else (Fr(Ps[0]), Fr(Ps[1]))
        t1, t2 = table(b, am, ap, P1), table(b, am, ap, P2)

        def cell(t, name):
            o, L, c, law = t[name]
            return f"{o:+d} {L:+d} {c:+d} [{law:+.2f}]", abs(c - law)
        parts, devs = [], []
        for name in ("x y", "x y + z", "x^2 + y"):
            s, d = cell(t1, name)
            parts.append(s)
            devs.append((d, name, 1))
        for name in ("1/(s+x)", "sqrt(s+x)", "x/(s+y)"):
            s1, d1 = cell(t1, name)
            s2, d2 = cell(t2, name)
            parts.append(f"{s1} {s2}")
            devs += [(d1, name, 1), (d2, name, 2)]
        print(f"  ({b},{am},{ap}) rho={am + ap + 1 - b} | " + " | ".join(parts))
        for d, name, which in devs:
            rows += 1
            ok(d < 1, f"K2 ({b},{am},{ap}) {name} P{which}: c* off the lead law by {d:.3f}")
            if d > worst[0]:
                worst = (d, (b, am, ap, name, which))
    print(f"  {rows} rows; the band's greatest deviation {worst[0]:.2f} at {worst[1]}")
    return worst


def print_chain(bmax):
    print(f"\n=== P-C THE CHAIN COLUMN, radices 2..{bmax}: naive L1* + L2* -> the escape law's floor; * marks a gain")
    gains = {}
    checked = 0
    for (b, am, ap) in census(bmax):
        rows = chain_rows(b, am, ap)
        rho = am + ap + 1 - b
        parts = []
        for name in ("(x y) + z", "(x y) z", "z (x + y)"):
            if name not in rows:
                parts.append(f"{name}: -")
                continue
            naive, floor, gain, law = rows[name]
            parts.append(f"{name}: {naive} -> {floor}{'*' if gain else ''}")
            if gain:
                gains.setdefault(name, []).append((b, am, ap))
            if law is not None:
                checked += 1
                ok(gain == law, f"K3 ({b},{am},{ap}) {name}: search {gain}, law {law}")
        print(f"  ({b},{am},{ap}) rho={rho} | " + " | ".join(parts))
    print(f"  gains: {gains}; the law checked at {checked} slack-1 rows")
    # the record's gain cells within the radices swept
    want_p = [c for c in [(4, 2, 2)] if c[0] <= bmax]
    want_s = [c for c in [(5, 2, 3), (5, 3, 2)] if c[0] <= bmax]
    ok(gains.get("(x y) + z") is None, "K3 the aligned adder gains somewhere")
    ok(gains.get("(x y) z", []) == want_p, f"K3 (x y) z gains at {gains.get('(x y) z')}")
    ok(gains.get("z (x + y)", []) == want_s, f"K3 z (x + y) gains at {gains.get('z (x + y)')}")


def print_beta():
    print("\n=== P-D THE PISOT COLUMN at a = 1: (L*, o, c*) by the law in the base; the level walk at L* - 1")
    record = {("golden", "x y"): (4, 1), ("golden", "x / (s + y)"): (3, 0),
              ("Narayana", "x y"): (5, 2), ("Narayana", "x / (s + y)"): (4, 0)}
    for B in ds.beta_bases():
        parts = []
        for fmap in ds.beta_maps(B, 1):
            L, o, c = beta_row(B, fmap, 1)
            parts.append(f"{fmap.name}: ({L}, {o}, {c})")
            key = (B.name.split()[0], fmap.name)
            if key in record:
                ok((L, o) == record[key], f"K4 {B.name} {fmap.name}: ({L}, {o}) against the record's {record[key]}")
        print(f"  {B.name}: " + " | ".join(parts))
    Bg = beta_base("golden")
    for fmap, want in ((bd.BProduct(Bg), 5), (bd.BDivision(Bg, 1, 1, 1), 4)):
        t1 = time.time()
        r, boxes, reached = certify_beta(Bg, fmap, 1)
        print(f"  the walk at L* - 1, golden {fmap.name}: kill round {r} ({boxes} boxes to round {reached}, "
              f"{time.time() - t1:.1f}s)")
        ok(r == want, f"K4 golden {fmap.name}: the walk kills at {r}, the record's {want}")


def print_gap():
    print("\n=== P-E THE GAP-SET COLUMN at radix 3: (L*, o, z_min) by the generalized law; the confined tree at L* - 1")
    b = 3
    runs = [((-3, -1, 0, 1, 2), ms.Product(3, 3, 2), 3, 4),
            ((-3, -2, -1, 0, 2), ms.Division(3, 3, 2, Fr(1, 2)), 4, 4)]
    for D, fmap, wantL, wantr in runs:
        L, o, zmin = gap_row(b, D, fmap)
        ok(L == wantL, f"K4 radix 3 {list(D)} {fmap.name}: L* = {L}, the record's {wantL}")
        t1 = time.time()
        r, depth, nodes = certify_gap(b, D, fmap, L - 1)
        print(f"  {list(D)} {fmap.name}: L* = {L}, o = {o}, z_min = {zmin}; the confined tree at L = {L - 1}: "
              f"kill round {r} [{depth}] ({nodes} nodes, {time.time() - t1:.1f}s)")
        ok(r == wantr, f"K4 radix 3 {list(D)} {fmap.name}: the tree kills at {r}, the record's {wantr}")


def main():
    bmax = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    t0 = time.time()
    print(f"THE LOOKAHEAD TABLE: {len(census(bmax))} cells of radices 2..{bmax}")
    control(bmax)
    if FAILURES:
        print("  CONTROL FAILED; nothing below is read.")
        return
    print_table(bmax)
    print_chain(bmax)
    print_beta()
    print_gap()
    print("\n=== VERDICT")
    print("  " + ("the table is the engines' at every pair, the band holds, the chain's gain cells and the "
                  "certifiers' rounds are the record's" if not FAILURES
                  else f"{len(FAILURES)} kill(s) fired"))
    print(f"\n{len(FAILURES)} failures; wall {time.time() - t0:.1f} s")


if __name__ == "__main__":
    main()
