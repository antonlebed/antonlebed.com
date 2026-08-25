"""Are the box's endpoints the condition's, or the grid's?

THE QUESTION
------------
On a bare cell -- a finite set of atoms, each carrying a mass and a
posterior row over labels -- the marginal-coverage optimum abandons an
atom precisely when its best label's posterior falls below the operative
level, PROVIDED the atoms carry equal mass. Off equal mass the condition
is not a law and both directions have exact counterexamples.

The family sweep asked how much wider than equal mass the condition
survives, scored per WEIGHT VECTOR against its own at-risk denominator.
Over five menus -- two designed, three drawn blind -- the vectors taking
zero loose failures on both halves cut down to exactly those whose every
coordinate lies in [1/4, 9/20]: a region with a one-line description,
with equal mass 1/3 strictly inside it. That is a proof target and not a
law; nothing derives it.

It is also written on a grid that can barely express it. The weights
there are twentieths and the menu rows are twentieths, and 1/4 = 5/20
and 9/20 are the COARSEST values that grid can put at a boundary: the
box could be the condition's own region, or it could be the twentieth
lattice rounding a region with different edges out to the nearest thing
it can say. This file refines the lattice to FORTIETHS and reads what
happens to the endpoints.

WHAT REFINING MEANS, AND WHY IT IS THREE ARMS AND NOT ONE
---------------------------------------------------------
Two lattices carry the twentieth result and they are independent. The
WEIGHTS live on one; the menu POSTERIORS live on another. Refining only
the weights leaves every posterior where it was, and a box that holds
under that would still be consistent with the edges being an artifact of
the rows. Refining both at once cannot say which one moved anything. So:

  ARM 1 -- THE WEIGHT LATTICE ALONE. The same five menus A-E, in
  twentieths, unchanged; the weight grid becomes all 741 ordered
  compositions of 40 into three positive parts, against 171 at
  twentieths. This is the arm that answers the roadmap's question,
  because it is the only one where a MOVED endpoint has one cause. The
  even-numerator vectors are the twentieth grid exactly, so this arm
  contains its own predecessor and must reproduce it (C3).

  ARM 2 -- THE POSTERIOR LATTICE. Five further menus F-J, drawn blind
  in fortieths, over the same 741 weight vectors. Every row carries
  exactly TWO odd numerators, which is the parity a fortieth row must
  have to sum to 40 without being a twentieth row in disguise, so no
  row of this arm is expressible on the old lattice and none can
  coincide with A-E. If the box is a property of the weights it should
  survive an arm whose posteriors it has never met.

  ARM 3 -- THE TARGET. Menus A-E and the 741 vectors again, at nominal
  coverage 3/5 instead of 7/10. This arm exists because of a relation
  read OFF the twentieth result after it printed, and it is that
  relation's first out-of-sample test. The box is [1/4, 9/20]; its
  endpoints sum to 7/10, which is the nominal coverage exactly, and they
  differ by 1/5. Post-hoc arithmetic on two numbers is worth nothing on
  its own -- it is worth a run because it makes a SHARP prediction at a
  target it was not fitted to.

THE PREDICTIONS, frozen before the engine
-----------------------------------------
P1  ARM 1 holds the box. The five-menu survivor set over the 741 is
    EXACTLY the 57 vectors with every coordinate in [1/4, 9/20], tested
    as set equality against the box and not read off the orbits.

P2  AND A HOLD DOES NOT PROVE THE ENDPOINTS -- this is registered as a
    prediction about the READING, so that a hold cannot be written up as
    more than it is. If P1 holds, the true endpoints are known only to
    lie in (9/40, 1/4] and [9/20, 19/40): every vector the finer grid
    adds outside the box is at least 1/40 out, so the grid still cannot
    see a boundary between 9/40 and 10/40. A hold NARROWS the window
    holding each endpoint from 1/20 to 1/40 and does no more; only a
    MOVE decides anything, and an inward move decides most.

P3  ARM 2's five-menu survivor set is again a box, and its endpoints
    are within 1/40 of 1/4 and 9/20. The refutation worth having is the
    other one: a set that is not a box, or endpoints further out, says
    the twentieth box was the posterior lattice's and not the weights'.

P4  ARM 3's survivor set is a box [lo, hi] with lo + hi = 3/5 and
    hi - lo = 1/5 -- that is, exactly [1/5, 2/5]. The rival named in
    advance is the CONSTANT reading: endpoints unchanged at [1/4, 9/20],
    which would make them a property of the menus and the arity and not
    a function of the target. Both are informative; a set that is no box
    at all kills the relation and the target question together.

P5  THE MENU SCARCITY IS RELIEVED, and it is measured rather than
    asserted. At twentieths the nearly flat three-label rows ran out --
    the fifth menu had to reuse the first's (8,8,4) -- so the count of
    fresh nearly flat rows the fortieth lattice offers is printed. The
    prediction is that it is at least ten, which is what five menus of
    two flats each need.

P6  Every survivor set is closed under permutation of the weight
    vector. A violation is a BUG in the scoring or the grid, never a
    finding.

HOW A SET IS READ AS A BOX
--------------------------
Never by eye and never against a remembered pair of endpoints. Given a
survivor set S the engine takes lo = the smallest coordinate appearing
anywhere in S and hi = the largest, builds the FULL box those two
determine over the grid, and reports set equality. A set that is a
proper subset of its own tightest box is NOT a box, and the report says
by how many vectors it misses. Two rival one-line descriptions are
scored the same way on the same set -- a SPREAD bound, max(w) - min(w)
at most the largest spread in S, and a RATIO bound, max(w)/min(w) at
most the largest ratio in S -- because "it is a box" is only news if the
neighbouring descriptions fit worse.

THE CONFOUND, unchanged and still the reason every count carries a
denominator: a weight vector can score zero failures because it never
puts an atom AT RISK. A failure needs an atom strictly ABOVE the level
that some optimum drops, or one strictly BELOW it that some optimum
buys. Where one atom is heavy enough to carry the target alone the level
lands on the cell's largest posterior value and no atom sits strictly
above it. So every survivor set is printed against its at-risk
populations on both halves, and a zero over an empty population is
reported as untested and never as a pass.

THE CONTROLS
------------
C1  PARITY. The optimum enumerator agrees with the bare cell library's
    independent exhaustive optimum at every cell of the equal-mass arm
    on menus A and B.

C2  THE CONTROL IS NOT VACUOUS. The equal-mass vector is swept
    explicitly on every arm and its at-risk populations are printed;
    the above-half population is asserted non-empty before any survivor
    verdict is read.

C3  REPRODUCTION. Arm 1 restricted to the 171 even-numerator vectors
    must reproduce the twentieth run's survivor counts exactly -- 42 on
    menus A+B, 42 on C, 24 on D, 39 on E -- and its five-menu
    intersection must be exactly the 18-vector twentieth box. This is
    the strongest bug check the design has, because the refined grid
    contains the old one as a subset and nothing about the old vectors'
    scores may change.

C4  CONTAINMENT. At every weight vector and on both halves the loose
    failure count is at least the forced one, by construction.

C5  EVERY MENU IS A MENU. Every cell every menu builds passes the
    probability-model check, and every menu reaches a non-empty
    above-half population -- a menu that put nothing at risk would hand
    back a survivor set of everything and refute nothing.

C6  THE NEW MENUS ARE NEW. The 25 rows of F-J are pairwise distinct as
    sorted tuples and no sorted row among them equals a sorted row of
    A-E. Asserted, not inspected.

RESOURCES
---------
Three arms of five menu-sweeps, 741 weight vectors x 125 cells each,
timed at ~30 s per sweep, so ~8 minutes wall-clock and a few megabytes
of Fractions. That is over the five-minute line and the reason is that
nothing cheaper decides these questions: the endpoint question needs the
whole refined grid, the lattice confound needs an arm whose posteriors
are not twentieths, and the relation in P4 can only be tested at a
target it was not fitted to. The pipeline is rehearsed first on a
restricted grid so that a kill costs seconds.

WHAT RAN
--------
TWO runs. The first was WRONG and the way it was wrong is the most
useful thing in this file. `score`, imported from the family sweep,
takes the operative LEVEL as an argument but read the OPTIMA from that
file's module-level target. Arms 1 and 2 run at that target and were
never affected; arm 3 and stage four move it, so they combined a level
computed at one target with optima computed at another and printed a
table with every control green. Nothing caught it: the controls check
parity, containment, permutation closure and reproduction, and a
scorer mixing two targets passes all four. What caught it was a
CONTROL LINE READ FOR ITS OWN SAKE -- equal mass showing 102 below-half
failures where the corpus proves it exact -- followed by printing the
optima of the first offending cell, which disagreed with the file's own
counters. The fix gives `score` an `alpha` that defaults to the old
global, so the family sweep is unchanged and a caller sweeping another
target must now say so.

The corrected run: 25 menu-sweeps at ~32 s, 741 weight vectors x 125
cells apiece, 13 minutes, 15 MB. Arms 1 and 2 reproduce the first run
line for line, which is the check that the fix reached only what it
should. Every control passes -- C1 at 250/250, C4, C5, C6, and P6 on
every arm, though P6 is printed over each arm's INTERSECTION and not
over each menu's own survivor set: the broader form frozen above was
checked separately and more strongly, by comparing the whole counter
tuple across all permutations of seven weight orbits on three menus, 99
tallies with no mismatch. C3 is exact: restricted to the 171
even-numerator vectors, arm 1 gives 42 survivors on A+B, 42 on C, 24 on
D, 39 on E, and a
five-menu intersection of 18 that IS the twentieth box. P5 holds: the
fortieth lattice offers 12 fresh nearly flat rows where twentieths had
none left.

WHAT IT FOUND
-------------
P1 IS REFUTED, AND THE BOX IS NOT BROKEN FROM INSIDE BUT OVERRUN FROM
OUTSIDE. Arm 1's five-menu survivor set is 87 of 741, not 57. All 57
box members survive; 30 further vectors come through clean, reaching
7/40 and 21/40. The tightest coordinate box over the 87 holds 165 and
MISSES 78, so the set is not a box, and neither rival fits -- spread
carries 69 excess vectors, ratio 42.

SO THE ENDPOINTS WERE THE GRID'S, WHICH IS THE CHEAP KILL THE QUESTION
WAS BUILT TO REACH. The vectors that break the box shape have odd
numerators -- (7, 16, 17), (9, 10, 21), (9, 11, 20) -- and a lattice
whose smallest step is 1/20 cannot write them. It rounded the clean
region out to the coarsest thing it could say and the result read as a
region with a one-line description.

ARM 2 CUTS THE 87 TO 27 ONE-WAY. Five menus on the fortieth POSTERIOR
lattice, sharing no row with A-E, leave 27 survivors, every one already
in the 87, none gained, against the 3.2 an unrelated set would share.
They are not a box either. Their extremes are 1/4 and 9/20 -- the old
endpoints, recovered on posteriors that never met them, which is worth
recording and is not worth a theory.

AND THE CRITERION ITSELF IS THE REAL FIND, arriving from the bug rather
than from the design. "Clean" here means EVERY optimum abandons exactly
the below-level atoms. That is strictly stronger than what the corpus
PROVES at equal mass, which is that the threshold rule IS an optimum
with that shape -- and the two come apart wherever a cell has several
optima. EQUAL MASS FAILS ITS OWN CRITERION AT TWO OF THE FOUR TARGETS
SWEPT: 162 loose above-level failures at coverage 3/5, and at coverage
1/2 no vector on the grid is clean at all while 816 of the control's
atoms sit AT the level in the indifference band. It is clean at 7/10
and at 3/4, so the failure is not monotone in the target and "away from
7/10" would be the wrong reading. What holds at all four is that it
takes ZERO FORCED failures, which is the proved property holding
exactly. So the survivor sets never measured "how far the derived law
extends".

AND THEY ARE NOT A MAP OF WHERE THE OPTIMUM IS UNIQUE EITHER, which is
the first thing they look like and is wrong in both directions: the
clean vector (11, 11, 18) carries 297 cells with more than one optimum
and takes no failure, while (2, 3, 35) has a unique optimum in all 625
cells and fails 619 times. Uniqueness is neither necessary nor
sufficient; what the criterion adds to the law is AGREEMENT among the
optima on the abandoned set, and a vector can fail it by having one
optimum that simply disagrees with the threshold rule.

WHICH IS WHY P4, P7 AND THE RELATION BEHIND THEM ARE ALL DEAD. The
extremes' sum reads 7/10 on arms 1 and 2, 13/20 at coverage 3/5, 31/40
at coverage 3/4, and is unreadable at 1/2 where the survivor set is
empty (P8's null, which the engine reports rather than counting as a
pass). It is neither the constant 7/10 nor the coverage. Four values,
no law -- and the two that agreed agreed because they share a target.
The relation was read off a printed table after the fact, predicted
sharply, and died at the first target it was not fitted to, which is
the whole of what such a relation is worth.

THE PAPER ROUTE IS DEFLATED TOO, and cheaply. Attacked on paper while
the first sweep ran, the corpus's own pieces assemble into a sufficient
condition: every cost is a multiple of 1/N when the weights are, the
certificate's error is at most D/t*, so D/t* < 1/N forces the threshold
rule optimal. That makes the clean set SHRINK as the lattice refines
and the clean region grew instead. The argument is only sufficient, so
it is not wrong -- but its N-dependence plainly does not govern what is
clean, and the tie gap it leaves open is the same gap the criterion
finding just made central.

(SETTLED, explore_ruler_room.py. Two corrections to the route above.
The threshold is not 1/N: g is the smallest POSITIVE element of the
lattice the weights generate, so it is gcd(a_r)/N, larger by the factor
gcd -- the 1/N reading is the worst case over the grid and the route
above is sound but loose. And read in its OTHER variable the room does
not run the wrong way, it does not run: D/t* is a subset-sum overshoot
in which t* fixes only a position, so it SAWTOOTHS in the target. On
this grid the corrected condition fires at ZERO of 741 vectors at every
one of four targets, its best orbit missing 41 to 70 cells of 625, so
the route's verdict stands and hardens -- the certificate's error is
not what governs the clean set in either variable.)

WHAT THIS LEAVES OPEN: whether a criterion that equal mass PASSES at
every target -- each atom respected by SOME optimum, rather than by
every one -- has a wider
clean set with a shape (SETTLED by explore_ruler_forced.py: wider, 105
of 741 against 87 on this arm, and NO shape -- the box, the spread bound
and the ratio bound fail on all eight non-empty sets under both
criteria, which puts the shapelessness on the condition rather than on
the criterion); what the clean set is, given four one-line
descriptions have failed on it (a FIFTH has since failed too, the gcd
stratification: no non-empty clean set is a union of gcd strata, though
gcd 8 and 10 are wholly clean at the two loosest targets --
explore_ruler_room.py); and the below half, which has 24
at-risk atoms at zero failures on one menu and needs an arity above
three for anything better.

STAGE FOUR, frozen after the three arms printed and before its own
engine
-------------------------------------------------------------------
Frozen against arm 3 AS FIRST PRINTED, which the bug above made wrong;
the stage is kept as written because a prediction is not rewritten
after the fact, and the corrected numbers refute it either way.

P7  If the extremes' sum is a constant of these menus, lo + hi = 7/10
    at both new targets. If it is the coverage, it reads 1/2 and 3/4.
    Any other pair kills the relation, which is the cheapest outcome
    and the one this stage is built to reach.

P8  An empty survivor set at either target is a NULL and not a
    confirmation: a relation about a set's extremes says nothing when
    there is no set. The engine prints the count first and reads the
    sum only where it is non-empty.

Both are answered above: P7 dies at both targets, and P8's null is what
coverage 1/2 returns.
"""

