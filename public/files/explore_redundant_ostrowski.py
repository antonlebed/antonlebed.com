"""Does a REDUNDANT Ostrowski alphabet buy the arithmetic maps a bottom-up
reader at bounded lookahead? The residual game on the carry automaton,
read exactly at the periodic windows over (map, slack).

THE QUESTION
------------
At every irrational window x m and floor(n/m) have no bottom-up reader
at bounded lookahead into the LEGAL Ostrowski strings: the images of
inputs converging to -alpha/m straddle the cut -alpha, whose two
codings part at the lowest admissible digit (the unimodular family,
explore_aperiodic_address.py D5). A positional window buys addition
back at lookahead 1 or 2 with an OVERLAPPING digit set
(explore_lookahead_proof.py). Admit output digits up to a_{k+1} + s at
k >= 1 and a_1 - 1 + s_0 at position 0, DROP the below-a-cap rule
(several strings per integer), keep the input greedy, and ask: which
maps have a bottom-up reader at bounded lookahead, and at what
lookahead? The reader chooses among the accepted output strings as it
goes -- a game against the input's continuation, with a winning set
per lattice state.

THE HAND-ATTACK (on paper, before the engine)
---------------------------------------------
Notation as in explore_limit_maps.py D7-D9: theta_k = q_k alpha - p_k,
the real star of a string is sum e_k theta_k (a REAL, not a circle
point -- two codings of one integer can differ by an integer in it,
which is D8's M), lookahead c means e_t is a function of d_0..d_{t+c}.

H1  THE TAIL RANGES. Tail values from position L (L even) fill the
    interval [-|theta_L| - s S_odd(L), |theta_{L-1}| + s S_even(L)],
    S_par(L) the parity sum of |theta_k| over k >= L: an interval,
    each step |theta_k| being under the diameter of the rest. The
    total range has length 1 + EXCESS, EXCESS = s_0 alpha +
    s sum_{k>=1} |theta_k|.
H2  THE TEAR SURVIVES IFF EXCESS = 0. At EXCESS = 0 the range is
    exactly [-alpha, 1 - alpha] and a coding of N has real star
    N alpha - P in it, so the K-even images of D5's family code near
    the MIN endpoint and the K-odd near the MAX; a coding within delta
    of the min agrees with the min string (0, a_2, 0, a_4, ...) at
    every position with |theta_k| > delta (the difference is a sum of
    non-negative terms), likewise the max string (a_1 - 1, 0, a_3, 0,
    ...). Whatever the reader chooses, the two subsequences part where
    those two strings part: position 0 at a_1 >= 2, position 1 at
    a_1 = 1 -- the legal address. Dropping the rule alone buys nothing.
    At EXCESS > 0 every circle point has a real lift interior to the
    range, and an interior point of a level-L range is interior to
    some member e_L theta_L + [level L + 1 range] (members overlap by
    |theta_{L+1}| + s S(L+1) > 0): a coding with the point interior at
    every depth exists, and the obstruction is gone everywhere.
H3  THE DELAY BOUND. Members A + j delta + [0, D] with D >= delta: an
    interval of length <= D - delta inside their union lies inside one
    member. At lookahead c the residual for e_L is m times an input
    cell at depth L + c + 1, an arc under 2m |theta_{L+c}|, inside the
    level-L range by the invariant; it fits a member whenever
    2m |theta_{L+c}| <= |theta_{L+1}| + s S(L+1). With |theta_{k+2}| <
    |theta_k| / (a_{k+2} + 1) <= |theta_k| / 2 everywhere (from
    |theta_k| = a_{k+2}|theta_{k+1}| + |theta_{k+2}| and
    |theta_{k+2}| < |theta_{k+1}|; the 2/3 a first pass used is the
    same inequality thrown away), c = O(log(2m/(1+s))) works at EVERY
    irrational window once EXCESS > 0 (plus the seam at L = 0:
    2m |theta_c| <= EXCESS). Digitwise identities give upper bounds
    too: e_k = m d_k at s >= (m - 1) a_max is lookahead 0; golden
    2 F_k = F_{k+1} + F_{k-2} is x 2 at s = 1, lookahead 2.
H3' WHAT H3 READS, AND WHAT IT DOES NOT (the re-derivation, and it
    narrows H3's own scope). The invariant H3 maintains is that the
    residual's REAL STAR stays inside the level-L range: that is the
    map on the COMPLETION -- infinite strings, the value a point of
    the circle -- and there H3 is complete. An INTEGER input must also
    FLUSH: the residual integer R_L has to be codable from level L,
    and every codable value is 0 or at least q_L, which the star
    cannot see. Golden, s = s_0 = 1, level 3 (q_3 = 3, q_4 = 5): the
    residual R = 3 has star 3a - 2 = -0.1459 and the level-4 range is
    [-0.1803, 0.2918], so e_3 = 0 (leaving 3, under q_4 and uncodable)
    and e_3 = 2 (leaving -3, negative) BOTH hold the star in range,
    while only e_3 = 1 flushes -- and no star-only tie-break survives
    either, since R = 3 there wants the middle digit and a residual of
    6 wants the largest. So the integer reader needs the set of alive
    integer-offset branches, which is exactly what the game's state
    carries and what its flush condition demands; H3's bound is a
    bound on the completion reader, and the integer reader's existence
    at a general irrational window is OPEN. The grid below reads it
    exactly where the game's STATE SPACE is finite -- the periodic
    windows, where the box and the phase frame recur; the branch set
    at a single state is finite at every window. (SETTLED IN PART
    LATER, explore_universal_reader.py: in the frame (q_t, q_{t-1})
    the game over a bounded quotient alphabet is one finite game with
    the opponent choosing quotients -- x 2 at s = s_0 = 1 reads at 2
    at every window with quotients <= 3, x 3 at 3 over quotients <= 2;
    open at unbounded quotients.)
    (AND NARROWED FURTHER, explore_completion_reader.py. H3 is an upper
    bound on the completion reader and it stands as stated, but it is
    LOOSE in both of its estimates: the residual arc is bounded here by
    2m|theta_{L+c}| where the exact width is m(|theta_{L+c}| +
    |theta_{L+c+1}|), and the fit is read by a ratio test on |theta|
    where the exact quantity is the overlap itself. Rebuilt with true
    widths the same bound beats this one at 89 of the grid's 120 cells,
    by 2 at 30 and by 1 at 59, and is never above it. Even then it is
    NOT that reader's minimum: at the 15 cells where the digitwise
    writing fits, the reader reads 0 while the true-width bound reads 1
    at nine of them and 2 at one -- a condition quantified over every
    placement cannot see winning placements that are isolated points,
    which is what the digitwise identity makes them. So the NECESSARY
    side of this bound is not the overlap condition. The completion
    reader's minimum is measured there directly instead, by an interval
    game with no box in it, and wherever both are decided the distance
    from it up to the integer reader is the flush's price, printed per
    cell by explore_flush_price.py.)
H4  THE FLOORS DO NOT DISSOLVE. D6's jump sends two input tails
    converging to one non-cut input point to images a fixed rotation
    apart; a reader at any lookahead gives them a common output prefix
    whose cylinder has length O(|theta_L|). So floor(n/m) is gated at
    every (s, s_0) and every irrational window: the floors' tear is
    the MAP's (x -> x/m is m-valued on the circle and the branch is
    n mod m, a function of every digit); x m's was the CODING's.
H5  THE ODOMETER. With the rule dropped, n + 1 at s = s_0 = 0 reads at
    lookahead 0 at every window: at a_1 >= 2, e_0 = d_0 + 1 unless
    d_0 = a_1 - 1, then e_0 = 0, e_1 = d_1 + 1 (d_1 = a_2 would force
    d_0 = 0); at a_1 = 1 the same one storey up. The legal odometer's
    lookahead 1 is the rule's.
TRANSPLANT, marked: the positional addition and slope criteria
(explore_lookahead_proof.py, explore_slope_proof.py) are LEADING-end
reads; the trailing Ostrowski x m is the analogue of positional
LEADING x m (the borrow runs against the read), and the floors have no
positional trailing analogue that reads at all.

THE GAME (the engine). State = (position label, the set of alive
M-branches (u, w) with D = u + w alpha in the phase frame of
explore_limit_column.py, the input's last digit zero?). Input digits
are PRE-ADDED c + 1 positions ahead, so no buffer is kept: the state
is a sufficient statistic. Reader emits y at position t, THEN the
opponent reveals d_{t+c+1} (legal: under its cap, and at the cap only
over a zero). A branch leaves when it exits D9's box widened by the
pre-added window -- a box derived for s_0 <= s + 1, position 0's
raised cap then sitting under the full cap sum, which the class
asserts; the reader wins from a state iff some y keeps every
input reply winning (greatest fixed point), AND under zero input it
can reach a state holding the branch (0, 0) within the winning set
(the flush -- an integer input must produce an integer output); the
two conditions alternate to a fixed point. The reader wins at
lookahead c iff every legal pre-read (d_0..d_c) lands in the winning
set. The winning strategy is then RUN on every n < N_CHECK and the
output string's value and digit caps are checked directly.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS,
never what they would mean). Windows: golden [1], silver [2], bronze
[3], sqrt3-1 [1,2], V1 (1,1,1,2), V2 (2,1,3,1). The lookahead searched
at a cell runs to H3's proved bound where H3 grants one, and to
LOOKCAP = 3 where it does not (the (0, 0) column and the floors, whose
cells never win and cost the most: 3.5 GB at lookahead 5 on a first
sizing); "-" means no lookahead up to that cap wins.
  C1 (controls, run FIRST; nothing below is read if any is red)
      (a) the LEGAL output (rule kept, s = s_0 = 0) through this game:
      the identity at lookahead 0, n + 1 at lookahead 1, x 2 and
      x 3 and floor(n/2) at "-", at every window -- the existing
      automaton's verdicts (explore_limit_maps.py L2, L4, L5);
      (b) every cell that prints a lookahead has its strategy run on
      n < N_CHECK with every output value and cap correct.
  P1  (H2) x m, m = 2..5, at (s, s_0) = (0, 0): "-" at every window
      (consistency with a theorem, at LOOKCAP). KILL: any x m cell
      printing a lookahead at (0, 0).
  P2  (H2, H3) x m, m = 2..5, at (0, 1), (1, 0), (1, 1), (2, 2),
      (3, 3): a lookahead at every cell, at most H3's bound
      min{c : |theta_{k+c-1}|/|theta_k| <= (1+s)/(2m) for all k and
      2m |theta_c| <= EXCESS} and at most the digitwise bound (0 when
      s >= (m - 1) a_max and s_0 >= (m - 1)(a_1 - 1), the digitwise
      reader needing position 0's cap m(a_1 - 1)); non-increasing in
      s and in s_0.
      KILL: a "-" at any of these cells, or a printed lookahead above
      either bound, or a lookahead rising with s or s_0.
  P3  (H4) floor(n/2), floor(n/3) at every (s, s_0) in the grid: "-".
      KILL: a floor cell printing a lookahead.
  P4  (H5) n + 1 at (0, 0): lookahead 0 at every window. KILL: 1 or
      more, or "-".
  P5  (the frontier, not predicted) golden x 2 at (1, 1): the printed
      lookahead against the digitwise 2.

THE DESIGN
----------
Stages: s0 the legal control (C1a); s1 the grid over windows x maps x
(s, s_0) with the strategy check (C1b) at every winning cell; the
bounds of P2 printed beside each x m row. Runtime is printed per
window. Memory: the state space is a few thousand states per cell.

FINDINGS (entered post-run; every number below sits in this file's
printed output; the run: 70 s, peak 145 MB under memwatch).

F1  THE CONTROLS HOLD. C1a: through this game the legal output reads
    the identity at 0, n + 1 at 1, and x 2, x 3, floor(n/2) at "-" at
    all six windows -- the existing automaton's verdicts. C1b: every
    winning cell's strategy, run on n < 1500, printed the right value
    under the caps and flushed, 0 bad at the 156 winning grid cells
    (36 n + 1, 120 x m) and the 12 winning control cells.
F2  THE (0, 0) COLUMN IS BLANK (P1, consistency with H2's theorem at
    the cap 3): x 2..x 5 print "-" at every window with the rule
    dropped and the caps kept.
F3  AT THESE SIX WINDOWS ANY RAISED CAP BUYS EVERY x m A BOUNDED
    LOOKAHEAD, UNDER H3's BOUND (P2 held at all 120 cells; the bound
    is the completion reader's, H3', and the integer reader measured
    here sits at or under it at every cell). The grid, cells (0,0) (0,1) (1,0)
    (1,1) (2,2) (3,3), each x m row followed by H3's bound:
      golden   x2  - 3 0 0 0 0 | - 4 3 3 2 1     x3  - 5 2 2 0 0 | - 5 4 4 3 2
               x4  - 5 3 3 2 0 | - 6 4 4 4 3     x5  - 6 3 3 2 2 | - 6 5 5 4 3
      silver   x2  - 2 2 2 0 0 | - 3 2 2 2 1     x3  - 3 2 2 2 2 | - 4 3 3 2 2
               x4  - 3 3 2 2 2 | - 4 3 3 3 2     x5  - 4 3 3 2 2 | - 4 4 3 3 3
      bronze   x2  - 2 2 2 2 0 | - 3 2 2 2 1     x3  - 2 2 2 2 2 | - 3 3 2 2 2
               x4  - 3 2 2 2 2 | - 3 3 3 2 2     x5  - 3 2 2 2 2 | - 3 3 3 3 2
      sqrt3-1  x2  - 3 2 2 0 0 | - 4 3 3 2 1     x3  - 4 2 2 2 2 | - 5 3 3 3 3
               x4  - 5 3 3 2 2 | - 5 4 4 3 3     x5  - 5 3 3 2 2 | - 5 4 4 3 3
      V1       x2  - 3 2 2 0 0 | - 5 3 3 2 1     x3  - 4 2 2 2 2 | - 5 4 4 3 3
               x4  - 5 3 3 2 2 | - 5 5 5 4 3     x5  - 5 4 4 2 2 | - 6 5 5 4 4
      V2       x2  - 3 2 2 2 0 | - 4 3 3 3 1     x3  - 4 2 2 2 2 | - 5 3 3 3 3
               x4  - 4 3 3 2 2 | - 5 4 4 3 3     x5  - 5 3 3 2 2 | - 5 5 5 3 3
    Every printed lookahead is at or under H3's bound and under the
    digitwise bound where one exists, and none rises with s or s_0 --
    so the flush H3' shows the star invariant cannot deliver costs the
    integer reader nothing in lookahead anywhere in this grid.
    Raising position 0's cap by ONE and nothing else (the (0, 1)
    column) already reads every x m, at 2..6, equal to H3's bound at
    9 of the 24 cells, one under at 14 and two under at 1 (V1 x 2).
F4  THE FLOORS STAY BLANK (P3): floor(n/2) and floor(n/3) print "-" at
    every one of the 72 cells, the (3, 3) column included, where every
    x m reads at 2 or below.
F5  THE ODOMETER READS AT 0 (P4): n + 1 prints 0 at all 36 cells,
    (0, 0) included -- the legal 1 is the rule's.
F6  THE FRONTIER (P5 and what the grid shows unasked). Golden x 2 at
    (1, 1) reads 0: at a_max = 1 the slack 1 is already the digitwise
    e_k = 2 d_k, and H3's Fibonacci identity was the long way round. A
    0 appears at exactly the digitwise cells (s >= (m - 1) a_max with
    s_0 >= (m - 1)(a_1 - 1)) and nowhere else, and NO CELL READS AT 1:
    every printed lookahead is 0 or at least 2 (pattern at the grid's
    scope; H3 grants 1 at s >= 2m - 1, which at THESE windows is past
    the digitwise line, so the bound never asks for 1 anywhere in this
    grid -- but the two lines CROSS at a_max > 2 + 1/(m - 1) and the
    clause is this grid's and not a general fact, which is the whole
    reason the pattern needed cells on the other side of the crossing:
    explore_lookahead_band.py). Below the digitwise line
    the floor of the frontier is 2, held by silver and bronze at every
    m >= 3 across s = 1..3.
"""

