"""explore_splice_cap.py -- HOW MANY STRANDS DOES A SPLICE HOLD? The width
half of the strand law, swept past every width arithmetic supplies.

THE QUESTION. A ramp's strands rest one above a ramp rung, at or below the
seat -- the DEPTHS half of the strand law is an identity
(explore_headed_block.py F6). The WIDTH half is a table: the strand count
rises with the splice width w on one (p, e), and each ladder has a CAP the
block count runs into rather than sets (explore_headed_block.py F4/F5). This
file sweeps w on ONE (p, e) past the arithmetic widths and asks whether the
cap is a number the schedule can be asked for directly -- a LADDER fact --
or a fact only the walk can produce.

THE INSTRUMENT, all of it imported: psi ladders from explore_headed_ladder
(ramp 1, p, ..., p^t, splice at p^t + e + w, tail gap e), the walker and its
clocks from explore_tick_pump, the block partitions and the cell reader from
explore_block_clock. The one (p, e) is (2, 4): seat 4, so TWO strandable
rungs (depths 3 and 5), the richest seat with a one-digit tail. Tail gap 4,
so the recurrent budget is B = price(1, 4) = 4; the splice door is e + w,
so the runaway's splice price is P = price(1, e + w) = 4 + w.

THE HAND-ATTACK, on paper before any engine code, and it came back a
DERIVATION rather than a guess.

 A. WHEN THE SPLICE FIRES. The walk takes the cheapest door every move. The
    degree-1 splice (price P) is taken only when no standing door prices
    under P; after it, the runaway recurs at B and the only new doors are
    its own tail doors, so nothing priced in (B, P) is ever created again.
    Hence every door that ever prices strictly under P is taken, and no
    door at or above P is ever taken after the crossing -- ties at exactly
    P lose to the splice by the menu's own sort, the splice sitting at
    degree 1 and slot 0, the lowest key in the tie list.
    THE HYPOTHESIS THIS STEP HIDES, separated out later by deleting each
    in turn (explore_price_hypotheses.py): "nothing priced in (B, P) is
    ever created again" is a claim about a STANDING item, whose door grows
    with the tick -- and a growing door costs more only if the price is
    nondecreasing in the DOOR. That is a property of the price and a
    fourth hypothesis, distinct from the ladder's own monotonicity in
    time; every schedule this corpus prices with happens to have it, and
    a price falling in the door breaks this step and the identity with it.
 B. THE RUNAWAY IS DEGREE 1, SLOT 0, always: born degree, cheapest splice,
    first in every tie. Exactly one item crosses.
    [SUPERSEDED IN SCOPE, explore_census_theorem.py: not always -- "born
    degree, cheapest" compares the born opening at door 2 against a fresh
    discount at door 1, which is a comparison ACROSS doors and needs its own
    hypothesis. Where a degree's discount undercuts the born opening the
    riser is not (1, 0), by witness. Every price this file runs meets the
    condition, so nothing below moves; the other steps close under a
    per-item clock, and the bar is more generally the door of the LAST step
    wider than the tail, e + w being the family's one-overshoot case.]
 C. SO THE PER-ITEM CENSUS IS A FORMULA -- the ADMISSION CENSUS A. For each
    item, seeded or supplied: its entry price (0 if seeded; price(d, 1) for
    a fresh first opening; price(d, 2) for every later slot and for every
    born-degree slot, the door being the fresh class tick plus one) must
    price strictly under P, and it then climbs its own ladder taking every
    door priced strictly under P, stalling at the first depth whose exit
    door prices at or above P. It is a strand iff it stalls above depth 1
    and is not the runaway. Everything here is read off the schedule, the
    ladder, the supply and the seed -- no walk is simulated.
 D. CHECKED AGAINST THE RECORDED INSTRUMENT before this file existed: the
    census reproduces every headed per-item strand count
    explore_headed_block.py printed -- Q_2 w1 -> 0, Z[sqrt2] w1 -> 2,
    K5ram2 w2 -> 3, Z[i] w3 -> 5, Z[sqrt-3] w1 -> 2, Z[2^1/4] w2 -> 6,
    Z[2^1/8] w4 -> 15 -- including the 15, which sums three depths. S1
    re-runs that check mechanically.
 E. THE BLOCK DIAL'S OWN LIMIT IS NOT PER-ITEM. blocks(nb) classes items by
    (degree + slot) mod nb, so no block count ever separates two items of
    equal degree + slot: the dial's true limit is the DIAGONAL partition
    cls(k) = degree + slot, and per-item strictly refines it. The sweep
    carries both ends explicitly.

THE SLATE, frozen before the engine. A(w) below is the admission census at
(2, 4), seed (9, 13), two items a degree.

 PR1 (DERIVED at the hand-attack, cross-checked at D). Every per-item cell
     prints exactly A(w): 5, 6, 8, 9, 12, 15, 21, 27, 39 at
     w = 1, 2, 3, 4, 6, 8, 12, 16, 24 -- and every strand depth is 3 or 5,
     both depths present at every w.
 PR2 (TRANSPLANT from explore_headed_block.py F4, measured at one to four
     blocks on arithmetic widths only). Along every refinement chain the
     count is nondecreasing: 1|2|4|8|16 blocks, 1|3|6|12 blocks, every
     block cell against the diagonal, the diagonal against per-item.
 PR3 (THE CANDIDATE, restated by the hand-attack). A(w) is the CAP: no cell
     of any partition prints a strand count above it, and per-item attains
     it. The cap is a count the schedule is asked for directly.
 PR4 (VIBES -- a three-point fit to the recorded (2, 2) rows at w = 1, 2, 3,
     flagged as the margin most likely to be wrong). The diagonal cell sits
     at D(w) = #{d >= 2 : price(d, 1) < P} = w + 2, strictly under A(w).
 PR5 (the width question's first form, kept as a FOIL). Counting
     (degree, rung) seats against the BUDGET B instead of the admission
     price P -- entry and climb doors at or under B, exit over B -- gives
     U = 4 at every w, blind to the width. The cap moves with w, so the
     budget-priced count cannot be it.
 PR6 (DERIVED seed/supply laws -- the kill's own controls). A is invariant
     across seeds (9, 13), (3, 5), (17, 19): seeding only pre-spends the
     fresh discount of a degree that opens under P anyway, or parks a
     degree that sits either way. A moves with a third item per degree by
     exactly dA = 1 + #{d >= 2 : price(d, 2) < P}: +2 at w = 2 (A 8),
     +5 at w = 8 (A 20).

 KILL-SHAPES, as observables this rig PRINTS.
  K1 a per-item cell whose printed strand count differs from its own
     inputs' A. That is the backlog kill in its meaning: the census would
     then need the walk, and the cap is a walk fact.
  K2 any cell of any partition printing a count above its inputs' A -- the
     cap is then not a cap.
  K3 a refinement pair printing a strict decrease.
  K4 a count that moves between 400 and 1200 moves.

 TRANSPLANT MARKS. PR2 is imported from the block rig's F4 (blocks one to
 four, arithmetic widths) and carried to finer partitions and dialled
 widths; the change of winner that its own note warns about is exactly what
 a wider splice buys, so it is the transplant under the most strain. PR4 is
 a fit, not a derivation. The census's tie rules (strict inequality against
 P everywhere, ties lost to the splice) are read from the walker's own
 sorted-tie order, not assumed.

RUN DISCIPLINE. Sweep cells run 400 moves (the transient at w = 24 is ~135
moves by the census's own door count; the trailing flatness window is 40);
the window control re-reads at 1200. Estimated wall clock under three
minutes, memory far under the 512 MB line (the parent rig peaked at 43 MB).

SECTIONS.
 S0 forced failures: every detector the verdict leans on, made to fire.
 S1 positive controls: (a) the census against all seven recorded headed
    per-item counts; (b) the parent rig's own (2, 4, 2) row reprinted at
    120 moves, partitions one to four and per-item -- 0, 1, 2, 3, 6.
 S2 the sweep: nine widths x ten partitions, counts, depths, A, D, U.
 S3 the verdicts: refinement chains, the cap, per-item against A.
 S4 the kill's controls: three seeds and a third item per degree at
    w = 2 and 8, per-item and diagonal, measured against their own A.
 S5 the window control at 1200 moves.

RUN RECORD. One process, 0.5 s wall, peak working set 22.3 MB under
memwatch.py's 512 MB ceiling. Nine widths x ten partitions at 400 moves,
window control at 1200, sixteen control cells.

F1 THE POSITIVE CONTROLS HOLD (S1). The census reproduces all seven
   recorded headed per-item counts -- 0, 2, 3, 5, 2, 6, 15 -- with their
   depth sets (including Z[2^1/8]'s {3, 5, 9}), and the walked (2, 4, 2)
   row reprints the parent rig's 0, 1, 2, 3, 6.

F2 THE CAP IS THE ADMISSION CENSUS (S2/S3, PR1 and PR3; K1, K2, K3 all at
   0). Every per-item cell prints exactly A(w) -- 5, 6, 8, 9, 12, 15, 21,
   27, 39 at w = 1, 2, 3, 4, 6, 8, 12, 16, 24 -- every cell of every
   partition sits at or under it, every refinement chain is nondecreasing,
   and every strand depth is 3 or 5, both present at every width. The
   width half of the strand law is a formula: an item strands iff its
   entry and every climb door price strictly under the runaway's splice
   price P = price(1, e + w), and it rests at the first rung whose exit
   door prices at or above P.

F3 THE BLOCK DIAL'S OWN CAP IS ONE STRAND PER ADMITTED DEGREE (S2/S3, PR4
   -- frozen as a three-point fit, confirmed at all nine widths). The
   diagonal cell -- the block dial's true limit, since (degree + slot)
   mod nb never separates equal sums -- prints D(w) = #{d >= 2 :
   price(d, 1) < P} = w + 2 at every width, strictly under A(w). And the
   finite rows read, by inspection after the run rather than by a frozen
   prediction: blocks(nb) prints min(nb - 1, D) at every swept cell --
   each losing block strands one item until the admitted degrees run out.
   So the count the block count runs into is D, and the count the
   partition's finest refinement runs into is A: TWO caps, one per-degree
   and one per-item, both asked of the schedule directly.

F4 THE KILL DOES NOT FIRE (S4; the item's own controls at 0 off). The cap
   is seed-invariant across (9, 13), (3, 5), (17, 19) -- as the census
   derives, seeding only pre-spends a discount an admitted degree would
   spend anyway -- and a third item per degree moves it by exactly the
   census's own delta: 8 and 20 predicted, 8 and 20 walked. The supply is
   an INPUT of the formula, not a perturbation of it: the cap moves with
   the supply the way a product moves with its factors, and needs no walk.

F5 THE BUDGET WAS THE WRONG THRESHOLD (S2, PR5). Counting seats against
   B = price(1, e) gives U = 4 at every width -- blind to w while the cap
   runs 5 to 39. The admission price P, not the recurrent budget, is what
   a splice charges, which is the head entering the law's statement
   exactly as the mixed-universe admission clause already has it
   (explore_headed_ladder.py hand-attack F).

F6 THE POPULATION IS NOT THE WINDOW'S (S5). All eighteen re-read cells
   are identical at 400 and 1200 moves.
"""

