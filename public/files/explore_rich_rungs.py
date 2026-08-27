"""
Rich rungs: the (p+1)-factorization census + heuristic.

A rung k of the primorial tower gains new seed-flower predictions by
the factorization rule (proved; explore_seed_flower_k8.py):

    new_preds(k) = twin(p_k) + f(p_k),
    f(p) = #{(a,b) : ab = p+1, 2 <= a <= b, a+1 and b+1 prime}

A rung is RICH when f >= 1 (the term's birthplace is
explore_seed_flower_k8.py section IX). The open question: are there
infinitely many rich rungs?

The "smaller tower primes" constraint is INTRINSIC: a >= 2 forces
b+1 <= (p+1)/2 + 1 < p for every p > 3, so q = a+1 and r = b+1 are
automatically primes below p (the scan verifies the lone exclusion
is p = 3 via 4 = 2*2, where b+1 = 3 = p).

Sections:
  I.   Exact small-case settlement: the published k=3..11 prediction
       table and the p=71 / p=29 anchors, re-derived and asserted
  II.  Census over all primes p <= N: rich density per decade,
       multiplicity, champions, the mod-4 obstruction, twin comparison
  III. Conditioned-Cramer heuristic: expected representation count vs
       measured per decade; the divergence shape x*lnln(x)/(ln x)^2

FINDINGS (run at N = 5*10^7, 3,001,134 rungs):
  1. (property) Rich requires p = 3 (mod 4): a+1 and b+1 are odd
     primes, so a and b are both even and 4 | p+1. Verified: all
     599,875 rich rungs in the scan are 3 mod 4.
  2. (rule, p <= 5*10^7) 599,875 rich rungs (19.99% of all rungs,
     40.0% of the p = 3 mod 4 class); 1,158,530 representations.
     Density per decade falls only logarithmically: 25.2% (10^4) ->
     19.7% (10^7..5*10^7) -- a slow log decay, not a die-out.
  3. (observation) Mean multiplicity is SCALE-INVARIANT: f per rich
     rung = 1.93-1.94 in every decade from 10^4 to the horizon
     (explore_rich_rung_constants.py: the independence model's own
     number to 0.4%, drifting down about 0.005 per decade).
     Champion f = 33 at p = 45,239,039 (p+1 = 2^8 * 3^3 * 5*7*11*17);
     highly composite p+1 keeps paying.
  4. (observation) Rich rungs OUTNUMBER twin rungs 2.51x at the
     horizon and the ratio GROWS (1.85 at 10^3, 2.55 in the last
     decade) -- the factorization term, not the twin term, dominates
     the seed-flower's long-run prediction supply.
  5. (heuristic) Conditioned-Cramer expectation (primality of
     ab - 1 modeled at 1/ln n conditioned on coprimality to primes
     <= 100, exact divisibility computed per pair) tracks the
     measured representation count at ratio 0.994-1.013 in every
     decade past 10^3 (1.000 at the horizon). The shape constant
     C = reps(x) * (ln x)^2 / (x * lnln x) holds at 2.53-2.58 across
     five decades (explore_rich_rung_constants.py: the finite-x
     reading of 2 C_2 prod (1 + 1/((l-1)(l-2))) = 2.301); the pair supply grows ~ x*lnln(x)/ln(x) and the
     expected representation count ~ x*lnln(x)/(ln x)^2 -> infinity,
     so the model says the census never dries up: infinitely many
     rich rungs, a CONJECTURE with heuristic support. It is implied
     by Dickson's conjecture via the q = 3 family alone (r and
     p = 2r-3 both prime gives p+1 = 2(r-1); the pair (x, 2x-3) is
     admissible) -- the same epistemic tier as twin primes (which
     the twin TERM of the same rule needs).

Tier: census facts are rule (exhaustive, p <= 5*10^7); decade trends
are pattern; "infinitely many" is a conjecture with a measured-and-
calibrated heuristic behind it. Not a proof.

Resource: peak commit 272 MB at N = 5*10^7, wall ~1.5 s. N is a CLI
arg: `python explore_rich_rungs.py [N]`
(default 50000000). OPENBLAS_NUM_THREADS=1 set before numpy import
(bare import commits ~730 MB of thread arenas).
"""

import os
import sys
from math import isqrt, log

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import numpy as np


def prime_sieve(n):
    """Boolean primality array for 0..n."""
    isp = np.ones(n + 1, dtype=bool)
    isp[:2] = False
    for i in range(2, isqrt(n) + 1):
        if isp[i]:
            isp[i * i:: i] = False
    return isp


