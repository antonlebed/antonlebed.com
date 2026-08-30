"""explore_flatten_class.py -- IS THE MULTIPLIER CLASS FINITELY
GENERATED?

explore_flatten_swap.py answered the near end of the failing band as a
CONSTRUCTION: at all 83 failing cells of the chart's rank-5..18
rectangle the least height over pure cofactors with one cyclotomic
block traded for an equal-degree product of a fixed class of
multipliers is h, and the exhibited minimiser is itself a member of
that family. The class was three polynomials -- A, B, C -- read off the
chart's own residual census. At rank 22, depth 30, the first cell
outside the chart that those three cannot make, the family missed h by
44108 against 42222, and the missing multiplier was a FOURTH
polynomial D of degree 6.

THAT LEFT ONE QUESTION AND IT IS THIS RIG'S: is D the fourth member of
finitely many, or the first of a stream. The two answers make different
public statements out of the same construction. A class with finitely
many MEMBERS is a catalogue and the swap is a route to h with a fixed
table in it; a class that gains a member every few ranks is a mechanism
with no catalogue, and the swap PROPOSES h without ever being able to
promise it. THE QUESTION IS ABOUT THE MEMBERS AND NEVER ABOUT THE CLASS:
the class is closed under multiplication, so it is infinite as soon as
it holds one non-constant member, and "is the class finite" has a free
and worthless answer, which is why the question above is put in
the generators and this rig asks for a member no product of the
members in hand can be.

(The senses are the thread's, restated because this rig is read alone.
A vector c on M atoms is the polynomial P(x) = sum_i c_i x^i; its
FLATTENING is the multiplicity of the root 1; its HEIGHT is the sup
norm max_i |c_i|. h(M, J) is the least height of a nonzero P with
flattening at least J and degree < M. A PURE PRODUCT is prod_i
(x^{d_i} - 1) over a multiset D of positive PARTS; ph(M, J) is the
least height of a pure product admissible at the cell. RANK is always
r = M - J. A cell FAILS when h < ph. The COFACTOR of a lattice vector
is q = P/(x-1)^J. split_witness factors a cofactor as a monomial times
a sign times a product of cyclotomics times a RESIDUAL R carrying no
cyclotomic factor. The SWAP FAMILY at a cell is every admissible pure
cofactor with a sub-multiset of its own cyclotomic blocks traded for an
equal-degree product of class members, and hs is its least height.)

THE MECHANISM THIS RIG IS, in one line: walk the ranks upward from the
answer key, take each rank's FIRST failing cell, and ask whether its
minimiser's residual is a product of the members ALREADY IN HAND -- the
class SEEDED at {A, B, C} and GROWING as the walk goes, so that rank 22
must re-mint D from nothing and every rank above it is asked the same
question against whatever the walk has accumulated.

THE HAND ATTACK, worked before any engine code.

FIRST, WHAT MINTS A MEMBER, exactly. At a failing cell route_h returns
a minimiser v; its cofactor q = v/(x-1)^J splits as x^s * (+-1) *
prod(S_min) * R. The LEFTOVER is R divided by each member in hand,
repeatedly, in a fixed order. A leftover of degree 0 says the class
already makes the residual. A leftover of degree >= 1 is a candidate
member, and it is one only after two further things are printed: that
an admissible parent exists (below), and that admitting it drops hs to
h at that cell.

SECOND, THE LEFTOVER IS ORDER-DEPENDENT UNLESS THE MEMBERS ARE
IRREDUCIBLE, AND IRREDUCIBILITY IS NOT ESTABLISHED HERE. A(1) = 17,
B(1) = 7, C(1) = 11 and D(1) = 71 are all prime, which is suggestive
and proves nothing. So the greedy division is not argued to be
well-defined -- it is MEASURED to be, by running the loop over every
permutation of the members in hand and printing whether the leftover
moves (C4/K8). That is cheaper than a factorisation routine and it
tests the thing that actually matters, which is whether this rig's
answer depends on the order it happens to store its class in.

THIRD, hs >= h ALWAYS, inherited from the parent rig's proof: a family
member is a nonzero lattice vector at the cell, so its height is at
least h. And hs <= ph always, the empty block with the empty multiplier
being in the family. So h <= hs <= ph at every cell, and hs = h says
the class in hand SUFFICES at that cell while hs > h says it does not.

FOURTH, hs > h HAS TWO CAUSES AND THEY MUST BE SEPARATED BEFORE THE
CLASS IS BLAMED. The family can miss because no admissible pure
cofactor holds the minimiser's cyclotomic multiset with exactly deg R
degrees to spare -- a PARENT obstruction, which says nothing about the
multipliers -- or because it does and the multiplier is not available.
The parent search is run at every first failing cell and printed, and a
member is minted only where a parent exists.

FIFTH, THE CHEAP FILTER IS NOT THE SCANNER HERE, AND THE REASON IS
MEASURED RATHER THAN ARGUED. hs < ph forces h <= hs < ph,
so the swap family CERTIFIES a cell as failing with no lattice
reduction in it. But at rank 22 depth 30 -- the one cell known to need
a member the class lacks -- hs equals ph exactly while h sits strictly
below both, so the filter is SILENT there. (The three values are K7's
and are not restated here: this record carried them four times over
and a number written four times is a number three of whose copies
nothing checks.) The filter is blind exactly at the cells whose
class is incomplete, which are the only cells this rig is hunting. It
is therefore run AT each decided cell as a measurement and never used
to locate one. Whether the blindness and the minting coincide at every
rank is P5.

SIXTH, THE COST, PRICED BEFORE THE FREEZE BECAUSE IT CHOSE THE DESIGN.
Four probes measured route_h and the swap family outside the chart, and
they overturn the cost model this walk was first designed around.
route_h's cost is NOT a
function of M and the rank and is not monotone in either, while its node
RATE is near constant, so the erratic quantity is the Fincke-Pohst node
count and nothing else. The swap family's own cost is smooth and rises
with the rank alone. The measurements are F6's and are not repeated
here: a cost list written twice drifts between its copies, and this one
did, carrying two probes' numbers into one rank's comparison until an
audit read them side by side. WHICH MEANS THE PARENT RIG'S CROSSOVER IS
A READING OF ONE COLUMN AT ONE RANK: at rank 23 route_h is cheaper than
the family at every depth measured, and the family's advantage at rank
22 depth 30 is one cell's node count and not a trend in M.

So the scan is route_h itself, with a NODE CAP standing in for a time
limit -- deterministic where a wall-clock limit is not. A cell over the
cap is UNDECIDED and printed as such, and a rank's first failing depth
is claimed only when every cell below it was decided.

SEVENTH, WHAT A FIRST CELL CANNOT ANSWER. A rank's first failing cell
is one cell of a column. A member minted there might be the rank's or
might be that cell's, and the two are different objects. ARM 2 takes
the next failing cells of each minting rank's own column, up to a
budget, and asks which members THEY need.

THE SCOPE. Ranks 19 to RANK_HI, each column scanned J = 2 upward to
J_CAP, route_h capped at NODE_CAP nodes. Ranks 19..22 are the answer
key and are re-derived rather than taken: the band rig's first failing
depths there are 26, 23, 25 and 30, and the parent rig's rank-22 cell
misses with the seed class and mints D, at the values K7 names.
Then ARM 2 at each minting rank, up to EXTRA_CELLS further failing
cells, and ARM 3 -- added in a second run and changing no arm before
it -- asking the same question at EVERY scanned rank, so that it
subsumes ARM 2 and rank 22's rows have to reproduce inside it.

THE PREDICTIONS, fixed here before the engine ran.

P1. THE CLASS GROWS AGAIN. At least one rank above 22 mints a member
    outside the multiplicative span of the class in hand at that point.
P2. IT DOES NOT GROW AT EVERY RANK. At least one rank above 22 has its
    first failing cell reached by the class already in hand: leftover
    of degree 0 and hs = h.
P3. THE MEMBERS HAVE D's SHAPE. Every member minted is reciprocal, has
    all its roots on the unit circle by the exact Sturm test, carries
    no cyclotomic factor, and has strictly positive coefficients.
P4. THE OBSTRUCTION IS THE MULTIPLIER AND NOT THE PARENT. At every
    first failing cell an admissible pure cofactor holds the
    minimiser's cyclotomic multiset with exactly deg R degrees to
    spare.
P5. THE FILTER IS BLIND EXACTLY WHERE THE CLASS IS INCOMPLETE. At
    every first failing cell that mints a member, hs = ph; at every
    first failing cell that mints none, hs < ph.

THE KILLS, frozen as OBSERVABLES the rig prints, never as inferences.

K1 No rank above 22 prints a leftover of degree >= 1. P1 dies, and the
   class as seeded plus D closes over every rank this rig reached.
K2 Every rank above 22 prints a leftover of degree >= 1. P2 dies: the
   class gains a member at every rank and the catalogue reading is
   finished.
K3 A minted member printing reciprocal FALSE, or all-roots-on-the-
   circle FALSE, or a cyclotomic part that is not empty, or a
   coefficient that is not strictly positive. P3 dies.
K4 A first failing cell printing NO admissible parent holding S_min
   with deg R degrees to spare. P4 dies at that rank, and the cell is
   reported as a parent obstruction and mints nothing.
K5 A first failing cell that mints a member and prints hs < ph, or one
   that mints none and prints hs = ph. P5 dies.
K6 Instrument: h > ph at any cell, or hs < h, or hs > ph, or hs0 != ph,
   or hs with the leftover admitted != h at a minting cell.
K7 Answer key: ranks 19..22 do not print first failing depths 26, 23,
   25 and 30 with every cell below decided; or rank 22 does not print
   h = 42222 and hs = 44108 against the seed class with the leftover
   [3, 9, 15, 17, 15, 9, 3].
K8 Instrument: the leftover differs across the permutations of the
   members in hand at any cell.

THE POSITIVE CONTROLS, run before any survive/kill result is read.

C1 The answer key (K7), with the four depths RE-DERIVED by scanning
   each column from J = 2 and not taken from the band rig. This is the
   real control: rank 22 must re-mint D from a class that does not
   contain it, by the same code path every new rank uses.
C2 h <= hs <= ph and hs0 = ph at every decided cell (K6). THE LOWER
   BOUND IS THE REAL ONE: hs is a minimum over objects claimed to be
   lattice vectors at the cell, so a fault in the degree bookkeeping
   would put it below an independently computed h. The upper bound is
   FORCED by the seeding -- swap_min starts at hs0 and accepts only
   strict improvements -- so its content sits entirely in hs0 = ph,
   which is checked against pure_min by a second route.
C3 The reconstruction, at every first failing cell: split_witness's own
   output multiplied back -- x^s times the sign times prod(S_min) times
   R -- equals the cofactor exactly.
C4 The leftover recomputed over every permutation of the members in
   hand, at every first failing cell (K8).
C5 The class printed before anything is measured: each member's degree,
   height, value at 1, reciprocity and the exact Sturm circle test.

COST. Single process, exact integer arithmetic throughout, no array
library, run under memwatch. The scan is bounded by NODE_CAP per cell
at the rate F6 measures, between about 19000 and 25000 a
second, so a capped cell costs at most about NODE_CAP over that rate
-- sixteen to twenty-one seconds at the cap set here; the swap family is run at one cell
per rank plus ARM 2's, at the per-rank prices measured above. The
estimate before the run is a REHEARSAL at ranks 19..20 first, whose
wall is multiplied out to the full range before the full range is run.

THE FINDINGS.

F1. THE FIRST FAILING CELLS SAY THE CLASS IS QUIET, AND SEVEN OF THE
EIGHT ARE REACHED BY THE SEED. Ranks 19 to 26 fail first at depths 26,
23, 25, 30, 22, 29, 31 and 27 -- M = 45, 43, 46, 52, 45, 53, 56 and 53 --
every depth re-derived by scanning that rank's own column from J = 2 with
no cell below it left undecided at the node cap. At six of the eight the
minimiser's residual is A alone, at rank 25 it is A*B, and only rank 22's
needs anything the seed cannot make. So P1 dies on the first-cell
reading, K1 fires, and the answer the first cells give is that the class
stopped growing at D.

F2. THE PARENT IS AVAILABLE AT ALL EIGHT, AND AT SEVEN OF THEM THAT
DECIDES NOTHING. An admissible pure cofactor holds the minimiser's
cyclotomic multiset with exactly the residual's degree to spare at every
one of the eight, so P4 holds with no exception. But the test only has
content where hs EXCEEDS h, and at seven of the eight it does not, so
there is no shortfall to attribute and the row cannot fail: the whole
content of P4 here is rank 22's first cell and ARM 3's two, where the
parent is present and the class is therefore what is short. Stated the
other way, the seven passing rows are what a control that cannot fire
looks like, and they are reported as such rather than counted as
evidence.

F3. THE FIRST CELL OF A RANK IS THE WRONG SAMPLE, AND THAT IS THE WHOLE
OF F1. Taking the next three failing cells of every one of the same eight
columns -- 24 more cells, 32 in all -- TWO need a multiplier the class at
the end of the walk cannot make, and they are at DIFFERENT RANKS: rank 22
depth 32, M = 54, where h = 108376 against hs = 110932 and ph = 125135;
and rank 26 depth 36, M = 62, where h = 402038 against hs = 421338 and ph
= 450551. Both carry the SAME residual, divisible by none of A, B, C and
D:

    E = 3 + 11x + 24x^2 + 37x^3 + 43x^4 + 37x^5 + 24x^6 + 11x^7 + 3x^8,

degree 8, height 43, E(1) = 193, reciprocal, carrying no cyclotomic
factor, every coefficient positive. Admitting E drops hs to h exactly at
both. So the class grows with the CELL and not with the RANK, one cell
per rank is a sample thin enough to report a class closed while the same
column two depths up is already outside it, and E recurring at two ranks
four apart is what separates a member from a one-cell accident.

F4. AND E IS NOT IN THE CIRCLE CLASS, WHICH NOTHING THIS THREAD HAD
FACTORED BEFORE THIS RAN HAD DONE. E is reciprocal, so it reduces
through y = x + 1/x to 1 + 4y + 12y^2 + 11y^3 + 3y^4, whose exact Sturm
count is TWO real roots in (-2, 2) out of four: four of E's eight roots
lie OFF the unit circle. Every residual the chart's 695 cells exhibit --
1, A, B, C and A*B -- is reciprocal with all roots ON it, and that is
what made Kronecker the reason the class is a class rather than a list.
At M = 54 and again at M = 62 the minimiser's residual leaves it. So the
all-roots-on-the-circle description is a fact about the chart's rectangle
in exactly the way the five-residual census is, and what survives outside
is only that the cofactor splits as cyclotomics times a residual. P3
dies at both cells; K3 did not fire because it guards the members the
walk ADMITS and the walk admits only at a first failing cell, which is a
gap in this rig's own kill wiring and is recorded rather than repaired -- the two cells print
the shape in full and the reading is made from the print.

F5. THE CHEAP FILTER IS SOUND AND BLIND IN THE SAME PLACES. hs < ph
certifies a cell as failing with no lattice reduction in it; hs = ph
certifies nothing. Over the eight first failing cells the filter FIRES at
the seven the class reaches and is SILENT at the one it does not, and P5
holds at every cell that could test it. Read forward that is a useful
certificate; read as a scanner it is the wrong instrument entirely, since
it goes quiet exactly on the cells that carry a new member -- which are
the only cells a hunt for members wants to find. The instrument the last
extension built cannot be pointed at the question that extension opened.

F6. AND THE COST MODEL THE WALK WAS DESIGNED AGAINST WAS WRONG IN ITS OWN
VARIABLE, AND THE PROBES ARE QUOTED ONE PROBE AT A TIME. Four separate
probes ran, and no comparison below crosses two of them. Probe A, at
rank 23: route_h 0.08 s at depth 10, 0.16 at 20 and 0.84 at 26, against
the swap family's 2.68, 2.69 and 2.86 at the same three cells. Probe B,
also at rank 23: 0.63 s at depth 28, 0.57 at 30, 2.72 at 32 and 4.07 at
34 -- not monotone in the depth, and the last two are above the family's
price at the depths probe A measured it, so the family is not beaten at
rank 23 everywhere, only at the four depths where both were measured
(probe D adds 2.97 for the family at depth 30 against probe B's 0.57).
Probe C, across ranks: 17.4 s at rank 25 depth 30 against 1.59 at 36;
3.27 at rank 27 depth 30 against 99.57 at 36; 0.41 at rank 29 depth 30
against 7.59 at 36. So route_h is not a function of M and the rank and
is not monotone in either, while probe E's node rate holds between about
19000 and 25000 a second across four cells spanning that whole range --
the erratic quantity is the Fincke-Pohst node count and nothing else,
and the crossover measured along one column at one rank is a reading of
that column. What the erratic cost DOES justify is the node cap: a
deterministic budget per cell, under which no cell of this walk went
undecided.

F7. THE CONTROLS THAT PASS SILENTLY, COUNTED. A control that prints
nothing when it holds cannot be told apart, from the output alone, from
a control that never ran, so the three that were silent now print their
own populations. Over 35 examine calls at 32 distinct cells: the bracket
h <= hs <= ph with hs0 = ph holds at 32 of the 32 cells where it is
checked -- ARM 2's three rows do not check it -- the split multiplies
back to its own cofactor at 35 of 35, and the leftover is the SAME
polynomial over every permutation of the members in hand at 35 of 35, so
the greedy division is order-independent on every residual this walk met
and the class's storage order decides nothing. That last is C4, and it
is the one that had to be measured rather than argued: the members are
not known to be irreducible.

THE RUN RECORD. THREE FULL RUNS, each ADDING to the one before and none
changing it. RUN 1 is arms 1 and 2 and every control. RUN 2 adds ARM 3, which
asks arm 2's question at every scanned rank rather than only the minting
one and SUBSUMES it -- rank 22's three rows reproduce inside ARM 3
identically. Every number of arms 1 and 2 is identical between the two
runs; the only quantities that differ are the wall-clocks. RUN 3 adds the
control tallies F7 quotes and changes no line of science: every number
of runs 1 and 2 reproduces in it exactly, the only textual differences
being two print strings an audit reworded. The wall is 224.5 s for the
design as frozen, 502.1 s with the added arm and 499.3 s for run 3, peak
working set 100.8, 121.1 and 120.9 MB against the 512 MB ceiling. The
added arm is what carries F3 and F4, so the second run is where the
answer is and the third is where the controls become readable.

THREE EDITS AFTER RUN 2, none of which can move a number it printed,
made because reading found them and no control would have. The leftover
was tested by its DEGREE -- a leftover of degree 0 was read as "the class
makes the residual" -- which is false for a nonzero CONSTANT other than
1, the residual then being a member product times a content the family
cannot supply. Every one of the 35 leftover lines run 2 printed is 1 or a
genuine polynomial, so no cell was misread; the test now compares against
1 and a constant leftover fires K6. The other edits are print strings: ARM 3's header said
"three rows" beside a parameterised cell count, its closing line read
"0 of those 0" at a sweep that finds nothing, and the banner asked whether
the CLASS is finite where the question is about its generators. The rig was re-smoked at ranks 21..22 with one extra cell after
all three, every arm exercised including ARM 3's empty path, and rank 21
and 22's rows reproduce run 2's exactly.

ONE SMOKE RUN before run 1, at ranks 21..22 with EXTRA_CELLS = 1 and
J_CAP = 32, exercising every stage including a mint and its admit test.
It found no fault: rank 22 re-minted D from the seed by the same path,
which is the control this rig turns on, and the restricted range fired K1
and K7 exactly as a restricted range must.
"""
import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import itertools
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_flatten_family import (polydiv, split_witness, on_unit_circle,
                                    phi_poly, basis, lll_incr, det_pm1,
                                    enum_ball, clears, NodeCap)
