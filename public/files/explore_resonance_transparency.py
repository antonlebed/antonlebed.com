"""Resonance and transparency — the geometry/dynamics interface.

The Ramanujan resonance chain (explore_moment_resonance.py) crossed
with the geometry/dynamics split (explore_tower_geometry.py). The
Ramanujan sum F(n) factors as:
  F(n) = product_{p|N} [1 if p|n, else -1/(p-1)]

Static F depends on {p_i} only (geometry side). But the *dynamical*
resonance spectrum — F(n) for n in the power map orbit (n=1..lambda) —
mixes geometry with dynamics. Transparent primes change the gates
without extending the orbit. Non-transparent primes extend both.

Question: does the dynamical resonance carry different information at
transparent vs non-transparent steps?

FINDINGS (all computed by this script; ranges as stated per item):

1. STATIC RESONANCE IS TRANSPARENCY-BLIND (property). The off-gate
   -1/(p-1) depends only on p, never on whether (p-1) | lambda — read
   off the factorization above; printed k=4..14 in section I.

2. DYNAMICAL RESONANCE SEES TRANSPARENCY (observation, k=3..14). At a
   jump the spectrum's DOMAIN grows (new orbit positions); at a plateau
   the domain is fixed and the new gate re-weights it. The relative
   gain in distinct F values separates cleanly: 0.64..1.50 per jump
   against 0.00..0.18 per plateau (section V).

3. TWO KINDS OF ENRICHMENT — AND THE FIRST PLATEAU SHOWS ONLY ONE
   (observation). At the k=6 plateau the distinct-F count is UNCHANGED
   (17 -> 17, gain 0): re-weighting alone, no new values, yet entropy
   still rises (+0.11 nats, section VII) because the weights move. The
   deep plateaus k=11..14 do mint new values (60, 20, 41, 70) — finer
   subdivision of fixed positions. Jumps add more: entropy delta
   +0.15..+0.34 over the k=7..10 jumps against +0.11 at the one
   plateau the entropy table reaches (k=6; sections II, V, VII).

4. ON/OFF BALANCE DOES NOT FACTOR THROUGH TRANSPARENCY (property).
   The on-count of prime p over one orbit is floor(lambda/p) — exact
   division only when p | lambda — so the balance is set by p alone
   and cannot report whether (p-1) | lambda.

5. THE INTERFACE IS LAMBDA (synthesis of 1-3). WHICH gates fire and
   HOW STRONG they are is geometry; HOW MUCH of that gate structure
   one orbit exposes is set by lambda, the dynamical quantity.

Run: python prime/code/explore_resonance_transparency.py
  (~1 s, peak working set 18.9 MB under the 512 MB watchdog)
"""

from math import gcd, prod, lcm, log, cos, pi
from fractions import Fraction
from collections import Counter
from crt import is_prime, factorize


def section(title):
    print(f"\n{'=' * 72}")
    print(f"  {title}")
    print(f"{'=' * 72}")


def first_n_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes


def tower_lambda(primes):
    result = 1
    for p in primes:
        result = lcm(result, p - 1)
    return result


def ramanujan_F(n, primes):
    """F(n) = product [1 if p|n, else -1/(p-1)] as exact Fraction."""
    result = Fraction(1)
    for p in primes:
        if n % p == 0:
            result *= 1
        else:
            result *= Fraction(-1, p - 1)
    return result


K_MAX = 14
ALL_PRIMES = first_n_primes(K_MAX)


# ═══════════════════════════════════════════════════════════════════════
# I. STATIC GATE STRUCTURE — WHAT ADDING A PRIME DOES TO F(n)
# ═══════════════════════════════════════════════════════════════════════

section("I. STATIC GATE — ADDING A PRIME TO THE RESONANCE")

print("""
  When you add prime p_new to the ring (rung k-1 -> k):
    - For n divisible by p_new: F_k(n) = F_{k-1}(n) * 1 = F_{k-1}(n).
    - For n NOT divisible by p_new: F_k(n) = F_{k-1}(n) * (-1/(p_new-1)).

  The new gate is IDENTICAL for transparent and non-transparent primes
  of the same value. Transparency is invisible to the static gate.
""")

