"""
FRAME STEP 2: THE LIMIT OBJECT -- what the tower converges to. (P46)

The places frame (gated P45-P47; ROAD THE FRAME) reads each
rung Z/p_k# as the integers seen through the first k residue windows,
with the archimedean window deleted. Step 2 makes the k -> infinity
limit precise and charts which blueprint properties survive it. The
transition maps of the tower (reduction Z/p_{k+1}# -> Z/p_k#) are, in
CRT coordinates, coordinate-forgetting projections -- so the inverse
limit is the FULL PRODUCT Pi_p F_p of all residue fields. Every prime's
exponent stays 1 forever: the limit is NOT the profinite completion
Z-hat = lim Z/n = Pi Z_p (the limit of the ALL-MODULI system --
fattening without bound; the fat Pareto tower (archived P219) is a BOUNDED
fattening, finite by finality, not this system), not the finite
adeles (no Z_p to restrict against), not an ultraproduct (no
quotient taken).
Thin-vs-fat in the limit is one classical line: Pi F_p =
Z-hat / J(Z-hat) -- the thin limit is the unbounded-fat limit's
semisimple quotient; fattening is the radical the thin tower never
grows, and stripping it recovers thin at EVERY fattening level.

Survey anchors (standard material, named so nothing here poses as new):
Z-hat = lim Z/n = Pi Z_p (profinite completion; CRT in the limit), the
finite adeles as the RESTRICTED product of the Q_p with respect to the
Z_p (Tate's thesis, Weil), Ostrowski (the places of Q = the primes plus
ONE archimedean place), Artin-Whaples 1945 (product-formula axioms;
finiteness: x != 0 has |x|_v != 1 at only finitely many v), von Neumann
regularity of products of fields and J(Pi R_i) = Pi J(R_i) (standard
commutative algebra), Spec of a product of fields over an index set X =
the Stone-Cech compactification beta(X), residue fields at non-principal
points = the ultraproducts (Stone duality on the idempotent algebra
P(X)), Ax 1968 (Pi F_p / U is a pseudo-finite field, characteristic 0
for non-principal U; Los's theorem), Mertens 1874
(prod_{p<=x}(1-1/p) ~ e^(-gamma)/ln x; sum_{p<=x} 1/p = ln ln x + M,
M = 0.26149...), Borel-Cantelli (coordinates are independent under the
product Haar measure), strong approximation (NAMED as Step 3(b)'s
subject; the density used below is plain finite CRT, nothing more).

Findings preview (full statements at the bottom):
  1. THE LIMIT IS THE FULL PRODUCT (rule + classical): lim Z/p_k# =
     Pi_p F_p -- transition maps verified to be channel-forgetting
     projections (exhaustive k <= 5, sampled k = 6, 7). v_p = 1 at
     every rung, so no Z_p ever forms; Pi F_p = Z-hat/J(Z-hat) (finite
     shadow verified: squared rungs AND the (archived) Pareto fat
     ring reduce mod their Jacobson radical to the thin rung).
  2. THE BIJECTION SPLITS (rule + classical): the per-rung bijection
     Z/N <-> tuples splits in the limit into injectivity of Z -> Pi F_p
     -- certified ONLY by the deleted place (every finite window set S
     has kernel containing prod(S); the certificate "p > |n| implies
     p does not divide n" is a size bound) -- plus density (= finite
     CRT). Decode-uniqueness was the height cut; it does not survive.
     Mirror refinement: in F_2[x] the same certificate is deg, the
     deleted place at infinity, which is NON-archimedean -- the
     mechanism is deleted-ness; over Q the deleted place happens to be
     the archimedean one (Ostrowski).
  3. THE BLUEPRINT SPLITS THREE WAYS (rule): STABLE -- all-field
     channels, meadow (coordinatewise, von Neumann regular), idempotent
     lattice (completes from 2^k to the full power set P(Primes)).
     DIES -- lambda (every fixed exponent fails at ALL channels
     p > lambda+1), and with it the Clifford identity a^(lambda+1) = a,
     the P37 collapse-measurement x^lambda, the meadow-as-one-polynomial
     formula a^(lambda-1); ECC dies with the height (no archimedean
     place, no cut, no code -- the P45 audit reading made exact).
     SPLITS -- the P38 criterion: channel-local = compatible STRICTLY
     CONTAINS polynomial in the limit (witness: the pseudo-inverse,
     whose minimal per-channel degree p-2 is unbounded).
  4. NO RING BETWEEN THE SUM AND THE PRODUCT (rule + classical): F_p
     has no proper unital subring, so no adelic-style ring-restricted
     product exists at residue-field level. Restricting by {0} gives
     the ideal Sum F_p (finite support -- meets Z only at 0);
     restricting by the units gives the finite-co-support locus, which
     is multiplicatively closed but NOT additively closed (witness);
     Z minus 0 lands inside that non-ring locus, a tiny part of it
     (Z meets Sum F_p only at 0). The adeles' fix -- restrict by
     Z_p -- is fattening, unavailable thin.
  5. BOUNDARY CHANNELS (classical contact, named not worn):
     Spec(Pi F_p) = beta(Primes); the principal points are our channels
     (residue fields F_p; verified: rung k has exactly k prime ideals);
     non-principal points have residue fields Pi F_p / U -- Ax's
     pseudo-finite fields of characteristic 0. Ghost channels:
     choice-dependent, nothing to compute, the model-theoretic
     neighbor placed and left alone.
  6. Z IS A NULL-SET ANOMALY (rule + classical): under Haar measure,
     almost every element of the limit has INFINITELY many zero
     channels (Borel-Cantelli: sum 1/p diverges, coordinates
     independent), while every nonzero integer has finitely many.
     Unit density dies at the Mertens rate e^(-gamma)/ln p_k (verified
     to 10^4 channels); the full sieve's surviving measure is 0, its
     surviving integers exactly {+1, -1}.

Runs on small rungs exhaustively + RAD + a 10^4-channel numerical
sweep. ~0.5 s, ~20 MB.
"""

