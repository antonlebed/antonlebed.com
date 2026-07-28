"""
Operation discovery, hunt (b): the DIVISION-ALGEBRA LADDER.

An earlier arc (explore_index_transform.py, explore_super_log.py)
charted Napier's ladder over the tower (two coordinate moves,
no third) and its char-2 mirrors. This hunt climbs a different ladder:
Cayley-Dickson doubling OVER the tower's finite fields. Over R the
ladder has three division floors (Frobenius: R, C, H) plus one
alternative floor (O); over a finite field the classical walls are
total -- Wedderburn (every finite division ring is a field) and
Artin-Zorn (the alternative case) -- so every floor above the first
SPLITS. The chart is what the split algebras KEEP on the tower: the
composition norm (a size-like quantity that, unlike size, IS
channel-computable), the zero-divisor cone (what plays non-unit; what
survives of the meadow), what remains of the index transform, and the
locality criterion's noncommutative reading.

Survey anchors (standard material, named so nothing here poses as new):
Frobenius 1878 (R, C, H are the only associative division algebras
over R), Wedderburn 1905 (finite division rings are fields), Artin-Zorn
(finite alternative division rings are fields), Chevalley-Warning
(forms of degree < #vars have nontrivial zeros over F_p -- every
quaternion/octonion norm form over F_p is isotropic, hence every
quaternion algebra over F_p is split M_2(F_p) and every octonion
algebra is Zorn's split vector matrices), Hurwitz 1898 + the
composition-algebra classification over arbitrary fields (Jacobson,
Kaplansky: composition algebras exist exactly in dimensions 1, 2, 4,
8), the full linear monoid M_n(F_q) is von Neumann regular (Putcha,
Okninski), Pearl 1968 (over an arbitrary field, the Moore-Penrose
inverse w.r.t. transpose exists iff rank(A A^T) = rank(A^T A) =
rank(A)), the multiplication algebra of a central simple algebra is
the full endomorphism ring (A tensor A^op = End_F(A)), and the
commutator subgroup [GL_n(F_q), GL_n(F_q)] = SL_n(F_q) away from tiny
exceptions (Dieudonne).

Findings preview (full statements at the bottom):
  1. ONE CHANNEL-SENSITIVE FLOOR, THEN UNIFORM COLLAPSE: floor 1
     (doubling Z/N once) is the Gaussian decality -- channel p splits
     iff p = 1 mod 4 (RAD: 5, 13, 17 split; 3, 7, 11 stay fields; 2
     ramifies). Floor 2 splits at EVERY odd channel: explicit
     isomorphism (-1,-1 | F_p) = M_2(F_p) constructed per channel.
     Channel 2 degenerates (commutative local ring, not M_2). No
     channel keeps division past the first doubling -- vs division
     up to floor 2 over R.
  2. THE NORM IS THE CHANNEL-COMPUTABLE SIZE: det is polynomial in the
     entries, hence channel-local (the locality criterion) -- a multiplicative
     size that lives INSIDE the locality class, where integer size was
     the information wall. Fibers exactly equidistributed over units
     (p^3 - p each); zero-divisor cone p^3 + p^2 - p; floor-3 cone
     p^7 + p^4 - p^3 (plus-type at every odd p).
  3. NILPOTENTS RETURN AND THE MEADOW SPLITS BY THE DECALITY: one
     doubling reinstates what squarefree-ness banished (p^2 - 1
     nonzero nilpotents per channel). Powering inverse (Clifford
     a^(m+1) = a) dead for every m; central-polynomial regularity
     dead; the adjugate map adj(A) det(A)^(2p-3) is a total polynomial
     unit-exact inverse but the cone collapses to 0 (meadow laws die);
     von Neumann regularity always total but choiceful; the canonical
     choice-free patch (Moore-Penrose) is total exactly at the
     p = 3 mod 4 channels -- the floor-1 norm x^2 + y^2 controls
     floor-2 meadow totality (failures = rank-1 with isotropic row or
     column space, count 4p(p-1)).
  4. NAPIER NARROWS TO THE NORM: GL_2(F_p) is nonabelian -- no index
     coordinate at floor 2. The commutator subgroup is exactly SL_2
     (verified p = 3..17), so the abelianization is F_p^* via det:
     everything loggable factors through the norm. ind o det is the
     whole floor-2 Napier move. Channel 2 exceptional (GL_2(F_2) = S_3,
     det blind).
  5. THE CRITERION SATURATES WITHIN CHANNELS, HOLDS ACROSS THEM:
     channel-local = compatible verbatim on M_2(Z/N) (the locality
     criterion's proof never used commutativity); with noncommutative coefficients every
     function M_2(F_p) -> M_2(F_p) is a generalized polynomial
     (constructive circuit: entry extraction E_1r X E_c1 = x_rc E_11 +
     Lagrange; verified pointwise), and the CRT glue collapses to one
     line -- central idempotents are now COEFFICIENTS.
  6. COMPOSITION OUTLIVES DIVISION BY EXACTLY TWO FLOORS: division
     dies at floor 2 (Wedderburn), the norm keeps composing through
     floors 2 and 3, and dies at floor 4 (witness over F_3) --
     the Hurwitz floors 1, 2, 4, 8 verbatim over the tower.

Runs on RAD's channels with exhaustive small cross-checks.
~2 s, ~24 MB.
"""