print(f"  {'k':>3} {'p_new':>6} {'trans?':>7} {'gate (off)':>14} "
      f"{'|gate|':>10} {'contrast':>10}")
print(f"  {'-'*55}")

for k in range(4, K_MAX + 1):
    ps = ALL_PRIMES[:k]
    p_new = ps[-1]
    lam = tower_lambda(ps)
    lam_prev = tower_lambda(ps[:-1])
    trans = lam == lam_prev

    gate_off = Fraction(-1, p_new - 1)
    contrast = p_new - 1  # |on/off| = 1 / (1/(p-1)) = p-1

    print(f"  {k:>3} {p_new:>6} {'YES' if trans else '':>7} "
          f"{str(gate_off):>14} {float(abs(gate_off)):>10.6f} "
          f"{contrast:>10}")


# ═══════════════════════════════════════════════════════════════════════
# II. DYNAMICAL RESONANCE SPECTRUM — F(n) FOR n=1..lambda
# ═══════════════════════════════════════════════════════════════════════

section("II. DYNAMICAL RESONANCE SPECTRUM")

print("""
  The power map has period lambda. Evaluating F(n) for n=1..lambda gives
  the "dynamical resonance spectrum" — how the unit group's coherence
  evolves through one full orbit.

  At a lambda JUMP, the orbit extends. At a PLATEAU, it doesn't.
  What happens to the spectrum's information content?
""")

print(f"  {'k':>3} {'p_k':>4} {'type':>8} {'lambda':>8} "
      f"{'distinct F':>11} {'|F|=1 hits':>12} "
      f"{'mean |F|':>10} {'max |F|':>10}")
print(f"  {'-'*80}")

for k in range(3, min(K_MAX + 1, 11)):  # up to k=10 to keep lambda tractable
    ps = ALL_PRIMES[:k]
    lam = tower_lambda(ps)
    lam_prev = tower_lambda(ps[:-1]) if k > 3 else 1
    trans = lam == lam_prev if k > 3 else False
    step = "plateau" if trans else "JUMP"

    # Compute F(n) for n=1..lambda
    f_values = []
    full_hits = 0
    for n in range(1, lam + 1):
        f = ramanujan_F(n, ps)
        f_values.append(f)
        if f == 1:
            full_hits += 1

    distinct_f = len(set(f_values))
    mean_abs_f = sum(abs(float(f)) for f in f_values) / len(f_values)
    max_abs_f = max(abs(float(f)) for f in f_values)

    print(f"  {k:>3} {ps[-1]:>4} {step:>8} {lam:>8,} "
          f"{distinct_f:>11,} {full_hits:>12,} "
          f"{mean_abs_f:>10.6f} {max_abs_f:>10.4f}")


# ═══════════════════════════════════════════════════════════════════════
# III. GATE PATTERN TYPES — HOW MANY DISTINCT GATE CONFIGURATIONS?
# ═══════════════════════════════════════════════════════════════════════

section("III. GATE CONFIGURATIONS")

print("""
  Each n produces a binary gate pattern: which channels are ON (p|n)?
  There are 2^k possible patterns. How many actually appear in n=1..lambda?
  And how does this change at transparent vs non-transparent steps?

  A gate pattern is a subset S of {p_1,...,p_k} — the primes dividing n.
  The number of distinct patterns in 1..lambda is at most 2^k.
""")

print(f"  {'k':>3} {'p_k':>4} {'type':>8} {'lambda':>8} {'2^k':>6} "
      f"{'patterns':>9} {'coverage':>10} {'new patterns':>13}")
print(f"  {'-'*72}")

