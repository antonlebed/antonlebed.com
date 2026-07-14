"""IRREDUCIBILITY AS ORDER PARAMETER — the depth column's critical clock.

VERTIGO STOCK (a), P165. The witness gap H(history | endpoint) is how much of
a growth trajectory is UNRECOVERABLE from its endpoint: computational
irreducibility (Wolfram's informal central thesis) made EXACT and DECIDABLE,
because the growth-world route posteriors are closed-form (route-weight
cancellation, OBSERVER.md). The established chambers noted route amnesia
peaks inside the temperature range (breadth: finite beta, chamber six; depth: at
the condensation clock beta_col, depth-observer). A peak is not an order
parameter. This script asks whether
the peak is a genuine PHASE TRANSITION (a non-analyticity in the depth->infinity
limit) at a named ARITHMETIC clock, and classifies it.

THE OBJECT. The depth column seed 1 -> 3^t (explore_depth_observer.py): the
genesis posterior is a product of independent level-visit coins
p_a = 1/(1+Z_a(beta)), Z_a = zeta(beta) - 1 - T_col(a,beta), T_col the transparent
divisor sum (base 1+2^-b+4^-b+8^-b times the sparse column primes 2*3^j+1).
Route entropy (the witness gap) H(beta,t) = sum_{a=1}^{t-1} h(p_a), h = binary
entropy. Stage clocks beta_a = root of Z_a=1 (where p_a=1/2) condense at
beta_col = root of Z_col=1, Z_col = lim_a Z_a.

FINDINGS (tiers stated per section; run record at bottom).

S1 THE RATE IS A CROSSOVER (intensive irreducibility, analytic). The route-
entropy RATE r(beta) = lim_t H(beta,t)/t = h(1/(1+Z_col(beta))) (Cesaro: the
tail coin dominates the average, Z_a -> Z_col). It is ANALYTIC in beta>1 (Z_col a
Dirichlet series, h smooth at 1/2), rises to its maximum log 2 at beta_col with
r'(beta_col)=0 and FINITE, CONTINUOUS curvature. The per-move irreducibility has
no critical point: it is a smooth crossover. (observation; closed form + Cesaro
convergence verified.)

S2 THE CORRELATION LENGTH DIVERGES (the order parameter). The genesis mode is
the deep SUFFIX {a : Z_a(beta)<1} (Z_a falls in a toward Z_col<1); its ONSET
DEPTH a*(beta) = the shallowest struck level = how deep the world's origin stays
uncertain (a correlation-length analog) DIVERGES as beta->beta_col+. The law is
exact: the clock gap beta_a - beta_col is governed by the next unincluded column
prime, gap ~ q_next^-beta_col (each new column prime q~2*3^j contributes
q^-beta_col to the gap; the clocks beta_a are a STAIRCASE falling to beta_col,
plateaus where 2*3^j+1 is composite). Measured on the clock gap directly
(float-safe past the ~1e-9 naive-subtraction wall): ln(gap) vs ln(q_next) slope
-beta_col to R^2=0.99997. The reciprocal reading a*(beta) ~
ln(1/(beta-beta_col))/(beta_col*ln3) is a LOGARITHMIC divergence whose
constant is EXACT at the staircase's risers (riser fit 0.6084 vs the law
1/(beta_col*ln3) = 0.6085, R^2 0.99995; the blind-grid fit 0.535 is pure
staircase geometry and never converges — the closure:
explore_astar_slope.py). (observation; slopes measured against the hand law.)

S3 A GEOMETRIC TRANSITION, THERMODYNAMICALLY INVISIBLE, AND WHERE THE CLOCK
COMES FROM. r(beta) is a composition of analytic functions (h at 1/2, Z_col a
uniformly convergent Dirichlet product over the sparse column primes), so the
intensive entropy is ANALYTIC through beta_col -- no free-energy singularity, no
thermodynamic transition. What marks beta_col is the genesis MODE, not the
entropy: the asymptotic deep-tail occupation m(beta) = 1{Z_col(beta)<1} JUMPS
0->1 there (Z_col crosses 1 monotone), and the mode's onset depth a* diverges
logarithmically. A geometric (mode) transition driven by CLOCK CONDENSATION (the
stage clocks accumulating at beta_col) -- the critical clock lives in the genesis
geometry and is invisible to the intensive irreducibility. (Not infinite-order:
that needs a C-infinity-but-non-analytic free energy; here the free energy is
analytic and the length diverges only logarithmically.)
THE STRUCTURAL LAW: an interior irreducibility critical point exists iff the
fate's normalizer has a NONZERO infinite-depth limit. DEPTH keeps ONE window to
infinite depth, so Z_col = lim Z_a is order 1 -> interior root beta_col. BREADTH
adds every window, so Z_{p_k#} = zeta*prod_p(1-p^-b)-1 -> zeta*(1/zeta)-1 = 0 ->
its clocks are pushed to the zeta POLE beta=1, no interior transition. The
irreducibility phase transition sits exactly where the tower RE-IMPORTS a place
(depth = the ultrametric |.|_q returning; breadth = the amnesiac CRT deleting
all). (observation + the Euler-product limit is exact.)

Run: `python explore_irreducibility_order.py`. Predictions frozen in SCRATCH.md
(P165) BEFORE the run; asserts adjudicate; printed values read against the hand
law. RUN RECORD (63 checks pass, ~5 s): beta_col = 1.49595 (interior root of
Z_col=1); r(beta_col) = 0.69315 = log2 (max), r' = 1.8e-10, r'' = -2.598 finite;
Cesaro H/t -> r verified (beta = 1.35, 1.6, 2.0, t to 2e4). S2: 9 column primes
[7, 19, 163, 487, 1459, 39367, 86093443, 258280327, 411782264189299], bisection
of the clock resolvable to 5 then the naive-subtraction float wall (gaps < 1e-9);
ln(gap) vs ln(q_next) slope -1.4990 (pred -beta_col = -1.4959), R^2 = 0.99997;
a*(beta) vs ln(1/(beta-beta_col)) slope 0.535 (the law 1/(beta_col*ln3) =
0.6085 lives at the staircase's risers; the blind-grid 0.535 is exact
staircase geometry — explore_astar_slope.py), logarithmic. S3:
Z_col(beta_col) = 1.0000 (interior); breadth Z(primes<=1e4) at beta = 1.5, 2, 3
= 0.00182, 0.00001, 0.00000 -> 0 (Euler product); breadth clocks k = 1..5 =
1.3778, 1.2478, 1.1966, 1.1673, 1.1518, falling to the pole. Prediction miss
adjudicated by asserts: the order parameter is the threshold DEPTH a* (the mode
is a deep suffix {a: Z_a<1}), NOT a count from level 1 (SCRATCH P2 had the
activation direction inverted; the assert caught the sign, -3.18 vs +0.61).
"""

