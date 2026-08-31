"""explore_flatten_endvalue.py -- IS THE VALUE 1 AT -1 A PROPERTY OF THE
RESIDUALS THE LATTICE EXHIBITS, OR OF THE FIVE THAT HAPPENED TO BE READ?

THE SUBJECT. Over a chart of cells (M, J), each cell's minimiser is an
integer vector of least sup norm h in a lattice, read as a polynomial.
Dividing a minimiser by its monomial factor and by every cyclotomic
factor it carries leaves a RESIDUAL R with positive leading coefficient
and no cyclotomic factor. Five residuals -- 1, and the members A, B, C,
D, E -- are all that the exhibited minimisers of 695 examined cells and
of two deep columns have ever produced, and every one of the five takes
the value 1 at x = -1. That shared end value is the front the class
block leaves open: it is read off five points, derived from nothing, and
it is what forces the value at 1 to be odd.

FIVE POINTS IS THE WHOLE OF THE EVIDENCE, AND THE REASON IS THE ROUTE
AND NOT THE OBJECT. The lattice reduction returns ONE minimiser per
cell, because the enumeration SHRINKS its radius on every improvement.
So the census that produced the five is a census of choices, one per
cell, and never of what the lattice can exhibit. explore_flatten_family
.py's arm 4 already fixes the radius at h*sqrt(M) and collects the WHOLE
minimiser set of a cell, and its record says what that buys: 405 of the
550 chart cells close, 28 of them carry two minimisers with DIFFERENT
residuals, 24 carry a minimiser whose residual leaves the unit-circle
family altogether, and over the closed cells 305 DISTINCT RESIDUAL
CLASSES appear. Those 305 were counted, sorted by how many cells carry
them, and tested for the circle -- and never once evaluated at -1.

THE QUESTION, and it is one run of a pass that already exists:

  Over every minimiser of every cell the fixed-radius pass closes, does
  the residual take the value 1 at -1?

WHY IT IS THE RIGHT ONE TO ASK FIRST. It is the cheapest thing that can
kill the pattern, and it needs no derivation: one residual with any
other value at -1 ends the reading outright, before an afternoon is
spent asking whether R(-1) = 1 is FORCED. And the population it tests is
not marginal -- 305 classes against 5 -- so a survival is a real
strengthening and not a re-reading of the same five.

THE HAND ATTACK, before any of this was coded.

(1) R(-1) CANNOT BE 0. split_witness divides out every cyclotomic factor
REPEATEDLY, so Phi_2 = x + 1 is gone from R entirely and R(-1) != 0. The
value is therefore a nonzero integer and the question is whether it is
the unit 1.

(2) THE SIGN IS A CONVENTION AND IT IS NOT THE VALUE'S. split_witness
normalises R to a POSITIVE LEADING COEFFICIENT, which fixes the sign of
R but says nothing about the sign of R(-1). So "1 at -1" and "a unit at
-1" are TWO claims, and the second can survive the first dying. Both are
frozen below as separate observables, because a run that reports only
the first cannot tell a dead pattern from a pattern about |R(-1)|.

(3) NOTHING IN THE THREAD'S BOUNDS FORCES IT. Every bound this subject
owns comes from evaluating P at a root of unity: P(z) = (z-1)^J Q(z)
with |P(z)| <= Mh gives |Q(z)| <= Mh/|z-1|^J. At z = -1 that reads
|Q(-1)| <= Mh/2^J, which is small but is an UPPER BOUND on the whole
cofactor Q and not on the residual: Q carries the cyclotomic part too,
and Phi_2 divides it at every cell where the bound bites, so Q(-1) = 0
there and the bound is discharged by the cyclotomic part alone. It
constrains R at -1 not at all. So the pattern has no derivation behind
it and the prediction below is a guess about the data.

(4) WHAT THE OFF-CIRCLE RESIDUALS LOOK LIKE, WHICH IS WHERE TO EXPECT A
KILL. A cyclotomic-free reciprocal integer polynomial with roots off the
circle carries them in pairs {z, 1/z}, so the cheapest shape it can take
is S(x) * x^deg S * S(1/x) for some S. That product's value at -1 is
S(-1) * (-1)^deg S * S(-1) = +- S(-1)^2, which is 1 only when S(-1)^2 =
1 AND the sign works out -- and is -1 whenever deg S is odd and S(-1) =
+-1. The negative slate already carries one such: 2x^2 + 5x + 2 =
(2x+1)(x+2), whose value at -1 is 2 - 5 + 2 = -1. So a residual with
value -1 is CONSTRUCTIBLE, it is exactly the shape the 24 off-circle
cells are expected to hold, and if the pattern dies it should die there
first. This is a shape argument and it claims that -1 is POSSIBLE; it
claims nothing about how many of the 305 realise it, which is why the
kills below are counts the rig PRINTS and never inferences.

(5) A TRANSPLANT, MARKED. The intuition that the value at -1 is
"multiplicative and therefore stable" is imported from the deep columns,
where every residual is a PRODUCT OF THE FIVE MEMBERS and so inherits
their end value for free. That is why the deep columns' residuals were
never independent evidence. The collected set here is NOT of that form:
its members are whatever vectors sit on the sphere of radius h*sqrt(M),
and nothing makes them products of anything. The transplant is noted so
that a survival is read as a finding and not as a restatement.

THE SLATE, frozen before any engine code.

  P1. THE EXACT-VALUE PATTERN DIES: some collected residual has R(-1)
      != 1. Predicted to FIRE, on (4).
  P2. THE UNIT PATTERN DIES TOO: some collected residual has |R(-1)| !=
      1. Predicted to FIRE, but LESS confidently than P1 -- (4) produces
      -1 cheaply and produces a large value only from an S with |S(-1)|
      > 1, which is no harder to write down but is not the shape the
      circle-leaving residuals were argued into.
  P3. THE TRIVIAL RESIDUAL DOMINATES: residual 1 is carried by more of
      the closed cells than every other class put together.
  P4. THE KILLS CONCENTRATE OFF THE CIRCLE: among the classes with
      R(-1) != 1, the fraction that leave the unit circle is higher than
      among the classes with R(-1) = 1.
  P5. THE FIVE MEMBERS ARE NOT THE COMMON CASE AMONG THE 305: A, B, C,
      D and E together account for fewer than half of the distinct
      classes the pass collects.

P6 and P7 are NOT in this list, and saying so here is the point: both
were frozen mid-run by the audit, each after the arm before it printed
and before that arm was read for the question the new one asks, and each
carries its freezing point in the design paragraph that introduces it.
A prediction written after a number exists is worth what its freezing
point is worth, so the freezing point is stated and not the pretence.

THE KILLS, as observables the rig prints and not as meanings.

  K-1. A collected residual with R(-1) != 1. The rig prints the count,
       the distinct values taken, and the extreme classes.
  K-2. A collected residual with |R(-1)| != 1.
  K-3. THE REPRODUCTION FAILS: the pass does not close 405 cells, cap
       57, leave 88 unreached, or fire K-H at 28. Any of the four
       differing means this is not the recorded pass and no comparison
       with F7's tallies is licensed.
  K-4. A CONTROL FAILS: see below.
  K-5. A residual class outside {1, A, B} at a cell of h >= 5. This
       kill and its prediction P7 were frozen in round 9 of the audit,
       after arm 5 printed and before arm 3 was read for anything about
       the members; P7 said there would be none.

THE CONTROLS. C1, C2 and C3 run and are read BEFORE any kill or survive
result. C4 CANNOT: it is a consistency test ON the collected classes and
so runs last, which makes it a check on the splitter's output and never
a licence to read the science -- the licence is C1 to C3.

  C1. THE FIVE MEMBERS, through THIS rig's evaluator, must each give 1
      at -1 -- the positive control on the arithmetic, against the
      values the class block commits to.
  C2. THE NEGATIVE CONTROL: 2x^2 + 5x + 2 must give -1, and
      (x^2+3x+1) must give -1. A rig that reports 1 everywhere because
      its evaluator cannot produce anything else is the failure this
      guards, and it is the reason the negative control is a polynomial
      the hand attack derived rather than a random one.
  C3. THE SPLITTER, re-exercised: split_witness applied to the exhibited
      minimiser of every chart cell must reproduce the census. THE SCOPE
      IS THE 550 AND NOT THE 695, which are two charts this subject keeps
      apart on purpose: the five residuals {1, A, B, C, A*B} are the 695's
      and the 550 exhibits only {1, A, B}, its 20 failing cells splitting
      16 to A and 4 to B, C and A*B living at depths past J = 20. The end
      values of those are reported separately from the collected set's,
      because they are among the five points the pattern already rests on
      and mixing them into the new population would inflate it.
  C4. THE MULTIPLICATIVITY CHECK: for every pair of collected classes
      whose product is also a collected class, the end values must
      multiply. A silent bug in the splitter that returned a residual
      missing a factor would show here.

WHAT IS AND IS NOT AT STAKE. The pass's 405 closed cells are a
measurement and not a target, and the 88 it never reaches are the
LOWEST-height cells by construction, the walk running in descending h.
So a survival is a statement about the collected classes of the closed
cells, and the low-height cells -- which is where the circle leak
already lives -- are UNDER-represented in it. A survival is therefore
weaker than it looks and a kill is exactly as strong as it looks.

THE DESIGN.

  Arm 1 rebuilds the chart: h(M, J) exactly at M = 4..40, J = 2..min(20,
  M-1), by explore_flatten_family.py's own route_h, keeping the reduced
  basis each cell returns so the second pass never reduces twice.

  Arm 2 is the recorded fixed-radius pass, cell by cell in descending h,
  the same 50,000-node cap and 4,000,000-node budget, collecting every
  vector of sup norm exactly h and splitting each into (monomial,
  cyclotomic multiset, residual). Its four coverage numbers are K-3.

  Arm 3 is this rig's own: every distinct residual class the pass
  collected, evaluated at -1, tallied by value, by circle membership and
  by how many cells carry it, with the classes off the value 1 printed
  in full. The two sub-populations the class block names are reported
  SEPARATELY as well as inside the whole -- the second residuals at the
  cells where K-H fires, and the residuals at the cells whose minimiser
  set leaves the circle -- because those are the ones an argument from
  the exhibited census cannot reach.

  Arm 4 runs C3 and C4 over the chart's exhibited residuals.

  Arm 5 was frozen AFTER arm 3 printed and BEFORE it was read for
  anything but its two kill counts, because arm 3's own P4 line makes
  the question unavoidable and the answer decides whether this is a
  death or a threshold. P4 reported the kills 163/163 off the unit
  circle against 139/142 among the survivors -- which is not a
  concentration, it is nearly everything collected being off the
  circle, and F7 confines the circle leak to cells of height 1, 2, 3
  and 6. A few very populous low-height cells (the counts run to 1,112
  minimisers) can therefore supply almost the whole class census, and
  then "163 classes" is 163 statements about a handful of cells.

  THE ARM 5 QUESTION: at what CELL HEIGHTS do the non-unit end values
  occur? It reports, per class, the heights of the cells carrying it;
  the number of cells carrying any class with R(-1) != 1 and their
  heights; and the same for the circle leak, so F7's 24 is reconciled
  against this rig's class counts rather than assumed compatible.

  P6, frozen before arm 5 ran: every class with R(-1) != 1 occurs ONLY
  at cells of height <= 6, so the pattern survives at every closed cell
  of height >= 7 and the finding is a THRESHOLD and not a death.

  Arm 6 was frozen after arm 5 printed and before arm 3's class count
  was read for anything about the MEMBERS, and its question is what the
  305 does and does not bear on. 305 classes over the 405 closed cells
  reads as evidence about which polynomials the LATTICE can exhibit,
  which is a standing open question for this class and a different one -- and the low cells' spheres are populous
  enough (232 classes at one h = 1 cell) to supply the whole census by
  themselves. So the arm asks the 297 cells where the end-value rule
  HOLDS what their whole minimiser sets exhibit, prints each class
  outside {1, A, B} with its cells, its end value, its monicity, its
  circle verdict, its divisibility over Z by A and by B, and the
  EXHIBITED residual at the cells carrying it -- that last being what
  separates a residual the collected set adds from a member the class
  was short of.

  P7, frozen before arm 6 ran: no class outside {1, A, B} at any cell of
  h >= 5, so the 305 is purely a low-height census. Predicted to HOLD,
  on the exhibited census at those cells being exactly those three.
  Predicted to HOLD, on P4 plus F7's confinement of the leak.

THE FINDINGS.

F1. THE PATTERN AS STATED IS FALSE, AND IT IS FALSE BY A WIDE MARGIN IN
CLASS COUNT (K-1 fires 163 times, K-2 83; P1 and P2 both hold). Over the
405 cells the pass closes, 305 distinct residual classes appear and the
value at -1 takes ELEVEN distinct values: -5, -4, -3, -2, -1, 1, 2, 3,
4, 5 and 7. 142 of the 305 classes give 1; 163 do not, and 83 of those
give something that is not even a unit. So "every residual the lattice
exhibits is 1 at -1" is refuted, and the refutation needed no derivation
and no new machinery -- only the radius held fixed, which arm 4 of the
parent had already done and never read at -1.

F2. AND THE CLASS COUNT IS THE WRONG DENOMINATOR, WHICH IS WHY F1 IS NOT
THE FINDING. 121 of the 163 killing classes come from ONE cell, M = 11,
J = 2, h = 1, whose ball holds 232 classes on its own. Four more cells
of height 1 carry 50, 12, 5 and 3 offending classes each, and how much
of the remaining 42 they account for is NOT read off those counts, the
same class appearing at several cells. Only 16 of the 405 closed cells
carry any class with a non-unit end value at all. A count over classes
is a count weighted by how populous a cell's sphere is, and the
low-height cells are populous by construction -- so 163 is one fact
about a handful of degenerate cells and not 163 facts about the chart.
This is why arm 5 was frozen: arm 3's P4 line reported the kills 163/163
off the circle against 139/142 among the survivors, which is not a
concentration but nearly everything collected being off the circle, and
that is the tell that the population is one or two cells' ball.

F3. WHAT REPLACES IT IS A HEIGHT THRESHOLD, AND IT IS EXHAUSTIVE (rule,
over the stated range; P6 holds and holds more sharply than it was
frozen). Every cell that carries a class with value != 1 at -1 has
height 1, 2 or 3 -- sixteen cells, the highest at h = 3. And the scope
is closed rather than assumed: the 57 cells that cap have heights 1, 2,
3 and 4 and the 88 the budget never reaches all have height 1, so EVERY
chart cell of height >= 5 is closed by the pass. There are 297 of them,
all 297 closed, and at every one of them every minimiser's residual
takes the value 1 at -1. At height >= 4 it is 315 of 317 closed and
again no exception, the two unexamined being capped cells. So the
statement that survives is:

   at every cell of the 550-cell chart with h >= 5, EVERY vector of
   least sup norm has a residual with the value 1 at -1,

exhaustively over 297 cells and over every minimiser of each, against
the five points the pattern rested on before this run. The pattern was
not five coincidences; it was a rule stated without its hypothesis.
(SETTLED SINCE, by explore_flatten_recur.py: the threshold is h >= 4,
the two capped cells above having closed at a raised cap, and the range
is the 695-cell chart's 462 such cells. What survives here unchanged is
this scope -- the 550-cell chart, 297 cells, this pass's own cap.)

F4. LEAVING THE CIRCLE DOES NOT COST THE END VALUE, AND THAT SEPARATES
TWO PROPERTIES THE THREAD HAD ONLY EVER SEEN TOGETHER (observation, on
the 24 leaking cells). The 24 closed cells whose minimiser set leaves
the unit-circle family have heights 1, 2, 3 and 6 -- reproducing F7 of
the parent exactly -- while the 16 that lose the end value have heights
1, 2 and 3. The cells at h = 6 therefore leak off the circle and keep
R(-1) = 1. So the circle membership and the end value are independent
properties of a residual, and E -- the one minted member with roots off
the circle, whose value at -1 is 1 -- is not the exception it looked
like but the first instance of a separation the chart shows at h = 6
too -- F8 names the polynomial that shows it there.

F5. THE TWO SUB-POPULATIONS THE AIM NAMED ARE NOT THE POPULATION, AND
THE PROJECTION THAT SIZED THEM WAS AN ORDER OF MAGNITUDE LOW. The move
was scoped in advance as "the second residuals at the 28 two-minimiser
cells plus the off-class minimisers at the 24" -- tens of new points.
What the pass actually collects is 305 classes over 405 cells and 995
cell-incidences, because a cell's minimiser SET is not two vectors: the
counts run to 1,112 below h = 10. The projection was made from the K-H
count, which counts cells where the residuals DIFFER and never how many
each cell has. The species is a population sized from a register that
counts events rather than members.

F5b. P4 HOLDS AND IS WORTH ALMOST NOTHING, WHICH IS ITSELF THE READING.
The prediction was that the classes with a non-unit end value leave the
unit circle more often than those with value 1. They do -- 163 of 163
against 139 of 142 -- and the margin is 100% against 97.9%, because
nearly EVERYTHING the pass collects is off the circle. So the prediction
is confirmed by a comparison whose two sides barely differ, and what it
actually reports is that circle membership does not discriminate here at
all. That is the observation arm 5 was frozen on, and F4 is where the
two properties are separated by something that does discriminate: the
height.

F6. WHAT THE FIVE MEMBERS DO IN THE COLLECTED SET (P5 holds). Only A and
B appear among the 305 -- A at 19 cells, B at 5, three and one more than
the exhibited witnesses reported -- and C, D and E are not collected at
all, and for two different reasons: C's single census cell is inside the
695 but at a depth past J = 20, which is exactly why the 550's exhibited
census is {1, A, B} where the 695's is five, while D and E were minted
at M = 54 and M = 62 and lie outside the census altogether. So the members are 2 of 305
classes, and the class the lattice exhibits at these heights is
overwhelmingly the trivial residual: 385 of the 405 closed cells carry
1, against 610 cell-incidences for everything else combined. WHERE those
610 sit is not printed -- the arm tallies incidences by residual class
and by end value, never by the height of the cell they came from -- so
the concentration F2 reads off the KILLING classes is not asserted here
for the non-trivial classes at large (P3 holds).

F7. THE CONTROLS. C1: all five members give 1 at -1 through this rig's
own evaluator. C2: 2x^2 + 5x + 2, which the hand attack derives as
(2x+1)(x+2), and x^2 + 3x + 1, which is irreducible but reciprocal with
its two roots (-3 +- sqrt 5)/2 a reciprocal pair OFF the circle -- the
same phenomenon without the rational split -- both give -1,
so a rig that can only print 1 is excluded -- and the shape argument
behind them is confirmed by the data, the two commonest killing classes
being 1 + x + x^3 and 1 + x + x^2 + x^3 + x^5, tied at 9 cells and both
of value -1. C3: the splitter reproduces the
chart census exactly, three residuals over the 550 exhibited minimisers
-- 1 at 530, A at 16, B at 4 -- and all three are 1 at -1, which is the
old evidence restated and kept out of the new population. C4: 119
collected pairs have their product also collected, and the end value
multiplies at all 119. K-3 clear: 405 closed, 57 capped, 88 unreached,
K-H at 28, the parent's four coverage numbers reproduced exactly, which
is what licenses reading F4 against the parent's F7.

F8. THE HIGH CELLS EXHIBIT A FOURTH CLASS, AND P7 IS FALSE (K-5 fires
once; the arm was frozen after arm 5 printed and before arm 3's class
count was read for anything about the members). The 305 is a class
count over ALL 405 closed cells, and it sits in the doc beside an open
question about what the LATTICE exhibits, so the two get read for each
other. Asking the 297 cells where the end-value rule HOLDS what their
whole minimiser sets exhibit was meant to show the 305 is purely a
low-height census. It very nearly is -- four classes over the 297 -- but
not entirely, and the fourth is

   1 + 2x + 4x^2 + 5x^3 + 4x^4 + 2x^5 + x^6,

MONIC, degree 6, reciprocal, carrying no cyclotomic factor by
construction, value 1 at -1 and 19 at 1, divisible over Z by neither A
nor B, and with roots OFF the unit circle -- which Kronecker forces
rather than merely permits, a monic cyclotomic-free integer polynomial
with nonzero constant term being unable to have all its roots on the
circle. It appears at exactly ONE cell, M = 18, J = 8, h = 6, which is
the h = 6 leak F4 already isolated: the cell that leaves the circle and
keeps the end value is this polynomial's. So F4's separation has a name.

WHAT IT IS AND IS NOT. It is a residual the lattice exhibits at a cell
above the threshold and outside everything this thread has catalogued --
and being MONIC settles that against all five members at once, with no
computation: every member has leading coefficient at least 2, so every
product of members is non-monic and a monic residual is neither.
It is NOT a minted member: a member is minted where the class in hand
cannot reach h, and this is read off a minimiser the reduction never
returned -- the exhibited witness at M = 18, J = 8 splits to 1, which
the arm prints beside the class. That makes
it the first object of its kind in the corpus, and the distinction is
the same one the exhibited census and the collected set have carried all
along. Whether it belongs in the member class is a question about the
minimiser SET's residuals, which nothing in the corpus has asked;
it is stated here as what it is, one polynomial at one cell
(observation; the divisibility and the circle verdict are exact).
(SETTLED SINCE, by explore_flatten_recur.py: it does NOT recur -- one
cell in 442 over the widened chart -- and it is irreducible over Z. The
high band's census is six classes there and not four, the two this arm
could not see being C and A*B, which live past depth 20. One cell and
the four classes are this chart's and stand.)

AND THE DIVISIBILITY TEST WAS WRONG THE FIRST TIME IT PRINTED. The arm
first reported the sextic divisible by BOTH A and B, which is
arithmetically impossible over Z -- A is non-monic with leading
coefficient 2 and cannot divide a monic polynomial there -- because it
called poly_exact_div, which divides over the RATIONALS and is the
splitter's tool for its Sturm work. polydiv is the integer one, and it
answers False to both. The impossible answer is what caught it, not a
reading of the code: the number said what no arithmetic allows.

WHAT THIS LEAVES FOR THE DERIVATION. The front is not closed and it is
better posed: R(-1) = 1 is now a rule with a hypothesis, and any
derivation of it must CONSULT THE HEIGHT, because the statement is false
at h <= 3 and the failures are not marginal there. That is a strong
constraint on the shape of a proof and it was not available before this
run -- the (x+1)-side bound |Q(-1)| <= Mh/2^J and the primitivity of the
minimiser are both height-free, so neither can be the whole argument.

RUN RECORD (final run: wall 128.0 s, peak working set 89.3 MB, peak
commit 84.1 MB under memwatch's 512 MB default -- exact rational
arithmetic over the reduced bases the chart pass already returns, plus
one cell's collected vectors, the largest being the 232-class ball at
M = 11, so the memory line was never in question). The estimate was 150
to 200 s and the wall is 129, of which 22.4 s is the chart and 106.7 s
the fixed-radius pass; the pass is the parent's and its cost is the
parent's.

TWELVE runs. None of the first six changed a number that survived
into the findings.
The FIRST was a smoke run at M <= 12, which exists because the arms
below the chart cannot be exercised any other way without paying the
full pass, and it caught nothing -- both controls passed and the shape
of every arm printed. The SECOND is the one arms 1 to 4 report and it
printed F1, F2's class counts, F5, F6 and F7. The THIRD added arm 5,
frozen on its own question after the second printed its kill counts and
before its P4 line was read for anything else, and it is where the
threshold appeared. The FOURTH added the scope line and the two height
censuses, because the third stated the threshold over the CLOSED cells
and could not say whether an unexamined cell sat above it -- which is
the difference between "no closed cell above h = 3 fails" and the rule
F3 states. The FIFTH changed no arithmetic at all: the audit smoke-ran
every arm at M <= 12 and at a zero node budget and found two REPORTING
faults that fire only off the shipped range -- the leak line comparing
its own count to the parent's whole-sweep 24 unconditionally, and the
P6 line reading `hi or 0` when no cell fails, which turns "above the
highest failing height" into "above zero" and makes a vacuous sentence
true by accident. Both are gated now, the first on K-3, which is the
rig's own test of whether this IS the recorded pass; and the height
census names the chart's own cell count so the threshold cannot be read
at a scope the run did not have. Every number arms 1 to 5 print is
identical in the second, third, fourth and fifth: 550 cells, three
exhibited residuals, 405/57/88/28, 305 classes, eleven values, 163 and
83, 119 multiplicative pairs, 16 failing cells at heights 1, 2 and 3,
24 leaking at 1, 2, 3 and 6, and 297 of 297 closed at h >= 5. The SIXTH is the audit's second, and it closed an ABSENCE rather
than an error: C3 was declared a control and wired to no kill, so a
disagreeing census would have printed beside a clean KILLS line. It now
asserts the 550's own census -- {1: 530, A: 16, B: 4}, all three 1 at
-1 -- and reports itself UNEXERCISED at any other range rather than
comparing a narrowed sweep to the shipped chart's answer key, which is
the fault the fifth run fixed one line further down. It passes. Every
number arms 1 to 5 print is identical in runs two through six: 550
cells, three exhibited residuals, 405/57/88/28, 305 classes, eleven
values, 163 and 83, 119 multiplicative pairs, 16 failing cells at
heights 1, 2 and 3, 24 leaking at 1, 2, 3 and 6, and 297 of 297 closed
at h >= 5.

The SEVENTH, EIGHTH and NINTH are the audit's third pass and they added
arm 6, which is where the science moved rather than the reporting. The
seventh printed the fourth class and fired K-5. The eighth added the
class's own properties and reported it divisible by A and by B, which is
impossible over Z and is the bug F8's last paragraph names. The ninth divides over Z. The TENTH and ELEVENTH close the
gap the audit found next: F8 said the carrying cell's own witness splits
to 1, which is the whole of why the sextic is not a minted member, and
NOTHING PRINTED IT -- the number was checked by hand outside the rig,
which is the state the two-write mint exists to prevent. The tenth put
P7 and arm 6 into the slate and the design where P1 to P6 already stood,
with their freezing points stated rather than hidden; the eleventh
prints the exhibited residual at every carrying cell, and it is [1], so
F8's clause now reads off this rig. The TWELFTH is the audit's last
and adds one number to a print rather than to the findings: F5 quoted
995 cell-incidences, which was the sum of eleven printed rows and of
385 + 610, correct both ways and greppable in neither. The arm prints
it. Nothing else moved. Arms 1 to 5 print in the seventh,
eighth and ninth exactly what they printed in the second: nothing arm 6
asks changes anything an earlier arm computes, arm 6 reading HEIGHTS_OF
and SPLIT after the pass has closed. Only the wall moves, by a second or two.
That is the only reproduction claimed here.
"""
import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_flatten_offchart import NodeCap
# lll_incr and basis are NOT imported: the reduction is route_h's and
# this rig keeps what it returns rather than reducing a second time,
# which is the one thing it changes about the parent's pass.
from explore_flatten_family import (SWEEP_M, SWEEP_J, COUNT_CAP,
                                    COUNT_BUDGET, route_h, enum_ball,
                                    split_witness, on_unit_circle,
                                    poly_trim, polydiv)

