"""explore_bare_cost.py -- the four laws under a cost the schedule family
cannot express.

THE QUESTION. Every law the greedy corpus has derived about limits, degree
ceilings, stopping and mixed universes was derived over a family whose price
is price(degree, sigma) with sigma the DOOR -- and under a per-item clock the
door is gap(depth) on the item's own ladder. So every price in the family
factors as f(degree, gap(depth)): a function of the item's OWN two
coordinates and of nothing else in the state.

A ring's cost does not factor that way. explore_populated_door.py F1 gives a
seated place's door as the least r with v_p(lambda(P^(e+r))) > v_p(L), and
F3 decomposes v_p(L) as a max over the OTHER seated places -- a place over
another prime contributing v_p(N(Q) - 1), its RESIDUE CARDINALITY, with its
own depth absent. So a seated place's price reads a number no item of its
own owns, and F8 (iv) files the consequence as unstarted: an item's price in
the family is a function of its own exponent, so the correction cannot be
carried there, and what a family admitting c(item, depth, state) does to the
four laws is a separate build.

This is that build. It runs the four laws -- the limit's shape, the degree
ceiling, the stop law, and the mixed universe's min over products -- over two
costs outside the family, and asks whether those laws are about WALKS or
about LADDERS. If they survive, the family was a convenience. If they break,
the corpus's ring readings are scoped to states where no other place's
residue field bites.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. The suspicion is
written in the SCHEDULE family's words -- ladder, gap, price, door, budget,
runaway, strand -- and that is the vocabulary under test, which is a hazard
and not a convenience: a rig that can only say "gap" cannot notice a cost
whose widening has no gap in it. So the cost object here is given its own
two-line interface -- a DOOR and a PRICE, both reading the whole state --
and the family is re-expressed THROUGH it (S1) rather than the new costs
being expressed through the family. The words that survive that inversion are
the ones the laws are allowed to keep.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 From the RING to the abstraction. The tag cost below is an abstraction of
    explore_populated_door.py's measured door, not that door. What is carried
    is the SHAPE -- a max over other seated items entering one item's door --
    and what is deliberately dropped is all of the arithmetic: no norms, no
    primes, no lambda. Whether the abstraction is faithful is checked in one
    place and one only (PR2's closed form), and everything else is a fact
    about the abstraction.
 T2 From the SEATED sweep to the walk. F1's identity is measured at seated
    readings. Nothing here inherits its 717 readings; the abstract door is
    defined for unseated items too (an opening at a covered degree) and that
    cell has no measured counterpart.
 T3 From the per-item clock to the global one. The tag cost reads an item's
    own column and never a shared tick, so it is per-item NATIVE and is run
    under that clock alone; a ring's clock is per-item (explore_tick_pump.py
    F9). Cost B keeps the family's tick-read door and is run under both.
 T4 From F4's UNREACHABILITY to this rig. F4 says a ring walk never builds a
    state carrying two seated places of equal characteristic, so the exponent
    route never fires. That is a fact about RINGS. Here the char assignment
    is a dial, and the "one char" regime builds exactly the state a ring
    cannot -- which is the point of having an abstraction at all.
 T5 From the factor family to a bare cost: b, and everything indexed by it.
    The ceiling formula's ratio is re-derived at each cost and not inherited.

THE HAND-ATTACK, on paper before any engine code.

 A. THE TAG COST, and what it abstracts. An item carries a ladder S_i and the
    valuation that ladder is the jump set of, v_i(a) = #{s in S_i : s < a}
    (explore_tick_pump.py hand-attack A). Give it two more coordinates: a TAG
    t_i, an integer standing for v_p of its own lambda column -- what it
    contributes to an item of a DIFFERENT characteristic -- and a CHAR c_i.
    Then for item i standing at depth e,

        M_i(state) = max over seated j != i of
                       ( v_j(e_j) if c_j == c_i else t_j )
        door_i(e, state) = least r >= 1 with v_i(e+r) > max(v_i(e), M_i)

    M_i is the abstract v_p(L), and the two branches are F3's two routes: the
    same-char branch is the EXPONENT route, moving with the other item's own
    DEPTH, and the other is the RESIDUE route, reading a constant with that
    item's depth absent. The price stays the family's price(degree, door), so
    the ONLY thing that leaves the family is that the door reads the state.

 B. THE ABSTRACTION IS FAITHFUL AT ONE CHECKABLE POINT. On the exact ladder
    v(a) = a - 1, so door = least r with e + r - 1 > max(e - 1, M), which is
    1 when M <= e - 1 and M - e + 2 otherwise. That is
    explore_populated_door.py F2's closed form door_pop = v_p(L) - e + 2
    verbatim, with its scope (the cyclic case) coming out as the exact
    ladder. PR2 checks it; nothing else here claims to be about a ring.

 C. THE TAG DOOR IS SELF-CORRECTING, which is the whole of what B1 predicts.
    The door is BY DEFINITION the least climb that outruns M, so an item that
    pays a widened door LANDS at a depth whose valuation exceeds M, and then
    pays its lone gap until M overtakes it again. M is non-decreasing along a
    walk, seating never unseating, so once a walk locks M is constant and the
    recurrent item is permanently past it. Hence the widening is a TRANSIENT
    for the runaway and PERMANENT for a strand, which stands shallow forever.
    Two consequences, and they pull opposite ways:
      - the stop law should SURVIVE, the recurrent price falling back to the
        lone gap. This is the slate's SAFETY MARGIN and a margin is the half
        to distrust: it is the half derived from a picture rather than from
        an inequality.
      - the min-over-products law should NOT survive as stated. An item's
        recurrent price is price(degree, POPULATED door at its standing
        depth), which equals its lone tail gap for the runaway and does not
        for a strand. So the naive product UNDER-PRICES strands, and the
        correction is stated before the run rather than fitted after it.

 D. COST B, degree x landing depth. c = degree * (the depth the move lands
    at). On a constant-gap ladder gap(depth) is constant, so f(degree, gap)
    cannot see the depth at all while d * (e + r) grows along the trajectory.
    Its door is the family's, so this cost isolates the PRICE's dependence on
    the state from the DOOR's.

 E. AND COST B COLLAPSES THE DEGREE CEILING TO d_min, EXACTLY. Take the
    planted two-item instrument (explore_tick_pump.py `planted`): a stale
    item of degree D at exponent e = T_prev + 1 with door lo = T - T_prev, so
    it LANDS at e + lo = T + 1 and costs D * (T + 1). Its rival is an
    unseated item of degree d_min at a covered degree, door T + 1 - 0,
    landing at T + 1 and costing d_min * (T + 1). The stale item is in the
    minimum iff D <= d_min -- at EVERY ladder and EVERY tick. The ratio
    (T + 1)/(T - T_prev) that carries the whole family formula cancels
    identically. This is the derived half of the slate.

 F. AND UNDER COST B A BOUNDED GAP DOES NOT STOP THE LADDER. The recurrent
    price d_deep * (e + 1) grows without bound with the item's own depth
    while the opening curve grows only with the degree.
    explore_tick_pump.py F10 already sharpened the stop law into a COMPARISON
    of two curves -- a bounded recurrent price against an opening curve
    growing without bound -- and found cells where the SECOND half fails.
    Cost B is the first where the FIRST half fails, so it tests the sharpened
    law rather than the slogan.

 G. THE SOUNDNESS PRECONDITION THE NEW CLASS CAN BREAK SILENTLY. PWalk.menu
    stops its scan at the first degree whose price(d, 1) already beats the
    best found. That is sound iff (i) every candidate at degree d costs at
    least floor(d) and (ii) floor is non-decreasing in d. Both survive at
    both costs here -- the tag cost keeps price(d, sigma) with sigma >= 1 and
    a price non-decreasing in sigma, and cost B has floor(d) = d -- but they
    are now properties of the COST rather than of the family, and a broken
    one returns a NON-MINIMAL menu with no assert firing, which would put
    every law below on the wrong walk. So they are checked and not argued: a
    brute full-scan menu beside the early-stop one, agreeing at every step of
    every walk, plus a monotonicity check per cost.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 THE CONTROL, run before any kill-or-survive result is read.
    (a) The brute full-scan menu equals the early-stop menu -- cost AND the
        whole tie list -- at every step of every cell of every cost.
    (b) The family's own schedule, re-expressed through the cost interface,
        reproduces explore_tick_pump.py's PWalk move for move over the S2
        cell, at five ladders and both clocks.
    (c) The tag cost at ALL TAGS ZERO reproduces the family cost move for
        move under a per-item clock, at every ladder.
    What the rig PRINTS: the cells compared, the states per cell, the
    disagreement counts.
    KILL: one disagreement in a cost, a tie list, or a final state.

PR2 THE TAG COST IS OUTSIDE THE FAMILY, AND FAITHFUL WHERE IT CLAIMS TO BE.
    On the exact ladder the populated door reads max(1, M - e + 2) at every
    (e, M) in range; and across the states of at least one walk, some
    (item, depth) pair reads TWO different doors -- which is precisely what
    no schedule in the family can do.
    What the rig PRINTS: the door table per ladder against M, the closed-form
    check count, and the number of (item, depth) pairs carrying more than one
    door over a walk.
    KILL: every (item, depth) pair reads a single door across all states of
    all walks -- the cost would be a schedule after all and the build is
    empty.

PR3 THE STOP LAW SURVIVES THE TAG COST, at bounded tags and at growing ones,
    by C. MARGIN FLAG: this is the safety half of the slate.
    What the rig PRINTS: per (ladder, tag regime) cell, the max gap, whether
    the cost tail is flat, how many degrees the walk OPENS in its last
    stretch, and the two curves the sharpened law compares -- the recurrent
    price and the least-uncovered opening price.
    KILL, as an observable: a bounded-gap cell whose last stretch carries an
    opening.

PR4 THE MIN-OVER-PRODUCTS LAW NEEDS THE POPULATED DOOR, AND THAT IS THE
    CORRECTION. The naive product -- price(degree, the item's LONE tail gap)
    -- mispredicts the flat tail minimum at at least one tag cell. The
    corrected product -- price(degree, the POPULATED door at the item's
    standing depth, read at the final state) -- equals it at every cell; the
    runaway is a corrected-argmin; every strand's corrected product is at or
    above the budget; and the runaway's corrected product equals its naive
    one, the runaway standing past M.
    What the rig PRINTS: per cell, the budget, both predictions, the runaway,
    the strands with both products.
    KILL: the corrected law failing at any cell.

PR5 THE TAG COST CHANGES THE WALK AND NOT ONLY ITS PRICES. At at least one
    cell the seated multiset or the runaway differs from the zero-tag control
    -- which is explore_populated_door.py F8 (v), whether a widened door ever
    changes which place is SEATED rather than only what a stranded one is
    priced at, asked with the arithmetic stripped off.
    What the rig PRINTS: per cell, the diff against the zero-tag control --
    degrees seated, count above exponent 1, the runaway.
    KILL: none frozen. Both outcomes are readings and the print is the diff.

PR6 THE DEGREE CEILING.
    (a) Under the tag cost the largest degree carrying an item above exponent
        1 is at or below the zero-tag control's at every cell, widened doors
        raising the price of a MOVE while leaving an uncovered degree's
        opening at door 1.
    (b) Under cost B the planted ceiling is EXACTLY d_min at every ladder and
        every tick, by E -- against the family's own bound_at at the same
        planted readings, which is where the ratio still lives.
    What the rig PRINTS: (a) the deepest-carrying degree per cell beside the
    control's; (b) the planted ceiling and the family bound side by side at
    three ladder members of each ladder.
    KILL: (a) a cell above the control; (b) one planted reading whose ceiling
    is not d_min.

PR7 UNDER COST B A BOUNDED GAP DOES NOT STOP, by F. Every ladder climbs --
    the exact one included -- and the sharpened two-curve law reads it right
    where the slogan does not.
    What the rig PRINTS: per (ladder, clock), the tail openings, whether the
    cost tail is flat, and the recurrent price against the opening price.
    KILL: the exact ladder stopping under cost B, its recurrent price being
    unbounded by construction.

PR8 THE LIMIT'S SHAPE UNDER COST B. What the rig PRINTS: per cell, how many
    items stand above exponent 1, the deep items' degrees and exponents, and
    the least uncovered degree.
    KILL: none frozen -- the filed theorem is proved inside the family and
    this is the first reading outside it, so the observable is recorded and
    weighed after the run.

POSITIVE CONTROL, run before any kill-or-survive result is read (S0 and S1).
S0 forces every check the run leans on to fail once. S1 is PR1: the walker is
certified against explore_tick_pump.py's PWalk through the family's own
schedule, and the tag cost is certified against the family at zero tags. A
rig whose walker is new cannot report a law's death without first showing it
reproduces the law's life.

THE SECTIONS.
  S0  forced failures.
  S1  PR1 -- the control: brute against early-stop, and the family reproduced.
  S2  PR2 -- the tag door: the closed form, and leaving the family.
  S3  PR3, PR4, PR5, PR6 (a) -- the four laws under the tag cost.
  S4  PR6 (b), PR7, PR8 -- the ceiling, the stop law and the limit under
      cost B.
  S5  the verdict table: which law survived which cost.

F1 THE WALKER IS THE CERTIFIED ONE AND THE EARLY STOP IS SOUND AT BOTH COSTS
   (rule in range; 900 (state, walker) pairs for the reproductions, and 3120
   walk states carrying a brute full-scan menu beside the early-stop one, 0
   disagreements -- 1800 in the tag sweep, 1200 under the second cost and 120
   in the control's own cells). The family's own schedule, re-expressed through the cost
   interface, reproduces explore_tick_pump.py's PWalk move for move at five
   ladders and both clocks; the tag cost at ALL TAGS ZERO reproduces the
   family at five ladders under a per-item clock, which is the regime in
   which the two are one object. The soundness precondition the handover
   worried about did not bite -- both costs keep a price non-decreasing in
   the door and a door at or above 1, so the scan's lower bound survives --
   but it is now CHECKED per cost rather than inherited from the family, and
   S0 shows what a cost that undercuts its own floor does to the menu: the
   brute twin parts from the early stop at once (2 against 1) and no other
   assert in the rig fires.

F2 THE ABSTRACT DOOR REPRODUCES THE RING'S CLOSED FORM, AND ITS SHAPE
   INVERTS THE LADDER'S VALUATION (PROPERTY for the inversion, which follows
   from the door's definition; the closed form checked at 64 readings). On
   the exact ladder the door reads max(1, M - e + 2) at every (e, M) in
   range, which is explore_populated_door.py F2's door_pop = v_p(L) - e + 2
   verbatim. Its scope lines up too -- a cyclic column (q-1)p^(a-1) has
   v_p = a - 1 and so jump set every integer, which is the exact ladder --
   but that correspondence is a one-line consequence of the ladder BEING
   lambda's jump set, which is the abstraction's own premise (T1) and not
   something this rig measures. What the rig checks is the door formula. The door is by definition
   the least climb that OUTRUNS M, so it inverts the ladder's own valuation:
   at M = 0..7 it reads 1..8 on the exact ladder, 1, 3, 5, 7, ... at gap 2,
   1, 4, 7, 10, ... at gap 3, 1, 4, 9, 16, ... on the squares, and 1, 2, 4,
   8, 16, 32, 64, 128 on the doubling ladder. So a MULTIPLICATIVE ladder
   prices its own state-widened move out of every tabulated range at once --
   a climb exponential in M -- which is why the walk sweep is the
   constant-gap ladders, the ones a mixed-characteristic place carries
   (explore_tick_pump.py hand-attack F). That scoping is derived from the
   cost and is not a limit of the rig.

F3 WHAT COSTS THE FAMILY ITS SHAPE IS THE TAG'S VARIANCE AND NOT ITS SIZE,
   AND SHAPE IS NOT MEMBERSHIP (rule in range for the counts; 5 regimes x 3
   ladders, 121 (item, depth) pairs read at every state of a 120-move walk.
   PROPERTY for the non-membership, which follows from every ladder here
   containing 1). Under a UNIFORM tag, M is one number at every state and
   every item, so the door is a function of the item's own degree and
   exponent again -- 0 pairs of 121 read two doors, at all three ladders.
   The regimes that lose that shape are the ones whose tags DIFFER across
   items: tag = degree reads 120 multi-door pairs of 121 with M running
   9..122, the one-char (exponent) route reads 2 or 3 with M running 0..120,
   and the sparse regime reads 5 at gap 3 and 0 at the other two. 372
   multi-door pairs in all, so PR2's kill did not fire -- but its first
   firing, on a uniform tag alone, is the finding: a state's surplus is
   invisible only when the state's items agree about it.
   AND THE UNIFORM REGIME IS STILL NOT A MEMBER OF THE FAMILY, which the
   multi-door count alone was read as showing and does not. Having the
   family's SHAPE -- a price factoring through the item's own two
   coordinates -- is weaker than being some ladder's gap. Every ladder here
   contains 1, which the Pump constructor asserts and which is what makes
   the initial tick a legal clock position, so every one of them has
   gap(1) = 1; a uniform tag T charges T + 1 at depth 1. Checked at all five
   ladders. So the uniform regime sits inside the family's shape and outside
   every one of its members, and "a schedule in disguise" is the wrong
   reading of a true count.
   Read back at the ring, the excess is set by the SPREAD of the seated
   residue cardinalities and not by their magnitude.

F4 THE STOP LAW BREAKS, ONLY WHERE THE TAG GROWS WITHOUT BOUND, AND THE
   MECHANISM IS NOT THE ONE THE SLATE DERIVED (rule in range; 3 of 15 cells,
   120 moves each). PR3's kill fired at the tag = degree regime and at all
   three ladders -- gap 1, 2 and 3 alike, so this is not the bounded/
   unbounded gap axis wearing another hat. The cheapest recurrent move reads
   248, 494 and 740 against a cheapest opening of 124: the recurrent curve
   is ABOVE the opening curve, which is the first half of
   explore_tick_pump.py F10's two-curve law failing -- where the only cells
   of its own 112 that fail at all, the 12 degree-blind ones, fail at the
   second.
   AND THE HAND-ATTACK'S SAFETY MARGIN WAS THE WRONG HALF, which is the
   half to expect. C argued the widening is self-correcting -- an item that
   pays a widened door LANDS past M and then pays its lone gap -- and that
   is true of an item that MOVES. At tag = degree no item moves at all: 122
   items are seated, ZERO stand above exponent 1, and there is no runaway.
   Every opening raises M, so the first move is already unaffordable and the
   self-correction never gets to operate. The limit under a growing tag is
   therefore a shape the family has no name for: an ever-widening flat
   support with no deep coordinate in it, where the filed theorem says one
   runaway plus strands.

F5 THE BUDGET SURVIVES THE TAG COST AND THE STRAND CLASSIFICATION DOES NOT
   (rule in range; 12 stopping cells, 4 strand readings). At every stopping
   cell BOTH products predict the flat tail minimum, naive and corrected
   alike, and the reason is C's surviving half: the budget is set by the
   RUNAWAY, which stands past M, so its populated door IS its lone tail gap
   and the state cancels out of the one number the law predicts. The
   correction bites where the law SORTS rather than where it predicts.
   explore_tick_pump.py F9 splits a strand two ways -- a product strictly
   above the budget is priced out on every branch, one EQUAL to it stands in
   the final menu's own minimum and only by tie-break -- and at gap 3 under
   the sparse regime the naive product reads the degree-1 strand at 3,
   equal to the budget, calling it a TIE, while the corrected product reads
   18 and calls it priced out. The final menu is the arbiter and it does not
   carry that item: the corrected reading is right and the naive one is
   wrong, at 1 of the 4 strand readings, 0 for the corrected. So the filed
   law's PREDICTION is about walks and its SORT is about ladders.

F6 A WIDENED DOOR CHANGES WHAT IS SEATED, WHICH IS F8 (v) ANSWERED YES IN
   THE ABSTRACT (rule in range; 8 of 12 non-control cells). The open
   question was whether a widened door ever changes which place a walk
   SEATS, rather than only what a stranded place is priced at -- and the
   sweep there could not decide it, its one widened specimen being a strand
   precisely because it is never seated again. Here the walk parts from the
   zero-tag control at 8 of 12 cells, in the seated multiset or in the
   runaway. It parts even at the BOUNDED UNIFORM tag, the regime F3 shows
   keeps the family's SHAPE: tags 4 seats 7, 10 and 13 items against the
   control's 3, 3 and 5. So a re-pricing that factors through the item's own
   two coordinates still moves the walk, and the two questions -- does the
   cost keep the family's shape, does it change the walk -- are independent.

F7 THE DEGREE CEILING SURVIVES THE TAG COST AND COLLAPSES TO d_min UNDER
   degree x depth (rule in range for (a), 15 cells; PROPERTY for (b), argued
   at E and checked at 15 planted readings). (a) No cell carries an item
   above exponent 1 at a degree above the zero-tag control's, at any ladder
   or regime. (b) The planted two-item ceiling reads d_min = 3 at every
   ladder and every tick -- exact, gap 2, gap 3, doubling and squares alike
   -- against a family bound running 5 to 15 at the same readings. The
   stale item lands at T + 1 and so does its unseated rival, so the ratio
   (T + 1)/(T - T_prev) that the whole family formula is made of cancels
   identically. A cost that reads the LANDING DEPTH has no degree ceiling
   above the least degree at all.

F8 UNDER degree x depth EVERY LADDER CLIMBS, AND THE LIMIT'S SHAPE IS A
   GLOBAL-CLOCK FACT (rule in range; 10 of 10 cells, 120 moves each). The
   exact ladder climbs -- gap 1, the most bounded ladder there is -- and so
   do all four others, PR7's kill missing at every cell. The recurrent price
   d * (e + 1) grows with the item's own depth while the opening curve grows
   only with the degree, which is the sharpened two-curve law reading it
   right where the slogan "a bounded gap stops the ladder" does not.
   AND THE LIMIT SPLITS BY CLOCK -- which is the FILED split surviving, not
   a new one, and the correction is worth stating because the import made it
   easy to miss. explore_tick_pump.py F5 and F10 already hold that the limit
   theorem survives every ladder under a GLOBAL clock and breaks under a
   per-item one, gradedly: 1, 1, 3 and 6 items above exponent 1 at gaps 1,
   2, 3 and 5. Here the global side holds again -- exactly ONE item above
   exponent 1 at every one of the five ladders, standing at the least degree
   -- so the theorem's shape survives a cost the family cannot express, which
   is the reading. What is NEW is where the per-item side breaks: 20 to 44
   items above exponent 1, and 20 of them at the EXACT ladder, which is the
   one cell that holds inside the family at exactly 1. So the cost does not
   introduce the clock split; it pushes the split's break down to gap 1.

F9 WHAT IS LEFT OPEN. (i) A tag here is a constant per ITEM; a ring's
   v_p(N(Q) - 1) is a constant per (place, reading prime) PAIR, so a state
   whose places sit over several rational primes carries a different tag per
   reader. Not modelled, and it is the nearest thing to a gap between the
   abstraction and F3's decomposition. (ii) The one-char regime measures the
   exponent route, which F4 there shows a ring walk cannot build; its
   readings are about the abstraction and about no ring. (iii) The
   multiplicative ladders are not walked under the tag cost. The reason is
   derived (F2) rather than a rig limit, but a function field's cost with a
   genuinely BOUNDED M is not ruled out by it and is not run. (iv)
   Everything here is the IDEAL world; an element move seats a bundle.
   (v) One supply, one seed, one dial (alpha = 1, m = 1, born = {1}). The
   eight-dial cross explore_tick_pump.py F10 runs over the family is not run
   over these costs, so every reading above is at the corner.

RUN RECORD. One process, CPython, no BLAS. Wall 1.3 s, peak working set
33.1 MB against memwatch.py's 512 MB ceiling. 376532 checks. Five ladders in
the control, the door table and the second cost; the tag cost's walk sweep is
the three constant-gap ones by F2, crossed with five tag regimes. 3120 walk
states in all, each carrying both menus.
explore_tick_pump.py's Pump, PWalk, bound_at and ladder constructors and
explore_price_schedule.py's Sched are imported rather than re-implemented,
so their own asserts fire underneath these.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bisect import bisect_left
from fractions import Fraction

import explore_price_schedule as PS
import explore_tick_pump as TP

CHECKS = 0

WALK_DCAP = TP.WALK_DCAP     # 400 degrees the grid's supply carries
WALK_N = TP.WALK_N           # 120 moves per cell
FLAT_TAIL = TP.FLAT_TAIL     # 40 trailing minima read for flatness
GRID_SEED = TP.GRID_SEED     # the seed the on/off grid runs, carried over
CTRL_N = 60                  # states the family control compares


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ------------------------------------------------------------------ the costs
class FamilyCost(object):
    """The schedule family re-expressed through the cost interface: a DOOR and
    a PRICE, both handed the whole walk. Everything the family does goes
    through `sch`, so this class adds no behaviour -- it exists so that S1 can
    certify the interface itself against explore_tick_pump.py's walker before
    any cost outside the family is run through it."""

    kind = "family"

    def __init__(self, sch):
        self.sch = sch
        self.tag = sch.tag
        self.m = sch.m
        self.born = sch.born

    def prepare(self, w):
        pass

    def door(self, w, d, slot, e, kind):
        if kind == "open" and not w.covered(d):
            return 1
        return max(1, w.tick((d, slot)) + 1 - e)

    def of(self, w, d, slot, e, r, kind):
        return self.sch.price(d, r)

    def floor(self, d):
        return self.sch.price(d, 1)

    def check_floor(self, dcap):
        """(ii) of hand-attack G: the early stop needs floor non-decreasing in
        the degree. (i) -- that no candidate undercuts its degree's floor --
        is the brute control's, which checks the menu itself rather than an
        inequality about it."""
        for d in range(1, dcap):
            ok(self.floor(d + 1) >= self.floor(d),
               "%s: floor(%d) = %s falls below floor(%d) = %s, so the menu's "
               "scan rule is unsound" % (self.tag, d + 1, self.floor(d + 1),
                                         d, self.floor(d)))


class TagCost(FamilyCost):
    """The measured ring door with the arithmetic stripped off. Each item
    carries a TAG (an integer standing for v_p of its own lambda column) and a
    CHAR; a seated item's door is the least climb whose own valuation column
    outruns the MAX contribution over the OTHER seated items -- the residue
    route where the chars differ, the exponent route where they agree.

    The price stays the family's price(degree, door), so the one thing that
    leaves the family is that the door reads the state (hand-attack A)."""

    kind = "tag"

    def __init__(self, sch, tagf, charf, lad, tag):
        FamilyCost.__init__(self, sch)
        self.tagf = tagf
        self.charf = charf
        self.lad = lad
        self.tag = tag
        self._memo = {}
        self._same = {}     # char -> (top v, its key, second v)
        self._tags = {}     # char -> best tag among OTHER chars
        self.M_seen = set()

    # -- the state's contribution, cached once per menu -----------------
    def prepare(self, w):
        """The two maxima M reads, built once per menu rather than per
        candidate: the top-two of each char's own column values (so that an
        item can be excluded from its own max) and, over chars, the top-two
        of each char's best tag (so that a char can be excluded from the
        cross-char max). Both O(seated); M is then O(1) per candidate."""
        same, best_tag = {}, {}
        for d, row in w.seat.items():
            for i, e in enumerate(row):
                key = (d, i)
                c = self.charf(key)
                v = self.lad(key).v(e)
                top = same.get(c)
                if top is None:
                    same[c] = (v, key, None)
                elif v > top[0]:
                    same[c] = (v, key, top[0])
                elif top[2] is None or v > top[2]:
                    same[c] = (top[0], top[1], v)
                t = self.tagf(key)
                if c not in best_tag or t > best_tag[c]:
                    best_tag[c] = t
        pairs = sorted(best_tag.items(), key=lambda kv: -kv[1])
        t1 = pairs[0] if pairs else None
        t2 = pairs[1][1] if len(pairs) > 1 else None
        self._same = same
        self._tags = {}
        for c in best_tag:
            if t1 is not None and t1[0] != c:
                self._tags[c] = t1[1]
            elif t2 is not None:
                self._tags[c] = t2
            else:
                self._tags[c] = None
        self._t1, self._t2 = t1, t2

    def M(self, w, key):
        c = self.charf(key)
        vals = []
        top = self._same.get(c)
        if top is not None:
            if top[1] == key:
                if top[2] is not None:
                    vals.append(top[2])
            else:
                vals.append(top[0])
        cross = self._tags.get(c)
        if cross is None:
            # `key` is unseated, so its char contributes no row of its own and
            # the cross-char max is simply the best tag anywhere seated
            if self._t1 is not None:
                cross = self._t2 if self._t1[0] == c else self._t1[1]
        if cross is not None:
            vals.append(cross)
        return max(vals) if vals else 0

    # -- the door -------------------------------------------------------
    def raw_door(self, pump, e, M):
        """The least climb whose own column outruns M. Bounded by the LADDER's
        own reach and not by a round number: on a multiplicative ladder v is
        logarithmic, so outrunning M takes a climb EXPONENTIAL in M and leaves
        any tabulated range at once. That is a property of the cost rather
        than a limit of the rig, and it is what scopes the walk sweep to the
        ladders mixed-characteristic arithmetic realizes."""
        # keyed on the ladder's TAG and not on id(): two Pump objects with one
        # tag are one ladder, and a temporary Pump's id can be recycled under
        # a later object, which would serve a stale door silently
        key = (pump.tag, e, M)
        got = self._memo.get(key)
        if got is not None:
            return got
        base = max(pump.v(e), M)
        r = 1
        while pump.v(e + r) <= base:
            r += 1
            ok(e + r <= pump.cap,
               "%s: no climb from depth %d outruns %d inside the ladder's own "
               "reach %d -- the door is exponential in M here and this cell "
               "is a lock rather than a walk" % (pump.tag, e, base, pump.cap))
        self._memo[key] = r
        return r

    def door(self, w, d, slot, e, kind):
        if kind == "open" and not w.covered(d):
            return 1
        key = (d, slot)
        M = self.M(w, key)
        self.M_seen.add(M)
        return self.raw_door(self.lad(key), e, M)


class DepthCost(FamilyCost):
    """degree x the depth the move LANDS at. The door stays the family's, so
    this cost isolates the PRICE's dependence on the state from the DOOR's:
    on a constant-gap ladder gap(depth) is constant, so f(degree, gap) cannot
    see the depth at all while d * (e + r) grows along the trajectory
    (hand-attack D)."""

    kind = "depth"

    def __init__(self, sch, tag="degree x depth"):
        FamilyCost.__init__(self, sch)
        self.tag = tag

    def of(self, w, d, slot, e, r, kind):
        return d * (e + r)

    def floor(self, d):
        return d


# ----------------------------------------------------------------- the walker
class CWalk(TP.PWalk):
    """explore_tick_pump.py's walker with the price replaced by a COST OBJECT
    that reads the whole state. Only two methods change -- the door and the
    menu -- and the menu carries a BRUTE full-scan twin, because the early
    stop's soundness is a property of the schedule family and a bare cost is
    entitled to break it silently (hand-attack G).

    Everything else -- the seating, the fresh discount, the covered test, the
    clock's landing along the item's own ladder -- is that walker's, inherited
    rather than copied, and S1 certifies the composite against it."""

    def __init__(self, npl, cost, pump, cls, dcap, seed=(), lad=None,
                 tag=None):
        self.cost = cost
        TP.PWalk.__init__(self, npl, cost, pump, cls, dcap, seed=seed,
                          lad=lad, tag=tag or cost.tag)

    def door(self, d, slot, e, kind):
        return self.cost.door(self, d, slot, e, kind)

    def menu(self, brute=False):
        """(cost, sorted ties). With brute=False the scan stops at the first
        degree whose floor already beats the best found; with brute=True it
        runs the whole supply. The two are required to agree at every step of
        every walk, which is the control the early stop needs once the price
        is no longer the family's."""
        self.cost.prepare(self)
        best, ties = None, []
        d, stopped = 0, False
        while d < self.dcap:
            d += 1
            if not brute and best is not None and self.cost.floor(d) > best:
                stopped = True
                break
            if self.npl.get(d, 0) == 0:
                continue
            row = self.seat.get(d, [])
            cands = []
            if self.npl[d] > len(row):
                r = self.door(d, len(row), 0, "open")
                cands.append((self.cost.of(self, d, len(row), 0, r, "open"),
                              d, len(row), r, "open"))
            for i, e in enumerate(row):
                r = self.door(d, i, e, "move")
                cands.append((self.cost.of(self, d, i, e, r, "move"),
                              d, i, r, "move"))
            for c in cands:
                if best is None or c[0] < best:
                    best, ties = c[0], [c]
                elif c[0] == best:
                    ties.append(c)
        ok(best is not None, "%s: an empty menu" % self.tag)
        ok(brute or stopped or not self.beyond,
           "%s: the menu scan ran to the degree cap %d and the supply has "
           "items past it, so the menu is a truncation"
           % (self.tag, self.dcap))
        return best, sorted(ties)

    def copy(self):
        s = CWalk(self.npl, self.cost, self.pump, self.cls, self.dcap,
                  lad=self.lad, tag=self.tag)
        s.seat = dict((d, list(v)) for d, v in self.seat.items())
        s.opens = dict(self.opens)
        s.opened = list(self.opened)
        s.T = dict(self.T)
        s.step = self.step
        s.clocks = list(self.clocks)
        return s


