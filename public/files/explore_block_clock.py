"""explore_block_clock.py -- THE CLOCK IS TWO DIALS, and a ring sits at the
cell between the family's two ends.

THE QUESTION. A seated place's price is a function of its own ladder, its own
exponent, and ONE integer read off the state: the door of a place P over the
rational prime p is the least r with v_p(lambda(P^(e+r))) > v_p(L), one
p-adic valuation and nothing else (explore_populated_door.py F1-F3, 188
(column, exponent, v_p(L)) keys over 717 seated readings, 0 clashes). So the
state's price structure is not a number, it is the VECTOR

    kappa(S) = (v_l(L(S)))_l   over the rational primes,

with the ladders of the places over l attached to coordinate l. Every place
reads exactly one coordinate of it.

WHICH MAKES "the clock" TWO INGREDIENTS THE FAMILY MOVES WITH ONE DIAL. The
schedule family offers a GLOBAL clock (one tick every item reads) and a
PER-ITEM clock (one tick each), and that single dial moves two things at
once: who shares a TICK, and who shares a LADDER. A number ring separates
them. Places over one rational prime SHARE a tick -- they read the same
kappa_p -- and do NOT share a ladder, a ramified place's gap being its
ramification index against an unramified place's 1. So a ring is a BLOCK
clock: one tick per residue characteristic, per-place ladders inside a block,
strictly between the family's two cells and never run at either.

The engine already admits it and nobody asked. explore_tick_pump.py's PWalk
takes `cls` (which items share a tick) and `lad` (which ladder each item
climbs) as INDEPENDENT arguments; every cell to date has set cls to GLOBAL or
PERITEM. This file sets it to a block index.

WHAT THE VECTOR PREDICTS, AND WHY THE ANSWER IS NOT OBVIOUS. Coordinates are
written one at a time by a clock move -- a mover raises v_p at its own residue
characteristic by one and touches nothing else (51 of 51, 0 off,
explore_undercut_nf.py) -- so under a block clock the blocks evolve
independently. Two blocks each holding a cheap vehicle should then each run
away, and the limit theorem's ONE deep coordinate should become one per
block. Against that stands the door's RESET: a recurrent mover lands on the
next rung of its own ladder, so its next door is next(kappa+1) - next(kappa),
its own GAP, and its cost is FLAT rather than rising. A global minimum over
flat costs has one winner forever. So the two readings disagree, the
disagreement is about whether the archimedean order on prices is what
collapses the product to a single deep place, and one walk decides it.

THE SLATE, frozen before any engine code.

 PR1 THE COLLAPSE. Exactly ONE runaway at every partition and every
     constant-gap ladder -- an item whose exponent is still rising over the
     trailing window. Items above exponent 1 beyond it are STRANDS.
 PR2 THE DIAL IS A DIAL. The count above exponent 1 is nondecreasing as the
     partition refines, and the one-block cell reproduces GLOBAL while the
     singleton cell reproduces PERITEM, move for move.
 PR3 THE BUDGET SURVIVES. The flat tail minimum at a block clock is the
     runaway's own f(d, gap) -- the number both ends already predict, the
     state cancelling out of it.
 PR4 THE CEILING IS PER-BLOCK. No block cell seats an item above exponent 1
     at a degree above the global cell's.

 KILL-SHAPES, as observables this rig PRINTS.
  K1 two or more items still rising over the trailing window (a second
     runaway) -- the archimedean-collapse reading is then wrong and the
     blocks are genuinely independent.
  K2 a block count above exponent 1 outside the range of its own run's
     global and per-item counts.
  K3 a flat tail minimum differing from the runaway's own product.

 TRANSPLANT MARKS -- intuitions imported from a neighbouring object, flagged
 as such before the run. PR1's mechanism -- the flat
 recurrent cost -- is derived from the NUMBER-RING door arithmetic, where
 sigma resets to the ramification index, and transplanted here to an abstract
 family whose ladder is a bare gap set. PR2's monotonicity has no derivation
 behind it at all and is the prediction most likely to be wrong: refining a
 partition slows every block's tick, which narrows doors and argues the count
 up, but a narrower door can also change WHICH item wins, and the strand set
 is not monotone under a change of winner.

 THE HAND-ATTACK found one cell the sweep would otherwise have missed. PR1's
 weak point is a TIE: two blocks whose flat costs are EQUAL, where the minimum
 could rotate between them by tie-break and both run away. S3 builds exactly
 that -- a two-block partition symmetric in degree, so the blocks are
 indistinguishable in supply and in ladder. If PR1 survives there it survives.
 (This much of the hand-attack was short: the SUPPLIES are isomorphic and the
 STATE is a second variable the standing seed does not hold fixed, so the cell
 as first designed could not have tested what it was for -- F6.)

 SECTIONS.
  S1  the positive control, run before any verdict is read: one block against
      GLOBAL and singletons against PERITEM, move for move.
  S2  the block sweep -- ladders x partitions, the four observables.
  S3  the tie cell the hand-attack demanded.
  S4  the ring's own shape: two ladders inside one block, which is what a
      ramified and an unramified place over one prime are.

RUN RECORD. One process, 0.3s wall, peak working set 30.1 MB under
memwatch.py's 512 MB ceiling. Six ladders x five partitions at one schedule
(alpha=1, b=2, m=1, born={1}), a supply of two items at every degree to 400,
seed (9, 13), 120 moves a cell.

F0 WHAT THE INSTRUMENT HAD TO BE FIXED FOR, since the fix moved two printed
   numbers. "Rising" is read by snapshotting the seat and comparing, and an
   item ABSENT at the snapshot was first given a baseline of 1. A covered
   opening seats at its DOOR, which can exceed 1, so that default counted an
   item seated ONCE as one that MOVED -- and the two are opposites here, an
   opening being exactly what a runaway competes against. It contaminated 33
   of 102 risers, every one of them in a per-item row: the six discriminating
   block cells and all 20 bounded-gap cells carried none. Items absent at the
   snapshot are now excluded, which took the two per-item counts from 33 and
   29 to 15 and 14 and moved no verdict.

F1 THE POSITIVE CONTROL, read before any verdict below (S1). The block dial's
   ENDS are the family's own two clocks: one block against GLOBAL and
   singletons against PERITEM agree move for move, menu for menu and seat for
   seat, 120 moves at each of four ladders, 0 partings. So the middle of the
   dial is the partition's reading and not a second engine's.

F2 THE COLLAPSE IS THE FLAT COST'S, NOT THE PRODUCT'S -- K1 FIRED, and it
   fired exactly where the mechanism said it would (S2, PR1). At all 20
   bounded-gap cells -- exact, gap 2, gap 3 and gap 5 across all five
   partitions -- exactly ONE item is rising at both windows, however finely
   the partition is cut. At the GROWING ladders with more than one block the
   risers number exactly the distinct blocks they occupy: 2, 3 and 4 at
   squares and 2, 3 and 4 at factor 2, one per block at 6 of 6 discriminating
   cells. (The two per-item rows read 15 over 15 and 14 over 14 and are
   consistent but VACUOUS for this reading, every item being its own block
   there.) So the reset is what collapses the product: a recurrent mover lands
   on its own next rung, so a bounded ladder's recurrent cost is FLAT and one
   global minimum wins forever, while a growing ladder's CLIMBS, the minimum
   rotates, and every block gets a runaway of its own. The limit theorem's ONE
   deep coordinate is the flat-cost corner of a law that otherwise reads one
   per block, and what does the collapsing is the total order on prices rather
   than anything p-adic.
   THE OBSERVABLE FIRED AND THE INFERENCE BUNDLED INTO IT DID NOT SURVIVE,
   which is worth saying out loud because K1 was written with a meaning
   attached: "the archimedean-collapse reading is then wrong and the blocks
   are genuinely independent". Half of that is right -- the blocks ARE
   independent, which is exactly what a rotation shows -- and the conclusion
   drawn from it was wrong, since independence is what makes ONE minimum
   decisive rather than what defeats it. The kill criterion should have named
   the print and stopped there.

F3 THE BUDGET LAW SURVIVES THE MIDDLE OF THE DIAL (S2, PR3; K3 at 0 of 20).
   At every bounded-gap cell the flat tail minimum is the runaway's own
   f(d, gap) -- 1, 2, 3 and 5 at the four ladders -- at every partition alike.
   The state cancels out of the budget at a block clock exactly as it does at
   both ends, which is the half of the min-over-products law the FOUR LAWS
   reading already isolated, now measured at a clock neither end supplies.

F4 THE PARTITION IS A DIAL, AND WHAT IT DIALS IS THE STRAND COUNT (S2, PR2;
   K2 at 0 of 6). Items above exponent 1 read 1,1,1,1,1 and 1,1,1,1,1 at exact
   and gap 2; 1,2,2,2,3 at gap 3; 1,2,3,4,6 at gap 5; 1,2,3,4,39 at squares
   and 1,2,3,4,32 at factor 2 -- every middle cell inside its own run's two
   ends. At a bounded gap the RUNAWAY count stays 1 while this climbs, so
   every coordinate a refinement adds there is a STRAND and not a second
   infinite one.

F5 PR4 IS REFUTED AT 10 OF 30 CELLS, AND WHAT IT REFUTES IS THE PREDICTION
   AND NOT THE CEILING. The deepest degree carrying an item above exponent 1
   runs 3 and 4 at three and four blocks (gap 5, squares and factor 2 alike)
   and 26 and 21 at singletons, against 1 at every one-block cell. The ceiling
   FORMULA is untouched -- it reads T and T_prev at the mover's own block, and
   `apply` lifts no block's tick but the mover's -- so the ceiling is per-BLOCK
   and the state's deepest degree is a MAX over blocks. The family's one-tick
   reading of the ceiling is a one-block reading, which is what the prediction
   inherited without marking it.

F6 THE TIE THE HAND-ATTACK DEMANDED DOES NOT ROTATE, AND IT TOOK A SECOND
   SEED TO SAY SO (S3). A two-block partition by (degree + slot) mod 2 makes
   the two SUPPLIES isomorphic, one item of every degree in each. The STATE
   is a second variable, and the standing seed does not hold it fixed:
   degrees 9 and 13 are both odd, so both seeds land in block 1 and the walk
   starts asymmetric -- a control that breaks the symmetry itself cannot test
   whether the tie-break does. Run at BOTH the standing seed and a
   block-split one (degrees 9 and 12, one item in each block, the only
   genuinely tied cell), all four bounded-gap ladders carry ONE runaway in
   ONE block, and the split seed reproduces the skewed one item for item --
   same degree, same slot, same exponents. So the tie IS broken by the
   tie-break and breaks permanently, and PR1 survives at the cell built to
   kill it.

F7 THE RING'S OWN SHAPE, WHICH ONLY THE TWO-DIAL SPLIT REACHES (S4). Put both
   slots of a degree on one tick and give them DIFFERENT ladders -- which is
   what a ramified and an unramified place over one rational prime are, and a
   pair neither end of the family's dial can express -- and the runaway is the
   NARROW item at all three widths, the wide one never carried above exponent
   1 at all, the flat minimum reading f(1, 1) = 1 rather than the wide
   ladder's gap. That is the corpus's own ring finding, N^gap pricing a wide
   place out, reproduced with no ring in it.
"""

