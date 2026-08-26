"""Which family of input pairs witnesses the tear of x m at the golden
window where no comb is written and the boundary family provably cannot
run -- and does that family exist at every periodic window, making the
flip address a theorem at the storey rather than a decision per cell?

THE QUESTION
------------
The carry automaton (explore_limit_maps.py L4) reads x m unbounded from
the lowest admissible digit at every one of 54 cells, the golden window
at m = 3, 5, 7 included. There the apparition criterion proves that no
residue class of the convergent pair holds both parities, so the
boundary family -- inputs (q_K + u q_{K-r} - t)/m along one class, whose
images straddle a coding boundary by the sign (-1)^K of the convergent
-- cannot run, and no comb telescope has been written for m = 3, 5, 7
at that window. The automaton holds SOME witness as a cycle reachable
after the outputs part. This rig extracts it, reads its word, and
derives by hand the family the reading suggests.

THE HAND-ATTACK (pre-engine, on paper)
--------------------------------------
The odometer's cut points -- the points of the circle with two legal
codings -- are -t alpha mod 1 for t >= 1 (0 itself has one coding). x m
tears at an input x with mx on a cut and x off it.
D1  THE RAISED-TOP FAMILY. Suppose m | q_K - 1 and put n = (q_K - 1)/m,
    n' = n + a_{K+2} q_{K+1}. n < q_K so its digit at K is 0, and greedy
    on n' takes the cap a_{K+2} at K+1 and leaves n: the two strings
    agree on positions 0..K. The images: mn = q_K - 1 has star value
    theta_K - alpha, at distance |theta_K| from the cut -alpha on the
    side sign(theta_K); mn' adds m a_{K+2} theta_{K+1} = m (theta_{K+2}
    - theta_K), so its star is -alpha + (1-m) theta_K + m theta_{K+2}:
    the OTHER side iff |theta_{K+2}| / |theta_K| < (m-1)/m. Since
    |theta_K| > 1/(q_{K+1} + q_K) and |theta_{K+2}| < 1/q_{K+3} <=
    1/(2 q_{K+1} + q_K), the ratio is below (1+x)/(2+x) with x =
    q_K/q_{K+1} < 1, hence below 2/3: one raised cap crosses at every
    m >= 3. At m = 2 raise the caps at K+1 and K+3 as well: the offset
    becomes (1-m) theta_K + m theta_{K+4} and the ratio is below 4/9.
    (At the golden window the ratio is alpha^2 = 0.382, so one cap
    serves m = 2 there too.)
D2  THE IMAGES' LOW DIGITS. The depth-d cells are the q_d arcs the
    circle is cut into at -t alpha, 1 <= t <= q_d (checked by hand at
    the golden depth 3: the arcs (0.146, 0.382), (0.382, 0.764),
    (0.764, 1.146) -- cut at -3 alpha, -alpha, -2 alpha -- are the
    cells of 2, 1, 0). Both images sit within
    (2m-1)|theta_K| of -alpha, and no cut -t' alpha with t' - 1 < q_d
    lies nearer to -alpha than |theta_{d-1}|; so at every depth d with |theta_{d-1}| >
    (2m-1)|theta_K| -- every d <= K - c_m -- the images' depth-d cells
    are the two cells adjacent to -alpha, i.e. the two parities of the
    MAXIMAL STRING, whose limits -alpha and 1 - alpha are the cut's two
    codings. The max-string theorem gives their bottoms as (0, a_2, 0)
    against (a_1 - 1, 0, a_3): they part at position 0 when a_1 >= 2 and
    at position 1 when a_1 = 1 -- the lowest admissible digit.
D3  EXISTENCE. At a periodic window the pair (q_K, q_{K-1}) mod m
    evolves by an invertible integer matrix per period, so K = jTP
    returns it to (q_0, q_{-1}) = (1, 0): m | q_K - 1 infinitely often,
    at every m >= 2, no class condition consulted. So D1-D2 make the
    flip address a THEOREM at every periodic window and every m >= 2
    -- and at any window where q_K = 1 mod m recurs. The family's shape
    is the comb telescopes' own, (Y_K, Y_K + q_K): the image beside a
    cut, the partner raising the input's top. The boundary family
    straddles the cut with the convergent's own parity, which is why it
    needs both parities in one class; the raised top straddles it with
    one digit.
D4  WHY OTHER t PART HIGHER. The codings of -t alpha for t >= 2 need
    not part at the lowest admissible digit: at the golden window q_K -
    3 is the odd comb minus 2 at even K (b_1 = 0, b_2 = 1) and the even
    comb minus 2 at odd K (b_1 = b_2 = 0, b_4 = 1) -- they part at b_2.
    A boundary-family class with such a t reads its flip higher, which
    is [0;1,1,7]'s b_2; the automaton's address is the minimum over
    all witnesses, and the t = 1 family is why it sits lowest.
D5  FLOORS ARE NOT COVERED. For floor(n/m) a legal change of the input
    above depth D moves the image's star by (sum c_k theta_k)/m plus a
    JUMP (sum c_k p_k)/m mod 1, and with the jump zero the small term
    cannot exceed |theta_D|/m: the raised-top construction does not
    transfer. The floors' witness is extracted and read here; no
    derivation is frozen for it.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS,
never what they would mean)
  C1 (the positive and negative controls, run FIRST; nothing below is
      read if any is red) (a) the witness walk ported to the general
      automaton prints, for the shift by 3 at the graded window (8, 4)
      at turns 0..3, the same (n1, n2, agreement, parting, cycle) as
      explore_limit_column.py's witness(); (b) at silver x 2 and bronze
      x 3 the extracted pairs reproduce under the engine (the runs are
      the greedy strings, asserted) and part at position 0; (c) the
      raised-top family with the partner's digit 1 instead of the cap,
      at bronze x 2, K = 3, 6, ..., 33: the images AGREE to depth at
      least K - 4 at every K (the crossing inequality fails, so this is
      not a witness).
  P1  at golden x 3, x 5, x 7, the extracted pair at t = 2, turns 0..2:
      the two images' nonzero digits below (agreement - 6) each sit on
      one position parity, the two parities opposite -- an even comb
      against an odd comb. The cycle's input word is printed and not
      predicted.
  P2  the raised-top family at all 54 (window, m) cells of x m -- the
      four storey windows, the four arbitrary-period windows, m = 2..7,
      and x a at [0;1,1,a], a = 2..7 -- at every K = jTP with K + 4
      inside the weight table: the inputs' greedy strings agree to depth
      EXACTLY K + 1 and the images' part at EXACTLY the lowest
      admissible position, with one raised cap at every m >= 3 cell,
      and at m = 2 with one cap where the printed ratio |theta_{K+2} /
      theta_K| is below 1/2 and with two caps otherwise.
  P3  (observable only) at golden floor(n/3), floor(n/5), floor(n/7)
      the extracted images' low digits are again the two comb parities.
  KILL (observable): an extracted pair failing its reproduction assert;
      a raised-top cell whose agreement is not K + 1 or whose parting is
      not the lowest admissible position; a C1(c) K whose images part
      below K - 4.

THE DESIGN
----------
Linear, make, engine_image and the window lists are imported from
explore_limit_maps.py; closure, Window, Shift and the parent witness()
from explore_limit_column.py. witness_linear() is the parent's walk with
the image computed by the map the automaton was built for: a parted
pair at position t with F infinite, on to a cycle of agreeing inputs,
around it `turns` times, each run completed to acceptance, the two
integers rebuilt and re-read by the engine. Stages (argv): s0 controls,
s1 the golden extraction, s2 the raised-top family at 54 cells, s3 the
floors' extraction. Every stage is bounded and rerunnable. The image
gap -- (val(e1) - val(e2)) alpha mod 1, exact against a deep convergent
-- was added to the extraction's print after s3 first ran (L5), as the
observable that tells the two mechanisms apart.

FINDINGS (each at its own tier)

L1  THE CONTROLS ARE GREEN. (a) The ported walk prints the parent's
    tuple at all four turns. (b) Silver x 2 and bronze x 3 extract pairs
    parting at position 0 (n = 8 against 3 at silver, 25 against 15 at
    bronze at turns 0, agreement 2; agreement 6 at turns 2). (c) The
    digit-1 partner at bronze x 2, K = 3, 6, ..., 33: the images agree exactly as deep as the
    inputs, K + 1, at all eleven K -- no witness, as the crossing
    inequality says.
L2  THE GOLDEN WITNESS IS OF THE RAISED-TOP KIND, AT t = 2 OR t = 1 (rule
    at the three cells; the reading is D1's mechanism at general t and a
    general raise). x 3 is D1's letter: n = 5903 = (q_21 - 2)/3 against
    n + q_22 (the cap at K + 1), agreement 22, images 3n = q_21 - 2 (the
    even comb minus 1, b_1 = 1) and q_24 + q_22 - 2 (the odd comb with
    q_24 above, b_1 = 0), the cycle word 00001010 of length 8 -- the two
    codings of the cut -2 alpha, parting at b_1. x 5 at t = 2 with a
    digit riding above the base: 5n = q_43 - 2 + q_48, the partner n +
    q_46 (the raise at K + 3), cycle 20. x 7 at t = 1 with two digits
    above: 7n = q_35 - 1 + q_38 + q_40, the partner n + q_38, cycle 16
    -- the odd comb against the even comb at the bottom, the two codings
    of -alpha. Each is an image beside the cut -t alpha and a partner
    whose one raised digit crosses it. The image gap
    falls to 0.000047, 0.000000, 0.000000 at two turns: both images
    converge to ONE circle point from its two sides. P1's parity
    observable holds at x 7 and fails at x 3 and x 5 -- it was written
    in the t = 1 family's vocabulary, and the automaton's first
    candidate there sits at t = 2, whose coding carries b_1 = 1 below an
    even comb. Every extracted pair reproduced (no assert fired).
L3  THE RAISED-TOP FAMILY WITNESSES ALL 54 CELLS WITH ONE CAP (rule at
    1,621 (cell, K) readings; the derivation D1-D3 a theorem). At every
    (window, m) and every K = jTP up to 252 -- TP from 2 (silver x 2,
    bronze x 3) to 100 (V4 x 5) -- the inputs agree to depth exactly K +
    1 and the images part at exactly the lowest admissible position,
    with the single cap at K + 1; the two-cap fallback never fired,
    the exact ratio |theta_{K+2}/theta_K| -- read once per cell at K =
    TP, the ratio being periodic in K -- being below 1/2 at every
    window read (0.092 at bronze to 0.420 at V1; the derived bound is
    2/3, so the m = 2 case at a window whose ratio sits in [1/2, 2/3)
    rests on D1's two-cap derivation alone). P2 confirmed, 0 off.
L4  THE FLOORS' WITNESS IS A JUMP, NOT A CUT (rule at three cells; the
    derivation below, made after the print, is a theorem). At golden
    floor(n/3) the automaton's cycle word is 00000000: the two inputs
    are x_0 + q_K against x_0 + q_{K-4} + q_{K-1} with x_0 = 7 fixed,
    converging to ONE point of the odometer, while their images'
    gap is 0.673762, 0.666818, 0.666670 -> 2/3; floor(n/5) 0.600000 =
    3/5 at every turn (a nonzero cycle word of length 40); floor(n/7)
    -> 5/7. THE JUMP: floor((x_0 + Delta)/m) has circle point
    ((x_0 - rho) alpha + J)/m with (rho, J) = (x_0 + sum c_k q_k, sum
    c_k p_k) mod m, so a tail's CLASS moves the image by a fixed
    rotation while the input converges. Two classes recur at every
    periodic window ((q_K, p_K) = (1, 0) at K = 0 mod TP and (0, 1) at
    K = -1 mod TP), the difference of the two image points is a
    nonzero fixed rotation, and x_0 alpha/m is dense, so some x_0 puts
    the two limit points in different depth-t_0 cells and off the cut
    orbit: the images' low digits converge to those of two different
    points and part at the lowest admissible position. So the floors'
    address is a THEOREM at every periodic window and every m >= 2
    too, by a macroscopic tear where x m's is a two-sided approach to
    one point. P3's comb observable is not the right one for it.
L5  THE GAP OBSERVABLE. Added after s3's first print: it reads 0 for
    every x m extraction and j/m for every floor, which is what names
    the mechanism from the print alone.

SETTLING POINTER (explore_aperiodic_address.py). The address this rig
proves at every PERIODIC window is a theorem at every IRRATIONAL
window, and periodicity was never needed: what it bought here was
m | q_K - 1 recurring, the price of witnessing with one convergent
where two consecutive convergents are unimodular and realize every
residue pair (Y, round(Y alpha)) mod m at every K. The raised-top
family is that rig's sub-case a = b = 0, and the jump of L4 is its D6
with the residue pair in place of the class. Everything read here
stands at its scope; nothing about the address waits on a period.

RUN RECORD (the estimate first, then what it cost)
Under a minute estimated per stage; s0 0.0 s, s1 0.0 s, s2 0.1 s, s3
0.2 s. Pure Python, standard library, memory far below the ceiling.
s0 ran three times (control (c)'s K list first stepped by 4 where q_K -
1 is odd at bronze every third K; then the weight tables lengthened).
s2 ran twice: the first ratio diagnostic was a float |q_K alpha - p_K|
that underflows past K = 16 and printed 0.000 at two cells before
dividing by zero -- replaced by the exact integer form. s3 ran twice
(the weight table, then the gap column).
"""

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_shift_repair import build_q_positions, greedy   # noqa: E402
from explore_cascade_rule import PERIOD, window              # noqa: E402
from explore_limit_column import (                           # noqa: E402
    INF,
    Shift,
    Window,
    closure,
    witness,
)
from explore_limit_maps import (                             # noqa: E402
    ARBITRARY,
    STOREY,
    Linear,
    address_predicted,
    engine_image,
    make,
    tail_caps,
)

