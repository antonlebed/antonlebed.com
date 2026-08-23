"""Thirteen windows with no verdict: is the silence the WINDOW's, or the
INSTRUMENT's own extra condition?

THE QUESTION
------------
The census over the Pisot family (explore_pisot_confound.py) established
that the trailing windows' phase count is neither the recurrence's order
nor the image comb's step -- and established it with an instrument that
speaks at only 8 of the 21 legal binary windows. At the other 13 it picks
no step out to 40, so the corpus has NO verdict there on whether x2
extends continuously, and the completion atlas's fourth shape is stated
over the windows the instrument reaches rather than over the family.

THE INSTRUMENT ASKS FOR MORE THAN THE QUESTION NEEDS, and that is the
suspicion this rig is built on. The selector requires the doubled comb's
digit set to be a SINGLE-STEP comb above a bottom -- one gap value, three
teeth. That condition is what the spine's theorem hands over for free and
what the Narayana cascade proof reproduces, and it is what makes the
ARITHMETIC reading (count = image step / gcd) sayable at all. But the
discontinuity itself needs none of it. x2 fails to extend continuously
the moment a family converging to ONE input limit has images whose LOW
digits take at least two values -- at a bounded digit, infinitely often.
A digit set that is not a comb separates just as well as one that is.

So the silence at those 13 windows may be reporting the absence of an
ARITHMETIC STRUCTURE in the image, not the absence of a WITNESS. The two
have never been separated because on the spine and at Narayana they
arrive together.

THE OBSERVABLE THAT ANSWERS IT, and two nearby ones that cannot. A blind
SEARCH over pairs of integers for growing input agreement against capped
image agreement fails in both of its natural forms: reading the LEAST
image agreement inside a bucket of integers sharing a greedy prefix is
saturated, since a minimum over a growing pool finds its own extreme for
free and reads the floor even at the two windows whose answers are
theorems; and following ONE nested chain of prefixes gives a false
negative, image agreement growing steadily along it at those same two
windows. So neither form can decide this in either direction. What is
used here is neither: it is the COUNT OF
DISTINCT IMAGE PREFIXES AT A FIXED SMALL DEPTH, over combs whose
convergence is a property rather than a measurement. Adding a tooth above
an admissible comb disturbs no digit below it, so T_K and T_{K+s} agree
to the added tooth's own index and the family converges by construction.
Two distinct depth-D prefixes recurring out to large K is then exactly a
bounded separating digit against unbounded input agreement -- the kill,
read off the print and not inferred from it.

TRANSPLANTS, flagged at the freeze. The WITNESS COMB is imported from the
spine and carried through Narayana and the census: an arithmetic-
progression tooth set is one shape of witness, and the three-tooth carry
derived below is a reason to doubt it is the right one here. It is tested
rather than assumed, and its failure is a named kill (K2) with the
construction of a non-progression tooth set as the successor. The DEPTH-AND-SPAN
settings are imported from the census unchanged, for the same reason it
imported them from Narayana: retuning an instrument on the question it is
about to answer is how a depth-12 reading once returned 2 where the truth
was 1. What is NOT transplanted is the single-step-image condition, whose
removal is the whole hypothesis.

THE HAND-DERIVATION at 10101, on paper before the engine
--------------------------------------------------------
10101 is the shortest silent word. Its root is computed and printed by
the rig rather than named here. Its places, from the seeding rule
q_k = t_1 q_{k-1} + ... + t_k q_0 + 1 below the word's length and the
plain recurrence q_k = q_{k-1} + q_{k-3} + q_{k-5} above it, are
    1, 2, 3, 5, 8, 12, 19, 30, 47, 74, 116, 182, ...
(hand-computed, and confirmed against the seeding rule before this file
was written).

THE LANGUAGE. Parry's condition is that every shift of the digit string,
read high index to low, is strictly below (10100)^w. So: no two 1s
adjacent, AND no three 1s at spacings 2, 2 -- the factor 10101 is itself
forbidden, being equal to the reference through four places and above it
at the fifth. Neither a run-length condition (the spine's) nor a gap
condition (Narayana's).

THE DOWN-CARRY, derived and then checked numerically at one k before the
freeze. From q_{k+1} = q_k + q_{k-2} + q_{k-4},
    2 q_k = q_{k+1} + (q_k - q_{k-2} - q_{k-4}),
and substituting q_k = q_{k-1} + q_{k-3} + q_{k-5} then
q_{k-1} - q_{k-2} = q_{k-4} + q_{k-6},
    q_k - q_{k-2} - q_{k-4} = q_{k-3} + q_{k-5} + q_{k-6}.
The pair {k-6, k-5} is adjacent, hence inadmissible, and normalizes by
    (R2)  q_j + q_{j+1} = q_{j+2} + q_{j-5}      (j >= 5)
which follows from q_{j+2} = q_{j+1} + q_{j-1} + q_{j-3} together with
q_j - q_{j-1} = q_{j-3} + q_{j-5}. (Check: q_5 + q_6 = 12 + 19 = 31 and
q_7 + q_0 = 30 + 1 = 31.) R2 at j = k-6 gives {k-4, k-11}, and {k-4, k-3}
is adjacent in turn; R2 at j = k-4 gives {k-2, k-9}. So
    2 q_k = q_{k+1} + q_{k-2} + q_{k-9} + q_{k-11}      (k >= 11),
whose index gaps are 3, 7, 2 -- pairwise at least 2 and with no two
consecutive 2s, hence canonical. (Check at k = 11: 2 x 182 = 364 and
q_12 + q_9 + q_2 + q_0 = 286 + 74 + 3 + 1 = 364.)

WHAT THE CARRY SAYS ABOUT THE INSTRUMENT. The spine's carry has ONE low
tooth, Narayana's has TWO, and this one has THREE, at lags 2, 9 and 11.
A step-s comb's teeth each deposit four indices, and a deposit collides
with a lower tooth's raised index when s divides 3, 10 or 12. So at most
steps the deposits from different teeth land at unrelated offsets and the
image digit set carries several gap values -- a mechanism for the
selector's silence that has nothing to do with whether the low digits
separate. Three low teeth is also why the image need not be a comb: the
one-lag and two-lag carries are the cases where a single cascade can
close, and neither shape is available here.

THE HAZARDS, priced before the engine
-------------------------------------
(i) DEPTH IS A FLOOR ON AGREEMENT AND A CEILING ON THE COUNT. Two image
    strings agreeing past the read depth count as one (undercount), so a
    count of 1 at depth D is evidence only that the separation is not
    below D. The count is therefore read at a LADDER of depths and the
    ladder is printed; a count that rises with depth without settling is
    the instrument's and is reported as such (K4).
(ii) THE TAIL IS A CEILING ON THE COUNT, and the census learned this the
    expensive way: a count read over 12 samples cannot exceed 12, and
    10001's true count of 15 printed as 9. Counts are read at several
    tails and a count equal to its own tail is not a number.
(iii) THE OFFSET IS FREE AND THE QUESTION DOES NOT FIX IT. The comb's
    bottom index lo is a parameter the reading fixes at s; Narayana swept
    it and it changed nothing there. It is swept here, because a silence
    that is the offset's would be a different finding from one that is
    the window's.
(iv) A SEPARATION AT A DRIFTING DIGIT IS NOT A SEPARATION. The kill needs
    a BOUNDED digit, so the rig prints the least index at which two
    distinct phases differ, and prints it as read rather than as a
    consequence of the count. If that index grows with K the kill is not
    met however large the count is.
(v) THE CONVERGENCE MUST STILL BE MEASURED even though it is a property,
    because the property is about an ADMISSIBLE comb and admissibility is
    exactly what varies across this family. The rig tests it the way the
    census does -- greedy must reproduce the index set -- and never
    applies a language by hand.

THE PREDICTIONS, frozen before the engine
-----------------------------------------
P1  THE CONTROL. At the two windows whose answers are theorems the
    depth-ladder count returns 3: Tribonacci (111) at step 4 and Narayana
    (101) at step 7, both with a separating digit at most 2.
P2  The hand-derived carry holds: 2 q_k = q_{k+1} + q_{k-2} + q_{k-9} +
    q_{k-11} at 10101 for every k in 11..60, with the right side already
    canonical.
P3  THE FINDING SOUGHT. At 10101 some admissible growing comb of step
    s <= 40 has at least TWO distinct image prefixes at a depth at most
    20, so x2 has no continuous extension there and the corpus's blank
    was the selector's extra condition rather than a missing witness.
P4  And it is not one window's luck: every one of the 13 silent binary
    windows has such a comb.

THE KILLS, as observables and never as inferences
-------------------------------------------------
K1  Either theorem window prints a count other than 3, or a separating
    digit above 2 -> the instrument is wrong and NO silent-window row is
    read.
K2  At 10101 every admissible growing comb prints exactly ONE distinct
    prefix at every depth in the ladder and every tail -> the
    progression-shaped witness genuinely fails there, P3 dies, and the
    successor is the construction of a non-progression tooth set.
K3  No step in 3..40 is admissible and growing at 10101 -> there is no
    progression comb at all to read, which is a different failure from
    K2 and is reported separately. (The printed verdict widens this to
    ANY silent window, which is strictly stronger than the letter here
    and is what D3 can say for free.)
K4  A window's count rises at every rung of the depth ladder without
    settling, or equals its own tail -> that row is the instrument's and
    is printed and excluded from the verdict.
K5  A window's distinct prefixes differ only at an index that GROWS with
    K -> the separation is not at a bounded digit and that row does not
    witness a discontinuity, whatever its count.

THE DESIGN
----------
D0  POSITIVE CONTROL, run first and read before any silent-window row:
    the seeding rule at 111 and 101 against the two rigs' published place
    sequences, and the full depth-ladder pipeline at both against their
    published counts of 3 (P1). A construction that cannot recover a
    theorem is not evidence at a window that has none.
D1  The legality filter and the 21 legal binary words to length 6,
    reproducing the census's partition (5 all-ones, 4 sparse, 12 mixed)
    and its list of 13 silent words, so this rig's family is the census's
    and not a re-derived neighbour of it.
D2  The down-carry at 10101: the canonical digits of 2 q_k for k in
    11..60 against the hand-derived form, with the boundaries k < 11
    printed rather than claimed.
D3  Per silent window, per step s in 3..40: is the comb admissible (does
    greedy reproduce its index set), does the input agreement grow, how
    many gap values does the image digit set have (the selector's own
    reading, kept as a column so the silence's cause is visible), and the
    DEPTH LADDER -- distinct image prefixes at depths 4, 8, 12, 20, 40,
    80 over a fixed tail.
D4  For every (window, step) whose ladder settles above 1: the least
    index at which two distinct prefixes differ, the tail sweep at 12,
    30, 60, 120, and the visiting order with its least period MEASURED
    rather than inferred from the count.
D4b ADDED TO THE SLATE DURING THE BUILD AND BEFORE ANY FINDING WAS
    WRITTEN, because D4's tail sweep printed rows whose depth-80 count
    equalled its own tail at every tail -- a number sitting on its
    instrument's edge with no settled value at all. The question that
    raises is whether the LOW-depth count settles where the deep one does
    not, so: the depth-4 count at tails 60, 120, 240 and 480, at exactly
    the tail-capped rows. It is the leg F3's second half rests on and it
    is named here rather than left to the print.
D4c ADDED TO THE SLATE AFTER D0-D6 RAN AND FROZEN BEFORE IT RAN, because
    the kill has two halves and only one of them was controlled where it
    is read. Admissibility and growth are tested by comb_ok at
    K in [lo+6s, lo+12s), and every prefix above is read over
    K in [151s, 270s]. So over that WHOLE range -- both ends and the
    middle, because a control on a sub-range would repeat the same gap
    one layer in: does greedy still reproduce the comb's index set, and
    does the input agreement between consecutive members still RISE? A comb that stopped being admissible
    out there would make the reading a statement about some other family,
    and no print in D0-D6 would show it.
D5  The offset sweep at the windows P3 turns on: lo in s..s+4, asking
    whether the count and the separating digit are the offset's. Its
    counts are tail-12 SCREENS, so a number there can be a ceiling; the
    two things read off it — that a count is 1, and that a separating
    digit exists — are both immune to that, which is why the sweep is
    not re-run at the settled tail.
D6  THE TABLE: word, order, whether the selector spoke, the least step
    with a settled count above 1, that count, its separating digit, and
    the verdict on whether the silence was the instrument's.

D7  ADDED TO THE SLATE AFTER EVERYTHING ABOVE RAN AND FROZEN BEFORE IT
    RAN. F3 reports three windows whose depth-80 count equals its own
    tail at every tail tried, and reads that as the instrument's ceiling.
    It is also what an INFINITE image limit set looks like, and the two
    are told apart by one observable the rig never asked for: does the
    count keep tracking the tail as the tail grows?
    THE QUESTION. At 100001, 101001 and 110101, the number of distinct
    depth-80 prefixes at tails 120, 240 and 480. N distinct prefixes over
    N samples at every N means the image takes unboundedly many values
    that differ BELOW depth 80, and any two of those are different limit
    points over the one input limit -- so the limit set is infinite, which
    is a shape the completion atlas does not have: neither a ring, nor
    finitely many limit points over one input limit.
    THE CONTROL IS THE WHOLE PROBE and it runs first. A count that tracks
    its tail is exactly what a broken sampler prints, so the same sweep
    runs at windows whose counts are KNOWN small -- Tribonacci at step 4
    (3 phases, theorem) and 10101 at step 3 (5 phases, period 15) -- and
    they must SATURATE at 3 and 5 while the tail grows fortyfold. If they
    track their tails too, the instrument is counting samples and NO row
    is read.
    THE KILL, as an observable: any of the three saturates at some tail
    -> its limit set is finite after all, the depth-80 reading was a
    transient, and the fifth-shape reading dies. Reported as printed
    either way; this probe can only distinguish, never prove.

THE FINDINGS (every number below is copied from the printed output)
-------------------------------------------------------------------
F0  CONTROLS PASS, read before any silent-window row. The seeding rule
    reproduces both known place sequences from the word alone, and the
    DEPTH LADDER -- this rig's own observable, which the corpus had never
    run -- returns a settled 3 at both theorem windows: Tribonacci at
    step 4 counts 3 at every depth from 4 to 80 with separating digit 1,
    Narayana at step 7 counts 3 at every depth with separating digit 0
    (P1 met). And the family is the census's rather than a re-derived
    neighbour: 21 legal binary words to length 6, the selector speaking
    at 8 of them with the same least steps (3, 7, 4, 15, 5, 7, 6, 7) and
    silent at the same 13, over the same partition of 5 all-ones, 4
    sparse and 12 mixed.

F1  THE 10101 DOWN-CARRY HAS THREE LOW TEETH, and the hand-derived form
    is exact: 2 q_k = q_{k+1} + q_{k-2} + q_{k-9} + q_{k-11}, already
    canonical, at every k in 11..60 with no failure (RULE -- derived
    algebraically above and verified over that range). The spine's carry
    has ONE low tooth and descends by its single lag; Narayana's has TWO;
    this one has three, at lags 2, 9 and 11. The boundaries are printed
    rather than claimed: 2 q_k has two teeth for k in 1..3, 5, 6 and
    three for k = 4, 7..10.

F2  THE SILENCE WAS THE INSTRUMENT'S, AT ALL THIRTEEN WINDOWS. Every
    silent window carries admissible growing progression combs -- 38 of
    the 38 steps in 3..40 at twelve of them, and 35 at 100001, whose
    steps 3, 4 and 5 are the only inadmissible ones among the THIRTEEN,
    the eight speaking windows' steps not being counted here -- and
    at every one of the thirteen some step's image separates at DEPTH 4,
    which pins the separating digit at most 3 with no further argument.
    The least such step is 3 at eight windows, 4 at three, 6 at two
    (1101 and 100001). The settled depth-4 counts run 2, 5, 4, 3, 2, 5,
    8, 3, 2, 13, 2, 10, 5 and the separating digit READ off the prefixes
    is 0 at eleven of the thirteen and 1 at the other two. So x2 has no
    continuous extension at ANY of the thirteen windows the corpus had
    no verdict for (OBSERVATION -- distinct low prefixes recurring over
    120 samples, the tier the census's own counts carry), P3 and P4 both
    survive, and K2 is refuted: the progression-shaped witness works
    here, and what failed was the SINGLE-STEP-IMAGE condition the
    selector asks for on top of the question. The image digit sets say
    so directly -- at 10101 the steps 3..8 carry 3, 3, 3, 4, 3 and 2 gap
    values where the selector needs exactly one.

F3  AND THE COUNT SPLITS FROM THE SEPARATION, which is the finding the
    comb instrument could not have made. TEN of the thirteen have a
    least period in K over 200 samples, searched to 100 steps -- 6, 6, 8,
    9, 12, 12, 12, 15, 20, 51. That is an OBSERVATION and not the status
    the spine and Narayana have: there the cycle is proved and the images
    are KNOWN to have finitely many limit points, while here a period
    holding over 200 samples is consistent with a longer one it did not
    reach. THREE rows do not even have that: 100001, 101001 and
    110101 print 200 distinct depth-80 prefixes over 200 samples with no
    period at or below 100 steps, and their depth-80 count equals its own
    tail at every tail 12, 30, 60, 120 -- so that number is the
    instrument's and not the window's (K4 fires, exactly as designed).
    BUT THEIR LOW-DEPTH COUNT SETTLES ANYWAY: the depth-4 counts are 5, 8
    and 13, constant across tails 60, 120, 240 and 480. So at those three
    the LOW digits take finitely many values while the deeper prefix does
    not cycle within the sampled span: the separation is settled where
    the phase count is not. A rig that only ever looks at windows whose
    image is a comb cannot report that distinction, because a comb image
    makes the two readings the same one.
    THE TAIL-CAPPED SET IS NOT THE NO-PERIOD SET, and keeping the two
    apart is where this finding is easiest to get wrong. FOUR rows have
    their depth-80 count capped by the tail-12 reading -- those three and
    111011 -- but 111011 SETTLES, at 17 depth-80 phases of least period
    51 over a depth-4 count of 10. It is the depth hazard showing in one
    row, not a fourth window without a period.

F4  THE OFFSET MOVES WHERE THE SEPARATION SHOWS, NEVER WHETHER. Every
    admissible offset in s..s+4 separates at some bounded digit at every
    one of the thirteen. The depth-4 reading is offset-uniform at twelve;
    at 1101 with step 6 the offsets 9 and 10 count 1 at depth 4 while
    still separating, at digits 4 and 5. So a depth-4 screen can miss a
    separation the window has, which is hazard (i) firing at a real row
    and is why the ladder is printed rather than a single depth.

F5  WHAT THIS DOES NOT SETTLE. The counts are observations off finite
    runs, at the tier the census's 1001 count carried before Narayana's
    was proved; no cascade theorem is derived here for any silent
    window, and the three rows with no period have no finite count at
    all -- F7 reads their limit set as INFINITE and no proof of that is
    offered here. The three-tooth carry is derived only at
    10101; the other twelve silent windows' carries are not.

F6  AND THE OTHER HALF OF THE KILL IS NOW CONTROLLED WHERE IT IS READ.
    Over the whole K range each prefix above was read across -- 453..810
    for a step-3 comb, 604..1080 for a step-4 one, 906..1620 for a
    step-6 one, sampled at both ends and in the middle -- greedy still
    reproduces the comb's index set at every one of the thirteen, and the
    input agreement between consecutive members still rises, by exactly
    the added tooth's index: 456 to 813 at step 3 and 912 to 1626 at
    step 6. So at the top of every row's range the two inputs agree to
    depth 813 or beyond while their images differ at digit 0 or 1. That
    pair of numbers IS the discontinuity, and until D4c it was the half
    the rig asserted from a property and measured only near lo+10s.

F7  AND THE THREE ARE A FIFTH SHAPE, not an instrument's ceiling. The
    controls saturate exactly as a working sampler must: Tribonacci at
    step 4 prints 3, 3, 3 and 10101 at step 3 prints 5, 5, 5 across tails
    120, 240 and 480, so the count reads PHASES and not samples. At
    100001, 101001 and 110101 every sample is distinct at every one of
    those tails -- 120 of 120, 240 of 240, 480 of 480 depth-80 prefixes.
    Two prefixes differing below depth 80 are different limit points over
    the one input limit, so those windows carry unboundedly many
    (OBSERVATION, tails to 480; the probe distinguishes and cannot
    prove). That is a shape the completion atlas does not have: not a
    ring, and not finitely many image limit points over one input limit
    either -- which is what the spine's theorem, Narayana's cascade and
    every measured row before these three delivered. The fourth shape
    turns out to have been the FINITE case of something wider, and the
    thing that had hidden it is the same single-step-image demand: a comb
    image has finitely many phases by construction, so an instrument that
    only reads comb images cannot return this answer at all.

RUN RECORD: one process, 3.7 s wall-clock, ordinary-analysis footprint
well under the 512MB ceiling, no BLAS import. ALL prints True, so every
CHECK passed. The four False lines are VERDICTS and not failures: K3
(no silent window lacks a progression comb), K5 (no separating digit is
unbounded), K2 (the progression witness does NOT fail at 10101) and the
offset-uniformity of the depth-4 reading. Three of those four are False
because the finding went the rig's way; the fourth is F4.
"""

