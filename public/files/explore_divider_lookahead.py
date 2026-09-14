"""The divider's lookahead at the deep pole: does the numerator stream
pin the divider's lookahead c* = L* - o at a bounded value while the
pole distance P grows, where the reciprocal's falls without bound?

THE QUESTION. The divider x/(s + y), s = M- + P, read as a C^2 map of
two streams, has its delay at exactly the margin law's L*
(explore_manystream_delay.py): the law b^L rho P^2 >= (P + Mh) wsum,
Lam = (P + Mh)/P^2 the box width rate, with Mh = max(M-, M+),
wsum = am + ap, rho = wsum + 1 - b, and the lead o the least integer
with 1/P <= b^o (the range [-M-/P, M+/P] inside the root cell). At the
pole sweep P = j/(b - 1), j in {1, 2, 4, 8}, the lookahead c* = L* - o
read 1 or 2 at all 80 pairs of radices 2..5 while the reciprocal's
c1* fell to -4 (explore_onestream_delay.py): the reciprocal emits before
it reads, the divider never does. Is that the shallow sweep's accident
or the unit's property, and what happens at P = 32/(b - 1) and
128/(b - 1), where the reciprocal runs furthest ahead?

THE DERIVATION, written before the engine. Both halves of c* are
closed forms: L* = ceil(x) with x = log_b((P + Mh) wsum / (rho P^2)),
o = ceil(y) with y = log_b(1/P), so

    x - y = log_b((1 + Mh/P) wsum / rho).

wsum/rho = 1 + (b - 1)/rho >= 2 since rho <= b - 1 (the largest slack,
am = ap = b - 1), so x - y >= log_b 2 > 0, and ceil(x) - ceil(y) >
x - y - 1 > -1: c* >= 0 AT EVERY P AND EVERY CELL. Upward,
c* < x - y + 1 <= 1 + log_b(wsum/rho) + log_b(1 + Mh/P) <=
2 + log_b(1 + Mh/P) (wsum/rho <= b at rho = 1), so c* <= 2 wherever
Mh/P < b - 1, which is every P >= 1/(b - 1) of the sweep. The
shallow sweep's "1 or 2" is the algebra's {0, 1, 2} with the 0 not
yet met; c* = 0 needs x and y to round to the same integer, which the
grid P = j/(b - 1) need not offer but a P with 1/P just above a power
of b does (at (5,4,4) and P = 249/10, 1/P = 0.04016 sits just above
1/25, so o = -1, and (P + 1) 8/(4 P^2) = 0.0806 gives L* = -1: c* = 0).
THE DESCENT. Nothing above used the pole: for f = x g(y), g any C^2
function of the other stream with G = sup |g| over the window, the
x-partial IS g, so Lam >= G, while the range's top is M+ G (g > 0),
so o = ceil(log_b G); the same two lines give c* > log_b(wsum/rho) - 1
>= -1. A unit that multiplies a stream by any function of the others
never emits before it reads, whatever the function's pole. The
reciprocal (Lam = 1/P^2 against a top of 1/P) and the square root
(Lam = 1/(2 sqrt P) against a top near sqrt P) carry no such stream:
their x - y is log_b(wsum/(rho P)) and log_b(wsum/(2 rho P)), falling
through every integer as P grows. The family x/(s + y)^k, k = 1, 2, 3,
has Lam = (P + k Mh)/P^(k + 1) at the pole corner (both partials are
largest there), G = 1/P^k, and the same bound; 1/(s + y)^k alone has
Lam = k/P^(k + 1), a one-signed range with top 1/P^k, so its lead is
the least o with 1/P^k <= M+ b^o and x - y = log_b(k M+ wsum/(rho P)).
THE CHAIN. The reciprocal feeding a product reads at L' = c2' + o1 in
the output's scale (explore_chain_product.py, leg 2), and the fused
divider's Lf* is at or below it at every pair, since
b^L1* >= wsum/(rho P^2) puts the chain's Mh term at or above the fused
unit's Mh/P^2: at the deep pairs both are closed forms.

THE SLATE, frozen before the engine.

P-A THE CONTROL. The closed forms ceil(x), ceil(y) agree with the
    engine's integer loops (explore_manystream_delay.py least_lead and
    law_L) at the 80 shallow pairs and the 40 deep pairs; the engine
    re-run at the four shallow pairs of radices 2 and 3 at P = 1/(b - 1)
    prints c* in {1, 2}, dead at L* - 1 and alive at L*, as its own
    record does.
P-B THE DEEP SWEEP. c* at the 40 pairs of P = 32/(b - 1) and
    128/(b - 1) over the 20 cells of radices 2..5: in {0, 1, 2} by the
    derivation; in {1, 2} is the shallow sweep's reading carried over,
    a TRANSPLANT, and the grid decides it. The engine at the 40 pairs:
    dead at L* - 1 and alive at L* (the theorem's check; the excess
    is small at the deep pairs, so the kills sit deeper than the
    shallow sweep's output depth 1..4 and the region is larger).
P-C THE DENSE SWEEP. c* over P = j/(b - 1), j = 1..4096, and over
    P = q/10, q = 1..1000, at every cell of radices 2..5: never
    negative, at most 2; at least one pair reads 0, (5,4,4) at
    P = 249/10 among them.
P-D THE DESCENT. x/(s + y)^k, k = 1, 2, 3, at every cell and every P
    of the dense sweep: c* >= 0 at all; 1/(s + y)^k at the same pairs:
    c* negative at the deep end of every cell, the least value falling
    with P.
P-E THE CHAIN AT THE DEEP PAIRS. L' against Lf* at the 40 deep pairs:
    Lf* <= L' at every pair, the count of equalities printed.

KILLS, frozen as what this rig PRINTS.

K1 A closed form differing from the engine's loop at any pair, or the
   re-run's verdict differing from the record -> the forms are not the
   engine's; nothing below is read.
K2 A negative c* printed anywhere in P-B, P-C or the product family of
   P-D -> the derivation is wrong.
K3 The engine at a deep pair killing at L*, or reaching a region of at
   least 10^5 boxes at L* - 1 with no kill and the confined tree
   surviving -> the theorem's check fails there (the engine's own K2
   and K3, re-raised here).
K4 Lf* > L' at a deep pair -> the chain inequality is wrong.

POSITIVE CONTROL: P-A whole, read before any other line.

FINDINGS (entered post-run; every number below sits in this file's
printed output at radices 2..5).

F1 THE CONTROL HOLDS. The closed forms agree with the engine's loops
   at 120 of 120 pairs; the four shallow pairs re-run print c* = 2,
   dead at L* - 1 (output depth 2, 2, 2, 3) and alive at L*. K1 never
   fired. Controls 1.0 s.

F2 THE DEEP SWEEP [the bound c* >= 0 a property, by the derivation;
   the values a rule at the 40 pairs]. c* in {0, 1, 2} at the 40
   pairs: 0 at 5 ((4,3,3) at P = 32/3; (3,2,2), (4,2,3), (4,3,2) and
   (4,3,3) at P = 128/(b - 1)), 1 at 33, 2 at 2 ((2,1,1) at P = 32 and
   128); leads o from -7 to -1, L* from -5 to 0. The transplant "1 or
   2" failed as the derivation allowed, the zeros at cells of slack
   rho >= 2 only. The engine: dead at L* - 1 at 40 of 40 (output depth
   t in {1, 2, 4, 5, 7}, input depth n from 0 to 8; the region at most
   605 boxes, at (4,2,3) P = 32/3; the line at the depth before the
   kill holds at most 15 boxes against N_0 from 9.26e5 to 7.99e12), alive
   at L* at 40 of 40 by the scan and by the bare tree. The deepest kill
   is (2,1,1) at P = 128, excess g = 0.008, output depth 7, input depth
   8, region 385. The two cited inequalities read at 40 depths of
   16,383 to 39,062 phases, D_N at most 0.003. K2 and K3 never fired.
   Deep sweep 11.3 s.

F3 THE DENSE SWEEP [property for the bounds; the zero cells a rule at
   the 20]. 98,620 distinct pairs: c* from 0 to 4 -- at most 2 at the
   98,561 pairs with P >= 1/(b - 1), at most 4 at the 59 below it, where
   Mh/P exceeds b - 1 (P-C's "at most 2" was written without the
   derivation's own range and fails there; the split print was added
   after the run). c* = 0 at 19,212 pairs over exactly the ten cells
   with rho >= 2 and at none of the ten with rho = 1, where wsum/rho
   = b, x - y >= 1 and the derivation gives c* >= 1; (5,4,4) at
   P = 249/10 reads 0 as predicted, the first zero in the sweep's
   order being (3,2,2) at P = 14/5. K2 never fired.

F4 THE DESCENT [property, the print its check]. x/(s + y)^k at
   k = 1, 2, 3: least c* 0 over the 98,620 pairs each; 1/(s + y)^k at
   the same pairs, its lead at the reciprocal rig's convention: least
   c* -11, -10, -10, negative at 97,368, 96,086 and 94,808 pairs, and
   negative at the deepest P at 20 of 20 cells.

F5 THE CHAIN AT THE DEEP PAIRS. The fused divider's Lf* equals the
   chain's L' at 33 of the 40 deep pairs, sits below it at 7 and above
   at none: below by one at four radix-5 pairs at P = 8 ((5,1,4),
   (5,2,3), (5,3,2), (5,4,1)) and at three pairs whose fused c* is 0
   ((4,3,3) at P = 32/3, (4,2,3) and (4,3,2) at P = 128/3). K4 never
   fired.

VERDICT. The divider's lookahead never negative is a PROPERTY of the
margin law's closed form and not the shallow sweep's accident: c* >= 0
at every pole distance, c* >= 1 at slack 1, c* <= 2 at every
P >= 1/(b - 1), and the pole-depth term past the lead is a rounding.
The property belongs to every unit that multiplies a stream by a
function of the others, the numerator's partial being the range's own
scale; the reciprocal and the root, with no such stream, run ahead
without bound. The deep sweep is the theorem's check, dead at L* - 1
and alive at L* at all 40 pairs, the kills deeper and the regions
larger than the shallow sweep's as the excess shrinks.

RUN RECORD: pure Python, exact rationals for every verdict, the
many-stream engine imported for the deep sweep; under memwatch, peak
commit 48.6 MB against the 512 MB default, wall 25 s at radices 2..5.
Prints reproduced by:
python prime/code/explore_divider_lookahead.py [BMAX]
"""

