"""Does the criterion the proved law implies have a shape the loose one lacked?

THE QUESTION
------------
On a bare cell -- a finite set of atoms, each carrying a mass and a
posterior row over labels -- the marginal-coverage optimum abandons an
atom precisely when its best label's posterior falls below the operative
level, PROVIDED the atoms carry equal mass. The family sweep and the
lattice refinement both scored a weight vector CLEAN by a criterion
strictly stronger than that law: every optimum of every cell abandons
exactly the below-level atoms. The law asks only that the threshold rule
BE one optimum. The two come apart wherever a cell has several optima,
and the gap is not small -- equal mass itself fails the strong reading
at two of the four targets swept.

So the survivor sets already printed never measured how far the derived
law extends. This file scores the FORCED criterion instead: an atom
fails only when EVERY optimum breaks the threshold rule, which is the
reading the proved law implies. The rig computes both criteria from one
pass over the optima, so the LOOSE reading comes free and serves as the
reproduction control on the whole sweep.

WHAT IS ALREADY DERIVED, AND SO IS NOT WHAT THIS RUN BUYS
---------------------------------------------------------
Three things were settled on paper before the engine, and the engine
prints them as confirmations rather than as findings.

  ZERO AT EQUAL MASS, EVERY TARGET. At equal masses the threshold rule
  IS an optimum. An above-level atom fails forcedly only when EVERY
  optimum abandons it -- and that one serves it. A below-level atom
  fails forcedly only when every optimum serves it -- and that one
  abandons it. So the equal-mass control takes zero forced failures on
  both halves at every target -- a PROPERTY, following from the threshold
  rule being an optimum there and from no sweep. A non-zero print is a bug
  in the scorer or the level, never a finding, and it is the assertion
  whose absence let a target-mixing bug through a full run.

  NOT VACUOUS. Where a cell's optimum is unique the two quantifiers
  coincide and forced equals loose. The vector (2, 3, 35) has a unique
  optimum in all 625 cells of the first arm and 619 loose failures, so
  it carries 619 forced failures and cannot survive. The forced set is a
  proper subset of the grid whatever else it is.

  WIDER OR EQUAL. Forced failures are at most loose ones at every
  vector, so the forced survivor set CONTAINS the loose one. Only
  STRICTLY wider is news, and only the SHAPE is the find.

WHAT FORCED MINUS LOOSE ACTUALLY MEASURES is where the TIES live. A
vector moves from loose-failing to forced-clean exactly when every one
of its loose failures is rescued by some optimum agreeing with the
threshold rule. The recorded tie census is lopsided -- the near-equal
(11, 11, 18) carries 297 tied cells and takes no loose failure, while
the extreme (2, 3, 35) is unique everywhere -- so the forced set may
fatten around the middle while the extremes stay failing.

THE ARMS
--------
The predecessor's five sweeps, unchanged in every other respect, over
the same 741 ordered compositions of 40 into three positive parts:

  ARM 1  menus A-E (twentieth posteriors), nominal coverage 7/10.
  ARM 2  menus F-J (fortieth posteriors, sharing no row with A-E),
         same target.
  ARM 3  menus A-E at nominal coverage 3/5.
  ARM 4  menus A-E at nominal coverage 1/2, where the loose survivor
         set is EMPTY -- the arm with the most room to move.
  ARM 5  menus A-E at nominal coverage 3/4.

THE PREDICTIONS, frozen before the engine
-----------------------------------------
P1  The forced survivor set on arm 1 is STRICTLY larger than the 87
    loose survivors, and contains all 87. Containment is construction;
    strictness is the prediction. Equality would be the sharpest
    outcome available -- ties rescuing individual cells but never a
    whole vector.

P2  IT IS NOT A BOX, and neither the SPREAD bound nor the RATIO bound
    fits either, all three tested as set equality against the tightest
    such description over the set. Four one-line descriptions have
    already failed on the loose set and nothing about the stronger
    criterion suggests a cleaner boundary. The refutation worth having
    is the other one: a fit would make the FORCED criterion the one
    with the shape and the loose reading the artifact, which is the
    outcome this run is built to reach.

P3  The forced extremes on arm 1 lie STRICTLY outside [7/40, 21/40],
    the loose set's own extremes.

P4  Arm 4 -- coverage 1/2, where the loose set is empty -- has a
    NON-EMPTY forced set. This is a prediction and not a derivation:
    equal mass is not a grid member (1/3 is not a fortieth), so the
    control's own zero guarantees nothing about the grid.

P5  Every forced survivor set is closed under permutation of the weight
    vector. A violation is a BUG in the scoring or the grid, never a
    finding.

THE CONTROLS
------------
C1  ZERO AT EQUAL MASS. The equal-mass vector is swept explicitly on
    every arm and its forced counts are asserted zero on both halves
    BEFORE any survivor set is read. Derived above; measured here.

C2  THE CONTROL IS NOT VACUOUS. The equal-mass above-half population is
    asserted non-empty on every arm.

C3  REPRODUCTION. The LOOSE readings recomputed here must reproduce the
    record exactly: 87 survivors on arm 1's five menus, 27 on arm 2 with
    none of them outside arm 1's, and ZERO at coverage 1/2. A miss means
    this file's sweep is not the sweep the record came from, and no
    forced number may be read.

C4  CONTAINMENT. At every weight vector, on both halves and every arm,
    the loose failure count is at least the forced one.

C5  THE DENOMINATORS. Every survivor set is printed against its at-risk
    populations on both halves. A zero over an empty population is
    reported as untested and never as a pass. The below half is known to
    be thin at three atoms and the report says how thin.

RESOURCES
---------
Five arms of five menu-sweeps, 741 weight vectors x 125 cells each,
timed at ~32 s per sweep: ~13 minutes wall-clock and a few tens of
megabytes of Fractions. That is over the ten-minute line and the reason
is that nothing cheaper decides it -- the shape question needs the whole
refined grid, and the criterion has to be read at every target because
the loose one's failures were not monotone in the target. The pipeline
is rehearsed first on a small grid (--rehearse), which exercises every
arm, every set reading and every control in seconds, so a kill costs
seconds rather than the run.

WHAT RAN
--------
One run, rehearsed first. 25 menu-sweeps, 741 weight vectors x 125
cells apiece, 817 s, peak working set 20.5 MB under memwatch against a
512 MB ceiling.

The rehearsal fired P5's permutation assert on its first execution, and
the fault was the REHEARSAL GRID: a sample drawn by a coordinate
condition is not closed under permutation, so asserting closure on it
tests the sample and not the scoring. The rehearsal grid is now the
closure of six representatives, and the full run's cost was measured
from it -- 27 vectors, 25 sweeps, 31 s -- rather than inherited.

EVERY CONTROL PASSES. C1: the equal-mass control takes zero FORCED
failures on both halves at all five arms, which is the theorem above
holding exactly; it takes loose failures freely, 372 above and 9 below
at coverage 1/2, every one of them rescued by a tie. C2 non-vacuous at
every arm (above-half populations 1674, 1755, 1365, 957, 1815). C3
REPRODUCTION is exact and it is the control that matters most, because
it is the whole sweep audited against the record it is being compared
to: 87 loose survivors on arm 1, 27 on arm 2 with none of them outside
arm 1's, and zero at coverage 1/2. C4 containment holds at all 741
vectors on all five menus of all five arms. C5's denominators are
printed per menu and they are the reason the below half is reported as
untested rather than passed.

WHAT IT FOUND
-------------
THE FORCED SET IS WIDER AND IT IS STILL SHAPELESS, WHICH PUTS THE
SHAPELESSNESS ON THE CONDITION AND NOT ON THE CRITERION. Arm 1's
five-menu forced set is 105 of 741 against the loose 87, containing all
87 (P1 holds). It is not a box: its tightest coordinate box [7/40, 3/5]
holds 201 and it misses 96 of them. Neither rival fits -- spread carries
168 excess vectors, ratio 87. Every other arm reads the same way. Over
the eight non-empty survivor sets this run produced -- four ARMS by two
criteria, spanning three targets and both posterior lattices, the fourth
target carrying no set at all -- not ONE is a box, and neither the spread
bound nor the ratio bound fits any of them. That was the reading the run was built to
decide, and it decides it against the criterion being the artifact:
the strong reading and the reading the proved law implies are shapeless
alike.

  arm            coverage    loose   forced   tightest forced box
  A-E            7/10           87      105   [7/40, 3/5]  misses 96
  F-J (40ths)    7/10           27       54   [1/5, 1/2]   misses 69
  A-E            3/5             6       18   [9/40, 1/2]  misses 78
  A-E            1/2             0        0   empty
  A-E            3/4           150      183   [3/20, 5/8]  misses 75

P3 IS REFUTED AND THE WAY IT FAILS IS THE INTERESTING PART. The forced
extremes on arm 1 are [7/40, 3/5]: the LOW endpoint does not move at
all while the high one moves 3/40 outward. It is not a general
asymmetry -- both endpoints move on arms 2 and 3 -- and on arm 5 the
tightest box is [3/20, 5/8] under BOTH criteria, so there the criterion
change fills 33 vectors of the interior without touching the hull at
all. What the criterion buys is not a uniformly wider region.

P4 IS REFUTED, AND ITS REFUTATION IS THE RUN'S SECOND FIND. At coverage
1/2 the forced five-menu set is EMPTY, not merely small, and it is
empty while the per-menu forced sets are not: 21, 9, 12, 12 and 6
vectors survive the menus one at a time and no vector survives all
five. So at that target NO fortieth weight vector obeys the derived law
across the five menus, while equal mass obeys it by theorem and is not
on the lattice (1/3 is not a fortieth). The clean region at coverage
1/2 is therefore smaller than this lattice can see -- a statement about
resolution, and the one place where refining the grid again would
actually buy something.

AND THE SET SIZE IS MONOTONE IN THE NOMINAL COVERAGE WHERE THE FAILURE
COUNT WAS NOT. Arms 1, 3, 4 and 5 share menus A-E, so the four targets
are a controlled comparison: the forced set reads 183, 105, 18, 0 as
coverage falls 3/4, 7/10, 3/5, 1/2, and the loose set reads 150, 87, 6,
0 alongside it. The obvious explanation is the wrong way round on the half
that was measured across the grid: the ABOVE-half exposure falls too,
1,307,295 atoms at 3/4 to 665,862 at 1/2, so the clean set is not being
killed by a growing above-level population. It collapses to nothing on
HALF that exposure. The below-level population is the half this run does
NOT have grid-wide, and it moves the OTHER way where it is visible --
the equal-mass control carries 0 below-level atoms at 7/10 and 102 at
1/2 -- so the population explanation is dead only for the above half.
Why is left open, and it is now the sharpest question this thread has.

AND THE HALF THIS RUN DID NOT HAVE GRID-WIDE WAS MEASURED AFTERWARDS,
which is cheap because the POPULATIONS need only the level and the
posteriors and never the optima -- the same 463,125 cells, 84 s, no
sweep. It reproduces this run's above-level figures exactly by a code
path that computes no optimum at all, and it moves the candidate back:

  coverage      ABOVE      BELOW    at level     forced clean
     3/4      1307295       5898       76182         183
     7/10     1204311      17796      167268         105
     3/5       951717      68124      369534          18
     1/2       665862     157623      565890           0

The BELOW-level population grows 26.7-fold, 5,898 atoms to 157,623,
across exactly the span where the clean set empties, while the above
half halves and the indifference band grows 7.4-fold. So a growing
population is NOT ruled out -- it is ruled out for the above half only,
and the half it is alive for is the half the survivors barely touch (24,
12, 168 and 0 at-risk atoms). The shape of a mechanism is now visible
and is not yet earned: a clean vector must get every below-level atom
right, below-level atoms proliferate as coverage falls, and at 1/2 no
vector on the lattice manages all five menus. Four points and a
correlation; it is a candidate, not a cause.

(STILL THE CANDIDATE, explore_ruler_room.py. The RIVAL candidate --
the certificate's own room D/t*, the only sufficient condition the
corpus carries -- has since been read at all four targets and is dead:
corrected to its true threshold gcd/N it fires at zero of 741 vectors
at every target, and its per-cell rate moves up then down against a
clean set falling monotonically. The below-level population above is
not confirmed by that; it is simply the candidate still standing.)

WHAT THIS LEAVES OPEN: the below half, which is where it was -- across
every arm the forced survivor sets carry at-risk below-level
populations of 24, 12, 168 and 0 atoms against six-figure above-level
ones, so nothing about the condition's other direction is decided at
three atoms and an arity above three is what would decide it. And the
shape question is now closed in the negative for both criteria at this
arity: the box, the spread bound and the ratio bound fail on all eight
sets under BOTH criteria, so the criterion is not what they were failing
against.
"""

