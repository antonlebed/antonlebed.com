"""explore_flatten_recur.py -- DOES THE MONIC SEXTIC RECUR, AND DOES THE
END-VALUE RULE READ h >= 4 OR h >= 5?

THE SUBJECT. Over a chart of cells (M, J), each cell's minimiser is an
integer vector of least sup norm h in a lattice, read as a polynomial.
Divide a minimiser by its monomial factor and by every cyclotomic factor
it carries and a RESIDUAL R survives, with positive leading coefficient
and no cyclotomic factor. Holding the enumeration radius FIXED collects
every minimiser of a cell instead of the one the reduction returns, and
over the 550-cell chart (M = 4..40, J = 2..20) that pass closes 405
cells and exhibits 305 distinct residual classes. That pass is
explore_flatten_endvalue.py, the parent of this rig, and two facts it
left are this rig's subject.

THE FIRST IS AN OBJECT. Asked what the 297 closed cells of height h >= 5
exhibit over their WHOLE minimiser sets, the pass gives four classes --
1, A = 2 + 4x + 5x^2 + 4x^3 + 2x^4, B = 2 + 3x + 2x^2, and

   S = 1 + 2x + 4x^2 + 5x^3 + 4x^4 + 2x^5 + x^6,

monic, degree 6, cyclotomic-free, 1 at -1 and 19 at 1, divisible over Z
by neither A nor B, roots off the unit circle, at exactly ONE cell
(M = 18, J = 8, h = 6). Being MONIC puts S outside all five minted
members at once with no computation -- every member has leading
coefficient at least 2, so every product of members is non-monic. It is
not itself a minted member either: that cell's exhibited witness splits
to 1, so the reduction never asked for one. One cell is one cell, and
the question that promoted the member E is the question S now faces --
E stopped being an accident when it turned up at two ranks four apart.

THE SECOND IS A GAP. The end-value rule -- at every cell of h >= 5,
EVERY vector of least sup norm has a residual with the value 1 at -1 --
is stated at h >= 5 for one reason only. The chart holds 20 cells at
h = 4; 18 closed under the pass's 50,000-node cap with no exception and
2 CAPPED, and those 2 are the only cells above h = 3 that anything is
unknown about. Two cells at a raised cap decide whether the rule reads
h >= 4 or h >= 5, and a failure at either would be the first non-unit
end value above h = 3.

THE QUESTIONS, in the order the rig answers them:

  (a) Widen the chart in DEPTH to J = 30 and run the same fixed-radius
      pass. Does S appear at any cell other than (18, 8)? Does any OTHER
      class outside {1, A, B} appear at a cell of h >= 5?
  (b) Does the end-value rule survive the widening at every closed cell
      of h >= 5?
  (c) At a per-cell cap of 1,000,000, do the two capped h = 4 cells
      close, and does the rule hold there?

WHY DEPTH AND NOT WIDTH. The direction is the whole of the pricing and
this thread has already measured it: extending to J = 30 adds 145 cells
for about 6 s against the 550's 23 s, because depth is where h GROWS and
the lattice rank SHRINKS. Widening in M does the opposite and is where
the cost lives. Since the recurrence question is about cells of LARGE h,
the cheap direction is also the right one.

THE HAND ATTACK, before any of this was coded.

(1) THE NEW CELLS ARE ALL DEEP IN THE RULE'S REGIME, AND THAT IS A
TRANSPLANT. explore_flatten_select.py's census records that every one of
the 145 cells at J >= 21 has h >= 10 -- taken by a DIFFERENT rig over the
same chart definition, so it is imported here and not derived, and the
import is what a transplant mark is for. Marked as a transplant, and arm
1 prints the minimum height over the new cells so the import is CHECKED
rather
than assumed. If it holds, all 145 new cells are simultaneously tests of
the rule and places S could recur.

(2) WHAT "RECURS" CAN EVEN MEAN, WHICH NARROWS THE OBSERVABLE. The
collected classes are closed under multiplication in the sense that a
product of residuals is residual-shaped, but S is MONIC and every member
is not, so S times any member is a DIFFERENT class and not a second
sighting of S. So recurrence splits into two observables the rig reports
apart: S ITSELF at a second cell, and any NEW class outside {1, A, B, S}
at a cell of h >= 5. The second is the wider question and the first is
the one that promoted E.

(3) S IS IRREDUCIBLE OVER Z, AND THE ARGUMENT IS THE DESCENT THE CLASS
BLOCK ALREADY USES. Two facts do all the work. S is reciprocal with
S(-1) = 1 - 2 + 4 - 5 + 4 - 2 + 1 = 1, so it has no root at -1; and it
descends in y = x + 1/x to S/x^3 = (x^3 + x^-3) + 2(x^2 + x^-2) +
4(x + x^-1) + 5 = (y^3 - 3y) + 2(y^2 - 2) + 4y + 5 = y^3 + 2y^2 + y + 1,
whose only candidate rational roots are +-1, giving 5 and 1 -- so that
cubic is irreducible over Q. Now take T an irreducible factor of S of
LEAST degree, so deg T <= 3, and the case split is on T alone, which is
what makes it exhaustive.
  (i) T SELF-RECIPROCAL. Its degree cannot be odd, a self-reciprocal
      factor of odd degree having -1 as a root. So deg T = 2, and a
      self-reciprocal factor of even degree 2m descends to a factor of
      degree m of the cubic -- the complementary factor being
      self-reciprocal too -- which the cubic's irreducibility forbids.
  (ii) T NOT SELF-RECIPROCAL. Then T*(x) = x^(deg T) T(1/x) is an
      irreducible factor as well and non-associate to T, so T*T*
      divides S and 2 deg T <= 6. At deg T = 1 that is a rational root,
      and a monic integer polynomial with constant term 1 admits only
      +-1, where S gives 19 and 1. At deg T = 2 the complementary
      factor S/(T*T*) is a self-reciprocal quadratic, which is case (i)
      again. At deg T = 3, S = T*T* exactly: S monic with constant term
      1 makes T monic with T(0) = 1, and T*(-1) = -T(-1), so S(-1) =
      -T(-1)^2, which cannot be 1 over R.
  So S is irreducible over Z. This is the FIRST structural fact about S
  beyond the four the class block records, and it is derived here rather
  than measured -- which is why the rig VERIFIES it by exhaustive trial
  division rather than restating it (arm 5), the argument being the
  thing under test.

(4) THE BUDGET IS THE HAZARD AND IT IS NOT THE WALL. The pass walks in
DESCENDING h and stops on a global node budget, so the 145 new cells --
all of them high -- are walked FIRST, and at the parent's 4,000,000
budget they could in the worst case consume it entirely (145 cells at
the 50,000-node cap is 7,250,000) and STARVE the 550's own h >= 5 cells,
which are the population the recurrence claim is compared against. That
is a scope failure of exactly the shape the parent's F3 guards against,
so this rig raises the budget to 12,000,000 and PRINTS the coverage
per height band. The recurrence question is asked at a scope the run
actually had or it is not asked. The wall is bounded by the budget and
not by the chart: the parent spent 4,000,000 nodes in 106.7 s, about
37,000 nodes a second.

(5) THE h = 4 ARM CANNOT SHARE THAT BUDGET. A cell caps because its
sphere is POPULOUS, so a raised cap buys nodes and grows the collected
vector list; running the two cells inside a budget-bound descending walk
would either starve the rest of the chart or be starved by it. They run
STANDALONE over the shipped 550's h = 4 cells at a per-cell cap of
1,000,000, which at the parent's rate is about 27 s a cell. A cell may
still cap there, and "still capped" is a printed outcome and not a
failure of the rig.

(6) WHAT A SURVIVAL IS WORTH. The pass under-represents LOW cells by
construction and this widening makes that worse, since the new cells all
outrank the old in h. So a survival of the end-value rule here is a
statement about the deep band and adds little to the low end, while a
KILL at any h >= 5 cell would refute the rule outright. Kill and
survival are asymmetric and the findings must say so.

THE SLATE, frozen before any engine code.

  P1. THE RULE SURVIVES THE WIDENING: every collected residual at every
      closed cell of h >= 5 in the 695-cell chart takes the value 1 at
      -1. Predicted to HOLD, on the parent's 297 of 297 and on (1)
      putting the new cells at h >= 10.
  P2. S DOES NOT RECUR: it appears at no cell but (18, 8). Predicted to
      HOLD, but WEAKLY -- E's promotion is the standing counter-example
      to reading one sighting as an accident, and the new band is a
      different corner of the chart (deep, small rank) rather than more
      of the same.
  P3. NEW CLASSES DO APPEAR: at least one class outside {1, A, B, S} at
      a cell of h >= 5. Predicted to FIRE, on the deep band being where
      extremality COLLAPSES -- 63 of the 145 cells at J >= 21 fail,
      against 3 of 362 at J <= 12 (explore_flatten_select.py) -- and a
      failing cell being exactly one whose minimiser is not a pure
      product.
  P4. S IS IRREDUCIBLE over Z, by (3). Predicted to HOLD.
  P5. THE h = 4 CELLS CLOSE AND KEEP THE VALUE: both capped cells close
      at 1,000,000 nodes and every residual collected at h = 4 is 1 at
      -1, so the rule reads h >= 4. Predicted to HOLD.

THE KILLS, as observables the rig prints and not as meanings.

  K-1. A collected residual with R(-1) != 1 at a closed cell of h >= 5.
  K-2. S at a cell other than (18, 8). The rig prints the COUNT of
       cells carrying S and the cells themselves, and the IDENTITY of
       the one cell is C4's job and not this line's -- so a single
       sighting at the wrong cell reads as a clear K-2 beside a FAILED
       C4, and the two are read together or not at all.
  K-3. A class outside {1, A, B, S} at a closed cell of h >= 5.
  K-4. A control fails.
  K-5. A monic integer polynomial of degree 1, 2 or 3 divides S exactly
       -- the exhaustive refutation of (3), inside the Mignotte bound
       2^deg * ||S||_2 on a factor's coefficients.
  K-6. At h = 4: a capped cell that does not close at 1,000,000 nodes,
       or a closed cell carrying a residual with value != 1 at -1. The
       two halves are DIFFERENT outcomes and are printed apart -- the
       first leaves the gap where it was, the second refutes the rule
       one step below its stated threshold.

THE CONTROLS. C1 to C4 run and are read BEFORE any kill or survive
result. C5 belongs to the h = 4 arm and runs with it.

  C1. THE FIVE MEMBERS, through THIS rig's evaluator, must each give 1
      at -1 -- the positive control on the arithmetic.
  C2. THE NEGATIVE CONTROL: 2x^2 + 5x + 2 = (2x+1)(x+2) must give -1,
      and x^2 + 3x + 1 -- irreducible, reciprocal, its roots a
      reciprocal pair OFF the circle -- must give -1. A rig whose
      evaluator can only print 1 is what this excludes.
  C3. THE CHART REPRODUCES BOTH CENSUSES. The widened sweep must decide
      695 cells; its 550-cell sub-rectangle (J <= 20) must exhibit
      exactly {1: 530, A: 16, B: 4}, and the whole 695 exactly
      {1: 612, B: 51, A: 29, A*B: 2, C: 1}. Two committed censuses at
      two scopes, and the second is what certifies the EXTENSION and
      not merely the reduction.
  C4. THE SEXTIC'S OWN CELL. M = 18, J = 8 must have h = 6 and its
      collected residual set must CONTAIN S. If it does not, this is
      not the recorded pass and nothing about recurrence is licensed --
      the analogue of the parent's K-3, re-pointed at the one cell the
      recurrence question is measured against, because the parent's
      four coverage numbers are the 550's and cannot hold here.
  C5. THE h = 4 POSITIVE CONTROL: the 18 cells of height 4 that closed
      under the parent's 50,000-node cap must close again at the raised
      cap and give the same verdict, every residual 1 at -1. A raised
      cap that changed those answers would be changing the enumeration
      and not extending it.

THE DESIGN.

  Arm 1 builds the chart: h(M, J) exactly at M = 4..40, J = 2..min(30,
  M - 1), by explore_flatten_family.py's own route_h, keeping the
  reduced basis each cell returns so no cell is reduced twice. It prints
  the cell count, the count past J = 20, and the minimum height over
  those -- which is (1)'s transplant, checked. C3 runs here, at both
  scopes.

  Arm 2 is the fixed-radius pass over all 695 cells in descending h, the
  same 50,000-node per-cell cap, at a budget of 12,000,000. It prints
  closed, capped and unreached counts, and the coverage broken out by
  height band, so the scope of arm 3 and arm 4 is read off the run. C4
  runs here.

  Arm 3 evaluates every collected residual class at -1 over the closed
  cells of h >= 5 and prints the values taken, the classes off the value
  1 in full, and the cells carrying them. K-1.

  Arm 4 is the recurrence: every class outside {1, A, B} at a closed
  cell of h >= 5, with its cells, its value at -1 and at 1, its
  monicity, its circle verdict, its divisibility over Z by A and by B
  (polydiv, the INTEGER division -- poly_exact_div divides over the
  rationals and has already returned an impossible answer on this exact
  sextic), and the EXHIBITED residual at each carrying cell, which is
  what separates a class the collected set adds from a member the class
  was short of. S is reported by name and apart, so K-2 and K-3 are two
  lines and not one.

  Arm 5 verifies (3) by exhaustive trial division: every monic integer
  polynomial of degree 1, 2 and 3 with coefficients inside the Mignotte
  bound is divided into S over Z. It prints the bound, the number of
  candidates tried, and any divisor found. K-5.

  Arm 6 is the h = 4 closure, standalone: every cell of the shipped
  550-cell rectangle with h = 4, enumerated at the fixed radius with a
  per-cell cap of 1,000,000 and no shared budget. It prints, per cell,
  whether it closes, its node count, the size of its minimiser set, its
  distinct residual classes and their values at -1; and it reports the
  two the parent capped apart from the 18 it closed. C5 and K-6.

THE FINDINGS.

F1. THE THRESHOLD IS h >= 4 AND THE GAP IS CLOSED (rule, exhaustive over
the 20 cells; K-6 clear, P5 holds). Every one of the 20 cells of height 4
closes at a per-cell cap of 1,000,000, each gives exactly ONE residual
class, and every one of the 20 is 1 at -1. The two the parent capped are
identified by the node counts against the old 50,000: exactly two cells
exceed it -- M = 39, J = 11 at 79,247 nodes and M = 40, J = 11 at
251,834 -- and the next largest is 39,068. So the "h >= 5" the rule was
stated at was an artefact of one cap on two cells, and the honest
threshold is one step lower. All twenty cost 16.4 s together.

F2. AND THE RULE SURVIVES A CHART HALF AGAIN AS LARGE (K-1 clear, P1
holds). Widened to J = 30 the chart decides 695 cells, and the pass
closes every one of the 442 with h >= 5 -- 51 at h = 5..9 and 391 at
h >= 10 -- against the parent's 297. Over those 442 cells the whole
minimiser sets exhibit SIX distinct residual classes and all six take the
value 1 at -1. With F1 the statement is now:

   at every one of the 462 cells of the 695-cell chart with h >= 4,
   EVERY vector of least sup norm has a residual with the value 1 at -1,

all 462 of them closed -- 442 by the pass at the 50,000-node cap and
the remaining 20 by arm 6 at 1,000,000, since 2 of those 20 cap under
the former -- and no exception. The
failures stay where the parent put them, at h = 1, 2 and 3, which is the
parent's measurement and not this run's -- this pass closed only 105 of
the 233 cells below h = 4 and says nothing new about them.

F3. THE HIGH BAND'S WHOLE CENSUS IS SIX CLASSES, AND FIVE OF THEM WERE
CATALOGUED BEFORE THE RUN (K-3 fires twice; P3 HOLDS, and holds for the
reason it named -- both firings sit at cells that FAIL, where the
exhibited minimiser is already not a pure product -- but the prediction
read {1, A, B, S} as the catalogue when the 695's own exhibited census is
five, so what it called a new class is not one). The three outside {1,
A, B} are C = 3 + 5x + 3x^2, at one cell (M = 39, J = 28, h = 170,792);
A*B = 4 + 14x + 26x^2 + 31x^3 + 26x^4 + 14x^5 + 4x^6, at two (M = 40, J
= 25 and M = 39, J = 24);
and S. At all three of C's and A*B's cells the cell's own EXHIBITED
residual is that same class, so the collected set adds nothing there --
those are the 695 census's own failing cells seen from the other side.
K-3 therefore fires twice and BOTH firings are the baseline's fault and
not an object: the set {1, A, B} was inherited from the parent's arm 6,
which ran on the 550-cell chart whose exhibited census is exactly those
three, while this rig runs the 695, whose exhibited census is five. The
kill was frozen at the wrong scope for its own chart. The observable is
sound -- the arm printed every class and its cells -- and the finding is
what the printout says rather than what the kill counted.

F4. S DOES NOT RECUR (K-2 clear, P2 holds -- and P2 was the weak
prediction). Over 442 cells at h >= 5, the monic sextic appears at
exactly one, M = 18, J = 8, h = 6, the same cell that produced it. What
this adds beyond the parent is scope and not a second sighting: the
population that failed to reproduce it is now 442 cells rather than 297,
and the 145 the widening added run from h = 700 to h = 155,117,520 --
that range being the NEW cells' and not the whole band's, which is what
the run prints. So S is not E: E turned up at two ranks four apart and
was promoted on the second sighting, and S has been asked once more,
over a chart half again as large and across a height range that dwarfs
the one it was found in, and has not answered (observation). It also
keeps its distinction: among the classes outside {1, A, B} it is the
only one whose carrying cell exhibits something else -- (18, 8) splits
to 1 -- which is what a class the COLLECTED set adds looks like against
a cell that merely fails.

F5. AND S IS IRREDUCIBLE OVER Z, which is the first structural fact
added to it since it was found (property, proved in the hand attack and
verified exhaustively; K-5 clear, P4 holds). The proof is the descent of
hand attack (3), split on an irreducible factor of LEAST degree so that
the cases are exhaustive: self-reciprocal it is odd, which needs a root
at -1, or
even, which needs a factor of the irreducible cubic y^3 + 2y^2 + y + 1;
not self-reciprocal, T and T* both divide, which leaves a rational root,
a self-reciprocal quadratic complement, or S = T*T* forcing
T(-1)^2 = -1. The rig checks it rather than restating it: every monic
integer polynomial of degree 1, 2 and 3 inside the Mignotte bounds 17,
33 and 66 -- 2,357,161 candidates -- is divided into S over Z, and none
divides. So the sextic is not a product of anything, which closes the
cheapest reading of why one cell exhibits it.

F6. THE TRANSPLANT HOLDS AND WAS LOOSE BY EIGHT ORDERS OF MAGNITUDE,
which is why hand attack (1) printed it rather than assuming it. The
imported census says every one of the 145 new cells has h >= 10; the
measured range over those cells is h = 700 to h = 155,117,520. So
widening in depth buys not merely 145 cells but a HEIGHT range the rule
had never been tested across, and F2's scope is the interesting half of
that, not the cell count.

F7. THE BUDGET HAZARD WAS REAL IN SHAPE AND SMALL IN SIZE, and the run
reports the number instead of the worry. The pass spent 8,010,364 nodes
of its 12,000,000 and left NOTHING unreached: every one of the 695 cells
was attempted, so closed and capped are the only two outcomes. Of that
spend, the 128 capped cells at h <= 3 account for 6,400,000 at the
50,000 cap, which puts the entire h >= 4 population at no more than
1,610,364 nodes -- comfortably inside the parent's 4,000,000. So hand
attack (4)'s starvation would have hit the LOW cells, which are not this
rig's population, and the raised budget bought completeness at the low
end rather than the scope F2 needed.

F8. THE CONTROLS. C1: all five members give 1 at -1 through this rig's
evaluator. C2: 2x^2 + 5x + 2 and x^2 + 3x + 1 both give -1, so an
evaluator that can only print 1 is excluded. C3 passes at BOTH scopes --
the 550 sub-rectangle exhibits exactly {1: 530, A: 16, B: 4} and the
whole 695 exactly {1: 612, B: 51, A: 29, A*B: 2, C: 1} -- and it is the
second that certifies the EXTENSION rather than the reduction, since the
145 new cells enter only there. C4: M = 18, J = 8 has h = 6 and its
collected set is 2 classes containing S, so this is the recorded pass
and F4 is licensed. C5 is inside arm 6: the 18 cells the parent closed
under the old cap close again at the raised one with the same verdict.

RUN RECORD (wall 290.8 s: 28.0 s chart, 242.9 s pass, 16.4 s the h = 4
arm; peak working set 350.7 MB, peak commit 347.0 MB under memwatch's
512 MB default). The estimate was 2 to 7 minutes and the wall is 4.85.
The memory is four times the parent's 89.3 MB and the reason is the
chart: 695 reduced bases held for the second pass instead of 550, plus
the collected vector lists of the populous low cells, 128 of which run
to the 50,000-node cap here where the parent's budget stopped short of
them.

FIVE runs. The FIRST was a smoke at M <= 12 with the budget at 200,000
and the h = 4 cap at 20,000, which exists because the arms below the
chart cannot be exercised any other way without paying the full pass. It
caught one thing and it was a reporting fault, not arithmetic: C4 read
its cell's ABSENCE as a failure, so a narrowed sweep would have printed
a failed control for having a smaller range -- the fault the parent's
fifth run fixed one line down in C3, arriving here through the same
door. C4 now reports itself unexercised outside its range. Both controls
passed and every arm printed its shape. The SECOND is the run above and
is what the findings report. The THIRD is that same smoke run AGAIN,
after the C4 change and after every arm had landed, because a claim
about how a control behaves at a range no run has taken it to is an
assertion and not a record: it prints C4 unexercised, every arm prints
its shape, and KILLS is all zeros. No number in the findings comes from
any run but the second. The FOURTH is the smoke a third time, after the
audit removed a helper the rig never called and added a clause to K-2:
a code edit expires a smoke run whatever it touched, and it prints the
same shapes and the same all-zero KILLS. The FIFTH is the smoke once
more, after the final pass rewrapped one print statement -- the same law,
and the reason a wrapping pass over CODE is not a free edit.
"""
import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_flatten_offchart import NodeCap
# the reduction is route_h's and this rig keeps what it returns rather
# than reducing a second time -- the parent's one change to the pass.
from explore_flatten_family import (SWEEP_M, COUNT_CAP, route_h, enum_ball,
                                    split_witness, on_unit_circle, polydiv)

