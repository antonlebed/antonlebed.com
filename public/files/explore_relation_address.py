"""Does one principle decide the limit lookahead of EVERY shift-free
linear relation at EVERY irrational Ostrowski window -- and what is left
of the shifted members once it does?

THE QUESTION
------------
The carry automaton reads, at every purely periodic window, the limit
lookahead column of any linear relation m_o . val(e) = m_i . val(d') + c
between the greedy string d of an input and the greedy string e of its
image, d' the r-shift of d (explore_limit_maps.py D7-D10). Where the
column is infinite it is infinite from a depth t_0 and t_0 - 1 is the
FLIP ADDRESS, the lowest position at which the images of a witness
family part; at every cell read the automaton put x m and floor(n/m)
at the lowest admissible digit and printed n + 1 finite at lookahead
1. Off periodicity the automaton does not exist, and the address of
x m and floor(n/m) was proved there by the unimodular family
(explore_aperiodic_address.py D1-D6). Does that family decide the
address of every relation off periodicity -- the constant c and the
offset r entering its residue target -- or is there a member it does
not reach?

THE HAND-ATTACK (on paper, before the engine)
---------------------------------------------
Notation as in explore_aperiodic_address.py: alpha irrational with
convergents p_k/q_k, theta_k = q_k alpha - p_k, the star of an integer
its point on the circle, the cuts -t alpha (t >= 1), and the depth-d
cells the arcs between the cuts C_d = {-s alpha : 1 <= s <= q_d}, C_d
EMPTY when q_d = 1 (one cell, the cut its wrap point). The output
digits below t of an image are the depth-t cell of its point. The
lookahead c_inf(t) is the least c-hat such that inputs sharing a
depth-(t + c-hat) cell have images sharing a depth-t cell; it is
infinite when no c-hat serves (explore_limit_column.py D5 reads the
same number off the pair automaton: A_inf(t) = t + c_inf(t) - 1).
p_1 = 0 when a_1 >= 2 and 1 when a_1 = 1, the lowest admissible digit;
q_t >= 2 exactly from t = p_1 + 1.

D1  THE IMAGE POINT OF A SHIFT-FREE RELATION. Take r = 0 and cancel
    gcd(m_o, m_i) (it divides c or the relation is empty). The domain
    is one residue class, m_i n + c = 0 mod m_o, and the image w =
    (m_i n + c)/m_o has point, writing n alpha = P_n + x,
        w alpha = (m_i x + c alpha + j) / m_o  mod 1,   j = m_i P_n mod m_o.
    Within any deep cell every j occurs: adding a zero-low-digit Y of
    residue pair (Y, P_Y) = (0, u) mod m_o (explore_aperiodic_address.py
    D4, every pair realized at every irrational window) keeps the class
    and the cell and moves j by m_i u, m_i invertible mod m_o.
D2  THE CONTAINMENT PRINCIPLE (m_o = 1). f(x) = m_i x + c alpha is a
    circle map, and c_inf(t) = 0 when q_t = 1, else the least c-hat
    with f^{-1}(C_t) contained in C_{t + c-hat}, infinite exactly when
    f^{-1}(C_t) holds a point that is not a cut. If the preimages are
    all cuts of depth t + c-hat, an open input cell holds none, its
    image is an arc holding no output cut, so it sits in one output
    cell. If some preimage z is not a cut, z is interior to a cell at
    EVERY depth, lattice points accumulate at z from both sides, their
    images at the cut from both sides, in the two cells it separates:
    no c-hat serves. f^{-1}(-s alpha) = {(-(s + c) alpha + j)/m_i : j
    mod m_i}, a cut iff m_i u = s + c with j = 0.
D3  THE MEMBERS. (i) m_i >= 2: the preimage with j != 0 is never a
    cut -- INFINITE from p_1 + 1 for every c: x m + c has the address
    of x m. The unimodular family witnesses it with the target pair
    (c + 1 mod m, rho), rho = 0 unless m divides c + 1 and then 1, so
    the inputs converge to (rho - (c + 1) alpha)/m, never a cut.
    (ii) m_i = 1, c >= 0: every preimage -(s + c) alpha is a cut, and
    containment reads q_t + c <= q_{t + c-hat}:
        c_inf(t) = min{ c-hat >= 0 : q_{t + c-hat} >= q_t + c }   (q_t >= 2),
    FINITE and exact at every irrational window. At c = 1, q_{t+1} =
    a_{t+1} q_t + q_{t-1} >= q_t + 1 at t >= 1 and c-hat = 0 never
    serves: the column is [q_t >= 2], the odometer's lookahead 1 from
    p_1 + 1 on -- the rule the automaton read at fourteen windows, now
    a theorem at all of them. At c >= 2 the column is eventually 1
    with early entries above 1 exactly where q_{t+1} - q_t < c, that
    is (a_{t+1} - 1) q_t + q_{t-1} < c.
    (iii) m_i = 1, c < 0: the preimage of -alpha is (|c| - 1) alpha,
    a LATTICE point and never a cut -- INFINITE from p_1 + 1. The
    witness needs no residue at all: n = |c| - 1 + q_K has image
    q_K - 1, whose point theta_K - alpha sits beside -alpha on the side
    of theta_K, alternating with K, within |theta_K|; so the images of
    consecutive K are the two codings of -alpha below depth K and part
    at p_1, while the inputs converge to the lattice point
    (|c| - 1) alpha. THE DECREMENT BORROWS AND THE INCREMENT DOES NOT:
    n - 1 is unbounded from the lowest admissible digit at every
    irrational window while n + 1 reads 1 forever.
D4  m_o >= 2: THE JUMP. By D1 the images of inputs converging to one
    point accumulate at the m_o points (m_i x + c alpha + j)/m_o,
    1/m_o apart; as the input point sweeps the circle so does the pair,
    and some position puts a depth-t cut between two of them, which
    the lattice reaches by density: INFINITE from p_1 + 1 for every
    (m_o, m_i, c) -- the floors' jump (explore_aperiodic_address.py
    D6), the floors being the union over c = -eps. The witness pair:
    x_0 + m_o q_K against x_0 + m_o q_K + a q_{K+4} + b q_{K+5} with
    (a, b) the solution of a (q, p)_{K+4} + b (q, p)_{K+5} = (0, 1)
    mod m_o, for some x_0 in the class.
    So over r = 0: every relation is unbounded from the lowest
    admissible digit EXCEPT n + c at c >= 0, which is finite with the
    exact column of D3(ii). One principle; the unimodular family is
    its residue-freedom lemma.
D5  THE SHIFTED MEMBERS ARE NOT ADDRESSES. At r != 0 the image point
    is the pseudo-star sum d_k theta_{k+r}, a function of the STRING
    and of no circle point, and the carry automaton already prints pure shifts infinite at some
    strides and finite at others -- the designed family by the parity
    of r mod P, the graded window by its largeness scale
    (explore_limit_column.py L4). The drop by l: the single-digit
    inputs j q_D and (j + 1) q_D agree to depth D exactly and drop to
    j q_{D-l} and (j + 1) q_{D-l}, points stepping by theta_{D-l}
    from 0. If a_{D+1} |theta_{D-l}| > 1 -- and a_{D+1} >= q_{D-l+1} +
    q_{D-l} suffices, |theta_k| > 1/(q_{k+1} + q_k) -- the sweep wraps
    the circle and some consecutive pair straddles -alpha within
    |theta_{D-l}|, its two drops the two codings of -alpha below depth
    D - l, parting at p_1. A window with that inequality at infinitely
    many D (a designed Liouville-type tail) has the drop UNBOUNDED
    from p_1 + 1, while the four quadratic windows print the drop by
    their period finite with peak l + 1 (explore_limit_maps.py L3, a
    rule at those four cells and no theorem): the drop's column is a
    Diophantine property of the window's quotients, not an address.
    At e - 2, whose quotients grow linearly and sit far below the
    denominators, the sweep never leaves a neighbourhood of 0 and the
    paper does not decide the column; that cell is a measurement.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS,
never what they would mean). t_0 = 1 + [a_1 = 1]. The nine periodic
windows: golden [1], silver [2], bronze [3], sqrt(3) - 1 = [1, 2], the
arbitrary-period V1 (1,1,1,2), V2 (2,1,3,1), V3 (1,2,1,1,3), V4
(3,1,2,2,1), and the designed P = 3, A = 2. The aperiodic windows:
e - 2 and cbrt(2) - 1 (certified quotients) and the five designed
tails of explore_aperiodic_address.py D7 at m = 3..7; golden and
bronze run beside them as periodic controls of the exact-integer
stages. Agreement is the number of low positions two strings share;
parting is the first position where they differ.
  C1 (controls, run FIRST; nothing below is read if any is red)
      (a) the identity prints the zero column at the nine periodic
      windows; (b) n + 1 there prints a finite column equal, entry for
      entry over the printed depths, to D3(ii)'s formula at c = 1;
      (c) x 2 and floor(n/2) there print infinite from t_0.
  P1  (n + c, the finite members) c = 2..5 at the nine periodic
      windows: the automaton's column is finite and equals D3(ii)'s
      formula at every printed depth. KILL: an infinite column, or one
      entry off the formula.
  P2  (n - c) c = 1..3 at the nine periodic windows: infinite from
      exactly t_0. KILL: a finite column or a t_0 off.
  P3  (m n + c) m = 2, 3 and c in {-2, -1, 1, 2} at the nine periodic
      windows: infinite from exactly t_0. KILL as P2.
  P4  (m_o >= 2) the six relations (m_o, m_i, c) = (2, 3, 0), (2, 3,
      1), (3, 2, 0), (3, 2, 1), (2, 1, 1), (3, 1, 1) at the nine
      periodic windows: infinite from exactly t_0. KILL as P2.
  P5  (the decrement's family, exact integers) at the seven aperiodic
      windows and the two controls, c = 1, 2, 3, every K from 8 to the
      top of the certified ladder: the inputs c - 1 + q_K and c - 1 +
      q_{K+1} agree to depth >= K - 2 and their images q_K - 1 and
      q_{K+1} - 1 part at EXACTLY p_1. KILL: a parting != p_1 or an
      agreement below K - 2 anywhere.
  P6  (x m + c, exact integers) same windows, m = 2..7, c in {-2, -1,
      1, 2}, K = 8..top: the D3(i) family's inputs n_K, n_{K+1} agree
      to depth >= K - 18 and the images m n + c part at EXACTLY p_1.
      KILL as P5 with the slack 18.
  P7  (the jump, exact integers) same windows, the six relations of
      P4, K = 8, 12, ..., top: some x_0 < 3000 in the class gives the
      D4 pair agreeing to depth >= K - 18 with images parting at
      EXACTLY p_1. KILL: no such x_0 at some cell.
  P8  (the drop's dichotomy) (a) the designed Liouville-type window
      a_1 = 2, a_k = 1 except a_{D+1} = q_D + q_{D-1} at D = 4, 8, ...,
      24: at every such D some j <= a_{D+1} - 1 has the drops by 1 of
      j q_D and (j + 1) q_D parting at EXACTLY p_1 = 0, the inputs
      agreeing to depth exactly D; and at D + 2 (a_{D+3} = 1) the
      least parting over the consecutive pairs is >= D - 2, the
      negative control. KILL: a big-digit D with no such j within 2 of
      the predicted crossing. (b) at e - 2, D = 3m + 1 for m = 1..20
      (a_{D+1} = 2m, asserted): the least parting over consecutive
      single-digit pairs is printed as a reach D - 1 - parting;
      prediction: no pair parts at p_1, and the reach at m = 20
      exceeds the reach at m = 1 by at least 2. (c) the finite-range
      column c_N(t) of the drop by 1 at e - 2 (t = 2..5) and cbrt(2)
      - 1 (t = 1..4), N = 10^4 and 10^5: RECORDED. The paper's lean:
      at e - 2 some t rises across the decade; a flat table is the
      bounded reading at scanned scope and refutes nothing on paper.

THE DESIGN
----------
The periodic stages import the automaton Linear(win, m_o, m_i, r, cs)
and its limit column from explore_limit_maps.py and the window class
from explore_limit_column.py; the formula column is computed from the
convergent denominators alone. The exact-integer stages import the
certified quotients, the designed tails, the greedy digits, the
unimodular solve and the agreement reader from
explore_aperiodic_address.py, and build the Liouville-type tail
incrementally (each big quotient from the two denominators below
it); the crossing j of P8(a) is located with an exact rational
approximation of alpha (a convergent far above D) and then READ off
the strings within 2 of it. No float enters a verdict. Stages (argv):
s0 controls, s1 the periodic checks P1-P4, s2 the exact families
P5-P7, s3 the drop P8; all by default. Every stage is bounded (minutes
at most, far under the memory ceiling) and rerunnable.

FINDINGS (each at its own tier)

L1  THE CONTROLS ARE GREEN. The identity prints the zero column at all
    nine periodic windows; n + 1 prints a finite column equal to
    D3(ii)'s formula at every printed depth at all nine (0 0 1 1 ... at
    a_1 = 1, 0 1 1 ... at a_1 >= 2, preperiod 1 or 2, period 1); x 2
    and floor(n/2) print infinite from t_0 at all nine.
L2  THE FOUR MEMBERS READ AS DERIVED AT EVERY PERIODIC CELL (rule at
    189 cells; D2-D4 a theorem at every irrational window). P1: n + c
    for c = 2..5 is finite and equals the formula entry for entry at
    all 36 cells -- golden n + 2 reads 0 0 2 1 1 1, n + 4 reads 0 0 3
    2 2 1 1, sqrt(3) - 1 at n + 5 reads 0 0 2 1 2 1 1 1, the early
    bumps exactly where q_{t+1} - q_t < c (silver n + 5 at t = 2 reads
    1 with q_1 = 2: the coarser reading q_{t-1} < c is wrong), then 1
    forever. P2: n - c for c =
    1..3 is infinite from exactly t_0 at all 27 cells. P3: m n + c is
    infinite from exactly t_0 at all 72 cells. P4: the six m_o >= 2
    relations are infinite from exactly t_0 at all 54 cells. Automata
    9 to 241 states; the three stages together under a second.
L3  THE EXACT FAMILIES WITNESS EVERY APERIODIC CELL (rule at the
    seven aperiodic windows and the two controls; D3-D4 a theorem).
    P5: the decrement's pair c - 1 + q_K, c - 1 + q_{K+1} agrees to
    depth EXACTLY K at every one of the 50 K read (the minimum of
    agreement - K is 0 at all 27 cells) and the images q_K - 1, q_{K+1}
    - 1 part at exactly p_1, 0 off in 1350 readings -- the two parities
    of q_K - 1 are the two codings of -alpha. P6: x m + c at m = 2..7,
    c in {-2, -1, 1, 2}: agreement within 8 of K everywhere (the slack
    18 loose by a factor above 2) and parting exactly p_1, 0 off in
    10800 readings. P7: the jump pair finds its x_0 at or below 3 at
    every (cell, K) of the 54 cells x 11 K, 0 without.
L4  THE DROP IS A DIOPHANTINE PROPERTY OF THE WINDOW (theorem at the
    designed window by D5; the periodic side the parent's L3). P8(a):
    at the Liouville-type window, at every D = 4, 8, ..., 24, the
    pair (j, j + 1) within 2 of the predicted crossing -- j = 3, 129,
    220716, 647577653847, then 26 and 52 digits -- has inputs j q_D,
    (j + 1) q_D agreeing to depth exactly D and drops parting at
    exactly 0 = p_1; the control two positions up reads its least
    parting at D + 1, one below the digit. The drop by 1 is unbounded
    from p_1 + 1 there, where the three constant-quotient windows,
    whose period is 1, read the drop by 1 finite with peak 2.
L5  AT e - 2 THE BIG DIGIT'S REACH IS THE CONSTANT 2 (observation, 20
    positions; the prediction of a growing reach was WRONG). At every
    D = 3m - 2, m = 2..21, the consecutive single-digit pairs' drops
    part at exactly D - 3: the sweep of 2m steps of theta_{D-1} sits
    inside the depth-(D - 3) cell of 0, because the big quotient two
    positions below, a_{D-2} = 2m - 2, sets that cell's scale --
    linear growth of the quotients is growth RELATIVE to nothing. The
    one pair parting at p_1 is D = 4, where D - 3 = 1 = p_1 coincide.
L6  THE SCAN, RECORDED (observation at scanned scope). The drop by 1's
    finite-range column reads 9 8 7 6 at t = 2..5 at e - 2 at BOTH N =
    10^4 and 10^5, flat across the decade, and 8 7 6 5 rising to 10 9
    8 7 at cbrt(2) - 1 (t = 1..4): both far above the periodic peak
    l + 1 = 2, one flat and one growing, and the paper decides neither
    -- the paper's lean (a rise at e - 2) did not print. Whether the
    drop's column is finite at a window whose quotients are unbounded
    yet far below its denominators is OPEN; the two ends read are
    the drop by the period at the four quadratic windows (finite, a
    rule at those cells) and the Liouville-type tail (unbounded, the
    theorem of D5).

THE READING. One principle decides every shift-free relation at every
irrational window: the image point is an affine map of the input point
with a finite set of offsets, and the column is infinite from the
lowest admissible digit exactly when an output cut has a preimage that
is not a cut -- always, except n + c at c >= 0, whose column is finite
and exact, min{c-hat : q_{t + c-hat} >= q_t + c}. The odometer's
lookahead 1 is that formula at c = 1; the decrement borrows and is
unbounded; x m + c and every m_o >= 2 relation carry x m's address.
The unimodular family is the residue-freedom lemma inside the
principle, and the drop is not an address at all: its column is a
property of the window's quotient growth, finite at every periodic
window and unbounded at a Liouville-type one, with the middle open.

RUN RECORD (the estimate first, then what it cost)
Minutes at most estimated; s0-s2 0.6 s wall together (189 automata,
9 to 241 states; 12150 exact-integer readings and 594 jump cells), s3
28 s of which 27
are the two N = 10^5 scans. Pure Python, standard library, exact
integers throughout; memory far below the ceiling (the largest table
10^5 digit tuples of 71 positions). s3 ran twice: the first run's
P8(b) indexed the big quotient at e - 2 as a_{3m+2} where the
certified list has it at a_{3m-1}, and its assertion stopped the
stage before anything printed; the slate's index was corrected to
D = 3m - 2 and the stage rerun, the prediction's content unchanged.
"""