NPOS = 260


def image_of(kind, m, n, d, q):
    return engine_image(kind, m, n, d, q, 0)


def parting(e1, e2):
    j = 0
    while j < len(e1) and e1[j] == e2[j]:
        j += 1
    return j


# ------------------------------------------------ the witness, ported

def witness_linear(au, t, turns, q, kind, m):
    """The parent's witness walk on a Linear automaton at offset r = 0
    (or a shift, r = au.r, for the regression). Returns (n1, n2, agree,
    parting, cycle length, cycle word, d1, d2, e1, e2)."""
    succ, F = closure(au)
    byx = au.byx
    layer = {((i, j), False): None for i in au.init for j in au.init}
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
    r = max(au.r, 0)
    L = max(len(dp1), len(dp2)) + 2
    dp1 = dp1 + [0] * (L - len(dp1))
    dp2 = dp2 + [0] * (L - len(dp2))
    n1 = sum(dp1[k] * q[k - r] for k in range(r, L) if dp1[k])
    n2 = sum(dp2[k] * q[k - r] for k in range(r, L) if dp2[k])
    d1, d2 = greedy(n1, q), greedy(n2, q)
    assert d1[:L - r] == dp1[r:], "run 1 is not the greedy string"
    assert d2[:L - r] == dp2[r:], "run 2 is not the greedy string"
    if kind == "shift":
        e1 = greedy(sum(d1[k] * q[k + r] for k in range(len(q) - r) if d1[k]), q)
        e2 = greedy(sum(d2[k] * q[k + r] for k in range(len(q) - r) if d2[k]), q)
    else:
        e1 = greedy(image_of(kind, m, n1, d1, q), q)
        e2 = greedy(image_of(kind, m, n2, d2, q), q)
    agree = parting(d1, d2)
    return n1, n2, agree, parting(e1, e2), len(cyc), cyc, d1, d2, e1, e2


