"""THE ABANDONED ATOM OFF FLAT WEIGHTS -- does the threshold condition
survive unequal atom weights?

THE QUESTION. A set-valued rule that minimizes expected set size subject
to a marginal coverage target sometimes hands a whole subpopulation the
EMPTY SET. explore_ruler_barecell.py derives the condition that decides
which: an atom r is abandoned exactly when its own best label's
posterior falls below the operative level,

    max_y p(y|r) < t*,

with t* set by the whole population and no part of it set by that atom.
That is the useful form for an auditor -- the quantity deciding whether
a subgroup gets an empty set is its own best posterior against a global
threshold it does not influence.

The derivation is the EQUAL-weight one. Every label costs the same, so a
rule's cost is a constant times the COUNT of labels it takes, minimizing
cost is minimizing that count, the increment greedy by posterior is
exactly optimal, and the threshold structure follows. At UNEQUAL weights
that argument is unavailable: explore_ruler_exchange.py measures the
same greedy certificate strictly above the true optimum at 5,447 of
19,125 weighted cells, and names this very condition as one of two laws
riding on an exchange step it then shows to fail. So the condition
stands at unequal weights on nothing -- neither derived nor measured.
This file measures it.

WHOSE VOCABULARY. The suspicion is written in the knapsack's terms --
cost, ratio, integrality, overshoot -- because the object is an
optimality claim about an integer program, and not in the conformal
literature's. ATOM, LEVEL, OPERATIVE and TIED BLOCK keep the senses
explore_ruler_barecell.py and explore_ruler_exchange.py give them.

TRANSPLANT, MARKED. The expectation that the threshold structure
survives unequal weights is imported from the equal-weight setting,
across the one hypothesis its derivation uses. It is what this file
tests rather than assumes.

THE HAND ATTACK, and it moved the probe before any engine code was
written.

FIRST, THE CONDITION IS TWO CLAIMS AND THEY FAIL BY DIFFERENT
MECHANISMS. Read as an iff it says (BELOW-ABANDONS) an atom whose every
label sits strictly below t* takes nothing, and (ABOVE-SERVES) an atom
carrying a label strictly above t* takes something. At equal weights
both fall out of the pair greedy. At unequal weights the pair ratio is
STILL p(y|r) -- pair (r, y) costs w_r and covers w_r * p(y|r), so the
weight cancels out of the ratio -- and what breaks is INTEGRALITY, not
the ranking. explore_ruler_exchange.py already records the two ways it
breaks, and each one attacks a different half:

  * an optimum can DROP a strictly-above pair outright (4,002 of its
    weighted cells admit it). Where the dropped pair is an atom's ONLY
    above-level label and its others go untaken, that atom is abandoned
    with max_y p(y|r) > t*, and ABOVE-SERVES fails.
  * an optimum can drop a heavy tied item and top the coverage back up
    with a LIGHT label from strictly BELOW the level (2,463 have no
    optimum that avoids one). Where that light label sits at an atom
    whose whole row is below t*, that atom is served with
    max_y p(y|r) < t*, and BELOW-ABANDONS fails.

So the two halves are measured separately throughout. A file that
reported one mismatch count would be reporting the sum of two unrelated
mechanisms.

SECOND, AND THIS IS WHAT MOVED THE PROBE: THE INHERITED SWEEP CANNOT
POSE HALF THE QUESTION. The plan was to read the condition straight off
explore_ruler_exchange.py's family, whose exact exhaustive optimum is
already built and already verified. But that family's posterior menu has
rows whose largest entry is 12/20, 10/20, 8/20, 14/20 and 8/20, and the
coverage target is 7/10: taking every atom's top label alone delivers at
most 7/10 and generally less, so the operative level never rises ABOVE a
row's maximum -- it can equal one, where every atom is the 14/20 row and
the top labels reach the target exactly, but it cannot clear one. An
atom with its whole row below t* does not occur there, at any
weighting. The antecedent of BELOW-ABANDONS is never
satisfied, so that half would have printed a vacuous zero and been read
as a confirmation.

Hence TWO ARMS. Arm A is the inherited family unchanged, which can pose
ABOVE-SERVES and is the parity link to the file it comes from. Arm B is
a new family designed so that the antecedent is REACHABLE: rows with a
large spike (16/20, 14/20, 12/20) that can carry the target on their own
against rows that are nearly flat (8/20, 7/20 largest), so that a level
of 6/10 or above is operative while a flat atom's entire row sits under
it. The design is checked by arithmetic before the run rather than
hoped for: two spike atoms at 16/20 holding weight 19/20 between them
cover 19/20 * 4/5 = 19/25, past the 7/10 target, so 4/5 is operative
while a flat atom's row tops out at 2/5. Arm B PRINTS its antecedent
count, and a zero there condemns the arm's design rather than
confirming the law.

THIRD, THE OPTIMUM IS NOT UNIQUE AND "ABANDONED" IS THEREFORE TWO
PREDICATES. Where several size vectors attain the minimum cost, an atom
may take nothing in some of them and something in others. This file
enumerates EVERY optimal size vector and separates FORCED abandonment
(size 0 in all of them) from AVAILABLE abandonment (size 0 in at least
one). A mismatch is scored against the predicate that makes the
condition hardest to break: ABOVE-SERVES fails only where an atom is
abandoned in EVERY optimum, and BELOW-ABANDONS fails only where a
below-level atom is served in EVERY optimum. Ties alone are never
reported as failures.

FOURTH, EQUALITY IS AN INDIFFERENCE BAND AND NOT A MISMATCH. The
condition is stated with strict inequalities. An atom whose best
posterior EQUALS t* is exactly the case the Lagrangian is indifferent
at, and both a taken and an untaken label are consistent with it. Those
atoms are counted and printed on their own line, never folded into
either mismatch count.

THE PREDICTIONS, fixed before the engine ran.

  P1 (VACUITY, arm A). The number of (cell, atom) pairs in arm A with
     max_y p(y|r) < t* is ZERO, at every weighting. This is the hand
     attack's arithmetic restated as an observable: if it prints
     nonzero, that derivation is wrong and arm A's read changes.
  P2 (ABOVE-SERVES fails, unequal weights). Arm A's unequal-weight cells
     contain at least one atom abandoned in every optimum whose best
     posterior is strictly ABOVE t*. Mechanism: the dropped above-level
     pair.
  P3 (BELOW-ABANDONS fails, unequal weights). Arm B's unequal-weight
     cells contain at least one atom served in every optimum whose whole
     row is strictly BELOW t*. Mechanism: the light below-level label
     bought to close an overshoot.
  P4 (THE CONTROL HALF). Both mismatch counts are ZERO at equal weights,
     on BOTH arms. Here the condition is proved, so a nonzero count is a
     defect in this rig and not a result, and it is read before any
     weighted verdict is read.

THE CONTROLS, fixed before the engine ran.

  C1 (POSITIVE, the detector fires). A detector that never fires reports
     nothing when it stays silent. Both mismatch tests are re-run
     against a deliberately WRONG level -- one step below the operative
     one -- on arm B's cells. Lowering the level admits pairs the
     optimum does not take, so atoms must appear on the wrong side of
     it, and both counters must go strictly positive. A counter still
     at zero under a level known to be wrong is not measuring anything.
  C2 (PARITY). This file's own optimum enumerator, minimized over its
     enumerated argmin set, must return the same cost as the imported
     exhaustive_optimum at every cell of both arms and at the parent
     bare cells. Any single disagreement means the enumeration is not
     the search whose record is being read.
  C3 (TRUTH). Every generated cell's posteriors sum to 1 per atom and
     its weights sum to 1, in Fraction. A cell failing this is not a
     probability model and its optimum means nothing.
  C4 (ANTECEDENT REACHED, arm B). Arm B's below-level atom count is
     strictly positive. This is the design check of the second arm, and
     it is a control rather than a prediction because a zero there means
     the arm was built wrong, not that the law held.

THE SWEEP. Both arms use M = 3 atoms and k = 3 labels over posterior
menus with denominator 20, crossed with the same weight grid the parent
file walks -- 153 of the 171 positive compositions of 20 into three
parts, plus the equal-weight point -- so 125 row-triples times 154
weightings per arm. The optimum is exhaustive over the (k+1)^M = 64 size
vectors at every cell, in Fraction, so nothing here rests on a bracket.
The grid is a designed sample and not a census, which matters only for
reading counts as proportions; nothing below turns on a proportion.

RESOURCE NOTE. Fractions throughout, no numpy, roughly 38,500 cells at
64 size vectors each, which is twice the parent file's sweep at its
14.8 s. Estimated well under two minutes and a few tens of MB, inside
the 512 MB default; the run record below carries what it actually cost.

RUN RECORD. 38,500 cells scored exactly -- 125 row-triples times 154
weightings on each of the two arms plus three eight-atom control cells
-- wall 50.1 s, peak working set 13.5 MB against the 512 MB default
(memwatch). Fractions throughout,
the exhaustive optimum ran at every cell, every optimal size vector was
enumerated at every cell, and nothing below rests on a bracket.

THE FROZEN C1 IS HALF A CONTROL, and it is left standing above with the
correction here. Scoring at a level one step BELOW the operative one
does stress ABOVE-SERVES -- lowering the bar puts more atoms above it --
but it does the OPPOSITE to the other half: it SHRINKS the below-level
population, from 634 atoms at the operative level to 12 under the
lowered one, so BELOW-ABANDONS printed 0 under a level known to be
wrong. That zero was not the law holding; it was a counter with almost
nothing left to count. The mistake was reading "a wrong level" as one
direction when the two halves are stressed by opposite ones. The
replacement runs each half under the shift that ENLARGES its own
population, and both counters are then loud: one step TOO LOW gives
1,229 ABOVE-SERVES failures over the 17,509 cells that HAVE a lower
level, and one step TOO HIGH gives 7,288 below-level atoms carrying
6,774 BELOW-ABANDONS failures over the 18,318 that have a higher one. A
cell whose operative level is already the extreme value is SKIPPED
rather than scored -- 1,616 and 807 of them -- because scoring it would
score it at the CORRECT level and fold real failures into a control's
count, which is a control measuring the thing it is supposed to be
independent of.

C2 PARITY: this file's enumerator agrees with the imported exhaustive
search at 7/7 parent bare cells and at every one of the 38,500 swept
cells -- 0 parity failures. C3 TRUTH: 0 failures over the same 38,500.
C4 ANTECEDENT REACHED: 634 below-level atoms on arm B, so the second
arm poses the question its design was built to pose.

P1 HOLDS, and the hand attack that predicted it was what earned the
second arm. Arm A carries ZERO atoms wholly below the operative level,
at the equal-weight point and across all 19,125 weightings alike. Read
off the inherited family alone, BELOW-ABANDONS would have printed a
vacuous 0 and been reported as a law confirmed.

P2 HOLDS, and not narrowly. ABOVE-SERVES fails at 2,074 atoms over arm
A's weighted cells and 1,080 over arm B's: an atom carrying a label
strictly above the operative level, abandoned in EVERY optimum. THE
COUNT IS MEASURED AND THE MECHANISM IS NOT -- what this file scores is
the failure, not its cause, and the cause below is read off the printed
witnesses alone. At the first arm-B witness the two served atoms cover
7/20 * 4/5 + 3/5 * 7/10 = 7/10 exactly, and the third atom, peaking at
4/5 well above the level of 7/10, is simply not needed, so its pair is
not bought rather than exchanged. Whether that account covers the other
3,153 is not asked here and is not answered by these counts.

P3 HOLDS. BELOW-ABANDONS fails at 24 of arm B's 634 below-level atoms:
an atom whose ENTIRE row sits strictly under the operative level, served
in EVERY optimum. Again the COUNT is what is measured. At the first
witness the heavy atom's label covers 17/20 * 4/5 = 17/25, short of 7/10
by 1/50, and closing it with the light atom's below-level label costs
1/20 where the remaining above-level atom would cost 1/10 -- the cheaper
purchase sits on the wrong side of the level and the optimum makes it
anyway. Whether that account covers the other 23 is not asked here.
AND NONE OF THE 24 IS A TIE ARTIFACT: the optimum is UNIQUE at every one
of them, so "served in every optimum" is not doing hidden work, and an
independent brute-force enumeration written without this file's helpers
returns the same 24 cells and the same minimum-weight reading.

P4 HOLDS ON ONE HALF AS FROZEN, AND THE OTHER HALF WAS VACUOUS UNTIL A
LEG WAS ADDED FOR IT. Both mismatch counts are 0 at the equal-weight
point on both arms -- but the BELOW counter had nothing to count there,
because THREE equal atoms cannot produce a below-level atom at all: the
others must carry the whole target alone, and two thirds of any
posterior in either menu falls short of 7/10. So the arm that was
supposed to reproduce the PROVED case reproduced half of it, and the
half it skipped is the half this file exists to test. It is the same
vacuity the hand attack caught on arm A, recurring one layer out in the
CONTROL, where it is worse: an empty positive control reads as the law
holding. C5 supplies the population -- EIGHT equal atoms, seven peaked
and one flat, which is the shape the derivation's own worked cell has.
At all three such cells the operative level is 4/5, one atom sits below
it, and both failure counts are 0. The proved case now reproduces with
something to reproduce, and E8-FLAT is the corpus's own worked cell, so
the leg is a parity link to it as well as a control.

SO THE CONDITION IS EQUAL-WEIGHT-ONLY: OFF EQUAL MASSES IT IS NOT A LAW,
AND BOTH DIRECTIONS HAVE EXACT COUNTEREXAMPLES. The refutation is
PROVED -- one exhibited cell kills an iff, every value in it is a
rational computed exactly, and the first witness of each direction is
re-derived by hand in this record. The COUNTS are observations over a
designed sweep and not a census, so they are counts and never
proportions. And the claim is EXISTENTIAL: most unequal-weight cells
still satisfy the condition, which is why the counts are small against
their populations and why that costs the condition nothing -- an iff
does not survive a minority. What an auditor loses is the right to read
a subgroup's fate off that subgroup's own best posterior against the
operative level once subgroups carry unequal mass. Both the sufficiency
and the necessity go.

AND THE LIGHT-ATOM READING IS ONE REAL SIGNAL AND ONE ARTIFACT, WHICH
ONLY THE BASE RATES SEPARATE (observation, post-hoc over the same sweep
and not a frozen prediction; the rig prints both denominators beside
both rates, which is the whole of what makes them readable). The
ABOVE-SERVES failures land at a MINIMUM-weight atom at 87.5% on arm A
and 92.6% on arm B, against base rates of 37.7% and 36.4% among all
above-level atoms -- a real concentration, better than two to one. The
BELOW-ABANDONS failures land there at 24 of 24, which looks stronger and
is NOTHING: 594 of the 634 below-level atoms are minimum-weight anyway,
a base rate of 93.7%, so 24 of 24 is what chance delivers about a fifth
of the time and the expected count is 22.5. And the base rate is FORCED
rather than sampled -- an atom sits wholly below the level only if the
others carry the target alone, which is to say only if they are heavy --
so the below half could not have shown anything else. The reading that
survives is the ABOVE one: an above-level atom is dropped
disproportionately when it is the cheapest thing in the cell to drop.
What does NOT survive is any claim that the deciding quantity has been
found; the threshold reading fails, and what replaces it is open.
(SETTLED SINCE, and the answer is that NOTHING of that form replaces it:
no predicate reading an atom's own mass and posterior row against the
operative level decides its fate, refuted by cells putting a numerically
identical atom on opposite sides -- explore_ruler_dual.py, which also
scores this file's light-atom reading against the LP dual's reduced cost
and finds the crude reading the better of the two. What survives here
unchanged is the light-atom concentration itself, measured over ALL
failures rather than the restricted population that comparison needs.)
"""

