"""The period-2 borrow family: xa has no continuous extension to the
[0; 1, a, 1, a, ...] completion, every a >= 2 — the constant-a proof
shape carried across an alternating alphabet, no parity stripe.

THE QUESTION
------------
The constant-a theorem (explore_constant_a_borrow.py) and the
Zeckendorf theorem (explore_zeckendorf_discontinuity.py) partition
the constant-quotient line by one datum: whether legality lets the
bottom digit reach 1 (a >= 2: the digital flip at b_0) or caps it at
0 (a = 1: Zeckendorf's positional parity stripe). The period-2
window sqrt(3)-1 = [0; 1, 2, 1, 2, ...] has a_1 = 1, so its b_0 is
capped at 0 like Zeckendorf's — the suspicion at the freeze: its xm
discontinuity proof needs a parity-striped family, not the even
comb. TRANSPLANT FLAG: that expectation is imported from
Zeckendorf's constant-1 alphabet; the alternating alphabet was
hand-attacked on its own terms below, and the transplant REFUTED on
paper before any engine ran: the constant-a shape (one comb plus a
top-raised partner) survives, carried on the odd positions — the
positions whose digit cap is a rather than 1 — and the flip moves
from b_0 to b_1, the lowest position whose cap admits a nonzero
digit. The kill considered at the freeze (no telescoping comb at
period 2) also missed on paper: the odd comb telescopes through the
even-index half of the period-2 recurrence.

THE WINDOW (vocabulary re-derived from explore_ostrowski_window.py's
engine before the freeze). CF [0; a_1, a_2, ...] with a_k = 1 at odd
k and a at even k, a >= 2; the tested window W4 is a = 2. Weights
q_0 = 1, q_1 = a_1 = 1, q_k = a_k q_{k-1} + q_{k-2}. Digits by
greedy descent (largest q first); classical Ostrowski legality:
b_0 <= a_1 - 1 = 0 (b_0 identically 0), b_k <= a_{k+1} for k >= 1 —
so the caps ALTERNATE: a at odd k, 1 at even k — and b_k = a_{k+1}
forces b_{k-1} = 0. Every nonnegative integer has exactly one legal
string, the greedy one.

THE PROOF (hand-derived before any engine)
------------------------------------------
The recurrence read backwards gives a down-borrow on each half of
the period: a q_k = q_{k+1} - q_{k-1} at odd k (where a_{k+1} = a),
and q_k = q_{k+1} - q_{k-1} at even k (where a_{k+1} = 1). The
witness spine is the ODD COMB, Y_K = q_1 + q_3 + ... + q_K for odd
K >= 1 — the comb supported where the alphabet reaches a.

LEMMA 1 (telescope): a Y_K = q_{K+1} - 1. Summing the odd-k
down-borrow over the comb: (q_2 - q_0) + (q_4 - q_2) + ... +
(q_{K+1} - q_{K-1}) = q_{K+1} - q_0 = q_{K+1} - 1.

LEMMA 1' (the even-side telescope): q_K - 1 = q_2 + q_4 + ... +
q_{K-1} for odd K (empty at K = 1). Summing q_j = q_{j+1} - q_{j-1}
over even j = 2..K-1 gives q_K - q_1 = q_K - 1.

LEMMA 2 (the two image strings, by legality + uniqueness):
  (a) q_{K+1} - 1 = a q_1 + a q_3 + ... + a q_K (the odd a-COMB,
      digit a at odd positions 1..K). Proof: the sum is a Y_K,
      Lemma 1; the string is legal (every a sits at its cap over a
      0 at the even position below it). Bottom digits b_0 = 0,
      b_1 = a.
  (b) q_{K+1} + a q_K - 1 = q_{K+2} + (a-2) q_K + (q_K - 1), since
      q_{K+2} = q_{K+1} + q_K (K+2 odd), and q_K - 1 is Lemma 1's
      even comb. The MIXED STRING (1 at even positions 2..K-1,
      a - 2 at K, 1 at K+2) is legal: each even-position 1 sits at
      its cap over a 0 at the odd position below it, b_K = a - 2
      < a, b_{K+2} = 1 <= a. Bottom digits b_0 = 0, b_1 = 0.
      At a = 2 the K-digit vanishes and the string is the even
      1-comb plus the lone 1 at K+2; at K = 1 the even comb is
      empty (a(Y_1 + q_1) = 2a = q_3 + (a-2) q_1).

LEMMA 3 (deep agreement): Y_K and Y_K + q_K are both legal strings
(the comb's 1s violate nothing; raising b_K from 1 to 2 is legal
because 2 <= a — this is where a >= 2 enters — and at a = 2, where
2 = a forces, b_{K-1} = 0 holds at the even position below)
agreeing at every digit index < K: input agreement depth K,
differing only at b_K (1 vs 2).

THEOREM (xa is unreadable at every depth and every lookahead, and
has no continuous extension to the [0; 1, a, 1, a, ...] completion,
EVERY a >= 2): a Y_K has b_1 = a and a (Y_K + q_K) = q_{K+1} +
a q_K - 1 has b_1 = 0 (Lemmas 1 + 2; a Y_K + a q_K = q_{K+1} - 1 +
q_{K+1} - q_{K-1} = q_{K+1} + a q_K - 1 by the down-borrow at K).
The pair (Y_K, Y_K + q_K) agrees to depth K while the images differ
at the LOWEST non-vacuous digit (b_0 is identically 0 at this
window): b_1 = a against b_1 = 0 for K >= 3, and a against a - 2
at the K = 1 edge, where Lemma 2(b)'s K-digit sits at position 1 —
distinct in every case. K unbounded. COMPLETION FORM: the strings of Y_K and
Y_K + q_K converge to the infinite odd 1-comb y*; a Y_K converges
to the infinite odd a-comb (0, a, 0, a, ...) and a (Y_K + q_K) to
the infinite even 1-comb (0, 0, 1, 0, 1, ...) — two distinct
points, so no continuous g with g|_Z = xa exists, and no continuous
addition on the completion extends Z's. WHAT THE ALTERNATION
CHANGES: not the family shape (one comb, top-raised partner — the
constant-a mechanism) but the flip's ADDRESS: the a_1 = 1 half of
the alphabet squeezes b_0 to 0 exactly as at Zeckendorf, yet no
parity stripe appears — the flip relocates to b_1, the lowest
position whose cap admits a nonzero digit. The map killed is xa
with a the LARGE quotient; other integer multiplications at this
window stay rule at scanned scope (explore_ostrowski_window.py).

THE DESIGN (checks, greedy extraction only — no closed form from
the proof enters the digit path; a in {2, 3, 4, 5, 6, 7}, odd
K = 1..41 throughout; predictions frozen: every check green, D4's
extremal scan at the tested window landing on the family)
----------------------------------------------------------------
D0  Positive control per a: greedy digits reconstruct n exactly
    and are legal (b_0 = 0, alternating caps, every cap digit over
    a 0), all n < 100000.
D1  Lemmas 1 and 1' in range: a * Y_K == q_{K+1} - 1, and the even
    comb sums to q_K - 1 (exact integers).
D2  Lemma 2 in range: greedy digits of q_{K+1} - 1 equal the
    stated odd a-comb, and greedy digits of q_{K+1} + a q_K - 1
    equal the stated mixed string.
D3  The family in range: each pair (Y_K, Y_K + q_K) is legal with
    greedy input agreement depth exactly K and image digits at
    position 1 equal to (a, 0) for K >= 3, (a, a - 2) at K = 1.
D4  The tested window's extremal anchor (a = 2 only): recompute
    the window rig's extremal-witness scan (sorted digit strings,
    consecutive pairs, deepest input agreement with images
    differing at b_1) over n < 100000. PREDICTION (frozen): the
    extremal depth is 17 — the recorded witness depth at this
    window and range — and the family pair (Y_17, Y_17 + q_17) =
    (55385, 95930) realizes it; whether the scan's own argmax IS
    the family pair is printed as an observable.
D5  The two limit strings per a: the low-order 12 digits of
    a Y_K and of a (Y_K + q_K) stabilize to two fixed distinct
    prefixes — the odd a-comb and the even 1-comb.

RESOURCE: instant, trivial memory (digit tuples below 10^7 rows
never held; per-a loops are O(N) with N = 100000).

RUN RECORD
----------
Two runs: the first found D3's K = 1 check mis-specified against
its own Lemma 2(b) — at K = 1 the (a-2)-digit sits at position 1,
so the image pair there is (a, a-2), not (a, 0); the check was
aligned with the lemma (and the theorem's edge stated) and the rig
rerun, all other output byte-identical. Seconds, trivial memory.
ALL CHECKS GREEN, every a.

FINDINGS (post-run)
-------------------
D0: zero reconstruction failures, zero legality failures, every
a in {2..7}, n < 100000 (the positive control, printed before any
verdict was read).
D1, D2: zero failures at every a over odd K = 1..41 — both
telescopes and both image strings hold exactly as stated.
D3: every family pair at every a prints input agreement depth
exactly K with image b_1 digits (a, 0) (K >= 3; (a, a-2) at the
K = 1 edge as stated); deepest pairs at K = 41 per a, e.g. a = 2:
(404358569165, 700369586270) at agreement depth 41.
D4: the extremal scan at the tested window (a = 2, n < 100000)
prints depth 17 — the window rig's recorded witness depth at this
range — and the family pair (55385, 95930) = (Y_17, Y_17 + q_17)
realizes it with image flip (2, 0). The scan's own argmax printed
(55384, 95929), the family pair translated by -1: subtracting 1
changes both members' low digits identically (their low windows
are the same comb), so the translate ties at depth 17 and the sort
order breaks the tie — the frozen depth-17 prediction landed, the
argmax-identity observable printed False for that reason.
D5: at every a the low-12 prefixes stabilize to (0, a, 0, a, ...)
and (0, 0, 1, 0, 1, ...) — the two limit points, distinct at b_1
(and at every position past: the odd a-comb against the even
1-comb, disjoint supports).
THE READING: the proof stands with every checkable consequence
confirmed at six alphabets. xa has no continuous extension to the
[0; 1, a, 1, a, ...] completion for EVERY a >= 2 — theorem, no
range cap: the flip is unconditional in both K and a, and the
tested window sqrt(3)-1 is the a = 2 instance. The parity-stripe
expectation was a transplant and it REFUTED: the alternating
alphabet keeps the constant-a proof shape (one comb, top-raised
partner) on the positions whose cap is a, and the a_1 = 1
degeneracy relocates the flip from b_0 to b_1 instead of forcing
a stripe. The map proved discontinuous is xa with a the large
quotient; other integer multiplications at these windows stay
rule at scanned scope (explore_ostrowski_window.py).
"""

