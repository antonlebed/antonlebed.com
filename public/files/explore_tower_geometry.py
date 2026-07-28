"""Torus geometry across the primorial tower k=3..14.

How does curvature, spectral gap, heat kernel, and mixing change as
you climb the tower? Does the geometry see lambda plateaus vs jumps?

Thread 4 (torus geometry) extended beyond k=7.
Cross-links: Thread 1 (lambda), Thread 3 (resonance).

Run: python prime/code/explore_tower_geometry.py
"""

from math import cos, sin, pi, sqrt, log, gcd, prod, comb, lcm
from fractions import Fraction
from itertools import combinations
from crt import (
    Ring, encode, decode, euler_characteristic,
    hamming_degree, spectral_gap, carmichael_lambda, factorize, is_prime,
)


def section(title):
    print(f"\n{'=' * 72}")
    print(f"  {title}")
    print(f"{'=' * 72}")


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
        e = f[p]
        parts.append(str(p) if e == 1 else f"{p}^{e}")
    return sign + " * ".join(parts)


# Build the tower: first k primes for k=3..14
def first_n_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

K_MAX = 14
ALL_PRIMES = first_n_primes(K_MAX)

# Build Ring objects for each rung
RUNGS = {}
for k in range(3, K_MAX + 1):
    ps = ALL_PRIMES[:k]
    RUNGS[k] = Ring(f"k={k}", ps, [1] * k)


# Precompute lambda for each rung (faster than from Ring, just lcm of (p-1))
def tower_lambda(k):
    result = 1
    for p in ALL_PRIMES[:k]:
        result = lcm(result, p - 1)
    return result


# ═══════════════════════════════════════════════════════════════════════
# I. THE TOWER TABLE
# ═══════════════════════════════════════════════════════════════════════

section("I. THE TOWER — GEOMETRIC QUANTITIES k=3..14")

print(f"\n  {'k':>3} {'p_k':>4} {'N':>14} {'lam':>8} {'trans?':>7} "
      f"{'deg':>5} {'H-gap':>6} {'C-gap':>10} {'kappa_OR':>10} {'chi':>15}")
print(f"  {'-'*90}")

rows = []
for k in range(3, K_MAX + 1):
    ring = RUNGS[k]
    ps = ALL_PRIMES[:k]
    p_new = ps[-1]
    lam = tower_lambda(k)
    lam_prev = tower_lambda(k - 1) if k > 3 else 1

    transparent = (lam == lam_prev) if k > 3 else False

    deg = hamming_degree(ring)
    h_gap = min(ps)  # Hamming spectral gap = smallest prime
    c_gap = 2 * sin(pi / max(ps))**2  # chord heat kernel gap (weight 1)

    # Ollivier-Ricci total curvature = sum((p-2)/deg)
    kappa_OR = Fraction(sum(p - 2 for p in ps), deg)

    chi = euler_characteristic(ring)

    rows.append(dict(
        k=k, p_new=p_new, N=ring.N, lam=lam, lam_prev=lam_prev,
        transparent=transparent, deg=deg, h_gap=h_gap, c_gap=c_gap,
        kappa_OR=kappa_OR, chi=chi, ring=ring, primes=ps,
    ))

    trans_mark = "YES" if transparent else ""
    print(f"  {k:>3} {p_new:>4} {ring.N:>14,} {lam:>8,} {trans_mark:>7} "
          f"{deg:>5} {h_gap:>6} {c_gap:>10.6f} {float(kappa_OR):>10.6f} {chi:>15,}")


# ═══════════════════════════════════════════════════════════════════════
# II. CURVATURE SCALING
# ═══════════════════════════════════════════════════════════════════════

section("II. OLLIVIER-RICCI CURVATURE ACROSS k")

print("""
  Ollivier-Ricci total = sum_{i=1}^{k} (p_i - 2) / degree.
  Since degree = sum(p_i - 1) = sum(p_i) - k, we get:
    kappa = [sum(p_i) - 2k] / [sum(p_i) - k]
          = 1 - k / [sum(p_i) - k]
          = 1 - k / degree

  As k grows, sum(p_i) ~ k^2 * ln(k) / 2 (PNT), so degree ~ k^2 ln(k) / 2.
  Thus kappa -> 1 - 2/(k*ln(k)) -> 1. The torus gets rounder.
""")

