"""Does a bounded cell's excess column have a limit, and is the measured
column it? The carry automaton at a periodic window, and the limit
column read off it exactly.

THE QUESTION
------------
The run-length rule (explore_cascade_rule.py H3) reads a digit shift's
excess column c(t) = A(t) - t + 1 at one table and gates a run that
outlasts the window's period. Every verdict it issues is a reading at a
range N: the column is monotone in N (explore_cascade_rule.py D6), the
trusted bounded population's (longest run, peak) histogram is identical
at N = 100000 and 300000 while the gated maxima rise
(explore_saturation_twins.py F6), and whether that population's
spectrum has a LIMIT in the range -- and whether the identical histogram
is that limit -- was not derived. This rig derives the limit column from
the window's own structure and computes it exactly, cell for cell, at
every periodic population the rule's verdicts stand on.

THE HAND-ATTACK (pre-engine, on paper)
--------------------------------------
Window purely periodic, a_{k+P} = a_k. Convergents q_{-1} = 0, q_0 = 1,
p_{-1} = 1, p_0 = 0, both on the recurrence x_k = a_k x_{k-1} + x_{k-2};
theta_k = q_k alpha - p_k (theta_{-1} = -1, theta_0 = alpha), signs
alternating, |theta_k| < 1/q_{k+1}.

D1  SELF-SIMILARITY. As row vectors (theta_k, theta_{k-1}) =
    (theta_{k-1}, theta_{k-2}) [[a_k, 1], [1, 0]], so one period carries
    (alpha, -1) to (alpha, -1) M_0 with M_0 = [[q_P, q_{P-1}], [p_P,
    p_{P-1}]] (a zero integer part swaps p and q in the convergent
    matrix). Pure periodicity is exactly (alpha, -1) being a left
    eigenvector: eta = p_{P-1} - q_{P-1} alpha = -theta_{P-1}, alpha a
    root of q_{P-1} x^2 + (q_P - p_{P-1}) x - p_P. By induction on the
    shared recurrence from k = -1, 0: theta_{k+P} = eta theta_k for
    EVERY k >= -1. |eta| < 1 and its conjugate |eta'| > 1, N(eta) = +-1.
    On the lattice L = Z + Z alpha, written u + w alpha, eta acts by the
    integer matrix H = [[p_{P-1}, -p_P], [-q_{P-1}, q_P]] of determinant
    (-1)^P: L is not a ring, but eta L = L. (Checked exactly below:
    H (-p_k, q_k) = (-p_{k+P}, q_{k+P}) as integers.)
D2  STAR VALUES. A legal string d has n = sum d_k q_k and n* = sum d_k
    theta_k = n alpha - m. The extremes telescope (a_{k+1} theta_k =
    theta_{k+1} - theta_{k-1}): the even-maximal string tends to 1 -
    alpha, the odd-maximal to -alpha, so n* in (-alpha, 1 - alpha) and
    m is a function of n. Two strings whose star values differ by an
    INTEGER have the same value (alpha irrational), so "sum (e_i -
    d'_i) theta_i in Z" says val(e) = val(d'), and a legal e with that
    property IS the greedy string of val(d').
D3  THE SHIFT. sigma_r(d) = greedy(v), v = sum d_k q_{k+r} = val(d')
    with d' = 0^r d. Its pseudo-star v° = sum d_k theta_{k+r} obeys |v°|
    <= sum a_{k+1} |theta_k| = 1 + alpha, so the integer m = v* - v°
    has |m| <= 2.
D4  THE CARRY IS FINITE. Read (d'_k, e_k) from the bottom and keep D_k =
    sum_{i<k} (e_i - d'_i) theta_i - m in L; the pair is accepted iff
    D = 0 at the end. On an accepting run D_k = -sum_{i>=k} (e_i -
    d'_i) theta_i, so C_k = D_k / theta_k is bounded in R (a legal
    output tail is at most |theta_{k-1}| + |theta_k|, the input tail at
    most A_max sum_{i>=k} |theta_i|), and its conjugate C_k' =
    (sum_{i<k} (e_i - d'_i) theta_i' - m) / theta_k' is bounded because
    theta_i' grows like q_i. C_k lies in theta_k^{-1} L = theta_{k mod
    P}^{-1} L (eta being a unit of L), a lattice: finitely many carries
    per phase. Normalized state E_k = D_k eta^{-floor(k/P)} in L, with
    E_{k+1} = E_k + (e_k - d'_k) theta_{k mod P} and eta^{-1} applied
    whenever k + 1 = 0 mod P; a state is (position class, E, the two
    previous-digit-zero bits). So {(d, sigma_r d)} is recognized by a
    finite synchronous automaton at every purely periodic window and
    every stride, with nothing imported: the base 1/eta is a Pisot
    unit and this is the classical bounded-carry argument (Frougny's
    normalization theorem is its Zeckendorf case).
D5  THE LIMIT COLUMN. A_N(t) is the largest agreement depth over pairs
    n1, n2 < N whose images differ below t (the consecutive-sorted-pair
    maximum equals the all-pair maximum: strings sharing a prefix form
    a contiguous lexicographic block, and an image difference between
    its ends falls on some consecutive pair). It is monotone in N, so
    A_inf(t) = sup_N A_N(t) exists in N u {inf}, and monotone in t, so
    A_inf is infinite from some depth on or finite everywhere. On the
    pair automaton (s1, s2) driven by a COMMON input: R_t = pairs
    reachable at position t by t agreeing steps whose outputs have
    differed below t; F(s) = the longest agreeing-input path from s
    (infinite on a cycle). Agreement in d below p is agreement in d'
    below p + r, so A_inf(t) >= p iff some s in R_t has F(s) >= p + r -
    t, and
        c_inf(t) = max(0, max_{s in R_t} F(s) - r + 1).
    R_t is a subset sequence under one fixed set map, hence EVENTUALLY
    PERIODIC, and c_inf with it. The paper gives existence and eventual
    periodicity; the depth, the period and the values are the pair
    automaton's, computed per cell, and whether the period is P is a
    prediction and not a derivation.
D6  WHAT THE RULE'S VERDICTS SAY IN THE LIMIT. c_N <= c_inf at every t,
    so a finite-range bounded verdict is a LOWER reading: the limit can
    be gated where the reading was bounded and never the reverse, and
    an identical histogram at two ranges is evidence about the limit
    only if the limit column's preperiod sits inside the measured
    depth, which the automaton prints.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS,
never what they would mean)
  C1 (the positive control, run FIRST; nothing below is read if it is
      red) at the golden window, the designed window P = 3, A = 2 and
      the graded window (8, 4), at strides 1..3: every n < 5000 has its
      engine image accepted by the automaton, and for every n < 300 the
      automaton accepts EXACTLY ONE output string, the engine's. And the
      exact self-test H (-p_k, q_k) = (-p_{k+P}, q_{k+P}) holds for k =
      -1 .. 3P at every window read.
  C2 (a proved control) at every designed window, r = P and r = 2P print
      a limit column identically 0: the shifted string is legal, so the
      map is the bare coordinate map.
  C3 (consistency) at every cell read, the engine's column at N = 30000
      sits at or below the limit column at every depth in its table.
  P1 the designed family P = 3, 4, 5 and A = 2, 3, 5, strides 1..2P: the
      residue law in the limit -- r = 0 mod P identically 0; r mod P odd
      infinite from some depth; r mod P even and nonzero finite at every
      depth, eventually periodic with period P, longest run below P.
  P2 the value grid (92 cells, r = 3): the 18 cells the value law bounds
      print finite columns of period 6 with (longest run, peak) = (5, 5)
      at every one; the 74 it gates print infinite columns.
  P3 the graded map (210 cells, r = 2): every column finite with period
      6, and the (longest run, peak) histogram (0, 0) x 18, (1, 1) x 17,
      (3, 3) x 175 -- the N = 300000 histogram, now as the limit.
  P4 at every finite cell the preperiod (the depth from which the column
      is periodic) is below 10, the shallowest deepest-range table.
  KILL (observable): a cell the rule bounds at N = 300000 whose limit
      column is infinite, carries a run >= P, a peak >= 6, or a (run,
      peak) off the recorded histogram; or a gated cell with a finite
      limit; or a finite cell whose period is not P; or a preperiod at
      or above the measured depth.

THE DESIGN
----------
The window builder, digits and greedy normalization are imported from
explore_shift_repair.py and explore_cascade_span.py; the finite columns
for C3 come from explore_cascade_rule.py's cell(), so the limit column is
compared with the column the rule reads and not a reimplementation. The
automaton is built by forward search from the initial carries -m, m =
-3..3, over every legal digit pair, pruned by D4's box (a state outside
it lies on no accepting run, so pruning is exact and a generous box
costs only size), then trimmed to the states from which an accepting
state is reachable. The pair automaton is closed under agreeing inputs
from all pairs of initial states, tracking whether the outputs have
differed; F is a longest-path with cycle detection over that closure.
Stages run one at a time (argv: s0 controls, s1 designed, s2 value, s3
graded, s4 explicit witnesses at the value law's bounded cells, s5 every
stride at the graded grid, s6 the box re-read at three times the
slack); every stage prints per-cell timing, automaton size and pair
closure size.

FINDINGS (each at its own tier)

L1  THE CONTROLS ARE GREEN AND THE AUTOMATA ARE SMALL. C1: at the
    golden, designed (3, 2) and graded (8, 4) windows at strides 1..3,
    5000 of 5000 engine pairs accepted and 300 of 300 inputs with
    exactly one accepted output; D1's exact identity holds at every k
    at every window read (0 mismatches), and the trimmed automata run
    4 to 105 states (graded (8, 4) r = 1: 105 states from 648 forward).
    C2: every r = P and r = 2P at the designed family prints the zero
    column. C3: the engine's N = 30000 column sits at or below the
    limit column at every depth of every cell of the three populations
    (0 violations over the designed family, the value grid and the
    graded map; s5's other strides were not checked). The box is
    not the verdict (s6): re-read at three times the slack, 0 of 302
    cells move and no trimmed automaton changes size. A cell costs well
    under a second.
L2  THE LIMIT EXISTS AND THE RECORDED HISTOGRAM IS IT (theorem for the
    existence and eventual periodicity, D4-D5, at every purely periodic
    window and stride; rule at the cells read for the values). The
    graded map's 210 cells at r = 2 are finite at every depth, periodic
    with period 6 (period 1 for the 18 zero columns), preperiod at most
    3, and their (longest run, peak) histogram is (0, 0) x 18, (1, 1) x
    17, (3, 3) x 175: the N = 300000 histogram, entry for entry, now as
    the limit -- P3 and P4 confirmed.
L3  THE VALUE LAW IS A FINITE-RANGE READING: EVERY UNEQUAL PAIR GATES AT
    THE HALF-PERIOD STRIDE (rule, exact at the 92 cells of the value
    grid and the 210 of the graded map; the KILL fixed above fires at
    all 18 cells the law bounded). At r = 3 every cell with A != B
    prints an infinite column from t = 4 -- the twelve bounded cells
    of the 8 x 8 grid, (8, 4) and (9, 7) and (9, 8) among them, and the
    six of the extended rows alike -- and the diagonal A = B prints the
    zero column (period 3, the shift is the period shift).
    The gate is EXPLICIT and checked with the engine's own digits (s4):
    at (8, 4), n1 = 1638 and n2 = 364170 agree on 10 digits and their
    images differ at position 3, so A(4) >= 10 and c(4) >= 7 at any
    range holding both -- the first such pair sits just past N =
    300000, which is why three ranges read 5 4 3 2 1 there; one turn
    of the pair automaton's 6-cycle later n2 = 66277120 at agreement
    16, then 12062071850 at agreement 22. The same ladder, agreement
    4, 10, 16, 22 with the cycle of length 6, prints at all six cells
    exhibited. So the roof, the floor and the product threshold were
    statements about how deep the FIRST witness sits against the range
    read, never about boundedness, and the (5, 5) the trusted bounded
    corpus was thought to top out at was the first bump of a gated
    column.
L4  THE PARITY LAW AT THE LARGENESS SCALE IS THE WHOLE LIMIT MAP OF THE
    GRADED WINDOW (rule at scanned scope, 210 cells x 8 strides, 0 off).
    Read against the scale 3 at which the large quotients recur: r = 1,
    4, 7 gated at every cell; r = 2, 5, 8 finite at every cell (zero at
    some); r = 6 zero at every cell; and r = 3, the half-period, gated
    at every cell with A != B and zero at the 9 with A = B. The four
    verdict vectors over strides 1..8 are GbGGb.G. (109 cells),
    GbGG..G. (83), G.GG..G. (9) and G..G..G. (9, the diagonal). The
    residue law of the designed family also holds in the limit at all
    54 strides of its nine windows (s1): r = 0 mod P zero, odd residues
    infinite, even nonzero residues finite -- 12 of them nonzero
    columns of period P with (run, peak) at most (2, 2), the others
    identically zero.
L5  THE BOUNDED CORPUS'S CEILING IN THE LIMIT IS (4, 4). Over every
    finite nonzero column at the graded grid: r = 2 prints (1, 1) at
    17 cells and (3, 3) at 175; r = 5 prints (3, 3) at 106 and (4, 4)
    at 3; the designed family's tops at (2, 2). The calibration
    constant one past the bounded ceiling is therefore 5, and the
    aperiodic split it reproduces (explore_saturation_twins.py F5:
    gated strides at peaks 7 and above, bounded ones at 3 or below)
    is reproduced by any constant from 5 to 7 -- three values of
    margin, the ceiling now exact rather than measured at three
    ranges. The threshold stays calibration at the two aperiodic
    windows, which have no period and so no automaton.
L6  WHAT THE RUN-LENGTH RULE IS, SEEN FROM THE LIMIT. Its gated verdicts
    are final (the column is monotone in N, so a run that has outlasted
    the period stays); its bounded verdicts are LOWER READINGS, open to
    the next range, and no scale repairs that: the sequence period 6
    reads (8, 4) at r = 3 bounded where the limit gates it, and the
    largeness scale 3 would read the 175 cells with run 3 at r = 2
    gated where the limit bounds them. At a periodic window the
    decision is the automaton's, at a cost below a second; the rule
    keeps its use where there is no period, as the reading the
    calibration constant is added to.

SETTLED LATER (explore_limit_maps.py L6, the same automaton run over the
two-class family): L5's (4, 4) is the ceiling of the corpus read HERE
and not of periodic windows -- two cells of that family print a finite
column whose cycle 5 4 3 2 1 never returns to 0, peak 5, so the constant
one past the bounded ceiling is 6, with two values of margin. And L6's
"gated verdicts are final" holds of the RUN, which stays, and not of the
verdict: the run-length rule reads both sawtooth cells gated where the
limit is bounded, so its gated half is a finite-table reading too.

RUN RECORD (the estimate first, then what it cost)
Unmeasured before s0. s0 1.7 s (the controls and four timed cells); s1
38.3 s and s3 52.6 s, all of it the engine's N = 30000 columns for C3
(the automata and limit columns together cost 0.0 s per cell at the
print's resolution); s2 inside the same run; s4 0.0 s; s5 8.7 s over
1680 cells; s6 3.5 s over 604 reads. Pure Python, standard library,
memory far below the ceiling. Every stage is bounded and rerunnable in
under a minute; s5 was run twice, once against the residue reading at
scale 6 (429 cells off, the wrong scale) and once against the largeness
scale (0 off), and s1 and s2 twice, the first prints flagging zero
columns and delay-0 cells as off laws that allow them (19 and 4 false
reds), the second 0 off at s1 and the 18 bounded-label cells at s2 --
the comparisons being the prints' and not the verdicts', which did not
move.
"""

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_shift_repair import (          # noqa: E402
    build_q_positions,
    designed,
    greedy,
)
from explore_cascade_span import WANT, graded    # noqa: E402
from explore_cascade_rule import (              # noqa: E402
    PERIOD,
    cell,
    law_says,
    window,
)
from explore_saturation_twins import VALUE_GRID  # noqa: E402

