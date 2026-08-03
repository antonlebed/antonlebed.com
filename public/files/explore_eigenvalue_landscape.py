"""Eigenvalue landscape of rung 7, Z/510510 — the squarefree 7-channel ring.

RAD has 18,144 eigenvalue classes. Each class is indexed by a tuple
(c0, c1, ..., c6) where ci in {0, 1, ..., floor(pi/2)} — the "half-residues"
that give distinct cosine values in each GF(p).

This script maps the full landscape: distribution, extremes, gaps,
moments, and structure. The spectral fingerprint theorem guarantees
all 18,144 eigenvalues are distinct.

Run: python prime/code/explore_eigenvalue_landscape.py
Run record: 0.3 s wall, 21 MB peak (memwatch, 512 MB limit).
"""

from math import cos, sin, pi, sqrt, log2, gcd, prod
from fractions import Fraction
from collections import Counter, defaultdict
from itertools import product as iterproduct
from crt import (
    Ring, RAD_RING, primorial_ring, powered_ring,
    encode, decode, eigenvalue, eigenvalue_of, spectral_gap,
    chord_distance_sq, euler_phi, carmichael_lambda, factorize,
    hamming_degree,
)


def section(title):
    print(f"\n{'=' * 72}")
    print(f"  {title}")
    print(f"{'=' * 72}")


# ═══════════════════════════════════════════════════════════════════════
# I. THE 18,144 EIGENVALUE CLASSES
# ═══════════════════════════════════════════════════════════════════════

section("I. RUNG 7 EIGENVALUE CLASS CENSUS")

# The prime-power variant of the same rung: first four channels raised to
# (3, 2, 2, 2). Every comparison below is squarefree rung 7 against this.
POWERED_7 = powered_ring(7)

PRIMES = RAD_RING.primes  # [2, 3, 5, 7, 11, 13, 17]
MODULI = RAD_RING.moduli  # same (all exp 1)