import sys


def make_Q(a, count=60):
    """Weights at [0; 1, a, 1, a, ...]: q_0 = 1, q_1 = 1,
    q_k = a_k q_{k-1} + q_{k-2} with a_k = 1 (k odd), a (k even)."""
    Q = [1, 1]
    while len(Q) < count:
        k = len(Q)
        ak = a if k % 2 == 0 else 1
        Q.append(ak * Q[-1] + Q[-2])
    return Q


def cap(k, a):
    """Digit cap at position k: a_{k+1} = a for odd k, 1 for even
    k >= 2; b_0 <= a_1 - 1 = 0."""
    if k == 0:
        return 0
    return a if k % 2 == 1 else 1


def digits(n, Q, a, width):
    """Greedy digits b_0..b_{width-1}, low-to-high tuple. Greedy
    maintains m < Q[k+1] at position k; caps and the cap-over-0
    rule are re-checked in legal(), not assumed."""
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
    if ds[0] != 0:
        return False
    for k in range(1, len(ds)):
        if ds[k] > cap(k, a):
            return False
        if ds[k] == cap(k, a) and ds[k] > 0 and ds[k - 1] != 0:
            return False
    return True


def agree_depth(x, y):
    d = 0
    while d < len(x) and d < len(y) and x[d] == y[d]:
        d += 1
    return d


