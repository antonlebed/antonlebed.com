"""explore_flatten_deep.py -- IS THE MEMBERS' VALUE AT 1 THE PATTERN,
OR IS IT THE VALUE AT -1?

explore_flatten_class.py walked ranks 19..26, took each column's first
failing cell and then its next three, and minted two members past the
chart's own three: D at rank 22 depth 30 and E at rank 22 depth 32 and
again at rank 26 depth 36. That rig's docstring records, as suggestive
and unproved, that A(1) = 17, B(1) = 7, C(1) = 11 and D(1) = 71 are all
prime; E(1) = 193 made it five for five. The reading offered was that
minimality might FORCE a member's value at 1 to admit no nontrivial
factorisation, which would make primality a consequence and would
PREDICT the next member where the walk only finds one.

THIS RIG IS THE TEST, AND IT IS TWO QUESTIONS AT ONE COST. The first is
the aimed one: does a deeper sweep of ONE column -- rank 22, the column
that has minted twice -- past the depth E was found at produce a SIXTH
member, and what is its value at 1. The second is what the hand attack
below turned up on the way, which is a different and tighter pattern at
the OTHER end of the interval, and the same run decides it.

(The senses are the thread's, restated because this rig is read alone.
A vector c on M atoms is the polynomial P(x) = sum_i c_i x^i; its
FLATTENING is the multiplicity of the root 1; its HEIGHT is the sup norm
max_i |c_i|. h(M, J) is the least height of a nonzero P with flattening
at least J and degree < M. A PURE PRODUCT is prod_i (x^{d_i} - 1) over a
multiset of positive PARTS; ph(M, J) is the least height of a pure
product admissible at the cell. RANK is always r = M - J. A cell FAILS
when h < ph. The COFACTOR of a lattice vector is q = P/(x-1)^J, and it
splits as a monomial times a sign times a product of cyclotomics times a
RESIDUAL R carrying no cyclotomic factor. A MEMBER is a residual, or a
factor of one, that no product of the members already in hand can make.
The SWAP FAMILY at a cell is every admissible pure cofactor with a
sub-multiset of its own cyclotomic blocks traded for an equal-degree
product of class members, and hs is its least height. h <= hs <= ph
always.)

THE HAND ATTACK, worked on paper before any engine code, and it moved
the question.

FIRST, THE FIVE MEMBERS AT BOTH ENDS OF THE INTERVAL.

    A = [2,4,5,4,2]                  A(1) = 17    A(-1) = 1
    B = [2,3,2]                      B(1) = 7     B(-1) = 1
    C = [3,5,3]                      C(1) = 11    C(-1) = 1
    D = [3,9,15,17,15,9,3]           D(1) = 71    D(-1) = 1
    E = [3,11,24,37,43,37,24,11,3]   E(1) = 193   E(-1) = 1

The value at -1 is 1 at all five, exactly, and nothing in this corpus
has written that down. It is also what the "extremal" look of B and C
actually is: a reciprocal [c0, c1, c0] has R(-1) = 2c0 - c1, so R(-1) =
1 forces c1 = 2c0 - 1, which is B at c0 = 2 and C at c0 = 3, and reading
those off as "c1 as large as the unit circle allows" is the same line
seen from the side.

SECOND, THE VALUE AT -1 IMPLIES ODDNESS AT 1 AND NOTHING MORE. R(1) and
R(-1) differ by twice the odd-index coefficient sum, so R(-1) = 1 forces
R(1) ODD. That is the whole of what the visible structure delivers at 1,
and it is what deflates the primality reading: the five primes are five
ODD numbers whose oddness was forced, and what is left to explain is the
primality of five odd numbers of sizes 7, 11, 17, 71 and 193. At the
prime density among odd numbers, 2/ln n, that is about 1.0 * 0.83 *
0.71 * 0.47 * 0.38, near one in eight by chance. Five points were never
evidence; after the oddness they are an eighth of one.

THIRD, THERE IS NO EVALUATION CONSTRAINT AT 1 AT ALL, WHICH IS THE
REASON. Every lower bound this subject has comes from evaluating P at a
root of unity: P(z) = (z-1)^J Q(z) with |P(z)| <= M*h forces |Q(z)| <=
M*h / |z-1|^J, which at z = -1 is the (x+1) | Q that every deep cell
obeys. At z = 1 the flattening IS the constraint and P(1) = 0 says
nothing whatever about the cofactor. The only statement available at 1
is an upper bound -- writing x = 1+u, Q(1) is the coefficient of u^J in
P(1+u), so Q(1) = sum_k C(k,J) c_k and |Q(1)| <= h*C(M, J+1) -- and an
upper bound on a value cannot force that value to be prime.

FOURTH, AND DECISIVELY, THE AMBIENT CLASS IS NOT PRIMALITY-CONSTRAINED,
BY CONSTRUCTION. Take

    W_c = [c, 2c-1, c],   c >= 2.

Reciprocal by inspection. Reduced through y = x + 1/x it is c*y + 2c-1,
whose single root -(2c-1)/c lies in (-2, 2) for every c >= 2, so BOTH
roots lie on the unit circle. Its discriminant (2c-1)^2 - 4c^2 = 1 - 4c
is negative for every c, so it is irreducible over Q. Its content
gcd(c, 2c-1) = gcd(c, -1) = 1, so it is primitive. It is non-monic, so
by Kronecker it is not cyclotomic, and being irreducible of degree 2 it
carries no cyclotomic factor either. W_2 = B and W_3 = C. So the
members' own ambient class -- integer polynomials, non-monic, primitive,
no cyclotomic factor, every root on the unit circle -- holds an INFINITE
one-parameter family at its LOWEST degree, and

    W_c(1) = 4c - 1,   W_c(-1) = 1,

which is composite at c = 4 (15), 7 (27), 9 (35), 10 (39), 13 (51) and
on. W_4 = [4,7,4] is member-shaped in every respect the corpus checks,
of height 7 -- between C's 5 and D's 17 -- with a composite value at 1.
So no law about the CLASS can force primality, and what survives of the
hunch is only a claim about NEED: that the lattice never exhibits such a
member. No derivation reaches that, which is what leaves the sweep as
the test. The same construction says something the thread has been
reading the other way round: the scarcity of members is the LATTICE's
and never the class's, so "finitely generated" is only ever a question
about what the lattice exhibits.

FIFTH, FOUR OF THE FIVE ARE IRREDUCIBLE, WHICH THE PARENT RIG RECORDS
THAT IT COULD NOT ESTABLISH AND MEASURES ITS WAY AROUND. THE DESCENT
NEEDS ALL ROOTS ON THE CIRCLE AND NOT MERELY RECIPROCITY, which is the
step it is easy to skip. On the circle conjugation and inversion agree,
so an irreducible factor's reciprocal is its complex conjugate, which
for real coefficients is the factor itself: every irreducible factor is
SELF-reciprocal. One of ODD degree would have -1 as a root, and all five
give 1 there, so every factor has even degree and descends to a
factorisation of S in y = x + 1/x. Hence R is irreducible exactly when S
is -- FOR A CLASS MEMBER WITH ALL ROOTS ON THE CIRCLE. B and C give S
linear. A gives S = 2y^2+4y+1, discriminant 8, not a square. D gives S =
3y^3+9y^2+6y-1, whose four rational-root candidates evaluate to 17, -1,
19/9 and -19/9, and a cubic with no rational root is irreducible. So A,
B, C and D are irreducible over Q. E IS NOT COVERED and the gap is
exactly the hypothesis above: four of its eight roots are OFF the
circle, so it could in principle be an irreducible quartic times that
quartic's reciprocal, a factorisation the descent cannot see, while S
stays irreducible. And S_E is irreducible -- 3y^4+11y^3+12y^2+4y+1 has
no rational root by the same four candidates (31, 1, 4.11, 0.63), and a
split (3y^2+ay+b)(y^2+cy+d) forces bd = 1, hence b = d = +-1, hence a+c
= 4 with 3c+a = 11 or a+c = -4 with 3c+a = 11, neither having an integer
solution -- which settles the descent's half and NOT E. So the greedy
division by A, B, C and D is well defined rather than merely measured to
be, E's own irreducibility is left where the walk had it, and the
permutation control stays the ground under that one.

SIXTH, WHAT THE SWEEP IS AND WHY THIS COLUMN. The parent rig's ARM 3
took three failing cells per column across eight columns and found E
twice, so depth in ONE column is where a sixth would show, and rank 22
is the column that has minted twice. The scan resumes at the depth after
E's, runs the same capped route_h, and examines every failing cell
against the class {A, B, C, D, E} by the parent rig's own code, imported
rather than restated so that no second copy of the walk can drift from
the first.

SEVENTH, THE TRANSPLANT, MARKED. The intuition that a member RECURS is
read off E at two ranks, and it is being carried here to further cells
of ONE rank. That is a different object: E's recurrence is evidence
about ranks and says nothing about what a single column does as it
deepens.

THE PREDICTIONS, fixed here before the engine ran.

P1. THE COLUMN MINTS AGAIN. At least one decided failing cell of rank
    22 between depth 33 and J_CAP has a residual the class {A, B, C, D,
    E} cannot make.
P2. ANY MEMBER MINTED HAS VALUE 1 AT -1. The pattern at the far end of
    the interval is the real one and it holds at the sixth.
P3. ANY MEMBER MINTED HAS AN ODD VALUE AT 1. Implied by P2 and printed
    separately, so that a failure separates the implication from the
    pattern.
P4. IT KEEPS D's AND E's SHAPE OTHERWISE: reciprocal, no cyclotomic
    factor, every coefficient strictly positive. The circle test is
    REPORTED AND NOT PREDICTED -- E already left the circle, so this rig
    has no expectation there.
P5. THE NODE CAP BINDS. At least one cell of this column between depth
    33 and J_CAP goes UNDECIDED at the cap. The CLASS WALK's cap has never yet
    bound, and a column deepening at fixed rank is where it should.
    (The clause as first frozen said the cap had never bound ANYWHERE in
    this thread, which an audit found false and is corrected here rather
    than quietly: the attainment pass caps 57 cells of its own on a
    different budget. The prediction itself is unchanged -- it was
    always about this walk's cap -- and the correction cannot move a
    number, P5 being decided by whether a cell of these columns goes
    undecided.)

THE VALUE AT 1 IS REPORTED WITH ITS FACTORISATION AND IS NOT PREDICTED.
A composite kills the primality reading outright. A prime leaves it at
six points against the chance level the hand attack computed, and the
corpus then records an ODD-value pattern with a derivation under it in
place of a primality pattern with none.

THE KILLS, frozen as OBSERVABLES the rig prints, never as inferences.

K1 No decided failing cell of the column from depth 33 to J_CAP prints
   a leftover of degree >= 1. P1 dies and the column is closed by the
   five over the depths reached.
K2 A minted member printing a value at -1 other than 1. P2 dies.
K3 A minted member printing an even value at 1. P3 dies.
K4 A minted member printing reciprocal FALSE, a non-empty cyclotomic
   part, or a coefficient that is not strictly positive. P4 dies.
K5 Every cell of ARM 1's column decided within the cap. P5 dies. The
   same line runs on ARM 2's column, where it tests nothing P5 predicted
   -- that column was not in P5's scope -- and is a report.
K6 Instrument: h > ph at a decided cell, or hs < h, or hs > ph, or
   hs0 != ph, or a leftover that is a constant other than 1, or a split
   that does not multiply back to its own cofactor, or a leftover that
   moves with the order the members are stored in.
K7 Answer key: rank 22 does not print h = 42222 with the seed class
   {A, B, C} leaving the leftover [3,9,15,17,15,9,3] at depth 30; or
   does not print h = 108376, hs = 110932 and ph = 125135 with the
   leftover [3,11,24,37,43,37,24,11,3] against {A, B, C, D} at depth 32.
K8 The hand attack: any W_c printing all-roots-on-the-circle FALSE, or
   a non-empty cyclotomic part, or reciprocal FALSE, or a value at -1
   other than 1, or a value at 1 other than 4c-1. The FOURTH step of the
   hand attack dies, and with it every reading in this record that rests
   on the ambient class being unconstrained at 1.

P6. ADDED IN A SECOND RUN, FROZEN BEFORE THAT RUN AND AFTER ARM 1 HAD
    PRINTED, WHICH IS WHY IT IS NUMBERED HERE AND NOT ABOVE. Whatever
    ARM 1's column does about minting, rank 26 -- the other column that
    has minted -- does the same over its own depths 37..48. One column
    is a sample of one, and reporting a barren column as a fact about
    DEPTH is the parent rig's own F3 committed one level up.

THE KILLS, continued.

K9 The two columns disagree: one mints over its swept depths and the
   other does not. P6 dies and whatever ARM 1 found is that column's and
   not depth's. WIRED AFTER RUN 2, which read P6 by hand off the two K1
   lines; the wiring changes no number and was smoked, not re-run.

THE POSITIVE CONTROLS, run before any survive/kill result is read.

C1 The class printed before anything is measured, with the value at -1
   in the table for the first time: degree, height, value at 1 and its
   factorisation, value at -1, reciprocity, the exact Sturm circle test,
   and the cyclotomic part, which must be empty for a residual.
C2 The ambient family W_c for c = 2..24 printed through the SAME
   describe path as the members (K8), with W_2 and W_3 required to come
   back as B and C, and the composite values at 1 among them listed.
   This is the hand attack's fourth step made mechanical: it is the step
   the whole reading turns on and it is the cheapest thing in the rig.
C3 The answer key at rank 22, depths 30 and 32, RE-DERIVED by the same
   capped route_h and the same split and leftover code the sweep uses,
   with the class seeded at {A, B, C} for the first and {A, B, C, D} for
   the second so that each re-mints its own member from a class that
   does not contain it (K7).
C4 The bracket h <= hs <= ph with hs0 = ph, the split multiplying back
   to its own cofactor, and the leftover recomputed over every
   permutation of the members in hand -- all three tallied against the
   population they were checked at, so that a control which RAN cannot
   be told apart from one that never did by reading the output.

COST. Single process, exact integer arithmetic, no array library, run
under memwatch. route_h is capped at NODE_CAP nodes per cell, at the
19000-25000 nodes a second the parent rig measured, so a capped cell
costs at most about twenty seconds; the swap family at rank 22 was
priced there at under three seconds a cell. The column is 33..J_CAP plus
two answer-key cells. A REHEARSAL over the two answer-key cells and the
first two sweep depths runs first, and its wall is multiplied out to the
full range before the full range is run.

THE FINDINGS.

F1. DEPTH IN A COLUMN DOES NOT MINT, AT EITHER COLUMN THAT HAS MINTED.
Rank 22 from depth 33 to 44 and rank 26 from 37 to 48: 24 cells, 23
decided, 22 of them failing, and every one of the 22 has a residual the
class {A, B, C, D, E} already makes. No sixth member. K1 fires at both
ranks, P1 dies, and P6 HOLDS -- the two columns agree, so the barrenness
is DEPTH's and not rank 22's. That reverses the route the sweep was
built on: D sits at rank 22's first failing cell, and E at the third of
that column and at one of rank 26's next three, so both members minted
outside the chart were found in a column's first FOUR failing cells --
that is the parent walk's own fact about two members and not a
consequence of anything here. What THIS adds is that nothing lies
further up: the twelve depths from 33 at rank 22 and from 37 at rank 26
carry nothing new. In DEPTH those four are not near the front -- rank 26
fails first at 27 and carries E at 36 -- so the object is the failing
cell's index in its column and not its depth. A hunt for members belongs
across ranks at the first few failing depths, which is what the parent
rig's ARM 3 was doing, and not down a column.

F2. AND THE RESIDUAL SETTLES TO THE SAME THREE AT BOTH RANKS, WHICH
IS NOT THE SAME ORDER. Rank 22
runs A, E, A, A, A, A*B, A, (clean), A*B, A*B, A*B, A*B; rank 26 runs A,
A, A, A, A, E, (capped), A*B, A*B, A*B, A*B, A*B. Three residuals across all 22
failing cells, E exactly once in each SCAN -- rank 22's column also
carries it at depth 32, below where this scan starts -- and both ending
in an unbroken A*B run -- five cells at rank 26 and four at rank 22. But rank
22 takes E at its SECOND cell and returns to A once after its first
A*B, so the two orders agree on the alphabet and on the tail and not on
the sequence. So a deep cell is not a harder cell for the
class; by the end of each scan its residual has stopped moving, which is
not the same as saying it never moves -- rank 22 returns to A after its
first A*B (observation, 22 failing cells at two ranks).

F3. A HOLE IN THE BAND FOURTEEN RANKS ABOVE ANY ON RECORD, AND WHERE
IN THE BAND IT SITS IS NOT DECIDABLE FROM THIS SCAN. Depth 40 is CLEAN -- h
= ph = 7124019 -- with failing cells at 39 and at 41 through 44. The
band being a containment and not an interval is already the thread's,
read off ranks 5 to 8 where the holes cluster at the ENDS; this one sits
fourteen ranks above any hole on record, with four failing depths above
it. WHETHER IT IS AT AN END IS NOT DECIDABLE FROM THIS SCAN, and the
first draft of this finding said it was at neither: the scan starts at
33, so rank 22's low edge was not re-walked, and it stops at 44 with the
cell still failing, so the far end was not reached -- while rank 7's
recorded holes sit 1 and 3 depths below their own far end, which is the
distance this one has above the last depth scanned (observation, one
cell).

F4. THE CLASS WALK'S NODE CAP BOUND FOR THE FIRST TIME, AND NOT AT A
FRONTIER. (The thread's other capped cells are the attainment pass's 57,
on a different budget and a different instrument.) Rank 26 depth 43 went
undecided at 400000 nodes after 24.2 s, while depth 44 -- wider, and
with h three times the last DECIDED cell's, depth 43's being unknown --
decided in 34.2 s. So the cap is not a depth frontier past which cells
stop being affordable; it is one cell's Fincke-Pohst node count, which
is what the parent rig's F6 named as the erratic quantity, now seen
erratic enough to cap a cell with decided cells on both sides. P5 DIES:
it was frozen over rank 22's column, and nothing there capped. Rank 26's
cap is outside its scope and is a report rather than a survival.

F5. AND THE COST IS FLAT IN DEPTH AT BOTH THESE RANKS, WHICH IS NOT A
LAW AND IS REPORTED AS THE OPPOSITE OF ONE. Rank 22 costs 3.4 to 4.5 s at
its eleven failing cells, over which h grows by a factor of 320, and 1.2
s at the clean one; rank 26 costs 17.9 to 34.2 s across its twelve, the
capped cell included at 24.2. Flat within a factor of two at both.
But the parent rig's probe C measured rank 25 at 17.4 s at depth 30
against 1.59 at 36, and rank 27 at 3.27 against 99.57 over the same two
depths -- swings of an order of magnitude in the same variable at the
neighbouring ranks. So flatness in depth is these two columns' and not
the walk's, and quoting it as a cost model is the mistake the parent rig
already made once and recorded.

F6. THE VALUE AT 1 IS NOT THE PATTERN AND CANNOT BE MADE ONE. No sixth
member was minted, so the primality reading was never handed the
composite that would kill it outright -- but C2 kills it as a law about
the class rather than by counterexample among members: the ambient
family W_c = [c, 2c-1, c] passes every test the corpus applies to a
member at every c from 2 to 24 -- reciprocal, all roots on the unit
circle by the exact Sturm test, empty cyclotomic part, value 1 at -1 --
and its value at 1 is composite at eleven of the twenty-three, from
W_4(1) = 15 upward. W_2 and W_3 come back as B and C, so the family is
the members' own. What survives of the hunch is only that the LATTICE
never exhibits such a member, which no derivation reaches and which
these 24 cells do not test either way. What replaces it is the value at
-1: 1 at all five members, 1 at every residual these 24 cells exhibit
(automatically, the value being multiplicative and A, B, E each giving
1), and it FORCES the oddness at 1 that the five primes were mostly
made of. (SETTLED, and the five points became a rule with a hypothesis
rather than a coincidence: explore_flatten_endvalue.py holds the
enumeration radius FIXED and reads every minimiser of a cell instead of
the one the reduction returns. The value is 1 at every minimiser of
every one of the 297 chart cells with h >= 5, exhaustively, and it is
FALSE below -- sixteen cells at h = 1, 2 and 3 exhibit eleven different
values. What survives here is the statement about the five members and
about these 24 cells, both of which that rig reproduces; what does not
is any reading of it as a law about what the lattice exhibits at
large.)

F7. P2, P3 AND P4 ARE UNTESTED, AND SAYING SO IS PART OF THE RECORD.
All three are conditioned on a member being minted -- its value at -1,
the oddness of its value at 1, and its shape -- and none was. So K2, K3
and K4 guard an EMPTY population across both arms: they did not fire,
and a kill that did not fire over nothing is not evidence for the
prediction it guards. The three are carried forward unspent rather than
counted as survivals. The one arm that could still have exercised that
code path is the smoke below, which forced it by withholding E, and that
is a code exercise and not a test of P2 to P4 either: the polynomial it
recovers is E, whose values were already in C1.

THE RUN RECORD. ONE REHEARSAL and TWO FULL RUNS, the second ADDING ARM 2
and changing nothing before it. The rehearsal ran the two answer-key
cells and depths 33..34 with W_HI = 6: 21.4 s, peak working set 43.4 MB,
K1 and K5 firing as a restricted range must. RUN 1 is C1 to C4 and ARM
1: 58.2 s, peak 50.6 MB. RUN 2 adds ARM 2, whose prediction P6 was
frozen after run 1 had printed and before run 2 ran: 346.0 s, peak 120.3
MB against the 512 MB ceiling. Every number of ARM 1 is identical
between the two runs; the only quantities that differ are two
wall-clocks, 4.2 against 4.3 s and 4.4 against 4.4. The answer key
reproduces in all three: h = 42222 with hs = ph = 44108 and the leftover
[3,9,15,17,15,9,3] at rank 22 depth 30 against the seed {A,B,C}, and h =
108376, hs = 110932, ph = 125135 with the leftover
[3,11,24,37,43,37,24,11,3] at depth 32 against {A,B,C,D}.

FIVE EDITS AFTER RUN 2, none of which can move a number it printed, made
because an audit read the code and no control would have caught four of
them. K9 was DECLARED and never wired -- P6 was read by hand off the two
K1 lines -- and is now computed from the two arms' own mint counts. K6's
clause "h > ph at a decided cell" was unreachable at a CLEAN cell, whose
line prints "= ph" and checked nothing; the clause now runs there, and
re-running rank 22 depth 40 with it in place leaves the cell clean. The
kill dictionary had no C3 key, so examine's own reconstruction guard
would have raised rather than reported. The value at 1 was labelled
prime whenever its factorisation had at most one factor, which reads a
UNIT as prime -- no value here is 1, and the guard is what makes that a
fact rather than luck. And the helper carrying that label was first
named `label`, which is also sweep's parameter for the arm's name, so
the branch that admits a new member -- the one branch neither full run
reaches, both having minted nothing -- would have crashed on a string
call.
TWO SMOKE RUNS AFTER THOSE EDITS, because the full run's coverage
expires when the wiring changes. The first ran both arms at two depths
each with W_HI = 4: 65.6 s, peak 118.6 MB, every cell reproducing run
2's numbers exactly and K9's agreeing path printing. The second ran the
two branches neither full run and no earlier smoke had entered -- rank
22 depths 39..41, which contains the clean cell, and rank 22 depth 34
with E WITHHELD from the class so that the residual must mint: 16.3 s,
peak 43.6 MB. The withheld-E cell prints hs = 282165 against h = 280913
and reaches h on admitting the leftover, which is that branch end to
end. It is a code exercise and not a measurement: the class it runs
against is not the class this record's findings are read from.
"""
import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_flatten_family import split_witness, on_unit_circle
from explore_flatten_band import height, xm1_pow
from explore_flatten_class import (SEED, decide_cell, examine,
                                   describe_member, swap_at, TALLY,
                                   NODE_CAP)

