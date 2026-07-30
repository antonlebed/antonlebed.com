"""
explore_class_gap.py -- THE CLASS GAP (sibling of explore_growth_laws.py
.. explore_selection_frame.py).

THE QUESTION: in Z[sqrt(-5)] elements are NOT free but
IDEALS are -- explore_selection_frame.py proved freeness necessary for the crystal
(the coprimality collapse), so what does thermal growth see of the
CLASS GROUP, the gap between the element and ideal selection theories?
ANSWER: everything -- the class group is a forced completion (T > 0
dynamics), an L-function gap (statics), and 1/h at the pole (the
thermometer). Design + predictions PR1-PR8 fixed before the run, plus
a literature attack and post-run adjudication.

THE WORLDS. K = Q(sqrt(-5)), O = Z[sqrt(-5)], disc -20, h = 2,
Cl = C2 (the class group is literally one parity bit per prime
ideal). M_id = nonzero ideals: FREE on prime ideals (floor 2),
partition function sum N(I)^-beta = zeta_K = zeta * L(chi_{-20}).
M_el = elements mod units = principal ideals: cancellative +
summable character but NOT free (6 = 2*3 = (1+sqrt(-5))(1-sqrt(-5)))
-- floor 1 with a free CLOSURE (Krull): THE MEZZANINE. Control
world: Z[i] (h = 1). Splitting by chi_{-20}, classes by the genus
rule (both classical, verified in range, S1).

FINDINGS (tiers per the standard naming scale; all sections assert;
run record below).

1. THE SENSOR CRITERION (criterion, proved; the zero-sum-free law in
   any Dedekind domain, the h > 1 witness constructive in any ring
   of integers O_K, where every class carries the needed coprime
   representatives; verified S2). Common non-unit element divisors
   of a, b correspond
   to nontrivial PRINCIPAL divisors of G = gcd((a),(b)), so a, b are
   element-coprime iff G's class sequence (with multiplicity) is
   ZERO-SUM-FREE over Cl -- and the sensor is exact (element-coprime
   <=> ideal-coprime, all pairs) iff h = 1 (h > 1 direction
   constructive: G = one nonprincipal prime P, generators of PA, PB
   with A != B integral in [P]^-1 coprime to P and each other).
   Element-coprimality is CLASS-BLIND: it cannot see a hidden common
   prime whose class obstructs a principal witness. THE COLLISION
   BUDGET: a hidden gcd carries at most D(Cl) - 1 primes (Davenport
   constant; = 1 for C2). Verified: brute divisor search == the
   zero-sum-free predicate on all 3240 pairs (norms <= 120); 904
   hidden-coprime pairs, every hidden gcd exactly one nonprincipal
   prime; norm-minimal hidden pairs = the conjugate twins
   {2, 1+-sqrt(-5)} (slate miss 1: minimality is conjugation-
   symmetric -- hidden pairs come in conjugate orbits); Z[i] control:
   zero hidden pairs among 4005.

2. FLOOR-2 TRANSFER: THE DEDEKIND PARTITION FUNCTION (rule, proved
   by ch.9 finding 4, hypotheses checked; verified S3). Thermal
   ideal-D-IND crystallizes at prod_P (1 - N(P)^-beta) = 1/zeta_K:
   the Dedekind zeta is the ideal world's partition function -- the
   family is now three deep (Riemann for Z, rational for F_2[x],
   Dedekind for O_K). Verified: matched-truncation mass identities
   exact to 1e-12 (the geometric-entry bijection m <-> P^d m',
   states 1 and (1+sqrt(-5)), d = 1, 2); Euler over the norm <= 10^4
   menu 1.855539 vs zeta(2) L(2, chi_{-20}) = 1.855557; crystal
   probability 1/zeta_K(2) = 0.538922 (frozen band (0.52, 0.56)
   hit); MC 400 runs squarefree 0.578 vs in-universe exact 0.546.

3. THE ABSORPTION PROFILE LAW: the element crystal is DEAD, not
   leaky (rule, proved in-universe; the infinite-world limit is this
   record's open edge; verified S5). By finding 1, element-D-IND
   admits a move iff it shares nothing with the state, or exactly
   one nonprincipal prime P with min(e_move, e_state) = 1 -- so the
   pure-square move gen(P^2) (e.g. 2 = P2^2) is admissible at
   e_state(P) = 0 AND 1, and an in-universe run can only absorb with
   EVERY nonprincipal atom at depth >= 2 and every principal atom
   entered (the in-universe menu carries every atom's pure square).
   MC: squarefree fraction 0.000, hidden collisions in
   400/400 runs (1.000 by move 5), mean P2 absorption depth 3.81;
   P(hidden collision at move 2) = 0.4125, exact within the
   norm <= 500 element menu (minimal-norm openings: 2 and
   1+-sqrt(-5) in either order, sharing exactly P2). Prediction
   miss 2, a familiar species: the predicted band (0.1, 0.9) died
   because the truth is a LAW, not a leak. Infinite-world reading (argued,
   NOT proved -- random-process asymptotics): P-through channels
   m = P * (fresh) stay admissible at every depth (min(1, e) = 1 is
   zero-sum-free), pure-square hazards are constant while e = 1, and
   coprime mass -> 0, so every nonprincipal prime is arguably driven
   to unbounded depth while principal primes stay entry-once: the
   thermal element limit would complete exactly the nonprincipal
   columns -- the class group as a partition of places into shallow
   (trivial class) and bottomless (nontrivial class).

4. THE ELEMENT MISMATCH AT ITS CLASSICAL HOME (rule in range; the
   static combinatorics is textbook block-monoid theory, stated as
   such; verified S4). Irreducible elements = principal ideals whose
   class sequence is a MINIMAL zero-sum sequence; over C2 exactly
   two species -- principal primes (19 of norm <= 200) and products
   of two nonprincipal primes (41) -- confirmed against brute
   proper-principal-divisor search on every principal ideal of norm
   <= 200. Euler-over-atoms vs Dirichlet-over-elements first
   diverges at norm 36 (6 vs 3; proved on paper before the run:
   factorizations = perfect matchings on the odd-bit primes,
   distinct matchings need four entries NOT all on one prime --
   P2^4 = (4), norm 16, matches uniquely -- and P2 is the only
   norm-2 prime, so the minimum is 2*2*3*3 = 36): ch.9's
   zeta-Euler mismatch (13/12 vs 1024/945) at its classical home.

5. THE PARTITION SPLIT (the identity is classical genus theory; the
   growth reading is the finding; verified S6, strong form).
   #principal(n) = (a_n + (chi_{-4} * chi_5)(n))/2 for ALL
   n <= 10^4, coefficient by coefficient: zeta_princ = (zeta_K +
   L(chi_{-4}) L(chi_5))/2, so the GAP between the element and ideal
   worlds' partition functions IS the class-group L-function
   (2 zeta_princ - zeta_K = L_cl). Numeric: zeta_princ(2) enumerated
   1.251141 vs formula 1.251211.

6. THE POLE RATIO: TEMPERATURE READS THE CLASS NUMBER (the residue
   equidistribution is classical; the thermal reading is the
   finding; verified S6). zeta_princ/zeta_K = 0.6743 (beta 2) ->
   0.5276 (1.2) -> 0.5063 (1.05) -> 1/h = 1/2 at the pole: heat the
   two selection theories toward the Haar edge and the element
   world's share of the ideal world's mass converges to 1/h -- the
   class number is a thermal observable. Self-check: h = w sqrt(20)
   L(1, chi_{-20})/(2 pi) = 1.999994 (L(1, chi_{-20}) = 1.404959).

7. THE MEZZANINE (synthesis -- the ladder gains a floor). M_el
   passes floor 1 (mass identity w(aM) = w(a) w(M) exact at a = 2,
   1+sqrt(-5), 3 -- S5; hot growth under up-closed demands reaches
   the top, and P2 | (2)
   makes ideal-cofinality ride along) but not floor 2; its free
   CLOSURE M_id is floor 2. Between "cancellative" and "free" sits
   the Krull mezzanine, graded by Cl: ch.9's coprimality collapse is
   the mezzanine's floor-1 face (D-IND mortal when zero-sum-free
   depth is 0), Z[sqrt(-5)] its graded face (collisions budgeted by
   D(Cl) - 1, crystal dead but growth immortal), the UFD its top
   (h = 1, sensor exact, crystal at 1/zeta). To be arithmetic at the
   IDEAL level needs only the mezzanine; to be arithmetic at the
   ELEMENT level -- squarefree, independent windows -- needs h = 1.

RUN RECORD. python prime/code/explore_class_gap.py: "RESULT: all
40040 checks pass", ~1.3 s, no deps. Sections S1-S6 as above; MC 400
runs/world at beta = 2, seeds 15213 (ideal) / 15214 (element),
6-atom universe (norms 2, 3, 3, 5, 7, 7), menu 1431 ideal / 712
element moves, norm cap 10^4. Predictions PR1-PR8 (fixed before the
run, amended once before running): PR1/PR2/PR3/PR4/PR6/PR7/PR8
CONFIRMED; PR5's band and the specimen-uniqueness clause MISSED, both
upgraded to stronger findings (the absorption profile law; the
conjugate-twin tie) -- adjudicated after the run, fixed in this file,
rerun clean.
"""

