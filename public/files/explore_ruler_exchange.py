"""explore_ruler_exchange.py -- THE EXCHANGE STEP: does forcing every
above-level pair into the marginal optimum ever overstate it?

(The machinery, the cells' base classes and the two oracles are IMPORTED
from explore_ruler_barecell.py and explore_ruler_setvalued.py rather than
rewritten, which is what makes the comparison below a re-reading of the
same instrument and not a second one.)

THE QUESTION. The set-valued read minimizes expected set size subject to
marginal coverage, and the problem is a knapsack over (atom, label)
PAIRS: pair (r, y) costs the atom's weight w_r and covers w_r * p(y|r),
so its ratio is p(y|r) alone and the atom weight cancels out of the
ranking. certified_optimum builds the answer as EVERY pair strictly
above the operative level t*, plus the cheapest sub-collection of the
tied block at t* that closes the deficit. The first half of that -- that
every strictly-above pair is in the optimum -- is an argument its own
author recorded as INCOMPLETE (explore_ruler_barecell.py, run record):
it assumes the coverage freed by dropping such a pair must be bought
back from the tied block, and it need not be.

Two laws ride on the step, and neither is stated wherever the step is
not available:

  (a) THE TIE RULE's zero half -- multiplicity 1 at t* implies a form
      penalty of exactly zero -- is VERIFIED by exhaustive search at
      nine of eleven cells and NOT derived.
  (b) THE ABANDONMENT CONDITION -- an atom is dropped from the optimum
      exactly when its best label's posterior falls below t* -- is
      derived only where every atom carries the same weight, and the
      corpus reads it nowhere else.

So this file does not ask whether the certificate is a sound upper bound
(it is, by construction, and every positive-penalty figure needs only
that). It asks whether the bound is TIGHT, and where it is not.

WHOSE VOCABULARY. The suspicion is written in the knapsack's terms --
cost, value, ratio, integrality -- and not in the conformal literature's
nor the tower's, because the object is a claimed optimality argument
about an integer program. ATOM keeps the sense the two parent files give
it: a point of positive marginal mass in the observable. LEVEL, TIED
BLOCK and OPERATIVE are the parent files' words for the same objects.

TRANSPLANT, MARKED. The expectation that the threshold structure
survives unequal atom weights is imported from the EQUAL-weight setting,
where "every label costs the same" is precisely the hypothesis that
makes the increment greedy optimal. Carrying it to unequal weights is a
transplant across the one hypothesis the derivation uses, and it is what
this file is built to test rather than to assume.

THE HAND ATTACK, and it moved the probe twice (worked on paper before
any engine code; recorded here because it changed both what gets
measured and what the file expects to see).

FIRST, THE RECORDED WORRY IS NOT THE MECHANISM. The parent file's note
says a pair BELOW t* sitting at a very light atom "can be cheaper in
absolute cost than a tied pair at a heavy one, ratio and cost being
different things". That is true about absolute cost and cannot break the
step. Dropping an above-level pair a at atom r frees w_r of cost and
loses w_r * p_a of coverage; buying that coverage back from pairs of
ratio p costs (w_r * p_a) / p, which is DECREASING in p. Every pair
below t* has p < t* < p_a, so every such repurchase costs strictly more
than w_r, and the swap is strictly worse. Absolute cost is the wrong
comparison because the coverage bought scales with the same weight that
sets the cost -- the weights cancel, which is the same cancellation that
makes the ratio p(y|r). So the step cannot fail through a cheap light
pair, and a probe built to hunt one would have found nothing and
reported the step safe.

SECOND, AND THIS IS WHAT THE FILE MEASURES: the step can fail through
INTEGRALITY. The repurchase argument treats the tied block as divisible.
It is not. The certificate closes the deficit with a min-cost SUBSET SUM
over the tied block, and a lumpy block OVERSHOOTS: the chosen subset S
delivers strictly more coverage than the deficit needs. Write that
surplus as D. If D >= w_r * p_a for some strictly-above pair a at atom
r, then dropping a is FEASIBLE without touching S, and it saves w_r.
The certificate, which forces a in, is then strictly above the optimum.

Minimality of S bounds the surplus: removing any s from S must break
feasibility, so D < w_s * t* for every s in S. So a disagreement needs

    min_{s in S} w_s * t*  >  w_r * p_a      with  p_a > t*,

which forces w_s > w_r -- a tied atom strictly HEAVIER than the atom of
the pair that should be dropped. That is the shape to look for.

THIRD, AND IT IS A DERIVATION RATHER THAN A PREDICTION: at EQUAL atom
weights the step CLOSES. With every w = w0 the tied items all cost w0
and cover w0 * t*, so the min-cost subset is just the smallest count
reaching the deficit and its surplus obeys D < w0 * t*. Any strictly
above-level pair covers w0 * p_a > w0 * t* > D, so no such pair is ever
droppable and the certificate is exact. This closes half of (a) outright
-- at equal weights the multiplicity-1 zeros are DERIVED and not merely
verified -- and it says the counterexample, if there is one, is a
UNEQUAL-WEIGHT object and could never have appeared among the
equal-weight cells the parent file searched.

THE SLATE, frozen before any engine code.

PREDICTIONS.
  P1. The EQUAL-weight arm of the sweep prints ZERO disagreements, at
      every cell it reaches. (The derivation above; a single
      disagreement refutes it.)
  P2. The UNEQUAL-weight arm prints AT LEAST ONE disagreement.
  P3. At every disagreement found, min_{s in S} w_s * t* > w_r * p_a
      holds for the dropped pair -- the heavy-tie-atom shape above --
      and in particular the tied atom is heavier than the dropped
      pair's atom.
  P4. The fractional lower bound stays a lower bound at every cell:
      lower <= exhaustive <= upper, with any gap at the UPPER end.

KILLS, as observables rather than as inferences -- what the rig prints,
with what it would mean weighed only after the run.
  K-A. The equal-weight arm prints a nonzero disagreement count.
  K-B. The unequal-weight arm prints a disagreement count of zero over
       the whole sweep.
  K-C. Any cell printing exhaustive < lower or exhaustive > upper.

CONTROLS, run and read BEFORE any kill or survive result is read.
  C1 (POSITIVE, the detector fires). certified_optimum is called at a
     level one step ABOVE the operative one on a cell known to carry a
     tie there. That forces a set which is feasible but not optimal, so
     the comparison MUST flag a disagreement. A detector that cannot
     fire on a rule known to be wrong reports nothing when it stays
     silent, and every K-B reading depends on this.
  C2 (PARITY). On the seven bare cells the parent file scores, the
     certificate and the exhaustive search agree exactly, reproducing
     that file's own 7/7. Any drift means the imported machinery is not
     the machinery whose record this file is reading.
  C3 (TRUTH). Every generated cell's posteriors sum to 1 per atom and
     its atom weights sum to 1, in Fraction. A cell failing this is not
     a probability model and its optimum means nothing.

THE SWEEP. Small designed cells, M = 3 atoms and k = 3 labels, over a
posterior MENU chosen so that a tie at the operative level is generic
(the parent file's finding: finitely many posterior values is what any
modulus gives, and hand-set cells inherit it), crossed with a weight
grid that includes the equal-weight point and a range of lopsided ones.
Exhaustive optimum at (k+1)^M = 64 size vectors per cell, so the search
is exact everywhere and nothing here rests on a bracket.

RESOURCE NOTE. Fractions throughout, no numpy, a few thousand cells at
64 size vectors each. Estimated well under a second and a few MB; the
run record below carries what it actually cost.

RUN RECORD. 19,250 cells scored exactly, wall 14.8s, peak working set
22.0 MB against the 512 MB default (memwatch). Fractions throughout; the
exhaustive optimum ran at every cell and nothing below rests on a
bracket. The tables below run wider than this file's prose and are left
that way: they are output copied verbatim, so rewrapping them would make
the record something other than what the run printed.

THE WEIGHT GRID IS A DESIGNED SAMPLE AND NOT A CENSUS, which matters
only for reading the counts as proportions. It walks 153 of the 171
positive compositions of 20 into three parts -- the third weight never
takes the value 1/20 -- so every "of 19,125" below is over that grid.
Nothing here turns on the proportions: the claims are that a
disagreement EXISTS densely at unequal weights and that none exists at
equal ones, and the second is proved rather than sampled.

THE FROZEN C1 COULD NOT RUN, and it is left standing above with the
correction here. Calling certified_optimum at a level one step ABOVE the
operative one does not produce a feasible-but-suboptimal rule: the
operative level is by construction the largest whose full inclusion
reaches the target, so at any higher level the tied block cannot close
the deficit and the subset sum asserts instead of returning. The control
caught nothing because it never ran on a single cell -- it printed DID
NOT FIRE, which is exactly what a real kill would have printed, and that
is the reason a positive control is read before any verdict. Its
replacement tests the same property with an object already known to be
non-optimal: the STRICT-THRESHOLD rule, which the parent file measured
standing a full label above the optimum at every tie cell.

C1 (replacement) fires at 4/7 parent cells, and WHERE it fires is the
control's real content: B-TIE-1, B-TIE-3 and B-DEAD-7 (3.0/3.0/7.0
against 2.0/2.0/5.0) and B-TILT-W (3.0 against 2.0) -- exactly the
multiplicity >= 2 cells -- while B-NOTIE, B-STRADDLE and B-MIXED show no
gap at all, which is the tie rule's zero half reproduced by a second
route. A detector silent at three cells and loud at four, along the
partition an independent law predicts, is a detector.
C2 parity: certificate == exhaustive at 7/7. C3: zero truth failures
over 19,250 generated cells. K-C did not fire -- zero order violations,
so P4 holds everywhere.

P1 HOLDS. The equal-weight arm: 125 cells, ZERO disagreements.
P2 HOLDS, and not narrowly. The unequal-weight arm: 5,447 disagreements
over 19,125 cells -- 28.5%, a bulk property of the weighted family and
not a corner of it.

  rows  weights            t*      mult  upper    OPT      gap      D          cheapest w_r*p_a  drop
  000   1/20/3/20/4/5      1/5     6     1.80000  1.75000  0.05000  3/50       3/100             1
  000   1/20/4/5/3/20      1/5     6     1.80000  1.75000  0.05000  3/50       3/100             1
  000   3/20/1/20/4/5      1/5     6     1.80000  1.75000  0.05000  3/50       3/100             1
  000   4/5/1/20/3/20      1/5     6     1.80000  1.75000  0.05000  3/50       3/100             1
  001   1/20/3/20/4/5      3/10    1     1.80000  1.75000  0.05000  3/50       3/100             1
  001   1/20/1/5/3/4       3/10    1     1.75000  1.70000  0.05000  1/20       3/100             1
  001   1/20/1/4/7/10      3/10    1     1.70000  1.65000  0.05000  1/25       3/100             1
  001   1/20/3/10/13/20    3/10    1     1.65000  1.60000  0.05000  3/100      3/100             1
  001   1/20/3/5/7/20      1/5     5     1.70000  1.65000  0.05000  1/25       3/100             1
  001   3/20/1/20/4/5      3/10    1     1.80000  1.75000  0.05000  3/50       3/100             1

THE HAND ATTACK'S FIRST CONCLUSION IS WRONG, and the audit found it
rather than the run. "The recorded worry is not the mechanism" is
refuted: 2,463 of the 5,447 disagreements have NO optimum that avoids
buying a label strictly BELOW the level -- 45% of them, and the route
the parent file's note named all along. The argument above is sound
about what it actually proves and proves the wrong thing. It shows that
a dropped pair's coverage cannot be REPURCHASED more cheaply at a worse
ratio, which is true. The optimum does not repurchase. It exploits the
same integrality SLACK the second half of the attack found: where the
tied fill overshoots, the optimum drops a HEAVY tied item and tops the
coverage back up with a LIGHT below-level one, giving up part of the
surplus it no longer needs. Absolute cost and ratio are both operative
and they are ONE mechanism, not two -- which is why splitting them and
retiring one half was the error.

The specimen is the smallest cell that shows it: three atoms at weights
3/10, 3/10, 2/5, every posterior (2/5, 2/5, 1/5), t* = 2/5 with nothing
strictly above it. The certificate fills from the tied block alone and
lands at cost 2 with coverage 4/5 against a target of 7/10. The optimum
takes sizes (2, 3, 1) for cost 19/10 and coverage exactly 7/10 -- the
third label at atom 2 is the 1/5 one, below the level, and buying it is
what lets a 2/5-weight tied item go.

THE ROUTES, over the 5,447, and they OVERLAP rather than partition:
4,002 admit the surplus route (some strictly-above pair fits inside D),
2,463 require a below-level label in EVERY optimum, 1,147 are both, and
129 are neither -- so the union leaves a remainder and this file claims
no characterization. What it does claim is that the two halves of the
hand attack are one mechanism and that neither alone reaches the cells
the other explains.

AND THE AUDIT ARM CARRIES THE RESULT THAT MATTERS MOST, which no frozen
prediction reached for because the slate was aimed at the certificate
and not at the law standing on it. At multiplicity 1 the certificate IS
the strict-threshold rule -- the tied block holds one item and the
certificate must take it -- so the TIE RULE's zero half is exactly the
claim that the certificate is optimal there, and this file has just
shown that claim to depend on the weights. Scored against the exhaustive
optimum: 21 equal-weight cells at multiplicity 1 and ZERO with a
positive penalty, against 2,492 unequal-weight cells at multiplicity 1
of which 1,080 carry a STRICTLY POSITIVE one -- worst 3/10, at
posteriors (10,6,4)/20, (8,8,4)/20, (8,8,4)/20 and weights 7/20, 1/20,
3/5, where the threshold rule costs 2 against an optimum of 17/10. So
the tie rule's zero half is DERIVED at equal weights and FALSE at
unequal ones. The corpus's eleven cells could not have seen it: its one
unequal-weight cell carries multiplicity 8, so the zero half was only
ever read where the weights are flat.

AND THE ARM'S OTHER READING BREAKS THE RULE'S REMAINING DIRECTION, at
BOTH weightings, which the predictions above did not ask about either. A
multiplicity of 2 or more does not force a positive penalty: 35 of 104
equal-weight cells at multiplicity >= 2 pay EXACTLY ZERO, and 3,045 of
16,633 unequal-weight ones. This half was never proved and the parent
file names the exception shape itself -- a tied block whose whole width
is exactly what the deficit needs -- while recording that no cell it
had placed one. A designed sweep places them at a third of the
equal-weight cells, so the shape is common and not a corner. What
survives of the tie rule is one direction at one weighting:
multiplicity >= 2 is NECESSARY for a positive penalty at equal weights,
and sufficient nowhere.

P3 IS MEASURED AT A DIFFERENT QUANTITY THAN IT NAMES, deliberately and
with the substitution recorded rather than dressed. As frozen it reads
min over the CHOSEN subset S, and certified_optimum returns that
subset's cost sum and not the subset, so the frozen statistic is not
recoverable from the instrument. The SURPLUS D is, exactly, and it is
what the mechanism turns on -- the minimality bound was only ever a
consequence of D. So D is what the table prints.

THE SURPLUS ROUTE IS A SUFFICIENT CONDITION AND NOT A CHARACTERIZATION.
At 4,002 of the 5,447 some strictly-above pair satisfies w_r * p_a <= D;
at 1,445 none does, and 16 of those carry no strictly-above pair at all,
which is where the audit started pulling. The freed weight accounts for
the whole gap at only 1,732 -- usually the tied subset moves too, and
the paragraph above says what it moves to.

AND THE EQUAL-WEIGHT CASE DESERVES THE STRONGER ARGUMENT IT TURNS OUT TO
HAVE, which the audit also supplied. The derivation frozen above rules
out dropping a strictly-above pair while the tied subset stands, and
that is weaker than the run needs: the below-level route shows a rule
may be beaten without dropping any above-level pair at all. The complete
statement is easier than the partial one. At equal weights every label
costs w0, so a rule's cost is w0 times the COUNT of labels it takes and
minimizing cost is minimizing that count; for a fixed count the largest
reachable coverage is w0 times the sum of that many largest posteriors
anywhere; so the optimum is the greedy by posterior, which is exactly
every pair above the level plus the smallest tied fill -- the
certificate. That holds for every M, k and level, and it covers
below-level substitutions and subset moves alike, because it never
argues about an exchange. It is why the equal-weight arm reads zero and
would read zero on any grid.

WHAT THIS DOES AND DOES NOT DISTURB. Nothing measured stands corrected.
The certificate remains a sound UPPER bound by construction, so every
positive-penalty figure in the parent files -- which need only OPT <=
upper -- is untouched, and so is every equal-weight zero. What DOES
move is what those figures are: the corpus scores three unequal-weight
cells and could exhaustively search only one. That one, B-TILT-W,
agrees exactly (2.0 against 2.0), which is how 28.5% of a weighted
sweep went unseen behind a single witness. The other two are the
tilted ring cells, whose penalties are therefore FLOORS and not values
-- an overstated optimum moves a penalty measured against it only up.

SETTLED SINCE, and the paragraph above is left standing as this file's
own record. explore_ruler_optimum.py solves both tilted cells exactly by
a different algorithm, so all three unequal-weight cells are searched
and neither penalty is a floor any longer: +0.0805 at TILT-3 and
+0.1033 at TILT-4-WIDE. The direction predicted here holds -- both moved
UP -- and the reason splits, which this file could not have seen: at
TILT-3 the certificate does overstate, while at TILT-4-WIDE it is EXACT
and was merely uncomputable past the parent's sum cap. What survives
here unchanged is everything the sweep measured, the equal-weight
derivation, and the two routes.
"""

