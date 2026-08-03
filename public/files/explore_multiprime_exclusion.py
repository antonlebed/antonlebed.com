"""
The multiprime exclusion: the two-fat-slice exclusion extends to every
odd d with three or more prime factors (with multiplicity) whose least
prime is unsquared -- by a low-weight classification of cyclotomic
codewords (the gon theorem) and a coset collapse, derived by hand
before the runs whose record sits below.

CONTEXT. The realizability law's composite row
(explore_realizability.py; the two-prime closure in
explore_cover_exclusion.py + explore_staircase_reduction.py): for
d = q*q' two odd primes, no nonzero (Phi_d)-codeword lies in a
triangle exponent set E(A, B, D) at D <= q-2 -- proved at every odd
prime pair. Composites of THREE or more primes with a close second
prime (q_2 <= (3q-4)/2, q = q_min >= 11, d squarefree at q) kept only
the slice-forcing scope. The question: does the exclusion extend --
a reduction quotienting the extra channels, or a genuine new evader
shape?

Notation: d odd, Omega(d) >= 3 prime factors with multiplicity,
distinct primes q = q_1 < q_2 < ..., q^2 nmid d (L1 and L2 need only
d odd; L3 slices at a multiplicity-1 prime; the squarefree-at-q
condition enters at L5). (Phi_d) = the
cyclotomic cyclic code {c in F[T]/(T^d - 1) : c(zeta) = 0
at every primitive d-th root zeta}, over any field F with char(F)
coprime to d. E(A, B, D) = {A*i + B*j mod d : i, j >= 0, i + j <= D},
gcd(A, B, d) = 1, D <= q - 2. Standing corpus laws used: the
torsion-menu law (min distance of (Phi_M) is q_min(M), field-free),
the slice congruence (mod-f slices of a codeword are pairwise
congruent mod (Phi_{d/f}), both directions, d squarefree at f), the
line pigeonhole.

THE DERIVATION (by hand, before the engine; the run verifies each leg):

 L1 (criterion -- THE CYLINDER DECOMPOSITION). (Phi_d) =
    V_1 + ... + V_r, where V_i = functions on Z/d invariant under
    translation by d/q_i (equivalently: functions of every CRT channel
    except i). Fourier proof: c in (Phi_d) iff c-hat vanishes on
    units; V_i is exactly {c-hat supported on q_i | t}; the non-units
    are the union of the {q_i | t}, and assigning each non-unit t to
    its least prime divisor splits any codeword's transform. Both
    directions. At r = 2 this IS the tensor-sum evader form of the
    rook reduction.

 L2 (rule -- SLICE CAPACITY AT EVERY CLASS, EVERY MODULUS). For any
    divisor m | d with m > 1 (every prime of d exceeds D+1 since
    D <= q-2) and ANY class (A, B): every congruence class
    {e == w mod m} meets E in at most D+1 points. If gcd(A, m) = 1,
    each j <= D fixes i uniquely mod m and m > D leaves at most one
    i per j. Otherwise pick a prime f | gcd(A, m): B is a unit mod f
    (gcd(A, B, d) = 1), so B*j == w mod f pins j to at most one
    value below f > D; with j fixed, the i-solutions of
    A*i == w - B*j mod m form one progression with difference
    m / gcd(A, m) -- either 1 (a single i-run of that one j, <= D+1
    points) or a product of primes > D (at most one i). The prime
    case m = f is the mod-f slice bound used by L3.

 L3 (rule -- THE MISSED-RESIDUE KILL). If E misses a residue mod
    some prime f | d with f^2 nmid d, no nonzero codeword is
    supported in E: one mod-f slice is empty, so by slice congruence
    (which needs d squarefree at f) ALL slices lie in (Phi_{d/f})
    with weight <= D+1 = q-1 < q_min(d/f) (which is q_2 if f = q,
    else q) -- every slice is 0. Corollaries: (i) every class with A
    or B non-unit at a multiplicity-1 prime dies (f | A or f | B
    hits <= D+1 < f residues mod f); (ii) THE BIG-CHANNEL KILL: any
    multiplicity-1 prime factor f > |E| <= (D+1)(D+2)/2 forces a
    missed residue -- a third factor beyond q(q-1)/2 is excluded by
    arithmetic alone. (The census below counts a class as L3-killed
    only on a miss at a multiplicity-1 prime; every class is
    kernel-checked regardless, and L5 never needs L3.)

 L4 (rule -- THE GON THEOREM, the low-weight classification). For
    EVERY odd M: every nonzero w in (Phi_M) with wt(w) < 2*q_min(M)
    is a scalar gon -- a constant on one coset of the order-t
    subgroup for a prime t | M (weight exactly t; only primes
    t < 2*q_min occur). Induction on Omega(M).
    Base Omega = 1: (Phi_t) = span(1). Prime powers M = s^a:
    codewords have Fourier support on multiples of s, i.e. are
    pullbacks from Z/(M/s); wt = s * wt(pullback) < 2s forces a
    weight-1 pullback -- the s-gon. Mixed M = N * s^a (s the largest
    prime, N > 1): slices over Z/s^a are pairwise congruent mod
    (Phi_N) WITHIN each coset of the order-s subgroup (the span of
    the primitive s^a-characters is exactly the vectors with zero
    sums on each such coset; both directions -- at a = 1 there is
    one coset and this is the plain slice congruence). Budget
    < 2*q_min: a coset holding two DIFFERING slices contributes
    >= q_min(N) >= q_min (a nonzero (Phi_N)-difference), so at most
    one coset differs. If none differs, w is a pullback from
    Z/(M/s): wt = s * wt(pullback) < 2*q_min <= 2s forces the s-gon.
    If one coset differs: a zero slice in it puts all its slices in
    (Phi_N), each nonzero one costing >= q_min, so exactly one
    nonzero slice survives anywhere -- itself in (Phi_N) with
    wt < 2*q_min(N), by induction a gon of N, and one slice of a gon
    of N is a gon of M; no zero slice means s nonzero slices
    totalling >= (s - 2) + q_min >= 2*q_min (s >= q_min + 2 for
    N > 1) -- over budget. At omega = 2 squarefree the
    classification is also checked exhaustively below by
    value-profile sweep (P5); at prime-power and mixed M it is
    spot-verified by kernel (PX).

 L5 (rule -- THE COSET COLLAPSE, the exclusion). d odd, Omega(d) >=
    3, q^2 nmid d, q = q_min. Let c be a nonzero codeword in E, any
    class. Slice by q (d squarefree at q, >= 3 slices). (a) Pairwise
    slice differences lie in (Phi_M), M = d/q, with weight <=
    2(D+1) <= 2q - 2 < 2*q_min(M) = 2*q_2: by L4 each is 0 or a
    scalar gon of M. (b) Coherence: differences on two DIFFERENT
    gons blow the budget (same-prime distinct cosets are disjoint,
    weight 2t >= 2*q_2 > 2q - 2; different-prime cosets meet in <= 1
    point, weight >= t + t' - 2 >= 2*q_2 - 2 > 2q - 2) -- so
    gamma_x = gamma + mu_x * G for ONE common gon G, a coset of the
    order-t subgroup of Z/M. (c) Off supp(G), a nonzero gamma(w)
    would put the full line {e == w mod M} (q points) inside E
    against L2 at modulus M, capacity D+1 < q: so supp(c) sits
    inside one coset of the order-(t*q) subgroup of Z/d. (d) THE
    MENU-LAW FINISH: that coset is {e == c0 mod d/(t*q)}, and
    Omega(d) >= 3 keeps d/(t*q) > 1, so L2 at modulus d/(t*q) caps
    |supp c| <= D+1 = q - 1 -- strictly below
    q_min(d) = q, the minimum distance of (Phi_d) itself (the menu
    law). c = 0. (At Omega = 2 the coset is all of Z/d and the
    finish fails -- exactly where the two-prime machinery was
    needed.)

 THE THEOREM (rule, proved; the census below is verification): for
 every odd d with Omega(d) >= 3 and q_min^2 nmid d, no nonzero
 (Phi_d)-codeword lies in any triangle E(A, B, D) with D <=
 q_min - 2. Field-free (char coprime to d). With the two-prime
 exclusion (Omega = 2) and the corpus's q_min^2 | d mechanism, THE
 COMPOSITE LAW CLOSES: D_min(d) = q_min(d) - 1 is a proved rule at
 every odd composite non-prime-power d (realization: the q-gon is a
 coset of the order-q subgroup <d/q>, so it enters at D = q - 1 via
 A = d/q, B = 1 -- one factor of q removed, which stays right when
 q^2 | d).

 (Freeze record: L1-L3, L4 at squarefree M, L5 with a third-prime
 finish, and P1-P9 were frozen before the engine's first run; the L4
 generalization to every odd M, the menu-law finish that replaced
 L5(d), and PX were derived and frozen after that run LAUNCHED but
 before any of its output was read, and the whole engine was rerun
 for the single record below.)

PREDICTIONS (stated before the run; a nonzero kernel vector at any
open-zone class in P6/P7/P9 is THE REFUTING WITNESS -- printed with
its class, it falsifies L4/L5 and the composite row keeps a new
evader shape instead):
 P1 (controls, run first): at d = 143 the kernel finder returns a
    codeword on a full gon coset, none on the coset minus one point,
    and none on E(1, 2, 9) (a class the two-prime sweep closed).
 P2 (L1): at d = 2431 a random sparse-Fourier codeword splits into
    three translation-invariant cylinders summing to it; conversely a
    random cylinder sum evaluates to zero at random unit characters.
 P3 (slice congruence): at d = 2431, both directions at all three
    slicing primes -- slice differences of the P2 codeword pass
    membership in the inner code; a slice system built as
    gamma_0 + (Phi_M)-words assembles to a codeword.
 P4 (L2): slice sizes <= D+1 at every prime for every swept class,
    non-unit classes included.
 P5 (L4 base, exhaustive at omega = 2): value-profile/matching sweep
    at (q, q') = (11, 13) and (13, 17): the achievable nonzero
    weights below 2q are exactly {q, q'}, on the single-column and
    single-row profiles alone; weight exactly 2q is achievable
    (the classification is sharp).
 P6 (THE CENSUS -- the verification sweep): kernel EMPTY at every
    class at d = 2431, 2717, 3289 (zone (11,13), D = 9) and 4199
    (zone (13,17), D = 11): every unit B up to inversion, plus
    non-unit controls at 2431. The split arithmetic-killed (L3
    applies: some residue missed) vs needs-rank is printed per d.
 P7 (L3 big-channel): at d = 11*13*59 = 8437 every unit class misses
    a residue mod 59 (|E| = 55 < 59); five kernel spot-checks empty.
 P8 (sharpness control): at d = 2431, class (A, B) = (221, 1) at
    D = q-1 = 10 the kernel is NONZERO -- the gon enters exactly one
    degree above the excluded range.
 P9 (r = 4): at d = 11*13*17*19 = 46189 (same zone, D = 9), 300
    sampled unit classes all empty.
 PX (the tenth prediction, the strengthened scope; frozen before the second run): (i) the
    gon theorem spot-verified at prime-power M = 169 and mixed
    M = 1859: kernel finds exactly the scalar gon on a full gon
    coset, nothing on the coset minus a point, and nothing on 30
    random supports of size 2*q_min - 1 containing no full gon
    coset; (ii) THE MIXED CENSUS: kernel EMPTY at every class at
    d = 1859 = 11*13^2 (zone (11,13), D = 9) and d = 3757 = 13*17^2
    (zone (13,17), D = 11). The arithmetic-kill split counts only
    misses at multiplicity-1 primes (L3's licensed scope -- the
    slice congruence needs d squarefree at the slicing prime).

RESULTS (the run below prints the record; all confirmed, no witness):
  P1 controls exact at d = 143 (p = 859): gon coset found as a scalar
     gon, coset-minus-one and E(1, 2, 9) empty.
  P2/P3 all green at d = 2431 (p = 29173): decomposition pointwise
     with invariant pieces, both random constructions vanish at 150
     random unit characters, slice differences pass membership at all
     three slicing primes, the assembled slice system is a codeword.
  P5 profile sweep: weights found in (0, 2q] are exactly [q, q', 2q]
     at both (11,13) and (13,17); below 2q only the single-column
     (weight q) and single-row (weight q') profiles; 2q achievable.
  P6 THE CENSUS -- kernel EMPTY at every class:
       2431 = 11*13*17,  D = 9:  972 classes (229 L3-killed, 743 rank)
       2717 = 11*13*19,  D = 9:  1084 classes (242 / 842)
       3289 = 11*13*23,  D = 9:  1324 classes (433 / 891)
       4199 = 13*17*19,  D = 11: 1732 classes (329 / 1403)
     with slice capacity <= D+1 at every prime, every class, and the
     eight non-unit control classes at 2431 empty.
  P7 all 3484 unit classes at 8437 = 11*13*59 miss a residue mod 59;
     five kernel spot-checks empty.
  P8 sharpness: at d = 2431, class (221, 1), D = 10, the kernel is
     exactly the scalar 11-gon {221*i} -- the exclusion boundary is
     tight.
  P9 r = 4: 300 sampled classes at 46189 = 11*13*17*19 all empty
     (75 L3-killed, 225 rank).
  PXa gon theorem at M = 169 and both gon orders of M = 1859: the
     coset carries exactly a scalar gon, the coset minus a point and
     30 random gon-free supports of size 2*q_min - 1 carry nothing.
  PXb THE MIXED CENSUS -- kernel EMPTY at every class:
       1859 = 11*13^2,  D = 9:  782 classes (79 L3-killed, 703 rank)
       3757 = 13*17^2,  D = 11: 1634 classes (137 / 1497)

Tier: L1-L5 and the theorem rule/criterion (proved as derived above;
every leg code-verified as stated -- the census at the six smallest
close-zone moduli plus the r = 4 sample stands as the verification
sweep, 7828 kernel calls, no witness anywhere). The composite law
D_min(d) = q_min(d) - 1 (explore_realizability.py P4) is now a proved
rule at every odd composite non-prime-power d: prime powers by the
line pigeonhole, q_min^2 | d by the slice forcing, two-prime d by the
rook reduction + staircase lemma (explore_cover_exclusion.py,
explore_staircase_reduction.py), and everything else -- Omega >= 3,
q_min^2 nmid d, squarefree or not -- by the gon theorem + coset
collapse here.

Classical contacts: the gon theorem is a below-2d minimum-weight
classification for the repetition-like cyclotomic ideal, cousin to
minimum-weight-word classifications for cyclic codes (the BCH-bound
regime); the coset collapse is a torsion-coset statement, Lang's
theorem's finite shadow one level up from the fiber criterion.

Run: 88.3 s, tiny memory, 47 checks green.
"""