import sys, os, math
from math import log

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_depth_observer import (  # lineage: the established column machinery
    is_prime, column_primes, T_col, z_col_level, zeta_bracket, PRIMES_1E6,
)
from explore_observer_view import z_state as breadth_z  # breadth normalizer

CHECKS = 0

def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1

# ---------------------------------------------------------------- zeta (hp)
# Euler-Maclaurin tail: tighter than the bracket midpoint, needed to locate
# beta_col and measure slopes. Error O(M^{-beta-3}); cross-checked into the
# sibling's bracket in S1.

_ZHP = {}

def zeta_hp(beta, M=20000):
    if beta not in _ZHP:
        s = sum(n ** -beta for n in range(1, M + 1))
        tail = (M ** (1 - beta) / (beta - 1)
                - 0.5 * M ** -beta
                + beta / 12.0 * M ** (-beta - 1))
        _ZHP[beta] = s + tail
    return _ZHP[beta]

# Column primes 2*3^j+1 capped at JMAX: beyond j~45 a term p^-beta < 1e-25
# (below float noise) AND 2*3^45 < 3.3e24 keeps is_prime deterministic. This
# both bounds cost (never builds a bignum) and keeps T_col exact to float.
JMAX = 45
_CP, _TC = {}, {}

def col_primes_capped(a):
    hi = min(a - 1, JMAX)
    if hi not in _CP:
        _CP[hi] = [2 * 3 ** j + 1 for j in range(1, hi + 1)
                   if is_prime(2 * 3 ** j + 1)]
    return _CP[hi]

def T_col_local(a, beta):
    hi = min(a - 1, JMAX)
    key = (hi, beta)
    if key not in _TC:
        t = 1 + 2.0 ** -beta + 4.0 ** -beta + 8.0 ** -beta
        for p in col_primes_capped(a):
            t *= 1 + p ** -beta
        _TC[key] = t - 1
    return _TC[key]

def Z_level(a, beta):
    return zeta_hp(beta) - 1 - T_col_local(a, beta)

def Z_col(beta):
    return Z_level(JMAX + 5, beta)  # converged: all column primes j<=JMAX in

