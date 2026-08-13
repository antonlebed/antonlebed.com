"""explore_rogue_world.py -- THE ROGUE WORLD
(third of the amnesia-certificate sequence:
explore_forgetting_certificate.py, explore_working_amnesiac.py;
growth conventions of explore_one_way.py).

THE QUESTION. The amnesia certificate's open obstruction: does
robust flatness (route posterior uniform at EVERY temperature)
FORCE the weight-side witness (equal interior-normalizer multisets
along all routes) beyond the exchange class? The abstract collision
exists -- Z_{2,4,8} * Z_{2,16} = Z_{2,4} * Z_{2,8,32} as Dirichlet
polynomials (equal products at every beta, distinct menu multisets).
Is it REALIZABLE as a closed designed fiber: menus assigned per
state so that a dated age-3 fiber contains EXACTLY two routes whose
interior normalizer multisets are {Z(1), Z_{2,4,8}, Z_{2,16}} vs
{Z(1), Z_{2,4}, Z_{2,8,32}}? Age 2 is barred (flatness at all beta
forces the two interior normalizers equal, and Dirichlet uniqueness
makes that menu coincidence -- the witness present); age >= 3 is
the question. A realization settles the obstruction NEGATIVELY --
grade S without the weight-side witness. The kill direction: a
derivation that the realization constraints (common seed normalizer,
endpoint equality, menus as functions of the state, fiber closure)
force coincidence anyway.

MODEL. State N a positive integer, admissible move m >= 2
multiplies, weight m^-beta / Z_N with Z_N the state's menu mass;
menus are functions of the state integer (the demand is Markov).
Dated fiber (N, tau) from seed 1: all length-tau menu-words with
product N -- a designed fiber must CLOSE (every word over the
world's menus reaching N at age tau joins the posterior). Route
posterior proportional to the product of interior 1/Z (Boltzmann
numerators cancel at a fixed endpoint). Unnamed states carry a junk
menu {N+1}: any word using a junk move overshoots N, so closure can
fail only through designed-state coincidences. (A junk menu coprime
to its state always exists -- any prime > N -- so junk menus never
block a coprime world's closure either.)

THE SLATE (fixed before the run; the hand attack produced the
construction, the scaling family, and the theorem below, all frozen
here; the engine instances and cross-checks, it does not prove).

THE ROGUE WORLD (hand-derived). menu(1) = {2,32},
menu(2) = {2,4,8}, menu(16) = {2,16}, menu(32) = {2,4},
menu(128) = {2,8,32}, all other states junk. The dated fiber
(256, 3) closes at exactly two routes:
    route 1:  1 -(2)-> 2 -(8)-> 16 -(16)-> 256
    route 2:  1 -(32)-> 32 -(4)-> 128 -(2)-> 256
Hand check at beta = 1: interior products Z(2)*Z(16) = (7/8)(9/16)
= 63/128 = (3/4)(21/32) = Z(32)*Z(128) -- flat; at every beta by
the collision identity (x = 2^-beta):
(x+x^2+x^3)(x+x^4) = (x+x^2)(x+x^3+x^5) = x^2+x^3+x^4+x^5+x^6+x^7,
the cyclotomic regrouping of (1+x)(1+x+x^2)(1-x+x^2): the factor
1-x+x^2 has a negative coefficient, cannot stand alone in the
nonnegative semiring, and its two pairings give two distinct
semiring factorizations -- the classical source of non-unique
factorization in N[x], here wearing menu clothes.

THE SCALING FAMILY (hand-derived). Z_{cA} = c^-beta * Z_A, so
Z_A * Z_{cB} = Z_{cA} * Z_B for every menu pair A, B and scale
c >= 2: the semiring collides ubiquitously, not only through
cyclotomic regroupings. Realization has TEETH: the smallest scaling
instance {2},{4,8} vs {4},{2,4} admits NO closed age-3 realization
(all four cross-choices force a state coincidence with a menu
conflict) (REFUTED by the run, finding 4: the four cross-choices
silently assumed the family formula's menu order along each route;
the order swap realizes it at N = 32), while the instance
{2},{32,64} vs {8},{8,16} realizes:
menu(1) = {2,4}, menu(4) = {2}, menu(2) = {8}, menu(8) = {32,64},
menu(16) = {8,16}, routes (4,2,32) and (2,8,16) to 256.

THE QUARANTINE THEOREM (proved on paper before the run; the engine
cross-checks it by exhaustive scan, kill K2). In a COPRIME designed
world -- menus are functions of the state and every menu element is
coprime to its state -- two distinct routes with common seed, common
length, and common endpoint have interior-normalizer products that
differ at some beta; equality as functions of beta (any open
interval suffices: finite Dirichlet series are analytic in beta)
forces the routes to be identical. Corollary: every multi-route
dated fiber in a coprime world leaks at some temperature --
all-temperature amnesia requires a single route, at EVERY age. This
removes the exchange-closure hypothesis of the exchange-rigidity
theorem (explore_one_way.py: age-2 pairs in full generality,
exchange-closed route sets at any age) within the coprime class.
PROOF (induction on the length tau). tau = 1: the endpoint forces
the single moves equal. tau >= 2: flatness at all beta makes the
interior-normalizer products equal as Dirichlet polynomials; cancel
the common seed factor (the ring of Dirichlet series is a domain),
leaving equal products of the TAIL menus (states at ages
1..tau-1). SUPPORT: all coefficients are nonnegative, so no
cancellation occurs and each side's support is the set of products
of one element per menu; its prime set is the union of the menus'
primes -- so both routes' tail-menu prime sets are the SAME set P.
QUARANTINE: every tail state of route 1 is divisible by the first
move m1, and menu elements are coprime to their states, so every
tail-menu element of route 1 is coprime to m1: m1 is coprime to P.
Likewise the other first move m1', through its own route's tail and
the same P. VALUATION: the endpoint equation m1 * (tail moves) =
m1' * (tail moves') splits over primes -- inside P both first moves
have valuation zero; outside P both tails have valuation zero, so
the first moves' valuations agree prime by prime: m1 = m1'. The
first interior states then coincide, so their menus coincide (a
menu is a function of the state); cancel that factor and recurse on
the tails, which share the new seed. QED. Consequences: the depth
column's constant menu (the known beta-free amnesiac) is exactly a
NON-coprime privilege -- a taken move recurs, recycling primes; the
tuned amnesiac is flat at one beta only, untouched; D-MEM (its own
non-coprime bar) stays under the prior argument.

CENSUS + SCAN DESIGN. Collision census: menus = subsets of
{2..16} u {32} of size 1..3 (696 menus; 32 joins the universe so
the contract collision's menus sit inside census scope), all
unordered pairs (242,556 products, exact integer polynomial
arithmetic), grouped by product polynomial; a collision class is a
product with >= 2 menu pairs.
Classification per colliding pair of pairs: SCALING-type (some
pairing and scale c >= 2 with one menu the c-multiple of its
partner across the pairs), ONE-PRIME type (all four menus powers of
a single prime -- substitution instances of N[x]). Realization
scan, per colliding pair of pairs: both menu orders per route, all
cross-choices of second/third moves, seed moves from the reduced
endpoint ratio scaled by t <= 8; a hit must pass state-menu
consistency, fiber closure at exactly the two routes, exact
flatness on the beta grid {1,2,3}, the product-polynomial identity
(all beta at once), and multiset distinctness (a ROGUE
realization). The COPRIME arm re-runs the identical scan admitting
only worlds where every designed menu element is coprime to its
state.

PREDICTIONS (fixed before the run).
  P1 (the rogue world): the fiber at (256, 3) is exactly the two
     routes; posterior (1/2, 1/2) exact at beta = 1, 2, 3; the two
     interior-normalizer product polynomials are identical; the two
     multisets are distinct.
  P2 (perturbed control): menu(128) -> {2,8,16} keeps the fiber at
     two routes and breaks flatness at EVERY grid beta (the
     difference polynomial is x^5(x^2 - 1), strictly negative on
     0 < x < 1 -- it never ties).
  P3 (extra-route control): menu(64) = {4} grows the fiber to three
     routes (it gains (32, 4, 2)'s sibling (32, 2, 4)) and breaks
     flatness at beta = 1.
  P4 (census, MEASURED): the contract collision appears; >= 10
     scaling classes; >= 1 non-scaling class (the contract's);
     total counts, the smallest collision, and the
     neither-scaling-nor-one-prime count are printed and decide.
  P5 (teeth): the smallest scaling collision {2},{4,8} vs {4},{2,4}
     yields ZERO rogue realizations at scan scope; the contract
     collision yields >= 1 (the rogue world or a sibling); the
     second scaling instance yields >= 1.
  P6 (quarantine): ZERO coprime rogue realizations across ALL
     census collision pairs at scan scope; the identical scan
     without the coprime flag finds >= 1 (control C4).

KILLS (observables with live failure modes, weighed after the run).
K1: any of P1's four prints fails -- the realization claim dies
(the constraints forced coincidence after all). K2: the coprime
scan prints a realization -- the quarantine theorem is wrong (the
scan shares no step with the proof; control C4 shows the same
machinery finds realizations when the coprime demand is dropped).
CONTROLS (positive, run first). C1: the contract collision and both
scaling instances re-multiplied by the engine, coefficient-exact.
C2 = P2 (the flatness checker can fail). C3 = P3 (the closure
checker can fail). C4 = P6's unrestricted arm.

FINDINGS (tiers per the standard naming scale; run record below).

1. THE ROGUE WORLD EXISTS -- THE OBSTRUCTION SETTLES NEGATIVELY
   (construction; flatness at every beta proved by the polynomial
   identity, closure and exactness engine-verified). The designed
   world menu(1) = {2,32}, menu(2) = {2,4,8}, menu(16) = {2,16},
   menu(32) = {2,4}, menu(128) = {2,8,32} closes its dated fiber
   (256, 3) at exactly two routes, (2,8,16) and (32,4,2), with
   posterior (1/2, 1/2) at every beta and DISTINCT interior-
   normalizer multisets: robust flatness does NOT force the
   weight-side witness beyond the exchange class -- grade S with
   the witness absent is designable. The scan found a smaller
   sibling (N = 128, routes (32,2,2) / (2,2,32)) -- two orderings
   of ONE move multiset {2,2,32}, the permuted-route shape the
   exchange-rigidity theorem kills in many-window growth (a move
   dividing its state is barred under coprimality), alive here
   because the moves recycle the prime 2. Age 2 stays barred (Dirichlet uniqueness forces menu
   coincidence there); age 3 is where products of pairs collide.

2. THE QUARANTINE THEOREM (rule, proved; cross-checked by the
   proof-independent scan: 0 coprime rogue realizations across all
   4849 census collision pairs, while the same scan finds 4805
   free-design realizations). In a coprime designed world, no
   dated multi-route fiber is flat at every beta, at ANY age: the
   coprime demand quarantines each route's leading move from all
   tail-menu primes, the support of the normalizer product pins
   both routes to the same prime set, and valuations force the
   leading moves equal -- induction runs down the route. This
   removes the exchange-closure hypothesis of the exchange-
   rigidity theorem within the coprime class, closing its named
   open question there. THE DICHOTOMY: the obstruction's true
   boundary is the coprimality axis, not age and not exchange
   structure -- with recycled primes the rogue exists; without
   them, rigidity is total and the witness question is vacuous
   (flat means single-route). The depth column's beta-free amnesia
   is exactly the recycled-prime privilege.

3. THE SEMIRING COLLIDES GENERICALLY (observation, exhaustive at
   census scope). (Settled since: "far from factorial" does not
   follow from a collision count -- 2*6 = 3*4 holds in Z -- and the
   surviving reading of every number below is COLLISIONS and not
   factorizations. The semiring is non-factorial all the same, on
   the one-variable witness this record's own contract collision
   carries; whether that reaches past one variable is not measured
   here.)
   Menu Dirichlet polynomials collide ubiquitously:
   4849 colliding pairs across 4487 product classes at
   scope. The partition (the two classifications overlap; printed
   directly): the scaling family Z_A * Z_{cB} = Z_{cA} * Z_B
   supplies 4369 (111 of which are also one-prime); the 480
   non-scaling pairs split into 6 one-prime (substitution
   instances of the nonnegative-semiring non-uniqueness in one
   variable, the contract's cyclotomic regrouping among them) and
   474 involving at least two primes -- e.g. the transfer
   collision {2},{3,6} vs {3},{2,4} (equal products
   6^-beta + 12^-beta). Non-unique factorization is the generic
   state of the normalizer semiring, not a cyclotomic curiosity.

4. REALIZATION'S TEETH ARE EXACTLY THE SINGLETON DEGENERACY
   (observation at scan scope, one direction proved). The
   unrealized set coincides EXACTLY with the all-singleton
   collisions (44 = 44): four singleton menus force equal
   move-products, hence equal leading moves, hence a first-state
   menu conflict (proved, all orders); every census collision with
   at least one non-singleton menu realizes at t <= 8. Prediction
   P5's first clause is REFUTED: the hand attack had fixed the
   menu ORDER along each route (a transplant-species slip -- the
   scaling family's formula order was imported as if forced), and
   the scan's order swap realizes the smallest scaling collision
   at N = 32, routes (4,4,2) / (2,4,4). Realizability is generic:
   4805 of 4849.

5. THE DESERT LAW SHARPENED (the sequence's synthesis). Partition
   design never manufactures the exact ties working amnesia needs
   (explore_working_amnesiac.py: the tie desert); MENU design
   manufactures them freely -- generically, by finding 4 -- but
   only with recycled primes; under the coprimality demand no
   design does, at any age (finding 2). The door chart of exact
   amnesia is complete at scope: symmetry (constant menus, depth),
   tuning (one temperature), recycled-prime menu design (every
   temperature) -- and many-window (coprime) growth admits only the
   tuned door: no all-temperature amnesia there, at any age.

THE HEADLINE. The amnesia certificate's open obstruction settles
BOTH WAYS as a dichotomy on the coprimality axis. Designed worlds
that may recycle primes realize the abstract normalizer collision
as a closed two-route fiber -- flat at every temperature with
distinct menu multisets, so robust flatness does not force the
weight-side witness -- and such collisions are generic
(realization failing only at the singleton degeneracy; the
"far from factorial" gloss is retired, see finding 3's note). Coprime worlds sit on the other side: the
quarantine theorem removes the exchange-closure hypothesis and
makes all-temperature amnesia impossible with more than one route
at any age. What forgetting a route robustly truly costs is prime
recycling -- a world whose menus never reuse its own primes cannot
help writing its history into its weights.

HONEST LIMITS. (a) Census exhaustive only at scope: menus inside
{2..16} u {32}, size <= 3; scan seeds t <= 8; "everything
non-singleton realizes" is measured there, not a theorem. (b) The
scan builds minimal worlds whose fibers hold exactly the two
intended routes; larger flat fibers (extra routes joining at equal
weight) are unscanned. (c) Numeric flatness runs on the beta grid
{1,2,3}; every all-beta claim rides the product-polynomial
identity (exact), never the grid. (d) The quarantine theorem needs
menus that are functions of the state (Markov demands) and dated
fibers (common length); D-MEM's non-coprime demand stays under its
own prior bar (explore_one_way.py), outside this theorem.

RUN RECORD (this file, python explore_rogue_world.py, ~10 s).
Run 1: exit 1, 28/30 -- two slate slips, no engine defect. (i) The
census universe {2..16} could not contain the contract collision's
own menu {2,8,32}: P4's membership check failed by scope; universe
extended to {2..16} u {32} (696 menus, 242,556 pairs). (ii) P5's
first clause (smallest scaling collision unrealizable) was
REFUTED: the scan found the order-swapped realization the hand
attack had missed; the assert was converted to a print plus an
independent validity re-check of the found world. Run 2: exit 0,
30/30. Run 3: added the measured-only all-singleton probe
(unrealized == all-singleton: True, 44 = 44); exit 0, 30/30.
Run 4 (the audit round): the scaling and one-prime classifications
OVERLAP (findings first read them as a partition); a direct
partition print was added (measured only) -- scaling 4369 of which
111 one-prime; non-scaling 480 = 6 one-prime + 474 multi-prime --
and finding 3 restated from it; runtime remeasured ~10 s (first
recorded as an unmeasured ~40 s); exit 0, 30/30.
Post-run edits: this findings block, the census-design universe
sentence, the two S6 blocks named above, the run-4 partition
print, and the refutation parenthetical in the scaling-family
slate paragraph; engine otherwise untouched.
"""

