"""The redundant continued-fraction cover: what mediant straddles buy
at the continued-fraction window, and what they cannot.

THE QUESTION
------------
The continued-fraction window reads irrationals through Stern-Brocot
cells (explore_cf_window.py). Two gates stand on its maps: the WALL
GATE (an output ON a cell vertex freezes emission forever — permanent
walls are the rationalizing set, explore_cf_nonlinear.py) and the RATE
GATE (an output orbit with mismatched scale rate stalls the digit
clock linearly — rate forcing, explore_cf_flow.py). At the positional
window, redundant (signed) digits dissolve the analogous gates
wholesale (explore_dual_redundant.py). This experiment builds the
mediant-native redundant cover of the CF window and asks which gate
dissolves: the prediction pair, fixed before any engine ran, is that
the WALL gate dissolves (walls are boundary-shaped; a positive
Lebesgue number plus the stream correction of
explore_reading_geometry.py cure them) while the RATE gate stands
(the stall is rate-shaped; overlap cannot let an output slow its
per-digit scale below what its own orbit supplies).

THE COVER (the design, fixed first)
-----------------------------------
Stern-Brocot vocabulary. A node v = mediant of its Farey parents
(l, r); its cell is the interval I(v) = (l, r). THE STRADDLE CHAIN at
v: m_k_L = (p_l + k p_v)/(q_l + k q_v), m_k_R symmetric, and
S_k(v) = (m_k_L, m_k_R), which contains v in its interior at every k.
Hand-derived laws the engine must confirm exactly:
  |v - m_k_L| = 1/(q_v (q_l + k q_v))     (Farey determinant)
  S_{k+1} subset S_k subset I(v)          (nesting)
  the side pieces (m_k_L, v), (v, m_k_R) are Farey intervals, and
  (m_k, v) on the deep side is the CELL of the run node at depth
  depth(v) + k + 1 — chain and quotient run interleave one-for-one
  S_k(v) = W(v)(S_k(root)) with W(v) the node's matrix — the chain is
  the node-translate of the root chain S_k(1) = (k/(k+1), (k+1)/k).
THE COVER = all node cells I(v) + all straddles S_k(v). It is GRADED:
rank(I(node)) = its tree depth, rank(S_k(v)) = depth(v) + k, and
every child relation (deeper chain link, side exit, tree child,
chain entry) steps the rank by exactly +1 — so every STEPWISE route
(one child per digit) between two cover cells has the same length,
and a jump commit (a non-child nested cell) can only shorten it.
The rank is the honest digit clock.

CLASSICAL IMPORTS (read full-text where leaned on; marked)
----------------------------------------------------------
The ALPHABET is classical. Niqui ("Coinductive formal reasoning in
exact real arithmetic", arXiv 0807.1669) fixes the redundant digit
set {L, R, M} on [-1,1] with M = x/3, overlap 1/3, conjugate via
S(x) = (x-1)/(x+1) of the Stern-Brocot representation of [0, +inf];
pulled back, M is (2x+1)/(x+2) with image [1/2, 2] and det 3 —
exactly the root straddle S_1(1) here. The homographic/quadratic
algorithms (Gosper's lazy CF arithmetic; Edalat-Potts) are PRODUCTIVE
for refining Moebius maps on that digit set (Niqui, Coq-verified),
and productivity is the existence half of the wall cure; regular
(non-redundant) CF/Stern-Brocot arithmetic is the lazy-but-partial
classical case (Niqui, "Exact arithmetic on the Stern-Brocot tree",
J. Discrete Algorithms 5 (2007): sign + output-bit algorithms;
Raney's unimodular transducers). Vuillemin (1990), Kornerup-Matula,
and Lester introduced and sized redundant CF representations
(landscape via the above, not read full-text, not leaned on).
Konecny's limitation theorems concern finite transducers (computable
implies piecewise affine) — the machine-class axis, not the delay
axis. What is NOT classical, and is this record's content: the
two-gates split at this cover, the ladder law and the rank grading
below, rate forcing surviving redundancy, the clock-relativity of
delay signs, and the one-digit margin law.

THE LADDER LAW (hand-derived; the crux)
---------------------------------------
The cover's AVAILABLE SCALE LADDER at a point z — the set of cover
cells containing z in their interior — is z's own Stern-Brocot cell
ladder plus, at each vertex v it approaches, a chain segment of
length K(v, z) = floor(1/(q_v^2 |z - v|) - q_far/q_v) (q_far = the
z-side parent; exact by the Farey determinant). At a CONVERGENT of z
the two ratio terms cancel exactly and K = a_next, the next partial
quotient, verbatim. So redundancy adds rungs graded by approximation
quality: at rational z = v the chain is infinite (the terminated
ladder is CURED — walls dissolve); at badly approximable z the added
rungs are the quotients z already owns (the ladder's rank slope is
orbit data no overlap can change — rates are FORCED). Wall gate =
ladder termination; rate gate = ladder spacing. One geometry, two
fates.

PREDICTIONS, fixed before the engine ran
-----------------------------------------
P1 [derived, property] THE COVER GEOMETRY: endpoint law, nesting,
   Farey side pieces, run-cell interleaving with depth bookkeeping
   (the grading), node-translation, and the root straddle = the
   classical M digit's image (1/2, 2) — all exact at every scanned
   node and k.
P2 [derived, rule] THE LADDER LAW: K(v, z) by the exact closed form
   equals K by enumeration at every scanned node, and equals a_next
   at every scanned convergent — all 4s at 2*phi = [3; 4, 4, ...],
   all 1s at phi; at z = 2 the chain never ends (scanned to 10^4).
P3 [derived, rule] THE WALL CURE at (x -> x^2, sqrt r), output the
   vertex r: the non-redundant reader freezes at the wall node's
   depth forever (positive control — the permanent wall of
   explore_cf_nonlinear.py in tree units; depth 1 at sqrt2); the
   straddle reader NEVER freezes: greedy chain index k(n) grows at
   ln k(n+1) - ln k(n) -> the input's own scale rate (2 ln(1+sqrt2)
   = 1.7627 at sqrt2, band [1.71, 1.82] at scanned depths; within 3%
   of the measured input rate at sqrt3 and sqrt(3/2)), the
   committed-vs-image scale gap D(n) stays in [0, 1.5], and the jump
   ratio k(n+1)/k(n) sits in [5.3, 6.4] at sqrt2 (limit (1+sqrt2)^2
   = 5.828). The digit clock is rank: at a rational the rank ladder
   is infinite and DENSE, so unit chain steps would emit k(n) ~
   5.83^n digits of o(1) scale each while jump digits emit one per
   input — the clock explodes because rank explodes, and scale-sync
   holds either way.
P4 [derived, rule] THE RATE GATE STANDS, AND DELAY SIGNS ARE
   CLOCK-RELATIVE: at (2x, phi) the tree-rank emission runs AHEAD at
   slope 4/3 (exact limit, by phi^3 = 2+sqrt5) while the SAME pair's
   quotient clock stalls at 1/3 (explore_cf_window.py) — one reader,
   three clocks (quotient 1/3, tree 4/3, scale 1); the delay's SIGN
   belongs to the clock, only the mismatch is the orbit's. At
   (x/2, 2 phi) the tree clock stalls at slope 3/4 (emission per
   input TREE step, both sides in tree units; band +-4% at 240 input
   quotients = 959 tree steps), and redundancy cannot mend it: the
   maximal RANK of a cover cell containing the image exceeds the
   plain tree depth by at most K = 1 (output phi's quotients are all
   1) at every sampled depth — the rank slope is the tree slope,
   orbit-forced.
P5 [derived, rule] THE MARGIN IS ONE DIGIT, NOT O(1) SCALE: any
   interval J straddling v with |J| <= 1/(q_v (q_max + q_v)) fits in
   S_1(v) — one child level — at every sample, while the SCALE cost
   of that level grows without bound along a quotient run (the
   positional margin log_b(1/rho) has no scale-uniform CF analog;
   the stream correction's one-digit law is the honest form).

KILL CRITERIA, fixed at the freeze: K1 any P1 identity failing kills
the cover design. K2 a frozen straddle reader at P3 kills the wall
cure — this record's headline. K3 rank slope at (x/2, 2 phi) above
0.78 kills the rate gate and the ladder law's teeth. K4 unbounded
D(n) at P3 kills the scale-sync reading. Positive controls, run
before any verdict: the non-redundant freeze (P3) and the
non-redundant stall slopes (P4).

Exact integer/Fraction arithmetic throughout; a bracket of deep
convergents stands in for each irrational, and every comparison must
be decided by the bracket or the run dies. Sequential, seconds, exit
nonzero on any failure.

FINDINGS (entered after the run; ALL ENGINES PASS, exit 0, ~2 s)
----------------------------------------------------------------
P1 CONFIRMED, exact: endpoint law, nesting, Farey side pieces,
   run-cell interleaving with the depth-(v)+k+1 grading, node
   translation — 510 nodes x 12 chain indices; the root straddle is
   (1/2, 2), the classical M digit's image.
P2 CONFIRMED, exact: closed form == enumeration at every scanned
   node; K at the convergents of 2 phi = [4,4,4,4,4,4,4,4,4], of
   phi = [1 x 11] — K = a_next verbatim; the chain at z = 2 contains
   2 at every scanned k up to 10^4.
P3 CONFIRMED — THE WALL CURE (the headline). Controls: the
   non-redundant reader freezes at the wall node's depth (1 at
   sqrt2, 2 at sqrt3 and sqrt(3/2)) at every scanned depth. The
   straddle reader never freezes: chain index at sqrt2 runs 3, 24,
   143, 840, 4899, ..., k(13) = 1119638520; ln-k slope EQUALS the
   measured input scale rate to four decimals at all three walls —
   1.7627 = 2 ln(1+sqrt2), 1.3170 = ln(2+sqrt3), and 2.2924 at
   sqrt(3/2), matching ln(5+2 sqrt6) = 2.2924 over the period-2 tail
   (5+2 sqrt6 the fundamental unit of Z[sqrt6]; the identification
   an observation at four decimals). D(n) within [0.000, 0.717]
   across all rows and depths — scale-synced, never negative. Jump
   ratio at sqrt2: 5.828 = (1+sqrt2)^2 printed exactly.
P4 CONFIRMED — THE RATE GATE STANDS. (2x, phi): tree slope 1.3250
   at 240 input steps (band 4/3); (x/2, 2phi): 0.7487 at 959 input
   tree steps (band 3/4). The rank law rows: (input steps, tree
   position, max rank) = (239, 178, 178), (479, 358, 358),
   (959, 718, 718) — max rank EQUALS tree position at every sampled
   depth (even the +1 allowance goes unused): overlap added no rank.
   Clock relativity printed on one pair: (2x, phi) stalls at 1/3 in
   quotients and runs ahead at 4/3 in tree steps; (x/2, 2phi) the
   reverse (3 and 3/4); the scale clock reads 1 for both.
P5 CONFIRMED: every sampled straddling interval fits at ONE level
   (S_1), and its scale cost grows monotonically along the run
   (2.20 -> 3.36 over eight samples).

Run record: the first run FAILED the P4 stall band with slope
2.9917 — a units mix in the rig (input counted in quotients, output
in tree steps), and 2.99 is itself the quotient-clock slope 3 the
flow layer predicts for this pair: the clock-relativity lesson,
enforced by the rig's own failure. Fixed by counting both sides in
tree steps; no prediction changed. A second fix moved the margin
scan's start one level in (the root spine's cells have infinite
length). All bands then passed unchanged.
"""

