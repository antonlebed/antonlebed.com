"""The fourth shape's not-a-ring half proved: x2 has no continuous
extension to the Tribonacci completion — the step-4 comb family.

THE QUESTION
------------
The completion atlas (explore_completion_atlas.py) realized the
fourth completion shape at the trailing Tribonacci window and left
one piece at rule tier: x2 torn at every scanned agreement depth
through 17, mechanism the down-carry 2q_k = q_{k+1} + q_{k-3}, with
the extremal pairs (93684, 63562 and neighbours) seeding a hand comb
family LEFT OPEN. The Zeckendorf template
(explore_zeckendorf_discontinuity.py): a step-3 comb whose double is
one Fibonacci minus 2, the image's lowest digit flipping with the
comb's parity — two limit points over one input limit. Does the
Tribonacci down-carry, descending three where Zeckendorf's descends
two, close the same way? This script carries the hand proof that it
does — with THREE image limit points instead of two — and verifies
every proved statement by greedy digit extraction in range; the rig
is a CHECK on the proof, not the evidence for it.

THE PROOF (hand-derived before any engine; conventions q_0 = 1,
q_1 = 2, q_2 = 4, q_k = q_{k-1} + q_{k-2} + q_{k-3}; digits d_k at
place q_k, low index first)
---------------------------
LEMMA 0 (canonicity): a 0/1 digit string with no "111" factor is
THE greedy expansion of its value. First, any 111-free string on
indices < k sums to <= q_k - 1: among its top three indices
k-1, k-2, k-3 at least one is absent, and the three cases give
sums <= q_{k-1} - 1, q_{k-1} + q_{k-2} - 1, and
q_{k-1} + q_{k-2} + q_{k-3} - 1 = q_k - 1 by induction (bases
k = 0, 1, 2: sums 0, 1, 3 = q_k - 1). So a 111-free string with top
index t has value n with q_t <= n <= q_{t+1} - 1, greedy takes q_t,
and the remainder recurses: greedy reproduces the string. Corollary:
distinct 111-free strings have distinct values.

LEMMA A (the down-carry): 2 q_k = q_{k+1} + q_{k-3} for k >= 3
(2 q_k = q_{k+1} + (q_k - q_{k-1} - q_{k-2}) = q_{k+1} + q_{k-3});
boundary: 2 q_0 = q_1, 2 q_1 = q_2, 2 q_2 = q_3 + q_0; and the base
consolidation q_0 + q_1 + q_2 = q_3 (1 + 2 + 4 = 7).

THE WITNESS SPINE is the STEP-4 COMB, the step the carry's descent
by three dictates: T_K = q_3 + q_7 + q_11 + ... + q_K, K = 3 mod 4.

THEOREM (three-phase image): the canonical digits of 2 T_K are the
step-3 comb with top tooth K+1 and a bottom that cycles with period
12 in K:
  K = 3  mod 12:  {0} u {j = 1 mod 3 : 4 <= j <= K+1}
  K = 7  mod 12:  {0, 1} u {j = 2 mod 3 : 5 <= j <= K+1}
  K = 11 mod 12:  {j = 0 mod 3 : 3 <= j <= K+1}
Bases (exact integers): 2 T_3 = 14 = q_4 + q_0; 2 T_7 = 176 =
q_8 + q_5 + q_1 + q_0; 2 T_11 = 2030 = q_12 + q_9 + q_6 + q_3.
Step K -> K+4: 2 T_{K+4} = 2 T_K + q_{K+5} + q_{K+1} (Lemma A on
2 q_{K+4}). The added q_{K+1} doubles the image's top tooth, and the
down-carry cascades down the comb — teeth spaced three, the carry
descending three: each 2 q_j = q_{j+1} + q_{j-3} deposits q_{j+1}
(fresh: deposits sit at j+1 = K+2 mod 3, remaining teeth at K+1 mod
3, disjoint) and re-doubles the tooth three below, so every tooth
shifts up one. The bottom closes the cycle: phase 11's bottom tooth
3 splits (2 q_3 = q_4 + q_0) opening phase 3's {0}; phase 3's bottom
tooth 4 splits (2 q_4 = q_5 + q_1), q_1 joining q_0 as phase 7's
{0, 1}; phase 7's bottom tooth 5 splits (2 q_5 = q_6 + q_2) and
q_0 + q_1 + q_2 consolidates to q_3, phase 11's bottom. Each result
is 111-free (teeth spaced three; the {0,1} pair sits below a gap),
hence canonical by Lemma 0.

CONSEQUENCE (the kill, unconditional in K): T_K and T_{K+4} are both
canonical step-4 combs agreeing at every digit index < K+4 — input
agreement K+4, unbounded — while the images' lowest digits read off
the phases: d_0 = 1, 1, 0 at K = 3, 7, 11 mod 12 and d_1 = 0, 1, 0.
So consecutive pairs' images differ at digit 0 (K = 7, 11 mod 12) or
digit 1 (K = 3 mod 12): a bounded digit at unbounded agreement.
COMPLETION FORM: the strings of T_K converge in the completion to
x* (the infinite step-4 comb); the strings of 2 T_K converge along
each phase class to the three infinite step-3 combs with bottoms
{0}, {0,1}, {3} — distinct at digit 0 or 1. A continuous g with
g|_Z = x2 would give all three as g(x*). So x2 has no continuous
extension — and hence no continuous addition on the completion
extends Z's (x -> x + x would be one): the fourth shape's
not-a-ring half is a THEOREM, no range cap. x3 and the floor
divisions remain rule at scanned scope (explore_completion_atlas.py
F4); the Zeckendorf x3 lesson (the spread carry 3F_k = F_{k+2} +
F_{k-2} defeats the comb) transplants untested here [TRANSPLANT:
3 q_k = q_{k+1} + q_{k-1} - q_{k-3} is not even a positive sum].

THE DESIGN (checks, greedy extraction only — no closed form from
the proof enters the digit path)
--------------------------------
D0  CONTROL (cross-rig, index conventions): the atlas's recorded
    extremal pair (93684, 63562) prints greedy agreement 17 and
    image (doubles) agreement 4 — the atlas's own ia = 17, im = 4.
D1  Lemma A in range: the down-carry at every 3 <= k < 45, the
    three boundary identities, the base consolidation (exact).
D2  Lemma 0's bound in range: max 111-free sum on indices < k
    equals q_k - 1, exhaustive over bitmasks for k <= 20.
D3  The theorem in range: greedy digits of 2 T_K equal the stated
    phase set for every K = 3, 7, ..., 43.
D4  Input agreement: greedy agreement of (T_K, T_{K+4}) is exactly
    K+4 for every K in range.
D5  The kill digit: the least digit where the images of consecutive
    pairs differ is 1 for K = 3 mod 12, else 0 — bounded by 1 at
    every K.
D6  The three limit strings: the low-16 digits of 2 T_K are
    constant on each phase class for K >= 15 and pairwise distinct
    across the classes.

PREDICTIONS, frozen before the engine
-------------------------------------
P1  D0 prints 17 and 4.
P2  D1 exact, zero failures.
P3  D2 exact at every k <= 20.
P4  D3 exact at every K — the three-phase table as stated.
P5  D4 exactly K+4 at every K.
P6  D5 least differing digit 1 at K = 3 mod 12, 0 otherwise.
P7  D6 three stable, pairwise distinct prefixes.

FINDINGS (entered after the run; prints copied from the run record)
--------------------------------------------------------------------
F1  THE CONTROL MATCHES THE ATLAS: (93684, 63562) prints input
    agreement 17, image agreement 4 (P1 met — the rig speaks the
    atlas's index conventions).
F2  LEMMA A EXACT: down-carry zero failures at 3 <= k < 45; the
    three boundary identities and the consolidation exact (P2 met).
F3  LEMMA 0'S BOUND EXACT: max 111-free sum on indices < k equals
    q_k - 1 at every k <= 20, exhaustive over all 2^k masks
    (P3 met).
F4  THE THREE-PHASE THEOREM EXACT IN RANGE: greedy digits of 2 T_K
    equal the stated phase set at every K = 3, 7, ..., 43 — eleven
    values, phases cycling 3 -> 7 -> 11 -> 3 (P4 met). The largest
    checked: 2 T_43 = 597858019470, the phase-7 comb
    {0, 1, 5, 8, ..., 44}.
F5  INPUT AGREEMENT EXACTLY K+4 at every pair (T_K, T_{K+4}) in
    range (P5 met) — past the atlas's scan ceiling of 17 by K = 39
    onward, unbounded by the theorem.
F6  THE KILL DIGIT AS STATED: least differing image digit 1 at
    K = 3 mod 12, 0 at K = 7, 11 mod 12 — never above 1 (P6 met).
F7  THE THREE LIMIT STRINGS, distinct and stable: low-16 digits
    1000100100100100 (phase 3), 1100010010010010 (phase 7),
    0001001001001001 (phase 11) — pairwise distinct already at
    digit 0 or 1, the theorem's three limit points printed (P7
    met).

RUN RECORD
----------
One run, all seven checks green first try, VERDICT True on every
line; wall 0.57s (the D2 bitmask sweep dominates), trivial memory.
"""

