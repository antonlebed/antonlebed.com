"""The Pisot tower off its spine: the NARAYANA trailing window --
does a completion depend on the recurrence, or only on its DEGREE?

THE QUESTION
------------
The corpus proves one theorem uniform in d (explore_tetranacci_window.py):
the trailing d-bonacci window refuses the ring at every degree d >= 2, its
down-carry 2 q_k = q_{k+1} + q_{k-d} doubling a step-(d+1) witness comb
into a step-d comb whose bottom cycles through d phases, so d image limit
points sit over one input limit and x2 has no continuous extension; and
each member completes almost one-to-one over a translation of T^{d-1}.
Every member of that spine has FULL support -- all d lags present -- so
the spine varied the DEGREE and never the SUPPORT.

This script walks the first window off the spine. The object is the
trailing NARAYANA window: q_k = q_{k-1} + q_{k-3}, the greedy numeration
of the supergolden root of x^3 = x^2 + 1 (b = 1.46557, Pisot -- the two
conjugates have modulus b^{-1/2} = 0.826, the product of the roots being
1). Degree 3 is deliberate: it holds the TRIBONACCI window as a positive
control and predicts the same torus, so the only thing varied is the
support, which here has a hole at lag 2.

The finding sought is the PHASE COUNT. A refusal of the ring is the
EXPECTED outcome and is not the finding: 3 phases would say the count is
the degree and the support is invisible; anything else says the tower's
one-per-degree reading was the spine's coincidence.

TRANSPLANTS, flagged at the freeze (the spine's vocabulary is not this
window's): the very idea that a WITNESS COMB is the right instrument is
imported from the spine, where a single descent lag makes the comb's
spacing obvious; the expectation of a torus at all is imported from
degree 3 of the spine (Rauzy). Both are predictions to test. The step of
the comb is NOT transplanted -- it is scanned, because the descent here
is a SET of lags and no single spacing is forced.

THE HAND-DERIVATION (on paper, before any engine; conventions
q_0 = 1, q_1 = 2, q_2 = 3, q_k = q_{k-1} + q_{k-3}, so
1, 2, 3, 4, 6, 9, 13, 19, 28, 41, 60, ...; digits d_k at place q_k,
low index first)
------------------------------------------------------------------
LEMMA 0 (the admissible language). The b-expansion of 1 is finite and
is 101: dividing x^3 = x^2 + 1 by x^3 gives 1 = b^-1 + b^-3. By Parry's
condition a greedy string is admissible iff every suffix is
lexicographically below (100)^w, which forbids exactly the factors 11
and 101 -- so an admissible string is 0/1 with its 1-indices PAIRWISE
AT LEAST 3 APART. The bound that makes it canonical: the largest such
string on indices < k is q_{k-1} + q_{k-4} + q_{k-7} + ... and that sum
is q_k - 1 (k = 4: 4 + 1 = 5; k = 5: 6 + 2 = 8; k = 6: 9 + 3 = 12;
k = 7: 13 + 4 + 1 = 18). So a gap-3 string with top index t has value in
[q_t, q_{t+1} - 1], greedy takes q_t and recurses: greedy reproduces the
string, and distinct admissible strings have distinct values.

LEMMA A (the down-carry has TWO teeth, and this is the whole departure).
From q_{k+1} = q_k + q_{k-2},
  2 q_k = q_{k+1} + (q_k - q_{k-2}),
and q_k - q_{k-2} = q_{k-1} + q_{k-3} - q_{k-2} = q_{k-4} + q_{k-3}
(using q_{k-1} - q_{k-2} = q_{k-4}). The pair q_{k-3} + q_{k-4} is
adjacent, hence not admissible, and normalizes by the same identity run
once more: q_{k-3} + q_{k-4} = q_{k-2} + q_{k-7}. So
  2 q_k = q_{k+1} + q_{k-2} + q_{k-7}   (k >= 7),
whose indices are spaced 3 and 5 and so ARE admissible: this is the
canonical form. The spine's carry descends by the single lag d; this one
descends by 2 AND by 7. Boundaries below k = 7 are printed rather than
claimed.

THE CASCADE THEOREM at the selected step (s = 7; on paper, before
the checker of it was written)
------------------------------------------------------------------
Write K = 7m, m >= 1, for the comb T_K = q_7 + q_14 + ... + q_K. Two
normalization identities carry the whole proof, both immediate from
the recurrence:
  (R1)  q_j + q_{j+2} = q_{j+3}                   (the recurrence)
  (R2)  q_j + q_{j+1} = q_{j+2} + q_{j-3}  (j >= 3)   (Lemma A's step)
with the two boundary consolidations q_0 + q_1 = q_2 and 2 q_2 = q_4.

THEOREM. The canonical digits of 2 T_{7m} are a step-3 comb with top
tooth 7m+1 over a single bottom tooth, cycling with period 3 in m
(period 21 in K):
  m = 1 mod 3:  {0} u {j = 2 mod 3 : 5 <= j <= 7m+1}
  m = 2 mod 3:  {2} u {j = 0 mod 3 : 6 <= j <= 7m+1}
  m = 0 mod 3:  {4} u {j = 1 mod 3 : 7 <= j <= 7m+1}

PROOF. Base m = 1: Lemma A at k = 7 is 2 q_7 = q_8 + q_5 + q_0, which
is the m = 1 row. Step m -> m+1: 2 T_{7m+7} = 2 T_{7m} + 2 q_{7m+7},
and Lemma A at k = 7m+7 gives 2 q_{7m+7} = q_{7m+8} + q_{7m+5} +
q_{7m}. THE DEPARTURE FROM THE SPINE IS EXACTLY HERE: the carry's low
tooth q_{7m} lands ADJACENT to the standing image's own top tooth
q_{7m+1}. On the spine the deposits are disjoint from the standing
teeth and each tooth shifts up once, independently; here the
collision opens a cascade that runs the FULL LENGTH of the comb, and
that cascade is the proof's content.

The cascade. R2 at j = 7m turns {7m, 7m+1} into {7m+2, 7m-3}. The
product 7m+2 sits three below the untouched q_{7m+5}, so the top
closes. The other product, 7m-3, sits one BELOW the next standing
tooth (the teeth are spaced 3, so that tooth is 7m-2) -- adjacent
again. R2 at j = 7m-3 turns {7m-3, 7m-2} into {7m-1, 7m-6}, and 7m-1
sits three below 7m+2, closing that rung, while 7m-6 is once more one
below the next standing tooth. So the adjacency propagates downward,
one R2 per tooth, RAISING EVERY STANDING TOOTH BY ONE and handing a
fresh adjacency to the tooth beneath. It terminates at the comb's
bottom tooth, and the three rows differ only in how it terminates:
  m = 1 mod 3: bottom tooth 5 over the standing {0}. The cascade
    arrives as {4, 5}; R2 at j = 4 gives {6, 1}; and q_0 + q_1 = q_2.
    Result {2} u {6, 9, ..., 7m+8} -- the m+1 = 2 mod 3 row.
  m = 2 mod 3: bottom tooth 6 over the standing {2}. The cascade
    arrives as {5, 6}; R2 at j = 5 gives {7, 2}; and 2 q_2 = q_4.
    Result {4} u {7, 10, ..., 7m+8} -- the m+1 = 0 mod 3 row.
  m = 0 mod 3: bottom tooth 7 over the standing {4}. The cascade
    arrives as {6, 7}; R2 at j = 6 gives {8, 3}; now {3, 4} is
    adjacent and R2 at j = 3 gives {5, 0}. Result
    {0} u {5, 8, ..., 7m+8} -- the m+1 = 1 mod 3 row.
Each result is a step-3 comb over a bottom tooth at gap 5, 4 or 3
from it, hence gap-3 throughout, hence canonical by Lemma 0. []

CONSEQUENCE. The three rows ARE the three phases, in the order the
cycle visits them, and the period 21 is proved rather than read off a
finite run. Their low digits differ at digit 0 (row 1 against rows 2
and 3) and at digit 2 (row 2 against row 3) -- a bounded separating
digit at every m, while the input agreement grows without bound. So
x2 has no continuous extension to the Narayana completion,
unconditionally in K rather than at scanned scope.

WHAT THE PROOF DOES NOT SETTLE. Three is the length of the BOTTOM
TOOTH'S return orbit 0 -> 2 -> 4 -> 0, and the proof exhibits that
orbit without deriving its length from the degree: nothing in the
cascade argument says the orbit must be as long as the recurrence is
deep. On the spine the same slot is filled by a theorem uniform in d;
here it is filled by three explicit rows. So the coincidence the
corpus has never separated -- degree, image step, phase count, all
three equal wherever it has measured -- survives this proof intact.

THE PREDICTIONS, frozen before the engine
-----------------------------------------
P1  Admissibility is the gap-3 language and greedy reproduces it; the
    largest admissible sum on indices < k is exactly q_k - 1.
P2  2 q_k = q_{k+1} + q_{k-2} + q_{k-7} exactly, for every k >= 7, and
    the right side is already canonical.
P3  A witness comb of some step s exists: the combs T_K over one
    residue of K mod s agree to a depth GROWING with K, so they converge
    to one input limit. The spine's forced spacing does not transplant,
    so s is scanned rather than named; the smallest s that keeps both
    the comb and its double admissible without collision is the
    prediction, and the scan is what decides it.
P4  THE FINDING: the number of distinct low-digit limit strings of
    2 T_K over that one input limit is NOT 3. The spine's count is d
    because its descent is a single lag d; here the descent is a SET of
    two lags, so a count of 3 would be a coincidence rather than the
    degree speaking. P4 is the prediction this rig exists to kill.
P6  D7 exact at every m = 1..40, zero failures, the extracted
    digits equal the theorem's rows; bases 2 T_7 = 38, 2 T_14 = 592,
    2 T_21 = 9042; least differing digits 0, 0, 2 across the three
    pairs of rows.
P5  x2 has no continuous extension: the phases differ at a BOUNDED
    digit index, so the images are distinct limit points over one input
    limit. (Expected, not the finding.)

THE KILLS, as observables and never as inferences
-------------------------------------------------
K1  D2 prints False at any k in range -> Lemma A is wrong and the paper
    derivation above is the thing that failed, not the window.
K2  D4 prints a distinct-limit-string count of 3 -> P4 dies and the
    phase count IS the degree, support invisible.
K3  D4 prints an UNBOUNDED or non-repeating count as the range grows
    -> no finite phase structure; the comb instrument itself does not
    transplant and the question needs a different witness.
K5  D7 prints a single mismatch at any m in range -> the cascade
    theorem is wrong as stated and the paper argument is what failed,
    the measured phases standing untouched.
K4  D5's kill digit grows with K rather than staying bounded -> P5
    dies, the images are not separated at a fixed digit, and no
    discontinuity is demonstrated by this construction.

THE DESIGN
----------
D0  POSITIVE CONTROL, run before any Narayana verdict is read: the same
    engine, given the Tribonacci lags (1, 2, 3) and its seeds, must
    reproduce the frozen prints of explore_tribonacci_discontinuity.py
    as they stand quoted in explore_tetranacci_window.py's own control
    -- the step-4 comb bases 2 T_3 = 14, 2 T_7 = 176, 2 T_11 = 2030
    with their digit sets, and the atlas pair (93684, 63562) at input
    agreement 17 and image agreement 4.
D0b THE CONTROL THE EXTRACTION CHECK DOES NOT GIVE: the INSTRUMENTS
    that produce the finding, run on the window whose answer is a
    theorem. The selector over s = 3..20 at Tribonacci, and the phase
    count at that window's forced step.
D0c THE PARAMETER THE INSTRUMENT FIXES AND THE QUESTION LEAVES FREE:
    the comb's OFFSET -- which residue class the teeth sit in. Swept
    over every offset at both windows, at three steps each.
D1  Lemma 0, exhaustively: over every 0/1 mask on indices < k for k up
    to 18, the gap-3 masks are exactly the greedy expansions of their
    values, and their maximum is q_k - 1.
D2  Lemma A at every k in range, with the boundaries k < 7 printed.
D3  The comb scan: for each step s in 3..30, build T_K over one residue
    class of K, check the comb is admissible, and record whether the
    inputs' pairwise agreement grows with K.
D4  The phase count at each step, read as a LIMIT and not as a sample:
    the low-DEEP digits of 2 T_K over a long run of K, transient
    discarded, counted at two depths and two range lengths so that a
    count still moving is visible as such. A FIRST INSTRUMENT AT DEPTH
    12 WAS DISCARDED HERE: at that depth the step-3 comb's images had
    not yet stabilized and read as two phases where they converge to
    one, and step 7's three read as three by luck. Depth is the
    instrument's own dial and it is set past the transient.
D5  The step's own selector, which the spine never had to state: is
    the image a SINGLE-STEP comb above its bottom? The spine's image is
    a step-d comb by its theorem, so every d-bonacci window satisfies
    this automatically and the question of choosing a step never
    arises. Here the step is free, so the criterion is applied over
    s = 3..30 and the steps meeting it are printed, with the phase
    count and the separating digit read at whichever it selects.
D7  THE CASCADE THEOREM IN RANGE, by greedy extraction only -- no
    closed form from the proof enters the digit path: the greedy
    digits of 2 T_{7m} against the stated phase row at every
    m = 1..40, the three bases as exact integers, and the least
    differing digit between the rows read off the extracted strings.
D6  The numeric torus shadow: cells of the window contract in the
    conjugate-plane coordinate sum d_k mu^k at the conjugate modulus's
    own rate, |mu| = b^{-1/2}. A shadow, never the classification --
    which side of the atlas this completion lands on is a classical
    question (the supergolden substitution's Rauzy fractal) and is
    contacted in the docs, not decided here.

THE FINDINGS (this section did not exist before the run; every number
below is copied from the printed output)
-------------------------------------------------------------------
F0  CONTROL PASSES, and is read before any Narayana result: the engine
    given the Tribonacci lags reproduces that rig's frozen prints --
    2 T_3 = 14 digits [0, 4]; 2 T_7 = 176 digits [0, 1, 5, 8];
    2 T_11 = 2030 digits [3, 6, 9, 12]; the atlas pair (93684, 63562)
    at input agreement 17 and image agreement 4. AND THE INSTRUMENTS
    THEMSELVES ARE CONTROLLED, which the extraction check does not do:
    at Tribonacci the phase instrument returns 3 at that window's
    forced step 4, reproducing the spine's theorem. THE CONTROL EARNED
    ITS PLACE BY FAILING FIRST -- it exposed that the phase reading
    fixed the comb's OFFSET, a parameter the question leaves free.
    Swept over every offset at three steps of each window, the phase
    count and the selector's verdict are both invariant (the printed
    gap SET is not, at the steps the selector rejects: Narayana step 5
    reads {3, 4, 7} or {3, 7} by offset, and both are rejections).

F1  P1 CONFIRMED (rule; proved on paper, verified exhaustively over
    every 0/1 mask on indices < k for k <= 18). The gap-3 language IS
    the greedy language of this window at every one of those masks, and
    the largest admissible sum below k = 18 is 1277 = q_18 - 1.
    Places: 1, 2, 3, 4, 6, 9, 13, 19, 28, 41, 60, 88.

F2  P2 CONFIRMED (rule; proved algebraically, verified k = 7..45).
    2 q_k = q_{k+1} + q_{k-2} + q_{k-7} exactly, and that form is
    already canonical (gap-3) at every k in range. Boundaries printed:
    2 q_5 = 18 = q_0 + q_3 + q_6, 2 q_6 = 26 = q_0 + q_4 + q_7.
    THE DEPARTURE FROM THE SPINE IS HERE AND IT IS STRUCTURAL: the
    d-bonacci carry descends by the SINGLE lag d; this one descends by
    2 AND by 7, because the naive residue q_{k-3} + q_{k-4} is adjacent
    and must itself normalize.

F3  P3 REFUTED AS FRAMED, and the hole was in the freeze rather than
    in the window. The slate said "a witness comb of SOME step s
    exists", presupposing the spine's uniqueness -- where the single
    descent lag forces the step, so the choice never had to be made.
    Here EVERY step s = 3..30 gives an admissible comb whose members
    converge to one input limit: the input agreements grow linearly in
    K at every step (at s = 7: 42, 49, 56, 63, 70, 77, 84, 91, 98, 105,
    112, 119). The comb does not select itself.

F4  SO THE PHASE COUNT IS THE WITNESS'S PROPERTY AND NOT THE WINDOW'S
    (rule at scanned scope, s = 3..30). The number of image limit
    points over one input limit, by step from 3: 1, 1, 2, 1, 3, 2, 2,
    1, 1, 1, ... and 1 at every step from 13 to 30. Stable at both
    depths (40, 80) and both spans (60, 90) at every step. The spine
    could not have seen this: its count is the answer of the one comb
    its carry forces.

F5  THE SPINE'S SELECTOR, MADE EXPLICIT, PICKS EXACTLY ONE STEP
    (observation, s = 3..30). The criterion every d-bonacci window
    satisfies for free -- the image is a SINGLE-STEP comb above its
    bottom -- holds at s = 7 ALONE, with image step 3. The scan shows
    why: from s = 11 up the image gaps read [3, 5, s-8], the three
    carry teeth {k+1, k-2, k-7} standing apart at their own spacings;
    at s = 7 they interlock and cascade. Printed at every row of
    s = 3..30, not sampled.

F6  P4 REFUTED, AND THE DEGREE READING SURVIVES THE SUPPORT HOLE
    (rule; measured here, proved at F9). At the selected step the image is a
    step-3 comb whose bottom cycles through exactly THREE phases,
    pairwise separated at digit <= 2, over one input limit:
      10000100100100100100100100
      00100010010010010010010010
      00001001001001001001001001
    The visiting order is periodic and printed rather than inferred --
    0, 1, 2, 0, 1, 2, ... as K steps by 7 -- so the period in K is 21
    and the phase is set by K mod 21. Three is the degree. The hole at
    lag 2 does not move it. Measured here to depth 80 over the tail
    of a 90-comb run, and proved unconditionally in K at F9.

F7  P5 CONFIRMED at that scope: x2 has no continuous extension to this
    completion, three distinct image limit points sitting over one
    input limit and separated at a bounded digit. The Narayana window
    is NOT a ring.

F9  THE CASCADE THEOREM HOLDS (rule at s = 7; proved on paper,
    verified by greedy extraction at every m = 1..40). D7's greedy
    digits of 2 T_{7m} equal the theorem's rows at every m, with no
    closed form entering the digit path, and the extracted rows
    separate at digits 0, 0, 2 -- the bound the proof states. Bases,
    printed: 2 T_7 = 38 = q_8 + q_5 + q_0;
    2 T_14 = 592 = q_15 + q_12 + q_9 + q_6 + q_2;
    2 T_21 = 8638 = q_22 + q_19 + q_16 + q_13 + q_10 + q_7 + q_4.
    P6 MET ON EVERYTHING D7 CHECKS AND MISSED ON ONE FROZEN NUMBER:
    the freeze wrote the third base as 9042, an arithmetic slip in the
    hand-summation of q_21; the theorem predicts a digit SET, D7
    compares sets, and the set at m = 3 is right. The slip is kept
    rather than corrected away because it is why a frozen base integer
    is a weaker check than a frozen set -- a wrong integer beside a
    right set says the paper's arithmetic slipped, where a wrong set
    would have said the argument did.
    WHAT THE PROOF BUYS AND WHAT IT DOES NOT. It buys the modality:
    three phases, period 21 in K, separating digit <= 2, at every
    K = 0 mod 7 rather than over a scanned run -- the same modality
    the spine has, reached by a different mechanism. On the spine the
    deposits are disjoint from the standing teeth and each tooth
    shifts up independently; here the carry's low tooth q_{7m} lands
    ADJACENT to the image's own top tooth q_{7m+1} and that adjacency
    runs the full length of the comb, one R2 per tooth. It does NOT
    buy the reading: the count is the length of the bottom tooth's
    return orbit 0 -> 2 -> 4 -> 0, and the proof exhibits that orbit
    without deriving its length from the degree. The
    degree/image-step/phase-count coincidence stands untouched.

F8  THE SHADOW (observation): lambda = 1.465571, |mu| = 0.826031,
    against the predicted b^{-1/2} = 0.826031. Cell diameters in the
    plane coordinate sum d_k mu^k contract at ratios 0.749-0.826 over
    depths 7-17 against |mu| = 0.8260. A shadow and nothing more:
    which cell of the atlas this completion lands in is a classical
    question about the supergolden substitution and is not decided
    here.

THE INSTRUMENT NOTE, kept because the first instrument was wrong and
its wrongness was invisible in the asserts: reading the low 12 digits
at a fixed drop reported TWO phases at s = 3 where the images converge
to one -- the two strings differed only at digit 11, the last one
measured -- and the same fixed drop at depth 80 reported TWELVE there.
Both are the transient, whose length grows with the depth being
measured. The instrument that stands reads the TAIL of a long run at
whatever depth it measures, which is why D4 prints its count at two
depths crossed with two spans: a count still moving shows as a count
that differs across the four.

RUN RECORD: one process, ~7 s wall-clock, ordinary-analysis footprint
well under the 512MB ceiling, no BLAS import.
"""

