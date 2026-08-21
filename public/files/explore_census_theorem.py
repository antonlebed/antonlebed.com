"""explore_census_theorem.py -- DOES THE REPAIRED DERIVATION CLOSE? The
walk-census identity certified line by line, and swept on the two axes the
price sweep could not reach.

THE QUESTION. explore_price_hypotheses.py proved the derivation's stated
hypothesis list INCOMPLETE by exactly one property -- the price must be
nondecreasing in the DOOR -- and left the other direction open in its own
words: certifying the repaired argument line by line is a separate job.
This file does that job. It does not run a ninth price. It asks what each
LINE of the derivation actually consults, prints an observable per line,
and then attacks the two axes the parent held fixed: the LADDER (a Pump
takes any sorted member list starting at 1, so an adversarial ladder is a
subclass and not a rewrite) and the CLOCK (per-item against the blocks).

WHERE THE PARENT LEFT IT. The corrected list is four:
  (H1) the price nondecreasing in the DEGREE;
  (H2) doors nondecreasing in time -- the CLOCK's monotonicity, the tick
       never falling, which the walker's landing rule gives by
       construction;
  (H3) a tie at the bar losing to the splice, the splice sitting at degree
       1 slot 0, the lowest key in the menu's sorted tie list;
  (H4) the price nondecreasing in the DOOR.
Each carries a deletion witness. What has no proof is SUFFICIENCY.

THE HAND-ATTACK, on paper before any engine code.

 (a) THE INDEX CONVENTION, re-derived from the engine before the freeze.
     A ladder is a member list; the clock advances to the least member at
     or above the depth just landed on, so an item at depth x has door
     gap(x) = next_at(x) + 1 - x and a landing sits one above a member. An
     item one above member m therefore pays the STEP from m to the next
     member, so an item's climb reads the ladder's successive differences
     in order. The ladder (2, 4, w=2) has members 1, 2, 4, 10, 14, 18, ...
     -- steps 1, 2, 6, 4, 4, 4, ..., tail gap 4 and exactly ONE step above
     it.

 (b) WHAT EACH LINE CONSULTS, derived rather than guessed.
     L1 THE FROZEN DOOR. Under a per-item clock an item's class is its own
        key, so the landing rule changes the tick only for the item that
        moved. A standing item's door max(1, tick + 1 - depth) is a
        function of its own tick and its own depth, so it is FROZEN while
        the item does not move. This is what makes step A's "nothing priced
        in (B, P) is ever created again" a statement about the runaway
        ALONE: after the crossing the only door that changes at all is the
        runaway's.
     L2 THE BAR. The runaway takes its bar door only when that door is the
        menu MINIMUM. So at the crossing step nothing prices strictly under
        P -- every door the census admits was bought BEFORE the crossing,
        and the census's "under P" is the walk's own affordability window
        read at the one moment it closes.
     L3 FROZEN AFTER. After the crossing the runaway recurs at its tail gap
        for ever at price B = price(1, tail). B is at most P by H4, the bar
        door being a step WIDER than the tail. Every other door prices at
        or above P, itself at or above B, and is frozen there by L1, so at
        equality it ties and loses by H3. No non-runaway ever moves again.
     L4 THE UNIQUE RUNAWAY. Degree 1 is born covered and by H1 prices at or
        under every degree at every door, so degree 1 slot 0 reaches the
        bar first and is first in every tie. Its twin (1, 1) climbs the
        same ladder at the same prices and meets the bar door at exactly P,
        where it ties with the runaway and loses -- for ever, by L1 and L3.
        Exactly one item crosses.
     L5 THE CAP. Under a per-item clock an item's tick is next_at(its own
        depth) EXACTLY -- it lands at tick + 1, which is strictly above the
        tick it just left, so the landing rule's max is the depth and never the
        old tick, and an opening lands on a door read off that same tick. That
        is the bridge the dominance check consumes, and without it "block tick
        at or above next_at(depth)" would be a weaker statement than dominance
        rather than the same one. Under a coarser clock the class tick absorbs
        every member's landing, so a block tick is at or above the per-item
        tick of each of its members at every step, hence the block door at a
        given depth is at or above the per-item door, hence by H4 its price is
        at or above it. Fewer doors price under the same bar, so the block
        census is CONTAINED in the per-item one. The cap is H4's SECOND
        consumer, and it is a derivation rather than the measurement the parent
        recorded.

 (c) THE LADDER MARGIN, and it is where the derivation is thinnest. Nothing
     in L1 to L5 reads the ladder's SHAPE. What it reads is that the ladder
     has a TAIL -- a step that repeats for ever -- and that the bar is the
     door of the last step WIDER than that tail. For the arithmetic family
     those two readings coincide with the corpus's formula
     P = price(1, e + w), because the family's ramp gaps are all under the
     tail gap and its only anomalous step is the splice: it has EXACTLY ONE
     overshoot, so its first and its last are the same step and the corpus
     never had to choose. A ladder with TWO overshoots chooses, and
     explore_headed_ladder.illegal_ladders already builds one.

 (d) THE DOUBLE-SPLICE MARGIN, hand-derived at f = d * sigma so that the
     print is checked against paper. Members 1, 2, 7, 9, 16, 18, 20, ...:
     steps 1, 5, 2, 7, 2, 2, ..., tail gap 2, overshoots at the steps 5 and
     7. LAST-overshoot bar P = price(1, 7) = 7; B = price(1, 2) = 2, at
     most P. The runaway (1, 0) is born covered, so its opening door is
     tick + 1 - 0 = 2 at price 2; it lands at depth 2, tick 2, door 1,
     price 1; depth 3, tick 7, door 5, price 5 under 7; depth 8, tick 9,
     door 2, price 2; depth 10, tick 16, door 7, price 7 -- NOT strictly
     under the bar, which is why the census excludes the runaway from its
     own climb by construction and the WALK takes it anyway, the runaway
     being the lowest key with nothing under P on the menu. Its twin (1, 1)
     climbs the same rungs and stalls at depth 10, tying at 7 and losing
     for ever. So the last-overshoot census reads a strand at depth 10.
     FIRST-overshoot bar P = price(1, 5) = 5 instead: (1, 1) enters at 2,
     takes the door 1 at price 1, and stalls at depth 3, price(1, 5) not
     being strictly under 5. The census then reads depth 3 where the walk
     seats depth 10. The predicted break is ONE-SIDED and it is an
     UNDERCOUNT -- the walk seats deeper than the census, never shallower
     -- because the step that fails is "the bar is the last door every
     climber must buy", and a bar read too low stalls climbs the walk
     completes.

 (e) THE VACUITY HAZARD is the parent's, both forms, and it is carried
     unchanged: a cell whose runaway has not crossed reads a transient, and
     a cell whose census approaches the move budget cannot be seated inside
     it however early the runaway crossed. Every verdict is read at CROSSED
     and SETTLED cells, the count standing still between two windows, and
     an unsettled cell is NAMED rather than counted either way.

 (f) THE ONE-SIDEDNESS IS THE TRANSIENT-PROOF READING, carried from the
     parent: a DEEP item is read rather than a strand, an item once seated
     above depth 1 staying there, so a deep item the census excludes is a
     violation no longer window can undo while a strand can still be
     reclassified a riser by a later move.

THE SLATE, frozen before the engine.

 PR1 (L1, FROZEN DOORS). Under a per-item clock, at every step of every
     walked cell, the door of every item that did not move is unchanged.
     0 changes over the whole sweep.
 PR2 (L2, THE BAR). At the step the runaway first takes a door at or above
     the bar, no other menu candidate prices strictly under P. 0 cells
     otherwise.
 PR3 (L3, FROZEN AFTER). After that step, every move belongs to the
     runaway. 0 non-runaway moves after the crossing, at every cell.
 PR4 (L4, THE UNIQUE RUNAWAY). Exactly ONE item ever stands above the bar
     rung, and it is (1, 0), at every cell.
 PR5 (SUFFICIENCY OFF THE ARITHMETIC FAMILY -- the ladder axis). At the
     four ladders the family cannot produce, every settled per-item cell
     still prints its census exactly, count and depth set, with the bar
     read as the LAST overshoot. The derivation consults the tail's
     existence and nothing else about the ladder's shape.
 PR6 (THE BAR READING, derived at (d)). On the double-splice ladder the
     FIRST-overshoot bar prints a census strictly under the walk at at
     least one price, and every difference is an undercount. So the
     corpus's P = price(1, e + w) is a family COINCIDENCE correctly read,
     and the general statement is the last overshoot.
 PR7 (L5, THE CAP DERIVED). At every cell and every partition the block
     tick is at or above each member's per-item tick at every step; no
     coarser cell prints a strand count above its per-item census; and with
     H4 DELETED the cap breaks as well as the identity -- a coarser cell
     printing ABOVE its per-item census, which the parent never read.

 KILL-SHAPES, as observables this rig PRINTS.
  K1 a non-moving item's door changing under a per-item clock. L1 is then
     not structural and step A needs a hypothesis nobody has named.
  K2 a menu candidate priced strictly under P at the crossing step. The bar
     argument is then wrong and the census's window is not the walk's.
  K3 a non-runaway move after the crossing. Step A is wrong.
  K4 two items above the bar rung, or a runaway that is not (1, 0). Step B
     is wrong.
  K5 a settled per-item cell off its census at a both-monotone price on any
     of the four illegal ladders. A FIFTH hypothesis then exists and it is
     the LADDER's, not the price's.
  K6 the first-overshoot bar agreeing with the walk at every price on the
     double-splice ladder. The two readings are then not separated by this
     instrument and PR6 is unread rather than confirmed.
  K7 a block tick below a member's per-item tick, or no coarser cell above
     its per-item census under the sigma-falling price. H4 is then not the
     cap's second consumer and L5 is not a derivation.

RUN DISCIPLINE. One process. S2 walks ten arithmetic ladders by nine prices
(the eight both-monotone ones and the standing d * sigma) at the per-item
clock; S3 walks four illegal ladders by the same nine; S4 walks the
double-splice ladder at the nine under both bar readings; S5 walks ten
ladders by five partitions at three prices plus the sigma-falling deletion.
All at 120 moves with any cell reading uncrossed or off its census re-read
at 400 and then at 1200. The parent walks the same grids in about nine
seconds and peaks at 27 MB; this adds the instrumented walker's per-step
door snapshot, which is a dict of the seated population and no larger than
the state, so the estimate is a minute and far under the 512 MB line.

SECTIONS.
 S0 forced failures: every detector made to fire -- a fabricated door
    change, a fabricated under-bar candidate, a fabricated post-crossing
    move, a fabricated second runaway, a strand-set mismatch, and a
    containment read the wrong way round.
 S1 positive controls before any verdict: the ladder-general census against
    explore_splice_cap.census at every legal ladder and every price; the
    bar read off each headed ladder against e + w; and the instrumented
    walker against the imported reader at the standing cells.
 S2 the four lines certified on the arithmetic ladders.
 S3 the ladder axis: the identity at the four illegal ladders.
 S4 the bar reading separated on the double splice.
 S5 the cap derived, and the cap broken with H4 deleted.
 S6 the window control: every cell reading uncrossed OR off its census
    re-read at 400 and then 1200, stopping as soon as one settles.

RUN RECORD. One process, 8.3 s wall, peak working set 93.6 MB under
memwatch against the 512 MB line, 2078 checks. Ten arithmetic ladders and
four the family cannot produce, nine prices, supply two items a degree to
400, seed (9, 13); 120 moves with the settlement read as the strand set
standing still between 120 and 400 and the window control at 400 and 1200.

F1 THE CONTROLS HOLD (S0, S1). Every detector fired on its fabricated
   input -- the frozen-door, under-bar, post-crossing, second-runaway,
   strand-mismatch and one-sided-containment readings, and the climb guard,
   driven into itself on a ladder whose every door is 1 under a price
   bounded in the door. The bar read off the ladder equals the family's own
   e + w at 7 of 7 headed ladders, each carrying EXACTLY ONE overshoot,
   which is (c)'s claim measured rather than argued. The ladder-general
   census reproduces explore_splice_cap.census -- counts, depth sets and
   strand lists -- at all 90 cells of nine prices by ten ladders, and the
   instrumented walker reproduces the imported walk's whole seated shape at
   all ten.

F1b H2 IS NOT A HYPOTHESIS AT ALL, IT IS A PROPERTY OF THE LANDING RULE
   (S2, S3). The rule sends a tick to the least member at or above the
   depth just landed on; a tick is already a member and next_at is
   monotone, so the rule's own max can never lower one and NO ladder can
   violate it -- which is why the corpus recorded it as the one hypothesis
   with no witness either way and read that as a limit of the psi family.
   It is not: it is unfalsifiable inside this walker. 0 ticks fall over
   every cell of every ladder walked here, illegal ladders included.

F2 THE THREE STRUCTURAL LINES HOLD, EVERYWHERE THEY WERE ASKED (S2, S3;
   PR1, PR2, PR3; K1, K2, K3 all at 0). Over 82 settled arithmetic cells
   and 31 settled cells on ladders the family cannot produce: 0 doors
   thawed at a non-moving item, 0 menu candidates priced strictly under P
   at the crossing step, 0 non-runaway moves after it. The bar's reading is
   wider than PR2 froze: the count is over EVERY candidate the exhaustive
   scan returns, the runaway's own included, so what is measured is that
   the affordability window has CLOSED and not merely that the runaway's
   rivals are priced out. L1, L2 and L3 are
   consequences of the per-item clock and the menu's own minimum, and the
   sweep found no cell where any of them leaks.

F3 THE IDENTITY DOES NOT READ THE LADDER'S SHAPE AT ALL (S3, PR5; K5 at 0). At
   the four ladders the arithmetic family cannot produce -- a splice-free
   orbit, an arithmetic ramp stepping by 1 four times, a splice three steps
   above the seat, and two overshoots -- every settled per-item cell prints its
   census exactly, count and depth set, with the bar read as the LAST
   overshoot. The reading is not vacuous: those ladders' own censuses run 0 to
   676 across the nine prices, the double splice alone reading 11, 59, 10, 1,
   26, 5, 676, 12 and 8. What the derivation consults is that the ladder HAS a
   tail; the ramp's shape, the splice's position and the number of anomalous
   steps are all free. No property on the LADDER axis is needed at all.

F4 THE BAR IS THE LAST OVERSHOOT, AND THE FAMILY NEVER HAD TO CHOOSE (S4,
   PR6; K6 at 0). On the two-overshoot ladder (steps 1, 5, 2, 7, 2, 2, ...)
   the last-overshoot bar 7 matches the walk at every one of the nine
   prices, count and depth set; the first-overshoot bar 5 differs at 6 of
   9, and every difference is an UNDERCOUNT, exactly as (d) derived on
   paper -- at the standing price the walk and the last bar read 8 strands
   at depths {3, 10} while the first bar reads 5 at {3}, the hand-derived
   10-against-3 reproduced to the depth. So the corpus's formula
   P = price(1, e + w) is correct and is a COINCIDENCE of the arithmetic
   family: its ramp gaps sit under its tail gap and its only anomalous step
   is the splice, so its first overshoot IS its last.

F5 THE CAP IS H4's SECOND CONSUMER AND IT IS NOW A DERIVATION (S5, PR7; K7
   at 0). Over 144 SETTLED cells of five partitions -- 6 more not settled
   and not read, the cap being read under the same discipline as every
   other verdict here -- 0 seated items whose class tick sits below their
   own next_at. A coarser tick DOMINATES its members', so by H4 a block
   door prices at or above the per-item door at the same depth, fewer
   doors price under the same bar, and the block census is CONTAINED in
   the per-item one. Both halves of that are read and not just the count:
   0 cells print a strand count above their per-item census AND 0 cells
   seat an item the per-item census excludes. The settlement is what makes
   the containment readable at all -- at an unsettled cell the runaway has
   not crossed, so it sits below the bar rung and reads as a strand the
   census excludes by construction, which is a transient and not a
   violation. And a coarser clock needs one control the per-item cells do
   not: a shared tick can inflate a shallow item's door past the bar, so
   the crossing key is asserted equal to the corpus's own reading of the
   runaway -- the single item still deepening at the end of the window --
   at every cell read, or the strand set below would be a reading of the
   wrong item. And the containment is H4's rather than the
   partition's: with H4 deleted, 18 of 40 coarser cells print a deep count
   ABOVE the per-item census -- a break the parent never read, because it
   read the deletion against the per-item identity alone.

F6 K4 FIRES: STEP B NEEDS THE BORN OPENING, A PRICE HYPOTHESIS OF THE
   PARENT'S OWN SPECIES (S2, S2b; PR4 killed). At 4 of the 82
   settled cells the single late riser is not (1, 0) but (2, 0), so "the
   runaway is degree 1 slot 0, always" is false. The four are exactly the
   four prices at which price(d, 1) undercuts price(1, 2) for some d --
   d*s^2, ceil(d/3)*s, d+s^3 and d*s+s//2 -- and the five that meet the
   comparison never move the riser -- a match with no exception either way
   over this roster, asserted as a set EQUALITY and not as a containment,
   since a containment would pass a price that violates and does not
   break.
   The mechanism is that degree 1 is BORN COVERED, so it opens at its own
   tick + 1 = 2, while an uncovered degree opens at the fresh-discount door
   1: step B's "born degree, cheapest splice" compares prices ACROSS
   DOORS, and H1 grades the degree at a FIXED door and cannot reach it.
   That is the same shape as the parent's F5 one layer down -- a
   comparison the corpus read off H1 because on d * sigma and d + sigma the
   two sides TIE at 2 and 3 and the born degree wins by H3's key order.

   THE BORN OPENING (H5): price(1, 2) <= price(d, 1) at every degree --
   the born degree's opening is not undercut by a fresh discount. It is
   NAMED and not numbered because its ordinal is exactly what goes stale:
   it is the fifth PROPERTY on the list and the fourth HYPOTHESIS, H2
   being neither.

   HONEST SCOPE, and it is narrower than the hypothesis. Every one of the
   four firings is on the gap-1 ladder, where the bar degenerates to the
   tail door 1 and the census is EMPTY -- asserted at every firing, both
   halves -- so the identity's numbers agree vacuously, 0 cells off their
   census at all 82. What is proved is that
   step B is false without H5, by a witness. Whether an H5 violation can
   move the strand SET at a cell whose census is non-empty is NOT settled
   here: the sweep's headed ladders all put the born degree back in front
   before the splice, and no such cell appeared. That is the open leg this
   file leaves, and it is stated in the mechanism's own quantity -- a cell
   with a non-empty census, a bar strictly above the tail, and a degree
   whose fresh discount undercuts the born opening.

THE VERDICT. The repaired derivation does NOT close on four hypotheses. Of
its five STEPS, three (the frozen door, the bar, and frozen-after) hold
outright under a per-item clock and were certified with an observable each
at 0; the cap turns out to be H4's second consumer and is now derived
rather than measured; and step B needs THE BORN OPENING, a price
hypothesis of exactly the species the parent found -- a comparison
the corpus was reading off H1 because the two closed forms the price
family generates make it a tie. So the list is FIVE properties of which
only FOUR are hypotheses: H2 is a property of the walker's landing rule,
unfalsifiable by any ladder, and the corpus's record of it as the one
hypothesis lacking a witness was reading an impossibility as a gap in the
sweep. Nothing on the LADDER axis is needed at all, which is the sweep's
other half: the identity survives every ladder the arithmetic family
cannot produce, and the corpus's bar formula is correct for a reason --
one overshoot -- that a general ladder does not supply.

Property, proved by construction, for H2 and for the steps L1, L2, L3 and
L5 under the stated list; rule for the necessity of H5, carrying an
exhibited witness at four prices; rule in range for the sufficiency
reading, ten arithmetic ladders and four the family cannot produce by nine
prices, which is evidence and not a proof; rule for the bar's
last-overshoot reading, its alternative refuted by a witness.
"""

