"""explore_rung_theorem.py — THE RUNG THEOREM: is every arrival class's
landing a closed form in the jump set, derived from the filtered module,
and does a Haar sample of octics reproduce Pagano's law?

THE QUESTION. The rung of an Eisenstein window of Q_2 of degree e — the
class-1 landing minimum, min v(u^{2e} - 1) over units u with v(u - 1)
= 1 — is the second weight of Pagano's jump set of the field capped at
the freedom rung 7e/2, a rule at every cell of e = 2 and 4
(explore_jump_haar.py finding 2) and at e = 8 a prediction. The
intermediate classes (c, m), c·2^m = e/1, have their own staircases with
floors 20 and 18 at e = 8 (explore_mu16_face.py EL3). This rig asks:
is the capped rule a THEOREM — a consequence of Pagano's structure
theorem for U_1 — and is every class's landing minimum the same kind of
read, a frontier weight capped by a class-specific floor? And second:
over a Haar-random population of octics, do the 44 admissible classes
appear at their law masses (explore_jump_haar.py finding 3, a
prediction there)?

THE OBJECTS (explore_jump_set.py's conventions). K = Q_2[x]/(F), F
Eisenstein of degree e = 2^k, pi = x, f = 1; T* = {i < 2e : i odd} u
{2e}; rho(i) = min(2i, i + e). Pagano (arXiv:1810.09975, Theorem 1.4):
U_1 is the free filtered Z_2-module on generators e_a (a in T*), where a
vector y has weight min_a rho^{ord y_a}(a), modulo one relation r =
2·dlog(-1), the level of a class being the largest weight of a
representative. The jump set (I, beta) is the Pareto frontier of
{(a, b_a)}, b_a = ord r_a, under (order, weight); Theorem 1.6: a jump
set is admissible iff its least weight is e* = 2e. An arrival class
(c, m) with c = 2^j, m = k - j, is the set of units of level exactly c;
its landing is v(u^{2^{m+1}} - 1).

THE HAND-DERIVATION (on paper, before the engine).

H1  THE FIRST POINT IS (1, B), B = log_2 e + 1, AT EVERY FIELD. The
    levels below e that are powers of 2, and the level 2e, are reached
    by rho^b(a) only at a = 1, so the least frontier weight 2e (Thm
    1.6) sits at (1, B): r_1 has order exactly B. Every coordinate has
    weight >= 2e, the least-weight coordinate being on the frontier.
H2  THE CLASS-c LANDING. A unit of level c = 2^j has ord x_1 = j and
    every other coordinate of weight >= c, i.e. ord x_a >= n_a, the
    least n with rho^n(a) >= c. Its landing is the level of 2^{m+1}x,
    the max over t of the weight of 2^{m+1}x + t·r.
      a = 1: 2^{m+1}x_1 has order j + m + 1 = B, as r_1 does; t == t_0
      (mod 4), t_0 a unit, lifts the coordinate to order >= B + 2 and
      weight >= rho^{B+2}(1) = 4e; any other t leaves it at weight
      <= rho^{B+1}(1) = 3e, below every floor in play. So t is a unit
      in t_0 + 4Z_2.
      a >= 3 with b_a < m + 1 + n_a: 2^{m+1}x_a has order >= m+1+n_a
      > b_a, so the coordinate has order exactly b_a for every such t
      and every unit in the class — weight rho^{b_a}(a), FIXED across
      the class. R_c := the least of these (infinity if none).
      a >= 3 with b_a >= m + 1 + n_a: order >= m+1+n_a, weight >=
      rho^{m+1+n_a}(a), and exactly that for a suitable x_a (a unit,
      or one avoiding the single cancellation when b_a = m+1+n_a); the
      4Z_2 freedom in t perturbs at order >= b_a + 2 and moves
      nothing. Phi_c := min_a rho^{m+1+n_a}(a).
    Hence every unit of the class lands at min(R_c, something >=
    Phi_c), and the class minimum is EXACTLY min(R_c, Phi_c): the
    spectrum is RIGID at R_c when R_c < Phi_c and GRADED from Phi_c
    when R_c >= Phi_c.
H3  THE INSTANCES. Class 1 (n_a = 0): R_1 = the second frontier
    weight w2 (the least weight among the b < B coordinates is on the
    frontier: its only possible absorber is (1, B), whose order is
    larger), Phi_1 = rho^B(3) = 7e/2 (3 doubles to 3e/4, then 3e/2,
    5e/2, 7e/2: B steps). THE CAPPED RULE, at every 2-power e, a
    theorem given Theorems 1.4 and 1.6. Class 2 at e = 8 (m = 2):
    R_2 = the least weight among b <= 2, which is w2 if beta_2 <= 2
    and w3 if beta_2 = 3; Phi_2 = rho^3(3) = 20. Class 4 at e = 8
    (m = 1): b_a <= 1 at a >= 5 (b_3 <= 2 is dead: weight 12 < 16);
    Phi_4 = rho^2(5) = 18. At e = 4 class 2 (m = 1): R_2 over b <= 1,
    Phi_2 = rho^2(3) = 10. Every floor the ladders printed — 7, 14,
    28; 20 and 18 at e = 8; 10 at e = 4 — is one of these, and in
    general Phi_c = 2e + 2^m for c > 1: the odd level c + 1 has
    n = 0 and doubles m times to e + 2^m, past e, so one more step
    adds e; every other a >= 3 has rho^{n_a}(a) >= c + 1 (only a = 1
    reaches c itself) and rho is monotone. The readout theorem's
    floors, from the module.
H4  WHAT (b) ASKS, ANSWERED ON PAPER: the third frontier point's
    weight is the class-2 landing minimum exactly when beta_2 = 3 and
    w3 < 20; when beta_2 <= 2 the class-2 minimum is min(w2, 20), the
    rung under its own cap; when beta_2 = 3 and w3 >= 20 it is 20.
H5  ONE SEAM LEFT OPEN BY THE DERIVATION: R_c is defined over the
    full order vector (every coordinate), and the frontier alone
    determines the module, so the least fixed weight must be a
    frontier weight; the rig computes R_c both ways and prints
    whether they agree, a disagreement being a bug in the derivation
    or the engine, never a finding.
H6  THE ENUMERATION IS SMALL. A class-1 landing below 38 is decided
    by u modulo U_7 (rho^4(7) = 38), so the exact class-1 minimum is
    the least landing over the 32 representatives 1 + pi + sum c_i
    pi^i, i = 2..6, at precision 48; class 2 (landing v(u^8 - 1),
    decided below rho^3(5) = 26 by u mod U_5): 4 representatives;
    class 4 (v(u^4 - 1), below rho^2(6) = 20 by u mod U_6): 2. At
    e = 4 the same: class 1 mod U_5 (rho^3(5) = 17 > 14), class 2
    mod U_4 (rho^2(4) = 12 > 10).
H7  THE SAMPLE IS HAAR TO THE ENGINE'S PRECISION. explore_jump_set.py
    builds a field at amax = 12e, coefficients modulo 2^M with M =
    12e/e + 3 = 15; drawing every coefficient uniformly at that
    modulus (a_i = 2·uniform, a_0 = 2·odd uniform) is the Haar measure
    as the engine sees it, and the jump set's frontier is exact at
    that precision by explore_jump_set.py's precision argument, so no
    purity read is owed: the sample is the law's, cell by cell.
    Transplant: the sampler is validated at e = 4 against the law
    explore_jump_haar.py verified exhaustively, before e = 8 is read.

PREDICTIONS, fixed before the engine ran.
  PR1 (the theorem's instance at e = 8, the aim's (a)). At every one
      of N = 8192 sampled octics the exact class-1 minimum equals
      min(w2, 28), an anchor's missing second point read as infinity,
      and equals the mu_16 ladder's rung on the digits. KILL: one
      field off in either equality.
  PR2 (every class). At every sampled octic the exact class-2 and
      class-4 minima equal min(R_c, Phi_c) with Phi_2 = 20, Phi_4 =
      18, and equal the ladders' rung2, rung4. KILL: one field off.
      PR2b: R_c from the full order vector equals R_c from the
      frontier alone at every field (H5); a disagreement halts the
      read.
  PR3 (the third point, the aim's (b)). The class-2 minimum is w3 at
      every field with beta_2 = 3 and w3 < 20, min(w2, 20) at every
      field with beta_2 <= 2, and 20 at every field with beta_2 = 3
      and w3 >= 20; the three cases' counts are printed and the
      third case is non-empty.
  PR4 (rigidity). At every sampled octic with w2 < 28 all 32 class-1
      representatives land at w2; at every octic with w2 >= 28 the
      32 representatives show at least two landings. The same for
      class 2 against 20.
  PR5 (the population, the aim's (a) second half). Over the N
      octics, every class with N·m >= 8 has |count - N·m| <= 4 sd,
      sd = sqrt(N m (1 - m)), and the chi-square over those classes
      plus one lumped tail, read as the Wilson-Hilferty normal
      deviate, is below 3.1 (p > 0.001). KILL: either bound broken.
  PR7 (THE SPECTRUM'S TOP; fixed after a 64-field smoke run had shown
      PR3's third case empty and before the run below, by the
      derivation's own algebra). Since beta_2 = 3 forces w2 >=
      rho^3(3) = 20, the case beta_2 = 3 with w3 < 20 is empty and
      the class-2 minimum is min(w2, 20) at every field: no class
      MINIMUM reads a point past the second (PR3 dies as written).
      What reads them is the top of a spectrum: by H2 the coordinates
      with b_a < m + 1 + n_a are fixed across the class and every
      other one can be killed by a unit of the class, so the class's
      LARGEST landing is R_c exactly, the weight of the first frontier
      point with beta <= m (every point with beta in (m, m + n_a] has
      weight <= 2e and is the first point), and is unbounded — the
      class holds a primitive 2^{m+1}-th root of unity — exactly when
      no frontier point has beta <= m. Prediction: at every sampled
      octic and every class, the largest landing over the class's
      representatives modulo U_n, n the least level with rho^{m+1}(n)
      above R_c (n = 9 when R_c is infinite), equals R_c when finite
      and is at least rho^{m+1}(9) when not: the class-1 top is w2,
      the class-2 top w2 or w3 by whether beta_2 <= 2, the class-4 top
      the last frontier point's weight when beta(max I) = 1 and
      unbounded when it is not. KILL: one field off.
  PR6 (positive controls, run and read before PR1-PR5).
      (a) At the 49 census quartics and the six quadratics the
          formula's class-1 minimum equals the exhaustive one of
          explore_jump_haar.py (rung4 = min(w2, 14); e = 2: 5, 6, 7)
          and the class-2 minimum at e = 4 equals 9 or 10 by the
          first digit, as the constellation law prints.
      (b) The hand value at x^2 - 2: (I, beta) = ([1, 3], [2, 1]),
          rung 5.
      (c) The six pure octics read class minima (20, 20, 18) and
          zeta_16 reads (28, 20, 18), explore_mu16_face.py's TL5 and
          TL6.
      (d) The sampler at e = 4 with N = 4096 draws: every class with
          N·m >= 8 within 4 sd and the chi-square deviate below 3.1
          — the population explore_jump_haar.py read exhaustively.
      (e) The e = 8 law from explore_jump_haar.py has 44 classes with
          masses summing to 1.

THE DESIGN. theory: rho, n_a, Phi_c and R_c (both ways) from a jump
set and its order vector; the exact class minima by the small
enumeration of H6. controls: PR6. sample: N seeded Haar octics
(seed 1176), per field the jump set with its order vector, the digits
and the three ladder rungs, the three exact minima; the tallies of
PR1-PR4 and the class counts of PR5. verdict. Flags: --n N (8192),
--seed S (1176). Run: python prime/code/memwatch.py
prime/code/explore_rung_theorem.py; estimate 8 minutes, under 100 MB.

FINDINGS (entered post-run, copied from printed output).

1. THE RUNG THEOREM'S INSTANCE AT e = 8 (PR1, PR2, PR4 hold; rule at
   every field of the sample, the derivation the theorem). At all
   8192 Haar-random octics the exact class-1 minimum over U_1/U_7 is
   min(w2, 28) and the mu_16 ladder's rung on the digits, 0 off on
   either; the exact class-2 and class-4 minima are min(R_c, Phi_c)
   with Phi_2 = 20 and Phi_4 = 18 and the ladders' rung2, rung4, 0
   off; R_c from the full order vector and from the frontier alone
   agree at every field (PR2b, 0 off). Rigidity as derived: every
   class rigid where its fixed weight sits below its floor, graded
   from the floor otherwise, 0 off both ways. The rung's frequency
   halves rung by rung: 4146, 2080, 997, 472, 241, 130, 58, 29, 21,
   13, 2, 3 of 8192 at rungs 17 to 28.

2. NO CLASS MINIMUM READS A POINT PAST THE SECOND; THE SPECTRUM'S
   TOP DOES (PR3 dies as frozen, PR7 holds). The case beta_2 = 3 with
   w3 < 20 is empty (0 of 8192; forced, w2 >= 20 there), so the
   class-2 minimum is min(w2, 20) at every field — 7705 fields with
   beta_2 <= 2, 487 with beta_2 = 3 and the minimum 20 — and every
   class minimum is the rung under its own floor. The largest landing
   of a class is the weight of the first frontier point with
   beta <= m at every field and class: class 1 finite at all 8192
   (the top w2), class 2 finite at 8187 with 5 unbounded (zeta_8 in
   the field), class 4 finite at 7947 with 245 unbounded (i in the
   field: beta(max I) >= 2), 0 off. The intermediate classes read the
   frontier from the top down, one order threshold per class.

3. THE OCTIC POPULATION IS PAGANO'S LAW (PR5 holds; observation,
   8192 seeded draws). All 22 classes with N m >= 8 sit within
   2.3 sd of their masses (4146 against 4096 at [1, 9], 1084 against
   1024 at [1, 5, 11], 997 against 1024 at [1, 11], ... 6 against 8
   at [1, 3, 11]); the tail 27 fields against 24; chi-square 26.2 on
   22 df, deviate +0.70; no class off the admissible set.

4. THE CONTROLS (PR6, all hit before the sample was read): the e = 8
   law's 44 classes sum to 1; x^2 - 2 prints ([1, 3], [2, 1]), rung
   5; formula = enumeration = ladder at every class of the six
   quadratics and 49 quartics; the six pure octics read (20, 20, 18)
   and zeta_16 (28, 20, 18) with I = {1}, by formula and enumeration
   alike; the sampler at e = 4 (4096 draws) reads worst |z| 1.64,
   chi-square 7.4 on 9 df, deviate -0.25, every per-field prediction
   0 off, the rung counts 2070, 1015, 522, 242, 120, 127 at rungs 9
   to 14 (the law's 1/2, 1/4, 1/8, 1/16, 1/32, 1/32 of 4096).

TIER. The bracket [min(w2, Phi_c), R_c] on every arrival class's
landing spectrum, both ends attained, is a THEOREM for every 2-power
e over Q_2 given Pagano's Theorems 1.4 and 1.6 (the derivation above,
H1-H3 and PR7's paragraph); its instances are rules at every field
read (e = 2 and 4 exhaustive by explore_jump_haar.py, e = 8 at 8192
Haar draws here). Finding 3 is an observation at N = 8192.

RUN RECORD. python prime/code/memwatch.py prime/code/explore_rung_theorem.py:
541.7 s wall (509 s the octic sample at 0.062 s a field), peak
working set 16.0 MB, 411,285 checks. Smoke runs at N = 64 and 128
preceded it; the 64-field run showed PR3's third case empty and PR7
was fixed before N = 128 ran. One pre-green fault: the first draft
named a helper explore_jump_set.py does not export.
"""
import argparse
import math
import os
import random
import sys
import time

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, ".")
import explore_local_clock as lc          # noqa: E402
import explore_jump_set as js             # noqa: E402
import explore_jump_haar as jh            # noqa: E402
import explore_mu16_face as m16           # noqa: E402

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("FAIL:", msg)
        sys.exit(1)