import sys

WIDTH = 3200
DEPTH = 46


def build_Q(lags, seeds, n=3400):
    """q_k = sum of q_{k-l} over the lags; seeds give the first max(lags)."""
    Q = list(seeds)
    while len(Q) < n:
        Q.append(sum(Q[-l] for l in lags))
    return Q


QN = build_Q((1, 3), [1, 2, 3])     # Narayana: x^3 = x^2 + 1
QT = build_Q((1, 2, 3), [1, 2, 4])  # Tribonacci control


def greedy(n, Q):
    """Greedy digits d_0..d_{WIDTH-1}, low index first."""
    d = [0] * WIDTH
    for k in range(len(Q) - 1, -1, -1):
        if Q[k] <= n:
            if k < WIDTH:
                d[k] = 1
            n -= Q[k]
    assert n == 0, n
    return tuple(d)


def digit_set(n, Q):
    return {k for k, bit in enumerate(greedy(n, Q)) if bit}


def agree(a, b, Q):
    da, db = greedy(a, Q), greedy(b, Q)
    t = 0
    while t < WIDTH and da[t] == db[t]:
        t += 1
    return t


def comb_T(K, Q, lo, step):
    return sum(Q[j] for j in range(lo, K + 1, step))


def gap3(idx):
    s = sorted(idx)
    return all(s[i + 1] - s[i] >= 3 for i in range(len(s) - 1))


