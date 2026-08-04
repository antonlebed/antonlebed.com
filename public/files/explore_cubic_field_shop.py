r"""explore_cubic_field_shop.py -- shopping for the first cubic ring that
is both CLASSED and HEADED: enumerate cubic fields by |discriminant|,
certify every class number on the way, and stop at the first field with
h > 1 whose cheapest place carries a head.

THE QUESTION. Every walkable ring in this corpus with a nontrivial class
group is quadratic, and every cubic ring it has walked is headless -- so
three separate questions (does the walk survive residue degree 3, does the
element price exist at h > 1, what width the image carries at degree 3)
all dead-end at the same missing instrument: a cubic ring with h > 1 whose
CHEAPEST place is headed. A head the walk cannot reach decides nothing --
explore_cubic_ring.py F5 shows a ring whose cheapest place is headless
locks at its first move and every informative state is a planted one --
so the shopping condition is on the cheapest place, not on the ring
having a head somewhere. This file is the shop: it does not walk
anything; it finds and certifies the ring the walker is then ported onto.

THE HEAD CRITERION, carried in at its surviving form (explore_head_width.py
F2, a rule in range over 24 places in 21 local fields): a place is headed
iff f = 1, e = (p-1)p^t, and mu_p lies in the completion -- never the
earlier reading p - 1 <= e. Consequences used here, each read back off a
brute ladder rather than trusted: a norm-2 place (f = 1, p = 2, mu_2
automatic) is headed iff e is 1 or 2 (e = 2^t; e = 3 fails the form); a
norm-3 place is headed iff e = 2 AND the completion is Q_3(zeta_3), which
is one of several ramified quadratic extensions and cannot be read off
(p, e, f) alone; f >= 2 is headless outright. The brute ladder's excess
(longest run of one lambda value, less e) is the verdict; the criterion
is the prediction beside it.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. The shopping
spec is written in the CLASS FIELD's own words -- discriminant order,
Minkowski bound, principality, Round-2 maximality -- and not in the
walker's, because what is under test here is arithmetic existence (which
field is first), not dynamics. The one walker-owned word, HEADED, enters
only through the brute ladder the walker family already trusts.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 From the quadratic engines to this shop: NOTHING about class groups
    is carried except three filed control values (h = 1 for Z[i], h = 2
    = C2 for Z[sqrt(-5)], h = 3 = C3 for Z[w] -- explore_number_field_lock.py
    and explore_module_law.py). The h-engine here must REPRODUCE all
    three at degree 2 before its cubic readings are admissible.
 T2 From literature memory: the expectation that the winner is the
    complex cubic of discriminant -283 with h = 2 is a REMEMBERED table
    value, not a derivation, and is frozen as an expectation the engine
    is free to refute. Nothing downstream assumes it.
 T3 From Hunter's theorem: the completeness of the enumeration rests on
    the cited bound (Cohen, A Course in Computational Algebraic Number
    Theory, Thm 6.4.2): every cubic field K contains theta, not in Q,
    with 0 <= Tr(theta) <= 3/2 and
    T2(theta) = sum |theta_i|^2 <= Tr^2/3 + (2/sqrt 3) * (|d_K|/3)^(1/2).
    A cubic field has no intermediate fields, so any such theta GENERATES
    K. The bound is a cited theorem, not re-proved here; everything
    downstream of it is verified independently per field.

THE HAND-ATTACK, on paper before any engine code.

  THE BOX. For |d_K| <= 600: T2 <= 1/3 + (2/sqrt 3)*sqrt(200) = 16.66.
  With s1 = Tr in {0, 1}: |s2| = |(s1^2 - Tr(theta^2))/2| and
  |Tr(theta^2)| = |sum theta_i^2| <= T2, so |s2| <= (1 + 16.66)/2 = 8.83
  -> |s2| <= 8. |s3| = prod |theta_i| <= (T2/3)^(3/2) = 13.08 -> 13.
  x^3 - s1 x^2 + s2 x - s3: 2 * 17 * 27 = 918 polynomials, minus the
  reducible (s3 = 0 or a rational root). Every cubic field with
  |d_K| <= 600 appears, possibly only through a generator of index > 1.

  THE INDEX. disc(poly) = ind^2 * d_K, so a poly with large disc can
  still name a small field, and a field can appear ONLY through
  non-maximal generators (2 is a common index divisor exactly when 2
  splits completely, and then EVERY generator has even index). So the
  shop cannot skip non-maximal polynomials: each order is p-maximalized
  by Round-2 -- the radical-idealizer step: with J' the full preimage of
  the nilradical of O/pO, the enlargement is (1/p){y : y J' <= p J'},
  computed as F_p-linear algebra -- at every p with p^2 | disc, and d_K
  is the maximal order's discriminant. All downstream ideal work is done
  in the MAXIMAL order via its integer multiplication table, so index
  primes are handled, not dodged. Places over p are read off the algebra
  O/pO itself: nilradical by iterated-Frobenius kernel, then the
  semisimple quotient split by idempotents from coprime minimal-
  polynomial factors, each field component's kernel a maximal ideal.

  THE CLASS NUMBER. Minkowski: every ideal class contains an integral
  ideal of norm <= (4/pi)^s * (n!/n^n) * sqrt|d|. If every prime ideal
  of norm under the bound is PRINCIPAL -- a generator found by direct
  search -- then h = 1, certified constructively. If some place resists:
  an upper structure comes from relations (smooth principal elements
  over the places above the primes to 29, Smith normal form: the
  quotient Z^k by the found relations SURJECTS onto Cl, so its order H
  is finite only at full rank and h then divides H; H = 1 certifies
  h = 1), and the lower bound from a NON-PRINCIPALITY CERTIFICATE: in a
  complex cubic (unit rank 1) a generator of an ideal of norm m can be
  unit-reduced until its real embedding lies in [m^(1/3)/sqrt(u),
  m^(1/3)*sqrt(u)] for ANY known unit of real absolute value u > 1 --
  fundamental or not; a non-fundamental unit only pads the box -- which
  bounds all three embeddings and hence the coefficients: an exhausted
  box with no generator is a proof. h = 2 needs one certificate (h | 2,
  h > 1); h = 3 likewise; other H handled loudly if they occur. A
  totally real candidate (unit rank 2) would need a 2-dimensional
  reduction this file does not implement: if one surfaces before the
  winner it is reported as UNRESOLVED and the first-claim is conditional
  (the remembered tables put the first totally real h > 1 far above this
  range, and the engine will say what it found either way).

  THE IDENTITY ASSUMPTION. Two polynomials name the same field iff same
  d_K and same splitting shapes at every fingerprint prime dividing
  neither polynomial discriminant (primes to 300). At degree 3 there is
  no arithmetic equivalence (that starts at degree 7), so distinct
  fields sharing d_K separate at some prime; the finite fingerprint is
  the one identification assumption this file makes, and merges are the
  only thing it affects.

PREDICTIONS, fixed before the engine ran, each naming what the rig PRINTS.
  P1 The degree-2 h-engine prints h = 1, 2, 3 for Z[i], Z[sqrt(-5)],
     Z[w], with a small place of the latter two certified non-principal
     by an exhausted box and the SNF order equal to the filed h. 0
     disagreements with the filed values.
  P2 The cubic enumeration's least |d| complex field is d = -23 with
     h = 1 certified (the field of explore_cubic_ring.py, whose
     Minkowski bound 1.36 < 2 makes h = 1 vacuous there), and the least
     totally real is d = 49.
  P3 The shop prints a first h > 1 field within |d| <= 600, and it is
     complex. (T2's remembered expectation: d = -283, h = 2. The engine
     decides.)
  P4 At the winner, the cheapest place's brute ladder prints excess >= 1
     iff the head criterion predicts a head there, and the shop verdict
     line names the first field passing BOTH gates (h > 1, cheapest
     place headed), with any h > 1 field failing the head gate recorded
     and passed over.
  P5 The completeness accounting prints: every box polynomial lands in
     exactly one bucket -- reducible, |d_K| > cap, or assigned to a
     field -- and the bucket counts sum to the box size.

KILL-SHAPES, as observables.
  K1 a degree-2 h disagrees with a filed control: the instrument is
     wrong and no cubic reading below is admissible.
  K2 no h > 1 field within the cap: the cap is raised once (recomputing
     the box) and the run repeated; still none is a finding about the
     range, printed as such.
  K3 an assert fires in the maximal-order path (a non-integral structure
     constant, a place census not summing to the degree): the instrument
     is wrong at that field; the run stops loudly rather than skipping.
  K4 a totally real candidate with SNF order > 1 before the first
     complex winner: printed UNRESOLVED; the first-claim is downgraded
     to conditional in the findings.
  K5 the certificate box FINDS a generator for a place the direct search
     missed: the place was principal after all; the run stops loudly and
     the field is re-read with the generator recorded.

THE SECTIONS.
  S1  positive control: the h-engine at degree 2 against three filed
      class numbers.
  S2  the box: Hunter enumeration, Round-2, field identification, the
      completeness accounting.
  S3  the shop: fields in |d| order, h certified, first h > 1 found.
  S4  the winner: factorization at small primes, cheapest place, brute
      ladders, the head verdict.

FINDINGS (tiers inline; run record at the bottom; every section asserts).

F1 THE RING EXISTS AND IS FIRST: d = -283, K = Q[x]/(x^3 + 4x + 1),
   h = 2 (rule in range; the Hunter box at |d| <= 600, 918 polynomials,
   83 fields, every field of smaller |d| certified h = 1 constructively
   -- 36 of them, both signatures -- before the winner; identity per the
   fingerprint assumption above). The h = 2 sandwich: the relation
   reading gives H = 2 at full rank (h divides H), and the NORM-4 place
   over 2 (the first resister in enumeration order) is certified
   non-principal by an exhausted unit-reduced box (539 elements, box
   [5, 3, 3]), so h > 1; hence h = 2. The norm-2 head place's class
   follows by arithmetic rather than by a second box: 2O is the product
   of the two places over 2 and is principal, so in C2 the two classes
   are mutual inverses -- both non-principal. No totally real
   candidate surfaced (K4 never fired), so the first-claim is
   unconditional in range, and the winner is also the first h > 1 cubic
   field OUTRIGHT -- the head gate never had to pass over anything.

F2 THE CHEAPEST PLACE IS HEADED, AND BY THE UNRAMIFIED SHAPE, NOT THE
   SHAPE THE SHOPPING SPEC GUESSED (observation at this field; the
   criterion clause it instantiates is the rule in range of
   explore_head_width.py F2). 2 factors as a norm-2 place (e = 1,
   f = 1) beside a norm-4 place (f = 2): the completion at the cheapest
   place is Q_2 itself, its ladder the 1,2,2,4,8,... column, excess 1
   in the brute read. That is the head shape of Z[w]'s SPLIT places
   over 2 (e = 1 = 2^0 in the criterion's form), not Z[i]'s wild
   ramified plateau (e = 2) the spec's "cheapest shop" paragraph
   named; the criterion decided, as it was carried in to do. And the
   shape was forced, not lucky: 2 ramifies only where 2 | d (with
   Stickelberger, 4 | d), and d = -283 is odd -- so at this field, and
   at any odd-d field, a head at the cheapest place can only arrive by
   the unramified shape.

F3 THE CONTROL SANDWICH HELD AT DEGREE 2 (rule in range; the three
   filed rings). The same engine -- Round-2, algebra-split places,
   relation Hermite order, unit-reduced certificate -- reproduces
   h = 1, 2, 3 for Z[i], Z[sqrt(-5)], Z[w] with the non-principality
   certificates exhausting 35-element boxes at the resisting norm-2
   places. The instrument shares no code path with the engines that
   filed those values (explore_number_field_lock.py,
   explore_module_law.py).

F4 WHAT THE WALK WILL SEE, propagated but not run (property of the
   ladder columns printed in S4, walk unread): the ring also carries a
   norm-3 place with the standard column 2,6,18,... (door 1 at every
   depth from the void), so the void's cheapest OPENING is 3, not the
   headed place's 4 -- the same configuration as Z[sqrt(-5)], whose
   ideal void locks its norm-3 place at 3/move while the class group
   shows up in the element world and the seeded basins. The walk
   reading therefore needs the seed census and the element world, not
   just the void; this file deliberately stops at the ladders.

RUN RECORD. `python explore_cubic_field_shop.py`. One process, CPython,
no BLAS. 119 checks, 3.0 s wall, peak working set 18.9 MB under
memwatch.py's 512 MB ceiling. S1: three degree-2 controls, H = 1, 2, 3,
two certificates (35 elements each). S2: 918 polynomials -> 142
reducible + 473 over-cap + 303 kept, 83 fields (69 complex, 14 totally
real), least discs -23 and 49. S3: 36 fields certified h = 1 before the
winner; the winner's line: H = 2, place 2.0 (norm 4, the f = 2 place
over 2) certified non-principal (box [5, 3, 3], 539 elements). S4:
ladders at norms 2, 3, 4, 9, 5 --
the norm-2 column 1,2,2,4,8,16,32 (run 2, excess 1), all others excess
0. All five predictions hit; no kill-shape fired.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fractions import Fraction
from math import gcd, sqrt

import explore_cubic_ring as CR

CHECKS = 0

DISC_CAP = 600          # |d_K| ceiling for the shop
FP_PRIME_CAP = 300      # fingerprint primes
GEN_BOXES = (4, 8, 16, 24)   # direct principality search boxes
UNIT_BOXES = (6, 12, 24)     # unit search boxes
REL_BOX = 10            # relation harvest box
REL_PRIME_CAP = 29      # generator set: places over primes <= this ...
REL_NORM_CAP = 30       # ... of norm <= this (reachable by the harvest)
LADDER_DEPTH = 12       # depths a winner ladder is read to
BRUTE_CAP = 15000       # residues allowed in one brute quotient


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def lcm(a, b):
    return a * b // gcd(a, b)


def v_p(n, p):
    v = 0
    n = abs(n)
    while n and n % p == 0:
        n //= p
        v += 1
    return v


SMALL_PRIMES = CR._sieve(FP_PRIME_CAP)


# ----------------------------------------------------- fraction linear algebra
def frac_inv(M):
    n = len(M)
    A = [[Fraction(M[i][j]) for j in range(n)] +
         [Fraction(1 if j == i else 0) for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if A[r][col] != 0)
        A[col], A[piv] = A[piv], A[col]
        inv = 1 / A[col][col]
        A[col] = [x * inv for x in A[col]]
        for r in range(n):
            if r != col and A[r][col]:
                f = A[r][col]
                A[r] = [x - f * y for x, y in zip(A[r], A[col])]
    return [row[n:] for row in A]


def mat_vec(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(len(v)))
                 for i in range(len(M)))


def det3(M):
    n = len(M)
    if n == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


# --------------------------------------------------------------- the order
class Order(object):
    """An order in Q[t]/(f), f monic of degree n, held as a basis of
    theta-coordinate Fractions plus an INTEGER multiplication table
    (structure constants are integers exactly when the lattice is a ring,
    asserted rather than assumed)."""

    def __init__(self, R, trvec, basis):
        self.n = len(R)
        self.R = R                        # t^n = R[0] + R[1] t + ...
        self.trvec = trvec                # Tr of 1, t, t^2, ...
        self.basis = [tuple(Fraction(x) for x in b) for b in basis]
        self.binv = frac_inv([[self.basis[j][i] for j in range(self.n)]
                              for i in range(self.n)])
        self.table = self._make_table()
        self.one = self.coords_of(tuple([1] + [0] * (self.n - 1)))

    def _make_table(self):
        tab = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                prod = CR.omul(self.basis[i], self.basis[j], self.R)
                co = mat_vec(self.binv, prod)
                for x in co:
                    assert x.denominator == 1, \
                        "non-integral structure constant: not an order"
                row.append(tuple(int(x) for x in co))
            tab.append(row)
        return tab

    def coords_of(self, theta_vec):
        co = mat_vec(self.binv, tuple(Fraction(x) for x in theta_vec))
        assert all(x.denominator == 1 for x in co), "element not in order"
        return tuple(int(x) for x in co)

    def mul(self, u, v):
        n = self.n
        out = [0] * n
        for i in range(n):
            if u[i]:
                for j in range(n):
                    if v[j]:
                        c = u[i] * v[j]
                        t = self.table[i][j]
                        for k in range(n):
                            out[k] += c * t[k]
        return tuple(out)

    def power(self, u, k):
        res, b = self.one, u
        while k:
            if k & 1:
                res = self.mul(res, b)
            b = self.mul(b, b)
            k >>= 1
        return res

    def norm(self, u):
        n = self.n
        rows = [self.mul(u, tuple(1 if j == i else 0 for j in range(n)))
                for i in range(n)]
        return det3(rows)

    def trace_form_disc(self):
        n = self.n
        T = []
        for i in range(n):
            row = []
            for j in range(n):
                prod = CR.omul(self.basis[i], self.basis[j], self.R)
                tr = sum(Fraction(self.trvec[k]) * prod[k]
                         for k in range(len(prod)))
                row.append(tr)
            T.append(row)
        d = det3(T)
        assert d.denominator == 1, "non-integral discriminant"
        return int(d)


# ------------------------------------------------------- F_p linear algebra
def kernel_mod_p(rows, p):
    """Kernel of the map e_i -> rows[i] over F_p, as coefficient vectors."""
    n = len(rows)
    if n == 0:
        return []
    m = len(rows[0])
    A = [[rows[i][j] % p for j in range(m)] +
         [1 if k == i else 0 for k in range(n)] for i in range(n)]
    rank_rows = []
    for col in range(m):
        piv = None
        for r in range(n):
            if r not in rank_rows and A[r][col] % p:
                piv = r
                break
        if piv is None:
            continue
        rank_rows.append(piv)
        inv = pow(A[piv][col], p - 2, p)
        A[piv] = [(x * inv) % p for x in A[piv]]
        for r in range(n):
            if r != piv and A[r][col] % p:
                f = A[r][col]
                A[r] = [(x - f * y) % p for x, y in zip(A[r], A[piv])]
    ker = []
    for r in range(n):
        if r not in rank_rows and all(A[r][j] % p == 0 for j in range(m)):
            ker.append([A[r][m + k] % p for k in range(n)])
    return ker


def echelon_rows(rows, p):
    """Row-reduced echelon basis of the span, over F_p."""
    work = [list(r) for r in rows]
    m = len(work[0]) if work else 0
    out = []
    for col in range(m):
        piv = next((r for r in work if r[col] % p), None)
        if piv is None:
            continue
        work.remove(piv)
        inv = pow(piv[col], p - 2, p)
        piv = [(x * inv) % p for x in piv]
        for r in work:
            if r[col] % p:
                f = r[col]
                for i in range(m):
                    r[i] = (r[i] - f * piv[i]) % p
        for r in out:
            if r[col] % p:
                f = r[col]
                for i in range(m):
                    r[i] = (r[i] - f * piv[i]) % p
        out.append(piv)
    return out


def reduce_by_echelon(v, ech, p):
    v = [x % p for x in v]
    for r in ech:
        lead = next(i for i in range(len(r)) if r[i] % p)
        if v[lead]:
            f = v[lead]
            v = [(a - f * b) % p for a, b in zip(v, r)]
    return v


def rank_mod_p(rows, p):
    return len(echelon_rows(rows, p))


# ------------------------------------------------------------ round 2 at p
def radical_mod_p(O, p):
    """F_p basis of the nilradical of O/pO: kernel of x -> x^q, q the
    least power of p at or above n (Frobenius iterate, F_p-linear)."""
    n = O.n
    q = p
    while q < n:
        q *= p
    rows = []
    for i in range(n):
        e = tuple(1 if j == i else 0 for j in range(n))
        rows.append([x % p for x in O.power(e, q)])
    return kernel_mod_p(rows, p)


def tri_solve(H, w, n):
    """Integer coordinates of w in the upper-triangular HNF basis H
    (row i leads at column i). Asserts exact membership."""
    w = list(w)
    co = [0] * n
    for i in range(n):
        assert w[i] % H[i][i] == 0, "tri_solve: not in the lattice"
        c = w[i] // H[i][i]
        co[i] = c
        if c:
            for k in range(i, n):
                w[k] -= c * H[i][k]
    assert all(x == 0 for x in w), "tri_solve residue"
    return co


def p_maximalize(O, p):
    """Round-2 at p: enlarge O by (1/p){y : y J' <= p J'} until stable,
    J' the full preimage of the nilradical."""
    while True:
        n = O.n
        J = radical_mod_p(O, p)
        if not J:
            return O
        Jl = [tuple(int(x) for x in j) for j in J]
        gens = [tuple(p if j == i else 0 for j in range(n))
                for i in range(n)] + list(Jl)
        Jp = hnf_red(gens, n)                       # J' lattice
        # y = sum a_l Jl[l]; condition: y * Jl[m] in p*J' for every m.
        maps = []
        for l in range(len(Jl)):
            row = []
            for m in range(len(Jl)):
                w = O.mul(Jl[l], Jl[m])            # lies in J'*J' <= J'
                co = tri_solve(Jp, w, n)
                row.extend([x % p for x in co])
            maps.append(row)
        ann = kernel_mod_p(maps, p)
        if not ann:
            return O
        newgens = [tuple(p if j == i else 0 for j in range(n))
                   for i in range(n)]
        for a in ann:
            y = [0] * n
            for l in range(len(Jl)):
                if a[l]:
                    for k in range(n):
                        y[k] += a[l] * Jl[l][k]
            newgens.append(tuple(y))
        H = hnf_red(newgens, n)
        detH = 1
        for i in range(n):
            detH *= H[i][i]
        if detH == p ** n:
            return O
        newb = []
        for i in range(n):
            tv = [Fraction(0)] * n
            for j in range(n):
                if H[i][j]:
                    for k in range(n):
                        tv[k] += Fraction(H[i][j], p) * O.basis[j][k]
            newb.append(tuple(tv))
        O = Order(O.R, O.trvec, newb)


