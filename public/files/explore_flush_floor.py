"""Why is 1 the one lookahead the flush never allows? The flushed state
is the exposed one, and a late digit at the cap needs TWO levels below
itself -- read inside the parent's own game at every decided cell.

THE QUESTION
------------
explore_flush_price.py F5(a): the integer reader reads at lookahead 1 at
NONE of 130 cells while the safety reader reads at 1 at 35 of them and
at 0 at two more, and at every one of those 37 the integer reader reads
2. Its s3 opened the two cells pricing 2 and found the terminal
condition ANNIHILATING a safety fixpoint holding the initial states
rather than trimming it -- at lookahead 0 and at lookahead 1 both,
while the safety fixpoint grows between them. So the number to explain
is a floor, not a landing point, and the question is WHY the flush
forbids exactly 1.

THE HAND-ATTACK (on paper, before the engine)
---------------------------------------------
H1  THE INDEX CONVENTION, RE-DERIVED FROM THE ENGINE. Game.step emits y
    at pos and then reads input index pos + look + 1; pre_states
    consumes d_0..d_look before position 0; cap_in(k) is a_1 - 1 at
    k = 0 and a_{k+1} otherwise, at the cap only over a zero;
    cap_out(k) is a_1 - 1 + s_0 at 0 and a_{k+1} + s otherwise;
    q_k = a_k q_{k-1} + q_{k-2} with q_{-1} = 0, q_0 = 1 (so q_1 = a_1).
    A reader at lookahead c emits e_t having seen d_0..d_{t+c}, and
    d_{t+c+1} is revealed AFTER e_t is written.
H2  THE FLUSHED STATE IS THE EXPOSED ONE. A reader correct on every
    integer writes, for the input n, a finite output: from some
    position t_0 on its residual is 0 and it emits zeros. Let k be
    large, with d_{k-1} = 0, and put n' = n + a_{k+1} q_k -- legal,
    the digit at index k being at its cap over a zero. The reader's
    outputs on n and n' agree through position k - c - 1 (it has seen
    the same digits), so on n' its residual at position k - c is
    exactly m a_{k+1} q_k, and that integer must be a capped string
    from level k - c: e_{k-c}, e_{k-c+1}, ... with 0 <= e_j <= a_{j+1}
    + s. Nothing below level k - c is available: those digits are
    written. The star is no extra condition here: for large k the level
    range has width under 1 and two stars of one integer differ by an
    integer, so an integer coding with its star in range is the lift
    the game holds.
H3  FROM LEVEL k - 1 THE VALUE N q_k HAS ONE CAPPED STRING, e_k = N.
    Write q_{k+j} = A_j q_k + B_j q_{k-1} for j >= 1; then A_j, B_j >= 0
    and B_j >= 1 (B_1 = 1, B_2 = a_{k+2}, B_{j} = a_{k+j} B_{j-1} +
    B_{j-2}). A capped string from level k - 1 with value N q_k has
    N q_k = X q_k + Y q_{k-1}, X = e_k + sum e_{k+j} A_j and Y = e_{k-1}
    + sum e_{k+j} B_j, so q_k divides Y (gcd(q_k, q_{k-1}) = 1); Y >= q_k
    would force N >= q_{k-1}, impossible once q_{k-1} > N, so Y = 0,
    every e_{k+j} and e_{k-1} vanish, and e_k = N. With N = m a_{k+1}
    the cap a_{k+1} + s is exceeded iff s < (m - 1) a_{k+1}. THEREFORE:
    at lookahead c <= 1 the reader writes from level k - c >= k - 1,
    and if (m - 1) a_{k+1} > s holds at infinitely many k (at a
    periodic window: s < (m - 1) a_max) with q_{k-1} > m a_{k+1} (free
    under bounded quotients), no integer reader exists at lookahead 0
    or 1. The flush costs a floor of 2 below the digitwise line, and
    the whole of the cost is that a late digit's overflow spills into
    the two levels below it, q_k = a_k q_{k-1} + q_{k-2}, and a reader
    that has flushed has written both.
H4  IN THE GAME'S OWN TERMS this is: at lookahead <= 1 every state
    holding the branch (0, 0) is doomed -- under zero input its play
    is forced (a positive digit makes the integer residual negative,
    and with the input staying zero a negative residual never returns
    to 0, so the flush is lost from there) and the adversary waits for
    the phase with
    (m - 1) a_{k+1} > s -- so the flush refinement's target set Z is
    empty in the final fixpoint and W with it. That is the
    ANNIHILATION s3 of the parent printed at two cells, and it should
    print at every non-digitwise cell of the 130, not just those two.
H5  THE OTHER HALF OF THE LINE, AND A CORNER THE GRID NEVER VISITED.
    The digitwise reader (explore_redundant_ostrowski.py) needs
    s >= (m - 1) a_max and s_0 >= (m - 1)(a_1 - 1). The second half is
    SUPERFLUOUS: at position 0 the overflow spills UP, q_1 = a_1, so
    e_0 = m d_0 mod a_1 <= a_1 - 1 fits under any s_0 and the carry
    floor(m d_0 / a_1) <= m - 1 lands on e_1 = m d_1 + carry. If
    d_0 = 0 there is no carry; if d_0 >= 1 the greedy rule caps d_1 at
    a_2 - 1, so e_1 <= m a_2 - 1 <= a_2 + (m - 1) a_max - 1 = cap. Both
    are functions of d_0, d_1 at positions 0, 1: lookahead 0. So c_int
    should read 0 at (s, s_0) = ((m - 1) a_max, 0) at every window with
    a_1 >= 2 -- cells no rig has run -- and with H3 the rule is
    complete: at every periodic window c_int = 0 iff s >= (m - 1) a_max
    and c_int >= 2 otherwise; 1 is never the answer.
H6  THE FLOOR AS A BOUND PER CELL, AND WHAT IT CANNOT SEE. H2 gives
    more than 2: for c >= 2 the same argument demands m x q_k codable
    from level k - c for every legal late digit x, and more generally
    m val(tau) for every legal tail tau starting at index k after a
    zero. So L1 = max over (phase, x) of the least l with m x q_k
    codable from k - l, and L* the same over tails to a bounded
    length, are LOWER bounds on c_int; so is c_saf (dropping a
    condition cannot raise a minimum). c_int >= max(c_saf, L*) is
    forced; where equality fails, a third obstruction -- a nonzero
    residual the reader must carry into a late digit -- binds, and
    this rig does not name it.
H7  WHERE IT CAN BLOW UP. The codability decision is a memoized
    recursion on (value, level) that terminates because q_j > value
    ends it. It is run in TRUE indices at a DEEP k of the phase, and
    "deep" is a size condition and not a period count: H3's argument
    needs q_{k-1} > N, and a first draft's k = 3P + phase put golden's
    k at 3 with q_2 = 2 under N = 4, where 4 q_3 = 12 = 3 q_2 + 2 q_3 IS
    a capped string from level 2 -- a small-index accident, printed as
    L1 = 1 at golden x4 (2, 2) against H3's own 2. So k is the least
    index of its phase with q_{k-LCAP-1} > 10^4, and every bound is
    recomputed at k + P and must agree (a control, C1e). The Game
    builds are the parent's and are run under memwatch; the corner
    cells at H5 stop at the first winning lookahead.
TRANSPLANT, marked: the game, its box, its grid, the band cells and the
frozen c_int/c_saf are explore_redundant_ostrowski.py's,
explore_lookahead_band.py's and explore_flush_price.py's. Nothing here
re-derives them.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS,
never what they would mean).
  C1 (controls, run FIRST; nothing below is read if any leg is red)
     (a) THE CODABILITY DECIDER AGAINST BRUTE FORCE: at every window,
         for levels j = 1..P+2 and every value under a bound, codable(V,
         j) agrees with an explicit enumeration of capped strings.
     (b) L1 = L* = 0 AT EVERY DIGITWISE CELL of the 130 (H5's s half:
         nothing overflows).
     (c) c_int >= L* AND c_int >= c_saf AT EVERY CELL where c_int is
         finite (H6; a violation is a fault of the derivation, not a
         finding).
     (e) L1 AND L* AGREE BETWEEN k AND k + P at every cell (H7: the
         bound is a fact about the phase and not about an index).
  P1 THE ANNIHILATION IS GENERAL (H4). At every one of the 130 cells,
     at lookahead 0 and 1, the rig prints the size of Game's final W and
     the count of (0, 0)-holding states inside it. Prediction: at every
     cell with s < (m - 1) a_max both are ZERO at both lookaheads; at
     the digitwise cells the count is positive at lookahead 0.
     KILL: a non-digitwise cell with a (0, 0)-holder inside W at
     lookahead <= 1.
  P2 THE WITNESS INSIDE THE GAME, at the two price-2 cells and one grid
     cell with c_saf = 1: from EVERY (0, 0)-holding safe state at
     lookahead 1, zero input is walked past the frame's first wrap
     (the first period is where position 0's cap and the small
     convergents live) and on to the phase with the largest
     (m - 1) a_{k+1} - s, the digit a_{k+1} is played, and the rig
     prints how many of those walks end in a state with no zero-input
     path inside the SAFETY fixpoint to any (0, 0)-holder -- predicted
     all -- beside the decider's verdict on m a_{k+1} q_k from level
     k - 1 (uncodable) and the least level it is codable from.
  P3 THE BOUND (H6): per cell L1, L*, c_saf, c_int; the tally of
     c_int - max(c_saf, L*) over the 130 cells, and the tally of
     c_int - L* alone. Not predicted: how often equality holds.
  P4 THE CORNER (H5): c_int at (s, s_0) = ((m - 1) a_max, 0) for x2
     and x3 at silver, bronze and V2 (the windows with a_1 >= 2).
     Prediction: 0 at all six. KILL: any nonzero print. A printed 1
     would be the corpus's first cell at 1 and confines H3's rule to
     s < (m - 1) a_max; a printed 2 kills H5 alone.
  P5 wall-clock and state counts printed; peak under memwatch in the
     run record.

THE DESIGN
----------
Stages: s0 the C1 controls, s1 the P1 annihilation sweep, s2 the P2
witness walk, s3 the P3 bound table, s4 the P4 corner. Stage selection
from the environment (FLOOR_STAGES). The codability decider, the
lower bounds and the corner's digitwise construction are this file's;
every game is the parent's Game, and c_int/c_saf come through
explore_flush_price.price so the numbers are the parent's own calls.

FINDINGS (entered post-run; every number below sits in this file's
printed output. Runs under memwatch at the 512 MB default, peaks as
WORKING SET: s0 with s2 in 268 s at 69.2 MB, the brute-force leg being
the whole of the time; s1 in 8 s at 83.4 MB; s3 in 61 s at 349.1 MB,
the band cells built to LOOKCAP; s4 in 1 s at 26.7 MB. Nothing ran
bare and nothing was killed. One rig fault fixed between the first and
the second s3 run, recorded at H7: the deep index.)

F1  THE CONTROLS HOLD (C1a, C1b, C1c and C1e, 0 bad each). The decider agrees with
    an explicit enumeration at every window, level and value tested;
    L1 = L* = 0 at all 15 digitwise cells; the bounds read the same
    at k and k + P at all 130; and c_int >= max(c_saf, L*) at all 130.
F2  THE ANNIHILATION IS GENERAL (P1). At all 115 cells with
    s < (m - 1) a_max, Game's final W is EMPTY at lookahead 0 and at
    lookahead 1 -- not one (0, 0)-holder survives -- and at all 15
    digitwise cells W holds (0, 0)-holders at lookahead 0. So what s3
    of the parent printed at two cells is the rule's own shape at every
    non-digitwise cell of the 130: the terminal condition does not trim
    the safety fixpoint at lookahead <= 1, it empties it.
F3  THE WITNESS INSIDE THE GAME (P2). V1 (1,1,1,2) x3 (3,3): 703 safe
    states at lookahead 1, 20 of them holding (0, 0), none in W; every
    one of the 20, walked past the wrap and on to the phase with
    a = 2, then hit with the digit 2, lands in a state that is alive in
    the box and reaches no (0, 0)-holder under zero input inside the
    safety fixpoint. V2 (2,1,3,1) x3 (5,5): 1,157 safe, 18 holders, all
    18 the same after the digit 3. silver x2 (1,1): 104 safe, 7
    holders, all 7 after the digit 2. At all three the decider reads
    m a q_k uncodable from level k - 1 and codable from k - 2 (l = 2).
F4  THE BOUND IS THE READER'S LOOKAHEAD (P3). c_int = max(c_saf, L*)
    at ALL 130 cells: c_int = c_saf at 91 of them and c_int = L* at 94,
    both at 55;
    c_int - L* is 0 at 94, 1 at 30, 2 at 4 and 3 at 2. The tail bound
    exceeds the single-digit one at six cells, 4 against 2 at every one
    -- golden x4, sqrt3-1 x5, V1 x3 and V2 x4 at (0, 1), and V1 x5 at
    (1, 0) and (1, 1) -- and the last two are the parent's two cells
    landing on 4 from c_saf = 3: the exceptional landing point is the
    flushed-state bound, a late TAIL rather than a late digit. The two
    cells landing on 2 from c_saf = 0, V1 x3 (3,3) and V2 x3 (5,5),
    read L* = 2.
F5  THE CORNER (P4). c_int = 0 at all six cells (s, s_0) =
    ((m - 1) a_max, 0): silver x2 (2,0), x3 (4,0); bronze x2 (3,0),
    x3 (6,0); V2 x2 (3,0), x3 (6,0). The digitwise line's s_0 half is
    superfluous, as H5 derives.

TIER. H3 with H5 is a RULE, proved: at every periodic window and every
m >= 2, the integer reader's lookahead is 0 when s >= (m - 1) a_max
(any s_0) and at least 2 otherwise -- 1 is never the answer; the
argument is H2-H3 and H5, and the computation confirms it at 130 + 6
cells but is not what it rests on. Its hypothesis at a general
irrational window is stated in H3 and is free under bounded quotients.
F2 and F3 are exhaustive computations at the cells named. F4 is an
OBSERVATION at 130 cells: both sides are proved lower bounds and the
equality has no proof of sufficiency under it; L* is read over tails
to length P + 2, a truncation, and where c_int = L* > c_saf that
truncation is exact by F4 itself. (SETTLED since, explore_flush_law.py:
L* is computed with no tail length in it, by the subset automaton of
the game -- the reader shown the whole input, from a flushed state --
and the truncation agrees with it at 128 of the 130 cells, reading 2
for 4 at golden x3 (0,1) and sqrt3-1 x4 (0,1), both under c_saf = 5;
F4's equality and its counts stand, and stand at 153 cells since.)
F5 is six cells confirming a derivation.
"""