M_RANGE = range(-3, 4)      # D3: |m| <= 2, one of slack each side
SLACK = 1.05                # box slop over D4's float bounds
NPOS = 48                   # weight positions built for the controls
INF = float("inf")


# ------------------------------------------------------------ the window

class Window:
    """A purely periodic window: its period matrix, eta, and D4's box."""

    def __init__(self, caps, period):
        self.P = period
        self.a = list(caps[:period])          # a[phi] = a_{phi+1}
        assert all(caps[k] == self.a[k % period]
                   for k in range(min(len(caps), 6 * period)))
        P = period
        # convergents from k = -1 to 3P (exact)
        q = {-1: 0, 0: 1}
        p = {-1: 1, 0: 0}
        for k in range(1, 3 * P + 1):
            ak = self.a[(k - 1) % P]
            q[k] = ak * q[k - 1] + q[k - 2]
            p[k] = ak * p[k - 1] + p[k - 2]
        self.q, self.p = q, p
        # alpha and its conjugate from D1's quadratic
        A2, A1, A0 = q[P - 1], q[P] - p[P - 1], -p[P]
        disc = A1 * A1 - 4 * A2 * A0
        r1 = (-A1 + disc ** 0.5) / (2 * A2)
        r2 = (-A1 - disc ** 0.5) / (2 * A2)
        qq = build_q_positions(list(caps), 60)
        approx = None
        # a deep convergent ratio: p_K/q_K with the p's rebuilt
        pk2, pk1 = 1, 0
        for k in range(1, 61):
            pk2, pk1 = pk1, caps[k - 1] * pk1 + pk2
            if k == 60:
                approx = pk1 / qq[60]
        self.alpha = r1 if abs(r1 - approx) < abs(r2 - approx) else r2
        self.alpha_c = r2 if self.alpha == r1 else r1
        assert abs(self.alpha - approx) < 1e-9, (self.alpha, approx)
        # eta = -theta_{P-1}, as a lattice matrix H on (u, w)
        self.H = ((p[P - 1], -p[P]), (-q[P - 1], q[P]))
        det = self.H[0][0] * self.H[1][1] - self.H[0][1] * self.H[1][0]
        assert det in (1, -1)
        self.Hinv = ((det * q[P], det * p[P]), (det * q[P - 1], det * p[P - 1]))
        self.eta = p[P - 1] - q[P - 1] * self.alpha
        self.eta_c = p[P - 1] - q[P - 1] * self.alpha_c
        assert abs(self.eta) < 1 < abs(self.eta_c), (self.eta, self.eta_c)
        # theta_phi as lattice coordinates and as floats, phases -1..P-1
        self.th = {phi: (-p[phi], q[phi]) for phi in range(-1, P)}
        self.thf = {phi: q[phi] * self.alpha - p[phi] for phi in range(-1, P)}
        self.thc = {phi: q[phi] * self.alpha_c - p[phi]
                    for phi in range(-1, P)}

    def self_test(self):
        """D1 exactly: H (-p_k, q_k) = (-p_{k+P}, q_{k+P}), k = -1..2P."""
        bad = 0
        for k in range(-1, 2 * self.P + 1):
            u, w = -self.p[k], self.q[k]
            u2 = self.H[0][0] * u + self.H[0][1] * w
            w2 = self.H[1][0] * u + self.H[1][1] * w
            if (u2, w2) != (-self.p[k + self.P], self.q[k + self.P]):
                bad += 1
        return bad

    def real(self, u, w):
        return u + w * self.alpha

    def conj(self, u, w):
        return u + w * self.alpha_c

    def box(self, amax):
        """D4's bounds on C_k = E_k/theta_phi per phase (real, conj)."""
        P = self.P
        eta, etac = abs(self.eta), abs(self.eta_c)
        T = sum(abs(self.thf[phi]) for phi in range(P))
        Tc = sum(abs(self.thc[phi]) for phi in range(P))
        real, conj = {}, {}
        for phi in range(P):
            th = abs(self.thf[phi])
            tail = (sum(abs(self.thf[psi]) for psi in range(phi, P))
                    + eta / (1 - eta) * T)
            real[phi] = ((abs(self.thf[phi - 1]) + th) / th
                         + amax * tail / th)
            thc = abs(self.thc[phi])
            head = Tc / (etac - 1) + sum(abs(self.thc[psi])
                                         for psi in range(phi))
            conj[phi] = 2 * amax * head / thc + 3 / thc
        return real, conj

    def apply_hinv(self, u, w):
        return (self.Hinv[0][0] * u + self.Hinv[0][1] * w,
                self.Hinv[1][0] * u + self.Hinv[1][1] * w)


