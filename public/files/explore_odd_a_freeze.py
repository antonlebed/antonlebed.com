"""Why the [0; 1, 1, a, ...] comb freezes at odd a: the absorption
lemma, the conserved top charge, and the closed forms on both sides
of the parity split.

THE QUESTION
------------
At the period-3 window [0; 1, 1, a, ...] the comb family
u_M = q_3 + q_6 + ... + q_{3M} maps under xa to an image whose low
window FREEZES at odd a (the family is read) but STRIPES by comb
parity at even a >= 4 (pattern at a <= 7, M <= 26 —
explore_period3_borrow.py D3/D4, where the parity split was the open
leg). WHY does the parity of a decide? Find the invariant the odd-a
cascade conserves that the even-a cascade cannot.

THE WINDOW (vocabulary as in explore_period3_borrow.py): tail
(1, 1, a), a_k = a at k = 0 (mod 3), else 1; q_0 = q_1 = 1,
q_k = a_k q_{k-1} + q_{k-2}; caps b_0 = 0, cap(k) = a at
k = 2 (mod 3), else 1; b_k = cap(k) forces b_{k-1} = 0.

THE HAND-ATTACK (pre-engine, on paper — the mechanism DERIVED)
------------------------------------------------------------------
THE UNIT-PAIR DOUBLE (all a, K = 0 mod 3): the two unit quotients
above a large one give q_{K+1} = q_K + q_{K-1} and
q_{K+2} = q_{K+1} + q_K, hence

    q_{K+2} = 2 q_K + q_{K-1}.

THE ABSORPTION LEMMA. Let the image's top tooth be c q_{K-1} and let
the next comb extension cost a q_K (K = 3M + 3). Then

    c q_{K-1} + a q_K = q_K + c q_{K+2}   iff   a - 1 = 2c:

an integer top charge c that absorbs the extension EXISTS iff a is
ODD, and then c = (a-1)/2. The absorption is TOP-LOCAL: the charge
is conserved and moves two positions up; every digit below is
untouched. That conserved half-charge is the invariant. At even a no
integer c solves 2c = a - 1, the leftover q_K spreads downward, and
the bottom restripes.

THE ODD-a CLOSED FORM (theorem candidate, all odd a >= 3, all
M >= 1):

    a u_M = q_1 + ((a+1)/2) q_2 + sum_{i=2}^{M} q_{3i}
            + ((a-1)/2) q_{3M+2}.

Base M = 1 by algebra at every a: 1 + (a+1) + ((a-1)/2)(4a+4)
= 2a^2 + a = a q_3. Step by the absorption lemma. Legality: unit
teeth at the cap-1 positions = 0 (mod 3) over zeros, b_1 = 1 over
b_0 = 0, b_2 = (a+1)/2 < a for a >= 3, top charge (a-1)/2 < a at a
cap-a position. Classical Ostrowski uniqueness makes the legal form
THE greedy string, so the image bottom is frozen at
(0, 1, (a+1)/2, 0, 0, 0, 1, 0) and consecutive images agree below
3M + 2: the comb family is read — the freeze is the conserved
charge, proved rather than scanned.

EVEN a (hand data a = 4 at M <= 4, a = 6 at M <= 2): both parity
classes carry the SAME top charge a/2 - 1 (checked by algebra at
M = 1 and M = 2 for every even a: q_1 + (a/2) q_2 + q_4
+ (a/2-1) q_5 = 2a^2 + a = a q_3, and q_1 + (a/2+1) q_2 + a q_5
+ q_7 + (a/2-1) q_8 = 4a^3 + 8a^2 + 4a = a (q_3 + q_6)), the
bottoms differ at b_2 (a/2 against a/2 + 1), and the two-step
induction M -> M+2 inside one parity class is top-local (checked
numerically at a = 4, M = 2 -> 4). The general middle coefficients
as functions of a are NOT derived — D4 prints the decompositions to
read them from.

THE DESIGN (greedy extraction only; predictions frozen before the
run)
------------------------------------------------------------------
D0  Positive control: greedy digits reconstruct n exactly and are
    legal (b_0 = 0, caps, every cap digit over a 0), a in {3..9},
    n < 100000. PREDICTION: green.
D1  (odd a: 3, 5, 7, 9) The closed form's VALUE equals a u_M and
    its digit tuple equals the greedy digits of a u_M, M = 1..26
    (a = 9 out-of-sample; hand data was a = 3, 5). PREDICTION: all
    green.
D2  (odd a) Consecutive images agree at every position < 3M + 2,
    and the low-8 prefix is (0, 1, (a+1)/2, 0, 0, 0, 1, 0) at every
    M >= 2. PREDICTION: green.
D3  (even a: 4, 6, 8; a = 8 out-of-sample) Frozen predictions:
    b_2 = a/2 at odd M, a/2 + 1 at even M; the top digit
    b_{3M+2} = a/2 - 1 at every M; b_{3M-1} = a at even M >= 2.
    PREDICTION: all green.
D4  (even a) OBSERVABLES: the full nonzero-digit decomposition of
    a u_M at a in {4, 6, 8}, M = 1..10 — the instrument for
    freezing the general even-a closed forms. No prediction; the
    prints are the material.
D6  (second round, design frozen AFTER D4's prints were read and
    the induction proved on paper) The general even-a closed forms:
      odd M:  a u_M = q_1 + (a/2) q_2 + q_4
              + sum_{j=1}^{(M-1)/2} (q_{6j} + a q_{6j+2} + q_{6j+4})
              + (a/2 - 1) q_{3M+2}
      even M: a u_M = q_1 + (a/2 + 1) q_2
              + sum_{j=1}^{M/2} (a q_{6j-1} + q_{6j+1})
              + sum_{j=1}^{M/2 - 1} q_{6j+3}
              + (a/2 - 1) q_{3M+2}
    Both parities carry the SAME top charge a/2 - 1; the deficit
    against the absorption requirement (a-1)/2 leaves a UNIT residue
    per extension (c q_{K-1} + a q_K = q_K + c q_{K+2}
    + (a-1-2c) q_K), the third block tooth the even-M form
    suppresses and the odd-M form carries. Both classes' two-step
    induction M -> M+2 runs on ONE identity (proved on paper, all
    a, K = 3M + 3):
      q_K + a q_{K+2} + q_{K+4} + (a/2-1)(q_{K+5} - q_{K-1})
        = a q_K + a q_{K+3},
    with bases M = 1, 2 algebraic at every even a, legality checked
    position-by-position, and Ostrowski uniqueness closing form =
    greedy. CHECK: form value and digit tuple against greedy at
    a in {4, 6, 8}, M = 1..26. PREDICTION: all green.
D5  (the kill scan: an odd-a comb family that UN-freezes would
    demote the freeze law to a one-comb artifact).
    Odd a in {3, 5, 7}, five comb families, M = 1..26:
      C1 teeth at 3i (the proved comb, control);
      C2 teeth at 3i + 3 (shifted one period);
      C3 teeth at 6i (double spacing, even teeth);
      C4 teeth at 6i + 3 (double spacing, odd teeth);
      C5 teeth at 3i + 2 (the cap-a positions);
      C6 teeth at 3i + 1 (the remaining residue).
    For each, print the distinct low-3 image prefixes per M-parity
    class. KILL as observable: a family whose two parity classes
    print DISJOINT distinct low-3 sets that alternate (the stripe
    shape) at an odd a. PREDICTION (from the absorption lemma's
    shape — a transplant from the C1 mechanism, flagged as such):
    C1-C4 frozen; C5, C6 genuinely open, the prints decide.

RESOURCE: well under a minute and trivially under 512MB (digit
tuples at M <= 26, q-indices < 90).

RUN RECORD
----------
Two runs (the second after D6's design was frozen from D4's prints
and the paper induction), all checks green both times, seconds each,
trivial memory.

FINDINGS (post-run)
-------------------
D0: zero failures (a in 3..9, n < 100000) — the positive control,
printed before any verdict was read.
D1: zero mismatches at every a in {3, 5, 7, 9} (a = 9
out-of-sample), M = 1..26: the odd-a closed form's value and digit
tuple equal the greedy string everywhere. With the algebraic base,
the absorption-lemma step, legality and uniqueness, the form is a
THEOREM for all odd a >= 3 and all M >= 1.
D2: zero freeze violations — consecutive images agree below 3M + 2
and the low-8 prefix is (0, 1, (a+1)/2, 0, 0, 0, 1, 0) at every
M >= 2, every odd a tested: the comb family is READ, now as a
corollary of the closed form.
D3: zero violations at a = 4, 6, 8 (a = 8 out-of-sample): b_2
stripes a/2 against a/2 + 1 by M parity, the top digit is a/2 - 1
at every M, and b_{3M-1} = a at even M.
D4: the decompositions pin the even-a forms exactly as D6 states
them — period-6 blocks, one cap-a tooth per block, the suppressed
third tooth at even M, the constant top charge a/2 - 1.
D5: the kill missed at every cell — all six comb families at
a = 3, 5, 7 print ONE low-3 value per parity class and the classes
agree (C1 the proved bottom (0, 1, (a+1)/2); C2-C5 all (0, 0, 0);
C6 (0, 0, (a+1)/2 - 1)): no odd-a un-freeze anywhere scanned, the
freeze survives shifts, double spacing, and both other residues.
D6: zero mismatches at a = 4, 6, 8, M = 1..26: both even-a forms
equal greedy everywhere. With the two bases, the shared two-step
identity, legality and uniqueness, the b_2 STRIPE is a THEOREM for
all even a >= 4 and all M >= 1.

THE READING: the parity split is the ABSORPTION LEMMA. The window's
two unit quotients give the doubling identity q_{K+2} = 2 q_K +
q_{K-1} at K = 0 (mod 3), so a top charge c q_{K-1} absorbs the
next comb extension a q_K top-locally iff 2c = a - 1. Odd a: the
charge (a-1)/2 exists, is conserved, and climbs two positions per
extension — everything below is untouched, the image bottom freezes
at (0, 1, (a+1)/2), and xa is READABLE along the comb (theorem, all
odd a >= 3, all M). Even a: the best integer charge a/2 - 1 leaves
one unit residue q_K per extension — the suppressed block tooth —
and the resettlement alternates the bottom between two legal forms
differing at b_2 (a/2 against a/2 + 1): the stripe is the
half-unit's wake (theorem, all even a >= 4, all M). Only a = 2
degenerates the residue into a full restructuring with the flip at
b_1 (explore_period3_borrow.py). The freeze also survives every
alternative comb scanned (D5): no un-freeze, the law is not a
one-comb artifact at the scanned families.
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
    """Classical Ostrowski legality for the (1, 1, a) tail."""
    if ds[0] != 0:
        return False
    for k in range(1, len(ds)):
        if ds[k] > cap(k, a):
            return False
        if ds[k] == cap(k, a) and ds[k - 1] != 0:
            return False
    return True


def nonzero(ds):
    """(position, digit) pairs, low-to-high."""
    return tuple((k, d) for k, d in enumerate(ds) if d)


def run():
    ok = True

    # ---- D0: positive control ----
    fails = 0
    for a in range(3, 10):
        Q = make_Q(a)
        for n in range(1, 100000):
            ds = digits(n, Q, 40)
            if sum(d * Q[k] for k, d in enumerate(ds)) != n:
                fails += 1
            elif not legal(ds, a):
                fails += 1
    print("D0 positive control: %d failures (a in 3..9, n < 100000)"
          % fails)
    ok = ok and fails == 0

    # ---- D1: the odd-a closed form ----
    for a in (3, 5, 7, 9):
        Q = make_Q(a)
        bad = 0
        for M in range(1, 27):
            u = sum(Q[3 * i] for i in range(1, M + 1))
            form_val = (Q[1] + ((a + 1) // 2) * Q[2]
                        + sum(Q[3 * i] for i in range(2, M + 1))
                        + ((a - 1) // 2) * Q[3 * M + 2])
            width = 3 * M + 4
            form_ds = [0] * width
            form_ds[1] = 1
            form_ds[2] = (a + 1) // 2
            for i in range(2, M + 1):
                form_ds[3 * i] += 1
            form_ds[3 * M + 2] += (a - 1) // 2
            gd = digits(a * u, Q, width)
            if form_val != a * u or tuple(form_ds) != gd \
                    or not legal(gd, a):
                bad += 1
        print("D1 a=%d: %d mismatches (form vs value vs greedy, "
              "M=1..26)" % (a, bad))
        ok = ok and bad == 0

    # ---- D2: the freeze readout ----
    for a in (3, 5, 7, 9):
        Q = make_Q(a)
        bad = 0
        prev = None
        for M in range(1, 27):
            u = sum(Q[3 * i] for i in range(1, M + 1))
            gd = digits(a * u, Q, 90)
            if prev is not None:
                depth = 3 * (M - 1) + 2
                if gd[:depth] != prev[:depth]:
                    bad += 1
            if M >= 2 and gd[:8] != (0, 1, (a + 1) // 2, 0, 0, 0, 1, 0):
                bad += 1
            prev = gd
        print("D2 a=%d: %d freeze violations" % (a, bad))
        ok = ok and bad == 0

    # ---- D3: even-a frozen predictions ----
    for a in (4, 6, 8):
        Q = make_Q(a)
        bad = 0
        for M in range(1, 27):
            u = sum(Q[3 * i] for i in range(1, M + 1))
            gd = digits(a * u, Q, 90)
            want_b2 = a // 2 if M % 2 == 1 else a // 2 + 1
            if gd[2] != want_b2:
                bad += 1
            if gd[3 * M + 2] != a // 2 - 1:
                bad += 1
            if M >= 2 and M % 2 == 0 and gd[3 * M - 1] != a:
                bad += 1
        print("D3 a=%d: %d stripe/top-charge violations" % (a, bad))
        ok = ok and bad == 0

    # ---- D4: even-a decompositions (observables) ----
    for a in (4, 6, 8):
        Q = make_Q(a)
        print("D4 a=%d decompositions (position:digit):" % a)
        for M in range(1, 11):
            u = sum(Q[3 * i] for i in range(1, M + 1))
            gd = digits(a * u, Q, 90)
            body = " ".join("%d:%d" % (k, d) for k, d in nonzero(gd))
            print("  M=%2d  %s" % (M, body))

    # ---- D6: the even-a closed forms ----
    for a in (4, 6, 8):
        Q = make_Q(a)
        bad = 0
        for M in range(1, 27):
            u = sum(Q[3 * i] for i in range(1, M + 1))
            width = 3 * M + 4
            form_ds = [0] * width
            form_ds[1] = 1
            if M % 2 == 1:
                form_ds[2] = a // 2
                form_ds[4] += 1
                for j in range(1, (M - 1) // 2 + 1):
                    form_ds[6 * j] += 1
                    form_ds[6 * j + 2] += a
                    form_ds[6 * j + 4] += 1
            else:
                form_ds[2] = a // 2 + 1
                for j in range(1, M // 2 + 1):
                    form_ds[6 * j - 1] += a
                    form_ds[6 * j + 1] += 1
                for j in range(1, M // 2):
                    form_ds[6 * j + 3] += 1
            form_ds[3 * M + 2] += a // 2 - 1
            form_val = sum(d * Q[k] for k, d in enumerate(form_ds))
            gd = digits(a * u, Q, width)
            if form_val != a * u or tuple(form_ds) != gd \
                    or not legal(gd, a):
                bad += 1
        print("D6 a=%d: %d mismatches (even-a forms vs greedy, "
              "M=1..26)" % (a, bad))
        ok = ok and bad == 0

    # ---- D5: the kill-shape scan ----
    families = {
        "C1 3i": lambda i: 3 * i,
        "C2 3i+3": lambda i: 3 * i + 3,
        "C3 6i": lambda i: 6 * i,
        "C4 6i+3": lambda i: 6 * i + 3,
        "C5 3i+2": lambda i: 3 * i + 2,
        "C6 3i+1": lambda i: 3 * i + 1,
    }
    for a in (3, 5, 7):
        Q = make_Q(a, count=200)
        for name, pos in families.items():
            lows = {0: set(), 1: set()}
            for M in range(1, 27):
                v = sum(Q[pos(i)] for i in range(1, M + 1))
                gd = digits(a * v, Q, 90)
                lows[M % 2].add(gd[:3])
            verdict = ("STRIPED" if lows[0].isdisjoint(lows[1])
                       and len(lows[0]) == 1 and len(lows[1]) == 1
                       else "frozen/mixed")
            print("D5 a=%d %-8s odd-M %s  even-M %s  -> %s"
                  % (a, name, sorted(lows[1]), sorted(lows[0]),
                     verdict))

    print("ALL CHECKS " + ("GREEN" if ok else "*** FAILURES ***"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(run())
