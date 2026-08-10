"""What SCALE does a run get measured against, and what is left of the
cascade once the two-point classifier is gone from all of it.

THE QUESTION
------------
The run-length rule (explore_cascade_rule.py H3) reads ONE table: split
the excess column c(t) = max(0, A(t) - t + 1) into maximal nonzero runs,
and a run reaching the window's PERIOD cannot be a local feature of that
period and gates. It retired a classifier that compared the excess
witness at the first range read against the last -- the range SPAN, a
rule with no fixed point -- and two surfaces read under that classifier
have been re-read: the r = 2 second surface died entirely, the r = 3
value law survived at zero misses.

The rest of the cascade still stands on the retired classifier, and the
scope is named by the IMPORT rather than by a grep. Three rigs import
range_verdict / verdict_vector / ranged from explore_cascade_span.py:
roof, second, values. Second and values are re-read. What is left is
explore_cascade_roof.py, and explore_cascade_span.py's own F4 and F5 --
the definer being also a user, which is the last place anyone looks.

And the rule has an open end of its own. Its discriminator is a run
against a PERIOD, so at a window with none it reaches only what
saturates (H6). What plays the period's role there is the thread's
founding question in the rule's own vocabulary, and this rig answers it
by deriving which SCALE the rule is entitled to -- a question that turns
out to have an answer already in the corpus, and to bear on the periodic
windows too, since the rule has been fed a NOMINAL period rather than a
measured one everywhere it has run.

THE HAND-ATTACK (pre-engine, on paper)
--------------------------------------
D1  WHAT THE RULE CAN AND CANNOT REACH, counted before it is run.
    roof H1 (the cubic and e - 2 at three ranges) is two APERIODIC
    windows: no period, so the rule refuses and the split cannot be
    re-read. roof H2's identical-multiset witness is read OFF that
    split, and roof H3's cubic scoring likewise -- both inherit the
    refusal. roof H4 is the flip signature, whose subject is which
    cells MOVED under a third range: the rule takes no range set, so
    there are no movers and the finding DISSOLVES rather than being
    re-read -- and the sweep it argued for costs nothing under a rule
    with one range in it. roof H5 (the two-class family, 84 cells at
    P = 4..7) is periodic and re-readable, as are span F4 (the graded
    control, 30 cells, and the swapped-pair witness) and span F5 (the
    value cell). So ONE of roof's five findings is in reach and four
    are not, and that count is a report about the rule's scope rather
    than about the cascade.
D2  A CONTRADICTION ALREADY ON THE RECORD, and no engine is owed for
    it. explore_cascade_values.py H4 states that six of the 64 grid
    pairs move a stride other than r = P, two of them at min >= 6, and
    explore_cascade_span.py F5 names (8, 5) as the pair moving r = 2.
    rule H1's map is B = 3..12 over A = 4..24 read
    at r = 2, and it reads every one of its 210 cells BOUNDED --
    (A, B) = (8, 5) among them. So H1 already refutes the r = 2 half
    of the second-cell claim at a cell inside its own scanned scope,
    and the two sentences sit two paragraphs apart in one section.
    Q4 measures it rather than inferring it.
D3  THE SCALE IS NOT THE NOMINAL PERIOD AND HAS NEVER BEEN MEASURED.
    D4 of the parent rig argues that a LOCAL obstruction recurs
    wherever its generating configuration recurs, so its run cannot
    reach the recurrence length -- copies would touch. The sharpest
    reading is therefore the SMALLEST such length, and feeding a
    MULTIPLE of it is the conservative direction: the threshold is too
    high, so gated cells can be missed and bounded ones cannot be
    manufactured. Every rig in the thread has fed the NOMINAL period
    the window was generated with. At the graded window
    [1, 1, A, 1, 1, B]^inf that is 6, and it is the true minimal
    period exactly when A != B -- on the DIAGONAL the sequence
    collapses to period 3. rule H1's map carries nine diagonal cells
    (4,4) .. (12,12) among its 210, read at 6 where 3 was available.
    Q5 reads them at 3.
D4  TWO SCALES ARE AVAILABLE AND THEY PART EXACTLY, which is what
    makes the choice load-bearing rather than a detail.
      SEQUENCE   the smallest s with a[j] = a[j+s] over the table.
                 Designed: P. Graded: 6 off the diagonal, 3 on it.
                 Two-class: P. Cubic and e - 2: NONE.
      LARGENESS  the smallest s with [a[j] >= 2] s-periodic.
                 Designed: P. Graded: 3. Two-class: P.
                 e - 2: 3. Cubic: NONE.
    They agree at the designed and two-class families and disagree at
    the graded family (3 against 6) and at e - 2 (3 against none). And
    the disagreement is not cosmetic: the graded r = 2 column at
    (13, 4) and (8, 5) is 0 0 3 2 1 0 0 0 3 2 1 0 0, whose runs are
    exactly 3, so the largeness scale GATES what the sequence scale
    reads bounded -- it revives the whole second surface rule H1
    killed. Q6 counts that over the map instead of asserting it from
    one column.
D5  AND WHAT FORBIDS THE CHEAPER SCALE IS span F4 ITSELF. The
    largeness scale reads the large-cap POSITIONS and nothing else.
    F4's witness is two windows with an IDENTICAL large-cap set,
    position for position, printing different verdicts -- so the
    positions do not decide, so the configuration that generates an
    obstruction includes the cap VALUES, so the recurrence length is
    the length at which the VALUES repeat: the sequence period. The
    rule is then family-specific to genuinely periodic quotient
    sequences BY DERIVATION rather than for want of a better idea, and
    an aperiodic window is refused because no scale it is entitled to
    exists there. This argument is only as good as F4, which Q2 and Q3
    re-read -- so the order is fixed: the re-read stages run and are
    read BEFORE S4 is read, and if F4 does not survive, D5 goes with
    it.
D6  WHAT THE JOINT REFUTATION DOES NOT KILL, said because it looks as
    though it should. F4 says the positions do not decide and roof H2
    says the drop-site VALUES do not decide, which between them
    exclude every criterion that is a function of the drop sites --
    and H2 is taken here at its weakest, since D1 has just said its
    own split is beyond re-reading; the argument below only needs the
    objection to exist, and a weaker objection makes it lighter. A
    SCALE is not such a criterion: the rule's observable is the c_min
    COLUMN, and the column is not drop-site data. e - 2's r = 1 and
    r = 2 carry identical drop-site multisets at identical positions
    and different columns, which is exactly the separation a scale is
    allowed to inherit and a verdict-from-drop-sites is not.
D7  THE ONE-WAY DIRECTION OF A TRUNCATION, inherited from D1 of the
    parent rig and needed here because the two-class family's windows
    are mostly 1s and their tables are the deepest in the thread.
    Truncating a column can only SHORTEN a run and lower a peak, so a
    cell read bounded at a truncated depth may be gated at the full
    one and never the reverse. S0 prints K(N) - 1 per window per range
    before any digits are built, so the cap this rig sets is known to
    clear the data rather than assumed to.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS,
never what it would mean)
  C1 (the positive control, run FIRST; nothing below is read if it is
      red) at the designed family [1^(P-1), A]^inf, P = 3, 4, 5 and
      A = 2, 3, 5, the run-length rule at the MEASURED minimal period
      prints the parity law at all nine windows and all 54 strides:
      delay-0 at r = 0 mod P, bounded at even residues, gated at odd.
      KILL: any miss.
  C2 (the diagonal control) the graded window at A = B, read at its
      measured minimal period 3, prints the designed family's law at
      strides 1..6. KILL: any miss -- the minimal-period reading would
      then be wrong at the one family where the answer is known.
  C3 (the cross-rig control) at r = 3 the value law reproduces over
      the pairs read here: bounded exactly on B < A <= 2B + 1 with
      A * B >= 30, delay-0 at A = B (rule H2 over 92 cells). KILL: any
      miss -- this rig is then not reading what rule.py read and
      nothing below is comparable.
  C4 (the retired classifier, reproduced) the two-class family read at
      three ranges by range_verdict prints roof H5's gap-parity
      disagreement count of 17. KILL: any other number -- the family
      path would then differ from roof's and Q1's comparison would not
      be a measurement.
  Q1 (roof H5) the 84 cells of the eight P = 4..7 windows under the
      rule at the deepest range. Observable: the verdict per cell, the
      cells that differ from the three-range reading, and the
      gap-parity disagreement count the rule leaves.
  Q2 (span F4, the control half) the 30 cells of the graded control,
      four windows at P = 3, 4, 5. Observable: the misses against
      F4-on-the-set (parity of r mod P), and whether the five misses
      F4 recorded survive.
  Q3 (span F4, the witness half, and F5's first clause) the three
      swapped pairs that still differ at three ranges -- (4, 8),
      (5, 8), (4, 9) against their swaps -- at r = 3. Observable:
      whether each pair still prints two different verdicts. F4 stands
      on these three and on nothing else. And across all 25 pairs of
      the value sweep, whether any stride OTHER than r = 3 departs
      from the parity law -- F5's "the cell is r = P and only r = P".
  Q4 (span F5's second observable, and values H4) which pairs move a
      stride other than r = 3, and which stride. D2 predicts no r = 2
      move at any pair, rule H1 having already read those cells.
  Q5 (the diagonal at its own period, D3) the nine diagonal cells of
      rule H1's map, (4,4) .. (12,12), at r = 2 read at the measured
      period 3 rather than the nominal 6. Observable: the run length
      and the verdict at each. A gated cell is a cell H1 read at a
      slack threshold.
  Q6 (the two scales, D4) both scales measured at every window used,
      and the graded map at r = 2 read under each. Observable: the
      count of cells whose verdict differs between the scales.
  Q7 (the refusals, D1) the cubic and e - 2 under the rule with the
      refusal ON. Observable: refused at every stride, and the count
      of roof's findings the rule can reach.

THE FIFTH SLATE, frozen AFTER S3 and S4 printed and reading only two
prints of theirs plus a rule that predates this rig -- said here because
a slate written after a print is the one that has to declare itself.
D5 argued the largeness scale away from the DERIVATION (F4 says the
values decide) and Q6 measured that the choice moves 175 of 210 cells.
But Q7 printed something D4 did not anticipate: at e - 2 the bounded
strides carry runs of 0 and the one gated stride the rule reaches by
run rather than saturation carries 6, so the largeness scale of 3 would
call e - 2's recorded split -- gated 1, 4, 7 -- EXACTLY. So there is
evidence on the other side of a derivation, and the two scales have
never been scored against a target that is independent of either.
Exactly one such target exists: the r = 3 VALUE LAW, established at
another rig under the retired classifier before either scale was
written, and reproduced at zero misses under the sequence scale (C3
here, rule H2 over 92 cells).
  Q8 (the discriminator) the 25 swept pairs at r = 3 under the
      LARGENESS scale 3 in place of the sequence scale 6. Observable:
      the misses against the value law. The value law's bounded cells
      are (8,4), (8,5) and (9,4); under a scale of 3 each stays
      bounded only if its longest run is below 3. KILL of the
      LARGENESS scale: any miss -- it would then break, on an
      independent target, the one law both scales were asked to
      preserve. KILL of the argument in D5: zero misses, which would
      leave two scales fitting every independent target and the
      corpus choosing between them by derivation alone, which is a
      weaker position than this rig has been writing.

THE DESIGN
----------
The RULE is imported from explore_cascade_rule.py -- verdict, runs_of
and the code table -- and not rewritten, for the reason that rig gives
in its own design section: the first candidate rule died partly because
a fresh loop rewrote a saturation guard the parent had documented as
inclusive, and a fresh loop inherits no guard a shared verdict
accumulated. The window builder, the digit path, the c_min row, the
retired classifier and gap parity come from explore_cascade_span.py for
the same reason and because C4 must be a measurement.

What is NEW here is the SCALE: every window's period is MEASURED off
its own quotient sequence by both readings of D4 rather than passed in
as the number the window was generated with.

S0  THE DEPTH BUDGET (weights only, no digits). K(N) - 1 per window per
    range against the cap this rig sets, and the measured scales beside
    the nominal periods. D7's and Q6's first observable, and it is what
    licenses the cap.
S1  THE CONTROLS. C1, C2, C3.
S2  THE TWO-CLASS FAMILY (Q1, C4). Eight windows, 84 cells, read at
    three ranges: the retired classifier for C4 and the rule at the
    deepest table.
S3  THE GRADED CONTROL AND THE VALUE SWEEP (Q2, Q3, Q4). The four
    control windows at 30 cells, then the 25 swept pairs at strides
    1..6.
S4  THE SCALE (Q5, Q6, Q7). The diagonal at its own period, the graded
    map at r = 2 under both scales, and the two aperiodic windows.
    Read only after S2 and S3, per D5.

RESOURCE: the rule takes ONE range, so the re-read of a surface costs a
fraction of what establishing it did -- but C4 needs the retired
classifier's three ranges at the two-class family, which is where the
cost is. Comparable stages: explore_cascade_roof.py S4 ran the same 84
cells at three ranges in 167.5 s at 245.4 MB, and explore_cascade_rule.py
read 92 cells at four ranges in 561 s. Estimate: S0 ~10 s, S1 ~60 s,
S2 ~180 s, S3 ~150 s, S4 ~120 s -- ABOUT 9 MINUTES over five stages,
stop at 20. The two-class windows are mostly 1s and carry the deepest
tables in the thread, so the cap is set at 34 and S0 checks it clears
K(N) - 1 everywhere before any digits are built. Peak working set
expected under 400 MB; run under memwatch at the 512 MB default. Stages
select by command-line argument (s0..s4) so no single call is
open-ended.

RUN RECORD
----------
Six runs under memwatch at the 512 MB default, peak commit 295.4 MB at
S4: S0 0.3 s, S1 170.3 s, S2 145.0 s VOIDED then 279.0 s, S3+S4 949.1 s
in one process, S5 117.7 s -- 28 minutes, against an estimate of 9 and a
stop at 20. The estimate was under by three causes, all named: it costed
C3 at nothing when C3 reads 25 windows at the deepest range; S2 gained a
whole second classifier pass when C4 fired; and Q6 is 210 cells at
N = 300000, which is the bulk of S4 and was folded into a "~120 s" line
that had no arithmetic behind it. The stop at 20 minutes was passed
inside the S3+S4 process and the necessity is Q6's own scope -- it
re-reads the 210 cells rule H1 states its verdict over, and a sample of
that map re-reads nothing.

C4 FIRED RED AND THE FIRST S2 IS VOID. It printed 25 gap-parity
disagreements where explore_cascade_roof.py H5 records 17, and the cause
is that this rig read the RETIRED classifier at its own deep cap where
every parent rig reads it at 10. The rig now builds both tables and
scores both, which is what H5 below is. Nothing else moved: the rule's
own reading is at the data's own depth in either run.

THE FIFTH SLATE WAS FROZEN AFTER A PRINT and says so where it stands.
S5 exists because Q7 printed e - 2's run lengths and they favoured the
scale D5 had argued away; it reads those runs, C3's law, and nothing
else.

FINDINGS (each at its own tier)
-------------------------------
H1  THE TWO-CLASS FAMILY SURVIVES THE INSTRUMENT AND ITS COUNT MOVES BY
    ONE (rule at scanned scope, 84 cells at the data's own depth; Q1,
    with C4 green at 17). Read under the run-length rule, gap parity
    disagrees at 16 of the 84 cells where the retired classifier at
    three ranges disagrees at 17. So explore_cascade_span.py F6's
    verdict -- the position-only reading fails inside the PERIODIC
    families and not only at the cubic -- is instrument-independent,
    and roof H5's count moves from 17 to 16. Five cells move, and NOT
    ONE of them is one of the two movers the third range found: the
    range set and the classifier disturb disjoint cells, which is why
    a count reproduced is not a reading reproduced.
H2  span F4 AND F5 BOTH STAND, AND F5 STANDS STRONGER THAN IT WAS
    (rule at scanned scope; Q2 over 30 cells, Q3 over 25 pairs). F4's
    witness is intact at 3 of 3: (4,8), (5,8) and (4,9) still print a
    different r = 3 verdict from their swaps, so the positions do not
    decide. Its CONTROL half improves -- the graded control misses
    F4-on-the-set at 4 of 30 cells where F4 recorded 5, and the four
    are the half-period cell r = P at all four windows. The fifth, the
    one F4 called "a genuine parity-cell flip" at P = 5, caps 2/4,
    r = 7, was the classifier: the rule reads it bounded, which is
    what the parity law asks for. That makes F5's first clause exact
    rather than nearly so -- the departure is r = P and only r = P,
    now with no exception anywhere in the family.
H3  THE SECOND CELL WAS THE CLASSIFIER, AND THE CORPUS ALREADY HELD
    ITS OWN REFUTATION (rule at scanned scope, 25 pairs at six strides;
    Q4, predicted by D2 before the run). At every one of the 25 swept
    pairs the verdict vector is the parity law exactly, with r = 3 the
    only departure: ZERO pairs move a second stride. So F5's "three
    pairs also move a SECOND cell" -- (4,8) and (4,9) at r = 5, (8,5)
    at r = 2 -- and explore_cascade_values.py H4's "six of the 64 grid
    pairs move a stride other than r = P, two of them at min >= 6" are
    both gone, at r = 5 as well as at r = 2. D2 predicted the r = 2
    half from the record alone: rule H1 reads all 210 cells of
    B = 3..12 over A = 4..24 bounded at r = 2, and (8,5) sits inside
    that map. The refutation was already on the record beside the
    claim, and the two had never been put side by side.
H4  THE SCALE A RUN IS MEASURED AGAINST IS THE SEQUENCE PERIOD, AND
    THE VALUE LAW IS WHAT DECIDES IT (rule; Q6 over 210 cells, Q8 over
    25 pairs). The rule's threshold is a run against a period, and two
    scales are derivable from a window: the SEQUENCE period and the
    LARGENESS pattern's. They agree at the designed and two-class
    families and part at every graded window (3 against 6) and at
    e - 2 (3 against none) -- and the parting is not a detail, moving
    175 of rule H1's 210 cells, the largeness scale reviving most of
    the second surface that rig killed. The derivation says sequence:
    F4 (H2 above) says the VALUES decide, so the configuration
    generating a local obstruction includes the cap values, so the
    recurrence length is the length at which the values repeat. And
    the derivation is not what settles it, because Q7 printed evidence
    the other way -- at e - 2 the largeness scale of 3 calls the split
    on record EXACTLY, gated at 1, 4, 7 and bounded at 2, 5, 8. The
    one target independent of both scales settles it: at r = 3 the
    largeness scale misses the VALUE LAW at 3 of 25 pairs, and the
    three are precisely its three bounded cells, (8,4), (8,5) and
    (9,4), each carrying a longest run of 5 -- at or above 3 and below
    6. The value law's whole bounded set is the cells whose runs sit
    strictly between the two scales. So a scale that calls the
    aperiodic window right is a scale that breaks the periodic law,
    and e - 2's agreement is a fact about e - 2 rather than evidence
    for the scale.
H5  THE RETIRED CLASSIFIER MOVES WITH THE INSTRUMENT CAP AS WELL AS
    WITH THE RANGE SET, which is a second axis its funeral never named
    (observation; C4's red, 84 cells). The same classifier over the
    same eight windows at the same three ranges disagrees with gap
    parity at 17 cells read at cap 10 and at 25 read at cap 34. rule
    H1 retired it for reading the range SPAN rather than the range
    DEPTH -- a rule with no fixed point in the RANGE SET. It has no
    fixed point in the CAP either, and every number the cascade
    carries from it is a reading at one particular cap that no finding
    states. The run-length rule has neither, reading one table at the
    data's own depth. This was not predicted; it fell out of a control
    firing.
H6  FOUR OF roof'S FIVE FINDINGS ARE OUT OF THE RULE'S REACH, AND THE
    RULE IS FAMILY-SPECIFIC BY DERIVATION AND NOT BY DEFAULT
    (property + measurement; D1, Q7). With the refusal on, the cubic
    is refused at 7 of 8 strides and reached only where r = 1
    saturates; e - 2 is refused at 4 of 8, reached at two saturations
    and two delay-0 cells. So roof H1's split cannot be re-read, and
    H2's identical-multiset witness and H3's scoring rest on it --
    H2's own witness pair r = 1 against r = 2 has one member saturated
    and the other refused. H4 dissolves instead: its subject is which
    cells MOVED under a third range, and a rule with no range set has
    no movers, so the sweep it argued for costs nothing here. Only H5
    is in reach, and it is H1 above. What makes this a scope statement
    rather than a gap is H4 together with which scale SURVIVES at an
    aperiodic window: the sequence length is undefined there, the
    largeness length is defined, and the largeness length is the one
    the value law refutes. So the rule is left with no scale it is
    entitled to, rather than with one it has not thought of. The founding question -- what
    plays the period at a window that has none -- is answered for the
    RUN in the negative, where gap parity answered it for the
    CRITERION in the positive by moving to the large-cap set.
H7  AND THE NOMINAL PERIOD WAS SLACK AT NINE CELLS WITH NO CONSEQUENCE
    (observation; Q5, D3). Every rig in the thread fed the rule the
    period its windows were GENERATED with, and at the graded map's
    diagonal that is 6 where the sequence collapses to 3 -- a
    threshold too high, the direction that misses gated cells. All
    nine of rule H1's diagonal cells are read again at 3: none gates,
    because every one of their r = 2 columns is identically zero at
    every depth. H1's 210 stand. The check was owed and it is cheaper
    to run than to argue.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_shift_repair import (          # noqa: E402
    build_q,
    designed,
    quotients_cbrt2_minus_1,
    quotients_e_minus_2,
    usable_depth,
)
from explore_cascade_span import (          # noqa: E402
    RANGES3,
    WANT,
    cell_rows,
    gap_parity,
    graded,
    range_verdict,
)
from explore_cascade_rule import (          # noqa: E402
    CODE,
    GATEDISH,
    col,
    verdict,
)

DEEP = 34            # S0 checks this clears K(N)-1 at every window used
OLD_CAP = 10         # the shared instrument cap every parent rig read at
N_TOP = RANGES3[-1]
CUBIC = quotients_cbrt2_minus_1(WANT)
E2MINUS = quotients_e_minus_2(WANT)

# the eight two-class windows of explore_cascade_span.py F6 / roof H5
TWO_CLASS = ((4, 1, 3, 5, 2), (4, 1, 3, 2, 5),
             (5, 1, 3, 5, 2), (5, 0, 2, 4, 2),
             (6, 1, 4, 5, 2), (6, 0, 3, 5, 2),
             (7, 1, 4, 5, 2), (7, 2, 3, 5, 2))

# the four graded-control windows of span E3
GRADED_CTRL = ((3, 5, 2), (3, 2, 5), (4, 3, 2), (5, 2, 4))

# span E4's eleven pairs and E5's fourteen, deduplicated in order
SWEEP = ((2, 2), (3, 3), (5, 5),
         (2, 3), (3, 2), (2, 5), (5, 2), (3, 5), (5, 3), (2, 7), (7, 2),
         (2, 4), (4, 2), (3, 6), (6, 3), (4, 8), (8, 4),
         (4, 7), (7, 4), (5, 8), (8, 5), (3, 7), (7, 3), (4, 9), (9, 4))

# the pairs F4 still stands on after the third range (span F4's note)
WITNESS = ((4, 8), (5, 8), (4, 9))


# ------------------------------------------------------------ the scale

def measured_period(a, upto=None):
    """Smallest s with a[j] = a[j+s] over the prefix, or None (D4)."""
    n = len(a) if upto is None else min(upto, len(a))
    for s in range(1, n // 2 + 1):
        if all(a[j] == a[j + s] for j in range(n - s)):
            return s
    return None


def largeness_period(a, upto=None):
    """Smallest s with [a[j] >= 2] s-periodic over the prefix (D4)."""
    n = len(a) if upto is None else min(upto, len(a))
    big = [x >= 2 for x in a[:n]]
    for s in range(1, n // 2 + 1):
        if all(big[j] == big[j + s] for j in range(n - s)):
            return s
    return None


def gwin(A, B):
    """The graded window [1, 1, A, 1, 1, B]^inf -- nominal period 6."""
    return graded(6, {2: A, 5: B})


PARITY = {0: "delay0", 1: "gated", 2: "bnd"}


def parity_law(r, P):
    """F4's law: delay-0 at r = 0 mod P, bounded even, gated odd."""
    res = r % P
    return "delay0" if res == 0 else ("bnd" if res % 2 == 0 else "gated")


