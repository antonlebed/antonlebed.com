"""What the losing pairs whose UNFLUSHED side fails on its own have
that the others do not -- the depth of the flush law's invariant R1
against the class of its collapse, and the cell labels tested against
the same split.

THE QUESTION
------------
c_int = max(c_saf, L*) is an observation with both sides proved lower
bounds and no sufficiency proof (explore_flush_law.py). The lemma a
proof owes keeps its invariant R1 -- the safe states from which a
(0, 0)-holder is reachable under zero input by moves whose EVERY reply
is safe -- and its failing side now has a shape
(explore_flush_seed.py F3): below c_int the collapse of R1 runs ONE
WAY, in that forgiving the FLUSHED states (those holding the zero
residual: exempt them from having to serve, leaving them legal
targets) leaves unflushed states alive at 21 of the 41 losing pairs
while forgiving the unflushed ones leaves no flushed state alive
anywhere; and yet at 13 pairs the unflushed side fails with the
flushed states forgiven, so the obstruction is not confined to the
flushed state and the lemma does not reduce to it. Those 13 against
those 21 are the one structural split the parent printed and did not
read. This rig reads it: it prints, per losing pair, the class beside
the DEPTH of R1 under the flush map and beside every cell label the
pair carries, and it says which of them the split follows.

Conventions are the engine's (explore_redundant_ostrowski.py, Game): a
state is (pos, branch set, pzd, pze); a branch is the lattice point
sum (e - m d)_k theta_k - M in the frame of the current period; the
reader emits e_t having seen d_0..d_{t+c}. SAFE is the safety fixpoint
(explore_flush_price.safety_wins); a DIRECT failure of a set B is a
state of B with no digit keeping every reply in B. The DEPTH of a
state of R1 is its distance in the flush map -- 0 at a flushed state,
k when k zero-input moves through safe-replied moves reach one -- and
the depth of R1 is the largest depth it holds.

THE HAND-ATTACK (on paper, before the engine)
---------------------------------------------
H1  TWO OF THE FOUR CANDIDATES DIE ON PAPER, ARITHMETIC ALONE.
    (a) c = c_saf. A losing pair is c_saf <= c < c_int; a cell with
    any losing pair therefore has c_int > c_saf, so c_int = L* there
    and every losing pair of the corpus satisfies c_saf <= c < L*.
    The number of losing pairs a cell contributes is exactly its flush
    price c_int - c_saf, and the corpus reads that price as 1 at 28 of
    the 30 grid pairs' cells and 2 at one (OSTROWSKI section III), so
    c = c_saf holds at every pair of a price-1 cell and fails at ONE
    pair per price-2 cell -- at most two of the 41. A predicate true
    at 39 pairs cannot cut 13 from 21. Same for c = c_int - 1, its
    mirror.
    (b) the tail. L* is set by a late TAIL rather than a late digit at
    six cells (OSTROWSKI section III: L* = 4 against 2 for one digit),
    and six labels cannot separate thirteen. Both are printed anyway
    -- the elimination is of the candidate, not of the column.
H2  WHAT SURVIVAL ACTUALLY NEEDS, and why depth is the candidate that
    replaces them. With the flushed states forgiven, an unflushed
    state u survives iff SOME output digit of u has EVERY reply
    landing in a flushed state or in a surviving unflushed one. At
    depth 1 the digit realizing u's distance sends the ZERO reply to a
    flushed state, which is free; its NONZERO replies are not, and
    they land at states no closer to a flush than u. So a depth-1
    state survives only on the back of another survivor, and where R1
    is entirely depth <= 1 the whole unflushed side stands or falls
    together on states that have nothing beneath them. Depth >= 2
    gives the closure an interior to hold. PREDICTED: the split is the
    depth.
H3  WHAT DEPTH IS NOT. Depth is not size: a wide shallow R1 has many
    unflushed states at depth 1, and the parent's largest excess (342
    unflushed survivors at V2 (2,1,3,1) x3 (3, 3)) is a count and says
    nothing about how far from a flush they sit. Size is the rival
    reading and is printed against the same split (K3): if the classes
    separate by a THRESHOLD on the unflushed count, the split is a
    size effect and the depth reading is a correlate of it.
H4  THE MEASUREMENT IS THE PARENT'S, NOT A NEW ONE. The dist map that
    grades the depth is what flush_refine already computes and the
    parent discards -- it is Game.solve's own first refinement run
    over the safety fixpoint -- so no new object enters and no reading
    of the parent moves.
H5  A CLASS EXISTS WHERE THE QUESTION DOES NOT ARISE: 7 of the 41
    pairs hold no unflushed state at all (R1 ENTIRELY flushed), where
    forgiving the flushed states can rescue nothing by construction.
    Those are excluded from every contingency and counted separately;
    the split is 13 against 21 over the remaining 34.
TRANSPLANT, marked: the game, its box, the grid, the band cells, the
frozen c_int / c_saf readings, the safety fixpoint, the flush
refinement and both closures are the parents'
(explore_redundant_ostrowski.py, explore_flush_price.py,
explore_flush_closure.py, explore_flush_seed.py); nothing here
re-derives them.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS,
never what they would mean).
  K0 (controls, run FIRST; nothing below is read if any leg is red)
     (a) the parent's classes reproduce through this rig's own build:
         30 losing pairs on the grid, 4 with R1 entirely flushed, 19
         with an excess when the flushed states are forgiven, 7
         neither; and 11 in the band, 3 / 2 / 6
         (explore_flush_seed.py F3).
     (b) c_int reproduces the parents' frozen rows -- silver x2
         "- 2 2 2 0 0", silver x3 "- 3 2 2 2 2", bronze x2
         "- 2 2 2 2 0", bronze x3 "- 2 2 2 2 2".
     (c) every flushed state of R1 has depth 0 and every unflushed one
         depth >= 1, at every pair (a tautology of the construction; a
         violation is a fault of this rig's bookkeeping).
  K1 THE DEPTH SPLIT (H2), over the 34 pairs holding an unflushed
     state: the depth of R1 per pair, against the class. PREDICTED:
     depth 1 at every one of the 13 pairs where forgiving the flushed
     states rescues nothing, depth >= 2 at every one of the 21 where
     it rescues something. KILL, as an observable: a pair of the 13
     printing depth >= 2, or a pair of the 21 printing depth 1.
  K2 THE LABEL PANEL, over the same 34: the class counted against each
     of the window, its period length, its largest partial quotient,
     m, s, s_0, c, c_saf, the flush price, and whether the pair is the
     price-1 cell's only one. PREDICTED (H1): no label is class-pure
     -- each has some value carrying both classes. KILL, as an
     observable: a label every value of which carries one class only,
     which would BE the split and would demote the depth to a
     correlate of it.
  K3 THE SIZE RIVAL (H3), over the same 34: the unflushed count of R1
     per pair, and the verdict of whether a threshold separates -- the
     minimum over one class against the maximum over the other, both
     ways. PREDICTED: an inversion exists (no threshold separates).
     KILL, as an observable: min over one class strictly above max
     over the other.
  K4 THE SURVIVORS' DEPTHS, at the 21 pairs where they exist: how many
     survivors sit at depth 1 and how many unflushed states at depth
     >= 2 fail to survive. PREDICTED (H2): no survivor at depth 1.
     Printed either way; the second count carries no prediction and
     says how much of the interior the closure still eats.
  K5 the depth of R1 at c = c_int, per cell, beside the losing pairs'
     -- printed, no prediction: it says whether the depth the split
     turns on is a property of the CELL or of the LOOKAHEAD.
  K6 state counts, wall-clock and peak per stage.

THE DESIGN
----------
Stages: s1 the grid (the 120 cells that read; the zero-slack column,
which reads at no lookahead, is skipped), s2 the ten band cells. Per
cell c ascends 0..c_int with the parent's cap (h3_bound, else
LOOKCAP); per (cell, c): Game(win, 1, m, (0,), c, s, s_0); SAFE by the
parent's safety loop; R1 and its depth map by the parent's flush
refinement of SAFE; the direct failures by the parent's closure; the
survivors as the EXCESS of the flushed-exempt closure over the flushed
states, which is the parent's F3 observable and the class it defines.
c_saf is the least c whose SAFE holds every init, c_int the least
whose W does. Each losing pair prints its class, the depth of R1, the
depth histogram of its unflushed states and of its survivors, and its
labels; the summaries cross the class against the depth (K1), against
each label (K2) and against the unflushed count (K3). Stage selection
by DEPTH_STAGES, the band cells by DEPTH_CELLS, one process per stage
under memwatch.

FINDINGS (post-run; the prints are the record. Grid 24 s at 146 MB,
band 14 s at 347 MB, one process each under memwatch.)
----------------------------------------------
F1  THE CONTROLS HOLD (K0). The parent's classes reproduce through
    this rig's own build at both stages -- 30 losing pairs on the grid
    as 4 entirely flushed / 19 with an excess / 7 neither, and 11 in
    the band as 3 / 2 / 6 -- the four frozen parent c_int rows
    reproduce, and no state of R1 is graded against its own flush map.
F2  THE SPLIT IS THE DEPTH OF R1, AT 32 OF THE 34 PAIRS (K1;
    observation). Depth 1 -- every unflushed state one zero-input move
    from a flushed one -- at 11 pairs (5 grid, 6 band), and forgiving
    the flushed states rescues nothing at every one of them. Depth
    >= 2 at the other 23, and it rescues something at 21 of them
    (depth 2 at 4 pairs, depth 3 at 17). So the class the parent
    printed is read by one number of the invariant itself, and by no
    label of the cell: over the 34 pairs no window, period, largest
    partial quotient, m, s, s_0, c, c_saf, price or price-1 flag is
    class-pure. The panel prints per STAGE and the reading is over the
    union, which the two panels decide between them: a label carrying
    both classes at one value on the GRID carries both at that value
    in the union too, and the grid panel marks none of the ten pure.
    The band's own 8 pairs make five of them look pure, which is what
    reading one stage's panel alone would cost.
F3  THE TWO EXCEPTIONS ARE THE CORPUS'S OWN TAIL CELLS, and they are
    the whole phenomenon. At V1 (1,1,1,2) x5, (s, s_0) = (1, 0) and
    (1, 1), c = 3, R1 holds 925 and 977 states of which 910 and 962 are
    unflushed, reaching depth 6 -- and not one of them survives with
    the flushed states forgiven. Those
    two cells are exactly where L* is set by a late TAIL rather than a
    late digit (L* = 4 against 2 for one digit, OSTROWSKI section
    III). So the 13 pairs are not one class: at 11 of them R1 is a
    SHELL -- 6 to 17 states, at most 10 of them unflushed, all at
    depth 1 -- where there was nothing to rescue; the phenomenon the
    question was after, a wide deep R1 whose unflushed side is
    annihilated on its own, happens at exactly two pairs, and at both
    of them L* is not a one-digit object either.
F4  DEPTH <= 1 NEVER COEXISTS WITH A WIN (K5; observation, 130 cells).
    At c = c_int the depth of R1 is at least 2 everywhere -- 2 at 15
    grid cells, 4 at 48, 5 at 28, 6 at 14, 7 at 5, 8 at 6, 9 at 3, 10
    at one, and 4 at all ten band cells. The depth-1 losing pairs are
    therefore R1 already shelled to its flushed core and one rim, not
    a shallow invariant that could have won.
F5  SIZE IS NOT THE SPLIT, AND THE SURVIVORS ARE NOT THE DEEP STATES
    (K3, K4). Over the 34 pairs the unflushed count runs 1 to 962 in
    the class that keeps nothing and 8 to 521 in the class that keeps
    something -- overlapping, so no threshold separates, and the
    band's own clean separation (2 to 10 against 123 to 521) is
    inverted by the grid. H2's state-level reading is REFUTED: 572
    survivors sit at depth 1 (467 grid, 105 band), while 2,822 states
    at depth >= 2 do not survive (2,711 and 111). Depth is a property
    of the SET -- whether the closure has an interior to hold -- and
    never a mark carried by the state that survives.

  TIER. F2, F4 and F5 are OBSERVATIONS, exhaustive at the 130 cells
  and the 41 losing pairs the corpus decides; F3 names two of them.
  What this leaves for a proof of c_int = max(c_saf, L*): the owed
  lemma keeps its invariant R1, and the failing side is nowhere the
  flushed state's ALONE -- the parent's K2b already found an unflushed
  direct failure at every pair holding an unflushed state, and this
  rig adds that forgiving the flushed ones rescues nothing at 13 of
  them. What the depth reading does divide is HOW MUCH unflushed
  structure dies unaided: at 11 of those 13 it is a rim of at most ten
  states, all at depth 1, on a set shelled to between 6 and 17; at the
  other two it is 910 and 962 states reaching depth 6. So the argument
  a proof owes over a DEEP unflushed interior is owed at exactly two
  pairs, both at the window V1 (1,1,1,2) at x5, where a late tail sets
  L*; everywhere else what it owes over the unflushed side is either
  nothing (21 pairs, where forgiving the flushed states leaves that
  side standing) or a rim.

RUN RECORD. DEPTH_STAGES=s1 and DEPTH_STAGES=s2, each
python memwatch.py explore_flush_depth.py; peaks and walls in the
findings header; nothing ran bare.
"""

