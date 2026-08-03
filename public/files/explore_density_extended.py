"""Transparency density to k=2000: what the wider range settles, and what
it turns out not to be able to say.

The middle range of three. explore_asymptotic_density.py runs the same
tower to k=200 and carries the criterion and the mechanism;
explore_complexity_ledger.py runs it to k=10000 and reads lambda's growth
as a ledger over the non-transparent rungs. A prime p_k is
lambda-transparent iff (p_k - 1) | lambda(k-1).

THE QUESTIONS:
  Q1. Density through k=2000, with 100-rung windows -- is it still moving
      at the top of the range?
  Q2. S(k), the distinct primes in lambda. Does S(k)/pi(p_k) -> 1? That
      would force density -> 1, so it is worth testing -- but it is a
      SUFFICIENT condition, and a falling ratio settles nothing on its
      own. The measurement that decides whether sparsity is even the
      right frame is omega(p-1): how many primes one rung actually asks
      of S.
  Q3. Do non-transparent rungs break on a prime new to lambda, or on a
      power bump of one already there?
  Q4. Can a power-law fit to the window rates say anything about the RATE
      of convergence? The test is not the fit's own residuals -- it is
      the fit against a measurement outside its range, which the k=10000
      script supplies.

SCOPE. The density tending to 1 is a theorem, proved by an elementary
sieve bound on log lcm{p-1 : p <= x}, general in x and computing at no
specific k (explore_lcm_shifted_primes.py). Nothing here bears on the
limit; the rate is open and Elliott-Halberstam-hard. Q4's answer is
negative and section VI states it as such.

Design: one pass over the first 2000 primes carrying lambda as a running
exponent map, so transparency, the blocking kind, S(k) and omega(p-1) all
fall out of the same per-rung exponent comparison.

Findings, tiers and their controls: section VIII.

Run: python prime/code/explore_density_extended.py  (well under a second;
integers and dicts only, far under the 512MB analysis ceiling)
"""

import sys
sys.path.insert(0, '.')
from math import gcd, log, log2, sqrt
from collections import Counter
from prime.code.crt import is_prime, factorize


def lcm(a, b):
    return a * b // gcd(a, b)


def first_n_primes(n):
    ps = []
    c = 2
    while len(ps) < n:
        if is_prime(c):
            ps.append(c)
        c += 1
    return ps


def prime_count_approx(x):
    if x < 2:
        return 0
    return x / log(x)


def section(title):
    print(f"\n{'=' * 76}")
    print(f"  {title}")
    print(f"{'=' * 76}")