# ------------------------------------------------------------------- the grid
def supply(dcap=WALK_DCAP):
    return dict((d, 2) for d in range(1, dcap + 1))


def ladders():
    return [TP.p_exact(), TP.p_step(2), TP.p_step(3), TP.p_geom(2),
            TP.p_squares()]


def arith_ladders():
    """The ladders a MIXED-characteristic place carries: constant gap, the gap
    being the ramification index, with the exact ladder the unramified extreme
    (explore_tick_pump.py hand-attack F). The tag cost abstracts a NUMBER
    RING's door, and the door table in S2 prints what the other ladders do
    with it -- a climb exponential in M on a multiplicative ladder, quadratic
    on the square one -- which is why the walk sweep is these three."""
    return [TP.p_exact(), TP.p_step(2), TP.p_step(3)]


def run(npl, cost, pump, cls, seed, n=WALK_N, brute=True, tag=None):
    """A cell: the walk, its menu minima, its tail openings, and the count of
    steps at which the brute and early-stop menus disagreed."""
    w = CWalk(npl, cost, pump, cls, WALK_DCAP, seed=seed, tag=tag)
    mins, tail_opens, off, moves = [], 0, 0, {}
    for j in range(n):
        best, ties = w.menu()
        if brute:
            b2, t2 = w.menu(brute=True)
            if (best, ties) != (b2, t2):
                off += 1
        mins.append(best)
        _, d, slot, _, kind = w.apply(ties[0])
        if j >= n - FLAT_TAIL:
            if kind == "open":
                tail_opens += 1
            else:
                moves[(d, slot)] = moves.get((d, slot), 0) + 1
    return w, mins, tail_opens, off, moves


