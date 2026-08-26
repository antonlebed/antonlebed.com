"""Does x m have a bottom-up integer reader at bounded lookahead at EVERY
irrational window whose partial quotients are bounded? The residual game
in frame coordinates with the OPPONENT CHOOSING THE QUOTIENTS -- the
universal game -- solved over an alphabet {1, ..., A}, and its winning
strategy run as a window-oblivious reader at random windows.

THE QUESTION
------------
With a redundant output alphabet (caps a_{k+1} + s, position 0 at
a_1 - 1 + s_0, the below-a-cap rule dropped; input greedy) the
completion's reader exists at lookahead O(log(2m/(1+s))) at every
irrational window (explore_redundant_ostrowski.py H3), and the INTEGER
reader -- which must flush -- is read exactly only where the residual
game's state space is finite, the periodic windows (H3'): twelve of
them so far, every one at or under the completion bound. Whether the
integer reader exists at a general irrational window is open. This rig
asks it for the class of windows with quotients <= A at once.

THE HAND-ATTACK (on paper, before the engine)
---------------------------------------------
U1  THE FRAME. The residual R_t = m sum_{k<=t} d_k q_k - sum_{k<t} e_k
    q_k is x q_t + y q_{t-1} with integers (x, y). The pre-read digits
    d_{t+1..t+c} stay SEPARATE in the state (folded in, they put
    m q_{t+c+1}/q_t into x), with the quotients a_{t+1..t+c+1} that cap
    d_t..d_{t+c} and the flag [d_{t+c} = 0]. The reader emits e <=
    a_{t+1} + s (position 0: a_1 - 1 + s_0); the opponent then reveals
    a_{t+c+2} and d_{t+c+1} <= a_{t+c+2}, the cap only over a zero.
    With q_{t+1} = a_{t+1} q_t + q_{t-1}:
        R_{t+1} = X q_{t+1} + Y q_t,  X = y + m d_{t+1},
                                       Y = x - e - a_{t+1} y.
    The frame pair is the lattice point (R, P): it fixes the integer M
    between the two real stars (the parent's D8), and R = 0 flushes at
    ANY M in range -- (x, y) and (x + k q_{t-1}, y - k q_t) carry one R
    and stars k apart -- so the state carries the SET of alive
    M-branches exactly as the parent's game does, seeded at position 0
    by (m d_0, -k) over |k| <= 2m + 2 (D8's bound on M), each branch
    moved by the same map,
    the wrong ones leaving the box as their kernel offsets grow, and
    the flush is (0, 0) in the set. (A first cut kept ONE branch and
    lost golden x 3 at n = 1, whose coding needs M = 1.) So the
    residual game at ANY window is a game on one finite set of frame
    states whose transition is labelled by the local quotient; a period
    makes it stationary, a bounded alphabet makes it a FINITE game with
    the opponent choosing the quotient at each step.
U2  THE TRUNCATION IS SOUND ONE WAY. A branch with |x| > B_x or |y| >
    B_y is pruned, a state with no branch left is LOST. A reader that wins the truncated game wins
    the real one at every window over the alphabet, its strategy never
    leaving the box; a LOSS is inconclusive (the box may have cut a
    winning state, and an adaptive opponent is stronger than any fixed
    window). The positive direction is what is wanted, so no box is
    derived: a win is CERTIFIED by extracting the strategy and running
    it, as a reader that sees only the quotients through a_{t+c+1}, on every
    n < N_CHECK at random windows over the alphabet -- value, caps and
    flush checked directly. THE NECESSARY BOX, for reading a loss: the
    full residual R_t + m(pre-read) + m(future) is codable from t, so
    its star lies in the level-t range, |star| <= (1 + s)|theta_{t-1}|,
    and sigma_t (the star of R_t alone) is within m A sum_{k>t}
    |theta_k| < 2mA |theta_t| of it; R_t itself lies in (-m q_{t+c+1},
    m q_{t+1}). In the unimodular frame x = +-(R theta_{t-1} - sigma
    q_{t-1}), y = +-(sigma q_t - R theta_t), which gives |y| <= (1 + s)
    + 2mA + m (A + 1)^c and |x| <= (1 + s) + 2mA + m (A + 1)^{c+1}:
    a loss inside THIS box is a loss of the universal game; a loss
    inside a smaller one is not readable. (For x 3 over {1, 2} at c = 2
    the necessary box is |x| <= 95, |y| <= 41.)
U3  THE FLUSH IS A TWO-PLAYER REACHABILITY. Under zero input the
    opponent still chooses quotients, so the reader must FORCE a state
    holding the branch (0, 0) with the pre-read tuple zero: the attractor Z_{i+1} = Z_i
    + {s : some e has every quotient reply in Z_i}, alternated with
    safety to a fixed point, where the parent's flush was one-player.
U4  WHAT A WIN SAYS. Reader wins at lookahead c over {1, ..., A} =>
    at every irrational window with partial quotients <= A, x m at
    slack (s, s_0) has an integer reader at lookahead c. The index
    convention is the parent's: e_t is a function of d_0..d_{t+c}.
TRANSPLANT, marked: the twelve periodic windows' lookahead 2 for x 2
and x 3 at slack 1 is a reading at STATIONARY games; the universal
opponent switches quotients at will, and nothing read so far says the
switch costs nothing.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS).
Alphabets {1}, {2}, {3}, {1, 2}, {1, 2, 3}; maps x 2 and x 3; slacks
(1, 1) and (2, 2); lookahead searched to LOOKCAP; box B_x = BOX (m + s)
(A + 1), B_y = BOX (m + s) + 3 with BOX = 3 unless a cell's state space
outgrows memwatch's ceiling, where BOX is lowered (a smaller box can
only lose cells, never win them falsely), and the state count printed
per cell.
  C1 (controls, run FIRST; nothing below is read if any is red)
      (a) the singleton alphabets reproduce the parent's F3 cells --
      {1} golden, {2} silver, {3} bronze -- at both slacks, both maps;
      (b) every winning cell's strategy, run on n < N_CHECK at every
      one of N_WIN random windows over the alphabet and at the
      alphabet's periodic windows of period <= 2, prints the right
      value under the caps and flushes, 0 bad.
  P1  {1, 2}: x 2 at (1, 1) WINS at lookahead 2 (the twelve windows'
      reading, if the switch costs nothing) -- a print of 2. A print
      of 3 or 4 says the switch costs lookahead; "-" at LOOKCAP is
      inconclusive by U2 and is read as such.
  P2  {1, 2, 3}: the same cell, the same three readings.
  P3  x 3 at (1, 1), and both maps at (2, 2): read unasked; (2, 2) at
      alphabet {1, 2} for x 2 is digitwise (s >= (m - 1) A) and must
      print 0.
  P4  the state count against the box: a cell whose winning strategy
      touches the box boundary is reported (the strategy's maximal
      |x| and |y| printed beside the win).

THE DESIGN
----------
Stages: s0 the singleton controls (C1a); s1 the alphabets with the
strategy certification (C1b) at every winning cell; s2 the periodic
witness hunt -- the parent's stationary game at every primitive
{1, 2}-necklace of period <= NECK_MAX for x 3 at (1, 1), printing any
window whose lookahead is not 2 (a universal reading above every
periodic one either has a periodic witness or has none short). LOOKCAP
= 3 by default; N_CHECK = 1000; N_WIN = 12 random windows of 60
quotients (seeded).
The alphabets, maps, cells and cap come from the environment
(UNIV_ALPHABETS, UNIV_MAPS, UNIV_CELLS, UNIV_LOOKCAP, UNIV_BOX,
NECK_MAX) so the rehearsal at {1}, {1, 2} and lookahead <= 2 exercises
every stage first and each heavy cell runs as its own process; the
defaults are the run that fits under memwatch's ceiling in one go.
Memory: the reachable state space is built explicitly; run under
memwatch.py.

FINDINGS (entered post-run; every number below sits in this file's
printed output. Runs: the default -- alphabets {1}, {2}, {3}, {1, 2},
LOOKCAP 3, BOX 2, NECK_MAX 8 -- 27 s, peak 352 MB; the {1, 2, 3} cells
one process each: x 2 (1, 1) at BOX 2 in 7 s, 382 MB, and at BOX 1.5 in
4 s, 228 MB; x 2 (2, 2) at BOX 1.5 in 11 s, 500 MB; x 3 at either slack
KILLED by memwatch at 514 MB at BOX 1.5. The x 3 (1, 1) cell over
{1, 2} at c = 2 was also run at BOX 3 (119k states) and BOX 6 (395k
states, 511 MB); the necklace hunt was also run to period 10 in a
scratch copy of s2, 25 s.)

F1  THE CONTROLS HOLD. C1a: all twelve singleton cells print the
    parent's F3 lookahead, at BOX 2 and at BOX 3. C1b: every winning
    cell in every run certified 0 bad -- the extracted reader, seeing
    only the quotients through a_{t+c+1}, produced the right value under the
    caps and flushed on every n < 1000 at the constant windows, the two
    alternating ones and twelve random 60-quotient windows.
F2  x 2 AT SLACK (1, 1) READS AT 2 OVER {1, 2} AND OVER {1, 2, 3}
    (P1, P2: the first shape). 34,641 states at BOX 2 over {1, 2}
    (61,315 at BOX 3); 323,136 over {1, 2, 3} at BOX 2 (187,110 at
    1.5). So at EVERY irrational window whose partial quotients are at
    most 3, x 2 with one unit of slack has an integer reader at
    lookahead 2 that reads the quotients through a_{t+3} (the state at
    emission holds a_{t+1}..a_{t+c+1}: c + 1 past its position, not
    c + 2 as first recorded) and nothing else of the window -- the
    twelve periodic windows' 2 is the class's.
F3  THE OTHER CELLS (P3). x 2 at (2, 2): 0 over {1, 2} (digitwise, as
    predicted) and 2 over {1, 2, 3} (373,005 states). x 3 at (2, 2):
    2 over {1, 2} (102,313 states); over {1, 2, 3} unread (memory).
F4  x 3 AT (1, 1) OVER {1, 2} READS AT 3, ONE ABOVE EVERY PERIODIC
    WINDOW -- AND THE 2 IS UNDECIDED. The win at 3: 268,863 states at
    BOX 2, 176,267 at 1.5, certified. The loss at 2 stands at BOX 1.5,
    2, 3 and 6 (|y| <= 27 at most), every one INSIDE the necessary box
    of U2 (|x| <= 95, |y| <= 41), so by U2 it reads nothing; and it
    has the truncation's signature -- at BOX 3 the winning set is
    EMPTY, all 31,546 dead states would keep a branch at a 10x box,
    and the opponent's tree from the losing start plays quotient 1 and
    digit 0 along every branch to depth 13 (the safety fixed point
    collapsing under the pruning, not a flush failing). Whether the
    quotient switch costs x 3 a unit of lookahead is OPEN: a decision
    at 2 needs the necessary box, which this encoding does not fit
    under 512 MB (BOX 6 sat at 511).
F5  NO SHORT PERIODIC WITNESS (s2). All 71 primitive {1, 2}-necklaces
    of period <= 8 -- 226 through period 10 in the scratch run -- read
    x 3 at (1, 1) at lookahead 2. If the universal 3 is tight, its
    witness is aperiodic or of period above 10.
P4 read: the printed "touched" |y| equals B_y at every cell, because
    the wrong-M branches run to the pruning edge before they leave; it
    reads the box, not the strategy, and is kept only as the check
    that the certified reader stayed inside.
"""

