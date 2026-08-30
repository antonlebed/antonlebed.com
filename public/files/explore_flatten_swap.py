"""explore_flatten_swap.py -- IS THE SWAP A CONSTRUCTION?

explore_flatten_near.py answered the NEAR end of the failing band as a
DESCRIPTION. At 73 of the 83 failing cells of the chart's rank-5..18
rectangle, the lattice minimiser's cofactor is the pure argmin AT THAT
CELL with one cyclotomic block traded for a single non-cyclotomic
factor of equal degree, drawn from the parent chart's committed
residual class. A description is not a construction, and the two
statements are not the same one.

(The senses are the thread's, restated because this rig is read alone.
A vector c on M atoms is the polynomial P(x) = sum_i c_i x^i; its
FLATTENING is the multiplicity of the root 1; its HEIGHT is the sup
norm max_i |c_i|. h(M, J) is the least height of a nonzero P with
flattening at least J and degree < M. A PURE PRODUCT is prod_i
(x^{d_i} - 1) over a multiset D of positive PARTS; ph(M, J) is the
least height of a pure product admissible at the cell. RANK is always
r = M - J. A cell FAILS when h < ph. The COFACTOR of a lattice vector
is q = P/(x-1)^J, of degree at most r - 1.)

THE QUESTION, in one line: is there a family of polynomials, built from
the pure family and a FIXED finite set of multipliers with no lattice
reduction anywhere in it, whose least height is h at the cells where
the pure family alone falls short.

THE MEMBERS, named once and used throughout. The parent chart's
committed residual class is B = 2 + 3x + 2x^2 at 51 cells, A = 2 + 4x +
5x^2 + 4x^3 + 2x^4 at 29, A*B at 2 and C = 3 + 5x + 3x^2 at 1. Only
THREE of those four entries are members in their own right: A*B is a
PRODUCT, and the class is closed under multiplication, so a product of
members is a member for free and costs nothing to admit. The MEMBERS
are A, B, C; the MULTIPLIERS are every product of members inside the
degree budget, the empty product included.

THE FAMILY, defined exactly. At the cell (M, J) of rank r = M - J:

    SWAP(M, J) = { (prod_{d in S'} Phi_d) * m * (x-1)^J }

over every admissible pure cofactor q, every sub-multiset S' of q's own
cyclotomic multiset S, and every multiplier m with deg m = deg q -
deg(prod_{d in S'} Phi_d) -- the block dropped and the multiplier
brought in having EQUAL degree, which is what makes it a swap. hs(M, J)
is the least height over the family.

THE HAND ATTACK, worked before any engine code.

FIRST, THE PARENT'S CYCLOTOMIC MULTISET IS FREE AND EXACT. An
admissible pure cofactor is q = (x-1)^t prod_{d in E} [d]_x with [d]_x
= 1 + x + ... + x^(d-1), the degree budget t + sum_{d in E} (d - 1) <=
r - 1 and the part count |E| <= J + t. Since Phi_1 = x - 1 and [d]_x =
prod_{e | d, e > 1} Phi_e, the cyclotomic multiset of q is

    S = {1}^t  union  union_{d in E} { e : e | d, e > 1 },

and prod_{d in S} Phi_d = q exactly, monic, of degree sum_{d in S}
phi(d) = deg q. So the multiset is read off (t, E) with no
factorisation, and split_witness of the same q must return residual 1
and that same multiset. That is C5 and it is a check on this rig's own
shortcut, not on the parent's.

SECOND, hs >= h ALWAYS, AND THE PROOF IS THE WHOLE REASON THE FAMILY IS
DEFINED WITH EQUAL DEGREES. A family member is (prod S') * m * (x-1)^J.
It is nonzero, being a product of nonzero polynomials. It is divisible
by (x-1)^J, so its flattening is at least J. Its degree is deg(prod S')
+ deg m + J = deg q + J <= (r - 1) + J = M - 1 < M. So it is a nonzero
vector of the lattice at that cell and its height is at least h. If the
multiplier were allowed a degree BELOW the block's the member would
still be a lattice vector, but it would no longer be a swap, and the
family would be the set of all products of cyclotomics and members
inside the degree budget -- a different object with a different name.
The narrower family is the one frozen here.

THIRD, hs <= ph ALWAYS. The empty block with the empty multiplier is in
the family for every parent, so the whole admissible pure family is
inside SWAP, and the least height over that sub-family is ph by
definition. So h <= hs <= ph at every cell, and:

    AT A CLEAN CELL h = ph FORCES hs = h WITH NO MEASUREMENT IN IT.

The clean cells of the rectangle decide nothing and are offered as no
evidence anywhere below. They are run because an enumeration that
silently returned an empty family would also print hs = ph, and the
clean column is where that is caught.

FOURTH, AND IT IS THE READING THAT RESHAPES THIS RIG: 73 OF THE 83
FAILING CELLS ARE FORCED TOO, AND ARE NOT EVIDENCE EITHER. The parent
rig's F2 classifies each failing cell by comparing the minimiser's
cyclotomic multiset S_min against the pure argmin's S_p at the same
cell, and reports 73 cells at which S_min is a SUB-MULTISET of S_p and
the dropped block prod(S_p \\ S_min) has the same degree as the
minimiser's residual R. At such a cell the minimiser's cofactor is
prod(S_min) * R by construction of split_witness, which is exactly the
family member with parent the argmin, block S_p \\ S_min and multiplier
R -- provided R is a multiplier, which the residual census says it is.
So hs = h at those 73 is a RESTATEMENT of F2 and not a measurement of
anything. It is checked here as an instrument control (K3) and it
carries no weight.

WHAT IS LEFT IS THE CONTENT, and it is three things and not the 370
cells the sweep visits.

  (i) THE TEN. Five failing cells have a minimiser that GAINS a
      cyclotomic index the argmin does not have, and five more drop a
      block whose degree does not match the residual's. At those ten,
      F2's classification against the argmin fails, and whether hs = h
      is open: the family's parent ranges over EVERY admissible pure
      cofactor and not only the argmin, so a cell can be reached from a
      different parent. Nothing forces the answer
      either way.
 (ii) THE MEMBERS. hs = h could hold because the three members are the
      right objects, or because ANY three polynomials of degrees 2, 4
      and 2 and heights 3, 5 and 5 would do, the family being large.
      That is a confound named by argument, and naming one owes a
      COUNT. The count is the SHAM family: the same construction with
      the members replaced by A~ = 5 + 4x + 4x^2 + 2x^3 + 2x^4, B~ = 3
      + 2x + 2x^2, C~ = 5 + 3x + 3x^2 -- the same degrees, the same
      heights, the same values at x = 1 (17, 7, 11), and NOT reciprocal,
      which is the property the parent found the real residuals have.
      hst is its least height, and it obeys h <= hst <= ph by the same
      two arguments, the empty multiplier being in both families.
(iii) THE EXTENSION. Everything above lives inside the chart's M <= 40
      corner. explore_flatten_band.py scans each rank's own column far
      past it and records first failures at ranks 19 to 22 -- J_lo = 26,
      23, 25 and 30, at M = 45, 43, 46 and 52 -- outside the window
      entirely. Recomputing the classification at those four cells is
      an independent second reading of the swap, on cells no rig in
      this thread has factored. THOSE FOUR DEPTHS ARE TAKEN AS AN
      ANSWER KEY AND NOT RE-DERIVED: this rig checks that the cell
      fails and the one below it is clean, which is not the same as
      scanning the column for an earlier failure, and the difference is
      declared rather than closed.

FIFTH, THE COST, WHICH IS WHAT A CONSTRUCTION WOULD BUY. route_h
reduces a basis of dimension M and then walks a Fincke-Pohst ball in
that dimension: its cost grows with M at fixed rank and there is no
polynomial bound on the walk. hs enumerates parents -- multisets of
parts with sum of (d - 1) at most r - 1, so their number is a partition
count in r - 1 and does not depend on J at all -- and then convolves a
polynomial of degree at most r - 1 against (x-1)^J, which is O(r J).
SO THE TWO COSTS SCALE IN DIFFERENT VARIABLES, and at fixed rank the
ratio route_h/hs must grow with M. It does not follow that hs is
cheaper anywhere the chart reaches: at M <= 40 the lattice is small and
the parent count at rank 18 is already in the thousands. The crossover
is a measurement and it is taken along one column, at rank 22, which is
the largest rank any cell here visits -- a column varies M at FIXED
rank, which is the only way to isolate the variable route_h pays for,
the rank being the variable the swap family pays for. THE PART COUNT |E| <= J +
t DEPENDS ON J AND THE PARTITION COUNT DOES NOT, so the parent count is bounded
by the partition count and reaches it only for J large; the claim above is a
ceiling on the cost and not its value. WHICH MEANS BOTH SIDES OF THE RATIO MOVE
ALONG A COLUMN, the swap family's parent count RISING with J while route_h's
dimension rises with it, and a rising ratio would say nothing if only the ratio
were printed. The two walls and the parent count are printed separately and the
ratio is read against them.

SIXTH, WHAT THE ABORT CAN AND CANNOT DO. Every height here is computed
by a convolution that stops as soon as its running maximum reaches the
best height so far, which is what makes 370 cells affordable. An abort
can only ever cause a candidate that TIES or LOSES to be skipped, so
the minimum it returns is exact; a fault in the abort's bounds would
make hs too HIGH and would print as hs > h, never as hs < h. It is
checked directly all the same, at every cell of ranks 5 to 9, against
the same enumeration with the abort switched off (C4).

THE SCOPE. The parent chart's rectangle, M = 4..40 and J = 2..30,
restricted to ranks 5..18 -- 370 cells, the same set the parent rig
swept and where the answer key lives. Then the four extension cells at
ranks 19..22 and the clean cell one depth below each. Then the rank-22
cost column at J = 8, 16, 24, 30, which is M = 30 to 52 -- a span wide
enough for a trend, the smoke run's own column having spanned four
depths at one rank and shown none.

THE PREDICTIONS, fixed here before the engine ran.

P1. THE TEN ARE REACHED ANYWAY. At every one of the failing cells whose
    minimiser is NOT the same-degree block swap of a pure argmin at
    that cell, hs = h -- reached from a different admissible parent.
P2. THE MEMBERS ARE SPECIAL. At every one of the 83 failing cells the
    sham family falls short: hst > h.
P3. PRODUCTS ARE NEEDED, AND EXACTLY WHERE THE CENSUS SAYS. At the two
    cells whose minimiser residual is A*B, the single-member family
    falls short and the product family does not: hs1 > h and hs = h. At
    every other failing cell where hs = h, hs1 = h as well.
P4. THE EXTENSION AGREES. At each of ranks 19, 20, 21 and 22 the first
    failing cell's minimiser is the same-degree block swap of a pure
    argmin at that cell, its residual is in the parent's committed
    class, and hs = h; and the cell one depth below is clean with
    residual 1 and a minimiser equal to the pure argmin up to sign and
    monomial.
P5. THE COST CROSSES OVER. Along the rank-22 column the ratio of
    route_h's wall to the swap family's exceeds 1 at the top of the
    column and is larger there than at the bottom. TWO COMPARISONS ACROSS THE
    WIDEST SPAN AND NOT A MONOTONE CHAIN: the smoke run of this rig took the
    cost column at rank 8, where all four walls sat at the timer's resolution
    and a four-term monotone chain fired on noise alone. The chain was the
    prediction as first frozen and it is the weaker reading that is measured.

THE KILLS, frozen as OBSERVABLES the rig prints, never as inferences.

K1 A failing cell outside the forced 73 whose printed hs exceeds its
   printed h. P1 dies there, and the construction reading is a
   description of 73 cells and not of the band's near end.
K2 A failing cell whose printed hst equals its printed h. P2 dies: the
   family reaches h with polynomials that are not the census's, and the
   members carry no weight in the construction.
K3 A cell inside the forced 73 whose printed hs exceeds its printed h,
   or whose exhibited minimiser is not found in the family. Instrument
   kill: this rig's family or its classification differs from the
   parent's F2.
K4 An extension rank whose first failing cell has a residual outside
   the committed class {A, B, C, A*B}, or a minimiser that is not a
   same-degree block swap of a pure argmin, or hs > h; or whose cell
   one depth below is not clean with residual 1 and the pure argmin.
   P4 dies at that rank.
K5 An A*B cell with hs1 = h, or a failing cell outside that pair with
   hs = h and hs1 > h. P3 dies.
K6 The ratio of walls at rank 22 does not exceed 1 at the top of the
   column, or is not larger there than at the bottom. P5 dies.
K7 Instrument: hs0 differs from ph at any cell, or hs < h, or hs > ph,
   or hst < h, or hst > ph, or hs1 < hs.
K8 Answer-key: the swept rectangle does not reproduce the parent's 83
   failures, or its residual census is not 51, 29, 2, 1, or its trade
   counts are not 78 gaining nothing and 73 matching degree.
K9 Instrument: the aborting hs differs from the non-aborting hs at any
   cell of ranks 5..9; or a parent's directly built cyclotomic multiset
   differs from split_witness's, or its residual is not 1, at any
   parent of those cells.

THE POSITIVE CONTROLS, run before any survive/kill result is read.

C1 The family's own empty-multiplier sub-family against pure_min, at
   every cell: hs0 = ph. Two implementations of one minimum, one
   building q from [d]_x and one from Phi_d (K7).
C2 h <= hs <= ph, h <= hst <= ph and hs <= hs1 at every cell (K7), AND
   ONLY SOME OF THOSE SIX COMPARISONS CAN FIRE, which is stated here
   because a control that cannot fail is worth nothing and reads like a
   control that passed. The LOWER bounds are the real ones: hs and hst
   are minima over objects claimed to be lattice vectors at the cell,
   and a fault in the degree bookkeeping would put either below an
   independently computed h. The UPPER bounds are FORCED BY THE SEEDING
   -- both searches start at hs0 and accept only strict improvements, so
   neither can exceed it -- and their whole content therefore sits in
   C1, which is where hs0 is checked against ph by a second route.
   hs1 >= hs is forced by inclusion rather than by seeding, the
   single-member table being built from the product table, so it can
   fire only on a fault in that filter and is kept for exactly that.
C3 hs = h = ph at every clean cell. FORCED by C2 and h = ph, so it is
   an emptiness check on the enumeration and NOT evidence: a family
   that came back empty would print ph here too, and this is where that
   is caught.
C4 hs recomputed with the abort switched off at every cell of ranks
   5..9, identical (K9).
C5 Every parent at every cell of ranks 5..9: split_witness returns
   residual 1 and the multiset this rig builds from (t, E) (K9).
C6 The answer key: 83 failures, the residual census 51/29/2/1, and the
   trade counts 78 and 73, all recomputed here from the swept cells
   (K8).
C7 The members: degrees 2, 4, 2, heights 3, 5, 5, reciprocal, all roots
   on the unit circle by the exact Sturm test; and the shams beside
   them with the same degrees, heights and values at 1 and reciprocal
   NONE. Printed before anything is measured.

COST. Single process, exact integer arithmetic throughout, no array
library. The estimate before the run, from a cost probe on five cells:
the whole-rectangle sweep at 370 cells is route_h and pure_min at the
parent rig's own price plus about 0.3 s per cell at the top rank for
three multiplier tables over one block enumeration, the extension is
eight cells at up to 7 s of route_h each, and the cost column is four
more; 2 to 4 minutes in total, inside the ordinary analysis footprint,
run under memwatch because the block enumeration's footprint has no
precedent. The wall is 87 s for the design as frozen and 100 s with the
added arm, peak working set 59.1 and 61.6 MB against the 512 MB
ceiling, comfortably inside the estimate.

THE FINDINGS.

F1. INSIDE THE CHART THE SWAP IS A CONSTRUCTION, AND WHAT IT BUILDS IS
THE EXHIBITED MINIMISER ITSELF. hs = h at 83 of the 83 failing cells of
the rank-5..18 rectangle, and at 83 of 83 the very vector route_h
returned is a member of the family UP TO SIGN -- which is the stronger
of the two statements, hs = h being reachable in principle by some other
vector of the same height. The qualifier is counted and not assumed, and
it is smaller than this thread's comparisons usually carry: 54 of the 83
minimiser cofactors have a negative leading coefficient and NONE of the
83 carries a monomial factor, where the standard comparison here strips
both. Seventy-three of those cells are FORCED by the parent
rig's F2 and were declared before the run to carry no weight; the
content is the OTHER TEN, and all ten are reached. Five of them have a
minimiser that GAINS a cyclotomic index the pure argmin lacks and five
drop a block whose degree does not match the residual's, so at all ten
the classification against the argmin fails. What reaches them is the
family's parent ranging over EVERY admissible pure cofactor rather than
the argmin alone: the minimiser is the same-degree block swap of a
DIFFERENT pure product. So F2's description is the special case of the
construction in which the parent happens to be the argmin, and P1
holds at every cell that could test it.

F2. THE MULTIPLIERS ARE NOT A DEGREE ACCIDENT, AND THE NULL IS EMPTIER
THAN THE PREDICTION ASKED FOR. The sham family reaches h at 0 of the 83
failing cells, its shortfall running from 1 to 824760. The sharper
count, added after the run: the sham family's minimum EQUALS ph at 83
of the 83 and beats it at NONE. Three polynomials carrying the members'
degrees, heights and values at x = 1 never improve on the pure family
anywhere in the band -- they do not fall a little short of h, they never
fire at all. So the multiplier is not any small polynomial of the right
degree, and P2 holds with room.

WHAT THE NULL DOES NOT ISOLATE, because a control is worth exactly the
variable it varies. The shams differ from the members in their whole
COEFFICIENT SEQUENCE, of which failing to be reciprocal is one visible
consequence, so this is a different-polynomial control and not a
reciprocity control: it kills "any polynomial of this shape would do"
and says nothing about WHICH property of A, B and C is doing the work.
Reciprocity could have been isolated and is not -- 3 + x + 3x^2 carries
B's degree, height and value at 1 and IS reciprocal, so a reciprocal
sham exists and was simply not run. And the members were not drawn at
random either: they are the residuals the parent's census read off these
very cells, so the null tests the SHAPE of the multiplier and never the
provenance of these three.

F3. PRODUCTS ARE NEEDED, AND EXACTLY AT THE TWO CELLS THE CENSUS NAMES.
The two cells carrying the residual A*B -- rank 15 at depths 24 and 25
-- are the only two at which the single-member family falls short and
the product family reaches: hs1 = 6763 against h = 6296, and 12702
against 12075. No cell outside that pair needs a product. P3 holds
exactly.

F4. PAST THE CHART'S CORNER THE DESCRIPTION AND THE CONSTRUCTION COME
APART, AND IT IS THE DESCRIPTION THAT BREAKS FIRST. At the first
failing cells of ranks 19, 20 and 21 -- depths 26, 23 and 25, at M =
45, 43 and 46, cells no rig in this thread had factored -- hs = h and
the exhibited minimiser is in the family at all three. At ranks 19 and
20 the classification AGAINST THE ARGMIN fails, the minimiser gaining
Phi_5, while the construction holds from another parent; only rank 21
conforms. At all three the FAMILY reaches the cell the same way, and it
is not what the argmin-relative trade column reports on those rows: the
witness is one parent's own multiset with a block of four copies of
Phi_2 traded for A. So the swap survives the first extension
of its scope and the argmin-relative reading does not.

F5. THE MEMBER CLASS IS CHART-LOCAL, THE OBSTRUCTION IS THE MULTIPLIER
AND NOT THE PARENT, AND THE FOURTH MEMBER IS NAMED. At rank 22, depth
30, M = 52 -- the largest cell any rig in this thread had
factored when this ran --
hs = 44108 against h = 42222, and the family misses the minimiser. K4
fires and P4 dies there. The obstruction is measured rather than
inferred and it is not the parent: an admissible pure cofactor holds
the minimiser's cyclotomic multiset {2^5, 3^3} with exactly the
residual's ten degrees to spare, and the block it trades away is ten
copies of Phi_2, of degree 10 exactly like the residual -- a same-degree
swap like every other. That block is the FAMILY's and not the
argmin-relative trade column's, which decomposes the same cell
differently from a different parent. What is missing is the
MULTIPLIER. The residual is degree 10 and factors as A * D with

    D = 3 + 9x + 15x^2 + 17x^3 + 15x^4 + 9x^5 + 3x^6,

of degree 6 and height 17, D(1) = 71, reciprocal, all its roots on the
unit circle by the exact Sturm test, carrying no cyclotomic factor, and
divisible by none of A, B and C. Admitting D as a fourth member drops
hs to 42222 = h and puts the exhibited minimiser back in the family as
that parent, that block, and the multiplier A*D. So the SWAP is the
mechanism and it extends past the corner; the THREE-MEMBER CLASS is a
fact about the chart's rectangle and not about the lattice, and the
class is closed under multiplication but not finite. A, B and C are its
MEMBERS and D is a FOURTH; counting instead the RESIDUALS the chart
exhibits -- 1, B, A, A*B and C -- A*D is a sixth, and the two counts
answer different questions about one object. THE TIER IS ONE SPECIMEN AT
ONE CELL: D is an observation, and whether the class grows
again above rank 22 is untested here. (SETTLED SINCE, and the
answer changes what a first cell is worth: walking the FIRST failing
cell of ranks 19..26 finds no member past D -- six of those cells carry
the residual A and one A*B -- while three cells further up each of the
same columns turn up a FIFTH, the same polynomial at rank 22 depth 32
and rank 26 depth 36, reciprocal of degree 8 and height 43 and carrying
four of its eight roots OFF the unit circle, which no residual the chart
exhibits does. So the class grows with the CELL and not the rank, and it
is not confined to the circle class this rig's members all sit in. AND
"NOT FINITE" ABOVE IS THE FREE HALF OF THE STATEMENT: closure under
multiplication gives it for nothing, and the question worth the name is
whether the MEMBERS are finitely many, which stands open at five;
explore_flatten_class.py.)

F6. THE ROUTE IS CHEAPER THAN THE LATTICE EXACTLY WHERE THE LATTICE IS
DEAR, AND BOTH SIDES OF THE RATIO WERE READ. Along the rank-22 column
at M = 30, 38, 46 and 52 the ratio of route_h's wall to the family's
runs 0.02, 0.05, 0.17, 3.60, so P5 holds. The rise is route_h's alone
and the printed counts say so: its wall goes 0.03 to 7.05 s across the
column while the family's goes 1.71 to 1.96 and its parent count goes
12885 to 14486 -- essentially flat once J is past the part count's
bite, which is the confound the column was widened to expose. The two
costs scale in different variables as the hand attack derived, and the
crossover at fixed rank 22 sits between M = 46 and M = 52. Over the
chart's own rectangle the family is the DEARER of the two, 25.5 s
against route_h's 10.5 over 370 cells, because the rectangle's cost is
in its RANKS, which is what the family pays for, and its M is small.

F7. WHAT THIS IS NOT. hs = h is a MEASUREMENT at every cell where it is
reported and a derivation nowhere, so the family is a candidate route
to h and not an algorithm for it -- and rank 22 settles that the route
as constituted from three members is not correct in general, since one
cell of the five outside the chart refutes it. A route that grows its
class as it goes is not a closed form and must not be called one. What
the construction does buy, at the tier it earns, is a way to PROPOSE h
with no lattice reduction in it, correct on the 83 cells of the
rectangle and on three of the four cells outside it, and cheap where
the reduction is not.

THE RUN RECORD. THREE FULL RUNS, each ADDING to the one before and
none changing it. RUN 1 is the science for arms 1 to 4 and RUN 2 ADDS an
arm rather than changing one -- arm 5, which asks
what the unreached cell is obstructed BY, and the count of the sham's
minimum against ph. Every number of arms 1 to 4 reproduces exactly
between them and no cell's h, ph or flag moved; the ONLY quantities
that differ are the wall-clocks, which is why F6 quotes RUN 2
throughout rather than run 1 -- a finding whose whole subject is a
ratio of walls may not carry one run's numerator beside another's
denominator, and it did until the audit read the two runs side by
side. RUN 3 adds the two counts F1's qualifier rests on -- the monomial
and the sign -- which the audit found asserted from an argument where
the rig had never printed them; every COUNT reproduces and the walls
move as walls do, which is why F6 stays with run 2's throughout.

TWO SMOKE RUNS before run 1, both before any science printed. SMOKE 1
at ranks 5..7 with M <= 30 found two faults and both were in the cost
arm. The column was timing cell_swap, which builds the sham and
single-member families as well as the real one -- three families where
a route to h computes one -- so the column now times the block table,
the empty-multiplier minimum and the real multipliers alone. And P5 was
frozen as a four-term monotone chain in the ratio, which fired K6 at a
rank where all four walls sat at the timer's resolution; the prediction
and its kill are now the two comparisons across the widest span of the
column, which is the weaker reading and the one measured. The timer
went to perf_counter in the same edit. SMOKE 2 at ranks 9..12 exercised
the content path -- one non-conforming cell, reached -- and showed that
four depths of one rank span too little M to carry a trend at all: the
cost column widened from J = 24, 26, 28, 30 to J = 8, 16, 24, 30, and
the parent count and block-table size joined it so that a rising ratio
cannot be read without seeing which side moved. That last is what makes
F6's confound answerable.

ONE FAULT WAS FOUND BY READING RATHER THAN BY RUNNING, and it is worth
the line because no control would have caught it: the containment test
in_family returned TRUE for any minimiser whose residual is 1, on the
ground that a pure product needs no multiplier. It does need an
admissible PARENT, and the part count |E| <= J + t is exactly what can
leave a pure product outside the family while the degree budget admits
it -- which is the mechanism the parent rig's own F6 is about. The test
searches for the parent in that case like any other.
"""
import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_flatten_family import (route_h, polydiv, split_witness,
                                    on_unit_circle, phi_poly, divisors)
