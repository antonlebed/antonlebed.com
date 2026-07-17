"""
explore_one_way.py -- ONE-WAY GROWTH (sibling of explore_growth_laws.py
.. explore_induction_ceiling.py).

THE QUESTION. Design a demand whose endpoint provably hides its
route -- route posterior near-uniform over many histories, every
endpoint, every beta: maximal amnesia as a design target, "capturing
the path into a function is a contradiction" made precise. Seeds:
the 2^|D| confound (explore_observer_view.py), the fossil paradox
(explore_induction_ceiling.py: zero menu drift forces uniform route
posteriors -- and a drift-free menu needs re-ground windows, so
growing NEW windows fights hiding). Design + predictions PR1-PR7
fixed before the run, plus a paper attack.

MODEL (thermometer-pair conventions). State N, admissible move m >= 2
multiplies, weight m^(-beta)/Z_N, demand Markov (admissibility reads
the state only); MANY-WINDOW demand := every admissible move coprime
to the state. Route posterior given (endpoint, age, G): weight prop
prod over interior states of 1/Z (numerators cancel -- the
route-weight cancellation, explore_observer_view.py). Designed worlds carry explicit
finite menus (any beta > 0 legitimate); the plain-breadth part uses
truncated D-IND (squarefree m <= M = 200 coprime to state, stated).

FINDINGS (tiers per the standard naming scale; run record below).

1. THE BALANCE CRITERION (rule, immediate). The route posterior at
   (N, tau) is uniform iff the product of interior normalizers is the
   same along every route -- all route information lives in the
   normalizer sequence; the perfect fossil (the equivalence zero
   drift <=> uniform routes <=> perfect fossil, established in
   earlier work) is the special case "menu literally constant".
   Design target = normalizer balance.

2. THE EXCHANGE-RIGIDITY THEOREM (rule, proved; the all-beta answer
   is NO). A many-window demand cannot hold >= 2 routes to any
   (N, tau) with route posterior uniform for ALL beta in an open
   interval. Proof: uniformity at all beta makes interior-normalizer
   products equal as Dirichlet series; (a) tau = 2, fully general --
   the two interior menus coincide as SETS (Dirichlet uniqueness),
   so each route's second move also sits in the OTHER route's menu
   and is thereby coprime to the other first move: the two set
   inclusions primes(m) <= primes(m') <= primes(m) follow, and equal
   supports + coprime cofactors force m = m' (v_p(N) = v_p(m) on the
   shared support): contradiction;
   (b) any tau, EXCHANGE-CLOSED route sets (adjacent coprime moves
   commute admissibly -- D-IND and D-SEMI are; D-MEM, not coprime,
   obeys the same conclusion via its own bar, see below): a
   transposition-adjacent pair shares all interior states but one,
   the odd pair's menus must coincide as sets, and the transposed
   move is BARRED from its own state's menu -- by coprimality in a
   many-window demand, and in D-MEM because a move dividing the
   state carries no new prime: contradiction.
   So beta-free perfect amnesia forces a single route IN MANY-WINDOW
   GROWTH -- the beta-free escape lives in DEPTH: a CONSTANT menu
   (drift-free, old windows re-ground -- {2, 3} at every state) is a
   beta-free amnesiac with exponentially many routes (C(a+b, a) to
   2^a 3^b; verified: 6 routes to 36, uniform EXACT at beta = 1 AND
   2), and coprimality forbids constant menus (a taken move may not
   recur). Beta-free amnesia is a DEPTH privilege -- drift-free menus
   suffice (the equivalence above); whether they are necessary beyond the many-window
   class is OPEN -- and breadth's skew is STRUCTURAL: no D-IND
   endpoint with >= 2 routes is route-uniform across any temperature
   interval.
   Mechanical witness: the 2^(-beta) coefficient is 1 in Z(3), 0 in
   Z(2) (coprimality) -- verified S1. Corroboration in a bounded
   design space (junk menus over pools |J2| = 15, |J3| = 17, subsets
   <= 4): 112 designs tuned at beta = 1, ZERO tuned at beta = 1 AND
   beta = 2 simultaneously -- verified S2. Fully-general multi-route
   rigidity beyond the exchange class: OPEN (named).

3. THE TUNED AMNESIAC (constructions, exact; the fixed-beta answer is
   YES). At one designed temperature the balance criterion is a
   finite system of mass equations, solved exactly by Egyptian-
   fraction junk menus (junk = admissible-but-off-cone moves: coprime
   to the state, state*m not dividing the endpoint). k = 2 specimen
   (beta_0 = 1): menu(1) = {2,3}, menu(2) = {3,5,15}, menu(3) =
   {2,10}; Z(2) = Z(3) = 3/5 exactly, so BOTH two-route endpoints (6
   and 30) get posterior spread EXACTLY 0 (Fractions), route entropy
   log 2; detuned at beta = 2 the odds snap to 117:70 ~ 1.6714
   (verified S1). k = 3 build (endpoint 30, single-prime moves, age
   3): a divisor-lattice search with p-adic feasibility filters
   (junk at state s has denominators coprime to s -- the 2-adic
   obstruction, found during hand-design) finds zeta_1 = 1, zeta_2 = 49/97:
   menu(2) = {3,5,7,11,13,17,21,33,55,1001,19635}, menu(3) =
   {2,5,7,11,22,55,385}, menu(5) = {2,3,7,42}, menu(6) =
   {5,7,11,35,55,65,143,455,37345,44135,97097}, menu(10) =
   {3,7,39,429,1067,22407,97097}, menu(15) = {2,194}; all 3! = 6
   routes exactly equiprobable (2.585 bits of route hidden), detuned
   spread 0.317 at beta = 2 (verified S3). Routes scale k! by
   design; BUILT at k = 2, 3; general-k existence is ARGUED
   (divergent junk subsums, Egyptian reachability) -- not a rule.

4. THE FOSSIL SPLIT (rule -- computed instance + the theorem pair;
   verified S4). At fixed beta the drift/uniformity/fossil
   equivalence (zero drift <=> uniform routes <=> perfect fossil)
   COMES APART: the tuned k = 2
   world has NONZERO menu drift, route posterior UNIFORM at beta_0
   (maximal amnesia), and witness gap I(beta; path) - I(beta; dated)
   = 0.015359 - 0.012242 = 0.003117 nats > 0 over the {1,2}
   beta-ensemble, ages <= 2 (chain identity < 1e-12,
   explore_induction_ceiling.py's MI form) -- a world that forgets
   its past WITHOUT
   becoming a fossil: memory-for-the-generator and amnesia coexist by
   tuning. Beta-free the notions re-fuse in the NONVACUOUS reading
   (finding 2 + the equivalence above): uniformity over >= 2 routes at all beta lives
   only where menus never drift (a single-route world is uniform
   vacuously, drift or not); the fixed-beta construction is the only
   many-window escape, and it is tuned.

5. THE FOOTPRINT LAW (observation across beta-grid x supports;
   verified S5). In plain truncated D-IND the route posterior's ONLY
   leak is the menu-mass footprint of the used primes: the
   singleton-footprint model w prop prod_j 1/(Z_empty - sum_{p in
   S_j} r_p) (r_p = menu mass p removes; overlaps dropped) captures
   the leak to KL(exact || model) / KL(exact || uniform) = 3.3e-4 /
   2.6e-5 / 1.4e-7 at beta = 1.5/2/3 on support {11,13,17,19} (and
   to roundoff at {101,...}); the posterior mode is ALWAYS
   ascending-primes (heavy footprint first) -- the staged creation
   cascade (explore_observer_view.py) re-derived as the unique leak. HONEST MISS at the
   overlap-dominated corner: on {2,3,5,7} the model captures only
   ~53% (beta 1.5) / ~28% (beta 2) of the leak and at beta = 3 its
   mass goes NEGATIVE (r_2 + r_3 + r_5 > Z_empty) -- the first-order
   model is a HIGH-SUPPORT law; small-prime history-reading is
   overlap-dominated.

6. FREE AMNESIA AT HEIGHT (observation in range; verified S5).
   Endpoints supported on high primes hide their history for free at
   EVERY tested beta: KL to uniform = 5.0e-9 / 3.8e-10 / 6.2e-13
   nats at beta = 1.5/2/3 for {101,103,107,109} (entropy ratio
   1.0000); {11,13,17,19} already sits at 4.2e-4 / 1.4e-4 / 8.1e-6.
   Breadth's 0.737 route-entropy ratio (explore_induction_ceiling.py) is a SMALL-PRIME
   artifact: {2,3,5,7} reads 0.9191 / 0.8261 / 0.6308 at beta =
   1.5/2/3 (KL 0.257 / 0.553 / 1.173 -- COOLING READS HISTORY at
   small support, where footprints fatten with beta; at high support
   cooling erases it, footprints ~ p^(-beta) -> 0).

THE HEADLINE. The design question resolves as a trichotomy: exact
amnesia at EVERY temperature is a THEOREM-level impossibility for
many-window growth (exchange rigidity), its beta-free escape a DEPTH
privilege -- constant menus, the column or any fixed menu ground into
depth, hide exponentially many routes at every beta, and coprimality
forbids them (the fossil paradox's other face); exact
amnesia at the world's OWN temperature is a CONSTRUCTION (Egyptian-
fraction menu balance, k! routes hidden exactly, built at k = 2, 3);
and near-perfect amnesia at every tested temperature is FREE at
height in plain breadth (the footprint law: the only leak is the used
primes' menu-mass footprint, vanishing as support climbs). "Capturing the
path into a function is a contradiction" made precise: true at all
temperatures, designable at one -- history-hiding is thermally tuned,
and a world hides its past exactly at the temperature it was grown.
(Exploitation contact, verify-first, NOT begun: information-theoretic
commitment/hiding schemes; Egyptian-fraction representation theory
for the general-k construction.)

HONEST LIMITS. (a) Rigidity proved for tau = 2 pairs (general) and
exchange-closed route sets; multi-route non-exchange demands OPEN.
(b) Constructions verified at k <= 3, dated channel (all routes to
the built endpoints share one age by design); the general-k and
mixed-age (constant-Z) designs are argued only. (c) The footprint
model is first-order and breaks where overlaps dominate (finding 5).
(d) S4's gap value is ensemble-specific (beta in {1,2}, ages <= 2,
uniform priors). (e) D-IND truncation M = 200 stated; beta = 1 is
legitimate throughout the designed worlds (finite menus).

RUN RECORD (this file, python explore_one_way.py, ~0.5 s -- the
p-adic feasibility filter keeps the k=3 divisor-lattice search
near-instant):
  S0 machinery: 5 age-2 paths in W1, total probability 1 exact at
     beta = 1 and 2.
  S1 tuned specimen: Z(2) = Z(3) = 3/5; endpoints 6 and 30 spread 0
     exact; detune odds 117/70; rigidity witness coefficients (1, 0);
     depth escape: constant menu {2,3}, 6 routes to 36 at age 4,
     uniform exact at beta = 1 and 2.
  S2 rigidity search: pools 15/17, 112 beta=1-tuned, 0 double-tuned.
  S3 k=3 build: zeta_1 = 1, zeta_2 = 49/97, menus above; 6 routes
     uniform exact, H = log 6 = 1.7918 nats = 2.585 bits; beta=2
     spread 0.317099.
  S4 fossil split: I(path) = 0.015359, I(dated) = 0.012242, gap =
     0.003117 nats; chain identity < 1e-12; drift nonzero.
  S5 footprint (M = 200): table in findings 5-6; KL chain strict at
     every beta; mode ascending at every beta; model BREAKS (negative
     mass) at beta = 3 on {2,3,5,7}; {2,3,5,7} beta=2 entropy ratio
     0.8261.
  Total: 125 asserts green.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

from fractions import Fraction
from math import gcd, log, log2
from itertools import permutations

checks = 0


def ok(cond, msg):
    global checks
    assert cond, msg
    checks += 1


def squarefree(n):
    d = 2
    while d * d <= n:
        if n % (d * d) == 0:
            return False
        if n % d == 0:
            n //= d
        d += 1
    return True


# ---------- machinery: explicit-menu worlds, exact posteriors ----------

def zmass(menu, e):
    """Normalizer sum m^(-e) over a menu, exact (e integer)."""
    return sum(Fraction(1, m ** e) for m in menu)


def paths_of_age(menus, age):
    """All admissible paths (move tuples) of the given age from seed 1."""
    out = []

    def rec(state, path):
        if len(path) == age:
            out.append(tuple(path))
            return
        for m in menus.get(state, ()):
            path.append(m)
            rec(state * m, path)
            path.pop()

    rec(1, [])
    return out


def path_prob(menus, path, e):
    """Exact thermal probability of a path at beta = e (integer)."""
    p = Fraction(1)
    state = 1
    for m in path:
        p *= Fraction(1, m ** e) / zmass(menus[state], e)
        state *= m
    return p


def route_posterior(menus, endpoint, age, e):
    """Exact posterior over routes given (endpoint, age, beta=e)."""
    routes = [p for p in paths_of_age(menus, age)
              if prod(p) == endpoint]
    w = [path_prob(menus, p, e) for p in routes]
    tot = sum(w)
    return routes, [x / tot for x in w]


def prod(xs):
    r = 1
    for x in xs:
        r *= x
    return r


def entropy_nats(probs):
    return -sum(float(p) * log(float(p)) for p in probs if p > 0)


# ---------- exact Egyptian subset-sum DFS ----------

def egyptian_dfs(target, pool, maxlen, node_cap=800000):
    """Find a subset of pool (distinct ints) with sum of 1/m == target.
    Pool sorted ascending. Returns list or None."""
    pool = sorted(pool)
    recip = [Fraction(1, m) for m in pool]
    suffix = [Fraction(0)] * (len(pool) + 1)
    for i in range(len(pool) - 1, -1, -1):
        suffix[i] = suffix[i + 1] + recip[i]
    nodes = [0]

    def rec(i, rem, acc):
        nodes[0] += 1
        if nodes[0] > node_cap:
            return None
        if rem == 0:
            return list(acc)
        if len(acc) >= maxlen or i >= len(pool):
            return None
        if suffix[i] < rem:
            return None
        for j in range(i, len(pool)):
            if recip[j] > rem:
                continue
            # even taking every remaining term cannot reach rem
            if suffix[j] < rem:
                return None
            acc.append(pool[j])
            got = rec(j + 1, rem - recip[j], acc)
            if got is not None:
                return got
            acc.pop()
            if nodes[0] > node_cap:
                return None
        return None

    return rec(0, target, [])


def junk_pool(state, endpoint, route_moves, lo=2, hi=3000):
    """Admissible junk at a state: coprime, squarefree, off-cone
    (state*m does not divide the endpoint), not a route move."""
    out = []
    for m in range(lo, hi):
        if m in route_moves:
            continue
        if gcd(m, state) != 1 or not squarefree(m):
            continue
        if endpoint % (state * m) == 0:
            continue
        out.append(m)
    return out


def prime_factors(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def divisors_of(primes):
    divs = [1]
    for p in primes:
        divs += [d * p for d in divs]
    return sorted(divs)


def solve_state_target(target, state, endpoint, route_moves):
    """Exact junk set with sum 1/m == target at a state, searching only
    unit fractions whose denominators divide a smooth modulus L that
    contains the target's denominator (keeps the DFS pool small and the
    subset-sum rational-exact)."""
    if target == 0:
        return []
    denp = prime_factors(target.denominator)
    if any(gcd(p, state) != 1 for p in denp):
        return None
    extras = [p for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
              if gcd(p, state) == 1 and p not in denp]
    for r in range(2, 7):
        P = denp + extras[:r]
        if len(P) > 8:
            break
        pool = []
        for m in divisors_of(P):
            if m < 4 or m in route_moves:
                continue
            if endpoint % (state * m) == 0:
                continue
            pool.append(m)
        if sum(Fraction(1, m) for m in pool) < target:
            continue
        got = egyptian_dfs(target, pool, maxlen=10, node_cap=300000)
        if got is not None:
            return got
    return None


# =====================================================================
print("S0 machinery")
# =====================================================================

W1 = {1: [2, 3], 2: [3, 5, 15], 3: [2, 10]}
allp = paths_of_age(W1, 2)
tot = sum(path_prob(W1, p, 1) for p in allp)
ok(tot == 1, "S0: age-2 path probabilities sum to 1 exactly")
tot2 = sum(path_prob(W1, p, 2) for p in allp)
ok(tot2 == 1, "S0: same at beta=2")
print("  age-2 paths in W1: %d, total prob 1 exact at beta=1,2" % len(allp))

# =====================================================================
print("S1 the tuned amnesiac (k=2 specimen) + rigidity witness")
# =====================================================================

z2, z3 = zmass(W1[2], 1), zmass(W1[3], 1)
ok(z2 == Fraction(3, 5) and z3 == Fraction(3, 5),
   "S1/PR1: Z(2) = Z(3) = 3/5 exactly at beta=1")
for endpoint in (6, 30):
    routes, post = route_posterior(W1, endpoint, 2, 1)
    ok(len(routes) == 2, "S1: two routes to %d" % endpoint)
    ok(post[0] == post[1] == Fraction(1, 2),
       "S1/PR1: posterior at %d uniform EXACTLY (beta=1)" % endpoint)
    print("  endpoint %d: routes %s, posterior spread 0 exact, H = log 2"
          % (endpoint, routes))

# detune at beta = 2
routes6, post6 = route_posterior(W1, 6, 2, 2)
i23 = routes6.index((2, 3))
i32 = routes6.index((3, 2))
odds = post6[i23] / post6[i32]
ok(odds == Fraction(117, 70),
   "S1/PR2: detuned odds (2-first):(3-first) = 117:70 exactly at beta=2")
print("  beta=2 detune: odds = %s ~ %.4f (tuning is not beta-free)"
      % (odds, float(odds)))

# rigidity witness: the route move 2 sits in menu(3); no coprime menu at
# state 2 can contain 2 -- the 2^(-beta) Dirichlet coefficient differs.
ok(2 in W1[3], "S1: route move 2 in menu(3)")
ok(all(gcd(m, 2) == 1 for m in W1[2]),
   "S1: menu(2) is coprime to 2, so it cannot contain 2")
print("  rigidity witness: coeff of 2^(-beta) is 1 in Z(3), 0 in Z(2)")

# the depth escape: a CONSTANT menu (drift-free, NOT coprime -- old
# windows re-ground) is beta-free amnesiac with exponentially many
# routes; coprimality forbids constant menus, so the escape lives in
# depth only.
WC = {}
frontier = [1]
for _ in range(4):
    nxt = []
    for s in frontier:
        if s not in WC:
            WC[s] = [2, 3]
            nxt += [2 * s, 3 * s]
    frontier = nxt
for e in (1, 2):
    routes36, post36 = route_posterior(WC, 36, 4, e)
    ok(len(routes36) == 6, "S1: C(4,2) = 6 routes to 36 at age 4")
    ok(all(p == Fraction(1, 6) for p in post36),
       "S1: constant-menu world uniform EXACTLY at beta=%d" % e)
print("  depth escape: constant menu {2,3} -> 6 routes to 36, uniform "
      "exact at beta=1 AND beta=2 (beta-free, two windows, drift-free)")

# =====================================================================
print("S2 rigidity search (bounded design space, endpoint 6)")
# =====================================================================
# menu(2) = {3} + J2, menu(3) = {2} + J3; uniformity at beta=e means
# Z_2 = Z_3, i.e. sum(J2, e) - sum(J3, e) = 2^-e - 3^-e.

pool2 = junk_pool(2, 6, {3}, lo=4, hi=41)      # odd squarefree, m != 3
pool3 = junk_pool(3, 6, {2}, lo=4, hi=41)


def subset_sums(pool, maxlen):
    """All subsets up to maxlen: list of (sum_beta1, sum_beta2)."""
    res = [(Fraction(0), Fraction(0))]
    subs = [((), Fraction(0), Fraction(0))]
    for _ in range(maxlen):
        new = []
        for s, a, b in subs:
            last = s[-1] if s else 0
            for m in pool:
                if m > last:
                    new.append((s + (m,), a + Fraction(1, m),
                                b + Fraction(1, m * m)))
        subs = new
        res.extend((a, b) for _, a, b in subs)
        if not subs:
            break
    return res


sums2 = subset_sums(pool2, 4)
sums3 = subset_sums(pool3, 4)
need1 = Fraction(1, 2) - Fraction(1, 3)        # s2 - s3 at beta=1
need2 = Fraction(1, 4) - Fraction(1, 9)        # s2 - s3 at beta=2
by_b1 = {}
for a, b in sums3:
    by_b1.setdefault(a, []).append(b)
n_single = 0
n_double = 0
for a, b in sums2:
    for b3 in by_b1.get(a - need1, ()):
        n_single += 1
        if b - b3 == need2:
            n_double += 1
print("  pools |J2|=%d |J3|=%d; beta=1-tuned designs: %d; "
      "double-tuned (beta=1 AND 2): %d" %
      (len(pool2), len(pool3), n_single, n_double))
ok(n_single >= 1, "S2/PR3: at least one beta=1-tuned design exists")
ok(n_double == 0, "S2/PR3: NO design is tuned at beta=1 and beta=2 "
                  "simultaneously (exchange rigidity, corroborated)")

# =====================================================================
print("S3 the k=3 build (endpoint 30, single-prime moves, age 3)")
# =====================================================================
# depth-1 states 2,3,5 (route moves = other two primes); depth-2 states
# 6,10,15 (route move = the last prime). Balance Z within each depth at
# beta=1; targets' denominators must dodge the junk pools' p-adic
# constraints (found during hand-design), so the solver picks its own target.

ROUTE1 = {2: [3, 5], 3: [2, 5], 5: [2, 3]}
ROUTE2 = {6: [5], 10: [3], 15: [2]}


def solve_depth(states, route_moves, endpoint, hand_cands=()):
    """Find junk sets making Z equal across states at beta=1.

    Feasibility filter (the 2-adic lesson from hand-design): junk at
    state s has denominators coprime to s, so any reachable target has
    denominator coprime to s -- candidates failing that for ANY state
    are dropped before the DFS ever runs. Hand-derived candidates
    (found during hand-design) are tried first."""
    masses = {s: zmass(route_moves[s], 1) for s in states}
    base = max(masses.values())
    anchor = max(states, key=lambda s: masses[s])
    apool = junk_pool(anchor, endpoint, set(route_moves[anchor]),
                      lo=4, hi=201)
    cands = list(hand_cands)
    for i, m1 in enumerate(apool):
        cands.append((base + Fraction(1, m1), [m1]))
        for m2 in apool[i + 1:]:
            if m2 <= 60 or m1 <= 60:
                cands.append((base + Fraction(1, m1) + Fraction(1, m2),
                              [m1, m2]))
    cands[len(hand_cands):] = sorted(cands[len(hand_cands):],
                                     key=lambda t: t[0])
    attempts = 0
    for zeta, ajunk in cands:
        feasible = all(
            (zeta - masses[s] >= 0
             and gcd((zeta - masses[s]).denominator, s) == 1)
            for s in states)
        if not feasible:
            continue
        attempts += 1
        if attempts > 300:
            break
        sol = {anchor: ajunk}
        good = True
        for s in states:
            if s == anchor:
                continue
            got = solve_state_target(zeta - masses[s], s, endpoint,
                                     set(route_moves[s]))
            if got is None:
                good = False
                break
            sol[s] = got
        if good:
            return zeta, sol
    return None, None


zeta1, junk1 = solve_depth([2, 3, 5], ROUTE1, 30,
                           hand_cands=[(Fraction(1), [7, 42])])
ok(junk1 is not None, "S3/PR4: depth-1 balance found")
zeta2, junk2 = solve_depth([6, 10, 15], ROUTE2, 30,
                           hand_cands=[(Fraction(5, 7), [7, 14])])
ok(junk2 is not None, "S3/PR4: depth-2 balance found")

W3 = {1: [2, 3, 5]}
for s in (2, 3, 5):
    W3[s] = sorted(ROUTE1[s] + junk1[s])
for s in (6, 10, 15):
    W3[s] = sorted(ROUTE2[s] + junk2[s])
print("  zeta1 = %s, zeta2 = %s" % (zeta1, zeta2))
for s in (2, 3, 5, 6, 10, 15):
    print("    menu(%d) = %s" % (s, W3[s]))

# verify legality of every designed menu
for s, menu in W3.items():
    for m in menu:
        ok(gcd(m, s) == 1 and squarefree(m),
           "S3: move %d at state %d coprime + squarefree" % (m, s))
        if m not in (ROUTE1.get(s, []) + ROUTE2.get(s, []) + [2, 3, 5]):
            ok(30 % (s * m) != 0,
               "S3: junk %d at state %d off-cone" % (m, s))
for s in (2, 3, 5):
    ok(zmass(W3[s], 1) == zeta1, "S3: Z(%d) = zeta1 exactly" % s)
for s in (6, 10, 15):
    ok(zmass(W3[s], 1) == zeta2, "S3: Z(%d) = zeta2 exactly" % s)

routes30, post30 = route_posterior(W3, 30, 3, 1)
ok(len(routes30) == 6, "S3: six orderings of 30 at age 3")
ok(all(p == Fraction(1, 6) for p in post30),
   "S3/PR4: posterior uniform EXACTLY over 6 routes at beta=1")
print("  posterior over 3! = 6 routes: uniform exact; H = log 6 = %.4f "
      "nats = %.3f bits hidden" % (log(6), log2(6)))

routes30b, post30b = route_posterior(W3, 30, 3, 2)
spread = max(post30b) - min(post30b)
ok(spread > 0, "S3/PR4: detuned at beta=2 (spread > 0)")
print("  beta=2 detune: max-min posterior = %.6f" % float(spread))

# =====================================================================
print("S4 the fossil split (tuned world W1, beta-ensemble {1,2})")
# =====================================================================

BETAS = (1, 2)
AGES = (1, 2)
# joint over (beta, tau, path), uniform prior on beta and tau
joint = {}
for e in BETAS:
    for tau in AGES:
        for p in paths_of_age(W1, tau):
            pr = Fraction(1, len(BETAS) * len(AGES)) * path_prob(W1, p, e)
            joint[(e, tau, p)] = pr
tot = sum(joint.values())
ok(tot == 1, "S4: joint normalized exactly")


def mi(joint, key_x):
    """I(beta; X) for X = key_x(tau, path), exact probs -> float nats."""
    px = {}
    pbx = {}
    for (e, tau, p), pr in joint.items():
        x = key_x(tau, p)
        px[x] = px.get(x, Fraction(0)) + pr
        pbx[(e, x)] = pbx.get((e, x), Fraction(0)) + pr
    pb = Fraction(1, len(BETAS))
    s = 0.0
    for (e, x), pr in pbx.items():
        if pr > 0:
            s += float(pr) * log(float(pr) / (float(pb) * float(px[x])))
    return s


I_path = mi(joint, lambda tau, p: (tau, p))
I_dated = mi(joint, lambda tau, p: (tau, prod(p)))
gap = I_path - I_dated
print("  I(beta; path) = %.6f, I(beta; dated) = %.6f, gap = %.6f nats"
      % (I_path, I_dated, gap))
ok(gap > 1e-6, "S4/PR5: witness gap POSITIVE in the tuned world")
ok(W1[2] != W1[3] and W1[1] != W1[2],
   "S4/PR5: menu drift nonzero (menus differ as sets)")
# chain identity: I(beta; path) = I(beta; dated) + I(beta; route | dated)
I_route_given = 0.0
dated_groups = {}
for (e, tau, p), pr in joint.items():
    dated_groups.setdefault((tau, prod(p)), {})[(e, p)] = pr
for (tau, n), grp in dated_groups.items():
    pd = sum(grp.values())
    pe = {}
    pp = {}
    for (e, p), pr in grp.items():
        pe[e] = pe.get(e, Fraction(0)) + pr
        pp[p] = pp.get(p, Fraction(0)) + pr
    for (e, p), pr in grp.items():
        if pr > 0:
            I_route_given += float(pr) * log(
                float(pr) * float(pd) / (float(pe[e]) * float(pp[p])))
ok(abs(I_path - I_dated - I_route_given) < 1e-12,
   "S4: chain identity exact (the MI witness gap, ch. sixteen)")
print("  amnesia at beta=1 (uniform routes) + positive gap + drift:"
      " the drift/uniformity/fossil equivalence splits at fixed beta")

# =====================================================================
print("S5 the footprint law (plain D-IND, M = 200)")
# =====================================================================

M = 200
ENDPOINTS = [(2, 3, 5, 7), (11, 13, 17, 19), (101, 103, 107, 109)]
FBETAS = (1.5, 2.0, 3.0)


def dind_menu_mass(used, beta):
    """Z of the D-IND menu (squarefree m <= M coprime to used) as float."""
    s = 0.0
    for m in range(2, M + 1):
        if squarefree(m) and all(m % p for p in used):
            s += m ** (-beta)
    return s


def removed_mass(p, beta):
    """Mass of squarefree menu elements divisible by p (footprint r_p)."""
    s = 0.0
    for m in range(2, M + 1):
        if m % p == 0 and squarefree(m):
            s += m ** (-beta)
    return s


def kl(p, q):
    return sum(pi * log(pi / qi) for pi, qi in zip(p, q) if pi > 0)


results = {}
for beta in FBETAS:
    z0 = dind_menu_mass((), beta)
    for supp in ENDPOINTS:
        rp = {p: removed_mass(p, beta) for p in supp}
        exact_w = []
        model_w = []
        perms = list(permutations(supp))
        for sig in perms:
            we = 1.0
            wm = 1.0
            for j in range(1, 4):          # interior states, depths 1..3
                used = sig[:j]
                we /= dind_menu_mass(used, beta)
                wm /= (z0 - sum(rp[p] for p in used))
            exact_w.append(we)
            model_w.append(wm)
        se = sum(exact_w)
        exact = [w / se for w in exact_w]
        uni = [1.0 / len(perms)] * len(perms)
        kl_u = kl(exact, uni)
        if min(model_w) <= 0:
            # first-order breakdown: the singleton footprints of the
            # used primes exceed the whole menu mass (overlap-dominated)
            kl_m = None
        else:
            sm = sum(model_w)
            model = [w / sm for w in model_w]
            kl_m = kl(exact, model)
            if -1e-12 < kl_m < 0:
                kl_m = 0.0      # float wall: identical to roundoff
        h_ratio = entropy_nats(exact) / log(len(perms))
        mode = perms[max(range(len(perms)), key=lambda i: exact[i])]
        results[(beta, supp)] = (kl_u, kl_m, h_ratio, mode)
        print("  beta=%.1f supp=%s: KL(uni) = %.3e, KL(model) = %s, "
              "H-ratio = %.4f, mode = %s"
              % (beta, supp, kl_u,
                 "BREAKS (neg mass)" if kl_m is None else "%.3e" % kl_m,
                 h_ratio, mode))

for beta in FBETAS:
    a = results[(beta, ENDPOINTS[0])][0]
    b = results[(beta, ENDPOINTS[1])][0]
    c = results[(beta, ENDPOINTS[2])][0]
    ok(a > b > c, "S5/PR6: KL chain strict at beta=%.1f" % beta)
    ok(c < 1e-6, "S5/PR6: high-support KL < 1e-6 at beta=%.1f" % beta)
    ok(results[(beta, ENDPOINTS[0])][3] == (2, 3, 5, 7),
       "S5/PR6: mode ascending (small primes first) at beta=%.1f" % beta)
    for supp in ENDPOINTS[1:]:
        kl_u, kl_m, _, _ = results[(beta, supp)]
        ok(kl_m / kl_u < 0.10,
           "S5/PR7: footprint model captures >90%% of the leak, "
           "beta=%.1f supp=%s" % (beta, supp))

hr = results[(2.0, ENDPOINTS[0])][2]
ok(0.5 < hr < 0.95, "S5: {2,3,5,7} beta=2 entropy ratio in (0.5, 0.95)")
print("  {2,3,5,7} beta=2 entropy ratio %.4f (cf. breadth's 0.737 at "
      "M=12, mixed ensemble)" % hr)

print("\nTotal: %d asserts green." % checks)