def digits(d, upto):
    return "".join(str(x) for x in d[:upto])


def comb_parity(e, below):
    """The position parities carrying a nonzero digit below `below`."""
    return sorted(set(k % 2 for k in range(below) if e[k]))


def image_gap(e1, e2, caps, N=240):
    """(val(e1) - val(e2)) alpha mod 1, exactly against the convergent
    p_N/q_N: near 0 when the images straddle one cut, a fixed j/m when
    they converge to points a jump apart."""
    q = build_q_positions(list(caps), N + 1)
    p = [0, 1]
    for k in range(2, N + 1):
        p.append(caps[k - 1] * p[-1] + p[-2])
    g = sum((e1[k] - e2[k]) * q[k] for k in range(min(len(e1), len(e2), N)))
    return ((g * p[N]) % q[N]) / q[N]


def show_extraction(name, kind, m, win, q, t, turns_list):
    au = make(win, kind, m)
    t0 = time.time()
    for turns in turns_list:
        w = witness_linear(au, t, turns, q, kind, m)
        if w is None:
            print(f"  {name}: no witness at t = {t}")
            continue
        n1, n2, agree, part, cyclen, cyc, d1, d2, e1, e2 = w
        below = max(agree - 6, 0)
        print(f"  {name} turns {turns} (cycle {cyclen}, word "
              f"{''.join(str(x) for x in cyc)}): n1 {n1} n2 {n2}  agree {agree}"
              f"  images part at {part}")
        print(f"      d1 {digits(d1, agree + 4)}")
        print(f"      d2 {digits(d2, agree + 4)}")
        print(f"      e1 {digits(e1, agree + 4)}  parities below {below}: "
              f"{comb_parity(e1, below)}")
        print(f"      e2 {digits(e2, agree + 4)}  parities below {below}: "
              f"{comb_parity(e2, below)}")
        print(f"      image gap (e1 - e2) alpha mod 1: "
              f"{image_gap(e1, e2, win.a * ((len(q) + 8) // len(win.a))):.6f}")
    print(f"      [{time.time() - t0:.1f} s, {len(au.states)} states]")


