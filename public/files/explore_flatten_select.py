"""explore_flatten_select.py -- WHAT SELECTS A FAILING CELL?

explore_flatten_family.py closed 550 cells of h(M, J) -- the least
HEIGHT of a nonzero M-atom vector whose first J moments vanish, read as
the sup-norm shortest vector of the rank-(M - J) lattice (x-1)^J Z[x]
cut at degree < M -- over M = 4..40, J = 2..20. At 530 of them h is the
least height over PURE PRODUCTS prod_i (x^{d_i} - 1) with at least J
factors and degree below M. At 20 it is strictly below one, and those
20 are a DENSITY IN THE DEPTH rather than a scatter: 3 of 362 cells at
J <= 12 against 17 of 188 at J >= 13, and 1.4% against 9.0% with the
153 cells of height 1 -- which cannot fail, the pure bound being 1
there and h >= 1 always -- conditioned out.

No variable named so far SELECTS one. The failing cells occupy lattice
ranks 5 to 18 of a chart reaching 38, so neither the width M nor the
depth J nor the rank M - J alone picks them out. Twenty positives
against 530 negatives is a small population but it is a population
rather than three points, which is the whole reason this question is
now askable at all.

THE QUESTION. Does any cheap cell-level quantity separate the failing
cells from the rest -- and if none does, WHICH of the candidates comes
closest and on what shape of evidence?

THE COMPANION QUESTION, on the same run and nearly free. Dividing every
cyclotomic factor out of each of the 550 exhibited minimisers left
exactly three residuals over the whole chart: 1 at 530 cells, A = 2 +
4x + 5x^2 + 4x^3 + 2x^4 at 16, and B = 2 + 3x + 2x^2 at 4. Both are
reciprocal with leading coefficient 2 and every root on |z| = 1, so the
pure products and their two enrichments sit inside one class -- integer
polynomials with all roots on the unit circle, whose MONIC members are
the products of cyclotomics by Kronecker. Is there a THIRD non-monic
member past depth 20? The cost law says depth is the cheap direction:
the enumeration is priced by the L2 ball's volume over the lattice's
covolume, and the rank M - J falls as J rises.

(FLATTENING, HEIGHT, PURE PRODUCT, RANK and RESIDUAL keep their earlier
senses, restated because this rig is read alone: a vector c on M atoms
is the polynomial P(x) = sum_r c_r x^r; its moments m_j = sum_r C(r,j)
c_r are its coefficients in the (x-1) basis, so the flattening -- the
least j with m_j nonzero -- IS the multiplicity of the root 1. HEIGHT
is the sup norm max_r |c_r|. A PURE PRODUCT is prod_i (x^{d_i} - 1)
over a multiset D of positive parts; it has |D| factors, degree sum D,
and flattening |D|. RANK is always M - J. The RESIDUAL of a witness is
what survives dividing out its monomial factor and every cyclotomic
factor it carries, well defined up to sign because the cyclotomics are
distinct irreducibles. A cell FAILS when h is strictly below the least
pure-product height at that cell.)

THE HAND ATTACK, worked on paper before any engine code.

FIRST, AND IT DISQUALIFIES ONE OF THE FOUR CANDIDATES AS A PREDICTOR.
The GAP -- the least pure height minus h -- is not a predictor of
failure. A cell fails exactly when the gap is positive, so a threshold
on it separates perfectly by construction and reports nothing. What the
gap can do is GRADE the failures, which is a different question with a
different answer, and it is carried below as a DESCRIPTOR and as the
positive control on the separation reporter rather than as a candidate.
The general form of the trap is that a predictor must be computable
without consulting the answer, and h is the answer here.

SECOND, THE MECHANISM THAT MAKES A PREDICTOR OUT OF THE ARITHMETIC.
A and B contribute NO flattening: A(1) = 17 and B(1) = 7, both nonzero.
What they cost is WIDTH -- four atoms for A, two for B -- so an
enriched product carrying at least J factors must fit its pure part
into degree M - 1 - 4 rather than M - 1. So a cell can only be enriched
where the pure family has SLACK in the width: where spending A's four
atoms costs the pure bound little or nothing. That names a predictor
the aim's list did not carry, computable from the pure table alone and
never consulting h -- the PLATEAU,

    plateau_4(M, J) = ph(M - 4, J) - ph(M, J),

with ph the least pure height at the cell and the difference >= 0
because ph FALLS in M: more width can only help. THE SIGN WAS WRITTEN
BACKWARDS IN THE FIRST DRAFT OF THIS PARAGRAPH and the smoke run at a
tiny sweep caught it, before any science had printed, by printing a
column of negative zeros where a nonnegative cost belonged. The
quantity wanted is what the pure bound COSTS when four atoms are taken
away from it, which is the subtraction in that order. Plateau_2 is the
same with B's two atoms. A cell at plateau 0 is one where four atoms of
width are free to the pure family, which is the state in which an
enrichment can pay for itself; a cell where the pure bound falls
steeply in M is one where the four atoms are expensive. This is the
aim's third candidate -- the arithmetic of the cell -- arrived at
through what the multipliers actually cost rather than through J's
divisors, and the divisor count is carried alongside it so the two
readings can be compared rather than conflated.

THIRD, WHAT THE BALL PREDICTOR MUST BE MEASURED AT. The lattice's
covolume is not 1: the basis rows x^i (x-1)^J are in echelon form with
unit pivots, so the leading r-by-r minor is +-1 and the covolume is at
least 1, but by Cauchy-Binet the Gram determinant sums the squares of
ALL r-by-r minors and the rest do not vanish. It is free to read
exactly: the covolume squared is the product of the Gram-Schmidt norms
||b*_i||^2 the reduction already carries, so no determinant needs
computing for the measurement -- and an independent integer determinant
of the Gram matrix is what CONTROLS it. The radius is the second half
of the choice and it decides whether the predictor is predictive at
all. At radius h*sqrt(M) the ball is defined by the answer, which is
the first section's trap in a second costume. The predictive radius is
(ph - 1)*sqrt(M): a cell fails exactly when some lattice vector has sup
norm at most ph - 1, and every such vector has L2 norm at most
(ph - 1)*sqrt(M), so the Gaussian-heuristic count

    log10 [ vol_r((ph - 1) sqrt(M)) / covol ]

is a heuristic for how much room sits below the pure bound, computed
without consulting h. It is a heuristic in the direction that inflates:
the L2 ball at that radius strictly contains the sup-norm box it stands
for, so a count well above 1 is weak evidence and a count below 1 is
the informative side. Both radii are printed, the h one because the aim
named it and because the two together say whether the radius is what
carries the variable.

FOURTH, WHAT THE STALL IS AND WHY IT IS EXPECTED TO BE FLAT. The pure
family's least-height witness at a cell is an argmin multiset; the
STALL asks whether it is forced onto a repeated part. Repeated parts
are cheap and common in that family -- (x-1)^a alone contributes a
parts of the same size -- so the honest expectation before the run is
that the stall rate is high on BOTH sides and separates nothing. It is
carried because the aim named it and because a flat predictor is a
result about the family, not a null.

FIFTH, THE REPORTER IS AN INSTRUMENT AND IT NEEDS BOTH CONTROLS. The
separation report is itself the thing under test here, so it runs
against a variable KNOWN to separate perfectly (the gap) and against
one known to carry nothing (a deterministic hash of the cell), before
any candidate's verdict is read. Its threshold-free number is the
rank-sum statistic -- the probability that a random failing cell scores
above a random non-failing one, ties counted at a half -- which is 1 at
the positive control and near 1/2 at the negative one. A best-threshold
count of false positives and false negatives is printed beside it,
because a rank statistic near 1 and a threshold that still misclassifies
half the negatives are the same evidence read two ways and the second
reading is the one that answers the question asked.

SIXTH, THE CONFOUND IS CARRIED RATHER THAN ARGUED. The 153 cells of
height 1 cannot fail at all, so every rate below is quoted raw AND
conditioned on h >= 2, and the separation is computed on both
populations. A predictor that only separates the h = 1 cells from the
rest is measuring the confound.

WHAT WAS ALREADY MEASURED BEFORE THE SLATE WAS FROZEN, stated so that
no prediction below is read as one it is not. One cost probe ran: eight
cells at depths 21 to 30, which decided the extension's range. The
whole deep block is cheap -- (40, 21) at rank 19 costs 0.50 s and
15,476 nodes, (40, 30) at rank 10 costs 0.01 s and 79 nodes, and the
rank-1 cells are instant -- so the depth extension is priced in
seconds, not minutes, and nothing about it was in question. No
predictor and no residual was computed before the freeze.

THE SLATE, frozen before any engine code.

PREDICTIONS.

P1. NO CANDIDATE SEPARATES. No predictor achieves a threshold with zero
false positives and zero false negatives over the failing cells, on
either population. This is the headline and the rig is built to be able
to refute it.

P2. THE PLATEAU IS THE BEST OF THEM. Plateau_4 carries the largest
rank-sum statistic of the four candidates on the h >= 2 population,
scored so that SMALL plateau predicts failure, and the failing cells'
median plateau_4 is strictly below the non-failing cells'.

P3. THE BALL COUNT IS POSITIVE EVERYWHERE AND SO SELECTS NOTHING. The
heuristic log-count at radius (ph - 1) sqrt(M) is at least 0 at every
one of the failing cells -- it must be, a shorter vector existing there
-- and also at more than half of the non-failing cells with h >= 2, so
its best threshold leaves many false positives.

P4. THE STALL IS FLAT. The rate of a repeated part in the pure argmin
differs by less than 20 percentage points between the failing and the
non-failing cells.

P5. J's DIVISOR COUNT SEPARATES NOTHING, rank-sum statistic within 0.15
of a half on the h >= 2 population.

P6. NO THIRD RESIDUAL CLASS. The exhibited minimisers of the extended
chart carry exactly the three residuals 1, A and B, and every
cyclotomic part is a pure product.

P7. THE DEPTH DENSITY KEEPS RISING. The conditioned failure rate at
J >= 21 is above the 9.0% the earlier chart measured at J = 13..20.

KILL CRITERIA, each an OBSERVABLE the rig prints and never an
inference. The meaning is weighed after the run.

K-A. A candidate predictor printing 0 false positives AND 0 false
negatives at its best threshold on either population. (Refutes P1, and
it is the outcome this rig would most like to have.)

K-B. Any control printing a mismatch: the parent's committed values,
the rank-1 closed form, the monotonicity comparisons, the splitter
multiplied back, the covolume against an independent determinant, the
ball formula against its exact small-dimension values, the two family
tables' pure halves against each other, or the reporter's own two
controls.

K-C. A residual over the extended chart's exhibited minimisers that is
not 1, A or B. (Refutes P6, and it is a find rather than a fault.)

K-D. A cell stalling at the node cap.

K-E. h rising in M or falling in J anywhere on the extended chart.

K-F. A residual the exact unit-circle test rejects.

THE ARMS.

1. THE EXTENDED CHART. h(M, J) over M = 4..40, J = 2..30, by the
   parent's incremental reduction and bounded enumeration, imported
   rather than reimplemented so that the 550 overlapping cells are the
   parent's own route and not a re-derivation of it.
2. THE HARVEST. Every exhibited minimiser split into monomial,
   cyclotomic and residual parts; the residual tally over the whole
   chart, each tested for all roots on the unit circle; each cyclotomic
   part tested for being a pure product; each split multiplied back to
   its own witness.
3. THE FAMILY BOUNDS. The pure table and the two enriched tables over
   one multiset enumeration, giving ph, its argmin multiset, and the
   least height over (pure product) times A and times B at every cell.
4. THE PREDICTORS. Five quantities at every cell beside the failure
   flag -- the gap as a descriptor, the stall, J's divisor count, the
   two ball counts, and the two plateaus -- printed as a table and as a
   per-predictor separation report on both populations.
5. THE CONTROLS, run before any verdict is read.

FINDINGS.

F1. EVERY CONTROL PASSES AND THE PARENT'S WHOLE RECORD REPRODUCES.
C1, the ball volume against five exact values and the stall and divisor
counts against ten hand values, 0 wrong. C2, monotonicity at 1,324
comparisons, 0 violations. C3, the rank-1 closed form h(M, M-1) =
C(M-1, (M-1)//2) at 28 cells reaching C(30, 15) = 155,117,520, 0
mismatches -- and it now certifies the NEW region, the deep chart's
narrow edge being rank 1. C4, the covolume read off the Gram-Schmidt
norms against an independent Bareiss determinant of the Gram matrix, 23
cells, 0 mismatches. C5, the splitter multiplied back at all 695
witnesses, 0 failing to reconstruct. C6, the parent's three committed
cells exact in h, residual and cyclotomic multiset. C7 is the strongest
of them: all ELEVEN of the parent's committed aggregates over its own
rectangle -- 550 cells, 530 tight, 20 below, (362, 3) and (188, 17) by
depth, 3 residuals, 0 non-pure cyclotomic parts, 16 enriched
attainments, worst cell (40, 16) at 20,287 nodes, 433,866 nodes total
-- recomputed inside the wider sweep, 0 mismatching. The reporter's own
two controls behave: the gap separates perfectly (rank-sum 1.000, 0
errors) and the hash does not (0.496, and its best threshold is the
degenerate one). The whole chart is 695 cells and 611,632 nodes in
about 28 s, worst cell (40, 23) at 28,064 nodes, and the two depth
bands split that as 22.5 s over the earlier 550 cells against 5.5 s
over the 145 the extension adds. The first of those is the PARENT's own
22.6 s reproduced by a different rig on the same cells, which is a
cheap independent check on the instrument's cost that nothing was
asking for; the second retires this record's pre-freeze estimate of
"about 3 s", which came from an eight-cell probe and undersampled by
nearly half. Both timings -- the
chart's and the whole rig's -- are quoted to the nearest second because
both move by a few tenths between runs while every other value holds to
the digit.

F2. NO PREDICTOR SELECTS A FAILING CELL AND P1 HOLDS. K-A never fires.
Of the eight candidates on both populations, seven have a best
threshold that is the DEGENERATE one -- predict that nobody fails, 0
false positives and 83 false negatives -- which is what a best
threshold does when no cut beats calling the whole chart clean. The
single exception is the ball count at the pure radius, whose best cut
buys 7 of the 83 failures for 1 false positive. The failure flag is not
a function of any one of these numbers -- BUT THE QUESTION AS ASKED IS
ONE-SIDED AND THAT LIMIT IS LOAD-BEARING HERE RATHER THAN INCIDENTAL.
The reporter's best threshold predicts failure on one SIDE of a cut, so
it cannot express a WINDOW at all, and the rank scored degenerate for
exactly that reason while a two-sided rank rule is the very next
finding. So these seven verdicts are verdicts about ONE-SIDED cuts and
nothing more. No variable but the rank was tried as a window, and
whether any of the other seven carries one is untested rather than
answered.

F3. THE RANK WINDOW IS A SHARP TWO-SIDED NECESSARY CONDITION, AND IT IS THE
ONLY THING HERE THAT SELECTS ANYTHING. Every one of the 83 failures sits at
rank 5..18. Outside that band 325 cells fail ZERO times -- 115 at rank 1..4 and
210 at rank 19..38 -- and both tails are populous rather than thin. THAT RAW
COUNT CARRIES THE SAME HEIGHT CONFOUND THE DEPTH RATES ARE CONDITIONED FOR, AND
IT IS NOT SPREAD EVENLY BETWEEN THE TAILS. A cell with h = 1 cannot fail, and
the high tail holds 100 of them against the low tail's 4: conditioned on h >= 2
the clean outside is 221 cells rather than 325, 111 low and 110 high, and at h
>= 10 it is 140, 97 low and 43 high. So the two tails are close in CONDITIONED
strength while the raw counts read two to one, and the low tail is the
better-evidenced of the two on every floor -- the opposite of what the raw
numbers say (arm 6, post-hoc). Neither tail is thin after conditioning, and
neither is explained by the height floor: 97 and 43 cells with h >= 10 have
every room to fail and none does. The band is DEFINED from the failing set, so
"all failures inside it" is a tautology and carries nothing; what carries is
the clean cells outside that COULD have failed, and above all that THE WINDOW
DID NOT WIDEN. It was 5..18 on the 550-cell chart, and adding 145 cells at
depths 21 to 30 -- which reach rank 1 at the narrow edge and are where the
failures now crowd -- left both endpoints exactly where they were. That is an
out-of-sample survival and not a fit, BUT THE TWO WALLS WERE NOT TESTED EQUALLY
AND THE ASYMMETRY IS LARGE. A new cell has J >= 21 and M <= 40, so its rank is
at most 19: of the 145, forty sit at rank <= 4 and exactly ONE at rank 19, with
the remaining 104 inside the window. So the LOW wall was offered forty fresh
chances to break and did not, while the HIGH wall was offered one. The low wall
is the half this chart tested; the high wall stands on the earlier chart's
evidence almost alone, and a census that tested it would have to widen in M.
The rank's own degenerate score in F2 is not evidence against this and never
was: the reporter cuts on one side and a window has two, so the two readings
are of different rules and not of different data. Inside the band the condition
is far from sufficient: 83 of 370 cells fail, 22.4% raw and 25.9% over the 321
that can fail at all. Crossed with the depth, the band holds the whole story --
3 of 154 at J <= 12, 17 of 112 at J = 13..20, and 63 of 104 at J >= 21, so
1.9%, 15.2% and 60.6% raw and 2.9%, 15.2% and 60.6% conditioned, the last two
unmoved because no cell in either has h = 1 -- and outside it the rate is 0 at
every depth on either reading. (Post-hoc: the window is arm 3's printed range
and the rate inside it is arm 6's, neither predicted.)

F4. THE PURE-PRODUCT LAW COLLAPSES IN THE DEPTH RATHER THAN FAILING
SPORADICALLY, AND P7 HOLDS BY A WIDE MARGIN. The failure rate is 0.8%
at J <= 12, 9.0% at J = 13..20, and 43.4% at J >= 21 -- 63 of 145
cells. ONLY THE SHALLOWEST OF THE THREE IS CONFOUNDED, and the other
two are exempt for a reason worth stating rather than leaving to a
reader: all 153 height-1 cells -- the ones that cannot fail -- sit at
J <= 12, so both deeper bands are entirely h >= 2 and their 9.0% and
43.4% are the raw AND the conditioned rate at once. The shallow band
alone moves, 0.8% raw against 1.4% over the 209 of its 362 that can
fail at all. Read across the three bands the law does not have
exceptions past a boundary; it stops being the answer.

F5. THE THIRD MEMBER EXISTS AND P6 IS REFUTED -- AND SO IS THE READING
THAT THE MULTIPLIERS HAVE LEADING COEFFICIENT 2. The extended chart's
695 exhibited minimisers carry FIVE distinct residuals, not three: 1 at
612 cells, B at 51 (47 of them past depth 20), A at 29 (13 past), and
two new ones. Exact division over the known members separates them.
A*B = 4 + 14x + 26x^2 + 31x^3 + 26x^4 + 14x^5 + 4x^6 appears at (39,
24) and (40, 25) and is NOT a new member of anything -- the class is
closed under multiplication, so a product of members is a member for
free, and what those two cells report is the first cell where ONE
multiplier does not suffice. The other is genuine: C = 3 + 5x + 3x^2 at
(39, 28), divisible by neither A nor B, reciprocal, and with leading
coefficient THREE. Its roots are (-5 +- i sqrt(11))/6, of modulus
squared (25 + 11)/36 = 1 exactly, so they are on the circle and its
y-polynomial 3y + 5 has its single root -5/3 inside (-2, 2), which is
what the Sturm test reports. So the description "reciprocal with
leading coefficient 2" was a fact about the two members the earlier
chart happened to reach, and the CLASS -- integer polynomials with
every root on the unit circle -- is what survives: all five residuals
pass the exact unit-circle test, K-F never fires, and every one of the
695 cyclotomic parts is a pure product.

F6. AT EVERY FAILURE BUT THREE, ONE KNOWN MULTIPLIER STILL ATTAINS h.
The A-enriched and B-enriched families are swept over the same multiset
enumeration as the pure family, so the three are three heights of one
object. Over the whole chart the better of them beats the pure bound at
EXACTLY the 83 failing cells and nowhere else -- 57 further cells are
too narrow to hold either multiplier and carry no enriched bound at all
-- and at 80 of those 83 it equals h exactly (arm 6, post-hoc). The
three exceptions are exactly the three cells naming a residual the pair
cannot make: (39, 24) at h = 6,296 against A's 6,763 and B's 7,734, and
(40, 25) at h = 12,075 against 12,825 and 12,702, both needing the
product A*B; and (39, 28) at h = 170,792 against 288,844 and 173,604,
which needs C. So the enrichment never improves without being exactly
right, as on the earlier chart, and where it misses it names what is
missing.

F7. THE PLATEAU IS REFUTED AND IN THE DIRECTION OPPOSITE TO ITS OWN
MECHANISM. P2 predicted small plateau at the failures -- a cell where
four atoms of width are free to the pure family being where an
enrichment can pay for itself. Scored that way plateau_4 has rank-sum
0.077 on the whole chart and 0.110 on the h >= 2 cells, so the failures
sit at LARGE plateau: the pure bound is STEEP in the width there, not
flat. The absolute reading is confounded -- heights run to 10^8 where
the failures crowd -- and the scale-free ratio (post-hoc, arm 6) cuts
the signal without reversing it: log10 ph(M-4, J)/ph(M, J) has rank-sum
0.776 for LARGE, median 0.687 at the failures against 0.301 elsewhere,
a factor of 4.9 against 2.0 over four atoms. So roughly half the
absolute reading was the depth confound and a real effect survives it,
pointing the other way from the hand attack. The mechanism to keep is
not that enrichment needs slack; it is that a pure family degrading
fast as the width narrows is a pure family far from the true minimum.

F8. THE GAUSSIAN HEURISTIC UNDERCOUNTS WHERE IT MATTERS AND P3 IS HALF
REFUTED. The ball count at the pure radius was predicted at least 0 at
every failing cell, a shorter vector provably existing there. Its
minimum over the failures is -2.159: at those cells the L2 ball of
radius (ph - 1) sqrt(M) has volume below the covolume and still
contains a lattice point. The prediction's other half holds -- the
count is near 0 at the median non-failing cell too and its best cut is
almost degenerate -- so the heuristic does not select. What it buys is
a measured statement about the heuristic itself on this family, which
is that the sup-norm question is not well approximated by the L2 ball
it is enumerated in.

F9. THE STALL AND THE ARITHMETIC ARE FLAT, AS PREDICTED. P5 holds:
J's divisor count has rank-sum 0.589 on the h >= 2 cells, 0.089 from a
half. P4 holds as a RATE -- a repeated part is present at essentially
every cell on both sides -- while the stall's MAGNITUDE, the largest
multiplicity in the pure argmin, tracks the depth (rank-sum 0.863),
which is the depth density read a third way and not an independent
variable. The pure argmins at the deep cells are long runs of 1s, which
is why.

THE RUN RECORD. Three runs of the whole rig. The FIRST is superseded and
carried nothing wrong: arms 1 to 5 printed every value quoted above and
each later run reproduces every one of them exactly. Only the two
TIMINGS move between runs, the chart's and the whole rig's, by a few
tenths of a second each, and that is the only reproduction claimed
here. The LATER ones add arm 6's post-hoc measurements a piece at a
time -- the enrichment counts among them, added because two sentences
of this record would otherwise have rested on a reading of 83 printed
rows rather than on a printed count -- and the last of them removes a
DUPLICATED BASIS REDUCTION that had been costing the chart ten seconds
while touching no result at all. Every post-hoc measurement is labelled
as such wherever it is quoted.
Before either, a SMOKE RUN at M <= 14, J <= 8 exercised every arm with
an EMPTY failing set and found two faults that no full run could have
shown: the plateau's subtraction was written in the wrong order in the
hand attack, printing a column of negative zeros, and C7 compared its
eleven whole-rectangle aggregates against a narrowed sweep's and
reported eleven mismatches for a rig that was working. The first is
corrected in the paragraph that states it; the second now reports
itself unexercised, which is the guard C6 already carried for a single
cell. Both were fixed before any science printed. Wall about 30 s,
single
process, well inside the ordinary analysis footprint.
"""
import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time
import math
from math import comb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_flatten_offchart import NodeCap
from explore_flatten_lattice import basis
from explore_flatten_family import (route_h, lll_incr, split_witness,
                                    polydiv,
                                    as_pure_product, on_unit_circle,
                                    family_tables, family_bound,
                                    divisor_multiset, mulpoly, phi_poly,
                                    poly_trim, AQ)