def deep_of(w):
    return sorted((d, i, e) for d, row in w.seat.items()
                  for i, e in enumerate(row) if e > 1)


def top_degree(w):
    """The largest degree carrying an item above exponent 1 -- the ceiling
    read off the walk rather than off a planted menu."""
    deep = deep_of(w)
    return max(d for d, _, _ in deep) if deep else 0


# -------------------------------------------------------- S0 forced failures
def s0_forced():
    section("S0  FORCED FAILURES -- every check the run leans on, made to "
            "fail once")
    sch = PS.Sched("corner", alpha=1, b=2, m=1)
    npl = supply()
    fired = 0

    class Falling(FamilyCost):
        def floor(self, d):
            return -d

    try:
        Falling(sch).check_floor(20)
    except AssertionError:
        fired += 1
        print("  a floor falling with the degree     -> caught")

    class Undercut(FamilyCost):
        """A cost that undercuts its own floor at one high degree: the early
        stop then returns a NON-MINIMAL menu and nothing but the brute twin
        can see it."""

        def of(self, w, d, slot, e, r, kind):
            return 1 if d == 300 else self.sch.price(d, r)

    w = CWalk(npl, Undercut(sch), TP.p_exact(), TP.PERITEM, WALK_DCAP,
              seed=GRID_SEED)
    a, _ = w.menu()
    b, _ = w.menu(brute=True)
    ok(a != b, "the undercut cost did not part the two menus")
    fired += 1
    print("  a cost undercutting its floor       -> the brute menu parts "
          "(%s against %s)" % (a, b))

    class Blind(TagCost):
        def raw_door(self, pump, e, M):
            return 1

    # run S2's OWN closed-form comparison against a door that ignores M --
    # a check is only forced to fail if the failing thing is the check the
    # run actually leans on, not a hand-written inequality beside it
    ex = TP.p_exact()
    blind = Blind(sch, lambda k: 4, lambda k: k, lambda k: ex, "blind tag")
    try:
        for e in range(1, 4):
            for M in range(0, 6):
                got = blind.raw_door(ex, e, M)
                ok(got == (1 if M <= e - 1 else M - e + 2),
                   "blind: e = %d, M = %d gave %d" % (e, M, got))
    except AssertionError:
        fired += 1
        print("  a door ignoring M                   -> S2's closed form "
              "catches it")

    real = TagCost(sch, lambda k: 4, lambda k: k, lambda k: ex, "tag 4")
    exhausted = TP.Pump("two rungs", [1, 2], cap=2)
    try:
        real.raw_door(exhausted, 3, 99)
    except AssertionError:
        fired += 1
        print("  a column that cannot outrun M       -> caught")

    print("\n  %d forced failures, all caught." % fired)
    ok(fired == 4, "only %d of 4 forced failures fired" % fired)


