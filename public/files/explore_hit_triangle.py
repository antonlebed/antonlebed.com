"""explore_hit_triangle.py — THE HIT TRIANGLE: is the hit vector of the
greedy dlog of zeta_p a unitriangular function of the digits of w, the
jump set its record reading and the mass law its pushforward?

THE QUESTION. The jump set of a totally ramified f = 1 window K/Q_p
with integral seat i* = c_0 p^M is a function of the first M e digits
of w = -p/pi^e (2/pi^e at p = 2), read by the greedy dlog of zeta_p in
the digit ring (explore_jump_digits.py): the dlog strips a basis
monomial (1 + pi^a)^(d p^b) at each HIT, a level L in [i*, CAP) with
pullback (a, b), CAP = e* + (M - 1) e + 1, and the frontier is the
Pareto frontier of the coordinates' (order, weight). Only the first
two frontier points had closed forms: (c_0, M + 1) at e*, and the
second at e* + min(delta_w, X) up to the truncation
(explore_second_point.py). The aim was the THIRD point's closed form.
The e = 4 census (256 digit strings, every hit set printed) shows
every one of the 256 subsets of the eight levels 5..12 appearing
exactly once — the map from digit strings to hit sets is a BIJECTION
there — and the count is not an accident: the digit precision M e is
exactly the number of levels in (i*, CAP), at every p. This rig asks
whether that map is unitriangular, and what follows.

THE OBJECTS. The HIT DIGIT h_L at level L is the digit d of the
monomial (1 + pi^a)^(d p^b) the greedy dlog strips at L (0 = no hit;
at p = 2 a hit indicator; a unit times the residual's digit); the HIT VECTOR is (h_(i*+1), ..., h_(i*+Me)), Me
entries. The pullback of L is the unique (a, b) with a in T* and
rho^b(a) = L, rho(i) = min(p i, i + e); the ORBIT of a is
{a, rho(a), rho^2(a), ...}. The RECORD READING of a hit vector:
scanning levels upward from the seat, a hit at L with pullback
(a, b) that is the first hit in a's orbit has order b + 1; it is a
frontier point iff its order is strictly below every earlier
frontier point's, and the seat hit (c_0, M + 1) opens the reading.

THE HAND DERIVATION (on paper, before the engine).

H1  THE TRIANGLE. h_(i*+r) = u_r w_r + g_r(w_1, ..., w_(r-1)) with u_r
    a unit mod p. The upward lemma (explore_jump_digits.py H2) puts
    every reading of w in the digit ring at or above the level it
    enters: a carry at level s lands at s + e carrying w_j at
    s + e + j, and s >= 1, i* <= e give j <= r - 1 at level i* + r;
    a product's level-X digit reads its factors' levels <= X; a
    stripped monomial (1 + pi^a)^(-d p^b) has unit coefficients at
    levels ak carrying no w, and p-divisible ones carrying w only
    through carries, j <= r - 1 again. The one reading of w_r at
    level i* + r is zeta_p's own: at p = 2, zeta_2 = 1 - w pi^e and
    the canonical digits of -w = w - w^2 pi^e read w_r once with
    coefficient 1 plus lower digits; at odd p the equation at the
    seat (1 + t)^(p-1) = w(1 + c_2 y + ...) reads t_s = -w_s + (lower)
    and zeta_p's digit at i* + s is d t_s + (lower), d the seat
    digit. The hit history below i* + r is a function of w_(<r). So
    the map (w_1..w_Me) -> (h_(i*+1)..h_(i*+Me)) is unitriangular over
    F_p, hence a BIJECTION F_p^Me -> F_p^Me, and the hit digits of a
    uniform digit string are independent and uniform on F_p, level
    by level.
H2  THE RECORD READING IS THE FRONTIER. A coordinate a's value is
    sum d_i p^(b_i) over the hits in its orbit, distinct b_i, so its
    order is 1 + min b_i, the first hit in the orbit, and its weight
    rho^(order)(a) = rho(that hit's level): weights increase with
    the level, so the Pareto frontier under (order, weight) is the
    set of first-in-orbit hits whose order is a strict record going
    up. Hits at or above CAP have order >= M + 1 and are dominated
    by the seat point (explore_jump_digits.py H1).
H3  THE MASS LAW IS THE PUSHFORWARD. Under independent uniform hit
    digits the order of a coordinate a is 1 + (the position of the
    first nonzero digit along its orbit): P(order = k) = (p - 1)/p^k,
    independent across coordinates since orbits are disjoint. That is
    Pagano's law (explore_jump_haar.py law: P(b) = (p - 1)/p^b,
    independent), conditioned on the least weight e* — which the
    digit picture has automatically, the seat hit fixing the point
    (c_0, M + 1) and no hit lying below i*. So the digit cells at
    precision M e carry the mass law's exact counts at every p and e:
    the digit-census rule (e = 2, 4) and observation (e = 8) become a
    THEOREM, the digit measure's pushforward and Pagano's law the same
    distribution. Nothing here says the digit cells are Haar cells.
H4  THE THIRD POINT AT e = 4, p = 2 (the aim). tau = 2 (w_1 = w_2 = 0)
    is the only second point of order 2, (3, 2) at weight 10; every
    other tau gives an order-1 second point and closes the frontier.
    After stripping B = (1 + pi)^4 and S = (1 + pi^3)^2, the residual
    is 1 + B S up to a unit: 1 + B S = 2 + 4 pi + 6 pi^2 + 6 pi^3 +
    9 pi^4 + 12 pi^5 + 9 pi^6 + ... with 2 = w pi^4 gives
    (w_3 + 1) pi^7 + (w_4 + 1) pi^8 mod pi^9: the pi^7 term is S's
    binomial tail 2 pi^3 = w pi^7 beside zeta's w_3, the pi^8 term the
    doubled seat 2 pi^4 = w pi^8 beside zeta's w_4. So the third point
    is (7, 1) at weight 11 iff w_3 = 0; (8, 1) at weight 12 iff
    w_3 = 1 and w_4 = 0; absent otherwise. It reads two digits past
    tau and two tails, S's and the seat's own doubling, so the aim's
    "one tail" formula is wrong and "two at once" is right — and both
    are one row of the triangle.
H5  THE ALGEBRAIC NORMAL FORM at e = 4 read off the census by hand:
    h_5 = w_1; h_6 = w_2 + 1; h_7 = w_3 + w_2 + w_1 + 1;
    h_8 = w_4 + (1 + w_1)(1 + w_2). Degree 2 appears at h_8; the
    triangle is not affine. At e = 2 (explore_jump_digits.py H5):
    h_3 = w_1 + 1 and h_4 = w_2 when w_1 = 1.

PREDICTIONS, fixed before the engine ran.
  PR1 (bijection, exhaustive). Over every digit string at (p, e) =
      (2, 2), (2, 4), (3, 6): the hit vectors are pairwise distinct
      and every hit lies in [i*, CAP). KILL: two strings sharing a
      hit vector.
  PR2 (the diagonal, sampled). At (2, 8), (2, 12) with c_0 = 3,
      (2, 16), (3, 12) with c_0 = 2, (3, 18), (5, 20), and the three
      exhaustive cells: for every sampled string and every r <= Me,
      the p strings differing only at w_r have identical hit digits
      below i* + r and hit digits at i* + r forming a permutation of
      F_p. KILL: one (string, r) off.
  PR3 (the record reading). At every string read, the record reading
      of the hit vector equals the digit ring's frontier. KILL: one
      string off.
  PR4 (the mass law is the pushforward). The record-reading masses
      under independent uniform hit digits, computed exactly by a
      recursion over the levels, equal explore_jump_haar.py's law at
      (2, 2), (2, 4), (2, 8), (2, 12), (3, 6), (3, 12): every class,
      every mass, as fractions. KILL: one mass off or one class
      missing on either side.
  PR5 (the ANF). At e = 4 the algebraic normal forms of h_5..h_12 are
      H5's for h_5..h_8, each h_(4+r) carries the monomial w_r with
      coefficient 1 and no variable past w_r; at e = 8, h_9..h_20 the
      same diagonal, computed over w_1..w_12. KILL: a diagonal
      coefficient 0, or a hand row off.
  PR6 (the third point at e = 4, H4). Over the 256 strings: the
      third frontier point is (7, 1) exactly at the 32 strings with
      w_1 = w_2 = w_3 = 0, (8, 1) exactly at the 16 with w_1 = w_2 =
      0, w_3 = 1, w_4 = 0, and absent at the other 208. KILL: one
      string off.
  PR7 (controls, read first). x^2 - 2's digits (1, 0, ...) give the
      hit vector (1, 1) at levels 3, 4 and records ((1, 2), (3, 1));
      the anchor zeta_8 gives the zero hit vector and records
      ((1, 3),); the e = 2 ANF is h_3 = w_1 + 1.

THE DESIGN. engine: explore_jump_digits.py's digit ring, seat split,
frontier and digit_frontier, with a dlog variant recording the hit
digit at every level; the record reading; the ANF by the Moebius
transform over F_2; the mass recursion over the levels with state
(orbits hit, frontier so far). Sampled strings are uniform digit
strings from seed 1180. verdict: PR1-PR7 as counts.
Run: python prime/code/explore_hit_triangle.py

FINDINGS (entered post-run, copied from printed output).

1. THE TRIANGLE (PR1, PR2 hit). Exhaustively, 4 strings at (2, 2), 256
   at (2, 4) and 729 at (3, 6) give 4, 256 and 729 distinct hit
   vectors over 2, 8 and 6 levels in (i*, CAP), each level count M e.
   At 6420 (string, digit) pairs over (2, 8), (2, 12) with c_0 = 3,
   (2, 16) with M e = 64, (3, 12) with c_0 = 2, (3, 18), (5, 20),
   (3, 6) and (2, 4), changing w_r leaves every hit below i* + r and
   runs the hit digit at i* + r through all of F_p.

2. THE RECORD READING IS THE FRONTIER (PR3 hit at every string read,
   exhaustive and sampled).

3. THE MASS LAW IS THE PUSHFORWARD (PR4 hit): the record-reading
   masses under independent uniform hit digits equal the law class by
   class as fractions — 3 classes at (2, 2), 10 at (2, 4), 44 at
   (2, 8), 30 at (2, 12), 6 at (3, 6), 10 at (3, 12); the largest
   1/2, 1/8, 1/8 at p = 2 and 2/3, 2/9, 2/27 at p = 3.

4. THE ALGEBRAIC NORMAL FORMS (PR5 hit, the diagonal w_r in every row
   and H5's four rows verbatim). e = 2: h_3 = 1 + w1, h_4 = 1 + w1 +
   w2. e = 4: h_5 = w1; h_6 = 1 + w2; h_7 = 1 + w1 + w2 + w3; h_8 =
   1 + w1 + w2 + w4 + w1w2; h_9 = 1 + w1 + w3 + w5; h_10 = w4 + w5 +
   w6 + w1w3 + w2w3 + w1w5; h_11 of degree 3 with eleven monomials;
   h_12 = 1 + w1 + w2 + w4 + w8 + w3w5 + w2w6 + w1w7. e = 8: h_9 =
   w1, h_10 = w2, h_11 = w3, h_12 = 1 + w4, h_13 = w1 + w2 + w5,
   h_14 = 1 + w2 + w4 + w6 + w1w2, h_15 = 1 + w1 + w3 + w4 + w6 + w7
   + w1w2 + w1w4, then degrees 2, 2, 3, 3, 3 to h_20 with up to 29
   monomials. The rows are affine to h_7 at e = 4 and to h_13 at
   e = 8 and of degree 1 to 3 after (h_9 affine, h_11 cubic at e = 4),
   so the triangle is not affine
   and no row past the first few is a formula in a fixed handful of
   digits.

5. THE THIRD POINT AT e = 4 (PR6 hit): (7, 1) at the 32 strings with
   w_1 = w_2 = w_3 = 0, (8, 1) at the 16 with w_1 = w_2 = 0, w_3 = 1,
   w_4 = 0, absent at 208 — H4's two tails, S's and the doubled seat.

TIER. THE HIT TRIANGLE — the hit vector of the greedy dlog of zeta_p
below CAP is a unitriangular function of the digits w_1..w_(Me),
h_(i*+r) = u_r w_r + g_r(w_(<r)) with u_r a unit, hence a bijection
F_p^(Me) -> F_p^(Me); the jump set is its record reading; and
Pagano's mass law is the pushforward of the uniform measure on digit
strings — is a THEOREM for every totally ramified f = 1 window with
integral seat at every p, given Pagano's Theorem 1.4 and the digit
precision theorem (H1-H3); its instances rules at the cells read.
The third point at e = 4 is a RULE, exhaustive (H4, PR6). The ANF
rows are records of the computation at e = 4 (exhaustive) and e = 8
to level 20 (exhaustive over w_1..w_12).

RUN RECORD. python prime/code/memwatch.py prime/code/explore_hit_triangle.py:
158.7 s wall, peak working set 55.3 MB, 25,047 checks. No pre-green
fault; one dead line (a first draft of the third-point extraction by
position, superseded by the extraction by order) deleted before the
run.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import random
import sys
import time
from fractions import Fraction
from itertools import product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_jump_digits as jd  # noqa: E402
import explore_jump_haar as jh  # noqa: E402

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("FAIL:", msg)
        sys.exit(1)


# ------------------------------------------------------------ the objects

def geometry(p, e):
    istar = e // (p - 1)
    c0, M = jd.seat_split(p, istar)
    estar = p * istar
    cap = estar + (M - 1) * e + 1 if M >= 1 else estar
    return istar, c0, M, estar, cap


def pullback(p, e, estar, L):
    a, b = L, 0
    while not (a == estar or (a < estar and a % p)):
        a = a // p if a < estar else a - e
        b += 1
    return a, b


def hit_vector(p, e, wdig):
    """{level: hit digit} for every hit of the greedy dlog of zeta_p
    below CAP, the seat included; None at the closed gate."""
    istar, c0, M, estar, cap = geometry(p, e)
    N = cap + e + 2
    R = jd.DigitRing(p, e, wdig, N)
    u = R.zeta_p(istar)
    if u is None:
        return None
    hits = {}
    cache = {}
    while True:
        i = R.val(R.sub(u, R.one))
        if i >= cap:
            break
        a, b = pullback(p, e, estar, i)
        if (a, b) not in cache:
            inv = R.inv(R.pow(R.mono(1, a), p ** b))
            pw = [R.one]
            for _ in range(p - 1):
                pw.append(R.mul(pw[-1], inv))
            cache[(a, b)] = pw
        for d in range(1, p):
            u2 = R.mul(u, cache[(a, b)][d])
            if R.val(R.sub(u2, R.one)) > i:
                u = u2
                hits[i] = d
                break
        else:
            ok(False, "no digit raises weight %d" % i)
    return hits


def records(p, e, hits):
    """The record reading of a hit set: the frontier as a sorted tuple
    of (a, order)."""
    istar, c0, M, estar, cap = geometry(p, e)
    seen = set()
    front = []
    best = None
    for L in sorted(hits):
        a, b = pullback(p, e, estar, L)
        if a in seen:
            continue
        seen.add(a)
        order = b + 1
        if best is None or order < best:
            front.append((a, order))
            best = order
    return tuple(sorted(front))


def vec(p, e, hits):
    istar, c0, M, estar, cap = geometry(p, e)
    return tuple(hits.get(L, 0) for L in range(istar + 1, cap))


def string_from_int(p, Me, k):
    digs = [1]
    for _ in range(Me):
        digs.append(k % p)
        k //= p
    return digs


def padded(p, e, digs):
    istar, c0, M, estar, cap = geometry(p, e)
    return list(digs) + [0] * (cap + 3 - len(digs))


# ------------------------------------------------------------ the ANF

def anf(table, r):
    """Moebius transform: table[k] = f(w_1..w_r) with bit j-1 of k = w_j;
    returns the set of monomials (as bitmasks) with coefficient 1."""
    t = list(table)
    n = 1 << r
    for j in range(r):
        bit = 1 << j
        for k in range(n):
            if k & bit:
                t[k] ^= t[k ^ bit]
    return {k for k in range(n) if t[k]}


def mono_str(mask):
    if mask == 0:
        return "1"
    return "".join("w%d" % (j + 1) for j in range(mask.bit_length()) if mask >> j & 1)


def anf_str(monos):
    return " + ".join(mono_str(m) for m in sorted(monos, key=lambda m: (bin(m).count("1"), m)))


# ------------------------------------------------------------ the mass recursion

def pushforward(p, e):
    """{frontier: mass} of the record reading under independent uniform
    hit digits at every level in (i*, CAP)."""
    istar, c0, M, estar, cap = geometry(p, e)
    hit_p = Fraction(p - 1, p)
    states = {(frozenset([c0]), ((c0, M + 1),), M + 1): Fraction(1)}
    for L in range(istar + 1, cap):
        a, b = pullback(p, e, estar, L)
        nxt = {}
        for (mask, front, best), m in states.items():
            if a in mask:
                nxt[(mask, front, best)] = nxt.get((mask, front, best), 0) + m
                continue
            nxt[(mask, front, best)] = nxt.get((mask, front, best), 0) + m * (1 - hit_p)
            order = b + 1
            mask2 = mask | {a}
            if order < best:
                key = (mask2, front + ((a, order),), order)
            else:
                key = (mask2, front, best)
            nxt[key] = nxt.get(key, 0) + m * hit_p
        states = nxt
    out = {}
    for (mask, front, best), m in states.items():
        fr = tuple(sorted(front))
        out[fr] = out.get(fr, 0) + m
    return out


# ------------------------------------------------------------ the stages

def stage_controls():
    print("[PR7] controls")
    hits = hit_vector(2, 2, padded(2, 2, [1, 0, 0]))
    ok(vec(2, 2, hits) == (1, 1) and records(2, 2, hits) == ((1, 2), (3, 1)),
       "x^2-2 control: %s %s" % (hits, records(2, 2, hits)))
    front, dig, cap, F = jd.engine_read("zeta8", 2, [2, 4, 6, 4, 1])
    hits = hit_vector(2, 4, dig)
    ok(vec(2, 4, hits) == (0,) * 8 and records(2, 4, hits) == ((1, 3),),
       "zeta8 control: %s" % hits)
    table = [vec(2, 2, hit_vector(2, 2, padded(2, 2, string_from_int(2, 2, k))))[0]
             for k in range(4)]
    a3 = anf([table[k] for k in range(2)], 1)
    ok(a3 == {0, 1}, "e = 2 ANF of h_3 is %s" % anf_str(a3))
    print("  controls hit\n")


def stage_exhaustive():
    print("[PR1, PR3, PR5, PR6] the exhaustive cells")
    tables = {}
    for p, e in ((2, 2), (2, 4), (3, 6)):
        istar, c0, M, estar, cap = geometry(p, e)
        Me = M * e
        seen = {}
        fronts = {}
        third = {}
        for k in range(p ** Me):
            digs = string_from_int(p, Me, k)
            hits = hit_vector(p, e, padded(p, e, digs))
            v = vec(p, e, hits)
            ok(v not in seen, "(%d, %d): strings %s and %s share hit vector %s"
               % (p, e, seen.get(v), digs, v))
            seen[v] = digs
            ok(all(istar <= L < cap for L in hits), "(%d, %d): a hit off [i*, CAP)" % (p, e))
            fr = records(p, e, hits)
            df, _h, _c = jd.digit_frontier(p, e, padded(p, e, digs))
            ok(fr == df, "(%d, %d) string %s: records %s, frontier %s" % (p, e, digs, fr, df))
            fronts[fr] = fronts.get(fr, 0) + 1
            if p == 2 and e == 4:
                pts = sorted(fr, key=lambda t: -t[1])
                third[tuple(digs[1:])] = pts[2] if len(pts) > 2 else None
            tables[(p, e)] = tables.get((p, e), {})
            tables[(p, e)][tuple(digs[1:])] = v
        print("  (p, e) = (%d, %d): %d strings, %d hit vectors, %d jump sets, %d levels in (i*, CAP)"
              % (p, e, p ** Me, len(seen), len(fronts), cap - istar - 1))
        ok(cap - istar - 1 == Me, "level count %d is not Me = %d" % (cap - istar - 1, Me))
        if p == 2 and e == 4:
            n7 = sum(1 for d, t in third.items() if t == (7, 1))
            n8 = sum(1 for d, t in third.items() if t == (8, 1))
            n0 = sum(1 for d, t in third.items() if t is None)
            ok(all((t == (7, 1)) == (d[0] == d[1] == d[2] == 0) for d, t in third.items()),
               "the (7, 1) third point is not w_1 = w_2 = w_3 = 0")
            ok(all((t == (8, 1)) == (d[0] == d[1] == 0 and d[2] == 1 and d[3] == 0)
                   for d, t in third.items()),
               "the (8, 1) third point is not w_1 = w_2 = 0, w_3 = 1, w_4 = 0")
            ok((n7, n8, n0) == (32, 16, 208), "third-point counts %s" % ((n7, n8, n0),))
            print("  [PR6] e = 4: third point (7, 1) at %d strings, (8, 1) at %d, absent at %d"
                  % (n7, n8, n0))
    return tables


def stage_anf(tables):
    print("\n[PR5] the algebraic normal forms at p = 2")
    hand = {(2, 5): {1}, (2, 6): {2, 0}, (2, 7): {4, 2, 1, 0}, (2, 8): {8, 0, 1, 2, 3}}
    # e = 8: h_9..h_20 over w_1..w_12
    t8 = {}
    for k in range(2 ** 12):
        digs = string_from_int(2, 12, k)
        hits = hit_vector(2, 8, padded(2, 8, digs))
        t8[tuple(digs[1:])] = vec(2, 8, hits)
    tables[(2, 8)] = t8
    for e, rmax in ((2, 2), (4, 8), (8, 12)):
        istar = e
        table = tables[(2, e)]
        n = len(next(iter(table)))
        print("  e = %d:" % e)
        for r in range(1, rmax + 1):
            # f(w_1..w_r): read at strings with w_(>r) = 0, then check no dependence
            f = [0] * (1 << r)
            for k in range(1 << r):
                digs = tuple((k >> j) & 1 for j in range(r)) + (0,) * (n - r)
                f[k] = table[digs][r - 1]
            monos = anf(f, r)
            ok((1 << (r - 1)) in monos, "e = %d: h_%d lacks the diagonal w_%d" % (e, istar + r, r))
            deg = max(bin(m).count("1") for m in monos)
            key = (e, istar + r)
            if key in hand:
                ok(monos == hand[key], "e = %d: h_%d is %s, hand %s"
                   % (e, istar + r, anf_str(monos), anf_str(hand[key])))
            print("    h_%-2d = %s   (degree %d%s)" % (istar + r, anf_str(monos), deg,
                                                       ", hand" if key in hand else ""))


def stage_diagonal(rng):
    print("\n[PR2, PR3] the diagonal at sampled strings")
    cells = [(2, 8, 100), (2, 12, 40), (2, 16, 12), (3, 12, 60), (3, 18, 12), (5, 20, 15),
             (3, 6, 60), (2, 4, 60)]
    total = 0
    for p, e, n in cells:
        istar, c0, M, estar, cap = geometry(p, e)
        Me = M * e
        for _ in range(n):
            digs = [1] + [rng.randrange(p) for _ in range(Me)]
            base = hit_vector(p, e, padded(p, e, digs))
            ok(records(p, e, base) == jd.digit_frontier(p, e, padded(p, e, digs))[0],
               "(%d, %d): records off the frontier" % (p, e))
            for r in range(1, Me + 1):
                L = istar + r
                seen = set()
                for d in range(p):
                    v = list(digs)
                    v[r] = d
                    h = hit_vector(p, e, padded(p, e, v))
                    ok({k: x for k, x in h.items() if k < L} == {k: x for k, x in base.items() if k < L},
                       "(%d, %d) r = %d: a digit change moved a hit below level %d" % (p, e, r, L))
                    seen.add(h.get(L, 0))
                ok(len(seen) == p, "(%d, %d) r = %d: hit digits at level %d are %s, not F_%d"
                   % (p, e, r, L, sorted(seen), p))
                total += 1
        print("  (p, e) = (%d, %d) c_0 = %d M = %d Me = %-2d: %d strings, every digit a unit on its level"
              % (p, e, c0, M, Me, n))
    print("  %d (string, digit) pairs, each a permutation of F_p at its level" % total)


def stage_mass():
    print("\n[PR4] the mass law as the pushforward of uniform hit digits")
    for p, e in ((2, 2), (2, 4), (2, 8), (2, 12), (3, 6), (3, 12)):
        pf = pushforward(p, e)
        law = jh.law(p, e)
        ok(set(pf) == set(law), "(%d, %d): classes differ: %d pushforward, %d law, %s"
           % (p, e, len(pf), len(law), set(pf) ^ set(law)))
        off = [fr for fr in law if pf[fr] != law[fr]]
        ok(not off, "(%d, %d): %d masses off, e.g. %s: %s vs %s"
           % (p, e, len(off), off[:1], [pf[f] for f in off[:1]], [law[f] for f in off[:1]]))
        ok(sum(pf.values()) == 1, "(%d, %d): masses sum to %s" % (p, e, sum(pf.values())))
        top = sorted(pf.items(), key=lambda kv: -kv[1])[:3]
        print("  (p, e) = (%d, %d): %d classes, every mass the law's; largest %s"
              % (p, e, len(pf), ", ".join("%s %s" % (jd.fmt(fr), m) for fr, m in top)))


def run():
    t0 = time.time()
    rng = random.Random(1180)
    print("THE HIT TRIANGLE")
    print("=" * 64)
    stage_controls()
    tables = stage_exhaustive()
    stage_anf(tables)
    stage_diagonal(rng)
    stage_mass()
    print("\nVERDICT: PR1-PR7 hit; %d checks, %.1f s" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    run()
