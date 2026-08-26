"""What should a growth rule read, when its verdict moves with the range
set it was read at? The run-length rule, and the map re-read under it.

THE QUESTION
------------
The verdict classifier this cascade of rigs shares gates a cell when the
excess-lookahead witness A_top at the FIRST range read sits below A_top
at the LAST. Two defects follow, both established
(explore_cascade_second.py H1 and H4) and neither re-measured here.
What the rule reads is the range SPAN rather than the range DEPTH, and
in the floor direction that is one-way BY CONSTRUCTION -- so a whole
row's gated run at B = 12 exists only because 30000 is in the range set
and vanishes without it. And A_top is A[tmax] with tmax = min(10,
K(N) - 1) moving with the range, so at (A, B) = (24, 12) the printed
growth 5/8/8 compares A[7], A[9] and A[10]: three different quantities,
the index change read as a deepening witness.

So the rule has no fixed point. Adding a shallower range to the set can
change a cell's verdict with no new information about the cell at all,
and the verdict a cell "has" is a fact about the sweep that read it.
This rig asks what to read instead, and re-reads under the answer the
two surfaces that stand on the old rule: this family's r = 2 map, and
the r = 3 value law that ships publicly.

THE HAND-ATTACK (pre-engine, on paper)
--------------------------------------
Write A_N(t) for the witness row at range N read to table depth cap T:
the largest agreement depth p over consecutive sorted pairs whose
images, truncated at T, first differ below t. The excess column is
c(t) = max(0, A(t) - t + 1) -- the lookahead beyond t that determining
the image to depth t costs.

D1  THE CAP IS NOT A PARAMETER OF THE COLUMN, IT IS A TRUNCATION OF IT.
    A pair contributes to A(t) only for t above the position dpos where
    its truncated images first differ, and a pair with dpos at or above
    the cap does not qualify at all. So raising the cap from T to T'
    leaves A(t) UNCHANGED at every t <= T and appends values above it.
    At fixed N the column is one object and the cap decides how much of
    it is on the page. This is what makes the two readings below
    derivable from ONE table, and it is checked and not assumed (Q7).
D2  THE INSTRUMENT WAS CAPPED BELOW ITS DATA. T_MAX = 10 is the shared
    cap. Usable depth K(N) - 1 over the r = 2 map's grid runs 9 to 15 at
    N = 100000 and 10 to 16 at N = 300000, so up to six depths of
    readable column were being discarded -- and the whole
    cross-range apparatus exists because one table could not decide,
    which is the shape of a workaround standing where a root cause was.
    Reading to the data's own depth costs 3.02 s -> 3.10 s per cell,
    measured before this slate was written.
D3  WHAT A SINGLE TABLE CAN AND CANNOT SAY, and this is where a first
    candidate died. A run of nonzeros served by ONE witness pair
    agreeing to depth p, whose images differ at position d, contributes
    c(t) = p - t + 1 for every t in (d, p]: a run of length p - d
    declining by exactly 1 per depth. So a column still nonzero at the
    table's edge says only that the witness sits at or beyond the edge.
    THE FIRST CANDIDATE FROZEN HERE -- the CLOSING RULE, reading whether
    the column returns to zero inside the table, with the trailing zeros
    as a margin -- was killed by C1 at 7 of its 9 windows, and the two
    reasons are why the rule below is a different observable rather than
    a repair of that one. It is PHASE-DEPENDENT: at the graded window
    the column is periodic, so whether it happens to close depends on
    where the cap falls against the bump, which is the old rule's
    disease in a new coat. And it is FALSIFIED OUTRIGHT at the designed
    family, where the gated stride r = 6 of P = 5, A = 3 prints
    0 0 0 0 0 0 8 7 6 5 4 3 2 1 0 0 0 0 -- a column that closes with
    four depths to spare and is gated by the family's own law.
D4  THE DISCRIMINATOR IS THE RUN LENGTH AGAINST THE PERIOD, and it is
    derived rather than fitted. At a window of period P the digit
    structure repeats every P positions, so a LOCAL obstruction sitting
    at one phase recurs at that phase in every period, and its run
    cannot reach length P -- at length P consecutive copies would touch
    and the feature would not be local at all. A SINGLE DEEP WITNESS has
    run length p - d with p unbounded in the data. So:
        run length >= P   is not a local obstruction      -> GATED
        runs shorter than P, recurring at the period      -> bounded
    Note what the argument does and does not give. It does NOT show a
    long run IS one deep witness -- a periodic feature whose own run
    reached P would have its copies touch and merge into one long run
    too. What it shows is that such a feature is not LOCAL at this
    period, which is the same conclusion for the verdict and a weaker
    one for the mechanism. The rule reads locality, and the deep witness
    is the shape that explains the cases, not a thing the rule detects.
    One table, no range set, no phase, no two-point comparison on a
    quantity whose index moves. This is the shape observable named as
    the thing to try before adding ranges, made precise: the
    decline of exactly 1 per depth is not by itself the tell, since a
    periodic bump declines by 1 too -- what separates them is whether
    the decline OUTLASTS the period.
D5  WHAT THE RULE INHERITS UNCHANGED, and one clause of it is why the
    first candidate went red at two further windows. Saturation is a
    verdict of its own and its threshold is >= C_MAX, NOT > C_MAX: the
    parent rig recorded that a column sitting exactly at C_MAX looks
    like an ordinary number while being a delay the lookahead cannot
    measure (explore_cascade_span.py saturates). The first candidate
    used the strict form and misread P = 3, A = 3 at r = 4, whose peak
    is exactly 10. And repairs = 0 stays delay-0.
D6  THE TWO AXES AND THEIR SIGNS. At fixed N, raising the cap only
    reveals more column (D1), so the deepest available table is the
    reading and a deeper read strictly dominates. At fixed cap, raising
    N can only RAISE A(t): A(t) is a max over consecutive sorted pairs,
    and inserting a string between a qualifying pair leaves at least one
    sub-pair qualifying at an agreement no smaller (H1's argument). So
    at a FIXED cap every c(t) is monotone in N, so the nonzero SET only
    grows, so runs only extend or merge and BOTH the longest run and the
    peak are monotone -- which is what carries the verdict, gating being
    a condition on the run and saturation on the peak. A cell gated at N
    is therefore gated at every larger N. Q3 makes every cell a chance to
    refute it.
D7  THE DEPTH THE RULE OWES, and it is the honest form of a minimum
    common-depth check. The signature is a run of length >= P, so a
    table of depth below P + 1 cannot carry one and every cell would
    read bounded for want of room. Such a cell is REFUSED and reported
    as refused. The graded family has P = 6, so depth 7 -- what
    N = 10000 leaves at most of this grid -- is the exact edge, and the
    refusal is what keeps a shallow floor from buying a green.
D8  WHAT THIS PREDICTS ABOUT THE MAP. Two graded cells the parent rig
    separates -- (13, 4) bounded and (8, 5) gated -- print the IDENTICAL
    r = 2 column at N = 300000, 0 0 3 2 1 0 0 0 3 2 1 0 0: two runs of
    length 3 recurring at the period 6. Under a one-table rule they
    cannot be separated, so either they agree or the information that
    separated them was never in the cell. H1 already showed this row's
    verdicts move with the range floor, so the predicted direction is
    that the gated readings at (14, 4), (8, 5), (9, 5), (11, 5), (8, 6)
    do not survive -- not because a measurement overturned them but
    because they were never facts about the cell.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS,
never what it would mean)
  C1 (the positive control, run FIRST; nothing below is read if it is
      red) at the designed family [1^(P-1), A]^inf, P = 3, 4, 5 and
      A = 2, 3, 5, the run-length rule prints F4's law at all nine
      windows and all 54 strides: delay-0 at r = 0 mod P, bounded at
      even residues, gated at odd residues. KILL: any miss.
  C2 (the diagonal control) the graded window's A = B cell at r = 2
      reads bounded at every B read. KILL: a diagonal cell gated.
  C3 (the two irrationals) cbrt(2) - 1 is gated at r = 1, 3, 5 and
      e - 2 at r = 1, 4, 7, bounded elsewhere -- the parent rig's
      verdict. These two are NOT periodic windows, so the run-length
      rule is applied with the period the rule needs absent: they are
      read with P taken as the table depth, which makes every finite run
      bounded and can only be red. What they test is therefore the
      SATURATION clause alone, and that is stated here so a green is not
      read as more than it is.
  C4 (attribution) every cell prints its reading at the OLD cap 10 and
      at the data's own depth, from one table by D1, so a verdict that
      moves is attributed to the depth recovered and not to the rule.
  Q1 (the calibration cells) the eleven cells H4 fixed, re-read.
      Observable: which move, and the column each moves on. D8 predicts
      five move to bounded.
  Q2 (the row the floor invented) row B = 12, A = 16..24 -- gated at
      three ranges, bounded at the two deeper ones. Observable: the
      verdict and the run length at N = 300000. Predicted bounded.
  Q3 (the one-way law, derived -- D6) at the FIXED cap 10, no cell
      reads bounded at a larger N after reading gated at a smaller one,
      over every cell at every stride. KILL: one such cell refutes the
      insertion argument H1 rests on, and four surfaces rest on H1.
  Q4 (the public claim) at r = 3, N = 300000, data depth, the bounded
      cells are exactly B < A <= 2B + 1 with A * B >= 30
      (explore_cascade_values.py H2). Observable: the miss count and
      every missed cell named. A miss that eats a CLAUSE -- the roof at
      2B + 1 or the product at 30 -- is a different outcome from a miss
      that trims an edge, and the two are separated in the print.
  Q5 (the r = 2 thresholds) the per-row smallest gated A at r = 2,
      against H2's row
          B      3    4   5   6    7   8   9   10  11  12
          T(B)  18   14   8   8   10  10  12   18  17  16
      Observable: the column, and which rows move.
  Q6 (the up-set) whether the gated cells of each row form an up-set in
      A, and whether H2's single interruption at (10, 5) survives.
  Q8 (refusals) every cell whose data depth is below P + 1 is refused
      and named (D7). Observable: the refused set per range.

FINDINGS (each at its own tier)
-------------------------------
H1  THE r = 2 SECOND SURFACE DOES NOT EXIST (rule at scanned scope, 210
    cells at four ranges, zero refusals; F3). Under the run-length rule
    every cell of the map -- B = 3..12 over A = 4..24 -- reads BOUNDED,
    at N = 10000, 30000, 100000 and 300000 alike. Not one cell gates at
    r = 2 anywhere. So the whole second surface goes: the thresholds
    18, 14, 8, 8, 10, 10, 12, 18, 17, 16, the up-sets in A, the single
    interruption at (10, 5), the region's shape, its boundary, and the
    claim that the parity law breaks at a SECOND cell. What breaks the
    parity law at this family is the half-period stride r = 3 and
    nothing else. The parity law's own gated stride survives untouched:
    r = 1 is SATURATED at every one of the 210 cells, which is the
    reading the law predicts and is not something the new rule could
    have manufactured -- counted at all 210 by F6, since F3 prints a
    cell's own line only where something moves and its r = 1 column sat
    in the tables unread.
H2  THE r = 3 VALUE LAW IS INSTRUMENT-INDEPENDENT (rule at scanned
    scope reproduced at zero misses over 92 cells and zero refusals;
    F4). Bounded exactly on B < A <= 2B + 1 with A * B >= 30, A = B
    delay-0, at N = 300000 read to the data's own depth. Both sharp
    clauses reproduce cell for cell: the roof turns the row gated at
    exactly A = 2B + 2 at B = 4, 5, 6, and the product threshold still
    sits between (7, 4) at 28 and (6, 5) at 30. This is the outcome the
    probe was aimed at, and it lands stronger than the kill asked
    for. The law was established under a classifier whose verdict is a
    two-point comparison across a range SET, at an instrument cap of
    10; it survives a classifier that reads ONE table, has no range set
    in it at all, and reads those 92 cells at depths running 12 to 20,
    52 of them at 13. The deep cap of 20 BINDS at exactly one cell,
    (2, 2), and that cell is delay-0, so no verdict here rests on a
    table this rig truncated. The public page therefore
    needs no word about its cells -- and its scope line, which said the
    ranges are part of the claim, can be replaced by the stronger fact
    rather than merely softened.
H3  THE RUN-LENGTH RULE, the banked shape observable made precise
    (the rule; C1 green at 9 windows and all 54 strides, C2 green at
    every diagonal read, Q3 green over every cell it tracked). At a
    window of period P, read the excess column c(t) = max(0, A(t) -
    t + 1) at ONE table to the data's own depth and split it into
    maximal nonzero runs. A peak at or above C_MAX is SATURATED
    (2026-08: the ceiling is CALIBRATION rather than a property of the
    column -- the trusted bounded corpus's excess peaks stop at 5, no
    intrinsic replacement exists, and one past that maximum is the
    honest form; explore_saturation_twins.py); a run
    of length >= P cannot be a local feature of the period and GATES;
    runs shorter than P, recurring at the period, are a local
    obstruction and read BOUNDED; a table of depth below P + 1 is
    REFUSED. The discriminator is not
    the decline of exactly 1 per depth -- a periodic bump declines by 1
    too -- but whether the decline OUTLASTS the period. The rule takes
    no range set, so it has the fixed point the old rule lacked:
    adding a range cannot change a verdict already read.
    READ C1's GREEN FOR WHAT IT IS. The run-against-period threshold was
    chosen by reading the c columns OF THOSE NINE WINDOWS after the
    first candidate died on them, so C1 is a consistency check on the
    successor and not an independent control of it -- a control has to
    differ from the treatment in one variable, and here it supplied the
    variable. What is independent is Q4: the r = 3 value law was
    established at another rig, by another classifier, before this rule
    existed, and its 92 cells reproduce at zero misses with no parameter
    of this rule fitted to them. The map's 210 cells are independent in
    the same way and are the reason C2 counts.
H4  THE FIRST CANDIDATE DIED AT ITS OWN POSITIVE CONTROL, and that is
    the run's most transferable fact. The CLOSING RULE -- does the
    column return to zero inside the table, with the trailing zeros as
    a margin -- was frozen, hand-attacked and coded before anything
    ran, and C1 killed it at 7 of 9 windows before a single map cell
    was read. Two distinct causes, and only one was a slip. The slip:
    it took saturation at > C_MAX where the parent rig had documented
    >= C_MAX, and misread P = 3, A = 3 at r = 4 whose peak is exactly
    10 -- a guard added upstream because a control went red without it,
    dropped by a rig that rewrote the verdict instead of importing it.
    The real defect: closure is PHASE-dependent. The graded window's
    column is periodic, so whether it happens to close depends on where
    the cap falls against the bump -- the old rule's disease in a new
    coat -- and at the designed family it is falsified outright, the
    gated stride r = 6 of P = 5, A = 3 printing a column that closes
    with four depths to spare. A rule built to fix a range artifact had
    reproduced it as a phase artifact.
H5  THE DEPTH RECOVERY IS A CALIBRATION FACT AND NOT A MAP FACT, and
    the two halves have to be said together or either one misleads
    (F3, F5). The shared cap T_MAX = 10 was below the data at almost
    every cell: usable depth runs to 13 at N = 100000 and to 16 at
    N = 300000, and one row of the grid discards 72 depths --
    while a deeper table costs 3.02 s against 3.10 s. Yet in the r = 2
    map -- whose depths run 10 to 16 at N = 300000, against the cap of
    10 -- the recovered depth moves NO cell, and that is DERIVED before
    it
    is counted: truncating to the cap can only SHORTEN a run and lower a
    peak (D1), so a cell bounded at the data depth has every run below
    the period at the cap too and is bounded there -- the converse of
    the direction that matters. All 210 are bounded at the data depth,
    so all 210 are bounded at the cap; F6 counts it at 210 of 210. H1 is
    therefore a verdict about the RULE and not about the depth, and
    saying the region died of truncation would be wrong. What the depth buys is
    the calibration itself: C1 scores 0 misses at data depth and 4 at cap 10,
    the designed family's gated strides r = 6 and r = 8 at P = 5 reading
    bounded when their runs are cut short of the period. The old cap could not
    have certified this rule, which is why the rule was not available to be
    written at the old instrument.
H6  WHAT THE RULE IS NOT, said because a green over 302 cells invites
    more than it earned -- and 54 of the strides behind it are the ones
    the threshold was read off (H3), so the independent count is 302
    cells and not 302 plus C1. It is stated for PERIODIC windows and its
    discriminator is a run against that period, so it does not apply
    where no period exists: at cbrt(2) - 1 and e - 2 (C3, read with the
    refusal off so only saturation can fire) it catches what saturates
    -- r = 1 at both windows and e - 2's r = 4 -- and misses three
    gated strides outright: the cubic's r = 3 and r = 5, whose runs are
    9 and 5, and e - 2's r = 7, whose run is 6. There is no period to
    measure any of them against. That is a scope limit and not a red control --
    C3's own text fixed it before the run -- but it is the open end: what plays
    the period's role at an aperiodic window is not answered here.
    ** IT IS ANSWERED NOW, IN THE NEGATIVE (explore_cascade_scale.py H4, H6).
    Two recurrence lengths are fixed by a window's own data with no further
    choice -- the quotient SEQUENCE's and its LARGENESS pattern's -- and a
    rule that picked any other would be reading a parameter rather than the
    window. They part at every graded window, 3
    against 6, moving 175 of F3's 210 cells. The sequence period is the
    entitled one, and what settles that is not the derivation but the value
    law: the largeness scale misses it at every bounded cell among the 25
    pairs swept, each carrying a run of 5, between the two scales. An
    aperiodic window has
    neither length, so the rule is family-specific to periodic quotient
    sequences BY DERIVATION and the refusal is not a gap to be closed. **
    Two further
    limits. Q3's one-way law held at every cell it was tracked at -- strides 1
    and 2 over F3's 210, stride 3 over F4's 92, 0 violations -- which supports
    H1's insertion argument but does not prove it, and says nothing about the
    strides it did not track. And the rule inherits the parent digit path and
    c_min row unchanged, so anything wrong there is wrong here identically.

THE DESIGN
----------
The window builder, the digit path and the c_min row are imported from
explore_cascade_span.py and explore_shift_repair.py -- not
reimplemented, since a fresh loop over the same windows would not be
comparable to the cells the parent rigs printed. What is NOT imported is
the verdict: range_verdict and measured_verdict are the subject here,
and the run-length rule is written below against the same rows they read.
Every window carries its PERIOD as a parameter of the reading, since D4
is a statement about the run against that period and a rule that guessed
the period would be reading its own guess.

Each cell is read ONCE per range, at the deep cap, and both the
data-depth reading and the old cap-10 reading are derived from that one
table by D1 -- which is why Q7 checks D1 against a second read rather
than trusting it: at the calibration cells the rig recomputes the table
at cap 10 and compares A[t] for t <= 10 entry by entry. If Q7 is red,
every derived cap-10 column in this file is void and C4 with it.

Ranges (10000, 30000, 100000, 300000). The two shallow ones cost about
a third of a second per cell together and carry Q3's shallow end and
the depth-bias demonstration; the cost is the two deep ones.

RUN RECORD (the estimate first, then what it cost)
Per cell at four ranges: 0.08 + 0.25 + 0.92 + 3.04 = 4.3 s at two
strides, measured. Estimated F1 ~5 s, F2 ~3 min, F3 210 cells ~15 min,
F4 92 cells at three strides ~7 min: ABOUT 25 MINUTES TOTAL, stop at 50. Ran:
F1 0.3 s, F2 159 s, F3 938 s, F4 561 s, F5 29 s, F6 667 s -- 40 minutes over
six stages, inside the stop. F5 and F6 were not in the estimate: F5 prices the
cap against the calibration (H5), and F6 counts two columns F3 held in its
tables and printed only where a cell moved -- the r = 1 stride and the cap-10
comparison, both of which H1 and H5 had claimed over all 210 before anything
printed them. Peak commit 298 MB at F4, under memwatch at 512 throughout; the
~310 MB estimate was close. F2 was run twice more: once on the candidate H4
buries, and once after C3's refusal switch was corrected to match its own
frozen text. That is over the ten-minute line and the necessity is the claim's
own shape: Q4 reproduces a law stated over a grid, cell for cell, and a sample
of the grid reproduces nothing. Stages run one at a time (argv) so no single
call is open-ended. Peak memory ~310 MB at N = 300000 with the deeper strings,
under memwatch at 512.

SETTLED LATER (explore_limit_column.py): the rule's gated verdicts are
final (the column is monotone in N) and its bounded verdicts are lower
readings -- H2's 92-cell reproduction reproduced a finite-range reading,
every cell with A != B at r = 3 having an infinite limit column, while
H1's 210 bounded cells are bounded in the limit with the histogram the
deepest range printed. At a periodic window the limit column is decided
exactly by a finite carry automaton; the rule keeps its home where there
is no period. """

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_shift_repair import (          # noqa: E402
    C_MAX,
    build_q,
    designed,
    quotients_cbrt2_minus_1,
    quotients_e_minus_2,
    usable_depth,
)
from explore_cascade_span import (          # noqa: E402
    WANT,
    cell_rows,
    graded,
)