import sys
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from math import gcd

CHECKS = []


def check(name, ok):
    CHECKS.append((name, bool(ok)))
    print(("PASS  " if ok else "FAIL  ") + name)


# ---------------------------------------------------------------- polynomials
# A Dirichlet polynomial is a dict {m: coeff} standing for
# sum coeff * m^-beta over integers m >= 1.

def zpoly(menu):
    return {m: 1 for m in menu}


def pmul(P, Q):
    R = {}
    for a, ca in P.items():
        for b, cb in Q.items():
            R[a * b] = R.get(a * b, 0) + ca * cb
    return R


def pprod(polys):
    R = {1: 1}
    for P in polys:
        R = pmul(R, P)
    return R


def pkey(P):
    return tuple(sorted(P.items()))


def peval(P, beta):
    return sum(Fraction(c, m ** beta) for m, c in P.items())


# ---------------------------------------------------------------- worlds
def fiber(menus, N, tau, junk):
    """All length-tau words from seed 1 with product N; unnamed states
    carry the junk menu (junk = N+1 in every call here, so a junk
    move overshoots N from any state)."""
    out = []

    def rec(state, word):
        if len(word) == tau:
            if state == N:
                out.append(tuple(word))
            return
        for m in menus.get(state, (junk,)):
            if state * m <= N:
                rec(state * m, word + [m])

    rec(1, [])
    return out