import sys, os, random
from functools import reduce
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import RAD_RING

random.seed(44)
R = RAD_RING
PRIMES = R.primes          # (2, 3, 5, 7, 11, 13, 17)
ODD = [p for p in PRIMES if p != 2]

def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)

# ---------------------------------------------------------------- 2x2 kit
def mmul(A, B, m):
    a, b, c, d = A; e, f, g, h = B
    return ((a*e + b*g) % m, (a*f + b*h) % m, (c*e + d*g) % m, (c*f + d*h) % m)

def madd(A, B, m):
    return tuple((x + y) % m for x, y in zip(A, B))

def msca(s, A, m):
    return tuple((s * x) % m for x in A)

def mdet(A, m):
    a, b, c, d = A
    return (a*d - b*c) % m

def mtra(A):
    a, b, c, d = A
    return (a, c, b, d)

def madj(A, m):
    a, b, c, d = A
    return (d % m, -b % m, -c % m, a % m)

def rank2(A, p):
    if mdet(A, p) != 0:
        return 2
    return 1 if any(A) else 0

ID = (1, 0, 0, 1)
ZERO = (0, 0, 0, 0)
E12 = (0, 1, 0, 0)

def all_mats(m):
    return [(a, b, c, d) for a in range(m) for b in range(m)
            for c in range(m) for d in range(m)]

def minv_unit(A, p):
    """Inverse of an invertible matrix over F_p (adjugate / det)."""
    di = pow(mdet(A, p), p - 2, p)
    return msca(di, madj(A, p), p)

# ------------------------------------------------- Cayley-Dickson kit
# Doubling with gamma = -1 throughout: (a,b)(c,d) = (ac - conj(d) b,
# d a + b conj(c)). Base = F_p (conj = id). Norm form = sum of squares.
def cd_conj(x):
    n = len(x)
    if n == 1:
        return list(x)
    h = n // 2
    return cd_conj(x[:h]) + [(-v) % CD_P for v in x[h:]]

def cd_mul(x, y):
    n = len(x)
    if n == 1:
        return [x[0] * y[0] % CD_P]
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    dc = cd_conj(d)
    cc = cd_conj(c)
    first = [(u - v) % CD_P for u, v in zip(cd_mul(a, c), cd_mul(dc, b))]
    second = [(u + v) % CD_P for u, v in zip(cd_mul(d, a), cd_mul(b, cc))]
    return first + second

def cd_norm(x):
    return sum(v * v for v in x) % CD_P

def cd_rand(dim):
    return [random.randrange(CD_P) for _ in range(dim)]

# ----------------------------------------------------------------------
section("I. FLOOR 1: THE DOUBLING ENTERS CHANNEL-SENSITIVELY (the decality)")
# ----------------------------------------------------------------------
# First Cayley-Dickson step over Z/N = adjoin i with i^2 = -1. Per
# channel: F_p[i] splits into F_p x F_p iff -1 is a QR iff p = 1 mod 4
# (the Gaussian decality). The only floor where the
# channels disagree.
split1, field1 = [], []
for p in ODD:
    has_i = any(x * x % p == p - 1 for x in range(p))
    assert has_i == (p % 4 == 1)
    (split1 if has_i else field1).append(p)
assert split1 == [5, 13, 17] and field1 == [3, 7, 11]
print(f"floor 1 per channel: split {split1}, field {field1}, ramified [2]")
print("  (x^2+1 = (x+1)^2 mod 2)  -- the Gaussian decality re-enters as")
print("  the ladder's ONLY channel-sensitive floor.")