# --------------------------------------------------------- the automaton

class Shift:
    """The carry automaton of sigma_r at a window (D4), trimmed."""

    def __init__(self, win, r):
        self.win, self.r, self.P = win, r, win.P
        P, a = win.P, win.a
        self.amax = max(a)
        breal, bconj = win.box(self.amax)
        self.breal = {phi: breal[phi] * SLACK + 1 for phi in range(P)}
        self.bconj = {phi: bconj[phi] * SLACK + 1 for phi in range(P)}
        self.init = [(0, -m, 0, True, True) for m in M_RANGE]
        self.trans = {}         # state -> list of (x, y, state')
        self.build()

    def npos(self, pos):
        r, P = self.r, self.P
        if pos < r:
            return pos + 1
        if pos == r:
            return r + 1
        return r + 1 + ((pos - r) % P)

    def inbox(self, u, w, phi):
        win = self.win
        return (abs(win.real(u, w) / win.thf[phi]) <= self.breal[phi]
                and abs(win.conj(u, w) / win.thc[phi]) <= self.bconj[phi])

    def step(self, s):
        """Every legal (x, y) successor of s inside the box."""
        pos, u, w, pze, pzd = s
        r, P, a, win = self.r, self.P, self.win.a, self.win
        phi = pos % P
        cap_e = a[phi]
        if pos == 0:
            ys = range(0, a[0])
        else:
            ys = range(0, cap_e + 1)
        if pos < r:
            xs = (0,)
        elif pos == r:
            xs = range(0, a[0])
        else:
            xs = range(0, a[(pos - r) % P] + 1)
        cap_d = a[(pos - r) % P] if pos > r else None
        tu, tw = win.th[phi]
        npos = self.npos(pos)
        wrap = (phi + 1 == P)
        nphi = (phi + 1) % P
        out = []
        for y in ys:
            if pos > 0 and y == cap_e and not pze:
                continue
            for x in xs:
                if cap_d is not None and x == cap_d and not pzd:
                    continue
                d = y - x
                u2, w2 = u + d * tu, w + d * tw
                if wrap:
                    u2, w2 = win.apply_hinv(u2, w2)
                if not self.inbox(u2, w2, nphi):
                    continue
                out.append((x, y, (npos, u2, w2, y == 0, x == 0)))
        return out

    def build(self):
        seen = set(self.init)
        todo = list(self.init)
        while todo:
            s = todo.pop()
            succ = self.step(s)
            self.trans[s] = succ
            for _x, _y, s2 in succ:
                if s2 not in seen:
                    seen.add(s2)
                    todo.append(s2)
        self.n_forward = len(seen)
        # trim: keep states from which an accepting (E = 0) state is reachable
        rev = {}
        for s, succ in self.trans.items():
            for _x, _y, s2 in succ:
                rev.setdefault(s2, []).append(s)
        good = set(s for s in seen if s[1] == 0 and s[2] == 0)
        todo = list(good)
        while todo:
            s = todo.pop()
            for s0 in rev.get(s, ()):
                if s0 not in good:
                    good.add(s0)
                    todo.append(s0)
        self.states = good
        self.trans = {s: [t for t in succ if t[2] in good]
                      for s, succ in self.trans.items() if s in good}
        self.init = [s for s in self.init if s in good]
        # by input digit, for the pair closure
        self.byx = {}
        for s, succ in self.trans.items():
            d = {}
            for x, y, s2 in succ:
                d.setdefault(x, []).append((y, s2))
            self.byx[s] = d

    # ---- acceptance of one pair (control C1)

    def accepts(self, dprime, e):
        cur = set(self.init)
        L = max(len(dprime), len(e))
        for k in range(L):
            x = dprime[k] if k < len(dprime) else 0
            y = e[k] if k < len(e) else 0
            nxt = set()
            for s in cur:
                for yy, s2 in self.byx.get(s, {}).get(x, ()):
                    if yy == y:
                        nxt.add(s2)
            cur = nxt
            if not cur:
                return False
        return any(s[1] == 0 and s[2] == 0 for s in cur)

    def outputs(self, dprime, L):
        """Every output of length L accepted on input dprime (padded)."""
        found = []
        xs = [dprime[k] if k < len(dprime) else 0 for k in range(L)]

        def rec(k, s, acc):
            if k == L:
                if s[1] == 0 and s[2] == 0:
                    found.append(tuple(acc))
                return
            for y, s2 in self.byx.get(s, {}).get(xs[k], ()):
                acc.append(y)
                rec(k + 1, s2, acc)
                acc.pop()
        for s in self.init:
            rec(0, s, [])
        return set(found)


