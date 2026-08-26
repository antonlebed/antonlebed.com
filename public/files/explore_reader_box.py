"""Is the universal game's NECESSARY BOX loose, and does tightening it
decide x 3 at lookahead 2? The box re-derived from the two exact
recursions, then checked against the trajectories that actually flush.

THE QUESTION
------------
The universal game (explore_universal_reader.py) solves the residual
game of x m over an alphabet {1, ..., A} inside a BOX on the frame pair
(x, y): a branch leaving the box is pruned, a state with no branch left
is LOST. Pruning is sound one way -- a WIN transfers to every window
over the alphabet, a LOSS reads nothing unless the box contains every
pair a flushing play can occupy. That containing box is the NECESSARY
BOX, and U2 derived it as

    |y| <= (1 + s) + 2mA + m(A + 1)^c,
    |x| <= (1 + s) + 2mA + m(A + 1)^(c+1),

which is (95, 41) for x 3 over {1, 2} at c = 2 -- wider than any box
that fits under 512 MB in that encoding, which is why x 3's loss at
lookahead 2 was left UNDECIDED (F4) while its win at 3 stands.

This rig asks whether that box is loose. If the necessary box is in
fact smaller than the BOX-6 run's (72, 27), then that run's loss at
c = 2 is a real loss of the universal game and x 3 at s = s_0 = 1 over
quotients <= 2 reads at EXACTLY 3 -- the quotient switch costing x 3
one unit of lookahead, with no run above 512 MB anywhere.

THE HAND-ATTACK (on paper, before the engine)
---------------------------------------------
Notation as in explore_universal_reader.py U1. At position t a branch
is the pair (x, y) with residual R_t = x q_t + y q_{t-1} and star
sigma_t = x theta_t + y theta_{t-1}; the transition on emitting e, the
opponent revealing d_{t+1}, is (X, Y) = (y + m d_{t+1}, x - e -
a_{t+1} y).

B1  THE TWO EXACT RECURSIONS. theta_{k+1} = a_{k+1} theta_k +
    theta_{k-1} (the same recursion as q). Substituting it into (X, Y):
        R_{t+1}     = R_t     + m d_{t+1} q_{t+1}     - e q_t,
        sigma_{t+1} = sigma_t + m d_{t+1} theta_{t+1} - e theta_t,
    both exact. With q_{t-1} theta_t - q_t theta_{t-1} = +-1 the frame
    pair inverts as
        |x| <= |R| |theta_{t-1}| + |sigma| q_{t-1},
        |y| <= |sigma| q_t       + |R| |theta_t|.
B2  THE STAR IS BOUNDED BY THE FUTURE. A branch that flushes at L has
    sigma_t = sum_{k=t}^{L-1} e_k theta_k - m sum_{j=t+1}^{L} d_j
    theta_j. The telescoping identity a_{k+1}|theta_k| = |theta_{k-1}|
    - |theta_{k+1}| gives sum_{k>=t} a_{k+1}|theta_k| = |theta_{t-1}| +
    |theta_t|, and the same identity at a >= 1 gives sum_{k>=t}
    |theta_k| <= |theta_{t-1}| + |theta_t|. With e_k <= a_{k+1} + s and
    d_j <= a_{j+1},
        |sigma_t| <= (1+s)(|theta_{t-1}| + |theta_t|)
                     + m(|theta_t| + |theta_{t+1}|),
    so with q_t|theta_{t-1}| < 1, q_t|theta_t| < 1, q_t|theta_{t+1}| <
    1: |sigma_t| q_t <= 2(1 + s) + 2m, and the same for q_{t-1}.
B3  THE RESIDUAL IS BOUNDED BY THE PAST, AT q_{t+1} AND NOT q_{t+c+1}.
    R_t = m sum_{k<=t} d_k q_k - sum_{k<t} e_k q_k: the PRE-READ digits
    d_{t+1..t+c} are held separately in the state and are not in R_t
    (seed(d0) = (m d_0, -k), succ folding one digit per step). The
    legal input to position t is under q_{t+1}, so the first term is <
    m q_{t+1}; the output paid is sum_{k<t}(a_{k+1} + s) q_k <=
    (q_t + q_{t-1}) + s sum_{k<t} q_k <= (1 + s) q_{t+1}. So |R_t| <=
    max(m, 1+s) q_{t+1}, with no c in it. Then q_{t+1}|theta_t| < 1 and
    q_{t+1}|theta_{t-1}| < a_{t+1} + 1 <= A + 1.
B4  THE BOX. Substituting B2 and B3 into B1:
        |y| <= 2(1 + s) + 2m + max(m, 1+s),
        |x| <= 2(1 + s) + 2m + max(m, 1+s)(A + 1).
    x 3 at s = s_0 = 1 over A = 2: (19, 13) -- against U2's (95, 41)
    and INSIDE the BOX-6 run's (72, 27). x 2 at s = s_0 = 1: (14, 10)
    at A = 2, (16, 10) at A = 3. The c-dependence is gone entirely.
    Sanity: branches differ by the kernel (q_{t-1}, -q_t), whose star
    is +-1, while B2 bounds |sigma| by a multiple of |theta_{t-1}| ->
    0, so at most one branch survives past the first few positions --
    which is what the parent's own P4 note reads off its prints.
TRANSPLANT, marked: none. Every step above is re-derived here; U2's box
is treated as a claim to attack and not as an input.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS,
never what they would mean).
  C1 (controls, run FIRST; nothing below is read if any is red)
      (a) THE RE-BOXED ENGINE REPRODUCES THE OLD CELLS. The twelve
      singleton-alphabet cells ({1}, {2}, {3} x maps 2, 3 x slacks
      (1,1), (2,2)) at the derived box print the parent's F3 lookahead
      -- the guard the banked species asks for (a re-coordinatized or
      re-boxed state silently choosing one representative of a set the
      old state kept).
      (b) Every winning cell's strategy certifies 0 bad on n < N_CHECK
      at the random and short periodic windows, as the parent's C1b.
  P1  THE DIRECT TEST OF B4, and it is the sharp one. The transition
      is INVERTIBLE (y = X - m d_{t+1}, x = Y + e + a_{t+1} y), so from
      a certified run's recorded triples (e_t, d_{t+1}, a_{t+1}) the
      trajectory of the branch that ACTUALLY FLUSHES reconstructs
      backward from (0, 0), exactly. Over every n and window of the
      certification set, for a set of winning cells, the rig prints the
      maximal |x| and |y| on those flushing trajectories beside the B4
      bound. A printed value ABOVE the bound REFUTES B4 and nothing
      below it is read. THE TRACE BOX MUST EXCEED B4 OR THE TEST IS
      VACUOUS -- a trajectory cannot leave the box it was pruned in, so
      each traced cell is solved in a box a stated multiple of B4 and
      the multiple is printed beside the maxima. (The reconstruction's own control:
      the trajectory's position-0 pair must be (m d_0, -k) for an
      integer k, printed as the seed check.)
  P2  x 3 at (1, 1) over {1, 2} at c = 2 at the derived box (19, 13)
      and at twice it (38, 26): a print of "-" at both. A WIN at
      either decides the cell the other way outright and is read as
      such (a win transfers at any box, U2).
  P3  the state count per cell against the box, printed; and the peak
      under memwatch named in the run record.

THE DESIGN
----------
Stages: s0 the C1a controls at the derived box; s1 the P1
reconstruction over the winning cells; s2 the P2 verdict cells; s3 the
seed-range test the audit added (see G5). The
engine is explore_universal_reader.Universal with the box taken from
B4 instead of from its BOX multiplier -- same game, same transition,
same solver; only the pruning bound and, in s3, the seed's M range
move. Stage and cell selection
come from the environment (RBOX_STAGES, RBOX_SCALE, RBOX_CELLS,
RBOX_SEED) so each
heavy cell runs as its own process. Memory: the reachable state space is
built explicitly; run under memwatch.py.

FINDINGS (entered post-run; every number below sits in this file's
printed output. Runs, each under memwatch at the 512 MB default, peaks
as WORKING SET with the kill read on commit: s0 in 8 s, peak 24.8 MB;
s1's default list in 19 s, peak 519.9 MB -- KILLED at 516 MB commit on
its eighth cell, the seven before it complete; two follow-up processes
for the killed cells at smaller multiples, both KILLED at 514 MB commit
with nothing printed; s2 in 6 s, peak 480.4 MB; s3 in 7 s at the doubled boxes, peak
519.7 MB -- KILLED at 516 MB commit on its tripled verdict box, after
the doubled one printed. s1 was re-run after the audit added a guard skipping an
unflushed trace, which changed no printed number -- unflushed was 0
at every cell both times.)

G1  THE CONTROLS HOLD (C1a). All twelve singleton-alphabet cells at the
    derived box print the parent's F3 lookahead -- 0, 0, 2, 0 / 2, 0, 2,
    2 / 2, 2, 2, 2 across ({1},{2},{3}) x (x2, x3) x ((1,1),(2,2)) -- and
    every winning strategy certified 0 bad. 421 to 5,894 states. So the
    re-boxed engine is the old engine at a different pruning bound, which
    is what the banked species asks before anything below is read.
G2  B4 SURVIVES ITS OWN TEST, WITH ROOM (P1). Six distinct winning cells
    over seven runs (the {2} x 3 cell twice, at 4x and at 8x), each
    solved in a box 3x to 8x the B4 bound so a violation had somewhere to
    happen, every flushing trajectory reconstructed backward from (0, 0)
    over the certification set -- 13 windows at a singleton alphabet (the
    constant window and twelve random 60-quotient ones) and 16 at {1, 2}
    (two constant, two alternating, twelve random), every n < 1000 with
    n = 0 skipped as having no digits:
        cell            box run    room   B4        trace max   states
        {1}   x3 c=2    (64,52)    x4     (16,13)   (3,2)        6,067
        {2}   x2 c=2    (56,40)    x4     (14,10)   (4,1)        6,199
        {2}   x3 c=2    (76,52)    x4     (19,13)   (6,2)       11,041
        {3}   x2 c=2    (64,40)    x4     (16,10)   (6,1)       11,975
        {3}   x3 c=2    (88,52)    x4     (22,13)   (9,2)       19,629
        {2}   x3 c=2   (152,104)   x8     (19,13)   (6,2)       23,011
        {1,2} x2 c=2    (42,30)    x3     (14,10)   (4,2)      382,853
    Not one trajectory reaches even half of B4 in |x|, or a quarter of it
    in |y|; seedbad 0 and unflushed 0 at every cell, so every trajectory
    read really did start at (m d_0, -k) and really did flush. The two
    remaining cells of the list -- {1,2,3} x2 c=2 and {1,2} x3 c=3 --
    are UNRUN: both need a box above B4 to be non-vacuous and both
    exceed 512 MB there (killed at 1.5x and at 1.25x respectively). So
    the test is silent at a multi-letter alphabet for x 3, and says so.
G3  THE VERDICT: x 3 AT s = s_0 = 1 OVER QUOTIENTS <= 2 READS AT
    EXACTLY 3 (P2). The cell LOSES at lookahead 2 at the B4 box (19,13),
    88,733 states, and at twice it (38,26), 366,115 states -- and the
    parent's BOX-6 run (72,27) lost there too. All three contain B4's
    (19,13), so by B4 each is a real loss of the universal game, while
    the win at 3 was already certified. Since every periodic window of
    the class reads at 2 (explore_universal_reader.py F5, now 2,538
    primitive {1,2}-necklaces to period 14), THE QUOTIENT SWITCH COSTS
    x 3 ONE UNIT OF LOOKAHEAD: the universal reader over a bounded
    alphabet is strictly weaker than every stationary reader in it.
    EXACTLY 3 also uses monotonicity in c, which is worth saying because
    only c = 2 was run at a box containing B4: a reader at lookahead c is
    simulable at c + 1 by ignoring the extra digit it is handed, so wins
    are monotone in c and the real loss at 2 carries down to 1 and to 0.
    (The parent's losses at 0 and 1 sit at BOX 2 and BOX 1.5, whose |y|
    of 11 and 9 do NOT contain B4's 13, so they do not transfer on their
    own -- the monotonicity is doing that work, not those runs.)
G4  WHAT U2's BOX WAS. Loose, not wrong. Its |R_t| <= m q_{t+c+1} prices
    a residual that has swallowed the whole pre-read with nothing
    emitted against it, where the engine's R_t stops at position t; the
    (A+1)^c that follows is the entire gap between (95, 41) and (19, 13),
    and with it goes the only reason the cell was left open.
G5  THE SEED IS WIDE ENOUGH, AND IT WAS NOT OBVIOUS (s3, added in the
    audit). G3 rests on TWO completeness facts, not one: the pruning box
    (B4) and the SEED's range of M. The seed takes |M| <= 2m + 2 from
    D8 (explore_limit_maps.py) -- but D8 derives that from a LEGAL
    output string's star lying in (-alpha, 1 - alpha), and this game's
    output is REDUNDANT, whose star range is longer by the excess. B2
    at t = 0 allows |M| up to 2(1 + s) + 2m + m|theta_0|(a_1 - 1),
    about 13 at m = 3 where the seed stops at 8; and a seed that is too
    narrow has exactly one artifact, a FALSE LOSS -- the verdict. Read
    directly rather than argued: widening the seed to |M| <= 20 moves
    NO control -- all six singleton (1,1) cells keep their lookahead,
    states 946 -> 911, 2810 -> 2688, 3030 -> 3020, 5370 -> 5370,
    5852 -> 5792, 11151 -> 11121 -- and the verdict cell still LOSES,
    363,321 states at (38,26), the same count the narrow seed gives
    there. So the narrow seed was not hiding a win, and G3 stands on a
    tested hypothesis rather than an inherited one.
    THE FIRST VERSION OF THIS TEST WAS ITSELF WRONG, which is why the
    boxes here are the doubled ones: pack() has no range check, so a
    seed with |k| above the box's b_y ALIASES onto another pair rather
    than being pruned. The first pass seeded |M| <= 20 into boxes of
    b_y 10 and 13 and read six controls and one verdict off aliased
    branches. The seed is now CLAMPED to the box and every cell runs at
    a box with b_y >= the seed, cells that cannot being SKIPPED and
    said so; the one figure that survived unchanged is the (38,26)
    verdict, whose box was already tall enough. Spurious branches can
    only make a state easier to win from -- a state dies only when
    every branch does -- so the direction of the old error was toward a
    false WIN, and it printed a loss; but that is an argument, and the
    clean run is the record.

TIER. B4 is proved algebraically here (B1-B4) and checked at the six
cells of G2; G3 is a rule -- the class decided by an exhaustive solve of
a finite game at three boxes, each containing B4. Neither is a theorem:
G3 rests on computation at a stated box, and B4 is a bound on THIS
encoding's frame pair, not a statement about readers.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_universal_reader import (            # noqa: E402
    N_CHECK, N_WIN, PARENT, Universal, certify, convergents, greedy)

STAGES = os.environ.get("RBOX_STAGES", "s0,s1,s2").split(",")
SCALE = float(os.environ.get("RBOX_SCALE", "1"))
LOOKCAP = int(os.environ.get("RBOX_LOOKCAP", "3"))


def derived_box(m, s, A):
    """B4: the necessary box, as a pair (b_x, b_y)."""
    base = 2 * (1 + s) + 2 * m
    return base + max(m, 1 + s) * (A + 1), base + max(m, 1 + s)


class BoxUniversal(Universal):
    """The parent's game with the pruning box, and the seed's M range,
    given outright. SEED_M None = the parent's 2m + 2 (D8)."""

    def __init__(self, alph, m, s, s0, look, bx, by, seed_m=None):
        self.alph, self.m, self.s, self.s0, self.look = (
            tuple(alph), m, s, s0, look)
        self.bx, self.by = bx, by
        self.seed_m = seed_m
        self.K = 2 * self.by + 1
        self.build()

    def seed(self, d0):
        if self.seed_m is None:
            return Universal.seed(self, d0)
        M = self.seed_m
        # pack() has no range check: a |k| above by would alias onto
        # another pair, so the seed is CLAMPED to the box and the caller
        # is responsible for running at a box with by >= seed_m.
        return tuple(sorted(self.pack(self.m * d0, -k)
                            for k in range(-M, M + 1)
                            if abs(k) <= self.by
                            and abs(self.m * d0) <= self.bx))


