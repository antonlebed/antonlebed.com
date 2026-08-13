"""The roof at the windows with no period, and the targets it is scored
against, re-read at a third range.

THE QUESTION
------------
At the graded window [1, 1, A, 1, 1, B]^inf the half-period stride r = 3
carries a LARGE-ONTO-LARGE drop -- an overflowing cap A landing on a
position whose own cap B must absorb it -- and its verdict is the value
law (explore_cascade_values.py H2): bounded iff B < A <= 2B + 1 and
A * B >= 30. Both clauses are criteria on ONE DROP, because that family
has one cap pair and repeats it forever.

The windows with no period have many. The cubic cbrt(2) - 1 carries eight
distinct cap values among its first fourteen large positions, so a stride
there has a whole MULTISET of cap pairs at its drop sites, and the law
reads a verdict per site. What is open is the QUANTIFIER over them --
the thread's founding question ("what plays the period at a window that
has none") reduced to a scoring exercise. This rig scores it, at the
cubic and at e - 2.

It cannot be scored against the split on record. The cubic's split
(gated 1, 3, 5; bounded 2, 4, 6, 7, 8) and e - 2's (gated 1, 4, 7) were
both measured at TWO ranges, and a two-range BOUNDED verdict at this
family is exactly what a third range was found to overturn -- six of 24
such cells flipped at 300000 (explore_cascade_values.py H1), the error
one-way, so bounded cells are the suspect ones and gated cells are not.
Nine cells are therefore owed a third range before any criterion is
scored against them, and the same debt is owed by the two-class family
whose 84 cells explore_cascade_span.py F6 reports at two ranges.
(Settled later, explore_cascade_second.py H1: the one-way direction is
the range CEILING, which is the direction this rig deepens along and
the one its debt is paid in. Lowering the range FLOOR gates by
construction, so every BOUNDED verdict scored below -- the cubic's
five, e - 2's three, the two-class family's -- is an upper-bound
reading at a fixed floor. No verdict printed here is superseded.)

DO NOT IMPORT THE CONSTANT. The threshold 30 was calibrated on ONE
family at P = 3 and nothing measured says it is universal rather than
that family's own number. The cubic's pairs are much larger -- 14 onto
10 among them -- so a product rule carried over unchanged could score
every site alike and look like a fit or a total miss for the same
reason. The ROOF is dimensionless in the caps and is carried over as it
stands; the PRODUCT is carried over with its threshold left FREE, and
the observable is whether ANY threshold separates, never whether 30
does.

THE HAND-ATTACK (pre-engine, on paper -- the drop-site cap pairs are
read off the quotient sequence alone, which no verdict enters)
--------------------------------------------------------------------
A drop site at stride r is a position j with a[j] > a[j+r]: the cap a[j]
overflows onto the cap a[j+r]. Writing the pairs out at the LANDING
bound (both j and j + r within the built table at N = 300000, K = 12 at
the cubic and 15 at e - 2) -- the conservative choice, and not the
natural one: a digit at a readable position shifts to a position above
K(N) and is still represented, so this table UNDER-counts and the run
scores the SOURCE bound j <= K(N) beside it:

  CUBIC  a = 3 1 5 1 1 4 1 1 8 1 14 1 10 2 1 4 12 2 3 2 ...
    r 1  (3,1) (5,1) (4,1) (8,1) (14,1)
    r 2  (5,1) (4,1) (14,10)
    r 3  (3,1) (5,4) (8,1)
    r 4  (3,1) (5,1) (4,1)
    r 5  (5,1)
    r 6  (3,1) (4,1)
    r 7  (3,1) (5,1)
    r 8  --
  E - 2  a = 1 2 1 1 4 1 1 6 1 1 8 1 1 10 1 1 12 1 1 14 ...
    r 1  (2,1) (4,1) (6,1) (8,1) (10,1)
    r 2  (2,1) (4,1) (6,1) (8,1) (10,1)
    r 3  --
    r 4  (2,1) (4,1) (6,1) (8,1)
    r 5  (2,1) (4,1) (6,1) (8,1)
    r 6  --
    r 7  (2,1) (4,1) (6,1)
    r 8  (2,1) (4,1) (6,1)

E - 2 IS THE WITNESS AND IT NEEDS NO QUANTIFIER AND NO COUNT. Its
quotient pattern 1, 1, 2n puts a cap of 1 under every overflow at every
stride, so its drop sites are the even caps dropping onto 1 and nothing
else -- and the strides PAIR UP with IDENTICAL multisets: r = 1 with
r = 2, r = 4 with r = 5, r = 7 with r = 8, position for position in
value if not in place. On the split on record the first member of each
pair is GATED and the second is BOUNDED. Any criterion that is a
FUNCTION of the drop-site cap multiset -- the roof under any quantifier,
the product under any threshold, any statistic whatever over the pairs
-- must give both members of a pair the same verdict. So the whole class
dies at one witness if the split survives the third range, exactly as
gap parity died at the cubic, and by a cleaner witness: not "both
parities appear among the sites" but "identical data, opposite
verdicts".

WHICH IS WHY THE RE-READ COMES FIRST AND CAN DISSOLVE THE WITNESS. The
second member of every one of those pairs is a BOUNDED verdict at two
ranges -- r = 2, 5, 8 -- and that is the direction H1 found unsafe. If
all three gate at 300000 the pairs agree, the witness is gone, and e - 2
says nothing about the class either way.

AND THE CUBIC IS ALREADY SCORED ON PAPER against the split on record,
which is why the run's job is the split and not the score. Counting
sites that satisfy the roof A <= 2B + 1 at the readable positions: r = 1
has 1 of 5, r = 2 has 1 of 3, r = 3 has 2 of 3, r = 4 has 1 of 3, r = 5
has 0 of 1, r = 6 has 1 of 2, r = 7 has 1 of 2, r = 8 has none. Against
gated 1, 3, 5 and bounded 2, 4, 6, 7, 8: EXISTENTIAL (some site
satisfies -> bounded) calls r = 1 and r = 3 bounded and misses both;
UNIVERSAL (all satisfy -> bounded) calls every stride gated and misses
all five bounded ones; a COUNT threshold cannot separate because the
count 1 sits at gated r = 1 and at bounded r = 2, 4, 6, 7; a FRACTION
threshold cannot either, gated occupying both ends (0 at r = 5 and 2/3
at r = 3, where the bounded strides run 0 to 1/2). If the split holds,
every form is already dead and the run confirms arithmetic. If it moves,
the score moves with it -- which is the whole reason the run exists.

THE INSTRUMENT'S OWN LIMIT, said before the run. At the cubic K(N) is 10
at 30000 and 12 at BOTH 100000 and 300000: the third range triples the
inputs and lengthens the table by nothing. Every cubic flip H1's
mechanism describes is a deeper WITNESS found among more inputs in a
table of the same length, and whether that can happen at all is an open
question about the instrument, not a prediction. It is printed per
window per range so a reader can see which of the two the cubic got.

PREDICTIONS, FIXED BEFORE THE RUN (as observables -- what the rig
PRINTS, never what it would mean)
  P1 (positive control, the parent's verdicts) read at the parent's two
      ranges the cubic gates at r = 1, 3, 5 and e - 2 at r = 1, 4, 7,
      explore_cascade_span.py F1's rows exactly. KILL: any
      disagreement -- the rig is then not reading what the parent read
      and nothing below it is looked at.
  P2 (positive control, the scoring code) the roof-and-product
      criterion, applied through the same site-extraction path used at
      the cubic, is run at six graded P = 3 windows whose r = 3 verdict
      is measured in this same run at three ranges -- (6, 5), (10, 6),
      (13, 6) bounded and (7, 4), (10, 4), (5, 2) gated under H2. Those
      windows have ONE cap pair repeated, so the quantifier is vacuous
      there and the criterion reduces to H2 itself. KILL: any miss of
      the six -- the extraction or the criterion is then wrong and every
      cubic score below is void.
  P3 (the re-read) the cubic's r = 2, 4, 6, 7, 8 and e - 2's r = 2, 5,
      8 -- every bounded stride of either window -- are re-read at
      RANGES3. The observable is the verdict per stride at three
      ranges, printed beside the c_min column at each. No direction is
      predicted beyond H5's one-way claim, under which none of the
      GATED strides can turn bounded. KILL of the one-way claim: a
      stride gated at two ranges reading bounded at three.
  P4 (the identical-multiset test) strides of one window are grouped by
      their drop-site cap multiset. The observable is whether any group
      holds two strides with DIFFERENT three-range verdicts. KILL OF
      THE WHOLE PER-DROP CLASS: one such group -- no function of the
      cap pairs can then be the law, whatever the quantifier.
  P5 (the quantifiers) the roof A <= 2B + 1 scored per site at every
      stride of both windows carrying drops, in four forms against the
      corrected split: EXISTENTIAL, UNIVERSAL, every COUNT threshold on
      the number of satisfying sites, and every FRACTION threshold.
      The observable is misses per form, and for the thresholded forms
      whether ANY threshold separates the split at all.
  P6 (the product with a free threshold) the same four forms with the
      site test A * B >= T, swept over every T realized among the
      drop-site products of the window. The observable is the set of T
      that separate, which may be empty. The constant 30 is scored as
      one T among them and carries no standing.
  P7 (the two-class family at three ranges) the eight P = 4..7 windows
      of explore_cascade_span.py F6, all 84 cells, re-read at RANGES3
      with the gap-parity disagreement recomputed. F6 reports 19
      disagreements at two ranges. The observable is how many cells
      flip and what the disagreement count becomes. KILL of F6's 19:
      any flip.
  P8 (the site window) every site set above is computed at THREE
      bounds: SOURCE (j <= K(N), the sites that can actually fire),
      LANDING (j + r <= K(N) too, which under-counts) and WIDE
      (explore_cascade_span.py's gap_parity bound, kn + EXTRA - r - 1,
      which reaches far past the built table and over-counts). The
      observable is whether any scored form's verdict
      depends on which bound is used. That dependence, if it appears,
      is a report about the criterion and not a choice to be made
      quietly.

THE DESIGN
----------
Windows, digit path, c_min rows and the VERDICT CLASSIFIER are imported
from explore_cascade_span.py -- not reimplemented, for the reason
explore_cascade_values.py gives: the classifier carries two guards added
because a control went red without them, and a fresh loop over the same
windows inherits neither. The ranges, the lookahead ceiling and the
stride cap are the parent's too, so every cell here is comparable to the
cells it corrects.

S0  THE CONTROLS. The cubic and e - 2 at the parent's two ranges,
    verdict per stride against F1's rows (P1); then the six graded
    P = 3 windows at three ranges, verdict at r = 3 beside the
    criterion's own call on their drop-site pairs (P2). Both run and
    both read before anything below.
S1  THE RE-READ. The cubic and e - 2 at RANGES3, every stride, c_min
    column per range and K(N) per range beside it. P3's and the
    instrument question's observable.
S2  THE SITE TABLE. Drop-site cap pairs per stride at both bounds, the
    multiset grouping, and the group verdicts from S1. P4's and P8's
    observable.
S3  THE SCORING. The roof and the free-threshold product in four
    quantifier forms against S1's corrected split, at both windows and
    both bounds. P5's and P6's observable.
S4  THE TWO-CLASS FAMILY. The eight F6 windows at RANGES3, per-cell
    verdict against the two-range record, and the gap-parity
    disagreement count recomputed. P7's observable.
S5  THE FLIP SIGNATURE. Whether a statistic of the two-range c_min
    column predicts which cells S4 moved. Its slate -- the third, and
    the only one this rig froze after a print -- sits on the stage
    itself, since it could not be written before S4 named the movers.

RESOURCE: S0 is 2 windows at two ranges plus 6 windows at three; S1 is
2 windows at three ranges over 8 strides; S4 is 8 windows at three
ranges over up to 12 strides. Comparable stages in the parent rigs ran
57.8 s at 243.1 MB (six windows, three ranges) and 224.8 s at 242.8 MB
(24 windows, three ranges), so the estimate is ~2 min for S0/S1, ~4 min
for S4, peak working set well under the 512 MB default. S2 and S3 are
quotient arithmetic and cost nothing. Run under memwatch. Stages select
with a command-line argument (s0, s1, s2, s3, s4, s5) so a re-run need not
repeat a printed stage; S2 and S3 need S1's split and recompute it if
run alone.

RUN RECORD
----------
Four runs, all under memwatch at the 512 MB default: S0 63.8 s at peak
working set 243.1 MB; S1/S2/S3 31.5 s at 237.4 MB; S4 167.5 s at
245.4 MB; S5 44.1 s at 92.4 MB. S2 and S3 were re-run once,
after review found the site bound mis-specified: the bound first called
readable demanded the LANDING sit inside the table, which under-counts
the sites that can fire. The natural SOURCE bound was added beside it
and all three are now scored. No verdict changes; the numbers sharpen.
Controls: P1 green, the cubic gating at
r = 1, 3, 5 and e - 2 at r = 1, 4, 7 at the parent's two ranges, F1's
rows exactly; P2 green at 6 of 6, the criterion calling three bounded
and three gated graded cells whose r = 3 verdict this run measured at
three ranges; and S4 reproducing F6's 19 gap-parity disagreements at two
ranges exactly, which controls the family path end to end. THE SLATE
MOVED ONCE AND A PRINT FORCED IT: S5's third slate was frozen after S4
printed its two movers and reads that list plus H1's stated shape,
nothing else.

FINDINGS (each at its own tier)
-------------------------------
H1  THE SPLIT HELD AT BOTH WINDOWS WITH NO PERIOD (rule at scanned
    scope; P3's re-read, zero movers of EIGHT).
    ** THE SPLIT IS STILL THE RETIRED CLASSIFIER'S, AND NO INSTRUMENT
    THE CORPUS TRUSTS HAS REPLACED IT. That classifier has no fixed
    point in the range SET (explore_cascade_rule.py H1) and none in
    the instrument CAP either (explore_cascade_scale.py H5). The
    run-length rule cannot re-read it: both windows are APERIODIC, so
    it refuses the cubic at 7 of 8 strides and e - 2 at 4 of 8, and
    the refusal is entitlement rather than a gap -- the only cheaper
    scale available at an aperiodic window breaks the value law at
    exactly its three bounded cells (explore_cascade_scale.py H4). So
    H1, and H2 and H3 which read off it, stand where they were and
    are owed a THIRD instrument, not a re-read. ** The cubic's r = 2, 4,
    6, 7, 8 and e - 2's r = 2, 5, 8 -- every bounded stride either
    window has, and the cells this line of work owed a third range -- all
    hold at 300000. Eight and not the nine the leg was aimed with: that
    list carried e - 2's r = 6, which prints ZERO repairs and is
    delay-0, so it can no more move than its r = 3, which the same list
    excluded for exactly that reason. So the cubic reads gated at
    r = 1, 3, 5 and bounded at
    2, 4, 6, 7, 8, and e - 2 gated at 1, 4, 7, bounded at 2, 5, 8,
    delay-0 at 3, 6, at THREE ranges. The one-way direction is measured
    again beside them: no gated stride turned bounded, and two of them
    deepened, the cubic's r = 1 and r = 5 both moving A_top 10 -> 12
    with r = 1's column opening to > > 10 9 8 7 6 5 4 3.
    THE CUBIC'S AUDIT IS THE WEAKER OF THE TWO AND THE REASON IS
    PRINTED. K(N) there is 10, 12, 12 across the three ranges: the
    third range triples the inputs and lengthens the table by NOTHING,
    so the cubic's five bounded verdicts are audited against inputs and
    not against depth. That the probe still reaches is what the two
    deepened gated strides show -- more inputs found deeper witnesses
    in a table of the same length -- and e - 2, where K did move
    13 -> 15, held too.
    WHAT THIS DISCHARGES. explore_cascade_span.py F3's kill of the span
    criterion takes its instances from the cubic's bounded strides and
    carries a settling note saying so; those strides stand, and the
    note is spent.
H2  NO FUNCTION OF THE DROP-SITE CAP PAIRS IS THE LAW AT A WINDOW WITH
    NO PERIOD, AND THE WITNESS NEEDS NO QUANTIFIER AND NO COUNT (P4's
    kill fires three times, at both site bounds). What dies is the
    LIFT; the value law itself is a statement about the graded family's
    half-period cell and is untouched here. At e - 2 the quotient
    pattern 1, 1, 2n puts a
    cap of 1 under every overflow, so the strides PAIR UP with
    identical drop-site cap multisets -- r = 1 with r = 2, r = 4 with
    r = 5, r = 7 with r = 8, the even caps 2, 4, 6, ... dropping onto 1
    -- and by H1 the first member of each pair is GATED and the second
    BOUNDED at three ranges. Any criterion that is a function of those
    pairs gives both members one verdict. So the roof does not lift to
    a window with no period under ANY quantifier, and neither does the
    product under any threshold, nor any statistic over the pairs
    whatever. IT IS THE MIRROR OF
    F4 AND COMPLETES IT. F4 killed the POSITIONS with the graded swap
    -- two windows with an identical large-cap set and different
    verdicts; this kills the VALUES with two strides of ONE window
    carrying an identical cap-pair multiset and different verdicts. The
    verdict is a function of neither half of what a drop site is.
    AND THE SCOPE IS WIDER THAN THE VALUES, WHICH IS WHAT NAMES WHAT
    SURVIVES. The paired strides share their drop POSITIONS too --
    j = 1, 4, 7, 10, 13 at every one of them, printed by S2 -- and
    differ only in where the drop LANDS, at j + r. So no function of
    the OVERFLOWING end of a drop can be the law, and only the
    absorbing end is left. That is where e - 2's verdict is in fact
    read: its large caps sit on one residue class mod 3, so by F2's
    derivation gap parity there IS the parity of r mod 3, and it calls
    all eight strides. The cubic has no such class and gap parity is
    dead at it (F2). Neither aperiodic window is readable by the
    criterion that reads the other.
    AND IT IS A MISS AND NOT A SILENCE, which the run and the paper
    argument agree on independently. A criterion with one output per
    multiset must be wrong at one member of each of the three pairs, so
    it misses at least 3 of e - 2's 6 scored strides -- and S3 printed
    exactly 3 for EVERY form at both bounds: roof existential, roof
    universal, product at 30 both ways. The floor the argument predicts
    is the number the rig measured.
H3  AND THE CUBIC SCORES IT INDEPENDENTLY, INCLUDING THE ONE FIT THAT
    SURVIVES (observation; P5 and P6). Against the corrected split the
    ROOF A <= 2B + 1 misses 2 of 7 strides existentially and 4 of 7
    universally at the natural bound (2 and 4 of 7 at the landing bound,
    3 and 5 of 8 at the wide one), and NO count or fraction threshold
    separates at any of the three. The product with its threshold free:
    none of the 16 products realized at the natural bound separates, and
    none of the 7 at the landing bound. At the WIDE bound alone three
    thresholds do --
    T = 10, 12, 14, each with a count threshold over 8 strides -- and
    it is a fit on three grounds, all measured rather than argued: it
    exists ONLY at the bound that counts drop sites OUTSIDE the built
    table and vanishes at the natural one, so P8's dependence fired and
    the criterion is reading data the verdict cannot see; it separates
    nothing at e - 2 at any of
    that window's 11 realized products; and its SIGN is backwards --
    more large-product sites reads GATED, where the value law one
    storey down has A * B >= 30 reading BOUNDED. Three free parameters
    over eight points is what it is.
H4  THE FLIP SIGNATURE IS NOT IN THE COLUMN, AND THE AUDIT STAYS A
    SWEEP (P9's kill; 33 bounded cells, 2 of them movers). H1 of
    explore_cascade_values.py describes the shape that flipped there --
    a witness declining by 1 per depth that bottoms out inside the
    table, 0 0 0 5 4 3 2 1 0 0 -- against the local bump that holds,
    and a reader takes that for a predictor, which would turn every
    third-range audit from a sweep into a filter. It is not one. Four
    statistics of the two-range column -- its maximum, its longest
    run falling by 1 per depth, its value at the deepest depth, and
    whether that value stands alone -- ALL overlap between the two
    cells that moved and the 31 that held. The movers refute the shape
    directly: both carry a bare nonzero at the deepest depth with zeros
    everywhere above (longest decline 1), the opposite of the specimen,
    while a held cell carries a full 3 2 1 ... 4 3 2 1 with a decline
    of 4, and another held cell has the movers' exact shape at value 1.
    So a bounded two-range verdict is suspect whatever its column looks
    like, and the cost of the guard cannot be argued down.
H5  THE TWO-CLASS FAMILY AT THREE RANGES: F6'S VERDICT STANDS AND ITS
    COUNT MOVES BY TWO (rule at scanned scope; P7's kill fires, small).
    ** AND IT STANDS UNDER THE RUN-LENGTH RULE TOO, at 16 rather than
    17, five cells moving and none of them either mover below
    (explore_cascade_scale.py H1). This family is the one finding
    here the rule can reach, being periodic. **
    All 84 cells of the eight P = 4..7 windows re-read at 300000. The
    two-range pass reproduces F6's 19 gap-parity disagreements exactly,
    which is what makes the comparison a measurement; two cells move
    under the third range, both bounded -> GATED, and both toward gap
    parity, so the disagreement count is 17 and not 19. F6's verdict --
    the position-only reading fails in the periodic families and not
    only at the cubic -- stands on the remaining 17. THE TWO MOVERS
    SHARE AN ADDRESS: both sit at r = 10, at (P = 6, caps 5@1/2@4) and
    (P = 7, caps 5@2/3), which are different periods and different
    offsets. One coincidence at two cells, named because it is the only
    structure the movers have and H4 says their columns have none.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_cascade_span import (          # noqa: E402
    CUBIC,
    E2MINUS,
    EXTRA,
    RANGES,
    RANGES3,
    cell_rows,
    gap_parity,
    graded,
    range_verdict,
)
from explore_shift_repair import (          # noqa: E402
    build_q,
    fmt_row,
    usable_depth,
)

R_MAX = 8
WINDOWS = (("cubic cbrt(2)-1", CUBIC), ("e - 2", E2MINUS))

# explore_cascade_span.py F1's rows, the verdicts this rig must reproduce
# at the parent's two ranges before anything below it is read.
PARENT_GATED = {"cubic cbrt(2)-1": (1, 3, 5), "e - 2": (1, 4, 7)}

# The graded P = 3 cells used as the scoring control: (A, B, H2's call).
# Their r = 3 verdict is MEASURED here at three ranges, not asserted --
# the pairs are listed with H2's call only so a mismatch is visible.
CONTROL_CELLS = ((6, 5, "b"), (10, 6, "b"), (13, 6, "b"),
                 (7, 4, "G"), (10, 4, "G"), (5, 2, "G"))

# explore_cascade_span.py E3's two-class family, verbatim: (P, c1, c2, A, B).
FAMILY = ((4, 1, 3, 5, 2), (4, 1, 3, 2, 5),
          (5, 1, 3, 5, 2), (5, 0, 2, 4, 2),
          (6, 1, 4, 5, 2), (6, 0, 3, 5, 2),
          (7, 1, 4, 5, 2), (7, 2, 3, 5, 2))


# ------------------------------------------------------- the site table

def drop_sites(a, r, jmax):
    """The (overflowing cap, absorbing cap) pair at every drop site."""
    return tuple((a[j], a[j + r]) for j in range(jmax)
                 if j + r < len(a) and a[j] > a[j + r])


SITE_BOUNDS = ("source", "landing", "wide")


def bounds(a, r, n_top):
    """The three site windows, and the middle one is the natural one.

    SOURCE keeps every drop whose source digit exists in the data, j <=
    K(N) -- the sites that can actually fire. LANDING is the strictly
    conservative variant that also demands the landing j + r be inside
    the original table, so it UNDER-counts: a digit at a readable
    position shifts to a position above K(N) and is still represented,
    the weights being built to K(N) + EXTRA. WIDE is
    explore_cascade_span.py gap_parity's own bound, which reaches far
    past the built table and so OVER-counts.
    """
    kn = usable_depth(build_q(a, n_top), n_top)
    return {"source": kn + 1,
            "landing": max(0, kn - r + 1),
            "wide": kn + EXTRA - r - 1}


# ---------------------------------------------------------- the engine

def vector3(a, rmax, ranges=RANGES3):
    """Verdict and c_min rows per stride at each range."""
    rows = [cell_rows("", a, n, rmax=rmax, show=False) for n in ranges]
    out = {}
    for r in sorted(rows[0]):
        out[r] = (range_verdict([row[r] for row in rows]),
                  [row[r] for row in rows])
    return out


def show_window(name, a, ranges):
    print(f"  {name}   quotients {a[:16]}")
    for n in ranges:
        print(f"      K(N) at N = {n:6d}: "
              f"{usable_depth(build_q(a, n), n)}")
    res = vector3(a, R_MAX, ranges=ranges)
    for r in sorted(res):
        v, rows = res[r]
        print(f"    r {r}: {v:8s}  repairs {rows[-1]['repairs']:6d}")
        for n, row in zip(ranges, rows):
            print(f"        N {n:6d}: c_min " + fmt_row(row["A"], row["tmax"])
                  + f"  CAP {row['cap']:2d}  A_top {row['A'][row['tmax']]:2d}")
    return {r: res[r][0] for r in res}


# ------------------------------------------------------------------ S0

def s0_controls():
    print("=" * 78)
    print(f"S0 CONTROLS.  P1: the parent's verdicts at {RANGES}")
    print("   explore_cascade_span.py F1: cubic gated at r = 1, 3, 5; "
          "e - 2 at r = 1, 4, 7")
    dead = False
    for name, a in WINDOWS:
        res = vector3(a, R_MAX, ranges=RANGES)
        got = tuple(r for r in sorted(res) if res[r][0] == "GATED")
        ok = got == PARENT_GATED[name]
        dead |= not ok
        print(f"  {name:16s} gated at {got}  expected "
              f"{PARENT_GATED[name]}  {'green' if ok else '<<< P1 KILL'}")
        print("      vector " + " ".join(
            {"GATED": "G", "bounded": "b", "delay-0": "."}[res[r][0]]
            for r in sorted(res)))
    if dead:
        print("  !! P1 KILL -- the rig is not reading what the parent read; "
              "nothing below is read.")
        return False
    print()
    print(f"  P2: the scoring code at six graded P = 3 cells, {RANGES3}")
    print("   one cap pair repeated, so the quantifier is vacuous and the "
          "criterion reduces to H2")
    miss = 0
    for A, B, call in CONTROL_CELLS:
        a = graded(6, {2: A, 5: B})
        res = vector3(a, 6, ranges=RANGES3)
        v = {"GATED": "G", "bounded": "b", "delay-0": "."}[res[3][0]]
        jm = bounds(a, 3, RANGES3[-1])["source"]
        sites = drop_sites(a, 3, jm)
        crit = criterion_call(sites, roof=True, product=30)
        bad = (v != call) or (crit != v)
        miss += bad
        print(f"    A={A:2d} B={B}: measured r3 {v}  H2 says {call}  "
              f"sites {sites}  criterion {crit}"
              f"{'   <<< P2 MISS' if bad else ''}")
    print(f"  P2: {miss} misses of {len(CONTROL_CELLS)}"
          + ("" if not miss else "  <<< P2 KILL, the cubic scores are void"))
    return not miss


def criterion_call(sites, roof=True, product=None):
    """H2 read at a site multiset under the UNIVERSAL quantifier.

    With one repeated pair this IS H2; it is the control's reduction and
    not a claim about many pairs.
    """
    if not sites:
        return "."
    for A, B in sites:
        if roof and not (B < A <= 2 * B + 1):
            return "G"
        if product is not None and A * B < product:
            return "G"
    return "b"


# ------------------------------------------------------------------ S1

def s1_reread():
    print()
    print("=" * 78)
    print(f"S1 THE RE-READ AT THREE RANGES {RANGES3}")
    print("   Every bounded stride of either window is a two-range verdict "
          "and H1's exposure")
    print("   applies to it; the gated ones stand on H5 and are printed "
          "beside them.")
    split = {}
    for name, a in WINDOWS:
        print()
        split[name] = show_window(name, a, RANGES3)
    print()
    for name, a in WINDOWS:
        two = vector3(a, R_MAX, ranges=RANGES)
        moved = [r for r in sorted(split[name])
                 if two[r][0] != split[name][r]]
        print(f"  {name:16s} strides that MOVED under the third range: "
              f"{[(r, two[r][0], split[name][r]) for r in moved]}")
        bad = [r for r in moved if two[r][0] == "GATED"]
        if bad:
            print(f"      !! one-way claim REFUTED at r = {bad}")
    return split


# ------------------------------------------------------------------ S2

def s2_sites(split):
    print()
    print("=" * 78)
    print("S2 THE DROP-SITE CAP PAIRS AND THE IDENTICAL-MULTISET TEST")
    print("   A drop site is j with a[j] > a[j+r]: the cap a[j] overflows "
          "onto the cap a[j+r].")
    tables = {}
    for name, a in WINDOWS:
        print(f"\n  {name}")
        tables[name] = {}
        for which in SITE_BOUNDS:
            print(f"    -- {which} bound --")
            groups = {}
            for r in range(1, R_MAX + 1):
                jm = bounds(a, r, RANGES3[-1])[which]
                s = drop_sites(a, r, jm)
                tables[name][(which, r)] = s
                key = tuple(sorted(s))
                groups.setdefault(key, []).append(r)
                print(f"      r {r}: {split[name][r]:8s} "
                      f"{len(s)} sites  {list(s)}")
            for key, rs in sorted(groups.items(), key=lambda kv: kv[1]):
                if len(rs) < 2:
                    continue
                vs = {split[name][r] for r in rs}
                flag = ("   <<< P4 KILL: identical sites, different verdicts"
                        if len(vs) > 1 else "")
                print(f"      group {rs}: verdicts "
                      f"{[split[name][r] for r in rs]}{flag}")
    return tables


# ------------------------------------------------------------------ S3

def separates(stat, verdict):
    """Thresholds t with (stat >= t) agreeing with bounded, or with gated.

    Returns the sorted list of separating thresholds -- empty when no
    threshold on this statistic reproduces the split.
    """
    keys = [r for r in stat if verdict[r] in ("GATED", "bounded")]
    if not keys:
        return []
    cands = sorted({stat[r] for r in keys} | {min(stat[r] for r in keys) - 1})
    out = []
    for t in cands:
        hi = {verdict[r] for r in keys if stat[r] >= t}
        lo = {verdict[r] for r in keys if stat[r] < t}
        if hi <= {"bounded"} and lo <= {"GATED"}:
            out.append((t, "bounded above"))
        if hi <= {"GATED"} and lo <= {"bounded"}:
            out.append((t, "gated above"))
    return out


def score_form(name, sites_by_r, verdict, test):
    """EXISTENTIAL, UNIVERSAL, COUNT and FRACTION over a per-site test."""
    live = {r: s for r, s in sites_by_r.items()
            if s and verdict[r] in ("GATED", "bounded")}
    if not live:
        print(f"      {name}: no stride with drops and a verdict")
        return
    ex = un = 0
    cnt, frac = {}, {}
    for r, s in live.items():
        ok = [test(A, B) for A, B in s]
        cnt[r] = sum(ok)
        frac[r] = sum(ok) / len(ok)
        ex += ("bounded" if any(ok) else "GATED") != verdict[r]
        un += ("bounded" if all(ok) else "GATED") != verdict[r]
    n = len(live)
    print(f"      {name}: {n} strides scored | EXISTENTIAL {ex} misses"
          f" | UNIVERSAL {un} misses"
          f" | COUNT thresholds that separate {separates(cnt, verdict)}"
          f" | FRACTION {separates(frac, verdict)}")
    print(f"         counts {dict(sorted(cnt.items()))}  verdicts "
          + str({r: verdict[r][0] for r in sorted(live)}))


def s3_scoring(split, tables):
    print()
    print("=" * 78)
    print("S3 THE QUANTIFIER SCORING against the corrected split")
    print("   ROOF     per site: A <= 2B + 1  (dimensionless in the caps)")
    print("   PRODUCT  per site: A * B >= T, T swept over every realized "
          "product; 30 carries no standing")
    for name, a in WINDOWS:
        print(f"\n  {name}")
        for which in SITE_BOUNDS:
            sites_by_r = {r: tables[name][(which, r)]
                          for r in range(1, R_MAX + 1)}
            print(f"    -- {which} bound --")
            score_form("ROOF   ", sites_by_r, split[name],
                       lambda A, B: A <= 2 * B + 1)
            prods = sorted({A * B for s in sites_by_r.values()
                            for A, B in s})
            sep = []
            for T in prods:
                live = {r: s for r, s in sites_by_r.items()
                        if s and split[name][r] in ("GATED", "bounded")}
                ex = sum(("bounded" if any(A * B >= T for A, B in s)
                          else "GATED") != split[name][r]
                         for r, s in live.items())
                un = sum(("bounded" if all(A * B >= T for A, B in s)
                          else "GATED") != split[name][r]
                         for r, s in live.items())
                cnt = {r: sum(1 for A, B in s if A * B >= T)
                       for r, s in live.items()}
                if ex == 0 or un == 0 or separates(cnt, split[name]):
                    sep.append((T, ex, un, separates(cnt, split[name])))
            print(f"      PRODUCT: {len(prods)} realized products "
                  f"{prods}")
            print(f"         thresholds T with a form scoring 0 misses or "
                  f"separating: {sep if sep else 'NONE'}")
            score_form("PROD@30", sites_by_r, split[name],
                       lambda A, B: A * B >= 30)
            score_form("BOTH@30", sites_by_r, split[name],
                       lambda A, B: A <= 2 * B + 1 and A * B >= 30)


# ------------------------------------------------------------------ S4

def s4_family():
    print()
    print("=" * 78)
    print(f"S4 THE TWO-CLASS FAMILY AT THREE RANGES {RANGES3}")
    print("   explore_cascade_span.py F6 reports 84 cells at two ranges "
          "with gap parity")
    print("   disagreeing at 19. Every BOUNDED cell there carries H1's "
          "exposure.")
    cells = flips = dis2 = dis3 = 0
    for P, c1, c2, A, B in FAMILY:
        a = graded(P, {c1: A, c2: B})
        rmax = min(2 * P, 8 + 4)
        two = vector3(a, rmax, ranges=RANGES)
        three = vector3(a, rmax, ranges=RANGES3)
        print(f"\n  X P={P} caps {A}@{c1}/{B}@{c2}")
        for r in sorted(three):
            cells += 1
            v2, v3 = two[r][0], three[r][0]
            gv = gap_parity(a, r, 30)[3]
            dis2 += gv != v2
            dis3 += gv != v3
            moved = v2 != v3
            flips += moved
            print(f"      r {r:2d}: two-range {v2:8s} three-range {v3:8s}"
                  f"  gap-parity {gv:8s}"
                  f"{'   <<< MOVED' if moved else ''}"
                  f"{'   gap-parity disagrees' if gv != v3 else ''}")
    print()
    print(f"  {cells} cells; {flips} moved under the third range")
    print(f"  gap-parity disagreements: {dis2} at two ranges "
          f"(F6 reports 19), {dis3} at three")


# The cells S4 printed as moving under the third range, copied from that
# run rather than recomputed -- S5's input set.
MOVED = (((6, 1, 4, 5, 2), 10), ((7, 2, 3, 5, 2), 10))


def column(row):
    """The c_min column as H1 reads it: max(0, A[t] - t + 1) at each t."""
    return [max(0, row["A"][t] - t + 1) for t in range(1, row["tmax"] + 1)]


def decline(c):
    """Longest run of nonzeros falling by exactly 1 per depth."""
    best = run = 0
    for i, x in enumerate(c):
        if x and i and c[i - 1] == x + 1:
            run += 1
        elif x:
            run = 1
        else:
            run = 0
        best = max(best, run)
    return best


def s5_signature():
    """THE THIRD SLATE (frozen after S4 printed; it reads S4's mover list
    and H1's stated shape, and no other result).

    H1's exposure is written as "a bounded two-range verdict", which is
    what made the audit 24 cells there and 84 here. But H1 also describes
    the SHAPE that flips -- a witness declining by exactly 1 per depth
    that bottoms out inside the table, 0 0 0 5 4 3 2 1 0 0 -- and
    contrasts it with the local bump 0 0 0 0 1 0 0 0 0 0 that holds at
    all three ranges. If the shape is what predicts the flip, the audit
    is a filter and not a sweep.

      P9 among the two-class family's bounded-at-two-ranges cells, the
         column's longest run of nonzeros falling by exactly 1 per depth
         is printed per cell. The observable is whether that statistic
         separates the cells S4 moved from the cells S4 held. KILL: a
         held cell whose run is as long as a mover's, or a mover with no
         run -- the shape is then not the predictor and the audit stays
         a sweep over every bounded cell.
    """
    print()
    print("=" * 78)
    print(f"S5 THE FLIP SIGNATURE at the two ranges {RANGES}")
    print("   H1's flipping shape is a decline of 1 per depth that bottoms "
          "out inside the")
    print("   table; its holding shape is a local bump. Printed per bounded "
          "cell here.")
    rows = {"moved": [], "held": []}
    for key in FAMILY:
        P, c1, c2, A, B = key
        a = graded(P, {c1: A, c2: B})
        rmax = min(2 * P, 8 + 4)
        two = [cell_rows("", a, n, rmax=rmax, show=False) for n in RANGES]
        for r in sorted(two[0]):
            v = range_verdict([row[r] for row in two])
            if v != "bounded":
                continue
            c = column(two[-1][r])
            tag = "moved" if (key, r) in MOVED else "held"
            rows[tag].append((P, c1, c2, r, c))
    for tag in ("moved", "held"):
        print(f"    -- {tag} ({len(rows[tag])} cells) --")
        for P, c1, c2, r, c in rows[tag]:
            print(f"      P={P} caps@{c1}/{c2} r {r:2d}: "
                  f"max c {max(c)}  longest decline {decline(c)}"
                  f"  bottom {c[-1]}  column {c}")
    # Four statistics of the shape, each scored for separation on its own.
    stats = {"max c": lambda c: max(c),
             "longest decline": decline,
             "value at the deepest depth": lambda c: c[-1],
             "deepest depth nonzero and alone": lambda c: int(
                 c[-1] > 0 and not any(c[:-1]))}
    won = []
    for label, f in stats.items():
        mv = sorted(f(c) for *_, c in rows["moved"])
        hd = sorted({f(c) for *_, c in rows["held"]})
        sep = bool(mv and hd and (min(mv) > max(hd) or max(mv) < min(hd)))
        won += [label] if sep else []
        print(f"    {label}: moved {mv}, held {hd} -> separates: "
              f"{'YES' if sep else 'NO'}")
    print(f"    P9: column statistics that predict the flip, of "
          f"{len(stats)}: {won if won else 'NONE -- the audit stays a sweep'}")
    print("    the aperiodic windows' bounded columns, for comparison:")
    for name, a in WINDOWS:
        two = [cell_rows("", a, n, rmax=R_MAX, show=False) for n in RANGES]
        for r in sorted(two[0]):
            if range_verdict([row[r] for row in two]) != "bounded":
                continue
            c = column(two[-1][r])
            print(f"      {name:16s} r {r}: max c {max(c)}  longest "
                  f"decline {decline(c)}  column {c}")


STAGES = ("s0", "s1", "s2", "s3", "s4", "s5")

if __name__ == "__main__":
    want = [s for s in sys.argv[1:] if s in STAGES] or list(STAGES)
    ok = s0_controls() if "s0" in want else True
    if not ok:
        sys.exit(1)
    split = tables = None
    if {"s1", "s2", "s3"} & set(want):
        split = s1_reread()
    if "s2" in want or "s3" in want:
        tables = s2_sites(split)
    if "s3" in want:
        s3_scoring(split, tables)
    if "s4" in want:
        s4_family()
    if "s5" in want:
        s5_signature()
