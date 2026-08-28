"""Is the flush the WHOLE price? The completion reader's lookahead
against the released integer reader's, proved equal at every periodic
window -- the inequalities the proof rests on, printed at every cell.

THE QUESTION
------------
Two readers of the same trailing map x -> m x at a periodic window.
The COMPLETION reader (explore_completion_reader.py) is the map on
infinite strings: it tracks no offsets, and at each level it owes an
interval -- the unseen input tail scaled by m -- to be placed whole
inside one member of the level range; its minimum lookahead is c_comp.
The RELEASED integer reader (explore_flush_price.py) is the residual
game of explore_redundant_ostrowski.py with its flush requirement
dropped: a finite SET of lattice branches, one per integer lift, pruned
to a level-scaled box, and safety is that the set never empties; its
minimum lookahead is c_saf. They agree at all 130 cells read, never
above and never below, and the inequality c_comp <= c_saf has stood
without proof: the argument offered for it -- a box-confined safe
strategy holds |real/theta| <= breal, "which is the completion reader's
requirement" -- is false, the box being far wider than the level range,
and a safe state with no branch inside the range is exhibited at
sqrt3-1 x3, (s, s_0) = (1, 0). Is c_comp = c_saf a theorem, and if so
why did the box's width never matter?

THE HAND-ATTACK (on paper, before the engine) -- the proof
----------------------------------------------------------
Conventions are the parents' (explore_redundant_ostrowski.py H1): the
reader emits e_t having seen d_0..d_{t+c}; theta_k = q_k alpha - p_k;
a branch is the lattice point m_o val(e) - m_i val(d) - M - c alpha in
the frame of the current period, pruned to |real/theta_phi| <= breal
and |conj/theta^c_phi| <= bconj; the box is the reader's own and its
widths are read off the engine, not re-derived.

H1  THE STATE IS A SET OF LIFTS, AND BRANCHES DESCEND DETERMINISTICALLY.
    The integer game's state carries one branch per integer lift M still
    alive; a step maps each branch to exactly one successor (add the
    output digit, subtract the input digit, renormalize at a wrap) and
    drops it if the successor leaves the box. So the branches alive
    along a play form a FOREST: every branch at step t+1 has one parent
    at step t, and a branch's root is its lift M. Safety says the set is
    non-empty at every step of every play from a safe state.
H2  KOENIG: A SAFE PLAY CARRIES ONE BRANCH FOREVER. The box holds
    finitely many lattice points per phase, so each level of the forest
    is finite; a forest that is non-empty at every depth with finite
    levels has an infinite path (Koenig's lemma). Along that path the
    branch's real coordinate obeys |real| <= breal |theta_t| at every
    level in ABSOLUTE terms -- the frame renormalization is by the unit
    that carries theta_k to theta_{k+P}, so a frame bound at phase phi
    after n wraps is breal |theta_phi| |eta|^n = breal |theta_{phi+nP}|
    -- and |theta_t| -> 0. So the residual tends to 0: the digits
    written on that play are a legal string whose value is exactly
    m x + c alpha + M for the path's lift M. That is a coding of the
    completion's target on the circle. THE WIDTH OF THE BOX NEVER
    ENTERS: any level-scaled box forces convergence, which is why "far
    wider than the level range" was never an objection to the
    inequality, only to the argument.
H3  ONE LIFT PER PREFIX WHERE THE COMPLETION GAME DEMANDS IT. The
    completion game with lifts (explore_completion_lift.py H2) is free
    at a level whose range has width >= 1 and demands, at a level whose
    range is narrower, that the whole interval of continuations sit in
    ONE translate T_t + M. H2 hands each infinite input its own lift;
    over the continuations of a fixed prefix the residuals form a
    connected set (the values of legal tails fill an interval -- the
    completion reader's H3, the classical fact that every point of the
    range has an expansion), and a connected set inside a disjoint union
    of closed translates lies in one of them. So the lifts H2 assigns
    agree on every prefix class at every constrained level, and the safe
    strategy -- a function of the seen digits, since the branch set is
    -- WINS the completion game at the same lookahead: c_comp <= c_saf.
H4  THE OTHER DIRECTION IS A CONTAINMENT. Take a winning completion
    strategy at lookahead c and run it in the integer game. Each infinite
    input x has a lift M_x and its output codes m x + M_x; the branch
    rooted at M_x has, at level t, residual
        m_o sum_{k>=t} e_k theta_k - m_i sum_{k>t+c} d_k theta_k
    (the two tails the limit identity leaves), so with m_o = 1, m_i = m:
        |real| <= W_t + m (|theta_{t+c}| + |theta_{t+c+1}|)
              <= (1+s)(|theta_{t-1}| + |theta_t|) + m (|theta_t| + |theta_{t+1}|),
    using W_t = |theta_{t-1}| + |theta_t| + s S_t and THE TAIL LEMMA
    S_t = sum_{j>=t} |theta_j| <= |theta_{t-1}| + |theta_t| (from
    |theta_{k-1}| = a_{k+1}|theta_k| + |theta_{k+1}| >= |theta_k| +
    |theta_{k+1}|, telescoped over alternate indices). The engine's box
    is breal |theta_phi| = (m_o(1+s) + m_i)(|theta_{phi-1}| + |theta_phi|)
    SLACK + |theta_phi| -- the same expression with SLACK >= 1 and a
    unit of theta to spare, so the real coordinate never leaves it. The
    conjugate coordinate is the engine's own derivation (the written
    part under a geometric head, the seen window, the constant and the
    lift), which uses nothing about finishing. And the lift itself lands
    in the initial set: |M| <= m_o W_0 + m_i |A_0| + c_max alpha
    < (1+s+m)(1+alpha) + c_max < 2(1+s+m) + c_max + 1 = mmax, since
    |A_0| <= |theta_{-1}| + |theta_0| = 1 + alpha < 2. So the branch M_x
    survives every step of every play and the strategy is safe:
    c_saf <= c_comp.
H5  WHAT THE EXHIBITED SAFE STATE WITH NO BRANCH IN RANGE MEANS. Its
    check is STATIC -- each carried branch's present star against the
    level range -- and the surviving branch need not pass it at any
    finite level: its residual carries the unseen tail m (d_{t+c+1}, ...)
    as an offset of up to m (|theta_{t+c}| + |theta_{t+c+1}|) beside the
    output tail, so its star can sit outside the range at level t and
    still tend to 0. The static criterion was the wrong one; the
    dynamic one (H2) is the theorem's.
H6  THE THEOREM. At every purely periodic window, every m >= 1 and every
    slack pair the box is derived for (s_0 <= s + 1): c_comp = c_saf --
    and c_saf is the same number for EVERY level-scaled box that carries
    the true-lift branch, the box's width being irrelevant above that
    floor. What the 130 cells were is the verification of a theorem
    whose proof is H2-H4; what this rig prints is H4's inequalities at
    every one of them and H2's play at the exhibited state.
H7  WHERE IT CAN BLOW UP. Floats: theta_k by recursion is cancellation
    garbage by depth 24 (the parents' warning), so every tail sum here
    is a geometric closed form over one period with the unit's ratio,
    never a truncated recursion; the frame identity |theta_{k+P}| =
    |eta| |theta_k| is checked at shallow depth before it is leaned on.
    The tracker below mirrors Game.step branch by branch and is checked
    against the engine's own interned states at every step of every
    play -- a divergence is a rig fault and stops the run.
TRANSPLANT, marked: the windows, the grid, the box, the band cells and
the frozen c_comp = c_saf readings are the parents' (explore_redundant_
ostrowski.py, explore_flush_price.py, explore_completion_reader.py,
explore_completion_lift.py); nothing here re-runs either game's minimum.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS,
never what they would mean).
  C1 (controls, run FIRST; nothing below is read if any leg is red)
     (a) THE TAIL LEMMA AND THE FRAME IDENTITY. At every phase of the six
         windows, S_phi <= |theta_{phi-1}| + |theta_phi| prints as a
         non-negative margin, and |theta_{k+P}| / |theta_k| = |eta| to
         1e-9 for k = 0..P-1 by the shallow recursion.
     (b) THE BOX IS THE ENGINE'S. The replica of breal and mmax used
         over the 154 cells agrees with a built Game's own to 1e-12 at
         three cheap cells.
     (c) THE TRACKER DISCRIMINATES. At the exhibited state's cell, a
         RANDOM legal output policy empties the branch set before depth
         60 in at least one of 300 plays (the rate printed); a policy
         that never lost would make P2's survival unreadable.
  P1 THE CONTAINMENT MARGINS (H4), at all 144 grid cells (six windows,
     x2..x5, six slack pairs) and the ten band cells: per cell the least
     over phases of breal |theta_phi| minus the true-lift bound, and
     mmax minus the lift bound. KILL, as an observable: any margin
     printed below 0.
  P2 THE PLAY AT THE EXHIBITED STATE (H2, H5): sqrt3-1 [1,2] x3,
     (s, s_0) = (1, 0), lookahead 2 (the parent's c_saf), 300 random
     legal inputs to depth 60 under a safety-only strategy, with two
     control cells beside it. Per cell the rig prints: plays whose branch
     set is non-empty at every step (predicted 300 -- safety's own
     promise, here a check of the tracker); plays where ONE lineage spans
     all 60 steps (predicted 300, H1-H2); plays with at least one step at
     which NO carried branch sits inside the level range (predicted > 0
     at the exhibited cell -- H5's static reading reproduced on the same
     plays that carry a lineage to the end); and the largest absolute
     residual of a surviving branch at depth 60 against breal
     |theta_60| (predicted under it, H2's convergence in absolute terms).
  P3 the wall-clock and state counts per cell, printed.

THE DESIGN
----------
Stages: s0 the C1 controls; s1 the P1 margins; s2 the P2 plays. The
windows come through explore_flush_price.window_of, the box through a
verbatim replica of Game's constructor lines (checked in s0b), the
safety fixpoint through a copy of explore_flush_price.safety_wins that
returns the set. The tracker keeps a dict branch -> root lift and mirrors
Game.step; after every step the frozenset of its branches must equal
the engine's interned state's, or the run aborts. Inputs are random
legal strings under the engine's own cap_in and after-zero rule.
Everything runs under 512 MB in one process; the cell builds are the
parents' sizes at the lookaheads used.

FINDINGS (post-run; the prints are the record)
----------------------------------------------
F1  THE CONTROLS HOLD (C1). The frame identity to 1.4e-13 at worst (V2)
    and the tail lemma's margin non-negative at every phase of the six
    windows -- with EQUALITY at golden, where every partial quotient is
    1 and |theta_{k-1}| = |theta_k| + |theta_{k+1}| is exact, so the
    margin prints -2e-16 and the flag reads it at a 1e-12 tolerance (the
    first run's flag read it as red at 0; the tolerance is the only
    change between the runs). The replica box is the engine's to 0.0 at
    all three cells, mmax the same. The random policy empties the branch
    set in 300 of 300 plays at the exhibited cell: the tracker's
    survival print discriminates.
F2  THE CONTAINMENT MARGINS ARE POSITIVE AT ALL 154 CELLS (P1): the
    least real margin +0.18690 at V2 x2 (0,0) and (0,1), the least lift
    margin +1.80385 at sqrt3-1 x2 (0,0); no margin below 0. The five
    smallest all sit at V2 x2, the window whose |theta_phi| is least. The
    margin is at least |theta_phi| by the algebra in H4, so the print
    confirms the reading of the engine's box rather than the sign.
F3  THE PLAY AT THE EXHIBITED STATE (P2), and the two controls: at
    sqrt3-1 x3 (1,0) c=2 (1,885 states, safe), golden x2 (1,1) c=2 (570)
    and bronze x2 (0,1), which the ascent reads safe first at c=2
    (1,550): the set is non-empty at every step in 300 of 300 plays and
    ONE lineage spans all 60 steps in 300 of 300 at every cell, and the
    largest end residual of a surviving branch is 0.18, 0.23 and 0.22 of
    breal |theta_60| -- H2's convergence at the scale the box forces.
    P2's THIRD PREDICTION IS REFUTED: a step at which no carried branch's
    owed residual sits inside the level range occurs on 0 of 300 plays
    at every cell. (The rig's first run printed 300, 299 and 300 there
    with the reading's SIGN wrong -- it held the branch's star, written
    - m seen - M, against the range that holds its negative, the
    residual still owed; the sign is the only change between the runs
    and the counts under it are withdrawn.) So this rig's static reading
    -- some carried branch's owed residual inside the level range at its
    phase -- is met at every step of every safe play read, and says
    nothing either way about the exhibited state's reading, which is a
    reach the parent computes and this rig does not. What reconciles
    that state with the theorem is H2 and not a print: the theorem needs
    no static reading at all.
F4  The whole run is 1 s of wall at 19 MB peak; the three cells build
    in under a second each.

TIER. H2-H4 are a PROOF and F1-F3 are its checks: the real and lift
containments H4 rests on hold at every cell of the parents' grid and
band (printed), the conjugate one is the engine's formula read and not
printed, the lemma they use holds at every phase, and the box read is
the engine's. So
c_comp = c_saf is a THEOREM at every purely periodic window, every m >=
1 and every slack pair with s_0 <= s + 1 -- the box's own hypothesis,
which is the one place the engine's derivation enters -- and the 130
frozen cells are its verification. What is NOT claimed: anything at a
non-periodic window (no frame, no box), or under the greedy rule on the
output (the parents' rule=True variant, whose cap depends on the
previous output digit; the argument goes through unchanged but no cell
of it was read here), or that c_saf as a NUMBER is cheap to compute --
the theorem moves the completion reader's minimum onto a finite game and
says which finite game, and nothing about that game's size.

RUN RECORD. python memwatch.py explore_flush_theorem.py: 1.0 s wall,
peak working set 19.1 MB, one process; SEED 20260828, 300 plays to
depth 60 per cell.
"""