# ---------------------------------------------------------------- S1 control
def s1_control(pumps):
    section("S1  PR1 -- THE CONTROL: the brute menu against the early stop, "
            "and the family reproduced through the cost interface")
    sch = PS.Sched("corner", alpha=1, b=2, m=1)
    sch.check_monotone(WALK_DCAP)
    npl = supply()
    fc = FamilyCost(sch)
    fc.check_floor(WALK_DCAP)

    print("  (b) the family's own schedule, run through the cost interface,")
    print("      against explore_tick_pump.py's PWalk -- %d states per cell."
          % CTRL_N)
    print("\n  %-12s %-9s %-9s %s" % ("ladder", "clock", "states", "verdict"))
    pairs = 0
    for pump in pumps:
        for ctag, cls in (("global", TP.GLOBAL), ("per item", TP.PERITEM)):
            a = TP.PWalk(npl, sch, pump, cls, WALK_DCAP, seed=GRID_SEED)
            b = CWalk(npl, fc, pump, cls, WALK_DCAP, seed=GRID_SEED,
                      tag=pump.tag)
            for _ in range(CTRL_N):
                ca, ta = a.menu()
                cb, tb = b.menu()
                ok(ca == cb and ta == tb,
                   "%s/%s: the cost-interface walker parted from PWalk at "
                   "step %d: %s against %s" % (pump.tag, ctag, a.step,
                                               ta[:2], tb[:2]))
                a.apply(ta[0])
                b.apply(tb[0])
                pairs += 1
            ok(a.seat == b.seat and a.T == b.T and a.opens == b.opens,
               "%s/%s: the two walkers' final states part" % (pump.tag, ctag))
            print("  %-12s %-9s %-9d %s" % (pump.tag, ctag, CTRL_N,
                                            "move for move"))

    print("\n  (c) the tag cost at ALL TAGS ZERO against the family cost,")
    print("      per-item clock -- the regime in which the two are the same")
    print("      object, the door falling back to the item's own gap.")
    print("\n  %-12s %-9s %s" % ("ladder", "states", "verdict"))
    for pump in pumps:
        tc = TagCost(sch, lambda k: 0, lambda k: k, lambda k: pump,
                     "tags 0/%s" % pump.tag)
        a = CWalk(npl, fc, pump, TP.PERITEM, WALK_DCAP, seed=GRID_SEED)
        b = CWalk(npl, tc, pump, TP.PERITEM, WALK_DCAP, seed=GRID_SEED)
        for _ in range(CTRL_N):
            ca, ta = a.menu()
            cb, tb = b.menu()
            ok(ca == cb and ta == tb,
               "%s: the zero-tag cost parted from the family at step %d: %s "
               "against %s" % (pump.tag, a.step, ta[:2], tb[:2]))
            a.apply(ta[0])
            b.apply(tb[0])
            pairs += 1
        ok(a.seat == b.seat, "%s: the zero-tag final state parts" % pump.tag)
        print("  %-12s %-9d %s" % (pump.tag, CTRL_N, "move for move"))

    print("\n  (a) the brute full-scan menu against the early stop, at every")
    print("      step of every cell below. Counted in S3 and S4 and reported")
    print("      there; the two cells here are the interface's own.")
    off_all = 0
    for pump in (pumps[0], pumps[2]):
        _, _, _, off, _ = run(npl, fc, pump, TP.PERITEM, GRID_SEED,
                              n=CTRL_N, tag=pump.tag)
        off_all += off
    ok(off_all == 0, "%d brute/early-stop disagreements in the control cells"
       % off_all)
    print("      %d disagreements over %d control states." % (off_all,
                                                              2 * CTRL_N))
    print("\n  %d (state, walker) pairs compared." % pairs)