prev_patterns = set()
for k in range(3, min(K_MAX + 1, 11)):
    ps = ALL_PRIMES[:k]
    lam = tower_lambda(ps)
    lam_prev = tower_lambda(ps[:-1]) if k > 3 else 1
    trans = lam == lam_prev if k > 3 else False
    step = "plateau" if trans else "JUMP"

    # Collect gate patterns
    patterns = set()
    for n in range(1, lam + 1):
        pattern = tuple(1 if n % p == 0 else 0 for p in ps)
        patterns.add(pattern)

    # How many new patterns vs previous rung (projected to first k-1 channels)?
    # Project current patterns to first k-1 channels
    projected = set(pat[:k-1] for pat in patterns)
    new_from_k = len(patterns) - len(projected)  # patterns that differ in the new channel

    coverage = len(patterns) / (2 ** k)

    print(f"  {k:>3} {ps[-1]:>4} {step:>8} {lam:>8,} {2**k:>6} "
          f"{len(patterns):>9} {coverage:>10.2%} {new_from_k:>13}")

    prev_patterns = patterns


# ═══════════════════════════════════════════════════════════════════════
# IV. THE RESONANCE SPECTRUM AT A PLATEAU — WHAT CHANGES?
# ═══════════════════════════════════════════════════════════════════════

section("IV. PLATEAU ANALYSIS: k=5 (jump) vs k=6 (plateau via p=13)")

print("""
  k=5: lambda=60. Adding p=11 (jump: lambda goes 12->60).
  k=6: lambda=60. Adding p=13 (plateau: lambda stays 60).

  Same lambda. Different gate structure. How does the spectrum change?
""")

for k, label in [(5, "k=5 (after jump: +11)"), (6, "k=6 (after plateau: +13)")]:
    ps = ALL_PRIMES[:k]
    lam = tower_lambda(ps)
    phi = prod(p - 1 for p in ps)

    # Collect all F values and their gate patterns
    f_counter = Counter()
    pattern_counter = Counter()

    for n in range(1, lam + 1):
        f = ramanujan_F(n, ps)
        f_counter[f] += 1
        pattern = tuple(1 if n % p == 0 else 0 for p in ps)
        pattern_counter[pattern] += 1

    print(f"\n  {label}: lambda={lam}, k={k}, phi={phi}")
    print(f"  Distinct F values: {len(f_counter)}")
    print(f"  Distinct gate patterns: {len(pattern_counter)}")

    # Show the top F values by frequency
    print(f"\n  {'F value':>20} {'count':>6} {'fraction':>10} {'gate pattern':>25}")
    print(f"  {'-'*65}")
    for f_val, count in f_counter.most_common(10):
        frac = count / lam
        # Find one representative n for this F value
        for n in range(1, lam + 1):
            if ramanujan_F(n, ps) == f_val:
                pattern = tuple(1 if n % p == 0 else 0 for p in ps)
                pat_str = "".join(str(b) for b in pattern)
                break
        print(f"  {str(f_val):>20} {count:>6} {frac:>10.4f} {pat_str:>25}")


# ═══════════════════════════════════════════════════════════════════════
# V. DYNAMICAL REDUNDANCY OF TRANSPARENT PRIMES
# ═══════════════════════════════════════════════════════════════════════

section("V. DYNAMICAL REDUNDANCY OF TRANSPARENT PRIMES")

print("""
  A transparent prime p has (p-1) | lambda. This means the cyclic group
  Z/(p-1) embeds into the existing orbit structure.

  In resonance terms: for n=1..lambda, the pattern of whether p|n repeats
  with period p. Since lambda is unchanged, the number of n in [1,lambda]
  divisible by p is floor(lambda/p) — exact division only when p | lambda
  (it is not here: 13 does not divide 60).

  Compare: for a non-transparent prime p, (p-1) does NOT divide the old
  lambda, so adding p extends lambda by a factor of lcm(old_lam, p-1)/old_lam.
  The resonance spectrum gets NEW orbit positions.
""")