import bisect
import sys
import time

# WIDTH is the digit ceiling. It is raised above the census's 2000 because
# the spans read here reach higher K; the clip drops HIGH digits only, so a
# low prefix is unaffected either way, and raising it removes the question.
WIDTH = 6000
NPLACES = 6200

t0 = time.time()
ok_all = True


def report(label, ok):
    """A CHECK the rig must pass. Folds into ALL."""
    global ok_all
    ok_all = ok_all and ok
    print("%s: %s" % (label, ok))


def verdict(label, val):
    """A prediction's OUTCOME. A False here is a finding, not a failure,
    so it never folds into ALL."""
    print("VERDICT %s: %s" % (label, val))


# ---- the census's engine, copied unchanged (explore_pisot_confound.py)
def legal(t):
    """Parry: every shift of the zero-padded word is strictly below it."""
    n = len(t)
    if t[-1] == 0:
        return False
    ext = list(t) + [0] * (2 * n)
    for k in range(1, n):
        if not ext[k:k + n + 1] < ext[:n + 1]:
            return False
    return True


def binary_words(maxlen=6):
    out = []
    for n in range(2, maxlen + 1):
        for code in range(2 ** n):
            t = [(code >> (n - 1 - i)) & 1 for i in range(n)]
            if t[0] == 0:
                continue
            out.append(tuple(t))
    return out


