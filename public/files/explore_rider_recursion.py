"""explore_rider_recursion.py -- whether the element limit's extra deep
coordinates grow WITHOUT BOUND, settled by arithmetic on the clock's own
increments rather than by a longer walk.

THE QUESTION. Over a ring with classes the greedy limit is the clock plus the
places its class orbit summons, each of the latter gaining about one rider
unit an era (explore_element_limit.py FE6). Whether those coordinates are
UNBOUNDED was left open there, and neither knob reaches it: the tie sweep's
cap already bites nowhere, so the coordinate COUNT is not a scope artifact,
and the walk cannot be bought either -- the tick doubles, so five more eras
cost about 32x the moves and buy five more units. What is left is the
increment sequence itself, which is a recursion in a finite state space.

THE RECURSION, off the door arithmetic at the head of explore_element_limit.py
and not remembered. Write C for the clock's cell, gamma for its class, h for
the class number, T for the tick and e for the clock's exponent. A clock move
takes r = T + 1 - e and lands the clock at exactly T + 1, where ceil_log2
turns over and the tick becomes 2T. The rider that move summons is the minimal
representative of -(r*gamma), a fixed multiset of cells per class; write
w = however many units that multiset puts back on C. Then the clock stands at
T + 1 + w and the next increment is

    r' = 2T + 1 - (T + 1 + w) = T - w.

So with T doubling every era the whole future is

    T_{j+1} = 2 T_j,    r_{j+1} = T_j - w_j,    w_j = rep[-(r_j*gamma)][C],

and w_j reads r_j only through r_j mod h, since scaling a class reduces its
multiplier mod h. THE STATE IS (T mod h, r mod h) AND IT IS FINITE. That is
the whole argument: the sequence of summoned classes is eventually periodic,
a cell hit anywhere inside the CYCLE is hit forever and its coordinate is
unbounded, a cell hit only in the PRE-PERIOD stops and its coordinate is
bounded at a computable exponent. The dichotomy is trivial; that the side is
DECIDABLE per ring, off a recursion with no free parameter, is the finding
this rig is aimed at.

ONE STEP THE ABOVE TAKES FOR GRANTED, AND IT IS THE ONE THE WALK CANNOT
COVER. T' = 2T holds only while the clock's landing at T + 1 + w stays at or
under 2T, that is while w <= T - 1, and past the walk's last era nothing
measures that. It is not an extra hypothesis: w can never exceed the largest
multiplicity the clock's own cell carries in any of the h minimal
representatives -- a constant of the ring -- so the condition is decided ONCE
at the seed tick and holds forever after, T only doubling. S3 asserts it
there rather than leaving the extrapolation to be read as obvious.

W IS A COUNT, NOT A FLAG. The obvious reading -- w = 1 exactly when the rider
lands back on the clock -- is right at the five rings whose minimal
representatives are single points and wrong in general: at g2 a
representative can carry a cell with multiplicity, and the hand-attack below
needs the count. Writing it as a boolean would silently misprice the one ring
whose answer is in doubt.

DO THE CLASS ARITHMETIC IN THE GROUP, NEVER ON THE LABELS. A class here is an
INDEX into the group ring's Cayley table and the labelling is not the
canonical one -- `scale(3, 2)` is 2 at h5 where 3*2 mod 5 is 1, and g2's
labels are further off still. A recursion written as "-r*gamma mod h" on the
labels predicts classes the walk contradicts outright. This is not left as a
warning: S1(b) RUNS the label version and asserts it disagrees, so the rig
carries a detector for its own worst failure rather than a note about it.

THE HAND-ATTACK, on paper before any engine code, at the one ring whose
answer was already legible -- h2, and the control the answer must reproduce.
There gamma is the non-zero class, rep[gamma] = {C} with C the clock's own
cell, and h = 2, so w_j = 1 exactly when r_j is odd. The walk's own ledger
reads a clock at cell (1, 1) taking r = 1 from e = 4, then 3 from 6, then 6
from 11, then 16 from 17, then 32, and no rider unit after the fourth era.
Against the recursion: r = 1 is odd, so w = 1 and r' = T - 1 = 4 - 1 = 3, which
is the walk's. r = 3 is odd, so w = 1 and r' = 8 - 1 = 7 -- and the walk reads
6, SHORT BY ONE, because an OPEN at step 6 put a second unit on the clock in
that era. That is the transient, and it is exactly what the window excludes;
with the era's total w = 2 the recursion reads 8 - 2 = 6 and rejoins. From
there r = 6 is even, so w = 0 and r' = 16, even again, and w = 0 is
ABSORBING. So h2's income does not merely stop, it CANNOT restart -- which is
weaker and truer than reading the stop off the walk's last era, since the
other fixed point (w = 1 forever) is equally consistent with the algebra and
is ruled out by which side of the parity the walk landed on. Two things fall
out of the attack and are frozen as design, not discovered later: the seed
must be taken at the first clock move PAST the transient window, and the
comparison must be era-by-era rather than headline-to-headline, since the
disagreement above is one unit in one era and a multiset quoted over a
window hides it.

WHOSE VOCABULARY. The suspicion is written in the ELEMENT world's terms --
cells, classes, riders, the tick -- which is the world the question lives in.
The one term reached in from a neighbour is the STRAND -- an item left behind
by the transient before the clock settles -- and it is reached in only as a
NAME for a residue this rig measures directly off its own ledger. No strand
law is imported and none is needed: PR5 counts stranded places by reading
which of them stop receiving units, so the admission census that prices
stranding elsewhere is neither used nor tested here.

TRANSPLANT FLAGS, fixed at the freeze.
 1. From explore_element_limit.py: the DOOR, re-derived above; FE6's steady
    state (after the last non-principal open the only move that is not an
    open is the clock's) as a named HYPOTHESIS, which is what makes the
    recursion exhaustive; and the walk itself, used as the CONTROL and never
    as an input to the prediction beyond its seed state.
 2. The recursion is written at h2 first and then read at five other rings.
    That is a storey-up transplant and it is flagged: h2's h is 2, its
    representative a single point, and its answer degenerate on both counts,
    so PR3 and PR5 are stated at the rings where neither holds.

THE SLATE, fixed before any engine code.

 PR1 THE RECURSION REPRODUCES THE WALK'S RIDER LEDGER EXACTLY. Seeded at the
     first clock move past the window, it predicts for every later era both
     the increment and the full multiset of cells taking rider units, and
     every one matches the walk's own `units` ledger, at every branch of
     every ring. KILL: any (branch, era, cell) where the predicted unit count
     differs from the measured one. This is where the index alignment is
     settled -- which era's units subtract from which move's increment -- and
     it is settled by the rig rather than argued.
 PR2 THE SEED IS READ, NOT FITTED. At every clock move past the window the
     walk's own increment equals max(1, T + 1 - e) with T counted off the
     doublings and e off the ledger, so the recursion needs no parameter the
     walk does not hand it. KILL: any clock move taking an increment the door
     does not give -- which is a live possibility and not a formality, the
     menu offering r0 + j for j up to the genus, so a longer core buying a
     cheaper completion would break this at g2 first.
 PR3 THE STATE CYCLES, AND THE PRE-PERIOD IS SHORT. Iterating (T mod h,
     r mod h) reaches a cycle at every ring and branch. Predicted: pre-period
     at most the 2-adic valuation of h plus one, cycle length dividing the
     multiplicative order of 2 modulo the odd part of h. KILL: no cycle
     inside h^2 steps, or a pre-period or length outside those bounds.
 PR4 THE VERDICT PER COORDINATE. A cell in the cycle's support gains units
     forever and its coordinate is UNBOUNDED; a cell only in the pre-period's
     is bounded at the exponent it stops on. Predicted: h5's two rider-fed
     places are both in the cycle, so all three of its deep coordinates are
     unbounded; h2's and h4's cycle support away from the clock is EMPTY, so
     the clock alone is unbounded; h3 and F_2[x] have gamma = 0 and no rider
     at all. KILL: a cell the walk still feeds in its last era that the cycle
     does not contain.
 PR5 G2'S SPREAD IS THE TRANSIENT'S, NOT THE MECHANISM'S. The cycle support
     is a function of gamma alone, so the recursion predicts ONE steady-state
     coordinate count per gamma while the walk prints 3 to 6 deep places over
     g2's 120 branches. Predicted: the post-window rider support is the same
     at every branch sharing a gamma, and every branch's excess deep places
     are places that take no unit after the window -- strands. KILL: two
     branches with the same gamma whose post-window rider supports differ, or
     a deep place outside both sets. This is the clause that decides whether
     the recursion explains g2 or merely fails to contradict it.
 PR6 WHAT THE VERDICT RESTS ON, AND THE ASYMMETRY. The steady state assumes
     no fresh open ever summons a rider again (FE2, read off the cell counts
     to degree 1200). Predicted: that hypothesis is one-sided -- a late rider
     could only ADD units, so an UNBOUNDED verdict survives its failure and a
     BOUNDED one does not. The rig prints the last degree with no principal
     place per ring against the degrees the walk actually reaches, so the
     margin is visible rather than asserted.

THE DESIGN: a control in three parts, then three sections.

 S1 THE POSITIVE CONTROL, run before any verdict is read.
    (a) THE DOOR AT EVERY CLOCK MOVE (PR2): the walk's increment against
        max(1, T + 1 - e), T counted off the doublings.
    (b) THE LABEL TRAP AS A DETECTOR: the recursion re-run with the class
        arithmetic done on the LABELS, asserted to disagree with the walk at
        h5 -- so a rig that had silently fallen back to label arithmetic
        would fail here instead of printing a wrong verdict.
    (c) H2'S ABSORBING STATE: the hand-attack's sequence, including the era
        where an open's unit is what rejoins prediction to walk.
 S2 THE RECURSION AGAINST THE WALK (PR1): per ring and branch, the predicted
    and measured rider ledger era by era, and the count of eras compared.
 S3 THE CYCLE (PR3, PR4): per ring and gamma, the pre-period, the cycle, the
    classes summoned inside it and the cells they reach.
 S4 THE VERDICT (PR4, PR5, PR6): per branch, every deep place sorted into
    unbounded, bounded-at-an-exponent, or stranded in the transient, against
    the deep-place count the walk prints.

THE FINDINGS.

FR1 THE RECURSION IS THE WALK, ERA FOR ERA (rule in range -- six rings, every
    branch of every complete branch set, 964 eras compared and not one
    mismatch, over the 2 to 6 cells each ring's riders reach). Seeded only at
    the branch's first post-window clock move, it predicts every later
    increment and the exact multiset of cells taking units. So the INDEX
    ALIGNMENT that was in doubt is settled in the direction the door
    arithmetic gives: the units subtract from the increment of the move that
    FOLLOWS the era they land in. And no rider unit past the window ever
    arrives without a clock move, which is asserted rather than assumed --
    without it the era-by-era comparison would be comparing two different
    ledgers.

FR2 THE SEED IS READ OFF THE DOOR, NOT FITTED (rule in range -- 964 clock
    moves past the window at six rings, none of them taking a core longer
    than max(1, T + 1 - e)). The menu offers r0 + j for j up to the genus, so
    this had a way to fail and g2's 776 moves are where it would have; the
    longest core over the door is 0 everywhere. The recursion therefore has
    no free parameter at all: the walk hands it a state and the door hands it
    every increment after that.

FR3 THE STATE CYCLES ALMOST IMMEDIATELY (rule in range). The pre-period is 0
    or 1 at every ring and branch and the cycle length is 1, 2 or 4. Both
    bounds the slate named hold, and both are ASSERTED rather than read off
    the table: the length divides the order of 2 modulo the odd part of h,
    and the pre-period is at most the 2-adic valuation of h PLUS ONE -- the
    plus one carrying the whole clause at h5 and g2, whose h are 5 and 15
    and whose valuation is therefore 0 against branches that do take a
    pre-period of 1. The cycle is exhibited, so the dichotomy stops being a
    dichotomy and becomes a verdict.

FR4 THE ANSWER: YES AT h5 AND g2, AND EXACTLY THREE COORDINATES AT EACH
    (proved for the steady state, and a rule in range at every branch of
    every complete branch set). The unbounded count is 1 at F_2[x], h2, h3
    and h4 -- the clock alone -- and 3 at both h5 and g2, on every one of
    their 20 and 120 branches. At h5 the clock is inside its own rider orbit
    and at g2 it is not, and the count is 3 either way, the clock being
    unbounded through its own core increments whatever its riders do. h2's
    case is the sharpest: w = 0 maps to itself, so its rider income is not
    merely observed to stop, it is in an ABSORBING state and cannot restart.

FR5 g2'S SPREAD IS THE TRANSIENT'S, AND THE BOTTOM OF IT IS THE STEADY STATE
    (rule in range, all 120 branches). The cycle support is a function of
    gamma alone -- one distinct support per gamma at every ring, which is
    PR5's kill missing -- so the recursion predicts the SAME three unbounded
    coordinates at every g2 branch, and the printed spread of 3 to 6 deep
    places decomposes exactly: 3 unbounded, 0 or 1 bounded, 0 to 3 stranded
    -- three columns whose ranges are read separately and whose SUM at each
    branch is that branch's own deep count, so the maxima are not addable.
    Nothing outside those three ever appears. So the count the sweep reads
    over branches was never a statement about the mechanism, and the number
    that is -- the count that survives -- is its MINIMUM. The same reading
    closes h2 and h4, whose [1, 2] is 1 unbounded plus 0 or 1 strand. THE
    STRAND LAWS WERE NOT NEEDED: the admission census that prices stranding
    in the schedule family would have predicted a count, and the scope caveat
    on importing it into the element world is real, but the residue is
    measured directly off this rig's own ledger and no law crosses over.

FR6 A THIRD KIND OF COORDINATE, AND ONLY g2 HAS IT (observation, one ring,
    over its complete branch set). Between the unbounded and the stranded
    sits a place that deepens PAST the window -- so it is not a strand -- and
    then stops forever, because the cells its class summons lie in the
    recursion's pre-period and not in its cycle. It appears on some g2
    branches and never at any other ring, at cells (1, 1), (1, 2), (1, 3),
    (1, 4), (2, 13) and (2, 14), stopping at exponents 2 to 6. Two of those
    are DEGREE-2 cells, which no other ring's riders reach at all. h5 has a
    pre-period too and no bounded coordinate, its pre-period cells already
    lying in its cycle -- so what makes the species is not the pre-period but
    a pre-period reaching OUTSIDE the cycle, and h = 15 having proper
    subgroups is the obvious place to look for why.

FR7 THE TWO VERDICTS DO NOT REST ON THE SAME HYPOTHESIS. Both inherit FE2 --
    no fresh open summons a rider again, read off cell counts exact to degree
    1200 against walks that reach degrees 291 to 293 -- but only one of them can
    be hurt by it. A late rider ADDS units, so it cannot stop an unbounded
    coordinate; it could restart a bounded one. FR4's YES is therefore
    firmer than FR6's stopping, and the same asymmetry makes the last degree
    with no principal place (4, 4, 4, 5 and 7 at the five rings that have
    one) a margin worth printing rather than a formality.

Run: `python explore_rider_recursion.py`. RUN RECORD (2521 checks, ~87 s, peak
48.9 MB under memwatch, the walk being 300 moves on each of 150 branches over
six rings and the recursion itself free). S1 control: every one of the 964
post-window clock moves taking exactly the door's increment; the label-
arithmetic recursion run alongside and DISAGREEING with the walk at h5 and g2
-- and coinciding with the group version at h2 and h4, where the detector is
therefore vacuous and says so; h2's era ledger reproduced including the era
whose second unit comes from an open. S2: 964 eras, 0 mismatched. S3: the
cycles exhibited, both of PR3's bounds asserted per branch and the tick's own
doubling asserted at every seed, pre-period 0 or 1 and length 1, 2 or 4, with
4 gamma at h5 and 4 at g2. S4: every branch's deep places first asserted to lie in
DISTINCT cells -- the verdict being per cell and the list per place -- and
then all 150 branches' sorted into unbounded, bounded and stranded with
nothing left over. Slate PR1-PR6: all six hit; no
kill fired. SUPERSEDED at the run: the reading that g2's steady state carries
FOUR rider cells and would predict a uniform five deep places -- that count
was taken over a WINDOW of the sequence rather than over its cycle, and the
cycle carries two.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_greedy_image_ec as EC        # the genus 0 and 1 rings
import explore_greedy_image_g2 as G2        # the genus 2 ring
import explore_coarse_type as CT            # the ladder
import explore_element_limit as EL          # the walk, the cells, the door

CHECKS = 0
CYCLE_CAP = 4096          # the state search bound, asserted against


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ------------------------------------------------------- reading a branch
def window_of(s):
    """The step past which FE6's steady state speaks: the clock established
    and the low-degree transient over, the last open that summoned a rider
    being what ends it. The same reading explore_element_limit.py's S4 uses,
    recomputed here off the same fields rather than imported, so this rig
    fails on its own terms if the reading drifts."""
    st0, _last = EL.settling(s)
    trans = max(s.doubles[0][0], max(s.open_riders) if s.open_riders else -1)
    return max(s.doubles[0][0] if st0 is None else st0, trans)


def tick_at(s, step):
    """The tick standing BEFORE the move at `step`: the walk starts at 1 and
    doubles once per recorded doubling, so counting them is independent of
    anything the recursion says."""
    return 1 << sum(1 for rec in s.doubles if rec[0] < step)


def clock_moves(s):
    """(step, increment, exponent before, {cell: rider units}) per move the
    clock's own slot took as a CORE, in step order -- the walk's ledger read
    as eras. Rider units at the same step are the move's own summons."""
    _st0, last = EL.settling(s)
    cell, slot = last
    rows, by_step = [], {}
    for step, c2, s2, kind, n, pre in s.units:
        if kind == "rider":
            by_step.setdefault(step, {})
            by_step[step][c2] = by_step[step].get(c2, 0) + n
        elif (c2, s2) == (cell, slot):
            rows.append([step, n, pre, None])
    for row in rows:
        row[3] = by_step.get(row[0], {})
    return [tuple(r) for r in rows], (cell, slot)