import os
import sys
import time
from fractions import Fraction

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_ruler_barecell import (  # noqa: E402
    exhaustive_optimum,
    operative_level,
)
from explore_ruler_abandon import (  # noqa: E402
    ALPHA,
    EQUAL,
    MENU_A,
    MENU_B,
    ROWS,
    all_optima,
    check_truth,
    make_cell,
)
from explore_ruler_family import (  # noqa: E402
    MENU_C,
    MENU_D,
    MENU_E,
    full_grid as twentieth_grid,
    score,
    KEYS,
    spread,
)

F = Fraction

ALPHA2 = F(2, 5)          # arm 3's target: nominal coverage 3/5
DEN = 40                  # the refined lattice


# ------------------------------------------------------- the weight grid

def refined_grid(den=DEN):
    """All ordered compositions of `den` into three positive parts."""
    out = []
    for a in range(1, den - 1):
        for b in range(1, den - a):
            c = den - a - b
            if c >= 1:
                out.append((F(a, den), F(b, den), F(c, den)))
    return out


GRID = refined_grid()
COARSE = set(twentieth_grid())

# The twentieth box, the object under test.
BOX_LO, BOX_HI = F(1, 4), F(9, 20)


# ------------------------------------------- arm 2: the fortieth menus

def _row(a, b, c):
    assert a + b + c == DEN, ("row does not sum to 1", a, b, c)
    assert (a % 2) + (b % 2) + (c % 2) == 2, ("row is a twentieth row"
                                              " in disguise", a, b, c)
    return [F(a, DEN), F(b, DEN), F(c, DEN)]