from fractions import Fraction as F
from explore_flatten_band import mulp, xm1_pow, height
from explore_flatten_near import adm_cofactors, pure_min
from explore_flatten_swap import (mult_table, blocks, pure_family_min,
                                  swap_min, cyc_multiset, PROD)

# The class as SEEDED -- the chart's own three, with D deliberately
# absent so that rank 22 has to re-mint it.
SEED = (("A", [2, 4, 5, 4, 2]), ("B", [2, 3, 2]), ("C", [3, 5, 3]))
# The band rig's committed first failing depths, and the parent rig's
# rank-22 numbers. Re-derived here, never taken.
KEY_JLO = {19: 26, 20: 23, 21: 25, 22: 30}
KEY_R22 = (42222, 44108, [3, 9, 15, 17, 15, 9, 3])

RANK_LO = 19
RANK_HI = 26
J_CAP = 40
NODE_CAP = 400000
EXTRA_CELLS = 3


# ------------------------------------------------- the capped lattice

def route_h_capped(M, J, cap):
    """route_h with the Fincke-Pohst walk capped. Returns (h, witness)
    or (None, None) when the cap is hit, so a cell too dear to decide is
    reported as UNDECIDED rather than silently skipped or waited on."""
    B, T, mu, A = lll_incr(basis(M, J))
    if not det_pm1(T):
        raise ValueError("basis corruption at M=%d J=%d" % (M, J))
    H = min(max(abs(c) for c in b) for b in B)
    try:
        h, v, _ = enum_ball(B, mu, A, M, F(H * H * M), cap)
    except NodeCap:
        return None, None
    if h is None or h > H:
        raise ValueError("ceiling violation at M=%d J=%d" % (M, J))
    ok, _ = clears(v, J)
    if not ok:
        raise ValueError("witness not divisible at M=%d J=%d" % (M, J))
    return h, v


