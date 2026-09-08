"""The square's necessity: the progression line kills x^2 by the
engine's own legality wherever the monomial law fails, so the
one-stream square reads at exactly the Lebesgue margin — a proof of
the product's shape with a progression in place of the split.

THE QUESTION. explore_monomial_delay.py certifies, cell by cell, that
the square X^2 of one D-stream (radix b, D = {-am..ap}, slack
rho = am + ap + 1 - b >= 1, the output aligned with the input) is
readable at lookahead c iff b^c (b-1) rho >= 2 max(am, ap)(am + ap),
the product's law, and that no reader survives one lookahead lower.
The product's necessity proof (explore_product_necessity.py) slides
the SPLIT of a fixed sum, a move one stream does not have. This rig
runs the one-stream line the derivation names and checks it against
the engine, closing the "only if" for the square by construction.

THE DERIVATION, in units of b^-(t+1) at the emitted level, with
n = t + 1 + c the input length, K = b^(n+c), M- = am/(b-1),
M+ = ap/(b-1), W = M- + M+. For u >= M- the image of the box is
[(u - M-)^2, (u + M+)^2] / K and the death criterion reads: no legal
digit iff an integer m has lo + M- - 1 < m < hi - M+, an open
interval of length lam(u) = (2uW + M+^2 - M-^2)/K - (W - 1).

THE PROGRESSION. Write a = (b-1) u - am, so lo = a^2 / ((b-1)^2 K).
Along u_j = u_0 - j b^h with 2h >= n + c the square's phase is
LINEAR in j: a_j^2 = a_0^2 - 2 a_0 j (b-1) b^h + j^2 (b-1)^2 b^(2h),
the last term a multiple of (b-1)^2 K, so lo_j = lo_0 - j sigma
(mod 1) with sigma = 2 a_0 / ((b-1) b^L), L = n + c - h. With
a_0 = r (mod (b-1) b^L) the step is sigma = 2r / ((b-1) b^L) (mod 1),
set by u_0's low digits alone; a_0 = -am (mod b-1) always, so r is
realizable iff (b-1) | r + am, and then u_0 = (r + am)/(b-1)
(mod b^L). The width lam falls by 2W / b^L per step. At the corner
lam -> g = E / ((b-1)^2 b^c), E the law's integer excess; over the
range where lam >= g/2, of length Delta = gK/(4W) in u, the walk has
J = Delta / b^h = g b^L / (4W) steps, and its dead arcs
(lo_j + M- - 1, lo_j + M- - 1 + lam_j) sweep J sigma = g r / (2W(b-1))
of the circle. Take r the least integer >= 2W(b-1)/g with
r = -am (mod b-1); once b^L > 4r / ((b-1) g) the step is under g/2,
consecutive arcs overlap, their union is an interval of length at
least 1, it holds an integer, and some u_j kills. Every u_j is an
n-digit D-string (a contiguous D reaches every integer in
[-am R, ap R], R = (b^n - 1)/(b-1)) and u_j >= M- for large n. So at
every cell where the law fails the adversary has a fixed stream
that kills every reader: the square's floor is the law.

THE SLATE, frozen before the engine.

P-A THE LINE KILLS. At every representable square cell of radices
    2..5 with c* >= 1 (13 cells), at c = c* - 1, the progression
    above finds a killing u at some n <= N_MAX, and the greedy reader
    of explore_monomial_delay.py's engine fed that u's digits dies at
    or before level n - c.
P-B THE PROOF'S THRESHOLD IS SLOWER. The least n at which the
    proof's own sufficient conditions hold (sigma <= lam over the
    walked range, sweep >= 1) is at least the least n where the line
    kills, at every cell; both exceed the exhaustive certificate's
    n = c + depth at most cells.
P-C NO STRATEGY. The least n at which ANY n-digit prefix u kills by
    the criterion equals c + the engine's certificate depth at every
    cell: the shallowest kill is the criterion's, and the reader has
    no move.

KILLS, frozen as what this rig PRINTS.

K1 A cell prints "line: no kill to N_MAX" -> the progression
   argument has a hole; the square's necessity is not proved here.
K2 A cell prints "engine: reader alive past n - c" on a u the
   criterion kills -> the criterion is not the engine's legality for
   the square.
K3 P-C prints a cell where the brute-force least n differs from
   c + depth -> the reader has a strategy for the square, or the
   brute force misses a prefix.

POSITIVE CONTROL: P-C whole (the criterion against the exhaustive
tree, prefix by prefix), read before the line.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 NO STRATEGY. At all 13 cells the criterion's least killing n
   equals c + the exhaustive certificate depth (depths 1, 2 and 4;
   n from 1 to 5): the shallowest kill is a property of the prefixes
   and the reader has no move. P-C held; K3 never fired.

F2 THE LINE KILLS [theorem: the progression above, checked by the
   engine]. At all 13 cells the progression finds a killing prefix,
   at n from 1 to 9 (r from 4 to 122; the deepest (5,2,4) at n = 9,
   u = 1831281), and the greedy reader fed its digits dies at or
   before level n - c at every one, earlier than n - c at two
   cells. P-A held; K1 and K2 never fired.

F3 THE PROOF'S THRESHOLD IS SLOWER. The n at which the proof's own
   conditions hold (step under the width across the range, sweep at
   least 1) runs 2 to 12 and sits at or above the line's kill at all
   13 cells; the exhaustive certificate's n = c + depth sits at or
   below the line's kill at all 13, equal at 6. P-B held.

VERDICT. The square of one signed-digit stream is readable at
lookahead c iff b^c (b-1) rho >= 2 max(am, ap)(am + ap), the
product's law: sufficiency by the corner width, necessity by a
progression whose quadratic phase is linear along it. A monomial's
delay is a property of its degree, and the proof for one stream
needs no split.

RUN RECORD: pure Python, integers and Fractions, standard library;
under memwatch, peak commit 7.9 MB against the 512 MB default; wall
0.3 s. Prints reproduced by:
python prime/code/explore_square_line.py
"""