ok_all = True


def report(label, ok):
    global ok_all
    ok_all = ok_all and ok
    print("%s: %s" % (label, ok))


# ---------------------------------------------------------------- D0
# POSITIVE CONTROL: the engine on the Tribonacci window must reproduce
# the frozen prints of the degree-3 rig before any Narayana result is
# read.
tri_bases = {3: (14, {0, 4}), 7: (176, {0, 1, 5, 8}),
             11: (2030, {3, 6, 9, 12})}
d0 = True
for K, (val, digits) in sorted(tri_bases.items()):
    t = 2 * comb_T(K, QT, 3, 4)
    got = digit_set(t, QT)
    print("D0 tribonacci K=%d: 2 T_K = %d, digits %s" % (K, t, sorted(got)))
    d0 = d0 and t == val and got == digits
ia = agree(93684, 63562, QT)
im = agree(2 * 93684, 2 * 63562, QT)
print("D0 atlas pair: input agreement %d, image agreement %d" % (ia, im))
d0 = d0 and ia == 17 and im == 4
report("D0 control (Tribonacci prints reproduced)", d0)
if not d0:
    print("CONTROL FAILED -- no Narayana verdict is read.")
    sys.exit(1)

print("Narayana places q_0..q_11: %s" % QN[:12])

# ---------------------------------------------------------------- D1
# Lemma 0: the gap-3 language IS the greedy language, and its top sum
# on indices < k is q_k - 1.
d1 = True
tops = {}
for k in range(1, 19):
    best = 0
    for mask in range(1 << k):
        if mask & (mask << 1) or mask & (mask << 2):
            continue
        idx = {i for i in range(k) if mask >> i & 1}
        v = sum(QN[i] for i in idx)
        best = max(best, v)
        if digit_set(v, QN) != idx:
            d1 = False
    tops[k] = best
    if best != QN[k] - 1:
        d1 = False