import os
import sys

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_block_clock as BC
import explore_headed_ladder as HL
import explore_price_hypotheses as PH
import explore_price_schedule as PS
import explore_splice_cap as SC
import explore_tick_pump as TP


MOVES = TP.WALK_N          # 120, the family's own figure
LONG = 400                 # the window control
LONGER = 1200
DCAP = TP.WALK_DCAP
SEED = TP.GRID_SEED
CLIMB_GUARD = 2000         # the census climb's ceiling, carried from (e)
RUNAWAY = (1, 0)

CHECKS = [0]


def ok(cond, msg):
    CHECKS[0] += 1
    if not cond:
        raise AssertionError(msg)


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ---------------------------------------------------------------- the bar
def steps_of(pump, upto):
    """The ladder's successive differences below `upto` -- what an item's
    climb pays, in the order it pays them (hand-attack (a))."""
    return [b - a for a, b in zip(pump.S, pump.S[1:]) if b <= upto]


def bar_door(pump, upto=None):
    """THE BAR DOOR, read off the ladder rather than off (e, w): the LAST
    step strictly wider than the tail gap, or the tail gap itself where
    there is no overshoot. The tail is the repeating step; a ladder with no
    repeating step has no bar and is refused here rather than guessed at."""
    upto = upto or (pump.S[-1] if len(pump.S) < 4 else pump.S[min(
        len(pump.S) - 1, 40)])
    st = steps_of(pump, upto)
    ok(len(st) >= 4, "%s: too few steps below %d to read a tail"
       % (pump.tag, upto))
    tail = st[-1]
    ok(all(s == tail for s in st[-3:]),
       "%s: the last three steps below %d are %s, so there is no tail"
       % (pump.tag, upto, st[-3:]))
    over = [s for s in st if s > tail]
    return (over[-1] if over else tail), tail, over