import os
import sys

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_price_schedule as PS
import explore_tick_pump as TP


DCAP = TP.WALK_DCAP      # degrees the supply carries
MOVES = TP.WALK_N        # moves per cell
TAIL = TP.FLAT_TAIL      # trailing window read for flatness and for rising
SEED = TP.GRID_SEED      # the grid's own seed, so cells compare to its cells


def ok(cond, msg):
    if not cond:
        raise AssertionError(msg)


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ------------------------------------------------------------- the partitions
def blocks(nb):
    """B blocks over items (degree, slot), assigned by (degree + slot) mod B.

    At B = 1 this is TP.GLOBAL by construction. At two items a degree and
    B = 2 every block holds exactly one item at every degree, which is the
    symmetric cell S3 needs: the blocks are indistinguishable in supply."""
    if nb == 1:
        return lambda k: 0
    return lambda k: (k[0] + k[1]) % nb


PARTITIONS = [("1 block", blocks(1)),
              ("2 blocks", blocks(2)),
              ("3 blocks", blocks(3)),
              ("4 blocks", blocks(4)),
              ("per item", TP.PERITEM)]


# --------------------------------------------------------------- the observables
def walk(npl, sch, pump, cls, lad=None, n=MOVES, seed=SEED):
    """One cell. Returns the walker, its menu minima, and the seat as it stood
    TAIL moves from the end and HALF moves from the end -- which is what makes
    'still rising' an observable rather than an inference about the future.

    TWO windows, because ONE cannot be read: a ladder whose era outruns the
    window reads zero risers on a walk that is plainly still climbing, and the
    doubling ladder is exactly that ladder. A count that disagrees between the
    windows is the instrument's and not the walk's, and printing both is what
    makes the difference visible instead of arguable."""
    w = TP.PWalk(npl, sch, pump, cls, DCAP, seed=seed, lad=lad)
    mins, mark, half = [], None, None
    for i in range(n):
        best, ties = w.menu()
        mins.append(best)
        if i == n - TAIL:
            mark = dict((d, list(v)) for d, v in w.seat.items())
        if i == n - n // 2:
            half = dict((d, list(v)) for d, v in w.seat.items())
        w.apply(ties[0])
    return w, mins, mark, half