def binary_entropy(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -(p * log(p) + (1 - p) * log(1 - p))

def rate(beta):
    """r(beta) = h(1/(1+Z_col)) — the route-entropy per move (nats)."""
    return binary_entropy(1.0 / (1.0 + Z_col(beta)))

def bisect_root(f, lo, hi, tol=1e-13):
    """Root of f (f decreasing on [lo,hi]: f(lo)>0>f(hi))."""
    flo, fhi = f(lo), f(hi)
    assert flo > 0 > fhi, f"bracket not straddling: f({lo})={flo}, f({hi})={fhi}"
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
        if hi - lo < tol:
            break
    return 0.5 * (lo + hi)

BETA_COL = bisect_root(lambda b: Z_col(b) - 1.0, 1.30, 1.60)
ZCOL_PRIME = (Z_col(BETA_COL + 1e-6) - Z_col(BETA_COL - 1e-6)) / 2e-6  # < 0

# ---------------------------------------------------------------- S1 the rate

def s1():
    print("S1 the rate is a crossover (intensive irreducibility, analytic)")
    # cross-check high-precision Z_col into the sibling's established bracket
    # (sibling T_col(90): includes column primes to j=89, agreeing with the
    # JMAX=45 cap to ~1e-25 — the extra primes are below float noise)
    for beta in (1.3, BETA_COL, 1.8, 2.5):
        zlo, zhi = zeta_bracket(beta)
        blo = zlo - 1 - T_col(90, beta)
        bhi = zhi - 1 - T_col(90, beta)
        ok(blo - 1e-9 <= Z_col(beta) <= bhi + 1e-9,
           f"S1 Z_col outside sibling bracket at beta={beta}")
    # beta_col is a genuine interior root, and h peaks there (p=1/2 exactly)
    ok(abs(Z_col(BETA_COL) - 1.0) < 1e-9, "S1 beta_col not a root of Z_col=1")
    ok(1.30 < BETA_COL < 1.60, "S1 beta_col not interior")
    ok(abs(rate(BETA_COL) - log(2.0)) < 1e-7,
       f"S1 rate at beta_col != log2: {rate(BETA_COL)}")
    # r'(beta_col) = 0 (h'(1/2)=0), r is maximal there
    hd = 1e-5
    dr = (rate(BETA_COL + hd) - rate(BETA_COL - hd)) / (2 * hd)
    ok(abs(dr) < 1e-3, f"S1 r'(beta_col) not ~0: {dr}")
    for b in (BETA_COL - 0.15, BETA_COL + 0.15):
        ok(rate(b) < rate(BETA_COL), f"S1 rate not maximal at beta_col vs {b}")
    # curvature FINITE and CONTINUOUS through beta_col: r is analytic (h at 1/2
    # composed with the convergent Dirichlet product Z_col) -- no singularity
    h = 1e-4
    def curv(b):
        return (rate(b + h) - 2 * rate(b) + rate(b - h)) / (h * h)
    c_at = curv(BETA_COL)
    c_lo, c_hi = curv(BETA_COL - 0.02), curv(BETA_COL + 0.02)
    ok(math.isfinite(c_at) and c_at < 0, "S1 curvature not finite<0 at beta_col")
    ok(abs(c_lo - c_at) < 0.6 and abs(c_hi - c_at) < 0.6,
       f"S1 curvature discontinuous: {c_lo:.4f} {c_at:.4f} {c_hi:.4f}")
    # Cesaro: H(beta,t)/t -> r(beta) as t grows
    for beta in (1.35, 1.6, 2.0):
        r = rate(beta)
        prev = None
        for t in (200, 2000, 20000):
            H = sum(binary_entropy(1.0 / (1.0 + Z_level(a, beta)))
                    for a in range(1, t))
            gap = abs(H / (t - 1) - r)
            if prev is not None:
                ok(gap < prev, f"S1 Cesaro not converging beta={beta} t={t}")
            prev = gap
        ok(gap < 1e-3, f"S1 Cesaro not within 1e-3 at beta={beta}: {gap}")
    print(f"  beta_col = {BETA_COL:.5f} (interior root of Z_col=1); "
          f"r(beta_col) = {rate(BETA_COL):.5f} = log2 (max), r' = {dr:.2e}, "
          f"r'' = {c_at:.3f} finite; Cesaro H/t -> r verified")

# ---------------------------------------------------------------- S2 length

def linfit(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) \
        / sum((x - mx) ** 2 for x in xs)
    ss_res = sum((y - (my + slope * (x - mx))) ** 2 for x, y in zip(xs, ys))
    ss_tot = sum((y - my) ** 2 for y in ys)
    return slope, 1 - ss_res / ss_tot

def col_primes_full():
    """(j, q) with q = 2*3^j+1 prime, j <= 30 (all < 3.3e24: is_prime exact)."""
    return [(j, 2 * 3 ** j + 1) for j in range(1, 31) if is_prime(2 * 3 ** j + 1)]

def delta_gap(j_n, col, beta):
    """The clock gap beta_a - beta_col at the level a = j_n+1, computed
    FLOAT-SAFE. beta_a solves Z_col(beta)-1 + delta = 0 where delta =
    T_col(inf) - T_col(a) = the missing column primes' contribution (a small
    positive number). Naively beta_a and beta_col are each ~1.496 and their
    difference walls below ~1e-10; here delta is built directly with expm1/log1p
    (no cancellation) and linearized through Z_col'. Extends the law to any
    depth. Returns (gap, delta)."""
    base = 1 + 2.0 ** -beta + 4.0 ** -beta + 8.0 ** -beta
    upto = 1.0
    for j, q in col:
        if j <= j_n:
            upto *= 1 + q ** -beta
    # prod_{j>j_n}(1+q^-b) - 1, float-safe:
    rem = math.expm1(sum(math.log1p(q ** -beta) for j, q in col if j > j_n))
    delta = base * upto * rem
    return delta / (-ZCOL_PRIME), delta

def s2():
    print("S2 the correlation length diverges (the order parameter)")
    col = col_primes_full()
    ok(len(col) >= 6, "S2 too few column primes for a slope")
    # cross-check the float-safe delta gap against DIRECT bisection where the
    # latter is still resolvable (gap > 1e-9): the naive subtraction wall.
    resolvable = 0
    for j, q in col:
        gap_delta, _ = delta_gap(j, col, BETA_COL)
        if gap_delta > 1e-9:
            beta_a = bisect_root(lambda b: Z_level(j + 1, b) - 1.0, 1.30, 1.60)
            gap_bis = beta_a - BETA_COL
            ok(abs(gap_bis - gap_delta) < 0.02 * gap_delta + 1e-12,
               f"S2 delta gap != bisection at j={j}: {gap_delta} vs {gap_bis}")
            resolvable += 1
    ok(resolvable >= 5, "S2 too few resolvable clocks to validate delta")
    # the gap at level a=j_n+1 is governed by the NEXT missing column prime
    # q_{n+1}: ln(gap) linear in ln(q_next) at slope -beta_col, to any depth.
    gaps = [delta_gap(j, col, BETA_COL)[0] for j, q in col]
    for g0, g1 in zip(gaps, gaps[1:]):
        ok(g1 < g0, "S2 clock gap not strictly shrinking (delta)")
    xs = [log(col[n + 1][1]) for n in range(len(col) - 1)]  # ln(q_next)
    ys = [log(gaps[n]) for n in range(len(col) - 1)]
    slope, r2 = linfit(xs, ys)
    pred = -BETA_COL
    ok(abs(slope - pred) < 0.08, f"S2 gap slope {slope:.4f} vs pred {pred:.4f}")
    ok(r2 > 0.97, f"S2 ln-linear fit poor, R^2={r2:.4f}")
    # The genesis mode is a THRESHOLD SUFFIX {a : Z_a<1} = the deep levels
    # (Z_a falls in a toward Z_col<1). The order parameter is the threshold
    # DEPTH a*(beta) = shallowest struck level = the depth to which the origin
    # stays uncertain — a correlation length. It DIVERGES as beta->beta_col+,
    # logarithmically, envelope slope 1/(beta_col*ln3) (reciprocal of the clock
    # slope; a staircase, measured looser than the clean gap fit).
    def a_star(beta):
        a = 1
        while a <= JMAX + 5 and Z_level(a, beta) >= 1.0:
            a += 1
        return a
    pred_slope = 1.0 / (BETA_COL * log(3.0))
    xs2 = [k * log(3.0) for k in range(2, 15)]  # ln(1/eps), eps = 3^-k
    ys2 = [a_star(BETA_COL + 3.0 ** -k) for k in range(2, 15)]
    slope2, _ = linfit(xs2, ys2)
    ok(abs(slope2 - pred_slope) < 0.15,
       f"S2 a* slope {slope2:.4f} vs pred {pred_slope:.4f}")
    print(f"  {len(col)} column primes {[q for _, q in col]}"
          f" (bisection resolvable to {resolvable}, then the float wall);")
    print(f"  ln(gap) vs ln(q_next): slope {slope:.4f} "
          f"(pred -beta_col = {pred:.4f}), R^2={r2:.5f};")
    print(f"  a*(beta) vs ln(1/(beta-beta_col)): slope {slope2:.4f} "
          f"(pred 1/(beta_col*ln3) = {pred_slope:.4f}) — logarithmic divergence")

# ---------------------------------------------------------------- S3 class

def s3():
    print("S3 a geometric transition (thermodynamically invisible), the clock")
    # geometric, not thermodynamic: intensive rate analytic (S1) while the mode
    # onset length diverges (S2, logarithmically) and the tail occupation jumps
    # (below). The critical clock is invisible to the entropy.
    # THE STRUCTURAL LAW: interior critical point <=> nonzero infinite-depth
    # normalizer limit. Depth: Z_col order 1 (=1 at beta_col). Breadth: the
    # Euler product kills it.
    ok(abs(Z_col(BETA_COL) - 1.0) < 1e-9, "S3 depth limit not order 1")
    # the order parameter m(beta) = 1{Z_col<1} = asymptotic deep-tail occupation
    # JUMPS 0->1 at beta_col (Z_col crosses 1 monotone) while the intensive rate
    # stays analytic: a geometric transition invisible to the entropy.
    ok(Z_col(BETA_COL - 0.01) > 1.0 > Z_col(BETA_COL + 0.01),
       "S3 tail-occupation order parameter does not jump at beta_col")
    # breadth normalizer Z_{p_k#} -> 0 as k grows (zeta * 1/zeta - 1)
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for beta in (1.2, 1.5, 2.0):
        seq = []
        for k in (1, 3, 6, 10, 15):
            seq.append(breadth_z(primes[:k], beta))
        for x, y in zip(seq, seq[1:]):
            ok(y < x, f"S3 breadth Z not decreasing in k at beta={beta}")
        ok(seq[-1] < 0.5 * seq[0], f"S3 breadth Z not collapsing at beta={beta}")
    # breadth clocks (roots of Z_{p_k#}=1) fall toward the zeta pole beta=1,
    # not to an interior accumulation point: for large k there is NO root>1.
    breadth_clocks = []
    for k in (1, 2, 3, 4, 5):
        f = lambda b: breadth_z(primes[:k], b) - 1.0
        if f(1.05) > 0 > f(1.60):
            breadth_clocks.append((k, bisect_root(f, 1.05, 1.60)))
    for (k0, c0), (k1, c1) in zip(breadth_clocks, breadth_clocks[1:]):
        ok(c1 < c0, f"S3 breadth clock not falling at k={k1}")
    # THE EULER-PRODUCT LIMIT: for every fixed interior beta, Z_{p_k#} -> 0
    # (zeta * prod_all(1-p^-b) = 1 exactly), so the breadth clocks accumulate
    # only at the pole beta=1 -- no interior transition. Evidence: primes to
    # 1e4 already drive Z essentially to 0 at beta >= 1.5.
    primes_1e4 = [p for p in PRIMES_1E6 if p <= 10000]
    for beta in (1.5, 2.0, 3.0):
        z_far = breadth_z(primes_1e4, beta)
        ok(abs(z_far) < 0.02, f"S3 breadth Z not -> 0 at beta={beta}: {z_far}")
    print(f"  depth limit Z_col(beta_col) = {Z_col(BETA_COL):.4f} (=1, interior);")
    print(f"  breadth Z(primes<=1e4) at beta=1.5,2,3: "
          + ", ".join(f"{breadth_z(primes_1e4, b):.5f}" for b in (1.5, 2.0, 3.0))
          + " -> 0 (Euler product); accumulation only at the pole;")
    print(f"  breadth Z_(p_k#) at beta=1.5, k=1,3,6,10,15: "
          + ", ".join(f"{breadth_z(primes[:k], 1.5):.4f}"
                      for k in (1, 3, 6, 10, 15)))
    print(f"  breadth clocks (roots >1): "
          + ", ".join(f"k={k}:{c:.4f}" for k, c in breadth_clocks)
          + " -> falling to the zeta pole; no interior transition")

def main():
    s1()
    s2()
    s3()
    print(f"\nALL SECTIONS PASS ({CHECKS} checks)")

if __name__ == "__main__":
    main()