import os
import sys
from fractions import Fraction

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_ruler_barecell import (  # noqa: E402
    WeightedBareCell,
    certified_optimum,
    exhaustive_optimum,
    operative_level,
    BARE,
)

F = Fraction
ALPHA = F(3, 10)


# ------------------------------------------------------------ the sweep

# Posterior rows, denominator 20 so every value is exact and the menu
# repeats values ACROSS rows -- which is what puts a tie at whatever
# level turns out to be operative.
MENU = [
    [F(12, 20), F(4, 20), F(4, 20)],
    [F(10, 20), F(6, 20), F(4, 20)],
    [F(8, 20), F(8, 20), F(4, 20)],
    [F(14, 20), F(4, 20), F(2, 20)],
    [F(8, 20), F(6, 20), F(6, 20)],
]

# Weight triples over denominator 20, the equal point first.
WEIGHTS = []
for a in range(1, 19):
    for b in range(1, 19 - a):
        c = 20 - a - b
        if c >= 1:
            WEIGHTS.append((F(a, 20), F(b, 20), F(c, 20)))
EQUAL = (F(1, 3), F(1, 3), F(1, 3))


def make_cell(name, rows, weights):
    return WeightedBareCell(name, [list(MENU[i]) for i in rows],
                            list(weights))


def check_truth(cell):
    """C3: a generated cell is a probability model, in Fraction."""
    if sum(cell.w) != 1:
        return False
    for r in range(cell.M):
        if sum(cell.posterior(r)) != 1:
            return False
    return True