RANGES = (10_000, 30_000, 100_000, 300_000)
DEEP = 20            # above every K(N)-1 in this grid; a truncation shows
OLD_CAP = 10         # the shared instrument cap the parent rigs read at
A_CAP = 24
CUBIC = quotients_cbrt2_minus_1(WANT)
E2MINUS = quotients_e_minus_2(WANT)


# --------------------------------------------------- THE RUN-LENGTH RULE

def runs_of(c):
    """Maximal nonzero runs of the excess column as (start, length, peak)."""
    out, i, n = [], 0, len(c)
    while i < n:
        if c[i] == 0:
            i += 1
            continue
        j = i
        while j < n and c[j] > 0:
            j += 1
        out.append((i + 1, j - i, max(c[i:j])))
        i = j
    return out


def verdict(A, tmax, repairs, period, refuse=True):
    """The run-length rule at ONE table (D4, D5, D7).

    Returns (code, longest run length, peak, run count). The period is
    the window's, passed in: D4 compares the run against it.
    """
    if repairs == 0:
        return "delay0", 0, 0, 0
    c = [max(0, A[t] - t + 1) for t in range(1, tmax + 1)]
    rs = runs_of(c)
    peak = max([r[2] for r in rs], default=0)
    longest = max([r[1] for r in rs], default=0)
    if peak >= C_MAX:                      # D5: inclusive, not strict
        return "satur", longest, peak, len(rs)
    if refuse and tmax < period + 1:       # D7: no room for the signature
        return "refuse", longest, peak, len(rs)
    if longest >= period:                  # D4: outlasts the period
        return "gated", longest, peak, len(rs)
    return "bnd", longest, peak, len(rs)