from explore_flatten_band import mulp, xm1_pow, height
from explore_flatten_near import (adm_cofactors, pure_min, same_shape,
                                  column, RANKS, KEY_FAILURES,
                                  KEY_RESIDUAL_COUNTS)

# The members, and the parent's fourth census entry which is their
# product. Low degree first throughout.
MEM = (("A", [2, 4, 5, 4, 2]), ("B", [2, 3, 2]), ("C", [3, 5, 3]))
# The sham: same degrees, same heights, same values at x = 1, not
# reciprocal. The count the confound owes.
SHAM = (("A~", [5, 4, 4, 2, 2]), ("B~", [3, 2, 2]), ("C~", [5, 3, 3]))

# The band rig's committed first failing depths outside the chart.
EXT = ((19, 26), (20, 23), (21, 25), (22, 30))
COST_RANK = 22
COST_DEPTHS = (8, 16, 24, 30)
# The parent rig's committed trade counts: gaining no cyclotomic index,
# and of those, matching the residual's degree.
KEY_TRADE = (78, 73)
NOABORT_RANKS = range(5, 10)


# ------------------------------------------------- the multiplier sets

def mult_table(members, cap):
    """Every product of members of degree at most cap and at least 1,
    keyed by degree. The empty product is NOT here -- it is the g = 0
    pass, run first and separately so that it can be checked against
    pure_min."""
    out, seen = {}, set()

    def rec(i, name, poly):
        if len(poly) - 1 > cap:
            return
        if i == len(members):
            if name and tuple(poly) not in seen:
                seen.add(tuple(poly))
                out.setdefault(len(poly) - 1, []).append((name, poly))
            return
        nm, mp = members[i]
        p, k = list(poly), 0
        while len(p) - 1 <= cap:
            rec(i + 1, name + (("%s^%d" % (nm, k)) if k > 1
                               else (nm if k else "")), p)
            p = mulp(p, mp)
            k += 1

    rec(0, "", [1])
    return out