from fractions import Fraction
import math
import sys

# ----------------------------------------------------------------- #
# rational points as integer pairs (p, q), q >= 0; (1, 0) = +infinity
# ----------------------------------------------------------------- #

def lt(a, b):
    return a[0] * b[1] < b[0] * a[1]

def frac(a):
    return Fraction(a[0], a[1])

def mediant(a, b):
    return (a[0] + b[0], a[1] + b[1])

class Node:
    """A Stern-Brocot node: v = mediant(l, r), cell I(v) = (l, r)."""
    def __init__(self, l, r, depth):
        self.l, self.r, self.depth = l, r, depth
        self.v = mediant(l, r)

ROOT = Node((0, 1), (1, 0), 0)

def children(nd):
    return (Node(nd.l, nd.v, nd.depth + 1),
            Node(nd.v, nd.r, nd.depth + 1))

def straddle(nd, k):
    """S_k(v) = (m_k_L, m_k_R)."""
    p_l, q_l = nd.l
    p_r, q_r = nd.r
    p_v, q_v = nd.v
    return ((p_l + k * p_v, q_l + k * q_v),
            (p_r + k * p_v, q_r + k * q_v))

# ----------------------------------------------------------------- #
# continued fractions -> convergents, cells, brackets
# ----------------------------------------------------------------- #