DEEP_J = 30              # the widened depth; the shipped chart is J <= 20
SHIPPED_J = 20
DEEP_BUDGET = 12000000   # hand attack (4): the parent's 4,000,000 can be
                         # consumed entirely by the 145 new cells
H4_CAP = 1000000         # hand attack (5): the h = 4 arm's per-cell cap

A_POLY = [2, 4, 5, 4, 2]
B_POLY = [2, 3, 2]
C_POLY = [3, 5, 3]
D_POLY = [3, 9, 15, 17, 15, 9, 3]
E_POLY = [3, 11, 24, 37, 43, 37, 24, 11, 3]
MEMBERS = [("A", A_POLY), ("B", B_POLY), ("C", C_POLY),
           ("D", D_POLY), ("E", E_POLY)]

S_POLY = [1, 2, 4, 5, 4, 2, 1]          # the monic sextic
AB_POLY = [4, 14, 26, 31, 26, 14, 4]    # A*B, the 695 census's fifth class

NEGATIVE = [([2, 5, 2], -1), ([1, 3, 1], -1)]

# C3's two committed censuses, at the two scopes
WANT_550 = {(1,): 530, tuple(A_POLY): 16, tuple(B_POLY): 4}
WANT_695 = {(1,): 612, tuple(B_POLY): 51, tuple(A_POLY): 29,
            tuple(AB_POLY): 2, tuple(C_POLY): 1}