# Drawn blind, before any fortieth survivor list existed, from the same
# shape vocabulary the first five menus span: one spike whose top label
# can carry the target alone (>= 28/40), two intermediates, two nearly
# flat rows (top <= 17/40, the fortieth counterpart of the twentieths'
# 8/20 flats).
MENU_F = [_row(31, 5, 4), _row(23, 11, 6), _row(21, 13, 6),
          _row(15, 13, 12), _row(14, 13, 13)]
MENU_G = [_row(29, 7, 4), _row(25, 9, 6), _row(19, 15, 6),
          _row(16, 13, 11), _row(15, 14, 11)]
MENU_H = [_row(33, 5, 2), _row(27, 9, 4), _row(21, 11, 8),
          _row(15, 15, 10), _row(16, 15, 9)]
MENU_I = [_row(35, 3, 2), _row(25, 11, 4), _row(19, 17, 4),
          _row(17, 12, 11), _row(17, 13, 10)]
MENU_J = [_row(29, 9, 2), _row(23, 9, 8), _row(19, 13, 8),
          _row(17, 14, 9), _row(17, 15, 8)]

OLD = ((MENU_A, "A"), (MENU_B, "B"), (MENU_C, "C"), (MENU_D, "D"),
       (MENU_E, "E"))
NEW = ((MENU_F, "F"), (MENU_G, "G"), (MENU_H, "H"), (MENU_I, "I"),
       (MENU_J, "J"))