# ------------------------------------------------------ the limit column

def limit_column(sh, tmax_print=60):
    """c_inf(t) off the pair automaton (D5).

    Returns dict(col=[c(0..)], inf_from=t0 or None, pre=preperiod,
    per=period of the set sequence, cper=minimal period of c, pairs=size
    of the agree closure).
    """
    r = sh.r
    byx = sh.byx

    succ, F = closure(sh)

    def f_of(pair):
        return F[pair]

    U = frozenset((i, j) for i in sh.init for j in sh.init)
    R = frozenset()
    seen = {(U, R): 0}
    col = []
    inf_from = None
    t = 0
    while True:
        # c(t)
        if R:
            m = 0
            for pair in R:
                fv = f_of(pair)
                if fv == INF:
                    m = INF
                    break
                if fv > m:
                    m = fv
            c = INF if m == INF else max(0, m - r + 1)
        else:
            c = 0
        col.append(c)
        if c == INF:
            inf_from = t
            break
        # advance
        U2, R2 = set(), set()
        for (s1, s2) in U:
            d1, d2 = byx[s1], byx[s2]
            for x, l1 in d1.items():
                l2 = d2.get(x)
                if not l2:
                    continue
                for y1, t1 in l1:
                    for y2, t2 in l2:
                        (U2 if y1 == y2 else R2).add((t1, t2))
        for (s1, s2) in R:
            d1, d2 = byx[s1], byx[s2]
            for x, l1 in d1.items():
                l2 = d2.get(x)
                if not l2:
                    continue
                for _y1, t1 in l1:
                    for _y2, t2 in l2:
                        R2.add((t1, t2))
        U, R = frozenset(U2), frozenset(R2)
        t += 1
        key = (U, R)
        if key in seen:
            pre, per = seen[key], t - seen[key]
            break
        seen[key] = t
        if t > 4000:
            raise RuntimeError("no cycle within 4000 depths")
    if inf_from is not None:
        return dict(col=col, inf_from=inf_from, pre=None, per=None,
                    cper=None, pairs=len(F))
    # the periodic part of c: col[pre:pre+per] repeats
    cyc = col[pre:pre + per]
    cper = per
    for d in range(1, per + 1):
        if per % d == 0 and all(cyc[i] == cyc[i % d] for i in range(per)):
            cper = d
            break
    # minimal preperiod of c itself
    cpre = pre
    while cpre > 0 and col[cpre - 1] == cyc[(cpre - 1 - pre) % per]:
        cpre -= 1
    return dict(col=col, inf_from=None, pre=cpre, per=per, cper=cper,
                pairs=len(F))