CODE = {"bnd": "b", "gated": "G", "satur": "S", "delay0": ".",
        "refuse": "?"}
GATEDISH = ("gated", "satur")


def col(v):
    """A reading as one printable field: code, longest run, peak."""
    code, longest, peak, nruns = v
    return f"{CODE[code]}L{longest:2d}/p{peak:2d}/n{nruns}"


def cell(a, n, rmax, period, refuse=True):
    """One cell at one range, read at the DEEP cap.

    Both readings come from that one table by D1: the data's own depth,
    and the old cap 10.
    """
    rows = cell_rows("", a, n, rmax=rmax, tmax_cap=DEEP, show=False)
    out = {}
    for r, row in rows.items():
        A, tmax, rep = row["A"], row["tmax"], row["repairs"]
        out[r] = {
            "tmax": tmax,
            "deep": verdict(A, tmax, rep, period, refuse),
            "old": verdict(A, min(OLD_CAP, tmax), rep, period, refuse),
            "A": A,
            "repairs": rep,
        }
    return out


PERIOD = 6           # the graded window [1,1,A,1,1,B]^inf


def window(A, B):
    return graded(PERIOD, {2: A, 5: B})


def cmin(row):
    return " ".join(f"{max(0, row['A'][t] - t + 1):2d}"
                    for t in range(1, row["tmax"] + 1))