import math
import random
import sys
from bisect import bisect_left

sys.setrecursionlimit(10000)

CHECKS = 0
FAILS = []


def ok(cond, msg=""):
    global CHECKS
    CHECKS += 1
    if not cond:
        FAILS.append(msg)
        print("  ** FAIL:", msg)


def weighted_sample(rg, cum, items):
    x = rg.random() * cum[-1]
    return items[bisect_left(cum, x)]


# ------------------------------------------------------------------ #
# The world: K = Q(sqrt(-5)), O = Z[sqrt(-5)], disc -20, units +-1,
# h = 2.  Prime-ideal symbols: ('r', 2) = P2 (norm 2, NONPRINCIPAL),
# ('r', 5) = P5 = (sqrt(-5)) (norm 5, principal), (p, c) split with
# c^2 = -5 mod p (norm p; nonprincipal iff p mod 20 in {3, 7} --
# genus rule, classical), ('i', q) inert (norm q^2, principal).
# Class group C2 = one parity bit per symbol: an ideal is principal
# iff its exponent-weighted bit sum is even.
# ------------------------------------------------------------------ #

XMAX = 10 ** 4


def sieve_primes(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(range(i * i, n + 1, i)))
    return [p for p in range(2, n + 1) if s[p]]


PRIMES = sieve_primes(XMAX)


