"""The ten cells the completion reader left undecided, decided by the
mod-1 reading: each input takes its OWN integer lift, and the price is a
wrap at the levels whose range is a full turn or more.

THE QUESTION
------------
explore_completion_reader.py measures the completion reader's minimum
lookahead c_comp as a game on one real coordinate, and it reads two
verdicts only: an EMPTY winning set is a loss from every placement, a
FULL one plus the level-0 seam is a win from every placement, and a
point game under ONE lift is a win where it wins. Ten of the 120 grid
cells fall between those certificates and print "open". Its prefix_ok
docstring names the sharper reading it does not take: the completion
map is a map to the CIRCLE, so the lift M -- the integer two codings of
one value differ by -- is whatever the output makes it and may differ
between inputs. What does that reading decide at the ten cells, and
what does it print beside the frozen c_saf (explore_flush_price.py F2)?
The corpus's observation "c_comp = c_saf wherever both read" stands at
110 cells; a decided cell reading BELOW c_saf would be the first cell
where the flush is not the whole gap.

THE HAND-ATTACK (on paper, before the engine)
---------------------------------------------
H1  THE INDEX CONVENTION, RE-DERIVED FROM THE PARENT'S ENGINE. At level
    t the reader has seen d_0..d_{t+c} and emits e_t. The residual arc
    is I_t = m (sum_{k<=t+c} d_k theta_k + |theta_{t+c+1}| A^(g)) -
    sum_{k<t} e_k theta_k - M, g = [d_{t+c} = 0] (the parent's H4
    flag), A^(g) the tail set from index t+c+1 in units of its own
    |theta|. A placement is u = (left(I_t) - low(T_t)) / |theta_t|;
    member j's left endpoint is u = j whatever the sign of theta_t
    (the parent's H5); after digit x the child is (u - j + K) / rho,
    K the parent's offset(psi, g, x) scaled, rho = |theta_{t+1}| /
    |theta_t|. Level 0's own caps: N_0 = a_1 - 1 + s_0 members, and
    the parent's root u_0 at M = 0 is this rig's root too.
H2  THE COMPLETABILITY CONDITION IS POINTWISE AND MOD 1. The reader
    wins iff at every level and for every input consistent with the
    digits seen, the residual sits in T_{t+1} + Z after e_t is emitted:
    I_t - e_t theta_t is a subset of T_{t+1} + Z. Two regimes and no
    third. |T_{t+1}| >= 1: the union is the whole line, every e_t is
    legal, the level is FREE and the lift stays open. |T_{t+1}| < 1:
    the translates T_{t+1} + M are disjoint closed intervals, and a
    connected arc inside their union lies inside ONE of them, so the
    reader must fit the arc into one member for one M -- the level is
    CONSTRAINED and the lift is fixed from there on, every later
    residual lying in T_{t'} + M for that M alone (e theta + T_{t'+1}
    is inside T_{t'}, and T_{t'} + M' is disjoint from T_{t'} + M).
H3  THE WRAP IS AN INITIAL SEGMENT. W_t = |theta_{t-1}| + |theta_t| +
    s S_t is strictly decreasing in t, and W_0 = 1 + E >= 1 always, so
    {t : W_t >= 1} = {0, ..., t* - 1}. Levels 0..t*-2 are free, level
    t*-1 is constrained, and from t* on the game is the parent's own,
    which was derived for absolute placements under a fixed lift and is
    exact there; its winning set at phase(t*) is the winning set at
    level t*, the game from a non-wrapping level depending on the phase
    alone. So the mod-1 reading is a FINITE prefix game feeding the
    parent's periodic one -- exactly what the parent's docstring says.
    And where W_1 < 1, t* = 1 and level 0 is the constrained level:
    THERE THE MOD-1 READING AND THE SINGLE-LIFT ONE COINCIDE, the
    parent's point game enumerating M at the seam already. At such a
    cell the mod-1 reading buys nothing, and undecidedness has another
    cause.
H4  WHAT THE PARENT'S CERTIFICATES LEFT ON THE TABLE. A diagnostic pass
    over the ten cells (reading each one's route per lookahead) preceded
    this rig, and two of the parent's "no verdict" outcomes are verdicts
    under H2/H3. (a) A prefix whose arc fits no (member, lift) at a
    CONSTRAINED level is a LOSS at that prefix: the reader must emit
    now, and every emission strands an input. The parent's point game
    returns False there and play() reads any False as open -- at t* = 1
    that is the seam, which the parent read as a failed WIN route. (b) A
    point-game loss on a closure that was NOT truncated (no node dropped
    at the cap) is the exact winning region of the reachable game, so it
    is a LOSS certificate; the parent's docstring calls a loss there "no
    verdict at all, the closure being an under-approximation", which is
    true only of a truncated closure. Both are read here, the truncation
    flag carried and printed. (b) under the single lift is exact only at
    t* = 1; at a wrapping cell the closure is rebuilt under the mod-1
    moves.
H5  THE ARITHMETIC OF THE WRAP. In units of |theta_t| the circle has
    period p_t = 1 / |theta_t|, an element of Q(sqrt Disc). A placement
    at a free level is reduced mod p_t (floor off a float, corrected by
    exact comparison). At the constrained level the lifts M with
    u - M p_t in [j, j + span_t] for some j <= N_t are finitely many:
    with 0 <= u < p_t and 0 <= j <= j + span <= Wr_t, M lies in
    [-ceil(Wr_t / p_t) - 1, 0]. (THE FREEZE WROTE THIS RANGE WITH ITS
    SIGN REVERSED, [-1, ceil(Wr_t / p_t) + 1], and the engine copied it:
    the first run's C1a printed one decided cell -- V1 (1,1,1,2) x2 at
    (0, 1) -- as a LOSS at the lookahead the parent wins, and C1c
    printed c_comp above c_int there, which H7 says is impossible. The
    range is corrected here and the engine enumerates both sides. The
    second run's C1a was red at five period-4 cells, all with t* >= 2,
    for a second engine fault of the same family: the root placement,
    which is in level-0 units, was reduced by the level-1 period.
    Corrected in place; the slate's H5 already said p_t.) A reduced
    placement's child at the next free level is reduced again, and that
    is consistent: p_{t+1} / rho = p_{t+2}.
H6  WHERE IT CAN BLOW UP. The prefix tree is the input prefixes
    d_0..d_{t*-1+c} times the reader's (N_t + 1) choices at each free
    level times the adversary's digits, memoized on (t, g, u); at the
    widest cell (V1 (1,1,1,2) x5 at (3,3), t* = 4 by the diagnostic,
    c = 1) that is of order 10^4 to 10^5 nodes. The closure cap stays
    the parent's 20000 nodes and truncation is printed, never silent.
    One process under memwatch at the 512 MB default.
H7  MONOTONICITY IS A CONTROL: a reader at lookahead c is simulable at
    c + 1, so WIN at c implies WIN at c + 1. A cell printing WIN at c
    and LOSS at c + 1 is a rig fault. And the parent's C1f: an integer
    reader is a completion reader at the same lookahead, so c_comp <=
    c_int everywhere. AT ALL TEN CELLS c_saf = c_int (the diagnostic),
    so a reading ABOVE c_saf is closed by construction there and the
    only live kill is a decided cell BELOW c_saf.
TRANSPLANT, marked: Frames, gfp, the interval helpers, the grid and
the windows are the parent's; c_saf and c_int come from
explore_flush_price.py's price(). Nothing here re-derives them.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS).
  C1 (controls, run FIRST; nothing below is read if any leg is red)
     (a) THE 110 DECIDED CELLS REPRODUCED: this rig's c_comp equals the
         parent's at every one, both readings sharing every certificate
         the parent used.
     (b) THE (0, 0) COLUMN IN THE KILLING DIRECTION: no reader printed
         at any of the 24 (window, m) cells up to COMPCAP -- the
         corpus's theorem, and the one leg that catches a game too
         permissive.
     (c) c_comp <= c_int at every cell printed (H7).
     (d) At every t* = 1 cell that a closure decides, the closure has
         the parent's point game's node count exactly (H3: the same
         game).
     (e) Where both routes read at a cell -- the closure and the
         stable winning set used as the terminal test of the prefix
         game -- they agree.
  P1 THE TEN CELLS: c_comp beside the frozen c_saf and c_int, with t*,
     the route that decided each lookahead (fixpoint empty / full,
     root loss, closure win / loss), the closure size and whether it
     truncated. The kill observable: a decided cell printing c_comp <
     c_saf.
  P2 THE VERDICT AT c_comp + 1 at each of the ten, which must print WIN
     (H7).
  P3 THE TALLY: how many of the ten decide, and by which route; the
     expectation, stated as a prediction, is that all ten decide with
     c_comp = c_saf, because at each the first open lookahead is c_saf
     (shape (a): full fixpoint, seam failing under one lift at a
     wrapping window) or c_saf - 1 (shapes (b) and (c): a root loss or
     an untruncated closure loss). The risk is "open" at c_saf where
     the fixpoint is unstable and the closure truncates.

THE DESIGN
----------
EXACT IN Q(sqrt Disc) THROUGHOUT, on the parent's Frames. t* is read
off the frames as the first level t >= 1 with Wr[t mod PP] |theta_t|
< 1. The mod-1 closure: roots are the parent's pre_reads with u_0 at
M = 0; at a free level every j in 0..N_t is an option and the child is
reduced mod p_{t+1}; at the constrained level the options are the
(j, M) pairs of H5 and the children are absolute placements at level
t*, from which the parent's edges (span, offset, digits) take over;
the reachable set is closed forward under every option and every digit
to the cap, the finite safety game solved on it, and the verdict is a
WIN if every root prefix has a winning option, a LOSS if not and
nothing was dropped, else no verdict. The terminal-test route: the same
prefix game with the terminal condition "u in W[(phase(t*), g)]" where
W is the stable greatest fixpoint, exact on closed intervals. Per
lookahead the verdict is read in order: fixpoint empty (LOSS), fixpoint
full + prefix_ok (WIN), closure, terminal test; c_comp is the least
WIN with every lower lookahead a LOSS, and anything else prints open.

Stages: s0 the controls (C1a-C1e over the grid), s1 the ten cells with
P1/P2/P3. Stage selection from the environment (LIFT_STAGES).

FINDINGS (entered post-run; every number below sits in this file's
printed output. One process under memwatch at the 512 MB default, the
third run -- the first two were the control failures H5 records --
329 s wall, peak working set 157.9 MB; nothing ran bare, nothing
killed.)

F1  THE CONTROLS HOLD (C1a-C1e, 0 bad each). All 110 cells the parent
    decided read the same c_comp here; the (0, 0) column prints no
    reader at any of its 24 cells to COMPCAP; c_comp <= c_int at every
    cell; the 10 closures built at t* = 1 cells have the parent's point
    game's node count exactly; and the closure and the terminal-test
    route never disagree where both read. The two runs that were red
    are in H5: both faults were in the wrap's arithmetic and both were
    caught by C1a and C1c, in the direction a fault there shows --
    a game too STRICT loses cells the parent wins.
F2  ALL TEN CELLS DECIDE, AND c_comp = c_saf AT EVERY ONE (P1, P3).
    golden x5 (1,0) 3; silver x2 (1,0) 2; silver x4 (1,0) 3; bronze x2
    (1,0) 2; sqrt3-1 x3 (1,0) 2; sqrt3-1 x4 (0,1) 5; sqrt3-1 x5 (3,3)
    2; V1 (1,1,1,2) x5 (3,3) 2; V2 (2,1,3,1) x3 (0,1) 4; V2 x5 (0,1)
    5 -- each equal to the frozen c_saf, and to c_int, at the cell. So
    the corpus's observation now stands at all 120 grid cells that
    read, none undecided, beside the ten band cells the parent read.
    The kill observable -- a decided cell below c_saf -- did not fire,
    and the above direction was closed by H7 before the run.
F3  WHAT DECIDED THEM, BY ROUTE. At the final lookahead, 8 of the 10
    are the parent's own FULL-fixpoint certificate -- the parent never
    reached that lookahead, having stopped at the open one below it --
    and 2 are closure WINS under the mod-1 moves, golden x5 (1,0) at
    c = 3 (t* = 3) and sqrt3-1 x3 (1,0) at c = 2 (t* = 2): the cells
    whose fixpoint was already full and whose seam fails under any one
    lift. At the lookahead below, all 8 losses are untruncated closure
    LOSSES -- 5 at t* = 1 (silver x2, silver x4, bronze x2, V2 x3, V2
    x5), where the closure IS the parent's point game and its loss was
    always a certificate, and 3 at a wrapping cell (sqrt3-1 x4 (0,1)
    at t* = 2, sqrt3-1 x5 (3,3) at t* = 3, V1 x5 (3,3) at t* = 4),
    where the loss is sound only under the mod-1 moves, the single-lift
    closure being the stricter game. So the mod-1 reading was NEEDED at
    5 of the 10 (two wins, three losses) and the other 5 were decided
    by a certificate the parent held and read as "open".
F4  P2 HOLDS: the verdict at c_comp + 1 is a WIN at all ten, by the
    full fixpoint every time. No closure truncated anywhere in the run
    (the largest is 727 nodes, at V2 x5 (0,1), c = 4).

TIER. F2 is an exhaustive computation at the ten cells, exact in
Q(sqrt Disc), each lookahead decided by a certificate (a loss from an
exact finite game or an empty fixpoint, a win from an exhibited
strategy or a full fixpoint). The equality c_comp = c_saf is an
OBSERVATION at 120 grid cells and 10 band cells, 130 in all, with no
mechanism derived and none claimed; the inequality c_comp <= c_saf
stays without proof. F3 is a reading of this rig's own routes and
claims nothing beyond them.
"""

