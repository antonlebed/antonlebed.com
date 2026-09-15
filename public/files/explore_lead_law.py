"""The lead law: is a unit's lookahead bounded below because a stream
is MULTIPLIED (the dependency structure), or because the map's relative
gradient is, whatever the structure?

THE QUESTION. The divider x/(s + y) never emits before it reads (its
lookahead c* = L* - o is at least 0 at every pole distance), while the
reciprocal 1/(s + y) and the square root run ahead without bound as the
pole deepens (explore_divider_lookahead.py). The recorded reason is the
numerator: a unit that multiplies a stream by a function of the others
has that stream's partial equal to the function, of the range's own
order, so its lookahead cannot fall. The hypothesis under test is the
CONVERSE: that a unit with no multiplied stream -- any g(y) of one
stream -- runs ahead by its pole depth, so that a datapath's lead
budget reads off which nodes multiply a stream and nothing else. If a
one-stream unit exists whose lookahead stays bounded below, and rises,
as its parameter deepens, the lead budget is not a function of the
dependency structure.

THE DERIVATION, written before the engine. Both halves of c* are closed
forms of two numbers of the map: Lam, the box width rate (the sup over
the window of the gradient's L1 norm), and G, the range's top (the
range [-M- G/M+, G]). With wsum = a- + a+ and rho = wsum + 1 - b,
L* = ceil(log_b(Lam wsum / rho)) and o = ceil(log_b(G / M+)), so

    c* - log_b(Gamma M+ wsum / rho)  lies in (-1, 1),   Gamma = Lam / G,

THE LEAD LAW: within one digit, the lookahead is the log of the map's
RELATIVE GRADIENT Gamma, the width of its image per unit of its range,
and nothing else of the map enters. A unit runs ahead without bound
exactly when Gamma falls to 0 along its family. For a multiplied stream
x g(y): Lam >= sup g = G / M+, so Gamma >= 1/M+ and c* > log_b(wsum/rho)
- 1 >= 0: the recorded property, one line. For the pole units of one
stream: 1/(s + y)^k has Gamma = k/P, sqrt(s + y) has
Gamma = 1/(2 sqrt(P (P + w))), both falling as 1/P. For exp(-P y) over
y in [-M-, M+], one stream and no product: G = e^{P M-},
Lam = P e^{P M-}, so Gamma = P, RISING with the parameter, and c* rises
like log_b P with no floor to run ahead of. The converse is false by
one specimen, and the "carrier" of the hypothesis -- a stream whose
partial's sup is of the range's own order -- is, by that definition,
exactly a stream along which Gamma is bounded below: the hypothesis's
if-clause is the lead law renamed, and its then-clause (the dependency
structure) is what exp(-P y) tests.

THE CHAIN, the second hypothesis this rig reads. A reciprocal that
emits c1* < 0 digits before it reads feeds a product consumer that
reads at the least c with (R_m + Mh b^{c1*}) w <= b^c (w - 1), R_m in
(M+/b, M+] the stream's top in cell units (explore_chain_recip.py). The
need is above R_m w > (M+/b) w, so b^c > (M+/b)(wsum/rho) >= 1/b, and
c >= 0: the product never emits before it reads z, its output is an
ordinary digit stream, and a third unit reading it and a fresh stream
sees two ordinary streams whatever the first unit's lead -- the depth
gain is spent in one hop, by the closed form.

THE SLATE, frozen before the engine. Radices 2..5, the 20 cells with
rho >= 1; P = j/(b - 1), j in {1, 2, 4, 8, 32, 128, 1024, 8192}.

P-A THE CONTROL. explore_divider_lookahead.py's divider_c at its 40
    deep pairs (j = 32, 128) reprints its F2 multiset: c* = 0 at 5
    pairs, 1 at 33, 2 at 2.
P-B THE LEAD LAW. |c* - log_b(Gamma M+ wsum/rho)| < 1 at every pair
    of every family below (property; the print its check).
P-C THE SPECIMEN. exp(-P y): c* at j = 8192 exceeds c* at j = 1 at
    every cell by at least floor(log_b 8192) - 1, and no c* over the
    sweep sits below the j = 1 value minus 1.
P-D THE POLE UNITS. 1/(s + y), 1/(s + y)^2, sqrt(s + y): c* at
    j = 8192 sits below c* at j = 1 at every cell by at least
    floor(log_b 8192) - 2 (the reciprocals) and floor(log_b 8192)/2 - 2
    (the root).
P-E THE MULTIPLIED STREAMS. x/(s + y) and x exp(-P y): c* >= 0 at
    every pair (property, Gamma >= 1/M+).
P-F THE CHAIN. c2 >= 0 at every pole pair where the reciprocal leads
    (explore_chain_product.py pole_pairs, 40 at radices 2..5).

KILLS, frozen as what this rig PRINTS.

K1 P-A's multiset differs from (5, 33, 2) -> the imported forms are
   not the record's; nothing below is read.
K2 The lead law's band violated at any pair -> the derivation is wrong.
K3 THE HYPOTHESIS'S OWN KILL: exp(-P y)'s c* at j = 8192 at or below
   its value at j = 1 at any cell -> a one-stream unit runs ahead as
   its parameter deepens and the converse survives that cell. c*
   rising at every cell -> the converse is killed: a unit with no
   multiplied stream and a bounded-below lookahead exists.
K4 c2 < 0 at any pole pair -> the product leads its third unit and the
   three-unit chain must be run; c2 >= 0 at all 40 -> the lead is
   spent in one hop.

POSITIVE CONTROL: P-A, read before any other line.

FINDINGS (entered after the run; every number below is in this file's
print).

F1 THE CONTROL HOLDS. The 40 deep pairs reprint c* = 0 at 5, 1 at 33,
   2 at 2. K1 never fired.
F2 THE LEAD LAW [property; the print its check]. The band holds at
   every pair of the six families: the greatest deviation is 0.924
   (exp), 0.876 and 0.893 (the reciprocals), 0.999 (the root), 1.000
   (the divider, a rounding of a near-tie: an exact 1 is impossible,
   since a tie in either ceiling puts the difference in a half-open
   interval short of 1) and 0.952 (x exp). K2 never fired. The first
   run of this rig fired K2 at the two multiplied-stream families by
   up to 1.689 because their gamma values in the code had dropped the
   1/M+ the derivation carries; the forms were corrected and the run
   repeated, no prediction changed.
F3 THE SPECIMEN. exp(-P y) rises at every cell: c* from 1 to 14 at
   (2,1,1), from -1 to 8 at (3,2,1), from -1 to 5 at the radix-5 cells;
   the rise is 13 at radix 2, 8 or 9 at radix 3, 6 or 7 at radix 4,
   5 or 6 at radix 5, every one at or above floor(log_b 8192) - 1;
   the least c* over the sweep is the j = 1 value at every cell (-1 at
   eight cells, 0 at eleven, 1 at (2,1,1)). K3 never fired: THE
   CONVERSE IS KILLED.
F4 THE POLE UNITS fall at every cell: 1/(s + y) by 5 to 13,
   1/(s + y)^2 by 5 to 13, sqrt(s + y) by 4 to 12.
F5 THE MULTIPLIED STREAMS: least c* 0 at both x/(s + y) (greatest 2)
   and x exp(-P y) (greatest 14).
F6 THE CHAIN. c2 in {0, 1, 2} at the 40 leading pairs, least 0. K4
   never fired.

VERDICT. A unit's lookahead is, within one digit, the log of its
relative gradient Lam/G, and the dependency structure is not the
variable: exp(-P y), one stream and no product, has a lookahead that
rises with P at all 20 cells, while the pole units fall. The converse
hypothesis is dead; what stands is the lead law, the divider's
property as its one-line corollary. A product fed by a leading
reciprocal never emits before it reads (c2 >= 0 at all 40 pairs), so
its output is an ordinary stream and a lead is spent in one hop.

RUN RECORD: pure Python, exact rationals in every ceiling but the
exponential's, which compares logs in floating point; under memwatch,
peak commit 45.3 MB against the 512 MB default, wall 0.3 s.
Run: python prime/code/explore_lead_law.py
"""

