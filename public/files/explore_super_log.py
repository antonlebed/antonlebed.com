"""
Operation discovery, hunt (b): the MISSING SUPER-LOGARITHM. (MOONSHOT, P41)

Hunts 1+2 charted the tower's two logs: the CRT map (P38 -- trivializes
exactly the polynomial functions, walls off size at the archimedean
place) and the index transform (P39 -- per-channel discrete log, x -> +,
walled by Zech's incompressible table). Napier's ladder suggests a THIRD
move: a coordinate in which POWERING becomes addition -- a
super-logarithm. Per channel, powering reads as multiplication in the
index ring Z/(p-1); a third log is therefore an index transform ON the
index ring. This script charts when that exists, what the recursion
costs, and where the ladder ends.

Survey anchors (standard material, named so nothing here poses as new):
Gauss (primitive roots mod m exist iff m in {1, 2, 4, q^k, 2q^k}, q an
odd prime; U(2^k) = <-1> x <5> for k >= 3 -- the unique non-cyclic
prime-power unit group), Pohlig-Hellman 1978 (the DL computation
already decomposes along the CRT split of the group order -- our
level-2 split, in algorithmic form), Mirsky 1949 (the density of
primes with p-1 squarefree is Artin's constant 0.3739558...), the
iterated Carmichael lambda function (Martin-Pomerance, Acta Arith. 118
(2005); Harland for the number of iterates needed to reach 1), Pratt
1975 (primality certificates recurse on the factors of p-1 -- the
iterated-log ladder IS the Pratt tree; tree heights and shape:
Ford-Konyagin-Luca, GAFA 2010), power-tower stabilization mod m
(folklore, via the generalized Euler lift), and Stadler 1996 (the
double discrete logarithm y = g^(h^x) is a cryptographic HARDNESS
assumption -- the crypto literature treats the second exponent level as
opaque, not as a coordinate).

Findings preview (full statements at the bottom):
  1. TYPE ESCAPE: powering is not a ring operation -- x^y is ill-defined
     on (x mod N, y mod N); it is well-defined as Z/N x Z/lambda(N) ->
     Z/N for exponents >= 1. The hyperoperation ladder exits the ring at
     the third rung; each exponent level lives one ring DOWN the
     lambda-chain.
  2. THREE GRADES OF EXISTENCE: (A) a single super-log on the index
     ring exists iff Z/(p-1) is cyclic (Gauss) -- inside RAD, channels
     13 and 17 already FAIL; census: the passing primes (essentially
     p = 2q^k + 1, safe-prime-like) thin out toward density 0.
     (B) a super-log through a SECOND CRT split exists iff 8 does not
     divide p-1 (odd prime-power unit groups are always cyclic; the
     unique obstruction is 2-adic) -- density 3/4; inside RAD only
     p = 17 fails. (C) the 2-adic group patch U(2^k) = <-1> x <5>
     always exists but is group-theoretic only: Z/2^k is local (no
     idempotents but 0, 1), so no ring split carries it.
  3. SELF-SIMILARITY EXACTLY ON SKIP TOWERS: the full level-1 blueprint
     (field channels, x^(lambda+1) = x, graded log over non-units)
     recurs at level 2 iff p-1 is SQUAREFREE -- then Z/(p-1) is itself
     a designed tower (P38). Otherwise nilpotents appear and the
     Clifford extension dies (witnesses in Z/4, Z/12, Z/16). Density of
     self-similar channels = Artin's constant (Mirsky), census-matched.
  4. THE LADDER IS THE PRATT TREE: iterating "unit group + CRT split"
     descends the Pratt certificate tree; the level-2 split is
     Pohlig-Hellman's decomposition. The lambda-chain of RAD is
     510510 -> 240 -> 4 -> 2 -> 1 (height 4).
  5. TETRATION COLLAPSES: x^^h mod N (any base x >= 2; x = 0
     alternates by the 0^0 convention) is constant once h reaches the
     lambda-chain height (lift validated against exact integers) -- at
     RAD every power tower stabilizes by depth 4. Above x, "turn it
     into +" dissolves: the operation has finitely many distinguishable
     depths, so a super-logarithm mod N takes at most H values.
  6. THE THIRD WALL IS EXISTENCE: size wall = information obstruction
     (cross-channel), Zech wall = structure obstruction
     (within-channel), super-log wall = the coordinate's DOMAIN dies
     (non-cyclic 2-adic unit groups, nilpotent leakage,
     finite lambda-chain). Crypto already prices the opacity: the
     double discrete log is someone else's one-way function.

Runs on RAD (k=7) with exhaustive small-ring cross-checks and a prime
census to 10^6. ~0.5 s, ~38 MB.
"""