# ------------------------------------------------------------------ s0

def s0_controls():
    print("=" * 78)
    print("S0 CONTROLS (C1)")
    allok = True
    # (a) the regression against the parent's witness at the shift
    caps = window(8, 4)
    win = Window(caps, PERIOD)
    q = build_q_positions(list(caps), 80)
    sh, li = Shift(win, 3), Linear(win, 1, 1, 3)
    print("  (a) shift 3 at the graded (8,4), parent vs ported:")
    for turns in range(4):
        old = witness(sh, 4, turns, q)
        new = witness_linear(li, 4, turns, q, "shift", 1)
        same = old is not None and new is not None and old == new[:5]
        allok &= same
        print(f"      turns {turns}: parent {old}  ported {new[:5] if new else None}"
              f"  {'identical' if same else 'DIFFERENT'}")
    # (b) silver x 2 and bronze x 3 reproduce and part at 0
    print("  (b) the comb-telescope cells, extracted:")
    for name, caps, m in (("silver [2]", tail_caps((2,), NPOS + 4), 2),
                          ("bronze [3]", tail_caps((3,), NPOS + 4), 3)):
        win = Window(caps, 1)
        q = build_q_positions(list(caps), NPOS)
        au = make(win, "mul", m)
        for turns in (0, 2):
            w = witness_linear(au, 1, turns, q, "mul", m)
            ok = w is not None and w[3] == 0
            allok &= ok
            print(f"      {name} x{m} turns {turns}: n1 {w[0]} n2 {w[1]} agree {w[2]}"
                  f" part {w[3]} {'OK' if ok else 'RED'}")
    # (c) the negative control: digit 1 in place of the cap at bronze x 2
    print("  (c) raised top by digit 1 (not the cap) at bronze x 2:")
    caps = tail_caps((3,), NPOS + 4)
    q = build_q_positions(list(caps), NPOS)
    T = pair_period(caps, 2, 1, 40)
    for K in range(T, 36, T):
        n = (q[K] - 1) // 2
        assert (q[K] - 1) % 2 == 0
        npr = n + q[K + 1]
        d1, d2 = greedy(n, q), greedy(npr, q)
        e1, e2 = greedy(2 * n, q), greedy(2 * npr, q)
        ag, pt = parting(d1, d2), parting(e1, e2)
        ok = pt >= K - 4
        allok &= ok
        print(f"      K {K}: inputs agree {ag}, images agree {pt}"
              f" {'OK (no witness)' if ok else 'RED: a witness'}")
    print(f"C1 {'GREEN' if allok else 'RED'}")