import math
import os
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_divider_lookahead as dl                     # noqa: E402
import explore_chain_product as cp                         # noqa: E402

FAILURES = []
JS = (1, 2, 4, 8, 32, 128, 1024, 8192)


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print("  KILL:", msg)


def ceil_log2(b, r):
    """Least integer k with b^(2k) >= r, r a positive rational: the
    ceiling of log_b sqrt(r), exact."""
    k = 0
    while Fr(b) ** (2 * k) < r:
        k += 1
    while Fr(b) ** (2 * (k - 1)) >= r:
        k -= 1
    return k


# ------------------------------------------------------------ the families
# each returns (o, L, c*, gamma_float): gamma = Lam / G, the relative gradient

def exp_c(b, am, ap, P):
    """g(y) = exp(-P y), y in [-M-, M+]: G = e^{P M-}, Lam = P G.
    Exact in the closed forms: the lead o is the least with G <= M+ b^o,
    L the least with b^L rho >= P G wsum -- both compare b^k against
    e^{P M-}, so the comparison is taken in logs (P M- against
    k ln b + ln M+), exact to floating precision, ties impossible off
    P M- = 0."""
    Mm, Mp, Mh, wsum, rho = dl.params(b, am, ap)
    lnG = float(P * Mm)
    o = math.ceil((lnG - math.log(Mp)) / math.log(b))
    L = math.ceil((lnG + math.log(P * wsum / rho)) / math.log(b))
    return o, L, L - o, float(P)