import os
import random
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

LOOKCAP = int(os.environ.get("UNIV_LOOKCAP", "3"))
BOX = float(os.environ.get("UNIV_BOX", "2"))      # the box multiplier (U2)
NECK_MAX = int(os.environ.get("NECK_MAX", "8"))
N_CHECK = 1000
N_WIN = 12
CELLS = [tuple(int(x) for x in c.split(","))
         for c in os.environ.get("UNIV_CELLS", "1,1;2,2").split(";")]
MAPS = [int(x) for x in os.environ.get("UNIV_MAPS", "2,3").split(",")]
ALPHABETS = [tuple(int(x) for x in grp.split(","))
             for grp in os.environ.get("UNIV_ALPHABETS",
                                       "1;2;3;1,2").split(";")]
# the parent's F3 cells at the singleton alphabets: (A, m) -> {(s, s0): c}
PARENT = {
    (1, 2): {(1, 1): 0, (2, 2): 0}, (1, 3): {(1, 1): 2, (2, 2): 0},
    (2, 2): {(1, 1): 2, (2, 2): 0}, (2, 3): {(1, 1): 2, (2, 2): 2},
    (3, 2): {(1, 1): 2, (2, 2): 2}, (3, 3): {(1, 1): 2, (2, 2): 2},
}


