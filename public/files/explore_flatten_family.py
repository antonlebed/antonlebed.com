"""explore_flatten_family.py -- WHAT FAMILY DO THE MINIMISERS LIVE IN?

explore_flatten_lattice.py read h(M, J) -- the least HEIGHT of a nonzero
M-atom vector whose first J moments vanish -- as the sup-norm shortest
vector of the rank-(M - J) lattice L_{M,J} = (x-1)^J Z[x] cut at degree
< M, and closed all 252 cells of M = 4..30, J = 2..12 by LLL plus a
Fincke-Pohst enumeration of the L2 ball of radius H*sqrt(M). It REFUTED
the pure-product law. At 249 cells h is the least height over PURE
PRODUCTS prod_i (x^{d_i} - 1) with at least J factors and degree below
M; at THREE it is strictly below one: h(21, 12) = 39 against 44,
h(23, 10) = 9 against 10, h(25, 12) = 25 against 28.

A counterexample says the family is not extremal and says nothing about
what is. The parent's close factored the three witnesses and every one
turned out to be a pure product times ONE fixed quartic:

    A = 2 + 4x + 5x^2 + 4x^3 + 2x^4
    h(21, 12) = 39 at (x-1)^9 (x^2-1)^2 (x^3-1) A
    h(23, 10) =  9 at (x-1)^6 (x^2-1)^2 (x^3-1) (x^5-1) A
    h(25, 12) = 25 at (x-1)^8 (x^2-1)^2 (x^3-1) (x^5-1) A

THE QUESTION. Is A a member of a family, or the only one -- and is
there a law the minimisers obey that the pure-product law was a special
case of?

(FLATTENING, HEIGHT and PURE PRODUCT keep their earlier senses,
restated because this rig is read alone: a vector c on M atoms is the
polynomial P(x) = sum_r c_r x^r; its moments m_j = sum_r C(r,j) c_r are
its coefficients in the (x-1) basis, so the flattening -- the least j
with m_j nonzero -- IS the multiplicity of the root 1. HEIGHT is the sup
norm max_r |c_r|. A PURE PRODUCT is prod_i (x^{d_i} - 1) over a multiset
D of positive parts; it has |D| factors, degree sum D, and flattening
|D|. RANK is always M - J. A CYCLOTOMIC POLYNOMIAL Phi_d is the minimal
polynomial of a primitive d-th root of unity, and x^d - 1 = prod_{e | d}
Phi_e, so every pure product is a product of cyclotomics -- the converse
is false, Phi_3 = 1 + x + x^2 being a product of cyclotomics and not a
pure product.)

THE HAND ATTACK, worked on paper before any engine code.

FIRST, WHAT A IS, AND IT NAMES THE FAMILY. A is reciprocal with leading
coefficient 2, so in y = x + 1/x it is A/x^2 = 2(y^2 - 2) + 4y + 5 =
2y^2 + 4y + 1, whose roots are y = -1 +- sqrt(2)/2, both REAL and both
strictly inside (-2, 2). The map y = 2 cos theta carries (-2, 2) onto
the unit circle, so ALL FOUR ROOTS OF A LIE ON |z| = 1. None is a root
of unity: a root of unity is an algebraic integer and its minimal
polynomial is monic, while A is irreducible over Q with leading
coefficient 2, so no root of A is an algebraic integer at all.

That is the family. Integer polynomials with all roots on the unit
circle are closed under multiplication; their MONIC members are exactly
the products of cyclotomics (Kronecker), and pure products are a
sub-family of those. A is a NON-MONIC member. So the refuted
pure-product law and its three counterexamples are both inside one
class, and the candidate replacement is the UNIT-CIRCLE LAW: the
minimiser has all its roots on the unit circle. This rig's headline is
whether that survives where the pure-product law did not.

SECOND, AND IT IS THE TRAP THIS LEG WAS WARNED ABOUT. PALINDROMICITY IS
NOT EVIDENCE: the lattice is closed under reversal, since
reverse((x-1)^J) = (-1)^J (x-1)^J, so a minimiser unique up to sign is
FORCED to be palindromic or anti-palindromic and reading that as a
family signal is numerology. The unit-circle law is not that. Being
reciprocal is necessary for all roots to lie on the circle and is the
part the symmetry gives away for free; having all roots ON the circle is
the part it does not -- x^2 - 3x + 1 is reciprocal with both roots real
and off the circle. The content of the law is exactly the residue after
the forced symmetry is subtracted, which is why the test below is a root
location test and never a coefficient symmetry test.

THIRD, THE TESTS ARE EXACT AND EACH IS FORCED. (a) THE RESIDUAL. Divide
out every cyclotomic factor of a witness by exact trial division by
Phi_d; the cyclotomics being distinct irreducibles, the order does not
matter and the remaining RESIDUAL is well defined up to sign. Residual 1
means the witness is a product of cyclotomics. THE INDEX RANGE IS THE
TRAP HERE and it bit a scratch probe: Phi_d has degree phi(d), which is
far below d, so bounding the trial index by the degree misses Phi_5 in a
quartic -- d must run while phi(d) <= deg, which for degree 40 reaches
d = 150. (b) THE PURE-PRODUCT TEST on a multiset S of cyclotomic
indices is deterministic and needs no search: divisors(d) has maximum d,
so max S must be a part, and removing divisors(max S) either succeeds or
the multiset is not a pure product. (c) THE UNIT-CIRCLE TEST. A residual
R with all roots on |z| = 1 has a root multiset closed under conjugation
(real coefficients) and hence under z -> 1/z, so R is +- reciprocal; if
its degree were odd, reciprocity would force R(-1) = 0 by pairing i with
n - i, and Phi_2 has already been divided out, so a cyclotomic-free
residual is reciprocal of EVEN degree or it fails. Then R/x^m = r_m +
sum_{k>=1} r_{m+k} t_k(y) with t_0 = 2, t_1 = y, t_{k+1} = y t_k -
t_{k-1}, giving an integer Q of degree m, and all roots of R are on the
circle exactly when all roots of Q are real and in [-2, 2]. That is a
Sturm count on the squarefree part of Q against its degree -- exact over
Q, no float in any decision. The test divides out (x - 1) and (x + 1)
FIRST, whose roots are on the circle and whose presence is what would
otherwise make an odd degree possible, so the test is correct on any
integer polynomial and not only on a cyclotomic-free residual -- which
is what lets C6 run it against Phi_1 and Phi_2 as known positives.

FOURTH, WHAT THE WIDENING COSTS, AND THE BILL HAS MOVED. The parent's
chart spent 127.7 of its 128.3 seconds in LLL because that LLL
recomputes the whole Gram-Schmidt in exact rationals on every swap. The
standard incremental update makes the swap O(n) and is the first arm
here. That moves the cost to the ENUMERATION, whose price is the ball's
volume over the lattice's covolume: the ball has radius H*sqrt(M) with H
a height, so the price rises where h is SMALL and the rank is LARGE --
the sup-norm ball and the L2 ball diverge by sqrt(M) and the L2 ball at
small height swallows a wide lattice. So the widening is cheap DOWNWARD
in depth, where h grows and the rank shrinks, and expensive rightward at
fixed shallow depth. This is the third distinct cost law these
rigs have met and it is the enumeration's own, not LLL's.

FIFTH, THE MINIMISER SET IS NOT WHAT THE FIRST PASS RETURNS. The
enumeration shrinks its radius to (h-1)*sqrt(M) the instant it improves,
so it never sees a second vector of the winning sup norm: every
statement about a witness is a statement about ONE minimiser and not
about the cell. A second pass at the FIXED radius h*sqrt(M) collects
them all -- and by the fourth section that pass is exactly the expensive
one, so it will close where h is large and cap where h is small. A
residual law read off single witnesses is a law about a choice until
that pass says the choice did not matter.

WHAT WAS ALREADY MEASURED BEFORE THE SLATE WAS FROZEN, stated so that no
prediction below is read as one it is not. Four scratch probes ran:
  (i) the incremental reduction over the parent's 252 cells against the
      parent's own, bases IDENTICAL at every cell and 74 times faster
      (128.2 s to 1.7 s), the carried Gram-Schmidt equal to a fresh one
      at every cell;
  (ii) the residual harvest over the parent's 252 witnesses: 249 have
      residual 1 and the three K-A cells have residual exactly A, so on
      the OLD chart A is the only non-cyclotomic multiplier there is;
  (iii) the cost curve, which is what fixed the range below: M = 50 at
      J = 12 already costs 15.7 s of enumeration while M = 40 at J = 20
      costs 0.2 s;
  (iv) the count pass at six cells, which returned 2 minimisers at five
      of them and 8 at (24, 11).
So question (2) of this leg is answered ON THE OLD CHART and the
predictions below are about the WIDENED one.

THE SLATE, frozen before any engine code.

PREDICTIONS.
  P1. THE WIDE CHART CLOSES. All 550 cells of M = 4..40,
      J = 2..min(20, M-1) are decided exactly within the node cap, and
      the bill has moved: the enumeration costs MORE than the reduction
      over the whole sweep, reversing the parent's 127.7-to-0.6.
  P2. THE UNIT-CIRCLE LAW HOLDS EVERYWHERE. Every exhibited minimiser
      on the wide chart, after its monomial factor is removed, has all
      roots on the unit circle -- residual 1, or a residual the exact
      test passes.
  P3. A IS NOT ALONE. On the widened range at least one residual appears
      that is neither 1 nor A. The old chart's three sightings all sit
      in its two deepest rows, which is where a chart that stops at
      J = 12 would put them if depth is what produces them.
  P4. THE FAILING SET IS A DENSITY IN THE DEPTH. The fraction of cells
      where h is strictly below the pure-product bound is strictly
      larger over J >= 13 than over J <= 12. Three in 252 is the old
      chart's answer and the old chart's depth ceiling is the suspect.
  P5. UNIQUENESS TRACKS THE HEIGHT. At every cell where the count pass
      closes with h >= 10 the minimiser count is 2 -- one vector up to
      sign. Where h is small the count is larger.
  P6. THE ENRICHED FAMILY IS AN IMPROVEMENT AND NOT THE ANSWER. Least
      height over (pure product) x A equals h at the three known cells,
      and it beats the pure family at strictly MORE cells than it
      attains h at -- so A repairs the family somewhere it is still not
      extremal, which is the same shape as the pure family's own
      failure one level down.
  P7. THE CYCLOTOMIC PART IS ALWAYS A PURE PRODUCT. At every cell the
      witness's cyclotomic multiset, after the residual is divided out,
      decomposes as prod_i (x^{d_i} - 1) -- so the non-pure cyclotomic
      products, of which Phi_3 is the smallest, never appear as the
      thing a minimiser is built from.

KILLS, as observables rather than inferences.
  K-A. THE UNIT-CIRCLE LAW REFUTED. A cell whose exhibited minimiser has
       a residual that the exact test rejects -- not reciprocal, odd
       degree, or a Sturm count below the squarefree degree. The cell,
       the witness, the residual, the y-polynomial and the count print.
  K-B. ROUTE DISAGREEMENT. Any cell where the route differs from the
       parent's end-to-end route, from the quotient DFS, from the rank-1
       closed form, from A059753's boundary, or from the d_2 ladder.
       ANY K-B FIRING BARS READING K-A OR ANY OTHER RESULT AS EVIDENCE.
  K-C. CEILING VIOLATION. An enumerated minimum strictly above the sup
       norm of the exhibited vector its own radius was built from.
  K-D. THE ROUTE STALLS. A first-pass cell exceeding the node cap.
       (A COUNT-pass cell exceeding it is not a kill: the count pass is
       expected to cap and its coverage is a measurement.)
  K-E. BASIS CORRUPTION. A transform that is not unimodular, or a
       witness that J exact synthetic divisions by (x-1) do not clear.
  K-F. MONOTONICITY VIOLATION. h increasing in M at fixed J, or
       decreasing in J at fixed M. Both follow from L_{M,J} sitting
       inside L_{M+1,J} and L_{M,J+1} sitting inside L_{M,J}.
  K-G. A NEW MULTIPLIER. A residual at any cell that is neither 1 nor A.
       It prints in full with its unit-circle verdict. This is P3's
       observable and a kill only of the "A is alone" reading.
  K-H. THE MINIMISER SET SPLITS. A cell where the count pass closes and
       two minimisers have DIFFERENT residuals -- which would make every
       residual statement a statement about a choice and not a cell.

CONTROLS, run and read BEFORE any verdict, each printing how many cases
it exercised.
  C1 (END-TO-END PARITY WITH THE PARENT). The whole new route --
     incremental reduction, own enumeration -- against the parent's
     whole route at all 252 cells of M = 4..30, J = 2..12: reduced bases
     identical, carried Gram-Schmidt equal to a fresh recomputation, and
     h identical. This is what licenses replacing a reduction that cost
     74 times more, and it is checked on the OUTPUT and not on the
     algebra.
  C2 (INDEPENDENT ALGORITHM). The route against the offchart rig's
     interval-pinned quotient DFS deepened until it accepts, over every
     cell of M = 4..12 -- no shared code, no shared arithmetic, no
     shared cost law.
  C3 (RANK-1 CLOSED FORM). h(M, M-1) = C(M-1, floor((M-1)/2)), which
     runs the enumeration at radii up to C(23, 11)*sqrt(24).
  C4 (INCUMBENT, HEIGHT 1). A059753 as an externally proved table:
     h(M, J) = 1 exactly when M > d_1(J). Its fourteen entries reach
     J = 14, but d_1(J) exceeds the widest M here at J >= 8, so both
     directions are exercised only at J <= 7 and the deeper rows check
     the h >= 2 side alone. The split prints.
  C5 (INCUMBENT, HEIGHT 2). The d_2 ladder as a cited table:
     h(M, J) <= 2 exactly when M > d_2(J), over J = 2..8, both sides.
  C6 (THE INSTRUMENTS' OWN CONTROLS). The unit-circle test on a slate of
     KNOWN answers fixed here: Phi_d for d = 1..12, A, 2x^2 + 3x + 2 and
     (x^2+1)(2x^2+3x+2) all on the circle; x^2 - 3x + 1, x^2 - x - 1,
     2x^2 + 5x + 2 and Lehmer's polynomial all off it. A test that says
     yes to everything would make P2 vacuous, so the negatives are the
     half that matters. And the pure-product multiset test on the
     divisor multisets of known products (positive) and on {3} and {4}
     (negative -- Phi_3 and Phi_4 are cyclotomic and not pure products).
  C7 (MONOTONICITY). Both monotonicities at every cell (K-F).
  C9 (THE SPLITTER, RECONSTRUCTED). Every claim about a residual rests
     on one routine, and multiplying its three pieces back -- the
     monomial shift, the cyclotomic multiset, the residual -- must
     return the witness up to sign at every cell. Complete, free, and
     added by the audit that noticed the instrument doing the headline
     work had a three-cell control. It tests the BOOKKEEPING and not
     the trial loop's index bound, which is argued rather than tested.
  C8 (THE PARENT'S THREE). The three K-A cells reproduce the parent's
     committed values and the parent's committed factorisations exactly:
     h = 39, 9, 25 with residual A and cyclotomic multisets matching the
     three products named at the head of this docstring. An anchor to a
     record outside this run.

THE ARMS.
  1. THE REDUCTION. Incremental LLL: the Gram-Schmidt updated in O(n) on
     each swap instead of recomputed. Returns the basis, the integer
     transform, mu and the norms.
  2. THE WIDE CHART. h(M, J) exactly at M = 4..40, J = 2..min(20, M-1),
     with node count, rank and the reduction/enumeration split (P1).
  3. THE HARVEST. Every witness split into monomial shift, cyclotomic
     multiset and residual; the residual tallied over the chart, tested
     for the unit circle, and the cyclotomic multiset tested for pure
     productness (P2, P3, P7, K-A, K-G).
  4. THE MINIMISER SET. A second enumeration per cell at the FIXED
     radius h*sqrt(M), collecting every vector of sup norm exactly h;
     the count, and the residual read over ALL of them (P5, K-H). By
     the fourth section of the hand attack this pass is expensive
     exactly where h is small, so it carries a per-cell node cap AND a
     total node budget for the arm, and it walks the cells in
     DESCENDING h -- a deterministic order, fixed here, that spends the
     budget on the cells P5 is about. Coverage is a measurement and
     never a target: cells that cap and cells the budget does not reach
     are both reported as such and neither is a kill.
  5. PRODUCT EXTREMALITY WIDE, AND THE ENRICHED FAMILY. Least height
     over pure products, over (pure product) x A, and exact h, at every
     cell; the failing set by depth (P4, P6).
  6. THE CONTROLS.

RESOURCE NOTE. Exact integer and rational arithmetic, no numpy, so no
BLAS arenas; the working set is a few reduced bases, a product table of
under a thousand rows and the collected vectors of one count-pass cell,
so the run sits far under the 512 MB default and is run under memwatch
anyway. Wall is estimated at 6 to 10 minutes, of which 128 s is C1's
parent-side reduction -- the control that licenses never paying it
again. Named as over the five-minute line and under the ten: nothing
cheaper decides C1, because the whole point of the arm is that the two
reductions agree on output.

F1. EVERY CONTROL PASSES, AND THE ONE THAT FIRED WAS THE SLATE'S OWN
HAND ANSWER. C6 first, because everything after it is read through the
two instruments it tests: the unit-circle test is right on all 21 cases,
16 positives and 5 negatives, the negatives being the half that matters
since a test saying yes to everything would make P2 vacuous; the
pure-product test is right on all 11, 6 positives and 5 negatives. IN
THE FIRST RUN IT WAS 9 OF 10 AND THE ERROR WAS THE ANSWER KEY'S: the slate had
listed the multiset {1, 1, 3} as a NEGATIVE and it is the divisor
multiset of (x-1)(x^3-1), so the instrument was right and the frozen
expectation was wrong. The K-B that fired was therefore a fault in the
control's own answer key and not in anything the route computes, which
is the only reading under which the rule "any K-B firing bars reading
K-A" is honoured rather than dodged -- the entry is corrected, two
genuine negatives replace it, and the whole rig was rerun. The value
controls: C1, end-to-end against the parent's whole route at all 252
cells of M = 4..30, J = 2..12, 0 bases differing, 0 carried
Gram-Schmidts differing and 0 heights differing. THE 137.5 s THAT
CONTROL COSTS IS NOT THE PARENT'S REDUCTION ALONE and an earlier draft
of this record said it was: the timer wraps BOTH routes over the 252
cells plus two extra Gram-Schmidts. The clean same-cells comparison is
the pre-slate probe's, 128.2 s against 1.7 s; what this rig itself
prints is that the incremental reduction does all 550 cells of the
wider chart in 10.0 s. C9, the splitter multiplied back -- monomial
shift times cyclotomics times residual against the witness -- 550
witnesses and 0 failing to reconstruct, which is the only complete
control the residual has and it was added by the audit that noticed
the instrument doing the headline work had a three-cell one;
C2, the interval-pinned quotient DFS at 54 cells, 0 mismatches; C3, the
rank-1 closed form at 22 cells, 0 mismatches, the largest being
C(23, 11) = 1,352,078 and the only control exercising a huge ball; C4,
A059753's boundary at 415 cells, 153 above it confirming h = 1 and 262
below confirming h >= 2, 0 mismatches; C5, the d_2 ladder's at 244
cells, 191 above confirming h <= 2 and 53 below confirming h >= 3, 0
mismatches; C7, both monotonicities at 1,044 comparisons, 0 violations;
C8, the parent's three cells reproducing its committed values AND its
committed factorisations, 3 of 3. K-B, K-C, K-D and K-E silent, and
K-F too.

F2. THE WIDE CHART CLOSES AND THE BILL HAS CROSSED (rule, exhaustive
over the range; P1 holds). All 550 cells of M = 4..40,
J = 2..min(20, M-1) are decided exactly in 22.6 s and 433,866
enumeration nodes, the worst single cell 20,287 at M = 40, J = 16. Of
that wall the REDUCTION is 10.0 s and the ENUMERATION 12.6 s: the
parent's 127.7-to-0.6 has become 10.0-to-12.6 on a chart 2.2 times the
size, so the incremental Gram-Schmidt has not merely sped the route up,
it has moved which half the instrument's cost lives in. Every sentence
about this route's price from here is a sentence about the ball's volume
over the lattice's covolume, and a wider census is priced by that.

F3. PRODUCT EXTREMALITY IS A DENSITY IN THE DEPTH AND NOT A SPORADIC
FAILURE (rule, exhaustive over the range; P4 holds). At 530 of the 550
cells h IS the least height over pure products with at least J factors
and degree below M; at 20 it is strictly below one. Split by depth the
20 are not scattered: 3 of 362 cells at J <= 12 (0.8%) against 17 of 188
at J >= 13 (9.0%). THAT RAW SPLIT IS CONFOUNDED BY THE HEIGHT AND THE
CONFOUND IS COUNTED RATHER THAN ARGUED: 153 of the 550 cells have
h = 1, where the pure bound is 1 and h >= 1 always, so the cell CANNOT
fail -- and they crowd the shallow half, since h = 1 needs width
against depth. Conditioned on h >= 2 the split is 3 of 209 against 17
of 188, 1.4% against 9.0%; at h >= 10 it is 2 of 61 against 17 of 185,
3.3% against 9.2%. The gap survives every floor, so the depth effect is
real and the headline 0.8% overstates it. And the failing cells sit at
RANKS 5 to 18 in a chart reaching rank 38, on ten of those fourteen
ranks, so neither variable alone selects them. The parent's own
rectangle reproduces its 3 of 252 exactly, so what the parent read as
three sporadic failures was a fact about its DEPTH CEILING and not about
the problem -- and the previous close's reading of the failing set's
shape in the WIDTH was reading the wrong variable.

F4. WHAT BEATS THE PRODUCTS IS TWO FIXED NON-MONIC FACTORS AND NOTHING
ELSE (rule, exhaustive over the range; K-G fires once, P3 holds, P7
holds). Divide every one of the 550 exhibited minimisers by every
cyclotomic factor it has. Exactly THREE residuals survive over the whole
chart:

    1                              at 530 cells
    A = 2 + 4x + 5x^2 + 4x^3 + 2x^4  at  16 cells
    B = 2 + 3x + 2x^2                at   4 cells

B is new; A is the parent's. And the CYCLOTOMIC part is a pure product
at every one of the 550, with 0 exceptions -- so no minimiser on this
chart is built from a cyclotomic product that is not a pure product.
P7's own parenthetical named Phi_3 as the smallest such and is WRONG:
x + 1 is smaller, and it is not a pure product because every pure
product vanishes at 1 while x + 1 does not. It appears in the multisets
constantly and never bare, always with the Phi_1 that makes it a factor
of x^2 - 1, which is exactly what the test checks. Every exhibited
minimiser is therefore a pure product times 1, A or B. The 16 A-cells
and the 4 B-cells are exactly the 20 of F3, so the enrichment is not an
extra structure noticed alongside the failures: it IS the failures.

F5. AND THE THREE ARE ONE FAMILY, WHICH IS WHAT THE REFUTED LAW WAS A
CASE OF. A and B are reciprocal with leading coefficient 2 and every
root on |z| = 1: in y = x + 1/x they are 2y^2 + 4y + 1 and 2y + 3, whose
roots -1 +- sqrt(2)/2 and -3/2 are real and inside (-2, 2), and the
Sturm count confirms 2 of 2 and 1 of 1. NEITHER CARRIES A ROOT OF UNITY,
and the reason is the census and not the leading coefficient --
non-monic does not forbid one, 2(x - 1) having the root 1. A root of
unity among their roots would force a cyclotomic factor, and A and B are
exactly what SURVIVES dividing every cyclotomic out, so the split that
produced them is the same fact. So the pure products -- monic, every
root a root of unity -- and their two enrichments sit inside ONE class:
integer polynomials with every root on the unit circle. KRONECKER IS
WHAT MAKES THAT THE RIGHT CLASS RATHER THAN A CONVENIENT ONE. A monic
integer polynomial with nonzero constant term and all roots on the
circle has all roots roots of unity, hence is a product of cyclotomics,
hence has residual 1. So a residual of positive degree can be inside the
class only by being NON-MONIC, and the census says exactly two non-monic
factors occur across 550 cells. The refuted pure-product law sits INSIDE
this class's monic case and is not equal to it: Kronecker delivers the
products of CYCLOTOMICS, and the pure products are a strict subset of
those -- Phi_3 = 1 + x + x^2 is a product of cyclotomics and not a pure
product, as the third section of this record says in as many words. What
carries the statement the rest of the way to the PURE products is the
census's other half, that the cyclotomic part decomposes as
prod(x^{d_i} - 1) at every cell. (SETTLED SINCE, by
explore_flatten_select.py, which extends this chart to 695 cells at
M = 4..40, J = 2..30: the residual count is FIVE rather than three, the
new ones being the product A*B at two cells -- no new member, the class
being closed under multiplication -- and C = 3 + 5x + 3x^2 at one, whose
LEADING COEFFICIENT IS THREE. Everything above survives as a statement
about the 550, which is what it measured; what does not survive is
"exactly two", and with it the reading of leading coefficient 2 as a
property of the multipliers rather than of the two this chart reached.
The unit-circle law itself survives all 695.)

P2 HOLDS, and its verdict needs one clause the findings above dropped.
22 of the 550 witnesses carry a MONOMIAL factor, and a root at 0 is not
on the unit circle, so those 22 vectors do not literally satisfy the
law. They do not need to. If P = x^a Q with Q(0) nonzero then Q has the
SAME coefficient multiset -- hence the same height -- the same
multiplicity of the root 1, hence the same flattening, and a lower
degree, so Q lies in the same lattice and is a minimiser of the same
cell with no root at 0. The attainment statement is therefore exactly
true with no qualifier at all: at every one of the 550 cells h is
attained by a vector all of whose roots lie on the unit circle. It is
the STRONGER reading, that every minimiser does, which F7 refutes.

F6. THE ENRICHED FAMILY NEVER IMPROVES WITHOUT BEING EXACTLY RIGHT, AND
P6 IS REFUTED IN THE HALF THAT WAS A GUESS. Least height over
(pure product) x A, swept over the same multiset enumeration as the pure
family so that the two are two heights of one object rather than two
searches, beats the pure family at exactly 16 cells and ATTAINS h at all
16 of them -- never at more, never by an amount that leaves a gap. The
frozen prediction said A would repair the family somewhere it was STILL
not extremal, on the analogy of the pure family's own failure one level
down; it does not, and the four cells where h is below the pure bound
and A does not help are precisely the four B cells. So the union of the
three families is extremal at every one of the 550 cells, exhaustively,
and the analogy that produced P6 was the wrong shape.

F7. THE LAW IS ABOUT ATTAINMENT AND NOT ABOUT MINIMISERS, AND THE LEAK
IS CONFINED TO SMALL HEIGHT (K-H fires 28 times; this arm's own
observable, unnamed at the freeze). The second pass at the FIXED radius
h*sqrt(M) closes 405 of the 550 cells -- 57 capped at 50,000 nodes and
88 never reached inside the arm's 4,000,000-node budget, 112.7 s, the
coverage being a measurement and not a target. At 28 of the 405 two
minimisers of ONE cell have DIFFERENT residuals, so the residual is a
property of the choice there and not of the cell. At 24 of the 405 some
minimiser leaves the unit-circle class altogether -- and their heights
are only 1, 2, 3 and 6, the highest leaking cell being h = 6. So what is
exhaustively true is that h is ATTAINED inside the class at every cell,
and the stronger reading -- that everything attaining it is inside -- is
FALSE. WHERE it is false is a statement about the 405 and not about the
550: the 88 cells the budget never reaches are the lowest-height ones by
construction, the pass walking in DESCENDING h, and the 57 that cap are
wherever the ball is too populous, their heights unreported. So the leak
is confined to small height among the cells that were LOOKED at, and the
cells that were not are on the same side of the height as the leak --
which weakens the confinement rather than the refutation. Over the
closed cells 305 distinct residual classes appear; A shows at 19 of them
and B at 5, three and one more than the exhibited witnesses alone
reported, so the count pass finds the two multipliers at cells whose
first-pass witness was a pure product. Of the 25 commonest classes the
arm prints, every off-circle one is monic -- an OBSERVATION over what
printed and not a consequence of anything, and stated here because an
earlier draft credited it to F5's Kronecker step. That step runs the
other way: it forbids a monic cyclotomic-free residual from being ON the
circle, and says nothing against a non-monic residual being off it. C6's
own negative slate holds one, 2x^2 + 5x + 2.

F8. UNIQUENESS IS NOT A HEIGHT PHENOMENON AND P5 IS REFUTED. Of the
closed cells 246 have h >= 10, and their minimiser counts are 2, 4, 6,
8, 10 and 18 -- always EVEN, the lattice being closed under negation, so
a count of 18 is nine minimisers up to sign and a count of 2 is one.
51 of the 246 carry a count other than 2, so a large
height does not force a single minimiser up to sign. Below h = 10 the
counts run to 1,112. The frozen prediction said every cell with h >= 10
has exactly 2. IT WAS ALREADY FALSE WHEN IT WAS FROZEN, against a
measurement recorded four paragraphs above it: pre-slate probe (iv)
returned 8 minimisers at (24, 11), and h(24, 11) = 16 is above the
prediction's own threshold of 10. So this is not a prediction the run
overturned; it is one the slate contradicted at the moment of writing,
by extrapolating from the five cells of a six-cell probe and not
checking the sixth against the threshold it was about to name. The
species is a prediction whose stated scope is not read back against the
data already in the same file.

RUN RECORD (final run: wall 281.5 s, peak working set 57.0 MB, peak
commit 51.8 MB under memwatch's 512 MB default -- exact rational
arithmetic over a few reduced bases, one product table of 780 keys and
one cell's collected vectors, so the memory line was never in question).
The estimate was 6 to 10 minutes and the wall is 4.7, which is recorded
because the estimate was made of the right half: C1 is 137.5 s of it,
half the run, and it is the control that licenses never paying the
parent's reduction again.

FIVE runs, and none of the four that preceded the last changed a
result. The FIRST was sound in everything the route computes and is
superseded for two reasons, neither of them science. Its C6 fired a K-B
on the PURE-PRODUCT ANSWER KEY (F1), and its arm 4 counted off-circle
vectors from the minimiser SET under K-A, whose frozen text reads "a
cell whose EXHIBITED minimiser has a residual the test rejects" -- a
code fault against the slate above, not a finding, and the 586 K-A
firings it printed were 586 statements about a question the frozen kill
does not ask. The SECOND corrects the answer key, gives arm 4 its own
named observable, and replaces those 586 lines with the tallies F7
quotes. The THIRD and FOURTH were the AUDIT's, and each bought one
thing the earlier runs could not state. The third added arm 5's split
at several floors on h, after the audit found the depth density's
headline divided by a denominator padded with 153 cells that cannot
fail (F3) -- a confound the rig had not counted and the prose had not
named. The fourth added C9, the splitter multiplied back at all 550
witnesses, after the audit found the instrument every residual claim
rests on controlled at three cells by C8 and nowhere else.

The FIFTH is this record's, and it exists because the audit SMOKE-RAN
every arm at a tiny sweep and found two arms that crash when their
result set is empty: the rank window when no cell fails, and C8 when
its three named cells fall outside the range. Both are impossible at
the range this rig ships with -- twenty cells fail and all three are
in the sweep -- and both would have fired on any narrower one, AFTER
the science had printed, which is the worst place for a crash. They
are guarded, C8 now reporting itself unexercised rather than crashing
or passing in silence, and the run confirms the guards move nothing.

Every value in F2 through F6 and F8 printed identically in every run
where the arm existed: 550 cells, 433,866 nodes, worst cell 20,287
at (40, 16), 530 tight and 20 strictly below, 3 of 362 against 17 of
188, three residuals, 0 non-pure cyclotomic parts, 16 enriched
attainments, 405 closed, 57 capped, 88 unreached and 28 K-H. Only the
WALL moves between them, by a few tenths. That is the only reproduction
claimed here.
"""
import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time
from fractions import Fraction as F
from math import comb, floor as mfloor, gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_flatten_offchart import NodeCap, feasible, mul_shift, height
from explore_flatten_lattice import (basis, gram_schmidt, clears, det_pm1,
                                     frac_sqrt_up)
