"""Does the integer reader's lookahead grow along the run family
[1^T, A]? The residual game of explore_redundant_ostrowski.py pointed at
the periodic windows whose period is a run of T ones closed by one
larger quotient A, read over T and A.

THE QUESTION
------------
With a redundant output alphabet (caps a_{k+1} + s, position 0 at
a_1 - 1 + s_0, the below-a-cap rule dropped) the overlap lemma hands x m
a bottom-up reader at lookahead O(log(2m/(1+s))) at every irrational
window -- on the COMPLETION. The INTEGER reader must also flush, and its
existence at a general irrational window is open
(explore_redundant_ostrowski.py H3'); the six periodic windows read so
far all read it at or under the completion bound. This rig asks the
question along one family designed by hand: a run of T quotients equal
to 1 closed by a quotient A. If the minimal lookahead RISES with T (or
with A) without bound, the loss transfers to an aperiodic window built
from the family's blocks and the integer reader does not exist there;
if it stays FLAT, the reader has a reserve-keeping coding of the run
and the family is not where the obstruction lives.

THE HAND-ATTACK (on paper, before the engine)
---------------------------------------------
Notation as in explore_limit_maps.py D7-D9 and the parent's H1-H5.
R1  THE FRAME. Any residual R at position t is R = x q_t + y q_{t-1}
    with integers (x, y), star x theta_t + y theta_{t-1}; the parent's
    box bounds (x, y) by a constant in (m, s, c, a_max), and position
    t -> t + 1 sends (x, y) -> (y, x - a_{t+1} y). The residual game at
    ANY window is therefore a game on one finite set of frame-states
    with the transition labelled by the local quotient: finite at every
    window with bounded quotients; a period makes it STATIONARY.
R2  THE TRANSFER. A loss at lookahead c is a finite input pair (two
    legal inputs agreeing through t + c whose images admit no common
    output prefix through t), so it depends only on the quotients up to
    the images' length. Under all-zero input the reader must emit zeros
    (0 has one coding), so its state at the first nonzero digit minus
    c - 1 is the zero residual with the zero flags: a loss FROM THE
    ZERO-RESIDUAL STATE AT AN ORDINARY PHASE of a periodic window is a
    loss at every window whose quotients agree with that window's from
    that phase on for long enough -- an aperiodic window concatenating
    blocks of the family with rising T (or A), each block longer than
    its witness, loses at every lookahead.
R3  THE CANDIDATE OBSTRUCTION (x 2, s = s_0 = 1). Quotients 1 below
    t, a_{t+1} = A, input d_t = A (forcing d_{t-1} = 0). 2A q_t is not
    codable from t once A >= 3 (a tail from t + 1 has frame
    Y-coordinate >= 1; a multiple of q_t needs Y = 0), and for A large
    against the low part's ceiling (about 4 q_t at these caps) every
    coding of 2(A q_t + r), r < q_{t-1} the low input, has low part
    2r + j q_t - q_{t-1} with j >= 0: never the digitwise 2r; the
    cheapest repairs are +q_{t-2} (j = 1) and -q_{t-1} (j = 0). Against
    the alternating input 1 0 1 0 ... below t, every even position
    coded digitwise is FULL (e = 2 at cap 2) and +q_{t-2} = q_{t-3} +
    q_{t-4} cascades through every full position to the bottom: a
    digitwise reader needs lookahead about T.
R4  THE CANDIDATE COUNTER-MOVE. The reader need not code the run
    digitwise: 2 q_k = q_{k+1} + q_{k-2} and 2 r_t = q_{t-1} + (r_t - 1)
    are codings of the same values that leave room at the top. Whether
    ONE prefix keeps room at t - 1 and t - 2 for every t at once --
    the reader not knowing where the A comes -- is the alternation the
    game solves, and it is not settled on paper.
TRANSPLANT, marked: the parent's grid read V1 = (1, 1, 1, 2) at
lookahead 2 for x 2 at (1, 1); that is T = 3, A = 2 of this family and
is a control here, not a prediction about T = 6.

THE ENGINE is the parent's Game unchanged. What this rig adds is the
family, the search cap raised past the completion bound (so a cell
whose integer reader needs MORE lookahead than the completion's prints
that number rather than "-"), and the zero-residual reading of R2: at
every ordinary phase of the period, the state (zero residual, zero
pre-read, zero flags) is looked up in the winning set at the cell's
minimal lookahead.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS).
Family: T = 0..T_MAX ones then A, for A in 2, 3, 4; maps x 2 and x 3;
slacks (1, 1) and (2, 2). The lookahead searched runs to LOOKCAP = 5 or
H3's bound, whichever is larger.
  C1 (controls, run FIRST; nothing below is read if any is red)
      (a) the parent's cells recur: T = 0 is silver (A = 2) and bronze
      (A = 3) and T = 1, A = 2 is sqrt3-1, T = 3, A = 2 is V1 -- every
      one must print the parent's F3 lookahead at (1, 1) and (2, 2);
      (b) every winning cell's strategy runs on n < N_CHECK with every
      output value and cap correct and the flush reached.
  P1  THE COLUMN OVER T AT FIXED A, x 2 at (1, 1). Two shapes are
      named and the print decides: RISES (the printed lookahead at
      T_MAX exceeds the one at T = 1 by 2 or more, or prints "-" at
      the search cap) or FLAT (within 1 of T = 1 at every T).
      KILL for the obstruction reading: FLAT at every A.
      KILL for the reserve-keeping reading: RISES at any A.
  P2  THE COMPLETION BOUND. Whether any cell prints a lookahead ABOVE
      H3's bound (the first cell anywhere at which the flush costs
      lookahead) -- printed as the cell's bound beside it.
  P3  THE ORDINARY PHASES (R2). At every winning cell, the zero-
      residual state at every ordinary phase is in the winning set at
      the minimal lookahead: printed as a count of winning phases over
      the period. KILL for the transfer as stated: a phase not winning
      at a cell whose initial states win.
  P4  x 3 and (2, 2) columns: read unasked, as the same two shapes.

THE DESIGN
----------
Stages: s0 the controls (C1a on the recurring cells); s1 the family
grid with the strategy check (C1b) and the phase count (P3) at every
winning cell, each row followed by H3's and the digitwise bound.
T_MAX and the A list are read from the environment (RUNS_TMAX, RUNS_A)
so the rehearsal at T_MAX = 2 exercises every stage before the full
run. Memory: the state space grows with the period; run under
memwatch.py.

FINDINGS (entered post-run; every number below sits in this file's
printed output. Runs: T <= 6 at A = 2, 3, 4 in 23 s, peak 51 MB; T <= 4
at A = 6 in 11 s, peak 184 MB; A = 10 KILLED by memwatch at 515 MB
commit at its first cell -- the parent's box grows with a_max, so the
family's ceiling here is A = 6, not a finding).

F1  THE CONTROLS HOLD. C1a: all 16 recurring cells print the parent's
    lookahead. C1b: every cell in every run won, and every winning
    strategy run on n < 1500 printed the right value under the caps
    and flushed, 0 bad.
F2  FLAT (P1's second shape, at every A; the obstruction reading of R3
    is KILLED). x 2 at (1, 1) prints lookahead 2 at EVERY T = 0..6 for
    A = 2, 3, 4 and at every T = 0..4 for A = 6: the run of ones below
    the large quotient costs the reader nothing, at any length read,
    whether or not A is large against the low part's ceiling. R4's
    counter-move is what the game plays: the digitwise cascade of R3 is
    real, and the winning reader is not digitwise.
F3  THE SAME AT EVERY CELL (P4). x 3 at (1, 1), x 2 at (2, 2) and x 3
    at (2, 2) print 2 at every (T, A) read, except x 2 at (2, 2) for
    A = 2, which prints 0 at every T -- the digitwise cell (s = 2 >=
    (m - 1) a_max). Fifteen of the sixteen (A, map, slack) rows are the
    constant 2 across T.
F4  THE COMPLETION BOUND IS NEVER EXCEEDED (P2). H3's bound prints 2
    or 3 at T = 0 and 3 or 4 beyond (4 for x 3 at (1, 1) from T = 2 on);
    every integer lookahead sits at or under it, 1 or 2 under at most
    cells. The flush still costs nothing in lookahead.
F5  EVERY ORDINARY PHASE WINS (P3): the zero-residual state at every
    one of the P - 1 ordinary labels sits in the winning set at the
    minimal lookahead, at every cell (k/k printed at every one): a
    reader that starts from zero residual at any phase of these windows
    reads at 2 (at these windows -- a win depends on the whole future
    and does not transfer; only R2's loss does).
What the family says: the integer reader's existence at a general
window is not decided by a run of small quotients before a large one,
and the lookahead-2 reading of x 2 and x 3 at slack 1 now stands at
every periodic window read (twelve, the parent's six included, golden's
digitwise 0 aside). The route to the general window is the frame game
of R1 with the opponent choosing the quotients -- the universal game --
whose box must be derived in frame coordinates, the parent's using the
quadratic conjugate.
"""

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_limit_maps import tail_caps                       # noqa: E402
from explore_limit_column import Window                         # noqa: E402
from explore_redundant_ostrowski import (                       # noqa: E402
    Game, h3_bound, digitwise_bound, qs_for, N_CHECK)