def route_menus(menus, route, junk):
    """The interior menus (states at ages 0..tau-1) along a route."""
    st, res = 1, []
    for m in route:
        res.append(tuple(sorted(menus.get(st, (junk,)))))
        st *= m
    return res


def posterior(menus, routes, beta, junk):
    ws = []
    for r in routes:
        st, w = 1, Fraction(1)
        for m in r:
            menu = menus.get(st, (junk,))
            Z = sum(Fraction(1, mm ** beta) for mm in menu)
            w *= Fraction(1, m ** beta) / Z
            st *= m
        ws.append(w)
    tot = sum(ws)
    return [w / tot for w in ws]


def flat_on_grid(menus, routes, junk, betas=(1, 2, 3)):
    n = len(routes)
    return all(posterior(menus, routes, b, junk) == [Fraction(1, n)] * n
               for b in betas)


# ---------------------------------------------------------------- factoring
def prime_factors(n):
    fs, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            fs.add(d)
            n //= d
        d += 1
    if n > 1:
        fs.add(n)
    return fs


# ================================================================ S0 machinery
print("== S0 machinery ==")
check("S0 pmul singleton", pmul(zpoly((2,)), zpoly((3,))) == {6: 1})
check("S0 pmul square", pmul(zpoly((2, 4)), zpoly((2, 4)))
      == {4: 1, 8: 2, 16: 1})

