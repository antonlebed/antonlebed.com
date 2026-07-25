"""THE CROSS-FIELD CLOCK — irreducibility critical temperatures across global fields.

The cross-field remainder of an earlier question. Earlier work built the interior
irreducibility clock beta_col (the depth column's condensation temperature);
it also showed the clock READS THE PLACE: every lock prime q of Q carries its own
beta_col^q, and the spectrum is Ostrowski's finite places of Q read
thermodynamically (explore_irreducibility_places.py). THIS script asks the
cross-FIELD question: is that a fact about Q, or about GLOBAL FIELDS?

  (i)  F_2[x] (rational zeta 1/(1-2x), x = 2^-beta): is the clock ALGEBRAIC —
       the clock equation a POLYNOMIAL in x?
  (ii) Z[sqrt(-5)] (h = 2, Dedekind zeta): does the clock SPLIT
       ideal-vs-element, and does the split read the class number?

THE OBJECTS. Depth column at a place: lock an irreducible/prime-ideal g,
states g^a. lambda = exponent of the unit group of the quotient. The thermal
D-DYN normalizer is the wall discount (explore_depth_observer.py finding 1):
Z_state = zeta_M - cofactor_sum = the ADMISSIBLE MASS (menu weight of the
non-transparent moves; -> inf at the zeta pole, -> 0 cold, one crossing);
the clock beta_col = interior root of Z = 1 in the deep-column limit.

FINDINGS (tiers per section; run record at bottom; predictions PR1-PR10 fixed
by hand and attacked BEFORE the run).

F0/F1 THE ALGEBRAIC CLOCK (the lambda/transparency structure: rule, brute-
verified in range; the clock equation: closed form). In F_2[x], lambda(g^a) =
(2^d - 1) * 2^ceil(log2 a) (d = deg g; char-2 Frobenius (1+w)^2 = 1+w^2 makes
the 1-unit clock exactly dyadic; brute: all g of deg <= 3 with deg g^a <= 9,
lcm law on ALL monic F of deg 6, the state lemma on 6 column states).
Transparency of h^j to the g-column: (2^e-1)2^ceil(log2 j) | (2^d-1)2^s <=>
e | d AND j <= 2^s — the transparent set is THE SUBFIELD LATTICE of the
residue field F_{2^d}, every member at UNBOUNDED exponent in the limit: the
ambient characteristic supplies every 2-part free (an earlier own-powers clause
is the WHOLE transparency structure in char 2). Limit cofactor C_d(x) =
prod_{e | d} (1-x^e)^-(N_e - [e=d]), so the clock equation zeta_M - C_d = 1
(zeta_M = 1/(1-2x)) CLEARS TO A POLYNOMIAL in x = 2^-beta: the critical
temperature of computational irreducibility over F_2(x) is -log2 of an
ALGEBRAIC NUMBER. d=1: 2x^2 - 4x + 1 = 0, x = 1 - 1/sqrt2 EXACTLY (assert
1e-9; the printed root matches to all 11 shown digits);
d=2: 2x^3 - 4x^2 + 4x - 1 = 0. The window is algebraic too: beta* (root of
zeta_M = 2) = 2 exactly (x = 1/4); every clock interior in (1, 2). The TYPE
of the critical temperature reads the global field: polynomial roots where Q
had zeta/Fermat-data roots.

F2 DEGREE IS THE WHOLE DIAL, WEIGHTED (rule in range for the sets; the
ordering observed). Same-degree columns share the clock EXACTLY (per-column
brute transparent sets identical for both deg-1 and both deg-3 irreducibles:
Frobenius symmetry, where Q's places were Fermat-idiosyncratic). The subfield
lattice orders the spectrum: e | d proper => beta_col(d) < beta_col(e); but
the dial is the transparent MASS, not the member count — the spectrum is
NON-MONOTONE in d (unfrozen surprise: beta_col(5) > beta_col(3) despite d=5's
6-member self-degree set vs d=3's 1, because x^5-weights are lighter than
x^3-weights near the root; prime degrees sit above their composite
neighbors). THE SEAT: deg-1 (residue field F_2) is the spectrum max.

F3 THE BREATHING IS A RAMIFICATION LAW (rule, proved by the ceiling formula;
verified at finite a). The wall ticks on the 1-UNIT CLOCK c(a) =
ceil(log2 a) while the state ticks on a, so the cofactor never converges
plainly: along a = 2^s it falls to C_d, along a = 2^s + 1 it rises toward
C_d/(1 - x^d) — TWO accumulation normalizers, two interior clocks
beta'_col < beta_col bracketing the breathing. Q's tame odd columns are the
degenerate case c(a) = a - 1 (wall = state, no breathing); THE CLOCK := the
tick-state limit. Curio (exact): C_1/(1-x) = (1-x)^-2 = C_2, so the deg-1
post-tick clock IS the deg-2 clock.

K0 THE LAMBDA TABLE OF Z[sqrt(-5)] (brute over HNF-coset quotient rings) +
the state lemma over ideals (the Dedekind carry-over the wall discount rests
on: transparent m <=> every prime power of Im fits its cap in W(lambda(I)) —
brute at state P3^2 over all 41 products of the six small primes, N(m) <= 32).
Split P3: 2*3^(a-1) (a <= 5) — Q-like tame, no breathing. Inert (13):
168 = (13^2-1), then 168*13 at a = 2 (sampled lcm over 1392 units, exact).
Ramified tame P5 = (sqrt-5): 4*5^ceil((j-1)/2) (j <= 4) — the wall ticks
every e = 2 states. Ramified wild P2: chain 1, 2, 4, 4, 4, 4, 8, 8, 16
(j <= 9) — irregular wild ticks. Ramification sets the breathing: tame =
period e, wild = irregular ticks.

K1 THE TRANSPARENT MENU READS K TWICE (observation + two proved exclusions).
P3-column menu (N(R)-1 | 2*3^inf): candidates d*3^i + 1 are gated by chi_-20
— a candidate enters only if it splits (or ramifies). Proved on paper +
asserted: NO INERT prime ever enters (4 | p^2-1 while v2(2*3^i) = 1); in
range the gate ejects 19 and 1459 (prime, inert). Every entrant is
NONPRINCIPAL (the odd candidates 2*3^i + 1 fall in {3, 7, 19, 15} mod 20,
missing the principal genus {1, 9} entirely; the even family 3^i + 1
contributes only p = 2, ramified nonprincipal): transparency at 3 FORCES
the class. The
conjugate P3' rides the column's own 3-route to unbounded exponent (THE
CONJUGATE SHADOW — the same mechanism as char-2's universal free ride:
places sharing the column's residue characteristic). Menu norms in range:
{2, 3, 7, 163, 487, 39367}.

K2 THE CLOCK SPLITS BY THE CLASS GROUP (observation; identity components
proved/cited). The element world (principal moves only, explore_class_gap.py's mezzanine)
prices BOTH sides of the clock equation through the genus character:
zeta_princ = (zeta_K + L_cl)/2 (explore_class_gap.py finding 5, spot-checked at beta = 2)
and C_princ = (C_id + C_chi)/2 (verified against direct principal-divisor
lattice enumeration, 1e-12, 5376 vectors) — the element clock equation is
the ideal one AVERAGED OVER THE CLASS-GROUP CHARACTERS, and since the menu
is purely nonprincipal (K1), C_chi is fully signed: maximal contrast.
beta_col: element 1.35270 < ideal 1.54922 (gap 0.1965; frozen direction PR7
hit — the element world's lost full mass outweighs its lost transparent
mass, so it crosses earlier).

K3 THE POLE READS h IN THE DEPTH WORLD (observation; mechanism = the zeta
residue ratio). Z_id/Z_el at beta 1.2 / 1.05 / 1.01: 2.0317 -> 2.0056 ->
2.0010 — h = 2 read off the clock pair's normalizers at the pole. SLATE MISS
(PR8): the frozen prediction said approach from BELOW; the run shows a clean
monotone DESCENT from above (band clause hit, direction wrong — asserts
corrected to the truth post-run, marked in k3). explore_class_gap.py's pole ratio was the
breadth/crystal reading; this is its depth-world twin.

SYN THE SEAT LAW + THE FERMAT GATE (observation). K ideal spectrum over
columns {P2, P3, Q7, (13)}: 1.70395 > 1.54922 > 1.45633 > 1.31983 — the P2
column tops K exactly as q = 2 tops Q (1.6045) and deg-1 tops F_2(x)
(1.77155): at all three global fields the spectrum max sits at the place
with residue field F_2, the least-rich transparent menu. And K's 2-column is
edited by class field theory: the Fermat candidates 17, 257, 65537 are all
= 17 mod 20 => INERT => gated out (asserted); K's 2-column menu in range is
just {3, 5} — poorer than Q's five Fermat primes. The inert (13) column
(residue field F_169, rich 168-menu) sits at the bottom. Synthesis: the
irreducibility critical temperature is a valuation-theoretic invariant at
every global field tested — its TYPE reads the field (algebraic for the
rational zeta, class-split for the Dedekind zeta), its SEAT reads the
residue field, and its SPLIT reads the class group.

Run: `python explore_irreducibility_crossfield.py`. RUN RECORD (274 checks
pass, ~60 s): F_2(x) spectrum d = 1..6: 1.77155, 1.50553, 1.47652, 1.39505,
1.48768, 1.33584; x-root(d=1) = 0.29289321881; breathing bracket d=1:
1.77155 > 1.50553 (= the d=2 clock, exact identity). K: lambda chains as in
K0; P3-menu norms {2, 3, 7, 163, 487, 39367}, inert-gated {19, 1459};
split clocks 1.35270 (el) < 1.54922 (id), gap 0.1965; pole ratios 2.0317 ->
2.0056 -> 2.0010; K spectrum P2 1.70395 > P3 1.54922 > Q7 1.45633 > (13)
1.31983. zeta_princ(2) formula-vs-explore_class_gap.py-record within 2e-3. Two bugs caught
by the gates mid-run: an hnf sign flip (conjugate-ideal swap, caught by
the K0 lambda assert) and a prime-only chi20 fed to the L-series (caught by
the zeta_princ spot check).
"""