import os
import sys
import time
from collections import deque
from functools import lru_cache

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_redundant_ostrowski import (               # noqa: E402
    GRID, LOOKCAP, WINDOWS, Game, digitwise_bound)
from explore_flush_price import (                       # noqa: E402
    BAND, price, window_of, safety_wins)

STAGES = os.environ.get("FLOOR_STAGES", "s0,s1,s2,s3,s4").split(",")
LCAP = 8            # the deepest level-drop the bound is searched to
TAILLEN = None      # tails to P + 2 digits (set per window)


# --------------------------------------------------- the numeration
class Caps:
    """True-index caps and convergents of one (window, s, s_0) cell."""

    def __init__(self, period, s, s0, top=None):
        self.a, self.P, self.s, self.s0 = list(period), len(period), s, s0
        top = top or 200
        q = {-1: 0, 0: 1}
        for k in range(1, top + 1):
            q[k] = self.a[(k - 1) % self.P] * q[k - 1] + q[k - 2]
        self.q, self.top = q, top

    def cap_in(self, k):
        return self.a[0] - 1 if k == 0 else self.a[k % self.P]

    def cap_out(self, k):
        if k == 0:
            return self.a[0] - 1 + self.s0
        return self.a[k % self.P] + self.s

    def codable(self, V, j):
        """Is V a capped output string from level j (true indices)?"""
        @lru_cache(maxsize=None)
        def rec(v, i):
            if v == 0:
                return True
            if i > self.top or self.q[i] > v:
                return False
            return any(rec(v - f * self.q[i], i + 1)
                       for f in range(min(self.cap_out(i), v // self.q[i]) + 1))
        return rec(V, j)

    def least_level_drop(self, V, k, lcap=LCAP):
        """The least l with V codable from level k - l, or None."""
        for l in range(lcap + 1):
            if k - l < 0:
                return None
            if self.codable(V, k - l):
                return l
        return None

    def deep(self, phi):
        """The least index of phase phi with q_{k - LCAP - 1} > 10^4."""
        k = phi
        while k - LCAP - 1 < 1 or self.q[k - LCAP - 1] <= 10 ** 4:
            k += self.P
        return k

    def legal_tails(self, k, length):
        """Legal digit strings d_k..d_{k+length-1} with d_{k-1} = 0 and
        d_k >= 1, at every length up to `length`."""
        out = []
        frontier = [((), True)]
        for i in range(length):
            nxt = []
            for tail, pzd in frontier:
                cap = self.cap_in(k + i)
                xs = range(cap + 1) if pzd else range(cap)
                for x in xs:
                    if i == 0 and x == 0:
                        continue
                    nxt.append((tail + (x,), x == 0))
            frontier = nxt
            out.extend(t for t, _ in nxt)
        return out


def brute_codable(caps, j, length, bound):
    """Every value of a capped string of `length` digits from level j."""
    vals = {0}
    for i in range(j, j + length):
        vals = set(v + f * caps.q[i] for v in vals
                   for f in range(caps.cap_out(i) + 1) if v + f * caps.q[i] <= bound)
    return vals


def bounds_at(caps, m, shift):
    """(L1, L*) of H6, read at each phase's deep index plus shift."""
    P = caps.P
    L1 = 0
    Lstar = 0
    for phi in range(P):
        k = caps.deep(phi) + shift
        for x in range(1, caps.cap_in(k) + 1):
            l = caps.least_level_drop(m * x * caps.q[k], k)
            L1 = None if (l is None or L1 is None) else max(L1, l)
        for tail in caps.legal_tails(k, P + 2):
            V = m * sum(x * caps.q[k + i] for i, x in enumerate(tail))
            l = caps.least_level_drop(V, k)
            Lstar = None if (l is None or Lstar is None) else max(Lstar, l)
    return L1, Lstar


def bounds(period, m, s, s0):
    """(L1, L*, stable): the bounds at the deep index, and whether one
    period deeper reads the same (C1e)."""
    caps = Caps(period, s, s0)
    b0 = bounds_at(caps, m, 0)
    b1 = bounds_at(caps, m, caps.P)
    return b0[0], b0[1], b0 == b1


def all_cells():
    """The 130 cells: the grid's 120 finite ones plus the ten band cells,
    as (name, period, m, s, s0)."""
    cells = []
    for name, period in WINDOWS:
        for m in (2, 3, 4, 5):
            for s, s0 in GRID:
                if (s, s0) != (0, 0):
                    cells.append((name, period, m, s, s0))
    for name, period, m, s, _want in BAND:
        cells.append((name, period, m, s, s))
    return cells


def is_digitwise(period, m, s, s0):
    return digitwise_bound(window_of(period), m, s, s0) == 0


def fmt(v):
    return "-" if v is None else str(v)


# ------------------------------------------------------------ stages
def s0_controls():
    print("== s0  C1: the decider against brute force; L = 0 at the "
          "digitwise cells; c_int >= max(c_saf, L*)")
    bad = 0
    for name, period in WINDOWS:
        for s, s0 in ((1, 0), (2, 2), (5, 5)):
            caps = Caps(period, s, s0)
            for j in range(1, caps.P + 3):
                bound = 6 * caps.q[j + 5]
                vals = brute_codable(caps, j, 6, bound)
                # a 6-digit string from level j reaches every codable
                # value under q_{j+6}; test below that
                lim = caps.q[j + 6]
                for V in range(0, lim):
                    if caps.codable(V, j) != (V in vals):
                        bad += 1
                        if bad <= 5:
                            print("    BAD decider %s s=%d j=%d V=%d"
                                  % (name, s, j, V))
    print("  C1a: %d bad" % bad)
    for name, period, m, s, s0 in all_cells():
        L1, Ls, stable = bounds(period, m, s, s0)
        if not stable:
            bad += 1
            print("    BAD C1e: %s x%d (%d,%d) bounds move with k"
                  % (name, m, s, s0))
        if is_digitwise(period, m, s, s0) and (L1, Ls) != (0, 0):
            bad += 1
            print("    BAD C1b: digitwise cell %s x%d (%d,%d) L1=%s L*=%s"
                  % (name, m, s, s0, fmt(L1), fmt(Ls)))
    print("  C1b, C1e: %d bad (cumulative)" % bad)
    # C1c is checked inside s3 where c_int is computed; its verdict
    # prints there and is folded into the return of main via s3.
    return bad


def s1_annihilation():
    print("== s1  P1: W and its (0, 0)-holders at lookahead 0 and 1, "
          "every cell")
    kill = 0
    t0 = time.time()
    rows = {"digitwise": [0, 0], "other": [0, 0]}
    for name, period, m, s, s0 in all_cells():
        win = window_of(period)
        dw = is_digitwise(period, m, s, s0)
        cells = []
        for look in (0, 1):
            g = Game(win, 1, m, (0,), look, s, s0)
            holders = sum(1 for i in g.W if g.holds0[i])
            cells.append((len(g.W), holders))
            if not dw and holders:
                kill += 1
                print("    KILL: %s x%d (%d,%d) c=%d: %d holders in W"
                      % (name, m, s, s0, look, holders))
            if dw and look == 0 and not holders:
                kill += 1
                print("    KILL: digitwise %s x%d (%d,%d) c=0 with no holder"
                      % (name, m, s, s0))
        key = "digitwise" if dw else "other"
        rows[key][0] += 1
        if all(w == 0 and h == 0 for w, h in cells):
            rows[key][1] += 1
    print("  non-digitwise cells: %d, with W EMPTY at both lookaheads: %d"
          % tuple(rows["other"]))
    print("  digitwise cells: %d, with W empty at both: %d"
          % tuple(rows["digitwise"]))
    print("  kills: %d   (%.0f s)" % (kill, time.time() - t0))
    return kill


def zero_reach(g, W, start):
    """States reachable from `start` under zero input by moves whose
    every reply stays in W; whether any holds (0, 0)."""
    seen = {start}
    dq = deque([start])
    while dq:
        i = dq.popleft()
        if g.holds0[i]:
            return True
        for _y, succ in g.trans[i].items():
            if all(s2 in W for _x, s2 in succ):
                for x, s2 in succ:
                    if x == 0 and s2 not in seen:
                        seen.add(s2)
                        dq.append(s2)
    return False


def s2_witness():
    print("== s2  P2: the witness walk from a flushed safe state, c = 1")
    cells = [("V1 (1,1,1,2)", (1, 1, 1, 2), 3, 3, 3),
             ("V2 (2,1,3,1)", (2, 1, 3, 1), 3, 5, 5),
             ("silver [2]", (2,), 2, 1, 1)]
    bad = 0
    for name, period, m, s, s0 in cells:
        win = window_of(period)
        g = Game(win, 1, m, (0,), 1, s, s0)
        Wsaf = set(i for i in g.trans if g.alive[i])
        changed = True
        while changed:
            changed = False
            for st in list(Wsaf):
                if not any(all(s2 in Wsaf for _x, s2 in succ)
                           for succ in g.trans[st].values()):
                    Wsaf.discard(st)
                    changed = True
        holders = [i for i in Wsaf if g.holds0[i]]
        caps = Caps(period, s, s0)
        P = caps.P
        # the phase with the largest overflow (m - 1) a_{k+1} - s
        phi_star = max(range(P), key=lambda phi: (m - 1) * caps.a[phi] - s)
        over = (m - 1) * caps.a[phi_star] - s
        print("  %s x%d (%d,%d): safe %d, of them (0,0)-holders %d, in W %d;"
              " worst phase %d (a=%d, overflow %d)"
              % (name, m, s, s0, len(Wsaf), len(holders),
                 sum(1 for i in holders if i in g.W), phi_star,
                 caps.a[phi_star], over))
        if not holders:
            print("    no safe holder to start from")
            bad += 1
            continue
        # walk zero input (y = 0, x = 0) from every holder past the wrap
        # and on to the phase where the NEXT revealed digit (index
        # pos + 2) has cap a_{phi_star+1}; then play that digit
        doomed = alive = 0
        for i in holders:
            walked = 0
            while (walked < P + 2
                   or (g.states[i][0] + 2) % P != phi_star):
                i = dict(g.trans[i][0])[0]
                walked += 1
                if walked > 6 * P:
                    break
            x = caps.cap_in(g.states[i][0] + 2)
            j = dict(g.trans[i][0])[x]
            alive += g.alive[j]
            doomed += not zero_reach(g, Wsaf, j)
        k = caps.deep(phi_star)
        x = caps.cap_in(k)
        V = m * x * caps.q[k]
        cod1 = caps.codable(V, k - 1)
        l = caps.least_level_drop(V, k)
        print("    %d walks: the state after the digit is alive (in the"
              " box) at %d and reaches no (0,0)-holder under zero input"
              " inside safety at %d" % (len(holders), alive, doomed))
        print("    the decider: m a q_k = %d x %d x q_%d codable from"
              " level k-1? %s; least level drop l = %s (codable from k-%s)"
              % (m, x, k, cod1, fmt(l), fmt(l)))
        if doomed != len(holders) or cod1:
            bad += 1
    print("  witness legs bad: %d" % bad)
    return bad


def s3_bound():
    print("== s3  P3: L1, L*, c_saf, c_int per cell; the tallies")
    t0 = time.time()
    bad = 0
    tally, tally1 = {}, {}
    eq_saf = eq_L = eq_both = 0
    for name, period, m, s, s0 in all_cells():
        win = window_of(period)
        top = None
        if (name, period, m, s, s0 - s) in [(b[0], b[1], b[2], b[3], 0)
                                            for b in BAND]:
            top = LOOKCAP
        c_int, c_saf, _n = price(win, m, s, s0, top=top)
        L1, Ls, _stable = bounds(period, m, s, s0)
        print("  %-14s x%d (%d,%d)  L1 %s  L* %s  c_saf %s  c_int %s"
              % (name, m, s, s0, fmt(L1), fmt(Ls), fmt(c_saf), fmt(c_int)))
        if c_int is None or Ls is None or c_saf is None:
            continue
        if c_int < Ls or c_int < c_saf:
            bad += 1
            print("    BAD C1c: c_int below a lower bound")
        d = c_int - max(c_saf, Ls)
        tally[d] = tally.get(d, 0) + 1
        d1 = c_int - Ls
        tally1[d1] = tally1.get(d1, 0) + 1
        eq_saf += (c_int == c_saf)
        eq_L += (c_int == Ls)
        eq_both += (c_int == max(c_saf, Ls))
    print("  c_int - max(c_saf, L*):")
    for d in sorted(tally):
        print("    %d: %d cells" % (d, tally[d]))
    print("  c_int - L*:")
    for d in sorted(tally1):
        print("    %d: %d cells" % (d, tally1[d]))
    print("  c_int = c_saf at %d, = L* at %d, = max at %d, of %d cells"
          % (eq_saf, eq_L, eq_both, sum(tally.values())))
    print("  C1c: %d bad   (%.0f s)" % (bad, time.time() - t0))
    return bad


def s4_corner():
    print("== s4  P4: the corner (s, s_0) = ((m-1) a_max, 0)")
    kill = 0
    for name, period in WINDOWS:
        if period[0] < 2:
            continue
        for m in (2, 3):
            s = (m - 1) * max(period)
            win = window_of(period)
            t0 = time.time()
            c_int, c_saf, n = price(win, m, s, 0, top=2)
            flag = "" if c_int == 0 else "   KILL"
            print("  %-14s x%d (%d,0)  c_int %s  c_saf %s  states %d  %.0f s%s"
                  % (name, m, s, fmt(c_int), fmt(c_saf), n,
                     time.time() - t0, flag))
            if c_int != 0:
                kill += 1
    print("  kills: %d" % kill)
    return kill


def main():
    t0 = time.time()
    if "s0" in STAGES:
        if s0_controls():
            print("CONTROL RED -- nothing below is read")
            return
    if "s1" in STAGES:
        s1_annihilation()
    if "s2" in STAGES:
        s2_witness()
    if "s3" in STAGES:
        s3_bound()
    if "s4" in STAGES:
        s4_corner()
    print("total %.0f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