import sys

# ---------------------------------------------------------------- tribonacci
Q = [1, 2, 4]
while len(Q) < 60:
    Q.append(Q[-1] + Q[-2] + Q[-3])

WIDTH = 50


def greedy(n):
    """Greedy digits d_0..d_{WIDTH-1}, low index first."""
    d = [0] * WIDTH
    for k in range(len(Q) - 1, -1, -1):
        if Q[k] <= n:
            if k < WIDTH:
                d[k] = 1
            n -= Q[k]
    assert n == 0
    return tuple(d)


def agree(a, b):
    da, db = greedy(a), greedy(b)
    t = 0
    while t < WIDTH and da[t] == db[t]:
        t += 1
    return t


def comb_T(K):
    """T_K = q_3 + q_7 + ... + q_K (K = 3 mod 4)."""
    return sum(Q[j] for j in range(3, K + 1, 4))


def phase_set(K):
    """The theorem's predicted digit index set for 2 T_K."""
    r = K % 12
    if r == 3:
        return {0} | set(range(4, K + 2, 3))
    if r == 7:
        return {0, 1} | set(range(5, K + 2, 3))
    return set(range(3, K + 2, 3))


def digit_set(n):
    return {k for k, bit in enumerate(greedy(n)) if bit}


ok_all = True