# ----------------------------------------------------------------------
section("II. FLOOR 2 SPLITS UNIFORMLY: (-1,-1 | F_p) = M_2(F_p), EVERY ODD p")
# ----------------------------------------------------------------------
# Wedderburn forbids a finite division algebra; Chevalley-Warning makes
# the 4-variable norm form isotropic at every odd p. Constructive leg:
# find X, Y in M_2(F_p) with X^2 = Y^2 = -I, XY = -YX, {I,X,Y,XY}
# spanning -- then i -> X, j -> Y extends to an algebra map from the
# 4-dim quaternion algebra ONTO M_2(F_p) (relations hold), and equal
# dimensions make it an isomorphism.
def gauss_rank(rows, p):
    rows = [list(r) for r in rows]
    rank, ncol = 0, len(rows[0])
    for col in range(ncol):
        piv = next((i for i in range(rank, len(rows)) if rows[i][col] % p), None)
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        inv = pow(rows[rank][col], p - 2, p)
        rows[rank] = [v * inv % p for v in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col] % p:
                f = rows[i][col]
                rows[i] = [(v - f * w) % p for v, w in zip(rows[i], rows[rank])]
        rank += 1
    return rank

for p in ODD:
    X = (0, p - 1, 1, 0)                      # [[0,-1],[1,0]], X^2 = -I
    negI = msca(p - 1, ID, p)
    assert mmul(X, X, p) == negI
    Y = None
    for cand in all_mats(p):
        if mmul(cand, cand, p) != negI:
            continue
        XY = mmul(X, cand, p)
        if XY != msca(p - 1, mmul(cand, X, p), p):
            continue
        if gauss_rank([ID, X, cand, XY], p) == 4:
            Y = cand
            break
    assert Y is not None
    print(f"  p={p:2d}: i->{X}, j->{Y}  (relations + spanning checked)")
print("floor 2 = M_2(F_p) at every odd channel: no channel keeps division")
print("  past the FIRST doubling (and the p = 1 mod 4 channels lose it at")
print("  the ground floor) -- vs division up to floor 2 over R (Frobenius).")

# Channel 2 degenerates: at char 2, -1 = 1, the doubling is commutative.
CD_P = 2
quat2 = [[a, b, c, d] for a in range(2) for b in range(2)
         for c in range(2) for d in range(2)]
assert all(cd_mul(x, y) == cd_mul(y, x) for x in quat2 for y in quat2)
one_plus_i = [1, 1, 0, 0]
assert cd_mul(one_plus_i, one_plus_i) == [0, 0, 0, 0]
units2 = sum(1 for x in quat2 if any(cd_mul(x, y) == [1, 0, 0, 0] for y in quat2))
assert units2 == 8
print(f"channel 2: floor-2 doubling is COMMUTATIVE (all 256 pairs), local")
print(f"  ring F_2[C2 x C2] -- 8 units of 16, (1+i)^2 = 0. Not M_2(F_2).")

# Tower-wide the channel question is trivial: M_2(Z/N) =
# prod M_2(F_p) entrywise. One-line spot check, then move on.
for _ in range(300):
    A = tuple(random.randrange(6) for _ in range(4))
    B = tuple(random.randrange(6) for _ in range(4))
    AB = mmul(A, B, 6)
    for p in (2, 3):
        assert tuple(v % p for v in AB) == mmul(tuple(v % p for v in A),
                                                tuple(v % p for v in B), p)
print("M_2(Z/6) = M_2(F_2) x M_2(F_3) entrywise (by construction; spot check).")

# ----------------------------------------------------------------------
section("III. THE COMPOSITION NORM = THE CHANNEL-COMPUTABLE SIZE")
# ----------------------------------------------------------------------
# det is the composition norm of the split quaternions: multiplicative,
# POLYNOMIAL in the entries -- hence channel-local by the locality
# criterion (n-variable version). The contrast this hunt chases: integer size is
# the tower's information wall; the algebra's intrinsic size-analogue
# sits INSIDE the locality class.
mats2 = all_mats(2)
mats3 = all_mats(3)
assert all(mdet(mmul(A, B, 2), 2) == mdet(A, 2) * mdet(B, 2) % 2
           for A in mats2 for B in mats2)
assert all(mdet(mmul(A, B, 3), 3) == mdet(A, 3) * mdet(B, 3) % 3
           for A in mats3 for B in mats3)
for _ in range(2000):
    A = tuple(random.randrange(6) for _ in range(4))
    B = tuple(random.randrange(6) for _ in range(4))
    assert mdet(mmul(A, B, 6), 6) == mdet(A, 6) * mdet(B, 6) % 6
    for p in (2, 3):
        assert mdet(A, 6) % p == mdet(tuple(v % p for v in A), p)
print("det multiplicative (exhaustive p=2,3; sampled Z/6) and channel-local")
print("  (det mod p = det of the mod-p reduction; it is a polynomial).")

