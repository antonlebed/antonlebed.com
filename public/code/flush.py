"""
flush.py -- a redundant output alphabet on the trailing Ostrowski
numeration: which maps a bottom-up reader then computes, and what
reading the integers costs over reading their completion.

QUESTION. Fix an irrational alpha = [0; a_1, a_2, ...] with
denominators q_k, numerators p_k and remainders theta_k = q_k alpha -
p_k (theta_(-1) = -1), which alternate in sign and shrink. The INPUT is
the greedy Ostrowski string of n (ostrowski.py). The OUTPUT alphabet is
widened: digit e_k may run to a_(k+1) + s (position 0 to a_1 - 1 + s_0,
with s_0 <= s + 1) and the below-a-cap rule is dropped, so an integer
has several output strings. A reader at lookahead c writes e_t having
seen d_0 .. d_(t+c). Under the legal output, n -> m n walls on the
circle and floor(n/m) is no continuous circle map at all
(ostrowski.py). Which of
the two does redundancy cure? And a reader that must write a FINITE
string equal to m n (the INTEGER reader) against one that need only
write an infinite string coding the circle point m x (the COMPLETION
reader): what separates them?

THE ARGUMENT (written before this script).
  (1) THE RANGES. The real star of a string is sum e_k theta_k, a REAL:
      two strings of one integer can differ in it by an integer. The
      tails from level t fill the interval T_t between -sum over the
      negative theta_k of (cap_k)|theta_k| and the same over the
      positive ones, and by a_(k+1) theta_k = theta_(k+1) - theta_(k-1)
      its length is |theta_(t-1)| + |theta_t| + s S_t, S_t = sum_(k>=t)
      |theta_k| (level 0: 1 + E, E = s_0 alpha + s S_1). The TAIL LEMMA
      S_t <= |theta_(t-1)| + |theta_t| follows from |theta_(k-1)| >=
      |theta_k| + |theta_(k+1)|. The members e theta_t + T_(t+1),
      e = 0 .. cap_t, cover T_t, consecutive ones overlapping by
      ov_t = |theta_(t+1)| + s S_(t+1).
  (2) THE TEAR AT E = 0. At s = s_0 = 0, T_0 = [-alpha, 1 - alpha]
      exactly, so every string of N has as star the representative of
      N alpha mod 1 in (-alpha, 1 - alpha). The least string (0, a_2,
      0, a_4, ...) has star -alpha, the greatest (a_1 - 1, 0, a_3, 0,
      ...) has 1 - alpha, and star minus -alpha is a sum of
      non-negative terms (e_k - e^min_k) theta_k, so a string within
      eta of -alpha agrees with the least string wherever |theta_k|
      > eta, likewise at the top. They part at position t_0 - 1. The
      integers of any input tile about the non-cut (1 - alpha)/m have
      images on both sides of the cut -alpha, so x m commits no output
      tile past depth t_0 - 1 there, at any lookahead: dropping the
      rule alone buys nothing.
  (3) THE COMPLETION READER AT E > 0. Keep the interval J_t of
      targets the unseen input still allows, M + m (seen star + I) -
      sum_(k<t) e_k theta_k, I the closed interval between
      -theta_(t+c+1) and -theta_(t+c), of width w_t = m (|theta_(t+c)|
      + |theta_(t+c+1)|). An interval no longer than the overlap lies
      in one member, so the reader commits e_t with J_t inside
      e_t theta_t + T_(t+1) whenever w_t <= ov_t, and the next target
      interval lies inside the committed member because the tail
      intervals nest. The lift M exists once w_0 <= E. So x m reads on
      the completion at the least c_ov meeting both, finite at every
      irrational alpha once E > 0 since |theta_(k+2)| < |theta_k| / 2.
      This is the signed-digit cure of the reading lemma: a cover
      whose children overlap by a positive amount, on the circle.
  (4) THE FLOORS DO NOT FOLLOW. A depth-t output cylinder holds stars
      in an interval of length |T_t|. The integers of any input tile
      about a non-cut x have floor(n/m) alpha accumulating at m points
      1/m apart (ostrowski.py, the residue section), so once |T_t| <
      1/m no depth-t output tile holds them: floor division commits
      nothing from that depth on, anywhere, at any s.
  (5) THE GAME. Write the residual H_t = m sum_(k<=t) d_k q_k + omega
      - sum_(k<t) e_k q_k (the pre-read d_(t+1) .. d_(t+c) kept apart)
      as g q_t + h q_(t-1), and put sigma = g theta_t + h
      theta_(t-1): (g, h) is a lattice point, integers, and a step
      sends it to (h + m d_(t+1), g - e - a_(t+1) h), labelled by the
      local quotient. The lift M sits in the seed (m d_0 + omega, -M),
      and every branch carries the same H, so the state holds the SET of
      lifts still alive: the branches' sigma differ only by integers,
      the fibre of R over R/Z. A true branch (the lift a
      correct reader realizes) has sigma_t = (output tail star) - m
      (input tail star from t + 1), so |sigma_t| < (1 + s)|theta_(t-1)|
      + m |theta_t|, and |H_t| <= mu q_(t+1), mu = max(m, 1 + s).
      Inverting the unimodular frame with q_t |theta_(t-1)|,
      q_(t+1) |theta_t| and q_(t-1) |theta_(t-1)| at most 1 (equal only
      at q_0 |theta_(-1)|, where the sigma bound is strict) and
      q_(t+1) |theta_(t-1)| < a_(t+1) + 1:
          |g| < mu (A + 1) + 1 + s + m,   |h| < 1 + s + m + mu,
      A the largest quotient. Prune to that BOX and the pruning never
      removes a true branch, so a win of the pruned game is a real
      reader and a loss is a real loss, with no lookahead in the box.
      The INTEGER game adds the FLUSH: under zero input the reader must
      force the branch (0, 0) with nothing pending (H = 0). The SAFETY
      game drops it. c_int and c_saf are their least lookaheads.
  (6) THE COMPLETION READER IS THE SAFETY GAME: c_comp = c_saf at
      omega = 0. A safe play keeps the branch set non-empty; each
      branch has one parent, the box holds finitely many per state, so
      by Koenig one lineage runs forever, and its sigma_t -> 0 at the
      rate of the box times |theta_(t-1)|: the output codes m x + M, a
      completion reader. A completion reader's own lift gives a true
      branch, inside the box by (5), so it plays safe. So tracking the
      lifts costs nothing, the width of the box is irrelevant above
      (5)'s floor, and
      c_int - c_comp = c_int - c_saf is the price of the flush alone.
  (7) THE FLUSH FLOOR. If s >= (m - 1) a_(k+1) at every k >= 1, the
      digitwise reader e_0 = m d_0 mod a_1, e_1 = m d_1 + floor(m d_0 /
      a_1), e_k = m d_k fits the caps (d_0 >= 1 forces d_1 <= a_2 - 1),
      whatever s_0: c_int = 0. If (m - 1) a_(k+1) > s and m a_(k+1) <
      q_(k-1) for infinitely many k, no integer reader has c <= 1: a
      reader flushed on n writes the same prefix on n' = n + a_(k+1)
      q_k (k deep, a zero below it) through position k - c - 1, so it
      owes exactly m a_(k+1) q_k, from level k - c >= k - 1. Writing
      q_(k+j) = U_j q_k + V_j q_(k-1) with V_j >= 1, a string of value
      m a_(k+1) q_k from level k - 1 has q_k | Y, Y = e_(k-1) + sum
      e_(k+j) V_j, and Y >= q_k would force m a_(k+1) >= q_(k-1); so
      Y = 0 and the only string is e_k = m a_(k+1), over its cap
      a_(k+1) + s. So c_int
      is 0 or at least 2, never 1, at every periodic alpha.
  (8) THE UNIVERSAL READER. The step is labelled by the local quotient
      only, so over the alphabet {1, .., A} the game with the OPPONENT
      choosing each quotient is ONE finite game; a win is a reader
      that sees the quotients through a_(t+c+1) and nothing else of
      alpha, correct at every alpha with quotients <= A.

PREDICTIONS (frozen before the engine ran).
  C1 CONTROLS, run first. (a) At every alpha the range T_0 has length
     1 + E and each overlap is ov_t as (1) says, the tail lemma holds
     at every level read. (b) The legal output (rule kept, s = s_0 =
     0) through the game: the identity at 0, n + 1 at 1, x 2 and x 3
     at no c <= LOOKCAP at all six periodic alphas (ostrowski.py's
     theorems); with the rule dropped, n + 1 at 0. (c) Every winning
     strategy of the grid and the band writes m n + omega under the caps
     and flushes for every n < N_CHECK, 0 bad (the legal output's are
     not certified). (d) The grid's c_int agrees at every
     cell with the table of an earlier, independent engine (lattice
     points of the quadratic field of alpha, a box derived otherwise),
     EARLIER below.
  P1 THE TEAR. Every string of every N < N_TEAR at s = s_0 = 0 has
     star the representative of N alpha mod 1; every string within
     eta of an end agrees with that end's extreme string where
     |theta_k| > eta; the extremes part at t_0 - 1. The game's
     (0, 0) column: x m reads at no c <= LOOKCAP. Kill: one string off.
  P2 THE COMPLETION READER. At every alpha (the six periodic ones,
     e - 2, and the band alphas) and every cell with E > 0, the
     overlap reader at c_ov never fails to find a member over
     N_PLAY random inputs to depth DEPTH, and |its star - (m x + M)|
     is at most |T_DEPTH|. c_ov printed. Kill: a failure.
  P3 THE FLOORS. For m = 2, 3 and s = s_0 = 0..3, at the first depth
     t* with |T_t*| < 1/m, every input tile at depth t* + c (c = 0..3)
     holding at least 12 integers below N_FLOOR has a circular hull of
     floor(n/m) alpha longer than |T_t*|. Kill: a tile whose hull fits.
  P4 THE FLUSH FLOOR. (a) The digitwise reader is correct on n <
     N_CHECK at every cell with s >= (m - 1) a_max, s_0 = 0 included.
     (b) At one k of every phase, the first k >= 2 with
     m a_(k+1) < q_(k-1), value m a_(k+1) q_k has exactly one string
     from level k - 1, of any digit sizes. (c) Over the grid, c_int is 0
     exactly where s >= (m - 1) a_max and at least 2 elsewhere. Kill:
     a printed 1, or a 0 below the line.
  P5 THE COMPLETION READER IS THE SAFETY GAME. (a) The overlap
     reader's true branch, tracked in frame coordinates, never leaves
     the box at any cell of P2: max |g|, |h| printed beside it. (b)
     c_saf <= c_ov at every cell. (c) --full: c_saf at twice the box
     equals c_saf at the box at a sample of cells. (d) The band cells
     [4] x 2 at s = s_0 = 3, [5] x 2 at 3, [4] x 3 at 5 and bronze
     x 3 at 5: c_ov = 1, so c_comp <= 1, and c_int >= 2 by P4: a
     strict flush price at each. Kill: c_saf above c_ov, a branch out
     of the box, or c_int <= 1 at a band cell.
  P6 THE UNIVERSAL READER. {1, 2}: x 2 at (1, 1) wins at 2 and not at
     1 (the default run). --full: {1, 2, 3} x 2 at (1, 1) at 2; {1, 2}
     x 3 at (1, 1) at exactly 3 and x 3 at (2, 2) at 2; every win
     certified at 12 random alphas over the alphabet and its constant
     ones; the flushing lineages of a win solved at twice the box stay
     inside the box ({1, 2}, x 2); every primitive {1, 2}-necklace of period <= 8
     reads x 3 at (1, 1) at c_int = 2, at every rotation. Not predicted: whether a
     periodic member reaches the class's 3.

THE DESIGN. Exact rationals for everything metric (ostrowski.py's
Numeration, alpha replaced by a convergent past 10^60). One game engine
for every quotient source: a periodic alpha is the source cycling its
period, a class is the source offering every letter at every step. The
state holds the sorted branches, the pending quotients a_(t+1) ..
a_(t+c+1), the source's state, the pending digits, whether the last
input digit is 0, whether this is position 0, and whether the last
output digit is 0 (read only with the rule kept, but carried always,
so every printed state count includes it). Safety is a greatest fixed
point; the flush alternates it with the attractor of the flushed
states under zero input. The reader picks, among moves keeping every
reply winning, one of least rank toward the flush under zero replies:
a rank that falls at every zero step, set once per state, not always
the least distance. Default: the grid at golden, silver and
sqrt(3) - 1 for x 2 and x 3, the band cell [4] x 2, the {1, 2}
universal cell; `--full` runs everything above.

FINDINGS (entered after the run, from its prints; `--full`).
  F1 CONTROLS (C1, all green, run first). The ranges and overlaps agree
     with (1) to half the truncation bound at worst over seven alphas
     and six slacks. The legal output reads the identity at 0, n + 1 at
     1, and x 2, x 3 at no c <= 3 at all six periodic alphas; with the
     rule dropped n + 1 reads at 0. Every winning strategy of the grid
     and the band is correct on every n < 1000. The grid's c_int agrees
     with EARLIER at all 144 cells, although this engine's box is smaller than that one's.
  F2 THE TEAR (P1 lands). 8,321 strings of N < 300 at seven alphas: 0
     stars off, 0 disagreements with the extremes; the (0, 0) column
     reads at no c <= 3 everywhere.
  F3 THE OVERLAP READER (P2 lands). 36,000 runs to depth 40 at nine
     alphas, x 2 .. x 5, five slacks: 0 failures, every output star
     within |T_40| of m x + M. c_ov runs from 0 to 6 over the grid
     (golden x 5 at (0, 1) is 6).
  F4 THE FLOORS (P3 lands). 9,063 (tile, m, s, c) tests, m = 2, 3,
     s = s_0 = 0 .. 3, c = 0 .. 3: none fits; the least hull exceeds
     |T_t*| by 0.196.
  F5 THE FLUSH FLOOR (P4 lands). The digitwise reader is correct at
     every alpha and m = 2 .. 5 at s = (m - 1) a_max, s_0 = 0; the value
     m a_(k+1) q_k has one string from level k - 1 of any digit sizes at
     every phase, e_k = m a_(k+1), which is over its cap, so it has no
     capped string: P4(b)'s "exactly one capped string" was wrong as
     frozen, and the check counts strings of any digit sizes; over the
     grid c_int
     is 0 exactly where s >= (m - 1) a_max and 2 or more elsewhere.
     c_int - c_saf over the 120 finite cells: 0 at 91, 1 at 28, 2 at one
     (V1 x 3 at (3, 3), c_saf 0).
  F6 THE SAFETY GAME (P5 lands). The overlap reader's true branch uses
     at most 0.92 of B_g and 0.42 of B_h; c_saf <= c_ov at every cell;
     c_saf is unchanged at twice the box at four cells; at the four band
     cells c_ov = c_saf = 1 and c_int = 2, strategies 0 bad.
  F7 THE UNIVERSAL READER (P6 lands). x 2 at (1, 1) reads at exactly 2
     over {1, 2} (28,268 states) and {1, 2, 3} (225,747); x 3 at (1, 1)
     at exactly 3 over {1, 2} (246,554) and x 3 at (2, 2) at 2
     (87,131). Every win certified at 14 or 15 members, 0 bad; the
     flushing lineages at twice the box reach (4, 2) against (10, 6).
     All 472 purely periodic {1, 2} alphas of primitive period <= 8
     (every rotation of the 71 words) read x 3 at (1, 1) at 2: no
     periodic member of the class to that period needs the class's 3.

RUN RECORD. `--full`: 109.0 s, peak 312 MB under a 512 MB watch; the
default: 5.8 s, 148 MB. Two earlier full runs were killed at the
ceiling while holding a twice-box game beside the {1, 2, 3} and the
x 3 cells; the twice-box lineage check now runs at {1, 2}, x 2 only,
and each game is freed before the next. A print of the c_int - c_saf
tally was added to the grid after the slate froze. An independent
audit then found P6's necklaces read at one rotation each (71 of the
472 alphas) and P1's comparison stopping at a string's own length; both
now run whole, and every print above is the whole run's. A later
reading found the box's A taken over a_1 .. a_52, past the quotients
the track's times 0 .. 40 use (a_1 .. a_41); at e - 2 that inflated
B_g, and with A over a_1 .. a_41 the branch's share of B_g is 0.92,
first printed as 0.77. The same reading split P6's unflushed reads
from its seed mismatches and asserted the (0, 0) column's safety game
too. The run after: 28/28, 110.4 s, peak 309 MB.
"""

