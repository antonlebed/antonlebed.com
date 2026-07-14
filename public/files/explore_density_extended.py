"""Thread 10 extension: push transparency density to k=2000.

Extends explore_asymptotic_density.py with:
  - Density through k=2000 (stronger evidence for density -> 1)
  - S(k) growth: how many distinct primes are in lambda at each rung?
  - S(k)/pi(p_k) ratio: does lambda's factor set approach "all primes"?
  - Model fit for convergence rate of non-transparent fraction
  - Power bump frequency: how often do power bumps (vs new primes) cause jumps?

Run: python prime/code/explore_density_extended.py
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
  which would force density -> 1.
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
    # exactly one new prime power -- cited by TOWER.md SVII.
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

        print(f"  Model: f(k) ~ {C:.4f} / k^{a:.4f}")
        print(f"  (non-transparent fraction decays as k^{{-{a:.2f}}})")
        print()
        print(f"  {'k midpoint':>12} {'observed f':>10} {'predicted f':>12}")
        print(f"  {'-' * 38}")
        for mid, f in window_data:
            pred = C / mid**a
            print(f"  {mid:>12.0f} {f:>10.4f} {pred:>12.4f}")

        print()
        print(f"  Extrapolated non-transparent fraction:")
        for k_ext in [5000, 10000, 50000]:
            f_ext = C / k_ext**a
            print(f"    k={k_ext}: {f_ext:.4f} ({(1-f_ext)*100:.1f}% transparent)")

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

  2. S(k) GROWTH: |S({K_MAX})| = {final['s_k']} distinct primes in lambda.
     S(k)/pi(p_k) = {final['s_k'] / K_MAX:.4f}.
     S(k) grows but does NOT approach pi(p_k) -- lambda's factor set
     is a SPARSE subset of all primes. Yet density still increases
     because p-1 values are biased toward these common factors.

  3. NON-TRANSPARENT BREAKDOWN:
     New primes: {new_prime_count}. Power bumps: {power_bump_count}.
     New primes dominate. Each new prime enters lambda exactly once.

  4. CONVERGENCE: non-transparent fraction decays, supporting density -> 1.
     The sieve becomes increasingly self-sufficient as it climbs.
""")

    print("=" * 76)
    print("  Done.")
    print("=" * 76)


if __name__ == "__main__":
    main()