import os
import random
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_limit_column import SLACK                  # noqa: E402
from explore_redundant_ostrowski import (               # noqa: E402
    GRID, WINDOWS, Game)
from explore_flush_price import BAND, window_of         # noqa: E402

MS = (2, 3, 4, 5)
DEPTH = 60
PLAYS = 300
SEED = 20260828

# (name, period, m, s, s0, lookahead) -- the exhibited state's cell first
PLAY_CELLS = [
    ("sqrt3-1 [1,2]", (1, 2), 3, 1, 0, 2),
    ("golden [1]", (1,), 2, 1, 1, 2),
    ("bronze [3]", (3,), 2, 0, 1, None),
]


# ------------------------------------------------------------ the sums
def theta_abs(win, k):
    """|theta_k| for any k >= -1 from the period's phases and the unit."""
    P = win.P
    if k == -1:
        return abs(win.thf[-1])
    n, phi = divmod(k, P)
    return abs(win.thf[phi]) * abs(win.eta) ** n


def tail_sum(win, phi):
    """S_phi = sum_{j >= phi} |theta_j|, phi in 0..P-1, closed form."""
    P = win.P
    per = sum(abs(win.thf[psi]) for psi in range(P))
    head = sum(abs(win.thf[psi]) for psi in range(phi, P))
    r = abs(win.eta)
    return head + per * r / (1 - r)


