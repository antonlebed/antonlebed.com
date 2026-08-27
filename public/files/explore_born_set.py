"""explore_born_set.py -- THE BORN SET AS A DIAL. Does the born opening reach
the strand SET, or only the runaway's name?

THE QUESTION. The walk-census identity's derivation closes on a list of
five properties, four of them hypotheses (explore_census_theorem.py). The
fifth property, THE BORN OPENING, says the born degree's opening is not
undercut by a fresh discount -- price(1, 2) <= price(d, 1) at every d --
and its necessity was proved by a witness: delete it and the single late
riser is (2, 0) rather than (1, 0) at four of the nine prices swept. But
every one of those four firings sits on the exact ladder, whose bar
degenerates to the tail door 1 and whose census is EMPTY, so the identity's
numbers agreed vacuously there and one question was left open in the
mechanism's own quantity: can an undercut born opening move the strand set
at a cell whose census is non-empty? The cheapest probe is the born set
itself, which the schedule carries as a dial (explore_price_schedule.py,
Sched(born=...), default (1,)): take degree 1 out, born = (), and the born
opening has no privilege left to be undercut. This file runs that dial at
every price and every ladder the derivation was certified on, and reads the
strand set at born = () against born = (1,).

THE INSTRUMENT, all of it imported: the ladder-general census, the
instrumented walker and its settlement reading from
explore_census_theorem.py; the psi ladders, the roster of ten legal and
four illegal ones from explore_headed_ladder.py; the eight both-monotone
prices from explore_price_hypotheses.py and the standing d * sigma; the
partitions from explore_block_clock.py. The born set enters the engine at
exactly two places -- PWalk.covered, which decides whether an opening pays
the discount door 1 or its own tick + 1, and the census's entry branch --
so a sweep here moves the born set and nothing else.

THE HAND-ATTACK, on paper before any engine code.

 (a) THE INDEX CONVENTION, re-derived from the engine. A ladder's door at
     depth x is gap(x) = next_at(x) + 1 - x; 1 is a member of every ladder,
     so gap(1) = 1 and an item opened at the discount door lands at depth
     1 and climbs to 2 at door 1. The born degree opens at its own tick + 1
     = 2 and lands at depth 2 directly. Under a per-item clock a never-
     landed item's tick is 1, so the SECOND slot of any degree opens at
     door 2 whether or not the degree is born -- once the first slot has
     spent the discount, the degree is covered either way.

 (b) THE CENSUS DOES NOT READ THE BORN SET AT DEGREE 1 -- by inspection of
     the formula. The census excludes the runaway (1, 0) by construction
     and prices (1, 1) at price(1, 2) from depth 2; at born = () the code
     path for (1, 1) is "not born, not slot 0", which is the same price at
     the same depth. Every other degree is outside the born set at both
     settings. So the census at born = () is the census at born = (1,),
     cell for cell, and the question is entirely about the WALK.

 (c) THE OVERTAKING LEMMA, which is the derivation's step B stated without
     the born opening. Fix a per-item clock and a ladder, and suppose the
     price is nondecreasing in the degree and in the door (H1, H4) with
     ties going to the lowest key (H3). Call any item that opens at the
     discount door a RIVAL. A rival at a rung whose door is 2 or wider
     prices at price(d, sigma) >= price(1, 2) by H1 and H4, so it cannot
     pass such a door before the born degree (1, 0) has opened -- (1, 0)
     is the menu minimum there, or ties and wins on the key. Hence when
     (1, 0) opens, every rival stands at or below x1, the FIRST rung whose
     door is 2 or wider, having climbed only door-1 rungs; (1, 0) lands at
     depth 2 <= x1 and climbs the same door-1 rungs at price(1, 1), the
     least price on any menu, reaching x1 while the rivals are still at or
     below it. From a shared rung (1, 0) is cheaper or first, and a rival
     behind it lands at most on (1, 0)'s own rung -- the next rung after x
     is next_at(x) + 1, and (1, 0) ahead of x stands at or beyond it -- so
     a rival can catch up and never pass. So (1, 0) reaches the bar rung
     and the tail first, recurs at price(1, tail), and every rival's door
     prices at or above it, tying at best and losing the tie: (1, 0) is
     the unique runaway. WHAT THE LEMMA NEEDS OF THE LADDER: that x1
     exists -- the ladder carries a door of width 2 or more at all, the
     tail's own step included. The one ladder with none is the exact ladder,
     every positive integer a member, gap 1 for ever; there the bar is the
     tail door 1, the census is empty, and a rival whose discount undercuts
     the born opening runs away at price(d, 1) with (1, 0) never opening.
     So THE BORN OPENING GRADES THE RUNAWAY'S NAME ON THE EXACT LADDER AND
     NOTHING ELSE ANYWHERE: it is not a hypothesis of the identity, whose
     list is then H1, H3 and H4 -- three -- with H2 a property of the
     landing rule. The cell the open clause asked for -- a non-empty
     census, a bar above the tail, a degree whose discount undercuts --
     is predicted to carry the riser (1, 0) and to print its census.

 (d) THE MARGINS, hand-derived at Q_2 w1 (members 1, 3, 4, 5, ...; steps
     2, 1, 1, ...; tail 1, one overshoot, bar door 2, bar rung 4) under
     f = d * sigma^2, where price(2, 1) = 2 undercuts price(1, 2) = 4 --
     a cell of exactly the kind the open clause named, and one that sat
     inside the parent's own sweep unread. Supply two a degree, seed (9,
     13). CENSUS, P = 4: (1, 1) enters at 4, excluded; (2, 0) enters at 2,
     climbs 1 -> 2 at door 1 (price 2), stalls at 2 (door 2 prices 8);
     (2, 1) enters at 8, excluded; (3, 0) enters at 3, climbs to 2, stalls
     (door 2 prices 12); (4, 0) enters at 4, excluded; the seeds' first
     door prices 9 and 13. A = 2, depths {2}, strands (2, 0) and (3, 0).
     WALK at born = (1,): (2, 0) opens at 2, moves to depth 2 at 2, its
     door then 2 at price 8; (3, 0) opens at 3, moves to 2 at 3, door 2 at
     12; the menu's next minimum is 4, tied between (1, 0)'s opening at
     door 2 and (4, 0)'s at door 1, and the key gives it to (1, 0), which
     lands at depth 2 with tick 3, door 2, price 4 -- ties with (1, 1)'s
     opening and (4, 0)'s and wins on the key again, lands at 4, tick 4,
     door 1, and recurs at price 1 for ever. Strands (2, 0) at 2 and
     (3, 0) at 2, the riser (1, 0). WALK at born = (): (1, 0) opens at
     price 1, moves to depth 2 at price 1, then the same seven moves in
     the same order. Same set, same riser. WALK at born = (1, 2): degree 2
     opens at door 2, price 8, so (3, 0) goes first and (1, 0) follows;
     census A = 1, depths {2}, strand (3, 0) -- the born set moving the
     census through the formula's own entry branch, which is a parameter
     the formula READS and not a hypothesis it omits.

 (e) THE SHIFT. At a price meeting the born opening, (1, 0) opens first at
     both settings: at born = (1,) in one move to depth 2, at born = () in
     two moves at door 1 -- the first tickless, the second landing at 2
     with the same tick. After that the two states are identical in every
     field the menu reads (covered(1) is true either way), so the born = ()
     walk is the born = (1,) walk with one move prepended, at every step.
     At a violating price the ORDER of the early moves differs -- a rival
     opens before (1, 0) at born = (1,) and after it at born = () -- so
     the shift is not exact there and only the settled strand sets are
     compared.

 (f) THE VACUITY HAZARD is the parent's, both forms, carried unchanged: a
     cell is read only where its runaway is across AND its strand set --
     keys and depths -- stands still between 120 and 400 moves; a cell
     unsettled at either born set is named and re-read at 400 and 1200
     rather than compared.

THE SLATE, frozen before the engine.

 PR1 (CENSUS INVARIANCE, derived at (b)). census_lad at born = () equals
     census_lad at born = (1,) -- count, depth set and strand list -- at
     every one of the nine prices by fourteen ladders.
 PR2 (THE PROBE). At every cell settled at both born sets, the walked
     strand set -- keys and depths -- is identical at born = () and at
     born = (1,); and at born = () the single late riser is (1, 0) at
     every settled cell, the exact ladder and the four violating prices
     included.
 PR3 (THE SHIFT, derived at (e)). At the five prices meeting the born
     opening, the born = () walk's seated shape after k + 1 moves equals
     the born = (1,) walk's after k moves, for every k from 1 to 120, at
     every ladder.
 PR4 (THE LEMMA'S OBSERVABLE at born = (1,), derived at (c)). At every
     settled cell whose ladder carries a door of width 2 or more, the
     single late riser is (1, 0) at all nine prices; on the exact ladder
     the riser is (d*, 0) with d* the least degree whose discount
     undercuts, at each of the four violating prices, and (1, 0) at the
     five that meet it; and every cell the open clause asked for -- a
     violating price, a non-empty census, a bar above the tail -- prints
     its census exactly with the riser (1, 0). The hand-derived Q_2 w1
     cell reads A = 2 at depth 2, strands (2, 0) and (3, 0).
 PR5 (THE DIAL AS A FORMULA INPUT). At born = (1, 2) every settled cell
     prints its own census exactly; that census differs from the
     born = (1,) one at some cells, and the Q_2 w1 cell reads A = 1.
 PR6 (COARSER CLOCKS). At the standing price, over ten ladders and five
     partitions, the strand set at born = () equals the born = (1,) set at
     every cell settled at both.

 KILL-SHAPES, as observables this rig PRINTS.
  K1 a cell settled at both born sets with differing strand sets. The
     born set is then a parameter of the strand law the list omits.
  K2 a born = () settled cell whose single late riser is not (1, 0).
  K3 a born = (1,) settled cell on a ladder with a wide door whose riser
     is not (1, 0); or a cell of the open clause's kind off its census.
     The overtaking lemma is then wrong.
  K4 a shift mismatch at a price meeting the born opening.
  K5 a born = (1, 2) settled cell off its own census.
  K6 a census at born = () differing from the census at born = (1,).

RUN DISCIPLINE. One process. Nine prices by fourteen ladders by three born
sets at 120 and 400 moves through the instrumented walker, the shift
check at 121 moves per cell, the partition sweep ten ladders by five cuts
by two born sets at two windows, and the window control at 400 and 1200
for whatever reads unsettled. The parent's sweep of the same grids at one
born set ran 8.3 s and peaked at 94 MB, so the estimate is under a minute
and far under the 512 MB line.

SECTIONS.
 S0 forced failures: every detector fired on a fabricated input -- a
    strand-set difference, a riser that is not (1, 0), a wide-door read on
    a doctored ladder.
 S1 positive controls before any verdict: the census at born = (1,)
    against the seven recorded headed counts; the parent's four firings
    reproduced; the Q_2 w1 margins at all three born sets.
 S2 the census invariance across the born dial.
 S3 the probe: born = () against born = (1,), per-item clock, with the
    shift check at the prices meeting the born opening.
 S4 the lemma's observables at born = (1,), and the cells of the open
    clause's kind.
 S5 the born = (1, 2) control.
 S6 the partition sweep at the standing price.
 S7 the window control.

RUN RECORD. One process, 15.0 s wall, peak working set 91.0 MB under
memwatch against the 512 MB line, 38 checks. Nine prices by fourteen
ladders (ten arithmetic, four the family cannot produce), supply two items
a degree to 400, seed (9, 13), 120 moves with the settlement read as the
strand set standing still between 120 and 400 and the window control at
400 and 1200.

F1 THE CONTROLS HOLD (S0, S1). Every detector fired on its fabricated
   input. The census at born = (1,) reprints the seven recorded headed
   counts; the parent's four firings reproduce on the exact ladder -- the
   riser (2, 0) at d * s^2, ceil(d/3) * s, d + s^3 and d * s + s//2 and
   (1, 0) at the other five; and the hand-derived Q_2 w1 cell under
   d * s^2 prints to the item at all three born sets -- A = 2 at depth 2,
   strands (2, 0) and (3, 0), at born = () and at born = (1,); A = 1,
   strand (3, 0), at born = (1, 2) -- the walk equal and the riser (1, 0)
   at each.

F2 THE CENSUS DOES NOT MOVE (S2, PR1; K6 at 0). census_lad at born = ()
   equals census_lad at born = (1,) -- count, depth set and strand list --
   at all 126 cells of nine prices by fourteen ladders, as (b) read off
   the formula.

F3 THE STRAND SET DOES NOT MOVE, AND AT born = () THE RUNAWAY IS (1, 0)
   EVERYWHERE (S3, S7; PR2, PR3; K1, K2, K4 all at 0). At the 113 cells
   settled at both born sets the walked strand set -- keys and depths --
   is identical, and the single late riser at born = () is (1, 0) at every
   one of them, the exact ladder at the four violating prices included:
   with no born privilege to undercut, degree 1 opens at the discount door
   at the least price on any menu and nothing ever passes it. At the five
   prices meeting the born opening the shift of (e) is exact: the
   born = () walk's shape and ticks after k + 1 moves equal the born = (1,)
   walk's after k, for every k to 120, at all 70 cells. Of the 13 cells
   unsettled at 120 moves -- all at violating prices -- nine settle at 400
   or 1200 on their census with the riser (1, 0) at both born sets
   (censuses 42 to 240), and four stay unsettled at 1200 at both:
   d + s^3 on the two widest arithmetic ladders, which are the parent's
   own two unreadable cells, and on the late-splice and double-splice
   ladders. Those are named and not counted either way.

F4 THE OVERTAKING LEMMA HOLDS, AND THE OPEN CLAUSE'S CELL WAS INSIDE THE
   PARENT'S SWEEP ALL ALONG (S4, PR4; K3 at 0). Every ladder but the exact
   one carries a wide door -- x1 = 2 at three, 3 at nine, 6 at the narrow
   ramp -- and at every one of the 104 settled cells at born = (1,) on
   those thirteen ladders the riser is (1, 0), the four violating prices
   included (113 settled cells in all, the exact ladder's nine among
   them). On the exact ladder the riser is (d*, 0) with d* the least
   undercutting degree at each violating price and (1, 0) at each meeting
   one, 9 of 9, the census 0 at all nine. And the cell the parent named as
   missing -- a violating price, a NON-EMPTY census, a bar strictly above
   the tail -- is not missing: 25 such cells sit inside the roster,
   censuses 1 to 44 across five ladders at d * s^2, eight at
   ceil(d/3) * s, three at d + s^3 and nine at d * s + s//2, and every one
   prints its census exactly with the riser (1, 0). The born opening being
   undercut moves nothing there, not even the runaway's name: the rival
   that opens first climbs its door-1 rungs and waits at x1, where the born
   degree opens, catches it, and passes.

F5 THE BORN SET IS AN INPUT THE FORMULA READS (S5, PR5; K5 at 0). At
   born = (1, 2) the census moves at 26 of the 126 cells -- degree 2's
   entry now priced at door 2 -- and the walk prints the recomputed census
   exactly at all 113 settled cells. The dial is a parameter of the
   admission census's entry branch, which already carries it, and not a
   hypothesis the derivation omits.

F6 COARSER CLOCKS AGREE (S6, PR6). At the standing price the strand set
   at born = () equals the born = (1,) set at all 50 cells of ten ladders
   by five partitions, every cell settled.

THE VERDICT. The born opening grades the runaway's NAME on the exact
ladder and nothing else anywhere. Where the ladder carries any door of
width 2 or more, the tail's own step included -- every ladder but the
all-integers one -- the born degree is the unique runaway under degree-monotonicity,
door-monotonicity and the tie order alone, by the overtaking lemma of (c),
and the walk prints its census whether or not a discount undercuts the
born opening; on the exact ladder the census is empty, so the identity's
numbers cannot move. The walk-census identity's hypothesis list is
therefore THREE -- the price nondecreasing in the degree, nondecreasing in
the door, and the tie at the bar going to the lowest key -- with the
doors' monotonicity in time a property of the landing rule and the born
opening a hypothesis of step B's LITERAL wording, "the runaway is degree 1
slot 0", on one ladder where nothing consumes it. What the clause left
open closes the way the lemma says: an undercut born opening cannot move
the strand set, because it cannot move the runaway wherever there is a
strand set to move.

Property, proved by construction, for the census invariance and the
shift; rule for the overtaking lemma, a derivation on H1, H3 and H4
corroborated at every settled cell of nine prices by fourteen ladders;
rule in range for the strand-set agreement across the born dial, 113
per-item cells and 50 partition cells, which is evidence and not a proof
of anything the lemma does not already give.
"""

