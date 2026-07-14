"""
NIMBERS AND THE CHAR-2 MIRRORS.

Three walls have been charted from inside the primorial tower: size (the
archimedean place, an information obstruction), Zech (within-channel
structure), and the super-log (existence). This script steps OUTSIDE and
builds the two characteristic-2 constructions next door: the VERTICAL
nim-field tower (one prime, quadratic extensions stacked upward) and the
HORIZONTAL polynomial mirror F_2[x]/f (the F_q[x] analogue of the
primorial ring). The questions: what plays "channel" in the
vertical tower, and does the size wall soften in the mirror?

Survey anchors (standard material, named so nothing here poses as new):
Conway, ONAG 1976 (nim-addition = XOR; nim-multiplication makes the
ordinals a field of characteristic 2; each interval [0, 2^(2^n)) is the
field F_{2^(2^n)}; the union over n is the quadratic closure of F_2;
for a Fermat 2-power D = 2^(2^k): D ox D = (3/2)D and D ox x = D*x for
x < D), Lenstra "Nim multiplication" 1978 (effective algorithms, the
tower's structure), the telescoping identity 2^(2^n) - 1 =
prod_{k<n} F_k with F_k = 2^(2^k) + 1 the Fermat numbers (elementary;
Fermat numbers are pairwise coprime -- Goldbach; F_0..F_4 prime, F_5 =
641 * 6700417 -- Euler; whether ALL Fermat numbers are squarefree is
OPEN), Gauss (x^(2^d) - x = product of all monic irreducibles over F_2
of degree dividing d; exact irreducible counts by Mobius inversion --
the polynomial prime number theorem is EXACT, and the zeta of F_2[x]
is rational: Z(t) = 1/(1 - 2t)), the function-field/number-field
dictionary (Artin-Whaples, Weil: every place of F_2(x) is
NON-archimedean -- the degree valuation is the place at infinity, with
residue field F_2, the same KIND of place as the finite ones; there is
no archimedean place to discard), Artin-Schreier (a field admits an
order iff it is formally real, i.e. -1 is not a sum of squares; in
characteristic 2, -1 = 1^2 -- no char-2 field is orderable),
Wieferich (squarefreeness of 2^p - 1 for prime p is tied to Wieferich
primes and OPEN in general; composite exponents fail concretely:
2^6 - 1 = 63 = 3^2 * 7), and carry-free GF(2^n) hardware (LFSR/XOR
multipliers; mod-Mersenne and mod-Fermat reduction as shift-add --
the two families named as designed-tower hardware knobs).
Carried over: Pohlig-Hellman, Pratt trees (Ford-Konyagin-Luca),
iterated lambda (Martin-Pomerance, Harland), the three existence grades.

Findings preview (full statements at the bottom):
  1. WHAT PLAYS CHANNEL: nothing, at ring level -- every nim-rung is a
     FIELD (idempotents {0,1}, no CRT split): the vertical move is
     extension, not product. The channels live ONE LEVEL DOWN: the unit
     group is cyclic of order 2^(2^n) - 1 = prod F_k, so the INDEX RING
     of the nim-rung is a squarefree all-field designed tower --
     on the five Fermat PRIMES for n <= 5, where at n = 5 it is exactly
     the machine-word specimen Z/(2^32 - 1) = 3*5*17*257*65537; at
     n = 6 on the prime factors of F_0..F_5 (still squarefree); beyond,
     it rides the OPEN all-Fermat-squarefree question.
  2. NAPIER INVERSION: the vertical tower has the PERFECT second log
     (cyclic units: one discrete log, no CRT detour -- what the
     primorial tower lacks at every rung k >= 3) and the maximally
     blocked third log (every Fermat channel >= 17 has 8 | p-1:
     grade B fails; only 3 and 5 are grade A). Pratt trees of Fermat
     primes are PATHS; the lambda-chain decays arithmetically (2 bits
     per step): height 10 at 2^32 - 1 vs 4 at RAD, so the 32-bit nim
     word's tetration depth is bounded by 10 (sampled bases stabilize
     by depth 9). Chain height is a design knob.
  3. THE MIRROR PRIMORIAL: F_2[x]/f (f squarefree) carries the full
     blueprint -- CRT bijection, 2^k idempotents, Clifford
     a^(lambda+1) = a, meadow inverse, phi = prod(2^e_i - 1). Canonical
     rungs f = x^(2^d) + x have channels <-> Frobenius orbits of
     F_{2^d}-points, lambda = 2^d - 1 (MERSENNE by construction), and
     collapse = Frobenius^d = d squarings. The two char-2 constructions
     realize the two hardware families as index rings: vertical/nim
     -> one Fermat tower, horizontal/mirror -> per-channel Mersenne
     rings (the rung-wide product is not a single Z/M).
  4. THE CRITERION TRANSFERS: channel-local = compatible = polynomial
     on squarefree F_2[x]/f (exhaustive at the 4- and 8-element rings;
     constructive Lagrange + CRT glue), and thin-only again
     (F_2[x]/x^2 has polynomial strictly inside channel-local). The
     locality criterion never used the integers.
  5. THE SIZE WALL SOFTENS EXACTLY IN ITS ARCHIMEDEAN PART: deg is
     incompatible (witnesses at every channel -- the information core
     of the wall is unchanged, and the recoding argument transfers
     verbatim). But the mirror has no archimedean place: sign/order is
     VACATED (Artin-Schreier), multiplication is carry-free
     (deg(ab) = deg a + deg b exactly), and the partial-fraction
     escape becomes EXACT-OR-FLAGGED -- t-term truncation either reads
     deg exactly or returns a self-flagging zero prefix; zero silent
     failures, exhaustively (vs Z's silent wraparound mode). Carries
     are the archimedean place's shadow in positional digits.
  6. THE MIRROR'S PRIME SIDE IS CLOSED-FORM: the Euler product over
     irreducibles equals 1/(1-2t) coefficientwise -- the exploratory
     questions trivialize in the mirror; it feeds engineering applications
     only (the designed-tower honest limit, reconfirmed).

Runs exhaustively at F_16 / F_256 / the 1024-element mirror ring, with
order-certified generators at F_{2^16} and F_{2^32} and a Mersenne
squarefree census e <= 40.  ~2 s, ~26 MB.
"""