print("D1 top admissible sum below k=18: %d, q_18 - 1 = %d"
      % (tops[18], QN[18] - 1))
report("D1 gap-3 language = greedy language, top sum = q_k - 1", d1)

# ---------------------------------------------------------------- D2
# Lemma A, and the boundaries below k = 7 printed rather than claimed.
d2 = all(2 * QN[k] == QN[k + 1] + QN[k - 2] + QN[k - 7]
         for k in range(7, DEPTH))
for k in range(7):
    print("D2 boundary 2 q_%d = %d = %s"
          % (k, 2 * QN[k], sorted(digit_set(2 * QN[k], QN))))
canon = all(gap3({k + 1, k - 2, k - 7}) for k in range(7, DEPTH))
report("D2 down-carry 2q_k = q_{k+1} + q_{k-2} + q_{k-7} (k>=7)", d2)
report("D2 that form is canonical (gap-3)", canon)

# ---------------------------------------------------------------- D3
# The comb scan: which step s gives an admissible comb whose members
# converge to one input limit?
steps = {}
for s in range(3, 31):
    lo = s
    Ks = [K for K in range(lo + 6 * s, lo + 12 * s, s)]
    adm = all(gap3(set(range(lo, K + 1, s))) for K in Ks)
    ag = [agree(comb_T(K, QN, lo, s), comb_T(K + s, QN, lo, s), QN)
          for K in Ks]
    grows = all(ag[i] < ag[i + 1] for i in range(len(ag) - 1))
    steps[s] = (adm, grows, ag)
    if s <= 12 or not (adm and grows):
        print("D3 step %2d: comb admissible %s, input agreements %s, "
              "grows %s" % (s, adm, ag, grows))