import os
import sys
import time
from collections import deque

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_limit_maps import tail_caps               # noqa: E402
from explore_limit_column import SLACK, Window         # noqa: E402
from explore_shift_repair import greedy                # noqa: E402

LOOKCAP = 3                 # where no bound is proved (H2's and H4's cells)
N_CHECK = 1500
WINDOWS = [("golden [1]", (1,)), ("silver [2]", (2,)),
           ("bronze [3]", (3,)), ("sqrt3-1 [1,2]", (1, 2)),
           ("V1 (1,1,1,2)", (1, 1, 1, 2)), ("V2 (2,1,3,1)", (2, 1, 3, 1))]
GRID = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2), (3, 3)]
MAPS = ([("id", 1, 1, (0,))] + [("n+1", 1, 1, (1,))]
        + [("x%d" % m, 1, m, (0,)) for m in (2, 3, 4, 5)]
        + [("fl/%d" % m, m, 1, tuple(-e for e in range(m)))
           for m in (2, 3)])


class Game:
    """The residual game of m_o val(e) = m_i val(d) + c at lookahead c."""

    def __init__(self, win, mo, mi, cs, look, s, s0, rule=False):
        self.win, self.P = win, win.P
        self.mo, self.mi, self.cs = mo, mi, tuple(cs)
        self.look, self.s, self.s0, self.rule = look, s, s0, rule
        assert s0 <= s + 1, "the box is derived for s_0 <= s + 1"
        P, a = win.P, win.a
        self.a = a
        self.amax = max(a)
        cmax = max(abs(c) for c in cs)
        top = P + look + 3
        q = {-1: 0, 0: 1}
        p = {-1: 1, 0: 0}
        for k in range(1, top + 1):
            q[k] = a[(k - 1) % P] * q[k - 1] + q[k - 2]
            p[k] = a[(k - 1) % P] * p[k - 1] + p[k - 2]
        self.q, self.p = q, p
        self.thv = {k: (-p[k], q[k]) for k in range(-1, top + 1)}
        self.thf = {k: q[k] * win.alpha - p[k] for k in range(-1, top + 1)}
        self.thc = {k: q[k] * win.alpha_c - p[k] for k in range(-1, top + 1)}
        mmax = 2 * (mo * (1 + s) + mi) + cmax + 1
        self.mrange = range(-mmax, mmax + 1)
        # the box, per phase, on the pre-added carry (H3's bound widened)
        etac = abs(win.eta_c)
        Tc = sum(abs(self.thc[phi]) for phi in range(P))
        self.breal, self.bconj = {}, {}
        for phi in range(P):
            th = abs(self.thf[phi])
            self.breal[phi] = ((mo * (1 + s) + mi)
                               * (abs(self.thf[phi - 1]) + th) / th
                               * SLACK + 1)
            thc = abs(self.thc[phi])
            head = Tc / (etac - 1) + sum(abs(self.thc[psi])
                                         for psi in range(phi))
            window = sum(abs(self.thc[i]) for i in range(phi, phi + look + 1))
            self.bconj[phi] = (((mo * (self.amax + s) + mi * self.amax) * head
                                + mi * self.amax * window
                                + cmax * abs(win.alpha_c) + mmax) / thc
                               * SLACK + 1)
        self.lmax = P + 1
        self.build()

    # ------------------------------------------------------------ pieces
    def inbox(self, u, w, phi):
        win = self.win
        return (abs(win.real(u, w) / self.thf[phi]) <= self.breal[phi]
                and abs(win.conj(u, w) / self.thc[phi]) <= self.bconj[phi])

    def npos(self, pos):
        nxt = pos + 1
        return nxt if nxt <= self.lmax else nxt - self.P

    def cap_in(self, k):
        return self.a[0] - 1 if k == 0 else self.a[k % self.P]

    def cap_out(self, pos):
        if self.rule:
            return self.a[0] - 1 if pos == 0 else self.a[pos % self.P]
        return self.a[0] - 1 + self.s0 if pos == 0 else self.a[pos % self.P] + self.s

    def inputs(self, k, pzd):
        """Legal digits at input position k after a zero (pzd) or not."""
        cap = self.cap_in(k)
        xs = list(range(cap + 1))
        if k >= 1 and not pzd:
            xs = xs[:-1]
        return xs

    def add(self, branches, coef, vec, phi):
        """branches + coef * vec, pruned to the box at phase phi."""
        du, dw = coef * vec[0], coef * vec[1]
        out = set()
        for u, w in branches:
            u2, w2 = u + du, w + dw
            if self.inbox(u2, w2, phi):
                out.add((u2, w2))
        return out

    def pre_states(self):
        """Every legal pre-read d_0..d_look, as a game state at pos 0."""
        init = set((-m, -c) for m in self.mrange for c in self.cs)
        # the box at phase 0 is the frame of position 0 -- prune late
        frontier = [(init, True)]
        for k in range(self.look + 1):
            nxt = []
            for br, pzd in frontier:
                for x in self.inputs(k, pzd):
                    br2 = set((u - self.mi * x * self.thv[k][0],
                               w - self.mi * x * self.thv[k][1]) for u, w in br)
                    nxt.append((br2, x == 0))
            frontier = nxt
        out = set()
        for br, pzd in frontier:
            br = frozenset((u, w) for u, w in br if self.inbox(u, w, 0))
            out.add((0, br, pzd, True))
        return out

    def step(self, state, y):
        """The reader emits y at pos; every legal reply, as next states."""
        pos, br, pzd, pze = state
        P, phi = self.P, state[0] % self.P
        k_in = phi + self.look + 1          # absolute index in the frame
        br_y = self.add(br, self.mo * y, self.thv[phi], phi)
        wrap = (phi + 1 == P)
        nphi = (phi + 1) % P
        npos = self.npos(pos)
        out = []
        for x in self.inputs(pos + self.look + 1, pzd):
            br2 = set()
            for u, w in br_y:
                u2 = u - self.mi * x * self.thv[k_in][0]
                w2 = w - self.mi * x * self.thv[k_in][1]
                if wrap:
                    u2, w2 = self.win.apply_hinv(u2, w2)
                if self.inbox(u2, w2, nphi):
                    br2.add((u2, w2))
            out.append((x, (npos, frozenset(br2), x == 0, y == 0)))
        return out

    def outputs(self, state):
        pos, _br, _pzd, pze = state
        cap = self.cap_out(pos)
        ys = list(range(cap + 1))
        if self.rule and pos >= 1 and not pze:
            ys = ys[:-1]
        return ys

    def build(self):
        """States interned to ids; trans[id] = {y: [(x, id2), ...]}."""
        ids = {}
        states = []

        def intern(s):
            i = ids.get(s)
            if i is None:
                i = ids[s] = len(states)
                states.append(s)
            return i

        self.init = [intern(s) for s in self.pre_states()]
        todo = list(self.init)
        trans = {}
        while todo:
            i = todo.pop()
            s = states[i]
            moves = {}
            for y in self.outputs(s):
                succ = []
                for x, s2 in self.step(s, y):
                    j = ids.get(s2)
                    if j is None:
                        j = intern(s2)
                        todo.append(j)
                    succ.append((x, j))
                moves[y] = succ
            trans[i] = moves
        self.trans = trans
        self.states, self.ids = states, ids
        self.alive = [bool(s[1]) for s in states]
        self.holds0 = [(0, 0) in s[1] for s in states]
        self.n_states = len(states)
        self.solve()

    def solve(self):
        W = set(i for i in self.trans if self.alive[i])   # no branch: lost
        while True:
            # safety: some y keeps every reply in W
            changed = True
            while changed:
                changed = False
                for s in list(W):
                    ok = any(all(s2 in W for _x, s2 in succ)
                             for succ in self.trans[s].values())
                    if not ok:
                        W.discard(s)
                        changed = True
            # the flush: reach a (0, 0)-holding state under zero input
            Z = set(i for i in W if self.holds0[i])
            dist = {s: 0 for s in Z}
            dq = deque(Z)
            rev = {}
            for s in W:
                for y, succ in self.trans[s].items():
                    if all(s2 in W for _x, s2 in succ):
                        for x, s2 in succ:
                            if x == 0:
                                rev.setdefault(s2, []).append(s)
            while dq:
                s = dq.popleft()
                for s0 in rev.get(s, ()):
                    if s0 not in dist:
                        dist[s0] = dist[s] + 1
                        dq.append(s0)
            if len(dist) == len(W):
                break
            W = set(dist)
        self.W, self.dist = W, dist
        self.wins = all(s in W for s in self.init)

    # ------------------------------------------------------- the strategy
    def choose(self, s):
        best = None
        for y, succ in self.trans[s].items():
            if all(s2 in self.W for _x, s2 in succ):
                d0 = min(self.dist[s2] for x, s2 in succ if x == 0)
                if best is None or d0 < best[0]:
                    best = (d0, y)
        return best[1]

    def run(self, n, qs):
        """Read n through the winning strategy; the output digits."""
        d = greedy(n, qs[:24])
        T = len(d)
        d = d + [0] * (self.look + 1 + 4 * self.P + 8)
        init = set((-m, -c) for m in self.mrange for c in self.cs)
        br = init
        for k in range(self.look + 1):
            br = set((u - self.mi * d[k] * self.thv[k][0],
                      w - self.mi * d[k] * self.thv[k][1]) for u, w in br)
        s = (0, frozenset((u, w) for u, w in br if self.inbox(u, w, 0)),
             d[self.look] == 0, True)
        i = self.ids[s]
        out = []
        for t in range(T + 4 * self.P + 6):
            y = self.choose(i)
            out.append(y)
            x = d[t + self.look + 1]
            i = dict(self.trans[i][y])[x]
        return out, self.holds0[i]


