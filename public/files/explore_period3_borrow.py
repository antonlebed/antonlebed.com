"""The period-3 borrow chain at [0; 1, 1, a, ...]: does any comb
telescope when the borrow's span mismatches the comb's spacing — and
what carries the discontinuity when it does?

THE QUESTION
------------
The proved discontinuity cells so far live where the down-borrow's
span MATCHES the witness comb's spacing: constant-a windows (span 2,
comb step 2 — explore_constant_a_borrow.py) and period-2 windows
(same span, the odd comb — explore_period2_borrow.py). At period 3
the largest quotient's positions are 3 apart while its borrow
a q_k = q_{k+1} - q_{k-1} still spans 2: no single identity
telescopes a comb, and the intermediate quotients' own rewrites must
CHAIN. The window here is the smallest period-3 alphabet holding a
large quotient: [0; 1, 1, a, 1, 1, a, ...], tested a = 2..7, with
the map xa (a the large quotient) the one on trial.

THE WINDOW (vocabulary re-derived from explore_ostrowski_window.py's
engine before the freeze). Tail (1, 1, a): a_k = tail[(k-1) mod 3],
so a_1 = a_2 = 1, a_3 = a, repeating. Weights q_0 = 1, q_1 = a_1 = 1,
q_k = a_k q_{k-1} + q_{k-2}. Digits by greedy descent; classical
Ostrowski legality: b_0 <= a_1 - 1 = 0 (b_0 identically 0),
b_k <= a_{k+1} = cap(k) for k >= 1 — cap 1 at k = 0, 1 (mod 3),
cap a at k = 2 (mod 3) — and b_k = cap(k) forces b_{k-1} = 0.

THE HAND-ATTACK (pre-engine, on paper; the a = 2 chain full, the
a >= 3 shape numeric at M <= 4)
------------------------------------------------------------------
TRANSPLANT FLAGS, both resolved on paper before the engine: (i) the
comb-at-the-cap-positions intuition imported from period 2 (the comb
supported where the alphabet reaches a) REFUTED — at period 3 that
comb doubles digit-wise (2 <= cap), its partner's difference is
pushed UP, and the family is READ at delay ~3; (ii) the parity-
stripe expectation imported from Zeckendorf, refuted at period 2,
RETURNS at this window's a = 2: the witness family's image flips by
the PARITY OF THE COMB LENGTH.

The witness comb lives at the a_k = a positions' NEIGHBORS — the
positions k = 0 (mod 3), where cap(k) = 1: u_M = q_3 + q_6 + ... +
q_{3M}, legal (each 1 sits at its cap over a 0). The three doubling
identities (a = 2): 2 q_K = q_{K+1} - q_{K-1} at K = 2 (mod 3) (the
true borrow), 2 q_K = q_{K+1} + q_{K-2} at K = 1 (mod 3), and
2 q_K = q_{K+1} + q_{K-1} + q_{K-2} at K = 0 (mod 3) (legal
spreads). Every comb-extension step u_M -> u_{M+1} triggers a full
cascade to the bottom (checked by hand at M = 1..4: the overflow
rewrites 2 q_K = q_{K+1} + q_{K-2}, 3 q_K = q_{K+1} + q_{K-2} at
K = 2 (mod 3), and the bottom absorption 2 q_2 + q_1 = q_3 chain
through every digit), flipping the whole image string between two
parity classes.

LEMMA 1 (blockwise doubles, from the period's recurrences):
  (a) 2 q_3 = q_1 + q_2 + q_4;
  (b) 2 (q_{6i} + q_{6i+3}) = q_{6i} + 2 q_{6i+2} + q_{6i+4}
      [via 2 q_{6i+3} = q_{6i+4} + q_{6i+2} + q_{6i+1} and
       q_{6i+1} + q_{6i} = q_{6i+2}];
  (c) 2 (q_{6i-3} + q_{6i}) = q_{6i-3} + 2 q_{6i-1} + q_{6i+1}
      [via q_{6i} = 3 q_{6i-1} - q_{6i-3}, itself from the two
       unit-quotient recurrences].
LEMMA 2 (the two image forms, by summing Lemma 1's blocks +
legality + uniqueness):
  odd M:  2 u_M = q_1 + q_2 + q_4
          + sum_{i=1}^{(M-1)/2} (q_{6i} + 2 q_{6i+2} + q_{6i+4}),
  even M: 2 u_M = sum_{i=1}^{M/2}
          (q_{6i-3} + 2 q_{6i-1} + q_{6i+1}),
  both legal, both topped at 3M + 1; disjoint digit supports above
  position 2 (even positions + {1, 2} against odd positions >= 3).
LEMMA 3 (the family): u_M is legal, u_{M+1} = u_M + q_{3M+3}, and
the strings agree at every position < 3M + 3.
THEOREM (a = 2): the pairs (u_M, u_{M+1}) agree to depth 3M + 3 —
unbounded — while the images 2 u_M and 2 u_{M+1} differ at b_1
(1 for odd M, 0 for even M): x2 is unreadable at every depth and
lookahead, and has no continuous extension to the [0; 1, 1, 2, ...]
completion. COMPLETION FORM: u_M converges to the infinite comb at
the 0 (mod 3) positions; the odd-M and even-M image subsequences
converge to two distinct limit strings — one convergent input
sequence whose image sequence does not converge. The flip
address is b_1, the lowest position whose cap admits a nonzero
digit — the storey's flip-address conjecture holds at this window.

THE a >= 3 SHAPE (hand numerics at M <= 4, the slate's predictions
below): the K = 0 (mod 3) spread generalizes to a q_K = q_{K+1} +
(a-2) q_K + (a-1) q_{K-1} + q_{K-2} — for a >= 3 an (a-2)-tooth
survives AT each input tooth, and the hand numerics split by the
parity of a: at a = 3 and a = 5 the image bottom FREEZES (the comb
family is READ); at a = 4 the bottom STRIPES by M parity at b_2
((1, 2) against (1, 3)). Only a = 2 vanishes the (a-2)-tooth and
relocates the flip to b_1.

THE DESIGN (checks; greedy extraction only — no closed form from
the proof enters the digit path; predictions frozen before the run)
------------------------------------------------------------------
D0  Positive control per a in {2..7}: greedy digits reconstruct n
    exactly and are legal (b_0 = 0, the alternating caps, every cap
    digit over a 0), all n < 100000.
D1  (a = 2) Lemma 1 exact over i = 1..12; Lemma 2's closed forms
    equal the greedy digits of 2 u_M for M = 1..26; Lemma 3's
    agreement depth exactly 3M + 3 with image b_1 pair (1, 0) at
    odd M and (0, 1) at even M. PREDICTION: all green.
D2  (a = 2) The two limit prefixes: the low-12 digits of 2 u_M
    stabilize per parity class to two fixed distinct prefixes,
    differing at b_1. PREDICTION: green.
D3  (odd a: 3, 5, 7) The comb image's low-3 digits (b_0, b_1, b_2)
    across M = 1..26. PREDICTION (from the a = 3, 5 hand numerics;
    a = 7 is the out-of-sample test): frozen at (0, 1, (a+1)/2) at
    every M — the family is read, no flip. The low-8 prefixes per
    parity class print as observables.
D4  (even a: 4, 6) The same low-3 digits. PREDICTION: a stripe by
    M parity at b_2 — (0, 1, 2) against (0, 1, 3) at a = 4 (hand);
    a = 6 stripes with values printed as observables.
D5  (the gate scan; kills freeze as prints) Windows a = 2, 3, 4,
    map xa, N in {30000, 100000, 300000}: CAP(N) = deepest realized
    consecutive-pair input agreement (sorted digit strings), and
    A(N) = deepest such agreement among pairs whose image low-3
    prefixes differ. PREDICTION: at a = 2 and a = 4 (a flip family
    exists) A(N) tracks CAP(N) within a few. At a = 3 the print IS
    the finding: A tracking CAP reads as the gate binding with the
    witness family still unknown; A FROZEN while CAP rises >= 3
    reads as a readable plateau — the unit-gate conjecture refuted
    at this window (a = 3 is not a unit there: norm 9).

RESOURCE: estimate ~2-3 min (the D5 sorts at N = 300000 dominate),
well under 512MB (digit strings as bytes, ~10 MB per window at the
largest N).

RUN RECORD
----------
One run, all checks green, every prediction landed. About two
minutes, trivial memory.

FINDINGS (post-run)
-------------------
D0: zero reconstruction failures, zero legality failures, every
a in {2..7}, n < 100000 (the positive control, printed before any
verdict was read).
D1: zero failures — Lemma 1 exact at i = 1..12, both closed forms
equal the greedy digits of 2 u_M at every M = 1..26, every family
pair prints agreement depth exactly 3M + 3 with image b_1 flip
(1, 0) / (0, 1) by parity.
D2: the low-12 image prefixes stabilize to (0,1,1,0,1,0,1,0,2,0,1,0)
(odd M) against (0,0,0,1,0,2,0,1,0,1,0,2) (even M) — distinct at
b_1, disjoint supports above position 2.
D3: the odd-a freeze CONFIRMED, including the out-of-sample a = 7:
low-3 frozen at (0, 1, (a+1)/2) at every M — (0,1,2) at a = 3,
(0,1,3) at a = 5, (0,1,4) at a = 7 — and the low-8 prefixes are
IDENTICAL across the parity classes ((0,1,(a+1)/2,0,0,0,1,0) both):
the comb family is READ at odd a, no flip anywhere in the low
window.
D4: the even-a stripe CONFIRMED: b_2 flips between a/2 and a/2 + 1
((0,1,2)/(0,1,3) at a = 4, (0,1,3)/(0,1,4) at a = 6), and the low-8
classes are stable and distinct in more than b_2 (odd M
(0,1,a/2,0,1,0,1,0) against even M (0,1,a/2+1,0,0,a,0,1)) — the
comb family carries a parity flip at EVERY tested even a, at b_1
for a = 2 and at b_2 for a >= 4.
D5: A(N) tracks CAP(N) within 1 at every window and every N
(a = 2: caps 17/19/21, A 16/19/20; a = 3: 14/17/18, A 14/16/18;
a = 4: 14/15/17, A 14/15/17) — the gate binds at all three tested
period-3 windows, no readable plateau; the kill missed.

THE READING: the borrow CHAIN exists and the discontinuity survives
the span mismatch — with a new carrier. At [0; 1, 1, 2, ...] the
theorem stands complete (the lemma chain above, every check green):
x2 has no continuous extension, and the flip is carried by the
PARITY OF THE COMB LENGTH — Zeckendorf's stripe mechanism, returned
one storey up, with the flip's address still the lowest position
whose cap admits a nonzero digit (b_1). The parity of a splits the
window family: at even a the comb family flips (b_2 by M parity,
values a/2 against a/2 + 1 — pattern at a = 4, 6, M <= 26), at odd
a it is read with a frozen bottom (0, 1, (a+1)/2) (pattern at
a = 3, 5, 7) — yet the gate still binds at a = 3 by the range scan
(rule at scanned scope): whatever witnesses the a = 3 discontinuity
is not this comb, and finding it is the open leg. The derived half
of the mechanism: the K = 0 (mod 3) spread keeps an (a-2)-tooth at
each input tooth for a >= 3, so only a = 2 lets the cascade
restructure the whole string; why the surviving tooth's
neighborhood still stripes at even a and freezes at odd a is not
derived here — the open leg's first question.

SETTLED SINCE (pointer; the record above is frozen): the a = 3
witness question closed via the certified boundary family
(explore_max_string_witness.py, explore_class_criterion.py), and
the parity split is now a theorem at all a — the absorption lemma
and the closed forms on both sides live in
explore_odd_a_freeze.py.
"""