import os
import sys
import time
from fractions import Fraction

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_shift_repair import build_q_positions, designed   # noqa: E402
from explore_cascade_span import WANT as CAP_WANT               # noqa: E402
from explore_limit_column import Window, show_col              # noqa: E402
from explore_limit_maps import (                               # noqa: E402
    ARBITRARY, NPOS, STOREY, Linear, limit_column, tail_caps)
from explore_aperiodic_address import (                        # noqa: E402
    K_FIRST, SLACK, X_TOP, Win, agreement, build_qp, designed_tail,
    solve_ab, windows)
from explore_nonquadratic_window import (                      # noqa: E402
    greedy, quotients_e_minus_2)

PRINT_DEPTH = 40
SUCC_CS = (2, 3, 4, 5)
PRED_CS = (1, 2, 3)
MUL_CELLS = [(m, c) for m in (2, 3) for c in (-2, -1, 1, 2)]
JUMP_CELLS = [(2, 3, 0), (2, 3, 1), (3, 2, 0), (3, 2, 1), (2, 1, 1), (3, 1, 1)]
LIOUVILLE_D = (4, 8, 12, 16, 20, 24)
E2_MS = range(2, 22)


# ------------------------------------------------------------ the paper

def formula_column(q, c, tmax):
    """D3(ii): 0 where q_t = 1, else the least c-hat with
    q_{t + c-hat} >= q_t + c; None past the table."""
    col = []
    for t in range(tmax):
        if q[t] < 2:
            col.append(0)
            continue
        ch = 0
        while t + ch < len(q) and q[t + ch] < q[t] + c:
            ch += 1
        col.append(ch if t + ch < len(q) else None)
    return col