def cell(a, n, rmax, period, refuse=True, cap=DEEP):
    """One cell at one range at the deep cap, per stride."""
    rows = cell_rows("", a, n, rmax=rmax, tmax_cap=cap, show=False)
    out = {}
    for r, row in rows.items():
        out[r] = {
            "tmax": row["tmax"],
            "v": verdict(row["A"], row["tmax"], row["repairs"], period,
                         refuse),
            "row": row,
        }
    return out


def cmin(row):
    return " ".join(f"{max(0, row['A'][t] - t + 1):2d}"
                    for t in range(1, row["tmax"] + 1))


def matches(got, want):
    """A reading agrees with a predicted verdict (saturation gates)."""
    return got == want or (want == "gated" and got in GATEDISH)


# --------------------------------------------------------------- S0

def s0_budget():
    print("=" * 78)
    print("S0 THE DEPTH BUDGET AND THE TWO SCALES (weights only)")
    print(f"   the cap this rig sets is {DEEP}; a K(N)-1 at or above it "
          "would truncate (D7)")
    print()
    wins = []
    for P, c1, c2, A, B in TWO_CLASS:
        wins.append((f"X P={P} {A}@{c1}/{B}@{c2}", graded(P, {c1: A, c2: B})))
    for P, A, B in GRADED_CTRL:
        wins.append((f"G P={P} {A}/{B}", graded(2 * P, {P - 1: A,
                                                        2 * P - 1: B})))
    for P in (3, 4, 5):
        for A in (2, 3, 5):
            wins.append((f"D P={P} A={A}", designed(P, A, WANT)))
    for A, B in ((13, 4), (8, 5), (9, 9), (4, 4)):
        wins.append((f"g A={A} B={B}", gwin(A, B)))
    wins.append(("cbrt(2)-1", CUBIC))
    wins.append(("e-2", E2MINUS))
    worst = 0
    print(f"  {'window':22s} {'seq':>4s} {'large':>5s}   K(N)-1 at "
          + " ".join(f"{n // 1000:6d}k" for n in RANGES3))
    for name, a in wins:
        ks = [usable_depth(build_q(a, n), n) - 1 for n in RANGES3]
        worst = max(worst, max(ks))
        sp, lp = measured_period(a, 40), largeness_period(a, 40)
        print(f"  {name:22s} {str(sp):>4s} {str(lp):>5s}   "
              + "        ".join(f"{k:2d}" for k in ks)
              + ("   <<< TRUNCATED" if max(ks) >= DEEP else ""))
    print(f"  deepest K(N)-1 over every window used: {worst}, cap {DEEP} -- "
          + ("clears" if worst < DEEP else "DOES NOT CLEAR, S1..S4 are void"))
    return worst < DEEP