def convergents(quots):
    ps, qs = [0, 1], [1, 0]
    for a in quots:
        ps.append(a * ps[-1] + ps[-2])
        qs.append(a * qs[-1] + qs[-2])
    return list(zip(ps[2:], qs[2:]))

def periodic(pre, per, n):
    out = list(pre)
    while len(out) < n:
        out += list(per)
    return out[:n]

def cf_cell(quots):
    """The Stern-Brocot cell of the streams starting with quots:
    endpoints the last convergent and its mediant with the previous."""
    cv = convergents(quots)
    p1, q1 = cv[-1]
    p0, q0 = cv[-2] if len(cv) >= 2 else (1, 0)
    a, b = (p1, q1), (p1 + p0, q1 + q0)
    return (a, b) if lt(a, b) else (b, a)

class Bracket:
    """An irrational pinned between two deep convergents; every
    comparison must be decided by the bracket."""
    def __init__(self, pre, per, depth):
        cv = convergents(periodic(pre, per, depth))
        a, b = cv[-2], cv[-1]
        self.lo, self.hi = (a, b) if lt(a, b) else (b, a)

    def cmp(self, x):
        """+1 if z > x, -1 if z < x (x a rational pair)."""
        if not lt(self.lo, x):        # x <= lo < z
            return 1
        if not lt(x, self.hi):        # z < hi <= x
            return -1
        raise AssertionError("bracket too shallow to decide")