def rising(w, mark):
    """The items whose exponent grew over the trailing window. A RUNAWAY is
    one of these; an item above exponent 1 that is NOT one is a strand.

    An item ABSENT at the mark is excluded rather than given a baseline of 1.
    A covered opening seats at its door, which can exceed 1, so defaulting the
    baseline counts an item that was seated ONCE as one that MOVED -- and the
    two are the opposite of each other here, an opening being what a runaway
    is competing against. The count of those is returned so that an exclusion
    is visible rather than silent."""
    out, seated_after = [], 0
    for d, row in sorted(w.seat.items()):
        base = mark.get(d, [])
        for i, e in enumerate(row):
            if i >= len(base):
                seated_after += 1
                continue
            if e > base[i]:
                out.append((d, i, base[i], e))
    return out, seated_after


def flat_min(mins):
    """The flat tail minimum, or None where the tail is still moving."""
    tail = set(mins[-TAIL:])
    return mins[-1] if len(tail) == 1 else None


def cell(npl, sch, pump, cls, lad=None):
    w, mins, mark, half = walk(npl, sch, pump, cls, lad=lad)
    deep = w.deep_items()
    run, _ = rising(w, mark)
    runh, after = rising(w, half)
    return {"w": w, "mins": mins, "deep": deep, "rising": run, "half": runh,
            "flat": flat_min(mins), "after": after,
            "blocks": len(set(cls((d, i)) for d, i, _, _ in runh)),
            "ceiling": max([d for d, _, _ in deep] or [0])}


