"""explore_headed_block.py -- WHAT A RAMP LEAVES BEHIND, BLOCK BY BLOCK.

THE QUESTION. The clock is two dials -- who shares a TICK and who shares a
LADDER -- and a ring sits at the cell between the family's ends: one tick per
residue characteristic, per-place ladders inside a block
(explore_block_clock.py). That file dialled the tick with CONSTANT-GAP and
GROWING ladders and settled the RUNAWAY count: it is the BLOCK count wherever
the recurrent cost climbs and 1 wherever it is flat, because a recurrent mover
lands on its own next rung and a bounded ladder's cost is therefore flat. The
same reading then derives that a HEAD buys only a TRANSIENT of the climbing
regime, every psi ladder flattening at its splice, so a headed ladder must
read one runaway too.

What neither the derivation nor any cell so far reads is the STRAND count. A
ramp is the rotating regime running for a bounded time, and what a rotation
leaves behind when it stops is items carried above exponent 1 and then priced
out -- one per block that lost. The runaway count is settled; the population
beside it is not.

The ladders are psi's own orbits with their splices, which
explore_headed_ladder.py generates from (p, e, w): the ramp 1, p, ..., p^t,
then the splice at p^t + e + w, then the constant gap e forever. Those are the
ladders arithmetic actually supplies, and the crossing depth -- one above the
last step wider than the tail -- is where an item is paying its tail forever.

WHAT IS BEING CROSSED, AND WHY IT IS NEW. Every headed cell to date ran at a
GLOBAL or a PER-ITEM clock; every block cell to date ran a splice-free ladder.
This file crosses the two dials at once, which is the ring's actual shape run
with the ring's actual ladders, and it does it twice: S2 gives every item one
headed ladder and dials the partition, S4 puts an unramified and a ramified
ladder inside ONE block, which is what two places over one rational prime are.

THE SLATE, frozen before any engine code.

 PR1 ONE RISER, HEAD OR NO HEAD. At every headed ladder and every partition
     exactly one item is rising over the trailing window, and its exponent
     stands at or above its ladder's crossing depth -- the splice passed, the
     tail flat, one global minimum holding forever.
 PR2 THE STRAND POPULATION MOVES WITH THE BLOCK COUNT. Strands -- items above
     exponent 1 that are not rising -- are nondecreasing as the partition
     refines, and strictly more numerous at four blocks than at one.
 PR3 THE HEAD GRADES THE DEPTHS, AND A WIDER HEAD GRADES THEM FURTHER. At a
     headed ladder the strands do not all sit at one exponent, against a
     constant-gap ladder's single strand depth; and the number of distinct
     strand depths is nondecreasing in the head width w.
 PR4 THE BUDGET SURVIVES THE HEAD. The flat tail minimum is the runaway's own
     f(degree, TAIL gap) -- its ladder's tail, since the runaway is past its
     splice -- at every cell whose tail has stopped moving.

 KILL-SHAPES, as observables this rig PRINTS.
  K1 two or more items rising at a cell where every item above exponent 1
     stands at or above the ladder's crossing depth. The derivation claims a
     constant recurrent cost past the splice, so that print refutes it
     outright.
  K2 a strand count that does NOT move with the block count -- identical at
     two, three and four blocks at every headed ladder. The rotation would
     then leave nothing and the transient would be invisible in the limit.
     (Frozen exactly as written, and F4 records that this wording omits the
     one-block cell and so fires where the meaning does not hold. The rig
     prints the frozen reading and the strict one side by side rather than
     quietly substituting the second, which is what it did before the audit.)
  K3 a flat tail minimum differing from the runaway's own f(d, tail gap).
  K4 every strand of every headed cell at ONE depth. The head would then buy
     no grading, and the constant-gap reading would cover the ramp too.

 TRANSPLANT MARKS -- intuitions imported from a neighbouring parameter value,
 flagged as such before the run.
  PR2 is imported from explore_block_clock.py F4, measured at w = 0 ladders,
  and carried across to w >= 1. Its own transplant note there stands: the
  monotonicity has no derivation behind it, a narrower door arguing the count
  up while a change of WINNER can move the strand set either way, and a head
  is exactly a device for changing the winner.
  PR3 is imported from explore_headed_ladder.py F5/F7, which measured the
  depth spread at a PER-ITEM clock. A block clock shares a tick inside a
  block, and a shared tick is what hides an item's own gap from the price
  (explore_tick_pump.py F9), so the spread has no derivation here at
  all -- it is the prediction most likely to be wrong.

 THE HAND-ATTACK, on paper before the engine, found the cell's real hazard is
 not a prediction but the WINDOW: a splice at depth 21 (Z[2^(1/8)], w = 4) is
 unreachable by a walk that never climbs that far, and PR1 would then be
 confirmed vacuously -- one riser, but rising on its head rather than on its
 tail. The crossing depths run 4 to 21 and are printed against the deepest
 exponent every cell reaches, so a vacuous confirmation is visible rather
 than silent. (This is what sized the cell: 120 moves is the family's own
 figure and it is what the sizing probe was run at.) The second hazard is the
 opposite one -- that the strand population is a transient of the window
 length itself -- so S3 re-reads every count at a window three times longer,
 which is the only way a count can say whether it is a fact about the walk or
 about where we stopped looking.

 SECTIONS.
  S1  the positive control, run before any verdict is read: psi's splice-free
      orbit against the family's certified exact ladder, then the block dial's
      two ends against GLOBAL and PERITEM at the headed ladders, move for
      move.
  S2  the sweep -- ten psi ladders x five partitions, risers against strands,
      the strand depths, the budget.
  S3  the window control: every strand count re-read at 400 moves.
  S4  the ring's own shape with the head put back -- an unramified and a
      ramified ladder inside ONE block.
  S5  the mechanism the sweep suggested, under a SECOND slate frozen after
      the sweep and before that section's engine (PR5-PR8, in its own
      docstring). One of the four is refuted, which is F7.

RUN RECORD. One process, 0.5s wall, peak working set 42.7 MB under
memwatch.py's 512 MB ceiling. Ten psi ladders x five partitions at one
schedule (alpha=1, b=2, m=1, born={1}), a supply of two items at every degree
to 400, seed (9, 13), 120 moves a cell and 400 at S3's re-read.

F1 THE POSITIVE CONTROL, read before any verdict below (S1). psi's
   splice-free orbit at (2, 1) IS the family's certified exact ladder, member
   for member to 200. The block dial's two ends against the family's own two
   clocks -- one block against GLOBAL, singletons against PERITEM -- agree
   menu for menu and seat for seat at all seven HEADED ladders, 120 moves
   each, 0 partings. So what the middle of the dial reads below is the
   partition's and not psi's.

F2 ONE RISER AT ALL 50 CELLS, AND NOT VACUOUSLY (S2, PR1; K1 at 0). Every
   cell carries exactly one rising item, and every cell's runaway stands past
   its ladder's crossing depth -- deepest exponents 121 to 869 against
   crossings 1 to 21 -- so the reading is taken where the tail is flat and
   not on the head. The derivation holds at the crossed cell: a head buys a
   TRANSIENT of the rotating regime and never a second infinite coordinate.
   WHAT THE INSTRUMENT HAD TO BE FIXED FOR. "Past the splice" was first read
   of every item above exponent 1, which no STRAND can ever satisfy -- a
   strand is precisely an item that did not get there -- so the test would
   have called every cell that has anything to say vacuous. PR1 is a claim
   about the recurrent cost of the item still moving, and that item's own
   depth is the whole of what tests it.

F3 THE BUDGET SURVIVES THE HEAD (S2, PR4; K3 at 0 of 50). The flat tail
   minimum is the runaway's own f(degree, TAIL gap) at every cell: 1, 2, 3,
   1, 2, 2, 2, 2, 4, 8 across the ten ladders, each the ladder's tail gap at
   the degree-1 runaway. The head moves nothing in the budget, which is the
   half of the min-over-products law that already survived both ends of the
   dial and now survives a ramp.

F4 THE STRAND COUNT IS THE BLOCKS THAT LOST, AND THE TAIL DECIDES WHETHER
   THERE ARE ANY (S2, PR2). The count is nondecreasing
   at all ten ladders, and at Z[i] w3, Z[2^(1/4)] w2 and Z[2^(1/8)] w4 it is
   0, 1, 2, 3 at one, two, three and four blocks -- exactly the blocks that
   did not win.
   K2 FIRED AT 3 OF 7 HEADED LADDERS AS FROZEN AND ITS MEANING SURVIVES AT
   ONE, which is a fact about the kill's wording and is why both counts are
   printed. As written it reads "identical at two, three and four blocks",
   and Z[sqrt(2)] and Z[sqrt(-3)] are: 0, 1, 1, 1. But both MOVED from the
   one-block cell, where a rotation that leaves anything at all first shows,
   so the transient is plainly visible at those two and the kill's stated
   meaning -- the rotation leaves nothing -- does not carry. The observable
   was frozen one cell too narrow, reading the dial's middle and omitting the
   end that discriminates. Only Q_2 w1 is deaf to the whole dial, and it is
   the interesting one: it is HEADED and strands nothing. Its
   tail gap is 1, so its budget is f(1, 1) = 1, the least price this schedule
   has, and no second item is ever affordable beside the runaway. So a ramp
   buys a strand population only where the TAIL leaves room under the
   budget -- genuine ramification and not merely a head.

F5 THE HEAD IS TWO THINGS AND PR3 NAMED THE WRONG ONE (S2, PR3 refuted; K4
   fired at 5 ladders and its inference did not survive). The depths are
   graded by the SEAT p^t -- the ramp's length -- and not by the width w. The
   three (p, e) = (2, 2) ladders at w = 1, 2, 3 share the single depth {3}
   while their strand totals run 5, 8, 11; Z[2^(1/4)] at w = 2 and seat 4
   shows {3, 5} and Z[2^(1/8)] at w = 4 and seat 8 shows {3, 5, 9}. So w = 3
   gives ONE depth against w = 2's TWO, and PR3's monotonicity in the width
   is refuted outright. THE WIDTH SETS HOW MANY STRANDS THERE ARE AND THE
   SEAT SETS WHERE THEY REST: two coordinates of one word, each paying a
   different half of the population, which is why dialling "the head" as a
   scalar could not have found either. K4's own observable fired at five
   ladders, and the meaning bundled into it -- that the head buys no
   grading -- does not survive: those five are exactly the ladders whose ramp
   has one strandable rung, so the grading is there and there is nothing for
   it to grade.

F6 WHERE A STRAND RESTS (S5, PR5, PR6, PR7 at 0 off over 67 strands). e - 1
   is a ladder member at 67 of 67, and at or below the seat at 62 of 62
   headed ones -- so ON A HEADED LADDER a strand rests one above a RAMP RUNG,
   e = p^j + 1, and the ramp is the whole of what a partition can strand. The
   five strands outside that scope are the splice-free ramp psi(2, 3), which
   has no seat for PR6 to read, and the e = p^j reading of them is inspection
   and not a print. The fill is
   top-down: refining the partition never drops a depth and never adds one
   deeper than a depth already held, so the deepest strandable rung goes
   first and the shallower ones fill in behind it.

F7 AND THE MECHANISM READ OFF THAT WAS WRONG (S5, PR8 refuted at 7 of the 7
   ladders carrying strands). F6's shape says nothing about how the resting
   place was reached, and the reading it invites -- that a strand is an
   untouched OPENING, seated at its block's own tick plus one and never
   moved -- is false: 63 of the 67 strands MOVED, one to four moves each, and
   the only ones that did not are four of Z[sqrt(-3)]'s five, whose seat is 1
   and whose single strandable depth an opening can land on directly. A
   strand CLIMBS the ramp's cheap early rungs and stalls one above the rung
   whose next door outruns the budget. A stalled climber and an untouched
   opening leave the identical seat, so nothing but a move count separates
   them, and the count is in the rig because the seat alone had already
   persuaded me.

F8 THE RING'S OWN SHAPE WITH THE HEAD PUT BACK, AND THE HEAD BUYS NOTHING
   THERE (S4). An unramified ladder in slot 0 and a HEADED ramified one in
   slot 1, both on one tick: the runaway is slot 0 at all seven widths, the
   wide item is never carried above exponent 1, the flat minimum reads
   f(1, 1) = 1, and the cell strands NOTHING. So the ramp does not get the
   wide place seated -- the shared tick is driven by the narrow ladder, and
   the wide item's door is the whole of that tick. The strand population of
   F4 needs items on DIFFERENT ticks, which is the partition and not the
   ladder: what a block clock strands, it strands across blocks and never
   inside one.

F9 THE POPULATION IS NOT THE WINDOW'S (S3). Every strand count is identical
   at 120 and at 400 moves, 0 of 28 cells moving, depths included. A count
   read at one window is a fact about the walk rather than about where the
   reading stopped.
"""

