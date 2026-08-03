"""Cross-thread: seed-flower at plateau vs jump.

Links the lambda/transparency sequence (explore_lambda_tower.py) with
seed-flower naming (explore_seed_flower_k8.py).

Three questions:
  Q1: Does transparency correlate with 2-prime prediction count?
  Q2: Does transparency affect 3-prime naming fraction at each rung?
  Q3: Are transparent primes easier or harder to name as targets?

Discovery: the reciprocal naming criterion.
  s | -chi({p_1,...,p_m}) iff sum(p_i^{-1}) = m-1 (mod s)

Run: python prime/code/explore_tower_naming.py
"""

import sys
sys.path.insert(0, '.')
from itertools import combinations
from math import prod, gcd
from collections import Counter
from prime.code.crt import factorize, is_prime


def first_n_primes(n):
    ps = []
    c = 2
    while len(ps) < n:
        if is_prime(c):
            ps.append(c)
        c += 1
    return ps


def lcm(a, b):
    return a * b // gcd(a, b)


def neg_chi_3(p, q, r):
    return 2 * p * q * r - p * q - p * r - q * r


def neg_chi(ps):
    k = len(ps)
    N = prod(ps)
    return N * (k - 1) - sum(N // p for p in ps)


def section(title):
    print(f"\n{'=' * 76}")
    print(f"  {title}")
    print(f"{'=' * 76}")


def main():
    K_MAX = 50
    primes = first_n_primes(K_MAX)

    print("=" * 76)
    print("  SEED-FLOWER AT PLATEAU VS JUMP")
    print("  Cross-thread: transparency x naming")
    print("=" * 76)
    print(f"\n  Tower: k=1..{K_MAX}, primes 2..{primes[-1]}.")

    tower = []
    running_lam = 1
    for k in range(K_MAX):
        p = primes[k]
        prev = running_lam
        running_lam = lcm(running_lam, p - 1)
        jump = running_lam // prev
        trans = (jump == 1) and k > 0
        tower.append({'k': k + 1, 'p': p, 'lam': running_lam,
                       'jump': jump, 'trans': trans})

    trans_set = {t['p'] for t in tower if t['trans']}

    # =================================================================
    section("I. RECIPROCAL NAMING CRITERION")
    # =================================================================

    print("""
  THEOREM. For thin sub-ring {p_1,...,p_m}, absent prime s divides -chi iff

      p_1^{-1} + ... + p_m^{-1}  =  m - 1   (mod s)

  Proof. -chi = N*(m-1) - sum(N/p_i).  Since s is absent and all p_i
  are distinct primes, gcd(N,s)=1.  Dividing by N (mod s):
  s | -chi iff (m-1) = sum(p_i^{-1}) (mod s), where N/p_i * N^{-1}
  = p_i^{-1}.   QED.

  Special cases:
    m=2: {p,q} names s iff 1/p + 1/q = 1  (mod s)
    m=3: {p,q,r} names s iff 1/p + 1/q + 1/r = 2  (mod s)

  Corollary (2-invisibility): for odd-only sub-rings, each 1/p_i = 1 (mod 2),
  so sum = m (mod 2).  Need m-1 (mod 2).  m != m-1, so 2 is never named.
""")

    ps8 = primes[:8]
    mismatches = 0
    checks = 0
    for size in range(2, 9):
        for combo in combinations(ps8, size):
            nc = neg_chi(list(combo))
            for s in ps8:
                if s in combo:
                    continue
                checks += 1
                brute = (nc % s == 0)
                inv_sum = sum(pow(p, -1, s) for p in combo) % s
                criterion = (inv_sum == (size - 1) % s)
                if brute != criterion:
                    mismatches += 1
    print(f"  Verified at k=8: {checks} checks, {mismatches} mismatches.")

    # =================================================================
    section("II. Q1 -- 2-PRIME PREDICTIONS VS TRANSPARENCY")
    # =================================================================

    print("""
  The factorization theorem: new_preds(k) = twin(p_k) + #factorizations.
  Does transparency correlate with the count of new predictions?
""")

    print(f"  {'k':>3} {'p':>4} {'trans':>5} {'twin':>5} {'#fac':>5} {'new':>4} {'cum':>5}")
    print(f"  {'-'*42}")

    cum_preds = 0
    trans_new = []
    nontrans_new = []

    for k_idx in range(2, K_MAX):
        k = k_idx + 1
        t = tower[k_idx]
        pk = t['p']
        prev_ps = set(primes[:k - 1])

        twin_val = 1 if is_prime(pk - 2) and pk - 2 >= 2 else 0
        target = pk + 1
        facts = []
        for a in range(1, int(target**0.5) + 1):
            if target % a == 0:
                bv = target // a
                if (a + 1) in prev_ps and (bv + 1) in prev_ps:
                    facts.append((a + 1, bv + 1))
        new_count = twin_val + len(facts)
        cum_preds += new_count

        tr = "YES" if t['trans'] else ""
        if k <= 30 or k % 10 == 0:
            print(f"  {k:>3} {pk:>4} {tr:>5} {twin_val:>5} {len(facts):>5} "
                  f"{new_count:>4} {cum_preds:>5}")

        if t['trans']:
            trans_new.append(new_count)
        else:
            nontrans_new.append(new_count)

    print()
    avg_t = sum(trans_new) / len(trans_new) if trans_new else 0
    avg_nt = sum(nontrans_new) / len(nontrans_new) if nontrans_new else 0
    med_t = sorted(trans_new)[len(trans_new) // 2] if trans_new else 0
    med_nt = sorted(nontrans_new)[len(nontrans_new) // 2] if nontrans_new else 0
    print(f"  Transparent rungs:     n={len(trans_new):>2}, "
          f"avg={avg_t:.2f}, median={med_t}")
    print(f"  Non-transparent rungs: n={len(nontrans_new):>2}, "
          f"avg={avg_nt:.2f}, median={med_nt}")

    # =================================================================
    section("III. Q2 -- 3-PRIME NAMING FRACTION PER RUNG")
    # =================================================================

    print("""
  For each rung k: of C(k,3) 3-prime sub-rings, what fraction names
  at least one absent tower prime?  Flag transparent rungs.
""")

    print(f"  {'k':>3} {'p_k':>4} {'T':>2} {'C(k,3)':>7} {'naming':>7} "
          f"{'frac':>7} {'new_3':>6} {'p_k named by':>12}")
    print(f"  {'-'*60}")

    trans_fracs = []
    nontrans_fracs = []

    for k in range(3, K_MAX + 1):
        ps_k = primes[:k]
        ps_set = set(ps_k)
        t = tower[k - 1]
        pk = t['p']

        naming_count = 0
        total_count = 0
        pk_named_by = 0

        for combo in combinations(ps_k, 3):
            total_count += 1
            nc = neg_chi_3(combo[0], combo[1], combo[2])
            absent = [s for s in ps_k if s not in combo]
            if any(nc % s == 0 for s in absent):
                naming_count += 1
            if pk not in combo and nc % pk == 0:
                pk_named_by += 1

        frac = naming_count / total_count
        tr = "*" if t['trans'] else ""

        # Count new triples involving p_k
        new_triples_with_pk = len(list(combinations(primes[:k - 1], 2)))
        pk_triples_not_containing = len(list(combinations(primes[:k - 1], 3)))

        if k <= 30 or k % 5 == 0:
            print(f"  {k:>3} {pk:>4} {tr:>2} {total_count:>7} {naming_count:>7} "
                  f"{frac:>7.3f} {new_triples_with_pk:>6} "
                  f"{pk_named_by}/{pk_triples_not_containing}")

        if k >= 4:
            if t['trans']:
                trans_fracs.append(frac)
            else:
                nontrans_fracs.append(frac)

    print()
    avg_tf = sum(trans_fracs) / len(trans_fracs) if trans_fracs else 0
    avg_nf = sum(nontrans_fracs) / len(nontrans_fracs) if nontrans_fracs else 0
    print(f"  Transparent rungs (k>=4): n={len(trans_fracs):>2}, "
          f"avg naming frac = {avg_tf:.4f}")
    print(f"  Non-transparent rungs:    n={len(nontrans_fracs):>2}, "
          f"avg naming frac = {avg_nf:.4f}")

    # =================================================================
    section("IV. Q3 -- TRANSPARENT VS NON-TRANSPARENT AS TARGETS")
    # =================================================================

    print("""
  For each tower prime s at rung k=25: what fraction of 3-prime sub-rings
  (not containing s) have s | -chi?  Compare to 1/s baseline.
""")

    k_check = 25
    ps_k = primes[:k_check]

    print(f"  {'prime':>6} {'trans':>5} {'named_by':>8} {'possible':>8} "
          f"{'actual':>8} {'1/s':>8} {'ratio':>8}")
    print(f"  {'-'*58}")

    trans_ratios = []
    nontrans_ratios = []

    for s in ps_k:
        others = [p for p in ps_k if p != s]
        named = 0
        total = 0
        for combo in combinations(others, 3):
            total += 1
            nc = neg_chi_3(combo[0], combo[1], combo[2])
            if nc % s == 0:
                named += 1
        actual = named / total if total else 0
        baseline = 1.0 / s
        ratio = actual / baseline if baseline > 0 else 0
        tr = "YES" if s in trans_set else ""
        print(f"  {s:>6} {tr:>5} {named:>8} {total:>8} "
              f"{actual:>8.4f} {baseline:>8.4f} {ratio:>8.2f}")

        if s == 2:
            continue  # 2 is invisible, skip for averages
        if s in trans_set:
            trans_ratios.append(ratio)
        else:
            nontrans_ratios.append(ratio)

    print()
    avg_tr = sum(trans_ratios) / len(trans_ratios) if trans_ratios else 0
    avg_nr = sum(nontrans_ratios) / len(nontrans_ratios) if nontrans_ratios else 0
    print(f"  Transparent targets:     avg actual/baseline = {avg_tr:.2f}")
    print(f"  Non-transparent targets: avg actual/baseline = {avg_nr:.2f}")
    print(f"  (Ratio = 1.0 means naming matches random expectation)")

    # =================================================================
    section("V. NAMING FRACTION BY PRIME SIZE AND TRANSPARENCY")
    # =================================================================

    print("""
  At k=25: for each tower prime s, the expected naming fraction is ~1/s
  (if reciprocal sums were uniform mod s).  The DEVIATION from 1/s is:
    delta(s) = actual_frac - 1/s

  Positive delta = named more than random.  Negative = less.
""")

    print(f"  {'s':>4} {'trans':>5} {'actual':>8} {'1/s':>8} "
          f"{'delta':>8} {'direction':>10}")
    print(f"  {'-'*50}")

    for s in ps_k:
        if s == 2:
            continue
        others = [p for p in ps_k if p != s]
        named = sum(1 for combo in combinations(others, 3)
                    if neg_chi_3(*combo) % s == 0)
        total = len(list(combinations(others, 3)))
        actual = named / total
        baseline = 1.0 / s
        delta = actual - baseline
        tr = "YES" if s in trans_set else ""
        direction = "+" if delta > 0.001 else ("-" if delta < -0.001 else "~")
        print(f"  {s:>4} {tr:>5} {actual:>8.4f} {baseline:>8.4f} "
              f"{delta:>+8.4f} {direction:>10}")

    # =================================================================
    section("VI. WHICH 3-PRIME TRIPLES NAME WHICH PRIMES? (k=8)")
    # =================================================================

    print("""
  The 30/56 naming fraction at k=8.  Using the reciprocal criterion:
    {a,b,c} names s iff 1/a + 1/b + 1/c = 2 (mod s).
""")

    NAMES = {p: str(p) for p in [2, 3, 5, 7, 11, 13, 17, 19]}

    naming_triples = []
    non_naming = []

    for combo in combinations(ps8, 3):
        nc = neg_chi_3(*combo)
        absent = [s for s in ps8 if s not in combo]
        named = [s for s in absent if nc % s == 0]
        label = "{" + ",".join(NAMES[p] for p in combo) + "}"
        if named:
            naming_triples.append((combo, nc, named))
        else:
            non_naming.append((combo, nc))

    print(f"  Naming triples ({len(naming_triples)}/56):")
    for combo, nc, named in naming_triples:
        label = "{" + ",".join(NAMES[p] for p in combo) + "}"
        named_str = ",".join(NAMES[s] for s in named)
        f = factorize(abs(nc))
        fs = "*".join(
            (NAMES.get(p, str(p)) if e == 1
             else f"{NAMES.get(p, str(p))}^{e}")
            for p, e in sorted(f.items())
        ) if f else "1"
        print(f"    {label:<16} -chi = {nc:>8} = {fs:<20} names: {named_str}")

    print(f"\n  Non-naming triples ({len(non_naming)}/56):")
    for combo, nc in non_naming[:10]:
        label = "{" + ",".join(NAMES[p] for p in combo) + "}"
        f = factorize(abs(nc))
        fs = "*".join(
            (NAMES.get(p, str(p)) if e == 1
             else f"{NAMES.get(p, str(p))}^{e}")
            for p, e in sorted(f.items())
        ) if f else "1"
        print(f"    {label:<16} -chi = {nc:>8} = {fs:<20}")
    if len(non_naming) > 10:
        print(f"    ... ({len(non_naming) - 10} more)")

    # Structure of naming: which primes are named how often at k=8?
    print(f"\n  Naming frequency at k=8 (3-prime sub-rings only):")
    freq = Counter()
    for combo, nc, named in naming_triples:
        for s in named:
            freq[s] += 1
    for s in ps8:
        possible = len([c for c in combinations(ps8, 3) if s not in c])
        count = freq.get(s, 0)
        tr = "YES" if s in trans_set else ""
        baseline_expected = possible / s
        print(f"    p={s:<2}: named {count:>3}/{possible} "
              f"(expected ~{baseline_expected:.1f} from 1/s)  trans={tr}")

    # =================================================================
    section("VII. NAMING AT PLATEAU VS JUMP TRANSITIONS")
    # =================================================================

    print("""
  The tower has two growth modes:
    JUMP:    lambda increases (non-transparent prime adds complexity)
    PLATEAU: lambda stays constant (transparent prime adds capacity)

  At each transition, how does the naming landscape change?
  Focus: k=9..14 (the first extended plateau at k=10..14).
""")

    for k in range(9, 15):
        ps_k = primes[:k]
        t = tower[k - 1]
        pk = t['p']
        tr = "PLAT" if t['trans'] else "JUMP"

        total = 0
        naming = 0
        pk_as_target = 0
        pk_possible = 0

        for combo in combinations(ps_k, 3):
            total += 1
            nc = neg_chi_3(*combo)
            absent = [s for s in ps_k if s not in combo]
            if any(nc % s == 0 for s in absent):
                naming += 1
            if pk not in combo:
                pk_possible += 1
                if nc % pk == 0:
                    pk_as_target += 1

        frac = naming / total
        pk_frac = pk_as_target / pk_possible if pk_possible else 0
        pk_baseline = 1.0 / pk

        print(f"  k={k:>2} p={pk:>3} [{tr}] lambda={t['lam']:>10,}  "
              f"naming: {naming}/{total} = {frac:.3f}  "
              f"p_k target: {pk_as_target}/{pk_possible} = {pk_frac:.4f} "
              f"(1/p = {pk_baseline:.4f})")

    # =================================================================
    section("VIII. 3-DOMINANCE VIA CHEBYSHEV BIAS")
    # =================================================================

    print("""
  p=3 is over-named because of the distribution of tower primes mod 3.

  The naming condition for K is: sum(1/p_i) = 2 (mod 3).
  Since 1/p mod 3 = 1 if p=1(mod3), 2 if p=2(mod3), the sum = 2 (mod 3)
  iff exactly 2 of the 3 primes have p=2(mod3) and 1 has p=1(mod3).

  Naming fraction = C(r2,2)*C(r1,1) / C(r1+r2,3)
  where r2 = #{tower primes = 2 mod 3}, r1 = #{tower primes = 1 mod 3}.
""")

    from math import comb

    for n in [8, 15, 25, 50]:
        others = [p for p in primes[:n] if p != 3]
        r2 = sum(1 for p in others if p % 3 == 2)
        r1 = sum(1 for p in others if p % 3 == 1)
        m = len(others)
        predicted = comb(r2, 2) * comb(r1, 1) / comb(m, 3) if comb(m, 3) else 0
        print(f"  k={n:>2}: r2={r2:>2}, r1={r1:>2}, "
              f"predicted={predicted:.4f}, baseline 1/3={1/3:.4f}")

    print("""
  Converges to 1/3 as k->inf (Dirichlet equidistribution), but the
  Chebyshev prime race bias (more primes = 2 mod 3 among small primes)
  makes K over-named at every finite rung.
""")

    # =================================================================
    section("IX. KEY FINDINGS")
    # =================================================================

    print("""
  1. RECIPROCAL NAMING CRITERION (new theorem, proved).
     s | -chi({p_1,...,p_m}) iff sum(p_i^{-1}) = m-1 (mod s).
     Verified 960/960 at k=8. Unifies all naming conditions.
     Corollary: 2-invisibility (immediate from parity argument).

  2. THREADS 1 AND 2 ARE INDEPENDENT.
     Q1: Transparency does NOT affect 2-prime prediction count.
         Both transparent and non-transparent rungs: avg = 0.96/rung.
     Q2: the 3-prime naming fraction DOES read higher at transparent
         rungs -- 0.7346 against 0.6963 averaged over k>=4 -- and that
         gap is position, not transparency.  The fraction climbs with k
         over the whole range printed above (0.000 at k=3 to 0.794 at
         k=50, rising in trend and not at every step -- k=11, 12, 17,
         21, 22, 25 and 29 each read below their predecessor) and the
         transparent rungs sit later in the tower, so any statistic
         averaging over them without controlling for k inherits the
         trend.  The comparison as run cannot separate the two.
     Q3: Naming targets track the 1/s baseline regardless of transparency.
         Avg actual/baseline: 1.05 (trans) vs 1.04 (non-trans).
     Lambda-transparency and seed-flower naming measure DIFFERENT
     properties of the tower. They are largely independent.

  3. NO TOWER-SPECIFIC PROPERTY ENTERS NAMING.
     The naming frequency of an absent s tracks 1/s, and the deviations
     come from finite-sample residue bias (Chebyshev), not from
     transparency, plateaus, or any other tower quantity -- which is what
     the tables above measure and all they measure.
     WHAT SETS THE FREQUENCY IS THE RESIDUE, NOT THE SIZE
     (explore_naming_complex.py, settling a reading this section first
     stated the other way): the criterion is a sum of weights 1 - p^{-1}
     depending on p mod s alone, so a member = 1 mod s is invisible
     whatever its size, and the 1/s figure is a character-sum bound
     rather than a Bayesian prior.  The Chebyshev reading of the
     deviation stands unchanged.

  4. 3-DOMINANCE EXPLAINED.
     p=3 is named by 18/35 triples at k=8 (vs 11.7 expected from 1/3).
     Exact formula: C(r2,2)*C(r1,1)/C(k-1,3) where r2,r1 are counts of
     tower primes = 2,1 mod 3. The Chebyshev prime race bias (more small
     primes = 2 mod 3) creates persistent p=3 over-representation.

  5. 30/56 AT k=8 DECOMPOSED.
     Naming triples = those where at least one absent prime s divides
     -chi = 2pqr - pq - pr - qr. Non-naming triples mostly have PRIME
     -chi (e.g. {2,3,5}->29, {2,3,7}->43, {2,3,11}->71). When -chi
     is prime and not in the tower set, no tower prime can divide it.
""")

    print("=" * 76)
    print("  Done.")
    print("=" * 76)


if __name__ == "__main__":
    main()