def level_range(win, phi, s, cap0=None):
    """[lo, hi] of the level-phi range in the frame: caps a + s at every
    position from phi on, theta_{nP+psi} = eta^n theta_psi (the frame
    identity s0 checks). cap0, when given, is position 0's own cap in
    the first period (a_1 - 1 + s_0)."""
    P = win.P
    lo = hi = 0.0
    for n in range(0, 400):
        scale = win.eta ** n
        if abs(scale) < 1e-18:
            break
        for psi in range(P):
            k = n * P + psi
            if k < phi:
                continue
            cap = win.a[psi] + s
            if k == 0 and cap0 is not None:
                cap = cap0
            v = cap * win.thf[psi] * scale
            if v < 0:
                lo += v
            else:
                hi += v
    return lo, hi


# ------------------------------------------------------------ the box
def replica_box(win, m, s, look):
    """breal per phase and mmax, the constructor's own lines."""
    mo, mi, cmax = 1, m, 0
    P = win.P
    breal = {}
    for phi in range(P):
        th = abs(win.thf[phi])
        breal[phi] = ((mo * (1 + s) + mi)
                      * (abs(win.thf[phi - 1]) + th) / th
                      * SLACK + 1)
    mmax = 2 * (mo * (1 + s) + mi) + cmax + 1
    return breal, mmax


