"""Three numbers that have never disagreed: a recurrence's DEGREE, its
image comb's STEP, and its PHASE COUNT. Which one does the count track?

THE QUESTION
------------
Two theorems now stand. On the k-bonacci SPINE
(explore_tetranacci_window.py) the trailing window's down-carry doubles
a step-(d+1) witness comb into a step-d comb whose bottom cycles
through d phases, uniform in d. Off the spine
(explore_narayana_window.py) the Narayana window's selected step 7
doubles into a step-3 comb whose bottom cycles through 3 phases, and
Narayana's degree is 3.

So at every window the corpus has measured, three numbers coincide:
degree d, image step, phase count. On the spine they coincide BY the
theorem -- the carry descends by the single lag d, so the image step is
d and the bottom's return orbit has length d. Off the spine they
coincide by a cascade with a different mechanism entirely, and the
Narayana proof EXHIBITS its bottom orbit 0 -> 2 -> 4 -> 0 without
deriving the length 3 from the degree 3. Nothing in the corpus says
which of the three the count actually tracks, and one coincidence at
one off-spine member is not evidence that it must.

THE CONFOUND IS BROKEN BY WALKING MORE RECURRENCES -- but only if they
are SEEDED RIGHT, and that is where the cheap version of this question
fails. A window's places are not free: they are forced by the
admissible language, which is forced by the beta-expansion of 1.
Seeding an off-spine window with the spine's own 1, 2, 4, 8, ... builds
a sequence that is not the greedy numeration of anything, and every
number read off it is an artifact. Narayana's true places begin
1, 2, 3, not 1, 2, 4.

THE SEEDING RULE (Parry; this is the rule the question turns on)
---------------------------------------------------------------
Let d(1, beta) = t_1 ... t_n be the beta-expansion of 1, finite, with
t_n >= 1 (a SIMPLE Parry number). Then
    q_0 = 1
    q_k = t_1 q_{k-1} + ... + t_k q_0 + 1        (1 <= k < n)
    q_k = t_1 q_{k-1} + ... + t_n q_{k-n}        (k >= n)
The "+ 1" is exactly the clause a transplanted seeding drops, and it is
what makes q_k = 1 + (the largest admissible sum on indices < k). The
corpus's two known seed vectors are the test: Tribonacci is t = 111 and
must give 1, 2, 4; Narayana is t = 101 and must give 1, 2, 3.
Admissibility is Parry's: the digit string, read high index to low, has
every suffix strictly below (t_1 ... t_{n-1} (t_n - 1))^w -- run-length
free on the spine, gap-3 at Narayana, and neither in general. The rig
never applies that condition by hand: it tests a candidate index set by
asking whether GREEDY reproduces it, which is the same test and cannot
inherit a language from the wrong window.

WHICH WORDS ARE LEGAL. A finite word t_1 ... t_n over the digits, with
t_n >= 1, is d(1, beta) for some beta > 1 iff every shift of its
zero-padded infinite extension is strictly below it lexicographically
(Parry) -- the nonzero final digit being one clause of that filter and
not a restriction on what is enumerated. So the family is enumerated
and FILTERED rather than named,
and the filter is printed: 1011 fails (its shift 11... exceeds 10...),
1101 and 1001 pass. Whether the root is PISOT is computed and printed
alongside, never assumed -- the completion story the corpus tells needs
it, and a non-Pisot member's row is reported as such rather than
silently mixed in.

TRANSPLANTS, flagged at the freeze. The WITNESS COMB and the
SINGLE-STEP-IMAGE SELECTOR are both imported -- the first from the
spine, the second made explicit at Narayana. They are the instrument
here, not the object, and the instrument is controlled at both windows
whose answers are theorems before any new row is read. What is NOT
transplanted is any expectation about the numbers: the degree is read
off the word, the step off the scan, the count off the run.

THE HAND-ATTACK, on paper before the engine
-------------------------------------------
The statistic is a COUNT OF DISTINCT STRINGS, so its algebra can blow
up in exactly two ways and both are the instrument's rather than the
window's. (i) It is read at a finite DEPTH, so two strings that agree
past the depth read as one -- undercount. (ii) It is read over a finite
SPAN of K, so a transient that has not cleared reads as extra
phases -- overcount. The Narayana rig priced both: a first instrument
at depth 12 returned 2 where the truth is 1, and 3 where it was right
by luck. The settings that survived there -- depth 40 and 80 crossed
with span 60 and 90, counted over the TAIL -- are carried here
UNCHANGED rather than retuned, because retuning an instrument on the
question it is about to answer is how the depth-12 reading happened.
A count that differs across the four is printed as unstable and is not
a row.

The DENOMINATOR-shaped hazard here is the selector, not the count: the
selector reads image gaps ABOVE A BOTTOM, and the bottom is a
parameter. Set it too low and the bottom tooth's own gap enters the
gap set, so every window fails the criterion; too high and a short comb
has too few teeth above it to have gaps at all -- and a gap set that is
EMPTY or a singleton by having only two teeth passes the criterion for
the wrong reason. So the tooth count above the bottom is carried
alongside the gap set and a row needs at least three teeth to qualify.

A second hazard is arithmetic rather than statistical, and it is the
one the digits engine can hide: off the binary alphabet a place can be
used TWICE, so greedy must subtract in a loop rather than once, and a
digit array of 0/1 would silently truncate. The engine loops, and the
words are enumerated over digits up to 2 so that the loop is exercised
rather than assumed dead.

THE PREDICTIONS, frozen before the engine
-----------------------------------------
P1  The seeding rule reproduces both known seed vectors from the word
    alone: t = 111 gives 1, 2, 4 and t = 101 gives 1, 2, 3.
P2  The controls pass at both theorem windows: Tribonacci's least
    selected step is 4 with image step 3 and 3 phases; Narayana's is 7
    with image step 3 and 3 phases.
P3  THE FINDING SOUGHT: some legal word in the family returns a triple
    (degree, image step, phase count) whose three entries are not all
    equal. P3 is what this rig exists to kill.
P4  If P3 survives, the count tracks the IMAGE STEP and not the
    degree: phase count = image step at every row where the selector
    picks a step. This is the reading the spine and Narayana are both
    consistent with, and it is the one a separating row can refute.

THE KILLS, as observables and never as inferences
-------------------------------------------------
K1  The seeding rule prints a place sequence different from 1, 2, 4 or
    1, 2, 3 at the two known words -> the rule is wrong, and NO row is
    read; the whole family would be an artifact of a bad seeding,
    which is the failure this rig was built to avoid.
K2  Every legal row prints degree = image step = phase count -> P3
    dies, the confound does not break in this family, and the corpus's
    one-number reading survives a real attempt on it.
K3  Some row's phase count differs across the four depth-by-span
    combinations -> that row is unstable and is not evidence in either
    direction; it is printed and excluded.
K4  The selector picks NO step at some legal window -> the SELECTOR is
    what breaks rather than the reading, and the criterion made
    explicit at explore_narayana_window.py is not general.

THE DESIGN
----------
D0  POSITIVE CONTROL, run first and read before any new row: the
    seeding rule at t = 111 and t = 101 against the two rigs' place
    sequences, and the full pipeline at both against their published
    answers (P2's triples).
D1  The legality filter over every word of length 2..6 on digits 0..2
    with a NONZERO LEADING digit -- the nonzero FINAL digit is part of
    the filter and not of the enumeration, which is why the printed
    rejects include 10, 20 and 1000. Parry's shift condition, with the
    rejects printed at length <= 4 so the filter is visible.
D2  The root: all roots by Durand-Kerner, and the Pisot verdict
    printed per word rather than assumed.
D3  The places: the seeding rule, plus the exhaustive check that the
    largest value whose greedy digits all sit below k is q_k - 1, for
    k <= 14, at the two control words. D3b, ADDED AFTER THE RUN AND
    FROZEN BEFORE IT RAN, carries that check to EVERY legal word,
    because the brute force covers two binary words while every row of
    the census rests on the same rule -- and the rule's failure is the
    exact failure this rig exists to avoid. Its O(1) form: every value
    whose digits sit below k is below q_k, so the largest is q_k - 1
    precisely when q_k - 1's own top index is below k.
D4  The scan, per window: over s = 3..20, is the step-s comb
    admissible (greedy reproduces its index set), do its members
    converge to one input limit, is the image a single-step comb above
    index 10, and how many teeth stand above that bottom.
D5  The phase count at the least selected step, at depth 40 and 80
    crossed with span 60 and 90, over the tail.
D6  THE TABLE: word, degree, Pisot, least selected step, image step,
    phase count -- and the verdict on whether the three numbers
    separate.

D7  ADDED TO THE SLATE AFTER D0-D6 RAN AND FROZEN BEFORE IT RAN,
    because D6's prints named a dial the hand-attack missed and a
    stratification the frozen verdict lines did not make:
    (a) THE TAIL SWEEP. The count is read over `tail` samples, so
        `tail` is a CEILING on it and not only a window onto it -- a
        count of 9 read from 12 samples is a number sitting at its own
        instrument's edge. Counts at tail 12, 30, 60, 120 crossed with
        two depth-span settings, at every window where the selector
        picks.
    (b) THE SELECTOR RE-SCAN to s = 40 at every binary window where
        s = 3..20 picked nothing, so "picks nothing" is separated from
        "picks something above 20" -- 1001 needs s = 15, so the
        distinction is live rather than hypothetical.
    (c) THE ALPHABET SPLIT, read observably rather than argued: at a
        word with t_1 >= 2, are the greedy digits of 2 T_K exactly the
        digit 2 sitting on the comb's own positions? If so the
        doubling carries NOTHING there, the image IS the witness, and
        a count of 1 measures the alphabet rather than the window.
    (d) The corrected table over the selecting binary windows, with
        the arithmetic reading count = image step / gcd(image step,
        s*) stated and checked row by row rather than asserted.

THE FINDINGS (every number below is copied from the printed output)
-------------------------------------------------------------------
F0  CONTROLS PASS, read before any new row. The seeding rule
    reproduces both known place sequences from the WORD alone --
    t = 111 gives 1, 2, 4, 7, 13, 24 and t = 101 gives 1, 2, 3, 4, 6,
    9 (P1 met) -- and the pipeline reproduces both published triples:
    Tribonacci s* = 4, image step 3, 3 phases; Narayana s* = 7, image
    step 3, 3 phases (P2 met). The places are the greedy numeration's:
    the largest value whose digits sit below k is q_k - 1 at every
    k <= 14 at both words, by brute force over every value.
    AND THAT CONTROL WAS NARROWER THAN THE CLAIM IT LICENSED, UNTIL
    D3b. The brute force covers two BINARY words of length 3, while
    every row of the census rests on the same seeding -- 172 of them
    over a digit-2 alphabet -- and a wrong seeding is precisely the
    artifact this rig exists to avoid. D3b carries the property to all
    193 legal words at k <= 24 with no failure, so the family's places
    are the greedy numeration's throughout and the rows stand. The
    filter is Parry's and it bites: 726 words scanned, 193 legal, 1011
    rejected.

F1  THE CONFOUND BREAKS, and the breaking row is 1001
    (beta = 1.38028, root of x^4 = x^3 + 1, irreducible over Z and
    Pisot -- conjugate moduli 0.819, 0.940, 0.940). The selector picks
    s* = 15 ALONE (rule at scanned scope, s = 3..20) and the image is
    a single-step comb of step 9; its bottom cycles through THREE
    phases, visited in one orbit of least period 45 in K
    (OBSERVATION -- a limit claim read off a finite run, which is the
    tier Narayana's own count carried until it was proved). Order 4, image step 9, phase count 3: the three numbers that
    had never disagreed are three different numbers at one window.
    So P3 SURVIVES and the corpus's one-number reading is dead. The
    count is NOT the degree -- 1001 has order and algebraic degree 4
    and counts 3.

F2  AND IT IS NOT THE IMAGE STEP EITHER (P4 REFUTED). 1001 counts 3
    against image step 9, and 10001 counts 15 against image step 5.
    What holds at seven of the eight selecting windows is arithmetic
    rather than either: count = image step / gcd(image step, s*) --
    the image comb's teeth are spaced `img` while the top tooth
    advances by s* each step, so IF the phase were a function of the
    top tooth's residue mod img it would return after
    img/gcd(img, s*) steps. That reading gives 2, 3, 3, 3, 4, 5, 6
    correctly and gives 5 at 10001, where the measurement is 15. It is
    an OBSERVATION with a named exception, not a rule.
    AND THE EXCEPTION IS SHARPER THAN A MISS, because the reading's
    PREMISE is checked and holds there: the image top tooth advances
    by exactly s* at 10001 as it does at 1001, 101 and 1111 (measured
    over five consecutive K at each). So what fails at the plastic
    window is the "if" -- the phase is NOT a function of the top
    tooth's residue there, and carries something the other seven
    windows' phases do not. THE PERIODS ARE MEASURED AND NEVER
    INFERRED FROM count x step, and that is what exposed the second
    half of it: at seven of the eight the phases form ONE orbit and
    the least period is count x s* (6, 21, 12, 45, 20, 30, 42); at
    10001 the least period is 210 where count x s* would give 105,
    and each of the 15 phases is visited TWICE per turn. So the
    plastic window departs twice over -- in the count and in the
    orbit -- and the second departure is invisible to any rig that
    computes a period from its own count.

F3  THE EXCEPTION IS THE PLASTIC NUMBER, and it is the row where the
    word's order and beta's degree come apart. 10001 is d(1, beta) for
    beta = 1.32472, and x^5 - x^4 - 1 = (x^2 - x + 1)(x^3 - x - 1):
    beta is the root of x^3 = x + 1, the smallest Pisot number,
    algebraic degree 3 while the numeration's recurrence has order 5.
    Its count is 15 = 3 x 5, and 5 is what the arithmetic reading
    predicts. (Settled at explore_cyclotomic_ghost.py: the seeded
    places carry a periodic component on the cofactor x^2 - x + 1 --
    the cyclotomic ghost -- and 15 = lcm(5, 3) and the period 210 are
    its numbers read with the arithmetic reading; which words carry
    such a component is a divisibility criterion on the word's length,
    and this row stays the only one whose comb reads it. The
    exception stands as recorded here.) THE PISOT FLAG IN THE TABLE IS
    COMPUTED ON THE WORD'S
    OWN COMPANION POLYNOMIAL AND SO CAN LIE IN ONE DIRECTION: it
    prints False here because the cyclotomic factor contributes roots
    ON the unit circle, not because beta fails to be Pisot. Every
    False in the printed table is that ambiguity and is read as
    "reducible or non-Pisot", never as "non-Pisot".
    AND THE PLASTIC ROW CARRIES ITS OWN SPECIMEN OF THE SEEDING TRAP.
    The greedy numeration of that beta is q_k = q_{k-1} + q_{k-5},
    read off d(1, beta) = 10001 and confirmed algebraically:
    beta^3 = beta + 1 gives beta^5 = beta^4 + 1. It is NOT
    q_k = q_{k-2} + q_{k-3}, the recurrence the minimal polynomial
    reads off directly -- 1, 2, 3, 4, 5, 6, 8, 11 against
    1, 2, 3, 4, 5, 7, 9, 12. Both are honest recurrences for the same
    number and only the first is its greedy numeration, so a walk that
    takes the minimal polynomial's recurrence measures a sequence the
    admissible language does not govern. The trap is not exotic: it is
    what reading a recurrence off the ALGEBRA rather than off the
    beta-expansion of 1 does at any word whose two disagree.

F4  THE SELECTOR IS NOT GENERAL, AND THIS IS THE OTHER HALF OF THE
    REOPEN (observation, binary words to length 6, steps to 40). It
    picks a step at 8 of the 21 legal binary windows and is SILENT at
    the other 13 -- 1101, 10101, 11001, 11011, 11101, and every legal
    word of length 6 except 111111. The re-scan to s = 40 is what
    makes this a finding rather than a scan boundary: 1001 needs
    s = 15, so a silence at s = 20 would have proved nothing. THE
    PARTITION IS EXACT AND IS NOT TWO CLEAN FAMILIES. The 21 legal
    binary words split into 5 all-ones words, 4 of the form
    1 0...0 1, and 12 MIXED. All five all-ones words speak -- they
    are the k-bonacci spine. Every one of the twelve mixed words is
    silent. And the sparse family SPLITS: 101, 1001 and 10001 speak,
    while 100001 does not, so the silent 13 are the twelve mixed
    words plus one member of the family that otherwise speaks. The
    instrument the tower's theorem gets for free is therefore not a
    property of two families either; the spine is the only family it
    covers whole, and where its other members stop is itself
    unexplained. (This is a statement about the INSTRUMENT and it
    stands. The WINDOWS it is silent at were settled afterwards by
    explore_silent_window.py, which drops the single-step-image
    condition the refusal never needed: all 13 refuse the ring.)

F5  AND THE COMB INSTRUMENT IS ALMOST BLIND OFF THE BINARY ALPHABET
    (observation, swept over all 172 legal words with t_1 >= 2). The
    phase count is 1 at 169 of them, and the mechanism is the one the
    alphabet suggests: the greedy digits of 2 T_K are the digit 2
    sitting on the comb's own positions, so the doubling carries
    NOTHING, the image IS the witness, and one limit point sits over
    one input limit. Those rows measure the alphabet, not the window.
    BUT IT IS NOT A PROPERTY, AND THE SWEEP IS WHY. The no-carry
    mechanism holds at 158 of the 172 and FAILS at 14, every one of
    them beginning 2 0 -- where a digit 2 over a run of zeros meets
    the admissibility condition. And the count is not 1 at three of
    those: 2002, 20002 and 200002 each carry TWO phases. So the
    alphabet reading is the bulk story and not a universal, and the
    exceptions are the words 2 0...0 2. A first version of this
    finding claimed the universal off three sampled words, and the
    rig's own printed table already contradicted it at 2002. D6'S OWN
    P3 LINE IS CONTAMINATED BY EXACTLY THIS and is kept as printed:
    it counts 180 "separating" rows because a count of 1 differs from
    the degree, where the honest count is the two of F1-F2. The
    frozen verdict line asked whether three numbers differ and never
    asked whether the witness witnessed anything.

F6  THE TAIL WAS A CEILING AND THE FREEZE MISSED IT. D5's instrument
    reads the count over 12 samples, so it cannot report more than 12
    phases -- a cap, not a window. Every window whose count is small
    is unaffected and prints the same number at tails 12, 30, 60, 120;
    10001 prints 10, 9, 15, 15, 15, 15, 15, 15 across the tail sweep,
    so its D5 reading of 9 was the instrument's edge and its count is
    15. The hand-attack named the DEPTH hazard and the SPAN hazard,
    inherited both from the Narayana rig's own instrument note, and
    inherited the tail with them without asking what it bounded. A
    count statistic read over N samples is bounded by N, and a rig
    that carries a validated instrument forward carries its
    unexamined dials too.

RUN RECORD: one process, 3.8 s wall-clock, ordinary-analysis footprint
well under the 512MB ceiling, no BLAS import. ALL prints True: the
engine's checks pass and the two False lines are VERDICTS -- P4 and
the arithmetic reading -- which are findings and not failures.
"""

