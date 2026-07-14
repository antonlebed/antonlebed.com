"""
Operation discovery: the SECOND log -- index coordinates.

explore_size_transform.py charted the first log: the CRT
map x -> residue tuple trivializes exactly the polynomial functions and
walls off size (the archimedean place). The tower has a SECOND log: per
channel, the discrete logarithm to a primitive root maps the unit group
F_p^* onto Z/(p-1), turning multiplication into channel-wise ADDITION
(the index transform -- Napier's move executed inside each field). This
script charts what THAT coordinate trades.

Survey anchors (standard material, named so nothing here poses as new):
Zech logarithms (the finite-field Gaussian logarithm; addition in log
coordinates via one unary table), index calculus (COMPUTING discrete
logs -- cost, not structure), the Discrete Logarithm Number System
(Mitchell, IEEE TC 2009 -- mult->add via discrete logs, but modulo 2^k:
one fat channel, no CRT stacking), and the real-number Logarithmic
Number System (the same trade at the archimedean place). The gap this
script fills: the index transform ON TOP of the squarefree tower -- the
composition story, the non-unit extension, the wall-shape comparison.

Findings preview (full statements at the bottom):
  1. THE SECOND LOG EXISTS ONLY THROUGH THE FIRST: for k >= 3 the unit
     group is non-cyclic (max order lambda < phi), so Z/N has no
     primitive root -- no single-modulus index transform exists. The
     composite U(Z/N) ~ prod Z/(p-1) is exact and lambda is its
     additive exponent.
  2. WHAT THE COMPOSITE TRIVIALIZES: multiplication -> channel-wise
     addition, powering -> scalar multiplication, multiplicative order
     -> per-channel gcd read, e-th-root existence/count -> per-channel
     divisibility, quadratic residuosity -> a coordinate projection.
  3. THE ZECH WALL HAS A DIFFERENT SHAPE THAN THE SIZE WALL: the index
     map recodes each channel independently (graded over non-units, so
     a channel-local bijection of the ring), and the locality
     criterion cannot see it -- addition stays tower-channel-local in
     index coordinates (one unary Zech table per channel). The wall is
     WITHIN the channel: Zech's logarithm is incompatible with EVERY
     nontrivial proper quotient of Z/(p-1) -- PROVED for every p >= 5
     and every divisor 2 <= q <= (p-1)/2, composite q included (the
     linear-fraction count below) -- hence not polynomial -- it
     resists structural compression, but costs only a (p-2)-entry
     table. Size: cross-channel, no table of any size. Zech:
     within-channel, one unary table. Different obstruction types.
  4. THE GRADED LOG: x^(lambda+1) = x for ALL x (exhaustive), so the
     multiplicative monoid is a commutative Clifford monoid -- the
     Boolean lattice of supports carrying the sub-rings' unit groups.
     The collapse x -> x^lambda = e_supp(x) IS the canonical
     grading; full log coordinate x <-> (supp, indices on supp);
     meadow inverse = index negation. "log 0 = -infinity" is realized
     structurally as grade drop.
  5. THE RIGIDITY DICHOTOMY: coordinates where + is channel-local =
     exactly the coprime factorizations (rigid -- the divisor lattice;
     adding x changes nothing). Coordinates where x alone is local =
     abelian regroupings of U(N), a strictly LARGER family (floppy --
     witnesses cross tower channels, which no +-local system can).
     No coordinate gives (+ local, x additive):
     the zero/idempotent grading obstructs. Each operation pair picks
     its home: (+,x) -> CRT, (x,^) -> index, (+,size) -> positional
     (sequential, the locality criterion's price (b)); all three at
     once: impossible.

THE PROOF (of the swept rule in finding 3): the classical route
considered was a compatible quotient forces every row of the q-th
cyclotomic-number matrix into one column, and all-positive cyclotomic
numbers (Jacobi sums) forbid that for p large; derive the bound. The
bound DISSOLVED: compatibility, read coset-side, says the ratio
(1 + wx)/(1 + x) lands in the index-q subgroup C for every w in C and
every x outside {0, -1, -1/w}; for fixed w != 1 that equation is
linear in x per target value c in C (c = w impossible, c = 1 gives
x = 0), so EXACTLY m - 2 of the p - 3 required x comply
(m = (p-1)/q), and m <= (p-1)/2 < p - 1 unconditionally. Elementary,
every p >= 5, every nontrivial proper quotient (the old claim: prime
q only, swept); primitive-root-free since only cosets of C appear.
Mechanical check: 263 (p,q) pairs (5 <= p < 200, ALL divisors
2 <= q <= (p-1)/2), complying-set = predicted-set verified as set
equality, witness pair violates in every case. The named heavy route
(Jacobi sums) was the verifier's shadow, not the fact's shape -- the
rule was a four-line count all along.

Runs on RAD (k=7) with exhaustive small-ring cross-checks. ~1 s, tiny
memory.
"""

