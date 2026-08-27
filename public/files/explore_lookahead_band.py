"""Is "no cell reads at lookahead 1" a law, or a fact about one grid's
slack range? The completion bound's own crossing point, computed and
then run.

THE QUESTION
------------
explore_redundant_ostrowski.py F6 reads NO CELL READS AT 1 off a
120-cell grid and files it as a pattern at that grid's scope, adding a
second clause that reads as a general fact: "H3 grants 1 only at
s >= 2m - 1, past the digitwise line, so the bound never asks for it
either". Two lines are in play at a window with largest partial quotient
a_max, for the map x m at slack s = s_0:

    the DIGITWISE line -- lookahead 0 suffices, e_k = m d_k being
        admissible -- at s >= (m - 1) a_max;
    H3 at c = 1 -- the COMPLETION reader exists at lookahead 1 -- at
        1 + s >= 2m together with 2m|theta_1| <= E.

They CROSS. (m - 1) a_max > 2m - 1 exactly when a_max > 2 + 1/(m - 1),
so at a_max = 3 with m >= 3, or a_max >= 4 with m = 2, there is a BAND

    2m - 1 <= s < (m - 1) a_max

of slacks where the completion reader exists at lookahead 1 and the
digitwise writing does not fit. The published grid never visits it: its
six windows have a_max 1, 2, 3, 2, 2, 3 and its slacks stop at 3, while
the band at a_max = 3 opens at m = 3, s = 5. So F6's parenthetical is
true OF THAT GRID, and the pattern's whole evidential base sits on one
side of a line the bound itself draws. This rig goes to the other side.

THE HAND-ATTACK (on paper, before the engine)
---------------------------------------------
H1  THE CONSTANT WINDOW, CLOSED. At [a], alpha^2 + a alpha - 1 = 0 and
    theta_0 = alpha, theta_1 = a alpha - 1 = -alpha^2, and inductively
    theta_k = (-1)^k alpha^(k+1). So |theta_1| = alpha^2 and
    sum_{k>=1}|theta_k| = alpha^2/(1 - alpha), and E = s_0 alpha +
    s alpha^2/(1 - alpha) at s = s_0.
H2  TWO BAND CELLS, BOTH HALVES OF H3 CHECKED BY HAND.
      [4], m = 2, s = s_0 = 3: alpha = sqrt5 - 2 = 0.23607, 1 + s = 4 =
      2m (equality), E = 3(0.23607) + 3(0.07295) = 0.92705 against
      2m|theta_1| = 0.22291. Digitwise wants s >= 4. IN THE BAND.
      [3], m = 3, s = s_0 = 5: alpha = (sqrt13 - 3)/2 = 0.30278,
      1 + s = 6 = 2m (equality), E = 5(0.30278) + 5(0.13148) = 2.17129
      against 2m|theta_1| = 0.55004. Digitwise wants s >= 6. IN THE
      BAND.
    Both sit at 1 + s = 2m exactly, the band's LEFT ENDPOINT -- where
    H3 first grants c = 1, and the cheapest place in it, the state
    space growing with the caps a + s.
H3' WHAT EACH VERDICT WOULD MEAN is weighed after the run; the kills
    below are prints.
TRANSPLANT, marked: the automaton, its box and its bounds are
explore_redundant_ostrowski.py's, used at slacks ABOVE the range that
grid ever ran -- the box's breal/bconj scale with (m_o(1 + s) + m_i),
so nothing here is read until the control has reproduced that grid's own
cells through this rig's calls. (The control reaches s = 3 and this rig
reads to s = 9; what carries the gap is F6, added in the audit.)

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS,
never what they would mean).
  C1 (control, run FIRST; nothing below is read if it is red) THE RIG
     REPRODUCES THE PUBLISHED GRID. Every cell of F3's silver and bronze
     rows for x2 and x3, and its H3 bound beside each, printed through
     this rig's own calls and compared against the frozen F3 table; and
     every winning cell's strategy certified on n < 1500 for value,
     caps and flush.
  P1 THE BAND IS COMPUTED, AND THE PUBLISHED GRID'S IS EMPTY. For each
     (window, m) over the six published windows plus [4] and [5], the
     rig prints the digitwise line, the smallest s at which h3_bound
     returns 1, and the band's integer slacks. Every published-grid
     window prints a band that misses s <= 3 entirely, and the published
     grid's OWN 144 cells are swept for band membership one by one --
     the band hunt runs the DIAGONAL s = s_0 and two of that grid's
     six (s, s_0) pairs are off it, so the emptiness is asked of the
     cells themselves and not of the diagonal through them.
  P2 THE VERDICT, and it is the sharp one. At each band cell the exact
     periodic-window automaton prints the integer reader's minimal
     lookahead. A printed 1 at any band cell is read as F6's "no cell
     reads at 1" being a fact about the grid's slack range. A printed 2
     or more at every band cell is read as the integer reader sitting
     strictly behind the completion reader THERE.
  P3 the state count per cell and the wall-clock, printed; peak under
     memwatch named in the run record.

THE DESIGN
----------
Stages: s0 the C1 control against the frozen F3 table; s1 the P1 band
computation; s2 the P2 verdict at the band cells. The engine is
explore_redundant_ostrowski.Game through its own min_look, h3_bound and
digitwise_bound -- same game, same box, same bounds; only the window set
and the slack range move. Stage and cell selection come from the
environment (BAND_STAGES, BAND_CELLS) so a heavy cell runs as its own
process. Memory: the state space is built explicitly and grows with the
output cap a + s; run under memwatch.py.

FINDINGS (entered post-run; every number below sits in this file's
printed output. Runs under memwatch at the 512 MB default, peaks as
WORKING SET: s0 in 4 s, peak 54.1 MB; s0+s1 in 4 s, peak 54.3 MB; the
verdict cells in tiers, 8 s at peak 238.8 MB for the seven cheapest,
2 s at 145.9 MB and 6 s at 409.8 MB for the three above them. Nothing
ran bare and nothing was killed.)

F1  THE CONTROL HOLDS (C1). All four PARENT rows print F3's lookaheads
    and F3's H3 bounds exactly -- silver x2 "- 2 2 2 0 0 / - 3 2 2 2 1",
    silver x3 "- 3 2 2 2 2 / - 4 3 3 2 2", bronze x2 "- 2 2 2 2 0 /
    - 3 2 2 2 1", bronze x3 "- 2 2 2 2 2 / - 3 3 2 2 2" -- with every
    winning cell's strategy 0 bad on n < 1500. So the automaton and its
    box are the published ones, which is what the marked transplant
    asks before a slack above that grid's range is read.
F2  THE BAND IS REAL AND THE PUBLISHED GRID'S IS EMPTY (P1). Over the
    six published windows plus [4] and [5], at m = 2..5: ZERO band cells
    among the published grid's OWN 144 cells -- swept one by one, the
    the two off-diagonal (s, s_0) pairs included, since the band hunt runs
    the diagonal; the grid is 6 x 4 x 6 = 144 cells of which 120 read at
    all, its zero-slack column reading at no lookahead, so the band
    sweep is over the 144 and the PATTERN's base is the 120 -- and 42
    band cells outside that
    over the hunted range s <= 12 -- a count the range CAPS, three of
    the bands ([4] x5, [5] x4, [5] x5) still open at s = 12, which is
    what their digitwise line printing "-" says. The crossing sits
    exactly where the question put it -- a_max 1 and 2 give
    an empty band at every m (golden, silver, sqrt3-1, V1), a_max = 3
    opens one at m >= 3 (bronze and V2: s = 5 at x3, {7, 8} at x4,
    {9, 10, 11} at x5), and a_max >= 4 opens one at m = 2 already
    ([4] x2 at s = 3, [5] x2 at s = {3, 4}). The published grid misses
    it by BOTH coordinates at once: its windows stop at a_max = 3, where
    the band opens at s = 5, and its slacks stop at 3.
F3  THE INTEGER READER STILL DOES NOT READ AT 1 (P2), at ten band cells
    across both crossing regimes -- and every one prints 2:
        cell                lookahead   states
        [4]      x2  s=3        2        5,692
        [5]      x2  s=3        2       10,634
        [5]      x2  s=4        2       12,006
        bronze   x3  s=5        2        7,892
        V2       x3  s=5        2        8,454
        [4]      x3  s=5        2       14,322
        [5]      x3  s=5        2       21,639
        [4]      x3  s=7        2       18,922
        bronze   x4  s=8        2       13,540
        [5]      x3  s=9        2       34,771
    every strategy certified 0 bad on n < 1500 for value, caps and
    flush. Six sit at the band's LEFT ENDPOINT (1 + s = 2m exactly) and
    four in its interior, the highest at 1 + s = 10 against 2m = 6.
F4  WHAT THIS MOVES, AND WHAT IT DOES NOT. The parent's F6 files "no
    cell reads at 1" as a pattern and adds that the bound never asks for
    1 either, "H3 grants 1 only at s >= 2m - 1, past the digitwise
    line". That second clause is true of THAT GRID and is not the
    general fact it reads as: the two lines cross at
    a_max > 2 + 1/(m - 1), and past the crossing the bound asks for 1 at
    every slack in the band. So before this run the whole evidential
    base for "never 1" sat on one side of a line the bound itself draws,
    and the cells where the bound would have granted 1 had never been
    run. They have now, and they read at 2. The statement is still a
    PATTERN -- 130 cells rather than 120 -- but its base is different in
    kind, because it now includes the cells that could have broken it.
F5  THE SHARPER "DOES NOT DESCEND". A band cell is a place where the
    completion reader exists at lookahead 1 -- the star invariant is
    deliverable one digit ahead -- and the integer reader is denied it.
    So what costs the extra unit at these ten cells is the FLUSH alone,
    isolated from the star: the corpus's standing specimen for the
    completion reader not descending is the golden residual 3, a
    negative at one window showing no tie-break on the star repairs it,
    where this is a two-parameter family in which the star is satisfied
    at exactly the lookahead the flush refuses. That the band's floor is
    2 and not higher is the other half: against the bound's GRANT of
    lookahead 1 the flush costs one unit and no more. Against the
    completion reader's own minimum it costs at least that -- H3 is
    sufficient and not necessary, so a band cell's completion reader may
    read below 1 and this rig never asks whether it does.
    (Settled since, by explore_flush_price.py: what stands above is the
    cost against H3'S GRANT and only that, and it holds at all ten cells.
    Priced instead against the same game with its terminal condition
    dropped, the flush costs 1 at nine of these cells and 2 at the tenth,
    so there is no one-unit law behind the reading and "no cell reads at
    1" is not a corollary of one. What that pricing does settle is that
    the terminal condition is the whole of what forbids lookahead 1.
    And the question left open in the sentence above it -- whether a
    band cell's completion reader reads BELOW 1 -- is answered by
    explore_completion_reader.py, which measures that reader directly
    with an interval game and no box in it: at nine of the ten cells it
    reads exactly 1, so the flush's unit there is the whole distance to
    it and not a floor, and at the tenth it reads 0 against an integer
    reader at 2.)

F6  WHY A LOSS AT THESE SLACKS IS REAL (added in the audit; F3 is
    nothing without it). Every band verdict is a WIN at 2 on top of
    LOSSES at 0 and 1, and a loss off a pruned game reads nothing
    unless the pruning box holds every branch that can still accept.
    The control reaches s = 3 and the band is read to s = 9, so the
    control cannot be what carries it. What carries it is that the box
    is DERIVED and not tuned: on an accepting run D_k = -sum_{i>=k}
    (m_o e_i - m_i d'_i) theta_i (explore_limit_maps.py D9), and with
    the caps raised the same telescoping sum_{i>=k}|theta_i| <=
    |theta_{k-1}| + |theta_k| gives |D_k/theta_k| <= (m_o(1 + s) +
    m_i)(|theta_{k-1}| + |theta_k|)/|theta_k| -- which is Game.breal
    term for term, s inside it. The conjugate side carries m_o(a_max +
    s) + m_i a_max the same way, and the seed range obeys |M| <= |D_0|
    + |c| alpha < 2(m_o(1 + s) + m_i) + cmax, which is Game's mmax less
    the +1 of margin it carries. So the box grows with the slack by
    construction, the
    branch it prunes is one that could not have accepted, and a loss at
    s = 9 reads what a loss at s = 1 reads. The float slop is the
    parent's SLACK = 1.05 on top.

TIER. The band is a property -- (m - 1)a_max > 2m - 1 iff
a_max > 2 + 1/(m - 1) is algebra, and both halves of H3 are computed per
cell by the parent's own h3_bound. F2's emptiness at the published grid
is exhaustive over that grid. F3 is an observation at ten cells: the
automaton is exact at a periodic window, so each cell is decided, but
ten cells decide ten cells. "No cell reads at 1" is a PATTERN and this
rig does not make it a rule. (SETTLED, explore_flush_floor.py: it is a
RULE, proved at every periodic window -- the flushed state is the
exposed one, and a late digit at its cap needs the two levels below it
-- and the band cells are its sharpest exhibit; every figure above
survives at its own scope.)
"""

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_limit_maps import tail_caps                # noqa: E402
from explore_limit_column import Window                 # noqa: E402
from explore_redundant_ostrowski import (               # noqa: E402
    GRID, WINDOWS, check_strategy, digitwise_bound, h3_bound, min_look)

