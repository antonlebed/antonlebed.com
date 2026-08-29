"""explore_flatten_lattice.py -- READ h(M, J) AS A LATTICE MINIMUM.

explore_flatten_offchart.py measured h(M, J) -- the least HEIGHT of a
nonzero M-atom vector whose first J moments vanish -- by DEEPENING: ask
"is there a vector of height <= k" for k = 1, 2, 3, ... until one says
yes. explore_flatten_d2.py added the inverse ladder d_2(J) and a
cyclotomic floor, and swept M = 4..30, J = 2..12: 174 cells decided, 78
left BRACKETED. Both instruments approach h by climbing in k, and both
run out at the same corner -- small rank, huge ceiling -- because the
cost of a deepening is the sum over k of (2k+1)^rank and the widest
bracket standing, [100, 264] at M = 15, J = 12, needs k to reach 264 at
rank 3, of order 10^10 nodes.

That corner is not a compute problem. It is an INSTRUMENT problem, and
the instrument is named by restating the object:

    h(M, J) = min over nonzero v in L_{M,J} of ||v||_inf,
    L_{M,J} = (x-1)^J * Z[x] cut at degree < M,

a lattice of rank M - J spanned by x^i (x-1)^J for i = 0..M-J-1, sitting
in Z^M. h is its SHORTEST VECTOR in the sup norm. Deepening in k is a
poor way to find a lattice minimum; reduction plus a bounded enumeration
reads it directly, and the bound that makes the enumeration exhaustive
is the whole question -- a box guessed against an answer already known
proves nothing.

THE BOX, and it is free. If v is a nonzero lattice vector of sup norm
at most H then ||v||_2 <= H*sqrt(M), so enumerating the L2 BALL of that
radius sees every candidate. Any lattice vector at all supplies an H:
the first vector of a reduced basis is one, so the route needs NO
external ceiling and in particular does not borrow the product family's
-- which matters, because the product family is what this rig tests.
Fincke-Pohst over the reduced basis enumerates the ball exactly, and the
radius shrinks every time a better sup norm is found. The whole route is
exact rational arithmetic: no float appears anywhere in a bound.

(FLATTENING, HEIGHT and the PURE-PRODUCT family keep the family's
senses, restated because this rig is read alone: a vector c on M atoms
is the polynomial P(x) = sum_r c_r x^r; its moments m_j = sum_r C(r,j)
c_r are its coefficients in the (x-1) basis, so the flattening J(c) --
the least j with m_j nonzero -- IS the multiplicity of the root 1.
HEIGHT is the sup norm max_r |c_r|. A PURE PRODUCT is prod_i
(x^{d_i} - 1) over a multiset D of positive parts; it has |D| factors,
degree sum D, and its flattening is |D|. RANK here always means
M - J, the rank of L_{M,J}.)

THE QUESTION. Three halves, and the third is the one that matters.
  (a) Does the reduction-plus-enumeration route decide the 78 brackets,
      and at what cost?
  (b) What is the rank distribution of those 78 -- which the parent
      sweep does not print, and on which the whole choice of route was
      resting on one cell?
  (c) IS THE PURE-PRODUCT FAMILY EXTREMAL FOR h OFF THE CHARTED RANGE?
      The parent verified product extremality exhaustively at the 63
      cells M <= 12 and at 18 more; every cell beyond that was a
      BRACKET whose upper end was the product's own height, so the law
      has never been tested where it was not also the only evidence.

THE HAND ATTACK, worked on paper before any engine code.

FIRST, THE COST LAW, AND IT IS THE INVERSE OF THE QUOTIENT ROUTE'S. The
quotient DFS branches 2k+1 over M - J positions, so it pays
(2k+1)^rank and dies when the CEILING is large. The enumeration pays
roughly the number of lattice points in a ball of radius H*sqrt(M),
which by the Gaussian heuristic is vol(B_r(H*sqrt(M))) / det(L_{M,J}),
and det is large exactly where the deepening is expensive: at rank 3,
J = 12, the basis vectors have L2 norm sqrt(C(2J, J)) = 1644 each and
the ball of radius 264*sqrt(15) = 1022 holds of order ONE lattice point.
The two routes therefore fail at opposite ends, which is the same shape
the parent found between its own two.

SECOND, WHY THE ROUTE CANNOT SILENTLY UNDER-REPORT. Every value it
prints is attained by an exhibited integer vector, and divisibility by
(x-1)^J is checkable by J exact synthetic divisions independent of every
line of lattice code. So h <= the printed value is verifiable by hand.
The direction that CAN fail silently is the other one: an enumeration
that misses vectors returns a minimum that is too LARGE while looking
exactly like a completed exhaustive search -- the same shape as the
parent's unsound propagation bound. That is what C6 exists for, and it
is the only control here that tests the thing the others cannot see.

THIRD, THE SELF-CHECK THE RADIUS GIVES FOR FREE. The enumeration is run
with radius H*sqrt(M) for an H that is the sup norm of an EXHIBITED
lattice vector. So the minimum it returns can never exceed H. If it
does, either the ball was not enumerated or H was not a lattice
vector's height, and both are faults. This costs nothing and it fires
on the failure mode of the whole design.

FOURTH, TWO MONOTONICITIES THAT ARE FREE AND MUST HOLD. L_{M,J} sits
inside L_{M+1,J} (a vector on M atoms is a vector on M+1 atoms with a
zero), so h is NONINCREASING in M at fixed J. And L_{M,J+1} sits inside
L_{M,J}, so h is NONDECREASING in J at fixed M. Neither is a finding;
both are checkable at every one of the 252 cells and a route that
violates either is broken.

FIFTH, WHAT A FAILURE OF PRODUCT EXTREMALITY WOULD LOOK LIKE. The
product family's least height at (M, J) is a min over multisets D with
|D| >= J and sum D <= M - 1. As M grows by one the family gains
multisets and its ceiling is nonincreasing -- but it can STALL, holding
the same value across several M while the true h keeps falling, because
the products available at sum M - 1 need not include one better than
the best at sum M - 2. A failure of extremality is therefore expected
at a STALL of the family and not at a step of it, which is a mechanical
prediction rather than a hope (P3).

SIXTH, WHAT IS BORROWED AND FROM WHERE. The product table and the
interval-pinned quotient DFS are imported from
explore_flatten_offchart.py: the first supplies arm 3's ceiling, which
is the object of the extremality test and never an input to arm 1, and
the second is control C2, an independent algorithm by construction. The
d_2 ladder's eight values and A059753's fourteen are CITED tables, used
as controls (C4, C5) and never as instruments.

WHAT WAS ALREADY MEASURED BEFORE THE SLATE WAS FROZEN, stated so that
no prediction below is read as one it is not. A scratch probe ran the
route at 15 cells: h(15, 12) = 264, h(12, 9) = 42, h(12, 8) = 15,
h(10, 7) = 14, and eleven more at M = 16..30 with J = 8..12. Every one
of the fifteen took under a quarter of a second of enumeration. FOURTEEN
of them returned exactly the least-height pure product, and ONE DID NOT:
at M = 25, J = 12 the product family's least height is 28 and the route
returned 25, on a witness whose divisibility by (x-1)^12 was checked by
twelve exact synthetic divisions outside the lattice code. So K-A has
already fired once, off this rig, and the predictions below are about
the SHAPE of the failing set and not about whether it is empty.

THE SLATE, frozen before any engine code.

PREDICTIONS.
  P1. THE CHART CLOSES. All 252 cells of M = 4..30, J = 2..12 are
      decided exactly, within the node cap, and the parent's 78
      brackets go to zero. The whole sweep costs under a minute of
      enumeration -- against the 10^10 nodes a deepening needs for one
      of its cells.
  P2. THE 78 ARE A LOW-RANK OBJECT. Their rank distribution is
      concentrated below rank 8; the median rank of a bracketed cell is
      at most 6, against a median over all 252 that is larger. This is
      the measurement the parent's reading rested on one cell for.
  P3. PRODUCT EXTREMALITY FAILS AT A STALL, NEVER AT A STEP. Every cell
      where h is strictly below the product family's least height has
      the SAME product ceiling as the cell at M - 1 (the family stalled
      there), and no cell where the family's ceiling strictly improved
      at M fails. The failures are sporadic in M rather than an up-set:
      M = 25 at J = 12 fails while M = 24 and M = 30 do not.
  P4. THE FAILURES ARE A LARGE-RANK PHENOMENON. Every failing cell has
      rank >= 9. The 63-cell exhaustive chart at M <= 12 tops out at
      rank 10 and shows none, so the threshold cannot be lower than
      that chart's own reach without contradicting it.
  P5. THE d_2 BOUNDARY IS REPRODUCED. h(M, J) <= 2 exactly when
      M > d_2(J), at every J <= 8 in range -- an independent
      recomputation of a ladder that cost 858 seconds, by a route
      sharing no code and no cost law with it.
  P6. THE COST IS SET BY RANK AND NOT BY CEILING. Across the 252 cells,
      node count is increasing in rank at fixed ceiling and roughly
      FLAT in the ceiling at fixed rank -- the exact inverse of the
      deepening's law, and the reason the two routes are complementary.

KILLS, as observables rather than inferences.
  K-A. PRODUCT EXTREMALITY REFUTED OFF CHART. A cell whose h is
       STRICTLY BELOW the least height over pure products with |D| >= J
       and sum D <= M - 1. The cell, both heights, the witness vector,
       its quotient by (x-1)^J and the product's multiset all print.
  K-B. ROUTE DISAGREEMENT. Any cell where the lattice route differs
       from the quotient DFS, from full brute force over a quotient
       box, from the rank-1 closed form, from A059753's k = 1 boundary,
       or from the d_2 ladder's k = 2 boundary. The cell and both
       answers print. ANY K-B FIRING BARS READING K-A AS EVIDENCE.
  K-C. CEILING VIOLATION. An enumerated minimum STRICTLY ABOVE the sup
       norm of the exhibited vector its own radius was built from.
  K-D. THE ROUTE STALLS. A cell exceeding the node cap, leaving a
       bracket standing.
  K-E. BASIS CORRUPTION. A reduced basis whose transform from the
       original is not unimodular, or a returned witness that J exact
       synthetic divisions by (x-1) do not clear.
  K-F. MONOTONICITY VIOLATION. h increasing in M at fixed J, or
       decreasing in J at fixed M (hand attack, fourth section).

CONTROLS, run and read BEFORE any verdict, each printing how many cases
it exercised.
  C1 (POSITIVE, PARITY). The lattice route against FULL BRUTE FORCE
     over the quotient: every q with coefficients in [-Q, Q] and degree
     < M - J, taking the least sup norm of (x-1)^J q. Exhaustive only
     inside the box, so it is read as a POSITIVE control -- it can
     confirm a value and can only ever report one that is too large.
  C2 (INDEPENDENT ALGORITHM). The lattice route against the offchart
     rig's interval-pinned quotient DFS, deepened until it accepts,
     over every cell of M = 4..12 -- a route sharing no code, no
     arithmetic and no cost law with this one.
  C3 (RANK-1 CLOSED FORM). h(M, M-1) = C(M-1, floor((M-1)/2)), which
     runs the enumeration at radii up to 92378*sqrt(20) and is the only
     control here that exercises a huge ball.
  C4 (INCUMBENT, HEIGHT 1). A059753 as an externally proved table:
     h(M, J) = 1 exactly when M > d_1(J), over J = 2..7 and the whole
     M = 4..30 range.
  C5 (INCUMBENT, HEIGHT 2). The d_2 ladder as a cited table:
     h(M, J) <= 2 exactly when M > d_2(J), over J = 2..8 (P5).
  C6 (EXHAUSTIVENESS). At small cells the enumeration's full COUNT of
     lattice points strictly inside a FIXED ball is compared against a
     brute-force count over a coefficient box provably containing that
     ball -- the box being derived from the reduced basis's
     Gram-Schmidt norms, so the comparison is exhaustive on both sides.
     WHAT IS UNIQUE ABOUT IT is not that it catches a missed vector --
     every control comparing a VALUE catches one too, since a miss
     makes the route report too large -- it is that it tests the
     enumeration ITSELF rather than its output, so it says something
     where no value control reaches, which is most of the chart and all
     of the 78.
  C7 (MONOTONICITY). Both monotonicities at every one of the 252 cells
     (K-F).
  C8 (THE PARENT'S WHOLE SWEEP). Arm 4 is not only bookkeeping: at each
     of the cells it decides it holds an exact second answer, and at
     each cell it brackets it holds an INTERVAL the lattice value must
     lie in -- which is the only check that reaches the 78, where by
     construction no other control does. ADDED AFTER THE FIRST VERDICT
     RUN and recorded as such: the arm was written to recover the 78
     and its two answers were sitting there unread, which is the shape
     of a control a rig should have been born with.

THE ARMS.
  1. THE LATTICE ROUTE. Basis x^i (x-1)^J; LLL reduction in exact
     rationals; exact Gram-Schmidt; Fincke-Pohst enumeration of the L2
     ball with the radius reset from every improvement in the sup norm.
     Returns h, a witness, and a node count. Every other arm is built
     on it.
  2. THE CHART. h(M, J) exactly at M = 4..30, J = 2..12, with the node
     count and the rank per cell (P1, P6, K-D).
  3. PRODUCT EXTREMALITY OFF CHART. Arm 2 against the product family's
     least height at every cell; every strict cell printed in full
     (P3, P4, K-A).
  4. THE LEGACY SWEEP. The parent's own decision procedure rerun --
     product ceiling, A059753, the d_2 ladder, the cyclotomic floor and
     the quotient route under its node cap -- to recover WHICH 78 cells
     it left bracketed, their rank distribution, and how many the
     lattice route closes (P2).
  5. THE CONTROLS.

RESOURCE NOTE. Exact integer and rational arithmetic, no numpy, so no
BLAS arenas; the working set is a few reduced bases and never a table,
so the run sits far under the 512 MB default and is run under memwatch
anyway. Wall is dominated by ARM 4, which is the parent's procedure and
not this rig's -- the deepening it reruns is the thing being replaced,
and it costs tens of minutes where arms 1 to 3 cost under one. The run
is estimated at 25 to 35 minutes for that reason: over the ten-minute
line, and named as such, because the bookkeeping that says WHICH cells
were bracketed cannot be got any other way than by running the
instrument that bracketed them. Arms 1, 2, 3 and the controls print
BEFORE arm 4 so that a kill on the science does not wait on the
bookkeeping.

F1. EVERY CONTROL PASSES, AND WHAT C6 ADDS IS NOT WHAT IT LOOKS LIKE.
The route is sound in the direction that is cheap to check -- every
value it prints is attained by an exhibited integer vector, and K-E
confirms all 252 clear J synthetic divisions -- and the direction that
fails SILENTLY is a missed vector, which returns a minimum too LARGE
while looking like a completed search. EVERY value control catches that
where it reaches, and the reach is the point: C1 at 10 cells, C2 at 54,
C3 at 18, C8 at the 81 the parent decided -- and none of them supplies a
value at the 78, where C8 supplies only an interval. C6 is what licenses
the route there, because it tests the enumeration rather than its
output: at 6 cells the enumeration's full point count inside a fixed
ball is compared with a brute-force count over a per-coordinate box
derived from the reduced basis's own Gram-Schmidt norms, both sides
exhaustive, and the counts agree at every one. READ THE LARGEST AND NOT
THE RANGE: five of the six hold between 12 and 314 points, and the sixth
holds 17,082 (M = 11, J = 6, radius 60, box half-width 15), which is the
only one of them that exercises the enumeration at a ball with a real
population -- a control agreeing on 12 points agrees about almost
nothing. The rest: C1 (parity) 10 cells against full brute force over
the quotient box, all 10 CONFIRMING the value rather than merely
consistent with it, 0 boxes short; C2 (independent algorithm) 54 cells
at M = 4..12 against the offchart rig's interval-pinned quotient DFS
deepened until it accepts, 0 mismatches; C3 (rank-1 closed form) 18
cells, 0 mismatches, the largest being C(19, 9) = 92378, which is the
only control exercising a huge ball. C4 and C5 are the two whose COUNT
is not their strength, so both print the split: A059753's boundary is
checked at 152 cells, 93 above it confirming h = 1 and 59 below
confirming h >= 2, 0 mismatches; the d_2 ladder's at 174, 121 above
confirming h <= 2 and 53 below confirming h >= 3, 0 mismatches. Both
directions are exercised at both boundaries, which is what an undivided
count would have hidden. C7 (monotonicity) 466 comparisons, 0
violations. K-B, K-C and K-D silent, and K-E and K-F too.

F2. THE CHART CLOSES ENTIRELY, AND THE COST IS NOT WHERE THE PARENT'S
WAS (rule, exhaustive over the range; P1 holds). All 252 cells at
M = 4..30, J = 2..12 are decided exactly -- 30,158 enumeration nodes
for the WHOLE chart, the worst single cell 3,417 at M = 25, J = 12.
Against that the parent's widest bracket alone needs a deepening of
order 10^10 nodes. AND THE WALL GOES ALMOST ENTIRELY TO THE WRONG HALF,
which is measured here rather than inferred from the node counts being
small: of 128.3 s, the REDUCTION takes 127.7 and the enumeration 0.6 --
six tenths of a second to answer all 252 cells, and two minutes to
prepare the bases. The LLL here recomputes the whole Gram-Schmidt on
every swap in exact rationals, so anything wider is priced by that and
not by the object; a standard incremental reduction is what a wider
census needs first. The 78 the two height-climbing routes
left bracketed are decided along with everything else, not as a special
case: the route does not know which cells were hard.

F3. PRODUCT EXTREMALITY IS FALSE OFF THE CHART (rule, exhaustive over
the range; K-A fires three times). At 249 of the 252 cells h equals the
least height over pure products with at least J factors and degree
below M. At THREE it is strictly below:
    h(21, 12) = 39  against the product's 44   (rank 9)
    h(23, 10) =  9  against the product's 10   (rank 13)
    h(25, 12) = 25  against the product's 28   (rank 13)
Each is exhibited. The M = 25 witness is
(-2, 12, -25, 14, 18, -17, -15, 15, 6, -7, 8, -17, 20, -17, 8, -7, 6,
15, -15, -17, 18, 14, -25, 12, -2), and dividing it by (x-1) twelve
times leaves no remainder and returns
-(2, 12, 37, 78, 126, 165, 180, 165, 126, 78, 37, 12, 2). That check is
J synthetic divisions and shares nothing with the lattice code, so the
refutation stands whatever one thinks of LLL. The law is therefore a
property of the CHARTED CORNER and not of the problem: exhaustive and
true at every cell of width at most 12, and false first at width 21.

F4. P3 IS REFUTED AND P4 SURVIVES, WHICH IS THE USEFUL HALF. The frozen
mechanism said the family fails where it STALLS -- holds the same
ceiling as the cell one width down -- and two of the three do exactly
that, at (23, 10) and (25, 12). The third does not: at (21, 12) the
product family STEPPED, 45 down to 44, and the truth went to 39 anyway.
So a stall is not what selects a failing cell and the mechanism named
before the run is wrong. What survives is P4's rank floor: all three
failures sit at rank >= 9, and no cell of the exhaustive 63-cell chart
at M <= 12 fails -- that chart runs J = 1..M-1, so it reaches rank 11
and not the rank 10 P4's own parenthetical claims, which makes the
argument STRONGER than the slate stated it: ranks 9, 10 and 11 are all
exercised there with no failure, so what the phenomenon needs is not
rank alone but a WIDTH past that chart as well. AND THE FAILURES ARE
SPORADIC RATHER THAN A THRESHOLD: depth 12 carries TWO of the three, at
widths 21 and 25, and widths 22, 23, 24, 26 and 30 in that same column
are all tight -- so the failing set is neither an up-set in the width
nor a run. (SETTLED SINCE, by explore_flatten_family.py, which widens
this chart to 550 cells at M = 4..40, J = 2..20 and the failing set is
20 rather than 3 and is a DENSITY IN THE DEPTH -- 0.8% of the cells at J
<= 12 against 9.0% at J >= 13, and 1.4% against 9.0% with the 153
height-1 cells that cannot fail conditioned out. Everything above
survives as a statement about the width AT DEPTH 12, which is what it
measured; what does not survive is reading it as the failing set's
shape, because the variable carrying the signal is the depth and this
chart stopped at J = 12.)

F5. TWO OF THE THREE SHARE ONE QUOTIENT, WHICH IS THE THREAD WORTH
PULLING. The width-23 witness divides by (x-1)^10 to
+(2, 12, 37, 78, 126, 165, 180, 165, 126, 78, 37, 12, 2) and the
width-25 witness divides by (x-1)^12 to its negative -- the SAME
degree-12 palindrome, q(1) = 1020, against two different powers. The
cell the intermediate power lands on, width 24 at depth 11, is tight.
The third failure's quotient is -(2, 10, 25, 41, 48, 41, 25, 10, 2),
also palindromic and also with leading coefficient 2 up to sign. One polynomial
serving two cells is either a coincidence at two points or a family
with a rule, and this rig does not factor them. What beats the pure
products is therefore NAMED nowhere: a counterexample says the family
is not extremal and says nothing about what is.

F6. THE COST LAW IS NOT MONOTONE IN THE RANK, AND P6 IS HALF WRONG FOR
A REASON WORTH KEEPING. The frozen prediction said node count rises
with rank at fixed ceiling and is flat in the ceiling at fixed rank.
The median rises to 207 nodes at rank 10 and then FALLS, to a few dozen
past rank 19. The price is the ball's volume over the lattice's
covolume, which is set by rank AND height together -- and on this chart
the two are anti-correlated, h running to 924 at rank 1 and pinned to 1
by rank 24, because a wider lattice at fixed depth contains shorter
vectors. So the cost peaks in the MIDDLE and the route is cheap at both
ends, which is why nothing here needed the node cap. That is the exact
inverse of a deepening, whose price is the sum over k of (2k+1)^rank
and rises in both variables at once. AND THE NODE COUNT IS NOT THE
BILL: the whole enumeration is 0.6 s against the reduction's 127.7, so
every sentence about this route's cost is really a sentence about LLL,
and the shape above is the shape of something that costs nothing.

F7. THE 78 ARE NOT A LOW-RANK OBJECT, AND P2 IS REFUTED. The parent's
sweep is reproduced exactly -- 174 decided, 78 bracketed -- and its rank
distribution, which it never printed, runs from rank 3 to rank 21 with
no rank holding more than 6 cells and a MEDIAN of 11, against a median
of 12 over all 252. The frozen prediction said the 78 concentrate below
rank 8 with a median of at most 6. They do not: they are spread across
essentially the whole rank range, near-uniformly. What that refutes is
not only a number but the reading the parent's own record rested on --
it named the corner "low-rank, huge-ceiling" from the WIDEST bracket
alone, [100, 264] at rank 3, and said in the same breath that how much
of the 78 was that corner was unmeasured. It was two cells of the 78.
The brackets are wide at low rank and narrow at high rank -- rank 3
spans widths 32 to 164, rank 20 spans 1 to 2 -- so the widest bracket
is at low rank BY CONSTRUCTION, and reading the set's shape off it
picks the one cell guaranteed to be unrepresentative.

F8. C8, AND IT IS THE STRONGEST CONTROL HERE BECAUSE IT REACHES THE 78.
The parent's sweep is a second answer at every cell it touched: an
exact value where it decided, an INTERVAL where it did not. Against the
81 informative decided values the lattice route matches all 81, 0
mismatches. Against the 78 brackets every lattice value falls INSIDE
its bracket, 0 outside -- which is the only check that reaches the
cells where, by construction, no other control does, since those are
exactly the cells nothing else could decide. And the three K-A cells
are among them: h(21, 12) = 39 sits inside the parent's [4, 44] and
h(25, 12) = 25 inside its own bracket, so the refutation is not the
route disagreeing with the older instruments anywhere -- it is the
route landing where they said it must, strictly below the product end.

RUN RECORD (final run: wall 1161.7 s, peak working set 22.4 MB, peak
commit 17.3 MB under memwatch's 512 MB default -- the exact rational
arithmetic holds a few reduced bases and never a table, so the memory
line is the one thing here that was never in question). ARM 4 IS
1020.0 s OF IT and the whole of arms 1 to 3 with every control is
141.7: the instrument being replaced costs seven times the instrument,
and it is doing less. The wall is UNDER the 25-to-35-minute estimate,
which is recorded because the estimate was made of the right half --
arm 4 was correctly named as the cost, and it dwarfed the chart it was
expected to.

FOUR runs. The FIRST was killed by hand at twelve minutes with nothing
printed since its opening line, under a runaway suspicion, and WHAT IT
WAS DOING IS NOT KNOWN -- which is worth recording where a diagnosis
would not be. Arm 2 completes in about two minutes here, so twelve
minutes inside it was not normal and the suspicion was not obviously
wrong; but the rig had no progress print in a 252-cell loop, so a
healthy run and a stuck one were indistinguishable from outside and the
kill decided nothing. The per-row print is now in both sweeps, and it is
there so the question cannot arise again rather than because the answer
was found. Nothing below rests on that run.

The SECOND ran to the end of the controls and was killed there
deliberately rather than for a fault, once two control DEFECTS it
exposed were understood, so that its twenty minutes of arm 4 would not
be paid twice: C2's deepening capped its height at 400 and one cell in
its range has h = 462, so a control comparing a value against None
reported a mismatch that was the cap and not the route; and C1 counted
any difference as a kill, when only brute-force-BELOW-the-route is one
-- brute-force ABOVE it is the box falling short, which is a scope fact
about the control and not a fault in what it checks. The THIRD carries
both fixes and C8, added in the same pass because arm 4 had been holding
two answers per cell all along and nothing was reading them.

The FOURTH is this record's, and it exists because the audit found two
statements that were not measurements: the control counts for C4 and C5
were reported undivided, where the split by side of the boundary is the
strength and the count is not; and the claim that the wall goes to the
REDUCTION was an inference from the node counts being small. Both are
now printed, and the second turned out to be the sharper fact in the
file -- 127.7 s against 0.6. No prediction and no kill was touched at
any point, and every value in F2 through F8 printed identically in the
third run and the fourth, which is the only reproduction claimed here.
"""
import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time
from fractions import Fraction as F
from math import comb, floor as mfloor, isqrt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_flatten_offchart import NodeCap, Products, feasible