def true_lift_bound(win, m, s, phi):
    """H4: (1+s)(|theta_{phi-1}| + |theta_phi|) + m(|theta_phi| + |theta_{phi+1}|)."""
    t_prev = abs(win.thf[phi - 1])
    t0 = abs(win.thf[phi])
    t1 = theta_abs(win, phi + 1)
    return (1 + s) * (t_prev + t0) + m * (t0 + t1)


def lift_bound(win, m, s):
    """H4: (1+s+m)(1+alpha) + c_max alpha, c_max = 0 for x m."""
    return (1 + s + m) * (1 + win.alpha)


# ------------------------------------------------------------ safety
def safety_set(g):
    W = set(i for i in g.trans if g.alive[i])
    changed = True
    while changed:
        changed = False
        for st in list(W):
            ok = any(all(s2 in W for _x, s2 in succ)
                     for succ in g.trans[st].values())
            if not ok:
                W.discard(st)
                changed = True
    return W


def safe_move(g, W, i):
    for y, succ in g.trans[i].items():
        if all(s2 in W for _x, s2 in succ):
            return y
    return None


def random_input(g, rng, length):
    """A random legal input string under cap_in and the after-zero rule."""
    d = []
    pzd = True
    for k in range(length):
        xs = g.inputs(k, pzd)
        x = rng.choice(xs)
        d.append(x)
        pzd = (x == 0)
    return d


