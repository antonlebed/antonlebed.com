"""Thread 10: Asymptotic density of lambda-transparent primes.

A prime p_k is lambda-transparent iff (p_k - 1) | lambda(k-1),
where lambda(k-1) = lcm(p_1-1, ..., p_{k-1}-1).

In sieve language: adding p_k to the sieve doesn't change the
multiplicative dynamics — p_k is "redundant" for the period.

Questions:
  Q1: Does the transparency density converge? To what?
  Q2: What controls whether a prime is transparent?
  Q3: Connection to smooth-number distribution in {p-1: p prime}?
  Q4: Does the running density stabilize or oscillate?

The key insight: p_k is transparent iff every prime power in the
factorization of (p_k - 1) already appears in lambda(k-1).
So transparency is about how "smooth" p_k - 1 is RELATIVE to
the accumulated prime-minus-one factorizations.

Run: python prime/code/explore_asymptotic_density.py
"""

import sys
sys.path.insert(0, '.')
from math import gcd, log, log2
from collections import Counter, defaultdict
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


def section(title):
    print(f"\n{'=' * 76}")
    print(f"  {title}")
    print(f"{'=' * 76}")


def main():
    K_MAX = 200

    print("=" * 76)
    print("  THREAD 10: ASYMPTOTIC DENSITY OF TRANSPARENCY")
    print("  Does the fraction of transparent primes converge?")
    print("=" * 76)

    primes = first_n_primes(K_MAX)
    print(f"\n  Computing tower through k={K_MAX}, p_max={primes[-1]}.")

    # Build the tower
    tower = []
    running_lcm = 1
    running_lcm_factors = {}
    trans_count = 0

    for k_idx in range(K_MAX):
        k = k_idx + 1
        p = primes[k_idx]
        pm1 = p - 1
        pm1_factors = factorize(pm1)

        prev_lcm = running_lcm

        transparent = True
        blocking_factors = {}
        for q, e in pm1_factors.items():
            old_e = running_lcm_factors.get(q, 0)
            if e > old_e:
                transparent = False
                blocking_factors[q] = (old_e, e)

        if k == 1:
            transparent = False

        if transparent and k > 1:
            trans_count += 1

        running_lcm = lcm(running_lcm, pm1)
        for q, e in pm1_factors.items():
            running_lcm_factors[q] = max(running_lcm_factors.get(q, 0), e)

        density = trans_count / (k - 1) if k > 1 else 0

        tower.append({
            'k': k, 'p': p, 'pm1': pm1, 'pm1_factors': pm1_factors,
            'transparent': transparent and k > 1,
            'blocking': blocking_factors,
            'density': density, 'trans_count': trans_count,
            'lambda': running_lcm,
        })

    # =================================================================
    section("I. TRANSPARENCY DENSITY THROUGH k=" + str(K_MAX))
    # =================================================================

    print(f"\n  {'k':>5} {'p_k':>6} {'trans':>6} {'count':>6} {'density':>8} "
          f"{'lambda_bits':>12}")
    print(f"  {'-' * 50}")

    for t in tower:
        if (t['k'] <= 20 or t['k'] % 10 == 0 or
            t['k'] in [25, 50, 75, 100, 125, 150, 175, 200]):
            tr = "YES" if t['transparent'] else ""
            lam_bits = log2(t['lambda']) if t['lambda'] > 0 else 0
            print(f"  {t['k']:>5} {t['p']:>6} {tr:>6} {t['trans_count']:>6} "
                  f"{t['density']:>8.4f} {lam_bits:>12.1f}")

    # =================================================================
    section("II. RUNNING DENSITY WINDOWS")
    # =================================================================

    print("""
  Instead of cumulative density, look at density in windows of 50 primes.
  If the density converges, windows should stabilize.
""")

    window = 50
    print(f"  {'window':>15} {'trans':>6} {'total':>6} {'density':>8}")
    print(f"  {'-' * 40}")

    for start in range(1, K_MAX, window):
        end = min(start + window, K_MAX + 1)
        w_trans = sum(1 for t in tower[start-1:end-1] if t['transparent'])
        w_total = end - start
        w_dens = w_trans / w_total if w_total > 0 else 0
        print(f"  {f'k={start}-{end-1}':>15} {w_trans:>6} {w_total:>6} {w_dens:>8.4f}")

    # =================================================================
    section("III. WHAT MAKES A PRIME TRANSPARENT?")
    # =================================================================

    print("""
  p_k is transparent iff every prime power in (p_k - 1) already divides
  lambda(k-1). What determines this?

  Key factor: the LARGEST prime factor of p_k - 1.
  If p_k - 1 has a large prime factor q, then q must already be in lambda.
  q enters lambda when some earlier prime p_j has q | (p_j - 1).
  By Linnik's theorem, such p_j exists and is bounded by q^L for some L.
  So large q factors are the bottleneck for transparency.
""")

    print("  Transparent primes and their p-1 factorizations:")
    print(f"  {'k':>4} {'p':>6} {'p-1 factors':>30} {'largest factor':>15}")
    print(f"  {'-' * 58}")

    for t in tower[:60]:
        if not t['transparent']:
            continue
        f = t['pm1_factors']
        largest = max(f.keys())
        fs = " * ".join(f"{q}^{e}" if e > 1 else str(q)
                       for q, e in sorted(f.items()))
        print(f"  {t['k']:>4} {t['p']:>6} {fs:>30} {largest:>15}")

    # Non-transparent: what blocks them?
    print()
    print("  Non-transparent primes and their blocking factors (first 30):")
    print(f"  {'k':>4} {'p':>6} {'blocking':>25} {'new prime power':>20}")
    print(f"  {'-' * 58}")

    shown = 0
    for t in tower[1:]:
        if t['transparent'] or shown >= 30:
            continue
        blocks = []
        for q, (old_e, new_e) in t['blocking'].items():
            if old_e == 0:
                blocks.append(f"{q}^{new_e}" if new_e > 1 else str(q))
            else:
                blocks.append(f"{q}:{old_e}->{new_e}")
        if blocks:
            print(f"  {t['k']:>4} {t['p']:>6} {','.join(blocks):>25} "
                  f"{'new prime' if any(t['blocking'][q][0]==0 for q in t['blocking']) else 'power bump':>20}")
            shown += 1

    # =================================================================
    section("IV. LARGEST PRIME FACTOR OF p-1")
    # =================================================================

    print("""
  The largest prime factor (lpf) of p-1 determines transparency.
  If lpf(p-1) is small relative to p, the prime is more likely transparent.

  For transparent primes: lpf(p-1) must already be in lambda.
  For non-transparent primes: some factor is new.
""")

    trans_lpf = []
    nontrans_lpf = []

    for t in tower[1:]:
        largest = max(t['pm1_factors'].keys())
        ratio = largest / t['p']
        if t['transparent']:
            trans_lpf.append((t['p'], largest, ratio))
        else:
            nontrans_lpf.append((t['p'], largest, ratio))

    print(f"  Transparent primes (n={len(trans_lpf)}):")
    print(f"    lpf/p: min={min(r for _,_,r in trans_lpf):.4f}, "
          f"max={max(r for _,_,r in trans_lpf):.4f}, "
          f"mean={sum(r for _,_,r in trans_lpf)/len(trans_lpf):.4f}")

    print(f"  Non-transparent primes (n={len(nontrans_lpf)}):")
    print(f"    lpf/p: min={min(r for _,_,r in nontrans_lpf):.4f}, "
          f"max={max(r for _,_,r in nontrans_lpf):.4f}, "
          f"mean={sum(r for _,_,r in nontrans_lpf)/len(nontrans_lpf):.4f}")

    # lpf distribution
    print()
    print("  Distribution of lpf(p-1) for transparent vs non-transparent:")

    buckets = [(0, 0.1), (0.1, 0.2), (0.2, 0.3), (0.3, 0.5), (0.5, 1.0)]
    print(f"  {'lpf/p range':>15} {'trans':>8} {'non-trans':>10} {'trans frac':>10}")
    print(f"  {'-' * 48}")

    for lo, hi in buckets:
        tc = sum(1 for _, _, r in trans_lpf if lo <= r < hi)
        nc = sum(1 for _, _, r in nontrans_lpf if lo <= r < hi)
        total = tc + nc
        frac = tc / total if total > 0 else 0
        print(f"  {f'[{lo:.1f}, {hi:.1f})':>15} {tc:>8} {nc:>10} {frac:>10.3f}")

    # =================================================================
    section("V. SMOOTHNESS OF p-1 AND TRANSPARENCY")
    # =================================================================

    print("""
  p-1 is B-smooth if all prime factors <= B.
  Smoothness relative to sqrt(p) is the classical boundary.

  For transparency, the relevant notion is: all prime POWERS in p-1
  already appear in lambda. This is "lambda-smooth" rather than B-smooth.
""")

    for threshold_name, threshold_fn in [
        ("sqrt(p)", lambda p: p**0.5),
        ("p^(1/3)", lambda p: p**(1/3)),
        ("log(p)^2", lambda p: log(p)**2),
    ]:
        smooth_and_trans = 0
        smooth_and_not = 0
        rough_and_trans = 0
        rough_and_not = 0

        for t in tower[1:]:
            largest = max(t['pm1_factors'].keys())
            B = threshold_fn(t['p'])
            smooth = (largest <= B)
            if smooth and t['transparent']:
                smooth_and_trans += 1
            elif smooth and not t['transparent']:
                smooth_and_not += 1
            elif not smooth and t['transparent']:
                rough_and_trans += 1
            else:
                rough_and_not += 1

        total = len(tower) - 1
        print(f"  Threshold: lpf(p-1) <= {threshold_name}")
        print(f"    Smooth & transparent:     {smooth_and_trans:>4} ({smooth_and_trans/total*100:.1f}%)")
        print(f"    Smooth & non-transparent: {smooth_and_not:>4} ({smooth_and_not/total*100:.1f}%)")
        print(f"    Rough & transparent:      {rough_and_trans:>4} ({rough_and_trans/total*100:.1f}%)")
        print(f"    Rough & non-transparent:  {rough_and_not:>4} ({rough_and_not/total*100:.1f}%)")
        print()

    # =================================================================
    section("VI. GROWTH OF LAMBDA vs PHI")
    # =================================================================

    print("""
  Lambda grows as phi^alpha for some alpha. What is alpha?
  If alpha < 1, lambda grows slower than phi -- more primes become
  transparent at higher rungs (density could increase).
  If alpha = 1, lambda tracks phi -- density stabilizes.
""")

    print(f"  {'k':>5} {'log2(lam)':>10} {'log2(phi)':>10} {'alpha':>8}")
    print(f"  {'-' * 38}")

    running_phi = 1
    for t in tower:
        running_phi *= (t['p'] - 1) if t['k'] > 1 else 1
        if t['k'] <= 1:
            continue
        if t['lambda'] > 1 and running_phi > 1:
            alpha = log(t['lambda']) / log(running_phi)
            if t['k'] <= 20 or t['k'] % 20 == 0:
                print(f"  {t['k']:>5} {log2(t['lambda']):>10.1f} "
                      f"{log2(running_phi):>10.1f} {alpha:>8.4f}")

    # =================================================================
    section("VII. THEORETICAL PREDICTION")
    # =================================================================

    print("""
  Classical results suggest:
  - Among integers n <= x, the fraction with all prime factors <= x^u
    is rho(1/u) (Dickman function). For u=0.5: rho(2) ~ 0.308.
  - Among {p-1 : p prime, p <= x}, the distribution is more complex
    due to the constraint that p is prime.

  For transparency, we need: every prime POWER q^e in (p-1) already
  appears in lambda = lcm(p_1-1,...,p_{k-1}-1). As k grows, lambda
  accumulates more factors, making transparency easier.

  Key question: does the "accumulated smoothness" of lambda grow fast
  enough to absorb most new p-1 factorizations?

  The prime powers in lambda at rung k:
""")

    milestones = [10, 20, 50, 100, 150, 200]
    for k in milestones:
        if k > K_MAX:
            break
        t = tower[k-1]
        lam_factors = factorize(t['lambda'])
        n_prime_powers = sum(e for e in lam_factors.values())
        max_power = max((q, e) for q, e in lam_factors.items())
        distinct_primes = len(lam_factors)
        print(f"  k={k:>3}: lambda has {distinct_primes} distinct primes, "
              f"{n_prime_powers} total prime powers, "
              f"largest: {max_power[0]}^{max_power[1]}")

    print()

    # =================================================================
    section("VIII. DENSITY EXTRAPOLATION")
    # =================================================================

    print("""
  Fit the density curve to predict limiting behavior.
  Method: look at density in successive windows and check for trend.
""")

    window_size = 20
    densities = []
    for start in range(2, K_MAX + 1, window_size):
        end = min(start + window_size, K_MAX + 1)
        w_trans = sum(1 for t in tower[start-1:end-1] if t['transparent'])
        w_total = end - start
        w_dens = w_trans / w_total if w_total > 0 else 0
        mid = (start + end - 1) / 2
        densities.append((mid, w_dens))

    print(f"  {'window midpoint':>15} {'density':>8}")
    print(f"  {'-' * 28}")
    for mid, d in densities:
        bar = '#' * int(d * 50)
        print(f"  {mid:>15.0f} {d:>8.4f}  {bar}")

    # Linear regression on window densities
    if len(densities) >= 3:
        n = len(densities)
        xs = [mid for mid, _ in densities]
        ys = [d for _, d in densities]
        x_mean = sum(xs) / n
        y_mean = sum(ys) / n
        num = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys))
        den = sum((x - x_mean) ** 2 for x in xs)
        slope = num / den if den > 0 else 0
        intercept = y_mean - slope * x_mean
        print(f"\n  Linear fit: density = {intercept:.4f} + {slope:.6f} * k")
        print(f"  Extrapolated density at k=500: {intercept + slope * 500:.4f}")
        print(f"  Extrapolated density at k=1000: {intercept + slope * 1000:.4f}")

    # Cumulative density trend
    print()
    print("  Cumulative density at milestones:")
    print(f"  {'k':>5} {'density':>8} {'delta from k-50':>15}")
    print(f"  {'-' * 32}")
    prev_d = None
    for k in [10, 20, 30, 40, 50, 75, 100, 125, 150, 175, 200]:
        if k > K_MAX:
            break
        d = tower[k-1]['density']
        delta = f"{d - prev_d:+.4f}" if prev_d is not None else ""
        print(f"  {k:>5} {d:>8.4f} {delta:>15}")
        prev_d = d

    # =================================================================
    section("IX. WHAT PRIME-1 FACTORIZATIONS LOOK LIKE")
    # =================================================================

    print("""
  For each non-transparent prime, what NEW prime factor does p-1 introduce?
  These are the "complexity primes" -- the ones that grow lambda.
""")

    new_prime_intro = Counter()
    for t in tower[1:]:
        if t['transparent']:
            continue
        for q, (old_e, new_e) in t['blocking'].items():
            if old_e == 0:
                new_prime_intro[q] += 1

    print("  Primes that most commonly block transparency (appear as new factor):")
    print(f"  {'blocking prime':>15} {'count':>6}")
    print(f"  {'-' * 25}")
    for q, c in sorted(new_prime_intro.items(), key=lambda x: -x[1])[:20]:
        print(f"  {q:>15} {c:>6}")

    print()
    print(f"  Total distinct primes introduced in p-1 factorizations: "
          f"{len(new_prime_intro)}")
    print(f"  Total non-transparent primes: "
          f"{sum(1 for t in tower[1:] if not t['transparent'])}")

    # =================================================================
    section("X. CONSECUTIVE TRANSPARENT RUNS")
    # =================================================================

    print("""
  Plateaus in lambda correspond to runs of consecutive transparent primes.
  How long are these runs? Do they grow?
""")

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

    print(f"  {'start k':>8} {'length':>8} {'primes':>30}")
    print(f"  {'-' * 50}")

    for start_k, length in sorted(runs, key=lambda x: -x[1])[:15]:
        ps = [tower[k-1]['p'] for k in range(start_k, start_k + length)]
        ps_str = ",".join(str(p) for p in ps[:8])
        if len(ps) > 8:
            ps_str += "..."
        print(f"  {start_k:>8} {length:>8} {ps_str:>30}")

    print(f"\n  Total runs of length >= 2: {sum(1 for _, l in runs if l >= 2)}")
    print(f"  Longest run: {max(l for _, l in runs) if runs else 0}")
    print(f"  Mean run length: {sum(l for _, l in runs) / len(runs):.2f}" if runs else "")

    # =================================================================
    section("XI. KEY FINDINGS")
    # =================================================================

    final_density = tower[-1]['density']
    final_trans = tower[-1]['trans_count']

    print(f"""
  1. DENSITY AT k={K_MAX}: {final_density:.4f} ({final_trans}/{K_MAX-1} primes transparent).

  2. TREND: {'increasing' if tower[-1]['density'] > tower[K_MAX//2-1]['density'] else 'stable/decreasing'}.
     The density at k={K_MAX//2} was {tower[K_MAX//2-1]['density']:.4f}.

  3. WHAT CONTROLS TRANSPARENCY:
     - The largest prime factor of p-1 is the key determinant.
     - Transparent primes have p-1 with small largest factor (already in lambda).
     - Non-transparent primes introduce a new prime (or new power) to lambda.

  4. SIEVE INTERPRETATION:
     Transparency density measures how "self-sufficient" the sieve becomes.
     As the tower grows, lambda accumulates more prime factors, making it
     easier for new p-1 to be fully absorbed. But occasionally a new prime
     introduces a factor that has never appeared before in any p-1, forcing
     a lambda jump.

  5. CONNECTION TO NUMBER THEORY:
     The density question reduces to: among {{p-1 : p prime}}, what fraction
     has all prime power factors already seen in earlier entries of the sequence?
     This is a question about the "novelty rate" of prime factorizations
     in the sequence of shifted primes -- a variant of the smooth-number
     distribution problem, specialized to primes.
""")

    print("=" * 76)
    print("  Done.")
    print("=" * 76)


if __name__ == "__main__":
    main()