import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import (Ring, RAD_RING, encode, idempotent, multiplicative_order,
                 mod_inverse, lcm_list)

random.seed(39)
R = RAD_RING
N = R.N
K = R.k
PRIMES = R.primes
LAM = R.lam
PHI = math.prod(p - 1 for p in PRIMES)

def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)

def primitive_roots(p):
    """All primitive roots mod p (p prime), smallest first."""
    roots = []
    for g in range(2, p):
        if multiplicative_order(g, p) == p - 1:
            roots.append(g)
    return roots if p > 2 else [1]

def index_table(p, g):
    """ind: F_p^* -> Z/(p-1) for primitive root g. p=2 -> {1: 0}."""
    tab, x = {}, 1
    for n in range(p - 1):
        tab[x] = n
        x = x * g % p
    return tab

GS  = [primitive_roots(p)[0] for p in PRIMES]          # smallest g per channel
IND = [index_table(p, g) for p, g in zip(PRIMES, GS)]

def to_index(x):
    """Unit x -> index tuple in prod Z/(p-1)."""
    return tuple(IND[i][x % p] for i, p in enumerate(PRIMES))

# ───────────────────────────────────────────────────────────────────────
section("I. THE SECOND LOG EXISTS ONLY THROUGH THE FIRST")
# ───────────────────────────────────────────────────────────────────────
# Napier's move on Z/N itself would need a primitive root mod N. None
# exists at any rung k >= 3: U(Z/N) = prod F_p^* has exponent
# lambda = lcm(p-1) < phi = prod(p-1) as soon as two channels share a
# factor (any two odd p share 2). The index transform is only available
# AFTER the CRT split -- the second log rides on the first.
for ring in (Ring("Z30", (2, 3, 5), (1, 1, 1)), R):
    phi_r = math.prod(p - 1 for p in ring.primes)
    print(f"{ring.name}: lambda = {ring.lam} < phi = {phi_r} "
          f"-> no primitive root mod {ring.N}")
    assert ring.lam < phi_r
assert LAM == lcm_list([p - 1 for p in PRIMES])  # = the index ring's exponent
print(f"lambda = lcm(p-1) = {LAM}: the additive exponent of the index "
      f"ring prod Z/(p-1).")

# The composite map: unit -> CRT tuple -> per-channel index. Exhaustive
# bijectivity at RAD: all phi(N) units hit distinct index tuples, and
# the tuple space has exactly phi(N) points.
units = [x for x in range(N) if math.gcd(x, N) == 1]
assert len(units) == PHI
images = set(to_index(x) for x in units)
assert len(images) == PHI == math.prod(p - 1 for p in PRIMES)
print(f"index map exhaustive at RAD: {len(images)} distinct tuples "
      f"= phi = {PHI}  (bijection VERIFIED)")