def sb_path(z, steps):
    """Descend the Stern-Brocot tree along the irrational z; return
    the nodes visited (root first); path index = depth."""
    nd, out = ROOT, [ROOT]
    for _ in range(steps):
        left, right = children(nd)
        nd = right if z.cmp(nd.v) > 0 else left
        out.append(nd)
    return out

# ----------------------------------------------------------------- #
# interval fitting
# ----------------------------------------------------------------- #

def fits(cell, lo, hi):
    """Is [lo, hi] strictly interior to the open interval cell?"""
    return lt(cell[0], lo) and lt(hi, cell[1])

def deepest_sb(lo, hi, maxdepth=100000):
    """Greedy non-redundant reader: depth of the deepest node cell
    with [lo, hi] interior, plus the node where descent stopped."""
    nd, d = ROOT, 0
    while d < maxdepth:
        left, right = children(nd)
        if fits((left.l, left.r), lo, hi):
            nd, d = left, d + 1
        elif fits((right.l, right.r), lo, hi):
            nd, d = right, d + 1
        else:
            break
    return d, nd

def chain_fit(nd, lo, hi):
    """Largest k with [lo, hi] interior to S_k(nd) (0 if none):
    m_k_L <= lo gives k <= (lo q_l - p_l)/(p_v - lo q_v), and
    hi <= m_k_R gives k <= (p_r - hi q_r)/(hi q_v - p_v)."""
    p_l, q_l = nd.l
    p_r, q_r = nd.r
    p_v, q_v = nd.v
    lof, hif = frac(lo), frac(hi)
    v = Fraction(p_v, q_v)
    if not (lof < v < hif):
        return 0
    kl = math.floor((lof * q_l - p_l) / (p_v - lof * q_v))
    kr = math.floor((p_r - hif * q_r) / (hif * q_v - p_v))
    return max(0, min(kl, kr))

def ladder_K(nd, z):
    """K(v, z): how many straddles at nd contain the irrational z in
    their interior — the exact closed form."""
    p_v, q_v = nd.v
    side = z.cmp(nd.v)
    far = nd.r if side > 0 else nd.l
    p_f, q_f = far
    def val(x):
        x = frac(x)
        if side > 0:
            return (p_f - x * q_f) / (x * q_v - p_v)
        return (x * q_f - p_f) / (p_v - x * q_v)
    klo, khi = math.floor(val(z.lo)), math.floor(val(z.hi))
    assert klo == khi, "bracket too shallow for ladder count"
    return klo