def closure(sh):
    """The agree closure of the pair automaton from all initial pairs,
    and F on it: INF for a node that reaches a cycle, else the longest
    agreeing path (an iterative Tarjan hands the DAG part out in reverse
    topological order). succ[pair] = list of (x, next pair)."""
    byx = sh.byx

    def agree_succ(pair):
        s1, s2 = pair
        d1, d2 = byx[s1], byx[s2]
        out = []
        for x, l1 in d1.items():
            l2 = d2.get(x)
            if not l2:
                continue
            for _y1, t1 in l1:
                for _y2, t2 in l2:
                    out.append((x, (t1, t2)))
        return out

    succ = {}
    roots = [(i, j) for i in sh.init for j in sh.init]
    todo = list(roots)
    for pr in roots:
        succ[pr] = None
    while todo:
        pr = todo.pop()
        nx = agree_succ(pr)
        succ[pr] = nx
        for _x, q in nx:
            if q not in succ:
                succ[q] = None
                todo.append(q)
    F = {}
    index, low, onstack, stack = {}, {}, set(), []
    counter = 0
    for root in succ:
        if root in index:
            continue
        work = [(root, 0)]
        while work:
            v, i = work[-1]
            if i == 0:
                index[v] = low[v] = counter
                counter += 1
                stack.append(v)
                onstack.add(v)
            nx = succ[v]
            if i < len(nx):
                work[-1] = (v, i + 1)
                w = nx[i][1]
                if w not in index:
                    work.append((w, 0))
                elif w in onstack:
                    low[v] = min(low[v], index[w])
                continue
            work.pop()
            if work:
                u = work[-1][0]
                low[u] = min(low[u], low[v])
            if low[v] == index[v]:
                comp = []
                while True:
                    w = stack.pop()
                    onstack.discard(w)
                    comp.append(w)
                    if w == v:
                        break
                cyclic = len(comp) > 1 or any(q == v for _x, q in succ[v])
                for w in comp:
                    if cyclic:
                        F[w] = INF
                    else:
                        best = 0
                        for _x, q in succ[w]:
                            fq = F[q]
                            if fq == INF:
                                best = INF
                                break
                            if fq + 1 > best:
                                best = fq + 1
                        F[w] = best
    return succ, F


