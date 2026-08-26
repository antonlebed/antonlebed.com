"""Does the carry automaton decide the ARITHMETIC maps too? The limit
lookahead column of n + 1, x m, floor(n/m) and the digit drop at every
periodic Ostrowski window, read exactly, and the flip address with it.

THE QUESTION
------------
At a purely periodic window the digit shift's limit lookahead column is
decided by a finite carry automaton (explore_limit_column.py D1-D5): a
shift's image is the greedy string of the same value, two strings of
one value have star values differing by an integer, and the bottom-up
discrepancy divided by theta_k is a bounded lattice point. Nothing in
that argument used that the map was a shift. This rig generalizes the
automaton's INPUT SIDE from a shifted string to any bounded-digit
string of a linear relation -- m_o . val(e) = m_i . val(d') + c -- and
reads, in the limit, the maps the quadratic storey measured at scanned
scope (explore_ostrowski_window.py): the odometer n + 1 ("delay <= 1"),
the drop of the low digit block ("l + 1, parity-striped"), and every
x m and floor(n/m) at m >= 2 ("gated, the witness tracking the cap").
Where the column is infinite, the depth it goes infinite from is the
FLIP ADDRESS the storey conjectures at every window and proves comb by
comb -- the lowest position whose cap admits a nonzero digit.

THE HAND-ATTACK (pre-engine, on paper; D1-D5 are the parent's)
--------------------------------------------------------------
D7  THE LINEAR RELATION. Let d be the greedy string of n, d' its
    r-shift (d'_k = d_{k-r}, zeros below r; r < 0 DROPS the low -r
    digits), e the greedy string of the image, and suppose
        m_o . sum e_k q_k  =  m_i . sum d'_k q_k  +  c
    with integers m_o, m_i >= 1 and c. Multiply by alpha and subtract
    the p-combination: sum (m_o e_k - m_i d'_k) theta_k - c alpha is an
    INTEGER M; conversely if that sum is an integer then the q-relation
    holds (alpha irrational), so a legal e with the property is the
    greedy string of the image. The maps: x m is (m_o, m_i, r, c) =
    (1, m, 0, 0); n + 1 is (1, 1, 0, 1); the shift by r is (1, 1, r,
    0) and the digit drop by l is (1, 1, -l, 0); floor(n/m) is (m, 1,
    0, -eps) with eps GUESSED in 0..m-1 -- an accepting run forces
    val(d) - eps = m val(e), so eps = n mod m and e = greedy(floor(n/m))
    with no check needed: the guess is verified by acceptance.
D8  THE BOUND ON M. A legal string's star value lies in (-alpha, 1 -
    alpha) (D2), a shifted string's pseudo-star has modulus at most
    1 + alpha (D3), so |M| <= m_o + 2 m_i + |c| + 1.
D9  THE CARRY. D_k = sum_{i<k} (m_o e_i - m_i d'_i) theta_i - c alpha
    - M in L = Z + Z alpha, D_0 = -c alpha - M, accepted iff D = 0 at
    the end. On an accepting run D_k = -sum_{i>=k} (m_o e_i - m_i d'_i)
    theta_i, so |D_k / theta_k| <= m_o (|theta_{k-1}| + |theta_k|) /
    |theta_k| + m_i A_max tail_k / |theta_k|, and in the conjugate
    |D_k' / theta_k'| <= ((m_o + m_i) A_max sum_{i<k} |theta_i'| + |c|
    |alpha'| + |M|) / |theta_k'|: D4's box with (m_o, m_i) in place of
    (1, 1). Finitely many carries per phase; the relation is a finite
    synchronous automaton at every purely periodic window, and D5's
    pair closure prints the limit column c_inf(t) = max(0, max_{R_t} F
    - r + 1), the input offset r now any integer (agreement in d below
    p is agreement in d' below p - r).
D10 WHAT AN INFINITE COLUMN'S DEPTH IS. c_inf infinite from t_0 says
    inputs agreeing arbitrarily deep have images differing at some
    position below t_0 and at none below t_0 - 1: t_0 - 1 is the flip
    ADDRESS, the lowest position at which the images of a witness
    family part. The storey's conjecture puts it at the lowest position
    whose cap admits a nonzero digit -- position 0 when a_1 >= 2 (cap
    a_1 - 1), position 1 when a_1 = 1 -- so it predicts t_0 = 1 + [a_1
    = 1]. The address cannot sit LOWER than that position (a digit
    there is forced to 0), so the automaton either confirms the
    conjecture at a cell or prints a higher address.
D11 THE POSITION LABEL. The parent's state carried a position label
    that cycled from r + 2 on, which is safe only at r >= 1: at r <= 0
    a cycling label could revisit 0 and re-apply the strict cap of
    output position 0. Labels here run 0, 1, ..., max(r, 0) + P + 1 and
    cycle over the last P of them, so label 0 (the output's strict cap)
    and label r (the input's) each occur once.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS,
never what they would mean; the four storey windows are golden [1],
silver [2], bronze [3] and sqrt(3) - 1 = [1, 2]; the four arbitrary-
period windows are explore_class_criterion.py's V1 (1,1,1,2), V2
(2,1,3,1), V3 (1,2,1,1,3), V4 (3,1,2,2,1))
  C1 (the positive controls, run FIRST; nothing below is read if any
      is red) (a) the identity (1, 1, 0, 0) prints the zero column at
      every window read; (b) the shift as the general relation prints
      explore_limit_column.py's column, entry for entry, at the
      designed window P = 3, A = 2, strides 1..6, and the graded
      window (8, 4), strides 1..3; (c) at the four storey windows and
      the designed (3, 2), the maps n + 1, x 2, x 3, floor(n/2) and the
      drop by 1: every n < 5000 has its engine image accepted and every
      n < 300 has EXACTLY ONE accepted output; (d) the parent's C2, x 1
      composed with the period stride, prints the zero column.
  P1 (the odometer) n + 1 at the four storey windows, the nine designed
      windows P = 3, 4, 5 and A = 2, 3, 5, and the graded (8, 4): a
      finite column with peak <= 1, period P (or identically 0).
  P2 (the drop) the drop by l = P at the four storey windows: a finite
      column with peak exactly l + 1 and period P.
  P3 (the multiplications) x m, m = 2..7, at the four storey windows,
      the four arbitrary-period windows and [1, 1, a] with m = a for a
      = 2..7: every column infinite, and infinite from t_0 = 1 + [a_1
      = 1] at every cell (D10).
  P4 (the floors; TRANSPLANT -- the address is imported from x m's)
      floor(n/m) at the same cells: every column infinite from the same
      t_0.
  P5 (the two-class family) the eight windows of
      explore_cascade_scale.py, strides 1..min(2P, 12), 84 cells: the
      limit verdict printed beside gap parity's existential form, the
      disagreement count printed (the rule's is 16 at one range; the
      limit's is not predicted); every finite nonzero column has
      (longest run, peak) at most (4, 4), the exact bounded ceiling the
      calibration constant sits one past.
  KILL (observable): an n + 1 cell printing an infinite column or a
      peak >= 2; a drop cell infinite or with peak != l + 1; a x m or
      floor(n/m) cell printing a finite column; an infinite cell whose
      t_0 is not 1 + [a_1 = 1]; a two-class finite cell with peak >= 5
      or run >= 5.
  P6 (added after L6 printed, frozen before s5 ran) the two-class shape
      widened -- caps (5@1, 2@3) and (4@0, 2@2) at P = 8, 9, 10, every
      stride 1..2P: the largest peak over the finite nonzero columns is
      printed per window; prediction: it is at most P at every window,
      and some finite cell carries an endless run. KILL: a finite cell
      with peak above P.

THE DESIGN
----------
Window, limit_column, closure, run_peak and show_col are imported from
explore_limit_column.py; the window builders from explore_shift_repair.py,
explore_cascade_span.py and explore_cascade_rule.py; gap parity from
explore_cascade_span.py. The general automaton Linear(win, mo, mi, r, cs)
seeds one initial state per (M, c) with M over D8's range and c over
the guessed constants, steps on every legal digit pair inside D9's box,
and trims to the states reaching acceptance; its byx/init/r interface
is the parent's, so the parent's pair closure and limit column run on
it unchanged. Stages, one at a time (argv): s0 controls, s1 the
odometer and the drop, s2 the multiplications, s3 the floors, s4 the
two-class family. Every cell prints its automaton size, closure size
and timing; every stage is bounded and rerunnable.

FINDINGS (each at its own tier)

L1  THE CONTROLS ARE GREEN. Identity: the zero column at all five
    windows. The shift as the general relation: the parent's column,
    entry for entry, at all 9 regression cells. Engine acceptance: 5000
    of 5000 images accepted and 300 of 300 inputs with exactly one
    accepted output at every one of the 25 (window, map) cells, the
    automata 9 to 89 states. The period stride: the zero column at all
    9 designed windows.
L2  THE ODOMETER'S LOOKAHEAD IS EXACTLY 1, FOREVER (rule at the 14
    windows read; the automaton's decision at each). n + 1 prints c_inf
    = 0 below depth 1 + [a_1 = 1] and 1 at every depth from there on,
    period 1, at the four storey windows, the nine designed windows and
    the graded (8, 4) alike -- the scanned "delay <= 1" is exact, and
    the column never returns to 0: the odometer needs one digit of
    lookahead at EVERY depth, not a bounded burst. P1 confirmed on
    finiteness and the peak; the period is 1 and not P.
L3  THE DROP ALTERNATES l AND l + 1 (rule at the four cells). The drop
    by the period prints 0 1 2 1 2 ... at silver and bronze (preperiod
    1), 0 0 2 1 2 ... at golden (preperiod 2) and 0 0 3 2 3 2 ... at
    sqrt(3) - 1 (l = 2): peak l + 1, period 2 whatever P is, and the
    engine's column at N = 30000 at or below it at every depth --
    explore_ostrowski_window.py F1's "l + 1, parity-striped" as the
    limit. THE FIRST PRINT WAS WRONG: the parent's formula counts only
    pairs whose inputs agree to depth t, which at r >= 0 is every pair
    that can contribute and at a drop is not -- a pair parting at p' <
    t in the read digits has agreement p' + l in d -- and it printed 0
    0 2 0 2 0, BELOW the recorded finite-range 1 2 1 2, which a limit
    cannot be. The second term (D9, bounded by l) repaired it; the
    finite column brute-forced by the engine is the control.
L4  EVERY MULTIPLICATION IS INFINITE FROM THE LOWEST ADMISSIBLE DIGIT
    (rule at 54 cells: x m for m = 2..7 at the four storey windows and
    the four arbitrary-period windows, x a at [1, 1, a] for a = 2..7).
    No finite column; t_0 = 1 at the 24 cells with a_1 >= 2 (silver,
    bronze, V2, V4) and t_0 = 2 at the 30 with a_1 = 1 -- P3 at every
    cell, 0 off. The flip address is DECIDED at each cell, the
    automaton being the decision procedure: it sits at the lowest
    position whose cap admits a nonzero digit, including the golden
    window at m = 3, 5, 7, where the boundary family provably cannot
    run (no both-parity class) and no comb has been written -- so the
    witness there is some other family, which the automaton holds and
    this rig does not extract. Automata 18 to 652 states, 0.0 s each.
L5  THE FLOORS LIKEWISE (rule at 54 cells). floor(n/m) at the same
    cells: every column infinite, t_0 = 1 + [a_1 = 1] at all 54, 0 off
    -- P4 confirmed, the transplant landing. The guessed remainder
    costs states (up to 791, closures to 47625 pairs) and not time
    (0.2 s at the largest).
L6  THE TWO-CLASS FAMILY'S LIMIT MAP, AND THE SAWTOOTH THAT REFUTES
    THE RUN-LENGTH RULE'S GATED HALF (rule at 84 cells). Against gap
    parity's existential form the limit disagrees at 18 cells (the
    rule read 16 at one range, the retired classifier 17): gap parity
    gated where the limit is bounded or zero at 14 -- both P = 5
    windows at r = 4, 9; (5@1, 2@4) at P = 7 at r = 4, 6, 11; (5@2,
    2@3) at r = 2, 4, 5, 6, 9, 11, 12 -- and bounded where the limit
    gates at 4, both P = 6 windows at r = 3, 9. The family's finite
    nonzero columns: (1, 1) x 1, (2, 2) x 4, (3, 3) x 4, (4, 4) x 2,
    and TWO cells whose column is finite with a run that never ends --
    (5@1, 2@3) at r = 4 prints 0 0 0 0 3 2 1 5 4 3 2 1 5 4 3 2 1 ...
    and (4@0, 2@2) at r = 4 prints 0 0 0 3 2 1 0 4 3 2 1 5 4 3 2 1
    ..., the cycle 5 4 3 2 1 of length P = 5 returning to 0 at no
    depth: lookahead 5 serves every depth, the cell is BOUNDED, and the
    peak is 5. The box tripled moves neither (66 and 64 states). The
    run-length rule at N = 300000, deep cap, reads both GATED (runs 10
    and 9 at t <= 15, 16; peak 5) -- so "a run of length >= P gates"
    is refuted: touching copies of a periodic bump merge into one
    endless run without any growth, and the rule's gated half is a
    finite-table reading like its bounded half. The KILL on the ceiling
    fires with it: the bounded corpus's ceiling was (4, 4) over the
    graded window and the designed family and is peak 5 once the
    two-class family is read, the sawtooth's peak being its period --
    so the calibration constant one past the bounded ceiling is 6, and
    the aperiodic split (gated at 7 and above, bounded at 3 and below)
    is issued by 6 or 7: two values of margin, and a ceiling that rose
    when a wider periodic family was read.
L7  THE SAWTOOTH IS P = 5's AND NOT THE SHAPE'S (rule at 6 windows, 108
    cells). The same two cap placements at P = 8, 9 and 10, every
    stride to 2P: the largest finite peak is 2 at every window (at r =
    2), no finite column carries an endless run, and the verdict
    vectors are the parity law's -- P6 confirmed, with room: the
    bounded ceiling over everything this rig and its parent read stays
    5, so the margin of L6 is not eroding with the period.

RUN RECORD (the estimate first, then what it cost)
Under a minute estimated per stage; s0 1.6 s, s1 0.5 s, s2 0.4 s, s3
1.7 s, s4 11.7 s of which 12 s are the run-length rule's two N = 300000
tables, s5 0.2 s. Pure Python, standard library, memory far below the
ceiling.
s1 ran twice (the drop's second term, L3) and s4 twice: the first read
gap parity's label in the wrong case and printed 38 disagreements, all
of them the label; the second added the box re-read.
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
from explore_cascade_span import WANT, gap_parity, graded   # noqa: E402
from explore_cascade_rule import PERIOD, col, window       # noqa: E402
from explore_cascade_scale import (         # noqa: E402
    DEEP,
    TWO_CLASS,
    cell as rule_cell,
    measured_period,
)
from explore_limit_column import (          # noqa: E402
    INF,
    SLACK,
    Shift,
    Window,
    closure,
    limit_column as limit_column_parent,
    run_peak,
    show_col,
)

NPOS = 48
BOX = 1.0                   # multiplies the parent's slack (the s4 re-read)

STOREY = [("golden [1]", (1,)), ("silver [2]", (2,)),
          ("bronze [3]", (3,)), ("sqrt3-1 [1,2]", (1, 2))]
ARBITRARY = [("V1 (1,1,1,2)", (1, 1, 1, 2)), ("V2 (2,1,3,1)", (2, 1, 3, 1)),
             ("V3 (1,2,1,1,3)", (1, 2, 1, 1, 3)),
             ("V4 (3,1,2,2,1)", (3, 1, 2, 2, 1))]


def tail_caps(tail, want=WANT):
    return [tail[k % len(tail)] for k in range(want)]


# ------------------------------------------------------- the automaton

class Linear:
    """The carry automaton of m_o val(e) = m_i val(d') + c (D7-D11)."""

    def __init__(self, win, mo, mi, r, cs=(0,)):
        self.win, self.P = win, win.P
        self.mo, self.mi, self.r, self.cs = mo, mi, r, tuple(cs)
        P, a = win.P, win.a
        self.amax = max(a)
        cmax = max(abs(c) for c in self.cs)
        mmax = mo + 2 * mi + cmax + 1
        self.mrange = range(-mmax, mmax + 1)
        self.lmax = max(r, 0) + P + 1
        breal, bconj = self.box(cmax, mmax)
        self.breal = {phi: breal[phi] * SLACK * BOX + 1 for phi in range(P)}
        self.bconj = {phi: bconj[phi] * SLACK * BOX + 1 for phi in range(P)}
        self.init = [(0, -m, -c, True, True)
                     for m in self.mrange for c in self.cs]
        self.trans = {}
        self.build()

    def box(self, cmax, mmax):
        """D9's bounds on D_k / theta_phi per phase (real, conjugate)."""
        win, P = self.win, self.P
        eta, etac = abs(win.eta), abs(win.eta_c)
        T = sum(abs(win.thf[phi]) for phi in range(P))
        Tc = sum(abs(win.thc[phi]) for phi in range(P))
        real, conj = {}, {}
        for phi in range(P):
            th = abs(win.thf[phi])
            tail = (sum(abs(win.thf[psi]) for psi in range(phi, P))
                    + eta / (1 - eta) * T)
            real[phi] = (self.mo * (abs(win.thf[phi - 1]) + th) / th
                         + self.mi * self.amax * tail / th)
            thc = abs(win.thc[phi])
            head = Tc / (etac - 1) + sum(abs(win.thc[psi])
                                         for psi in range(phi))
            conj[phi] = ((self.mo + self.mi) * self.amax * head / thc
                         + (mmax + cmax * abs(win.alpha_c)) / thc)
        return real, conj

    def npos(self, pos):
        nxt = pos + 1
        return nxt if nxt <= self.lmax else nxt - self.P

    def inbox(self, u, w, phi):
        win = self.win
        return (abs(win.real(u, w) / win.thf[phi]) <= self.breal[phi]
                and abs(win.conj(u, w) / win.thc[phi]) <= self.bconj[phi])

    def step(self, s):
        pos, u, w, pze, pzd = s
        r, P, a, win = self.r, self.P, self.win.a, self.win
        phi = pos % P
        cap_e = a[phi]
        ys = range(0, a[0]) if pos == 0 else range(0, cap_e + 1)
        ipos = pos - r
        if ipos < 0:
            xs, cap_d = (0,), None
        elif ipos == 0:
            xs, cap_d = range(0, a[0]), None
        else:
            cap_d = a[ipos % P]
            xs = range(0, cap_d + 1)
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
                d = self.mo * y - self.mi * x
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
        self.byx = {}
        for s, succ in self.trans.items():
            d = {}
            for x, y, s2 in succ:
                d.setdefault(x, []).append((y, s2))
            self.byx[s] = d

    # acceptance and uniqueness (the parent's C1 interface)
    accepts = Shift.accepts
    outputs = Shift.outputs


# ------------------------------------------------- the limit column, r < 0

def limit_column(au):
    """The parent's column at r >= 0; at r = -l < 0 the second term of D9.

    A pair whose inputs part at position p' < t and whose images differ
    below t has d-agreement p' + l, which exceeds t - 1 when p' >= t - l:
    at r >= 0 that contribution is never positive and the parent's max
    with 0 covers it, at a drop it is the whole reading at small t.
    """
    if au.r >= 0:
        return limit_column_parent(au)
    l = -au.r
    byx, trans = au.byx, au.trans
    succ, F = closure(au)
    U = frozenset((i, j) for i in au.init for j in au.init)
    R = frozenset()
    layers = [(U, R)]
    seen = {(U, R): 0}
    pre = per = None
    t = 0
    while True:
        if any(F[p] == INF for p in R):
            break
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
        layers.append(key)
        if t > 4000:
            raise RuntimeError("no cycle within 4000 depths")

    def layer(t):
        if t < len(layers):
            return layers[t]
        return layers[pre + (t - pre) % per]

    def reach(p, t):
        """From the pairs at position p after p agreeing steps, can t - p
        free steps end with the outputs having differed?"""
        Up, Rp = layer(p)
        cur = set((pr, False) for pr in Up) | set((pr, True) for pr in Rp)
        for _k in range(t - p):
            nxt = set()
            for (s1, s2), diff in cur:
                for _x1, y1, t1 in trans[s1]:
                    for _x2, y2, t2 in trans[s2]:
                        nxt.add(((t1, t2), diff or y1 != y2))
            cur = nxt
        return any(diff for _pr, diff in cur)

    def value(t):
        Ut, Rt = layer(t)
        c = 0
        for p in Rt:
            fv = F[p]
            if fv == INF:
                return INF
            c = max(c, fv + l + 1)
        for p in range(max(0, t - l), t):
            if p + l - t + 1 > c and reach(p, t):
                c = p + l - t + 1
        return c

    col = []
    tmax = len(layers) if pre is None else pre + l + 2 * per
    for t in range(tmax + 1):
        c = value(t)
        col.append(c)
        if c == INF:
            return dict(col=col, inf_from=t, pre=None, per=None, cper=None,
                        pairs=len(F))
    cpre0 = pre + l
    cyc = col[cpre0:cpre0 + per]
    cper = per
    for d in range(1, per + 1):
        if per % d == 0 and all(cyc[i] == cyc[i % d] for i in range(per)):
            cper = d
            break
    cpre = cpre0
    while cpre > 0 and col[cpre - 1] == cyc[(cpre - 1 - cpre0) % per]:
        cpre -= 1
    return dict(col=col[:cpre0 + per], inf_from=None, pre=cpre, per=per,
                cper=cper, pairs=len(F))


# --------------------------------------------------------- the engine

def engine_image(kind, m, n, d, q, r):
    """The image's value under the map the automaton is built for."""
    if kind == "mul":
        return m * n
    if kind == "succ":
        return n + 1
    if kind == "floor":
        return n // m
    if kind == "shift":
        return sum(d[k] * q[k + r] for k in range(len(q) - r) if d[k])
    if kind == "drop":
        return sum(d[k] * q[k + r] for k in range(-r, len(q)) if d[k])
    raise ValueError(kind)


def make(win, kind, m=1, r=0):
    if kind == "mul":
        return Linear(win, 1, m, 0)
    if kind == "succ":
        return Linear(win, 1, 1, 0, cs=(1,))
    if kind == "floor":
        return Linear(win, m, 1, 0, cs=tuple(-e for e in range(m)))
    if kind == "shift":
        return Linear(win, 1, 1, r)
    if kind == "drop":
        return Linear(win, 1, 1, -r)
    raise ValueError(kind)


def input_string(d, r, L):
    """d' for the automaton: d_{k-r}, zeros below r, the low -r dropped."""
    out = []
    for pos in range(L):
        k = pos - r
        out.append(d[k] if 0 <= k < len(d) else 0)
    return out


def read(name, win, kind, m=1, r=0, verbose=True):
    t0 = time.time()
    au = make(win, kind, m, r)
    t1 = time.time()
    lc = limit_column(au)
    t2 = time.time()
    run, peak = run_peak(lc)
    if verbose:
        lab = {"mul": f"x{m}", "succ": "n+1", "floor": f"n//{m}",
               "shift": f"shift {r}", "drop": f"drop {r}"}[kind]
        print(f"  {name} {lab}: states {len(au.states):5d} (fwd "
              f"{au.n_forward:6d}) pairs {lc['pairs']:7d}  build "
              f"{t1 - t0:5.1f}s limit {t2 - t1:5.1f}s  run/peak {run}/{peak}")
        print(f"      c_inf: {show_col(lc)}")
    return dict(lc=lc, run=run, peak=peak, au=au)


def address_predicted(caps):
    return 1 + (1 if caps[0] == 1 else 0)


# ------------------------------------------------------------------ s0

def s0_controls():
    print("=" * 78)
    print("S0 CONTROLS (C1): identity, the shift regression, engine "
          "acceptance and uniqueness, the period stride")
    allok = True
    wins = [(n, tail_caps(t), len(t)) for n, t in STOREY]
    wins.append(("designed P3 A2", designed(3, 2, WANT), 3))
    # (a) identity
    for name, caps, P in wins:
        win = Window(caps, P)
        res = read(name, win, "mul", 1, verbose=False)
        zero = res["lc"]["inf_from"] is None and all(c == 0 for c in res["lc"]["col"])
        allok &= zero
        print(f"  identity at {name}: {'zero column' if zero else 'NONZERO'}")
    # (b) the shift as the general relation against the parent
    print("  the shift regression against explore_limit_column.py:")
    for name, caps, P, rs in [("designed P3 A2", designed(3, 2, WANT), 3, range(1, 7)),
                              ("graded (8,4)", window(8, 4), PERIOD, range(1, 4))]:
        win = Window(caps, P)
        for r in rs:
            old = limit_column(Shift(win, r))
            new = limit_column(Linear(win, 1, 1, r))
            same = (old["col"] == new["col"] and old["inf_from"] == new["inf_from"]
                    and old["pre"] == new["pre"] and old["per"] == new["per"])
            allok &= same
            print(f"    {name} r {r}: {'identical' if same else 'DIFFERENT'}"
                  f"  {show_col(new)}")
    # (c) engine acceptance and uniqueness
    print("  engine acceptance (n < 5000) and unique output (n < 300):")
    for name, caps, P in wins:
        win = Window(caps, P)
        q = build_q_positions(list(caps), NPOS)
        for kind, m, r in (("succ", 1, 0), ("mul", 2, 0), ("mul", 3, 0),
                           ("floor", 2, 0), ("drop", 1, 1)):
            au = make(win, kind, m, r)
            acc = uniq = 0
            for n in range(5000):
                d = greedy(n, q)
                dp = input_string(d, -r if kind == "drop" else r, len(q))
                e = greedy(engine_image(kind, m, n, d, q,
                                        -r if kind == "drop" else r), q)
                if au.accepts(dp, e):
                    acc += 1
                if n < 300:
                    L = (max(i for i in range(len(dp)) if dp[i] or e[i]) + 4
                         if any(dp) or any(e) else 4)
                    if au.outputs(dp, L) == {tuple(e[:L])}:
                        uniq += 1
            ok = (acc == 5000 and uniq == 300)
            allok &= ok
            lab = {"mul": f"x{m}", "succ": "n+1", "floor": f"n//{m}",
                   "drop": f"drop {r}"}[kind]
            print(f"    {name} {lab}: states {len(au.states)} accepted "
                  f"{acc}/5000 unique {uniq}/300 {'OK' if ok else 'RED'}")
    # (d) the period stride
    print("  the period stride at the designed family:")
    for P in (3, 4, 5):
        for A in (2, 3, 5):
            win = Window(designed(P, A, WANT), P)
            res = read("", win, "shift", r=P, verbose=False)
            zero = res["lc"]["inf_from"] is None and all(c == 0 for c in res["lc"]["col"])
            allok &= zero
            print(f"    P {P} A {A} r {P}: {'zero' if zero else 'NONZERO'}")
    print(f"C1 {'GREEN' if allok else 'RED'}")


# ------------------------------------------------------------------ s1

def s1_odometer():
    print("=" * 78)
    print("S1 THE ODOMETER n + 1 (P1) AND THE DROP BY THE PERIOD (P2)")
    miss = 0
    wins = [(n, tail_caps(t), len(t)) for n, t in STOREY]
    for P in (3, 4, 5):
        for A in (2, 3, 5):
            wins.append((f"designed P{P} A{A}", designed(P, A, WANT), P))
    wins.append(("graded (8,4)", window(8, 4), PERIOD))
    for name, caps, P in wins:
        win = Window(caps, P)
        res = read(name, win, "succ")
        lc = res["lc"]
        ok = (lc["inf_from"] is None and res["peak"] <= 1
              and (lc["cper"] == P or all(c == 0 for c in lc["col"])
                   or P % lc["cper"] == 0))
        if not ok:
            miss += 1
            print("      <<< OFF P1")
    print(f"S1 n + 1 cells off P1: {miss}")
    miss = 0
    for name, caps, P in wins[:4]:
        win = Window(caps, P)
        res = read(name, win, "drop", r=P)
        lc = res["lc"]
        fin = finite_column_brute(caps, "drop", P, 30_000, 12)
        ext = lc["col"][:]
        while len(ext) <= 13:
            ext.append(ext[lc["pre"] + (len(ext) - lc["pre"]) % lc["per"]])
        below = all(fin[t] <= ext[t] for t in range(1, 13))
        print(f"      c_N at N = 30000: {' '.join(str(c) for c in fin[1:13])}"
              f"   finite<=limit {'OK' if below else 'VIOLATED'}")
        ok = lc["inf_from"] is None and res["peak"] == P + 1 and below
        if not ok:
            miss += 1
            print("      <<< OFF P2")
    print(f"S1 drop cells off P2: {miss}")


def finite_column_brute(caps, kind, m, n_top, tmax):
    """c_N(t) by the engine: sorted strings, consecutive pairs (D5)."""
    q = build_q_positions(list(caps), NPOS)
    r = -m if kind == "drop" else 0
    ds, es = [], []
    for n in range(n_top):
        d = greedy(n, q)
        ds.append(tuple(d))
        es.append(tuple(greedy(engine_image(kind, m, n, d, q, r), q)))
    order = sorted(range(n_top), key=lambda i: ds[i])
    A = [0] * (tmax + 2)
    for i in range(n_top - 1):
        a, b = order[i], order[i + 1]
        p = 0
        while p < len(q) and ds[a][p] == ds[b][p]:
            p += 1
        j = 0
        while j < len(q) and es[a][j] == es[b][j]:
            j += 1
        for t in range(j + 1, tmax + 2):
            A[t] = max(A[t], p)
    return [max(0, A[t] - t + 1) for t in range(tmax + 2)]


# ------------------------------------------------------------------ s2, s3

def cells_arith():
    out = [(n, tail_caps(t), len(t), range(2, 8)) for n, t in STOREY]
    out += [(n, tail_caps(t), len(t), range(2, 8)) for n, t in ARBITRARY]
    out += [(f"[1,1,{a}]", tail_caps((1, 1, a)), 3, (a,)) for a in range(2, 8)]
    return out


def s_arith(kind, label):
    print("=" * 78)
    print(f"S {label} IN THE LIMIT: every column infinite, from t_0 = "
          "1 + [a_1 = 1] (the flip at the lowest admissible digit)")
    miss = finite = 0
    hist = {}
    for name, caps, P, ms in cells_arith():
        win = Window(caps, P)
        want = address_predicted(caps)
        for m in ms:
            res = read(name, win, kind, m)
            lc = res["lc"]
            if lc["inf_from"] is None:
                finite += 1
                print("      <<< FINITE -- the kill")
                continue
            key = (lc["inf_from"], want)
            hist[key] = hist.get(key, 0) + 1
            if lc["inf_from"] != want:
                miss += 1
                print(f"      <<< ADDRESS OFF: infinite from {lc['inf_from']},"
                      f" predicted {want}")
    print(f"{label}: finite cells {finite}; (t_0, predicted): count")
    for k in sorted(hist):
        print(f"  {k}: {hist[k]}")
    print(f"{label}: cells whose t_0 is off 1 + [a_1 = 1]: {miss}")


def s2_mul():
    s_arith("mul", "THE MULTIPLICATIONS x m")


def s3_floor():
    s_arith("floor", "THE FLOORS floor(n/m)")


# ------------------------------------------------------------------ s4

def s4_two_class():
    print("=" * 78)
    print("S4 THE TWO-CLASS FAMILY, 84 CELLS, IN THE LIMIT (P5): the limit"
          " verdict beside gap parity's existential form")
    cells = dis = 0
    ceiling = {}
    tally = {}
    endless = []
    for P, c1, c2, A, B in TWO_CLASS:
        a = graded(P, {c1: A, c2: B})
        per = measured_period(a, 40)
        win = Window(a, per)
        rmax = min(2 * P, 12)
        row = []
        print(f"-- P={P} caps {A}@{c1}/{B}@{c2}  period {per} --")
        for r in range(1, rmax + 1):
            cells += 1
            res = read(f"  ({A}@{c1},{B}@{c2})", win, "shift", r=r, verbose=False)
            lc = res["lc"]
            if lc["inf_from"] is not None:
                code = "G"
            elif all(c == 0 for c in lc["col"]):
                code = "."
            else:
                code = "b"
                key = (res["run"], res["peak"], lc["cper"])
                ceiling[key] = ceiling.get(key, 0) + 1
            gp = gap_parity(a, r, 30)[3]
            gpc = {"GATED": "G", "bounded": "b", "delay-0": "."}[gp]
            agree = (code == "G") == (gpc == "G")
            if not agree:
                dis += 1
            row.append(code)
            print(f"   r {r:2d}: limit {code}  gap parity {gpc}"
                  f"{'' if agree else '  <<< disagree'}   {show_col(lc, 24)}")
            if code == "b" and res["run"] == INF:
                endless.append((P, c1, c2, A, B, a, per, r, res["peak"]))
        tally["".join(row)] = tally.get("".join(row), 0) + 1
    print(f"S4 cells {cells}; limit-vs-gap-parity disagreements {dis}")
    print("  finite nonzero columns by (run, peak, period): count")
    for k in sorted(ceiling):
        print(f"    {k}: {ceiling[k]}")
    top = max(((k[0], k[1]) for k in ceiling), default=None)
    print(f"  ceiling over the family's finite nonzero columns: {top}")
    if endless:
        print("  cells whose finite column never returns to 0 -- the"
              " run-length rule's own verdict at N = 300000, deep cap:")
        for P, c1, c2, A, B, a, per, r, peak in endless:
            t0 = time.time()
            v = rule_cell(a, 300_000, r, per)[r]
            print(f"    P={P} caps {A}@{c1}/{B}@{c2} r {r}: limit peak {peak};"
                  f" rule {col(v['v'])} at t<={v['tmax']}"
                  f"  ({time.time() - t0:.0f} s)")
        global BOX
        BOX = 3.0
        for P, c1, c2, A, B, a, per, r, peak in endless:
            res = read("", Window(a, per), "shift", r=r, verbose=False)
            print(f"    at three times the slack: run/peak {res['run']}/"
                  f"{res['peak']} states {len(res['au'].states)}"
                  f"  {show_col(res['lc'], 14)}")
        BOX = 1.0


def s5_wider():
    print("=" * 78)
    print("S5 THE TWO-CLASS SHAPE AT P = 8, 9, 10 (P6): the bounded ceiling"
          " against the period")
    for P in (8, 9, 10):
        for c1, c2, A, B in ((1, 3, 5, 2), (0, 2, 4, 2)):
            a = graded(P, {c1: A, c2: B})
            per = measured_period(a, 60)
            win = Window(a, per)
            top = (0, 0)
            endless = []
            codes = []
            for r in range(1, 2 * P + 1):
                res = read("", win, "shift", r=r, verbose=False)
                lc = res["lc"]
                if lc["inf_from"] is not None:
                    codes.append("G")
                    continue
                if all(c == 0 for c in lc["col"]):
                    codes.append(".")
                    continue
                codes.append("b")
                if res["peak"] > top[1]:
                    top = (r, res["peak"])
                if res["run"] == INF:
                    endless.append((r, res["peak"]))
            print(f"  P={P} caps {A}@{c1}/{B}@{c2} period {per}: "
                  f"{''.join(codes)}  largest finite peak {top[1]} at r "
                  f"{top[0]}  endless runs {endless}"
                  f"{'  <<< PEAK ABOVE P' if top[1] > P else ''}")


STAGES = {"s0": s0_controls, "s1": s1_odometer, "s2": s2_mul,
          "s3": s3_floor, "s4": s4_two_class, "s5": s5_wider}

if __name__ == "__main__":
    for name in sys.argv[1:] or ["s0"]:
        t0 = time.time()
        STAGES[name]()
        print(f"[{name} {time.time() - t0:.1f} s]")