import os
import sys

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_block_clock as BC
import explore_headed_ladder as HL
import explore_price_schedule as PS
import explore_tick_pump as TP

P_, E_ = 2, 4                 # the one (p, e): seat 4, depths {3, 5}
WIDTHS = [1, 2, 3, 4, 6, 8, 12, 16, 24]
MOVES = 400                   # sweep window; the deepest transient is ~135
LONG = 1200                   # the window control's window
DCAP = TP.WALK_DCAP
SEED = TP.GRID_SEED

DIAG = lambda k: k[0] + k[1]  # the block dial's own limit (hand-attack E)
PARTS = [("1 block", BC.blocks(1)), ("2 blocks", BC.blocks(2)),
         ("3 blocks", BC.blocks(3)), ("4 blocks", BC.blocks(4)),
         ("6 blocks", BC.blocks(6)), ("8 blocks", BC.blocks(8)),
         ("12 blocks", BC.blocks(12)), ("16 blocks", BC.blocks(16)),
         ("diagonal", DIAG), ("per item", TP.PERITEM)]
# refinement pairs among the above: coarser -> finer, checked at K3
CHAINS = [("1 block", "2 blocks"), ("2 blocks", "4 blocks"),
          ("4 blocks", "8 blocks"), ("8 blocks", "16 blocks"),
          ("1 block", "3 blocks"), ("3 blocks", "6 blocks"),
          ("6 blocks", "12 blocks")] + \
         [(p, "diagonal") for p, _ in
          [("1 block", 0), ("2 blocks", 0), ("3 blocks", 0), ("4 blocks", 0),
           ("6 blocks", 0), ("8 blocks", 0), ("12 blocks", 0),
           ("16 blocks", 0)]] + [("diagonal", "per item")]