# Fibers: |det = d| = p^3 - p for every unit d, cone |det = 0| =
# p^3 + p^2 - p. Exhaustive at every odd RAD channel.
for p in ODD:
    counts = [0] * p
    for a in range(p):
        for b in range(p):
            for c in range(p):
                bc = b * c
                for d in range(p):
                    counts[(a * d - bc) % p] += 1
    assert counts[0] == p**3 + p**2 - p
    assert all(counts[d] == p**3 - p for d in range(1, p))
print(f"fibers exhaustive p in {ODD}: cone p^3+p^2-p, units p^3-p each")
print("  (exactly flat over units).")

# Unit test is per-channel cone-avoidance: A invertible in M_2(Z/6) iff
# det(A) is a unit of Z/6. Exhaustive count cross-check.
g6 = sum(1 for A in all_mats(6) if mdet(A, 6) % 2 != 0 and mdet(A, 6) % 3 != 0)
assert g6 == 6 * 48                      # |GL_2(F_2)| * |GL_2(F_3)|
sample = random.sample(all_mats(6), 200)
for A in sample:
    has_inv = any(mmul(A, X, 6) == ID and mmul(X, A, 6) == ID
                  for X in all_mats(6))
    assert has_inv == (mdet(A, 6) % 2 != 0 and mdet(A, 6) % 3 != 0)
print(f"|GL_2(Z/6)| = {g6} = 6 * 48; invertible iff det avoids every")
print("  channel's cone (brute-checked on 200 random matrices).")

# Floor-3 cone (split octonion norm = 8 squares): plus-type count
# p^7 + p^4 - p^3 at every odd channel (discriminant 1 -> plus type).
for p in ODD:
    sq = [0] * p
    for x in range(p):
        sq[x * x % p] += 1
    vec = [1] + [0] * (p - 1)
    for _ in range(8):
        new = [0] * p
        for u, cu in enumerate(vec):
            if cu:
                for v, cv in enumerate(sq):
                    new[(u + v) % p] += cu * cv
        vec = new
    assert vec[0] == p**7 + p**4 - p**3
print(f"floor-3 cone exhaustive (DP) p in {ODD}: p^7 + p^4 - p^3 (plus type)")

# ----------------------------------------------------------------------
section("IV. NILPOTENTS RETURN; THE MEADOW SPLITS BY THE DECALITY")
# ----------------------------------------------------------------------
# Squarefree-ness banished nilpotents from Z/N (the lesson of
# explore_super_log.py: they
# kill the Clifford extension). One doubling reinstates them over a
# FIELD: E12^2 = 0. Census: p^2 - 1 nonzero nilpotents per channel.
for p in (2, 3, 5):
    nil = sum(1 for A in all_mats(p)
              if any(A) and mmul(A, A, p) == ZERO)
    assert nil == p * p - 1
print("nonzero nilpotents in M_2(F_p): p^2 - 1 (exhaustive p = 2, 3, 5)")

# Tier 1 -- powering (Clifford) inverse: DEAD. a^(m+1) = a fails for
# every m at any nilpotent (E12^k = 0 for k >= 2).
assert mmul(E12, E12, 5) == ZERO
print("tier 1 (Clifford a^(m+1) = a): DEAD for every m -- E12^(m+1) = 0.")

# Tier 2 -- central-polynomial regularity: DEAD. If g(A) commutes with
# A and A g(A) A = A, then A^2 g(A) = A; at a nilpotent that reads
# 0 = A. Exhaustive confirmation: no X commuting with E12 satisfies
# E12 X E12 = E12 (p = 2, 3).
for p in (2, 3):
    assert not any(mmul(E12, X, p) == mmul(X, E12, p)
                   and mmul(mmul(E12, X, p), E12, p) == E12
                   for X in all_mats(p))
print("tier 2 (any polynomial in A with scalar coefficients): DEAD --")
print("  commuting inner inverses do not exist at nilpotents (exhaustive).")

# The adjugate meadow map: minv(A) = adj(A) det(A)^(2p-3). Total,
# polynomial, unit-exact; the cone collapses to 0, so the meadow laws
# (x * x^-1 * x = x, (x^-1)^-1 = x) die on the cone.
for p in (2, 3, 5):
    for A in all_mats(p):
        d = mdet(A, p)
        # det^(p-2) realizes the meadow inverse of det for p >= 3; at
        # p = 2 the exponent is 0 and 0^0 = 1 breaks the 0 -> 0 leg,
        # so the uniform polynomial form is det^(2p-3) (= det^(p-2)
        # times det^(p-1), the unit indicator).
        MA = msca(pow(d, 2 * p - 3, p), madj(A, p), p)
        if mdet(A, p) != 0:
            assert mmul(A, MA, p) == ID
        else:
            assert MA == ZERO