A_POLY = [2, 4, 5, 4, 2]
B_POLY = [2, 3, 2]
C_POLY = [3, 5, 3]
D_POLY = [3, 9, 15, 17, 15, 9, 3]
E_POLY = [3, 11, 24, 37, 43, 37, 24, 11, 3]
MEMBERS = [("A", A_POLY), ("B", B_POLY), ("C", C_POLY),
           ("D", D_POLY), ("E", E_POLY)]

# the two the hand attack derived, and what it says they must give
NEGATIVE = [([2, 5, 2], -1), ([1, 3, 1], -1)]

# F7's recorded coverage -- K-3 is these four numbers
WANT = {"closed": 405, "capped": 57, "unreached": 88, "KH": 28}


def at_minus_1(p):
    """The value of an integer polynomial, low degree first, at -1."""
    return sum(c * (-1) ** i for i, c in enumerate(p))


def mulpoly(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r


def main():
    t_all = time.time()
    fired = {"K-1": 0, "K-2": 0, "K-3": 0, "K-4": 0, "K-5": 0}

    # ------------------------------------------------- the controls
    print("[C1] the five members through this rig's evaluator")
    for nm, p in MEMBERS:
        v = at_minus_1(p)
        print("   %-2s %-34s at -1: %3d %s"
              % (nm, str(p), v, "ok" if v == 1 else "CONTROL FAILED"))
        if v != 1:
            fired["K-4"] += 1

    print("[C2] the negative control -- the evaluator must NOT say 1")
    for p, want in NEGATIVE:
        v = at_minus_1(p)
        print("   %-16s at -1: %3d (want %d) %s"
              % (str(p), v, want, "ok" if v == want else "CONTROL FAILED"))
        if v != want:
            fired["K-4"] += 1

    # --------------------------------------------- arm 1: the chart
    print("\n[arm 1] the chart -- h(M, J), M = 4..%d, J = 2..%d"
          % (SWEEP_M, SWEEP_J))
    t = time.time()
    H, RED = {}, {}
    for M in range(4, SWEEP_M + 1):
        for J in range(2, min(SWEEP_J, M - 1) + 1):
            try:
                h, v, _, red = route_h(M, J)
            except NodeCap:
                print("   stalled at M=%d J=%d" % (M, J))
                continue
            H[(M, J)] = (h, v)
            RED[(M, J)] = red
    print("   %d cells decided, %.1f s" % (len(H), time.time() - t))

    # ------------------------------ arm 4a: C3, the exhibited census
    print("\n[C3] the splitter over the exhibited minimisers")
    SPLIT = {}
    exh = {}
    for c in sorted(H):
        sh, cyc, res = split_witness(H[c][1])
        SPLIT[c] = (sh, cyc, res)
        exh.setdefault(res, 0)
        exh[res] += 1
    print("   %d distinct exhibited residuals over %d cells:"
          % (len(exh), len(H)))
    for r in sorted(exh, key=lambda r: -exh[r]):
        print("      %-30s %3d cells, at -1: %3d, circle %s"
              % (str(list(r))[:30], exh[r], at_minus_1(list(r)),
                 on_unit_circle(list(r))[0]))
    bad = [r for r in exh if at_minus_1(list(r)) != 1]
    print("   exhibited residuals with value != 1 at -1: %d %s"
          % (len(bad), [list(r) for r in bad]))
    # A CONTROL WITH NO KILL WIRED TO IT IS A PRINT. C3 asserts the
    # splitter reproduces the census this subject already owns, at the
    # SHIPPED range only -- at a narrowed one the census is a different
    # chart's and the control reports itself unexercised rather than
    # failing. WANT is the 550's own: {1: 530, A: 16, B: 4}.
    if len(H) != 550:
        print("   C3 unexercised: the census is the 550-cell chart's and "
              "this sweep decided %d" % len(H))
    else:
        want = {(1,): 530, tuple(A_POLY): 16, tuple(B_POLY): 4}
        if exh != want or bad:
            fired["K-4"] += 1
            print("   C3 FAILED: census %s, want %s, non-unit end values %d"
                  % ({str(list(k)): v for k, v in exh.items()},
                     {str(list(k)): v for k, v in want.items()}, len(bad)))
        else:
            print("   C3 ok: the census is exactly {1: 530, A: 16, B: 4} "
                  "and all three are 1 at -1")

    # ------------------------------- arm 2: the fixed-radius pass
    print("\n[arm 2] the fixed-radius pass -- the whole minimiser set")
    t = time.time()
    order = sorted(H, key=lambda c: (-H[c][0], c[0], c[1]))
    spent = closed = capped = 0
    kh = 0
    setres = {}          # class -> [cells carrying it, off-circle flag]
    HEIGHTS_OF = {}      # cell -> the set of classes its minimisers give
    CAPPED = []          # the cells whose ball outruns the node cap
    khres = {}           # class -> cells, restricted to K-H cells
    offres = {}          # class -> cells, restricted to leaking cells
    for c in order:
        M, J = c
        h = H[c][0]
        if spent >= COUNT_BUDGET:
            break
        B, mu, A = RED[c]
        got = []
        try:
            _, _, nodes = enum_ball(B, mu, A, M, F(h * h * M), COUNT_CAP,
                                    collect=got)
            spent += nodes
            mins = [w for w in got if max(abs(x) for x in w) == h]
            closed += 1
            res = set(split_witness(w)[2] for w in mins)
            if len(res) > 1:
                kh += 1
            HEIGHTS_OF[c] = res
            leak = any(not on_unit_circle(list(r))[0] for r in res)
            for r in res:
                setres.setdefault(r, [0, 0])
                setres[r][0] += 1
                if not on_unit_circle(list(r))[0]:
                    setres[r][1] = 1
                if len(res) > 1:
                    khres[r] = khres.get(r, 0) + 1
                if leak:
                    offres[r] = offres.get(r, 0) + 1
        except NodeCap:
            spent += COUNT_CAP
            capped += 1
            CAPPED.append(c)
    unreached = len(H) - closed - capped
    print("   %d closed, %d capped, %d unreached, K-H at %d cells, %.1f s"
          % (closed, capped, unreached, kh, time.time() - t))
    got4 = {"closed": closed, "capped": capped, "unreached": unreached,
            "KH": kh}
    for k in WANT:
        if got4[k] != WANT[k]:
            fired["K-3"] += 1
            print("   K-3 %s: %d, the record says %d" % (k, got4[k], WANT[k]))
    if not fired["K-3"]:
        print("   K-3 clear: the pass reproduces F7's four coverage numbers")

    # ---------------------------- arm 3: the end value over the set
    print("\n[arm 3] the value at -1 over every collected residual class")
    vals = {}
    for r in setres:
        v = at_minus_1(list(r))
        vals.setdefault(v, []).append(r)
    print("   %d distinct residual classes over %d cell-incidences; "
          "value at -1 -> class count:"
          % (len(setres), sum(v[0] for v in setres.values())))
    for v in sorted(vals):
        cells = sum(setres[r][0] for r in vals[v])
        off = sum(1 for r in vals[v] if setres[r][1])
        print("      %6d : %4d classes, %5d cell-incidences, %d off circle"
              % (v, len(vals[v]), cells, off))
    off1 = [r for r in setres if at_minus_1(list(r)) != 1]
    if off1:
        fired["K-1"] += len(off1)
    nonunit = [r for r in setres if abs(at_minus_1(list(r))) != 1]
    if nonunit:
        fired["K-2"] += len(nonunit)
    print("   K-1: %d classes with value != 1 at -1" % fired["K-1"])
    print("   K-2: %d classes with |value| != 1 at -1" % fired["K-2"])
    for r in sorted(off1, key=lambda r: (-setres[r][0], len(r)))[:20]:
        print("      %-40s %3d cells, at -1: %4d, circle %s"
              % (str(list(r))[:40], setres[r][0], at_minus_1(list(r)),
                 on_unit_circle(list(r))[0]))

    # P4: are the kills concentrated off the circle?
    def frac_off(rs):
        return (sum(1 for r in rs if setres[r][1]), len(rs))
    k_off, k_n = frac_off(off1)
    s_off, s_n = frac_off([r for r in setres if at_minus_1(list(r)) == 1])
    print("   P4: off-circle share among value != 1: %d/%d; among value "
          "= 1: %d/%d" % (k_off, k_n, s_off, s_n))

    # P3: does residual 1 dominate the cells?
    one = setres.get((1,), [0, 0])[0]
    print("   P3: residual 1 carried by %d of the %d closed cells; every "
          "other class together %d cell-incidences"
          % (one, closed, sum(setres[r][0] for r in setres if r != (1,))))

    # P5: how many of the 305 ARE the five members. Membership only --
    # products of members are not counted here and the finding says so,
    # because a product of members is a member for free and counting
    # them would inflate the answer with nothing new.
    known = set()
    for nm, p in MEMBERS:
        known.add(tuple(p))
    print("   P5: the five members appear as %d of the %d classes; the "
          "classes carrying each:" % (len(known & set(setres)), len(setres)))
    for nm, p in MEMBERS:
        r = tuple(p)
        print("      %-2s %s" % (nm, ("%d cells" % setres[r][0])
                                 if r in setres else "not collected"))

    # the two named sub-populations, reported on their own
    for label, pop in (("K-H cells (two residuals at one cell)", khres),
                       ("cells whose minimiser set leaves the circle",
                        offres)):
        bad = [r for r in pop if at_minus_1(list(r)) != 1]
        print("   %s: %d classes, %d with value != 1 at -1 %s"
              % (label, len(pop), len(bad),
                 [list(r) for r in sorted(bad, key=lambda r: len(r))[:6]]))

    # ------------------------- arm 5: at what heights do the kills sit
    print("\n[arm 5] the cell heights behind the non-unit end values")
    killcells = sorted(set(c for c in HEIGHTS_OF
                           for r in HEIGHTS_OF[c]
                           if at_minus_1(list(r)) != 1))
    leakcells = sorted(set(c for c in HEIGHTS_OF
                           for r in HEIGHTS_OF[c]
                           if not on_unit_circle(list(r))[0]))
    print("   %d of the %d closed cells carry a class with value != 1 at "
          "-1; their heights: %s"
          % (len(killcells), closed,
             sorted(set(H[c][0] for c in killcells))))
    # A WHOLE-SWEEP RECORD IS NOT COMPARABLE TO A NARROWED SWEEP'S COUNT.
    # F7's 24 is the shipped range's; at any other range the comparison
    # is meaningless and saying it anyway is how a narrowed smoke run
    # reads as a contradiction. K-3 is exactly the test of whether this
    # IS the recorded pass, so the parenthetical is gated on it.
    print("   %d closed cells leak off the circle%s; their heights: %s"
          % (len(leakcells),
             " (F7 records 24)" if not fired["K-3"] else
             " (F7's 24 is the shipped range's and does not compare here)",
             sorted(set(H[c][0] for c in leakcells))))
    unre = [c for c in H if c not in HEIGHTS_OF and c not in CAPPED]
    print("   THE SCOPE OF WHAT SURVIVES: the %d capped cells have heights "
          "%s and the %d unreached have heights %s -- an unexamined cell "
          "of height above 3 would narrow the surviving statement"
          % (len(CAPPED), sorted(set(H[c][0] for c in CAPPED)),
             len(unre), sorted(set(H[c][0] for c in unre))))
    for lo in (4, 5):
        tot = [c for c in H if H[c][0] >= lo]
        cl = [c for c in tot if c in HEIGHTS_OF]
        # the chart size is named on the line so the threshold cannot be
        # read at a scope the run did not have
        print("   of the %d-cell chart, %d cells have height >= %d, of "
              "which %d closed by the pass, %d carrying a class with "
              "value != 1 at -1"
              % (len(H), len(tot), lo, len(cl),
                 sum(1 for c in cl if any(at_minus_1(list(r)) != 1
                                          for r in HEIGHTS_OF[c]))))
    hi = max((H[c][0] for c in killcells), default=None)
    if hi is None:
        # NO KILL AT ALL is a different sentence, and `hi or 0` would
        # silently turn it into "above height 0" -- true by accident and
        # not by design, which is the shape this line must not take.
        print("   P6: no closed cell carries a non-unit end value at this "
              "range, so there is no threshold to report")
    else:
        print("   P6: the highest cell carrying a non-unit end value is "
              "h = %d; closed cells of height above it: %d, all with every "
              "collected residual at 1"
              % (hi, sum(1 for c in HEIGHTS_OF if H[c][0] > hi)))
    for c in sorted(killcells, key=lambda c: -H[c][0])[:10]:
        bad = [r for r in HEIGHTS_OF[c] if at_minus_1(list(r)) != 1]
        print("      M=%2d J=%2d h=%-4d %3d classes, %3d of them != 1 at -1"
              % (c[0], c[1], H[c][0], len(HEIGHTS_OF[c]), len(bad)))

    # ------------- arm 6: what the HIGH cells exhibit, on its own
    # FROZEN AFTER ARM 5 AND BEFORE ANY OF THIS PRINTED. The class
    # count 305 sits next to an open question -- whether the class the
    # LATTICE exhibits is finitely generated -- and a reader takes one
    # for evidence about the other. It may be neither: the low cells
    # spheres are populous enough to supply the whole census by
    # themselves. So ask the cells where the end-value rule HOLDS what
    # they exhibit. K-5 is a class outside {1, A, B} at a cell of
    # h >= 5; P7 says there is none, on the exhibited census at those
    # cells being exactly those three.
    print("\n[arm 6] the classes the h >= 5 cells exhibit")
    hi5 = [c for c in HEIGHTS_OF if H[c][0] >= 5]
    seen5 = set()
    for c in hi5:
        seen5 |= HEIGHTS_OF[c]
    base3 = {(1,), tuple(A_POLY), tuple(B_POLY)}
    extra = sorted(seen5 - base3, key=len)
    print("   %d cells at h >= 5 exhibit %d distinct classes; outside "
          "{1, A, B}: %d" % (len(hi5), len(seen5), len(extra)))
    if extra:
        fired["K-5"] = len(extra)
        for r in extra[:10]:
            at = [c for c in hi5 if r in HEIGHTS_OF[c]]
            ok, why, _Q, _n, _d = on_unit_circle(list(r))
            # polydiv, NOT poly_exact_div: the latter divides over the
            # RATIONALS and answered "divisible by A" for a monic
            # sextic, which A cannot divide over Z at all -- its
            # leading coefficient is 2. The impossible answer is what
            # caught it.
            byA = polydiv(list(r), A_POLY) is not None
            byB = polydiv(list(r), B_POLY) is not None
            print("      %s" % (list(r),))
            print("         at -1: %d, at 1: %d, monic: %s, circle: "
                  "%s (%s), divisible over Z by A: %s, by B: %s"
                  % (at_minus_1(list(r)), sum(r), r[-1] == 1, ok, why,
                     byA, byB))
            print("         cells at h >= 5 carrying it: %s"
                  % ([(c[0], c[1], H[c][0]) for c in at],))
            # THE EXHIBITED RESIDUAL AT THOSE CELLS IS THE WHOLE OF why
            # this is not a minted member: a member is minted where the
            # class in hand cannot reach h, and a cell whose own witness
            # splits to 1 never asked for one. Printed, not asserted.
            print("         their EXHIBITED residuals: %s"
                  % ([list(SPLIT[c][2]) for c in at],))
    else:
        print("   K-5 clear: the high cells' whole minimiser set is "
              "exactly {1, A, B}, so the 305 is a low-height census")
    # ------------------------------------ arm 4b: C4, multiplicativity
    print("\n[C4] multiplicativity over collected pairs")
    idx = set(setres)
    n4 = ok4 = 0
    for r1 in sorted(idx, key=len)[:60]:
        for r2 in sorted(idx, key=len)[:60]:
            p = tuple(poly_trim(mulpoly(list(r1), list(r2))))
            if p in idx:
                n4 += 1
                if at_minus_1(list(p)) == (at_minus_1(list(r1))
                                           * at_minus_1(list(r2))):
                    ok4 += 1
                else:
                    fired["K-4"] += 1
    print("   %d collected pairs whose product is also collected, %d "
          "multiply correctly at -1" % (n4, ok4))

    print("\nKILLS: %s" % fired)
    print("wall %.1f s" % (time.time() - t_all))


if __name__ == "__main__":
    main()