live = [s for s, (adm, grows, _) in steps.items() if adm and grows]
report("D3 at least one step gives a converging comb", bool(live))
print("D3 live steps: %s" % live)

# ---------------------------------------------------------------- D4
# The phase count, read as a limit: transient discarded, two depths,
# two range lengths. A count that differs across any of the four is a
# count still moving.
def phases(s_step, deep, span, tail=12, Q=None, off=None):
    """Distinct low-`deep` image strings over the LAST `tail` combs of a
    span-long run — deep in the tail, so the transient (whose length
    grows with `deep`) is excluded by construction rather than by a
    fixed drop."""
    Q = QN if Q is None else Q
    lo = s_step if off is None else off
    Ks = list(range(lo + (span - tail) * s_step, lo + span * s_step, s_step))
    strs = [greedy(2 * comb_T(K, Q, lo, s_step), Q)[:deep] for K in Ks]
    seen = []
    for x in strs:
        if x not in seen:
            seen.append(x)
    return seen


def image_gaps(s_step, Q, bottom=10, off=None):
    """The image's gap set above the bottom, over six consecutive combs."""
    lo = s_step if off is None else off
    gaps = set()
    for K in range(lo + 20 * s_step, lo + 26 * s_step, s_step):
        ds = [k for k in sorted(digit_set(2 * comb_T(K, Q, lo, s_step), Q))
              if k >= bottom]
        gaps |= {ds[i + 1] - ds[i] for i in range(len(ds) - 1)}
    return gaps