print("adjugate map adj(A) det^(2p-3): total + polynomial + unit-exact,")
print("  cone -> 0 (exhaustive p = 2, 3, 5); meadow laws fail at E12.")

# Tier 3 -- von Neumann regularity: ALWAYS total (the full linear
# monoid is regular) but requires a CHOICE of inner inverse.
for p in (2, 3, 5):
    mats = all_mats(p)
    assert all(any(mmul(mmul(A, X, p), A, p) == A for X in mats)
               for A in mats)
print("tier 3 (von Neumann AXA = A): total, exhaustive p = 2, 3, 5 --")
print("  but choiceful: no canonical X without extra structure.")

# Tier 4 -- the canonical choice-free patch: Moore-Penrose w.r.t.
# transpose. Pearl's criterion: exists iff rank(AA^T) = rank(A^TA) =
# rank(A). Verified against brute force exhaustively at p = 2, 3, 5
# (uniqueness checked at p = 2, 3).
def mp_exists_brute(A, p, mats):
    found = 0
    for X in mats:
        AX, XA = mmul(A, X, p), mmul(X, A, p)
        if (mmul(AX, A, p) == A and mmul(XA, X, p) == X
                and AX == mtra(AX) and XA == mtra(XA)):
            found += 1
    return found

def mp_exists_rank(A, p):
    r = rank2(A, p)
    return (rank2(mmul(A, mtra(A), p), p) == r
            and rank2(mmul(mtra(A), A, p), p) == r)

for p in (2, 3):
    for A in all_mats(p):
        n = mp_exists_brute(A, p, all_mats(p))
        assert (n > 0) == mp_exists_rank(A, p)
        assert n <= 1
mats5 = all_mats(5)
for A in mats5:
    assert (mp_exists_brute(A, 5, mats5) > 0) == mp_exists_rank(A, 5)
print("Moore-Penrose existence = Pearl's rank criterion (exhaustive")
print("  p = 2, 3 with uniqueness; exhaustive p = 5).")

# The punchline: MP totality splits by the DECALITY. Failures are the
# rank-1 matrices with isotropic row or column space for the dot
# product -- and x^2 + y^2 = 0 has nonzero solutions iff p = 1 mod 4:
# the FLOOR-1 norm controls the FLOOR-2 meadow. Census per channel.
def iso_vec(v, p):
    return (v[0] * v[0] + v[1] * v[1]) % p == 0

def iso_rank1_set(p):
    """Rank-1 matrices with isotropic row or column space (computed
    directly, independent of the MP criterion)."""
    out = set()
    for A in all_mats(p):
        if rank2(A, p) != 1:
            continue
        a, b, c, d = A
        row = (a, b) if (a or b) else (c, d)
        col = (a, c) if (a or c) else (b, d)
        if iso_vec(row, p) or iso_vec(col, p):
            out.add(A)
    return out

for p in ODD:
    fails = {A for A in all_mats(p) if not mp_exists_rank(A, p)}
    iso = iso_rank1_set(p)
    assert fails == iso                       # set EQUALITY, both ways
    if p % 4 == 3:
        assert fails == set()
    else:
        assert len(fails) == 4 * p * (p - 1)
    tag = "TOTAL" if p % 4 == 3 else f"{len(fails)} failures = 4p(p-1)"
    print(f"  p={p:2d} ({'3' if p%4==3 else '1'} mod 4): MP {tag}")
# Channel 2 fails too -- char-2 isotropy ((1,1) is self-orthogonal):
fails2 = {A for A in all_mats(2) if mp_exists_brute(A, 2, all_mats(2)) == 0}
assert fails2 == iso_rank1_set(2) and len(fails2) == 5
print("  p= 2: 5 failures of 16 (char-2 isotropy: (1,1).(1,1) = 0)")
print("MP failure set = rank-1 with isotropic row or column space (set")
print("  equality, exhaustive per channel): total exactly at the")
print("  p = 3 mod 4 channels -- the floor-1 norm's isotropy (the")
print("  decality) is the floor-2 meadow obstruction.")