import bisect
import sys
import time
from math import gcd

WIDTH = 2000
NPLACES = 2200
MAXDIG = 2

t0 = time.time()
ok_all = True


def report(label, ok):
    """A CHECK the rig must pass. Folds into ALL."""
    global ok_all
    ok_all = ok_all and ok
    print("%s: %s" % (label, ok))


def verdict(label, val):
    """A prediction's OUTCOME. A False here is a finding, not a failure,
    so it never folds into ALL -- ALL is the engine's health and must
    not read as broken because the mathematics said no."""
    print("VERDICT %s: %s" % (label, val))


# ---------------------------------------------------------------- D1
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


def words(maxlen=6):
    out = []
    for n in range(2, maxlen + 1):
        for code in range((MAXDIG + 1) ** n):
            t, c = [], code
            for _ in range(n):
                t.append(c % (MAXDIG + 1))
                c //= (MAXDIG + 1)
            t = t[::-1]
            if t[0] == 0:
                continue
            out.append(tuple(t))
    return out


ALL = words()
LEGAL = [t for t in ALL if legal(t)]
rej = [t for t in ALL if len(t) <= 4 and not legal(t)]
print("D1 words scanned %d, legal %d" % (len(ALL), len(LEGAL)))
print("D1 rejects at length <= 4 (first 24): %s"
      % ["".join(map(str, t)) for t in rej][:24])