S_CELL = (18, 8)                        # C4: the sextic's own cell


def at_minus_1(p):
    """The value of an integer polynomial, low degree first, at -1."""
    return sum(c * (-1) ** i for i, c in enumerate(p))


def census(cells, SPLIT):
    c = {}
    for cell in cells:
        r = SPLIT[cell][2]
        c[r] = c.get(r, 0) + 1
    return c


def show(c):
    return {str(list(k)): v for k, v in
            sorted(c.items(), key=lambda kv: -kv[1])}


def main():
    t_all = time.time()
    fired = {"K-1": 0, "K-2": 0, "K-3": 0, "K-4": 0, "K-5": 0, "K-6": 0}

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
    print("\n[arm 1] the widened chart -- h(M, J), M = 4..%d, J = 2..%d"
          % (SWEEP_M, DEEP_J))
    t = time.time()
    H, RED = {}, {}
    for M in range(4, SWEEP_M + 1):
        for J in range(2, min(DEEP_J, M - 1) + 1):
            try:
                h, v, _, red = route_h(M, J)
            except NodeCap:
                print("   stalled at M=%d J=%d" % (M, J))
                continue
            H[(M, J)] = (h, v)
            RED[(M, J)] = red
    deep = [c for c in H if c[1] > SHIPPED_J]
    ship = [c for c in H if c[1] <= SHIPPED_J]
    print("   %d cells decided, %.1f s -- %d at J <= %d, %d past it"
          % (len(H), time.time() - t, len(ship), SHIPPED_J, len(deep)))
    # hand attack (1), the TRANSPLANT, checked rather than assumed
    if deep:
        hs = sorted(set(H[c][0] for c in deep))
        print("   the transplant: heights over the %d new cells run %d..%d "
              "(the imported census says every one has h >= 10)"
              % (len(deep), hs[0], hs[-1]))

    # -------------------------------- C3, the two committed censuses
    print("\n[C3] the splitter over the exhibited minimisers, at both scopes")
    SPLIT = {}
    for c in sorted(H):
        SPLIT[c] = split_witness(H[c][1])
    for label, cells, want, n in (("550", ship, WANT_550, 550),
                                  ("695", sorted(H), WANT_695, 695)):
        got = census(cells, SPLIT)
        if len(cells) != n:
            print("   C3/%s unexercised: that census is a %d-cell chart's "
                  "and this sweep decided %d" % (label, n, len(cells)))
            continue
        if got != want:
            fired["K-4"] += 1
            print("   C3/%s FAILED: census %s, want %s"
                  % (label, show(got), show(want)))
        else:
            print("   C3/%s ok: %s" % (label, show(got)))
    bad = [c for c in H if at_minus_1(list(SPLIT[c][2])) != 1]
    print("   exhibited residuals with value != 1 at -1: %d" % len(bad))

    # ------------------------------- arm 2: the fixed-radius pass
    print("\n[arm 2] the fixed-radius pass over %d cells, budget %d nodes"
          % (len(H), DEEP_BUDGET))
    t = time.time()
    order = sorted(H, key=lambda c: (-H[c][0], c[0], c[1]))
    spent = closed = capped = 0
    SETS = {}            # cell -> the set of residual classes it exhibits
    CAPPED = []
    for c in order:
        M, J = c
        h = H[c][0]
        if spent >= DEEP_BUDGET:
            break
        B, mu, A = RED[c]
        got = []
        try:
            _, _, nodes = enum_ball(B, mu, A, M, F(h * h * M), COUNT_CAP,
                                    collect=got)
            spent += nodes
            mins = [w for w in got if max(abs(x) for x in w) == h]
            closed += 1
            SETS[c] = set(split_witness(w)[2] for w in mins)
        except NodeCap:
            spent += COUNT_CAP
            capped += 1
            CAPPED.append(c)
    unreached = len(H) - closed - capped
    print("   %d closed, %d capped, %d unreached, %d nodes spent, %.1f s"
          % (closed, capped, unreached, spent, time.time() - t))
    # THE SCOPE, per height band -- arm 3 and arm 4 are read at this and
    # at nothing wider. A band with an unreached or capped cell is a band
    # the recurrence question was not asked over.
    print("   coverage by height band (cells: total / closed / capped / "
          "unreached):")
    for lo, hi in ((1, 3), (4, 4), (5, 9), (10, 10 ** 9)):
        band = [c for c in H if lo <= H[c][0] <= hi]
        if not band:
            continue
        cl = sum(1 for c in band if c in SETS)
        cp = sum(1 for c in band if c in CAPPED)
        print("      h %-7s %4d / %4d / %3d / %3d"
              % ("%d..%d" % (lo, hi) if hi < 10 ** 9 else ">= %d" % lo,
                 len(band), cl, cp, len(band) - cl - cp))
    hi5 = [c for c in SETS if H[c][0] >= 5]
    tot5 = [c for c in H if H[c][0] >= 5]
    print("   the h >= 5 population: %d cells, %d closed by this pass"
          % (len(tot5), len(hi5)))

    # ------------------------------------- C4: the sextic's own cell
    print("\n[C4] the sextic's own cell M = %d, J = %d" % S_CELL)
    # A NARROWED SWEEP IS NOT A FAILING RIG. If the cell is outside the
    # range this run swept, the control is UNEXERCISED -- the same
    # discipline C3 keeps, and the reason the parent's fifth run existed.
    if S_CELL not in H:
        print("   C4 unexercised: the cell is outside this sweep's range")
    elif S_CELL not in SETS:
        fired["K-4"] += 1
        print("   C4 FAILED: the cell was %s by this pass"
              % ("capped" if S_CELL in CAPPED else "never reached"))
    else:
        h = H[S_CELL][0]
        has = tuple(S_POLY) in SETS[S_CELL]
        print("   h = %d (record says 6), collected classes: %d, contains "
              "S: %s" % (h, len(SETS[S_CELL]), has))
        if h != 6 or not has:
            fired["K-4"] += 1
            print("   C4 FAILED: this is not the recorded pass and nothing "
                  "about recurrence is licensed")
        else:
            print("   C4 ok")

    # --------------------- arm 3: the end value over the h >= 5 cells
    print("\n[arm 3] the value at -1 over every class collected at h >= 5")
    seen5 = {}           # class -> cells carrying it
    for c in hi5:
        for r in SETS[c]:
            seen5.setdefault(r, []).append(c)
    vals = {}
    for r in seen5:
        vals.setdefault(at_minus_1(list(r)), []).append(r)
    print("   %d distinct classes over %d closed cells; value at -1 -> "
          "class count:" % (len(seen5), len(hi5)))
    for v in sorted(vals):
        print("      %6d : %4d classes, %5d cell-incidences"
              % (v, len(vals[v]), sum(len(seen5[r]) for r in vals[v])))
    off1 = [r for r in seen5 if at_minus_1(list(r)) != 1]
    fired["K-1"] = len(off1)
    print("   K-1: %d classes with value != 1 at -1 at a cell of h >= 5"
          % fired["K-1"])
    for r in sorted(off1, key=lambda r: -len(seen5[r]))[:10]:
        print("      %-42s %3d cells, at -1: %4d, heights %s"
              % (str(list(r))[:42], len(seen5[r]), at_minus_1(list(r)),
                 sorted(set(H[c][0] for c in seen5[r]))))

    # ---------------------------------------- arm 4: the recurrence
    print("\n[arm 4] the classes outside {1, A, B} at h >= 5")
    base3 = {(1,), tuple(A_POLY), tuple(B_POLY)}
    extra = sorted(set(seen5) - base3, key=lambda r: (len(r), r))
    print("   %d such classes over the %d closed cells at h >= 5"
          % (len(extra), len(hi5)))
    scells = seen5.get(tuple(S_POLY), [])
    others = [r for r in extra if r != tuple(S_POLY)]
    fired["K-2"] = max(0, len(scells) - 1)
    fired["K-3"] = len(others)
    print("   K-2: S is carried by %d cells: %s" % (len(scells), scells))
    print("   K-3: %d classes outside {1, A, B, S}" % fired["K-3"])
    for r in extra[:20]:
        at = seen5[r]
        ok, why, _Q, _n, _d = on_unit_circle(list(r))
        # polydiv is the INTEGER division; poly_exact_div divides over the
        # rationals and has already returned an impossible answer here.
        byA = polydiv(list(r), A_POLY) is not None
        byB = polydiv(list(r), B_POLY) is not None
        print("      %s%s"
              % (list(r), "   <- S" if r == tuple(S_POLY)
                 else ""))
        print("         at -1: %d, at 1: %d, monic: %s, circle: %s (%s), "
              "divisible over Z by A: %s, by B: %s"
              % (at_minus_1(list(r)), sum(r), r[-1] == 1, ok, why, byA, byB))
        print("         cells: %s" % ([(c[0], c[1], H[c][0]) for c in at],))
        print("         their EXHIBITED residuals: %s"
              % ([list(SPLIT[c][2]) for c in at],))

    # ------------------------- arm 5: the irreducibility of S, verified
    print("\n[arm 5] S irreducible over Z, by exhaustive trial division")
    norm2 = sum(c * c for c in S_POLY) ** 0.5
    divisors = []
    tried = 0
    for deg in (1, 2, 3):
        bnd = int((2 ** deg) * norm2) + 1
        rng = range(-bnd, bnd + 1)
        if deg == 1:
            cand = [[c0, 1] for c0 in rng]
        elif deg == 2:
            cand = [[c0, c1, 1] for c0 in rng for c1 in rng]
        else:
            cand = [[c0, c1, c2, 1] for c0 in rng for c1 in rng
                    for c2 in rng]
        tried += len(cand)
        for g in cand:
            if polydiv(S_POLY, g) is not None:
                divisors.append(g)
        print("   degree %d: Mignotte bound %d, %d candidates"
              % (deg, bnd, len(cand)))
    fired["K-5"] = len(divisors)
    print("   %d candidates tried, %d proper monic divisors found %s"
          % (tried, len(divisors), divisors))

    # --------------------------------- arm 6: the h = 4 closure, alone
    print("\n[arm 6] the h = 4 cells of the shipped 550, cap %d, no shared "
          "budget" % H4_CAP)
    t = time.time()
    h4 = sorted(c for c in ship if H[c][0] == 4)
    print("   %d cells at h = 4 in the shipped rectangle" % len(h4))
    still = []
    n_bad = 0
    for c in h4:
        M, J = c
        B, mu, A = RED[c]
        got = []
        try:
            _, _, nodes = enum_ball(B, mu, A, M, F(16 * M), H4_CAP,
                                    collect=got)
            mins = [w for w in got if max(abs(x) for x in w) == 4]
            res = set(split_witness(w)[2] for w in mins)
            bad = [r for r in res if at_minus_1(list(r)) != 1]
            n_bad += len(bad)
            print("      M=%2d J=%2d  closed, %8d nodes, %4d minimisers, "
                  "%3d classes, %d with value != 1 at -1 %s"
                  % (M, J, nodes, len(mins), len(res), len(bad),
                     [list(r) for r in bad[:4]]))
        except NodeCap:
            still.append(c)
            print("      M=%2d J=%2d  STILL CAPPED at %d nodes"
                  % (M, J, H4_CAP))
    fired["K-6"] = len(still) + n_bad
    print("   K-6: %d cells still capped, %d classes with value != 1 at -1; "
          "%.1f s" % (len(still), n_bad, time.time() - t))
    if not still and not n_bad and len(h4) == 20:
        print("   every one of the 20 h = 4 cells closes and keeps the "
              "value, so the rule reads h >= 4 over this chart")

    print("\nKILLS: %s" % fired)
    print("wall %.1f s" % (time.time() - t_all))


if __name__ == "__main__":
    main()