import os
import sys

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_block_clock as BC
import explore_census_theorem as CT
import explore_headed_ladder as HL
import explore_price_hypotheses as PH
import explore_tick_pump as TP


MOVES = CT.MOVES           # 120
LONG = CT.LONG             # 400
LONGER = CT.LONGER         # 1200
DCAP = CT.DCAP
SEED = CT.SEED
PRICES = CT.PRICES         # the eight both-monotone prices and d * sigma
BORN = [("born=()", ()), ("born=(1,)", (1,)), ("born=(1,2)", (1, 2))]

CHECKS = [0]


def ok(cond, msg):
    CHECKS[0] += 1
    if not cond:
        raise AssertionError(msg)


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def sched_of(tag, fn, born):
    return PH.Free("%s %s" % (tag, born), fn, born=born)


def ladders():
    out = [(t, HL.psi_ladder(t, p, e, w)) for t, p, e, w in HL.LEGAL]
    out += [(p.tag, p) for p, _ in HL.illegal_ladders()]
    return out


def first_wide(pump, upto=200):
    """x1 of hand-attack (c): the first depth whose door is 2 or wider, or
    None where every door below `upto` is 1 -- the exact ladder."""
    for x in range(1, upto):
        if pump.gap(x) >= 2:
            return x
    return None