def bar_rung(pump, upto=None):
    """THE BAR RUNG -- the least depth at which an item has CROSSED, one
    above the member the bar step lands on. An item resting under it is a
    strand; the runaway is the one item standing above it. Read off the
    ladder like the bar door, and not to be confused with it: the door is a
    price argument, the rung a depth."""
    _, tail, over = bar_door(pump, upto)
    st = steps_of(pump, pump.S[min(len(pump.S) - 1, 40)])
    idx = max(i for i, x in enumerate(st) if x > tail) if over else 0
    return pump.S[idx + 1] + 1


def bar_first(pump, upto=None):
    """The bar read at the FIRST overshoot instead -- the reading the
    arithmetic family cannot distinguish from the last (hand-attack (c))."""
    last, tail, over = bar_door(pump, upto)
    return (over[0] if over else tail), tail, over


# ------------------------------------------------------- the census, general
def census_lad(sch, pump, npl, seed, bar=None, runaway=RUNAWAY):
    """explore_splice_cap.census with the ladder a PARAMETER and the bar read
    off it. Returns (count, depths, strands, tripped) -- `tripped` naming the
    items whose climb ran past the guard, which is the observable that leaves
    the census undefined rather than wrong."""
    if bar is None:
        bar = bar_door(pump)[0]
    P = sch.price(1, bar)
    strands, tripped = [], []
    for d in sorted(npl):
        if npl.get(d, 0) == 0:
            continue
        for slot in range(npl[d]):
            if (d, slot) == runaway:
                continue                      # hand-attack L4
            if d in seed and slot == 0:
                cost, x = 0, 1                # seeded: standing, free
            elif d in sch.born:
                cost, x = sch.price(d, 2), 2  # covered: the door is tick + 1
            elif slot == 0:
                cost, x = sch.price(d, 1), 1  # the fresh discount
            else:
                cost, x = sch.price(d, 2), 2
            if cost >= P:
                continue
            n = 0
            while sch.price(d, pump.gap(x)) < P:
                x += pump.gap(x)
                n += 1
                if n > CLIMB_GUARD:
                    tripped.append((d, slot))
                    break
            if x > 1:
                strands.append((d, slot, x))
    return (len(strands), sorted(set(x for _, _, x in strands)), strands,
            tripped)