def stray_riders(s, win):
    """Rider units past the window that did NOT arrive with a clock move --
    the steady state says there are none, and PR1's comparison would be
    meaningless if there were, so it is checked rather than assumed."""
    steps = set(step for step, _c, _s, kind, _n, _p in s.units
                if kind == "core" and (_c, _s) == EL.settling(s)[1])
    out = []
    for step, c2, _s2, kind, n, _pre in s.units:
        if kind == "rider" and step > win and step not in steps:
            out.append((step, c2, n))
    return out


# ------------------------------------------------------------ the recursion
def summon(s, gam, r, labels=False):
    """The cells the rider of a clock move of increment r reaches, with their
    unit counts. In the GROUP unless `labels`, which is the trap S1(b) runs
    on purpose."""
    GR = s.GR
    if labels:
        c = (-(r * gam)) % s.h
    else:
        c = GR.negc[GR.scale(gam, r)]
    return dict(s.rep[c])


def step_rec(s, gam, clock_cell, T, r, labels=False):
    """One era: the cells this move's rider reaches, and the next (T, r)."""
    cells = summon(s, gam, r, labels)
    w = cells.get(clock_cell, 0)
    return cells, w, 2 * T, T - w


def predict(s, gam, clock_cell, T0, r0, n, labels=False):
    """n eras of the recursion from (T0, r0): (increment, {cell: units}) per
    era, the clock's own r folded into its cell so the row is comparable to
    the walk's ledger without either side being reshaped to fit."""
    out, T, r = [], T0, r0
    for _ in range(n):
        cells, w, T2, r2 = step_rec(s, gam, clock_cell, T, r, labels)
        row = dict(cells)
        row[clock_cell] = row.get(clock_cell, 0) + r
        out.append((r, row))
        T, r = T2, r2
    return out


