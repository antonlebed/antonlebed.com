"""
explore_selection_frame.py -- THE SELECTION FRAME (a later probe in a
sequence of growth-law records; sibling of explore_growth_laws.py ..
explore_hot_limit.py).

THE QUESTION (the descent target): which growth theorems survive on
an arbitrary locally-finite poset with weights? ANSWER: they
STRATIFY -- the three fates live at three structural floors, and
each floor's necessity is witnessed one floor down. Design +
predictions PR1-PR6 fixed before the run, amended once before
running.

THE FRAME. Floor 0 (POSET): states ascend strictly; a demand names
the admissible ascents; no weight needed. Floor 1 (MONOID): a
countable cancellative commutative monoid M, moves m != 1 act by
multiplication; weight = a summable CHARACTER w (w(ab) = w(a)w(b),
sum w(m) < inf); thermal policy picks m in A(x) with prob w(m)/Z.
Floor 2 (FREE = UFD): M free on countable atoms -- supp, gcd,
coprimality, v_g well-defined. Instance worlds: INT (free on primes,
w = m^-beta), POLY2 (monic F_2[x], free on irreducibles, w =
2^(-beta deg f)), NUM23 (the numerical monoid {x^n : n = 0 or
n >= 2}, atoms x^2, x^3 -- cancellative, NOT free: x^2x^2x^2 =
x^3x^3).

FINDINGS (tiers per the standard naming scale; run record below; all
sections assert).

1. THE MORTALITY FLOOR (rule, proved -- floor 0, PURE ORDER; verified
   S1). Any demand that confines the trajectory to a finite region R
   absorbs, under EVERY policy, within height(R) moves (strict
   ascent in a finite poset -- no demand shape needed). WHERE it
   dies is the demand's: for the INTERVAL demand (admissible = every
   region element above the state -- mortality's own shape: the
   D-TRA state lemma makes the frozen fiber exactly such an
   interval) the tombstone set is the no-R-successor elements, each
   realizable by some policy, and the tombstone is unique iff the
   reachable filter has a maximum (both directions: ascend from any
   element to a terminal; a maximum dominates every terminal). A
   general confined demand can run dry BELOW a maximum (specimen:
   region = divisors of 8, A(1) = {2}, A(2) = empty -- dies at 2
   with 8 above it): the tombstone law is interval-demand property,
   absorption is not. Mortality needs no weight, no monoid,
   no ring -- the D-TRA wall is the instance: the frozen-lambda fiber
   above seed s is exactly the multiples of s dividing W(lambda(s))
   (verified seeds 3, 5, 7 -> walls 24, 240, 504; every maximal path
   dies at the wall), and the fiber HAS a maximum, which is WHY the
   tombstone is one wall rather than many. Necessity of finiteness:
   an infinite region (the constant-{2} demand, explore_hot_limit.py's
   counterexample) never absorbs.

2. THE MULTI-TOMBSTONE PHENOMENON (rule, proved; verified S1 -- new
   at floor 0, invisible from inside the tower). On a region whose
   reachable filter has several maximal elements, the interval
   demand still surely absorbs but THE GRAVE IS THE POLICY'S: greedy
   dies at the cheapest maximal element, thermal splits w(b) : w(c). Census: 240 regions
   (divisor lattices of 60/72/210, every seed + 200 random
   sub-regions of divisors(360)), 30 with policy-dependent
   tombstones; minimal specimen {1 < 2, 1 < 3}. The tower's D-TRA
   never shows this (its fiber has a maximum): a genuinely new
   degree of freedom that opens one floor below the ring.

3. THE HOT LIMIT AT ITS CARRIER (rule, proved -- floor 1; verified
   S2). explore_hot_limit.py's upward-closure law states its true
   hypotheses: cancellative commutative monoid + summable character
   + up-closed nonempty admissible sets => for EVERY ELEMENT a (not
   only atoms -- cancellation and the character are element-
   agnostic) the injection m -> am gives mass(A cap aM) >= w(a)
   mass(A) (the mass identity w(aA) = w(a)w(A), exact on all three
   worlds incl. composite a), the opening floor is uniform in the
   state, and Levy Borel-Cantelli makes every element divide the
   state eventually a.s.; M is countable for free (a positive
   summable weight forces it), so a.s. simultaneously for all m:
   the chain is COFINAL -- the limit is the TOP of the completion,
   with NO ATOMICITY axiom (per-element cofinality is what survives
   in non-free worlds, where atom-depth domination does not imply
   divisibility; in a free world it specializes to every atom-depth
   -> infinity). INT cross-checks reproduce explore_hot_limit.py (Z_6(2) =
   0.332434, P(5|pick|6) = 0.1979261 >= 1/25); POLY2 floors hold in
   closed form (beta 1.5/2/3, elements of deg <= 2 incl. composite
   x(x+1)); MC: every window of
   deg <= 3 opens in 100/100 runs, v_x deepens (min 161 at step
   300). NUM23 satisfies the hypotheses (cancellative!), so hot
   growth reaches the top of a NON-FREE world too (mean ascent 465.0
   ~ the exact rate 7/3 per step) -- in the same world where
   independence dies (finding 5): the fates separate structurally
   within one monoid.

4. THE ZETA MEASURE AT ITS CARRIER (rule, proved -- floor 2;
   verified S3). explore_thermal_growth.py's thermal-breadth limit lifts verbatim
   to any FREE monoid: support-avoidance gives entry-once surely;
   the bijection m -> gm within the entering moves gives the exactly
   geometric entry depth (mass ratios = w(g), brute-verified at
   states 1, x, x(x+1)); depths independent across atoms (the weight
   factorizes over disjoint supports; asserted in the MC: joint
   depth-1 fraction = product of marginals within band); and
   P(limit = the crystal) = prod_g (1 - w(g)) = 1/zeta_M(w) BY THE
   EULER PRODUCT. The partition function of thermal breadth is the
   zeta function OF THE MONOID: Riemann for the integers (1/zeta(2)
   = 0.607927, sieve-verified to 10^6), and for POLY2 the RATIONAL
   zeta 1/(1 - 2^(1-beta)) -- crystal probability 1 - 2^(1-beta),
   EXACTLY 1/2 at beta = 2 (Euler truncation 0.500002 within its
   6.1e-5 tail; MC 400 runs: squarefree fraction 0.470 vs in-universe
   exact 0.505, deg-1 entry depth-1 fractions 0.733/0.740 vs 3/4).

5. THE COPRIMALITY COLLAPSE (rule, proved; verified S4 -- freeness
   is NECESSARY, the ladder's sharpest witness). In NUM23 the
   independence demand is MORTAL: atoms(x^n) = {both} for every
   n >= 5 (proved: n-2 >= 3 and n-3 >= 2 lie in M), so every D-IND
   trajectory from seed 1 dies by move 2 -- exhaustive census: the 4
   maximal 2-move paths (2,3),(3,2),(3,4),(4,3) ending at x^5, x^7;
   every first move n >= 5 terminal at once. Breadth's immortality
   (healing forever, explore_growth_laws.py) is a UFD PRIVILEGE. And the
   partition identity breaks with it: Dirichlet sum 13/12 != Euler
   product 1024/945 at t = 1/4, first divergence at t^6 (x^6 =
   x2 x2 x2 = x3 x3, one element, two multisets): P(crystal) =
   1/zeta_M IS unique factorization, quantitatively.

6. THE DEMAND LADDER (synthesis -- this record's headline). To DIE
   you need only order (floor 0); to REACH EVERYTHING you need
   multiplication (floor 1); to BE ARITHMETIC -- independent
   windows, squarefree, the crystal -- you need unique factorization
   (floor 2). Each fate is proved at its floor (findings 1, 3, 4);
   freeness's necessity is proved (finding 5), finiteness's and
   up-closure's likewise (findings 1, 3); cancellativity is the
   floor-1 proof's hypothesis with the boundary probed (finding 8).
   With the selection grading spanning explore_thermal_growth.py
   through explore_hot_limit.py (shape / full-support / argmin)
   the selection frame is now TWO-AXIS:
   structure floor x selection need. The primorial tower is what
   growth does on the ground floor of UFDs.

7. THE CLOCK TRANSFER (closed forms proved; decrease rule in range;
   verified S5). The stage-clock machinery (explore_observer_view.py /
   explore_depth_observer.py) is monoid-generic: clocks = roots of Z_state(beta) = 1. POLY2's
   spectrum is ALGEBRAIC -- u = 2^-beta satisfies an integer
   polynomial per rung: seed clock beta = 2 EXACTLY (zeta_2 = 2);
   rung-1 (state x) 2^beta = 3, beta = log2(3) = 1.584963; rung-2
   (state x(x+1)) u^2 + 2u - 1 = 0, u = sqrt(2) - 1, beta =
   1.271553; rungs 3-4 verified against their quartic/sextic
   witnesses (1.199519, 1.174252); strictly decreasing toward the
   pole beta = 1 (breadth's march transfers). explore_observer_view.py's
   duel mechanism holds verbatim: odds(gradual : stroke) = 1/Z_state,
   crossing 1 at the clock. (The integer clocks 1.3778, 1.2478, ...
   have no known closed form; the polynomial world's do -- a
   function-field simplification of the usual kind.)

8. THE CHARACTER GATE (observation; verified S6). The floor-1 weight
   axiom polices the monoid by itself: on the absorber specimen
   {1, g, h, z} (gh = g^2 = h^2 = z, z absorbing) NO nontrivial
   character exists (w(gz) = w(z) forces w(g) = 1 -- scanned);
   adjoining an idempotent (M = {g^k, g^k e}) admits a character
   only with w(e) = 1 FORCED, where the uniform floor genuinely
   FAILS (P(e-move) = 1/(1+a) = 0.7692 < 1 = w(e)) yet cofinality
   SURVIVES (200/200 MC runs pass above g^5 e: the cancellative
   g-direction plus a.s. e-entry suffice). Cancellativity is the
   proof's hypothesis; no counterexample to the CONCLUSION was
   found at the specimens tried. Route-weight cancellation (the
   observer engine) is pure floor 1: all 34 routes to x^10 in
   non-free NUM23 carry one numerator t^10, and route odds
   [3,3] : [2,2,2] = Z = 1/12 exactly, direct = formula -- the
   inside view survives where the crystal dies.

SCOPE + HONESTY. Floor-0 census: finite regions inside divisor
lattices (a divisibility-shaped sample of finite posets, all-policy
by exhaustive path enumeration). Floor-1/2 statements proved for
summable characters; the upward-closure proof needs only w(gm) =
w(g)w(m), as at explore_hot_limit.py. POLY2 MC runs a truncated menu (deg
<= 12) and the in-universe S3 model (8 atoms, deg <= 14, exponent
caps) with exact in-universe marginals -- findings 3-4 are proved
for the full laws. The D-DYN lock over function fields (which
irreducible column does F_2[x] dynamics fall into?) is untouched --
its lambda is the unit group of F_2[x]/(f), a study of its own. Non-commutative and non-cancellative-with-character worlds
beyond the S6 specimens are not chased.

PREDICTIONS (fixed before the run, amended once before running).
Adjudication -- NO MISSES, all six confirmed:
  PR1 mortality census .... CONFIRMED (240 regions, 30 multi-
      tombstone; specimen splits; walls 24/240/504; constant-{2}
      alive at 100 moves)
  PR2 floor + cross-checks  CONFIRMED (Z_6(2) = 0.332434 and
      P(5|pick|6) = 0.1979261 as frozen; POLY2 floors closed-form;
      NUM23 13/16 exact; openings 100/100 all >= frozen 97/90; v_x
      min 161 >= 60; NUM23 min 445 >= 400 sure, mean 465.0 in
      [455, 478])
  PR3 zeta measure ........ CONFIRMED (mass ratios within 1e-3;
      crystal 0.500002 / 0.750000 within tails; INT 0.607927; MC
      0.470 within 0.10 of 0.505; depth-1 0.733/0.740 within 0.09
      of 3/4; round-1 addition: joint depth-1 0.545 vs marginal
      product 0.542 -- independence asserted, band 0.10)
  PR4 collapse ............ CONFIRMED (max length 2; the 4 paths;
      13/12 vs 1024/945; first divergence t^6, +1)
  PR5 clocks .............. CONFIRMED (2.000000 exact, log2(3),
      -log2(sqrt(2)-1) to 1e-8; witnesses to 1e-10; decreasing;
      duel crossing at the clock)
  PR6 boundary (as 2b) .... CONFIRMED (character forcing; P_e =
      0.7692 = 1/(1+a); 200/200 cofinal)

RUN RECORD (python prime/code/explore_selection_frame.py, ~0.3 s
(timed), trivial memory, 3010 checks -- 2997 at the initial run, +11
in a first follow-up pass (composite-element floors a = 6 on INT and
POLY2 + the joint-independence band), +2 in a second follow-up pass
(the dry-death specimen)): S0 harness (poly sieve to deg
14, irreducible counts [2,1,2,3,6,9,18,30,56,99,186,335,630,1161] vs
the Moebius formula; zeta_poly vs brute with exact geometric tails;
300 pfactor recompositions; Bernoulli walls 24/240/504; NUM23 atoms
to n = 200); S1 mortality census (240 regions, exhaustive path
enumeration; D-TRA fibers seeds 3/5/7 with 4/48/76 maximal paths);
S2 hot limit (INT states 6/12/27 mass identity m <= 400; POLY2
closed-form floors; MC 100 x 300 menu deg <= 12; NUM23 MC 100 x
200 menu n <= 30); S3 zeta measure (mass ratios at deg <= 14; Euler
truncations; sieve to 10^6; in-universe MC 400 runs, menu 2914
moves); S4 collapse census + exact rationals + series to t^20; S5
clocks (bisection 80 iters, tol ~1e-9) + duel; S6 routes to x^10 +
the two boundary specimens. One mid-run fix, caught by reading
the first run's output: the per-atom depth-1 statistic used a
per-MOVE flag (a move g^2 h wrongly marked h deep) -- fractions read
0.695/0.710, both low; per-atom deep-mask fix moved them to
0.733/0.740; the crystal event was computed correctly both ways
(fraction 0.470 unchanged). Asserts had passed on the biased stat
(band 0.09): the eye caught what the band absorbed.
"""

