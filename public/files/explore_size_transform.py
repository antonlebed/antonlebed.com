"""
Operation discovery, hunt 1: is SIZE transform-trivializable? (MOONSHOT, P38)

The CRT log (x -> residue tuple) makes multiplication channel-parallel.
The classic residue-system walls -- magnitude comparison, sign, overflow --
are all SIZE questions. The hunt: is there a transform that makes size
channel-local, or a proof that none can exist? The RNS literature calls
these "non-positional operations" and says channel-wise computation is
impossible "because RNS is non-positional" -- a truism, not a theorem.
This script states and verifies the algebraic theorem behind the wall.

Findings preview (full statements at the bottom):
  1. THE CRITERION: on a squarefree ring, channel-local = compatible =
     polynomial functions. The CRT log trivializes EXACTLY the polynomial
     functions, and only the thin tower has this equivalence (mod 4:
     64 polynomial < 256 channel-local functions).
  2. THE WALL: sign / comparison / overflow are incompatible, hence not
     polynomial, hence no channel-local algorithm computes them -- and the
     obstruction is invariant under every channel-local change of
     coordinates. Nonlinearity is a red herring; the wall is locality.
  3. HOW HIDDEN: fibers over known channel subsets are arithmetic
     progressions; sign-bit bias is <= half an element, and EXACTLY ZERO
     whenever channel 2 is among the unknowns.
  4. THE ESCAPES, each with its price: CRT-fractional sum (exact, but a
     full-precision archimedean summation), mixed-radix (exact, but
     triangular/sequential), diagonal function (exact, but a fresh
     ring-sized modulus). Tie-break lemma: within a diagonal tie class
     the residues mod the smallest modulus strictly increase, so
     (D, x mod p_min) is an exact comparator for ANY squarefree set;
     with 2 a channel the break is a single parity bit.
  5. THE TROPICAL SHADOW: the (min,+) content of a residue is exactly the
     P37 collapse e_supp(x); size is the archimedean place -- the one
     place the CRT log discards (Ostrowski framing).

Runs on RAD (k=7) with exhaustive small-k cross-checks. ~2 s, tiny memory.
"""

import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import Ring, RAD_RING, encode, mod_inverse, idempotent

random.seed(38)
R = RAD_RING
N = R.N
K = R.k
PRIMES = R.primes

def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)

# ───────────────────────────────────────────────────────────────────────
section("I. THE CRITERION: channel-local = compatible = polynomial "
        "(squarefree)")
# ───────────────────────────────────────────────────────────────────────
# f: Z/N -> Z/N is CHANNEL-LOCAL if f(x) mod p depends only on x mod p for
# every channel p (i.e. f is a tuple of per-channel maps g_p).
# f is COMPATIBLE if a = b mod p  =>  f(a) = f(b) mod p, for every p | N.
#
# Channel-local <=> compatible (any squarefree N):
#   local => compatible: f(a) = g_p(a_p) = g_p(b_p) = f(b) mod p.
#   compatible => local: g_p(r) := f(x) mod p for any x with x_p = r is
#   well-defined, and f(x) = CRT(g_p(x_p)) by uniqueness of residues.
# Compatible <=> polynomial (squarefree N only):
#   polynomial => compatible: evaluate the polynomial mod p.
#   compatible => polynomial: each g_p is a function on the FIELD Z/p,
#   hence a polynomial (Lagrange); CRT-glue the coefficients degreewise.
# The gluing step needs fields: mod p^2 not every function on Z/p^2 is
# polynomial, so the equivalence is a THIN-TOWER property (contrast below).

# (a) Exhaustive at Z/6: all 6^6 = 46656 functions; count compatible,
#     channel-local, and polynomial-induced tables. All three must agree.
n6 = 6
compat_count = 0
for code in range(n6 ** n6):
    f = []
    c = code
    for _ in range(n6):
        f.append(c % n6)
        c //= n6
    ok = all(f[a] % p == f[b] % p
             for p in (2, 3) for a in range(n6) for b in range(a + 1, n6)
             if a % p == b % p)
    if ok:
        compat_count += 1
local_count = (2 ** 2) * (3 ** 3)          # independent per-channel maps
poly_tables = set()
for code in range(n6 ** 5):                # degree < 5 suffices at Z/6
    coeffs = []
    c = code
    for _ in range(5):
        coeffs.append(c % n6)
        c //= n6
    poly_tables.add(tuple(sum(co * pow(x, j, n6) for j, co in
                              enumerate(coeffs)) % n6 for x in range(n6)))