import explore_flatten_lattice as PARENT

A059753 = [1, 3, 6, 11, 15, 22, 30, 41, 48, 61, 69, 93, 112, 120]
D2 = [1, 2, 4, 7, 11, 16, 22, 26]
AQ = [2, 4, 5, 4, 2]

SWEEP_M = 40
SWEEP_J = 20
PARENT_M = 30
PARENT_J = 12
FIRST_CAP = 20000000
COUNT_CAP = 50000
COUNT_BUDGET = 4000000


# ------------------------------------------------ arm 1: the reduction

def lll_incr(B, delta=F(99, 100)):
    """LLL in exact rationals with the Gram-Schmidt UPDATED on a swap
    rather than recomputed. Same size-reduction order and the same
    rounding as the parent's, so the two walk the same path and their
    outputs are comparable elementwise (C1). Returns basis, transform,
    mu and the squared norms of the orthogonalised basis."""
    B = [list(b) for b in B]
    n = len(B)
    T = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    mu, A = gram_schmidt(B)
    k = 1
    while k < n:
        for j in range(k - 1, -1, -1):
            r = mfloor(mu[k][j] + F(1, 2))
            if r:
                B[k] = [B[k][t] - r * B[j][t] for t in range(len(B[k]))]
                T[k] = [T[k][t] - r * T[j][t] for t in range(n)]
                for t in range(j):
                    mu[k][t] -= r * mu[j][t]
                mu[k][j] -= r
        if A[k] >= (delta - mu[k][k - 1] ** 2) * A[k - 1]:
            k += 1
        else:
            m = mu[k][k - 1]
            Bk = A[k] + m * m * A[k - 1]
            mu[k][k - 1] = m * A[k - 1] / Bk
            A[k] = A[k - 1] * A[k] / Bk
            A[k - 1] = Bk
            B[k], B[k - 1] = B[k - 1], B[k]
            T[k], T[k - 1] = T[k - 1], T[k]
            for j in range(k - 1):
                mu[k][j], mu[k - 1][j] = mu[k - 1][j], mu[k][j]
            for i in range(k + 1, n):
                t = mu[i][k]
                mu[i][k] = mu[i][k - 1] - m * t
                mu[i][k - 1] = t + mu[k][k - 1] * mu[i][k]
            k = max(k - 1, 1)
    return B, T, mu, A


