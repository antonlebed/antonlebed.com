"""
The staircase reduction: the strong staircase lemma becomes a
max-coverage bound, the caps are proved on the
closed region, and the lattice-count closure proves
them at EVERY (m, D, B) -- the lemma is a rule with complete
coverage, and twin 2's exclusion holds at every two-prime d.

CONTEXT. Twin 2's residual (explore_cover_exclusion.py):
THE STRONG STAIRCASE LEMMA -- lay intervals A_u = [-Bu, -Bu+u]
(u = 0..D, B a unit) on Z/m, f(c) = covering multiplicity; claim
#{c : f(c) >= D+1-s} <= s+1 for every s < (D+1)/2. This reduces the
lemma to the caps (R3), proves them on the closed region
(R7-R11), and closes the rest (R12-R14): analytic for m >= 213,
exhaustive below. m prime throughout (the pair application needs
nothing else; R7/R8 hold for any m with B, B-1 units).

THE FINDINGS (derived by hand, checked computationally, fixed here
as the permanent record):

 R1 (rule, proved -- THE UNCONDITIONAL WEAK STAIRCASE). The weak
    bound #deep(s) <= 2s+1 holds for ALL s < (D+1)/2 with NO zone
    condition, and for intervals of sizes 1..D+1 at ARBITRARY
    positions (an earlier clustering proof was also position-free but
    needed the zone 8s <= m).
    Proof (pure counting): an interval of size u+1 covers at most
    min(k, u+1) of any k cells, so k deep cells receive coverage
    k(D+1-s) <= sum_u min(k, u+1) = k(k-1)/2 + k(D+2-k) (for
    k <= D+1), giving k <= 2s+1; k >= D+2 is killed by total mass
    (D+1)(D+2)/2 < k(D+1-s) when s < (D+1)/2. This retro-explains
    the prior tally: all 348,488 weak excesses sat at or beyond
    half-range because below it the bound is a theorem everywhere.

 R2 (criterion, proved -- THE ANHARMONIC INVOLUTION). For a good
    time u, z_u = (c+Bu) mod m and h_u = u - z_u satisfy
    h_u == ((1-B)u - c) mod m, so the good sets obey
    G_B(c) = G_{1-B}(-c) exactly: f_B(c) = f_{1-B}(-c). B and 1-B
    are interchangeable everywhere; both are units iff B != 0, 1.
    (The companion map B -> B^{-1} swaps the diagonal side --
    an earlier observation fmax_B = fmax_{B^{-1}}, PROVED pointwise
    by time reversal, R9. Orbit of 2 under the S3 cross-ratio
    action: {2, 1/2, -1} = the extremal multipliers.)

 R3 (rule, proved -- THE STAIRCASE REDUCTION). For m prime and
    B != 1, the strong staircase lemma at (m, D, B) FOLLOWS FROM
      (i)  MAX-COVERAGE CAP: f(c) <= floor(D/2)+1 for every c, and
      (ii) MAXIMIZER CAP (D even only): #{c : f = D/2+1} <= D/2+1;
    and given (i), (ii) is exactly what remains of the lemma (the
    only reachable deep threshold). One-directional: the lemma does
    NOT imply (i) -- it tolerates up to s+1 cells above the cap.
    Derivation: s < (D+1)/2 makes the deep threshold D+1-s exceed
    floor(D/2)+1 for D odd (no deep cells at all) and equal it
    exactly at s = D/2 for D even (deep cells = the maximizers).
    B = 1 is exact by inspection: f(c) = D+1-c on [0, D], deep(s)
    = {0..s}, equality s+1 at every s. So the two caps carry the
    whole lemma -- statements about one modular staircase's
    maximum, with no quantifier over s left.

 R4 (rule, proved on its stated scope -- THE ONE-LINE REGIME).
    Lattice picture: f(c) = #{(u,p) in Z^2 : 0 <= u <= D,
    (B-1)u + c <= pm <= Bu + c}, a thin triangle with apex
    (0, c/m), slopes (B-1)/m and B/m, area D^2/(2m). Let B* =
    min(B, m+1-B), the smaller of the involution pair {B, 1-B} as
    integers -- B* >= 2 for every B in [2, m-1]. If B*D < m the
    triangle spans at most the lines p = 0 (which holds only u = 0,
    c = 0) and p = 1, and the p = 1 count is #integers in
    [X/B*, min(D, X/(B*-1))] with X = m-c, maximized at
    X = (B*-1)D: F <= floor(D/B*) + 1 <= floor(D/2) + 1. The
    maximizer cap too: B* >= 3 leaves the maximizer set EMPTY
    (floor(D/3)+1 < D/2+1 for D >= 3), and B* = 2 reaches
    f = D/2+1 only at X = D (X = D+1 already drops to D/2: the
    count is floor(X/2)+1 for X <= D, D - ceil(X/2) + 1 above) --
    a SINGLE maximizer. So
    both caps (and hence the lemma) are PROVED whenever B*D < m;
    the B = 2 extremal (G = [D/2, D] at c = -D) achieves equality.

 R5 (pattern, swept here -- THE CAPS IN GENERAL). Max-coverage cap
    and maximizer cap verified for every prime m <= 61, every
    D in [3, m-2], every B in [2, m-1] (both caps + the full
    reduction end-to-end), and caps-only to every prime m <= 103
    (a follow-up extension, kept as a check); maximizer count
    <= max(1, D/2 - 1) everywhere swept -- slack 2 under
    need, stable as m doubles. The wrapped regime B*D >= m,
    the open residual, is CLOSED: R7-R11 give the arithmetic
    closed region, R12-R14 everything else.

 R6 (pattern, swept -- THE TRUE GENERALITY). The s+1 bound needs
    neither the AP structure nor primality: interval systems of
    sizes 1..D+1 with all left ends distinct AND all right ends
    distinct satisfy #deep(s) <= s+1 in half-range across ~20k
    random systems swept below (m <= 41, D up to m-2, two thirds
    cluster-biased toward the near-tight packed shape).
    One-sided distinctness FAILS (witness asserted below); fully
    arbitrary positions fail even harder (an earlier probe). The AP
    family with B != 0, 1 has both ends distinct (steps B, B-1
    both units) -- the lemma's mechanism is END-DISTINCTNESS, with
    B = 1 (repeated lefts, the nested extremal) the one AP case
    that leans on its own exact count instead. BUT the COVERAGE
    CAP does NOT follow from end-distinctness (guard confirmed, witness
    asserted in S7): on Z/40 at D = 5 a both-distinct system
    covers one cell 4 > floor(D/2)+1 = 3 times -- the cap is
    genuinely arithmetic (R7-R11), only the deep-count bound is
    combinatorial. Don't hunt a combinatorial cap proof.

 R7 (rule, proved -- EQUICOVERAGE). For ANY m and any B with B and
    B-1 both units, the full system D = m-2 covers EVERY cell
    exactly (m-1)/2 times. Proof (telescope): f(c+1) - f(c) =
    #{u <= m-2 : -Bu = c+1} - #{u <= m-2 : (1-B)u = c}; each
    congruence has one solution u in Z/m, counted unless u = m-1,
    and BOTH exceptions occur at the same c = B-1 -- the difference
    vanishes at every c, so f = mean = (m-1)/2. Corollary: the
    strong staircase lemma at D = m-2 holds with ZERO deep cells
    (threshold m-1-s > (m-1)/2 in half-range) -- the m = q side
    (D = q-2 = m-2) of EVERY pair is proved outright.

 R8 (rule, proved -- THE COMPLEMENTATION DUALITY). For D < m-2
    (same unit conditions),
      f^B_D(c) = f^{1-B}_{m-3-D}(c - 2B + 1) + D + (3-m)/2.
    Proof: equicoverage minus the tail u in [D+1, m-2]; a tail
    interval's complement is an interval, and reindexed by
    w = m-2-u the tail-complements are EXACTLY the (1-B)-staircase
    of degree D~ = m-3-D shifted by 2B-1. The involution squares
    to the identity. Cap transfer is EXACT at both parities
    (algebra: (m-1)/2 - ceil(D/2) = floor(D~/2) + 1), and equality
    cases (maximizers) biject: every cap statement needs proving
    only for min(D, D~) <= (m-3)/2.

 R9 (rule, proved -- TIME REVERSAL). The triangle reflection
    (u, v) -> (D-v, D-u) maps the lattice picture to itself and
    proves f^B_D(c) = f^{B^-1}_D(D - B^{-1}D + B^{-1}c): R2's
    fmax_B = fmax_{B^-1} observation upgrades to a pointwise rule.
    With R2 this generates the full S3 cross-ratio action
    {B, 1-B, 1/B, 1-1/B, 1/(1-B), B/(B-1)}: both caps are
    invariant along the orbit at fixed D, and via R8 also across
    D <-> D~.

R10 (rule, proved -- THE PRODUCT BOUND). WLOG b = B* <= (m+1)/2
    (R2). A good time's wrap count p satisfies
    pm in [c+(b-1)u, c+bu]. (i) p is NONDECREASING along good
    times (p dropping forces m <= u <= D), and the r distinct
    values satisfy (r-1)m <= bD: r <= floor(bD/m)+1. (ii) at fixed
    p the good times lie in [X/b, min(D, X/(b-1))], X = pm-c --
    at most floor(D/b)+1 of them (R4's count, valid on every
    line). So fmax <= (floor(bD/m)+1)(floor(D/b)+1). R4's
    one-line regime is the r = 1 case; the SPARSE regime
    b in [D+1, (m-1)/2] is the L = 1 case, where moreover
    floor(bD/m) <= D/2 - 1 at even D: NO cell reaches D/2+1 and
    the maximizer cap is vacuous-true. Verified exact below:
    every prime m <= 103, every D, every b, both involution
    representatives -- zero violations (S12).

R11 (rule + pattern -- THE CLOSED REGION). Both caps are PROVED at
    (m, D, B) whenever SOME cross-ratio orbit element x (R9),
    tested at D or at D~ (R8), has b = B*(x) with either
    b·D' < m (one-line R4) or product bound <= floor(D'/2)+1
    (R10; for the even-D maximizer cap: product <= D'/2, or the
    one-line / sparse cases, which prove it directly). Clean
    corollary (rule, proved): min(D, D~)^2 < m implies BOTH CAPS
    for ALL B -- b <= D' is one-line (bD' <= D'^2 < m), b >= D'+1
    is sparse, and the top edge b in {(m-1)/2, (m+1)/2} has 2, -2
    or 3 in its orbit (B = +-2^{-1}-shaped), rescued one-line.
    Numerically the all-B threshold reaches min(D, D~) ~ m/4
    (computed: floor(m/4) or floor(m/4)-1 at m = 101, 199, 307,
    401, 503, 1009, 2003 -- tier: pattern); each arithmetic-test
    pass IS a proof at its instance, and the test survives as the
    cheap first pass in sweeps. Its residual (the mid-band
    min(D, D~)/m in (1/4, 1/2] with the whole orbit in the gap
    window) is closed by R12-R14 below.

R12 (rule, proved -- THE LATTICE COUNTING LEMMAS). The frame:
    f(c) = #((L_B + (0, c)) cap T_D) EXACTLY, where L_B =
    {(u, v) in Z^2 : v == Bu (mod m)} (index m, det m) and
    T_D = {0 <= v <= u <= D} (asserted S17). Four lemmas:
    (A) UNIMODAL SUM: phi >= 0 unimodal, sample points spaced h:
        sum phi(y_i) <= (1/h) int phi + max phi (rising terms
        bounded by right-neighbor integrals, falling by left,
        peak by max; intervals disjoint).
    (B) GENERIC COUNT: g = shortest vector of L_B, lam = |g|
        (Euclidean; g is primitive -- a proper divisor k < 7 < m
        of g is coprime to m, so g/k would be a shorter lattice
        vector; for m > 49 the sub-7 direction is UNIQUE, two
        independent ones force det < 49 < m). Lattice points lie
        on lines parallel to g spaced h = m/lam with on-line
        spacing exactly lam; chord length of a convex set along
        parallel lines is concave (Brunn), so (A) applies:
        f <= D^2/2m + sqrt2 D/lam + sqrt2 lam D/m + 1
        (area D^2/2, chord_max <= diam = sqrt2 D, width <=
        sqrt2 D). Asserted S18.
    (C) RUN BOUND: n consecutive steps of primitive g = (t, s),
        t >= 1, staying inside T_D satisfy (n-1) r_g <= D where
        r_g = s (s > t), t (0 < s < t), t+|s| (s < 0): add the
        binding constraints (n-1)t <= D - u0 and (n-1)(s-t) <=
        u0 - v0 (resp. (n-1)|s| <= v0 <= u0). Per-line count
        <= floor(D/r_g) + 1. Asserted S19.
    (D) RESONANT COUNT: if L_B has a primitive vector g with
        lam = |g| < 7, per-line count <= min(chord/lam + 1,
        floor(D/r_g) + 1) -- min of unimodal and constant is
        unimodal, (A) gives
        f <= D^2/2m + sqrt2 lam D/m + floor(D/r_g) + 1.
        Asserted S20.

R13 (rule, proved -- THE BESPOKE FAMILIES). fmax is orbit-invariant
    (R2 + R9), so families are analyzed at their best rep. All
    primitive (t, s) with |g| < 7 and r_g <= 4 have B == s/t in
    family {2} = orbit of 2 ({2, -1, 1/2}), {3} = orbit of 3
    ({3, -2, 1/3, 2/3, 3/2, -1/2}) or {4} = orbit of 4
    ({4, -3, 1/4, 3/4, 4/3, -1/3}) -- finite enumeration, asserted
    S21. {2}: rep B = 2 is one-line (2D <= m-3 < m), R4 proves
    both caps (cap met, single maximizer). {3}, {4}: rep B == -a
    (a = 2, 3), intervals [au, (a+1)u]: X = c + pm <= (a+1)D < 2m
    forces TWO lines p in {0, 1}; per-line N <= X/(a(a+1)) + 1
    (unclipped X <= aD) or D - X/(a+1) + 1 (clipped): zone algebra
    (a = 3 split at delta = 1/3) gives every branch <= D/3 + 7/4:
    fmax <= D/3 + 2 (asserted S21), and D/3 + 2 < D/2 + 1/2 for
    D >= 10 (D <= 9 falls to the R11 small-D corollary at
    m >= 213).

R14 (rule, proved, COMPLETE COVERAGE -- THE CLOSURE). Target
    fmax < D/2 + 1/2 strictly: integer fmax then gives BOTH caps
    with the maximizer set empty at even D (family {2} alone meets
    the cap, R4-exact). WLOG D <= (m-3)/2 (R8, exact transfer;
    D = m-2 is R7). For m >= 213 every (D, B) falls to a case:
      0. D^2 < m: the R11 small-D corollary.
      1. lam(L_B) >= 7: Lemma B. Condition sqrt2/lam + sqrt2 lam/m
         < 1/2 - D/2m - 1/2D; RHS decreasing in D on D >= sqrt(m),
         so deep D binds; convex in lam, endpoints lam = 7
         (10.16/m < 0.048: m >= 212) and lam = 2 sqrt(m/pi)
         (Minkowski; 2.85/sqrt m < 1/4: m >= 135).
      2. lam < 7, r_g >= 5: Lemma D with floor(D/r) <= D/5:
         (D + 19.8)/2m < 3/10 - 1/2D, deep D binds: m >= 205.
      3. lam < 7, r_g <= 4: family {2}/{3}/{4}, R13.
    (r_g >= 5 in case 2 is automatic: the r <= 4 directions are
    exactly the three families of R13.) The case split + bounds
    verified mechanically at every (D, B) for every prime m in
    [213, 449] plus spot prime 1009: zero uncovered, zero bound
    failures, brute samples below the bounds (S22; a further run
    extended the same test to m = 2003 and 5003 -- margins GROW
    with m: minimum 6.0 at 2003, 10.3 at 5003). THE FINITE LEG: every prime m <= 211,
    every D in [1, m-2], every B in [2, m-1], BOTH caps brute-
    verified (R11 fast pass first, ~9% brute): zero violations;
    the coverage cap is attained only at (m, D) = (13, 5),
    B in {4, 10} (S23). TOGETHER: the max-coverage cap and the
    maximizer cap hold at EVERY prime m, every D in [1, m-2],
    every unit B not in {0, 1} -- so by R3 (+ R3's exact B = 1
    case) THE STRONG STAIRCASE LEMMA HOLDS AT EVERY (m, D, B).
    Tier: rule with complete coverage -- analytic m >= 213,
    exhaustive m <= 211; nothing conjectured (a finite-
    verification proof in the four-color sense; "theorem" is
    withheld only by the naming gate on computation-assisted
    proofs).

CONSEQUENCE FOR TWIN 2 (this closure). The strong staircase lemma now
holds unconditionally, so with the kill algebra (proved), the
counting gate, and R7/R8: TWIN 2'S EXCLUSION HOLDS AT EVERY
ODD PRIME PAIR (q, q') -- no covering system with two fat slices
evades at any two-prime d = q q', any D <= q-2. The open-zone
censuses (98 pairs q <= 97, 1103/1130 to q <= 400 by the R11 test
alone) survive as the arithmetic-test benchmark (S15); R1's
weak+gate classification (46 of 98) stays in
explore_cover_exclusion.py IV as the gate-only benchmark; the
unconditional closure is asserted there too. The >=3-factor
close-second-prime zone (slice-forcing scope only) remains open --
differences there are (Phi_m)-codewords, not constants; it needs
its own idea.

Checks below: S1 weak bound at arbitrary positions (random sweep +
strong-bound non-vacuity witness); S2 involution exact + inverse
observation; S3 max-coverage cap sweep; S4 maximizer cap sweep;
S5 reduction end-to-end (brute deep counts == reduction verdicts,
B=1 exactness); S6 one-line regime: proof bound floor(D/B*)+1
asserted + equality witness; S7 both-distinct relaxation (random) +
rights-only counterexample; S8 pair-shaped spot checks (the two
smallest open-zone pairs' moduli); S9 equicoverage exact (incl.
composite m); S10 duality identity exact; S11 time reversal exact;
S12 product bound exact to m = 103; S13 closed-region residual
census; S14 the all-B threshold pattern; S15 the 98-pair closure +
the q <= 400 frontier (the R11 test benchmark); S16 mid-band
residual sweep to m = 251; S17 the lattice-translate frame exact;
S18 Lemma B; S19 Lemma C; S20 Lemma D; S21 the family enumeration +
bespoke tents; S22 the assembled case split, primes in [213, 449];
S23 the finite leg, both caps, every prime m <= 211.

Classical contacts: lattice points in thin rational triangles
(three-distance theorem, Ostrowski representation -- the earlier-named
suspicion; R10 is its first descent step; R12 replaces the descent
with geometry of numbers); Minkowski's first theorem + Brunn
concavity (the generic count); the cross-ratio S3 action on the
multiplier; postage-stamp / h-basis (the un-reduced reading).

Runs in ~50 s, tiny memory. ALL CHECKS PASSED (33).
"""