def undercutters(sch):
    return CT.probe_born(sch)


def strand_key(r):
    return (CT.keyset(r["strand"]), tuple(r["depths"]))


def read_settled(pump, sch, cls=TP.PERITEM):
    """One cell at 120 and 400 moves under the parent's settlement reading:
    the runaway across and the strand set -- keys and depths -- standing
    still between the two windows. Returns (settled, the 400-move read)."""
    bar = CT.bar_door(pump)[0]
    r1 = CT.certify(pump, sch, CT.supply(), cls, n=MOVES, bar=bar)
    r2 = CT.certify(pump, sch, CT.supply(), cls, n=LONG, bar=bar)
    settled = (r1["cross"] is not None and r2["cross"] is not None
               and strand_key(r1) == strand_key(r2) and len(r2["late"]) == 1)
    return settled, r2


def shift_check(pump, sch0, sch1, n=MOVES):
    """PR3: walk born = () (sch0) and born = (1,) (sch1) side by side and
    return the first k >= 1 at which sch0's shape after k + 1 moves differs
    from sch1's after k, or None."""
    npl = CT.supply()
    w0 = TP.PWalk(npl, sch0, pump, TP.PERITEM, DCAP, seed=SEED, tag="s0")
    w1 = TP.PWalk(npl, sch1, pump, TP.PERITEM, DCAP, seed=SEED, tag="s1")
    w0.apply(w0.menu()[1][0])
    for k in range(1, n + 1):
        w0.apply(w0.menu()[1][0])
        w1.apply(w1.menu()[1][0])
        if w0.shape() != w1.shape() or w0.T != w1.T:
            return k
    return None


