"""The silver borrow family: x2 has no continuous extension to the
silver (Pell) completion — the third storey's proof leg.

THE QUESTION
------------
The third-storey rig (explore_ostrowski_window.py) measured the gate
at four quadratic Ostrowski windows: every tested integer m >= 2 is
unreadable at bounded delay, with witness depth tracking the
exhaustive cap across three ranges. The unproved half at the silver
window alpha = sqrt(2) - 1 = [0; 2, 2, 2, ...]: does x2 REALLY fail
at every lookahead — equivalently, does x2 extend continuously to
the silver completion? This script carries the hand proof that it
does not, and verifies every proved statement by greedy digit
extraction in range — the rig is a CHECK on the proof, not the
evidence for it. The template is the Zeckendorf leg
(explore_zeckendorf_discontinuity.py); the mechanism differs:
subtraction (a down-BORROW) where Zeckendorf's was a down-carry.

THE PROOF (hand-derived before any engine; weights q_0 = 1, q_1 = 2,
q_k = 2 q_{k-1} + q_{k-2} — the Pell denominators 1, 2, 5, 12, 29,
70, ...; legal digits b_0 <= 1, b_k <= 2 for k >= 1, b_k = 2 forces
b_{k-1} = 0; every nonnegative integer has exactly one legal string,
the greedy one — classical Ostrowski uniqueness)
------------------------------------------------------------------
The witness spine is the EVEN COMB, extracted from the recorded
extremal pair rather than constructed: Y_K = q_2 + q_4 + ... + q_K
for even K >= 2. The measured extremal pair (40390, 73851) of the
window rig is exactly (Y_12, Y_12 + q_12). The down-borrow identity
2 q_k = q_{k+1} - q_{k-1} (the a = 2 case of the recurrence read
backwards) is the whole engine of the proof.

LEMMA 1 (telescope): 2 Y_K = q_{K+1} - 2. Summing the down-borrow
over the comb: 2 Y_K = (q_3 - q_1) + (q_5 - q_3) + ... +
(q_{K+1} - q_{K-1}) = q_{K+1} - q_1.

LEMMA 2 (the two image strings, by legality + uniqueness):
  (a) q_{K+1} - 2 = 2 q_K + 2 q_{K-2} + ... + 2 q_2 (the 2-comb,
      even positions 2..K). Proof: the sum telescopes to
      q_{K+1} - q_1 by Lemma 1's computation; the string is legal
      (every 2 sits over a 0 at the odd position below it; b_0 = 0).
      Bottom digit b_0 = 0.
  (b) q_{K+1} + 2 q_K - 2 = q_{K+1} + q_K + 2(q_{K-1} + q_{K-3} +
      ... + q_3) + q_1 + q_0. Proof: the inner odd comb telescopes,
      2(q_3 + ... + q_{K-1}) = q_K - q_2, so the right side is
      q_{K+1} + 2 q_K - q_2 + q_1 + q_0 = q_{K+1} + 2 q_K - 2. The
      string (b_0 = 1, b_1 = 1, 2 at odd positions 3..K-1, 1 at K
      and K+1) is legal: b_0 = 1 <= 1, every 2 sits over a 0 at the
      even position below it, b_K = 1. Bottom digit b_0 = 1.
      (At K = 2 the 2-run is empty: q_3 + q_2 + q_1 + q_0 = 20.)

LEMMA 3 (deep agreement): Y_K and Y_K + q_K are both legal strings
(the comb's 1s violate nothing; raising b_K from 1 to 2 is legal
because b_{K-1} = 0) agreeing at every digit index < K: input
agreement depth K, differing only at b_K (1 vs 2).

THEOREM (x2 is unreadable at every depth and every lookahead, all
of Z): 2 Y_K has b_0 = 0 and 2 (Y_K + q_K) = q_{K+1} + 2 q_K - 2
has b_0 = 1 (Lemmas 1 + 2; 2 Y_K + 2 q_K = q_{K+1} - 2 + q_{K+1} -
q_{K-1} = q_{K+1} + 2 q_K - 2 by the down-borrow at K). So the pair
(Y_K, Y_K + q_K) agrees to depth K while the doubles differ at the
LOWEST digit — and K is unbounded, so no lookahead c makes
depth-(t+c) agreement force even depth-1 image agreement. Unlike
the Zeckendorf comb, no parity condition enters: the flip is
unconditional at every even K.
COMPLETION FORM: the strings of Y_K and of Y_K + q_K both converge
in the completion to y* (the infinite even comb — the differing
digit marches to infinity); 2 Y_K converges to the infinite 2-comb
(b_0 = 0) and 2 (Y_K + q_K) to the Lemma 2(b) tail (b_0 = 1) — two
distinct points. A continuous g with g|_Z = x2 would give both as
g(y*). So x2 has no continuous extension — and hence no continuous
addition on the silver completion extends Z's (x -> x + x would be
one): the completion carries the odometer, not a ring. The borrow
mechanism, against Zeckendorf's carry: doubling a comb term injects
-q_{k-1}, a SUBTRACTION rewriting lower positions, where the
Zeckendorf mechanism 2 F_k = F_{k+1} + F_{k-2} was an additive
down-carry. Both proofs run entirely on the recurrence identity
a q_k = q_{k+1} - q_{k-1}; the conjugate enters neither explicitly.
The maps 3n, n//2 at silver, and all gated maps at the bronze and
period-2 windows, remain rule at scanned scope
(explore_ostrowski_window.py F2).

THE DESIGN (checks, exhaustive where marked; greedy silver
extraction only — no closed form from the proof enters the digit
path; predictions frozen: every check green)
----------------------------------------------------------------
D0  Positive control: greedy digits reconstruct n exactly and are
    legal (b_0 <= 1, b_k <= 2, every 2 over a 0), all n < 200000.
D1  Lemma 1 in range: 2 * Y_K == q_{K+1} - 2 for every even K with
    K + 1 <= 41 (integer identity, exact).
D2  Lemma 2 in range: greedy digits of q_{K+1} - 2 equal the stated
    2-comb, and greedy digits of q_{K+1} + 2 q_K - 2 equal the
    stated mixed string, every even K = 2..40.
D3  The family in range: for each even K = 2..40, the pair
    (Y_K, Y_K + q_K) has greedy input agreement depth exactly K and
    image bottom digits (b_0(2 Y_K), b_0(2 Y_K + 2 q_K)) = (0, 1).
D4  The recorded extremal pair is the family: Y_12 == 40390 and
    Y_12 + q_12 == 73851.
D5  The two limit strings: the low-order 12 digits of 2 Y_K and of
    2 (Y_K + q_K) stabilize to two fixed distinct prefixes.

RUN RECORD
----------
One run; instant, trivial memory. ALL CHECKS GREEN.

FINDINGS (post-run)
-------------------
D0: zero reconstruction failures, zero legality failures, n < 200000
(the positive control, printed before any verdict was read).
D1, D2: zero failures over the stated ranges — both lemmas hold as
printed (even K = 2..40).
D3: every family pair K = 2..40 prints input agreement depth exactly
K with image bottom digits (0, 1) — the deepest pair
(2108646576008244, 3855506596076653) at agreement depth 40, far past
the window rig's exhaustive cap of 14 at N = 300000
(explore_ostrowski_window.py E6).
D4: True — the measured extremal pair is the family at K = 12.
D5: the low-12 strings of 2 Y_K stabilize to (0,0,2,0,2,0,2,...) and
of 2 (Y_K + q_K) to (1,1,0,2,0,2,0,...) — the two limit points of
the theorem, distinct at b_0 (and at every position past b_1: the
tails are offset 2-combs).
THE READING: the proof stands with every checkable consequence
confirmed. The silver cell of the third storey is proved: x2 does
not extend continuously to the silver completion, so the window
gate's failure for x2 at silver holds at every depth, every
lookahead, over all of Z — theorem, no range cap. The down-borrow
family is simpler than Zeckendorf's: one comb, no parity stripe,
the flip unconditional.
"""

