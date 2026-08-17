"""explore_ruler_optimum.py -- AN EXACT SOLVER FOR THE MARGINAL OPTIMUM,
and the two tilted cells no pass has ever been able to SEARCH.

(The cells, the machinery and the certificate are IMPORTED from
explore_ruler_barecell.py, explore_ruler_setvalued.py and
explore_ruler_exchange.py rather than rewritten, so what is new here is
one algorithm and nothing about the objects it is run on.)

THE QUESTION. Minimizing expected set size subject to marginal coverage
is a multiple-choice knapsack: atom r takes one of k+1 sizes, size s
costing w_r * s and covering w_r * T_r(s), where T_r(s) is the sum of
that atom's s largest posteriors. The corpus has two instruments for it
and neither can answer the two cells that matter. certified_optimum is
an ARGUMENT -- every pair strictly above the operative level, plus the
cheapest sub-collection of the tied block that closes the deficit --
and explore_ruler_exchange.py has just shown that argument false at
5,447 of 19,125 designed weighted cells, so what it returns at an
unequal-weight cell is an upper bound and not a value.
exhaustive_optimum is exact and dies at (k+1)^M: 4^15 at TILT-3 and
5^105 at TILT-4-WIDE. Those two are the only unequal-weight ring cells
the corpus scores whose optima have never been searched, and both carry
a PENALTY recorded as a floor for exactly that reason.

So: an exact algorithm, validated where the exhaustive search can still
run, then spent on the two cells where it cannot.

WHY NOT THE OBVIOUS ONE. A dynamic program along the coverage axis needs
a state per reachable coverage value, and these cells have none to run
along: the tilted posteriors are geometric in theta = 24/25 and 199/200
over rings of 105 and 1155 elements, so the common denominator runs to
127 digits at TILT-3 and 2,417 at TILT-4-WIDE. The same kills a
subset-sum over the tied block, which is why TILT-4-WIDE's 26-weight
block already returns a bracket. Neither axis is discrete at any usable
granularity, so nothing here counts states.

WHOSE VOCABULARY. The design is written in INTEGER PROGRAMMING's terms
-- relaxation, reduced cost, fixing, branch and bound -- and not in the
conformal literature's nor the tower's, because the object is an integer
program and the question is exactness of an optimum. ATOM, LEVEL and
TIED BLOCK keep the parent files' senses. PROFILE is this file's word
for an atom's sorted posterior vector, which is what its top-mass
function T is a function of.

TRANSPLANT, MARKED. Nothing about the ring cells' shape is imported from
the designed sweep. The sweep is M = 3 atoms on a denominator-20 menu
with weights on a /20 grid; the ring cells are 15 and 105 atoms with
geometric weights and no grid at all. Validation on the sweep therefore
tests the ALGEBRA of the solver and not its behaviour at scale, and the
node counts are printed for both so the difference is visible rather
than assumed.

THE HAND ATTACK, worked on paper before any engine code.

FIRST, THE BOUND, RE-DERIVED RATHER THAN INHERITED. Write T = 1 - alpha,
t* for the operative level, and give pair i = (r, y) the cost c_i = w_r
and the coverage v_i = w_r * p(y|r). For ANY feasible set X,

    cost(X) = sum_{i in X} [ c_i - v_i/t* ] + coverage(X)/t*
            >= sum_{i: rc_i < 0} rc_i + T/t*   =:  L,

writing rc_i = c_i - v_i/t* for the reduced cost at price 1/t*. This is
a lower bound on every feasible rule and it needs no argument about
exchanges. It also comes out ALGEBRAICALLY EQUAL to certified_optimum's
`lower` -- above_cost + deficit/t* -- which is a cross-check on both and
the reason `lower` is re-read here rather than recomputed.

SECOND, THE FIXING, WHICH IS WHAT MAKES THE SEARCH SMALL. Let U be any
feasible cost and g = U - L. Rearranging the same identity,

    cost(X) - L  =  sum_{i in X, rc_i > 0} rc_i
                 +  sum_{i not in X, rc_i < 0} (-rc_i)
                 +  (coverage(X) - T)/t*,

three non-negative terms. So a pair with rc_i > g is in NO optimal rule
and a pair with rc_i < -g is in EVERY one: each such deviation alone
costs more than the incumbent already achieves. Reduced costs are
monotone in the size index -- rc = w_r(1 - p/t*) and the masses are
sorted descending -- so fixing lands as a RANGE [lo_r, hi_r] of sizes
per atom and never as a hole, and the prefix structure survives it. The
atoms with lo_r < hi_r are the CORE, and everything else is decided
before the search starts.

THIRD, THE SEARCH. Depth-first over the core atoms, incumbent U updated
on every feasible leaf, each node bounded by the same relaxation applied
to the remaining suffix: the fractional greedy by ratio over the pairs
still available. Within an atom the ratios are the sorted masses, so the
greedy respects the prefix order for free and the relaxation is a valid
lower bound on the residual. Nodes are capped, and the cap is a printed
observable rather than a silent truncation.

FOURTH, WHY THE ARITHMETIC IS INTEGER. Every cost and coverage is
rescaled by one common denominator at the start, so the search compares
integers rather than Fractions and the bound test is a cross-multiplied
integer inequality with no division in it. The integers are large --
rescaling the whole cell lands on a denominator of 148 digits at TILT-3
and 2,659 at TILT-4-WIDE, the posteriors' own 127 and 2,417 plus what
the atom weights add. The size does not go away; it stops being
re-derived at every comparison.

FIFTH, WHAT COULD MAKE THIS WRONG RATHER THAN SLOW, since that is the
question a validated solver has to answer. The bound and the fixing are
both derived above from one identity, so an error in either shows up as
a solver value that is not the exhaustive one -- which is what the
validation arm reads. The failure mode the validation CANNOT see is a
cell shape the sweep does not contain: the sweep is 3 atoms and the ring
cells are 15 and 105, so agreement there tests the algebra and not the
recursion's behaviour at depth. That is why the node counts and core
sizes are printed at every arm rather than only the answers.

SIXTH, AND IT IS A DERIVATION RATHER THAN A PREDICTION. At EQUAL atom
weights the solver must return the certificate at every cell, because
the certificate is PROVED optimal there (explore_ruler_exchange.py: cost
is a constant times the count of labels, so the cheapest rule takes the
largest posteriors anywhere). An equal-weight disagreement is therefore
a solver bug and never a finding, and the equal-weight arm is read that
way.

THE SLATE, frozen before any engine code.

PREDICTIONS.
  P1. The solver equals exhaustive_optimum at all seven bare cells and
      at every one of the 19,125 designed sweep cells. (A single
      disagreement refutes it and the solver is what is wrong, the
      enumeration being exhaustive by construction.)
  P2. At the 5,447 sweep cells where the certificate is known to
      overstate, the solver returns STRICTLY LESS than the certificate
      -- so the search is doing work rather than reproducing the
      argument it replaces.
  P3. TILT-3's certificate is EXACT. Its weights are geometric in
      24/25 over 15 atoms, a spread of 1.77x from heaviest to lightest,
      and a disagreement needs a tied atom heavy enough that the
      surplus it leaves covers a strictly-above pair whole. This is a
      transplant from the equal-weight derivation and is marked as one.
  P4. TILT-4-WIDE's exact optimum lies inside the bracket its greedy
      fill already printed, [0.8967, 0.9028]. (A consistency check on
      the two instruments, not a new claim; the value is what is new.)

KILLS, as observables rather than as inferences -- what the rig prints,
with what it would mean weighed only after the run.
  K-A. Any cell where the solver and exhaustive_optimum disagree.
  K-B. Any cell where the solver's value falls below the relaxation L or
       above the certificate's upper bound.
  K-C. Either tilted cell hitting the node cap. That is a REFUSAL with
       its size named, not a result, and the printed node count is what
       says which.
  K-D. Any equal-weight cell where the solver differs from the
       certificate (see SIXTH: a bug, not a finding).

CONTROLS, run and read BEFORE any kill or survive result, each printing
HOW MANY cases it exercised -- a control that cannot run prints what a
blind one prints.
  C1 (POSITIVE, the search fires). Over the sweep, the number of cells
     whose CORE is non-empty and the number where the solver's answer is
     strictly better than the certificate's. A solver that agreed with
     the certificate everywhere would pass P1 while searching nothing,
     and these two counts are what separates the cases.
  C2 (PARITY). The seven bare cells: solver against exhaustive_optimum
     against the certificate, printed per cell, reproducing the parent
     file's own 7/7 agreement of certificate and exhaustive.
  C3 (ORDER). L <= solver <= certificate upper at every cell scored, as
     a count of violations over the whole sweep.
  C4 (TRUTH). Every generated cell's posteriors sum to 1 per atom and
     its weights sum to 1, in Fraction, as the sweep's own control does.

THE ARMS.
  1. The seven bare cells (C2).
  2. The 19,125-cell designed sweep, plus its 125 equal-weight cells
     (P1, P2, K-D, C1, C3, C4).
  3. TILT-3 and TILT-4-WIDE: the certificate, the relaxation, the exact
     optimum, and whether they coincide (P3, P4, K-C).

RESOURCE NOTE. Exact integers throughout, no numpy. The sweep is the
same 19,125 cells the exchange rig scored in 14.8s; this solver replaces
a 64-vector enumeration with a bounded search over a core of at most
three atoms, so the arm is expected to be of the same order. The two
ring cells are the unknown and are what the node cap is for. Estimated
well under the 512 MB default and under a few minutes; the run record
below carries what it actually cost.

RUN RECORD (wall 26.8s with C6 added at audit; the figures below are
that run). 19,261 cells solved exactly -- 19,257 of them also solved
by an exhaustive enumeration and checked against it, plus the four ring
cells, which are the ones nothing else can reach. Peak
working set 184.3 MB against the 512 MB default (memwatch) -- the peak
is TILT-4-WIDE's truth, as it is in the parent file. Integers throughout,
no bracket anywhere in the output. The tables below run wider than this
file's prose and are left that way: they are output copied verbatim.

THE DESIGN AS FROZEN SOLVED TILT-3 AND NOT TILT-4-WIDE, and what fixed
the second is one line of reasoning rather than a faster machine. TILT-3
came out at 185 nodes, its certificate already being an exact fill. The
fixing needs a gap U - L, so it is only as strong as the INCUMBENT, and
the incumbent the design reached for is the parent file's certificate --
which at TILT-4-WIDE is a greedy fill past a 200,000-sum cap, 0.9027944
against a relaxation of 0.8966969. That gap, 6.1e-3, sits INSIDE the
cell's range of reduced costs (1.8e-3 to 1.2e-2), so most increments
fell under it unfixed, every one of the 105 atoms stayed in the core,
and the 26 zero-reduced-cost tied pairs made the search a 2^26
enumeration. Computing the tied fill EXACTLY -- meet in the middle over
the block, 2^13 sums a half, which the sum cap was there to avoid and
which costs 12s -- moves the incumbent to 0.8967012 and the gap to
4.3e-6, some four hundred times under the SMALLEST reduced cost in the
cell. Every pair outside the tied block then fixes, the core IS the tied
block, and the answer falls out of one subset sum at ONE node. So the
lesson is not that branch and bound needed help: an exact bound at the
top made the search unnecessary, and the loose bound was the whole
difficulty.

TWO SHAPES OF CELL THEN CAPPED THE SEARCH AND BOTH WERE THE SAME MISS --
the tied block being modelled as one item per ATOM. FLAT-3's fifteen
identical atoms each carry TWO tied labels, so they were branched rather
than summed, and DEAD-7's block is 105 items, past any meet-in-the-middle
half. Both dissolve on the same reading: tied pairs all buy coverage at
the same rate, so they are interchangeable ITEMS and an atom contributes
as many as it has, and deduplicating sums makes 105 equal weights 106
sums rather than 2^105. What remained after that was FLAT-3 enumerating
the permutations of one aggregate -- only the total weight at each size
matters, so identical atoms are interchangeable too, and forbidding a
twin to take more than the atom before it leaves one representative per
aggregate. 4^15 becomes 1,251 nodes.

CONTROLS, read before any verdict. C2: solver == exhaustive at 7/7 bare
cells. C3: zero order violations over 19,250 cells. C4: zero truth
failures. C1 (the search fires): the core is non-empty at all 19,125
sweep cells and the solver beats the certificate at 5,447 of them --
which is the exchange rig's own count, reached by a second instrument
that shares no step with it. C6, also added at audit, is the only control here that asks whether the
reported cost belongs to a rule that EXISTS: every other one compares a
number against a number. It rebuilds the certificate's rule explicitly --
the strictly-above pairs plus the tied items the subset sum picked -- and
recomputes cost and coverage from the cell. Cost matches and coverage
clears the target at 4/4 ring cells. C5, added at audit: a split exhaustive
search -- both halves of the atoms enumerated separately and joined on
the coverage axis, no relaxation and no fixing in it anywhere -- agrees
with the solver at 9/9 cells it can reach, TILT-3 among them. C5 ALSO
FIRED AS A CONTROL SHOULD: its first version read the last index of a
saturated binary search and returned INFEASIBLE answers, 4.667 against
5.0 at B-DEAD-7 and 0.9 against 2.0 at B-TILT-W. A control that agrees
with the instrument at the two cells it was written for and disagrees
at two it was not is a control catching itself, and it is why the bare
cells are in it at all.

P1 HOLDS. 19,125 of 19,125 sweep cells and 125 of 125 equal-weight ones
agree with exhaustive_optimum exactly, the two arms costing 193,631 and
1,123 search nodes.
P2 HOLDS. The solver beats the certificate at exactly 5,447 unequal-weight
cells and at 0 equal-weight ones -- the second being the derivation in
SIXTH reproduced rather than assumed.
P4 HOLDS. TILT-4-WIDE's optimum lies inside the printed bracket.

WHAT EACH ANSWER RESTS ON IS NOT THE SAME, and the difference is worth
stating because "validated" covers one of them and not the other. The
sweep exercises the branching path hard -- 2,280 of a 3,825-cell slice
take more than one node -- but at a core of at most 3 atoms, and C5 is a
full independent enumeration at 15. So TILT-3's answer is confirmed by a
search sharing no step with the solver, and TILT-4-WIDE's is confirmed by
neither: at 105 atoms nothing else can enumerate it, and its one node
means the answer IS the fixing argument plus one subset sum. What holds
there without the fixing is still sharp, and it is worth separating: the
RELAXATION alone brackets that cell's optimum to [0.8966969, 0.8967012],
a width of 4.3e-6, since the lower end is a bound on every feasible rule
and the upper is a rule that exists. So the penalty +0.1033 is safe to
five decimals whatever one thinks of the fixing, and it is only the
verdict CERTIFICATE EXACT that needs the fixing derivation to be right.

P3 IS REFUTED, AND THE TWO CELLS ANSWER OPPOSITE WAYS.

  cell            M   k      relax certificate    optimum  core   nodes
  TILT-3         15   3  0.9008338  0.9287750  0.9194957    15      17
      t* multiplicity 10, parent bound 0.9287750 (tied fill exact: True)
      CERTIFICATE EXACT: False   penalty against the threshold rule 0.0805043
      tied items 10, fill surplus 2.001e-02, certificate over the relaxation 2.794e-02
  FLAT-3         15   3  1.9500000  2.0000000  2.0000000    15    1251
      t* multiplicity 30, parent bound 2.0000000 (tied fill exact: True)
      CERTIFICATE EXACT: True   penalty against the threshold rule 1.0000000
      tied items 30, fill surplus 1.429e-02, certificate over the relaxation 5.000e-02
  DEAD-7         15   7  4.9000000  4.9333333  4.9333333    15       1
      t* multiplicity 105, parent bound 4.9333333 (tied fill exact: True)
      CERTIFICATE EXACT: True   penalty against the threshold rule 2.0666667
      tied items 105, fill surplus 4.762e-03, certificate over the relaxation 3.333e-02
  TILT-4-WIDE   105   4  0.8966969  0.8967012  0.8967012    26       1
      t* multiplicity 26, parent bound 0.9027944 (tied fill exact: False)
      CERTIFICATE EXACT: True   penalty against the threshold rule 0.1032988
      tied items 26, fill surplus 2.840e-06, certificate over the relaxation 4.349e-06

BOTH FLOORS BECOME VALUES, and they move in the same direction because a
stand-in ABOVE the optimum can only understate a penalty measured against
it: TILT-3 from "at least +0.0712" to +0.0805043, TILT-4-WIDE from "at
least +0.0972" to +0.1032988. They were loose for DIFFERENT reasons,
which one clause covering both would hide -- at TILT-3 the certificate
overstates the optimum, and at TILT-4-WIDE it does not and merely could
not be computed, the greedy fill past the sum cap being what stood in. Every other number the parent files print stands:
the certificate never stopped being a sound upper bound.

AND THE MULTIPLICITY IS NOT WHAT DECIDES IT, WHICH IS SETTLED BY THE
PAIR, WHILE WHAT REPLACES IT IS A MECHANISM AND NOT A CRITERION. TILT-3
carries TEN tied items and its certificate overstates; TILT-4-WIDE
carries TWENTY-SIX and its certificate is exact, so the count orders
them backwards and cannot be the cause. The reading that would
have predicted the opposite is the one the corpus had, ties being what
the form penalty was traced to. What separates them is printed above and
it is four orders of magnitude: the exact tied fill overshoots the target
by 2.0e-2 at TILT-3 and by 2.8e-6 at TILT-4-WIDE, and the surplus is
exactly what the exchange rig showed an optimum spending -- to drop a
strictly-above pair, or to swap a heavy tied item for a light below-level
one. A block of 26 geometric weights at ratio 199/200 can hit a deficit
almost exactly and leaves the optimum nothing to spend; a block of 10 at
ratio 24/25 cannot. So MORE ties means a FINER block and a smaller
surplus, which is the opposite of the intuition that more ties cost more,
and it is why counting the tied block was never going to answer this.
FLAT-3 is the control on that reading and it is why the statement is
about unequal weights only: its surplus is 1.4e-2, comparable to
TILT-3's, and its certificate is exact anyway -- because its atoms carry
EQUAL weight, where the certificate is proved optimal whatever the
surplus does.

WHAT THIS LEAVES OPEN. The surplus reading above is a mechanism read off
four cells and one designed sweep, not a criterion: nothing here derives
how small a surplus must be to forbid a disagreement, and the condition
the exchange rig's hand attack gives (SOME strictly-above pair has
w_r * p_a <= D, so dropping it is feasible and saves w_r) is SUFFICIENT
for a disagreement and not necessary -- 4,002 of that file's 5,447 admit
it and 1,445 disagree without it.
A cell built to sit between the two -- geometric weights at a ratio dialled
to put the surplus in the decade between 2.8e-6 and 2.0e-2 -- is what
would turn it into one.

SETTLED SINCE, and the paragraph above is left standing as this file's own
record. explore_ruler_surplus.py derives the criterion on paper instead,
and the walk this paragraph proposes turns out to answer nothing: the
certificate's gap over the relaxation IS the surplus over the operative
level, exactly, so the surplus BOUNDS the inexactness rather than
predicting it, and the exactness test that follows is a lattice condition
on the WEIGHTS. Walking theta at this cell's shape drives that lattice
down thirty-six orders of magnitude while the surplus wanders trendless,
which is why the dialled cell would have decided nothing. The "certificate
over the relaxation" column printed above is the same quantity as the
"fill surplus" beside it, divided by t*.
"""