A059753 = [1, 3, 6, 11, 15, 22, 30, 41, 48, 61, 69, 93, 112, 120]
D2 = [1, 2, 4, 7, 11, 16, 22, 26]

SWEEP_M = 30
SWEEP_J = 12
PRODUCT_BUDGET = 44
NODE_CAP = 20000000
LEGACY_CAP = 4000000


# ------------------------------------------------ polynomial helpers

def pow_xm1(J):
    """Coefficients of (x-1)^J, low degree first."""
    return [comb(J, m) * (-1) ** (J - m) for m in range(J + 1)]


def divide_xm1(p):
    """(quotient, remainder) of p by (x-1), low degree first. Synthetic
    division written out rather than called from anywhere else: this is
    the check on the lattice code and must not share with it."""
    n = len(p) - 1
    if n < 0:
        return [], 0
    q = [0] * n
    acc = 0
    for t in range(n):
        acc += p[t]
        q[t] = -acc
    rem = p[n] - (q[n - 1] if n else 0)  # = p(1)
    return q, rem


def clears(p, J):
    """Does J exact synthetic divisions by (x-1) clear p? (K-E)"""
    q = list(p)
    for _ in range(J):
        q, rem = divide_xm1(q)
        if rem != 0:
            return False, None
    return True, q


def basis(M, J):
    """x^i (x-1)^J for i = 0..M-J-1, as vectors of Z^M."""
    e = pow_xm1(J)
    r = M - J
    return [[0] * i + e + [0] * (r - 1 - i) for i in range(r)]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


