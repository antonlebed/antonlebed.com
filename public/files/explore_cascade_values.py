"""The value law at the half-period cell, read off the FULL grid rather
than off a sample of it.

THE QUESTION
------------
At the graded trailing-Ostrowski window [1, 1, A, 1, 1, B]^inf the
stride verdict is the parity of r mod 3 at every stride but ONE
(explore_cascade_span.py F5). The exception is the HALF-PERIOD stride
r = 3, the shift carrying each large-cap class member onto the other:
the equal family A = B has no repair there at all, and every unequal
pair has a LARGE-ONTO-LARGE drop instead -- an overflow landing on a
position that is itself an absorber. That one cell is where the cap
VALUES act, and the parent rig read its law off 25 pairs:

    min(A, B) = 2   -> GATED in both orders
    min(A, B) >= 3  -> GATED unless A exceeds B by 3 or more

with ORDER, RATIO and DIFFERENCE all dead against that table. Twenty-
five points cannot separate the readings that fit it. This rig prints
the whole surface at once: the (A, B) grid over 2..9 at P = 3, one
verdict vector per pair, 64 windows of which eight are the A = B
control.

THE HAND-ATTACK (pre-engine, on paper)
--------------------------------------
WHICH CELLS ARE NEW. The parent measured 22 off-diagonal pairs, all
of them with min(A, B) <= 5 and every BOUNDED one among them carrying
B in {3, 4, 5}. The grid's 56 off-diagonal cells therefore buy three
things the sample could not:

  (i) THE min = 2 WALL AT ITS EXTREME. The clause "min = 2 gates in
      both orders" is the half of the law no ratio and no difference
      reading has, and it rests on (4, 2), (5, 2), (7, 2) and their
      mirrors -- a largest gap of 5. The grid runs it to (9, 2), gap
      7. If a gap-only reading were right with the min = 2 rows an
      artifact of small gaps, this column is where it shows.

 (ii) A FORK THE SAMPLE CANNOT SEE. Every measured bounded cell has
      B <= 5, so two readings of the same table are open:
          FLOOR ONLY   bounded iff B >= 3 and A - B >= 3
          FLOOR + ROOF bounded iff 3 <= B <= 5 and A - B >= 3
      -- the second saying the absorber must be small as well as not
      tiny. They differ at exactly ONE cell in this grid, (9, 6),
      which is the only pair with B >= 6 that the difference clause
      can reach at all (B = 6 needs A >= 9). One window decides it.

(iii) THE THRESHOLD READ ALONG EACH ROW. "A exceeds B by 3 or more"
      is one number fitted across three values of B. On the grid the
      row B = 3 runs A = 4..9 and the row B = 4 runs A = 5..9, so the
      threshold is read PER ROW rather than pooled, and a threshold
      that drifts with B is visible where a pooled fit would hide it.

WHAT CANNOT BE SEPARATED HERE, said in advance so no reading claims
it. Within B >= 3, "A - B >= 3" and "A >= B + 3 and A >= 6" and
"A - B >= 3 and A + B >= 9" all agree on every cell of this grid,
because B >= 3 with A - B >= 3 forces A >= 6 and A + B >= 9. A grid
over 2..9 cannot part them; only a window with B >= 3 and A < 6 could,
and none exists.

PREDICTIONS, FIXED BEFORE THE RUN (as observables -- what the rig
PRINTS, never what it would mean)
  Q1 (positive control, exact) the eight diagonal pairs A = B = 2..9
      print the vector G b . G b . -- the designed family's own law,
      since A = B IS that family. KILL: any diagonal row differing.
      The grid is then void and nothing below it is read.
  Q2 (the standing law) at every off-diagonal cell, r = 3 reads
      bounded iff min(A, B) >= 3 and A - B >= 3, and GATED otherwise.
      KILL: any cell disagreeing -- and a disagreement is the finding,
      not a failure, since the law was fitted to a quarter of these
      cells.
  Q3 (the min = 2 wall) every cell of the B = 2 column and the A = 2
      row is GATED at r = 3, to A = 9 and B = 9. KILL: any of them
      bounded, which would make the wall a small-gap artifact and put
      a pure gap reading back on the table.
  Q4 (the fork) (9, 6) reads bounded under FLOOR ONLY and GATED under
      FLOOR + ROOF. Both are live; the cell is the observable and the
      reading is scored after it prints.
  Q5 (the second cell) the three known second-cell moves reproduce --
      (4, 8) and (4, 9) gate r = 5, (8, 5) gates r = 2 -- and if the
      concentration in the half-period cell is the small-value fact
      the parent rig called it, no pair with min(A, B) >= 6 moves a
      second cell. KILL: a second-cell move at min(A, B) >= 6, which
      makes the moves a law of the pair rather than a small-value
      edge.

THE DESIGN
----------
Windows, digit path, c_min rows and the VERDICT CLASSIFIER are
imported from explore_cascade_span.py -- not reimplemented. That is a
control and not a convenience: the classifier carries two guards that
were added because a control went red without them (a column sitting
exactly AT the lookahead ceiling reads as an ordinary number; a column
with a strictly declining tail is one deep witness rather than a local
event), and a fresh loop over the same windows inherits neither. The
range pair, the lookahead ceiling and the stride cap are the parent's
too, so every cell here is comparable to the 25 it extends.

G1  THE GRID. graded(6, {2: A, 5: B}) for A, B in 2..9, one verdict
    vector per pair at two ranges, growth-authoritative. Printed as
    the full 8x8 matrix of the r = 3 verdict with the diagonal marked,
    scored against Q2 cell by cell, with the per-row threshold (the
    smallest A at which each row B turns bounded) read off the matrix
    rather than fitted to it. Q1..Q4's observable.
G2  THE SECOND CELL. The same 64 vectors read at the strides OTHER
    than r = 3: every pair whose vector differs from G b . G b . away
    from position 3, listed with the stride that moved. Q5's
    observable. No new run -- G1's vectors are reused.
G3  THE ROOF. Rows B = 3, 4, 5, 6 with A run to 16, verdict vector
    and usable depth per window, each row's gated threshold read off
    the row and scored against both frozen roofs. Q6 and Q7's
    observable. Written after G1 printed, on G1's matrix alone.
G5  THE BOUNDED CELLS AT THREE RANGES. The 24 cells G1 and G3 read
    bounded at r = 3, each re-read at three ranges to 300000, scored
    against Q10's corrected law. Q9 and Q10's observable. The gated
    cells are not re-read and the reason is the one-way argument
    above, stated so a reader can refuse it.
G6  THE ONE-WAY CLAIM. Nine cells that read GATED at two ranges, one
    or two on each side of each clause's boundary, re-read at three.
    G5 re-reads only the bounded cells and the ARGUMENT for that is
    the one-way direction; this stage measures it instead. Added
    after G5 printed, reading the classifier's own fall-through path
    and no result.
G4  THE ANOMALIES AT THREE RANGES. `ranged` at (8, 3), (9, 3),
    (8, 9) with (7, 3), (5, 4) and (5, 3) beside them, to 300000 --
    the c_min rows, drop and large-onto-large counts, and span per
    range. Q8's observable.

THE SECOND SLATE (frozen after G1 printed and before G3 was written;
it reads only G1's r = 3 matrix, which fixes no roof)
------------------------------------------------------------------
G1's bounded set has a FLOOR that is A > B at every row B >= 4 and a
ROOF sighted at exactly one row: B = 3 is bounded at A = 6, 7 and
GATED again at A = 8, 9. At every other row the bounded run reaches
A = 9 and stops there because the grid does, so the roof is measured
once and its shape is a fit to two numbers. Two readings pass through
them and they are separable by construction:

    ROOF-RATIO    bounded needs A < (8/3) B
    ROOF-DOUBLE   bounded needs A <= 2B + 1

Both call B = 3 exactly (bounded 6, 7; gated from 8). They disagree
from B = 4 up: ratio turns B = 4 gated at A = 11, B = 5 at A = 14,
B = 6 at A = 16; double turns them gated at A = 10, 12, 14. The
parting cells are (10, 4), (12, 5), (13, 5), (14, 6) and (15, 6),
where double says GATED and ratio says bounded.

  Q6 (the roof) at rows B = 3, 4, 5, 6 with A run to 16, each row
      turns GATED at one A and stays gated above it. KILL of
      ROOF-RATIO: a row turning gated below its ratio threshold.
      KILL of ROOF-DOUBLE: a row still bounded at 2B + 2. KILL OF
      BOTH SHAPES: a row that is not an interval -- bounded, gated,
      bounded again -- which would mean the roof is not a threshold
      at all.
  Q7 (the instrument at large caps) a bigger cap makes q grow faster,
      so the usable depth at a fixed N shrinks and a verdict can be
      read off a table too short to carry one. The usable depth is
      PRINTED per window beside its verdict rather than assumed.
      KILL: usable depth below 4 at any window whose verdict is read
      -- that row is then an instrument limit and not a measurement.
  Q8 (the anomalies re-read) three G1 cells break the shape the rest
      of the matrix has: (8, 3) and (9, 3) gate above a bounded run,
      and (8, 9) is the ONLY A < B cell in the grid that is bounded.
      Each is re-read at THREE ranges to 300000 with its c_min rows,
      drop counts and span beside it, against (7, 3) and (5, 4) as
      bounded controls and (5, 3) as a gated one. The observable is
      whether each cell's c_min column is unchanged across the three
      ranges. KILL: a verdict that moves with the range -- the cell
      is then a classifier reading and not a fact about the window.

THE THIRD SLATE (frozen after G4 printed; it reads G4's control
failure and G3's roof, and nothing else)
--------------------------------------------------------------
G4 fired Q8's kill on a CONTROL rather than on an anomaly: (5, 4),
which G1 and G3 both read bounded at two ranges, reads GATED at
300000 -- its c_min column is 0 0 0 5 4 3 2 1 0 0 at 30000 and at
100000 and opens to 0 0 0 > 10 9 8 7 6 5 at 300000. So the two-range
surface is a two-range reading and not the window's verdict, and the
direction of the error is one-way: adding a deeper range can only
DEEPEN a witness or push a column onto the lookahead ceiling, and the
classifier reads growth and saturation at the DEEPEST range, so a cell
called GATED at two ranges cannot turn bounded at three. Only the
bounded cells are suspect, and there are 24 of them across G1 and G3.

  Q9 (the depth) every cell that read bounded at r = 3 in G1 or G3 is
      re-read at three ranges to 300000. KILL of the two-range
      surface: any flip -- G1's and G3's matrices are then superseded
      cell for cell by this one, and no reading is taken off them.
  Q10 (the corrected law) with (5, 4) gated, the floor and the roof
      state one interval in the GAP: bounded iff B >= 3 and
      3 <= A - B <= B + 1. It calls G3's row B = 3 exactly and with
      no exception -- bounded A = 6, 7 -- which the two-range floor
      A > B could only call by exempting that row. Its predictions
      here: exactly ten cells flip to GATED -- (6, 4), (6, 5),
      (7, 5), (7, 6), (8, 6), (8, 7), (8, 9), (9, 7), (9, 8) and
      (5, 4), already flipped -- and the other fourteen hold bounded,
      including (10, 6) through (13, 6), whose gaps 4..7 all sit
      under that row's roof of 7. KILL: any cell disagreeing.

RESOURCE: G1/G2 measured 174.2 s wall at peak working set 92.2 MB
under a 512 MB ceiling. G3 is 28 windows and G4 is six windows at
three ranges including 300000; ~3 min more, same footprint. Run under
memwatch at the 512 MB default. Stages select with a command-line
argument (g1, g3, g4) so a re-run need not repeat a printed stage.

RUN RECORD
----------
Four runs, one per stage, all under memwatch at the 512 MB default:
G1/G2 174.2 s at peak working set 92.2 MB; G3 191.3 s at 90.7 MB;
G4 57.8 s at 243.1 MB; G5 224.8 s at 242.8 MB; G6 86.9 s at
244.7 MB. Controls: G1's eight
A = B rows print G b . G b . at 8 of 8, the designed family's own law
read through this rig's imported classifier; Q7 green, every window
G3 and G4 print carrying usable depth t <= 10, the instrument's own
cap, at caps up to A = 16 -- and that transfers to the stages that
do not print it, since a SMALLER cap makes q grow slower and the
depth larger, so no window here can sit under the A = 16 rows; and
the parent rig's three second-cell movers reproduce exactly.
THE SLATE MOVED TWICE AND BOTH TIMES A PRINT FORCED IT, never a
result being unwelcome: G3's roof pair was frozen after G1 printed a
roof at one row and could not have been written before it, and G5's
corrected law was frozen after G4 printed a control failure. Each
addition is marked above with what it was allowed to read.

FINDINGS (each at its own tier)
-------------------------------
H1  THE TWO-RANGE VERDICT IS NOT THE WINDOW'S VERDICT AT THIS CELL,
    AND THE PARENT RIG'S VALUE LAW WAS READ OFF ONE (Q8's kill fires,
    on a CONTROL). (5, 4) reads bounded at 30000 and at 100000 --
    c_min 0 0 0 5 4 3 2 1 0 0, byte-identical across the two, which
    is the stability the classifier calls authoritative -- and GATED
    at 300000, where the same column opens to 0 0 0 > 10 9 8 7 6 5.
    Six of the 24 cells read bounded at two ranges flip: (5, 4),
    (6, 3), (6, 4), (7, 3), (7, 4), (8, 9). Every flip is witness
    GROWTH and not a ceiling artifact -- A_top rises 8 -> 14, 10 ->
    14, 7 -> 11 across the three ranges at the cells G4 printed in
    full -- so the deeper table is finding a deeper witness, not
    re-reading the same one. The direction is one-way, which is what
    makes the re-read affordable: the classifier reads growth and
    saturation at the DEEPEST range, so a deeper range can only turn
    a cell GATED, and the gated cells need no second look.
    (Settled later, explore_cascade_second.py H1: one-way holds in the
    range CEILING, which is the direction argued here and the only one
    this rig varies. The range FLOOR is a second axis, and lowering it
    gates BY CONSTRUCTION -- so what survives is the affordability
    argument at a FIXED floor, and the bounded set every finding below
    reports is an upper bound on the bounded set rather than a
    measurement of it. No cell printed here is superseded.)
    WHAT THE INSTRUMENT MISSES, exactly. The classifier downgrades a
    stable column to bounded when it RETURNS to 0 above its own
    nonzeros, on the ground that a single deep witness declines by 1
    per depth and never comes back. A witness whose decline BOTTOMS
    OUT inside the table satisfies that test while being one witness
    -- 0 0 0 5 4 3 2 1 0 0 is a decline of exactly 1 per depth that
    ran out of table, and it is indistinguishable at two ranges from
    the local bump 0 0 0 0 1 0 0 0 0 0 that the same cell prints at
    r = 2 and holds at all three ranges. The guard is not wrong; it
    is under-ranged, and the graded family's half-period cell is
    where that bites because its witnesses are the deepest here.
    THE SHAPE IS NOT A PREDICTOR, ONLY HOW THE EXPOSURE WAS SEEN
    (explore_cascade_roof.py H4): four statistics of the two-range
    column fail to separate the two-class family's movers from its
    holders, whose declines run LONGER than the movers'. So the
    re-read stays a sweep over EVERY bounded cell and cannot be
    narrowed to the columns that look like this one.
H2  REPRODUCED UNDER A SECOND CLASSIFIER: all 92 cells at zero misses
    under the run-length rule, which reads one table at the data's own
    depth and takes no range set at all (explore_cascade_rule.py H2).
    Both sharp clauses survive intact. The law is not an artifact of
    the instrument that found it.
    THE VALUE LAW IS A GAP INTERVAL WITH A ROOF AT 2B + 1, AND THE
    ROOF IS THE ABSORPTION LEMMA'S OWN BOUNDARY (rule at scanned
    scope; Q2, Q6's ratio reading, and Q10 all die, ROOF-DOUBLE
    lands 4 of 4). At the half-period stride r = 3 of
    [1, 1, A, 1, 1, B]^inf the cell reads bounded only when
        B < A <= 2B + 1     and     A * B >= 30,
    and GATED at every other off-diagonal pair, with A = B reading
    delay-0. Every measured cell obeys it, at zero misses: the 64
    grid cells at 2..9 and the four roof rows B = 3..6 with A to 16,
    of which 35 distinct cells were read at THREE ranges (G4's six,
    G5's 24 and G6's nine, overlapping in four) and the rest are
    gated cells standing on H5. The three clauses are separately
    witnessed. The ROOF is
    the sharp one -- each row with a bounded run turns GATED at
    exactly A = 2B + 2 and stays gated: first gated A = 10, 12, 14 at
    B = 4, 5, 6, which ROOF-DOUBLE calls at 3 of 3 and ROOF-RATIO
    (A < 8B/3) misses at 3 of 3, predicting 11, 14, 16. THREE rows
    and not the four G3 printed: G3 read its runs at two ranges, and
    B = 3's run of two cells is exactly what G5 flipped, so that row
    is EMPTY at three ranges and carries no roof datum at all. It
    cost the roof nothing to lose, since ratio and double both
    predicted 8 there and the row never separated them. And
    2B + 1 >= A is 2B >= A - 1, which is the
    ABSORPTION LEMMA's condition 2c = a - 1 one storey down
    (explore_odd_a_freeze.py: a top charge c absorbs a comb extension
    a top-locally iff 2c = a - 1) read as an inequality, with the
    absorber's cap B standing where the lemma has c and the
    overflowing cap A where it has a. That is a coincidence of the
    boundary at three rows and a mechanism reading, NOT a derivation,
    and the mapping is where it is loosest: the lemma's c is a top
    CHARGE and B here is a CAP, the lemma is an equality about a
    comb extension and this an inequality about a shift's drop.
    A weld would still have to explain why a cap may stand in for a
    charge, and it is not owed by the leg that followed: that leg
    asked whether the roof LIFTS off the period and found it does not,
    the verdict at a window with no period being a function of neither
    the drop's position nor its cap pair (explore_cascade_roof.py H2).
    The roof's scope is this family, and the coincidence stands
    unexplained rather than pending.
H3  THE PRODUCT CLAUSE IS THE min = 2 WALL, GENERALIZED -- AND ITS
    THRESHOLD IS PINNED BY TWO CELLS (observation; Q3 green at 14 of
    14). The parent rig's "min(A, B) = 2 gates in both orders" is
    two different clauses wearing one name, and only one of them is
    the product. Where A = 2 the FLOOR does it: B < A fails at every
    B >= 2, so that whole row gates for the same reason every A < B
    cell does, and the value 2 is incidental. Where B = 2 the PRODUCT
    does it: the roof caps A at 2B + 1 = 5, so the largest product
    that column can reach is 10 and no cell in it can clear 30 --
    measured, at every A to 9. The clause is not a min, and B = 3 is
    what shows it: that column's roof is 7 and its largest product
    21, so it is EMPTY too, where a min >= 3 reading predicts bounded
    cells in it and the parent rig reported two ((6, 3) and (7, 3),
    both flipped by H1). The threshold sits in (28, 30], and the two
    cells that pin it are the extremes rather than neighbours: (7, 4)
    at 28 is the largest product among the gated cells that satisfy
    floor and roof, and (6, 5) at exactly 30 is the smallest among
    the bounded. SAID PLAINLY: any monotone reparametrization
    of the product fits identically, and the clause only BITES at
    B <= 4 -- at B >= 5 the floor cell (B + 1) * B already clears 30
    -- so its evidence is the B = 4 row's step from gated at A = 7 to
    bounded at A = 8, plus two empty rows. It is the weakest of the
    three clauses and the one a new row cannot strengthen.
H4  THE SECOND CELL IS NOT A SMALL-VALUE FACT (Q5's kill fires).
    ** SUPERSEDED IN FULL: there is no second cell. Every verdict in
    this finding is the retired classifier's, and under the
    run-length rule all 25 swept pairs print the parity law with
    r = P the only departure -- the r = 5 movers, the r = 2 movers
    and the region above the grid alike (explore_cascade_rule.py H1
    for the region, explore_cascade_scale.py H3 for the pairs). What
    survives is the r = 3 VALUE LAW this rig established, reproduced
    at zero misses under a classifier with a fixed point. ** The
    parent rig's three movers reproduce exactly -- (4, 8) and (4, 9)
    gate r = 5, (8, 5) gates r = 2 -- and they are three of six in
    the 8x8 grid alone, two of which ((8, 6), (9, 6)) have
    min(A, B) >= 6, which is Q5's named kill. THE SIX IS A LOWER
    BOUND AND NOT A COUNT, for the reason H1 gives about r = 3: a
    NON-mover is a cell whose r = 2 and r = 5 both read bounded, and
    bounded is exactly the verdict a third range can gate, so the 40
    grid cells never re-read could hold movers this count misses.
    What is measured: every mover among the 35 cells read at three
    ranges held, and no new one appeared among them. Above the grid
    it is
    not an edge at all: whole rows move r = 2 -- from A = 8 at
    B = 6 and from A = 14 at B = 4, both unbroken to A = 16, and at
    B = 5 from A = 8 with ONE interruption, A = 10 reading bounded
    between gated 8, 9 and gated 11..16. B = 3 never moves it. So a
    second stride turns gated over a region rather than at scattered
    pairs, and the region is not an interval in A -- so it is a
    surface with
    its own law and not a spillover from r = 3, and reading it is the
    next leg. r = 6, the graded window's true period, reads delay-0
    at every window measured here, and r = 1 and
    r = 4 gate at every one: the parity law survives untouched at the
    four strides that are not the half-period and not its partner.
H5  THE ONE-WAY DIRECTION IS MEASURED AND NOT ONLY ARGUED
    (observation, 9 cells; G6's kill misses). H1's argument -- a
    deeper range can only turn a cell GATED, so the gated cells need
    no re-read -- has a hole the argument does not close: when the
    columns differ across ranges WITHOUT the top-depth witness
    growing, the classifier falls through to the deepest table's
    single-range verdict, and nothing makes that verdict monotone.
    Nine two-range GATED cells, one or two on each side of each
    clause's boundary -- (10, 4), (12, 5), (14, 6) just above the
    roof; (4, 3), (5, 3) inside it with the product short; (9, 2),
    (5, 2) on the product clause at B = 2; (4, 8), (6, 7) on the
    A < B side -- all nine hold GATED at 300000, and H2 calls all
    nine. So the two-range gated cells of G1 and G3 stand, and the
    audit's cost stays four minutes rather than an hour. This is
    evidence for the direction at the boundaries, not a proof of
    monotonicity: a cell far from any boundary was not probed,
    because a flip there would break H2 as loudly.

SETTLED LATER (explore_limit_column.py L3): the law above is a
    reading at the ranges scanned and not a fact about the windows. The
    limit column at every cell with A != B is INFINITE at r = 3 -- at
    (8, 4) the integers 1638 and 364170 agree on 10 digits with images
    differing at position 3, the pair sitting just past N = 300000, and
    the next witnesses agree on 16 and 22 -- so the roof, the floor and
    the product threshold locate the FIRST witness against the range
    read and nothing else. The diagonal A = B reads the zero column.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_cascade_span import (          # noqa: E402
    RANGES,
    RANGES3,
    cell_rows,
    graded,
    ranged,
    verdict_vector,
)

VALUES = range(2, 10)
R_MAX = 6
F4_VECTOR = "Gb.Gb."


def standing_law(A, B):
    """Q2: the parent rig's table, as a predicted r = 3 verdict."""
    if A == B:
        return "."
    if min(A, B) >= 3 and A - B >= 3:
        return "b"
    return "G"