import os
import sys
import time
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_redundant_ostrowski import (               # noqa: E402
    GRID, WINDOWS, Game, LOOKCAP, h3_bound)
from explore_flush_price import BAND, window_of         # noqa: E402
from explore_flush_closure import safety_set, closure   # noqa: E402
from explore_flush_seed import (                        # noqa: E402
    PARENT, flush_refine, closure_exempt)

PARENT_CLASS = {"s1": (30, 4, 19, 7), "s2": (11, 3, 2, 6)}
LABELS = ("win", "P", "amax", "m", "s", "s0", "c", "c_saf", "price",
          "only")


def read_cell(win, m, s, s0, top):
    """Ascend c = 0..c_int; per c the R1 depth map, its classes and
    the survivors of the flushed-exempt closure."""
    rows = []
    c_int = c_saf = None
    for look in range(top + 1):
        t0 = time.time()
        g = Game(win, 1, m, (0,), look, s, s0)
        S = safety_set(g)
        R1, dist = flush_refine(g, S)
        _I, direct = closure(g, R1)
        holds = set(i for i in R1 if g.holds0[i])
        unf = R1 - holds
        surv = closure_exempt(g, R1, holds) - holds
        bad = sum(1 for i in R1 if (dist[i] == 0) != (i in holds))
        rows.append(dict(
            look=look, states=g.n_states, R1=len(R1), n_holds=len(holds),
            n_unf=len(unf), depth=max(dist.values()) if R1 else 0,
            hist=Counter(dist[i] for i in unf),
            surv=len(surv), surv_hist=Counter(dist[i] for i in surv),
            surv_d1=sum(1 for i in surv if dist[i] == 1),
            deep_lost=sum(1 for i in unf if dist[i] >= 2 and i not in surv),
            d_fl=sum(1 for i in direct if g.holds0[i]),
            d_mid=sum(1 for i in direct if not g.holds0[i]),
            grade_bad=bad, wall=time.time() - t0))
        if c_saf is None and all(i in S for i in g.init):
            c_saf = look
        if all(i in g.W for i in g.init):
            c_int = look
            break
    return c_int, c_saf, rows