def f_direct(p, isp):
    """Direct divisor-enumeration f(p): independent of the vector scan."""
    m = p + 1
    c = 0
    for a in range(2, isqrt(m) + 1):
        if m % a == 0:
            b = m // a
            if isp[a + 1] and isp[b + 1] and b + 1 < p:
                c += 1
    return c


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 50_000_000

    print(f"RICH RUNGS: f(p) = #(p+1 = (q-1)(r-1)) for primes p <= {N:,}")
    print("=" * 72)
    print()

    isp = prime_sieve(N + 2)
    primes = np.flatnonzero(isp[: N + 1]).astype(np.int64)
    k_max = len(primes)
    print(f"pi({N:,}) = {k_max:,} rungs")
    print()

    # --- the scan: iterate the smaller divisor a (a+1 prime), count
    # representations at p = a*b - 1 and accumulate the heuristic ---
    counts = np.zeros(N + 1, dtype=np.uint16)   # f(p), indexed by p

    SMALL_ODD = [int(q) for q in primes[1:] if q <= 100]   # 3..97
    PRODFAC = 0.5
    for q in SMALL_ODD:
        PRODFAC *= 1.0 - 1.0 / q
    NDEC = len(str(N)) + 1
    exp_dec = np.zeros(NDEC)     # expected reps, bucketed by decade of n
    removed = 0                  # b+1 >= p exclusions (exactly p=3's 2*2)

    CHUNK = 5_000_000
    amax = isqrt(N + 1)
    for a in range(2, amax + 1):
        if not isp[a + 1]:
            continue
        bmax = (N + 1) // a
        for lo in range(a, bmax + 1, CHUNK):
            bs = np.arange(lo, min(lo + CHUNK, bmax + 1), dtype=np.int64)
            bs = bs[isp[bs + 1]]
            if not bs.size:
                continue
            n = a * bs - 1                     # candidate rung prime
            # heuristic weight for EVERY pair (n prime or not):
            # P(n prime | n coprime to primes <= 100) ~ 1/(ln n * PRODFAC)
            ok = np.ones(n.size, dtype=bool)
            for ell in SMALL_ODD:              # n is always odd (a,b even)
                ok &= (n % ell) != 0
            n_ok = n[ok]
            if n_ok.size:
                dec = np.log10(n_ok.astype(np.float64)).astype(np.int64)
                w = 1.0 / (np.log(n_ok) * PRODFAC)
                exp_dec[: NDEC] += np.bincount(dec, weights=w,
                                               minlength=NDEC)[:NDEC]
            # measured: n prime (and the q,r < p boundary, p=3 only)
            pm = isp[n]
            good = pm & (bs + 1 < n)
            removed += int((pm & ~good).sum())
            counts[n[good]] += 1               # n distinct within a chunk

    assert removed == 1, f"expected exactly the p=3 boundary case, got {removed}"
    assert counts[3] == 0

    f_all = counts[primes]

    # --- I. Exact small-case settlement ---
    print("I. SMALL-CASE SETTLEMENT (the published table, re-derived)")
    print("-" * 72)
    anchors = {5: 0, 7: 1, 11: 1, 13: 0, 17: 0, 19: 1, 23: 2, 29: 0,
               31: 1, 71: 3}
    for p, want in anchors.items():
        assert counts[p] == want, f"f({p}) = {counts[p]}, doc says {want}"
    print(f"  f anchors hold: " +
          ", ".join(f"f({p})={v}" for p, v in anchors.items()))

    # cumulative new_preds(k) = twin + f must reproduce the published
    # table 1,3,4,5,5,7,9,9,11 for k = 3..11
    published = [1, 3, 4, 5, 5, 7, 9, 9, 11]
    cum = 0
    got = []
    for idx in range(2, 11):                   # rungs k = 3..11
        p = int(primes[idx])
        twin = 1 if isp[p - 2] else 0
        cum += twin + int(counts[p])
        got.append(cum)
    assert got == published, f"prediction table mismatch: {got}"
    print(f"  cumulative prediction table k=3..11 reproduced: {got}")
    print()

    # --- II. Census ---
    print("II. CENSUS")
    print("-" * 72)

    rich_mask = f_all >= 1
    rich_p = primes[rich_mask]
    n_rich = int(rich_mask.sum())
    n_reps = int(f_all.sum())

    # property: rich requires p = 3 (mod 4)  (a, b both even => 4 | p+1)
    assert np.all(rich_p % 4 == 3), "a rich rung with p != 3 mod 4?!"
    mod4_class = int((primes % 4 == 3).sum())
    print(f"  rich rungs: {n_rich:,} of {k_max:,} "
          f"({100 * n_rich / k_max:.2f}%); representations: {n_reps:,}")
    print(f"  PROPERTY: all rich p = 3 (mod 4) (both factors even); "
          f"within that class: {100 * n_rich / mod4_class:.1f}%")
    print()

    # per-decade: density, multiplicity, twin comparison
    twin_mask = np.zeros(k_max, dtype=bool)
    twin_mask[2:] = isp[primes[2:] - 2]        # p >= 5: is p-2 prime
    digs = np.log10(primes.astype(np.float64)).astype(np.int64)

    print(f"  {'p in':>22} {'rungs':>9} {'rich':>8} {'dens':>6} "
          f"{'reps':>9} {'f-bar':>5} {'twins':>8} {'rich/tw':>7}")
    meas_dec = np.zeros(NDEC)
    for d in range(int(digs.max()) + 1):
        m = digs == d
        rungs = int(m.sum())
        if rungs == 0:
            continue
        rich_d = int((m & rich_mask).sum())
        reps_d = int(f_all[m].sum())
        meas_dec[d] = reps_d
        twins_d = int((m & twin_mask).sum())
        fbar = reps_d / rich_d if rich_d else 0.0
        ratio = rich_d / twins_d if twins_d else float("inf")
        hi = min(10 ** (d + 1) - 1, N)
        print(f"  {10**d:>10,}..{hi:>10,} {rungs:>9,} {rich_d:>8,} "
              f"{100*rich_d/rungs:>5.1f}% {reps_d:>9,} {fbar:>5.2f} "
              f"{twins_d:>8,} {ratio:>7.2f}")
    n_twin = int(twin_mask.sum())
    print(f"  totals: rich/twin = {n_rich / n_twin:.2f} "
          f"({n_rich:,} rich vs {n_twin:,} twin rungs)")
    print()

    # multiplicity histogram + champions
    hist = np.bincount(f_all)
    print("  multiplicity f -> rung count: " +
          ", ".join(f"{f}:{int(c):,}" for f, c in enumerate(hist)
                    if f >= 1 and c > 0))
    top = np.argsort(f_all)[-5:][::-1]
    print("  champions:")
    for idx in top:
        p = int(primes[idx])
        fd = f_direct(p, isp)
        assert fd == int(f_all[idx]), \
            f"vector scan disagrees with direct count at p={p}"
        print(f"    f = {int(f_all[idx]):>2} at p = {p:,} "
              f"(p+1 = {factored_str(p + 1)})")
    print("  (each champion re-counted by direct divisor enumeration)")
    print()

    # --- III. Heuristic ---
    print("III. CONDITIONED-CRAMER HEURISTIC")
    print("-" * 72)
    print("  model: P(ab-1 prime) ~ 1/(ln n * prod_(ell<=100)(1-1/ell)),")
    print("  applied only when ab-1 is coprime to every prime <= 100")
    print("  (divisibility computed exactly per pair; ell = 2 is free,")
    print("  ab-1 is always odd). Measured vs expected representations:")
    print()
    print(f"  {'n in':>22} {'measured':>10} {'expected':>11} {'ratio':>6}")
    for d in range(NDEC):
        if meas_dec[d] == 0 and exp_dec[d] == 0:
            continue
        hi = min(10 ** (d + 1) - 1, N)
        r = (f"{meas_dec[d] / exp_dec[d]:6.3f}" if exp_dec[d]
             else "     -")  # below the ell<=100 conditioning floor
        print(f"  {10**d:>10,}..{hi:>10,} {int(meas_dec[d]):>10,} "
              f"{exp_dec[d]:>11,.1f} {r}")
    print(f"  horizon totals: measured {int(meas_dec.sum()):,}, "
          f"expected {exp_dec.sum():,.1f}, "
          f"ratio {meas_dec.sum() / exp_dec.sum():.3f}")
    print()

    # divergence shape: pairs(x) ~ x*lnln(x)/ln(x) * (1/ln x) reps
    print("  divergence shape: representations(x) * (ln x)^2 / "
          "(x * lnln x):")
    cum_meas = np.cumsum(meas_dec)
    prev_x = 0
    for d in range(2, NDEC):
        x = min(10 ** (d + 1) - 1, N)
        if cum_meas[d] == 0 or x == prev_x:
            continue
        prev_x = x
        c = cum_meas[d] * log(x) ** 2 / (x * log(log(x)))
        print(f"    x = {x:>11,}: C = {c:.3f}")
    print("  (slow drift in C = the usual lower-order terms; the point")
    print("   is divergence: the expected count never dries up)")
    print()

    print("=" * 72)
    print("FINDINGS")
    print(f"  1. (property) rich requires p = 3 (mod 4); "
          f"verified on all {n_rich:,} rich rungs")
    print(f"  2. (rule)     {n_rich:,} rich rungs <= {N:,} "
          f"({100*n_rich/k_max:.2f}% of rungs, "
          f"{100*n_rich/mod4_class:.1f}% of the 3-mod-4 class)")
    print(f"  3. (observation) mean multiplicity ~ "
          f"{n_reps/n_rich:.2f}; champion f = {int(f_all.max())}")
    print(f"  4. (observation) rich/twin = {n_rich/n_twin:.2f} "
          f"and growing -- the factorization term dominates")
    print(f"  5. (heuristic) Cramer model calibrated at ratio "
          f"{meas_dec.sum()/exp_dec.sum():.3f}; expected count ~ "
          f"x*lnln(x)/(ln x)^2 diverges -> infinitely many rich rungs "
          f"(conjecture, implied by Dickson)")


def factored_str(m):
    """Small-number factorization string for champion display."""
    parts = []
    d = 2
    while d * d <= m:
        e = 0
        while m % d == 0:
            m //= d
            e += 1
        if e:
            parts.append(f"{d}^{e}" if e > 1 else f"{d}")
        d += 1
    if m > 1:
        parts.append(f"{m}")
    return " * ".join(parts)


if __name__ == "__main__":
    main()