import os
import sys

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_block_clock as BC
import explore_headed_ladder as HL
import explore_price_schedule as PS
import explore_tick_pump as TP


MOVES = TP.WALK_N        # the family's own figure, and what the sizing probe ran
LONG = 400               # S3's window, over three times the standing one
DCAP = TP.WALK_DCAP
SEED = TP.GRID_SEED

PARTITIONS = BC.PARTITIONS


def ok(cond, msg):
    if not cond:
        raise AssertionError(msg)


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ------------------------------------------------------------- the ladder set
def ladders():
    """psi's own orbits, splice-free and headed, each with its crossing depth
    and its tail gap read off the ladder rather than off (p, e, w)."""
    out = []
    for tag, p, e, w in HL.LEGAL:
        pump = HL.psi_ladder(tag, p, e, w)
        _, tail, _ = HL.profile(pump)
        out.append((tag, w, pump, tail, HL.cross_from(pump)))
    return out


# --------------------------------------------------------------- observables
def read(pump, cls, sch, npl, cross, n=MOVES, lad=None):
    """One cell, split into the runaway and what the ramp left behind.

    Rising is read at the HALF window, which is the window explore_block_clock
    F0 established as the readable one -- a ladder whose era outruns the short
    trailing window reads zero risers on a walk that is plainly still climbing.
    An item absent at the mark is excluded there rather than baselined at 1,
    so an item seated ONCE is not counted as one that moved.

    `crossed` is read of the RUNAWAY and not of every item above exponent 1.
    The first reading asked the whole deep population to stand past the
    splice, which no strand can ever do -- a strand is precisely an item that
    did not get there -- so it would have called every interesting cell
    vacuous. PR1 is a claim about the recurrent cost of the item that is still
    moving, and that item's own depth is what tests it."""
    w, mins, mark, half = BC.walk(npl, sch, pump, cls, lad=lad, n=n)
    run, after = BC.rising(w, half)
    deep = w.deep_items()
    keys = set((d, i) for d, i, _, _ in run)
    strand = [(d, i, e) for d, i, e in deep if (d, i) not in keys]
    depths = sorted(set(e for _, _, e in strand))
    maxe = max([e for _, _, e in deep] or [0])
    return {"w": w, "deep": deep, "run": run, "strand": strand,
            "depths": depths, "maxe": maxe, "after": after,
            "flat": BC.flat_min(mins),
            "crossed": all(e >= cross for _, _, _, e in run),
            "blocks": len(set(cls((d, i)) for d, i, _, _ in run))}