def min_look(alph, m, s, s0, bx, by, cap=None):
    cap = LOOKCAP if cap is None else cap
    g = None
    for look in range(cap + 1):
        g = BoxUniversal(alph, m, s, s0, look, bx, by)
        if g.wins:
            return look, g
    return None, g


def flush_trace(g, digits, quots):
    """P1: run the strategy, then reconstruct the FLUSHING branch's
    trajectory backward from (0, 0) through the recorded triples.
    Returns (max|x|, max|y|, seed_pair, flushed)."""
    c = g.look
    T = len(digits)
    d = list(digits) + [0] * (c + 8)
    st = (g.seed(d[0]), tuple(quots[:c + 1]), tuple(d[1:c + 1]),
          d[c] == 0, True)
    i = g.ids[st]
    steps = []
    for t in range(T + 6):
        e = g.choose(i)
        a1, d1 = g.states[i][1][0], (g.states[i][2] + (d[t + c + 1],))[0]
        steps.append((e, d1, a1))
        st2 = g.succ(g.states[i], e, quots[t + c + 1], d[t + c + 1])
        i = g.ids[st2]
    flushed = g.holds0(g.states[i])
    x, y = 0, 0
    mx, my = 0, 0
    for e, d1, a1 in reversed(steps):
        y, x = x - g.m * d1, y + e + a1 * (x - g.m * d1)
        mx, my = max(mx, abs(x)), max(my, abs(y))
    return mx, my, (x, y), flushed


