"""Is equal mass the boundary of the abandonment condition, or only the
boundary that happened to get named?

THE QUESTION
------------
On a bare cell -- a finite set of atoms, each carrying a mass and a
posterior row over labels -- the marginal-coverage optimum is the
cheapest rule reaching a nominal coverage on average. At EQUAL masses
that optimum has an exact shape: pairs enter in order of posterior, so
an atom is abandoned precisely when its best label's posterior falls
below the operative level, max_y p(y|r) < t*. The derivation is the
equal-weight one -- every label costs the same, so the increment greedy
is exactly optimal -- and off equal masses the condition is not a law:
both directions have exact counterexamples, atoms above the level that
every optimum abandons and atoms below it that every optimum serves.

What nobody has asked is whether equal mass is the WIDEST sufficient
condition. The derivation needs every label to cost the same, which is
a statement about the weights, so a wider family of weight vectors
carrying the condition would be a derivation and not a census. This
file asks whether such a family shows up in the designed sweep at all.

THE CONFOUND, and it is the reason a count of clean weight vectors
decides nothing on its own: a weight vector can score zero failures
because it never puts an atom AT RISK. A failure needs an atom strictly
ABOVE the level for some optimum to drop, or one strictly BELOW it for
some optimum to buy. A vector whose geometry produces neither scores a
clean zero while saying nothing about the condition. The mechanism is
concrete and is expected here: where one atom is heavy enough that its
own spike carries the target alone, the operative level lands on the
largest posterior value in the cell, so NO atom sits strictly above it
and the above-half antecedent is empty. So every count in this file is
printed against its own denominator -- how many atoms were at risk on
each half -- and a vector's zero is read only where that denominator is
non-zero.

THE DESIGN
----------
The arms, the menus and the cells are the abandonment sweep's, imported
rather than restated: two five-row posterior menus (an inherited one
whose rows all peak high enough that the below-level antecedent is
unreachable, and a designed one pairing spikes that can carry the target
alone against nearly flat rows that then sit wholly under the level),
crossed with all 125 ordered choices of three rows. Nominal coverage
7/10 throughout. Everything is exact rational arithmetic.

What is NEW here is the aggregation and the grid:

  * AGGREGATION BY WEIGHT VECTOR, not by arm. The abandonment sweep
    reports one pair of failure counts per arm over all weight vectors
    at once, which cannot see a family. Here every atom of every cell is
    charged to the weight vector that scored it, and each vector carries
    four numbers per half: the population at risk and the failures
    inside it, on both the LOOSE criterion (some optimum breaks the half)
    and the FORCED one (every optimum does).

  * THE LOOSE CRITERION DECIDES. A claim that a family SATISFIES the
    condition is a claim about the complement of the failure set: an
    atom abandoned in one optimum and served in another already denies
    the condition its claim to DETERMINE a fate, even though it is not a
    forced failure. So a vector SURVIVES only with zero LOOSE failures
    on both halves. The forced counters ride along for one purpose, to
    reproduce the abandonment sweep's published figures as a control.

  * THE FULL WEIGHT GRID. The abandonment sweep's grid holds 153 of the
    171 ordered compositions of 20 into three positive parts: its loop
    bound leaves the third coordinate at least 2/20, so every vector
    with a 1/20 in the last position is missing and the grid is not
    closed under permutation. For an arm-level failure count that is
    simply a designed sweep. For a question about a FAMILY it is not:
    the missing vectors sit on the boundary where vacuity is likeliest,
    and permutation-closure is the cheapest bug check this design has,
    since permuting a weight vector permutes the atoms of a cell family
    the row enumeration already covers whole. So the grid here is all
    171, and the 153-subset totals print beside them.

THE PREDICTIONS, frozen before the engine
-----------------------------------------
P1  The equal-mass vector scores ZERO loose failures on both halves.
    Its above-half population is non-zero. Its below-half population is
    NOT predicted: at three atoms the abandonment sweep had to go to
    eight equal atoms before a flat atom sat under the level at all, so
    a zero below-population here means the below half is untested at
    equal mass at this arity, and that is what gets said -- it is not
    read as a pass. The run asserts the above-half population is
    non-empty before any survivor verdict is read.

P2  Survivors exist off the diagonal: at least 20 of the 171 vectors
    carry zero loose failures across both arms.

P3  The confound bites, and hard: most survivors are VACUOUS on at
    least one half, and the largest single group is survivors with an
    above-half population of exactly ZERO -- the heavy-spike vectors,
    where the level lands on the cell's largest posterior value.

P4  CREDIBLE survivors -- zero loose failures with BOTH populations
    non-zero -- are few, 0 to 5 of the 171; and any that exist lie near
    the diagonal, spread max(w) - min(w) at most 3/20. If that holds,
    the wider family is a TOLERANCE around equal mass and not a
    structure: a census, and the derivation stays where it is. The
    prediction worth refuting is exactly this one -- a credible survivor
    far from the diagonal would be a proof target.

P5  The survivor set is closed under permutation of the weight vector.
    A violation is a BUG in the scoring or the grid, not a finding.

STAGE TWO, frozen after stage one printed and before its own engine
-------------------------------------------------------------------
A set of weight vectors that scores clean on two menus is a CANDIDATE
family and not yet a family: the two menus here were designed as one
pair, sharing a construction and much of their row vocabulary, so a
survivor set could belong to that geometry rather than to the weights.
The question has one decisive cheap test, and it is the difference
between a proof target and a census.

A THIRD MENU, drawn BLIND -- chosen before any survivor list was read
against it, from the same shape vocabulary the first two span (one
spike that can carry the target alone, two intermediates, two nearly
flat rows) and sharing no row with either. The survivor test is re-run
on that menu alone and the two survivor sets are intersected.

P6  If the survivor set is a property of the WEIGHTS, its members
    survive the third menu too: the intersection is most of it, and a
    derivation is worth hunting. If it is a census of the first two
    menus' geometry, the third menu's survivor set is largely disjoint
    and the intersection falls toward what an unrelated set of that
    size would give. The prediction registered here is the FAMILY one:
    at least half the first survivor set survives the third menu.

STAGE THREE, frozen after stage two printed and before its own engine
---------------------------------------------------------------------
Stage two read 24 survivors in common against 10.3 for an unrelated set
and called the set a census on the strength of the 18 that swapped. That
reading has a blind spot: 24 against 10.3 is 2.3 times chance, so the
CORE may be the real object and the 18 the noise. Two further menus,
drawn blind, decide it.

P7  If the survivor set is a census artifact, the core erodes in
    proportion on each further menu -- 24 down to roughly 12 to 16, and
    less again on the fifth. If a family is in there, the core holds at
    or near 24 on both.

THE CONTROLS
------------
C1  PARITY. This file's optimum-cost enumerator agrees with the bare
    cell library's independent exhaustive optimum at every cell of the
    equal-mass arm, both menus.

C2  THE CONTROL IS NOT VACUOUS. The equal-mass vector is swept
    explicitly and its at-risk populations are printed and asserted
    non-empty on the above half before any survivor list is read. (The
    trap this guards is the one that catches a control built from a
    grid that holds no equal-mass vector at all: the check then runs
    over an empty population and reads as a pass.)

C3  REPRODUCTION. Restricted to the 153-vector subset and the two
    unequal arms, the FORCED failure totals must equal the abandonment
    sweep's published figures exactly -- 3,154 above-level atoms
    abandoned in every optimum and 24 below-level atoms served in every
    optimum. A mismatch means the aggregation, not the physics, moved.

C4  CONTAINMENT. At every weight vector and on both halves, the loose
    failure count is at least the forced one, by construction.

C5  THE THIRD MENU IS A MENU. Every cell it builds passes the same
    probability-model check, and it reaches a non-empty above-half
    population -- a third menu that put nothing at risk would hand back
    a survivor set of everything and refute nothing.

TWO MEASUREMENTS NOT FROZEN WITH THE PREDICTIONS, asked once stage one
had printed, and printed here because a rate needs its denominator: the
DISTRIBUTION of loose failure counts over the grid, which says whether
zero is a mode or the end of a tail, and the grid-wide above-half
failure RATE, which is the base rate a zero has to beat.

Runtime is seconds; memory is a few megabytes of Fractions.

WHAT RAN
--------
One run, 36 s, a few megabytes. 171 weight vectors x 250 cells on the
first two menus and x 125 on each of the third, fourth and fifth, plus
the equal-mass vector on 250 cells. All four stage-one controls pass:
the optimum enumerator agrees with the library at 250/250 equal-mass
cells; no cell fails the probability-model check anywhere; loose
contains forced at all 171 vectors; and, restricted to the 153-vector
subset, the forced totals reproduce the abandonment sweep's published
3,154 above and 24 below EXACTLY. The third menu passes C5: 0 model
failures and 61,557 at-risk atoms above the level. P5 holds -- the
survivor set is closed under permutation of the weight vector, on a grid
that is itself closed only because this file swept all 171 compositions
rather than the 153.

WHAT IT FOUND
-------------
EQUAL MASS IS NOT THE ONLY VECTOR THE SWEEP LEAVES CLEAN -- and the
distinction is the whole of the tier. Equal mass carries a DERIVATION;
these vectors carry only a finite sweep that failed to refute them, which
is a weaker thing and which stage two then breaks for 18 of them.
42 of the 171 unequal weight vectors
carry ZERO loose failures across both designed menus, and their zeros
are not vacuous: every one of the 42 has an above-half at-risk
population between 648 and 670 atoms, against a grid-wide above-half
failure rate of 5,706 in 110,286 = 5.17%. A vector scoring zero over
~660 at-risk atoms is not what that rate delivers by chance. Nor are
they huddled around the diagonal: the survivor multisets in twentieths
are (6,7,7), (6,6,8), (5,7,8), (5,6,9), (3,8,9), (3,7,10), (3,5,12)
and (3,4,13), spreads running from 1/20 out to 1/2.

AND THE CONFOUND THE DESIGN WAS BUILT TO KILL DIED ON THE ABOVE HALF
AND WON ON THE BELOW. Not one survivor is vacuous above. Every single
one is vacuous BELOW: at three atoms no cell of these menus puts an
atom strictly under the level for any of the 42, and the EQUAL-MASS
CONTROL IS VACUOUS THERE TOO -- 660 at-risk atoms above the level, 0
below. So the below half of the condition is untested at equal mass at
this arity, and every statement here is about the ABOVE half alone.
(93 of the 171 vectors do reach a non-empty below population, 888 atoms
carrying 78 loose failures between them; none of those 93 survives.)

THE SURVIVOR SET IS MENU-DEPENDENT, AND THAT IS THE ANSWER TO WHETHER
IT IS A FAMILY. On the third menu, drawn blind, the survivor count is
again 42 -- and the intersection with the first set is 24, against the
10.3 an unrelated set of that size would give. P6 asked for at least
half and got 24 of 42, so its threshold passed; but the same three
numbers refute the reading it was testing for 18 of the 42, which fail
the third menu (by 1, 4 and 6 atoms), while 18 vectors the first two
menus rejected come through clean. A set that keeps its size and
swaps 43% of its members with the menu is a CENSUS of the geometry,
not a property of the weights.

WHAT SURVIVES ALL THREE MENUS is a core of 24 vectors, five permutation
orbits: (6,7,7), (6,6,8), (5,7,8), (5,6,9) and (3,7,10) in twentieths.
It is not ordered by spread -- (3,8,9) dies on the third menu while the
wider (3,7,10) lives. Stage three takes this further and changes what it
means.

THE TIERS. That equal mass is not the widest clean condition at this
arity is an OBSERVATION over a designed sweep, exhaustive in its own
range: 3-atom cells, three 5-row menus, coverage 7/10, weights in
twentieths. It is not a rule and it is nowhere near a proof -- no
derivation covers any vector off the diagonal, and the census reading
is the one the third menu supports. The 24-vector core is a CANDIDATE
and its stability rests on three menus.

STAGE THREE REFUTES P7, AND WITH IT THIS FILE'S OWN CENSUS VERDICT. The
fourth menu returns 24 survivors and they are EXACTLY the core -- 24 of
24, nothing lost and nothing gained. The fifth returns 39 and keeps 18 of
the core. The set surviving all FIVE menus is 18 vectors, four
permutation orbits, (6,7,7), (6,6,8), (5,7,8) and (5,6,9) in twentieths.

AND THAT SET IS NOT A LIST -- IT IS A BOX. The 18 are EXACTLY the weight
vectors whose every coordinate lies in [1/4, 9/20], tested as set
equality against the box and not read off the orbits, and equal mass 1/3
lies strictly inside it. So the census verdict was right about the 42 and
wrong about what the 42 contains: three blind menus cut it to a region
with a one-line description that no census would land on, and the region
contains the one vector the condition is PROVED at.

WHAT THE BOX IS AND IS NOT. It is a PROOF TARGET at this arity, not a
law and not a family yet. Nothing here derives it; the endpoints 1/4 and
9/20 are the coarsest the twentieth grid can express, and whether they
are the condition's own endpoints or an artifact of that grid is the
cheapest next question -- the same sweep at fortieths would move them or
hold them. (SETTLED, and against this file: explore_ruler_box.py runs
that sweep and the endpoints are the GRID's. Every box member survives
at fortieths, 30 further vectors survive outside it, and the clean set
there is not a box at all -- the vectors breaking the shape are exactly
the ones a twentieth lattice cannot write. What survives of this file
is its counts at its own grid, which that sweep reproduces to the
vector; the box, the proof target and the endpoint question do not.
That file also finds the criterion scored here to be stronger than the
proved law, and failed by equal mass itself at two of the four coverage
targets swept -- though not at this file's own 7/10.)
And the box is evidence on the ABOVE half ALONE: its members
meet no below-level atom on any of the five menus. The claim that no
clean vector anywhere meets one is FALSE and stage three is what
refutes it -- on the fourth menu, clean vectors outside the box carry 24
at-risk below-level atoms between them and take zero failures on them.

WHAT THIS LEAVES OPEN: what the core's five orbits share; whether the
below half can be exercised by a clean vector at all above three atoms,
which is the only way to test the condition's other direction on a
candidate family; and whether the survivor line is a wall or a knife
edge -- the distribution of loose failures over the grid runs
0:42, 1:12, 2:6, then 6 and up, so 18 vectors sit within two atoms of
clean out of ~660 at risk.
"""