# ------------------------------------------------------ the leftover

def leftover(R, members):
    """R divided by each member repeatedly, in the order given. Returns
    (the leftover, the names divided out)."""
    rest, used = list(R), []
    for (nm, m) in members:
        while True:
            d = polydiv(rest, m)
            if d is None:
                break
            rest = d
            used.append(nm)
    return rest, used


def leftover_stable(R, members):
    """The leftover over EVERY permutation of the members. Returns the
    set of distinct leftovers, which C4 requires to be a singleton."""
    out = set()
    for perm in itertools.permutations(members):
        rest, _ = leftover(R, perm)
        out.add(tuple(rest))
    return out


def parent_for(Smin, g, r, J):
    """An admissible pure cofactor whose cyclotomic multiset contains
    Smin with exactly g degrees to spare, or None. Separates a PARENT
    obstruction from a MULTIPLIER one."""
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
            return (S, sorted(rem))
    return None


def describe_member(p):
    """The five things a minted member owes: degree, height, value at 1,
    reciprocity, the exact Sturm circle test, and its cyclotomic part
    (which must be empty for a residual)."""
    return dict(deg=len(p) - 1, height=height(p), at1=sum(p),
                recip=list(reversed(p)) == p,
                circle=on_unit_circle(p)[0],
                cyc=split_witness(list(p))[1],
                positive=all(c > 0 for c in p))