# ================================================================ S1 controls
print("\n== S1 control C1: the abstract collisions, engine-multiplied ==")
CONTRACT = (((2, 4, 8), (2, 16)), ((2, 4), (2, 8, 32)))
SMALL_SCALING = (((2,), (4, 8)), ((4,), (2, 4)))
SECOND_SCALING = (((2,), (32, 64)), ((8,), (8, 16)))

for name, (p1, p2) in (("contract", CONTRACT),
                       ("smallest-scaling", SMALL_SCALING),
                       ("second-scaling", SECOND_SCALING)):
    L = pmul(zpoly(p1[0]), zpoly(p1[1]))
    R = pmul(zpoly(p2[0]), zpoly(p2[1]))
    print(f"  {name}: {p1[0]} x {p1[1]}  vs  {p2[0]} x {p2[1]}"
          f"  ->  {sorted(L.items())}")
    check(f"S1 {name} products equal", L == R)
check("S1 contract support",
      pkey(pmul(zpoly((2, 4, 8)), zpoly((2, 16))))
      == tuple((m, 1) for m in (4, 8, 16, 32, 64, 128)))

# ================================================================ S2 the rogue
print("\n== S2 the rogue world ==")
ROGUE = {1: (2, 32), 2: (2, 4, 8), 16: (2, 16), 32: (2, 4),
         128: (2, 8, 32)}