D_POLY = [3, 9, 15, 17, 15, 9, 3]
E_POLY = [3, 11, 24, 37, 43, 37, 24, 11, 3]
FULL = list(SEED) + [("D", D_POLY), ("E", E_POLY)]

RANK = 22
J_LO = 33          # the depth after E's, which the parent rig reached
J_CAP = 44
RANK2 = 26         # ARM 2, added in a second run: the other minting column
J2_LO = 37         # the depth after rank 26's own E cell
J2_CAP = 48
W_HI = 24          # the ambient family printed for c = 2..W_HI

# The parent rig's committed rank-22 numbers, re-derived here.
KEY30 = (42222, 44108, D_POLY)
KEY32 = (108376, 110932, 125135, E_POLY)


def factorise(n):
    """Trial division, for values at 1 of the sizes this thread sees."""
    out, m, d = [], abs(n), 2
    while d * d <= m:
        while m % d == 0:
            out.append(d)
            m //= d
        d += 1 if d == 2 else 2
    if m > 1:
        out.append(m)
    return out


def value_label(n, f):
    """The value at 1 read off its own factorisation. A unit factorises
    to the EMPTY list, which "len(f) > 1 is composite" reads as prime --
    no value here is 1, and the guard is what makes that a fact rather
    than luck."""
    if len(f) == 1:
        return "prime"
    if not f:
        return "%d, a unit" % n
    return "*".join(map(str, f))