import os
import sys
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
    WEIGHTS,
    all_optima,
    check_truth,
    make_cell,
)

F = Fraction


# ------------------------------------------------------- the weight grid

def full_grid():
    """All ordered compositions of 20 into three positive twentieths."""
    out = []
    for a in range(1, 19):
        for b in range(1, 20 - a):
            c = 20 - a - b
            if c >= 1:
                out.append((F(a, 20), F(b, 20), F(c, 20)))
    return out


FULL = full_grid()
PARENT = set(WEIGHTS)

# The third menu, drawn blind: a spike that can carry the target alone,
# two intermediates and two nearly flat rows, sharing no row with either
# of the first two menus.
MENU_C = [
    [F(15, 20), F(3, 20), F(2, 20)],
    [F(13, 20), F(5, 20), F(2, 20)],
    [F(11, 20), F(6, 20), F(3, 20)],
    [F(9, 20), F(7, 20), F(4, 20)],
    [F(8, 20), F(7, 20), F(5, 20)],
]


# ------------------------------------------------------------- scoring

def score(cell, level, alpha=ALPHA):
    """One cell's atoms, split by half and charged with their failures.

    Returns (above_pop, below_pop, at_level, above_loose, below_loose,
    above_forced, below_forced). An atom is ABOVE the half's antecedent
    when its best posterior is strictly greater than `level` and BELOW
    when strictly less; equality is the indifference band and belongs to
    neither population. An above-level atom fails LOOSELY when SOME
    optimum abandons it and FORCEDLY when every optimum does; a
    below-level atom fails loosely when some optimum serves it and
    forcedly when every optimum does.

    The optima are taken at `alpha`, which defaults to this file's own
    target. A caller sweeping a DIFFERENT target must pass it: the level
    and the optima have to come from the same program, and a scorer
    reading the level from its argument and the optima from a module
    global will silently mix two targets and print a clean-looking
    table.
    """
    _best, arg = all_optima(cell, alpha)
    # An infeasible cell would leave arg empty, where `all` is vacuously
    # true and `any` is false -- forced without loose, which C4 would
    # then trip. No cell here is infeasible; the invariant is asserted
    # rather than left to the control.
    assert arg, ("no feasible rule", cell.name)
    above_pop = below_pop = at_level = 0
    above_loose = below_loose = above_forced = below_forced = 0
    for r in range(cell.M):
        top = max(cell.posterior(r))
        if top == level:
            at_level += 1
        elif top < level:
            below_pop += 1
            if any(sizes[r] > 0 for sizes in arg):
                below_loose += 1
                if all(sizes[r] > 0 for sizes in arg):
                    below_forced += 1
        else:
            above_pop += 1
            if any(sizes[r] == 0 for sizes in arg):
                above_loose += 1
                if all(sizes[r] == 0 for sizes in arg):
                    above_forced += 1
    return (above_pop, below_pop, at_level, above_loose, below_loose,
            above_forced, below_forced)


