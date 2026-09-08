"""The two-stream delay's necessity: the reader of a product of two
signed-digit streams has no strategy, and sliding the split of a
near-corner sum drives the image over an overlap zone, so the
tolerance law is a criterion at every radix and contiguous digit set.

THE QUESTION. explore_product_delay.py proves that the product X * Y
of two D-streams (radix b, D = {-am..ap}, slack rho = am + ap + 1 - b
>= 1, the output aligned with the inputs) is readable at lookahead c
when the law holds, and certifies by finite adversary trees that it
is not readable one lookahead lower at 13 cells, radices 2..5. This
rig closes the "only if" by a derivation and checks the derivation's
three moving parts against the same engine, then extends the census
to radices 6 and 7 as the derivation's check.

THE DERIVATION, in units of b^-(t+1) at the emitted level, with
n = t + 1 + c the input length and K = b^(n + c). The output cells at
level t+1 are [p - M-, p + M+] for integers p, M- = am/(b-1),
M+ = ap/(b-1), W = M- + M+ in [1, 2]; the image of the two input
boxes is an interval [lo, hi] lying in the parent cell because the
history was legal. A digit p is legal iff p <= lo + M- and
p >= hi - M+, so

  THE DEATH CRITERION: the reader has no legal digit iff the image
  STRICTLY CONTAINS an overlap zone [m + 1 - M-, m + M+] of two
  consecutive cells, for some integer m.

The criterion never mentions the output prefix: survival is a
property of the two streams alone, the reader has no strategy, and
the adversary may fix both streams in advance. Sufficiency is one
line: the image is at most 2 Mh W b^-c long, Mh = max(M-, M+), and
the law says exactly that this is at most W - 1, the zone's length,
so no image strictly contains a zone. Necessity: when the law fails
the excess E = 2 max(am, ap)(am + ap) - b^c (b-1) rho is a positive
integer and the corner image exceeds the zone by
g = E / ((b-1)^2 b^c) in the limit. Let U = ap (b^n - 1)/(b-1) be the
all-ap prefix (the top corner; the bottom corner mirrors it when
am > ap) and slide the split of a fixed sum:

    (u_i, v_i) = (U - I + i, U - I - i),   i = 0 .. I.

The sum is fixed, so the image length is fixed; its lower end
lo_i = ((U - I - M-)^2 - i^2)/K falls by (2i - 1)/K at each step and
by I^2/K in all. With lam = length - (W - 1)
= g - (W^2 + 2 I W)/K, the dead arcs (lo_i + M- - 1, lo_i + M- - 1
+ lam) of consecutive i overlap once lam > (2I - 1)/K, and their
union is an open interval longer than 1 once I^2 >= K, so it holds
an integer and some split kills. Taking I = ceil(sqrt K), both hold
once

    g K > W^2 + (2W + 2) ceil(sqrt K) - 1,                   (DEPTH)

true for every n past a threshold the cell sets, since K grows as
b^n. Every u_i, v_i is an n-digit D-string because a contiguous D
reaches every integer in [-am R, ap R], R = (b^n - 1)/(b-1).

THE SUM BESIDE IT. The same criterion prices addition at lookahead
c, the (t+1)-th output digit read against t + 1 + c input digits
(the sum's doubled range needs the output led by one position, or
the corpus's flush offset; the criterion is convention-free once the
levels are matched): the image is [s - 2M-, s + 2M+] b^-c with
s = u + v ANY integer, a lattice of pitch b^-c, so the reader dies
iff an integer lies in the open interval
((b^c - 2) M+, b^c - (b^c - 2) M-), whose length 2W - b^c rho/(b-1)
is the sum's Lebesgue excess. The reading lemma's stream correction
is this and nothing else: the set of image endpoints a map can reach
at the emitted scale against the dead arc — dense for the bilinear
product, whose split move (u+1)(v-1) - uv = v - u - 1 steps by any
integer over K, so the margin is exact; a lattice for the linear sum,
where the arc can fall between lattice points and the exact law sits
one digit above the margin.

THE SLATE, frozen before the engine.

P-A THE CRITERION IS THE ENGINE'S LEGALITY. Over every state the
    exact game reaches in at most two rounds at every census cell,
    radices 2..5, at both c* - 1 and c*, the engine's legal-digit
    set is empty iff the death criterion holds (a transplant of
    nothing: the criterion is derived from the engine's own cell
    and image formulas).
P-B THE LINE KILLS. At every cell with c* >= 1, at the least n
    satisfying (DEPTH), the split line's dead-arc union covers an
    integer at some i, and a greedy reader fed those two digit
    strings dies at or before level t + 1 = n - c, by the engine's
    own legality. The bottom corner is exercised at (8, 5, 4), the
    least cell with am > ap in scope.
P-C THE LINE IS SLOWER THAN THE CERTIFICATES. (DEPTH)'s n exceeds
    the certificates' one or two rounds at every cell: the sweep is
    a proof, not the fastest kill.
P-D THE SUM'S CLAUSE. At every census cell, radices 2..6, lookaheads
    1 and 2 (at 2 the clause's interval is empty at every cell, so
    the engine can only print survivals there), the engine's sum game certifies a kill exactly where the
    integer-free-interval clause says dead and survives the search
    where it says alive, in both conventions the engine carries — the
    corpus's flush game (delay 0, output offset c) and the aligned
    game with the output led by one position so the sum's doubled
    range fits the root cell (delay c - 1, offset 1); in the clause's
    units both read the (t+1)-th output against t + 1 + c input
    digits.
P-E RADICES 6 AND 7. Every representable cell there: the engine
    certifies c* - 1 failing within two rounds (the law's floor) and
    the greedy reader survives the search at c* (a theorem; the
    search a sanity print).

KILLS, frozen as what this rig PRINTS.

K1 P-A prints a disagreeing state -> the derivation's cell or image
   algebra is not the engine's; nothing downstream is read.
K2 A cell prints "line survives": no i on the split line at
   (DEPTH)'s n kills by the engine -> the sweep argument has a hole
   (the parabola's step or the arc's length), the theorem is not
   proved.
K3 P-D prints a cell where the engine's verdict and the clause
   differ -> the stream-correction clause is wrong for the sum.
K4 A radix-6 or 7 cell prints a certificate at c* -> engine or law
   fault (the sufficiency proof is contradicted); a survival at
   c* - 1 to the search depth is not a kill (the line kills deeper)
   but is printed.

POSITIVE CONTROL: P-A whole, read before any line.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CRITERION IS THE ENGINE'S LEGALITY. Over 19,364,453 states
   within two rounds at every representable cell of radices 2..5, at
   c* - 1 and c*, the death criterion and the engine's legal-digit
   set disagree at 0. P-A held; K1 never fired. The reader has no
   strategy at the tolerance cover: survival is a property of the
   streams.

F2 THE LINE KILLS EVERYWHERE [theorem: the derivation above, its
   three parts each checked against the engine]. At every cell with
   c* >= 1 in radices 2..7, 35 cells, and at the bottom-corner cell
   (8,5,4), the split line at (DEPTH)'s least n holds a killing
   split by the criterion, and the greedy reader fed those digit
   strings dies at or before level n - c by the engine's own
   legality (36/36). (DEPTH)'s n runs from 2 to 5 (I from 4 to 216);
   at every c* = 1 cell the corner split i = 0 kills at level 1 —
   the corner image already sticks out at the first emission — and
   at c* = 2 cells the killing split sits up to i = 185 of I = 216
   ((6,3,3), E = 6, the smallest excess per (b-1)^2 b^c in the
   census). P-B held; K2 never fired.

F3 THE SWEEP IS THE SLOW PROOF. (DEPTH)'s rounds n - c (2 to 4)
   never fall below the exhaustive certificates' 1 or 2 rounds and
   exceed them at every c* = 2 cell; the theorem's depth is a bound
   the certificates beat. P-C held.

F4 THE SUM'S CLAUSE, both conventions. At 70 census cells of
   radices 2..6 and lookaheads 1, 2, in the corpus's flush game and
   the aligned game alike, the engine's verdict equals the
   integer-free-interval clause at 140/140: dead at lookahead c iff
   an integer lies in ((b^c - 2) M+, b^c - (b^c - 2) M-). The clause
   is a second form of the lookahead criterion
   (explore_lookahead_proof.py: a lattice's residues against an
   interval, where that proof counts residues mod b) and explains
   the margin's wedge (explore_margin_wedge.py): the
   interval has positive length there and holds no integer. P-D
   held; K3 never fired.

F5 RADICES 6 AND 7, the law cell-for-cell. At all 22 representable
   cells the engine certifies c* - 1 failing in 1 round (17 cells)
   or 2 (5 cells: (6,2,5), (6,3,3), (7,2,6), (7,3,4), (7,4,3)), and
   the greedy reader survives the
   search at c* at 22/22. With explore_product_delay.py's 13 the law
   is certified at 35 cells, radices 2..7, and proved at all. P-E
   held; K4 never fired.

VERDICT. The two-stream delay is a CRITERION: the product of two
D-streams is readable at lookahead c iff b^c (b-1) rho
>= 2 max(am, ap)(am + ap), at every radix and every contiguous D
with rho >= 1 whose window holds its own products. The reading
lemma's stream correction is the map's reachable image-endpoint set
against the dead arc: zero for the product, whose endpoints are
dense at the emitted scale, and the lattice clause for the sum.

RUN RECORD: pure Python, integers and Fractions, standard library;
under memwatch, peak commit 9.1 MB against the 512 MB default; wall
255 s (P-A 139 s, P-D 1 s, P-E 115 s). Prints reproduced by:
python prime/code/explore_product_necessity.py
"""