# --------------------------------------------- arm 1: the lattice route

def gram_schmidt(B):
    """Exact GSO: mu[i][j] and A[i] = ||b*_i||^2, both rational."""
    n = len(B)
    mu = [[F(0)] * n for _ in range(n)]
    star = []
    A = []
    for i in range(n):
        v = [F(x) for x in B[i]]
        for j in range(i):
            m = sum(F(B[i][t]) * star[j][t] for t in range(len(v))) / A[j]
            mu[i][j] = m
            if m:
                v = [v[t] - m * star[j][t] for t in range(len(v))]
        star.append(v)
        A.append(sum(x * x for x in v))
    return mu, A


def lll(B, delta=F(99, 100)):
    """LLL in exact rationals. Returns the reduced basis and the integer
    transform T with reduced = T * original, so unimodularity is
    checkable (C5, K-E). Size reduction updates mu in place; a swap
    recomputes the GSO, which is affordable at these ranks."""
    B = [list(b) for b in B]
    n = len(B)
    T = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    mu, A = gram_schmidt(B)
    k = 1
    while k < n:
        for j in range(k - 1, -1, -1):
            q = mu[k][j]
            r = mfloor(q + F(1, 2))
            if r:
                B[k] = [B[k][t] - r * B[j][t] for t in range(len(B[k]))]
                T[k] = [T[k][t] - r * T[j][t] for t in range(n)]
                for t in range(j):
                    mu[k][t] -= r * mu[j][t]
                mu[k][j] -= r
        if A[k] >= (delta - mu[k][k - 1] ** 2) * A[k - 1]:
            k += 1
        else:
            B[k], B[k - 1] = B[k - 1], B[k]
            T[k], T[k - 1] = T[k - 1], T[k]
            mu, A = gram_schmidt(B)
            k = max(k - 1, 1)
    return B, T