import sys, os, math
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_depth_observer import is_prime  # guarded module (lineage)

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


# ------------------------------------------------------------- zeta + L (hp)
_ZHP = {}


def zeta_hp(beta, M=20000):
    if beta not in _ZHP:
        s = sum(n ** -beta for n in range(1, M + 1))
        tail = (M ** (1 - beta) / (beta - 1)
                - 0.5 * M ** -beta
                + beta / 12.0 * M ** (-beta - 1))
        _ZHP[beta] = s + tail
    return _ZHP[beta]


def chi20(n):
    """Kronecker chi_-20 (multiplicative mod 20; at a prime: +1 split,
    -1 inert, 0 ramified)."""
    if gcd(n, 20) > 1:
        return 0
    return 1 if n % 20 in (1, 3, 7, 9) else -1


def chi4(n):
    return 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)


def chi5(n):
    if n % 5 == 0:
        return 0
    return 1 if pow(n, 2, 5) == 1 else -1


_LC = {}


def lseries(beta, chi, name, LN=100000):
    key = (beta, name)
    if key not in _LC:
        _LC[key] = sum(chi(n) * n ** -beta for n in range(1, LN + 1))
    return _LC[key]


def bisect_root(f, lo, hi, tol=1e-11):
    flo, fhi = f(lo), f(hi)
    ok(flo > 0 > fhi, f"bracket not straddling: f({lo})={flo}, f({hi})={fhi}")
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
        if hi - lo < tol:
            break
    return 0.5 * (lo + hi)


