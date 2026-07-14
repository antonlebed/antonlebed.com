"""
explore_thermal_growth.py — thermal growth (sibling of
explore_growth_laws.py, explore_growth_capability.py,
explore_size_crystallization.py, explore_lock_prime.py).

THE QUESTION. Every growth law in the companion scripts above is a
ZERO-TEMPERATURE object: the greedy takes the minimal admissible m. This
script softens the selection into THE THERMAL LAW at inverse temperature
beta — from state N, pick admissible m >= 2 with probability proportional
to m^(-beta) (normalizable for beta > 1; beta -> infinity recovers the
greedy). Demands unchanged: D-IND (coprime), D-DYN (lambda-growing),
D-TRA (transparent). Which parts of each fate survive temperature,
and what are the hot limits?

FINDINGS (run record below; all sections assert).

1. ENTRY-ONCE (rule, proved; asserted as a trajectory invariant over
   all MC picks). Under thermal D-IND a prime is touched by at most
   one pick: once p | N every later move is coprime to N. So the
   limit supernatural number factorizes over picks, each prime's
   depth fixed at its entry.

2. THE GEOMETRIC DEPTH LAW (rule, proved; verified by exact
   enumeration at beta = 1.25, 1.5, 2, 3 and by MC). Conditional on
   prime p entering at a pick (p | m, gcd(m, N) = 1, any past), write
   m = p^k c with c coprime to Np: the weight p^(-k beta) c^(-beta)
   factorizes and the cofactor range is identical for every k >= 1,
   so P(v_p = k) = p^(-beta(k-1)) (1 - p^(-beta)) EXACTLY — geometric
   with ratio p^(-beta), independent of when and how p enters, and
   (same factorization, applied per pick to the activated set)
   independent ACROSS primes. THE ZETA MEASURE: the hot-breadth limit
   object is the random supernatural number prod_p p^(G_p) with G_p
   independent and geometric — per-prime, exactly the v_p-law of a
   zeta(beta)-random integer conditioned on p | n. Enumeration check:
   m <= 200000, 6 (state, prime) cases x 4 betas, k = 1..4, within
   the rigorous truncation tolerance (reported per beta in the run
   output; tight at beta >= 1.5, honest-but-loose at 1.25).
   Cross-prime independence asserted in MC: the joint depth-1
   fraction of 2 and 3 equals the product of the measured marginals
   (within +-0.05).

3. THE CRYSTAL PROBABILITY (rule, proved; verified at beta = 1.5, 2,
   3). P(the hot limit is squarefree — the primorial-crystal profile)
   = prod_p P(G_p = 1) = prod_p (1 - p^(-beta)) = 1/zeta(beta): the
   Riemann zeta function is the thermal tower's PARTITION FUNCTION,
   and 1/zeta(beta) is the fraction of temperature-beta worlds that
   grow the exact blueprint (0.608 at beta = 2 — the classical
   squarefree density, reappearing as a crystal fraction). Verified:
   Euler product over p <= 2e5 vs direct-sum zeta with integral
   bracket, both sides independent.

4. HOT HEALING (rule, proved; engine verified in S7, dynamics in S3).
   For p not dividing N the single move m = p is admissible, so
   P(p | pick) >= p^(-beta)/(zeta(beta) - 1) > 0 uniformly in N
   (verified by enumeration at 4 states x missing primes <= 13);
   Levy's Borel-Cantelli then forces every prime in a.s.: the breadth
   DESTINATION (window set -> all primes) is TEMPERATURE-INVARIANT at
   every beta > 1. MC: 1500 trajectories x 60 steps at beta = 2, 100%
   absorb the first 5 primes. What melts is the profile around the
   destination: squarefree-ness survives only with probability
   1/zeta(beta) (finding 3), and the ROUTE melts — P(first pick is a
   2-power) = 0.517 at beta = 2 (exact closed form in the truncated
   model; MC 0.495), so the increasing route is no longer forced from
   the first move; P(route prefix = 2, 3, 5) = 0.120 (exact; MC
   0.120). The route distribution interpolates the archimedean
   author's single itinerary (beta = infinity) toward a spread over
   all enumerations.

5. THE HAAR EDGE (rule — the depth law's limit; formula asserted in
   the S1 harness at all four betas). P(G_p >= k) = p^(-beta(k-1)).
   As beta -> 1+ this converges to p^(-(k-1)): per coordinate, Haar
   measure on Z_p conditioned on p | x (a probability-1/p event),
   jointly independent — the COORDINATE-WISE full-support
   conditioning of Haar on Z-hat = prod Z_p (the global full-support
   event is Haar-null; the product conditioning is the canonical
   reading). beta = 1 is
   simultaneously zeta's pole and the law's normalizability edge. The
   thermal family therefore runs from THE CRYSTAL (beta = infinity:
   the primorial tower, all depths 1) to THE HAAR SHADOW (beta -> 1+:
   the uniform profinite profile); the tower is the ground state of a
   Gibbs family whose partition function is zeta and whose hot edge
   is Haar measure's.

6. THE LOCK MELTS (rule for the mechanism, proved; measured for the
   census). At T = 0 the lock held because the locked door q is the
   strict minimum forever (explore_lock_prime.py). At any finite beta a rival blocked
   opening r with (r-1) | lambda costs r^(v_r(lambda)+2) — CONSTANT
   in t while v_r(lambda) is constant — so its per-step probability
   is bounded below and it fires a.s. (conditional Borel-Cantelli;
   constancy hypothesis explicit). Exact deviation line along the
   pure 2-column (states 2^a, a = 3..30, menu enumerated exactly):
   P(pick outside the column) in [0.312, 0.374] at beta = 2 — the
   deviation sum grows linearly in range. MC from seed 2 (the T = 0
   2-adic lock, re-derived in-harness as contrast): 100/100 hot runs
   open a second window within 40 steps; windows-after-40 histogram
   mode 5-6, max 11 — hot dynamics opens windows steadily (measured;
   no unbounded claim). The single-column depth fate is a
   ZERO-TEMPERATURE PHENOMENON: the recurrence invariant survives
   heat, but the argmin that made it absorbing does not.

7. MORTALITY IS THERMALLY INERT (rule, proved; verified 200 runs x 3
   seeds). D-TRA's state space is the divisor lattice of
   W(lambda(seed)) ({n : lambda(n) | L} is lcm-closed with maximum W,
   so every member divides W); from any N < W every prime p | W/N is
   admissible (lambda(Np) = L forced), every admissible move keeps
   N | W, and every move consumes >= 1 prime factor (with
   multiplicity) of W/N — so EVERY trajectory, at ANY temperature,
   absorbs at exactly W within Omega(W/seed) moves (a deterministic
   bound, stronger than a.s.). Verified: seeds
   5, 7, 73 absorb at 240, 504, 20174525280 in every run; seed 2 is
   its own wall (W(1) = 2, zero admissible moves). Same tombstones as
   explore_growth_laws.py's table (cross-asserted, L <= 12 and 72).

8. THE MELTING ASYMMETRY (the synthesis). Temperature grades the
   blueprint by how much of the SELECTION each property needs. The
   mortality wall needs none: it holds for EVERY admissible
   trajectory (sure, selection-independent). The breadth destination
   needs only FULL SUPPORT: healing is a.s. at every beta (the entry
   bound keeps every missing prime's door at uniformly positive
   mass; starving routes — e.g. odd prime squares forever — exist in
   the support but carry probability zero, so the destination is a.s.
   yet never sure). The route, the depth-1 profile (squarefree-ness),
   the lock, and the wander bound needed the ARGMIN itself — and melt
   at any finite beta. explore_size_crystallization.py split free growth's
   authorship into demand vs selection; this script makes the split physical
   AND graded: demand-authored structure survives every selection,
   full-support-purchasable structure survives every temperature
   (the thermal analog of explore_size_crystallization.py's properness), and what only the
   argmin enforced is exactly the thermal part. Windows write the
   invariants; the softened deleted place writes a MEASURE over
   itineraries, with zeta as its partition function. The three fates
   reorganize under heat: breadth stays breadth (its limit thickening
   from the crystal toward the Haar shadow as beta -> 1), depth's
   column shatters into ever-more windows, mortality dies at the same
   wall on a random climb.

HONEST SCOPE. Multiplicative thermal laws over Z/N at beta > 1, the
ambient of explore_growth_laws.py; MC sections run truncated models
(D-IND universe = primes <= 300; D-DYN menu m <= 1000) whose in-universe
per-prime marginals are exact — the proofs (findings 1-5, 6-mechanism, 7) are
for the full law; the hot D-DYN limit object is NOT claimed here (the
measured window growth is 40-step scope; whether every window opens
a.s. and deepens without bound — candidate limit Z-hat itself — was
left open: v_r(lambda) can grow spontaneously and freeze doors, the
same delicacy as explore_lock_prime.py's ghost-ladder question. ANSWERED
by explore_hot_limit.py: the admissible set is upward-closed, the
door-freeze prices only minimal moves, and hot D-DYN reaches Z-hat
a.s. at every seed and every beta > 1). Additive moves and
non-cyclic ambients remain open. beta <= 1 is not a
law (zeta's pole); the Haar-edge statement is a limit of laws, never
a law at 1.

PREDICTIONS (fixed before any code was written). Adjudication:
  PR1 entry-once ........ CONFIRMED (S3 invariant, every MC pick)
  PR2 geometric depths .. CONFIRMED (S1 exact at 4 betas; S3 MC bands)
  PR3 crystal 1/zeta .... CONFIRMED (S2 both sides; S3 fraction 0.642
                          vs 5-prime product 0.622, band +-0.055)
  PR4 hot healing ....... CONFIRMED (S3: 100% >= the frozen 99%)
  PR5 route melt ........ CONFIRMED (P(first != 2-power) = 0.483 >
                          1/4; prefix235 MC 0.120 == exact 0.120)
  PR6 lock melt ......... CONFIRMED (S4 line >= 0.10 everywhere — the
                          hand estimate ~0.16 was an UNDERESTIMATE,
                          measured 0.31-0.374: composite deviating
                          moves the hand sum ignored; S5 100/100 >=
                          the frozen 50%)
  PR7 mortality inert ... CONFIRMED (S6: every run, exact walls,
                          within the Omega bound)
  PR8 Haar edge ......... CONFIRMED (S1 formula asserts at beta =
                          1.25, 1.5, 2, 3; the limit is algebra)

RUN RECORD (python explore_thermal_growth.py, ~4 s, trivial memory):
  S0 lambda cross-check: 299 moduli n <= 300, factored lambda == the
     exponent of U(n) from raw element orders
  S1 depth law: 6 (state, prime) cases x 4 betas x k = 1..4,
     enumeration to 2e5, geometric within rigorous tolerance
  S2 crystal: Euler product (p <= 2e5) == 1/zeta (direct sum +
     integral bracket) at beta = 1.5, 2, 3
  S3 thermal D-IND beta = 2: 1500 x 60 steps; healing 1.000; depth
     P(2: k=1) 0.763, P(2: k=2) 0.183, P(3: k=1) 0.892 vs laws
     0.750, 0.1875, 0.889; crystal 0.642 vs 0.622; joint(2,3)
     depth-1 == marginal product (+-0.05); route 2-power 0.495 vs
     exact 0.517, prefix (2,3,5) 0.120 vs exact 0.120
  S4 exact deviation line: 2^a, a = 3..30, P(deviate) in
     [0.312, 0.374], sum 8.80
  S5 thermal D-DYN beta = 2, seed 2: T=0 greedy contrast single-
     column; 100/100 hot runs open a 2nd window <= 40 steps;
     histogram {3:2, 4:11, 5:30, 6:27, 7:19, 8:8, 9:2, 11:1}
  S6 thermal D-TRA: seeds 5, 7, 73 x 200 runs -> absorb at 240, 504,
     20174525280, within Omega(W/seed); wall table re-asserted
     (L = 2..12, 72); seed 2 = its own wall
  S7 entry bound: 4 states x missing primes <= 13, enumerated to 2e5
  TOTAL 99,536 checks, exit 0.
"""