class Universal:
    """The residual game of x m at lookahead c, the opponent choosing
    quotients from `alph`, in frame coordinates (U1)."""

    def __init__(self, alph, m, s, s0, look):
        self.alph, self.m, self.s, self.s0, self.look = tuple(alph), m, s, s0, look
        A = max(alph)
        self.bx = int(BOX * (m + s) * (A + 1))
        self.by = int(BOX * (m + s)) + 3
        self.K = 2 * self.by + 1              # a branch (x, y) is packed as an int
        self.build()

    def pack(self, x, y):
        return (x + self.bx) * self.K + (y + self.by)

    def unpack(self, v):
        x, y = divmod(v, self.K)
        return x - self.bx, y - self.by

    # a state: (branches, quots, digs, lastzero, pos0)
    #   branches = sorted tuple of packed (x, y), one per alive M;
    #   quots = (a_{t+1}, ..., a_{t+c+1}); digs = (d_{t+1}, ..., d_{t+c})
    def cap_out(self, st):
        a1 = st[1][0]
        return a1 - 1 + self.s0 if st[4] else a1 + self.s

    def replies(self, st):
        lastzero = st[3]
        for a_new in self.alph:
            top = a_new if lastzero else a_new - 1
            for d_new in range(top + 1):
                yield a_new, d_new

    def succ(self, st, e, a_new, d_new):
        br, quots, digs, _lz, _p0 = st
        seq = digs + (d_new,)
        d1, digs2 = seq[0], seq[1:]
        a1 = quots[0]
        out = []
        bx, by, K = self.bx, self.by, self.K
        for v in br:
            x, y = divmod(v, K)
            x -= bx
            y -= by
            X = y + self.m * d1
            Y = x - e - a1 * y
            if -bx <= X <= bx and -by <= Y <= by:
                out.append((X + bx) * K + (Y + by))
        if not out:
            return None
        out.sort()
        return (tuple(out), quots[1:] + (a_new,), digs2, d_new == 0, False)

    def seed(self, d0):
        M = 2 * self.m + 2                    # D8: |M| <= m_o + 2 m_i + 1
        return tuple(sorted(self.pack(self.m * d0, -k) for k in range(-M, M + 1)))

    def holds0(self, st):
        return self.pack(0, 0) in st[0]

    def initial(self):
        """Every legal pre-read (d_0..d_c) with quotients a_1..a_{c+1}."""
        out = []
        c = self.look

        def rec(quots, digs, lastzero):
            if len(quots) == c + 1:
                out.append((self.seed(digs[0]), quots, digs[1:], lastzero, True))
                return
            k = len(quots)
            for a in self.alph:
                top = (a - 1) if k == 0 else (a if lastzero else a - 1)
                for d in range(top + 1):
                    rec(quots + (a,), digs + (d,), d == 0)
        rec((), (), True)
        return out

    def build(self):
        ids, states = {}, []

        def intern(st):
            i = ids.get(st)
            if i is None:
                i = ids[st] = len(states)
                states.append(st)
            return i

        self.init = [intern(st) for st in self.initial()]
        todo = list(self.init)
        trans = {}
        while todo:
            i = todo.pop()
            st = states[i]
            moves = {}
            for e in range(self.cap_out(st) + 1):
                zs, nz = [], []
                dead = False
                for a_new, d_new in self.replies(st):
                    st2 = self.succ(st, e, a_new, d_new)
                    if st2 is None:
                        dead = True
                        break
                    j = ids.get(st2)
                    if j is None:
                        j = intern(st2)
                        todo.append(j)
                    (zs if d_new == 0 else nz).append(j)
                if not dead:
                    moves[e] = (len(zs), tuple(zs + nz))   # zero replies first
            trans[i] = moves
        self.trans, self.states, self.ids = trans, states, ids
        self.n_states = len(states)
        self.solve()

    def solve(self):
        W = set(self.trans)
        zero = set(i for i, st in enumerate(self.states)
                   if self.holds0(st) and not any(st[2]))
        while True:
            changed = True
            while changed:
                changed = False
                for s_ in list(W):
                    ok = any(all(j in W for j in ids_)
                             for _nz, ids_ in self.trans[s_].values())
                    if not ok:
                        W.discard(s_)
                        changed = True
            # the flush (U3): force the zero state under zero input
            Z = set(i for i in zero if i in W)
            dist = {i: 0 for i in Z}
            frontier = True
            while frontier:
                frontier = False
                for s_ in W:
                    if s_ in dist:
                        continue
                    best = None
                    for e, (nz, ids_) in self.trans[s_].items():
                        if not all(j in W for j in ids_):
                            continue
                        zs = ids_[:nz]
                        if zs and all(j in dist for j in zs):
                            m_ = 1 + max(dist[j] for j in zs)
                            if best is None or m_ < best:
                                best = m_
                    if best is not None:
                        dist[s_] = best
                        frontier = True
            if len(dist) == len(W):
                break
            W = set(dist)
        self.W, self.dist = W, dist
        self.wins = all(i in W for i in self.init)

    # ------------------------------------------------------- the reader
    def choose(self, i):
        best = None
        for e, (nz, ids_) in self.trans[i].items():
            if all(j in self.W for j in ids_):
                d0 = max(self.dist[j] for j in ids_[:nz])
                if best is None or d0 < best[0]:
                    best = (d0, e)
        return best[1]

    def read(self, digits, quots):
        """Run the reader on a greedy string at a window given by its
        quotients (a_1, a_2, ...): the output digits, the final state,
        and the largest |x|, |y| seen."""
        c = self.look
        T = len(digits)
        d = list(digits) + [0] * (c + 8)
        st = (self.seed(d[0]), tuple(quots[:c + 1]), tuple(d[1:c + 1]),
              d[c] == 0, True)
        i = self.ids[st]
        out, mx, my = [], 0, 0
        for t in range(T + 6):
            e = self.choose(i)
            out.append(e)
            a_new, d_new = quots[t + c + 1], d[t + c + 1]
            st2 = self.succ(self.states[i], e, a_new, d_new)
            i = self.ids[st2]
            for v in st2[0]:
                x, y = self.unpack(v)
                mx, my = max(mx, abs(x)), max(my, abs(y))
        st = self.states[i]
        return out, self.holds0(st), mx, my