import math
import os
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_product_delay import Game, census, delta_law, representable  # noqa: E402

FAILURES = []


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


# ------------------------------------------------------- the criterion

def dead_by_criterion(g, u, v, n, t):
    """The death criterion at level t+1 for the boxes of the n-digit
    prefixes u, v: an integer m with lo < m + 1 - M- and hi > m + M+,
    in units of b^-(t+1)."""
    lo, hi, s = g.image(u, v, n)
    Mm, Mp = Fr(g.am, g.b - 1), Fr(g.ap, g.b - 1)
    L = Fr(lo, s) * g.b ** (t + 1)
    H = Fr(hi, s) * g.b ** (t + 1)
    m = math.floor(L + Mm - 1) + 1       # least integer above L + M- - 1
    return m < H - Mp


def check_criterion(g, rounds):
    """Walk every state reached in <= rounds rounds; compare."""
    n_states = disagree = 0
    b = g.b

    def walk(u, v, q, t, r):
        nonlocal n_states, disagree
        n = t + g.c
        for (x, y) in g.pairs:
            u1, v1 = b * u + x, b * v + y
            legal = g.legal_digits(u1, v1, n + 1, q, t)
            n_states += 1
            if (not legal) != dead_by_criterion(g, u1, v1, n + 1, t):
                disagree += 1
            if r > 1:
                for p in legal:
                    walk(u1, v1, b * q + p, t + 1, r - 1)

    for (u, v) in g.opening_states():
        if g.legal(u, v, g.c, 0, 0):
            walk(u, v, 0, 0, rounds)
    return n_states, disagree


