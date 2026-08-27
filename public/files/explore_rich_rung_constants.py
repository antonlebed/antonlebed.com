"""
explore_rich_rung_constants.py -- THE RICH-RUNG CONSTANTS DERIVED
(descends from explore_rich_rungs.py, whose census this script
re-derives as its control; the tower's rich-rung block).

THE QUESTION. A rung p of the primorial tower is RICH when
f(p) = #{(a, b) : ab = p + 1, 2 <= a <= b, a + 1 and b + 1 prime}
is at least 1. The census to 5*10^7 left two numbers undeserved: the
SHAPE CONSTANT C(x) = reps(x) * (ln x)^2 / (x * lnln x), where reps(x)
is the sum of f(p) over primes p <= x, read at 2.53-2.58 over five
decades; and the MEAN MULTIPLICITY f-bar = reps / rich over the rich
rungs of a decade, read flat at 1.93-1.94 from 10^4 to the horizon. A
conditioned-Cramer model tracks reps(x) at ratio 1.000 and says
nothing about either constant. THIS SCRIPT ASKS: what are they?

THE HAND ANALYSIS (derived before the engine; the sections verify it).

 1. A REPRESENTATION IS A PRIME PAIR ON A LINE. Write q = a + 1 and
    r = b + 1, both prime, q <= r. Then p = (q-1)(r-1) - 1 =
    (q-1)*r - q. So reps(x) = sum over odd primes q with (q-1)^2 <=
    x+1 of N_q(x), N_q(x) = #{r prime, q <= r <= (x+1)/(q-1) + 1 :
    (q-1)*r - q prime}. Each N_q is a Hardy-Littlewood count for the
    pair of linear forms (r, (q-1)r - q). Its singular series: at
    ell = 2 the second form is odd for every r (q odd), one residue
    killed, factor 2; at an odd ell dividing q-1 the second form is
    -q, never zero, one residue killed, factor ell/(ell-1); at ell =
    q the second form is -r, zero exactly where the first is, one
    residue killed, factor q/(q-1); at every other odd ell two
    residues are killed, the twin-prime factor. So
        S(q) = 2*C_2 * prod_{ell odd, ell | q(q-1)} (ell-1)/(ell-2),
    C_2 the twin-prime constant, and conditioning on r prime,
        N_q(x) ~ S(q) * sum_{r prime in range} 1/ln((q-1)r - q).

 2. THE SHAPE CONSTANT IN CLOSED FORM. For q far below x the inner
    sum is about x/((q-1) (ln x)^2), so reps(x) ~ (x/(ln x)^2) *
    sum_{q <= sqrt x} S(q)/(q-1). With g(n) = prod_{ell odd | n}
    (ell-1)/(ell-2) (the ell = q factor tends to 1), S(q)/(q-1) =
    2*C_2 * g(q-1)/(q-1), and the sum W_0(y) of g(q-1)/(q-1) over
    primes q <= y is A * lnln y + B for the prime-average A of g(q-1)
    (the ell = q factors add a convergent sum, 0.72, to the full
    singular-series sum W(y) the decomposition below uses). Since
    g = 1 * h with h(ell) = 1/(ell-2) and h(ell^k) = 0 for k >= 2,
    the average over primes q of g(q-1) is sum_d h(d)/phi(d) over
    odd squarefree d, i.e.
        A = prod_{ell odd prime} (1 + 1/((ell-1)(ell-2))),
    so C_inf = lim C(x) = 2*C_2*A. Hand estimate: A ~ 1.74, 2*C_2 =
    1.3203, C_inf ~ 2.3. The finite-x reading C(x) carries the
    corrections the limit drops: the sqrt-x cut (lnln sqrt x = lnln x
    - ln 2), the constant B, and ln((q-1)r - q) against ln x along
    the inner sum; their sizes are what the sections print.

 3. THE MULTIPLICITY IS A PREDICTION OF THE INDEPENDENCE MODEL. For
    a prime p, f(p) = sum over the divisors a of p+1 with a+1 prime
    and a <= sqrt(p+1) of the indicator [(p+1)/a + 1 prime]. The
    conditioned-Cramer model makes these independent with rho_a =
    1/(ln c * prod_{ell <= 100}(1 - 1/ell)) for c = (p+1)/a + 1
    coprime to every prime <= 100 and rho_a = 0 otherwise -- and
    exact, rho_a = [c prime], for c < 101^2, where coprimality to the
    primes <= 100 IS primality and the formula would exceed 1. Then
    E[f] = sum rho_a and P(rich) = 1 - prod(1 - rho_a), both per
    rung, and the model's multiplicity is the ratio of their decade
    sums. Whether the model CARRIES the measured 1.94
    is the question; the perturbative reading (rho small) puts the
    excess over 1 at the order of (lnln p)^2 / ln p, which moves only
    from 0.54 to 0.46 across the census window -- flat is what a slow
    drift looks like there -- but the rich rungs are the highly
    composite p+1 where rho_a sum past 1 and nothing perturbative
    holds, so the number is read off the model and not guessed.
    Pairwise correlations between candidates at two divisors carry a
    singular series only at primes the conditioning does not fix, ell
    > 100, a factor within 0.2% of 1 -- the independence model with
    exact small-prime conditioning is the whole Hardy-Littlewood
    heuristic for f.

PREDICTIONS, FROZEN. P1: the Hardy-Littlewood count of item 1,
summed per decade of p, tracks the measured representation count
within 3% in every decade from 10^4 (the positive control; the sibling
conditioning of item 3, sum rho_a over primes p, tracks it too). P2:
A computed as the product lands in 1.70-1.78 and the prime-average of
g(q-1) over q <= 10^7 lands within 1% of it; C_inf = 2*C_2*A lands in
2.2-2.4; the Hardy-Littlewood C(x) at 5*10^7 lands within 3% of the
measured value and DECREASES toward C_inf across x = 10^8..10^12 by
the integral form. P3: the model's multiplicity lands within 5% of
the measured f-bar in every decade from 10^4, and its own per-decade
trend is what the flatness is read from. KILLS, as prints: a decade
where the Hardy-Littlewood count is off by more than 3%; A off the
prime-average by more than 1%; C_inf outside 2.2-2.4 or C(x) rising
away from it; the model's multiplicity off the measured by more than
5% in a decade from 10^4.

FINDINGS (the run's prints; tiers as the charter names them).

 F1. THE COUNT IS A HARDY-LITTLEWOOD SUM (rule in range; P1 held):
     the pair count of item 1 tracks the measured representations at
     ratio 0.994, 0.997, 0.997, 0.999 in the four decades from 10^4
     and 0.9987 at the horizon (1,160,045 against 1,158,530); the
     integral form of the inner sum agrees with the prime sum to
     0.2%. The sibling conditioning -- sum rho_a over primes p --
     tracks at 1.013, 1.005, 1.003, 1.002.

 F2. THE SHAPE CONSTANT IN CLOSED FORM (derivation within the
     Hardy-Littlewood heuristic; the prime-average the classical
     mean-value law, verified; P2 held whole): A = prod_{ell odd} (1 + 1/((ell-1)
     (ell-2))) = 1.74272540 and C_2 = 0.66016182, so C_inf = 2*C_2*A
     = 2.300962. The prime-average of g(q-1) reads 1.742358 at q <=
     10^7, within 0.02% of A, and W_0(y) - A lnln y settles at B =
     -0.5516 from 10^5 on.

 F3. THE MEASURED 2.53-2.58 IS THE FINITE-x READING OF 2.30 (rule in
     range for the agreement, the trend the model's): the
     Hardy-Littlewood C(x) reads 2.604, 2.575, 2.551, 2.536 at x =
     10^5, 10^6, 10^7, 5*10^7 against the measured 2.578, 2.566,
     2.544, 2.533, and by the integral form 2.534, 2.515, 2.500,
     2.488, 2.477 at x = 10^8..10^12. Split as 2 C_2 * [W(sqrt x) /
     lnln x] * kappa(x): at 5*10^7 the singular-series factor W/lnln
     x is 1.379, rising toward A = 1.743 from below (the sqrt-x cut
     and B are constants over lnln x), while kappa, the inner sums'
     logs, is 1.396, falling toward 1 from above; the product falls,
     and slower than any window shows -- 2.48 at 10^12 against 2.30.

 F4. THE MULTIPLICITY IS THE INDEPENDENCE MODEL'S (rule in range; P3
     held at 0.4%): the model's f-bar reads 1.941, 1.936, 1.934,
     1.927 in the four decades from 10^4 against the measured 1.939,
     1.944, 1.938, 1.929 -- ratios 0.999, 1.004, 1.002, 1.001 -- and
     the model's own reading drifts DOWN by about 0.005 per decade,
     which is what the census read as flat. The number is the
     saturated rungs': 378,497 rungs (12.6%) with sum rho >= 1 carry
     78.4% of the model's representations and 58.4% of its rich
     count, with measured f-bar 2.594 on them and 1.000 off them
     (observed; nearly forced at this range, a candidate surviving
     the sieve to 100 carrying rho >= 0.46, so two hits saturate
     unless both sit at the two smallest divisors near the horizon).
     Where the model's multiplicity goes past the window is not read
     here.

RUN RECORD. python explore_rich_rung_constants.py -- CHECKS: 11/11
passed, 9.5 s, peak working set 303.5 MB under memwatch (N = 5*10^7).
Sections: S1 the census and the per-rung model, S2 the
Hardy-Littlewood count per decade, S3 the closed form, the
prime-average, C(x) measured against the model and its integral-form
trend to 10^12. The rehearsal at N = 10^6 caught the model's cap:
below 101^2 the conditioning is primality and the formula exceeded 1.

ASSUMED, NOT RUN: the Hardy-Littlewood prime-pair heuristic; the mean
of a multiplicative function of q-1 over primes q as the sum of
h(d)/phi(d), the classical mean-value law (no source opened here; the
0.02% agreement at 10^7 is what this record stands on). Everything
else asserts.
"""

