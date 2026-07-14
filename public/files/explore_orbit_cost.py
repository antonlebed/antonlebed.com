"""
The orbit-cost law (MOONSHOT probe, P85).

The gate-budget grading's sharpest residual (LOGIC.md SI), taken with
the P83 bar: both censused orbit programs read as coset gates + an
order read (pentagon: gate_1(a^2 b^-1) AND the order-5 read; Phi_6:
gate_1(ab) AND the order-6 read). Is that additive decomposition a
THEOREM -- a law with a lower-bound mechanism -- or an accident of two
examples? Bar: a LAW, never a bare cost table.

THE REFRAME (fixed before anything ran). Work in dlog coordinates:
units of F_p = Z/n (n = p - 1), L-leaf points V = (Z/n)^L. A monomial
gate gate_m(prod x_i^{e_i}) decides [chi(z) = 0] for the character
chi = m*(e_1, ..., e_L) -- gate shadows are EXACTLY the character
kernels of V (verified against field-side shadows below). A stable
torsion orbit is the set O of generators of the cyclic subgroup
C = <c>, c the dlog vector of the pair, d = |C| = lcm of the leaf
orders, |O| = phi(d). Program anatomy: every kernel K is TRIVIAL on C
(C <= K; coset/membership work; S' := intersection of the trivial
kernels) or a SEPARATOR of restriction order e = [C : C cap K] > 1
(e | d by Lagrange). Generators all share one bit pattern (bit true
iff C <= K), so O sits in a single Boolean atom and a family DECIDES
O iff

    intersection{K : C <= K}  minus  union{K : C not<= K}  ==  O

(the atom condition; separators never meet O since chi(uc) = u*chi(c)
with u a unit mod d). Define m(C) = minimal number of monomial
equations cutting C exactly = minimal generator count of the
annihilator C-perp <= V-dual (computed two ways below: q-ranks, and
exhaustive subset search over trivial kernels).

PREDICTIONS (stated before the run):
 P1 (rule, proved any L): THE ORBIT-COST LAW, upper bound. The
    canonical program -- m(C) coset gates cutting C exactly, plus for
    each prime q | d the separator (d/q)*chi_0 (chi_0 a frame
    character with chi_0(c) of order d; one exists since the value
    set {chi(c)} is the cyclic group of order d) -- decides O at
    m(C) + omega(d) gates. Readout: AND of coset bits AND NOT of
    separator bits; within C the q-separator bit fires on u*c iff
    q | u, so all-false = generator. At L = 2: m(C) = 1 if d = n
    else 2 (Smith form: V/C is cyclic iff the generator's
    coordinates have gcd 1 with n). At rank 1: m = 0 if d = n else
    1 -- the law REPRODUCES the order-cost law omega(d)+1 / omega(n)
    (P83 P1) exactly, and prices the pentagon (2+1 = 3), Phi_6 at
    p = 7 (1+2 = 3) and p = 13 (2+2 = 4).
 P2 (rule, proved any L): FORCED SEPARATORS. For each prime q | d,
    separating the generators (bits: [e_i = 1]) from the order-d/q
    element q*c (bits: [e_i | q]) forces a gate with restriction
    order exactly q; distinct primes cannot share a gate. Every
    decider has >= omega(d) separators carrying the primes of d.
 P3 (rule, proved any L): THE COSET-COVER BOUND. If S' > C, every
    nontrivial C-coset x+C of S' must be covered by the separator
    slices T_i = K_i cap (x+C), and a coset meets a subgroup in a
    single coset of the intersection or not at all -- a q-separator's
    slice is ONE residue class mod q in torsor coordinates on
    x+C = Z/d. With only the omega(d) forced separators the slices
    form a covering system with one class per DISTINCT PRIME
    modulus, and by CRT such a system never covers Z/d: choosing an
    avoided residue per prime leaves prod(q-1) >= 1 points uncovered
    (verified exhaustively over every class choice at d = 6, 30,
    210, 1722; section III). So s = omega(d) forces S' = C, hence
    t >= m(C): any decider using only the forced separators costs
    >= m(C) + omega(d) -- every L, every d. A trade therefore needs
    EXTRA separators whose slices repeat a prime modulus or use a
    composite one (mass bound: the moduli e_i must satisfy
    sum 1/e_i >= 1 per coset) -- the territory P4 censuses.
 P4 (rule at the swept range): NO TRADE BEATS THE LAW. Programs
    trading coset gates for extra separators (t < m(C), s > omega)
    are the remaining escape; the per-coset arithmetic leaves some
    trades open (two same-prime separators with complementary
    slices; at d = 6 the {2,3,3} masses satisfy every per-coset
    test). Swept: full unstructured censuses at p = 13 (mixed
    orbit, all <= 3-gate families), p = 31 (primitive orbit, all
    <= 3-gate), (Z/6)^3 at p = 7 (all <= 3-gate, three leaves);
    structured censuses (exhaustive GIVEN the proved P2 constraint:
    s >= omega(d) with every prime of d carried) at p = 61, d = 30
    (all <= 4-gate shapes) and (Z/12)^3 at p = 13 with m(C) = 3
    (all <= 4-gate shapes -- where a {2,3,3} trade would live).
    Prediction: no beat anywhere; a beat is the counterexample
    orbit the residual asks for, and would be the headline.
 P5 (observation): THE NEW SPECIES PRICED. The mixed-generator
    orbit (ord a = 2, ord b = 3, d = 6: C is not the graph of any
    monomial -- no single coset gate suggests itself, the journal's
    hunch territory) and the primitive orbit (d = n: O = the
    primitive pairs) obey the same law as the graph orbits.

RESULTS (the run below prints the record; all confirmed):
  I   dlog kernels == field gate shadows computed by pure field
      arithmetic: 28 distinct at p = 11, 50 at p = 13 (the P83
      shadow counts); atom condition == generic atom-split decides
      on 200 random families per prime, zero disagreements.
  II  m(C) by q-rank == exhaustive cut search at all 8 battery
      configs; canonical programs decide O at m + omega gates
      everywhere; rank-1 Z/12 full exhaust reproduces the order-cost
      law at every d | 12 (min = m + omega exactly).
  III cover bound: no class choice covers at d = 6, 30, 210, 1722 --
      including the Sylvester set {2,3,7,41} whose mass
      sum 1/q = 1.0006 EXCEEDS 1: the mass bound alone would leave
      it open; the CRT cover bound closes every d. (A first
      reconstruction of this lemma claimed mass >= 1 iff 30 | d --
      refuted by exactly this witness; the cover bound replaced it.)
  IV  censuses (lower bounds; minimum = law everywhere, NO beat):
      - mixed p=13: all 20,875 families of <= 3 of 50 shadows fail
        -> cost exactly 4 = 2 + 2.
      - primitive p=31: all 457,450 families of <= 3 of 140 shadows
        fail -> cost exactly 4 = 1 + 3.
      - (Z/6)^3: all 234,248 families of <= 3 of 112 kernels fail
        (three leaves, unstructured) -> cost exactly 4 = 2 + 2.
      - p=61 d=30: 350 kernels (24 trivial; forced classes 16/36/60
        at orders 2/3/5); all 829,440 structured <= 4-gate
        candidates fail -> cost exactly 5 = 2 + 3.
      - (Z/12)^3 m=3: 504 kernels (100 trivial; forced classes
        80/180 at orders 2/3); all 337,054,176 structured <= 4-gate
        candidates fail -> cost exactly 5 = 3 + 2. The {2,3,3}
        trade does not realize: no counterexample at three leaves.
  V   every canonical decider carries separator orders exactly the
      primes of d.

Tier: P1, P2, P3 rule (proved, any L, any d -- P3's cover bound is
one CRT line, no boundary cases; section III verifies it
exhaustively over all class choices at four d including a
mass-over-1 witness). P4 rule for the swept battery (L <= 3,
d in {5, 6, 30}, p in {7, 11, 13, 31, 61}; structured legs
exhaustive GIVEN the proved P2 constraint; the pentagon and Phi_6
lower bounds are P83's exhaustive censuses, explore_gate_budget.py
-- cited, not rerun). The general trade-exclusion (this record's
named residual; whenever m(C) = 1 it is already proved by P3
alone) is CLOSED at P99: proved for any finite abelian ambient --
the law is exact, both directions, every leaf count
(explore_trade_exclusion.py). P5 observation.

Classical contacts: covering systems of congruences (Erdos) -- the
trade question IS covering-system existence under kernel
realizability; B.H. Neumann's lemma (a group covered by k subgroups
is covered by those of index <= k) bounds trade configurations; the
subgroup-cell bound (P83) is the ambient Lagrange arithmetic this
law sharpens on cyclic targets.

Runs standalone, stdlib only. ~70 s, tiny memory.
ALL CHECKS PASSED (43).
"""