import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import (Ring, RAD_RING, carmichael_lambda, multiplicative_order,
                 factorize, primes_up_to, lcm_list)

random.seed(41)
R = RAD_RING
N = R.N
PRIMES = R.primes
LAM = R.lam

def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)

def units_of(m):
    return [x for x in range(1, m + 1) if math.gcd(x, m) == 1] if m > 1 else [0]

def is_cyclic_brute(m):
    """U(m) cyclic, by computing the maximal order (small m only)."""
    if m <= 2:
        return True
    phi = len([x for x in range(1, m) if math.gcd(x, m) == 1])
    return any(multiplicative_order(x, m) == phi
               for x in range(1, m) if math.gcd(x, m) == 1)

def is_cyclic_criterion(m):
    """Gauss: Z/m has a primitive root iff m in {1, 2, 4, q^k, 2q^k}."""
    if m in (1, 2, 4):
        return True
    if m % 4 == 0:
        return False
    core = m // 2 if m % 2 == 0 else m
    fac = factorize(core)
    return len(fac) == 1 and 2 not in fac

def is_squarefree(m):
    return all(e == 1 for e in factorize(m).values()) if m > 1 else True

# ----------------------------------------------------------------------
section("I. THE TYPE ESCAPE: POWERING IS NOT A RING OPERATION")
# ----------------------------------------------------------------------
# + and x map Z/N x Z/N -> Z/N. Powering does not: x^y is not a
# function of (x mod N, y mod N). Exhaustive witness count at Z/30.
bad = sum(1 for x in range(30) for y in range(1, 30)
          if pow(x, y, 30) != pow(x, y + 30, 30))
assert bad > 0
print(f"Z/30: x^y != x^(y+30) for {bad} of {30*29} pairs (x, y>=1)")
print("      -> the exponent slot does NOT live in the ring.")

# Where it does live: one ring down. For ALL x and a >= 1,
# x^(a + lambda) = x^a (per channel: 0 stays 0, units have order
# dividing lambda). Exhaustive at Z/30 and Z/210, sampled at RAD.
for m in (30, 210):
    lm = carmichael_lambda(m)
    for x in range(m):
        for a in range(1, lm + 1):
            assert pow(x, a + lm, m) == pow(x, a, m)
    print(f"Z/{m}: x^(a+lambda) = x^a for all x, a>=1 (exhaustive, "
          f"lambda={lm})")
for _ in range(20000):
    x, a = random.randrange(N), random.randrange(1, LAM + 1)
    assert pow(x, a + LAM, N) == pow(x, a, N)
print(f"RAD:  same, 20000 sampled (x, a) pairs (lambda={LAM})")
print()
print("Ladder of types:  +, x : Z/N x Z/N      -> Z/N   (ring ops)")
print("                  ^    : Z/N x Z/lambda -> Z/N   (exponent one")
print("                         rung down -- a module action, not a")
print("                         ring operation)")