def surplus(cell, alpha, level):
    """The certificate's coverage SURPLUS D over the target.

    P3 as frozen names min over the CHOSEN subset S, which
    certified_optimum does not return -- it returns the subset's cost
    sum. D is the quantity the mechanism actually turns on and it is
    exactly recoverable, so it is what gets measured; see the run
    record.
    """
    _l, _u, _e, cov = certified_optimum(cell, alpha, level)
    return cov - (1 - alpha)


def droppable(cell, level, D):
    """The strictly-above pairs whose whole coverage fits inside the
    surplus -- the pairs the mechanism says the certificate should not
    have forced in. Returns (count, weight freed)."""
    n, freed = 0, F(0)
    for r in range(cell.M):
        w = cell.atom_prob(r)
        for y in range(cell.k):
            p = cell.posterior(r)[y]
            if p > level and w * p <= D:
                n += 1
                freed += w
    return n, freed


def cheapest_above(cell, level):
    """The strictly-above pair with the SMALLEST coverage -- the cheapest
    candidate to drop. None where the level is the top value and no pair
    sits strictly above it."""
    best = None
    for r in range(cell.M):
        w = cell.atom_prob(r)
        for y in range(cell.k):
            p = cell.posterior(r)[y]
            if p > level:
                cov = w * p
                if best is None or cov < best[0]:
                    best = (cov, w, p)
    return best