def single_table(cap):
    """The multipliers that are a member ITSELF and not a product of
    two, which is what separates the two families of P3."""
    out = {}
    for g, v in mult_table(MEM, cap).items():
        keep = [z for z in v if len(z[0]) == 1]
        if keep:
            out[g] = keep
    return out


# ---------------------------------------------------- the swap family

PROD = {}


def cyc_prod(S):
    """prod_{d in S} Phi_d, memoised on the sorted multiset."""
    if S not in PROD:
        PROD[S] = [1] if not S else mulp(cyc_prod(S[:-1]), phi_poly(S[-1]))
    return PROD[S]


def cyc_multiset(t, E):
    """The cyclotomic multiset of (x-1)^t prod_{d in E} [d]_x, read off
    (t, E) with no factorisation: Phi_1 = x - 1 and [d]_x is the product
    of Phi_e over the divisors e > 1 of d."""
    S = [1] * t
    for d in E:
        S.extend(e for e in divisors(d) if e > 1)
    return tuple(sorted(S))


def blocks(r, J, degs):
    """{g: set of S'} over every admissible pure cofactor at the cell and
    every sub-multiset removed whose degree g is in degs, plus g = 0.
    The parent is dropped once its multiset is taken: the family depends
    on the parent only through S."""
    maxg = max(degs)
    out = dict((g, set()) for g in degs)
    out[0] = set()
    for (t, E, _) in adm_cofactors(r, J):
        S = cyc_multiset(t, E)
        idx = sorted(set(S))
        mult = [S.count(d) for d in idx]
        deg = [len(phi_poly(d)) - 1 for d in idx]
        n = len(idx)

        def rec(i, g, rem):
            if g in out:
                out[g].add(rem)
            if i == n or g >= maxg:
                return
            rl = list(rem)
            for j in range(mult[i]):
                if g + (j + 1) * deg[i] > maxg:
                    break
                rl.remove(idx[i])
                rec(i + 1, g + (j + 1) * deg[i], tuple(rl))
            rec(i + 1, g, rem)

        rec(0, 0, S)
    return out