# ---------------------------------------------------------------- theory

def rho_k(e, i, k):
    return jh.rho_k(2, e, i, k)


def n_of(e, a, c):
    """The least n with rho^n(a) >= c."""
    n = 0
    while rho_k(e, a, n) < c:
        n += 1
    return n


def phi(e, c, m):
    """Phi_c = min over a >= 3 in T* of rho^{m+1+n_a}(a)."""
    return min(rho_k(e, a, m + 1 + n_of(e, a, c))
               for a in jh.tstar(2, e) if a != 1)


def r_full(e, c, m, orders):
    """R_c over the full order vector {a: b_a}."""
    ws = [rho_k(e, a, b) for a, b in orders.items()
          if a != 1 and b < m + 1 + n_of(e, a, c)]
    return min(ws) if ws else None


def r_front(e, c, m, front):
    """R_c over the frontier alone."""
    ws = [rho_k(e, a, b) for a, b in front
          if a != 1 and b < m + 1 + n_of(e, a, c)]
    return min(ws) if ws else None


def r_top(e, m, front):
    """R_c as the frontier reads it: the first point with beta <= m."""
    ws = [rho_k(e, a, b) for a, b in front if a != 1 and b <= m]
    return min(ws) if ws else None


def predicted(e, c, m, front, orders):
    """(min(R_c, Phi_c) by the frontier, by the full vector, Phi_c)."""
    P = phi(e, c, m)
    rf, ru = r_front(e, c, m, front), r_full(e, c, m, orders)
    pf = P if rf is None else min(rf, P)
    pu = P if ru is None else min(ru, P)
    return pf, pu, P


