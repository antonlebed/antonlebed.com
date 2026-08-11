"""The Pisot tower's third member: the degree-4 (Tetranacci) trailing
window — the comb scaling and the 3-torus shadow.

THE QUESTION
------------
Is the odometer cell the degree-2 member of a tower of translation
cells, one per recurrence degree? The opening hook (observation, two
members): a carry descending d makes the witness comb step d+1 and
the image cycle through d phases (d = 2 Zeckendorf, d = 3
Tribonacci). This script builds the hook's third member — the
trailing Tetranacci window, q_k = q_{k-1} + q_{k-2} + q_{k-3} +
q_{k-4}, greedy digits, 1111-free — and asks whether the comb scales
as the hook predicts: witness comb step 5, image a step-4 comb whose
bottom cycles through FOUR phases over one input limit, so x2 has no
continuous extension and the degree-4 completion is not a ring. The
completion's positive side is a CLASSICAL IMPORT, contacted before
this rig was built: the k-bonacci substitution is the substitutive
Arnoux-Rauzy sequence, substitutive Arnoux-Rauzy sequences have pure
discrete spectrum (Berthe-Steiner-Thuswaldner), so the degree-k
system is measurably isomorphic to a translation of the (k-1)-torus
— T^3 here; the rig measures only its numeric shadow (cells
contracting at the conjugate roots' own rates). TRANSPLANTS, flagged
at the freeze: the step/phase scaling is imported from degrees 2 and
3 (the hook's two members); the torus expectation from degree 3
(Rauzy). Both are predictions to test, not facts.

THE PROOF (hand-derived before any engine; conventions q_0 = 1,
q_1 = 2, q_2 = 4, q_3 = 8, digits d_k at place q_k, low index first)
--------------------------------------------------------------------
LEMMA 0 (canonicity): a 0/1 digit string with no "1111" factor is
THE greedy expansion of its value. Any 1111-free string on indices
< k sums to <= q_k - 1: among its top four indices k-1..k-4 at least
one is absent, and the four cases give sums <= q_{k-1} - 1,
q_{k-1} + q_{k-2} - 1, q_{k-1} + q_{k-2} + q_{k-3} - 1, and
q_{k-1} + q_{k-2} + q_{k-3} + q_{k-4} - 1 = q_k - 1 by induction
(bases k = 0..3: sums 0, 1, 3, 7 = q_k - 1). So a 1111-free string
with top index t has value in [q_t, q_{t+1} - 1], greedy takes q_t
and recurses: greedy reproduces the string; distinct 1111-free
strings have distinct values.

LEMMA A (the down-carry): 2 q_k = q_{k+1} + q_{k-4} for k >= 4
(2 q_k - q_{k+1} = q_k - q_{k-1} - q_{k-2} - q_{k-3} = q_{k-4});
boundary: 2 q_0 = q_1, 2 q_1 = q_2, 2 q_2 = q_3, 2 q_3 = q_4 + q_0;
and the base consolidation q_0 + q_1 + q_2 + q_3 = q_4 (15).

THE WITNESS SPINE is the STEP-5 COMB, the step the carry's descent
by four dictates: T_K = q_4 + q_9 + q_14 + ... + q_K, K = 4 mod 5.

THEOREM (four-phase image): the canonical digits of 2 T_K are the
step-4 comb with top tooth K+1 and a bottom that cycles with period
20 in K:
  K = 4  mod 20:  {0} u {j = 1 mod 4 : 5 <= j <= K+1}
  K = 9  mod 20:  {0, 1} u {j = 2 mod 4 : 6 <= j <= K+1}
  K = 14 mod 20:  {0, 1, 2} u {j = 3 mod 4 : 7 <= j <= K+1}
  K = 19 mod 20:  {j = 0 mod 4 : 4 <= j <= K+1}
Bases (exact integers): 2 T_4 = 30 = q_5 + q_0; 2 T_9 = 832 =
q_10 + q_6 + q_1 + q_0; 2 T_14 = 22174 = q_15 + q_11 + q_7 + q_2 +
q_1 + q_0; 2 T_19 = 590080 = q_20 + q_16 + q_12 + q_8 + q_4.
Step K -> K+5: 2 T_{K+5} = 2 T_K + q_{K+6} + q_{K+1} (Lemma A on
2 q_{K+5}). The added q_{K+1} doubles the image's top tooth, and the
down-carry cascades down the comb — teeth spaced four, the carry
descending four: each 2 q_j = q_{j+1} + q_{j-4} deposits q_{j+1}
(fresh: deposits sit at j+1 = K+2 mod 4, remaining teeth at K+1 mod
4, disjoint) and re-doubles the tooth four below, so every tooth
shifts up one. The bottom closes the cycle: phase 19's bottom tooth
4 splits (2 q_4 = q_5 + q_0) opening phase 4's {0}; phase 4's bottom
tooth 5 splits (2 q_5 = q_6 + q_1), q_1 joining q_0 as phase 9's
{0, 1}; phase 9's bottom tooth 6 splits (2 q_6 = q_7 + q_2) giving
phase 14's {0, 1, 2}; phase 14's bottom tooth 7 splits
(2 q_7 = q_8 + q_3) and q_0 + q_1 + q_2 + q_3 consolidates to q_4,
phase 19's comb bottom. Each result is 1111-free (teeth spaced four;
the longest low run {0, 1, 2} has length three and sits below a
gap), hence canonical by Lemma 0.

THE GENERAL THEOREM (every degree d >= 2 — the proof above is
UNIFORM in d and this paragraph is its statement; the d-bonacci
system q_j = 2^j for j < d, q_k = q_{k-1} + ... + q_{k-d}, greedy
digits, (1^d)-free): Lemma 0 holds with "no d consecutive ones"
(the top-d-indices case split, bases q_j - 1 = 2^j - 1); Lemma A
reads 2 q_k = q_{k+1} + q_{k-d} for k >= d, with small doublings
2 q_j = q_{j+1} (j <= d-2), 2 q_{d-1} = q_d + q_0, and the
consolidation q_0 + ... + q_{d-1} = 2^d - 1 = q_d. The witness comb
T_K = q_d + q_{2d+1} + ... + q_K (step d+1, K = d mod d+1) doubles
to the step-d comb with top tooth K+1 whose bottom cycles with
period d(d+1) in K through d phases: at K = d + (d+1) i mod
d(d+1), bottom {0, ..., i} and comb {j = i+1 mod d :
d+1+i <= j <= K+1} for i = 0..d-2, and at i = d-1 the consolidated
comb {j = 0 mod d : d <= j <= K+1}. The induction is the same
cascade (teeth spaced d, carry descending d, deposits disjoint,
every tooth up one; the bottom walks its d splits and consolidates),
every result (1^d)-free, canonical by Lemma 0. CONSEQUENCE at every
d: input agreement K+d+1 unbounded, the d image limit strings
pairwise distinct at a digit <= d-2, so x2 has no continuous
extension to ANY d-bonacci completion, d >= 2 — Zeckendorf's two
phases and Tribonacci's three are the d = 2, 3 rows of one theorem,
and the hook's step/phase scaling (witness d+1, image d, d phases)
is that theorem's shape rather than an observed coincidence.

CONSEQUENCE (the kill, unconditional in K): T_K and T_{K+5} are both
canonical step-5 combs agreeing at every digit index < K+5 — input
agreement K+5, unbounded — while the images differ at a bounded low
digit read off the phase table: first difference at digit 1
(K = 4 mod 20), 2 (K = 9), 0 (K = 14 and 19) — never above 2.
COMPLETION FORM: the strings of T_K converge in the completion to x*
(the infinite step-5 comb); the strings of 2 T_K converge along each
phase class to the FOUR infinite step-4 combs with bottoms {0},
{0,1}, {0,1,2}, {4} — pairwise distinct at digit 0, 1, or 2. A
continuous g with g|_Z = x2 would give all four as g(x*). So x2 has
no continuous extension — and hence no continuous addition on the
completion extends Z's — at degree 4: the hook's third member, the
image cycling through d = 4 phases where Tribonacci cycles three and
Zeckendorf two, witness step d+1 = 5, image step d = 4. x3 does not
transplant to a comb move here either [TRANSPLANT from d = 2, 3,
same shape]: 3 q_k = q_{k+1} + q_k + q_{k-4}, immediate from Lemma
A, keeps a copy at position k — the triple carry never clears its
own tooth.

THE DESIGN (checks; greedy extraction only — no closed form from the
proof enters the digit path. The greedy engine is parameterized by
DEGREE so the control can run it at d = 3 against the Tribonacci
rig's published prints before any d = 4 verdict is read.)
--------------------------------------------------------------------
D0  POSITIVE CONTROL (cross-rig, d = 3 engine): the Tribonacci
    rig's base integers and digit sets — 2 T_3 = 14 = {0, 4},
    2 T_7 = 176 = {0, 1, 5, 8}, 2 T_11 = 2030 = {3, 6, 9, 12} — and
    the atlas's extremal pair (93684, 63562) printing input
    agreement 17, image agreement 4.
D1  Lemma A in range: the down-carry at every 4 <= k < 45, the four
    boundary identities, the base consolidation (exact).
D2  Lemma 0's bound in range: max 1111-free sum on indices < k
    equals q_k - 1, exhaustive over bitmasks for k <= 20.
D3  The theorem in range: greedy digits of 2 T_K equal the stated
    phase set for every K = 4, 9, ..., 49.
D4  Input agreement: greedy agreement of (T_K, T_{K+5}) is exactly
    K+5 for every K in range.
D5  The kill digit: the least digit where the images of consecutive
    pairs differ is 1, 2, 0, 0 at K = 4, 9, 14, 19 mod 20 — bounded
    by 2 at every K.
D6  The four limit strings: the low-16 digits of 2 T_K are constant
    on each phase class for K >= 20 and pairwise distinct across the
    four classes.
D7  THE 3-TORUS SHADOW (numeric shadow of the classical import,
    never its proof): the quartic x^4 - x^3 - x^2 - x - 1 has one
    root outside the unit circle (the Pisot root) and three inside —
    one real, one complex pair (roots by Durand-Kerner, pure
    Python). For each contracting direction, the coordinate
    c(n) = sum d_k lambda^k over a sample n < 200000 grouped into
    depth-t cells (digits below t shared): the mean cell diameter's
    ratio between depths t and t+5 prints against |lambda|^5, at
    t = 4 -> 9 and 9 -> 14.
D8  The x3 identity 3 q_k = q_{k+1} + q_k + q_{k-4} in range
    (the non-transplant note's own check).
D9  THE GENERAL THEOREM at two untouched degrees (added to the
    slate after D0-D8 ran, frozen before it ran): the generic phase
    table, input agreement K+d+1, and kill digit <= d-2, checked by
    greedy extraction at d = 5 (period 30) and d = 6 (period 42)
    over every K = d mod d+1 with K + 2 < WIDTH.

PREDICTIONS, frozen before the engine
-------------------------------------
P1  D0 prints the three Tribonacci digit sets and 17/4 exactly.
P2  D1 exact, zero failures.
P3  D2 exact at every k <= 20.
P4  D3 exact at every K — the four-phase table as stated.
P5  D4 exactly K+5 at every K.
P6  D5 least differing digit 1, 2, 0, 0 by phase — never above 2.
P7  D6 four stable, pairwise distinct prefixes.
P8  D7 prints one real + one complex-pair contracting direction and
    diameter ratios within [0.7, 1.3] x |lambda|^5 for each (the
    Tribonacci shadow sat within ~6% of |lambda|^4; the band is
    deliberately loose — the kill is a ratio OUTSIDE it, read from
    the print).
P9  D8 exact, zero failures.
PG  D9 exact at every checked K at both degrees: digits equal the
    generic table, agreement exactly K+d+1, kill digit <= d-2.

FINDINGS (entered after the run; prints copied from the run record)
--------------------------------------------------------------------
F1  THE CONTROL MATCHES THE TRIBONACCI RIG: the d = 3 engine prints
    2 T_3 = 14 = {0, 4}, 2 T_7 = 176 = {0, 1, 5, 8}, 2 T_11 = 2030
    = {3, 6, 9, 12}, and the atlas pair (93684, 63562) at input
    agreement 17, image agreement 4 (P1 met — the engine speaks both
    prior rigs' conventions before any degree-4 line is read).
F2  LEMMA A EXACT: down-carry zero failures at 4 <= k < 45; the four
    boundary identities and the consolidation exact (P2 met).
F3  LEMMA 0'S BOUND EXACT: max 1111-free sum on indices < k equals
    q_k - 1 at every k <= 20, exhaustive over all 2^k masks
    (P3 met).
F4  THE FOUR-PHASE THEOREM EXACT IN RANGE: greedy digits of 2 T_K
    equal the stated phase set at every K = 4, 9, ..., 49 — ten
    values, phases cycling 4 -> 9 -> 14 -> 19 -> 4 (P4 met). The
    largest checked: 2 T_49 = 209489562353088, the phase-9 comb
    {0, 1, 6, 10, ..., 50}.
F5  INPUT AGREEMENT EXACTLY K+5 at every pair (T_K, T_{K+5}) in
    range (P5 met), unbounded by the theorem.
F6  THE KILL DIGIT AS STATED: least differing image digit 1, 2, 0, 0
    at K = 4, 9, 14, 19 mod 20 — never above 2 (P6 met).
F7  THE FOUR LIMIT STRINGS, distinct and stable: low-16 digits
    1000010001000100 (phase 4), 1100001000100010 (phase 9),
    1110000100010001 (phase 14), 0000100010001000 (phase 19) —
    pairwise distinct already at digit 0, 1, or 2: the theorem's
    four limit points printed (P7 met).
F8  THE 3-TORUS SHADOW AT THE CONJUGATE RATES, with a thinning
    caveat read from the prints: contracting roots one real
    (-0.774804) and one complex pair (modulus 0.818276) — three
    contracting dimensions. Diameter ratios per 5 depths: real
    direction 0.25769 (t 4->9) and 0.20464 (9->14) against
    |lambda|^5 = 0.279228; plane direction 0.34284 and 0.25893
    against 0.366859. All four inside the frozen band (P8 met); the
    4->9 pair sits within 8% of the conjugate rates while the 9->14
    pair reads LOW — n < 200000 has top index <= 18, so a depth-14
    cell varies only digits 14..18 and its few residents undersample
    the diameter; a shadow, not a proof, and the import carries the
    statement.
F9  THE x3 IDENTITY EXACT at 4 <= k < 45 (P9 met) — the triple
    carry keeps its copy at k; the comb move does not transplant, as
    at degrees 2 and 3.
F10 THE GENERAL THEOREM EXACT AT d = 5 AND 6: every phase set
    equals the generic table (8 checked at d = 5, largest
    2 T_47 = 135145202029312; 7 at d = 6, largest
    2 T_48 = 395537260501502), agreement exactly K+d+1, kill digit
    <= d-2 at every pair (PG met) — two degrees no rig had
    touched, read straight off the uniform proof.

RUN RECORD
----------
Three runs: D0-D8 green on the first (wall 4.2s; the run whose D5
report label carried an em dash the Windows console cannot encode),
label ASCII-fixed and rerun identical (wall 4.1s, every printed
number unchanged); D9 added to the slate and the full rig rerun, all
ten checks green, D0-D8's numbers unchanged (wall 4.1s), VERDICT
True on every line. The D2 bitmask sweep and the D7 sample dominate
the wall; trivial memory.
"""