print(f"  Transparent prime redundancy test:")
print(f"  At k=6 (p=13 transparent), lambda=60.")
print(f"  How many of n=1..60 have 13|n? = floor(60/13) = {60 // 13}")
print(f"  These n get gate=1 for channel 13. The other {60 - 60//13} get gate=-1/12.")
print()
print(f"  At k=10 (p=29, jump), lambda goes 7920->55440.")
print(f"  How many of n=1..55440 have 29|n? = {55440 // 29}")
print(f"  At k=11 (p=31, plateau), lambda stays 55440.")
print(f"  How many of n=1..55440 have 31|n? = {55440 // 31}")
print()

# Measure: the "information gain" of adding a prime
# = number of new distinct (F, gate) pairs in the spectrum
print(f"  INFORMATION GAIN per rung (new distinct F values in spectrum):")
print(f"  {'k':>3} {'p_k':>4} {'type':>8} {'lambda':>8} {'distinct F_k':>13} "
      f"{'distinct F_{k-1}':>17} {'gain':>6} {'gain ratio':>11}")
print(f"  {'-'*75}")

prev_distinct = 0
for k in range(3, K_MAX + 1):
    ps = ALL_PRIMES[:k]
    lam = tower_lambda(ps)
    lam_prev = tower_lambda(ps[:-1]) if k > 3 else 1
    trans = lam == lam_prev if k > 3 else False
    step = "plateau" if trans else "JUMP"

    # F(n) is a function of the gate pattern alone (which primes divide n),
    # so collect patterns in one sweep, then one exact product per pattern.
    # This reaches the k=10..14 plateau (lambda 55440) in seconds.
    patterns = set()
    for n in range(1, lam + 1):
        patterns.add(tuple(1 if n % p == 0 else 0 for p in ps))
    f_values = set()
    for pat in patterns:
        f = Fraction(1)
        for p, on in zip(ps, pat):
            if not on:
                f *= Fraction(-1, p - 1)
        f_values.add(f)

    distinct = len(f_values)
    gain = distinct - prev_distinct
    ratio = gain / prev_distinct if prev_distinct > 0 else 0

    print(f"  {k:>3} {ps[-1]:>4} {step:>8} {lam:>8,} {distinct:>13} "
          f"{prev_distinct:>17} {gain:>6} {ratio:>11.2f}")

    prev_distinct = distinct


# ═══════════════════════════════════════════════════════════════════════
# VI. THE ON/OFF BALANCE — TRANSPARENT vs NON-TRANSPARENT
# ═══════════════════════════════════════════════════════════════════════

section("VI. ON/OFF BALANCE ACROSS THE ORBIT")

print("""
  For each prime p at rung k, count how often p's gate is ON (p|n)
  vs OFF over n=1..lambda. The on-fraction = floor(lambda/p)/lambda.

  For small p (like 2,3), the on-fraction is large (many multiples).
  For large p, the on-fraction is small. Does transparency change this?
""")

for k in range(3, min(K_MAX + 1, 11)):
    ps = ALL_PRIMES[:k]
    lam = tower_lambda(ps)
    lam_prev = tower_lambda(ps[:-1]) if k > 3 else 1
    trans = lam == lam_prev if k > 3 else False

    if k >= 5 and k <= 8:
        print(f"\n  k={k} (p_new={ps[-1]}, {'plateau' if trans else 'jump'}, lambda={lam}):")
        print(f"  {'prime':>6} {'on-count':>10} {'off-count':>10} "
              f"{'on-frac':>10} {'E[|gate|]':>10}")
        print(f"  {'-'*50}")
        for p in ps:
            on_count = lam // p
            off_count = lam - on_count
            on_frac = on_count / lam
            # Expected |gate| over the orbit
            e_gate = on_frac * 1 + (1 - on_frac) * (1 / (p - 1))
            print(f"  {p:>6} {on_count:>10} {off_count:>10} "
                  f"{on_frac:>10.4f} {e_gate:>10.6f}")


# ═══════════════════════════════════════════════════════════════════════
# VII. THE SELECTIVITY MEASURE
# ═══════════════════════════════════════════════════════════════════════

section("VII. SELECTIVITY — HOW SHARPLY DOES F(n) DISCRIMINATE?")