def chi20(n):
    r = n % 20
    if r in (1, 3, 7, 9):
        return 1
    if r in (11, 13, 17, 19):
        return -1
    return 0


def chi4(n):
    r = n % 4
    return 1 if r == 1 else (-1 if r == 3 else 0)


def chi5(n):
    r = n % 5
    return 1 if r in (1, 4) else (-1 if r in (2, 3) else 0)


SQRTM5 = {}          # split p -> smallest c with c^2 = -5 mod p
SYMS = []
for p in PRIMES:
    if p == 2:
        SYMS.append(('r', 2))
    elif p == 5:
        SYMS.append(('r', 5))
    elif chi20(p) == 1:
        c = next(c for c in range(1, p) if (c * c + 5) % p == 0)
        SQRTM5[p] = c
        SYMS.append((p, c))
        SYMS.append((p, p - c))
    elif p * p <= XMAX:
        SYMS.append(('i', p))


def norm_sym(s):
    if s[0] == 'r':
        return s[1]
    if s[0] == 'i':
        return s[1] * s[1]
    return s[0]


def bit_sym(s):
    if s == ('r', 2):
        return 1
    if s[0] == 'i' or s == ('r', 5):
        return 0
    return 1 if s[0] % 20 in (3, 7) else 0


SYMS.sort(key=norm_sym)
NSYM = len(SYMS)
NORMS = [norm_sym(s) for s in SYMS]
BITS = [bit_sym(s) for s in SYMS]


def parity(fac):
    return sum(bit_sym(s) * e for s, e in fac.items()) % 2


