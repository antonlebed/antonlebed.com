"""WHAT REPLACES THE ABANDONED ATOM'S THRESHOLD -- the LP dual, and
whether any per-atom predicate can exist at all.

THE QUESTION. explore_ruler_abandon.py leaves an open front. The
condition deciding whether a subgroup gets the empty set --

    r is abandoned exactly when max_y p(y|r) < t*

-- is EQUAL-WEIGHT-ONLY: off equal masses both directions have exact
counterexamples, 3,154 above-level atoms abandoned in every optimum and
24 below-level atoms served in every optimum over a 38,500-cell sweep.
What replaces it is open, and three readings of "the subgroup's mass
against the coverage still owed" are already refuted. This file does
not mint a fourth guess. It asks the two questions that sit
UNDER the guessing.

THE PROGRAM, restated so the dual is available. Minimize E|H| subject to
marginal coverage >= 1-alpha. The problem is separable over (atom,
label) PAIRS: pair (r, y) costs w_r and covers w_r * p(y|r). So it is a
0/1 knapsack whose ratio is p(y|r) with the weight cancelled, which is
exactly why the RANKING survives unequal weights and only INTEGRALITY
breaks. The LP relaxation is solved by the threshold rule itself --
take every pair strictly above t*, then a FRACTION of the tied block --
so every failure of the condition is an integrality correction to the
relaxation, and the object the relaxation hands us for reading those
corrections is the DUAL PRICE.

THE DUAL. With a single covering constraint the dual price is
lambda = 1/t*, and the reduced cost of a pair is

    rc(r, y) = w_r - lambda * w_r * p(y|r) = w_r * (t* - p(y|r)) / t*

which is negative strictly above the level, zero on the tied block, and
positive strictly below it. Two things follow and the first is checked
before anything is read off the second.

  * AN EXACT IDENTITY. Writing s for the OVERSHOOT (coverage delivered
    minus the target), the cost of ANY feasible rule is

        cost = lambda * (1 - alpha)  +  lambda * s  +  sum_selected rc

    -- the LP price of the target, plus the price of overshooting it,
    plus the reduced costs of what was bought. This is a rearrangement
    and not an approximation, so it is an ARITHMETIC control (C-LAG)
    on the whole dual construction rather than a finding.
  * RC CARRIES BOTH COORDINATES. The threshold condition reads the
    posterior alone; rc reads w_r * (t* - p) / t*, a PRODUCT of the
    atom's mass and its distance from the level. That is the coordinate
    the refuted condition is missing, and it predicts the one signal
    the parent file did measure -- an abandoned above-level atom is the
    cell's lightest at 87.5% and 92.6% -- as a SHADOW of a sharper
    quantity rather than as the quantity itself, since a heavy atom
    barely above the level and a light atom far above it can trade
    places.

SO THE FIRST QUESTION is whether the dual ORDERS the failures: is the
atom that gets abandoned the one the dual makes marginal?

THE HAND ATTACK, and it moved the file before any engine code.

FIRST, THE OBSERVABLE IS PER-CELL AND ITS DENOMINATOR IS THE CELL. "The
extreme reduced cost" is a comparison AMONG the atoms of one cell, so it
is trivially satisfied wherever the comparison has one participant. A
cell with exactly one above-level atom scores a hit for free. Every
count below is therefore reported TWICE -- over all failures, and over
the failures whose candidate set has at least TWO members -- and the
second is the one that means anything. This is the species that cost the
parent file a headline: a rate without its denominator.

SECOND, AND FOR THE SAME REASON, THE BASE RATE IS PART OF THE
MEASUREMENT. Being the extreme of a two-atom set happens half the time
by chance. So the extreme-rate among FAILING atoms is printed beside the
extreme-rate among ALL candidate atoms of the same restricted
population, and beside the mean candidate-set size. A rate that matches
its base rate is the dual saying nothing.

THIRD, THE TWO HALVES NEED DIFFERENT REDUCED COSTS, because they are
different events. Being ABANDONED drops every label the atom would have
taken, so its price is the sum of rc over the atom's strictly-above
labels (RC-ALL, negative, and the least-negative atom is the marginal
one -- the MAXIMUM). Being SERVED buys ONE label, its best, so its
price is that label's rc alone (RC-TOP, positive below the level, and
the cheapest purchase is the MINIMUM). Reading both halves with one
statistic would be reading one of them with the wrong object; RC-TOP is
printed for the above half as well, as a second reading rather than the
frozen one.

FOURTH, AND THIS IS WHAT THE ATTACK ACTUALLY FOUND: THE HONEST
ALTERNATIVE IS NOT A CONSTRUCTION TO BE BUILT, IT IS A HASH-TABLE PASS
OVER THE SWEEP ALREADY BUILT. An auditor's predicate is by definition a
function of what the auditor can see: the subgroup's OWN weight, its OWN
posterior row, and the global level it does not influence. The refuted
condition max_y p(y|r) < t* is a member of that class. So is rc, which
is w_r * (t* - p) / t*. So is every fourth guess. The whole class dies
at ONE collision: two atoms carrying the SAME (w, row, t*) in different
cells, one abandoned in every optimum and the other served in every
optimum. That is decidable by indexing the sweep, and it is exact.

  * THE ROW IS SORTED, and that is canonicalization rather than
    weakening. The objective is separable over pairs given the per-atom
    SIZES, and an optimum at size s takes the atom's top s labels, so
    the label INDICES never couple one atom to another: a permuted row
    is the same atom. Two atoms with the same sorted row and weight are
    interchangeable inputs.
  * THE FATES COMPARED ARE THE FORCED ONES. Where the optimum is not
    unique an atom can take nothing in one optimum and something in
    another, so only size-0-in-ALL against size-positive-in-ALL is
    scored. An atom ambiguous across its own cell's optima is excluded
    from the comparison entirely; a collision built on one would be a
    tie artifact and not a refutation.
  * AND IT CARRIES ITS OWN POSITIVE CONTROL, which the reduced-cost
    route does not. At EQUAL weights the threshold condition is PROVED,
    so it IS a per-atom predicate there, so the collision count over
    equal-weight cells must be ZERO. A nonzero count is a defect in this
    file and not a result, and it is read before any unequal-weight
    verdict is read.

FIFTH, WHAT A COLLISION WOULD AND WOULD NOT SAY. It refutes predicates
reading the atom's own numbers against the level. It does NOT refute the
per-CELL reading, which is why the dual question is asked anyway and not
made moot: rc-extremeness compares an atom to its neighbours and is
outside the class. An auditor holding the whole cell is a different
auditor from one holding a subgroup, and the corpus's claim is about the
second.

THE PREDICTIONS, fixed before the engine ran.

  D1 (THE DUAL ORDERS THE ABOVE HALF). The count of ABOVE-SERVES
     failures whose atom is NOT the RC-ALL maximum among its cell's
     above-level atoms, over cells with at least two of them, is ZERO.
     Nonzero kills the route and the count's SHAPE is the finding.
  D2 (THE DUAL ORDERS THE BELOW HALF). The count of BELOW-ABANDONS
     failures whose atom is NOT the RC-TOP minimum among its cell's
     below-level atoms, over cells with at least two of them, is ZERO.
  D3 (NO PER-ATOM PREDICATE). At least one key (w, sorted row, t*) is
     carried by a forced-ABANDONED atom in one cell and a forced-SERVED
     atom in another. Predicted to HOLD. It would close the question
     rather than fail it: no function of a subgroup's own numbers
     against the operative level can decide that subgroup's fate.

THE CONTROLS, fixed before the engine ran.

  C-LAG (ARITHMETIC). At every cell and every optimal size vector,
     cost == lambda*(1-alpha) + lambda*s + sum_selected rc, in Fraction,
     exactly. AND IT IS WEAKER THAN IT LOOKS, which is why it is not the
     only dual control: the identity is a rearrangement and holds for
     ANY lambda, so passing it says the bookkeeping is right and says
     NOTHING about the price being the LP's.
  C-DUAL (THE PRICE). The dual objective at lambda = 1/t*, namely
     lambda*(1-alpha) minus the positive parts, equals the fractional
     relaxation explore_ruler_barecell.py computes independently, at
     every cell. This is what establishes that 1/t* is the LP's own
     price and hence that the reduced costs below are the LP's reduced
     costs. Added at audit rather than frozen, because the freeze read
     C-LAG as covering it.
  C-EQ (POSITIVE, and it is the one that matters). Zero D3 collisions
     among equal-weight cells, where the condition is proved and a
     per-atom predicate demonstrably exists. Read before D3.
  C-DEGEN (VACUITY). The extreme-rate over ALL candidate atoms in the
     restricted population must be strictly below 100%. At 100% the
     statistic cannot fail and D1/D2's zeros would mean nothing -- the
     same empty-control shape the parent file caught in its own P4.
  C-PARITY (INHERITED SWEEP). The arms, menus, weight grid and optimum
     enumerator are imported from explore_ruler_abandon.py unchanged, so
     the cell population is the same one whose optimum was checked
     against the imported exhaustive search at all 38,500 cells there.
     The atom counts printed here must reproduce that file's: 634
     below-level atoms on arm B, 3,154 ABOVE-SERVES and 24
     BELOW-ABANDONS failures across the two arms.

THE SWEEP. Unchanged from the parent: both arms, M = 3 atoms, k = 3
labels, denominator-20 menus, 125 row-triples times the 153-point weight
grid plus the equal-weight point, 38,500 cells, every optimal size
vector enumerated exhaustively in Fraction.

RESOURCE NOTE. The parent's sweep at 50.1 s and 13.5 MB, with one
all_optima call per cell rather than two, plus a collision index keyed by
(weight, sorted row, level) holding two witnesses per key -- bounded by
the number of DISTINCT keys, which is small against 115,500 atoms.
Estimated well under two minutes and a few tens of MB, inside the 512 MB
default; the run record below carries what it actually cost.

RUN RECORD. 38,500 cells, wall 16.3 s, peak working set 14.5 MB against
the 512 MB default (memwatch) -- a third of the parent's wall because
the optimum enumerator runs once per cell here rather than twice. (The
figures are the audited rig's, C-DUAL included; before that control was
added the same sweep ran 14.5 s at 14.3 MB.)
Fractions throughout; every optimal size vector enumerated at every
cell.

THE CONTROLS, read before any verdict. C-LAG: 0 failures over all 38,500
cells and every optimal size vector at each, so the bookkeeping is
exact. C-DUAL: 0 failures over the same 38,500, so lambda = 1/t* is the
LP's own price and the reduced costs are the LP's -- the check C-LAG was
mistakenly read as covering at the freeze, since that identity holds at
any lambda at all. C-EQ: 0 collisions over the
equal-weight cells, where a per-atom predicate provably exists -- the
detector does not fire where it must not. C-PARITY: 3,154 ABOVE-SERVES
failures, 24 BELOW-ABANDONS failures and 634 arm-B below-level atoms,
reproducing explore_ruler_abandon.py exactly. C-DEGEN: the extreme-rate
over all candidates is 37.3% above and 62.5% below, so neither test was
one a zero could be had from.

D1 FAILS, AND THE COUNT'S SHAPE IS THE FINDING. The abandoned atom is
NOT always the dual's marginal one: 240 of arm A's 1,921 comparable
failures and 118 of arm B's 1,080 sit at an atom that is not the RC-ALL
maximum of its cell. (Arm A's other 153 failures are in cells with a
single above-level atom, where the comparison has one participant and a
hit is free; arm B has none such.) So the LP dual does not ORDER the
integrality corrections, and the route the aim named is closed as
stated.

What it does do is order them WELL: 87.5% and 89.1% against base rates
of 36.7% and 38.0%, better than two to one. That is a real tendency and
it is the same strength the parent file's crude light-atom reading has,
which is the question this file then had to ask rather than leave.

AND THE DUAL DOES NOT BEAT THE WEIGHT ALONE, WHICH IS THE RESULT WORTH
CARRYING. Scored on the SAME restricted population, the crude reading
"the abandoned atom is the lightest of its cell's above-level atoms"
takes 87.7% on arm A against the dual's 87.5% and 92.6% on arm B against
the dual's 89.1%. THOSE FOUR RATES DO NOT RANK THE TWO READINGS, and
saying they did would be this file's own species turned on itself: the
rival's base rate is HIGHER in both arms, 37.8% and 39.3% against 36.7%
and 38.0%, so its criterion is the looser one and read as lift over base
the two are indistinguishable -- 2.38 against 2.32 on arm A, 2.35 against
2.36 on arm B.

SO THE READINGS ARE SCORED AGAINST EACH OTHER ON THE SAME ATOMS, which
no base rate can argue with. Where they disagree on arm A the split is
36 to 32 in the weight's favour over 1,921 failures, which is a TIE and
is reported as one. On arm B it is not close and the shape is stronger
than a rate: the dual is uniquely right ZERO times and the weight 38
times, so every failure the dual identifies the weight identifies too and
the dual's hits are a strict SUBSET. Containment, not a deficit of three
and a half points.

The dual reads w_r * (t* - p) / t* and the rival reads w_r; the extra
coordinate is the atom's DISTANCE from the level, and it buys nothing on
either arm and is dominated on one. The transplant this file marked at
the freeze -- that a quantity carrying both coordinates must beat one
carrying a single coordinate -- is refuted by its own measurement. WHAT
IS MEASURED IS THE RANKING AND NOT THE REASON: why the distance term
fails to pay is not asked here.

D2 IS UNTESTABLE ON THIS SWEEP, AND THE RIG'S OWN DENOMINATOR CAUGHT IT.
All 24 BELOW-ABANDONS failures sit in cells carrying exactly ONE
below-level atom, so the comparison has one participant at every one of
them and the miss count is 0 of 0 rather than 0 of 24. Sixteen cells (32
atoms) do carry two below-level atoms and none of them carries a
failure. A file printing the unrestricted count would have reported "0
misses" and read the dual as ordering the below half perfectly. It is
the same vacuity the parent caught twice -- on arm A's antecedent and in
its own positive control -- recurring a third time in a third place, and
what caught it here was freezing the restricted denominator BEFORE the
run rather than noticing the shape after.

D3 HOLDS, AND IT CLOSES THE FRONT RATHER THAN FAILING IT. 67 of the 444
distinct keys carry both a forced-abandoned and a forced-served atom,
and the headline is 55 of them rather than all 67: 12 sit at an AT-LEVEL
atom, which is the indifference band the condition's strict inequalities
say nothing about and which the parent file excludes from both of its
failure counts, so counting them here would rest the refutation partly
on ties. The other 55 are 49 strictly above the level and 6 strictly
below. AND NO COLLISION IS A TIE ARTIFACT AT THE OPTIMUM EITHER: the
optimum is UNIQUE in both cells at all 67, so "forced" is never doing
hidden work anywhere in the set. NOR IS IT AN ARTIFACT OF POOLING THE
TWO DESIGNED MENUS, which would be the obvious objection to a refutation
built on a crossed sweep: taken alone arm A carries 31 above-level
collisions and arm B 33 above-level and 6 below, so either arm refutes
the class by itself and the pooled 55 is smaller than their sum only
because a key found in both is one key (checked at audit, not frozen).
NO PREDICATE READING A SUBGROUP'S OWN NUMBERS AGAINST THE OPERATIVE
LEVEL CAN DECIDE THAT SUBGROUP'S FATE once subgroups carry unequal mass
-- not the refuted threshold, not the three refuted readings of the
mass against the coverage owed, not the reduced cost, and not any
fourth guess.

The first witness is exhibited whole and re-derived by hand. An atom of
mass 1/20 with row (3/5, 1/5, 1/5) sits in two cells whose operative
level is 1/5 in both. Against weights (1/20, 1/20, 9/10) the heavy atom
takes two labels and covers 9/10 * 4/5 = 18/25, already past the 7/10
target, so the light atom is ABANDONED and the optimum (0, 0, 2) costs
9/5. Against weights (1/20, 1/10, 17/20) the heavy atom's two labels
cover 17/20 * 4/5 = 17/25, short by 1/50, and the cheapest top-up is the
light atom's own best label at 1/20 against the middle atom's 1/10 -- so
the SAME atom is SERVED and the optimum (1, 0, 2) costs 7/4. The
optimum is UNIQUE in both cells, so nothing here is a tie artifact, and
an independent brute-force enumerator written without this file's
helpers -- ranging over label SUBSETS rather than sizes -- returns the
same two optima and the same two fates.

SO THE ANSWER TO "WHAT REPLACES THE THRESHOLD" IS THAT NOTHING OF THAT
FORM DOES (proved: two exhibited cells, every value a rational computed
exactly, the optimum unique in both). The condition's failure off equal
masses is not a matter of having found the wrong quantity. Min-cost
covering stops being a pointwise problem once purchases are lumpy: what
an atom's fate depends on is WHAT THE REST OF THE CELL LEAVES OWED, and
two cells can leave a numerically identical atom on opposite sides of
that. What survives for an auditor is a per-CELL reading and not a
per-subgroup one -- and the best per-cell reading measured here is the
crude one, the lightest above-level atom at 87.7% and 92.6%, which is a
tendency and not a law.
"""

