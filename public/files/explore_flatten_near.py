"""explore_flatten_near.py -- WHY DOES A RANK START FAILING?

explore_flatten_band.py answered the FAR end of the failing band. At
rank r = M - J, past a per-rank threshold, the least height h(M, J) of
a nonzero vector of the lattice (x-1)^J Z[x] cut at degree < M is the
height of the CHAMPION (1+x)^(r-1) (x-1)^J -- a pure product, so the
cell is clean -- and that champion is the whole minimiser set. The NEAR
end is stated open there and answered nowhere: scanning J UPWARD at a
fixed rank, the cells are clean, and then at J_lo(r) one fails. Why.

(The senses are the thread's, restated because this rig is read alone.
A vector c on M atoms is the polynomial P(x) = sum_i c_i x^i; its
FLATTENING is the multiplicity of the root 1; its HEIGHT is the sup
norm max_i |c_i|. h(M, J) is the least height of a nonzero P with
flattening at least J and degree < M. A PURE PRODUCT is prod_i
(x^{d_i} - 1) over a multiset D of positive PARTS; it has |D| factors,
degree sum D and flattening |D|. ph(M, J) is the least height of a pure
product admissible at the cell. RANK is always r = M - J. A cell FAILS
when h < ph -- when the lattice beats every pure product. The COFACTOR
of a lattice vector is q = P/(x-1)^J, of degree at most r - 1, and the
whole question lives in that variable.)

THE QUESTION, in one line: at the first failing depth of a rank, WHICH
vector is it that the pure family does not have -- and what changed at
that depth that did not hold one depth below.

THE HAND ATTACK, worked before any engine code.

FIRST, THE PURE FAMILY IN THE COFACTOR VARIABLE. A pure product with c
parts, c >= J, factors as (x-1)^c prod_{d in E} [d]_x with [d]_x = 1 +
x + ... + x^(d-1) and E the parts exceeding 1; the parts equal to 1
contribute nothing but their degree. So its cofactor is

    q = (x-1)^t prod_{d in E} [d]_x,   t = c - J >= 0,

and the degree budget deg q = sum D - J <= r - 1 reads t + sum_{d in
E} (d - 1) <= r - 1. THAT BUDGET IS NOT THE WHOLE ADMISSIBILITY. The
part count gives a SECOND constraint the degree does not imply: the
number of 1-parts is c - |E| = J + t - |E|, which must be nonnegative,
so

    |E| <= J + t.

BOTH constraints are imposed here. The parent rig's cofactor bound
imposes only the first, and a probe run before this rig was written --
a direct enumeration of both the constrained and the unconstrained
families over the whole parent rectangle at ranks 2 to 20 -- found the
two minima EQUAL at every cell, so the omission never moved a published
number. It is a PROBE reading and is re-measured at full scope as C6
rather than assumed. It is not cosmetic either way, because of what the
part count does to the champion.

SECOND, THE CHAMPION IS NOT ALWAYS A PURE PRODUCT, AND THAT IS THE
FIRST OF TWO MECHANISMS. The champion cofactor (1+x)^(r-1) = [2]_x^(r-1)
has t = 0 and E = {2}^(r-1), so its degree cost is exactly r - 1 and it
never violates the degree budget at any depth. It violates the PART
COUNT whenever |E| = r - 1 > J. Equivalently the pure product it stands
for, (x^2 - 1)^(r-1) (x-1)^(J-r+1), needs J >= r - 1 to have a
nonnegative number of (x-1) factors. So:

    at every cell with J < r - 1 the champion is a LATTICE VECTOR and
    NOT a pure product.

The lattice holds it -- deg (1+x)^(r-1) = r - 1 <= r - 1 is all the
lattice asks -- and the pure family cannot reach it. That is a
mechanism for failure available at exactly the shallow end of a
high-rank column, and it is invisible to the band rig's far-end
argument, which is asymptotic in J at fixed rank.

THIRD, WHAT THE COMMITTED NUMBERS ALREADY SAY, AND IT SPLITS THE
QUESTION IN TWO. The band rig's F6 records first failing depths J_lo(r)
= 26, 19, 12, 14, 10, 17, 19 at ranks 7, 8, 9, 11, 13, 15, 17. At rank
13, J_lo = 10 while r - 1 = 12: the rank's FIRST failure sits in the
regime where the champion is not a pure product at all. At rank 9,
J_lo = 12 while r - 1 = 8: the first failure sits above it. So the near
end is not one phenomenon, and any single-threshold story is already
refuted by numbers standing in the corpus. The two regimes are named
here:

    the DENIED regime, J < r - 1, where the pure family lacks the
    champion outright;
    the COMMITTED regime, J >= r - 1, where the champion is available
    to both sides and the question is whether the pure family's own
    argmin has yet BECOME the champion.

FOURTH, WHAT THE COMMITTED REGIME INHERITS FROM RANKS 3 AND 4. There
the champion is beaten INSIDE the pure family by low-order cofactors up
to a per-rank threshold -- largest non-attaining depth 6 at rank 3 and
12 at rank 4, with 1+x winning at rank 3 and (1+x)(1+x+x^2) at rank 4,
of vanishing order 1, 0 and 1 at -1 against champions of order 2 and 3
(explore_flatten_theorem.py arm F). Those two ranks never fail, so that
threshold explains a crossover in a CLEAN column and has never been
read at a rank that fails. Reading it at ranks 5 to 18, beside the
failure flag, is what this rig is for.

FIFTH, WHAT IS FREE FROM THE LATTICE SIDE AND WHAT IS NOT. Every rig in
this thread reduces the basis with lll_incr, which returns mu and the
squared Gram-Schmidt norms, and hands them to a ball enumeration that
prunes with them and reports neither. So the L2 GRAM-SCHMIDT PROFILE is
free. THE SUCCESSIVE MINIMA ARE NOT, and conflating the two would be
the whole error: the minima this thread's own rank-2 theorem states --
lambda_1 = h and lambda_2 = C(J, floor(J/2)) exactly, attained among
vectors independent of the minimiser at +-(1,0) and +-(0,1) and nowhere
else -- are SUP-NORM minima, while the Gram-Schmidt norms are L2 and
basis-dependent besides. A second enumeration is therefore written
here: the same Fincke-Pohst walk with the same shrinking radius, and
vectors proportional to the minimiser rejected. It starts from the L2
radius s_ub * sqrt(M), s_ub being the least sup norm among reduced
basis vectors independent of the minimiser -- which bounds lambda_2
because lambda_i <= max_{j<=i} ||b_j|| for any basis -- and shrinks to
(s - 1) * sqrt(M) on every improvement, which is sound because a vector
of sup norm at most s - 1 has L2 norm at most that. Both prints are
made and they are never identified with each other.

SIXTH, THE CONTROL, AND THE OBVIOUS ANSWER IS A TRANSPLANT. The rank-2
theorem gives lambda_2/lambda_1 ~ (sqrt(e)/2) sqrt(J+1). It is PROVED,
and it is proved about a lattice of RANK 2. A rank-18 lattice has
eighteen minima and no reason to follow a two-dimensional formula.
IT IS FLAGGED HERE AS A TRANSPLANT -- an intuition carried in from a
neighbouring value of the parameter -- and is used in this rig ONLY as
a sanity print on the rank-2 column, never as a baseline for any other
rank. The control is INSIDE the sweep -- each rank of 5..18 has clean
cells and failing cells in its own column, so a failing cell is read
against a CLEAN CELL OF ITS OWN RANK. If the gap cannot separate them
within a rank, that is the answer and it is a NO.

THE SCOPE. The parent chart's own rectangle, M = 4..40 and J = 2..30,
restricted to ranks 5..18 -- the failing ranks -- for the pure side and
the flag, which is where the answer key lives and where every cell is
already charted. The minima arm runs on the NEAR-END WINDOW of each
rank instead, J_lo - 4 to J_lo + 4 clipped to the column, because that
is where the question is and the second enumeration is the dear half.
Ranks 2, 3 and 4 carry the controls.

THE PREDICTIONS, fixed here before the engine ran.

P1. IN THE COMMITTED REGIME, COMMITMENT IS NECESSARY. At every failing
    cell with J >= r - 1, the pure family's argmin cofactor set
    contains the champion (1+x)^(r-1).
P2. IN THE DENIED REGIME, THE CHAMPION IS WHAT THE LATTICE HAS. At
    every failing cell with J < r - 1, the minimiser's cofactor is
    +-(1+x)^(r-1) up to the monomial factor -- the failure being exactly that the lattice holds
    the champion and the pure family may not.
P3. BELOW THE BAND THE PURE FAMILY IS EXTREMAL WITH ITS OWN WITNESS. At
    every clean cell below its rank's first failing depth, h = ph AND
    the minimiser's cofactor equals the pure argmin up to sign AND up
    to the monomial factor: the lattice has nothing the pure family
    lacks, rather than merely nothing shorter. The monomial belongs in
    the prediction and not only in the code, because the lattice is
    closed under multiplication by x inside the degree budget, so q and
    x q are the same vector for every purpose here. It was written "up
    to sign" when this slate was frozen and the smoke run corrected the
    COMPARISON without the prediction being restated; it is restated
    now, and it is the weaker claim of the two.
P4. THE GAP SEPARATES, WITHIN A RANK. At each rank of 5..18 the sup-norm
    ratio lambda_2/lambda_1 at the failing cells of the near-end window
    is strictly below its value at every clean cell of that window, the
    two ranges disjoint rank by rank.
P5. DENIAL ALONE CAUSES NOTHING. The regime J < r - 1 contains clean
    cells as well as failing ones, so "the champion is not a pure
    product here" is not by itself a failure criterion.

THE KILLS, frozen as OBSERVABLES the rig prints, never as inferences.

K1 A failing cell with J >= r - 1 whose printed pure argmin set does
   not contain the champion. P1 dies.
K2 A failing cell with J < r - 1 whose printed minimiser cofactor is
   not the champion up to sign and monomial. P2 dies.
K3 A clean cell below its rank's first failing depth whose printed
   minimiser cofactor is not the pure argmin up to sign and monomial.
   P3 dies.
K4 A rank of 5..18 whose failing and clean lambda_2/lambda_1 ranges
   over the near-end window OVERLAP. P4 dies at that rank.
K5 A regime column of the printed 2x2 table that is all failures or
   all clean. P5 dies.
K6 The admissible pure minimum differs from the parent's multiset bound
   or from its unconstrained cofactor bound at any answer-key cell of
   rank at most 20; or an argmin fails the part accounting; or ranks 3
   and 4's non-attaining depths miss 6 and 12. Instrument kill.
K7 The second enumeration reaches a nonzero vector of sup norm BELOW
route_h's h at any cell, or rank 2's lambda_2 differs from C(J,
floor(J/2)) at any depth. Instrument kill.
K8 The failure flag over the swept cells does not reproduce the
   parent's committed 83 failures at ranks 5..18. Answer-key kill.

THE POSITIVE CONTROLS, run before any survive/kill result is read. C1
rank 2 against the theorem at J = 2..20, the one place both minima are
proved: h against the closed form max_k |C(J,k) - C(J,k-1)| -- never
against the witness the walk was handed, which is the same vector twice
-- and lambda_2 against C(J, floor(J/2)) (K7). C2 the largest depth at
which the champion is present and does not attain ph, at ranks 3 and 4,
against the committed 6 and 12 (K6). C3 the admissible pure minimum
against the parent's multiset bound at every answer-key cell of rank at
most 20 (K6). C4 the second enumeration reaching NOTHING SHORTER than
route_h's h at every cell it runs on -- not its lambda_1 against that
h, which is v1's own height on both sides and cannot fail (K7). C5
every printed argmin re-checked as an admissible pure product by part
accounting -- |E| <= J + t, at least J parts, degree sum at most M - 1
-- and by the polynomial identity (K6). C6 the admissible pure minimum
against the parent rig's UNCONSTRAINED cofactor bound over the same
cells, which is the probe reading of the hand attack re-measured at
scope (K6). AND C7, WHICH WAS NOT AMONG THE CONTROLS FIXED BEFORE THE RUN: the residual
census against the parent's committed class -- B at 51 cells, A at 29,
A*B at 2 and C at 1, and the whole minimiser's cyclotomic part a pure
product at every failing cell (K6, K8). It could not be written before
the run because the census it compares is this rig's own output, so it
is an answer-key check added at run 5 and it is named here as one
rather than folded into the design.

COST. Single process, exact integer and rational arithmetic throughout,
no array library. The parent's 695-cell chart closes in about 30 s and
this sweep is 370 of those cells plus a second enumeration on about a
hundred OF THEM, the near-end windows being a subset and not extra cells; the estimate before the run was 2 to 5 minutes and the
wall is 41 s, comfortably under it and inside the ordinary analysis
footprint, and it is run under memwatch because the second
enumeration's footprint had no precedent.

THE FINDINGS.

F1. THE CHAMPION HAS NOTHING TO DO WITH THE NEAR END, AND P1 IS REFUTED
66 TIMES. Of the 82 failing cells in the committed regime, only 16 have
the champion in the pure argmin set at all; K1 fired at the other 66.
The stronger reading is the column, and it is COUNTED rather than read
off J_cm: the depth from which the champion is the pure argmin
continuously to the top of the column is undefined at TWELVE of the
fourteen ranks, and J_cm alone would not settle the stronger sentence,
being blind to an interior depth where the champion attains and loses
it again -- so the attaining depths are counted per column, and at
those twelve ranks the count is ZERO out of 21 to 29 depths each. The
champion never takes the pure family over anywhere the chart reaches
there. At the two ranks where it does, the attaining depths are 12 of
29 at rank 5 and 4 of 29 at rank 6, each a clean suffix from J_cm = 19
and 27, against first failures at 18 and 22: the rank fails BEFORE the
pure family commits, by one depth at rank 5 and five at rank 6. So the
mechanism that governs the far end -- the champion's asymptotic
takeover -- is simply absent at the near end, and the ranks-3-and-4
threshold does not extend to a rank that fails. The comparison at a
failing rank exists now, and what it says is that the low-rank
threshold story does not reach the band.

F2. WHAT ACTUALLY HAPPENS IS A CYCLOTOMIC SWAP INSIDE THE ARGMIN.
(SETTLED FURTHER, and this record's scope is the ARGMIN comparison
alone: explore_flatten_swap.py takes the same swap over EVERY admissible
pure cofactor and finds it reaches h at all 83 failing cells, so the 73
below are the sub-case where the parent happens to be the argmin. The
counts here are reproduced there exactly and nothing in this block is
withdrawn.) At
each rank the clean cell immediately below the first failure has a
minimiser whose residual is 1 -- a pure product, cyclotomics only --
and the first failing cell one depth up has a minimiser that is the
same kind of object with one cyclotomic BLOCK replaced by a single
non-cyclotomic factor. Counted over all 83 failing cells: at 78 the
minimiser's cyclotomic multiset is a SUBSET of the pure argmin's at the
same cell -- nothing gained -- and at 73 the dropped block and the
residual have the same degree, so the minimiser is the pure argmin with
a factor swapped for one of equal degree. The three commonest swaps
carry 64 of the 83, and the residual is PRINTED beside the dropped
block rather than read off its degree, two of the four residuals having
degree 2: Phi_2^2 -> B at 36 cells, Phi_5 -> A at 15 and Phi_3 -> B at
13, writing A and B for the parent's residuals below. At the fourteen
first-failing cells themselves the swap is B at five ranks (5, 6, 7, 8,
10) and A at the other nine. SIX of the 83 have a pure argmin SET
rather than a single argmin and at all six the members classify
differently, so the row taken is the one most favourable to the swap
and the two counts above are upper bounds by at most six.

F3. THE RESIDUAL CLASS IS REPRODUCED FROM THE FAILING CELLS ALONE, AND
IT IS THE PARENT'S. The four non-trivial residuals and their cell
counts come out 51, 29, 2, 1 -- B = 2 + 3x + 2x^2, A = 2 + 4x + 5x^2 +
4x^3 + 2x^4, A*B and C = 3 + 5x + 3x^2 -- matching the parent chart's
committed census exactly, and each with all its roots on the unit
circle by the exact Sturm test this rig runs (C7). That they are also
RECIPROCAL is the parent's finding and is not tested here. THAT IS A
REPRODUCTION AND NOT A NEW RESULT: the census is the parent chart's,
established over all 695 cells (explore_flatten_select.py). What is new
is F2, which says what the residual DOES -- the parent records which
multiplier appears, this rig records that it appears by replacing a
named cyclotomic block of the very same argmin.

F4. BELOW THE BAND THE LATTICE MINIMISER IS THE PURE ARGMIN ITSELF, AT
230 OF 230 CELLS. P3 holds without exception: at every clean cell below
its rank's first failure the exhibited minimiser's cofactor equals the
pure argmin up to sign and up to the monomial factor. This is a
COROLLARY of the parent's residual criterion rather than an independent
fact -- residual 1 makes the witness a pure product, and a pure product
of height h = ph is a minimal one -- and it is worth the print because
it is the statement the swap of F2 acts on.

F5. THE SUP-NORM GAP DOES NOT SEPARATE, AND P4 IS A NO. lambda_2 is
computed here at ranks above 2 for the first time in this thread. Over
each rank's near-end window the failing and clean ranges of
lambda_2/lambda_1 OVERLAP at twelve of the fourteen ranks; they are
disjoint with the failing cells below only at ranks 11 and 16, on one
and two failing cells respectively, which is a coincidence at that
count and not a separation. The values sit between 1.00 and 1.71
throughout with no trend in the rank, against 1.50 to 3.81 down the
whole rank-2 control column -- a range read off all nineteen of its
depths and not off the four the rig displays, which start at 2.00 and
would have made the contrast look cleaner than it is -- so the
two-dimensional picture -- one short vector and a wide gap -- is gone
by rank 5. The free L2 Gram-Schmidt spread falls monotonically with the
DEPTH inside each rank and does not fall with the rank: each rank's
window sits at its own J_lo, so rank 13 at J = 6 reads 0.283 against
rank 5 at J = 14 reading 0.168, and no comparison across ranks is
available from this sweep at all. So the lattice geometry, read through
its two shortest vectors, does not know which cells fail: what knows is
the FACTORISATION, which is F2.

F6. THE DENIED REGIME IS REAL AND NEARLY EMPTY OF FAILURES, AND P2 DIES
ON ITS ONE CELL. P5 holds: the 119 cells with J < r - 1 -- where the
champion is a lattice vector and provably not a pure product -- carry
exactly ONE failure, at rank 13 depth 10, against 82 failures among the
251 committed cells. So denial causes nothing on its own; a rate of 1
in 119 against 82 in 251 points the opposite way. Both denominators are
the regime's whole cell count and not its clean column, which is 118
and 169 and is what the 2x2 table displays. And at that one cell --
rank 13, depth 10, where h = 9 against ph = 10 and the pure argmin set
has five members -- the minimiser is not the champion either. Its
cyclotomic part is Phi_2^2 Phi_3 Phi_5 and its residual is A, which is
F2's swap and not a third mechanism. So P2 is refuted at the only cell
that could test it, and the denied regime turns out to be the same
phenomenon as the rest.

F7. THE PART-COUNT CONSTRAINT IS REAL AND NEVER BITES. |E| <= J + t is
a genuine admissibility condition the parent's cofactor bound does not
impose, and imposing it changes the pure minimum at NONE of the 496
answer-key cells of rank 2 to 20 (C6), nor the multiset bound at any of
them (C3). The parent's published numbers are unaffected. What the
constraint is load-bearing for is the STATEMENT of F6 -- the champion's
absence from the pure family below J = r - 1 -- which is a fact about
the family and not about any routine.

THE RUN RECORD. SIXTEEN full runs. RUNS 1 AND 2 are the same code and
run 1 is the science: every value quoted in F1 and F4 to F7 is its
value and every later run reproduces all of them, run 2 differing only
in being captured whole to a file rather than read at its tail. RUNS 3
TO 5 each ADD an arm rather than change one, because a sentence of this
record would otherwise have rested on a reading of printed rows rather
than on a printed number: run 3 added the factored census and the
per-rank transition rows, run 4 the TRADE count that turns F2 from an
eyeball into a pair of counts, and run 5 the C7 comparison against the
parent's committed residual class, which the census of run 3 first made
available. The three arms added are measurements over cells run 1 had
already decided; no cell's h, ph or flag moved. RUN 6 carries the
audit's two corrections and both were to this record rather than to a
result: the TRADE grouping keys on the residual as well as on the
dropped block now, because two of the four residuals have degree 2 and
F2's pairing was being read off a degree match rather than off a print
-- it survives, all three counts unchanged; and F5's rank-2 comparison
is computed over the whole control column, whose nineteen depths run
1.50 to 3.81 where the four the rig displays run 2.00 to 3.81. Both
were quoted wrong here and in the commit that first landed this record.
RUNS 7 AND 8 carry the audit's next two, and the second MOVED numbers.
Run 7: C4 was comparing the second walk's lambda_1 with route_h's h,
which is one vector's height on both sides and could not fail; the walk
now reports the least sup norm it reached over ANY nonzero vector and
K7 fires if that is below h, which it is not at any cell. Run 8: the
TRADE was classifying each failing cell against bs[0], an arbitrary
member of the pure argmin SET. Six of the 83 cells have a set, all six
classify differently across their members, and taking the most
favourable member moves the counts from 76 and 71 to 78 and 73 and the
Phi_5 -> A class from 14 cells to 15. The figures before run 8 were
understated and depended on an enumeration order. RUN 9 adds the
per-column COUNT of depths at which the champion attains, because F1's
strongest sentence had been resting on J_cm, which reads a suffix and
cannot see an interior attainment. The count is zero at all twelve
ranks, so the sentence was right and was unmeasured. Two arithmetic
faults stood in this record through run 9 and neither is a rig fault:
F6's denominators were the 2x2 table's CLEAN columns, 118 and 169,
where the regimes hold 119 and 251 cells; and F5 called the
Gram-Schmidt spread monotone in the RANK where the sweep compares it
only within one, each rank's window sitting at its own first failure.
RUN 10 finishes the tautology sweep run 7 started: C1 was still
comparing rank 2's lambda_1 with route_h's h, the same vector on both
sides, where the rank-2 theorem supplies an independent closed form for
h. It compares against that now and passes at all nineteen depths. RUN
11 fixes the NEAR-END table, which was displaying the first two members
of the pure argmin set truncated to 24 characters -- so a cell with
seven argmins showed one of them, lost the +N marker to the same
truncation, and printed a 'same' verdict computed over the whole set
beside a polynomial visibly unequal to the minimiser. It prints the
set's SIZE and, where one member matches, THAT member. RUN 12 fixes the
residual census's pure-product column, which was testing the COFACTOR's
cyclotomic multiset -- Phi_2^2, which is not a pure product's divisor
multiset -- and printing NOT beside a residual, where the parent's
statement is about the whole minimiser and its J further copies of
Phi_1. Tested on the whole vector it is a pure product at 83 of the 83
failing cells, the parent's finding over its 695 reproduced here from
the failing ones alone, and the column now names which object it
tested. RUN 13 declares C7 in the controls list, where it had been
printed and cited by F3 while the list fixed before the run stopped at
C6, and gives it the pure-product reading run 12 added so that the
check fires K8 rather than only printing. RUN 14 restates P2, P3, K2
and K3, which had said 'up to sign' where the comparison the smoke run
installed is up to sign AND the monomial factor -- the weaker test, so
the predictions as frozen were stronger than what was measured and F4's
230 of 230 read stronger than it is. No count moves; the claims now say
what the rig tests. RUN 15 renames the near-end table's argmin-set
column, which was headed |A| three lines above a census in which A is
the quartic residual, and glosses it so the two cannot be read as one.
RUN 16 lands a fix run 6 reported and did not make: F3's reciprocity
clause was to be scoped to the parent, and the edit that did it matched
nothing and said nothing, so the record carried the unscoped sentence
and a run record claiming it had been scoped, for ten runs.

TWO SMOKE RUNS before run 1, at M <= 20 with ranks 5..8 and then at
M <= 28 with ranks 5..7, the second widened because the first had an
EMPTY failing set and so exercised no kill but K5 and K8. The second
found the one fault that mattered: the minimiser cofactor was being
compared to the pure argmin as a polynomial, and the lattice is closed
under multiplication by x, so a minimiser that was the argmin SHIFTED
read as different -- K3 fired at three cells of rank 6 that refute
nothing. No control would have caught it, both readings being about
vectors that exist; the comparison strips the monomial factor now, and
the smoke's own P3 count went from 33 of 36 to 36 of 36 -- what the
unfixed comparison would have read at full scope was never measured,
the fix landing before run 1. Both smokes were run before any science
printed.

Single process, exact integer and rational arithmetic throughout, wall
40.9 to 42.1 s across the fifteen timed runs, peak working set 43.5 to 44.9 MB
under memwatch against the 512 MB ceiling, no cell reaching the
enumeration's node cap.
"""
import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time
from math import comb, floor as mfloor
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_flatten_offchart import NodeCap
from explore_flatten_lattice import frac_sqrt_up
from explore_flatten_family import (route_h, polydiv, family_tables,
                                    family_bound, split_witness,
                                    as_pure_product, on_unit_circle,
                                    phi_poly)