BQ = [2, 3, 2]
SWEEP_M = 40
SWEEP_J = 30
OLD_J = 20

# The parent's committed aggregate record over its own rectangle,
# M = 4..40 and J = 2..20. Every one of these is quoted from the frozen
# findings of explore_flatten_family.py and is an external answer key
# here: this rig recomputes the rectangle inside a wider sweep and must
# reproduce all of it.
COMMITTED = {
    "cells": 550,
    "tight": 530,
    "below": 20,
    "shallow": (362, 3),      # J <= 12: cells, failures
    "deep": (188, 17),        # J = 13..20: cells, failures
    "residuals": 3,
    "nonpure": 0,
    "enriched_attains": 16,
    "worst_cell": (40, 16),
    "worst_nodes": 20287,
    "nodes": 433866,
}
PARENT_CELLS = {(21, 12): (39, (1,) * 9 + (2, 2, 3)),
                (23, 10): (9, (1,) * 6 + (2, 2, 3, 5)),
                (25, 12): (25, (1,) * 8 + (2, 2, 3, 5))}
LOG10 = math.log(10.0)


# ------------------------------------------- the measuring instruments

def log10_frac(q):
    """log10 of a positive Fraction, exact-integer logs on both halves
    so that a covolume far outside float range still reads."""
    return math.log10(q.numerator) - math.log10(q.denominator)