import sys, os, math, random
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import (Ring, RAD_RING, encode, decode, decode_partial,
                 carmichael_lambda, factorize, primes_up_to, prod)

random.seed(46)

GAMMA = 0.5772156649015329
MERTENS_M = 0.2614972128476428

def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)

def thin_ring(k):
    ps = primes_up_to(200)[:k]
    return Ring(f"T{k}", tuple(ps), (1,) * k)

# ----------------------------------------------------------------------
section("I. THE INVERSE SYSTEM: TRANSITIONS FORGET CHANNELS")
# ----------------------------------------------------------------------
# The tower's transition map is reduction mod the smaller primorial.
# Claim: in CRT coordinates it is the projection that forgets the new
# channel -- nothing else moves. Hence a coherent sequence is exactly a
# free choice of one residue per prime: lim Z/p_k# = Pi_p F_p (full
# product). Exhaustive at k+1 <= 6, sampled at k+1 = 7, 8.
for k1 in range(3, 9):
    Rk1, Rk = thin_ring(k1), thin_ring(k1 - 1)
    xs = (range(Rk1.N) if Rk1.N <= 30030
          else random.sample(range(Rk1.N), 20000))
    for x in xs:
        assert encode(x % Rk.N, Rk) == encode(x, Rk1)[:k1 - 1]
    tag = "exhaustive" if Rk1.N <= 30030 else "sampled 20000"
    print(f"  Z/{Rk1.N} -> Z/{Rk.N}: transition = forget channel "
          f"{Rk1.primes[-1]}  ({tag})")
# Every exponent stays 1: no Z_p ever forms (the FAT system lim Z/n
# raises exponents without bound and converges to Z-hat = Pi Z_p).
for k in range(2, 13):
    assert all(e == 1 for e in factorize(thin_ring(k).N).values())
print("  v_p = 1 at every rung k <= 12 (squarefree by construction):")
print("  the limit is Pi_p F_p, the FULL product -- not Z-hat, not")
print("  restricted, not an ultraproduct quotient.")