import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import is_prime, factorize, primes_up_to, carmichael_lambda, lcm_list

random.seed(42)

def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)

# ----------------------------------------------------------------------
# Nim arithmetic (Conway ONAG; algorithm shape after Lenstra 1978).
# Nimbers in [0, 2^(2^n)) form the field F_{2^(2^n)}; addition is XOR.
# Recursion: split at the largest Fermat 2-power F = 2^(2^k) <= a
# (then a < F^2); for x < F, F ox x = F*x, and F ox F = F + F/2.
# ----------------------------------------------------------------------
NIM_MEMO = {}

def nim_mul(a, b):
    if a < b:
        a, b = b, a
    if b < 2:
        return a * b
    key = (a, b)
    r = NIM_MEMO.get(key)
    if r is not None:
        return r
    F = 2
    while F * F <= a:
        F *= F
    ah, al = divmod(a, F)
    if b < F:
        r = nim_mul(ah, b) * F ^ nim_mul(al, b)
    else:
        bh, bl = divmod(b, F)
        hi = nim_mul(ah, bh)
        cross = nim_mul(ah, bl) ^ nim_mul(al, bh)
        r = (hi ^ cross) * F ^ nim_mul(hi, F >> 1) ^ nim_mul(al, bl)
    NIM_MEMO[key] = r
    return r

def nim_pow(x, e):
    r = 1
    while e:
        if e & 1:
            r = nim_mul(r, x)
        x = nim_mul(x, x)
        e >>= 1
    return r

# ----------------------------------------------------------------------
# F_2[x] arithmetic: integers as polynomials (bit i = coefficient of x^i).
# Addition/subtraction = XOR (char 2). deg 0 reads as -1 (= -infinity).
# ----------------------------------------------------------------------
def pdeg(a):
    return a.bit_length() - 1

def pmul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r

def pdivmod(a, b):
    db = pdeg(b)
    q = 0
    da = pdeg(a)
    while da >= db:
        q ^= 1 << (da - db)
        a ^= b << (da - db)
        da = pdeg(a)
    return q, a

def pmod(a, b):
    return pdivmod(a, b)[1]

def pgcd(a, b):
    while b:
        a, b = b, pmod(a, b)
    return a

def pegcd(a, b):
    s0, s1, t0, t1 = 1, 0, 0, 1
    while b:
        q, r = pdivmod(a, b)
        a, b = b, r
        s0, s1 = s1, s0 ^ pmul(q, s1)
        t0, t1 = t1, t0 ^ pmul(q, t1)
    return a, s0, t0

def pinvmod(a, m):
    g, s, _ = pegcd(pmod(a, m), m)
    assert g == 1
    return pmod(s, m)

def pmulmod(a, b, m):
    return pmod(pmul(a, b), m)

def ppow(a, e, m):
    r = 1
    a = pmod(a, m)
    while e:
        if e & 1:
            r = pmulmod(r, a, m)
        a = pmulmod(a, a, m)
        e >>= 1
    return r

def pcrt(residues, moduli):
    x, m = 0, 1
    for r, f in zip(residues, moduli):
        g, s, _ = pegcd(m, f)
        assert g == 1
        x ^= pmul(m, pmulmod(s, pmod(r ^ x, f), f))
        m = pmul(m, f)
        x = pmod(x, m)
    return x