def g1_grid():
    print("=" * 78)
    print("G1 THE FULL (A, B) GRID AT P = 3 -- [1, 1, A, 1, 1, B]^inf")
    print("   strides r = 1..6; F4's parity of r mod 3 is G b . G b .")
    print("   the diagonal A = B IS the designed family and must print it")
    print()
    vectors = {}
    void = False
    for A in VALUES:
        for B in VALUES:
            v = "".join(verdict_vector(graded(6, {2: A, 5: B}), R_MAX))
            vectors[(A, B)] = v
            if A == B and v != F4_VECTOR:
                print(f"  !! CONTROL FAILS at A = B = {A}: {v} "
                      f"(expected {F4_VECTOR}) -- THE GRID IS VOID")
                void = True
    print(f"  Q1 control: {'RED, grid void' if void else 'green'} "
          f"-- {sum(1 for A in VALUES if vectors[(A, A)] == F4_VECTOR)}"
          f"/8 diagonal rows print {F4_VECTOR}")
    print()
    print("-- the r = 3 cell (rows A, columns B; * = diagonal) --")
    print("      B = " + "  ".join(f"{B}" for B in VALUES))
    for A in VALUES:
        cells = []
        for B in VALUES:
            c = vectors[(A, B)][2]
            cells.append(f"{c}*" if A == B else f"{c} ")
        print(f"  A = {A}  " + " ".join(cells))
    print()
    miss = []
    for A in VALUES:
        for B in VALUES:
            got, want = vectors[(A, B)][2], standing_law(A, B)
            if got != want:
                miss.append((A, B, want, got))
    print(f"  Q2 the standing law at r = 3: {len(miss)} misses of 64")
    for A, B, want, got in miss:
        print(f"      A={A} B={B}: predicted {want}, measured {got}")
    print()
    wall = [(A, B, vectors[(A, B)][2]) for A in VALUES for B in VALUES
            if (A == 2 or B == 2) and A != B and vectors[(A, B)][2] != "G"]
    print(f"  Q3 the min = 2 wall: {len(wall)} of the 14 off-diagonal "
          f"cells with a 2 in them are NOT gated at r = 3")
    for A, B, c in wall:
        print(f"      A={A} B={B}: {c}")
    print(f"  Q4 the fork at (9, 6): r = 3 reads "
          f"{vectors[(9, 6)][2]} -- "
          f"{'FLOOR ONLY' if vectors[(9, 6)][2] == 'b' else 'FLOOR + ROOF'}")
    print()
    print("-- the threshold per row: smallest A turning r = 3 bounded --")
    for B in VALUES:
        firsts = [A for A in VALUES if A != B and vectors[(A, B)][2] == "b"]
        if firsts:
            gaps = sorted(set(A - B for A in firsts))
            print(f"      B = {B}: first bounded A = {min(firsts)}"
                  f"  (gap {min(firsts) - B}), all bounded A = {firsts}"
                  f", gaps {gaps}")
        else:
            print(f"      B = {B}: no bounded cell in the row")
    return vectors