LOOKCAP = 5
T_MAX = int(os.environ.get("RUNS_TMAX", "6"))
A_LIST = [int(x) for x in os.environ.get("RUNS_A", "2,3,4").split(",")]
CELLS = [(1, 1), (2, 2)]
MAPS = [("x2", 2), ("x3", 3)]
# the parent's F3 readings at the cells that recur here: (T, A, map) ->
# {(s, s0): lookahead}
PARENT = {
    (0, 2, "x2"): {(1, 1): 2, (2, 2): 0}, (0, 2, "x3"): {(1, 1): 2, (2, 2): 2},
    (0, 3, "x2"): {(1, 1): 2, (2, 2): 2}, (0, 3, "x3"): {(1, 1): 2, (2, 2): 2},
    (1, 2, "x2"): {(1, 1): 2, (2, 2): 0}, (1, 2, "x3"): {(1, 1): 2, (2, 2): 2},
    (3, 2, "x2"): {(1, 1): 2, (2, 2): 0}, (3, 2, "x3"): {(1, 1): 2, (2, 2): 2},
}


def family(T, A):
    return tuple([1] * T + [A])


def check_strategy(g, caps, label):
    """C1b, the parent's check with enough convergents for a period-7
    window (the run emits up to 24 + 4P + 6 digits)."""
    qs = qs_for(caps, 24 + 4 * g.P + 12)
    bad = 0
    for n in range(N_CHECK):
        out, flushed = g.run(n, qs)
        val = sum(y * qs[k] for k, y in enumerate(out))
        okval = (g.mo * val == g.mi * n)
        okcap = all(y <= g.cap_out(k) for k, y in enumerate(out))
        if not (okval and okcap and flushed):
            bad += 1
            if bad <= 3:
                print("    BAD %s n=%d val=%d out=%s flushed=%s"
                      % (label, n, val, out[:12], flushed))
    return bad


