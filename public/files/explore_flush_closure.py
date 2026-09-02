"""Is the integer reader's winning set the CLOSURE of safe-and-codable,
and where does that closure fail -- at a flushed state only, or
mid-flush? The commitment the flush law's proof must rule out, read as
a count at every decided cell and every lookahead up to the reader's.

THE QUESTION
------------
c_int = max(c_saf, L*) is an observation at 153 cells with both sides
proved lower bounds and no sufficiency proof (explore_flush_law.py).
What a proof must rule out is a COMMITMENT: mid-flush, one output digit
due and two continuations of the seen window demanding two pending
strings for one residual. This rig does not prove anything; it asks
the game itself WHERE the reader's winning set falls short of the
simplest invariant a proof could carry, at every cell and lookahead.

THE HAND-ATTACK (on paper, before the engine)
---------------------------------------------
Conventions are the engine's (explore_redundant_ostrowski.py, Game): a
state is (pos, branch set, pzd, pze); a branch is the lattice point
sum (e - m d)_k theta_k - M in the frame of the current period, with
theta_k = (-p_k, q_k) in the (u, w) = u + w alpha coordinates; the
reader emits e_t having seen d_0..d_{t+c}.
H1  WHAT A BRANCH SAYS ABOUT THE RESIDUAL. With m_o = 1 and c = 0,
    before the first wrap a branch's w-coordinate is -R, R the integer
    residual m val(d_{<=t+c}) - val(e_{<t}), every branch of one state
    sharing it and differing in the lift M; after a wrap the lifts'
    images under the frame's renormalization spread in BOTH coordinates
    (the printed states show it -- the first draft of this line said
    the branches always share w), and what survives is the per-branch
    reading of H2. The state holds (0, 0) iff R = 0 and the lift the
    run actually took is still alive.
H2  CODABLE, READ OFF THE STATE. R is a capped output string f from
    level t, sum_{j>=t} f_j q_j = R, iff sum (e + f - m d)_k theta_k is
    an integer, i.e. iff some branch EQUALS minus the frame star of f:
    (u, w) = (sum f_j p_j, -sum f_j q_j) over frame positions j >= pos,
    the caps the engine's cap_out(j). So CODABLE(state) is a finite
    recursion on the branches with w <= 0, no true index and no wrap
    count needed, and the (0, 0)-holders are its f = 0 case. Whether
    the lift that coding needs is alive is part of the read, which is
    the right reading: the box is a sound necessary condition, so a
    residual codable in arithmetic whose lift the box has dropped was
    never completable.
H3  THE CLOSURE IS THE WINNING SET -- an argument, so its print is a
    CONTROL. Let SC = SAFE and CODABLE (SAFE the safety fixpoint) and
    I the greatest subset of SC closed under "some output digit keeps
    EVERY reply in I". W (Game.solve) is safe, closed, and codable --
    reaching a (0, 0)-holder under zero input from a state is a coding
    of its residual by the digits of that path -- so W is a subset of
    I. Conversely from a state of I, under zero input, the reader can
    keep every reply and so the zero reply inside I: the residual
    never rises and, being codable from level t, is 0 or at least q_t,
    so it reaches 0 within log steps at a (0, 0)-holder of I. Then I
    meets both of W's conditions and I is a subset of W. So I = W, and
    the flush refinement adds nothing to closure: the full game is the
    safety game with CODABLE as an extra invariant.
H4  WHERE CLOSURE FAILS, AND WHICH KIND OF STATE FAILS. A DIRECT
    failure is a state of SC with no digit keeping every reply in SC;
    everything else I removes is propagation. A direct failure at a
    FLUSHED state (holding (0, 0)) is a late digit the reader cannot
    place -- the flush floor's mechanism, and L*'s one-digit case. A
    direct failure at a MID-FLUSH state (codable, not holding (0, 0))
    is the commitment itself: a pending string half written and a
    continuation the same digit cannot serve. L* is a clairvoyant
    reading and says nothing about one-step choices, so at c >= L* a
    mid-flush direct failure is exactly what a proof of the law must
    show cannot happen; and if SC is closed at c = c_int at every cell
    (no direct failure of either kind) the law's proof is one lemma:
    at c >= max(c_saf, L*) every safe codable state has a digit
    keeping every reply safe and codable.
H5  WHERE MID-FLUSH FAILURES ARE FORCED. At V1 (1,1,1,2) x5, (s, s_0)
    = (1, 0) and (1, 1), the corpus reads c_saf = 3 and L* = 4 with a
    late TAIL rather than a late digit needing the four levels
    (explore_flush_law.py F2): a single late digit is codable at a
    smaller drop and some tail is not. Along such a tail codability is
    lost at the arrival of some digit after the first, at a state that
    is safe (c >= c_saf) and codable -- a mid-flush direct failure at
    c = 3 (and at 2). So the prediction "no mid-flush failure ever" is
    already refuted by the corpus's own reading, and the hypothesis
    with content is the one gated by L*: NONE at c >= L*.
H6  WHERE IT CAN BLOW UP. The codability recursion is on exact integers
    and branches are small (the box); it is memoized per state. The
    band cells' games are the corpus's heaviest at lookahead 2 (345 MB
    for three of them, explore_flush_price.py), so the band is its own
    stage under memwatch. The safety fixpoint is iterated to closure
    and the verdict read at the inits, never as non-emptiness.
TRANSPLANT, marked: the game, its box, the grid, the band cells and the
frozen c_int/c_saf readings are the parents' (explore_redundant_
ostrowski.py, explore_flush_price.py); nothing here re-derives them.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS,
never what they would mean).
  C1 (controls, run FIRST; nothing below is read if any leg is red)
     (a) I = W at every (cell, lookahead) pair built: I minus W and W minus I both empty (H3; a violation is a fault of the codability read
         or of the closure, never a finding).
     (b) every (0, 0)-holder is CODABLE, and no state whose branches
         all have w > 0 is (H2's f = 0 case and its sign).
     (c) c_int reproduces the parents' frozen rows -- silver x2
         "- 2 2 2 0 0", silver x3 "- 3 2 2 2 2", bronze x2
         "- 2 2 2 2 0", bronze x3 "- 2 2 2 2 2" -- through this rig's
         own builds.
  P1 THE CLOSURE AT c = c_int, over the 120 grid cells that read and the
     ten band cells: per cell the direct failures of SC, split FLUSHED /
     MID-FLUSH. Prediction: 0 and 0 at every cell (SC itself closed).
     KILL, as an observable: a nonzero count at any cell, the state
     printed (pos, its w-coordinates, holds (0, 0)).
  P2 THE COMMITMENT BELOW c_int, at c_saf <= c < c_int: per cell the
     mid-flush direct failures. Predicted > 0 at V1 x5 (1, 0) and
     (1, 1) at c = 2 and c = 3 (H5). Not predicted elsewhere; printed,
     and tallied as cells with a nonzero mid-flush count.
  P3 THE INITS: at c = c_int the inits inside SC (forced: all of them,
     a control); at c = c_int - 1 >= c_saf the count of inits inside
     SC, printed and not predicted -- whether the loss is at the start
     or downstream.
  P4 state counts and wall-clock per stage; peak under memwatch in the
     run record.

THE DESIGN
----------
Stages: s1 the grid (120 cells that read; the zero-slack column, which
reads at no lookahead, is skipped), s2 the ten band cells, each cell
ascending c = 0..c_int with the parent's cap. Per (cell, c): Game(win,
1, m, (0,), c, s, s_0); SAFE by the closure loop of
explore_flush_price.safety_wins returning the set; CODABLE by H2's
recursion over frame positions with the engine's q, p extended by its
own recurrence and its cap_out; SC, its direct failures split by
Game.holds0, its closure I, and W = Game.W compared. Everything in one
process per stage, under 512 MB. Added after the run, off the same
builds: s3 prints the P1 kill states with every digit's replies flagged
(safe, codable, winning); s4 and s6 test uniform digit rules on W --
the least and greatest digit keeping every reply in SC, and the digit
whose zero reply flushes soonest through safe states -- counting the
states of W they leave; s5 replays Game.solve counting alternations,
CLOSURE_BAND=1 for the band.

FINDINGS (post-run; the prints are the record)
----------------------------------------------
F1  THE CONTROLS HOLD (C1), after one rig fault fixed between the runs:
    the first run began a coding at the state's frame POSITION where
    the engine's frame is phase-based (theta_{pos mod P}, renormalized
    at every wrap), and W minus I was non-empty at 120 of 120 cells; with
    the phase as the start I = W at all 394 grid (cell, c) pairs and all
    30 band pairs, every (0, 0)-holder is codable, no state whose
    branches all have w > 0 is, and the four parent rows reproduce.
F2  THE CLOSURE AT c_int (P1): SC is closed at 116 of the 120 grid
    cells and 9 of the 10 band cells. At the five others -- sqrt3-1
    x3 and x4 at (2, 2), V1 x4 and x5 at (3, 3), bronze x3 at (5, 5) --
    two (one at bronze) MID-FLUSH direct failures, no flushed one: safe,
    codable states every winning strategy avoids. Their shape (s3): at
    sqrt3-1 x3 (2, 2) a fork -- digit 0 keeps the replies 0 and 1
    winning and dies at the cap digit 2, digit 3 keeps 1 and 2 winning
    and at the reply 0 leaves a residual that is safe and no longer
    codes; at V1 x4 (3, 3) the state has ONE legal reply and still no
    digit serves it, 0 keeping safety and losing codability and 5 the
    reverse. So the winning set's invariant is NOT safe-and-codable.
F3  BELOW c_int (P2, P3): at c_saf <= c < c_int mid-flush direct
    failures at every one of the 30 grid pairs and the 11 band pairs,
    beside flushed ones at every pair. H5's prediction at V1 x5 holds
    at c = 3 (7 states at each slack) and is REFUTED at c = 2 (0 of
    both kinds): at c < c_saf SC is closed at every pair and the loss
    is the inits sitting outside SAFE. At c = c_int - 1 >= c_saf every
    init sits inside SC at all 29 grid and 10 band cells: the loss is
    downstream, never at the start.
F4  THE WINNING SET'S CLOSED FORM (s5). Let R1 be the safe states from
    which a (0, 0)-holder is reachable under zero input by moves whose
    EVERY reply is safe -- Game.solve's first flush refinement. At c =
    c_int, W = R1 at all 130 cells: the safety pass after that
    refinement removes nothing, and R1 sits strictly inside SC at the
    five cells of F2. At every losing c >= c_saf -- the 30 grid and 11
    band pairs -- the same pass ANNIHILATES R1 to the empty set, never
    trims it; below c_saf R1 can stand non-empty and losing (silver x4
    (1, 0) at c = 2: 348 states, the inits unsafe) and is annihilated at
    two pairs. No pair anywhere needs a second alternation.
F5  NO UNIFORM DIGIT RULE SERVES (s4, s6). Over the states of W at
    c_int: the least digit keeping every reply in SC leaves W at 4
    states in 3 cells, the greatest at 6 states in 3, and the digit
    whose zero reply flushes soonest through safe states at 10 states
    in one cell (V1 x4 (3, 3)). The winning choice is global.
F6  Wall and peak per stage under memwatch, one process each: s1 27 s
    at 152 MB; s2 14 s at 348 MB; s3 with s4 44 s at 165 MB; s5 52 s at
    166 MB on the grid and 29 s at 413 MB on the band; s6 42 s at
    166 MB.

TIER. H3 is an argument and F1 its check: I = W is a PROPERTY of the
game (the flush refinement adds nothing to closure). F2-F5 are
exhaustive computations at the cells named. W = R1 at the winning
lookahead is an OBSERVATION at 130 cells with no proof under it (R1 is
a subset of W exactly when R1 is closed), and the annihilation below
c_int an observation at 41 pairs. What this leaves for a proof of
c_int = max(c_saf, L*) is one lemma with its invariant now named: at
c >= max(c_saf, L*) every state of R1 has a digit keeping every reply
in R1 -- safe-and-codable refuted as that invariant at five cells, and
every uniform digit rule tried refuted as the strategy.

RUN RECORD. python memwatch.py explore_flush_closure.py, stages by
CLOSURE_STAGES (s1..s6) and CLOSURE_BAND; peaks in F6; nothing ran bare.
"""