def scan(rows_list, weights, tag):
    """Score every (rows, weights) cell and return the disagreements."""
    found, seen, bad_truth, bad_order = [], 0, 0, 0
    for rows in rows_list:
        for wts in weights:
            cell = make_cell("%s-%s" % (tag, "".join(map(str, rows))),
                             rows, wts)
            if not check_truth(cell):
                bad_truth += 1
                continue
            seen += 1
            level, mult, _cov, _sets = operative_level(cell, ALPHA)
            lower, upper, exact, _c = certified_optimum(cell, ALPHA, level)
            opt = exhaustive_optimum(cell, ALPHA)
            if opt is None:
                continue
            if opt < lower or opt > upper:
                bad_order += 1
            if exact and opt < upper:
                found.append((rows, wts, level, mult, lower, upper, opt,
                              cell))
    return found, seen, bad_truth, bad_order


# ---------------------------------------------------------- the controls

def control_C1():
    """POSITIVE: the detector must flag a rule already known to be
    non-optimal.

    The frozen C1 -- certified_optimum at a level one step ABOVE the
    operative one -- could not run, and the run record says why. This is
    its replacement and it tests the same thing: the STRICT-THRESHOLD
    rule, which takes the whole tied block, is the object the parent
    file measured standing a full label above the optimum at every tie
    cell. Feeding it through this file's comparison must reproduce that
    gap, or a silent comparison means nothing.
    """
    out = []
    for cell in BARE:
        level, _m, _c, sets = operative_level(cell, ALPHA)
        thresh = sum(cell.atom_prob(r) * len(sets[r])
                     for r in range(cell.M))
        opt = exhaustive_optimum(cell, ALPHA)
        if opt is not None:
            out.append((cell.name, thresh, opt, thresh > opt))
    return out