# ----------------------------------------------------------------------
section("V. NAPIER NARROWS TO THE NORM: [GL_2, GL_2] = SL_2")
# ----------------------------------------------------------------------
# GL_2(F_p) is nonabelian -- no index coordinate exists at floor 2.
# What survives: the subgroup generated by commutators reaches ALL of
# SL_2 (size p^3 - p), and commutators have det 1, so [GL_2, GL_2] =
# SL_2 exactly and the abelianization is F_p^* via det. Everything
# loggable factors through the norm.
for p in ODD:
    units = [A for A in all_mats(p) if mdet(A, p) != 0]
    U12, L21 = (1, 1, 0, 1), (1, 0, 1, 1)      # transvections, in GL_2
    assert mmul(U12, L21, p) != mmul(L21, U12, p)
    gens = []
    for _ in range(40):
        U, V = random.choice(units), random.choice(units)
        gens.append(mmul(mmul(U, V, p),
                         mmul(minv_unit(U, p), minv_unit(V, p), p), p))
    S = {ID}
    frontier = [ID]
    while frontier:
        new = []
        for s in frontier:
            for g in gens:
                t = mmul(s, g, p)
                if t not in S:
                    S.add(t)
                    new.append(t)
        frontier = new
    assert len(S) == p**3 - p
    assert all(mdet(s, p) == 1 for s in S)
    print(f"  p={p:2d}: commutators generate {len(S)} = p^3-p elements,"
          f" all det 1  -> [GL_2,GL_2] = SL_2, abelianization = F_p^*")
print("Napier's move at floor 2 exists ONLY through det: ind o det is")
print("  the complete floor-2 index transform (findings 2+4 fuse: the")
print("  channel-computable size IS the residual logarithm).")

# Channel 2 exceptional: GL_2(F_2) = S_3, det is blind (F_2^* trivial)
# but the abelianization is C_2 (the sign of the permutation).
units = [A for A in all_mats(2) if mdet(A, 2) != 0]
assert len(units) == 6
comms = {mmul(mmul(U, V, 2), mmul(minv_unit(U, 2), minv_unit(V, 2), 2), 2)
         for U in units for V in units}
S = {ID}
frontier = [ID]
while frontier:
    new = []
    for s in frontier:
        for g in comms:
            t = mmul(s, g, 2)
            if t not in S:
                S.add(t); new.append(t)
    frontier = new
assert len(S) == 3
print("channel 2: GL_2(F_2) = S_3, commutator subgroup C_3, abelianization")
print("  C_2 -- det sees none of it (F_2^* = 1). The exceptional channel.")

# ----------------------------------------------------------------------
section("VI. THE CRITERION: SATURATES WITHIN CHANNELS, HOLDS ACROSS THEM")
# ----------------------------------------------------------------------
# Across channels the locality criterion's proof transfers verbatim (it never used
# commutativity of the value ring: a function M_2(Z/N) -> M_2(Z/N) is
# 4 functions of 4 scalar variables). Within a channel, noncommutative
# COEFFICIENTS saturate the polynomial class: every function
# M_2(F_p) -> M_2(F_p) is a generalized polynomial. Constructive:
# E_1r X E_c1 = x_rc E_11 extracts entries into the (1,1) corner,
# corner values multiply like scalars, Lagrange builds any function of
# the entries, and E_k1 (.) E_1l moves the corner anywhere. (Classical
# shadow: A tensor A^op = End_F(A) for central simple A.)

# nc-polynomial circuits: ('X',), ('C', mat), ('+', t, u), ('*', t, u)
def nc_eval(t, X, m):
    if t[0] == 'X':
        return X
    if t[0] == 'C':
        return t[1]
    a, b = nc_eval(t[1], X, m), nc_eval(t[2], X, m)
    return madd(a, b, m) if t[0] == '+' else mmul(a, b, m)

def emat(r, c):
    M = [0, 0, 0, 0]
    M[2 * r + c] = 1
    return tuple(M)

XV = ('X',)

def extractor(r, c):
    """Circuit for x_rc E_11."""
    return ('*', ('*', ('C', emat(0, r)), XV), ('C', emat(c, 0)))

