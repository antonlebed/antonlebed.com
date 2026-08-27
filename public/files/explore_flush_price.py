"""What does the FLUSH cost? The same game with and without its
terminal condition, at every cell the grid and the band have decided.

THE QUESTION
------------
explore_lookahead_band.py F5 reads the ten band cells as the flush
costing ONE unit: there the overlap bound GRANTS the completion reader
lookahead 1 -- the star is deliverable one digit ahead -- and the
integer reader is denied it, reading 2. But that "one unit" is measured
against a SUFFICIENT bound, not against a reader. H3 overshoots and the
grid says so: silver x2 reads 2 where H3 says 3, and 0 where H3 says 2
and where H3 says 1. So the quantity "what the flush costs" has never
been given an object of its own, and the sharper claim the thread wants
-- IF THE FLUSH ALWAYS COSTS EXACTLY ONE UNIT, THAT IS THE LAW AND "NO
CELL READS AT 1" IS ITS COROLLARY -- cannot be tested against a bound.

It can be tested against the same game with its terminal condition
removed. Game.solve runs two nested fixpoints: a SAFETY fixpoint (keep
some branch alive, i.e. some output digit whose every reply stays in the
surviving set) and then a FLUSH refinement (from every surviving state a
(0, 0)-holding state must be reachable under zero input, or the state
leaves and safety is re-run). Stop after the first and the reader is
released from ever finishing: it must write forever without leaving the
box and need never land on the value. Write

    c_int  = the least lookahead at which the full game wins
    c_saf  = the least lookahead at which the safety fixpoint alone wins

both inside ONE fixed box, and the FLUSH PRICE is c_int - c_saf.

WHOSE VOCABULARY IS THE SUSPICION WRITTEN IN? It arrives in
H3's vocabulary -- "one unit against the bound's grant" -- and its own
object is not a bound but a game. c_saf is that object. It is NOT the
completion reader's minimum and this rig never claims it is: see H2.

THE HAND-ATTACK (on paper, before the engine)
---------------------------------------------
H1  THE INDEX CONVENTION, RE-DERIVED FROM THE ENGINE AND NOT FROM
    MEMORY. Game.step emits y at position pos and then reads input index
    pos + look + 1; pre_states consumes d_0..d_look before position 0.
    So a reader at lookahead c emits e_t having seen d_0..d_{t+c}, which
    is the parent's convention and the one both numbers below are in.
H2  WHAT c_saf IS NOT, AND WHICH WAY THE ERROR RUNS. c_saf is not the
    COMPLETION reader's minimum, and the gap between them is not only
    the box. The completion reader is a map on INFINITE STRINGS: it
    tracks no integer offsets at all and its whole requirement is that
    the real star stay in range. c_saf's reader tracks the offset set,
    is confined in the conjugate coordinate as well, and carries a bconj
    DERIVED on a run that ACCEPTS (explore_lookahead_band.py F6's
    telescoping is over an accepting tail) -- a hypothesis dropping the
    flush removes. THE DIRECTION CLAIMED HERE IS WRONG AND THE ARGUMENT
    FOR IT IS DEAD (explore_completion_reader.py F6). What stood here
    was this: a box-confined safe strategy holds
    |real/theta| <= breal at every step, "which IS the completion
    reader's requirement", so c_comp <= c_saf and c_int - c_saf
    UNDERSTATES c_int - c_comp. breal is NOT that requirement. It is
    D9's box widened by SLACK and a +1, and it is far wider than the
    level range a residual has to sit in to be completable at all, so a
    branch holds inside the box with its star out of range and safety
    does not imply completability. That is not an objection but a
    printed fact: at sqrt3-1 [1,2] x3, (s, s_0) = (1, 0), a safety
    strategy at this rig's own c_saf = 2 reaches a SAFE state with no
    completable branch at all in 300 of 300 runs -- and the box's own
    margin over completability is printed there, so the reading is
    safety's and not the pruning's. The INEQUALITY
    survives as an observation and has no proof under it: c_comp,
    measured by an interval game with no box in it, EQUALS c_saf at all
    110 grid cells where both read and at all eleven cells priced below,
    never above and never below -- and at the ten grid cells that game
    left open, decided since under the circle's own lifts
    (explore_completion_lift.py): 130 cells, none undecided. So the
    prices printed here understate
    nothing -- they are the gap wherever the gap can be checked. (The
    tempting version of the dead argument -- "safety inside the box
    implies safety, so c_saf bounds the UNCONFINED safety minimum" -- is
    true and useless: with no box no branch ever dies and unconfined
    safety is won at lookahead 0.) A printed 2 kills "at most one unit"
    outright; a printed 1 is read as the price and, since the
    measurement landed, as the gap.
H3  THE PRICE IS NON-NEGATIVE BY CONSTRUCTION, so a negative print is a
    rig fault and not a finding: the full game's winning set is the
    safety fixpoint intersected with a further condition, and dropping a
    requirement cannot raise a minimum. This is a control, not a
    prediction.
H4  WHERE IT CAN BLOW UP. The safety fixpoint can be non-empty while no
    INITIAL state sits in it, so the verdict is `all(init in W)` and
    never `W != {}` -- the same test Game.solve's own verdict uses. And
    the fixpoint must iterate to closure: one removal can strand a
    predecessor, so the loop re-runs until nothing changes.
H5  WHAT A ZERO PRICE MEANS AT A CELL READING 0. Where the digitwise
    writing fits, e_k = m d_k is admissible and the residual is 0 at
    every position, so the flush is free and c_int = c_saf = 0. Any
    other reading at such a cell is a rig fault; it is C1's second leg.
TRANSPLANT, marked: the game, its box, its bounds and its grid are
explore_redundant_ostrowski.py's, and the band cells and their frozen
lookaheads are explore_lookahead_band.py F3's. Nothing here re-derives
either; this rig only removes one fixpoint and re-reads the same cells.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS,
never what they would mean).
  C1 (control, run FIRST; nothing below is read if any leg is red)
     (a) THE RIG REPRODUCES THE PUBLISHED GRID'S c_int. The four parent
         rows -- silver and bronze, x2 and x3, over the six (s, s_0)
         pairs -- print explore_lookahead_band.py's frozen PARENT
         lookaheads exactly, through this rig's own Game calls.
     (b) c_saf = 0 AT EVERY CELL PRINTING c_int = 0 (H5).
     (c) c_saf <= c_int AT EVERY CELL PRINTED ANYWHERE (H3).
  P1 THE PRICE OVER THE PUBLISHED GRID. For the six windows, x2..x5 and
     the six (s, s_0) pairs -- 144 cells, the 120 that read at all and
     the zero-slack column that reads at none -- the rig prints c_int,
     c_saf and their difference per cell, and the tally of differences
     over the cells where both are finite.
  P2 THE PRICE AT THE TEN BAND CELLS, printed one per cell against F3's
     frozen c_int. These are the cells where the bound grants the
     completion reader 1, so this is the number the thread's claim is
     about.
  P3 KILL, AS AN OBSERVABLE: a printed difference of 2 or more at any
     cell of P1 or P2. A printed difference of 0 at a BAND cell is not a
     kill and is its own reading -- it would say the extra unit there is
     bought by the box's confinement rather than by the terminal
     condition.
  P4 the state count per cell and the wall-clock, printed; peak under
     memwatch named in the run record.

THE DESIGN
----------
Stages: s0 the C1 control, s1 the P1 grid, s2 the P2 band cells. One
ascending loop over lookahead serves both numbers at once -- Game's
constructor already runs the full solve, so `g.wins` is c_int's test and
the safety fixpoint recomputed from `g.trans` and `g.alive` is c_saf's,
off the same build. The safety fixpoint is recomputed here rather than
taken from Game because Game does not keep it: solve overwrites W with
the flush-refined set. Ascend to the parent's LOOKCAP and print "-"
where neither wins by it.

Stage and cell selection come from the environment (PRICE_STAGES,
PRICE_CELLS) so a heavy cell runs as its own process. Memory: the state
space is built explicitly and grows with the output cap a + s; run under
memwatch.py.

FINDINGS (entered post-run; every number below sits in this file's
printed output. Runs under memwatch at the 512 MB default, peaks as
WORKING SET: s0 in 2 s at 41.0 MB; s1 in 22 s at 86.6 MB; the band in
two tiers, 6 s at 173.9 MB for the seven cheapest and 7 s at 345.0 MB
for the three above them; s3 in 1 s at 51.0 MB. Nothing ran bare and
nothing was killed.)

F1  THE CONTROL HOLDS (C1). All four parent rows print PARENT's
    lookaheads exactly through this rig's own calls -- bronze x2
    "- 2 2 2 2 0", bronze x3 "- 2 2 2 2 2", silver x2 "- 2 2 2 0 0",
    silver x3 "- 3 2 2 2 2" -- and 0 bad on both invariants: c_saf = 0
    at every cell reading c_int = 0, and c_saf <= c_int everywhere. The
    lookahead cap is the PARENT'S PER CELL and not a constant, which is
    what makes the finite-cell count agree with the corpus's own: 120,
    the grid's 144 less its zero-slack column, every one of which the
    theorem answers rather than a cap.
F2  THE PRICE OVER THE PUBLISHED GRID (P1), 120 finite cells: price 0 at
    91, price 1 at 28, price 2 at ONE. And where a nonzero price LANDS,
    printed as (c_int, c_saf) pairs: (2, 1) at 26 cells, (2, 0) at one
    -- V1 (1,1,1,2) x3 at s = s_0 = 3 -- and (4, 3) at two, V1
    (1,1,1,2) x5 at (s, s_0) = (1, 0) and (1, 1).
F3  THE PRICE AT THE TEN BAND CELLS (P2). Nine print 1, every one of
    them (2, 1). The tenth, V2 (2,1,3,1) x3 at s = 5, prints (2, 0) --
    price 2. So the band, the place the claim was read off, itself
    carries a counterexample. (The band is searched to LOOKCAP and not
    to the parent's H3 cap: at a band cell H3 returns 1 by definition
    and c_int is 2, H3 bounding the COMPLETION reader and being no upper
    bound on the integer one -- the one place the parent's own cap rule
    does not transfer, and it transfers everywhere in the grid only
    because the grid has no band cell in it.)
F4  THE KILL FIRED (P3). "The flush always costs exactly one unit" is
    FALSE. Two cells print 2, one in the grid and one in the band, and
    both are period-4 windows at x3 where the safety reader needs NO
    lookahead at all. The claim that would have made "no cell reads at
    lookahead 1" a corollary does not hold, and the corollary route is
    closed with it. What F5 of the parent said stays true as stated --
    at those ten cells the flush costs one unit AGAINST H3'S GRANT --
    and it does not generalize to a law about the flush.
F5  WHAT SURVIVES. Two statements, and they are not equally strong.
    (a) THE ROBUST ONE. c_int = 1 at ZERO cells of the 130, while c_saf
    is 1 at 35 of them (26 in the grid, 9 in the band) and 0 at two
    more, and at every one of those 37 the integer reader reads 2. So
    the terminal condition is exactly what forbids lookahead 1: the
    safety reader does read there and the flush is the whole of what
    denies it. This does not depend on any regularity in the price.
    (SETTLED, explore_flush_floor.py: the floor is a RULE, proved --
    the flushed state is the exposed one, and a late digit at its cap
    needs the two levels below it -- and c_int = max(c_saf, L*) at all
    130 cells, L* the flushed-state bound, which is where the (4, 3)
    cells of (b) come from.)
    (b) THE WEAKER ONE, and the capped first pass overstated it. Where
    the price is nonzero the integer reader lands on 2 at 37 of 39
    cells; the two exceptions are V1 (1,1,1,2) x5 at (1, 0) and (1, 1),
    which land on 4. So the landing point is a PATTERN with two
    counterexamples in 130 cells and not a law, and "the flush never
    carries the reader past 2" is simply false. What holds without
    exception is the weaker bound: the price itself is 0, 1 or 2 at
    every one of the 130 cells and never more.
F6  THE TWO PRICE-2 CELLS OPENED (s3, added in the audit; F4 rests on a
    boolean and a fixpoint bug forges exactly that boolean). At both
    cells the safety fixpoint at lookahead 0 is large and CONTAINS the
    initial states -- 375 of 2,382 alive at V1, 640 of 3,514 at V2 --
    while Game's own flush-refined set is EMPTY, inits excluded; the
    same at lookahead 1 (703 and 1,157 safe, 0 flushing); and at
    lookahead 2 both hold (1,114 safe / 784 flushing, 1,964 / 1,387).
    So the terminal condition annihilates a non-empty safety fixpoint
    twice over rather than trimming it, which is what a price of 2 has
    to look like from inside and is not what a stalled fixpoint looks
    like.

TIER. F2 and F3 are exhaustive computations at the cells named, each
decided exactly by the automaton inside the parent's box: at 120 grid
cells and 10 band cells the two numbers are what this game prints. F4 is
a KILL and needs only its two witnesses. F5(a) is an OBSERVATION at 130
cells; F5(b) is a PATTERN with two counterexamples inside its own
evidence, which is why it is written as one. No mechanism is derived for
either. H2's denial is CORRECTED above and the correction runs
the other way: c_comp was measured (explore_completion_reader.py) and
equals c_saf at every cell BOTH rigs decide, so the prices here are
the gap and not a floor on it, and the flush is not part of what fills
it but the whole of it -- the offset tracking and the conjugate
confinement cost nothing in lookahead at any cell read.
"""

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_limit_maps import tail_caps                # noqa: E402
from explore_limit_column import Window                 # noqa: E402
from explore_redundant_ostrowski import (               # noqa: E402
    GRID, LOOKCAP, WINDOWS, Game, h3_bound)