report("D1 the two known words are legal",
       (1, 1, 1) in LEGAL and (1, 0, 1) in LEGAL)
report("D1 the illegal word 1011 is rejected", (1, 0, 1, 1) not in LEGAL)


# ---------------------------------------------------------------- D2
def roots(t):
    """Roots of x^n - t_1 x^{n-1} - ... - t_n, Durand-Kerner, no numpy."""
    n = len(t)
    coef = [1.0] + [-float(c) for c in t]

    def f(z):
        v = 0j
        for c in coef:
            v = v * z + c
        return v

    r = [complex(0.4, 0.9) ** i for i in range(n)]
    for _ in range(600):
        new = []
        for i, zi in enumerate(r):
            d = 1 + 0j
            for j, zj in enumerate(r):
                if i != j:
                    d *= (zi - zj)
            new.append(zi - f(zi) / d)
        r = new
    return r


def beta_and_pisot(t):
    rs = roots(t)
    b = max(rs, key=lambda z: z.real if abs(z.imag) < 1e-7 else -9.0)
    others = [z for z in rs if abs(z - b) > 1e-7]
    return b.real, all(abs(z) < 1 - 1e-9 for z in others)


# ---------------------------------------------------------------- D3
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
    """Greedy digits, low index first. The while-loop is load-bearing off
    the binary alphabet, where a place can be used more than once."""
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