def g2_second_cell(vectors):
    print()
    print("=" * 78)
    print("G2 THE SECOND CELL -- where a vector differs from G b . G b . "
          "away from r = 3")
    movers = []
    for A in VALUES:
        for B in VALUES:
            v = vectors[(A, B)]
            other = [r + 1 for r in range(R_MAX)
                     if r != 2 and v[r] != F4_VECTOR[r]]
            if other:
                movers.append((A, B, v, other))
    print(f"  {len(movers)} of 64 pairs move a cell other than r = 3")
    for A, B, v, other in movers:
        print(f"      A={A} B={B}: {' '.join(v)}   strides moved "
              f"{other}  min {min(A, B)}")
    big = [(A, B) for A, B, v, o in movers if min(A, B) >= 6]
    print(f"  Q5: known movers (4,8) r=5, (4,9) r=5, (8,5) r=2 -- "
          f"reproduced: "
          f"{[(A, B, o) for A, B, v, o in movers
              if (A, B) in {(4, 8), (4, 9), (8, 5)}]}")
    print(f"  Q5: second-cell movers with min(A, B) >= 6: {big}")


ROOF_ROWS = (3, 4, 5, 6)
ROOF_A = range(4, 17)


def g3_roof():
    print()
    print("=" * 78)
    print("G3 THE ROOF -- rows B = 3, 4, 5, 6 with A run to 16")
    print("   ROOF-RATIO  bounded needs A <  (8/3) B  -> first gated A "
          "= 8, 11, 14, 16")
    print("   ROOF-DOUBLE bounded needs A <= 2B + 1   -> first gated A "
          "= 8, 10, 12, 14")
    for B in ROOF_ROWS:
        cells = []
        for A in ROOF_A:
            if A == B:
                continue
            a = graded(6, {2: A, 5: B})
            # usable depth at the top range, printed rather than assumed
            row = cell_rows("", a, RANGES[-1], rmax=3, show=False)
            tmax = row[3]["tmax"]
            v = "".join(verdict_vector(a, R_MAX))
            cells.append((A, v[2], tmax, v))
        print(f"  B = {B}:")
        for A, c, tmax, v in cells:
            print(f"      A = {A:2d}: r3 {c}  t<= {tmax:2d}  vector "
                  f"{' '.join(v)}")
        bounded = [A for A, c, _, _ in cells if c == "b"]
        gated_above = [A for A, c, _, _ in cells
                       if c == "G" and bounded and A > min(bounded)]
        interval = (not bounded or
                    bounded == list(range(min(bounded), max(bounded) + 1)))
        first_gated = min(gated_above) if gated_above else None
        print(f"      bounded A = {bounded}, first gated above the run = "
              f"{first_gated}, run is an interval: {interval}")
        pr = {3: 8, 4: 11, 5: 14, 6: 16}[B]
        pd = {3: 8, 4: 10, 5: 12, 6: 14}[B]
        print(f"      ratio predicts first gated {pr}"
              f"{'  <<< MISS' if first_gated != pr else ''}"
              f" | double predicts {pd}"
              f"{'  <<< MISS' if first_gated != pd else ''}")
        thin = [A for A, _, tmax, _ in cells if tmax < 4]
        if thin:
            print(f"      !! usable depth below 4 at A = {thin} "
                  f"-- Q7 KILL, those rows are instrument limit")