KEYS = ("above_pop", "below_pop", "at_level", "above_loose", "below_loose",
        "above_forced", "below_forced")


# Two more menus, drawn blind for the stage-three probe. D shares no
# row with A, B or C. E's flat row (8,8,4) is menu A's
# -- it is the only nearly flat three-label row in twentieths not already
# spent, which is a fact about the grid and is stated rather than hidden.
MENU_D = [
    [F(17, 20), F(2, 20), F(1, 20)],
    [F(13, 20), F(4, 20), F(3, 20)],
    [F(11, 20), F(7, 20), F(2, 20)],
    [F(10, 20), F(5, 20), F(5, 20)],
    [F(9, 20), F(6, 20), F(5, 20)],
]
MENU_E = [
    [F(16, 20), F(3, 20), F(1, 20)],
    [F(14, 20), F(3, 20), F(3, 20)],
    [F(12, 20), F(6, 20), F(2, 20)],
    [F(10, 20), F(7, 20), F(3, 20)],
    [F(8, 20), F(8, 20), F(4, 20)],
]

PAIR = ((MENU_A, "A"), (MENU_B, "B"))
THIRD = ((MENU_C, "C"),)
FOURTH = ((MENU_D, "D"),)
FIFTH = ((MENU_E, "E"),)

BOX_LO, BOX_HI = F(5, 20), F(9, 20)