# --------------------------------------------------------------- S1

def s1_controls():
    print("=" * 78)
    print("S1 THE CONTROLS")
    print()
    print("-- C1 the designed family at the MEASURED minimal period, "
          "N = 100000 --")
    miss = 0
    for P in (3, 4, 5):
        for A in (2, 3, 5):
            a = designed(P, A, WANT)
            per = measured_period(a, 40)
            c = cell(a, 100_000, 2 * P, per)
            bad, line = [], []
            for r in sorted(c):
                got = c[r]["v"][0]
                want = parity_law(r, P)
                if not matches(got, want):
                    bad.append((r, want, got))
                line.append(f"r{r}:{col(c[r]['v'])}")
            miss += len(bad)
            print(f"  D P={P} A={A} period {per} t<={c[1]['tmax']:2d} "
                  + " ".join(line))
            if bad:
                print(f"      C1 MISS {bad}")
    print(f"  C1: {miss} stride misses over 9 windows / 54 strides -- "
          + ("GREEN" if not miss else "RED, nothing below is read"))
    print()
    print("-- C2 the diagonal graded window at its own measured period --")
    dmiss = 0
    for A in (4, 5, 9):
        a = gwin(A, A)
        per = measured_period(a, 40)
        c = cell(a, N_TOP, 6, per)
        bad, line = [], []
        for r in sorted(c):
            got = c[r]["v"][0]
            want = parity_law(r, 3)
            if not matches(got, want):
                bad.append((r, want, got))
            line.append(f"r{r}:{col(c[r]['v'])}")
        dmiss += len(bad)
        print(f"  g A=B={A} period {per} (nominal 6) t<={c[1]['tmax']:2d} "
              + " ".join(line))
        if bad:
            print(f"      C2 MISS {bad}")
    print(f"  C2: {dmiss} misses -- " + ("GREEN" if not dmiss else "RED"))
    print()
    print("-- C3 the value law at r = 3 over the swept pairs "
          "(rule H2: bounded iff B < A <= 2B+1 and A*B >= 30) --")
    cmiss = 0
    line = []
    for A, B in SWEEP:
        a = gwin(A, B)
        per = measured_period(a, 40)
        c = cell(a, N_TOP, 3, per)
        got = c[3]["v"][0]
        want = ("delay0" if A == B
                else "bnd" if (B < A <= 2 * B + 1 and A * B >= 30)
                else "gated")
        ok = matches(got, want)
        cmiss += not ok
        line.append(f"({A},{B}){CODE[got]}" + ("" if ok else "!"))
    print("  " + "  ".join(line))
    print(f"  C3: {cmiss} misses over {len(SWEEP)} pairs -- "
          + ("GREEN" if not cmiss else "RED"))
    return miss == 0 and dmiss == 0 and cmiss == 0