def control_C2():
    """PARITY: the parent file's bare cells, certificate against the
    exhaustive search, must agree exactly."""
    rows = []
    for cell in BARE:
        level, mult, _c, _s = operative_level(cell, ALPHA)
        lower, upper, exact, _cv = certified_optimum(cell, ALPHA, level)
        opt = exhaustive_optimum(cell, ALPHA)
        rows.append((cell.name, exact, upper, opt))
    agree = sum(1 for _n, e, u, o in rows if o is not None and e and u == o)
    total = sum(1 for _n, e, u, o in rows if o is not None and e)
    return agree, total, rows


def tie_rule_arm(weights):
    """THE TIE RULE at multiplicity 1, scored against the EXHAUSTIVE
    optimum rather than against the certificate.

    Added at audit and labelled as such, not dressed as a frozen arm.
    The tie rule's zero half says the form penalty is exactly zero
    wherever the operative level carries multiplicity 1. At
    multiplicity 1 the certificate IS the strict-threshold rule -- the
    tied block holds one item and the certificate must take it -- so
    the zero half is the statement that the certificate is optimal
    there, and the sweep above says that depends on the weights. This
    arm reads the penalty against the exhaustive optimum, which the
    corpus's own reading of the rule could not do at these cells.
    """
    seen = pos = many = many_zero = 0
    worst = None
    for rows in ROWS:
        for wts in weights:
            cell = make_cell("TR", rows, wts)
            if not check_truth(cell):
                continue
            level, mult, _c, sets = operative_level(cell, ALPHA)
            thresh = sum(cell.atom_prob(r) * len(sets[r])
                         for r in range(cell.M))
            opt = exhaustive_optimum(cell, ALPHA)
            if opt is None:
                continue
            if mult == 1:
                seen += 1
                if thresh > opt:
                    pos += 1
                    if worst is None or thresh - opt > worst[0]:
                        worst = (thresh - opt, rows, wts, level, thresh,
                                 opt)
            else:
                many += 1
                if thresh == opt:
                    many_zero += 1
    return seen, pos, worst, many, many_zero