def recip_k(b, am, ap, P, k):
    o, L, c = dl.recip_c(b, am, ap, P, k)
    return o, L, c, float(Fr(k) / P)


def sqrt_c(b, am, ap, P):
    """sqrt(s + y), s = M- + P: range [sqrt P, sqrt(P + w)], the lead
    the least o with sqrt(P + w) <= M+ b^o, i.e. P + w <= M+^2 b^(2o);
    Lam = 1/(2 sqrt P), L the least with b^L rho >= wsum/(2 sqrt P),
    i.e. 4 b^(2L) rho^2 P >= wsum^2 (the square root's law)."""
    Mm, Mp, Mh, wsum, rho = dl.params(b, am, ap)
    w = Mm + Mp
    o = ceil_log2(b, (P + w) / (Mp * Mp))
    L = ceil_log2(b, Fr(wsum * wsum) / (4 * rho * rho * P))
    return o, L, L - o, 1 / (2 * math.sqrt(float(P * (P + w))))


def divider(b, am, ap, P):
    o, L, c = dl.divider_c(b, am, ap, P)
    Mm, Mp, Mh, wsum, rho = dl.params(b, am, ap)
    return o, L, c, float((P + Mh) / (P * Mp))


def xexp_c(b, am, ap, P):
    """x exp(-P y): d/dx = g <= G, d/dy = x g' <= Mh P G, both largest at
    y = -M-, so Lam = G (1 + Mh P); the range's top is M+ G."""
    Mm, Mp, Mh, wsum, rho = dl.params(b, am, ap)
    lnG = float(P * Mm)                     # ln sup g; the range's top is M+ sup g
    o = math.ceil(lnG / math.log(b))
    L = math.ceil((lnG + math.log((1 + Mh * P) * wsum / rho)) / math.log(b))
    return o, L, L - o, float((1 + Mh * P) / Mp)


FAMILIES = (("exp(-P y)", exp_c, "one stream, no product"),
            ("1/(s+y)", lambda b, am, ap, P: recip_k(b, am, ap, P, 1), "pole"),
            ("1/(s+y)^2", lambda b, am, ap, P: recip_k(b, am, ap, P, 2), "pole"),
            ("sqrt(s+y)", sqrt_c, "pole"),
            ("x/(s+y)", divider, "multiplied stream"),
            ("x exp(-P y)", xexp_c, "multiplied stream"))


def law_value(b, am, ap, gamma):
    Mm, Mp, Mh, wsum, rho = dl.params(b, am, ap)
    return math.log(gamma * float(Mp * wsum / rho)) / math.log(b)