# The twentieth run's survivor counts, per menu group, for C3.
COARSE_COUNTS = {"AB": 42, "C": 42, "D": 24, "E": 39}


def fmt(w):
    return "(%s, %s, %s)" % tuple(str(x) for x in w)


# ------------------------------------------------------------- scoring

def sweep(weights, menus, alpha):
    """Score every (weight vector, menu, row choice) cell.

    Returns {weight vector: {counter: total}} summed over the given
    menus, plus the count of cells failing the probability-model check.
    The per-cell scorer is the family sweep's, imported rather than
    restated, so the two files cannot drift.
    """
    tally = {w: dict.fromkeys(KEYS, 0) for w in weights}
    truth_failures = 0
    for menu, tag in menus:
        for rows in ROWS:
            for w in weights:
                cell = make_cell(menu, "%s-%s" % (tag, rows), rows, w)
                if not check_truth(cell):
                    truth_failures += 1
                    continue
                level, _m, _c, _s = operative_level(cell, alpha)
                got = score(cell, level, alpha)
                row = tally[w]
                for key, val in zip(KEYS, got):
                    row[key] += val
    return tally, truth_failures


def survivors_of(tally):
    return {w for w, r in tally.items()
            if r["above_loose"] == 0 and r["below_loose"] == 0}