import os
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_monomial_delay import KGame, census, monomial_law, representable  # noqa: E402

FAILURES = []
N_MAX = 16


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


def ceil_div(x, y):
    return -((-x) // y)


def repunit(b, n):
    return (b ** n - 1) // (b - 1)


def kills(b, am, ap, c, u, n):
    """The death criterion at prefix u of length n, lookahead c: the
    image of the square in emitted units strictly contains a zone."""
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    lo, hi, s = KGame(b, am, ap, c, (2,)).image((u,), n)
    lo, hi = Fr(lo * b ** (n - c), s), Fr(hi * b ** (n - c), s)
    x = lo + Mm - 1
    m = x.__floor__() + 1
    return m < hi - Mp


def digits(b, am, ap, u, n):
    """An n-digit D-string for the integer u (contiguous D, redundant:
    the first admissible digit at each position)."""
    out = []
    for i in range(n):
        rest = n - 1 - i
        R = repunit(b, rest)
        for x in range(-am, ap + 1):
            v = u - x * b ** rest
            if -am * R <= v <= ap * R:
                out.append(x)
                u = v
                break
        else:
            raise ValueError("not representable")
    return out


def greedy_death_level(b, am, ap, c, stream):
    """Feed the stream to the greedy reader (first legal digit); return
    the level at which it dies, or None if it survives the stream."""
    g = KGame(b, am, ap, c, (2,))
    u, q, t = 0, 0, 0
    for i, x in enumerate(stream):
        u = b * u + x
        if i + 1 <= c:
            if i + 1 == c and not g.legal((u,), c, 0, 0):
                return 0
            continue
        legal = g.legal_digits((u,), i + 1, q, t)
        if not legal:
            return t + 1
        q, t = b * q + legal[0], t + 1
    return None


def line(b, am, ap, c, n):
    """The progression at input length n: returns (killing u or None,
    r, conditions_hold, sweep) for the cell."""
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    W = Mm + Mp
    K = b ** (n + c)
    h = ceil_div(n + c, 2)
    L = n + c - h
    E = 2 * max(am, ap) * (am + ap) - b ** c * (b - 1) * (am + ap + 1 - b)
    g = Fr(E, (b - 1) ** 2 * b ** c)
    r = (2 * W * (b - 1) / g).__ceil__()
    while (r + am) % (b - 1) != 0:
        r += 1
    U = ap * repunit(b, n)
    # u_0: the largest u <= U with u = (r + am)/(b-1) (mod b^L)
    res = ((r + am) // (b - 1)) % (b ** L)
    u0 = U - ((U - res) % (b ** L))
    sigma = Fr(2 * r, (b - 1) * b ** L)

    def lam(u):
        return Fr(2 * u * W.numerator, W.denominator * K) + Fr(Mp * Mp - Mm * Mm) / K - (W - 1)

    kill_u, j, sweep, cond = None, 0, Fr(0), True
    while True:
        u = u0 - j * b ** h
        if u < Mm or lam(u) < g / 2:
            break
        if kills(b, am, ap, c, u, n):
            kill_u = u
        if sigma > lam(u):
            cond = False
        sweep += sigma
        j += 1
        if kill_u is not None and not cond:
            break
    return kill_u, r, (cond and sweep >= 1 and j > 0), sweep, j


def main():
    t0 = time.time()
    cells = [(b, am, ap) for (b, am, ap) in census(5)
             if representable(b, am, ap, (2,)) and monomial_law(b, am, ap, 2) >= 1]

    print("=== P-C: the criterion's shallowest kill against the exhaustive tree")
    depths = {}
    for (b, am, ap) in cells:
        c = monomial_law(b, am, ap, 2) - 1
        d, _ = KGame(b, am, ap, c, (2,)).certificate_depth(12)
        depths[(b, am, ap)] = d
        least = None
        for n in range(c + 1, c + 12):
            R = repunit(b, n)
            if any(kills(b, am, ap, c, u, n) for u in range(-am * R, ap * R + 1)):
                least = n
                break
        ok(d is not None and least == c + d,
           f"K3 ({b},{am},{ap}) c={c}: brute-force least n {least} != c + depth {c}+{d}")
        print(f"  ({b},{am},{ap}) c={c}: certificate depth {d}, criterion's least n {least}"
              f" = c + {None if least is None else least - c}")
    if FAILURES:
        print("POSITIVE CONTROL FAILED; nothing below is read")
        return

    print("\n=== P-A, P-B: the progression line")
    print("  cell c | r | least n: line kills | proof's conditions hold | certificate n = c + depth")
    for (b, am, ap) in cells:
        c = monomial_law(b, am, ap, 2) - 1
        n_kill, n_cond, r_used, u_kill = None, None, None, None
        for n in range(c + 1, N_MAX + 1):
            u, r, cond, sweep, j = line(b, am, ap, c, n)
            if u is not None and n_kill is None:
                n_kill, r_used, u_kill = n, r, u
            if cond and n_cond is None:
                n_cond = n
            if n_kill is not None and n_cond is not None:
                break
        ok(n_kill is not None, f"K1 ({b},{am},{ap}) c={c}: line: no kill to N_MAX {N_MAX}")
        if n_kill is not None:
            lvl = greedy_death_level(b, am, ap, c, digits(b, am, ap, u_kill, n_kill))
            ok(lvl is not None and lvl <= n_kill - c,
               f"K2 ({b},{am},{ap}) c={c}: engine: reader alive past n - c on u={u_kill}, n={n_kill}")
            ok(n_cond is None or n_cond >= n_kill,
               f"P-B ({b},{am},{ap}): conditions hold at n={n_cond} before the line kills at {n_kill}")
        print(f"  ({b},{am},{ap}) c={c} | r={r_used} | {n_kill} (u={u_kill}, engine death level "
              f"{lvl if n_kill is not None else '-'}) | {n_cond} | {c + depths[(b, am, ap)]}")

    print(f"\nwall {time.time()-t0:.1f}s; failures: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)


if __name__ == "__main__":
    main()