import os
import sys
from fractions import Fraction

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_ruler_barecell import (  # noqa: E402
    WeightedBareCell,
    exhaustive_optimum,
    operative_level,
    BARE,
)

F = Fraction
ALPHA = F(3, 10)


# ------------------------------------------------------------ the arms

# Arm A: the inherited menu, unchanged. Every row's largest entry is at
# least 8/20, which is what makes the below-level antecedent unreachable
# here (P1).
MENU_A = [
    [F(12, 20), F(4, 20), F(4, 20)],
    [F(10, 20), F(6, 20), F(4, 20)],
    [F(8, 20), F(8, 20), F(4, 20)],
    [F(14, 20), F(4, 20), F(2, 20)],
    [F(8, 20), F(6, 20), F(6, 20)],
]

# Arm B: spikes that can carry the target alone, against nearly flat
# rows that then sit entirely under the operative level.
MENU_B = [
    [F(16, 20), F(2, 20), F(2, 20)],
    [F(14, 20), F(4, 20), F(2, 20)],
    [F(12, 20), F(4, 20), F(4, 20)],
    [F(8, 20), F(6, 20), F(6, 20)],
    [F(7, 20), F(7, 20), F(6, 20)],
]

WEIGHTS = []
for _a in range(1, 19):
    for _b in range(1, 19 - _a):
        _c = 20 - _a - _b
        if _c >= 1:
            WEIGHTS.append((F(_a, 20), F(_b, 20), F(_c, 20)))