# ------------------------------------------------------------- S2 the tag door
def s2_door(pumps):
    section("S2  PR2 -- THE TAG DOOR: the closed form it must reproduce, and "
            "the state-dependence no schedule has")
    sch = PS.Sched("corner", alpha=1, b=2, m=1)
    ex = TP.p_exact()
    tc = TagCost(sch, lambda k: 0, lambda k: k, lambda k: ex, "form")
    print("  On the exact ladder v(a) = a - 1, so the door is the least r")
    print("  with e + r - 1 > max(e - 1, M): 1 where M <= e - 1 and M - e + 2")
    print("  otherwise. That is explore_populated_door.py F2's closed form")
    print("  door_pop = v_p(L) - e + 2, with its scope -- the cyclic unit")
    print("  group -- coming out here as the exact ladder.")
    print("\n  %-6s %s" % ("e", "  ".join("M=%-3d" % M for M in range(0, 8))))
    n = 0
    for e in range(1, 9):
        row = []
        for M in range(0, 8):
            got = tc.raw_door(ex, e, M)
            want = 1 if M <= e - 1 else M - e + 2
            ok(got == want,
               "exact ladder at e = %d, M = %d: the door is %d and the closed "
               "form says %d" % (e, M, got, want))
            n += 1
            row.append("%-5d" % got)
        print("  %-6d %s" % (e, "  ".join(row)))
    print("\n  %d readings, closed form reproduced at every one." % n)

    print("\n  the same table off the exact ladder -- where the family's own")
    print("  gap is already above 1, the widening starts from that gap and")
    print("  the closed form is not expected to hold. Read the ROW SHAPE and")
    print("  not only the numbers: the door is what it takes to outrun M, so")
    print("  it inverts the ladder's own valuation -- linear in M where v is")
    print("  linear, and exponential in M where v is logarithmic.")
    print("\n  %-12s %-6s %s"
          % ("ladder", "gap(1)", "  ".join("M=%-3d" % M for M in range(0, 8))))
    for pump in pumps:
        tc2 = TagCost(sch, lambda k: 0, lambda k: k, lambda k: pump, "form")
        row = ["%-5d" % tc2.raw_door(pump, 1, M) for M in range(0, 8)]
        print("  %-12s %-6d %s" % (pump.tag, pump.gap(1), "  ".join(row)))
    print("\n  which is what scopes the walk sweep below to the constant-gap")
    print("  ladders: a multiplicative one prices its own state-widened move")
    print("  out of every tabulated range at once, so that cell is a lock and")
    print("  not a walk. Those are also the ladders a MIXED-characteristic")
    print("  place carries (explore_tick_pump.py hand-attack F), which is the")
    print("  world the tag cost abstracts.")

    print("\n  and the state-dependence itself, swept over every tag regime")
    print("  the freeze names: over one walk per (ladder, regime), how many")
    print("  (item, depth) pairs read MORE THAN ONE door. A schedule in the")
    print("  family can read only one -- its price is a function of the")
    print("  item's own degree and exponent -- so a regime reading one door")
    print("  everywhere has the family's own SHAPE back, and which")
    print("  regimes those are is the reading rather than the failure.")
    npl = supply()
    print("\n  %-12s %-11s %-9s %-11s %-9s %s"
          % ("ladder", "regime", "pairs", "multi-door", "M seen",
             "doors at a pair"))
    multi_any = 0
    for pump in arith_ladders():
        for rtag, tagf, charf in REGIMES:
            cost = TagCost(sch, tagf, charf, lambda k: pump,
                           "%s/%s" % (rtag, pump.tag))
            w = CWalk(npl, cost, pump, TP.PERITEM, WALK_DCAP, seed=GRID_SEED)
            seen = {}
            for _ in range(WALK_N):
                cost.prepare(w)
                for d, row in w.seat.items():
                    for i, e in enumerate(row):
                        seen.setdefault((d, i, e), set()).add(
                            w.door(d, i, e, "move"))
                _, ties = w.menu()
                w.apply(ties[0])
            multi = [k for k, v in seen.items() if len(v) > 1]
            multi_any += len(multi)
            ex_pair = ""
            if multi:
                k = sorted(multi)[0]
                ds = sorted(seen[k])
                ex_pair = "d%d slot %d e%d: %s%s" % (
                    k[0], k[1], k[2], ds[:4],
                    " ..%d doors" % len(ds) if len(ds) > 4 else "")
            print("  %-12s %-11s %-9d %-11d %-9s %s"
                  % (pump.tag, rtag, len(seen), len(multi),
                     "%d..%d" % (min(cost.M_seen), max(cost.M_seen)), ex_pair))
    ok(multi_any > 0,
       "no (item, depth) pair read two doors at any ladder or regime, so the "
       "tag cost is a schedule after all")
    print("\n  %d multi-door pairs in all -- PR2's kill did not fire."
          % multi_any)

    print("\n  and the uniform regime is NOT thereby a member of the family,")
    print("  which reading 0 multi-door pairs is one step short of showing. A")
    print("  door that is a function of the item's own depth has the family's")
    print("  SHAPE; to be a member it must be some ladder's gap. Every ladder")
    print("  here contains 1 -- the Pump constructor asserts it, and it is")
    print("  what makes the initial tick a legal clock position -- so every")
    print("  one of them has gap(1) = 1, while a uniform tag T charges T + 1")
    print("  at depth 1. So the uniform regime sits inside the family's shape")
    print("  and outside every one of its members.")
    print("\n  %-12s %-9s %-14s %s"
          % ("ladder", "gap(1)", "uniform T = 4", "realizable"))
    for pump in ladders():
        tc3 = TagCost(sch, lambda k: 4, lambda k: k, lambda k: pump, "u")
        d1 = tc3.raw_door(pump, 1, 4)
        print("  %-12s %-9d %-14d %s"
              % (pump.tag, pump.gap(1), d1, "yes" if d1 == pump.gap(1)
                 else "no"))
        ok(pump.S[0] == 1 and pump.gap(1) == 1,
           "%s: a ladder whose gap at depth 1 is %d, so the argument that no "
           "member charges T + 1 there does not run" % (pump.tag, pump.gap(1)))
        ok(d1 != pump.gap(1),
           "%s: the uniform door at depth 1 is %d, which IS this ladder's own "
           "gap, so the regime is a member after all" % (pump.tag, d1))