STAGES = os.environ.get("BAND_STAGES", "s0,s1,s2").split(",")
SMAX = 12                    # how far up the slack axis the band is hunted

# F3's printed table, frozen here as the control's answer key: the
# lookahead row and the H3 row over GRID for each (window, map).
PARENT = {
    ("silver [2]", 2): ([None, 2, 2, 2, 0, 0], [None, 3, 2, 2, 2, 1]),
    ("silver [2]", 3): ([None, 3, 2, 2, 2, 2], [None, 4, 3, 3, 2, 2]),
    ("bronze [3]", 2): ([None, 2, 2, 2, 2, 0], [None, 3, 2, 2, 2, 1]),
    ("bronze [3]", 3): ([None, 2, 2, 2, 2, 2], [None, 3, 3, 2, 2, 2]),
}

# the windows the band is hunted over: the published six plus two the
# published set has no member of -- a_max above the crossing point.
EXTRA = [("[4]", (4,)), ("[5]", (5,))]


def window_of(period):
    return Window(tail_caps(period), len(period))


def in_band(win, m, s, s0):
    """A cell is in the band iff H3 grants c = 1 and digitwise does not."""
    return (h3_bound(win, m, s, s0) == 1
            and digitwise_bound(win, m, s, s0) is None)


def band_of(win, m):
    """P1: the digitwise line, H3's first c = 1 slack, and the band.

    Hunted along the DIAGONAL s = s_0; the published grid's own six
    (s, s_0) cells, two of them off that diagonal, are swept
    separately in s1 so the emptiness is a print and not an argument.
    """
    line = None
    first1 = None
    band = []
    for s in range(0, SMAX + 1):
        db = digitwise_bound(win, m, s, s)
        hb = h3_bound(win, m, s, s)
        if db == 0 and line is None:
            line = s
        if hb == 1 and first1 is None:
            first1 = s
        if hb == 1 and db is None:
            band.append(s)
    return line, first1, band