import random, time
from math import gcd

random.seed(615)
T0 = time.time()

CHECKS = 0
def check(cond, msg):
    global CHECKS
    CHECKS += 1
    print(f"  [{'ok' if cond else 'FAIL'}] {msg}")
    assert cond, msg

def section(t):
    print(); print("=" * 72)
    print(f"{t}   [t={time.time()-T0:.1f}s]"); print("=" * 72)

# ---------------------------------------------------------------- helpers

def is_prime(n):
    if n < 2: return False
    q = 2
    while q * q <= n:
        if n % q == 0: return False
        q += 1
    return True

def factorize(n):
    fs, q = {}, 2
    while q * q <= n:
        while n % q == 0:
            fs[q] = fs.get(q, 0) + 1
            n //= q
        q += 1
    if n > 1: fs[n] = fs.get(n, 0) + 1
    return fs

def mult_order(x, p):
    o, t = 1, x % p
    assert t != 0
    while t != 1:
        t = t * x % p
        o += 1
    return o

def primitive_root(p):
    n = p - 1
    qs = list(factorize(n))
    for g in range(2, p):
        if all(pow(g, n // q, p) != 1 for q in qs):
            return g

def units_mod(n):
    return [u for u in range(n) if gcd(u, n) == 1]

def exponent_set(A, B, D, d):
    E = set()
    for i in range(D + 1):
        for j in range(D + 1 - i):
            E.add((A * i + B * j) % d)
    return sorted(E)

def find_p(d):
    """Smallest prime p == 1 mod d."""
    p = d + 1
    while not is_prime(p):
        p += d
    return p

# ------------------------------------------------- the kernel machinery
# (the tester from explore_realizability.py, copied verbatim -- scripts
#  stay standalone)

class CodeTester:
    """Codewords of (Phi_d) over F_p, p = 1 mod d: c with c(zeta) = 0
    at every primitive d-th root zeta. kernel(E) returns a nonzero
    codeword supported on E (as a dict e -> coeff) or None."""

    def __init__(self, d, p):
        assert is_prime(p) and (p - 1) % d == 0, (d, p)
        self.d, self.p = d, p
        g = primitive_root(p)
        z = pow(g, (p - 1) // d, p)
        assert mult_order(z, p) == d
        self.zpow = [pow(z, t, p) for t in range(d)]
        self.units = units_mod(d)

    def kernel(self, E):
        d, p, zp = self.d, self.p, self.zpow
        cols = len(E)
        pivots = {}
        order = []
        for u in self.units:
            row = [zp[(u * e) % d] for e in E]
            for c in order:
                f = row[c]
                if f:
                    pr = pivots[c]
                    row = [(x - f * y) % p for x, y in zip(row, pr)]
            lead = next((c for c in range(cols) if row[c]), None)
            if lead is None:
                continue
            inv = pow(row[lead], p - 2, p)
            row = [x * inv % p for x in row]
            for c in order:
                f = pivots[c][lead]
                if f:
                    pivots[c] = [(x - f * y) % p
                                 for x, y in zip(pivots[c], row)]
            pivots[lead] = row
            order.append(lead)
            if len(order) == cols:
                return None
        free = next(c for c in range(cols) if c not in pivots)
        vec = {E[free]: 1}
        for c, prow in pivots.items():
            v = (-prow[free]) % p
            if v: vec[E[c]] = v
        for u in self.units:
            s = sum(co * zp[(u * e) % d] for e, co in vec.items()) % p
            assert s == 0, "kernel vector fails codeword condition"
        return vec

# ---------------------------------------------------------- P1: controls

section("P1: CONTROLS at d = 143 = 11*13")
d0 = 143
p0 = find_p(d0)
print(f"  p = {p0}")
t0 = CodeTester(d0, p0)
gon = [e for e in range(d0) if e % 13 == 5]      # coset of order-11 subgroup
w = t0.kernel(gon)
check(w is not None, f"gon coset (11 points, e == 5 mod 13): codeword FOUND")
check(set(w) <= set(gon) and len(w) == 11 and len(set(w.values())) == 1,
      "the found codeword is the full coset at one constant (a scalar gon)")
w2 = t0.kernel(gon[:-1])
check(w2 is None, "coset minus one point: NO codeword")
w3 = t0.kernel(exponent_set(1, 2, 9, d0))
check(w3 is None, "E(1, 2, 9) at 143 (two-prime closed class): kernel empty")

# ------------------------------------- P2: the cylinder decomposition

section("P2: THE CYLINDER DECOMPOSITION at d = 2431 = 11*13*17")
d = 2431
PR = [11, 13, 17]
p = find_p(d)
print(f"  p = {p}")
tester = CodeTester(d, p)
zp = tester.zpow

# random sparse-Fourier codeword: c-hat supported on 40 random non-units
nonunits = [t for t in range(d) if gcd(t, d) > 1]
supp_hat = random.sample(nonunits, 40)
coef = {t: random.randrange(1, p) for t in supp_hat}
c = [sum(a * zp[(t * e) % d] for t, a in coef.items()) % p
     for e in range(d)]
# decomposition: assign each t to its least prime divisor among PR
parts = {f: {} for f in PR}
for t, a in coef.items():
    f = next(f for f in PR if t % f == 0)
    parts[f][t] = a
cyl = {f: [sum(a * zp[(t * e) % d] for t, a in parts[f].items()) % p
           for e in range(d)] for f in PR}
check(all((cyl[11][e] + cyl[13][e] + cyl[17][e]) % p == c[e]
          for e in range(d)), "c = c_11 + c_13 + c_17 pointwise")
ok_inv = all(all(cyl[f][e] == cyl[f][(e + d // f) % d] for e in range(d))
             for f in PR)
check(ok_inv, "each piece is invariant under translation by d/q_i")
us = random.sample(tester.units, 150)
check(all(sum(c[e] * zp[(u * e) % d] for e in range(d)) % p == 0
          for u in us),
      "c vanishes at 150 random unit characters (codeword)")
# converse: a random cylinder sum is a codeword
cc = [0] * d
tabs = {f: [random.randrange(p) for _ in range(d // f)] for f in PR}
for e in range(d):
    cc[e] = (tabs[11][e % 221] + tabs[13][e % 187] + tabs[17][e % 143]) % p
check(all(sum(cc[e] * zp[(u * e) % d] for e in range(d)) % p == 0
          for u in random.sample(tester.units, 150)),
      "a random cylinder sum vanishes at 150 random unit characters")

# ------------------------------------------- P3: the slice congruence

section("P3: SLICE CONGRUENCE at d = 2431, all three slicing primes")

def inner_unit_evals(vec_on_M, M, n_evals):
    """Evaluate a vector on Z/M at random unit characters of Z/M,
    inside F_p via the M-th root zp[d//M]."""
    zM = [zp[(d // M) * t % d] for t in range(M)]
    uM = units_mod(M)
    for u in random.sample(uM, min(n_evals, len(uM))):
        yield sum(a * zM[(u * w) % M] for w, a in enumerate(vec_on_M)) % p

for f in PR:
    M = d // f
    slices = {z: [0] * M for z in range(f)}
    for e in range(d):
        slices[e % f][e % M] = c[e]
    ok = True
    for z1, z2 in [(0, 1), (1, 2), (0, f - 1)]:
        diff = [(a - b) % p for a, b in zip(slices[z1], slices[z2])]
        ok = ok and all(v == 0 for v in inner_unit_evals(diff, M, 40))
    check(ok, f"slicing by {f}: slice differences vanish at 40 random "
              f"unit characters of Z/{M} (membership in (Phi_{M}))")

# converse: assemble gamma_0 + (Phi_221)-words over the 11-channel
M = 221
g0 = [random.randrange(p) for _ in range(M)]
gam = {}
for z in range(11):
    u1 = [random.randrange(p) for _ in range(17)]
    v1 = [random.randrange(p) for _ in range(13)]
    gam[z] = [(g0[w] + u1[w % 17] + v1[w % 13]) % p for w in range(M)]
casm = [gam[e % 11][e % M] for e in range(d)]
check(all(sum(casm[e] * zp[(u * e) % d] for e in range(d)) % p == 0
          for u in random.sample(tester.units, 100)),
      "assembled slice system (gamma_0 + inner codewords) is a codeword")

# ------------------------- P5: the gon theorem's omega = 2 base, exhaustive

section("P5: LOW-WEIGHT CLASSIFICATION, exhaustive profile sweep")

def partitions(n, mx=None):
    if mx is None: mx = n
    if n == 0:
        yield []
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield [k] + rest

def profile_sweep(q, qp):
    """All achievable weights w in (0, 2q] of nonzero words
    g(x) + f(y) on Z/q x Z/qp, via value profiles + all matchings.
    Returns {w: set of (pa, pb) profiles}."""
    lo = q * qp - 2 * q          # need matched sum s >= lo, s < q*qp
    found = {}
    pas = [tuple(x) for x in partitions(q)]
    pbs = [tuple(x) for x in partitions(qp)]
    for pa in pas:
        for pb in pbs:
            k = min(len(pa), len(pb))
            best = sum(a * b for a, b in zip(pa[:k], pb[:k]))
            if best < lo:
                continue
            sums = set()
            def dfs(i, used, s, rem_best):
                if s + rem_best < lo:
                    return
                if i == len(pa):
                    sums.add(s)
                    return
                avail = [b for j, b in enumerate(pb) if not used & (1 << j)]
                rb = sum(a * b for a, b in
                         zip(pa[i + 1:], sorted(avail, reverse=True)))
                dfs(i + 1, used, s, rb)          # pa[i] unmatched
                for j, b in enumerate(pb):
                    if used & (1 << j): continue
                    avail2 = [bb for jj, bb in enumerate(pb)
                              if not used & (1 << jj) and jj != j]
                    rb2 = sum(a * bb for a, bb in
                              zip(pa[i + 1:], sorted(avail2, reverse=True)))
                    dfs(i + 1, used | (1 << j), s + pa[i] * b, rb2)
            dfs(0, 0, 0, best)
            for s in sums:
                if lo <= s < q * qp:
                    w = q * qp - s
                    found.setdefault(w, set()).add((pa, pb))
    return found

for (q, qp) in [(11, 13), (13, 17)]:
    found = profile_sweep(q, qp)
    below = {w: ps for w, ps in found.items() if w < 2 * q}
    print(f"  ({q},{qp}): weights found in (0, 2q]: {sorted(found)}")
    check(sorted(below) == [q, qp],
          f"({q},{qp}): nonzero weights below 2q are exactly {{{q}, {qp}}}")
    check(below[q] == {((q,), (qp - 1, 1))},
          f"({q},{qp}): weight {q} only from the single-column profile")
    check(below[qp] == {((q - 1, 1), (qp,))},
          f"({q},{qp}): weight {qp} only from the single-row profile")
    check(2 * q in found,
          f"({q},{qp}): weight exactly 2q achievable (sharp)")

# --------------------------------------- P4 + P6: THE CENSUS (r = 3)

section("P4 + P6: THE CENSUS -- kernel at every class, four moduli")

def census(d, D, extra_classes=(), sample=None):
    fd = factorize(d)
    fs = sorted(fd)
    label = '*'.join(str(f) if fd[f] == 1 else f"{f}^{fd[f]}"
                     for f in fs)
    p = find_p(d)
    tester = CodeTester(d, p)
    Bs = [B for B in tester.units if B <= pow(B, -1, d)]
    classes = [(1, B) for B in Bs] + list(extra_classes)
    if sample is not None:
        classes = ([(1, B) for B in random.sample(Bs, sample)]
                   + list(extra_classes))
    n_arith = n_rank = 0
    cap_ok = True
    witnesses = []
    for idx, (A, B) in enumerate(classes):
        E = exponent_set(A, B, D, d)
        missed = False
        for f in fs:
            szs = [0] * f
            for e in E:
                szs[e % f] += 1
            if max(szs) > D + 1:
                cap_ok = False
            if 0 in szs and fd[f] == 1:
                missed = True
        if missed: n_arith += 1
        else: n_rank += 1
        w = tester.kernel(E)
        if w is not None:
            witnesses.append(((A, B), w))
        if (idx + 1) % 400 == 0:
            print(f"    ... {idx + 1}/{len(classes)} classes "
                  f"[t={time.time()-T0:.0f}s]")
    print(f"  d = {d} = {label}, D = {D}, p = {p}: "
          f"{len(classes)} classes, {n_arith} arithmetic-killed (L3), "
          f"{n_rank} needed rank")
    check(cap_ok, f"d = {d}: slice capacity <= D+1 at every prime, "
                  f"every class (L2)")
    check(not witnesses,
          f"d = {d}: kernel EMPTY at all {len(classes)} classes"
          + (f" -- WITNESS AT {witnesses[0][0]}" if witnesses else ""))
    return witnesses

NONUNIT = [(11, 1), (1, 11), (13, 1), (17, 1), (143, 1), (11, 13),
           (13, 17), (221, 2)]
census(2431, 9, extra_classes=NONUNIT)
census(2717, 9)          # 11*13*19
census(3289, 9)          # 11*13*23
census(4199, 11)         # 13*17*19, zone (13,17)

# ------------------------------------------- P7: the big-channel kill

section("P7: THE BIG-CHANNEL KILL at d = 8437 = 11*13*59")
d7 = 8437
D7 = 9
u7 = units_mod(d7)
B7 = [B for B in u7 if B <= pow(B, -1, d7)]
miss_all = True
for B in B7:
    E = exponent_set(1, B, D7, d7)
    if len(set(e % 59 for e in E)) == 59:
        miss_all = False
check(miss_all, f"all {len(B7)} unit classes miss a residue mod 59 "
                f"(|E| <= 55 < 59): arithmetic exclusion")
p7 = find_p(d7)
print(f"  p = {p7}")
t7 = CodeTester(d7, p7)
spot = random.sample(B7, 5)
check(all(t7.kernel(exponent_set(1, B, D7, d7)) is None for B in spot),
      "five kernel spot-checks empty")

# ------------------------------------------- P8: sharpness at D = q-1

section("P8: SHARPNESS -- the gon enters at D = q-1")
E8 = exponent_set(221, 1, 10, 2431)
w8 = tester.kernel(E8)
check(w8 is not None, "d = 2431, class (221, 1), D = 10: codeword FOUND")
gon8 = set(range(0, 2431, 221))
check(set(w8) == gon8 and len(set(w8.values())) == 1,
      "and it is exactly the scalar 11-gon {221*i}")

# ------------------------------------------------- P9: the r = 4 sample

section("P9: r = 4 SAMPLE at d = 46189 = 11*13*17*19")
census(46189, 9, sample=300)

# ---------------------------- PX: the strengthened scope (mixed d)

section("PXa: THE GON THEOREM at prime-power and mixed M")
for (M, t) in [(169, 13), (1859, 11), (1859, 13)]:
    pM = find_p(M)
    tM = CodeTester(M, pM)
    step = M // t                     # order-t subgroup = <M/t>
    coset = sorted((3 + k * step) % M for k in range(t))
    wg = tM.kernel(coset)
    check(wg is not None and set(wg) == set(coset)
          and len(set(wg.values())) == 1,
          f"M = {M}: the order-{t} gon coset carries exactly a "
          f"scalar gon")
    check(tM.kernel(coset[:-1]) is None,
          f"M = {M}: the coset minus a point carries nothing")
    qmin = min(factorize(M))
    csets = [set((c0 + k * (M // f)) % M for k in range(f))
             for f in sorted(factorize(M)) for c0 in range(M // f)]
    tried = 0
    ok_rand = True
    while tried < 30:
        S = set(random.sample(range(M), 2 * qmin - 1))
        if any(cs <= S for cs in csets):
            continue
        tried += 1
        if tM.kernel(sorted(S)) is not None:
            ok_rand = False
    check(ok_rand, f"M = {M}: 30 random gon-free supports of size "
                   f"{2*qmin-1} carry nothing")

section("PXb: THE MIXED CENSUS")
census(1859, 9)          # 11*13^2, zone (11,13)
census(3757, 11)         # 13*17^2, zone (13,17)

print()
print("=" * 72)
print(f"ALL CHECKS PASSED ({CHECKS})   total {time.time()-T0:.1f} s")
print("=" * 72)