# --------------------------------------------------------------- S2

def s2_two_class():
    print("=" * 78)
    print("S2 THE TWO-CLASS FAMILY (roof H5 / span F6), 84 cells")
    print("   the retired classifier at three ranges beside the rule at "
          "the deepest table")
    print("   C4: the retired classifier must print 17 gap-parity "
          "disagreements")
    old_dis = deep_dis = new_dis = moved = 0
    cells = 0
    for P, c1, c2, A, B in TWO_CLASS:
        a = graded(P, {c1: A, c2: B})
        per = measured_period(a, 40)
        rmax = min(2 * P, 12)
        # the retired classifier at the PARENT'S cap, which is what C4
        # reproduces -- it reads a different verdict at a different cap,
        # so the deep tables below cannot stand in for it
        shal = [cell_rows("", a, n, rmax=rmax, tmax_cap=OLD_CAP, show=False)
                for n in RANGES3]
        rows = [cell_rows("", a, n, rmax=rmax, tmax_cap=DEEP, show=False)
                for n in RANGES3]
        print()
        print(f"-- X P={P} caps {A}@{c1}/{B}@{c2}  measured period {per} "
              f"(nominal {P})  t<={rows[-1][1]['tmax']} "
              f"(old cap {shal[-1][1]['tmax']}) --")
        for r in sorted(rows[0]):
            cells += 1
            old = range_verdict([row[r] for row in shal])
            deepold = range_verdict([row[r] for row in rows])
            deep = rows[-1][r]
            v = verdict(deep["A"], deep["tmax"], deep["repairs"], per)
            gp = gap_parity(a, r, 30)[3]
            tr = {"GATED": "gated", "bounded": "bnd", "delay-0": "delay0"}
            oldc, deepc, gpc = tr[old], tr[deepold], tr[gp]
            od = oldc != gpc
            dd = deepc != gpc
            nd = not matches(v[0], gpc) and v[0] != gpc
            old_dis += od
            deep_dis += dd
            new_dis += nd
            mv = v[0] != oldc and not (v[0] in GATEDISH
                                       and oldc == "gated")
            moved += mv
            print(f"  r{r:3d}  old {CODE[oldc]}  old@{DEEP} {CODE[deepc]}"
                  f"  rule {col(v)}  gap-parity {CODE[gpc]}"
                  f"{'  old-dis' if od else '        '}"
                  f"{'  rule-dis' if nd else '         '}"
                  f"{'   <<< MOVED' if mv else ''}")
            print(f"        c_min {cmin(deep)}")
    print()
    print(f"  cells {cells}; retired classifier at the parent's cap "
          f"{OLD_CAP}: {old_dis} gap-parity disagreements (C4 wants 17 -- "
          + ("GREEN" if old_dis == 17 else "RED") + ")")
    print(f"  the SAME classifier at cap {DEEP}: {deep_dis} -- the "
          "retired rule's own verdict moves with the instrument cap, "
          "not only with the range set")
    print(f"  rule gap-parity disagreements {new_dis}; cells that moved "
          f"under the rule {moved}")