import math
import random
from math import gcd

# ---------------------------------------------------------------- helpers

def sieve(n):
    bs = bytearray([1]) * (n + 1)
    bs[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if bs[i]:
            bs[i * i :: i] = bytearray(len(bs[i * i :: i]))
    return [i for i in range(2, n + 1) if bs[i]]

PRIMES_2E5 = sieve(200000)
PRIMES_SMALL = [p for p in PRIMES_2E5 if p <= 1000]

_factor_cache = {}

def factorize(n):
    """n -> dict {p: e}, cached."""
    if n in _factor_cache:
        return dict(_factor_cache[n])
    m, out = n, {}
    d = 2
    while d * d <= m:
        while m % d == 0:
            out[d] = out.get(d, 0) + 1
            m //= d
        d += 1
    if m > 1:
        out[m] = out.get(m, 0) + 1
    _factor_cache[n] = dict(out)
    return out

def lcm_d(a, b):
    out = dict(a)
    for p, e in b.items():
        if out.get(p, 0) < e:
            out[p] = e
    return out

def divides_d(a, b):
    return all(b.get(p, 0) >= e for p, e in a.items())

def lam_pp(p, e):
    """lambda(p^e) as a factorization dict."""
    if e == 0:
        return {}
    if p == 2:
        if e == 1:
            return {}
        if e == 2:
            return {2: 1}
        return {2: e - 2}
    d = factorize(p - 1)
    if e > 1:
        d[p] = d.get(p, 0) + e - 1
    return d

def lam_of(nd):
    """lambda of a factored modulus (dict) as a dict."""
    out = {}
    for p, e in nd.items():
        out = lcm_d(out, lam_pp(p, e))
    return out

def dict_to_int(d):
    n = 1
    for p, e in d.items():
        n *= p ** e
    return n

def zeta_bracket(beta, M=200000):
    """(lower, upper) bracket for zeta(beta) via direct sum + integral tail."""
    s = sum(n ** -beta for n in range(1, M + 1))
    lo = s + (M + 1) ** (1 - beta) / (beta - 1)
    hi = s + M ** (1 - beta) / (beta - 1)
    return lo, hi

CHECKS = 0

def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1

# ---------------------------------------------------------------- S0
# lambda cross-check: factored-form lambda vs the exponent of U(n)
# computed raw from element orders (the shared formula verified outside
# itself; the same pattern used in explore_lock_prime.py's S0 section).

def brute_exponent(n):
    exp = 1
    for a in range(1, n):
        if gcd(a, n) == 1:
            o, x = 1, a % n
            while x != 1:
                x = x * a % n
                o += 1
            exp = exp * o // gcd(exp, o)
    return exp

def s0():
    for n in range(2, 301):
        lam = dict_to_int(lam_of(factorize(n)))
        ok(lam == brute_exponent(n), f"S0 lambda mismatch at n={n}")
    print(f"S0 lambda cross-check: 299 moduli, factored lambda == U(n) exponent")

# ---------------------------------------------------------------- S1
# THE GEOMETRIC DEPTH LAW, exact enumeration. Conditional on prime p
# entering at a pick from state N (p | m, gcd(m, N) = 1), the depth law
# P(v_p = k) = p^(-beta(k-1)) (1 - p^(-beta)) — exactly, for every
# state and prime. Enumerate m <= CAP, weights m^-beta; tolerance =
# rigorous truncation bound (per beta), reported.

def s1():
    CAP = 200000
    cases = [(1, 2), (1, 3), (30, 7), (30, 11), (56, 3), (56, 11)]
    betas = [1.25, 1.5, 2.0, 3.0]
    for beta in betas:
        tail = CAP ** (1 - beta) / (beta - 1)
        for (N, p) in cases:
            w = {}
            for m in range(2, CAP + 1):
                if m % p or gcd(m, N) > 1:
                    continue
                k, t = 0, m
                while t % p == 0:
                    t //= p
                    k += 1
                w[k] = w.get(k, 0.0) + m ** -beta
            mass = sum(w.values())
            tol = 3 * tail / mass
            r = p ** -beta
            for k in range(1, 5):
                emp = w.get(k, 0.0) / mass
                law = r ** (k - 1) * (1 - r)
                ok(abs(emp - law) <= max(tol, 1e-12),
                   f"S1 depth law N={N} p={p} beta={beta} k={k}: "
                   f"{emp:.6f} vs {law:.6f} tol {tol:.2e}")
        print(f"S1 depth law beta={beta}: {len(cases)} (state, prime) cases, "
              f"k=1..4 exact-geometric within rigorous tol "
              f"{3 * tail:.2e}/mass")

# ---------------------------------------------------------------- S2
# THE CRYSTAL PROBABILITY: prod_p (1 - p^-beta) = 1/zeta(beta), both
# sides computed independently (Euler product over primes <= 2e5 vs
# direct-sum zeta with integral bracket).

def s2():
    for beta in (1.5, 2.0, 3.0):
        lo, hi = zeta_bracket(beta)
        prod = 1.0
        for p in PRIMES_2E5:
            prod *= 1 - p ** -beta
        # product excludes primes > 2e5: log-defect <= sum_{n>2e5} n^-beta
        defect = 200000 ** (1 - beta) / (beta - 1)
        mid = 2 / (lo + hi)
        ok(abs(prod - mid) <= 3 * (defect + (hi - lo)),
           f"S2 crystal prob beta={beta}: {prod:.8f} vs 1/zeta {mid:.8f}")
        print(f"S2 crystal probability beta={beta}: Euler product "
              f"{prod:.6f} == 1/zeta {mid:.6f} (defect bound {defect:.1e})")

# ---------------------------------------------------------------- S3
# THERMAL D-IND, Monte Carlo. Exact sampler for the truncated model:
# universe = primes <= 300; the coprime-restricted zeta law factorizes
# as independent per-prime geometrics conditioned on m >= 2 (sampled
# via the first-active-prime inverse CDF — no rejection). Checks:
# entry-once invariant, hot healing, depth histograms vs the geometric
# law, the crystal fraction, the route melt.

UNIVERSE = [p for p in PRIMES_SMALL if p <= 300]

def sample_move_ind(nd, beta, rng):
    """One thermal D-IND pick from factored state nd. Returns dict move."""
    avail = [p for p in UNIVERSE if p not in nd]
    if not avail:
        return None
    a = [p ** -beta for p in avail]
    # P(all inactive) among available primes
    q = [1 - x for x in a]
    # first-active inverse CDF
    tot_none = 1.0
    for x in q:
        tot_none *= x
    z = 1 - tot_none  # P(m >= 2) in truncated model
    u = rng.random() * z
    move = {}
    pref = 1.0
    first = None
    for i, p in enumerate(avail):
        w = pref * a[i]  # P(first active = p)
        if u < w:
            first = i
            break
        u -= w
        pref *= q[i]
    if first is None:  # float corner: force last available
        first = len(avail) - 1
    # depth of the first-active prime: P(v=k | v>=1) = r^(k-1)(1-r)
    def depth(p):
        r = p ** -beta
        uu = rng.random()
        k = 1
        while uu < r:
            uu /= r
            k += 1
        return k
    move[avail[first]] = depth(avail[first])
    for p in avail[first + 1 :]:
        if rng.random() < p ** -beta:
            move[p] = depth(p)
    return move

def s3():
    beta = 2.0
    rng = random.Random(147)
    NTRAJ, NSTEP = 1500, 60
    tracked = [2, 3, 5, 7, 11]
    entry_depth = {p: [] for p in tracked}
    absorbed5 = 0
    crystal5 = 0
    joint11 = 0
    first_pick_2power = 0
    prefix_235 = 0
    for _ in range(NTRAJ):
        nd = {}
        seen_at = {}
        picks = []
        for step in range(NSTEP):
            mv = sample_move_ind(nd, beta, rng)
            if mv is None:  # universe exhausted (truncated model)
                break
            picks.append(mv)
            for p, k in mv.items():
                ok(p not in nd, "S3 entry-once violated")
                nd[p] = k
                if p in tracked and p not in seen_at:
                    seen_at[p] = step
                    entry_depth[p].append(k)
        if all(p in nd for p in tracked):
            absorbed5 += 1
            if all(nd[p] == 1 for p in tracked):
                crystal5 += 1
        if nd.get(2) == 1 and nd.get(3) == 1:
            joint11 += 1
        if list(picks[0].keys()) == [2]:
            first_pick_2power += 1
            if len(picks) >= 3 and list(picks[1].keys()) == [3] and \
               list(picks[2].keys()) == [5]:
                prefix_235 += 1
    # healing
    frac = absorbed5 / NTRAJ
    ok(frac >= 0.99, f"S3 healing: only {frac:.3f} absorbed first 5 primes")
    # depth histograms vs the geometric law
    for p, want1 in ((2, 0.75), (3, 8 / 9)):
        d = entry_depth[p]
        f1 = sum(1 for k in d if k == 1) / len(d)
        ok(abs(f1 - want1) <= 0.055,
           f"S3 depth p={p}: P(k=1) {f1:.4f} vs {want1:.4f}")
    d2 = entry_depth[2]
    f2 = sum(1 for k in d2 if k == 2) / len(d2)
    ok(abs(f2 - 0.1875) <= 0.05, f"S3 depth p=2 k=2: {f2:.4f} vs 0.1875")
    # crystal fraction over the tracked primes
    want = 1.0
    for p in tracked:
        want *= 1 - p ** -beta
    fc = crystal5 / max(absorbed5, 1)
    ok(abs(fc - want) <= 0.055,
       f"S3 crystal fraction {fc:.4f} vs product {want:.4f}")
    # cross-prime independence: joint == product of measured marginals
    f1_2 = sum(1 for k in entry_depth[2] if k == 1) / len(entry_depth[2])
    f1_3 = sum(1 for k in entry_depth[3] if k == 1) / len(entry_depth[3])
    fj = joint11 / NTRAJ
    ok(abs(fj - f1_2 * f1_3) <= 0.05,
       f"S3 independence: joint {fj:.4f} vs marginals product "
       f"{f1_2 * f1_3:.4f}")
    # route melt: closed forms inside the truncated model
    Zu_none = 1.0
    for p in UNIVERSE:
        Zu_none *= 1 - p ** -beta
    z = 1 - Zu_none
    # P(only 2 active) = P(v_2 >= 1) * prod_{p != 2}(1 - a_p)
    #                  = a2 * Zu_none / (1 - a2)   [a_p = p^-beta]
    p2power = 2 ** -beta * Zu_none / (1 - 2 ** -beta)
    p2power_cond = p2power / z
    f2p = first_pick_2power / NTRAJ
    sd = math.sqrt(p2power_cond * (1 - p2power_cond) / NTRAJ)
    ok(abs(f2p - p2power_cond) <= 4 * sd + 0.01,
       f"S3 route: P(first pick 2-power) {f2p:.4f} vs {p2power_cond:.4f}")
    ok(1 - p2power_cond > 0.25, "S3 route: P(first != 2-power) <= 1/4")
    # P(prefix 2,3,5): product of three conditional only-p-active probs
    def only_p(pp, missing):
        a, none = pp ** -beta, 1.0
        for p in missing:
            none *= 1 - p ** -beta
        return (a * none / (1 - a)) / (1 - none)
    m0 = UNIVERSE[:]
    pr = only_p(2, m0)
    m1 = [p for p in m0 if p != 2]
    pr *= only_p(3, m1)
    m2 = [p for p in m1 if p != 3]
    pr *= only_p(5, m2)
    f235 = prefix_235 / NTRAJ
    sd = math.sqrt(pr * (1 - pr) / NTRAJ)
    ok(abs(f235 - pr) <= 4 * sd + 0.01,
       f"S3 route prefix (2,3,5): {f235:.4f} vs {pr:.4f}")
    d3 = entry_depth[3]
    print(f"S3 thermal D-IND beta=2, {NTRAJ} x {NSTEP} steps: healing "
          f"{frac:.3f}; depth P(2:k=1) {sum(1 for k in d2 if k==1)/len(d2):.3f}"
          f" (law 0.750), P(2:k=2) {f2:.3f} (law 0.1875), P(3:k=1) "
          f"{sum(1 for k in d3 if k==1)/len(d3):.3f} (law 0.889); crystal "
          f"{fc:.3f} (law {want:.3f}); route 2-power {f2p:.3f} "
          f"(exact {p2power_cond:.3f}), prefix235 {f235:.3f} (exact {pr:.3f})")

# ---------------------------------------------------------------- S4/S5
# THERMAL D-DYN: THE LOCK MELTS. Menu = m <= M_CAP with
# lambda(N m) > lambda(N), weights m^-beta. (a) exact deviation line
# along the 2-column: P(pick not a 2-power) from states 2^a, a=3..30,
# each >= 0.10 (constant rival doors -> the deviation sum grows
# linearly, Borel-Cantelli fires); (b) T=0 contrast: the greedy from
# seed 2 stays single-window (re-derived in-harness from explore_lock_prime.py); (c) MC:
# fraction of hot seed-2 runs opening a second window within 40 steps.

M_CAP = 1000
_move_lam = [None] * (M_CAP + 1)  # per-m list of (q, a) prime powers
for _m in range(2, M_CAP + 1):
    _move_lam[_m] = list(factorize(_m).items())

def lam_grows(nd, lamd, m):
    for q, a in _move_lam[m]:
        if not divides_d(lam_pp(q, nd.get(q, 0) + a), lamd):
            return True
    return False

def menu_dyn(nd, lamd, beta):
    moves, weights = [], []
    for m in range(2, M_CAP + 1):
        if lam_grows(nd, lamd, m):
            moves.append(m)
            weights.append(m ** -beta)
    return moves, weights

def s45():
    beta = 2.0
    # (a) exact deviation line along the 2-column
    devs = []
    for a in range(3, 31):
        nd = {2: a}
        lamd = lam_of(nd)
        moves, weights = menu_dyn(nd, lamd, beta)
        tot = sum(weights)
        dev = sum(w for m, w in zip(moves, weights)
                  if _move_lam[m][0][0] != 2 or len(_move_lam[m]) > 1)
        devs.append(dev / tot)
        ok(dev / tot >= 0.10, f"S4 deviation at 2^{a}: {dev/tot:.4f} < 0.10")
    ok(sum(devs) >= 0.10 * len(devs), "S4 deviation sum too small")
    print(f"S4 exact deviation line 2^a (a=3..30): P(deviate) in "
          f"[{min(devs):.3f}, {max(devs):.3f}], sum {sum(devs):.2f} "
          f"over 28 states (linear growth in range)")
    # (b) T=0 contrast: greedy from seed 2, 40 steps, single window
    nd = {2: 1}
    lamd = lam_of(nd)
    for _ in range(40):
        moves, _w = menu_dyn(nd, lamd, beta)
        m = moves[0]  # least admissible = the greedy
        for q, a2 in _move_lam[m]:
            nd[q] = nd.get(q, 0) + a2
        lamd = lam_of(nd)
    ok(set(nd) == {2}, f"S5 T=0 lock broken: windows {sorted(nd)}")
    # (c) hot MC from seed 2
    rng = random.Random(148)
    NTRAJ, NSTEP = 100, 40
    second = 0
    win_hist = {}
    for _ in range(NTRAJ):
        nd = {2: 1}
        lamd = lam_of(nd)
        opened2 = None
        for step in range(NSTEP):
            moves, weights = menu_dyn(nd, lamd, beta)
            tot = sum(weights)
            u = rng.random() * tot
            for m, w in zip(moves, weights):
                if u < w:
                    break
                u -= w
            for q, a2 in _move_lam[m]:
                if q not in nd and opened2 is None and q != 2:
                    opened2 = (q, step)
                nd[q] = nd.get(q, 0) + a2
            lamd = lam_of(nd)
        if opened2 is not None:
            second += 1
        k = len(nd)
        win_hist[k] = win_hist.get(k, 0) + 1
    ok(second / NTRAJ >= 0.50,
       f"S5 lock melt: only {second}/{NTRAJ} opened a second window")
    print(f"S5 thermal D-DYN beta=2 seed 2, {NTRAJ} x {NSTEP}: T=0 greedy "
          f"stays 2-column; hot runs opening 2nd window {second}/{NTRAJ}; "
          f"windows-after-40 histogram {dict(sorted(win_hist.items()))}")

# ---------------------------------------------------------------- S6
# THERMAL D-TRA: MORTALITY IS THERMALLY INERT. State space = divisors
# of W(lambda(seed)); admissible = m >= 2 with m | W/N; every run — any
# temperature — absorbs at exactly W within Omega(W/seed) steps
# (deterministic bound: every move consumes >= 1 prime factor of W/N).

def wall(L):
    """W(L) = max {n : lambda(n) | L} as a factorization dict."""
    Ld = factorize(L)
    out = {}
    for p in PRIMES_SMALL:
        if L % (p - 1) == 0:
            e = 1
            while divides_d(lam_pp(p, e + 1), Ld):
                e += 1
            out[p] = e
        if p > L + 1:
            break
    return out

def divisors_of(d):
    out = [1]
    for p, e in d.items():
        out = [x * p ** i for x in out for i in range(e + 1)]
    return out

def s6():
    # wall table cross-check (explore_growth_laws.py)
    table = {2: 24, 4: 240, 6: 504, 8: 480, 10: 264, 12: 65520, 72: 20174525280}
    for L, w in table.items():
        ok(dict_to_int(wall(L)) == w, f"S6 wall W({L}) != {w}")
    beta = 2.0
    rng = random.Random(149)
    for seed in (5, 7, 73):
        L = brute_exponent(seed)
        Wd = wall(L)
        W = dict_to_int(Wd)
        cof = W // seed
        omega_bound = sum(factorize(cof).values())
        for _ in range(200):
            N = seed
            steps = 0
            while True:
                rem = W // N
                cand = [m for m in divisors_of(factorize(rem)) if m >= 2]
                if not cand:
                    break
                weights = [m ** -beta for m in cand]
                tot = sum(weights)
                u = rng.random() * tot
                for m, w in zip(cand, weights):
                    if u < w:
                        break
                    u -= w
                N *= m
                steps += 1
                ok(W % N == 0, "S6 left the divisor lattice")
                ok(steps <= omega_bound, "S6 exceeded the Omega bound")
            ok(N == W, f"S6 absorbed at {N} != W {W}")
        print(f"S6 thermal D-TRA seed {seed}: 200 runs all absorb at "
              f"W({L}) = {W} within {omega_bound} moves")
    # seed 2: W(lambda(2)) = W(1) = 2 — born on the wall, no moves
    ok(dict_to_int(wall(1)) == 2, "S6 W(1) != 2")
    print("S6 seed 2 is its own wall (W(1) = 2): zero admissible moves")

# ---------------------------------------------------------------- S7
# THE ENTRY BOUND (hot healing's engine): for p not dividing N,
# P(p | pick) >= p^-beta / (zeta(beta) - 1), verified by enumeration.

def s7():
    beta, CAP = 2.0, 200000
    lo, hi = zeta_bracket(beta)
    bound_denom = hi - 1
    for N in (1, 30, 210, 2310):
        for p in (2, 3, 5, 7, 11, 13):
            if N % p == 0:
                continue
            wp = tot = 0.0
            for m in range(2, CAP + 1):
                if gcd(m, N) > 1:
                    continue
                w = m ** -beta
                tot += w
                if m % p == 0:
                    wp += w
            ok(wp / tot >= p ** -beta / bound_denom,
               f"S7 entry bound fails N={N} p={p}")
    print(f"S7 entry bound: P(p | pick) >= p^-beta/(zeta-1) at 4 states "
          f"x missing primes (enumerated to {CAP})")

# ---------------------------------------------------------------- main

if __name__ == "__main__":
    import time
    t0 = time.time()
    s0()
    s1()
    s2()
    s3()
    s45()
    s6()
    s7()
    print(f"TOTAL {CHECKS} checks, {time.time() - t0:.1f} s, exit 0")
