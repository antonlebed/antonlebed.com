"""
The gate-budget grading (MOONSHOT probe, P83).

The idempotent-logic entry's last named reopen (LOGIC.md SI), taken
with its bar: the meadow closure proved omniscience -- every shadow
decidable -- at unstated cost. Grade the decidable world by
measurement cost. Bar: a LAW (exact costs for the named shadows plus
lower-bound mechanisms), never a bare cost table.

THE DEFINITION (fixed before anything ran). A measurement program
against a shadow S on the units of F_p (n = p - 1), or of a cyclic
group C_n: WORDS are formulas over the leaves built from MUL
(binary), INV, NOT (unary) -- the meadow alphabet; the MONOMIAL
alphabet drops NOT. GATES are the ladder's bits gate_m(w) =
[w^m = 1]; the READOUT is any Boolean function of the gate bits, and
the program decides S if readout = [x in S] at every unit point.
Three budget axes: GATE COUNT, WORD OPS (formula operations, the
integer-complexity convention -- no reuse), ALPHABET LEVEL
(monomial < NOT-closed < meadow). The CUT budget -- collected
monomials of a defining polynomial, the torsion-menu law's currency
(P82) -- prices the shadow as a CONDITION; the axes price DECIDING
it. Each axis binds at its own level: at the monomial level gate
count carries laws; at the meadow level gate count collapses to 1
(gate_1 of a decision word) and the price moves to word ops.

PREDICTIONS (stated before the run):
 P1 (rule, proved, field-free): THE ORDER-COST LAW. On one leaf over
    the monomial alphabet every gate is an order filter [ord x | m],
    m | n (word exponent k and gate index m collapse through gcd),
    so gate cost is divisor-lattice separation. For the exact-order
    shadow [ord x = d]:
        cost = omega(d) + 1   if d is a proper divisor of n,
        cost = omega(n)       if d = n  (primitivity),
    omega = number of distinct primes. Upper: the canonical family
    {d} + {d/q : q prime | d} (drop the gate m = d when d = n -- it
    is the constant-true bit; for d = n every e != n divides some
    n/q). Lower (the SEPARATION mechanism): the downward pair
    (d, d/q) forces a gate with d/q | m, d nmid m, and two distinct
    primes cannot share one (lcm(d/q, d/q') = d | m); the upward
    pair (d, dq), nonempty iff d < n, forces a gate with d | m --
    disjoint from every downward gate. Corollary prices: filters
    [ord x | m] cost 1 (the equality-grading rungs gate_m(ab^-1)
    and [x = 1] = gate_1 are priced exactly 1); primitivity costs
    omega(p - 1).
 P2 (rule, proved): THE INFINITY ROWS. A monomial gate bit is
    conjugacy-orbit-constant (w(a^u, b^u) = w(a, b)^u preserves
    order), so every readout is orbit-constant: a shadow that
    splits one orbit has NO finite monomial-gate price at any gate
    count. The P75/P77 measurement walls are exactly the infinite
    entries of the cost table ([a + b = 3] at p = 7 splits the
    orbit of (3, 3)); the alphabet axis is what makes them finite
    (the +-1-ratio lines fall at the NOT-closed level and the
    meadow level decides everything -- P77, cited not rerun).
 P3 (rule, proved): THE SUBGROUP-CELL BOUND. A two-leaf monomial
    gate shadow is the kernel of a torus character composed with
    ^m -- a subgroup H <= (F_p*)^2 of index dividing n, so
    |H| >= n. The readout makes the target a union of Boolean
    atoms of r subgroups, and Lagrange arithmetic prices small
    targets: a difference atom H1 - K (K = H1 cap H2, K < H1)
    inside a t-point target forces |K| | |H1| and |H1| - |K| <= t,
    so |H1| <= 2t; a complement atom forces |H1 u H2| >= n^2 - t
    while two proper subgroups cover at most 3n^2/4; the
    intersection atom contains (1, 1). For a target of <= 4 points
    avoiding (1, 1) this kills r <= 2 whenever n > 8.
 P4 (rule, proved + exhaustive): THE PENTAGON PRICE. The order-5
    orbit O = {(t^u, t^2u)} of the pentagon conic (P82) has READ
    cost exactly 3 monomial gates (p = 1 mod 5, p > 9): >= 3 by P3
    (|O| = 4); <= 3 by gate_1(a^2 b^-1) AND gate_5(a) AND NOT
    gate_1(a). Its CUT cost is 5 collected monomials (the
    torsion-menu law, P82). Cutting and reading are different
    currencies -- the same orbit is cheaper to read than to cut.
 P5 (rule, proved at p = 7; censused at p = 13): THE
    CRYSTALLOGRAPHIC PRICE. The Phi_6 stable orbit of the line
    a + b = 1 (the dependent shadow's stable points, |O| = 2,
    O = {(z, z^-1), (z^-1, z)}, ord z = 6) reads at exactly 3
    monomial gates at p = 7: >= 3 by P3; <= 3 because 6 = n there --
    gate_1(ab) AND NOT gate_3(a) AND NOT gate_2(a); primitivity
    is one gate cheaper exactly at d = n (the P1 boundary case
    landing in the field). At p = 13 (6 proper in 12) the additive
    program gate_1(ab) + canonical [ord a = 6] costs
    1 + (omega(6) + 1) = 4; whether any 3-gate program exists is
    censused exhaustively. Prediction: the bracket [3, 4]; the
    exact value is the run's verdict.
 P6 (rule, proved + census): THE HEIGHT FLOOR. At the meadow level
    every shadow costs ONE gate, so the price moves to word ops.
    Upper route: [x = c] is decided by 1 gate and at most
    h_p(c) + 2 word ops -- gate_1(x * w^-1) with w a word of
    h_p(c) ops making the constant c from one graded leaf
    (constant on the units except 1: at the leaf value 1 every
    word reads 0 or 1, so the exception is forced; one masking
    gate_1(x) patches it when w reads 1 there). h_p(-1) <= 6 at
    every p (the P77 wall-breaker word NOT(a^-1) * (NOT a)^-1 * a
    -- an algebraic identity, any p). Floor: COUNTING applies to
    decision words directly -- at most F(t) formulas of cost t
    exist (F(t) = 2F(t-1) + sum_{i+j=t-1} F(i)F(j), F(0) = 1), so
    at most cum(L) shadows are single-gate-decidable at word cost
    <= L, and the dearest residue's decision-word cost (likewise
    max_c h_p(c)) is >= L_min(p) = min{L : cum(L) >= p - 2} -- a
    numeric floor growing with p without bound. Census: exact
    h_p(c) tables at p = 5, 7 (Dijkstra over the function space);
    direct word checks beyond. Size, deleted as data, returns as
    cost: WHICH residue a program decides is priced like height.
 P7 (rule, by construction; verified): RING ASSEMBLY. One ring gate
    is k channel gates in parallel (gates of CRT words assemble
    per channel), so per-channel prices multiply across channels
    at no extra gate count -- one RAD gate gate_m(ab^-1) reads all
    seven equality gradings at once.

RESULTS (the run below prints the record; all confirmed):
  P1 lattice sweep exhaustive: every d | n for n in {6, 12, 30,
     60, 360} (54 targets) + 7 boundary targets at n = 2310 -- no
     family below the law separates, the canonical family does.
     Field realization at p = 11, 13: distinct one-leaf monomial
     gate shadows = the d(n) order filters exactly (4 at p = 11,
     6 at p = 13); canonical programs decide [ord x = d] at every
     d; primitivity at p = 11 read by 2 = omega(10) gates.
  P2 orbit-constancy exhaustive at p = 7 (5,184 gate-point
     combinations x all automorphisms), 3,000 random at p = 11;
     the [a + b = 3] orbit split verified.
  P3/P4 pentagon: p = 11 -- 28 distinct gate shadows, all 406
     1-/2-gate families fail, the named 3-gate program decides O
     exactly; p = 31 -- 140 shadows, all 9,870 families fail,
     program decides. Read 3 (exact) vs cut 5 (menu law).
  P5 p = 7: 20 shadows, all 210 1-/2-gate families fail, the named
     3-gate program decides -- exact 3. p = 13: 50 shadows; all
     1,275 1-/2-gate and all 19,600 3-gate families fail
     (exhaustive); the additive 4-gate program decides -- the
     crystallographic price at p = 13 is exactly 4. The p = 7
     discount is real and is the law's d = n boundary case.
  P6 heights (exact Dijkstra): p = 5: h(2) = 7, h(3) = 7,
     h(4) = 6; p = 7: h(2) = 7, h(3) = 11, h(4) = 8, h(5) = 11,
     h(6) = 6. So h_p(-1) = 6 exactly at p = 5, 7: the P77
     wall-breaker word is OPTIMAL there, and -1 is the cheapest
     nontrivial constant (observation; heights are not monotone
     in c -- h(4) < h(3) at p = 7). The 6-op word verified at
     p = 11, 13, 31. Counting floor: L_min(10^3) = 5,
     L_min(10^6) = 9 -- the floor grows without bound.
  P7 RAD: 300 unit pairs x m in {1, 2, 4, 240}: ring gate = AND of
     7 channel bits, zero disagreements.

Tier: P1 rule (proved field-free both directions; lattice sweep +
field realizations exhaustive as stated). P2, P3 rule (proved).
P4 rule (proved >= 3 for n > 8; censuses exhaustive at p = 11, 31).
P5 rule at p = 7 (proved + exhaustive); the p = 13 value 4 is an
exhaustive census (rule for the swept case, observation as a
general "+1 off the boundary" claim). P6 counting floor rule
(proved, numeric); height tables exact at p = 5, 7 (Dijkstra),
upper bounds by explicit words beyond; the cheapest-constant clause
is observation. P7 rule (by construction; verified).

Runs standalone (crt.py for P7 only). ~40 s, tiny memory.
ALL CHECKS PASSED (35).
"""