def build_nc(table, p):
    """Explicit generalized-polynomial circuit for an arbitrary
    function table: M_2(F_p) -> M_2(F_p)."""
    pts = all_mats(p)
    terms = []
    for a in pts:
        val = table[a]
        if val == ZERO:
            continue
        # Lagrange indicator of point a, valued in the (1,1) corner
        factors = []
        norm = 1
        for i in range(4):
            for c in range(p):
                if c != a[i]:
                    factors.append(('+', extractor(i // 2, i % 2),
                                    ('C', msca((-c) % p, emat(0, 0), p))))
                    norm = norm * (a[i] - c) % p
        ind = reduce(lambda t, u: ('*', t, u), factors)
        ind = ('*', ('C', msca(pow(norm, p - 2, p), emat(0, 0), p)), ind)
        for k in range(2):
            for l in range(2):
                if val[2 * k + l]:
                    terms.append(('*', ('*', ('C', msca(val[2 * k + l],
                                                        emat(k, 0), p)), ind),
                                  ('C', emat(0, l))))
    return reduce(lambda t, u: ('+', t, u), terms) if terms else ('C', ZERO)

# Exhaustive verification: p = 2 (three random functions, all 16
# inputs) and p = 3 (one random function, all 81 inputs).
for p, n_funcs in ((2, 3), (3, 1)):
    pts = all_mats(p)
    for _ in range(n_funcs):
        table = {A: random.choice(pts) for A in pts}
        circ = build_nc(table, p)
        assert all(nc_eval(circ, A, p) == table[A] for A in pts)
print("every function M_2(F_p) -> M_2(F_p) is a generalized polynomial:")
print("  explicit circuits built + verified pointwise (p = 2: all 16")
print("  inputs x 3 functions; p = 3: all 81 inputs).")

# The CRT glue collapses to one line: central idempotents are now
# COEFFICIENTS. glued(X) = e_2 f_2(X) + e_3 f_3(X) with e_2 = 3,
# e_3 = 4 in Z/6 -- a single circuit, channel-correct at every point.
pts2, pts3 = all_mats(2), all_mats(3)
t2_table = {A: random.choice(pts2) for A in pts2}
t3_table = {A: random.choice(pts3) for A in pts3}
glued = ('+', ('*', ('C', msca(3, ID, 6)), build_nc(t2_table, 2)),
              ('*', ('C', msca(4, ID, 6)), build_nc(t3_table, 3)))
for _ in range(150):
    A = tuple(random.randrange(6) for _ in range(4))
    val = nc_eval(glued, A, 6)
    assert tuple(v % 2 for v in val) == t2_table[tuple(v % 2 for v in A)]
    assert tuple(v % 3 for v in val) == t3_table[tuple(v % 3 for v in A)]
print("CRT glue in one line: e_2 f_2(X) + e_3 f_3(X) over M_2(Z/6) --")
print("  the idempotent is a coefficient, not degreewise bookkeeping")
print("  (150 random points, both channels exact).")
print("=> channel-local = compatible = generalized polynomial; the wall")
print("   keeps its cross-channel teeth while the within-channel")
print("   polynomial hierarchy saturates.")

# ----------------------------------------------------------------------
section("VII. FLOORS 3 AND 4: COMPOSITION DIES AT THE HURWITZ BOUNDARY")
# ----------------------------------------------------------------------
# Floor 3 (octonion doubling, split by Chevalley-Warning + Artin-Zorn):
# nonassociative but ALTERNATIVE, norm still composes, zero divisors
# at the cone. Floor 4 (sedenion doubling): composition and
# alternativity both fail. Hurwitz floors 1, 2, 4, 8 verbatim.
for CD_P in (3, 5):
    one = [1] + [0] * 7
    # x conj(x) = N(x) * 1 (samples)
    for _ in range(400):
        x = cd_rand(8)
        xc = cd_mul(x, cd_conj(x))
        assert xc == [cd_norm(x)] + [0] * 7
    # nonassociative witness
    wit = next((x, y, z) for x, y, z in
               ((cd_rand(8), cd_rand(8), cd_rand(8)) for _ in range(2000))
               if cd_mul(cd_mul(x, y), z) != cd_mul(x, cd_mul(y, z)))
    # alternative laws hold (samples)
    for _ in range(3000):
        x, y = cd_rand(8), cd_rand(8)
        assert cd_mul(cd_mul(x, x), y) == cd_mul(x, cd_mul(x, y))
        assert cd_mul(cd_mul(y, x), x) == cd_mul(y, cd_mul(x, x))
    # composition holds (samples)
    for _ in range(3000):
        x, y = cd_rand(8), cd_rand(8)
        assert cd_norm(cd_mul(x, y)) == cd_norm(x) * cd_norm(y) % CD_P
    # zero divisors at the cone: x != 0, N(x) = 0 -> x conj(x) = 0
    x = next(x for x in (cd_rand(8) for _ in range(3000))
             if any(x) and cd_norm(x) == 0)
    assert cd_mul(x, cd_conj(x)) == [0] * 8
    print(f"  p={CD_P}: floor 3 nonassociative (witness), alternative +"
          f" composing (3000 samples each), cone = zero divisors")

CD_P = 3
comp_fail = next((x, y) for x, y in
                 ((cd_rand(16), cd_rand(16)) for _ in range(5000))
                 if cd_norm(cd_mul(x, y)) != cd_norm(x) * cd_norm(y) % 3)
alt_fail = next((x, y) for x, y in
                ((cd_rand(16), cd_rand(16)) for _ in range(5000))
                if cd_mul(cd_mul(x, x), y) != cd_mul(x, cd_mul(x, y)))
print("  p=3: floor 4 -- N(xy) != N(x)N(y) (witness found) and")
print("       x(xy) != (xx)y (witness found): composition AND")
print("       alternativity die at the fourth doubling.")
print("division dies at floor 2 (Wedderburn), composition at floor 4")
print("  (Hurwitz 1, 2, 4, 8) -- the ladder's long shadow is the norm.")

# ----------------------------------------------------------------------
section("FINDINGS")
# ----------------------------------------------------------------------
print("""
1. ONE CHANNEL-SENSITIVE FLOOR, THEN UNIFORM COLLAPSE (rule +
   classical contacts). Floor 1 is the Gaussian decality: channel p
   splits iff p = 1 mod 4 (RAD: 5, 13, 17 split / 3, 7, 11 field / 2
   ramified). Floor 2 splits at EVERY odd channel -- explicit iso
   (-1,-1 | F_p) = M_2(F_p) constructed per channel (Wedderburn +
   Chevalley-Warning behind it); channel 2 degenerates to the
   commutative local ring F_2[C2 x C2]. No channel keeps division
   past the first doubling, and the p = 1 mod 4 channels lose it at
   the ground floor -- vs division up to floor 2 over R (Frobenius).

2. THE NORM IS THE CHANNEL-COMPUTABLE SIZE (rule). det is polynomial
   in the entries, hence channel-local (the locality criterion): a
   multiplicative size-analogue that lives INSIDE the locality class,
   where integer size was the information wall. Honest limit: it is
   the multiplicative half of size only -- char p admits no order.
   Fibers exactly equidistributed over units (p^3 - p each), cone
   p^3 + p^2 - p; floor-3 cone p^7 + p^4 - p^3 (plus type at every
   odd channel). Unit test = per-channel cone avoidance.

3. NILPOTENTS RETURN AND THE MEADOW SPLITS BY THE DECALITY (rule).
   One doubling reinstates what squarefree-ness banished: p^2 - 1
   nonzero nilpotents per channel (E12^2 = 0) -- the same disease that
   kills the Clifford extension of explore_super_log.py off the
   squarefree locus, now
   unavoidable over a field. Inverse tiers: powering (a^(m+1) = a)
   DEAD for every m; central-polynomial regularity DEAD (commuting
   inner inverses die at nilpotents, exhaustive p <= 3); the adjugate
   map adj(A) det(A)^(2p-3) is a total polynomial unit-exact inverse
   with cone -> 0 (meadow laws fail on the cone); von Neumann
   regularity is total but choiceful; the canonical choice-free patch
   (Moore-Penrose, Pearl's rank criterion verified) is total exactly
   at the p = 3 mod 4 channels -- failures are the 4p(p-1) rank-1
   matrices with isotropic row or column space, so the FLOOR-1 norm
   x^2 + y^2 governs the FLOOR-2 meadow.

4. NAPIER NARROWS TO THE NORM (rule). GL_2(F_p) is nonabelian: no
   index coordinate exists at floor 2. The commutator subgroup is
   exactly SL_2 (generated-subgroup = full p^3 - p, every odd RAD
   channel), so the abelianization is F_p^* via det and every
   homomorphism to an abelian group factors through the norm:
   ind o det is the complete floor-2 Napier move. Findings 2+4 fuse --
   the channel-computable size IS the residual logarithm. Channel 2
   exceptional: GL_2(F_2) = S_3, abelianization C_2, det blind.

5. THE CRITERION SATURATES WITHIN CHANNELS, HOLDS ACROSS THEM (rule).
   Channel-local = compatible on M_2(Z/N) verbatim (the locality
   criterion's proof never used commutativity). Within a channel, noncommutative
   coefficients saturate the polynomial class: every function
   M_2(F_p) -> M_2(F_p) is a generalized polynomial -- constructive
   circuits (entry extraction E_1r X E_c1 = x_rc E_11 + Lagrange)
   verified pointwise at p = 2, 3; classical shadow A (x) A^op =
   End(A). The CRT glue collapses to one line because central
   idempotents are now coefficients: e_2 f_2(X) + e_3 f_3(X).

6. COMPOSITION OUTLIVES DIVISION BY EXACTLY TWO FLOORS (rule +
   Hurwitz). Division dies at floor 2 (Wedderburn); the norm keeps
   composing through floor 3 (alternative; classical -- composition
   algebras exist in dims 1, 2, 4, 8 over any field -- with 3000-pair
   sample checks at p = 3, 5) and dies at floor 4 (explicit witnesses
   over F_3 for both composition and alternativity). The Hurwitz
   dimensions 1, 2, 4, 8 hold verbatim
   over the tower: the ladder ends where it ends everywhere, but
   over the tower its long shadow -- the norm -- is channel-local.
""")
print("done.")
