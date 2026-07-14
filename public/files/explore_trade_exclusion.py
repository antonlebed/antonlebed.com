"""
The trade-exclusion, closed.

The orbit-cost law's last open piece (explore_orbit_cost.py
P4): could a program trade coset gates for EXTRA separators (repeated-
or composite-modulus covering systems) and beat m(C) + omega(d)? Known:
excluded whenever m(C) = 1 (the cover bound alone), excluded by
exhaustive census on an earlier battery (L <= 3, d in {5,6,30}, p <= 61),
open in general. This session: PROVED in general -- and the proof never
uses the leaf structure: it holds for ANY finite abelian ambient group
V, any cyclic C = <c> of order d >= 2, gates = character kernels.

THE THEOREM (the trade-exclusion; with the canonical upper bound the
orbit-cost law is exact, both directions, general):
    any decider of O (the generators of C) costs t + s >= m(C) + omega(d).

PROOF (7 steps; each verified mechanically below).
 0. Decider == {z in S' : psi_i(z) != 0 for all separators} = O, where
    S' = intersection of the trivial kernels. Everything happens in S'.
 1. Duality bookkeeping: m(C) = rank(V/C); t >= rank(V/S'); socle
    subadditivity rank_p(V/C) <= rank_p(V/S') + rank_p(S'/C) at every
    prime. At a prime p* achieving rank(V/C): m <= t + r*,
    r* = rank_{p*}(S'/C). Suffices: s >= omega(d) + r*.
 2. Within-C forcing (the old P2): the zero coset pins every class to
    0 mod e_i; position q*w (w a unit) then needs e_i | qw, so
    e_i = q: one separator per prime q | d, omega(d) forced.
 3. Torsion localization: a coset of prime order p with p NOT | d has
    every separator class PINNED through one point (p is invertible
    mod every e_i; p*delta_i == -a mod e_i with the same a for all i),
    so position u0 + 1 is uncovered: S'/C has torsion only at primes
    dividing d.
 4. del = 0: for p | d, an order-p coset whose connecting value a has
    p NOT | a is uncoverable the same way (p | e_i separators cannot
    meet it at all; the rest are pinned). So every socle element lifts
    to an order-p element: the p-socle SPLITS, U ~ F_p^{r_p} with
    additive order-p lifts.
 5. lambda-linearization: on a socle coset (lift x, px = 0), psi_i(x)
    has order | p, so each separator's kill class delta_i(y) (the
    unique solution of delta * psi_i(c) = -psi_i(x) mod e_i) lies in
    (e_i/p)Z mod e_i when p | e_i, and is 0 when p does not divide
    e_i. A UNIT position u == delta_i then forces f_i | u (f_i the
    p'-part of e_i) and p^{beta-1} | u: unit positions of socle
    cosets are covered ONLY by e_i = p separators, whose class mod p
    is lambda_i(y) -- a LINEAR functional of y. Units mod d realize
    every nonzero class mod p, so every y != 0 needs
    {lambda_i(y) : e_i = p} >= F_p^* -- all p - 1 values.
 6. Covering rigidity: (a) p >= 3: nonzero lambdas need zero common
    kernel (#I_p >= r); at exactly r they form a basis and the
    preimage of the all-2s vector misses the value 1: #I_p >= r + 1.
    (b) p = 2: odd positions force some lambda_i(y) = 1 (e = 2);
    positions 2w (w a unit) admit exactly two coverer species --
    {e = 2, lambda = 0} or {e = 4, class 2 mod 4} (the latter only
    when 4 | d). No e=4 extra: both values needed from I_2 alone, and
    the all-ones vector kills #I_2 = r: #I_2 >= r + 1. An e=4 extra
    is itself a (+1) outside I_2 and the odd forced set. Either way
    the even separators number >= r + 1.
 7. Stitch: s >= (omega - 1) [forced at the primes != p*, step 2]
    + (r* + 1) [step 6 at p*; e-values 2, 4, or p* -- disjoint from
    the other forced primes] = omega + r*, and t >= m - r*:
    total >= m + omega. QED.
    (If p* NOT | d then r* = 0 by step 3 and t >= m directly.)

The piece the earlier per-coset arithmetic could not see: the {2,3,3}-style
trades pass every SINGLE-coset mass test, but the classes are linear
ACROSS cosets (step 5), and fewer than rank + 1 linear functionals
cannot serve every coset (step 6). The exclusion is a covering-rigidity
fact one level above the covering system.

PREDICTIONS (stated before the run):
 PR1 (rule): off-d-torsion cosets are uncoverable even by the union of
     ALL separators at once (testbed Z/6 x Z/5); the split-case control
     coset (Z/2 x Z/2) IS coverable -- the lemma kills exactly the
     off-d cosets, nothing more.
 PR2 (rule): del != 0 cosets are uncoverable likewise (Z/4 over <2>;
     Z/9 over <3>).
 PR3 (rule): on socle cosets, unit-position coverers have e = p
     exactly, and the covered class is one residue mod p, linear in y
     (testbeds Z/6 x Z/3 at p = 3; Z/12 x Z/2 at p = 2 including the
     e = 4 species for positions 2w).
 PR4 (rule): the abstract functional bound: no family of <= r
     functionals on F_p^r attains all required values on every
     nonzero point; exhaustive censuses at (p, r) = (2,1), (2,2),
     (2,3), (3,1), (3,2) -- true minima reported, all >= r + 1.
 PR5 (rule at these configs): end-to-end adversarial censuses on
     configs BEYOND the earlier battery, sized so a trade would fit under
     the law: (Z/2)^4 / <e1> (m=3, law 4): all <= 3-gate families
     fail; Z/6 x Z/3 x Z/3 / <(1,1,1)> (m=2, d=6, law 4; a rank-2
     3-socle -- exactly where a {2,3,3} trade would live): all
     <= 3-gate families fail; Z/12 x Z/2 x Z/2 / <(3,0,0)> (m=2,
     d=4, law 3; the e=4 species live): all <= 2-gate families fail.
 PR6 (property): the canonical program meets the law on every PR5
     config (upper bound tight; the law is exact there).
 PR7 (rule at this config; predictions stated before the run):
     the species analysis at its
     most delicate regime, alpha = v_2(d) = 3 (Z/24 x Z/2 x Z/2 over
     <(3,0,0)>, d = 8, m = 2, law 3; e in {2,4,8} separators
     coexist): unit-position coverers still e = 2 only; 2w-position
     coverers still {e=2} u {e=4, 2 mod 4} (e=8 classes are 0 or 4
     mod 8 -- they reach only the 4w positions); no <= 2-gate family
     decides; canonical ties at 3.

RESULTS (run record below; all predictions landed):
  I    m(C) == rank(V/C) at all four config testbeds (duality leg).
  II   PR1/PR2: all claimed-uncoverable cosets uncoverable; the
       split-case control coset coverable (the lemma is sharp).
  III  PR3: unit-coverers e = p exactly at both testbeds; every e=p
       separator's class map on the whole p-torsion subgroup G[p] is
       total, single-residue, additive; the 2w species at Z/12 x Z/2
       exactly {e=2} u {e=4, 2 mod 4}, both species occurring.
  IV   PR4 true minima: (2,1) 2, (2,2) 3, (2,3) 4, (3,1) 2, (3,2) 4
       -- every one >= r + 1 (the proof's bound; (3,2) shows the
       Jamison-sharp r(p-1) the proof does not need).
  V    PR5 censuses: (Z/2)^4: all 575 families of <= 3 of 15 shadows
       fail. Z/6x3x3: all 3,303 families of <= 3 of 27 shadows fail.
       Z/12x2x2: all 276 families of <= 2 of 23 shadows fail. PR7:
       Z/24x2x2: all 496 families of <= 2 of 31 shadows fail, and
       the alpha = 3 species landed exactly as predicted (unit
       coverers {2}; 2w coverers {2, 4}, the 4s at 2 mod 4). No
       trade anywhere; minima = law.
  VI   PR6: canonical programs decide O at m + omega on all four.
  VII  duality spot-check: t >= rank(V/S') over every trivial-kernel
       subset of size <= 2 at config B.

Tier: the trade-exclusion is PROVED (steps 0-7 general, no computation
at specific values; the script is verification, not evidence). With
explore_orbit_cost.py P1 (canonical upper bound, proved any L) the
orbit-cost law reads cost = m(C) + omega(d) exactly -- proved both
directions for every finite abelian ambient, every cyclic orbit:
a THEOREM under the naming ladder (complete general proof, no
computation at specific values -- the repo's first minted use).

Classical contacts: covering systems (Erdos) -- steps 3-6 say the
kernel-realizable covering systems are affine-linear families, and
those never cover; Jamison / Brouwer-Schrijver hyperplane covers of
F_p^r minus 0 -- step 6's sharp form (r(p-1) per nonzero value); B.H.
Neumann's lemma is the ambient qualitative cousin.

Runs standalone, stdlib only. ~10 s, tiny memory.
ALL CHECKS PASSED (27).
"""