def sweep_checked(tag, menus, alpha, weights):
    """One menu group's sweep, refused unless it can actually refute."""
    t0 = time.time()
    tt, tr = sweep(weights, menus, alpha)
    assert tr == 0, ("C5: menu is not a probability model", tag)
    pop = sum(r["above_pop"] for r in tt.values())
    assert pop > 0, ("C5: menu puts nothing above the level", tag)
    print("      %-4s swept: at-risk above %7d, survivors %4d  (%.0f s)"
          % (tag, pop, len(survivors_of(tt)), time.time() - t0))
    return tt


# --------------------------------------------------- reading a set

def box_of(members, grid):
    """The tightest coordinate box over `members`, and whether it fits.

    Returns (lo, hi, box, missing) where box is every vector of `grid`
    inside [lo, hi] on every coordinate and missing is the vectors the
    box holds that the set does not. `members` is a box exactly when
    missing is empty.
    """
    lo = min(min(w) for w in members)
    hi = max(max(w) for w in members)
    box = {w for w in grid if all(lo <= x <= hi for x in w)}
    return lo, hi, box, box - set(members)


def rival_fits(members, grid):
    """The two neighbouring one-line descriptions, scored the same way."""
    ms = max(spread(w) for w in members)
    sp = {w for w in grid if spread(w) <= ms}
    mr = max(max(w) / min(w) for w in members)
    ra = {w for w in grid if max(w) / min(w) <= mr}
    return ((ms, len(sp), len(sp - set(members))),
            (mr, len(ra), len(ra - set(members))))


