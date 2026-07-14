"""
explore_observer_view.py -- THE INSIDE VIEW (THE HUNT chamber six,
P148; sibling of explore_growth_laws.py P143, explore_growth_
capability.py P144, explore_size_crystallization.py P145,
explore_lock_prime.py P146, explore_thermal_growth.py P147).

THE QUESTION. P143-P147 studied growth from OUTSIDE (seeds, routes,
temperatures given). Turn the eye around: an observer INSIDE a grown
world, whose entire epistemic access is the isomorphism class of its
ring -- the depth profile {(p, v_p(N))}, window vocabulary only (no
arrival log, no seed tag, no size). What can the world's inhabitant
know of its own GENESIS -- the temperature, the route, the seed, the
law, the fate? Design + frozen predictions PR1-PR9: SCRATCH P148
passes 2-3 (git). The observer's inference engine throughout is the
thermal D-IND law (P147): state normalizer Z_N(beta) =
zeta(beta) * prod_{p|N} (1 - p^(-beta)) - 1 (Euler-factor removal;
S0 verifies against brute coprime sums with rigorous tail brackets;
brute-summed for beta >= 5 where the closed form cancels).

FINDINGS (tiers per CLAUDE.md; run record below; all sections assert).

1. THE ROUTE-WEIGHT CANCELLATION (rule, proved). A genesis history
   from seed s to state N is an ordered coprime factorization of N/s
   (blocks = picks). Its Boltzmann numerator prod m_i^(-beta) =
   (N/s)^(-beta) is IDENTICAL for every history (complete
   multiplicativity), so the genesis posterior given the state is
   P(history) prop. to prod_i 1/Z_{state_i}(beta) -- all route
   information lives in the normalizer sequence: in what each
   intermediate world COULD have done otherwise, never in what it
   did. This makes every posterior below exact (no Monte Carlo).

2. THE BOUNDED-EVIDENCE LAW (rule, proved; verified S1). An observer
   in a squarefree world (the blueprint -- OUR arithmetic) testing
   crystal (beta = inf, genesis seed 1) against thermal beta: the
   likelihood ratio over the window primes <= P is
   prod_{p<=P} (1-p^(-beta))^(-1), monotone increasing, converging
   to zeta(beta). THE TOTAL EVIDENCE THE WHOLE INFINITE WORLD CAN
   EVER SUPPLY FOR THE CRYSTAL IS FINITE -- zeta(beta):1 odds,
   forever (1.6449:1 against beta = 2; 0.4977 nats). The evidence is
   small-prime-concentrated: p <= 10 carries 93.8% of it at beta = 2
   (83.2% at 1.5, 99.0% at 3). Falsifiability is ASYMMETRIC: one
   depth->=2 column refutes crystal-from-squarefree-genesis outright
   (the crystal never deepens -- sure, healing rule P143), while no
   finite observation ever refutes hot growth. Qualifier: the
   crystal side needs the genesis convention; without a seed
   convention beta = inf explains ANY state as a defective seed at
   t = 0 (finding 6). Verified: LR monotone over cutoffs 10..1e5,
   ceiling within the Euler tail bound of zeta at beta = 1.5, 2, 3;
   crystal-run squarefreeness asserted along 30-step trajectories.

3. THE FINITE THERMOMETER (rule -- convergence proved by integral
   bound; brackets computed S3; MLE measured). The state is the
   depth profile, so all temperature information is Fisher
   information of independent geometrics: I_p(beta) =
   (log p)^2 p^(-beta) / (1-p^(-beta))^2, and the TOTAL over all
   primes CONVERGES: I_total(2) in [0.8844, 0.8859] -- the whole
   infinite world carries a bounded amount of temperature
   information. Cramer-Rao: any unbiased inside estimate of beta = 2 has
   sd >= 1.062 (0.449 at beta = 1.5, 2.409 at 3) -- ORDER-1
   UNCERTAINTY FOREVER, concentrated in the small windows (p <= 10
   carries >= 65.0% at beta = 2). And the thermometer READS DEFECTS
   (PR9, proved + measured): on a squarefree sample the score is
   positive at EVERY beta, so the MLE diverges to the crystal --
   63.0% of simulated beta = 2 worlds read CRYSTAL (score still
   positive at the bisection ceiling beta = 12; in this run exactly
   the squarefree samples, though a lone deep column on a huge prime
   could also do it; law: squarefree probability 1/zeta(2) = 0.608)
   -- a FALSE CRYSTAL READING for the majority.
   Conditional on a finite MLE (defect-bearing worlds): mean 1.635
   (biased cold), sd 0.263 -- below the unconditional floor, as
   conditioning permits (CR binds unbiased whole-ensemble
   estimators). MLE harness: primes <= 3000, 300 replicates,
   bisection on the monotone score. (Scope sharpened at P153,
   chamber eleven: this cap is the STATE's -- an inhabitant that
   WATCHES the moves gains per-move information bounded below, so
   watched information grows without bound and passes this whole
   cap in one late move; the finite thermometer is the snapshot's
   compression artifact. explore_interactive_observer.py.)

4. THE CREATION-STORY TRANSITION + THE STAGED CASCADE (duel rule
   proved; cascade measured on a fine grid with its stage clocks
   proved for neighboring stages; S4). Compare the two extreme
   geneses of the crystal state p_n# from seed 1: GRADUALISM (n
   single-prime moves, ascending) vs FIAT (one move m = p_n#). By
   finding 1 the odds are 1/prod_{k=1}^{n-1} Z_{p_k#}(beta); each Z
   is strictly decreasing and continuous in beta with limits +inf
   (pole) and 0 (greedy), so the duel crosses 1 EXACTLY ONCE, at
   beta*(n = 3..7) = 1.3040, 1.2613, 1.2324, 1.2126, 1.1976 --
   decreasing in n. The GLOBAL mode does NOT jump fiat ->
   gradualism at beta*: on the fine grid (all histories, n = 5, 6)
   the mode is ALWAYS a PREFIX-BLOCK genesis -- one primordial
   stroke {p_1..p_j}, then single windows in ascending order
   (asserted at every grid point) -- with the stage count j falling
   monotonically n -> 1 as beta rises. Neighboring stages differ
   only in visiting p_{j-1}#, so the j vs j-1 duel crosses once, at
   the unique root of Z_{p_{j-1}#}(beta) = 1 (same monotonicity
   proof as beta*): THE STAGE CLOCKS, one per rung, INDEPENDENT of
   the world size n
   -- 1.3778 (k = 1), 1.2478 (k = 2), 1.1966 (k = 3), 1.1673
   (k = 4), 1.1518 (k = 5); every measured global flip bracket
   contains its clock (asserted, n = 5 and 6). Cold worlds infer
   gradualism, near-pole worlds fiat, and between them the inferred
   creation story adds stages one at a time: EACH RUNG OF THE TOWER
   GETS ITS OWN CRITICAL TEMPERATURE -- the beta at which that
   rung's total move mass Z passes 1. The first critical
   temperatures in the thermal family (the P147 JOURNAL watch item)
   -- properties of the observer's posterior, not of the growth
   laws (chamber five stands: the laws themselves exhibit none).

5. TEMPERATURE = AMNESIA, NON-MONOTONE + THE HAAR-EDGE ROUTE
   RESIDUE (measured on the grid; limit form proved). The genesis
   entropy H(history | state = p_n#, seed 1) -> 0 at BOTH ends
   (crystal certainty at beta = inf, fiat certainty near the pole)
   and peaks at finite temperature: 5.904 nats at beta = 1.3
   (n = 5, over Fubini(5) = 541 histories), 7.904 at beta = 1.2
   (n = 6). Conditioned on gradual genesis (all-singles), the order
   marginal has a NONDEGENERATE pole limit: the zeta factors cancel
   between equal-length histories, leaving exactly P(sigma) prop. to
   prod_i N_i/phi(N_i) over the intermediate states (rule, proved;
   TV(beta = 1.02 posterior, exact limit) = 0.0087). Ascending
   remains the modal order AT THE EDGE: P = 0.0268 vs uniform
   0.0083 (n = 5), H = 4.533 of max 4.787 nats. The route melts
   almost -- never fully: even the Haar shadow leans small-first.

6. THE SEED-HISTORY CONFOUND (rule, proved; exhaustive N <= 2000,
   S5). The crystal preimages of a state N -- pairs (seed, t) whose
   greedy D-IND trajectory passes through N -- are exactly the
   subsets of D(N) = {p : v_p(N) = 1 and every prime < p divides N}
   (pick set = the subset, seed = N / prod): count 2^|D(N)|. Even at
   ZERO temperature the state alone supports exponentially many
   pasts (N = 210 has 16); the genesis convention (seed 1) makes the
   past unique. Initial condition and history are separable from
   inside only by decree.

7. FATE IS INVISIBLE TO THE LAW-BLIND (witnesses + argument, S6).
   One state under three laws: N = 96 is one-step-reached by D-IND
   (from 32), D-DYN (from 48), and D-TRA (from 32); 161 states below
   500 are one-step-reachable under >= 2 distinct laws. Scope: under
   a KNOWN greedy law the snapshot computes the entire future
   (the laws are deterministic); what no finite snapshot reveals is
   WHICH law is writing the world -- and across laws the fates
   differ as limit properties (the three supernatural classes, P143
   -- all-finite-depth / one-infinite / finite), so the law-blind
   observer's fate is undecided at every finite time.

8. THE ANTHROPIC WEIGHT (rule + worked posterior, S7). Conditioning
   a temperature prior on the blueprint (squarefree = all-field
   windows) reweights it by exactly 1/zeta(beta) (P147 finding 3),
   and the expected number of defective columns is the prime zeta
   function sum_p p^(-beta) (0.8491 / 0.4522 / 0.1748 at beta = 1.5
   / 2 / 3; finitely many defects a.s. by Borel-Cantelli). Worked:
   a uniform prior on beta in [1.1, 4.0] moves its median only
   2.5 -> 2.9 given a squarefree world; the largest available Bayes
   factor is zeta(1.1)/zeta(4.0) = 9.78. "Why is MY arithmetic
   squarefree?" has a quantitative answer, and it is WEAK: the
   anthropic case for coldness is zeta-capped.

SYNTHESIS -- THE FINITE-MEMORY LAW. (Scoped at P149, chamber seven:
this is the BREADTH fate's law -- a world grown DEEP remembers its
genesis at a rate linear in depth; explore_depth_observer.py.)
A grown world of the breadth fate retains only
finitely much information about its own genesis: zeta-capped
evidence for the ground state (2), an order-1 temperature floor with
majority false-crystal readings (3), a genesis posterior that
re-concentrates at both temperature extremes and climbs the staged
creation cascade between them (4, 5), exponentially many pasts
absent a genesis decree (6), and a fate no law-blind snapshot
decides (7). P145 showed the route is authored by the deleted place;
the inside view shows the author left ALMOST no signature: what
survives is a 3:1 lean toward ascending entry (5) and one anthropic
factor of 1/zeta (8). An observer inside a squarefree all-primes
world -- us, if arithmetic were grown -- can bound but never know
how it was made.

HONEST SCOPE. Inference model = thermal D-IND with genesis seed 1
unless stated; beta ranges are grids (1.02..40); n <= 7 windows for
exact posteriors; the crystal-preimage rule is proved generally and
verified N <= 2000; fate underdetermination is one-step witnesses
plus the tail argument, not a census. The observer here is a
STATISTICIAN, not an agent: what an observer with dynamics (powers,
idempotents) could measure beyond the depth profile -- nothing; the
profile IS the isomorphism class -- but interactive protocols
(growing the world further and watching) are unexplored.

FROZEN-PREDICTION ADJUDICATION (SCRATCH P148 passes 2-3): PR1-PR3,
PR7, PR8 CONFIRMED as frozen. PR4 corrected pre-run by hand (80% ->
55-75% share; measured 65.0%); PR5/PR6 corrected pre-run by the
route-weight cancellation analysis (monotone amnesia was WRONG --
the fiat transition was found on paper before the run and confirmed
by it); PR9 (the false crystal reading) added pre-run, CONFIRMED.
The pre-run amendment pattern (P146) carried the chamber's two best
findings.

RUN RECORD (python prime/code/explore_observer_view.py, ~2.9 s,
689,596 checks): S0 normalizer closed form vs brute brackets, both
codepaths independently vs a direct sum in the overlap zone, Z
strictly decreasing; S1 evidence
ceilings 2.6124 / 1.6449 / 1.2021 at beta = 1.5 / 2 / 3, shares
83.2 / 93.8 / 99.0%, crystal probabilities 0.3828 / 0.6079 /
0.8319; S2 honest truncated-integer sampler (m <= 50000, no reuse
of the limit law), 300/300 trajectories fill the p <= 13 window,
defects mean 0.353 (law 0.436), squarefree 0.683 (law 0.618), both
in MC bands; S3 Fisher brackets + MC score-variance checks + MLE;
S4 Fubini counts 541/4683 asserted, posterior normalization, the
staged cascade (prefix-block mode + monotone stages asserted at
every fine-grid point, n = 5 and 6) with stage clocks inside every
flip bracket, beta* bisection, Haar-edge TV; S5 preimage counts for
all N <= 2000; S6 witnesses + 161-state scan; S7 posterior grid.
"""