# ------------------------------------------------------------ tracker
class Tracker:
    """The branch forest of one play, mirrored on Game.step with roots."""

    def __init__(self, g, d):
        self.g = g
        self.d = d
        init = {}
        for M in g.mrange:
            for c in g.cs:
                init[(-M, -c)] = M
        br = init
        for k in range(g.look + 1):
            nb = {}
            for (u, w), root in br.items():
                key = (u - g.mi * d[k] * g.thv[k][0],
                       w - g.mi * d[k] * g.thv[k][1])
                nb[key] = root
            br = nb
        self.br = {k: r for k, r in br.items() if g.inbox(k[0], k[1], 0)}
        self.state = (0, frozenset(self.br), d[g.look] == 0, True)
        self.sid = g.ids[self.state]
        self.pos = 0
        self.wraps = 0

    def step(self, y, x):
        g = self.g
        pos = self.pos
        phi = pos % g.P
        k_in = phi + g.look + 1
        wrap = (phi + 1 == g.P)
        nphi = (phi + 1) % g.P
        nb = {}
        for (u, w), root in self.br.items():
            u1, w1 = u + g.mo * y * g.thv[phi][0], w + g.mo * y * g.thv[phi][1]
            if not g.inbox(u1, w1, phi):
                continue
            u2 = u1 - g.mi * x * g.thv[k_in][0]
            w2 = w1 - g.mi * x * g.thv[k_in][1]
            if wrap:
                u2, w2 = g.win.apply_hinv(u2, w2)
            if g.inbox(u2, w2, nphi):
                nb[(u2, w2)] = root
        self.br = nb
        self.pos = g.npos(pos)
        if wrap:
            self.wraps += 1
        # the engine's own successor, for the cross-check
        self.sid = dict(g.trans[self.sid][y])[x]
        st = g.states[self.sid]
        assert frozenset(nb) == st[1], "tracker diverged from the engine"
        return phi