# ------------------------------------------------------------- D0b
# The control the extraction check does not give: the INSTRUMENTS that
# produce the finding, run on the window whose answer is a theorem.
tri_sel = [s_step for s_step in range(3, 21)
           if len(image_gaps(s_step, QT)) == 1]
tri_ph = len(phases(4, 80, 90, Q=QT))
print("D0b Tribonacci: selector picks %s; phase count at its forced "
      "step 4 = %d" % (tri_sel, tri_ph))
report("D0b the instrument reproduces the spine's theorem (3 phases at "
       "the forced step)", tri_ph == 3)
report("D0b the selector holds at the forced step, and the forced step "
       "is the least it holds at", bool(tri_sel) and min(tri_sel) == 4)

# D0c — the parameter the instrument fixes and the question leaves free:
# the comb's OFFSET, i.e. which residue class the teeth sit in.
off_ok = True
for Q, name, s_list in ((QT, "tribonacci", (4, 8)), (QN, "narayana", (5, 7, 9))):
    for s_step in s_list:
        ph = {len(phases(s_step, 80, 40, Q=Q, off=o))
              for o in range(s_step, 2 * s_step)}
        gp = {len(image_gaps(s_step, Q, off=o)) == 1
              for o in range(s_step, 2 * s_step)}
        print("D0c %s step %d: over all %d offsets, phase counts %s and "
              "selector verdicts %s" % (name, s_step, s_step, sorted(ph),
                                        sorted(gp)))
        off_ok = off_ok and len(ph) == 1 and len(gp) == 1
