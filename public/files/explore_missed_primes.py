"""Missed primes — why does 41 escape prediction at k=7?

The open question left by explore_prediction_horizon.py. At rung k=7,
the tower predicts 14 of the first 15 primes beyond p_7=17 — only 41 is
missed. Why? Does it get absorbed at k=8? Is there a pattern to which
primes resist prediction?

The reciprocal naming criterion (proved, explore_tower_naming.py):
s | -chi(S) iff
  sum(p_i^{-1} mod s) = |S| - 1   (mod s)
for the primes p_i in sub-ring S. So s is "missed" at rung k iff no subset
of {p_1,...,p_k} satisfies this congruence — a SUBSET SUM problem in Z/s.

Run: python prime/code/explore_missed_primes.py
Runs in about 7 s, peak memory under 15 MB.
"""

from math import prod
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
    """Modular inverse of a mod m via extended Euclidean."""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        return None
    return x % m


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    return g, y1 - (b // a) * x1, x1


def neg_chi(ps):
    k = len(ps)
    N = prod(ps)
    return N * (k - 1) - sum(N // p for p in ps)


K_MAX = 12
ALL_PRIMES = first_n_primes(200)


# ═══════════════════════════════════════════════════════════════════════
# I. THE 41 MYSTERY — SUBSET SUM IN Z/41
# ═══════════════════════════════════════════════════════════════════════

section("I. THE 41 MYSTERY — SUBSET SUM IN Z/41")

s = 41
ps_k7 = ALL_PRIMES[:7]  # {2,3,5,7,11,13,17}

print(f"\n  Tower primes at k=7: {ps_k7}")
print(f"  Target prime: s = {s}")
print()

# Compute inverses mod 41
invs = {}
for p in ps_k7:
    inv = mod_inv(p, s)
    invs[p] = inv
    print(f"  {p}^(-1) mod {s} = {inv}   (check: {p}*{inv} = {p*inv} = {p*inv % s} mod {s})")

inv_values = [invs[p] for p in ps_k7]
print(f"\n  Inverse set: {inv_values}")

# Check all subsets
print(f"\n  Checking all {2**7 - 1} non-empty subsets for sum = |S|-1 mod {s}:")
hits = 0
for size in range(1, 8):
    target = (size - 1) % s
    found = False
    for subset in combinations(range(7), size):
        sigma = sum(inv_values[i] for i in subset) % s
        if sigma == target:
            primes_in = [ps_k7[i] for i in subset]
            chi = neg_chi(primes_in)
            print(f"    HIT: size={size}, S={primes_in}, sum(inv)={sigma}, "
                  f"target={target}, -chi={chi}")
            hits += 1
            found = True
    if not found:
        print(f"    size={size}: target={target} — NO subset matches")

print(f"\n  Total hits: {hits}")
if hits == 0:
    print(f"  CONFIRMED: 41 is INVISIBLE to all {2**7-1} sub-rings at k=7.")


# ═══════════════════════════════════════════════════════════════════════
# II. ABSORPTION AT k=8 — THE PAIR {17,19}
# ═══════════════════════════════════════════════════════════════════════

section("II. ABSORPTION AT k=8 — DOES 41 APPEAR?")

ps_k8 = ALL_PRIMES[:8]  # {2,3,5,7,11,13,17,19}

print(f"\n  Tower primes at k=8: {ps_k8}")
print(f"  New prime: 19.  19^(-1) mod 41 = {mod_inv(19, s)}")

inv_k8 = [mod_inv(p, s) for p in ps_k8]
print(f"  Full inverse set: {inv_k8}")

print(f"\n  Sub-rings at k=8 that predict 41:")
absorbers = []
for size in range(2, 9):
    target = (size - 1) % s
    for subset in combinations(range(8), size):
        sigma = sum(inv_k8[i] for i in subset) % s
        if sigma == target:
            primes_in = [ps_k8[i] for i in subset]
            chi = neg_chi(primes_in)
            absorbers.append((size, primes_in, chi))
            if len(absorbers) <= 15:
                print(f"    S={primes_in}, -chi={chi}, 41 divides? {chi % 41 == 0}")

print(f"\n  Total sub-rings predicting 41 at k=8: {len(absorbers)}")
print(f"  Smallest: {absorbers[0][1]} with -chi = {absorbers[0][2]} = {absorbers[0][2]//41} * 41")

# Verify the {17,19} pair specifically
chi_17_19 = neg_chi([17, 19])
print(f"\n  Direct check: -chi({{17,19}}) = 17*19 - 17 - 19 = {chi_17_19}")
print(f"  = (17-1)(19-1) - 1 = {16*18-1}")
print(f"  = 287 = 7 * 41.  41 | 287? {287 % 41 == 0}")
print(f"\n  41 is absorbed at k=8 by the pair {{17,19}}.")
print(f"  It needed 19 — the NEXT prime after 17 — to break through.")


# ═══════════════════════════════════════════════════════════════════════
# III. MISSED PRIMES MAP — ALL RUNGS k=3..12
# ═══════════════════════════════════════════════════════════════════════

section("III. MISSED PRIMES MAP (k=3..12)")

print("""
  For each rung k, find ALL primes p_k < s <= max(10*p_k, 100) that are
  NOT predicted by any sub-ring. These are the tower's blind spots.
""")

# For each rung, compute predicted primes up to some horizon
miss_data = {}

for k in range(3, K_MAX + 1):
    ps = ALL_PRIMES[:k]
    p_k = ps[-1]
    prime_set = set(ps)
    horizon = max(10 * p_k, 100)

    predicted = set()
    for size in range(2, k + 1):
        for subset in combinations(ps, size):
            nc = neg_chi(list(subset))
            if nc == 0:
                continue
            abs_nc = abs(nc)
            f = factorize(abs_nc)
            for s_val in f:
                if s_val not in set(subset) and is_prime(s_val):
                    predicted.add(s_val)

    # Primes in range (p_k, horizon] not in tower and not predicted
    check_primes = [p for p in ALL_PRIMES if p > p_k and p <= horizon]
    missed = [p for p in check_primes if p not in predicted]
    hit = [p for p in check_primes if p in predicted]

    miss_data[k] = missed

    miss_str = ", ".join(str(m) for m in missed[:12])
    if len(missed) > 12:
        miss_str += f" ...+{len(missed)-12}"
    print(f"  k={k:>2} p_k={p_k:>3}  checked {len(check_primes):>3} primes, "
          f"hit {len(hit):>3}, missed {len(missed):>2}  [{miss_str}]")


# ═══════════════════════════════════════════════════════════════════════
# IV. ABSORPTION TRACKING — WHEN IS EACH MISS CURED?
# ═══════════════════════════════════════════════════════════════════════

section("IV. ABSORPTION TRACKING — WHEN DOES EACH MISS GET CURED?")

print("""
  For each missed prime, find the smallest rung where it first gets
  predicted. Prediction is MONOTONE in k (property: the rung-k
  sub-rings are a subfamily of the rung-(k+1) sub-rings), so a prime
  unpredicted at its absorption rung minus one is unpredicted at EVERY
  smaller rung. The in_survey column below therefore records only when
  the survey window max(10*p_k, 100) first CONTAINS the prime — the
  miss itself always dates back to the smallest rungs. Persistence is
  measured by the absorption rung alone, never by the survey lag.
""")

# Collect all missed primes across rungs
all_missed = set()
for k, missed in miss_data.items():
    for m in missed:
        all_missed.add((k, m))

# For each missed prime, check when it's first absorbed
# We already have predicted sets; let's recompute more carefully
predicted_at = {}
for k in range(3, K_MAX + 1):
    ps = ALL_PRIMES[:k]
    predicted = set()
    for size in range(2, k + 1):
        for subset in combinations(ps, size):
            nc = neg_chi(list(subset))
            if nc == 0:
                continue
            abs_nc = abs(nc)
            f = factorize(abs_nc)
            for s_val in f:
                if s_val not in set(subset) and is_prime(s_val):
                    predicted.add(s_val)
    predicted_at[k] = predicted

print(f"  {'miss':>6} {'in_survey':>9} {'absorbed_k':>12} {'absorbing sub-ring':>30}")
print(f"  {'-'*60}")

absorption = []
for first_k, miss in sorted(all_missed, key=lambda x: (x[1], x[0])):
    # Only track the first time a prime is missed
    if any(first_k > fk for fk, m in all_missed if m == miss):
        continue

    absorbed_k = None
    absorber = None
    for k2 in range(first_k, K_MAX + 1):
        if miss in predicted_at[k2]:
            absorbed_k = k2
            # Find smallest absorbing sub-ring
            ps2 = ALL_PRIMES[:k2]
            for size in range(2, k2 + 1):
                found = False
                for subset in combinations(ps2, size):
                    if miss in set(subset):
                        continue
                    nc = neg_chi(list(subset))
                    if nc != 0 and abs(nc) % miss == 0:
                        absorber = list(subset)
                        found = True
                        break
                if found:
                    break
            break

    abs_str = str(absorbed_k) if absorbed_k else ">12"
    sub_str = str(absorber) if absorber else "?"
    absorption.append((miss, first_k, absorbed_k, absorber))
    print(f"  {miss:>6} {first_k:>9} {abs_str:>12} {sub_str:>30}")

latest = sorted(absorption, key=lambda t: -(t[2] if t[2] else 99))[:4]
print(f"\n  Latest absorptions in the survey (the persistence ranking): "
      + ", ".join(f"{m} (k={a})" for m, _, a, _ in latest))


# ═══════════════════════════════════════════════════════════════════════
# V. THE SUBSET SUM PICTURE — WHY SOME PRIMES RESIST
# ═══════════════════════════════════════════════════════════════════════

section("V. SUBSET SUM PICTURE — WHY SOME PRIMES RESIST")

print("""
  For a prime s, the tower at rung k predicts s iff -1 is in the
  subset-sum range of {p_i^{-1} - 1 mod s : i=1..k} in Z/s.

  With k values, there are 2^k - 1 subset sums. If they were uniform
  in Z/s, P(miss) ~ (1-1/s)^(2^k - 1). For s=41, k=7:
  P ~ (40/41)^127 ~ 0.044. So ~4.4% of primes near 41 should be missed.

  Let's compare observed vs expected miss rates.
""")

for k in range(4, K_MAX + 1):
    ps = ALL_PRIMES[:k]
    p_k = ps[-1]
    horizon = max(10 * p_k, 100)
    check_primes = [p for p in ALL_PRIMES if p > p_k and p <= horizon]
    n_check = len(check_primes)
    n_missed = len(miss_data[k])

    if n_check == 0:
        continue

    observed_rate = n_missed / n_check
    # Expected miss rate: average over checked primes of (1-1/s)^{2^k - 1}.
    # The model treats primes independently, so the expected miss count is
    # a sum of Bernoullis: sd = sqrt(sum p(1-p)), z = (obs - exp)/sd.
    n_subsets = 2**k - 1
    probs = [(1 - 1/s)**n_subsets for s in check_primes]
    expected_misses = sum(probs)
    expected_rate = expected_misses / n_check
    sd = sum(p * (1 - p) for p in probs) ** 0.5
    z = (n_missed - expected_misses) / sd if sd > 1e-9 else 0.0

    print(f"  k={k:>2}: checked {n_check:>3} primes, "
          f"missed {n_missed:>2} ({observed_rate:>6.1%}), "
          f"expected ~{expected_misses:>5.1f} ({expected_rate:>6.1%}), "
          f"z = {z:>+5.1f}  [2^k-1 = {n_subsets}]")


# ═══════════════════════════════════════════════════════════════════════
# VI. STRUCTURAL ANALYSIS — WHAT MAKES 41 SPECIAL?
# ═══════════════════════════════════════════════════════════════════════

section("VI. STRUCTURAL ANALYSIS — WHAT MAKES 41 SPECIAL?")

print("""
  At k=7, inverses mod 41: {21, 14, 33, 6, 15, 19, 29}.
  These are p^{-1} mod 41 for p in {2,3,5,7,11,13,17}.

  The subset-sum targets are {0,1,2,3,4,5,6} for sizes 1..7.
  All 7 targets must be missed for 41 to be invisible.

  What's the subset-sum coverage of these 7 values in Z/41?
""")

ps_k7 = ALL_PRIMES[:7]
inv_41 = [mod_inv(p, 41) for p in ps_k7]

# Compute ALL subset sums
all_sums = set()
sum_by_size = defaultdict(set)
for size in range(1, 8):
    for subset in combinations(inv_41, size):
        s_val = sum(subset) % 41
        all_sums.add(s_val)
        sum_by_size[size].add(s_val)

print(f"  Inverse values: {inv_41}")
print(f"  Total distinct subset sums: {len(all_sums)} out of 41")
print(f"  Covered values: {sorted(all_sums)}")
uncovered = sorted(set(range(41)) - all_sums)
print(f"  Uncovered values: {uncovered}")
print()

for size in range(1, 8):
    target = (size - 1) % 41
    hit = target in sum_by_size[size]
    coverage = len(sum_by_size[size])
    print(f"  size {size}: target={target:>2}, sums cover {coverage:>2}/41 values, "
          f"target hit: {'YES' if hit else 'NO'}")

# Compare with a nearby prime that IS predicted
print(f"\n  Comparison: prime 43 (predicted at k=7)")
inv_43 = [mod_inv(p, 43) for p in ps_k7]
sums_43 = set()
sums_43_by_size = defaultdict(set)
for size in range(1, 8):
    for subset in combinations(inv_43, size):
        s_val = sum(subset) % 43
        sums_43.add(s_val)
        sums_43_by_size[size].add(s_val)

print(f"  Inverse values mod 43: {inv_43}")
print(f"  Total distinct subset sums: {len(sums_43)} out of 43")
for size in range(1, 8):
    target = (size - 1) % 43
    hit = target in sums_43_by_size[size]
    if hit:
        # Find the actual subset
        for subset in combinations(range(7), size):
            sigma = sum(inv_43[i] for i in subset) % 43
            if sigma == target:
                primes_in = [ps_k7[i] for i in subset]
                print(f"  size {size}: target={target:>2} — HIT by S={primes_in}")
                break
        break  # Just show first hit


# ═══════════════════════════════════════════════════════════════════════
# VII. (p-1) FACTORIZATION AND MISSED PRIMES
# ═══════════════════════════════════════════════════════════════════════

section("VII. (p-1) FACTORIZATION OF MISSED PRIMES")

print("""
  Does the factorization of (s-1) predict whether s is missed?
  A prime s with (s-1) having only small factors might have more
  structured inverses, making subset-sum avoidance easier.
""")

for k in [7, 8, 10]:
    if k > K_MAX:
        continue
    ps = ALL_PRIMES[:k]
    p_k = ps[-1]
    horizon = max(10 * p_k, 100)
    check_primes = [p for p in ALL_PRIMES if p > p_k and p <= horizon]
    missed_set = set(miss_data[k])

    print(f"\n  k={k} (p_k={p_k}):")
    print(f"  {'prime':>6} {'status':>8} {'p-1':>8} {'factorization'}")
    print(f"  {'-'*55}")

    for s in check_primes[:20]:
        status = "MISSED" if s in missed_set else "hit"
        f = factorize(s - 1)
        f_str = " * ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(f.items()))
        print(f"  {s:>6} {status:>8} {s-1:>8} = {f_str}")


# ═══════════════════════════════════════════════════════════════════════
# VIII. CUNNINGHAM CHAIN — 41, 83, 167
# ═══════════════════════════════════════════════════════════════════════

section("VIII. CUNNINGHAM CHAIN — 41, 83, 167")

print("""
  At k=7, three missed primes form a Cunningham chain (first kind):
    41 -> 83 = 2*41+1 -> 167 = 2*83+1
  Each term is 2p+1. So (s-1) has the previous missed prime as factor.
  Does the chain structure cause correlated misses?
""")

chain = [41, 83, 167]

for s in chain:
    ps_k7 = ALL_PRIMES[:7]
    invs_s = [mod_inv(p, s) for p in ps_k7]
    print(f"  s = {s}:  s-1 = {s-1} = {dict(factorize(s-1))}")
    print(f"    Inverses mod {s}: {invs_s}")

    # Per-size coverage
    covers = {}
    for size in range(1, 8):
        target = (size - 1) % s
        sums = set()
        for subset in combinations(invs_s, size):
            sums.add(sum(subset) % s)
        covers[size] = (target, target in sums, len(sums))
        status = "HIT" if target in sums else "miss"
        print(f"    size {size}: target={target:>3}, coverage={len(sums):>3}/{s}, {status}")

    # Overall subset sum coverage
    all_ss = set()
    for size in range(1, 8):
        for subset in combinations(invs_s, size):
            all_ss.add(sum(subset) % s)
    print(f"    Overall: {len(all_ss)}/{s} values reachable")
    print()

# Check if the chain continues
next_chain = 2 * 167 + 1
print(f"  Next in chain: 2*167+1 = {next_chain} = "
      f"{dict(factorize(next_chain))}  prime? {is_prime(next_chain)}")
print(f"  Chain terminates at 167 (335 = 5*67 is composite).")

# The chain's absorptions (rungs from the section IV table; persistence
# is the absorption rung — the monotonicity note there)
print(f"\n  The chain's absorptions: 41 at k=8, 83 and 167 at k=9 — the")
print(f"    latter two tied with 163 for the k=7 window's last absorptions")
print(f"    (section IV; the survey-wide latest is 281, absorbed at k=11).")
print(f"    83's absorbing sub-ring: {{11, 19, 23}}")
chi_absorber = neg_chi([11, 19, 23])
print(f"    -chi({{11,19,23}}) = {chi_absorber}")
print(f"    {chi_absorber} / 83 = {chi_absorber // 83}")
print(f"    83 | {chi_absorber}? {chi_absorber % 83 == 0}")

# Correlation test: does s-1 having a large prime factor predict misses?
print(f"\n  Largest prime factor of (s-1) for missed vs hit primes at k=7:")
ps_k7 = ALL_PRIMES[:7]
p_k = ps_k7[-1]
horizon = 10 * p_k
check_primes = [p for p in ALL_PRIMES if p > p_k and p <= horizon]
missed_set = set(miss_data[7])

missed_lpf = []
hit_lpf = []
for s in check_primes:
    f = factorize(s - 1)
    lpf = max(f.keys())
    if s in missed_set:
        missed_lpf.append((s, lpf, lpf / s))
    else:
        hit_lpf.append((s, lpf, lpf / s))

print(f"    Missed ({len(missed_lpf)} primes):")
for s, lpf, ratio in missed_lpf:
    print(f"      s={s:>4}, P+(s-1)={lpf:>4}, P+/s = {ratio:.3f}")

avg_missed = sum(r for _, _, r in missed_lpf) / len(missed_lpf) if missed_lpf else 0
avg_hit = sum(r for _, _, r in hit_lpf) / len(hit_lpf) if hit_lpf else 0
print(f"    Mean P+(s-1)/s for missed: {avg_missed:.3f}")
print(f"    Mean P+(s-1)/s for hit:    {avg_hit:.3f}")
if avg_missed > avg_hit:
    print(f"    Missed primes have {avg_missed/avg_hit:.2f}x larger relative P+ factor.")


# ═══════════════════════════════════════════════════════════════════════
# IX. COMPLEMENT STRUCTURE OF UNCOVERED VALUES
# ═══════════════════════════════════════════════════════════════════════

section("IX. COMPLEMENT STRUCTURE OF UNCOVERED VALUES")

print("""
  For 7 values in Z/41, subset S of size m has complement of size 7-m.
  If S sums to sigma, complement sums to (total - sigma) mod 41.
  Total = sum of all 7 inverses = 137 = 14 mod 41.

  So if sigma is unreachable at size m, then (14 - sigma) mod 41 is
  unreachable at size 7-m. Uncovered values come in complement pairs.
""")

total_inv = sum(mod_inv(p, 41) for p in ALL_PRIMES[:7]) % 41
print(f"  Total of inverses mod 41: {total_inv}")
print()

ps_k7 = ALL_PRIMES[:7]
inv_41 = [mod_inv(p, 41) for p in ps_k7]

for size in range(1, 8):
    comp_size = 7 - size
    sums_m = set()
    sums_c = set()
    for subset in combinations(inv_41, size):
        sums_m.add(sum(subset) % 41)
    for subset in combinations(inv_41, comp_size):
        sums_c.add(sum(subset) % 41)

    # Verify complement relation
    target_m = (size - 1) % 41
    target_c = (comp_size - 1) % 41

    print(f"  size {size} (target={target_m:>2}): uncovered = "
          f"{sorted(set(range(41)) - sums_m)[:6]}")
    if size <= 3:
        # Check complement mapping
        complement_of_uncovered = sorted((total_inv - v) % 41
                                         for v in set(range(41)) - sums_m)
        uncovered_at_comp = sorted(set(range(41)) - sums_c)
        print(f"           complement -> size {comp_size} uncovered = "
              f"{uncovered_at_comp[:6]}")
        matches = complement_of_uncovered == uncovered_at_comp
        print(f"           complement relation holds: {matches}")


# ═══════════════════════════════════════════════════════════════════════
# X. KEY FINDINGS
# ═══════════════════════════════════════════════════════════════════════

section("X. KEY FINDINGS")

print("""
1. 41 IS INVISIBLE AT k=7. Confirmed via subset-sum analysis: the
   7 inverse values {21,14,33,6,15,19,29} in Z/41 have no subset
   whose sum equals the required target (|S|-1 mod 41) at any size.
   Only 37/41 values are reachable; the 4 gaps form complement pairs.

2. 41 IS ABSORBED AT k=8. The pair {17,19} predicts 41:
   -chi({17,19}) = 287 = 7 * 41. Adding p_8=19 to the tower unlocks
   the prediction. The formula: (p-1)(q-1) - 1 = 287 = 7*41.

3. CUNNINGHAM CHAIN {41, 83, 167}. All three missed at k=7. Each
   term is 2p+1 of the previous. 83-1 = 2*41, 167-1 = 2*83. The
   chain terminates (335 = 5*67). Absorptions: 41 at k=8, 83 and
   167 at k=9 (83 by {11,19,23}), tied with 163 for the k=7
   window's last. Whether chained primes miss TOGETHER is tested
   at scale in explore_cunningham_bias.py (verdict: no bias).

4. MISSED PRIMES ARE SUBSET-SUM FAILURES. A prime s is missed at
   rung k iff {p_i^{-1} mod s : i=1..k} has no subset with sum
   equal to |S|-1 mod s. The criterion is deterministic; the MODEL
   treats the inverses as uniform random values, giving miss
   probability approximately (1 - 1/s)^(2^k - 1) over the 2^k - 1
   subsets. The model's fit is finding 5; its tier is pattern.

5. RANDOM MODEL CONSISTENT AT EVERY RUNG. Observed vs expected
   miss counts agree within sampling noise across k=4..12: the
   worst rung is k=4 (17 missed vs 14.0 expected, z = +1.5); the
   quoted pair k=7 (21.9% vs 22.6%) and k=8 (8.8% vs 9.0%) sit at
   |z| <= 0.1. Miss rate decreases exponentially with k (2^k
   subsets vs Z/s).

6. PERSISTENCE IS THE ABSORPTION RUNG. Prediction is monotone in k
   (the rung-k sub-rings are a subfamily of the rung-(k+1) ones),
   so a "first missed at" rung is a survey-window artifact, never
   an object property. Every miss in the surveyed range is
   absorbed by k=11; the persistence ranking is 281 (k=11), then
   83, 163, 167 (all k=9).

7. NO P+ SIGNAL AT k=7. The largest prime factor of (s-1) shows no
   separation: P+(s-1)/s averages 0.192 over the 7 missed vs 0.184
   over the 25 hit (1.04x). Cunningham chain members have high P+
   (83-1=2*41, 167-1=2*83) but smooth primes are also missed
   (41-1=2^3*5, 109-1=2^2*3^3). A 7-prime sample decides nothing
   alone; the at-scale null is explore_cunningham_bias.py's.
""")

print("=" * 72)
print("  Done. Missed primes mapped.")
print("=" * 72)