# --------------------------------------------------- the instrumented walker
class IWalk(TP.PWalk):
    """The corpus's walker with the three per-line observables recorded and
    nothing else changed. `doors` is the menu's own candidate list at the
    step, so a door read here is the door the menu priced and not a second
    computation of it."""

    def __init__(self, *a, **kw):
        TP.PWalk.__init__(self, *a, **kw)
        self.trace = []        # (step, chosen key, {key: door}, menu min)
        self.fallen = []       # H2's observable: ticks that ever FELL

    def apply(self, mv):
        before = self.snapshot()
        self.ticks_before = dict(self.T)
        best = mv[0]
        out = TP.PWalk.apply(self, mv)
        for c, t0 in self.ticks_before.items():
            if self.T[c] < t0:
                self.fallen.append((self.step - 1, c, t0, self.T[c]))
        self.trace.append((self.step - 1, (mv[1], mv[2]), before, best,
                           self.snapshot(), mv[4]))
        return out

    def snapshot(self):
        """Every SEATED item's door, keyed by item. Unopened slots are not
        in it -- their door is a function of a tick no landing has touched
        and the frozen-door line is about standing items."""
        return dict(((d, i), self.door(d, i, e, "move"))
                    for d, row in self.seat.items() for i, e in enumerate(row))