import os
import sys
from fractions import Fraction

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_ruler_abandon import (  # noqa: E402
    ALPHA, MENU_A, MENU_B, WEIGHTS, EQUAL, ROWS,
    make_cell, all_optima, check_truth,
)
from explore_ruler_barecell import (  # noqa: E402
    operative_level, certified_optimum,
)

F = Fraction


# ------------------------------------------------------ the dual prices

def reduced_costs(cell, level):
    """rc(r, y) = w_r * (t* - p(y|r)) / t*, per atom, sorted by posterior
    descending so index s-1 is the s-th label an optimum of that size
    takes."""
    out = []
    for r in range(cell.M):
        w = cell.atom_prob(r)
        post = sorted(cell.posterior(r), reverse=True)
        out.append([(p, w * (level - p) / level) for p in post])
    return out


def check_strong_duality(cell, level):
    """C-DUAL: lambda = 1/t* is the LP's OWN price, not merely a number
    the identity tolerates.

    C-LAG is a rearrangement and holds for ANY lambda, so it cannot
    establish this and must not be read as doing so. The dual of
    min c'x s.t. a'x >= b, x <= 1 is max b*lambda - sum mu with
    mu_ry = max(0, lambda*a_ry - c_ry), and at the optimum its value
    equals the primal LP. So this compares the dual objective at
    lambda = 1/t* against the fractional relaxation the parent file
    computes independently, and any gap means the price is wrong.
    """
    lam = 1 / level
    dual = lam * (1 - ALPHA)
    for r in range(cell.M):
        w = cell.atom_prob(r)
        for p in cell.posterior(r):
            rc = w * (level - p) / level
            if rc < 0:
                dual += rc
    lower, _upper, _exact, _cov = certified_optimum(cell, ALPHA, level)
    return dual == lower