N_R, TAU_R, JUNK_R = 256, 3, 257
ROUTE1, ROUTE2 = (2, 8, 16), (32, 4, 2)

fib = fiber(ROGUE, N_R, TAU_R, JUNK_R)
print(f"  fiber(256, 3) = {sorted(fib)}")
check("S2 fiber exactly the two routes",
      sorted(fib) == sorted((ROUTE1, ROUTE2)))

for b in (1, 2, 3):
    post = posterior(ROGUE, [ROUTE1, ROUTE2], b, JUNK_R)
    print(f"  beta = {b}: posterior = {post[0]}, {post[1]}")
    check(f"S2 flat at beta={b}",
          post == [Fraction(1, 2), Fraction(1, 2)])

ms1 = route_menus(ROGUE, ROUTE1, JUNK_R)
ms2 = route_menus(ROGUE, ROUTE2, JUNK_R)
P1poly = pprod([zpoly(m) for m in ms1])
P2poly = pprod([zpoly(m) for m in ms2])
print(f"  route 1 interior menus: {ms1}")
print(f"  route 2 interior menus: {ms2}")
print(f"  common product polynomial: {sorted(P1poly.items())}")
check("S2 product polynomials identical (all beta)", P1poly == P2poly)
check("S2 multisets distinct (witness absent)",
      sorted(ms1) != sorted(ms2))