def det_pm1(T):
    """Is the integer matrix T unimodular? Fraction-exact Gaussian
    elimination -- the ranks here make anything cleverer pointless."""
    n = len(T)
    Mx = [[F(x) for x in row] for row in T]
    det = F(1)
    for c in range(n):
        p = None
        for r in range(c, n):
            if Mx[r][c]:
                p = r
                break
        if p is None:
            return False
        if p != c:
            Mx[c], Mx[p] = Mx[p], Mx[c]
            det = -det
        det *= Mx[c][c]
        inv = Mx[c][c]
        for r in range(c + 1, n):
            if Mx[r][c]:
                f = Mx[r][c] / inv
                Mx[r] = [Mx[r][t] - f * Mx[c][t] for t in range(n)]
    return det == 1 or det == -1


def frac_sqrt_up(w):
    """A rational UPPER bound on sqrt(w) for w >= 0. Exact: no float
    appears in any enumeration bound."""
    if w <= 0:
        return F(0)
    num, den = w.numerator, w.denominator
    return F(isqrt(num * den) + 1, den)


def enumerate_ball(B, mu, A, M, R2, collect=None):
    """Fincke-Pohst over the lattice spanned by B, exact. Returns the
    least sup norm of a nonzero vector inside the L2 ball of radius
    sqrt(R2), a witness, and the node count. R2 SHRINKS whenever a
    better sup norm lands: a vector can only help if its sup norm is
    below the best so far, so the ball may be cut to that. Pass a list
    as `collect` to record every vector found instead (C6)."""
    n = len(B)
    x = [0] * n
    best = [None, None]
    nodes = [0]
    rad = [R2]

    def rec(i, partial):
        nodes[0] += 1
        if nodes[0] > NODE_CAP:
            raise NodeCap
        if i < 0:
            if not any(x):
                return
            v = [sum(x[j] * B[j][t] for j in range(n)) for t in range(M)]
            h = max(abs(c) for c in v)
            if collect is not None:
                collect.append(v)
                return
            if best[0] is None or h < best[0]:
                best[0], best[1] = h, v
                rad[0] = F((h - 1) ** 2 * M)
            return
        c = -sum(mu[j][i] * x[j] for j in range(i + 1, n))
        rem = rad[0] - partial
        if rem < 0:
            return
        s = frac_sqrt_up(rem / A[i])
        lo, hi = mfloor(c - s), -mfloor(-(c + s))
        # nearest-first, so a good sup norm lands early and cuts rad
        mid = mfloor(c + F(1, 2))
        order = sorted(range(lo, hi + 1), key=lambda t: abs(t - mid))
        for xi in order:
            d = (F(xi) - c) ** 2 * A[i]
            if d <= rad[0] - partial:
                x[i] = xi
                rec(i - 1, partial + d)
        x[i] = 0

    rec(n - 1, F(0))
    return best[0], best[1], nodes[0]


