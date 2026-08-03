"""The density of lambda-transparent primes through k=200, and what
actually predicts one.

A prime p_k is lambda-transparent iff (p_k - 1) | lambda(k-1), where
lambda(k-1) = lcm(p_1-1, ..., p_{k-1}-1). In sieve language: adding p_k
to the sieve does not move the period, so p_k is redundant for the
multiplicative dynamics. Equivalently, every prime power in the
factorization of p_k - 1 already appears in lambda(k-1) -- transparency
is smoothness of p_k - 1 relative to the ACCUMULATED shifted-prime
factorizations, which is the definition and not a result.

THE QUESTIONS:
  Q1. What is the density through k=200, and is it still moving?
  Q2. Is the available proxy -- smoothness of p-1 relative to p rather
      than to lambda -- strong enough to be called the determinant? The
      test has to be against the majority-class baseline, since the
      density itself is the accuracy of predicting "transparent" for
      everything, and any weak signal beats a coin without meaning it.
  Q3. Is log(lambda)/log(phi) an independent reading of the same tower,
      or a restatement of Q1?
  Q4. What blocks a non-transparent prime -- a prime new to lambda, or a
      power bump of one already there?

SCOPE. This script computes a trend; it does not settle the limit. That
the density tends to 1 is a theorem proved elsewhere by an elementary
sieve bound on log lcm{p-1 : p <= x}, general in x
(explore_lcm_shifted_primes.py); the trend is charted further by
explore_density_extended.py. The rate is open.

Design: build the tower of the first 200 primes carrying lambda's
factorization as a running exponent map, so transparency is decided per
rung by an exponent comparison and the blocking factors fall out of the
same test. Nothing here is sampled or fitted except the window slope in
section VIII, which is read as a local trend only.

Findings, tiers and their controls: section XI.

Run: python prime/code/explore_asymptotic_density.py  (well under a
second; integers and dicts only, far under the 512MB analysis ceiling)
"""

from math import gcd, log, log2
from crt import is_prime, factorize


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
    print("  ASYMPTOTIC DENSITY OF TRANSPARENCY")
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

    print("""
  CONVENTION AT k=1. p_1 - 1 = 1 and lambda(0) = 1 (the empty lcm), so
  1 | 1 and the criterion as stated calls p_1 = 2 transparent. It is
  counted NON-transparent here and excluded from every density
  denominator: there is no accumulated lambda for it to be transparent
  against, and the degenerate rung would otherwise shift the density by
  1/(k-1). Every rate below is over k = 2..K_MAX.
""")

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

    for start in range(2, K_MAX + 1, window):
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
  Transparency is smoothness of p-1 relative to LAMBDA, by definition.
  The available proxy is smoothness relative to P -- the largest prime
  factor (lpf) of p-1 against p itself. The two are different notions,
  and section V measures how much of the first the second carries.

  Here: does the proxy separate the two classes in MEAN?
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

  A mean gap between two classes is not a mechanism. Read each threshold
  as a CLASSIFIER of transparency and score it against the majority-class
  baseline -- predict "transparent" for everything, which is right at the
  transparency density itself. A threshold worth calling the determinant
  has to beat that.
""")

    n_elig = len(tower) - 1
    n_trans_all = sum(1 for t in tower[1:] if t['transparent'])
    baseline = n_trans_all / n_elig
    print(f"  Majority-class baseline (always predict transparent): "
          f"{baseline*100:.1f}%\n")

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
        acc = (smooth_and_trans + rough_and_not) / total
        print(f"  Threshold: lpf(p-1) <= {threshold_name}")
        print(f"    Smooth & transparent:     {smooth_and_trans:>4} ({smooth_and_trans/total*100:.1f}%)")
        print(f"    Smooth & non-transparent: {smooth_and_not:>4} ({smooth_and_not/total*100:.1f}%)")
        print(f"    Rough & transparent:      {rough_and_trans:>4} ({rough_and_trans/total*100:.1f}%)")
        print(f"    Rough & non-transparent:  {rough_and_not:>4} ({rough_and_not/total*100:.1f}%)")
        print(f"    -> accuracy {acc*100:.1f}%, "
              f"{(acc-baseline)*100:+.1f}pp against baseline; "
              f"{rough_and_trans}/{n_trans_all} "
              f"({rough_and_trans/n_trans_all*100:.1f}%) of transparent "
              f"primes are ROUGH by it")
        print()

    # =================================================================
    section("VI. GROWTH OF LAMBDA vs PHI")
    # =================================================================

    print("""
  Lambda grows as phi^alpha for some alpha. The tempting reading is that
  alpha DRIVES the density -- lambda growing slower than phi leaving more
  room to absorb the next p-1. That reading is backwards, and the column
  beside alpha is why: lambda's log gain on a transparent rung is exactly
  zero, since a transparent p-1 divides lambda already and the lcm does
  not move. So log lambda(k) collects contributions only from the
  NON-transparent rungs, while log phi(k) collects every rung. alpha is
  therefore capped by the non-transparent share of log phi and is pushed
  down BY transparency, not a predictor of it -- a second reading of the
  density, not an independent measurement of it.