# Multiplication -> channel-wise addition: exhaustive at Z/210 (all
# 48^2 unit pairs), sampled 20k pairs at RAD.
R210 = Ring("Z210", (2, 3, 5, 7), (1, 1, 1, 1))
GS210 = [primitive_roots(p)[0] for p in R210.primes]
IND210 = [index_table(p, g) for p, g in zip(R210.primes, GS210)]
u210 = [x for x in range(210) if math.gcd(x, 210) == 1]
for a in u210:
    for b in u210:
        got = tuple(IND210[i][a * b % p] for i, p in enumerate(R210.primes))
        want = tuple((IND210[i][a % p] + IND210[i][b % p]) % (p - 1)
                     for i, p in enumerate(R210.primes))
        assert got == want
print(f"mul -> add exhaustive at Z/210: all {len(u210)}^2 = "
      f"{len(u210)**2} unit pairs VERIFIED")
for _ in range(20_000):
    a, b = random.choice(units), random.choice(units)
    got = to_index(a * b % N)
    want = tuple((x + y) % (p - 1) for x, y, p in
                 zip(to_index(a), to_index(b), PRIMES))
    assert got == want
print("mul -> add at RAD: 20k random unit pairs VERIFIED")

# ───────────────────────────────────────────────────────────────────────
section("II. WHAT THE COMPOSITE TRIVIALIZES (that neither log does alone)")
# ───────────────────────────────────────────────────────────────────────
# CRT alone makes multiplication channel-PARALLEL but each channel still
# multiplies. A single-modulus index doesn't exist (section I). The
# composite makes the unit group's whole multiplicative theory LINEAR:

# (a) powering x^e = scalar multiplication e * ind(x), channel-wise.
for _ in range(2_000):
    x, e = random.choice(units), random.randrange(1, 1000)
    got = to_index(pow(x, e, N))
    want = tuple((e * n) % (p - 1) for n, p in zip(to_index(x), PRIMES))
    assert got == want
print("(a) powering -> index scaling: 2k random (x, e) VERIFIED")

# (b) multiplicative order = a gcd READ: ord(x) = lcm_p (p-1)/gcd(ind_p, p-1).
#     Exhaustive over all 92160 units; the distribution must reproduce
#     the documented exhaustive table (verify_algebra.py::test_order_distribution).
from collections import Counter
order_of = {}
for x in units:
    o = 1
    for n, p in zip(to_index(x), PRIMES):
        ch = (p - 1) // math.gcd(n, p - 1)        # per-channel order
        o = o * ch // math.gcd(o, ch)             # lcm across channels
    order_of[x] = o
dist = Counter(order_of.values())
documented = {1: 1, 12: 3584, 48: 8192, 60: 14336, 120: 16384, 240: 32768}
for o, c in documented.items():
    assert dist[o] == c, (o, dist[o], c)
divisors240 = [d for d in range(1, 241) if 240 % d == 0]
assert sorted(dist) == [d for d in divisors240 if dist.get(d)]
assert len(dist) == 20 and sum(dist.values()) == PHI
sample = random.sample(units, 2_000)
assert all(multiplicative_order(x, N) == order_of[x] for x in sample)
print(f"(b) order = per-channel gcd read: exhaustive {PHI} units, "
      f"distribution matches the order census (all 20 divisors of 240, "
      f"primitives {dist[240]}); 2k direct cross-checks pass")

# (c) e-th roots: x is an e-th power iff gcd(e, p-1) | ind_p per channel;
#     an e-th power has prod_p gcd(e, p-1) roots. The iff is verified as
#     SET EQUALITY (both directions), exhaustively, for squares and cubes:
for e in (2, 3):
    g_e = [math.gcd(e, p - 1) for p in PRIMES]
    cond_set = set(x for x in units
                   if all(n % g == 0 for n, g in zip(to_index(x), g_e)))
    power_set = set(pow(x, e, N) for x in units)
    assert cond_set == power_set
    n_roots = math.prod(g_e)
    assert len(power_set) * n_roots == PHI
    print(f"(c) e={e}: {{x^{e}}} == {{index condition}} as SETS "
          f"({len(power_set)} e-th powers x {n_roots} roots each = {PHI})")