import math
import random
from bisect import bisect_left
from math import log

# ---------------------------------------------------------------- lib

def sieve(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if s[i]:
            s[i * i :: i] = bytearray(len(s[i * i :: i]))
    return [i for i in range(2, n + 1) if s[i]]

PRIMES_1E5 = sieve(100000)
PRIMES_3000 = [p for p in PRIMES_1E5 if p <= 3000]
PRIMES_SMALL = [p for p in PRIMES_1E5 if p <= 50]

def factorize(n):
    d, out = 2, {}
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def lam_pp(p, e):
    """lambda(p^e) as a factored dict."""
    if p == 2:
        if e == 1:
            return {}
        if e == 2:
            return {2: 1}
        return {2: e - 2}
    f = factorize(p - 1)
    if e > 1:
        f[p] = f.get(p, 0) + (e - 1)
    return f

def lcm_d(a, b):
    out = dict(a)
    for p, e in b.items():
        out[p] = max(out.get(p, 0), e)
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

def z_state(present, beta):
    """Z_N(beta) = sum over admissible thermal D-IND moves m >= 2,
    gcd(m, N) = 1, of m^(-beta). Closed form via the Euler factors:
    zeta(beta) * prod_{p | N} (1 - p^(-beta)) - 1.
    For beta >= 5 the closed form cancels catastrophically
    (zeta*prod - 1 with both near 1), so brute-sum instead
    (tail < integral_{2000}^inf x^-5 dx, far below float noise)."""
    if beta < 5:
        prod = 1.0
        for p in present:
            prod *= 1 - p ** -beta
        return zeta_mid(beta) * prod - 1
    s = 0.0
    for m in range(2, 2001):
        ok_m = True
        for p in present:
            if m % p == 0:
                ok_m = False
                break
        if ok_m:
            s += m ** -beta
    return s

CHECKS = 0

def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1

# ---------------------------------------------------------------- S0
# The normalizer harness: closed form vs brute bracket; radical
# dependence; monotone decreasing in beta.

def z_brute_bracket(present, beta, M=200000):
    s = 0.0
    for m in range(2, M + 1):
        good = True
        for p in present:
            if m % p == 0:
                good = False
                break
        if good:
            s += m ** -beta
    return s, s + M ** (1 - beta) / (beta - 1)

def s0():
    print("S0 normalizer harness")
    states = [frozenset(), frozenset([2]), frozenset([2, 3]),
              frozenset([2, 3, 5]), frozenset([2, 3, 5, 7]),
              frozenset([2, 3, 5, 7, 11]), frozenset([3]),
              frozenset([2, 7])]
    for beta in (1.2, 1.5, 2.0, 3.0):
        for st in states:
            lo, hi = z_brute_bracket(st, beta, M=100000)
            z = z_state(st, beta)
            ok(lo - 1e-9 <= z <= hi + 1e-9,
               f"S0 Z mismatch present={sorted(st)} beta={beta}: "
               f"{z} not in [{lo},{hi}]")
    # both codepaths vs an independent direct sum in the overlap
    # zone: the closed form (beta < 5 path) AND the brute path
    # (beta >= 5, m <= 2000) must each match z_brute_bracket's
    # direct M = 100000 sum.
    for beta in (4.9, 5.0, 5.1):
        for st in states[:4]:
            prod = 1.0
            for p in st:
                prod *= 1 - p ** -beta
            closed = zeta_mid(beta) * prod - 1
            direct, _ = z_brute_bracket(st, beta, M=100000)
            ok(abs(closed - direct) < 1e-9,
               f"S0 closed-form mismatch {sorted(st)} beta={beta}")
            if beta >= 5:
                ok(abs(z_state(st, beta) - direct) < 1e-9,
                   f"S0 brute-path mismatch {sorted(st)} beta={beta}")
    # strictly decreasing in beta (grid; proved termwise anyway)
    grid = [1.05, 1.2, 1.5, 2.0, 3.0, 4.0]
    for st in states:
        vals = [z_state(st, b) for b in grid]
        for a, b in zip(vals, vals[1:]):
            ok(a > b, f"S0 Z not decreasing at {sorted(st)}")
    print(f"  Z closed form verified against brute brackets; "
          f"Z_1(2) = {z_state(frozenset(), 2.0):.6f} "
          f"(zeta(2) - 1 = {zeta_mid(2.0) - 1:.6f})")

# ---------------------------------------------------------------- S1
# THE BOUNDED-EVIDENCE LAW. Observer in a squarefree world, crystal
# (beta = inf, genesis seed 1) vs thermal beta, both predicting the
# depth profile. Likelihood ratio over the window [primes <= P]:
# crystal predicts all depths 1 surely; thermal predicts depth 1 at
# p w.p. (1 - p^-beta) (the P147 geometric law). LR = prod 1/(1-r).

def crystal_step(n):
    for p in PRIMES_1E5:
        if n % p:
            return p
    raise RuntimeError("universe exhausted")

def s1():
    print("S1 the bounded-evidence law")
    # crystal never deepens (sure; healing rule P143 observer-side)
    for seed in (1, 5, 77):
        n, missing_hist = seed, []
        for _ in range(30):
            p = crystal_step(n)
            missing_hist.append(p)
            n *= p
            fac = factorize(n // seed)
            ok(all(e == 1 for e in fac.values()),
               f"S1 crystal deepened off-seed at seed={seed}")
        ok(missing_hist == sorted(missing_hist),
           f"S1 crystal route not ascending from seed {seed}")
    # LR monotone in the window, converging to zeta(beta)
    shares = {}
    for beta in (1.5, 2.0, 3.0):
        z_lo, z_hi = zeta_bracket(beta, M=200000)
        cuts = [10, 100, 1000, 10000, 100000]
        lr_cuts, acc, ci = [], 0.0, 0
        for p in PRIMES_1E5:
            while ci < len(cuts) and p > cuts[ci]:
                lr_cuts.append(acc)
                ci += 1
            acc += -math.log(1 - p ** -beta)
        while ci < len(cuts):
            lr_cuts.append(acc)
            ci += 1
        for a, b in zip(lr_cuts, lr_cuts[1:]):
            ok(b >= a, f"S1 LR not monotone beta={beta}")
        # convergence: remaining tail above 1e5 is bounded by
        # sum_{n > 1e5} 2 n^-beta <= 2 * 1e5^(1-beta)/(beta-1)
        tail = 2 * 100000 ** (1 - beta) / (beta - 1)
        ok(lr_cuts[-1] <= math.log(z_hi) + 1e-12,
           f"S1 LR exceeds zeta beta={beta}")
        ok(math.log(z_lo) - lr_cuts[-1] <= tail + 1e-12,
           f"S1 LR gap above tail bound beta={beta}")
        share10 = lr_cuts[0] / math.log(zeta_mid(beta, M=200000))
        shares[beta] = share10
        print(f"  beta={beta}: total evidence = zeta = "
              f"{zeta_mid(beta, M=200000):.4f} "
              f"({math.log(zeta_mid(beta, M=200000)):.4f} nats, ceiling); "
              f"p <= 10 carries {100 * share10:.1f}% of it")
    ok(shares[2.0] >= 0.90, "S1 PR2 share miss")  # PR2
    # asymmetry: P(hot world shows NO defect ever) = 1/zeta(beta)
    for beta in (1.5, 2.0, 3.0):
        prod = 1.0
        for p in PRIMES_1E5:
            prod *= 1 - p ** -beta
        z_lo, z_hi = zeta_bracket(beta, M=200000)
        # prod over p <= 1e5 >= 1/zeta >= prod * (tail factor)
        ok(prod >= 1 / z_hi - 1e-9, f"S1 crystal prob low beta={beta}")
        ok(1 / z_lo >= prod * math.exp(-2 * 100000 ** (1 - beta)
                                       / (beta - 1)) - 1e-9,
           f"S1 crystal prob high beta={beta}")
        print(f"  beta={beta}: P(squarefree world) ~ {1 / z_lo:.4f}; "
              f"a squarefree observer's max odds for the crystal = "
              f"zeta = {z_lo:.4f} : 1, FOREVER")

# ---------------------------------------------------------------- S2
# Process spot check: honest truncated-integer thermal sampler (no
# reuse of the limit law), observer-visible statistics vs the law.

M_SAMP = 50000

def build_sampler(beta):
    w = [0.0] * (M_SAMP + 1)
    acc = 0.0
    for m in range(2, M_SAMP + 1):
        acc += m ** -beta
        w[m] = acc
    return w

def sample_pick(w, nd, rng):
    total = w[M_SAMP]
    for _ in range(200000):
        u = rng.random() * total
        m = bisect_left(w, u)
        if m < 2:
            m = 2
        good = True
        for p in nd:
            if m % p == 0:
                good = False
                break
        if good:
            return m
    raise RuntimeError("S2 sampler starved")

def s2():
    print("S2 process spot check (beta = 2, 300 trajectories)")
    beta = 2.0
    rng = random.Random(148)
    w = build_sampler(beta)
    window = [p for p in PRIMES_SMALL if p <= 13]
    defects, sqfree, done = [], 0, 0
    for _ in range(300):
        nd = {}
        for _ in range(60):
            m = sample_pick(w, nd, rng)
            fac = factorize(m)
            ok(all(p not in nd for p in fac),
               "S2 entry-once violated (non-coprime pick)")
            for p, e in fac.items():
                nd[p] = e
            if all(p in nd for p in window):
                break
        if not all(p in nd for p in window):
            continue
        done += 1
        d = sum(1 for p in window if nd[p] >= 2)
        defects.append(d)
        if d == 0:
            sqfree += 1
    ok(done >= 285, f"S2 only {done}/300 filled the window")
    mean_def = sum(defects) / done
    target_def = sum(p ** -beta for p in window)
    target_sq = 1.0
    for p in window:
        target_sq *= 1 - p ** -beta
    frac_sq = sqfree / done
    print(f"  window p <= 13: defects mean {mean_def:.3f} "
          f"(law {target_def:.3f}); squarefree {frac_sq:.3f} "
          f"(law {target_sq:.3f}); {done}/300 complete")
    ok(abs(mean_def - target_def) <= 0.11, "S2 PR3 defect mean miss")
    ok(abs(frac_sq - target_sq) <= 0.085, "S2 PR3 squarefree miss")

# ---------------------------------------------------------------- S3
# THE FINITE THERMOMETER. Fisher information of the depth profile
# about beta: per prime (geometric, ratio r = p^-beta)
# I_p = (log p)^2 r/(1-r)^2; the total over ALL primes converges.
# The MLE diverges to the crystal on squarefree samples (PR9).

def fisher_p(p, beta):
    r = p ** -beta
    return (log(p)) ** 2 * r / (1 - r) ** 2

def fisher_tail_bound(P0, beta):
    """sum_{p > P0} I_p <= (1-P0^-beta)^-2 * integral_{P0}^inf
    (log x)^2 x^-beta dx (every integer counted as if prime)."""
    a = beta - 1
    L = log(P0)
    integ = P0 ** -a * (L * L / a + 2 * L / a ** 2 + 2 / a ** 3)
    return integ / (1 - P0 ** -beta) ** 2

def s3():
    print("S3 the finite thermometer")
    rng = random.Random(1487)
    # (i) I_p formula vs MC score variance
    for p in (2, 5):
        beta, n = 2.0, 20000
        r = p ** -beta
        draws = []
        for _ in range(n):
            k, u = 1, rng.random()
            while u < r:
                u /= r
                k += 1
            draws.append(k)
        mean = sum(draws) / n
        var = sum((d - mean) ** 2 for d in draws) / (n - 1)
        emp_i = (log(p)) ** 2 * var
        ok(abs(emp_i - fisher_p(p, beta)) <= 0.06 * fisher_p(p, beta),
           f"S3 Fisher MC mismatch p={p}")
    # (ii) total information: finite, small-prime-concentrated
    floors = {}
    for beta in (1.5, 2.0, 3.0):
        part = sum(fisher_p(p, beta) for p in PRIMES_1E5)
        tail = fisher_tail_bound(100000.0, beta)
        i_lo, i_hi = part, part + tail
        floors[beta] = 1 / math.sqrt(i_hi)
        share10 = sum(fisher_p(p, beta) for p in (2, 3, 5, 7)) / i_hi
        print(f"  beta={beta}: I_total in [{i_lo:.4f}, {i_hi:.4f}] "
              f"(FINITE); CR floor sd >= {1 / math.sqrt(i_hi):.3f}; "
              f"p <= 10 share >= {100 * share10:.1f}%")
        # the tail bound counts every integer as prime -- tight at
        # beta >= 2, loose (but still FINITE, which is the claim)
        # at 1.5; the CR floor uses i_hi, so it stays conservative.
        ok(math.isfinite(tail) and tail > 0, f"S3 tail beta={beta}")
        if beta >= 2.0:
            ok(tail < 0.01 * part, f"S3 tail loose beta={beta}")
        if beta == 2.0:
            ok(0.55 <= share10 <= 0.75, "S3 PR4' share miss")
    # (iii) MLE experiment at beta0 = 2, primes <= 3000
    beta0, reps = 2.0, 300
    logps = [log(p) for p in PRIMES_3000]
    rs = [p ** -beta0 for p in PRIMES_3000]
    sq_target = 1.0
    for r in rs:
        sq_target *= 1 - r

    def score(beta, depths):
        s = 0.0
        for lp, d in zip(logps, depths):
            r = math.exp(-beta * lp)
            s += lp * (r / (1 - r) - (d - 1))
        return s

    ceil_ct, sq_ct, finite = 0, 0, []
    for _ in range(reps):
        depths = []
        for r in rs:
            k, u = 1, rng.random()
            while u < r:
                u /= r
                k += 1
            depths.append(k)
        if all(d == 1 for d in depths):
            sq_ct += 1
            ok(score(12.0, depths) > 0, "S3 PR9 squarefree score sign")
        if score(12.0, depths) > 0:
            ceil_ct += 1
            continue
        lo, hi = 1.05, 12.0
        for _ in range(40):
            mid = (lo + hi) / 2
            if score(mid, depths) > 0:
                lo = mid
            else:
                hi = mid
        finite.append((lo + hi) / 2)
    frac_ceil = ceil_ct / reps
    print(f"  MLE at beta0=2: {100 * frac_ceil:.1f}% of worlds read "
          f"CRYSTAL (score > 0 up to beta = 12; squarefree fraction "
          f"{sq_ct / reps:.3f}, law {sq_target:.3f})")
    ok(abs(frac_ceil - sq_target) <= 0.10, "S3 PR9 ceiling fraction")
    if finite:
        m = sum(finite) / len(finite)
        sd = math.sqrt(sum((x - m) ** 2 for x in finite)
                       / (len(finite) - 1))
        print(f"  finite-MLE ({len(finite)} worlds): mean {m:.3f}, "
              f"sd {sd:.3f} (CR floor {floors[2.0]:.3f}, "
              f"conditioning caveat)")
        ok(sd > 0.2, "S3 finite-MLE sd sanity")

# ---------------------------------------------------------------- S4
# TEMPERATURE = AMNESIA + THE CREATION-STORY TRANSITION. Exact
# genesis posterior given the state: histories = ordered coprime
# factorizations of N/seed = ordered set partitions of the prime
# columns; the Boltzmann numerator (N/seed)^-beta is history-
# invariant (complete multiplicativity), so
# P(history) prop. to prod_i 1/Z_{state_i}.

def ordered_partitions(items):
    """All ordered sequences of disjoint nonempty blocks covering
    items: enumerate the first block as any nonempty subset, then
    recurse (counts = Fubini numbers, asserted in s4)."""
    if not items:
        yield []
        return
    n = len(items)
    for mask in range(1, 1 << n):
        block = [items[i] for i in range(n) if mask >> i & 1]
        rem = [items[i] for i in range(n) if not mask >> i & 1]
        for tail in ordered_partitions(rem):
            yield [block] + tail

FUBINI = {3: 13, 4: 75, 5: 541, 6: 4683, 7: 47293}

def posterior(n, beta):
    """Exact genesis posterior for state p_n# from seed 1."""
    prs = PRIMES_SMALL[:n]
    zmemo = {}

    def zz(present):
        if present not in zmemo:
            zmemo[present] = z_state(present, beta)
        return zmemo[present]

    hists, weights = [], []
    for h in ordered_partitions(prs):
        present = frozenset()
        wgt = 1.0
        for block in h:
            wgt /= zz(present)
            present = present | frozenset(block)
        hists.append(h)
        weights.append(wgt)
    tot = sum(weights)
    qs = [w / tot for w in weights]
    for q in qs:
        ok(q >= 0, "S4 negative posterior")
    return hists, qs

def entropy(qs):
    return -sum(q * math.log(q) for q in qs if q > 0)

def is_ascending_singles(h):
    return all(len(b) == 1 for b in h) and \
        [b[0] for b in h] == sorted(b[0] for b in h)

def s4():
    print("S4 temperature = amnesia + the creation-story transition"
          " + the staged cascade")
    grid = [1.02, 1.05, 1.1, 1.2, 1.3, 1.5, 1.75, 2.0, 2.5,
            3.0, 4.0, 6.0, 10.0, 20.0, 40.0]
    for n in (5, 6):
        hs, _ = posterior(n, 2.0)
        ok(len(hs) == FUBINI[n], f"S4 Fubini count n={n}")
        ents, modes = [], []
        for beta in grid:
            hists, qs = posterior(n, beta)
            ents.append(entropy(qs))
            modes.append(hists[max(range(len(qs)), key=qs.__getitem__)])
        # PR5': -> 0 at both ends, interior peak
        peak = max(ents)
        pk_i = ents.index(peak)
        ok(0 < pk_i < len(grid) - 1, f"S4 PR5' peak at boundary n={n}")
        ok(ents[-1] < 0.05, f"S4 PR5' hot-end entropy n={n}")
        ok(ents[0] < peak and ents[-1] < peak,
           f"S4 PR5' no interior peak n={n}")
        # PR6': fiat mode near the pole, ascending singles when cold
        ok(len(modes[1]) == 1, f"S4 PR6' mode at 1.05 not fiat n={n}")
        for bi, beta in enumerate(grid):
            if beta >= 3.0:
                ok(is_ascending_singles(modes[bi]),
                   f"S4 PR6' cold mode not ascending n={n} beta={beta}")
        print(f"  n={n}: H(genesis|state) peak {peak:.3f} nats at "
              f"beta={grid[pk_i]}; H(1.02)={ents[0]:.3f}, "
              f"H(40)={ents[-1]:.5f}; mode at 1.05 = "
              f"{'FIAT' if len(modes[1]) == 1 else modes[1]}, "
              f"mode at 3.0 = ascending singles")
    # THE STAGED CREATION CASCADE: on a fine grid, the GLOBAL mode
    # (all histories) is always a PREFIX-BLOCK genesis -- one
    # primordial stroke {p_1..p_j} then single windows in ascending
    # order -- with the stage count j non-increasing in beta: the
    # duel root beta* below sits INSIDE the cascade; the full
    # gradualist mode arrives later.
    for n in (5, 6):
        prs = PRIMES_SMALL[:n]

        def prefix_j(h):
            """j if h is a prefix-block history, else None."""
            j = len(h[0])
            if sorted(h[0]) != prs[:j]:
                return None
            if any(len(b) != 1 for b in h[1:]):
                return None
            if [b[0] for b in h[1:]] != prs[j:]:
                return None
            return j

        stages, flips = [], []
        grid_fine = [i / 100 for i in range(102, 331, 2)]
        for beta in grid_fine:
            hists, qs = posterior(n, beta)
            h = hists[max(range(len(qs)), key=qs.__getitem__)]
            j = prefix_j(h)
            ok(j is not None,
               f"S4 non-prefix global mode n={n} beta={beta}: {h}")
            if stages and j != stages[-1]:
                ok(j < stages[-1],
                   f"S4 cascade not monotone n={n} beta={beta}")
                flips.append((beta, stages[-1], j))
            stages.append(j)
        ok(stages[0] == n, f"S4 cascade start not fiat n={n}")
        ok(stages[-1] == 1, f"S4 cascade end not gradualism n={n}")
        print(f"  staged creation cascade n={n}: mode = one stroke of"
              f" j windows then singles; j falls {n} -> 1 at beta = "
              + ", ".join(f"{b:.2f} ({a}->{c})" for b, a, c in flips))
        # THE STAGE CLOCKS: neighboring stages differ only in
        # visiting state p_{j-1}#, so the j -> j-1 duel flips at the
        # unique root of Z_{p_{j-1}#}(beta) = 1 (same monotonicity
        # proof as beta*) -- n-INDEPENDENT. Assert each measured
        # global flip bracket contains its stage clock.
        clocks = []
        for beta_flip, j_from, j_to in flips:
            st = frozenset(prs[:j_to])
            lo, hi = 1.01, 6.0
            for _ in range(60):
                mid = (lo + hi) / 2
                if z_state(st, mid) > 1:
                    lo = mid
                else:
                    hi = mid
            clock = (lo + hi) / 2
            clocks.append((j_to, clock))
            ok(beta_flip - 0.02 < clock <= beta_flip + 1e-9,
               f"S4 stage clock off n={n} {j_from}->{j_to}: "
               f"clock {clock:.4f} vs flip at {beta_flip}")
        print("  stage clocks (roots of Z_(p_k#)(beta) = 1, "
              "n-independent): "
              + ", ".join(f"k={k}: {c:.4f}" for k, c in clocks))
    # the asc-vs-fiat crossing: unique root of prod Z_{p_k#} = 1
    roots = {}
    for n in (3, 4, 5, 6, 7):
        states = []
        acc = frozenset()
        for p in PRIMES_SMALL[:n - 1]:
            acc = acc | frozenset([p])
            states.append(acc)

        def prodz(beta):
            v = 1.0
            for st in states:
                v *= z_state(st, beta)
            return v

        lo, hi = 1.01, 6.0
        ok(prodz(lo) > 1 and prodz(hi) < 1, f"S4 no sign change n={n}")
        for _ in range(60):
            mid = (lo + hi) / 2
            if prodz(mid) > 1:
                lo = mid
            else:
                hi = mid
        roots[n] = (lo + hi) / 2
        print(f"  beta*({n}) = {roots[n]:.4f}  "
              f"(fiat below, gradualism above)")
    ok(1.2 <= roots[5] <= 2.0, "S4 PR6' beta*(5) range")
    vals = [roots[n] for n in (3, 4, 5, 6, 7)]
    for a, b in zip(vals, vals[1:]):
        ok(a > b, "S4 beta* not decreasing in n")
    # the Haar-edge order marginal (singles-conditioned): exact limit
    # P(sigma) prop. to prod_i N_i/phi(N_i) over intermediates
    n = 5
    prs = PRIMES_SMALL[:n]
    import itertools
    orders = list(itertools.permutations(prs))

    def order_dist(beta):
        ws = []
        for sig in orders:
            present = frozenset()
            wgt = 1.0
            for p in sig:
                wgt /= z_state(present, beta)
                present = present | frozenset([p])
            ws.append(wgt)
        t = sum(ws)
        return [x / t for x in ws]

    d102 = order_dist(1.02)
    d105 = order_dist(1.05)
    lim = []
    for sig in orders:
        present = []
        wgt = 1.0
        for p in sig[:-1]:
            present.append(p)
            c = 1.0
            for q in present:
                c *= 1 - 1 / q
            wgt /= c
        lim.append(wgt)
    t = sum(lim)
    lim = [x / t for x in lim]
    tv_102_lim = sum(abs(a - b) for a, b in zip(d102, lim)) / 2
    tv_102_105 = sum(abs(a - b) for a, b in zip(d102, d105)) / 2
    asc = orders.index(tuple(sorted(prs)))
    ok(max(range(len(lim)), key=lim.__getitem__) == asc,
       "S4 Haar-edge order mode not ascending")
    ok(max(range(len(d102)), key=d102.__getitem__) == asc,
       "S4 1.02 order mode not ascending")
    ok(tv_102_lim < 0.05, f"S4 limit TV {tv_102_lim}")
    h_lim = entropy(lim)
    print(f"  Haar-edge order marginal (n=5, singles-conditioned): "
          f"TV(beta=1.02, exact limit prod N/phi(N)) = "
          f"{tv_102_lim:.4f}; TV(1.02, 1.05) = {tv_102_105:.4f}; "
          f"H = {h_lim:.3f} of max {math.log(120):.3f} nats; "
          f"mode = ascending, P = {lim[asc]:.4f} vs uniform "
          f"{1 / 120:.4f}")

# ---------------------------------------------------------------- S5
# THE SEED-HISTORY CONFOUND. Crystal (beta = inf) preimages of N:
# (seed, t) pairs whose greedy D-IND trajectory passes through N.
# Claim: pick sets = subsets of D(N) = {p : v_p(N) = 1 and every
# prime < p divides N}; count = 2^|D(N)|.

def divisors(n):
    out = [1]
    for p, e in factorize(n).items():
        out = [d * p ** k for d in out for k in range(e + 1)]
    return out

def s5():
    print("S5 the seed-history confound (crystal preimages)")
    for n in range(2, 2001):
        fac = factorize(n)
        prs = sorted(fac)
        dset = []
        for p in prs:
            if fac[p] != 1:
                continue
            if all(n % q == 0 for q in PRIMES_SMALL if q < p):
                dset.append(p)
        want = 2 ** len(dset)
        got = 0
        for s in divisors(n):
            cur = s
            while cur < n:
                cur *= crystal_step(cur)
            if cur == n:
                got += 1
        ok(got == want, f"S5 preimage count N={n}: {got} != {want}")
    ex = 2 * 3 * 5 * 7
    print(f"  verified count = 2^|D(N)| for all N <= 2000; "
          f"e.g. N = {ex} has {2 ** 4} crystal pasts without genesis, "
          f"1 with it")

# ---------------------------------------------------------------- S6
# FATE IS INVISIBLE FROM INSIDE: one state, three laws.

def greedy_dyn_step(n, cap):
    """Least lambda-growing m <= cap from n, else None."""
    lam = lam_int(n)
    for m in range(2, cap + 1):
        if lam_int(n * m) > lam:
            return m
    return None

def greedy_tra_step(n, cap):
    """Least transparent m <= cap from n, else None."""
    lam = lam_int(n)
    for m in range(2, cap + 1):
        if lam_int(n * m) == lam:
            return m
    return None

def s6():
    print("S6 fate is invisible from inside")
    # the worked witness: N = 96
    ok(crystal_step(32) == 3 and 32 * 3 == 96, "S6 D-IND witness")
    ok(greedy_dyn_step(48, 100) == 2, "S6 D-DYN witness")
    ok(greedy_tra_step(32, 100) == 3, "S6 D-TRA witness")
    # scan: states below 500 reachable by >= 2 distinct laws
    multi = 0
    for n in range(4, 501):
        laws = set()
        for s in divisors(n):
            if s == n or s < 2:
                continue
            m_target = n // s
            if crystal_step(s) * s == n:
                laws.add("IND")
            if greedy_dyn_step(s, m_target) == m_target:
                laws.add("DYN")
            if greedy_tra_step(s, m_target) == m_target:
                laws.add("TRA")
        if len(laws) >= 2:
            multi += 1
    ok(multi >= 10, f"S6 only {multi} multi-law states")
    print(f"  N = 96: D-IND (from 32), D-DYN (from 48), D-TRA "
          f"(from 32) all pass through it; {multi} states below 500 "
          f"are one-step-reachable under >= 2 distinct laws")

# ---------------------------------------------------------------- S7
# THE ANTHROPIC WEIGHT: conditioning on the blueprint reweights any
# temperature prior by exactly 1/zeta(beta); expected defect count
# is the prime zeta function.

def s7():
    print("S7 the anthropic weight")
    grid = [1.1 + 0.1 * i for i in range(30)]
    zs = [zeta_mid(b, M=200000) for b in grid]
    post = [1 / z for z in zs]
    t = sum(post)
    post = [x / t for x in post]
    ok(abs(sum(post) - 1) < 1e-12, "S7 normalization")
    for a, b in zip(post, post[1:]):
        ok(b > a, "S7 posterior not increasing in beta")
    # medians (1e-12 tolerance: 15 * (1/30) sums to just under 0.5
    # in floats, which would slip the uniform median a grid point)
    def median(ws):
        acc = 0.0
        for i, w in enumerate(ws):
            acc += w
            if acc >= 0.5 - 1e-12:
                return grid[i]
    prior_med = median([1 / 30] * 30)
    post_med = median(post)
    bf = zs[0] / zs[-1]
    print(f"  uniform prior on beta in [1.1, 4.0]: median "
          f"{prior_med:.1f} -> {post_med:.1f} given a squarefree "
          f"world; the largest Bayes factor on the grid is "
          f"zeta(1.1)/zeta(4.0) = {bf:.2f} -- the anthropic case for "
          f"coldness is zeta-capped")
    ok(bf < 12, "S7 cap sanity")
    # expected defects = prime zeta
    for beta in (1.5, 2.0, 3.0):
        part = sum(p ** -beta for p in PRIMES_1E5)
        tail = 100000 ** (1 - beta) / (beta - 1)
        print(f"  beta={beta}: expected defective columns = prime "
              f"zeta = {part:.4f} (+ tail < {tail:.2e}) -- finitely "
              f"many defects a.s. (Borel-Cantelli)")
        ok(tail < 0.01, f"S7 tail beta={beta}")

# ---------------------------------------------------------------- run

if __name__ == "__main__":
    import time
    t0 = time.time()
    s0()
    s1()
    s2()
    s3()
    s4()
    s5()
    s6()
    s7()
    print(f"ALL SECTIONS PASS -- {CHECKS} checks, "
          f"{time.time() - t0:.1f} s")