import os
import sys
from math import isqrt, log

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import numpy as np

CHECKS = []


def check(name, ok):
    CHECKS.append((name, ok))
    print(("  ok    " if ok else "  FAIL  ") + name)


def prime_sieve(n):
    isp = np.ones(n + 1, dtype=bool)
    isp[:2] = False
    for i in range(2, isqrt(n) + 1):
        if isp[i]:
            isp[i * i::i] = False
    return isp


def spf_table(n):
    """Smallest prime factor for 0..n (0 where undefined)."""
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i::i][spf[i::i] == 0] = i
    return spf


def odd_prime_factors(m, spf):
    out = []
    while m > 1:
        ell = int(spf[m])
        if ell != 2 and (not out or out[-1] != ell):
            out.append(ell)
        m //= ell
    return out


def g_of(m, spf):
    """g(m) = prod over odd primes ell | m of (ell-1)/(ell-2)."""
    v = 1.0
    for ell in odd_prime_factors(m, spf):
        v *= (ell - 1.0) / (ell - 2.0)
    return v


def twin_constant(limit, isp):
    """C_2 = prod_{ell odd prime <= limit} (1 - 1/(ell-1)^2)."""
    ells = np.flatnonzero(isp[:limit + 1])[1:].astype(np.float64)
    return float(np.exp(np.sum(np.log1p(-1.0 / (ells - 1.0) ** 2))))