import os
import sys
import time
from fractions import Fraction

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_ruler_abandon import ALPHA, EQUAL  # noqa: E402
from explore_ruler_box import (  # noqa: E402
    ALPHA2,
    DEN,
    GRID,
    NEW,
    OLD,
    box_of,
    fmt,
    perm_closed,
    rival_fits,
    sweep,
)

F = Fraction

# The record this run must reproduce on its loose reading (C3).
LOOSE_ARM1 = 87
LOOSE_ARM2 = 27

# The loose set's own extremes on arm 1, for P3.
LOOSE_LO, LOOSE_HI = F(7, DEN), F(21, DEN)

# The vector whose optimum is unique in all 625 arm-1 cells.
UNIQUE_W = (F(2, DEN), F(3, DEN), F(35, DEN))

ARMS = (
    ("ARM 1 -- menus A-E, coverage 7/10", OLD, ALPHA),
    ("ARM 2 -- menus F-J (fortieth posteriors), coverage 7/10", NEW, ALPHA),
    ("ARM 3 -- menus A-E, coverage 3/5", OLD, ALPHA2),
    ("ARM 4 -- menus A-E, coverage 1/2", OLD, F(1, 2)),
    ("ARM 5 -- menus A-E, coverage 3/4", OLD, F(1, 4)),
)