import cmath
import sys

WIDTH = 55


def build_Q(degree, seeds):
    Q = list(seeds)
    while len(Q) < 60:
        Q.append(sum(Q[-degree:]))
    return Q


Q4 = build_Q(4, [1, 2, 4, 8])
Q3 = build_Q(3, [1, 2, 4])


def greedy(n, Q):
    """Greedy digits d_0..d_{WIDTH-1}, low index first."""
    d = [0] * WIDTH
    for k in range(len(Q) - 1, -1, -1):
        if Q[k] <= n:
            if k < WIDTH:
                d[k] = 1
            n -= Q[k]
    assert n == 0
    return tuple(d)


def agree(a, b, Q):
    da, db = greedy(a, Q), greedy(b, Q)
    t = 0
    while t < WIDTH and da[t] == db[t]:
        t += 1
    return t


def digit_set(n, Q):
    return {k for k, bit in enumerate(greedy(n, Q)) if bit}


def comb_T(K, Q, lo, step):
    return sum(Q[j] for j in range(lo, K + 1, step))


def phase_set(K):
    """The theorem's predicted digit index set for 2 T_K (degree 4)."""
    r = K % 20
    if r == 4:
        return {0} | set(range(5, K + 2, 4))
    if r == 9:
        return {0, 1} | set(range(6, K + 2, 4))
    if r == 14:
        return {0, 1, 2} | set(range(7, K + 2, 4))
    return set(range(4, K + 2, 4))