# --------------------------------------------------------------- S3

def s3_graded():
    print("=" * 78)
    print("S3 THE GRADED CONTROL AND THE VALUE SWEEP (span F4, F5)")
    print()
    print("-- Q2 the graded control, 30 cells: F4-on-the-set predicts "
          "the parity of r mod P --")
    total = 0
    for P, A, B in GRADED_CTRL:
        a = graded(2 * P, {P - 1: A, 2 * P - 1: B})
        per = measured_period(a, 40)
        c = cell(a, N_TOP, 2 * P, per)
        bad, line = [], []
        for r in sorted(c):
            got = c[r]["v"][0]
            want = parity_law(r, P)
            if not matches(got, want):
                bad.append((r, want, got))
            line.append(f"r{r}:{col(c[r]['v'])}")
        total += len(bad)
        print(f"  G P={P} caps {A}/{B} period {per} (nominal {2 * P}) "
              f"t<={c[1]['tmax']:2d}")
        print("      " + " ".join(line))
        if bad:
            print(f"      misses F4-on-the-set: {bad}")
    print(f"  Q2: {total} misses over 30 cells (span F4 recorded 5)")
    print()
    print("-- Q3 / Q4 the value sweep, strides 1..6, P = 3.")
    print("   F4's law on the set is  G b . G b .  and F5 says the only "
          "departure is r = 3 --")
    vecs = {}
    second = []
    for A, B in SWEEP:
        a = gwin(A, B)
        per = measured_period(a, 40)
        c = cell(a, N_TOP, 6, per)
        v = "".join(CODE[c[r]["v"][0]] for r in sorted(c))
        vecs[(A, B)] = (v, c, per)
        off = [r for r in sorted(c)
               if r != 3 and not matches(c[r]["v"][0], parity_law(r, 3))]
        if off:
            second.append(((A, B), off))
        print(f"  A={A} B={B} period {per}: " + " ".join(v)
              + (f"   <<< departs at r = {off}" if off else ""))
    print(f"  Q3 second clause: {len(second)} of {len(SWEEP)} pairs depart "
          f"from the parity law at a stride other than r = 3")
    print(f"  Q4: the departures are {second}")
    print(f"      r = 2 departures: "
          f"{[p for p, o in second if 2 in o]} (D2 predicts none)")
    print()
    print("-- Q3 first clause: F4's three surviving swapped pairs at "
          "r = 3 --")
    alive = 0
    for A, B in WITNESS:
        v1 = vecs[(A, B)][0][2]
        v2 = vecs[(B, A)][0][2]
        differ = v1 != v2
        alive += differ
        print(f"  ({A},{B}) r3 = {v1}   ({B},{A}) r3 = {v2}   "
              + ("DIFFER -- F4's witness holds here" if differ
                 else "AGREE -- this pair no longer witnesses"))
    print(f"  Q3: {alive} of {len(WITNESS)} swapped pairs still differ; "
          "F4 stands iff at least one does")


