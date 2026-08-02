"""Torus geometry of rung 7, Z/510510 — the squarefree 7-channel ring.

CRT makes RAD a discrete torus T^7 = S^1(2) x S^1(3) x S^1(5) x S^1(7)
x S^1(11) x S^1(13) x S^1(17). Every channel is a field. Addition rotates
each circle independently. Sigma = (1,1,...,1) winds the diagonal.

This script maps the full geometry: metrics, curvature, heat kernel,
distance distribution, spectral structure, and 2-invisibility
in topological form.

Run: python prime/code/explore_torus_geometry.py
"""

from math import cos, sin, pi, sqrt, log, gcd, prod, comb
from fractions import Fraction
from collections import Counter
from itertools import combinations, product as iterproduct
from crt import (
    Ring, RAD_RING, primorial_ring, powered_ring,
    encode, decode, eigenvalue, eigenvalue_of, spectral_gap,
    chord_distance_sq, euler_phi, carmichael_lambda, factorize,
    hamming_degree, hamming_distance, euler_characteristic,
    is_prime,
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


PRIMES = list(RAD_RING.primes)  # [2, 3, 5, 7, 11, 13, 17]
K_RAD = RAD_RING.k  # 7

# The prime-power variant of the same rung: the first four channels raised
# to (3, 2, 2, 2), so they are rings rather than fields. Every comparison
# below is squarefree rung 7 against this.
POWERED_7 = powered_ring(7)


# ═══════════════════════════════════════════════════════════════════════
# I. THE RAD TORUS
# ═══════════════════════════════════════════════════════════════════════

section("I. THE RAD TORUS T^7")

print(f"""
RAD = Z/510510 decomposes as:
  T^7 = Z/2 x Z/3 x Z/5 x Z/7 x Z/11 x Z/13 x Z/17

Every channel is a prime field GF(p). Every element is a point on the
7-torus. Addition = rotation. Sigma = (1,1,1,1,1,1,1) winds the diagonal.

Ring parameters:
  N     = {RAD_RING.N:,}
  k     = {K_RAD}
  phi   = {RAD_RING.phi:,}
  lam   = {RAD_RING.lam}
  |Idem|= {RAD_RING.num_idempotents}
""")

# Dimension of the ambient real torus (before discrete sampling)
# Real T^7 has dimension 7. Our discrete torus samples it at
# 2*3*5*7*11*13*17 = 510510 points.
print(f"  Continuous dimension: 7")
print(f"  Discrete points: {RAD_RING.N:,}")
print(f"  Points per dimension: {RAD_RING.N**(1/7):.2f} (geometric mean)")

# Per-circle sizes
print(f"\n  Per-circle sizes (points on each S^1):")
for i, p in enumerate(PRIMES):
    frac = Fraction(1, p)
    print(f"    S^1({p:>2}): {p:>2} points, arc = 2*pi/{p} = {2*pi/p:.4f} rad,"
          f" fraction = 1/{p}")


# ═══════════════════════════════════════════════════════════════════════
# II. THREE METRICS
# ═══════════════════════════════════════════════════════════════════════

section("II. THREE METRICS ON T^7")

# A. Hamming metric
deg_rad = hamming_degree(RAD_RING)
deg_pw = hamming_degree(POWERED_7)
print(f"\n  A. HAMMING METRIC (CRT Hamming graph H = K_2 [] K_3 [] ... [] K_17)")
print(f"     Degree (neighbors) = sum(p_i - 1) = {deg_rad} = {factor_str(deg_rad)}")
print(f"     Diameter = k = {K_RAD}")
print(f"     Compare powered rung 7: degree = {deg_pw} = {factor_str(deg_pw)}")

# B. CRT L1 metric (circular arc distance per channel, summed)
print(f"\n  B. CRT L1 METRIC (sum of circular arc distances)")
print(f"     d_L1(a,b) = sum_i min(|r_i - s_i|, p_i - |r_i - s_i|)")
print(f"     Max distance = sum(floor(p_i/2)) = ", end="")
max_l1 = sum(p // 2 for p in PRIMES)
print(f"{max_l1} = {factor_str(max_l1)}")

# C. Cayley (cyclic) metric
print(f"\n  C. CAYLEY METRIC (cyclic distance mod N)")
print(f"     d_Cayley(a,b) = min(|a-b|, N-|a-b|) mod N")
print(f"     Max distance = N/2 = {RAD_RING.N // 2}")

# Spectral gaps for each metric
gap_chord_rad = 4 * sin(pi / max(PRIMES))**2  # chord distance, w=2
gap_chord_pw = 4 * sin(pi / max(POWERED_7.moduli))**2
gap_hamming_rad = min(PRIMES)  # Hamming gap = smallest modulus
gap_hamming_pw = min(POWERED_7.moduli)

print(f"\n  SPECTRAL GAPS:")
print(f"  {'Metric':<20} {'k=7':>12} {'k=7 powered':>14} {'Ratio':>8}")
print(f"  {'-'*55}")
print(f"  {'Hamming':<20} {gap_hamming_rad:>12} {gap_hamming_pw:>12} "
      f"{gap_hamming_rad/gap_hamming_pw:>8.2f}")
print(f"  {'Chord':<20} {gap_chord_rad:>12.6f} {gap_chord_pw:>12.6f} "
      f"{gap_chord_rad/gap_chord_pw:>8.1f}")

# Gap duality
print(f"""
  GAP DUALITY (squarefree):
    Hamming gap controlled by SMALLEST channel: Z/{min(PRIMES)}.
    Chord gap controlled by LARGEST channel: Z/{max(PRIMES)}.
    Two complementary views of the same torus.

  GAP DUALITY (powered):
    Hamming gap controlled by Z/{min(POWERED_7.moduli)} = Z/2^3.
    Chord gap controlled by Z/{max(POWERED_7.moduli)} = Z/7^2.
    Same duality, different channels.
""")


# ═══════════════════════════════════════════════════════════════════════
# III. OLLIVIER-RICCI CURVATURE
# ═══════════════════════════════════════════════════════════════════════

section("III. OLLIVIER-RICCI CURVATURE")

print("""
On the CRT Hamming graph, the Ollivier-Ricci curvature of an edge in
channel i is kappa_i = (q_i - 2) / degree. This measures how much
optimal transport contracts along that channel.
""")

print(f"  {'Channel':<12} {'q_i':>4} {'q_i-2':>6} {'kappa_i':>12} {'As fraction':>16}")
print(f"  {'-'*55}")

kappa_sum = Fraction(0)
for i, p in enumerate(PRIMES):
    k_frac = Fraction(p - 2, deg_rad)
    kappa_sum += k_frac
    print(f"  Z/{p:<4} {p:>4} {p-2:>6} {float(k_frac):>12.6f} {str(k_frac):>16}")

print(f"\n  Total curvature = sum(kappa_i) = {kappa_sum} = {float(kappa_sum):.6f}")
print(f"    = {kappa_sum.numerator}/{kappa_sum.denominator}")
num_f = factorize(kappa_sum.numerator)
den_f = factorize(kappa_sum.denominator)
print(f"    numerator   = {kappa_sum.numerator} = {factor_str(kappa_sum.numerator)}")
print(f"    denominator = {kappa_sum.denominator} = {factor_str(kappa_sum.denominator)}")

# Fat comparison
deg_pw7 = hamming_degree(POWERED_7)
print(f"\n  POWERED comparison (rung 7 powered, degree = {deg_pw7}):")
print(f"  {'Channel':<12} {'q_i':>4} {'q_i-2':>6} {'kappa_i':>12}")
print(f"  {'-'*40}")

kappa_pw_sum = Fraction(0)
for i, q in enumerate(POWERED_7.moduli):
    k_frac = Fraction(q - 2, deg_pw7)
    kappa_pw_sum += k_frac
    base = POWERED_7.primes[i]
    e = POWERED_7.exponents[i]
    label = f"{base}^{e}" if e > 1 else f"{base}"
    print(f"  Z/{q:<8} ({label:<4}) {q:>4} {q-2:>6} {float(k_frac):>12.6f}")

print(f"\n  Powered total curvature = {kappa_pw_sum} = {float(kappa_pw_sum):.6f}")

# Key observation
print(f"""
  KEY: the 2-channel is FLAT when squarefree (kappa = 0). 2 is the unique
  prime where Z/p has only 2 points, making it metrically trivial in the
  Hamming graph.

  The 17-channel is most curved: kappa = 15/51 = 5/17.
  The largest prime contributes the most curvature — opposite to
  the gap duality (where the largest prime controls the chord gap).

  Curvature numerators (p-2): {[p-2 for p in PRIMES]}
  Sum = {sum(p-2 for p in PRIMES)} = {factor_str(sum(p-2 for p in PRIMES))}
""")


# ═══════════════════════════════════════════════════════════════════════
# IV. GAUSS-BONNET AND EULER CHARACTERISTIC
# ═══════════════════════════════════════════════════════════════════════

section("IV. GAUSS-BONNET (EULER CHARACTERISTIC)")

chi_rad = euler_characteristic(RAD_RING)
chi_pw = euler_characteristic(POWERED_7)
chi_deep = euler_characteristic(powered_ring(5))

print(f"\n  chi = N * (1 - k + sum(1/q_i))")
print(f"  -chi = N * (k - 1 - sum(1/q_i))")

# Compute exact sum 1/p_i
frac_sum = sum(Fraction(1, p) for p in PRIMES)
chi_exact = RAD_RING.N * (1 - K_RAD + frac_sum)
print(f"\n  sum(1/p_i) = {frac_sum} = {float(frac_sum):.6f}")
print(f"  1 - 7 + {frac_sum} = {1 - K_RAD + frac_sum}")

rings_for_chi = [
    (primorial_ring(4), "k=4 (Z/210)"),
    (primorial_ring(5), "k=5 (Z/2310)"),
    (primorial_ring(6), "k=6 (Z/30030)"),
    (RAD_RING, "k=7 (Z/510510)"),
    (powered_ring(5), "k=5 powered (Z/970200)"),
    (powered_ring(6), "k=6 powered (Z/12612600)"),
    (POWERED_7, "k=7 powered (Z/214414200)"),
]

print(f"\n  {'Ring':<30} {'chi':>15} {'-chi':>15} {'factors of -chi'}")
print(f"  {'-'*85}")
for ring, name in rings_for_chi:
    chi = euler_characteristic(ring)
    neg_chi = -chi
    fs = factor_str(abs(neg_chi)) if neg_chi > 0 else factor_str(abs(neg_chi))
    if neg_chi < 0:
        fs = "-" + factor_str(abs(neg_chi))
    print(f"  {name:<30} {chi:>15,} {neg_chi:>15,}  {fs}")

# Check: is -chi(RAD) axiom-smooth?
neg_chi_rad = -chi_rad
f_rad = factorize(abs(neg_chi_rad))
smooth = all(p in set(PRIMES) for p in f_rad)
intruders = [p for p in f_rad if p not in set(PRIMES)]
print(f"\n  -chi(RAD) = {neg_chi_rad:,} = {factor_str(abs(neg_chi_rad))}")
print(f"  Axiom-smooth: {'YES' if smooth else 'NO'}")
if intruders:
    print(f"  Intruder primes: {intruders}")

# Cross-lattice curvature: kappa_cross = (tau - |Idem|) / tau
# tau = number of divisors of N
from functools import reduce
def num_divisors(n):
    f = factorize(n)
    return reduce(lambda a, b: a * b, (e + 1 for e in f.values()), 1)

tau_rad = num_divisors(RAD_RING.N)
tau_pw = num_divisors(POWERED_7.N)
idem_rad = RAD_RING.num_idempotents
idem_pw = POWERED_7.num_idempotents

print(f"\n  CROSS-LATTICE CURVATURE: kappa = (tau - |Idem|) / tau")
print(f"    RAD:   tau = {tau_rad}, |Idem| = {idem_rad}, "
      f"kappa = {Fraction(tau_rad - idem_rad, tau_rad)} = "
      f"{(tau_rad - idem_rad)/tau_rad:.6f}")
print(f"    k=7 powered: tau = {tau_pw}, |Idem| = {idem_pw}, "
      f"kappa = {Fraction(tau_pw - idem_rad, tau_pw)} = "
      f"{(tau_pw - idem_pw)/tau_pw:.6f}")

# For squarefree N: tau = 2^k = |Idem|, so kappa = 0.
print(f"\n  SQUAREFREE THEOREM: For squarefree N, tau(N) = 2^k = |Idem|,")
print(f"    so kappa_cross = 0. RAD: tau = {tau_rad} = 2^{K_RAD} = {2**K_RAD} "
      f"= |Idem|. Check: {'CONFIRMED' if tau_rad == idem_rad else 'FAILED'}")
print(f"    Powered rings break this: tau = {tau_pw} > {idem_pw} = |Idem|.")


# ═══════════════════════════════════════════════════════════════════════
# V. HAMMING GRAPH ADJACENCY SPECTRUM
# ═══════════════════════════════════════════════════════════════════════

section("V. HAMMING GRAPH SPECTRUM (128 SUBSETS, 53 VALUES)")

print(f"""
The CRT Hamming graph is H = K_2 [] K_3 [] ... [] K_17 (Cartesian product).
K_p has adjacency eigenvalues: (p-1) with multiplicity 1, and -1 with
multiplicity (p-1). The product graph has one eigenvalue per subset S of
the channels, so 2^7 = 128 subset-indexed eigenvalues:

  lambda_S = sum_{{i not in S}} (p_i - 1) + sum_{{i in S}} (-1)
           = degree - sum_{{i in S}} p_i

They are NOT 128 distinct VALUES.
lambda_S depends on S only through the SUM of its primes, so the spectrum
is the subset sums reflected through the degree, and subsets sharing a sum
collide -- {{2,5}} and {{7}} both give 7. The distinct count is below.
""")

# Compute all 128 subset-indexed eigenvalues
hamming_evs = []
for mask in range(128):
    active = [i for i in range(7) if mask & (1 << i)]
    ev = deg_rad - sum(PRIMES[i] for i in active)
    mult = prod(PRIMES[i] - 1 for i in active) if active else 1
    hamming_evs.append((ev, mask, active, mult))

hamming_evs.sort(key=lambda x: -x[0])

print(f"  {'Rank':>4} {'EV':>6} {'Subset S':>30} {'|S|':>4} {'Mult':>10}")
print(f"  {'-'*60}")

# Show top 10 and bottom 10
for i, (ev, mask, active, mult) in enumerate(hamming_evs[:10]):
    subset = "{" + ",".join(str(PRIMES[j]) for j in active) + "}" if active else "{}"
    print(f"  {i+1:>4} {ev:>6} {subset:>30} {len(active):>4} {mult:>10,}")

print(f"  {'...':>4}")
for i, (ev, mask, active, mult) in enumerate(hamming_evs[-5:]):
    idx = 128 - 5 + i
    subset = "{" + ",".join(str(PRIMES[j]) for j in active) + "}"
    print(f"  {idx+1:>4} {ev:>6} {subset:>30} {len(active):>4} {mult:>10,}")

# Total multiplicity check
total_mult = sum(m for _, _, _, m in hamming_evs)
print(f"\n  Total multiplicity = {total_mult:,} (should be {RAD_RING.N:,})")
assert total_mult == RAD_RING.N

# The distinct count, and why it is that: the REACHABLE subset sums.
distinct_evs = {ev for ev, _, _, _ in hamming_evs}
total_p = sum(PRIMES)
reachable = {deg_rad - ev for ev in distinct_evs}
missing = sorted(set(range(total_p + 1)) - reachable)
print(f"\n  Distinct eigenvalues = {len(distinct_evs)} of {len(hamming_evs)} subsets")
print(f"  Subset sums run 0..{total_p}: {total_p + 1} candidates, unreachable {missing}")
print(f"  {total_p + 1} - {len(missing)} = {len(distinct_evs)}. The missing set is closed under")
print(f"  s -> {total_p} - s, since a subset and its complement sum to {total_p}; only")
print(f"  1, 4 and 6 carry information (1 is below the smallest prime, and 4 and 6")
print(f"  would need 2+2 and 3+3).")
assert len(distinct_evs) == 53
assert {total_p - r for r in reachable} == reachable
assert missing == [1, 4, 6, 52, 54, 57]

# Key eigenvalues
print(f"\n  Spectral gap = degree - second EV = {deg_rad} - {hamming_evs[1][0]} "
      f"= {deg_rad - hamming_evs[1][0]} = min(p_i) = {min(PRIMES)}")
print(f"  Most negative EV = degree - sum(p_i) = {deg_rad} - {sum(PRIMES)} "
      f"= {deg_rad - sum(PRIMES)} = -k = -{K_RAD}")

# Eigenvalue by weight
print(f"\n  Eigenvalues by |S|:")
print(f"  {'|S|':>4} {'Count':>6} {'EV range':>20} {'Sum of mults':>15}")
print(f"  {'-'*50}")
for w in range(8):
    evs_w = [(ev, m) for ev, _, a, m in hamming_evs if len(a) == w]
    if evs_w:
        total_m = sum(m for _, m in evs_w)
        ev_min = min(ev for ev, _ in evs_w)
        ev_max = max(ev for ev, _ in evs_w)
        print(f"  {w:>4} {len(evs_w):>6} [{ev_min:>6}, {ev_max:>6}] {total_m:>15,}")


# ═══════════════════════════════════════════════════════════════════════
# VI. HEAT KERNEL ON THE TORUS
# ═══════════════════════════════════════════════════════════════════════

section("VI. HEAT KERNEL")

print("""
Two heat kernels, two stories:

A. HAMMING HEAT KERNEL: diffusion on the CRT neighbor graph.
   Normalized Laplacian: L = I - A/degree.
   Eigenvalues of L: mu_S = 1 - lambda_S/degree = sum_{i in S} p_i / degree.
   Spectral gap = min_i (p_i / degree).

B. CHORD HEAT KERNEL: diffusion measured by spectral (cosine) distance.
   Spectral gap = 2*sin^2(pi/max_modulus) for weight 1.
""")

# A. Hamming heat kernel
lap_gap_rad = Fraction(min(PRIMES), deg_rad)
lap_gap_pw = Fraction(min(POWERED_7.moduli), deg_pw)
half_life_ham_rad = float(log(2) / float(lap_gap_rad))
half_life_ham_pw = float(log(2) / float(lap_gap_pw))

print(f"  A. HAMMING HEAT KERNEL")
print(f"     RAD:   Laplacian gap = {lap_gap_rad} = {float(lap_gap_rad):.6f}")
print(f"            Half-life = ln(2) / gap = {half_life_ham_rad:.2f}")
print(f"     k=7 powered: Laplacian gap = {lap_gap_pw} = {float(lap_gap_pw):.6f}")
print(f"            Half-life = ln(2) / gap = {half_life_ham_pw:.2f}")
print(f"     Ratio (squarefree/powered): {half_life_ham_rad/half_life_ham_pw:.2f}x")

# Per-channel Laplacian eigenvalue (contribution to heat decay)
print(f"\n     Per-channel Laplacian eigenvalue mu_i = p_i / degree:")
print(f"     {'Channel':<10} {'p_i':>4} {'mu_i':>12} {'1/mu_i':>10} {'Relaxation time':>16}")
print(f"     {'-'*55}")
for i, p in enumerate(PRIMES):
    mu = Fraction(p, deg_rad)
    relax = float(1 / float(mu))
    print(f"     Z/{p:<4} {p:>4} {float(mu):>12.6f} {relax:>10.2f} "
          f"{'(SLOWEST)' if p == min(PRIMES) else '(FASTEST)' if p == max(PRIMES) else ''}")

# B. Chord heat kernel
gap_w1_rad = 2 * sin(pi / max(PRIMES))**2
gap_w1_pw = 2 * sin(pi / max(POWERED_7.moduli))**2
half_life_chord_rad = log(2) / gap_w1_rad
half_life_chord_pw = log(2) / gap_w1_pw

print(f"\n  B. CHORD HEAT KERNEL (weight 1)")
print(f"     RAD:   gap = 2*sin^2(pi/17) = {gap_w1_rad:.6f}")
print(f"            Half-life = {half_life_chord_rad:.2f}")
print(f"     k=7 powered: gap = 2*sin^2(pi/49) = {gap_w1_pw:.6f}")
print(f"            Half-life = {half_life_chord_pw:.2f}")
print(f"     Ratio (powered/squarefree): {half_life_chord_pw/half_life_chord_rad:.1f}x")

# Per-channel chord forgetting rates
print(f"\n     Per-channel chord contribution = 2*sin^2(pi/p):")
print(f"     {'Channel':<10} {'p':>4} {'2*sin^2':>12} {'Forgetting %':>14}")
print(f"     {'-'*45}")
for i, p in enumerate(PRIMES):
    chord = 2 * sin(pi / p)**2
    # At time t = half-life, decay = exp(-chord * t)
    decay_at_half = 1 - 2**(-chord / gap_w1_rad)
    print(f"     Z/{p:<4} {p:>4} {chord:>12.6f} {decay_at_half:>13.1%}")

print(f"""
  KEY FINDING: The two heat kernels tell opposite stories about Z/2.

  HAMMING: Z/2 is the SLOWEST to forget. The 2-point circle has the
  smallest Laplacian eigenvalue (2/51). It's the bottleneck for mixing
  on the graph — the 2-channel equilibrates last.

  CHORD: Z/2 is the FASTEST to forget. cos(2*pi*0/2)=1, cos(2*pi*1/2)=-1.
  Maximum spectral contrast, instant decay to equilibrium.

  Z/2 is metrically trivial (just 2 points) but topologically persistent
  (the binary choice is the hardest to randomize on the graph).
""")


# ═══════════════════════════════════════════════════════════════════════
# VII. DISTANCE DISTRIBUTION
# ═══════════════════════════════════════════════════════════════════════

section("VII. DISTANCE DISTRIBUTION (SHELL POLYNOMIAL)")

print(f"""
On the Hamming graph, the distance-d shell from any point has size
given by the shell polynomial:

  E(x) = prod_i (1 + (p_i - 1)*x)

Coefficient of x^d = number of elements at Hamming distance d.
""")

# Compute shell polynomial coefficients
# E(x) = (1+x)(1+2x)(1+4x)(1+6x)(1+10x)(1+12x)(1+16x)
coeffs = [1]  # start with constant polynomial "1"
for p in PRIMES:
    new_coeffs = [0] * (len(coeffs) + 1)
    for j, c in enumerate(coeffs):
        new_coeffs[j] += c          # * 1
        new_coeffs[j+1] += c * (p - 1)  # * (p-1)*x
    coeffs = new_coeffs

print(f"  E(x) = {'(1+x)' if PRIMES[0] == 2 else ''}", end="")
for p in PRIMES[1:]:
    print(f"(1+{p-1}x)", end="")
print()

print(f"\n  {'Distance':>10} {'Shell size':>15} {'Fraction':>10} {'Cumulative':>12} "
      f"{'Factored'}")
print(f"  {'-'*70}")
cumul = 0
for d in range(K_RAD + 1):
    cumul += coeffs[d]
    frac = coeffs[d] / RAD_RING.N
    cumfrac = cumul / RAD_RING.N
    fs = factor_str(coeffs[d]) if coeffs[d] > 1 else "1"
    print(f"  {d:>10} {coeffs[d]:>15,} {frac:>10.4f} {cumfrac:>12.4f}  {fs}")

print(f"\n  Total = {sum(coeffs):,} (should be {RAD_RING.N:,})")
assert sum(coeffs) == RAD_RING.N

# Compare with Betti numbers
print(f"\n  Shell sizes vs Betti numbers C(7,d):")
print(f"  {'d':>4} {'Shell e_d':>12} {'C(7,d)':>8} {'Ratio':>10}")
print(f"  {'-'*38}")
for d in range(K_RAD + 1):
    betti = comb(K_RAD, d)
    ratio = coeffs[d] / betti if betti > 0 else 0
    print(f"  {d:>4} {coeffs[d]:>12,} {betti:>8} {ratio:>10.1f}")

# Notable shell values
print(f"\n  Notable:")
print(f"    e_1 = {coeffs[1]} = sum(p_i - 1) = degree (neighbors)")
print(f"    e_7 = {coeffs[7]:,} = prod(p_i - 1) = phi(RAD) = {RAD_RING.phi:,}")
print(f"    e_2 = {coeffs[2]:,}")
e2_f = factorize(coeffs[2])
print(f"       = {factor_str(coeffs[2])}")

# Chromatic number and independence number
print(f"\n  CHROMATIC NUMBER chi(H) = max(p_i) = {max(PRIMES)}")
print(f"  INDEPENDENCE NUMBER alpha = N / max(p_i) = {RAD_RING.N} / {max(PRIMES)}")
alpha = RAD_RING.N // max(PRIMES)
print(f"    = {alpha:,} = {factor_str(alpha)}")
print(f"    = Z/30030 = rung 6")

# Compare with the powered ring
alpha_pw = POWERED_7.N // max(POWERED_7.moduli)
print(f"\n  Powered: chi(H) = max(q_i) = {max(POWERED_7.moduli)} = 7^2")
print(f"       alpha = N/49 = {alpha_pw:,}")

# When squarefree, the largest non-conflicting set IS the 6-prime sub-ring
print(f"\n  CHROMATIC-DEPTH THEOREM (squarefree):")
print(f"    The largest independent set in rung 7's Hamming graph = {alpha:,}")
print(f"    = Z/30030 = rung 6, the same ring with 17 dropped.")
print(f"    The largest non-conflicting set is the ring WITH the coloring prime removed.")


# ═══════════════════════════════════════════════════════════════════════
# VIII. FORMAN-RICCI CURVATURE
# ═══════════════════════════════════════════════════════════════════════

section("VIII. FORMAN-RICCI CURVATURE")

print("""
Forman-Ricci curvature on the Hamming graph:
  F_i = 3*q_i - (2*degree + 2)

This is a coarser combinatorial curvature. Linear in q_i.
""")

print(f"  {'Channel':<12} {'q_i':>4} {'F_i':>8} {'Sign':>6}")
print(f"  {'-'*35}")

forman_sum = 0
for i, p in enumerate(PRIMES):
    F = 3 * p - (2 * deg_rad + 2)
    forman_sum += F
    sign = "+" if F > 0 else "-" if F < 0 else "0"
    print(f"  Z/{p:<4} {p:>4} {F:>8} {sign:>6}")

print(f"\n  Sum of Forman curvatures = {forman_sum}")
print(f"  = 3*sum(p_i) - 7*(2*degree + 2) = 3*{sum(PRIMES)} - 7*{2*deg_rad + 2} = {forman_sum}")

# All negative for RAD: degree = 51 is large relative to any modulus
print(f"\n  All Forman curvatures are NEGATIVE at rung 7 (and at any ring with")
print(f"  degree >> max(q_i)). The Hamming graph is sparse relative to its degree.")


# ═══════════════════════════════════════════════════════════════════════
# IX. 2-INVISIBILITY IN TORUS GEOMETRY
# ═══════════════════════════════════════════════════════════════════════

section("IX. 2-INVISIBILITY — THE TOPOLOGICAL INTERPRETATION")

print(f"""
2-INVISIBILITY (rule, proved; explore_seed_flower_rad.py):
  2 is NEVER named by any squarefree sub-ring that doesn't contain it.
  Proof: -chi of an odd-prime sub-ring is always odd.

IN TORUS TERMS:
  The 2-axis of T^7 is S^1(2) = {{0, 1}} — a 2-point discrete circle.
  Every odd-prime sub-torus T^k in T^7 (built from odd primes only)
  projects onto a SINGLE point in the 2-direction.

  WHY the topology can't see it:
""")

# Compute: for each odd-prime subset, show that -chi is odd
odd_primes = [p for p in PRIMES if p > 2]
print(f"  Odd-prime sub-rings: subsets of {odd_primes}")
print(f"  For Z/(p1*p2*...*pk) with all p_i odd:")
print(f"    N = product of odd primes = ODD")
print(f"    Each N/p_i = product of (k-1) odd primes = ODD")
print(f"    -chi = N*(k-1) - sum(N/p_i) = ODD*(k-1) - k*ODD")
print(f"         = ODD*(k-1-k) = ODD*(-1) = ODD")
print(f"  So 2 never divides -chi. The 2-channel is topologically invisible.")

# Verify by computing
print(f"\n  Verification — all 63 odd-prime sub-rings:")
print(f"  {'Size':>5} {'Count':>6} {'All -chi odd?':>14} {'2 nmid -chi':>20}")
print(f"  {'-'*50}")
for size in range(1, 7):
    all_odd = True
    count = 0
    for subset in combinations(range(6), size):
        ps = [odd_primes[i] for i in subset]
        N = prod(ps)
        nc = N * (size - 1) - sum(N // p for p in ps)
        if nc % 2 == 0:
            all_odd = False
        count += 1
    print(f"  {size:>5} {count:>6} {'YES':>14} {'CONFIRMED':>20}" if all_odd
          else f"  {size:>5} {count:>6} {'NO — VIOLATION':>14}")

# Geometric meaning
print(f"""
  GEOMETRIC INTERPRETATION:
    On T^7, the 2-coordinate is a parity bit (0 or 1).
    The projection T^7 -> T^6 (drop it) collapses each fiber
    {{(0,r2,...,r7), (1,r2,...,r7)}}
    to a single point (r2,...,r7).

    The Euler characteristic of ANY odd-prime sub-torus is always ODD.
    Since chi = -(-chi), and -chi is always odd, chi is always odd too.
    An odd chi can never be divisible by 2.

    2 is the BRIDGE — and bridges are invisible from inside.
    You cross the bridge to get to the rest of the torus, but the topology
    of the territory you're standing in can never name the bridge.

    This is 2-invisibility in its torus-geometric form.
""")


# ═══════════════════════════════════════════════════════════════════════
# X. CURVATURE PHASE TRANSITION: SQUAREFREE -> POWERED
# ═══════════════════════════════════════════════════════════════════════

section("X. CURVATURE PHASE TRANSITION")

print("""
Raising the first four channels to prime powers is a curvature phase
transition. While every channel is a field, every structural invariant
below is simpler.
""")

# Compare key quantities across the tower
squarefree_tower = [(primorial_ring(k), f"k={k}") for k in (4, 5, 6, 7)]
powered_tower = [(primorial_ring(4), "k=4")] + [
    (powered_ring(k), f"k={k} powered") for k in (5, 6, 7)]

print(f"  SQUAREFREE TOWER:")
print(f"  {'Ring':<12} {'N':>10} {'deg':>5} {'tau':>5} {'|Idem|':>7} {'kappa_cross':>12}"
      f" {'chi':>15}")
print(f"  {'-'*70}")
for ring, name in squarefree_tower:
    tau = num_divisors(ring.N)
    idem = ring.num_idempotents
    kappa_c = Fraction(tau - idem, tau)
    chi = euler_characteristic(ring)
    deg = hamming_degree(ring)
    print(f"  {name:<12} {ring.N:>10,} {deg:>5} {tau:>5} {idem:>7} "
          f"{str(kappa_c):>12} {chi:>15,}")

print(f"\n  POWERED TOWER:")
print(f"  {'Ring':<12} {'N':>10} {'deg':>5} {'tau':>5} {'|Idem|':>7} {'kappa_cross':>12}"
      f" {'chi':>15}")
print(f"  {'-'*70}")
for ring, name in powered_tower:
    tau = num_divisors(ring.N)
    idem = ring.num_idempotents
    kappa_c = Fraction(tau - idem, tau)
    chi = euler_characteristic(ring)
    deg = hamming_degree(ring)
    print(f"  {name:<12} {ring.N:>10,} {deg:>5} {tau:>5} {idem:>7} "
          f"{str(kappa_c):>12} {chi:>15,}")

print(f"""
  THE PHASE TRANSITION:
    Squarefree tower: kappa_cross = 0 everywhere (tau = 2^k = |Idem|).
    Powered tower:    kappa_cross = 23/27 everywhere (from k=5 onward).

    The boundary is k=4 -> k=5 powered: squarefree -> prime-power channels.
    This is the SAME boundary as:
      - Meadow -> non-meadow
      - Von Neumann regular -> non-regular
      - All channels fields -> some channels rings

    When squarefree, divisor lattice and idempotent lattice are identical:
    both are the Boolean lattice 2^{{1,...,k}}. Powered, the divisor lattice
    is strictly larger: prime-power exponents add divisors beyond idempotents.
""")


# ═══════════════════════════════════════════════════════════════════════
# XI. MIXING TIME
# ═══════════════════════════════════════════════════════════════════════

section("XI. MIXING TIME COMPARISON")

print(f"""
Relaxation time of the random walk, ONE instrument on both graphs:

  t_rel = degree / (smallest nonzero Laplacian eigenvalue)

On the CRT Hamming graph the Laplacian is the sum of the per-channel
Laplacians, whose nonzero eigenvalues are the moduli themselves, so the
gap is min(q_i).  On the cycle Z/N the degree is 2 and the gap is
2 - 2cos(2pi/N), which is ~ 4pi^2/N^2 -- the quadratic that makes a
cycle slow.  Reading both with the same formula is the point: a
comparison of two DIFFERENT conventions would measure the conventions.

The cycle gap is evaluated as 4 sin^2(pi/N), never as 2 - 2cos(2pi/N).
They are the same number and the second is unusable here: at N = 2.1e8
the cosine sits within 1e-15 of 1, so the subtraction cancels away all
but about one significant digit and the printed relaxation time comes
out ~3% low.  The sine form has no cancellation at any N.
""")

# CRT mixing vs cyclic mixing, same instrument on both
for ring, name in [(RAD_RING, "k=7"), (POWERED_7, "k=7 powered")]:
    deg = hamming_degree(ring)
    gap = min(ring.moduli)
    t_rel_crt = deg / gap
    gap_cycle = 4.0 * sin(pi / ring.N) ** 2
    t_rel_cyclic = 2.0 / gap_cycle
    ratio = t_rel_cyclic / t_rel_crt
    print(f"  {name}: N = {ring.N:,}, degree = {deg}, gap = {gap}, "
          f"t_rel(CRT) ~ {t_rel_crt:.1f}")
    print(f"    Cycle Z/N: degree 2, gap {gap_cycle:.3e}, "
          f"t_rel ~ {t_rel_cyclic:.3e} (~ N^2/2pi^2)")
    print(f"    CRT/cyclic ratio: {ratio:.3e}x faster")

print(f"""
  The separation is not a constant factor and not a factor of N: the
  cycle's relaxation time is QUADRATIC in N while the product graph's
  is degree/min(q_i), a ratio of two small integers that barely moves
  as the tower grows.  Both walks visit the same N elements; only one
  of them has to travel to reach them.  The k channels mix at once
  because the Laplacian is their sum, so the slowest channel alone sets
  the gap -- which is why the SMALLEST modulus is the bottleneck and a
  powered tower, whose smallest modulus is 8 rather than 2, relaxes
  faster than the squarefree one despite being 420 times larger.
""")


# ═══════════════════════════════════════════════════════════════════════
# XII. BETTI NUMBERS AND THE IDEMPOTENT LATTICE
# ═══════════════════════════════════════════════════════════════════════

section("XII. BETTI NUMBERS AND THE IDEMPOTENT LATTICE")

print(f"""
The Betti numbers of T^7 are beta_d = C(7,d):

  d:       0    1    2    3    4    5    6    7
  C(7,d):  1    7   21   35   35   21    7    1
  sum = 2^7 = 128 = |Idem(RAD)|

The d-th Betti number = number of weight-d idempotents.
""")

# The 490 split as a cell decomposition
print(f"  THE 490 SPLIT AS A CELL DECOMPOSITION:")
print(f"    DEAD (zero residues)  = {{2, 5, 7}}      weight-3 idempotent,")
print(f"                            beta_3 = C(7,3) = {comb(7,3)}")
print(f"    ALIVE (unit residues) = {{3, 11, 13, 17}} weight-4 idempotent,")
print(f"                            beta_4 = C(7,4) = {comb(7,4)}")
print(f"    Both beta_3 = beta_4 = 35 = {factor_str(35)}.")
print(f"    The 490 split IS a Poincare-dual cell decomposition of T^7.")

# All C(7,k) mod 7 = 0 for 1 <= k <= 6
print(f"\n  DIVISIBILITY BY b = 7:")
print(f"  {'d':>4} {'C(7,d)':>8} {'mod 7':>6} {'C(7,d)/7':>10}")
print(f"  {'-'*32}")
for d in range(8):
    c = comb(7, d)
    print(f"  {d:>4} {c:>8} {c % 7:>6}"
          f"{'':>4}{c // 7 if c % 7 == 0 and d > 0 and d < 7 else '':>6}")

# Normalized Betti sequence
normalized = [comb(7, d) // 7 for d in range(1, 7)]
print(f"\n  Normalized interior Betti: C(7,d)/7 = {normalized}")
print(f"  Palindromic: {normalized == normalized[::-1]}")
print(f"  Uses only primes: {sorted(set(normalized))} = {{1, 3, 5}}")


# ═══════════════════════════════════════════════════════════════════════
# XIII. THE DIAGONAL AND SIGMA'S WINDING
# ═══════════════════════════════════════════════════════════════════════

section("XIII. SIGMA'S DIAGONAL WINDING")

print(f"""
Sigma = 1 has CRT tuple (1, 1, 1, 1, 1, 1, 1).
Adding sigma rotates each circle by 1 step: the DIAGONAL of T^7.
After n steps: (n mod 2, n mod 3, ..., n mod 17).
""")

# When does sigma's walk return to the origin?
print(f"  Sigma winds the diagonal. Period = lcm(2,3,5,7,11,13,17) = {RAD_RING.N}")
print(f"  (Sigma visits EVERY point on T^7 before returning. The walk is dense.)")

# Per-channel return times
print(f"\n  Per-channel return times (when that coordinate returns to 0):")
print(f"  {'Channel':<10} {'Period':>8} {'Fraction of walk':>18}")
for p in PRIMES:
    print(f"  Z/{p:<4} {p:>8} {1/p:>18.4f}")

# First return to a particular channel combination being zero
print(f"\n  First time ALL data channels (2,3,5,7) are simultaneously 0:")
data_period = prod(PRIMES[:4])
print(f"    lcm(2,3,5,7) = {data_period} = Z/210 = rung 4.")
print(f"    At step {data_period}, CRT = (0,0,0,0, 210 mod 11, 210 mod 13, 210 mod 17)")
t_210 = encode(210, RAD_RING)
print(f"                         = (0,0,0,0, {t_210[4]}, {t_210[5]}, {t_210[6]})")

print(f"\n  First time ALL parity channels (11,13,17) are simultaneously 0:")
parity_period = 11 * 13 * 17
print(f"    lcm(11,13,17) = {parity_period}")
t_par = encode(parity_period, RAD_RING)
print(f"    At step {parity_period}, CRT = ({t_par[0]},{t_par[1]},{t_par[2]},{t_par[3]}, 0,0,0)")


# ═══════════════════════════════════════════════════════════════════════
# XIV. SQUAREFREE vs POWERED TORUS — SUMMARY
# ═══════════════════════════════════════════════════════════════════════

section("XIV. SQUAREFREE vs POWERED TORUS — COMPLETE COMPARISON")

print(f"""
  {'Property':<35} {'k=7':>20} {'k=7 powered':>20}
  {'='*77}
  Ring                                 Z/510510             Z/214414200
  Channels                             7 fields             4 rings + 3 fields
  N                                    {RAD_RING.N:>15,}      {POWERED_7.N:>15,}
  phi                                  {RAD_RING.phi:>15,}      {POWERED_7.phi:>15,}
  lambda                               {RAD_RING.lam:>15}      {POWERED_7.lam:>15}
  Idempotents                          {RAD_RING.num_idempotents:>15}      {POWERED_7.num_idempotents:>15}
  {'-'*77}
  Hamming degree                       {deg_rad:>15}      {deg_pw:>15}
  Hamming spectral gap                 {min(PRIMES):>15}      {min(POWERED_7.moduli):>15}
  Chord spectral gap (w=1)             {gap_w1_rad:>15.6f}      {gap_w1_pw:>15.6f}
  Chord gap ratio                      {gap_w1_rad/gap_w1_pw:>15.1f}x     1.0x
  {'-'*77}
  Eigenvalue classes                   {prod(p//2+1 for p in PRIMES):>15,}      {prod(q//2+1 for q in POWERED_7.moduli):>15,}
  Spectral fingerprint                 {f"all distinct":>15}      {f"all distinct":>15}
  {'-'*77}
  Hamming heat half-life               {half_life_ham_rad:>15.2f}      {half_life_ham_pw:>15.2f}
  Chord heat half-life                 {half_life_chord_rad:>15.2f}      {half_life_chord_pw:>15.2f}
  {'-'*77}
  Cross-lattice kappa                  {f"0":>15}      {f"23/27":>15}
  Ollivier-Ricci (2 channel)           {f"0 (flat)":>15}      {f"6/125":>15}
  Ollivier-Ricci (sum)                 {float(kappa_sum):>15.4f}      {float(kappa_pw_sum):>15.4f}
  Euler characteristic chi             {euler_characteristic(RAD_RING):>15,}      {euler_characteristic(POWERED_7):>15,}
  {'-'*77}
  Diameter                             {K_RAD:>15}      {K_RAD:>15}
  Chromatic number                     {max(PRIMES):>15}      {max(POWERED_7.moduli):>15}
  Independence number                  {RAD_RING.N // max(PRIMES):>15,}      {POWERED_7.N // max(POWERED_7.moduli):>15,}
  Meadow (total pseudo-inverse)        {"YES":>15}      {"NO":>15}
""")


# ═══════════════════════════════════════════════════════════════════════
# XV. KEY FINDINGS
# ═══════════════════════════════════════════════════════════════════════

section("XV. KEY FINDINGS")

print(f"""
1. GAP DUALITY. The Hamming gap is controlled by the SMALLEST channel
   (2, the bridge). The chord gap by the LARGEST (17). Two complementary
   views of T^7: the smallest channel controls topology, the largest
   controls spectroscopy.

2. CURVATURE PHASE TRANSITION. The squarefree tower has kappa_cross = 0
   everywhere (tau = 2^k = |Idem|). Powered, kappa_cross = 23/27. The
   boundary is rung 4 -> rung 5 powered: squarefree -> prime-power. This
   is the SAME boundary as meadow, regularity, and lattice structure.

3. HEAT KERNEL DUALITY. The Hamming heat kernel has Z/2 as the slowest
   channel (smallest Laplacian eigenvalue: 2/51). The chord heat kernel
   has it as the fastest (maximum cosine contrast). Z/2 is metrically
   trivial but topologically persistent.

4. 2-INVISIBILITY IN TORUS FORM. The 2-coordinate is a parity bit on
   T^7. Odd-prime sub-tori have Euler characteristic always odd, so
   2 can never divide -chi. The bridge is invisible from inside —
   you have to cross it to know it exists.

5. CHROMATIC-DEPTH THEOREM. chi(H) = 17 at rung 7: the largest prime
   colors the graph. The independence number alpha = 30030 = rung 6 =
   the largest sub-ring that fits inside rung 7 without 17. The coloring
   prime determines the maximum non-conflicting subset.

6. MIXING ACCELERATION, AND IT IS QUADRATIC RATHER THAN LINEAR. Read
   with one instrument on both graphs -- degree over the smallest
   nonzero Laplacian eigenvalue -- the cycle Z/510510 relaxes in
   ~1.3e10 steps and the product graph in 51/2 ~ 26, a factor 5.2e8.
   The cycle's time is ~ N^2/2pi^2, so the separation GROWS like N and
   is not the ~20,000x a linear reading of the cycle would report. The
   7 channels mix at once because the Laplacian is their sum, so the
   smallest modulus alone sets the gap.

7. BETTI-IDEMPOTENT CORRESPONDENCE. beta_d(T^7) = C(7,d) = number of
   weight-d idempotents. Sum = 128 = 2^7. The 490 split — zero residues
   at {{2, 5, 7}} (weight 3), unit residues at {{3, 11, 13, 17}} (weight
   4) — is a Poincare-dual cell decomposition. Interior Betti numbers
   C(7,d)/7 = {{1,3,5,5,3,1}}: palindromic, using only {{1, 3, 5}}.

8. OLLIVIER-RICCI, SQUAREFREE. Z/2 is FLAT (kappa = 0). Z/17 is most
   curved (kappa = 15/51 = 5/17). Total Ollivier-Ricci curvature = 44/51.
   Curvature numerators p-2 sum to 44 = 2^2 * 11.

9. THE SPECTRUM IS A SUBSET-SUM PROBLEM, AND HAS 53 VALUES, NOT 128.
   lambda_S = degree - sum_{{i in S}} p_i depends on S only through the
   sum, so subsets sharing a sum collide: {{2,5}} and {{7}} both give 7.
   Subset sums run 0..58, six are unreachable (1, 4, 6 and their
   reflections 52, 54, 57), and 59 - 6 = 53. The missing set is
   symmetric because a subset and its complement sum to 58, so only
   1, 4 and 6 carry information. Section V asserts all of it.
""")

print("=" * 72)
print("  Done. Rung 7 torus geometry mapped.")
print("=" * 72)