def places(t, n=NPLACES):
    """The Parry seeding rule: the '+1' below length n is the whole point."""
    L = len(t)
    Q = [1]
    for k in range(1, n):
        if k < L:
            Q.append(sum(t[i] * Q[k - 1 - i] for i in range(k)) + 1)
        else:
            Q.append(sum(t[i] * Q[k - 1 - i] for i in range(L)))
    return Q


def greedy(v, Q):
    """Greedy digits, low index first."""
    d = [0] * WIDTH
    for k in range(bisect.bisect_right(Q, v) - 1, -1, -1):
        while Q[k] <= v:
            if k < WIDTH:
                d[k] += 1
            v -= Q[k]
    assert v == 0, v
    return tuple(d)


def digit_set(v, Q):
    return {k for k, b in enumerate(greedy(v, Q)) if b}


def comb_T(K, Q, lo, step):
    return sum(Q[j] for j in range(lo, K + 1, step))


def agree(a, b, Q):
    da, db = greedy(a, Q), greedy(b, Q)
    i = 0
    while i < WIDTH and da[i] == db[i]:
        i += 1
    return i


def comb_ok(Q, s, lo=None):
    """Admissible = greedy reproduces the index set. No language by hand."""
    lo = s if lo is None else lo
    Ks = list(range(lo + 6 * s, lo + 12 * s, s))
    for K in Ks:
        if digit_set(comb_T(K, Q, lo, s), Q) != set(range(lo, K + 1, s)):
            return False, False
    ag = [agree(comb_T(K, Q, lo, s), comb_T(K + s, Q, lo, s), Q) for K in Ks]
    return True, all(ag[i] < ag[i + 1] for i in range(len(ag) - 1))