ok_all = True


def report(label, ok):
    global ok_all
    ok_all = ok_all and ok
    print(f"{label}: {ok}")


# D0 — positive control: the d = 3 engine against the Tribonacci rig
tri_bases = {3: (14, {0, 4}), 7: (176, {0, 1, 5, 8}),
             11: (2030, {3, 6, 9, 12})}
d0 = True
for K, (val, digits) in tri_bases.items():
    t = 2 * comb_T(K, Q3, 3, 4)
    got = digit_set(t, Q3)
    print(f"D0 d=3 base K={K}: 2 T_K = {t}, digits {sorted(got)}")
    d0 = d0 and t == val and got == digits
ia = agree(93684, 63562, Q3)
im = agree(2 * 93684, 2 * 63562, Q3)
print(f"D0 atlas pair: input agreement {ia}, image agreement {im}")
d0 = d0 and ia == 17 and im == 4
report("D0 control (Tribonacci prints reproduced)", d0)

# D1 — Lemma A
d1 = all(2 * Q4[k] == Q4[k + 1] + Q4[k - 4] for k in range(4, 45))
d1 = d1 and 2 * Q4[0] == Q4[1] and 2 * Q4[1] == Q4[2]
d1 = d1 and 2 * Q4[2] == Q4[3] and 2 * Q4[3] == Q4[4] + Q4[0]
d1 = d1 and Q4[0] + Q4[1] + Q4[2] + Q4[3] == Q4[4]
report("D1 down-carry + boundaries", d1)