print(f"  {'k':>3} {'sum(p_i-2)':>12} {'degree':>8} {'kappa':>12} {'1-k/deg':>12} {'kappa_D':>10}")
print(f"  {'-'*62}")
for r in rows:
    k = r['k']
    ps = r['primes']
    deg = r['deg']
    kappa = r['kappa_OR']
    kappa_D = Fraction(0, 1)  # D channel: (2-2)/deg = 0 always
    print(f"  {k:>3} {sum(p-2 for p in ps):>12} {deg:>8} {float(kappa):>12.6f} "
          f"{1 - k/deg:>12.6f} {float(kappa_D):>10.6f}")


# Per-channel curvature for new prime at each rung
print(f"\n  Curvature contributed by the NEW prime at each rung:")
print(f"  {'k':>3} {'p_new':>6} {'kappa_new':>14} {'fraction of total':>20}")
print(f"  {'-'*50}")
for r in rows:
    k = r['k']
    p_new = r['p_new']
    deg = r['deg']
    kappa_new = Fraction(p_new - 2, deg)
    kappa_total = r['kappa_OR']
    frac_of_total = float(kappa_new) / float(kappa_total) if float(kappa_total) > 0 else 0
    trans = " (transparent)" if r['transparent'] else ""
    print(f"  {k:>3} {p_new:>6} {float(kappa_new):>14.6f} {frac_of_total:>19.1%}{trans}")


# ═══════════════════════════════════════════════════════════════════════
# III. LAMBDA JUMPS vs PLATEAUS — GEOMETRIC SIGNATURE
# ═══════════════════════════════════════════════════════════════════════

section("III. GEOMETRY AT LAMBDA JUMPS vs PLATEAUS")

print("""
  When a new prime is transparent (doesn't change lambda), the tower
  gains "capacity" but not "complexity." Does the geometry see this?

  Lambda jump: lam(k) > lam(k-1). The new prime adds a new order level.
  Plateau:     lam(k) = lam(k-1). The new prime is structurally absorbed.
""")

# Compute delta-quantities at each step
print(f"  {'k':>3} {'p_k':>4} {'type':>8} {'lam_ratio':>10} {'d(deg)':>7} "
      f"{'d(kappa)':>10} {'d(C-gap)':>10} {'d(chi)/chi':>12}")
print(f"  {'-'*72}")

for i, r in enumerate(rows):
    if i == 0:
        continue
    prev = rows[i - 1]
    step_type = "plateau" if r['transparent'] else "JUMP"
    lam_ratio = r['lam'] / prev['lam'] if prev['lam'] > 0 else 0
    d_deg = r['deg'] - prev['deg']
    d_kappa = float(r['kappa_OR']) - float(prev['kappa_OR'])
    d_c_gap = r['c_gap'] - prev['c_gap']
    d_chi_frac = (r['chi'] - prev['chi']) / abs(prev['chi']) if prev['chi'] != 0 else 0

    print(f"  {r['k']:>3} {r['p_new']:>4} {step_type:>8} {lam_ratio:>10.1f}x "
          f"{d_deg:>7} {d_kappa:>+10.6f} {d_c_gap:>+10.6f} {d_chi_frac:>+12.4f}")


# ═══════════════════════════════════════════════════════════════════════
# IV. HEAT KERNEL SCALING
# ═══════════════════════════════════════════════════════════════════════

section("IV. HEAT KERNEL ACROSS THE TOWER")

print(f"""
  Two heat kernels:
  A. Hamming: gap = min(p_i)/degree. Half-life = ln(2)*degree/min(p_i).
  B. Chord:   gap = 2*sin^2(pi/p_k).  Half-life = ln(2)/gap.

  As k grows, p_k grows, so the chord gap SHRINKS (larger circles = slower
  decay). The Hamming gap shrinks too (degree grows, min stays at 2).
""")

print(f"  {'k':>3} {'Ham gap':>12} {'Ham t_1/2':>10} {'Chord gap':>12} {'Chord t_1/2':>12} "
      f"{'Mix ratio':>10}")
print(f"  {'-'*65}")

for r in rows:
    k = r['k']
    deg = r['deg']
    h_gap_frac = Fraction(r['h_gap'], deg)
    ham_half = log(2) / float(h_gap_frac)
    chord_half = log(2) / r['c_gap']
    mix_ratio = r['ring'].N / (deg / r['h_gap'])  # cyclic vs CRT mixing

    print(f"  {k:>3} {float(h_gap_frac):>12.6f} {ham_half:>10.2f} "
          f"{r['c_gap']:>12.6f} {chord_half:>12.2f} {mix_ratio:>10.0f}x")


# ═══════════════════════════════════════════════════════════════════════
# V. EULER CHARACTERISTIC — THE DEEP PATTERN
# ═══════════════════════════════════════════════════════════════════════