def fmt(v):
    return "-" if v is None else str(v)


def hist_str(h):
    return ",".join("%d:%d" % (d, h[d]) for d in sorted(h)) or "-"


def new_tallies():
    return dict(pairs=0, cells=0, allflush=0, exc=0, none=0, grade_bad=0,
                rows=[], k1_bad=[], surv_d1=0, deep_lost=0, ctrl_rows=0)


def classify(r):
    if r["n_unf"] == 0:
        return "ALLFLUSH"
    return "EXC" if r["surv"] else "NONE"


def report(name, m, s, s0, c_int, c_saf, rows, tallies):
    price = None if (c_int is None or c_saf is None) else c_int - c_saf
    parts = []
    for r in rows:
        look = r["look"]
        tallies["grade_bad"] += r["grade_bad"]
        losing = (c_saf is not None and c_int is not None
                  and c_saf <= look < c_int)
        if c_int is not None and look == c_int:
            tallies["cells"] += 1
            parts.append("c%d:WIN depth %d" % (look, r["depth"]))
            continue
        if not losing:
            continue
        cls = classify(r)
        tallies["pairs"] += 1
        tallies[{"ALLFLUSH": "allflush", "EXC": "exc",
                 "NONE": "none"}[cls]] += 1
        parts.append("c%d:%s depth %d|R1 %d,%df|unf %s|surv %d %s"
                     % (look, cls, r["depth"], r["R1"], r["n_holds"],
                        hist_str(r["hist"]), r["surv"],
                        hist_str(r["surv_hist"])))
        if cls == "ALLFLUSH":
            continue
        tallies["surv_d1"] += r["surv_d1"]
        tallies["deep_lost"] += r["deep_lost"]
        if (cls == "NONE") != (r["depth"] == 1):
            tallies["k1_bad"].append((name, m, s, s0, look, cls, r["depth"]))
        tallies["rows"].append(dict(
            cell="%s x%d (%d,%d) c=%d" % (name, m, s, s0, look), cls=cls,
            depth=r["depth"], n_unf=r["n_unf"],
            labels=dict(win=name, P=len(win_a(name)), amax=max(win_a(name)),
                        m=m, s=s, s0=s0, c=look, c_saf=c_saf, price=price,
                        only=(price == 1))))
    print("  %-14s x%d (%d,%d)  c_int %s  c_saf %s  states %d  %s"
          % (name, m, s, s0, fmt(c_int), fmt(c_saf),
             max(r["states"] for r in rows), "  ".join(parts)))