ROWS = [(a, b, c)
        for a in range(len(MENU))
        for b in range(len(MENU))
        for c in range(len(MENU))]


def main():
    print("EXCHANGE STEP -- is the forced above-level set the optimum?")
    print("alpha = %s, nominal coverage %s" % (ALPHA, 1 - ALPHA))
    print()

    c1 = control_C1()
    fired = sum(1 for _n, _t, _o, f in c1 if f)
    print("C1 POSITIVE detector  fires at %d/%d parent cells"
          % (fired, len(c1)))
    for n, t, o, f in c1:
        print("   %-12s threshold rule %-8s optimum %-8s  %s"
              % (n, float(t), float(o), "FLAGGED" if f else "-"))
    print()

    agree, total, rows = control_C2()
    print("C2 PARITY  certificate == exhaustive at %d/%d parent bare cells"
          % (agree, total))
    for n, e, u, o in rows:
        print("   %-12s exact=%-5s upper=%-8s exhaustive=%s"
              % (n, e, float(u), "n/a" if o is None else float(o)))
    print()

    eq, eq_seen, eq_bad, eq_ord = scan(ROWS, [EQUAL], "EQ")
    print("EQUAL-WEIGHT ARM   cells %d, truth failures %d, order "
          "violations %d" % (eq_seen, eq_bad, eq_ord))
    print("   disagreements: %d" % len(eq))
    print()

    un, un_seen, un_bad, un_ord = scan(ROWS, WEIGHTS, "UN")
    print("UNEQUAL-WEIGHT ARM cells %d, truth failures %d, order "
          "violations %d" % (un_seen, un_bad, un_ord))
    print("   disagreements: %d" % len(un))
    print()

    if un:
        print("the disagreements, smallest gap first -- D is the")
        print("certificate's coverage surplus, and the mechanism says a")
        print("pair is droppable exactly when w_r*p_a <= D")
        print("  rows  weights            t*      mult  upper    OPT"
              "      gap      D          cheapest w_r*p_a  drop")
        for rows_, wts, level, mult, lower, upper, opt, cell in sorted(
                un, key=lambda t: (t[5] - t[6], t[0]))[:10]:
            D = surplus(cell, ALPHA, level)
            ca = cheapest_above(cell, level)
            n, freed = droppable(cell, level, D)
            print("  %-5s %-18s %-7s %-5d %-8.5f %-8.5f %-8.5f %-10s %-17s %d"
                  % ("".join(map(str, rows_)),
                     "/".join(str(w) for w in wts),
                     level, mult, float(upper), float(opt),
                     float(upper - opt), str(D),
                     "none" if ca is None else str(ca[0]), n))
        print()
        # The mechanism, over every disagreement: does the surplus
        # account for the whole gap?
        exact_hit, no_pair, gap_eq = 0, 0, 0
        for _r, _w, level, _m, _l, upper, opt, cell in un:
            D = surplus(cell, ALPHA, level)
            ca = cheapest_above(cell, level)
            if ca is None:
                no_pair += 1
                continue
            n, freed = droppable(cell, level, D)
            if n > 0:
                exact_hit += 1
            if freed == upper - opt:
                gap_eq += 1
        print("MECHANISM over %d disagreements:" % len(un))
        print("  at least one pair with w_r*p_a <= D : %d" % exact_hit)
        print("  no strictly-above pair at all       : %d" % no_pair)
        print("  freed weight EQUALS the whole gap   : %d" % gap_eq)
        print()

    print("AUDIT ARM -- BOTH halves of the tie rule, scored against the")
    print("exhaustive optimum rather than against the certificate")
    for tag, wl in (("equal  ", [EQUAL]), ("unequal", WEIGHTS)):
        seen, pos, worst, many, many_zero = tie_rule_arm(wl)
        print("  %s weights" % tag)
        print("     zero half: %d cells at multiplicity 1, %d with a "
              "STRICTLY POSITIVE penalty" % (seen, pos))
        if worst:
            print("        worst %s at rows %s weights %s (threshold %s "
                  "against optimum %s)"
                  % (worst[0], "".join(map(str, worst[1])),
                     "/".join(str(w) for w in worst[2]),
                     worst[4], worst[5]))
        print("     positive half: %d cells at multiplicity >= 2, %d "
              "paying EXACTLY ZERO" % (many, many_zero))


if __name__ == "__main__":
    main()