import sys


def make_Q(a, count=90):
    """Weights at [0; 1, 1, a, ...]: q_0 = q_1 = 1, q_k = a_k q_{k-1}
    + q_{k-2}, a_k = a at k = 0 (mod 3), else 1."""
    Q = [1, 1]
    while len(Q) < count:
        k = len(Q)
        ak = a if k % 3 == 0 else 1
        Q.append(ak * Q[-1] + Q[-2])
    return Q


def cap(k, a):
    """Digit cap at position k: a_{k+1} = a at k = 2 (mod 3), else 1;
    b_0 <= a_1 - 1 = 0."""
    if k == 0:
        return 0
    return a if k % 3 == 2 else 1


def digits(n, Q, width):
    """Greedy digits b_0..b_{width-1}, low-to-high tuple."""
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


def U(M, Q):
    """The comb q_3 + q_6 + ... + q_{3M}."""
    return sum(Q[3 * m] for m in range(1, M + 1))


def odd_form(M, Q):
    """Lemma 2, odd M: value and digit string."""
    W = 3 * M + 6
    ds = [0] * W
    ds[1] = ds[2] = ds[4] = 1
    for i in range(1, (M - 1) // 2 + 1):
        ds[6 * i] = 1
        ds[6 * i + 2] = 2
        ds[6 * i + 4] = 1
    return sum(d * Q[k] for k, d in enumerate(ds)), tuple(ds)


def even_form(M, Q):
    """Lemma 2, even M: value and digit string."""
    W = 3 * M + 6
    ds = [0] * W
    for i in range(1, M // 2 + 1):
        ds[6 * i - 3] = 1
        ds[6 * i - 1] = 2
        ds[6 * i + 1] = 1
    return sum(d * Q[k] for k, d in enumerate(ds)), tuple(ds)


def main():
    MS = list(range(1, 27))

    # D0 — positive control, every a
    for a in [2, 3, 4, 5, 6, 7]:
        Q = make_Q(a)
        bad = 0
        for n in range(100000):
            ds = digits(n, Q, 40)
            if sum(d * Q[k] for k, d in enumerate(ds)) != n \
                    or not legal(ds, a):
                bad += 1
        print("a=%d D0 control (reconstruct + legality, n < 100000): "
              "%d failures" % (a, bad))

    # D1 — the a = 2 lemma chain
    a = 2
    Q = make_Q(a)
    W = 90
    f1 = []
    for i in range(1, 13):
        if 2 * Q[3] != Q[1] + Q[2] + Q[4]:
            f1.append((i, "a"))
        if 2 * (Q[6 * i] + Q[6 * i + 3]) != \
                Q[6 * i] + 2 * Q[6 * i + 2] + Q[6 * i + 4]:
            f1.append((i, "b"))
        if 2 * (Q[6 * i - 3] + Q[6 * i]) != \
                Q[6 * i - 3] + 2 * Q[6 * i - 1] + Q[6 * i + 1]:
            f1.append((i, "c"))
    print("D1 Lemma 1 (blockwise doubles), i = 1..12: %d failures %s"
          % (len(f1), f1 if f1 else ""))

    f2 = []
    for M in MS:
        u = U(M, Q)
        val, form = (odd_form if M % 2 else even_form)(M, Q)
        gd = digits(2 * u, Q, len(form))
        if val != 2 * u:
            f2.append((M, "value"))
        if gd != form or not legal(gd, a):
            f2.append((M, "string"))
    print("D1 Lemma 2 (closed forms = greedy digits of 2u_M), "
          "M = 1..26: %d failures %s" % (len(f2), f2 if f2 else ""))

    f3 = []
    for M in MS[:-1]:
        u, v = U(M, Q), U(M + 1, Q)
        du, dv = digits(u, Q, W), digits(v, Q, W)
        if not (legal(du, a) and legal(dv, a)):
            f3.append((M, "legality"))
            continue
        if agree_depth(du, dv) != 3 * M + 3:
            f3.append((M, "depth", agree_depth(du, dv)))
        iu, iv = digits(2 * u, Q, W), digits(2 * v, Q, W)
        want = (1, 0) if M % 2 else (0, 1)
        if (iu[1], iv[1]) != want:
            f3.append((M, "b_1", iu[1], iv[1]))
    print("D1 Lemma 3 + theorem (family depth 3M+3, image b_1 flip), "
          "M = 1..25: %d failures %s" % (len(f3), f3 if f3 else ""))

    # D2 — the two limit prefixes (a = 2)
    pre = {0: set(), 1: set()}
    for M in MS[12:]:
        pre[M % 2].add(digits(2 * U(M, Q), Q, W)[:12])
    stable = len(pre[0]) == 1 and len(pre[1]) == 1 and pre[0] != pre[1]
    print("D2 limit prefixes (low-12, M = 13..26): stable+distinct = "
          "%s  odd %s vs even %s"
          % (stable, sorted(pre[1]), sorted(pre[0])))

    # D3/D4 — the a >= 3 comb bottoms
    for a in [3, 5, 7, 4, 6]:
        Q = make_Q(a)
        lows = [digits(a * U(M, Q), Q, W)[:3] for M in MS]
        prefs = {0: set(), 1: set()}
        for M in MS[12:]:
            prefs[M % 2].add(digits(a * U(M, Q), Q, W)[:8])
        tag = "D3" if a % 2 else "D4"
        print("%s a=%d comb-image low-3 across M = 1..26: %s"
              % (tag, a, sorted(set(lows))))
        print("   low-8 per parity class (M = 13..26): odd %s even %s"
              % (sorted(prefs[1]), sorted(prefs[0])))

    # D5 — the gate scan
    for a in [2, 3, 4]:
        Q = make_Q(a)
        print("D5 window a=%d, map x%d:" % (a, a))
        for N in (30000, 100000, 300000):
            T = 40
            strs = [bytes(digits(n, Q, T)) for n in range(N)]
            order = sorted(range(N), key=lambda i: strs[i])
            pref = []
            for j in range(N - 1):
                s1, s2 = strs[order[j]], strs[order[j + 1]]
                p = 0
                while p < T and s1[p] == s2[p]:
                    p += 1
                pref.append(p)
            capN = max(pref)
            imgs = [bytes(digits(a * n, Q, 3)) for n in range(N)]
            A = -1
            for j in range(N - 1):
                if imgs[order[j]] != imgs[order[j + 1]] \
                        and pref[j] > A:
                    A = pref[j]
            print("   N = %6d: CAP %2d  A(x%d) %2d" % (N, capN, a, A))


if __name__ == "__main__":
    sys.exit(main())