# ------------------------------------------------------- S1 the positive control
def s1_control(pumps, npl, sch):
    section("S1  POSITIVE CONTROL -- the block dial's two ends against the "
            "family's own\n    two clocks, move for move, before any verdict "
            "below is read")
    print("  %-12s %-10s %-8s %s" % ("ladder", "end", "moves", "agreement"))
    for pump in pumps:
        for tag, mine, theirs in (("1 block", blocks(1), TP.GLOBAL),
                                  ("singletons", TP.PERITEM, TP.PERITEM)):
            a = TP.PWalk(npl, sch, pump, mine, DCAP, seed=SEED)
            b = TP.PWalk(npl, sch, pump, theirs, DCAP, seed=SEED)
            for _ in range(MOVES):
                ca, ta = a.menu()
                cb, tb = b.menu()
                ok(ca == cb and ta == tb,
                   "%s/%s: the menus parted: %s against %s"
                   % (pump.tag, tag, ta[:3], tb[:3]))
                a.apply(ta[0])
                b.apply(tb[0])
                ok(a.seat == b.seat,
                   "%s/%s: the seats parted" % (pump.tag, tag))
            print("  %-12s %-10s %-8d %s" % (pump.tag, tag, MOVES, "equal"))
    print("\n  The dial's ends ARE the family's two clocks, so anything the")
    print("  middle reads below is the partition's and not a second engine's.")


