"""explore_price_hypotheses.py -- WHAT DOES THE WALK-CENSUS IDENTITY
ACTUALLY CONSULT? The hypothesis audit under the strand law.

THE QUESTION. The admission census reproduces the walked strand set --
count and resting depths -- at three prices now (explore_splice_cap.py at
f = d * sigma, explore_rung_schedule.py at f = d^2 * sigma and at
f = d + sigma). Its derivation is stated, not fitted: explore_splice_cap.py
steps A-C claim to consult exactly THREE properties of the schedule and the
ladder --

  (H1) the price is nondecreasing in the DEGREE at a fixed door, which is
       what makes the runaway degree 1 slot 0 and what makes the menu's
       scan economy sound;
  (H2) doors are nondecreasing in time, which is the ladder's monotonicity
       and not the price's;
  (H3) a tie at the bar P loses to the splice, the splice sitting at
       degree 1 and slot 0, the lowest key in the menu's sorted tie list.

-- and nothing else. If that list is COMPLETE the identity is a theorem of
every schedule meeting it, and the three reproductions are instances rather
than evidence. This file does not run a fourth price to add a fourth
instance. It tests the LIST: sufficiency, by sweeping prices arithmetic
does not supply and that no closed form in the family generates, and
NECESSITY, by deleting one hypothesis at a time and reading what breaks.

WHY THE LIST IS THE SUSPECT. It is stated over a price of TWO arguments and
grades only ONE of them. The price is f(d, sigma): a degree and a door. H1
grades the degree. Nothing in the list grades sigma -- and step A's load-
bearing sentence, "nothing priced in (B, P) is ever created again", is a
claim about what happens to a STANDING item's price as its door grows. A
door grows with the tick (H2 gives that), but a growing door only costs
MORE if the price says so. So H2 is stated about the ladder and used about
the price, which is one hypothesis doing two jobs for two different
consumers. The candidate finding is a fourth hypothesis the corpus has been
using without naming it.

THE INSTRUMENT, all of it imported and already price-agnostic: the census
from explore_splice_cap, the walker and its clocks from explore_tick_pump,
the partitions and the cell reader from explore_block_clock and
explore_headed_block, the psi ladders and the ten-ladder roster from
explore_headed_ladder. Nothing in that chain reads a schedule except
through sch.price(d, sigma), sch.born, sch.m and sch.b -- which is what
makes an arbitrary price a subclass rather than a rewrite, and what makes
this a sweep rather than a build.

THE HAND-ATTACK, on paper before any engine code.

 (a) THE INDEX CONVENTION, re-derived from the engine before the freeze.
     psi(2, 4, w=2) has members {1, 2, 4, 10, 14, 18, ...}: ramp rungs 1,
     2, 4 with seat p^t = 4, splice at 10, tail gap 4. A door at depth e is
     gap(e) = next_at(e) + 1 - e, so a landing sits one above a member.
     The census bar is P = price(1, e + w), the runaway's splice price.
 (b) THE STANDING MARGIN, hand-derived at (p, e, w) = (2, 4, 2), seed
     (9, 13), two items a degree, f = d * sigma, so that the print is
     checked against paper. P = 6. Degree 1 is born, so slot 1 enters at
     price(1, 2) = 2 and climbs 2 -> 3 -> 5, stalling at 5 (the exit door
     from 5 is 6, priced 6, not under P). Degree 2 slot 0 takes the fresh
     discount at price 2 and climbs to 5; slot 1 enters at 4 and climbs to
     5. Degrees 3, 4, 5 admit slot 0 only (entries 3, 4, 5 < 6) and each
     stalls at 3, the exit door from 3 being 2 and pricing 6, 8, 10.
     Degree 6 admits nothing. The seeded 9 and 13 cost 0 and sit at depth
     1, which is not a strand. A = 6, depths {3, 5} -- the recorded value.
 (c) THE SIGMA MARGIN, the same cell at f = d * max(1, 10 - sigma), which
     is nondecreasing in d and FALLING in sigma. P = price(1, 6) = 4.
     Every fresh entry costs 9d >= 9, the born degree-1 slot costs
     price(1, 2) = 8, and the seeded items' climbs price 81 and 117 -- so
     no item at all prices strictly under 4 and the census reads A = 0
     with an empty depth set. The walk cannot agree with that unless it
     seats nothing above depth 1: a standing item's door grows, its price
     FALLS toward d, and every degree eventually prices under a bar the
     runaway's own recurrence keeps at 4. The predicted break is therefore
     ONE-SIDED -- the walk seats what the census excluded, never the
     reverse -- because the step that fails is "priced out forever" and
     the step that survives is "priced in gets taken".
 (d) THE STATISTIC'S ALGEBRA, where the census can blow up rather than
     merely be wrong -- and where the first draft of this slate was WRONG
     and its own forced-failure section refuted it on paper before any
     verdict ran. The census's climb is
     `while price(d, gap(x)) < P: x += gap(x)`, which terminates only
     because some door it meets prices at or above P. The draft predicted
     that a price BOUNDED in sigma leaves that loop running, the bound
     capping the climb's cost below a bar it never reaches. It does not,
     and the reason is the ladder's own shape rather than the price's:

       THE TERMINATION LEMMA. Under H1 alone, every census climb stalls,
       and it takes two branches because the bar P = price(1, e + w) sits
       differently in each. Only the TAIL has a door that repeats for
       ever (the constant gap e); everything else is a finite ramp.
       HEADED (w > 0): an item climbing rests one above a ramp rung, and
       the deepest of those is one above the seat p^t, whose exit door is
       exactly (p^t + e + w) + 1 - (p^t + 1) = e + w -- the splice door.
       Its price is price(d, e + w) >= price(1, e + w) = P by H1, so it
       stalls there and never reaches the tail; and it must pass that
       rung, the ramp rungs being the only members below the splice.
       SPLICE-FREE (w = 0): there is no barrier and the item does reach
       the tail, but the bar has moved with it -- P = price(1, e), and
       the tail's repeating door prices price(d, e) >= price(1, e) = P by
       H1, so it stalls at the first tail door instead. Either way the
       one door that could repeat for ever is priced at or above the bar,
       and H1 is the whole of what is consulted.

     So the bar P is not an arbitrary constant the price might undercut:
     it is the price of the one door every climber must buy, at the
     cheapest degree there is. Termination is a THIRD consumer of H1 --
     beside the runaway's identity and the scan's early exit -- and the
     door side is not implicated in it at all. What the guard in this
     file's census copy therefore observes is H1's deletion and nothing
     else, and a price bounded in the door becomes a POSITIVE prediction
     rather than a break.
 (e) THE VACUITY HAZARD is the parent's, and it has a SECOND form here
     that the parent never met. A cell whose runaway has not yet crossed
     its splice reads a strand set that is still a transient, so every
     verdict is read only at CROSSED cells and the uncrossed ones are
     re-read at the long window rather than dropped silently. But
     crossing is not settling: these prices admit sets far larger than
     the family's own, and a walk of n moves cannot seat more than n
     items however early its runaway crossed. So a cell whose census
     approaches or exceeds the move budget is UNREADABLE at that budget
     -- neither agreement nor a break -- and the settlement test is the
     count standing still between two windows with the runaway across.
     Read the other way round, the cell would print a walk below its
     census and look exactly like the kill this file is hunting. And a
     deletion sweep can break the identity for
     the WRONG reason: with H1 deleted the menu's scan economy is unsound
     on its own terms, so every deletion cell is walked with an
     EXHAUSTIVE scan, and the exhaustive scan's agreement with the
     economy scan wherever H1 holds is what makes that substitution
     free.

THE SLATE, frozen before the engine.

 PR1 (SUFFICIENCY, the claim under test). At every price nondecreasing in
     d and nondecreasing AND unbounded in sigma, the per-item cell's
     walked strand count and depth set equal the census's, at every
     SETTLED cell of all ten ladders in the sense of (e) -- eight prices
     no closed form in the family generates, including two with flat runs
     in d and one growing sublinearly in both arguments.
 PR2 (THE CAP, carried from the parent). No coarser partition prints a
     count above its per-item census at any of those prices.
 PR3 (THE SCAN'S SEPARATE JOB). Wherever H1 holds, the exhaustive scan
     reproduces the economy scan cell for cell -- so H1's two consumers,
     the runaway's identity and the scan's early exit, are separable and
     only the first is the census's.
 PR4 (H1 DELETED -- price falling in d). Three failures at once, by (d):
     the walked riser is not degree 1 slot 0; the census, which fixes that
     item as the runaway and reads its splice as the bar, misreads the
     cell; and the census's own climb runs past the splice into the tail
     and trips the guard.
 PR5 (H-SIGMA DELETED, falling -- the UNNAMED hypothesis, derived at (c)).
     The walked deep set strictly CONTAINS the census's at at least one
     crossed cell, and containment is one-sided at every cell.
 PR6 (H-SIGMA BOUNDED -- the corrected prediction, derived at (d)). A
     price nondecreasing in both arguments but BOUNDED in the door meets
     the identity at every crossed cell and its census terminates
     everywhere, termination being H1's and not the door's.
 PR7 (H3 DELETED -- the tie order reversed so the highest key wins a tie).
     At the standing price some crossed cell's walked strand count or
     depth set differs from its census.

 KILL-SHAPES, as observables this rig PRINTS.
  K1 a both-monotone price with a crossed per-item cell whose count or
     depth set differs from its census. The list is then not sufficient
     and the identity is not a theorem of it.
  K2 an exhaustive-scan cell differing from its economy-scan cell where
     H1 holds. The scan substitution is then not free and every deletion
     reading below is confounded.
  K3 a sigma-falling cell where the census admits an item the walk does
     not seat. The break is then not one-sided and (c)'s mechanism is
     wrong even if the identity fails.
  K4 a sigma-bounded cell off its census, or a sigma-bounded census
     tripping the guard. The termination lemma is then wrong and the
     door side is implicated in well-definedness after all.
  K5 the reversed-tie sweep matching its census at every crossed cell.
     H3 is then not load-bearing for the identity, whatever step A says.
  K6 a control cell of S1 differing from the imported reader. The variant
     walker is then not the corpus's walker and nothing below is a
     reading of the corpus's claim.

RUN DISCIPLINE. One process. S1 walks ten ladders x five partitions at the
standing schedule twice, once through the imported reader and once through
the variant; S2 walks eight prices x ten ladders at three partitions; S2b
walks eight prices x three ladders with the exhaustive scan; S3 walks four
deletions x ten ladders exhaustively -- S3's tie deletion at the economy
scan, the tie order being the walker's and not the schedule's. All at 120
moves, with any cell reading uncrossed or off its census re-read at 400 and
then at 1200. The parent rigs walk the same grids
in about half a second each and peak at 43 MB, and the exhaustive scan runs
the degree cap rather than exiting early, so the estimate is under a minute
and far under the 512 MB line.

SECTIONS.
 S0 forced failures: every detector the verdicts lean on, made to fire --
    a fabricated strand-set mismatch, a fabricated one-sided containment
    the wrong way round, a census climb driven into its own guard, and a
    price-property probe run against a price that violates it.
 S1 positive controls before any verdict: the census against the seven
    recorded headed per-item counts, the guarded census copy against the
    imported one over three schedules, and the variant walker against the
    imported reader at all fifty cells.
 S2 the sufficiency sweep: eight both-monotone prices, ten ladders, the
    per-item identity and the cap at two coarser partitions.
 S2b the scan control: the same prices walked exhaustively on three
    ladders against their economy-scan cells.
 S3 the necessity sweep: H1, H-sigma falling, H-sigma bounded and H3
    deleted one at a time, each read against the census it is supposed to
    reproduce.
 S4 the window control: every cell that read uncrossed OR off its census
    re-read at 400 and then at 1200, stopping as soon as one settles.

RUN RECORD. One process, 9.0 s wall, peak working set 26.7 MB under
memwatch against the 512 MB line. Ten psi ladders, supply two items a
degree to 400, seed (9, 13); 120 moves with the window control at 400 and
1200. Eight both-monotone prices x ten ladders x three partitions, the same
prices x three ladders walked exhaustively, four deletions x ten ladders.

F1 THE CONTROLS HOLD (S0, S1). Every detector fired on its fabricated
   input -- the count and depth-set mismatches, a census excess over a
   walk, and the climb guard, which tripped on the DEGREE-falling price at
   798 items past the splice. The three property probes each fired on a
   price violating them. The census reprints the seven recorded headed
   per-item counts (0, 2, 3, 5, 2, 6, 15); the census COPY reproduces
   explore_splice_cap.census -- counts, depth sets and strand lists -- at
   all 30 cells of three schedules x ten ladders, which is what makes the
   guarded copy a copy and not a second formula; and the variant walker
   reproduces explore_headed_block.read at all 50 standing cells --
   strands, depths, flat minimum, riser count and crossing identical.

F2 THE IDENTITY SURVIVES EVERY BOTH-MONOTONE PRICE SWEPT (S2, S4; PR1,
   PR2; K1 at 0). Of the 80 cells, 78 SETTLE in the sense of the
   hand-attack's (e) and every settled one prints its census EXACTLY,
   count and depth set alike -- including cells an order past the family's
   own figures (42, 47, 118, 177, 240 strands). The two that do not settle
   are named rather than counted either way: at f = d + s^3 the widest two
   ladders carry censuses of 422 and 799 and their runaways have not
   crossed at 1200 moves. No coarser partition prints above its per-item
   census anywhere. AND THE SETTLEMENT DISCIPLINE IS NOT DECORATION: three
   cells read CROSSED and off their census at 120 moves -- the shape of
   the kill this file hunts -- and all three landed exactly on the census
   at the longer window (29 -> 44, 48 -> 118, 48 -> 240). A runaway can
   cross while the admitted set is still filling, which is a second form
   of the parent's vacuity hazard and the one that would have produced a
   false kill.

F3 H1's TWO CONSUMERS ARE SEPARABLE (S2b, PR3; K2 at 0). The exhaustive
   scan reproduces the economy scan cell for cell over eight prices and
   three ladders. So the menu's early exit and the census are DIFFERENT
   consumers of the price's degree-monotonicity, and substituting the
   exhaustive scan through the deletion sweep is free.

F4 H1 IS NECESSARY, AND IT HAS A THIRD JOB NOBODY NAMED (S3 (i), PR4). At
   s * max(1, 5 - d) the walked riser is not (1, 0) at 10 of 10 cells --
   it is (4, 0) or (24, 0) or there is no riser at all -- so the census's
   step B is simply false at that price. And its climb runs past the
   splice into the tail at 10 of 10, 796 or 798 items each: the census is
   not merely wrong there, it is UNDEFINED. Both observables are
   transient-proof, neither being a count; the count column is unreadable
   by (e) at every one of those cells and is recorded rather than read.

F5 THE STATED LIST IS INCOMPLETE BY EXACTLY ONE HYPOTHESIS -- THE PRICE
   MUST BE NONDECREASING IN THE DOOR (S3 (ii), PR5; K3 at 0). At
   d * max(1, 10 - s), which meets H1, H2 and H3 in full, the identity
   fails at 7 of 10 cells, and every failure is the predicted one: the
   walk seats an item the census excludes, deep-only 1 and census-only 0
   at every cell that differs, with no cell failing the other way. The
   excess is read over the DEEP items rather than the strands, which is
   what makes it transient-proof: an item once seated above depth 1 stays
   there, so a deep item the census excludes is a violation no longer
   window can undo, while a strand can still be reclassified a riser by
   later moves. The step that fails is step A's "nothing priced in
   (B, P) is ever created again": a standing item's door grows with the
   tick, and a growing door only costs MORE if the price says so. H2 says
   the DOOR grows; it was being read as though it said the PRICE grows.
   One hypothesis had been doing two jobs for two different consumers.

F6 AND UNBOUNDEDNESS IN THE DOOR IS FREE (S3 (iii), PR6; K4 at 0). At
   d * min(s, 3) -- nondecreasing in both arguments, bounded in the door
   -- every one of the 10 cells crosses, prints its census exactly, and
   the census's climb terminates everywhere with no guard trip. The
   termination lemma at (d) is why, and it is H1's: the deepest strandable
   rung's exit is the splice door e + w, whose price is at least
   price(1, e + w) = P at every degree, so no climb reaches the one door
   that repeats for ever. The first draft of this slate predicted the
   opposite and its own forced-failure section refuted it before any
   verdict ran.

F7 H3 IS NECESSARY (S3 (iv), PR7; K5 at 0). With the tie order reversed so
   the highest key takes a tie, 8 of the 9 crossed cells print off their
   census, and all 8 in the transient-proof direction -- the walk seats
   items the census excludes (2 against 0 at two ladders, 8 against 6 at
   the richest). The one uncrossed cell is not read.

THE VERDICT. The walk-census identity does NOT follow from the three
properties its derivation names, and the missing one is not exotic: the
price must be nondecreasing in BOTH arguments, and only the degree side
was ever written down. That much is proved, a witness being a proof: there
is a price meeting all three and breaking the identity. What is NOT proved
here is the other direction -- whether the derivation with the fourth
hypothesis added closes as a theorem. Steps A-C are a written argument and
this file repairs the one step it found leaking; certifying the repaired
argument line by line is a separate job and is left open. The corrected
list is FOUR, each now carrying a deletion witness except the ladder's
own:

  (H1) the price nondecreasing in the DEGREE -- three consumers, all
       separable: the runaway's identity (step B), the menu's scan economy
       (free, F3), and the census climb's termination (the lemma at (d));
  (H2) doors nondecreasing in time -- the LADDER's property, untested here
       because psi cannot produce a ladder that violates it;
  (H3) a tie at the bar losing to the splice;
  (H4) the price nondecreasing in the DOOR -- new, and the one the corpus
       was consuming through H2 without naming.

Unboundedness in the door is NOT among them. Rule in range for the
sufficiency reading (eight prices x ten ladders, which is evidence and not
a proof); property, proved by construction, for the termination lemma;
rule for each necessity, every one carrying an exhibited witness.
"""

