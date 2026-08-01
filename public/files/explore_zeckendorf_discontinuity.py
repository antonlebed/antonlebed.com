"""The odometer-not-a-ring statement proved: x2 has no continuous
extension to the Zeckendorf completion — the infinite witness family.

THE QUESTION
------------
The fourth window (explore_zeckendorf_window.py) measured the gate:
2n, 3n, 4n, n//2 unreadable at every lookahead <= 12 at every depth
<= 11 below F_26, with the deepest x2 witness pair data-capped at
input agreement 23. The unproved half: does x2 REALLY fail at every
lookahead — equivalently, does x2 extend continuously to the
completion (the golden-mean odometer)? This script carries the hand
proof that it does not, and verifies every proved statement by greedy
digit extraction in range — the rig is a CHECK on the proof, not the
evidence for it.

THE PROOF (hand-derived before any engine; conventions F_2 = 1,
F_3 = 2, F_4 = 3, ...)
----------------------
The witness spine is the STEP-3 COMB, extracted from the recorded
extremal pair rather than constructed: C_K = F_4 + F_7 + ... + F_K
for K = 4, 7, 10, ... (K = 1 mod 3). The measured extremal pair
(23183, 98208) is exactly (C_22, C_25).

LEMMA 1: 2*C_K = F_{K+2} - 2. Induction: 2*C_4 = 6 = F_6 - 2;
2*C_{K+3} = (F_{K+2} - 2) + 2 F_{K+3} = F_{K+4} + F_{K+3} - 2
= F_{K+5} - 2.

LEMMA 2 (the Zeckendorf form of F_m - 2, m >= 5): from the classical
comb sums F_3 + F_5 + ... + F_{2j+1} = F_{2j+2} - 1 and
F_2 + F_4 + ... + F_{2j} = F_{2j+1} - 1,
  m even:  F_m - 2 = F_2 + F_5 + F_7 + ... + F_{m-1}   (d_2 = 1),
  m odd :  F_m - 2 = F_4 + F_6 + ... + F_{m-1}         (d_2 = 0).
Both strings are golden; both checked at the base (F_5 - 2 = F_4,
F_6 - 2 = F_5 + F_2).

LEMMA 3 (deep agreement): C_K and C_{K+3} = C_K + F_{K+3} are both
canonical combs agreeing at every digit index < K+3: input agreement
depth K+1.

THEOREM (x2 is unreadable at every depth and every lookahead, all of
Z): d_2(2 C_K) = 1 iff K is even (Lemmas 1+2 with m = K+2), and K,
K+3 have opposite parity, so the pair (C_K, C_{K+3}) agrees to depth
K+1 while the doubles differ at the lowest digit. K is unbounded, so
no lookahead c makes depth-(t+c) agreement force even depth-1 image
agreement.
COMPLETION FORM: the strings of C_K converge in the odometer
completion to x* (the infinite step-3 comb); 2 C_K converges along
even K to the string of F_2 + (odd comb) and along odd K to the
string of (even comb) — two distinct points. A continuous g with
g|_Z = x2 would give both as g(x*). So x2 has no continuous
extension — and hence no continuous addition on the completion
extends Z's (x -> x + x would be one): the completion carries the
odometer, not a ring. The b-adic contrast: Z_b is a ring, every
integer multiplication continuous, and the trailing gate there binds
only division. This is the two-gates law's continuity form with the
Zeckendorf half now proved for x2; 3n, 4n, n//2 remain rule at
scanned scope (explore_zeckendorf_window.py F2). The x3 spine is a
real open: 3 F_k = F_{k+2} + F_{k-2} spreads instead of descending,
and the step-4 comb it suggests has 3*(F_5 + F_9 + ... + F_K) =
F_{K+3} - 1 with K = 1 mod 4 — the image parity never flips inside
one family and the two families (start 4, start 5) disagree at the
bottom, so the x3 witness family is not a comb.

THE DESIGN (checks, exhaustive where marked; greedy Zeckendorf
extraction only — no closed form from the proof enters the digit
path)
----------------------------------------------------------------
D1  Lemma 1 in range: 2*C_K == F_{K+2} - 2 for every K = 1 mod 3
    with K+2 <= 36 (integer identity, exact).
D2  Lemma 2 in range: greedy digits of F_m - 2 equal the stated comb
    for every 5 <= m <= 36.
D3  The family in range: for each K, the pair (C_K, C_{K+3}) has
    greedy input agreement depth exactly K+1 and image lowest digits
    (d_2(2 C_K), d_2(2 C_{K+3})) = (1, 0) or (0, 1) by the stated
    parity.
D4  The recorded extremal pair is the family: C_22 == 23183 and
    C_25 == 98208.
D5  The two limit strings: the low-order 12 digits of 2 C_K
    stabilize along each parity class of K to two fixed distinct
    prefixes.

RUN RECORD
----------
One run; instant, trivial memory. ALL CHECKS GREEN.

FINDINGS (post-run)
-------------------
D1, D2: zero failures over the stated ranges — both lemmas hold as
printed (K+2 <= 36; m = 5..36).
D3: every family pair K = 4..31 prints input agreement depth exactly
K+1 with image lowest digits flipping by the stated parity — pairs up
to (1762288, 7465175) at depth 32, past the first rig's data cap of
23 (explore_zeckendorf_window.py).
D4: True — the measured extremal pair is the family at K = 22.
D5: the low-12 strings of 2 C_K stabilize to (1,0,0,1,0,1,0,1,...)
along even K and (0,0,1,0,1,0,1,0,...) along odd K — the two limit
points of the theorem, distinct at d_2 (and at every position: the
strings are disjoint combs).
THE READING: the proof stands with every checkable consequence
confirmed. The odometer-not-a-ring statement is proved: x2 does not
extend continuously to the Zeckendorf completion, so the fourth
window's gate failure for x2 holds at every depth, every lookahead,
over all of Z — theorem, no range cap.
"""