import math
import os
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_manystream_delay as ms                      # noqa: E402
import explore_chain_product as cp                         # noqa: E402

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


def params(b, am, ap):
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    return Mm, Mp, max(Mm, Mp), am + ap, am + ap + 1 - b


def unit_c(b, am, ap, lam, top):
    """(o, L*, c*) of a unit with box width rate lam and range top
    `top` in units of M+ (the range [-M- top, M+ top]): o the least
    integer with top <= b^o, L* the least with b^L rho >= lam wsum."""
    Mm, Mp, Mh, wsum, rho = params(b, am, ap)
    o = ceil_log(b, top)
    L = ceil_log(b, lam * wsum / rho)
    return o, L, L - o


def divider_c(b, am, ap, P, k=1):
    """x/(s + y)^k: lam = (P + k Mh)/P^(k + 1), top 1/P^k."""
    Mm, Mp, Mh, wsum, rho = params(b, am, ap)
    return unit_c(b, am, ap, (P + k * Mh) / P ** (k + 1), 1 / P ** k)


def recip_c(b, am, ap, P, k=1):
    """1/(s + y)^k alone: lam = k/P^(k + 1); its range [1/(P + w)^k, 1/P^k]
    is one-signed, so the lead is the least o with 1/P^k <= M+ b^o
    (explore_onestream_delay.py's convention), the top 1/(P^k M+)."""
    Mm, Mp, Mh, wsum, rho = params(b, am, ap)
    return unit_c(b, am, ap, Fr(k) / P ** (k + 1), 1 / (P ** k * Mp))