import random
from math import gcd

CHECKS = 0
def check(cond, msg):
    global CHECKS
    CHECKS += 1
    print(f"  [{'ok' if cond else 'FAIL'}] {msg}")
    assert cond, msg

def section(t):
    print(); print("=" * 72); print(t); print("=" * 72)

def is_prime(n):
    if n < 2: return False
    q = 2
    while q * q <= n:
        if n % q == 0: return False
        q += 1
    return True

PRIMES = [p for p in range(5, 62) if is_prime(p)]

def coverage(m, D, lefts):
    """f-vector for intervals [lefts[u], lefts[u]+u], u = 0..D."""
    diff = [0] * (m + 1)
    for u in range(D + 1):
        L = lefts[u] % m
        R = L + u
        if R < m:
            diff[L] += 1; diff[R + 1] -= 1
        else:
            diff[L] += 1; diff[m] -= 1
            diff[0] += 1; diff[R - m + 1] -= 1
    f, acc = [], 0
    for t in range(m):
        acc += diff[t]
        f.append(acc)
    return f

def f_ap(m, D, B):
    return coverage(m, D, [(-B * u) % m for u in range(D + 1)])

def deep_count(f, D, s):
    thr = D + 1 - s
    return sum(1 for v in f if v >= thr)

# ------------------------------------------------------------------ S1
section("S1: the unconditional weak staircase (R1) -- arbitrary positions")
rng = random.Random(90)
weak_viol = 0
strong_viol = 0
trials = 0
for _ in range(4000):
    m = rng.randrange(7, 40)
    D = rng.randrange(3, m - 1)
    lefts = [rng.randrange(m) for _ in range(D + 1)]
    f = coverage(m, D, lefts)
    s = 0
    while s < (D + 1) / 2.0:
        k = deep_count(f, D, s)
        if k > 2 * s + 1: weak_viol += 1
        if k > s + 1: strong_viol += 1
        s += 1
    trials += 1