def image_gaps(Q, s, bottom=10, lo=None):
    lo = s if lo is None else lo
    gaps, teeth = set(), []
    for K in range(lo + 20 * s, lo + 26 * s, s):
        ds = [k for k in sorted(digit_set(2 * comb_T(K, Q, lo, s), Q))
              if k >= bottom]
        teeth.append(len(ds))
        gaps |= {ds[i + 1] - ds[i] for i in range(len(ds) - 1)}
    return gaps, (min(teeth) if teeth else 0)


# ---- this rig's own observable
LADDER = (4, 8, 12, 20, 40, 80)


def prefixes(Q, s, deep, span=90, tail=12, lo=None):
    """The distinct depth-`deep` prefixes of the image, over the tail."""
    lo = s if lo is None else lo
    seen = []
    for K in range(lo + (span - tail) * s, lo + span * s, s):
        x = greedy(2 * comb_T(K, Q, lo, s), Q)[:deep]
        if x not in seen:
            seen.append(x)
    return seen


def ladder(Q, s, span=90, tail=12, lo=None):
    return [len(prefixes(Q, s, d, span, tail, lo)) for d in LADDER]


def sep_digit(pref):
    """Least index at which two of these prefixes differ. READ, not
    inferred: None when they are all equal."""
    best = None
    for i in range(len(pref)):
        for j in range(i + 1, len(pref)):
            a, b = pref[i], pref[j]
            for k in range(min(len(a), len(b))):
                if a[k] != b[k]:
                    best = k if best is None else min(best, k)
                    break
    return best


