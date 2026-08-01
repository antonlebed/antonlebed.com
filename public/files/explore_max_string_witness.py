"""The max-string witness at [0; 1, 1, a, ...]: does the string of
q_K - 1 carry the discontinuity the odd-a comb cannot?

THE QUESTION
------------
At the period-3 windows [0; 1, 1, a] with ODD a the = 0 mod 3 comb
is READ (image bottom frozen — explore_period3_borrow.py D3) while
the gate scan says xa is still gated (D5): whatever witnesses the
discontinuity is another family. The candidate here, found by hand:
q_K - 1, the largest integer whose legal string is supported below
position K — its string is the maximal legal filling below K, and
the shape of that filling depends on the PARITY of K. If integers
y_K = (q_K - 1)/a exist with converging strings (one mod-a class of
the convergent pair (q_K, p_K), both K-parities represented), the
family (y_K) is one convergent input sequence whose images q_K - 1
land on two distinct bottoms by the parity of K: xa discontinuous,
no comb involved, the parity of a never consulted.

THE WINDOW (vocabulary identical to explore_period3_borrow.py's
engine): tail (1, 1, a), q_0 = q_1 = 1, q_k = a_k q_{k-1} + q_{k-2}
with a_k = a at k = 0 (mod 3) else 1; caps b_0 = 0, cap 1 at
k = 0, 1 (mod 3), cap a at k = 2 (mod 3); b_k = cap(k) forces
b_{k-1} = 0.

THE HAND-ATTACK (pre-engine, on paper, a = 3)
------------------------------------------------------------------
Dead candidates first: the cap-position comb q_2 + q_5 + ... maps
to the digit-wise triple (read outright); its top-raised partner's
image defect climbs AWAY from the bottom as M grows (checked at
M <= 5); the = 1 mod 3 comb's image bottom freezes at (0, 0, 1).
Every local perturbation's image defect is absorbed upward — the
a = 2 down-cascade needed the vanished (a-2)-tooth.

The live candidate: q_K - 1. Hand values at a = 3 — q_7 - 1 = 72 =
(0,0,3,0,1,0,1), q_9 - 1 = 462 = (0,0,3,0,1,0,1,0,3), q_11 - 1 =
1055 = (0,0,3,0,1,0,1,0,3,0,1) at odd K, against q_6 - 1 = 56 =
(0,1,0,1,0,3), q_14 - 1 = 8577 = (0,1,0,1,0,3,0,1,0,1,0,3,0,1),
q_16 - 1 = 39128 at even K: bottom (b_1, b_2) = (0, 3) at odd K,
(1, 0) at even K. Periodic patterns (period 6): odd K carries
(3, 1, 1) on the even positions from b_2, even K carries (1, 1, 3)
on the odd positions from b_1.

LEMMA 1 (blocks; one-line consequences of the recurrences, every
a >= 2):
  (even) q_{6i+1} + q_{6i+3} + a q_{6i+5} = q_{6i+6} - q_{6i}
         [expand q_{6i+6} down through the two unit quotients];
  (odd)  a q_{6i+2} + q_{6i+4} + q_{6i+6} = q_{6i+7} - q_{6i+1}
         [the true borrow a q_k = q_{k+1} - q_{k-1} at k = 2 mod 3
          plus q_{6i+7} = q_{6i+6} + q_{6i+5}].
LEMMA 2 (telescope): summing Lemma 1's blocks from i = 0, with
q_0 = q_1 = 1, lands exactly on q_{6j} - 1 and q_{6j+1} - 1; the
four remaining K mod 6 classes each add one truncated top block.
Both patterns are legal (support on one parity of position, every
cap digit over a forced 0), so by uniqueness of the legal string
they ARE the strings of q_K - 1. Hand-verified sums at a = 3:
1 + 7 + 48 = 56 = q_6 - 1; 56 + 73 + 463 + 3168 = 3760 = q_12 - 1;
6 + 9 + 57 = 72 = q_7 - 1; 72 + 390 + 593 + 3761 = 4816 = q_13 - 1.

THE INPUT SIDE: y_K = (q_K - 1)/a needs a | q_K - 1, and one
convergent input family needs the pair (q_K, p_K) mod a fixed —
{y_K theta} ~ (p_K - theta)/a mod 1, so a fixed class converges to
one point while the side alternates with the convergent's sign
(-1)^K. At a = 3 the class (q, p) = (1, 2) mod 3 holds K = 7, 9
(odd) and 14 (even): y_7 = 24 = (0,1,0,1,0,1), y_9 = 154 =
(0,1,0,1,0,1,0,0,1), y_14 = 2859 = (0,1,0,1,0,1,0,0,1,0,1,2) —
prefixes extending, images 72, 462, 8577 splitting at b_1. The
(q, p) mod a orbit is periodic (finite state), so an even period
makes every class member recur with its parity: both parities
forever.

THE DESIGN (checks; greedy extraction only — no closed form enters
the digit path; predictions frozen before the run)
------------------------------------------------------------------
D0  Positive control per a in {2..7}: greedy digits reconstruct n
    exactly and are legal, all n < 100000.
D1  (all a in {2..7}, K = 3..40) The greedy string of q_K - 1
    equals the Lemma 2 periodic pattern for K's class mod 6, and
    the bottom (b_1, b_2) is (1, 0) at even K, (0, a) at odd K.
    PREDICTION: all green (derived; theorem-shaped).
D2  (a in {2..7}) The (q_K, p_K) mod a orbit: period of the pair
    sequence, and the class q = 1 mod a with a fixed p-residue
    holding BOTH K-parities — smallest members printed. KILL AS
    OBSERVABLE: some a with no both-parity class at K <= 200.
    PREDICTION: the class exists at every tested a; at a = 3 it is
    (1, 2) with K = 7, 9, 14.
D3  (odd a: 3, 5, 7; the found class) The family y_K = (q_K - 1)/a:
    consecutive-member input agreement depths (print — the kill is
    a bounded run), and the image bottom (b_1, b_2) at every member.
    PREDICTION: agreement depth grows with K; bottoms split by K
    parity as (1, 0) against (0, a) at every member. a = 3 is the
    hand-derived instance; 5 and 7 are out of sample.
D4  (even a: 2, 4, 6; the same machinery) PREDICTION: the same
    split (1, 0) against (0, a) — the max-string witness never
    consults the parity of a; at even a it simply stands BESIDE the
    comb witness.
D5  (the tie to the scan, a = 3) Among all n < 100000 sorted by
    digit string: the deepest-agreeing pairs whose image low-3
    prefixes differ — print the top three pairs' strings and image
    bottoms, read against the y-family's shape. Observable, no
    prediction frozen.

RESOURCE: well under a minute and trivially under 512MB (big ints
at K <= 40, one sort at 10^5).

RUN RECORD
----------
Two runs: the original design D0-D5, then D6-D7 added after D2's
kill fired (design frozen before the second run; see below). Each
a few seconds, trivial memory.

FINDINGS, FIRST RUN (post-run)
------------------------------
D0: zero failures (a = 2..7, n < 100000).
D1: zero mismatches — q_K - 1 IS the parity-split pattern with
bottom (b_1, b_2) = (1, 0) at even K, (0, a) at odd K, every
a = 2..7, K = 3..40: with Lemma 1 + 2 the image side is proved.
D2: at a = 3 the class exists — (q, p) = (1, 0) mod 3, period 24,
K = 5, 22, 24, 29, 46, 48, 53, 70, ... (the hand-attack's (1, 2)
class with K = 7, 9, 14 is a second one; the rig returns the
smallest p-residue). THE KILL FIRED at every other a: no
both-parity class with q_K = 1 mod a at K <= 200 for a = 2, 4, 5,
6, 7 — the t = 1 target is special to a = 3.
D3 (a = 3): WITNESS CONFIRMED — consecutive input agreement depths
8, 23, 25, 32, 47, 49, 56 (growing throughout) while the image
bottom is (0, 3) at every odd member (K = 5, 29, 53) and (1, 0) at
every even member (K = 22, 24, 46, 48, 70): one convergent input
family, two image bottoms, flip at b_1.
D4: no even-a family to test at t = 1 (D2's kill).
D5 (a = 3, N = 10^5): the scan's extremal pairs are single-tooth
translates — depth 16, x - y = 30551 = q_15 at all three top pairs,
image low-3 differing — a context-dependent cascade shape, not the
y-family (whose members at depth > 16 sit above N): consistent with
A tracking CAP while the structured witness lives elsewhere.

THE EXTENSION (design frozen before the second run; the kill's
lesson applied): drop t = 1. For ANY fixed t >= 1 the integers
q_K - t converge by K-parity to the two codings of one boundary
point, so the witness needs only a both-parity class of
(q_K, p_K) = (t, c) mod a — pigeonhole over the finite periodic
orbit, no divisibility miracle. Hand instance at a = 3, t = 2:
q_6 - 2 = 55 = (0,0,0,1,0,3) against q_7 - 2 = 71 = (0,1,2,0,1,0,1)
— bottoms differ at b_1 again.
D6  (a = 2..7) The general class scan: the smallest t >= 1 whose
    class (q_K, p_K) = (t mod a, c) holds both K-parities at
    K <= 400, with its members. PREDICTION: exists at every a.
    KILL AS OBSERVABLE: some a with none.
D7  (every a with a class) The family y_K = (q_K - t)/a: input
    agreement depths (kill: a bounded run), image low-4
    (b_1, b_2, b_3) per member. PREDICTION: within each K-parity
    the low-4 is eventually constant, and the two parities' values
    differ at b_1 or b_2 — at every a, even a included (the
    witness never consults the parity of a).

FINDINGS, SECOND RUN (post-run)
-------------------------------
D6: THE KILL FIRED AGAIN at a = 4, 5, 6, 7 — no both-parity class
(q_K, p_K) = (t, c) mod a at any t <= a, K <= 400: the residue
pairs there are PARITY-PURE (hand-check at a = 5: q = 2 occurs
with p in {1, 2, 3} at even K and p = 0 at odd K — disjoint
p-sets). At a = 2 the free-t scan finds t = 2, p = 1,
K = 2, 5, 8, 11, ... (both parities); a = 3 re-finds t = 1. D7
crashed on the a = 2 edge member K = 2 (q_2 - 2 = 0) before
printing any row — no D7 or D5 output this run.

THE SECOND EXTENSION (design frozen before the third run): the
single-q image family cannot reach a both-parity class at
a = 4..7, so widen it: z_K = q_K + u q_{K-r} - t with fixed
u >= 0, r in {1, 2}, t >= 1. Still one boundary point: z_K theta
differs from an integer by delta_K + u delta_{K-r} -> 0, with the
sign eventually fixed by K's parity (r = 2: the same sign as
delta_K; r = 1: the larger opposite term dominates for u >= 1),
so {z_K theta} -> {-t theta} sided by K-parity either way, and
the divisibility constraint z_K = 0 mod a now has the u-knob's
residue combinations available.
D8  (a = 2..7) The two-knob class scan: smallest (r, u, t) whose
    class q_K + u q_{K-r} = t, p_K + u p_{K-r} = c (mod a) holds
    both K-parities at K <= 400 (u = 0 recovers D6).
    PREDICTION: exists at every a. KILL AS OBSERVABLE: some a
    with none.
D9  (every a with a class) The family x_K = (z_K)/a = the witness:
    input agreement depths (kill: a bounded run), image low-4
    (b_1, b_2, b_3) per member. PREDICTION: depths grow; low-4
    eventually constant within each K-parity, the two parity
    values differing at a bounded position — every a, even a
    included (the witness never consults the parity of a).

FINDINGS, THIRD RUN (post-run)
------------------------------
D7 (a = 2, t = 2): WITNESS CONFIRMED — depths 6, 9, 12, ..., 24
growing, bottoms (1, 1, 0) at odd K (5, 11, 17, 23) against
(0, 0, 1) at even K (8, 14, 20, 26): a second witness at
[0;1,1,2], beside the comb, flip at b_1.
D9 (a = 7, r = 2, u = 1, t = 3): WITNESS CONFIRMED — depths 10,
19, 28, ..., 64 growing, bottoms (0, 6, 0) at odd K (11, 29, 47,
65) against (0, 7, 0) at even K (20, 38, 56, 74): flip at b_2.
D9 (a = 4, 5, 6): DEPTHS STUCK AT 1 — not a convergent family,
and the print located the flaw in the pre-run reasoning:
the class found is the TRIVIAL one (u = a - 1, t = a, c = 0),
where z_K = q_K + (a-1) q_{K-2} - a = a (q_{K-1} + q_{K-2} - 1),
so the input x_K = q_{K-1} + q_{K-2} - 1 carries the max-string
below K - 2 as its low digits — the input family lands ON the
boundary point -theta itself, and its strings alternate between
that point's two codings by the same parity mechanism one level
down. A fixed residue class is not enough: the input point
(c - t theta)/a must not itself be a coding boundary.

THE REFINEMENT (frozen before the fourth run): (c - t theta)/a is
an orbit point -j theta mod 1 iff theta (a j - t) is rational,
i.e. iff a | t and c = 0. Exclude exactly the class
(t = a, c = 0) from D8's scan; every other class's input point is
irrational-shifted and lies off the boundary orbit.
PREDICTION: a nontrivial class exists at a = 4, 5, 6 and its
family passes D9 (depths grow, parity-split bottoms).

FINDINGS, FOURTH RUN (post-run)
-------------------------------
D8 with the boundary class excluded: a nontrivial class at EVERY
a — a = 4: (r, u, t, c) = (1, 1, 1, 0), K = 8, 9, 20, 21, ...;
a = 5: same knobs, K = 32, 33, 68, 69, ...; a = 6: same knobs,
K = 20, 21, 44, 45, ...; a = 2, 3, 7 as before.
D9: WITNESS CONFIRMED AT EVERY WINDOW a = 2..7 — input agreement
depths grow throughout every family, and the image low-4 splits
by K-parity at every a: a = 2 (1,1,0)/(0,0,1); a = 3
(0,3,0)/(1,0,1); a = 4 (0,4,0)/(1,0,1); a = 5 (0,5,0)/(1,0,1);
a = 6 (0,6,0)/(1,0,1); a = 7 (0,6,0)/(0,7,0). The flip sits at
b_1 everywhere except a = 7, where both parities freeze b_1 = 0
and the flip is b_2's 6 against 7. The kill missed at every
window.

THE READING: the odd-a witness is FOUND, and it is not a comb.
It is the BOUNDARY FAMILY: integers x_K = (q_K + u q_{K-r} - t)/a
inside one residue class of the convergent pair mod a, chosen so
the input point (c - t theta)/a is OFF the coding-boundary orbit
(a | t with c = 0 is exactly the boundary and is excluded) while
the image point -t theta is ON it. The inputs then converge — one
family, growing agreement — while the images a x_K = q_K +
u q_{K-r} - t land beside the boundary on the side the
convergent's sign (-1)^K dictates, so the image strings alternate
between the two codings of one point forever: xa is unreadable at
every depth at all six windows, the parity of a never consulted.
The image side of the u = 0, t = 1 families — the strings of
q_K - 1 itself — is PROVED (Lemma 1 + 2, the two periodic
patterns telescoping to q_K - 1 by a two-line induction in steps
of 2, legality + uniqueness closing it — theorem); every other
image family, the class membership and the input convergence are
measured (rule at scanned scope: K <= 400, depths to 140). The even/odd split of
the COMB's fate (stripe against freeze) was a fact about the
comb, never about the gate — at even a the boundary family stands
beside the comb witness, at odd a it stands alone. Why the comb
itself freezes at odd a stays underived. And the failed trivial
class is its own specimen: the input family that lands ON the
boundary is exactly the max-string family one level down,
non-convergent by the same parity mechanism — the witness's
mechanism and its failure mode are one fact.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")


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


def max_pattern(K, a):
    """Lemma 2's periodic filling below K, low-to-high tuple: odd K
    carries (a, 1, 1) on positions 2, 4, 6 (mod 6) from b_2; even K
    carries (1, 1, a) on positions 1, 3, 5 (mod 6) from b_1."""
    ds = [0] * K
    if K % 2 == 1:
        for k in range(2, K, 2):
            ds[k] = a if k % 6 == 2 else 1
    else:
        for k in range(1, K, 2):
            ds[k] = a if k % 6 == 5 else 1
    return tuple(ds)


def pair_period(a):
    """Period of (q_K mod a, p_K mod a, K mod 2) — even by
    construction, so every residue class recurs with its parity."""
    qs = [1 % a, 1 % a]
    ps = [0, 1 % a]
    K = 2
    seen = {}
    while True:
        ak = a if K % 3 == 0 else 1
        qs.append((ak * qs[-1] + qs[-2]) % a)
        ps.append((ak * ps[-1] + ps[-2]) % a)
        state = (qs[-2], qs[-1], ps[-2], ps[-1], K % 3, K % 2)
        if state in seen:
            return K - seen[state]
        seen[state] = K
        K += 1


def find_class(a, kmax=200):
    """K's with q_K = 1 mod a, grouped by p_K mod a; return the
    p-residue whose K-list holds both parities (smallest such), with
    the list."""
    Q = make_Q(a, kmax)
    ps = [0, 1]
    while len(ps) < kmax:
        k = len(ps)
        ak = a if k % 3 == 0 else 1
        ps.append(ak * ps[-1] + ps[-2])
    groups = {}
    for K in range(3, kmax):
        if Q[K] % a == 1 % a:
            groups.setdefault(ps[K] % a, []).append(K)
    for c in sorted(groups):
        Ks = groups[c]
        if any(K % 2 == 0 for K in Ks) and any(K % 2 == 1 for K in Ks):
            return c, Ks
    return None, []


def main():
    # D0 positive control
    bad = 0
    for a in range(2, 8):
        Q = make_Q(a, 40)
        for n in range(100000):
            ds = digits(n, Q, 40)
            if sum(d * Q[k] for k, d in enumerate(ds)) != n or \
               not legal(ds, a):
                bad += 1
    print("D0 positive control: %d failures (a = 2..7, n < 100000)"
          % bad)

    # D1 the max-string pattern
    bad = 0
    for a in range(2, 8):
        Q = make_Q(a, 60)
        for K in range(3, 41):
            ds = digits(Q[K] - 1, Q, K)
            pat = max_pattern(K, a)
            b12 = (ds[1], ds[2])
            want = (1, 0) if K % 2 == 0 else (0, a)
            if ds != pat or b12 != want or not legal(ds, a):
                bad += 1
                print("   D1 MISMATCH a=%d K=%d: %s vs %s"
                      % (a, K, ds, pat))
    print("D1 q_K - 1 = the parity-split pattern, bottom (1,0)/(0,a): "
          "%d mismatches (a = 2..7, K = 3..40)" % bad)

    # D2 the class scan
    print("D2 the (q, p) mod a class q = 1 with both parities:")
    classes = {}
    for a in range(2, 8):
        per = pair_period(a)
        c, Ks = find_class(a)
        classes[a] = (c, Ks)
        if c is None:
            print("   a=%d: period %d, NO both-parity class at "
                  "K <= 200 (the kill)" % (a, per))
        else:
            print("   a=%d: period %d, class p = %d, K = %s..."
                  % (a, per, c, Ks[:6]))

    # D3/D4 the witness family
    for a in range(2, 8):
        c, Ks = classes[a]
        if c is None:
            continue
        Q = make_Q(a, max(Ks[:8]) + 5)
        tag = "D3" if a % 2 == 1 else "D4"
        rows = []
        prev = None
        for K in Ks[:8]:
            y = (Q[K] - 1) // a
            assert (Q[K] - 1) % a == 0
            dy = digits(y, Q, K + 3)
            di = digits(Q[K] - 1, Q, K + 3)
            dep = agree_depth(prev, dy) if prev is not None else -1
            rows.append((K, dep, (di[1], di[2])))
            prev = dy
        print("%s a=%d witness y_K = (q_K - 1)/%d: "
              "(K, input agree depth vs previous, image (b1, b2)):"
              % (tag, a, a))
        print("   %s" % rows)

    # D6 the general-t class scan
    print("D6 the general class (q_K, p_K) = (t, c) mod a, both "
          "parities, smallest t:")
    gen = {}
    for a in range(2, 8):
        Q = make_Q(a, 400)
        ps = [0, 1]
        while len(ps) < 400:
            k = len(ps)
            ak = a if k % 3 == 0 else 1
            ps.append(ak * ps[-1] + ps[-2])
        found = None
        for t in range(1, a + 1):
            groups = {}
            for K in range(2, 400):
                if Q[K] % a == t % a:
                    groups.setdefault(ps[K] % a, []).append(K)
            for c in sorted(groups):
                Ks = groups[c]
                if any(K % 2 == 0 for K in Ks) and \
                   any(K % 2 == 1 for K in Ks):
                    found = (t, c, Ks)
                    break
            if found:
                break
        gen[a] = found
        if found is None:
            print("   a=%d: NO class at t <= %d, K <= 400 (the kill)"
                  % (a, a))
        else:
            t, c, Ks = found
            print("   a=%d: t = %d, p = %d, K = %s..."
                  % (a, t, c, Ks[:8]))

    # D7 the general boundary-family witness
    for a in range(2, 8):
        if gen[a] is None:
            continue
        t, c, Ks = gen[a]
        Q = make_Q(a, 400)
        use = [K for K in Ks if Q[K] > t][:8]
        rows = []
        prev = None
        for K in use:
            y = (Q[K] - t) // a
            assert (Q[K] - t) % a == 0 and y > 0
            dy = digits(y, Q, K + 3)
            di = digits(Q[K] - t, Q, K + 3)
            dep = agree_depth(prev, dy) if prev is not None else -1
            rows.append((K, dep, di[1:4]))
            prev = dy
        print("D7 a=%d witness y_K = (q_K - %d)/%d: "
              "(K, input agree depth vs previous, image (b1,b2,b3)):"
              % (a, t, a))
        print("   %s" % rows)

    # D8 the two-knob class scan
    print("D8 the two-knob class q_K + u q_{K-r} = t, "
          "p_K + u p_{K-r} = c (mod a), both parities:")
    gen2 = {}
    for a in range(2, 8):
        Q = make_Q(a, 400)
        ps = [0, 1]
        while len(ps) < 400:
            k = len(ps)
            ak = a if k % 3 == 0 else 1
            ps.append(ak * ps[-1] + ps[-2])
        found = None
        for r in (2, 1):
            for u in range(0, a):
                for t in range(1, a + 1):
                    groups = {}
                    for K in range(3, 400):
                        if (Q[K] + u * Q[K - r]) % a == t % a:
                            c = (ps[K] + u * ps[K - r]) % a
                            groups.setdefault(c, []).append(K)
                    for c in sorted(groups):
                        if t % a == 0 and c == 0:
                            continue  # the boundary class: the
                            # input point is -theta itself
                        Ks = groups[c]
                        if any(K % 2 == 0 for K in Ks) and \
                           any(K % 2 == 1 for K in Ks):
                            found = (r, u, t, c, Ks)
                            break
                    if found:
                        break
                if found:
                    break
            if found:
                break
        gen2[a] = found
        if found is None:
            print("   a=%d: NO class at K <= 400 (the kill)" % a)
        else:
            r, u, t, c, Ks = found
            print("   a=%d: r = %d, u = %d, t = %d, p-comb = %d, "
                  "K = %s..." % (a, r, u, t, c, Ks[:8]))

    # D9 the two-knob witness
    for a in range(2, 8):
        if gen2[a] is None:
            continue
        r, u, t, c, Ks = gen2[a]
        Q = make_Q(a, 400)
        use = [K for K in Ks if Q[K] + u * Q[K - r] > t][:8]
        rows = []
        prev = None
        for K in use:
            z = Q[K] + u * Q[K - r] - t
            assert z % a == 0 and z > 0
            x = z // a
            dx = digits(x, Q, K + 3)
            di = digits(z, Q, K + 3)
            dep = agree_depth(prev, dx) if prev is not None else -1
            rows.append((K, dep, di[1:4]))
            prev = dx
        print("D9 a=%d witness x_K = (q_K + %d q_{K-%d} - %d)/%d: "
              "(K, input agree depth vs previous, image (b1,b2,b3)):"
              % (a, u, r, t, a))
        print("   %s" % rows)

    # D5 the scan's own extremal pairs at a = 3
    a = 3
    Q = make_Q(a, 40)
    N = 100000
    strs = sorted((digits(n, Q, 30), n) for n in range(1, N))
    pairs = []
    for i in range(len(strs) - 1):
        x, y = strs[i], strs[i + 1]
        ix = digits(a * x[1], Q, 30)[:4]
        iy = digits(a * y[1], Q, 30)[:4]
        if ix != iy:
            pairs.append((agree_depth(x[0], y[0]), x[1], y[1],
                          ix[1:], iy[1:]))
    pairs.sort(reverse=True)
    print("D5 a=3 deepest-agreeing pairs with differing image low-3")
    print("   (depth, x, y, image (b1,b2,b3) of 3x, of 3y):")
    for row in pairs[:3]:
        print("   %s" % (row,))


if __name__ == "__main__":
    main()