# D2 — Lemma 0's bound, exhaustive
d2 = True
for k in range(1, 21):
    best = 0
    for mask in range(1 << k):
        if mask & (mask << 1) & (mask << 2) & (mask << 3):
            continue
        s = sum(Q4[j] for j in range(k) if mask >> j & 1)
        best = max(best, s)
    if best != Q4[k] - 1:
        d2 = False
        print(f"  D2 FAIL at k={k}: max {best} vs {Q4[k] - 1}")
report("D2 max 1111-free sum = q_k - 1 (k <= 20)", d2)

# D3 — the four-phase theorem
KS = list(range(4, 50, 5))
d3 = True
for K in KS:
    got = digit_set(2 * comb_T(K, Q4, 4, 5), Q4)
    want = phase_set(K)
    if got != want:
        d3 = False
        print(f"  D3 FAIL at K={K}: got {sorted(got)} want {sorted(want)}")
print(f"D3 largest: 2 T_49 = {2 * comb_T(49, Q4, 4, 5)}")
report("D3 four-phase image (K = 4..49)", d3)

# D4 — input agreement exactly K+5
d4 = all(agree(comb_T(K, Q4, 4, 5), comb_T(K + 5, Q4, 4, 5), Q4) == K + 5
         for K in KS[:-1])