def at_minus_1(p):
    return sum(c * (-1) ** i for i, c in enumerate(p))


def show(nm, p):
    """One line through describe_member, plus the two things this rig
    adds: the value at -1 and the factorisation of the value at 1."""
    d = describe_member(p)
    f = factorise(d["at1"])
    print("   %-6s %-34s deg %d  height %-3d  P(1) %6d = %-14s  "
          "P(-1) %3d  recip %-5s  circle %-5s  cyc %s"
          % (nm, str(p), d["deg"], d["height"], d["at1"],
             value_label(d["at1"], f),
             at_minus_1(p), d["recip"], d["circle"],
             list(d["cyc"]) or "(none)"))
    return d, f


def sweep(rank, jlo, jcap, fired, label):
    """One column swept in depth: every failing cell examined
    against the class {A,B,C,D,E}. ARM 1 and ARM 2 are this one
    function at two ranks, so the second column cannot drift from
    the first."""
    print("\n%s -- ONE COLUMN, DEEPER. Rank %d from depth %d to %d, "
          "every failing cell examined against the class {A,B,C,D,E}."
          % (label, rank, jlo, jcap))
    minted, decided, capped = [], 0, 0
    for J in range(jlo, jcap + 1):
        t0 = time.time()
        h, v, ph, verdict = decide_cell(rank, J, NODE_CAP)
        if verdict == "?":
            capped += 1
            print("   r=%d J=%d M=%d UNDECIDED at the %d-node cap "
                  "(%.1f s)" % (rank, J, J + rank, NODE_CAP,
                                time.time() - t0))
            sys.stdout.flush()
            continue
        decided += 1
        if verdict != "F":
            print("   r=%d J=%d M=%d: h=%d = ph, clean (%.1f s)"
                  % (rank, J, J + rank, h, time.time() - t0))
            if h > ph:
                # K6's own clause. A clean cell prints "= ph" and only
                # this reads whether it IS ph; the failing branch's
                # bracket never sees a clean cell.
                fired["K6"] += 1
                print("      K6 h = %d > ph = %d at r=%d J=%d"
                      % (h, ph, rank, J))
            sys.stdout.flush()
            continue
        e = examine(rank, J, h, v, FULL, fired)
        print("   r=%d J=%d M=%d: h=%d hs=%d ph=%d, residual %s, divided "
              "by %s leaves %s (%.1f s)"
              % (rank, J, J + rank, h, e["hs"], ph, e["R"],
                 e["used"] or "(none)", e["rest"], time.time() - t0))
        if e["hs"] < h or e["hs"] > ph or e["hs0"] != ph:
            fired["K6"] += 1
            print("      K6 bracket at r=%d J=%d" % (rank, J))
        else:
            TALLY["C2"] += 1
        sys.stdout.flush()
        if e["rest"] == [1]:
            continue
        minted.append((J, list(e["rest"])))
        p = e["rest"]
        print("      A MEMBER THE CLASS CANNOT MAKE:")
        d, f = show("J=%d" % J, p)
        if at_minus_1(p) != 1:
            fired["K2"] += 1
            print("      K2 the value at -1 is %d" % at_minus_1(p))
        if d["at1"] % 2 == 0:
            fired["K3"] += 1
            print("      K3 the value at 1 is even")
        if not d["recip"] or list(d["cyc"]) or not d["positive"]:
            fired["K4"] += 1
            print("      K4 the shape breaks at J=%d" % J)
        print("      the value at 1 is %d = %s"
              % (d["at1"], value_label(d["at1"], f).upper()))
        par = e["parent"]
        print("      an admissible parent holding %s with %d to spare: %s"
              % (list(e["S"]), len(e["R"]) - 1,
                 "yes" if par else "NO -- a PARENT obstruction"))
        if par:
            _, hsx = swap_at(rank, J, FULL + [("X%d" % J, list(p))],
                             xm1_pow(J))
            print("      with it admitted, hs = %d against h = %d -- %s"
                  % (hsx, h, "reached" if hsx == h
                     else "STILL NOT REACHED"))
        sys.stdout.flush()

    print("\n   %d cells decided, %d capped, %d minted a member"
          % (decided, capped, len(minted)))
    if not minted:
        fired["K1"] += 1
        print("   K1 rank %d mints nothing over the depths reached"
              % rank)
    if capped == 0:
        fired["K5"] += 1
        print("   K5 the node cap never bound at rank %d" % rank)
    return minted, decided, capped