import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_completion_reader import (                  # noqa: E402
    COMPCAP, Frames, QQ, c_comp as parent_c_comp, gfp, point_game,
    pre_reads, same)
from explore_flush_price import price                    # noqa: E402
from explore_limit_column import Window                  # noqa: E402
from explore_limit_maps import tail_caps                 # noqa: E402
from explore_redundant_ostrowski import GRID, WINDOWS    # noqa: E402

STAGES = os.environ.get("LIFT_STAGES", "s0,s1").split(",")
CAP = 20000

# The ten cells the parent printed "open" at (its F7), as
# (window name, period, m, s, s_0); c_saf and c_int come from price().
TEN = [
    ("golden [1]", (1,), 5, 1, 0),
    ("silver [2]", (2,), 2, 1, 0),
    ("silver [2]", (2,), 4, 1, 0),
    ("bronze [3]", (3,), 2, 1, 0),
    ("sqrt3-1 [1,2]", (1, 2), 3, 1, 0),
    ("sqrt3-1 [1,2]", (1, 2), 4, 0, 1),
    ("sqrt3-1 [1,2]", (1, 2), 5, 3, 3),
    ("V1 (1,1,1,2)", (1, 1, 1, 2), 5, 3, 3),
    ("V2 (2,1,3,1)", (2, 1, 3, 1), 3, 0, 1),
    ("V2 (2,1,3,1)", (2, 1, 3, 1), 5, 0, 1),
]