import os
import random
import sys
import time

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ostrowski import Numeration, e_minus_2  # noqa: E402

CHECKS = []
FULL = "--full" in sys.argv    # the record run; the default runs small
LOOKCAP = 3
N_CHECK = 1000 if FULL else 400
N_TEAR = 300 if FULL else 120
N_FLOOR = 60000 if FULL else 20000
N_PLAY, DEPTH = (200, 40) if FULL else (60, 30)
SEED = 20260924

PERIODIC = [("golden [1]", (1,)), ("silver [2]", (2,)),
            ("bronze [3]", (3,)), ("sqrt(3) - 1 [1, 2]", (1, 2)),
            ("V1 [1, 1, 1, 2]", (1, 1, 1, 2)),
            ("V2 [2, 1, 3, 1]", (2, 1, 3, 1))]
SLACKS = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2), (3, 3)]
# The integer reader's least lookahead over this grid as an earlier,
# independent engine printed it (lattice points of the quadratic field
# of alpha, its own box): rows x2..x5, columns SLACKS, None for no c up
# to its cap.
EARLIER = {
    "golden [1]": [[None, 3, 0, 0, 0, 0], [None, 5, 2, 2, 0, 0],
                   [None, 5, 3, 3, 2, 0], [None, 6, 3, 3, 2, 2]],
    "silver [2]": [[None, 2, 2, 2, 0, 0], [None, 3, 2, 2, 2, 2],
                   [None, 3, 3, 2, 2, 2], [None, 4, 3, 3, 2, 2]],
    "bronze [3]": [[None, 2, 2, 2, 2, 0], [None, 2, 2, 2, 2, 2],
                   [None, 3, 2, 2, 2, 2], [None, 3, 2, 2, 2, 2]],
    "sqrt(3) - 1 [1, 2]": [[None, 3, 2, 2, 0, 0], [None, 4, 2, 2, 2, 2],
                           [None, 5, 3, 3, 2, 2], [None, 5, 3, 3, 2, 2]],
    "V1 [1, 1, 1, 2]": [[None, 3, 2, 2, 0, 0], [None, 4, 2, 2, 2, 2],
                        [None, 5, 3, 3, 2, 2], [None, 5, 4, 4, 2, 2]],
    "V2 [2, 1, 3, 1]": [[None, 3, 2, 2, 2, 0], [None, 4, 2, 2, 2, 2],
                        [None, 4, 3, 3, 2, 2], [None, 5, 3, 3, 2, 2]],
}
BAND = [("[4]", (4,), 2, 3), ("[5]", (5,), 2, 3), ("[4]", (4,), 3, 5),
        ("bronze [3]", (3,), 3, 5)]


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    tag = "ok  " if ok else "FAIL"
    print(f"  [{tag}] {name}" + (f" -- {detail}" if detail else ""))