import os
import sys
import time
from functools import lru_cache

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_redundant_ostrowski import (               # noqa: E402
    GRID, WINDOWS, Game, LOOKCAP, h3_bound)
from explore_flush_price import BAND, window_of         # noqa: E402

PARENT = {("silver [2]", 2): "- 2 2 2 0 0", ("silver [2]", 3): "- 3 2 2 2 2",
          ("bronze [3]", 2): "- 2 2 2 2 0", ("bronze [3]", 3): "- 2 2 2 2 2"}
QTOP = 90


def safety_set(g):
    """explore_flush_price.safety_wins, returning the set."""
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
    return W


def closure(g, base):
    """The greatest subset of `base` closed under some digit keeping
    every reply inside; and the DIRECT failures of `base` itself."""
    direct = set(s for s in base
                 if not any(all(s2 in base for _x, s2 in succ)
                            for succ in g.trans[s].values()))
    I = set(base)
    changed = True
    while changed:
        changed = False
        for s in list(I):
            ok = any(all(s2 in I for _x, s2 in succ)
                     for succ in g.trans[s].values())
            if not ok:
                I.discard(s)
                changed = True
    return I, direct


def codable_flags(g):
    """H2: per state, does some branch equal minus the frame star of a
    capped output string from the state's frame position?"""
    P, a = g.P, g.a
    q = {-1: 0, 0: 1}
    p = {-1: 1, 0: 0}
    for k in range(1, QTOP + 1):
        q[k] = a[(k - 1) % P] * q[k - 1] + q[k - 2]
        p[k] = a[(k - 1) % P] * p[k - 1] + p[k - 2]

    @lru_cache(maxsize=None)
    def rec(j, wr, ur, z):
        # j is the index in the CURRENT frame, phase-based: the engine
        # adds y theta_{pos mod P} and renormalizes by H at each wrap,
        # so a coding from a state at pos starts at phase pos mod P and
        # runs up the true recurrence from there; position 0's own cap
        # (s_0) applies at the true position 0 only (z), never at phase
        # 0 after a wrap.
        if wr == 0:
            return ur == 0
        if j > QTOP or q[j] > wr:
            return False
        cap = g.cap_out(0) if (j == 0 and z) else a[j % P] + g.s
        for f in range(min(cap, wr // q[j]) + 1):
            if rec(j + 1, wr - f * q[j], ur - f * p[j], z):
                return True
        return False

    flags = []
    for st in g.states:
        pos, br = st[0], st[1]
        phi, z = pos % P, pos == 0
        flags.append(any(w <= 0 and rec(phi, -w, u, z) for u, w in br))
    return flags


def read_cell(win, m, s, s0, top):
    """Ascend c = 0..top; per c the counts; stop at c_int."""
    rows = []
    c_int = c_saf = None
    for look in range(top + 1):
        t0 = time.time()
        g = Game(win, 1, m, (0,), look, s, s0)
        S = safety_set(g)
        cod = codable_flags(g)
        SC = set(i for i in S if cod[i])
        I, direct = closure(g, SC)
        W = g.W
        d_fl = sum(1 for i in direct if g.holds0[i])
        d_mid = len(direct) - d_fl
        inits = g.init
        row = dict(look=look, states=g.n_states, S=len(S), SC=len(SC),
                   I=len(I), W=len(W), I_W=len(I - W), W_I=len(W - I),
                   d_fl=d_fl, d_mid=d_mid,
                   init_SC=sum(1 for i in inits if i in SC),
                   init_W=sum(1 for i in inits if i in W),
                   n_init=len(inits),
                   hold_cod=all(cod[i] for i in range(g.n_states)
                                if g.holds0[i]),
                   pos_cod=any(cod[i] for i, st in enumerate(g.states)
                               if st[1] and all(w > 0 for _u, w in st[1])),
                   wall=time.time() - t0,
                   sample=[(g.states[i][0], sorted(w for _u, w in g.states[i][1]),
                            g.holds0[i]) for i in sorted(direct)[:2]])
        if c_saf is None and all(i in S for i in inits):
            c_saf = look
        if all(i in W for i in inits):
            c_int = look
        rows.append(row)
        if c_int is not None:
            break
    return c_int, c_saf, rows


def fmt(v):
    return "-" if v is None else str(v)


def report(name, m, s, s0, c_int, c_saf, rows, tallies):
    parts = []
    for r in rows:
        parts.append("c%d:%d/%d" % (r["look"], r["d_fl"], r["d_mid"]))
        bad = r["I_W"] + r["W_I"]
        if bad or not r["hold_cod"] or r["pos_cod"]:
            tallies["ctrl_bad"] += 1
            parts.append("CTRL-BAD(I\\W %d, W\\I %d, hold %s, pos %s)"
                         % (r["I_W"], r["W_I"], r["hold_cod"], r["pos_cod"]))
        look = r["look"]
        if c_int is not None and look == c_int:
            tallies["cells"] += 1
            if r["d_fl"] or r["d_mid"]:
                tallies["p1_kill"].append((name, m, s, s0, look, r["d_fl"],
                                           r["d_mid"], r["sample"]))
            if r["init_SC"] != r["n_init"]:
                tallies["init_bad"] += 1
        if c_saf is not None and c_int is not None and c_saf <= look < c_int:
            if r["d_mid"]:
                tallies["p2_mid"].append((name, m, s, s0, look, r["d_mid"]))
            else:
                tallies["p2_zero"] += 1
            if look == c_int - 1:
                tallies["p3"].append((name, m, s, s0, r["init_SC"],
                                      r["n_init"]))
        if c_saf is not None and look < c_saf and r["d_mid"]:
            tallies["below_saf_mid"] += 1
    print("  %-14s x%d (%d,%d)  c_int %s  c_saf %s  states %d  %s"
          % (name, m, s, s0, fmt(c_int), fmt(c_saf),
             max(r["states"] for r in rows), "  ".join(parts)))


def new_tallies():
    return dict(ctrl_bad=0, cells=0, p1_kill=[], init_bad=0, p2_mid=[],
                p2_zero=0, p3=[], below_saf_mid=0)


def summarize(tallies, label):
    print("== %s summary" % label)
    print("  C1(a,b) control violations: %d" % tallies["ctrl_bad"])
    print("  P1  cells read at c_int: %d; cells with a direct failure of "
          "SC at c_int (KILL): %d" % (tallies["cells"], len(tallies["p1_kill"])))
    for k in tallies["p1_kill"]:
        print("      %s x%d (%d,%d) c=%d  flushed %d  mid-flush %d  sample %s"
              % k)
    print("  P3  inits outside SC at c_int: %d cells" % tallies["init_bad"])
    print("  P2  (cell, c) pairs with c_saf <= c < c_int: mid-flush direct "
          "failures at %d, none at %d"
          % (len(tallies["p2_mid"]), tallies["p2_zero"]))
    for k in tallies["p2_mid"]:
        print("      %s x%d (%d,%d) c=%d  mid-flush %d" % k)
    print("  P3  at c = c_int - 1 >= c_saf, inits inside SC (of inits):")
    for k in tallies["p3"]:
        print("      %s x%d (%d,%d)  %d of %d" % k)
    print("  (cell, c) pairs below c_saf with mid-flush direct failures: %d"
          % tallies["below_saf_mid"])


def s1_grid():
    print("== s1  the grid: per cell, per lookahead c, direct failures "
          "of SC as flushed/mid-flush")
    tallies = new_tallies()
    t0 = time.time()
    ctrl_bad = 0
    for name, period in WINDOWS:
        win = window_of(period)
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
                print("  C1(c) %s x%d  got '%s'  want '%s'  %s"
                      % (name, m, got, want, "ok" if ok else "BAD"))
    print("  C1(c) parent-row mismatches: %d" % ctrl_bad)
    summarize(tallies, "s1")
    print("  s1 wall %.0f s" % (time.time() - t0))


def s2_band():
    print("== s2  the ten band cells")
    tallies = new_tallies()
    t0 = time.time()
    cells = os.environ.get("CLOSURE_CELLS")
    pick = set(int(i) for i in cells.split(",")) if cells else None
    for i, (name, period, m, s, want) in enumerate(BAND):
        if pick is not None and i not in pick:
            continue
        win = window_of(period)
        c_int, c_saf, rows = read_cell(win, m, s, s, LOOKCAP)
        report(name, m, s, s, c_int, c_saf, rows, tallies)
        if c_int != want:
            print("      BAD c_int, the parent froze %d" % want)
    summarize(tallies, "s2")
    print("  s2 wall %.0f s" % (time.time() - t0))


KILL4 = [("sqrt3-1 [1,2]", (1, 2), 3, 2, 2), ("sqrt3-1 [1,2]", (1, 2), 4, 2, 2),
         ("V1 (1,1,1,2)", (1, 1, 1, 2), 4, 3, 3),
         ("V1 (1,1,1,2)", (1, 1, 1, 2), 5, 3, 3)]


def s3_states():
    """Added post-run: the avoidable commitment states at the four cells
    P1 named, with every digit's replies flagged (safe, codable)."""
    print("== s3  the direct failures of SC at c_int, at the four cells")
    for name, period, m, s, s0 in KILL4:
        win = window_of(period)
        c_int, _c_saf, _rows = read_cell(win, m, s, s0, LOOKCAP)
        g = Game(win, 1, m, (0,), c_int, s, s0)
        S = safety_set(g)
        cod = codable_flags(g)
        SC = set(i for i in S if cod[i])
        _I, direct = closure(g, SC)
        print("  %s x%d (%d,%d) c=%d  |SC| %d  |W| %d  direct %d"
              % (name, m, s, s0, c_int, len(SC), len(g.W), len(direct)))
        for i in sorted(direct):
            pos, br, pzd, pze = g.states[i]
            print("    state pos %d pzd %s pze %s  branches %s  holds0 %s"
                  % (pos, pzd, pze, sorted(br), g.holds0[i]))
            for y, succ in sorted(g.trans[i].items()):
                print("      y=%d: %s" % (y, "  ".join(
                    "x=%d(%s%s%s)" % (x, "S" if s2 in S else "-",
                                      "C" if cod[s2] else "-",
                                      "W" if s2 in g.W else "-")
                    for x, s2 in succ)))


def s4_rules():
    """Added post-run: does a UNIFORM digit rule stay inside W? Per cell
    at c = c_int, over every state of W: the least and the greatest
    digit keeping every reply in SC, and whether each keeps every reply
    in W; violations counted."""
    print("== s4  uniform rules on W at c_int: least / greatest digit "
          "keeping every reply in SC -- states of W where it leaves W")
    tot = {"min": 0, "max": 0, "cells_min": 0, "cells_max": 0, "cells": 0}
    for name, period in WINDOWS:
        win = window_of(period)
        for m in (2, 3, 4, 5):
            row = []
            for s, s0 in GRID:
                if (s, s0) == (0, 0):
                    continue
                hb = h3_bound(win, m, s, s0)
                top = LOOKCAP if hb is None else hb
                c_int, _c_saf, _rows = read_cell(win, m, s, s0, top)
                g = Game(win, 1, m, (0,), c_int, s, s0)
                S = safety_set(g)
                cod = codable_flags(g)
                SC = set(i for i in S if cod[i])
                bad = {"min": 0, "max": 0}
                for i in g.W:
                    ys = [y for y, succ in g.trans[i].items()
                          if all(s2 in SC for _x, s2 in succ)]
                    for key, y in (("min", min(ys)), ("max", max(ys))):
                        if not all(s2 in g.W for _x, s2 in g.trans[i][y]):
                            bad[key] += 1
                tot["cells"] += 1
                tot["min"] += bad["min"]
                tot["max"] += bad["max"]
                tot["cells_min"] += bool(bad["min"])
                tot["cells_max"] += bool(bad["max"])
                row.append("(%d,%d)c%d:%d/%d" % (s, s0, c_int, bad["min"],
                                                 bad["max"]))
            print("  %-14s x%d  %s" % (name, m, "  ".join(row)))
    print("  s4 summary over %d cells: least-digit rule leaves W at %d "
          "states in %d cells; greatest-digit rule at %d states in %d cells"
          % (tot["cells"], tot["min"], tot["cells_min"], tot["max"],
             tot["cells_max"]))


def rounds(g):
    """Game.solve replayed, counting alternations: the safety pass, the
    flush refinement, and how many times a refinement removed a state
    before the pair agreed. Returns (rounds, |W after the first
    refinement|, |W|)."""
    from collections import deque
    W = set(i for i in g.trans if g.alive[i])
    n = 0
    first = None
    while True:
        changed = True
        while changed:
            changed = False
            for s in list(W):
                ok = any(all(s2 in W for _x, s2 in succ)
                         for succ in g.trans[s].values())
                if not ok:
                    W.discard(s)
                    changed = True
        Z = set(i for i in W if g.holds0[i])
        dist = {s: 0 for s in Z}
        dq = deque(Z)
        rev = {}
        for s in W:
            for y, succ in g.trans[s].items():
                if all(s2 in W for _x, s2 in succ):
                    for x, s2 in succ:
                        if x == 0:
                            rev.setdefault(s2, []).append(s)
        while dq:
            s = dq.popleft()
            for s0 in rev.get(s, ()):
                if s0 not in dist:
                    dist[s0] = 1
                    dq.append(s0)
        if first is None:
            first = len(dist)
        if len(dist) == len(W):
            break
        n += 1
        W = set(dist)
    return n, first, len(W)


def s5_rounds():
    """Added post-run: how many alternations Game.solve needs at every
    cell and lookahead -- 0 means W is exactly the safe states from
    which (0, 0) is reachable under zero input through safe states."""
    print("== s5  alternation rounds of the safety/flush fixpoint per "
          "(cell, c): rounds beyond the first refinement")
    tally = {}
    worst = []
    if os.environ.get("CLOSURE_BAND"):
        cells = [(name, period, m, s, s, LOOKCAP)
                 for name, period, m, s, _w in BAND]
    else:
        cells = [(name, period, m, s, s0, None) for name, period in WINDOWS
                 for m in (2, 3, 4, 5) for s, s0 in GRID if (s, s0) != (0, 0)]
    last = None
    for name, period, m, s, s0, top in cells:
        win = window_of(period)
        if True:
            row = []
            if True:
                if top is None:
                    hb = h3_bound(win, m, s, s0)
                    top = LOOKCAP if hb is None else hb
                c_int, _c_saf, _rows = read_cell(win, m, s, s0, top)
                cell = []
                for look in range(c_int + 1):
                    g = Game(win, 1, m, (0,), look, s, s0)
                    n, first, final = rounds(g)
                    tally[n] = tally.get(n, 0) + 1
                    cell.append("%d" % n)
                    if n:
                        worst.append((name, m, s, s0, look, n, first, final))
                row.append("(%d,%d):%s" % (s, s0, "".join(cell)))
            print("  %-14s x%d  %s" % (name, m, "  ".join(row)))
    print("  rounds tally over (cell, c) pairs: %s"
          % ", ".join("%d rounds: %d" % (k, tally[k]) for k in sorted(tally)))
    for w in worst:
        print("    %s x%d (%d,%d) c=%d  rounds %d  |W| after first "
              "refinement %d, final %d" % w)


def reach_S(g, S):
    """R1 and its flush distances: BFS from the (0, 0)-holders of S
    backwards along zero replies of moves whose EVERY reply is in S."""
    from collections import deque
    Z = set(i for i in S if g.holds0[i])
    dist = {s: 0 for s in Z}
    dq = deque(Z)
    rev = {}
    for s in S:
        for y, succ in g.trans[s].items():
            if all(s2 in S for _x, s2 in succ):
                for x, s2 in succ:
                    if x == 0:
                        rev.setdefault(s2, []).append(s)
    while dq:
        s = dq.popleft()
        for s0 in rev.get(s, ()):
            if s0 not in dist:
                dist[s0] = dist[s] + 1
                dq.append(s0)
    return dist


def s6_shortest():
    """Added post-run: the rule 'flush by the shortest path through safe
    states' -- at each state of W at c_int, the least digit whose every
    reply is safe and whose zero reply has the least flush distance in
    R1 -- and whether every reply of that digit lands in W. Computed
    from S and R1 alone, never from W."""
    print("== s6  the shortest-flush rule on W at c_int: states of W where "
          "it leaves W")
    tot_bad = cells_bad = cells = 0
    for name, period in WINDOWS:
        win = window_of(period)
        for m in (2, 3, 4, 5):
            row = []
            for s, s0 in GRID:
                if (s, s0) == (0, 0):
                    continue
                hb = h3_bound(win, m, s, s0)
                top = LOOKCAP if hb is None else hb
                c_int, _c_saf, _rows = read_cell(win, m, s, s0, top)
                g = Game(win, 1, m, (0,), c_int, s, s0)
                S = safety_set(g)
                dist = reach_S(g, S)
                R1 = set(dist)
                assert R1 == g.W, "s5's reading: W = R1 at c_int"
                bad = 0
                for i in g.W:
                    best = None
                    for y, succ in sorted(g.trans[i].items()):
                        if not all(s2 in S for _x, s2 in succ):
                            continue
                        z = [s2 for x, s2 in succ if x == 0]
                        if not z or z[0] not in dist:
                            continue
                        d = dist[z[0]]
                        if best is None or d < best[0]:
                            best = (d, y)
                    y = best[1]
                    if not all(s2 in g.W for _x, s2 in g.trans[i][y]):
                        bad += 1
                cells += 1
                tot_bad += bad
                cells_bad += bool(bad)
                row.append("(%d,%d)c%d:%d" % (s, s0, c_int, bad))
            print("  %-14s x%d  %s" % (name, m, "  ".join(row)))
    print("  s6 summary over %d cells: the shortest-flush rule leaves W at "
          "%d states in %d cells" % (cells, tot_bad, cells_bad))


def main():
    stages = os.environ.get("CLOSURE_STAGES", "s1,s2").split(",")
    if "s6" in stages:
        s6_shortest()
    if "s5" in stages:
        s5_rounds()
    if "s1" in stages:
        s1_grid()
    if "s2" in stages:
        s2_band()
    if "s3" in stages:
        s3_states()
    if "s4" in stages:
        s4_rules()


if __name__ == "__main__":
    main()