LOOSE_KEYS = ("above_loose", "below_loose")
FORCED_KEYS = ("above_forced", "below_forced")


def survivors(tally, half_keys):
    return {w for w, r in tally.items() if all(r[k] == 0 for k in half_keys)}


def equal_mass_control(name, menus, alpha):
    """C1 and C2, both asserted before any survivor set is read."""
    tal, tr = sweep([EQUAL], menus, alpha)
    r = tal[EQUAL]
    print("   C1/C2 EQUAL MASS: model failures %d; at risk ABOVE %d"
          " BELOW %d (at level %d)"
          % (tr, r["above_pop"], r["below_pop"], r["at_level"]))
    print("         loose ABOVE %d BELOW %d;  FORCED ABOVE %d BELOW %d"
          % (r["above_loose"], r["below_loose"],
             r["above_forced"], r["below_forced"]))
    assert tr == 0, ("C1: equal-mass cell is not a probability model", name)
    assert r["above_pop"] > 0, ("C2 vacuous: nothing above the level", name)
    assert r["above_forced"] == 0 and r["below_forced"] == 0, (
        "C1 BROKEN: equal mass takes a FORCED failure, which the proved"
        " law forbids -- this is a bug and not a finding", name,
        r["above_forced"], r["below_forced"])
    if r["below_pop"] == 0:
        print("         BELOW HALF UNTESTED at equal mass on this arm:"
              " an empty population, not a pass.")
    return r