import sys

F = [0, 1]
while len(F) < 60:
    F.append(F[-1] + F[-2])
# F[2] = 1, F[3] = 2, F[4] = 3, ... (F[0], F[1] unused pad)


def zeck_digits(n, width):
    """Greedy Zeckendorf digits d_2..d_{width+1}, low-to-high tuple."""
    ds = [0] * width
    k = len(F) - 1
    m = n
    while m > 0 and k >= 2:
        if F[k] <= m:
            m -= F[k]
            if k - 2 < width:
                ds[k - 2] = 1
            k -= 2
        else:
            k -= 1
    return tuple(ds)


def agree_depth(a, b, width):
    da, db = zeck_digits(a, width), zeck_digits(b, width)
    d = 0
    while d < width and da[d] == db[d]:
        d += 1
    return d


def comb_C(K):
    """C_K = F_4 + F_7 + ... + F_K (K = 1 mod 3)."""
    return sum(F[j] for j in range(4, K + 1, 3))


def lemma2_comb(m):
    """The stated Zeckendorf of F_m - 2 as a digit tuple (width m)."""
    ds = [0] * m
    if m % 2 == 0:
        ds[0] = 1                      # F_2
        for j in range(5, m, 2):       # F_5, F_7, ..., F_{m-1}
            ds[j - 2] = 1
    else:
        for j in range(4, m, 2):       # F_4, F_6, ..., F_{m-1}
            ds[j - 2] = 1
    return tuple(ds)


def main():
    ok_all = True

    # D1 — Lemma 1 in range
    bad = [K for K in range(4, 35, 3) if 2 * comb_C(K) != F[K + 2] - 2]
    print("D1 Lemma 1 (2*C_K = F_{K+2} - 2), K = 4..34 step 3: "
          "failures = %d" % len(bad))
    ok_all &= not bad

    # D2 — Lemma 2 in range
    bad = []
    for m in range(5, 37):
        got = zeck_digits(F[m] - 2, m)
        want = lemma2_comb(m)
        if got != want:
            bad.append(m)
    print("D2 Lemma 2 (Zeckendorf of F_m - 2), m = 5..36: "
          "failures = %d" % len(bad))
    ok_all &= not bad

    # D3 — the family
    print("D3 family pairs (C_K, C_{K+3}): in-depth / image d_2 flip")
    bad = 0
    for K in range(4, 32, 3):
        a, b = comb_C(K), comb_C(K + 3)
        width = K + 8
        ind = agree_depth(a, b, width)
        da = zeck_digits(2 * a, 1)[0]
        db = zeck_digits(2 * b, 1)[0]
        want_da = 1 if K % 2 == 0 else 0
        good = (ind == K + 1) and (da == want_da) and (db == 1 - want_da)
        if not good:
            bad += 1
        print("   K=%2d: pair (%9d,%10d) in-depth %2d (want %2d), "
              "d_2 images (%d,%d)%s"
              % (K, a, b, ind, K + 1, da, db, "" if good else "  <-- FAIL"))
    ok_all &= bad == 0

    # D4 — the recorded extremal pair is the family
    hit = comb_C(22) == 23183 and comb_C(25) == 98208
    print("D4 recorded extremal pair (23183, 98208) == (C_22, C_25): %s"
          % hit)
    ok_all &= hit

    # D5 — the two limit strings
    lows = {0: set(), 1: set()}
    for K in range(16, 35, 3):
        lows[K % 2].add(zeck_digits(2 * comb_C(K), 12))
    stable = len(lows[0]) == 1 and len(lows[1]) == 1
    distinct = lows[0] != lows[1]
    print("D5 low-12 strings of 2*C_K stabilize per parity: %s; "
          "the two limits distinct: %s" % (stable, distinct))
    if stable:
        print("   K even -> %s" % (sorted(lows[0])[0],))
        print("   K odd  -> %s" % (sorted(lows[1])[0],))
    ok_all &= stable and distinct

    print("ALL CHECKS: %s" % ("GREEN" if ok_all else "RED"))
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