import sys
from itertools import product, combinations
from math import gcd
from functools import reduce

CHECKS = [0]
def check(name, ok):
    CHECKS[0] += 1
    print(("  [OK] " if ok else "  [FAIL] ") + name)
    if not ok:
        sys.exit("CHECK FAILED: " + name)

def lcm2(a, b): return a * b // gcd(a, b)

def prime_factors(n):
    out, q = [], 2
    while q * q <= n:
        if n % q == 0:
            out.append(q)
            while n % q == 0: n //= q
        q += 1
    if n > 1: out.append(n)
    return out

class Grp:
    """Finite abelian group as a product of cyclic groups Z/m_j.
    Characters are indexed by the same tuples: chi_a(x) =
    sum a_j (M/m_j) x_j in Z/M, M = lcm(m_j)."""
    def __init__(self, ms):
        self.ms = tuple(ms)
        self.M = reduce(lcm2, ms, 1)
        self.w = [self.M // m for m in ms]
        self.elems = [tuple(t) for t in product(*[range(m) for m in ms])]
        self.zero = tuple(0 for _ in ms)
    def add(self, x, y):
        return tuple((a + b) % m for a, b, m in zip(x, y, self.ms))
    def smul(self, k, x):
        return tuple((k * a) % m for a, m in zip(x, self.ms))
    def chi(self, a, x):
        return sum(aj * wj * xj for aj, wj, xj in zip(a, self.w, x)) % self.M
    def order(self, x):
        o, y = 1, x
        while y != self.zero:
            y = self.add(y, x); o += 1
        return o
    def kernels(self):
        """Distinct character kernels (gate shadows), the whole dual."""
        seen = {}
        for a in self.elems:
            K = frozenset(x for x in self.elems if self.chi(a, x) == 0)
            seen.setdefault(K, a)
        return seen  # kernel -> one representing character

def orbit_setup(G, c):
    d = G.order(c)
    Cset = frozenset(G.smul(u, c) for u in range(d))
    O = frozenset(G.smul(u, c) for u in range(d) if gcd(u, d) == 1)
    return d, Cset, O

def restriction_order(G, K, Cset, d):
    return d // sum(1 for x in Cset if x in K)

def quotient_rank(G, Cset):
    """rank(G/C) = max_p dim_p of the p-socle of G/C."""
    reps, coset_id = [], {}
    for z in G.elems:
        if z in coset_id: continue
        i = len(reps); reps.append(z)
        for x in Cset:
            coset_id[G.add(z, x)] = i
    nq = len(reps)
    best = 0
    for p in prime_factors(nq):
        np_ = sum(1 for z in reps if G.smul(p, z) in Cset)
        dim = 0
        while p ** dim < np_: dim += 1
        best = max(best, dim)
    return best

def m_of_C(G, kernels, Cset, cap=4):
    """Exhaustive: min number of trivial kernels intersecting to C."""
    triv = [K for K in kernels if Cset <= K]
    for size in range(1, cap + 1):
        for fam in combinations(triv, size):
            inter = set(G.elems)
            for K in fam: inter &= K
            if frozenset(inter) == Cset:
                return size
    return None

def decides(G, fam, c, Cset, O):
    triv = [K for K in fam if c in K]
    seps = [K for K in fam if c not in K]
    acc = frozenset(z for z in G.elems
                    if all(z in K for K in triv)
                    and all(z not in K for K in seps))
    return acc == O

def census_min(G, kernels, c, Cset, O, maxsize):
    """Smallest deciding family among all <= maxsize-subsets of the
    nontrivial shadows; returns (min or None, families tested)."""
    shadows = [K for K in kernels if len(K) < len(G.elems)]
    tested = 0
    for size in range(1, maxsize + 1):
        for fam in combinations(shadows, size):
            tested += 1
            if decides(G, fam, c, Cset, O):
                return size, tested
    return None, tested

def coset_coverable(G, kernels, c, Cset, y):
    """Can the coset y + C be fully covered by the union of ALL
    separator slices at once? (The outer bound on any program.)"""
    coset = {G.add(y, x) for x in Cset}
    seps = [K for K in kernels if c not in K]
    covered = set()
    for K in seps:
        covered |= (coset & K)
    return covered == coset

print("=" * 72)
print("THE TRADE-EXCLUSION, CLOSED: mechanical verification")
print("=" * 72)

# ---------------------------------------------------------------- I
print("\nI. Duality leg: m(C) == rank(V/C) on the config testbeds")
CONFIGS = [
    ("A  (Z/2)^4   / <e1>      d=2", Grp([2, 2, 2, 2]), (1, 0, 0, 0)),
    ("B  Z/6x3x3   / <(1,1,1)> d=6", Grp([6, 3, 3]), (1, 1, 1)),
    ("C  Z/12x2x2  / <(3,0,0)> d=4", Grp([12, 2, 2]), (3, 0, 0)),
    ("D  Z/6x5     / <(1,0)>   d=6", Grp([6, 5]), (1, 0)),
    ("E  Z/24x2x2  / <(3,0,0)> d=8", Grp([24, 2, 2]), (3, 0, 0)),
]
setup = {}
for name, G, c in CONFIGS:
    d, Cset, O = orbit_setup(G, c)
    kers = G.kernels()
    m = m_of_C(G, kers, Cset)
    r = quotient_rank(G, Cset)
    setup[name[0]] = (G, c, d, Cset, O, kers, m)
    print(f"   {name}: |V|={len(G.elems)}, d={d}, m(C)={m}, rank(V/C)={r}")
    check(f"S1{name[0].lower()}: m(C) == rank(V/C) at config {name[0]}", m == r)

# ---------------------------------------------------------------- II
print("\nII. Pinning lemmas (PR1 torsion localization, PR2 del != 0)")
G, c, d, Cset, O, kers, _ = setup["D"]
bad = [y for y in G.elems if y not in Cset]
reps, seen = [], set()
for y in bad:
    key = frozenset(G.add(y, x) for x in Cset)
    if key not in seen:
        seen.add(key); reps.append(y)
check("S2a: PR1 every off-d coset of Z/6x5 uncoverable by ALL separators",
      all(not coset_coverable(G, kers, c, Cset, y) for y in reps))

G4 = Grp([4]); c4 = (2,)
d4, C4, O4 = orbit_setup(G4, c4)
k4 = G4.kernels()
check("S2b: PR2 the odd coset of Z/4 over <2> uncoverable (del != 0)",
      not coset_coverable(G4, k4, c4, C4, (1,)))
G9 = Grp([9]); c9 = (3,)
d9, C9, O9 = orbit_setup(G9, c9)
k9 = G9.kernels()
check("S2c: PR2 both nonzero cosets of Z/9 over <3> uncoverable",
      not coset_coverable(G9, k9, c9, C9, (1,)) and
      not coset_coverable(G9, k9, c9, C9, (2,)))
G22 = Grp([2, 2]); c22 = (1, 0)
d22, C22, O22 = orbit_setup(G22, c22)
k22 = G22.kernels()
check("S2d: control -- the split-case coset of Z/2xZ/2 IS coverable",
      coset_coverable(G22, k22, c22, C22, (0, 1)))

# ---------------------------------------------------------------- III
print("\nIII. Socle mechanics (PR3): e = p forcing + lambda linearity")

def socle_analysis(G, c, p):
    """Classify coverers of unit positions on nonzero socle cosets;
    then, for EVERY e=p separator, build its total class map
    lambda: G[p] -> F_p from the full position sweep (all u, not just
    units -- lambda = 0 points included) and test single-residue,
    totality, and additivity on the whole p-torsion subgroup."""
    d, Cset, O = orbit_setup(G, c)
    kers = G.kernels()
    dom = [x for x in G.elems if G.smul(p, x) == G.zero]   # all of G[p]
    socle = [x for x in dom if x not in Cset]
    units = [u for u in range(d) if gcd(u, d) == 1]
    e_of_unit_coverers = set()
    for x in socle:
        for u in units:
            z = G.add(x, G.smul(u, c))
            for K in kers:
                if c in K or z not in K: continue
                e_of_unit_coverers.add(restriction_order(G, K, Cset, d))
    seps_p = [K for K in kers
              if c not in K and restriction_order(G, K, Cset, d) == p]
    lam, single, total = {}, True, True
    for K in seps_p:
        for x in dom:
            classes = {u % p for u in range(d)
                       if G.add(x, G.smul(u, c)) in K}
            if len(classes) > 1: single = False
            if not classes: total = False
            else: lam[(K, x)] = next(iter(classes))
    additive = total and all(
        (lam[(K, x1)] + lam[(K, x2)]) % p == lam[(K, G.add(x1, x2))]
        for K in seps_p for x1 in dom for x2 in dom)
    return e_of_unit_coverers, single and total, additive, socle, units

G63 = Grp([6, 3]); c63 = (1, 0)
es, single, additive, socle, _ = socle_analysis(G63, c63, 3)
print(f"   Z/6x3 at p=3: unit-coverer e-set {sorted(es)}, "
      f"{len(socle)} socle lifts")
check("S3a: PR3 unit-coverers at the 3-socle have e = 3 exactly",
      es == {3})
check("S3b: PR3 every e=3 separator's class map on G[3] is total, "
      "single-residue, additive", single and additive)

G122 = Grp([12, 2]); c122 = (1, 0)
es2, single2, additive2, socle2, _ = socle_analysis(G122, c122, 2)
print(f"   Z/12x2 at p=2: unit-coverer e-set {sorted(es2)}, "
      f"{len(socle2)} socle lifts")
check("S3c: PR3 unit-coverers at the 2-socle have e = 2 exactly",
      es2 == {2})
check("S3d: PR3 every e=2 separator's class map on G[2] is total, "
      "single-residue, additive", single2 and additive2)

# the 2w species at 4 | d: coverers of positions 2w (w a unit) are
# exactly {e=2, class 0 mod 2} u {e=4, class 2 mod 4}
d122, C122, O122 = orbit_setup(G122, c122)
k122 = G122.kernels()
species_ok = True
occ = {2: 0, 4: 0}
for x in socle2:
    for w in [u for u in range(d122) if gcd(u, d122) == 1]:
        u = (2 * w) % d122
        z = G122.add(x, G122.smul(u, c122))
        for K in k122:
            if c122 in K or z not in K: continue
            e = restriction_order(G122, K, C122, d122)
            if e == 2 or (e == 4 and u % 4 == 2):
                occ[e] += 1
            else:
                species_ok = False
check("S3e: PR3 the 2w-position species is {e=2} u {e=4, 2 mod 4}, "
      "both species occurring", species_ok and occ[2] > 0 and occ[4] > 0)

# ---------------------------------------------------------------- IV
print("\nIV. Abstract functional rigidity (PR4): exhaustive censuses")

def functional_min(p, r):
    """Min #functionals on F_p^r with {lam_i(y)} covering the required
    values at every y != 0 (p=2: both {0,1}; p>=3: all of F_p^*)."""
    pts = [t for t in product(range(p), repeat=r) if any(t)]
    funcs = list(product(range(p), repeat=r))
    need = set(range(p)) if p == 2 else set(range(1, p))
    def val(f, y): return sum(a * b for a, b in zip(f, y)) % p
    for size in range(1, len(funcs) + 1):
        for fam in combinations(funcs, size):
            if all(need <= {val(f, y) for f in fam} for y in pts):
                return size
    return None

minima = {}
for (p, r) in [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2)]:
    minima[(p, r)] = functional_min(p, r)