# ======================================================= F: the field F_2(x)
# polys as ints (bit i = coeff of x^i); monic, char 2.

def pdeg(f):
    return f.bit_length() - 1


def pmul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r


def pmod(a, m):
    dm = pdeg(m)
    while a and pdeg(a) >= dm:
        a ^= m << (pdeg(a) - dm)
    return a


def pdiv(a, m):
    q = 0
    dm = pdeg(m)
    while a and pdeg(a) >= dm:
        s = pdeg(a) - dm
        q ^= 1 << s
        a ^= m << s
    assert a == 0, "pdiv: non-exact division"
    return q


def pgcd(a, b):
    while b:
        a, b = b, pmod(a, b)
    return a


DMAX = 9
IRRED = {d: [] for d in range(1, DMAX + 1)}
_SPF = {}
for _f in range(2, 1 << (DMAX + 1)):
    if _f in _SPF:
        continue
    _SPF[_f] = _f
    IRRED[pdeg(_f)].append(_f)
    for _m in range(2, 1 << (DMAX - pdeg(_f) + 1)):
        _fm = pmul(_f, _m)
        if _fm not in _SPF:
            _SPF[_fm] = _f
N_E = {d: len(IRRED[d]) for d in range(1, DMAX + 1)}


def pfactor(f):
    out = {}
    while f > 1:
        g = _SPF[f]
        out[g] = out.get(g, 0) + 1
        f = pdiv(f, g)
    return out


def pow_poly(g, a):
    F = 1
    for _ in range(a):
        F = pmul(F, g)
    return F


def ceil_log2(a):
    return (a - 1).bit_length()


def lam_poly_formula(F):
    """exponent of (F_2[x]/(F))^*: lcm over g^a || F of (2^deg g - 1)*2^ceil(log2 a)."""
    L = 1
    for g, a in pfactor(F).items():
        part = (2 ** pdeg(g) - 1) * (1 << ceil_log2(a) if a > 1 else 1)
        L = L * part // gcd(L, part)
    return L


def lam_poly_brute(F):
    """brute exponent: lcm of orders of all units of F_2[x]/(F)."""
    L = 1
    for r in range(1, 1 << pdeg(F)):
        if pgcd(F, r) != 1:
            continue
        u, o = r, 1
        while u != 1:
            u = pmod(pmul(u, r), F)
            o += 1
        L = L * o // gcd(L, o)
    return L


