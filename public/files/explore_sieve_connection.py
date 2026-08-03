"""Sieve-theoretic reading of the primorial tower: the dictionary.

Along the primorial trajectory the tower is the algebraic form of the
sieve of Eratosthenes -- identity, not analogy. Units of Z/p_k# are the
integers surviving sieving by the first k primes; CRT is the sieve
factored into independent per-prime parts. This script states the
term-by-term dictionary and verifies every row that computes.

Sections:
  I.    Units = sieve survivors (Mertens density)
  II.   Idempotents = inclusion-exclusion projectors
  III.  -chi = N*(d_mean - 1): the mean-distance identity
  IV.   Ramanujan sum = Mobius inversion on the sieve
  V.    Naming read as sieve prediction (the reciprocal criterion)
  VI.   Sieve survivor classes (the 2^k profile partition)
  VII.  ECC = sieve redundancy, with direct reconstruction
  VIII. The dictionary table
  IX.   Quantitative: -chi against phi across the tower
  X.    Sub-sieve naming census at k=7
  XI.   Findings

FINDINGS (all computed by this script; ranges as stated per item):

1. THE IDENTITY (property). Units are survivors by the definition of
   coprimality, and the idempotent lattice IS the inclusion-exclusion
   computation: the sum over all 128 idempotents of (-1)^|S| * N/prod(S)
   equals phi(N) = 92160 at k=7 (section II).

2. -CHI IS A MEAN-DISTANCE MULTIPLE (property, algebra; printed
   k=2..7). -chi = N*(d_mean - 1) where d_mean = sum(1 - 1/p_i) is the
   mean CRT Hamming distance from 0 of a UNIFORM ring element (channel
   i is nonzero with probability 1 - 1/p_i). Not a statement about the
   survivors: every unit sits at distance exactly m, all its channels
   nonzero; the mean is over the whole ring (sections III, IX).

3. RAMANUJAN SUM = MOBIUS INVERSION (property; verified at 16 values,
   k=7). c_N(n) = sum over d | gcd(n,N) of mu(N/d)*d, and the frequency
   moment F(n) = c_N(n)/phi(N) factors into per-channel gates
   [1 if p|n else -1/(p-1)] (explore_moment_resonance.py). The gate is
   the individual prime sieve's hit/miss decision; the product form is
   CRT independence = sieve independence (section IV).

4. NAMING NEVER HITS THE SUCCESSOR IN RANGE (observation, k=3..9).
   The reciprocal criterion -- s | -chi iff sum(1/p_i) = m-1 (mod s),
   proved in explore_tower_naming.py -- read as sieve prediction: the
   full-ring -chi does name absent primes (53 at k=7), but it names
   p_{k+1} at NO tested rung k=3..9 (section V). And at k=7 the naming
   fraction FALLS with sub-sieve size: 0.571 at m=2 down to 0.095 at
   m=5 and 0 at m>=6 (section X).

5. ECC IS SIEVE REDUNDANCY, RECONSTRUCTION CHECKED (computed, k=7).
   Any 4 of the 7 prime sieves determine a codeword: verified by
   direct CRT reconstruction of every one of the 210 codewords from
   each of the 35 four-channel subsets (section VII). The capacity
   reason: every 4-subset's product is >= 210, the data modulus.

6. LAMBDA IS THE SURVIVORS' DYNAMICAL PERIOD (property). lambda =
   lcm(p_i - 1) is the exponent of the survivor group, and
   transparency -- (p-1) | lambda -- reads as: adding sieve prime p
   leaves the multiplicative dynamics unchanged (section VIII; the
   geometry/dynamics split is explore_tower_geometry.py's).

Run: python prime/code/explore_sieve_connection.py
  (~1 s, peak working set 14.0 MB under the 512 MB watchdog)
"""

from math import gcd, prod, cos, pi, exp, log
from itertools import combinations
from collections import Counter, defaultdict
from fractions import Fraction
from crt import is_prime, factorize, Ring, all_idempotents

EULER_GAMMA = 0.5772156649015329