# ------------------------------------------------------------------ s1

def s1_golden():
    print("=" * 78)
    print("S1 THE GOLDEN WINDOW'S WITNESS AT x 3, x 5, x 7 (P1)")
    caps = tail_caps((1,), NPOS + 4)
    win = Window(caps, 1)
    q = build_q_positions(list(caps), NPOS)
    for m in (3, 5, 7):
        show_extraction(f"golden x{m}", "mul", m, win, q, 2, (0, 1, 2))


# ------------------------------------------------------------------ s2

def pair_period(caps, m, P, kmax):
    """Least K = jP > 0 with (q_K, q_{K-1}) = (1, 0) mod m."""
    q = build_q_positions(list(caps), kmax + 2)
    for K in range(P, kmax + 1, P):
        if q[K] % m == 1 and q[K - 1] % m == 0:
            return K
    return None


def raised_top(caps, m, K, q, ncaps):
    """n = (q_K - 1)/m and its partner with the caps raised at K+1,
    K+3, ... (ncaps of them); the engine's agreement and parting."""
    n = (q[K] - 1) // m
    npr = n
    for j in range(ncaps):
        pos = K + 1 + 2 * j
        npr += caps[pos] * q[pos]      # the cap of position pos is a_{pos+1}
    d1, d2 = greedy(n, q), greedy(npr, q)
    e1, e2 = greedy(m * n, q), greedy(m * npr, q)
    return parting(d1, d2), parting(e1, e2)