# ------------------------------------------------------- S1 positive control
def s1_control(sch, npl):
    section("S1  POSITIVE CONTROL -- psi's orbit against a certified ladder, "
            "then the block\n    dial's two ends against the family's own two "
            "clocks, before any verdict")
    ref = TP.p_exact()
    mine = HL.psi_ladder("psi 2,1 w0", 2, 1, 0)
    ok(mine.S[:200] == ref.S[:200],
       "psi's splice-free orbit at (2, 1) is not the exact ladder")
    print("  (a) psi(2, 1, w=0) IS the family's exact ladder, member for "
          "member to 200.")
    print("\n  (b) one block against GLOBAL and singletons against PERITEM, "
          "at the HEADED\n      ladders -- so anything the middle of the dial "
          "reads below is the\n      partition's and not psi's.")
    print("\n  %-15s %-11s %-7s %s" % ("ladder", "end", "moves", "agreement"))
    for tag, p, e, w in HL.HEADED:
        pump = HL.psi_ladder(tag, p, e, w)
        for etag, mine_cls, theirs in (("1 block", BC.blocks(1), TP.GLOBAL),
                                       ("singletons", TP.PERITEM, TP.PERITEM)):
            a = TP.PWalk(npl, sch, pump, mine_cls, DCAP, seed=SEED)
            b = TP.PWalk(npl, sch, pump, theirs, DCAP, seed=SEED)
            for _ in range(MOVES):
                ca, ta = a.menu()
                cb, tb = b.menu()
                ok(ca == cb and ta == tb,
                   "%s/%s: the menus parted" % (tag, etag))
                a.apply(ta[0])
                b.apply(tb[0])
                ok(a.seat == b.seat, "%s/%s: the seats parted" % (tag, etag))
            print("  %-15s %-11s %-7d %s" % (tag, etag, MOVES, "equal"))