# ------------------------------------------------------------ the wrap

def floor_qq(x):
    f = math.floor(float(x))
    while QQ(f, 0, x.D) > x:
        f -= 1
    while QQ(f + 1, 0, x.D) <= x:
        f += 1
    return f


def reduce_mod(u, p):
    return u - QQ(floor_qq(u / p), 0, u.D) * p


def t_star(F):
    """The first level t >= 1 whose range is less than a full turn."""
    t = 1
    while F.Wr[t % F.PP] * F.t[t] >= F.I:
        t += 1
        assert t < F.PP * 4 + 8, "the wrap does not end"
    return t


def level_params(F, t):
    """(N, rho, psi, Rc, memwidth, width by g) at level t >= 0."""
    phi = t % F.PP
    if t == 0:
        N = F.N0
        Rc = F.t[F.c + 1] / F.t[0]
    else:
        N = F.N[phi]
        Rc = F.Rc[phi]
    rho = F.r[(t + 1) % F.P]
    psi = (t + F.c + 1) % F.PP
    memw = F.Wr[(t + 1) % F.PP] * F.r[(t + 1) % F.P]
    return N, rho, psi, Rc, memw


def roots_of(F):
    """The parent's roots: (g, u_0) per prefix, absolute at M = 0."""
    psi = (F.c + 1) % F.PP
    lo0 = F.LT0 * F.t[0]
    out = []
    for _ds, val, pzd in pre_reads(F):
        g = 1 if pzd else 0
        left = (val * F.m + F.AL[psi][g] * F.t[F.c + 1] * F.m - lo0) / F.t[0]
        out.append((g, left))
    return out