def min_look(win, m, s, s0, top):
    for look in range(top + 1):
        g = Game(win, 1, m, (0,), look, s, s0)
        if g.wins:
            return look, g
    return None, None


def zero_state(g, pos):
    """The zero-residual state at label pos (R2): after enough zero
    periods every wrong-M branch has left the box (the wrap scales a
    constant's real coordinate by 1/eta), leaving the branch (0, 0)
    alone, with the zero flags."""
    return (pos, frozenset([(0, 0)]), True, True)


def phase_count(g):
    """How many ordinary labels' zero states sit in the winning set."""
    wins, seen = 0, 0
    for pos in range(2, g.lmax + 1):          # labels 0 and 1 are special
        st = zero_state(g, pos)
        i = g.ids.get(st)
        if i is None:
            continue
        seen += 1
        if i in g.W:
            wins += 1
    return wins, seen


def run_cell(win, caps, name, m, s, s0):
    hb = h3_bound(win, m, s, s0)
    top = max(LOOKCAP, hb if hb is not None else 0)
    look, g = min_look(win, m, s, s0, top)
    bad = 0
    phases = "-"
    if g is not None:
        bad = check_strategy(g, caps, "%s x%d (%d,%d)" % (name, m, s, s0))
        w, n = phase_count(g)
        phases = "%d/%d" % (w, n)
    return look, hb, digitwise_bound(win, m, s, s0), phases, bad


def s0_controls():
    print("== s0  C1a: the parent's cells recur")
    bad = 0
    for (T, A, label), want in PARENT.items():
        if T > T_MAX or A not in A_LIST:
            continue
        m = int(label[1:])
        caps = tail_caps(family(T, A))
        win = Window(caps, len(family(T, A)))
        for (s, s0), lk in want.items():
            look, hb, db, phases, nb = run_cell(win, caps, "T%dA%d" % (T, A),
                                                m, s, s0)
            ok = (look == lk and nb == 0)
            bad += 0 if ok else 1
            print("  T=%d A=%d %s (%d,%d): %s  parent %d  %s"
                  % (T, A, label, s, s0, look, lk, "ok" if ok else "RED"))
    print("  C1a %s" % ("GREEN" if bad == 0 else "RED (%d)" % bad))
    return bad == 0


def s1_family():
    print("== s1  the family [1^T, A]: minimal lookahead / H3 bound /"
          " digitwise bound / winning ordinary phases")
    for A in A_LIST:
        for label, m in MAPS:
            for s, s0 in CELLS:
                print("  A = %d  %s  (s, s0) = (%d, %d)" % (A, label, s, s0))
                row = []
                nbad = 0
                t0 = time.time()
                for T in range(T_MAX + 1):
                    per = family(T, A)
                    caps = tail_caps(per)
                    win = Window(caps, len(per))
                    look, hb, db, phases, nb = run_cell(
                        win, caps, "T%dA%d" % (T, A), m, s, s0)
                    nbad += nb
                    row.append("T%d:%s/%s/%s/%s" % (
                        T, "-" if look is None else look,
                        "-" if hb is None else hb,
                        "-" if db is None else db, phases))
                print("    " + "  ".join(row))
                print("    strategy checks bad: %d   (%.0f s)"
                      % (nbad, time.time() - t0))


if __name__ == "__main__":
    t0 = time.time()
    print("T_MAX = %d  A = %s  LOOKCAP = %d" % (T_MAX, A_LIST, LOOKCAP))
    if s0_controls():
        s1_family()
    else:
        print("controls red: nothing below is read")
    print("total %.0f s" % (time.time() - t0))