def survivors_of(tally):
    return {w for w, r in tally.items()
            if r["above_loose"] == 0 and r["below_loose"] == 0}


def sweep_checked(tag, menus):
    """A menu's sweep, refused unless the menu can actually refute."""
    tt, tr = sweep(FULL, menus)
    assert tr == 0, ("menu is not a probability model", tag)
    assert sum(r["above_pop"] for r in tt.values()) > 0, ("vacuous", tag)
    return tt


def sweep(weights, menus=PAIR):
    """Score every (weight vector, menu, row choice) cell.

    Returns {weight vector: {counter: total}} summed over the given
    menus, plus the count of cells that failed the probability-model
    check.
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
                level, _m, _c, _s = operative_level(cell, ALPHA)
                got = score(cell, level)
                row = tally[w]
                for key, val in zip(KEYS, got):
                    row[key] += val
    return tally, truth_failures


# ------------------------------------------------------------ controls

def control_parity():
    """C1: the local enumerator against the library's exhaustive cost."""
    agree = total = 0
    for menu in (MENU_A, MENU_B):
        for rows in ROWS:
            cell = make_cell(menu, "parity", rows, EQUAL)
            ref = exhaustive_optimum(cell, ALPHA)
            if ref is None:
                continue
            total += 1
            best, _arg = all_optima(cell, ALPHA)
            agree += (best == ref)
    return agree, total


