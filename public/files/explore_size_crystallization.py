"""
explore_size_crystallization.py — the archimedean crystallization
(sibling of explore_growth_laws.py and explore_growth_capability.py).

THE QUESTION. Prior work closed on one honest limit: every growth law
prices its candidates by SIZE ("least m") — the deleted archimedean
place returns as the cost axis of growth. This script removes size
from the cost too, and asks both directions of the traffic:
(A) GROWTH WITHOUT SIZE — which of explore_growth_laws.py's blueprint outputs (fields
    for free, squarefree-ness, healing, the primorial route) can be
    purchased with pure window data, and which are archimedean-authored?
(B) SIZE FROM WINDOWS — a window budget Q reads the horizon [1, X]
    through residues; when does the archimedean order CRYSTALLIZE out
    of window data? The hiding lemma (explore_size_transform.py)
    owns the rigid divisor-budget corner — seated here, not
    re-walked.

VOCABULARY (the window world). Candidate moves are rings Z/m; the only
canonical structure between them is unital ring homomorphisms, and
Hom(Z/a, Z/b) is nonempty iff b | a (S1) — the window world's canonical
order on moves is DIVISIBILITY, and distinct primes are an ANTICHAIN.
A window-visible cost = any function of the iso class of Z/m (of m's
factorization shape); comparing cost VALUES is ordinal bookkeeping.
What is removed is the archimedean order on m itself as a primitive.

FINDINGS (naming tiers below; run record follows; all sections assert).

1. THE HOM-ORDER LEMMA (rule, textbook content; verified exhaustively
   a, b <= 60 via the forced form). A unital ring hom Z/a -> Z/b is
   forced to x mod b (1 generates additively), which is well-defined
   iff b | a. So hom-existence IS reverse divisibility, and distinct
   prime fields admit no map either way: the primes are an antichain.
   No CANONICAL window order exists on them (a window-visible cost
   can order them, but any such order is an arbitrary choice);
   "least prime" is external data.

2. THE DEMAND PROPOSES, THE PLACE DISPOSES (rule; specimens verified).
   Strip the cost from D-IND and the move set at N is ALL m >= 2 with
   gcd(m, N) = 1 — composites and prime powers included. Legal D-IND
   trajectories include: seed 2 -> pick 9 (a depth-2 NON-FIELD window;
   Z/18 not squarefree — fields-for-free dies); seed 3 -> 5, 7, 11,
   ..., 37 with 2 never entering (healing dies: the all-primes
   destination is not demand-forced). EVERY blueprint output —
   fields, squarefree-ness, healing, the primorial route — is
   authored by the SELECTION axis, not by the independence demand.

3. FIELDS ARE WINDOW-PURCHASABLE (rule, proved; verified across
   seeds x tie-breaks). If the cost is strictly monotone under proper
   divisibility (d | m proper => c(d) < c(m); e.g. c = Omega, the
   prime-factor count with multiplicity — an iso invariant), every
   greedy pick is a divisibility-MINIMAL admissible move, i.e. a
   PRIME: a composite coprime to N has a prime divisor, also coprime,
   strictly cheaper. Fields for free + squarefree-ness restored with
   ZERO archimedean input, under EVERY tie-breaking (verified: 3
   tie-break policies x 6 seeds x 20 steps, all picks prime).

4. THE PROPERNESS CRITERION (criterion, proved; both directions
   verified in range). Under a div-strict-monotone cost, a prime p is
   guaranteed to enter the window set under EVERY tie-breaking iff its
   cost sublevel set {q prime : c(q) <= c(p)} is FINITE. Proof: while
   p is admissible every greedy pick has cost <= c(p), so picks come
   from the sublevel set; each pick consumes one member permanently
   (picked primes divide N forever); finite => p is eventually the
   unique minimum. Conversely, an infinite sublevel set feeds an
   adversarial tie-break that picks others forever (specimen: c =
   Omega puts ALL primes in one fiber — the odd-preferring tie-break
   starves 2 indefinitely; verified 30 steps). COROLLARY: the
   destination (window set -> all primes, the healing property above) is
   guaranteed for every tie-break iff the cost is PROPER (every
   prime's sublevel set finite). The archimedean order enters "least m" ONLY
   through properness plus one choice of linear extension — nothing
   else about size is load-bearing for the destination.

5. THE ROUTE RESIDUE (rule; 3 scrambled costs verified). Proper
   div-monotone costs realize ANY enumeration of the primes as the
   route (assign scrambled ranks; verified: 3 scrambles give 3
   distinct routes, each prime entering exactly at its rank bound,
   all with the SAME destination). So the window world purchases the
   DESTINATION and the field/squarefree properties; the ROUTE — entry
   order, hence rung identity, the Linnik ordering, the transparency
   schedule, the plateaus, everything that makes the tower a SEQUENCE
   — is the archimedean place's sole irreducible contribution to free
   growth. The tower-as-limit is window-authored; the tower-as-
   sequence is archimedean-authored.

6. THE PRATT ORDER ROUTES WITHOUT SIZE (rule in range; extension
   count measured). One natural arrival constraint IS window-
   visible: demand the new channel's unit-group order have all its
   prime content resident (every prime factor of q - 1 already a
   window — divisibility of orders, hom-visible data). This constraint
   is exactly the PRATT-CERTIFICATE partial order (parents of p = the
   prime factors of p - 1; the primality-certificate DAG). It forces
   2 first; after {2} the available primes are exactly the Fermat
   primes (3, 5, 17 in range: p - 1 a 2-power). Sizeless shift-closed
   routes = linear extensions of the Pratt order; the primorial route
   is one of them (parents < child, verified first 300 primes — the
   increasing order extends Pratt). Extension counts (downset DP,
   first n primes of the 20-prime poset): n=5: 6, n=10: 6,048, n=15:
   108,662,400, n=20: 8,506,240,142,400 — against n! = 120, 3.6e6,
   1.3e12, 2.4e18. The window order ROUTES ONLY WEAKLY: absolute
   freedom explodes (8.5e12 routes at n=20) while the fraction of all
   enumerations collapses (ratio 5.0e-2 -> 3.5e-6). In bits: the
   first 20 primes carry log2(20!) ~ 61 bits of route; the Pratt
   order supplies ~18 of them, the archimedean choice the remaining
   ~43 — and what routing the windows DO supply is precisely
   primality-certificate order. NOT claimed maximal: stronger
   window-visible arrival demands exist (transparency-arrival,
   q - 1 | lambda(N), is one — and it HALTS, the mortality fate);
   whether Pratt is the strongest such demand still compatible with
   the all-primes destination is open. Lineage: the Pratt tree itself
   is charted elsewhere (the super-logarithm — its iterated
   index-ring construction descends the tree; Ford-Konyagin-Luca
   contact there); new here is its role as a window-visible route
   order of growth.

7. THE CRYSTALLIZATION CURVE (rule, proved; verified exhaustively
   X <= 240, all Q). Read the horizon [1, X] through a window budget
   Q (know n mod Q, n uniform). An element is DETERMINED iff its
   fiber has one lift: the determined count is exactly max(0, 2Q - X)
   — the order parameter max(0, 2*rho - 1), rho = Q/X, is FLAT ZERO
   below HALF coverage, rises linearly, completes at rho = 1. Size
   certainty switches on at exactly half coverage. Growth reading: a
   tower watching horizon X crystallizes nothing until its modulus
   passes X/2, and everything at X (specimen: N = 30 vs X = 50
   determines exactly the 10 elements 21..30).

8. THE HALF-COVERAGE LAW (rule, proved; verified exhaustively — the
   frozen ragged-leak prediction REFUTED, see adjudication). Every
   fiber touches both ends of the horizon: its least lift is <= Q and
   its greatest is > X - Q. Two fiber spans can be disjoint only when
   Q >= (X + 2)/2. So at or below half coverage NO archimedean fact
   about [1, X] is certain — no determined points, no determined
   pairs — for ANY budget shape, ragged or rigid. Onsets: points at
   2Q - X >= 1, pairs at 2Q - X >= 2 (at 2Q - X = 1 the single
   determined middle element sits strictly inside every other fiber's
   span; from 2, determined singles pair up). Verified: pair
   determinacy iff 2Q - X >= 2 at every budget X <= 120; zero
   singles and pairs at every proper-divisor budget X <= 240.
   Kinship: the proof is the linear-order sibling of the
   orientation-hiding argument (every ladder contains an
   element <= M and one >= (c-1)M); same extreme-pair mechanism, there
   cyclic, here [1, X].

9. THE SUB-RING CAP (corollary of 8; the hiding lemma seated). A
   proper divisor budget Q | X, Q < X has Q <= X/2: sub-ring windows
   are exactly the budgets that can NEVER cross the onset. The hiding
   lemma's totality (proper windows leave size uniform,
   orientation hiding total) is explained by the CAP, not by any
   rigidity of divisor fibers — certainty-blindness below half
   coverage is universal (finding 8); divisor structure just pins the
   coverage there permanently.

10. THE STATISTICAL SHADOW (rule, proved closed form; verified
    exactly at all rigid budgets X <= 120). In the rigid phase the
    optimal comparison guess (order the residues) has accuracy
    EXACTLY (X + Q - 2) / (2(X - 1)) = 1/2 + (Q-1)/(2(X-1)) ~
    1/2 + rho/2: the archimedean ORDER leaks statistically at every
    coverage — linearly from zero — while certainty stays exactly
    zero below the onset. No contradiction with the hiding lemma:
    each element's fiber stays perfectly uniform (points are hidden);
    what leaks is the residue ORDER of pairs. Certainty crystallizes
    at half coverage; statistics leak from the first window.

THE SYNTHESIS (this script's close). Remove the archimedean place
from growth's cost and the blueprint splits cleanly in two: the
window world purchases FIELDS, SQUAREFREE-NESS, and (given any
proper div-monotone cost) the DESTINATION — but the primes are a
hom-antichain, so the ROUTE is unpurchasable: every sizeless law
leaves a fan of routes (the one natural window-visible arrival
demand measured constrains the fan to the Pratt order's linear
extensions), and the archimedean order is the external choice that
collapses the fan into THE tower. Conversely, size does crystallize back out of window data
— but no certainty of any kind exists at or below half coverage (the
half-coverage law), points onset first and pairs one step later,
completion only at coverage one, while the statistical shadow of
ORDER leaks from the first window at rate rho/2. The sub-rings the
tower itself offers are capped at half coverage — they never cross
the onset, which is the hiding lemma. The bootstrap remark ties the
halves: from rung
3 on, the next prime is far below the modulus (Bertrand), so growth's
own comparisons are ring-internal and DETERMINED — priced by the size
wall but available. The route residue is therefore not an information
gap at scale; it is a CRITERION gap: nothing in the window world
makes "ascending" canonical. The tower is co-authored: windows write
the destination, the deleted place writes the itinerary.

HONEST SCOPE. Threshold-greedy laws over ring extensions of Z/N, as
in the sibling scripts; costs = functions of the iso class with well-ordered
values; the Pratt constraint is ONE natural window-visible arrival
demand, not the unique one; crystallization is stated for uniform
priors on [1, X] (the hiding lemma's setting), exhaustive in range,
with the closed forms proved. Stochastic laws were subsequently
charted in explore_thermal_growth.py — it
makes this script's authorship split physical: the
selection-authored residue is exactly what temperature melts;
additive moves and non-cyclic ambients remain open questions.

RUN RECORD (python explore_size_crystallization.py, ~60 s, <200 MB):
  S1 hom-order: 3,481 (a,b) pairs, existence == reverse divisibility;
     272 distinct-prime pairs, no hom either way
  S2 demand-proposes: composite moves present at 6 seeds; the seed-2
     pick-9 specimen (Z/18: not squarefree, 3 a zero divisor in Z/9);
     the seed-3 ten-step 2-free route legal at every step
  S3 fields-for-free without size: 3 tie-breaks x 6 seeds x 20 steps,
     360 picks, all prime
  S4 properness: Omega-cost odd-tie-break starves 2 for 30 steps (2
     admissible throughout); 3 scrambled proper costs x 46 primes:
     every prime enters at exactly its rank bound; 3 distinct routes,
     one destination
  S5 Pratt: parents < p for the first 300 primes; 2 the only
     parentless prime (forced first); after {2} exactly
     {3, 5, 17} available (the Fermat primes in range); downset DP on
     the 20-prime poset: extensions 6 / 6,048 / 108,662,400 /
     8,506,240,142,400 at n = 5/10/15/20; ratio to n! collapsing
     5.0e-2 -> 3.5e-6
  S6 crystallization: determined singles == max(0, 2Q - X) at 28,919
     budgets (X <= 240, all Q); 0 singles + 0 pairs at all 884
     proper-divisor budgets X <= 240; pair determinacy iff
     2Q - X >= 2 at 7,259 budgets (X <= 120, all Q); rigid accuracy
     == (X + Q - 2)/(2(X - 1)) exactly at all 597 rigid budgets
     X <= 120; the N = 30, X = 50 growth specimen (10 elements,
     21..30)
  TOTAL 43,690 checks, exit 0.

ADJUDICATION vs the predictions fixed before the run.
PR1, PR2, PR3, PR4 landed as stated. PR6 landed on the singles curve,
the divisor blindness, and the exact rigid accuracy law (derivation
A, frozen pre-code) — but its RAGGED-LEAK clause ("determined pairs
exist strictly below half coverage, specimen X = 2Q + 2") is
REFUTED: the hand specimen ignored that every fiber's least lift is
<= Q and greatest is > X - Q, so spans always overlap at or below
half coverage. The failed assert forced the stronger true law
(finding 8: no certainty of ANY kind below the onset). Same species
as explore_growth_capability.py's PR2: a hand-derived specimen blind to a structural fact,
caught only because the prediction was fixed before the run and asserted. PR5
landed on both qualitative calls (extensions grow superexponentially,
ratio to n! collapses); its first docstring draft carried typed
placeholder counts that the run replaced (the unfrozen-specimen
reflex again, caught before the final draft).
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import random
from math import gcd, factorial

CHECKS = 0


def check(cond, msg=""):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def factorize(n):
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


def omega_mult(n):
    return sum(factorize(n).values())


def is_prime(n):
    return n >= 2 and omega_mult(n) == 1


def primes_upto(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i:: i] = bytearray(len(sieve[i * i:: i]))
    return [i for i in range(2, n + 1) if sieve[i]]


# ────────────────────────────────────────────────────────────────────
section("S1. THE HOM-ORDER LEMMA: unital homs Z/a -> Z/b exist iff "
        "b | a")
# ────────────────────────────────────────────────────────────────────
# A unital hom f is additively determined: f(x) = x * f(1) = x mod b.
# It is well-defined on Z/a iff a == 0 (mod b) (test the pair 0 ~ a).
# When b | a, x mod b is a ring hom (verified on all pairs). So
# existence == reverse divisibility; distinct primes are an antichain.
for a in range(2, 61):
    for b in range(2, 61):
        well_defined = (a % b == 0)
        if well_defined:
            ok = all(((x + y) % a % b == ((x % b) + (y % b)) % b) and
                     ((x * y) % a % b == ((x % b) * (y % b)) % b)
                     for x in range(a) for y in range(a))
            check(ok, f"reduction not a hom at ({a},{b})")
        else:
            # the forced form x -> x mod b identifies 0 with a yet
            # sends them to different images: no unital hom exists
            check(0 % b != a % b, f"({a},{b})")
antichain_pairs = 0
P60 = primes_upto(60)
for p in P60:
    for q in P60:
        if p != q:
            check(p % q != 0, "prime antichain")
            antichain_pairs += 1
print(f"3481 (a,b) pairs: existence == reverse divisibility; "
      f"{antichain_pairs} distinct-prime pairs: no hom either way "
      f"(antichain)")

# ────────────────────────────────────────────────────────────────────
section("S2. THE DEMAND PROPOSES, THE PLACE DISPOSES: sizeless D-IND")
# ────────────────────────────────────────────────────────────────────
# D-IND at N admits every m >= 2 coprime to N. Without the size
# tiebreak the move set contains composites and prime powers.
CAP = 200
for seed in (1, 2, 3, 6, 30, 210):
    moves = [m for m in range(2, CAP + 1) if gcd(m, seed) == 1]
    comps = [m for m in moves if not is_prime(m)]
    check(len(comps) > 0, f"no composite moves at seed {seed}")
check(9 in [m for m in range(2, 20) if gcd(m, 2) == 1], "9 from seed 2")

# Specimen A: seed 2 picks 9 -> Z/18. Legal (coprime => splits), yet
# the new window Z/9 is not a field and 18 is not squarefree.
check(gcd(9, 2) == 1, "9 admissible at 2")
check(any(18 % (p * p) == 0 for p in (2, 3)), "18 not squarefree")
check((3 * 3) % 9 == 0, "3 is a zero divisor in Z/9 (non-field window)")

# Specimen B: seed 3, ten steps, 2 never enters — healing is not
# demand-forced.
N = 3
route = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
for m in route:
    check(gcd(m, N) == 1, f"illegal move {m} at {N}")   # D-IND holds
    N *= m
check(N % 2 == 1, "2 never entered in 10 legal D-IND steps")
print("composite/prime-power moves legal at all 6 seeds; seed-2 "
      "pick-9 kills squarefree+fields; seed-3 route starves 2 "
      "(10 steps) — every output is selection-authored")

# ────────────────────────────────────────────────────────────────────
section("S3. FIELDS ARE WINDOW-PURCHASABLE: div-monotone costs pick "
        "primes")
# ────────────────────────────────────────────────────────────────────
# Cost c = Omega (prime factors with multiplicity): an iso invariant,
# strictly monotone under proper divisibility. Every greedy pick is a
# divisibility-minimal admissible move = a prime, under EVERY
# tie-breaking (proof in docstring finding 3).
SCAN = 2000
rng = random.Random(145)


def greedy_run(seed, steps, tiebreak):
    N = seed
    picks = []
    for _ in range(steps):
        adm = [m for m in range(2, SCAN + 1) if gcd(m, N) == 1]
        lvl = min(omega_mult(m) for m in adm)
        tier = [m for m in adm if omega_mult(m) == lvl]
        m = tiebreak(tier)
        picks.append(m)
        N *= m
    return picks


tiebreaks = [("smallest", min), ("largest", max),
             ("random", lambda t: rng.choice(t))]
total_picks = 0
for name, tb in tiebreaks:
    for seed in (1, 2, 6, 30, 49, 100):
        for m in greedy_run(seed, 20, tb):
            check(is_prime(m), f"non-prime pick {m} ({name}, {seed})")
            total_picks += 1
print(f"{total_picks} picks across 3 tie-breaks x 6 seeds x 20 steps: "
      f"all prime — fields for free with zero archimedean input")

# ────────────────────────────────────────────────────────────────────
section("S4. THE PROPERNESS CRITERION: destination iff finite "
        "sublevels")
# ────────────────────────────────────────────────────────────────────
# (i) c = Omega has ALL primes in one fiber (infinite sublevel): the
# odd-preferring tie-break starves 2 indefinitely.
N = 1
for step in range(30):
    adm = [m for m in range(2, SCAN + 1) if gcd(m, N) == 1]
    lvl = min(omega_mult(m) for m in adm)
    tier = [m for m in adm if omega_mult(m) == lvl]
    check(2 in tier or N % 2 == 0, "2 should stay admissible")
    odd = [m for m in tier if m != 2]
    m = min(odd)                        # adversarial: never 2
    N *= m
check(N % 2 == 1, "2 starved for 30 steps under the infinite fiber")
print("(i) Omega cost + odd tie-break: 2 admissible and unpicked for "
      "30 steps — infinite sublevel => starvable")

# (ii) Proper scrambled-rank costs: every prime enters at exactly its
# rank bound; different scrambles = different routes, same destination.
UNIVERSE = primes_upto(200)             # 46 primes
routes = []
for scramble_seed in (1, 2, 3):
    r2 = random.Random(scramble_seed)
    ranks = list(range(len(UNIVERSE)))
    r2.shuffle(ranks)
    rank = dict(zip(UNIVERSE, ranks))
    order = sorted(UNIVERSE, key=lambda p: rank[p])

    def cost(m):
        if m in rank:
            return rank[m]
        return 10 ** 9 + omega_mult(m)  # composites always dearer

    N = 1
    route = []
    for step in range(len(UNIVERSE)):
        adm = [m for m in range(2, 201) if gcd(m, N) == 1]
        m = min(adm, key=cost)
        route.append(m)
        N *= m
        entered = step + 1
        bound = sum(1 for q in UNIVERSE if rank[q] <= rank[m])
        check(entered == bound, f"entry step != rank bound at {m}")
    check(route == order, "route must be the cost order")
    check(sorted(route) == UNIVERSE, "destination = whole universe")
    routes.append(tuple(route))
check(len(set(routes)) == 3, "3 scrambles must give 3 distinct routes")
print("(ii) 3 proper scrambled costs x 46 primes: every prime enters "
      "at its rank bound; 3 distinct routes, one destination — the "
      "route is a free external choice, the destination is not")

# ────────────────────────────────────────────────────────────────────
section("S5. THE PRATT ORDER: what window data CAN route")
# ────────────────────────────────────────────────────────────────────
# Arrival constraint (window-visible): every prime factor of q-1 must
# already be a window. Parents(q) = prime factors of q-1: the Pratt
# certificate DAG. Increasing order extends it (parents < child).
P300 = primes_upto(2000)[:300]
for p in P300:
    if p > 2:
        for q in factorize(p - 1):
            check(q < p, f"Pratt parent {q} !< {p}")
print(f"parents < child for the first {len(P300)} primes: the "
      f"primorial (increasing) route is a linear extension")

PRATT_N = 20
PP = primes_upto(200)[:PRATT_N]
idx = {p: i for i, p in enumerate(PP)}
parent_mask = [0] * PRATT_N
for p in PP:
    if p > 2:
        for q in factorize(p - 1):
            parent_mask[idx[p]] |= 1 << idx[q]
child_mask = [0] * PRATT_N
for i in range(PRATT_N):
    for j in range(PRATT_N):
        if parent_mask[j] >> i & 1:
            child_mask[i] |= 1 << j

# the constraint forces 2 first: 2 is the only parentless prime
roots = [PP[i] for i in range(PRATT_N) if parent_mask[i] == 0]
check(roots == [2], f"parentless primes {roots} != [2]")
# available after {2}: primes whose parents are within {2} = Fermat
avail = [PP[i] for i in range(PRATT_N)
         if parent_mask[i] & ~1 == 0 and i != 0]
check(avail == [3, 5, 17], f"after {{2}}: {avail} != Fermat primes")
print(f"2 is the only parentless prime (forced first); available "
      f"after {{2}}: {avail} — exactly the Fermat primes in range")

# downset DP: f[S] = # linear extensions of the poset restricted to S
# (first-k prefixes are downsets since parents < child).
f = [0] * (1 << PRATT_N)
f[0] = 1
for S in range(1, 1 << PRATT_N):
    ok = True
    T = S
    while T:
        i = (T & -T).bit_length() - 1
        if parent_mask[i] & ~S:
            ok = False
            break
        T &= T - 1
    if not ok:
        continue
    tot = 0
    T = S
    while T:
        i = (T & -T).bit_length() - 1
        if not (child_mask[i] & S):
            tot += f[S & ~(1 << i)]
        T &= T - 1
    f[S] = tot

exts = {n: f[(1 << n) - 1] for n in (1, 2, 3, 5, 10, 15, 20)}
check(exts[1] == 1 and exts[2] == 1, "hand cases: {2}, {2<3}")
check(exts[3] == 2, "hand case: 2 then {3,5} free")
print(f"{'n':>3} {'extensions':>16} {'n!':>22} {'ratio':>12}")
prev_ratio = None
for n in (5, 10, 15, 20):
    ratio = exts[n] / factorial(n)
    print(f"{n:>3} {exts[n]:>16,} {factorial(n):>22,} {ratio:>12.3e}")
    if prev_ratio is not None:
        check(ratio < prev_ratio, "ratio must collapse")
    check(exts[n] > exts.get(n - 5, 0), "extensions must grow")
    prev_ratio = ratio
print("the window order routes only weakly: freedom explodes "
      "absolutely, collapses relatively — the residue is the "
      "archimedean route information")

# ────────────────────────────────────────────────────────────────────
section("S6. THE CRYSTALLIZATION CURVE: certainty at half coverage, "
        "statistics from zero")
# ────────────────────────────────────────────────────────────────────
# (a) determined singles == max(0, 2Q - X), exhaustively.
budgets = 0
for X in range(2, 241):
    for Q in range(1, X + 1):
        det = sum(1 for n in range(1, X + 1)
                  if n - Q < 1 and n + Q > X)
        check(det == max(0, 2 * Q - X), f"singles at X={X},Q={Q}")
        budgets += 1
print(f"(a) determined singles == max(0, 2Q - X) at {budgets} "
      f"budgets (X <= 240): flat zero below HALF coverage, linear "
      f"to full")


def fiber_stats(X, Q):
    stats = {}
    for r in range(Q):
        lifts = list(range(r if r >= 1 else Q, X + 1, Q))
        if lifts:
            stats[r] = (min(lifts), max(lifts), len(lifts))
    return stats


def determined_pairs(X, Q):
    st = fiber_stats(X, Q)
    total = 0
    keys = list(st)
    for i, r in enumerate(keys):
        for s in keys[i + 1:]:
            (amin, amax, ac), (bmin, bmax, bc) = st[r], st[s]
            if amax < bmin or bmax < amin:
                total += 2 * ac * bc        # ordered pairs
    return total


# (b) the sub-ring cap: a proper divisor budget has Q <= X/2, so by
# the half-coverage law (c) it is certainty-blind — zero singles AND
# zero pairs (the hiding lemma's home case).
rigid_budgets = 0
for X in range(4, 241):
    for Q in range(2, X):
        if X % Q == 0:
            check(max(0, 2 * Q - X) == 0, "rigid singles")
            check(determined_pairs(X, Q) == 0, f"rigid pairs X={X},Q={Q}")
            rigid_budgets += 1
print(f"(b) the sub-ring cap: 0 singles + 0 pairs at all "
      f"{rigid_budgets} proper-divisor budgets X <= 240 — a proper "
      f"divisor never exceeds half coverage (seats the hiding lemma)")

# (c) THE HALF-COVERAGE LAW, pair side (the frozen ragged-leak
# prediction REFUTED by the first run — see docstring adjudication).
# Every fiber's least lift is <= Q and its greatest is > X - Q, so
# fiber spans always overlap unless Q >= (X+2)/2: determined pairs
# exist iff 2Q - X >= 2, one step after the singles onset (at
# 2Q - X = 1 the one determined middle element sits strictly inside
# every other fiber's span).
pair_budgets = 0
for X in range(2, 121):
    for Q in range(1, X + 1):
        has_pairs = determined_pairs(X, Q) > 0
        check(has_pairs == (2 * Q - X >= 2),
              f"pair onset at X={X},Q={Q}")
        pair_budgets += 1
print(f"(c) THE HALF-COVERAGE LAW at {pair_budgets} budgets: "
      f"determined pairs > 0 iff 2Q - X >= 2 — NO certainty of any "
      f"kind at or below half coverage, ragged or rigid; the frozen "
      f"below-half leak prediction is refuted")

# (d) the statistical shadow: exact rigid accuracy law (derivation A,
# frozen pre-run): optimal comparison accuracy = (X + Q - 2)/(2(X-1)).
rigid_acc = 0
for X in range(4, 121):
    for Q in range(1, X + 1):
        if X % Q == 0:
            fibers = [[n for n in range(1, X + 1) if n % Q == r]
                      for r in range(Q)]
            correct = 0
            for fr in fibers:
                for fs in fibers:
                    lt = sum(1 for n in fr for m in fs if n < m)
                    gt = sum(1 for n in fr for m in fs if n > m)
                    correct += max(lt, gt)
            check(2 * correct == X * (X + Q - 2),
                  f"accuracy law at X={X},Q={Q}")
            rigid_acc += 1
print(f"(d) rigid accuracy == (X + Q - 2)/(2(X - 1)) EXACTLY at all "
      f"{rigid_acc} rigid budgets X <= 120: order leaks at rho/2 "
      f"from the first window while certainty sleeps below half")

# (e) growth reading: the rung N = 30 tower against horizon X = 50.
det = [n for n in range(1, 51) if n - 30 < 1 and n + 30 > 50]
check(det == list(range(21, 31)), "N=30, X=50 specimen")
check(max(0, 2 * 30 - 50) == 10, "formula agrees: 10 elements")
print("(e) growth reading: N = 30 vs horizon 50 determines exactly "
      "21..30 — a tower crystallizes nothing below half its horizon, "
      "everything at it")

print()
print(f"ALL SECTIONS PASS — {CHECKS} checks")
