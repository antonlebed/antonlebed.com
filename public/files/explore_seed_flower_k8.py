"""Seed-flower at k=8: does the naming of absent primes extend to Z/9699690?

Call a pair {p, q} of tower primes a PREDICTION when its -chi =
(p-1)(q-1) - 1 is itself a tower prime — necessarily absent from the pair.
At k=7 (RAD, 127 sub-rings) there are five; four are proved as algebraic
identities under the consecutive-prime parametrization
(explore_seed_flower_proof.py), the fifth is the linear 2-root law p - 2.
At k=8 (+19, 255 sub-rings), two new predictions appear:
  {3, 11} -> 19  (19 was an intruder at k=7, now a tower prime at k=8)
  {2, 19} -> 17

This script maps all 255 non-empty thin sub-rings of Z/9699690, checks how
the prediction/smoothness/naming structure extends, identifies the root
patterns (2-rooted, 3-rooted) that generate every prediction at k <= 8, and
verifies the p_k+1 factorization rule against an exhaustive pair scan for
k = 3..24.

Run: python prime/code/explore_seed_flower_k8.py
Resources: ~13 MB peak working set, ~0.3 s wall (memwatch, 512 MB ceiling).
"""

from itertools import combinations
from math import prod
from collections import Counter
from crt import factorize, is_prime, lcm_list

PRIMES_7 = [2, 3, 5, 7, 11, 13, 17]
PRIMES_8 = [2, 3, 5, 7, 11, 13, 17, 19]

NAMES = {2: '2', 3: '3', 5: '5', 7: '7', 11: '11', 13: '13', 17: '17', 19: '19'}