from explore_flatten_band import mulp, xm1_pow, ph_cof, height

# The parent chart, which is this rig's answer key and nothing else.
KEY_M = 40
KEY_J = 30
KEY_FAILURES = 83
# The parent's committed residual class, cell counts descending.
KEY_RESIDUAL_COUNTS = (51, 29, 2, 1)
RANKS = range(5, 19)
CTRL_JMAX = 20
KEY_RANK_CAP = 20
NEAR = 4
SECOND_CAP = 20000000


# ------------------------------------------ the admissible pure family

def adm_cofactors(r, J):
    """Every pure-product cofactor admissible at rank r and depth J:
    q = (x-1)^t prod_{d in E} [d]_x with t + sum (d - 1) <= r - 1 AND
    |E| <= J + t, the second constraint being the part count the degree
    budget does not imply. Returns a list of (t, E, q)."""
    out = []

    def rec(start, e, E, poly):
        t, q = 0, poly
        while t + e <= r - 1:
            if len(E) <= J + t:
                out.append((t, tuple(E), q))
            q = mulp(q, [-1, 1])
            t += 1
        for d in range(start, r + 1):
            if e + d - 1 > r - 1:
                break
            rec(d, e + d - 1, E + [d], mulp(poly, [1] * d))

    rec(2, 0, [], [1])
    return out