from explore_lookahead_band import PARENT               # noqa: E402

STAGES = os.environ.get("PRICE_STAGES", "s0,s1,s2").split(",")

# explore_lookahead_band.py F3, frozen here as the band's answer key:
# (window name, period, m, s) -> the integer reader's lookahead.
BAND = [
    ("[4]", (4,), 2, 3, 2),
    ("[5]", (5,), 2, 3, 2),
    ("[5]", (5,), 2, 4, 2),
    ("bronze [3]", (3,), 3, 5, 2),
    ("V2 (2,1,3,1)", (2, 1, 3, 1), 3, 5, 2),
    ("[4]", (4,), 3, 5, 2),
    ("[5]", (5,), 3, 5, 2),
    ("[4]", (4,), 3, 7, 2),
    ("bronze [3]", (3,), 4, 8, 2),
    ("[5]", (5,), 3, 9, 2),
]


def window_of(period):
    return Window(tail_caps(period), len(period))


def safety_wins(g):
    """H4: the safety fixpoint alone, iterated to closure, at the inits.

    W starts as every state with a branch left (an empty branch set is
    already lost) and sheds any state with no output digit whose every
    reply is still in W. One removal can strand a predecessor, so the
    loop runs until nothing changes -- and the verdict is that every
    INITIAL state survives, never that W is non-empty.
    """
    W = set(i for i in g.trans if g.alive[i])
    changed = True
    while changed:
        changed = False
        for s in list(W):
            ok = any(all(s2 in W for _x, s2 in succ)
                     for succ in g.trans[s].values())
            if not ok:
                W.discard(s)
                changed = True
    return all(s in W for s in g.init)