def s0_control():
    print("== s0  C1: the published grid reproduced through this rig")
    bad = 0
    for name, period in WINDOWS:
        for m in (2, 3):
            key = (name, m)
            if key not in PARENT:
                continue
            win = window_of(period)
            caps = tail_caps(period)
            looks, bounds = [], []
            for s, s0 in GRID:
                hb = h3_bound(win, m, s, s0)
                look, g = min_look(win, 1, m, (0,), s, s0,
                                   top=(3 if hb is None else hb))
                looks.append(look)
                bounds.append(hb)
                if g is not None:
                    bad += check_strategy(g, caps, "%s x%d (%d,%d)"
                                          % (name, m, s, s0))
            want_l, want_b = PARENT[key]
            ok = (looks == want_l and bounds == want_b)
            bad += 0 if ok else 1
            print("  %-12s x%d  look %s  H3 %s  %s"
                  % (name, m,
                     " ".join("-" if v is None else str(v) for v in looks),
                     " ".join("-" if v is None else str(v) for v in bounds),
                     "ok" if ok else "MISMATCH want look %s H3 %s"
                     % (want_l, want_b)))
    print("  C1 %s" % ("GREEN" if bad == 0 else "RED (%d)" % bad))
    return bad == 0


def s1_band():
    print("== s1  P1: the digitwise line, H3's first c = 1, and the band")
    cells = []
    for name, period in WINDOWS + EXTRA:
        win = window_of(period)
        for m in (2, 3, 4, 5):
            line, first1, band = band_of(win, m)
            print("  %-14s x%d  digitwise s>=%s   H3 c=1 at s>=%s   band %s"
                  % (name, m,
                     "-" if line is None else line,
                     "-" if first1 is None else first1,
                     band if band else "(empty)"))
            for s in band:
                cells.append((name, period, m, s))
    ongrid = 0
    for name, period in WINDOWS:
        win = window_of(period)
        for m in (2, 3, 4, 5):
            for s, s0 in GRID:
                if in_band(win, m, s, s0):
                    ongrid += 1
                    print("    ON THE GRID: %s x%d (%d,%d)"
                          % (name, m, s, s0))
    print("  band cells at the published grid's OWN cells "
          "(6 windows x 4 maps x its 6 (s, s_0) pairs, %d in all): %d"
          % (len(WINDOWS) * 4 * len(GRID), ongrid))
    print("  band cells found: %s"
          % ", ".join("%s x%d s=%d" % (c[0], c[2], c[3]) for c in cells))
    return cells


def s2_verdict(cells):
    print("== s2  P2: the integer reader's lookahead at the band cells")
    pick = os.environ.get("BAND_CELLS")
    for name, period, m, s in cells:
        tag = "%s x%d s=%d" % (name, m, s)
        if pick and tag not in pick:
            continue
        t0 = time.time()
        win = window_of(period)
        caps = tail_caps(period)
        look, g = min_look(win, 1, m, (0,), s, s, top=3)
        nbad = check_strategy(g, caps, tag) if g is not None else None
        print("  %-16s lookahead %s   states %s   bad %s   (%.0f s)"
              % (tag, "-" if look is None else look,
                 "-" if g is None else len(g.states),
                 "-" if nbad is None else nbad,
                 time.time() - t0))


if __name__ == "__main__":
    t0 = time.time()
    ok = True
    if "s0" in STAGES:
        ok = s0_control()
    if ok and "s1" in STAGES:
        cells = s1_band()
        if "s2" in STAGES:
            s2_verdict(cells)
    print("total %.0f s" % (time.time() - t0))