# ----------------------------------------------------------------------
section("II. THE THIRD LOG: THREE GRADES OF EXISTENCE")
# ----------------------------------------------------------------------
# P39 cross-check: in index coordinates powering is index-ring
# multiplication. Channel p=7, g=3: ind(x^n) = n * ind(x) mod 6.
p7, g7 = 7, 3
ind7 = {}
x = 1
for n in range(p7 - 1):
    ind7[x] = n
    x = x * g7 % p7
for u in range(1, p7):
    for n in range(12):
        assert ind7[pow(u, n, p7)] == (n * ind7[u]) % (p7 - 1)
print("powering = index-ring multiplication (p=7, exhaustive): "
      "ind(x^n) = n*ind(x) mod 6")
print("-> a super-log must linearize multiplication in Z/(p-1).")
print()

# Grade A: a single index transform on Z/(p-1) exists iff Z/(p-1) is
# cyclic. Validate the Gauss criterion against brute force, m <= 300.
for m in range(1, 301):
    assert is_cyclic_brute(m) == is_cyclic_criterion(m)
print("Gauss criterion (cyclic iff m in {1,2,4,q^k,2q^k}) validated "
      "against brute force, m <= 300")
print()

# RAD channel table: all three grades per channel.
print("RAD channels -- the third log per channel:")
print(f"  {'p':>3} {'p-1':>4} {'factor':>10} {'A: cyclic':>10} "
      f"{'B: 8|p-1?':>10} {'sf(p-1)':>8}")
for p in PRIMES:
    m = p - 1
    fac = "*".join(f"{q}^{e}" if e > 1 else f"{q}"
                   for q, e in factorize(m).items()) if m > 1 else "1"
    a = "yes" if is_cyclic_criterion(m) else "NO"
    b = "FAILS" if m % 8 == 0 else "yes"
    sf = "yes" if is_squarefree(m) else "NO"
    print(f"  {p:>3} {m:>4} {fac:>10} {a:>10} {b:>10} {sf:>8}")
assert not is_cyclic_criterion(12) and not is_cyclic_criterion(16)
assert is_cyclic_criterion(6) and is_cyclic_criterion(10)
print()
print("Grade A fails INSIDE RAD at p = 13 (Z/12) and p = 17 (Z/16).")

# Grade B: split Z/(p-1) by CRT into prime-power channels and take a
# log per channel. Odd prime-power unit groups are always cyclic
# (Gauss); U(2^k) is non-cyclic for k >= 3. So grade B exists iff
# 8 does not divide p-1. Inside RAD only p = 17 fails (16 = 2^4);
# p = 13 passes: Z/12 = Z/4 x Z/3, both unit groups cyclic.
assert all(is_cyclic_criterion(q ** e)
           for q in (3, 5, 7, 11, 13) for e in (1, 2, 3))
assert is_cyclic_criterion(4) and not is_cyclic_criterion(8) \
    and not is_cyclic_criterion(16)
print("Grade B (second CRT split) exists iff 8 does not divide p-1:")
print("  the ONLY non-cyclic prime-power unit group is U(2^k), k >= 3.")
print("  RAD: p = 13 passes (12 = 4*3, U(4) and U(3) cyclic);")
print("       p = 17 fails (16 = 2^4, U(16) non-cyclic, ring unsplittable).")
# Grade A can fail where grade B passes: p = 31 has p-1 = 30, not
# divisible by 8, yet Z/30 is non-cyclic -- U(3) and U(5) both have
# even order, the same lambda < phi collision that kills the level-1
# primitive root. Only grade B's residual obstruction is purely 2-adic.
assert not is_cyclic_criterion(30) and 30 % 8 != 0
print("  (Grade A fails without any 8: p = 31 -> Z/30 non-cyclic -- the")
print("   level-1 lambda < phi mechanism. Only grade B is purely 2-adic.)")