def swap_at(r, J, members, xm1):
    """(hs0, hs) with the given class at the cell."""
    PROD.clear()
    MT = mult_table(tuple(members), r - 1)
    bl = blocks(r, J, sorted(MT))
    hs0 = pure_family_min(bl, xm1)
    hs, _ = swap_min(bl, MT, xm1, hs0)
    return hs0, hs


def reconstruct(q):
    """split_witness's own output multiplied back (C3): x^s times the
    sign times prod(S_min) times R against the cofactor itself. Returns
    (the split, whether it reconstructs)."""
    sh, S, R = split_witness(list(q))
    p = list(R)
    for d in S:
        p = mulp(p, phi_poly(d))
    p = [0] * sh + p
    t = list(q)
    while len(t) > 1 and t[-1] == 0:
        t.pop()
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return (sh, S, R), (t == p or t == [-c for c in p])


# ------------------------------------------------------------- the run

def decide_cell(r, J, cap):
    """(h, witness, ph, verdict) at one cell. verdict is 'F' failing,
    '.' clean, or '?' undecided because the walk hit the cap."""
    M = J + r
    xm1 = xm1_pow(J)
    h, v = route_h_capped(M, J, cap)
    ph, _, _, _ = pure_min(r, J, xm1)
    if h is None:
        return None, None, ph, "?"
    return h, v, ph, ("F" if h < ph else ".")