def check_lagrangian(cell, level, best, arg):
    """C-LAG: cost == lambda*(1-alpha) + lambda*s + sum_selected rc.

    An exact rearrangement, so any mismatch is an error in the reduced
    costs and not a property of the cell.
    """
    lam = 1 / level
    target = 1 - ALPHA
    rc = reduced_costs(cell, level)
    for sizes in arg:
        cov = F(0)
        cost = F(0)
        sel = F(0)
        for r in range(cell.M):
            w = cell.atom_prob(r)
            for j in range(sizes[r]):
                p, c = rc[r][j]
                cov += w * p
                sel += c
            cost += w * sizes[r]
        if cost != lam * target + lam * (cov - target) + sel:
            return False
        if cost != best:
            return False
    return True


# --------------------------------------------------- the two questions

def score_dual(cell, level, arg):
    """Both halves against the dual, with their denominators.

    The `*2` counters are restricted to cells where the comparison has
    at least TWO participants, which is the only population an
    extreme-rate is readable over.
    """
    rc = reduced_costs(cell, level)
    above, below = [], []
    for r in range(cell.M):
        top = rc[r][0][0]
        if top > level:
            rc_all = sum(c for p, c in rc[r] if p > level)
            above.append((r, rc_all, rc[r][0][1], cell.atom_prob(r)))
        elif top < level:
            below.append((r, rc[r][0][1]))

    d = dict(above_fail=0, below_fail=0,
             above_fail2=0, below_fail2=0,
             above_miss=0, below_miss=0,
             above_miss_top=0,
             above_cand2=0, below_cand2=0,
             above_extreme2=0, below_extreme2=0,
             above_setsum=0, below_setsum=0,
             above_ncells2=0, below_ncells2=0,
             above_light=0, above_lightbase=0,
             hh_both=0, hh_dual=0, hh_rival=0, hh_neither=0)

    best_all = max((c for _r, c, _t, _w in above), default=None)
    best_top_above = max((t for _r, _c, t, _w in above), default=None)
    # The RIVAL quantity, on the SAME population: the parent file's
    # crude reading, an atom being the lightest of its cell's
    # above-level atoms. Printed beside D1 because two rates on
    # different denominators cannot be compared, and the whole claim
    # for the dual is that it BEATS the weight alone.
    light_above = min((w for _r, _c, _t, w in above), default=None)
    best_below = min((t for _r, t in below), default=None)

    if len(above) >= 2:
        d["above_ncells2"] = 1
        d["above_setsum"] = len(above)
        for _r, c, _t, w in above:
            d["above_cand2"] += 1
            d["above_extreme2"] += (c == best_all)
            d["above_lightbase"] += (w == light_above)
    if len(below) >= 2:
        d["below_ncells2"] = 1
        d["below_setsum"] = len(below)
        for _r, t in below:
            d["below_cand2"] += 1
            d["below_extreme2"] += (t == best_below)

    for r, c, t, w in above:
        if all(sizes[r] == 0 for sizes in arg):
            d["above_fail"] += 1
            if len(above) >= 2:
                d["above_fail2"] += 1
                if c != best_all:
                    d["above_miss"] += 1
                if t != best_top_above:
                    d["above_miss_top"] += 1
                d["above_light"] += (w == light_above)
                # HEAD TO HEAD. Two hit-rates with different base rates
                # cannot be ranked by either number, so the two readings
                # are scored AGAINST EACH OTHER on the same atoms: who
                # is right where they disagree.
                dl, rv = (c == best_all), (w == light_above)
                d["hh_both"] += (dl and rv)
                d["hh_dual"] += (dl and not rv)
                d["hh_rival"] += (rv and not dl)
                d["hh_neither"] += (not dl and not rv)
    for r, t in below:
        if all(sizes[r] > 0 for sizes in arg):
            d["below_fail"] += 1
            if len(below) >= 2:
                d["below_fail2"] += 1
                if t != best_below:
                    d["below_miss"] += 1
    d["below_atoms"] = len(below)
    return d