def top_admissible(Q, kmax=14):
    """Largest value whose greedy digits all sit below k, brute force."""
    out = {}
    for k in range(1, kmax + 1):
        best = 0
        for v in range(1, Q[k]):
            if max(digit_set(v, Q)) < k:
                best = max(best, v)
        out[k] = best
    return out


# ---------------------------------------------------------------- D4/D5
def image_gaps(Q, s, bottom=10, lo=None):
    lo = s if lo is None else lo
    gaps, teeth = set(), []
    for K in range(lo + 20 * s, lo + 26 * s, s):
        ds = [k for k in sorted(digit_set(2 * comb_T(K, Q, lo, s), Q))
              if k >= bottom]
        teeth.append(len(ds))
        gaps |= {ds[i + 1] - ds[i] for i in range(len(ds) - 1)}
    return gaps, (min(teeth) if teeth else 0)


def phases(Q, s, deep, span, tail=12, lo=None):
    lo = s if lo is None else lo
    seen = []
    for K in range(lo + (span - tail) * s, lo + span * s, s):
        x = greedy(2 * comb_T(K, Q, lo, s), Q)[:deep]
        if x not in seen:
            seen.append(x)
    return seen


def comb_ok(Q, s, lo=None):
    """Admissible = greedy reproduces the index set. No language by hand."""
    lo = s if lo is None else lo
    Ks = list(range(lo + 6 * s, lo + 12 * s, s))
    for K in Ks:
        if digit_set(comb_T(K, Q, lo, s), Q) != set(range(lo, K + 1, s)):
            return False, False
    ag = [agree(comb_T(K, Q, lo, s), comb_T(K + s, Q, lo, s), Q) for K in Ks]
    return True, all(ag[i] < ag[i + 1] for i in range(len(ag) - 1))