def vp(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def _fill(fac, a, b, p, v):
    if p == 2:
        fac[('r', 2)] = v                 # P2^2 = (2), N(P2) = 2
    elif p == 5:
        fac[('r', 5)] = v
    elif chi20(p) == -1:
        assert v % 2 == 0
        fac[('i', p)] = v // 2
    else:
        c = SQRTM5[p]
        aa, bb, com = a, b, 0
        while aa % p == 0 and bb % p == 0:
            aa //= p
            bb //= p
            com += 1
        rem = v - 2 * com
        if com:
            fac[(p, c)] = com
            fac[(p, p - c)] = com
        if rem:
            hit_c = (aa + bb * c) % p == 0
            hit_d = (aa + bb * (p - c)) % p == 0
            assert hit_c != hit_d, (a, b, p)
            key = (p, c) if hit_c else (p, p - c)
            fac[key] = fac.get(key, 0) + rem


def elem_factor(a, b):
    """Ideal factorization of (a + b sqrt(-5)) as {symbol: exp}."""
    n = a * a + 5 * b * b
    assert n > 0
    fac = {}
    m = n
    for p in PRIMES:
        if p * p > m:
            break
        if m % p:
            continue
        v = vp(m, p)
        m //= p ** v
        _fill(fac, a, b, p, v)
    if m > 1:
        _fill(fac, a, b, m, vp(n, m))
    nn = 1
    for s, e in fac.items():
        nn *= norm_sym(s) ** e
    assert nn == n, (a, b, fac)
    return fac


def elements_upto(X):
    """Nonzero non-unit elements mod units {+-1}: rep b > 0, or
    b == 0 and a >= 2."""
    out = []
    bmax = int((X / 5) ** 0.5)
    for b in range(0, bmax + 1):
        amax = int((X - 5 * b * b) ** 0.5)
        for a in range(-amax, amax + 1):
            n = a * a + 5 * b * b
            if n < 2 or n > X:
                continue
            if b == 0 and a < 2:
                continue
            out.append((a, b))
    return out


def divides(a, b, c, d):
    """Does c + d sqrt(-5) divide a + b sqrt(-5) in O?"""
    n = c * c + 5 * d * d
    return (a * c + 5 * b * d) % n == 0 and (b * c - a * d) % n == 0


# ------------------------------------------------------------------ #
print("S1: the world (splitting, genus parity, the census identities)")
# ------------------------------------------------------------------ #

cnt_all = [0] * (XMAX + 1)      # ideals of norm n
cnt_p0 = [0] * (XMAX + 1)       # principal (parity-0) ideals of norm n


def dfs_count(i, n, par):
    cnt_all[n] += 1
    if par == 0:
        cnt_p0[n] += 1
    for j in range(i, NSYM):
        nj = NORMS[j]
        if n * nj > XMAX:
            break
        m = n * nj
        b = BITS[j]
        pp = par
        while m <= XMAX:
            pp ^= b
            dfs_count(j + 1, m, pp)
            m *= nj


dfs_count(0, 1, 0)

a_n = [0] * (XMAX + 1)          # sum_{d|n} chi20(d), by sieve
for d in range(1, XMAX + 1):
    c = chi20(d)
    if c:
        for n in range(d, XMAX + 1, d):
            a_n[n] += c

r_n = [0] * (XMAX + 1)          # #{(a,b): a^2 + 5b^2 = n}
bmax = int((XMAX / 5) ** 0.5)
for b in range(-bmax, bmax + 1):
    amax = int((XMAX - 5 * b * b) ** 0.5)
    for a in range(-amax, amax + 1):
        n = a * a + 5 * b * b
        if 1 <= n <= XMAX:
            r_n[n] += 1

for n in range(1, XMAX + 1):
    ok(cnt_all[n] == a_n[n],
       "PR1a ideal count vs divisor-sum at n=%d: %d vs %d"
       % (n, cnt_all[n], a_n[n]))
for n in range(1, XMAX + 1):
    ok(2 * cnt_p0[n] == r_n[n],
       "PR1b principal count vs lattice/2 at n=%d: %d vs %d/2"
       % (n, cnt_p0[n], r_n[n]))
print("  PR1 CONFIRMED: #ideals(n) = sum_{d|n} chi_{-20}(d) and"
      " #principal(n) = r(n)/2 for all n <= %d" % XMAX)

for p in PRIMES:
    if p in (2, 5) or chi20(p) != 1:
        continue
    ok((r_n[p] > 0) == (p % 20 in (1, 9)), "genus rule at split p=%d" % p)
ok(r_n[2] == 0, "no element of norm 2 (P2 nonprincipal)")
ok(cnt_p0[4] == 1, "P2^2 = (2) principal")
ok(cnt_p0[9] == 3, "all three norm-9 ideals principal (incl. Q3^2)")
print("  genus rule verified on every split p <= %d; P2 nonprincipal,"
      " P2^2 = (2); Q3^2 principal (generator 2-sqrt(-5))" % XMAX)

LN = 5 * 10 ** 5


def lseries(beta, chi):
    return sum(chi(n) * n ** -beta for n in range(1, LN + 1))


zeta2 = math.pi ** 2 / 6
euler = 1.0
for s in SYMS:
    euler *= 1.0 / (1.0 - norm_sym(s) ** -2.0)
L2_20 = lseries(2.0, chi20)
zK2_formula = zeta2 * L2_20
ok(abs(euler - zK2_formula) < 4 / XMAX ** 0.5 * zK2_formula,
   "zeta_K(2) Euler %.6f vs formula %.6f" % (euler, zK2_formula))
ok(0.52 < 1 / zK2_formula < 0.56,
   "PR3 band: 1/zeta_K(2) = %.4f in (0.52, 0.56)" % (1 / zK2_formula))
print("  zeta_K(2) = %.6f (Euler over the symbol menu) = zeta(2)"
      " L(2, chi_{-20}) = %.6f; ideal-crystal probability"
      " 1/zeta_K(2) = %.6f" % (euler, zK2_formula, 1 / zK2_formula))

# ------------------------------------------------------------------ #
print("S2: the sensor criterion (element-coprimality is class-blind)")
# ------------------------------------------------------------------ #


def zsf(g):
    """C2 zero-sum-free: g trivial, or exactly one bit-1 prime at
    exponent 1 (any bit-0 prime, any square, or two bit-1 primes
    yields a principal subdivisor)."""
    if any(bit_sym(s) == 0 for s in g):
        return False
    if any(e >= 2 for e in g.values()):
        return False
    return len(g) <= 1


EL = elements_upto(120)
EL_FAC = {ab: elem_factor(*ab) for ab in EL}
hidden = []
for i in range(len(EL)):
    for j in range(i + 1, len(EL)):
        (a, b), (c, d) = EL[i], EL[j]
        na = a * a + 5 * b * b
        nc = c * c + 5 * d * d
        g_norm = math.gcd(na, nc)
        brute_coprime = True
        for (e, f) in EL:
            ne = e * e + 5 * f * f
            if g_norm % ne:
                continue
            if divides(a, b, e, f) and divides(c, d, e, f):
                brute_coprime = False
                break
        fa, fc = EL_FAC[(a, b)], EL_FAC[(c, d)]
        g = {s: min(e2, fc[s]) for s, e2 in fa.items() if s in fc}
        ok(brute_coprime == zsf(g),
           "PR2a sensor law at pair %s %s" % ((a, b), (c, d)))
        if brute_coprime and g:
            hidden.append(((a, b), (c, d), g))

ok(len(hidden) > 0, "hidden-coprime pairs exist (h = 2)")
ok(all(len(g) == 1 and list(g.values()) == [1] and
       bit_sym(next(iter(g))) == 1 for _, _, g in hidden),
   "PR2b collision budget: every hidden gcd = ONE nonprincipal prime"
   " (Davenport D(C2) - 1 = 1)")


def _norms_pair(t):
    n0 = t[0][0] ** 2 + 5 * t[0][1] ** 2
    n1 = t[1][0] ** 2 + 5 * t[1][1] ** 2
    return (max(n0, n1), min(n0, n1))


min_profile = min(_norms_pair(t) for t in hidden)
min_pairs = sorted(sorted(t[:2]) for t in hidden
                   if _norms_pair(t) == min_profile)
ok(min_pairs == [[(-1, 1), (2, 0)], [(1, 1), (2, 0)]],
   "norm-minimal hidden pairs are the conjugate twins"
   " {2, 1+-sqrt(-5)}: got %s" % (min_pairs,))
print("  PR2 CONFIRMED: %d hidden-coprime pairs among %d elements"
      " (norms <= 120); every hidden gcd is one nonprincipal prime;"
      " norm-minimal pairs = the conjugate twins {2, 1+-sqrt(-5)},"
      " gcd = P2" % (len(hidden), len(EL)))


def gauss_divides(a, b, c, d):
    n = c * c + d * d
    return (a * c + b * d) % n == 0 and (b * c - a * d) % n == 0


def gauss_gcd(a, b, c, d):
    while c or d:
        n = c * c + d * d
        q_re = round((a * c + b * d) / n)
        q_im = round((b * c - a * d) / n)
        a, b, c, d = c, d, a - (q_re * c - q_im * d), \
            b - (q_re * d + q_im * c)
    return a, b


GEL = []
for b in range(0, 8):
    for a in range(-7, 8):
        n = a * a + b * b
        if 2 <= n <= 60 and (b > 0 or a > 0):
            GEL.append((a, b))
gz_hidden = 0
for i in range(len(GEL)):
    for j in range(i + 1, len(GEL)):
        (a, b), (c, d) = GEL[i], GEL[j]
        brute_coprime = True
        for (e, f) in GEL:
            if gauss_divides(a, b, e, f) and gauss_divides(c, d, e, f):
                brute_coprime = False
                break
        ga, gb = gauss_gcd(a, b, c, d)
        ok(brute_coprime == (ga * ga + gb * gb == 1),
           "Z[i] sensor exact at %s %s" % ((a, b), (c, d)))
        if brute_coprime and ga * ga + gb * gb != 1:
            gz_hidden += 1
ok(gz_hidden == 0, "PR2c Z[i] control: zero hidden pairs")
print("  Z[i] control (h = 1): element-coprimality = ideal-coprimality"
      " on all %d pairs -- the sensor criterion's other leg"
      % (len(GEL) * (len(GEL) - 1) // 2))

# ------------------------------------------------------------------ #
print("S3: floor-2 transfer (the Dedekind zeta is the ideal world's"
      " partition function)")
# ------------------------------------------------------------------ #

IDE = []                        # (norm, {symbol: exp}) for norm <= 2000


def dfs_ideals(i, n, fac, cap, out):
    out.append((n, dict(fac)))
    for j in range(i, NSYM):
        nj = NORMS[j]
        if n * nj > cap:
            break
        m = n * nj
        e = 1
        while m <= cap:
            fac[SYMS[j]] = e
            dfs_ideals(j + 1, m, fac, cap, out)
            m *= nj
            e += 1
        del fac[SYMS[j]]


dfs_ideals(0, 1, {}, 2000, IDE)

beta = 2.0
P2S, P5S = ('r', 2), ('r', 5)
Q3, Q3B = (3, SQRTM5[3]), (3, 3 - SQRTM5[3])
Q7, Q7B = (7, SQRTM5[7]), (7, 7 - SQRTM5[7])
for state, sname in ((frozenset(), "1"),
                     (frozenset([P2S, Q3]), "(1+sqrt(-5))")):
    for P in (Q3B, P5S, Q7):
        NP = norm_sym(P)
        for d in (1, 2):
            lhs = sum(n ** -beta for n, f in IDE
                      if not (set(f) & state) and f.get(P, 0) >= d)
            rhs = NP ** (-beta * d) * sum(
                n ** -beta for n, f in IDE
                if not (set(f) & state) and n <= 2000 / NP ** d)
            ok(abs(lhs - rhs) < 1e-12,
               "PR3 matched-truncation mass identity state %s P=%s d=%d"
               % (sname, P, d))
print("  PR3 CONFIRMED: mass(coprime, v_P >= d) = N(P)^(-beta d) *"
      " mass(coprime, matched cap) EXACT -- the geometric-entry"
      " bijection, states 1 and (1+sqrt(-5)), atoms Q3bar/P5/Q7,"
      " d = 1, 2")

# in-universe MC: the 6 atoms of norm <= 10
UNIV = [P2S, Q3, Q3B, P5S, Q7, Q7B]
UN = [norm_sym(s) for s in UNIV]
UB = [bit_sym(s) for s in UNIV]
MENU = []                       # (exps, mask, norm, weight, parity)


def gen_menu(i, n, exps):
    if i == 6:
        if n > 1:
            mask = sum(1 << k for k in range(6) if exps[k])
            par = sum(e * b for e, b in zip(exps, UB)) % 2
            MENU.append((tuple(exps), mask, n, n ** -2.0, par))
        return
    m = n
    e = 0
    while m <= XMAX:
        exps[i] = e
        gen_menu(i + 1, m, exps)
        e += 1
        m *= UN[i]
    exps[i] = 0


gen_menu(0, 1, [0] * 6)
menu_id = MENU
menu_el = [mv for mv in MENU if mv[4] == 0]
print("  in-universe menu: %d ideal moves, %d element (principal)"
      " moves (6 atoms, norm cap %d)" % (len(menu_id), len(menu_el), XMAX))


def run_growth(menu, element_world, rg, cap=200):
    """Thermal D-IND in-universe. Returns (final exps, #hidden
    collisions, #self-square moves, absorbed, hidden-by-move-5)."""
    st = [0] * 6
    st_mask = 0
    hid = sq = 0
    hid5 = False
    for step in range(cap):
        adm = []
        cum = []
        s = 0.0
        for mv in menu:
            exps, mask, n, w, par = mv
            shared = mask & st_mask
            if shared:
                if not element_world:
                    continue
                if shared & (shared - 1):          # two+ shared atoms
                    continue
                k = shared.bit_length() - 1
                if UB[k] == 0 or min(exps[k], st[k]) != 1:
                    continue
            adm.append(mv)
            s += w
            cum.append(s)
        if not adm:
            return st, hid, sq, True, hid5
        exps, mask, n, w, par = weighted_sample(rg, cum, adm)
        if mask & st_mask:
            hid += 1
            if step < 5:
                hid5 = True
        if any(e >= 2 for e in exps):
            sq += 1
        for k in range(6):
            st[k] += exps[k]
        st_mask |= mask
    return st, hid, sq, False, hid5


RUNS = 400
rg = random.Random(15213)
id_crystal = 0
for _ in range(RUNS):
    st, hid, sq, absorbed, _ = run_growth(menu_id, False, rg)
    ok(absorbed, "ideal-world run absorbed")
    ok(hid == 0, "ideal world: no hidden collisions possible")
    if all(e <= 1 for e in st):
        id_crystal += 1
exact_iu = 1.0
for n in UN:
    exact_iu *= 1.0 - n ** -2.0
frac_id = id_crystal / RUNS
ok(abs(frac_id - exact_iu) <= 0.10,
   "PR3 ideal MC crystal %.3f vs in-universe exact %.3f"
   % (frac_id, exact_iu))
print("  ideal-world MC (%d runs): squarefree fraction %.3f vs"
      " in-universe exact prod(1 - N^-2) = %.3f; full-world crystal"
      " probability = 1/zeta_K(2) = %.4f -- the Dedekind zeta is the"
      " third member of the partition-function family (Riemann,"
      " rational, Dedekind)" % (RUNS, frac_id, exact_iu, 1 / zK2_formula))

# ------------------------------------------------------------------ #
print("S4: the element mismatch (atoms = minimal zero-sum sequences;"
      " Euler != Dirichlet, first divergence at norm 36)")
# ------------------------------------------------------------------ #

CAP4 = 200
IDE4 = []
dfs_ideals(0, 1, {}, CAP4, IDE4)
princ4 = [(n, f) for n, f in IDE4 if n > 1 and parity(f) == 0]


def is_min_zero_sum(f):
    tot = sum(f.values())
    if tot == 1:
        return all(bit_sym(s) == 0 for s in f)
    if tot == 2:
        return all(bit_sym(s) == 1 for s in f)
    return False


def has_proper_principal_divisor(f):
    items = list(f.items())

    def rec(i, cur):
        if i == len(items):
            nonempty = any(cur)
            proper = any(c < e for c, (_, e) in zip(cur, items))
            par = sum(c * bit_sym(items[k][0])
                      for k, c in enumerate(cur)) % 2
            return nonempty and proper and par == 0
        for c in range(items[i][1] + 1):
            if rec(i + 1, cur + [c]):
                return True
        return False

    return rec(0, [])


species = {'prime0': 0, 'pair11': 0}
irr_norms = []
for n, f in princ4:
    irr = not has_proper_principal_divisor(f)
    ok(irr == is_min_zero_sum(f),
       "PR4 species law at ideal norm %d %s" % (n, f))
    if irr:
        irr_norms.append(n)
        species['prime0' if sum(f.values()) == 1 else 'pair11'] += 1
print("  irreducible census (principal ideals, norm <= %d): %d"
      " principal primes + %d two-nonprincipal-prime atoms; species"
      " law exact (atoms = minimal zero-sum sequences over C2)"
      % (CAP4, species['prime0'], species['pair11']))

for (a, b) in ((2, 0), (3, 0), (1, 1)):
    n0 = a * a + 5 * b * b
    brute_irr = all(not (2 <= e * e + 5 * f * f < n0
                         and n0 % (e * e + 5 * f * f) == 0
                         and divides(a, b, e, f))
                    for (e, f) in EL)
    ok(brute_irr, "brute irreducibility of %s" % ((a, b),))

euler_c = [0] * (CAP4 + 1)      # multisets of atoms, by norm product
euler_c[1] = 1
for nn in irr_norms:
    for n in range(2, CAP4 + 1):
        if n % nn == 0 and euler_c[n // nn]:
            euler_c[n] += euler_c[n // nn]
dirich_c = [0] * (CAP4 + 1)     # elements (principal ideals), by norm
dirich_c[1] = 1
for n, f in princ4:
    dirich_c[n] += 1

first_div = next((n for n in range(1, CAP4 + 1)
                  if euler_c[n] != dirich_c[n]), None)
ok(first_div == 36,
   "PR4 first Euler/Dirichlet divergence at 36: got %s" % first_div)
print("  PR4 CONFIRMED: Euler-over-atoms = Dirichlet-over-elements"
      " for n < 36, split at n = 36 (Euler %d vs Dirichlet %d):"
      " 6 = 2*3 = (1+sqrt(-5))(1-sqrt(-5)) -- the ch.9 zeta-Euler"
      " mismatch at its classical home" % (euler_c[36], dirich_c[36]))

# ------------------------------------------------------------------ #
print("S5: the hidden collision in growth (the element crystal dies)")
# ------------------------------------------------------------------ #

menu5 = [mv for mv in menu_el if mv[2] <= 500]
Z1 = sum(w for _, _, _, w, _ in menu5)
p_col2 = 0.0
for exps1, mask1, n1, w1, _ in menu5:
    z2 = c2 = 0.0
    for exps2, mask2, n2, w2, _ in menu5:
        shared = mask2 & mask1
        if shared:
            if shared & (shared - 1):
                continue
            k = shared.bit_length() - 1
            if UB[k] == 0 or min(exps2[k], exps1[k]) != 1:
                continue
            z2 += w2
            c2 += w2
        else:
            z2 += w2
    if z2 > 0:
        p_col2 += (w1 / Z1) * (c2 / z2)
ok(p_col2 > 0, "PR5 exact 2-move hidden-collision probability > 0")
# the minimal-norm openings (total norm 4 + 6), both orders: 2 and
# 1+-sqrt(-5) share exactly P2 with min exponent 1
mv_two = next(m for m in menu_el if m[0] == (2, 0, 0, 0, 0, 0))
mv_a = next(m for m in menu_el if m[0] == (1, 1, 0, 0, 0, 0))
mv_b = next(m for m in menu_el if m[0] == (1, 0, 1, 0, 0, 0))
for first, second in ((mv_a, mv_two), (mv_b, mv_two),
                      (mv_two, mv_a), (mv_two, mv_b)):
    shared = first[1] & second[1]
    ok(shared == 1 and min(first[0][0], second[0][0]) == 1,
       "minimal opening admissible in either order: %s then %s"
       % (first[0], second[0]))
print("  exact 2-move opening (element menu, norm <= 500): P(hidden"
      " collision at move 2) = %.4f; minimal-norm openings: 2 and"
      " 1+-sqrt(-5) in either order, sharing exactly P2" % p_col2)

rg5 = random.Random(15214)
el_crystal = el_hid5 = el_hid_runs = 0
depth_p2 = []
for _ in range(RUNS):
    st, hid, sq, absorbed, hid5 = run_growth(menu_el, True, rg5)
    ok(absorbed, "element-world run absorbed")
    # THE ABSORPTION PROFILE LAW (in-universe, proved): at absorption
    # every bit-1 atom sits at depth >= 2 (its pure-square move
    # gen(P^2) is admissible at e = 0 AND at e = 1: min(2, 1) = 1 is
    # zero-sum-free) and every bit-0 atom has entered (its pure move
    # is admissible at e = 0).
    ok(all(st[k] >= 2 for k in range(6) if UB[k] == 1),
       "absorption profile: every nonprincipal atom at depth >= 2")
    ok(all(st[k] >= 1 for k in range(6) if UB[k] == 0),
       "absorption profile: every principal atom entered")
    if all(e <= 1 for e in st):
        el_crystal += 1
    if hid5:
        el_hid5 += 1
    if hid:
        el_hid_runs += 1
    depth_p2.append(st[0])
frac_el = el_crystal / RUNS
ok(frac_el == 0.0,
   "the element crystal is surely dead in-universe: fraction %.3f"
   % frac_el)
ok(frac_el < frac_id,
   "PR5 directional: element squarefree %.3f < ideal %.3f"
   % (frac_el, frac_id))
ok(el_hid_runs == RUNS, "every run collides (forced, not a leak)")
print("  element-world MC (%d runs): squarefree fraction %.3f (ideal"
      " world: %.3f); hidden collision within 5 moves %.3f; every"
      " absorbed run has ALL nonprincipal atoms at depth >= 2 (the"
      " absorption profile law; mean P2 depth %.2f) -- PR5's band"
      " MISSED because the truth is a LAW, not a leak: the class"
      " group forces the nonprincipal columns deep"
      % (RUNS, frac_el, frac_id, el_hid5 / RUNS,
         sum(depth_p2) / RUNS))

# floor-1 hypotheses on M_el (PR8): the mass identity, composite a
princ_all = [(n, f) for n, f in IDE if parity(f) == 0]
for a_sym, aname, na in (({P2S: 2}, "2", 4),
                         ({P2S: 1, Q3: 1}, "1+sqrt(-5)", 6),
                         ({Q3: 1, Q3B: 1}, "3", 9)):
    lhs = sum(n ** -2.0 for n, f in princ_all
              if all(f.get(s, 0) >= e for s, e in a_sym.items()))
    rhs = na ** -2.0 * sum(n ** -2.0 for n, f in princ_all
                           if n <= 2000 / na)
    ok(abs(lhs - rhs) < 1e-12,
       "PR8 mass identity w(aM_el) = w(a) w(M_el) at a = %s" % aname)
print("  PR8 CONFIRMED: M_el is cancellative with a summable"
      " character (mass identity exact at a = 2, 1+sqrt(-5), 3), so"
      " the floor-1 hot-limit theorem applies to the element world;"
      " P2 | (2) makes ideal-cofinality ride along")

# ------------------------------------------------------------------ #
print("S6: the partition split (genus reading) + the pole ratio"
      " (temperature reads the class number)")
# ------------------------------------------------------------------ #

acl_n = [0] * (XMAX + 1)        # coefficients of L(chi_{-4}) L(chi_5)
for d in range(1, XMAX + 1):
    cd = chi4(d)
    if not cd:
        continue
    for e in range(1, XMAX // d + 1):
        acl_n[d * e] += cd * chi5(e)
for n in range(1, XMAX + 1):
    ok(2 * cnt_p0[n] == a_n[n] + acl_n[n],
       "PR6 per-coefficient genus identity at n=%d" % n)
print("  PR6 CONFIRMED (strong form): #principal(n) = (a_n +"
      " (chi_{-4} * chi_5)(n))/2 for ALL n <= %d -- the element"
      " world's partition function is (zeta_K + L(chi_{-4})"
      " L(chi_5))/2, coefficient by coefficient" % XMAX)

CATALAN = 0.915965594177219
ok(abs(lseries(2.0, chi4) - CATALAN) < 1e-6, "L(2, chi_{-4}) = Catalan")
ok(abs(lseries(1.0, chi4) - math.pi / 4) < 1e-5, "L(1, chi_{-4}) = pi/4")
phi_gr = (1 + 5 ** 0.5) / 2
ok(abs(lseries(1.0, chi5) - 2 * math.log(phi_gr) / 5 ** 0.5) < 1e-5,
   "L(1, chi_5) = 2 ln(phi)/sqrt(5)")

L1_20 = lseries(1.0, chi20)
h_val = 2 * 20 ** 0.5 * L1_20 / (2 * math.pi)
ok(round(h_val) == 2 and abs(h_val - 2) < 1e-3,
   "PR7 class number from L(1, chi_{-20}): %.6f" % h_val)
print("  L(1, chi_{-20}) = %.6f -> h = w sqrt(20) L/(2 pi) = %.6f:"
      " the world self-reports h = 2 (analytic class number formula,"
      " classical)" % (L1_20, h_val))


def zeta_em(b, N=10 ** 5):
    s = sum(n ** -b for n in range(1, N + 1))
    return s + N ** (1 - b) / (b - 1) - 0.5 * N ** -b \
        + b / 12 * N ** (-b - 1)


ok(abs(zeta_em(2.0) - zeta2) < 1e-9, "Euler-Maclaurin zeta(2)")

ratios = {}
for b in (2.0, 1.2, 1.05):
    zK = zeta_em(b) * lseries(b, chi20)
    Lcl = lseries(b, chi4) * lseries(b, chi5)
    ratios[b] = ((zK + Lcl) / 2) / zK
ok(ratios[1.05] < ratios[1.2] < ratios[2.0],
   "PR6 pole trend: ratio decreasing toward the pole")
ok(0.50 < ratios[1.05] < 0.56, "PR6 band: ratio(1.05) = %.4f"
   % ratios[1.05])
ok(0.60 < ratios[2.0] < 0.78, "PR6 band: ratio(2) = %.4f" % ratios[2.0])
print("  the pole ratio zeta_princ/zeta_K: %.4f (beta 2) -> %.4f"
      " (1.2) -> %.4f (1.05) -> 1/h = 1/2 at the pole (classical"
      " residue equidistribution; the trend is the in-range witness):"
      " TEMPERATURE READS THE CLASS NUMBER"
      % (ratios[2.0], ratios[1.2], ratios[1.05]))

zpr_enum = sum(n ** -2.0 * cnt_p0[n] for n in range(1, XMAX + 1))
zpr_formula = (zK2_formula + lseries(2.0, chi4) * lseries(2.0, chi5)) / 2
ok(abs(zpr_enum - zpr_formula) < 4 / XMAX ** 0.5,
   "zeta_princ(2) enumerated %.6f vs split formula %.6f"
   % (zpr_enum, zpr_formula))
print("  zeta_princ(2) = %.6f (enumerated to %d) vs (zeta_K +"
      " L(chi_{-4}) L(chi_5))/2 = %.6f" % (zpr_enum, XMAX, zpr_formula))

# ------------------------------------------------------------------ #
print()
if FAILS:
    print("RESULT: %d/%d checks FAILED" % (len(FAILS), CHECKS))
    raise SystemExit(1)
print("RESULT: all %d checks pass" % CHECKS)
