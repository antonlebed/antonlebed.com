"""The constant-a borrow family: xa has no continuous extension to
the constant-a completion, every a >= 2 — the silver proof template
generalized.

THE QUESTION
------------
The silver leg (explore_silver_discontinuity.py) proved x2
discontinuous on the silver completion [0; 2, 2, ...] via the even
Pell comb and the down-borrow 2 q_k = q_{k+1} - q_{k-1}. Neither
proof leg consulted the conjugate — both run on the recurrence
identity a q_k = q_{k+1} - q_{k-1}, which holds at EVERY constant-a
window [0; a, a, ...]. Does the template generalize: is xa proved
discontinuous at every constant-a window, or does the bottom-digit
flip fail at some a — the a = 2 flip an accident of the small
alphabet? The open piece is the a-analog of the mixed-string lemma.
TRANSPLANT FLAG: the entire slate is imported from a = 2, storey-up
in the alphabet parameter; every lemma is re-derived at general a
below, none assumed.

THE PROOF (hand-derived before any engine; weights q_0 = 1,
q_1 = a, q_k = a q_{k-1} + q_{k-2}; legal digits b_0 <= a - 1,
b_k <= a for k >= 1, b_k = a forces b_{k-1} = 0 — classical
Ostrowski legality at [0; a, a, ...], every nonnegative integer
having exactly one legal string, the greedy one)
------------------------------------------------------------------
The witness spine is the same EVEN COMB, Y_K = q_2 + q_4 + ... +
q_K for even K >= 2. The down-borrow a q_k = q_{k+1} - q_{k-1} is
the recurrence read backwards and is the whole engine.

LEMMA 1 (telescope): a Y_K = q_{K+1} - a. Summing the down-borrow
over the comb: (q_3 - q_1) + (q_5 - q_3) + ... + (q_{K+1} -
q_{K-1}) = q_{K+1} - q_1 = q_{K+1} - a.

LEMMA 2 (the two image strings, by legality + uniqueness):
  (a) q_{K+1} - a = a q_K + a q_{K-2} + ... + a q_2 (the a-COMB,
      digit a at even positions 2..K). Proof: the sum telescopes
      to q_{K+1} - a by Lemma 1's computation; the string is legal
      (every a sits over a 0 at the odd position below it;
      b_0 = 0). Bottom digit b_0 = 0.
  (b) q_{K+1} + a q_K - a = q_{K+1} + (a-1) q_K + (q_K - a), and
      q_K - a = q_0 + (a-1) q_1 + a (q_3 + q_5 + ... + q_{K-1}):
      the odd comb telescopes, a (q_3 + ... + q_{K-1}) = q_K - q_2
      = q_K - a^2 - 1, and q_0 + (a-1) q_1 = 1 + a^2 - a supplies
      the difference. The MIXED STRING (b_0 = 1, b_1 = a - 1,
      a at odd positions 3..K-1, a - 1 at K, 1 at K + 1) is legal:
      b_0 = 1 <= a - 1 (this is where a >= 2 enters), every digit
      a sits over a 0 at the even position below it, and
      b_K = a - 1 < a forces nothing. Bottom digit b_0 = 1.
      At a = 2 this is digit-for-digit the silver mixed string;
      at K = 2 the a-run is empty (b_0 = 1, b_1 = a - 1,
      b_2 = a - 1, b_3 = 1, summing to 2 a^3 + 2 a).

LEMMA 3 (deep agreement): Y_K and Y_K + q_K are both legal strings
(the comb's 1s violate nothing; raising b_K from 1 to 2 is legal
because 2 <= a and, at a = 2 where 2 = a forces, b_{K-1} = 0
holds) agreeing at every digit index < K: input agreement depth K,
differing only at b_K (1 vs 2).

THEOREM (xa is unreadable at every depth and every lookahead, and
has no continuous extension to the constant-a completion, EVERY
a >= 2): a Y_K has b_0 = 0 and a (Y_K + q_K) = q_{K+1} + a q_K - a
has b_0 = 1 (Lemmas 1 + 2; a Y_K + a q_K = q_{K+1} - a + q_{K+1} -
q_{K-1} = q_{K+1} + a q_K - a by the down-borrow at K). The pair
(Y_K, Y_K + q_K) agrees to depth K while the images differ at the
LOWEST digit, K unbounded. COMPLETION FORM: the strings of Y_K and
Y_K + q_K converge to the infinite even comb y*; a Y_K converges
to the infinite a-comb (b_0 = 0) and a (Y_K + q_K) to the mixed
tail (1, a-1, 0, a, 0, a, ...) (b_0 = 1) — two distinct points, so
no continuous g with g|_Z = xa exists, and no continuous addition
on the completion extends Z's. The flip is unconditional in BOTH K
and a: the kill-shape (the flip failing at some a) misses
everywhere. WHERE THE FAMILY DEGENERATES: a = 1 exactly — legality
caps b_0 <= 0, so the mixed string's b_0 = 1 is illegal there, and
the golden storey instead runs Zeckendorf's parity-striped comb
(explore_zeckendorf_discontinuity.py): the parity stripe appears
precisely where the constant-a family's bottom digit is squeezed
out.

THE DESIGN (checks, greedy extraction only — no closed form from
the proof enters the digit path; a in {2, 3, 4, 5, 6, 7}, even
K = 2..40 throughout; predictions frozen: every check green, D4
reproducing the silver rig's recorded family pair)
----------------------------------------------------------------
D0  Positive control per a: greedy digits reconstruct n exactly
    and are legal (b_0 <= a - 1, b_k <= a, every a over a 0),
    all n < 100000.
D1  Lemma 1 in range: a * Y_K == q_{K+1} - a (exact integers).
D2  Lemma 2 in range: greedy digits of q_{K+1} - a equal the
    stated a-comb, and greedy digits of q_{K+1} + a q_K - a equal
    the stated mixed string.
D3  The family in range: each pair (Y_K, Y_K + q_K) has greedy
    input agreement depth exactly K and image bottom digits
    (b_0(a Y_K), b_0(a Y_K + a q_K)) = (0, 1).
D4  a = 2 is the silver family: Y_12 == 40390 and
    Y_12 + q_12 == 73851 (the window rig's recorded extremal
    pair, explore_silver_discontinuity.py D4).
D5  The two limit strings per a: the low-order 12 digits of
    a Y_K and of a (Y_K + q_K) stabilize to two fixed distinct
    prefixes — the a-comb prefix and the mixed tail.

RUN RECORD
----------
One run; instant, trivial memory. ALL CHECKS GREEN, every a.

FINDINGS (post-run)
-------------------
D0: zero reconstruction failures, zero legality failures, every
a in {2..7}, n < 100000 (the positive control, printed before any
verdict was read).
D1, D2: zero failures at every a over even K = 2..40 — the
telescope and both image strings hold exactly as stated.
D3: every family pair at every a prints input agreement depth
exactly K with image bottom digits (0, 1); deepest pairs at K = 40
per a, e.g. a = 7: (14067900399457664191313908208018199,
27859853481012721953299858477318548) at agreement depth 40.
D4: True on both — the a = 2 family at K = 12 is the silver rig's
recorded extremal pair (40390, 73851).
D5: at every a the low-12 prefixes stabilize to
(0, 0, a, 0, a, ...) and (1, a-1, 0, a, 0, a, ...) — the two limit
points, distinct at b_0 (and at b_1, and at every position past:
offset a-combs).
THE READING: the proof stands with every checkable consequence
confirmed at six alphabets. xa has no continuous extension to the
constant-a completion for EVERY a >= 2 — theorem, no range cap, no
per-a caveat: the storey's odometer verdict now rests on a proved
cell at every constant-a window rather than at silver alone. The
kill-shape missed everywhere; the a = 2 flip was the general
mechanism, not an accident of the small alphabet. The one
degeneracy is a = 1, where legality squeezes the mixed string's
bottom digit out and the Zeckendorf parity stripe takes over.
"""