# --------------------------------------------------------- the line

def to_digits(x, n, b, am, ap):
    """An n-digit D-string for the integer x, most significant first;
    the remainder is kept inside [-am R, ap R] at every step."""
    ds = []
    for j in range(n - 1, -1, -1):
        R = (b ** j - 1) // (b - 1)
        for d in range(-am, ap + 1):
            r = x - d * b ** j
            if -am * R <= r <= ap * R:
                ds.append(d)
                x = r
                break
        else:
            raise ValueError("not representable")
    assert x == 0
    return ds


def depth_ok(b, am, ap, c, n):
    """(DEPTH) at input length n: g K > W^2 + (2W + 2) ceil(sqrt K) - 1,
    and the corner window stays one-signed: U - 2I - M- > 0."""
    rho, ah, Wd = am + ap + 1 - b, max(am, ap), am + ap
    E = 2 * ah * Wd - b ** c * (b - 1) * rho
    K = b ** (n + c)
    W = Fr(Wd, b - 1)
    g = Fr(E, (b - 1) ** 2 * b ** c)
    I = math.isqrt(K - 1) + 1            # ceil(sqrt K)
    U = ah * (b ** n - 1) // (b - 1)
    Ml = Fr(min(am, ap), b - 1)          # the far side of the corner box
    return (g * K > W * W + (2 * W + 2) * I - 1) and (U - 2 * I - Ml > 0), I, g


def run_line(b, am, ap, c, n, I):
    """Build the split line at input length n and find the killing
    split by the criterion, then feed the two digit strings to a
    greedy reader in the engine and report where it dies."""
    g = Game(b, am, ap, c, "prod")
    top = ap >= am
    R = (b ** n - 1) // (b - 1)
    U = ap * R if top else -am * R
    t = n - 1 - c
    kill_i = None
    for i in range(0, I + 1):
        u, v = (U - I + i, U - I - i) if top else (U + I - i, U + I + i)
        if dead_by_criterion(g, u, v, n, t):
            kill_i = (i, u, v)
            break
    if kill_i is None:
        return None, None
    i, u, v = kill_i
    xs, ys = to_digits(u, n, b, am, ap), to_digits(v, n, b, am, ap)
    # the greedy reader along the line
    uu = vv = q = 0
    for j in range(c):
        uu, vv = b * uu + xs[j], b * vv + ys[j]
    if not g.legal(uu, vv, c, 0, 0):
        return kill_i, ("root illegal", 0)
    for tt in range(0, t + 1):
        uu, vv = b * uu + xs[c + tt], b * vv + ys[c + tt]
        legal = g.legal_digits(uu, vv, c + tt + 1, q, tt)
        if not legal:
            return kill_i, ("dies at level", tt + 1)
        q = b * q + legal[0]
    return kill_i, ("survives the line", t + 1)


# ------------------------------------------------------------ the sum