TIME = {"lll": 0.0, "enum": 0.0}


def lattice_h(M, J):
    """h(M, J) exactly, with a witness and the node count. The starting
    radius comes from the reduced basis's OWN first vector -- no
    external ceiling enters, which is what keeps arm 1 independent of
    the product family it is used to test."""
    t0 = time.time()
    B, T = lll(basis(M, J))
    if not det_pm1(T):
        raise ValueError("K-E basis corruption at M=%d J=%d" % (M, J))
    mu, A = gram_schmidt(B)
    t1 = time.time()
    H = min(max(abs(c) for c in b) for b in B)
    h, v, nodes = enumerate_ball(B, mu, A, M, F(H * H * M))
    # WHICH HALF the wall goes to is a claim, so it is measured here
    # rather than inferred from the node counts being small.
    TIME["lll"] += t1 - t0
    TIME["enum"] += time.time() - t1
    if h is None or h > H:
        raise ValueError("K-C ceiling violation at M=%d J=%d: %s > %d"
                         % (M, J, h, H))
    ok, _ = clears(v, J)
    if not ok:
        raise ValueError("K-E witness not divisible at M=%d J=%d" % (M, J))
    return h, v, nodes


# ------------------------------------------------------- the controls

def brute_quotient(M, J, Q):
    """Least sup norm of (x-1)^J q over every q of degree < M-J with
    coefficients in [-Q, Q]. Exhaustive inside the box only (C1)."""
    e = pow_xm1(J)
    r = M - J
    best = None
    q = [0] * r
    def rec(i):
        nonlocal best
        if i == r:
            if not any(q):
                return
            v = [0] * M
            for a in range(r):
                if q[a]:
                    for b in range(J + 1):
                        v[a + b] += q[a] * e[b]
            h = max(abs(c) for c in v)
            if best is None or h < best:
                best = h
            return
        for t in range(-Q, Q + 1):
            q[i] = t
            rec(i + 1)
        q[i] = 0
    rec(0)
    return best