# -------------------------------------------------------------- S2 the sweep
def s2_sweep(sch, npl):
    section("S2  THE SWEEP -- ten psi ladders x five partitions: the runaway, "
            "what the\n    ramp left behind, and at what depths it left it")
    print("  supply: two items at every degree to %d; seed %s; %d moves a "
          "cell." % (DCAP, SEED, MOVES))
    print("  'past' is the RUNAWAY standing at or above the ladder's crossing")
    print("  depth -- its splice passed, its tail flat. A cell that is not")
    print("  past confirms PR1 vacuously and says so.")
    print("\n  %-15s %-3s %-10s %-6s %-6s %-5s %-7s %-7s %-8s %-8s %s"
          % ("ladder", "w", "partition", "cross", "maxe", "past", "above1",
             "risers", "strands", "flatmin", "strand depths"))
    res, k1, k3, k4 = {}, [], [], []
    for tag, w, pump, tail, cross in ladders():
        for ptag, cls in PARTITIONS:
            c = read(pump, cls, sch, npl, cross)
            res[(tag, ptag)] = c
            if len(c["run"]) > 1 and c["crossed"]:
                k1.append((tag, ptag, len(c["run"]), c["blocks"]))
            pred = None
            if c["flat"] is not None and len(c["run"]) == 1:
                d = c["run"][0][0]
                pred = sch.price(d, tail)
                if pred != c["flat"]:
                    k3.append((tag, ptag, c["flat"], pred))
            print("  %-15s %-3d %-10s %-6d %-6d %-5s %-7d %-7d %-8d %-8s %s"
                  % (tag, w, ptag, cross, c["maxe"],
                     "yes" if c["crossed"] else "NO", len(c["deep"]),
                     len(c["run"]), len(c["strand"]),
                     c["flat"] if c["flat"] is not None else "moving",
                     ", ".join(str(x) for x in c["depths"]) or "none"))
        print()
    for tag, w, pump, tail, cross in ladders():
        if w == 0:
            continue
        dep = set()
        for ptag, _ in PARTITIONS:
            dep |= set(res[(tag, ptag)]["depths"])
        if len(dep) <= 1:
            k4.append((tag, sorted(dep)))
    return res, k1, k3, k4