section("V. EULER CHARACTERISTIC ACROSS THE TOWER")

print("""
  chi(k) = N * (1 - k + sum(1/p_i)).
  -chi(k) = N * (k - 1 - sum(1/p_i)).

  As k grows, (k - 1 - sum(1/p_i)) grows roughly as k (since sum(1/p)
  diverges only as log(log(k))). And N grows super-exponentially.
  So -chi grows VERY fast.
""")

print(f"  {'k':>3} {'-chi':>18} {'log10(-chi)':>12} {'-chi/N':>12} "
      f"{'k-1-sum(1/p)':>14} {'intruders'}")
print(f"  {'-'*75}")

for r in rows:
    k = r['k']
    neg_chi = -r['chi']
    ratio = neg_chi / r['ring'].N
    sum_inv = sum(Fraction(1, p) for p in r['primes'])
    k_minus = float(Fraction(k - 1) - sum_inv)
    log10_chi = log(abs(neg_chi)) / log(10) if neg_chi != 0 else 0

    # Factor -chi and find intruder primes
    f = factorize(abs(neg_chi))
    prime_set = set(r['primes'])
    intruders = sorted([p for p in f if p not in prime_set])
    intr_str = ",".join(str(p) for p in intruders) if intruders else "smooth"

    print(f"  {k:>3} {neg_chi:>18,} {log10_chi:>12.1f} {float(ratio):>12.4f} "
          f"{k_minus:>14.6f} {intr_str}")


# ═══════════════════════════════════════════════════════════════════════
# VI. D-INVISIBILITY ACROSS THE TOWER
# ═══════════════════════════════════════════════════════════════════════

section("VI. D-INVISIBILITY — DOES IT HOLD AT EVERY RUNG?")

print("""
  At k=7, all odd-prime sub-rings have odd -chi, so 2 never divides -chi.
  Does this hold at every k? The proof was: product of odd primes is odd,
  so N*(k-1) - sum(N/p_i) is odd. This argument is k-independent.
""")