import bisect
import os
import sys
import time
from fractions import Fraction

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_ruler_setvalued import CELLS  # noqa: E402
from explore_ruler_barecell import (  # noqa: E402
    BARE,
    certified_optimum,
    exhaustive_optimum,
    operative_level,
)
from explore_ruler_exchange import (  # noqa: E402
    ALPHA, EQUAL, ROWS, WEIGHTS, check_truth, make_cell,
)

F = Fraction

NODE_CAP = 40000000


# ------------------------------------------------------ the integer form

def integerize(cell, alpha):
    """Rescale the whole cell by one common denominator.

    Returns (cost, cover, target, den) where cost[r] is the integer cost of
    ONE label at atom r, cover[r][j] the integer coverage of that atom's
    (j+1)-th largest mass, and target the integer coverage required.
    Costs and coverages share the scale, so the ratio cover/cost is the
    posterior and the two are directly comparable in the bound.
    """
    w = [cell.atom_prob(r) for r in range(cell.M)]
    inc = [sorted(cell.posterior(r), reverse=True) for r in range(cell.M)]
    vals = [F(1) - alpha]
    for r in range(cell.M):
        vals.append(w[r])
        for y in range(cell.k):
            vals.append(w[r] * inc[r][y])
    den = 1
    for v in vals:
        d = v.denominator
        den = den // _gcd(den, d) * d
    cost = [int(w[r] * den) for r in range(cell.M)]
    cover = [[int(w[r] * inc[r][y] * den) for y in range(cell.k)]
             for r in range(cell.M)]
    return cost, cover, int((F(1) - alpha) * den), den


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# ------------------------------------------------------------ the solver