EQUAL = (F(1, 3), F(1, 3), F(1, 3))

ROWS = [(a, b, c) for a in range(5) for b in range(5) for c in range(5)]


def make_cell(menu, name, rows, weights):
    return WeightedBareCell(name, [list(menu[i]) for i in rows],
                            list(weights))


def check_truth(cell):
    """C3: a generated cell is a probability model, in Fraction."""
    if sum(cell.w) != 1:
        return False
    for r in range(cell.M):
        if sum(cell.posterior(r)) != 1:
            return False
    return True


# ------------------------------------------------- every optimal rule

def all_optima(cell, alpha):
    """Every size vector attaining the minimum cost, and that cost.

    A rule's cost at an atom depends only on how MANY labels it takes
    there, and for a fixed size the top-mass labels are best, so the
    search over size vectors is exhaustive over the rules that can be
    optimal -- the same reduction the imported exhaustive_optimum makes,
    kept here because that function returns the cost alone and the
    question is about WHICH atoms the optimum serves.
    """
    M, k = cell.M, cell.k
    w = [cell.atom_prob(r) for r in range(M)]
    tops = []
    for r in range(M):
        masses = sorted(cell.posterior(r), reverse=True)
        tops.append([sum(masses[:s]) for s in range(k + 1)])
    target = 1 - alpha
    best, arg = None, []
    stack = [()]
    while stack:
        pre = stack.pop()
        d = len(pre)
        if d == M:
            cov = sum(w[r] * tops[r][pre[r]] for r in range(M))
            if cov >= target:
                cost = sum(w[r] * pre[r] for r in range(M))
                if best is None or cost < best:
                    best, arg = cost, [pre]
                elif cost == best:
                    arg.append(pre)
            continue
        for s in range(k + 1):
            stack.append(pre + (s,))
    return best, arg