# ================================================================ S3 controls
print("\n== S3 controls C2 (perturbed) and C3 (extra route) ==")
PERT = dict(ROGUE)
PERT[128] = (2, 8, 16)
fibp = fiber(PERT, N_R, TAU_R, JUNK_R)
check("S3 C2 perturbed fiber still two routes",
      sorted(fibp) == sorted((ROUTE1, ROUTE2)))
for b in (1, 2, 3):
    post = posterior(PERT, [ROUTE1, ROUTE2], b, JUNK_R)
    check(f"S3 C2 perturbed NOT flat at beta={b}",
          post != [Fraction(1, 2), Fraction(1, 2)])

EXTRA = dict(ROGUE)
EXTRA[64] = (4,)
fibe = fiber(EXTRA, N_R, TAU_R, JUNK_R)
print(f"  extra-route fiber = {sorted(fibe)}")
check("S3 C3 extra-route fiber has three routes",
      len(fibe) == 3 and (32, 2, 4) in fibe)
check("S3 C3 extra-route NOT flat at beta=1",
      posterior(EXTRA, sorted(fibe), 1, JUNK_R)
      != [Fraction(1, 3)] * 3)

# ================================================================ S4 second
print("\n== S4 the second rogue world (scaling instance) ==")
ROGUE2 = {1: (2, 4), 4: (2,), 2: (8,), 8: (32, 64), 16: (8, 16)}
R2A, R2B = (4, 2, 32), (2, 8, 16)
fib2 = fiber(ROGUE2, 256, 3, 257)
print(f"  fiber(256, 3) = {sorted(fib2)}")
check("S4 fiber exactly the two routes",
      sorted(fib2) == sorted((R2A, R2B)))
check("S4 flat on grid", flat_on_grid(ROGUE2, [R2A, R2B], 257))
ms1 = route_menus(ROGUE2, R2A, 257)
ms2 = route_menus(ROGUE2, R2B, 257)
check("S4 product polynomials identical (all beta)",
      pprod([zpoly(m) for m in ms1]) == pprod([zpoly(m) for m in ms2]))
check("S4 multisets distinct (witness absent)",
      sorted(ms1) != sorted(ms2))

# ================================================================ S5 census
print("\n== S5 the collision census (menus in {2..16} u {32},"
      " size <= 3) ==")
UNIVERSE = tuple(range(2, 17)) + (32,)
menus_all = []
for size in (1, 2, 3):
    menus_all += list(combinations(UNIVERSE, size))
print(f"  menus: {len(menus_all)}")

products = {}
for A, B in combinations_with_replacement(menus_all, 2):
    key = pkey(pmul(zpoly(A), zpoly(B)))
    products.setdefault(key, []).append((A, B))

classes = {k: v for k, v in products.items() if len(v) >= 2}
print(f"  menu pairs: {sum(len(v) for v in products.values())}")
print(f"  collision classes (>= 2 pairs sharing one product): "
      f"{len(classes)}")


