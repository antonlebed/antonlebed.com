"""Prime gap structure via lambda.

QUESTION. Walking the tower k=1..500 (p_max = 3571) with
lambda = lcm(p_i - 1): which rungs jump lambda (non-transparent), what
sets the jump size, in what order primes ENTER lambda (the Linnik
ordering), and whether the lambda jump is correlated with the prime gap
p_k - p_{k-1}.

DESIGN. Section I: jump size distribution (top-20 table, log2 buckets).
Section II: new-prime entries vs power bumps, with a per-100-rung window
census (transparent / new-prime / power-bump counts, mean log2(jump)).
Section III: the entry rung E(q) and its log-log fit. Section IV: safe
primes (p-1 = 2q, q prime), with jump == q asserted per row. Section V:
gap vs jump over the full window -- raw Pearson r and the partial r
controlling for k, since both variables grow with the rung. Section VI:
jump complexity (new prime powers per jump).

FINDINGS (k=1..500).
  1. The jump is the entering prime, so jumps grow with the rung: range
     2..1733, the twenty largest all safe primes with jump = (p-1)/2,
     mean log2(jump) rising 4.47 to 9.38 across the census windows.
     (observation)
  2. 123 new-prime jumps vs 18 power bumps; the bumps front-load
     (12, 2, 2, 1, 1 per 100 rungs). (observation)
  3. Entry order fits E(q) ~ q^0.706 here, entry-censored at K_MAX;
     the at-scale windowed fit is ~q^0.96..0.98
     (explore_linnik_injectivity.py). (observation)
  4. Every safe prime is non-transparent with jump exactly q: proved
     (for q > 2 the only candidate p' = 1 mod q below 2q+1 is q+1,
     even; for q = 2 the 2^2 bump at p = 5), asserted at all 55 rows.
     (rule)
  5. Gap vs jump: raw r = 0.330 roughly halves controlling for k
     (partial r = 0.179; both variables grow with the rung,
     r(log2(jump),k) = 0.700). Independence not decided at this
     window. (observation)
  6. Multi-factor jumps are absent at this window: 0 of 141; the wider
     check to k=10^4 agrees (explore_complexity_ledger.py).
     (observation)

Run: python prime/code/explore_prime_gaps.py
Run record: 0.3s, 13.1 MB peak (memwatch).
"""