report("D0c the phase count and the selector's VERDICT are both "
       "invariant under the offset", off_ok)

d4 = True
counts = {}
for s_step in range(3, 31):
    row = [len(phases(s_step, deep, span))
           for deep in (40, 80) for span in (60, 90)]
    counts[s_step] = row[0]
    if len(set(row)) != 1:
        d4 = False
    if s_step <= 14:
        print("D4 step %2d: phase count %s at (depth 40/80) x (span 60/90)"
              % (s_step, row))
print("D4 phase count by step 3..30: %s"
      % [counts[k] for k in range(3, 31)])
report("D4 phase count stable in depth and in range at every step", d4)
report("D4 the count DEPENDS on the step (not a window invariant)",
       len(set(counts.values())) > 1)

# ---------------------------------------------------------------- D5
# The selector the spine satisfies for free: is the image a single-step
# comb above its bottom?
BOTTOM = 10
single = []
for s_step in range(3, 31):
    gaps = image_gaps(s_step, QN, BOTTOM)
    if True:
        print("D5 step %2d: image gaps above %d = %s%s"
              % (s_step, BOTTOM, sorted(gaps),
                 "   <== single-step image" if len(gaps) == 1 else ""))
    if len(gaps) == 1:
        single.append((s_step, gaps.pop()))
print("D5 steps with a single-step image, s = 3..30: %s" % single)
report("D5 the selector picks exactly one step", len(single) == 1)