check(weak_viol == 0,
      f"weak bound 2s+1 holds in half-range at ARBITRARY positions "
      f"({trials} random systems, zero violations -- proof is pure "
      f"counting, no zone condition, no AP structure)")
check(strong_viol > 0,
      f"strong bound s+1 FAILS at arbitrary positions ({strong_viol} "
      f"violations) -- the strong lemma genuinely needs more than sizes")

# ------------------------------------------------------------------ S2
section("S2: the anharmonic involution (R2) + inverse observation")
ok = True
for m in (11, 23, 47):
    for D in range(3, m - 1):
        for B in range(2, m):
            fB = f_ap(m, D, B)
            fI = f_ap(m, D, (1 - B) % m)
            if any(fB[c] != fI[(-c) % m] for c in range(m)):
                ok = False
check(ok, "f_B(c) = f_{1-B}(-c) exactly (m = 11, 23, 47: all D, all B)")
m = 61
obs = True
for D in (10, 30, 50):
    for B in range(2, m):
        if max(f_ap(m, D, B)) != max(f_ap(m, D, pow(B, m - 2, m))):
            obs = False
check(obs, "fmax_B = fmax_{B^-1} (m = 61, D = 10/30/50) -- the earlier "
           "observation, PROVED pointwise (R9, asserted S11)")