# ---------------------------------------------------- S2 the sweep (PR1..PR4)
def s2_sweep(pumps, npl, sch):
    section("S2  PR1, PR2, PR3, PR4 -- the block sweep: what the four laws "
            "read at a clock\n    that is neither global nor per-item")
    print("  supply: two items at every degree to %d; seed %s; %d moves a "
          "cell." % (DCAP, SEED, MOVES))
    print("  rising is read at TWO windows -- the last %d moves and the last "
          "half --\n  because a ladder whose era outruns the short one reads "
          "zero on a climbing walk." % TAIL)
    print("\n  %-12s %-10s %-9s %-7s %-7s %-7s %-9s %-8s %s"
          % ("ladder", "partition", "above e1", "rise40", "rise60", "blocks",
             "flat min", "ceiling", "runaway"))
    res, k1, k3 = {}, [], []
    for pump in pumps:
        for ptag, cls in PARTITIONS:
            c = cell(npl, sch, pump, cls)
            res[(pump.tag, ptag)] = c
            run = c["half"]
            if len(run) > 1:
                k1.append((pump.tag, ptag, len(run), c["blocks"]))
            # PR3: the flat tail minimum against the runaway's own product
            pred = None
            if c["flat"] is not None and len(run) == 1:
                d, _, _, e = run[0]
                pred = sch.price(d, pump.gap(e))
                if pred != c["flat"]:
                    k3.append((pump.tag, ptag, c["flat"], pred))
            print("  %-12s %-10s %-9d %-7d %-7d %-7d %-9s %-8d %s"
                  % (pump.tag, ptag, len(c["deep"]), len(c["rising"]),
                     len(run), c["blocks"],
                     c["flat"] if c["flat"] is not None else "moving",
                     c["ceiling"],
                     ("d%d e%d, f(d,gap)=%s" % (run[0][0], run[0][3], pred))
                     if len(run) == 1 else
                     ("%d items over %d blocks" % (len(run), c["blocks"])
                      if run else "none")))
        print()
    return res, k1, k3


def s2_verdicts(pumps, res, k1, k3):
    print("  PR1 (K1) -- cells carrying more than one rising item: %d"
          % len(k1))
    print("      %-12s %-10s %-9s %s"
          % ("ladder", "partition", "risers", "distinct blocks"))
    for tag, ptag, n, nb in k1:
        print("      %-12s %-10s %-9d %d%s"
              % (tag, ptag, n, nb, "  (one per block)" if n == nb else ""))
    print("  PR3 (K3) -- cells whose flat minimum is not the runaway's own "
          "product: %d" % len(k3))
    for tag, ptag, got, pred in k3:
        print("      %s / %s: %s against %s" % (tag, ptag, got, pred))
    print("\n  PR2 (K2) -- the block counts against their own run's two ends:")
    print("  %-12s %-8s %-8s %-8s %-8s %-8s %s"
          % ("ladder", "1 block", "2", "3", "4", "per item", "in range"))
    k2 = []
    for pump in pumps:
        row = [len(res[(pump.tag, p)]["deep"]) for p, _ in PARTITIONS]
        lo, hi = min(row[0], row[-1]), max(row[0], row[-1])
        good = all(lo <= x <= hi for x in row[1:-1])
        if not good:
            k2.append((pump.tag, row))
        print("  %-12s %-8d %-8d %-8d %-8d %-8d %s"
              % tuple([pump.tag] + row + ["yes" if good else "NO"]))
    print("\n  PR4 -- every partition's ceiling against its own 1-block cell:")
    bad4 = []
    for pump in pumps:
        base = res[(pump.tag, "1 block")]["ceiling"]
        for ptag, _ in PARTITIONS:
            c = res[(pump.tag, ptag)]["ceiling"]
            if c > base:
                bad4.append((pump.tag, ptag, c, base))
    print("      cells seating a deep item above the 1-block ceiling: %d"
          % len(bad4))
    for t in bad4:
        print("      %s / %s: %d against %d" % t)
    return k2, bad4