def prefix_options(F, ts, t, g, u):
    """The reader's options at prefix level t < ts: a list of kid lists.

    Free level (t < ts - 1): every member, child reduced mod p_{t+1}.
    Constrained level (t = ts - 1): every (member, lift) fitting the arc,
    children absolute at level ts as parent states (phase, g, u).
    """
    N, rho, psi, Rc, memw = level_params(F, t)
    width = (F.AH[psi][g] - F.AL[psi][g]) * Rc * F.m
    span = memw - width
    xs = F.digits(psi, g)
    Ks = [(x, 1 if x == 0 else 0, F.offset(psi, g, x) * Rc * F.m)
          for x in xs]
    opts = []
    if t < ts - 1:
        p_next = F.I / F.t[t + 1]
        for j in range(N + 1):
            jj = QQ(j, 0, F.D)
            opts.append([("pre", t + 1, h, reduce_mod((u - jj + K) / rho,
                                                       p_next))
                         for _x, h, K in Ks])
        return opts
    if span < F.Z:
        return []
    p = F.I / F.t[t]
    urep = reduce_mod(u, p)
    wr = F.Wr0 if t == 0 else F.Wr[t % F.PP]
    mtop = int(math.ceil(float(wr / p))) + 2
    for M in range(-mtop, mtop + 1):
        v = urep - QQ(M, 0, F.D) * p
        for j in range(N + 1):
            jj = QQ(j, 0, F.D)
            if v < jj or v > jj + span:
                continue
            opts.append([((t + 1) % F.PP, h, (v - jj + K) / rho)
                         for _x, h, K in Ks])
    return opts


