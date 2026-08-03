"""Davenport constant and EGZ — when does subset-sum coverage become complete?

An extension of an earlier finding: missed primes are subset-sum failures in Z/s:
a prime s is missed at rung k iff {p_i^{-1} mod s : i=1..k} has no subset
summing to |S|-1 mod s. The random model P(miss) ~ (1-1/s)^(2^k-1) matches the
observed miss rates within sampling noise at every measured rung
(explore_missed_primes.py carries the per-rung comparison).

Question: how does this connect to the Davenport constant D(Z/n) = n and
the Erdos-Ginzburg-Ziv (EGZ) theorem?

EGZ: any 2n-1 integers contain an n-element subset summing to 0 mod n.
Davenport: D(Z/n) = n — the smallest d such that any d elements of Z/n
contain a non-empty zero-sum subsequence.

Our setup: k values in Z/s, all 2^k-1 non-empty subsets checked. Coverage
transitions from partial to complete around 2^k ~ s (i.e., k ~ log_2(s)).
This script maps the exact transition and its relationship to D(Z/s).

Run: python prime/code/explore_davenport_egz.py
"""

from math import prod, log2, gcd
from itertools import combinations
from collections import defaultdict
from crt import is_prime, factorize


def section(title):
    print(f"\n{'=' * 72}")
    print(f"  {title}")
    print(f"{'=' * 72}")


def first_n_primes(n):
    primes = []
    c = 2
    while len(primes) < n:
        if is_prime(c):
            primes.append(c)
        c += 1
    return primes