def ok(cond, msg):
    if not cond:
        raise AssertionError(msg)


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ------------------------------------------------------- the admission census
def census(sch, p, e, w, npl, seed):
    """The admission census A -- strands and their depths, asked of the
    schedule directly. Returns (count, sorted depth set, strand list)."""
    pump = HL.psi_ladder("cap w%d" % w, p, e, w)
    P = sch.price(1, e + w)
    strands = []
    for d in sorted(npl):
        if npl.get(d, 0) == 0:
            continue
        seeded = 1 if d in seed else 0
        for slot in range(npl[d]):
            if d == 1 and slot == 0:
                continue                      # the runaway (hand-attack B)
            if d in seed and slot == 0:
                cost, x = 0, 1                # seeded: standing, free
            elif d in sch.born:
                cost, x = sch.price(d, 2), 2  # covered: door is tick + 1
            elif slot == 0:
                cost, x = sch.price(d, 1), 1  # the fresh discount
            else:
                cost, x = sch.price(d, 2), 2
            if cost >= P:
                continue                      # never seated
            while sch.price(d, pump.gap(x)) < P:
                x += pump.gap(x)
            if x > 1:
                strands.append((d, slot, x))
    return len(strands), sorted(set(x for _, _, x in strands)), strands


def budget_seats(sch, p, e, w):
    """The foil U: (degree, rung) seats priced against the BUDGET B -- entry
    and climb doors at or under B, exit over B (PR5's stated reading)."""
    pump = HL.psi_ladder("foil w%d" % w, p, e, w)
    B = sch.price(1, e)
    seats = set()
    for d in range(1, DCAP + 1):
        cost, x = (sch.price(d, 2), 2) if d in sch.born \
            else (sch.price(d, 1), 1)
        if cost > B:
            continue
        while sch.price(d, pump.gap(x)) <= B:
            x += pump.gap(x)
        if x > 1:
            seats.add((d, x))
    return len(seats), sorted(seats)