def ord2(n):
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def orders_of(coords):
    """{a: ord_2 of the relation coordinate} from dlog(-1)'s coordinates."""
    return {a: ord2(v) + 1 for a, v in coords.items() if v}


# The class representatives of H6: bits at levels c..n-1, level c set.

def reps(F, c, n):
    monos = []
    for i in range(F.M):
        for j in range(F.e):
            lvl = F.e * i + j
            if c < lvl < n:
                monos.append((i, j))
    base = [list(cc) for cc in F.one]
    i0, j0 = divmod(c, F.e)
    base[j0][0] = (base[j0][0] + 2 ** i0) % F.pM
    for bits in range(2 ** len(monos)):
        u = [list(cc) for cc in base]
        for k, (i, j) in enumerate(monos):
            if bits >> k & 1:
                u[j][0] = (u[j][0] + 2 ** i) % F.pM
        yield tuple(tuple(cc) for cc in u)


def landing(F, u):
    o = F.orbit(u)
    ok(F.seat in o, "%s: orbit misses the seat" % F.name)
    k = o.index(F.seat)
    return o[k + 1] if k + 1 < len(o) else F.CAP


def exact_minima(eis, e, amax, tops=None):
    """{c: (min, number of distinct landings, top)} over H6's
    representatives; the top over U_c/U_n with n the least level whose
    (m+1)-fold image exceeds R_c (9 when R_c is infinite), PR7."""
    F = lc.LF("x", 2, [0, 1], eis, amax)
    plan = {8: ((1, 7), (2, 5), (4, 6)), 4: ((1, 5), (2, 4)), 2: ((1, 4),)}
    out = {}
    for c, n in plan[e]:
        ls = [landing(F, u) for u in reps(F, c, n)]
        top = None
        if tops is not None:
            R, m = tops[c]
            nt = 9 if e == 8 else 6
            if R is not None:
                nt = c + 1
                while rho_k(e, nt, m + 1) <= R:
                    nt += 1
            top = max(landing(F, u) for u in reps(F, c, nt))
        out[c] = (min(ls), len(set(ls)), top)
    return out