def report_set(label, members, grid):
    """Size, orbits, the box fit and the two rivals, scored alike."""
    print("      %s: %d of %d vectors" % (label, len(members), len(grid)))
    if not members:
        print("         EMPTY -- nothing to read a shape off.")
        return None
    orbits = sorted({tuple(sorted(int(x * DEN) for x in w))
                     for w in members})
    print("         orbits in %dths (%d): %s"
          % (DEN, len(orbits),
             orbits if len(orbits) <= 10 else str(orbits[:10]) + " ..."))
    lo, hi, box, missing = box_of(members, grid)
    print("         tightest coordinate box [%s, %s] holds %d;"
          " IS THE SET A BOX: %s%s"
          % (lo, hi, len(box), not missing,
             "" if not missing else "  (misses %d)" % len(missing)))
    (ms, nsp, dsp), (mr, nra, dra) = rival_fits(members, grid)
    print("         rival SPREAD <= %-7s holds %4d, excess %4d, FITS: %s"
          % (str(ms), nsp, dsp, dsp == 0))
    print("         rival RATIO  <= %-7s holds %4d, excess %4d, FITS: %s"
          % (str(mr), nra, dra, dra == 0))
    ok, bad = perm_closed(members)
    print("         P5 permutation closure: %s"
          % ("holds" if ok else "BROKEN at %s / %s -- a bug" % bad))
    assert ok, ("P5: survivor set is not permutation closed", label, bad)
    return lo, hi, box, missing


