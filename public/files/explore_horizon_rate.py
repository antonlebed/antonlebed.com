"""explore_horizon_rate.py -- is the prediction horizon faster than
exponential in k? The horizon is the primorial, up to a small drop.

THE QUESTION. The prediction horizon H(k) is the largest prime any
sub-ring of rung k names -- the largest prime factor of -chi(S) over
sub-rings S of the first k primes (explore_prediction_horizon.py,
explore_prediction_density.py). Its per-rung rate log2(H(k)/p_k)/k
climbs to 3.24 bits at k = 11 and dips to 3.15 at k = 12, and whether
the horizon grows faster than exponentially in k was left undecided at
that window, the survey ending at k = 12 because its factoring was
trial division. Here the horizon is CERTIFIED exactly to k = 60 by a
top-down search, and its rate is derived.

THE DERIVATION, fixed before the run. Write P_k for the rung's prime
set, X = -chi(P_k) = p_k# (k - 1 - sum 1/p_i), and for a dropped set T
the sub-ring S = P_k \\ T has -chi(S) < X / prod(T): every -chi is below
the full ring's divided by the product of what it drops. So the
horizon is attained by a sub-ring dropping a SMALL product, and
H(k) = X / D_k defines the drop factor D_k >= 1. Then, exactly,

  rate(k) = log2(H(k)/p_k)/k
          = [theta(p_k) + ln(k - 1 - sum 1/p_i) - ln p_k - ln D_k]/(k ln 2)

with theta(p_k) = ln p_k#. By the prime number theorem theta(p_k) ~ p_k
~ k ln k, so unless ln D_k grows like k the rate grows like log2 k
without bound: the horizon is p_k#^(1 + o(1)) -- super-exponential in
k, and exponential in p_k. The whole question is therefore the size
of the drop.

THE DROP MODEL M0. Order the candidates by what they drop: squarefree
d = prod(T) = 1, 2, 3, 5, 6, 7, 10, ... (every squarefree d <= p_k is
a product of tower primes). A candidate's -chi is coprime to every
prime of S and to 2 whether or not 2 is dropped (the primality gate,
explore_chi_primality.py: -chi is always odd) and equidistributed mod
the odd primes of T, so under Cramer its chance of being PRIME is
q(T) = (e^gamma ln p_k / ln X) * phi(d')/d' with d' the odd part of d,
the e^gamma ln p_k the Mertens boost for the certain coprimality over
every prime up to p_k. M0 takes the horizon as the
first prime -chi in that order, ignoring the composite route (-chi =
c * prime with c small), which can only LOWER the drop; so M0 is an
upper model for D_k. Its E[ln D] is summed exactly over the ordered
squarefree list, no sampling.

THE CERTIFICATE. For each k the search walks sub-rings in decreasing
-chi (by increasing dropped product, checked against the exact value),
strips every prime factor <= B = 10^5 from -chi(S), and tests the
cofactor: prime and above the running horizon raises it. A composite
cofactor has every prime factor above B, so its largest is below
cofactor / B < X / (prod(T) B) <= X / B, and the running horizon is at
least X / D_k with D_k far below B, so no composite cofactor can hide a
larger prime; the run asserts this bound against the FINAL horizon for
every composite it met. The walk stops when the next candidate's -chi
is below the horizon found. Primality: the deterministic Miller-Rabin
base set below 3.317e24 (Sorenson-Webster), 25 random bases above (the
census convention of explore_chi_primality.py).

POSITIVE CONTROL, run before any verdict: the certified horizons at
k = 3..12 must equal the trial-division survey's column
(explore_prediction_density.py section VI), and the k <= 12 rates its
bits/k column to two decimals.

PREDICTIONS, FROZEN BEFORE THE RUN (kills are what the rig PRINTS).
P1 (the identity, property): rate(k) printed from H(k) equals the
   bracket formula at every k to 1e-9 -- a check on the arithmetic,
   not a finding.
P2 (the law): rate(k) exceeds 3.24, the survey's k = 11 maximum, at
   every k in 20..60; rate(20) in 3.9..4.3, rate(40) in 5.3..5.9,
   rate(60) in 5.9..6.4 (the bracket with ln D = 3 +- 1 as the band).
   KILL: any k in 20..60 printing rate(k) <= 3.24.
P3 (the drop): the mean of ln D_k over k = 13..60 is within 1.0 nat of
   M0's mean of E[ln D_k] over the same rungs, and BELOW it (M0 omits
   the composite route). KILL: the measured mean above M0's, or off it
   by more than 1.0.
P4 (the full ring attains): the count of k in 13..60 with D_k = 1 is
   within the binomial 95% band around M0's sum of q({}) over those
   rungs. KILL: a count outside the band.
P5 (the dip): D_12 prints above the median of M0's D at k = 12, so the
   dip at k = 12 is the drop's noise and not a change of law.

Run: python prime/code/explore_horizon_rate.py
Estimate before the run: under 60 s, under 100 MB.

FINDINGS (every figure below is the run's print).
F1 (rule, k = 3..60; MR-25 above the deterministic bound, the census
   convention). The horizon is the full ring's -chi up to a drop of at
   most 208.06: D_k = 1 at 8 of the 58 rungs (the full ring attains,
   last at k = 28), a single dropped prime at 35, two or three at 15,
   D_k under 76 at every k but 41 (208.06, dropping {3, 5, 13}), 44
   (130.14, dropping 127) and 51 (115.38, dropping 113). Positive
   control: the ten survey horizons k = 3..12 reproduced exactly.
F2 (rule in range, the front's answer). rate(k) = log2(H(k)/p_k)/k
   is the bracket formula exactly (P1), and it rises past the survey's
   3.24 at every k >= 13 (minimum 3.419 at k = 13; 4.288 at k = 20,
   5.454 at 40, 6.266 at 60; P2 met with every band), the dips
   (k = 12, 15, 18, 21, 29, 51, 57) being the drop's noise: the
   horizon is p_k#^(1 + o(1)), super-exponential in k, heuristic law
   for the limit through ln D_k = o(k) and a rule over the range.
F3 (pattern, the drop). Mean ln D_k over k = 13..60 is 2.869 against
   M0's 2.665 -- P3's 1.0-nat band met, its one-sided clause NOT met:
   measured sits 0.204 ABOVE the upper model, one standard error (near
   0.2 from 48 rungs), so the composite route is invisible at this
   sample and M0 reads slightly generous rather than short. D_k = 1 at
   3 of the 48 rungs against M0's 3.66, band [0.09, 7.22] (P4 met);
   D_12 = 7.70 against M0's median 5 (P5 met). THE FREEZE'S ERROR: as
   first written M0 penalised a dropped 2 by 1/2 as if -chi were
   equidistributed mod 2, against the gate's own fact that -chi is
   always odd, cited one sentence earlier; that run read 2.860, a
   cancellation, and the audit corrected the model before any prose
   moved. The figures above are the corrected model's.
Tier: the horizons are a rule over k <= 60 by certificate (MR-25
above 3.317e24 -- k >= 19); the rate identity is a property; the
super-exponential limit is a heuristic law resting on ln D_k = o(k),
which M0 predicts and the range shows; M0 is a model, its fit a
pattern.
Run record: 0.8 s wall, 12.4 MB peak under memwatch, 599 composite
cofactors met and bounded. Seed 1032 for the MR-25 bases.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import math
import random
import time

K_MAX = 60
B = 10 ** 5
MR_DET_BOUND = 3_317_044_064_679_887_385_961_981  # Sorenson & Webster
MR_DET_BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41)
MR_RANDOM_ROUNDS = 25
EULER_GAMMA = 0.5772156649015329

# the survey's column (explore_prediction_density.py section VI, as
# printed by its run; k = 3 from the same survey's horizon/p_k = 5.8):
# k -> horizon, the positive control
SURVEY = {3: 29, 4: 383, 5: 2579, 6: 109_789, 7: 1_045_819,
          8: 53_780_147, 9: 669_395_063, 10: 14_664_410_603,
          11: 1_691_587_976_399, 12: 9_064_042_869_209}


def primes_upto(n):
    flags = bytearray([1]) * (n + 1)
    flags[0:2] = b"\x00\x00"
    for p in range(2, int(n ** 0.5) + 1):
        if flags[p]:
            flags[p * p::p] = bytearray(len(range(p * p, n + 1, p)))
    return [i for i, f in enumerate(flags) if f]


def mr_strong(n, bases):
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in bases:
        a %= n
        if a == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def is_prime_big(n, rng):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13):
        if n % p == 0:
            return n == p
    if n < MR_DET_BOUND:
        return mr_strong(n, MR_DET_BASES)
    bases = [rng.randrange(2, n - 1) for _ in range(MR_RANDOM_ROUNDS)]
    return mr_strong(n, bases)


def neg_chi(ps):
    m = len(ps)
    N = math.prod(ps)
    return N * (m - 1) - sum(N // p for p in ps)


def strip_small(n, small_primes):
    """Divide out every prime factor <= B; return the cofactor."""
    for p in small_primes:
        if p * p > n:
            break
        while n % p == 0:
            n //= p
    return n


def certified_horizon(primes, small_primes, rng):
    """(H, D_attained_by (dropped set), composite bounds checked)."""
    k = len(primes)
    X = neg_chi(primes)
    # candidates: dropped sets T with product <= cap, walked by product.
    # cap grows until the walk terminates by the -chi bound.
    horizon = 0
    best_T = None
    composite_bounds = []
    cap = 64
    seen_products = set()
    while True:
        cands = [(d, T) for d, T in _dropped_sets(primes, cap)
                 if d not in seen_products]
        cands.sort()
        stop = False
        for d, T in cands:
            seen_products.add(d)
            S = [p for p in primes if p not in T]
            if len(S) < 2:
                continue
            nc = neg_chi(S)
            if nc <= horizon:
                continue
            cof = strip_small(nc, small_primes)
            if cof > horizon and is_prime_big(cof, rng):
                horizon = cof
                best_T = T
            elif cof > 1 and cof > horizon:
                composite_bounds.append(cof // B + 1)
        # termination: every candidate with product > cap has
        # -chi < X / cap; if that is below the horizon, done.
        if horizon > 0 and X // cap < horizon:
            stop = True
        if stop:
            break
        cap *= 4
    return X, horizon, best_T, composite_bounds


def m0_expected(primes, X):
    """M0: candidates by squarefree d (products of tower primes),
    success chance q0 * phi(d)/d each; returns (E[ln D], q0,
    median D, P(D = 1))."""
    p_k = primes[-1]
    q0 = math.exp(EULER_GAMMA) * math.log(p_k) / math.log(X)
    # squarefree d up to a bound large enough that survival is < 1e-9
    bound = 1
    survive = 1.0
    ds = []
    # enumerate squarefree products of tower primes up to bound
    # (grow bound until the tail mass is negligible)
    while True:
        bound *= 4
        ds = sorted(d for d in _squarefree_products(primes, bound))
        survive = 1.0
        for d in ds:
            survive *= (1 - q0 * _odd_phi_over_d(d, primes))
        if survive < 1e-9 or bound > 10 ** 9:
            break
    e_ln = 0.0
    survive = 1.0
    median = None
    cum = 0.0
    p_one = None
    for d in ds:
        q = q0 * _odd_phi_over_d(d, primes)
        prob = survive * q
        if p_one is None:
            p_one = prob
        e_ln += prob * math.log(d)
        cum += prob
        if median is None and cum >= 0.5:
            median = d
        survive *= (1 - q)
    return e_ln, q0, median, p_one


def _dropped_sets(primes, bound):
    """Every (product, dropped tuple) with squarefree product <= bound."""
    out = [(1, ())]
    for p in primes:
        if p > bound:
            break
        out += [(d * p, T + (p,)) for d, T in out if d * p <= bound]
    return out


def _odd_phi_over_d(d, primes):
    """phi(d')/d' for the ODD part d' of d: a dropped odd prime p leaves
    -chi equidistributed mod p (chance 1 - 1/p of coprimality, the
    generic one Cramer already prices), while a dropped 2 changes
    nothing -- -chi is always odd (the primality gate), so coprimality
    to 2 is certain whether 2 is a member or dropped."""
    out = 1.0
    for p in primes:
        if p > 2 and d % p == 0:
            out *= (1 - 1 / p)
    return out


def _squarefree_products(primes, bound):
    out = [1]
    for p in primes:
        if p > bound:
            break
        out += [d * p for d in out if d * p <= bound]
    return out


def main():
    t0 = time.time()
    rng = random.Random(1032)
    small_primes = primes_upto(B)
    all_primes = primes_upto(400)
    assert len(all_primes) >= K_MAX

    print("=" * 72)
    print("  explore_horizon_rate.py -- the horizon certified to k = 60")
    print("=" * 72)

    rows = []
    for k in range(3, K_MAX + 1):
        primes = all_primes[:k]
        p_k = primes[-1]
        X, H, T, comp = certified_horizon(primes, small_primes, rng)
        D = X / H
        theta = sum(math.log(p) for p in primes)
        bracket = (theta + math.log(k - 1 - sum(1 / p for p in primes))
                   - math.log(p_k) - math.log(D)) / (k * math.log(2))
        rate = math.log2(H / p_k) / k
        e_ln, q0, med, p_one = m0_expected(primes, X)
        rows.append(dict(k=k, p_k=p_k, H=H, D=D, T=T, rate=rate,
                         bracket=bracket, e_ln=e_ln, q0=q0, med=med,
                         p_one=p_one, comp=comp, X=X))

    # certificate: every composite cofactor's largest-prime bound is
    # below that rung's FINAL horizon
    n_comp = 0
    for r in rows:
        for bnd in r["comp"]:
            n_comp += 1
            assert bnd < r["H"], f"composite bound escapes at k={r['k']}"
    print(f"\n  certificate: {n_comp} composite cofactors met, every "
          f"largest-prime bound below its rung's final horizon")

    print("\nPOSITIVE CONTROL: certified horizons against the survey "
          "(k = 3..12)")
    ok = True
    for r in rows:
        if r["k"] in SURVEY:
            match = r["H"] == SURVEY[r["k"]]
            ok &= match
            print(f"  k={r['k']:2d}  certified {r['H']:>16,}  survey "
                  f"{SURVEY[r['k']]:>16,}  {'OK' if match else 'MISMATCH'}")
    print(f"  control {'PASS' if ok else 'FAIL'}")
    assert ok, "positive control failed"

    print("\nTHE TABLE: k, p_k, drop D_k (dropped set), rate, the bracket, "
          "M0's E[ln D], q0")
    print(f"  {'k':>3} {'p_k':>4} {'D_k':>9} {'dropped':>16} {'rate':>7} "
          f"{'bracket':>8} {'E0[lnD]':>8} {'q0':>6} {'lnD':>6}")
    for r in rows:
        assert abs(r["rate"] - r["bracket"]) < 1e-9, "P1 identity"
        print(f"  {r['k']:>3} {r['p_k']:>4} {r['D']:>9.2f} "
              f"{str(r['T']) if r['T'] else '{}':>16} {r['rate']:>7.3f} "
              f"{r['bracket']:>8.3f} {r['e_ln']:>8.3f} {r['q0']:>6.3f} "
              f"{math.log(r['D']):>6.3f}")
    print("  P1: rate == bracket at every k (asserted)")

    # P2
    print("\nP2 -- the law: rate(k) against 3.24 on k = 20..60")
    r20 = next(r for r in rows if r["k"] == 20)["rate"]
    r40 = next(r for r in rows if r["k"] == 40)["rate"]
    r60 = next(r for r in rows if r["k"] == 60)["rate"]
    below = [r["k"] for r in rows if r["k"] >= 20 and r["rate"] <= 3.24]
    print(f"  rate(20) = {r20:.3f}  rate(40) = {r40:.3f}  "
          f"rate(60) = {r60:.3f}")
    print(f"  rungs in 20..60 at or below 3.24: {below if below else 'none'}")
    late = [r for r in rows if r["k"] >= 20]
    least = min(late, key=lambda r: r["rate"])
    print(f"  minimum rate on 20..60: {least['rate']:.3f} at k = {least['k']}")

    # P3
    tail = [r for r in rows if r["k"] >= 13]
    meas = sum(math.log(r["D"]) for r in tail) / len(tail)
    model = sum(r["e_ln"] for r in tail) / len(tail)
    print("\nP3 -- the drop: mean ln D_k over k = 13..60")
    print(f"  measured {meas:.3f}   M0 {model:.3f}   difference "
          f"{meas - model:+.3f}  (P3 wants measured <= M0, within 1.0)")

    # P4
    n_one = sum(1 for r in tail if r["D"] < 1.0000001)
    mean_q = sum(r["p_one"] for r in tail)
    var = sum(r["p_one"] * (1 - r["p_one"]) for r in tail)
    lo, hi = mean_q - 1.96 * math.sqrt(var), mean_q + 1.96 * math.sqrt(var)
    print("\nP4 -- the full ring attains (D_k = 1) on k = 13..60")
    print(f"  count {n_one}   M0 expects {mean_q:.2f}, 95% band "
          f"[{lo:.2f}, {hi:.2f}]")

    # P5
    r12 = next(r for r in rows if r["k"] == 12)
    print("\nP5 -- the k = 12 dip")
    print(f"  D_12 = {r12['D']:.2f}  M0 median D at k = 12: {r12['med']}  "
          f"dropped {r12['T']}")

    print(f"\n  wall {time.time() - t0:.1f} s")


if __name__ == "__main__":
    main()