def census(bmax):
    return [(b, am, ap) for b in range(2, bmax + 1)
            for am in range(0, b) for ap in range(0, b)
            if am + ap + 1 - b >= 1]


# -------------------------------------------------------------------- runs

def control(bmax):
    print("\n=== P-A: the closed forms against the engine's loops at the 120 sweep pairs")
    agree = tot = 0
    for j in (1, 2, 4, 8, 32, 128):
        for (b, am, ap) in census(bmax):
            P = Fr(j, b - 1)
            fmap = ms.Division(b, am, ap, P)
            o_e, L_e = ms.least_lead(b, am, ap, fmap), ms.law_L(b, am, ap, fmap)
            o, L, c = divider_c(b, am, ap, P)
            tot += 1
            good = (o, L) == (o_e, L_e)
            agree += good
            ok(good, f"K1 ({b},{am},{ap}) P={P}: closed (o,L*)=({o},{L}), engine ({o_e},{L_e})")
    print(f"  {agree} of {tot} pairs agree")
    print("\n=== P-A: the engine re-run at the shallow pairs of radices 2..3, P = 1/(b - 1)")
    for (b, am, ap) in census(3):
        P = Fr(1, b - 1)
        r = ms.one_pair(b, am, ap, ms.Division(b, am, ap, P), label=f"P={P}")
        ok(r["c"] in (1, 2) and r["tk"] is not None and r["ns"] >= 0,
           f"K1 ({b},{am},{ap}) P={P}: c*={r['c']}, kill t={r['tk']}, L* scan n={r['ns']}")