def score_cell(cell, level):
    """Both halves of the condition at one cell, against one level.

    Returns (below_atoms, above_fail, below_fail, at_level), where
    below_atoms counts atoms whose whole row is strictly under `level`,
    above_fail counts atoms carrying a label strictly ABOVE `level` that
    every optimum abandons, below_fail counts atoms wholly under
    `level` that every optimum serves, and at_level counts the
    indifference band -- atoms whose best posterior equals `level`.
    """
    best, arg = all_optima(cell, ALPHA)
    if best is None:
        return None
    below_atoms = above_fail = below_fail = at_level = 0
    light_above = light_below = 0
    # The DENOMINATORS the two light-atom rates are read against. A
    # concentration without its base rate is not a measurement: a
    # below-level atom is nearly FORCED to be the light one, since the
    # others must carry the target alone.
    base_below = base_above = 0
    wmin = min(cell.atom_prob(r) for r in range(cell.M))
    for r in range(cell.M):
        top = max(cell.posterior(r))
        served_always = all(sizes[r] > 0 for sizes in arg)
        abandoned_always = all(sizes[r] == 0 for sizes in arg)
        light = cell.atom_prob(r) == wmin
        if top == level:
            at_level += 1
        elif top < level:
            below_atoms += 1
            base_below += light
            if served_always:
                below_fail += 1
                light_below += light
        else:
            base_above += light
            if abandoned_always:
                above_fail += 1
                light_above += light
    return (below_atoms, above_fail, below_fail, at_level,
            light_above, light_below, base_below, base_above,
            sum(1 for r in range(cell.M)
                if max(cell.posterior(r)) > level))