def s2_verdicts(res, k1, k3, k4):
    print("  PR1 (K1) -- crossed cells carrying more than one riser: %d"
          % len(k1))
    for tag, ptag, n, nb in k1:
        print("      %-15s %-10s %d risers over %d blocks" % (tag, ptag, n, nb))
    print("  PR4 (K3) -- cells whose flat minimum is not the runaway's own "
          "f(d, tail): %d" % len(k3))
    for tag, ptag, got, pred in k3:
        print("      %s / %s: %s against %s" % (tag, ptag, got, pred))

    print("\n  PR2 -- the strand count as the partition refines:")
    print("  %-15s %-3s %-8s %-4s %-4s %-4s %-9s %s"
          % ("ladder", "w", "1 block", "2", "3", "4", "per item", "verdict"))
    k2, k2loose, bad2 = [], [], []
    for tag, w, pump, tail, cross in ladders():
        row = [len(res[(tag, p)]["strand"]) for p, _ in PARTITIONS]
        # K2 AS FROZEN reads "identical at two, three and four blocks" and
        # nothing else; the STRICT reading adds the one-block cell, which is
        # where a rotation that leaves something first shows. Both are
        # printed because they disagree, and the frozen one is the kill.
        mid = row[1:4]
        if w and len(set(mid)) == 1:
            k2loose.append((tag, row))
            if mid[0] == row[0]:
                k2.append((tag, row))
        mono = all(b >= a for a, b in zip(row, row[1:]))
        if not mono or row[3] <= row[0]:
            bad2.append((tag, row))
        print("  %-15s %-3d %-8d %-4d %-4d %-4d %-9d %s"
              % tuple([tag, w] + row +
                      ["as predicted" if (mono and row[3] > row[0])
                       else "NOT nondecreasing" if not mono
                       else "flat across the dial"]))
    print("\n  K2 AS FROZEN -- headed ladders flat at two, three and four "
          "blocks: %d" % len(k2loose))
    for tag, row in k2loose:
        print("      %-15s %s%s" % (tag, row,
                                    "" if row[1] == row[0]
                                    else "   (but 1 block -> 2 blocks MOVED)"))
    print("  K2 STRICT -- and deaf to the one-block cell too, which is where "
          "a rotation\n           that leaves anything at all first shows: %d"
          % len(k2))
    for tag, row in k2:
        print("      %-15s %s" % (tag, row))

    print("\n  PR3 (K4) -- distinct strand depths against the head width:")
    print("  %-15s %-3s %-8s %-4s %-4s %-4s %-9s %s"
          % ("ladder", "w", "1 block", "2", "3", "4", "per item",
             "depths seen"))
    for tag, w, pump, tail, cross in ladders():
        row = [len(res[(tag, p)]["depths"]) for p, _ in PARTITIONS]
        dep = sorted(set().union(*[set(res[(tag, p)]["depths"])
                                   for p, _ in PARTITIONS]))
        print("  %-15s %-3d %-8d %-4d %-4d %-4d %-9d %s"
              % tuple([tag, w] + row +
                      [", ".join(str(x) for x in dep) or "none"]))
    print("\n  K4 -- headed ladders whose strands all sit at one depth: %d"
          % len(k4))
    for tag, dep in k4:
        print("      %-15s %s" % (tag, dep or "no strands at all"))
    return k2, k2loose, bad2