def convergents(quots, top):
    q = [1, quots[0]]
    for k in range(2, top + 1):
        q.append(quots[k - 1] * q[-1] + q[-2])
    return q


def greedy(n, q):
    d = [0] * len(q)
    r = n
    for k in range(len(q) - 1, -1, -1):
        d[k], r = divmod(r, q[k])
    top = max((k for k in range(len(q)) if d[k]), default=-1)
    return d[:top + 1]


def certify(g, alph, label, seed=0):
    """C1b: the strategy at random windows and the short periodic ones."""
    rng = random.Random(seed)
    windows = [[a] * 60 for a in alph]
    if len(alph) > 1:
        windows += [[alph[i % 2] for i in range(60)],
                    [alph[(i + 1) % 2] for i in range(60)]]
    windows += [[rng.choice(alph) for _ in range(60)] for _ in range(N_WIN)]
    bad, mx, my = 0, 0, 0
    for quots in windows:
        q = convergents(quots, 40)
        for n in range(N_CHECK):
            digs = greedy(n, q)
            out, flushed, x_, y_ = g.read(digs, quots)
            mx, my = max(mx, x_), max(my, y_)
            val = sum(e * q[k] for k, e in enumerate(out))
            caps = [quots[0] - 1 + g.s0] + [quots[k] + g.s
                                            for k in range(1, len(out))]
            if not (val == g.m * n and flushed
                    and all(e <= cp for e, cp in zip(out, caps))):
                bad += 1
                if bad <= 3:
                    print("    BAD %s n=%d val=%d out=%s flushed=%s"
                          % (label, n, val, out[:12], flushed))
    return bad, mx, my