def champ_cof(r):
    """(1 + x)^(r-1), the champion's cofactor."""
    p = [1]
    for _ in range(r - 1):
        p = mulp(p, [1, 1])
    return p


def canon(p):
    """Trim, DROP THE MONOMIAL FACTOR and fix the sign, so that two
    cofactors compare as the LATTICE sees them. The monomial matters:
    the lattice is spanned by x^i (x-1)^J and so is closed under
    multiplication by x inside the degree budget, which makes q and x q
    two vectors of the same height and the same shape. Comparing
    without stripping x reports a minimiser as DIFFERENT from the pure
    argmin it is a shift of -- which a smoke run of this rig did at
    three cells of rank 6 before the strip was added, and no control
    would have caught it, both readings being about vectors that exist."""
    q = list(p)
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    while len(q) > 1 and q[0] == 0:
        q.pop(0)
    if q[-1] < 0:
        q = [-c for c in q]
    return tuple(q)


def same_shape(u, v):
    """Two cofactors equal up to sign and up to the monomial factor."""
    return canon(u) == canon(v)


def pure_min(r, J, xm1):
    """(ph, the argmin SET as canonical cofactors, the champion's own
    height or None where it is inadmissible, whether the champion is in
    the argmin set). No early abort: the SET is the deliverable."""
    ch = canon(champ_cof(r))
    best, bestset, chh = None, [], None
    for (t, E, q) in adm_cofactors(r, J):
        hq = height(mulp(q, xm1))
        c = canon(q)
        if c == ch:
            chh = hq
        if best is None or hq < best:
            best, bestset = hq, [c]
        elif hq == best and c not in bestset:
            bestset.append(c)
    return best, bestset, chh, ch in bestset