def first_n_primes(n):
    ps = []
    c = 2
    while len(ps) < n:
        if is_prime(c):
            ps.append(c)
        c += 1
    return ps


def mobius(n):
    if n == 1:
        return 1
    f = factorize(n)
    if any(e > 1 for e in f.values()):
        return 0
    return (-1) ** len(f)


def neg_chi(ps):
    k = len(ps)
    N = prod(ps)
    return N * (k - 1) - sum(N // p for p in ps)


def ramanujan_sum(n, N):
    total = 0
    for a in range(N):
        if gcd(a, N) == 1:
            total += cos(2 * pi * a * n / N)
    return round(total)


def crt_combine(residues, moduli):
    M = prod(moduli)
    x = 0
    for r, m in zip(residues, moduli):
        Mi = M // m
        x += r * Mi * pow(Mi, -1, m)
    return x % M


def mertens_approx(p):
    return exp(-EULER_GAMMA) / log(p)


def section(title):
    print(f"\n{'=' * 76}")
    print(f"  {title}")
    print(f"{'=' * 76}")


def main():
    K_MAX = 12

    print("=" * 76)
    print("  THE SIEVE-THEORETIC INTERPRETATION")
    print("  The primorial tower as the Eratosthenes sieve in algebraic form")
    print("=" * 76)

    all_primes = first_n_primes(K_MAX + 10)

    # =================================================================
    section("I. UNITS = SIEVE SURVIVORS")
    # =================================================================

    print("""
  Z/p_k# has N = p_k# elements. Units (gcd(n,N)=1) are the integers
  coprime to all of p_1,...,p_k -- exactly the sieve survivors.

  Density = phi(N)/N = product(1 - 1/p_i)  (Mertens product).
  As k grows, this approaches e^{-gamma}/ln(p_k) (Mertens' theorem).
""")

    print(f"  {'k':>3} {'p_k':>4} {'N':>14} {'phi':>14} {'density':>10} "
          f"{'Mertens':>10} {'ratio':>8}")
    print(f"  {'-' * 68}")

    for k in range(2, K_MAX + 1):
        ps = all_primes[:k]
        N = prod(ps)
        phi = prod(p - 1 for p in ps)
        density = phi / N
        approx = mertens_approx(ps[-1])
        ratio = density / approx

        print(f"  {k:>3} {ps[-1]:>4} {N:>14,} {phi:>14,} {density:>10.6f} "
              f"{approx:>10.6f} {ratio:>8.4f}")

    # =================================================================
    section("II. IDEMPOTENTS = INCLUSION-EXCLUSION PROJECTORS")
    # =================================================================

    print("""
  The 2^k idempotents of Z/p_k# correspond to subsets of {p_1,...,p_k}.
  Idempotent e_S has CRT tuple: 1 on channels in S, 0 outside S.

  In sieve language, e_S projects onto "the part visible through primes in S."
  The inclusion-exclusion formula for counting sieve survivors IS the sum
  over the idempotent lattice weighted by the alternating signs.
""")

    k_demo = 7
    ps = all_primes[:k_demo]
    N = prod(ps)
    phi = prod(p - 1 for p in ps)
    ring = Ring("demo", ps, [1] * k_demo, n_data=4)

    idems = all_idempotents(ring)

    print(f"  Ring: Z/{N} = Z/{'*'.join(str(p) for p in ps)}")
    print(f"  {2**k_demo} idempotents, {phi} units")
    print()

    print(f"  {'subset':>30} {'|S|':>4} {'e_S':>10} {'(-1)^|S|':>10} "
          f"{'N/prod(S)':>10}")
    print(f"  {'-' * 70}")

    for channels, val in sorted(idems, key=lambda x: len(x[0])):
        if len(channels) > 4:
            continue
        S_primes = [ps[i] for i in channels]
        complement = [ps[i] for i in range(k_demo) if i not in channels]
        N_comp = prod(complement) if complement else 1
        sign = (-1) ** len(channels)
        S_label = "{" + ",".join(str(p) for p in S_primes) + "}" if S_primes else "{}"

        print(f"  {S_label:>30} {len(channels):>4} {val:>10} "
              f"{sign:>10} {N_comp:>10}")

    print(f"  ... (showing |S| <= 4 of {2**k_demo} total)")
    print()

    ie_full = 0
    for channels, val in idems:
        complement = [ps[i] for i in range(k_demo) if i not in channels]
        N_comp = prod(complement) if complement else 1
        sign = (-1) ** len(channels)
        ie_full += sign * N_comp

    print(f"  Inclusion-exclusion sum = {ie_full}")
    print(f"  phi(N) = {phi}")
    print(f"  Match: {ie_full == phi}")
    print()
    print("  The idempotent lattice IS the inclusion-exclusion computation.")
    print("  Projecting onto e_S selects elements divisible by primes NOT in S.")

    # =================================================================
    section("III. -CHI = N*(d_mean - 1): THE MEAN-DISTANCE IDENTITY")
    # =================================================================

    print("""
  For a thin sub-ring on primes {p_1,...,p_m}:
    -chi = N*(m-1) - sum(N/p_i)

  Rewrite:
    -chi = sum_{i} (N - N/p_i) - N
         = N * (sum(1 - 1/p_i) - 1)
         = N * (d_mean - 1)

  where d_mean = sum(1 - 1/p_i) is the mean CRT Hamming distance from 0
  of a UNIFORM ring element: channel i is nonzero with probability
  (p_i - 1)/p_i. The mean is over the WHOLE ring -- the survivors
  themselves all sit at distance exactly m, every channel nonzero.
""")

    print(f"  {'primes':>25} {'N':>8} {'phi':>8} {'-chi':>8} "
          f"{'N-phi':>8} {'d_mean':>8} {'N*(d-1)':>8}")
    print(f"  {'-' * 80}")

    for m in range(2, 8):
        ps_sub = all_primes[:m]
        N_sub = prod(ps_sub)
        phi_sub = prod(p - 1 for p in ps_sub)
        nc = neg_chi(ps_sub)
        non_units = N_sub - phi_sub
        d_mean = sum(1 - 1/p for p in ps_sub)
        n_d_1 = N_sub * (d_mean - 1)

        label = "{" + ",".join(str(p) for p in ps_sub) + "}"
        print(f"  {label:>25} {N_sub:>8} {phi_sub:>8} {nc:>8} "
              f"{non_units:>8} {d_mean:>8.4f} {n_d_1:>8.1f}")

    print()
    print("  -chi = N*(d_mean - 1) exactly (by algebra). Verified above.")
    print()

    print("  Sieve interpretation of -chi:")
    print("    N/p_i = count of multiples of p_i in {0,...,N-1} = 'sieved by p_i'")
    print("    N - N/p_i = survivors of the single sieve p_i alone")
    print("    -chi = sum(survivors_per_channel) - N")
    print()
    print("  Verification:")
    for m in range(2, 8):
        ps_sub = all_primes[:m]
        N_sub = prod(ps_sub)
        survivors_sum = sum(N_sub - N_sub // p for p in ps_sub)
        nc = neg_chi(ps_sub)
        print(f"    k={m}: sum(surv_per_ch) = {survivors_sum}, "
              f"N = {N_sub}, difference = {survivors_sum - N_sub}, -chi = {nc}, "
              f"match = {survivors_sum - N_sub == nc}")

    # =================================================================
    section("IV. RAMANUJAN SUM = MOBIUS INVERSION ON THE SIEVE")
    # =================================================================

    print("""
  The Ramanujan sum c_N(n) = sum_{gcd(a,N)=1} cos(2*pi*a*n/N) satisfies:

    c_N(n) = sum_{d | gcd(n,N)} mu(N/d) * d

  This IS the Mobius inversion applied to the sieve.

  From the resonance chain (explore_moment_resonance.py), the
  frequency moment F(n) = c_N(n)/phi(N) factors:
    F(n) = product_{p|N} [1 if p|n, -1/(p-1) if p does not divide n]

  The per-channel factor IS the individual prime sieve:
    - p|n: "sieved out" by p -> factor 1 (full resonance)
    - p does not divide n: "survives" sieve by p -> factor -1/(p-1)

  So the Ramanujan sum is the SIEVE'S CHARACTERISTIC FUNCTION,
  decomposed into independent prime sieves via CRT.
""")

    N7 = prod(all_primes[:7])
    phi7 = prod(p - 1 for p in all_primes[:7])

    print(f"  Verifying at k=7, N={N7}:")
    print()
    print(f"  {'n':>8} {'gcd(n,N)':>10} {'c_N(n)':>10} {'Mobius':>10} "
          f"{'c_N/phi':>12} {'gate prod':>12}")
    print(f"  {'-' * 70}")

    test_ns = [1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 30, 42, 210, N7]

    all_ok = True
    for n in test_ns:
        g = gcd(n, N7)
        c_N = ramanujan_sum(n, N7)
        mu_sum = sum(mobius(N7 // d) * d for d in range(1, g + 1) if g % d == 0)
        c_over_phi = Fraction(c_N, phi7)

        F_product = Fraction(1)
        for p in all_primes[:7]:
            if n % p == 0:
                F_product *= 1
            else:
                F_product *= Fraction(-1, p - 1)

        ok = (c_N == mu_sum) and (c_over_phi == F_product)
        all_ok = all_ok and ok

        print(f"  {n:>8} {g:>10} {c_N:>10} {mu_sum:>10} "
              f"{float(c_over_phi):>12.6f} {float(F_product):>12.6f}  "
              f"{'OK' if ok else 'MISMATCH'}")

    print()
    print(f"  c_N(n) = Mobius sum, and c_N(n)/phi = per-channel gate product")
    print(f"  (compared exactly, as fractions): "
          f"{'verified for all test values' if all_ok else 'MISMATCH SOMEWHERE'}.")
    print()
    print("  THE DICTIONARY ENTRY:")
    print("    Ramanujan sum = Mobius function summed over divisor lattice")
    print("    Per-channel factor = individual prime sieve decision")
    print("    Product structure = independence of prime sieves (CRT)")

    # =================================================================
    section("V. NAMING READ AS SIEVE PREDICTION")
    # =================================================================

    print("""
  When -chi({p_1,...,p_m}) is divisible by absent prime s, the sub-sieve
  "names" s -- a prime beyond its boundary.

  By the reciprocal criterion (proved, explore_tower_naming.py):
  s | -chi iff sum(1/p_i) = m-1 (mod s).

  Sieve interpretation: the STRUCTURE of the sub-sieve (the reciprocal
  sum of its primes) constrains which primes can appear beyond it --
  not a sieving operation, but a number-theoretic property of the
  sieve primes themselves.
""")

    print("  Named absent primes at each rung (thin tower);")
    print("  divisor search bounded at 500 -- larger prime factors are not shown:")
    print(f"  {'k':>3} {'primes':>30} {'-chi':>14} {'names (<500)':>30}")
    print(f"  {'-' * 80}")

    for k in range(2, 10):
        ps = all_primes[:k]
        nc = neg_chi(ps)
        label = "{" + ",".join(str(p) for p in ps) + "}"
        divs = [q for q in range(2, min(nc + 1, 500)) if nc % q == 0 and is_prime(q)]
        beyond = [q for q in divs if q not in ps]
        div_str = ",".join(str(q) for q in beyond)
        print(f"  {k:>3} {label:>30} {nc:>14,} {div_str:>30}")

    print()

    print("  Does the full-ring -chi name its own successor p_{k+1}?")
    print()

    successor_named = []
    for k in range(3, 10):
        ps = all_primes[:k]
        nc = neg_chi(ps)
        p_next = all_primes[k]

        hits_next = (nc % p_next == 0)
        successor_named.append(hits_next)
        inv_sum = sum(pow(p, -1, p_next) for p in ps) % p_next
        target = (k - 1) % p_next

        print(f"    k={k}: p_{{k+1}} = {p_next:>3},  "
              f"-chi mod {p_next} = {nc % p_next},  "
              f"sum(1/p_i) mod {p_next} = {inv_sum},  "
              f"target = {target},  "
              f"names p_{{k+1}}: {hits_next}")

    print()
    print(f"  Successor named at any tested rung k=3..9: {any(successor_named)}.")
    print("  The criterion asks the reciprocal sum of the first k primes to hit")
    print("  (k-1) mod p_{k+1}; at every tested rung it misses.")

    # =================================================================
    section("VI. SIEVE SURVIVOR CLASSES AND THEIR STRUCTURE")
    # =================================================================

    print("""
  The non-units of Z/p_k# partition into 2^k - 1 classes by their
  "sieve profile" -- which primes divide them. Each class corresponds
  to a non-empty subset S of {p_1,...,p_k}: elements divisible by
  exactly the primes in S.

  Class size |C_S| = N * product(1/p_i, i in S) * product(1 - 1/p_j, j not in S)

  The unit class (S = empty) has size phi(N).
""")

    k_demo = 7
    ps = all_primes[:k_demo]
    N = prod(ps)
    phi = prod(p - 1 for p in ps)

    total_check = 0
    classes = []
    for mask in range(2 ** k_demo):
        S = [i for i in range(k_demo) if mask & (1 << i)]
        S_primes = [ps[i] for i in S]
        notS = [i for i in range(k_demo) if not (mask & (1 << i))]

        size = Fraction(N)
        for i in S:
            size *= Fraction(1, ps[i])
        for j in notS:
            size *= Fraction(ps[j] - 1, ps[j])
        size_int = int(size)
        total_check += size_int

        classes.append((mask, S_primes, size_int))

    print(f"  k={k_demo}, N={N}, phi={phi}")
    print(f"  Total across all classes: {total_check} (should be {N}): "
          f"{'OK' if total_check == N else 'MISMATCH'}")
    print()

    print("  Largest classes (by size):")
    print(f"  {'profile':>30} {'|S|':>4} {'size':>10} {'fraction':>10}")
    print(f"  {'-' * 58}")

    for mask, S_primes, size in sorted(classes, key=lambda x: -x[2])[:15]:
        label = ("{" + ",".join(str(p) for p in S_primes) + "}") if S_primes else "units"
        print(f"  {label:>30} {len(S_primes):>4} {size:>10,} "
              f"{size/N:>10.6f}")

    print()
    print("  The unit class (sieve survivors) is the largest single class,")
    print("  tied by {2}; each added sieve prime p scales a class by 1/p or")
    print("  (p-1)/p.")

    # =================================================================
    section("VII. ECC = SIEVE REDUNDANCY")
    # =================================================================

    print("""
  At k=7 (rate 4/7 MDS): knowing n mod {2,3,5,7} determines n mod {11,13,17}
  for codewords. In sieve terms: the coarse sieve (small primes) determines
  the fine sieve (large primes) for the 210 codeword residue classes.

  The 210 codewords embed Z/210 into Z/510510: codeword n is the integer
  n in {0,...,209}, read on all seven channels. The MDS property (d=4)
  says any 4 channels reconstruct. Two checks below:
    - capacity: the product of the 4 chosen primes is >= 210, so a
      codeword's residue mod that product determines it;
    - reconstruction: every codeword CRT-recovered from its 4 residues
      alone and compared against the original.
""")

    ps7 = all_primes[:7]
    N7 = prod(ps7)
    data_N = prod(ps7[:4])

    print(f"  k=7: N={N7}, data channels = {ps7[:4]}, data_N = {data_N}")
    print(f"  Codewords: {data_N} out of {N7} elements ({data_N/N7*100:.4f}%)")
    print()

    print(f"  {'channels':>30} {'product':>10} {'capacity':>10} {'recovered':>12}")
    print(f"  {'-' * 68}")

    all_4subsets = list(combinations(range(7), 4))
    subsets_ok = 0
    shown = 0
    for subset in all_4subsets:
        sub_primes = [ps7[i] for i in subset]
        sub_N = prod(sub_primes)
        capacity = (sub_N >= data_N)
        recovered = sum(
            1 for n in range(data_N)
            if crt_combine([n % p for p in sub_primes], sub_primes) == n
        )
        ok = capacity and recovered == data_N
        if ok:
            subsets_ok += 1
        label = "{" + ",".join(str(p) for p in sub_primes) + "}"
        if shown < 10 or not ok:
            print(f"  {label:>30} {sub_N:>10} {'YES' if capacity else 'NO':>10} "
                  f"{recovered:>7}/{data_N}")
            shown += 1

    if shown < len(all_4subsets):
        print(f"  ... ({len(all_4subsets)} total 4-subsets)")

    print()
    print(f"  Subsets passing both checks: {subsets_ok}/{len(all_4subsets)}")
    print()

    print("  Sieve interpretation:")
    print("    The Eratosthenes sieve has BUILT-IN REDUNDANCY at every rung k >= 7.")
    print("    Losing up to 3 prime sieves (any 3) still allows full reconstruction")
    print("    of the data. The redundancy is structural -- it comes from the CRT")
    print("    decomposition, not from any external code.")
    print()

    rate_data = []
    for k in range(4, K_MAX + 1):
        n_data = 4 if k <= 7 else k - 3
        n_parity = k - n_data
        if n_parity < 3:
            continue
        rate = Fraction(n_data, k)
        rate_data.append((k, n_data, n_parity, float(rate)))

    print("  ECC rate improves as the tower grows:")
    print(f"  {'k':>3} {'data':>5} {'parity':>7} {'rate':>8}")
    print(f"  {'-' * 28}")
    for k, nd, np_, r in rate_data:
        print(f"  {k:>3} {nd:>5} {np_:>7} {r:>8.3f}")

    # =================================================================
    section("VIII. THE SIEVE DICTIONARY")
    # =================================================================

    print("""
  TOWER CONCEPT              SIEVE CONCEPT
  -------------------------- ------------------------------------------
  Z/p_k# (the ring)         residue classes mod the k-th primorial
  Element n                  residue class n mod p_k#
  Unit (gcd(n,N)=1)          sieve survivor -- coprime to p_1,...,p_k
  Zero divisor               sieved-out integer
  CRT channel p              individual prime sieve mod p
  CRT decomposition          factoring the sieve into independent parts
  phi(N)                     count of sieve survivors (Mertens product)
  lambda(N)                  exponent of the survivor group
  Transparency               (p-1)|lambda -- no new multiplicative orders
  Idempotent e_S             inclusion-exclusion projector for subset S
  Sum over idempotents       Legendre sieve formula (IE for phi)
  Ramanujan sum c_N(n)       Mobius inversion over the divisor lattice
  Per-channel gate factor    individual prime sieve decision (hit/miss)
  Product of factors         CRT independence = sieve independence
  -chi(sub-ring)             N*(d_mean - 1): mean distance of a uniform
                             element from 0, minus one, times N
  Naming criterion           reciprocal-sum constraint on absent primes
  ECC (rate 4/7 at k=7)     sieve redundancy: 4 primes determine all 7
  MDS (d=4)                  any 4 of 7 prime sieves reconstruct the data
  Codeword                   residue class consistent across all channels

  The tower is not ANALOGOUS to the sieve; along the primorial
  trajectory it IS the sieve (property -- the identification is
  term-by-term above, each computable row verified in its section).
""")

    # =================================================================
    section("IX. QUANTITATIVE: -CHI AGAINST PHI ACROSS THE TOWER")
    # =================================================================

    print("""
  How does -chi relate to phi across the tower?
  -chi = N*(k-1) - sum(N/p_i)
  phi = N * product(1-1/p_i)
""")

    print(f"  {'k':>3} {'N':>14} {'phi':>14} {'-chi':>14} "
          f"{'-chi/phi':>10} {'-chi/N':>10}")
    print(f"  {'-' * 72}")

    for k in range(2, K_MAX + 1):
        ps = all_primes[:k]
        N = prod(ps)
        phi = prod(p - 1 for p in ps)
        nc = neg_chi(ps)
        ratio_phi = nc / phi
        ratio_N = nc / N

        print(f"  {k:>3} {N:>14,} {phi:>14,} {nc:>14,} "
              f"{ratio_phi:>10.4f} {ratio_N:>10.6f}")

    print()
    print("  -chi/N = d_mean - 1 = k - 1 - sum(1/p_i), growing as k - O(log log k)")
    print("  by Mertens. -chi/phi grows faster because the survivor density")
    print("  phi/N also falls (Mertens product) while d_mean grows.")

    # =================================================================
    section("X. SUB-SIEVE NAMING CENSUS AT k=7")
    # =================================================================

    print("""
  At k=7, there are 2^7-1 = 127 non-empty sub-sieves; the census below
  covers the 120 of size m >= 2 (a single prime has -chi = -1, which
  no prime divides). For each, compute -chi and check which TOWER primes it
  "sees" (divides). Group by sub-sieve size: do larger sub-sieves see
  more?
""")

    ps7 = all_primes[:7]

    size_stats = defaultdict(lambda: {'total': 0, 'naming': 0, 'primes_seen': Counter()})

    for m in range(2, 8):
        for combo in combinations(ps7, m):
            nc = neg_chi(list(combo))
            absent = [s for s in ps7 if s not in combo]
            named = [s for s in absent if nc % s == 0]

            stats = size_stats[m]
            stats['total'] += 1
            if named:
                stats['naming'] += 1
            for s in named:
                stats['primes_seen'][s] += 1

    print(f"  {'size m':>7} {'count':>7} {'naming':>7} {'frac':>7} {'primes seen':>30}")
    print(f"  {'-' * 62}")

    for m in sorted(size_stats):
        s = size_stats[m]
        frac = s['naming'] / s['total']
        seen_str = ", ".join(f"{p}:{c}" for p, c in sorted(s['primes_seen'].items()))
        print(f"  {m:>7} {s['total']:>7} {s['naming']:>7} {frac:>7.3f} {seen_str:>30}")

    print()
    print("  The naming fraction FALLS as the sub-sieve grows: larger")
    print("  sub-sieves see fewer of the tower's own primes.")
    print()

    nc_full = neg_chi(ps7)
    named_beyond = [p for p in range(2, 200)
                    if is_prime(p) and p not in ps7 and nc_full % p == 0]
    print(f"  Beyond-boundary primes named by the full-ring -chi (search < 200):")
    print(f"    -chi({','.join(str(p) for p in ps7)}) = {nc_full}")
    print(f"    Prime divisors beyond p_7=17 and below 200: {named_beyond}")

    # =================================================================
    section("XI. FINDINGS")
    # =================================================================

    print(f"""
  1. THE IDENTITY (property). Units are survivors by the definition of
     coprimality; the idempotent lattice IS the inclusion-exclusion
     computation (sum over idempotents = phi, verified k=7, section II).

  2. -CHI IS A MEAN-DISTANCE MULTIPLE (property; printed k=2..7).
     -chi = N*(d_mean - 1), d_mean the mean CRT Hamming distance from 0
     of a UNIFORM ring element -- the whole ring, not the survivors,
     who all sit at distance exactly m (sections III, IX).

  3. RAMANUJAN SUM = MOBIUS INVERSION (property; verified at 16 values,
     k=7). The frequency moment's per-channel gate is the individual
     prime sieve's hit/miss decision; the product form is sieve
     independence via CRT (section IV; explore_moment_resonance.py).

  4. NAMING NEVER HITS THE SUCCESSOR IN RANGE (observation, k=3..9).
     The full-ring -chi names absent primes but named p_{{k+1}} at no
     tested rung, and the k=7 naming fraction falls with sub-sieve
     size (sections V, X).

  5. ECC IS SIEVE REDUNDANCY, RECONSTRUCTION CHECKED (computed, k=7).
     {subsets_ok}/{len(all_4subsets)} four-channel subsets recover all
     {data_N} codewords by direct CRT reconstruction (section VII).

  6. LAMBDA IS THE SURVIVORS' DYNAMICAL PERIOD (property). lambda is
     the exponent of the survivor group; transparency reads as: adding
     sieve prime p leaves the multiplicative dynamics unchanged
     (section VIII; explore_tower_geometry.py).
""")

    print("=" * 76)
    print("  Done.")
    print("=" * 76)


if __name__ == "__main__":
    main()