import sys

Q = [1, 2]
while len(Q) < 60:
    Q.append(2 * Q[-1] + Q[-2])
# Q[0] = 1, Q[1] = 2, Q[2] = 5, ... (Pell denominators)


def silver_digits(n, width):
    """Greedy Ostrowski digits b_0..b_{width-1} for [0;2,2,...],
    low-to-high tuple. Greedy maintains m < Q[k+1] at position k, so
    the caps and the 2-over-0 rule hold by construction; both are
    re-checked, not assumed."""
    ds = [0] * width
    m = n
    for k in range(len(Q) - 1, -1, -1):
        if Q[k] <= m:
            c = m // Q[k]
            if k < width:
                ds[k] = c
            m -= c * Q[k]
    assert m == 0
    return tuple(ds)


def legal(ds):
    if ds[0] > 1:
        return False
    for k in range(1, len(ds)):
        if ds[k] > 2:
            return False
        if ds[k] == 2 and ds[k - 1] != 0:
            return False
    return True


def agree_depth(a, b):
    d = 0
    while d < len(a) and d < len(b) and a[d] == b[d]:
        d += 1
    return d


def Y(K):
    return sum(Q[j] for j in range(2, K + 1, 2))


def comb_string(K, width):
    """Lemma 2(a): 2 at even positions 2..K."""
    ds = [0] * width
    for j in range(2, K + 1, 2):
        ds[j] = 2
    return tuple(ds)