# --------------------------------------------------------- S0 forced fails
def s0_forced():
    section("S0  FORCED FAILURES -- every detector fired on a fabricated "
            "input")
    a = (set([(2, 0), (3, 0)]), (2,))
    b = (set([(2, 0)]), (2,))
    ok(a != b, "S0 (i): a strand-set difference read as equal")
    print("  (i)   strand-set difference detector fires:  %s != %s"
          % (sorted(a[0]), sorted(b[0])))
    late = [(2, 0)]
    ok(not (len(late) == 1 and late[0] == (1, 0)),
       "S0 (ii): a (2, 0) riser read as (1, 0)")
    print("  (ii)  riser-not-(1,0) detector fires:          %s" % late)
    doctored = TP.Pump("doctored", [1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 18,
                                    20, 22, 24, 26, 28, 30], 40)
    ok(first_wide(doctored, upto=30) == 7,
       "S0 (iii): the wide-door read missed the doctored ladder's step")
    ok(first_wide(TP.p_exact(), upto=200) is None,
       "S0 (iii): the exact ladder read as carrying a wide door")
    print("  (iii) wide-door read: doctored ladder x1 = %d, exact ladder "
          "none -> both fired." % first_wide(doctored, upto=30))


# ---------------------------------------------------------- S1 the controls
def s1_controls(lads):
    section("S1  POSITIVE CONTROLS -- the recorded counts, the parent's four "
            "firings, and the\n    hand margins, before any verdict")
    std = sched_of("d*s (standing)", dict(PRICES)["d*s (standing)"], (1,))
    recorded = {"Q_2 w1": 0, "Z[sqrt2] w1": 2, "K5ram2 w2": 3, "Z[i] w3": 5,
                "Z[sqrt-3] w1": 2, "Z[2^1/4] w2": 6, "Z[2^1/8] w4": 15}
    lad = dict(lads)
    for tag, want in recorded.items():
        a = CT.census_lad(std, lad[tag], CT.supply(), SEED)[0]
        ok(a == want, "S1 (a): %s census %d against recorded %d"
           % (tag, a, want))
    print("  (a) the census at born = (1,) reprints all seven recorded "
          "headed counts.")
    # (b) the parent's four firings: (2, 0) risers at born = (1,) sit at the
    #     exact ladder and the four violating prices, nowhere else
    fired = []
    for ptag, fn in PRICES:
        sch = sched_of(ptag, fn, (1,))
        settled, r = read_settled(lad["psi 2,1 w0"], sch)
        ok(settled, "S1 (b): the exact ladder unsettled at %s" % ptag)
        if r["late"][0] != (1, 0):
            fired.append((ptag, r["late"][0]))
    viol = sorted(p for p, f in PRICES if undercutters(sched_of(p, f, (1,))))
    ok(sorted(p for p, _ in fired) == viol,
       "S1 (b): the exact ladder's (2, 0) risers %s are not the violating "
       "prices %s" % (fired, viol))
    print("  (b) the parent's four firings reproduced on the exact ladder: "
          "%s" % fired)
    # (c) the hand margins at Q_2 w1 under d * sigma^2
    fn = dict(PRICES)["d*s^2"]
    pump = lad["Q_2 w1"]
    bar, tail, over = CT.bar_door(pump)
    ok((bar, tail, len(over)) == (2, 1, 1) and CT.bar_rung(pump) == 4,
       "S1 (c): Q_2 w1 reads bar %d tail %d overshoots %d rung %d against "
       "the hand's 2, 1, 1, 4" % (bar, tail, len(over), CT.bar_rung(pump)))
    want = {(): (2, [2], set([(2, 0), (3, 0)])),
            (1,): (2, [2], set([(2, 0), (3, 0)])),
            (1, 2): (1, [2], set([(3, 0)]))}
    for btag, born in BORN:
        sch = sched_of("d*s^2", fn, born)
        a, dep, strands, trip = CT.census_lad(sch, pump, CT.supply(), SEED)
        ok(not trip and (a, dep, CT.keyset(strands)) == want[born],
           "S1 (c): Q_2 w1 / d*s^2 census at %s reads %s against the hand's "
           "%s" % (btag, (a, dep, sorted(CT.keyset(strands))), want[born]))
        settled, r = read_settled(pump, sch)
        ok(settled and strand_key(r) == (want[born][2], tuple(want[born][1]))
           and r["late"] == [(1, 0)],
           "S1 (c): Q_2 w1 / d*s^2 walk at %s reads %s riser %s against the "
           "hand's %s riser (1, 0)"
           % (btag, strand_key(r), r["late"], want[born]))
        print("  (c) Q_2 w1 / d*s^2 at %-10s census A = %d depths %s strands "
              "%s; walk equal, riser %s -- the hand's figures."
              % (btag, a, dep, sorted(CT.keyset(strands)), r["late"][0]))