# --------------------------------------------------------------- F1

def f1_depth_recovered():
    print("=" * 78)
    print("F1 THE DEPTH THE CAP WAS DISCARDING (weights only, no digits)")
    print(f"   K(N) - 1 against the shared instrument cap T_MAX = {OLD_CAP};"
          f" D7 refuses depth < {PERIOD + 1}")
    for n in RANGES:
        lost = ref = 0
        rows = []
        for B in range(3, 13):
            raw = [usable_depth(build_q(window(A, B), n), n) - 1
                   for A in range(4, A_CAP + 1)]
            lost += sum(max(0, t - OLD_CAP) for t in raw)
            ref += sum(1 for t in raw if t < PERIOD + 1)
            rows.append((B, raw))
        print(f"  N = {n}: depths discarded by the old cap {lost}, "
              f"cells refused by D7 {ref} of 210")
        for B, raw in rows:
            print(f"    B={B:2d} A=4..24: {' '.join(f'{t:2d}' for t in raw)}")


# --------------------------------------------------------------- F2

CALIBRATION = ((13, 4, "b"), (14, 4, "G"),
               (7, 5, "b"), (8, 5, "G"), (9, 5, "G"),
               (10, 5, "b"), (11, 5, "G"),
               (7, 6, "b"), (8, 6, "G"),
               (16, 3, "b"), (9, 9, "b"))