print("   true minima:", {k: v for k, v in sorted(minima.items())})
check("S4a: PR4 every functional minimum >= r + 1 (the proof's bound)",
      all(v >= r + 1 for (p, r), v in minima.items()))
check("S4b: PR4 p=2 minima are exactly r + 1 (the bound is sharp there)",
      all(minima[(2, r)] == r + 1 for r in (1, 2, 3)))

# ---------------------------------------------------------------- V
print("\nV. End-to-end adversarial censuses (PR5) + canonical (PR6)")

def canonical_cost(G, kers, c, Cset, O, d, m):
    """Build the canonical program and confirm it decides O."""
    # m trivial kernels cutting C exactly
    triv = [K for K in kers if Cset <= K]
    cut = None
    for fam in combinations(triv, m):
        inter = set(G.elems)
        for K in fam: inter &= K
        if frozenset(inter) == Cset:
            cut = list(fam); break
    # a frame character of full order d on c, one separator per prime
    frame = next(a for a in G.elems
                 if G.chi(a, c) != 0
                 and G.M // gcd(G.M, G.chi(a, c)) == d)
    seps = []
    for q in prime_factors(d):
        aq = tuple((d // q) * ai % mi for ai, mi in zip(frame, G.ms))
        Kq = frozenset(x for x in G.elems if G.chi(aq, x) == 0)
        seps.append(Kq)
    fam = cut + seps
    return len(fam), decides(G, fam, c, Cset, O)

for key, maxs in [("A", 3), ("B", 3), ("C", 2), ("E", 2)]:
    G, c, d, Cset, O, kers, m = setup[key]
    law = m + len(prime_factors(d))
    found, tested = census_min(G, kers, c, Cset, O, maxs)
    nsh = len([K for K in kers if len(K) < len(G.elems)])
    print(f"   config {key}: law {law} = {m}+{len(prime_factors(d))}; "
          f"{tested} families of <= {maxs} of {nsh} shadows swept")
    check(f"S5{key.lower()}: PR5 config {key}: no family of "
          f"<= {maxs} gates decides O", found is None)
    ncan, ok = canonical_cost(G, kers, c, Cset, O, d, m)
    check(f"S6{key.lower()}: PR6 config {key}: canonical decides O "
          f"at {ncan} = law {law} gates", ok and ncan == law)

# the delicate-regime probe: the species analysis at its most delicate
# regime, alpha = v_2(d) = 3 (e in {2,4,8} separators coexist).
# Predictions stated first: unit-position coverers still e = 2 only;
# 2w-position coverers still {e=2} u {e=4, 2 mod 4} -- the e=8
# separators (classes 0 or 4 mod 8) reach only the 4w positions.
print("\nV'. The alpha = 3 species probe (config E socle cosets)")
GE, cE, dE, CE, OE, kE, mE = setup["E"]
socE = [x for x in GE.elems
        if x not in CE and GE.smul(2, x) == GE.zero]
unit_es, twow_es, ok_2w = set(), set(), True
for x in socE:
    for w in [u for u in range(dE) if gcd(u, dE) == 1]:
        for u, bag in ((w, unit_es), ((2 * w) % dE, twow_es)):
            z = GE.add(x, GE.smul(u, cE))
            for K in kE:
                if cE in K or z not in K: continue
                e = restriction_order(GE, K, CE, dE)
                bag.add(e)
                if bag is twow_es and not (e == 2 or (e == 4 and u % 4 == 2)):
                    ok_2w = False
print(f"   unit-coverer e-set {sorted(unit_es)}, "
      f"2w-coverer e-set {sorted(twow_es)}")
check("S5e': follow-up: at alpha = 3 unit-coverers are e = 2 only",
      unit_es == {2})
check("S5e'': follow-up: at alpha = 3 the 2w species is still "
      "{e=2} u {e=4, 2 mod 4} -- e=8 never reaches 2w",
      ok_2w and twow_es == {2, 4})

# ---------------------------------------------------------------- VI
print("\nVI. Duality spot-check: t >= rank(V/S') at config B")
G, c, d, Cset, O, kers, m = setup["B"]
triv = [K for K in kers if Cset <= K]
ok_dual = True
for size in (1, 2):
    for fam in combinations(triv, size):
        Sp = set(G.elems)
        for K in fam: Sp &= K
        # rank(V/S') via the same socle counter with S' playing C
        if size < quotient_rank(G, frozenset(Sp)):
            ok_dual = False
check("S7a: every <= 2-subset of trivial kernels has t >= rank(V/S')",
      ok_dual)

print("\n" + "=" * 72)
print(f"ALL CHECKS PASSED ({CHECKS[0]})")
print("=" * 72)