def measured(s, rows, clock_cell):
    """The walk's ledger in the same shape: the core increment folded into
    the clock's cell beside whatever the rider put there."""
    out = []
    for _step, r, _pre, riders in rows:
        row = dict(riders)
        row[clock_cell] = row.get(clock_cell, 0) + r
        out.append((r, row))
    return out


def cycle_of(s, gam, clock_cell, T0, r0):
    """(pre-period length, cycle length, the (T mod h, r mod h) states of the
    cycle, the cells the cycle summons, the cells the pre-period summons).
    The state space is finite, so the search terminates; CYCLE_CAP is the
    assertion that it did so where expected and not a truncation."""
    h = s.h
    seen, order, T, r = {}, [], T0 % h, r0 % h
    for i in range(CYCLE_CAP):
        key = (T % h, r % h)
        if key in seen:
            start = seen[key]
            pre = order[:start]
            cyc = order[start:]
            pre_cells, cyc_cells = {}, {}
            for _T, rr in pre:
                for c, n in summon(s, gam, rr).items():
                    pre_cells[c] = pre_cells.get(c, 0) + n
            for _T, rr in cyc:
                for c, n in summon(s, gam, rr).items():
                    cyc_cells[c] = cyc_cells.get(c, 0) + n
            return len(pre), len(cyc), cyc, cyc_cells, pre_cells
        seen[key] = i
        order.append((T % h, r % h))
        _cells, w, _T2, r2 = step_rec(s, gam, clock_cell, T, r)
        T, r = (2 * T) % h, r2 % h
    ok(False, "the state search ran %d steps at h=%d without repeating"
       % (CYCLE_CAP, h))