# ----------------------------------------------------------------- #
# E1  the cover geometry
# ----------------------------------------------------------------- #

def e1_geometry():
    print("E1  THE COVER GEOMETRY (exact, every scanned node, k <= 12)")
    frontier = [ROOT]
    nodes = []
    for _ in range(8):
        nxt = []
        for nd in frontier:
            nxt.extend(children(nd))
        nodes.extend(nxt)
        frontier = nxt
    for nd in nodes:
        p_l, q_l = nd.l
        p_r, q_r = nd.r
        p_v, q_v = nd.v
        prev = None
        for k in range(1, 13):
            mL, mR = straddle(nd, k)
            # endpoint law
            assert abs(frac(nd.v) - frac(mL)) == Fraction(1, q_v * (q_l + k * q_v))
            assert abs(frac(mR) - frac(nd.v)) == Fraction(1, q_v * (q_r + k * q_v))
            # nesting
            if prev is not None:
                assert lt(prev[0], mL) and lt(mR, prev[1])
            assert lt(nd.l, mL) and lt(mR, nd.r)
            # side pieces are Farey
            assert abs(mL[0] * q_v - p_v * mL[1]) == 1
            assert abs(mR[0] * q_v - p_v * mR[1]) == 1
            # node translation: S_k(v) = W(v)(S_k(root)),
            # W(v): x -> (p_r x + p_l)/(q_r x + q_l)
            for (a, b), img in (((k, k + 1), mL), ((k + 1, k), mR)):
                assert (p_r * a + p_l * b, q_r * a + q_l * b) == img
            prev = (mL, mR)
        # run-cell interleaving WITH depth bookkeeping (the grading):
        # walking the right run below v, the k-th step's deep-side
        # child has cell (v, m_k_R) at depth depth(v) + k + 1
        run = children(nd)[1]                    # cell (v, r)
        for k in range(1, 9):
            exit_cell = children(run)[0]         # cell (v, run.v)
            assert exit_cell.l == nd.v
            assert exit_cell.r == straddle(nd, k)[1]
            assert exit_cell.depth == nd.depth + k + 1
            run = exit_cell
    assert straddle(ROOT, 1) == ((1, 2), (2, 1))
    print("    endpoint law, nesting, Farey side pieces, run-cell")
    print("    interleaving + grading (side exit of S_k sits at depth")
    print("    depth(v)+k+1), node translation: EXACT at 510 nodes")
    print("    root straddle S_1(1) = (1/2, 2) = the classical M digit")
    print()

# ----------------------------------------------------------------- #
# E2  the ladder law
# ----------------------------------------------------------------- #

def e2_ladder():
    print("E2  THE LADDER LAW (closed form == enumeration; K = a_next)")
    for name, pre, per, a_next in (("2phi = [3;(4)]", [3], [4], 4),
                                   ("phi  = [1;(1)]", [1], [1], 1)):
        z = Bracket(pre, per, 400)
        path = sb_path(z, 36)
        cv = set(convergents(periodic(pre, per, 12)))
        got = []
        for nd in path[1:]:
            K = ladder_K(nd, z)
            for k in range(1, K + 4):
                mL, mR = straddle(nd, k)
                inside = z.cmp(mL) > 0 and z.cmp(mR) < 0
                assert inside == (k <= K), "closed form != enumeration"
            if nd.v in cv:
                got.append(K)
        assert got and all(K == a_next for K in got), \
            f"K at convergents of {name}: {got} != {a_next}"
        print(f"    {name}: K at its convergents = {got}")
    node2 = children(ROOT)[1]
    assert node2.v == (2, 1)
    for k in (1, 2, 3, 10, 100, 10000):
        mL, mR = straddle(node2, k)
        assert lt(mL, (2, 1)) and lt((2, 1), mR)
    print("    z = 2: the chain contains 2 at every scanned k (to 10^4)")
    print("    — the terminated ladder is cured")
    print()