_WIN_A = {}


def win_a(name):
    return _WIN_A[name]


def summarize(tallies, label):
    want = PARENT_CLASS[label]
    got = (tallies["pairs"], tallies["allflush"], tallies["exc"],
           tallies["none"])
    print("== %s summary" % label)
    print("  K0(a) losing pairs / entirely flushed / excess / neither: "
          "%d %d %d %d  want %d %d %d %d  %s"
          % (got + want + ("ok" if got == want else "BAD",)))
    print("  K0(c) depth-grade violations: %d" % tallies["grade_bad"])
    rows = tallies["rows"]
    print("  K1  the 34-pair split by DEPTH of R1 (class: depth counts)")
    for cls in ("NONE", "EXC"):
        h = Counter(r["depth"] for r in rows if r["cls"] == cls)
        print("      %-4s n=%d  %s" % (cls, sum(h.values()), hist_str(h)))
    print("      pairs against the prediction (NONE iff depth 1): %d"
          % len(tallies["k1_bad"]))
    for k in tallies["k1_bad"]:
        print("        %s x%d (%d,%d) c=%d  %s depth %d" % k)
    print("  K2  the label panel (value: NONE/EXC), class-pure marked PURE")
    for key in LABELS:
        cells = {}
        for r in rows:
            v = r["labels"][key]
            cells.setdefault(v, Counter())[r["cls"]] += 1
        pure = all(len(c) == 1 for c in cells.values()) and cells
        body = "  ".join("%s:%d/%d" % (v, cells[v]["NONE"], cells[v]["EXC"])
                         for v in sorted(cells, key=str))
        print("      %-6s %s%s" % (key, body, "   PURE" if pure else ""))
    print("  K3  the size rival: unflushed count per class")
    lo = {cls: [r["n_unf"] for r in rows if r["cls"] == cls]
          for cls in ("NONE", "EXC")}
    for cls in ("NONE", "EXC"):
        v = lo[cls]
        print("      %-4s n=%d  min %s  max %s"
              % (cls, len(v), min(v) if v else "-", max(v) if v else "-"))
    if lo["NONE"] and lo["EXC"]:
        sep = (min(lo["NONE"]) > max(lo["EXC"])
               or min(lo["EXC"]) > max(lo["NONE"]))
        print("      a threshold separates: %s" % ("YES" if sep else "no"))
    print("  K4  survivors at depth 1: %d;  unflushed states at depth >= 2 "
          "that do not survive: %d" % (tallies["surv_d1"],
                                       tallies["deep_lost"]))