def deep_sweep(bmax):
    print(f"\n=== P-B: the deep sweep, P = 32/(b - 1) and 128/(b - 1), radices 2..{bmax}")
    print("  pair: lead o, the law's L*, lookahead c* | at L*-1: excess g, the cube, N_0, "
          "the scan's kill (t, n) with the region and line counts, the confined tree | at L* | P-D")
    rows = []
    for j in (32, 128):
        for (b, am, ap) in census(bmax):
            P = Fr(j, b - 1)
            before = len(ms.FAILURES)
            r = ms.one_pair(b, am, ap, ms.Division(b, am, ap, P), label=f"P={j}/{b - 1}")
            for f in ms.FAILURES[before:]:
                ok(False, "K3 " + f)
            ok(r["c"] >= 0, f"K2 ({b},{am},{ap}) P={P}: c*={r['c']} negative")
            rows.append(r)
    ms.summarize(rows, "x/(s + y) deep")
    cs = sorted(set(r["c"] for r in rows))
    print(f"  c* at the 40 deep pairs in {cs}; zero at {sum(1 for r in rows if r['c'] == 0)}, "
          f"one at {sum(1 for r in rows if r['c'] == 1)}, two at {sum(1 for r in rows if r['c'] == 2)}; "
          f"leads o from {min(r['o'] for r in rows)} to {max(r['o'] for r in rows)}, "
          f"L* from {min(r['L'] for r in rows)} to {max(r['L'] for r in rows)}")
    kills = [r for r in rows if r["tk"] is not None]
    print(f"  certified at L*-1 at {len(kills)} of {len(rows)}: output depth t in {sorted(set(r['tk'] for r in kills))}, "
          f"the region at most {max((r['rcnt'] for r in kills), default=0)}; "
          f"alive at L* by the scan at {sum(1 for r in rows if r['ns'] >= 0)}, by the tree at {sum(1 for r in rows if r['rdepth2'] > 0)}")
    return rows