def periodic_options(F, phi, g, u):
    """The parent's edges: the absolute game from level t* on."""
    sp = F.span(phi, g)
    if sp < F.Z:
        return []
    rho = F.r[(phi + 1) % F.P]
    psi = (phi + F.c + 1) % F.PP
    Ks = [(1 if x == 0 else 0, F.offset(psi, g, x) * F.Rc[phi] * F.m)
          for x in F.digits(psi, g)]
    out = []
    for j in range(F.N[phi] + 1):
        jj = QQ(j, 0, F.D)
        if u < jj or u > jj + sp:
            continue
        out.append([((phi + 1) % F.PP, h, (u - jj + K) / rho)
                    for h, K in Ks])
    return out


def options(F, ts, st):
    if st[0] == "pre":
        return prefix_options(F, ts, st[1], st[2], st[3])
    return periodic_options(F, st[0], st[1], st[2])


def closure_game(F, ts, cap=CAP):
    """(verdict, nodes, truncated): the mod-1 game on the reachable set.

    True is a WIN (a strategy exhibited). False with truncated False is
    a LOSS (the exact winning region of the reachable game excludes a
    root prefix). False with truncated True is no verdict.
    """
    roots = []
    for g, u0 in roots_of(F):
        st = ("pre", 0, g, u0)
        if ts == 1:
            roots.append(prefix_options(F, ts, 0, g, u0))
        else:
            p0 = F.I / F.t[0]
            roots.append(prefix_options(F, ts, 0, g, reduce_mod(u0, p0)))
    succ = {}
    dropped = set()
    frontier = [k for opts in roots for kids in opts for k in kids]
    while frontier:
        st = frontier.pop()
        if st in succ or st in dropped:
            continue
        if len(succ) >= cap:
            dropped.add(st)
            continue
        succ[st] = options(F, ts, st)
        for kids in succ[st]:
            frontier.extend(kids)
    W = set(succ)
    changed = True
    while changed:
        changed = False
        for st in list(W):
            if not any(all(k in W for k in kids) for kids in succ[st]):
                W.discard(st)
                changed = True
    ok = all(any(all(k in W for k in kids) for kids in opts)
             for opts in roots)
    return ok, len(succ), bool(dropped)