# ---------------------------------------------------------------- D0
print("--- D0 control: the seeding rule and the depth ladder at the two "
      "windows whose answers are theorems ---")
seed_ok = True
for t, want in (((1, 1, 1), [1, 2, 4, 7, 13, 24]),
                ((1, 0, 1), [1, 2, 3, 4, 6, 9])):
    got = places(t, 6)
    print("D0 word %s -> places %s (want %s)"
          % ("".join(map(str, t)), got, want))
    seed_ok = seed_ok and got == want
report("D0 the seeding rule reproduces both known place sequences", seed_ok)
if not seed_ok:
    print("SEEDING FAILED -- no row is read.")
    sys.exit(1)

ctrl_ok = True
for t, s_star in (((1, 1, 1), 4), ((1, 0, 1), 7)):
    Q = places(t)
    lad = ladder(Q, s_star)
    sd = sep_digit(prefixes(Q, s_star, 80))
    print("D0 word %s step %d: ladder at depths %s -> %s, separating digit %s "
          "(want a settled 3 and a digit <= 2)"
          % ("".join(map(str, t)), s_star, list(LADDER), lad, sd))
    ctrl_ok = ctrl_ok and lad[-1] == 3 and len(set(lad[2:])) == 1 and sd <= 2
report("D0 the depth ladder reproduces both published counts of 3 with a "
       "bounded separating digit", ctrl_ok)