# ----------------------------------------------------------------------
section("II. INTEGER POINTS: INJECTIVE + DENSE, NEVER SURJECTIVE")
# ----------------------------------------------------------------------
# (a) No finite window set certifies injectivity: for every finite set
# of primes S, prod(S) is a nonzero integer reading 0 at every p in S.
ps7 = RAD_RING.primes
for r in range(1, 8):
    for S in combinations(ps7, r):
        n = prod(S)
        assert n != 0 and all(n % p == 0 for p in S)
print("  every finite window set S has nonzero kernel prod(S)")
print("  (all 127 nonempty subsets of the RAD primes verified)")
# (b) The working certificate is a SIZE bound: p > |n| => p does not
# divide n. So ker(Z -> Pi_p F_p) = 0 -- by the deleted place.
import bisect
plist = primes_up_to(200000)
for n in range(1, 100001):
    p = plist[bisect.bisect_right(plist, n)]   # first prime > n
    assert n % p != 0
print("  certificate 'p > |n| => p ndiv n' verified n <= 1e5 (first")
print("  prime above n): injectivity is certified by the deleted")
print("  (archimedean) place -- no finite window set can certify it")
# (b') Mirror refinement: in F_2[x] (polynomials as bitmasks) the same
# certificate is deg -- the place at infinity, NON-archimedean. The
# mechanism is deleted-ness, not archimedean-ness.
def pmul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r
def pmod(a, m):
    dm = m.bit_length()
    while a.bit_length() >= dm:
        a ^= m << (a.bit_length() - dm)
    return a
irr = [f for f in range(2, 128)
       if all(pmod(f, g) != 0 for g in range(2, f) if g.bit_length() < f.bit_length())]
for g in random.sample(range(2, 1 << 11), 300):
    divs = [f for f in irr if pmod(g, f) == 0]
    assert all(f.bit_length() <= g.bit_length() for f in divs)
assert pmod(pmul(irr[0], irr[1]), irr[0]) == 0   # finite-window kernel
print("  mirror F_2[x]: irreducible divisors of g have deg <= deg g")
print("  (300 samples, deg <= 10); finite window sets again have kernel")
# (c) Density = finite CRT: any finite condition list is solvable in Z.
for _ in range(500):
    target = tuple(random.randrange(p) for p in ps7)
    assert encode(decode(target, RAD_RING), RAD_RING) == target