import sys
import random
from math import gcd
from itertools import combinations, product

CHECKS = [0]
def check(name, ok):
    CHECKS[0] += 1
    print(("  [OK] " if ok else "  [FAIL] ") + name)
    if not ok:
        sys.exit("CHECK FAILED: " + name)

def prime_factors(n):
    out, q = [], 2
    while q * q <= n:
        if n % q == 0:
            out.append(q)
            while n % q == 0: n //= q
        q += 1
    if n > 1: out.append(n)
    return out

def omega(n):
    return len(prime_factors(n))

def mult_order(x, p):
    o, y = 1, x % p
    while y != 1:
        y = y * x % p; o += 1
    return o

POP = (lambda x: x.bit_count()) if hasattr(int, "bit_count") \
    else (lambda x: bin(x).count("1"))

def gcd_all(t):
    g = 0
    for x in t: g = gcd(g, x)
    return g

def and_all(ms, total):
    a = total
    for m in ms: a &= m
    return a

def or_all(ms):
    u = 0
    for m in ms: u |= m
    return u

def decides_generic(masks, target, total):
    """generic atom split (P83's decides) -- cross-check oracle."""
    atoms = [total]
    for s in masks:
        nxt = []
        for a in atoms:
            x, y = a & s, a & ~s
            if x: nxt.append(x)
            if y: nxt.append(y)
        atoms = nxt
    return all((a & target) in (0, a) for a in atoms)