if not ctrl_ok:
    print("CONTROL FAILED -- no silent-window row is read.")
    sys.exit(1)

# ---------------------------------------------------------------- D1
print("\n--- D1 the family, reproduced from the census rather than "
      "re-derived ---")
BIN = [t for t in binary_words() if legal(t)]
print("D1 legal binary words to length 6: %d -- %s"
      % (len(BIN), ["".join(map(str, t)) for t in BIN]))
SPOKE = []
for t in BIN:
    Q = places(t, 2600)
    picked = []
    for s in range(3, 41):
        adm, grows = comb_ok(Q, s)
        if not (adm and grows):
            continue
        g, teeth = image_gaps(Q, s)
        if len(g) == 1 and teeth >= 3:
            picked.append(s)
    if picked:
        SPOKE.append(("".join(map(str, t)), picked[0]))
SILENT = [t for t in BIN
          if "".join(map(str, t)) not in [w for w, _ in SPOKE]]
print("D1 the selector speaks at %d: %s" % (len(SPOKE), SPOKE))
print("D1 SILENT to s = 40 at %d: %s"
      % (len(SILENT), ["".join(map(str, t)) for t in SILENT]))
allones = [t for t in BIN if all(c == 1 for c in t)]
sparse = [t for t in BIN if len(t) > 2 and t[0] == 1 and t[-1] == 1
          and not any(t[1:-1])]
mixed = [t for t in BIN if t not in allones and t not in sparse]
print("D1 partition: %d all-ones, %d sparse 1 0..0 1, %d mixed"
      % (len(allones), len(sparse), len(mixed)))
report("D1 the census's partition and its 13 silent words are reproduced",
       len(BIN) == 21 and len(SILENT) == 13 and len(allones) == 5
       and len(sparse) == 4 and len(mixed) == 12)

# ---------------------------------------------------------------- D2
print("\n--- D2 the down-carry at 10101, against the hand-derived form ---")
W = (1, 0, 1, 0, 1)
QW = places(W, 200)
print("D2 places: %s" % QW[:12])
bad = []
for k in range(11, 61):
    want = {k + 1, k - 2, k - 9, k - 11}
    got = digit_set(2 * QW[k], QW)
    if got != want:
        bad.append((k, sorted(got)))
print("D2 2 q_k = q_{k+1} + q_{k-2} + q_{k-9} + q_{k-11} canonical for "
      "k in 11..60: failures %s" % bad)
report("D2 the hand-derived carry is the canonical form at 10101", not bad)
print("D2 the boundaries below k = 11, printed rather than claimed:")
for k in range(1, 11):
    print("     k=%2d: 2 q_%d = %d -> digits %s"
          % (k, k, 2 * QW[k], sorted(digit_set(2 * QW[k], QW))))

# ---------------------------------------------------------------- D3
print("\n--- D3 the silent windows, with the selector's own reading kept "
      "as a column so the cause of the silence is visible ---")
print("     (ladder read at span 60, tail 12 -- a SCREEN; the settled "
      "reading is D4's)")