def scan(menu, rows_list, weights, tag, shift=0):
    """Score a whole arm. `shift` drops the scoring level by that many
    steps down the cell's own sorted value list -- 0 is the operative
    level and anything else is C1's deliberately wrong level."""
    tot = dict(cells=0, truth=0, below=0, above_fail=0, below_fail=0,
               at_level=0, parity=0, light_above=0, light_below=0,
               unshiftable=0, base_below=0, base_above=0, above_atoms=0)
    wit_above, wit_below = [], []
    for rows in rows_list:
        for wts in weights:
            cell = make_cell(menu, "%s-%s" % (tag, "".join(map(str, rows))),
                             rows, wts)
            if not check_truth(cell):
                tot["truth"] += 1
                continue
            level, _mult, _cov, _sets = operative_level(cell, ALPHA)
            if shift:
                vals = sorted({v for r in range(cell.M)
                               for v in cell.posterior(r)}, reverse=True)
                j = vals.index(level) + shift
                if not 0 <= j < len(vals):
                    # The level cannot move that way here, so scoring
                    # this cell would score it at the CORRECT level and
                    # fold real failures into a control's count.
                    tot["unshiftable"] += 1
                    continue
                level = vals[j]
            out = score_cell(cell, level)
            if out is None:
                continue
            tot["cells"] += 1
            b, af, bf, al, la, lb, bb, ba, aa = out
            tot["base_below"] += bb
            tot["base_above"] += ba
            tot["above_atoms"] += aa
            tot["below"] += b
            tot["above_fail"] += af
            tot["below_fail"] += bf
            tot["at_level"] += al
            tot["light_above"] += la
            tot["light_below"] += lb
            if not shift:
                best, _arg = all_optima(cell, ALPHA)
                if best != exhaustive_optimum(cell, ALPHA):
                    tot["parity"] += 1
            if af and len(wit_above) < 6:
                wit_above.append((rows, wts, level, cell))
            if bf and len(wit_below) < 6:
                wit_below.append((rows, wts, level, cell))
    return tot, wit_above, wit_below