# -------------------------------------------- S3 the four laws under the tag
REGIMES = [
    ("tags 0", lambda k: 0, lambda k: k),
    ("tags 4", lambda k: 4, lambda k: k),
    ("tag = deg", lambda k: k[0], lambda k: k),
    ("sparse 6", lambda k: 6 if k[0] in (2, 3, 5, 7) else 0, lambda k: k),
    ("one char", lambda k: 0, lambda k: 0),
]


def lone_gap(pump, upto=64):
    """The gap the item pays forever on its OWN ladder, ignoring the state --
    explore_tick_pump.py's tail_gap, which only an arithmetic ladder has."""
    return TP.tail_gap(pump, upto)


def s3_tag_laws(pumps):
    section("S3  PR3, PR4, PR5, PR6 (a) -- THE FOUR LAWS UNDER THE TAG COST")
    sch = PS.Sched("corner", alpha=1, b=2, m=1)
    npl = supply()
    print("  The S2 cell of explore_tick_pump.py exactly -- two items at every")
    print("  degree to %d, seeded at degrees %s, %d moves -- with the DOOR"
          % (WALK_DCAP, GRID_SEED, WALK_N))
    print("  reading the state. Per-item clock throughout: the tag cost reads")
    print("  an item's own column and never a shared tick, and a ring's clock")
    print("  is per-item (explore_tick_pump.py F9).")
    print("\n  the naive product is price(degree, the item's LONE tail gap) --")
    print("  the filed law's own instrument. The corrected product is")
    print("  price(degree, the POPULATED door at the item's standing depth),")
    print("  read at the final state through the cost's own door.")

    rows, off_all, states = {}, 0, 0
    for pump in pumps:
        arith = True
        try:
            lone_gap(pump)
        except AssertionError:
            arith = False
        for rtag, tagf, charf in REGIMES:
            cost = TagCost(sch, tagf, charf, lambda k: pump,
                           "%s/%s" % (rtag, pump.tag))
            w, mins, opens, off, moves = run(npl, cost, pump, TP.PERITEM,
                                             GRID_SEED)
            off_all += off
            states += WALK_N
            budget = mins[-1]
            flat = len(set(mins[-FLAT_TAIL:])) == 1
            cost.prepare(w)
            seated = [(d, i) for d, row in w.seat.items()
                      for i in range(len(row))]
            depth = dict((d, i) for d, row in w.seat.items()
                         for i, _ in enumerate(row))
            depth = dict(((d, i), e) for d, row in w.seat.items()
                         for i, e in enumerate(row))
            corr = dict((k, cost.of(w, k[0], k[1], depth[k],
                                    w.door(k[0], k[1], depth[k], "move"),
                                    "move")) for k in seated)
            naive = (dict((k, sch.price(k[0], lone_gap(pump))) for k in seated)
                     if arith else None)
            run_item = sorted(moves, key=lambda k: -moves[k])[0] \
                if moves else None
            rows[(pump.tag, rtag)] = dict(
                w=w, mins=mins, opens=opens, budget=budget, flat=flat,
                corr=corr, naive=naive, run=run_item, seated=seated,
                depth=depth, deep=deep_of(w), top=top_degree(w),
                lu=w.least_uncovered(), arith=arith, cost=cost,
                Ms=(min(cost.M_seen), max(cost.M_seen)))

    # -- PR3, the stop law ------------------------------------------------
    print("\n  PR3 -- the stop law. `flat` is the filed proxy (a flat cost")
    print("  tail); `opens` is the direct reading (degrees opened in the last")
    print("  %d moves). The two curves the SHARPENED law compares are printed"
          % FLAT_TAIL)
    print("  beside them: `cheapest move` is the least price over seated items")
    print("  of moving at the depth it stands at -- the recurrent curve -- and")
    print("  `cheapest open` is the least-uncovered degree's opening. A walk")
    print("  stops iff the first stays below the second forever.")
    print("\n  %-12s %-11s %-8s %-6s %-7s %-14s %-14s %s"
          % ("ladder", "regime", "max gap", "flat", "opens", "cheapest move",
             "cheapest open", "M range"))
    pr3_fired = []
    for pump in pumps:
        for rtag, _, _ in REGIMES:
            r = rows[(pump.tag, rtag)]
            w = r["w"]
            nxt = r["cost"].of(w, r["lu"], 0, 0, 1, "open") if r["lu"] else 0
            rec = min(r["corr"].values())
            print("  %-12s %-11s %-8d %-6s %-7d %-14d %-14d %d..%d"
                  % (pump.tag, rtag, pump.max_gap(4000),
                     "yes" if r["flat"] else "NO", r["opens"], rec, nxt,
                     r["Ms"][0], r["Ms"][1]))
            if pump.max_gap(4000) <= 5 and r["opens"] > 0:
                pr3_fired.append((pump.tag, rtag, r["opens"], rec, nxt))
    print("\n  PR3's kill -- a bounded-gap cell opening a degree in its last")
    print("  %d moves -- fired at %d of %d cells:"
          % (FLAT_TAIL, len(pr3_fired), len(pumps) * len(REGIMES)))
    for tag, rtag, op, rec, nxt in pr3_fired:
        print("    %-12s %-11s %d opens, cheapest move %d against a cheapest "
              "opening of %d" % (tag, rtag, op, rec, nxt))
    if not pr3_fired:
        print("    none.")

    # -- PR4, the min over products ---------------------------------------
    print("\n  PR4 -- the budget against both products. `naive` is the filed")
    print("  law's prediction, `corrected` this slate's. Only cells with a")
    print("  FLAT tail appear: a walk that never stops has no budget for a")
    print("  product law to predict, so PR3's firing removes the object PR4")
    print("  is about rather than falsifying it.")
    print("\n  %-12s %-11s %-8s %-8s %-10s %-9s %s"
          % ("ladder", "regime", "budget", "naive", "corrected", "runaway",
             "strands (degree, naive, corrected)"))
    naive_off, corr_off = 0, 0
    for pump in pumps:
        for rtag, _, _ in REGIMES:
            r = rows[(pump.tag, rtag)]
            if not r["flat"] or r["run"] is None:
                continue
            cpred = min(r["corr"].values())
            npred = min(r["naive"].values()) if r["naive"] else None
            strand = [k for k in r["seated"]
                      if r["depth"][k] > 1 and k != r["run"]]
            if npred is not None and npred != r["budget"]:
                naive_off += 1
            if cpred != r["budget"]:
                corr_off += 1
            print("  %-12s %-11s %-8d %-8s %-10d %-9s %s"
                  % (pump.tag, rtag, r["budget"],
                     npred if npred is not None else "-", cpred,
                     "d%d" % r["run"][0],
                     ", ".join("d%d n%s c%d"
                               % (k[0],
                                  r["naive"][k] if r["naive"] else "-",
                                  r["corr"][k]) for k in strand) or "-"))
            ok(cpred == r["budget"],
               "%s/%s: the corrected product predicts %d and the flat tail "
               "minimum is %d -- PR4's kill"
               % (pump.tag, rtag, cpred, r["budget"]))
            ok(r["corr"][r["run"]] == cpred,
               "%s/%s: the runaway %s has corrected product %d, not the least "
               "%d" % (pump.tag, rtag, r["run"], r["corr"][r["run"]], cpred))
            for k in strand:
                ok(r["corr"][k] >= r["budget"],
                   "%s/%s: item d%d slot %d stands at exponent %d with "
                   "corrected product %d BELOW the budget %d"
                   % (pump.tag, rtag, k[0], k[1], r["depth"][k],
                      r["corr"][k], r["budget"]))
            if r["naive"]:
                ok(r["corr"][r["run"]] == r["naive"][r["run"]],
                   "%s/%s: the runaway's corrected product %d parts from its "
                   "naive %d, so it is not standing past M"
                   % (pump.tag, rtag, r["corr"][r["run"]],
                      r["naive"][r["run"]]))
    print("\n  the naive product mispredicts the budget at %d of the flat"
          % naive_off)
    print("  cells, the corrected one at %d." % corr_off)
    ok(corr_off == 0, "the corrected product mispredicts at %d cells"
       % corr_off)

    print("\n  and the STRAND KIND, which the budget column cannot show. The")
    print("  filed law splits a strand two ways: a product strictly ABOVE the")
    print("  budget is priced out on every branch, one EQUAL to it stands in")
    print("  the final menu's own minimum and only by tie-break. So the two")
    print("  products can agree on the budget and still disagree on what a")
    print("  strand IS -- and the final menu's ties are the arbiter.")
    print("\n  %-12s %-11s %-9s %-8s %-11s %-9s %s"
          % ("ladder", "regime", "strand", "naive", "corrected", "in ties",
             "naive kind / corrected kind"))
    strand_off = 0
    for pump in pumps:
        for rtag, _, _ in REGIMES:
            r = rows[(pump.tag, rtag)]
            if not r["flat"] or r["run"] is None or not r["naive"]:
                continue
            _, ties = r["w"].menu()
            tied = set((t[1], t[2]) for t in ties)
            for k in r["seated"]:
                if r["depth"][k] <= 1 or k == r["run"]:
                    continue
                nk = "tie" if r["naive"][k] == r["budget"] else "priced out"
                ck = "tie" if r["corr"][k] == r["budget"] else "priced out"
                if (nk == "tie") != (k in tied):
                    strand_off += 1
                print("  %-12s %-11s d%-8d %-8d %-11d %-9s %s"
                      % (pump.tag, rtag, k[0], r["naive"][k], r["corr"][k],
                         "yes" if k in tied else "no", "%s / %s" % (nk, ck)))
                ok((ck == "tie") == (k in tied),
                   "%s/%s: the corrected product calls item d%d a %s and the "
                   "final menu %s carry it" % (pump.tag, rtag, k[0], ck,
                                               "does" if k in tied
                                               else "does not"))
    print("\n  the naive product misclassifies %d strands against the final"
          % strand_off)
    print("  menu; the corrected one misclassifies 0, which is asserted.")

    # -- PR5, does the cost change the WALK -------------------------------
    print("\n  PR5 -- the walk itself against the zero-tag control: does a")
    print("  widened door ever change what is SEATED, or only what a strand")
    print("  is priced at (explore_populated_door.py F8 (v), abstracted)?")
    print("\n  %-12s %-11s %-9s %-9s %-9s %s"
          % ("ladder", "regime", "seated", "above 1", "runaway", "against the "
             "control"))
    changed = 0
    for pump in pumps:
        base = rows[(pump.tag, "tags 0")]
        for rtag, _, _ in REGIMES:
            r = rows[(pump.tag, rtag)]
            same_seat = r["w"].shape() == base["w"].shape()
            same_run = r["run"] == base["run"]
            verdict = "control" if rtag == "tags 0" else (
                "same" if same_seat and same_run else
                ("seating" if not same_seat else "runaway"))
            if rtag != "tags 0" and not (same_seat and same_run):
                changed += 1
            print("  %-12s %-11s %-9d %-9d %-9s %s"
                  % (pump.tag, rtag, len(r["seated"]), len(r["deep"]),
                     "d%d" % r["run"][0] if r["run"] else "-", verdict))
    print("\n  %d of %d non-control cells part from the control."
          % (changed, len(pumps) * (len(REGIMES) - 1)))

    # -- PR6 (a), the ceiling ---------------------------------------------
    print("\n  PR6 (a) -- the largest degree carrying an item above exponent")
    print("  1, against the zero-tag control's. A widened door raises the")
    print("  price of a MOVE and leaves an uncovered degree's opening at door")
    print("  1, so the tag cost should never seat DEEPER than the control.")
    print("\n  %-12s %-11s %-9s %-9s %s"
          % ("ladder", "regime", "top degree", "control", "verdict"))
    pr6_fired = []
    for pump in pumps:
        base = rows[(pump.tag, "tags 0")]["top"]
        for rtag, _, _ in REGIMES:
            r = rows[(pump.tag, rtag)]
            if r["top"] > base:
                pr6_fired.append((pump.tag, rtag, r["top"], base))
            print("  %-12s %-11s %-9d %-9d %s"
                  % (pump.tag, rtag, r["top"], base,
                     "at or under" if r["top"] <= base else "ABOVE"))
    print("\n  PR6 (a)'s kill fired at %d of %d cells%s"
          % (len(pr6_fired), len(pumps) * len(REGIMES),
             ":" if pr6_fired else "."))
    for tag, rtag, top, base in pr6_fired:
        print("    %-12s %-11s top degree %d against the control's %d"
              % (tag, rtag, top, base))

    ok(off_all == 0,
       "%d brute/early-stop menu disagreements over %d states -- the early "
       "stop is returning a non-minimal menu" % (off_all, states))
    print("\n  PR1 (a) here: %d brute/early-stop disagreements over %d states."
          % (off_all, states))
    return rows