def exposure(label, members, tallies):
    """C5: the denominators, per menu, for a set."""
    if not members:
        return
    for half in ("above", "below"):
        parts = []
        for t in sorted(tallies):
            pop = sum(tallies[t][w]["%s_pop" % half] for w in members)
            frc = sum(tallies[t][w]["%s_forced" % half] for w in members)
            parts.append("%s %d/%d%s" % (t, pop, frc,
                                         "" if pop else " UNTESTED"))
        print("         %s %s-half exposure per menu (pop/forced): %s"
              % (label, half, "   ".join(parts)))


def run_arm(name, menus, alpha, grid):
    print()
    print("=" * 70)
    print(name)
    print("   alpha = %s, nominal coverage %s, %d weight vectors"
          % (alpha, 1 - alpha, len(grid)))
    equal_mass_control(name, menus, alpha)
    tallies, loose, forced = {}, {}, {}
    for menu, tag in menus:
        t0 = time.time()
        tt, tr = sweep(grid, ((menu, tag),), alpha)
        assert tr == 0, ("C5: menu is not a probability model", tag)
        for w, r in tt.items():
            assert r["above_loose"] >= r["above_forced"], ("C4", tag, w)
            assert r["below_loose"] >= r["below_forced"], ("C4", tag, w)
        tallies[tag] = tt
        loose[tag] = survivors(tt, LOOSE_KEYS)
        forced[tag] = survivors(tt, FORCED_KEYS)
        print("      %-4s swept: at-risk above %7d;  loose survivors %4d,"
              " FORCED survivors %4d   (%.0f s)"
              % (tag, sum(r["above_pop"] for r in tt.values()),
                 len(loose[tag]), len(forced[tag]), time.time() - t0))
    fl = set.intersection(*loose.values())
    ff = set.intersection(*forced.values())
    print("   C4 CONTAINMENT holds at all %d vectors on all five menus"
          % len(grid))
    print("   FIVE-MENU INTERSECTIONS: loose %d, forced %d (gain %d)"
          % (len(fl), len(ff), len(ff - fl)))
    assert fl <= ff, "containment broken at the intersection"
    report_set("LOOSE (the record's criterion)", fl, grid)
    fit = report_set("FORCED (the law's criterion)", ff, grid)
    exposure("its", ff, tallies)
    return tallies, fl, ff, fit