def witness(sh, t, turns, q):
    """Two integers agreeing on a prefix that grows with `turns` whose
    images under the shift differ below t -- the gate made explicit.

    Walks the pair automaton to a pair at position t whose outputs have
    differed and whose F is infinite, on to a cycle of agreeing inputs,
    around it `turns` times, then completes each run to acceptance on
    its own. Returns (n1, n2, agreement in d, first image difference,
    cycle length).
    """
    succ, F = closure(sh)
    byx = sh.byx
    layer = {((i, j), False): None for i in sh.init for j in sh.init}
    parent = dict(layer)
    for _k in range(t):
        nxt = {}
        for (pair, diff) in layer:
            s1, s2 = pair
            d1, d2 = byx[s1], byx[s2]
            for x, l1 in d1.items():
                l2 = d2.get(x)
                if not l2:
                    continue
                for y1, t1 in l1:
                    for y2, t2 in l2:
                        key = ((t1, t2), diff or y1 != y2)
                        if key not in parent:
                            parent[key] = ((pair, diff), x)
                            nxt[key] = None
        layer = nxt
    cands = [k for k in layer if k[1] and F[k[0]] == INF]
    if not cands:
        return None
    start = cands[0]
    prefix = []
    key = start
    while parent[key] is not None:
        prev, x = parent[key]
        prefix.append(x)
        key = prev
    prefix.reverse()
    path, onpath, pos = [], {}, start[0]
    while pos not in onpath:
        onpath[pos] = len(path)
        for x, qq in succ[pos]:
            if F[qq] == INF:
                path.append((x, qq))
                pos = qq
                break
    i0 = onpath[pos]
    lead = [x for x, _q in path[:i0]]
    cyc = [x for x, _q in path[i0:]]
    common = prefix + lead + cyc * turns
    end1, end2 = pos

    def complete(s0):
        par = {s0: None}
        todo = [s0]
        while todo:
            u = todo.pop(0)
            if u[1] == 0 and u[2] == 0:
                out = []
                while par[u] is not None:
                    u0, x = par[u]
                    out.append(x)
                    u = u0
                return out[::-1]
            for x, l in byx[u].items():
                for _y, v in l:
                    if v not in par:
                        par[v] = (u, x)
                        todo.append(v)
        raise RuntimeError("no completion")
    dp1 = common + complete(end1)
    dp2 = common + complete(end2)
    r = sh.r
    L = max(len(dp1), len(dp2)) + 2
    dp1 = dp1 + [0] * (L - len(dp1))
    dp2 = dp2 + [0] * (L - len(dp2))
    n1 = sum(dp1[k] * q[k - r] for k in range(r, L) if dp1[k])
    n2 = sum(dp2[k] * q[k - r] for k in range(r, L) if dp2[k])
    d1, d2 = greedy(n1, q), greedy(n2, q)
    assert d1[:L - r] == dp1[r:], "run 1 is not the greedy string"
    assert d2[:L - r] == dp2[r:], "run 2 is not the greedy string"
    e1 = greedy(sum(d1[k] * q[k + r] for k in range(len(q) - r) if d1[k]), q)
    e2 = greedy(sum(d2[k] * q[k + r] for k in range(len(q) - r) if d2[k]), q)
    agree = 0
    while agree < len(d1) and d1[agree] == d2[agree]:
        agree += 1
    diff = 0
    while diff < len(e1) and e1[diff] == e2[diff]:
        diff += 1
    return n1, n2, agree, diff, len(cyc)



def run_peak(lc):
    """(longest run, peak) of the limit column; INF where unbounded."""
    if lc["inf_from"] is not None:
        return INF, INF
    col, pre, per = lc["col"], lc["pre"], lc["per"]
    cyc = col[pre:pre + per]
    if all(c > 0 for c in cyc):
        return INF, max(col)
    seq = col[:pre] + cyc * 3
    longest = run = 0
    for c in seq:
        run = run + 1 if c > 0 else 0
        longest = max(longest, run)
    return longest, max(seq)


def show_col(lc, upto=40):
    col = lc["col"]
    s = " ".join("*" if c == INF else str(c) for c in col[:upto])
    if lc["inf_from"] is not None:
        return s + f"   (infinite from t = {lc['inf_from']})"
    return s + f"   (pre {lc['pre']}, period {lc['cper']})"


def finite_column(caps, period, r, n=30_000):
    """The engine's column at range n (explore_cascade_rule.py cell)."""
    rows = cell(caps, n, r, period)
    row = rows[r]
    A, tmax = row["A"], row["tmax"]
    return [max(0, A[t] - t + 1) for t in range(1, tmax + 1)], row["repairs"]