class Solved(object):
    """One cell's answer, with everything the controls read."""

    def __init__(self, opt, den, nodes, core, capped, lower, cert=None):
        self.opt_int = opt
        self.den = den
        self.nodes = nodes
        self.core = core
        self.capped = capped
        self.lower = lower
        self.cert_int = cert

    @property
    def opt(self):
        return None if self.opt_int is None else F(self.opt_int, self.den)

    @property
    def cert(self):
        """The certificate computed with an EXACT tied fill -- which is
        what the parent file's sum cap prevented at TILT-4-WIDE."""
        return None if self.cert_int is None else F(self.cert_int, self.den)


class TiedBlock(object):
    """The pairs whose ratio IS the operative level, solved by subset sum.

    Every such pair has reduced cost exactly zero, so no bound ever
    separates them and a search that branches over them is a 2^n
    enumeration -- which is what the parent file's 200,000-sum cap ran
    into at 26 items. They all buy coverage at the same rate, so the
    only question they pose is a MIN-COST SUBSET SUM, and that is what
    this solves: both halves' sums are enumerated once per cell and
    every later query is one binary search per left sum.
    """

    SUM_CAP = 1 << 21

    def __init__(self, weights):
        self.w = list(weights)
        n = len(self.w)
        self.total = sum(self.w)
        self.half = n // 2
        a = _subset_sums(self.w[: self.half], self.SUM_CAP)
        b = _subset_sums(self.w[self.half:], self.SUM_CAP)
        self.usable = a is not None and b is not None
        if self.usable:
            self.sa = sorted(a.items())
            self.sb = sorted(b.items())
            self.sbv = [s for s, _m in self.sb]

    def fill(self, need):
        """The cheapest total weight >= need, or None if unreachable."""
        got = self.fill_witness(need)
        return None if got is None else got[0]

    def fill_witness(self, need):
        """(cheapest total, the indices achieving it) -- the witness is
        what lets the answer be re-checked against the cell itself."""
        if need <= 0:
            return 0, []
        if self.total < need:
            return None
        best = None
        for x, ma in self.sa:
            i = bisect.bisect_left(self.sbv, need - x)
            if i < len(self.sbv):
                v = x + self.sbv[i]
                if best is None or v < best[0]:
                    best = (v, ma, self.sb[i][1])
        if best is None:
            return None
        _v, ma, mb = best
        idx = [i for i in range(self.half) if ma >> i & 1]
        idx += [self.half + i for i in range(len(self.w) - self.half)
                if mb >> i & 1]
        return best[0], idx