TALLY = dict(C2=0, C3=0, C4perm=0, cells=0)


def examine(r, J, h, v, members, fired):
    """One failing cell, fully: the split, the leftover against the
    class in hand, the permutation check, the parent search, and the
    swap family's hs0 and hs with the class in hand."""
    xm1 = xm1_pow(J)
    q = polydiv(v, xm1)
    (sh, S, R), rebuilt = reconstruct(q)
    if not rebuilt:
        fired["C3"] += 1
        print("      C3 the split does not reconstruct at r=%d J=%d"
              % (r, J))
    TALLY["cells"] += 1
    if rebuilt:
        TALLY["C3"] += 1
    rest, used = leftover(R, members)
    alt = leftover_stable(R, members)
    if len(alt) == 1:
        TALLY["C4perm"] += 1
    if len(alt) > 1:
        fired["K8"] += 1
        print("      K8 the leftover moves with the member order at "
              "r=%d J=%d: %s" % (r, J, sorted(alt)))
    if len(rest) == 1 and rest != [1]:
        # A leftover that is a nonzero CONSTANT other than 1 means the
        # residual is a member product times a content the family cannot
        # supply, and reading it as "the class makes the residual" would
        # be false. No cell of this walk produced one; the guard is here
        # because the degree test alone would not have said so.
        fired["K6"] += 1
        print("      K6 the leftover is the constant %s at r=%d J=%d"
              % (rest, r, J))
    g = len(R) - 1
    par = parent_for(S, g, r, J)
    hs0, hs = swap_at(r, J, members, xm1)
    return dict(J=J, M=J + r, h=h, hs0=hs0, hs=hs, R=list(R), S=S,
                shift=sh, rest=list(rest), used=used, parent=par,
                minted=None, hsx=None)