def trace_cell(alph, m, s, s0, look, bx, by, seed=0):
    """P1 over one winning cell: the certification set, every n."""
    import random
    g = BoxUniversal(alph, m, s, s0, look, bx, by)
    if not g.wins:
        print("  TRACE SKIPPED (cell does not win at this box)")
        return None
    rng = random.Random(seed)
    windows = [[a] * 60 for a in alph]
    if len(alph) > 1:
        windows += [[alph[i % 2] for i in range(60)],
                    [alph[(i + 1) % 2] for i in range(60)]]
    windows += [[rng.choice(alph) for _ in range(60)] for _ in range(N_WIN)]
    mx, my, bad_seed, unflushed = 0, 0, 0, 0
    for quots in windows:
        q = convergents(quots, 40)
        for n in range(N_CHECK):
            digs = greedy(n, q)
            if not digs:
                continue
            ax, ay, seed_pair, flushed = flush_trace(g, digs, quots)
            if not flushed:
                # the reconstruction starts at (0, 0); with no flush
                # there is no flushing branch and the trace is meaningless
                unflushed += 1
                continue
            mx, my = max(mx, ax), max(my, ay)
            if seed_pair[0] != m * digs[0]:
                bad_seed += 1
    return mx, my, bad_seed, unflushed, g.n_states