report("D4 input agreement = K+5", d4)

# D5 — the kill digit
d5 = True
want_by_phase = {4: 1, 9: 2, 14: 0, 19: 0}
for K in KS[:-1]:
    da = greedy(2 * comb_T(K, Q4, 4, 5), Q4)
    db = greedy(2 * comb_T(K + 5, Q4, 4, 5), Q4)
    least = next(t for t in range(WIDTH) if da[t] != db[t])
    want = want_by_phase[K % 20]
    print(f"D5 K={K:2d} (phase {K % 20:2d}): least differing image digit {least}")
    if least != want:
        d5 = False
report("D5 kill digit (1, 2, 0, 0 by phase, bounded by 2)", d5)

# D6 — the four limit strings
d6 = True
prefixes = {}
for r in (4, 9, 14, 19):
    lows = ["".join(map(str, greedy(2 * comb_T(K, Q4, 4, 5), Q4)[:16]))
            for K in KS if K % 20 == r and K >= 20]
    stable = len(set(lows)) == 1
    prefixes[r] = lows[0]
    print(f"D6 phase {r:2d}: low-16 {lows[0]} stable {stable}")
    d6 = d6 and stable
d6 = d6 and len(set(prefixes.values())) == 4
report("D6 four distinct stable limit prefixes", d6)


# D7 — the 3-torus shadow
def quartic_roots():
    """Durand-Kerner on x^4 - x^3 - x^2 - x - 1."""
    def f(x):
        return x ** 4 - x ** 3 - x ** 2 - x - 1
    rs = [complex(0.4, 0.9) ** j for j in range(1, 5)]
    for _ in range(200):
        rs = [r - f(r) / prod_others(rs, i) for i, r in enumerate(rs)]
    return rs