def scale_of(A, C):
    """c >= 2 with C == c*A elementwise, else None."""
    if len(A) != len(C) or C[0] % A[0]:
        return None
    c = C[0] // A[0]
    if c < 2:
        return None
    return c if all(c * a == cc for a, cc in zip(A, C)) else None


def is_scaling(pp1, pp2):
    (A, B), (C, D) = pp1, pp2
    for X1, Y1 in ((A, B), (B, A)):
        for X2, Y2 in ((C, D), (D, C)):
            c = scale_of(X1, X2)
            if c is not None and scale_of(Y2, Y1) == c:
                return True
    return False


def one_prime(pp1, pp2):
    ps = set()
    for menu in pp1 + pp2:
        for m in menu:
            ps |= prime_factors(m)
    return len(ps) == 1


colliding = []          # (pair, pair) with distinct multisets
for key, pairs in classes.items():
    for pp1, pp2 in combinations(pairs, 2):
        colliding.append((key, pp1, pp2))

n_scaling = sum(1 for _, a, b in colliding if is_scaling(a, b))
n_oneprime = sum(1 for _, a, b in colliding if one_prime(a, b))
n_neither = sum(1 for _, a, b in colliding
                if not is_scaling(a, b) and not one_prime(a, b))
scaling_classes = {k for k, a, b in colliding if is_scaling(a, b)}
nonscaling_classes = {k for k, a, b in colliding if not is_scaling(a, b)}
n_s_and_op = sum(1 for _, a, b in colliding
                 if is_scaling(a, b) and one_prime(a, b))
print(f"  colliding pair-of-pairs: {len(colliding)}"
      f"  (scaling-type {n_scaling}, one-prime {n_oneprime},"
      f" neither-scaling-nor-one-prime {n_neither})")
print(f"  partition: scaling {n_scaling} (of which one-prime"
      f" {n_s_and_op}); non-scaling {len(colliding) - n_scaling}"
      f" = one-prime {n_oneprime - n_s_and_op}"
      f" + multi-prime {n_neither}")
print(f"  classes with a scaling collision: {len(scaling_classes)};"
      f" with a non-scaling collision: {len(nonscaling_classes)}")

smallest = min(colliding, key=lambda t: (max(m for m, _ in t[0]), t[0]))
print(f"  smallest collision (by largest product-support entry): "
      f"{smallest[1]} vs {smallest[2]}"
      f"  product {[m for m, _ in smallest[0]]}")

# membership test: both contract pairs sit in one census class
ckey = pkey(pmul(zpoly(CONTRACT[0][0]), zpoly(CONTRACT[0][1])))
in_class = classes.get(ckey, [])
contract_found = (tuple(sorted(CONTRACT[0])) in
                  [tuple(sorted(p)) for p in in_class]
                  and tuple(sorted(CONTRACT[1])) in
                  [tuple(sorted(p)) for p in in_class])
check("S5 contract collision present in the census", contract_found)
check("S5 >= 10 scaling classes", len(scaling_classes) >= 10)
check("S5 >= 1 non-scaling class", len(nonscaling_classes) >= 1)

# ================================================================ S6 the scan
print("\n== S6 realization scan (teeth + the quarantine cross-check) ==")


def try_world(m1, M1, M2, m1p, M3, M4, m2, m3, m2p, m3p, coprime):
    """Build the minimal world for the two intended routes; return the
    world record if it is a closed, flat, witness-absent (rogue)
    realization, else None."""
    a, b = m1, m1 * m2
    c, d = m1p, m1p * m2p
    menu1 = tuple(sorted(set((m1, m1p))))
    assign = {}
    for st, mn in ((1, menu1), (a, tuple(sorted(M1))),
                   (b, tuple(sorted(M2))), (c, tuple(sorted(M3))),
                   (d, tuple(sorted(M4)))):
        if st in assign and assign[st] != mn:
            return None
        assign[st] = mn
    if coprime:
        for st, mn in assign.items():
            if any(gcd(m, st) != 1 for m in mn):
                return None
    N = m1 * m2 * m3
    r1, r2 = (m1, m2, m3), (m1p, m2p, m3p)
    fib = fiber(assign, N, 3, N + 1)
    if sorted(fib) != sorted({r1, r2}) or len({r1, r2}) != 2:
        return None
    if not flat_on_grid(assign, [r1, r2], N + 1):
        return None
    q1 = route_menus(assign, r1, N + 1)
    q2 = route_menus(assign, r2, N + 1)
    if pprod([zpoly(m) for m in q1]) != pprod([zpoly(m) for m in q2]):
        return None
    if sorted(q1) == sorted(q2):
        return None
    return (assign, N, r1, r2)