def s0_controls(scale):
    print("== s0  C1a: the re-boxed engine at the derived box")
    red = 0
    for A in (1, 2, 3):
        for m in (2, 3):
            for s, s0 in ((1, 1), (2, 2)):
                bx, by = derived_box(m, s, A)
                bx, by = int(bx * scale), int(by * scale)
                look, g = min_look((A,), m, s, s0, bx, by)
                want = PARENT[(A, m)][(s, s0)]
                bad = 0
                if look is not None:
                    bad, _, _ = certify(g, (A,), "{%d} x%d (%d,%d)"
                                        % (A, m, s, s0))
                print("  {%d} x%d (%d,%d)  look %s  want %d  box (%d,%d)"
                      "  states %d  bad %d"
                      % (A, m, s, s0, look, want, bx, by, g.n_states, bad))
                if look != want or bad:
                    red += 1
                    print("    RED")
    print("  C1a %s" % ("GREEN" if red == 0 else "RED (%d)" % red))
    return red == 0


#   (alphabet, m, lookahead, the multiple of the B4 box it is solved in)
DEFAULT_TRACE = ("1|3|2|4;2|2|2|4;2|3|2|4;3|2|2|4;3|3|2|4;2|3|2|8;"
                 "1,2|2|2|3;1,2,3|2|2|2;1,2|3|3|1")