def enum_ball(B, mu, A, M, R2, cap, collect=None):
    """Fincke-Pohst over the lattice spanned by B, exact. Returns the
    least sup norm of a nonzero vector inside the L2 ball of radius
    sqrt(R2), a witness and the node count. With collect=None the radius
    SHRINKS to (h-1)*sqrt(M) on every improvement, which is what makes
    the first pass cheap and is also why it never sees a second
    minimiser. Pass a list as collect to hold the radius fixed and
    record every vector in the ball instead (arm 4)."""
    n = len(B)
    x = [0] * n
    best = [None, None]
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
        mid = mfloor(c + F(1, 2))
        for xi in sorted(range(lo, hi + 1), key=lambda t: abs(t - mid)):
            d = (F(xi) - c) ** 2 * A[i]
            if d <= rad[0] - partial:
                x[i] = xi
                rec(i - 1, partial + d)
        x[i] = 0

    rec(n - 1, F(0))
    return best[0], best[1], nodes[0]


TIME = {"lll": 0.0, "enum": 0.0}


def route_h(M, J):
    """h(M, J) exactly, with a witness, the node count and the reduced
    data kept for the count pass. The starting radius comes from the
    reduced basis's OWN vectors, so no external ceiling enters and in
    particular the product family under test supplies nothing."""
    t0 = time.time()
    B, T, mu, A = lll_incr(basis(M, J))
    if not det_pm1(T):
        raise ValueError("K-E basis corruption at M=%d J=%d" % (M, J))
    t1 = time.time()
    H = min(max(abs(c) for c in b) for b in B)
    h, v, nodes = enum_ball(B, mu, A, M, F(H * H * M), FIRST_CAP)
    TIME["lll"] += t1 - t0
    TIME["enum"] += time.time() - t1
    if h is None or h > H:
        raise ValueError("K-C ceiling violation at M=%d J=%d: %s > %d"
                         % (M, J, h, H))
    ok, _ = clears(v, J)
    if not ok:
        raise ValueError("K-E witness not divisible at M=%d J=%d" % (M, J))
    return h, v, nodes, (B, mu, A)