# ----------------------------------------------------- S3 the window control
def s3_window(sch, npl, res):
    section("S3  THE WINDOW CONTROL -- every count re-read at %d moves, "
            "because a\n    population that is a transient of the window is "
            "not a population" % LONG)
    print("  %-15s %-10s %-13s %-13s %s"
          % ("ladder", "partition", "strands @%d" % MOVES,
             "strands @%d" % LONG, "depths @%d" % LONG))
    moved = []
    for tag, w, pump, tail, cross in ladders():
        if w == 0:
            continue
        for ptag, cls in PARTITIONS[:4]:
            c = read(pump, cls, sch, npl, cross, n=LONG)
            was = len(res[(tag, ptag)]["strand"])
            now = len(c["strand"])
            if was != now:
                moved.append((tag, ptag, was, now))
            print("  %-15s %-10s %-13d %-13d %s"
                  % (tag, ptag, was, now,
                     ", ".join(str(x) for x in c["depths"]) or "none"))
        print()
    print("  cells whose strand count moved with the window: %d" % len(moved))
    for t in moved:
        print("      %s / %s: %d at %d moves, %d at %d"
              % (t[0], t[1], t[2], MOVES, t[3], LONG))
    return moved


# ----------------------------------------------- S4 the ring's shape, headed
def s4_mixed(sch, npl):
    section("S4  THE RING'S OWN SHAPE WITH THE HEAD PUT BACK -- an unramified "
            "and a\n    ramified ladder inside ONE block, which is what two "
            "places over one\n    rational prime are")
    print("  cls puts both slots of a degree on one tick; lad gives slot 0 the")
    print("  unramified ladder psi(2, 1) and slot 1 a HEADED one. The")
    print("  constant-gap version of this cell puts the runaway in slot 0 at")
    print("  every width and never carries the wide item above exponent 1 at")
    print("  all (explore_block_clock.py F7). The question the head asks is")
    print("  whether a ramp gets the wide place seated before it is priced")
    print("  out -- a strand where the flat reading has nothing.")
    bydeg = lambda k: k[0]
    narrow = HL.psi_ladder("psi 2,1 w0", 2, 1, 0)
    print("\n  %-15s %-6s %-7s %-7s %-8s %-8s %-9s %s"
          % ("wide ladder", "cross", "above1", "risers", "run slot",
             "strands", "flatmin", "strand slots @ depths"))
    out = []
    for tag, p, e, w in HL.HEADED:
        wide = HL.psi_ladder(tag, p, e, w)
        lad = lambda k, wd=wide, nr=narrow: (nr if k[1] == 0 else wd)
        c = read(narrow, bydeg, sch, npl, HL.cross_from(wide), lad=lad)
        out.append((tag, c))
        print("  %-15s %-6d %-7d %-7d %-8s %-8d %-9s %s"
              % (tag, HL.cross_from(wide), len(c["deep"]), len(c["run"]),
                 ",".join(str(i) for _, i, _, _ in c["run"]) or "none",
                 len(c["strand"]),
                 c["flat"] if c["flat"] is not None else "moving",
                 ", ".join("s%d@%d" % (i, e) for _, i, e in c["strand"])
                 or "none"))
    return out