# Grade C: the 2-adic group patch. U(2^k) = <-1> x <5> (k >= 3) --
# verify at 8 and 16 -- but Z/2^k is LOCAL: its only idempotents are
# 0 and 1, so no ring decomposition carries the factorization. The
# patch is group theory, not a ring-channel coordinate.
for k in (3, 4):
    m = 2 ** k
    sub5 = set()
    x = 1
    while x not in sub5:
        sub5.add(x)
        x = x * 5 % m
    full = set(u % m for u in units_of(m))
    span = set(s % m for s in sub5) | set((m - 1) * s % m for s in sub5)
    assert span == full and (m - 1) not in sub5
    idem = [x for x in range(m) if x * x % m == x]
    assert idem == [0, 1]
print("Grade C: U(8), U(16) = <-1> x <5> verified; idempotents of "
      "Z/8, Z/16 = {0,1}")
print("  (local ring, no CRT split: the patch is group-only).")
print()

# Census to 10^6: how common is each grade?
LIMIT = 10 ** 6
ps = primes_up_to(LIMIT)
sf_sieve = bytearray([1]) * (LIMIT + 1)
d = 2
while d * d <= LIMIT:
    for j in range(d * d, LIMIT + 1, d * d):
        sf_sieve[j] = 0
    d += 1

# smallest-prime-factor sieve up to LIMIT//2 (we factor (p-1)/2)
HALF = LIMIT // 2
spf = list(range(HALF + 1))
i = 2
while i * i <= HALF:
    if spf[i] == i:
        for j in range(i * i, HALF + 1, i):
            if spf[j] == j:
                spf[j] = i
    i += 1

def grade_a(p):
    m = p - 1
    if m in (1, 2, 4):
        return True
    if m % 4 == 0:
        return False
    h = m // 2                       # odd; need h = q^k, q odd prime
    q = spf[h]
    while h % q == 0:
        h //= q
    return h == 1

counts = {}
for bound in (10 ** 4, 10 ** 5, 10 ** 6):
    sub = [p for p in ps if p <= bound]
    na = sum(1 for p in sub if grade_a(p))
    nb = sum(1 for p in sub if (p - 1) % 8 != 0)
    nsf = sum(1 for p in sub if sf_sieve[p - 1])
    counts[bound] = (len(sub), na, nb, nsf)
    print(f"p <= 10^{round(math.log10(bound))}: {len(sub):>6} primes | "
          f"grade A {na:>5} ({na/len(sub):.3f}) | "
          f"grade B {nb:>6} ({nb/len(sub):.3f}) | "
          f"sf(p-1) {nsf:>6} ({nsf/len(sub):.3f})")
fa = [counts[b][1] / counts[b][0] for b in (10**4, 10**5, 10**6)]
assert fa[0] > fa[1] > fa[2]         # grade A thins out
nP, _, nb6, nsf6 = counts[10 ** 6]
assert abs(nb6 / nP - 0.75) < 0.01           # Dirichlet: p = 1 mod 8 has density 1/4
ARTIN = 0.3739558136
assert abs(nsf6 / nP - ARTIN) < 0.01         # Mirsky
print()
print(f"grade A (p = 2q^k+1, safe-prime-like) thins: "
      f"{fa[0]:.3f} -> {fa[1]:.3f} -> {fa[2]:.3f} (toward density 0)")
print(f"grade B fraction {nb6/nP:.4f} ~ 3/4 (Dirichlet, p != 1 mod 8)")
print(f"sf(p-1) fraction {nsf6/nP:.4f} ~ Artin constant {ARTIN:.4f} "
      f"(Mirsky)")

# ----------------------------------------------------------------------
section("III. SELF-SIMILARITY EXACTLY ON SKIP TOWERS")
# ----------------------------------------------------------------------
# The level-1 blueprint needs two facts: squarefree modulus (field
# channels, no nilpotents, Clifford identity x^(lambda+1) = x, graded
# log over non-units) and cyclic channel unit groups (fields: always).
# At level 2 the modulus is p-1. The Clifford identity characterizes
# squarefreeness -- validate the iff for all m <= 300.
for m in range(2, 301):
    lm = carmichael_lambda(m)
    holds = all(pow(x, lm + 1, m) == x for x in range(m))
    assert holds == is_squarefree(m)