def main():
    t_all = time.time()
    fired = dict((k, 0) for k in
                 ("K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8", "K9",
                  "C3"))

    print("=" * 70)
    print("explore_flatten_deep.py -- the value at 1, or the value at -1?")
    print("=" * 70)

    # -------------------------------------------------------------- C1
    print("\n[C1] the class in hand, with the value at -1 in the table "
          "for the first time.")
    for (nm, p) in FULL:
        show(nm, p)

    # -------------------------------------------------------------- C2
    print("\n[C2] the ambient family W_c = [c, 2c-1, c] for c = 2..%d, "
          "through the SAME describe path (K8). W_2 must come back as B "
          "and W_3 as C." % W_HI)
    comp = []
    for c in range(2, W_HI + 1):
        p = [c, 2 * c - 1, c]
        d, f = show("W_%d" % c, p)
        bad = (not d["circle"] or list(d["cyc"]) or not d["recip"]
               or at_minus_1(p) != 1 or d["at1"] != 4 * c - 1)
        if bad:
            fired["K8"] += 1
            print("      K8 W_%d fails the hand attack's fourth step" % c)
        if len(f) > 1:
            comp.append((c, d["at1"], f))
    named = dict(FULL)
    if [2, 3, 2] != list(named["B"]) or [3, 5, 3] != list(named["C"]):
        fired["K8"] += 1
        print("      K8 W_2 and W_3 are not B and C")
    print("   composite at 1 among them: %s"
          % ", ".join("W_%d(1) = %d = %s" % (c, v, "*".join(map(str, f)))
                      for (c, v, f) in comp))

    # -------------------------------------------------------------- C3
    print("\n[C3] the answer key at rank %d, RE-DERIVED by this rig's "
          "own path: depth 30 against the seed {A,B,C}, depth 32 against "
          "{A,B,C,D}. Each must re-mint its own member from a class that "
          "does not contain it." % RANK)
    seedABC = list(SEED)
    seedABCD = list(SEED) + [("D", D_POLY)]
    for (J, cls, want) in ((30, seedABC, KEY30), (32, seedABCD, KEY32)):
        h, v, ph, verdict = decide_cell(RANK, J, NODE_CAP)
        if verdict != "F":
            fired["K7"] += 1
            print("   K7 r=%d J=%d verdict %s, not a failing cell"
                  % (RANK, J, verdict))
            continue
        e = examine(RANK, J, h, v, cls, fired)
        print("   r=%d J=%d M=%d: h=%d hs=%d ph=%d, residual %s, divided "
              "by %s leaves %s"
              % (RANK, J, J + RANK, h, e["hs"], ph, e["R"],
                 e["used"] or "(none)", e["rest"]))
        ok = (h == want[0] and e["hs"] == want[1]
              and e["rest"] == want[-1]
              and (len(want) < 4 or ph == want[2]))
        if not ok:
            fired["K7"] += 1
            print("      K7 the key does not reproduce at J=%d" % J)
        if e["hs"] < h or e["hs"] > ph or e["hs0"] != ph:
            fired["K6"] += 1
            print("      K6 bracket at r=%d J=%d" % (RANK, J))
        else:
            TALLY["C2"] += 1
        sys.stdout.flush()

    # ----------------------------------------------------------- ARM 1
    m1, _, _ = sweep(RANK, J_LO, J_CAP, fired, "ARM 1")
    # ------------------------------ ARM 2, added in a second run
    m2, _, _ = sweep(RANK2, J2_LO, J2_CAP, fired, "ARM 2")
    if bool(m1) != bool(m2):
        fired["K9"] += 1
        print("\n   K9 the two columns DISAGREE: rank %d minted %d and "
              "rank %d minted %d, so whatever ARM 1 found is that "
              "column's and not depth's"
              % (RANK, len(m1), RANK2, len(m2)))
    else:
        print("\n   the two columns AGREE, both minting %d, so P6 holds "
              "and the reading is about depth" % len(m1))

    print("\n[C4] the controls that pass SILENTLY, counted.")
    print("   %d cells examined; the bracket h <= hs <= ph with hs0 = ph "
          "holds at %d; the split reconstructs its own cofactor at %d; "
          "and the leftover is the same over EVERY permutation of the "
          "members in hand at %d"
          % (TALLY["cells"], TALLY["C2"], TALLY["C3"], TALLY["C4perm"]))

    print("\n" + "=" * 70)
    hit = ", ".join("%s x%d" % (k, n) for k, n in sorted(fired.items()) if n)
    print("KILLS FIRED: %s" % (hit or "none"))
    print("wall %.1f s" % (time.time() - t_all))
    print("=" * 70)


if __name__ == "__main__":
    main()