def f2_controls():
    print("=" * 78)
    print("F2 THE CONTROLS")
    print()
    print("-- C1 the designed family: F4's parity of r mod P, N=100000 --")
    miss = 0
    for P in (3, 4, 5):
        for A in (2, 3, 5):
            c = cell(designed(P, A, WANT), 100_000, 2 * P, P)
            line, bad = [], []
            for r in sorted(c):
                v = c[r]["deep"]
                res = r % P
                want = ("delay0" if res == 0
                        else "bnd" if res % 2 == 0 else "gated")
                got = v[0]
                if not (got == want or (want == "gated" and got in GATEDISH)):
                    bad.append((r, want, got))
                line.append(f"r{r}:{col(v)}")
            miss += len(bad)
            print(f"  D P={P} A={A} t<={c[1]['tmax']:2d} " + " ".join(line))
            if bad:
                print(f"      C1 MISS {bad}")
    print(f"  C1: {miss} stride misses over 9 windows -- "
          + ("GREEN" if not miss else "RED, nothing below is read"))
    print()
    print("-- C3 the two irrationals, N=100000, period taken as the table")
    print("   depth so ONLY the saturation clause can fire (C3's own words) --")
    for name, a, want in (("cbrt(2)-1", CUBIC, {1, 3, 5}),
                          ("e-2", E2MINUS, {1, 4, 7})):
        c = cell(a, 100_000, 8, DEEP, refuse=False)
        bad, line = [], []
        for r in sorted(c):
            v = c[r]["deep"]
            if (v[0] in GATEDISH) != (r in want):
                bad.append((r, v[0]))
            line.append(f"r{r}:{col(v)}")
        print(f"  {name:10s} t<={c[1]['tmax']:2d} " + " ".join(line))
        print("      C3 " + ("GREEN" if not bad else f"MISS {bad}"))
    print()
    print("-- Q7 D1's truncation, checked against a second read at cap 10 --")
    bad = 0
    for A, B, _ in CALIBRATION:
        deep = cell_rows("", window(A, B), 300_000, rmax=2, tmax_cap=DEEP,
                         show=False)
        shal = cell_rows("", window(A, B), 300_000, rmax=2,
                         tmax_cap=OLD_CAP, show=False)
        for r in (1, 2):
            t = shal[r]["tmax"]
            if deep[r]["A"][1:t + 1] != shal[r]["A"][1:t + 1]:
                bad += 1
                print(f"      Q7 MISS at A={A} B={B} r={r}")
    print(f"  Q7: {bad} disagreements -- "
          + ("GREEN, D1 holds" if not bad else "RED, C4 is void"))
    print()
    print("-- Q1 the eleven calibration cells at r = 2, all four ranges --")
    moved = 0
    for A, B, want in CALIBRATION:
        cs = [cell(window(A, B), n, 2, PERIOD) for n in RANGES]
        per = "  ".join(f"{n // 1000:3d}k:{CODE[c[2]['deep'][0]]}"
                        f"{c[2]['tmax']:2d}" for n, c in zip(RANGES, cs))
        d = cs[-1][2]
        got = CODE[d["deep"][0]]
        if got != want:
            moved += 1
        print(f"  A={A:2d} B={B:2d}  {per}   deep {col(d['deep'])}"
              f"   old10 {col(d['old'])}   H4 {want}"
              + ("" if got == want else "   <<< MOVED"))
        print(f"           c_min {cmin(d)}")
    print(f"  Q1: {moved} of 11 cells moved off H4 (D8 predicts 5)")
    return miss == 0