# ----------------------------------------------------------------- #
# E3  the wall cure
# ----------------------------------------------------------------- #

def e3_wall_cure():
    print("E3  THE WALL CURE at (x -> x^2, sqrt r) — output a vertex")
    cases = (("sqrt2   -> 2  ", [1], [2], (2, 1)),
             ("sqrt3   -> 3  ", [1], [1, 2], (3, 1)),
             ("sqrt3/2 -> 3/2", [1], [4, 2], (3, 2)))
    for name, pre, per, target in cases:
        # positive control: the non-redundant reader freezes
        frozen = None
        for n in range(2, 14):
            quots = periodic(pre, per, n)
            a, b = cf_cell(quots)
            lo = (a[0] * a[0], a[1] * a[1])
            hi = (b[0] * b[0], b[1] * b[1])
            d, _ = deepest_sb(lo, hi)
            if frozen is None:
                frozen = d
            assert d == frozen, "non-redundant emission moved"
        # the wall node
        wall = ROOT
        while wall.v != target:
            left, right = children(wall)
            wall = right if lt(wall.v, target) else left
        assert frozen == wall.depth, \
            f"freeze depth {frozen} != wall node depth {wall.depth}"
        # the straddle reader
        ks, Ds, scale_in = [], [], []
        for n in range(2, 14):
            quots = periodic(pre, per, n)
            a, b = cf_cell(quots)
            lo = (a[0] * a[0], a[1] * a[1])
            hi = (b[0] * b[0], b[1] * b[1])
            k = chain_fit(wall, lo, hi)
            ks.append(k)
            if k:
                mL, mR = straddle(wall, k)
                lenS = frac(mR) - frac(mL)
                lenI = frac(hi) - frac(lo)
                Ds.append(math.log(lenS / lenI))
                scale_in.append(-math.log(frac(b) - frac(a)))
        assert all(k2 > k1 for k1, k2 in zip(ks[2:], ks[3:])), \
            "straddle emission froze (K2)"
        slopes = [math.log(ks[i + 1] / ks[i]) for i in range(4, len(ks) - 1)]
        sbar = sum(slopes[-4:]) / 4
        r_in = [scale_in[i + 1] - scale_in[i]
                for i in range(len(scale_in) - 1)]
        rbar = sum(r_in[-4:]) / 4
        print(f"    {name}: control freeze at depth {frozen} | "
              f"chain k: {ks[:5]}... k(13)={ks[-1]}")
        print(f"      ln-k slope {sbar:.4f} vs input rate {rbar:.4f} | "
              f"D in [{min(Ds):.3f}, {max(Ds):.3f}] | "
              f"jump {ks[-1]/ks[-2]:.3f}")
        assert abs(sbar - rbar) < 0.03 * rbar
        assert 0 <= min(Ds) and max(Ds) <= 1.5, "D out of band (K4)"
        if name.startswith("sqrt2"):
            assert frozen == 1
            assert 1.71 <= sbar <= 1.82
            assert 5.3 <= ks[-1] / ks[-2] <= 6.4
    print("    no wall freezes the straddle reader; unit chain steps")
    print("    would count k(n) ~ e^(r n) digits of o(1) scale each,")
    print("    jump digits one per input — rank explodes at a rational,")
    print("    and the scale account syncs either way")
    print()

# ----------------------------------------------------------------- #
# E4  the rate gate and the three clocks
# ----------------------------------------------------------------- #

def moebius_image(mat, cell):
    (a, b), (c, d) = mat
    x, y = cell
    u = (a * x[0] + b * x[1], c * x[0] + d * x[1])
    w = (a * y[0] + b * y[1], c * y[0] + d * y[1])
    return (u, w) if lt(u, w) else (w, u)