def a_constant(limit, isp):
    """A = prod_{ell odd prime <= limit} (1 + 1/((ell-1)(ell-2)))."""
    ells = np.flatnonzero(isp[:limit + 1])[1:].astype(np.float64)
    return float(np.exp(np.sum(np.log1p(1.0 / ((ells - 1.0) *
                                               (ells - 2.0))))))


def hl_integral(q, x, npts=400):
    """S-free inner sum in integral form: int_q^{R} dt /
    (ln t * ln((q-1)t - q)), R = (x+1)/(q-1) + 1, on a log grid."""
    R = (x + 1) / (q - 1) + 1
    if R <= q:
        return 0.0
    t = np.exp(np.linspace(log(q), log(R), npts))
    y = 1.0 / (np.log(t) * np.log((q - 1) * t - q))
    return float(np.trapezoid(y, t))


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 50_000_000
    print(f"THE RICH-RUNG CONSTANTS: primes p <= {N:,}")
    print("=" * 72)

    isp = prime_sieve(max(N + 2, 10_000_001))
    primes = np.flatnonzero(isp[: N + 1]).astype(np.int64)
    k_max = len(primes)
    NDEC = len(str(N)) + 1
    LO_DEC = 4                                   # decades read from 10^4

    SMALL = [int(q) for q in primes if q <= 100]  # 2..97
    PRODFAC = 1.0
    for q in SMALL:
        PRODFAC *= 1.0 - 1.0 / q

    # ---------------------------------------------------------------
    # S1. THE CENSUS (control) AND THE INDEPENDENCE MODEL PER RUNG.
    # Scan the smaller divisor a (a+1 prime); at each prime n = ab-1
    # count the representation when b+1 is prime, and accumulate the
    # model's rho for the candidate c = b+1 whether prime or not.
    print()
    print("S1. CENSUS AND THE INDEPENDENCE MODEL PER RUNG")
    print("-" * 72)
    counts = np.zeros(k_max, dtype=np.int32)     # measured f, by rung
    S1 = np.zeros(k_max)                          # sum rho_a, by rung
    LG = np.zeros(k_max)                          # sum ln(1-rho_a)
    CHUNK = 5_000_000
    amax = isqrt(N + 1)
    for a in range(2, amax + 1):
        if not isp[a + 1]:
            continue
        bmax = (N + 1) // a
        for lo in range(a, bmax + 1, CHUNK):
            bs = np.arange(lo, min(lo + CHUNK, bmax + 1), dtype=np.int64)
            n = a * bs - 1
            sel = isp[n]
            if not sel.any():
                continue
            bs, n = bs[sel], n[sel]
            c = bs + 1
            idx = np.searchsorted(primes, n)
            # measured
            good = isp[c] & (c < n)               # excludes p = 3 only
            np.add.at(counts, idx[good], 1)
            # model: rho for every candidate c
            rho = np.zeros(c.size)
            small = c < 10201                     # 101^2: exact there
            rho[small] = isp[c[small]].astype(np.float64)
            big = ~small
            ok = np.ones(int(big.sum()), dtype=bool)
            cb = c[big]
            for ell in SMALL:
                ok &= (cb % ell) != 0
            r = np.zeros(cb.size)
            r[ok] = 1.0 / (np.log(cb[ok]) * PRODFAC)
            rho[big] = r
            np.add.at(S1, idx, rho)
            with np.errstate(divide="ignore"):
                np.add.at(LG, idx, np.log1p(-rho))

    anchors = {5: 0, 7: 1, 11: 1, 13: 0, 17: 0, 19: 1, 23: 2, 29: 0,
               31: 1, 71: 3}
    pidx = {int(p): i for i, p in enumerate(primes[:25])}
    check("census anchors f(5..71) reproduce the published table",
          all(counts[pidx[p]] == v for p, v in anchors.items()))
    rich = counts >= 1
    check("every rich rung is 3 mod 4",
          bool(np.all(primes[rich] % 4 == 3)))
    digs = np.log10(primes.astype(np.float64)).astype(np.int64)
    meas_reps = np.bincount(digs, weights=counts, minlength=NDEC)
    meas_rich = np.bincount(digs, weights=rich, minlength=NDEC)
    mod_reps = np.bincount(digs, weights=S1, minlength=NDEC)
    mod_rich = np.bincount(digs, weights=1.0 - np.exp(LG), minlength=NDEC)
    print(f"  {'p in':>22} {'reps':>9} {'model':>10} {'ratio':>6}"
          f" {'f-bar':>6} {'model':>6} {'ratio':>6}")
    p1b_ok, p3_ok = True, True
    for d in range(NDEC):
        if meas_reps[d] == 0:
            continue
        hi = min(10 ** (d + 1) - 1, N)
        fb = meas_reps[d] / meas_rich[d]
        fm = mod_reps[d] / mod_rich[d]
        print(f"  {10**d:>10,}..{hi:>10,} {int(meas_reps[d]):>9,} "
              f"{mod_reps[d]:>10,.1f} {meas_reps[d]/mod_reps[d]:6.3f}"
              f" {fb:6.3f} {fm:6.3f} {fb/fm:6.3f}")
        if d >= LO_DEC:
            p1b_ok &= abs(meas_reps[d] / mod_reps[d] - 1) <= 0.03
            p3_ok &= abs(fb / fm - 1) <= 0.05
    check("P1b: sum rho over primes tracks reps within 3% per decade "
          "from 10^4", p1b_ok)
    check("P3: the independence model's multiplicity within 5% of "
          "the measured per decade from 10^4", p3_ok)
    # where the model's rich mass sits: saturated rungs
    sat = S1 >= 1.0
    print(f"  rungs with sum rho >= 1: {int(sat.sum()):,}; they carry "
          f"{100 * S1[sat].sum() / S1.sum():.1f}% of the model's reps "
          f"and {100 * (1 - np.exp(LG[sat])).sum() / mod_rich.sum():.1f}% "
          f"of its rich count; measured f-bar on them "
          f"{counts[sat].sum() / max(1, rich[sat].sum()):.3f}, "
          f"off them {counts[~sat].sum() / max(1, rich[~sat].sum()):.3f}")

    # ---------------------------------------------------------------
    # S2. THE HARDY-LITTLEWOOD COUNT (item 1) PER DECADE.
    print()
    print("S2. THE HARDY-LITTLEWOOD PAIR COUNT PER DECADE")
    print("-" * 72)
    spf = spf_table(10_000_000)
    C2 = twin_constant(10_000_000, isp)
    print(f"  C_2 = {C2:.10f} (product to 10^7)")
    hl_reps = np.zeros(NDEC)
    hl_total_int = 0.0
    qmax = isqrt(N + 1) + 1
    for q in range(3, qmax + 1):
        if not isp[q]:
            continue
        S = 2 * C2 * g_of(q - 1, spf) * (q - 1.0) / (q - 2.0)
        rmax = (N + 1) // (q - 1) + 1
        rs = np.flatnonzero(isp[q:rmax + 1]).astype(np.int64) + q
        p = (q - 1) * rs - q
        p = p[(p <= N) & (p > q)]
        if p.size == 0:
            continue
        w = S / np.log(p.astype(np.float64))
        dec = np.log10(p.astype(np.float64)).astype(np.int64)
        hl_reps += np.bincount(dec, weights=w, minlength=NDEC)[:NDEC]
        hl_total_int += S * hl_integral(q, N)
    print(f"  {'p in':>22} {'reps':>9} {'H-L':>10} {'ratio':>6}")
    p1_ok = True
    for d in range(NDEC):
        if meas_reps[d] == 0:
            continue
        hi = min(10 ** (d + 1) - 1, N)
        print(f"  {10**d:>10,}..{hi:>10,} {int(meas_reps[d]):>9,} "
              f"{hl_reps[d]:>10,.1f} {meas_reps[d]/hl_reps[d]:6.3f}")
        if d >= LO_DEC:
            p1_ok &= abs(meas_reps[d] / hl_reps[d] - 1) <= 0.03
    check("P1: the Hardy-Littlewood count tracks reps within 3% per "
          "decade from 10^4", p1_ok)
    tot_meas, tot_hl = meas_reps.sum(), hl_reps.sum()
    print(f"  horizon: measured {int(tot_meas):,}, H-L {tot_hl:,.1f} "
          f"(ratio {tot_meas/tot_hl:.4f}), integral form "
          f"{hl_total_int:,.1f} (ratio to sum {hl_total_int/tot_hl:.4f})")
    check("integral form agrees with the prime-sum form within 2%",
          abs(hl_total_int / tot_hl - 1) <= 0.02)

    # ---------------------------------------------------------------
    # S3. THE CLOSED FORM (item 2).
    print()
    print("S3. THE SHAPE CONSTANT IN CLOSED FORM")
    print("-" * 72)
    A = a_constant(10_000_000, isp)
    C_inf = 2 * C2 * A
    print(f"  A = prod (1 + 1/((l-1)(l-2))) = {A:.8f}; "
          f"C_inf = 2*C_2*A = {C_inf:.6f}")
    check("P2a: A in 1.70-1.78", 1.70 <= A <= 1.78)
    check("P2b: C_inf in 2.2-2.4", 2.2 <= C_inf <= 2.4)
    # prime-average of g(q-1) and the weighted sum W(y)
    qs = np.flatnonzero(isp[:10_000_001])[1:]   # odd primes to 10^7
    gv = np.fromiter((g_of(int(q) - 1, spf) for q in qs), dtype=float,
                     count=qs.size)
    print(f"  {'y':>12} {'mean g(q-1)':>12} {'W_0(y)':>9} "
          f"{'W_0 - A lnln y':>15}")
    for e in range(3, 8):
        y = 10 ** e
        m = qs <= y
        mean_g = gv[m].mean()
        W = float((gv[m] / (qs[m] - 1.0)).sum())
        print(f"  {y:>12,} {mean_g:12.6f} {W:9.5f} "
              f"{W - A * log(log(y)):15.5f}")
    check("P2c: the prime-average of g(q-1) at 10^7 within 1% of A",
          abs(mean_g / A - 1) <= 0.01)
    B = W - A * log(log(10 ** 7))
    # C(x) measured, H-L, and the integral-form trend to 10^12
    print()
    print(f"  C(x) = reps(x) (ln x)^2 / (x lnln x):")
    cum = np.cumsum(meas_reps)
    cum_hl = np.cumsum(hl_reps)
    seen = set()
    for d in range(LO_DEC, NDEC):
        x = min(10 ** (d + 1) - 1, N)
        if cum[d] == 0 or x in seen:
            continue
        seen.add(x)
        cm = cum[d] * log(x) ** 2 / (x * log(log(x)))
        ch = cum_hl[d] * log(x) ** 2 / (x * log(log(x)))
        print(f"    x = {x:>13,}: measured {cm:.3f}  H-L {ch:.3f}")
        if x == N:
            check("P2d: H-L C(x) at the horizon within 3% of measured",
                  abs(ch / cm - 1) <= 0.03)
    print("  integral-form C(x) beyond the census (q <= sqrt x, S(q) "
          "exact), split as")
    print("  C(x) = 2 C_2 * [W(sqrt x) / lnln x] * kappa(x), with "
          "W(y) = sum_{q <= y} S(q)/(2 C_2 (q-1))")
    print("  (the singular-series sum, -> A lnln y) and kappa the "
          "inner sums' logs against x/((q-1) (ln x)^2), -> 1:")
    prev = None
    trend_ok = True
    xs = [N] + [10 ** e for e in range(8, 13)]
    for x in xs:
        qm = isqrt(x + 1) + 1
        qq = np.flatnonzero(isp[3:min(qm, 10_000_000) + 1]) + 3
        tot, Wf = 0.0, 0.0
        for q in qq:
            q = int(q)
            S = 2 * C2 * g_of(q - 1, spf) * (q - 1.0) / (q - 2.0)
            tot += S * hl_integral(q, x, npts=120)
            Wf += S / (2 * C2 * (q - 1.0))
        cx = tot * log(x) ** 2 / (x * log(log(x)))
        f1 = 2 * C2 * Wf / log(log(x))
        print(f"    x = {x:>15,}: C = {cx:.3f} = 2 C_2 * "
              f"{Wf / log(log(x)):.4f} * {cx / f1:.4f}"
              f"   (W = {Wf:.4f}, A = {A:.4f})")
        if prev is not None:
            trend_ok &= cx < prev
        prev = cx
    check("P2e: the integral-form C(x) decreases across 10^8..10^12",
          trend_ok)

    print()
    print("=" * 72)
    n_ok = sum(1 for _, ok in CHECKS if ok)
    print(f"CHECKS: {n_ok}/{len(CHECKS)} passed")
    if n_ok != len(CHECKS):
        sys.exit(1)


if __name__ == "__main__":
    main()