# ------------------------------------------------------------- Q3

def q3_check(seen, label, track):
    """D6's one-way law at the FIXED cap 10, over the ranges in order."""
    bad = []
    for key, per_range in track.items():
        gated = False
        for n, v in zip(RANGES, per_range):
            if v[0] in GATEDISH:
                gated = True
            elif gated and v[0] == "bnd":
                bad.append((key, n))
    seen.extend(bad)
    print(f"  Q3 {label}: {len(bad)} cells bounded after gating"
          + ("" if not bad else f" -- KILL {bad}"))


# --------------------------------------------------------------- F3

def f3_map():
    print("=" * 78)
    print(f"F3 THE r = 2 MAP UNDER THE RUN-LENGTH RULE, {RANGES}")
    print("   b = bounded, G = gated, S = saturated, . = delay-0, "
          "? = refused for depth (D7).")
    print("   Per row: the verdict string over A = 4..24 at each range, "
          "then every cell's deep reading.")
    q3bad, T = [], {}
    for B in range(3, 13):
        track, deep_rows, by_range = {}, {}, {n: [] for n in RANGES}
        for A in range(4, A_CAP + 1):
            cs = [cell(window(A, B), n, 2, PERIOD) for n in RANGES]
            track[(A, 2)] = [c[2]["old"] for c in cs]
            track[(A, 1)] = [c[1]["old"] for c in cs]
            deep_rows[A] = cs[-1]
            for n, c in zip(RANGES, cs):
                by_range[n].append(CODE[c[2]["deep"][0]])
        print()
        print(f"-- row B = {B}   (A = 4..24, verdicts at the DATA depth) --")
        for n in RANGES:
            print(f"      N={n:6d}: {''.join(by_range[n])}")
        deep = by_range[RANGES[-1]]
        As = list(range(4, A_CAP + 1))
        gated = [A for A, ch in zip(As, deep) if ch in ("G", "S")]
        refused = [A for A, ch in zip(As, deep) if ch == "?"]
        dch = deep[B - 4] if 4 <= B <= A_CAP else "n/a"
        print(f"      C2 diagonal A = B = {B}: {dch}"
              + ("   <<< KILL" if dch in ("G", "S") else ""))
        print(f"      gated at r = 2: {gated if gated else 'none'}"
              f"   refused: {refused if refused else 'none'}")
        off = [A for A in gated if A != B]
        if off:
            lo = min(off)
            holes = [A for A in range(lo + 1, A_CAP + 1)
                     if A != B and A not in gated and A not in refused]
            T[B] = lo
            print(f"      T({B}) = {lo}   up-set: {not holes}"
                  f"   interruptions: {holes if holes else 'none'}")
        else:
            T[B] = 0
            print(f"      T({B}) = none to A = {A_CAP}")
        show = sorted((set(gated) | set(refused) | {B}
                       | {A for A, ch in zip(As, deep)
                         if ch != by_range[RANGES[0]][A - 4]}) & set(As))
        for A in show:
            d = deep_rows[A][2]
            print(f"        A={A:2d} t<={d['tmax']:2d} {col(d['deep'])}"
                  f"  old10 {col(d['old'])}"
                  f"  r1 {col(deep_rows[A][1]['deep'])}  c {cmin(d)}")
        q3_check(q3bad, f"row B={B}", track)
    print()
    print("-- Q5 the threshold column under the run-length rule --")
    print("   B      " + " ".join(f"{B:4d}" for B in range(3, 13)))
    print("   T(B)   " + " ".join(f"{T[B]:4d}" for B in range(3, 13)))
    print("   H2     " + " ".join(f"{x:4d}" for x in
                                  (18, 14, 8, 8, 10, 10, 12, 18, 17, 16)))
    print(f"  Q3 over F3: {len(q3bad)} violations of D6's one-way law")