def sum_clause_dead(b, am, ap, c):
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    lo, hi = (b ** c - 2) * Mp, b ** c - (b ** c - 2) * Mm
    m = math.floor(lo) + 1
    return m < hi


def certificate(g, max_rounds):
    """Least r <= max_rounds at which the adversary wins, else None."""
    for r in range(0, max_rounds + 1):
        if not g.reader_survives(r):
            return r
    return None


# ------------------------------------------------------------------ main

def main():
    t0 = time.time()
    print("=== P-A: the death criterion against the engine's legality, "
          "every state within 2 rounds, radices 2..5, c*-1 and c*")
    tot = bad = 0
    for (b, am, ap) in census(5):
        if not representable(b, am, ap):
            continue
        cs = delta_law(b, am, ap)
        for c in (cs - 1, cs):
            if c < 0:
                continue
            g = Game(b, am, ap, c, "prod")
            ns, dis = check_criterion(g, 2)
            tot += ns
            bad += dis
            ok(dis == 0, f"criterion disagrees at ({b},{am},{ap}) c={c}: {dis}")
    print(f"  states {tot}, disagreements {bad}   [{time.time()-t0:.1f}s]")

    print("\n=== P-B/P-C: the split line at (DEPTH)'s least n, every cell "
          "radices 2..7 with c* >= 1, plus the bottom corner (8,5,4)")
    print("  cell rho c*-1 E | least n (rounds t+1 = n-c), I | killing i, "
          "greedy reader's fate")
    cells = [x for x in census(7) if representable(*x)] + [(8, 5, 4)]
    for (b, am, ap) in cells:
        cs = delta_law(b, am, ap)
        c = cs - 1
        if c < 0:
            continue
        rho = am + ap + 1 - b
        n = c + 1
        while True:
            good, I, g = depth_ok(b, am, ap, c, n)
            if good:
                break
            n += 1
        E = g * (b - 1) ** 2 * b ** c
        kill, fate = run_line(b, am, ap, c, n, I)
        ok(kill is not None and fate[0] == "dies at level",
           f"line survives at ({b},{am},{ap}) c={c} n={n}")
        ki = kill[0] if kill else None
        print(f"  ({b},{am},{ap}) {rho} {c} {int(E)} | n={n} (rounds {n-c}), "
              f"I={I} | i={ki}, {fate}")

    print("\n=== P-D: the sum's integer-free-interval clause at lookahead c "
          "against the engine in both conventions, radices 2..6, c = 1..2 "
          "(search 2 rounds at c = 1, 1 at c = 2): flush (delay 0, o = c) "
          "and aligned "
          "(delay c-1, o = 1; the output leads by one so the sum's range "
          "fits the root cell)")
    agree = tot = 0
    for (b, am, ap) in census(6):
        for c in range(1, 3):
            pred = sum_clause_dead(b, am, ap, c)
            for (dl, o, name) in ((0, c, "flush"), (c - 1, 1, "aligned")):
                g = Game(b, am, ap, dl, "sum", o=o)
                r = certificate(g, 3 - c)
                tot += 1
                if (r is not None) == pred:
                    agree += 1
                else:
                    ok(False, f"sum clause ({b},{am},{ap}) c={c} {name}: engine "
                              f"{'kill@'+str(r) if r is not None else 'alive'} "
                              f"clause {'dead' if pred else 'alive'}")
    print(f"  cells x lookaheads x conventions {tot}, agree {agree}   "
          f"[{time.time()-t0:.1f}s]")

    print("\n=== P-E: radices 6 and 7, every representable cell: certificate "
          "at c*-1 (<= 2 rounds), greedy survival at c* (2 rounds, 1 at c* = 2 "
          "past radix 6)")
    print("  cell rho | c* | cert rounds at c*-1 | greedy at c*")
    for (b, am, ap) in census(7):
        if b < 6 or not representable(b, am, ap):
            continue
        cs = delta_law(b, am, ap)
        rho = am + ap + 1 - b
        r = certificate(Game(b, am, ap, cs - 1, "prod"), 2) if cs >= 1 else "-"
        gs = Game(b, am, ap, cs, "prod")
        gr = 2 if b ** (2 * cs) <= 64 else 1     # the search stays under a minute
        alive = gs.reader_survives(gr, reader="greedy")
        ok(alive, f"greedy dies at c* at ({b},{am},{ap})")
        if cs >= 1:
            ok(r is not None, f"no certificate within 2 rounds at ({b},{am},{ap}) c*-1")
        print(f"  ({b},{am},{ap}) {rho} | {cs} | {r} | "
              f"{'survives' if alive else 'DIES'}   [{time.time()-t0:.1f}s]")

    print(f"\n{'ALL OK' if not FAILURES else str(len(FAILURES)) + ' FAILURES'}"
          f"   wall {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