def prod_others(rs, i):
    p = 1
    for j, r in enumerate(rs):
        if j != i:
            p *= rs[i] - r
    return p


roots = quartic_roots()
contracting = sorted((r for r in roots if abs(r) < 1),
                     key=lambda r: r.imag)
real_root = next(r for r in contracting if abs(r.imag) < 1e-9).real
cplx_root = next(r for r in contracting if r.imag > 1e-9)
print(f"D7 roots: real {real_root:.6f}, complex pair modulus "
      f"{abs(cplx_root):.6f}")

N = 200000
digs = [greedy(n, Q4) for n in range(N)]


def shadow_ratio(lam, t_lo, t_hi):
    """Mean depth-t cell diameter ratio between t_hi and t_lo
    (diameter by the farthest-from-centroid point — the same
    statistic at both depths, so any bias cancels in the ratio)."""
    out = []
    for t in (t_lo, t_hi):
        cells = {}
        for d in digs:
            key = d[:t]
            c = sum(bit * lam ** k for k, bit in enumerate(d) if bit)
            cells.setdefault(key, []).append(c)
        diams = []
        for cs in cells.values():
            if len(cs) < 2:
                continue
            mid = sum(cs) / len(cs)
            far = max(cs, key=lambda z: abs(z - mid))
            diams.append(max(abs(far - z) for z in cs))
        out.append(sum(diams) / len(diams))
    return out[1] / out[0]


d7 = True
for lam, name in ((complex(real_root), "real"), (cplx_root, "plane")):
    target = abs(lam) ** 5
    r1 = shadow_ratio(lam, 4, 9)
    r2 = shadow_ratio(lam, 9, 14)
    print(f"D7 {name}: ratio {r1:.5f} (t 4->9), {r2:.5f} (9->14) "
          f"vs |lambda|^5 = {target:.6f}")
    for r in (r1, r2):
        d7 = d7 and 0.7 * target <= r <= 1.3 * target
report("D7 3-torus shadow (ratios inside the band)", d7)

# D8 — the x3 identity
d8 = all(3 * Q4[k] == Q4[k + 1] + Q4[k] + Q4[k - 4] for k in range(4, 45))
report("D8 x3 keeps its copy at k", d8)


# D9 — the general theorem at d = 5, 6
def phase_set_general(d, K):
    """The general theorem's digit index set for 2 T_K at degree d."""
    i = ((K - d) // (d + 1)) % d
    if i == d - 1:
        return set(range(d, K + 2, d))
    return set(range(i + 1)) | {j for j in range(d + 1 + i, K + 2, d)
                                if j % d == (i + 1) % d}


d9 = True
for d in (5, 6):
    Qd = build_Q(d, [2 ** j for j in range(d)])
    KSd = [K for K in range(d, WIDTH - 2, d + 1)]
    for K in KSd:
        T = comb_T(K, Qd, d, d + 1)
        got = digit_set(2 * T, Qd)
        want = phase_set_general(d, K)
        if got != want:
            d9 = False
            print(f"  D9 FAIL d={d} K={K}: got {sorted(got)} "
                  f"want {sorted(want)}")
    for K in KSd[:-1]:
        T1, T2 = comb_T(K, Qd, d, d + 1), comb_T(K + d + 1, Qd, d, d + 1)
        if agree(T1, T2, Qd) != K + d + 1:
            d9 = False
            print(f"  D9 FAIL d={d} K={K}: agreement "
                  f"{agree(T1, T2, Qd)} want {K + d + 1}")
        da, db = greedy(2 * T1, Qd), greedy(2 * T2, Qd)
        least = next(t for t in range(WIDTH) if da[t] != db[t])
        if least > d - 2:
            d9 = False
            print(f"  D9 FAIL d={d} K={K}: kill digit {least} > {d - 2}")
    print(f"D9 d={d}: {len(KSd)} phase sets checked, largest "
          f"2 T_{KSd[-1]} = {2 * comb_T(KSd[-1], Qd, d, d + 1)}")
report("D9 general theorem at d = 5, 6", d9)

print(f"VERDICT all checks: {ok_all}")
sys.exit(0 if ok_all else 1)