def e4_rate_gate():
    print("E4  THE RATE GATE (rank clock) + clock relativity")
    depths = (60, 120, 240)
    slopes = {}
    for name, pre, per, mat in (
            ("(2x, phi)", [1], [1], ((2, 0), (0, 1))),
            ("(x/2, 2phi)", [3], [4], ((1, 0), (0, 2)))):
        out = []
        for n in depths:
            quots = periodic(pre, per, n)
            cell = cf_cell(quots)
            lo, hi = moebius_image(mat, cell)
            d, _ = deepest_sb(lo, hi)
            out.append((sum(quots), d))       # both sides in tree steps
        slopes[name] = out[-1][1] / out[-1][0]
        print(f"    {name}: (input tree steps, emission) {out} "
              f"slope {slopes[name]:.4f}")
    assert 1.28 <= slopes["(2x, phi)"] <= 1.39, "4/3 band"
    assert 0.71 <= slopes["(x/2, 2phi)"] <= 0.79, "3/4 band"
    print("    one pair, three clocks at (2x, phi): quotient 1/3")
    print("    (explore_cf_window.py), tree 4/3 (phi^3 = 2+sqrt5),")
    print("    scale 1 — and (x/2, 2phi) shows quotient 3, tree 3/4:")
    print("    the delay SIGN belongs to the clock, only the mismatch")
    print("    belongs to the orbit")
    # the rank law at (x/2, 2phi): redundancy adds at most K = 1 rank
    z = Bracket([1], [1], 1700)
    path = sb_path(z, 780)
    rows = []
    for n in depths:
        quots = periodic([3], [4], n)
        cell = cf_cell(quots)
        lo, hi = moebius_image(((1, 0), (0, 2)), cell)
        pos = 0
        while pos + 1 < len(path) and fits(
                (path[pos + 1].l, path[pos + 1].r), lo, hi):
            pos += 1
        assert pos + 1 < len(path), "path too short for this depth"
        rmax = pos
        for i in range(max(1, pos - 3), min(len(path), pos + 4)):
            k = chain_fit(path[i], lo, hi)
            if k:
                assert k <= ladder_K(path[i], z)
                rmax = max(rmax, i + k)
        rows.append((sum(quots), pos, rmax))
    print(f"    rank law at (x/2, 2phi): (input steps, tree pos, max"
          f" rank) = {rows}")
    for n, pos, rmax in rows:
        assert rmax - pos <= 1, "rank exceeded position by more than K"
    assert 0.71 <= rows[-1][2] / rows[-1][0] <= 0.79, \
        "rank slope escaped the stall band (K3)"
    print("    max rank = tree position + at most K = 1: overlap adds")
    print("    routes, never length — the rate gate stands where it")
    print("    always lived")
    print()

# ----------------------------------------------------------------- #
# E5  the one-digit margin
# ----------------------------------------------------------------- #

def e5_margin():
    print("E5  THE MARGIN: one digit deep, unboundedly many nats")
    nd = children(children(ROOT)[1])[0]     # v = 3/2, cell (1, 2)
    gaps = []
    for j in range(1, 9):
        p_v, q_v = nd.v
        q_l, q_r = nd.l[1], nd.r[1]
        thr = Fraction(1, q_v * (max(q_l, q_r) + q_v))
        eps = thr / 3
        lof = frac(nd.v) - eps
        hif = frac(nd.v) + eps
        lo = (lof.numerator, lof.denominator)
        hi = (hif.numerator, hif.denominator)
        mL, mR = straddle(nd, 1)
        assert lt(mL, lo) and lt(hi, mR), "one-digit fit failed"
        left, right = children(nd)
        assert not fits((left.l, left.r), lo, hi)
        assert not fits((right.l, right.r), lo, hi)
        gaps.append(math.log((frac(nd.r) - frac(nd.l)) / (hif - lof)))
        nd = children(nd)[0]
    print(f"    J straddling v with |J| <= 1/(q_v(q_max+q_v)) fits at")
    print(f"    ONE level (S_1) at every sample; its scale cost along")
    print(f"    the run: {['%.2f' % g for g in gaps]}")
    assert all(b > a for a, b in zip(gaps, gaps[1:])), \
        "scale gap should grow along the run"
    print("    the honest CF margin is ONE DIGIT, priced at the local")
    print("    roof — no scale-uniform log_b(1/rho) exists here")
    print()

# ----------------------------------------------------------------- #

def main():
    e1_geometry()
    e2_ladder()
    e3_wall_cure()
    e4_rate_gate()
    e5_margin()
    print("ALL ENGINES PASS")

if __name__ == "__main__":
    main()
    sys.exit(0)