# ------------------------------------------------- S2 the census invariance
def s2_census(lads):
    section("S2  THE CENSUS ACROSS THE BORN DIAL -- born = () against "
            "born = (1,) at every\n    price and ladder")
    same, diff = 0, []
    for ptag, fn in PRICES:
        s0 = sched_of(ptag, fn, ())
        s1 = sched_of(ptag, fn, (1,))
        for ltag, pump in lads:
            c0 = CT.census_lad(s0, pump, CT.supply(), SEED)
            c1 = CT.census_lad(s1, pump, CT.supply(), SEED)
            if c0[:3] == c1[:3]:
                same += 1
            else:
                diff.append((ptag, ltag, c0[:2], c1[:2]))
    print("  cells with an identical census at both born sets: %d of %d"
          % (same, same + len(diff)))
    print("  K6 (a census that moved): %s" % (diff or "none"))
    return diff


# ----------------------------------------------------------- S3 the probe
def s3_probe(lads):
    section("S3  THE PROBE -- the walked strand set at born = () against "
            "born = (1,),\n    per-item clock, %d prices x %d ladders"
            % (len(PRICES), len(lads)))
    print("  %-16s %-14s %-9s %-9s %-7s %-7s %s"
          % ("price", "ladder", "riser ()", "riser (1)", "count", "same",
             "depths"))
    k1, k2, unsettled, cells, shifts = [], [], [], 0, []
    for ptag, fn in PRICES:
        s0 = sched_of(ptag, fn, ())
        s1 = sched_of(ptag, fn, (1,))
        meets = not undercutters(s1)
        for ltag, pump in lads:
            st0, r0 = read_settled(pump, s0)
            st1, r1 = read_settled(pump, s1)
            if not (st0 and st1):
                unsettled.append((ptag, ltag, st0, st1))
                print("  %-16s %-14s %-9s %-9s unsettled at %s"
                      % (ptag, ltag, r0["late"][:1], r1["late"][:1],
                         "born=()" if not st0 else "born=(1,)"))
                continue
            cells += 1
            same = strand_key(r0) == strand_key(r1)
            if not same:
                k1.append((ptag, ltag, sorted(strand_key(r0)[0]),
                           sorted(strand_key(r1)[0])))
            if r0["late"][0] != (1, 0):
                k2.append((ptag, ltag, r0["late"][0]))
            print("  %-16s %-14s %-9s %-9s %-7d %-7s %s"
                  % (ptag, ltag, r0["late"][0], r1["late"][0],
                     len(r1["strand"]), "yes" if same else "NO",
                     r1["depths"]))
            if meets:
                k = shift_check(pump, s0, s1)
                if k is not None:
                    shifts.append((ptag, ltag, k))
    print("\n  cells settled at both born sets: %d; named unsettled: %d"
          % (cells, len(unsettled)))
    print("  K1 (strand set differs between born sets): %s" % (k1 or "none"))
    print("  K2 (a born = () riser that is not (1, 0)): %s" % (k2 or "none"))
    print("  K4 (the shift parting at a price meeting the born opening): %s"
          % (shifts or "none"))
    return k1, k2, shifts, unsettled