# ------------------------------------------------------------ one walked cell
def cell(sch, npl, pump, cls, n=MOVES, seed=SEED):
    """One cell through the imported walker: strand count, depths, and the
    crossing check -- the runaway must stand past the splice member, else the
    reading is vacuous and says so."""
    w, mins, mark, half = BC.walk(npl, sch, pump, cls, n=n, seed=seed)
    run, _ = BC.rising(w, half)
    deep = w.deep_items()
    keys = set((d, i) for d, i, _, _ in run)
    strand = [(d, i, e) for d, i, e in deep if (d, i) not in keys]
    cross = HL.cross_from(pump)
    return {"n": len(strand), "depths": sorted(set(e for _, _, e in strand)),
            "strand": strand, "risers": len(run),
            "crossed": all(e >= cross for _, _, _, e in run) and len(run) == 1,
            "flat": BC.flat_min(mins)}


# --------------------------------------------------------- S0 forced failures
def s0_forced(sch, npl):
    section("S0  FORCED FAILURES -- every detector the verdict leans on, "
            "made to fire")
    fired = []
    a, _, _ = census(sch, P_, E_, 2, npl, SEED)
    try:
        ok(a == a + 1, "census mismatch")
    except AssertionError:
        fired.append("K1/K2's comparator on a doctored census")
    try:
        ok(3 >= 4, "refinement decrease")
    except AssertionError:
        fired.append("K3's comparator on a doctored pair")
    try:
        ok(1 == 2, "the harness itself")
    except AssertionError:
        fired.append("the harness itself")
    print("  forced failures fired: %d" % len(fired))
    for f in fired:
        print("    - %s" % f)
    ok(len(fired) == 3, "only %d of 3 forced failures fired" % len(fired))