# ---------------------------------------------------------- reporting

def show_arm(title, tot):
    print("%s" % title)
    print("   cells %d, truth failures %d, parity failures %d"
          % (tot["cells"], tot["truth"], tot["parity"]))
    print("   atoms wholly BELOW the level      : %d" % tot["below"])
    print("   atoms AT the level (indifference) : %d" % tot["at_level"])
    print("   ABOVE-SERVES failures             : %d" % tot["above_fail"])
    print("   BELOW-ABANDONS failures           : %d" % tot["below_fail"])
    def _pc(n, d):
        return "n/a" if not d else "%.1f%%" % (100.0 * n / d)
    print("   ABOVE-SERVES failures at a LIGHTEST atom: %d (%s) against a"
          " base rate of %d/%d (%s)"
          % (tot["light_above"], _pc(tot["light_above"], tot["above_fail"]),
             tot["base_above"], tot["above_atoms"],
             _pc(tot["base_above"], tot["above_atoms"])))
    print("   BELOW-ABANDONS failures at a LIGHTEST atom: %d (%s) against a"
          " base rate of %d/%d (%s)"
          % (tot["light_below"], _pc(tot["light_below"], tot["below_fail"]),
             tot["base_below"], tot["below"],
             _pc(tot["base_below"], tot["below"])))


def show_witnesses(label, wits):
    if not wits:
        print("   %s: none" % label)
        return
    print("   %s, first %d:" % (label, len(wits)))
    for rows, wts, level, cell in wits:
        best, arg = all_optima(cell, ALPHA)
        print("      rows %-5s weights %-18s t*=%-6s cost=%-8s optima=%d"
              % ("".join(map(str, rows)),
                 "/".join(str(w) for w in wts), str(level),
                 str(best), len(arg)))
        for r in range(cell.M):
            print("         atom %d  w=%-6s top=%-6s sizes=%s"
                  % (r, str(cell.atom_prob(r)),
                     str(max(cell.posterior(r))),
                     sorted({s[r] for s in arg})))


# Equal-weight cells that DO carry a below-level atom. Three atoms of
# equal mass cannot: the others must carry the whole target alone, and
# two thirds of any posterior here falls short of it. Eight can, which
# is the shape the derivation's own worked cell has -- peaked atoms
# whose top labels clear the target between them, and one flat atom
# left under the level.
def _eight(flat):
    peaked = [[F(a, 100), F(b, 100), F(100 - a - b, 100)]
              for a, b in ((80, 12), (81, 11), (82, 10), (83, 9),
                           (84, 8), (85, 7), (86, 6))]
    return peaked + [flat]


EIGHT = [
    ("E8-FLAT", _eight([F(40, 100), F(32, 100), F(28, 100)])),
    ("E8-LOW", _eight([F(35, 100), F(35, 100), F(30, 100)])),
    ("E8-MID", _eight([F(50, 100), F(30, 100), F(20, 100)])),
]