import math
import random
from bisect import bisect_left
from fractions import Fraction

CHECKS = 0


def ok(cond, msg=""):
    global CHECKS
    if not cond:
        raise AssertionError("CHECK FAILED: " + msg)
    CHECKS += 1


# ------------------------------------------------------------------ #
# S0 harness: three instance worlds + poset machinery
# ------------------------------------------------------------------ #

# ---- INT: integers, free on primes, w(m) = m^(-beta) ----

def factorint(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def carmichael(n):
    lam = 1
    for p, e in factorint(n).items():
        if p == 2:
            lp = 1 if e == 1 else (2 if e == 2 else 2 ** (e - 2))
        else:
            lp = p ** (e - 1) * (p - 1)
        lam = lam * lp // math.gcd(lam, lp)
    return lam if n > 1 else 1


def bernoulli(nmax):
    """B_0..B_nmax as Fractions (recurrence sum C(m+1,j) B_j = 0)."""
    B = [Fraction(1)]
    for m in range(1, nmax + 1):
        s = Fraction(0)
        for j in range(m):
            s += Fraction(math.comb(m + 1, j)) * B[j]
        B.append(-s / (m + 1))
    return B


def wall_W(L, Bern):
    """W(L) = denominator of B_L / (2L), even L (explore_growth_laws.py's identity)."""
    return (Bern[L] / (2 * L)).denominator


ZETA2 = math.pi ** 2 / 6  # zeta(2), exact source


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def sigma_beta(D, beta):
    return sum(d ** (-beta) for d in divisors(D))


# ---- POLY2: monic polynomials over F_2 (ints, bit i = coeff of x^i),
#      free on monic irreducibles, w(f) = 2^(-beta deg f) ----

def pdeg(f):
    return f.bit_length() - 1


def pmul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r


def pdivmod(a, m):
    q = 0
    dm = pdeg(m)
    while a and pdeg(a) >= dm:
        s = pdeg(a) - dm
        q ^= 1 << s
        a ^= m << s
    return q, a


def moebius(n):
    f = factorint(n)
    if any(e > 1 for e in f.values()):
        return 0
    return -1 if len(f) % 2 else 1


DMAX = 14                 # factor table covers all monic f, deg <= DMAX
SPF = {}                  # f -> smallest irreducible factor
IRRED = {}                # deg -> sorted list of irreducibles
IRRED_ALL = []


def build_poly_sieve():
    """poly Eratosthenes: unmarked in (deg, value) order = irreducible."""
    for d in range(1, DMAX + 1):
        IRRED[d] = []
    for f in range(2, 1 << (DMAX + 1)):
        if f in SPF:
            continue
        SPF[f] = f
        IRRED[pdeg(f)].append(f)
        IRRED_ALL.append(f)
        dmax_m = DMAX - pdeg(f)
        for m in range(2, 1 << (dmax_m + 1)):
            fm = pmul(f, m)
            if fm not in SPF:
                SPF[fm] = f


def pfactor(f):
    """factorization dict irreducible -> exponent, monic f (int >= 2)."""
    out = {}
    while f > 1:
        g = SPF[f]
        out[g] = out.get(g, 0) + 1
        f = pdivmod(f, g)[0]
    return out


def zeta_poly(beta):
    """zeta of the monic-F_2[x] monoid: sum over ALL monic incl. 1."""
    r = 2.0 ** (1.0 - beta)
    ok(r < 1, "zeta_poly domain")
    return 1.0 / (1.0 - r)


# ---- NUM23: the numerical monoid {n : n = 0 or n >= 2} (additive
#      exponents of x; atoms 2, 3), cancellative, NOT free ----

def in_M23(n):
    return n == 0 or n >= 2


def atoms23(n):
    """atoms dividing x^n: a in {2,3} with n - a in M."""
    return frozenset(a for a in (2, 3) if n >= a and in_M23(n - a))


def weighted_sample(rg, cum, items):
    x = rg.random() * cum[-1]
    return items[bisect_left(cum, x)]


# ------------------------------------------------------------------ #
print("S0: harness")

build_poly_sieve()
for d in range(1, DMAX + 1):
    formula = sum(moebius(e) * 2 ** (d // e) for e in divisors(d)) // d
    ok(len(IRRED[d]) == formula,
       "irreducible count deg %d: %d vs %d" % (d, len(IRRED[d]), formula))
ok(IRRED[1] == [2, 3], "deg-1 irreducibles are x, x+1")
ok(IRRED[2] == [7], "deg-2 irreducible is x^2+x+1")
ok(IRRED[3] == [11, 13], "deg-3 irreducibles x^3+x+1, x^3+x^2+1")
print("  irreducible counts deg 1..%d: %s"
      % (DMAX, [len(IRRED[d]) for d in range(1, DMAX + 1)]))

# zeta_poly vs brute Dirichlet sum (exact geometric tail)
for beta in (1.5, 2.0, 3.0):
    D = 40
    brute = sum(2 ** d * 2.0 ** (-beta * d) for d in range(0, D + 1))
    r = 2.0 ** (1 - beta)
    tail = r ** (D + 1) / (1 - r)
    ok(abs(zeta_poly(beta) - brute) <= tail + 1e-12,
       "zeta_poly brute beta %.2f" % beta)

# pfactor sanity: recompose 300 random monic polys
rng = random.Random(151)
for _ in range(300):
    f = rng.randrange(4, 1 << (DMAX + 1))
    prod = 1
    for g, e in pfactor(f).items():
        for _ in range(e):
            prod = pmul(prod, g)
    ok(prod == f, "pfactor recompose")

# Bernoulli walls
BERN = bernoulli(18)
ok(wall_W(2, BERN) == 24 and wall_W(4, BERN) == 240
   and wall_W(6, BERN) == 504, "walls 24/240/504")

# NUM23 atoms: {2} for n in {2,4}; {3} for 3; both for all n >= 5
ok(atoms23(2) == frozenset([2]) and atoms23(4) == frozenset([2]), "atoms 2,4")
ok(atoms23(3) == frozenset([3]), "atoms 3")
for n in range(5, 201):
    ok(atoms23(n) == frozenset([2, 3]), "atoms both at %d" % n)
print("  zeta_poly, pfactor, walls, NUM23 atoms verified")


# ------------------------------------------------------------------ #
# S1: T1 MORTALITY AT FLOOR 0 (pure poset; no weight, no monoid).
#     A demand that confines the trajectory to a finite region R
#     absorbs -- at an element with no proper R-successor, within
#     height(R) moves, under EVERY policy; the tombstone is unique
#     iff the reachable filter has a maximum.
# ------------------------------------------------------------------ #
print("S1: mortality at floor 0 (pure poset)")


def reachable_filter(R, seed):
    return sorted(y for y in R if y == seed or (y % seed == 0 and y != seed))


def region_paths(R, seed, cap=500000):
    """all maximal strictly-ascending divisibility paths from seed in R."""
    Rs = set(reachable_filter(R, seed))
    paths = []
    stack = [(seed, (seed,))]
    while stack:
        x, path = stack.pop()
        succ = [y for y in Rs if y != x and y % x == 0]
        if not succ:
            paths.append(path)
            ok(len(paths) <= cap, "path explosion")
        else:
            for y in succ:
                stack.append((y, path + (y,)))
    return paths


def region_height(R, seed):
    """longest chain (edges) in the reachable filter."""
    Rs = reachable_filter(R, seed)
    h = {}
    for x in sorted(Rs):
        preds = [h[y] for y in Rs if y in h and y != x and x % y == 0]
        h[x] = 1 + max(preds) if preds else 0
    return max(h.values())


def census_region(R, seed):
    Rs = set(reachable_filter(R, seed))
    terminals = set(y for y in Rs
                    if not any(z != y and z % y == 0 for z in Rs))
    height = region_height(R, seed)
    paths = region_paths(R, seed)
    ends = set(p[-1] for p in paths)
    maxlen = max(len(p) - 1 for p in paths)
    ok(ends <= terminals, "ends are terminals")
    ok(terminals <= ends, "every terminal realizable by some policy")
    ok(maxlen <= height, "budget: within height(R) moves")
    has_max = any(all(y % z == 0 for z in Rs) for y in Rs)
    ok((len(ends) == 1) == has_max, "unique tombstone iff maximum")
    return len(ends)


count_regions = 0
multi_tomb = 0
for base in (60, 72, 210):
    ds = divisors(base)
    for seed in ds:
        if census_region(set(ds), seed) > 1:
            multi_tomb += 1
        count_regions += 1
rng = random.Random(1510)
ds360 = divisors(360)
for _ in range(200):
    size = rng.randrange(2, 9)
    R = set(rng.sample(ds360, size))
    seed = rng.choice(sorted(R))
    if census_region(R, seed) > 1:
        multi_tomb += 1
    count_regions += 1
ok(multi_tomb > 0, "multi-tombstone phenomenon realized")
print("  census: %d regions -- every policy absorbs at a local maximum"
      " within height moves; %d regions have policy-dependent"
      " tombstones" % (count_regions, multi_tomb))

# the minimal multi-tombstone specimen {1, 2, 3}: policy picks the grave
paths = region_paths({1, 2, 3}, 1)
ok(sorted(p[-1] for p in paths) == [2, 3], "specimen terminals {2,3}")
for beta in (1.5, 2.0, 4.0):
    pb = 2.0 ** (-beta) / (2.0 ** (-beta) + 3.0 ** (-beta))
    ok(0.5 < pb < 1.0, "thermal split favors the light tombstone")
print("  specimen {1<2, 1<3}: greedy dies at 2, thermal splits"
      " w(2):w(3) -- the tombstone is the policy's")

# the D-TRA instance: frozen-lambda fiber = [seed, W] interval;
# unique wall because the fiber has a maximum
for seed, L in ((3, 2), (5, 4), (7, 6)):
    ok(carmichael(seed) == L, "lambda(seed)")
    W = wall_W(L, BERN)
    fiber = [y for y in range(seed, 4 * W + 1, seed) if carmichael(y) == L]
    ok(fiber == [d for d in divisors(W) if d % seed == 0],
       "fiber = multiples of seed dividing W (seed %d)" % seed)
    ok(max(fiber) == W, "fiber max = W")
    paths = region_paths(set(fiber), seed)
    ok(all(p[-1] == W for p in paths), "every policy dies at W")
    print("  D-TRA seed %d: fiber = multiples of %d dividing %d; all %d"
          " maximal paths die at the wall %d" % (seed, seed, W,
                                                 len(paths), W))

# the tombstone law is INTERVAL-demand property: a general confined
# demand can run dry below a maximum -- region divisors(8), A(1) =
# {move to 2}, A(2) = empty: dies at 2 with 8 above it
R8 = {1, 2, 4, 8}
demand_dry = {1: [2], 2: [], 4: [8], 8: []}
state, moves_made = 1, 0
while demand_dry[state]:
    state = demand_dry[state][0]
    moves_made += 1
ok(state == 2 and moves_made == 1, "dry death at 2")
ok(any(y != 2 and y % 2 == 0 for y in R8),
   "2 is NOT a no-successor element of the region")
print("  scope: a non-interval confined demand dies at 2 inside"
      " divisors(8) -- the tombstone law belongs to interval demands;"
      " absorption belongs to all confined demands")

# necessity of finiteness: the constant-{2} demand's region is
# infinite (every state has successor 2x) -- immortal at any policy
x = 3
for _ in range(100):
    x *= 2
ok(x == 3 * 2 ** 100, "constant-{2}: 100 moves, alive")
print("  necessity: an infinite region (constant-{2} demand)"
      " never absorbs -- finiteness is the mortality axiom")


# ------------------------------------------------------------------ #
# S2: T2 HOT LIMIT AT FLOOR 1 (cancellative commutative monoid +
#     summable character + up-closed nonempty demand => the uniform
#     floor P(g | pick) >= w(g) => the top, a.s.)
# ------------------------------------------------------------------ #
print("S2: hot limit at floor 1 (cancellative monoid + character)")

# --- INT cross-checks (explore_hot_limit.py's printed values re-derived) ---
beta = 2.0
N = 6
W = wall_W(carmichael(N), BERN)
D = W // N
Z6 = ZETA2 - sigma_beta(D, beta)
ok(abs(Z6 - 0.332434) < 5e-7, "Z_6(2) = 0.332434 (explore_hot_limit.py)")
# v_5(W/N) = 0 so the transparent correction sigma(D) - sigma(D/5^v)
# vanishes and explore_hot_limit.py's exact formula reduces to 5^-beta zeta/Z
ok(D % 5 != 0, "5 does not divide W/N at N = 6")
P5 = 5.0 ** (-beta) * ZETA2 / Z6
ok(abs(P5 - 0.1979261) < 1e-6, "P(5|pick|6,beta 2) = 0.1979261")
ok(P5 >= 5.0 ** (-beta), "floor at INT state 6")
print("  INT: Z_6(2) = %.6f, P(5|pick|6) = %.7f >= 1/25 (explore_hot_limit.py"
      " values re-derived)" % (Z6, P5))

# --- the abstract mass identity w(gA) = w(g) w(A) (the injection's
#     engine), verified by finite enumeration on all three worlds ---
for N in (6, 12, 27):
    W = wall_W(carmichael(N), BERN)
    ok(W % N == 0, "N divides its wall")
    DD = W // N
    A = [m for m in range(2, 401) if DD % m != 0]     # D-DYN admissible
    for g in (2, 3, 5, 6):     # 6 composite: the floor is per ELEMENT
        wA = sum(m ** (-beta) for m in A)
        wgA = sum((g * m) ** (-beta) for m in A)
        ok(abs(wgA - g ** (-beta) * wA) < 1e-12,
           "mass identity INT N=%d a=%d" % (N, g))
        ok(all(DD % (g * m) != 0 for m in A),
           "up-closure: aA stays admissible (N=%d a=%d)" % (N, g))
u = 2.0 ** (-beta)
for g in (2, 3, 7, 6):     # 6 = x(x+1) composite: per-element floor
    dg = pdeg(g)
    wg = 2.0 ** (-beta * dg)
    massA_tr = sum(2 ** d * 2.0 ** (-beta * d) for d in range(2, 30 - dg))
    wgA = sum(2 ** d * 2.0 ** (-beta * (d + dg)) for d in range(2, 30 - dg))
    ok(abs(wgA - wg * massA_tr) < 1e-12, "mass identity POLY2 a=%d" % g)
t = Fraction(1, 4)
massA23 = t ** 2 / (1 - t)                      # all moves n >= 2
massx2M = t ** 2 + t ** 4 / (1 - t)             # x^2-multiples: n=2, n>=4
P22 = massx2M / massA23
ok(P22 == Fraction(13, 16), "NUM23 P(x^2-multiple) = 13/16 exactly")
ok(P22 >= t ** 2, "floor at NUM23: 13/16 >= 1/16")
print("  mass identity w(aA) = w(a)w(A) exact on INT, POLY2, NUM23"
      " incl. composite a; NUM23 floor 13/16 >= 1/16 (exact rational)")

# --- POLY2 floors in closed form: up-closed demand A = {deg m >= 2} ---
for beta2 in (1.5, 2.0, 3.0):
    r = 2.0 ** (1 - beta2)
    massA = r ** 2 / (1 - r)                    # sum_{d >= 2} (2u)^d
    zp = zeta_poly(beta2)
    for g in (2, 3, 7, 6):    # incl. composite 6 = x(x+1)
        wg = 2.0 ** (-beta2 * pdeg(g))
        if pdeg(g) == 1:
            massAgM = wg * (zp - 1)   # gm needs deg m >= 1
        else:
            massAgM = wg * zp         # every gm has deg >= 2
        Pg = massAgM / massA
        ok(Pg >= wg - 1e-12,
           "POLY2 floor a=%d beta=%.1f: %.6f >= %.6f" % (g, beta2, Pg, wg))
print("  POLY2 floors P(a | pick) >= w(a): exact closed forms,"
      " beta 1.5/2/3, elements of deg <= 2 incl. composite x(x+1) --"
      " the floor is per ELEMENT, not per atom")

# --- POLY2 MC: hot growth reaches the top ---
beta = 2.0
MENU_D = 12
menu = [f for d in range(1, MENU_D + 1)
        for f in range(1 << d, 1 << (d + 1))]
menu_fac = {f: pfactor(f) for f in menu}
cum = []
s = 0.0
for f in menu:
    s += 2.0 ** (-beta * pdeg(f))
    cum.append(s)

RUNS, STEPS = 100, 300
open_by = {g: 0 for g in [2, 3, 7] + IRRED[3]}
vx_final = []
rg = random.Random(9151)
for run in range(RUNS):
    state = {}
    for step in range(STEPS):
        m = weighted_sample(rg, cum, menu)
        for g, e in menu_fac[m].items():
            state[g] = state.get(g, 0) + e
    for g in open_by:
        if g in state:
            open_by[g] += 1
    vx_final.append(state.get(2, 0))
for g in (2, 3, 7):
    ok(open_by[g] >= 97, "deg<=2 window %d opens %d/100" % (g, open_by[g]))
for g in IRRED[3]:
    ok(open_by[g] >= 90, "deg-3 window %d opens %d/100" % (g, open_by[g]))
ok(min(vx_final) >= 60, "v_x deepens: min %d >= 60" % min(vx_final))
print("  POLY2 MC (beta 2, %d runs x %d steps, menu deg <= %d):"
      % (RUNS, STEPS, MENU_D))
print("    openings deg<=2: %s/100 each; deg-3: %s/100; v_x final"
      " min %d, mean %.1f"
      % ([open_by[g] for g in (2, 3, 7)],
         [open_by[g] for g in IRRED[3]],
         min(vx_final), sum(vx_final) / RUNS))

# --- NUM23 MC: same-monoid contrast -- free thermal reaches the top ---
tf = 0.25
menu23 = list(range(2, 31))
cum23 = []
s = 0.0
for n in menu23:
    s += tf ** n
    cum23.append(s)
totals = []
rg = random.Random(23151)
for run in range(100):
    v = 0
    for step in range(200):
        v += weighted_sample(rg, cum23, menu23)
    totals.append(v)
ok(min(totals) >= 400, "NUM23: every run gains >= 400 (moves >= 2)")
mean_t = sum(totals) / len(totals)
ok(455 <= mean_t <= 478, "NUM23 mean total %.1f in [455, 478]" % mean_t)
print("  NUM23 MC: free thermal ascends (mean %.1f, E-rate 7/3; min %d"
      " >= 400 surely) -- the top is reached in the SAME world where"
      " independence dies (S4)" % (mean_t, min(totals)))
print("  necessity: up-closure (constant-{2} column, S1);"
      " cancellativity is the injection's hypothesis (boundary: S6)")


# ------------------------------------------------------------------ #
# S3: T3 ZETA MEASURE AT FLOOR 2 (free monoid: entry-once, geometric
#     depths, crystal probability = 1/zeta_M -- the Euler product)
# ------------------------------------------------------------------ #
print("S3: zeta measure at floor 2 (free monoid)")

# precompute factorizations for all monic f, deg <= 14
FAC = {}
for d in range(1, DMAX + 1):
    for f in range(1 << d, 1 << (d + 1)):
        FAC[f] = pfactor(f)

# --- the mass-ratio identity, brute on POLY2: among support-avoiding
#     moves containing g, mass(v_g = k+1)/mass(v_g = k) = w(g) ---
beta = 2.0
for S, Sname in ((frozenset(), "1"), (frozenset([2]), "x"),
                 (frozenset([2, 3]), "x(x+1)")):
    for g in (2, 3, 7):
        if g in S:
            continue
        wg = 2.0 ** (-beta * pdeg(g))
        mass = {}
        for f, fac in FAC.items():
            if any(p in S for p in fac):
                continue
            k = fac.get(g, 0)
            if k >= 1:
                mass[k] = mass.get(k, 0.0) + 2.0 ** (-beta * pdeg(f))
        for k in (1, 2, 3):
            ratio = mass[k + 1] / mass[k]
            ok(abs(ratio - wg) < 1e-3,
               "geometric ratio state %s g %d k %d: %.5f vs %.5f"
               % (Sname, g, k, ratio, wg))
print("  entry-depth mass ratios = w(g) (the geometric law) at states"
      " 1, x, x(x+1), atoms deg <= 2")

# --- crystal probability: Euler truncation vs 1 - 2^(1-beta) ---
for beta3, target in ((2.0, 0.5), (3.0, 0.75)):
    prod = 1.0
    for d in range(1, DMAX + 1):
        prod *= (1.0 - 2.0 ** (-beta3 * d)) ** len(IRRED[d])
    r = 2.0 ** (1 - beta3)
    tail = r ** (DMAX + 1) / (1 - r)   # >= sum_{d>DMAX} N_d 2^(-beta d)
    ok(abs(prod - target) <= tail + 1e-9,
       "crystal prob beta %.1f: %.6f vs %.6f" % (beta3, prod, target))
    print("  POLY2 crystal probability at beta %.1f: %.6f (exact"
          " 1 - 2^(1-beta) = %.4f; |err| <= %.1e)"
          % (beta3, prod, target, tail))

# --- INT instance: prod(1 - p^-2) -> 1/zeta(2) (Riemann demoted) ---
LIM = 10 ** 6
sieve = bytearray([1]) * (LIM + 1)
sieve[0] = sieve[1] = 0
for i in range(2, int(LIM ** 0.5) + 1):
    if sieve[i]:
        sieve[i * i::i] = bytearray(len(range(i * i, LIM + 1, i)))
prodi = 1.0
for p in range(2, LIM + 1):
    if sieve[p]:
        prodi *= 1.0 - p ** (-2.0)
ok(abs(prodi - 1.0 / ZETA2) < 3e-6,
   "INT crystal 1/zeta(2): %.7f vs %.7f" % (prodi, 1.0 / ZETA2))
print("  INT crystal probability %.6f = 1/zeta(2): the Riemann zeta is"
      " the integer instance of the partition function" % prodi)

# --- MC witness: in-universe support-avoiding growth, 8 atoms deg<=4 ---
beta = 2.0
universe = [g for d in range(1, 5) for g in IRRED[d]]
ok(len(universe) == 8, "universe size 8")
uidx = {g: i for i, g in enumerate(universe)}
wat = {g: 2.0 ** (-beta * pdeg(g)) for g in universe}
# master move list as (support bitmask, depth-1 flag, weight),
# exponent vectors over the 8 atoms with total deg <= 14
by_mask = {}


def gen_moves(i, deg, mask, deepmask, wgt):
    if i == len(universe):
        if mask:
            by_mask.setdefault(mask, []).append((wgt, deepmask))
        return
    g = universe[i]
    dg = pdeg(g)
    e = 0
    while deg + e * dg <= 14:
        gen_moves(i + 1, deg + e * dg, mask | ((1 << i) if e else 0),
                  deepmask | ((1 << i) if e >= 2 else 0),
                  wgt * wat[g] ** e)
        e += 1


gen_moves(0, 0, 0, 0, 1.0)
mask_cum = {}
mask_items = {}
n_moves = 0
for mask, lst in by_mask.items():
    c = []
    s = 0.0
    for wgt, deepmask in lst:
        s += wgt
        c.append(s)
    mask_cum[mask] = c
    mask_items[mask] = lst
    n_moves += len(lst)
print("  in-universe menu: %d moves (8 atoms, deg <= 14)" % n_moves)

crystal_runs = 0
depth1 = {2: 0, 3: 0}
joint11 = 0
RUNS3 = 400
rg = random.Random(31513)
masks = sorted(by_mask)
for run in range(RUNS3):
    entered_mask = 0
    entry_depth = {}
    while entered_mask != (1 << 8) - 1:
        avail = [m for m in masks if not (m & entered_mask)]
        tot_c = []
        s = 0.0
        for m in avail:
            s += mask_cum[m][-1]
            tot_c.append(s)
        pick_mask = weighted_sample(rg, tot_c, avail)
        wgt, deepmask = weighted_sample(
            rg, mask_cum[pick_mask], mask_items[pick_mask])
        for i in range(8):
            if pick_mask & (1 << i):
                entry_depth[universe[i]] = not (deepmask & (1 << i))
        entered_mask |= pick_mask
    # a run is crystal iff every atom entered at depth 1
    if all(entry_depth.values()):
        crystal_runs += 1
    for g in (2, 3):
        if entry_depth[g]:
            depth1[g] += 1
    if entry_depth[2] and entry_depth[3]:
        joint11 += 1
exact_in_universe = 1.0
for g in universe:
    exact_in_universe *= 1.0 - wat[g]
frac = crystal_runs / RUNS3
ok(abs(frac - exact_in_universe) <= 0.10,
   "MC crystal %.3f vs in-universe exact %.3f" % (frac, exact_in_universe))
for g in (2, 3):
    ok(abs(depth1[g] / RUNS3 - 0.75) <= 0.09,
       "depth-1 fraction atom %d: %.3f vs 3/4" % (g, depth1[g] / RUNS3))
marg_prod = (depth1[2] / RUNS3) * (depth1[3] / RUNS3)
ok(abs(joint11 / RUNS3 - marg_prod) <= 0.10,
   "independence: joint depth-1 %.3f vs marginal product %.3f"
   % (joint11 / RUNS3, marg_prod))
print("  MC (%d runs): squarefree fraction %.3f vs in-universe exact"
      " %.3f; deg-1 depth-1 fractions %.3f, %.3f (3/4); joint %.3f"
      " vs product %.3f (independence)"
      % (RUNS3, frac, exact_in_universe,
         depth1[2] / RUNS3, depth1[3] / RUNS3,
         joint11 / RUNS3, marg_prod))


# ------------------------------------------------------------------ #
# S4: T4 THE COPRIMALITY COLLAPSE (freeness is necessary: in NUM23
#     the independence demand is MORTAL -- a UFD privilege)
# ------------------------------------------------------------------ #
print("S4: the coprimality collapse (freeness necessary)")

# exhaustive D-IND trajectory census from seed 1 (= x^0). First moves
# n >= 5 are terminal at once (atoms both -- S0, proved all n >= 5);
# the continuing classes are first moves {2, 3, 4}, and every later
# admissible move lies in {2, 3, 4} too (any n >= 5 carries both
# atoms and the state after one move carries at least one).
all_paths = []
stack = [((n,), n) for n in (2, 3, 4)]
while stack:
    path, state = stack.pop()
    moves = [n for n in (2, 3, 4) if not (atoms23(n) & atoms23(state))]
    if not moves:
        all_paths.append(path)
        continue
    for n in moves:
        stack.append((path + (n,), state + n))
maxlen = max(len(p) for p in all_paths)
two_move = sorted(p for p in all_paths if len(p) == 2)
ok(maxlen == 2, "max D-IND trajectory length = 2")
ok(two_move == [(2, 3), (3, 2), (3, 4), (4, 3)],
   "exactly 4 maximal 2-move trajectories")
ok(all(atoms23(sum(p)) == frozenset([2, 3]) for p in all_paths),
   "every terminal state carries both atoms")
ok(sorted(set(sum(p) for p in two_move)) == [5, 7],
   "terminal states x^5, x^7")
print("  D-IND census from seed 1: every trajectory dies by move 2;"
      " the 4 two-move paths %s end at x^5, x^7; first moves n >= 5"
      " die at once. Independence is MORTAL without freeness."
      % (two_move,))

# the zeta-Euler mismatch: Dirichlet sum != Euler product (non-UFD)
t = Fraction(1, 4)
dsum = 1 + t ** 2 / (1 - t)
eprod = 1 / ((1 - t ** 2) * (1 - t ** 3))
ok(dsum == Fraction(13, 12), "Dirichlet sum = 13/12")
ok(eprod == Fraction(1024, 945), "Euler product = 1024/945")
ok(eprod > dsum, "product > sum (multisets overcount elements)")
part23 = [0] * 21
part23[0] = 1
for part in (2, 3):
    for n in range(part, 21):
        part23[n] += part23[n - part]
elem = [1 if in_M23(n) else 0 for n in range(21)]
first_div = next(n for n in range(21) if part23[n] != elem[n])
ok(first_div == 6 and part23[6] - elem[6] == 1,
   "first divergence at t^6, coefficient +1")
print("  zeta-Euler mismatch: sum 13/12 != product 1024/945, first"
      " divergence t^6 (x^6 = x2x2x2 = x3x3): the partition identity"
      " P(crystal) = 1/zeta_M IS unique factorization")


# ------------------------------------------------------------------ #
# S5: T5 THE CLOCK TRANSFER (normalizer machinery is monoid-generic;
#     POLY2 stage clocks are closed-form ALGEBRAIC numbers)
# ------------------------------------------------------------------ #
print("S5: the clock transfer (POLY2 clocks are algebraic)")

ATOM_ORDER = [2, 3, 7, 11, 13]   # x, x+1, x^2+x+1, then the deg-3 pair


def Z_breadth(state_atoms, beta):
    """normalizer of the support-avoiding thermal law at this state."""
    zp = zeta_poly(beta)
    for g in state_atoms:
        zp *= 1.0 - 2.0 ** (-beta * pdeg(g))
    return zp - 1.0


def bisect_clock(state_atoms):
    lo, hi = 1.0001, 8.0
    ok(Z_breadth(state_atoms, lo) > 1.0
       and Z_breadth(state_atoms, hi) < 1.0, "clock bracket")
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if Z_breadth(state_atoms, mid) > 1.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


clocks = [bisect_clock(ATOM_ORDER[:j]) for j in range(5)]
ok(abs(clocks[0] - 2.0) < 1e-9, "seed clock = 2 EXACTLY: %.10f" % clocks[0])
ok(abs(clocks[1] - math.log2(3.0)) < 1e-8,
   "rung-1 clock = log2(3): %.10f" % clocks[1])
ok(abs(clocks[2] - (-math.log2(math.sqrt(2.0) - 1.0))) < 1e-8,
   "rung-2 clock = -log2(sqrt(2)-1): %.10f" % clocks[2])
u3 = 2.0 ** (-clocks[3])
ok(abs((1 - u3) ** 2 * (1 - u3 ** 2) - 2 * (1 - 2 * u3)) < 1e-10,
   "rung-3 algebraic witness (1-u)^2(1-u^2) = 2(1-2u)")
u4 = 2.0 ** (-clocks[4])
ok(abs((1 - u4) ** 2 * (1 - u4 ** 2) * (1 - u4 ** 3)
       - 2 * (1 - 2 * u4)) < 1e-10,
   "rung-4 algebraic witness (1-u)^2(1-u^2)(1-u^3) = 2(1-2u)")
ok(all(clocks[i] > clocks[i + 1] for i in range(4)),
   "clocks strictly decrease toward the pole")
print("  clocks (rungs 0..4): %s" % ", ".join("%.6f" % c for c in clocks))
print("  closed forms: 2 exact; log2(3); -log2(sqrt(2)-1); higher rungs"
      " = roots of integer polynomials in u = 2^-beta -- the clock"
      " spectrum is ALGEBRAIC; strictly decreasing (breadth's march to"
      " the pole transfers)")

# the duel (explore_observer_view.py's boundary mechanism at floor 1): neighbor
# prefix-block geneses of x(x+1): H2 = [one stroke] vs H1 = [x, then
# x+1]; both share the numerator w(x(x+1)) and the seed normalizer,
# so odds(H1 : H2) = 1/Z_x -- crossing 1 exactly at the rung-1 clock
for b5 in (1.4, clocks[1], 1.8):
    odds = 1.0 / Z_breadth(ATOM_ORDER[:1], b5)
    if b5 == clocks[1]:
        ok(abs(odds - 1.0) < 1e-6, "duel odds = 1 at the clock")
    elif b5 < clocks[1]:
        ok(odds < 1.0, "below the clock: the stroke is favored")
    else:
        ok(odds > 1.0, "above the clock: gradualism is favored")
print("  the duel: odds(gradual : stroke) = 1/Z_state crosses 1 at the"
      " clock -- explore_observer_view.py's mechanism, verbatim at floor 1")


# ------------------------------------------------------------------ #
# S6: T6 ROUTE-WEIGHT CANCELLATION AT FLOOR 1 + the axiom boundary
# ------------------------------------------------------------------ #
print("S6: route cancellation at floor 1 + the boundary of the axioms")

# NUM23 (cancellative, NOT free): all routes from 1 to x^10 have equal
# Boltzmann numerators
t = Fraction(1, 4)


def routes_to(total):
    out = []
    stack = [((), 0)]
    while stack:
        path, s = stack.pop()
        if s == total:
            out.append(path)
            continue
        for n in range(2, total - s + 1):
            rem = total - s - n
            if rem == 0 or rem >= 2:
                out_n = path + (n,)
                stack.append((out_n, s + n))
    return out


rts = routes_to(10)
ok(len(rts) > 5, "multiple routes to x^10: %d" % len(rts))
nums = set()
for p in rts:
    numer = Fraction(1)
    for n in p:
        numer *= t ** n
    nums.add(numer)
ok(nums == {t ** 10}, "all route numerators equal t^10")
Z23 = t ** 2 / (1 - t)   # demand = all moves: state-independent Z
odds_direct = ((t ** 3 / Z23) * (t ** 3 / Z23)) / \
    ((t ** 2 / Z23) * (t ** 2 / Z23) * (t ** 2 / Z23))
ok(odds_direct == Z23 == Fraction(1, 12),
   "route odds [3,3]:[2,2,2] = Z = 1/12, direct = formula")
print("  NUM23: %d routes to x^10, one numerator t^10 -- the observer"
      " engine needs only cancellativity; it survives where the"
      " crystal dies. Route odds [3,3]:[2,2,2] = Z = 1/12 exactly"
      " (longer route favored at Z < 1)." % len(rts))

# boundary specimen A: {1, g, h, z} with gh = g^2 = h^2 = z, z
# absorbing: the character equations FORCE w = 1 -- the weight axiom
# itself polices absorbers. Table check + forcing scan.
ELEMS = ["1", "g", "h", "z"]


def mulA(x, y):
    if x == "1":
        return y
    if y == "1":
        return x
    return "z"


for x in ELEMS:
    for y in ELEMS:
        ok(mulA(x, y) == mulA(y, x), "specimen A commutative")
        for zz in ELEMS:
            ok(mulA(mulA(x, y), zz) == mulA(x, mulA(y, zz)),
               "specimen A associative")
for a in (0.1, 0.3, 0.5, 0.9, 1.5):
    w = {"1": 1.0, "g": a, "h": a, "z": a * a}
    violations = sum(1 for x in ELEMS for y in ELEMS
                     if abs(w[mulA(x, y)] - w[x] * w[y]) > 1e-12)
    ok(violations > 0, "no nontrivial character at a = %.1f" % a)
w1 = {e: 1.0 for e in ELEMS}
ok(all(abs(w1[mulA(x, y)] - w1[x] * w1[y]) < 1e-15
       for x in ELEMS for y in ELEMS), "trivial character works")
print("  specimen A {1,g,h,z}: no nontrivial character exists (w(g z)"
      " = w(z) forces w(g) = 1) -- the character axiom polices"
      " absorbing elements by itself")

# boundary specimen B: M = {g^k, g^k e}, e idempotent (ge = eg,
# e^2 = e): nontrivial character exists (w(e) = 1 FORCED, w(g) = a
# free) but the uniform floor FAILS at e: P(pick in eM) = 1/(1+a)
# < 1 = w(e) -- while COFINALITY SURVIVES (g-direction cancellative,
# e enters a.s.)
a = 0.3
mass_eM = 1.0 / (1.0 - a)                     # g^k e, k >= 0
mass_all = a / (1.0 - a) + 1.0 / (1.0 - a)    # g^k (k>=1) + g^k e (k>=0)
P_e = mass_eM / mass_all
ok(abs(P_e - 1.0 / (1.0 + a)) < 1e-12, "P(e-move) = 1/(1+a)")
ok(P_e < 1.0, "the uniform floor FAILS at the idempotent")
moves_b = [("g", j) for j in range(1, 25)] + [("e", j) for j in range(25)]
cw = []
s = 0.0
for kind, j in moves_b:
    s += a ** j
    cw.append(s)
rg = random.Random(61516)
reached = 0
for run in range(200):
    k, has_e = 0, False
    for step in range(60):
        kind, j = weighted_sample(rg, cw, moves_b)
        k += j
        if kind == "e":
            has_e = True
    if has_e and k >= 5:
        reached += 1
ok(reached == 200, "cofinality survives: 200/200 pass above g^5 e")
print("  specimen B (idempotent adjoined): w(e) = 1 forced, the floor"
      " fails at e (P = 1/(1+a) = %.4f < 1) yet cofinality holds"
      " 200/200 -- cancellativity is the proof's hypothesis; no"
      " counterexample to the conclusion found" % P_e)

print()
print("ALL CHECKS PASS: %d" % CHECKS)