def qs_for(caps, top):
    q = [1, caps[0]]
    for k in range(2, top + 1):
        q.append(caps[k - 1] * q[-1] + q[-2])
    return q


def check_strategy(g, caps, label):
    """C1b: the strategy's output on n < N_CHECK, value and caps."""
    qs = qs_for(caps, 46)
    bad = 0
    for n in range(N_CHECK):
        out, flushed = g.run(n, qs)
        val = sum(y * qs[k] for k, y in enumerate(out))
        okval = any(g.mo * val == g.mi * n + c for c in g.cs)
        okcap = all(y <= g.cap_out(k) for k, y in enumerate(out))
        if not (okval and okcap and flushed):
            bad += 1
            if bad <= 3:
                print("    BAD %s n=%d val=%d out=%s flushed=%s"
                      % (label, n, val, out[:12], flushed))
    return bad


def min_look(win, mo, mi, cs, s, s0, rule=False, top=LOOKCAP):
    for look in range(top + 1):
        g = Game(win, mo, mi, cs, look, s, s0, rule)
        if g.wins:
            return look, g
    return None, None


def h3_bound(win, m, s, s0):
    """P2's bound from H3: the smallest c meeting both inequalities.

    Read over ONE period plus a margin -- the ratios repeat with eta --
    and the tail sum closed by the geometric factor 1/(1 - |eta|): a
    float theta_k at depth 24 is cancellation garbage (q_k alpha - p_k
    with q_k ~ 1e9), which is where a first pass printed no bound.
    """
    a = win.a
    P = win.P
    q = {-1: 0, 0: 1}
    p = {-1: 1, 0: 0}
    top = 5 * P + 12
    for k in range(1, top + 1):
        q[k] = a[(k - 1) % P] * q[k - 1] + q[k - 2]
        p[k] = a[(k - 1) % P] * p[k - 1] + p[k - 2]
    th = {k: abs(q[k] * win.alpha - p[k]) for k in range(-1, top + 1)}
    excess = (s0 * win.alpha
              + s * sum(th[k] for k in range(1, P + 1)) / (1 - abs(win.eta)))
    for c in range(0, 2 * P + 8):
        ok = all(th[k + c - 1] / th[k] <= (1 + s) / (2 * m)
                 for k in range(1, 2 * P + 2))
        if ok and 2 * m * th[c] <= excess:
            return c
    return None