print(f"(a) Z/6 exhaustive: compatible {compat_count}, "
      f"channel-local {local_count}, polynomial {len(poly_tables)}")
assert compat_count == local_count == len(poly_tables) == 108

# (b) Constructive lift at Z/30: random per-channel maps -> Lagrange per
#     channel -> CRT-glue coefficients -> one polynomial mod 30 that
#     computes the channel-local function at every point.
R30 = Ring("Z30", (2, 3, 5), (1, 1, 1))
def lagrange_coeffs(g, p):
    """Coefficients (degree < p) of the polynomial inducing g on Z/p."""
    coeffs = [0] * p
    for a in range(p):
        # basis poly L_a(x) = prod_{b != a} (x - b) / (a - b)
        num = [1]                          # polynomial product, low-first
        denom = 1
        for b in range(p):
            if b == a:
                continue
            new = [0] * (len(num) + 1)
            for j, c in enumerate(num):
                new[j] = (new[j] - c * b) % p
                new[j + 1] = (new[j + 1] + c) % p
            num = new
            denom = (denom * (a - b)) % p
        inv = mod_inverse(denom % p, p)
        for j, c in enumerate(num):
            coeffs[j] = (coeffs[j] + g[a] * c * inv) % p
    return coeffs

ok = True
for _ in range(200):
    gs = [[random.randrange(p) for _ in range(p)] for p in R30.primes]
    per_channel = [lagrange_coeffs(g, p) for g, p in zip(gs, R30.primes)]
    glued = []
    for j in range(5):                     # max degree < max prime = 5
        residues = [cs[j] if j < len(cs) else 0 for cs in per_channel]
        # CRT-glue coefficient j
        coef = 0
        for r, p in zip(residues, R30.primes):
            Mp = R30.N // p
            coef = (coef + r * Mp * mod_inverse(Mp, p)) % R30.N
        glued.append(coef)
    for x in range(R30.N):
        want_residues = tuple(g[x % p] for g, p in zip(gs, R30.primes))
        got = sum(co * pow(x, j, R30.N) for j, co in enumerate(glued)) % R30.N
        if tuple(got % p for p in R30.primes) != want_residues:
            ok = False
print(f"(b) Z/30 constructive: 200 random channel-local functions lifted "
      f"to single polynomials,\n    verified at all 30 points each: "
      f"{'VERIFIED' if ok else 'FAILED'}")
assert ok

# (c) Fat contrast at Z/4: one channel, so EVERY function (256) is
#     channel-local; polynomial functions are fewer.
poly4 = set()
for code in range(4 ** 4):                 # degree < mu(4) = 4 suffices
    coeffs = [(code >> (2 * j)) & 3 for j in range(4)]
    poly4.add(tuple(sum(co * pow(x, j, 4) for j, co in enumerate(coeffs)) % 4
                    for x in range(4)))
print(f"(c) Z/4 (fat): {len(poly4)} polynomial functions of 256 "
      f"channel-local -- the equivalence is THIN-ONLY")
assert len(poly4) == 64

print()
print("    => The CRT log trivializes EXACTLY the polynomial functions:")
print("       channel-parallel computable = polynomial, at every thin rung.")