def neg_chi_thin(ps):
    k = len(ps)
    N = prod(ps)
    return N * (k - 1) - sum(N // p for p in ps)


def factor_str(n):
    if n == 0: return "0"
    if n == 1: return "1"
    sign = ""
    if n < 0:
        sign = "-"
        n = -n
    f = factorize(n)
    parts = []
    for p in sorted(f):
        name = NAMES.get(p, str(p))
        e = f[p]
        parts.append(name if e == 1 else f"{name}^{e}")
    return sign + "*".join(parts)


def tower_smooth(n, primes):
    if n == 0 or abs(n) == 1:
        return True
    f = factorize(abs(n))
    return all(p in set(primes) for p in f)


def intruder_primes(n, primes):
    if n == 0 or abs(n) == 1:
        return []
    f = factorize(abs(n))
    return sorted(p for p in f if p not in set(primes))


def section(title):
    print(f"\n{'=' * 76}")
    print(f"  {title}")
    print(f"{'=' * 76}")


def compute_all_subrings(primes):
    results = []
    k = len(primes)
    for size in range(1, k + 1):
        for subset in combinations(range(k), size):
            ps = [primes[i] for i in subset]
            nc = neg_chi_thin(ps)
            absent = [p for p in primes if p not in ps]
            named = []
            if nc > 1:
                f = factorize(abs(nc))
                named = [p for p in f if p in set(primes) and p not in ps]
            results.append({
                'primes': ps, 'size': size, 'N': prod(ps), 'neg_chi': nc,
                'smooth': tower_smooth(nc, primes),
                'factors': factor_str(nc),
                'intruders': intruder_primes(nc, primes),
                'absent': absent, 'named': named,
            })
    return results


def main():
    print("=" * 76)
    print("SEED-FLOWER AT k=8: do the absent-prime predictions extend to Z/9699690?")
    print("=" * 76)
    print()
    print("Z/9699690 = 2*3*5*7*11*13*17*19.  8 channels, 255 non-empty sub-rings.")
    lam = lcm_list([p - 1 for p in PRIMES_8])
    print(f"Lambda = lcm(p_i - 1, i=1..8) = {lam}.")
    print()

    results_7 = compute_all_subrings(PRIMES_7)
    results_8 = compute_all_subrings(PRIMES_8)

    # ═══════════════════════════════════════════════════════════════
    # I. 2-PRIME PREDICTIONS: k=7 vs k=8
    # ═══════════════════════════════════════════════════════════════

    section("I. 2-PRIME PREDICTIONS")

    print("""
For thin Z/(p*q): -chi = (p-1)(q-1) - 1.
A pair {p,q} PREDICTS prime r if -chi = r, r is a tower prime, r not in {p,q}.
""")

    def find_predictions(primes):
        preds = []
        for i in range(len(primes)):
            for j in range(i + 1, len(primes)):
                p, q = primes[i], primes[j]
                nc = (p - 1) * (q - 1) - 1
                if is_prime(nc) and nc in set(primes) and nc != p and nc != q:
                    preds.append((p, q, nc))
        return preds

    preds_7 = find_predictions(PRIMES_7)
    preds_8 = find_predictions(PRIMES_8)

    print("  k=7 predictions (RAD):")
    for p, q, r in preds_7:
        label = f"{{{NAMES[p]},{NAMES[q]}}}"
        print(f"    {label:<12} -chi = ({p-1})({q-1})-1 = {(p-1)*(q-1)-1:>3} -> {r}")
    print(f"    Total: {len(preds_7)}")

    print()
    print("  k=8 predictions (RUNG5):")
    preds_7_set = {(p, q) for p, q, _ in preds_7}
    for p, q, r in preds_8:
        label = f"{{{NAMES[p]},{NAMES[q]}}}"
        new = " ** NEW **" if (p, q) not in preds_7_set else ""
        print(f"    {label:<12} -chi = ({p-1})({q-1})-1 = {(p-1)*(q-1)-1:>3} -> {r}{new}")
    print(f"    Total: {len(preds_8)}")

    print()
    print("  New predictions at k=8:")
    for p, q, r in preds_8:
        if (p, q) not in preds_7_set:
            label = f"{{{NAMES[p]},{NAMES[q]}}}"
            print(f"    {label} -> {r}")

    # ═══════════════════════════════════════════════════════════════
    # II. ROOT PATTERNS
    # ═══════════════════════════════════════════════════════════════

    section("II. ROOT PATTERNS -- why roots 2 and 3 generate every k=8 prediction")

    print("""
The ROOT of a pair is its smaller prime, so each pair is classified once.
For {root, p}, p > root: -chi = (root - 1)(p - 1) - 1.
The root's totient controls the growth rate:
  2-rooted (totient 1): -chi = p - 2     (twin prime offset)
  3-rooted (totient 2): -chi = 2p - 3    (Sophie-Germain-flavored)
  5-rooted (totient 4): -chi = 4p - 5    (fast growth, few hits)
  7-rooted (totient 6): -chi = 6p - 7    (fastest growth)
""")

    for root in [2, 3, 5, 7]:
        tot = root - 1
        print(f"  {root}-rooted (totient {tot}): -chi = {tot}*p - {tot+1}")
        hits = []
        for p in PRIMES_8:
            if p <= root:
                continue
            nc = (root - 1) * (p - 1) - 1
            hit = is_prime(nc) and nc in set(PRIMES_8) and nc != root and nc != p
            status = f"= {nc:>3} = {NAMES.get(nc, '?')}" if hit else f"= {nc:>3} = {factor_str(nc)}"
            marker = "  <-- PREDICTION" if hit else ""
            hits.append(hit)
            print(f"    {{{root},{NAMES[p]}}}  ({tot})*({p-1})-1 {status}{marker}")
        print(f"    Predictions with root {root}: {sum(hits)}")
        print()

    # ═══════════════════════════════════════════════════════════════
    # III. ALGEBRAIC IDENTITY ANALYSIS
    # ═══════════════════════════════════════════════════════════════

    section("III. ALGEBRAIC IDENTITIES FOR NEW PREDICTIONS")

    print("""
At k=7, four predictions are algebraic identities under the
consecutive-prime parametrization (explore_seed_flower_proof.py):
  {2,5}->3: (2x+1)(x-2)=0    {2,7}->5: (3x+1)(x-2)=0     (x = p_1)
  {3,5}->7: (2y-1)(y-3)=0    {3,7}->11: 2y(y-3)=0        (y = p_2)

Plus {2,13}->11: (2-1)(13-1)-1 = 11.
  For p_1=2: -chi = p-2 for any p. So {2,13}->13-2 = 11.

New at k=8:
""")

    # {2, 19} -> 17
    print("  {2, 19} -> 17:")
    print(f"    -chi = (2-1)(19-1) - 1 = 19 - 2 = 17")
    print(f"    For root 2: -chi = p - 2 for ANY p. This is the 2-root identity.")
    print(f"    It predicts whenever p-2 is prime AND in the tower set.")
    print(f"    Connection: p and p-2 are a TWIN PRIME PAIR.")
    print(f"    At k=8, twin pairs in tower set: (5,3), (7,5), (13,11), (19,17).")
    print()

    twin_pairs_in_tower = []
    for p in PRIMES_8:
        if p - 2 in set(PRIMES_8) and p > 2:
            twin_pairs_in_tower.append((p, p - 2))
    print(f"    Twin pairs: {twin_pairs_in_tower}")
    d_predictions = [(p, p - 2) for p in PRIMES_8 if p > 2 and p - 2 in set(PRIMES_8) and p - 2 != 2]
    print(f"    2-rooted predictions: {{2,p}} -> p-2 for p in {[p for p, _ in d_predictions]}")
    print()

    # {3, 11} -> 19
    print("  {3, 11} -> 19:")
    print(f"    -chi = (3-1)(11-1) - 1 = 2*10 - 1 = 19")
    print(f"    For root 3: -chi = 2(p-1) - 1 = 2p - 3 for any p.")
    print()
    print(f"    The 3-root law: set 2p - 3 = r where r is a target prime.")
    print(f"    Then p = (r+3)/2. Need p to be a tower prime.")
    print(f"    r=19: p = 11. CHECK: {{3,11}} -> 19. Correct.")
    print()
    print(f"    Root 3 predicts r whenever (r+3)/2 is a tower prime and r != 3.")
    k_predictions = []
    for p in PRIMES_8:
        if p == 3:
            continue
        nc = 2 * (p - 1) - 1
        if is_prime(nc) and nc in set(PRIMES_8) and nc != 3 and nc != p:
            k_predictions.append((p, nc))
    print(f"    3-rooted predictions: {{3,p}} -> 2p-3 for p in {[(p, nc) for p, nc in k_predictions]}")
    print()

    # Check: does {3,11}->19 have a polynomial factoring like the k=7 ones?
    print("  Polynomial analysis for {3, 11} -> 19:")
    print(f"    11 = 4*3 - 1, so with y = p_2 and partner 4y - 1:")
    print(f"    -chi = (y-1)(4y-2) - 1 = 4y^2 - 6y + 1.")
    print(f"    Setting equal to the constant 19: 4y^2 - 6y - 18 = 2(2y+3)(y-3) = 0.")
    print(f"      Roots: y = 3 and y = -3/2.")
    print()
    print(f"    The (y-3) factor RESTATES the arithmetic: 19 enters as a constant,")
    print(f"    so y = 3 is a root exactly when this pair's -chi equals 19 -- one")
    print(f"    numeric check, not a new identity. The four k=7 identities carry")
    print(f"    more: there the target is itself parametrized by the")
    print(f"    consecutive-prime rules (explore_seed_flower_proof.py), so each")
    print(f"    identity holds across the whole seed family, with the seed its")
    print(f"    only prime root -- a uniqueness statement, not one check.")
    print()

    # ═══════════════════════════════════════════════════════════════
    # IV. COMPLETE 2-PRIME TABLE AT k=8
    # ═══════════════════════════════════════════════════════════════

    section("IV. COMPLETE 2-PRIME TABLE AT k=8")

    print(f"\n  {'pair':<12} {'(p-1)(q-1)-1':>14} {'factors':>20}  {'prime?':>6}  result")
    print(f"  {'-'*70}")

    for i in range(8):
        for j in range(i + 1, 8):
            p, q = PRIMES_8[i], PRIMES_8[j]
            nc = (p - 1) * (q - 1) - 1
            fs = factor_str(nc)
            is_p = is_prime(nc) if nc > 1 else False
            label = f"{{{NAMES[p]},{NAMES[q]}}}"
            pred = ""
            if is_p and nc in set(PRIMES_8) and nc != p and nc != q:
                pred = f"PREDICTS {NAMES[nc]}"
            elif is_p and nc in set(PRIMES_8):
                pred = f"= self ({NAMES[nc]})"
            elif is_p:
                pred = f"prime {nc} (not in tower)"
            else:
                pred = f"composite"
            print(f"  {label:<12} {nc:>14} {fs:>20}  {'YES' if is_p else 'no':>6}  {pred}")

    # ═══════════════════════════════════════════════════════════════
    # V. SMOOTHNESS COMPARISON
    # ═══════════════════════════════════════════════════════════════

    section("V. SMOOTHNESS SCALING: k=7 vs k=8")

    print()
    print(f"  {'size':<6} {'k=7 smooth':>12} {'k=7 total':>10} {'k=7 %':>8}   "
          f"{'k=8 smooth':>12} {'k=8 total':>10} {'k=8 %':>8}")
    print(f"  {'-'*80}")

    for size in range(1, 9):
        r7 = [r for r in results_7 if r['size'] == size]
        r8 = [r for r in results_8 if r['size'] == size]
        s7 = sum(1 for r in r7 if r['smooth'])
        t7 = len(r7)
        s8 = sum(1 for r in r8 if r['smooth'])
        t8 = len(r8)
        col7 = f"{s7}/{t7}" if t7 else "-"
        pct7 = f"{s7/t7:.0%}" if t7 else "-"
        col8 = f"{s8}/{t8}" if t8 else "-"
        pct8 = f"{s8/t8:.0%}" if t8 else "-"
        print(f"  {size:<6} {col7:>12} {t7:>10} {pct7:>8}   {col8:>12} {t8:>10} {pct8:>8}")

    total_7 = len(results_7)
    smooth_7 = sum(1 for r in results_7 if r['smooth'])
    total_8 = len(results_8)
    smooth_8 = sum(1 for r in results_8 if r['smooth'])
    print(f"  {'ALL':<6} {f'{smooth_7}/{total_7}':>12} {total_7:>10} {smooth_7/total_7:>8.0%}   "
          f"{f'{smooth_8}/{total_8}':>12} {total_8:>10} {smooth_8/total_8:>8.0%}")

    # ═══════════════════════════════════════════════════════════════
    # VI. INTRUDER COMPARISON
    # ═══════════════════════════════════════════════════════════════

    section("VI. INTRUDER PRIMES: k=7 vs k=8")

    int7 = Counter()
    for r in results_7:
        for p in r['intruders']:
            int7[p] += 1

    int8 = Counter()
    for r in results_8:
        for p in r['intruders']:
            int8[p] += 1

    all_intruders = sorted(set(int7.keys()) | set(int8.keys()))

    print(f"\n  {'prime':>6}  {'k=7 count':>10}  {'k=8 count':>10}  notes")
    print(f"  {'-'*50}")
    for p in all_intruders[:20]:
        c7 = int7.get(p, 0)
        c8 = int8.get(p, 0)
        note = ""
        if p == 19:
            note = "was intruder at k=7, NOW TOWER PRIME at k=8"
        elif c8 == 0 and c7 > 0:
            note = "vanished at k=8"
        elif c8 > c7:
            note = f"+{c8-c7}"
        print(f"  {p:>6}  {c7:>10}  {c8:>10}  {note}")

    print(f"\n  Distinct intruders: k=7 = {len(int7)}, k=8 = {len(int8)}")

    # 19 specifically: how many k=7 sub-rings had 19 as intruder?
    int19_at_7 = sum(1 for r in results_7 if 19 in r['intruders'])
    print(f"  19 appeared as intruder in {int19_at_7} sub-rings at k=7.")
    print(f"  At k=8, 19 is a tower prime — those sub-rings become smoother or gain new named primes.")

    # ═══════════════════════════════════════════════════════════════
    # VII. WHO NAMES 19?
    # ═══════════════════════════════════════════════════════════════

    section("VII. WHO NAMES 19? (new at k=8)")

    print(f"\nSub-rings whose -chi is divisible by 19 but don't contain 19:")
    namers = [r for r in results_8 if 19 in r['named']]
    for r in namers:
        label = "{" + ",".join(NAMES[p] for p in r['primes']) + "}"
        print(f"  {label:<25} -chi = {r['neg_chi']:>10} = {r['factors']}")
    print(f"  Total: {len(namers)} sub-rings name 19.")

    # ═══════════════════════════════════════════════════════════════
    # VIII. 3-PRIME PREDICTIONS AT k=8
    # ═══════════════════════════════════════════════════════════════

    section("VIII. 3-PRIME SUB-RINGS — NEW PATTERNS AT k=8")

    print("\nFor thin {p,q,r}: -chi = 2pqr - pq - pr - qr.")
    print("Checking: -chi divisible by absent tower primes?\n")

    three_prime_8 = [r for r in results_8 if r['size'] == 3]

    print(f"  {'subset':<20} {'-chi':>10} {'factors':<30} {'names tower p':>15}")
    print(f"  {'-'*80}")

    naming_3 = 0
    for r in three_prime_8:
        label = "{" + ",".join(NAMES[p] for p in r['primes']) + "}"
        named_str = ",".join(NAMES[p] for p in r['named']) if r['named'] else "-"
        if r['named']:
            naming_3 += 1
        print(f"  {label:<20} {r['neg_chi']:>10} {r['factors']:<30} {named_str:>15}")

    print(f"\n  3-prime sub-rings naming an absent tower prime: {naming_3}/{len(three_prime_8)}")

    # ═══════════════════════════════════════════════════════════════
    # IX. THE SCALING LAW
    # ═══════════════════════════════════════════════════════════════

    section("IX. PREDICTION GROWTH: THE p_k+1 FACTORIZATION RULE")

    print("""
New predictions at rung k come from two sources:
  (A) TWIN: {2, p_k} -> p_k-2, fires iff p_k-2 is prime (twin pair).
  (B) TARGET: {p_i, p_j} -> p_k, fires for each factorization
      p_k+1 = (p_i-1)(p_j-1) with p_i, p_j both primes < p_k.

So: new_preds(k) = twin(p_k) + |{(a,b): ab = p_k+1, a+1 and b+1 primes < p_k}|.
Primes where p+1 is highly factorable are "rich" rungs for the seed-flower.

The "scan" column is the INDEPENDENT check: the number of predictions at
rung k counted by exhaustive scan over all pairs of the first k primes.
The rule holds iff the cumulative formula total matches it at every rung.
""")

    def first_k_primes(k_val):
        ps = []
        n = 2
        while len(ps) < k_val:
            if is_prime(n):
                ps.append(n)
            n += 1
        return ps

    def count_predictions_scan(primes_list):
        s = set(primes_list)
        n = 0
        for a_i in range(len(primes_list)):
            for b_i in range(a_i + 1, len(primes_list)):
                nc = (primes_list[a_i] - 1) * (primes_list[b_i] - 1) - 1
                if nc in s and nc != primes_list[a_i] and nc != primes_list[b_i]:
                    n += 1
        return n

    cum_preds = 0
    mismatches = []
    print(f"  {'k':>3} {'p_k':>4} {'p_k+1':>6} {'twin':>5} {'#tgt':>5} {'new':>4} {'total':>5} {'scan':>5}  target factorizations")
    print(f"  {'-'*84}")
    for k_test in range(3, 25):
        primes_k = first_k_primes(k_test)
        pk = primes_k[-1]
        prev_set = set(primes_k[:-1])

        twin_val = 1 if is_prime(pk - 2) and pk - 2 >= 2 else 0
        target = pk + 1
        facts = []
        for a in range(1, int(target**0.5) + 1):
            if target % a == 0:
                bv = target // a
                if a + 1 in prev_set and bv + 1 in prev_set:
                    facts.append((a + 1, bv + 1))
        new_count = twin_val + len(facts)
        cum_preds += new_count
        scan = count_predictions_scan(primes_k)
        if scan != cum_preds:
            mismatches.append((k_test, cum_preds, scan))
        fact_str = ", ".join(f"{{{p},{q}}}" for p, q in facts) if facts else "-"
        print(f"  {k_test:>3} {pk:>4} {pk+1:>6} {twin_val:>5} {len(facts):>5} {new_count:>4} {cum_preds:>5} {scan:>5}  {fact_str}")

    if mismatches:
        print(f"\n  MISMATCH (k, formula, scan): {mismatches}")
    else:
        print(f"\n  VERIFIED k=3..24: the cumulative formula total equals the")
        print(f"  exhaustive pair scan at every rung.")

    # ═══════════════════════════════════════════════════════════════
    # X. KEY FINDINGS
    # ═══════════════════════════════════════════════════════════════

    section("X. KEY FINDINGS")

    print(f"""
1. SEED-FLOWER EXTENDS TO k=8.
   {len(preds_8)} predictions at k=8 (vs {len(preds_7)} at k=7).
   New predictions: {{3,11}}->19 and {{2,19}}->17.

2. ROOT PATTERNS: 2-root tracks twin primes (p -> p-2), 3-root tracks
   2p-3 pairs. These generate all predictions at k<=8. At k=9, 5-root
   contributes {{5,7}}->23 (first higher-root prediction).

3. THE {{3,11}}->19 PREDICTION FOLLOWS THE 3-ROOT LAW -chi = 2p - 3.
   Its polynomial form 4y^2 - 6y - 18 = 2(2y+3)(y-3) has the root
   y = 3, but with the target 19 entering as a constant that root
   restates the arithmetic; the content of the k=7 identities (target
   parametrized by the consecutive-prime rules,
   explore_seed_flower_proof.py) does not transfer.

4. THE p_k+1 FACTORIZATION RULE ({'verified k=3..24 against the exhaustive'
   if not mismatches else 'MISMATCHED against the'} pair scan, section IX):
   New predictions at rung k = twin(p_k) + #factorizations of p_k+1
   as (p_i-1)(p_j-1) with p_i, p_j both smaller tower primes.
   "Rich" rungs are those where p_k+1 is highly composite (e.g.,
   p=71, 72=2^3*3^2 -> 3 new predictions). "Barren" rungs have
   p_k+1 with no usable factorizations (e.g., p=29, 30=2*3*5 but
   no factorization yields two prime-minus-one values).

5. 2-rooted 2-pairs are always tower-smooth: p-2 < p, so all its
   prime factors are below p and hence in the tower set.
""")

    print("=" * 76)
    print("  Done. 255 sub-rings computed at k=8.")
    print("=" * 76)


if __name__ == "__main__":
    main()