# --------------------------------------------------------------- S4

def s4_scale():
    print("=" * 78)
    print("S4 THE SCALE (read only after S2 and S3, per D5)")
    print()
    print("-- Q5 the diagonal cells of rule H1's map at r = 2, read at "
          "the measured period 3 rather than the nominal 6 --")
    gated = 0
    for A in range(4, 13):
        a = gwin(A, A)
        per = measured_period(a, 40)
        c = cell(a, N_TOP, 2, per)
        cn = cell(a, N_TOP, 2, 6)
        g = c[2]["v"][0] in GATEDISH
        gated += g
        print(f"  A=B={A:2d} period {per}: measured {col(c[2]['v'])}"
              f"   nominal-6 {col(cn[2]['v'])}"
              + ("   <<< GATED AT ITS OWN PERIOD" if g else ""))
        print(f"          c_min {cmin(c[2]['row'])}")
    print(f"  Q5: {gated} of 9 diagonal cells gate at the measured period")
    print()
    print("-- Q6 the graded map at r = 2 under both scales, B = 3..12 "
          "over A = 4..24 (rule H1's 210 cells) --")
    diff = 0
    for B in range(3, 13):
        seq_row, lrg_row = [], []
        for A in range(4, 25):
            a = gwin(A, B)
            sp, lp = measured_period(a, 40), largeness_period(a, 40)
            c = cell_rows("", a, N_TOP, rmax=2, tmax_cap=DEEP, show=False)[2]
            vs = verdict(c["A"], c["tmax"], c["repairs"], sp)
            vl = verdict(c["A"], c["tmax"], c["repairs"], lp)
            seq_row.append(CODE[vs[0]])
            lrg_row.append(CODE[vl[0]])
            diff += vs[0] != vl[0]
        print(f"  B={B:2d}  sequence  " + " ".join(seq_row))
        print(f"        largeness " + " ".join(lrg_row))
    print(f"  Q6: {diff} of 210 cells differ between the two scales")
    print()
    print("-- Q7 the two aperiodic windows under the rule, refusal ON --")
    for name, a in (("cbrt(2)-1", CUBIC), ("e-2", E2MINUS)):
        sp, lp = measured_period(a, 40), largeness_period(a, 40)
        c = cell(a, 100_000, 8, sp if sp else 10 ** 6)
        line = " ".join(f"r{r}:{CODE[c[r]['v'][0]]}L{c[r]['v'][1]:2d}"
                        for r in sorted(c))
        print(f"  {name:10s} sequence period {sp}  largeness {lp}")
        print(f"      {line}")
    print("  Q7: roof's five findings -- H1, H2, H3 rest on the two "
          "windows above, H4's subject is a range set the rule does not "
          "have, H5 is S2.")