def s1_grid():
    print("== s1  the grid: per losing pair the class (ALLFLUSH / EXC / "
          "NONE), the DEPTH of R1, its size and flushed share, the depth "
          "histogram of its unflushed states and of the survivors; the "
          "winning lookahead prints its depth alone (K5)")
    tallies = new_tallies()
    t0 = time.time()
    ctrl_bad = 0
    for name, period in WINDOWS:
        win = window_of(period)
        _WIN_A[name] = win.a
        for m in (2, 3, 4, 5):
            cints = []
            for s, s0 in GRID:
                if (s, s0) == (0, 0):
                    cints.append(None)
                    continue
                hb = h3_bound(win, m, s, s0)
                top = LOOKCAP if hb is None else hb
                c_int, c_saf, rows = read_cell(win, m, s, s0, top)
                cints.append(c_int)
                report(name, m, s, s0, c_int, c_saf, rows, tallies)
            want = PARENT.get((name, m))
            if want is not None:
                got = " ".join(fmt(c) for c in cints)
                ok = got == want
                ctrl_bad += 0 if ok else 1
                print("  K0(b) %s x%d  got '%s'  want '%s'  %s"
                      % (name, m, got, want, "ok" if ok else "BAD"))
    print("  K0(b) parent-row mismatches: %d" % ctrl_bad)
    summarize(tallies, "s1")
    print("  s1 wall %.0f s" % (time.time() - t0))


def s2_band():
    print("== s2  the ten band cells (columns as s1)")
    tallies = new_tallies()
    t0 = time.time()
    cells = os.environ.get("DEPTH_CELLS")
    pick = set(int(i) for i in cells.split(",")) if cells else None
    for i, (name, period, m, s, want) in enumerate(BAND):
        if pick is not None and i not in pick:
            continue
        win = window_of(period)
        _WIN_A[name] = win.a
        c_int, c_saf, rows = read_cell(win, m, s, s, LOOKCAP)
        report(name, m, s, s, c_int, c_saf, rows, tallies)
        if c_int != want:
            print("      BAD c_int, the parent froze %d" % want)
    summarize(tallies, "s2")
    print("  s2 wall %.0f s" % (time.time() - t0))


STAGES = {"s1": s1_grid, "s2": s2_band}


def main():
    want = os.environ.get("DEPTH_STAGES", "s1,s2").split(",")
    for name in want:
        STAGES[name.strip()]()


if __name__ == "__main__":
    main()