print("  density: 500 random finite condition sets solved in Z (CRT)")
# (d) Not surjective. Nonzero integers have FINITE co-support (zero
# channels exactly at p | n); exhibit a coherent tuple whose co-support
# grows without bound: x_p = 0 at p = 3 mod 4, x_p = 1 elsewhere.
LIM = 100000
spf = list(range(LIM + 1))              # smallest-prime-factor sieve
for i in range(2, int(LIM**0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, LIM + 1, i):
            if spf[j] == j:
                spf[j] = i
max_omega = 0
for n in range(2, LIM + 1):
    m, w = n, 0
    while m > 1:
        p = spf[m]
        w += 1
        while m % p == 0:
            m //= p
    max_omega = max(max_omega, w)
assert max_omega == 6                   # 2*3*5*7*11*13 = 30030 <= 1e5
print("  nonzero integers: co-support = the prime divisors -- finite,")
print(f"  and tiny: max {max_omega} zero channels for any n <= 1e5")
P25 = primes_up_to(200)[:25]
witness_zero = [p for p in P25 if p % 4 == 3]
bound = prod(witness_zero)
print(f"  witness tuple (0 at p=3 mod 4, 1 elsewhere): at rung 25 its")
print(f"  co-support is already {len(witness_zero)} channels; a matching integer")
print(f"  would be a nonzero multiple of {bound}")
print(f"  (> 10^{len(str(bound)) - 1}) -- the bound grows without limit: no integer matches.")
assert len(witness_zero) >= 12 and bound > 10**15
# (e) Char 0, and the sieve line: n*1 = 0 iff n = 0 (injectivity);
# 2 is a zero divisor (zero at channel 2); the only integers that are
# UNITS of the limit are +1 and -1 (every |n| >= 2 has a zero channel).
for n in range(2, LIM + 1):
    assert spf[n] <= n and n % spf[n] == 0
print("  units of the limit among integers: {+1, -1} only (n <= 1e5):")
print("  the FULL sieve's only integer survivors -- yet U(Pi F_p) is")
print("  uncountable. Char 0; every prime is a zero divisor.")

# ----------------------------------------------------------------------
section("III. BLUEPRINT PROPERTIES UNDER THE LIMIT")
# ----------------------------------------------------------------------
# STABLE: fields (definitional), meadow (coordinatewise), idempotents
# (all 0/1 tuples -- the lattice completes to P(Primes)).
R = RAD_RING
for _ in range(2000):
    a = tuple(random.randrange(p) for p in R.primes)
    inv = tuple(pow(r, p - 2, p) if r else 0 for r, p in zip(a, R.primes))
    aia = tuple((x * y % p) * x % p for x, y, p in zip(a, inv, R.primes))
    ii = tuple(pow(r, p - 2, p) if r else 0 for r, p in zip(inv, R.primes))
    assert aia == a and ii == a
print("  meadow: a.a'.a = a and a'' = a, coordinatewise -- no size, no")
print("  exponent, survives any product (von Neumann regular, classical)")
idem = [x for x in range(2310) if x * x % 2310 == x]
assert len(idem) == 2**5
assert all(all(r in (0, 1) for r in encode(x, thin_ring(5))) for x in idem)
print("  idempotents = 0/1 tuples (exhaustive k=5): in the limit, ALL")
print("  0/1 patterns -- the lattice completes to the power set P(Primes)")
# DIES: lambda. Any fixed exponent L fails at every channel p > L+1
# ((p-1) | L impossible), and at non-transparent smaller channels too.
for L in (240, 720, 55440):
    bound = max(1200, L + 1000)
    band = primes_up_to(bound)
    fails = []
    for p in band:
        if L % (p - 1) != 0:
            g = next(g for g in range(2, p)
                     if all(pow(g, (p - 1) // q, p) != 1
                            for q in factorize(p - 1)))
            assert pow(g, L + 1, p) != g
            fails.append(p)
    above = [p for p in band if p > L + 1]
    assert above and all(p in set(fails) for p in above)
    print(f"  lambda candidate {L}: a^(L+1) = a fails at {len(fails)} channels")
    print(f"    p <= {bound} (incl. ALL {len(above)} channels p > {L + 1})")
lams = [carmichael_lambda(thin_ring(k).N) for k in range(2, 13)]
assert all(l2 >= l1 for l1, l2 in zip(lams, lams[1:]))
assert all(l >= p - 1 for l, p in zip(lams, thin_ring(12).primes[1:]))
print("  lambda_k unbounded (lambda_k >= p_k - 1): no global exponent --")
print("  Clifford identity, collapse x^lambda, meadow FORMULA a^(lambda-1)")
print("  are all finite-rung artifacts; the OPERATIONS survive channelwise")
# SPLITS: the P38 criterion. Per channel, the unique reduced polynomial
# representing the inverse function has degree exactly p-2 (p odd), so
# no single polynomial of any degree d serves all channels p > d+2:
# in the limit, channel-local = compatible STRICTLY CONTAINS polynomial.
for p in [q for q in primes_up_to(32) if q > 2]:
    coeffs = [0] * p
    for a in range(p):
        fa = pow(a, p - 2, p) if a else 0
        num, den = [1], 1               # prod_{b != a} (x - b)
        for b in range(p):
            if b == a:
                continue
            num = [((num[i] if i < len(num) else 0) * (-b)
                    + (num[i - 1] if i >= 1 else 0)) % p
                   for i in range(len(num) + 1)]
            den = den * (a - b) % p
        scale = fa * pow(den, p - 2, p) % p
        for i, c in enumerate(num):
            coeffs[i] = (coeffs[i] + scale * c) % p
    deg = max(i for i, c in enumerate(coeffs) if c != 0)
    assert deg == p - 2
    for a in range(p):
        v = sum(c * pow(a, i, p) for i, c in enumerate(coeffs)) % p
        assert v == (pow(a, p - 2, p) if a else 0)
print("  pseudo-inverse interpolant has degree EXACTLY p-2 at every odd")
print("  channel p <= 31: minimal degree is unbounded across channels,")
print("  so no global polynomial -- the P38 equivalence (local =")
print("  compatible = polynomial) is a finite-rung statement; the limit")
print("  keeps local = compatible and drops polynomial to a proper subclass")
# DIES WITH THE HEIGHT: ECC. Below the cut (x < 210 = min 4-modulus
# product) any 4 of 7 channels determine x; above it, collisions.
ok = 0
for x in range(210):
    t = encode(x, R)
    for chs in combinations(range(7), 4):
        m = prod(R.moduli[i] for i in chs)
        assert x < m                    # 210 = the MIN 4-modulus product
        assert decode_partial(t, R, chs) == x
        ok += 1
assert ok == 210 * 35
t0, t1 = encode(0, R), encode(210, R)
assert t0[:4] == t1[:4] and t0 != t1
n_coll = R.N // 210
print(f"  height cut: all 210 x 35 erasure decodes exact below 210;")
print(f"  above it x=0 and x=210 collide on channels (2,3,5,7) --")
print(f"  {n_coll} elements share each 4-residue class. No archimedean")
print(f"  place in the limit => no cut => no code: ECC was a property of")
print(f"  the INTEGER POINTS under a height bound, not of the product ring")
print("  torus: the limit's native topology is profinite (a Cantor set);")
print("  the T^infinity dress stays an optional archimedean re-import")

# ----------------------------------------------------------------------
section("IV. THE NEIGHBORS, PLACED EXACTLY")
# ----------------------------------------------------------------------
# (a) Z-hat: the all-moduli (unbounded-fattening) limit. Pi F_p =
# Z-hat/J(Z-hat) -- finite shadow: every fat ring, bounded Pareto
# included, reduces mod its Jacobson radical to its thin rung.
fat_cases = [prod(q * q for q in thin_ring(k).primes) for k in range(2, 6)]
fat_cases.append(214414200)            # the Pareto fat ring (fat era, archived)
for m in fat_cases:
    radm = prod(factorize(m))
    J = list(range(0, m, radm))         # = rad(m) * Z/m, the radical
    assert len(J) == m // radm
    js = J if len(J) <= 64 else random.sample(J, 64)
    for j in js:                        # the radical is nilpotent here
        assert pow(j, 4, m) == 0        # max exponent in any fat case = 3
    sample = J if len(J) <= 500 else random.sample(J, 500)
    for j in sample:                    # Jacobson: 1 + J consists of units
        assert math.gcd(1 + j, m) == 1
    # quotient map x -> x mod radm is a ring surjection with kernel J
    for _ in range(200):
        a, b = random.randrange(m), random.randrange(m)
        assert (a * b) % radm == ((a % radm) * (b % radm)) % radm
        assert (a + b) % radm == ((a % radm) + (b % radm)) % radm
    print(f"  Z/{m} mod J (|J| = {m // radm}) = Z/{radm} (thin)")
print("  => thin limit = all-moduli limit / radical: Pi F_p = Z-hat/J(Z-hat);")
print("  thin-vs-fat IS strip-the-radical-or-not (J(Pi R_i) = Pi J(R_i))")
# (b) No adelic restricted product: F_p has no proper unital subring
# (generated by 1), so the only restrictions are {0} (giving the ideal
# Sum F_p, finite support, meets Z only at 0) and F_p^* (giving the
# finite-co-support locus -- NOT additively closed):
for p in primes_up_to(50):
    sub = {1}
    while True:
        new = sub | {(a + 1) % p for a in sub}
        if new == sub:
            break
        sub = new
    assert sub == set(range(p))
print("  F_p has no proper unital subring (verified p < 50): nothing to")
print("  restrict against -- the adelic move (restrict by Z_p) is fattening")
k = 12
ps12 = thin_ring(k).primes
x = tuple(1 for _ in ps12)                       # full support
A = set(ps12[::2])                               # kill half the channels
y = tuple(p - 1 if p in A else 1 for p in ps12)  # full support
s = tuple((a + b) % p for a, b, p in zip(x, y, ps12))
assert all(v != 0 for v in x) and all(v != 0 for v in y)
assert sum(1 for v in s if v == 0) == len(A) and any(v != 0 for v in s)
print(f"  finite shadow at k=12: two full-support tuples sum to a tuple")
print(f"  with {len(A)} zero channels -- finite-co-support is multiplicative,")
print(f"  not additive: no ring sits between Sum F_p and Pi F_p this way;")
print(f"  Z \\ {{0}} lands inside this non-ring locus (a tiny part of it)")
# (c) Spec at finite rungs = the channel set. Every ideal of Z/N is
# dZ/N for d | N; dZ/N is maximal iff the quotient Z/d is a field iff
# d is prime. Verify by direct containment among the ideals.
for k in range(2, 6):
    N = thin_ring(k).N
    divisors = [d for d in range(2, N + 1) if N % d == 0]
    maximal = [d for d in divisors
               if not any(e != d and d % e == 0 for e in divisors)]
    assert sorted(maximal) == sorted(thin_ring(k).primes)
print("  Spec(rung k) = exactly the k channels (k <= 5). In the limit,")
print("  Spec(Pi F_p) = beta(Primes): the channel set COMPACTIFIES; the")
print("  boundary points have residue fields Pi F_p / U -- Ax's")
print("  pseudo-finite fields, characteristic 0 (classical; choice-")
print("  dependent, named not worn)")

# ----------------------------------------------------------------------
section("V. THE MEASURE READ: WHERE Z SITS")
# ----------------------------------------------------------------------
# Haar on the compact group Pi F_p = product of uniform measures.
ps = primes_up_to(105000)
assert len(ps) >= 10000
ps = ps[:10000]
dens, s_inv = 1.0, 0.0
checkpoints = {100, 1000, 10000}
print("       k      p_k     unit density    e^-gamma/ln p_k    ratio")
for i, p in enumerate(ps, 1):
    dens *= 1 - 1 / p
    s_inv += 1 / p
    if i in checkpoints:
        mert = math.exp(-GAMMA) / math.log(p)
        print(f"  {i:6d}  {p:7d}    {dens:.6f}        {mert:.6f}       "
              f"{dens / mert:.4f}")
        if i == 10000:
            assert abs(dens / mert - 1) < 0.02
            assert abs(s_inv - (math.log(math.log(p)) + MERTENS_M)) < 0.01
print("  unit density -> 0 at the Mertens rate (ratio -> 1.00); expected")
print(f"  zero-channel count sum 1/p = {s_inv:.4f} = ln ln p_k + M: diverges")
# Borel-Cantelli finite shadow: P[co-support <= 2] under product Haar,
# exact DP over the first k channels -- monotone to 0.
def cosupport_tail(kk, m):
    probs = [0.0] * (m + 2)             # P[#zeros = j], overflow bucket
    probs[0] = 1.0
    for p in primes_up_to(2000)[:kk]:
        q = 1 / p
        new = [0.0] * (m + 2)
        for j, pr in enumerate(probs):
            if j <= m:
                new[min(j + 1, m + 1)] += pr * q
                new[j] += pr * (1 - q)
            else:
                new[j] += pr
        probs = new
    return sum(probs[:m + 1])
tail = [cosupport_tail(kk, 2) for kk in (10, 50, 100, 200)]
assert all(a > b for a, b in zip(tail, tail[1:]))
print("  P[<= 2 zero channels] at k = 10, 50, 100, 200:")
print("    " + ", ".join(f"{t:.4f}" for t in tail) + "  (monotone down;")
print("  Borel-Cantelli: sum 1/p = infinity + independence => Haar-a.e.")
print("  element has INFINITELY many zero channels. Every nonzero integer")
print("  has finitely many: Z lives inside a null set, and finite")
print("  co-support -- the certificate of the deleted place -- is exactly")
print("  its null-set membership card)")

# ----------------------------------------------------------------------
section("FINDINGS (tier-labeled)")
# ----------------------------------------------------------------------
print("""
1. THE LIMIT IS THE FULL PRODUCT (rule + classical). The tower's
   transition maps are channel-forgetting projections (exhaustive
   k <= 5, sampled k = 6, 7), so lim Z/p_k# = Pi_p F_p over ALL
   primes -- the full product of residue fields. v_p = 1 at every
   rung: no Z_p forms. The all-moduli system lim Z/n (fattening
   without bound) converges to Z-hat = Pi Z_p instead, and Pi F_p =
   Z-hat/J(Z-hat): the thin limit is that fat limit's semisimple
   quotient -- and mod-the-radical recovers thin at every BOUNDED
   fattening level too (verified at squared rungs and at the Pareto
   fat ring Z/214414200 -> Z/510510). Thin-vs-fat =
   strip-the-radical-or-not, per place.

2. THE BIJECTION SPLITS (rule + classical). Per rung, Z/N <-> tuples
   is a bijection. In the limit it splits: Z -> Pi F_p is INJECTIVE --
   certified only by the deleted place (every finite window set S has
   kernel prod(S); the certificate is the size bound p > |n|) -- and
   DENSE (= finite CRT, solvability of any finite condition set), but
   never surjective: nonzero integers have finite co-support, and a
   coherent tuple prescribing zeros along p = 3 mod 4 outruns every
   integer. Mirror refinement: F_2[x]'s certificate is deg, the
   deleted place at infinity, NON-archimedean -- deleted-ness is the
   mechanism; archimedean is which place Q happens to delete
   (Ostrowski). Decode-uniqueness was the height cut; gone.

3. THE BLUEPRINT SPLITS THREE WAYS (rule). STABLE: all-field
   channels (definitional), meadow (coordinatewise von Neumann
   regularity -- products of fields), idempotents (the lattice
   completes from the finite Boolean algebra 2^k to the full power
   set P(Primes)). DIES: lambda -- every fixed exponent L fails at
   all channels p > L+1, so the Clifford identity, the P37 collapse
   measurement x^lambda, and the one-polynomial meadow formula
   a^(lambda-1) are finite-rung artifacts (the operations survive
   channel-locally); ECC -- no archimedean place, no height cut, no
   code: redundancy was a property of the integer points under a
   bound (P45 audit reading, made exact). SPLITS: the P38 criterion
   -- in the limit channel-local = compatible STRICTLY CONTAINS
   polynomial (pseudo-inverse witness: minimal degree p-2 per
   channel, unbounded). Torus: native limit topology is profinite
   (Cantor set); T^infinity remains an optional re-dress.

4. NO RING BETWEEN THE SUM AND THE PRODUCT (rule + classical). F_p
   has no proper unital subring, so the adelic restricted-product
   construction has nothing to restrict against at residue-field
   level: restrict by {0} -> Sum F_p (the finite-support ideal,
   meeting Z only at 0); restrict by units -> the finite-co-support
   locus, multiplicatively closed but not additively (two
   full-support tuples sum to co-support 6 at k = 12). Z \\ {0} lands
   inside that non-ring locus -- a tiny part of it. Restricting by
   Z_p -- the adeles' move -- is fattening, which the thin tower
   never does.

5. BOUNDARY CHANNELS (classical contact, named not worn).
   Spec(Pi F_p) = beta(Primes), the Stone-Cech compactification of
   the channel set; principal points = our channels (rung k's Spec
   has exactly k points, verified k <= 5); non-principal points have residue
   fields Pi F_p / U = Ax's pseudo-finite fields of characteristic 0.
   The ultraproduct is thus literally a residue field of the limit
   object at a boundary channel -- placed, choice-dependent, nothing
   computable, left alone.

6. Z IS A NULL-SET ANOMALY (rule + classical). Unit density falls at
   the Mertens rate e^(-gamma)/ln p_k (ratio 1.00 at 10^4 channels):
   the full sieve survives measure zero, and its only integer
   survivors are +1 and -1. Borel-Cantelli (sum 1/p diverges,
   coordinates independent under Haar): almost every element has
   infinitely many zero channels, while every nonzero integer has
   finitely many. Z sits inside a Haar-null set, and its membership
   certificate -- finite co-support -- is the deleted place's
   certificate again, in measure language.
""")
print("explore_limit_object.py: ALL CHECKS PASSED")