def g4_anomalies():
    print()
    print("=" * 78)
    print(f"G4 THE ANOMALIES AT THREE RANGES {RANGES3}")
    print("   (8,3) and (9,3) gate above a bounded run; (8,9) is the only "
          "A < B bounded cell.")
    print("   Controls beside them: (7,3) and (5,4) bounded, (5,3) gated.")
    for A, B, note in ((8, 3, "anomaly: gated above the run"),
                       (9, 3, "anomaly: gated above the run"),
                       (8, 9, "anomaly: the only A < B bounded cell"),
                       (7, 3, "control: bounded"),
                       (5, 4, "control: bounded"),
                       (5, 3, "control: gated")):
        print()
        ranged(f"V A={A} B={B}  [{note}]", graded(6, {2: A, 5: B}),
               R_MAX, ranges=RANGES3)


# The cells G1 and G3 PRINTED as bounded at r = 3 -- the input set for
# the three-range re-read, copied from those runs rather than recomputed.
TWO_RANGE_BOUNDED = (
    (5, 4), (6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (7, 6),
    (8, 4), (8, 5), (8, 6), (8, 7), (8, 9), (9, 4), (9, 5), (9, 6),
    (9, 7), (9, 8), (10, 5), (11, 5), (10, 6), (11, 6), (12, 6), (13, 6),
)


def corrected_law(A, B):
    """Q10: bounded iff B >= 3 and 3 <= A - B <= B + 1."""
    return "b" if B >= 3 and 3 <= A - B <= B + 1 else "G"


def g5_deep():
    print()
    print("=" * 78)
    print(f"G5 THE BOUNDED CELLS AT THREE RANGES {RANGES3}")
    print("   Q10: bounded iff B >= 3 and 3 <= A - B <= B + 1")
    flips = []
    miss = []
    for A, B in TWO_RANGE_BOUNDED:
        v = "".join(verdict_vector(graded(6, {2: A, 5: B}), R_MAX,
                                   ranges=RANGES3))
        got, want = v[2], corrected_law(A, B)
        if got != "b":
            flips.append((A, B, got))
        if got != want:
            miss.append((A, B, want, got))
        print(f"  A={A:2d} B={B}: gap {A - B:2d}  {' '.join(v)}"
              f"   r3 two-range b -> three-range {got}"
              f"   Q10 predicts {want}"
              f"{'   <<< MISS' if got != want else ''}")
    print(f"  Q9: {len(flips)} of {len(TWO_RANGE_BOUNDED)} bounded cells "
          f"flipped under the deeper range: "
          f"{[(A, B) for A, B, _ in flips]}")
    print(f"  Q10: {len(miss)} misses of {len(TWO_RANGE_BOUNDED)}")
    for A, B, want, got in miss:
        print(f"      A={A} B={B}: predicted {want}, measured {got}")


def final_law(A, B):
    """H2: bounded iff B < A <= 2B + 1 and A * B >= 30."""
    if A == B:
        return "."
    return "b" if B < A <= 2 * B + 1 and A * B >= 30 else "G"


# Cells that read GATED at two ranges, one on each side of each clause's
# boundary -- the test set for the one-way claim, which H1 argues rather
# than measures. Every one of them is predicted GATED by H2.
ONE_WAY_PROBE = (
    (10, 4), (12, 5), (14, 6),        # just above the roof 2B + 1
    (4, 3), (5, 3),                   # inside the roof, product too small
    (9, 2), (5, 2),                   # the product clause at B = 2
    (4, 8), (6, 7),                   # the A < B side
)


def g6_one_way():
    print()
    print("=" * 78)
    print(f"G6 THE ONE-WAY CLAIM AT THREE RANGES {RANGES3}")
    print("   H1 argues that a deeper range can only turn a cell GATED, "
          "which is what")
    print("   lets G5 re-read the bounded cells alone. The argument has a "
          "hole: when the")
    print("   columns DIFFER across ranges without the top-depth witness "
          "growing, the")
    print("   classifier falls through to the deepest table's SINGLE-range "
          "verdict, and")
    print("   nothing above proves that verdict is monotone. So the "
          "two-range GATED cells")
    print("   at every clause boundary are re-read here. KILL: any of them "
          "reading bounded")
    print("   -- the G1 and G3 gated cells would then all be unaudited too, "
          "and H2 with them.")
    bad = []
    for A, B in ONE_WAY_PROBE:
        v = "".join(verdict_vector(graded(6, {2: A, 5: B}), R_MAX,
                                   ranges=RANGES3))
        got, want = v[2], final_law(A, B)
        if got != "G":
            bad.append((A, B, got))
        print(f"  A={A:2d} B={B}: gap {A - B:2d} product {A * B:3d}  "
              f"{' '.join(v)}   r3 two-range G -> three-range {got}"
              f"   H2 predicts {want}"
              f"{'   <<< MISS' if got != want else ''}")
    print(f"  one-way claim: {len(bad)} of {len(ONE_WAY_PROBE)} gated "
          f"cells flipped to bounded under the deeper range -- "
          f"{'HOLDS' if not bad else 'REFUTED: ' + str(bad)}")


STAGES = {"g1": None, "g2": None, "g3": g3_roof, "g4": g4_anomalies,
          "g5": g5_deep, "g6": g6_one_way}

if __name__ == "__main__":
    want = [s for s in sys.argv[1:] if s in STAGES] or list(STAGES)
    if "g1" in want or "g2" in want:
        vectors = g1_grid()
        if "g2" in want:
            g2_second_cell(vectors)
    if "g3" in want:
        g3_roof()
    if "g4" in want:
        g4_anomalies()
    if "g5" in want:
        g5_deep()
    if "g6" in want:
        g6_one_way()