# (d) quadratic residuosity = ONE BIT of the coordinate: x is a QR mod p
#     iff ind_p(x) is even. (Already channel-local in CRT coordinates as
#     x^((p-1)/2) -- the second log turns an evaluation into a projection.)
for _ in range(2_000):
    x = random.choice(units)
    for i, p in enumerate(PRIMES[1:], 1):
        qr = pow(x % p, (p - 1) // 2, p) == 1
        assert qr == (to_index(x)[i] % 2 == 0)
print("(d) QR per channel = index parity bit: 2k random units VERIFIED")
print()
print("    None of (a)-(d) is available from one log alone: CRT alone")
print("    leaves within-channel multiplication nonlinear; a single-")
print("    modulus index does not exist (no primitive root, section I).")

# ───────────────────────────────────────────────────────────────────────
section("III. THE ZECH WALL -- and why it is NOT the size wall")
# ───────────────────────────────────────────────────────────────────────
# In index coordinates addition is the hard operation. But first, what
# the locality criterion says: the index map recodes each channel
# INDEPENDENTLY (units here; the section-IV graded coordinate extends
# the recode to all of Z/p, since addition is not closed on units), so
# it is a channel-local bijection of the ring -- and channel-local
# bijections cannot change which functions are channel-local (the
# locality criterion's survival argument). So tower addition REMAINS
# tower-channel-local in (graded) index coordinates -- the Zech wall
# cannot be a cross-channel
# locality obstruction. It lives WITHIN the channel:
#
#   ind(g^a + g^b) = a + Z(b - a),   Z(n) := ind(1 + g^n)
#
# -- one subtraction, one unary table Z (Zech's logarithm), one
# addition. Addition leaves the units exactly once: 1 + g^n0 = 0 at
# n0 = ind(-1) -- the grade-drop point (section IV picks this up).
# The wall question, stated as explore_size_transform.py stated it: does Z itself carry
# structure -- is it a polynomial on Z/(p-1)? A polynomial is compatible
# with EVERY quotient (a = b mod q => f(a) = f(b) mod q). Test every
# prime quotient q | p-1, every channel.
print("channel   q | p-1   compatible pairs   violations   verdict")
for i, p in enumerate(PRIMES):
    if p == 2:
        continue                                   # F_2^*: nothing to add
    g = GS[i]
    ind = IND[i]
    n0 = ind[p - 1]                                # ind(-1) = (p-1)/2
    assert n0 == (p - 1) // 2
    Z = {n: ind[(1 + pow(g, n, p)) % p] for n in range(p - 1) if n != n0}
    dom = sorted(Z)
    if p == 3:
        print(f"  p=3     (domain has one point -- vacuous)")
        continue
    for q in sorted(set(f for f in range(2, p) if (p - 1) % f == 0
                        and all(f % d for d in range(2, f)))):
        ok = viol = 0
        for ai in range(len(dom)):
            for bi in range(ai + 1, len(dom)):
                a, b = dom[ai], dom[bi]
                if (a - b) % q == 0:
                    if (Z[a] - Z[b]) % q == 0:
                        ok += 1
                    else:
                        viol += 1
        verdict = "INCOMPATIBLE" if viol else "compatible"
        print(f"  p={p:<3}   q={q:<2}      {ok:<16} {viol:<12} {verdict}")
        assert viol > 0, (p, q)
print()
print("    Z is incompatible with EVERY nontrivial proper quotient of")
print("    Z/(p-1), every p >= 5 -- not a polynomial on Z/(p-1) (polynomial =>")
print("    compatible holds in any modulus). PROVED, elementarily:")
print("    read coset-side, the residue classes of indices mod q are the")
print("    cosets of the index-q subgroup C <= F_p^* (m = (p-1)/q")
print("    elements), and compatibility says (1 + wx)/(1 + x) lands in C")
print("    for EVERY w in C and every x in F_p^* outside {-1, -1/w}. But")
print("    1 + wx = c(1 + x) is LINEAR in x: c = w forces w = 1, c = 1")
print("    forces x = 0, and every other c gives exactly one x -- so for")
print("    a fixed w != 1, EXACTLY m - 2 of the p - 3 required x comply,")
print("    and m <= (p-1)/2 < p - 1 always. Every other x is a witness:")
print("    a = ind(x), b = ind(wx) has a = b (mod q), Z(a) != Z(b)")
print("    (mod q). Holds for every p >= 5 and every divisor q with")
print("    2 <= q <= (p-1)/2 -- COMPOSITE q included -- and is primitive-")
print("    root-free (the condition only mentions cosets of C). The")
print("    cyclotomic-number route (Jacobi sums, 'for p large') was")
print("    never needed; no bound to derive.")
# Mechanical verification of every step of the proof: every prime
# 5 <= p < 200, every divisor 2 <= q <= (p-1)/2 of p-1 (the old sweep
# covered prime q only; the proof covers all, so the check does too).
swept = tight = 0
for p in [n for n in range(5, 200) if all(n % d for d in range(2, n))]:
    g = primitive_roots(p)[0]
    ind = index_table(p, g)
    n0 = ind[p - 1]
    Z = {n: ind[(1 + pow(g, n, p)) % p] for n in range(p - 1) if n != n0}
    for q in [d for d in range(2, (p - 1) // 2 + 1) if (p - 1) % d == 0]:
        m = (p - 1) // q
        omega = pow(g, q, p)                       # a non-1 element of C
        C = set(pow(g, q * j, p) for j in range(m))
        assert len(C) == m and m >= 2 and omega in C and omega != 1
        # the proof's solution set: one x per c in C \ {1, omega}
        sols = set((c - 1) * pow((omega - c) % p, p - 2, p) % p
                   for c in C if c not in (1, omega))
        assert len(sols) == m - 2                  # all distinct, as proved
        # cross-check against the compatibility condition directly:
        # the complying x are EXACTLY the proof's solution set
        excl = {0, p - 1, -pow(omega, p - 2, p) % p}
        comply = set(x for x in range(1, p) if x not in excl
                     and (1 + omega * x) * pow((1 + x) % p, p - 2, p) % p in C)
        assert comply == sols and not (sols & excl)
        assert p - 3 > m - 2                       # the deficit, always > 0
        # any other x gives the violating Zech pair of the claim:
        wit = next(x for x in range(1, p) if x not in excl and x not in sols)
        a, b = ind[wit], ind[omega * wit % p]
        assert (a - b) % q == 0 and a != n0 and b != n0
        assert (Z[a] - Z[b]) % q != 0, (p, q, wit)
        swept += 1
        tight += (len(comply) == m - 2 > 0)
print(f"    Proof verified mechanically: all primes 5 <= p < 200, every")
print(f"    divisor 2 <= q <= (p-1)/2 ({swept} (p,q) pairs, composite q")
print(f"    included): complying x's = exactly m-2 (cap attained with")
print(f"    m-2 > 0 in {tight} pairs), witness pair violates, every case.")
print()
print("    SHAPE COMPARISON. Size wall: CROSS-channel, an")
print("    information obstruction -- no per-channel data of any size")
print("    computes sign; survives every transform. Zech wall: WITHIN-")
print("    channel, a structure obstruction -- addition needs one unary")
print(f"    table per channel (total {sum(p - 2 for p in PRIMES if p > 2)}"
      f" entries at RAD vs the size")
print("    wall's 'no table exists'), and the table is structureless:")
print("    not polynomial, no quotient compression. Different walls.")

# ───────────────────────────────────────────────────────────────────────
section("IV. THE GRADED LOG: non-units, the collapse x^lambda as grading")
# ───────────────────────────────────────────────────────────────────────
# Non-units have no index. The canonical extension: x^(lambda+1) = x for
# ALL x on a squarefree ring (per channel: x_p = 0 stays 0; x_p != 0 has
# x_p^lambda = 1). Exhaustive at RAD:
assert all(pow(x, LAM + 1, N) == x for x in range(N))
print(f"x^(lambda+1) = x for all {N} elements (exhaustive) -- the")
print("multiplicative monoid is COMPLETELY REGULAR: a commutative")
print("Clifford monoid (classically: a semilattice of groups; here")
print("the semilattice is the Boolean lattice of supports).")
# The grading map is the collapse x -> x^lambda = e_supp(x); the
# grade-S group is e_S * U = the unit group of the S-SUB-RING -- the
# sub-ring lattice (census threads) IS the Clifford skeleton.
for _ in range(5_000):
    x = random.randrange(N)
    S = frozenset(i for i, r in enumerate(encode(x, R)) if r != 0)
    assert pow(x, LAM, N) == idempotent(S, R)
print("grade(x) = x^lambda = e_supp(x): 5k random x VERIFIED (collapse map)")

# Full log coordinate: x <-> (supp(x), (ind_p(x_p))_{p in supp}).
# Multiplication = intersect supports, add indices on the intersection.
# Exhaustive at Z/210 (all 210^2 pairs):
def graded_log(x, primes, inds):
    supp, idx = [], []
    for i, p in enumerate(primes):
        r = x % p
        if r:
            supp.append(i)
            idx.append(inds[i][r])
    return tuple(supp), tuple(idx)

for a in range(210):
    for b in range(210):
        sa, ia = graded_log(a, R210.primes, IND210)
        sb, ib = graded_log(b, R210.primes, IND210)
        want_s = tuple(i for i in sa if i in sb)
        da, db = dict(zip(sa, ia)), dict(zip(sb, ib))
        want_i = tuple((da[i] + db[i]) % (R210.primes[i] - 1) for i in want_s)
        assert graded_log(a * b % 210, R210.primes, IND210) == (want_s, want_i)
print("graded multiplication exhaustive at Z/210: all 44100 pairs")
print("(supports intersect, indices add on the intersection) VERIFIED")
for _ in range(10_000):
    a, b = random.randrange(N), random.randrange(N)
    sa, ia = graded_log(a, PRIMES, IND)
    sb, ib = graded_log(b, PRIMES, IND)
    want_s = tuple(i for i in sa if i in sb)
    da, db = dict(zip(sa, ia)), dict(zip(sb, ib))
    want_i = tuple((da[i] + db[i]) % (PRIMES[i] - 1) for i in want_s)
    assert graded_log(a * b % N, PRIMES, IND) == (want_s, want_i)
print("graded multiplication at RAD: 10k random pairs VERIFIED")

# The meadow inverse in log coordinates = grade-preserving index
# NEGATION: x^- has the same support, inverse residues there.
def meadow_inv(x, ring):
    t = [mod_inverse(r, p) if r else 0
         for r, p in zip(encode(x, ring), ring.primes)]
    n = 0
    for r, (p, c) in zip(t, zip(ring.primes, ring.crt_coefficients)):
        n = (n + r * c) % ring.N
    return n

for x in range(210):
    y = meadow_inv(x, R210)
    assert x * y * x % 210 == x and y * x * y % 210 == y
    sx, ix = graded_log(x, R210.primes, IND210)
    sy, iy = graded_log(y, R210.primes, IND210)
    assert sx == sy and all((a + b) % (R210.primes[i] - 1) == 0
                            for a, b, i in zip(ix, iy, sx))
print("meadow inverse = index negation: exhaustive at Z/210 VERIFIED")
print()
print("    'log 0 = -infinity' is realized STRUCTURALLY: addition's one")
print("    exit from the units (1 + g^n0 = 0, section III) is a grade")
print("    drop in the Boolean lattice. The second log extends to the")
print("    whole ring as (grade, index) -- and the collapse is the")
print("    canonical projection onto the grade.")

# ───────────────────────────────────────────────────────────────────────
section("V. THE RIGIDITY DICHOTOMY: + is rigid, x is floppy")
# ───────────────────────────────────────────────────────────────────────
# Question 4: with three charted coordinates (positional, CRT,
# index), which operation-pairs can be simultaneously local? The
# backbone is a decomposition fact, checked exhaustively at k=3.
#
# A coordinate system in which an operation is channel-local = a
# bijection to a product of components under which the operation acts
# component-wise; the component operations inherit the laws pointwise.
# For + this is exactly a direct-sum decomposition of the group (Z/N,+).
add_subgroups = [frozenset(range(0, 30, d)) for d in range(1, 31)
                 if 30 % d == 0]                    # all subgroups (cyclic)

def direct_sums(subgroups, op, size, identity):
    """All unordered tuples of >=2 nontrivial subgroups whose op-sum is
    bijective onto the full group."""
    nontriv = [H for H in subgroups if 1 < len(H) < size]
    found = []
    import itertools
    for t in (2, 3):
        for combo in itertools.combinations(nontriv, t):
            if math.prod(len(H) for H in combo) != size:
                continue
            elems = set()
            for tup in itertools.product(*combo):
                acc = identity
                for h in tup:
                    acc = op(acc, h)
                elems.add(acc)
            if len(elems) == size:
                found.append(combo)
    return found

adds = direct_sums(add_subgroups, lambda a, b: (a + b) % 30, 30, 0)
print(f"(Z/30, +): {len(adds)} direct decompositions -- exactly the")
for combo in adds:
    print("   ", " (+) ".join(f"|H|={len(H)}" for H in combo))
assert len(adds) == 4              # {2,15},{3,10},{5,6},{2,3,5}: the
                                   # nontrivial partitions of {2,3,5}
print("    nontrivial coprime factorizations of 30 = partitions of the")
print("    prime set. (Standard: a finite cyclic group decomposes ONLY")
print("    into coprime cyclic pieces.) + is RIGID: demanding + local")
print("    already pins the coordinates to the divisor lattice; adding")
print("    x to the demand changes nothing (components inherit the ring")
print("    laws pointwise; ring decompositions = the same partitions,")
print("    via central idempotents). The archimedean wall is")
print("    therefore unavoidable in EVERY +-local coordinate system.")
print()
# Multiplication alone is floppier: U(30) = C2 x C4 (8 elements).
u30 = [x for x in range(30) if math.gcd(x, 30) == 1]
mul_subgroups = []
for mask in range(1, 1 << len(u30)):
    S = frozenset(u30[i] for i in range(len(u30)) if mask >> i & 1)
    if 1 in S and all(a * b % 30 in S for a in S for b in S):
        mul_subgroups.append(S)
muls = direct_sums(mul_subgroups, lambda a, b: a * b % 30, len(u30), 1)
def aligned(H):
    """Channel-aligned iff H = product of its channel projections."""
    return len(H) == math.prod(len(set(h % p for h in H)) for p in (3, 5))
n_aligned = sum(all(aligned(H) for H in combo) for combo in muls)
print(f"(U(30), x): {len(mul_subgroups)} subgroups, {len(muls)} direct")
print(f"    decompositions, of which {n_aligned} channel-aligned. Witness")
for combo in muls:
    if not all(aligned(H) for H in combo):
        parts = [f"{{{', '.join(map(str, sorted(H)))}}}" for H in combo]
        print(f"    (crosses tower channels): {' x '.join(parts)}")
        break
assert len(muls) == 4 and n_aligned == 1
# The cross-channel mechanism at RAD scale: the primary (Sylow)
# regrouping gathers each prime's part across ALL channels. The
# 2-primary component of U(RAD) has order prod 2part(p-1) = 2^11:
two_part = math.prod(p - 1 & -(p - 1) for p in PRIMES)   # lowest set bit
n_2power = sum(1 for x in units if order_of[x] & (order_of[x] - 1) == 0)
assert two_part == 2048 == n_2power and PHI == 2048 * 45
print(f"    At RAD the same floppiness is the Sylow regrouping: "
      f"{n_2power} units")
print("    of 2-power order form ONE 2-group component gathering the")
print("    2-parts of all seven channels (92160 = 2^11 * 45).")
print()
print("    THE CAPSTONE. No coordinate makes + local AND x additive:")
print("    on the full ring, x has the absorbing zero and the idempotent")
print("    grading (section IV) -- not a group operation; on the units,")
print("    + exits the units (grade drop), so no unit coordinate can")
print("    carry it. Each pair picks its home, and the homes differ:")
print("      (+, x)    -> CRT coordinates (unique up to regrouping)")
print("      (x, ^)    -> index coordinates (one of many regroupings)")
print("      (+, size) -> positional/mixed-radix (sequential -- the")
print("                   the size-wall escape (b) price, not channel-local)")
print("      (+, x, size) or (+, x-as-addition): NO common home.")

# ───────────────────────────────────────────────────────────────────────
section("FINDINGS")
# ───────────────────────────────────────────────────────────────────────
print("""
1. NO SINGLE-MODULUS INDEX (property). lambda = lcm(p-1) < phi at every
   rung k >= 3, so Z/N has no primitive root: Napier's move on the ring
   exists only THROUGH the CRT split. The index map U(Z/N) ->
   prod Z/(p-1) is a bijection (exhaustive at RAD, 92160 tuples) and
   lambda is precisely the index ring's additive exponent.

2. THE COMPOSITE'S CLONE (rule -- standard per-field facts, verified
   tower-wide). Two stacked logs turn the unit group's multiplicative
   theory linear: mul -> channel-wise add (exhaustive Z/210, 20k RAD
   pairs), powering -> index scaling, multiplicative order -> per-
   channel gcd read (exhaustive: reproduces the order
   distribution, all 20 divisors of 240), e-th-root existence and
   count -> per-channel divisibility (squares: 1440 x 64 = 92160),
   QR -> index parity projection.

3. THE ZECH WALL (rule, PROVED; shape comparison is the
   new content). The index map recodes each channel independently (the
   graded coordinate of finding 4 covers the non-units, making it a
   channel-local bijection of the RING), so the locality criterion is BLIND
   to it: addition stays tower-channel-local (per-channel cost = one
   unary Zech table, 44 entries total at RAD). The wall lives within
   the channel: Zech's logarithm is incompatible with every nontrivial
   proper quotient of Z/(p-1) -- proved for every p >= 5 and every
   divisor 2 <= q <= (p-1)/2, composite q included,
   primitive-root-free, by the linear-fraction count (exactly m - 2 of
   p - 3 required x can comply; mechanical check 263 (p,q) pairs) --
   hence not polynomial:
   a STRUCTURE obstruction (the table resists compression), not the
   size wall's INFORMATION obstruction (no table exists at all).
   Different shapes: hunt 1's wall is cross-channel locality; hunt 2's
   wall is within-channel structurelessness.

4. THE GRADED LOG (rule + classical contact). x^(lambda+1) = x for all
   510510 RAD elements (exhaustive): the multiplicative monoid is a
   commutative Clifford monoid -- the Boolean support lattice carrying
   the sub-rings' unit groups (the census threads' sub-ring lattice IS
   the Clifford skeleton). Full log coordinate x <-> (supp, indices);
   multiplication = intersect + add (exhaustive Z/210, 10k RAD);
   meadow inverse = index negation (exhaustive Z/210). The collapse
   x^lambda = e_supp(x) is the canonical grading map, and 'log 0 =
   -infinity' is the grade drop at 1 + g^(ind(-1)) = 0.

5. THE RIGIDITY DICHOTOMY (rule at k=3 exhaustive + standard
   ingredients; the operations-are-coordinates chart is the
   observation). Coordinates with + channel-local = coprime
   factorizations ONLY (exhaustive at Z/30: 4 = the partitions of
   {2,3,5}); adding x changes nothing. Coordinates with x alone local
   form a strictly LARGER family -- not in count (U(30) also has 4
   direct decompositions) but by containment: 3 of the 4 cross tower
   channels, which no +-local system can; at RAD the Sylow regrouping
   gathers all channels' 2-parts into one 2^11 component. Addition is RIGID (pins the divisor
   lattice -- and with it the archimedean wall), multiplication is
   FLOPPY (free regrouping -- and with it the Zech wall). No coordinate
   system hosts (+ local, x additive) or (+, x, size) together: every
   coordinate choice picks which operation pays.
""")
print("ALL ASSERTIONS PASSED")