def quotient_h(M, J, cap):
    """h by DEEPENING with the offchart rig's interval-pinned DFS (C2)."""
    k = 1
    while k <= 1000:
        if feasible(M, J, k, cap):
            return k
        k += 1
    return None


def main():
    t_all = time.time()
    fired = dict(("K-" + c, 0) for c in "ABCDEF")

    print("=" * 70)
    print("explore_flatten_lattice.py -- h(M, J) as a lattice minimum")
    print("=" * 70)

    # ------------------------------------------------ arm 2: the chart
    print("\n[arm 2] the chart -- h(M, J) exactly, M = 4..%d, J = 2..%d"
          % (SWEEP_M, SWEEP_J))
    t = time.time()
    H = {}
    NODES = {}
    stalled = []
    for M in range(4, SWEEP_M + 1):
        t_row = time.time()
        for J in range(2, min(SWEEP_J, M - 1) + 1):
            try:
                h, v, nodes = lattice_h(M, J)
            except NodeCap:
                stalled.append((M, J))
                fired["K-D"] += 1
                print("   K-D stalled at M=%d J=%d rank=%d" % (M, J, M - J))
                continue
            H[(M, J)] = (h, v)
            NODES[(M, J)] = nodes
        # a sweep that prints nothing until it ends cannot be told from a
        # hang, and this one was not: the reduction, not the enumeration,
        # is what costs at high rank.
        print("   M = %2d done, %.1f s (%.1f s in)"
              % (M, time.time() - t_row, time.time() - t))
    t_chart = time.time() - t
    print("   %d cells decided, %d stalled, %.1f s, %d nodes total"
          % (len(H), len(stalled), t_chart, sum(NODES.values())))
    print("   worst cell %s at %d nodes"
          % (max(NODES, key=lambda c: NODES[c]), max(NODES.values())))
    print("   of which reduction %.1f s and enumeration %.1f s"
          % (TIME["lll"], TIME["enum"]))

    print("\n   h(M, J), rows M, columns J = 2..%d" % SWEEP_J)
    print("      M |" + "".join("%7d" % J for J in range(2, SWEEP_J + 1)))
    for M in range(4, SWEEP_M + 1):
        row = "".join("%7s" % (H[(M, J)][0] if (M, J) in H else "")
                      for J in range(2, SWEEP_J + 1))
        print("   %4d |%s" % (M, row))

    # ------------------------------------------------ C7: monotonicity
    checks = 0
    for (M, J), (h, _) in sorted(H.items()):
        if (M + 1, J) in H:
            checks += 1
            if H[(M + 1, J)][0] > h:
                fired["K-F"] += 1
                print("   K-F h rises in M at M=%d J=%d" % (M, J))
        if (M, J + 1) in H:
            checks += 1
            if H[(M, J + 1)][0] < h:
                fired["K-F"] += 1
                print("   K-F h falls in J at M=%d J=%d" % (M, J))
    print("\n[C7] monotonicity: %d comparisons, %d violations"
          % (checks, fired["K-F"]))

    # --------------------------------- arm 3: product extremality
    print("\n[arm 3] product extremality off chart")
    prods = Products(PRODUCT_BUDGET)
    tight = loose = 0
    fails = []
    for (M, J), (h, v) in sorted(H.items()):
        ceil_h, wit = prods.bound(M, J)
        if ceil_h is None:
            continue
        if h == ceil_h:
            tight += 1
        elif h < ceil_h:
            loose += 1
            fired["K-A"] += 1
            fails.append((M, J, h, ceil_h, v, wit))
        else:
            fired["K-B"] += 1
            print("   K-B h ABOVE the product ceiling at M=%d J=%d: %d > %d"
                  % (M, J, h, ceil_h))
    print("   %d cells with a product bound: %d TIGHT, %d STRICTLY BELOW"
          % (tight + loose, tight, loose))
    for (M, J, h, ceil_h, v, wit) in fails:
        prev = prods.bound(M - 1, J)[0]
        ok, q = clears(v, J)
        print("   K-A M=%2d J=%2d rank=%2d  h=%d < product %d "
              "(product at M-1 = %s, %s)"
              % (M, J, M - J, h, ceil_h, prev,
                 "STALL" if prev == ceil_h else "STEP"))
        print("        product multiset %s" % (wit,))
        print("        witness  %s" % (v,))
        print("        quotient %s  (cleared by %d divisions: %s)"
              % (q, J, ok))

    # ------------------------------------------------------ controls
    print("\n[C1] parity against full brute force over the quotient box")
    # READ THE DIRECTIONS SEPARATELY. The box is not the whole lattice, so
    # brute ABOVE the route is the box falling short and is not a fault;
    # brute BELOW it is the route having missed a vector, which is the one
    # failure this route can have and is a kill. Only the equalities are
    # the control's strength, and they are counted on their own.
    n1 = tight1 = short1 = 0
    for (M, J, Q) in [(6, 2, 3), (7, 3, 4), (8, 4, 5), (8, 5, 6),
                      (9, 6, 8), (10, 7, 15), (9, 4, 4), (10, 5, 6),
                      (11, 8, 20), (12, 9, 45)]:
        b = brute_quotient(M, J, Q)
        n1 += 1
        if b == H[(M, J)][0]:
            tight1 += 1
        elif b > H[(M, J)][0]:
            short1 += 1
            print("   box short at M=%d J=%d: brute %s route %s"
                  % (M, J, b, H[(M, J)][0]))
        else:
            fired["K-B"] += 1
            print("   K-B M=%d J=%d brute %s BELOW route %s"
                  % (M, J, b, H[(M, J)][0]))
    print("   %d cells: %d confirm the value, %d boxes short, %d kills"
          % (n1, tight1, short1, fired["K-B"]))

    print("\n[C2] independent algorithm: the quotient DFS, deepened")
    n2 = mism2 = 0
    for M in range(4, 13):
        for J in range(2, M):
            if (M, J) not in H:
                continue
            k = quotient_h(M, J, 200000000)
            n2 += 1
            if k != H[(M, J)][0]:
                mism2 += 1
                fired["K-B"] += 1
                print("   K-B M=%d J=%d quotient %s lattice %s"
                      % (M, J, k, H[(M, J)][0]))
    print("   %d cells, %d mismatches" % (n2, mism2))

    print("\n[C3] the rank-1 closed form h(M, M-1) = C(M-1, (M-1)//2)")
    n3 = mism3 = 0
    for M in range(3, 21):
        h, v, nodes = lattice_h(M, M - 1)
        want = comb(M - 1, (M - 1) // 2)
        n3 += 1
        if h != want:
            mism3 += 1
            fired["K-B"] += 1
            print("   K-B M=%d rank 1: got %d want %d" % (M, h, want))
    print("   %d cells, %d mismatches (largest %d)"
          % (n3, mism3, comb(19, 9)))

    print("\n[C4] A059753 as a cited height-1 boundary")
    # THE COUNT IS NOT THE STRENGTH. Split the cells by which side of
    # the cited boundary they sit on: above it the check is "h is
    # exactly 1" and below it "h is at least 2", and a route wrong in
    # one direction need not be wrong in the other.
    n4 = mism4 = above4 = below4 = 0
    for J in range(2, 8):
        d1 = A059753[J - 1]
        for M in range(4, SWEEP_M + 1):
            if (M, J) not in H:
                continue
            n4 += 1
            got = H[(M, J)][0] == 1
            want = M > d1
            if want:
                above4 += 1
            else:
                below4 += 1
            if got != want:
                mism4 += 1
                fired["K-B"] += 1
                print("   K-B M=%d J=%d h=%d but d_1(%d)=%d"
                      % (M, J, H[(M, J)][0], J, d1))
    print("   %d cells (%d above the boundary confirming h = 1, %d below "
          "confirming h >= 2), %d mismatches"
          % (n4, above4, below4, mism4))

    print("\n[C5] the d_2 ladder as a cited height-2 boundary")
    n5 = mism5 = above5 = below5 = 0
    for J in range(2, 9):
        d2 = D2[J - 1]
        for M in range(4, SWEEP_M + 1):
            if (M, J) not in H:
                continue
            n5 += 1
            got = H[(M, J)][0] <= 2
            want = M > d2
            if want:
                above5 += 1
            else:
                below5 += 1
            if got != want:
                mism5 += 1
                fired["K-B"] += 1
                print("   K-B M=%d J=%d h=%d but d_2(%d)=%d"
                      % (M, J, H[(M, J)][0], J, d2))
    print("   %d cells (%d above the boundary confirming h <= 2, %d below "
          "confirming h >= 3), %d mismatches"
          % (n5, above5, below5, mism5))

    print("\n[C6] exhaustiveness: the ball's point count against a box")
    n6 = mism6 = 0
    for (M, J, rad) in [(8, 5, 40), (9, 6, 60), (10, 7, 90),
                        (12, 9, 200), (11, 6, 60), (13, 10, 300)]:
        B, T = lll(basis(M, J))
        mu, A = gram_schmidt(B)
        R2 = F(rad * rad)
        got = []
        enumerate_ball(B, mu, A, M, R2, collect=got)
        # THE BOX, and it is a bound rather than a guess. The coefficient
        # of b*_i in v = sum x_j b_j is x_i + sum_{j>i} mu[j][i] x_j, and
        # its modulus is at most R/||b*_i||, so descending from the top
        # coordinate gives |x_i| <= R/||b*_i|| + sum_{j>i} |mu[j][i]|*W_j
        # with W the bounds already fixed above i. Nothing here consults
        # the enumeration.
        n = len(B)
        W = [0] * n
        for i in range(n - 1, -1, -1):
            b = frac_sqrt_up(R2 / A[i])
            b += sum(abs(mu[j][i]) * W[j] for j in range(i + 1, n))
            W[i] = mfloor(b)
        cnt = 0
        x = [0] * n
        def rec(i):
            nonlocal cnt
            if i == n:
                if not any(x):
                    return
                v = [sum(x[j] * B[j][t] for j in range(n)) for t in range(M)]
                if sum(c * c for c in v) <= R2:
                    cnt += 1
                return
            for t in range(-W[i], W[i] + 1):
                x[i] = t
                rec(i + 1)
            x[i] = 0
        rec(0)
        wide = max(W)
        n6 += 1
        if cnt != len(got):
            mism6 += 1
            fired["K-B"] += 1
            print("   K-B M=%d J=%d r=%d: ball %d, box %d"
                  % (M, J, rad, len(got), cnt))
        else:
            print("   M=%2d J=%2d radius %3d: %5d points, box half-width "
                  "%d, agree" % (M, J, rad, cnt, wide))
    print("   %d cells, %d mismatches" % (n6, mism6))

    # ---------------------------------------------- P6: the cost law
    print("\n[P6] cost by rank (median nodes, and the ceiling range)")
    by_rank = {}
    for (M, J), nodes in NODES.items():
        by_rank.setdefault(M - J, []).append((nodes, H[(M, J)][0]))
    for r in sorted(by_rank):
        rows = sorted(by_rank[r])
        med = rows[len(rows) // 2][0]
        hs = [h for _, h in rows]
        print("   rank %2d: %2d cells, median %6d nodes, max %7d, "
              "h in [%d, %d]"
              % (r, len(rows), med, max(x for x, _ in rows),
                 min(hs), max(hs)))

    print("\nKILLS after arms 1-3 and the controls: %s" % fired)
    print("wall so far %.1f s" % (time.time() - t_all))

    # ------------------------------------------- arm 4: legacy sweep
    print("\n[arm 4] the parent's own sweep, rerun to recover the 78")
    t = time.time()
    from explore_flatten_d2 import cyclotomic_floor
    floor = dict(((k, J), cyclotomic_floor(J, k))
                 for k in range(1, 10) for J in range(1, 16))
    d2map = dict((J + 1, D2[J]) for J in range(len(D2)))
    decided = 0
    brackets = []
    legacy = {}
    for M in range(4, SWEEP_M + 1):
        for J in range(2, min(SWEEP_J, M - 1) + 1):
            ceil_h, _ = prods.bound(M, J)
            if ceil_h is None:
                continue
            if J <= len(A059753) and M > A059753[J - 1]:
                ceil_h = min(ceil_h, 1)
            if J in d2map and M > d2map[J]:
                ceil_h = min(ceil_h, 2)
            if ceil_h == 1:
                decided += 1
                continue
            lo = 1
            for k in range(1, ceil_h):
                w = None
                if k == 1 and J <= len(A059753) and M <= A059753[J - 1]:
                    w = 1
                elif k == 2 and J in d2map and M <= d2map[J]:
                    w = 1
                elif M <= floor.get((k, J), 0):
                    w = 1
                else:
                    try:
                        if feasible(M, J, k, LEGACY_CAP):
                            ceil_h = k
                            break
                        w = 1
                    except NodeCap:
                        pass
                if w is None:
                    break
                lo = k + 1
            if lo >= ceil_h:
                decided += 1
                legacy[(M, J)] = ceil_h
            else:
                brackets.append((M, J, M - J, lo, ceil_h))
        print("   M = %2d done, %.1f s in" % (M, time.time() - t))
    print("   %d decided, %d bracketed, %.1f s"
          % (decided, len(brackets), time.time() - t))
    dist = {}
    for (M, J, r, lo, hi) in brackets:
        dist.setdefault(r, []).append(hi - lo)
    ranks = sorted(r for (_, _, r, _, _) in brackets)
    allranks = sorted(M - J for (M, J) in H)
    print("   RANK DISTRIBUTION of the bracketed cells "
          "(median %d, against %d over all cells):"
          % (ranks[len(ranks) // 2] if ranks else -1,
             allranks[len(allranks) // 2]))
    for r in sorted(dist):
        print("      rank %2d: %2d cells, widths %d..%d"
              % (r, len(dist[r]), min(dist[r]), max(dist[r])))
    closed = sum(1 for (M, J, _, _, _) in brackets if (M, J) in H)
    print("   of the %d bracketed, the lattice route closes %d"
          % (len(brackets), closed))

    # C8, and it is free: the parent's whole sweep is a second answer at
    # every cell it reached -- an exact value where it decided, an
    # interval where it did not -- so both halves check the route, and
    # the interval half checks it at exactly the cells where no other
    # control reaches.
    agree = out = 0
    for (M, J), val in sorted(legacy.items()):
        if (M, J) not in H:
            continue
        if H[(M, J)][0] == val:
            agree += 1
        else:
            out += 1
            fired["K-B"] += 1
            print("   K-B M=%d J=%d legacy decided %d, lattice %d"
                  % (M, J, val, H[(M, J)][0]))
    inside = outside = 0
    for (M, J, r, lo, hi) in brackets:
        if (M, J) not in H:
            continue
        if lo <= H[(M, J)][0] <= hi:
            inside += 1
        else:
            outside += 1
            fired["K-B"] += 1
            print("   K-B M=%d J=%d lattice %d outside the bracket [%d, %d]"
                  % (M, J, H[(M, J)][0], lo, hi))
    print("   [C8] the parent's sweep as a second answer: %d decided "
          "values matched, %d not; %d lattice values inside their "
          "bracket, %d outside" % (agree, out, inside, outside))
    print("   every bracketed cell, with what the lattice route says:")
    for (M, J, r, lo, hi) in sorted(brackets, key=lambda z: (z[2], -z[4])):
        h = H[(M, J)][0] if (M, J) in H else None
        print("      M=%2d J=%2d rank=%2d  [%3d, %6d]  ->  h = %s"
              % (M, J, r, lo, hi, h))

    print("\nKILLS: %s" % fired)
    print("wall %.1f s" % (time.time() - t_all))


if __name__ == "__main__":
    main()