# --------------------------------------------------------------- S3-S5
section("S3-S5: the caps sweep + the reduction end-to-end (R3, R5)")
cap_viol = []
maxcnt_viol = []
red_viol = []
worst_margin = None
for m in PRIMES:
    for D in range(3, m - 1):
        cap = D // 2 + 1
        for B in range(1, m):
            f = f_ap(m, D, B)
            fmax = max(f)
            if B == 1:
                # exactness: deep(s) = s+1 for all s < (D+1)/2
                s = 0
                while s < (D + 1) / 2.0:
                    if deep_count(f, D, s) != s + 1:
                        red_viol.append((m, D, B, s))
                    s += 1
                continue
            if fmax > cap:
                cap_viol.append((m, D, B, fmax))
            if D % 2 == 0:
                cnt = sum(1 for v in f if v >= cap)
                if cnt > cap:
                    maxcnt_viol.append((m, D, B, cnt))
                margin = cap - cnt
                if worst_margin is None or margin < worst_margin:
                    worst_margin = margin
            # reduction verdicts vs brute deep counts
            s = 0
            while s < (D + 1) / 2.0:
                k = deep_count(f, D, s)
                predicted_zero = (D % 2 == 1) or (s < D // 2)
                if predicted_zero and k != 0:
                    red_viol.append((m, D, B, s, k))
                if k > s + 1:
                    red_viol.append((m, D, B, s, k, 'LEMMA'))
                s += 1
check(not cap_viol,
      f"MAX-COVERAGE CAP: f <= floor(D/2)+1 for every prime m <= 61, "
      f"every D in [3, m-2], every B in [2, m-1] (violations: "
      f"{len(cap_viol)})")
check(not maxcnt_viol and worst_margin >= 2,
      f"MAXIMIZER CAP (D even): count <= D/2+1 everywhere swept; "
      f"observed slack >= {worst_margin} (count never exceeds D/2-1)")
check(not red_viol,
      "REDUCTION end-to-end: deep counts = 0 below the cap threshold, "
      "lemma bound s+1 never violated, B = 1 exact (= s+1 at every s)")

# caps-only extension (cheap: no per-s loop) -- a follow-up check, kept
ext_viol = 0
ext_worst = 99
for m in [p for p in range(63, 104) if is_prime(p)]:
    for D in range(3, m - 1):
        cap = D // 2 + 1
        for B in range(2, m):
            f = f_ap(m, D, B)
            if max(f) > cap: ext_viol += 1
            if D % 2 == 0:
                c = sum(1 for v in f if v >= cap)
                if c > cap: ext_viol += 1
                ext_worst = min(ext_worst, cap - c)
check(ext_viol == 0 and ext_worst >= 2,
      "caps extension sweep: both caps hold for every prime"
      " 63 < m <= 103, every D, every B in [2, m-1]; maximizer slack"
      " still >= 2 (wrapped-regime evidence at doubled m)")

# ------------------------------------------------------------------ S6
section("S6: the one-line regime (R4) -- proof bound + tightness")
ol_viol = []
tight = 0
for m in PRIMES:
    for D in range(3, m - 1):
        for B in range(2, m):
            Bs = min(B, m + 1 - B)
            if Bs * D >= m: continue
            fmax = max(f_ap(m, D, B))
            if fmax > D // Bs + 1:
                ol_viol.append((m, D, B, fmax))
            if Bs == 2 and D % 2 == 0 and fmax == D // 2 + 1:
                tight += 1
check(not ol_viol,
      "one-line regime B*D < m: fmax <= floor(D/B*)+1 everywhere "
      "(the proved R4 bound, B* = min(B, m+1-B))")
check(tight > 0,
      f"R4 bound is SHARP: B* = 2 achieves fmax = D/2+1 in {tight} "
      f"swept one-line cases (the c = -D construction)")

# ------------------------------------------------------------------ S7
section("S7: the both-distinct relaxation (R6)")
def random_both_distinct(m, D, rng, cluster):
    # cluster=True biases lefts toward one arc (stress: packed
    # small intervals are the near-tight shape)
    for _ in range(50):
        lefts, uL, uR = [], set(), set()
        ok = True
        for u in range(D + 1):
            cands = rng.sample(range(m), m)
            if cluster:
                cands.sort(key=lambda x: min(x, m - x) + 3 * rng.random())
            for L in cands:
                if L not in uL and (L + u) % m not in uR:
                    uL.add(L); uR.add((L + u) % m); lefts.append(L)
                    break
            else:
                ok = False; break
        if ok: return lefts
    return None

viol = 0; trials = 0
rng2 = random.Random(2026)
for i in range(25000):
    m = rng2.randrange(9, 42)
    D = rng2.randrange(4, m - 1)
    lefts = random_both_distinct(m, D, rng2, cluster=(i % 3 > 0))
    if lefts is None: continue
    trials += 1
    f = coverage(m, D, lefts)
    s = 0
    while s < (D + 1) / 2.0:
        if deep_count(f, D, s) > s + 1: viol += 1
        s += 1
check(viol == 0 and trials > 20000,
      f"both-distinct systems: #deep(s) <= s+1 in half-range "
      f"({trials} random systems, 2/3 cluster-biased, zero violations"
      f" -- tier: pattern)")
# one-sided distinctness fails: rights distinct, lefts repeat
m, D = 12, 10
lefts = [5, 10, 7, 11, 9, 3, 6, 0, 7, 1, 6]
rights = [(lefts[u] + u) % m for u in range(D + 1)]
f = coverage(m, D, lefts)
one_sided_breaks = (len(set(rights)) == D + 1 and len(set(lefts)) < D + 1
                    and any(deep_count(f, D, s) > s + 1
                            for s in range(0, (D + 1) // 2 + 1)
                            if s < (D + 1) / 2))
check(one_sided_breaks,
      "one-sided distinctness is NOT enough: the m=12, D=10 witness "
      "(rights distinct, lefts repeat) violates s+1 in half-range")
# the coverage cap is NOT combinatorial: both-distinct witness above cap
m40, D5, c20 = 40, 5, 20
w_lefts = [0, 20, 30, 19, 16, 18]
w_rights = [(w_lefts[u] + u) % m40 for u in range(D5 + 1)]
w_f = sum(1 for u in range(D5 + 1) if (c20 - w_lefts[u]) % m40 <= u)
check(len(set(w_lefts)) == 6 and len(set(w_rights)) == 6 and w_f == 4,
      "the COVERAGE CAP does not follow from end-distinctness: "
      "both-distinct system on Z/40, D = 5, covers a cell 4 > 3 "
      "times -- the cap is arithmetic, not combinatorial (R6 guard)")

# ------------------------------------------------------------------ S8
section("S8: pair-shaped spot checks (the kill algebra's inputs)")
for (q, qp) in ((11, 13), (13, 17)):
    D = q - 2
    bad = 0
    for m in (q, qp):
        for B in range(1, m):
            f = f_ap(m, D, B)
            s = 0
            while s < (D + 1) / 2.0:
                if deep_count(f, D, s) > s + 1: bad += 1
                s += 1
    check(bad == 0,
          f"pair ({q},{qp}): strong staircase holds at both moduli, "
          f"every B, D = q-2 (the exclusion's staircase input)")

# ------------------------------------------------------------------ S9
section("S9: equicoverage at D = m-2 (R7) -- any m, B and B-1 units")
eq_viol = 0
eq_tested = 0
for m in range(5, 80):
    for B in range(2, m):
        if gcd(B, m) != 1 or gcd(B - 1, m) != 1: continue
        eq_tested += 1
        f = f_ap(m, m - 2, B)
        if any(v != (m - 1) // 2 for v in f): eq_viol += 1
check(eq_viol == 0 and eq_tested > 1000,
      f"EQUICOVERAGE: f = (m-1)/2 at every cell, every m in [5, 79] "
      f"(composite included), every B with B, B-1 units "
      f"({eq_tested} systems, zero violations)")

# ----------------------------------------------------------------- S10
section("S10: the complementation duality (R8) -- exact identity")
du_viol = 0
du_tested = 0
for m in PRIMES:
    for D in range(0, m - 1):
        Dt = m - 3 - D
        off = D + (3 - m) // 2
        for B in range(2, m):
            fB = f_ap(m, D, B)
            ft = f_ap(m, Dt, (1 - B) % m) if Dt >= 0 else [0] * m
            for c in range(m):
                du_tested += 1
                if fB[c] != ft[(c - 2 * B + 1) % m] + off: du_viol += 1
check(du_viol == 0,
      f"DUALITY: f^B_D(c) = f^(1-B)_(m-3-D)(c-2B+1) + D + (3-m)/2 "
      f"exactly ({du_tested} point checks, primes m <= 61)")

# ----------------------------------------------------------------- S11
section("S11: time reversal (R9) -- the R2 observation is a rule")
tr_viol = 0
for m in PRIMES:
    for D in range(1, m - 1):
        for B in range(2, m):
            Bi = pow(B, m - 2, m)
            fB = f_ap(m, D, B)
            fI = f_ap(m, D, Bi)
            if any(fB[c] != fI[(D - Bi * D + Bi * c) % m]
                   for c in range(m)):
                tr_viol += 1
check(tr_viol == 0,
      "TIME REVERSAL: f^B_D(c) = f^(B^-1)_D(D - B^-1 D + B^-1 c) "
      "exactly (primes m <= 61, all D, all B)")

# ----------------------------------------------------------------- S12
section("S12: the product bound (R10) -- exact to m = 103")
pb_viol = 0
for m in [p for p in range(5, 104) if is_prime(p)]:
    for D in range(1, m - 1):
        for b in range(2, (m + 1) // 2 + 1):
            bound = (b * D // m + 1) * (D // b + 1)
            for B in (b, (1 - b) % m):
                if max(f_ap(m, D, B)) > bound: pb_viol += 1
check(pb_viol == 0,
      "PRODUCT BOUND: fmax <= (floor(bD/m)+1)(floor(D/b)+1) for "
      "every prime m <= 103, every D, every b = B*, both involution "
      "representatives (zero violations)")

# ------------------------------------------------- S13-S15 shared kit
def orbit(B, m):
    Bi = pow(B, m - 2, m)
    return {B % m, (1 - B) % m, Bi, (1 - Bi) % m,
            pow((1 - B) % m, m - 2, m),
            (B * pow((B - 1) % m, m - 2, m)) % m}

def caps_proved(B, m, D, even_maximizer=False):
    """The R11 arithmetic test: both caps proved at (m, D, B)?
    (even_maximizer=True demands the maximizer cap at even D too.)"""
    for Dp in (D, m - 3 - D):
        if Dp <= 0: return True            # R7 equicoverage / trivial
        cap = Dp // 2 + 1
        for x in orbit(B, m):
            b = min(x, m + 1 - x)
            if b * Dp < m: return True     # one-line (R4): both caps
            if Dp + 1 <= b <= (m - 1) // 2:
                return True                # sparse (R10): both caps
            prod = (b * Dp // m + 1) * (Dp // b + 1)
            if prod <= (Dp // 2 if even_maximizer else cap):
                return True                # product (R10)
    return False

# ----------------------------------------------------------------- S13
section("S13: the closed region (R11) -- residual census at m <= 47")
resid_cov = tot = 0
resid_max = tot_even = 0
for m in [p for p in range(5, 48) if is_prime(p)]:
    for D in range(3, m - 1):
        for B in range(2, m):
            tot += 1
            if not caps_proved(B, m, D): resid_cov += 1
            if D % 2 == 0:
                tot_even += 1
                if not caps_proved(B, m, D, even_maximizer=True):
                    resid_max += 1
band_ok = True
for m in [p for p in range(5, 48) if is_prime(p)]:
    for D in range(3, m - 1):
        if min(D, m - 3 - D)**2 < m:      # the proved small-D corollary
            for B in range(2, m):
                if not caps_proved(B, m, D): band_ok = False
check(band_ok,
      "SMALL-D COROLLARY: min(D, m-3-D)^2 < m closes ALL B (the "
      "arithmetic test confirms the union has no hole)")
check(resid_cov / tot < 0.06 and resid_max / tot_even < 0.13,
      f"residual census: the R11 test leaves {resid_cov}/{tot} "
      f"triples ({100*resid_cov/tot:.1f}%) for the coverage cap and "
      f"{resid_max}/{tot_even} even-D triples "
      f"({100*resid_max/tot_even:.1f}%) for the maximizer cap -- "
      f"the mid-band, closed at R12-R14")

# ----------------------------------------------------------------- S14
section("S14: the all-B threshold (R11 pattern) -- ~ m/4")
thr_ok = True
for m in (101, 199, 307, 503):
    Dt_max = 0
    for d in range(1, m - 1):
        good = True
        for b in range(2, (m + 1) // 2 + 1):
            if b * d < m: continue
            if d + 1 <= b <= (m - 1) // 2: continue
            if (b * d // m + 1) * (d // b + 1) <= d // 2 + 1: continue
            good = False; break
        if good: Dt_max = d
        else: break
    if not (m // 4 - 1 <= Dt_max <= m // 4): thr_ok = False
    print(f"  m = {m}: contiguous all-B threshold = {Dt_max} "
          f"(m/4 = {m // 4})")
check(thr_ok,
      "all-B threshold (every b closed with NO orbit help) is "
      "floor(m/4) or floor(m/4)-1 at m = 101, 199, 307, 503 -- "
      "tier: pattern")

# ----------------------------------------------------------------- S15
section("S15: the pair closure -- all 98 open-zone pairs, q <= 400 "
        "frontier")
def open_zone(qcap):
    out = []
    for q in range(11, qcap + 1, 2):
        if not is_prime(q): continue
        for qp in range(q + 2, (3 * q - 4) // 2 + 1, 2):
            if is_prime(qp): out.append((q, qp))
    return out

pairs98 = open_zone(97)
unclosed = [(q, qp) for (q, qp) in pairs98
            if not all(caps_proved(B, qp, q - 2)
                       for B in range(2, qp))]
check(len(pairs98) == 98 and not unclosed,
      "ALL 98 open-zone pairs q <= 97 close by the R11 test ALONE at "
      "(q', q-2), every unit B (q side = R7; D = q-2 odd, no "
      "maximizer cap needed) -- the arithmetic-test benchmark; the "
      "unconditional closure is R14's")
frontier = open_zone(400)
failing = [(q, qp) for (q, qp) in frontier
           if not all(caps_proved(B, qp, q - 2)
                      for B in range(2, qp))]
wide = all(qp - q - 1 >= qp // 4 for (q, qp) in failing)
check(len(frontier) == 1130 and len(failing) == 27 and wide,
      f"q <= 400 frontier of the R11 test: "
      f"{len(frontier) - len(failing)}/{len(frontier)} open-zone "
      f"pairs close by the test alone; the {len(failing)} others sit "
      f"in the widest-gap band (q'-q-1 >= q'/4) and fall to R14's "
      f"cases like everything else")

# ----------------------------------------------------------------- S16
section("S16: the mid-band itself -- residual-only cap sweep to "
        "m = 251 (follow-up probe, kept)")
mb_viol = 0
mb_tested = 0
mb_at_cap = []
for m in [p for p in range(5, 252) if is_prime(p)]:
    for D in range(3, m - 1):
        cap = D // 2 + 1
        for B in range(2, m):
            if caps_proved(B, m, D): continue      # unproved region only
            mb_tested += 1
            mx = max(f_ap(m, D, B))
            if mx > cap: mb_viol += 1
            elif mx == cap: mb_at_cap.append((m, D, B))
check(mb_viol == 0 and mb_tested > 75000
      and mb_at_cap == [(13, 5, 4), (13, 5, 10)],
      f"MID-BAND CAP: zero violations across all {mb_tested} "
      f"R11-residual (m, D, B) triples, every prime m <= 251 -- and"
      f" the cap is ATTAINED in the residual only at (13, 5, B in"
      f" {{4, 10}}) (self-dual D = D~ = 5, two-element orbit):"
      f" slack >= 1 everywhere else in the residual")

# ----------------------------------------------------------------- S17
section("S17: the lattice-translate frame (R12) -- exact")
frame_bad = 0
for (m, D, B) in [(13, 5, 4), (23, 9, 5), (31, 14, 7), (47, 21, 12),
                  (61, 29, 44)]:
    f = f_ap(m, D, B)
    for c in range(m):
        cnt = sum(1 for u in range(D + 1) if (c + B * u) % m <= u)
        if cnt != f[c]: frame_bad += 1
check(frame_bad == 0,
      "f(c) = #{(u,v): 0 <= v <= u <= D, v == c + Bu (mod m)} -- the "
      "translate of L_B in the triangle T_D, exactly (5 spot systems, "
      "every c)")

# --------------------------------------------------- S18-S23 shared kit
SQ2 = 2 ** 0.5

def short_vec(B, m):
    """Shortest nonzero (t, s) with s == Bt (mod m), t >= 1, s signed;
    returns (t, s, norm^2)."""
    best = (0, m, m * m)
    t = 1
    while t * t < best[2]:
        s = (B * t) % m
        if s > m - s: s -= m
        n2 = t * t + s * s
        if n2 < best[2]: best = (t, s, n2)
        t += 1
    return best

def run_denom(t, s):
    if s > t: return s
    if s > 0: return t
    return t - s

# ----------------------------------------------------------------- S18
section("S18: Lemma B (generic count) -- bound holds at every B")
lb_bad = 0
for m in (211, 401, 599):
    for B in range(2, m):
        t, s, n2 = short_vec(B, m)
        lam = n2 ** 0.5
        for D in (m // 4 + 1, m // 3, (m - 3) // 2):
            fm = max(f_ap(m, D, B))
            if fm > D * D / (2 * m) + SQ2 * D / lam \
                    + SQ2 * lam * D / m + 1 + 1e-9:
                lb_bad += 1
check(lb_bad == 0,
      "f <= D^2/2m + sqrt2 D/lam + sqrt2 lam D/m + 1 at m = 211, "
      "401, 599: every B, three D each (zero violations)")

# ----------------------------------------------------------------- S19
section("S19: Lemma C (run bound) -- random directions and starts")
rc_bad = 0
rng3 = random.Random(92)
for _ in range(4000):
    D = rng3.randint(10, 400)
    t = rng3.randint(1, 6)
    s = rng3.randint(-6, 6)
    if s == 0 or s == t or gcd(t, abs(s)) != 1: continue
    cap_r = D // run_denom(t, s) + 1
    for _ in range(40):
        u0 = rng3.randint(0, D); v0 = rng3.randint(0, u0)
        n = 0
        while 0 <= v0 + n * s <= u0 + n * t <= D:
            n += 1
        if n > cap_r: rc_bad += 1
check(rc_bad == 0,
      "runs of primitive (t, s) inside T_D never exceed "
      "floor(D/r_g)+1, r_g = s / t / t+|s| (random sweep, zero "
      "violations)")

# ----------------------------------------------------------------- S20
section("S20: Lemma D (resonant count) -- bound holds at every "
        "resonant B")
ldn_bad = 0
for m in (211, 401, 599):
    for B in range(2, m):
        t, s, n2 = short_vec(B, m)
        if n2 >= 49: continue
        r = run_denom(t, s)
        lam = n2 ** 0.5
        for D in (m // 4 + 1, m // 3, (m - 3) // 2):
            fm = max(f_ap(m, D, B))
            if fm > D * D / (2 * m) + SQ2 * lam * D / m \
                    + D // r + 1 + 1e-9:
                ldn_bad += 1
check(ldn_bad == 0,
      "f <= D^2/2m + sqrt2 lam D/m + floor(D/r_g) + 1 at every "
      "sub-7-lambda B, m = 211/401/599 (zero violations)")

# ----------------------------------------------------------------- S21
section("S21: the family enumeration + the bespoke tents (R13)")
# every primitive (t,s), norm < 7, r_g <= 4 lands in family {2}/{3}/{4}
def family_of(t, s, m):
    inv = lambda x: pow(x % m, m - 2, m)
    B = (s * inv(t)) % m
    fam2 = {2 % m, m - 1, inv(2)}
    fam3 = {3 % m, m - 2, inv(3), (2 * inv(3)) % m,
            (3 * inv(2)) % m, (m - inv(2)) % m}
    fam4 = {4 % m, m - 3, inv(4), (3 * inv(4)) % m,
            (4 * inv(3)) % m, (m - inv(3)) % m}
    return (B in fam2, B in fam3, B in fam4)

enum_ok = True
enum_count = 0
for t in range(1, 7):
    for s in range(-6, 7):
        if s == 0 or s == t or gcd(t, abs(s)) != 1: continue
        if t * t + s * s >= 49: continue
        if run_denom(t, s) >= 5: continue
        enum_count += 1
        for m in (223, 401):                    # family membership is
            if not any(family_of(t, s, m)):     # m-independent algebra
                enum_ok = False
check(enum_ok and enum_count == 15,
      f"ENUMERATION: all {enum_count} primitive sub-7 directions with "
      f"r_g <= 4 have B == s/t in family {{2}}, {{3}} or {{4}} "
      f"(checked at m = 223, 401)")
tent_bad = 0
for m in [p for p in range(50, 402) if is_prime(p)]:
    for a in (2, 3):
        B = m - a
        for D in range(1, (m - 3) // 2 + 1):
            if max(f_ap(m, D, B)) > D / 3 + 2:
                tent_bad += 1
check(tent_bad == 0,
      "BESPOKE TENTS: fmax <= D/3 + 2 for B == -2 and B == -3, every "
      "prime m in [53, 401], every D <= (m-3)/2 (zero violations)")

# ----------------------------------------------------------------- S22
section("S22: the assembled case split (R14) -- primes in [213, 449]")
rng4 = random.Random(214)
uncovered = 0
bound_fail = 0
brute_fail = 0
asm_total = 0
asm_sampled = 0
for m in [p for p in range(213, 450) if is_prime(p)] + [1009]:
    inv = lambda x: pow(x % m, m - 2, m)
    fam2 = {2, m - 1, inv(2)}
    fam34 = {3, m - 2, inv(3), (2 * inv(3)) % m, (3 * inv(2)) % m,
             (m - inv(2)) % m, 4, m - 3, inv(4), (3 * inv(4)) % m,
             (4 * inv(3)) % m, (m - inv(3)) % m}
    for B in range(2, m):
        t, s, n2 = short_vec(B, m)
        lam = n2 ** 0.5
        for D in range(3, (m - 3) // 2 + 1):
            asm_total += 1
            if D * D < m: continue                     # case 0 (R11)
            if n2 >= 49:                               # case 1
                bnd = D * D / (2 * m) + SQ2 * D / lam \
                      + SQ2 * lam * D / m + 1
            else:
                r = run_denom(t, s)
                if r >= 5:                             # case 2
                    bnd = D * D / (2 * m) + SQ2 * lam * D / m \
                          + D // r + 1
                elif B in fam2:                        # case 3: R4
                    continue
                elif B in fam34:                       # case 3: tents
                    bnd = D / 3 + 2
                else:
                    uncovered += 1
                    continue
            if bnd >= D / 2 + 0.5:
                bound_fail += 1
            elif rng4.random() < 0.001:
                asm_sampled += 1
                if max(f_ap(m, D, B)) > bnd:
                    brute_fail += 1
check(uncovered == 0 and bound_fail == 0 and brute_fail == 0,
      f"CASE SPLIT: {asm_total} triples over primes in [213, 449] "
      f"plus spot prime 1009: every (D, B) covered by a case, every "
      f"case-1/2/3 bound STRICTLY below D/2 + 1/2, {asm_sampled} "
      f"brute samples all under their bounds")

# ----------------------------------------------------------------- S23
section("S23: the finite leg (R14) -- both caps, every prime m <= 211")
fl_cov = 0
fl_max = 0
fl_brute = 0
fl_total = 0
fl_tight = []
for m in [p for p in range(2, 212) if is_prime(p)]:   # 2, 3 included:
    # m = 2 has no valid (D, B); m = 3 has exactly (D, B) = (1, 2)
    for D in range(1, m - 1):
        cap = D // 2 + 1
        for B in range(2, m):
            fl_total += 1
            need_cov = not caps_proved(B, m, D)
            need_max = (D % 2 == 0) and not caps_proved(B, m, D, True)
            if not (need_cov or need_max): continue
            fl_brute += 1
            f = f_ap(m, D, B)
            fm = max(f)
            if fm > cap: fl_cov += 1
            if fm == cap and need_cov: fl_tight.append((m, D, B))
            if D % 2 == 0 and \
                    sum(1 for v in f if v == cap) > cap:
                fl_max += 1
check(fl_cov == 0 and fl_max == 0
      and fl_tight == [(13, 5, 4), (13, 5, 10)],
      f"FINITE LEG: {fl_total} triples (every prime m <= 211, every "
      f"D, every B in [2, m-1]), {fl_brute} brute-forced past the "
      f"R11 filter: BOTH caps hold everywhere; coverage cap attained "
      f"only at (13, 5, B in {{4, 10}})")

print(f"\nALL CHECKS PASSED ({CHECKS})")