import sys, os, random
from math import gcd
from itertools import combinations
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

CHECKS = [0]
def check(name, ok):
    CHECKS[0] += 1
    print(("  [OK] " if ok else "  [FAIL] ") + name)
    if not ok:
        sys.exit("CHECK FAILED: " + name)

def divisors(n):
    return sorted(d for d in range(1, n + 1) if n % d == 0)

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

# ----------------------------------------------------------------- I
print("I. THE ORDER-COST LAW -- divisor-lattice separation (P1)")

def law(n, d):
    return omega(d) + 1 if d != n else max(omega(n), 1)

def min_separating(n, d, cap):
    """Exact min family size M subset Div(n) separating {d} from the
    other divisors; search sizes 1..cap, return size or None."""
    divs = divisors(n)
    others = [e for e in divs if e != d]
    masks = []
    for m in divs:
        dm = (m % d == 0)
        bm = 0
        for i, e in enumerate(others):
            if (m % e == 0) != dm:
                bm |= 1 << i
        masks.append(bm)
    full = (1 << len(others)) - 1
    for s in range(1, cap + 1):
        for combo in combinations(masks, s):
            u = 0
            for c in combo: u |= c
            if u == full:
                return s
    return None

n_targets = 0
for n in (6, 12, 30, 60, 360):
    for d in divisors(n):
        got = min_separating(n, d, law(n, d))
        assert got == law(n, d), (n, d, got)
        n_targets += 1