import sys


def make_Q(a, count=60):
    Q = [1, a]
    while len(Q) < count:
        Q.append(a * Q[-1] + Q[-2])
    return Q


def digits(n, Q, a, width):
    """Greedy Ostrowski digits b_0..b_{width-1} at [0;a,a,...],
    low-to-high tuple. Greedy maintains m < Q[k+1] at position k,
    so the caps and the a-over-0 rule hold by construction; both
    are re-checked, not assumed."""
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


def legal(ds, a):
    if ds[0] > a - 1:
        return False
    for k in range(1, len(ds)):
        if ds[k] > a:
            return False
        if ds[k] == a and ds[k - 1] != 0:
            return False
    return True


def agree_depth(x, y):
    d = 0
    while d < len(x) and d < len(y) and x[d] == y[d]:
        d += 1
    return d


def Y(K, Q):
    return sum(Q[j] for j in range(2, K + 1, 2))


def a_comb_string(K, a, width):
    """Lemma 2(a): digit a at even positions 2..K."""
    ds = [0] * width
    for j in range(2, K + 1, 2):
        ds[j] = a
    return tuple(ds)


def mixed_string(K, a, width):
    """Lemma 2(b): b_0 = 1, b_1 = a-1, a at odd 3..K-1, a-1 at K,
    1 at K+1."""
    ds = [0] * width
    ds[0] = 1
    ds[1] = a - 1
    for j in range(3, K, 2):
        ds[j] = a
    ds[K] = a - 1
    ds[K + 1] = 1
    return tuple(ds)