def _subset_sums(ws, limit):
    """{sum: one mask reaching it} over every subset, or None past
    `limit` distinct sums. Deduplicating is what makes a block of equal
    weights cheap: 105 identical items have 106 sums, not 2^105."""
    out = {0: 0}
    for i, w in enumerate(ws):
        bit = 1 << i
        add = {}
        for s, m in out.items():
            t = s + w
            if t not in out and t not in add:
                add[t] = m | bit
        out.update(add)
        if len(out) > limit:
            return None
    return out


def greedy_feasible(cost, cover, target):
    """A feasible rule by ratio order -- an upper bound to start from.

    Pairs are taken in decreasing posterior, which within an atom is
    decreasing mass, so the prefix structure holds automatically.
    """
    pairs = []
    for r in range(len(cost)):
        for j in range(len(cover[r])):
            pairs.append((cover[r][j], cost[r]))
    pairs.sort(key=lambda p: F(p[0], p[1]), reverse=True)
    c = v = 0
    for cv, ct in pairs:
        if v >= target:
            break
        v += cv
        c += ct
    return c if v >= target else None


def solve(cell, alpha, node_cap=NODE_CAP):
    """The exact optimum, by relaxation + reduced-cost fixing + search.

    Every step is the one derived in the hand attack above.
    """
    cost, cover, target, den = integerize(cell, alpha)
    M, k = cell.M, cell.k
    level, _mult, _cov, _sets = operative_level(cell, alpha)

    # The relaxation L, at price 1/t*, in the integer scale.
    rc = [[F(cost[r]) - F(cover[r][j]) / level for j in range(k)]
          for r in range(M)]
    L = F(target) / level + sum(v for row in rc for v in row if v < 0)

    # The tied pairs, and with them the EXACT certificate: every pair
    # strictly above the level, plus the cheapest tied fill. The parent
    # file's version falls back to a greedy fill past its sum cap, and
    # a loose incumbent makes the fixing below do nothing -- which is
    # the design correction the run record names.
    above_cost = above_cov = 0
    tied_w = []
    for r in range(M):
        for j in range(k):
            ratio = F(cover[r][j], cost[r])
            if ratio > level:
                above_cost += cost[r]
                above_cov += cover[r][j]
            elif ratio == level:
                tied_w.append(cost[r])
    block = TiedBlock(tied_w)
    cert = None
    if block.usable:
        f = block.fill(F(target - above_cov) / level)
        if f is not None:
            cert = above_cost + f

    # An incumbent: whichever feasible rule is cheapest.
    _lo, upper, _exact, _cv = certified_optimum(cell, alpha, level)
    U = int(upper * den)
    for cand in (cert, greedy_feasible(cost, cover, target)):
        if cand is not None and cand < U:
            U = cand

    # Reduced-cost fixing: a range of sizes per atom, never a hole.
    gap = F(U) - L
    lo, hi = [], []
    for r in range(M):
        a = 0
        while a < k and rc[r][a] < -gap:
            a += 1
        b = k
        while b > a and rc[r][b - 1] > gap:
            b -= 1
        lo.append(a)
        hi.append(b)

    base_cost = sum(lo[r] * cost[r] for r in range(M))
    base_cov = sum(sum(cover[r][:lo[r]]) for r in range(M))
    need = target - base_cov
    core = [r for r in range(M) if hi[r] > lo[r]]
    if need <= 0:
        return Solved(base_cost, den, 0, len(core), False, L, cert)

    # The core splits in two. An atom whose ONLY free increment buys
    # coverage at exactly the operative level is a subset-sum item and
    # is never branched on; everything else is.
    tied_items, branch = [], []
    for r in core:
        if all(F(cover[r][j], cost[r]) == level
               for j in range(lo[r], hi[r])):
            # Interchangeable: every one of this atom's free increments
            # costs the same and buys the same, so they enter the block
            # as separate items and the prefix order is free.
            tied_items.extend([(cover[r][j], cost[r])
                               for j in range(lo[r], hi[r])])
        else:
            branch.append(r)
    blk = TiedBlock([ct for _cv, ct in tied_items])
    if not blk.usable:
        return Solved(None, den, 0, len(core), True, L, cert)

    menus = [[(cover[r][j], cost[r]) for j in range(lo[r], hi[r])]
             for r in branch]
    # Best-ratio-first atom order: good incumbents early, tight bounds.
    order = sorted(range(len(branch)),
                   key=lambda i: (F(menus[i][0][0], menus[i][0][1]),
                                  menus[i]),
                   reverse=True)
    menus = [menus[i] for i in order]
    n = len(menus)
    # Only the AGGREGATE matters, so two atoms offering the same menu
    # are interchangeable and enumerating both orders of one answer is
    # the whole cost at a cell of identical atoms. Sorting puts equal
    # menus adjacent; this forbids the second one taking more than the
    # first, which leaves exactly one representative per aggregate.
    twin = [i > 0 and menus[i] == menus[i - 1] for i in range(n)]
    tied_pairs = list(tied_items)

    # Suffix relaxations: every remaining pair, ratio-sorted, prefixed.
    # The tied block sits in every suffix, since it stays available
    # however the branched atoms are decided.
    suf = [None] * (n + 1)
    for d in range(n, -1, -1):
        pairs = list(tied_pairs)
        for i in range(d, n):
            pairs.extend(menus[i])
        pairs.sort(key=lambda p: F(p[0], p[1]), reverse=True)
        cc, vv = [0], [0]
        for cv, ct in pairs:
            vv.append(vv[-1] + cv)
            cc.append(cc[-1] + ct)
        suf[d] = (pairs, cc, vv)

    best = [U - base_cost]          # residual budget: strictly improve
    nodes = [0]
    capped = [False]

    def bound_ok(d, c, need_left):
        """Can the suffix from d still beat the incumbent? Integer test.

        The fractional greedy over the remaining pairs is a valid lower
        bound on the residual cost. The comparison is cross-multiplied,
        so no division enters the search.
        """
        pairs, cc, vv = suf[d]
        if vv[-1] < need_left:
            return False
        i = _first_at_least(vv, need_left)
        room = best[0] - c
        if room <= 0:
            return False
        # cost = cc[i-1] + (need_left - vv[i-1]) * ct/cv  <  room
        cv, ct = pairs[i - 1]
        return cc[i - 1] * cv + (need_left - vv[i - 1]) * ct < room * cv

    def walk(d, c, need_left, cap_j):
        nodes[0] += 1
        if nodes[0] > node_cap:
            capped[0] = True
            return
        if need_left <= 0:
            if c < best[0]:
                best[0] = c
            return
        if not bound_ok(d, c, need_left):
            return
        if d == n:
            # Everything left is tied: one subset sum closes it exactly.
            f = blk.fill(F(need_left) / level)
            if f is not None and c + f < best[0]:
                best[0] = c + f
            return
        top = len(menus[d])
        if twin[d] and cap_j < top:
            top = cap_j
        acc_v = acc_c = 0
        for j in range(top + 1):
            if j:
                cv, ct = menus[d][j - 1]
                acc_v += cv
                acc_c += ct
            walk(d + 1, c + acc_c, need_left - acc_v, j)
            if capped[0]:
                return

    sys.setrecursionlimit(10000 + 20 * n)
    walk(0, 0, need, 1 << 30)
    if capped[0]:
        return Solved(None, den, nodes[0], len(core), True, L, cert)
    return Solved(base_cost + best[0], den, nodes[0], len(core), False,
                  L, cert)