import os
import sys

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_block_clock as BC
import explore_headed_block as HB
import explore_headed_ladder as HL
import explore_price_schedule as PS
import explore_splice_cap as SC
import explore_tick_pump as TP


MOVES = TP.WALK_N        # 120, the family's own figure
LONG = 400               # the window control
DCAP = TP.WALK_DCAP
SEED = TP.GRID_SEED
CLIMB_GUARD = 2000       # the census climb's iteration ceiling, (d)


def ok(cond, msg):
    if not cond:
        raise AssertionError(msg)


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ------------------------------------------------------------- the prices
class Free(PS.Sched):
    """A schedule whose price is an arbitrary function of (degree, door).
    Everything else -- the clock's growth b, the fresh-discount count m, the
    born degrees -- is the family's own, so a sweep here moves the price and
    nothing else."""

    def __init__(self, tag, fn, b=2, m=1, born=(1,)):
        PS.Sched.__init__(self, tag, b=b, m=m, born=born)
        self.fn = fn

    def price(self, d, sigma):
        return self.fn(d, sigma)


def isqrt_up(n):
    """The least integer at or above the square root of n, exactly."""
    r = 0
    while r * r < n:
        r += 1
    return r


# eight prices nondecreasing in d and nondecreasing and unbounded in sigma,
# none of them d^alpha * sigma or d + sigma: a max, a quadratic door, a
# squared sum, a cubic degree, two with FLAT RUNS in d, one growing
# sublinearly in both arguments, and one non-separable.
BOTH_MONOTONE = [
    ("max(d,s)", lambda d, s: max(d, s)),
    ("d*s^2", lambda d, s: d * s * s),
    ("(d+s)^2", lambda d, s: (d + s) ** 2),
    ("d^3*s", lambda d, s: d * d * d * s),
    ("ceil(d/3)*s", lambda d, s: ((d + 2) // 3) * s),
    ("ceil(sqrt(ds))", lambda d, s: isqrt_up(d * s)),
    ("d+s^3", lambda d, s: d + s * s * s),
    ("d*s+s//2", lambda d, s: d * s + s // 2),
]

# the deletions, one hypothesis each. The tie deletion carries the STANDING
# price and moves the walker instead, the tie order being the walker's and
# not the schedule's.
FALL_D = ("H1 gone: s*max(1,5-d)", lambda d, s: s * max(1, 5 - d))
FALL_S = ("H-sigma gone: d*max(1,10-s)", lambda d, s: d * max(1, 10 - s))
BOUND_S = ("H-sigma bounded: d*min(s,3)", lambda d, s: d * min(s, 3))


# --------------------------------------------------- the property probes
def probe_d(sch, dcap=60):
    """The degrees at which price(d, 1) falls -- H1's own observable."""
    return [d for d in range(1, dcap)
            if sch.price(d + 1, 1) < sch.price(d, 1)]


def probe_sigma(sch, smax=60, dtest=(1, 2, 5)):
    """The (degree, door) cells at which the price falls in the DOOR -- the
    unnamed hypothesis's observable."""
    return [(d, s) for d in dtest for s in range(1, smax)
            if sch.price(d, s + 1) < sch.price(d, s)]


def probe_unbounded(sch, smax=4000, dtest=(1, 2, 5)):
    """The degrees whose price stops growing in the door: the price at the
    far door against the price at door 1. Bounded in sigma is what makes the
    census's climb a loop rather than a formula."""
    return [d for d in dtest if sch.price(d, smax) <= sch.price(d, 3)]


# ------------------------------------------------------ the guarded census
def census_guarded(sch, p, e, w, npl, seed, runaway=(1, 0)):
    """explore_splice_cap.census with two things made explicit: the runaway
    is a PARAMETER rather than a constant, and the climb carries the guard
    (d) named. Returns (count, depths, strands, tripped) where tripped names
    the items whose climb ran past the guard -- the observable that a price
    bounded in the door leaves the census undefined rather than wrong."""
    pump = HL.psi_ladder("guarded w%d" % w, p, e, w)
    P = sch.price(1, e + w)
    strands, tripped = [], []
    for d in sorted(npl):
        if npl.get(d, 0) == 0:
            continue
        for slot in range(npl[d]):
            if (d, slot) == runaway:
                continue
            if d in seed and slot == 0:
                cost, x = 0, 1
            elif d in sch.born:
                cost, x = sch.price(d, 2), 2
            elif slot == 0:
                cost, x = sch.price(d, 1), 1
            else:
                cost, x = sch.price(d, 2), 2
            if cost >= P:
                continue
            steps = 0
            while sch.price(d, pump.gap(x)) < P:
                x += pump.gap(x)
                steps += 1
                if steps > CLIMB_GUARD:
                    tripped.append((d, slot))
                    break
            if x > 1:
                strands.append((d, slot, x))
    return (len(strands), sorted(set(x for _, _, x in strands)), strands,
            tripped)


# ------------------------------------------------------- the variant walker
class VWalk(TP.PWalk):
    """The corpus's walker with the menu's SCAN made a dial. `economy` is the
    imported behaviour -- stop at the first degree whose door-1 price already
    beats the best found, sound only under H1. `exhaustive` runs the whole
    degree cap, which is what makes a walk under a deleted H1 a reading of
    the dynamics rather than of a truncated menu."""

    def __init__(self, *a, **kw):
        self.scan = kw.pop("scan", "economy")
        TP.PWalk.__init__(self, *a, **kw)

    def menu(self):
        if self.scan == "economy":
            return TP.PWalk.menu(self)
        best, ties = None, []
        for d in range(1, self.dcap + 1):
            if self.npl.get(d, 0) == 0:
                continue
            row = self.seat.get(d, [])
            cands = []
            if self.npl[d] > len(row):
                r = self.door(d, len(row), 0, "open")
                cands.append((self.sch.price(d, r), d, len(row), r, "open"))
            for i, e in enumerate(row):
                r = self.door(d, i, e, "move")
                cands.append((self.sch.price(d, r), d, i, r, "move"))
            for c in cands:
                if best is None or c[0] < best:
                    best, ties = c[0], [c]
                elif c[0] == best:
                    ties.append(c)
        ok(best is not None, "%s: an empty menu" % self.tag)
        return best, sorted(ties)


def walk_v(npl, sch, pump, cls, n=MOVES, scan="economy", pick="low"):
    """explore_block_clock.walk with the scan and the TIE ORDER made dials.
    `low` is the imported behaviour, the lowest key winning a tie, which is
    H3; `high` deletes it."""
    w = VWalk(npl, sch, pump, cls, DCAP, seed=SEED, scan=scan)
    mins, mark, half = [], None, None
    for i in range(n):
        best, ties = w.menu()
        mins.append(best)
        if i == n - BC.TAIL:
            mark = dict((d, list(v)) for d, v in w.seat.items())
        if i == n - n // 2:
            half = dict((d, list(v)) for d, v in w.seat.items())
        w.apply(ties[0] if pick == "low" else ties[-1])
    return w, mins, mark, half


def read_v(pump, cls, sch, npl, cross, n=MOVES, scan="economy", pick="low"):
    """explore_headed_block.read over the variant walker: the runaway read at
    the HALF window, the strands what is deep and not rising, and `crossed`
    read of the runaway alone."""
    w, mins, mark, half = walk_v(npl, sch, pump, cls, n=n, scan=scan,
                                 pick=pick)
    run, after = BC.rising(w, half)
    deep = w.deep_items()
    keys = set((d, i) for d, i, _, _ in run)
    strand = [(d, i, e) for d, i, e in deep if (d, i) not in keys]
    return {"w": w, "deep": deep, "run": run, "strand": strand,
            "depths": sorted(set(e for _, _, e in strand)),
            "flat": BC.flat_min(mins), "after": after,
            "crossed": all(e >= cross for _, _, _, e in run)}


def keyset(items):
    """A cell's deep population as bare (degree, slot) keys -- what a
    containment read compares, the depths being read separately."""
    return set((d, i) for d, i, _ in items)


# --------------------------------------------------------- S0 forced failures
def s0_forced():
    section("S0  FORCED FAILURES -- every detector fired on purpose, before "
            "any verdict\n    leans on its silence")
    fired = []

    # the identity detector: a fabricated strand set against a census
    got, want = (6, [3, 5]), (5, [3, 5])
    ok(got != want, "the identity detector missed a count mismatch")
    fired.append("count mismatch (6 against 5) -> fired")
    got, want = (6, [3, 5]), (6, [3])
    ok(got != want, "the identity detector missed a depth-set mismatch")
    fired.append("depth-set mismatch ({3,5} against {3}) -> fired")

    # the one-sidedness detector: a census admitting what a walk did not
    walked, cens = set([(2, 0)]), set([(2, 0), (3, 0)])
    ok(cens - walked, "the one-sidedness detector missed a census excess")
    fired.append("census excess over the walk -> fired")

    # the climb guard, driven by the price that deletes H1 -- which is what
    # the termination lemma at (d) says is the only thing that can drive it
    sch = Free(*FALL_D)
    _, _, _, trip = census_guarded(sch, 2, 4, 2, HL.supply(), SEED)
    ok(trip, "the climb guard never tripped on a degree-falling price")
    fired.append("census climb guard on a degree-falling price -> fired (%d "
                 "items past the splice)" % len(trip))

    # the property probes, each against a price that violates it
    ok(probe_d(Free(*FALL_D)), "the degree probe missed a falling price")
    ok(probe_sigma(Free(*FALL_S)), "the door probe missed a falling price")
    ok(probe_unbounded(Free(*BOUND_S)),
       "the unboundedness probe missed a bounded price")
    fired.append("the three property probes on prices that violate them -> "
                 "all fired")
    for f in fired:
        print("  %s" % f)


# ------------------------------------------------------- S1 positive controls
def s1_controls(std, npl):
    section("S1  POSITIVE CONTROLS at the standing schedule -- the census "
            "against the\n    recorded counts, and the variant walker "
            "against the imported reader")
    want = [0, 2, 3, 5, 2, 6, 15]
    got = []
    for tag, p, e, w in HL.HEADED:
        a, _, _, trip = census_guarded(std, p, e, w, npl, SEED)
        ok(not trip, "%s: the standing census tripped its own climb guard"
           % tag)
        got.append(a)
    ok(got == want, "the census reprints %s against the recorded %s"
       % (got, want))
    print("  (a) the seven recorded headed per-item counts: %s -- equal."
          % got)

    # the copy against the original, everywhere the original terminates:
    # census_guarded differs from SC.census only in taking the runaway as a
    # parameter and guarding the climb, and a drift between them would be
    # invisible to every other control in this file
    n = 0
    for stag, sch in [("standing", std),
                      ("alpha=2", PS.Sched("a2", alpha=2)),
                      ("additive", PS.Sched("add", add=True))]:
        for tag, p, e, w in HL.LEGAL:
            mine = census_guarded(sch, p, e, w, npl, SEED)
            theirs = SC.census(sch, p, e, w, npl, SEED)
            ok(not mine[3], "%s / %s: the copy tripped its own guard where "
                            "the original terminates" % (stag, tag))
            ok((mine[0], mine[1], sorted(mine[2])) ==
               (theirs[0], theirs[1], sorted(theirs[2])),
               "%s / %s: the census copy differs from explore_splice_cap's"
               % (stag, tag))
            n += 1
    print("  (b) the census copy against explore_splice_cap.census at %d "
          "cells (three\n      schedules x ten ladders), counts, depth sets "
          "and strand lists: identical." % n)

    diffs = 0
    for tag, p, e, w in HL.LEGAL:
        pump = HL.psi_ladder("ctl %s" % tag, p, e, w)
        cross = HL.cross_from(pump)
        for ptag, cls in BC.PARTITIONS:
            a = HB.read(pump, cls, std, npl, cross, n=MOVES)
            b = read_v(pump, cls, std, npl, cross, n=MOVES)
            same = (sorted(a["strand"]) == sorted(b["strand"])
                    and a["depths"] == b["depths"]
                    and a["flat"] == b["flat"]
                    and len(a["run"]) == len(b["run"])
                    and a["crossed"] == b["crossed"])
            if not same:
                diffs += 1
                print("  K6: %s / %s differs from the imported reader"
                      % (tag, ptag))
    ok(diffs == 0, "the variant walker differs from the imported reader at "
                   "%d cells" % diffs)
    print("  (c) the variant walker against explore_headed_block.read at all "
          "%d cells\n      (strands, depths, flat minimum, riser count, "
          "crossing): identical."
          % (len(HL.LEGAL) * len(BC.PARTITIONS)))


# ---------------------------------------------------- S2 the sufficiency sweep
CAP_PARTS = [("1 block", dict(BC.PARTITIONS)["1 block"]),
             ("4 blocks", dict(BC.PARTITIONS)["4 blocks"])]
PERITEM = dict(BC.PARTITIONS)["per item"]


def s2_sufficiency(npl):
    section("S2  THE SUFFICIENCY SWEEP -- eight prices nondecreasing in the "
            "degree and\n    nondecreasing and unbounded in the door, ten "
            "ladders, %d moves" % MOVES)
    print("  %-16s %-15s %-6s %-9s %-9s %s"
          % ("price", "ladder", "cross", "walked", "census", "depths w/c"))
    k1, k2cap, uncrossed = [], [], []
    for ptag, fn in BOTH_MONOTONE:
        sch = Free(ptag, fn)
        ok(not probe_d(sch), "%s: falls in the degree" % ptag)
        ok(not probe_sigma(sch), "%s: falls in the door" % ptag)
        ok(not probe_unbounded(sch), "%s: is bounded in the door" % ptag)
        sch.check_monotone(DCAP)
        for tag, p, e, w in HL.LEGAL:
            pump = HL.psi_ladder("%s %s" % (ptag, tag), p, e, w)
            cross = HL.cross_from(pump)
            a, dep, _, trip = census_guarded(sch, p, e, w, npl, SEED)
            ok(not trip, "%s / %s: the census tripped its climb guard"
               % (ptag, tag))
            c = read_v(pump, PERITEM, sch, npl, cross, n=MOVES)
            n = len(c["strand"])
            if not c["crossed"] or n != a or c["depths"] != dep:
                uncrossed.append((ptag, tag, n, c["depths"], a, dep,
                                  c["crossed"]))
                if c["crossed"]:
                    k1.append((ptag, tag, n, c["depths"], a, dep))
            for qtag, cls in CAP_PARTS:
                cc = read_v(pump, cls, sch, npl, cross, n=MOVES)
                if len(cc["strand"]) > a:
                    k2cap.append((ptag, tag, qtag, len(cc["strand"]), a))
            print("  %-16s %-15s %-6s %-9d %-9d %s / %s"
                  % (ptag, tag, "yes" if c["crossed"] else "NO", n, a,
                     c["depths"], dep))
    print("\n  K1 at %d moves (crossed and off its census -- read as a "
          "VERDICT only\n      after S4, a cell whose census exceeds what "
          "the move budget can seat\n      being unreadable rather than "
          "off): %s" % (MOVES, k1 or "none"))
    print("  PR2 (a partition above the census):   %s" % (k2cap or "none"))
    print("  carried to S4 (uncrossed or off census): %s"
          % ([(a, b) for a, b, _, _, _, _, _ in uncrossed] or "none"))
    return k1, uncrossed


def s2b_scan(npl):
    section("S2b THE SCAN CONTROL -- the same prices walked EXHAUSTIVELY on "
            "three\n    ladders against their economy-scan cells")
    k2 = []
    lads = [HL.LEGAL[0], HL.LEGAL[5], HL.LEGAL[8]]
    for ptag, fn in BOTH_MONOTONE:
        sch = Free(ptag, fn)
        for tag, p, e, w in lads:
            pump = HL.psi_ladder("%s %s" % (ptag, tag), p, e, w)
            cross = HL.cross_from(pump)
            a = read_v(pump, PERITEM, sch, npl, cross, n=MOVES)
            b = read_v(pump, PERITEM, sch, npl, cross, n=MOVES,
                       scan="exhaustive")
            if sorted(a["strand"]) != sorted(b["strand"]):
                k2.append((ptag, tag, len(a["strand"]), len(b["strand"])))
    print("  %d prices x %d ladders walked both ways." % (len(BOTH_MONOTONE),
                                                          len(lads)))
    print("  K2 (exhaustive differing from economy): %s" % (k2 or "none"))
    return k2


# ----------------------------------------------------- S3 the necessity sweep
def s3_necessity(std, npl):
    section("S3  THE NECESSITY SWEEP -- one hypothesis deleted at a time, "
            "each cell\n    walked EXHAUSTIVELY so the menu is the dynamics "
            "and not a truncation")

    # --- H1 deleted: the price falls in the degree
    print("\n  (i) H1 deleted -- %s. The census fixes the runaway at "
          "(1, 0)\n      and reads its splice as the bar; the walk is asked "
          "what it actually\n      seats and what actually rises."
          % FALL_D[0])
    sch = Free(*FALL_D)
    print("      the price falls in the degree at %d of the first 59 steps."
          % len(probe_d(sch)))
    off_runaway, mism, trips = [], [], []
    for tag, p, e, w in HL.LEGAL:
        pump = HL.psi_ladder("H1 %s" % tag, p, e, w)
        cross = HL.cross_from(pump)
        c = read_v(pump, PERITEM, sch, npl, cross, n=MOVES,
                   scan="exhaustive")
        a, dep, _, trip = census_guarded(sch, p, e, w, npl, SEED)
        if trip:
            trips.append((tag, len(trip)))
        risers = sorted((d, i) for d, i, _, _ in c["run"])
        if risers != [(1, 0)]:
            off_runaway.append((tag, risers[:3], len(risers)))
        if len(c["strand"]) != a or c["depths"] != dep:
            mism.append((tag, len(c["strand"]), a))
        print("      %-15s risers %-14s walked %-5d census %-5d trips %-4d %s"
              % (tag, str(risers[:2]) + ("..." if len(risers) > 2 else ""),
                 len(c["strand"]), a, len(trip), c["depths"]))
    print("      PR4, the two TRANSIENT-PROOF observables -- neither is a "
          "count, and\n           the count column above is UNREADABLE by "
          "(e), every census here\n           standing at 796 or above "
          "against a budget of %d moves:" % MOVES)
    print("      PR4: cells whose riser set is not [(1, 0)]: %d of %d"
          % (len(off_runaway), len(HL.LEGAL)))
    print("      PR4: cells whose census climb passed the splice (the "
          "termination\n           lemma's own observable, a formula fact "
          "with no walk in it): %d of %d" % (len(trips), len(HL.LEGAL)))
    print("      (the count column, recorded and not read: %d of %d cells "
          "differ)" % (len(mism), len(HL.LEGAL)))

    # --- the door side deleted, falling
    print("\n  (ii) the DOOR side deleted (falling) -- %s. Derived at the "
          "hand-\n       attack (c): the break must be ONE-SIDED, the walk "
          "seating what the\n       census excluded and never the reverse."
          % FALL_S[0])
    sch = Free(*FALL_S)
    ok(not probe_d(sch), "the door-falling price also falls in the degree")
    contain, reverse, mism2 = 0, [], 0
    for tag, p, e, w in HL.LEGAL:
        pump = HL.psi_ladder("Hs %s" % tag, p, e, w)
        cross = HL.cross_from(pump)
        c = read_v(pump, PERITEM, sch, npl, cross, n=MOVES,
                   scan="exhaustive")
        a, dep, cs, _ = census_guarded(sch, p, e, w, npl, SEED)
        # the transient-proof read is over the DEEP items and not the
        # strands: a strand can be reclassified a riser by later moves,
        # but an item seated above depth 1 stays there for ever, so an
        # item deep in the walk and absent from the census is a violation
        # no longer window can undo. The runaway is dropped by hand, the
        # census excluding it by construction rather than by admission.
        wk = keyset(c["deep"]) - set([(1, 0)])
        ck = keyset(cs)
        if len(c["strand"]) != a or c["depths"] != dep:
            mism2 += 1
        if ck - wk:
            reverse.append((tag, sorted(ck - wk)[:3]))
        elif wk - ck:
            contain += 1
        print("      %-15s walked %-5d census %-5d  deep-only %-4d "
              "census-only %d"
              % (tag, len(c["strand"]), a, len(wk - ck), len(ck - wk)))
    print("      PR5: cells off their census: %d of %d" % (mism2,
                                                           len(HL.LEGAL)))
    print("      PR5: cells where the walk strictly contains the census: %d"
          % contain)
    print("      K3 (a census admitting what the walk did not seat): %s"
          % (reverse or "none"))
    print("      The direction is what makes this read TRANSIENT-PROOF, and "
          "the excess is\n      read over the DEEP items rather than the "
          "strands: an item once seated above\n      depth 1 stays there, "
          "so a deep item the census excludes is a violation no\n      "
          "longer window can undo, while a strand can still be "
          "reclassified a riser.")

    # --- the door side deleted, bounded
    print("\n  (iii) the door side BOUNDED -- %s. Nondecreasing in both\n"
          "        arguments, so H1, H2 and H3 all stand; by the "
          "termination lemma at\n        (d) the climb still stalls at the "
          "splice, so this is a positive read."
          % BOUND_S[0])
    sch = Free(*BOUND_S)
    ok(not probe_d(sch), "the door-bounded price falls in the degree")
    ok(not probe_sigma(sch), "the door-bounded price falls in the door")
    ok(probe_unbounded(sch), "the door-bounded price is unbounded after all")
    tripped, mism4, cr4 = [], [], 0
    for tag, p, e, w in HL.LEGAL:
        pump = HL.psi_ladder("Hb %s" % tag, p, e, w)
        cross = HL.cross_from(pump)
        a, dep, _, trip = census_guarded(sch, p, e, w, npl, SEED)
        if trip:
            tripped.append((tag, len(trip)))
        c = read_v(pump, PERITEM, sch, npl, cross, n=MOVES)
        if c["crossed"]:
            cr4 += 1
            if len(c["strand"]) != a or c["depths"] != dep:
                mism4.append((tag, len(c["strand"]), a))
        print("      %-15s crossed %-4s walked %-5d census %-5d %s / %s"
              % (tag, "yes" if c["crossed"] else "NO", len(c["strand"]), a,
                 c["depths"], dep))
    print("      PR6: cells whose census climb ran past the guard of %d: "
          "%d of %d" % (CLIMB_GUARD, len(tripped), len(HL.LEGAL)))
    print("      PR6: crossed cells off their census: %d of %d crossed"
          % (len(mism4), cr4))
    print("      K4 (a bounded cell off its census, or a tripped guard): %s"
          % ((tripped + mism4) or "none"))

    # --- H3 deleted: the tie order reversed
    print("\n  (iv) H3 deleted -- the standing price with the tie order "
          "REVERSED, the\n       highest key winning a tie instead of the "
          "splice's lowest.")
    mism3, crossed, excess = [], 0, 0
    for tag, p, e, w in HL.LEGAL:
        pump = HL.psi_ladder("H3 %s" % tag, p, e, w)
        cross = HL.cross_from(pump)
        c = read_v(pump, PERITEM, std, npl, cross, n=MOVES, pick="high")
        a, dep, cs, _ = census_guarded(std, p, e, w, npl, SEED)
        off = len(c["strand"]) != a or c["depths"] != dep
        if c["crossed"]:
            crossed += 1
            if off:
                mism3.append((tag, len(c["strand"]), a))
                if (keyset(c["deep"]) - set([(1, 0)])) - keyset(cs):
                    excess += 1
        print("      %-15s crossed %-4s walked %-5d census %-5d %s / %s%s"
              % (tag, "yes" if c["crossed"] else "NO", len(c["strand"]), a,
                 c["depths"], dep, "" if c["crossed"] else "   (not read)"))
    print("      PR7: CROSSED cells off their census: %d of %d crossed; the "
          "uncrossed\n           cell is not read at all"
          % (len(mism3), crossed))
    print("      PR7: of those, cells seating an item the census excludes "
          "(the\n           transient-proof direction again): %d" % excess)
    print("      K5 (the reversed tie matching everywhere): %s"
          % ("FIRED" if not mism3 else "none"))
    return off_runaway, mism, reverse, tripped, mism3


# ---------------------------------------------------------- S4 window control
def s4_window(npl, carried):
    section("S4  THE WINDOW CONTROL -- every cell that read uncrossed or off "
            "its census\n    at %d moves, re-read at %d and then at %d. A "
            "cell whose census exceeds\n    what the budget can seat is "
            "UNREADABLE at that budget, which is a fact\n    about the "
            "instrument and not about the identity." % (MOVES, LONG, 3 * LONG))
    if not carried:
        print("  No cell of the sufficiency sweep was carried here.")
        return []
    bad, unread = [], []
    for ptag, tag, n120, dep120, a, dep, _ in carried:
        sch = Free(ptag, dict(BOTH_MONOTONE)[ptag])
        p, e, w = [r[1:] for r in HL.LEGAL if r[0] == tag][0]
        row = []
        for n_moves in (LONG, 3 * LONG):
            pump = HL.psi_ladder("long %s %s" % (ptag, tag), p, e, w)
            cross = HL.cross_from(pump)
            c = read_v(pump, PERITEM, sch, npl, cross, n=n_moves)
            row.append((len(c["strand"]), c["depths"], c["crossed"]))
            if c["crossed"] and len(c["strand"]) == a and c["depths"] == dep:
                break
        n, dp, cr = row[-1]
        rising = len(row) > 1 and row[-1][0] > row[-2][0]
        if cr and n == a and dp == dep:
            state = "SETTLED on its census"
        elif (not cr) or rising or a >= n_moves:
            state = "unreadable at %d moves (census %d, %s)" % (
                n_moves, a,
                "uncrossed" if not cr else
                ("still filling" if rising else "census above the budget"))
            unread.append((ptag, tag, a, n_moves))
        else:
            state = "OFF ITS CENSUS"
            bad.append((ptag, tag, n, a))
        print("  %-16s %-15s %d -> %s : %s"
              % (ptag, tag, n120,
                 " -> ".join("%d%s" % (x, "" if c else "*")
                             for x, _, c in row),
                 state))
    print("\n  (* = the runaway had not crossed at that window.)")
    print("  K1 at the long windows:               %s" % (bad or "none"))
    print("  unreadable at the budgets run (census above what the walk can\n"
          "  seat -- named rather than counted as agreement or as a break): "
          "%s" % (unread or "none"))
    return bad


def main():
    std = PS.Sched("standing d*sigma")
    npl = dict((d, 2) for d in range(1, DCAP + 1))
    print("THE HYPOTHESIS AUDIT UNDER THE STRAND LAW -- what the walk-census "
          "identity\nconsults. Ten psi ladders, supply two items a degree to "
          "%d, seed %s,\n%d moves with the long window at %d."
          % (DCAP, SEED, MOVES, LONG))
    s0_forced()
    s1_controls(std, npl)
    k1, uncrossed = s2_sufficiency(npl)
    s2b_scan(npl)
    s3_necessity(std, npl)
    s4_window(npl, uncrossed)
    print("\nDone.")


if __name__ == "__main__":
    main()