def numeration(name, period):
    reps = -(-200 // len(period))
    while True:
        quots = list(period) * reps
        try:
            return Numeration(name, quots)
        except AssertionError:
            reps += 1


# ------------------------------------------------------------ the metric

class Metric:
    """theta_k, the level ranges T_L and their overlaps at slack
    (s, s0), exactly: every real is held as its numerator over the
    convergent's denominator Q."""

    def __init__(self, w, s, s0, top):
        self.w, self.s, self.s0, self.top = w, s, s0, top
        self.Q, self.a = w.Q, w.a
        self.th = [A * w.Q + B * w.P
                   for A, B in (w.theta(k) for k in range(-1, top + 3))]

    def theta(self, k):
        return self.th[k + 1]

    def cap(self, k):
        return self.a[1] - 1 + self.s0 if k == 0 else self.a[k + 1] + self.s

    def S(self, L):
        return sum(abs(self.theta(k)) for k in range(L, self.top))

    def T(self, L):
        """(lo, hi) of the tails from level t, truncated at top."""
        lo = hi = 0
        for k in range(L, self.top):
            v = self.cap(k) * self.theta(k)
            if v < 0:
                lo += v
            else:
                hi += v
        return lo, hi

    def E(self):
        return self.s0 * self.theta(0) + self.s * self.S(1)

    def ov(self, L):
        lo, hi = self.T(L + 1)
        return hi - lo - abs(self.theta(L))

    def width(self, L, c, m):
        return m * (abs(self.theta(L + c)) + abs(self.theta(L + c + 1)))


def c_overlap(met, m, depth, cmax=12):
    """The least c with w_0 <= E and w_t <= ov_t at every t < depth."""
    E = met.E()
    if E <= 0:
        return None
    ovs = [met.ov(L) for L in range(depth)]
    for c in range(cmax + 1):
        if met.width(0, c, m) <= E and all(
                met.width(L, c, m) <= ovs[L] for L in range(depth)):
            return c
    return None


# ------------------------------------------------------------ the game

class Source:
    """Where the quotients come from: a periodic alpha (the state is
    the index of the next quotient in the period) or a class (every
    letter of the alphabet at every step, one state)."""

    def __init__(self, period=None, alphabet=None):
        self.period, self.alphabet = period, alphabet
        self.A = max(period or alphabet)

    def start(self):
        return 0

    def nxt(self, st):
        if self.period:
            P = self.period
            return [(P[st], (st + 1) % len(P))]
        return [(a, 0) for a in self.alphabet]


class Game:
    """The residual game of n -> m n + omega at lookahead `look`, the
    output capped at a_(t+1) + s (position 0: a_1 - 1 + s0), in frame
    coordinates (argument (5)). rule=True keeps the below-a-cap rule
    on the output (the legal output; s = s0 = 0 only)."""

    def __init__(self, src, m, s, s0, look, omega=0, rule=False, scale=1):
        assert 0 <= omega <= m and s0 <= s + 1
        assert not rule or s == s0 == 0
        self.src, self.m, self.s, self.s0 = src, m, s, s0
        self.look, self.omega, self.rule = look, omega, rule
        mu = max(m, 1 + s)
        self.bx = scale * (mu * (src.A + 1) + 1 + s + m)
        self.by = scale * (1 + s + m + mu)
        self.K = 2 * self.by + 1
        self.build()

    def pack(self, x, y):
        return (x + self.bx) * self.K + (y + self.by)

    # a state: (branches, quots, srcst, digs, lastzero_in, pos0,
    # lastzero_out); quots = (a_(t+1) .. a_(t+c+1)), digs = (d_(t+1) ..
    # d_(t+c)).
    def cap_out(self, st):
        a1 = st[1][0]
        if st[5]:
            return a1 - 1 + self.s0
        if self.rule and not st[6]:
            return a1 - 1
        return a1 + self.s

    def replies(self, st):
        for a_new, src2 in self.src.nxt(st[2]):
            top = a_new if st[4] else a_new - 1
            for d_new in range(top + 1):
                yield a_new, src2, d_new

    def succ(self, st, e, a_new, src2, d_new):
        br, quots, digs = st[0], st[1], st[3]
        seq = digs + (d_new,)
        d1, a1, m = seq[0], quots[0], self.m
        bx, by, K = self.bx, self.by, self.K
        out = []
        for v in br:
            x, y = divmod(v, K)
            x -= bx
            y -= by
            X, Y = y + m * d1, x - e - a1 * y
            if -bx <= X <= bx and -by <= Y <= by:
                out.append((X + bx) * K + (Y + by))
        if not out:
            return None
        return (tuple(sorted(out)), quots[1:] + (a_new,), src2, seq[1:],
                d_new == 0, False, e == 0)

    def seed(self, d0):
        x = self.m * d0 + self.omega
        return tuple(sorted(self.pack(x, y)
                            for y in range(-self.by, self.by + 1)))

    def initial(self):
        """Every legal pre-read d_0 .. d_c with its quotients."""
        out, c = [], self.look

        def rec(quots, srcst, digs, lastzero):
            if len(quots) == c + 1:
                out.append((self.seed(digs[0]), quots, srcst, digs[1:],
                            lastzero, True, True))
                return
            k = len(quots)
            for a, src2 in self.src.nxt(srcst):
                top = a - 1 if k == 0 else (a if lastzero else a - 1)
                for d in range(top + 1):
                    rec(quots + (a,), src2, digs + (d,), d == 0)
        rec((), self.src.start(), (), True)
        return out

    def build(self):
        ids, states = {}, []
        self.init = []
        for st in self.initial():
            if st not in ids:
                ids[st] = len(states)
                states.append(st)
            self.init.append(ids[st])
        todo = list(range(len(states)))
        trans = [None] * len(states)
        while todo:
            i = todo.pop()
            st = states[i]
            moves = {}
            for e in range(self.cap_out(st) + 1):
                zs, nz = [], []
                for a_new, src2, d_new in self.replies(st):
                    st2 = self.succ(st, e, a_new, src2, d_new)
                    if st2 is None:
                        break
                    j = ids.get(st2)
                    if j is None:
                        j = ids[st2] = len(states)
                        states.append(st2)
                        trans.append(None)
                        todo.append(j)
                    (zs if d_new == 0 else nz).append(j)
                else:
                    moves[e] = (len(zs), tuple(zs + nz))
            trans[i] = moves
        self.trans, self.states, self.ids = trans, states, ids
        self.zero = self.pack(0, 0)

    def solve(self, flush):
        """The winning set: safety, alternated with the flush attractor
        when flush is True. Sets W and dist; returns whether every
        initial state wins."""
        W = set(range(len(self.states)))
        flushed = [self.zero in st[0] and not any(st[3])
                   for st in self.states]
        while True:
            changed = True
            while changed:
                changed = False
                for i in list(W):
                    if not any(all(j in W for j in succ)
                               for _nz, succ in self.trans[i].values()):
                        W.discard(i)
                        changed = True
            if not flush:
                self.W, self.dist = W, None
                break
            dist = {i: 0 for i in W if flushed[i]}
            grew = True
            while grew:
                grew = False
                for i in W:
                    if i in dist:
                        continue
                    best = None
                    for nz, succ in self.trans[i].values():
                        zs = succ[:nz]
                        if zs and all(j in W for j in succ) and all(
                                j in dist for j in zs):
                            v = 1 + max(dist[j] for j in zs)
                            best = v if best is None else min(best, v)
                    if best is not None:
                        dist[i] = best
                        grew = True
            if len(dist) == len(W):
                self.W, self.dist = W, dist
                break
            W = set(dist)
        self.wins = all(i in self.W for i in self.init)
        return self.wins

    def choose(self, i):
        best = None
        for e, (nz, succ) in self.trans[i].items():
            if all(j in self.W for j in succ):
                key = 0
                if self.dist is not None:
                    key = max(self.dist[j] for j in succ[:nz])
                if best is None or key < best[0]:
                    best = (key, e)
        return best[1]

    def start_state(self, d, quots):
        c = self.look
        for i in self.init:
            st = self.states[i]
            if st[1] == tuple(quots[:c + 1]) and st[3] == tuple(d[1:c + 1]) \
                    and st[0] == self.seed(d[0]):
                return i
        raise KeyError("no initial state for this pre-read")

    def read(self, digits, quots, extra=6):
        """Run the reader on a greedy string at the alpha whose
        quotients are quots (a_1, a_2, ...): (output, flushed, path),
        path holding (e, d_(t+1), a_(t+1)) per step."""
        c = self.look
        d = list(digits) + [0] * (c + extra + 2)
        i = self.start_state(d, quots)
        out, path = [], []
        for t in range(len(digits) + extra):
            e = self.choose(i)
            cur = self.states[i]
            a_new, d_new = quots[t + c + 1], d[t + c + 1]
            src2 = [s2 for a, s2 in self.src.nxt(cur[2]) if a == a_new][0]
            st2 = self.succ(cur, e, a_new, src2, d_new)
            path.append((e, (cur[3] + (d_new,))[0], cur[1][0]))
            out.append(e)
            i = self.ids[st2]
        st = self.states[i]
        return out, self.zero in st[0] and not any(st[3]), path


def least(src, m, s, s0, flush, lo=0, hi=LOOKCAP, omega=0, rule=False,
          scale=1):
    """The least lookahead in lo..hi at which the reader wins, with the
    winning game; (None, None) when none does."""
    for c in range(lo, hi + 1):
        g = Game(src, m, s, s0, c, omega, rule, scale)
        if g.solve(flush):
            return c, g
    return None, None


# ------------------------------------------------------------ helpers

def maps():
    return (2, 3, 4, 5) if FULL else (2, 3)


def legal_random(rnd, quots, length):
    """A random legal greedy string of the given length."""
    d, last = [], 0
    for k in range(length):
        cap = quots[0] - 1 if k == 0 else quots[k]
        top = cap if (k == 0 or last == 0) else cap - 1
        d.append(rnd.randint(0, top))
        last = d[-1]
    return d


def certify(g, w, m, s, s0, N, omega=0):
    """Run the reader of game g on every n < N at numeration w; the
    count of wrong values, broken caps or missing flushes."""
    bad = 0
    quots = w.a[1:]
    for n in range(N):
        out, flushed, _path = g.read(w.digits(n), quots)
        val = sum(e * w.q(k) for k, e in enumerate(out))
        caps = all(e <= (quots[0] - 1 + s0 if k == 0 else quots[k] + s)
                   for k, e in enumerate(out))
        if val != m * n + omega or not caps or not flushed:
            bad += 1
    return bad


def lineage(g, path):
    """The flushing branch's trajectory, rebuilt backward from (0, 0)
    through the recorded (e, d_(t+1), a_(t+1)): its largest |g|, |h|
    and its seed's g."""
    x = y = 0
    mx = my = 0
    for e, d1, a1 in reversed(path):
        y0 = x - g.m * d1
        x0 = y + e + a1 * y0
        x, y = x0, y0
        mx, my = max(mx, abs(x)), max(my, abs(y))
    return mx, my, x


# ------------------------------------------------------------ C1a ranges

def section_ranges():
    print("== C1a the ranges, the overlaps and the tail lemma")
    alist = [(n, p) for n, p in PERIODIC] + [("e - 2", None)]
    worst = 0
    for name, per in alist:
        w = numeration(name, per) if per else Numeration(name, e_minus_2(200))
        for s, s0 in SLACKS:
            met = Metric(w, s, s0, 120)
            lo, hi = met.T(0)
            tol = 4 * abs(met.theta(met.top - 1))
            dev = abs((hi - lo) - (met.Q + met.E()))
            ovdev = max(abs(met.ov(L) - abs(met.theta(L + 1))
                            - s * met.S(L + 1)) for L in range(30))
            lemma = min(abs(met.theta(L - 1)) + abs(met.theta(L))
                        - met.S(L) for L in range(40))
            worst = max(worst, float(dev / tol), float(ovdev / tol))
            if lemma < 0:
                worst = float("inf")
    check("|T_0| = 1 + E and ov_t = |theta_(t+1)| + s S_(t+1) to the "
          "truncation, the tail lemma at every level read",
          worst <= 1, f"worst deviation {worst:.2f} of the truncation bound")


# ------------------------------------------------------------ P1 the tear

def strings_of(w, N, s, s0, k=None):
    """Every string with e_j <= cap_j and sum e_j q_j = N."""
    if k is None:
        k = w.depth_of(N) if N else 0
    if k < 0:
        return [[]] if N == 0 else []
    cap = w.a[1] - 1 + s0 if k == 0 else w.a[k + 1] + s
    out = []
    for e in range(min(cap, N // w.q(k)) + 1):
        for rest in strings_of(w, N - e * w.q(k), s, s0, k - 1):
            out.append(rest + [e])
    return out


def section_tear():
    print("== P1 the tear at E = 0")
    alist = [(n, p) for n, p in PERIODIC] + [("e - 2", None)]
    total = off = disagree = 0
    part_ok = True
    for name, per in alist:
        w = numeration(name, per) if per else Numeration(name, e_minus_2(200))
        th = [w.value(w.theta(k)) for k in range(40)]
        alpha = th[0]
        lo_s = [0 if k % 2 == 0 else w.a[k + 1] for k in range(40)]
        hi_s = [(w.a[1] - 1 if k == 0 else w.a[k + 1]) if k % 2 == 0 else 0
                for k in range(40)]
        part = next(k for k in range(40) if lo_s[k] != hi_s[k])
        part_ok &= part == w.t0 - 1
        for N in range(N_TEAR):
            rep = N * alpha - ((N * alpha + alpha).numerator
                               // (N * alpha + alpha).denominator)
            for e in strings_of(w, N, 0, 0):
                e = e + [0] * (40 - len(e))
                total += 1
                star = sum(ek * th[k] for k, ek in enumerate(e))
                if star != rep:
                    off += 1
                for ext, gap in ((lo_s, star + alpha),
                                 (hi_s, 1 - alpha - star)):
                    for k, ek in enumerate(e):
                        if abs(th[k]) > gap and ek != ext[k]:
                            disagree += 1
    check("every string's star is the representative of N alpha mod 1",
          off == 0, f"{total} strings over N < {N_TEAR} at seven alphas, "
          f"{off} off")
    check("a string within eta of an end agrees with that end's extreme "
          "string wherever |theta_k| > eta", disagree == 0,
          f"{disagree} disagreements")
    check("the extreme strings part at position t_0 - 1", part_ok)


# ------------------------------------------------------ P2 and P5a

class Overlap:
    """The completion reader of argument (3) at lookahead c, in integer
    numerators over the convergent's denominator Q."""

    def __init__(self, w, m, s, s0, c, depth):
        self.w, self.m, self.s, self.s0, self.c = w, m, s, s0, c
        top = depth + c + 60
        self.th = [w.theta(k) for k in range(-1, top + 2)]
        self.th = [A * w.Q + B * w.P for A, B in self.th]
        self.Q = w.Q
        self.depth, self.top = depth, top
        self.cap = [w.a[1] - 1 + s0] + [w.a[k + 1] + s
                                        for k in range(1, top + 1)]
        self.T = []
        for L in range(depth + 2):
            lo = hi = 0
            for k in range(L, top):
                v = self.cap[k] * self.t(k)
                lo, hi = (lo + v, hi) if v < 0 else (lo, hi + v)
            self.T.append((lo, hi))

    def t(self, k):
        return self.th[k + 1]

    def interval(self, j):
        """The closed interval between -theta_j and -theta_(j-1)."""
        a, b = -self.t(j), -self.t(j - 1)
        return min(a, b), max(a, b)

    def run(self, d):
        """Read the legal string d (long enough); returns (ok, M, out,
        close), close whether |output star - (m x + M)| <= |T_depth|."""
        m, c, Q = self.m, self.c, self.Q
        seen = sum(d[k] * self.t(k) for k in range(c + 1))
        ilo, ihi = self.interval(c + 1)
        lo, hi = m * (seen + ilo), m * (seen + ihi)
        T0lo, T0hi = self.T[0]
        M = -((lo - T0lo) // Q)          # lo + M Q lands in [T0lo, T0lo + Q)
        lo, hi = lo + M * Q, hi + M * Q
        if not (T0lo <= lo and hi <= T0hi):
            return False, M, [], None
        committed = 0
        out = []
        for L in range(self.depth):
            base = M * Q + m * seen - committed     # M + m seen - committed
            ilo, ihi = self.interval(L + c + 1)
            jlo, jhi = base + m * ilo, base + m * ihi
            tl, th_ = self.T[L + 1]
            best = None
            for e in range(self.cap[L] + 1):
                off = e * self.t(L)
                if off + tl <= jlo and jhi <= off + th_:
                    margin = min(jlo - off - tl, off + th_ - jhi)
                    if best is None or margin > best[0]:
                        best = (margin, e)
            if best is None:
                return False, M, out, None
            e = best[1]
            out.append(e)
            committed += e * self.t(L)
            seen += d[L + c + 1] * self.t(L + c + 1)
        xstar = sum(d[k] * self.t(k) for k in range(len(d)))
        err = abs(committed - (m * xstar + M * Q))
        tl, th_ = self.T[self.depth]
        return True, M, out, err <= th_ - tl


def section_completion():
    print("== P2 the completion reader, and P5a its branch in the box")
    rnd = random.Random(SEED)
    alist = [(n, p) for n, p in PERIODIC] + [("e - 2", None)]
    if FULL:
        alist += [("[4]", (4,)), ("[5]", (5,))]
    fails = errs = outbox = runs = 0
    cov = {}
    worst = (0, 0)
    for name, per in alist:
        w = numeration(name, per) if per else Numeration(name, e_minus_2(200))
        quots = w.a[1:]
        A = max(quots[:DEPTH + 1])        # a_(t+1) at the track's times 0..DEPTH
        for m in maps():
            for s, s0 in SLACKS[1:]:
                met = Metric(w, s, s0, DEPTH + 60)
                c = c_overlap(met, m, DEPTH)
                cov[(name, m, s, s0)] = c
                rd = Overlap(w, m, s, s0, c, DEPTH)
                mu = max(m, 1 + s)
                bx, by = mu * (A + 1) + 1 + s + m, 1 + s + m + mu
                for _ in range(N_PLAY):
                    d = legal_random(rnd, quots, DEPTH + c + 4)
                    ok, M, out, close = rd.run(d)
                    runs += 1
                    if not ok:
                        fails += 1
                        continue
                    if not close:
                        errs += 1
                    mx, my = _track(m, out, d, M, quots)
                    worst = (max(worst[0], mx / bx), max(worst[1], my / by))
                    if mx > bx or my > by:
                        outbox += 1
    check("the overlap reader finds a member at every level", fails == 0,
          f"{runs} runs to depth {DEPTH}, {fails} failures")
    check("its output star lies within |T_depth| of m x + M", errs == 0,
          f"{errs} off")
    check("its true branch stays inside the box", outbox == 0,
          f"largest |g|/Bg {worst[0]:.2f}, |h|/Bh {worst[1]:.2f}")
    return cov


def _track(m, out, d, M, quots):
    x, y = m * d[0], -M
    mx, my = abs(x), abs(y)
    for t, e in enumerate(out):
        x, y = y + m * d[t + 1], x - e - quots[t] * y
        mx, my = max(mx, abs(x)), max(my, abs(y))
    return mx, my


# ------------------------------------------------------------ P3 floors

def section_floors():
    print("== P3 the floors at every slack")
    alist = PERIODIC if FULL else PERIODIC[:4]
    tiles = fits = 0
    least_excess = None
    for name, per in alist:
        w = numeration(name, per)
        keys = w.keys(N_FLOOR)
        for m in (2, 3):
            for s in range(4):
                met = Metric(w, s, s, 120)
                t = next(t for t in range(1, 60)
                         if m * (met.T(t)[1] - met.T(t)[0]) < met.Q)
                width = met.T(t)[1] - met.T(t)[0]
                for c in range(4):
                    if t + c >= len(keys):
                        break
                    groups = {}
                    for n, key in enumerate(keys[t + c]):
                        groups.setdefault(key, []).append(n)
                    for ns in groups.values():
                        if len(ns) < 12:
                            continue
                        pts = sorted((n // m) * w.P % w.Q for n in ns)
                        gaps = [b - a for a, b in zip(pts, pts[1:])]
                        gaps.append(pts[0] + w.Q - pts[-1])
                        hull = w.Q - max(gaps)
                        tiles += 1
                        ex = (hull - width) / w.Q
                        least_excess = ex if least_excess is None \
                            else min(least_excess, ex)
                        if hull <= width:
                            fits += 1
    check("floor(n/m): no input tile's images fit a depth-t* cylinder",
          fits == 0, f"{tiles} (tile, m, s, c) tests, m = 2, 3, s = s_0 "
          f"= 0..3, c = 0..3, least "
          f"hull less |T_t*| = {least_excess:.4f}")


# ------------------------------------------------------ C1b-d, P1, P4, P5b

def section_controls():
    print("== C1b the legal output through the game")
    ok = True
    for name, per in PERIODIC:
        src = Source(period=per)
        ident = least(src, 1, 0, 0, True, rule=True)[0]
        succ = least(src, 1, 0, 0, True, omega=1, rule=True)[0]
        x2 = least(src, 2, 0, 0, True, rule=True)[0]
        x3 = least(src, 3, 0, 0, True, rule=True)[0]
        free = least(src, 1, 0, 0, True, omega=1)[0]
        row = (ident, succ, x2, x3, free)
        ok &= row == (0, 1, None, None, 0)
        print(f"    {name:20s} id {ident}  n+1 {succ}  x2 {x2}  x3 {x3}"
              f"   n+1 rule dropped {free}")
    check("identity 0, n + 1 at 1, x 2 and x 3 at no c <= LOOKCAP; "
          "n + 1 at 0 once the rule is dropped", ok)


def section_grid(cov):
    print("== the grid: c_saf / c_int per (alpha, m, (s, s_0)), c_ov after")
    alist = PERIODIC if FULL else [PERIODIC[0], PERIODIC[1], PERIODIC[3]]
    bad = earlier_off = floor_off = saf_over = tear_off = 0
    grid = {}
    for name, per in alist:
        src = Source(period=per)
        w = numeration(name, per)
        A = max(per)
        print(f"  {name}")
        for m in maps():
            row = []
            for j, (s, s0) in enumerate(SLACKS):
                c_ov = cov.get((name, m, s, s0))
                hi = max(LOOKCAP, (c_ov or 0) + 1)
                c_saf, _g = least(src, m, s, s0, False, hi=hi)
                c_int, g = least(src, m, s, s0, True, lo=c_saf or 0, hi=hi) \
                    if c_saf is not None else (None, None)
                if g is not None:
                    bad += certify(g, w, m, s, s0, N_CHECK)
                grid[(name, m, s, s0)] = (c_saf, c_int)
                if c_int != EARLIER[name][m - 2][j]:
                    earlier_off += 1
                digitwise = s >= (m - 1) * A
                if (c_int == 0) != digitwise or c_int == 1:
                    floor_off += 1
                if (s, s0) == (0, 0) and c_saf is not None:   # no reader at all
                    tear_off += 1
                if c_ov is not None and (c_saf is None or c_saf > c_ov):
                    saf_over += 1
                row.append(f"{_fmt(c_saf)}/{_fmt(c_int)} {_fmt(c_ov)}")
            print(f"    x{m}  " + "   ".join(f"{r:7s}" for r in row))
    tally = {}
    for c_saf, c_int in grid.values():
        if c_saf is not None and c_int is not None:
            tally[c_int - c_saf] = tally.get(c_int - c_saf, 0) + 1
    print("  c_int - c_saf over the finite cells: " + ", ".join(
        f"{k}: {v}" for k, v in sorted(tally.items())))
    check("every winning strategy is correct on every n < N_CHECK",
          bad == 0, f"{bad} bad")
    check("c_int agrees with the earlier independent engine",
          earlier_off == 0, f"{earlier_off} cells off")
    check("the (0, 0) column: x m reads at no c <= LOOKCAP", tear_off == 0)
    check("c_int is 0 exactly where s >= (m - 1) a_max, else >= 2",
          floor_off == 0, f"{floor_off} cells off")
    check("c_saf <= c_ov at every cell with E > 0", saf_over == 0,
          f"{saf_over} cells over")
    return grid


def _fmt(c):
    return "-" if c is None else str(c)


def section_digitwise():
    print("== P4a,b the flush floor's two halves")
    bad = 0
    for name, per in PERIODIC:
        w = numeration(name, per)
        A = max(per)
        for m in maps():
            s = (m - 1) * A
            a1 = w.a[1]
            for n in range(N_CHECK):
                d = w.digits(n) + [0, 0]
                e = [m * dk for dk in d]
                e[0], carry = (m * d[0]) % a1, (m * d[0]) // a1
                e[1] += carry
                val = sum(ek * w.q(k) for k, ek in enumerate(e))
                caps = e[0] <= a1 - 1 and all(
                    e[k] <= w.a[k + 1] + s for k in range(1, len(e)))
                if val != m * n or not caps:
                    bad += 1
    check("the digitwise reader at s = (m - 1) a_max, s_0 = 0: correct",
          bad == 0, f"{bad} bad over n < {N_CHECK}")
    wrong = 0
    shown = []
    for name, per in PERIODIC:
        w = numeration(name, per)
        P = len(per)
        for m in maps():
            for phase in range(P):
                k = next(k for k in range(2, 200) if k % P == phase
                         and w.q(k - 1) > m * w.a[k + 1])
                N = m * w.a[k + 1]
                V = N * w.q(k)
                coins = [w.q(j) for j in range(k - 1, 200) if w.q(j) <= V]
                ways = [1] + [0] * V
                for q in coins:
                    for v in range(q, V + 1):
                        ways[v] += ways[v - q]
                if ways[V] != 1:
                    wrong += 1
                if len(shown) < 3:
                    shown.append(f"{name} x{m} k={k}: {V} = {N} q_{k}")
    check("m a_(k+1) q_k has exactly one string from level k - 1 (any "
          "digit sizes), e_k = m a_(k+1)", wrong == 0,
          f"{wrong} off; e.g. " + "; ".join(shown))


# ------------------------------------------------------------ P5c, P5d

def section_band():
    print("== P5d the band cells: c_ov = 1 < 2 <= c_int")
    ok = True
    cells = BAND if FULL else BAND[:1]
    for name, per, m, s in cells:
        w = numeration(name, per)
        met = Metric(w, s, s, DEPTH + 60)
        c_ov = c_overlap(met, m, DEPTH)
        src = Source(period=per)
        c_saf, _g = least(src, m, s, s, False, hi=3)
        c_int, g = least(src, m, s, s, True, hi=3)
        bad = certify(g, w, m, s, s, N_CHECK) if g else None
        print(f"    {name:12s} x{m} s = s_0 = {s}: c_ov {c_ov}  c_saf "
              f"{c_saf}  c_int {c_int}  states {len(g.states) if g else '-'}"
              f"  bad {bad}")
        ok &= (c_ov == 1 and c_saf is not None and c_saf <= 1
               and c_int == 2 and bad == 0)
    check("a strict flush price at every band cell", ok)
    if not FULL:
        return
    print("== P5c c_saf at twice the box")
    same = True
    for name, per, m, s, s0 in [("golden [1]", (1,), 3, 0, 1),
                                ("silver [2]", (2,), 2, 1, 1),
                                ("sqrt(3) - 1 [1, 2]", (1, 2), 3, 2, 2),
                                ("bronze [3]", (3,), 2, 2, 2)]:
        src = Source(period=per)
        one = least(src, m, s, s0, False, hi=6)[0]
        two = least(src, m, s, s0, False, hi=6, scale=2)[0]
        print(f"    {name:20s} x{m} ({s},{s0}): c_saf {one} at the box, "
              f"{two} at twice it")
        same &= one == two
    check("c_saf does not move when the box doubles", same)


# ------------------------------------------------------------ P6

def section_universal():
    print("== P6 the universal reader")
    rnd = random.Random(SEED + 1)
    cells = [((1, 2), 2, 1, 1, 2)]
    if FULL:
        cells += [((1, 2, 3), 2, 1, 1, 2), ((1, 2), 3, 1, 1, 3),
                  ((1, 2), 3, 2, 2, 2)]
    for alph, m, s, s0, want in cells:
        src = Source(alphabet=alph)
        t0 = time.time()
        c, g = least(src, m, s, s0, True, hi=want)
        tag = "{" + ", ".join(map(str, alph)) + "}"
        print(f"    {tag:10s} x{m} ({s},{s0}): c_int {c}  states "
              f"{len(g.states) if g else '-'}  ({time.time() - t0:.0f} s)")
        check(f"{tag} x{m} at ({s}, {s0}) reads at exactly {want}",
              c == want)
        if g is None:
            continue
        alphas = [[a] * 400 for a in alph]
        alphas += [[rnd.choice(alph) for _ in range(400)] for _ in range(12)]
        bad = 0
        for quots in alphas:
            w = Numeration("class member", quots)
            bad += certify(g, w, m, s, s0, N_CHECK // 2)
        check(f"certified at {len(alphas)} members", bad == 0, f"{bad} bad")
        if (alph, m) == ((1, 2), 2):
            g2 = Game(src, m, s, s0, want, scale=2)
            won = g2.solve(True)
            mx = my = 0
            unflushed = seeds = 0
            for quots in alphas[:6]:       # the two constant members, four random
                w = Numeration("class member", quots)
                for n in range(N_CHECK // 4):
                    out, fl, path = g2.read(w.digits(n), quots)
                    if not fl:
                        unflushed += 1
                        continue
                    x_, y_, x0 = lineage(g2, path)
                    mx, my = max(mx, x_), max(my, y_)
                    seeds += x0 != m * w.digits(n)[0]
            check("at twice the box the flushing lineages stay in the box",
                  won and mx <= g.bx and my <= g.by and unflushed == seeds == 0,
                  f"largest |g|, |h| = {mx}, {my} against ({g.bx}, {g.by}), "
                  f"6 members, n < {N_CHECK // 4}, {unflushed} unflushed")
            del g2
        del g
    if not FULL:
        return
    print("== P6 the periodic members of {1, 2} for x 3 at (1, 1)")
    necks = necklaces((1, 2), 8)
    off = []
    for per in necks:
        c, _g = least(Source(period=per), 3, 1, 1, True, hi=3)
        if c != 2:
            off.append((per, c))
    check("every purely periodic alpha of primitive period <= 8 reads "
          "at 2", not off, f"{len(necks)} alphas (every rotation of "
          f"{len(set(min(tuple(p[i:] + p[:i]) for i in range(len(p))) for p in necks))}"
          f" words), off: {off}")


def necklaces(alph, top):
    out = []
    for P in range(1, top + 1):
        seen = set()
        for k in range(len(alph) ** P):
            word = []
            for _ in range(P):
                k, r = divmod(k, len(alph))
                word.append(alph[r])
            rots = [tuple(word[i:] + word[:i]) for i in range(P)]
            if len(set(rots)) < P or min(rots) in seen:
                continue
            seen.add(min(rots))
            out.extend(rots)
    return out


# ------------------------------------------------------------ main

def main():
    t0 = time.time()
    section_ranges()
    section_controls()
    section_tear()
    cov = section_completion()
    section_floors()
    section_grid(cov)
    section_digitwise()
    section_band()
    section_universal()
    n_ok = sum(CHECKS)
    print(f"\n{n_ok} of {len(CHECKS)} checks passed "
          f"({time.time() - t0:.1f} s{', full' if FULL else ''})")
    sys.exit(0 if n_ok == len(CHECKS) else 1)


if __name__ == "__main__":
    main()