def dense_sweep(bmax):
    print(f"\n=== P-C: the dense sweep, P = j/(b - 1), j = 1..4096, and P = q/10, q = 1..1000, radices 2..{bmax}")
    cells = census(bmax)
    Ps = lambda b: sorted(set([Fr(j, b - 1) for j in range(1, 4097)] + [Fr(q, 10) for q in range(1, 1001)]))
    cmin, cmax, zeros, tot = 10, -10, [], 0
    cmax_in, cmax_out, nout = -10, -10, 0     # P >= 1/(b - 1) against below it
    for (b, am, ap) in cells:
        for P in Ps(b):
            o, L, c = divider_c(b, am, ap, P)
            tot += 1
            cmin, cmax = min(cmin, c), max(cmax, c)
            if P >= Fr(1, b - 1):
                cmax_in = max(cmax_in, c)
            else:
                cmax_out, nout = max(cmax_out, c), nout + 1
            if c == 0:
                zeros.append((b, am, ap, P))
    ok(cmin >= 0, f"K2 dense sweep: least c* = {cmin}")
    named = (5, 4, 4, Fr(249, 10)) in zeros
    zin = [z for z in zeros if z[3] >= Fr(1, z[0] - 1)]
    print(f"  {tot} pairs: c* from {cmin} to {cmax}; at the {tot - nout} pairs with P >= 1/(b - 1) c* at most {cmax_in}, "
          f"at the {nout} below it at most {cmax_out}; c* = 0 at {len(zeros)} pairs over "
          f"{len(set(z[:3] for z in zeros))} cells ({len(zin)} pairs over {len(set(z[:3] for z in zin))} cells at P >= 1/(b - 1)); "
          f"(5,4,4) at P = 249/10 reads 0: {named}"
          + (f"; first zero {zeros[0][:3]} at P = {zeros[0][3]}" if zeros else ""))
    cz = sorted(set(z[:3] for z in zeros))
    print(f"  cells with a zero: {cz}; cells without: {[c for c in cells if c not in cz]}")
    print("\n=== P-D: the descent, x/(s + y)^k against 1/(s + y)^k, k = 1, 2, 3, the same pairs")
    for k in (1, 2, 3):
        pmin, rmin, rneg, tot = 10, 10, 0, 0
        deep_neg = 0
        for (b, am, ap) in cells:
            ps = Ps(b)
            for P in ps:
                tot += 1
                pmin = min(pmin, divider_c(b, am, ap, P, k)[2])
                rc = recip_c(b, am, ap, P, k)[2]
                rmin = min(rmin, rc)
                rneg += rc < 0
            deep_neg += recip_c(b, am, ap, Fr(4096, b - 1), k)[2] < 0
        ok(pmin >= 0, f"K2 x/(s + y)^{k}: least c* = {pmin}")
        print(f"  k={k}: x/(s + y)^k least c* {pmin} over {tot} pairs; 1/(s + y)^k least c* {rmin}, "
              f"negative at {rneg} pairs, negative at the deepest P at {deep_neg} of {len(cells)} cells")


def chain_deep(bmax):
    print(f"\n=== P-E: the two-unit divider against the fused divider at the 40 deep pairs, radices 2..{bmax}")
    print("  cell P | o1 c1* d | eager c2' | chain L' | fused (of, Lf*)")
    eq = below = above = 0
    for j in (32, 128):
        for (b, am, ap) in census(bmax):
            P = Fr(j, b - 1)
            Mm, Mp, w, Mh = cp.window(b, am, ap)
            o1, L1s, c1, Rmin, Rm = cp.recip_params(b, am, ap, P)
            d = max(0, -c1)
            c2e = cp.least_L(b, w, (Rm + Mh / Fr(b) ** d) * w)
            of, Lf = cp.divider_params(b, am, ap, P)
            Lp = c2e + o1
            eq += Lf == Lp
            below += Lf < Lp
            above += Lf > Lp
            ok(Lf <= Lp, f"K4 ({b},{am},{ap}) P={P}: fused Lf*={Lf} above the chain's L'={Lp}")
            print(f"  ({b},{am},{ap}) P={P} | {o1} {c1} {d} | {c2e} | {Lp} | ({of}, {Lf})")
    print(f"  fused equal to the chain at {eq}, below at {below}, above at {above}")


def main():
    bmax = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    t0 = time.time()
    control(bmax)
    if FAILURES:
        print("\nPOSITIVE CONTROL FAILED; nothing below is read")
        for f in FAILURES:
            print("  ", f)
        return
    print(f"  controls: {time.time() - t0:.1f}s")
    deep_sweep(bmax)
    print(f"  deep sweep: {time.time() - t0:.1f}s")
    dense_sweep(bmax)
    chain_deep(bmax)
    print(f"\nwall {time.time() - t0:.1f}s; failures: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)


if __name__ == "__main__":
    main()