def price(win, m, s, s0, top=None):
    """c_int, c_saf and the state count, off one ascending build loop.

    The cap is the PARENT's and not a constant: s1_grid searches to H3's
    bound wherever one exists and to LOOKCAP only where none does, and a
    flat LOOKCAP here would print "-" at the cells reading 4..6 and count
    them as not reading at all.
    """
    if top is None:
        hb = h3_bound(win, m, s, s0)
        top = LOOKCAP if hb is None else hb
    c_int = c_saf = None
    states = 0
    for look in range(top + 1):
        g = Game(win, 1, m, (0,), look, s, s0)
        states = max(states, g.n_states)
        if c_saf is None and safety_wins(g):
            c_saf = look
        if c_int is None and g.wins:
            c_int = look
        if c_int is not None:
            break
    return c_int, c_saf, states


def fmt(v):
    return "-" if v is None else str(v)


def s0_control():
    print("== s0  C1: the parent rows reproduced, and the two invariants")
    bad = 0
    for (name, m), (looks, _h3) in sorted(PARENT.items()):
        period = dict(WINDOWS)[name]
        win = window_of(period)
        row_i, row_s = [], []
        for (s, s_0), want in zip(GRID, looks):
            c_int, c_saf, _n = price(win, m, s, s_0)
            row_i.append(fmt(c_int))
            row_s.append(fmt(c_saf))
            if c_int != want:
                print("    BAD c_int %s x%d (s,s0)=(%d,%d): %s want %s"
                      % (name, m, s, s_0, fmt(c_int), fmt(want)))
                bad += 1
            if c_int == 0 and c_saf != 0:                     # C1b / H5
                print("    BAD c_saf at a digitwise cell %s x%d (%d,%d): %s"
                      % (name, m, s, s_0, fmt(c_saf)))
                bad += 1
            if (c_int is not None and c_saf is not None
                    and c_saf > c_int):                       # C1c / H3
                print("    BAD c_saf > c_int at %s x%d (%d,%d): %s > %s"
                      % (name, m, s, s_0, fmt(c_saf), fmt(c_int)))
                bad += 1
        print("  %-14s x%d  c_int %s   c_saf %s"
              % (name, m, " ".join(row_i), " ".join(row_s)))
    print("  control: %d bad" % bad)
    return bad