def min_look(alph, m, s, s0):
    for look in range(LOOKCAP + 1):
        g = Universal(alph, m, s, s0, look)
        if g.wins:
            return look, g
    return None, g


def run_cell(alph, m, s, s0):
    label = "{%s} x%d (%d,%d)" % (",".join(map(str, alph)), m, s, s0)
    t0 = time.time()
    look, g = min_look(alph, m, s, s0)
    if look is None:
        print("  %-22s -   (states %d at c=%d, %.0f s)"
              % (label, g.n_states, LOOKCAP, time.time() - t0))
        return None, 0
    bad, mx, my = certify(g, alph, label)
    print("  %-22s %d   states %d  box (%d,%d) touched (%d,%d)  bad %d  (%.0f s)"
          % (label, look, g.n_states, g.bx, g.by, mx, my, bad,
             time.time() - t0))
    return look, bad


def s0_controls():
    print("== s0  C1a: the singleton alphabets reproduce the parent")
    red = 0
    for alph in ALPHABETS:
        if len(alph) != 1:
            continue
        for m in MAPS:
            for s, s0 in CELLS:
                look, bad = run_cell(alph, m, s, s0)
                want = PARENT[(alph[0], m)][(s, s0)]
                if look != want or bad:
                    red += 1
                    print("    RED: parent %s" % want)
    print("  C1a %s" % ("GREEN" if red == 0 else "RED (%d)" % red))
    return red == 0