def maximal_order(a, b, c):
    """The maximal order of Q[t]/(t^3 + a t^2 + b t + c), and d_K."""
    R = (-c, -b, -a)
    trvec = (3, -a, a * a - 2 * b)
    O = Order(R, trvec, [(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    d0 = O.trace_form_disc()
    assert abs(d0) < 90000, "polynomial discriminant out of sieve range"
    for p in SMALL_PRIMES:
        if p * p > abs(d0):
            break
        if d0 % (p * p) == 0:
            O = p_maximalize(O, p)
    return O, O.trace_form_disc()


# ------------------------------------------------- places of a maximal order
def poly_eval_alg(coeffs, x, mul, one):
    """coeffs low-first over F_p context handled by caller; Horner."""
    res = None
    for c in reversed(coeffs):
        if res is None:
            res = tuple(c * v for v in one)
        else:
            res = mul(res, x)
            res = tuple(r + c * v for r, v in zip(res, one))
    return res


def pxgcd(a, b, p):
    """(g, u, v) with u a + v b = g, monic g, over F_p."""
    r0, r1 = CR.pnorm(a, p), CR.pnorm(b, p)
    u0, u1 = (1,), ()
    v0, v1 = (), (1,)
    while r1:
        # divide r0 by r1
        q = poly_divmod_q(r0, r1, p)
        r0, r1 = r1, CR.pnorm(tuple_sub(r0, CR.pmul(q, r1, p), p), p)
        u0, u1 = u1, CR.pnorm(tuple_sub(u0, CR.pmul(q, u1, p), p), p)
        v0, v1 = v1, CR.pnorm(tuple_sub(v0, CR.pmul(q, v1, p), p), p)
    if r0:
        inv = pow(r0[-1], p - 2, p)
        r0 = CR.pnorm(tuple(x * inv for x in r0), p)
        u0 = CR.pnorm(tuple(x * inv for x in u0), p)
        v0 = CR.pnorm(tuple(x * inv for x in v0), p)
    return r0, u0, v0


def poly_divmod_q(a, b, p):
    """Quotient of a by b over F_p (b nonzero)."""
    a = list(CR.pnorm(a, p))
    b = CR.pnorm(b, p)
    inv = pow(b[-1], p - 2, p)
    q = [0] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and a:
        c = (a[-1] * inv) % p
        off = len(a) - len(b)
        q[off] = c
        if c:
            for i, y in enumerate(b):
                a[off + i] = (a[off + i] - c * y) % p
        a.pop()
        while a and a[-1] % p == 0:
            a.pop()
    return CR.pnorm(tuple(q), p)


def tuple_sub(a, b, p):
    n = max(len(a), len(b))
    a = tuple(a) + (0,) * (n - len(a))
    b = tuple(b) + (0,) * (n - len(b))
    return tuple((x - y) % p for x, y in zip(a, b))


def factor_squarefree_le3(m, p):
    """Monic squarefree poly of degree <= 3 over F_p -> list of monic
    irreducible factors (each once). Squarefreeness is guaranteed by the
    caller's semisimplicity (a min poly over a product of fields), and
    asserted rather than trusted."""
    m = CR.pnorm(m, p)
    deg = len(m) - 1
    assert 1 <= deg <= 3
    assert len(CR.pgcd(m, CR.pderiv(m, p), p)) == 1, \
        "min poly not squarefree: the algebra was not semisimple"
    roots = [r for r in range(p)
             if sum(c * pow(r, i, p) for i, c in enumerate(m)) % p == 0]
    fac = [( -r % p, 1) for r in roots]
    rem = m
    for r in roots:
        rem = poly_divmod_q(rem, (-r % p, 1), p)
    if len(rem) - 1 >= 1:
        fac.append(tuple(rem))
    return [CR.pnorm(f, p) for f in fac]


def maximal_places(O, p):
    """[(P_hnf, e, f)] for every place over p, via the algebra O/pO."""
    n = O.n
    tab = [[tuple(x % p for x in O.table[i][j]) for j in range(n)]
           for i in range(n)]

    def amul(u, v):
        out = [0] * n
        for i in range(n):
            if u[i] % p:
                for j in range(n):
                    if v[j] % p:
                        c = (u[i] * v[j]) % p
                        t = tab[i][j]
                        for k in range(n):
                            out[k] = (out[k] + c * t[k]) % p
        return tuple(out)

    aone = tuple(x % p for x in O.one)
    J = radical_mod_p(O, p)
    Jech = echelon_rows(J, p) if J else []

    def proj(v):
        return tuple(reduce_by_echelon(v, Jech, p))

    # decompose the semisimple quotient by idempotents held as elements
    # of O/pO (projected representatives); identity of a component = e.
    def comp_dim(e):
        rows = []
        for i in range(n):
            b = tuple(1 if j == i else 0 for j in range(n))
            rows.append(list(proj(amul(e, b))))
        return rank_mod_p(rows, p)

    def min_poly(x, e, dim):
        """Monic min poly of x in the unital algebra eA (identity e)."""
        pows = [e]
        cur = e
        rows = []
        for k in range(dim + 1):
            rows.append(list(pows[-1]))
            dep = kernel_mod_p([list(r) for r in rows], p)
            if dep:
                co = dep[0]
                lead = max(i for i in range(len(co)) if co[i] % p)
                inv = pow(co[lead], p - 2, p)
                return CR.pnorm(tuple((c * inv) % p for c in co), p)
            cur = amul(cur, x)
            pows.append(proj(cur))
        assert False, "min poly not found"

    def candidates(e):
        for i in range(n):
            yield proj(amul(e, tuple(1 if j == i else 0 for j in range(n))))
        for i in range(n):
            for j in range(i + 1, n):
                v = tuple((1 if k == i else 0) + (1 if k == j else 0)
                          for k in range(n))
                yield proj(amul(e, v))
        for v in all_vectors(n, p):
            yield proj(amul(e, v))

    def decompose(e):
        dim = comp_dim(e)
        if dim == 1:
            return [(e, 1)]
        for x in candidates(e):
            m = min_poly(x, e, dim)
            degm = len(m) - 1
            if degm < 2:
                continue
            fac = factor_squarefree_le3(m, p)
            if len(fac) == 1:
                if degm == dim:
                    return [(e, dim)]           # a field component
                continue
            g = fac[0]
            h = m
            for _ in range(1):
                h = poly_divmod_q(m, g, p)
            gpoly, u, v = pxgcd(g, h, p)
            assert len(gpoly) - 1 == 0, "factors not coprime"
            ug = CR.pmul(u, g, p)
            e1 = poly_eval_alg(ug, x, amul, e)
            e1 = proj(tuple(x1 % p for x1 in e1))
            assert e1 == proj(amul(e1, e1)), "not an idempotent"
            e2 = tuple((a1 - b1) % p for a1, b1 in zip(e, e1))
            out = []
            for esub in (e1, e2):
                out.extend(decompose(esub))
            return out
        assert False, "no separating element found"

    comps = decompose(proj(aone))
    found = []
    for (e, f) in comps:
        rows = []
        for i in range(n):
            b = tuple(1 if j == i else 0 for j in range(n))
            rows.append(list(proj(amul(e, b))))
        # kernel of v -> e * v-bar: maximal ideal, dim n - f
        ker = kernel_mod_p(rows, p)
        assert len(ker) == n - f, "maximal ideal dimension off"
        gens = [tuple(p if j == i else 0 for j in range(n))
                for i in range(n)]
        gens += [tuple(int(x) for x in k) for k in ker]
        P = hnf_red(gens, n)
        found.append([P, 0, f])
    pO = hnf_red([tuple(p if j == i else 0 for j in range(n))
                 for i in range(n)], n)
    for rec in found:
        P = rec[0]
        k = 1
        while True:
            Pk = ideal_pow_hnf(O, P, k + 1)
            if lattice_contains(Pk, pO, n):
                k += 1
                assert k <= n, "ramification above the degree"
            else:
                break
        rec[1] = k
    ok(sum(r[1] * r[2] for r in found) == n,
       "place census at p = %d does not sum to the degree: %s"
       % (p, [(r[1], r[2]) for r in found]))
    return [(r[0], r[1], r[2]) for r in found]


def all_vectors(n, p):
    if n == 1:
        return [(x,) for x in range(p)]
    sub = all_vectors(n - 1, p)
    return [(x,) + s for x in range(p) for s in sub]


# ----------------------------------------------------- ideal lattice tools
def hnf_red(gens, n):
    """CR.hnf plus off-diagonal reduction, without which iterated ideal
    products swell into hundred-digit entries."""
    H = CR.hnf(gens, n)
    for i in range(n - 1, -1, -1):
        for j in range(i):
            q = H[j][i] // H[i][i]
            if q:
                H[j] = [a - q * b for a, b in zip(H[j], H[i])]
    return H


def ideal_mul_hnf(O, A, B):
    n = O.n
    gens = []
    for i in range(n):
        for j in range(n):
            gens.append(O.mul(tuple(A[i]), tuple(B[j])))
    return hnf_red(gens, n)


def ideal_pow_hnf(O, P, k):
    cur = hnf_red([tuple(1 if j == i else 0 for j in range(O.n))
                  for i in range(O.n)], O.n)
    b = P
    while k:
        if k & 1:
            cur = ideal_mul_hnf(O, cur, b)
        k >>= 1
        if k:
            b = ideal_mul_hnf(O, b, b)
    return cur


def lattice_contains(A, B, n):
    for row in B:
        if any(x != 0 for x in CR.reduce_mod(tuple(row), A, n)):
            return False
    return True


def in_lattice(v, A, n):
    return all(x == 0 for x in CR.reduce_mod(tuple(v), A, n))


# ------------------------------------------------------------- principality
def element_boxes(n, B):
    if n == 2:
        return ((x, y) for x in range(-B, B + 1) for y in range(-B, B + 1))
    return ((x, y, z) for x in range(-B, B + 1)
            for y in range(-B, B + 1) for z in range(-B, B + 1))


def find_generator(O, A, target, boxes=GEN_BOXES):
    n = O.n
    for B in boxes:
        for v in element_boxes(n, B):
            if all(x == 0 for x in v):
                continue
            if abs(O.norm(v)) != target:
                continue
            if in_lattice(v, A, n):
                return v
    return None


def find_unit(O):
    n = O.n
    one = O.one
    for B in UNIT_BOXES:
        for v in element_boxes(n, B):
            if all(x == 0 for x in v):
                continue
            if abs(O.norm(v)) != 1:
                continue
            if v == one or v == tuple(-x for x in one):
                continue
            return v
    return None


# -------------------------------------------- embeddings and the certificate
def real_root_cubic(a, b, c):
    def f(x):
        return ((x + a) * x + b) * x + c
    M = 1.0 + max(abs(a), abs(b), abs(c))
    lo, hi = -M - 1, M + 1
    assert f(lo) < 0 < f(hi)
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    r = (lo + hi) / 2
    for _ in range(8):
        d = (3 * r + 2 * a) * r + b
        if d:
            r -= f(r) / d
    return r


def mat_inv_float(M):
    n = len(M)
    A = [[float(M[i][j]) for j in range(n)] +
         [1.0 if k == i else 0.0 for k in range(n)] for i in range(n)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(A[r][col]))
        A[col], A[piv] = A[piv], A[col]
        d = A[col][col]
        A[col] = [x / d for x in A[col]]
        for r in range(n):
            if r != col:
                f = A[r][col]
                A[r] = [x - f * y for x, y in zip(A[r], A[col])]
    return [row[n:] for row in A]


def cert_box_search(O, A, target, emb_rows, bounds):
    """Exhaust the coefficient box implied by per-embedding bounds."""
    n = O.n
    inv = mat_inv_float(emb_rows)
    lim = []
    for i in range(n):
        s = sum(abs(inv[i][j]) * bounds[j] for j in range(n))
        lim.append(int(s * (1 + 1e-9)) + 2)
    if n == 2:
        it = ((x, y) for x in range(-lim[0], lim[0] + 1)
              for y in range(-lim[1], lim[1] + 1))
    else:
        it = ((x, y, z) for x in range(-lim[0], lim[0] + 1)
              for y in range(-lim[1], lim[1] + 1)
              for z in range(-lim[2], lim[2] + 1))
    count = 0
    for v in it:
        count += 1
        if all(x == 0 for x in v):
            continue
        if abs(O.norm(v)) != target:
            continue
        if in_lattice(v, A, n):
            return v, count, lim
    return None, count, lim


def non_principality_certificate(O, A, target, poly):
    """PROVE no element of A has |norm| = target -- complex cubic (unit
    rank 1) or imaginary quadratic (rank 0). Returns (certified, detail);
    certified False means a generator was FOUND."""
    n = O.n
    if n == 2:
        a1, a0 = poly
        disc = a1 * a1 - 4 * a0
        assert disc < -4, "imaginary quadratic with extra torsion"
        re = -a1 / 2.0
        im = sqrt(-disc) / 2.0
        rows = [[float(b[0]) + float(b[1]) * re for b in O.basis],
                [float(b[1]) * im for b in O.basis]]
        Bc = sqrt(target) * (1 + 1e-9)
        got, cnt, lim = cert_box_search(O, A, target, rows, (Bc, Bc))
        return (got is None), (got, cnt, lim, 1.0)
    a, b, c = poly
    eta = find_unit(O)
    assert eta is not None, "no unit found for the certificate box"
    r = real_root_cubic(a, b, c)
    q1 = a + r
    q0 = b + r * q1
    zr = -q1 / 2
    im2 = q0 - q1 * q1 / 4
    assert im2 > 0, "complex pair expected (disc < 0)"
    zi = sqrt(im2)
    emb = []
    for bvec in O.basis:
        t = [float(bvec[k]) for k in range(3)]
        sR = t[0] + t[1] * r + t[2] * r * r
        zRe = t[0] + t[1] * zr + t[2] * (zr * zr - zi * zi)
        zIm = t[1] * zi + t[2] * (2 * zr * zi)
        emb.append((sR, zRe, zIm))
    rows = [[e[0] for e in emb], [e[1] for e in emb], [e[2] for e in emb]]
    sR_eta = sum(float(eta[j]) * emb[j][0] for j in range(3))
    u = abs(sR_eta)
    if u < 1:
        u = 1 / u
    assert u > 1 + 1e-9, "unit with unit-modulus real embedding"
    BR = target ** (1 / 3) * sqrt(u) * (1 + 1e-9)
    BC = (target ** (1 / 3)) * (u ** 0.25) * (1 + 1e-9)
    got, cnt, lim = cert_box_search(O, A, target, rows, (BR, BC, BC))
    return (got is None), (got, cnt, lim, u)


# ------------------------------------------------------ relations and SNF
def hermite_order(rows, k):
    """Order of Z^k / <rows>, or None if infinite. Row ops only; at the
    end the pivot rows are upper triangular and the order is the product
    of the pivots' absolute values."""
    M = [list(r) for r in rows]
    if not M:
        return None if k else 1
    r0 = 0
    for c in range(k):
        piv = None
        for r in range(r0, len(M)):
            if M[r][c]:
                if piv is None or abs(M[r][c]) < abs(M[piv][c]):
                    piv = r
        if piv is None:
            return None
        M[r0], M[piv] = M[piv], M[r0]
        again = True
        while again:
            again = False
            for r in range(r0 + 1, len(M)):
                if M[r][c]:
                    q = M[r][c] // M[r0][c]
                    M[r] = [x - q * y for x, y in zip(M[r], M[r0])]
                    if M[r][c]:
                        M[r0], M[r] = M[r], M[r0]
                        again = True
        r0 += 1
    order = 1
    for c in range(k):
        order *= abs(M[c][c])
    return order


def place_valuation(O, v, P, cap):
    n = O.n
    k = 0
    Pk = P
    while k < cap:
        if in_lattice(v, Pk, n):
            k += 1
            Pk = ideal_mul_hnf(O, Pk, P)
        else:
            break
    return k


def all_places_upto_prime(O, pcap):
    """Every place over every prime p <= pcap: (p, e, f, name, P)."""
    out = []
    for p in SMALL_PRIMES:
        if p > pcap:
            break
        for i, (P, e, f) in enumerate(maximal_places(O, p)):
            out.append((p, e, f, "%d.%d" % (p, i), P))
    return out


def harvest_relations(O, gen_places, box=REL_BOX, cap=400):
    n = O.n
    prime_set = sorted(set(p for (p, _, _, _, _) in gen_places))
    rows = []
    for v in element_boxes(n, box):
        if all(x == 0 for x in v):
            continue
        N = abs(O.norm(v))
        if N == 0:
            continue
        m = N
        for p in prime_set:
            while m % p == 0:
                m //= p
        if m != 1:
            continue
        row = [0] * len(gen_places)
        checksum = {}
        for i, (p, e, f, name, P) in enumerate(gen_places):
            val = place_valuation(O, v, P, v_p(N, p) + 1)
            row[i] = val
            checksum[p] = checksum.get(p, 0) + val * f
        if any(checksum.get(p, 0) != v_p(N, p) for p in prime_set):
            continue
        rows.append(row)
        if len(rows) >= cap:
            break
    return rows


# ---------------------------------------------------- per-field processing
def minkowski_bound(d, n, s_complex):
    fac = {2: 0.5, 3: 2.0 / 9.0}[n]
    mb = fac * sqrt(abs(d))
    if s_complex:
        mb *= 4 / 3.141592653589793
    return int(mb * (1 + 1e-9))


def relation_generators(O):
    """The generator set for the relation reading: every place over a
    prime to REL_PRIME_CAP whose NORM the harvest box can actually reach.
    It contains all places under any Minkowski bound in range, so it
    still generates the class group."""
    return [t for t in all_places_upto_prime(O, REL_PRIME_CAP)
            if t[0] ** t[2] <= REL_NORM_CAP]


def relation_H(O):
    gen_places = relation_generators(O)
    rows = harvest_relations(O, gen_places)
    H = hermite_order(rows, len(gen_places))
    if H is None:
        rows = harvest_relations(O, gen_places, box=REL_BOX + 6, cap=1500)
        H = hermite_order(rows, len(gen_places))
    return H


def certify_h(O, d, cx, poly):
    """('h=1' | 'h>1' | 'unresolved', h_or_None, detail)."""
    n = O.n
    mb = minkowski_bound(d, n, cx)
    small = [t for t in all_places_upto_prime(O, mb)
             if t[0] ** t[2] <= mb]
    if not small:
        return 'h=1', 1, "Minkowski %d: vacuous" % mb
    resisting = []
    for (p, e, f, name, P) in small:
        if find_generator(O, P, p ** f) is None:
            resisting.append((p, e, f, name, P))
    if not resisting:
        return 'h=1', 1, ("Minkowski %d: %d places all principal"
                          % (mb, len(small)))
    H = relation_H(O)
    if H is None:
        return 'unresolved', None, "relation rank deficient"
    if H == 1:
        return 'h=1', 1, "H = 1 (direct box too small for a generator)"
    if not cx:
        return 'unresolved', None, ("totally real, H = %d: rank-2 "
                                    "certificate not implemented" % H)
    p, e, f, name, P = resisting[0]
    cert, detail = non_principality_certificate(O, P, p ** f, poly)
    assert cert, ("certificate box found a generator at the resisting "
                  "place %s: %s" % (name, detail[0]))
    if H in (2, 3):
        return 'h>1', H, ("H = %d, place %s (norm %d) certified "
                          "non-principal (box %s, %d elements)"
                          % (H, name, p ** f, detail[2], detail[1]))
    return 'h>1', None, ("H = %d, non-principality certified; exact h "
                         "needs more certificates" % H)


# ------------------------------------------------------------ S1 controls
QUAD_CONTROLS = [
    ("Z[i]", 0, 1, 1),          # t^2 + 1, disc -4
    ("Z[sqrt-5]", 0, 5, 2),     # t^2 + 5, disc -20
    ("Z[w] (-23)", -1, 6, 3),   # t^2 - t + 6, disc -23
]


def s1_controls():
    section("S1  POSITIVE CONTROL -- the h-engine at degree 2, against "
            "three filed class numbers")
    print("  Filed: h = 1 (Z[i]), h = 2 = C2 (Z[sqrt-5],")
    print("  explore_number_field_lock.py), h = 3 = C3 (Z[w],")
    print("  explore_module_law.py). No code path is shared with the")
    print("  engines that filed them.")
    print()
    for (label, a1, a0, filed) in QUAD_CONTROLS:
        R = (-a0, -a1)
        trvec = (2, -a1)
        O = Order(R, trvec, [(1, 0), (0, 1)])
        d = O.trace_form_disc()
        for p in SMALL_PRIMES:
            if p * p > abs(d):
                break
            if d % (p * p) == 0:
                O2 = p_maximalize(O, p)
                ok(O2 is O, "%s: control order not maximal at %d"
                   % (label, p))
        mb = minkowski_bound(d, 2, True)
        small = [t for t in all_places_upto_prime(O, mb)
                 if t[0] ** t[2] <= mb]
        resisting = []
        for (p, e, f, name, P) in small:
            if find_generator(O, P, p ** f) is None:
                resisting.append((p, e, f, name, P))
        H = relation_H(O)
        print("  %-12s d = %-4d Minkowski %d: %d small places, "
              "%d resisting; H = %s"
              % (label, d, mb, len(small), len(resisting), H))
        ok(H == filed, "%s: H = %s against the filed h = %d"
           % (label, H, filed))
        if filed == 1:
            ok(not resisting, "%s: h = 1 but a place resisted" % label)
        else:
            ok(bool(resisting), "%s: h > 1 but no place resisted" % label)
            p, e, f, name, P = resisting[0]
            cert, (got, cnt, lim, u) = non_principality_certificate(
                O, P, p ** f, (a1, a0))
            ok(cert, "%s: certificate found a generator %s"
               % (label, got))
            print("     norm-%d place %s certified non-principal: "
                  "box %s, %d elements exhausted" % (p ** f, name, lim, cnt))
    print("\n  All three filed class numbers reproduced; the instrument"
          " stands.")


# ------------------------------------------------------- S2 the enumeration
def hunter_box(cap):
    t2max = 1.0 / 3.0 + (2.0 / sqrt(3.0)) * sqrt(cap / 3.0)
    s2max = int((1.0 + t2max) / 2.0)
    s3max = int((t2max / 3.0) ** 1.5)
    return t2max, s2max, s3max


def is_irreducible_cubic(a, b, c):
    if c == 0:
        return False
    for r in range(1, abs(c) + 1):
        if abs(c) % r == 0:
            for s in (r, -r):
                if ((s + a) * s + b) * s + c == 0:
                    return False
    return True


def poly_disc3(a, b, c):
    return (18 * a * b * c - 4 * a ** 3 * c + a * a * b * b
            - 4 * b ** 3 - 27 * c * c)


def shape_at(a, b, c, p):
    """Field splitting shape at p (only called at p not dividing the
    polynomial discriminant, where Z[theta] is p-maximal)."""
    rts = [r for r in range(p) if (((r + a) * r + b) * r + c) % p == 0]
    if not rts:
        return ((1, 3),)
    if len(rts) == 3:
        return ((1, 1), (1, 1), (1, 1))
    assert len(rts) == 1, \
        "cubic with %d roots mod %d off its discriminant" % (len(rts), p)
    return ((1, 1), (1, 2))


def enumerate_fields(cap):
    t2max, s2max, s3max = hunter_box(cap)
    n_poly = n_red = n_over = n_kept = 0
    records = []          # (d, fp_dict, [(a,b,c,O), ...])
    for s1 in (0, 1):
        for s2 in range(-s2max, s2max + 1):
            for s3 in range(-s3max, s3max + 1):
                n_poly += 1
                a, b, c = -s1, s2, -s3
                if not is_irreducible_cubic(a, b, c):
                    n_red += 1
                    continue
                O, d = maximal_order(a, b, c)
                if abs(d) > cap:
                    n_over += 1
                    continue
                n_kept += 1
                pd = poly_disc3(a, b, c)
                fp = {}
                for p in SMALL_PRIMES:
                    if pd % p:
                        fp[p] = shape_at(a, b, c, p)
                home = None
                for rec in records:
                    if rec[0] != d:
                        continue
                    common = [p for p in fp if p in rec[1]]
                    if all(fp[p] == rec[1][p] for p in common):
                        home = rec
                        break
                if home is None:
                    records.append((d, fp, [(a, b, c, O)]))
                else:
                    home[1].update(fp)
                    home[2].append((a, b, c, O))
    out = [(abs(d), d, d < 0, polys) for (d, fp, polys) in records]
    out.sort(key=lambda t: (t[0], t[1]))
    return out, (n_poly, n_red, n_over, n_kept)


def s2_enumeration():
    section("S2  THE BOX -- Hunter enumeration to |d| <= %d" % DISC_CAP)
    t2max, s2max, s3max = hunter_box(DISC_CAP)
    print("  T2 <= %.2f, so s1 in {0,1}, |s2| <= %d, |s3| <= %d"
          % (t2max, s2max, s3max))
    fields, (n_poly, n_red, n_over, n_kept) = enumerate_fields(DISC_CAP)
    print("  %d polynomials: %d reducible, %d with |d_K| > cap, %d kept"
          % (n_poly, n_red, n_over, n_kept))
    ok(n_red + n_over + n_kept == n_poly, "bucket counts do not sum")
    n_complex = sum(1 for f in fields if f[2])
    print("  %d fields: %d complex, %d totally real"
          % (len(fields), n_complex, len(fields) - n_complex))
    first_c = next(f for f in fields if f[2])
    first_r = next(f for f in fields if not f[2])
    print("  least |d| complex: %d   least totally real: %d"
          % (first_c[1], first_r[1]))
    ok(first_c[1] == -23, "least complex cubic disc is %d, not -23"
       % first_c[1])
    ok(first_r[1] == 49, "least totally real cubic disc is %d, not 49"
       % first_r[1])
    return fields


# ------------------------------------------------------------- S3 the shop
def cheapest_place_headed(O):
    best = None
    for p in (2, 3, 5, 7):
        for (P, e, f) in maximal_places(O, p):
            nrm = p ** f
            if best is None or nrm < best[0]:
                best = (nrm, p, e, f, P)
        if best is not None and best[0] <= p:
            break
    nrm, p, e, f, P = best
    desc = "norm %d (p=%d, e=%d, f=%d)" % (nrm, p, e, f)
    if f != 1:
        return False, desc
    if p == 2:
        return e in (1, 2), desc
    good_form = False
    t = p - 1
    while t <= e:
        if t == e:
            good_form = True
        t *= p
    if good_form:
        desc += " [mu_%d membership read off the ladder in S4]" % p
    return good_form, desc


def s3_shop(fields):
    section("S3  THE SHOP -- fields in |d| order, h certified, first "
            "h > 1 with a headed cheapest place")
    winner = None
    h_over_1 = []
    n_h1 = 0
    for (ad, d, cx, polys) in fields:
        a, b, c, O = polys[0]
        status, h, detail = certify_h(O, d, cx, (a, b, c))
        if status == 'h=1':
            n_h1 += 1
            continue
        print("  d = %-6d %-24s %s" % (d, str((a, b, c)), detail))
        if status == 'unresolved':
            print("    ^ UNRESOLVED (kill-shape K4)")
            continue
        h_over_1.append((d, h))
        headed, cheap_desc = cheapest_place_headed(O)
        print("    h = %s; cheapest place %s -> %s"
              % (h, cheap_desc, "HEADED" if headed else "headless"))
        if headed and winner is None:
            winner = (d, cx, polys, h)
            break
    print("  (%d fields before this point certified h = 1)" % n_h1)
    ok(winner is not None,
       "no h > 1 field with a headed cheapest place within |d| <= %d"
       % DISC_CAP)
    return winner, h_over_1


# ------------------------------------------------------------ S4 the winner
def unit_exponent_order(O, P, a, q):
    """Exponent of (O/P^a)^* over the maximal order's own residue ring --
    CR.unit_exponent's method with table multiplication."""
    n = O.n
    Pa = ideal_pow_hnf(O, P, a)
    dims = [Pa[i][i] for i in range(n)]
    total = 1
    for x in dims:
        total *= x
    assert total == q ** a, "residue count %d is not the norm %d" \
        % (total, q ** a)
    one = CR.reduce_mod(O.one, Pa, n)
    order = q ** (a - 1) * (q - 1)
    fac, m, dd = [], order, 2
    while dd * dd <= m:
        while m % dd == 0:
            fac.append(dd)
            m //= dd
        dd += 1
    if m > 1:
        fac.append(m)
    fac = sorted(set(fac))

    def powmod(u, k):
        res, bb = one, u
        while k:
            if k & 1:
                res = CR.reduce_mod(O.mul(res, bb), Pa, n)
            bb = CR.reduce_mod(O.mul(bb, bb), Pa, n)
            k >>= 1
        return res

    exp = 1

    def walk(idx, acc):
        nonlocal exp
        if idx == n:
            u = tuple(acc)
            if in_lattice(u, P, n):
                return
            if powmod(u, exp) == one:
                return
            o = order
            for r in fac:
                while o % r == 0 and powmod(u, o // r) == one:
                    o //= r
            exp = lcm(exp, o)
            return
        for x in range(dims[idx]):
            acc.append(x)
            walk(idx + 1, acc)
            acc.pop()

    walk(0, [])
    return exp


def s4_winner(winner):
    d, cx, polys, h = winner
    a, b, c, O = polys[0]
    section("S4  THE WINNER -- d = %d, h = %s: places, ladders, the head "
            "verdict" % (d, h))
    print("  field: x^3 %+d x^2 %+d x %+d, %s cubic, h = %s, "
          "%d generators in the box"
          % (a, b, c, "complex" if cx else "totally real", h, len(polys)))
    print()
    print("  places over the small primes, with brute lambda ladders:")
    print("  %-8s %-4s %-4s %-26s %-5s %s"
          % ("place", "e", "f", "lambda by depth", "run", "excess"))
    ladders = []
    for p in (2, 3, 5, 7):
        for i, (P, e, f) in enumerate(maximal_places(O, p)):
            q = p ** f
            lams = []
            aa = 1
            while q ** aa <= BRUTE_CAP and aa <= LADDER_DEPTH:
                lams.append(unit_exponent_order(O, P, aa, q))
                aa += 1
            if len(lams) < 3:
                continue
            if any(x > 1 for x in lams):
                run = max(sum(1 for x in lams if x == v)
                          for v in set(lams) if v > 1)
            else:
                run = 0
            excess = run - e
            ladders.append((q, p, i, e, f, lams, excess))
            print("  %-8s %-4d %-4d %-26s %-5d %d"
                  % ("%d.%d" % (p, i), e, f,
                     ",".join(str(x) for x in lams[:7])[:26], run, excess))
    cheapest_norm = min(t[0] for t in ladders)
    cheap_excesses = [t[6] for t in ladders if t[0] == cheapest_norm]
    ok(any(x >= 1 for x in cheap_excesses),
       "the winner's cheapest place shows no head in the brute ladder")
    print("\n  cheapest norm %d: excesses %s -- the head is REAL in the"
          " brute ladder." % (cheapest_norm, cheap_excesses))
    return ladders


def main():
    s1_controls()
    fields = s2_enumeration()
    winner, h_over_1 = s3_shop(fields)
    s4_winner(winner)

    section("VERDICT -- the predictions read against what printed")
    print("  P1 three filed degree-2 class numbers: see S1")
    print("  P2 least discs: see S2")
    print("  P3 first h > 1 with headed cheapest place: d = %d, h = %s"
          % (winner[0], winner[3]))
    print("  P4 the head verdict: see S4")
    print("  P5 the bucket accounting: see S2")
    print("  h > 1 fields seen on the way: %s" % h_over_1)
    print("\n  %d checks passed." % CHECKS)


if __name__ == "__main__":
    main()