def digitwise_bound(win, m, s, s0):
    return 0 if (s >= (m - 1) * max(win.a)
                 and s0 >= (m - 1) * (win.a[0] - 1)) else None


def s0_controls():
    print("== s0  C1a: the LEGAL output (rule kept) through the game")
    bad = 0
    for name, period in WINDOWS:
        P = len(period)
        caps = tail_caps(period)
        win = Window(caps, P)
        row = []
        for label, mo, mi, cs in MAPS:
            if label in ("x4", "x5", "fl/3"):
                continue
            look, g = min_look(win, mo, mi, cs, 0, 0, rule=True)
            row.append("%s:%s" % (label, "-" if look is None else look))
            want = {"id": 0, "n+1": 1}.get(label)
            if want is not None and look != want:
                bad += 1
            if want is None and look is not None:
                bad += 1
            if g is not None:
                bad += check_strategy(g, caps, name + " " + label)
        print("  %-16s %s" % (name, "  ".join(row)))
    print("  C1a %s" % ("GREEN" if bad == 0 else "RED (%d)" % bad))
    return bad == 0


def s1_grid():
    print("== s1  the grid: minimal lookahead per (window, map, (s, s0))")
    print("       cells: " + "  ".join("(%d,%d)" % c for c in GRID))
    for name, period in WINDOWS:
        t0 = time.time()
        P = len(period)
        caps = tail_caps(period)
        win = Window(caps, P)
        print("  %s  a_1 = %d" % (name, caps[0]))
        nbad = 0
        for label, mo, mi, cs in MAPS:
            if label == "id":
                continue
            cells, bounds = [], []
            for s, s0 in GRID:
                hb = h3_bound(win, mi, s, s0) if label.startswith("x") else None
                top = LOOKCAP if hb is None else hb
                look, g = min_look(win, mo, mi, cs, s, s0, top=top)
                cells.append("-" if look is None else str(look))
                if g is not None:
                    nbad += check_strategy(g, caps, "%s %s (%d,%d)"
                                           % (name, label, s, s0))
                if label.startswith("x"):
                    db = digitwise_bound(win, mi, s, s0)
                    bounds.append("%s/%s" % ("-" if hb is None else hb,
                                             "-" if db is None else db))
            line = "    %-6s " + "  ".join("%5s" % c for c in cells)
            print(line % label)
            if bounds:
                print("           bounds H3/digitwise: " + "  ".join(
                    "%5s" % b for b in bounds))
        print("    strategy checks bad: %d   (%.0f s)" % (nbad, time.time() - t0))


if __name__ == "__main__":
    t0 = time.time()
    if s0_controls():
        s1_grid()
    else:
        print("controls red: nothing below is read")
    print("total %.0f s" % (time.time() - t0))