def bare_degrees(L):
    """Every degree in the light walker's universe with no principal place --
    what FE2's bounded initial stretch is bounded BY, and PR6's margin."""
    npl = EL.cell_universe(L)[1]
    return [d for d in range(1, EL.DEG_CAP + 1) if npl[d][0] == 0]


def main():
    EC.DMAX = G2.DMAX = EL.ENGINE_DMAX
    ladder = CT.build_ladder()

    print("The element limit's rider-fed coordinates, decided by the clock's")
    print("own increment recursion rather than by a longer walk. Every ring")
    print("is walked exactly as explore_element_limit.py walks it -- %d moves"
          % EL.WALK_N)
    print("on every branch of the complete tie sweep -- and that walk is the")
    print("CONTROL here, never an input to the prediction beyond its seed.")

    shapes = {}
    for L in ladder:
        got, dropped = EL.branches(L, record=False)
        ok(dropped == 0, "%s: the branch sweep dropped %d states, so no "
           "column here is over all branches" % (L.name, dropped))
        shapes[L.name] = [EL.continue_walk(s, EL.WALK_N - EL.BRANCH_N, [0, 0])
                          for s in got]

    section("S1  THE POSITIVE CONTROL")

    print("(a) THE DOOR AT EVERY CLOCK MOVE (PR2)")
    print("  The walk's own increment against max(1, T + 1 - e), the tick")
    print("  counted off the doublings and the exponent off the ledger. The")
    print("  menu offers a core longer than the door by up to the genus, so")
    print("  this can fail, and at g2 first.")
    print("\n  ring     branches  clock moves past the window  longest core "
          "over the door")
    for L in ladder:
        tot, over = 0, 0
        for s in shapes[L.name]:
            win = window_of(s)
            rows, (cell, _slot) = clock_moves(s)
            for step, r, pre, _rid in rows:
                if step <= win:
                    continue
                tot += 1
                door = max(1, tick_at(s, step) + 1 - pre)
                ok(r >= door, "%s: a clock move took increment %d under the "
                   "door's %d at step %d" % (L.name, r, door, step))
                over = max(over, r - door)
        print("  %-8s %-9d %-28d %d" % (L.name, len(shapes[L.name]), tot, over))
        ok(tot > 0, "%s: no clock move past the window, so PR2 is vacuous "
           "here" % L.name)

    print("\n(b) THE LABEL TRAP AS A DETECTOR")
    print("  The same recursion with the class arithmetic done on the LABELS")
    print("  rather than in the group. It must DISAGREE with the walk: a rig")
    print("  that had quietly fallen back to label arithmetic fails here")
    print("  instead of printing a wrong verdict. Shown at every ring whose")
    print("  labelling is not canonical, which is where the trap can spring.")
    print("\n  ring     gamma  group support   label support   disagree")
    for L in ladder:
        s = shapes[L.name][0]
        _st0, last = EL.settling(s)
        gam, cell = last[0][1], last[0]
        if gam == 0:
            continue
        win = window_of(s)
        rows, _c = clock_moves(s)
        past = [r for r in rows if r[0] > win]
        T0 = tick_at(s, past[0][0])
        grp = predict(s, gam, cell, T0, past[0][1], len(past))
        lab = predict(s, gam, cell, T0, past[0][1], len(past), labels=True)
        gs = sorted(set(c for _r, row in grp for c in row))
        ls = sorted(set(c for _r, row in lab for c in row))
        meas = measured(s, past, cell)
        agree_g, agree_l = grp == meas, lab == meas
        ok(agree_g, "%s: the GROUP recursion already disagrees with the walk "
           "at branch 0, so the detector below reads nothing" % L.name)
        print("  %-8s %-6d %-15s %-15s %s"
              % (L.name, gam, gs, ls, "yes" if not agree_l else "NO"))
        if gs != ls:
            ok(not agree_l, "%s: the LABEL recursion agrees with the walk, so "
               "this rig's detector for its own worst failure is dead"
               % L.name)
        else:
            print("           (the two coincide at this gamma -- the detector "
                  "is vacuous here)")

    print("\n(c) H2'S ABSORBING STATE")
    print("  The hand-attack's own sequence, era by era, including the era")
    print("  where an OPEN's unit -- not the clock's -- is what rejoins the")
    print("  prediction to the walk. w = 0 is absorbing, so the income cannot")
    print("  restart; the walk decides which fixed point h2 is in.")
    s = shapes["h2"][0]
    _st0, last = EL.settling(s)
    cell, gam = last[0], last[0][1]
    rows, _c = clock_moves(s)
    print("\n  step  tick  e before  increment  rider units on the clock")
    for step, r, pre, rid in rows[:7]:
        print("  %-5d %-5d %-9d %-10d %d"
              % (step, tick_at(s, step), pre, r, rid.get(cell, 0)))
    w_tail = [rid.get(cell, 0) for _st, _r, _p, rid in rows if _st > window_of(s)]
    ok(set(w_tail) == set([0]), "h2: the clock still takes rider units past "
       "the window: %s" % w_tail)
    print("  every era past the window at step %d takes w = 0, and w = 0 maps"
          % window_of(s))
    print("  to itself, so h2's rider income is in the absorbing fixed point.")

    section("S2  THE RECURSION AGAINST THE WALK")
    print("  PR1. Seeded at the first clock move past the window with the")
    print("  increment the door gives there, the recursion predicts every")
    print("  later era's increment AND the full multiset of cells taking")
    print("  rider units. Compared era by era, not headline to headline: the")
    print("  hand-attack's own disagreement was one unit in one era.")
    print("\n  ring     branches  eras compared  cells ranged over  "
          "mismatched eras")
    for L in ladder:
        eras, cells, bad = 0, set(), 0
        for s in shapes[L.name]:
            win = window_of(s)
            _st0, last = EL.settling(s)
            cell, gam = last[0], last[0][1]
            stray = stray_riders(s, win)
            ok(not stray, "%s: %d rider units past the window arrived without "
               "a clock move: %s" % (L.name, len(stray), stray[:3]))
            rows, _c = clock_moves(s)
            past = [r for r in rows if r[0] > win]
            ok(past, "%s: no clock move past the window" % L.name)
            T0 = tick_at(s, past[0][0])
            pred = predict(s, gam, cell, T0, past[0][1], len(past))
            meas = measured(s, past, cell)
            for i, (p, m) in enumerate(zip(pred, meas)):
                eras += 1
                cells |= set(p[1]) | set(m[1])
                if p != m:
                    bad += 1
                    print("    MISMATCH %s era %d: predicted %s, measured %s"
                          % (L.name, i, p, m))
        ok(bad == 0, "%s: %d eras where the recursion and the walk part"
           % (L.name, bad))
        print("  %-8s %-9d %-14d %-18d %d"
              % (L.name, len(shapes[L.name]), eras, len(cells), bad))

    section("S3  THE CYCLE")
    print("  PR3. The state (T mod h, r mod h) is finite, so the increment")
    print("  sequence is eventually periodic; the cycle is EXHIBITED rather")
    print("  than argued. gamma is per BRANCH, not per ring, so the table is")
    print("  over the distinct gamma each ring's branch set actually reads.")
    print("\n  ring     h   gamma  pre-period  cycle  classes in the cycle  "
          "cells it summons")
    print("  THE CYCLE IS COMPUTED PER BRANCH, not per gamma. The seed is the")
    print("  branch's own state at its first post-window clock move, and two")
    print("  branches sharing a gamma need not share it -- whether they reach")
    print("  the same cycle anyway is PR5's question and is read at S4, so")
    print("  presuming it here would answer the question with the indexing.")
    print("  A row is one DISTINCT (gamma, pre-period, cycle) the ring's")
    print("  branches actually reach, with how many branches reach it.")
    print("\n  ring     h   gamma  branches  pre-period  cycle  classes in "
          "the cycle  cells it summons")
    verdicts, distinct = {}, {}
    for L in ladder:
        for bi, s in enumerate(shapes[L.name]):
            _st0, last = EL.settling(s)
            cell, gam = last[0], last[0][1]
            win = window_of(s)
            rows, _c = clock_moves(s)
            past = [r for r in rows if r[0] > win]
            T0, r0 = tick_at(s, past[0][0]), past[0][1]
            npre, nc, cyc, cyc_cells, pre_cells = cycle_of(s, gam, cell, T0, r0)
            ok(npre + nc <= s.h * s.h, "%s: pre-period %d plus cycle %d "
               "exceeds h^2 = %d" % (L.name, npre, nc, s.h * s.h))
            # PR3's KILL, which the h^2 bound above is far too loose to
            # fire: the state is (T mod h, r mod h) and T's own orbit is
            # the powers of 2, so the pre-period cannot outlast 2's and the
            # length must divide 2's order on the odd part. Without these
            # two the slate named a kill the rig could not have fired.
            v2, odd = 0, s.h
            while odd % 2 == 0:
                v2, odd = v2 + 1, odd // 2
            o2, x = 1, 2 % odd
            while x != 1 % odd:
                x, o2 = (2 * x) % odd, o2 + 1
            ok(npre <= v2 + 1, "%s: pre-period %d over the 2-adic valuation "
               "of h = %d plus one" % (L.name, npre, v2))
            ok(o2 % nc == 0, "%s: cycle length %d does not divide the order "
               "%d of 2 modulo the odd part %d of h"
               % (L.name, nc, o2, odd))
            # THE STEP THE RECURSION TAKES FOR GRANTED WHEN IT RUNS PAST
            # THE WALK. T' = 2T holds only while the clock's landing at
            # T + 1 + w stays at or under 2T, i.e. while w <= T - 1. Inside
            # the walk PR1's era-by-era match covers it; past the walk
            # nothing does, and it is the one place the extrapolation could
            # quietly be a different recursion. w is bounded by the largest
            # multiplicity the clock's own cell has in ANY of the h minimal
            # representatives -- a constant of the ring -- so the condition
            # is decided once, at the seed tick, and holds forever after,
            # T only doubling.
            wmax = max(s.rep[c].get(cell, 0) for c in range(s.h))
            ok(wmax + 1 <= T0, "%s: the clock's cell takes up to %d units "
               "from a single representative against a seed tick of %d, so "
               "T' = 2T is not guaranteed past the walk"
               % (L.name, wmax, T0))
            classes = tuple(sorted(set(s.GR.negc[s.GR.scale(gam, r)]
                                       for _T, r in cyc)))
            verdicts[(L.name, bi)] = (cell, npre, nc, cyc_cells, pre_cells)
            row = (gam, npre, nc, classes, tuple(sorted(cyc_cells)))
            distinct.setdefault(L.name, {})
            distinct[L.name][row] = distinct[L.name].get(row, 0) + 1
        for row in sorted(distinct[L.name]):
            gam, npre, nc, classes, cells = row
            print("  %-8s %-3d %-6d %-9d %-11d %-6d %-21s %s"
                  % (L.name, shapes[L.name][0].h, gam, distinct[L.name][row],
                     npre, nc, list(classes), list(cells)))

    section("S4  THE VERDICT")
    print("  PR4, PR5, PR6. Every deep place of every branch sorted by what")
    print("  the recursion says of it: a cell the CYCLE summons gains units")
    print("  forever, a cell only the PRE-PERIOD summons stops, and a place")
    print("  in neither took its units before the window and is a STRAND. The")
    print("  three must exhaust the branch's deep places, which is the check.")
    print("\n  ring     deep places  unbounded  bounded  stranded  "
          "distinct cycle supports per gamma (PR5)")
    for L in ladder:
        deep, unb, bnd, strand = set(), set(), set(), set()
        supports, stopped = {}, set()
        for bi, s in enumerate(shapes[L.name]):
            _st0, last = EL.settling(s)
            cell, gam = last[0], last[0][1]
            _c, npre, _nc, cyc_cells, pre_cells = verdicts[(L.name, bi)]
            win = window_of(s)
            past = [r for r in clock_moves(s)[0] if r[0] > win]
            after = set()
            for step, c2, _s2, kind, _n, _pre in s.units:
                if step > win and kind == "rider":
                    after.add(c2)
            supports.setdefault(gam, set()).add(tuple(sorted(cyc_cells)))
            # the recursion must ACCOUNT for the walk: every cell the walk
            # still feeds past the window is one the recursion summons, and
            # every cell it summons within the walked eras is one the walk
            # fed. Neither direction is implied by PR1's era comparison
            # alone once the cycle is read past the walk's own length.
            ok(after <= set(cyc_cells) | set(pre_cells),
               "%s branch %d: %s took units past the window and the "
               "recursion does not summon them"
               % (L.name, bi, sorted(after - set(cyc_cells) - set(pre_cells))))
            places = EL.deep_places(s)
            # THE SORT IS BY CELL AND THE THING SORTED IS A PLACE, so two
            # deep places in one cell would inherit one verdict between them
            # and the three counts below would not be counting what they
            # say. The walker asserts singleton cells only for the RIDER
            # TARGETS; the clock's cell and any stranded one are outside
            # that guarantee, so assert it here over exactly the places
            # being sorted.
            ok(len(set((d, c) for d, c, _e, _co, _ri in places))
               == len(places), "%s branch %d: two deep places share a cell, "
               "so the verdict below is per-cell over a per-place list: %s"
               % (L.name, bi, places))
            deep.add(len(places))
            u = b = t = 0
            for d, c, _e, _co, _ri in places:
                if (d, c) == cell or (d, c) in cyc_cells:
                    u += 1
                elif (d, c) in pre_cells:
                    b += 1
                else:
                    ok((d, c) not in after, "%s: cell %s took a unit past the "
                       "window and the recursion does not summon it"
                       % (L.name, (d, c)))
                    t += 1
            unb.add(u)
            bnd.add(b)
            strand.add(t)
            # PR4's second half has a NUMBER in it -- a bounded coordinate
            # stops at a computable exponent -- so name it rather than let
            # the count stand for it, and check the stopping directly: a
            # pre-period-only cell takes no unit in the walk's LAST era.
            for d, c, e, _co, _ri in places:
                if (d, c) == cell or (d, c) in cyc_cells:
                    continue
                if (d, c) in pre_cells:
                    lastera = max(st for st, c2, _s2, k, _n, _p in s.units
                                  if c2 == (d, c) and k == "rider")
                    # WHERE IT MUST STOP IS THE PRE-PERIOD'S END, not the
                    # walk's. "Its last unit came before the walk's last
                    # clock move" would pass for a coordinate still being
                    # fed every second era, which is the reading this
                    # claim exists to exclude; the recursion says the last
                    # unit lands at or before the pre-period's own last
                    # move, and there are enough walked eras past that for
                    # the difference to bite.
                    ok(npre > 0, "%s: cell %s is filed as pre-period-only "
                       "at a branch whose pre-period is empty"
                       % (L.name, (d, c)))
                    ok(lastera <= past[npre - 1][0],
                       "%s: the pre-period cell %s took a unit at step %d, "
                       "past the pre-period's last clock move at step %d of "
                       "%d walked past the window"
                       % (L.name, (d, c), lastera, past[npre - 1][0],
                          len(past)))
                    stopped.add(((d, c), e))
        print("  %-8s %-12s %-10s %-8s %-9s %s"
              % (L.name, sorted(deep), sorted(unb), sorted(bnd),
                 sorted(strand),
                 dict((g, len(ss)) for g, ss in sorted(supports.items()))))
        if stopped:
            print("           the bounded coordinates as (cell, the exponent "
                  "it stops at), the UNION over branches and never one "
                  "branch's list -- the column above is the per-branch "
                  "count: %s" % sorted(stopped))

    print("\n  PR6, the hypothesis the BOUNDED verdicts rest on and the")
    print("  UNBOUNDED ones do not: no fresh open summons a rider again. A")
    print("  late rider could only ADD units, so it cannot make an unbounded")
    print("  coordinate stop -- only a bounded one restart. The margin:")
    print("\n  ring     last degree with no principal place  degrees the walk "
          "reaches  universe")
    for L in ladder:
        bare = bare_degrees(L)
        reach = max(max(d for (d, _c) in s.seat) for s in shapes[L.name])
        print("  %-8s %-36s %-24d %d"
              % (L.name, max(bare) if bare else "none", reach, EL.DEG_CAP))
        ok(not bare or max(bare) < reach, "%s: a degree with no principal "
           "place sits above everything the walk reached" % L.name)

    section("SUMMARY")
    print("  %d checks passed." % CHECKS)


if __name__ == "__main__":
    main()