if len(single) == 1:
    sel, img_step = single[0]
    ph = phases(sel, 80, 90)
    sep = max(next(t for t in range(80) if a[t] != b[t])
              for i, a in enumerate(ph) for b in ph[i + 1:])
    print("D5 selected step %d: image step %d, %d phases, separated at "
          "digit <= %d" % (sel, img_step, len(ph), sep))
    for i, a in enumerate(ph):
        print("     phase %d: %s" % (i, "".join(str(b) for b in a[:26])))
    Ks = list(range(sel + 78 * sel, sel + 90 * sel, sel))
    cyc = [ph.index(greedy(2 * comb_T(K, QN, sel, sel), QN)[:80]) for K in Ks]
    print("D5 phase visited, K stepping by %d: %s" % (sel, cyc))
    print("D5 period in K: %d (%d phases x step %d); phase set by K mod %d"
          % (len(ph) * sel, len(ph), sel, len(ph) * sel))
    report("D5 the visiting order is periodic with that period",
           all(cyc[i] == cyc[i % len(ph)] for i in range(len(cyc))))
    ag = [agree(comb_T(K, QN, sel, sel), comb_T(K + sel, QN, sel, sel), QN)
          for K in range(sel + 4 * sel, sel + 16 * sel, sel)]
    print("D5 selected step input agreements: %s" % ag)
    report("D5 at the selected step the inputs converge to ONE limit",
           all(ag[i] < ag[i + 1] for i in range(len(ag) - 1)))
    report("D5 x2 has no continuous extension (>=2 phases, bounded "
           "separating digit)", len(ph) >= 2 and sep < 80)

# ---------------------------------------------------------------- D7
# THE CASCADE THEOREM in range. The digits come from the greedy engine
# alone; the theorem supplies only the SET to compare against.
def theorem_row(m):
    """The proved canonical digit set of 2 T_{7m}, m >= 1."""
    top = 7 * m + 1
    bottom, first = {1: (0, 5), 2: (2, 6), 0: (4, 7)}[m % 3]
    return {bottom} | set(range(first, top + 1, 3))


d7 = True
for m in range(1, 41):
    K = 7 * m
    got = digit_set(2 * comb_T(K, QN, 7, 7), QN)
    if got != theorem_row(m):
        d7 = False
        print("D7 MISMATCH at m=%d: greedy %s, theorem %s"
              % (m, sorted(got), sorted(theorem_row(m))))
for m in (1, 2, 3):
    K = 7 * m
    print("D7 base 2 T_%d = %d = q_%s"
          % (K, 2 * comb_T(K, QN, 7, 7),
             " + q_".join(str(j) for j in
                          sorted(digit_set(2 * comb_T(K, QN, 7, 7), QN),
                                 reverse=True))))
report("D7 theorem rows = greedy digits at every m = 1..40", d7)

rows = [greedy(2 * comb_T(7 * m, QN, 7, 7), QN)[:26] for m in (1, 2, 3)]
seps = [min(t for t in range(26) if rows[i][t] != rows[j][t])
        for i, j in ((0, 1), (0, 2), (1, 2))]
print("D7 least differing digit, rows (1,2) (1,3) (2,3): %s" % seps)
report("D7 the rows separate at a digit <= 2", max(seps) <= 2)

# ---------------------------------------------------------------- D6
# The numeric torus shadow at the conjugate modulus.
def roots_cubic():
    """Roots of x^3 - x^2 - 1 by Durand-Kerner, no numpy."""
    def f(z):
        return z ** 3 - z ** 2 - 1
    r = [complex(0.4, 0.9) ** i for i in range(3)]
    for _ in range(500):
        new = []
        for i, zi in enumerate(r):
            d = 1
            for j, zj in enumerate(r):
                if i != j:
                    d *= (zi - zj)
            new.append(zi - f(zi) / d)
        r = new
    return r


rts = roots_cubic()
lam = max(rts, key=lambda z: abs(z)).real
mu = min(rts, key=lambda z: abs(z))
print("D6 roots: lambda = %.6f, |mu| = %.6f, predicted b^-1/2 = %.6f"
      % (lam, abs(mu), lam ** -0.5))


def plane_coord(n):
    d = greedy(n, QN)
    return sum(d[k] * mu ** k for k in range(DEPTH))


rates = []
for t in range(6, 18):
    cell = [n for n in range(1, 4000)
            if greedy(n, QN)[:t] == greedy(1, QN)[:t]]
    if len(cell) < 3:
        break
    pts = [plane_coord(n) for n in cell]
    diam = max(abs(a - b) for a in pts for b in pts)
    rates.append((t, diam))
for i in range(1, len(rates)):
    t, d = rates[i]
    t0, d0v = rates[i - 1]
    if d0v > 0:
        print("D6 depth %2d: cell diameter %.6f, ratio %.4f, |mu| = %.4f"
              % (t, d, d / d0v, abs(mu)))
report("D6 shadow measured (a shadow, never the classification)",
       len(rates) >= 3)

print("ALL: %s" % ok_all)