def log10_ball(r, log10R):
    """log10 of the volume of the r-dimensional L2 ball of radius R:
    pi^(r/2) R^r / Gamma(r/2 + 1)."""
    return ((r / 2.0) * math.log10(math.pi) + r * log10R
            - math.lgamma(r / 2.0 + 1.0) / LOG10)


def int_det(Mx):
    """Determinant of an integer matrix by Bareiss -- exact, integer
    throughout, and an INDEPENDENT route to the covolume the reduction
    reads off its Gram-Schmidt norms."""
    n = len(Mx)
    Mx = [row[:] for row in Mx]
    sign, prev = 1, 1
    for k in range(n - 1):
        if Mx[k][k] == 0:
            piv = None
            for i in range(k + 1, n):
                if Mx[i][k]:
                    piv = i
                    break
            if piv is None:
                return 0
            Mx[k], Mx[piv] = Mx[piv], Mx[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                Mx[i][j] = (Mx[i][j] * Mx[k][k]
                            - Mx[i][k] * Mx[k][j]) // prev
        prev = Mx[k][k]
    return sign * Mx[n - 1][n - 1]


def gram(B):
    return [[sum(x * y for x, y in zip(a, b)) for b in B] for a in B]


def ndivisors(n):
    return sum(1 for d in range(1, n + 1) if n % d == 0)


def max_multiplicity(parts):
    """The largest number of equal parts in a multiset -- the STALL."""
    if not parts:
        return 0
    best = 0
    for p in set(parts):
        best = max(best, sum(1 for q in parts if q == p))
    return best


# -------------------------------------------- the separation reporter

def rank_sum(pos, neg):
    """P(a random positive scores above a random negative), ties at a
    half -- the Mann-Whitney statistic, computed directly because the
    populations here are small and a rank table would only hide the
    tie handling."""
    if not pos or not neg:
        return None
    tot = 0.0
    for a in pos:
        for b in neg:
            tot += 1.0 if a > b else (0.5 if a == b else 0.0)
    return tot / (len(pos) * len(neg))


def best_threshold(pos, neg):
    """The threshold on the score minimising false positives plus false
    negatives, predicting POSITIVE at score >= t. Returns the threshold
    and its two error counts."""
    if not pos or not neg:
        return None, None, None
    cands = sorted(set(pos + neg))
    cands = cands + [cands[-1] + 1.0]
    best = None
    for t in cands:
        fn = sum(1 for a in pos if a < t)
        fp = sum(1 for b in neg if b >= t)
        if best is None or (fp + fn) < best[1] + best[2]:
            best = (t, fp, fn)
    return best


def quantiles(v):
    if not v:
        return None
    s = sorted(v)
    n = len(s)
    return (s[0], s[n // 4], s[n // 2], s[(3 * n) // 4], s[-1])


def report(name, score, flag, cells, sense=1):
    """One predictor, one population. `score` maps a cell to a float or
    to None where the quantity is undefined; `sense` is +1 when LARGE
    predicts failure and -1 when small does. Prints the rank-sum
    statistic, the best threshold's two error counts, and the two
    five-number summaries -- and returns the error counts so the caller
    can fire the perfect-separation kill on an observable rather than
    on a reading of the text. THE SUMMARIES AND THE THRESHOLD PRINT IN
    THE PREDICTOR'S OWN UNITS and never in the sense-adjusted ones the
    ranking uses: a column of negated plateaus is a column no reader
    can check against the cell table above it."""
    pos = [score[c] for c in cells
           if flag[c] and score.get(c) is not None]
    neg = [score[c] for c in cells
           if not flag[c] and score.get(c) is not None]
    skipped = sum(1 for c in cells if score.get(c) is None)
    rs = rank_sum([sense * a for a in pos], [sense * b for b in neg])
    t, fp, fn = best_threshold([sense * a for a in pos],
                               [sense * b for b in neg])
    qp, qn = quantiles(pos), quantiles(neg)
    print("   %-22s n = %3d + %4d (%3d undefined)  rank-sum %s"
          % (name, len(pos), len(neg), skipped,
             "%.3f" % rs if rs is not None else "n/a"))
    if t is not None:
        print("      failure predicted at score %s %-12s "
              "false positives %4d, false negatives %3d"
              % (">=" if sense > 0 else "<=", "%.4g" % (sense * t),
                 fp, fn))

    def fmt(q):
        return ("n/a" if q is None else
                "[%.4g %.4g %.4g %.4g %.4g]" % tuple(x + 0.0 for x in q))

    print("      failing    min q1 med q3 max %s" % fmt(qp))
    print("      not failing            same %s" % fmt(qn))
    return fp, fn


def main():
    t_all = time.time()
    fired = dict(("K-" + c, 0) for c in "ABCDEF")

    print("=" * 70)
    print("explore_flatten_select.py -- what selects a failing cell?")
    print("=" * 70)

    # ------------------------------ C1: the measuring instruments first
    print("\n[C1] the measuring instruments, before anything uses them")
    exact = [(1, 0.0, 2.0), (2, 0.0, math.pi), (3, 0.0, 4 * math.pi / 3),
             (4, 0.0, math.pi ** 2 / 2), (2, 1.0, math.pi * 100.0)]
    badv = 0
    for (r, lR, want) in exact:
        got = 10.0 ** log10_ball(r, lR)
        if abs(got - want) > 1e-9 * want:
            badv += 1
            fired["K-B"] += 1
            print("   K-B ball volume r=%d R=1e%g: got %r want %r"
                  % (r, lR, got, want))
    print("   ball volume against %d exact values: %d wrong"
          % (len(exact), badv))
    hand = [((1, 1, 2), 2), ((3,), 1), ((), 0), ((4, 4, 4, 1), 3)]
    badm = 0
    for (S, want) in hand:
        if max_multiplicity(S) != want:
            badm += 1
            fired["K-B"] += 1
            print("   K-B stall on %s: got %d want %d"
                  % (list(S), max_multiplicity(S), want))
    badd = 0
    for (n, want) in [(1, 1), (6, 4), (12, 6), (16, 5), (17, 2), (30, 8)]:
        if ndivisors(n) != want:
            badd += 1
            fired["K-B"] += 1
    print("   stall on %d hand multisets: %d wrong; divisor count on 6 "
          "hand values: %d wrong" % (len(hand), badm, badd))

    # --------------------------------------- arm 1: the extended chart
    print("\n[arm 1] the extended chart -- h(M, J), M = 4..%d, J = 2..%d"
          % (SWEEP_M, SWEEP_J))
    t = time.time()
    H, NODES, COVOL = {}, {}, {}
    # SPLIT BY DEPTH BAND, because what the extension COSTS is a claim
    # this rig makes and an eight-cell probe is not a measurement of it.
    band_t = {"old": 0.0, "new": 0.0}
    for M in range(4, SWEEP_M + 1):
        t_row = time.time()
        for J in range(2, min(SWEEP_J, M - 1) + 1):
            t_cell = time.time()
            try:
                h, v, nodes, red = route_h(M, J)
            except NodeCap:
                fired["K-D"] += 1
                print("   K-D stalled at M=%d J=%d rank=%d" % (M, J, M - J))
                continue
            H[(M, J)] = (h, v)
            NODES[(M, J)] = nodes
            # THE REDUCTION IS NOT REDONE. route_h returns its reduced
            # data as a fourth value and the covolume is the product of
            # the Gram-Schmidt norms it already carries, so reading it
            # costs nothing. An earlier draft discarded that value and
            # called the reduction a second time per cell, which made
            # this chart's 695 cells cost more than the parent's 550
            # plus the extension's 145 -- a timing that could not be
            # reconciled from the page, which is how it was found.
            COVOL[(M, J)] = sum(log10_frac(a) for a in red[2]) / 2.0
            band_t["old" if J <= OLD_J else "new"] += time.time() - t_cell
        print("   M = %2d done, %.1f s (%.1f s in)"
              % (M, time.time() - t_row, time.time() - t))
    old = [c for c in H if c[1] <= OLD_J]
    new = [c for c in H if c[1] > OLD_J]
    print("   %d cells decided in %.1f s, %d nodes; %d in the earlier "
          "rectangle and %d new"
          % (len(H), time.time() - t, sum(NODES.values()), len(old),
             len(new)))
    print("   worst cell %s at %d nodes"
          % (max(NODES, key=lambda c: NODES[c]), max(NODES.values())))

    print("   of that, %.1f s on the %d cells at J <= %d and %.1f s "
          "on the %d the depth extension adds"
          % (band_t["old"], len(old), OLD_J, band_t["new"],
             len(new)))
    print("\n   h(M, J), rows M, columns J = %d..%d" % (OLD_J + 1, SWEEP_J))
    print("      M |" + "".join("%12d" % J
                                for J in range(OLD_J + 1, SWEEP_J + 1)))
    for M in range(4, SWEEP_M + 1):
        row = "".join("%12s" % (H[(M, J)][0] if (M, J) in H else "")
                      for J in range(OLD_J + 1, SWEEP_J + 1))
        if row.strip():
            print("   %4d |%s" % (M, row))

    # -------------------------------------------- C2: monotonicity
    checks = 0
    for (M, J), (h, _) in sorted(H.items()):
        if (M + 1, J) in H:
            checks += 1
            if H[(M + 1, J)][0] > h:
                fired["K-E"] += 1
                print("   K-E h rises in M at M=%d J=%d" % (M, J))
        if (M, J + 1) in H:
            checks += 1
            if H[(M, J + 1)][0] < h:
                fired["K-E"] += 1
                print("   K-E h falls in J at M=%d J=%d" % (M, J))
    print("\n[C2] monotonicity: %d comparisons, %d violations"
          % (checks, fired["K-E"]))

    # ----------------------------- C3: the rank-1 closed form, deepened
    n3 = mism3 = 0
    for M in range(3, SWEEP_J + 2):
        if (M, M - 1) not in H:
            continue
        n3 += 1
        if H[(M, M - 1)][0] != comb(M - 1, (M - 1) // 2):
            mism3 += 1
            fired["K-B"] += 1
            print("   K-B M=%d rank 1: got %d want %d"
                  % (M, H[(M, M - 1)][0], comb(M - 1, (M - 1) // 2)))
    print("[C3] the rank-1 closed form h(M, M-1) = C(M-1, (M-1)//2): "
          "%d cells, %d mismatches (largest %d)"
          % (n3, mism3, comb(SWEEP_J, SWEEP_J // 2)))

    # ------------------------------------- C4: the covolume, two routes
    n4 = mism4 = 0
    sample = sorted(H)[::37] + [(40, 21), (40, 30), (22, 21), (12, 2)]
    for c in sample:
        if c not in H:
            continue
        n4 += 1
        d = int_det(gram(basis(c[0], c[1])))
        if d <= 0:
            mism4 += 1
            fired["K-B"] += 1
            print("   K-B M=%d J=%d Gram determinant %d is not positive"
                  % (c[0], c[1], d))
            continue
        if abs(0.5 * math.log10(d) - COVOL[c]) > 1e-6:
            mism4 += 1
            fired["K-B"] += 1
            print("   K-B M=%d J=%d covolume %.9f against determinant "
                  "route %.9f" % (c[0], c[1], COVOL[c],
                                  0.5 * math.log10(d)))
    print("[C4] the covolume off the Gram-Schmidt against an independent "
          "integer determinant: %d cells, %d mismatches" % (n4, mism4))

    # ----------------------------------------------- arm 2: the harvest
    print("\n[arm 2] the harvest -- every exhibited minimiser split")
    SPLIT = {}
    tally, shifts, nonpure = {}, 0, []
    for (M, J), (h, v) in sorted(H.items()):
        sh, cyc, res = split_witness(v)
        SPLIT[(M, J)] = (sh, cyc, res)
        if sh:
            shifts += 1
        tally.setdefault(res, []).append((M, J, h))
        if as_pure_product(cyc) is None:
            nonpure.append((M, J, h, cyc))
    print("   %d witnesses, %d carrying a monomial factor"
          % (len(H), shifts))
    print("   %d distinct residuals over the whole chart:" % len(tally))
    for res in sorted(tally, key=lambda r: (len(r), r)):
        rcells = tally[res]
        ok, why, Q, cnt, deg = on_unit_circle(list(res))
        if not ok:
            fired["K-F"] += 1
        if list(res) not in ([1], list(AQ), list(BQ)):
            fired["K-C"] += 1
        deepc = [c for c in rcells if c[1] > OLD_J]
        print("      residual %-24s %3d cells (%d past depth %d)   "
              "unit circle: %s (%s)"
              % (str(list(res)), len(rcells), len(deepc), OLD_J, ok, why))
        if list(res) != [1]:
            print("         y-polynomial %s; cells %s"
                  % (Q, rcells if len(rcells) <= 24 else
                     "%d cells" % len(rcells)))
    print("   cyclotomic parts that are NOT pure products: %d"
          % len(nonpure))
    for row in nonpure[:20]:
        print("      M=%2d J=%2d h=%d cyclotomic %s" % row)

    # C5: the splitter multiplied back at every witness of the chart.
    n5 = bad5 = 0
    for (M, J), (sh, cyc, res) in sorted(SPLIT.items()):
        n5 += 1
        prod = [0] * sh + [1]
        for d in cyc:
            prod = mulpoly(prod, phi_poly(d))
        prod = mulpoly(prod, list(res))
        w = poly_trim(list(H[(M, J)][1]))
        if prod != w and [-c for c in prod] != w:
            bad5 += 1
            fired["K-B"] += 1
            print("   K-B M=%d J=%d splitter does not reconstruct its "
                  "witness" % (M, J))
    print("   [C5] the split multiplied back: %d witnesses, %d failing "
          "to reconstruct" % (n5, bad5))

    # ------------------------------------------ arm 3: the family bounds
    print("\n[arm 3] the pure family and its two enrichments")
    t = time.time()
    pure_t, enrA_t = family_tables(SWEEP_M - 1, AQ)
    pure_t2, enrB_t = family_tables(SWEEP_M - 1, BQ)
    if pure_t[0] != pure_t2[0]:
        fired["K-B"] += 1
        print("   K-B the two runs' pure tables differ")
    print("   family tables to degree %d: %.1f s, %d keys, the two runs' "
          "pure halves identical: %s"
          % (SWEEP_M - 1, time.time() - t, len(pure_t[0]),
             pure_t[0] == pure_t2[0]))

    PH, PW, EH = {}, {}, {}
    for (M, J) in sorted(H):
        ph, pw = family_bound(pure_t, J, M - 1)
        if ph is None:
            continue
        PH[(M, J)] = ph
        PW[(M, J)] = pw
        ea, _ = family_bound(enrA_t, J, M - 1 - (len(AQ) - 1))
        eb, _ = family_bound(enrB_t, J, M - 1 - (len(BQ) - 1))
        EH[(M, J)] = (ea, eb)

    cells = sorted(PH)
    FAIL = dict((c, H[c][0] < PH[c]) for c in cells)
    for c in cells:
        if H[c][0] > PH[c]:
            fired["K-B"] += 1
            print("   K-B h ABOVE the pure bound at M=%d J=%d: %d > %d"
                  % (c[0], c[1], H[c][0], PH[c]))
    nfail = sum(1 for c in cells if FAIL[c])
    print("   %d cells with a pure bound, %d TIGHT, %d STRICTLY BELOW"
          % (len(cells), len(cells) - nfail, nfail))

    print("\n   the failure rate by depth band, raw and conditioned:")
    bands = [("J <= 12", lambda J: J <= 12),
             ("J = 13..20", lambda J: 13 <= J <= 20),
             ("J >= 21", lambda J: J >= 21)]
    for (nm, sel) in bands:
        for cut in (1, 2, 10):
            sub = [c for c in cells if sel(c[1]) and H[c][0] >= cut]
            bad = [c for c in sub if FAIL[c]]
            print("      %-11s h >= %2d: %3d cells, %2d failing (%.1f%%)"
                  % (nm, cut, len(sub), len(bad),
                     100.0 * len(bad) / len(sub) if sub else 0.0))
    print("   of the %d cells, %d have h = 1 and so cannot fail at all"
          % (len(cells), sum(1 for c in cells if H[c][0] == 1)))
    print("\n   every cell where h is strictly below the pure bound:")
    for c in cells:
        if not FAIL[c]:
            continue
        ea, eb = EH[c]
        print("      M=%2d J=%2d rank=%2d  h=%-8d pure %-8d gap %-6d "
              "A-enriched %-8s B-enriched %-8s residual %s"
              % (c[0], c[1], c[0] - c[1], H[c][0], PH[c],
                 PH[c] - H[c][0], ea, eb, list(SPLIT[c][2])))
        print("         pure argmin multiset %s" % (list(PW[c]),))

    # ----------------------------------------------- arm 4: predictors
    print("\n[arm 4] the predictors, printed beside the failure flag")
    GAP, STALL, NDIV, BALLH, BALLP, PL4, PL2, NOISE = ({}, {}, {}, {},
                                                       {}, {}, {}, {})
    for c in cells:
        M, J = c
        r = M - J
        h, ph = H[c][0], PH[c]
        GAP[c] = float(ph - h)
        STALL[c] = float(max_multiplicity(PW[c]))
        NDIV[c] = float(ndivisors(J))
        BALLH[c] = (log10_ball(r, math.log10(h) + 0.5 * math.log10(M))
                    - COVOL[c])
        BALLP[c] = (None if ph <= 1 else
                    log10_ball(r, math.log10(ph - 1)
                               + 0.5 * math.log10(M)) - COVOL[c])
        PL4[c] = (float(PH[(M - 4, J)] - ph) if (M - 4, J) in PH else None)
        PL2[c] = (float(PH[(M - 2, J)] - ph) if (M - 2, J) in PH else None)
        NOISE[c] = float((M * 7919 + J * 104729) % 1000)

    print("\n    M   J rank        h     pure gap stall nd  ball(h) "
          "ball(p-1) pl4 pl2 FAIL")
    for c in cells:
        M, J = c
        print("   %2d %3d %4d %8d %8d %3d %5d %2d %8.2f %9s %3s %3s %s"
              % (M, J, M - J, H[c][0], PH[c], int(GAP[c]), int(STALL[c]),
                 int(NDIV[c]), BALLH[c],
                 "-" if BALLP[c] is None else "%.2f" % BALLP[c],
                 "-" if PL4[c] is None else "%d" % PL4[c],
                 "-" if PL2[c] is None else "%d" % PL2[c],
                 "FAIL" if FAIL[c] else ""))

    pops = [("all %d cells" % len(cells), cells),
            ("the h >= 2 cells", [c for c in cells if H[c][0] >= 2])]
    cand = [("gap [DESCRIPTOR]", GAP, 1),
            ("noise [NEGATIVE]", NOISE, 1),
            ("stall", STALL, 1),
            ("divisors of J", NDIV, 1),
            ("ball at h", BALLH, 1),
            ("ball at pure - 1", BALLP, 1),
            ("plateau_4 (small)", PL4, -1),
            ("plateau_2 (small)", PL2, -1),
            ("rank M - J", dict((c, float(c[0] - c[1])) for c in cells), 1),
            ("depth J", dict((c, float(c[1])) for c in cells), 1)]
    for (pname, pop) in pops:
        print("\n   SEPARATION over %s (%d failing)"
              % (pname, sum(1 for c in pop if FAIL[c])))
        for (nm, sc, sense) in cand:
            fp, fn = report(nm, sc, FAIL, pop, sense)
            if nm.startswith("gap"):
                if fp or fn:
                    fired["K-B"] += 1
                    print("      K-B the positive control does not "
                          "separate: %d + %d errors" % (fp, fn))
            elif nm.startswith("noise"):
                if fp == 0 and fn == 0:
                    fired["K-B"] += 1
                    print("      K-B the negative control separates "
                          "perfectly")
            elif fp == 0 and fn == 0:
                fired["K-A"] += 1
                print("      K-A %s SEPARATES PERFECTLY over %s"
                      % (nm, pname))

    # ------------------------------------------ arm 6: POST-HOC, and
    # EVERY NUMBER IT PRINTS IS EXPLORATORY. The slate above was frozen
    # before the engine and its predictions are graded on arms 1 to 5
    # alone. This arm exists because two of those verdicts are
    # UNINTERPRETABLE as printed and a third is a fact about the
    # residuals rather than about the cells:
    #   (a) the plateaus are absolute height differences, and heights
    #       run to 10^8 at the deep cells where the failures crowd, so
    #       a plateau verdict cannot be told apart from the depth
    #       density that arm 3 already measures. The ratio is the
    #       scale-free form and it is one division;
    #   (b) the rank window is printed by the parent and by arm 3 as a
    #       range, and a range is not a rate -- what a band selects is
    #       decided by the failure rate INSIDE it against the rate
    #       outside, which no arm above computes;
    #   (c) a residual that is a PRODUCT of residuals already known is
    #       not a new member of anything, the class being closed under
    #       multiplication. Whether the new residuals factor over the
    #       old ones decides what the companion question answered.
    # None of this was predicted and none of it is graded. It is
    # printed here so that the record's reading of arms 1 to 5 rests on
    # numbers this rig prints rather than on an argument about them.
    print("\n[arm 6] POST-HOC -- what the run raised, ungraded")

    print("   (a) the plateau as a scale-free RATIO, log10 "
          "ph(M-4, J) / ph(M, J)")
    RPL4, RPL2 = {}, {}
    for c in cells:
        M, J = c
        RPL4[c] = (math.log10(PH[(M - 4, J)]) - math.log10(PH[c])
                   if (M - 4, J) in PH else None)
        RPL2[c] = (math.log10(PH[(M - 2, J)]) - math.log10(PH[c])
                   if (M - 2, J) in PH else None)
    for (nm, sc) in [("ratio plateau_4", RPL4), ("ratio plateau_2", RPL2)]:
        for sense in (1, -1):
            report("%s %s" % (nm, "(large)" if sense > 0 else "(small)"),
                   sc, FAIL, [c for c in cells if H[c][0] >= 2], sense)

    print("\n   (b) the failure rate BY RANK, and the band as a rule")
    byrank = {}
    for c in cells:
        byrank.setdefault(c[0] - c[1], [0, 0])
        byrank[c[0] - c[1]][0] += 1
        byrank[c[0] - c[1]][1] += 1 if FAIL[c] else 0
    for r in sorted(byrank):
        n, b = byrank[r]
        print("      rank %2d: %3d cells, %2d failing (%.1f%%)"
              % (r, n, b, 100.0 * b / n))
    # GUARDED, and the guard was earned twice. An empty failing set is a
    # legitimate outcome at any narrower range, and this arm was written
    # AFTER the smoke run that licensed the others -- so it shipped with
    # exactly the crash the earlier smoke run existed to catch, firing
    # after the science had printed. The second smoke run found it.
    fails = [c[0] - c[1] for c in cells if FAIL[c]]
    if not fails:
        print("      no cell fails, so there is no window to report and "
              "no band to cross with the depth")
        lo = hi = None
    else:
        lo, hi = min(fails), max(fails)
    if lo is not None:
        inband = [c for c in cells if lo <= c[0] - c[1] <= hi]
        out = [c for c in cells if not (lo <= c[0] - c[1] <= hi)]
        print("      the band rank %d..%d holds %d of the %d cells and "
              "ALL %d failures; outside it %d cells fail of %d"
              % (lo, hi, len(inband), len(cells),
                 sum(1 for c in inband if FAIL[c]),
                 sum(1 for c in out if FAIL[c]), len(out)))
        # RAW AND CONDITIONED SIDE BY SIDE. The h = 1 cells cannot
        # fail, and they sit INSIDE the window as well as outside it,
        # so a raw in-band rate understates for the same reason a raw
        # depth rate does.
        ib2 = [c for c in inband if H[c][0] >= 2]
        print("      as a rule it is NECESSARY and not sufficient: "
              "inside the band %d of %d fail (%.1f%%) raw, %d of %d "
              "(%.1f%%) at h >= 2"
              % (sum(1 for c in inband if FAIL[c]), len(inband),
                 100.0 * sum(1 for c in inband if FAIL[c])
                 / len(inband),
                 sum(1 for c in ib2 if FAIL[c]), len(ib2),
                 100.0 * sum(1 for c in ib2 if FAIL[c]) / len(ib2)))
        print("      the band crossed with the depth, cells and "
              "failures:")
        for (nm, sel) in bands:
            i = [c for c in inband if sel(c[1])]
            i2 = [c for c in i if H[c][0] >= 2]
            o = [c for c in out if sel(c[1])]
            print("         %-11s in band %3d cells %2d failing "
                  "(%5.1f%% raw; %5.1f%% over the %3d at h >= 2)   "
                  "outside %3d cells %2d failing"
                  % (nm, len(i), sum(1 for c in i if FAIL[c]),
                     100.0 * sum(1 for c in i if FAIL[c]) / len(i)
                     if i else 0.0,
                     100.0 * sum(1 for c in i2 if FAIL[c]) / len(i2)
                     if i2 else 0.0, len(i2),
                     len(o), sum(1 for c in o if FAIL[c])))

    if lo is not None:
        # THE WINDOW'S OWN CONFOUND, counted rather than argued. The
        # depth rates above are conditioned on h >= 2 because a cell
        # with h = 1 cannot fail at all; the window's clean tails were
        # quoted RAW, and the confound is not spread evenly between
        # them. Printed per tail so the two are comparable.
        tails = [("rank <= %d" % (lo - 1), lo - 1, True),
                 ("rank >= %d" % (hi + 1), hi + 1, False)]
        for (nm, cut, low) in tails:
            t = [c for c in cells
                 if ((c[0] - c[1] <= cut) if low
                     else (c[0] - c[1] >= cut))]
            print("      %-11s %3d cells, %3d at h = 1 (cannot fail), "
                  "%3d with h >= 2, %3d with h >= 10, %d failing"
                  % (nm, len(t), sum(1 for c in t if H[c][0] == 1),
                     sum(1 for c in t if H[c][0] >= 2),
                     sum(1 for c in t if H[c][0] >= 10),
                     sum(1 for c in t if FAIL[c])))


    print("\n   (c) do the new residuals FACTOR over the known ones?")
    known = [("A", list(AQ)), ("B", list(BQ))]
    for res in sorted(tally, key=lambda r: (len(r), r)):
        p = list(res)
        parts = []
        again = True
        while again and len(p) > 1:
            again = False
            for (nm, f) in known:
                q = polydiv(p, f)
                if q is not None:
                    parts.append(nm)
                    p = q
                    again = True
                    break
        print("      residual %-24s = %s%s"
              % (str(list(res)), " * ".join(parts) if parts else "",
                 (" * " if parts else "") + str(p)
                 if p != [1] else ""))

    print("\n   (d) the two enriched families over the WHOLE chart")
    # A cell too narrow to hold the multiplier at all -- M - 1 - 4 < J
    # for A, and the same two atoms shallower for B -- has NO enriched
    # bound on that side, and where neither fits there is nothing to
    # compare. Those cells are counted out loud rather than skipped.
    def ebound(c):
        xs = [x for x in EH[c] if x is not None]
        return min(xs) if xs else None

    nofit = [c for c in cells if ebound(c) is None]
    ebeat = [c for c in cells
             if ebound(c) is not None and ebound(c) < PH[c]]
    eatt = [c for c in ebeat if ebound(c) == H[c][0]]
    fatt = [c for c in cells
            if FAIL[c] and ebound(c) is not None
            and ebound(c) == H[c][0]]
    print("      %d cells too narrow to hold either multiplier and so "
          "carrying no enriched bound" % len(nofit))
    print("      A or B beats the pure bound at %d cells and ATTAINS h "
          "at %d of them" % (len(ebeat), len(eatt)))
    print("      of the %d FAILING cells, %d are attained by A or B "
          "alone; the %d misses are %s"
          % (sum(1 for c in cells if FAIL[c]), len(fatt),
             sum(1 for c in cells if FAIL[c]) - len(fatt),
             [c for c in cells if FAIL[c] and c not in fatt]))
    print("      cells where an enrichment beats the pure bound WITHOUT "
          "attaining h: %d" % (len(ebeat) - len(eatt)))

    # -------------------------------------- C6: the parent's own cells
    print("\n[C6] the parent's three committed cells")
    n6 = ok6 = 0
    for c, (wh, parts) in sorted(PARENT_CELLS.items()):
        if c not in SPLIT:
            print("   M=%2d J=%2d NOT IN THIS SWEEP -- control unexercised"
                  % c)
            continue
        n6 += 1
        sh, cyc, res = SPLIT[c]
        good = (H[c][0] == wh and list(res) == list(AQ)
                and cyc == divisor_multiset(parts))
        ok6 += 1 if good else 0
        if not good:
            fired["K-B"] += 1
        print("   M=%2d J=%2d: h %d (want %d), residual %s, cyclotomic "
              "matches the committed product: %s"
              % (c[0], c[1], H[c][0], wh, list(res),
                 cyc == divisor_multiset(parts)))
    print("   %d of 3 exercised, %d reproduce the committed record"
          % (n6, ok6))

    # ------------------------- C7: the parent's whole aggregate record
    # A CONTROL THAT CANNOT RUN MUST SAY SO. Every value in COMMITTED is
    # an aggregate over the whole rectangle M = 4..40, J = 2..20, so a
    # narrowed sweep does not weaken the control, it makes it a
    # comparison between two different populations -- which prints as
    # eleven mismatches and says nothing about this rig. The smoke run
    # at a tiny sweep is what surfaced that, and the guard is the same
    # one C6 already carries at the level of a single cell.
    print("\n[C7] the parent's rectangle recomputed inside this sweep")
    if (SWEEP_M, SWEEP_J) < (40, OLD_J) or OLD_J != 20:
        print("   this sweep is M <= %d, J <= %d and the committed record "
              "is an aggregate over M <= 40, J <= 20 -- control "
              "unexercised" % (SWEEP_M, SWEEP_J))
        print("\nKILLS: %s" % fired)
        print("wall %.1f s" % (time.time() - t_all))
        return
    rect = [c for c in cells if c[1] <= OLD_J]
    rfail = [c for c in rect if FAIL[c]]
    sh12 = [c for c in rect if c[1] <= 12]
    dp = [c for c in rect if 13 <= c[1] <= OLD_J]
    rtally = set(SPLIT[c][2] for c in rect)
    rnon = [c for c in rect if as_pure_product(SPLIT[c][1]) is None]
    reatt = [c for c in rect if EH[c][0] is not None
             and EH[c][0] < PH[c] and EH[c][0] == H[c][0]]
    rnodes = sum(NODES[c] for c in rect)
    worst = max(rect, key=lambda c: NODES[c])
    got = {"cells": len(rect), "tight": len(rect) - len(rfail),
           "below": len(rfail),
           "shallow": (len(sh12), sum(1 for c in sh12 if FAIL[c])),
           "deep": (len(dp), sum(1 for c in dp if FAIL[c])),
           "residuals": len(rtally), "nonpure": len(rnon),
           "enriched_attains": len(reatt), "worst_cell": worst,
           "worst_nodes": NODES[worst], "nodes": rnodes}
    n7 = bad7 = 0
    for k in sorted(COMMITTED):
        n7 += 1
        agree = got[k] == COMMITTED[k]
        if not agree:
            bad7 += 1
            fired["K-B"] += 1
        print("   %-18s committed %-14s recomputed %-14s %s"
              % (k, COMMITTED[k], got[k], "" if agree else "K-B MISMATCH"))
    print("   %d committed values, %d mismatching" % (n7, bad7))

    print("\nKILLS: %s" % fired)
    print("wall %.1f s" % (time.time() - t_all))


if __name__ == "__main__":
    main()