# --------------------------------------------------------------- F4

def law_says(A, B):
    """explore_cascade_values.py H2: bounded iff B < A <= 2B+1, A*B >= 30."""
    if A == B:
        return "delay0"
    return "bnd" if (B < A <= 2 * B + 1 and A * B >= 30) else "gated"


def f4_value_law():
    print("=" * 78)
    print(f"F4 THE r = 3 VALUE LAW RE-READ, {RANGES}")
    print("   H2: bounded iff B < A <= 2B + 1 and A*B >= 30; A = B delay-0.")
    q3bad, misses, refused, track, grid = [], [], [], {}, {}
    cells = [(A, B) for B in range(2, 10) for A in range(2, 10)]
    cells += [(A, B) for B in range(3, 7) for A in range(10, 17)]
    for A, B in cells:
        cs = [cell(window(A, B), n, 3, PERIOD) for n in RANGES]
        track[(A, B)] = [c[3]["old"] for c in cs]
        d = cs[-1][3]
        got, want = d["deep"][0], law_says(A, B)
        if got == "refuse":
            refused.append((A, B))
            mark = "  <<< REFUSED"
        elif got == want or (want == "gated" and got in GATEDISH):
            mark = ""
        else:
            misses.append((A, B, want, got))
            mark = "  <<< MISS"
        per = " ".join(f"{n // 1000}k:{CODE[c[3]['deep'][0]]}"
                       for n, c in zip(RANGES, cs))
        moved = CODE[d["deep"][0]] != CODE[d["old"][0]]
        if mark or moved:
            print(f"  A={A:2d} B={B:2d} t<={d['tmax']:2d} {per}"
                  f"  deep {col(d['deep'])}  old10 {col(d['old'])}"
                  f"  H2 {want:6s}{mark}"
                  f"{'  <<< MOVED off cap 10' if moved and not mark else ''}"
                  f"  c {cmin(d)}")
        grid.setdefault(B, {})[A] = CODE[d["deep"][0]]
    q3_check(q3bad, "F4", track)
    print()
    print()
    print("  the grid as measured (rows B, columns A ascending):")
    for B in sorted(grid):
        As = sorted(grid[B])
        print(f"    B={B:2d} A={As[0]}..{As[-1]}: "
              + "".join(grid[B][A] for A in As))
    print(f"  Q4: {len(misses)} misses and {len(refused)} refusals "
          f"of {len(cells)} cells")
    print(f"      refused: {refused if refused else 'none'}")
    for A, B, want, got in misses:
        fails = []
        if not B < A:
            fails.append("floor A>B")
        if not A <= 2 * B + 1:
            fails.append("roof 2B+1")
        if not A * B >= 30:
            fails.append("product 30")
        print(f"      MISS A={A} B={B}: H2 {want}, measured {got}"
              f"   clauses this cell fails: {fails if fails else 'none'}")