# ------------------------------------------- S5 the mechanism the sweep found
def traced_walk(pump, cls, sch, npl, n=MOVES, lad=None):
    """The same cell again, counting each item's MOVES. The walker records
    clock lifts and seats and not who moved, and a stalled climber and an
    untouched opening are indistinguishable in the seat alone."""
    w = TP.PWalk(npl, sch, pump, cls, DCAP, seed=SEED, lad=lad)
    moved = {}
    for _ in range(n):
        _, ties = w.menu()
        _, d, slot, _, kind = w.apply(ties[0])
        if kind == "move":
            moved[(d, slot)] = moved.get((d, slot), 0) + 1
    return moved, w.seat


def s5_mechanism(sch, npl, res):
    """A SECOND SLATE, frozen after the sweep and before this section's engine.

    The sweep's strand depths are not arbitrary numbers: they are small, they
    sit BELOW the crossing depth at every headed ladder, and they look like
    the ladder's own early members shifted by one. A covered opening seats an
    item at its door, and under a block clock that door is the block's own
    tick plus one -- so a strand should be an OPENING taken while the block's
    tick still stood on a low rung, and never an item that climbed and
    stalled.

     PR5 EVERY STRAND SITS ONE ABOVE A LADDER MEMBER. e - 1 is in S for every
         strand at every cell.
     PR6 THE RAMP IS THE WHOLE OF WHAT CAN BE STRANDED. At a headed ladder
         every strand's e - 1 is at or below the seat p^t -- inside the ramp,
         strictly below the splice -- so the strandable depths are the ramp's
         rungs and nothing else.
     PR7 THE FILL IS TOP-DOWN. As the partition refines, the depth set grows
         by adding SHALLOWER depths: the deepest strandable rung is taken
         first and never given up.
     PR8 A STRAND NEVER MOVED. Every strand made ZERO moves: its exponent is
         the door of the opening that seated it and nothing else. This is the
         one of the four that PR5 does NOT already imply and the reason it is
         here -- on Z[i] the ladder is 1, 2, 7, ... so an item seated at 2 has
         door 1 and CLIMBS to 3, which is the depth the sweep reports. A
         stalled climber and an untouched opening leave the identical print,
         and only a move count tells them apart.

     KILL-SHAPES, as prints: a strand whose e - 1 is not a ladder member; a
     strand above the seat; a refinement whose depth set is not a superset of
     the coarser one, or which adds a depth deeper than one already held; a
     strand with a move to its name."""
    section("S5  THE MECHANISM THE SWEEP SUGGESTS -- a strand is an opening "
            "taken at a\n    block's own tick, so the ramp is the whole of "
            "what a block can strand")
    print("  %-15s %-4s %-6s %-8s %-16s %-9s %-12s %s"
          % ("ladder", "seat", "cross", "strands", "depths (all cells)",
             "e-1 in S", "e-1 <= seat", "moves made"))
    bad5, bad6, bad7, bad8 = [], [], [], []
    tot = totmoved = 0
    for tag, w, pump, tail, cross in ladders():
        S = set(pump.S)
        # the seat p^t is where a headed ladder's ramp ends and its splice
        # begins; a splice-free orbit has no seat and PR6 does not bind there
        p, e = [r[1:3] for r in HL.LEGAL if r[0] == tag][0]
        t = HL.seat_exp(p, e) if w else None
        seat = p ** t if t is not None else None
        allst, dep, moves = [], [], []
        for ptag, cls in PARTITIONS:
            c = res[(tag, ptag)]
            allst += c["strand"]
            dep.append(c["depths"])
            traced, final = traced_walk(pump, cls, sch, npl)
            ok(final == c["w"].seat,
               "%s/%s: the traced walk and the sweep's walk end at different "
               "seats, so the move counts are not this cell's" % (tag, ptag))
            moves += [traced.get((d, i), 0) for d, i, _ in c["strand"]]
        inS = sum(1 for _, _, e in allst if (e - 1) in S)
        under = sum(1 for _, _, e in allst
                    if seat is not None and (e - 1) <= seat)
        if inS != len(allst):
            bad5.append((tag, [e for _, _, e in allst if (e - 1) not in S]))
        if seat is not None and under != len(allst):
            bad6.append((tag, seat, [e for _, _, e in allst
                                     if (e - 1) > seat]))
        for a, b in zip(dep, dep[1:]):
            if not set(a) <= set(b) or (a and b and max(b) > max(a)):
                bad7.append((tag, a, b))
        tot += len(moves)
        totmoved += sum(1 for m in moves if m)
        if any(moves):
            bad8.append((tag, sorted(set(m for m in moves if m))))
        print("  %-15s %-4s %-6d %-8d %-16s %-9s %-12s %s"
              % (tag, seat if seat is not None else "-", cross, len(allst),
                 ", ".join(str(x) for x in
                           sorted(set(e for _, _, e in allst))) or "none",
                 "%d/%d" % (inS, len(allst)),
                 "%d/%d" % (under, len(allst)) if seat is not None else "-",
                 "%d of %d moved" % (sum(1 for m in moves if m), len(moves))))
    # printed rather than left to be summed off the column above: the first
    # write of F7 added that column by hand and got it wrong by three
    print("\n  TOTALS over every ladder and partition: %d strands, %d of them "
          "moved,\n  %d seated and never moved."
          % (tot, totmoved, tot - totmoved))
    print("\n  PR5 -- strands not one above a ladder member: %d ladders"
          % len(bad5))
    for t in bad5:
        print("      %s: %s" % t)
    print("  PR6 -- strands above the seat, outside the ramp: %d ladders"
          % len(bad6))
    for t in bad6:
        print("      %s: seat %d, offenders %s" % t)
    print("  PR7 -- refinements that drop a depth or add a deeper one: %d"
          % len(bad7))
    for t in bad7:
        print("      %s: %s then %s" % t)
    print("  PR8 -- ladders carrying a strand that MOVED: %d" % len(bad8))
    for tag, ms in bad8:
        print("      %s: move counts %s" % (tag, ms))
    return bad5, bad6, bad7, bad8