rows = []
for t in SILENT:
    w = "".join(map(str, t))
    Q = places(t)
    hits = []
    for s in range(3, 41):
        adm, grows = comb_ok(Q, s)
        if not (adm and grows):
            continue
        pref = prefixes(Q, s, 80, span=60, tail=12)
        lad = [len({p[:d] for p in pref}) for d in LADDER]
        g, teeth = image_gaps(Q, s)
        hits.append((s, lad, len(g), teeth))
    rows.append(dict(t=t, w=w, hits=hits))
    if not hits:
        print("%-7s NO admissible growing comb at any s in 3..40" % w)
        continue
    best = [h for h in hits if h[1][-1] > 1]
    print("%-7s admissible growing steps %s; ladders %s"
          % (w, [h[0] for h in hits],
             ["s=%d:%s" % (h[0], h[1]) for h in hits[:6]]))
    print("        image gap-value counts %s (the selector needs exactly 1 "
          "with >= 3 teeth)"
          % ["s=%d:%d gaps,%d teeth" % (h[0], h[2], h[3]) for h in hits[:6]])
    print("        steps whose depth-80 count exceeds 1: %s"
          % [h[0] for h in best])
report("D3 every silent window has at least one admissible growing comb",
       all(r["hits"] for r in rows))
verdict("D3 K3: some silent window has NO progression comb at all",
        any(not r["hits"] for r in rows))

# ---------------------------------------------------------------- D4
print("\n--- D4 the settled reading at the least step whose DEPTH-4 count "
      "exceeds 1 -- depth 4 is chosen because a separation there pins the "
      "separating digit at most 3 without any further argument ---")
for r in rows:
    cand = [h for h in r["hits"] if h[1][0] > 1]
    r["s4"] = cand[0][0] if cand else None
    r["s80"] = ([h for h in r["hits"] if h[1][-1] > 1] or [(None,)])[0][0]