# ---------------------------------------------- S4 the laws under cost B
def planted_depth(cost, pump, D, dmin, T):
    """explore_tick_pump.py's planted two-item menu, run under a bare cost: a
    stale item of degree D at the stalest exponent the ladder allows at tick
    T, one unseated item of degree dmin, nothing else, both degrees covered.
    Returns whether the stale item is in the menu's minimum."""
    i = bisect_left(pump.S, T)
    prev = pump.S[i - 1] if i else 0
    e = prev + 1
    npl = dict((d, 0) for d in range(1, PS.DEG_CAP + 1))
    npl[D] = 1
    npl[dmin] = npl.get(dmin, 0) + 1
    w = CWalk(npl, cost, pump, TP.GLOBAL, PS.DEG_CAP)
    w.opens = {D: cost.m, dmin: cost.m}
    w.seat = {D: [e]}
    w.T = {0: T}
    _, ties = w.menu()
    return any(t[1] == D and t[4] == "move" for t in ties), e


def s4_depth_laws(pumps):
    section("S4  PR6 (b), PR7, PR8 -- THE CEILING, THE STOP LAW AND THE "
            "LIMIT UNDER degree x depth")
    sch = PS.Sched("corner", alpha=1, b=2, m=1)
    cost = DepthCost(sch)
    cost.check_floor(WALK_DCAP)
    npl = supply()

    print("  PR6 (b) -- the planted two-item ceiling. The stale item of")
    print("  degree D stands at exponent T_prev + 1 with door T - T_prev, so")
    print("  it LANDS at T + 1 and costs D * (T + 1); the unseated rival at")
    print("  d_min lands at T + 1 too and costs d_min * (T + 1). The ratio")
    print("  the family formula is made of cancels, so the ceiling should be")
    print("  d_min at every ladder and every tick. Beside it the family's own")
    print("  bound at the same reading, which is where the ratio still lives.")
    dmin = 3
    print("\n  %-12s %-7s %-9s %-9s %-9s %s"
          % ("ladder", "tick", "stale e", "ceiling", "family", "verdict"))
    for pump in pumps:
        ticks = [t for t in pump.S[1:4] if t < 200]
        for T in ticks:
            D, e = dmin, None
            while D <= dmin * (T + 8):
                inm, e = planted_depth(cost, pump, D, dmin, T)
                if not inm:
                    break
                D += 1
            ceiling = D - 1
            fam = TP.bound_at(sch, pump, dmin, T)
            print("  %-12s %-7d %-9d %-9d %-9s %s"
                  % (pump.tag, T, e, ceiling, fam,
                     "d_min" if ceiling == dmin else "NOT d_min"))
            ok(ceiling == dmin,
               "%s at tick %d: the planted ceiling is %d and d_min is %d -- "
               "PR6 (b)'s kill" % (pump.tag, T, ceiling, dmin))

    print("\n  PR7 -- the stop law. The recurrent price d * (e + 1) grows with")
    print("  the item's own depth while the opening curve grows only with the")
    print("  degree, so the sharpened two-curve law says a bounded gap does")
    print("  not stop the ladder here. `opens` is the direct reading.")
    print("\n  %-12s %-9s %-8s %-7s %-7s %-11s %s"
          % ("ladder", "clock", "max gap", "flat", "opens", "recurrent",
             "next opening"))
    rows, off_all, states = {}, 0, 0
    for pump in pumps:
        for ctag, cls in (("global", TP.GLOBAL), ("per item", TP.PERITEM)):
            w, mins, opens, off, moves = run(npl, cost, pump, cls, GRID_SEED)
            off_all += off
            states += WALK_N
            flat = len(set(mins[-FLAT_TAIL:])) == 1
            lu = w.least_uncovered()
            nxt = cost.of(w, lu, 0, 0, 1, "open") if lu else 0
            rows[(pump.tag, ctag)] = (w, mins, opens, flat, lu, moves)
            print("  %-12s %-9s %-8d %-7s %-7d %-11d %d"
                  % (pump.tag, ctag, pump.max_gap(4000),
                     "yes" if flat else "NO", opens, mins[-1], nxt))
    ok(rows[("exact", "per item")][2] > 0,
       "the exact ladder opened no degree in its last %d moves under "
       "degree x depth, so its recurrent price is bounded -- PR7's kill"
       % FLAT_TAIL)

    print("\n  PR8 -- the limit's shape. How many items stand above exponent")
    print("  1, where they stand, and what the walk has left uncovered.")
    print("\n  %-12s %-9s %-9s %-11s %-11s %s"
          % ("ladder", "clock", "above 1", "least unc", "top degree",
             "the deep items (degree, exponent)"))
    for pump in pumps:
        for ctag, _ in (("global", None), ("per item", None)):
            w, mins, opens, flat, lu, moves = rows[(pump.tag, ctag)]
            deep = deep_of(w)
            print("  %-12s %-9s %-9d %-11s %-11d %s"
                  % (pump.tag, ctag, len(deep), lu, top_degree(w),
                     ", ".join("d%d e%d" % (d, e) for d, _, e in deep[:6])
                     + (" ..." if len(deep) > 6 else "")))

    ok(off_all == 0,
       "%d brute/early-stop menu disagreements over %d states under cost B"
       % (off_all, states))
    print("\n  PR1 (a) here: %d brute/early-stop disagreements over %d states."
          % (off_all, states))
    return rows