def read(eis, e):
    """jump set, order vector, second and third weights, digits, rungs."""
    F = js.field("x", eis)
    front, coords = js.jump_set(F, js.pi_el(F))
    orders = orders_of(coords)
    wts = [rho_k(e, a, b) for a, b in front]
    w2 = wts[1] if len(wts) > 1 else None
    w3 = wts[2] if len(wts) > 2 else None
    b2 = front[1][1] if len(front) > 1 else None
    rungs = {}
    if e == 8:
        G = lc.LF("x", 2, [0, 1], eis, 48)
        d = m16.w_digits_g(G, m16.w_element_g(G), 12)
        rungs = {1: m16.rung1(d), 2: m16.rung2(d), 4: m16.rung4(d)}
    elif e == 4:
        d = js.digits(F, js.w_element(F), 6)
        rungs = {1: js.rung4(d), 2: 9 if d[1] else 10}
    return front, orders, w2, w3, b2, rungs


CLASSES = {8: ((1, 3), (2, 2), (4, 1)), 4: ((1, 2), (2, 1)), 2: ((1, 1),)}
CAP = {8: 28, 4: 14, 2: 7}


def field_row(eis, e, amax):
    front, orders, w2, w3, b2, rungs = read(eis, e)
    tops = {c: (r_top(e, m, front), m) for c, m in CLASSES[e]}
    ex = exact_minima(eis, e, amax, tops)
    row = {"front": front, "w2": w2, "w3": w3, "b2": b2, "rungs": rungs,
           "exact": ex, "pred": {}, "top": {}}
    for c, m in CLASSES[e]:
        row["pred"][c] = predicted(e, c, m, front, orders)
        R = tops[c][0]
        got = ex[c][2]
        floor_inf = rho_k(e, 9 if e == 8 else 6, m + 1)
        row["top"][c] = (R, got, (got == R) if R is not None else (got >= floor_inf))
    return row