def irreducibles_up_to(maxdeg):
    irr = []
    for f in range(2, 1 << (maxdeg + 1)):
        d = pdeg(f)
        if all(pmod(f, g) != 0 for g in irr if pdeg(g) <= d // 2):
            irr.append(f)
    return irr

SMALL_PRIMES = primes_up_to(1 << 20)

def factorize_fast(n):
    """Trial division over a prime list (adequate for n <= 2^40)."""
    f = {}
    for p in SMALL_PRIMES:
        if p * p > n:
            break
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

# ----------------------------------------------------------------------
section("I. NIM ARITHMETIC: THE VERTICAL TOWER")
# ----------------------------------------------------------------------
# Fermat 2-power rules (Conway) -- the implementation's contract:
for D in (2, 4, 16, 256, 65536, 1 << 32):
    assert nim_mul(D, D) == D ^ (D >> 1)          # D ox D = (3/2) D
for D in (4, 16, 256):
    for x in range(D):
        assert nim_mul(D, x) == D * x             # D ox x = D x, x < D
for D in (65536, 1 << 32):
    for x in random.sample(range(D), 200):
        assert nim_mul(D, x) == D * x
print("Fermat 2-power rules hold: D ox D = 3D/2 (D up to 2^32),")
print("                           D ox x = D*x for x < D (exh. to 256)")

# F_16 = nimbers [0, 16): full field axioms, exhaustively.
T16 = [[nim_mul(a, b) for b in range(16)] for a in range(16)]
for a in range(16):
    for b in range(16):
        assert T16[a][b] < 16                     # closure
        assert T16[a][b] == T16[b][a]             # commutativity
        for c in range(16):
            assert T16[a][T16[b][c]] == T16[T16[a][b]][c]      # assoc
            assert T16[a][b ^ c] == T16[a][b] ^ T16[a][c]      # distrib
assert all(any(T16[a][b] == 1 for b in range(16)) for a in range(1, 16))
assert all(T16[a][b] < 4 for a in range(4) for b in range(4))  # F_4 subfield
print("F_16 verified exhaustively: closure, comm, assoc, distrib,")
print("                            inverses; [0,4) is the F_4 subfield")

# Ground truth: the recursion above could implement SOME field on XOR
# and still pass the axiom checks. Pin it to Conway's game definition:
# a ox b = mex{ a' ox b  XOR  a ox b'  XOR  a' ox b' : a' < a, b' < b }.
MEX_MEMO = {}

def nim_mul_mex(a, b):
    if a < b:
        a, b = b, a
    key = (a, b)
    if key in MEX_MEMO:
        return MEX_MEMO[key]
    excl = {nim_mul_mex(i, b) ^ nim_mul_mex(a, j) ^ nim_mul_mex(i, j)
            for i in range(a) for j in range(b)}
    r = 0
    while r in excl:
        r += 1
    MEX_MEMO[key] = r
    return r

for a in range(16):
    for b in range(16):
        assert nim_mul_mex(a, b) == T16[a][b]
print("ground truth: the recursion matches Conway's mex game definition")
print("              on all 256 pairs of [0,16)")

def t16_order(a):
    o, x = 1, a
    while x != 1:
        x = T16[x][a]
        o += 1
    return o

g16 = min(a for a in range(2, 16) if t16_order(a) == 15)
print(f"smallest generator of F_16^* : {g16} (order 15)")

# F_256: table; field axioms via structure (cheap but exhaustive).
T = [[nim_mul(a, b) for b in range(256)] for a in range(256)]
assert all(T[a][b] < 256 for a in range(256) for b in range(256))
assert all(T[a][b] == T[b][a] for a in range(256) for b in range(256))
assert all(T[0][b] == 0 for b in range(256))
# Distributivity is exhaustive via linearity: T[a][b^c] = T[a][b]^T[a][c]
# for ALL b, c  <=>  row a is F_2-linear  <=>  every value is the XOR of
# the basis images (char 2: overlapping terms cancel pairwise).
for a in range(256):
    Ta = T[a]
    basis = [Ta[1 << i] for i in range(8)]
    for b in range(256):
        v, bb, i = 0, b, 0
        while bb:
            if bb & 1:
                v ^= basis[i]
            bb >>= 1
            i += 1
        assert Ta[b] == v
print("F_256: closure, commutativity, zero row exhaustive;")
print("       distributivity exhaustive via row-linearity (mul-by-a is")
print("       F_2-linear -- the field is an F_2-algebra)")

def t256_powers(g):
    xs, x = [1], g
    while x != 1:
        xs.append(x)
        x = T[x][g]
    return xs

g256 = next(a for a in range(2, 256) if len(t256_powers(a)) == 255)
exp = t256_powers(g256)
assert len(set(exp)) == 255
# Index isomorphism, exhaustive on all unit pairs: this certifies
# associativity and inverses structurally (units ~ Z/255 under +).
for i in range(255):
    for j in range(255):
        assert T[exp[i]][exp[j]] == exp[(i + j) % 255]
print(f"smallest generator of F_256^*: {g256} (order 255); index iso")
print("       U(F_256) ~ Z/255 verified exhaustively (255^2 pairs) --")
print("       assoc + inverses follow structurally")
assert g16 >= 4 and g256 >= 16   # generators lie OUTSIDE the next subfield down

# Frobenius orbits on F_256: |orbit| in {1,2,4,8}; the squaring map is
# the tower's symmetry (Gal(F_{2^(2^n)}/F_2) = Z/2^n; the inverse limit
# over the whole vertical tower is Z_2 -- the SAME 2-adic object that
# walls grade B. Classical; verified here at n = 3.)
seen, orbit_count = set(), {}
for a in range(256):
    if a in seen:
        continue
    orb, x = [], a
    while x not in orb:
        orb.append(x)
        x = T[x][x]
    for y in orb:
        seen.add(y)
    orbit_count[len(orb)] = orbit_count.get(len(orb), 0) + 1
assert orbit_count == {1: 2, 2: 1, 4: 3, 8: 30}
print("Frobenius orbits on F_256: {1: 2, 2: 1, 4: 3, 8: 30} -- the")
print("       vertical symmetry group is Z/2^n per rung, Z_2 in the limit")

# No CRT split anywhere on the vertical tower: each rung is a field,
# so its only idempotents are 0 and 1 (verified exhaustively at F_256).
assert [a for a in range(256) if T[a][a] == a] == [0, 1]
print("idempotents of F_256: {0, 1} -- no CRT split at ring level;")
print("       the vertical move is extension, not product")

# ----------------------------------------------------------------------
section("II. CHANNELS ONE LEVEL DOWN: INDEX RINGS ARE FERMAT TOWERS")
# ----------------------------------------------------------------------
# Telescoping (elementary): 2^(2^n) - 1 = prod_{k<n} F_k.
FERMAT = [2 ** (2 ** k) + 1 for k in range(6)]      # F_0..F_5
for n in range(1, 7):
    assert 2 ** (2 ** n) - 1 == math.prod(FERMAT[:n])
assert all(is_prime(F) for F in FERMAT[:5])
assert FERMAT[5] == 641 * 6700417 and is_prime(641) and is_prime(6700417)
print("2^(2^n) - 1 = F_0 * ... * F_{n-1} verified n <= 6;")
print("F_0..F_4 prime (Euler: F_5 = 641 * 6700417)")

# The index ring of the nim-rung F_{2^(2^n)} is Z/(2^(2^n) - 1):
# squarefree, all prime-field channels for n <= 5 -- a DESIGNED
# TOWER on the Fermat primes. At n = 5 it is the machine-word specimen.
M16, M32 = 65535, (1 << 32) - 1
assert M16 == 3 * 5 * 17 * 257 and M32 == 3 * 5 * 17 * 257 * 65537

def certify_generator(x, group_order, prime_facs):
    return (nim_pow(x, group_order) == 1 and
            all(nim_pow(x, group_order // p) != 1 for p in prime_facs))

# Elements below 2^(2^(n-1)) lie in the next subfield down (Conway), so
# scanning upward from there yields the SMALLEST primitive element.
g16b = next(x for x in range(256, 65536)
            if certify_generator(x, M16, [3, 5, 17, 257]))
g32 = next(x for x in range(65536, 1 << 32)
           if certify_generator(x, M32, [3, 5, 17, 257, 65537]))
print(f"smallest generators: F_2^16: {g16b} (order 65535),")
print(f"                     F_2^32: {g32} (order 4294967295) --")
print("                     certified by prime-cofactor powering")

for n, (m, lam_expected) in enumerate([(15, 4), (255, 16), (M16, 256),
                                       (M32, 65536)], start=2):
    assert carmichael_lambda(m) == lam_expected == 2 ** (2 ** (n - 1))
print("index-ring lambdas: 4, 16, 256, 65536 -- always a 2-power")
print("  (the cheap-collapse knob: collapse = 2^(n-1) squarings);")
print("  the n = 5 index ring IS the machine-word tower Z/(2^32-1)")

# n = 6: F_5 composite. The index ring Z/(2^64-1) is STILL squarefree
# all-field (7 distinct prime channels) but the rung<->Fermat-number
# alignment breaks (one vertical rung adds two channels), and lambda is
# no longer a 2-power -- the cheap-collapse knob dies with primality.
M64 = (1 << 64) - 1
assert M64 == 3 * 5 * 17 * 257 * 65537 * 641 * 6700417
lam64 = carmichael_lambda(M64)
assert lam64 == lcm_list([2, 4, 16, 256, 65536, 640, 6700416])
assert lam64 & (lam64 - 1) != 0
print(f"n = 6: Z/(2^64-1) has 7 prime channels (still squarefree) but")
print(f"       lambda = {lam64} is not a 2-power: the cheap-collapse")
print("       knob = Fermat primality. All-Fermat-squarefree is OPEN.")

# Third-log grades on the Fermat channels: p - 1 = 2^(2^k), so
# Z/(p-1) is cyclic iff 2^(2^k) in {2, 4} (k <= 1), and 8 | p-1 for
# every k >= 2: channels 17, 257, 65537 fail grade B 2-adically -- the
# vertical tower is the WORST CASE of the census, by construction.
def euler_phi(m):
    r = 1
    for p, a in factorize(m).items():
        r *= (p - 1) * p ** (a - 1)
    return r

for p in (3, 5):
    assert carmichael_lambda(p - 1) == euler_phi(p - 1)   # cyclic: grade A
for p in (17, 257, 65537):
    assert (p - 1) % 8 == 0                               # grade B fails
print("third-log grades: 3, 5 grade A; 17, 257, 65537 fail grade B")
print("  (8 | p-1, the 2-adic obstruction -- maximal by construction)")

# Pratt trees of Fermat primes are PATHS: p - 1 has the single prime 2.
assert all(list(factorize(F - 1).keys()) == [2] for F in FERMAT[:5])
print("Pratt trees of Fermat primes: paths (single prime 2, no branching")
print("  -- vs the branching-random-walk trees of FKL on random primes)")

# The lambda-chain: arithmetic decay. lambda(2^k) = 2^(k-2) loses two
# bits per step, so the chain from 2^32 - 1 is LONG where RAD's crashes.
def lambda_chain(m):
    chain = [m]
    while chain[-1] > 1:
        chain.append(carmichael_lambda(chain[-1]))
    return chain

chain_rad = lambda_chain(510510)
chain_m32 = lambda_chain(M32)
assert chain_rad == [510510, 240, 4, 2, 1]
assert chain_m32 == [M32] + [2 ** e for e in (16, 14, 12, 10, 8, 6, 4, 2, 1, 0)]
H32 = len(chain_m32) - 1
print(f"lambda-chain of 2^32-1: height {H32} "
      f"(2^16 -> 2^14 -> ... -> 2 -> 1) vs RAD height 4")

# Tetration depth resolution (engine from explore_super_log.py,
# including the lift-validity assert: lambda(m) >= nu(m); m = 8 and 24
# are the only failing moduli and neither appears in these chains).
def exact_tower(x, h, max_bits=1 << 22):
    t = 1
    for _ in range(h):
        if x >= 2 and t > max_bits / math.log2(x):
            return None
        t = x ** t
    return t

def tower_mod(x, h, m):
    if m == 1:
        return 0
    if h == 0:
        return 1 % m
    t = exact_tower(x, h - 1, max_bits=64)
    if t is not None:
        return pow(x, t, m)
    lm = carmichael_lambda(m)
    assert lm >= max(factorize(m).values())     # lift validity (8, 24 fail)
    return pow(x, tower_mod(x, h - 1, lm) + lm, m)

checked = 0
for x in range(2, 11):
    for h in range(0, 6):
        t = exact_tower(x, h)
        if t is None:
            continue
        for m in (15, 255, M16, M32):
            assert tower_mod(x, h, m) == t % m
            checked += 1
print(f"tower_mod validated against exact integer towers: {checked} cases")

def stab_depth(x, m, hmax):
    vals = [tower_mod(x, h, m) for h in range(hmax + 1)]
    d = hmax
    while d > 0 and vals[d - 1] == vals[hmax]:
        d -= 1
    assert all(v == vals[hmax] for v in vals[d:])
    return d

depths = {x: stab_depth(x, M32, 14) for x in (2, 3, 5, 7, 11, 123456789)}
assert max(depths.values()) <= H32
print(f"tetration mod 2^32-1 stabilization depths: {depths}")
print(f"  chain height {H32} bounds the depth; sampled max = "
      f"{max(depths.values())}.")
print("  RAD (a ring 8400x smaller) has height 4: the lambda-chain")
print("  height -- tetration resolution -- is a DESIGN KNOB")

# ----------------------------------------------------------------------
section("III. THE MIRROR PRIMORIAL: F_2[x]/f AND MERSENNE INDEX RINGS")
# ----------------------------------------------------------------------
IRR = irreducibles_up_to(12)
by_deg = {}
for f in IRR:
    by_deg.setdefault(pdeg(f), []).append(f)

# Gauss's exact count: N_d = (1/d) sum_{e|d} mu(e) 2^(d/e).
def mobius(n):
    fs = factorize_fast(n)
    if any(a > 1 for a in fs.values()):
        return 0
    return -1 if len(fs) % 2 else 1

for d in range(1, 13):
    Nd = sum(mobius(e) * 2 ** (d // e) for e in range(1, d + 1)
             if d % e == 0) // d
    assert len(by_deg.get(d, [])) == Nd
print("irreducible census deg <= 12 matches the Gauss-Mobius formula --")
print("  the mirror's prime counting is EXACT (no PNT error term)")

# Rational zeta: prod over irreducibles of (1 - t^deg)^-1 = 1/(1-2t).
series = [1] + [0] * 12
for d in range(1, 13):
    for _ in by_deg.get(d, []):
        for j in range(d, 13):
            series[j] += series[j - d]
assert series == [2 ** n for n in range(13)]
print("Euler product over irreducibles = 1/(1-2t) verified to t^12 --")
print("  the sieve closes in closed form; the mirror's MAP side is")
print("  trivial (the limit reconfirmed: the mirrors feed engineering)")

# Canonical rungs: x^(2^d) + x = prod of irreducibles of degree | d.
for d in range(1, 5):
    prod = 1
    for f in IRR:
        if d % pdeg(f) == 0:
            prod = pmul(prod, f)
    assert prod == (1 << (1 << d)) ^ 2
print("x^(2^d) + x = prod of irreducibles with degree | d (d <= 4)")

# Channels <-> Frobenius orbits: at d = 3, the points of F_8 fall into
# orbits {0}, {1}, and two 3-orbits whose minimal polynomials are the
# two cubic irreducibles -- one channel per orbit.
F8MOD = 0b1011                                   # x^3 + x + 1
orbits, seen8 = [], set()
for a in range(8):
    if a in seen8:
        continue
    orb, x = [], a
    while x not in orb:
        orb.append(x)
        x = pmulmod(x, x, F8MOD)
    orbits.append(orb)
    seen8.update(orb)
minpolys = set()
for orb in orbits:
    mp = [1]                                     # poly in t, coeffs in F_8
    for root in orb:
        mp = [(mp[j - 1] if j else 0) ^ pmulmod(mp[j] if j < len(mp) else 0,
                                                root, F8MOD)
              for j in range(len(mp) + 1)]
    assert all(c in (0, 1) for c in mp)          # coefficients drop to F_2
    minpolys.add(sum(c << j for j, c in enumerate(mp)))
assert sorted(len(o) for o in orbits) == [1, 1, 3, 3]
assert minpolys == {0b10, 0b11, 0b1011, 0b1101}
print("d = 3 rung: channels are the Frobenius orbits of F_8 points")
print("  (orbit sizes 1,1,3,3 -> x, x+1, x^3+x+1, x^3+x^2+1)")

# Clifford identity on canonical rungs IS Frobenius^d: a^(2^d) = a, so
# lambda = 2^d - 1 -- MERSENNE BY CONSTRUCTION -- and the collapse
# costs d squarings (both knobs at once).
for d in (2, 3, 4):
    rung = (1 << (1 << d)) ^ 2
    lam = lcm_list([2 ** e - 1 for e in range(1, d + 1) if d % e == 0])
    assert lam == 2 ** d - 1
    for a in range(1 << (1 << d)):               # every ring element
        assert ppow(a, 2 ** d, rung) == a
print("canonical rungs d = 2,3,4: a^(2^d) = a for every element --")
print("  lambda = 2^d - 1 (Mersenne), collapse = d squarings (Frobenius)")

# Working ring W: the 'first five irreducibles' primorial, deg 10.
F5_IRR = IRR[:5]
assert F5_IRR == [0b10, 0b11, 0b111, 0b1011, 0b1101]
FW = 1
for f in F5_IRR:
    FW = pmul(FW, f)
assert pdeg(FW) == 10
W = 1 << 10
DEGS = [pdeg(f) for f in F5_IRR]                 # [1, 1, 2, 3, 3]
LAMW = lcm_list([2 ** e - 1 for e in DEGS])      # lcm(1,1,3,7,7) = 21
assert LAMW == 21

# CRT bijection, exhaustive.
for a in range(W):
    assert pcrt([pmod(a, f) for f in F5_IRR], F5_IRR) == a
# Blueprint: 2^5 idempotents; Clifford a^(lambda+1) = a; meadow inverse
# a* = a^(lambda-1) (a a* a = a and a* a a* = a*); phi = prod(2^e - 1).
idem = [a for a in range(W) if pmulmod(a, a, FW) == a]
assert len(idem) == 32
units = [a for a in range(W) if pgcd(a, FW) == 1]
assert len(units) == 147 == math.prod(2 ** e - 1 for e in DEGS)
for a in range(W):
    assert ppow(a, LAMW + 1, FW) == a
    astar = ppow(a, LAMW - 1, FW)
    assert pmulmod(pmulmod(a, astar, FW), a, FW) == a
    assert pmulmod(pmulmod(astar, a, FW), astar, FW) == astar

def unit_order(u):
    o, x = 1, u
    while x != 1:
        x = pmulmod(x, u, FW)
        o += 1
    return o

# lambda is TIGHT: every unit order divides 21 and 21 is attained
# (a^(lambda+1) = a alone only bounds the exponent).
orders = {unit_order(u) for u in units}
assert max(orders) == LAMW and all(LAMW % o == 0 for o in orders)
print(f"W = F_2[x]/(deg-10 squarefree f), 1024 elements: CRT bijection,")
print(f"  32 = 2^5 idempotents, a^22 = a (lambda = 21), meadow inverse")
print(f"  a^(lambda-1), phi = 147 = prod(2^e - 1): full blueprint, exhaustive")

# Index rings of the mirror channels are Z/(2^e - 1): MERSENNE towers.
# Designed (squarefree all-field) iff 2^e - 1 squarefree -- census:
nonsf = [e for e in range(2, 41)
         if any(a > 1 for a in factorize_fast(2 ** e - 1).values())]
gradeA = [e for e in range(2, 41)
          if len(factorize_fast(2 ** e - 1)) == 1]
assert nonsf[0] == 6                              # 63 = 3^2 * 7
assert all(not is_prime(e) for e in nonsf)        # prime e clean in range
assert all(is_prime(2 ** e - 1) for e in gradeA)  # no proper prime powers
print(f"Mersenne census e <= 40: 2^e - 1 non-squarefree at e = {nonsf}")
print("  (first failure 2^6-1 = 63 = 3^2*7; every prime e is clean in")
print("  range -- general squarefreeness OPEN, Wieferich-tied);")
print(f"  third-log grade A exactly at Mersenne-prime exponents {gradeA}")
print("  (no proper prime-power 2^e - 1 appears -- the Catalan route)")

# ----------------------------------------------------------------------
section("IV. THE LOCALITY CRITERION TRANSFERS")
# ----------------------------------------------------------------------
# The locality criterion (channel-local = compatible = polynomial on squarefree
# rings) never used the integers: Lagrange interpolation works over any
# finite field and coefficients CRT-glue degreewise. Verified here.

# 4-element ring F_2[x]/(x^2+x) = F_2 x F_2: all three classes, brute.
R4MOD, R4CH = 0b110, [0b10, 0b11]
compat4 = set()
for code in range(4 ** 4):
    f = [(code >> (2 * i)) & 3 for i in range(4)]
    ok = all(pmod(f[a] ^ f[b], c) == 0
             for c in R4CH for a in range(4) for b in range(4)
             if pmod(a ^ b, c) == 0)
    if ok:
        compat4.add(tuple(f))
local4 = set()
for g1 in range(4):
    for g2 in range(4):
        local4.add(tuple(pcrt([(g1 >> pmod(a, 2)) & 1,
                               (g2 >> pmod(a, 3)) & 1], R4CH)
                         for a in range(4)))
poly4 = set()
for code in range(4 ** 4):
    cs = [(code >> (2 * i)) & 3 for i in range(4)]
    vals = []
    for a in range(4):
        v = 0
        for c in reversed(cs):
            v = pmulmod(v, a, R4MOD) ^ c
        vals.append(v)
    poly4.add(tuple(vals))
assert compat4 == local4 == poly4 and len(compat4) == 16
print("F_2 x F_2 (4 elements): compatible = local = polynomial = 16,")
print("  all three classes enumerated brute-force")

# 8-element ring F_2[x]/(x(x^2+x+1)) = F_2 x F_4: exhaustive compatible
# count via pruned DFS (complete search, sound pruning), local by
# construction, polynomial by constructive Lagrange + CRT glue.
R8MOD, R8CH = 0b1110, [0b10, 0b111]
constraints = [[(b, c) for b in range(a) for c in R8CH
                if pmod(a ^ b, c) == 0] for a in range(8)]
solutions = set()

def dfs(pos, vals):
    if pos == 8:
        solutions.add(tuple(vals))
        return
    for v in range(8):
        if all(pmod(v ^ vals[b], c) == 0 for b, c in constraints[pos]):
            dfs(pos + 1, vals + [v])

dfs(0, [])
assert len(solutions) == 1024 == 2 ** 2 * 4 ** 4

F4 = [0, 1, 2, 3]                                # residues mod x^2+x+1
def lagrange_f4(g2):
    """Interpolating poly (coeff list over F_4) for g2: F_4 -> F_4."""
    coeffs = [0, 0, 0, 0]
    for u in F4:
        num, denom = [1], 1
        for v in F4:
            if v == u:
                continue
            num = [(num[j - 1] if j else 0) ^
                   pmulmod(num[j] if j < len(num) else 0, v, 0b111)
                   for j in range(len(num) + 1)]
            denom = pmulmod(denom, u ^ v, 0b111)
        scale = pmulmod(g2[u], pinvmod(denom, 0b111), 0b111)
        for j in range(len(num)):
            coeffs[j] ^= pmulmod(num[j], scale, 0b111)
    return coeffs

localpoly8 = set()
for g1code in range(4):
    g1 = [(g1code >> r) & 1 for r in range(2)]
    p1 = [g1[0], g1[0] ^ g1[1]]                  # interpolant over F_2
    for g2code in range(256):
        g2 = [(g2code >> (2 * r)) & 3 for r in range(4)]
        induced = tuple(pcrt([g1[pmod(a, 0b10)], g2[pmod(a, 0b111)]],
                             R8CH) for a in range(8))
        p2 = lagrange_f4(g2)
        glued = [pcrt([p1[j] if j < 2 else 0, p2[j]], R8CH)
                 for j in range(4)]
        vals = []
        for a in range(8):
            v = 0
            for c in reversed(glued):
                v = pmulmod(v, a, R8MOD) ^ c
            vals.append(v)
        assert tuple(vals) == induced            # the glued poly realizes it
        localpoly8.add(induced)
assert localpoly8 == solutions
print("F_2 x F_4 (8 elements): exhaustive compatible (pruned DFS) =")
print("  local = polynomial = 1024 = 2^2 * 4^4; every local function")
print("  realized constructively by Lagrange + degreewise CRT glue")

# Thin-only, mirrored: F_2[x]/x^2 has nilpotents; polynomial functions
# sit strictly inside the 256 functions (= channel-local, vacuously).
polyN = set()
for length in (6, 8):
    cur = set()
    for code in range(4 ** length):
        cs = [(code >> (2 * i)) & 3 for i in range(length)]
        vals = []
        for a in range(4):
            v = 0
            for c in reversed(cs):
                v = pmul(v, a) & 3 ^ c           # mod x^2: keep low 2 bits
            vals.append(v)
        cur.add(tuple(vals))
    if polyN:
        assert cur == polyN                      # stabilized
    polyN = cur
assert len(polyN) < 256
print(f"F_2[x]/x^2 (nilpotent): polynomial functions = {len(polyN)} of 256")
print("  -- the equivalence is THIN-only in the mirror too (cf. Z/4: 64/256)")

# ----------------------------------------------------------------------
section("V. THE SIZE WALL IN THE MIRROR")
# ----------------------------------------------------------------------
# (1) The information core is unchanged: deg is incompatible -- at every
# channel there are congruent pairs with different top-degree bit, so
# deg is not polynomial, not channel-local, and (the argument
# transfers verbatim: channel-local bijections compose and invert
# channel-locally) no within-ring recoding exposes it.
for f in F5_IRR:
    # next() raises StopIteration if no witness exists -- existence IS
    # the test (a dead 'assert wit is not None' would never fire).
    next((a, b) for a in range(W) for b in range(a)
         if pmod(a ^ b, f) == 0 and (pdeg(a) == 9) != (pdeg(b) == 9))
print("deg incompatible: witness pairs at every channel of W --")
print("  the wall's information core transfers verbatim")

# (2) But the archimedean flesh is gone.
# (2a) Sign is VACATED: char-2 fields admit no order (Artin-Schreier:
#      -1 = 1^2 is a square, so nothing is formally real). Computational
#      echo: squaring is a BIJECTION on W (Frobenius), every element is
#      a square, every element is its own negative.
assert len({pmulmod(a, a, FW) for a in range(W)}) == W
print("squaring is a bijection on W (every element a square, -1 = 1):")
print("  the sign face of the wall is not softened, it is VACATED")

# (2b) Multiplication is carry-free: deg(ab) = deg a + deg b EXACTLY
#      (leading coefficients in F_2 multiply to 1; exhaustive a,b < 256).
for a in range(1, 256):
    for b in range(1, 256):
        assert pdeg(pmul(a, b)) == pdeg(a) + pdeg(b)
print("deg(a*b) = deg a + deg b exactly (exhaustive a,b < 256) -- the")
print("  +-1 carry ambiguity of integer bit-length does not exist here")

# (3) The partial-fraction escape, re-priced. Exact identity first:
# a = sum_i c_i * (f/f_i) with c_i = (a mod f_i) * (f/f_i)^-1 mod f_i.
FHAT = [pdivmod(FW, f)[0] for f in F5_IRR]
CINV = [pinvmod(pmod(FHAT[i], F5_IRR[i]), F5_IRR[i]) for i in range(5)]
def pf_coeffs(a):
    return [pmulmod(pmod(a, F5_IRR[i]), CINV[i], F5_IRR[i])
            for i in range(5)]
for a in range(W):
    acc = 0
    for c, fh in zip(pf_coeffs(a), FHAT):
        acc ^= pmul(c, fh)
    assert acc == a
print("partial fractions exact for all 1024 elements of W")

# The expansion of a/f at the place at infinity, truncated to t terms
# per channel: E_t(c, g) = (c << t) // g holds coefficients b_1..b_t of
# c/g = sum b_j x^-j. The XOR of channel expansions is the EXACT prefix
# of a/f's expansion -- coefficient j of the sum depends only on
# coefficient j of each term (ultrametric: no carry propagation), so a
# truncated readout is either exactly right or all-zero (self-flagging).
silent, flag_counts = 0, {}
for t in range(1, 11):
    flagged = 0
    for a in range(W):
        S = 0
        for c, f in zip(pf_coeffs(a), F5_IRR):
            S ^= pdivmod(c << t, f)[0]
        if S == 0:
            flagged += 1
            if not pdeg(a) < 10 - t:             # flag must be truthful
                silent += 1
        else:
            if 10 - t + pdeg(S) != pdeg(a):      # readout must be right
                silent += 1
    flag_counts[t] = flagged
    assert flagged == 1 << (10 - t)              # exactly the small elements
assert silent == 0
print("truncation sweep t = 1..10, all 1024 elements: ZERO silent")
print(f"  failures; flagged counts {flag_counts}")
print("  = 2^(10-t) exactly (the elements with deg < 10 - t). The Z")
print("  escape fails SILENTLY near wraparound (measured); the")
print("  mirror escape is exact-or-flagged. Carries were the failure.")

# (4) Mixed-radix analogue: exact, still triangular (depth = k) -- the
# sequential price is characteristic-free.
for a in range(W):
    rem, digits = a, []
    for f in F5_IRR:
        digits.append(pmod(rem, f))
        rem = pdivmod(rem ^ digits[-1], f)[0]
    assert rem == 0
    acc, m = 0, 1
    for dgt, f in zip(digits, F5_IRR):
        acc ^= pmul(dgt, m)
        m = pmul(m, f)
    assert acc == a
print("mixed-radix: exact, depth-5 sequential -- triangularity is")
print("  characteristic-free (the measured price does not move)")

# (5) Diagonal-function analogue D(a) = XOR of (a div f_i): the
# channel-linearity identity holds verbatim (char-2 signs vanish):
# f * D(a) = a * SQ + sum (a mod f_i)(f/f_i),  SQ = sum f/f_i.
# And it COLLAPSES further: polynomial division by f is F_2-LINEAR in
# the dividend (no borrow propagation), so the sum-of-remainders term
# (degree < deg f) divides away and D(a) = (a * SQ) div f EXACTLY --
# the whole diagonal is one multiplication followed by a shift-out, an
# F_2-linear map. Its size readout is exact with a fixed offset:
# deg D = deg a - (deg f - deg SQ), kernel = the small elements.
SQ = 0
for fh in FHAT:
    SQ ^= fh
assert pdeg(SQ) == 4                  # XOR kills the top f/f_i degrees
for a in range(W):
    D = 0
    for f in F5_IRR:
        D ^= pdivmod(a, f)[0]
    rhs = pmul(a, SQ)
    for f, fh in zip(F5_IRR, FHAT):
        rhs ^= pmul(pmod(a, f), fh)
    assert pmul(FW, D) == rhs                       # channel-linearity identity
    assert D == pdivmod(pmul(a, SQ), FW)[0]         # exact linearity
    if pdeg(a) >= 6:
        assert pdeg(D) == pdeg(a) - 6               # exact offset readout
    else:
        assert D == 0                               # kernel: deg a < 6
print("diagonal: the channel-linearity identity exact for all 1024, and")
print("  stronger -- D(a) = (a*SQ) div f exactly (division by f is")
print("  F_2-linear: no borrows), an F_2-linear map with deg SQ = 4:")
print("  deg D = deg a - 6 for deg a >= 6, D = 0 below (64-element")
print("  kernel). In Z the diagonal is nonlinear (carries couple the")
print("  floor terms); the mirror linearizes even the escape")

# ----------------------------------------------------------------------
section("VI. FINDINGS")
# ----------------------------------------------------------------------
print("""
1. WHAT PLAYS CHANNEL: NOTHING AT RING LEVEL (property + rule). Every
   nim-rung is a field -- idempotents {0,1} (exhaustive at F_256), no
   CRT split: the vertical move is extension, not product. The channels
   live ONE LEVEL DOWN: U(F_2^(2^n)) is cyclic of order 2^(2^n)-1 =
   F_0...F_{n-1}, so the INDEX RING of the nim-rung is a squarefree
   all-field designed tower -- on the five Fermat PRIMES for
   n <= 5 (verified by index isomorphism, exhaustive at n = 2, 3;
   order-certified smallest generators at n = 4, 5), at n = 5 exactly
   the machine-word specimen Z/(2^32-1) = 3*5*17*257*65537; at
   n = 6 on the prime factors of F_0..F_5 (still squarefree, verified);
   beyond, it rides the OPEN all-Fermat-squarefree question.

2. NAPIER INVERSION (rule, stated ranges). The vertical tower has the
   PERFECT second log -- cyclic units, one discrete log, no CRT detour
   (what the primorial tower lacks at every rung k >= 3) -- and
   the maximally blocked third log: every Fermat channel >= 17 has
   8 | p-1, failing the third-log grade B 2-adically; only 3 and 5 are grade A.
   Vertical trades third-rung existence for second-rung perfection.
   Pratt trees of Fermat primes are PATHS; the lambda-chain decays
   arithmetically (2 bits per step): height 10 at 2^32-1 vs 4 at RAD,
   bounding tetration depth at 10 (sampled bases stabilize by 9;
   tower_mod, validated). Chain height is a DESIGN KNOB: Fermat-index
   towers maximize tetration resolution; primorial chains crash.
   Lambda of the index ring is 2^(2^(n-1)) (the cheap-collapse knob)
   for n <= 5 -- and the knob DIES at n = 6 with F_5's compositeness
   (lambda(2^64-1) is not a 2-power), though squarefree/all-field
   survives. All-Fermat-squarefree is OPEN.

3. THE MIRROR PRIMORIAL (rule, exhaustive small rings). F_2[x]/f with
   f squarefree carries the full blueprint: CRT bijection, 2^k
   idempotents, Clifford a^(lambda+1) = a, meadow inverse a^(lambda-1),
   phi = prod(2^e_i - 1) (all exhaustive at the 1024-element W).
   Canonical rungs f = x^(2^d)+x have channels <-> FROBENIUS ORBITS of
   F_2^d-points, lambda = 2^d - 1 MERSENNE BY CONSTRUCTION, and the
   collapse x^lambda = Frobenius^d = d squarings. So the two char-2
   constructions realize the two designed-tower hardware families as INDEX RINGS:
   vertical/nim -> one Fermat tower, horizontal/mirror -> PER-CHANNEL
   Mersenne rings Z/(2^e-1) (designed iff 2^e-1 squarefree: fails
   first at e = 6, prime e clean to 40, general OPEN -- Wieferich;
   grade A exactly at Mersenne-prime exponents in range). The
   rung-wide index ring is their product, NOT a single Z/M -- channels
   of non-coprime degrees share factors (gcd(2^a-1, 2^b-1) =
   2^gcd(a,b)-1; W carries two Z/7s) -- the clean rung-wide Mersenne
   statement is lambda = 2^d-1.

4. THE CRITERION TRANSFERS (rule, exhaustive). channel-local =
   compatible = polynomial on squarefree F_2[x]/f: 16 = 16 = 16 at
   F_2 x F_2 (brute), 1024 = 1024 = 1024 at F_2 x F_4 (pruned-DFS
   exhaustive compatible; every local function realized constructively
   by Lagrange + degreewise CRT glue); thin-only again (F_2[x]/x^2:
   polynomial strictly inside the 256 functions). The locality
   criterion never used the integers.

5. THE SIZE WALL SOFTENS EXACTLY IN ITS ARCHIMEDEAN PART (rule +
   classical contacts). deg is incompatible -- witnesses at every
   channel of W -- so size stays invisible to channels and to every
   channel-local recoding: the INFORMATION CORE of the size wall is
   unchanged. What disappears is everything archimedean about it:
   (i) sign is VACATED, not softened -- char-2 fields admit no order
   (Artin-Schreier; squaring is a bijection on W, -1 = 1); (ii) the
   carry ambiguity is gone -- deg(ab) = deg a + deg b exactly; (iii)
   the partial-fraction escape becomes EXACT-OR-FLAGGED: t-term
   truncation either reads deg exactly or returns an all-zero prefix
   that flags itself -- zero silent failures across all t, all 1024
   elements, vs Z's silent wraparound mode (measured). Carries
   are the archimedean place's shadow in positional digits; the mirror
   (where every place is finite -- Artin-Whaples) deletes them and
   with them every silent size-failure mode, while the wall stands.
   Triangularity (mixed radix) is characteristic-free; the diagonal
   escape COLLAPSES TO AN F_2-LINEAR MAP -- division by f is linear in
   the dividend (no borrows), so D(a) = (a*SQ) div f exactly, with an
   exact offset readout deg D = deg a - (deg f - deg SQ) and a
   small-element kernel. In Z the diagonal is nonlinear (carries
   couple the floor terms); the mirror linearizes even the escape.

6. THE MIRROR'S PRIME SIDE IS CLOSED-FORM (classical contact). The
   Euler product over irreducibles equals 1/(1-2t) coefficientwise
   (verified to t^12) and irreducible counts are exact (Gauss-Mobius):
   the sieve-lens MAP questions trivialize in the mirror. Like the
   designed towers, the mirrors feed engineering, not the prime-lens questions.
""")
print("ALL CHECKS PASSED")