def atom_key(cell, r, level):
    """What an auditor holding the subgroup can see: its own mass, its
    own posterior row canonicalized by sorting, and the global level."""
    return (cell.atom_prob(r),
            tuple(sorted(cell.posterior(r), reverse=True)),
            level)


# --------------------------------------------------------- the sweep

def run_arm(menu, tag, rows_list, weights, index):
    tot = {}
    lag_fail = 0
    dual_fail = 0
    cells = 0
    miss_wit, forced = [], 0
    for rows in rows_list:
        for wts in weights:
            cell = make_cell(menu, tag, rows, wts)
            if not check_truth(cell):
                continue
            level, _m, _c, _s = operative_level(cell, ALPHA)
            best, arg = all_optima(cell, ALPHA)
            if best is None:
                continue
            cells += 1
            if not check_lagrangian(cell, level, best, arg):
                lag_fail += 1
            if not check_strong_duality(cell, level):
                dual_fail += 1
            d = score_dual(cell, level, arg)
            for k, v in d.items():
                tot[k] = tot.get(k, 0) + v
            if (d["above_miss"] or d["below_miss"]) and len(miss_wit) < 6:
                miss_wit.append((rows, wts, level, cell, arg))
            # D3 / C-EQ: index every atom whose fate is FORCED.
            for r in range(cell.M):
                if all(s[r] == 0 for s in arg):
                    fate = "ab"
                elif all(s[r] > 0 for s in arg):
                    fate = "sv"
                else:
                    continue
                forced += 1
                slot = index.setdefault(atom_key(cell, r, level), {})
                if fate not in slot:
                    slot[fate] = (tag, rows, wts, r, cell)
    tot["cells"] = cells
    tot["lag_fail"] = lag_fail
    tot["dual_fail"] = dual_fail
    tot["forced"] = forced
    return tot, miss_wit