def spread(w):
    return max(w) - min(w)


def fmt(w):
    return "(%s, %s, %s)" % tuple(str(x) for x in w)


# ------------------------------------------------------------- reporting

def main():
    print("IS EQUAL MASS THE BOUNDARY, OR ONLY THE BOUNDARY WE NAMED?")
    print("alpha = %s, nominal coverage %s, 3-atom cells, two 5-row menus"
          % (ALPHA, 1 - ALPHA))
    print("weight grid: %d ordered compositions of 20 into three positive"
          " parts" % len(FULL))
    print("             %d of them are the abandonment sweep's own grid"
          % len(PARENT))
    print()

    agree, total = control_parity()
    print("C1 PARITY (equal-mass arm, both menus) : %d/%d agree"
          % (agree, total))
    assert agree == total, "optimum enumerator disagrees with the library"
    print()

    eq_tally, eq_truth = sweep([EQUAL])
    eq = eq_tally[EQUAL]
    print("C2 THE EQUAL-MASS CONTROL -- swept explicitly, %d cells"
          % (2 * len(ROWS)))
    print("   probability-model failures : %d" % eq_truth)
    print("   at-risk population   ABOVE %4d   BELOW %4d   (at level %4d)"
          % (eq["above_pop"], eq["below_pop"], eq["at_level"]))
    print("   loose failures       ABOVE %4d   BELOW %4d"
          % (eq["above_loose"], eq["below_loose"]))
    print("   forced failures      ABOVE %4d   BELOW %4d"
          % (eq["above_forced"], eq["below_forced"]))
    assert eq["above_pop"] > 0, "vacuous control: no atom above the level"
    if eq["below_pop"] == 0:
        print("   BELOW HALF UNTESTED AT EQUAL MASS: no atom of any cell")
        print("   sits strictly under the level at three equal atoms, so")
        print("   its zero is an empty population and not a pass.")
    print()

    tally, truth = sweep(FULL)
    print("THE SWEEP: %d weight vectors x %d cells, model failures %d"
          % (len(FULL), 2 * len(ROWS), truth))

    for w, row in tally.items():
        assert row["above_loose"] >= row["above_forced"], ("C4", w)
        assert row["below_loose"] >= row["below_forced"], ("C4", w)
    print("C4 CONTAINMENT (loose >= forced, both halves) : holds at all"
          " %d vectors" % len(tally))

    par_above = sum(r["above_forced"] for w, r in tally.items()
                    if w in PARENT)
    par_below = sum(r["below_forced"] for w, r in tally.items()
                    if w in PARENT)
    print("C3 REPRODUCTION over the %d-vector subset: forced ABOVE %d"
          " (expect 3154), forced BELOW %d (expect 24)"
          % (len(PARENT), par_above, par_below))
    print()

    survivors = [w for w, r in tally.items()
                 if r["above_loose"] == 0 and r["below_loose"] == 0]
    credible = [w for w in survivors
                if tally[w]["above_pop"] > 0 and tally[w]["below_pop"] > 0]
    vac_above = [w for w in survivors if tally[w]["above_pop"] == 0]
    vac_below = [w for w in survivors if tally[w]["below_pop"] == 0]
    print("SURVIVORS -- zero LOOSE failures on both halves")
    print("   survivors            : %d of %d" % (len(survivors), len(FULL)))
    print("   of which above-half population EMPTY : %d" % len(vac_above))
    print("   of which below-half population EMPTY : %d" % len(vac_below))
    print("   CREDIBLE (both populations non-empty): %d" % len(credible))
    print("   in the %d-vector subset               : %d survivors, %d"
          " credible"
          % (len(PARENT), sum(1 for w in survivors if w in PARENT),
             sum(1 for w in credible if w in PARENT)))
    print()

    print("EVERY SURVIVOR, with its denominators")
    print("   %-22s %6s %6s %6s %8s" % ("weights", "above", "below",
                                        "atlvl", "spread"))
    for w in sorted(survivors, key=lambda v: (-tally[v]["above_pop"],
                                              -tally[v]["below_pop"], v)):
        r = tally[w]
        print("   %-22s %6d %6d %6d %8s%s"
              % (fmt(w), r["above_pop"], r["below_pop"], r["at_level"],
                 str(spread(w)), "" if w in PARENT else "   [off-grid]"))
    print()

    print("THE NON-SURVIVORS' FLOOR -- the smallest loose failure counts")
    print("among vectors that DO fail, which says how close the survivor")
    print("line is to being a threshold rather than a wall")
    losers = sorted(((tally[w]["above_loose"] + tally[w]["below_loose"], w)
                     for w in tally if w not in set(survivors)))
    for n, w in losers[:8]:
        r = tally[w]
        print("   %-22s loose %4d (above %3d of %3d, below %3d of %3d)"
              % (fmt(w), n, r["above_loose"], r["above_pop"],
                 r["below_loose"], r["below_pop"]))
    print()

    perm_ok = True
    surv = set(survivors)
    for w in surv:
        for p in ((w[0], w[2], w[1]), (w[1], w[0], w[2]),
                  (w[1], w[2], w[0]), (w[2], w[0], w[1]),
                  (w[2], w[1], w[0])):
            if p not in surv:
                perm_ok = False
                print("   P5 VIOLATED: %s survives, %s does not"
                      % (fmt(w), fmt(p)))
    print("P5 PERMUTATION CLOSURE of the survivor set : %s"
          % ("holds" if perm_ok else "BROKEN -- treat as a bug"))

    if credible:
        print()
        print("THE CREDIBLE SURVIVORS -- the only rows that bear on the")
        print("question, printed whole")
        for w in sorted(credible, key=lambda v: (spread(v), v)):
            r = tally[w]
            print("   %-22s spread %-6s above-pop %4d  below-pop %4d"
                  % (fmt(w), str(spread(w)), r["above_pop"], r["below_pop"]))
    print()

    # --- the two measurements asked after stage one printed ---
    hist = {}
    for r in tally.values():
        n = r["above_loose"] + r["below_loose"]
        hist[n] = hist.get(n, 0) + 1
    tot_loose = sum(r["above_loose"] for r in tally.values())
    tot_pop = sum(r["above_pop"] for r in tally.values())
    print("THE DISTRIBUTION of total loose failures over the %d vectors"
          % len(FULL))
    print("   " + "  ".join("%d:%d" % (n, hist[n])
                            for n in sorted(hist)[:12]) + "  ...  max %d"
          % max(hist))
    print("   grid-wide ABOVE-half failure rate: %d of %d at-risk atoms"
          " = %.2f%%" % (tot_loose, tot_pop, 100.0 * tot_loose / tot_pop))
    print("   vectors with a non-empty BELOW-half population : %d of %d"
          % (sum(1 for r in tally.values() if r["below_pop"] > 0),
             len(FULL)))
    print()

    # ------------------------------------------------------- stage two
    print("=" * 62)
    print("STAGE TWO -- the same test on a third menu, drawn blind")
    c_tally, c_truth = sweep(FULL, THIRD)
    c_pop = sum(r["above_pop"] for r in c_tally.values())
    print("C5 THE THIRD MENU IS A MENU: model failures %d, at-risk"
          " above-half atoms %d" % (c_truth, c_pop))
    assert c_truth == 0 and c_pop > 0, "third menu puts nothing at risk"

    c_surv = set(w for w, r in c_tally.items()
                 if r["above_loose"] == 0 and r["below_loose"] == 0)
    both = surv & c_surv
    print("   survivors on the first two menus : %d of %d"
          % (len(surv), len(FULL)))
    print("   survivors on the third menu      : %d of %d"
          % (len(c_surv), len(FULL)))
    print("   INTERSECTION                     : %d" % len(both))
    print("   what an unrelated set of that size would give:"
          " %.1f" % (len(surv) * len(c_surv) / float(len(FULL))))
    print()
    print("   the first set's members, scored on the third menu")
    print("   %-22s %6s %6s %6s" % ("weights", "above", "below", "loose"))
    for w in sorted(surv, key=lambda v: (c_tally[v]["above_loose"]
                                         + c_tally[v]["below_loose"], v)):
        r = c_tally[w]
        print("   %-22s %6d %6d %6d%s"
              % (fmt(w), r["above_pop"], r["below_pop"],
                 r["above_loose"] + r["below_loose"],
                 "   [survives]" if w in c_surv else ""))
    print()
    print("   the third menu's OWN survivors not in the first set : %d"
          % len(c_surv - surv))
    for w in sorted(c_surv - surv)[:12]:
        print("      %-22s spread %s" % (fmt(w), str(spread(w))))
    print()

    # ----------------------------------------------------- stage three
    print("=" * 62)
    print("STAGE THREE -- two further blind menus, and what the census")
    print("cuts DOWN TO")
    sets = {"A+B": surv, "C": c_surv}
    tals = {"A+B": tally, "C": c_tally}
    for tag, menus in (("D", FOURTH), ("E", FIFTH)):
        tals[tag] = sweep_checked(tag, menus)
        sets[tag] = survivors_of(tals[tag])
    order = ("A+B", "C", "D", "E")
    final = set.intersection(*sets.values())
    print("   survivors per menu : %s"
          % ", ".join("%s %d" % (t, len(sets[t])) for t in order))
    print("   surviving ALL FIVE : %d" % len(final))
    box = {w for w in FULL if all(BOX_LO <= x <= BOX_HI for x in w)}
    print("   the box [1/4, 9/20] on every coordinate holds %d vectors"
          % len(box))
    print("   THE FIVE-MENU SURVIVOR SET IS EXACTLY THAT BOX : %s"
          % (final == box))
    print("   equal mass 1/3 lies strictly inside it : %s"
          % (BOX_LO < F(1, 3) < BOX_HI))
    print("   its orbits, in twentieths: %s"
          % sorted({tuple(sorted(int(x * 20) for x in w)) for w in final}))
    print("   the box's BELOW-half population per menu, against every")
    print("   survivor's -- 0 means the other direction is never")
    print("   exercised for the box, and the last column shows a menu")
    print("   where it IS exercised for clean vectors outside it:")
    for t in order:
        print("      %-4s box below-pop %3d, box below-failures %3d,"
              "  all survivors' below-pop %3d"
              % (t, sum(tals[t][w]["below_pop"] for w in final),
                 sum(tals[t][w]["below_loose"] for w in final),
                 sum(tals[t][w]["below_pop"] for w in sets[t])))


if __name__ == "__main__":
    main()