def read_cell(name, caps, period, r, check_finite=True, verbose=True):
    t0 = time.time()
    win = Window(caps, period)
    sh = Shift(win, r)
    t1 = time.time()
    lc = limit_column(sh)
    t2 = time.time()
    lr, pk = run_peak(lc)
    fin_ok = None
    if check_finite:
        fcol, _rep = finite_column(caps, period, r)
        # finite column c(t) indexes t = 1..tmax; limit col index t
        fin_ok = all(fcol[t - 1] <= lc["col"][t]
                     if t < len(lc["col"]) else True
                     for t in range(1, len(fcol) + 1))
        # a finite column that runs past the limit's computed prefix
        # cannot be checked there; the limit's periodic part extends it
        if lc["inf_from"] is None:
            ext = lc["col"][:]
            while len(ext) <= len(fcol) + 1:
                ext.append(ext[lc["pre"] + (len(ext) - lc["pre"]) % lc["per"]])
            fin_ok = all(fcol[t - 1] <= ext[t] for t in range(1, len(fcol) + 1))
    if verbose:
        print(f"  {name} r {r}: states {len(sh.states):5d} (fwd "
              f"{sh.n_forward:6d}) pairs {lc['pairs']:7d}  build "
              f"{t1 - t0:5.1f}s limit {t2 - t1:5.1f}s"
              f"  run/peak {lr}/{pk}"
              + ("" if fin_ok is None else
                 f"  finite<=limit {'OK' if fin_ok else 'VIOLATED'}"))
        print(f"      c_inf: {show_col(lc)}")
    return dict(lc=lc, run=lr, peak=pk, states=len(sh.states),
                pairs=lc["pairs"], fin_ok=fin_ok, sh=sh)


# ------------------------------------------------------------------ s0

def s0_controls():
    print("=" * 78)
    print("S0 CONTROLS: the exact self-test, acceptance, uniqueness (C1),"
          " and the proved delay-0 stride (C2)")
    wins = [("golden [1]", [1] * WANT, 1),
            ("designed P3 A2", designed(3, 2, WANT), 3),
            ("graded (8,4)", window(8, 4), PERIOD)]
    allok = True
    for name, caps, P in wins:
        win = Window(caps, P)
        bad = win.self_test()
        print(f"{name}: P {P} alpha {win.alpha:.9f} eta {win.eta:+.6f}"
              f" eta' {win.eta_c:+.4f}  D1 exact mismatches {bad}")
        allok &= (bad == 0)
        q = build_q_positions(list(caps), NPOS)
        for r in (1, 2, 3):
            sh = Shift(win, r)
            acc = uniq = 0
            for n in range(5000):
                d = greedy(n, q)
                dp = [0] * r + d[:len(q) - r]
                v = sum(d[k] * q[k + r] for k in range(len(q) - r) if d[k])
                e = greedy(v, q)
                if sh.accepts(dp, e):
                    acc += 1
                if n < 300:
                    L = max(i for i in range(len(dp)) if dp[i] or e[i]) + 4 \
                        if any(dp) else 4
                    outs = sh.outputs(dp, L)
                    if outs == {tuple(e[:L])}:
                        uniq += 1
            ok = (acc == 5000 and uniq == 300)
            allok &= ok
            print(f"  r {r}: states {len(sh.states)} (forward "
                  f"{sh.n_forward}) accepted {acc}/5000  unique output "
                  f"{uniq}/300  {'OK' if ok else 'RED'}")
    print(f"C1 {'GREEN' if allok else 'RED'}")
    # C2: r = P and 2P at the designed windows
    print("C2 the period strides at the designed family:")
    c2 = True
    for P in (3, 4, 5):
        for A in (2, 3, 5):
            for r in (P, 2 * P):
                res = read_cell(f"P{P} A{A}", designed(P, A, WANT), P, r,
                                check_finite=False, verbose=False)
                zero = (res["lc"]["inf_from"] is None
                        and all(c == 0 for c in res["lc"]["col"]))
                c2 &= zero
                print(f"  P {P} A {A} r {r:2d}: {'zero' if zero else 'NONZERO'}"
                      f"  states {res['states']} pairs {res['pairs']}")
    print(f"C2 {'GREEN' if c2 else 'RED'}")
    # timing one cell of each population
    print("timing, one cell per population:")
    read_cell("graded (8,4)", window(8, 4), PERIOD, 2)
    read_cell("value (8,4)", window(8, 4), PERIOD, 3)
    read_cell("value (7,4)", window(7, 4), PERIOD, 3)
    read_cell("graded (24,12)", window(24, 12), PERIOD, 2)


# ------------------------------------------------------------------ s1

def s1_designed():
    print("=" * 78)
    print("S1 THE DESIGNED FAMILY IN THE LIMIT (P1)")
    miss = 0
    for P in (3, 4, 5):
        for A in (2, 3, 5):
            for r in range(1, 2 * P + 1):
                res = read_cell(f"P{P} A{A}", designed(P, A, WANT), P, r)
                lc = res["lc"]
                m = r % P
                if m == 0:
                    ok = lc["inf_from"] is None and all(c == 0 for c in lc["col"])
                elif m % 2 == 1:
                    ok = lc["inf_from"] is not None
                else:
                    ok = (lc["inf_from"] is None and res["run"] < P
                          and (lc["cper"] == P
                               or all(c == 0 for c in lc["col"])))
                if not ok:
                    miss += 1
                    print("      <<< OFF THE RESIDUE LAW")
    print(f"S1 misses against the residue law: {miss}")


# ------------------------------------------------------------------ s2