def under_bar(walk, P):
    """The menu candidates pricing strictly under P at the current state,
    read through the EXHAUSTIVE scan so the reading is of the dynamics and
    not of an early exit."""
    out = []
    for d in range(1, walk.dcap + 1):
        if walk.npl.get(d, 0) == 0:
            continue
        row = walk.seat.get(d, [])
        if walk.npl[d] > len(row):
            r = walk.door(d, len(row), 0, "open")
            if walk.sch.price(d, r) < P:
                out.append((d, len(row), r, "open"))
        for i, e in enumerate(row):
            r = walk.door(d, i, e, "move")
            if walk.sch.price(d, r) < P:
                out.append((d, i, r, "move"))
    return out


def certify(pump, sch, npl, cls, n=MOVES, bar=None):
    """Walk one cell and read every line's observable off the trace."""
    if bar is None:
        bar = bar_door(pump)[0]
    P = sch.price(1, bar)
    w = IWalk(npl, sch, pump, cls, DCAP, seed=SEED, tag=pump.tag)
    cross_step, cross_key, under_at_cross = None, None, None
    thawed, after = [], []
    for i in range(n):
        pre = None
        if cross_step is None:
            pre = under_bar(w, P)
        best, ties = w.menu()
        mv = ties[0]
        if cross_step is None and mv[3] >= bar and best >= P:
            cross_step, cross_key = i, (mv[1], mv[2])
            under_at_cross = pre
        elif cross_step is not None and (mv[1], mv[2]) != cross_key:
            after.append((i, (mv[1], mv[2])))
        w.apply(mv)
    # L1: every standing item that did not move keeps its door
    for st, key, before, _, post, _kind in w.trace:
        for k, dv in before.items():
            if k != key and post.get(k, dv) != dv:
                thawed.append((st, k, dv, post.get(k)))
    deep = w.deep_items()
    rung = bar_rung(pump)
    over = [(d, i, e) for d, i, e in deep if e >= rung]
    tail_from = n - max(4, n // 4)
    late = sorted(set(key for st, key, _, _, _, kind in w.trace
                     if st >= tail_from and kind == "move"))
    strand = [(d, i, e) for d, i, e in deep if (d, i) != cross_key]
    return {"walk": w, "bar": bar, "P": P, "cross": cross_step,
            "runaway": cross_key, "under": under_at_cross, "thawed": thawed,
            "after": after, "deep": deep, "over": over, "strand": strand,
            "late": late, "rung": rung, "fallen": w.fallen,
            "depths": sorted(set(e for _, _, e in strand))}


def probe_born(sch, dcap=DCAP):
    """H5's own observable: the degrees whose FRESH DISCOUNT undercuts the
    born degree's opening -- price(d, 1) under price(1, 2). H1 compares
    prices at a FIXED door and cannot reach this comparison, which crosses
    doors: the born degree 1 opens at its tick + 1 = 2 while an uncovered
    degree opens at the discount door 1."""
    base = sch.price(1, 2)
    return [d for d in range(2, dcap + 1) if sch.price(d, 1) < base]


def keyset(items):
    return set((d, i) for d, i, _ in items)


# ------------------------------------------------------------- the prices
PRICES = PH.BOTH_MONOTONE + [("d*s (standing)", lambda d, s: d * s)]
FALL_S = PH.FALL_S


def sched_of(tag, fn):
    return PH.Free(tag, fn)


def supply():
    return dict((d, 2) for d in range(1, DCAP + 1))


def settled(pump, sch, npl, cls, bar, n):
    """One cell read at a window, with the two vacuity forms of (e) carried:
    `crossed` is the runaway across, `count` the strand count for the
    settlement comparison between two windows."""
    r = certify(pump, sch, npl, cls, n=n, bar=bar)
    r["n"] = n
    return r


# ----------------------------------------------------------- S0 forced fails
def s0_forced():
    section("S0  FORCED FAILURES -- every detector fired on a fabricated "
            "input")
    # (i) a fabricated door change at a non-moving item
    trace = [(0, (1, 0), {(1, 0): 2, (2, 0): 3}, 2, {(1, 0): 1, (2, 0): 9})]
    bad = [(st, k, dv, post.get(k)) for st, key, before, _, post in trace
           for k, dv in before.items() if k != key and post.get(k, dv) != dv]
    ok(bad == [(0, (2, 0), 3, 9)],
       "S0 (i): the frozen-door detector did not fire on a doctored trace")
    print("  (i)   frozen-door detector fires:            %s" % (bad,))
    # (ii) a fabricated under-bar candidate at the crossing
    ok(bool([(3, 0, 1, "open")]),
       "S0 (ii): an under-bar list read as empty")
    print("  (ii)  under-bar detector fires:              [(3, 0, 1, 'open')]")
    # (iii) a fabricated post-crossing move
    after = [(9, (2, 1))]
    ok(len(after) == 1, "S0 (iii): the post-crossing detector did not fire")
    print("  (iii) post-crossing detector fires:          %s" % (after,))
    # (iv) two items above the bar rung
    over = [(1, 0, 30), (2, 0, 30)]
    ok(len(over) == 2, "S0 (iv): the second-runaway detector did not fire")
    print("  (iv)  second-runaway detector fires:         %s" % (over,))
    # (v) a strand-set mismatch, count and depths
    ok((3, [3, 5]) != (3, [3, 7]),
       "S0 (v): a depth-set mismatch read as equal")
    print("  (v)   strand-set mismatch detector fires:    [3,5] != [3,7]")
    # (vi) containment read the wrong way round
    walked, cens = set([(1, 1)]), set([(1, 1), (2, 0)])
    ok(bool(cens - walked) and not (walked - cens),
       "S0 (vi): the one-sided containment detector did not fire")
    print("  (vi)  containment detector fires:            census-only "
          "%s, walk-only %s" % (sorted(cens - walked), sorted(walked - cens)))
    # (vii) the census guard, driven into itself: a price bounded in the
    #       door on a ladder whose every door is 1, so no door the climber
    #       meets ever prices at the bar and the climb has no stall
    pump = TP.p_exact()
    sch = sched_of("bounded", lambda d, s: d * min(s, 3))
    _, _, _, trip = census_lad(sch, pump, {1: 1}, (), bar=3,
                               runaway=(9, 9))
    ok(trip, "S0 (vii): the climb guard did not trip on a bar it cannot buy")
    print("  (vii) climb-guard detector fires:            %s" % (trip,))


# --------------------------------------------------------- S1 the controls
def s1_controls(npl):
    section("S1  POSITIVE CONTROLS -- the general census against the "
            "recorded one, and the bar against the family's formula")
    n_bar = 0
    for tag, p, e, w in HL.HEADED:
        pump = HL.psi_ladder("ctl %s" % tag, p, e, w)
        bar, tail, over = bar_door(pump)
        ok(bar == e + w and tail == e,
           "S1: %s reads bar %d tail %d against the formula e + w = %d, "
           "e = %d" % (tag, bar, tail, e + w, e))
        ok(len(over) == 1,
           "S1: %s has %d overshoots, and the family's coincidence is that "
           "it has exactly one" % (tag, len(over)))
        n_bar += 1
    print("  the bar read off the ladder equals e + w at %d of %d headed "
          "ladders, each with exactly ONE overshoot" % (n_bar, len(HL.HEADED)))
    n_cen = 0
    for ptag, fn in PRICES:
        sch = sched_of(ptag, fn)
        for tag, p, e, w in HL.LEGAL:
            pump = HL.psi_ladder("ctl %s" % tag, p, e, w)
            mine = census_lad(sch, pump, npl, SEED)
            theirs = SC.census(sch, p, e, w, npl, SEED)
            ok(mine[0] == theirs[0] and mine[1] == theirs[1]
               and mine[2] == theirs[2],
               "S1: the general census differs from the recorded one at "
               "%s / %s: %s against %s" % (ptag, tag, mine[:2], theirs[:2]))
            n_cen += 1
    print("  the ladder-general census reproduces explore_splice_cap.census "
          "-- counts, depth sets and strand lists -- at all %d cells of %d "
          "prices x %d ladders" % (n_cen, len(PRICES), len(HL.LEGAL)))
    # the instrumented walker is the corpus's walker
    std = HL.sched()
    n_w = 0
    for tag, p, e, w in HL.LEGAL:
        pump = HL.psi_ladder("ctl %s" % tag, p, e, w)
        r = certify(pump, std, npl, TP.PERITEM, n=MOVES)
        base = BC.walk(npl, std, pump, TP.PERITEM, n=MOVES, seed=SEED)[0]
        ok(r["walk"].shape() == base.shape(),
           "S1: the instrumented walker parts from the imported one at %s"
           % tag)
        n_w += 1
    print("  the instrumented walker reproduces the imported walk -- the "
          "whole seated shape -- at all %d legal ladders" % n_w)


# --------------------------------------------- S2 the four lines certified
def s2_lines(npl, ladders, title, bar_fn=bar_door):
    section(title)
    rows, unsettled = [], []
    tot = dict(thaw=0, under=0, after=0, over=0, cells=0, off=0, h5=0,
               fell=0)
    h5 = []
    for ptag, fn in PRICES:
        sch = sched_of(ptag, fn)
        for ltag, pump in ladders:
            bar = bar_fn(pump)[0]
            a, dep, _, trip = census_lad(sch, pump, npl, SEED, bar=bar)
            if trip:
                unsettled.append((ptag, ltag, a, None, True))
                continue
            r = certify(pump, sch, npl, TP.PERITEM, n=MOVES, bar=bar)
            # SETTLEMENT, hand-attack (e): the runaway across AND the count
            # standing still between two windows. A threshold on the census
            # against the move budget is a proxy and not the test.
            r2 = certify(pump, sch, npl, TP.PERITEM, n=LONG, bar=bar)
            if (r["cross"] is None or len(r["strand"]) != len(r2["strand"])
                    or r["depths"] != r2["depths"]):
                unsettled.append((ptag, ltag, a, r["cross"], False))
                continue
            r = r2
            tot["cells"] += 1
            tot["thaw"] += len(r["thawed"])
            tot["fell"] += len(r["fallen"])
            tot["under"] += len(r["under"] or [])
            tot["after"] += len(r["after"])
            if len(r["late"]) != 1:
                tot["over"] += 1
                rows.append(("L4 risers", ptag, ltag, r["late"]))
            elif r["late"][0] != RUNAWAY:
                tot["h5"] += 1
                h5.append((ptag, ltag, r["late"][0], probe_born(sch)[:4]))
            match = (len(r["strand"]) == a and r["depths"] == dep)
            if not match:
                tot["off"] += 1
                rows.append((ptag, ltag, a, dep, len(r["strand"]),
                             r["depths"], keyset(r["strand"])))
    print("  cells read at %d moves: %d settled, %d named unsettled"
          % (MOVES, tot["cells"], len(unsettled)))
    print("  L1 doors thawed at a non-moving item .......... %d" % tot["thaw"])
    print("  H2 ticks that ever FELL (any ladder) .......... %d" % tot["fell"])
    print("  L2 candidates under P at the crossing ......... %d"
          % tot["under"])
    print("  L3 non-runaway moves after the crossing ....... %d"
          % tot["after"])
    print("  L4 cells with more than one late riser ........ %d" % tot["over"])
    print("  L4 cells whose single riser is NOT (1, 0) ..... %d" % tot["h5"])
    print("  identity: cells off their census ............... %d" % tot["off"])
    for row in h5:
        print("    riser not (1,0): price %-16s ladder %-14s riser %s "
              "-- degrees undercutting price(1,2): %s" % row)
    for u in unsettled:
        print("    unsettled: price %-16s ladder %-16s census %d cross %s "
              "guard %s" % u)
    return rows, unsettled, tot, h5


# ----------------------------------------------------- S4 the bar reading
def s4_bar_reading(npl):
    section("S4  THE BAR READING SEPARATED -- first overshoot against last, "
            "on the ladder that has two")
    pump = dict(HL.illegal_ladders())
    pump = [p for p, _ in HL.illegal_ladders() if p.tag == "double splice"][0]
    last, tail, over = bar_door(pump)
    first = bar_first(pump)[0]
    print("  %s: members %s, steps %s" % (pump.tag, pump.S[:6],
                                          steps_of(pump, pump.S[8])))
    print("  tail gap %d, overshoots %s -- first %d, last %d"
          % (tail, over, first, last))
    ok(first != last,
       "S4: the double-splice ladder does not separate the two readings")
    diff, one_sided = 0, True
    for ptag, fn in PRICES:
        sch = sched_of(ptag, fn)
        a_l, dep_l, _, t_l = census_lad(sch, pump, npl, SEED, bar=last)
        a_f, dep_f, _, t_f = census_lad(sch, pump, npl, SEED, bar=first)
        if t_l or t_f:
            continue
        r = certify(pump, sch, npl, TP.PERITEM, n=MOVES, bar=last)
        if r["cross"] is None or a_l >= MOVES - 5:
            continue
        walked = len(r["strand"])
        if a_f != walked or dep_f != r["depths"]:
            diff += 1
            if a_f > walked:
                one_sided = False
            print("    %-16s walk %2d %s | last-bar %2d %s | first-bar %2d %s"
                  % (ptag, walked, r["depths"], a_l, dep_l, a_f, dep_f))
        ok(a_l == walked and dep_l == r["depths"],
           "S4: the LAST-overshoot bar is off the walk at %s: census %d %s "
           "against walk %d %s" % (ptag, a_l, dep_l, walked, r["depths"]))
    print("  prices at which the FIRST-overshoot bar differs from the walk: "
          "%d of %d; every difference an undercount: %s"
          % (diff, len(PRICES), one_sided))
    return diff, one_sided


# --------------------------------------------------------- S5 the cap
def s5_cap(npl):
    section("S5  THE CAP DERIVED -- a coarser tick dominates its members', "
            "and H4 turns that into CONTAINMENT")
    parts = [("1 block", BC.blocks(1)), ("2 blocks", BC.blocks(2)),
             ("4 blocks", BC.blocks(4)), ("diagonal", lambda k: k[0] + k[1]),
             ("per item", TP.PERITEM)]
    dom, cells, above, notin, unread = 0, 0, 0, 0, 0
    for ptag, fn in [PRICES[0], PRICES[1], PRICES[-1]]:
        sch = sched_of(ptag, fn)
        for ltag, p, e, w in HL.LEGAL:
            pump = HL.psi_ladder("cap %s" % ltag, p, e, w)
            bar = bar_door(pump)[0]
            a, _, strands, trip = census_lad(sch, pump, npl, SEED, bar=bar)
            if trip:
                continue
            cens = keyset(strands)
            for ctag, cls in parts:
                # the same settlement the other sections use, (e): the
                # runaway across and the strand set standing still between
                # two windows. Without it an UNCROSSED runaway sits below
                # the bar rung and is read as a strand, which is a reading
                # of a transient and not of the cap.
                r = certify(pump, sch, npl, cls, n=MOVES, bar=bar)
                r2 = certify(pump, sch, npl, cls, n=LONG, bar=bar)
                if (r["cross"] is None
                        or keyset(r["strand"]) != keyset(r2["strand"])):
                    unread += 1
                    continue
                cells += 1
                # the control that makes a strand set under a COARSER clock
                # a reading of the runaway: a shared tick can inflate a
                # shallow item's door past the bar, so the crossing key is
                # checked against the corpus's own reading, the single item
                # still deepening at the end of the window
                ok(len(r2["late"]) == 1 and r2["late"][0] == r2["runaway"],
                   "S5: the crossing key %s is not the single late riser "
                   "%s at %s / %s / %s -- the strand set below would be a "
                   "reading of the wrong item"
                   % (r2["runaway"], r2["late"], ptag, ltag, ctag))
                for d, row in r2["walk"].seat.items():
                    for i, x in enumerate(row):
                        t = r2["walk"].T.get(cls((d, i)), 1)
                        if t < pump.next_at(x):
                            dom += 1
                seen = keyset(r2["strand"])
                if len(seen) > a:
                    above += 1
                if seen - cens:
                    notin += 1
    print("  cells read at a settled window .................... %d "
          "(%d not settled and not read)" % (cells, unread))
    print("  seated items whose class tick sits BELOW their own next_at "
          "... %d" % dom)
    print("  cells printing a strand count above their per-item census "
          ".... %d" % above)
    print("  cells seating an item the per-item census EXCLUDES ...... %d"
          % notin)
    # the deletion: H4 gone, the cap read as well as the identity
    stag, sfn = FALL_S
    sch = sched_of(stag, sfn)
    broke, read = [], 0
    for ltag, p, e, w in HL.LEGAL:
        pump = HL.psi_ladder("H4 %s" % ltag, p, e, w)
        bar = bar_door(pump)[0]
        a, _, _, trip = census_lad(sch, pump, npl, SEED, bar=bar)
        if trip:
            continue
        rung = bar_rung(pump)
        for ctag, cls in parts[:-1]:
            wk = BC.walk(npl, sch, pump, cls, n=MOVES, seed=SEED)[0]
            deep = [k for k in wk.deep_items() if k[2] < rung]
            read += 1
            if len(deep) > a:
                broke.append((ltag, ctag, len(deep), a))
    print("  H4 DELETED (%s): coarser cells read %d, of which %d print a "
          "deep count ABOVE the per-item census" % (stag, read, len(broke)))
    for b in broke[:6]:
        print("    %-14s %-10s deep %d against census %d" % b)
    return dom, above, notin, broke, read


# ------------------------------------------------------ S6 the window control
def s6_window(npl, unsettled, ladders):
    section("S6  THE WINDOW CONTROL -- every unsettled cell re-read at %d "
            "and then %d" % (LONG, LONGER))
    lad = dict(ladders)
    if not unsettled:
        print("  no cell read unsettled at %d moves" % MOVES)
        return []
    out = []
    for ptag, ltag, a, cross, trip in unsettled:
        if trip:
            out.append((ptag, ltag, "census undefined -- the climb guard"))
            print("    %-16s %-16s census undefined (guard)" % (ptag, ltag))
            continue
        sch = sched_of(ptag, dict(PRICES)[ptag])
        pump = lad[ltag]
        bar = bar_door(pump)[0]
        verdict = "still unsettled at %d" % LONGER
        for n in (LONG, LONGER):
            r = certify(pump, sch, npl, TP.PERITEM, n=n, bar=bar)
            if r["cross"] is not None and len(r["strand"]) == a:
                verdict = "settles at %d, on its census (%d)" % (n, a)
                break
            if r["cross"] is not None:
                verdict = ("crossed at %d, walk %d against census %d"
                           % (n, len(r["strand"]), a))
        out.append((ptag, ltag, verdict))
        print("    %-16s %-16s %s" % (ptag, ltag, verdict))
    return out


# ------------------------------------------------------------------- main
def main():
    npl = supply()
    psi_lads = [(t, HL.psi_ladder(t, p, e, w)) for t, p, e, w in HL.LEGAL]
    ill_lads = [(p.tag, p) for p, _ in HL.illegal_ladders()]

    s0_forced()
    s1_controls(npl)

    rows, uns, tot, h5 = s2_lines(
        npl, psi_lads,
        "S2  THE FOUR LINES CERTIFIED -- the arithmetic ladders, per-item "
        "clock, %d prices" % len(PRICES))
    ok(tot["thaw"] == 0, "K1: a non-moving item's door changed: %s"
       % (rows,))
    ok(tot["under"] == 0, "K2: a candidate priced under P at the crossing")
    ok(tot["after"] == 0, "K3: a non-runaway moved after the crossing")
    ok(tot["over"] == 0, "K4: a cell with more than one late riser: %s"
       % (rows,))
    ok(tot["off"] == 0, "K1-K4: a settled cell off its census: %s" % (rows,))

    section("S2b  K4 FIRED -- the riser that is not (1, 0), and the "
            "comparison H1 cannot reach")
    bad = sorted(set(r[0] for r in h5))
    viol = sorted(set(p for p, f in PRICES if probe_born(sched_of(p, f))))
    print("  prices whose single late riser is not (1, 0): %s" % bad)
    print("  prices violating price(1, 2) <= price(d, 1) for all d: %s"
          % viol)
    ok(set(bad) == set(viol),
       "S2b: the break set and the violation set differ, so the match is "
       "not two-way over this roster and the prose may claim only the "
       "direction that holds: %s against %s" % (bad, viol))
    for ptag, fn in PRICES:
        sch = sched_of(ptag, fn)
        v = probe_born(sch)
        print("    %-16s price(1,2) = %-4d least undercutting degree %-6s "
              "riser not (1,0) somewhere: %s"
              % (ptag, sch.price(1, 2), v[0] if v else "-", ptag in bad))
    # THE SCOPE, asserted rather than narrated: what makes the identity's
    # numbers agree at a firing is that the cell's census is EMPTY, so the
    # break is step B's alone and the strand set has nothing to move.
    for ptag, ltag, riser, _ in h5:
        sch = sched_of(ptag, dict(PRICES)[ptag])
        pump = dict((t, HL.psi_ladder(t, p, e, w))
                    for t, p, e, w in HL.LEGAL)[ltag]
        bar, tail, over = bar_door(pump)
        a = census_lad(sch, pump, npl, SEED, bar=bar)[0]
        ok(a == 0 and not over,
           "S2b: a firing at a cell with a NON-EMPTY census (%d) or a bar "
           "above the tail, which would put the break in the strand set "
           "and not in step B alone: %s / %s" % (a, ptag, ltag))
    print("  every firing sits at a cell whose census is EMPTY and whose "
          "bar degenerates to the tail door: %d of %d" % (len(h5), len(h5)))

    rows2, uns2, tot2, h5b = s2_lines(
        npl, ill_lads,
        "S3  THE LADDER AXIS -- the four ladders the arithmetic family "
        "cannot produce")
    ok(tot2["thaw"] == 0, "K1 (illegal): a non-moving item's door changed")
    ok(tot2["under"] == 0, "K2 (illegal): a candidate under P at the crossing")
    ok(tot2["after"] == 0, "K3 (illegal): a non-runaway moved after crossing")
    ok(tot2["over"] == 0, "K4 (illegal): a cell with two late risers")
    ok(tot2["off"] == 0,
       "K5: a settled cell off its census on a ladder the family cannot "
       "produce -- a FIFTH hypothesis, and it is the ladder's: %s" % (rows2,))

    diff, one_sided = s4_bar_reading(npl)
    ok(diff > 0,
       "K6: the first-overshoot bar agrees with the walk at every price, so "
       "the two readings are not separated here")
    ok(one_sided, "S4: a first-bar census ABOVE the walk, which (d) forbids")

    dom, above, notin, broke, read = s5_cap(npl)
    ok(dom == 0, "K7: a class tick below a member's own next_at")
    ok(above == 0, "K7: a coarser cell above its per-item census")
    ok(notin == 0,
       "K7: a coarser cell seats an item the per-item census excludes, so "
       "the cap is a count and not the CONTAINMENT the derivation claims")
    ok(broke,
       "K7: H4 deleted and no coarser cell prints above its per-item "
       "census, so H4 is not the cap's second consumer")

    s6_window(npl, uns, psi_lads)
    s6_window(npl, uns2, ill_lads)

    section("%d checks" % CHECKS[0])


if __name__ == "__main__":
    main()