def describe(p):
    """A cofactor as (x-1)^a (1+x)^b times what is left, which is how
    the mechanism reads it. The remainder prints as its coefficient
    list, low degree first."""
    q = list(canon(p))
    a = 0
    while True:
        d = polydiv(q, [-1, 1])
        if d is None:
            break
        q, a = d, a + 1
    b = 0
    while True:
        d = polydiv(q, [1, 1])
        if d is None:
            break
        q, b = d, b + 1
    s = ""
    if a:
        s += "(x-1)^%d" % a
    if b:
        s += "(1+x)^%d" % b
    if q != [1] or not s:
        s += str(list(q))
    return s


# ------------------------------------------------- the second minimum

def parallel_to(v, w):
    """v proportional to w, both integer vectors of the same length."""
    i0 = next(i for i, c in enumerate(w) if c)
    return all(v[i0] * w[j] == w[i0] * v[j] for j in range(len(w)))


def enum_second(B, mu, A, M, R2, cap, v1):
    """The least SUP norm among lattice vectors NOT proportional to v1,
    with a witness, the least sup norm over ALL nonzero vectors the walk
    reached, and the node count. Fincke-Pohst with the radius shrunk to
    (s - 1) sqrt(M) on every improvement, which is sound because a
    vector of sup norm at most s - 1 has L2 norm at most that. Raises
    NodeCap past the budget rather than reporting a number it cannot
    stand behind.

    THE THIRD RETURN IS WHAT MAKES C4 A CONTROL RATHER THAN A
    TAUTOLOGY. Comparing a lambda_1 read off v1 with route_h's h
    compares a value with itself, v1 BEING route_h's witness. What this
    walk can say independently is that it reached nothing SHORTER: the
    final radius is (lambda_2 - 1) sqrt(M) and lambda_2 >= h, so every
    vector of sup norm at most h - 1 stayed inside the ball for the
    whole walk and would have been seen. So any_ < h is a real
    contradiction between two enumerations and any_ >= h is a real
    pass, while any_ > h only says v1's own L2 norm was outside the
    shrunk radius and is not a finding."""
    n = len(B)
    x = [0] * n
    best = [None, None]
    any_ = [None]
    nodes = [0]
    rad = [R2]

    def rec(i, partial):
        nodes[0] += 1
        if nodes[0] > cap:
            raise NodeCap
        if i < 0:
            if not any(x):
                return
            v = [sum(x[j] * B[j][t] for j in range(n)) for t in range(M)]
            s = max(abs(c) for c in v)
            if any_[0] is None or s < any_[0]:
                any_[0] = s
            if parallel_to(v, v1):
                return
            if best[0] is None or s < best[0]:
                best[0], best[1] = s, v
                rad[0] = F((s - 1) ** 2 * M)
            return
        c = -sum(mu[j][i] * x[j] for j in range(i + 1, n))
        rem = rad[0] - partial
        if rem < 0:
            return
        sq = frac_sqrt_up(rem / A[i])
        lo, hi = mfloor(c - sq), -mfloor(-(c + sq))
        mid = mfloor(c + F(1, 2))
        for xi in sorted(range(lo, hi + 1), key=lambda t: abs(t - mid)):
            d = (F(xi) - c) ** 2 * A[i]
            if d <= rad[0] - partial:
                x[i] = xi
                rec(i - 1, partial + d)
        x[i] = 0

    rec(n - 1, F(0))
    return best[0], best[1], any_[0], nodes[0]