def s5_discriminator():
    print("=" * 78)
    print("S5 THE DISCRIMINATOR (Q8) -- the value law at r = 3 under the "
          "LARGENESS scale")
    print("   the sequence scale reproduces it at zero misses (C3). The "
          "value law is bounded")
    print("   iff B < A <= 2B + 1 and A*B >= 30, and it is the one target "
          "independent of both scales.")
    miss = 0
    for A, B in SWEEP:
        a = gwin(A, B)
        sp, lp = measured_period(a, 40), largeness_period(a, 40)
        row = cell_rows("", a, N_TOP, rmax=3, tmax_cap=DEEP,
                        show=False)[3]
        vs = verdict(row["A"], row["tmax"], row["repairs"], sp)
        vl = verdict(row["A"], row["tmax"], row["repairs"], lp)
        want = ("delay0" if A == B
                else "bnd" if (B < A <= 2 * B + 1 and A * B >= 30)
                else "gated")
        ok = matches(vl[0], want)
        miss += not ok
        print(f"  A={A:2d} B={B:2d} seq {sp} large {lp}: "
              f"sequence {col(vs)}  largeness {col(vl)}  law "
              f"{CODE[want]}" + ("" if ok else "   <<< LARGENESS MISSES"))
    print(f"  Q8: the largeness scale misses the value law at {miss} of "
          f"{len(SWEEP)} pairs")
    print()
    print("-- and e - 2 under its own largeness scale, printed because "
          "Q7's runs are what forced this slate --")
    c = cell(E2MINUS, 100_000, 8, largeness_period(E2MINUS, 40))
    print("      " + " ".join(f"r{r}:{col(c[r]['v'])}" for r in sorted(c)))
    print("      the split on record is gated 1, 4, 7 -- itself a "
          "reading of the retired classifier")


STAGES = {"s0": s0_budget, "s1": s1_controls, "s2": s2_two_class,
          "s3": s3_graded, "s4": s4_scale, "s5": s5_discriminator}

if __name__ == "__main__":
    for key in (sys.argv[1:] or ["s0"]):
        STAGES[key]()