TRACE_CELLS = []
for _spec in os.environ.get("RBOX_CELLS", DEFAULT_TRACE).split(";"):
    _a, _m, _c, _mult = _spec.split("|")
    TRACE_CELLS.append((tuple(int(v) for v in _a.split(",")),
                        int(_m), int(_c), float(_mult)))


def s1_traces(scale):
    print("== s1  P1: the flushing branch's own trajectory vs the B4 box")
    for alph, m, look, mult in TRACE_CELLS:
        A = max(alph)
        bx, by = derived_box(m, 1, A)
        rbx, rby = int(bx * mult * scale), int(by * mult * scale)
        out = trace_cell(alph, m, 1, 1, look, rbx, rby)
        if out is None:
            continue
        mx, my, bad_seed, unflushed, n_states = out
        verdict = "OK" if (mx <= bx and my <= by) else "ABOVE THE BOUND"
        room = "VACUOUS" if (rbx <= bx or rby <= by) else "x%g room" % mult
        print("  {%s} x%d c=%d  box run (%d,%d) %s  B4 (%d,%d)"
              "  trace max (%d,%d)  %s  seedbad %d  unflushed %d"
              "  states %d"
              % (",".join(map(str, alph)), m, look, rbx, rby, room, bx, by,
                 mx, my, verdict, bad_seed, unflushed, n_states))