# ───────────────────────────────────────────────────────────────────────
section("II. THE WALL: sign, comparison, overflow are NOT channel-local")
# ───────────────────────────────────────────────────────────────────────
# SGN(x) = [x >= N/2] (the sign bit of the symmetric representation).
# Incompatibility witness per channel p: a = 0 and b = the smallest
# multiple of p at or above N/2 satisfy a = b mod p but SGN differs --
# and 0 != 1 mod p for every p. Hence SGN is not compatible, not
# polynomial, and NO channel-local algorithm computes it. The witnesses
# exist at every rung k >= 2 (each fiber spans both halves).
half = N // 2
print("SGN(x) = [x >= N/2]; per-channel incompatibility witnesses:")
for p in PRIMES:
    b = ((half + p - 1) // p) * p
    assert b < N and b % p == 0 and 0 % p == b % p
    assert (0 < half) and (b >= half)               # SGN(0)=0, SGN(b)=1
    assert (0 - 1) % p != 0                          # 0 != 1 mod p
    print(f"  p={p:>2}: a=0, b={b}  (a=b mod {p}, SGN 0 vs 1)")

# Comparison CMP(x,y) = [x < y] and overflow OV(x,y) = [x+y >= N]: same
# wall, two variables. The criterion holds verbatim for n-variable
# functions (every function (Z/p)^n -> Z/p is a polynomial by Lagrange
# interpolation on the product, and coefficients CRT-glue the same way),
# so incompatible-in-one-argument => not channel-local.
for p in PRIMES:
    # CMP: (0,1) vs (p,1) -- first args agree mod p, CMP flips 1 -> 0.
    assert (0 < 1) and not (p < 1)
    # OV: (0,N-1) vs (p,N-1) -- first args agree mod p, OV flips 0 -> 1.
    assert (0 + N - 1 < N) and (p + N - 1 >= N)
print("CMP(x,y)=[x<y] and OV(x,y)=[x+y>=N]: witnesses verified at all "
      f"{K} channels.")

# Invariance: if T is a channel-local bijection then f o T is channel-local
# iff f is (channel-local maps compose; the inverse of a channel-local
# bijection is channel-local, inverting per channel). So NO channel-local
# change of coordinates -- linear or wildly nonlinear -- can expose size.
# Verified: SGN o T stays incompatible for random per-channel permutations.
ok = True
for _ in range(30):
    perms = [random.sample(range(p), p) for p in R30.primes]
    def T(x):
        residues = [perm[x % p] for perm, p in zip(perms, R30.primes)]
        out = 0
        for r, p in zip(residues, R30.primes):
            Mp = R30.N // p
            out = (out + r * Mp * mod_inverse(Mp, p)) % R30.N
        return out
    sgnT = [1 if T(x) >= 15 else 0 for x in range(30)]
    for p in R30.primes:
        witness = any(sgnT[a] != sgnT[b]
                      for a in range(30) for b in range(a + 1, 30)
                      if a % p == b % p)
        if not witness:
            ok = False
print(f"Invariance: SGN o T incompatible at every channel for 30 random "
      f"channel-local\nbijections T of Z/30: {'VERIFIED' if ok else 'FAILED'}")
assert ok
print()
print("    => The wall is LOCALITY, not linearity. Any exact size detector")
print("       must leave channel-locality; no within-ring recoordination helps.")

# ───────────────────────────────────────────────────────────────────────
section("III. HOW HIDDEN: the proper-subset sign-bit bias dichotomy")
# ───────────────────────────────────────────────────────────────────────
# Fix the residues on a PROPER subset S of channels (the known channels).
# The fiber is an arithmetic progression x0 + t*d, d = prod(p in S),
# length L = N/d, covering [0,N) with even spacing. Count below N/2:
# ceil(L/2 - x0/d), which is EXACTLY L/2 when L is even (2 not in S),
# and (L +- 1)/2 when L is odd (2 in S). So:
#   - channel 2 UNKNOWN  => exactly zero information about the sign bit;
#   - channel 2 KNOWN    => bias at most half an element of the fiber.

# Exhaustive at k=4 (N=210): every proper nonempty subset, every fiber.
R4 = Ring("Z210", (2, 3, 5, 7), (1, 1, 1, 1))
n4 = R4.N
max_dev_even = 0.0
max_dev_odd = 0.0
for mask in range(1, 2 ** 4 - 1):
    S = [i for i in range(4) if mask & (1 << i)]
    d = math.prod(R4.primes[i] for i in S)
    L = n4 // d
    for x0 in range(d):
        # fiber = {x0 + t*d}; (residues on S are those of x0)
        count = sum(1 for t in range(L) if x0 + t * d < n4 // 2)
        if L % 2 == 0:
            assert count == L // 2, (S, x0)
            max_dev_even = max(max_dev_even, abs(count - L / 2))
        else:
            assert count in ((L - 1) // 2, (L + 1) // 2), (S, x0)
            max_dev_odd = max(max_dev_odd, abs(count - L / 2))
print(f"k=4 exhaustive (all 14 proper subsets, all fibers): "
      f"max deviation from L/2:\n"
      f"  2 unknown (L even): {max_dev_even}  (EXACTLY ZERO bias)\n"
      f"  2 known   (L odd):  {max_dev_odd}  (half an element)")

# RAD direct check at the extreme subset: know ONLY channel 2
below_even = sum(1 for x in range(0, N, 2) if x < half)
below_odd = sum(1 for x in range(1, N, 2) if x < half)
print(f"RAD: know only channel 2: even fiber {below_even}/{N//2} below N/2, "
      f"odd fiber {below_odd}/{N//2}")
assert abs(below_even - N / 4) <= 0.5 and abs(below_odd - N / 4) <= 0.5
print()
print("    => Hide channel 2 and the other six channels together carry")
print("       EXACTLY ZERO bits about the sign. Size is not merely")
print("       unexposed by the CRT log; it is equidistributed away.")

# ───────────────────────────────────────────────────────────────────────
section("IV. THE ESCAPES: every exact method pays one of three prices")
# ───────────────────────────────────────────────────────────────────────

# (a) CRT-FRACTIONAL SUM (the archimedean summation; standard, exact).
#     x/N = frac( sum_p (x_p * w_p mod p) / p ),  w_p = (N/p)^{-1} mod p.
#     This is the partial-fraction (Prufer) decomposition of x/N in Q/Z:
#     size IS channel-additive -- in the circle group, not the ring.
#     Integer form verified for ALL x at RAD: sum_p (x_p w_p mod p)*(N/p)
#     = x + c*N with 0 <= c < k.
w = {p: mod_inverse(N // p, p) for p in PRIMES}
Mdiv = {p: N // p for p in PRIMES}
max_c = 0
for x in range(N):
    s = 0
    for p in PRIMES:
        s += ((x % p) * w[p] % p) * Mdiv[p]
    assert s % N == x
    c = s // N
    if c > max_c:
        max_c = c
print(f"(a) CRT-fractional: integer identity verified for all {N} x; "
      f"carry c <= {max_c} < k={K}.")
print("    EXACT -- price: the sum must be carried at FULL precision")
print("    (log2 N bits). Truncation to t bits fails two ways: close")
print("    pairs (error window) and small x (the per-term truncation")
print("    error wraps past the mod-1 boundary, misordering x against")
print("    ANY y -- the literature's documented near-zero failure):")
for t in (16, 24, 32):
    scale = 1 << t
    def frac_t(x):
        return sum((((x % p) * w[p] % p) * scale // p) for p in PRIMES) % scale
    bound = K * N // scale + 1
    close = wrap = 0
    for _ in range(100_000):
        x, y = random.randrange(N), random.randrange(N)
        if x == y:
            continue
        if (frac_t(x) < frac_t(y)) != (x < y):
            if abs(x - y) <= bound:
                close += 1
            else:
                assert min(x, y) <= bound, (t, x, y)
                wrap += 1
    print(f"      t={t}: {close + wrap}/100000 wrong "
          f"({close} close-pair, {wrap} wraparound); every failure within "
          f"{bound} (~ k*N/2^t) of the partner or of 0")

# (b) MIXED-RADIX CONVERSION (exact; the price is SEQUENTIAL depth).
#     Digits a_0 + a_1*2 + a_2*6 + a_3*30 at k=4: each digit needs the
#     previous -- a TRIANGULAR transform, the antithesis of channel-diagonal.
def mrc_digits(x, ring):
    digits = []
    residues = list(encode(x, ring))
    primes = ring.primes
    for i, p in enumerate(primes):
        a = residues[i] % p
        digits.append(a)
        for j in range(i + 1, ring.k):
            q = primes[j]
            residues[j] = ((residues[j] - a) *
                           mod_inverse(p % q, q)) % q
    return digits
ok = all(d[0] + d[1] * 2 + d[2] * 6 + d[3] * 30 == x
         for x, d in ((x, mrc_digits(x, R4)) for x in range(n4)))
keys = [tuple(reversed(mrc_digits(x, R4))) for x in range(n4)]
ok = ok and keys == sorted(keys) and len(set(keys)) == n4
print(f"(b) Mixed-radix at k=4: reconstruction + lexicographic order = "
      f"magnitude order,\n    all {n4} values: {'VERIFIED' if ok else 'FAILED'}")
assert ok
print("    EXACT -- price: depth k, each digit gated on the last "
      "(triangular, not diagonal).")

# (c) DIAGONAL FUNCTION (Akushskii core function with unit weights;
#     exact comparator here -- the price is a FRESH ring-sized modulus).
#     D(x) = sum_p (x - x_p)/p = sum_p floor(x/p). Over Z:
#     D*N = x*SQ - sum_p x_p*(N/p), SQ = sum_p N/p, so with gcd(N,SQ)=1:
#     D = -N^{-1} * sum_p x_p*(N/p)  (mod SQ) -- channel-LINEAR, but the
#     arithmetic lives in Z/SQ, a NEW modulus as large as the ring.
SQ = sum(N // p for p in PRIMES)
g = math.gcd(N, SQ)
print(f"(c) Diagonal function: SQ = sum N/p = {SQ} (~{SQ/N:.3f} N), "
      f"gcd(N, SQ) = {g}")
assert g == 1
Ninv = mod_inverse(N % SQ, SQ)
cp = {p: (-Ninv * (N // p)) % SQ for p in PRIMES}
ties = 0
prevD = None
for x in range(N):
    D = sum(x // p for p in PRIMES)
    lin = sum((x % p) * cp[p] for p in PRIMES) % SQ
    assert lin == D
    if prevD is not None:
        assert D >= prevD                    # monotone
        if D == prevD:
            ties += 1
            assert math.gcd(x, N) == 1       # tie partner x is a unit
    prevD = D
print(f"    channel-linear form mod SQ == direct D for all {N} x; "
      f"monotone; ties = {ties} = phi(N) = {R.phi}")
assert ties == R.phi
# TIE-BREAK LEMMA (proved): D steps exactly at the multiples of the
# moduli, so a D-tie class is a run of <= p_min consecutive integers
# none of which, past the first, is divisible by ANY modulus (at
# all-prime sets: later elements are units). No channel residue can
# wrap inside a class, so the residues at EVERY channel strictly
# increase, and (D, x mod p_min) is an exact comparator for ANY
# squarefree modulus set (composite-moduli specimen verified P102,
# explore_rns_comparator.py). (The residue tie-break is also the
# standard sum-of-quotients (SQT) architecture's move -- a parallel
# compare on one channel's residues, Dimauro 1993 / Piestrak IPL 2015;
# the lemma supplies the general proof and scope. The
# modified-diagonal strand changes D itself instead.) With 2 as a
# channel the tie-break is a single parity bit and ties cap at
# adjacent pairs.
ok = True
for _ in range(100_000):
    x, y = random.randrange(N), random.randrange(N)
    Dx = sum(x // p for p in PRIMES)
    Dy = sum(y // p for p in PRIMES)
    verdict = (Dx < Dy) or (Dx == Dy and x % 2 < y % 2)
    if verdict != (x < y):
        ok = False
print(f"    (D, parity) exact comparator, 100k random pairs: "
      f"{'VERIFIED' if ok else 'FAILED'}")
assert ok
# Odd-moduli check of the lemma: drop channel 2 (the standard odd-RNS
# regime, p_min = 3). Tie classes reach size 3; residues mod 3 increase
# strictly inside every class; (D, x mod 3) stays exact.
ODD = PRIMES[1:]
nodd = N // 2
def D_odd(x):
    return sum(x // p for p in ODD)
max_class = 1
cls = 1
for x in range(1, nodd):
    if D_odd(x) == D_odd(x - 1):
        cls += 1
        assert (x - 1) % 3 < x % 3          # strict increase mod p_min=3
        max_class = max(max_class, cls)
    else:
        cls = 1
ok = True
for _ in range(100_000):
    x, y = random.randrange(nodd), random.randrange(nodd)
    verdict = (D_odd(x) < D_odd(y)) or (D_odd(x) == D_odd(y) and
                                        x % 3 < y % 3)
    if x != y and verdict != (x < y):
        ok = False
print(f"    odd-moduli lemma check (ring {nodd}, p_min=3): max tie class "
      f"{max_class},\n    residues mod 3 strictly increase in every class, "
      f"(D, x mod 3) exact on 100k\n    random pairs: "
      f"{'VERIFIED' if ok else 'FAILED'}")
assert ok and max_class == 3
print("    EXACT -- price: one dot product mod a fresh modulus SQ ~ 1.4 N.")
print("    (Core function = weighted diagonal; the redundant-modulus")
print("    variants = base extension: same price, a bolted-on positional")
print("    channel. Every KNOWN exact method pays one of prices (a)-(c).)")

# ───────────────────────────────────────────────────────────────────────
section("V. THE TROPICAL SHADOW: size is the archimedean place")
# ───────────────────────────────────────────────────────────────────────
# ROAD lead 3 asked: does size live naturally in the (min,+) image?
# Answer: NO. On a squarefree ring the only well-defined valuation data
# of a residue is v_p in {0, >=1} per channel -- the zero pattern. The
# (min,+) shadow of Z/N is the support lattice {0,1}^k, i.e. exactly the
# idempotent skeleton, and the shadow map is the P37 collapse x -> x^lambda
# = e_supp(x). All phi(N) units share ONE shadow while ranging over the
# whole interval [1, N-1]: size and tropical content are fully decoupled.
ok = True
for _ in range(10_000):
    x = random.randrange(N)
    S = frozenset(i for i, r in enumerate(encode(x, R)) if r != 0)
    if pow(x, R.lam, N) != idempotent(S, R):
        ok = False
print(f"shadow(x) = x^lambda = e_supp(x), 10k random x: "
      f"{'VERIFIED' if ok else 'FAILED'}")
assert ok
units = [x for x in (1, N - 1) if math.gcd(x, N) == 1]
assert units == [1, N - 1]
print(f"units 1 and N-1 = {N-1}: same full-support shadow, sizes at the "
      f"two ends of the ring.")
print()
print("    Ostrowski's theorem names the obstruction: the places of Q are")
print("    the primes plus ONE archimedean place, where size lives. Each")
print("    channel carries the reduction at one finite place; no channel")
print("    carries archimedean data. Recovering size = recovering the")
print("    discarded place = the full-precision summation of escape (a).")

# ───────────────────────────────────────────────────────────────────────
section("FINDINGS (tiers per CLAUDE.md)")
# ───────────────────────────────────────────────────────────────────────
print("""
1. THE CRITERION (rule, proved; classical ingredients, Kempner-flavored).
   On a squarefree ring: channel-local = compatible = polynomial
   functions. Exhaustive at Z/6 (all 46656 functions: 108 = 108 = 108);
   constructive Lagrange+CRT lift at Z/30. The equivalence is THIN-ONLY:
   mod 4 has 64 polynomial of 256 channel-local functions. The CRT log
   trivializes exactly the polynomial functions -- this is the algebraic
   form of the RNS literature's "non-positional" truism.

2. THE WALL (rule, proved). Sign, comparison, and overflow are
   incompatible (explicit witnesses at every channel, every rung k >= 2),
   hence not polynomial, hence NOT channel-locally computable -- and the
   obstruction is invariant under every channel-local bijection. The wall
   is locality, not linearity: no within-ring transform, linear or
   nonlinear, can expose size. Any exact size detector must leave the
   ring or leave locality.

3. THE HIDING DICHOTOMY (rule, proved + exhaustive k=4). Fibers over
   known channel subsets are arithmetic progressions: with channel 2
   among the unknowns the sign bit is EXACTLY equidistributed (zero
   information); with 2 known the bias is at most half an element.

4. THE ESCAPES (rule for the constructions; classification observation).
   Three exact escapes, three prices: (a) CRT-fractional / partial-
   fraction summation -- exact identity verified at all 510510 RAD
   values; price = full log2(N)-bit archimedean sum (t-bit truncation
   fails only within k*N/2^t of the partner or of 0, measured -- the
   wraparound mode is the literature's near-zero failure). (b) Mixed-radix --
   exact; price = triangular sequential depth k. (c) Diagonal function --
   channel-linear mod a FRESH modulus SQ ~ 1.4N (verified all x);
   price = ring-sized new modulus. The KNOWN exact methods (core
   function, base extension, redundant moduli; approximate reciprocals
   = escape (a) truncated) each pay one -- a classification of the
   literature, not a theorem over all possible methods.

5. THE TIE-BREAK LEMMA (rule, proved + verified, incl. a composite-
   moduli specimen P102). D steps exactly at the multiples of the
   moduli, so no tie-class element past the first is divisible by ANY
   modulus and no channel residue wraps inside a class: the residues
   at EVERY channel strictly increase, and (D, x mod p_min) is an
   exact comparator for ANY squarefree modulus set -- the same residue
   compare the standard sum-of-quotients (SQT) comparator wires in
   parallel (Dimauro 1993; Piestrak, IPL 2015); the lemma is the
   general proof and scope (P102 contact). Tower bonus: with 2 as a
   channel the tie-break is a single parity bit, ties cap at adjacent
   pairs {x, x+1} (count = phi(N)), and parity itself is free (unlike
   odd-moduli RNS).

6. THE TROPICAL ANSWER (observation + standard framing). Size does NOT
   live in the (min,+) image: the tropical shadow of a residue is exactly
   the P37 collapse e_supp(x) (all units share one shadow). Ostrowski
   names the wall: channels are the finite places of Q; size is the
   archimedean place -- the one place the CRT log discards by
   construction. What CRT trivializes (polynomials) and what it hides
   (size) are now both exactly characterized.
""")
print("ALL ASSERTIONS PASSED")