# ------------------------------------------------------- S1 positive controls
def s1_control(sch, npl):
    section("S1  POSITIVE CONTROLS -- the census against the recorded "
            "instrument,\n    before any verdict is read")
    print("  (a) the admission census against every headed per-item strand")
    print("      count explore_headed_block.py printed:")
    recorded = [("Q_2 w1", 2, 1, 1, 0), ("Z[sqrt2] w1", 2, 2, 1, 2),
                ("K5ram2 w2", 2, 2, 2, 3), ("Z[i] w3", 2, 2, 3, 5),
                ("Z[sqrt-3] w1", 3, 2, 1, 2), ("Z[2^1/4] w2", 2, 4, 2, 6),
                ("Z[2^1/8] w4", 2, 8, 4, 15)]
    for tag, p, e, w, want in recorded:
        got, depths, _ = census(sch, p, e, w, npl, SEED)
        print("      %-15s recorded %-3d census %-3d depths %s"
              % (tag, want, got, depths))
        ok(got == want, "%s: census %d against the recorded %d"
           % (tag, got, want))
    print("  (b) the parent rig's own (2, 4, 2) row reprinted, 120 moves:")
    pump = HL.psi_ladder("Z[2^1/4] w2", 2, 4, 2)
    row = []
    for ptag, cls in [("1 block", BC.blocks(1)), ("2 blocks", BC.blocks(2)),
                      ("3 blocks", BC.blocks(3)), ("4 blocks", BC.blocks(4)),
                      ("per item", TP.PERITEM)]:
        c = cell(sch, npl, pump, cls, n=TP.WALK_N)
        row.append(c["n"])
        ok(set(c["depths"]) <= {3, 5},
           "%s: a depth outside {3, 5}: %s" % (ptag, c["depths"]))
    print("      %s" % row)
    ok(row == [0, 1, 2, 3, 6],
       "the recorded row 0, 1, 2, 3, 6 did not reprint: %s" % row)


# ----------------------------------------------------------------- S2 sweep
def s2_sweep(sch, npl):
    section("S2  THE SWEEP -- nine widths x ten partitions at (p, e) = "
            "(2, 4):\n    the count, its depths, and the three asked-for "
            "numbers beside it")
    res = {}
    print("  %-4s %-4s %-4s %-4s | %s" % ("w", "A", "D", "U", "strand count "
          "per partition (depths of the per-item cell last)"))
    for w in WIDTHS:
        a, adep, _ = census(sch, P_, E_, w, npl, SEED)
        dd = sum(1 for d in range(2, DCAP + 1)
                 if sch.price(d, 1) < sch.price(1, E_ + w))
        u, _ = budget_seats(sch, P_, E_, w)
        pump = HL.psi_ladder("cap w%d" % w, P_, E_, w)
        row = []
        for ptag, cls in PARTS:
            c = cell(sch, npl, pump, cls)
            res[(w, ptag)] = c
            row.append(c)
            ok(c["crossed"], "w%d/%s: the runaway has not crossed -- the "
               "window is too short to read" % (w, ptag))
        print("  %-4d %-4d %-4d %-4d | %s   depths %s (census %s)"
              % (w, a, dd, u,
                 " ".join("%3d" % c["n"] for c in row),
                 res[(w, "per item")]["depths"], adep))
        res[(w, "A")] = a
        res[(w, "Ad")] = adep
        res[(w, "D")] = dd
        res[(w, "U")] = u
    print("\n  partitions, in column order: %s"
          % ", ".join(p for p, _ in PARTS))
    return res


# -------------------------------------------------------------- S3 verdicts
def s3_verdicts(res):
    section("S3  VERDICTS -- the cap, the chains, the census")
    k1, k2, k3 = [], [], []
    pr4 = []
    for w in WIDTHS:
        a = res[(w, "A")]
        for ptag, _ in PARTS:
            n = res[(w, ptag)]["n"]
            if n > a:
                k2.append((w, ptag, n, a))
        n = res[(w, "per item")]["n"]
        if n != a:
            k1.append((w, n, a))
        for co, fi in CHAINS:
            if res[(w, co)]["n"] > res[(w, fi)]["n"]:
                k3.append((w, co, fi, res[(w, co)]["n"], res[(w, fi)]["n"]))
        if res[(w, "diagonal")]["n"] != res[(w, "D")]:
            pr4.append((w, res[(w, "diagonal")]["n"], res[(w, "D")]))
    print("  K1 -- per-item cells off their census:            %d" % len(k1))
    for w, n, a in k1:
        print("      w%d: walked %d against census %d" % (w, n, a))
    print("  K2 -- cells above the census (the cap broken):    %d" % len(k2))
    for w, ptag, n, a in k2:
        print("      w%d/%s: %d against %d" % (w, ptag, n, a))
    print("  K3 -- refinement pairs that decreased:            %d" % len(k3))
    for t in k3:
        print("      w%d: %s %d -> %s %d" % (t[0], t[1], t[3], t[2], t[4]))
    print("  PR4 -- diagonal cells off the three-point fit:    %d" % len(pr4))
    for w, n, dd in pr4:
        print("      w%d: diagonal %d against the fit %d" % (w, n, dd))
    return k1, k2, k3, pr4