def exhaustive_meet(cell, alpha, cap=10000000):
    """The optimum by a TRUE exhaustive search, split down the middle.

    Added at audit and labelled as such. exhaustive_optimum enumerates
    (k+1)^M size vectors and refuses at 4^15; splitting the atoms in
    two enumerates each half separately and joins them on the coverage
    axis, which is the same enumeration at the square root of its cost
    and shares no line of reasoning with the solver above -- no
    relaxation, no reduced cost, no fixing, no bound. It is what checks
    TILT-3 rather than the solver's own arithmetic. Returns None where
    even the halves are too large (TILT-4-WIDE, at 5^52).
    """
    M, k = cell.M, cell.k
    if (k + 1) ** ((M + 1) // 2) > cap:
        return None
    cost, cover, target, den = integerize(cell, alpha)
    tops = [[sum(cover[r][:s]) for s in range(k + 1)] for r in range(M)]

    def half(rs):
        out = [(0, 0)]
        for r in rs:
            out = [(c + s * cost[r], v + tops[r][s])
                   for c, v in out for s in range(k + 1)]
        return out

    left = half(range(M // 2))
    right = sorted(half(range(M // 2, M)), key=lambda p: p[1])
    # Suffix minimum of cost over right halves sorted by coverage.
    covs = [v for _c, v in right]
    sufmin = [None] * (len(right) + 1)
    sufmin[len(right)] = None
    for i in range(len(right) - 1, -1, -1):
        nxt = sufmin[i + 1]
        sufmin[i] = right[i][0] if nxt is None else min(right[i][0], nxt)
    best = None
    for c, v in left:
        need = target - v
        i = 0
        if need > 0:
            if covs[-1] < need:
                continue        # _first_at_least saturates; check it
            i = _first_at_least(covs, need)
        m = sufmin[i]
        if m is not None and (best is None or c + m < best):
            best = c + m
    return None if best is None else F(best, den)


def _first_at_least(vv, need):
    """Smallest i with vv[i] >= need, on a non-decreasing list."""
    lo, hi = 0, len(vv) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if vv[mid] >= need:
            hi = mid
        else:
            lo = mid + 1
    return lo


# ---------------------------------------------------------- the controls

def surplus(cell, alpha, level, solved):
    """The coverage the EXACT certificate delivers over the target.

    The exchange rig's mechanism runs on this: a lumpy tied block
    overshoots, and the optimum spends the overshoot. Recomputed here
    from the exact fill rather than from the parent's capped one.
    """
    cost, cover, target, den = integerize(cell, alpha)
    above_cov = 0
    for r in range(cell.M):
        for j in range(cell.k):
            if F(cover[r][j], cost[r]) > level:
                above_cov += cover[r][j]
    fill_cost = solved.cert_int - sum(
        cost[r] for r in range(cell.M) for j in range(cell.k)
        if F(cover[r][j], cost[r]) > level)
    return F(above_cov + fill_cost * level - target, den)


def control_C6(cell, alpha, solved):
    """WITNESS: is the reported cost realized by a rule that covers?

    Added at audit. Every other control compares one NUMBER against
    another, which cannot see a cost reported for a rule that does not
    exist. This rebuilds the certificate's rule explicitly -- the
    strictly-above pairs plus the tied items the subset sum picked --
    and recomputes its cost and coverage from the cell. Returns
    (cost matches, coverage >= target), or None where the block is
    past the sum cap.
    """
    cost, cover, target, den = integerize(cell, alpha)
    level, _m, _c, _s = operative_level(cell, alpha)
    above_cost = above_cov = 0
    tied = []
    for r in range(cell.M):
        for j in range(cell.k):
            ratio = F(cover[r][j], cost[r])
            if ratio > level:
                above_cost += cost[r]
                above_cov += cover[r][j]
            elif ratio == level:
                tied.append((cost[r], cover[r][j]))
    blk = TiedBlock([ct for ct, _cv in tied])
    if not blk.usable:
        return None
    got = blk.fill_witness(F(target - above_cov) / level)
    if got is None:
        return None
    _f, idx = got
    c = above_cost + sum(tied[i][0] for i in idx)
    v = above_cov + sum(tied[i][1] for i in idx)
    return F(c, den) == solved.cert, v >= target


def control_C2():
    """PARITY on the seven bare cells: solver, exhaustive, certificate."""
    rows = []
    for cell in BARE:
        level, _m, _c, _s = operative_level(cell, ALPHA)
        _lo, upper, exact, _cv = certified_optimum(cell, ALPHA, level)
        ex = exhaustive_optimum(cell, ALPHA)
        s = solve(cell, ALPHA)
        rows.append((cell.name, s.opt, ex, upper, exact, s.nodes, s.core))
    return rows


def sweep(weights, tag):
    """Score every (rows, weights) cell: solver against the exhaustive
    search, with C1's two counts, C3's violations and C4's truth check."""
    seen = agree = disagree = 0
    bad_truth = bad_order = 0
    cored = beats = 0
    nodes = 0
    worst = None
    for rows in ROWS:
        for wts in weights:
            cell = make_cell(tag, rows, wts)
            if not check_truth(cell):
                bad_truth += 1
                continue
            level, _m, _c, _s = operative_level(cell, ALPHA)
            lower, upper, _e, _cv = certified_optimum(cell, ALPHA, level)
            ex = exhaustive_optimum(cell, ALPHA)
            s = solve(cell, ALPHA)
            seen += 1
            nodes += s.nodes
            if s.core:
                cored += 1
            if s.opt is not None and s.opt < upper:
                beats += 1
            if s.opt is not None and (s.opt < lower or s.opt > upper):
                bad_order += 1
            if ex is None:
                continue
            if s.opt == ex:
                agree += 1
            else:
                disagree += 1
                d = abs(s.opt - ex)
                if worst is None or d > worst[0]:
                    worst = (d, rows, wts, s.opt, ex)
    return dict(seen=seen, agree=agree, disagree=disagree,
                bad_truth=bad_truth, bad_order=bad_order,
                cored=cored, beats=beats, nodes=nodes, worst=worst)


def main():
    print("THE MARGINAL OPTIMUM -- an exact solver, and the two cells")
    print("the corpus has never been able to search.")
    print("alpha = %s, nominal coverage %s" % (ALPHA, 1 - ALPHA))
    print()

    print("C2 PARITY -- the seven bare cells")
    print("  %-12s %10s %10s %10s %6s %7s %5s"
          % ("cell", "solver", "exhaust", "cert", "exact", "nodes", "core"))
    par_ok = par_n = 0
    for name, sv, ex, up, exact, nd, core in control_C2():
        exs = "%.4f" % float(ex) if ex is not None else "--"
        print("  %-12s %10.4f %10s %10.4f %6s %7d %5d"
              % (name, float(sv), exs, float(up), exact, nd, core))
        if ex is not None:
            par_n += 1
            if sv == ex:
                par_ok += 1
    print("  solver == exhaustive at %d/%d bare cells" % (par_ok, par_n))
    print()

    for weights, tag, label in ((WEIGHTS, "SW", "UNEQUAL-weight sweep"),
                                ([EQUAL], "EQ", "EQUAL-weight arm")):
        t0 = time.time()
        r = sweep(weights, tag)
        print("%s: %d cells, %.1fs" % (label, r["seen"], time.time() - t0))
        print("  solver == exhaustive: %d   disagreements: %d"
              % (r["agree"], r["disagree"]))
        print("  C1 non-empty core: %d   solver beats the certificate: %d"
              % (r["cored"], r["beats"]))
        print("  C3 order violations: %d   C4 truth failures: %d"
              % (r["bad_order"], r["bad_truth"]))
        print("  search nodes over the arm: %d" % r["nodes"])
        if r["worst"] is not None:
            d, rows, wts, sv, ex = r["worst"]
            print("  WORST DISAGREEMENT %s rows=%s weights=%s "
                  "solver=%.6f exhaustive=%.6f"
                  % (d, rows, [str(x) for x in wts], float(sv), float(ex)))
        print()

    print("C5 SECOND ROUTE -- the split exhaustive search, which shares")
    print("no step with the solver, over every cell it can still reach")
    ran = ok = 0
    for cell in list(BARE) + list(CELLS):
        v = exhaustive_meet(cell, ALPHA)
        if v is None:
            print("  %-12s out of reach" % cell.name)
            continue
        s = solve(cell, ALPHA)
        ran += 1
        if s.opt == v:
            ok += 1
        print("  %-12s meet %.7f   solver %.7f   agree %s"
              % (cell.name, float(v), float(s.opt), s.opt == v))
    print("  agreement %d/%d" % (ok, ran))
    print()

    print("THE FOUR RING CELLS")
    print("  %-12s %4s %3s %10s %10s %10s %5s %7s"
          % ("cell", "M", "k", "relax", "certificate", "optimum",
             "core", "nodes"))
    for cell in CELLS:
        t0 = time.time()
        level, mult, _c, sets = operative_level(cell, ALPHA)
        lower, upper, exact, _cv = certified_optimum(cell, ALPHA, level)
        s = solve(cell, ALPHA)
        opt = "CAPPED" if s.opt is None else "%.7f" % float(s.opt)
        cert = "--" if s.cert is None else "%.7f" % float(s.cert)
        print("  %-12s %4d %3d %10.7f %10s %10s %5d %7d"
              % (cell.name, cell.M, cell.k, float(lower), cert, opt,
                 s.core, s.nodes))
        thresh = sum(cell.atom_prob(r) * len(sets[r])
                     for r in range(cell.M))
        print("      t* multiplicity %d, parent bound %.7f (tied fill "
              "exact: %s), %.1fs"
              % (mult, float(upper), exact, time.time() - t0))
        if s.opt is not None and s.cert is not None:
            print("      CERTIFICATE EXACT: %s   penalty against the "
                  "threshold rule %.7f"
                  % (s.cert == s.opt, float(thresh - s.opt)))
            # The surplus the tied fill leaves is what the exchange rig
            # showed the optimum spending, so it is printed beside the
            # verdict rather than left to be inferred from it.
            print("      tied items %d, fill surplus %.3e, "
                  "certificate over the relaxation %.3e"
                  % (mult, float(surplus(cell, ALPHA, level, s)),
                     float(s.cert - lower)))
            w = control_C6(cell, ALPHA, s)
            print("      C6 witness: cost matches %s, covers %s"
                  % (w if w is None else w[0], w if w is None else w[1]))


if __name__ == "__main__":
    main()