def t0_of(caps):
    return 1 + (1 if caps[0] == 1 else 0)


# --------------------------------------------------- the periodic stages

def periodic_windows():
    out = [(n, tail_caps(t), len(t)) for n, t in STOREY]
    out += [(n, tail_caps(t), len(t)) for n, t in ARBITRARY]
    out.append(("designed P3 A2", designed(3, 2, CAP_WANT), 3))
    return out


def read_relation(win, mo, mi, cs, r=0):
    au = Linear(win, mo, mi, r, cs=cs)
    return limit_column(au), len(au.states)


def check_finite_formula(name, caps, P, c, verbose=True):
    win = Window(caps, P)
    lc, ns = read_relation(win, 1, 1, (c,))
    q = build_q_positions(list(caps), NPOS)
    want = formula_column(q, c, PRINT_DEPTH)
    got = lc["col"]
    depth = min(len(got), PRINT_DEPTH)
    ok = lc["inf_from"] is None
    off = [t for t in range(depth) if want[t] is not None and got[t] != want[t]]
    ok &= not off
    if verbose:
        tag = "ok" if ok else ("INFINITE" if lc["inf_from"] is not None
                               else f"OFF at t = {off[:6]}")
        print(f"  {name:16s} n + {c}: states {ns:4d}  {tag}")
        print(f"      automaton {show_col(lc)}")
        print(f"      formula   " + " ".join(str(x) for x in want[:depth]))
    return ok