def main():
    rehearse = "--rehearse" in sys.argv
    if rehearse:
        # A permutation-CLOSED sample, because P5 is asserted and an
        # unclosed rehearsal grid would fire it as an artifact of the
        # sample rather than of the scoring. Representatives: three
        # near-equal orbits, the unique-optimum extreme, and two of the
        # odd-numerator vectors that broke the box.
        reps = ((12, 12, 16), (13, 13, 14), (12, 14, 14), (2, 3, 35),
                (7, 16, 17), (9, 10, 21))
        grid = sorted({tuple(F(x, DEN) for x in p)
                       for r in reps
                       for p in ((r[0], r[1], r[2]), (r[0], r[2], r[1]),
                                 (r[1], r[0], r[2]), (r[1], r[2], r[0]),
                                 (r[2], r[0], r[1]), (r[2], r[1], r[0]))})
        print("REHEARSAL on %d weight vectors (permutation closed) --"
              " every arm, every set reading, every control; the record's"
              " numbers are NOT reproduced here and C3 is skipped."
              % len(grid))
    else:
        grid = GRID
    print("DOES THE FORCED CRITERION HAVE A SHAPE THE LOOSE ONE LACKED?")
    print("weight lattice %dths: %d ordered compositions; scoring %d"
          % (DEN, len(GRID), len(grid)))

    out = {}
    for name, menus, alpha in ARMS:
        out[name[:5]] = run_arm(name, menus, alpha, grid)

    print()
    print("=" * 70)
    print("THE READING")

    tal1, fl1, ff1, fit1 = out["ARM 1"]
    _t2, fl2, ff2, _f2 = out["ARM 2"]
    if not rehearse:
        print("   C3 REPRODUCTION of the record's loose numbers:"
              " arm 1 %d (expect %d), arm 2 %d (expect %d), arm 2"
              " outside arm 1 %d (expect 0), coverage 1/2 %d (expect 0)"
              % (len(fl1), LOOSE_ARM1, len(fl2), LOOSE_ARM2,
                 len(fl2 - fl1), len(out["ARM 4"][1])))
        assert len(fl1) == LOOSE_ARM1 and len(fl2) == LOOSE_ARM2, (
            "C3: the loose reading does not reproduce the record")
        assert not (fl2 - fl1), "C3: arm 2 gained a loose survivor"
        assert not out["ARM 4"][1], "C3: coverage 1/2 loose set is not empty"

    print("   P1 arm 1 forced %d vs loose %d: STRICTLY WIDER: %s;"
          " contains all %d: %s"
          % (len(ff1), len(fl1), len(ff1) > len(fl1), len(fl1),
             fl1 <= ff1))

    if UNIQUE_W in tal1["A"]:
        lo_t = sum(tal1[t][UNIQUE_W]["above_loose"]
                   + tal1[t][UNIQUE_W]["below_loose"] for t in tal1)
        fo_t = sum(tal1[t][UNIQUE_W]["above_forced"]
                   + tal1[t][UNIQUE_W]["below_forced"] for t in tal1)
        print("   NOT VACUOUS, as derived: %s takes %d loose and %d forced"
              " failures over arm 1's five menus (unique optimum, so the"
              " two quantifiers coincide); it survives forced: %s"
              % (fmt(UNIQUE_W), lo_t, fo_t, UNIQUE_W in ff1))

    if fit1:
        print("   P3 forced extremes [%s, %s] against the loose [%s, %s]:"
              " STRICTLY OUTSIDE: %s"
              % (fit1[0], fit1[1], LOOSE_LO, LOOSE_HI,
                 fit1[0] < LOOSE_LO and fit1[1] > LOOSE_HI))

    print("   P4 coverage 1/2: loose %d, FORCED %d, non-empty: %s"
          % (len(out["ARM 4"][1]), len(out["ARM 4"][2]),
             bool(out["ARM 4"][2])))

    print("   ACROSS THE ARMS (forced size, and whether it is a box):")
    for name, _m, _a in ARMS:
        _t, fl, ff, fit = out[name[:5]]
        # An EMPTY set is not "not a box" -- it is no set. Printing
        # False for it reads as a shape verdict that was never taken.
        print("      %-52s %4d   box: %s"
              % (name, len(ff),
                 "no set" if fit is None else str(not fit[3])))


if __name__ == "__main__":
    main()