def mod_inv(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        return None
    return x % m


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    return g, y1 - (b // a) * x1, x1


def subset_sum_coverage(values, modulus):
    """Compute the set of all non-empty subset sums of values in Z/modulus."""
    covered = set()
    n = len(values)
    for size in range(1, n + 1):
        for subset in combinations(values, size):
            covered.add(sum(subset) % modulus)
    return covered


def subset_sum_coverage_by_size(values, modulus):
    """Compute subset sums grouped by subset size."""
    by_size = defaultdict(set)
    n = len(values)
    for size in range(1, n + 1):
        for subset in combinations(values, size):
            by_size[size].add(sum(subset) % modulus)
    return by_size


ALL_PRIMES = first_n_primes(300)


# ═══════════════════════════════════════════════════════════════════════
# I. COVERAGE THRESHOLD — WHEN DOES Z/s GET FULLY COVERED?
# ═══════════════════════════════════════════════════════════════════════

section("I. COVERAGE THRESHOLD — WHEN DOES Z/s GET FULLY COVERED?")

print("""
  For each prime s in [73..200] (below 73, s is a tower prime at k=20), find the smallest rung k such that
  the subset sums of {p_i^{-1} mod s : i=1..k} cover ALL of Z/s.
  Compare to log_2(s) — the point where 2^k = s.
""")

K_SCAN = 20

print(f"  {'s':>5} {'k_full':>7} {'log2(s)':>8} {'ratio':>7} {'2^k_full':>9} {'s':>6}")
print(f"  {'-'*50}")

thresholds = []
for idx in range(8, 80):  # primes from ~19 to ~200
    s = ALL_PRIMES[idx]
    if s > 200:
        break

    tower_primes = ALL_PRIMES[:K_SCAN]
    if s in tower_primes:
        continue

    k_full = None
    for k in range(2, K_SCAN + 1):
        ps = tower_primes[:k]
        if s in ps:
            continue
        invs = []
        for p in ps:
            inv = mod_inv(p, s)
            if inv is None:
                break
            invs.append(inv)
        if len(invs) != k:
            continue

        covered = subset_sum_coverage(invs, s)
        if len(covered) == s:
            k_full = k
            break

    if k_full is not None:
        ratio = k_full / log2(s)
        thresholds.append((s, k_full, log2(s), ratio))
        print(f"  {s:>5} {k_full:>7} {log2(s):>8.2f} {ratio:>7.2f} {2**k_full:>9} {s:>6}")
    else:
        print(f"  {s:>5} {'>'+str(K_SCAN):>7} {log2(s):>8.2f} {'?':>7}")

if thresholds:
    avg_ratio = sum(r for _, _, _, r in thresholds) / len(thresholds)
    min_ratio = min(r for _, _, _, r in thresholds)
    max_ratio = max(r for _, _, _, r in thresholds)
    print(f"\n  Ratio k_full / log2(s):  mean={avg_ratio:.3f}  "
          f"min={min_ratio:.3f}  max={max_ratio:.3f}")
    print(f"  ({len(thresholds)} primes measured)")


# ═══════════════════════════════════════════════════════════════════════
# II. THE TRANSITION ZONE — PARTIAL TO FULL COVERAGE
# ═══════════════════════════════════════════════════════════════════════

section("II. THE TRANSITION ZONE — PARTIAL TO FULL COVERAGE")

print("""
  For s=41 (the earlier case study), track coverage fraction at each rung.
  The transition should be sharp around k ~ log_2(41) ~ 5.4.
""")

s = 41
tower_primes = ALL_PRIMES[:K_SCAN]

print(f"  s = {s}, log_2(s) = {log2(s):.2f}\n")
print(f"  {'k':>4} {'#covered':>10} {'frac':>8} {'#subsets':>10} {'subsets/s':>10}")
print(f"  {'-'*48}")

for k in range(2, 15):
    ps = tower_primes[:k]
    if s in ps:
        continue
    invs = [mod_inv(p, s) for p in ps]
    covered = subset_sum_coverage(invs, s)
    n_subsets = 2**k - 1
    frac = len(covered) / s
    print(f"  {k:>4} {len(covered):>10} {frac:>8.1%} {n_subsets:>10} {n_subsets/s:>10.1f}")

# Do the same for a few more primes
for s_test in [67, 97, 127, 151]:
    print(f"\n  s = {s_test}, log_2(s) = {log2(s_test):.2f}")
    print(f"  {'k':>4} {'#covered':>10} {'frac':>8}")
    print(f"  {'-'*28}")
    for k in range(2, 15):
        ps = tower_primes[:k]
        if s_test in ps:
            continue
        invs = [mod_inv(p, s_test) for p in ps]
        covered = subset_sum_coverage(invs, s_test)
        frac = len(covered) / s_test
        print(f"  {k:>4} {len(covered):>10} {frac:>8.1%}")
        if frac == 1.0:
            break


# ═══════════════════════════════════════════════════════════════════════
# III. NAMING COVERAGE — DOES FULL SUBSET-SUM COVERAGE = ZERO MISSES?
# ═══════════════════════════════════════════════════════════════════════

section("III. NAMING COVERAGE VS SUBSET-SUM COVERAGE")

print("""
  Subset-sum coverage of Z/s is NECESSARY but not SUFFICIENT for naming.
  Naming requires sum(p_i^{-1}) = |S|-1 mod s for some subset of SIZE |S|.
  Full Z/s coverage means every residue is hit by SOME subset, but the
  size-target pairing must also match.

  Check: at what k does naming-coverage (size-correct hits) become
  complete vs raw subset-sum coverage?
""")

for s_test in [41, 67, 97]:
    print(f"\n  s = {s_test}:")
    print(f"  {'k':>4} {'raw_cover':>10} {'naming_hit':>11} {'raw%':>6} {'note':>12}")
    print(f"  {'-'*50}")

    for k in range(3, 14):
        ps = tower_primes[:k]
        if s_test in ps:
            continue
        invs = [mod_inv(p, s_test) for p in ps]

        raw_covered = subset_sum_coverage(invs, s_test)
        by_size = subset_sum_coverage_by_size(invs, s_test)

        naming_hit = False
        for size in range(2, k + 1):
            target = (size - 1) % s_test
            if target in by_size.get(size, set()):
                naming_hit = True
                break

        note = ""
        if len(raw_covered) == s_test and naming_hit:
            note = "full+named"
        elif len(raw_covered) == s_test:
            note = "full,unnamed"
        elif naming_hit:
            note = "partial,named"

        pct = len(raw_covered) / s_test
        print(f"  {k:>4} {len(raw_covered):>10} {'YES' if naming_hit else 'no':>11} "
              f"{pct:>6.1%} {note:>12}")


# ═══════════════════════════════════════════════════════════════════════
# IV. SUBGROUP OBSTRUCTION — WHY COVERAGE FAILS
# ═══════════════════════════════════════════════════════════════════════

section("IV. SUBGROUP OBSTRUCTION — WHY COVERAGE FAILS")

print("""
  When coverage is incomplete, do the inverse values lie in a proper
  subgroup or coset of Z/s? If gcd of the values generates a proper
  subgroup, only that subgroup's cosets are reachable.

  For Z/s with s prime this is a PROPERTY, not a finding: Z/s has no
  non-trivial additive subgroups (its order is prime), and every inverse is
  nonzero, so the values generate all of Z/s by construction. Coverage
  failure is therefore purely a coupon-collector effect — too few
  subsets. The gcd printout below ILLUSTRATES the property; it cannot
  fail while s is prime, so it confirms nothing beyond the arithmetic.
""")

for s_test in [41, 67, 97]:
    print(f"\n  s = {s_test} (prime, Z/{s_test} is a field):")
    for k in range(3, 10):
        ps = tower_primes[:k]
        if s_test in ps:
            continue
        invs = [mod_inv(p, s_test) for p in ps]
        g = invs[0]
        for v in invs[1:]:
            g = gcd(g, v)
        g = gcd(g, s_test)
        print(f"    k={k}: invs mod {s_test} = {invs}, gcd = {g}, "
              f"generates Z/{s_test}: {g == 1}")


# ═══════════════════════════════════════════════════════════════════════
# V. EGZ COMPARISON — THE 2n-1 BOUND
# ═══════════════════════════════════════════════════════════════════════

section("V. EGZ COMPARISON — THE 2n-1 BOUND")

print("""
  EGZ theorem: any 2n-1 integers contain an n-element subset summing
  to 0 mod n. In our context, if we had 2s-1 tower primes, we'd be
  guaranteed an s-element subset summing to 0 mod s.

  But k << s typically (explore_missed_primes.py reads rung k=7
  against primes up to its window edge 10*p_7 = 170 — a window
  choice, not an object bound). EGZ doesn't directly apply — it's a
  guarantee for WORST-CASE inputs with enough elements.
  Our setting has FEW elements (k) but MANY subsets (2^k).

  The relevant bound: with k "random" values in Z/s, full coverage
  by 2^k subsets happens around k ~ log_2(s) + O(log log s).

  Compare EGZ requirement (2s-1 elements) vs observed threshold:
""")

print(f"  {'s':>5} {'EGZ needs':>10} {'observed k':>11} {'savings':>8}")
print(f"  {'-'*40}")

for s, k_full, lg2, ratio in thresholds:
    egz_needs = 2 * s - 1
    savings = egz_needs / k_full
    print(f"  {s:>5} {egz_needs:>10} {k_full:>11} {savings:>8.0f}x")

if thresholds:
    mean_savings = sum((2 * s - 1) / k for s, k, _, _ in thresholds) / len(thresholds)
    print(f"\n  EGZ requires O(s) elements for worst-case guarantee.")
    print(f"  The tower achieves full coverage with O(log s) elements.")
    print(f"  Mean savings over {len(thresholds)} primes: "
          f"{mean_savings:.1f}x fewer elements needed.")
    print(f"\n  Why? EGZ handles adversarial inputs. Our values (prime inverses)")
    print(f"  are pseudo-random in Z/s, so coverage is MUCH faster.")


# ═══════════════════════════════════════════════════════════════════════
# VI. DAVENPORT CONSTANT — D(Z/s) = s
# ═══════════════════════════════════════════════════════════════════════

section("VI. DAVENPORT CONSTANT D(Z/s) = s")

print("""
  The Davenport constant D(G) is the smallest d such that every sequence
  of d elements in G has a non-empty zero-sum subsequence.
  For cyclic Z/n: D(Z/n) = n.

  In our context: with s elements in Z/s (worst case), there's always
  a zero-sum subsequence. With k < s elements, coverage depends on the
  specific values. But the tower's inverses are well-distributed.

  The CONNECTION: D(Z/s) = s means full zero-sum coverage is guaranteed
  at k = s (one free subset per residue class). The tower achieves it
  exponentially earlier because 2^k subsets >> k.

  The effective Davenport constant for "all 2^k subsets" is:
    D_eff(s) = min k such that ALL of Z/s is in the subset-sum range.
  We've computed this above. Let's characterize D_eff vs D = s.
""")

print(f"  {'s':>5} {'D(Z/s)':>7} {'D_eff':>6} {'D/D_eff':>8} {'log2(s)':>8}")
print(f"  {'-'*40}")

for s, k_full, lg2, ratio in thresholds:
    D = s
    D_eff = k_full
    print(f"  {s:>5} {D:>7} {D_eff:>6} {D/D_eff:>8.1f} {lg2:>8.2f}")

if thresholds:
    avg_D_ratio = sum(s / k for s, k, _, _ in thresholds) / len(thresholds)
    print(f"\n  Mean D(Z/s) / D_eff = {avg_D_ratio:.1f}")
    print(f"  D_eff ~ log_2(s) + small constant.")


# ═══════════════════════════════════════════════════════════════════════
# VII. COUPON COLLECTOR ANALOGY
# ═══════════════════════════════════════════════════════════════════════

section("VII. COUPON COLLECTOR ANALOGY")

print("""
  The subset-sum coverage problem is analogous to the coupon collector.
  With s coupons (residues) and 2^k - 1 random draws (subsets), the
  expected number of draws to collect all coupons is s * H(s) where
  H(s) = sum(1/i, i=1..s) ~ ln(s) + 0.577.

  Full coverage when 2^k - 1 >= s * H(s), i.e., k >= log_2(s * H(s)).
  But subsets aren't independent draws — later subsets are correlated
  with earlier ones (they share elements).

  Compare predicted vs observed thresholds:
""")

print(f"  {'s':>5} {'k_obs':>6} {'k_coupon':>9} {'k_log2':>7} {'obs/coupon':>11}")
print(f"  {'-'*45}")

for s, k_full, lg2, ratio in thresholds:
    H_s = sum(1.0 / i for i in range(1, s + 1))
    k_coupon = log2(s * H_s)
    obs_coupon_ratio = k_full / k_coupon
    print(f"  {s:>5} {k_full:>6} {k_coupon:>9.2f} {lg2:>7.2f} {obs_coupon_ratio:>11.2f}")

if thresholds:
    avg_obs_coupon = sum(k / log2(s * sum(1.0/i for i in range(1, s+1)))
                         for s, k, _, _ in thresholds) / len(thresholds)
    print(f"\n  Mean observed / coupon-collector prediction: {avg_obs_coupon:.3f}")


# ═══════════════════════════════════════════════════════════════════════
# VIII. SIZE-SPECIFIC COVERAGE — FIXED-SIZE SUBSET SUMS
# ═══════════════════════════════════════════════════════════════════════

section("VIII. SIZE-SPECIFIC COVERAGE — FIXED-SIZE SUBSET SUMS")

print("""
  EGZ specifically concerns fixed-size (n-element) subsets summing to 0.
  How does fixed-size coverage compare to all-size coverage?

  For each k and s=41, show coverage by subset size.
""")

s = 41
print(f"  s = {s}\n")

for k in [5, 6, 7, 8, 9, 10]:
    ps = tower_primes[:k]
    if s in ps:
        continue
    invs = [mod_inv(p, s) for p in ps]
    by_size = subset_sum_coverage_by_size(invs, s)

    sizes_str = "  ".join(f"sz{m}:{len(by_size[m]):>2}/{s}"
                          for m in sorted(by_size.keys())[:6])
    all_covered = set()
    for sums in by_size.values():
        all_covered |= sums
    print(f"  k={k:>2}: total={len(all_covered):>2}/{s}  [{sizes_str}]")


# ═══════════════════════════════════════════════════════════════════════
# IX. GENERALIZATION — COMPOSITE MODULI
# ═══════════════════════════════════════════════════════════════════════

section("IX. COMPOSITE MODULI — D(Z/n) FOR NON-PRIME n")

print("""
  The tower also produces composite -chi values. For composite n,
  D(Z/n) = n still holds for cyclic groups, but the structure differs.

  For n with small prime factors, coverage may be faster (subgroup
  structure helps). Note: Z/pq for distinct primes p, q is cyclic
  (by CRT), so D(Z/pq) = pq. The formula D = p+q-1 applies only to
  rank-2 groups like Z/p x Z/p, not to coprime products.

  Test: does coverage of composite moduli follow the same log_2 pattern?
""")

composites = [35, 55, 77, 91, 119, 143, 161, 187]

# k_vals counts the coprime inverses actually summed; k_rung is the tower
# rung consumed to collect them (the factors of n sit in the tower and are
# skipped, so k_rung >= k_vals by the number of skipped factors).
print(f"  {'n':>5} {'factored':>12} {'k_vals':>7} {'k_rung':>7} {'log2(n)':>8}")
print(f"  {'-'*48}")

for n in composites:
    coprime_idx = [i for i, p in enumerate(ALL_PRIMES[:30]) if gcd(p, n) == 1]
    coprime_primes = [ALL_PRIMES[i] for i in coprime_idx]

    k_full = None
    for num_vals in range(2, min(len(coprime_primes), 16) + 1):
        invs = [mod_inv(p, n) for p in coprime_primes[:num_vals]]
        covered = subset_sum_coverage(invs, n)
        if len(covered) == n:
            k_full = num_vals
            break

    f = factorize(n)
    f_str = "*".join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(f.items()))

    if k_full is not None:
        k_rung = coprime_idx[k_full - 1] + 1
        print(f"  {n:>5} {f_str:>12} {k_full:>7} {k_rung:>7} {log2(n):>8.2f}")
    else:
        print(f"  {n:>5} {f_str:>12} {'>16':>7} {'?':>7} {log2(n):>8.2f}")


# ═══════════════════════════════════════════════════════════════════════
# X. THE PREDICTION-COMPLETE FRONTIER
# ═══════════════════════════════════════════════════════════════════════

section("X. THE PREDICTION-COMPLETE FRONTIER")

print("""
  Define k_pred(s) as the smallest k where s is NAMED (predicted) by
  some sub-ring. This is different from k_full (full Z/s coverage) —
  naming only needs ONE hit at the right (size, target) pair.

  Typically k_pred(s) < k_full(s) (naming is easier than full coverage),
  but exceptions exist (s=83: naming needs one MORE rung than full coverage).
  Map the frontier: for each s, find k_pred and compare to k_full.
""")

print(f"  {'s':>5} {'k_pred':>7} {'k_full':>7} {'gap':>5} {'log2(s)':>8}")
print(f"  {'-'*38}")

frontier_data = []
for idx in range(8, 80):
    s = ALL_PRIMES[idx]
    if s > 200:
        break

    tower_primes_here = ALL_PRIMES[:K_SCAN]
    if s in tower_primes_here:
        continue

    k_pred = None
    k_full = None

    for k in range(2, K_SCAN + 1):
        ps = tower_primes_here[:k]
        if s in ps:
            continue
        invs = [mod_inv(p, s) for p in ps]
        if None in invs:
            continue

        if k_pred is None:
            by_size = subset_sum_coverage_by_size(invs, s)
            for size in range(2, k + 1):
                target = (size - 1) % s
                if target in by_size.get(size, set()):
                    k_pred = k
                    break

        if k_full is None:
            covered = set()
            for sums in subset_sum_coverage_by_size(invs, s).values():
                covered |= sums
            if len(covered) == s:
                k_full = k

        if k_pred is not None and k_full is not None:
            break

    if k_pred is not None and k_full is not None:
        gap = k_full - k_pred
        frontier_data.append((s, k_pred, k_full, gap))
        print(f"  {s:>5} {k_pred:>7} {k_full:>7} {gap:>5} {log2(s):>8.2f}")
    elif k_pred is not None:
        print(f"  {s:>5} {k_pred:>7} {'>' + str(K_SCAN):>7} {'?':>5} {log2(s):>8.2f}")

if frontier_data:
    avg_gap = sum(g for _, _, _, g in frontier_data) / len(frontier_data)
    avg_pred = sum(kp for _, kp, _, _ in frontier_data) / len(frontier_data)
    avg_full = sum(kf for _, _, kf, _ in frontier_data) / len(frontier_data)
    print(f"\n  Mean k_pred = {avg_pred:.1f},  mean k_full = {avg_full:.1f},  "
          f"mean gap = {avg_gap:.1f}")
    print(f"  Naming is MUCH easier than full coverage — one hit suffices.")


# ═══════════════════════════════════════════════════════════════════════
# XI. KEY FINDINGS
# ═══════════════════════════════════════════════════════════════════════

section("XI. KEY FINDINGS")

print("""
  Summary of the Davenport / EGZ connection:

  1. COVERAGE THRESHOLD (observation, 26 primes s=73..199). Full
     subset-sum coverage of Z/s requires k_full ~ 1.36 * log_2(s)
     tower primes. Ratio k_full/log_2(s): mean 1.36, range [1.25, 1.50].

  2. COUPON COLLECTOR MODEL (observation, 26 primes). The threshold
     k ~ log_2(s * H(s)) where H(s) = sum(1/i, i=1..s) predicts
     k_full almost exactly: mean observed/predicted = 1.008. Subset
     sums behave like near-independent draws despite correlation.
     This is the sharpest result of the exploration.

  3. EGZ IS INAPPLICABLE. EGZ guarantees zero-sum at 2s-1 elements
     (fixed size). The tower achieves full coverage at k ~ log_2(s),
     which is 28.4x fewer elements on average over s in [73, 199]
     (mean printed in section V), because 2^k subsets grow
     exponentially. (The 14.2x below is a different ratio — against
     the Davenport constant D(Z/s) = s, not against EGZ's 2s-1.)
     EGZ addresses worst-case inputs; the tower's prime inverses are
     well-distributed (pseudo-random in Z/s).

  4. SUBGROUP OBSTRUCTION ABSENT (property). Since s is prime, Z/s
     has no proper additive subgroups and every inverse is nonzero,
     so the values generate all of Z/s by construction — the gcd
     printout in section IV illustrates this and cannot fail.
     Coverage failure is purely a counting effect: too few subsets
     to hit all s residues.

  5. NAMING << FULL COVERAGE (observation, 26 primes). Naming needs
     one (size, target) hit; full coverage needs all s residues. Mean
     k_pred = 7.2 vs k_full = 9.6 (gap = 2.3 rungs). This explains
     why the miss rate from the earlier finding drops faster than full coverage.

  6. D_eff = O(log s). The effective Davenport constant for 2^k
     subsets is D_eff ~ log_2(s * ln(s)), vs D(Z/s) = s. The
     exponential advantage: each new prime doubles the sub-ring
     count. D(Z/s)/D_eff = 14.2x on average for s in [73, 199].
""")

print("=" * 72)
print("  Done. Davenport / EGZ connection mapped.")
print("=" * 72)