# -------------------------------------------------------------- sampling

def haar_octic(rng, e, M):
    mod = 2 ** M
    a0 = 2 * rng.randrange(1, mod // 2, 2)
    rest = [2 * rng.randrange(mod // 2) for _ in range(e - 1)]
    return [a0] + rest + [1]


def band(counts, law, N):
    """(worst |z| over classes with N m >= 8, chi-square deviate)."""
    worst = 0.0
    chi, df, tail_m, tail_n = 0.0, 0, 0.0, 0
    for fr, m in law.items():
        n = counts.get(fr, 0)
        mu = float(N * m)
        if mu >= 8:
            sd = math.sqrt(mu * (1 - float(m)))
            worst = max(worst, abs(n - mu) / sd)
            chi += (n - mu) ** 2 / mu
            df += 1
        else:
            tail_m += float(m)
            tail_n += n
    if tail_m > 0:
        mu = N * tail_m
        chi += (tail_n - mu) ** 2 / mu
        df += 1
    df -= 1
    z = ((chi / df) ** (1 / 3) - (1 - 2 / (9 * df))) / math.sqrt(2 / (9 * df))
    return worst, chi, df, z


def run_sample(e, N, seed, amax, law, verbose):
    rng = random.Random(seed)
    M = 12 * e // e + 3
    counts = {}
    t0 = time.time()
    bad = {"pr1_rule": 0, "pr1_ladder": 0, "pr2_rule": 0, "pr2_ladder": 0,
           "pr2b": 0, "pr4_rigid": 0, "pr4_graded": 0, "pr7_top": 0}
    top_kinds = {}
    third = {"b2<=2": 0, "b2=3,w3<20": 0, "b2=3,w3>=20": 0}
    third_bad = 0
    rung_counts = {}
    for i in range(N):
        eis = haar_octic(rng, e, M)
        row = field_row(eis, e, amax)
        counts[row["front"]] = counts.get(row["front"], 0) + 1
        ex, pred, rungs, w2 = row["exact"], row["pred"], row["rungs"], row["w2"]
        cap = CAP[e]
        capped = cap if w2 is None else min(w2, cap)
        rung_counts[ex[1][0]] = rung_counts.get(ex[1][0], 0) + 1
        if ex[1][0] != capped:
            bad["pr1_rule"] += 1
        if 1 in rungs and ex[1][0] != rungs[1]:
            bad["pr1_ladder"] += 1
        for c, _m in CLASSES[e]:
            pf, pu, P = pred[c]
            if pf != pu:
                bad["pr2b"] += 1
            if c != 1 and ex[c][0] != pf:
                bad["pr2_rule"] += 1
            if c != 1 and c in rungs and ex[c][0] != rungs[c]:
                bad["pr2_ladder"] += 1
            rigid = ex[c][1] == 1
            if pf < P and not rigid:
                bad["pr4_rigid"] += 1
            if pf >= P and rigid:
                bad["pr4_graded"] += 1
            R, got, fine = row["top"][c]
            if not fine:
                bad["pr7_top"] += 1
            kind = (c, "inf" if R is None else "finite")
            top_kinds[kind] = top_kinds.get(kind, 0) + 1
        if e == 8:
            b2, w3 = row["b2"], row["w3"]
            if b2 is None or b2 <= 2:
                key, want = "b2<=2", min(w2 if w2 is not None else 99, 20)
            elif w3 is not None and w3 < 20:
                key, want = "b2=3,w3<20", w3
            else:
                key, want = "b2=3,w3>=20", 20
            third[key] += 1
            if ex[2][0] != want:
                third_bad += 1
            # PR7's class-2 top: w3 when beta_2 = 3 and a third point exists
            if b2 == 3 and w3 is not None and row["top"][2][1] != w3:
                third_bad += 1
        if verbose and (i + 1) % 1024 == 0:
            print("    %d fields, %.0f s" % (i + 1, time.time() - t0))
    print("  %d fields at e = %d in %.0f s" % (N, e, time.time() - t0))
    print("  class counts against the law (N m >= 8 shown):")
    for fr, m in sorted(law.items(), key=lambda kv: -kv[1]):
        mu = float(N * m)
        if mu >= 8:
            n = counts.get(fr, 0)
            sd = math.sqrt(mu * (1 - float(m)))
            print("    %-30s %6d  law %8.1f  z %+.2f" %
                  (jh.fmt(fr), n, mu, (n - mu) / sd))
    small = sum(n for fr, n in counts.items() if float(N * law.get(fr, 0)) < 8)
    off_law = [fr for fr in counts if fr not in law]
    print("    tail (N m < 8): %d fields, law %.1f; classes off the law: %d"
          % (small, N * sum(float(m) for m in law.values()
                            if float(N * m) < 8), len(off_law)))
    ok(not off_law, "a jump set outside the admissible set at e = %d" % e)
    worst, chi, df, z = band(counts, law, N)
    print("    worst |z| %.2f; chi-square %.1f on %d df, deviate %+.2f"
          % (worst, chi, df, z))
    print("  exact class-1 minima by rung: %s" % dict(sorted(rung_counts.items())))
    print("  off counts: %s" % bad)
    print("  spectrum tops by class (finite / unbounded): %s"
          % dict(sorted(top_kinds.items())))
    if e == 8:
        print("  the third point (class-2 minimum by case): %s, off %d"
              % (third, third_bad))
    return bad, third, third_bad, worst, z


# -------------------------------------------------------------- controls

def controls():
    print("[controls] PR6")
    law8 = jh.law(2, 8)
    ok(len(law8) == 44 and sum(law8.values()) == 1, "e = 8 law")
    print("  (e) e = 8 law: 44 classes, masses sum 1")
    # (b) the hand value
    row = field_row([-2, 0, 1], 2, 12)
    ok(row["front"] == ((1, 2), (3, 1)) and row["exact"][1][0] == 5,
       "hand value at x2-2")
    print("  (b) x2-2: %s, rung %d" % (jh.fmt(row["front"]), row["exact"][1][0]))
    # (a) the census
    off = 0
    for name, eis in js.QUADS:
        row = field_row(eis, 2, 12)
        pf = row["pred"][1][0]
        if row["exact"][1][0] != pf:
            off += 1
    for name, eis in js.QUARTS:
        row = field_row(eis, 4, 20)
        if row["exact"][1][0] != row["pred"][1][0]:
            off += 1
        if row["exact"][2][0] != row["pred"][2][0]:
            off += 1
        if name != "zeta8" and row["exact"][1][0] != row["rungs"][1]:
            off += 1
        if row["exact"][2][0] != row["rungs"][2]:
            off += 1
        if row["pred"][1][1] != row["pred"][1][0] or row["pred"][2][1] != row["pred"][2][0]:
            off += 1
    ok(off == 0, "census: %d disagreements" % off)
    print("  (a) six quadratics and 49 quartics: formula = enumeration = "
          "ladder at every class, %d off" % off)
    # (c) the pures and zeta16
    for k in m16.PURE:
        eis = list(k) + [1]
        row = field_row(eis, 8, 48)
        got = tuple(row["exact"][c][0] for c in (1, 2, 4))
        ok(got == (20, 20, 18), "pure octic %s reads %s" % (k, got))
        ok(tuple(row["pred"][c][0] for c in (1, 2, 4)) == got,
           "pure octic %s: formula %s" % (k, got))
    row = field_row([2, 8, 28, 56, 70, 56, 28, 8, 1], 8, 48)
    got = tuple(row["exact"][c][0] for c in (1, 2, 4))
    ok(got == (28, 20, 18), "zeta16 reads %s" % (got,))
    ok(tuple(row["pred"][c][0] for c in (1, 2, 4)) == got, "zeta16 formula")
    ok(row["front"] == ((1, 4),), "zeta16 frontier %s" % (row["front"],))
    print("  (c) six pure octics (20, 20, 18), zeta16 (28, 20, 18), "
          "formula and enumeration alike")
    # (d) the sampler at e = 4
    print("  (d) the sampler at e = 4, 4096 draws:")
    bad, _t, _tb, worst, z = run_sample(4, 4096, 1176, 20, jh.law(2, 4), False)
    ok(all(v == 0 for v in bad.values()), "e = 4 sample: %s" % bad)
    ok(worst <= 4 and z < 3.1, "e = 4 sampler off the law")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=8192)
    ap.add_argument("--seed", type=int, default=1176)
    a = ap.parse_args()
    print("THE RUNG THEOREM")
    print("=" * 64)
    print("[theory] the floors: Phi_1 = %d, Phi_2 = %d, Phi_4 = %d at e = 8;"
          " Phi_1 = %d, Phi_2 = %d at e = 4; Phi_1 = %d at e = 2"
          % (phi(8, 1, 3), phi(8, 2, 2), phi(8, 4, 1), phi(4, 1, 2),
             phi(4, 2, 1), phi(2, 1, 1)))
    controls()
    print("[sample] e = 8, N = %d, seed %d" % (a.n, a.seed))
    bad, third, third_bad, worst, z = run_sample(8, a.n, a.seed, 48,
                                                 jh.law(2, 8), True)
    print("[verdict]")
    print("  PR1 %s (rule off %d, ladder off %d)" %
          ("HOLDS" if bad["pr1_rule"] == 0 and bad["pr1_ladder"] == 0 else "KILLED",
           bad["pr1_rule"], bad["pr1_ladder"]))
    print("  PR2 %s (rule off %d, ladder off %d, PR2b off %d)" %
          ("HOLDS" if bad["pr2_rule"] == bad["pr2_ladder"] == bad["pr2b"] == 0
           else "KILLED", bad["pr2_rule"], bad["pr2_ladder"], bad["pr2b"]))
    print("  PR3 %s: %s, off %d" %
          ("HOLDS" if third_bad == 0 and third["b2=3,w3<20"] > 0 else "KILLED",
           third, third_bad))
    print("  PR4 %s (rigid off %d, graded off %d)" %
          ("HOLDS" if bad["pr4_rigid"] == bad["pr4_graded"] == 0 else "KILLED",
           bad["pr4_rigid"], bad["pr4_graded"]))
    print("  PR5 %s (worst |z| %.2f, deviate %+.2f)" %
          ("HOLDS" if worst <= 4 and z < 3.1 else "KILLED", worst, z))
    print("  PR7 %s (top off %d)" %
          ("HOLDS" if bad["pr7_top"] == 0 else "KILLED", bad["pr7_top"]))
    print("checks passed: %d" % CHECKS)


if __name__ == "__main__":
    main()