def s1_grid():
    print("== s1  P1: the price over the published grid")
    tally, pairs = {}, {}
    for name, period in WINDOWS:
        win = window_of(period)
        for m in (2, 3, 4, 5):
            row = []
            for s, s_0 in GRID:
                c_int, c_saf, _n = price(win, m, s, s_0)
                row.append("%s/%s" % (fmt(c_int), fmt(c_saf)))
                if c_int is not None and c_saf is not None:
                    tally[c_int - c_saf] = tally.get(c_int - c_saf, 0) + 1
                    pairs[(c_int, c_saf)] = pairs.get((c_int, c_saf), 0) + 1
            print("  %-14s x%d  %s" % (name, m, "  ".join(row)))
    print("  c_int/c_saf per (s, s_0) cell; price tally over the cells "
          "where both are finite:")
    for d in sorted(tally):
        print("    price %d: %d cells" % (d, tally[d]))
    print("  and where a nonzero price LANDS, as (c_int, c_saf) pairs:")
    for pr in sorted(pairs):
        if pr[0] != pr[1]:
            print("    (c_int %d, c_saf %d): %d cells" % (pr[0], pr[1],
                                                          pairs[pr]))
    print("  finite cells: %d;  c_int = 1 anywhere: %d cells"
          % (sum(tally.values()),
             sum(n for pr, n in pairs.items() if pr[0] == 1)))
    return tally