# ------------------------------------------------- S4 the lemma's observables
def s4_lemma(lads):
    section("S4  THE OVERTAKING LEMMA at born = (1,) -- the riser on every "
            "ladder with a\n    wide door, and the cells the open clause "
            "asked for")
    wide = dict((ltag, first_wide(pump)) for ltag, pump in lads)
    print("  first wide door x1 per ladder: %s"
          % ", ".join("%s: %s" % (t, x) for t, x in wide.items()))
    ok(sum(1 for x in wide.values() if x is None) == 1
       and wide["psi 2,1 w0"] is None,
       "S4: the exact ladder is not the only ladder without a wide door")
    k3, exact_rows, asked, off, cells = [], [], [], [], 0
    for ptag, fn in PRICES:
        sch = sched_of(ptag, fn, (1,))
        cut = undercutters(sch)
        for ltag, pump in lads:
            settled, r = read_settled(pump, sch)
            if not settled:
                continue
            cells += 1
            a, dep, strands, trip = CT.census_lad(sch, pump, CT.supply(),
                                                  SEED)
            bar, tail, over = CT.bar_door(pump)
            riser = r["late"][0]
            if wide[ltag] is None:
                want = (cut[0], 0) if cut else (1, 0)
                exact_rows.append((ptag, riser, want, a))
                if riser != want or a != 0:
                    k3.append(("exact", ptag, riser, want, a))
                continue
            if riser != (1, 0):
                k3.append(("wide", ptag, ltag, riser))
            if cut and a > 0 and over:
                match = (len(r["strand"]) == a and r["depths"] == dep
                         and CT.keyset(r["strand"]) == CT.keyset(strands))
                asked.append((ptag, ltag, a, dep, riser, match))
                if not match:
                    off.append((ptag, ltag, a, len(r["strand"])))
    print("\n  settled cells read: %d" % cells)
    print("  the exact ladder, riser against the lemma's (least "
          "undercutting degree, 0):")
    for ptag, riser, want, a in exact_rows:
        print("      %-16s riser %-8s predicted %-8s census %d"
              % (ptag, riser, want, a))
    print("  cells of the open clause's kind -- a violating price, a "
          "non-empty census, a bar\n  above the tail -- %d found, each "
          "with its riser and whether the walk prints its census:"
          % len(asked))
    for row in asked:
        print("      %-16s %-14s A = %-3d depths %-12s riser %s  census "
              "printed: %s" % row)
    print("  K3 (a wide-door riser not (1, 0), an exact-ladder riser off "
          "the lemma, or an asked\n      cell off its census): %s"
          % (k3 + off or "none"))
    return k3, off, asked