def scan(pp1, pp2, coprime, t_max=8, first_only=True):
    (Aa, Bb), (Cc, Dd) = pp1, pp2
    found = []
    for M1, M2 in ((Aa, Bb), (Bb, Aa)):
        for M3, M4 in ((Cc, Dd), (Dd, Cc)):
            for m2 in M1:
                for m3 in M2:
                    for m2p in M3:
                        for m3p in M4:
                            num, den = m2p * m3p, m2 * m3
                            g = gcd(num, den)
                            u, v = num // g, den // g
                            for t in range(1, t_max + 1):
                                m1, m1p = u * t, v * t
                                if m1 < 2 or m1p < 2:
                                    continue
                                w = try_world(m1, M1, M2, m1p, M3, M4,
                                              m2, m3, m2p, m3p, coprime)
                                if w:
                                    found.append(w)
                                    if first_only:
                                        return found
    return found


# -- teeth (P5; the first clause of P5 predicted the smallest scaling
# collision unrealizable -- the print decides, and a found world is
# re-verified independently)
hits_small = scan(*SMALL_SCALING, coprime=False)
if hits_small:
    w, N, r1, r2 = hits_small[0]
    print(f"  smallest-scaling realization found: N = {N},"
          f" routes {r1} / {r2}, menus {w}")
    check("S6 smallest-scaling realization valid",
          sorted(fiber(w, N, 3, N + 1)) == sorted((r1, r2))
          and flat_on_grid(w, [r1, r2], N + 1)
          and sorted(route_menus(w, r1, N + 1))
          != sorted(route_menus(w, r2, N + 1)))
else:
    print("  smallest-scaling collision: no realization at scan scope")
hits_contract = scan(*CONTRACT, coprime=False)
if hits_contract:
    w, N, r1, r2 = hits_contract[0]
    print(f"  contract realization found: N = {N}, routes {r1} / {r2},"
          f" menus {w}")
check("S6 teeth: contract collision realizes", len(hits_contract) >= 1)
hits_second = scan(*SECOND_SCALING, coprime=False)
check("S6 teeth: second scaling instance realizes",
      len(hits_second) >= 1)

# -- the quarantine cross-check (K2) + the free-design control (C4)
coprime_hits = 0
free_hits = 0
unrealized = []
for key, pp1, pp2 in colliding:
    if scan(pp1, pp2, coprime=True):
        coprime_hits += 1
        print(f"  COPRIME ROGUE (kill K2 FIRES): {pp1} vs {pp2}")
    if scan(pp1, pp2, coprime=False):
        free_hits += 1
    else:
        unrealized.append((pp1, pp2))
print(f"  census pairs scanned: {len(colliding)};"
      f" free-design rogue realizations: {free_hits};"
      f" coprime rogue realizations: {coprime_hits}")
print(f"  unrealized at scan scope: {len(unrealized)}; first five: "
      f"{unrealized[:5]}")
# measured only (post-run probe): all-singleton collisions are provably
# unrealizable (singleton interiors force equal move-products, hence
# equal seed moves, hence a first-state menu conflict) -- does the
# unrealized set coincide with the all-singleton set exactly?
all_singleton = {(pp1, pp2) for _, pp1, pp2 in colliding
                 if all(len(m) == 1 for m in pp1 + pp2)}
print(f"  all-singleton colliding pairs: {len(all_singleton)};"
      f" unrealized == all-singleton: "
      f"{set(unrealized) == all_singleton}")
check("S6 K2 missed: zero coprime rogue realizations",
      coprime_hits == 0)
check("S6 C4: free-design scan finds realizations", free_hits >= 1)

# ================================================================ verdict
print()
bad = [n for n, ok in CHECKS if not ok]
print(f"{len(CHECKS) - len(bad)}/{len(CHECKS)} checks green"
      + ("" if not bad else "  FAILURES: " + ", ".join(bad)))
sys.exit(0 if not bad else 1)