def check_infinite(name, caps, P, mo, mi, c, label, verbose=True):
    win = Window(caps, P)
    lc, ns = read_relation(win, mo, mi, (c,))
    want = t0_of(caps)
    ok = lc["inf_from"] == want
    if verbose:
        tag = ("ok" if ok else
               ("FINITE" if lc["inf_from"] is None
                else f"t_0 = {lc['inf_from']} != {want}"))
        print(f"  {name:16s} {label:14s}: states {ns:4d}  infinite from "
              f"{lc['inf_from']}  {tag}")
    return ok


def s0_controls():
    print("=" * 78)
    print("S0 CONTROLS (C1): identity, n + 1 against the formula, x 2 and "
          "floor(n/2) from t_0")
    ok = True
    for name, caps, P in periodic_windows():
        win = Window(caps, P)
        lc, _ = read_relation(win, 1, 1, (0,))
        zero = lc["inf_from"] is None and all(x == 0 for x in lc["col"])
        ok &= zero
        print(f"  {name:16s} identity: {'zero column' if zero else 'NONZERO'}")
    for name, caps, P in periodic_windows():
        ok &= check_finite_formula(name, caps, P, 1)
    for name, caps, P in periodic_windows():
        ok &= check_infinite(name, caps, P, 1, 2, 0, "x 2")
        win = Window(caps, P)
        lc, ns = read_relation(win, 2, 1, (0, -1))
        good = lc["inf_from"] == t0_of(caps)
        ok &= good
        print(f"  {name:16s} floor(n/2)    : states {ns:4d}  infinite from "
              f"{lc['inf_from']}  {'ok' if good else 'OFF'}")
    print(f"S0: {'ALL GREEN' if ok else 'RED -- nothing below is read'}")
    return ok