def terminal_game(F, ts, Wfix):
    """The prefix game with the stable fixpoint as its terminal test."""
    memo = {}

    def inW(st):
        phi, g, u = st
        return any(a <= u and u <= b for a, b in Wfix[(phi, g)])

    def win(st):
        if st[0] != "pre":
            return inW(st)
        if st in memo:
            return memo[st]
        res = any(all(win(k) for k in kids)
                  for kids in prefix_options(F, ts, st[1], st[2], st[3]))
        memo[st] = res
        return res

    for g, u0 in roots_of(F):
        u = u0 if ts == 1 else reduce_mod(u0, F.I / F.t[0])
        if not win(("pre", 0, g, u)):
            return False
    return True


def verdict(F):
    """(won, route, nodes, truncated) at one lookahead, both readings."""
    W, rnd, stable = gfp(F)
    if stable and not any(W.values()):
        return False, "fixpoint empty", 0, False
    full = stable and all(same(W[(p, g)], F.domain(p, g))
                          for p in range(F.PP) for g in (0, 1))
    if full and F.prefix_ok():
        return True, "fixpoint full", 0, False
    ts = t_star(F)
    won, n, trunc = closure_game(F, ts)
    route = None
    if won:
        route = "closure win"
    elif not trunc:
        route = "closure loss" if n else "root loss"
    tw = None
    if stable:
        tw = terminal_game(F, ts, W)
        if route is not None and tw != won:
            print("    BAD C1e: routes disagree at t*=%d: closure %s "
                  "terminal %s" % (ts, won, tw))
        if route is None:
            won, route = tw, ("terminal win" if tw else "terminal loss")
    if route is None:
        return None, "open", n, trunc
    return won, route, n, trunc


def c_comp_lift(period, s, s0, m, cap=COMPCAP):
    """(c, routes): the completion reader's minimum under the mod-1
    reading, with the route that decided every lookahead walked."""
    routes = []
    for c in range(cap + 1):
        F = Frames(period, s, s0, m, c)
        won, route, n, trunc = verdict(F)
        routes.append((c, won, route, n, trunc))
        if won is None:
            return None, routes
        if won:
            return c, routes
    return None, routes


def fmt_routes(routes):
    return " ".join("c%d:%s%s%s" % (c, "W" if w else ("L" if w is False
                                                        else "?"),
                                     "[" + r + "]",
                                     ("/n%d%s" % (n, "T" if tr else ""))
                                     if n else "")
                    for c, w, r, n, tr in routes)