# --------------------------------------------------------------- S5 verdict
def s5_verdict(tag_rows, depth_rows, tag_pumps, pumps):
    section("S5  THE VERDICT: which law survived which cost")
    print("  A law is read SURVIVED where the rig's own assert for it did not")
    print("  fire, CORRECTED where it holds only in the form this slate fixed")
    print("  before the run, and BROKEN where the observable it names fired.")
    print("\n  %-28s %-24s %s" % ("law", "the tag cost", "degree x depth"))

    tag_cells = [(p.tag, r) for p in tag_pumps for r, _, _ in REGIMES]
    climbed = [k for k in tag_cells if tag_rows[k]["opens"] > 0]
    budget_ok, budget_n, strand_off = 0, 0, 0
    for k in tag_cells:
        r = tag_rows[k]
        if not r["flat"] or r["run"] is None:
            continue
        budget_n += 1
        if min(r["corr"].values()) == r["budget"]:
            budget_ok += 1
        if not r["naive"]:
            continue
        for s in r["seated"]:
            if r["depth"][s] > 1 and s != r["run"]:
                if (r["naive"][s] == r["budget"]) != \
                        (r["corr"][s] == r["budget"]):
                    strand_off += 1
    parted = sum(1 for k in tag_cells if k[1] != "tags 0" and
                 (tag_rows[k]["w"].shape() !=
                  tag_rows[(k[0], "tags 0")]["w"].shape() or
                  tag_rows[k]["run"] != tag_rows[(k[0], "tags 0")]["run"]))
    depth_cells = [(p.tag, c) for p in pumps
                   for c in ("global", "per item")]
    depth_climbed = [k for k in depth_cells if depth_rows[k][2] > 0]
    dg = [len(deep_of(depth_rows[(p.tag, "global")][0])) for p in pumps]
    dp = [len(deep_of(depth_rows[(p.tag, "per item")][0])) for p in pumps]

    print("  %-28s %-24s %s"
          % ("the stop law",
             "%d of %d cells climb" % (len(climbed), len(tag_cells)),
             "%d of %d cells climb" % (len(depth_climbed), len(depth_cells))))
    print("  %-28s %-24s %s"
          % ("  and where",
             ("only at " + ", ".join(sorted(set(k[1] for k in climbed))))
             if climbed else "nowhere",
             "every ladder, the exact one included"))
    print("  %-28s %-24s %s"
          % ("the min over products",
             "budget right at %d/%d, strand kind wrong at %d"
             % (budget_ok, budget_n, strand_off),
             "no flat tail anywhere to read it at"))
    print("  %-28s %-24s %s"
          % ("the degree ceiling", "at or under the control at all %d"
             % len(tag_cells), "d_min at every planted reading"))
    print("  %-28s %-24s %s"
          % ("the limit's shape",
             "%d..%d above exponent 1"
             % (min(len(tag_rows[k]["deep"]) for k in tag_cells),
                max(len(tag_rows[k]["deep"]) for k in tag_cells)),
             "%d..%d global, %d..%d per item"
             % (min(dg), max(dg), min(dp), max(dp))))
    print("  %-28s %-24s %s"
          % ("the walk itself", "%d of %d cells part from the control"
             % (parted, len(tag_cells) - len(tag_pumps)), "-"))


def main():
    pumps = ladders()
    s0_forced()
    s1_control(pumps)
    s2_door(pumps)
    tag_rows = s3_tag_laws(arith_ladders())
    depth_rows = s4_depth_laws(pumps)
    s5_verdict(tag_rows, depth_rows, arith_ladders(), pumps)
    print("\n%d checks passed." % CHECKS)


if __name__ == "__main__":
    main()