# ------------------------------------------------------------------
# The configuration: V = (Z/n)^L, C = <c>, kernels, classes.
# ------------------------------------------------------------------

class Config:
    def __init__(self, n, c):
        self.n, self.c, self.L = n, tuple(ci % n for ci in c), len(c)
        c = self.c
        L = self.L
        self.points = list(product(range(n), repeat=L))
        self.idx = {z: i for i, z in enumerate(self.points)}
        self.total = (1 << len(self.points)) - 1
        self.d = n // gcd(gcd_all(c), n) if gcd_all(c) else 1
        C = [tuple(k * ci % n for ci in c) for k in range(self.d)]
        self.Cmask = mask_of(C, self.idx)
        O = [tuple(u * ci % n for ci in c)
             for u in range(self.d) if gcd(u, self.d) == 1] \
            if self.d > 1 else [tuple(c)]
        self.Omask = mask_of(O, self.idx)
        # distinct kernels: canonicalize characters by <chi>
        seen, kers = set(), []
        for chi in product(range(n), repeat=L):
            g = gcd_all(chi)
            o = n // gcd(g, n) if g else 1
            rep = min(tuple(k * u % n for u in chi)
                      for k in range(1, o + 1) if gcd(k, o) == 1) \
                if o > 1 else chi
            if rep in seen: continue
            seen.add(rep)
            m = 0
            for i, z in enumerate(self.points):
                if sum(u * x for u, x in zip(chi, z)) % n == 0:
                    m |= 1 << i
            val = sum(u * x for u, x in zip(chi, self.c)) % n
            e = n // gcd(val, n) if val else 1
            kers.append((m, e, chi))
        self.kernels = kers          # (mask, restriction order e, chi)
        self.trivial = [k for k in kers if k[1] == 1]
        self.seps = [k for k in kers if k[1] > 1]

    def m_by_rank(self):
        """min generators of C-perp, by q-ranks of the q-torsion."""
        n, L = self.n, self.L
        perp = [chi for chi in product(range(n), repeat=L)
                if sum(u * x for u, x in zip(chi, self.c)) % n == 0]
        assert len(perp) == n ** L // self.d
        m = 0
        for q in prime_factors(n):
            tor = sum(1 for chi in perp
                      if all(q * u % n == 0 for u in chi))
            r = 0
            while q ** (r + 1) <= tor: r += 1
            m = max(m, r)
        return m

    def coset_gates(self, m):
        """exhaustive: no m-1 trivial kernels cut C; some m do.
        Returns a cutting m-set (verifying m(C) independently)."""
        if self.Cmask == self.total:
            return []                      # C = V: zero coset gates
        for r in range(1, m):
            for fam in combinations(self.trivial, r):
                if and_all([k[0] for k in fam], self.total) == self.Cmask:
                    raise AssertionError("m(C) smaller than predicted")
        for fam in combinations(self.trivial, m):
            if and_all([k[0] for k in fam], self.total) == self.Cmask:
                return list(fam)
        raise AssertionError("no m-set of trivial kernels cuts C")

    def canonical_seps(self):
        """(d/q)*chi_0 for each prime q | d, chi_0 a frame char."""
        n, d = self.n, self.d
        bymask = {k[0]: k for k in self.kernels}
        chi0 = next(k[2] for k in self.kernels if k[1] == d)
        out = []
        for q in prime_factors(d):
            chi = tuple((d // q) * u % n for u in chi0)
            m = 0
            for i, z in enumerate(self.points):
                if sum(u * x for u, x in zip(chi, z)) % n == 0:
                    m |= 1 << i
            out.append(bymask[m])
        return out

    def decides(self, fam):
        """atom condition: fam = list of (mask, e, chi)."""
        A, U = self.total, 0
        for m, e, chi in fam:
            if e == 1: A &= m
            else: U |= m
        return (A & ~U) == self.Omask


def mask_of(pts, idx):
    m = 0
    for z in pts: m |= 1 << idx[z]
    return m


# ------------------------------------------------------------------ I
print("I. GROUNDING -- dlog kernels are the field gate shadows")

def field_shadows(p, cf):
    """gate masks via FIELD arithmetic (pow, no dlogs), indexed in
    cf's point space through z = (g^x, g^y)."""
    n = p - 1
    g = next(x for x in range(2, p) if mult_order(x, p) == n)
    fld = [(pow(g, x, p), pow(g, y, p)) for x, y in cf.points]
    divs = [m for m in range(1, n + 1) if n % m == 0]
    shadows = set()
    for i in range(n):
        for j in range(n):
            ws = [pow(a, i, p) * pow(b, j, p) % p for a, b in fld]
            for m in divs:
                bm = 0
                for t, w in enumerate(ws):
                    if pow(w, m, p) == 1:
                        bm |= 1 << t
                shadows.add(bm)
    return shadows

random.seed(85)
for p in (11, 13):
    n = p - 1
    cf = Config(n, (1, 2))
    ours = {k[0] for k in cf.kernels}
    theirs = field_shadows(p, cf)
    check("p=%d: dlog kernels == field gate shadows (%d distinct)"
          % (p, len(ours)), ours == theirs)
    bad = sum(1 for _ in range(200)
              if (lambda fam: cf.decides(fam) != decides_generic(
                  [k[0] for k in fam], cf.Omask, cf.total))(
                  random.sample(cf.kernels, random.randint(1, 4))))
    check("p=%d: atom condition == generic atom-split decides on "
          "200 random families" % p, bad == 0)
print()

# ----------------------------------------------------------------- II
print("II. THE LAW'S UPPER BOUND -- canonical programs (P1)")

print("  rank-1 reproduction (Z/12, full exhaust per d):")
for d in (1, 2, 3, 4, 6, 12):
    cfd = Config(12, (12 // d,))
    law = cfd.m_by_rank() + omega(d)
    found = None
    for r in range(0, 4):
        for fam in combinations(cfd.kernels, r):
            if cfd.decides(list(fam)):
                found = r; break
        if found is not None: break
    check("Z/12 d=%-2d: exhaust min = %d = m+omega (m=%d) -- the "
          "order-cost law" % (d, law, cfd.m_by_rank()),
          found == law)

battery = []
def add(name, n, c, exp_m):
    cf = Config(n, c)
    m = cf.m_by_rank()
    check("%s: m(C) = %d (q-rank == exhaustive cut search)"
          % (name, exp_m), m == exp_m)
    coset = cf.coset_gates(m)      # also verifies no (m-1)-set cuts
    seps = cf.canonical_seps()
    law = m + omega(cf.d)
    es = sorted(k[1] for k in seps)
    check("%s: canonical %d-gate program (m=%d coset + omega=%d "
          "seps, orders %s) decides O" %
          (name, law, m, omega(cf.d), es),
          cf.decides(coset + seps) and len(coset) + len(seps) == law
          and es == sorted(prime_factors(cf.d)))
    battery.append((name, cf, law))
    return cf

cf_pent  = add("pentagon p=11 d=5",        10, (2, 4),     2)
cf_phi7  = add("Phi_6 p=7 d=6=n",          6,  (1, 5),     1)
cf_phi13 = add("Phi_6 p=13 d=6",           12, (2, 10),    2)
cf_mix   = add("mixed p=13 c=(6,4) d=6",   12, (6, 4),     2)
cf_prim  = add("primitive p=31 d=30=n",    30, (1, 1),     1)
cf_61    = add("30-boundary p=61 d=30",    60, (2, 4),     2)
cf_l3a   = add("(Z/6)^3 p=7 c=(3,2,0)",    6,  (3, 2, 0),  2)
cf_l3b   = add("(Z/12)^3 p=13 c=(6,4,0)",  12, (6, 4, 0),  3)
print()

# ---------------------------------------------------------------- III
print("III. THE COSET-COVER BOUND -- one class per prime never "
      "covers (P3)")
# 1722 = 2*3*7*41: Sylvester primes, sum 1/q > 1 with 30 nmid d --
# the mass bound alone would NOT close it; the CRT cover bound does.
for d in (6, 30, 210, 1722):
    qs = prime_factors(d)
    covers = False
    for choice in product(*(range(q) for q in qs)):
        if all(any(x % q == a for q, a in zip(qs, choice))
               for x in range(d)):
            covers = True; break
    check("d=%d (primes %s, sum 1/q = %.4f): no class choice covers"
          % (d, qs, sum(1.0 / q for q in qs)), not covers)
print()

# ---------------------------------------------------------------- IV
print("IV. THE CENSUSES -- lower bounds, the counterexample hunt (P4)")

def full_exhaust(cf, name, upto):
    cnt = 0
    for r in range(1, upto + 1):
        for fam in combinations(cf.kernels, r):
            cnt += 1
            if cf.decides(list(fam)):
                check("%s: %d-gate family decides -- BEAT FOUND"
                      % (name, r), False)
    return cnt

n_f = full_exhaust(cf_mix, "mixed p=13", 3)
check("mixed p=13: all %d families of <= 3 of %d shadows fail -> "
      "cost exactly 4" % (n_f, len(cf_mix.kernels)), True)

n_f = full_exhaust(cf_prim, "primitive p=31", 3)
check("primitive p=31: all %d families of <= 3 of %d shadows fail "
      "-> cost exactly 4" % (n_f, len(cf_prim.kernels)), True)

n_f = full_exhaust(cf_l3a, "(Z/6)^3", 3)
check("(Z/6)^3: all %d families of <= 3 of %d kernels fail "
      "(three leaves, unstructured) -> cost exactly 4"
      % (n_f, len(cf_l3a.kernels)), True)


def structured_census(cf, name, budget):
    """Every family of <= budget gates that could decide O, by the
    PROVED P2 constraint: >= omega(d) separators carrying every
    prime of d. Shapes (t, s): trivial intersections S' deduped at
    minimal t; forced core = one separator per prime; 0, 1, or 2
    extra separators. Size-bucketed subset tests prune the extras.
    Returns candidate-family count; FAILs the run on any beat."""
    primes = prime_factors(cf.d)
    om = len(primes)
    E = {q: [k for k in cf.seps if k[1] == q] for q in primes}
    print("    %s: %d kernels = %d trivial + %d separators; forced "
          "classes %s" % (name, len(cf.kernels), len(cf.trivial),
                          len(cf.seps),
                          {q: len(E[q]) for q in primes}))
    # S' -> min trivial-gate count
    Smin = {cf.total: 0}
    frontier = {cf.total}
    for t in range(1, budget - om + 1):
        nxt = set()
        for S in frontier:
            for k in cf.trivial:
                S2 = S & k[0]
                if S2 not in Smin:
                    Smin[S2] = t
                    nxt.add(S2)
        frontier = nxt
    # separators bucketed by mask size, descending
    by_size = sorted(cf.seps, key=lambda k: -POP(k[0]))
    sizes = [POP(k[0]) for k in by_size]
    fams = 0
    for core in product(*(E[q] for q in primes)):
        Ucore = or_all([k[0] for k in core])
        coreset = set(core)
        for S, t in Smin.items():
            rem = budget - t - om
            if rem < 0: continue
            fams += 1
            if (S & ~Ucore) == cf.Omask:
                check("%s: BEAT at (t=%d, s=%d)" % (name, t, om),
                      False)
            if rem >= 1:
                R = S & ~Ucore & ~cf.Omask
                pr = POP(R)
                for k, sz in zip(by_size, sizes):
                    if sz < pr: break
                    if k in coreset: continue
                    fams += 1
                    if (R & ~k[0]) == 0 and \
                       (S & ~(Ucore | k[0])) == cf.Omask:
                        check("%s: BEAT at (t=%d, s=%d)"
                              % (name, t, om + 1), False)
            if rem >= 2:
                # two extras: K must take >= half of R, K' the rest
                R = S & ~Ucore & ~cf.Omask
                pr = POP(R)
                half = (pr + 1) // 2
                for k in cf.seps:
                    if k in coreset: continue
                    RK = R & ~k[0]
                    if POP(R & k[0]) < half: continue
                    prk = POP(RK)
                    for k2, sz2 in zip(by_size, sizes):
                        if sz2 < prk: break
                        if k2 in coreset or k2 is k: continue
                        fams += 1
                        if (RK & ~k2[0]) == 0 and \
                           (S & ~(Ucore | k[0] | k2[0])) == cf.Omask:
                            check("%s: BEAT at (t=%d, s=%d)"
                                  % (name, t, om + 2), False)
    return fams

n_f = structured_census(cf_61, "p=61 d=30", 4)
check("p=61 d=30: all %d structured <= 4-gate candidates fail "
      "(exhaustive given P2; <= 2 gates impossible outright) -> "
      "cost exactly 5 = 2 + 3" % n_f, True)

n_f = structured_census(cf_l3b, "(Z/12)^3 m=3", 4)
check("(Z/12)^3 m=3: all %d structured <= 4-gate candidates fail "
      "(exhaustive given P2; the {2,3,3} trade does not realize) -> "
      "cost exactly 5 = 3 + 2 -- no counterexample at three leaves"
      % n_f, True)
print()

# ----------------------------------------------------------------- V
print("V. FORCED SEPARATORS carried by every decider found (P2)")
for name, cf, law in battery:
    es = sorted(k[1] for k in cf.canonical_seps())
    check("%s: separator orders %s == primes of d" % (name, es),
          es == sorted(prime_factors(cf.d)))
print()

print("ALL CHECKS PASSED (%d)" % CHECKS[0])