# ------------------------------------- arm 3: the cyclotomic machinery

def polydiv(a, b):
    """Exact quotient of integer polys, low degree first; None if b does
    not divide a."""
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    db, da = len(b) - 1, len(a) - 1
    if da < db:
        return None if any(a) else [0]
    q = [0] * (da - db + 1)
    for i in range(da - db, -1, -1):
        if a[i + db] % b[db]:
            return None
        c = a[i + db] // b[db]
        q[i] = c
        if c:
            for t in range(db + 1):
                a[i + t] -= c * b[t]
    return None if any(a) else q


CYC = {}


def phi_poly(d):
    """Phi_d, from x^d - 1 divided by the proper divisors' cyclotomics."""
    if d not in CYC:
        p = [-1] + [0] * (d - 1) + [1]
        for e in range(1, d):
            if d % e == 0:
                p = polydiv(p, phi_poly(e))
        CYC[d] = p
    return CYC[d]


def split_witness(w):
    """(monomial shift, cyclotomic multiset, residual with positive
    leading coefficient). THE INDEX BOUND IS ON deg Phi_d AND NOT ON d:
    Phi_d has degree phi(d), so a quartic can carry Phi_5 and a
    degree-40 residual can carry a Phi_d with d far above 40."""
    p = list(w)
    while p and p[-1] == 0:
        p.pop()
    shift = 0
    while p and p[0] == 0:
        p.pop(0)
        shift += 1
    fac = []
    d = 1
    dmax = 6 * len(p) + 40
    while d <= dmax:
        if len(phi_poly(d)) - 1 > len(p) - 1:
            d += 1
            continue
        q = polydiv(p, phi_poly(d))
        if q is None:
            d += 1
        else:
            fac.append(d)
            p = q
    if p and p[-1] < 0:
        p = [-c for c in p]
    return shift, tuple(sorted(fac)), tuple(p)