check("full d-sweep n in {6,12,30,60,360}: cost = omega(d)+1 "
      "(omega(n) at d=n), %d targets" % n_targets, True)
for d in (1, 2, 6, 30, 210, 1155, 2310):
    got = min_separating(2310, d, law(2310, d))
    check("n=2310 d=%d cost=%s = law %d" % (d, got, law(2310, d)),
          got == law(2310, d))

for p in (11, 13):
    n = p - 1
    units = list(range(1, p))
    ordx = {x: mult_order(x, p) for x in units}
    shadows = set()
    for k in range(n):
        for m in divisors(n):
            shadows.add(frozenset(x for x in units
                                  if pow(x, k * m, p) == 1))
    filters = set(frozenset(x for x in units if m % ordx[x] == 0)
                  for m in divisors(n))
    check("p=%d distinct one-leaf gate shadows = the %d filters"
          % (p, len(filters)), shadows == filters)
    for d in divisors(n):
        if d == n:
            fam = sorted(set(n // q for q in prime_factors(n)))
        else:
            fam = [d] + sorted(set(d // q for q in prime_factors(d)))
        target = set(x for x in units if ordx[x] == d)
        want = tuple(m % d == 0 for m in fam)
        decided = set(x for x in units
                      if tuple(m % ordx[x] == 0 for m in fam) == want)
        assert decided == target and len(fam) == law(n, d), (p, d)
    check("p=%d canonical programs decide [ord=d] at every d | %d"
          % (p, n), True)
check("p=11 primitivity read by %d = omega(10) gates"
      % law(10, 10), law(10, 10) == 2)
print()

# ---------------------------------------------------------------- II
print("II. THE INFINITY ROWS -- orbit-constancy (P2)")
def orbit_constant_triples(p, sample=None):
    n = p - 1
    units = list(range(1, p))
    cop = [u for u in range(1, n) if gcd(u, n) == 1]
    divs = divisors(n)
    triples = 0
    if sample is None:
        space = [(i, j, m, a, b) for i in range(n) for j in range(n)
                 for m in divs for a in units for b in units]
    else:
        rng = random.Random(83)
        space = [(rng.randrange(n), rng.randrange(n),
                  rng.choice(divs), rng.choice(units),
                  rng.choice(units)) for _ in range(sample)]
    for (i, j, m, a, b) in space:
        w = pow(a, i, p) * pow(b, j, p) % p
        bit = pow(w, m, p) == 1
        for u in cop:
            w2 = pow(a, i * u, p) * pow(b, j * u, p) % p
            if (pow(w2, m, p) == 1) != bit:
                return None
        triples += 1
    return triples

t7 = orbit_constant_triples(7)
check("p=7 exhaustive: every monomial gate orbit-constant "
      "(%s gate-point combinations)" % t7, t7 is not None)
t11 = orbit_constant_triples(11, sample=3000)
check("p=11 sampled (3000): orbit-constant", t11 is not None)
p = 7
orb = set((pow(3, u, p), pow(3, u, p)) for u in (1, 5))
split = set((a + b) % p == 3 for (a, b) in orb)
check("p=7 [a+b=3] splits the orbit {(3,3),(5,5)} -> infinite "
      "monomial price", split == {True, False})
print()

# --------------------------------------------------------------- III
print("III. THE PENTAGON PRICE -- read 3 vs cut 5 (P3, P4)")

def two_leaf_machinery(p):
    """dlog-based gate shadows; returns (pairs, idx, gate, shadows)
    with gate(i,j,m) -> bitmask and shadows = distinct masks."""
    n = p - 1
    g = next(x for x in range(2, p) if mult_order(x, p) == n)
    dlog = {pow(g, e, p): e for e in range(n)}
    units = list(range(1, p))
    pairs = [(a, b) for a in units for b in units]
    idx = {ab: t for t, ab in enumerate(pairs)}
    dls = [(dlog[a], dlog[b]) for (a, b) in pairs]
    def gate(i, j, m):
        bm = 0
        for t, (da, db) in enumerate(dls):
            if (i * da + j * db) * m % n == 0:
                bm |= 1 << t
        return bm
    shadows = set()
    for i in range(n):
        for j in range(n):
            for m in divisors(n):
                shadows.add(gate(i, j, m))
    return pairs, idx, gate, sorted(shadows)

def decides(masks, target, total):
    atoms = [total]
    for s in masks:
        nxt = []
        for a in atoms:
            x, y = a & s, a & ~s
            if x: nxt.append(x)
            if y: nxt.append(y)
        atoms = nxt
    return all((a & target) in (0, a) for a in atoms)

for p in (11, 31):
    pairs, idx, gate, shadows = two_leaf_machinery(p)
    total = (1 << len(pairs)) - 1
    th = next(x for x in range(2, p) if mult_order(x, p) == 5)
    O = 0
    for u in range(1, 5):
        O |= 1 << idx[(pow(th, u, p), pow(th, 2 * u, p))]
    fams = [[s] for s in shadows] + \
           [list(c) for c in combinations(shadows, 2)]
    bad = sum(1 for f in fams if decides(f, O, total))
    check("p=%d pentagon: all %d 1-/2-gate families fail "
          "(%d distinct shadows)" % (p, len(fams), len(shadows)),
          bad == 0)
    n = p - 1
    g1 = gate(2, n - 1, 1)   # [a^2 b^-1 = 1]
    g2 = gate(1, 0, 5)       # [a^5 = 1]
    g3 = gate(1, 0, 1)       # [a = 1]
    check("p=%d pentagon: 3-gate program g1&g2&~g3 = O exactly" % p,
          (g1 & g2 & ~g3) & total == O)
print()

# ---------------------------------------------------------------- IV
print("IV. THE CRYSTALLOGRAPHIC PRICE -- the Phi_6 orbit (P5)")
for p in (7, 13):
    pairs, idx, gate, shadows = two_leaf_machinery(p)
    total = (1 << len(pairs)) - 1
    z = next(x for x in range(2, p) if mult_order(x, p) == 6)
    zi = pow(z, -1, p)
    O = (1 << idx[(z, zi)]) | (1 << idx[(zi, z)])
    fams = [[s] for s in shadows] + \
           [list(c) for c in combinations(shadows, 2)]
    bad = sum(1 for f in fams if decides(f, O, total))
    check("p=%d Phi_6 orbit: all %d 1-/2-gate families fail "
          "(%d shadows)" % (p, len(fams), len(shadows)), bad == 0)
    if p == 7:
        g1, g2, g3 = gate(1, 1, 1), gate(1, 0, 3), gate(1, 0, 2)
        check("p=7 Phi_6: 3-gate program g1&~g2&~g3 = O "
              "(price exactly 3 -- the d = n discount)",
              (g1 & ~g2 & ~g3) & total == O)
    else:
        n3 = 0
        found = False
        for combo in combinations(shadows, 3):
            n3 += 1
            if decides(list(combo), O, total):
                found = True; break
        check("p=13 Phi_6: exhaustive 3-gate census (%d families): "
              "none decides -> price exactly 4" % n3, not found)
        g1, g2 = gate(1, 1, 1), gate(1, 0, 6)
        g3, g4 = gate(1, 0, 3), gate(1, 0, 2)
        check("p=13 Phi_6: 4-gate program g1&g2&~g3&~g4 = O",
              (g1 & g2 & ~g3 & ~g4) & total == O)
print()

# ----------------------------------------------------------------- V
print("V. THE HEIGHT FLOOR -- constants priced by formula ops (P6)")

def height_census(p, cost_cap=20, state_cap=400_000):
    """Exact min formula ops to each constant function on
    F_p* - {1} (meadow inverse: 0^-1 = 0). Level Dijkstra with
    stale-skip; early exit once all constants are settled and the
    level exceeds their max (no later derivation can improve)."""
    dom = list(range(2, p))
    leaf = tuple(dom)
    consts = {tuple(c for _ in dom): c for c in range(2, p)}
    best = {leaf: 0}
    by_cost = {0: [leaf]}
    found = {}
    cmax = 0
    while cmax <= cost_cap and len(best) < state_cap:
        layer = [f for f in by_cost.get(cmax, [])
                 if best.get(f) == cmax]
        settled = [(f, c) for c, fl in by_cost.items() if c <= cmax
                   for f in fl if best.get(f) == c]
        new = {}
        def offer(gf, c):
            if c > cost_cap: return
            if gf in best and best[gf] <= c: return
            if gf not in new or new[gf] > c: new[gf] = c
        for f in layer:
            offer(tuple((1 - v) % p for v in f), cmax + 1)
            offer(tuple(pow(v, p - 2, p) if v else 0 for v in f),
                  cmax + 1)
            for gth, cg in settled:
                offer(tuple(x * y % p for x, y in zip(f, gth)),
                      cmax + cg + 1)
        for gf, c in new.items():
            best[gf] = c
            by_cost.setdefault(c, []).append(gf)
        for cf, c in consts.items():
            if cf in best:
                found[c] = best[cf]
        if len(found) == len(consts) and \
           cmax >= max(found.values()):
            break
        cmax += 1
    return found, len(found) == len(consts)

F = [1]
for t in range(1, 25):
    F.append(2 * F[t - 1] +
             sum(F[i] * F[t - 1 - i] for i in range(t)))
cum = [sum(F[:t + 1]) for t in range(25)]
def L_min(p):
    return next(t for t in range(25) if cum[t] >= p - 2)

print("  counting: F(t) t=0..7:", F[:8])
for p in (5, 7):
    hs, exact = height_census(p)
    tab = " ".join("h(%d)=%d" % (c, hs[c]) for c in sorted(hs))
    print("  p=%d exact: %s   (L_min=%d)" % (p, tab, L_min(p)))
    check("p=%d every constant reached exactly; max h(c)=%d >= "
          "L_min=%d" % (p, max(hs.values()), L_min(p)),
          exact and max(hs.values()) >= L_min(p))
    check("p=%d h(-1)=%d <= 6 (P77 word bound)" % (p, hs[p - 1]),
          hs[p - 1] <= 6)
    check("p=%d -1 is a cheapest nontrivial constant" % p,
          hs[p - 1] == min(hs.values()))
for p in (11, 13, 31):
    okw = all((1 - pow(a, p - 2, p)) * pow(1 - a, p - 2, p) * a % p
              == p - 1 for a in range(2, p))
    check("p=%d the 6-op P77 word makes -1 on every unit != 1" % p,
          okw)
print("  counting floor growth: L_min(10^3)=%d, L_min(10^6)=%d"
      % (next(t for t in range(25) if cum[t] >= 10 ** 3),
         next(t for t in range(25) if cum[t] >= 10 ** 6)))
print()

# ---------------------------------------------------------------- VI
print("VI. RING ASSEMBLY -- one ring gate = k channel gates (P7)")
from crt import RAD_RING
R = RAD_RING
N = R.N
rng = random.Random(83)
tested = 0
ok = True
while tested < 300:
    a, b = rng.randrange(1, N), rng.randrange(1, N)
    if gcd(a, N) != 1 or gcd(b, N) != 1: continue
    w = a * pow(b, -1, N) % N
    for m in (1, 2, 4, 240):
        ring = pow(w, m, N) == 1
        per = all(pow(w % q, m, q) == 1 for q in R.primes)
        if ring != per: ok = False
    tested += 1
check("RAD gate_m(ab^-1) = AND of 7 channel bits "
      "(300 unit pairs x m in {1,2,4,240})", ok)
print()

print("ALL CHECKS PASSED (%d)" % CHECKS[0])