def s1_periodic():
    print("=" * 78)
    print("S1 THE PERIODIC CHECKS (P1-P4)")
    wins = periodic_windows()
    bad = {"P1": 0, "P2": 0, "P3": 0, "P4": 0}
    tot = dict(bad)
    print("-- P1: n + c, c = 2..5, finite and equal to the formula")
    for name, caps, P in wins:
        for c in SUCC_CS:
            tot["P1"] += 1
            bad["P1"] += not check_finite_formula(name, caps, P, c)
    print("-- P2: n - c, c = 1..3, infinite from t_0")
    for name, caps, P in wins:
        for c in PRED_CS:
            tot["P2"] += 1
            bad["P2"] += not check_infinite(name, caps, P, 1, 1, -c, f"n - {c}")
    print("-- P3: m n + c, infinite from t_0")
    for name, caps, P in wins:
        for m, c in MUL_CELLS:
            tot["P3"] += 1
            bad["P3"] += not check_infinite(name, caps, P, 1, m, c,
                                            f"{m}n{c:+d}")
    print("-- P4: m_o >= 2, infinite from t_0")
    for name, caps, P in wins:
        for mo, mi, c in JUMP_CELLS:
            tot["P4"] += 1
            bad["P4"] += not check_infinite(name, caps, P, mo, mi, c,
                                            f"({mo},{mi},{c:+d})")
    for k in bad:
        print(f"S1 {k}: {tot[k]} cells, {bad[k]} off")
    return all(v == 0 for v in bad.values())