def divisors(n):
    return [e for e in range(1, n + 1) if n % e == 0]


def as_pure_product(S):
    """Is the cyclotomic multiset S the divisor multiset of a pure
    product? Deterministic: divisors(d) has maximum d, so the largest
    surviving index MUST be a part, and there is nothing to search.
    Returns the parts, or None."""
    S = sorted(S, reverse=True)
    parts = []
    while S:
        d = S[0]
        parts.append(d)
        for e in divisors(d):
            if e not in S:
                return None
            S.remove(e)
        S.sort(reverse=True)
    return tuple(sorted(parts, reverse=True))


# ----------------------------------- arm 3: the unit-circle test, exact

def poly_trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def poly_rem(a, b):
    """Remainder over Q, both lists of Fraction."""
    a = [F(c) for c in a]
    b = poly_trim([F(c) for c in b])
    while True:
        a = poly_trim(a)
        if len(a) < len(b):
            return a
        c = a[-1] / b[-1]
        sh = len(a) - len(b)
        for t in range(len(b)):
            a[sh + t] -= c * b[t]


def poly_gcd(a, b):
    a, b = [F(c) for c in a], [F(c) for c in b]
    while poly_trim(b):
        a, b = b, poly_rem(a, b)
    a = poly_trim(a)
    if a and a[-1] != 1:
        a = [c / a[-1] for c in a]
    return a


def poly_exact_div(a, b):
    a = [F(c) for c in a]
    b = poly_trim([F(c) for c in b])
    q = [F(0)] * (len(a) - len(b) + 1)
    for i in range(len(a) - len(b), -1, -1):
        c = a[i + len(b) - 1] / b[-1]
        q[i] = c
        if c:
            for t in range(len(b)):
                a[i + t] -= c * b[t]
    return q