from math import gcd, log, log2
from collections import Counter, defaultdict
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
    K_MAX = 500

    print("=" * 76)
    print("  PRIME GAP STRUCTURE VIA LAMBDA")
    print("  Jump sizes, complexity spectrum, Artin connection")
    print("=" * 76)

    primes = first_n_primes(K_MAX)
    print(f"\n  Tower k=1..{K_MAX}, p_max={primes[-1]}.")

    tower = []
    running_lcm = 1
    running_lcm_factors = {}

    for k_idx in range(K_MAX):
        k = k_idx + 1
        p = primes[k_idx]
        pm1 = p - 1
        pm1_factors = factorize(pm1)

        prev_lcm = running_lcm
        running_lcm = lcm(running_lcm, pm1)
        jump = running_lcm // prev_lcm if prev_lcm > 0 else running_lcm
        transparent = (jump == 1) and k > 1

        new_factors = {}
        for q, e in pm1_factors.items():
            old_e = running_lcm_factors.get(q, 0)
            if e > old_e:
                new_factors[q] = (old_e, e)

        for q, e in pm1_factors.items():
            running_lcm_factors[q] = max(running_lcm_factors.get(q, 0), e)

        tower.append({
            'k': k, 'p': p, 'pm1': pm1, 'jump': jump,
            'transparent': transparent,
            'new_factors': new_factors,
            'pm1_factors': pm1_factors,
            'lambda': running_lcm,
        })

    # =================================================================
    section("I. JUMP SIZE DISTRIBUTION")
    # =================================================================

    jumps = [(t['k'], t['p'], t['jump']) for t in tower[1:] if not t['transparent']]

    print(f"\n  Non-transparent primes: {len(jumps)} out of {K_MAX-1}")
    print()

    print("  Largest jumps:")
    print(f"  {'k':>5} {'p':>6} {'jump':>15} {'log2(jump)':>12}")
    print(f"  {'-' * 42}")

    for k, p, j in sorted(jumps, key=lambda x: -x[2])[:20]:
        print(f"  {k:>5} {p:>6} {j:>15,} {log2(j):>12.1f}")

    print()
    print("  Jump size distribution (log2 buckets):")
    buckets = defaultdict(int)
    for _, _, j in jumps:
        b = int(log2(j)) if j > 1 else 0
        buckets[b] += 1

    print(f"  {'log2(jump)':>12} {'count':>6}")
    print(f"  {'-' * 22}")
    for b in sorted(buckets):
        print(f"  {b:>12} {buckets[b]:>6}")

    # =================================================================
    section("II. WHAT CAUSES LAMBDA JUMPS?")
    # =================================================================

    print("""
  Each non-transparent prime introduces new prime power(s) to lambda.
  Two types: (a) brand-new prime factor, (b) higher power of existing factor.
""")

    new_prime_jumps = []
    power_bump_jumps = []

    for t in tower[1:]:
        if t['transparent']:
            continue
        has_new = any(old == 0 for old, new in t['new_factors'].values())
        if has_new:
            new_prime_jumps.append(t)
        else:
            power_bump_jumps.append(t)

    print(f"  New prime introductions: {len(new_prime_jumps)}")
    print(f"  Power bumps only: {len(power_bump_jumps)}")
    print()

    print("  Window census (per 100 rungs):")
    print(f"  {'rungs':>12} {'trans':>6} {'new-prime':>10} {'power-bump':>11} "
          f"{'mean log2(jump)':>16}")
    print(f"  {'-' * 60}")
    for lo in range(0, K_MAX, 100):
        win = [t for t in tower[lo:lo + 100] if t['k'] > 1]
        nt = [t for t in win if not t['transparent']]
        n_new = sum(1 for t in nt
                    if any(old == 0 for old, new in t['new_factors'].values()))
        n_bump = len(nt) - n_new
        n_trans = len(win) - len(nt)
        mean_l2 = sum(log2(t['jump']) for t in nt) / len(nt) if nt else 0.0
        print(f"  {lo + 1:>5}-{lo + 100:<6} {n_trans:>6} {n_new:>10} "
              f"{n_bump:>11} {mean_l2:>16.2f}")
    print()

    print("  New primes entering lambda (in order of entry):")
    print(f"  {'k':>5} {'p':>6} {'new q':>8} {'from p-1':>15} {'jump':>12}")
    print(f"  {'-' * 50}")

    new_qs = []
    for t in new_prime_jumps[:40]:
        new_q_list = [q for q, (old, new) in t['new_factors'].items() if old == 0]
        for q in new_q_list:
            new_qs.append((t['k'], t['p'], q, t['jump']))

    for k, p, q, j in new_qs[:40]:
        pm1_str = "*".join(f"{q}^{e}" if e > 1 else str(q)
                          for q, e in sorted(factorize(p-1).items()))
        print(f"  {k:>5} {p:>6} {q:>8} {pm1_str:>15} {j:>12,}")

    # =================================================================
    section("III. THE PRIME ENTRY SEQUENCE")
    # =================================================================

    print("""
  Each prime q eventually enters lambda (via some p with q | (p-1)).
  The ENTRY ORDER of primes into lambda differs from natural order.
  This is the Linnik ordering (explore_lambda_tower.py).

  Key question: how does the entry rung E(q) relate to q?
""")

    entry_rung = {}
    for t in tower:
        for q, (old, new) in t['new_factors'].items():
            if old == 0 and q not in entry_rung:
                entry_rung[q] = (t['k'], t['p'])

    sorted_entries = sorted(entry_rung.items(), key=lambda x: x[1][0])

    print(f"  {'q':>6} {'enters at k':>12} {'via p':>8} {'E(q)/q':>8} {'E(q)/q^2':>10}")
    print(f"  {'-' * 48}")

    for q, (k, p) in sorted_entries[:50]:
        eq_q = k / q if q > 0 else 0
        eq_q2 = k / (q * q) if q > 0 else 0
        print(f"  {q:>6} {k:>12} {p:>8} {eq_q:>8.3f} {eq_q2:>10.6f}")

    # E(q) vs q relationship
    print()
    if len(sorted_entries) >= 10:
        # (q, E(q)) pairs, q > 2. The fit is entry-censored (late
        # entrants beyond K_MAX are missing), which is why it sits far
        # below the at-scale windowed ~0.96-0.98.
        pairs = [(q, k) for q, (k, p) in sorted_entries if q > 2]
        if len(pairs) >= 5:
            log_qs = [log(q) for q, _ in pairs]
            log_es = [log(k) for _, k in pairs]
            n = len(pairs)
            x_mean = sum(log_qs[:n]) / n
            y_mean = sum(log_es[:n]) / n
            num = sum((x - x_mean) * (y - y_mean) for x, y in zip(log_qs[:n], log_es[:n]))
            den = sum((x - x_mean) ** 2 for x in log_qs[:n])
            slope = num / den if den > 0 else 0
            print(f"  Power law fit: E(q) ~ q^{slope:.3f}")
            print(f"  (Linnik's theorem guarantees E(q) <= C*q^L with L ~ 5;")
            print(f"   sample censored at K_MAX -- the at-scale windowed fit")
            print(f"   lives in explore_linnik_injectivity.py)")

    # =================================================================
    section("IV. ARTIN'S CONJECTURE CONNECTION")
    # =================================================================

    print("""
  Artin's conjecture: for any non-square integer a != -1, there are
  infinitely many primes p where a is a primitive root mod p.

  Connection to lambda: if 2 is a primitive root mod p, then p-1 is
  the order of 2 mod p, which means p-1 has specific structure.

  For a safe prime (p-1 = 2q, q prime) with q odd, the 2-part of p-1 is
  2^1, in lambda from k=2, so p is transparent iff q is. That is
  impossible below p: a prime p' with q | p'-1 satisfies p' = 1 (mod q),
  and the only candidate below 2q+1 is q+1, which is even. For q = 2
  (p = 5), 2 is in lambda but p-1 = 4 forces the 2^2 bump. So every
  safe prime is non-transparent with jump exactly q -- proved, and
  asserted per row below.
""")

    safe_prime_count = 0
    safe_and_nontrans = 0

    for t in tower[1:]:
        pm1 = t['pm1']
        if pm1 % 2 == 0:
            q = pm1 // 2
            if is_prime(q):
                safe_prime_count += 1
                assert not t['transparent'] and t['jump'] == q, \
                    (t['k'], t['p'], t['jump'], q)
                if not t['transparent']:
                    safe_and_nontrans += 1

    print(f"  Safe primes in k=2..{K_MAX}: {safe_prime_count}")
    print(f"  Safe AND non-transparent: {safe_and_nontrans}")
    print(f"  Safe AND transparent: {safe_prime_count - safe_and_nontrans}")
    print(f"  jump == q asserted at all {safe_prime_count} rows.")
    print()
    print("  Safe primes and their behavior:")
    print(f"  {'k':>5} {'p':>6} {'q=(p-1)/2':>12} {'trans':>6} {'jump':>12}")
    print(f"  {'-' * 45}")

    shown = 0
    for t in tower[1:]:
        pm1 = t['pm1']
        if pm1 % 2 == 0:
            q = pm1 // 2
            if is_prime(q) and shown < 25:
                tr = "YES" if t['transparent'] else ""
                print(f"  {t['k']:>5} {t['p']:>6} {q:>12} {tr:>6} {t['jump']:>12,}")
                shown += 1


    # =================================================================
    section("V. PRIME GAP AND JUMP CORRELATION")
    # =================================================================

    print("""
  Is there a relationship between prime gaps (p_k - p_{k-1}) and
  lambda jumps? Large gaps might correspond to primes with unusual
  p-1 factorizations.
""")

    print(f"  {'k':>5} {'p':>6} {'gap':>5} {'jump':>12} {'trans':>5}")
    print(f"  {'-' * 38}")

    gaps_and_jumps = []
    for i in range(1, K_MAX):
        gap = tower[i]['p'] - tower[i-1]['p']
        jump = tower[i]['jump']
        gaps_and_jumps.append((gap, jump, tower[i]['transparent']))
        if i <= 30 or gap >= 20:
            tr = "YES" if tower[i]['transparent'] else ""
            print(f"  {tower[i]['k']:>5} {tower[i]['p']:>6} {gap:>5} "
                  f"{jump:>12,} {tr:>5}")

    trans_gaps = [g for g, j, t in gaps_and_jumps if t]
    nontrans_gaps = [g for g, j, t in gaps_and_jumps if not t]
    print(f"\n  Over the full window k=2..{K_MAX}:")
    print(f"  Mean gap for transparent primes: {sum(trans_gaps)/len(trans_gaps):.2f}"
          f"  (n={len(trans_gaps)})")
    print(f"  Mean gap for non-transparent primes: {sum(nontrans_gaps)/len(nontrans_gaps):.2f}"
          f"  (n={len(nontrans_gaps)})")

    # The decider: Pearson r between the gap and log2(jump) over the
    # non-transparent rungs (jump > 1, so log2 is finite). Both grow
    # with the rung (the gap ~ log p, the jump ~ the entering prime),
    # so the raw r is confounded by k; the partial r controlling for k
    # is what decides independence beyond the shared growth.
    def pearson(xs, ys):
        n = len(xs)
        xm = sum(xs) / n
        ym = sum(ys) / n
        num = sum((x - xm) * (y - ym) for x, y in zip(xs, ys))
        dx = sum((x - xm) ** 2 for x in xs) ** 0.5
        dy = sum((y - ym) ** 2 for y in ys) ** 0.5
        return num / (dx * dy) if dx > 0 and dy > 0 else 0.0

    nt_rows = [(i + 2, g, log2(j))
               for i, (g, j, t) in enumerate(gaps_and_jumps) if not t]
    ks = [k for k, _, _ in nt_rows]
    gs = [g for _, g, _ in nt_rows]
    ls = [l for _, _, l in nt_rows]
    r_gj = pearson(gs, ls)
    r_gk = pearson(gs, ks)
    r_jk = pearson(ls, ks)
    denom = ((1 - r_gk ** 2) * (1 - r_jk ** 2)) ** 0.5
    r_partial = (r_gj - r_gk * r_jk) / denom if denom > 0 else 0.0
    print(f"  Pearson r, gap vs log2(jump), non-transparent rungs "
          f"(n={len(nt_rows)}): {r_gj:.3f}")
    print(f"  r(gap, k) = {r_gk:.3f}, r(log2(jump), k) = {r_jk:.3f}")
    print(f"  Partial r, gap vs log2(jump) controlling for k: {r_partial:.3f}")

    # =================================================================
    section("VI. COMPLEXITY SPECTRUM")
    # =================================================================

    print("""
  The "complexity" of a lambda jump = number of new prime power factors
  it introduces. How common are multi-factor jumps?
""")

    complexity = Counter()
    for t in tower[1:]:
        if not t['transparent']:
            c = len(t['new_factors'])
            complexity[c] += 1

    print(f"  {'new factors':>12} {'count':>6} {'fraction':>10}")
    print(f"  {'-' * 32}")
    total_nt = sum(complexity.values())
    for c in sorted(complexity):
        print(f"  {c:>12} {complexity[c]:>6} {complexity[c]/total_nt:>10.3f}")
    multi = sum(v for c, v in complexity.items() if c > 1)
    print(f"\n  Multi-factor jumps at this window: {multi} of {total_nt}")

    # =================================================================
    section("VII. KEY FINDINGS")
    # =================================================================

    print(f"""
  1. THE JUMP IS THE ENTERING PRIME, SO JUMPS GROW WITH THE RUNG.
     Range at this window: 2 to 1,733 (k=486, p=3467). The twenty
     largest jumps are all safe primes with jump = (p-1)/2, the log2
     buckets climb (36 jumps below log2=6 against 105 at 6..10), and
     the window census's mean log2(jump) rises 4.47 to 9.38. The
     distribution tracks the entering primes' sizes; there is no
     stationary most-jumps-small law at this window. (observation)

  2. NEW PRIMES DOMINATE POWER BUMPS, AND THE BUMPS FRONT-LOAD.
     {len(new_prime_jumps)} jumps from new primes vs {len(power_bump_jumps)} from power bumps; the census
     prints bumps 12, 2, 2, 1, 1 per 100 rungs while new-prime entries
     hold near 19-32 per window. Each new prime enters lambda exactly
     once. (observation)

  3. ENTRY ORDER FOLLOWS A POWER LAW -- NEAR-LINEAR AT SCALE.
     The global fit at this horizon prints ~0.71, but the sample is
     entry-censored (primes that enter past K_MAX are missing); the
     uncensored windowed fit at scale is E(q) ~ q^0.96..0.98
     (explore_linnik_injectivity.py). Far below the Linnik worst
     case E(q) <= C*q^L. (observation)

  4. EVERY SAFE PRIME IS NON-TRANSPARENT, WITH JUMP EXACTLY q.
     Proved: for q > 2 no prime = 1 (mod q) exists below 2q+1 (the only
     candidate q+1 is even), so q cannot be in lambda before p; for
     q = 2 (p = 5), p-1 = 4 forces the 2^2 bump. Asserted at all 55
     safe primes in the window. Safe primes are conjectured infinite,
     so conditionally the non-transparent rungs never stop. (rule,
     proved + asserted k=2..500)

  5. GAP VS JUMP: CONTROLLING FOR THE RUNG ROUGHLY HALVES THE CORRELATION.
     Raw Pearson r = 0.330 over the 141 non-transparent rungs, but both
     variables grow with k (r(gap,k) = 0.297, r(log2(jump),k) = 0.700);
     the partial r controlling for k is 0.179 -- a weak residual
     association. Independence is not decided at this window; mean gaps
     7.18 (transparent) vs 7.09 (non-transparent). (observation)

  6. MULTI-FACTOR JUMPS ARE ABSENT AT THIS WINDOW: 0 OF 141.
     Every non-transparent rung introduces exactly one new prime power.
     The wider check runs to k=10^4 with the same result
     (explore_complexity_ledger.py); whether a multi-factor jump ever
     occurs is open. (observation; settled much further since — the
     record search certifies none for every p <= 10^16, and the
     question stays open only beyond that: explore_double_birth.py)

  7. GAPS CONNECT TO DENSITY.
     The window census's non-transparent count settles near 20-26 per
     100 rungs after the first window's 44; the decreasing fraction at
     scale is the density record's subject
     (explore_asymptotic_density.py). Both measure the sieve's growing
     vocabulary of prime factors. (observation)
""")

    print("=" * 76)
    print("  Done.")
    print("=" * 76)


if __name__ == "__main__":
    main()