def s1_alphabets():
    print("== s1  the alphabets: minimal lookahead of the universal game")
    for alph in ALPHABETS:
        if len(alph) == 1:
            continue
        for m in MAPS:
            for s, s0 in CELLS:
                run_cell(alph, m, s, s0)


def s2_necklaces():
    """The periodic witness hunt: every primitive {1, 2}-necklace of
    period <= NECK_MAX through the parent's stationary game, x 3 at
    (1, 1); a window reading anything but 2 is printed."""
    import itertools
    from explore_limit_maps import tail_caps
    from explore_limit_column import Window
    from explore_redundant_ostrowski import Game
    print("== s2  periodic witness hunt, x3 (1,1) over {1,2}-necklaces,"
          " period <= %d" % NECK_MAX)
    hits, count = [], 0
    t0 = time.time()
    for P in range(1, NECK_MAX + 1):
        for w in itertools.product((1, 2), repeat=P):
            if min(w[i:] + w[:i] for i in range(P)) != w:
                continue
            if any(w == w[:d] * (P // d) for d in range(1, P) if P % d == 0):
                continue
            count += 1
            win = Window(tail_caps(w), P)
            look = None
            for c in range(4):
                if Game(win, 1, 3, (0,), c, 1, 1).wins:
                    look = c
                    break
            if look != 2:
                hits.append((w, look))
                print("  HIT %s lookahead %s" % (w, look))
    print("  %d primitive necklaces, %d not at lookahead 2   (%.0f s)"
          % (count, len(hits), time.time() - t0))


if __name__ == "__main__":
    t0 = time.time()
    print("alphabets %s  LOOKCAP %d  BOX %s" % (ALPHABETS, LOOKCAP, BOX))
    if s0_controls():
        s1_alphabets()
        s2_necklaces()
    else:
        print("controls red: nothing below is read")
    print("total %.0f s" % (time.time() - t0))