def collisions(index):
    """Keys carrying BOTH a forced-abandoned and a forced-served atom.
    Each one refutes every predicate reading the atom's own numbers
    against the operative level."""
    return [(k, v["ab"], v["sv"]) for k, v in index.items()
            if "ab" in v and "sv" in v]


def collision_sides(coll):
    """Split the collisions by which side of the level the atom sits on.

    The AT-LEVEL ones are the indifference band, where the condition is
    stated with strict inequalities and says nothing either way, and the
    parent file excludes that band from both of its failure counts. So
    they are excluded from the headline here too rather than quietly
    counted: a refutation resting on ties would be a weaker claim than
    the one being made, and the split is printed so it cannot be read
    as the stronger one by accident.
    """
    out = {"above": 0, "at": 0, "below": 0}
    for key, _ab, _sv in coll:
        top = max(key[1])
        out["above" if top > key[2] else
            ("below" if top < key[2] else "at")] += 1
    return out


# ---------------------------------------------------------- reporting

def _pc(n, d):
    return "n/a" if not d else "%.1f%%" % (100.0 * n / d)


def show(title, t):
    print("%s" % title)
    print("   cells %d, C-LAG failures %d, C-DUAL failures %d,"
          " forced-fate atoms %d"
          % (t["cells"], t["lag_fail"], t["dual_fail"], t["forced"]))
    print("   ABOVE-SERVES failures %d (%d in cells with >=2 above-level"
          " atoms)" % (t["above_fail"], t["above_fail2"]))
    print("      D1 misses (not the RC-ALL maximum) : %d of %d  (%s)"
          % (t["above_miss"], t["above_fail2"],
             _pc(t["above_miss"], t["above_fail2"])))
    print("      second reading, RC-TOP maximum     : %d of %d  (%s)"
          % (t["above_miss_top"], t["above_fail2"],
             _pc(t["above_miss_top"], t["above_fail2"])))
    print("      RIVAL, the WEIGHT alone (lightest above-level atom),"
          " same population: %d of %d (%s) against its own base rate"
          " %d of %d (%s)"
          % (t["above_light"], t["above_fail2"],
             _pc(t["above_light"], t["above_fail2"]),
             t["above_lightbase"], t["above_cand2"],
             _pc(t["above_lightbase"], t["above_cand2"])))
    print("      HEAD TO HEAD on the same failures: both %d, dual only"
          " %d, weight only %d, neither %d"
          % (t["hh_both"], t["hh_dual"], t["hh_rival"], t["hh_neither"]))
    print("      BASE RATE, all above-level atoms in those cells:"
          " %d of %d extreme (%s), mean set size %.2f"
          % (t["above_extreme2"], t["above_cand2"],
             _pc(t["above_extreme2"], t["above_cand2"]),
             (float(t["above_setsum"]) / t["above_ncells2"])
             if t["above_ncells2"] else 0.0))
    print("   below-level atoms %d" % t["below_atoms"])
    print("   BELOW-ABANDONS failures %d (%d in cells with >=2 below-level"
          " atoms)" % (t["below_fail"], t["below_fail2"]))
    print("      D2 misses (not the RC-TOP minimum) : %d of %d  (%s)"
          % (t["below_miss"], t["below_fail2"],
             _pc(t["below_miss"], t["below_fail2"])))
    print("      BASE RATE, all below-level atoms in those cells:"
          " %d of %d extreme (%s), mean set size %.2f"
          % (t["below_extreme2"], t["below_cand2"],
             _pc(t["below_extreme2"], t["below_cand2"]),
             (float(t["below_setsum"]) / t["below_ncells2"])
             if t["below_ncells2"] else 0.0))