print("x^(lambda+1) = x for all x  IFF  m squarefree (validated m <= 300)")
print()
# Witnesses inside RAD's index rings: nilpotents and Clifford failures.
for m in (4, 12, 16):
    lm = carmichael_lambda(m)
    fails = [x for x in range(m) if pow(x, lm + 1, m) != x]
    nilp = [x for x in range(1, m) if pow(x, 5, m) == 0]
    print(f"Z/{m}: x^(lambda+1) = x fails for {len(fails)} elements "
          f"(e.g. x={fails[0]}); nilpotents {nilp}")
    assert fails and nilp
for m in (6, 10):
    lm = carmichael_lambda(m)
    assert all(pow(x, lm + 1, m) == x for x in range(m))
    assert all(e == 1 for e in factorize(m).values())
print("Z/6, Z/10: Clifford identity holds, all channels fields -- these")
print("  index rings ARE designed towers (P38 skip towers: {2,3}, {2,5}).")
print()
print("So the ladder is self-similar at a channel IFF p-1 is squarefree:")
print("  then Z/(p-1) carries the FULL level-1 blueprint and the same")
print("  two moves (CRT split + per-channel index) repeat verbatim.")
print("  Density of self-similar channels = Artin constant (Mirsky).")
print("  RAD: self-similar at p = 2, 3, 7, 11; broken at p = 5, 13, 17.")
for p in PRIMES:
    assert is_squarefree(p - 1) == (p in (2, 3, 7, 11))

# ----------------------------------------------------------------------
section("IV. THE LADDER IS THE PRATT TREE")
# ----------------------------------------------------------------------
# Iterating "take the unit group, split by CRT" from a prime p descends
# on the prime factors of p-1: exactly the recursion of Pratt's
# primality certificate. The level-2 split is what Pohlig-Hellman
# exploits algorithmically. Print RAD's forest with squarefree labels.
def pratt(p, depth=0, out=None):
    out = out if out is not None else []
    m = p - 1
    tag = "" if m <= 1 else ("  [sf]" if is_squarefree(m) else "  [NOT sf]")
    out.append("    " + "  " * depth + f"{p} -> {m}{tag}")
    for q in factorize(m):
        if q > 2:
            pratt(q, depth + 1, out)
    return out

for p in PRIMES:
    for line in pratt(p):
        print(line)
print()

# The lambda-chain: m -> lambda(m) -> ... -> 1. Each hyperoperation
# level consumes one rung (Section I: exponents live one rung down).
def lam_chain(m):
    chain = [m]
    while chain[-1] > 1:
        chain.append(carmichael_lambda(chain[-1]))
    return chain

for m in (30, 210, N):
    ch = lam_chain(m)
    print(f"lambda-chain of {m}: {' -> '.join(map(str, ch))}   "
          f"(height {len(ch) - 1})")
assert lam_chain(N) == [510510, 240, 4, 2, 1]
H_RAD = len(lam_chain(N)) - 1
print()
print("Chain length is O(log m) (iterated-lambda literature:")
print("Martin-Pomerance 2005, Harland). The tower's whole hyperoperation")
print(f"ladder above x has at most {H_RAD} live levels at RAD.")

# ----------------------------------------------------------------------
section("V. TETRATION COLLAPSES")
# ----------------------------------------------------------------------
# The generalized Euler lift: x^e = x^(lambda(m) + (e mod lambda(m)))
# mod m for ALL x (units AND non-units), PROVIDED e >= log2(m) AND
# lambda(m) >= nu(m), the largest prime-power exponent of m -- the
# lifted exponent must keep every non-unit channel absorbed. The only
# moduli that violate the second condition are m = 8 and m = 24
# (lambda = 2 < nu = 3); every modulus this script feeds the recursion
# satisfies it (squarefree rings and their chain elements 240, 16, 12,
# 4, 2 -- and tower_mod asserts it on every call, so a future reuse on
# a ring whose lambda-chain passes through 24 fails loudly instead of
# silently). Exhaustive at Z/30 and Z/210, sampled at RAD.
for m in (30, 210):
    lm = carmichael_lambda(m)
    for x in range(m):
        for e in range(8, 8 + 2 * lm):
            assert pow(x, e, m) == pow(x, (e % lm) + lm, m)