# ------------------------------------------------------------ S3 the tie cell
def s3_tie(npl, sch):
    section("S3  THE TIE THE HAND-ATTACK DEMANDED -- two blocks symmetric in "
            "supply and\n    in ladder, where the minimum could rotate and "
            "give a runaway to each")
    print("  At two items a degree, (d + slot) mod 2 puts exactly one item of")
    print("  every degree in each block, so the two SUPPLIES are isomorphic.")
    print("  The STATE is a second variable and the standing seed does not")
    print("  hold it fixed: degrees 9 and 13 are both odd, so both seeds land")
    print("  in block 1 and the walk starts asymmetric. A control that breaks")
    print("  the symmetry itself cannot test whether the TIE-BREAK does, so")
    print("  the cell is run at BOTH seeds -- the standing one, comparable to")
    print("  the sweep above, and a block-SPLIT one seating degrees 9 and 12,")
    print("  one item in each block, which is the only genuinely tied cell.")
    print("\n  %-12s %-11s %-9s %-8s %-26s %s"
          % ("ladder", "seed", "above e1", "rising", "the rising items",
             "blocks"))
    rot = []
    for pump in (TP.p_exact(), TP.p_step(2), TP.p_step(3), TP.p_step(5)):
        for stag, sd in (("9,13 skew", (9, 13)), ("9,12 split", (9, 12))):
            w, _, _, half = walk(npl, sch, pump, blocks(2), seed=sd)
            run, _ = rising(w, half)
            bl = sorted(set((d + i) % 2 for d, i, _, _ in run))
            if len(bl) > 1:
                rot.append((pump.tag, stag, run))
            print("  %-12s %-11s %-9d %-8d %-26s %s"
                  % (pump.tag, stag, len(w.deep_items()), len(run),
                     ", ".join("d%d s%d e%d->%d" % r for r in run[:2])
                     or "none", bl))
    print("\n  cells whose runaways span BOTH blocks: %d" % len(rot))
    return rot


# ------------------------------------------------- S4 the ring's actual shape
def s4_mixed(npl, sch):
    section("S4  THE RING'S OWN SHAPE -- two ladders inside one block, which "
            "is what a\n    ramified and an unramified place over one rational "
            "prime are")
    print("  cls puts both slots of a degree in one block (they share a tick);")
    print("  lad gives slot 0 the exact ladder and slot 1 a wider one. That")
    print("  pair is unreachable at either end of the family's own dial: a")
    print("  global clock shares the ladder too, a per-item clock shares")
    print("  neither.")
    bydeg = lambda k: k[0]
    print("\n  %-14s %-9s %-8s %-9s %-9s %s"
          % ("wide ladder", "above e1", "rising", "flat min", "ceiling",
             "runaway slot"))
    out = []
    for wide in (TP.p_step(2), TP.p_step(3), TP.p_step(5)):
        narrow = TP.p_exact()
        lad = lambda k, w=wide, n=narrow: (n if k[1] == 0 else w)
        c = cell(npl, sch, narrow, bydeg, lad=lad)
        run = c["half"]
        out.append((wide.tag, c))
        print("  %-14s %-9d %-8d %-9s %-9d %s"
              % (wide.tag, len(c["deep"]), len(run),
                 c["flat"] if c["flat"] is not None else "moving",
                 c["ceiling"],
                 ",".join(str(i) for _, i, _, _ in run) or "none"))
    print("\n  A runaway in slot 0 at every row says the shared tick is paid")
    print("  by the WIDE place and spent by the NARROW one -- which is the")
    print("  populated door read forward rather than measured at a state.")
    return out


def main():
    pumps = [TP.p_exact(), TP.p_step(2), TP.p_step(3), TP.p_step(5),
             TP.p_squares(), TP.p_geom(2)]
    sch = PS.Sched("alpha=1,b=2,m=1", alpha=1, b=2, m=1)
    sch.check_monotone(DCAP)
    npl = dict((d, 2) for d in range(1, DCAP + 1))

    print("explore_block_clock.py -- the clock is two dials, and a ring sits")
    print("between the family's two ends.")

    s1_control(pumps[:4], npl, sch)
    res, k1, k3 = s2_sweep(pumps, npl, sch)
    k2, bad4 = s2_verdicts(pumps, res, k1, k3)
    rot = s3_tie(npl, sch)
    s4_mixed(npl, sch)

    section("VERDICT")
    print("  K1 (a second runaway):            %d cells" % len(k1))
    print("  K2 (a count outside its ends):    %d ladders" % len(k2))
    print("  K3 (the budget law's prediction): %d cells" % len(k3))
    print("  PR4 (the ceiling):                %d cells above the 1-block "
          "ceiling" % len(bad4))
    print("  S3 (the tie cell rotating):       %d cells" % len(rot))


if __name__ == "__main__":
    main()