# -------------------------------------------------------------- stages

def s0_controls():
    print("== s0  C1: the decided cells reproduced, the (0,0) column, "
          "c_comp <= c_int, the t*=1 closures against the parent's")
    bad = {"a": 0, "b": 0, "c": 0, "d": 0}
    n_a = n_b = n_d = 0
    t0 = time.time()
    for name, period in WINDOWS:
        win = Window(tail_caps(period), len(period))
        for m in (2, 3, 4, 5):
            for s, s0 in GRID:
                c_int, c_saf, _ = price(win, m, s, s0)
                cc, routes = c_comp_lift(period, s, s0, m)
                if (s, s0) == (0, 0):
                    n_b += 1
                    if cc is not None:
                        bad["b"] += 1
                        print("    BAD C1b: reader at (0,0) %s x%d: %s"
                              % (name, m, fmt_routes(routes)))
                    continue
                pc, _n, note = parent_c_comp(period, s, s0, m)
                if pc is not None:
                    n_a += 1
                    if cc != pc:
                        bad["a"] += 1
                        print("    BAD C1a: %s x%d (%d,%d) parent %s here "
                              "%s  %s" % (name, m, s, s0, pc, cc,
                                          fmt_routes(routes)))
                if cc is not None and c_int is not None and cc > c_int:
                    bad["c"] += 1
                    print("    BAD C1c: c_comp %d > c_int %d at %s x%d "
                          "(%d,%d)" % (cc, c_int, name, m, s, s0))
                for c, w, r, n, tr in routes:
                    if r.startswith("closure") and pc is not None:
                        F = Frames(period, s, s0, m, c)
                        if t_star(F) == 1:
                            n_d += 1
                            _pw, pn = point_game(F)
                            if pn != n:
                                bad["d"] += 1
                                print("    BAD C1d: %s x%d (%d,%d) c=%d "
                                      "closure %d parent %d"
                                      % (name, m, s, s0, c, n, pn))
    print("  C1a decided cells compared %d, bad %d" % (n_a, bad["a"]))
    print("  C1b (0,0) cells %d, readers printed %d" % (n_b, bad["b"]))
    print("  C1c c_comp > c_int: %d" % bad["c"])
    print("  C1d t*=1 closures compared %d, bad %d" % (n_d, bad["d"]))
    print("  C1e disagreements are printed inline as BAD C1e")
    print("  %.0f s" % (time.time() - t0))


def s1_ten():
    print("== s1  P1/P2/P3: the ten cells under the mod-1 reading")
    tally = {}
    for name, period, m, s, s0 in TEN:
        t0 = time.time()
        win = Window(tail_caps(period), len(period))
        c_int, c_saf, _ = price(win, m, s, s0)
        cc, routes = c_comp_lift(period, s, s0, m)
        F = Frames(period, s, s0, m, routes[-1][0])
        ts = t_star(F)
        nxt = "-"
        if cc is not None:
            w2, r2, n2, tr2 = verdict(Frames(period, s, s0, m, cc + 1))
            nxt = "%s[%s]" % ("W" if w2 else ("L" if w2 is False else "?"),
                              r2)
        key = routes[-1][2]
        tally[key] = tally.get(key, 0) + 1
        print("  %-14s x%d (%d,%d)  t*=%d  c_int %s  c_saf %s  c_comp %s"
              "  at c+1: %s  %s  %.0f s"
              % (name, m, s, s0, ts, c_int, c_saf,
                 "-" if cc is None else cc, nxt, fmt_routes(routes),
                 time.time() - t0))
        sys.stdout.flush()
    print("  deciding route at the final lookahead:")
    for k in sorted(tally):
        print("    %s: %d" % (k, tally[k]))


def main():
    if "s0" in STAGES:
        s0_controls()
    if "s1" in STAGES:
        s1_ten()


if __name__ == "__main__":
    main()