def s2_value():
    print("=" * 78)
    print("S2 THE VALUE GRID AT r = 3 IN THE LIMIT (P2)")
    hist = {}
    miss = 0
    for A, B in VALUE_GRID:
        lab = law_says(A, B)
        res = read_cell(f"({A},{B}) law {lab}", window(A, B), PERIOD, 3)
        lc = res["lc"]
        key = (lab, res["run"], res["peak"],
               None if lc["inf_from"] is not None else lc["cper"])
        hist[key] = hist.get(key, 0) + 1
        if lab == "bnd":
            ok = lc["inf_from"] is None and (res["run"], res["peak"]) == (5, 5)
        elif lab == "delay0":
            ok = lc["inf_from"] is None and all(c == 0 for c in lc["col"])
        else:
            ok = lc["inf_from"] is not None
        if not ok:
            miss += 1
            print("      <<< OFF THE VALUE LAW")
    print("S2 histogram (label, run, peak, period): count")
    for k in sorted(hist, key=str):
        print(f"  {k}: {hist[k]}")
    print(f"S2 cells off the value law's label -- at a bounded label the fixed"
          f" kill firing: {miss}")


# ------------------------------------------------------------------ s3

def s3_graded():
    print("=" * 78)
    print("S3 THE GRADED MAP AT r = 2 IN THE LIMIT (P3, P4)")
    hist = {}
    pre_max = 0
    infs = 0
    for B in range(3, 13):
        for A in range(4, 25):
            res = read_cell(f"({A},{B})", window(A, B), PERIOD, 2)
            lc = res["lc"]
            if lc["inf_from"] is not None:
                infs += 1
                key = ("INF", lc["inf_from"])
            else:
                key = (res["run"], res["peak"], lc["cper"])
                pre_max = max(pre_max, lc["pre"])
            hist[key] = hist.get(key, 0) + 1
    print("S3 histogram (run, peak, period) or (INF, from): count")
    for k in sorted(hist, key=str):
        print(f"  {k}: {hist[k]}")
    print(f"S3 infinite columns {infs}; largest preperiod among finite "
          f"columns {pre_max}")


# ------------------------------------------------------------------ s4

def s4_witness():
    print("=" * 78)
    print("S4 THE GATE MADE EXPLICIT at the value law's bounded cells")
    for A, B in ((8, 4), (9, 4), (6, 5), (8, 5), (9, 6), (7, 6)):
        caps = window(A, B)
        win = Window(caps, PERIOD)
        sh = Shift(win, 3)
        q = build_q_positions(list(caps), 80)
        print(f"  ({A},{B}) r 3, law {law_says(A, B)}:")
        for turns in (0, 1, 2, 3):
            w = witness(sh, 4, turns, q)
            if w is None:
                print("      no witness")
                continue
            n1, n2, agree, diff, cyclen = w
            print(f"      turns {turns} (cycle {cyclen}): n1 {n1} n2 {n2}"
                  f"  agree {agree}  images differ at {diff}"
                  f"  -> A(4) >= {agree}, c(4) >= {agree - 3}")


# ------------------------------------------------------------------ s5

def s5_strides():
    print("=" * 78)
    print("S5 EVERY STRIDE 1..8 AT THE GRADED GRID IN THE LIMIT, against"
          " the parity law at the largeness scale 3 (r odd mod 3 gated,"
          " r = 2 mod 3 finite, r = 0 mod 3 zero) with the half-period"
          " stride r = 3 read gated at A != B")
    tally = {}
    off = []
    ceiling = {}
    for B in range(3, 13):
        for A in range(4, 25):
            row = []
            for r in range(1, 9):
                res = read_cell("", window(A, B), PERIOD, r,
                                check_finite=False, verbose=False)
                lc = res["lc"]
                if lc["inf_from"] is not None:
                    code = "G"
                elif all(c == 0 for c in lc["col"]):
                    code = "."
                else:
                    code = "b"
                    key = (r, res["run"], res["peak"], lc["cper"])
                    ceiling[key] = ceiling.get(key, 0) + 1
                row.append(code)
                m = r % 3
                if r == 3:
                    want = "." if A == B else "G"
                else:
                    want = "G" if m == 1 else ("." if m == 0 else "b.")
                if code not in want:
                    off.append((A, B, r, code))
            key = "".join(row)
            tally[key] = tally.get(key, 0) + 1
    for k in sorted(tally, key=lambda k: -tally[k]):
        print(f"  {k}: {tally[k]}")
    print(f"  cells off that reading: {len(off)}"
          + (f" {off[:20]}" if off else ""))
    print("  finite nonzero columns by (stride, run, peak, period): count")
    for k in sorted(ceiling):
        print(f"    {k}: {ceiling[k]}")


# ------------------------------------------------------------------ s6

def s6_box():
    global SLACK
    print("=" * 78)
    print("S6 THE BOX IS NOT THE VERDICT: the graded map and the value grid"
          " re-read at three times the slack")
    base = {}
    for B in range(3, 13):
        for A in range(4, 25):
            res = read_cell("", window(A, B), PERIOD, 2, check_finite=False,
                            verbose=False)
            base[("g", A, B)] = (res["run"], res["peak"], res["states"])
    for A, B in VALUE_GRID:
        res = read_cell("", window(A, B), PERIOD, 3, check_finite=False,
                        verbose=False)
        base[("v", A, B)] = (res["run"], res["peak"], res["states"])
    SLACK = 3.0
    moved = grew = 0
    for key, (run, peak, states) in base.items():
        kind, A, B = key
        res = read_cell("", window(A, B), PERIOD, 2 if kind == "g" else 3,
                        check_finite=False, verbose=False)
        if (res["run"], res["peak"]) != (run, peak):
            moved += 1
            print(f"  MOVED {key}: {(run, peak)} -> "
                  f"{(res['run'], res['peak'])}")
        if res["states"] != states:
            grew += 1
    SLACK = 1.05
    print(f"  cells whose (run, peak) moved: {moved} of {len(base)};"
          f" trimmed automata whose size changed: {grew}")


STAGES = {"s0": s0_controls, "s1": s1_designed, "s2": s2_value,
          "s3": s3_graded, "s4": s4_witness, "s5": s5_strides,
          "s6": s6_box}

if __name__ == "__main__":
    for name in sys.argv[1:] or ["s0"]:
        t0 = time.time()
        STAGES[name]()
        print(f"[{name} {time.time() - t0:.1f} s]")