def report_set(label, members, grid):
    """Everything a survivor set owes: size, orbits, box fit, rivals."""
    print("   %s: %d of %d vectors" % (label, len(members), len(grid)))
    if not members:
        return None
    orbits = sorted({tuple(sorted(int(x * DEN) for x in w))
                     for w in members})
    print("      orbits in %dths (%d): %s"
          % (DEN, len(orbits),
             orbits if len(orbits) <= 14 else str(orbits[:14]) + " ..."))
    lo, hi, box, missing = box_of(members, grid)
    print("      tightest coordinate box [%s, %s] holds %d;"
          " IS THE SET A BOX: %s%s"
          % (lo, hi, len(box), not missing,
             "" if not missing else "  (misses %d)" % len(missing)))
    (ms, nsp, dsp), (mr, nra, dra) = rival_fits(members, grid)
    print("      rival SPREAD <= %-6s holds %4d, excess %4d"
          % (str(ms), nsp, dsp))
    print("      rival RATIO  <= %-6s holds %4d, excess %4d"
          % (str(mr), nra, dra))
    return lo, hi, box, missing


def perm_closed(members):
    for w in members:
        for p in ((w[0], w[2], w[1]), (w[1], w[0], w[2]),
                  (w[1], w[2], w[0]), (w[2], w[0], w[1]),
                  (w[2], w[1], w[0])):
            if p not in members:
                return False, (fmt(w), fmt(p))
    return True, None


def equal_mass_control(arm_name, menus, alpha):
    """C2: the equal-mass vector swept explicitly, populations printed."""
    tal, tr = sweep([EQUAL], menus, alpha)
    r = tal[EQUAL]
    print("   C2 EQUAL MASS: model failures %d; at risk ABOVE %d BELOW %d"
          " (at level %d); loose ABOVE %d BELOW %d"
          % (tr, r["above_pop"], r["below_pop"], r["at_level"],
             r["above_loose"], r["below_loose"]))
    assert r["above_pop"] > 0, ("C2 vacuous: nothing above", arm_name)
    if r["below_pop"] == 0:
        print("      BELOW HALF UNTESTED at equal mass on this arm: an"
              " empty population, not a pass.")
    return r


def below_report(label, members, tallies):
    """The other direction's denominator, per menu, for a set."""
    print("      %s below-half exposure per menu (pop/failures): %s"
          % (label, "   ".join(
              "%s %d/%d"
              % (t, sum(tallies[t][w]["below_pop"] for w in members),
                 sum(tallies[t][w]["below_loose"] for w in members))
              for t in sorted(tallies))))


# ------------------------------------------------------------ the arms