def play(g, W, d, rng, s, s0, policy):
    """One play; returns (nonempty_all, lineage_spans, static_miss,
    absres, breal_at_end, roots_alive_at_end)."""
    tr = Tracker(g, d)
    nonempty = bool(tr.br)
    static_miss = False
    roots_alive = set(tr.br.values())
    for t in range(DEPTH):
        if not tr.br:
            nonempty = False
            break
        i = tr.sid
        if policy == "safe":
            y = safe_move(g, W, i)
            if y is None:
                y = g.outputs(g.states[i])[0]
        else:
            y = rng.choice(g.outputs(g.states[i]))
        phi = tr.pos % g.P
        # the static reading: is any carried branch's star inside the
        # level range at this phase (first period, position 0: own cap)?
        cap0 = g.a[0] - 1 + s0 if (tr.wraps == 0 and phi == 0) else None
        lo, hi = level_range(g.win, phi, s, cap0)
        # the branch's star is written - m seen - M, so the residual
        # still OWED is its negative, and that is what the range holds
        inside = any(lo - 1e-12 <= -g.win.real(u, w) <= hi + 1e-12
                     for (u, w) in tr.br)
        if not inside:
            static_miss = True
        x = d[t + g.look + 1]
        tr.step(y, x)
        roots_alive = set(tr.br.values())
    spans = bool(tr.br) and nonempty
    absres = None
    bend = None
    if tr.br:
        phi = tr.pos % g.P
        scale = abs(g.win.eta) ** tr.wraps
        absres = max(abs(g.win.real(u, w)) for (u, w) in tr.br) * scale
        bend = g.breal[phi] * abs(g.win.thf[phi]) * scale
    return nonempty, spans, static_miss, absres, bend, len(roots_alive)


# ------------------------------------------------------------ stages
def s0_controls():
    print("== s0  C1 controls")
    ok = True
    for name, period in WINDOWS:
        win = window_of(period)
        P = win.P
        # (a) frame identity by shallow recursion on (p, q)
        q = {-1: 0, 0: 1}
        p = {-1: 1, 0: 0}
        for k in range(1, 2 * P + 1):
            q[k] = win.a[(k - 1) % P] * q[k - 1] + q[k - 2]
            p[k] = win.a[(k - 1) % P] * p[k - 1] + p[k - 2]
        worst = 0.0
        for k in range(0, P):
            tk = abs(q[k] * win.alpha - p[k])
            tkP = abs(q[k + P] * win.alpha - p[k + P])
            worst = max(worst, abs(tkP / tk - abs(win.eta)))
        margins = []
        for phi in range(P):
            margins.append(abs(win.thf[phi - 1]) + abs(win.thf[phi])
                           - tail_sum(win, phi))
        flag = "" if (worst < 1e-9 and min(margins) >= -1e-12) else "   RED"
        ok = ok and not flag
        print("  %-14s frame |eta| dev %.1e   tail-lemma min margin %+.4f%s"
              % (name, worst, min(margins), flag))
    # (b) the replica against built games
    for name, period, m, s, s0, look in [("golden [1]", (1,), 2, 1, 1, 1),
                                         ("silver [2]", (2,), 3, 0, 1, 1),
                                         ("bronze [3]", (3,), 2, 2, 2, 0)]:
        win = window_of(period)
        g = Game(win, 1, m, (0,), look, s, s0)
        breal, mmax = replica_box(win, m, s, look)
        dev = max(abs(breal[phi] - g.breal[phi]) for phi in range(win.P))
        same = (mmax == max(g.mrange))
        flag = "" if (dev < 1e-12 and same) else "   RED"
        ok = ok and not flag
        print("  replica box at %-14s x%d (%d,%d) c=%d: breal dev %.1e  mmax %s%s"
              % (name, m, s, s0, look, dev, "same" if same else "DIFF", flag))
    # (c) the random policy at the exhibited cell
    name, period, m, s, s0, look = PLAY_CELLS[0]
    win = window_of(period)
    g = Game(win, 1, m, (0,), look, s, s0)
    W = safety_set(g)
    rng = random.Random(SEED)
    deaths = 0
    for _ in range(PLAYS):
        d = random_input(g, rng, DEPTH + look + 2)
        nonempty, spans, _sm, _a, _b, _r = play(g, W, d, rng, s, s0, "random")
        if not spans:
            deaths += 1
    flag = "" if deaths >= 1 else "   RED"
    ok = ok and not flag
    print("  random policy at %s x%d (%d,%d) c=%d: %d of %d plays empty the set%s"
          % (name, m, s, s0, look, deaths, PLAYS, flag))
    print("  C1 %s" % ("GREEN" if ok else "RED"))
    return ok