def control_C5():
    """The equal-weight arm's BELOW half, given a population.

    P4 as frozen asks both mismatch counts to be zero at equal weights.
    The below counter cannot be exercised at three equal atoms at all --
    see the run record -- so this leg supplies eight, where a flat atom
    does sit under the operative level and the derivation still applies.
    """
    out = []
    for name, rows in EIGHT:
        w = [F(1, 8)] * 8
        cell = WeightedBareCell(name, [list(r) for r in rows], w)
        if not check_truth(cell):
            out.append((name, None, None, None, False))
            continue
        level, _m, _c, _s = operative_level(cell, ALPHA)
        b, af, bf, al = score_cell(cell, level)[:4]
        out.append((name, level, b, (af, bf), True))
    return out


def control_C2_parent():
    """PARITY on the parent bare cells: this file's enumerator against
    the imported exhaustive search."""
    agree, total = 0, 0
    for cell in BARE:
        ref = exhaustive_optimum(cell, ALPHA)
        if ref is None:
            continue
        total += 1
        best, _arg = all_optima(cell, ALPHA)
        if best == ref:
            agree += 1
    return agree, total


def main():
    print("THE ABANDONED ATOM OFF FLAT WEIGHTS")
    print("alpha = %s, nominal coverage %s" % (ALPHA, 1 - ALPHA))
    print()

    agree, total = control_C2_parent()
    print("C2 PARITY (parent bare cells)  %d/%d agree" % (agree, total))
    print()

    print("C5 EQUAL-WEIGHT BELOW HALF -- eight equal atoms, so the")
    print("below-level population is not empty the way three leave it")
    for name, level, below, fails, ok in control_C5():
        if not ok:
            print("   %-8s NOT A PROBABILITY MODEL" % name)
            continue
        print("   %-8s t*=%-8s below-level atoms %d   "
              "(ABOVE-SERVES, BELOW-ABANDONS) failures %s"
              % (name, str(level), below, fails))
    print()

    print("=== ARM A -- the inherited menu ===")
    a_eq, _wa, _wb = scan(MENU_A, ROWS, [EQUAL], "A-EQ")
    show_arm("EQUAL-WEIGHT ARM (the control half)", a_eq)
    print()
    a_un, a_wa, a_wb = scan(MENU_A, ROWS, WEIGHTS, "A-UN")
    show_arm("UNEQUAL-WEIGHT ARM", a_un)
    show_witnesses("ABOVE-SERVES witnesses", a_wa)
    show_witnesses("BELOW-ABANDONS witnesses", a_wb)
    print()

    print("=== ARM B -- the designed menu ===")
    b_eq, _wa2, _wb2 = scan(MENU_B, ROWS, [EQUAL], "B-EQ")
    show_arm("EQUAL-WEIGHT ARM (the control half)", b_eq)
    print()
    b_un, b_wa, b_wb = scan(MENU_B, ROWS, WEIGHTS, "B-UN")
    show_arm("UNEQUAL-WEIGHT ARM", b_un)
    show_witnesses("ABOVE-SERVES witnesses", b_wa)
    show_witnesses("BELOW-ABANDONS witnesses", b_wb)
    print()

    print("C4 ANTECEDENT REACHED (arm B below-level atoms) : %d"
          % (b_eq["below"] + b_un["below"]))
    c1lo, _x, _y = scan(MENU_B, ROWS, WEIGHTS, "B-C1LO", shift=1)
    c1hi, _x2, _y2 = scan(MENU_B, ROWS, WEIGHTS, "B-C1HI", shift=-1)
    print("C1 POSITIVE -- each half stressed by the shift that ENLARGES")
    print("its own population, which the frozen C1 got wrong for the")
    print("below half; see the run record.")
    print("   TOO LOW : cells %d (skipped, no lower level %d), "
          "ABOVE-SERVES failures %d, atoms below the level %d"
          % (c1lo["cells"], c1lo["unshiftable"], c1lo["above_fail"],
             c1lo["below"]))
    print("   TOO HIGH: cells %d (skipped, no higher level %d), "
          "BELOW-ABANDONS failures %d, atoms below the level %d"
          % (c1hi["cells"], c1hi["unshiftable"], c1hi["below_fail"],
             c1hi["below"]))


if __name__ == "__main__":
    main()