""")

    running_phi = 1
    prev_lam = 1
    max_trans_gain = 0.0
    nt_log = 0.0
    cap_holds_at = 0
    worst_slack = None
    print(f"  {'k':>5} {'log2(lam)':>10} {'log2(phi)':>10} {'alpha':>8} "
          f"{'nontrans share':>15}")
    print(f"  {'-' * 54}")
    for t in tower:
        if t['k'] > 1:
            running_phi *= (t['p'] - 1)
            if not t['transparent']:
                nt_log += log(t['p'] - 1)
        if t['transparent']:
            max_trans_gain = max(max_trans_gain,
                                 log(t['lambda']) - log(prev_lam))
        prev_lam = t['lambda']
        if t['k'] <= 1:
            continue
        if t['lambda'] > 1 and running_phi > 1:
            alpha = log(t['lambda']) / log(running_phi)
            share = nt_log / log(running_phi)
            slack = share - alpha
            assert slack >= -1e-12, (t['k'], alpha, share)
            cap_holds_at += 1
            if worst_slack is None or slack < worst_slack[1]:
                worst_slack = (t['k'], slack)
            if t['k'] <= 20 or t['k'] % 20 == 0:
                print(f"  {t['k']:>5} {log2(t['lambda']):>10.1f} "
                      f"{log2(running_phi):>10.1f} {alpha:>8.4f} "
                      f"{share:>15.4f}")

    print(f"\n  Control: lambda's largest log gain over the "
          f"{n_trans_all} transparent rungs = {max_trans_gain:.3e} "
          f"(zero, as the mechanism above requires).")
    print(f"  Cap alpha <= nontrans share ASSERTED at all {cap_holds_at} "
          f"rungs k=2..{K_MAX}, not just the ones tabulated;")
    print(f"  tightest at k={worst_slack[0]}, slack {worst_slack[1]:.4f}. It is "
          f"a property, not a range fact: each")
    print(f"  raise adds log(a prime power dividing p-1) <= log(p-1), so "
          f"log lambda <= the")
    print(f"  non-transparent sum at every k (the domination inequality, "
          f"explore_complexity_ledger.py).")

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
        cross = (1.0 - intercept) / slope if slope > 0 else float('inf')
        print(f"  The slope is positive, and that is all the fit says. A "
              f"density lives in [0, 1],")
        print(f"  so a straight line cannot be its asymptotic form: this "
              f"one reaches 1 at")
        print(f"  k = {cross:.0f} and exceeds it after. The fit is a local "
              f"trend inside the")
        print(f"  window it was taken over, and is NOT extrapolated here.")

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
  For each non-transparent prime, what does p-1 introduce? Two kinds of
  block: a prime NEW to lambda, or a POWER BUMP of a prime already there.

  There is no frequency question here, and asking one is the trap: a
  prime q can block as a new factor at most ONCE in the whole tower,
  since after that rung q sits in lambda permanently. A table of "which
  primes block most often" is all 1s by construction, and would look
  like an answer. The two counts below are what the split actually says.
""")

    new_prime_blocks = 0
    bump_only_blocks = 0
    new_primes_in_order = []
    for t in tower[1:]:
        if t['transparent']:
            continue
        fresh = [q for q, (old_e, _) in t['blocking'].items() if old_e == 0]
        if fresh:
            new_prime_blocks += 1
            new_primes_in_order.extend(sorted(fresh))
        else:
            bump_only_blocks += 1

    n_nontrans = sum(1 for t in tower[1:] if not t['transparent'])
    print(f"  Non-transparent primes:                     {n_nontrans:>4}")
    print(f"    blocked by at least one NEW prime:        "
          f"{new_prime_blocks:>4}")
    print(f"    blocked by a POWER BUMP only:             "
          f"{bump_only_blocks:>4}")
    print(f"  Distinct primes entering lambda as new:     "
          f"{len(set(new_primes_in_order)):>4}")
    print(f"  Repeats among them (must be 0):             "
          f"{len(new_primes_in_order) - len(set(new_primes_in_order)):>4}")
    print()
    print("  The content is the ORDER these enter, not a frequency. First 20:")
    print("   ", ", ".join(str(q) for q in new_primes_in_order[:20]))

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
    half_k = K_MAX // 2
    half_density = tower[half_k - 1]['density']
    trend = 'rising' if final_density > half_density else 'flat or falling'
    n_runs2 = sum(1 for _, l in runs if l >= 2)
    mean_run = sum(l for _, l in runs) / len(runs)
    longest_run = max(l for _, l in runs)

    print(f"""
  1. DENSITY AT k={K_MAX}: {final_density:.4f}
     ({final_trans}/{K_MAX-1} transparent), and still {trend} at the top
     of the range -- it was {half_density:.4f} at k={half_k}. The 50-rung windows
     run 0.48, 0.64, 0.66 and then 0.82 over the last 49.
     Observation, this range only. That it tends to
     1 is a theorem, but not one this script establishes -- the proof is
     an elementary sieve bound on log lcm{{p-1 : p <= x}}, general in x
     and computing at no specific k (explore_lcm_shifted_primes.py).

  2. THE LINEAR FIT CARRIES NO ASYMPTOTIC CONTENT, and the bound is what
     says so. The window fit rises at +0.0021 per rung, which reaches
     density 1 at k = 267 and passes it after; a density lives in [0, 1],
     so a straight line cannot be this sequence's form anywhere near the
     limit. What the fit measures is a local slope inside k <= {K_MAX}. The
     RATE at which the density approaches 1 is exactly what stays open
     (Elliott-Halberstam-hard), so no extrapolation is printed.

  3. WHAT CONTROLS TRANSPARENCY -- the proxy is weaker than it looks.
     Transparency IS smoothness of p-1 relative to lambda; that is the
     definition, not a finding. The measurable proxy is smoothness
     relative to P, and it separates the two classes in MEAN --
     lpf(p-1)/p averages 0.0555 for transparent primes against 0.2858
     for non-transparent. But a mean gap is not a mechanism, and scored
     as a CLASSIFIER against the 64.8% majority-class baseline the proxy
     is thin: at the classical sqrt(p) boundary it reaches 67.3%, +2.5pp,
     with 39.5% of transparent primes ROUGH by it; at p^(1/3) it scores
     45.2%, which is 19.6pp WORSE than predicting "transparent" for
     everything. Only (log p)^2 earns the word determinant, at 75.9%
     (+11.1pp, 20.9% rough-transparent) -- and the threshold that works
     is the polylogarithmic one, not either power of p tested. Pattern,
     k=2..{K_MAX}.

  4. ALPHA IS THE DENSITY READ A SECOND TIME, NOT A PREDICTOR OF IT.
     log(lambda)/log(phi) falls 1.0 -> 0.2282 across the range, and the
     tempting reading -- lambda growing slower than phi leaves room, so
     the density rises -- has the arrow backwards. The control: lambda's
     largest log gain over all {n_trans_all} transparent rungs is exactly
     0.000e+00, since a transparent p-1 already divides lambda and the
     lcm does not move. So log lambda collects contributions only from
     non-transparent rungs while log phi collects every rung, which caps
     alpha by the non-transparent share of log phi -- 0.2282 against
     0.3255 at k={K_MAX}, and the cap is asserted at all {cap_holds_at} rungs, not
     only the tabulated ones. Alpha is pushed down BY transparency.
     PROPERTY, not a range fact, in both halves: the zero gain follows
     from the definition of the lcm, and the cap from each raise adding
     at most log(p-1).
     The corpus already holds this at two other scales, and the reading
     above was the odd one out. explore_complexity_ledger.py proves the
     domination inequality alpha <~ nt_frac rigorously and runs it to
     k=10000; explore_tower_geometry.py finding 6 reads the same ratio's
     fall across k=3..14 and finds every step of it a lambda PLATEAU --
     this mechanism at run length rather than in aggregate.

  5. THE BLOCKING SPLIT, and the frequency question that does not exist.
     Of {n_nontrans} non-transparent primes, {new_prime_blocks} are blocked by a
     prime NEW to lambda and {bump_only_blocks} by a power bump alone.
     A blocking prime can enter
     as new AT MOST ONCE in the whole tower -- once q is in lambda it
     stays -- so "which primes block most often" is all 1s by
     construction and is not a table worth printing; the repeat count
     above is 0 and could not have been anything else. What the blockers
     carry is their ORDER of entry, not a frequency.

  6. RUNS. Transparent rungs come in runs --
     {n_runs2} of length >= 2, mean {mean_run:.2f}, longest
     {longest_run} at k=78..90 (p=397..463). A run is exactly a
     lambda plateau, by finding 4's zero-gain control.

  7. SIEVE READING. The density measures how self-sufficient the sieve
     becomes: lambda accumulates prime powers, and a new p-1 is more
     often absorbed whole. Non-transparent primes are expected never to
     stop appearing -- safe primes p = 2q+1 are reliably non-transparent
     and conjectured infinite -- only to thin, which is all the
     vanishing forces.

  8. CONVENTION. p_1 = 2 satisfies the criterion vacuously (1 | 1) and is
     counted non-transparent throughout; every density here is over
     k = 2..{K_MAX}. See section I.
""")

    print("=" * 76)
    print("  Done.")
    print("=" * 76)


if __name__ == "__main__":
    main()