def arm(name, menus, alpha, grid):
    """One arm: five menu sweeps, their intersection, and how it reads."""
    print()
    print("=" * 68)
    print("%s" % name)
    print("   alpha = %s, nominal coverage %s, %d weight vectors"
          % (alpha, 1 - alpha, len(grid)))
    equal_mass_control(name, menus, alpha)
    tallies, sets = {}, {}
    for menu, tag in menus:
        tallies[tag] = sweep_checked(tag, ((menu, tag),), alpha, grid)
        sets[tag] = survivors_of(tallies[tag])
    final = set.intersection(*sets.values())
    print("   survivors per menu: %s"
          % ", ".join("%s %d" % (t, len(sets[t])) for t in sorted(sets)))
    ok, bad = perm_closed(final)
    print("   P6 permutation closure of the intersection: %s"
          % ("holds" if ok else "BROKEN at %s / %s -- a bug" % bad))
    fit = report_set("SURVIVING ALL FIVE", final, grid)
    if final:
        below_report("its", final, tallies)
    return tallies, sets, final, fit


def main():
    print("ARE THE BOX'S ENDPOINTS THE CONDITION'S, OR THE GRID'S?")
    print("weight lattice %dths: %d ordered compositions (%d at 20ths)"
          % (DEN, len(GRID), len(COARSE)))
    print()

    # C6 -- the new menus are new.
    old_rows = {tuple(sorted(r)) for m, _t in OLD for r in m}
    new_rows = [tuple(sorted(r)) for m, _t in NEW for r in m]
    assert len(set(new_rows)) == 25, "C6: F-J repeat a row"
    assert not (set(new_rows) & old_rows), "C6: F-J reuse a row of A-E"
    print("C6 THE NEW MENUS ARE NEW: 25 rows, all distinct, none shared"
          " with A-E (%d distinct rows there)" % len(old_rows))

    # P5 -- the menu scarcity, measured.
    flats = {tuple(sorted((a, b, DEN - a - b), reverse=True))
             for a in range(1, DEN) for b in range(1, DEN - a)
             if (a % 2) + (b % 2) + ((DEN - a - b) % 2) == 2
             and max(a, b, DEN - a - b) <= 17}
    print("P5 FRESH NEARLY FLAT ROWS the %dth lattice offers (top <= 17/%d,"
          " not a %dth row): %d" % (DEN, DEN, DEN // 2, len(flats)))
    print()

    agree = total = 0
    for menu in (MENU_A, MENU_B):
        for rows in ROWS:
            cell = make_cell(menu, "parity", rows, EQUAL)
            ref = exhaustive_optimum(cell, ALPHA)
            if ref is None:
                continue
            total += 1
            best, _a = all_optima(cell, ALPHA)
            agree += (best == ref)
    print("C1 PARITY (equal-mass arm, menus A and B): %d/%d agree"
          % (agree, total))
    assert agree == total, "optimum enumerator disagrees with the library"

    tal1, set1, final1, fit1 = arm(
        "ARM 1 -- the weight lattice alone, menus A-E unchanged",
        OLD, ALPHA, GRID)

    # C4 containment, over every arm-1 vector and menu.
    for tag, tt in tal1.items():
        for w, r in tt.items():
            assert r["above_loose"] >= r["above_forced"], ("C4", tag, w)
            assert r["below_loose"] >= r["below_forced"], ("C4", tag, w)
    print("   C4 CONTAINMENT holds at all %d vectors on all five menus"
          % len(GRID))

    # C3 reproduction of the twentieth run. The control rests on the
    # refined grid CONTAINING the old one, which is asserted and not
    # assumed: a refinement that dropped a vector would make the
    # reproduction read on a different population than the one it names.
    assert COARSE <= set(GRID), "the refined grid does not contain the old"
    print("   C3 REPRODUCTION on the %d even-numerator vectors"
          " (subset of the grid, asserted):" % len(COARSE))
    ab = {w for w in COARSE
          if tal1["A"][w]["above_loose"] + tal1["A"][w]["below_loose"]
          + tal1["B"][w]["above_loose"] + tal1["B"][w]["below_loose"] == 0}
    print("      A+B %d (expect %d)" % (len(ab), COARSE_COUNTS["AB"]))
    for t in ("C", "D", "E"):
        print("      %s   %d (expect %d)"
              % (t, len(set1[t] & COARSE), COARSE_COUNTS[t]))
    coarse_final = final1 & COARSE
    coarse_box = {w for w in COARSE
                  if all(BOX_LO <= x <= BOX_HI for x in w)}
    print("      five-menu intersection over the old grid: %d, and it is"
          " the old box (%d vectors) exactly: %s"
          % (len(coarse_final), len(coarse_box),
             coarse_final == coarse_box))

    # P1/P2 -- the box, tested as set equality.
    box = {w for w in GRID if all(BOX_LO <= x <= BOX_HI for x in w)}
    print()
    print("   P1 THE BOX [1/4, 9/20] over the refined grid holds %d"
          " vectors" % len(box))
    print("      IS THE FIVE-MENU SURVIVOR SET EXACTLY THAT BOX: %s"
          % (final1 == box))
    if final1 != box:
        print("      survivors outside the box: %d;  box members that"
              " failed: %d" % (len(final1 - box), len(box - final1)))
        for w in sorted(final1 - box)[:8]:
            print("         outside: %s" % fmt(w))
        for w in sorted(box - final1)[:8]:
            print("         failed : %s" % fmt(w))
    print("      equal mass 1/3 strictly inside the box: %s"
          % (BOX_LO < F(1, 3) < BOX_HI))
    if final1 == box:
        print("      P2 THE READING: the endpoints are now known only to"
              " lie in (%s, %s] and [%s, %s) -- a hold NARROWS each"
              " window to 1/%d and proves nothing about 1/4 or 9/20."
              % (F(9, DEN), BOX_LO, BOX_HI, F(19, DEN), DEN))

    tal2, set2, final2, fit2 = arm(
        "ARM 2 -- the posterior lattice, five blind %dth menus F-J" % DEN,
        NEW, ALPHA, GRID)
    print("   P3 against arm 1: intersection %d; arm 1 members lost %d;"
          " gained %d"
          % (len(final1 & final2), len(final1 - final2),
             len(final2 - final1)))
    print("      what an unrelated set of that size would give: %.1f"
          % (len(final1) * len(final2) / float(len(GRID))))

    tal3, set3, final3, fit3 = arm(
        "ARM 3 -- the target moved to 3/5, menus A-E", OLD, ALPHA2, GRID)
    pred = {w for w in GRID if all(F(1, 5) <= x <= F(2, 5) for x in w)}
    print("   P4 the relation lo+hi = coverage and hi-lo = 1/5 predicts"
          " [1/5, 2/5], %d vectors" % len(pred))
    print("      IS THE SURVIVOR SET EXACTLY THAT: %s" % (final3 == pred))
    print("      the CONSTANT rival [1/4, 9/20] instead: %s"
          % (final3 == box))
    if fit3:
        lo3, hi3 = fit3[0], fit3[1]
        print("      as measured: lo %s, hi %s, lo+hi %s (coverage %s),"
              " hi-lo %s" % (lo3, hi3, lo3 + hi3, 1 - ALPHA2, hi3 - lo3))

    # ------------------------------------------------------ stage four
    print()
    print("=" * 68)
    print("STAGE FOUR -- the extremes' sum at two further targets")
    print("   the sum so far: arm1 %s, arm2 %s, arm3 %s"
          % (fit1[0] + fit1[1] if fit1 else None,
             fit2[0] + fit2[1] if fit2 else None,
             fit3[0] + fit3[1] if fit3 else None))
    for a4 in (F(1, 2), F(1, 4)):
        _t, _s, f4, fit4 = arm(
            "STAGE FOUR -- coverage %s, menus A-E" % (1 - a4), OLD, a4,
            GRID)
        if not f4:
            print("   P8 NULL at coverage %s: no survivor, so the"
                  " relation is not read here" % (1 - a4))
            continue
        lo4, hi4 = fit4[0], fit4[1]
        print("   P7 at coverage %s: lo %s, hi %s, lo+hi %s"
              % (1 - a4, lo4, hi4, lo4 + hi4))
        print("      the CONSTANT reading 7/10: %s;  the COVERAGE"
              " reading %s: %s" % (lo4 + hi4 == F(7, 10), 1 - a4,
                                   lo4 + hi4 == 1 - a4))


if __name__ == "__main__":
    main()