def main():
    t_all = time.time()
    fired = dict((k, 0) for k in
                 ("K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8", "C3"))

    print("=" * 70)
    print("explore_flatten_class.py -- is the multiplier class "
          "finitely generated?")
    print("=" * 70)

    members = list(SEED)

    # -------------------------------------------------------------- C5
    print("\n[C5] the class as SEEDED, before anything is measured. D is "
          "deliberately absent: rank 22 has to re-mint it by the same "
          "code path every new rank uses.")
    for (nm, p) in members:
        d = describe_member(p)
        print("   %-3s %-24s deg %d  height %d  P(1) %3d  reciprocal "
              "%-5s  on the circle %-5s  cyclotomic part %s"
              % (nm, str(p), d["deg"], d["height"], d["at1"], d["recip"],
                 d["circle"], list(d["cyc"]) or "(none)"))

    # ------------------------------------------------------------ ARM 1
    print("\nARM 1 -- THE WALK. Each rank's column scanned J = 2 upward "
          "to the first failure, route_h capped at %d nodes; a cell over "
          "the cap is UNDECIDED and a first failure is claimed only when "
          "every cell below it was decided." % NODE_CAP)
    first = {}
    cells = {}
    undecided = {}
    minted_at = {}
    for r in range(RANK_LO, RANK_HI + 1):
        t_r = time.time()
        und = []
        got = None
        for J in range(2, J_CAP + 1):
            h, v, ph, verdict = decide_cell(r, J, NODE_CAP)
            if verdict == "?":
                und.append(J)
                continue
            if h > ph:
                fired["K6"] += 1
                print("   K6 h above ph at r=%d J=%d: %d > %d"
                      % (r, J, h, ph))
            if verdict == "F":
                got = (J, h, v, ph)
                break
        undecided[r] = und
        if got is None:
            print("   rank %2d: NO failure up to J = %d%s"
                  % (r, J_CAP,
                     "; undecided at %s" % und if und else ""))
            sys.stdout.flush()
            continue
        J, h, v, ph = got
        below = [j for j in und if j < J]
        e = examine(r, J, h, v, members, fired)
        e["ph"] = ph
        cells[r] = e
        first[r] = J
        if e["hs"] < h or e["hs"] > ph or e["hs0"] != ph:
            fired["K6"] += 1
            print("   K6 bracket at r=%d J=%d: h=%d hs0=%d hs=%d ph=%d"
                  % (r, J, h, e["hs0"], e["hs"], ph))
        else:
            TALLY["C2"] += 1
        print("\n   rank %2d: first failure at J = %d (M = %d)%s"
              % (r, J, J + r,
                 "  -- UNDECIDED BELOW IT AT %s, so this depth is an "
                 "UPPER BOUND" % below if below else ""))
        print("      h = %d, ph = %d, hs = %d with the class in hand "
              "(%s); the filter %s"
              % (h, ph, e["hs"], ",".join(nm for nm, _ in members),
                 "FIRES, hs < ph" if e["hs"] < ph else "is SILENT, hs = ph"))
        print("      residual %s, cyclotomic multiset %s"
              % (e["R"], list(e["S"])))
        print("      divided by the members it carries %s leaves %s"
              % (e["used"] or "(none)", e["rest"]))
        if not e["parent"]:
            fired["K4"] += 1
            print("      K4 NO admissible parent holds %s with %d to "
                  "spare -- a PARENT obstruction, and no member is "
                  "minted here" % (list(e["S"]), len(e["R"]) - 1))
        else:
            print("      an admissible parent holds it with %d to spare: "
                  "%s, block %s"
                  % (len(e["R"]) - 1, list(e["parent"][0]), e["parent"][1]))
        if e["rest"] != [1] and e["parent"]:
            nm = chr(ord("D") + len(members) - 3)
            d = describe_member(e["rest"])
            print("      A NEW MEMBER %s = %s: deg %d, height %d, "
                  "value at 1 = %d, reciprocal %s, on the circle %s, "
                  "cyclotomic part %s, all coefficients positive %s"
                  % (nm, e["rest"], d["deg"], d["height"], d["at1"],
                     d["recip"], d["circle"],
                     list(d["cyc"]) or "(none)", d["positive"]))
            if not (d["recip"] and d["circle"] and not d["cyc"]
                    and d["positive"]):
                fired["K3"] += 1
                print("      K3 the minted member does not have D's shape")
            for (onm, om) in members:
                if polydiv(e["rest"], om) is not None:
                    print("      the leftover is divisible by %s, so it "
                          "is not a new object" % onm)
            ext = members + [(nm, list(e["rest"]))]
            _, hsx = swap_at(r, J, ext, xm1_pow(J))
            e["hsx"] = hsx
            print("      with %s admitted, hs = %d against h = %d -- %s"
                  % (nm, hsx, h, "reached" if hsx == h
                     else "STILL NOT REACHED"))
            if hsx != h:
                fired["K6"] += 1
                print("      K6 admitting the leftover does not reach h")
            e["minted"] = nm
            minted_at[r] = (nm, list(e["rest"]))
            members = ext
        elif e["rest"] == [1]:
            print("      the class in hand MAKES the residual, and hs = "
                  "h is %s" % (e["hs"] == h))
        print("      (rank %d in %.1f s)" % (r, time.time() - t_r))
        sys.stdout.flush()

    # ---------------------------------------------------- C1: the key
    print("\n[C1] the answer key, RE-DERIVED: the band rig's first "
          "failing depths at ranks 19..22 and the parent rig's rank-22 "
          "numbers")
    keyok = True
    for r in sorted(KEY_JLO):
        got = first.get(r)
        ok = (got == KEY_JLO[r]
              and not [j for j in undecided.get(r, []) if j < KEY_JLO[r]])
        keyok = keyok and ok
        print("   rank %d: first failure at J = %s (key %d) %s"
              % (r, got, KEY_JLO[r], "ok" if ok else "MISMATCH"))
    c22 = cells.get(22)
    if c22:
        ok22 = (c22["h"], c22["hs"], c22["rest"]) == KEY_R22
        keyok = keyok and ok22
        print("   rank 22: h = %d (key %d), hs = %d (key %d), leftover "
              "%s (key %s) %s"
              % (c22["h"], KEY_R22[0], c22["hs"], KEY_R22[1],
                 c22["rest"], KEY_R22[2], "ok" if ok22 else "MISMATCH"))
    else:
        keyok = False
        print("   rank 22: no first failing cell decided")
    if not keyok:
        fired["K7"] += 1
        print("   K7 the answer key is not reproduced")

    # ------------------------------------------------- P1, P2, P3, P5
    print("\n   THE WALK'S VERDICT, rank by rank")
    print("   %4s %4s %4s %11s %11s %11s %8s %-28s %s"
          % ("r", "J", "M", "h", "hs", "ph", "filter", "residual",
             "what the class had to gain"))
    grew = held = 0
    for r in sorted(cells):
        e = cells[r]
        print("   %4d %4d %4d %11d %11d %11d %8s %-28s %s"
              % (r, e["J"], e["M"], e["h"], e["hs"], e["ph"],
                 "fires" if e["hs"] < e["ph"] else "silent",
                 str(e["R"]),
                 ("%s = %s" % (e["minted"], e["rest"])) if e["minted"]
                 else ("nothing, the residual is %s"
                       % (" ".join(e["used"]) or "1"))))
        if r <= 22:
            continue
        if e["minted"]:
            grew += 1
        else:
            held += 1
        if (e["minted"] is not None) != (e["hs"] == e["ph"]):
            fired["K5"] += 1
            print("      K5 rank %d mints %s while the filter %s"
                  % (r, e["minted"], "fires" if e["hs"] < e["ph"]
                     else "is silent"))
    print("   above rank 22: %d ranks minted a member and %d were "
          "reached by the class in hand" % (grew, held))
    if grew == 0:
        fired["K1"] += 1
        print("   K1 no rank above 22 minted a member")
    if held == 0 and grew:
        fired["K2"] += 1
        print("   K2 every rank above 22 minted a member")

    print("\n   THE CLASS AT THE END OF THE WALK: %s"
          % ", ".join(nm for nm, _ in members))
    for (nm, p) in members:
        d = describe_member(p)
        print("      %-3s %-32s deg %d height %d value at 1 %d "
              "reciprocal %s circle %s positive %s"
              % (nm, str(p), d["deg"], d["height"], d["at1"], d["recip"],
                 d["circle"], d["positive"]))

    # ------------------------------------------------------------ ARM 2
    print("\nARM 2 -- IS A MEMBER THE RANK'S OR THE CELL'S? The next %d "
          "failing cells of each MINTING rank's own column, against the "
          "class as it stood at the end of the walk." % EXTRA_CELLS)
    for r in sorted(minted_at):
        J0 = first[r]
        n = 0
        for J in range(J0 + 1, J_CAP + 1):
            if n >= EXTRA_CELLS:
                break
            h, v, ph, verdict = decide_cell(r, J, NODE_CAP)
            if verdict == "?":
                print("   r=%d J=%d UNDECIDED at the cap" % (r, J))
                continue
            if verdict != "F":
                continue
            n += 1
            e = examine(r, J, h, v, members, fired)
            print("   r=%d J=%d M=%d: h=%d hs=%d ph=%d, residual %s, "
                  "divided by %s leaves %s"
                  % (r, J, J + r, h, e["hs"], ph, e["R"],
                     e["used"] or "(none)", e["rest"]))
            if e["rest"] != [1]:
                d = describe_member(e["rest"])
                print("      A FURTHER member at the SAME rank: deg %d "
                      "height %d value at 1 %d reciprocal %s circle %s "
                      "positive %s" % (d["deg"], d["height"], d["at1"],
                                       d["recip"], d["circle"],
                                       d["positive"]))
            sys.stdout.flush()

    # ------------------------------------------------------------ ARM 3
    print("\nARM 3 -- IS THE CLASS A PER-RANK OBJECT? The next %d "
          "failing cells of EVERY scanned rank's own column, examined "
          "in full: the residual, the leftover against the class at the "
          "end of the walk, the parent search and the admit test. It "
          "SUBSUMES ARM 2 at rank 22, whose three rows must reproduce "
          "inside it. Added in a second run; no arm before it changes."
          % EXTRA_CELLS)
    deep = []
    for r in sorted(cells):
        J0 = first[r]
        n = 0
        for J in range(J0 + 1, J_CAP + 1):
            if n >= EXTRA_CELLS:
                break
            h, v, ph, verdict = decide_cell(r, J, NODE_CAP)
            if verdict == "?":
                print("   r=%d J=%d UNDECIDED at the cap" % (r, J))
                continue
            if verdict != "F":
                continue
            n += 1
            e = examine(r, J, h, v, members, fired)
            print("   r=%d J=%d M=%d: h=%d hs=%d ph=%d, residual %s, "
                  "divided by %s leaves %s"
                  % (r, J, J + r, h, e["hs"], ph, e["R"],
                     e["used"] or "(none)", e["rest"]))
            if e["hs"] < h or e["hs"] > ph or e["hs0"] != ph:
                fired["K6"] += 1
                print("      K6 bracket at r=%d J=%d" % (r, J))
            else:
                TALLY["C2"] += 1
            if e["rest"] == [1]:
                continue
            deep.append((r, J, list(e["rest"])))
            d = describe_member(e["rest"])
            print("      A MEMBER THE FIRST CELL OF THIS RANK DID NOT "
                  "SHOW: %s -- deg %d, height %d, value at 1 %d, "
                  "reciprocal %s, ALL ROOTS ON THE CIRCLE %s, cyclotomic "
                  "part %s, all coefficients positive %s"
                  % (e["rest"], d["deg"], d["height"], d["at1"],
                     d["recip"], d["circle"],
                     list(d["cyc"]) or "(none)", d["positive"]))
            par = e["parent"]
            print("      an admissible parent holding %s with %d to "
                  "spare: %s" % (list(e["S"]), len(e["R"]) - 1,
                                 "yes" if par else "NO -- a PARENT "
                                 "obstruction"))
            if par:
                nm = "X%d.%d" % (r, J)
                _, hsx = swap_at(r, J, members + [(nm, list(e["rest"]))],
                                 xm1_pow(J))
                print("      with it admitted, hs = %d against h = %d "
                      "-- %s" % (hsx, h,
                                 "reached" if hsx == h
                                 else "STILL NOT REACHED"))
            sys.stdout.flush()
    print("   %d of the cells ARM 3 examined need a multiplier the "
          "class at the end of the walk cannot make" % len(deep))
    off = [z for z in deep if not on_unit_circle(z[2])[0]]
    print("   and of those, %d carry a root OFF the unit circle, which "
          "is the class the chart's own census is described by"
          % len(off))
    for (r, J, pz) in off:
        print("      r=%d J=%d M=%d: %s" % (r, J, J + r, pz))

    print("\n[C2, C3, C4] the controls that pass SILENTLY, counted so that a "
          "control which RAN cannot be told apart from one that did not by "
          "reading this output")
    print("   %d cells examined; the bracket h <= hs <= ph with hs0 = ph holds "
          "at %d of the cells it is checked at; the split reconstructs its own "
          "cofactor at %d; and the leftover is the same over EVERY permutation "
          "of the members in hand at %d"
          % (TALLY["cells"], TALLY["C2"], TALLY["C3"], TALLY["C4perm"]))

    # ------------------------------------------------------- the tally
    print("\n" + "=" * 70)
    hit = ", ".join("%s x%d" % (k, n) for k, n in sorted(fired.items()) if n)
    print("KILLS FIRED: %s" % (hit or "none"))
    print("wall %.1f s" % (time.time() - t_all))
    print("=" * 70)


if __name__ == "__main__":
    main()