def Y(K, Q):
    """The odd comb q_1 + q_3 + ... + q_K, K odd."""
    return sum(Q[j] for j in range(1, K + 1, 2))


def a_comb_string(K, a, width):
    """Lemma 2(a): digit a at odd positions 1..K."""
    ds = [0] * width
    for j in range(1, K + 1, 2):
        ds[j] = a
    return tuple(ds)


def mixed_string(K, a, width):
    """Lemma 2(b): 1 at even positions 2..K-1, a-2 at K, 1 at
    K+2."""
    ds = [0] * width
    for j in range(2, K, 2):
        ds[j] = 1
    ds[K] = a - 2
    ds[K + 2] = 1
    return tuple(ds)


def main():
    W = 46  # digit width, enough for K = 41 images at K+2
    ALPHAS = [2, 3, 4, 5, 6, 7]
    KS = list(range(1, 42, 2))

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

        # D1 — Lemmas 1 and 1'
        f1 = [K for K in KS if a * Y(K, Q) != Q[K + 1] - 1]
        f1b = [K for K in KS
               if sum(Q[j] for j in range(2, K, 2)) != Q[K] - 1]
        print("a=%d D1 Lemma 1 (a*Y_K = q_{K+1} - 1) and 1' (even "
              "comb = q_K - 1), odd K = 1..41: %d + %d failures"
              % (a, len(f1), len(f1b)))

        # D2 — Lemma 2
        f2 = []
        for K in KS:
            if digits(Q[K + 1] - 1, Q, a, W) != a_comb_string(K, a, W):
                f2.append((K, "a"))
            if digits(Q[K + 1] + a * Q[K] - 1, Q, a, W) \
                    != mixed_string(K, a, W):
                f2.append((K, "b"))
        print("a=%d D2 Lemma 2 (odd a-comb / mixed string), odd "
              "K = 1..41: %d failures %s"
              % (a, len(f2), f2 if f2 else ""))

        # D3 — the family
        f3 = []
        for K in KS:
            u, v = Y(K, Q), Y(K, Q) + Q[K]
            du, dv = digits(u, Q, a, W), digits(v, Q, a, W)
            if not (legal(du, a) and legal(dv, a)):
                f3.append((K, "legality"))
                continue
            if agree_depth(du, dv) != K:
                f3.append((K, "depth", agree_depth(du, dv)))
            iu, iv = digits(a * u, Q, a, W), digits(a * v, Q, a, W)
            want = (a, 0) if K >= 3 else (a, a - 2)
            if (iu[1], iv[1]) != want:
                f3.append((K, "b_1", iu[1], iv[1]))
        deep = (Y(41, Q), Y(41, Q) + Q[41])
        print("a=%d D3 family (legal, depth K, image b_1 = (a, 0)), "
              "odd K = 1..41: %d failures %s; deepest pair %s"
              % (a, len(f3), f3 if f3 else "", deep))

        # D5 — the two limit prefixes
        pre_u = set()
        pre_v = set()
        for K in KS[10:]:
            u, v = Y(K, Q), Y(K, Q) + Q[K]
            pre_u.add(digits(a * u, Q, a, W)[:12])
            pre_v.add(digits(a * v, Q, a, W)[:12])
        stable = len(pre_u) == 1 and len(pre_v) == 1 \
            and pre_u != pre_v
        print("a=%d D5 limit prefixes (low-12, K = 21..41): "
              "stable+distinct = %s  %s vs %s"
              % (a, stable, sorted(pre_u), sorted(pre_v)))

    # D4 — the tested window's extremal anchor (a = 2)
    a = 2
    Q = make_Q(a)
    N = 100000
    T = 22
    rows = sorted(range(N), key=lambda n: digits(n, Q, a, T))
    best = (-1, None)
    for i in range(N - 1):
        u, v = rows[i], rows[i + 1]
        du, dv = digits(u, Q, a, T), digits(v, Q, a, T)
        iu, iv = digits(2 * u, Q, a, T), digits(2 * v, Q, a, T)
        if iu[1] != iv[1]:
            d = agree_depth(du, dv)
            if d > best[0]:
                best = (d, (u, v))
    fam = (Y(17, Q), Y(17, Q) + Q[17])
    fu, fv = digits(fam[0], Q, a, T), digits(fam[1], Q, a, T)
    fdep = agree_depth(fu, fv)
    fflip = (digits(2 * fam[0], Q, a, T)[1],
             digits(2 * fam[1], Q, a, T)[1])
    print("D4 a=2 extremal scan (n < %d): depth %d, pair %s; "
          "family pair %s: depth %d, image b_1 %s; scan argmax "
          "is the family pair: %s"
          % (N, best[0], best[1], fam, fdep, fflip,
             tuple(sorted(best[1])) == fam))


if __name__ == "__main__":
    sys.exit(main())