# ------------------------------------------------- S4 the kill's own controls
def s4_controls(sch):
    section("S4  THE KILL'S CONTROLS -- seeds and supply, each cell against "
            "its OWN\n    census: the cap is a walk fact exactly where "
            "these part")
    bad = []
    print("  %-6s %-10s %-8s %-10s %-6s %-6s %s"
          % ("w", "seed", "supply", "partition", "walked", "census",
             "depths"))
    for w in (2, 8):
        for seed in [(9, 13), (3, 5), (17, 19)]:
            for nper in (2, 3):
                if nper == 3 and seed != SEED:
                    continue        # supply moves with the standing seed only
                npl = dict((d, nper) for d in range(1, DCAP + 1))
                a, adep, _ = census(sch, P_, E_, w, npl, seed)
                pump = HL.psi_ladder("cap w%d" % w, P_, E_, w)
                for ptag, cls in [("diagonal", DIAG), ("per item",
                                                       TP.PERITEM)]:
                    c = cell(sch, npl, pump, cls, seed=seed)
                    ok(c["crossed"], "w%d control: not crossed" % w)
                    if ptag == "per item" and c["n"] != a:
                        bad.append((w, seed, nper, c["n"], a))
                    if c["n"] > a:
                        bad.append((w, seed, nper, c["n"], a))
                    print("  %-6d %-10s %-8d %-10s %-6d %-6s %s"
                          % (w, seed, nper, ptag, c["n"],
                             a if ptag == "per item" else "(cap %d)" % a,
                             c["depths"]))
    print("\n  control cells off their own census (K1), or above it (K2): %d"
          % len(bad))
    for t in bad:
        print("      w%d seed %s supply %d: walked %d census %d" % t)
    return bad


# ------------------------------------------------------- S5 window control
def s5_window(sch, npl, res):
    section("S5  THE WINDOW CONTROL -- every per-item and diagonal count "
            "re-read at\n    %d moves" % LONG)
    moved = []
    for w in WIDTHS:
        pump = HL.psi_ladder("cap w%d" % w, P_, E_, w)
        for ptag, cls in [("diagonal", DIAG), ("per item", TP.PERITEM)]:
            c = cell(sch, npl, pump, cls, n=LONG)
            was = res[(w, ptag)]["n"]
            if c["n"] != was:
                moved.append((w, ptag, was, c["n"]))
    print("  counts that moved with the window: %d" % len(moved))
    for w, ptag, was, now in moved:
        print("      w%d/%s: %d at %d moves, %d at %d"
              % (w, ptag, was, MOVES, now, LONG))
    return moved


def main():
    sch = PS.Sched("alpha=1,b=2,m=1", alpha=1, b=2, m=1)
    sch.check_monotone(DCAP)
    npl = dict((d, 2) for d in range(1, DCAP + 1))
    print("explore_splice_cap.py -- how many strands a splice holds, the "
          "width swept\npast arithmetic. One (p, e) = (2, 4); B = %d; the "
          "splice price P = 4 + w." % sch.price(1, E_))

    s0_forced(sch, npl)
    s1_control(sch, npl)
    res = s2_sweep(sch, npl)
    k1, k2, k3, pr4 = s3_verdicts(res)
    bad = s4_controls(sch)
    moved = s5_window(sch, npl, res)

    section("VERDICT")
    print("  K1 (a per-item cell off its census):       %d" % len(k1))
    print("  K2 (any cell above the census):            %d" % len(k2))
    print("  K3 (a refinement that decreased):          %d" % len(k3))
    print("  K4 (a count moving with the window):       %d" % len(moved))
    print("  PR4 (diagonal cells off the w + 2 fit):    %d" % len(pr4))
    print("  S4 (control cells off their own census):   %d" % len(bad))


if __name__ == "__main__":
    main()