def primitive(q):
    """Scale a Fraction poly to primitive integers."""
    den = 1
    for c in q:
        den = den * c.denominator // gcd(den, c.denominator)
    ints = [int(c * den) for c in q]
    g = 0
    for c in ints:
        g = gcd(g, abs(c))
    return [c // g for c in ints] if g else ints


def poly_eval(p, x):
    acc = F(0)
    for c in reversed(p):
        acc = acc * x + F(c)
    return acc


def sturm_count(p, lo, hi):
    """Distinct real roots of a SQUAREFREE p in (lo, hi], exact."""
    chain = [[F(c) for c in p],
             [F(i) * F(p[i]) for i in range(1, len(p))]]
    while True:
        r = poly_trim(poly_rem(chain[-2], chain[-1]))
        if not r:
            break
        chain.append([-c for c in r])

    def sc(x):
        s = [poly_eval(c, F(x)) for c in chain]
        s = [t for t in s if t != 0]
        return sum(1 for i in range(len(s) - 1)
                   if (s[i] > 0) != (s[i + 1] > 0))

    return sc(lo) - sc(hi)


def y_polynomial(R):
    """The integer Q with R(x) = x^m Q(x + 1/x), for R reciprocal of even
    degree 2m. t_0 = 2, t_1 = y, t_{k+1} = y t_k - t_{k-1}, and
    R/x^m = r_m + sum_{k>=1} r_{m+k} t_k(y)."""
    m = (len(R) - 1) // 2
    t_prev, t_cur = [2], [0, 1]
    Q = [R[m]]
    for k in range(1, m + 1):
        c = R[m + k]
        if c:
            while len(Q) < len(t_cur):
                Q.append(0)
            for i in range(len(t_cur)):
                Q[i] += c * t_cur[i]
        nxt = [0] * (len(t_cur) + 1)
        for i in range(len(t_cur)):
            nxt[i + 1] += t_cur[i]
        for i in range(len(t_prev)):
            nxt[i] -= t_prev[i]
        t_prev, t_cur = t_cur, nxt
    return poly_trim(Q)


def on_unit_circle(R):
    """Do ALL roots of the integer polynomial R lie on |z| = 1?
    Returns (verdict, reason, Q, count, squarefree degree). Vacuously
    true for a constant. (x -+ 1) divided out first, so the test is
    correct on any integer polynomial; then reciprocal or fail, even
    degree or fail, then a Sturm count of Q's distinct real roots in
    [-2, 2] against the degree of Q's squarefree part."""
    R = poly_trim(R)
    if not R:
        return False, "zero polynomial", [], 0, 0
    if R[0] == 0:
        return False, "root at 0", [], 0, 0
    for f in ([-1, 1], [1, 1]):
        while len(R) > 1:
            q = polydiv(R, f)
            if q is None:
                break
            R = poly_trim(q)
    if len(R) <= 1:
        return True, "constant", [], 0, 0
    if list(reversed(R)) != R:
        return False, "not reciprocal", [], 0, 0
    if (len(R) - 1) % 2:
        return False, "odd degree", [], 0, 0
    Q = y_polynomial(R)
    g = poly_gcd(Q, [F(i) * F(Q[i]) for i in range(1, len(Q))])
    sf = Q if len(g) <= 1 else primitive(poly_exact_div(Q, g))
    if poly_eval(sf, F(-2)) == 0 or poly_eval(sf, F(2)) == 0:
        return False, "y = +-2 survives the cyclotomic split", Q, 0, 0
    cnt = sturm_count(sf, F(-2), F(2))
    return cnt == len(sf) - 1, "sturm", Q, cnt, len(sf) - 1


# ------------------------------ arm 5: the pure and the enriched family

def family_tables(budget, mult):
    """Least height over multisets of parts keyed (count, degree sum),
    for the pure products AND for the products times `mult`. Both walk
    the SAME multiset enumeration, so the comparison is between two
    heights of one object and never between two searches."""
    pure, purew, enr, enrw, cur = {}, {}, {}, {}, []

    def dfs(start, poly, polyA, count, s):
        if count:
            key = (count, s)
            h1, h2 = height(poly), height(polyA)
            if key not in pure or h1 < pure[key]:
                pure[key], purew[key] = h1, tuple(cur)
            if key not in enr or h2 < enr[key]:
                enr[key], enrw[key] = h2, tuple(cur)
        for d in range(start, budget - s + 1):
            cur.append(d)
            dfs(d, mul_shift(poly, d), mul_shift(polyA, d), count + 1, s + d)
            cur.pop()

    dfs(1, [1], list(mult), 0, 0)
    return (pure, purew), (enr, enrw)


def family_bound(tab, J, maxsum):
    """(least height, witness multiset) over |D| >= J, sum D <= maxsum."""
    best, wit = None, None
    for (c, s), H in tab[0].items():
        if c >= J and s <= maxsum and (best is None or H < best):
            best, wit = H, tab[1][(c, s)]
    return best, wit


def mulpoly(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, c in enumerate(a):
        if c:
            for j, d in enumerate(b):
                r[i + j] += c * d
    return r


def divisor_multiset(parts):
    S = []
    for d in parts:
        S += divisors(d)
    return tuple(sorted(S))


def main():
    t_all = time.time()
    fired = dict(("K-" + c, 0) for c in "ABCDEFGH")

    print("=" * 70)
    print("explore_flatten_family.py -- what family do the minimisers"
          " live in?")
    print("=" * 70)

    # -------------------------------- C6: the instruments' own controls
    print("\n[C6] the instruments' own controls, before anything uses them")
    slate = [("Phi_%d" % d, list(phi_poly(d)), True) for d in range(1, 13)]
    slate += [
        ("A", list(AQ), True),
        ("2x^2+3x+2", [2, 3, 2], True),
        ("(x^2+1)(2x^2+3x+2)", mulpoly([1, 0, 1], [2, 3, 2]), True),
        ("A^2", mulpoly(AQ, AQ), True),
        ("x^2-3x+1", [1, -3, 1], False),
        ("x^2-x-1", [-1, -1, 1], False),
        ("2x^2+5x+2", [2, 5, 2], False),
        ("Lehmer", [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1], False),
        ("A*(x^2-3x+1)", mulpoly(AQ, [1, -3, 1]), False),
    ]
    okc = badc = 0
    for (nm, p, want) in slate:
        got = on_unit_circle(p)[0]
        if got == want:
            okc += 1
        else:
            badc += 1
            fired["K-B"] += 1
            print("   K-B unit-circle test: %s wanted %s got %s"
                  % (nm, want, got))
    print("   unit circle: %d cases (%d positives, %d negatives), "
          "%d correct, %d wrong"
          % (len(slate), sum(1 for s in slate if s[2]),
             sum(1 for s in slate if not s[2]), okc, badc))

    pslate = [(divisor_multiset(D), True) for D in
              [(1,), (2,), (3,), (2, 2), (5, 3, 2, 2, 1, 1), (6, 4, 1)]]
    # THE FIRST RUN'S C6 CAUGHT A WRONG EXPECTED ANSWER HERE, not a wrong
    # instrument: the slate had listed {1, 1, 3} as a negative, and it is
    # the divisor multiset of (x-1)(x^3-1) and so a pure product. The
    # control fired, the hand answer was the thing that was wrong, and the
    # two genuine negatives that replace it are checked in the comment
    # rather than assumed -- {1, 3, 3} peels 3 and is left with a bare 3
    # whose divisor 1 is gone, and {1, 1, 6} lacks the 2 and 3 that
    # divisors(6) demands.
    pslate += [((3,), False), ((4,), False), ((1, 3, 3), False),
               ((1, 1, 6), False), ((1, 2, 2), False)]
    okp = badp = 0
    for (S, want) in pslate:
        got = as_pure_product(S) is not None
        if got == want:
            okp += 1
        else:
            badp += 1
            fired["K-B"] += 1
            print("   K-B pure-product test: %s wanted %s got %s"
                  % (list(S), want, got))
    print("   pure product: %d cases (%d positives, %d negatives), "
          "%d correct, %d wrong"
          % (len(pslate), sum(1 for s in pslate if s[1]),
             sum(1 for s in pslate if not s[1]), okp, badp))

    # -------------------------------------------- arm 2: the wide chart
    print("\n[arm 2] the wide chart -- h(M, J), M = 4..%d, J = 2..%d"
          % (SWEEP_M, SWEEP_J))
    t = time.time()
    H, NODES = {}, {}
    for M in range(4, SWEEP_M + 1):
        t_row = time.time()
        for J in range(2, min(SWEEP_J, M - 1) + 1):
            try:
                h, v, nodes, _ = route_h(M, J)
            except NodeCap:
                fired["K-D"] += 1
                print("   K-D stalled at M=%d J=%d rank=%d" % (M, J, M - J))
                continue
            H[(M, J)] = (h, v)
            NODES[(M, J)] = nodes
        print("   M = %2d done, %.1f s (%.1f s in)"
              % (M, time.time() - t_row, time.time() - t))
    print("   %d cells decided, %.1f s, %d nodes total"
          % (len(H), time.time() - t, sum(NODES.values())))
    print("   worst cell %s at %d nodes"
          % (max(NODES, key=lambda c: NODES[c]), max(NODES.values())))
    print("   of which reduction %.1f s and enumeration %.1f s"
          % (TIME["lll"], TIME["enum"]))

    for (j0, j1) in [(2, 11), (12, SWEEP_J)]:
        print("\n   h(M, J), rows M, columns J = %d..%d" % (j0, j1))
        print("      M |" + "".join("%8d" % J for J in range(j0, j1 + 1)))
        for M in range(4, SWEEP_M + 1):
            row = "".join("%8s" % (H[(M, J)][0] if (M, J) in H else "")
                          for J in range(j0, j1 + 1))
            if row.strip():
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

    # ----------------------------------------------- arm 3: the harvest
    print("\n[arm 3] the harvest -- every witness split and tested")
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
    print("   %d witnesses, %d carrying a monomial factor" % (len(H), shifts))
    print("   %d distinct residuals:" % len(tally))
    for res in sorted(tally, key=lambda r: (len(r), r)):
        cells = tally[res]
        ok, why, Q, cnt, deg = on_unit_circle(list(res))
        if not ok:
            fired["K-A"] += 1
        if list(res) not in ([1], list(AQ)):
            fired["K-G"] += 1
        print("      residual %-30s %3d cells   unit circle: %s (%s%s)"
              % (str(list(res)), len(cells), ok, why,
                 ", %d of %d roots in [-2,2]" % (cnt, deg)
                 if why == "sturm" else ""))
        if list(res) != [1]:
            print("         y-polynomial %s; cells %s"
                  % (Q, cells if len(cells) <= 20 else
                     "%d cells" % len(cells)))
    # C9 (THE SPLITTER, RECONSTRUCTED). The residual is the instrument
    # every claim below rests on, and until this pass its only control
    # was C8's three cells against an externally committed
    # factorisation. Multiplying the pieces back is a COMPLETE control
    # and it is free: x^shift times the cyclotomics times the residual
    # must be the witness up to sign at every cell, which catches a
    # dropped factor, a wrong index, a lost sign and a lost monomial at
    # once. It cannot catch a residual that is itself divisible by a
    # cyclotomic the trial loop never reached -- that is what the index
    # bound on phi(d) is for -- so it is a control on the BOOKKEEPING
    # and the loop bound is argued rather than tested.
    n9 = bad9 = 0
    for (M, J), (sh, cyc, res) in sorted(SPLIT.items()):
        n9 += 1
        prod = [0] * sh + [1]
        for d in cyc:
            prod = mulpoly(prod, phi_poly(d))
        prod = mulpoly(prod, list(res))
        w = poly_trim(list(H[(M, J)][1]))
        if prod != w and [-c for c in prod] != w:
            bad9 += 1
            fired["K-B"] += 1
            print("   K-B M=%d J=%d splitter does not reconstruct its "
                  "witness" % (M, J))
    print("   [C9] the split multiplied back: %d witnesses, %d failing to "
          "reconstruct" % (n9, bad9))
    print("   cyclotomic parts that are NOT pure products: %d" % len(nonpure))
    for row in nonpure[:20]:
        print("      M=%2d J=%2d h=%d cyclotomic %s" % row)

    # ---------------------------------- arm 5: pure and enriched family
    print("\n[arm 5] product extremality wide, and the enriched family")
    t = time.time()
    pure_t, enr_t = family_tables(SWEEP_M - 1, AQ)
    print("   family tables to degree %d: %.1f s, %d keys"
          % (SWEEP_M - 1, time.time() - t, len(pure_t[0])))
    rows = []
    for (M, J), (h, v) in sorted(H.items()):
        ph, pw = family_bound(pure_t, J, M - 1)
        eh, ew = family_bound(enr_t, J, M - 1 - (len(AQ) - 1))
        if ph is None:
            continue
        if h > ph:
            fired["K-B"] += 1
            print("   K-B h ABOVE the pure bound at M=%d J=%d: %d > %d"
                  % (M, J, h, ph))
        rows.append((M, J, h, ph, eh, pw, ew))
    tight = sum(1 for r in rows if r[2] == r[3])
    below = [r for r in rows if r[2] < r[3]]
    print("   %d cells with a pure bound: %d TIGHT, %d STRICTLY BELOW"
          % (len(rows), tight, len(below)))
    # THE DEPTH SPLIT IS CONFOUNDED BY THE HEIGHT AND THE CONFOUND IS
    # COUNTED HERE RATHER THAN ARGUED. Where h = 1 the pure bound is 1
    # and h >= 1 always, so equality is FORCED and the cell can never
    # fail -- and those cells are not spread evenly, since h = 1 needs
    # width against depth. A raw density over all cells therefore
    # divides the shallow half by a denominator padded with cells the
    # comparison cannot reach. The split is printed at several floors on
    # h so the reader can see what survives conditioning.
    for cut in (1, 2, 3, 10):
        for depth in ("<=12", ">=13"):
            sel = [r for r in rows
                   if (r[1] <= 12) == (depth == "<=12") and r[2] >= cut]
            bad = [r for r in sel if r[2] < r[3]]
            print("   h >= %2d, J %s: %d cells, %d strictly below (%.1f%%)"
                  % (cut, depth, len(sel), len(bad),
                     100.0 * len(bad) / len(sel) if sel else 0.0))
    print("   of the %d cells, %d have h = 1 and so cannot fail at all"
          % (len(rows), sum(1 for r in rows if r[2] == 1)))
    ranks = sorted(r[0] - r[1] for r in rows if r[2] < r[3])
    byrank = {}
    for r in rows:
        if r[2] >= 2:
            byrank.setdefault(r[0] - r[1], [0, 0])
            byrank[r[0] - r[1]][0] += 1
            byrank[r[0] - r[1]][1] += 1 if r[2] < r[3] else 0
    # GUARDED because an empty failing set is a legitimate outcome --
    # any narrower range, and the whole point of the sweep is that the
    # count is a measurement. An unguarded ranks[0] crashes the arm
    # AFTER the science has printed, which is the worst place for it.
    if ranks:
        print("   the failing cells' RANKS run %d..%d, in a chart reaching "
              "rank %d; ranks carrying a failure: %s"
              % (ranks[0], ranks[-1], max(r[0] - r[1] for r in rows),
                 sorted(set(ranks))))
    else:
        print("   no cell fails, so there is no rank window to report")
    print("   cells with h >= 2 by rank (cells, failures): %s"
          % sorted((k, tuple(v)) for k, v in byrank.items()))
    old = [r for r in rows if r[0] <= PARENT_M and r[1] <= PARENT_J]
    print("   the parent's rectangle M<=%d J<=%d: %d cells, %d strictly "
          "below" % (PARENT_M, PARENT_J, len(old),
                     sum(1 for r in old if r[2] < r[3])))
    print("   every cell where h is strictly below the pure bound:")
    for (M, J, h, ph, eh, pw, ew) in below:
        print("      M=%2d J=%2d rank=%2d  h=%-5d pure %-5d enriched %-5s "
              "%s" % (M, J, M - J, h, ph, eh,
                      "ENRICHED ATTAINS h" if eh == h else
                      ("enriched also beats pure" if eh is not None
                       and eh < ph else "enriched no better")))
        print("         pure multiset %s   enriched multiset %s"
              % (list(pw), list(ew) if ew else None))
        print("         residual %s" % (list(SPLIT[(M, J)][2]),))
    ebeats = [r for r in rows if r[4] is not None and r[4] < r[3]]
    eattain = [r for r in ebeats if r[4] == r[2]]
    print("   the enriched family beats the pure family at %d cells and "
          "ATTAINS h at %d of them" % (len(ebeats), len(eattain)))
    for (M, J, h, ph, eh, pw, ew) in ebeats:
        print("      M=%2d J=%2d  h=%-5d pure %-5d enriched %-5d %s"
              % (M, J, h, ph, eh, "= h" if eh == h else "> h"))

    # ----------------------------------- arm 4: the minimiser set
    print("\n[arm 4] the minimiser set -- a second pass at fixed radius")
    t = time.time()
    order = sorted(H, key=lambda c: (-H[c][0], c[0], c[1]))
    spent = closed = capped = 0
    counts = {}
    # K-A IS ARM 3's OBSERVABLE AND NOT THIS ARM'S: the frozen kill reads
    # "a cell whose EXHIBITED minimiser has a residual the test rejects",
    # and these vectors are not the exhibited one. The first run counted
    # them under K-A, which is a code fault against the slate above and
    # not a finding. What this arm measures instead is named here and was
    # not named at the freeze: the cells whose minimiser SET leaves the
    # family, which is a strictly stronger question than P2's.
    setoff, setres = [], {}
    for c in order:
        M, J = c
        h = H[c][0]
        if spent >= COUNT_BUDGET:
            break
        B, T, mu, A = lll_incr(basis(M, J))
        got = []
        try:
            _, _, nodes = enum_ball(B, mu, A, M, F(h * h * M), COUNT_CAP,
                                    collect=got)
            spent += nodes
            mins = [w for w in got if max(abs(x) for x in w) == h]
            counts[c] = len(mins)
            closed += 1
            res = set(split_witness(w)[2] for w in mins)
            if len(res) > 1:
                fired["K-H"] += 1
                print("   K-H M=%d J=%d: %d distinct residuals among %d "
                      "minimisers: %s" % (M, J, len(res), len(mins),
                                          [list(r) for r in sorted(res)]))
            off = [r for r in res if not on_unit_circle(list(r))[0]]
            if off:
                setoff.append((M, J, h, len(mins), len(off)))
            for r in res:
                setres.setdefault(r, [0, 0])
                setres[r][0] += 1
                if not on_unit_circle(list(r))[0]:
                    setres[r][1] = 1
        except NodeCap:
            spent += COUNT_CAP
            capped += 1
    print("   %d cells closed, %d capped at %d nodes, %d not reached "
          "(budget %d nodes, %.1f s)"
          % (closed, capped, COUNT_CAP, len(H) - closed - capped,
             COUNT_BUDGET, time.time() - t))
    if counts:
        byh = {}
        for c, n in counts.items():
            byh.setdefault(H[c][0], []).append(n)
        big = [(c, n) for c, n in counts.items() if H[c][0] >= 10]
        print("   of the closed cells, %d have h >= 10; their minimiser "
              "counts: %s" % (len(big), sorted(set(n for _, n in big))))
        notwo = [(c, n) for c, n in big if n != 2]
        print("   cells with h >= 10 and a count other than 2: %d %s"
              % (len(notwo), notwo[:12]))
        small = sorted((h, sorted(set(v))) for h, v in byh.items() if h < 10)
        print("   counts by height below 10: %s" % small)
        print("   K-H fired at %d of the %d closed cells: the residual is a "
              "property of the CHOICE there and not of the cell"
              % (fired["K-H"], closed))
        print("   cells whose minimiser SET leaves the unit-circle family: "
              "%d of %d closed" % (len(setoff), closed))
        hoff = sorted(set(r[2] for r in setoff))
        print("      their heights: %s (the highest closed cell that leaks "
              "is h = %s)" % (hoff[:20], max(hoff) if hoff else None))
        for row in sorted(setoff, key=lambda r: -r[2])[:8]:
            print("      M=%2d J=%2d h=%-6d %d minimisers, %d residual "
                  "classes off the circle" % row)
        print("   residuals seen over ALL minimisers of the closed cells "
              "(cells carrying it, off the circle):")
        srt = sorted(setres, key=lambda r: (-setres[r][0], len(r)))
        print("      %d distinct residual classes; the 25 commonest:"
              % len(srt))
        for r in srt[:25]:
            print("      %-36s %3d cells, off circle: %s"
                  % (str(list(r))[:36], setres[r][0], bool(setres[r][1])))

    print("\nKILLS after arms 2-5: %s" % fired)
    print("wall so far %.1f s" % (time.time() - t_all))

    # ---------------------------------------------- the value controls
    print("\n[C8] the parent's three cells, against its committed record")
    want = {(21, 12): (39, (1,) * 9 + (2, 2, 3)),
            (23, 10): (9, (1,) * 6 + (2, 2, 3, 5)),
            (25, 12): (25, (1,) * 8 + (2, 2, 3, 5))}
    n8 = ok8 = 0
    for c, (wh, parts) in sorted(want.items()):
        # A CONTROL THAT CANNOT RUN MUST SAY SO, not crash and not pass
        # in silence: its three cells are inside the sweep at the range
        # this rig ships with, and a narrowed range must report the
        # control as unexercised rather than take the range's word.
        if c not in SPLIT:
            print("   M=%2d J=%2d NOT IN THIS SWEEP -- control unexercised"
                  % c)
            continue
        n8 += 1
        sh, cyc, res = SPLIT[c]
        good = (H[c][0] == wh and list(res) == list(AQ)
                and cyc == divisor_multiset(parts))
        if good:
            ok8 += 1
        else:
            fired["K-B"] += 1
        print("   M=%2d J=%2d: h %d (want %d), residual %s, cyclotomic "
              "matches the committed product: %s"
              % (c[0], c[1], H[c][0], wh, list(res),
                 cyc == divisor_multiset(parts)))
    print("   %d of 3 cells exercised, %d reproduce the parent exactly"
          % (n8, ok8))

    print("\n[C2] independent algorithm: the quotient DFS, deepened")
    n2 = mism2 = 0
    for M in range(4, 13):
        for J in range(2, M):
            if (M, J) not in H:
                continue
            k = 1
            while k <= 1000 and not feasible(M, J, k, 200000000):
                k += 1
            n2 += 1
            if k != H[(M, J)][0]:
                mism2 += 1
                fired["K-B"] += 1
                print("   K-B M=%d J=%d quotient %s lattice %s"
                      % (M, J, k, H[(M, J)][0]))
    print("   %d cells, %d mismatches" % (n2, mism2))

    print("\n[C3] the rank-1 closed form h(M, M-1) = C(M-1, (M-1)//2)")
    n3 = mism3 = 0
    for M in range(3, 25):
        h, v, nodes, _ = route_h(M, M - 1)
        n3 += 1
        if h != comb(M - 1, (M - 1) // 2):
            mism3 += 1
            fired["K-B"] += 1
            print("   K-B M=%d rank 1: got %d want %d"
                  % (M, h, comb(M - 1, (M - 1) // 2)))
    print("   %d cells, %d mismatches (largest %d)"
          % (n3, mism3, comb(23, 11)))

    print("\n[C4] A059753 as a cited height-1 boundary")
    n4 = mism4 = above4 = below4 = 0
    for J in range(2, min(SWEEP_J, len(A059753)) + 1):
        d1 = A059753[J - 1]
        for M in range(4, SWEEP_M + 1):
            if (M, J) not in H:
                continue
            n4 += 1
            if M > d1:
                above4 += 1
            else:
                below4 += 1
            if (H[(M, J)][0] == 1) != (M > d1):
                mism4 += 1
                fired["K-B"] += 1
                print("   K-B M=%d J=%d h=%d but d_1(%d)=%d"
                      % (M, J, H[(M, J)][0], J, d1))
    print("   %d cells (%d above the boundary confirming h = 1, %d below "
          "confirming h >= 2), %d mismatches"
          % (n4, above4, below4, mism4))

    print("\n[C5] the d_2 ladder as a cited height-2 boundary")
    n5 = mism5 = above5 = below5 = 0
    for J in range(2, len(D2) + 1):
        d2 = D2[J - 1]
        for M in range(4, SWEEP_M + 1):
            if (M, J) not in H:
                continue
            n5 += 1
            if M > d2:
                above5 += 1
            else:
                below5 += 1
            if (H[(M, J)][0] <= 2) != (M > d2):
                mism5 += 1
                fired["K-B"] += 1
                print("   K-B M=%d J=%d h=%d but d_2(%d)=%d"
                      % (M, J, H[(M, J)][0], J, d2))
    print("   %d cells (%d above the boundary confirming h <= 2, %d below "
          "confirming h >= 3), %d mismatches"
          % (n5, above5, below5, mism5))

    print("\n[C1] end-to-end parity with the parent's whole route")
    t = time.time()
    n1 = badb = badg = badh = 0
    for M in range(4, PARENT_M + 1):
        for J in range(2, min(PARENT_J, M - 1) + 1):
            n1 += 1
            Bp, Tp = PARENT.lll(basis(M, J))
            mup, Ap = gram_schmidt(Bp)
            Hp = min(max(abs(c) for c in b) for b in Bp)
            hp, vp, _ = PARENT.enumerate_ball(Bp, mup, Ap, M,
                                              F(Hp * Hp * M))
            Bn, Tn, mun, An = lll_incr(basis(M, J))
            if Bn != Bp:
                badb += 1
                fired["K-B"] += 1
            mu2, A2 = gram_schmidt(Bn)
            if mu2 != mun or A2 != An:
                badg += 1
                fired["K-B"] += 1
            if hp != H[(M, J)][0]:
                badh += 1
                fired["K-B"] += 1
                print("   K-B M=%d J=%d parent %s new %s"
                      % (M, J, hp, H[(M, J)][0]))
        print("   M = %2d done, %.1f s in" % (M, time.time() - t))
    print("   %d cells: %d bases differ, %d carried Gram-Schmidts differ, "
          "%d heights differ (%.1f s against the incremental reduction's "
          "%.1f s over the wide chart and the rank-1 control together)"
          % (n1, badb, badg, badh, time.time() - t, TIME["lll"]))

    print("\nKILLS: %s" % fired)
    print("wall %.1f s" % (time.time() - t_all))


if __name__ == "__main__":
    main()