# Per-channel class counts: floor(p/2) + 1
per_ch_classes = [p // 2 + 1 for p in PRIMES]
total_classes = prod(per_ch_classes)

print(f"\nRung 7 moduli: {list(MODULI)}")
print(f"Per-channel eigenvalue classes: {per_ch_classes}")
print(f"  = floor(p/2)+1 for p in {list(PRIMES)}")
print(f"Total classes: {'*'.join(map(str, per_ch_classes))} = {total_classes:,}")

# Factorize total
f = factorize(total_classes)
f_str = " * ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(f.items()))
print(f"  = {f_str}")

# For comparison
deep_classes = prod(q // 2 + 1 for q in powered_ring(5).moduli)
pw7_classes = prod(q // 2 + 1 for q in POWERED_7.moduli)
print(f"\nComparison: k=5 powered = {deep_classes:,}, k=7 powered = {pw7_classes:,}")
print(f"  k=7 ratio, squarefree to powered = {total_classes}/{pw7_classes}"
      f" = {Fraction(total_classes, pw7_classes)}")


# ═══════════════════════════════════════════════════════════════════════
# II. ENUMERATE ALL CLASSES
# ═══════════════════════════════════════════════════════════════════════

section("II. FULL EIGENVALUE ENUMERATION")

print(f"\nComputing all {total_classes:,} eigenvalue classes...")

# Each class is indexed by (c0, ..., c6) where ci in {0, ..., floor(pi/2)}.
# Two normalizations differ by the constant factor 2: the library weighs
# each channel 2 (degree 2k); this script computes weight 1 (degree k = 7)
# and prints both where a comparison needs the library's convention.

# Precompute cosine tables per channel
cos_table = []
for p in PRIMES:
    table = []
    for c in range(p // 2 + 1):
        table.append(cos(2 * pi * c / p))
    cos_table.append(table)

# Multiplicity of each class: how many ring elements map to it
# For channel Z/p, class c has multiplicity:
#   c = 0: 1 element (just 0)
#   0 < c < p/2: 2 elements (c and p-c give same cosine)
#   c = p/2 (only when p even, i.e. p=2, c=1): 1 element
def class_multiplicity(class_tuple):
    m = 1
    for c, p in zip(class_tuple, PRIMES):
        if c == 0:
            m *= 1
        elif p == 2 and c == 1:
            m *= 1  # Z/2, residue 1
        elif 2 * c == p:
            m *= 1  # midpoint (can't happen for odd primes)
        else:
            m *= 2
    return m

# Enumerate
classes = []  # (eigenvalue_w1, eigenvalue_w2, class_tuple, multiplicity)
total_mult = 0

for class_tuple in iterproduct(*(range(p // 2 + 1) for p in PRIMES)):
    ev_w1 = sum(cos_table[i][c] for i, c in enumerate(class_tuple))  # weight 1
    ev_w2 = 2 * ev_w1  # weight 2 (library default)
    mult = class_multiplicity(class_tuple)
    classes.append((ev_w1, ev_w2, class_tuple, mult))
    total_mult += mult

print(f"Enumerated {len(classes):,} classes.")
print(f"Total multiplicity check: {total_mult:,} (should be {RAD_RING.N:,})")
assert total_mult == RAD_RING.N, f"Multiplicity mismatch: {total_mult} != {RAD_RING.N}"

# Sort by eigenvalue (weight 1)
classes.sort(key=lambda x: x[0])

# Verify all distinct
evs_w1 = [c[0] for c in classes]
for i in range(len(evs_w1) - 1):
    if abs(evs_w1[i] - evs_w1[i + 1]) < 1e-15:
        print(f"  WARNING: eigenvalues {i} and {i+1} are equal!")
        break
else:
    print("All 18,144 eigenvalues confirmed DISTINCT.")


# ═══════════════════════════════════════════════════════════════════════
# III. DISTRIBUTION STATISTICS
# ═══════════════════════════════════════════════════════════════════════

section("III. DISTRIBUTION STATISTICS")

# Weight-1 eigenvalues: degree = 7 (sum of 7 cos values, each in [-1, 1])
# Max = 7 (all cos = 1, all residues = 0 -> element 0)
# Min = sum of min cos values per channel

ev_max_w1 = classes[-1][0]
ev_min_w1 = classes[0][0]
degree_w1 = len(PRIMES)

print(f"\nWeight-1 eigenvalues (degree = {degree_w1}):")
print(f"  Maximum: {ev_max_w1:.6f} (class {classes[-1][2]})")
print(f"    = {degree_w1} (all residues 0 -> element 0)")
print(f"  Minimum: {ev_min_w1:.6f} (class {classes[0][2]})")

# The minimum class: each channel contributes its minimum cosine
print(f"\n  Per-channel minimum cos(2*pi*c/p):")
for i, p in enumerate(PRIMES):
    c_min = p // 2  # the class giving minimum cos
    cos_min = cos(2 * pi * c_min / p)
    print(f"    Z/{p}: c = {c_min}, cos(2*pi*{c_min}/{p}) = {cos_min:.6f}")

# Moments (weighted by multiplicity = true distribution over ring elements)
total_w = RAD_RING.N
mean_w1 = sum(ev * mult for ev, _, _, mult in classes) / total_w
var_w1 = sum((ev - mean_w1)**2 * mult for ev, _, _, mult in classes) / total_w
std_w1 = sqrt(var_w1)

# Unweighted moments (over classes)
mean_class = sum(ev for ev, _, _, _ in classes) / len(classes)

print(f"\nRing-element-weighted moments:")
print(f"  Mean     = {mean_w1:.6f}")
print(f"  Variance = {var_w1:.6f}")
print(f"  Std dev  = {std_w1:.6f}")
print(f"  Degree   = {degree_w1}")
print(f"  Var/deg  = {var_w1/degree_w1:.6f}")

# Variance, squarefree: Z/2 contributes Var(cos) = 1, odd primes 1/2.
# Total = 1 + 6*(1/2) = 4 = (k+1)/2. Powered (all q >= 3): k/2.
print(f"  Expected: (k+1)/2 = {(degree_w1+1)/2:.6f}  (the 2-channel gives 1, not 1/2)")
print(f"  Powered formula (k/2): {degree_w1/2:.6f}")

# Skewness and kurtosis
m3 = sum((ev - mean_w1)**3 * mult for ev, _, _, mult in classes) / total_w
m4 = sum((ev - mean_w1)**4 * mult for ev, _, _, mult in classes) / total_w
skewness = m3 / var_w1**1.5
kurtosis = m4 / var_w1**2 - 3  # excess kurtosis

# Skewness, squarefree: only Z/3 contributes (cos^3 mean = 1/4 there).
# m3 = 1/4. skewness = (1/4) / 4^(3/2) = 1/32.
print(f"\n  Third moment (m3) = {m3:.6f}  (expected: 1/4 = {0.25:.6f}, from 3 alone)")
print(f"  Skewness       = {skewness:.6f}  (expected: 1/32 = {1/32:.6f})")
print(f"  Source: 3 only. cos^3 mean over GF(3) = 1/4. Powered (Z/9): 0.")

print(f"\n  Excess kurtosis = {kurtosis:.6f}")
print(f"  Powered formula: -3/(2k) = {-3/(2*degree_w1):.6f}")
print(f"  Sub-Gaussian (platykurtic): {'YES' if kurtosis < 0 else 'NO'}")


# ═══════════════════════════════════════════════════════════════════════
# IV. EXTREMES AND SPECTRAL GAP
# ═══════════════════════════════════════════════════════════════════════

section("IV. EXTREMES AND SPECTRAL GAP")

# Top 10 and bottom 10
print("\nTop 10 eigenvalue classes:")
print(f"  {'Rank':<6} {'ev(w=1)':>10} {'Class tuple':<30} {'Mult':>6}")
print(f"  {'-'*55}")
for i, (ev, _, ct, mult) in enumerate(reversed(classes[-10:])):
    print(f"  {i+1:<6} {ev:>10.6f} {str(ct):<30} {mult:>6}")

print("\nBottom 10 eigenvalue classes:")
print(f"  {'Rank':<6} {'ev(w=1)':>10} {'Class tuple':<30} {'Mult':>6}")
print(f"  {'-'*55}")
for i, (ev, _, ct, mult) in enumerate(classes[:10]):
    print(f"  {i+1:<6} {ev:>10.6f} {str(ct):<30} {mult:>6}")

# Spectral gap: eigenvalue of element nearest to 0 (which has ev = degree)
# = degree - second-largest eigenvalue
# = minimum chord distance squared
gap = degree_w1 - classes[-2][0]
print(f"\nSpectral gap (w=1): {gap:.6f}")
print(f"  = degree - second eigenvalue = {degree_w1} - {classes[-2][0]:.6f}")
print(f"  Second eigenvalue achieved by class {classes[-2][2]}")

# Squarefree, the spectral gap = 4*sin^2(π/max_modulus) / 2 (for w=1)
# = 2*sin^2(π/17)
sf_gap = 2 * sin(pi / max(PRIMES))**2
print(f"\n  Theoretical: 2*sin^2(pi/17) = {sf_gap:.6f}")
print(f"  Match: {'YES' if abs(gap - sf_gap) < 1e-10 else 'NO'}")

# Compare with the powered ring
pw_gap = 2 * sin(pi / max(POWERED_7.moduli))**2
print(f"\n  POWERED (k=7): 2*sin^2(pi/49) = {pw_gap:.6f}")
print(f"  Squarefree/powered gap ratio = {sf_gap / pw_gap:.2f}x")
print(f"  Squarefree has the WIDER gap (easier to distinguish neighbors)")


# ═══════════════════════════════════════════════════════════════════════
# V. EIGENVALUE SPACING DISTRIBUTION
# ═══════════════════════════════════════════════════════════════════════

section("V. EIGENVALUE SPACING")

print("\nNearest-neighbor spacings between sorted eigenvalues:")

spacings = [evs_w1[i+1] - evs_w1[i] for i in range(len(evs_w1) - 1)]
mean_spacing = sum(spacings) / len(spacings)

# Global unfolding (divide by global mean). NOTE: this is a rough measure;
# proper Poisson/GOE testing needs LOCAL density unfolding (the eigenvalue
# density is non-uniform, so global unfolding inflates variance).
unfolded = [s / mean_spacing for s in spacings]

var_spacing = sum((s - 1)**2 for s in unfolded) / len(unfolded)
print(f"  Mean spacing: {mean_spacing:.8f}")
print(f"  Unfolded variance (global): {var_spacing:.4f}")
print(f"    (Poisson = 1.0, GOE = 0.273; global unfolding inflates this)")

# Spacing histogram (10 bins)
max_spacing = max(unfolded)
nbins = 10
bin_width = max_spacing / nbins
bins = [0] * nbins
for s in unfolded:
    b = min(int(s / bin_width), nbins - 1)
    bins[b] += 1

print(f"\n  Spacing histogram (normalized):")
print(f"  {'Bin':<15} {'Count':>8} {'Density':>10}")
print(f"  {'-'*35}")
for i in range(nbins):
    lo = i * bin_width
    hi = (i + 1) * bin_width
    density = bins[i] / (len(unfolded) * bin_width)
    bar = '#' * min(int(density * 30), 50)
    print(f"  [{lo:.2f}, {hi:.2f}) {bins[i]:>8} {density:>10.4f} {bar}")


# ═══════════════════════════════════════════════════════════════════════
# VI. MULTIPLICITY DISTRIBUTION
# ═══════════════════════════════════════════════════════════════════════

section("VI. CLASS MULTIPLICITY DISTRIBUTION")

print(f"\nHow many ring elements map to each eigenvalue class?")
print(f"Multiplicity = product of per-channel factors:")
print(f"  c=0: 1, 0<c<p/2: 2, c=p/2 (p=2 only): 1")

mult_dist = Counter(m for _, _, _, m in classes)
print(f"\n{'Multiplicity':<15} {'Classes':>10} {'Total elements':>15} {'Fraction':>10}")
print("-" * 55)
for m in sorted(mult_dist.keys()):
    count = mult_dist[m]
    total = m * count
    print(f"{m:<15} {count:>10} {total:>15,} {total/RAD_RING.N:>10.4f}")

# Z/2 has two classes, both multiplicity 1. Each odd p has (p-1)/2
# interior classes of multiplicity 2 and one class (c=0) of multiplicity
# 1. Max = 2^6 = 64: all six odd channels interior, whatever the 2-channel.

print(f"\nMax multiplicity = 2^6 = {2**6} (all odd primes at interior class)")
print(f"  These are the 'generic' elements, far from 0 in every channel")
print(f"Min multiplicity = 1 (at least one channel at extremal class)")

# Where the largest orbits sit: walk the sorted spectrum from the bottom.
run_64 = 0
while classes[run_64][3] == 64:
    run_64 += 1
first_break_mult = classes[run_64][3]
bottom200_min = min(m for _, _, _, m in classes[:200])
first_32 = next(i for i, c in enumerate(classes) if c[3] == 32)
print(f"\nLowest-class run of multiplicity 64: {run_64} classes, broken by "
      f"multiplicity {first_break_mult} at position {run_64 + 1}")
print(f"Bottom 200 classes: minimum multiplicity {bottom200_min} "
      f"(first multiplicity-32 class at position {first_32 + 1})")

# The mass sits low: split the eigenvalue RANGE at its midpoint.
mid_ev = (classes[0][0] + classes[-1][0]) / 2
lo_classes = sum(1 for ev, _, _, _ in classes if ev < mid_ev)
lo_elements = sum(m for ev, _, _, m in classes if ev < mid_ev)
print(f"\nBottom half of the eigenvalue range (ev < {mid_ev:.4f}):")
print(f"  {lo_classes:,} / {len(classes):,} classes  = "
      f"{lo_classes/len(classes):.1%}")
print(f"  {lo_elements:,} / {RAD_RING.N:,} elements = "
      f"{lo_elements/RAD_RING.N:.1%}")


# ═══════════════════════════════════════════════════════════════════════
# VII. EIGENVALUE MAP OF SPECIAL ELEMENTS
# ═══════════════════════════════════════════════════════════════════════

section("VII. EIGENVALUES OF SPECIAL ELEMENTS")

print(f"\n{'Element':<15} {'Value':>8} {'ev(w=1)':>10} {'ev(w=2)':>10} {'CRT':>25}")
print("-" * 72)

special = [
    ("0 (void)", 0),
    ("1 (seed)", 1),
    ("-1", RAD_RING.N - 1),
    ("2", 2),
    ("3", 3),
    ("5", 5),
    ("7", 7),
    ("11", 11),
    ("13", 13),
    ("17", 17),
    ("N/2 = 255255", RAD_RING.N // 2),
    ("210 (rung 4)", 210),
    ("2310 (rung 5)", 2310),
    ("30030 (rung 6)", 30030),
    ("137 (a prime)", 137),
    ("42", 42),
    ("240 (lambda)", 240),
]

for name, val in special:
    t = encode(val, RAD_RING)
    ev1 = sum(cos(2 * pi * r / p) for r, p in zip(t, PRIMES))
    ev2 = 2 * ev1
    print(f"{name:<15} {val:>8} {ev1:>10.4f} {ev2:>10.4f} {str(t):>25}")


# ═══════════════════════════════════════════════════════════════════════
# VIII. ZERO-CROSSING: WHERE DOES THE EIGENVALUE CHANGE SIGN?
# ═══════════════════════════════════════════════════════════════════════

section("VIII. ZERO-CROSSING ANALYSIS")

n_positive = sum(1 for ev, _, _, _ in classes if ev > 1e-10)
n_negative = sum(1 for ev, _, _, _ in classes if ev < -1e-10)
n_near_zero = len(classes) - n_positive - n_negative

# Weighted
w_positive = sum(mult for ev, _, _, mult in classes if ev > 1e-10)
w_negative = sum(mult for ev, _, _, mult in classes if ev < -1e-10)
w_zero = RAD_RING.N - w_positive - w_negative

print(f"\nClasses:  positive = {n_positive}, negative = {n_negative}, near-zero = {n_near_zero}")
print(f"Elements: positive = {w_positive:,}, negative = {w_negative:,}, near-zero = {w_zero:,}")
print(f"Positive fraction (classes): {n_positive/len(classes):.4f}")
print(f"Positive fraction (elements): {w_positive/RAD_RING.N:.4f}")

# Find eigenvalues closest to zero
near_zero = sorted(classes, key=lambda c: abs(c[0]))[:10]
print(f"\n10 eigenvalues closest to zero:")
print(f"  {'ev(w=1)':>12} {'Class':>30} {'Mult':>6}")
print(f"  {'-'*50}")
for ev, _, ct, mult in near_zero:
    print(f"  {ev:>12.8f} {str(ct):>30} {mult:>6}")


# ═══════════════════════════════════════════════════════════════════════
# IX. THE SPECTRUM IN 24 BINS
# ═══════════════════════════════════════════════════════════════════════

section("IX. THE SPECTRUM IN 24 BINS")

# Equal-width bins across the actual eigenvalue range, classes and
# elements per bin — the shape behind section VI's low-mass lean.
nbins24 = 24
bin_w = (ev_max_w1 - ev_min_w1) / nbins24
bin_classes = [0] * nbins24
bin_elements = [0] * nbins24
for ev, _, _, mult in classes:
    b = min(int((ev - ev_min_w1) / bin_w), nbins24 - 1)
    bin_classes[b] += 1
    bin_elements[b] += mult

print(f"\n  {'Bin':>21} {'Classes':>8} {'Elements':>10}")
print(f"  {'-'*42}")
for i in range(nbins24):
    lo = ev_min_w1 + i * bin_w
    hi = lo + bin_w
    bar = '#' * (bin_classes[i] // 40)
    print(f"  [{lo:>8.3f}, {hi:>8.3f}) {bin_classes[i]:>8} "
          f"{bin_elements[i]:>10,} {bar}")


# ═══════════════════════════════════════════════════════════════════════
# X. TOWER COMPARISON — SQUAREFREE AGAINST POWERED
# ═══════════════════════════════════════════════════════════════════════

section("X. EIGENVALUE LANDSCAPE COMPARISON")

def ring_eigenvalue_stats(ring, name):
    """Compute eigenvalue class statistics for a ring."""
    primes = ring.primes
    moduli = ring.moduli
    k = ring.k
    n_classes = prod(q // 2 + 1 for q in moduli)

    # Precompute cosines
    ctab = []
    for q in moduli:
        ctab.append([cos(2 * pi * c / q) for c in range(q // 2 + 1)])

    # Compute extremes and moments
    ev_max = sum(1.0 for _ in moduli)  # all cos = 1 at c=0
    ev_min = sum(ctab[i][-1] for i in range(k))

    # Compute gap: second-highest eigenvalue
    # For w=1 gap, the second class is (0,...,0,1,...,0) with the 1 in
    # the channel that has the smallest sin^2(π/q)
    gap = min(2 * sin(pi / q)**2 for q in moduli)

    return {
        'name': name,
        'k': k,
        'N': ring.N,
        'classes': n_classes,
        'ev_max': ev_max,
        'ev_min': ev_min,
        'range': ev_max - ev_min,
        'gap': gap,
        'lambda': ring.lam,
        'phi': ring.phi,
    }

rings = [(primorial_ring(k), f"k={k}") for k in (4, 5, 6, 7)] + [
    (powered_ring(k), f"k={k} powered") for k in (5, 6, 7)]

print(f"\n{'Ring':<12} {'k':>3} {'Classes':>10} {'ev_min':>10} {'ev_max':>6} "
      f"{'Gap':>10} {'Lambda':>8}")
print("-" * 72)

for ring, name in rings:
    s = ring_eigenvalue_stats(ring, name)
    print(f"{s['name']:<12} {s['k']:>3} {s['classes']:>10,} {s['ev_min']:>10.4f} "
          f"{s['ev_max']:>6.1f} {s['gap']:>10.6f} {s['lambda']:>8}")

print(f"\nSquarefree-to-powered class ratios at each rung:")
for k in (4, 5, 6, 7):
    tc = prod(q // 2 + 1 for q in primorial_ring(k).moduli)
    fc = prod(q // 2 + 1 for q in powered_ring(k).moduli)
    if tc != fc:
        print(f"  k={k}: {tc:,} squarefree vs {fc:,} powered "
              f"(ratio {Fraction(fc, tc)})")


# ═══════════════════════════════════════════════════════════════════════
# XI. EIGENVALUE SYMMETRIES
# ═══════════════════════════════════════════════════════════════════════

section("XI. EIGENVALUE SYMMETRIES")

print("\nMirror symmetry: lambda(N - n) = lambda(n).")
print("In class space: reflecting each ci -> (p-ci) mod p gives an")
print("equivalent class (since cos(2*pi*(p-c)/p) = cos(2*pi*c/p)).")
print("So the class tuple IS the mirror-folded representation.")

# More interesting: which class tuples are self-mirror?
# Self-mirror means ci = 0 for all channels (only class (0,0,...,0))
# Actually, the mirror of ci is (p-ci) mod p. The CLASS index for
# residue r is min(r, p-r). So the class IS already folded.
# The "mirror" in class space is the identity. All classes are self-mirror.
print("\nAll eigenvalue classes are already mirror-folded (class index = min(r, p-r)).")
print("Mirror pairs collapse at the class level, not within it.")

# Sign group structure: elements related by sign flips in each channel
# The sign group G = {n : n = ±1 mod p for odd p, n = 1 mod 2}
# has |G| = 2^6 = 64 (since p=2 only allows r=1).
# All 64 elements in a sign-group coset have the SAME eigenvalue class.
# So: eigenvalue classes = ring elements modulo the sign group.

sign_group_size = 2**(len(PRIMES) - 1)  # 2^6 = 64 for 6 odd primes
print(f"\nSign group size: 2^{len(PRIMES)-1} = {sign_group_size}")
print(f"Ring elements / sign group = {RAD_RING.N} / {sign_group_size}")
print(f"  But NOT equal to {total_classes} because zero channels break the factor-2 rule")

# The exact formula: total elements = sum of multiplicities over all classes
# Class (c0,...,c6) has multiplicity = product of (1 if c_i = 0, 2 if 0 < c_i < p/2, 1 if c_i = p/2)
# For Z/2: c=0 has mult 1, c=1 has mult 1
# For odd p: c=0 has mult 1, interior c has mult 2 (no p/2 case for odd p)

# Classes with every channel nonzero hold exactly the units: all
# residues nonzero mod every p_i is coprimality to N.
all_nonzero = sum(1 for _, _, ct, _ in classes if all(c > 0 for c in ct))
unit_elements = sum(m for _, _, ct, m in classes if all(c > 0 for c in ct))
print(f"\nClasses with all channels nonzero: {all_nonzero:,}")
print(f"  Elements they hold: {unit_elements:,} = phi(N) = "
      f"{RAD_RING.phi:,} -- exactly the units")
assert unit_elements == RAD_RING.phi


# ═══════════════════════════════════════════════════════════════════════
# XII. EIGENVALUE ARITHMETIC — PRODUCTS AND SUMS
# ═══════════════════════════════════════════════════════════════════════

section("XII. EIGENVALUE ARITHMETIC")

# The chord identity at weight 1: chord_sq(n) = sum 2*sin^2(pi*r/p)
# = sum (1 - cos(2*pi*r/p)) = 7 - eigenvalue(n).

# Per-channel chord contributions
print(f"\nPer-channel chord distance^2 = 1 - cos(2*pi*c/p):")
print(f"  {'p':<4} {'Classes':<8} {'Min chord²':>12} {'Max chord²':>12}")
print(f"  {'-'*40}")
for i, p in enumerate(PRIMES):
    n_cl = p // 2 + 1
    min_chord = 0  # c = 0
    max_chord = 1 - cos(2 * pi * (p // 2) / p)
    print(f"  {p:<4} {n_cl:<8} {min_chord:>12.6f} {max_chord:>12.6f}")

# What does the eigenvalue landscape look like as a lattice?
# Each class tuple is a point in a 7D grid. The eigenvalue is a function
# on this grid. What are the level sets?

# Count classes at each integer rounding of ev
int_ev_count = Counter()
for ev, _, _, _ in classes:
    int_ev_count[round(ev)] += 1

print(f"\nClasses by integer-rounded eigenvalue:")
print(f"  {'ev':>4} {'Classes':>10}")
print(f"  {'-'*16}")
for ev_int in sorted(int_ev_count.keys()):
    bar = '#' * (int_ev_count[ev_int] // 20)
    print(f"  {ev_int:>4} {int_ev_count[ev_int]:>10} {bar}")


# ═══════════════════════════════════════════════════════════════════════
# XIII. THE HALF-COUNT FUNCTION ACROSS CHANNELS
# ═══════════════════════════════════════════════════════════════════════

section("XIII. THE HALF-COUNT FUNCTION")

# d(q) = floor(q/2) + 1 counts a channel's eigenvalue classes; the total
# is its product across channels — a property, part of the fingerprint
# theorem's statement (explore_spectral_theorem.py).
d = lambda q: q // 2 + 1

print(f"\nPer-channel class count d(q) = floor(q/2) + 1:")
print(f"\n  Channel   p    d(p)   d(p) factored")
print(f"  {'-'*40}")
for p in PRIMES:
    fd = factorize(d(p))
    form = "*".join(f"{q}^{e}" if e > 1 else str(q)
                    for q, e in sorted(fd.items()))
    print(f"  Z/{p:<8} {p:<4} {d(p):<6} {form}")
print(f"\n  Total classes = product = {prod(d(p) for p in PRIMES):,}")

# Iterating d from any modulus descends to the fixed point 2.
print(f"\n  d iterated from the top three channels:")
for p in (17, 13, 11):
    chain = [p]
    while chain[-1] != 2:
        chain.append(d(chain[-1]))
    print(f"    {' -> '.join(map(str, chain))}")

print("""
An observation, recorded as a curiosity: products along d's iteration
chains meet exceptional Weyl group orders -- 8*5*3*2 = 240, 9*5*3*2 =
270, 7*4*3*2 = 168, and 240*270*168*64 = |W(E8)| with 64 = |Idem(Z/30030)|
(verify_algebra.py::test_cascade_weyl). Deflation: every exceptional
Weyl order is {2,3,5,7}-smooth because exceptional rank <= 8 keeps the
factor 11 out of |W|, so small primes are forced by rank, not by tower
structure (verify_algebra.py::test_rank_barrier).""")


# ═══════════════════════════════════════════════════════════════════════
# XIV. CUMULATIVE EIGENVALUE FUNCTION
# ═══════════════════════════════════════════════════════════════════════

section("XIV. CUMULATIVE DISTRIBUTION")

print(f"\nWhat fraction of ring elements have eigenvalue <= x?")
print(f"(Element-weighted CDF)")

# Build CDF
sorted_by_ev = sorted(classes, key=lambda c: c[0])
cumul = 0
cdf_points = []
percentiles = [0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99]
pct_idx = 0

for ev, _, _, mult in sorted_by_ev:
    cumul += mult
    frac = cumul / RAD_RING.N
    while pct_idx < len(percentiles) and frac >= percentiles[pct_idx]:
        cdf_points.append((percentiles[pct_idx], ev))
        pct_idx += 1

print(f"  {'Percentile':>12} {'ev(w=1)':>12}")
print(f"  {'-'*26}")
for pct, ev in cdf_points:
    print(f"  {pct:>12.0%} {ev:>12.6f}")

# Median eigenvalue
median_ev = cdf_points[4][1] if len(cdf_points) > 4 else 0
mode_cl = max(int_ev_count.items(), key=lambda kv: kv[1])
elem_ev_count = Counter()
for ev, _, _, mult in classes:
    elem_ev_count[round(ev)] += mult
mode_el = max(elem_ev_count.items(), key=lambda kv: kv[1])
print(f"\n  Median eigenvalue: {median_ev:.6f}")
print(f"  Mean eigenvalue:   {mean_w1:.6f}")
print(f"  Modal integer-rounded ev: {mode_cl[0]} over classes "
      f"({mode_cl[1]:,} classes), {mode_el[0]} over elements "
      f"({mode_el[1]:,} elements)")


# ═══════════════════════════════════════════════════════════════════════
# XV. KEY FINDINGS
# ═══════════════════════════════════════════════════════════════════════

section("XV. KEY FINDINGS")

print(f"""
1. HALF-COUNT FACTORIZATION (property). Per-channel class count d(p)
   = floor(p/2)+1; total = 2*2*3*4*6*7*9 = 18,144 = 2^5*3^4*7 — part of
   the fingerprint theorem's statement. Products along d's iteration
   chains meeting exceptional Weyl orders (240*270*168*64 = |W(E8)|) is
   an observation recorded as a curiosity, deflated by the rank barrier:
   exceptional Weyl orders are {{2,3,5,7}}-smooth because rank <= 8 keeps
   the factor 11 out, not because of tower structure.

2. SQUAREFREE VARIANCE FORMULA. Var = (k+1)/2, NOT k/2. The 2-channel
   contributes variance 1 (only {+1,-1}), other channels contribute 1/2.
   At rung 7: Var = 4 = (7+1)/2. Powered (all q >= 3): Var = k/2 = 3.5.

3. SQUAREFREE SKEWNESS = 1/32. Source: the 3-channel ALONE. In GF(3), the
   mean of cos^3(2*pi*r/3) = 1/4 — the only prime where this is nonzero.
   m3 = 1/4, skewness = (1/4)/4^(3/2) = 1/32. Powered (Z/9): zero. The
   3-channel creates an asymmetry that raising the exponent eliminates.

4. SPECTRAL GAP = {sf_gap:.6f} = 2*sin^2(pi/17), controlled by the
   largest prime. {sf_gap/pw_gap:.1f}x wider than the powered ring,
   where 7^2 = 49 controls it. Wider gap = elements more distinguishable.

5. ALL 18,144 EIGENVALUES DISTINCT. Spectral fingerprint confirmed.

6. SQUAREFREE/POWERED CLASS RATIO = 48/8125, CONSTANT across every rung.
   Raising exponents multiplies the class count by d(p^e)/d(p) per channel.

7. MULTIPLICITY STRUCTURE. Max = 64 = 2^6 (all odd channels at interior
   class), min = 1. The 60 lowest classes all carry multiplicity 64; the
   run breaks at position 61 with a class of multiplicity 32. The mass
   sits low: the bottom half of the eigenvalue range holds 43.9% of the
   classes but 58.4% of the elements (7,958 / 18,144 and
   298,376 / 510,510).
""")

print("=" * 72)
print("  Done. 18,144 eigenvalue classes computed and analyzed.")
print("=" * 72)