def theta_ratio(caps, K):
    """|theta_{K+2}| / |theta_K|, exactly: with alpha taken as the deep
    convergent p_N/q_N (N = K + 40) the errors q_k p_N - p_k q_N are
    integers and the ratio is correct to a relative 1/q_N."""
    N = K + 40
    q = build_q_positions(list(caps), N + 1)
    p = [0, 1]
    for k in range(2, N + 1):
        p.append(caps[k - 1] * p[-1] + p[-2])
    err = lambda k: abs(q[k] * p[N] - p[k] * q[N])
    return err(K + 2) / err(K)


def s2_family():
    print("=" * 78)
    print("S2 THE RAISED-TOP FAMILY AT 54 CELLS (P2): agreement K + 1,"
          " parting at the lowest admissible position")
    cells = []
    for name, tail in STOREY + ARBITRARY:
        cells.append((name, tail_caps(tail, NPOS + 4), len(tail), range(2, 8)))
    for a in range(2, 8):
        cells.append((f"[1,1,{a}]", tail_caps((1, 1, a), NPOS + 4), 3, (a,)))
    off = 0
    total = 0
    one_cap = two_caps = 0
    for name, caps, P, ms in cells:
        q = build_q_positions(list(caps), NPOS)
        want = address_predicted(caps) - 1
        for m in ms:
            T = pair_period(caps, m, P, NPOS)
            Ks = [K for K in range(T, NPOS - 6, T)] if T else []
            res = []
            for K in Ks:
                assert (q[K] - 1) % m == 0
                ag1, pt1 = raised_top(caps, m, K, q, 1)
                ag2, pt2 = raised_top(caps, m, K, q, 2)
                res.append((K, ag1, pt1, ag2, pt2))
            ratio = theta_ratio(caps, Ks[0]) if Ks else None
            ok1 = all(ag == K + 1 and pt == want for K, ag, pt, _a, _p in res)
            ok2 = all(ag == K + 1 and pt == want for K, _a, _p, ag, pt in res)
            total += 1
            if ok1:
                one_cap += 1
            elif ok2:
                two_caps += 1
            else:
                off += 1
            verdict = ("one cap" if ok1 else "two caps" if ok2 else "OFF")
            print(f"  {name} x{m}: TP {T}, K = {Ks[0]}..{Ks[-1]} ({len(Ks)}),"
                  f" |th_K+2/th_K| {ratio:.3f}, address {want}: {verdict}"
                  + ("" if ok1 or ok2 else f"  <<< {res}"))
    print(f"S2 cells {total}: one cap {one_cap}, two caps {two_caps}, off {off}")


# ------------------------------------------------------------------ s3

def s3_floors():
    print("=" * 78)
    print("S3 THE FLOORS' WITNESS AT THE GOLDEN WINDOW (P3, observable only)")
    caps = tail_caps((1,), NPOS + 4)
    win = Window(caps, 1)
    q = build_q_positions(list(caps), NPOS)
    for m in (3, 5, 7):
        show_extraction(f"golden n//{m}", "floor", m, win, q, 2, (0, 1, 2))


STAGES = {"s0": s0_controls, "s1": s1_golden, "s2": s2_family,
          "s3": s3_floors}

if __name__ == "__main__":
    for name in sys.argv[1:] or ["s0"]:
        t0 = time.time()
        STAGES[name]()
        print(f"[{name} {time.time() - t0:.1f} s]")