def main():
    t0 = time.time()
    cells = dl.census(5)
    print(f"THE LEAD LAW: {len(cells)} cells of radices 2..5, P = j/(b-1), j in {JS}")

    print("\n=== P-A THE CONTROL: the divider's c* at the 40 deep pairs against explore_divider_lookahead.py F2")
    counts = {}
    for (b, am, ap) in cells:
        for j in (32, 128):
            c = dl.divider_c(b, am, ap, Fr(j, b - 1))[2]
            counts[c] = counts.get(c, 0) + 1
    print(f"  c* multiset: {dict(sorted(counts.items()))}")
    ok(counts == {0: 5, 1: 33, 2: 2}, f"K1 the deep-pair multiset is {counts}, not (5, 33, 2)")
    if FAILURES:
        print("  CONTROL FAILED; nothing below is read.")
        return

    print("\n=== P-B THE LEAD LAW: max |c* - log_b(Gamma M+ wsum/rho)| per family over every pair")
    table = {}
    worst = {}
    for name, fn, kind in FAMILIES:
        for (b, am, ap) in cells:
            for j in JS:
                P = Fr(j, b - 1)
                o, L, c, gamma = fn(b, am, ap, P)
                table[(name, b, am, ap, j)] = c
                dev = abs(c - law_value(b, am, ap, gamma))
                worst[name] = max(worst.get(name, 0.0), dev)
                ok(dev < 1, f"K2 {name} ({b},{am},{ap}) P={P}: c*={c} off the law by {dev:.3f}")
    for name, fn, kind in FAMILIES:
        print(f"  {name:12s} [{kind}]: max deviation {worst[name]:.3f}")

    print("\n=== P-C THE SPECIMEN exp(-P y): c* at j = 1 .. 8192 per cell (rise = c*(8192) - c*(1))")
    for (b, am, ap) in cells:
        row = [table[("exp(-P y)", b, am, ap, j)] for j in JS]
        rise = row[-1] - row[0]
        need = math.floor(math.log(8192) / math.log(b)) - 1
        print(f"  ({b},{am},{ap}): {row}  rise {rise} (>= {need})  min {min(row)}")
        ok(rise > 0, f"K3 exp(-P y) at ({b},{am},{ap}): c* {row[-1]} at j=8192 not above {row[0]} at j=1")
        ok(rise >= need, f"P-C exp(-P y) at ({b},{am},{ap}): rise {rise} under floor(log_b 8192) - 1 = {need}")
        ok(min(row) >= row[0] - 1, f"P-C exp(-P y) at ({b},{am},{ap}): a c* below the j=1 value minus 1")

    print("\n=== P-D THE POLE UNITS: c*(1) - c*(8192) per cell (fall)")
    for name in ("1/(s+y)", "1/(s+y)^2", "sqrt(s+y)"):
        falls = []
        for (b, am, ap) in cells:
            row = [table[(name, b, am, ap, j)] for j in JS]
            fall = row[0] - row[-1]
            lb = math.floor(math.log(8192) / math.log(b))
            need = lb - 2 if name != "sqrt(s+y)" else lb // 2 - 2
            falls.append(fall)
            ok(fall >= need, f"P-D {name} at ({b},{am},{ap}): fall {fall} under {need}")
        print(f"  {name:10s}: falls {falls}")

    print("\n=== P-E THE MULTIPLIED STREAMS: least c* over every pair")
    for name in ("x/(s+y)", "x exp(-P y)"):
        cs = [table[(name, b, am, ap, j)] for (b, am, ap) in cells for j in JS]
        print(f"  {name:12s}: least c* {min(cs)}, greatest {max(cs)}")
        ok(min(cs) >= 0, f"P-E {name}: c* {min(cs)} below 0")

    print("\n=== P-F THE CHAIN: the eager product consumer's c2 at the pole pairs where the reciprocal leads")
    pairs = cp.pole_pairs(5)
    c2s = []
    for (b, am, ap, P) in pairs:
        o1, L1, c1, Rmin, Rm = cp.recip_params(b, am, ap, P)
        Mm, Mp, w, Mh = cp.window(b, am, ap)
        need = (Rm + Mh * Fr(b) ** c1) * w
        c2 = 0
        while Fr(b) ** c2 * (w - 1) < need:
            c2 += 1
        while Fr(b) ** (c2 - 1) * (w - 1) >= need:
            c2 -= 1
        c2s.append(c2)
        ok(c2 >= 0, f"K4 ({b},{am},{ap}) P={P}: the eager consumer's c2 = {c2} < 0")
    print(f"  {len(pairs)} pairs: c2 in {sorted(set(c2s))}, least {min(c2s)}; the product's output stream "
          f"has top R_m Mh at every pair, independent of c1*, so a third unit's floor is its own")

    print("\n=== VERDICT")
    k3 = [f for f in FAILURES if f.startswith("K3")]
    print("  THE CONVERSE IS KILLED: exp(-P y), one stream and no product, has a lookahead that rises with P"
          if not k3 else "  THE CONVERSE SURVIVES at: " + "; ".join(k3))
    print("  THE LEAD IS SPENT IN ONE HOP: c2 >= 0 at every leading pair" if not any(f.startswith("K4") for f in FAILURES)
          else "  the product leads at some pair; the three-unit chain is owed")
    print(f"\n{len(FAILURES)} failures; wall {time.time() - t0:.1f} s")


if __name__ == "__main__":
    main()
