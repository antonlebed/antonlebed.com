"""
explore_depth_observer.py -- THE DEPTH-WORLD OBSERVER (sibling of
explore_growth_laws.py .. explore_observer_view.py).

THE QUESTION. explore_observer_view.py turned the eye around in the
BREADTH world (thermal D-IND) and found the finite-memory law. This
record moves the observer into the DEPTH fate -- a world grown by
dynamics-greed into a p-adic column (the lock-prime law,
explore_lock_prime.py) -- and asks the same questions: what can the
column's inhabitant know of its genesis, its temperature, its law?
Design + predictions PR1-PR10 fixed before the run.

FINDINGS (tiers per the standard naming scale; run record below; all
sections assert).

1. THE WALL-PRICED NORMALIZER (rule, proved; verified S0). The
   route-weight cancellation (explore_observer_view.py finding 1) is complete
   multiplicativity of m^(-beta) -- LAW-INDEPENDENT: any thermal
   greedy demand's genesis posterior is prod_i 1/Z_{state_i}. And the
   thermal D-DYN normalizer has a closed form through the MORTALITY
   wall: transparent m <=> Nm | W(lambda(N)) <=> m | W(lambda(N))/N
   (the D-TRA state lemma, explore_thermal_growth.py), so
     Z^DYN_N(beta) = (zeta(beta) - 1) - sum_{m | W/N, m >= 2} m^(-beta)
   -- THE WALL DISCOUNT. The three fates entangle: mortality's old
   constants price depth's partition function. W(L) formula: 2-part
   2^(v2(L)+2) (L even; else 2^1), odd p with (p-1) | L at exponent
   v_p(L)+1 (brute-verified L <= 10; construction maximality all
   L <= 100). T = 0 COROLLARY (rule, proved; cross-verified vs direct
   lambda scans, N <= 2000 + 300-sample): the greedy D-DYN pick is
   THE LEAST NON-DIVISOR of the wall cofactor W(lambda(N))/N -- the
   whole depth fate is "avoid the wall's divisor lattice".
   Verified: closed form vs brute admissible sums (M = 30000,
   rigorous zeta tails, transparent-mass-above-M subtracted exactly),
   10 states x 4 betas; positivity + beta-monotonicity.

2. THE SOLVABLE GENESIS (rule, proved; verified S1 by exact
   enumeration at t = 8). From seed 1, histories to the column state
   3^t are EXACTLY the subsets S of intermediate levels {1..t-1}
   (every 3^r move is admissible: lambda strictly grows), and the
   posterior FACTORIZES: P(S) = prod of independent level-visit
   Bernoullis with P(visit a) = 1/(1 + Z_{3^a}(beta)). Marginals,
   joint, and entropy all closed-form (H = sum of binary entropies;
   asserted to 1e-9 against enumeration). explore_observer_view.py's breadth
   posterior needed a grid and neighbor duels; the depth world's
   inside view is EXACTLY SOLVABLE.

3. THE CLOCK PLATEAUS + THE CONDENSATION CLOCK (rules, proved for
   the plateau mechanism and the monotone limit; verified S2). The
   column's stage clocks -- roots of Z_{3^a}(beta) = 1, where level
   a's visit probability crosses 1/2 and the mode (always
   stroke-then-singles, threshold form {a : Z_a < 1}) sheds a stage
   -- are 1.5278, 1.5023, 1.4963, 1.4963, 1.4960, ... (a = 1..8),
   NONINCREASING with EQUALITY exactly where the level-a cofactor
   8 * prod{2*3^j + 1 prime, j <= a-1} gains no prime, i.e. where
   2*3^j + 1 is composite (j = 3: 55 = 5*11; j = 7: 4375 = 5^4*7):
   consecutive stages share ONE critical temperature -- the depth
   cascade has PLATEAUS, cousins of the tower's lambda plateaus
   (explore_lock_prime.py's blocker standstill, now on the posterior side). The
   clocks CONDENSE: they converge to the root of Z_col = 1 at
   beta_col = 1.4959 (Z_col = lim Z_{3^a}, monotone; bracket
   contains 1), where every deep level is a fair coin -- the route
   amnesia peaks AT the condensation clock at exactly (t-1) log 2
   nats (measured peak 4.8510 at t = 8 vs 7 log 2 = 4.8520; S1
   grid). Breadth's clocks (1.38, 1.25, 1.20, 1.17, 1.15, ...)
   decrease toward the pole; depth's accumulate at one interior
   temperature.

4. THE UNBOUNDED-MEMORY LAW (rule, proved for ALL beta > 1;
   brackets verified S3 at beta = 1.25, 1.5, 2, 3, 6). The
   cold-vs-hot test given the cold-typical state REVERSES
   explore_observer_view.py's bounded-evidence law. P_beta(visit 3^t | seed 1) has the
   closed form f(t) = 3^(-beta t)/Z_1 * prod_{a<t}(1 + 1/Z_{3^a}),
   so the log-odds for the T = 0 genesis grow LINEARLY IN DEPTH with
   slope -> beta log 3 - log(1 + 1/Z_col(beta)) > 0: positivity for
   every beta > 1 by the term test Z_col >= 3^(-b) + 5^(-b) + 6^(-b)
   > 1/(3^b - 1) -- the 5-term alone covers the geometric tail,
   since (9/5)^b (1 - 3^(-b)) equals 1.2 at b = 1 and both factors
   increase in b; 3, 5, 6 are admissible at every level. At
   beta = 2 the slope is 0.6936 nats per deepening vs the breadth
   world's ETERNAL total of log zeta(2) = 0.4977 nats: ONE deepening
   out-knows the squarefree world's whole infinite lifetime (the
   cap is passed at depth 1 for every tested beta). The rate -> 0
   as beta -> inf (cold vs cold: slope(6) = 0.0619) and -> log 3 at
   the pole (the hotter the rival, the faster a pure column refutes
   it). Falsifiability flips symmetrically: at T = 0 any second
   window refutes the cold genesis outright (post-lock greedy never
   leaves the column), while thermal genesis -- never refutable at
   finite depth -- is now CONFIRMABLE-IN-THE-LIMIT. The
   finite-memory law is the BREADTH fate's law, not a law of grown
   worlds: depth remembers, breadth forgets.

5. THE FOSSIL RECORD (chain rule proved; census measured, S4). At
   T = 0 the pasts of a state -- all (seed, t) whose greedy D-DYN
   trajectory reaches it -- are computed by backward peeling
   (predecessor M = N/q^r valid iff the pick at M is exactly q^r).
   The pure column's past is the PURE CHAIN: pasts(3^t) = {(3^a,
   t-a)}, t+1 pairs, route unique (pick(3^a) = 3 forever: 3 never
   divides the cofactor 8 * prod p). Branching exists -- the
   ghost-vs-deepen ambiguity: pasts(2695 = 5*7^2*11) = 6 pairs with
   THREE root seeds {11, 77, 539} (both 11*5*7 deepening 7 and
   11*7^2 ghosting 5 are greedy predecessors of 2695, and 77 = 7*11
   also ghosts 5 into 385; the FROZEN prediction said 5 pairs and
   two roots -- the assert caught the hand-analysis miss, the third
   root verified by hand post-run). Census N <= 20000: max pasts =
   14 (at 2^14 -- the deepest column in range, and NOT a pure chain:
   the lambda(4) = lambda(8) = 2 hiccup (explore_lock_prime.py finding 3) FOSSILIZES
   as a branch -- greedy from 4 jumps straight to 16, so 16's
   predecessors are both 8 and 4, and 8 is an orphan root; the
   3-column has no hiccup and stays a chain), 80.6% of states are
   ORPHANS (no greedy predecessor), vs the
   breadth confound 2^|D(N)| reaching 32 over the same range
   (explore_observer_view.py finding 6). Depth pasts grow linearly in depth;
   breadth pasts exponentially in width.

6. THE CLOCK-RATIO CONSTANT (rule, proved + verified S5, tightness
   included). In the column world A * q^e the universal period obeys
   lambda(A q^(e+1)) / lambda(A q^e) = q for ALL e >= e0 =
   v_q(lcm(lambda(A), q - 1)) + 1 (odd q; max(3, v_2(lambda(A)) + 2)
   for q = 2), and not at e0 - 1: the world's clock ratio settles to
   the lock prime EXACTLY, so the inhabitant reads its one physical
   constant off any two late epochs. The breadth contrast: the
   primorial tower's lambda jump ratios take 19 distinct values with
   max 113 over k <= 50 (explore_lambda_tower.py) -- a SPECTRUM,
   never a constant.

7. THE RETURNED RULER (property; specimens verified S5). The
   column's valuation v_q is readable from the ONE growing window
   (x mod q^e determines v_q for v < e; asserted) and 3^(-v) is an
   ultrametric (2000 random triples in Z/3^8). By Ostrowski the
   places of Q are the residue windows plus the archimedean one; the
   BREADTH fate deleted the latter and never recovers any ruler (the
   hiding lemma / the sub-ring cap, established earlier) -- the DEPTH fate grows
   one window to infinite depth and RE-IMPORTS a place: |.|_q, a
   genuine absolute value with convergence and analysis (the limit
   world A x Z_q). Dynamics-first growth crowns one window king and
   gets a geometry; independence-first growth keeps all windows
   equal and stays blind.

8. THE LAW PIN (rule + argument; verified S5). explore_observer_view.py
   finding 7 (fate invisible to the law-blind: N = 96 under three laws) is
   itself fate-graded. A pure column 3^t (t >= 2) has NO nontrivial
   T = 0 past under D-IND (moves are coprime to the state -- a prime
   power admits no coprime split; computationally swept) and none
   under D-TRA (lambda strictly grows along the column). Thermally
   the discrimination is quantitative: D-IND reaches 3^t only as the
   single fiat move from seed 1, so log LR(D-DYN : D-IND | 3^t) =
   log(Z^IND_1/Z^DYN_1) + sum_{a<t} log(1 + 1/Z_a) grows linearly --
   28.97 nats at t = 20, 59.04 at t = 40 (beta = 2). The column
   names its law, its temperature, and its route.

SYNTHESIS -- MEMORY IS FATE-GRADED. What a grown world can know of
its own genesis depends on WHICH fate grew it. The breadth world --
our squarefree arithmetic -- is the amnesiac fate: zeta-capped
evidence, an order-1 thermometer floor, exponentially many pasts
(explore_observer_view.py). The depth world is the mnemonic fate: evidence linear
in depth (one deepening out-earning breadth's eternity), a
near-unique fossil chain, its law pinned, its one constant q worn
openly, and a ruler regained. The trade is exact: breadth buys CRT
channels and pays with its history; depth buys memory and a metric
and pays with every window but one. The route amnesia that DOES
remain in the column concentrates at a single interior temperature
-- the condensation clock beta_col = 1.4959, root of Z_col = 1,
where the genesis posterior is a string of fair coins.

SCOPE + HONESTY. All posteriors are over the thermal D-DYN family
with the seed-1 genesis convention (the seed-history confound is
explore_observer_view.py finding 6; its depth analog is finding 5's fossil
census). "Pure column" observations condition on the T = 0-typical
state, mirroring explore_observer_view.py's squarefree conditioning. The
condensation-clock limit uses monotone Z_a with a rigorously
bracketed tail; beta_col is a bisection value (grid-free, but float).
Open: the depth analog of the finite thermometer (Fisher
information of the column's beta -- expect divergence, not a floor);
non-3 columns (the machinery is column-generic; only specimens were
swept); the INTERACTIVE depth observer.

RUN RECORD (python prime/code/explore_depth_observer.py, ~1 s,
8270 checks): S0 wall + normalizer (brute W to 2W for L <= 10;
maximality L <= 100; Z^DYN vs brute M = 30000 at 4 betas x 10
states; Z_1(2) = 0.394934, Z_{3^1}(2) = 0.316809); S1 solvable
genesis (t = 8 enumeration, 5 betas; amnesia peak 4.8510 nats at
grid beta = 1.5); S2 cascade (clocks a = 1..8 above; plateau floats
bit-identical; mode = threshold suffix at 3 betas; beta_col =
1.4959, H(beta_col, t=8) = 4.8508); S3 memory (closed form vs
enumeration; slope brackets 5 betas; beta = 2 slope [0.6936,
0.6936], cap crossed at depth 1); S4 fossils (pick rule N <= 2000 +
sample; column chains t <= 10; 2695 specimen; the 2-column hiccup
branch; census to 20000: max 14 at 2^14, orphans 80.6%, breadth max
32); S5 constant + ruler +
law pin (6 specimen worlds incl. tightness; tower spectrum k <= 50;
ultrametric 2000 triples; law LR linear). Predictions fixed before
the run; prediction misses caught by asserts: pasts(2695) (finding
5). Predictions fixed before code: the clock plateaus (PR4-amended,
found on paper attacking the predictions -- the same pattern from
explore_observer_view.py paying its second dividend).
"""