def main():
    W = 46  # digit width, enough for K = 40 images
    ALPHAS = [2, 3, 4, 5, 6, 7]

    for a in ALPHAS:
        Q = make_Q(a)

        # D0 — positive control
        bad = 0
        for n in range(100000):
            ds = digits(n, Q, a, 30)
            if sum(d * Q[k] for k, d in enumerate(ds)) != n \
                    or not legal(ds, a):
                bad += 1
        print("a=%d D0 control (reconstruct + legality, n < 100000): "
              "%d failures" % (a, bad))

        # D1 — Lemma 1
        f1 = [K for K in range(2, 41, 2) if a * Y(K, Q) != Q[K + 1] - a]
        print("a=%d D1 Lemma 1 (a*Y_K = q_{K+1} - a), even K = 2..40: "
              "%d failures" % (a, len(f1)))

        # D2 — Lemma 2
        f2 = []
        for K in range(2, 41, 2):
            if digits(Q[K + 1] - a, Q, a, W) != a_comb_string(K, a, W):
                f2.append((K, "a"))
            if digits(Q[K + 1] + a * Q[K] - a, Q, a, W) \
                    != mixed_string(K, a, W):
                f2.append((K, "b"))
        print("a=%d D2 Lemma 2 (a-comb / mixed string), even K = 2..40: "
              "%d failures %s" % (a, len(f2), f2 if f2 else ""))

        # D3 — the family
        f3 = []
        deepest = None
        for K in range(2, 41, 2):
            u, v = Y(K, Q), Y(K, Q) + Q[K]
            du, dv = digits(u, Q, a, W), digits(v, Q, a, W)
            if not (legal(du, a) and legal(dv, a)):
                f3.append((K, "legality"))
                continue
            if agree_depth(du, dv) != K:
                f3.append((K, "depth", agree_depth(du, dv)))
            iu, iv = digits(a * u, Q, a, W), digits(a * v, Q, a, W)
            if (iu[0], iv[0]) != (0, 1):
                f3.append((K, "bottom", iu[0], iv[0]))
            deepest = (K, u, v)
        print("a=%d D3 family (agreement K, image bottoms (0,1)): "
              "%d failures %s" % (a, len(f3), f3 if f3 else ""))
        print("a=%d D3 deepest pair: K=%d (%d, %d)"
              % (a, deepest[0], deepest[1], deepest[2]))

        # D5 — the two limit strings
        lows_u = {tuple(digits(a * Y(K, Q), Q, a, W)[:12])
                  for K in range(24, 41, 2)}
        lows_v = {tuple(digits(a * (Y(K, Q) + Q[K]), Q, a, W)[:12])
                  for K in range(24, 41, 2)}
        stable = len(lows_u) == 1 and len(lows_v) == 1 \
            and lows_u != lows_v
        print("a=%d D5 limit prefixes stable+distinct: %s  %s | %s"
              % (a, stable, sorted(lows_u), sorted(lows_v)))
        print()

    # D4 — a = 2 is the silver family
    Q2 = make_Q(2)
    print("D4 silver cross-check: Y_12 == 40390: %s, "
          "Y_12 + q_12 == 73851: %s"
          % (Y(12, Q2) == 40390, Y(12, Q2) + Q2[12] == 73851))


if __name__ == "__main__":
    sys.exit(main())