# --------------------------------------------------- S5 the born=(1,2) dial
def s5_born_two(lads):
    section("S5  THE DIAL AS A FORMULA INPUT -- born = (1, 2): the walk "
            "against the census\n    recomputed with degree 2 born")
    k5, moved, cells, unsettled = [], 0, 0, 0
    for ptag, fn in PRICES:
        s2 = sched_of(ptag, fn, (1, 2))
        s1 = sched_of(ptag, fn, (1,))
        for ltag, pump in lads:
            c2 = CT.census_lad(s2, pump, CT.supply(), SEED)
            c1 = CT.census_lad(s1, pump, CT.supply(), SEED)
            if c2[3]:
                unsettled += 1
                continue
            if c2[:3] != c1[:3]:
                moved += 1
            settled, r = read_settled(pump, s2)
            if not settled:
                unsettled += 1
                continue
            cells += 1
            if (len(r["strand"]) != c2[0] or r["depths"] != c2[1]
                    or CT.keyset(r["strand"]) != CT.keyset(c2[2])):
                k5.append((ptag, ltag, c2[:2], len(r["strand"]),
                           r["depths"]))
    print("  settled cells: %d (%d unsettled, not read); censuses that "
          "moved against born = (1,): %d" % (cells, unsettled, moved))
    print("  K5 (a settled cell off its own census): %s" % (k5 or "none"))
    return k5, moved