def s2_band():
    print("== s2  P2: the price at the ten band cells")
    cells = os.environ.get("PRICE_CELLS")
    pick = set(int(i) for i in cells.split(",")) if cells else None
    for i, (name, period, m, s, want) in enumerate(BAND):
        if pick is not None and i not in pick:
            continue
        win = window_of(period)
        t0 = time.time()
        # NOT the parent's H3 cap here: at a band cell H3 returns 1 by
        # definition, and c_int is 2 -- H3 bounds the COMPLETION reader
        # and is no upper bound on the integer one. LOOKCAP, as the band
        # rig's own verdict stage used.
        c_int, c_saf, n = price(win, m, s, s, top=LOOKCAP)
        flag = "" if c_int == want else "   BAD c_int, want %d" % want
        pr = ("-" if (c_int is None or c_saf is None)
              else str(c_int - c_saf))
        print("  %-14s x%d s=%-2d  c_int %s  c_saf %s  price %s  "
              "states %d  %.0f s%s"
              % (name, m, s, fmt(c_int), fmt(c_saf), pr, n,
                 time.time() - t0, flag))


def s3_open(cells):
    """Added in the audit: the fixpoint SIZES at a named cell.

    P1 and P2 read a boolean per lookahead, and a price of 2 rests on
    c_saf = 0 -- the safety reader needing no lookahead where the
    integer reader needs two. That is the one reading a fixpoint bug
    would forge, so the two cells that print it are opened: per
    lookahead, how many states have a branch left, how many survive the
    safety fixpoint, how many survive Game's own flush-refined solve,
    and whether the INITIAL states sit in each.
    """
    print("== s3  the fixpoint sizes at the cells printing price 2")
    for name, period, m, s, s0 in cells:
        win = window_of(period)
        print("  %s x%d s=%d s0=%d" % (name, m, s, s0))
        for look in (0, 1, 2):
            g = Game(win, 1, m, (0,), look, s, s0)
            W = set(i for i in g.trans if g.alive[i])
            changed = True
            while changed:
                changed = False
                for st in list(W):
                    if not any(all(s2 in W for _x, s2 in succ)
                               for succ in g.trans[st].values()):
                        W.discard(st)
                        changed = True
            print("    c=%d  states %6d  alive %6d  safe %6d (inits in: "
                  "%s)  flushing %6d (inits in: %s)"
                  % (look, g.n_states, sum(g.alive), len(W),
                     all(i in W for i in g.init), len(g.W),
                     all(i in g.W for i in g.init)))


def main():
    t0 = time.time()
    if "s0" in STAGES:
        if s0_control():
            print("CONTROL RED -- nothing below is read")
            return
    if "s1" in STAGES:
        s1_grid()
    if "s2" in STAGES:
        s2_band()
    if "s3" in STAGES:
        s3_open([("V1 (1,1,1,2)", (1, 1, 1, 2), 3, 3, 3),
                 ("V2 (2,1,3,1)", (2, 1, 3, 1), 3, 5, 5)])
    print("total %.0f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