print("generalized Euler lift validated exhaustively at Z/30, Z/210")
for _ in range(5000):
    x, e = random.randrange(N), random.randrange(20, 2000)
    assert pow(x, e, N) == pow(x, (e % LAM) + LAM, N)
print("                          and on 5000 sampled (x, e) at RAD")
# Negative control: the naive lambda-lift is NOT a general lemma.
assert pow(2, 6, 24) != pow(2, (6 % 2) + 2, 24)      # 16 != 4 at m = 24
print("negative control: the lift fails at m = 24 (lambda 2 < nu 3) --")
print("                  tower_mod asserts the validity condition per call")

def exact_tower(x, h, max_bits=1 << 22):
    """x^^h as an exact integer, or None if it exceeds max_bits."""
    t = 1
    for _ in range(h):
        if x >= 2 and t > max_bits / math.log2(x):
            return None
        t = x ** t
    return t

def tower_mod(x, h, m):
    """x^^h mod m via the lambda-chain recursion."""
    if m == 1:
        return 0
    if h == 0:
        return 1 % m
    t = exact_tower(x, h - 1, max_bits=64)
    if t is not None:                # exponent fits: direct
        return pow(x, t, m)
    lm = carmichael_lambda(m)        # exponent >= 2^64 > log2(m): lift
    assert lm >= max(factorize(m).values())   # lift validity (m = 8, 24 fail)
    return pow(x, tower_mod(x, h - 1, lm) + lm, m)

# Validate against exact integer towers wherever they fit (~4M bits).
checked = 0
for x in range(2, 11):
    for h in range(0, 6):
        t = exact_tower(x, h)
        if t is None:
            continue
        for m in (12, 16, 30, 210, 240, N):
            assert tower_mod(x, h, m) == t % m
            checked += 1
print(f"tower_mod validated against exact integer towers: "
      f"{checked} cases (largest exact case 7^(7^7), a 2.3-Mbit integer)")

# Tetration is not a ring operation either (the type escape, level 4):
assert tower_mod(2, 2, 30) != tower_mod(32, 2, 30)   # 2 = 32 mod 30
print("type escape again: 2^^2 != 32^^2 mod 30 although 2 = 32 mod 30")
print()

# Stabilization: x^^h mod m is CONSTANT once h reaches the chain height
# (x >= 2; x = 0 alternates 1,0 by the 0^0 convention, x = 1 is fixed).
def stab_depth(x, m, hmax):
    vals = [tower_mod(x, h, m) for h in range(hmax + 1)]
    d = hmax
    while d > 0 and vals[d - 1] == vals[hmax]:
        d -= 1
    assert all(v == vals[hmax] for v in vals[d:])
    return d

for m in (30, 210):
    hh = len(lam_chain(m)) - 1
    worst = max(stab_depth(x, m, hh + 6) for x in range(2, 400))
    print(f"Z/{m}: every tower x^^h (2 <= x < 400) constant for "
          f"h >= {worst}; chain height {hh}")
    assert worst <= hh + 1
worst_rad = max(stab_depth(x, N, H_RAD + 6)
                for x in [random.randrange(2, 10 ** 9) for _ in range(150)])
print(f"RAD:   150 sampled bases, constant for h >= {worst_rad}; "
      f"chain height {H_RAD}")