# --------------------------------------------------- S6 the partition sweep
def s6_partitions(lads):
    section("S6  COARSER CLOCKS at the standing price -- born = () against "
            "born = (1,) over\n    ten ladders x five partitions")
    fn = dict(PRICES)["d*s (standing)"]
    s0 = sched_of("d*s", fn, ())
    s1 = sched_of("d*s", fn, (1,))
    diff, cells, unsettled = [], 0, 0
    for ltag, pump in lads[:len(HL.LEGAL)]:
        for ptag, cls in BC.PARTITIONS:
            st0, r0 = read_settled(pump, s0, cls)
            st1, r1 = read_settled(pump, s1, cls)
            if not (st0 and st1):
                unsettled += 1
                continue
            cells += 1
            if strand_key(r0) != strand_key(r1):
                diff.append((ltag, ptag, sorted(strand_key(r0)[0]),
                             sorted(strand_key(r1)[0])))
    print("  cells settled at both born sets: %d (%d not); strand sets that "
          "differ: %s" % (cells, unsettled, diff or "none"))
    return diff


# ---------------------------------------------------- S7 the window control
def s7_window(lads, unsettled):
    section("S7  THE WINDOW CONTROL -- every cell unsettled at either born "
            "set re-read at\n    %d and %d" % (LONG, LONGER))
    if not unsettled:
        print("  no cell read unsettled.")
        return
    lad = dict(lads)
    for ptag, ltag, st0, st1 in unsettled:
        fn = dict(PRICES)[ptag]
        bar = CT.bar_door(lad[ltag])[0]
        for btag, born in BORN[:2]:
            sch = sched_of(ptag, fn, born)
            a = CT.census_lad(sch, lad[ltag], CT.supply(), SEED)[0]
            line = "still unsettled at %d" % LONGER
            for n in (LONG, LONGER):
                r = CT.certify(lad[ltag], sch, CT.supply(), TP.PERITEM,
                               n=n, bar=bar)
                if r["cross"] is not None and len(r["strand"]) == a:
                    line = "settles at %d on its census (%d), riser %s" % (
                        n, a, r["late"][:1])
                    break
            print("    %-16s %-14s %-10s %s" % (ptag, ltag, btag, line))


def main():
    lads = ladders()
    s0_forced()
    s1_controls(lads)
    k6 = s2_census(lads)
    ok(not k6, "K6: the census moved with the born set at degree 1: %s" % k6)
    k1, k2, shifts, uns = s3_probe(lads)
    ok(not k1, "K1: the strand set differs between born sets: %s" % k1)
    ok(not k2, "K2: a born = () riser that is not (1, 0): %s" % k2)
    ok(not shifts, "K4: the shift parts at a price meeting the born "
       "opening: %s" % shifts)
    k3, off, asked = s4_lemma(lads)
    ok(not k3 and not off, "K3: the overtaking lemma fails: %s" % (k3 + off))
    ok(asked, "S4: no cell of the open clause's kind was found, so the "
       "clause is unread here")
    k5, moved = s5_born_two(lads)
    ok(not k5, "K5: a born = (1, 2) cell off its own census: %s" % k5)
    ok(moved > 0, "S5: born = (1, 2) moved no census, so the dial control "
       "is vacuous")
    d6 = s6_partitions(lads)
    ok(not d6, "K1 (partitions): the strand set differs: %s" % d6)
    s7_window(lads, uns)
    section("%d checks" % CHECKS[0])


if __name__ == "__main__":
    main()