def conv_h(q, xm1, best):
    """height(q * xm1), abandoned as soon as the running maximum reaches
    best. Returns None when abandoned, so only a STRICT improvement is
    ever reported and the minimum returned is exact."""
    n, m = len(q), len(xm1)
    hi = 0
    for i in range(n + m - 1):
        s = 0
        for j in range(max(0, i - m + 1), min(i, n - 1) + 1):
            s += q[j] * xm1[i - j]
        a = -s if s < 0 else s
        if a > hi:
            hi = a
            if best is not None and hi >= best:
                return None
    return hi


def pure_family_min(bl, xm1, abort=True):
    """The empty-multiplier minimum: the admissible pure family's own
    least height reached through THIS rig's machinery rather than the
    parent's, which is what makes C1 a comparison and not a copy."""
    best = None
    for Sp in bl[0]:
        v = conv_h(cyc_prod(Sp), xm1, best if abort else None)
        if v is not None and (best is None or v < best):
            best = v
    return best


def swap_min(bl, MT, xm1, seed, abort=True):
    """(least height over the family, a witness (S', name, g)). seed is
    the empty-multiplier minimum, already computed and passed in so that
    the g = 0 pass is not repeated; the witness is None when nothing
    beats it."""
    best, wit = seed, None
    for g in sorted(k for k in bl if k):
        if g not in MT:
            continue
        for Sp in bl[g]:
            base = cyc_prod(Sp)
            for (nm, m) in MT[g]:
                v = conv_h(mulp(base, m), xm1, best if abort else None)
                if v is not None and (best is None or v < best):
                    best, wit = v, (Sp, nm, g)
    return best, wit