STAGES = {"f1": f1_depth_recovered, "f2": f2_controls,
          "f3": f3_map, "f4": f4_value_law}


# --------------------------------------------------------------- F5

def f5_cap_attribution():
    """C4's other half: what the run-length rule does at the OLD cap.

    F3 finds the r = 2 map reads the same at cap 10 and at data depth,
    so the depth recovered moved no cell there. That could be read as
    the depth recovery having been unnecessary, and this stage is what
    refuses that reading: the rule is CALIBRATED at the designed family,
    and the calibration is what the cap was destroying.
    """
    print("=" * 78)
    print("F5 THE RULE AT THE OLD CAP -- C1 re-scored on the cap-10 column")
    miss_deep = miss_old = 0
    for P in (3, 4, 5):
        for A in (2, 3, 5):
            c = cell(designed(P, A, WANT), 100_000, 2 * P, P)
            bad_d, bad_o = [], []
            for r in sorted(c):
                res = r % P
                want = ("delay0" if res == 0
                        else "bnd" if res % 2 == 0 else "gated")
                for key, bad in (("deep", bad_d), ("old", bad_o)):
                    got = c[r][key][0]
                    if not (got == want or (want == "gated"
                                            and got in GATEDISH)):
                        bad.append((r, want, got))
            miss_deep += len(bad_d)
            miss_old += len(bad_o)
            print(f"  D P={P} A={A} t<={c[1]['tmax']:2d}"
                  f"  deep misses {len(bad_d)}  cap-10 misses {len(bad_o)}"
                  f"{'  ' + str(bad_o) if bad_o else ''}")
    print(f"  C1 at the data depth: {miss_deep} misses")
    print(f"  C1 at the old cap 10: {miss_old} misses")


STAGES["f5"] = f5_cap_attribution


# --------------------------------------------------------------- F6

def f6_parity_stride():
    """The r = 1 column over the WHOLE map, and cap 10 against data depth.

    F3 prints the r = 2 map entire but shows a cell's own line only where
    something moves, so its r = 1 readings and its cap-10 comparison sat
    in the tables unprinted. Both are load-bearing -- r = 1 gated
    everywhere is what says the rule is not simply calling this family
    bounded -- so they are counted here at the deepest range.
    """
    print("=" * 78)
    print(f"F6 r = 1 OVER THE WHOLE MAP at N = {RANGES[-1]}, and cap 10")
    tally, same, cells = {}, 0, 0
    for B in range(3, 13):
        row = []
        for A in range(4, A_CAP + 1):
            c = cell(window(A, B), RANGES[-1], 2, PERIOD)
            v1, d2, o2 = c[1]["deep"], c[2]["deep"], c[2]["old"]
            tally[v1[0]] = tally.get(v1[0], 0) + 1
            same += d2[0] == o2[0]
            cells += 1
            row.append(CODE[v1[0]])
        print(f"  B={B:2d} r=1 over A=4..24: {''.join(row)}")
    print(f"  r = 1 verdict tally over {cells} cells: {tally}")
    print(f"  r = 2 cap-10 agrees with data depth at {same} of {cells}")


STAGES["f6"] = f6_parity_stride



if __name__ == "__main__":
    for name in (sys.argv[1:] or ["f1", "f2", "f3", "f4"]):
        STAGES[name]()