assert worst_rad <= H_RAD + 1
print()
print(f"-> mod N a power tower has at most ~{H_RAD} distinguishable")
print("   depths: a super-logarithm of x^^h takes finitely many values.")
print("   Above x, the 'turn it into +' question dissolves -- there is")
print("   almost nothing left to coordinate. Crypto prices the residue:")
print("   the double discrete log g^(h^x) (Stadler 1996) is a HARDNESS")
print("   assumption -- the missing coordinate is a one-way function.")

# ----------------------------------------------------------------------
section("FINDINGS")
# ----------------------------------------------------------------------
fa0, fa1, fa2 = fa
print(f"""
1. TYPE ESCAPE (rule; exhaustive Z/30 + Z/210, 20k sampled at RAD).
   Powering is not a ring operation: x^y is ill-defined on residue
   pairs; it is well-defined as Z/N x Z/lambda(N) -> Z/N for exponents
   >= 1. The hyperoperation ladder exits the ring at the third rung --
   each further level lives one ring down the lambda-chain.

2. THREE GRADES OF EXISTENCE (rule, classical ingredients + census to
   10^6). The third log = an index transform on the index ring Z/(p-1):
   (A) single super-log iff Z/(p-1) cyclic (Gauss) -- RAD channels 13,
   17 FAIL; passing primes (p = 2q^k+1, safe-prime-like) thin toward
   density 0 (census {fa0:.3f} -> {fa1:.3f} -> {fa2:.3f}).
   (B) super-log through a second CRT split iff 8 does not divide p-1
   -- the unique non-cyclic prime-power unit group is U(2^k), k >= 3;
   density 3/4 (census matches Dirichlet); only p = 17 fails in RAD.
   (C) the 2-adic patch U(2^k) = <-1> x <5> always exists but is
   group-only: Z/2^k is local, no ring split carries it.
   Grade B's obstruction is entirely 2-ADIC -- odd places never block
   the second split; grade A also dies the level-1 way (lambda < phi:
   p = 31 fails with 8 not dividing 30).

3. SELF-SIMILARITY EXACTLY ON SKIP TOWERS (rule; iff validated
   m <= 300 + classical contact Mirsky). The full level-1 blueprint
   recurs at level 2 iff p-1 is squarefree: then Z/(p-1) is a designed
   tower (P38) and the two moves repeat verbatim. Otherwise nilpotents
   appear, x^(lambda+1) = x fails, and the graded log dies. Density of
   self-similar channels = Artin constant 0.374 (census-matched).
   RAD: self-similar at 2, 3, 7, 11; broken at 5, 13, 17.

4. THE LADDER IS THE PRATT TREE (classical contact, computed). The
   iterated-log recursion descends the Pratt certificate tree; the
   level-2 split is Pohlig-Hellman's decomposition. Lambda-chain of
   RAD: 510510 -> 240 -> 4 -> 2 -> 1 (height 4; iterated-lambda
   literature: Martin-Pomerance, Harland).

5. TETRATION COLLAPSES (rule; recursion validated against exact towers
   up to 7^(7^7), a 2.3-Mbit integer). x^^h mod N (any base x >= 2)
   is constant once h reaches the chain height: every sampled tower
   stabilizes by depth {worst_rad} at RAD (chain height {H_RAD}).
   Above x the hyperoperation ladder mod N is FINITE; a
   super-logarithm has almost no domain to act on.

6. THE THIRD WALL IS EXISTENCE (synthesis). Size wall = information
   obstruction (cross-channel, no table); Zech wall = structure
   obstruction (within-channel, incompressible table); super-log wall
   = the coordinate's domain dies -- 2-adically non-cyclic unit
   groups, nilpotent leakage off the squarefree locus, and a finite
   lambda-chain that exhausts the ladder. Napier's ladder has exactly
   two rungs on the tower; the third exists only channel-by-channel,
   generically degraded, and the object it would coordinate is
   already finite. (Stadler's double-DL assumption: the absence,
   priced.)
""")