def report(label, ok):
    global ok_all
    ok_all = ok_all and ok
    print(f"{label}: {ok}")


# D0 — cross-rig control on the atlas's extremal pair
ia = agree(93684, 63562)
im = agree(2 * 93684, 2 * 63562)
print(f"D0 control: input agreement {ia}, image agreement {im}")
report("D0", ia == 17 and im == 4)

# D1 — Lemma A
d1 = all(2 * Q[k] == Q[k + 1] + Q[k - 3] for k in range(3, 45))
d1 = d1 and 2 * Q[0] == Q[1] and 2 * Q[1] == Q[2]
d1 = d1 and 2 * Q[2] == Q[3] + Q[0] and Q[0] + Q[1] + Q[2] == Q[3]
report("D1 down-carry + boundaries", d1)

# D2 — Lemma 0's bound, exhaustive
d2 = True
for k in range(1, 21):
    best = 0
    for mask in range(1 << k):
        if mask & (mask << 1) & (mask << 2):
            continue
        s = sum(Q[j] for j in range(k) if mask >> j & 1)
        best = max(best, s)
    if best != Q[k] - 1:
        d2 = False
        print(f"  D2 FAIL at k={k}: max {best} vs {Q[k] - 1}")
report("D2 max 111-free sum = q_k - 1 (k <= 20)", d2)

# D3 — the three-phase theorem
KS = list(range(3, 44, 4))
d3 = True
for K in KS:
    got = digit_set(2 * comb_T(K))
    want = phase_set(K)
    if got != want:
        d3 = False
        print(f"  D3 FAIL at K={K}: got {sorted(got)} want {sorted(want)}")
print(f"D3 largest: 2 T_43 = {2 * comb_T(43)}")
report("D3 three-phase image (K = 3..43)", d3)

# D4 — input agreement exactly K+4
d4 = all(agree(comb_T(K), comb_T(K + 4)) == K + 4 for K in KS[:-1])
report("D4 input agreement = K+4", d4)

# D5 — the kill digit
d5 = True
for K in KS[:-1]:
    da = greedy(2 * comb_T(K))
    db = greedy(2 * comb_T(K + 4))
    least = next(t for t in range(WIDTH) if da[t] != db[t])
    want = 1 if K % 12 == 3 else 0
    print(f"D5 K={K:2d} (phase {K % 12:2d}): least differing image digit {least}")
    if least != want:
        d5 = False
report("D5 kill digit (1 at K=3 mod 12, else 0)", d5)

# D6 — the three limit strings
d6 = True
prefixes = {}
for r in (3, 7, 11):
    lows = ["".join(map(str, greedy(2 * comb_T(K))[:16]))
            for K in KS if K % 12 == r and K >= 15]
    stable = len(set(lows)) == 1
    prefixes[r] = lows[0]
    print(f"D6 phase {r:2d}: low-16 {lows[0]} stable {stable}")
    d6 = d6 and stable
d6 = d6 and len(set(prefixes.values())) == 3
report("D6 three distinct stable limit prefixes", d6)

print(f"VERDICT all checks: {ok_all}")
sys.exit(0 if ok_all else 1)