def transparent_cap_poly(h, L):
    """max j >= 0 with lambda(h^j) | L, h irreducible (capped 10**6)."""
    lam1 = 2 ** pdeg(h) - 1
    if L % lam1:
        return 0
    j = 1
    while (L // lam1) % (1 << ceil_log2(j + 1)) == 0 and j < 10 ** 6:
        j += 1
    return j


def f0():
    print("F0 the lambda law of F_2[x] (brute)")
    for d in (1, 2, 3):
        for g in IRRED[d]:
            F, a = g, 1
            while pdeg(F) + d <= 9:
                F, a = pmul(F, g), a + 1
                ok(lam_poly_brute(F) == lam_poly_formula(F) ==
                   (2 ** d - 1) * (1 << ceil_log2(a)),
                   f"F0 lambda(g^a) wrong at deg {d}, a={a}")
    for F in range(64, 128):        # all monic deg-6: the lcm law
        ok(lam_poly_brute(F) == lam_poly_formula(F), f"F0 lcm law fails at F={F}")
    # state lemma: transparent m <=> lambda(Fm) = lambda(F) <=> Fm | W(lambda(F)),
    # the wall checked componentwise via per-irreducible caps
    for F in (4, 8, 16, 32, 5, 25):
        L = lam_poly_formula(F)
        for m in range(2, 1 << 4):
            Fm = pmul(F, m)
            if pdeg(Fm) > 9:
                continue
            trans = (lam_poly_formula(Fm) == L)
            fits = all(e <= transparent_cap_poly(h, L)
                       for h, e in pfactor(Fm).items())
            ok(trans == fits, f"F0 state lemma fails at F={F}, m={m}")
    print("  lambda(g^a) = (2^d - 1) * 2^ceil(log2 a); lcm law all monic deg 6; "
          "state lemma on 6 states")


def C_d(d, xv, post=False):
    """limit cofactor of a degree-d column; post=True: the post-tick limit."""
    s = 1.0
    for e in range(1, d + 1):
        if d % e == 0:
            s *= (1.0 / (1.0 - xv ** e)) ** (N_E[e] - (1 if e == d else 0))
    if post:
        s /= (1.0 - xv ** d)
    return s


def zeta_F2(xv):
    return 1.0 / (1.0 - 2.0 * xv)


def clock_F(d, post=False):
    f = lambda b: zeta_F2(2.0 ** -b) - C_d(d, 2.0 ** -b, post) - 1.0
    return bisect_root(f, 1.0001, 1.9999999)


def f1():
    print("F1 the algebraic clock")
    ok(abs(zeta_F2(0.25) - 2.0) < 1e-15, "F1 beta* != 2")
    bc = {d: clock_F(d) for d in range(1, 7)}
    x1 = 2.0 ** -bc[1]
    ok(abs(x1 - (1.0 - 2.0 ** -0.5)) < 1e-9, f"F1 d=1 x-root {x1} != 1 - 1/sqrt2")
    ok(abs(2 * x1 ** 2 - 4 * x1 + 1) < 1e-9, "F1 d=1 poly residual")
    x2 = 2.0 ** -bc[2]
    ok(abs(2 * x2 ** 3 - 4 * x2 ** 2 + 4 * x2 - 1) < 1e-9, "F1 d=2 poly residual")
    for d in range(1, 7):
        ok(1.0 < bc[d] < 2.0, f"F1 beta_col({d}) = {bc[d]} not in (1, 2)")
    print(f"  beta* = 2 EXACTLY (x = 1/4); x-root(d=1) = {x1:.11f} = 1 - 1/sqrt2;")
    print("  spectrum: " + ", ".join(f"d={d}:{bc[d]:.5f}" for d in range(1, 7)))
    return bc


def f2(bc):
    print("F2 degree is the whole dial + the seat")
    # per-column transparent sets from the lambda law directly (a = 64, s = 6)
    for d in (1, 3):
        sets = []
        for g in IRRED[d]:
            L = (2 ** d - 1) * 64
            T = frozenset(h for e in range(1, 7) for h in IRRED[e]
                          if h != g and transparent_cap_poly(h, L) >= 1)
            sets.append(T)
            ok(all(d % pdeg(h) == 0 for h in T),
               f"F2 transparent set of deg-{d} column not the subfield lattice")
            ok(len(T) == sum(N_E[e] for e in range(1, d + 1) if d % e == 0) - 1,
               f"F2 transparent count wrong at deg {d}")
        ok(len({frozenset(pdeg(h) for h in T) for T in sets}) == 1 and
           len({len(T) for T in sets}) == 1,
           f"F2 same-degree columns differ at d={d}")
    for e, d in ((1, 2), (1, 3), (2, 4), (2, 6), (3, 6)):
        ok(bc[d] < bc[e], f"F2 beta_col({d}) !< beta_col({e}) (e | d)")
    ok(bc[3] < bc[2], "F2 count-richness: beta_col(3) !< beta_col(2)")
    ok(bc[1] == max(bc.values()), "F2 the seat: deg-1 not the max")
    print("  transparent set = subfield lattice; same-degree columns identical;")
    print(f"  seat: deg-1 (residue field F_2) = spectrum max {bc[1]:.5f}")


def cofactor_poly_finite(g, a, xv):
    """finite-state cofactor of column g^a: W(lambda(g^a)) = prod_{deg h | d}
    h^(2^s), s = ceil(log2 a); divided by the state g^a."""
    d = pdeg(g)
    cap = 1 << (ceil_log2(a) if a > 1 else 0)
    total = 1.0
    for e in range(1, d + 1):
        if d % e == 0:
            geom = sum(xv ** (e * j) for j in range(cap + 1))
            total *= geom ** (N_E[e] - (1 if e == d else 0))
    total *= sum(xv ** (d * j) for j in range(cap - a + 1))  # the g-remainder
    return total


def f3():
    print("F3 the breathing is a ramification law")
    g, d, beta = 2, 1, 1.5              # the column of x
    xv = 2.0 ** -beta
    for a in (5, 6, 7, 8):
        ok(lam_poly_formula(pow_poly(g, a)) == lam_poly_formula(pow_poly(g, 8)),
           f"F3 lambda not block-constant at a={a}")
    ok(lam_poly_formula(pow_poly(g, 9)) != lam_poly_formula(pow_poly(g, 8)),
       "F3 lambda fails to tick at a=9")
    for s in (2, 3, 4):
        ok(cofactor_poly_finite(g, 2 ** s + 1, xv) >
           cofactor_poly_finite(g, 2 ** s, xv), f"F3 no breathing at s={s}")
    clean, post = C_d(d, xv), C_d(d, xv, post=True)
    ec = [abs(cofactor_poly_finite(g, 2 ** s, xv) - clean) for s in (4, 5, 6)]
    ep = [abs(cofactor_poly_finite(g, 2 ** s + 1, xv) - post) for s in (4, 5, 6)]
    ok(ec[0] > ec[1] > ec[2] and ec[2] < 1e-6, "F3 clean limit wrong")
    ok(ep[0] > ep[1] > ep[2] and ep[2] < 1e-6, "F3 post-tick limit wrong")
    b_clean, b_post = clock_F(d), clock_F(d, post=True)
    ok(1.0 < b_post < b_clean < 2.0, "F3 breathing clocks not ordered/interior")
    # curio: C_1/(1-x) = (1-x)^-2 = C_2 exactly (N_2 = 1, self-blind), so the
    # deg-1 post-tick clock IS the deg-2 clock
    ok(abs(b_post - clock_F(2)) < 1e-9, "F3 post-tick(1) != clock(2)")
    print(f"  clean clock {b_clean:.5f} > post-tick clock {b_post:.5f} "
          f"(= the d=2 clock exactly: C_1/(1-x) = C_2)")


# ==================================================== K: the field Q(sqrt(-5))
# elements x + y*t, t^2 = -5, as pairs (x, y); ideals as HNF lattices
# (n1, s, n2): Z-basis {(n1, 0), (s, n2)} = {n1, s + n2*t}.

def xgcd(a, b):
    if b == 0:
        return a, 1, 0
    g, u, v = xgcd(b, a % b)
    return g, v, u - (a // b) * v


def hnf(vecs):
    vecs = [list(v) for v in vecs if v != (0, 0)]
    v2 = None
    for v in vecs:
        if v[1] == 0:
            continue
        if v2 is None:
            v2 = v[:]
        else:
            g, a, b = xgcd(v2[1], v[1])
            v2 = [a * v2[0] + b * v[0], g]
    assert v2 is not None and v2[1] != 0, "hnf: rank < 2"
    if v2[1] < 0:
        v2 = [-v2[0], -v2[1]]
    n1 = 0
    for v in vecs:
        n1 = gcd(n1, abs(v[0] - (v[1] // v2[1]) * v2[0]))
    assert n1 > 0, "hnf: rank < 2 (x)"
    return (n1, v2[0] % n1, v2[1])


def ideal_from_gens(gens):
    vecs = []
    for (x, y) in gens:
        vecs.append((x, y))
        vecs.append((-5 * y, x))        # (x + yt) * t
    return hnf(vecs)


def ideal_mul(A, B):
    gens = []
    for (x1, y1) in ((A[0], 0), (A[1], A[2])):
        for (x2, y2) in ((B[0], 0), (B[1], B[2])):
            gens.append((x1 * x2 - 5 * y1 * y2, x1 * y2 + y1 * x2))
    return ideal_from_gens(gens)


def ideal_pow(A, n):
    R = (1, 0, 1)
    for _ in range(n):
        R = ideal_mul(R, A)
    return R


def ideal_norm(A):
    return A[0] * A[2]


def qreduce(A, x, y):
    n1, s, n2 = A
    k = y // n2
    return ((x - k * s) % n1, y - k * n2)


def qmul(A, u, v):
    return qreduce(A, u[0] * v[0] - 5 * u[1] * v[1], u[0] * v[1] + u[1] * v[0])


def lam_ideal_brute(A):
    """exponent of (O/A)^* by full order brute (norm(A) small)."""
    N = ideal_norm(A)
    L = 1
    for x in range(A[0]):
        for y in range(A[2]):
            r = (x, y)
            u, o = r, 1
            while u != (1, 0) and o <= N:
                u = qmul(A, u, r)
                o += 1
            if u == (1, 0):
                L = L * o // gcd(L, o)
    return L


P3 = ideal_from_gens([(3, 0), (-1, 1)])     # (3, t - 1)
P2 = ideal_from_gens([(2, 0), (1, 1)])      # (2, 1 + t)
P5 = ideal_from_gens([(0, 1)])              # (sqrt -5)

LAM2 = {}
LAM5 = {}


def k0():
    print("K0 the lambda table of Z[sqrt(-5)] (brute)")
    for a in range(1, 6):
        Pa = ideal_pow(P3, a)
        ok(ideal_norm(Pa) == 3 ** a, f"K0 N(P3^{a}) != 3^{a}")
        ok(lam_ideal_brute(Pa) == 2 * 3 ** (a - 1), f"K0 lambda(P3^{a}) wrong")
    ok(ideal_pow(P2, 2) == ideal_from_gens([(2, 0)]), "K0 P2^2 != (2)")
    for j in range(1, 10):
        ok(ideal_norm(ideal_pow(P2, j)) == 2 ** j, f"K0 N(P2^{j}) wrong")
        LAM2[j] = lam_ideal_brute(ideal_pow(P2, j))
    for j in range(1, 5):
        LAM5[j] = lam_ideal_brute(ideal_pow(P5, j))
        ok(LAM5[j] == 4 * 5 ** (j // 2), f"K0 lambda(P5^{j}) = {LAM5[j]}")
    I13 = ideal_from_gens([(13, 0)])
    ok(lam_ideal_brute(I13) == 168, "K0 lambda((13)) != 168")
    A2 = ideal_from_gens([(169, 0)])
    L, target, n_seen = 1, 168 * 13, 0
    for x in range(1, 169, 3):
        for y in range(0, 169, 7):
            if (x * x + 5 * y * y) % 13 == 0:
                continue
            r, o = (x, y), 1
            u = r
            while u != (1, 0) and o <= target:
                u = qmul(A2, u, r)
                o += 1
            assert u == (1, 0), f"K0 sampled order at ({x},{y}) exceeds 2184"
            L = L * o // gcd(L, o)
            n_seen += 1
    ok(L == target and n_seen > 300, f"K0 inert a=2 sampled lcm {L} != 2184")
    # the state lemma over ideals (the Dedekind carry-over of a companion record's D-TRA
    # lemma, which the wall-discount normalizer rests on): at state I = P3^2,
    # a move m is transparent (lambda(Im) = lambda(I)) iff every prime power
    # in Im fits its cap in W(lambda(I)) — brute over all products of the six
    # small primes with N(m) <= 32
    P3C = ideal_from_gens([(3, 0), (1, 1)])
    Q7 = ideal_from_gens([(7, 0), (-3, 1)])
    Q7C = ideal_from_gens([(7, 0), (3, 1)])
    small = [(P2, 2), (P3, 3), (P3C, 3), (P5, 5), (Q7, 7), (Q7C, 7)]
    I0 = ideal_pow(P3, 2)
    L0 = lam_ideal_brute(I0)
    base_e = [0, 2, 0, 0, 0, 0]         # exponents of I0 = P3^2 over `small`
    cap = []
    for R, nrm in small:
        j = 0
        while L0 % lam_ideal_brute(ideal_pow(R, j + 1)) == 0:
            j += 1
        cap.append(j)
    n_lemma = 0
    def gen_vecs(i, nrm, vec):
        nonlocal n_lemma
        if i == len(small):
            if nrm > 1:
                Im = I0
                for (R, _), e in zip(small, vec):
                    Im = ideal_mul(Im, ideal_pow(R, e))
                trans = (lam_ideal_brute(Im) == L0)
                fits = all(b + e <= c
                           for b, e, c in zip(base_e, vec, cap))
                assert trans == fits, f"K0 ideal state lemma fails at {vec}"
                n_lemma += 1
            return
        e = 0
        while nrm * small[i][1] ** e <= 32:
            gen_vecs(i + 1, nrm * small[i][1] ** e, vec + [e])
            e += 1
    gen_vecs(0, 1, [])
    ok(n_lemma > 20, f"K0 ideal state lemma coverage too thin ({n_lemma})")
    print(f"  P3: 2*3^(a-1); (13): 168 then 168*13 (a=2 sampled lcm, "
          f"{n_seen} units); ideal state lemma at P3^2 over {n_lemma} moves;")
    print(f"  P5 chain: {[LAM5[j] for j in range(1, 5)]} = 4*5^ceil((j-1)/2) "
          f"(tame breathing, period e=2);")
    print(f"  P2 chain: {[LAM2[j] for j in range(1, 10)]} (wild 2-chain)")


def strip_p(m, p):
    while m % p == 0:
        m //= p
    return m


def build_menu(Q0, proute, imax=14):
    """transparent prime ideals of the column with lambda-limit Q0 * proute^inf:
    list of (kind, p, norm, cap, bit); cap 10**9 = the unbounded proute-route.
    Caller removes the column's own place. bit = genus character (1 = nonprin)."""
    cands = set()
    for d in range(1, Q0 + 1):
        if Q0 % d == 0:
            for i in range(imax + 1):
                cands.add(d * proute ** i + 1)
    menu = []
    for N in sorted(cands):
        if N < 2 or not is_prime(N):
            continue
        p = N
        if p == 2:
            cap = 0
            for j in sorted(LAM2):
                if Q0 % strip_p(LAM2[j], proute) == 0:
                    cap = j
                else:
                    break
            if cap:
                menu.append(('ram2', 2, 2, cap, 1))
        elif p == 5:
            cap = 0
            for j in sorted(LAM5):
                if Q0 % strip_p(LAM5[j], proute) == 0:
                    cap = j
                else:
                    break
            if cap:
                menu.append(('ram5', 5, 5, cap, 0))
        elif chi20(p) == 1:
            bit = 1 if p % 20 in (3, 7) else 0
            if p == proute:
                cap = 10 ** 9           # the conjugate shadow
            else:
                cap, j = 0, 1
                while Q0 % strip_p((p - 1) * p ** (j - 1), proute) == 0:
                    cap = j
                    j += 1
            if cap:
                menu.append(('split', p, p, cap, bit))
                menu.append(('split', p, p, cap, bit))
    # inert entrants: (q) has norm q^2, lambda((q)^j) = (q^2-1) q^(j-1); it
    # enters iff q^2 - 1 | Q0 * proute^inf <=> q^2 in cands (single path, so
    # no double count; cap 1 unless q = proute, the caller's own column)
    for N in sorted(cands):
        r = math.isqrt(N)
        if r * r == N and is_prime(r) and chi20(r) == -1:
            if Q0 % strip_p(r * r - 1, proute) == 0:
                cap = 10 ** 9 if r == proute else 1
                menu.append(('inert', r, r * r, cap, 0))
    return menu


def cof_factor(norm, cap, beta, sign=1.0):
    q = sign * norm ** -beta
    if cap >= 10 ** 9:
        return 1.0 / (1.0 - q)
    return sum(q ** j for j in range(cap + 1))


def C_menu(menu, beta, twisted=False):
    s = 1.0
    for kind, p, norm, cap, bit in menu:
        s *= cof_factor(norm, cap, beta, -1.0 if (twisted and bit) else 1.0)
    return s


def zeta_K(beta):
    return zeta_hp(beta) * lseries(beta, chi20, 'chi20')


def zeta_princ(beta):
    return 0.5 * (zeta_K(beta) +
                  lseries(beta, chi4, 'chi4') * lseries(beta, chi5, 'chi5'))


def drop_own(menu, own_norm):
    i = next(i for i, m in enumerate(menu) if m[2] == own_norm)
    return menu[:i] + menu[i + 1:]


MENU_P3 = None


def k1():
    global MENU_P3
    print("K1 the transparent menu reads K twice (the P3 column)")
    MENU_P3 = drop_own(build_menu(2, 3), 3)
    ok(all(m[0] != 'inert' for m in MENU_P3), "K1 an inert prime entered")
    ok(all(m[4] == 1 for m in MENU_P3), "K1 a principal entrant")
    ok(all(m[1] != 5 for m in MENU_P3), "K1 P5 entered (4 not | 2*3^inf)")
    shadows = [m for m in MENU_P3 if m[3] >= 10 ** 9]
    ok(len(shadows) == 1 and shadows[0][1] == 3, "K1 conjugate shadow wrong")
    gated = [2 * 3 ** i + 1 for i in range(15)
             if is_prime(2 * 3 ** i + 1) and chi20(2 * 3 ** i + 1) == -1]
    ok(19 in gated, "K1 19 not gated (should be inert)")
    norms = sorted(set(m[2] for m in MENU_P3))
    print(f"  menu norms {norms} (all nonprincipal; conjugate shadow at 3);")
    print(f"  inert-gated split candidates: {gated}")


def Z_id(beta):
    return zeta_K(beta) - C_menu(MENU_P3, beta)


def Z_el(beta):
    return zeta_princ(beta) - 0.5 * (C_menu(MENU_P3, beta) +
                                     C_menu(MENU_P3, beta, twisted=True))


def k2():
    print("K2 the clock splits by the class group")
    zp2 = zeta_princ(2.0)
    ok(abs(zp2 - 1.2512) < 2e-3, f"K2 zeta_princ(2) = {zp2} vs ch.10 record")
    beta = 1.4
    tmenu = [(k, p, n, min(c, 6), b) for (k, p, n, c, b) in MENU_P3]
    vecs = [(1.0, 0)]
    for kind, p, norm, cap, bit in tmenu:
        vecs = [(w * norm ** (-beta * j), (par + bit * j) % 2)
                for (w, par) in vecs for j in range(cap + 1)]
    direct_full = sum(w for w, _ in vecs)
    direct_princ = sum(w for w, par in vecs if par == 0)
    ok(abs(direct_full - C_menu(tmenu, beta)) < 1e-12,
       "K2 C_id truncated mismatch")
    ok(abs(direct_princ - 0.5 * (C_menu(tmenu, beta) +
                                 C_menu(tmenu, beta, twisted=True))) < 1e-12,
       "K2 C_princ truncated mismatch")
    b_id = bisect_root(lambda b: Z_id(b) - 1.0, 1.0001, 2.5)
    b_el = bisect_root(lambda b: Z_el(b) - 1.0, 1.0001, 2.5)
    ok(b_el < b_id - 1e-3, f"K2 split direction: el {b_el} !< id {b_id}")
    print(f"  C_princ = (C_id + C_chi)/2 (direct lattice check 1e-12; "
          f"{len(vecs)} vectors);")
    print(f"  beta_col: element {b_el:.5f} < ideal {b_id:.5f} "
          f"(gap {b_id - b_el:.4f})")
    return b_id, b_el


def k3():
    print("K3 the pole reads h in the depth world")
    ratios = [Z_id(b) / Z_el(b) for b in (1.2, 1.05, 1.01)]
    # slate miss (PR8 predicted approach from below): the run shows the ratio
    # DESCENDS to h from above — |ratio - h| shrinking, monotone
    ok(ratios[0] > ratios[1] > ratios[2] > 2.0, "K3 ratio not descending to h")
    ok(abs(ratios[2] - 2.0) < abs(ratios[0] - 2.0) / 10,
       "K3 ratio not converging on h")
    ok(1.85 < ratios[2] < 2.05, f"K3 ratio at 1.01 = {ratios[2]} not near h=2")
    print("  Z_id/Z_el at beta 1.2 / 1.05 / 1.01: "
          + " -> ".join(f"{r:.4f}" for r in ratios) + "  (h = 2)")


def syn(bc_F):
    print("SYN the seat law + the Fermat gate")
    cols = {}
    for name, Q0, proute, own_norm in (('P2', 1, 2, 2), ('P3', 2, 3, 3),
                                       ('Q7', 6, 7, 7), ('(13)', 168, 13, 169)):
        menu = drop_own(build_menu(Q0, proute), own_norm)
        cols[name] = bisect_root(
            lambda b, mm=menu: zeta_K(b) - C_menu(mm, b) - 1.0, 1.0001, 2.5)
        if name == 'P2':
            for f in (17, 257, 65537):
                ok(chi20(f) == -1, f"SYN Fermat {f} not inert")
                ok(all(m[1] != f for m in menu), f"SYN Fermat {f} entered")
            ok(sorted(set(m[2] for m in menu)) == [3, 5],
               "SYN P2-column menu != {3, 5}")
    ok(cols['P2'] == max(cols.values()), "SYN P2 column not the K max")
    ok(cols['P2'] > cols['P3'] > cols['Q7'] > cols['(13)'],
       "SYN K spectrum not ordered P2 > P3 > Q7 > (13)")
    ok(bc_F[1] == max(bc_F.values()), "SYN F_2(x) seat regressed")
    print("  K spectrum: " + " > ".join(f"{n}:{cols[n]:.5f}"
                                        for n in ('P2', 'P3', 'Q7', '(13)')))
    print("  the seat at all three fields = residue field F_2 (q=2 in Q, "
          "deg-1 in F_2(x), P2 in K);")
    print("  Fermat 17/257/65537 inert-gated out of K's 2-column")


def main():
    f0()
    bc = f1()
    f2(bc)
    f3()
    k0()
    k1()
    k2()
    k3()
    syn(bc)
    print(f"\nALL SECTIONS PASS ({CHECKS} checks)")


if __name__ == "__main__":
    main()