# ------------------------------------------------ the exact-integer stages

def decrement_pair(w, c, K):
    n1, n2 = c - 1 + w.q[K], c - 1 + w.q[K + 1]
    ag = agreement(w.digits(n1), w.digits(n2))
    im = agreement(w.digits(n1 - c), w.digits(n2 - c))
    return ag, im


def mul_c_input(w, m, c, K):
    """D3(i): Y = m q_K + a q_{K+4} + b q_{K+5} with pair (c + 1, rho)."""
    rho = 1 if (c + 1) % m == 0 else 0
    a, b = solve_ab(w.q, w.p, K + 4, m, target=((c + 1) % m, rho))
    Y = m * w.q[K] + a * w.q[K + 4] + b * w.q[K + 5]
    assert (Y - 1 - c) % m == 0
    n = (Y - 1 - c) // m
    assert n >= 0
    return n


def mul_c_pair(w, m, c, K):
    n1, n2 = mul_c_input(w, m, c, K), mul_c_input(w, m, c, K + 1)
    ag = agreement(w.digits(n1), w.digits(n2))
    im = agreement(w.digits(m * n1 + c), w.digits(m * n2 + c))
    return ag, im


def jump_pair(w, mo, mi, c, K, x0):
    a, b = solve_ab(w.q, w.p, K + 4, mo, target=(0, 1))
    Y = mo * w.q[K]
    Y2 = Y + a * w.q[K + 4] + b * w.q[K + 5]
    n1, n2 = x0 + Y, x0 + Y2
    assert (mi * n1 + c) % mo == 0 and (mi * n2 + c) % mo == 0
    ag = agreement(w.digits(n1), w.digits(n2))
    im = agreement(w.digits((mi * n1 + c) // mo), w.digits((mi * n2 + c) // mo))
    return ag, im


def s2_families(ws):
    print("=" * 78)
    print("S2 THE EXACT FAMILIES (P5-P7)")
    ok = True
    print("-- P5: the decrement's family, agreement >= K - 2, parting p_1")
    for w in ws.values():
        for c in PRED_CS:
            n = off = 0
            agmin = None
            for K in range(K_FIRST, w.k_top + 1):
                ag, im = decrement_pair(w, c, K)
                n += 1
                agmin = ag - K if agmin is None else min(agmin, ag - K)
                if im != w.p1 or ag < K - 2:
                    off += 1
            ok &= off == 0
            print(f"  {w.name:26s} n - {c}: {n} K, {off} off, min(agreement - K)"
                  f" = {agmin}, parting {w.p1} predicted")
    print("-- P6: x m + c, agreement >= K - 18, parting p_1")
    for w in ws.values():
        for m in range(2, 8):
            n = off = 0
            agmin = None
            for c in (-2, -1, 1, 2):
                for K in range(K_FIRST, w.k_top + 1):
                    ag, im = mul_c_pair(w, m, c, K)
                    n += 1
                    agmin = ag - K if agmin is None else min(agmin, ag - K)
                    if im != w.p1 or ag < K - SLACK:
                        off += 1
            ok &= off == 0
            print(f"  {w.name:26s} x{m} + c: {n} readings, {off} off, "
                  f"min(agreement - K) = {agmin}")
    print("-- P7: the jump, some x_0 < 3000 per (cell, K)")
    for w in ws.values():
        for mo, mi, c in JUMP_CELLS:
            n = miss = 0
            xmax = 0
            for K in range(K_FIRST, w.k_top - 5, 4):
                found = None
                for x0 in range(X_TOP):
                    if (mi * x0 + c) % mo:
                        continue
                    ag, im = jump_pair(w, mo, mi, c, K, x0)
                    if im == w.p1 and ag >= K - SLACK:
                        found = x0
                        break
                n += 1
                if found is None:
                    miss += 1
                else:
                    xmax = max(xmax, found)
            ok &= miss == 0
            print(f"  {w.name:26s} ({mo},{mi},{c:+d}): {n} K, {miss} without"
                  f" x_0, largest x_0 {xmax}")
    print(f"S2: {'ALL GREEN' if ok else 'RED'}")
    return ok


# ------------------------------------------------------------- the drop

def liouville_tail(dset, npos):
    """a_1 = 2, a_k = 1, except a_{D+1} = q_D + q_{D-1} at D in dset."""
    a = [2]
    q = [1, 2]
    for k in range(2, npos + 2):
        D = k - 1
        x = q[D] + q[D - 1] if D in dset else 1
        a.append(x)
        q.append(x * q[-1] + q[-2])
    return a


def drop1(d, q):
    return sum(d[k] * q[k - 1] for k in range(1, len(d)) if d[k])


def crossing_j(q, p, D, top):
    """The j at which (j + 1) theta_{D-1} first passes -alpha mod 1,
    from the rational alpha ~ p_top/q_top (error under 1/q_top^2)."""
    al = Fraction(p[top], q[top])
    th = q[D - 1] * al - p[D - 1]
    target = (1 - al) if th > 0 else -al
    return int(target / th)


def s3_drop(ws):
    print("=" * 78)
    print("S3 THE DROP'S DICHOTOMY (P8)")
    ok = True
    # (a) the Liouville-type window
    npos = max(LIOUVILLE_D) + 14
    a = liouville_tail(set(LIOUVILLE_D), npos)
    q, p = build_qp(a, npos)
    p1 = 0 if a[0] >= 2 else 1
    print(f"-- P8(a): the Liouville-type window, a_1 = 2, big quotients at "
          f"D = {LIOUVILLE_D}; p_1 = {p1}")
    for D in LIOUVILLE_D:
        big = a[D]                      # a_{D+1}
        assert big == q[D] + q[D - 1]
        j0 = crossing_j(q, p, D, npos)
        hit = None
        for j in range(max(0, j0 - 2), min(big - 1, j0 + 2) + 1):
            d1, d2 = greedy(j * q[D], q), greedy((j + 1) * q[D], q)
            ag = agreement(d1, d2)
            im = agreement(greedy(drop1(d1, q), q), greedy(drop1(d2, q), q))
            if im == p1:
                hit = (j, ag, im)
                break
        ok &= hit is not None
        digits = len(str(big))
        print(f"  D = {D:2d}: a_(D+1) has {digits} digits, crossing j ~ {j0}, "
              + (f"pair (j, j+1) = ({hit[0]}, {hit[0] + 1}) agrees to {hit[1]},"
                 f" drops part at {hit[2]}" if hit else "NO PAIR within 2 -- the kill"))
        # the negative control two positions up, a_{D+3} = 1
        Dc = D + 2
        parts = []
        for j in range(a[Dc]):
            d1, d2 = greedy(j * q[Dc], q), greedy((j + 1) * q[Dc], q)
            parts.append(agreement(greedy(drop1(d1, q), q), greedy(drop1(d2, q), q)))
        least = min(parts)
        ok &= least >= Dc - 2
        print(f"      control D = {Dc} (a_(D+1) = {a[Dc]}): least parting {least}"
              f" (>= {Dc - 2} predicted)")
    # (b) e - 2: the reach of a big digit
    w = ws["e-2"]
    print("-- P8(b): e - 2, D = 3m - 2, the reach D - 1 - parting of the "
          "consecutive single-digit pairs")
    reaches = {}
    anyp1 = 0
    for m in E2_MS:
        D = 3 * m - 2
        big = w.a[D]                    # a_{D+1}
        assert big == 2 * m, (m, D, big)
        if D + 2 >= len(w.q):
            break
        parts = []
        for j in range(big):
            d1, d2 = w.digits(j * w.q[D]), w.digits((j + 1) * w.q[D])
            parts.append(agreement(w.digits(drop1(d1, w.q)), w.digits(drop1(d2, w.q))))
        least = min(parts)
        anyp1 += least == w.p1
        reaches[m] = D - 1 - least
        print(f"  m = {m:2d} (D = {D:2d}, a_(D+1) = {big:2d}): least parting "
              f"{least:2d}, reach {reaches[m]}")
    ms = sorted(reaches)
    grew = reaches[ms[-1]] - reaches[ms[0]]
    ok &= anyp1 == 0 and grew >= 2
    print(f"  pairs parting at p_1: {anyp1}; reach at m = {ms[-1]} minus reach "
          f"at m = {ms[0]}: {grew}")
    # (c) the finite-range column of the drop by 1
    print("-- P8(c): the drop by 1's finite-range column c_N(t), RECORDED")
    for key, ts in (("e-2", range(2, 6)), ("cbrt", range(1, 5))):
        w = ws[key]
        for N in (10 ** 4, 10 ** 5):
            t1 = time.time()
            col = finite_columns(w, lambda n, w=w: drop1(w.digits(n), w.q), ts, N)
            print(f"  {w.name:26s} N = {N:6d}: " +
                  " ".join(f"c({t}) = {col[t]}" for t in ts) +
                  f"   ({time.time() - t1:.0f} s)")
    print(f"S3: {'as predicted' if ok else 'a prediction is off'}")
    return ok


def finite_columns(w, imgs_of, ts, N):
    """c_N(t) for every t in ts from one pass over the strings."""
    ins = [tuple(w.digits(n)) for n in range(N)]
    outs = [tuple(w.digits(imgs_of(n))) for n in range(N)]
    depth = len(w.q)
    res = {}
    for t in ts:
        found = 0
        for D in range(depth, -1, -1):
            seen = {}
            hit = False
            for i in range(N):
                key = ins[i][:D]
                o = outs[i][:t]
                prev = seen.get(key)
                if prev is None:
                    seen[key] = o
                elif prev != o:
                    hit = True
                    break
            if hit:
                found = max(0, D - t + 1)
                break
        res[t] = found
    return res


# ---------------------------------------------------------------- main

def main():
    stages = sys.argv[1:] or ["s0", "s1", "s2", "s3"]
    t0 = time.time()
    ws = windows()
    for w in ws.values():
        w.a = list(w.a)
    if "s0" in stages:
        if not s0_controls():
            print("controls red: stopping")
            return
    if "s1" in stages:
        s1_periodic()
    if "s2" in stages:
        s2_families(ws)
    if "s3" in stages:
        s3_drop(ws)
    print(f"total wall {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