print("""
  Selectivity = how well F(n) distinguishes different n values.
  Measure: entropy of the F-value distribution over n=1..lambda.
  Higher entropy = more discriminating = more "information" in the spectrum.
""")

print(f"  {'k':>3} {'p_k':>4} {'type':>8} {'lambda':>8} {'H(F)':>10} "
      f"{'H_max':>8} {'H/H_max':>10} {'d(H)':>8}")
print(f"  {'-'*65}")

prev_H = 0
for k in range(3, min(K_MAX + 1, 11)):
    ps = ALL_PRIMES[:k]
    lam = tower_lambda(ps)
    lam_prev = tower_lambda(ps[:-1]) if k > 3 else 1
    trans = lam == lam_prev if k > 3 else False
    step = "plateau" if trans else "JUMP"

    f_counter = Counter()
    for n in range(1, lam + 1):
        f_counter[ramanujan_F(n, ps)] += 1

    # Shannon entropy
    H = 0
    for count in f_counter.values():
        p_val = count / lam
        if p_val > 0:
            H -= p_val * log(p_val)

    H_max = log(lam)  # maximum entropy = uniform over lambda values
    ratio = H / H_max if H_max > 0 else 0
    d_H = H - prev_H

    print(f"  {k:>3} {ps[-1]:>4} {step:>8} {lam:>8,} {H:>10.4f} "
          f"{H_max:>8.4f} {ratio:>10.4f} {d_H:>+8.4f}")

    prev_H = H


# ═══════════════════════════════════════════════════════════════════════
# VIII. KEY FINDINGS
# ═══════════════════════════════════════════════════════════════════════

section("VIII. KEY FINDINGS")

print("""
1. STATIC RESONANCE IS TRANSPARENCY-BLIND. The gate -1/(p-1) depends
   only on p, not on whether (p-1)|lambda. Adding any prime p modifies
   the spectrum identically: multiply F(n) by -1/(p-1) for n not
   divisible by p. This is the resonance face of the geometry/dynamics
   split (explore_tower_geometry.py).

2. DYNAMICAL RESONANCE SEES TRANSPARENCY. The dynamical spectrum
   (F(n) for n=1..lambda) changes differently at jumps vs plateaus:
   - JUMP: lambda extends, so the DOMAIN of the spectrum grows.
     New orbit positions appear with new F values.
   - PLATEAU: lambda unchanged, so the domain is fixed.
     Existing positions get re-weighted by the new gate.
   The RELATIVE gain in distinct F values separates cleanly:
   0.64..1.50 per jump against 0.00..0.18 per plateau (section V).

3. TWO KINDS OF ENRICHMENT — AND THE FIRST PLATEAU SHOWS ONLY ONE.
   - At a jump, the spectrum gets WIDER (more positions, more values).
   - At the k=6 plateau the distinct-F count is UNCHANGED (17 -> 17):
     re-weighting alone, yet entropy still rises (+0.11 nats) because
     the weights move. The deep plateaus k=11..14 do mint new values
     (60, 20, 41, 70) — finer subdivision of fixed positions.
   Jumps add more entropy: +0.15..+0.34 over k=7..10 against +0.11 at
   the one plateau the entropy table reaches.

4. ON/OFF BALANCE. For prime p, the on-fraction over one orbit is
   floor(lambda/p)/lambda ~ 1/p. Large primes are mostly OFF (small
   gate contribution). The balance is fixed by p alone, so it does not
   factor through transparency: it cannot report whether (p-1) divides
   lambda, and it moves whenever p moves whether or not lambda does.

5. THE GEOMETRY/DYNAMICS INTERFACE. The Ramanujan sum F(n) lives at
   the intersection:
   - WHICH gates fire (p|n) = geometry (depends on n and the primes)
   - HOW LONG the orbit runs (lambda) = dynamics (depends on p-1)
   - HOW STRONG each gate is (1/(p-1)) = geometry again
   The interface is lambda: it's the dynamical quantity that limits
   how much of the geometric gate structure you actually see.
""")

print("=" * 72)
print("  Done. Resonance-transparency cross-link mapped.")
print("=" * 72)