def main():
    K_MAX = 2000

    print("=" * 76)
    print("  THREAD 10 EXTENSION: DENSITY TO k=2000")
    print("  Stronger evidence, S(k) growth, convergence model")
    print("=" * 76)

    primes = first_n_primes(K_MAX)
    print(f"\n  Tower k=1..{K_MAX}, p_max={primes[-1]}.")

    tower = []
    running_lcm = 1
    running_lcm_factors = {}
    trans_count = 0
    new_prime_count = 0
    power_bump_count = 0
    max_new_powers = 0   # max new prime powers introduced by one jump

    for k_idx in range(K_MAX):
        k = k_idx + 1
        p = primes[k_idx]
        pm1 = p - 1
        pm1_factors = factorize(pm1)

        transparent = True
        is_new_prime = False
        is_power_bump = False
        new_powers = 0

        for q, e in pm1_factors.items():
            old_e = running_lcm_factors.get(q, 0)
            if e > old_e:
                transparent = False
                new_powers += 1
                if old_e == 0:
                    is_new_prime = True
                else:
                    is_power_bump = True

        if new_powers > max_new_powers:
            max_new_powers = new_powers

        if k == 1:
            transparent = False

        if transparent and k > 1:
            trans_count += 1
        elif k > 1:
            if is_new_prime:
                new_prime_count += 1
            elif is_power_bump:
                power_bump_count += 1

        running_lcm = lcm(running_lcm, pm1)
        for q, e in pm1_factors.items():
            running_lcm_factors[q] = max(running_lcm_factors.get(q, 0), e)

        s_k = len(running_lcm_factors)
        density = trans_count / (k - 1) if k > 1 else 0

        tower.append({
            'k': k, 'p': p, 'transparent': transparent and k > 1,
            'density': density, 'trans_count': trans_count,
            's_k': s_k, 'lambda': running_lcm,
            'omega': len(pm1_factors),
        })

    # =================================================================
    section("I. DENSITY AT MILESTONES")
    # =================================================================

    print(f"\n  {'k':>6} {'p_k':>7} {'trans':>6} {'density':>8} "
          f"{'|S(k)|':>7} {'pi(p_k)':>8} {'S/pi':>7}")
    print(f"  {'-' * 52}")

    milestones = [10, 20, 50, 100, 200, 300, 400, 500, 750, 1000, 1250, 1500, 1750, 2000]
    for k in milestones:
        if k > K_MAX:
            break
        t = tower[k-1]
        pi_pk = sum(1 for p in primes if p <= t['p'])
        s_pi = t['s_k'] / pi_pk if pi_pk > 0 else 0
        print(f"  {k:>6} {t['p']:>7} {t['trans_count']:>6} {t['density']:>8.4f} "
              f"{t['s_k']:>7} {pi_pk:>8} {s_pi:>7.4f}")

    # =================================================================
    section("II. WINDOW DENSITIES (windows of 100)")
    # =================================================================

    window = 100
    print(f"\n  {'window':>18} {'trans':>6} {'density':>8} {'bar':>30}")
    print(f"  {'-' * 65}")

    for start in range(1, K_MAX, window):
        end = min(start + window, K_MAX + 1)
        w_trans = sum(1 for t in tower[start-1:end-1] if t['transparent'])
        w_total = end - start
        w_dens = w_trans / w_total if w_total > 0 else 0
        bar = '#' * int(w_dens * 40)
        print(f"  {f'k={start}-{end-1}':>18} {w_trans:>6} {w_dens:>8.4f} {bar}")

    # =================================================================
    section("III. S(k) GROWTH -- PRIMES IN LAMBDA")
    # =================================================================

    print("""
  S(k) = distinct prime factors of lambda(k) = primes that have appeared
  as factors of some p_j - 1 for j <= k.

  pi(p_k) = total primes up to p_k.

  If S(k)/pi(p_k) -> 1, lambda eventually contains ALL small primes,
  which would force density -> 1. That is a SUFFICIENT condition, and
  the table below refutes it -- S/pi falls throughout. It was never a
  necessary one, and the reason is the second measurement here: a rung
  does not need S to be large, it needs S to contain the few primes
  dividing ITS OWN p-1, and omega(p-1) is about 3. Sparse against
  pi(p_k) and ample against omega(p-1) are not in tension; the two
  numbers are answers to different questions.
""")

    print(f"  {'k':>6} {'p_k':>7} {'|S(k)|':>7} {'pi(p_k)':>8} "
          f"{'S/pi':>7} {'new in window':>14}")
    print(f"  {'-' * 52}")

    prev_s = 0
    for k in milestones:
        if k > K_MAX:
            break
        t = tower[k-1]
        pi_pk = sum(1 for p in primes if p <= t['p'])
        new_in_window = t['s_k'] - prev_s
        s_pi = t['s_k'] / pi_pk if pi_pk > 0 else 0
        print(f"  {k:>6} {t['p']:>7} {t['s_k']:>7} {pi_pk:>8} "
              f"{s_pi:>7.4f} {new_in_window:>14}")
        prev_s = t['s_k']

    omegas = [t['omega'] for t in tower[1:]]
    mean_omega = sum(omegas) / len(omegas)
    print(f"\n  What one rung actually asks of S: omega(p-1) over "
          f"k=2..{K_MAX} has")
    print(f"  mean {mean_omega:.2f} and max {max(omegas)}, against "
          f"|S({K_MAX})| = {tower[-1]['s_k']}.")

    # =================================================================
    section("IV. NON-TRANSPARENT BREAKDOWN")
    # =================================================================

    print(f"""
  Total primes (k=2..{K_MAX}): {K_MAX - 1}
  Transparent: {trans_count} ({trans_count/(K_MAX-1)*100:.1f}%)
  Non-transparent: {K_MAX - 1 - trans_count} ({(K_MAX-1-trans_count)/(K_MAX-1)*100:.1f}%)
    Due to new prime in p-1: {new_prime_count}
    Due to power bump only:  {power_bump_count}
  Max new prime powers in any single jump: {max_new_powers}
""")
    # jump anatomy (rule, k<=K_MAX): every lambda jump introduces
    # exactly one new prime power.
    assert max_new_powers == 1, \
        f"a jump introduced {max_new_powers} new prime powers (a finding!)"

    print("  Non-transparent rate in windows of 200:")
    print(f"  {'window':>18} {'non-trans':>10} {'rate':>8}")
    print(f"  {'-' * 40}")

    for start in range(1, K_MAX, 200):
        end = min(start + 200, K_MAX + 1)
        nt = sum(1 for t in tower[start-1:end-1] if not t['transparent'] and t['k'] > 1)
        total = end - start
        rate = nt / total if total > 0 else 0
        print(f"  {f'k={start}-{end-1}':>18} {nt:>10} {rate:>8.4f}")

    # =================================================================
    section("V. ALPHA TREND")
    # =================================================================

    print(f"\n  {'k':>6} {'log2(lam)':>10} {'log2(phi)':>10} {'alpha':>8}")
    print(f"  {'-' * 38}")

    running_phi = 1
    for t in tower:
        running_phi *= (t['p'] - 1) if t['k'] > 1 else 1
        if t['k'] <= 1:
            continue
        if t['lambda'] > 1 and running_phi > 1 and t['k'] in milestones:
            alpha = log(t['lambda']) / log(running_phi)
            print(f"  {t['k']:>6} {log2(t['lambda']):>10.1f} "
                  f"{log2(running_phi):>10.1f} {alpha:>8.4f}")

    # =================================================================
    section("VI. CONVERGENCE MODEL")
    # =================================================================

    print("""
  Fit: non-transparent fraction f(k) = C / k^a.
  Take log: log(f) = log(C) - a*log(k).
  Linear regression on (log(k), log(f)) for window data.
""")

    import math
    window_data = []
    for start in range(2, K_MAX, 100):
        end = min(start + 100, K_MAX + 1)
        nt = sum(1 for t in tower[start-1:end-1] if not t['transparent'] and t['k'] > 1)
        total = end - start
        if total > 0 and nt > 0:
            f = nt / total
            mid = (start + end - 1) / 2
            window_data.append((mid, f))

    if len(window_data) >= 3:
        xs = [math.log(mid) for mid, _ in window_data]
        ys = [math.log(f) for _, f in window_data]
        n = len(xs)
        x_mean = sum(xs) / n
        y_mean = sum(ys) / n
        num = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys))
        den = sum((x - x_mean) ** 2 for x in xs)
        slope = num / den if den > 0 else 0
        intercept = y_mean - slope * x_mean
        C = math.exp(intercept)
        a = -slope

        syy = sum((y - y_mean) ** 2 for y in ys)
        r2 = (num ** 2) / (den * syy) if den * syy > 0 else 0

        # Refit without the first window, which sits far above the rest.
        def refit(data):
            lx = [math.log(m) for m, _ in data]
            ly = [math.log(v) for _, v in data]
            m_ = len(lx)
            xb, yb = sum(lx) / m_, sum(ly) / m_
            nu = sum((x - xb) * (y - yb) for x, y in zip(lx, ly))
            de = sum((x - xb) ** 2 for x in lx)
            sy = sum((y - yb) ** 2 for y in ly)
            return (math.exp(yb + (nu / de) * xb), -nu / de,
                    (nu ** 2) / (de * sy) if de * sy > 0 else 0)

        C1, a1, r2_1 = refit(window_data[1:])

        print(f"  Model: f(k) ~ {C:.4f} / k^{a:.4f}   (R^2 = {r2:.4f})")
        print(f"  DROPPING THE FIRST WINDOW: f(k) ~ {C1:.4f} / k^{a1:.4f} "
              f"(R^2 = {r2_1:.4f})")
        tail = [(m, v) for m, v in window_data if m > 200]
        tn = len(tail)
        tx = [m for m, _ in tail]
        ty = [v for _, v in tail]
        txb, tyb = sum(tx) / tn, sum(ty) / tn
        tnu = sum((x - txb) * (y - tyb) for x, y in zip(tx, ty))
        tde = sum((x - txb) ** 2 for x in tx)
        tsy = sum((y - tyb) ** 2 for y in ty)
        tr = tnu / (tde * tsy) ** 0.5 if tde * tsy > 0 else 0
        h1 = sum(ty[:tn // 2]) / (tn // 2)
        h2 = sum(ty[tn // 2:]) / (tn - tn // 2)

        print(f"""
  Read those two lines together before using either. The exponent nearly
  halves and the fit loses more than half its explained variance when one
  window of the twenty is removed: the decay this model reports is carried
  mostly by the drop out of k <= 100, not by the range it was fitted over.
  Over the {tn} windows past k=200 the rate falls from a mean of {h1:.4f} to
  {h2:.4f}, correlation {tr:+.2f} -- a real decline, and far too noisy to carry
  an exponent.
""")
        print(f"  {'k midpoint':>12} {'observed f':>10} {'predicted f':>12}")
        print(f"  {'-' * 38}")
        for mid, f in window_data:
            pred = C / mid**a
            print(f"  {mid:>12.0f} {f:>10.4f} {pred:>12.4f}")

        print()
        print("  OUT-OF-RANGE TEST -- the model against a measurement, not")
        print("  against itself. explore_complexity_ledger.py runs the same")
        print("  tower to k=10000 and counts 1986 non-transparent rungs of")
        print("  9999, f = 0.1986 (80.1% transparent).")
        print()
        f_ext = C / 10000 ** a
        print(f"    at k=10000 this model predicts f = {f_ext:.4f} "
              f"({(1-f_ext)*100:.1f}% transparent)")
        print(f"    measured (explore_complexity_ledger.py)  f = 0.1986 "
              f"(80.1% transparent)")
        print(f"    the model is low by {0.1986 - f_ext:.4f} in f, "
              f"{(0.1986 - f_ext)/0.1986*100:.0f}% of the measured value")
        print()
        print("  So the fit does not survive one step outside its range, and")
        print("  no extrapolation is printed from it. The decay is real --")
        print("  the density does tend to 1, which is a theorem proved by an")
        print("  elementary sieve bound and not by any fit here")
        print("  (explore_lcm_shifted_primes.py) -- but its RATE is open and")
        print("  Elliott-Halberstam-hard, and a power law read off twenty")
        print("  noisy windows is not evidence about it.")

    # =================================================================
    section("VII. LONGEST PLATEAUS")
    # =================================================================

    runs = []
    current_run = 0
    current_start = None

    for t in tower[1:]:
        if t['transparent']:
            if current_run == 0:
                current_start = t['k']
            current_run += 1
        else:
            if current_run > 0:
                runs.append((current_start, current_run))
            current_run = 0

    if current_run > 0:
        runs.append((current_start, current_run))

    print(f"\n  Top 10 longest consecutive transparent runs:")
    print(f"  {'start k':>8} {'length':>8} {'primes':>30}")
    print(f"  {'-' * 50}")

    for start_k, length in sorted(runs, key=lambda x: -x[1])[:10]:
        ps = [tower[k-1]['p'] for k in range(start_k, min(start_k + length, K_MAX + 1))]
        ps_str = f"{ps[0]}..{ps[-1]}" if len(ps) > 1 else str(ps[0])
        print(f"  {start_k:>8} {length:>8} {ps_str:>30}")

    print(f"\n  Longest run: {max(l for _, l in runs) if runs else 0}")
    print(f"  Runs of length >= 10: {sum(1 for _, l in runs if l >= 10)}")
    print(f"  Runs of length >= 20: {sum(1 for _, l in runs if l >= 20)}")
    print(f"  Runs of length >= 50: {sum(1 for _, l in runs if l >= 50)}")

    # =================================================================
    section("VIII. KEY FINDINGS")
    # =================================================================

    final = tower[-1]
    print(f"""
  1. DENSITY AT k={K_MAX}: {final['density']:.4f}
     ({final['trans_count']}/{K_MAX-1} transparent).
     Window k={K_MAX-99}-{K_MAX}: {sum(1 for t in tower[-100:] if t['transparent'])}/100
     = {sum(1 for t in tower[-100:] if t['transparent'])/100:.2f}.

  2. S(k) IS SPARSE, AND THAT WAS NEVER THE OBSTACLE. |S({K_MAX})| =
     {final['s_k']} distinct primes in lambda, S/pi(p_k) = {final['s_k'] / K_MAX:.4f} and falling
     from 0.50 at k=10 -- so the sufficient condition section III sets
     up, S/pi -> 1 forcing density -> 1, is refuted in range. The
     density rises anyway, and no bias in the p-1 values is needed to
     explain it: a rung asks S only for the primes dividing its OWN
     p-1, and omega(p-1) has mean {mean_omega:.2f} and max {max(omegas)} here. Comparing
     {final['s_k']} against pi(p_k) = {K_MAX} answers a question no rung asks.
     Observation, k=2..{K_MAX}.

  3. NON-TRANSPARENT BREAKDOWN. {new_prime_count} rungs blocked by a prime new to
     lambda, {power_bump_count} by a power bump alone. New-prime blocks dominate, and
     each new prime can enter exactly once -- so the {new_prime_count} equals the
     number of distinct primes entering, not a frequency over them
     (section IV's max-new-powers-per-jump of 1 is why the two counts
     coincide, and that ceiling is an observation in range, not a
     construction).

  4. CONVERGENCE -- the decay is real and the FIT IS NOT USABLE. The
     window fit f(k) ~ {C:.4f}/k^{a:.4f} loses half its explained variance
     (R^2 {r2:.3f} -> {r2_1:.3f}) and nearly half its exponent when one of the
     twenty windows is dropped, and past k=200 the rate falls only from
     a mean of {h1:.3f} to {h2:.3f} at correlation {tr:+.2f}. Tested one step out of
     range it fails outright: at k=10000 it predicts f = {C / 10000 ** a:.4f} where
     explore_complexity_ledger.py measures 0.1986, low by
     {(0.1986 - C / 10000 ** a)/0.1986*100:.0f}% of the measured value. So this script supplies
     evidence that the non-transparent fraction declines over
     k=2..{K_MAX} and supplies NOTHING about the rate. That the density
     tends to 1 is a theorem and is not this fit's to support: the
     proof is an elementary sieve bound on log lcm{{p-1 : p <= x}},
     general in x (explore_lcm_shifted_primes.py). The rate stays open
     and Elliott-Halberstam-hard.
""")

    print("=" * 76)
    print("  Done.")
    print("=" * 76)


if __name__ == "__main__":
    main()