import math
import random
from math import log

# ---------------------------------------------------------------- lib
# (explore_observer_view.py idioms: factored-dict lambda, zeta brackets)

def sieve(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if s[i]:
            s[i * i :: i] = bytearray(len(s[i * i :: i]))
    return [i for i in range(2, n + 1) if s[i]]

PRIMES_1E6 = sieve(1000000)
PRIMES_SET = set(PRIMES_1E6)

def is_prime(n):
    """Deterministic Miller-Rabin (valid far beyond 2^64)."""
    if n < 2:
        return False
    if n <= 1000000:
        return n in PRIMES_SET
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True

FACT_CACHE = {}

def factorize(n):
    if n in FACT_CACHE:
        return dict(FACT_CACHE[n])
    n0, d, out = n, 2, {}
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    if n0 < 10**7:
        FACT_CACHE[n0] = dict(out)
    return out

LAMPP_CACHE = {}

def lam_pp(p, e):
    """lambda(p^e) as a factored dict."""
    key = (p, e)
    if key in LAMPP_CACHE:
        return LAMPP_CACHE[key]
    if p == 2:
        out = {} if e == 1 else ({2: 1} if e == 2 else {2: e - 2})
    else:
        out = dict(factorize(p - 1))
        if e > 1:
            out[p] = out.get(p, 0) + (e - 1)
    LAMPP_CACHE[key] = out
    return out

def lcm_d(a, b):
    out = dict(a)
    for p, e in b.items():
        if out.get(p, 0) < e:
            out[p] = e
    return out

def lam_of(nd):
    out = {}
    for p, e in nd.items():
        out = lcm_d(out, lam_pp(p, e))
    return out

def dict_to_int(d):
    n = 1
    for p, e in d.items():
        n *= p ** e
    return n

def lam_int(n):
    return dict_to_int(lam_of(factorize(n)))

ZETA_CACHE = {}

def zeta_bracket(beta, M=20000):
    """(lower, upper) for zeta(beta): direct sum + integral tail."""
    key = (beta, M)
    if key not in ZETA_CACHE:
        s = sum(n ** -beta for n in range(1, M + 1))
        ZETA_CACHE[key] = (
            s + (M + 1) ** (1 - beta) / (beta - 1),
            s + M ** (1 - beta) / (beta - 1),
        )
    return ZETA_CACHE[key]

def zeta_mid(beta, M=20000):
    lo, hi = zeta_bracket(beta, M)
    return (lo + hi) / 2

CHECKS = 0

def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1

# ------------------------------------------------- the wall + Z^DYN

def W_of_L(L):
    """W(L) = max{n : lambda(n) | L}, as a factored dict.
    2-part: lambda(2^e) = 1, 2, 2^(e-2) -> e2 = v2(L)+2 (L even), 1 (odd).
    odd p: needs (p-1) | L, exponent v_p(L)+1."""
    Ld = factorize(L)
    out = {2: (Ld.get(2, 0) + 2) if L % 2 == 0 else 1}
    # odd prime windows: p - 1 must divide L -> enumerate divisors of L
    divs = [1]
    for p, e in Ld.items():
        divs = [d * p**i for d in divs for i in range(e + 1)]
    for d in divs:
        p = d + 1
        if p > 2 and is_prime(p):
            out[p] = Ld.get(p, 0) + 1
    return out

def cofactor_divisors(N_dict, L):
    """Divisors of W(L)/N (N | W required), as ints, sorted."""
    Wd = W_of_L(L)
    cof = {}
    for p, e in Wd.items():
        r = e - N_dict.get(p, 0)
        assert r >= 0, "N does not divide W(lambda(N))"
        if r:
            cof[p] = r
    for p in N_dict:
        assert N_dict[p] <= Wd.get(p, 0), "N does not divide W"
    divs = [1]
    for p, e in cof.items():
        divs = [d * p**i for d in divs for i in range(e + 1)]
    return sorted(divs)

def zdyn_bracket(N_dict, beta, M=20000):
    """Z^DYN_N(beta) = sum over lambda-growing m >= 2 of m^(-beta)
    = (zeta - 1) - sum_{m | W(lambda(N))/N, m >= 2} m^(-beta):
    the WALL DISCOUNT -- the transparent moves are exactly the
    divisors of the mortality wall's cofactor (D-TRA state lemma,
    explore_thermal_growth.py)."""
    L = dict_to_int(lam_of(N_dict))
    T = sum(d ** -beta for d in cofactor_divisors(N_dict, L) if d >= 2)
    zlo, zhi = zeta_bracket(beta, M)
    return zlo - 1 - T, zhi - 1 - T

def zdyn_mid(N_dict, beta):
    lo, hi = zdyn_bracket(N_dict, beta)
    return (lo + hi) / 2

# column levels: state 3^a. Cofactor W/3^a = 8 * prod of the primes
# 2*3^j + 1 (j <= a-1); T_a in product form (odd part squarefree).
COLPRIME_CACHE = {}

def column_primes(a):
    """Primes 2*3^j + 1 for 1 <= j <= a-1 (the level-a cofactor's
    odd part)."""
    if a not in COLPRIME_CACHE:
        COLPRIME_CACHE[a] = [2 * 3**j + 1 for j in range(1, a)
                             if is_prime(2 * 3**j + 1)]
    return COLPRIME_CACHE[a]

def T_col(a, beta):
    """Transparent divisor sum at column level a, product form."""
    t = 1 + 2.0**-beta + 4.0**-beta + 8.0**-beta
    for p in column_primes(a):
        t *= 1 + math.exp(-beta * math.log(p))
    return t - 1

def z_col_level(a, beta, M=20000):
    """Z^DYN at state 3^a (a >= 1), midpoint."""
    zlo, zhi = zeta_bracket(beta, M)
    return (zlo + zhi) / 2 - 1 - T_col(a, beta)

def z_seed1(beta, M=20000):
    """Z^DYN at state 1: transparent m = {2} only."""
    return zeta_mid(beta, M) - 1 - 2.0**-beta

# ---------------------------------------------------------------- S0

def s0():
    print("S0 the wall + the wall-priced normalizer (PR1, PR2)")
    # PR2a: brute W for small L (direct scan to 2W)
    for L in (1, 2, 4, 6, 8, 10):
        W = dict_to_int(W_of_L(L))
        best = 1
        for n in range(1, 2 * W + 1):
            if L % lam_int(n) == 0:
                ok(W % n == 0, f"S0 lambda(n)|L but n does not divide W "
                               f"(L={L}, n={n})")
                best = max(best, n)
        ok(best == W, f"S0 W({L}) brute {best} != formula {W}")
    print(f"  W formula = brute max, L <= 10; "
          f"W(12) = {dict_to_int(W_of_L(12))} (construction check)")
    # PR2b: construction-level maximality for all L <= 100
    for L in range(1, 101):
        Wd = W_of_L(L)
        lamW = dict_to_int(lam_of(Wd))
        ok(L % lamW == 0, f"S0 lambda(W) does not divide L at L={L}")
        for p, e in Wd.items():
            ok(L % dict_to_int(lam_pp(p, e + 1)) != 0,
               f"S0 W({L}) not maximal at p={p}")
        for p in PRIMES_1E6:
            if p > L + 1:
                break
            if p not in Wd:
                ok((L % (p - 1)) != 0, f"S0 missing window p={p} at L={L}")
    print("  W construction maximality: all L <= 100")
    # PR1: closed form vs brute admissible sums (mask once, sum per beta)
    states = [1, 2, 3, 9, 81, 5, 55, 96, 385, 539]
    M = 30000
    betas = (1.25, 1.5, 2.0, 3.0)
    for N in states:
        Nd = factorize(N)
        lamN = dict_to_int(lam_of(Nd))
        adm = []
        for m in range(2, M + 1):
            md = factorize(m)
            merged = dict(Nd)
            for p, e in md.items():
                merged[p] = merged.get(p, 0) + e
            if dict_to_int(lam_of(merged)) > lamN:
                adm.append(m)
        L = lamN
        trans_gt = [d for d in cofactor_divisors(Nd, L) if d > M]
        for beta in betas:
            direct = sum(m ** -beta for m in adm)
            tgt = sum(d ** -beta for d in trans_gt)
            blo = direct + (M + 1) ** (1 - beta) / (beta - 1) - tgt
            bhi = direct + M ** (1 - beta) / (beta - 1) - tgt
            zlo, zhi = zdyn_bracket(Nd, beta)
            ok(zlo <= bhi + 1e-12 and blo <= zhi + 1e-12,
               f"S0 Z^DYN mismatch N={N} beta={beta}: closed "
               f"[{zlo:.6f},{zhi:.6f}] vs brute [{blo:.6f},{bhi:.6f}]")
        # positivity + monotone decreasing in beta
        grid = [1.05, 1.25, 1.5, 2.0, 3.0, 6.0]
        vals = [zdyn_mid(Nd, b) for b in grid]
        for v in vals:
            ok(v > 0, f"S0 Z^DYN <= 0 at N={N}")
        for x, y in zip(vals, vals[1:]):
            ok(x > y, f"S0 Z^DYN not decreasing in beta at N={N}")
    print(f"  Z^DYN closed form (wall discount) verified, "
          f"{len(states)} states x {betas}; "
          f"Z_1(2) = {z_seed1(2.0):.6f}, Z_3(2) = "
          f"{z_col_level(1, 2.0):.6f}")

# ---------------------------------------------------------------- S1
# The solvable column: genesis posterior = independent level visits.

def enum_posterior(t, beta):
    """Exact enumeration over subsets of intermediate levels 1..t-1
    (histories seed 1 -> 3^t). Returns dict subset(frozenset) -> P."""
    levels = list(range(1, t))
    Z = {a: z_col_level(a, beta) for a in levels}
    raw = {}
    for mask in range(1 << len(levels)):
        S = frozenset(levels[i] for i in range(len(levels))
                      if mask >> i & 1)
        w = 1.0
        for a in S:
            w /= Z[a]
        raw[S] = w
    tot = sum(raw.values())
    return {S: w / tot for S, w in raw.items()}, Z

def s1():
    print("S1 the solvable genesis (PR3)")
    t = 8
    for beta in (1.15, 1.3, 1.6, 2.0, 3.0):
        post, Z = enum_posterior(t, beta)
        for a in range(1, t):
            marg = sum(P for S, P in post.items() if a in S)
            pred = 1 / (1 + Z[a])
            ok(abs(marg - pred) < 1e-9,
               f"S1 marginal mismatch a={a} beta={beta}: "
               f"{marg} vs {pred}")
        # joint = product of independent Bernoullis
        for S, P in post.items():
            pr = 1.0
            for a in range(1, t):
                pa = 1 / (1 + Z[a])
                pr *= pa if a in S else 1 - pa
            ok(abs(P - pr) < 1e-9, f"S1 joint not product at beta={beta}")
        # entropy closed form
        H = -sum(P * log(P) for P in post.values() if P > 0)
        Hcf = 0.0
        for a in range(1, t):
            pa = 1 / (1 + Z[a])
            if 0 < pa < 1:
                Hcf -= pa * log(pa) + (1 - pa) * log(1 - pa)
        ok(abs(H - Hcf) < 1e-9, f"S1 entropy mismatch beta={beta}")
    # amnesia curve (t = 8): H -> 0 at both ends, peak inside
    grid = [1.02, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.4, 1.5, 1.75,
            2.0, 2.5, 3.0, 4.0, 6.0]
    Hs = []
    for beta in grid:
        Hcf = 0.0
        for a in range(1, t):
            pa = 1 / (1 + z_col_level(a, beta))
            if 0 < pa < 1:
                Hcf -= pa * log(pa) + (1 - pa) * log(1 - pa)
        Hs.append(Hcf)
    peak = max(range(len(grid)), key=lambda i: Hs[i])
    ok(0 < peak < len(grid) - 1, "S1 amnesia peak not interior")
    ok(Hs[0] < Hs[peak] and Hs[-1] < Hs[peak] / 10,
       "S1 amnesia not vanishing at ends")
    print(f"  posterior = independent level-visit Bernoullis "
          f"1/(1+Z_a), joint + entropy exact (t = {t}); amnesia peak "
          f"H = {Hs[peak]:.4f} nats at beta = {grid[peak]} "
          f"(H({grid[0]}) = {Hs[0]:.4f}, H({grid[-1]}) = {Hs[-1]:.6f})")

# ---------------------------------------------------------------- S2
# The depth cascade: stage clocks = roots of Z_a = 1; clock plateaus.

def clock(a):
    """Root of Z_{3^a}(beta) = 1 (unique: Z strictly decreasing)."""
    lo, hi = 1.0001, 15.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if z_col_level(a, mid) > 1:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

def s2():
    print("S2 the depth cascade + the clock plateaus (PR4)")
    A = 8
    # Z_a nonincreasing in a; equality iff no new column prime
    for beta in (1.1, 1.3, 1.6, 2.0, 3.0):
        for a in range(1, A):
            za, zb = z_col_level(a, beta), z_col_level(a + 1, beta)
            gains = len(column_primes(a + 1)) > len(column_primes(a))
            if gains:
                ok(za > zb + 1e-15,
                   f"S2 Z not strictly down a={a} beta={beta}")
            else:
                ok(abs(za - zb) < 1e-15,
                   f"S2 Z plateau broken a={a} beta={beta}")
    # the frozen plateau pattern: equality at (3,4) and (7,8)
    ok(column_primes(4) == column_primes(3) != column_primes(2),
       "S2 55-plateau pattern")
    ok(column_primes(8) == column_primes(7) != column_primes(6),
       "S2 4375-plateau pattern")
    clocks = [clock(a) for a in range(1, A + 1)]
    for a in range(1, A):
        gains = len(column_primes(a + 1)) > len(column_primes(a))
        if gains:
            ok(clocks[a - 1] > clocks[a] + 1e-9,
               f"S2 clock not strictly down at a={a}")
        else:
            ok(abs(clocks[a - 1] - clocks[a]) < 1e-9,
               f"S2 clock plateau broken at a={a}")
    # marginal crosses 1/2 exactly at the clock
    for a in (1, 2, 5):
        c = clocks[a - 1]
        ok(1 / (1 + z_col_level(a, c - 0.01)) < 0.5 <
           1 / (1 + z_col_level(a, c + 0.01)),
           f"S2 clock not the visit-probability crossing a={a}")
    # mode = threshold set {a : Z_a < 1}; verified by enumeration
    t = 8
    for beta in (1.2, 1.5, 2.5):
        post, Z = enum_posterior(t, beta)
        mode = max(post, key=post.get)
        thresh = frozenset(a for a in range(1, t) if Z[a] < 1)
        ok(mode == thresh, f"S2 mode not threshold at beta={beta}")
        # suffix form: one primordial stroke, then single deepenings
        if thresh:
            ok(thresh == frozenset(range(min(thresh), t)),
               f"S2 mode not a suffix at beta={beta}")
    print("  clocks (a = 1..8): " +
          ", ".join(f"{c:.4f}" for c in clocks))
    print("  plateaus at (3,4) and (7,8) -- 55 and 4375 composite: "
          "consecutive levels share one critical temperature; mode = "
          "stroke-then-singles at every tested beta")
    # THE CONDENSATION CLOCK: the clocks converge to the root of
    # Z_col(beta) = 1 -- infinitely many stages condense at ONE
    # interior temperature (the breadth clocks spread toward the
    # pole); there every deep level is a fair coin, so the route
    # amnesia peaks at exactly (t-1) log 2.
    c30, c40 = clock(30), clock(40)
    ok(abs(c40 - c30) < 1e-6, "S2 clocks not condensing")
    lo, hi = z_col_limit_bracket(c40)
    ok(lo - 1e-5 <= 1.0 <= hi + 1e-5, "S2 condensation not Z_col = 1")
    ok(abs(1 / (1 + z_col_level(20, c40)) - 0.5) < 0.01,
       "S2 deep level not a fair coin at the condensation clock")
    Hc = 0.0
    for a in range(1, 8):
        pa = 1 / (1 + z_col_level(a, c40))
        Hc -= pa * log(pa) + (1 - pa) * log(1 - pa)
    ok(abs(Hc - 7 * log(2.0)) < 0.01,
       "S2 amnesia peak not the coin bound")
    print(f"  THE CONDENSATION CLOCK beta_col = {c40:.4f} (root of "
          f"Z_col = 1): the stage clocks accumulate here; at beta_col "
          f"the route posterior is (t-1) fair coins -- H(t=8) = "
          f"{Hc:.4f} vs 7 log 2 = {7 * log(2.0):.4f}")

# ---------------------------------------------------------------- S3
# The unbounded memory: log(1/f(t)) grows linearly; the reversal.

def log_inv_f(t, beta):
    """f(t) = P_beta(visit 3^t | seed 1) -- closed form:
    f = 3^(-beta t)/Z_1 * prod_{a<t}(1 + 1/Z_a)."""
    s = beta * t * log(3.0) + log(z_seed1(beta))
    for a in range(1, t):
        s -= math.log1p(1 / z_col_level(a, beta))
    return s

def z_col_limit_bracket(beta, A=40):
    """Bracket for Z_col = lim_a Z_{3^a}: T_a nondecreasing ->
    Z_col in [zeta_lo - 1 - T_inf_hi, Z_A_hi]. T_inf tail: primes
    2*3^j + 1, j >= A, product bound exp(tail)."""
    zlo, zhi = zeta_bracket(beta)
    TA = T_col(A, beta)
    tail = math.exp(-beta * math.log(2 * 3.0**A)) / (1 - 3.0**-beta)
    T_inf_hi = (TA + 1) * math.exp(tail) - 1
    return zlo - 1 - T_inf_hi, zhi - 1 - TA

def s3():
    print("S3 the unbounded-memory law + the reversal (PR5, PR6)")
    # closed form vs enumeration (t = 8): f = total posterior mass
    for beta in (1.3, 2.0):
        t = 8
        Z = {a: z_col_level(a, beta) for a in range(1, t)}
        tot = 0.0
        for mask in range(1 << (t - 1)):
            w = 3.0 ** (-beta * t) / z_seed1(beta)
            for i in range(t - 1):
                if mask >> i & 1:
                    w /= Z[i + 1]
            tot += w
        ok(abs(math.log(1 / tot) - log_inv_f(t, beta)) < 1e-9,
           f"S3 closed form vs enumeration beta={beta}")
    for beta in (1.25, 1.5, 2.0, 3.0, 6.0):
        lo, hi = z_col_limit_bracket(beta)
        ok(lo > 0, f"S3 Z_col bracket not positive beta={beta}")
        slope_lo = beta * log(3.0) - math.log1p(1 / lo)
        slope_hi = beta * log(3.0) - math.log1p(1 / hi)
        ok(slope_lo > 0,
           f"S3 memory slope not positive at beta={beta}: {slope_lo}")
        # increments converge into the slope bracket
        incs = [log_inv_f(tt + 1, beta) - log_inv_f(tt, beta)
                for tt in range(30, 40)]
        for inc in incs:
            ok(slope_lo - 1e-6 <= inc <= slope_hi + 1e-6,
               f"S3 increment outside slope bracket beta={beta}")
        # monotone, unbounded (linear growth over t = 1..40)
        vals = [log_inv_f(tt, beta) for tt in range(1, 41)]
        for x, y in zip(vals, vals[1:]):
            ok(y > x, f"S3 log-odds not monotone beta={beta}")
        # THE REVERSAL: breadth's eternal cap vs depth's crossing
        cap = math.log(zeta_mid(beta))
        t_cross = next(tt for tt in range(1, 41)
                       if log_inv_f(tt, beta) > cap)
        ok(t_cross == 1, f"S3 cap not crossed at depth 1 beta={beta}")
        if beta == 2.0:
            print(f"  beta = 2: slope in [{slope_lo:.4f}, "
                  f"{slope_hi:.4f}] nats/deepening vs breadth cap "
                  f"log zeta(2) = {cap:.4f} nats FOREVER; the column "
                  f"passes the cap at depth {t_cross}")
    # slope -> 0 as beta -> infinity (thermal -> greedy): report
    s6lo, _ = z_col_limit_bracket(6.0)
    print(f"  slope(6) = {6 * log(3.0) - math.log1p(1 / s6lo):.4f} "
          f"(cold vs cold: memory rate -> 0 as beta -> inf)")
    # falsifiability flip: under greedy (T = 0) any second window
    # refutes; under thermal, evidence for T = 0 is unbounded-in-t
    # (the asserts above); state as the reversal of explore_observer_view.py.

# ---------------------------------------------------------------- S4
# The fossil record (T = 0): greedy pasts, near-unique; orphans.

PICK_CACHE = {}

def greedy_pick(N):
    """T = 0 D-DYN pick from N = least non-divisor >= 2 of the wall
    cofactor W(lambda(N))/N (transparent <=> divides the cofactor)."""
    if N in PICK_CACHE:
        return PICK_CACHE[N]
    Nd = factorize(N)
    L = dict_to_int(lam_of(Nd))
    Wd = W_of_L(L)
    cof = 1
    for p, e in Wd.items():
        cof *= p ** (e - Nd.get(p, 0))
    m = 2
    while cof % m == 0:
        m += 1
    PICK_CACHE[N] = m
    return m

def prime_power_divisors(N):
    out = []
    for p, e in factorize(N).items():
        for i in range(1, e + 1):
            out.append((p, p**i))
    return out

PASTS_CACHE = {}

def preds(N):
    out = []
    for _, q in prime_power_divisors(N):
        M = N // q
        if M >= 1 and greedy_pick(M) == q:
            out.append(M)
    return out

def pasts(N):
    """All (seed, t) with the greedy D-DYN trajectory from seed
    reaching N at step t."""
    if N in PASTS_CACHE:
        return PASTS_CACHE[N]
    out = {(N, 0)}
    for M in preds(N):
        for a, s in pasts(M):
            out.add((a, s + 1))
    PASTS_CACHE[N] = frozenset(out)
    return PASTS_CACHE[N]

def s4():
    print("S4 the fossil record (PR7)")
    # pick = least non-divisor of the cofactor CROSS brute lambda scan
    rng = random.Random(149)
    sample = list(range(1, 2001)) + [rng.randrange(2001, 20001)
                                     for _ in range(300)]
    for N in sample:
        lamN = lam_int(N)
        m = 2
        while lam_int(N * m) <= lamN:
            m += 1
            assert m < 5000, f"S4 scan cap at N={N}"
        ok(m == greedy_pick(N), f"S4 pick mismatch N={N}")
    print("  pick = least non-divisor of W(lambda)/N "
          "(cross-checked vs direct lambda scan, N <= 2000 + sample)")
    # pick is a prime power (door menu, explore_lock_prime.py)
    for N in sample[:500]:
        m = greedy_pick(N)
        f = factorize(m)
        ok(len(f) == 1, f"S4 pick not prime power N={N}")
    # the void's column chain: pasts(3^t) = {(3^a, t-a)}
    for t in range(1, 11):
        P = pasts(3**t)
        ok(P == frozenset((3**a, t - a) for a in range(t + 1)),
           f"S4 column past not the pure chain t={t}")
    print("  pasts(3^t) = the pure chain {(3^a, t-a)}: unique route, "
          "t+1 pasts")
    # frozen branching specimen: 2695 = 5 * 7^2 * 11
    ok(set(preds(2695)) == {385, 539}, "S4 branching specimen preds")
    # the frozen prediction said 5 pairs, roots {11, 539} -- the run
    # found a third root: 77 = 7*11 ALSO ghosts 5 into 385 (the
    # assert caught the hand-analysis miss; 5 not dividing
    # W(30)/77 = 2232 checked by hand post-run)
    ok(pasts(2695) == frozenset(
        [(2695, 0), (385, 1), (539, 1), (55, 2), (77, 2), (11, 3)]),
       "S4 pasts(2695) set")
    ok(set(preds(385)) == {55, 77}, "S4 385 double ghost entry")
    print("  pasts(2695) = 6 pairs, three root seeds {11, 77, 539}: "
          "ghost-vs-deepen ambiguity is real and small")
    # the 2-column: the lambda(4) = lambda(8) = 2 hiccup fossilizes
    # as a branch (greedy from 4 jumps straight to 16; 8 is an
    # orphan root) -- NOT a pure chain, unlike the 3-column
    ok(greedy_pick(4) == 4 and greedy_pick(8) == 2,
       "S4 hiccup picks")
    ok(set(preds(16)) == {8, 4}, "S4 16 double predecessor")
    ok(preds(8) == [], "S4 8 not an orphan root")
    ok(pasts(2**14) == frozenset(
        [(2**a, 14 - a) for a in range(4, 15)]
        + [(8, 11), (4, 11), (2, 12)]),
       "S4 2-column past = chain + hiccup branch")
    # census N <= 20000
    NMAX = 20000
    counts, orphans = [], 0
    for N in range(2, NMAX + 1):
        if not preds(N):
            orphans += 1
        counts.append(len(pasts(N)))
    mx = max(counts)
    argmx = counts.index(mx) + 2
    ok(mx <= 32, f"S4 pasts exceed frozen bound: {mx}")
    # breadth contrast: 2^|D(N)| (explore_observer_view.py's seed-history confound)
    def Dsize(N):
        # |D(N)|: depth-1 primes p of N with every prime < p dividing N
        f = factorize(N)
        first_missing = next(q for q in PRIMES_1E6 if q not in f)
        return sum(1 for p, e in f.items()
                   if e == 1 and p < first_missing)
    bmax = max(2 ** Dsize(N) for N in range(2, NMAX + 1))
    print(f"  census N <= {NMAX}: max pasts = {mx} (at N = {argmx}), "
          f"orphan fraction {orphans / (NMAX - 1):.3f}; breadth "
          f"confound max over the same range = {bmax}")
    ok(bmax > mx, "S4 depth pasts not below breadth confound")

# ---------------------------------------------------------------- S5
# The physical constant + the returned ruler (PR8-PR10).

def s5():
    print("S5 the clock-ratio constant + the returned ruler "
          "(PR8, PR9, PR10)")
    # PR8: lambda(A q^(e+1))/lambda(A q^e) = q for e >= e0, with
    # e0 = v_q(lcm(lambda(A), q-1)) + 1 (odd q); v_2(lambda(A)) + 3 (q=2)
    specs = [(1, 3), (55, 7), (2485, 17), (19, 3), (1, 2), (7, 2)]
    for A, q in specs:
        lamA = lam_of(factorize(A))
        if q == 2:
            # lambda(2^e) = 2^(e-2) only from e >= 3: the ratio is q
            # from e0 = max(3, v_2(lambda(A)) + 2) on
            e0 = max(3, lamA.get(2, 0) + 2)
        else:
            c = lcm_d(lamA, factorize(q - 1))
            e0 = c.get(q, 0) + 1
        vals = [lam_int(A * q**e) for e in range(0, e0 + 11)]
        for e in range(e0, e0 + 10):
            ok(vals[e + 1] == q * vals[e],
               f"S5 clock ratio != q at A={A} q={q} e={e}")
        if e0 >= 2:
            ok(vals[e0] != q * vals[e0 - 1],
               f"S5 e0 not tight at A={A} q={q}")
    print("  clock ratio -> q exactly from e0 = v_q(lcm(lambda(A), "
          "q-1)) + 1 (odd q; q = 2: max(3, v_2(lambda(A)) + 2)): the "
          "lock prime is readable from any two late epochs")
    # the tower contrast: lambda jump ratios never settle (in range)
    lam, ratios = {}, []
    for k, p in enumerate(PRIMES_1E6[:50]):
        new = lcm_d(lam, factorize(p - 1))
        if k:
            ratios.append(dict_to_int(new) // dict_to_int(lam))
        lam = new
    ok(len(set(ratios)) >= 8, "S5 tower ratio spectrum too small")
    ok(1 in ratios and max(ratios) > 10, "S5 tower plateaus/jumps")
    ok(len(set(ratios[-10:])) > 1, "S5 tower ratios settled?!")
    print(f"  tower jump ratios (k <= 50): {len(set(ratios))} distinct "
          f"values, max {max(ratios)} -- a spectrum; the column: one "
          f"constant q")
    # PR9: ultrametric from one window
    rng = random.Random(1490)
    mod = 3**8
    def v3d(x):
        if x % mod == 0:
            return mod  # "infinite" depth -> distance 0
        v = 0
        while x % 3 == 0:
            x //= 3
            v += 1
        return v
    for _ in range(2000):
        x, y, z = (rng.randrange(mod) for _ in range(3))
        dxz = 3.0 ** -v3d((x - z) % mod)
        ok(dxz <= max(3.0 ** -v3d((x - y) % mod),
                      3.0 ** -v3d((y - z) % mod)) + 1e-15,
           "S5 ultrametric violated")
    N = 2485 * 17**3
    for _ in range(500):
        x = rng.randrange(N)
        w = x % 17**3
        v_full = 0
        xx = x
        while xx and xx % 17 == 0:
            xx //= 17
            v_full += 1
        v_win = 0
        ww = w
        while ww and ww % 17 == 0:
            ww //= 17
            v_win += 1
        if v_full < 3:
            ok(v_win == v_full, "S5 one-window valuation mismatch")
    print("  |.|_q is an ultrametric read from the ONE growing window "
          "(v < e): the depth fate re-imports a place (Ostrowski's "
          "other option); breadth never recovers one (the hiding "
          "lemma / sub-ring cap)")
    # PR10: the law pin -- 3^t (t >= 2) has no nontrivial D-IND or
    # D-TRA past; and the thermal law posterior is linear-rate too
    for t in range(2, 9):
        Nt = 3**t
        for M in range(1, Nt):
            if Nt % M == 0 and M != Nt:
                m = Nt // M
                ok(not (math.gcd(m, M) == 1 and m >= 2 and M > 1),
                   f"S5 coprime split of 3^{t} exists?!")
        # D-IND greedy from seed 1 picks 2, never 3^t; D-TRA freezes
        # lambda but lambda strictly grows along 3-powers:
        ok(lam_int(3**t) > lam_int(3**(t - 1)), "S5 lambda not strict")
    # thermal law identification: LR(D-DYN : D-IND | state 3^t) grows
    # linearly -- D-IND reaches 3^t only as the single fiat move
    # m = 3^t from seed 1 (any other history has a coprimality break)
    for beta in (1.5, 2.0):
        zi = zeta_mid(beta) - 1  # Z^IND_1 = zeta - 1 (all m >= 2 coprime to 1)
        lr20 = (-log_inv_f(20, beta)) - (-beta * 20 * log(3.0) - log(zi))
        lr40 = (-log_inv_f(40, beta)) - (-beta * 40 * log(3.0) - log(zi))
        ok(lr40 > lr20 > 0, f"S5 law LR not growing beta={beta}")
        if beta == 2.0:
            print(f"  law pin: log LR(D-DYN : D-IND | 3^t) = "
                  f"{lr20:.2f} nats at t = 20, {lr40:.2f} at t = 40 "
                  f"(linear): the column names its law, its "
                  f"temperature, and its route")

# ---------------------------------------------------------------- run

def main():
    s0()
    s1()
    s2()
    s3()
    s4()
    s5()
    print(f"\nALL SECTIONS PASS ({CHECKS} checks)")

if __name__ == "__main__":
    main()