# --------------------------------------------- the parent's F2 classes

def trade_row(q, bs):
    """The parent rig's classification of one failing cell: for each
    member of the pure argmin SET, what the minimiser's cyclotomic
    multiset drops, what it gains, and whether the dropped block's
    degree matches the residual's. The row taken is the one most
    favourable to the swap -- gaining nothing first, then matching the
    degree -- which is the parent's own rule and is declared here for
    the same reason."""
    _, Sf, Rf = split_witness(list(q))
    deg = len(Rf) - 1
    got = []
    for cand in bs:
        _, Sp, _ = split_witness(list(cand))
        out, back = list(Sp), list(Sf)
        for d in list(out):
            if d in back:
                out.remove(d)
                back.remove(d)
        dout = sum(len(phi_poly(d)) - 1 for d in out)
        got.append((tuple(sorted(out)), tuple(sorted(back)), Rf,
                    dout == deg))
    got.sort(key=lambda k: (len(k[1]), not k[3]))
    return got[0]


def conforms(row):
    """The cell is one of the FORCED ones: the minimiser gains no
    cyclotomic index and the dropped block matches the residual's
    degree."""
    return not row[1] and row[3]


def in_family(q, r, J, MT):
    """Is the EXHIBITED minimiser itself a member of the swap family?
    Its cofactor is prod(S_min) * R_min, so the question is whether
    R_min is a multiplier and whether S_min extends to some admissible
    parent's multiset with exactly deg R_min to spare. Returns
    (verdict, reason)."""
    _, Smin, R = split_witness(list(q))
    g = len(R) - 1
    if g:
        names = [nm for (nm, m) in MT.get(g, []) if tuple(m) == tuple(R)]
        if not names:
            return False, "residual %s is not a multiplier" % (list(R),)
    else:
        # A residual of 1 is not a free pass. The minimiser is then a
        # pure product, and the question is whether it is an ADMISSIBLE
        # one -- the part count is exactly what can leave a pure product
        # outside the family while the degree budget admits it.
        names = ["1"]
    want = sorted(Smin)
    for (t, E, _) in adm_cofactors(r, J):
        S = cyc_multiset(t, E)
        rem = list(S)
        ok = True
        for d in want:
            if d in rem:
                rem.remove(d)
            else:
                ok = False
                break
        if ok and sum(len(phi_poly(d)) - 1 for d in rem) == g:
            return True, "parent %s block %s times %s" % (
                list(S), sorted(rem), names[0])
    return False, ("no admissible parent contains %s with %d to spare"
                   % (want, g))


# ------------------------------------------------------------- the run

def cell_swap(r, J, xm1, MT, MT1, MTS):
    """(hs0, hs, hs1, hst, the witness of hs, the block table)."""
    degs = sorted(set(list(MT) + list(MT1) + list(MTS)))
    bl = blocks(r, J, degs)
    hs0 = pure_family_min(bl, xm1)
    hs, wit = swap_min(bl, MT, xm1, hs0)
    hs1, _ = swap_min(bl, MT1, xm1, hs0)
    hst, _ = swap_min(bl, MTS, xm1, hs0)
    return hs0, hs, hs1, hst, wit, bl