for r in rows:
    k = r['k']
    ps = r['primes']
    odd_ps = [p for p in ps if p > 2]

    all_odd = True
    count = 0
    for size in range(1, len(odd_ps) + 1):
        for subset in combinations(odd_ps, size):
            N_sub = prod(subset)
            neg_chi_sub = N_sub * (size - 1) - sum(N_sub // p for p in subset)
            if neg_chi_sub % 2 == 0 and neg_chi_sub != 0:
                all_odd = False
            count += 1

    print(f"  k={k:>2}: {count:>5} odd-prime sub-rings. All -chi odd: "
          f"{'YES' if all_odd else 'NO — VIOLATION!'}")

print(f"\n  D-invisibility holds at every rung tested. The proof is algebraic:")
print(f"  for odd primes {{p_i}}, N=prod(p_i) is odd, each N/p_j is odd,")
print(f"  so -chi = N*(s-1) - sum(N/p_j) has parity (s-1) - s = -1 mod 2 = odd.")


# ═══════════════════════════════════════════════════════════════════════
# VII. SHELL POLYNOMIAL EVOLUTION
# ═══════════════════════════════════════════════════════════════════════

section("VII. SHELL POLYNOMIAL — HOW DISTANCE DISTRIBUTION CHANGES WITH k")

print("""
  E_k(x) = prod_{i=1}^{k} (1 + (p_i - 1)*x).
  Coefficient of x^d = number of elements at Hamming distance d.
  e_1 = degree. e_k = phi(N). The shape changes with k.
""")

print(f"  Concentration: what fraction of elements are at distance >= k/2?")
print(f"  {'k':>3} {'N':>14} {'frac d>=k/2':>14} {'median d':>10} {'mean d':>10}")
print(f"  {'-'*55}")

for r in rows:
    k = r['k']
    ps = r['primes']
    # Compute shell polynomial
    coeffs = [1]
    for p in ps:
        new_coeffs = [0] * (len(coeffs) + 1)
        for j, c in enumerate(coeffs):
            new_coeffs[j] += c
            new_coeffs[j + 1] += c * (p - 1)
        coeffs = new_coeffs

    N = r['ring'].N
    # Fraction at distance >= k/2
    half = k / 2
    far = sum(coeffs[d] for d in range(len(coeffs)) if d >= half)
    frac_far = far / N

    # Mean distance
    mean_d = sum(d * coeffs[d] for d in range(len(coeffs))) / N

    # Median distance (smallest d where cumul >= 0.5)
    cumul = 0
    median_d = 0
    for d in range(len(coeffs)):
        cumul += coeffs[d]
        if cumul >= N / 2:
            median_d = d
            break

    print(f"  {k:>3} {N:>14,} {frac_far:>14.4f} {median_d:>10} {mean_d:>10.2f}")


# ═══════════════════════════════════════════════════════════════════════
# VIII. FORMAN-RICCI ACROSS THE TOWER
# ═══════════════════════════════════════════════════════════════════════

section("VIII. FORMAN-RICCI CURVATURE SCALING")

print("""
  F_i = 3*p_i - (2*degree + 2).  Sum F = 3*sum(p_i) - k*(2*deg + 2).
  All F_i negative when degree >> max(p_i).
  At what k does the first non-negative F_i appear?
""")

print(f"  {'k':>3} {'F(p_k)':>8} {'F(2)':>8} {'max F':>8} {'sum F':>10}")
print(f"  {'-'*42}")

for r in rows:
    k = r['k']
    ps = r['primes']
    deg = r['deg']
    F_vals = [3 * p - (2 * deg + 2) for p in ps]
    F_new = F_vals[-1]
    F_D = F_vals[0]
    print(f"  {k:>3} {F_new:>8} {F_D:>8} {max(F_vals):>8} {sum(F_vals):>10}")

print(f"\n  All Forman curvatures remain negative through k=14.")
print(f"  The Hamming graph is always 'thin' compared to its degree at")
print(f"  these scales. F converges toward -2*degree per channel.")


# ═══════════════════════════════════════════════════════════════════════
# IX. TRANSPARENCY AND GEOMETRIC COST
# ═══════════════════════════════════════════════════════════════════════

section("IX. GEOMETRIC COST OF ADDING A PRIME — JUMP vs PLATEAU")

print("""
  Every new prime p adds the same geometric cost:
    +1 dimension, +(p-1) degree, new curvature (p-2)/degree.

  But a JUMP also changes lambda (the global period), while a PLATEAU
  does not. Question: does the geometry differentiate these?

  The answer: the geometry DOES NOT distinguish them intrinsically.
  Curvature, degree, spectral gap, shell polynomial all depend only
  on the set {p_1,...,p_k}, not on lambda.

  Lambda is an ORDER-THEORETIC quantity (lcm of p_i - 1). The geometry
  is a DISTANCE-THEORETIC quantity (depends on p_i directly).

  BUT: lambda controls DYNAMICS (power map orbits). A transparent prime
  adds a new spatial dimension WITHOUT adding new dynamical complexity.
  The torus gets bigger but its orbits don't get longer.
""")

# Compute: dimension / dynamical complexity ratio
print(f"  {'k':>3} {'p_k':>4} {'type':>8} {'dim':>4} {'log(lam)':>10} "
      f"{'dim/log(lam)':>14} {'log(phi)':>10} {'log(lam)/log(phi)':>18}")
print(f"  {'-'*80}")

for r in rows:
    k = r['k']
    lam = r['lam']
    phi = r['ring'].phi
    step = "plateau" if r['transparent'] else "JUMP"
    log_lam = log(lam)
    log_phi = log(phi)
    ratio = k / log_lam
    lam_phi_ratio = log_lam / log_phi

    print(f"  {k:>3} {r['p_new']:>4} {step:>8} {k:>4} {log_lam:>10.3f} "
          f"{ratio:>14.4f} {log_phi:>10.3f} {lam_phi_ratio:>18.4f}")


# ═══════════════════════════════════════════════════════════════════════
# X. BETTI NUMBERS AND IDEMPOTENT GROWTH
# ═══════════════════════════════════════════════════════════════════════

section("X. BETTI NUMBERS C(k,d) — SYMMETRY AND GROWTH")

print(f"  The Betti numbers of T^k are C(k,d) for d=0..k.")
print(f"  Total = 2^k = number of idempotents.\n")

# Show the Betti number triangle
max_d = K_MAX
header = f"  {'k':>3} |"
for d in range(max_d + 1):
    header += f" {d:>6}"
header += f" | {'sum':>8}"
print(header)
print(f"  {'-' * (len(header) - 2)}")

for k in range(3, K_MAX + 1):
    row = f"  {k:>3} |"
    for d in range(max_d + 1):
        if d <= k:
            row += f" {comb(k, d):>6}"
        else:
            row += f" {'':>6}"
    row += f" | {2**k:>8}"
    print(row)

# Poincare duality: beta_d = beta_{k-d}
print(f"\n  Poincare duality: C(k,d) = C(k,k-d) at every k.")
print(f"  The 490 split (k=7, d=3 vs d=4, both = 35) is the middle.")
print(f"  At k=14: middle split is C(14,7) = {comb(14,7):,} (= beta_7).")


# ═══════════════════════════════════════════════════════════════════════
# XI. CROSS-THREAD: DOES GEOMETRY EXPLAIN NAMING?
# ═══════════════════════════════════════════════════════════════════════

section("XI. CROSS-THREAD — EULER CHARACTERISTIC AND NAMING")

print("""
  The seed-flower's naming property: a sub-ring names s if s | -chi.
  -chi = N*(k-1) - sum(N/p_i) for sub-ring with primes {p_i}.

  -chi is a topological quantity (Euler characteristic of the sub-torus).
  The naming property says: which primes divide this topological invariant?

  At each rung, we can ask: what fraction of -chi values are prime?
  What fraction are tower-smooth (all prime factors in the tower set)?
""")

for k in [4, 5, 6, 7, 8]:
    ps = ALL_PRIMES[:k]
    prime_set = set(ps)
    total = 0
    chi_prime = 0
    chi_smooth = 0
    chi_vals = []

    for size in range(2, k + 1):
        for subset in combinations(ps, size):
            N_sub = prod(subset)
            neg_chi = N_sub * (size - 1) - sum(N_sub // p for p in subset)
            if neg_chi == 0:
                continue
            total += 1
            abs_chi = abs(neg_chi)
            chi_vals.append(abs_chi)
            if is_prime(abs_chi):
                chi_prime += 1
            f = factorize(abs_chi)
            if all(p in prime_set for p in f):
                chi_smooth += 1

    print(f"  k={k}: {total} sub-rings with -chi != 0. "
          f"-chi prime: {chi_prime}/{total} ({chi_prime/total:.0%}). "
          f"Tower-smooth: {chi_smooth}/{total} ({chi_smooth/total:.0%}).")


# ═══════════════════════════════════════════════════════════════════════
# XII. KEY FINDINGS
# ═══════════════════════════════════════════════════════════════════════

section("XII. KEY FINDINGS")

print("""
1. CURVATURE APPROACHES 1. Ollivier-Ricci total kappa = 1 - k/degree.
   Since degree ~ k^2*ln(k)/2, kappa -> 1. The torus gets uniformly
   rounder as you climb. No plateau/jump distinction in curvature.

2. HEAT KERNEL: HAMMING SLOWS, CHORD SLOWS. Both half-lives grow with k.
   Hamming half-life ~ degree/2 * ln(2) (controlled by Z/2 bottleneck).
   Chord half-life = ln(2)/(2*sin^2(pi/p_k)) (controlled by largest prime).
   The tower diffuses slower as it grows — more dimensions, longer to mix.

3. GEOMETRY DOES NOT SEE LAMBDA. Curvature, degree, gaps, shells all
   depend on {p_1,...,p_k} directly, not on lcm(p_i - 1) = lambda.
   A transparent prime and a non-transparent prime of the same size
   contribute identical geometry. Lambda is dynamical, not metric.

4. D-INVISIBILITY HOLDS AT EVERY RUNG (k=3..14, verified). The proof
   is algebraic and k-independent: odd-prime sub-rings always have
   odd -chi, so 2 never divides -chi.

5. SHELL CONCENTRATION. The shell polynomial concentrates: mean distance
   grows with k, but median stays at or below k/2. Most elements are at
   "moderate" distance — the torus is well-connected.

6. LAMBDA-PHI RATIO. log(lambda)/log(phi) trends toward ~0.3. This is
   the "dynamical dimension" of the tower — lambda uses ~30% of the
   available complexity (measured by phi). Stable across jumps and plateaus.

7. EULER CHARACTERISTIC PRIMALITY. -chi is prime for 82% (k=4) down
   to 45% (k=8) of size>=2 sub-rings, decaying toward zero as the
   tower climbs (census + conditioned heuristic to k=128:
   explore_chi_primality.py). Tower-smooth fraction also decreases
   with k (intruder primes become more common).

8. THE GEOMETRY/DYNAMICS SPLIT. The tower has two independent aspects:
   - GEOMETRY: depends on {p_1,...,p_k}. Every new prime has equal cost.
   - DYNAMICS: depends on {p_1-1,...,p_k-1}. Transparent primes are free.
   The torus gets bigger at every step; orbits get longer only at jumps.
   This is the tower's two-speed growth: capacity (every step) vs
   complexity (jumps only).
""")

print("=" * 72)
print("  Done. Tower geometry mapped k=3..14.")
print("=" * 72)