def walk(t, smax=20, verbose=False):
    """One window, end to end. Returns the row."""
    Q = places(t)
    beta, pisot = beta_and_pisot(t)
    sel = []
    for s in range(3, smax + 1):
        adm, grows = comb_ok(Q, s)
        if not (adm and grows):
            continue
        gaps, teeth = image_gaps(Q, s)
        if verbose:
            print("     s=%2d: image gaps %s, teeth above bottom %d"
                  % (s, sorted(gaps), teeth))
        if len(gaps) == 1 and teeth >= 3:
            sel.append((s, sorted(gaps)[0]))
    row = dict(t=t, beta=beta, pisot=pisot, deg=len(t), sel=sel or None,
               Q=Q[:6])
    if sel:
        s_star, img = sel[0]
        counts = [len(phases(Q, s_star, deep, span))
                  for deep in (40, 80) for span in (60, 90)]
        row.update(s_star=s_star, img=img, counts=counts,
                   stable=len(set(counts)) == 1)
    return row


# ---------------------------------------------------------------- D0
print("\n--- D0 control: the seeding rule and the pipeline at the two "
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
for t, want in (((1, 1, 1), (4, 3, 3)), ((1, 0, 1), (7, 3, 3))):
    r = walk(t)
    print("D0 word %s: least selected step %s, image step %s, phases %s "
          "(want %s)" % ("".join(map(str, t)), r.get("s_star"),
                         r.get("img"), r.get("counts"), list(want)))
    ctrl_ok = ctrl_ok and r.get("sel") and r["stable"] and \
        (r["s_star"], r["img"], r["counts"][0]) == want
report("D0 the pipeline reproduces both published triples", bool(ctrl_ok))
if not ctrl_ok:
    print("CONTROL FAILED -- no row is read.")
    sys.exit(1)

d3 = True
for t in ((1, 1, 1), (1, 0, 1)):
    Q = places(t)
    tops = top_admissible(Q)
    bad = [k for k, v in tops.items() if v != Q[k] - 1]
    print("D3 word %s: largest admissible value below k equals q_k - 1 for "
          "k <= 14, brute force over every value, failures %s"
          % ("".join(map(str, t)), bad))
    d3 = d3 and not bad
report("D3 the places are the greedy numeration's, brute force at the two "
       "control words", d3)

# D3b -- ADDED AFTER THE RUN, frozen before it ran. The brute force above
# controls the SEEDING RULE at two binary words while every row of the
# census uses it, digit-2 and length-6 words included. The same property
# has an O(1) form: every value whose greedy digits sit below k is < q_k
# because greedy takes the largest place <= v, so the largest such value
# is q_k - 1 exactly when q_k - 1 itself has top index < k.
d3b = [("".join(map(str, t)), k) for t in LEGAL for k in range(1, 25)
       if max(digit_set(places(t, 60)[k] - 1, places(t, 60))) >= k]
print("D3b the same property at every one of the %d legal words, k <= 24: "
      "failures %s" % (len(LEGAL), d3b))
report("D3b the seeding rule is the greedy numeration's at EVERY word the "
       "census reads, not only at the controls", not d3b)

# ---------------------------------------------------------------- D2/4/5/6
print("\n--- D2/D4/D5/D6 the family ---")
rows = []
for t in LEGAL:
    w = "".join(map(str, t))
    r = walk(t)
    if r["sel"] is None:
        print("%-7s deg %d  beta %.5f  pisot %-5s  SELECTOR PICKS NOTHING "
              "in s=3..20   places %s"
              % (w, r["deg"], r["beta"], r["pisot"], r["Q"]))
    else:
        print("%-7s deg %d  beta %.5f  pisot %-5s  s*=%2d  image step %d  "
              "phases %s%s   selected %s   places %s"
              % (w, r["deg"], r["beta"], r["pisot"], r["s_star"], r["img"],
                 r["counts"], "" if r["stable"] else "  UNSTABLE",
                 [s for s, _ in r["sel"]], r["Q"]))
    rows.append(r)

good = [r for r in rows if r["sel"] and r["stable"]]
sep = [r for r in good if len({r["deg"], r["img"], r["counts"][0]}) > 1]
print("\nD6 rows with a stable count: %d of %d" % (len(good), len(rows)))
print("D6 rows where degree, image step and phase count are NOT all equal: "
      "%d" % len(sep))
for r in sep:
    print("     %-7s degree %d, image step %d, phase count %d"
          % ("".join(map(str, r["t"])), r["deg"], r["img"], r["counts"][0]))
verdict("D6 P3: the confound BREAKS (some row separates the three)", bool(sep))
tracks_img = [r for r in good if r["counts"][0] == r["img"]]
tracks_deg = [r for r in good if r["counts"][0] == r["deg"]]
print("D6 phase count = image step at %d of %d rows; = degree at %d"
      % (len(tracks_img), len(good), len(tracks_deg)))
verdict("D6 P4: the count tracks the IMAGE STEP at every stable row",
       len(tracks_img) == len(good))
print("D6 windows where the selector picks nothing: %s"
      % ["".join(map(str, r["t"])) for r in rows if r["sel"] is None])

# ---------------------------------------------------------------- D7
# Added after D0-D6 ran, frozen before it ran. See the design note.
print("")
print("--- D7 the dials the freeze missed, and the stratification D6's "
      "verdict lines did not make ---")

BINARY = [r for r in rows if all(c <= 1 for c in r["t"])]
SELECTING = [(r, r["s_star"]) for r in BINARY if r["sel"]]

print("D7a tail sweep -- the count is capped by the number of samples:")
tail_ok = True
for r, s_star in SELECTING:
    Q = places(r["t"], 6400)
    cs = [len(phases(Q, s_star, deep, span, tail=tl))
          for tl in (12, 30, 60, 120)
          for deep, span in ((80, 250), (120, 300))]
    r["count_true"] = cs[-1]
    print("     %-7s s*=%2d counts by tail 12/30/60/120 x two spans: %s%s"
          % ("".join(map(str, r["t"])), s_star, cs,
             "   <== D5 tail-12 reading was a CEILING"
             if cs[0] != cs[-1] else ""))
    tail_ok = tail_ok and len(set(cs[4:])) == 1
report("D7a every selecting window's count is stable once the tail "
       "exceeds it", tail_ok)

print("D7b selector re-scan to s = 40 where s = 3..20 picked nothing:")
still = []
for r in BINARY:
    if r["sel"]:
        continue
    Q = places(r["t"], 4400)
    found = []
    for s_try in range(3, 41):
        adm, grows = comb_ok(Q, s_try)
        if not (adm and grows):
            continue
        g, teeth = image_gaps(Q, s_try)
        if len(g) == 1 and teeth >= 3:
            found.append(s_try)
    w = "".join(map(str, r["t"]))
    print("     %-7s %s" % (w, found if found else "still NOTHING to s = 40"))
    if not found:
        still.append(w)
print("D7b binary windows where the selector is SILENT to s = 40, %d of "
      "%d: %s" % (len(still), len(BINARY), still))

print("D7c the alphabet split, swept over EVERY t_1 >= 2 word rather "
      "than sampled:")
NONBIN = [r for r in rows if r["t"][0] >= 2]
flat_fail = []
for r in NONBIN:
    Q = places(r["t"], 400)
    K = 3 + 30 * 3
    d = greedy(2 * comb_T(K, Q, 3, 3), Q)
    idx = {k for k, b in enumerate(d) if b}
    if not (idx == set(range(3, K + 1, 3)) and all(d[k] == 2 for k in idx)):
        flat_fail.append("".join(map(str, r["t"])))
print("     2 T_K is the digit 2 on the comb's own positions -- no carry "
      "at all -- at %d of %d words with t_1 >= 2"
      % (len(NONBIN) - len(flat_fail), len(NONBIN)))
print("     the %d where that mechanism does NOT hold, every one of them "
      "beginning 2 0: %s" % (len(flat_fail), flat_fail))
cnt1 = [r for r in NONBIN if r["sel"] and r["counts"][0] == 1]
cntx = [("".join(map(str, r["t"])), r["counts"][0]) for r in NONBIN
        if r["sel"] and r["counts"][0] != 1]
print("     phase count 1 at %d of %d; the exceptions: %s"
      % (len(cnt1), len(NONBIN), cntx))
report("D7c the no-carry mechanism is the MAJORITY story at t_1 >= 2 and "
       "is not universal", bool(flat_fail) and len(flat_fail) < len(NONBIN))

print("D7d the corrected table over the selecting binary windows:")
print("     word    order  s*  image step  count  img/gcd(img,s*)")
law = []
for r, s_star in SELECTING:
    img, c = r["img"], r["count_true"]
    pred = img // gcd(img, s_star)
    law.append(c == pred)
    print("     %-7s %5d %3d %10d %6d %14d%s"
          % ("".join(map(str, r["t"])), r["deg"], s_star, img, c, pred,
             "" if c == pred else "   <== the reading MISSES"))
print("D7d the visiting order, so the PERIOD is MEASURED and never "
      "inferred from count x step:")
for r, s_star in SELECTING:
    Q = places(r["t"], 6400)
    seen, seq = {}, []
    for K in range(s_star + 200 * s_star,
                   s_star + 200 * s_star + 120 * s_star, s_star):
        x = greedy(2 * comb_T(K, Q, s_star, s_star), Q)[:120]
        seq.append(seen.setdefault(x, len(seen)))
    per = next((pp for pp in range(1, 61)
                if all(seq[i] == seq[i + pp] for i in range(len(seq) - pp))),
               None)
    r["period"] = None if per is None else per * s_star
    r["visits"] = None if per is None else per // len(seen)
    print("     %-7s %d phases, order %s..., least period %s in K, each "
          "phase visited %s per turn"
          % ("".join(map(str, r["t"])), len(seen), seq[:8],
             r["period"], r["visits"]))
report("D7d every selecting window has a measurable period",
       all(r.get("period") for r, _ in SELECTING))
verdict("D7d the phases form ONE orbit (period = count x step) at every "
        "selecting window",
        all(r.get("visits") == 1 for r, _ in SELECTING))

sepr = [r for r, _ in SELECTING
        if len({r["deg"], r["img"], r["count_true"]}) > 1]
print("D7d selecting binary windows separating all three numbers: %s"
      % ["".join(map(str, r["t"])) for r in sepr])
verdict("D7d THE CONFOUND BREAKS on a witness that measures something "
       "(count >= 2)",
       any(r["count_true"] >= 2 for r in sepr))
verdict("D7d the arithmetic reading count = img/gcd(img, s*) holds at "
       "every selecting window", all(law))


print("\nwall-clock %.1f s" % (time.time() - t0))
print("ALL: %s" % ok_all)
