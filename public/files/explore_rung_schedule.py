"""explore_rung_schedule.py -- THE STRAND LAW AT A SECOND SCHEDULE. Is the
fill order the ramp's, or one pricing's?

THE QUESTION. The strand law has two halves, both read at ONE schedule --
f = d * sigma, one fresh discount, degree 1 born covered. WHERE a strand
rests is the rung law: one above a ramp rung, at or below the seat, the
fill top-down, deepest rung first and never given up
(explore_headed_block.py F6). HOW MANY is the admission census: an item
strands iff its entry and every climb door price strictly under the
runaway's splice price P, and the per-item count is a formula asked of the
schedule with no walk in it (explore_splice_cap.py F2). Every number behind
both halves is the standing schedule's. This file runs both reads at two
schedules the family exposes and arithmetic does not supply -- the price
exponent raised (f = d^2 * sigma) and the price made ADDITIVE (f = d +
sigma) -- and asks whether the law is the ramp's or that cell's. The
ladders are untouched throughout: psi's own orbits, seats, splices and
tails, because the ladder is the clock here and the ladder is the
arithmetic. What a schedule moves is the PRICE the same ramp is read
against.

WHAT A PRICE EXPONENT CAN AND CANNOT MOVE, from the hand-attack: the
splice price P = f(1, e + w) is UNCHANGED at every exponent (1^alpha = 1)
and shifted by exactly 1 at the additive price -- so alpha moves the
ADMITTED SET (whose entries price d^alpha against P) and never the bar
itself. The prediction structure follows: the census should SHRINK at
alpha = 2 and WIDEN at the additive price, while the resting depths stay
the ramp's own rungs.

THE INDEX CONVENTION, re-derived from the engine before the freeze. A
ladder's door at depth e is gap(e) = next_at(e) + 1 - e (Pump.gap), so a
clock landing sits at MEMBER + 1 for every moved item by the landing rule
itself -- "one above a ladder member" alone is the engine's and not a
finding. The rung law's content is WHICH members: ramp rungs at or below
the seat p^t, never the splice or the tail, with the fill top-down. That
is what K1 and K2 watch.

THE HAND-ATTACK, on paper before any engine code.

 (a) The census derivation (explore_splice_cap.py's steps A-C) re-run with
     the price symbolic. It consults FOUR properties, of which this file's
     slate named only three -- the fourth was supplied silently by both
     prices swept here and by the standing one, and it was separated out
     later by deleting each in turn (explore_price_hypotheses.py). The
     price is nondecreasing in d at fixed sigma (so the runaway is degree
     1, slot 0, the menu scan's early exit is sound -- checked per
     schedule by Sched.check_monotone, never assumed -- and the climb
     terminates at the splice door rather than running into the tail);
     doors are nondecreasing in time (the LADDER is monotone); a tie at P
     loses to the splice by the sorted-tie order (degree 1, slot 0, the
     lowest key); and the price is nondecreasing in SIGMA at fixed d,
     which is what makes a standing item's cost RISE as its door grows and
     what step A's "nothing priced in (B, P) is ever created again"
     actually rests on -- the door's monotonicity in time being the
     ladder's property and not the price's. All four hold at alpha = 2 and
     at the additive price, so the census formula is DERIVED at both new
     schedules and the sweep tests the derivation, not a guess.
     [SUPERSEDED IN SCOPE, explore_census_theorem.py: the list is FIVE, and
     the parenthetical above -- degree-monotonicity making the runaway
     degree 1 slot 0 -- is the clause that does not survive. That step
     compares the BORN degree's opening at door 2 against a fresh discount
     at door 1, a comparison across two doors that monotonicity at a fixed
     door cannot reach, and where a discount undercuts the born opening the
     riser is not (1, 0), by witness. Both prices swept here meet the
     missing condition, as does the standing one, so nothing below moves.
     Three of the derivation's lines close outright under a per-item clock
     and the coarser-clock cap is the door side's second consumer. The
     door monotonicity above is not the LADDER's either: the landing rule
     sends a tick to the least member at or above the depth just landed
     on, so no ladder whatever can lower one.]
 (b) Margins, hand-derived from the census formula at (p, e) = (2, 4),
     w = 2, two items a degree, seed (9, 13) -- frozen here so the print is
     checked against paper rather than paper against the print.
     At alpha = 2: P = 6; (1, slot 1) enters at price 2 and climbs 2 -> 3
     -> 5, resting at 5 (exit door 6 prices 6, not under); (2, slot 0)
     enters fresh at 4 and climbs to 3 (exit door 2 prices 8); every d >= 3
     entry prices d^2 >= 9 >= P; the seeded 9 and 13 rest at depth 1.
     A = 2, depths {3, 5}.
     At the additive price: P = 7; degrees 1 through 4 admit BOTH slots,
     degree 5 admits slot 0 only (entry 6, second slot 7), degree 6 admits
     nothing (entry 7); the climbers rest at 5 except (5, 0), whose door
     out of 3 prices 7. A = 8, depths {3, 5}.
 (c) The vacuity hazard is the parent's: a crossing never reached makes
     PR6 vacuous. Degree-1 prices are IDENTICAL at every alpha (1^alpha =
     1), and the other degrees only get dearer at alpha = 2, so the
     runaway crosses at least as fast as the parent's cells; the additive
     price admits more spending elsewhere, so the crossing check is read
     and printed rather than trusted.
 (d) The statistic's algebra: a strand is a deep item minus a riser, the
     risers read at the half window -- imported reads whose window
     behaviour the parent already measured (F9); K5 re-reads the counts at
     400 moves anyway, because the admitted set is wider at the additive
     price and a wider transient is exactly what a window artifact rides.

THE SLATE, frozen before the engine. Every prediction is a TRANSPLANT from
the standing schedule unless marked derived -- that is the point of the
run, and PR2 is the one with no derivation anywhere.

 PR1 (rung law, depths half). At both new schedules every strand on a
     headed ladder rests one above a RAMP RUNG at or below the seat:
     e - 1 a ladder member with e - 1 <= p^t. Splice-free ladders are
     checked for membership only, the seat clause having no seat to read.
 PR2 (top-down fill -- the transplant under most strain, no derivation).
     Along every refinement pair of the grid's partitions, at both new
     schedules, the strand depth set never drops a depth and never gains
     one deeper than a depth already held.
 PR3 (the census -- DERIVED at (a), margins at (b)). Every per-item cell
     prints exactly its own inputs' A -- count and depth set -- at both
     new schedules, all widths.
 PR4 (the budget). The flat tail minimum is the runaway's own
     f(1, tail gap) at every cell whose tail has stopped moving:
     tail gap e at alpha = 2, 1 + e additive.
 PR5 (the cap). No cell of any partition prints a strand count above its
     inputs' A, and every refinement pair is nondecreasing.
 PR6 (one riser). Exactly one item rises at every cell, standing at or
     above its ladder's crossing depth wherever the cell has crossed.

 KILL-SHAPES, as observables this rig PRINTS.
  K1 a strand on a headed ladder whose e - 1 is not a ladder member or
     lies above the seat. The rung law is then the standing schedule's.
  K2 a refinement pair that drops a strand depth or gains one deeper
     than any held. The fill order is then not the ramp's.
  K3 a per-item cell whose printed count or depth set differs from its
     own inputs' A. The census then needs the walk at the new price.
  K4 a flat tail minimum differing from f(1, tail gap).
  K5 a strand count or depth set that moves between 120 and 400 moves.
  K6 two or more risers at a cell whose runaway stands past its crossing.

RUN DISCIPLINE. The grid is ten psi ladders x five partitions x two
schedules at 120 moves with the window control at 400; the census sweep is
nine widths x ten partitions x two schedules at 400 moves. The parent rigs
ran the same grids at one schedule in 0.5 s each and peaked at 43 MB, so
the estimate is ~5 s and far under the 512 MB line. One process.

SECTIONS.
 S0 forced failures: every detector the verdicts lean on, made to fire --
    a fabricated off-ramp strand against K1, a fabricated depth drop
    against K2, a walked count against the wrong width's A for K3.
 S1 positive controls at the STANDING schedule, before any verdict: the
    census against all seven recorded headed per-item counts, and the
    walked (2, 4, 2) row against the parent's printed 0, 1, 2, 3, 6.
 S2 the grid at each new schedule: risers, strands, depths, the budget,
    the rung-law read at every strand.
 S3 the census sweep at each new schedule: nine widths x ten partitions
    against A, the chains, the cap.
 S4 the window control: every S2 strand count and depth set re-read at
    400 moves.

RUN RECORD. One process, ~4 s wall, memory far under the 512 MB line (the
parent rigs peak at 43 MB and this file runs their grids three times).
Ten psi ladders x five partitions x two new schedules at 120 moves, the
window control at 400 with the moved cell re-read at 400 and 1200, the
census sweep nine widths x ten partitions x two schedules at 400 moves,
supply two items a degree to 400, seed (9, 13).

F1 THE CONTROLS HOLD (S0, S1). Every detector fired on its fabricated
   input -- the off-ramp strand, the above-seat strand, the dropped depth,
   the too-deep gain, the wrong-width census (A(w=2) = 6 against
   A(w=4) = 9). The census reproduces all seven recorded headed per-item
   counts -- 0, 2, 3, 5, 2, 6, 15, depth sets included -- and the walked
   (2, 4, 2) row reprints the parent's 0, 1, 2, 3, 6.

F2 THE RUNG LAW IS THE RAMP'S (S2, PR1; K1 at 0 over both schedules, all
   100 grid cells). At f = d^2 * sigma and at f = d + sigma alike, every
   strand rests one above a ramp rung at or below the seat. The occupied
   depth sets follow the admitted count and stay top segments of ONE rung
   set per ladder: the headed per-item sets coincide with the standing
   schedule's -- {3, 5} at (2, 4), {3, 5, 9} at (2, 8), {2} at (3, 2),
   {3} at (2, 2) -- while the splice-free psi(2, 3) drops to {5} at the
   squared price from the standing {3, 5} (computed in the audit,
   standing grid), its shallow rung vacated WITH its admitted items. So
   the price moves which rungs are OCCUPIED and never where resting
   happens.

F3 THE FILL IS TOP-DOWN AT BOTH SCHEDULES (S2, PR2; the strict read at 0).
   Every cell's depth set is a top segment of its per-item cell's, at
   every ladder and both schedules. The FROZEN pair wording fired at 14
   pairs in each grid, 28 in all, every one on the empty-base case -- a
   first fill from an empty coarser cell counts as a "too-deep gain" as
   written -- and every one of those gains is a top segment of the depths
   the finer partitions hold (27 of the 28 the deepest alone, the
   alpha = 2 (2, 8) one-to-three-blocks pair gaining {5, 9}), which is
   the top-down law doing precisely what it says. The wording was frozen
   against nonempty bases; the strict top-segment read is the meaning, and
   both are printed.

F4 THE CENSUS IS THE SCHEDULE'S AT EVERY PRICE SWEPT (S3, PR3; K2, K3 and
   the chains all at 0, both schedules, nine widths x ten partitions).
   Every per-item cell prints exactly its own inputs' A: at alpha = 2 the
   counts 2, 2, 2, 2, 4, 4, 4, 6, 7 and at the additive price 6, 8, 10,
   12, 16, 20, 28, 36, 52 across w = 1..24, every coarser cell at or
   under A, every refinement chain nondecreasing. The hand-derived margins
   held to the digit: A = 2 {3, 5} at alpha = 2, w = 2; A = 8 {3, 5}
   additive. As the hand-attack predicted, the exponent SHRINKS the
   admitted set (entries price d^alpha against an unchanged P) and the
   additive price WIDENS it (P shifts by 1 while entries price d + 1);
   the depths never moved.

F5 THE BUDGET SURVIVES BOTH PRICES (S2, PR4; K4 at 0). The flat tail
   minimum is the runaway's own f(1, tail gap) at every settled cell --
   equal to the tail gap at alpha = 2 (1^alpha = 1) and to 1 + tail gap
   additive.

F6 ONE RISER AT EVERY CROSSED CELL, AND THE ONE SLOW CELL SETTLES ON ITS
   CENSUS (S2, S4, PR6; K6 at 0, K5 at one cell resolved). Exactly one
   item rises at 99 of the 100 grid cells; the additive Z[2^1/8]
   per-item cell is the one uncrossed 120-move read in the file -- the
   widest admitted set, 7 items still climbing, its transient longer
   than the window -- and K5's window read moved it 14 -> 20. Re-read
   settled: by 400 moves it has crossed with exactly ONE riser, flat
   minimum 9 = 1 + tail, and prints 20 strands {3, 5, 9} = its own A,
   identical at 1200. A moved count was a transient still running, not a
   window artifact, and the vacuity hazard the hand-attack named is why
   the crossing is printed rather than trusted.

THE VERDICT THE SHELF EVENT ASKED FOR: both halves of the strand law
reproduce at two schedules the standing one does not contain -- the fill
order and resting depths are the RAMP'S (rule in range, this file), and
the count is the admission census recomputed from whichever price is in
force (rule in range, derived per schedule by the hand-attack's properties
-- read (a), whose count was corrected from three to four after this file
ran). What a price changes is the admitted set alone.
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

# refinement pairs among BC.PARTITIONS: coarser -> finer only. 2 and 3
# blocks are incomparable; 4 blocks refines 2 ((d+s) mod 4 determines
# (d+s) mod 2); per item refines everything.
GRID_CHAINS = [("1 block", "2 blocks"), ("1 block", "3 blocks"),
               ("2 blocks", "4 blocks"), ("4 blocks", "per item"),
               ("3 blocks", "per item")]

SCHEDULES = [("alpha=2", PS.Sched("alpha=2,b=2,m=1", alpha=2)),
             ("additive", PS.Sched("additive,m=1", add=True))]


def ok(cond, msg):
    if not cond:
        raise AssertionError(msg)


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def seat_of(p, e, w):
    """The seat p^t, or None for a splice-free ladder (no seat clause)."""
    if w == 0:
        return None
    t = HL.seat_exp(p, e)
    return p ** t


def rung_check(pump, seat, strands):
    """K1's read: the strands whose rest violates the rung law. Returns the
    violating (d, slot, e) list -- membership always, the seat bound only
    where there is a seat."""
    bad = []
    for d, slot, e in strands:
        member = (e - 1) in pump.S
        below = True if seat is None else (e - 1) <= seat
        if not (member and below):
            bad.append((d, slot, e))
    return bad


def fill_check(depth_sets):
    """K2's read over one refinement pair (coarse set, fine set): the depths
    dropped, and the depths gained deeper than any held."""
    coarse, fine = depth_sets
    dropped = sorted(set(coarse) - set(fine))
    deepest = max(coarse) if coarse else 0
    over = sorted(d for d in set(fine) - set(coarse) if d > deepest)
    return dropped, over


# --------------------------------------------------------- S0 forced failures
def s0_forced(sch_std):
    section("S0  FORCED FAILURES -- every detector fired on purpose, before "
            "any verdict\n    leans on its silence")
    pump = HL.psi_ladder("forced 2,4 w2", 2, 4, 2)
    seat = seat_of(2, 4, 2)
    bad = rung_check(pump, seat, [(1, 1, 7)])   # 6 is not a member
    ok(bad == [(1, 1, 7)], "K1's detector missed an off-ramp strand")
    print("  K1 detector: a fabricated strand at depth 7 (6 not a member) "
          "-> fired.")
    bad = rung_check(pump, seat, [(1, 1, 11)])  # 10 is the splice, above seat
    ok(bad == [(1, 1, 11)], "K1's detector missed an above-seat strand")
    print("  K1 detector: a fabricated strand at depth 11 (the splice, above "
          "the seat)\n               -> fired.")
    dropped, over = fill_check(([3, 5], [3]))
    ok(dropped == [5], "K2's detector missed a dropped depth")
    dropped, over = fill_check(([3], [3, 9]))
    ok(over == [9], "K2's detector missed a too-deep gain")
    print("  K2 detector: a dropped depth and a too-deep gain -> both fired.")
    npl = HL.supply()
    a2, _, _ = SC.census(sch_std, 2, 4, 2, npl, SEED)
    a4, _, _ = SC.census(sch_std, 2, 4, 4, npl, SEED)
    ok(a2 != a4, "K3's control is vacuous: A(w=2) == A(w=4)")
    print("  K3 detector: A(w=2) = %d against A(w=4) = %d -> a wrong-width "
          "census is\n               visible." % (a2, a4))


# ------------------------------------------------------- S1 positive controls
def s1_control(sch_std, npl):
    section("S1  POSITIVE CONTROLS at the standing schedule, before any "
            "verdict")
    print("  (a) the census against all seven recorded headed per-item "
          "counts:")
    recorded = {"Q_2 w1": 0, "Z[sqrt2] w1": 2, "K5ram2 w2": 3, "Z[i] w3": 5,
                "Z[sqrt-3] w1": 2, "Z[2^1/4] w2": 6, "Z[2^1/8] w4": 15}
    for tag, p, e, w in HL.HEADED:
        a, depths, _ = SC.census(sch_std, p, e, w, npl, SEED)
        ok(a == recorded[tag], "%s: census %d against recorded %d"
           % (tag, a, recorded[tag]))
        print("      %-15s A = %-3d depths %s" % (tag, a, depths))
    print("\n  (b) the walked (2, 4, 2) row at 120 moves against the "
          "parent's 0, 1, 2, 3, 6:")
    pump = HL.psi_ladder("ctrl 2,4 w2", 2, 4, 2)
    cross = HL.cross_from(pump)
    want = [0, 1, 2, 3, 6]
    got = []
    for ptag, cls in BC.PARTITIONS:
        c = HB.read(pump, cls, sch_std, npl, cross, n=MOVES)
        got.append(len(c["strand"]))
    ok(got == want, "the parent row reprints %s against %s" % (got, want))
    print("      %s -- equal." % got)


# ------------------------------------------------------------ S2 the grid
def s2_grid(stag, sch, npl):
    section("S2  THE GRID at %s -- ten psi ladders x five partitions, "
            "%d moves" % (stag, MOVES))
    print("  %-15s %-10s %-6s %-6s %-7s %-8s %-8s %s"
          % ("ladder", "partition", "cross", "past", "risers", "strands",
             "flatmin", "strand depths"))
    res, k1, k4, k6 = {}, [], [], []
    for tag, p, e, w in HL.LEGAL:
        pump = HL.psi_ladder("%s %s" % (stag, tag), p, e, w)
        _, tail, _ = HL.profile(pump)
        cross = HL.cross_from(pump)
        seat = seat_of(p, e, w)
        want_flat = sch.price(1, tail)
        for ptag, cls in BC.PARTITIONS:
            c = HB.read(pump, cls, sch, npl, cross, n=MOVES)
            res[(tag, ptag)] = c
            bad = rung_check(pump, seat, c["strand"])
            if bad:
                k1.append((tag, ptag, bad))
            if c["flat"] is not None and c["flat"] != want_flat:
                k4.append((tag, ptag, c["flat"], want_flat))
            if c["crossed"] and len(c["run"]) > 1:
                k6.append((tag, ptag, len(c["run"])))
            print("  %-15s %-10s %-6d %-6s %-7d %-8d %-8s %s"
                  % (tag, ptag, cross, "yes" if c["crossed"] else "NO",
                     len(c["run"]), len(c["strand"]),
                     str(c["flat"]), c["depths"]))
    print("\n  K1 (off-rung or above-seat strands): %s" % (k1 or "none"))
    print("  K4 (flat minimum off f(1, tail)):    %s" % (k4 or "none"))
    print("  K6 (extra risers at a crossed cell): %s" % (k6 or "none"))
    print("  K2, the fill order -- the FROZEN pair read and the STRICT "
          "top-segment read\n  side by side (the frozen wording counts a "
          "first fill from an empty cell as a\n  too-deep gain, which the "
          "meaning does not):")
    for a, b in GRID_CHAINS:
        for tag, _, _, _ in HL.LEGAL:
            ca, cb = res[(tag, a)], res[(tag, b)]
            dropped, over = fill_check((ca["depths"], cb["depths"]))
            if dropped or over:
                print("      frozen: %s %s -> %s: dropped %s, gained deep %s"
                      % (tag, a, b, dropped, over))
    strict = []
    for tag, _, _, _ in HL.LEGAL:
        full = res[(tag, "per item")]["depths"]
        for ptag, _ in BC.PARTITIONS:
            held = res[(tag, ptag)]["depths"]
            if held != full[len(full) - len(held):]:
                strict.append((tag, ptag, held, full))
    print("      strict (a cell's depth set must be a top segment of its "
          "per-item\n      cell's): %s" % (strict or "none fired"))
    return res


# ------------------------------------------------------ S3 the census sweep
def s3_census(stag, sch, npl):
    section("S3  THE CENSUS SWEEP at %s -- nine widths x ten partitions "
            "against A" % stag)
    p, e = 2, 4
    k2, k3 = [], []
    print("  %-4s %-4s %-14s | per-partition strand counts (SC.PARTS order)"
          % ("w", "A", "A depths"))
    res = {}
    for w in SC.WIDTHS:
        a, adep, _ = SC.census(sch, p, e, w, npl, SEED)
        pump = HL.psi_ladder("%s cap w%d" % (stag, w), p, e, w)
        row = []
        for ptag, cls in SC.PARTS:
            c = SC.cell(sch, npl, pump, cls, n=SC.MOVES, seed=SEED)
            res[(w, ptag)] = c
            row.append(c["n"])
            if c["n"] > a:
                k2.append((w, ptag, c["n"], a))
            if ptag == "per item" and (c["n"] != a
                                       or c["depths"] != list(adep)):
                k3.append((w, c["n"], a, c["depths"], adep))
        print("  %-4d %-4d %-14s | %s" % (w, a, adep, row))
    print("\n  the chains (coarser -> finer, a strict decrease fires):")
    fired = []
    for a_t, b_t in SC.CHAINS:
        for w in SC.WIDTHS:
            if res[(w, a_t)]["n"] > res[(w, b_t)]["n"]:
                fired.append((w, a_t, b_t,
                              res[(w, a_t)]["n"], res[(w, b_t)]["n"]))
    print("      %s" % (fired or "none fired"))
    print("  K2 (a count above A): %s" % (k2 or "none"))
    print("  K3 (per-item off its A): %s" % (k3 or "none"))


# --------------------------------------------------- S4 the window control
def s4_window(npl, grids):
    section("S4  THE WINDOW CONTROL -- every S2 strand count and depth set "
            "re-read at %d\n    moves" % LONG)
    moved = []
    for stag, sch in SCHEDULES:
        for tag, p, e, w in HL.LEGAL:
            pump = HL.psi_ladder("%s %s long" % (stag, tag), p, e, w)
            cross = HL.cross_from(pump)
            for ptag, cls in BC.PARTITIONS:
                c0 = grids[stag][(tag, ptag)]
                c1 = HB.read(pump, cls, sch, npl, cross, n=LONG)
                if (len(c0["strand"]) != len(c1["strand"])
                        or c0["depths"] != c1["depths"]):
                    moved.append((stag, tag, ptag,
                                  len(c0["strand"]), len(c1["strand"]),
                                  c0["depths"], c1["depths"]))
    print("  cells whose count or depth set moved between %d and %d moves:"
          % (MOVES, LONG))
    print("      %s" % (moved or "none"))
    if moved:
        print("\n  the moved cells re-read at a SETTLED window -- crossed, "
              "and the count\n  against the cell's own A (a moved count is a "
              "transient still running only\n  if the settled read matches "
              "the census and the crossing is passed):")
        for stag, tag, ptag, _, _, _, _ in moved:
            sch = dict(SCHEDULES)[stag]
            p, e, w = [(r[1], r[2], r[3]) for r in HL.LEGAL
                       if r[0] == tag][0]
            a, adep, _ = SC.census(sch, p, e, w, npl, SEED)
            pump = HL.psi_ladder("%s %s settle" % (stag, tag), p, e, w)
            cross = HL.cross_from(pump)
            cls = dict(BC.PARTITIONS)[ptag]
            for n in (LONG, 3 * LONG):
                c = HB.read(pump, cls, sch, npl, cross, n=n)
                print("      %s %s %s at %4d moves: %d riser(s), crossed %s, "
                      "flat %s,\n      %d strands %s against A = %d %s"
                      % (stag, tag, ptag, n, len(c["run"]),
                         "yes" if c["crossed"] else "NO", str(c["flat"]),
                         len(c["strand"]), c["depths"], a, list(adep)))


def main():
    sch_std = PS.Sched("alpha=1,b=2,m=1", alpha=1)
    sch_std.check_monotone(DCAP)
    for _, sch in SCHEDULES:
        sch.check_monotone(DCAP)
    npl = HL.supply()
    s0_forced(sch_std)
    s1_control(sch_std, npl)
    grids = {}
    for stag, sch in SCHEDULES:
        grids[stag] = s2_grid(stag, sch, npl)
    for stag, sch in SCHEDULES:
        s3_census(stag, sch, npl)
    s4_window(npl, grids)
    print("\ndone.")


if __name__ == "__main__":
    main()