def show_cell(label, tag, rows, wts, r, cell, level, arg):
    print("      %s  %s rows %s  weights %s  t*=%s  atom %d"
          % (label, tag, "".join(map(str, rows)),
             "/".join(str(w) for w in wts), str(level), r))
    for i in range(cell.M):
        print("         atom %d  w=%-6s row=%-22s sizes=%s"
              % (i, str(cell.atom_prob(i)),
                 ",".join(str(v) for v in
                          sorted(cell.posterior(i), reverse=True)),
                 sorted({s[i] for s in arg})))


def main():
    print("WHAT REPLACES THE ABANDONED ATOM'S THRESHOLD -- THE LP DUAL")
    print("alpha = %s, nominal coverage %s, dual price lambda = 1/t*"
          % (ALPHA, 1 - ALPHA))
    print()

    eq_index, un_index = {}, {}

    print("=== EQUAL WEIGHTS -- the control half, read first ===")
    ta_eq, _w = run_arm(MENU_A, "A-EQ", ROWS, [EQUAL], eq_index)
    tb_eq, _w2 = run_arm(MENU_B, "B-EQ", ROWS, [EQUAL], eq_index)
    show("ARM A, equal weights", ta_eq)
    show("ARM B, equal weights", tb_eq)
    eq_coll = collisions(eq_index)
    print()
    print("C-EQ POSITIVE CONTROL -- the condition is PROVED at equal")
    print("weights, so a per-atom predicate exists there and the")
    print("collision count MUST be zero.")
    print("   collisions over equal-weight cells: %d" % len(eq_coll))
    print()

    print("=== UNEQUAL WEIGHTS ===")
    ta, wa = run_arm(MENU_A, "A-UN", ROWS, WEIGHTS, un_index)
    tb, wb = run_arm(MENU_B, "B-UN", ROWS, WEIGHTS, un_index)
    show("ARM A, unequal weights", ta)
    print()
    show("ARM B, unequal weights", tb)
    print()

    print("C-PARITY (against explore_ruler_abandon.py): ABOVE-SERVES"
          " %d+%d = %d against 3,154; BELOW-ABANDONS %d+%d = %d against"
          " 24; arm B below-level atoms %d against 634"
          % (ta["above_fail"], tb["above_fail"],
             ta["above_fail"] + tb["above_fail"],
             ta["below_fail"], tb["below_fail"],
             ta["below_fail"] + tb["below_fail"],
             tb["below_atoms"] + tb_eq["below_atoms"]))
    print()

    print("C-DEGEN: the extreme-rate over ALL candidates must be below")
    print("100%%, or D1/D2 cannot fail.  above %s, below %s"
          % (_pc(ta["above_extreme2"] + tb["above_extreme2"],
                 ta["above_cand2"] + tb["above_cand2"]),
             _pc(ta["below_extreme2"] + tb["below_extreme2"],
                 ta["below_cand2"] + tb["below_cand2"])))
    print()

    for label, wits in (("ARM A", wa), ("ARM B", wb)):
        if not wits:
            print("D1/D2 miss witnesses, %s: none" % label)
            continue
        print("D1/D2 miss witnesses, %s, first %d:" % (label, len(wits)))
        for rows, wts, level, cell, arg in wits:
            rc = reduced_costs(cell, level)
            print("   rows %-5s weights %-18s t*=%s"
                  % ("".join(map(str, rows)),
                     "/".join(str(w) for w in wts), str(level)))
            for i in range(cell.M):
                top = rc[i][0][0]
                side = "ABOVE" if top > level else (
                    "below" if top < level else "at")
                print("      atom %d  w=%-6s top=%-6s %-5s "
                      "rc_all=%-10s rc_top=%-10s sizes=%s"
                      % (i, str(cell.atom_prob(i)), str(top), side,
                         str(sum(c for p, c in rc[i] if p > level)),
                         str(rc[i][0][1]),
                         sorted({s[i] for s in arg})))
    print()

    un_coll = collisions(un_index)
    print("D3 -- NO PER-ATOM PREDICATE.  A key is (own weight, own")
    print("sorted posterior row, operative level): everything an auditor")
    print("holding the subgroup can see.  A key carrying both a")
    print("forced-abandoned and a forced-served atom kills every")
    print("predicate of that form at once.")
    sides = collision_sides(un_coll)
    print("   distinct keys %d, colliding keys %d -- %d at an atom"
          " strictly ABOVE the level, %d strictly below, and %d in the"
          " AT-LEVEL indifference band, which the parent file excludes"
          " from its failure counts and which is therefore excluded"
          " from the headline: the refutation rests on the other %d."
          % (len(un_index), len(un_coll), sides["above"], sides["below"],
             sides["at"], sides["above"] + sides["below"]))
    for key, ab, sv in un_coll[:3]:
        _w3, row, lev = key
        print("   KEY  w=%s  row=%s  t*=%s"
              % (str(key[0]), ",".join(str(v) for v in row), str(lev)))
        tag, rows, wts, r, cell = ab
        _b, arg = all_optima(cell, ALPHA)
        show_cell("ABANDONED in every optimum:", tag, rows, wts, r,
                  cell, lev, arg)
        tag, rows, wts, r, cell = sv
        _b, arg = all_optima(cell, ALPHA)
        show_cell("SERVED in every optimum   :", tag, rows, wts, r,
                  cell, lev, arg)


if __name__ == "__main__":
    main()