def main():
    t_all = time.time()
    fired = dict(("K%d" % i, 0) for i in range(1, 10))

    print("=" * 70)
    print("explore_flatten_swap.py -- is the swap a construction?")
    print("=" * 70)

    # -------------------------------------------------------------- C7
    print("\n[C7] the members and the shams, before anything is "
          "measured: degree, height, value at x = 1, reciprocal, all "
          "roots on the unit circle")
    for tag, fam in (("member", MEM), ("sham  ", SHAM)):
        for (nm, p) in fam:
            print("   %s %-3s %-22s deg %d  height %d  P(1) %3d  "
                  "reciprocal %-5s  on the circle %s"
                  % (tag, nm, str(p), len(p) - 1, height(p), sum(p),
                     list(reversed(p)) == p, on_unit_circle(p)[0]))
    print("   and the parent's fourth census entry A*B = %s, a product "
          "of members and not a member" % (mulp(MEM[0][1], MEM[1][1]),))

    # ------------------------------------------------------- the sweep
    print("\nARM 1 -- THE RECTANGLE: h, ph and the swap family's hs at "
          "every cell of ranks %d..%d" % (RANKS[0], RANKS[-1]))
    t = time.time()
    cells = {}
    nfail = 0
    t_route = t_swap = 0.0
    for r in RANKS:
        PROD.clear()
        cap = r - 1
        MT = mult_table(MEM, cap)
        MT1 = single_table(cap)
        MTS = mult_table(SHAM, cap)
        for J in column(r):
            M = J + r
            xm1 = xm1_pow(J)
            t0 = time.time()
            h, v, _, _ = route_h(M, J)
            t1 = time.time()
            ph, bs, _, _ = pure_min(r, J, xm1)
            q = polydiv(v, xm1)
            t2 = time.time()
            hs0, hs, hs1, hst, wit, _ = cell_swap(r, J, xm1, MT, MT1, MTS)
            t3 = time.time()
            t_route += t1 - t0
            t_swap += t3 - t2
            fail = h < ph
            nfail += fail
            cells[(r, J)] = dict(M=M, h=h, ph=ph, fail=fail, bs=bs, q=q,
                                 hs0=hs0, hs=hs, hs1=hs1, hst=hst,
                                 wit=wit)
    print("   %d cells swept, %d failures; route_h %.1f s, the swap "
          "family %.1f s (%.1f s in all)"
          % (len(cells), nfail, t_route, t_swap, time.time() - t))

    # ------------------------------------------------------- C1 and C2
    print("\n[C1] the family's empty-multiplier sub-family against "
          "pure_min, and [C2] the two-sided bracket h <= hs <= ph")
    b1 = b2 = 0
    for (r, J), c in sorted(cells.items()):
        if c["hs0"] != c["ph"]:
            b1 += 1
            fired["K7"] += 1
            if b1 <= 5:
                print("   K7 hs0 != ph at r=%d J=%d: %s vs %s"
                      % (r, J, c["hs0"], c["ph"]))
        bad = (c["hs"] < c["h"] or c["hs"] > c["ph"]
               or c["hst"] < c["h"] or c["hst"] > c["ph"]
               or c["hs1"] < c["hs"])
        if bad:
            b2 += 1
            fired["K7"] += 1
            if b2 <= 5:
                print("   K7 bracket at r=%d J=%d: h=%d hs=%d hs1=%d "
                      "hst=%d ph=%d" % (r, J, c["h"], c["hs"], c["hs1"],
                                        c["hst"], c["ph"]))
    print("   %d cells disagree with pure_min, %d violate the bracket"
          % (b1, b2))

    # -------------------------------------------------------------- C3
    nclean = sum(1 for c in cells.values() if not c["fail"])
    okc = sum(1 for c in cells.values()
              if not c["fail"] and c["hs"] == c["h"] == c["ph"])
    print("\n[C3] hs = h = ph at %d of the %d clean cells. FORCED by "
          "C2, so it is an emptiness check on the enumeration and is "
          "evidence for nothing" % (okc, nclean))

    # -------------------------------------------------------------- C6
    print("\n[C6] the answer key, recomputed here from the swept "
          "cells: the failure count, the residual census and the "
          "parent's two trade counts")
    res = {}
    for (r, J), c in sorted(cells.items()):
        if c["fail"]:
            _, _, R = split_witness(list(c["q"]))
            res.setdefault(R, []).append((r, J))
    got = tuple(sorted((len(v) for v in res.values()), reverse=True))
    rows = {}
    gain0 = same = 0
    for (r, J), c in sorted(cells.items()):
        if not c["fail"]:
            continue
        row = trade_row(c["q"], c["bs"])
        rows[(r, J)] = row
        if not row[1]:
            gain0 += 1
            if row[3]:
                same += 1
    print("   failures %d (key %d); residual census %s (key %s); "
          "gaining no index %d and matching degree %d (key %s)"
          % (nfail, KEY_FAILURES, got, KEY_RESIDUAL_COUNTS, gain0,
             same, KEY_TRADE))
    if (nfail != KEY_FAILURES or got != KEY_RESIDUAL_COUNTS
            or (gain0, same) != KEY_TRADE):
        fired["K8"] += 1
        print("   K8 the answer key is not reproduced")

    # ------------------------------------------------------- C4 and C5
    print("\n[C4] hs with the abort switched off, and [C5] every "
          "parent's cyclotomic multiset against split_witness, at "
          "every cell of ranks %d..%d"
          % (NOABORT_RANKS[0], NOABORT_RANKS[-1]))
    t = time.time()
    b4 = b5 = n5 = 0
    for r in NOABORT_RANKS:
        PROD.clear()
        cap = r - 1
        MT = mult_table(MEM, cap)
        for J in column(r):
            xm1 = xm1_pow(J)
            bl = blocks(r, J, sorted(MT))
            s0 = pure_family_min(bl, xm1, abort=False)
            hs, _ = swap_min(bl, MT, xm1, s0, abort=False)
            if hs != cells[(r, J)]["hs"]:
                b4 += 1
                fired["K9"] += 1
                if b4 <= 5:
                    print("   K9 abort r=%d J=%d: %s vs %s"
                          % (r, J, hs, cells[(r, J)]["hs"]))
            for (t_, E, q) in adm_cofactors(r, J):
                n5 += 1
                sh, S, R = split_witness(q)
                if S != cyc_multiset(t_, E) or R != (1,) or sh:
                    b5 += 1
                    fired["K9"] += 1
                    if b5 <= 5:
                        print("   K9 parent r=%d J=%d t=%d E=%s: %s vs "
                              "%s residual %s" % (r, J, t_, E, S,
                                                  cyc_multiset(t_, E), R))
    print("   %d cells re-run without the abort, %d disagree; %d "
          "parents factored, %d disagree (%.1f s)"
          % (sum(len(column(r)) for r in NOABORT_RANKS), b4, n5, b5,
             time.time() - t))

    # ------------------------------------------------ P1: the content
    print("\n   THE FAILING CELLS, split by the parent's F2 "
          "classification. The FORCED rows restate F2 and are checked "
          "as an instrument; the rest is the question.")
    print("   %4s %3s %4s %8s %8s %8s %8s %8s  %-10s %s"
          % ("r", "J", "cls", "h", "hs", "hs1", "hst", "ph",
             "residual", "why it is not forced"))
    ncf = nnc = 0
    okP1 = badP1 = 0
    for (r, J), c in sorted(cells.items()):
        if not c["fail"]:
            continue
        row = rows[(r, J)]
        cf = conforms(row)
        _, _, R = split_witness(list(c["q"]))
        if cf:
            ncf += 1
            if c["hs"] != c["h"]:
                fired["K3"] += 1
                print("   K3 forced cell r=%d J=%d has hs=%d > h=%d"
                      % (r, J, c["hs"], c["h"]))
            continue
        nnc += 1
        why = ("gains %s" % (list(row[1]),) if row[1]
               else "drops %s of degree %d against a residual of "
                    "degree %d" % (list(row[0]),
                                   sum(len(phi_poly(d)) - 1
                                       for d in row[0]), len(R) - 1))
        if c["hs"] == c["h"]:
            okP1 += 1
        else:
            badP1 += 1
            fired["K1"] += 1
        print("   %4d %3d %4s %8d %8d %8d %8d %8d  %-10s %s"
              % (r, J, "NOT", c["h"], c["hs"], c["hs1"], c["hst"],
                 c["ph"], str(list(R)), why))
    print("   [P1] %d of the %d failing cells are FORCED by F2 and "
          "carry no weight; of the %d that are not, hs = h at %d and "
          "hs > h at %d" % (ncf, nfail, nnc, okP1, badP1))

    # --------------------------------------- P3: is the minimiser in?
    print("\n   THE EXHIBITED MINIMISER ITSELF, at every failing cell: "
          "is the very vector route_h returned a member of the family")
    inn = out = shifted = negative = 0
    for r in RANKS:
        MT = mult_table(MEM, r - 1)
        for J in column(r):
            c = cells[(r, J)]
            if not c["fail"]:
                continue
            # THE MEMBERSHIP IS UP TO SIGN AND UP TO THE MONOMIAL, because
            # split_witness strips both before the family is asked. Both
            # are counted rather than assumed: the lattice is closed under
            # multiplication by x inside the budget, so the monomial costs
            # nothing, but a qualifier owed is a qualifier printed.
            sh, _, _ = split_witness(list(c["q"]))
            shifted += 1 if sh else 0
            t = list(c["q"])
            while len(t) > 1 and t[-1] == 0:
                t.pop()
            negative += 1 if t[-1] < 0 else 0
            ok, why = in_family(c["q"], r, J, MT)
            if ok:
                inn += 1
            else:
                out += 1
                if conforms(rows[(r, J)]):
                    fired["K3"] += 1
                    print("   K3 forced cell r=%d J=%d not in the "
                          "family: %s" % (r, J, why))
                elif out <= 12:
                    print("   r=%2d J=%2d NOT in the family: %s"
                          % (r, J, why))
    print("   %d of %d failing cells have their exhibited minimiser in "
          "the family, %d do not" % (inn, nfail, out))
    print("      and the qualifier that membership is up to, counted "
          "rather than assumed: %d of the %d minimiser cofactors carry "
          "a MONOMIAL factor and %d have a NEGATIVE leading coefficient"
          % (shifted, nfail, negative))

    # ------------------------------------------------------ P2, the null
    print("\nARM 2 -- THE NULL: the same construction with the sham "
          "members, over the failing cells")
    hit = miss = 0
    eq = []
    for (r, J), c in sorted(cells.items()):
        if not c["fail"]:
            continue
        if c["hst"] == c["h"]:
            hit += 1
            fired["K2"] += 1
            eq.append((r, J, c["h"], c["ph"]))
        else:
            miss += 1
    print("   the sham family reaches h at %d of the %d failing cells "
          "and falls short at %d" % (hit, nfail, miss))
    for (r, J, h, ph) in eq[:12]:
        print("      r=%2d J=%2d h=%d ph=%d" % (r, J, h, ph))
    gapr = [c["hst"] - c["h"] for c in cells.values() if c["fail"]]
    gaps = [c["hs"] - c["h"] for c in cells.values() if c["fail"]]
    print("   the sham's shortfall hst - h runs %d to %d; the real "
          "family's hs - h runs %d to %d"
          % (min(gapr), max(gapr), min(gaps), max(gaps)))

    # ------------------------------------------------ P3: the products
    print("\n   THE SINGLE-MEMBER FAMILY against the product family, "
          "over the failing cells")
    AB = tuple(mulp(MEM[0][1], MEM[1][1]))
    nab = nabok = nother = 0
    for (r, J), c in sorted(cells.items()):
        if not c["fail"]:
            continue
        _, _, R = split_witness(list(c["q"]))
        isab = tuple(R) == AB
        if isab:
            nab += 1
            if c["hs1"] > c["h"] and c["hs"] == c["h"]:
                nabok += 1
            else:
                fired["K5"] += 1
                print("   K5 the A*B cell r=%d J=%d has hs1=%d hs=%d "
                      "h=%d" % (r, J, c["hs1"], c["hs"], c["h"]))
        else:
            if c["hs"] == c["h"] and c["hs1"] > c["h"]:
                nother += 1
                fired["K5"] += 1
                print("   K5 r=%d J=%d needs a product and its residual "
                      "is %s" % (r, J, list(R)))
    print("   %d cells carry the residual A*B and %d of them need a "
          "product; %d cells outside that pair need one"
          % (nab, nabok, nother))

    # ------------------------------------------------- ARM 3: the extension
    print("\nARM 3 -- THE EXTENSION, past the chart's corner: the band "
          "rig's first failing depth at ranks 19..22 and the depth "
          "below it. The depths are an ANSWER KEY and the column is "
          "not rescanned for an earlier failure.")
    print("   %4s %3s %4s %6s %9s %9s %9s %5s  %-12s %s"
          % ("r", "J", "M", "fail", "h", "hs", "ph", "swap",
             "residual", "the trade"))
    for (r, Jlo) in EXT:
        PROD.clear()
        cap = r - 1
        MT = mult_table(MEM, cap)
        MT1 = single_table(cap)
        MTS = mult_table(SHAM, cap)
        for J in (Jlo - 1, Jlo):
            M = J + r
            xm1 = xm1_pow(J)
            h, v, _, _ = route_h(M, J)
            ph, bs, _, _ = pure_min(r, J, xm1)
            q = polydiv(v, xm1)
            hs0, hs, hs1, hst, wit, _ = cell_swap(r, J, xm1, MT, MT1, MTS)
            fail = h < ph
            _, _, R = split_witness(list(q))
            inf, iwhy = in_family(q, r, J, MT)
            row = trade_row(q, bs) if fail else None
            cf = conforms(row) if fail else None
            note = ("drops %s gains %s, degrees match %s"
                    % (list(row[0]), list(row[1]), row[3])) if fail \
                else ("minimiser is the pure argmin: %s"
                      % any(same_shape(q, list(b)) for b in bs))
            print("   %4d %3d %4d %6s %9d %9d %9d %5s  %-12s %s"
                  % (r, J, M, "F" if fail else ".", h, hs, ph,
                     cf if fail else "-", str(list(R)), note))
            print("        the exhibited minimiser in the family: %s -- %s"
                  % (inf, iwhy))
            if hs0 != ph or hs < h or hs > ph:
                fired["K7"] += 1
                print("      K7 bracket at the extension cell r=%d J=%d"
                      % (r, J))
            if J == Jlo:
                if not fail or not cf or hs != h or tuple(R) not in (
                        tuple(MEM[0][1]), tuple(MEM[1][1]),
                        tuple(MEM[2][1]), AB):
                    fired["K4"] += 1
                    print("      K4 rank %d: fail %s conforms %s hs %d "
                          "h %d residual %s"
                          % (r, fail, cf, hs, h, list(R)))
                if hst == h:
                    fired["K2"] += 1
                    print("      K2 the sham reaches h at r=%d J=%d"
                          % (r, J))
            else:
                if fail or R != (1,) or not any(
                        same_shape(q, list(b)) for b in bs):
                    fired["K4"] += 1
                    print("      K4 rank %d: the cell below J_lo is "
                          "fail %s residual %s" % (r, fail, list(R)))

    # ------------------------------------------------- ARM 4: the cost
    print("\nARM 4 -- THE COST along the rank-%d column: route_h "
          "against the swap family at four depths" % COST_RANK)
    PROD.clear()
    r = COST_RANK
    MT = mult_table(MEM, r - 1)
    print("   THE SWAP COLUMN IS TIMED AT WHAT A ROUTE TO h WOULD "
          "ACTUALLY COMPUTE -- the block table, the empty-multiplier "
          "minimum and the real multipliers -- and not at the sham and "
          "single-member families, which are this rig's controls and "
          "no part of the construction.")
    print("   %4s %4s %10s %10s %8s %8s %8s %10s %10s"
          % ("J", "M", "route_h s", "swap s", "ratio", "parents",
             "blocks", "h", "hs"))
    ratios = []
    for J in COST_DEPTHS:
        M = J + r
        xm1 = xm1_pow(J)
        t0 = time.perf_counter()
        h, v, _, _ = route_h(M, J)
        t1 = time.perf_counter()
        bl = blocks(r, J, sorted(MT))
        hs, _ = swap_min(bl, MT, xm1, pure_family_min(bl, xm1))
        t2 = time.perf_counter()
        ratios.append((t1 - t0) / (t2 - t1))
        print("   %4d %4d %10.2f %10.2f %8.2f %8d %8d %10d %10d"
              % (J, M, t1 - t0, t2 - t1, ratios[-1],
                 len(adm_cofactors(r, J)), sum(len(v) for v in bl.values()),
                 h, hs))
    if ratios[-1] <= 1.0 or ratios[-1] <= ratios[0]:
        fired["K6"] += 1
        print("   K6 the ratios are %s -- the last is not above 1, or "
              "not above the first" % ["%.2f" % x for x in ratios])

    # ---------------------------------------- ARM 5: the obstruction
    print("\nARM 5 -- WHAT THE UNREACHED EXTENSION CELL IS OBSTRUCTED "
          "BY. Every number here is over cells ARM 3 had already "
          "decided; no cell's h, ph or flag moves.")
    for (r, Jlo) in EXT:
        M = Jlo + r
        xm1 = xm1_pow(Jlo)
        h, v, _, _ = route_h(M, Jlo)
        q = polydiv(v, xm1)
        _, Smin, R = split_witness(list(q))
        MT = mult_table(MEM, r - 1)
        g = len(R) - 1
        known = [nm for gg in MT for (nm, m) in MT[gg]
                 if tuple(m) == tuple(R)]
        if known:
            print("   r=%d J=%d: the residual is the multiplier %s, "
                  "already in the class" % (r, Jlo, known[0]))
            continue
        print("   r=%d J=%d: the residual %s is NOT a product of %s"
              % (r, Jlo, list(R),
                 ", ".join(nm for nm, _ in MEM)))
        # Is the obstruction the PARENT or the MULTIPLIER? They are two
        # different failures and hs alone cannot tell them apart.
        par = None
        for (t, E, _) in adm_cofactors(r, Jlo):
            Sp = cyc_multiset(t, E)
            rem = list(Sp)
            ok = True
            for d in sorted(Smin):
                if d in rem:
                    rem.remove(d)
                else:
                    ok = False
                    break
            if ok and sum(len(phi_poly(d)) - 1 for d in rem) == g:
                par = (Sp, sorted(rem))
                break
        print("      an admissible parent holding %s with %d degrees to "
              "spare: %s" % (list(Smin), g, "yes" if par else "NO"))
        if par:
            print("      parent %s, block %s -- so the swap STRUCTURE is "
                  "available and what is missing is the multiplier"
                  % (list(par[0]), par[1]))
        rest = list(R)
        used = []
        for (nm, m) in MEM:
            while True:
                d = polydiv(rest, m)
                if d is None:
                    break
                rest = d
                used.append(nm)
        print("      the residual divided by the members it does carry "
              "%s leaves %s" % (used or "(none)", rest))
        if len(rest) > 1:
            print("      that leftover: degree %d, height %d, value at 1 "
                  "%d, reciprocal %s, all roots on the unit circle %s, "
                  "cyclotomic part %s"
                  % (len(rest) - 1, height(rest), sum(rest),
                     list(reversed(rest)) == rest,
                     on_unit_circle(rest)[0], split_witness(rest)[1]))
            for (nm, m) in MEM:
                if polydiv(rest, m) is not None:
                    print("      the leftover is divisible by %s, so it "
                          "is not a new object" % nm)
            # Admit it as a member and ask the cell again. If hs falls to
            # h the obstruction was the CLASS and nothing else.
            ext = MEM + (("D", list(rest)),)
            MTX = mult_table(ext, r - 1)
            bl = blocks(r, Jlo, sorted(MTX))
            hsx, _ = swap_min(bl, MTX, xm1, pure_family_min(bl, xm1))
            print("      with the leftover admitted as a fourth member, "
                  "hs = %d against h = %d -- %s"
                  % (hsx, h, "reached" if hsx == h
                     else "STILL NOT REACHED"))
            okx, whyx = in_family(q, r, Jlo, MTX)
            print("      and the exhibited minimiser is then in the "
                  "family: %s -- %s" % (okx, whyx))

    print("\n   THE SHAM AGAINST THE PURE FAMILY, over the failing "
          "cells of the rectangle: does the sham EVER improve on the "
          "pure minimum, or does it never fire at all")
    nev = sum(1 for c in cells.values()
              if c["fail"] and c["hst"] == c["ph"])
    imp = sum(1 for c in cells.values()
              if c["fail"] and c["hst"] < c["ph"])
    print("   the sham matches ph at %d of the %d failing cells and "
          "beats it at %d" % (nev, nfail, imp))

    # ------------------------------------------------------ the tally
    print("\n" + "=" * 70)
    hit = ", ".join("%s x%d" % (k, n)
                    for k, n in sorted(fired.items()) if n)
    print("KILLS FIRED: %s" % (hit or "none"))
    print("wall %.1f s" % (time.time() - t_all))
    print("=" * 70)


if __name__ == "__main__":
    main()