def mixed_string(K, width):
    """Lemma 2(b): b_0 = b_1 = 1, 2 at odd 3..K-1, 1 at K, K+1."""
    ds = [0] * width
    ds[0] = 1
    ds[1] = 1
    for j in range(3, K, 2):
        ds[j] = 2
    ds[K] = 1
    ds[K + 1] = 1
    return tuple(ds)


def main():
    W = 46  # digit width, enough for K = 40 images

    # D0 — positive control
    bad = 0
    for n in range(200000):
        ds = silver_digits(n, 30)
        if sum(d * Q[k] for k, d in enumerate(ds)) != n or not legal(ds):
            bad += 1
    print("D0 control (reconstruct + legality, n < 200000): "
          "%d failures" % bad)

    # D1 — Lemma 1
    f1 = [K for K in range(2, 41, 2) if 2 * Y(K) != Q[K + 1] - 2]
    print("D1 Lemma 1 (2*Y_K = q_{K+1} - 2), even K = 2..40: "
          "%d failures" % len(f1))

    # D2 — Lemma 2
    f2 = []
    for K in range(2, 41, 2):
        if silver_digits(Q[K + 1] - 2, W) != comb_string(K, W):
            f2.append((K, "a"))
        if silver_digits(Q[K + 1] + 2 * Q[K] - 2, W) != mixed_string(K, W):
            f2.append((K, "b"))
    print("D2 Lemma 2 (strings of q_{K+1}-2 and q_{K+1}+2q_K-2): "
          "%d failures %s" % (len(f2), f2 if f2 else ""))

    # D3 — the family
    f3 = []
    for K in range(2, 41, 2):
        x, y = Y(K), Y(K) + Q[K]
        dx, dy = silver_digits(x, W), silver_digits(y, W)
        ix, iy = silver_digits(2 * x, W), silver_digits(2 * y, W)
        if agree_depth(dx, dy) != K or (ix[0], iy[0]) != (0, 1):
            f3.append(K)
    print("D3 family (agreement K, image b_0 = (0,1)), even K = 2..40: "
          "%d failures %s" % (len(f3), f3 if f3 else ""))
    print("   deepest pair: (%d, %d) at agreement depth %d"
          % (Y(40), Y(40) + Q[40], 40))

    # D4 — the recorded extremal pair
    print("D4 recorded pair is the family at K = 12: %s"
          % (Y(12) == 40390 and Y(12) + Q[12] == 73851))

    # D5 — the two limit strings
    lows_x = {silver_digits(2 * Y(K), W)[:12] for K in range(26, 41, 2)}
    lows_y = {silver_digits(2 * (Y(K) + Q[K]), W)[:12]
              for K in range(26, 41, 2)}
    print("D5 low-12 of doubles stabilize: %s; distinct: %s"
          % (len(lows_x) == 1 and len(lows_y) == 1,
             lows_x.isdisjoint(lows_y)))
    print("   2*Y_K   -> %s" % str(sorted(lows_x)[0]))
    print("   2*(Y+q) -> %s" % str(sorted(lows_y)[0]))


if __name__ == "__main__":
    main()