def main():
    sch = PS.Sched("alpha=1,b=2,m=1", alpha=1, b=2, m=1)
    sch.check_monotone(DCAP)
    npl = dict((d, 2) for d in range(1, DCAP + 1))

    print("explore_headed_block.py -- what a ramp leaves behind, block by "
          "block.")

    s1_control(sch, npl)
    res, k1, k3, k4 = s2_sweep(sch, npl)
    k2, k2loose, bad2 = s2_verdicts(res, k1, k3, k4)
    moved = s3_window(sch, npl, res)
    s4_mixed(sch, npl)
    bad5, bad6, bad7, bad8 = s5_mechanism(sch, npl, res)

    section("VERDICT")
    print("  K1 (a second riser past the splice):  %d cells" % len(k1))
    print("  K2 as frozen (flat at 2, 3, 4 blocks): %d ladders" % len(k2loose))
    print("  K2 strict (deaf to the dial entirely): %d ladders" % len(k2))
    print("  K3 (the budget law's prediction):     %d cells" % len(k3))
    print("  K4 (every strand at one depth):       %d ladders" % len(k4))
    print("  PR2 off (not nondecreasing, or flat): %d ladders" % len(bad2))
    print("  S3 (counts moving with the window):   %d cells" % len(moved))
    print("  PR5 (a strand off the ladder):        %d ladders" % len(bad5))
    print("  PR6 (a strand outside the ramp):      %d ladders" % len(bad6))
    print("  PR7 (a fill that is not top-down):    %d refinements" % len(bad7))
    print("  PR8 (a strand that actually moved):   %d ladders" % len(bad8))


if __name__ == "__main__":
    main()