for r in rows:
    s = r["s4"]
    if s is None:
        print("%-7s no step in 3..40 separates at depth 4 (least step "
              "separating at depth 80: %s)" % (r["w"], r["s80"]))
        continue
    Q = places(r["t"])
    ts = []
    for tl in (12, 30, 60, 120):
        pref = prefixes(Q, s, 80, span=tl + 150, tail=tl)
        ts.append((len({p[:4] for p in pref}), len(pref)))
    pref = prefixes(Q, s, 80, span=270, tail=120)
    sd = sep_digit(pref)
    seen, seq = {}, []
    for K in range(s + 300 * s, s + 300 * s + 200 * s, s):
        x = greedy(2 * comb_T(K, Q, s, s), Q)[:80]
        seq.append(seen.setdefault(x, len(seen)))
    per = next((pp for pp in range(1, 101)
                if all(seq[i] == seq[i + pp] for i in range(len(seq) - pp))),
               None)
    r.update(s=s, tails=ts, sd=sd, phases=len(seen),
             period=None if per is None else per * s,
             visits=None if per is None else per // max(len(seen), 1))
    print("%-7s s=%2d  (depth-4 count, depth-80 count) by tail 12/30/60/120: "
          "%s" % (r["w"], s, ts))
    print("        separating digit %s (READ, not inferred); %d distinct "
          "depth-80 prefixes over 200 samples; least period %s in K; each "
          "visited %s per turn"
          % (sd, len(seen), r["period"], r["visits"]))
capped = [r["w"] for r in rows if r.get("tails")
          and any(c == t for c, t in [(x[1], y) for x, y in
                                      zip(r["tails"], (12, 30, 60, 120))])]
print("D4 rows whose depth-80 count equals its own tail at some tail (K4 -- "
      "the number is the instrument's, the separation is not): %s" % capped)
report("D4 every row that separates at depth 4 has a separating digit at "
       "most 3", all(r["sd"] <= 3 for r in rows if r.get("sd") is not None))
verdict("D4 K5: some separating digit is unbounded (no row separates at a "
        "bounded digit)", not any(r.get("sd") is not None for r in rows))

print("")
print("D4b the tail-capped rows again, asking whether the LOW-depth count "
      "settles where the depth-80 one does not:")
set_ok = True
for r in rows:
    if r.get("s") is None or r["w"] not in capped:
        continue
    Q = places(r["t"])
    cs = [len({p[:4] for p in prefixes(Q, r["s"], 8, span=tl + 150, tail=tl)})
          for tl in (60, 120, 240, 480)]
    print("     %-7s s=%2d depth-4 count by tail 60/120/240/480: %s"
          % (r["w"], r["s"], cs))
    set_ok = set_ok and len(set(cs[1:])) == 1
report("D4b every tail-capped row's depth-4 count is settled by tail 120",
       set_ok)

print("")
print("D4c the OTHER half of the kill, over the WHOLE K range the "
      "readings above span -- admissibility and growth are tested near "
      "lo+10s and every prefix above is read over K in [151s, 270s]:")
far_ok = True
for r in rows:
    if r.get("s") is None:
        continue
    s_star, Q = r["s"], places(r["t"])
    # the FULL range the readings above span, both ends and the middle --
    # a control on a sub-range would repeat, one layer in, the gap D4c
    # exists to close.
    Ks = ([s_star * m for m in range(151, 157)]
          + [s_star * m for m in range(210, 216)]
          + [s_star * m for m in range(265, 271)])
    adm = all(digit_set(comb_T(K, Q, s_star, s_star), Q)
              == set(range(s_star, K + 1, s_star)) for K in Ks)
    ag = [agree(comb_T(K, Q, s_star, s_star),
                comb_T(K + s_star, Q, s_star, s_star), Q) for K in Ks]
    grows = all(ag[i] < ag[i + 1] for i in range(len(ag) - 1))
    print("     %-7s s=%2d  K over %d..%d (both ends of the read range and "
          "its middle): greedy reproduces the comb %s; input agreement "
          "%d -> %d, rising %s"
          % (r["w"], s_star, Ks[0], Ks[-1], adm, ag[0], ag[-1], grows))
    far_ok = far_ok and adm and grows
report("D4c the comb is still admissible and the input agreement is still "
       "rising at the K every prefix above was read at", far_ok)

# ---------------------------------------------------------------- D5
print("\n--- D5 the offset sweep: is the separation the OFFSET's? ---")
off_ok = True
for r in rows:
    if r.get("s") is None:
        continue
    s, Q = r["s"], places(r["t"])
    out = []
    for lo in range(s, s + 5):
        adm, grows = comb_ok(Q, s, lo=lo)
        if not (adm and grows):
            out.append((lo, "not admissible/growing"))
            continue
        pref = prefixes(Q, s, 80, span=90, tail=12, lo=lo)
        out.append((lo, len({p[:4] for p in pref}), sep_digit(pref)))
    print("%-7s s=%2d  (offset, depth-4 count, separating digit): %s"
          % (r["w"], s, out))
    live = [o for o in out if len(o) == 3]
    r["off_sep"] = bool(live) and all(o[2] is not None for o in live)
    r["off_d4"] = bool(live) and all(o[1] > 1 for o in live)
    off_ok = off_ok and r["off_sep"]
report("D5 every admissible offset in s..s+4 still separates at SOME "
       "bounded digit", off_ok)
verdict("D5 and the DEPTH-4 reading is offset-uniform too",
        all(r.get("off_d4") for r in rows if r.get("s") is not None))
print("D5 windows where the depth-4 count drops to 1 at some offset while "
      "the separation survives at a higher bounded digit: %s"
      % [r["w"] for r in rows
         if r.get("s") is not None and r["off_sep"] and not r["off_d4"]])

# ---------------------------------------------------------------- D6
print("\n--- D6 the table ---")
print("     (the count column is the SETTLED tail-120 reading, never the "
      "tail-12 screen -- at 110101 those two differ, 13 against 7)")
print("     word    order  admissible steps 3..40  least s separating at "
      "depth 4  depth-4 count  separating digit  least period in K")
for r in rows:
    print("     %-7s %5d %23d  %24s  %13s  %16s  %16s"
          % (r["w"], len(r["t"]), len(r["hits"]), r.get("s", "-"),
             r["tails"][-1][0] if r.get("tails") else "-",
             r.get("sd", "-"), r.get("period") or "none <= 100 steps"))
wit = [r for r in rows if r.get("sd") is not None]
print("D6 silent windows with a witness to discontinuity: %d of %d"
      % (len(wit), len(rows)))
verdict("D6 P3: 10101 has a progression comb separating at a bounded digit",
        any(r["w"] == "10101" and r.get("sd") is not None for r in rows))
verdict("D6 P4: EVERY one of the 13 silent windows does",
        len(wit) == len(rows))
verdict("D6 K2: the progression-shaped witness fails at 10101 and a "
        "non-progression tooth set is needed",
        not any(r["w"] == "10101" and r.get("sd") is not None for r in rows))

# ---------------------------------------------------------------- D7
print("")
print("--- D7 is the no-period count the instrument's ceiling, or an "
      "INFINITE limit set? The control runs first and must saturate ---")
CTRL = [((1, 1, 1), 4, 3), ((1, 0, 1, 0, 1), 3, 5)]
ctrl_sat = True
for t, s_star, want in CTRL:
    Q = places(t)
    cs = [len(prefixes(Q, s_star, 80, span=tl + 150, tail=tl))
          for tl in (120, 240, 480)]
    print("     CONTROL %-7s s=%d: depth-80 count by tail 120/240/480: %s "
          "(want a flat %d)" % ("".join(map(str, t)), s_star, cs, want))
    ctrl_sat = ctrl_sat and cs == [want] * 3
report("D7 the controls SATURATE while the tail grows fourfold -- the "
       "instrument counts phases and not samples", ctrl_sat)
if not ctrl_sat:
    print("CONTROL FAILED -- no D7 row is read.")
else:
    tracks = []
    for r in rows:
        if r.get("s") is None or r["period"] is not None:
            continue
        Q = places(r["t"])
        cs = [len(prefixes(Q, r["s"], 80, span=tl + 150, tail=tl))
              for tl in (120, 240, 480)]
        hit = cs == [120, 240, 480]
        tracks.append(hit)
        print("     %-7s s=%d: depth-80 count by tail 120/240/480: %s  %s"
              % (r["w"], r["s"], cs,
                 "EVERY sample distinct" if hit else "SATURATES"))
    verdict("D7 all three no-period windows still track their tail at 480 "
            "-- the limit set is infinite at scanned scope", all(tracks))
    verdict("D7 K: some no-period window SATURATES and its limit set is "
            "finite after all", not all(tracks))


print("\nwall-clock %.1f s" % (time.time() - t0))
print("ALL: %s" % ok_all)