def s2_verdict(scale):
    print("== s2  P2: x3 (1,1) over {1,2} at c = 2, at the derived box")
    bx, by = derived_box(3, 1, 2)
    for mult in (1, 2):
        rbx, rby = int(bx * mult * scale), int(by * mult * scale)
        g = BoxUniversal((1, 2), 3, 1, 1, 2, rbx, rby)
        print("  box (%d,%d)  x%d the B4 box  states %d  wins %s"
              % (rbx, rby, mult, g.n_states, g.wins))
        if g.wins:
            bad, _, _ = certify(g, (1, 2), "{1,2} x3 (1,1) c=2")
            print("    WIN -- certified bad %d" % bad)


def s3_seed(scale):
    """P3 (added in audit): the SEED's M range is D8's, derived for a
    LEGAL output string; this game's output is REDUNDANT and its star
    range is wider, so a seed at 2m + 2 could be narrow -- and a narrow
    seed's only artifact is a FALSE LOSS, which is exactly the verdict.
    B2 at t = 0 allows |M| up to 2(1+s) + 2m + m|theta_0|(a_1 - 1).
    Widen the seed and re-read: the controls must not move (a wider seed
    can only turn a loss into a win, so a control whose lookahead DROPS
    convicts the parent's grid), and the verdict cell must still lose."""
    wide = int(os.environ.get("RBOX_SEED", "20"))
    mult = float(os.environ.get("RBOX_SEED_MULT", "2"))
    print("== s3  the seed's M range widened to |k| <= %d (D8 gives %d)"
          % (wide, 2 * 3 + 2))
    red = 0
    for A in (1, 2, 3):
        for m in (2, 3):
            bx, by = derived_box(m, 1, A)
            bx, by = int(bx * mult * scale), int(by * mult * scale)
            if by < wide:
                print("  {%d} x%d SKIPPED: box by %d < seed %d (would alias)"
                      % (A, m, by, wide))
                continue
            look, g = min_look((A,), m, 1, 1, bx, by)
            lookw, gw = None, None
            for c in range(LOOKCAP + 1):
                gw = BoxUniversal((A,), m, 1, 1, c, bx, by, seed_m=wide)
                if gw.wins:
                    lookw = c
                    break
            flag = "" if lookw == look else "  MOVED"
            if lookw != look:
                red += 1
            print("  {%d} x%d (1,1)  narrow %s  wide %s  states %d -> %d%s"
                  % (A, m, look, lookw, g.n_states, gw.n_states, flag))
    print("  controls %s" % ("GREEN" if red == 0 else "RED (%d)" % red))
    bx, by = derived_box(3, 1, 2)
    for mlt in (2, 3):
        rbx, rby = int(bx * mlt * scale), int(by * mlt * scale)
        if rby < wide:
            print("  VERDICT SKIPPED: box by %d < seed %d" % (rby, wide))
            continue
        g = BoxUniversal((1, 2), 3, 1, 1, 2, rbx, rby, seed_m=wide)
        print("  VERDICT CELL wide seed  box (%d,%d)  states %d  wins %s"
              % (rbx, rby, g.n_states, g.wins))


if __name__ == "__main__":
    import time
    t0 = time.time()
    print("stages %s  scale %s  N_CHECK %d  N_WIN %d"
          % (STAGES, SCALE, N_CHECK, N_WIN))
    ok = True
    if "s0" in STAGES:
        ok = s0_controls(SCALE)
    if not ok:
        print("controls red: nothing below is read")
    else:
        if "s1" in STAGES:
            s1_traces(SCALE)
        if "s2" in STAGES:
            s2_verdict(SCALE)
        if "s3" in STAGES:
            s3_seed(SCALE)
    print("total %.0f s" % (time.time() - t0))