def minima(M, v1, red):
    """lambda_1, lambda_2, the second witness, the L2 Gram-Schmidt
    profile, the least sup norm the second walk reached over ANY nonzero
    vector, and the node count at one cell. lambda_1 is v1's own height
    and so is route_h's h restated; the independent reading is amin, and
    enum_second says why."""
    B, mu, A = red
    s_ub = None
    for b in B:
        if not parallel_to(b, v1):
            s = max(abs(c) for c in b)
            if s_ub is None or s < s_ub:
                s_ub = s
    l2, w, amin, nodes = enum_second(B, mu, A, M, F(s_ub * s_ub * M),
                                     SECOND_CAP, v1)
    l1 = max(abs(c) for c in v1)
    return l1, l2, w, list(A), amin, nodes


# ----------------------------------------------------------- the cells

def column(r):
    """The chart's own depths at rank r: J from 2 up, with M = J + r at
    most 40 and J at most 30."""
    return list(range(2, min(KEY_J, KEY_M - r) + 1))


def main():
    t_all = time.time()
    fired = dict(("K%d" % i, 0) for i in range(1, 9))

    print("=" * 70)
    print("explore_flatten_near.py -- why does a rank start failing?")
    print("=" * 70)

    # ------------------------------------------------------- C3 and C6
    print("\n[C3] the admissible pure minimum against the parent's "
          "MULTISET bound, and [C6] against its UNCONSTRAINED cofactor "
          "bound, over every answer-key cell of rank 2..%d"
          % KEY_RANK_CAP)
    t = time.time()
    ptab, _ = family_tables(KEY_M - 1, [1])
    n3 = bad3 = bad6 = 0
    for M in range(4, KEY_M + 1):
        for J in range(2, min(KEY_J, M - 1) + 1):
            r = M - J
            if r > KEY_RANK_CAP or r < 2:
                continue
            xm1 = xm1_pow(J)
            a = family_bound(ptab, J, M - 1)[0]
            b, _, _, _ = pure_min(r, J, xm1)
            c, _ = ph_cof(M, J, xm1)
            n3 += 1
            if a != b:
                bad3 += 1
                fired["K6"] += 1
                if bad3 <= 5:
                    print("   K6 multiset M=%d J=%d r=%d: %s vs %s"
                          % (M, J, r, a, b))
            if b != c:
                bad6 += 1
                fired["K6"] += 1
                if bad6 <= 5:
                    print("   K6 unconstrained M=%d J=%d r=%d: %s vs %s"
                          % (M, J, r, b, c))
    print("   %d cells; %d disagree with the multiset bound, %d with "
          "the unconstrained cofactor bound (%.1f s)"
          % (n3, bad3, bad6, time.time() - t))

    # -------------------------------------------------------------- C5
    print("\n[C5] every argmin of the swept cells re-checked as an "
          "admissible pure product, by part accounting and by the "
          "polynomial identity")
    n5 = bad5 = 0
    for r in list(RANKS) + [2, 3, 4]:
        for J in column(r):
            xm1 = xm1_pow(J)
            _, bs, _, _ = pure_min(r, J, xm1)
            adm = adm_cofactors(r, J)
            for c in bs:
                n5 += 1
                ok = False
                for (t_, E, q) in adm:
                    if canon(q) != c:
                        continue
                    ones = J + t_ - len(E)
                    D = list(E) + [1] * ones
                    P = [1]
                    for d in D:
                        P = mulp(P, [-1] + [0] * (d - 1) + [1])
                    if (ones >= 0 and len(D) >= J
                            and sum(D) <= J + r - 1
                            and P == mulp(q, xm1)):
                        ok = True
                        break
                if not ok:
                    bad5 += 1
                    fired["K6"] += 1
                    if bad5 <= 5:
                        print("   K6 argmin not an admissible pure "
                              "product at r=%d J=%d: %s" % (r, J, c))
    print("   %d argmin cofactors checked, %d not admissible"
          % (n5, bad5))

    # -------------------------------------------------------------- C2
    print("\n[C2] the depths at which the champion is PRESENT and "
          "beaten inside the pure family, ranks 3 and 4, against the "
          "committed largest 6 and 12")
    last = {}
    for r in (3, 4):
        miss = []
        for J in range(2, KEY_J + 1):
            _, bs, chh, att = pure_min(r, J, xm1_pow(J))
            if chh is not None and not att:
                miss.append(J)
        last[r] = max(miss, default=None)
        print("   rank %d: beaten at J = %s, largest %s"
              % (r, miss, last[r]))
    if (last[3], last[4]) != (6, 12):
        fired["K6"] += 1
        print("   K6 the committed thresholds are not reproduced")

    # --------------------------------------------------------- C1 + C4
    print("\n[C1] rank 2's two minima against the theorem, J = 2..%d"
          % CTRL_JMAX)
    bad1 = 0
    for J in range(2, CTRL_JMAX + 1):
        M = J + 2
        h, v, _, red = route_h(M, J)
        _, l2, _, _, amin, _ = minima(M, v, red)
        want = comb(J, J // 2)
        # THE FIRST MINIMUM IS CHECKED AGAINST THE THEOREM'S CLOSED
        # FORM AND NEVER AGAINST THE WITNESS IT CAME FROM: the second
        # walk is handed route_h's own vector, so reading lambda_1 off
        # it and comparing with h compares a value with itself. What
        # the rank-2 theorem gives independently is the binomial row's
        # largest first difference.
        row = [0] + [comb(J, k) for k in range(J + 1)] + [0]
        D = max(abs(row[k] - row[k - 1]) for k in range(1, len(row)))
        if (h != D or l2 != want
                or (amin is not None and amin < h)):
            bad1 += 1
            fired["K7"] += 1
            print("   K7 J=%d: h %s vs the closed form %s, lambda_2 %s "
                  "vs %s, least sup norm reached %s"
                  % (J, h, D, l2, want, amin))
    print("   %d depths, %d wrong -- h against the theorem's closed "
          "form, lambda_2 against C(J, floor(J/2)), and the walk "
          "reaching nothing shorter than h" % (CTRL_JMAX - 1, bad1))
    r2 = []
    for J in range(2, CTRL_JMAX + 1):
        h, v, _, red = route_h(J + 2, J)
        l1, l2, _, _, _, _ = minima(J + 2, v, red)
        r2.append((l2 / l1, J))
    print("   over the WHOLE control column the rank-2 ratio runs "
          "%.4f at J=%d to %.4f at J=%d, and it is not monotone -- the "
          "range is quoted from here and never from the four depths "
          "printed below" % (min(r2)[0], min(r2)[1], max(r2)[0],
                             max(r2)[1]))
    print("   the rank-2 ratio against the TRANSPLANTED asymptotic -- a "
          "rank-2 fact, printed here as a sanity check on that column "
          "and used as a baseline for no other rank:")
    for J in (2, 5, 10, 20):
        M = J + 2
        h, v, _, red = route_h(M, J)
        l1, l2, _, _, _, _ = minima(M, v, red)
        pred = (2.718281828459045 ** 0.5 / 2) * ((J + 1) ** 0.5)
        print("      J=%2d  lambda_2/lambda_1 = %7.4f   (sqrt(e)/2)"
              "sqrt(J+1) = %7.4f" % (J, l2 / l1, pred))

    # ------------------------------------------------- ARM 1: the sweep
    print("\nARM 1 -- THE PURE ARGMIN BESIDE THE FAILURE FLAG, "
          "RANKS 5..18 ON THE PARENT RECTANGLE")
    t = time.time()
    cells = {}
    nfail = 0
    for r in RANKS:
        for J in column(r):
            M = J + r
            xm1 = xm1_pow(J)
            h, v, _, red = route_h(M, J)
            ph, bs, chh, att = pure_min(r, J, xm1)
            q = polydiv(v, xm1)
            fail = h < ph
            nfail += fail
            cells[(r, J)] = dict(M=M, h=h, ph=ph, fail=fail, bs=bs,
                                 chh=chh, att=att, q=q, v=v, red=red,
                                 denied=(J < r - 1))
    print("   %d cells swept, %d failures (%.1f s)"
          % (len(cells), nfail, time.time() - t))
    if nfail != KEY_FAILURES:
        fired["K8"] += 1
        print("   K8 the parent's %d failures are not reproduced"
              % KEY_FAILURES)

    jlo = {}
    for r in RANKS:
        f = [J for J in column(r) if cells[(r, J)]["fail"]]
        jlo[r] = min(f) if f else None
    jcm = {}
    for r in RANKS:
        d = None
        for J in reversed(column(r)):
            if cells[(r, J)]["att"]:
                d = J
            else:
                break
        jcm[r] = d
    print("\n   J_lo is the first failing depth; J_cm the depth from "
          "which the champion is in the pure argmin set continuously to "
          "the top of the column; r - 1 the depth from which it is a "
          "pure product at all")
    print("   rank  r-1  J_cm  J_lo  att   regime of the first "
          "failure  flags up the column from J = 2 (C clean, F fail)")
    print("   att is the count of depths in the column at which the "
          "champion IS in the pure argmin set, which J_cm cannot give: "
          "J_cm reads the maximal SUFFIX and is blind to an interior "
          "depth where the champion attains and then loses it again")
    for r in RANKS:
        s = "".join("F" if cells[(r, J)]["fail"] else "C"
                    for J in column(r))
        reg = ("--" if jlo[r] is None
               else ("DENIED" if jlo[r] < r - 1 else "COMMITTED"))
        nat = sum(1 for J in column(r) if cells[(r, J)]["att"])
        print("   %4d %4d %5s %5s %4d/%-3d  %-11s %s"
              % (r, r - 1, jcm[r], jlo[r], nat, len(column(r)),
                 reg, s))

    print("\n   THE NEAR END, cell by cell: the last clean depths and "
          "the first failing ones at each rank; arg is the SIZE of "
          "the pure argmin set at that cell, and A and B below are "
          "residuals and not this column")
    print("   %4s %3s %4s %8s %8s %4s %3s  %-28s %-28s %s"
          % ("r", "J", "reg", "h", "ph", "fail", "arg",
             "a pure argmin, the matching one", "minimiser cofactor",
             "same"))
    for r in RANKS:
        if jlo[r] is None:
            continue
        for J in column(r):
            if not (jlo[r] - NEAR <= J <= jlo[r] + 2):
                continue
            c = cells[(r, J)]
            # THE ARGMIN SHOWN IS THE ONE THE COMPARISON USED. Where
            # the set has a member equal to the minimiser that member
            # is displayed, because printing an arbitrary one beside a
            # "y" shows the reader two different polynomials and
            # asserts they are the same. |set| is printed so a tie is
            # never hidden by the column width.
            hit = [b for b in c["bs"] if same_shape(c["q"], list(b))]
            show = describe(list((hit or c["bs"])[0]))
            print("   %4d %3d %4s %8d %8d %4s %3d  %-28s %-28s %s"
                  % (r, J, "D" if c["denied"] else "C", c["h"], c["ph"],
                     "F" if c["fail"] else ".", len(c["bs"]),
                     show[:28], describe(c["q"])[:28],
                     "y" if hit else "n"))

    # -------------------------------------------- P1, P2, P3, P5
    print("\n   P1  committed-regime failures whose pure argmin set "
          "contains the champion")
    n = ok = 0
    for (r, J), c in sorted(cells.items()):
        if c["fail"] and not c["denied"]:
            n += 1
            if c["att"]:
                ok += 1
            else:
                fired["K1"] += 1
                if fired["K1"] <= 6:
                    print("      K1 r=%d J=%d argmin %s"
                          % (r, J, [describe(list(b)) for b in c["bs"]]))
    print("      %d of %d committed failures" % (ok, n))

    print("\n   P2  denied-regime failures whose minimiser cofactor IS "
          "the champion")
    n = ok = 0
    for (r, J), c in sorted(cells.items()):
        if c["fail"] and c["denied"]:
            n += 1
            if same_shape(c["q"], champ_cof(r)):
                ok += 1
            else:
                fired["K2"] += 1
                if fired["K2"] <= 6:
                    print("      K2 r=%d J=%d cofactor %s"
                          % (r, J, describe(c["q"])))
    print("      %d of %d denied failures" % (ok, n))

    print("\n   P3  clean cells BELOW their rank's first failure whose "
          "minimiser cofactor is the pure argmin up to sign and "
          "monomial")
    n = ok = 0
    for (r, J), c in sorted(cells.items()):
        if jlo[r] is None or J >= jlo[r] or c["fail"]:
            continue
        n += 1
        if any(same_shape(c["q"], list(b)) for b in c["bs"]):
            ok += 1
        else:
            fired["K3"] += 1
            if fired["K3"] <= 6:
                print("      K3 r=%d J=%d minimiser %s argmin %s"
                      % (r, J, describe(c["q"]),
                         [describe(list(b)) for b in c["bs"]]))
    print("      %d of %d clean-below cells" % (ok, n))

    print("\n   P5  the 2x2 table: regime against the flag")
    tab = {}
    for c in cells.values():
        k = ("denied" if c["denied"] else "committed", c["fail"])
        tab[k] = tab.get(k, 0) + 1
    for reg in ("denied", "committed"):
        print("      %-10s fail %4d   clean %4d"
              % (reg, tab.get((reg, True), 0), tab.get((reg, False), 0)))
        if tab.get((reg, True), 0) == 0 or tab.get((reg, False), 0) == 0:
            fired["K5"] += 1
            print("      K5 the %s column is pure" % reg)

    print("\n   THE MINIMISER CENSUS AT THE FAILING CELLS: which "
          "cofactor is it that the pure family does not have, written "
          "as its (1+x) part times what is left")
    cen = {}
    for (r, J), c in sorted(cells.items()):
        if not c["fail"]:
            continue
        w = list(canon(c["q"]))
        a = 0
        while True:
            d = polydiv(w, [1, 1])
            if d is None:
                break
            w, a = d, a + 1
        cen.setdefault((tuple(w), a - (r - 1)), []).append((r, J))
    for (w, off), ws in sorted(cen.items(), key=lambda kv: -len(kv[1])):
        print("      %-18s x (1+x)^(r-1%+d)  %3d cells, ranks %s"
              % (str(list(w)), off, len(ws),
                 sorted(set(r for (r, _) in ws))))

    print("\n   THE SAME CENSUS FACTORED BY THE PARENT'S OWN "
          "MACHINERY: the cofactor's cyclotomic indices, whether the "
          "WHOLE minimiser's are a pure product's divisor "
          "multiset, and the RESIDUAL left over")
    res = {}
    nonpp = 0
    for (r, J), c in sorted(cells.items()):
        if not c["fail"]:
            continue
        _, S, w = split_witness(list(c["q"]))
        # THE PURE-PRODUCT TEST IS ON THE WHOLE VECTOR AND NOT ON THE
        # COFACTOR. split_witness is handed q = P/(x-1)^J, so the J
        # copies of Phi_1 that (x-1)^J carries are not in S, and asking
        # whether S alone is a pure product's divisor multiset asks a
        # question about an object nobody built -- Phi_2^2 is not one
        # and (x^2-1)^2 is. The parent's statement, that the cyclotomic
        # part of every minimiser is a pure product, is about P.
        if as_pure_product(sorted(list(S) + [1] * J)) is None:
            nonpp += 1
        res.setdefault(w, []).append((r, J, S, J))
    for w, ws in sorted(res.items(), key=lambda kv: -len(kv[1])):
        S, J0 = ws[0][2], ws[0][3]
        pp = as_pure_product(sorted(list(S) + [1] * J0))
        circ = on_unit_circle(list(w)) if len(w) > 1 else True
        big = [d for d in (pp or ()) if d > 1]
        print("      residual %-18s %3d cells, ranks %s; the first "
              "cell's cofactor cyclotomics %s, which with the "
              "flattening factor's %d copies of Phi_1 are the divisors "
              "of the pure product with parts %s and %d ones; residual "
              "roots on the unit circle: %s"
              % (str(list(w)), len(ws),
                 sorted(set(r for (r, _, _, _) in ws)), list(S), J0,
                 big if pp else "NONE -- not a pure product",
                 len(pp) - len(big) if pp else 0, circ))
    print("      the cyclotomic part of the whole minimiser is a pure "
          "product at %d of the %d failing cells, which is the "
          "parent's statement over its 695 read here over the failing "
          "ones alone" % (nfail - nonpp, nfail))
    got = tuple(sorted((len(ws) for ws in res.values()), reverse=True))
    named = dict((w, len(ws)) for w, ws in res.items())
    print("   [C7] that census against the parent's committed residual "
          "class -- 1 at the clean cells, B = 2 + 3x + 2x^2 at 51, "
          "A = 2 + 4x + 5x^2 + 4x^3 + 2x^4 at 29, A*B at 2 and "
          "C = 3 + 5x + 3x^2 at 1")
    if (got != KEY_RESIDUAL_COUNTS or named.get((2, 3, 2)) != 51
            or named.get((2, 4, 5, 4, 2)) != 29 or nonpp):
        fired["K8"] += 1
        print("      K8 the committed residual class is not reproduced: "
              "%s" % (got,))
    else:
        print("      reproduced exactly, %s, and this rig reaches it "
              "from the FAILING cells alone" % (got,))
    print("      and the pure argmin just BELOW each rank's first "
          "failure, factored the same way:")
    for r in RANKS:
        if jlo[r] is None or jlo[r] - 1 not in column(r):
            continue
        c = cells[(r, jlo[r] - 1)]
        _, S, w = split_witness(list(c["q"]))
        cf = cells[(r, jlo[r])]
        _, S2, w2 = split_witness(list(cf["q"]))
        print("      r=%2d J=%2d clean %-14s cyclotomics %-22s -> "
              "J=%2d fail residual %-14s cyclotomics %s"
              % (r, jlo[r] - 1, str(list(w)), str(list(S)), jlo[r],
                 str(list(w2)), list(S2)))

    print("\n   THE TRADE, counted over every failing cell: the pure "
          "argmin at the SAME cell against the minimiser, both "
          "factored, and what the multisets differ by")
    trade = {}
    ties = tiesplit = 0
    for (r, J), c in sorted(cells.items()):
        if not c["fail"]:
            continue
        _, Sf, Rf = split_witness(list(c["q"]))
        deg = len(Rf) - 1
        # THE ARGMIN SET CAN HAVE MORE THAN ONE MEMBER, AND WHICH ONE
        # IS READ DECIDES THE ROW. Every member is classified and the
        # BEST classification is taken -- gaining nothing first, then
        # matching the residual's degree -- so a tie can only ever be
        # reported in the swap's favour, which is the direction that
        # has to be declared. tiesplit counts the cells where the
        # members disagree, and it is the honest size of the choice.
        got = []
        for cand in c["bs"]:
            _, Sp, _ = split_witness(list(cand))
            out, back = list(Sp), list(Sf)
            for d in list(out):
                if d in back:
                    out.remove(d)
                    back.remove(d)
            dout = sum(len(phi_poly(d)) - 1 for d in out)
            got.append((tuple(sorted(out)), tuple(sorted(back)), Rf,
                        dout == deg))
        if len(c["bs"]) > 1:
            ties += 1
            if len(set(got)) > 1:
                tiesplit += 1
        got.sort(key=lambda k: (len(k[1]), not k[3]))
        trade.setdefault(got[0], []).append((r, J))
    swap = block = 0
    for (out, back, Rf, samedeg), ws in sorted(
            trade.items(), key=lambda kv: -len(kv[1])):
        if not back:
            swap += len(ws)
            if samedeg:
                block += len(ws)
        print("      argmin drops %-14s gains %-8s  for the residual "
              "%-16s  degrees match: %-5s  %3d cells, ranks %s"
              % (str(list(out)), str(list(back)), str(list(Rf)),
                 samedeg, len(ws), sorted(set(r for (r, _) in ws))))
    print("      %d of the failing cells have a pure argmin SET rather "
          "than a single argmin, and at %d of those the members do not "
          "all classify the same way -- where they differ the row taken "
          "is the one most favourable to the swap" % (ties, tiesplit))
    print("      %d of %d failing cells GAIN no cyclotomic index: the "
          "minimiser's cyclotomic part DIVIDES the pure argmin's and "
          "the difference is one non-cyclotomic residual. At %d of "
          "those the dropped block and the residual have the same "
          "degree." % (swap, nfail, block))

    # ----------------------------------------------- ARM 2: the minima
    print("\nARM 2 -- THE SUP-NORM MINIMA OVER EACH RANK'S NEAR-END "
          "WINDOW, AND THE L2 PROFILE BESIDE THEM")
    t = time.time()
    print("   %4s %3s %4s %4s %8s %8s %9s %9s %s"
          % ("r", "J", "reg", "fail", "lam1", "lam2", "lam2/lam1",
             "b1*/bn*", "nodes"))
    gaps = {}
    caps = 0
    for r in RANKS:
        if jlo[r] is None:
            continue
        for J in column(r):
            if not (jlo[r] - NEAR <= J <= jlo[r] + NEAR):
                continue
            c = cells[(r, J)]
            try:
                l1, l2, w, A, amin, nodes = minima(c["M"], c["v"],
                                                  c["red"])
            except NodeCap:
                caps += 1
                print("   %4d %3d  the node cap %d was reached; no "
                      "value" % (r, J, SECOND_CAP))
                continue
            if amin is not None and amin < c["h"]:
                fired["K7"] += 1
                print("      K7 r=%d J=%d the second walk reached sup "
                      "norm %s below route_h's h = %s"
                      % (r, J, amin, c["h"]))
            spread = float(A[0] / A[-1]) ** 0.5
            gaps.setdefault(r, []).append((J, c["fail"], l2 / l1))
            print("   %4d %3d %4s %4s %8d %8d %9.4f %9.3f %s"
                  % (r, J, "D" if c["denied"] else "C",
                     "F" if c["fail"] else ".", l1, l2, l2 / l1,
                     spread, nodes))
    print("   %d cells hit the node cap (%.1f s)"
          % (caps, time.time() - t))

    print("\n   P4  does the gap separate the two classes, rank by rank?")
    print("   %4s %9s %9s %9s %9s %s"
          % ("r", "F min", "F max", "C min", "C max", "verdict"))
    for r in sorted(gaps):
        fs = [g for (_, f, g) in gaps[r] if f]
        cs = [g for (_, f, g) in gaps[r] if not f]
        if not fs or not cs:
            print("   %4d  one class only in the window; no comparison"
                  % r)
            continue
        sep = max(fs) < min(cs)
        if not sep:
            fired["K4"] += 1
        print("   %4d %9.4f %9.4f %9.4f %9.4f %s"
              % (r, min(fs), max(fs), min(cs), max(cs),
                 ("disjoint, F below C, on %d failing and %d clean "
                  "cells" % (len(fs), len(cs))) if sep
                 else "K4 OVERLAP"))

    print("\n" + "=" * 70)
    hit = ", ".join("%s=%d" % (k, v) for k, v in sorted(fired.items())
                    if v)
    print("kills fired: %s" % (hit or "none"))
    print("wall %.1f s" % (time.time() - t_all))


if __name__ == "__main__":
    main()