def s1_margins():
    print("== s1  P1: the containment margins (H4) at 144 grid + 10 band cells")
    worst_real = None
    worst_lift = None
    n = 0
    neg = 0
    rows = []
    cells = [(name, period, m, s, s0)
             for name, period in WINDOWS for m in MS for s, s0 in GRID]
    cells += [(name, period, m, s, s) for name, period, m, s, _w in BAND]
    for name, period, m, s, s0 in cells:
        win = window_of(period)
        breal, mmax = replica_box(win, m, s, 0)
        mr = min(breal[phi] * abs(win.thf[phi]) - true_lift_bound(win, m, s, phi)
                 for phi in range(win.P))
        ml = mmax - lift_bound(win, m, s)
        n += 1
        if mr < 0 or ml < 0:
            neg += 1
        rows.append((mr, ml, name, m, s, s0))
        if worst_real is None or mr < worst_real[0]:
            worst_real = (mr, name, m, s, s0)
        if worst_lift is None or ml < worst_lift[0]:
            worst_lift = (ml, name, m, s, s0)
    print("  cells %d   negative margins %d" % (n, neg))
    print("  least real margin %+.5f at %s x%d (%d,%d)" % worst_real)
    print("  least lift margin %+.5f at %s x%d (%d,%d)" % worst_lift)
    for mr, ml, name, m, s, s0 in sorted(rows)[:5]:
        print("    %+.5f  %+.4f  %-14s x%d (%d,%d)" % (mr, ml, name, m, s, s0))
    return neg == 0


def s2_plays():
    print("== s2  P2: the play at the exhibited state and two controls")
    for name, period, m, s, s0, look in PLAY_CELLS:
        t0 = time.time()
        win = window_of(period)
        if look is None:
            look = 0
            while True:
                g = Game(win, 1, m, (0,), look, s, s0)
                W = safety_set(g)
                if all(i in W for i in g.init):
                    break
                look += 1
        else:
            g = Game(win, 1, m, (0,), look, s, s0)
            W = safety_set(g)
        safe = all(i in W for i in g.init)
        rng = random.Random(SEED + 1)
        cnt_ne = cnt_sp = cnt_sm = 0
        worst = 0.0
        roots = set()
        for _ in range(PLAYS):
            d = random_input(g, rng, DEPTH + look + 2)
            ne, sp, sm, absres, bend, nroots = play(g, W, d, rng, s, s0, "safe")
            cnt_ne += ne
            cnt_sp += sp
            cnt_sm += sm
            if absres is not None:
                worst = max(worst, absres / bend)
        print("  %-14s x%d (%d,%d) c=%d  safe %s  states %d"
              % (name, m, s, s0, look, safe, g.n_states))
        print("    plays %d: set non-empty at every step %d, one lineage "
              "spans all %d steps %d, plays with a step where no branch "
              "sits in the level range %d, largest end residual / "
              "(breal |theta_end|) %.4f   %.0f s"
              % (PLAYS, cnt_ne, DEPTH, cnt_sp, cnt_sm, worst,
                 time.time() - t0))


def main():
    t0 = time.time()
    ok = s0_controls()
    if not ok:
        print("controls red; nothing below is read")
        return
    s1_margins()
    s2_plays()
    print("total %.0f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
