"""The bounded half of the parity law as a decision procedure: a stride
gates iff a finite deficit-walk graph carries a strict-interior cycle.

THE QUESTION
------------
The one-class stride law's gated half is derived (comb families landing
on cuts, explore_parity_derivation.py); the bounded half — no legal
pattern of ANY period lands a two-sided cut at an even nonzero residue —
stood enumerated at periods P and 2P only. This rig carries the upgrade:
an exact criterion deciding, per cell (P, A, r), whether ANY cut is
two-sidedly approachable by ANY legal string — all periods, aperiodic
strings included — as a cycle test on a finite graph, certified in
integer/rational arithmetic.

THE HAND-ATTACK (pre-engine, on paper; frame and index conventions
re-derived from explore_parity_derivation.py:
theta_k = q_k alpha - p_k, sign (-1)^k, theta_{k+P} = eta theta_k,
eta = -theta_{P-1}, |eta| < 1, sign (-1)^P; L = Z + Z alpha, eta L = L,
mult-by-eta = the integer matrix H, det +-1; conjugates theta'_k < 0
all k, |theta'_k| increasing, and eta' = -theta'_{P-1} > 1 at BOTH
parities of P, N(eta) = -1 at odd P)
----------------------------------------------------------------------
D1  THE DEFICIT WALK. An input's star is an integer combination and
    never sits exactly on a cut, so a gate at cut ell (lattice point
    with alpha-part <= -1) needs finite legal input pairs agreeing
    ever deeper whose stars sit STRICTLY on both sides of ell. By
    compactness their prefixes stabilize to an infinite legal c* with
    star exactly ell, and the straddles live in c*'s own cylinders:
    gate at ell <==> at infinitely many depths D, legal tails exist
    strictly on both sides of the deficit delta_D = ell - S_D. Each
    delta_D is in L, is nonzero (a finite hit would force the cut's
    alpha-part >= 0), sits in the exact tail interval
    [tmin(state), tmax(state)] of its (phase, predecessor-flag) state,
    and has POSITIVE conjugate: delta'_D = ell' - S'_D with ell' > 0
    and S'_D <= 0 since every theta' < 0.
D2  THE FINITE BOX. Normalizing by H^{-1} once per period keeps the
    deficit in L, keeps the real part in the fixed per-state tail
    interval, and — eta' > 1 positive — keeps the conjugate positive
    and eventually below the all-caps geometric bound
    B = (sum_i cap(i) |theta'_{i+r}|) * eta'/(eta'-1). So every gate
    walk's normalized deficits eventually live in the finite box
    {eps in L : tmin <= eps_real <= tmax, 0 < eps' <= B} — the
    recurrent states obey eps' <= B exactly by the limit over visits,
    and every late state obeys eps' <= B + ell'/eta'^t, which sits
    under the ENUMERATED bound because the rational enclosure used for
    it is strictly above B, so whole path segments between recurrences
    stay in the graph — and a straddle depth recurring infinitely
    often in a finite graph is a CYCLE through a state with
    tmin < eps_real < tmax STRICTLY.
D3  THE CRITERION (both directions). Gate at (P, A, r) <==> the box
    graph has a cycle through a strict-interior state. Necessity is
    D1+D2. Sufficiency: from such a state eps set ell = eta^t eps for
    large t — ell' = eta'^t eps' > 0 grows, so the alpha-part
    (ell - ell')/(alpha - alpha') drops below -1: a genuine cut; the
    walk "t periods of zeros, then the cycle forever" emits a legal
    string with star exactly ell, and each cycle visit yields a
    strict straddle pair (truncate the tmin- and tmax-attaining tails
    deep enough), parting at the fixed position p_s of the straddled
    cut. Any cycle in the real-pruned graph is automatically live
    (loop it), so no liveness fixed point is needed; eps = 0 is
    excluded by eps' > 0.
D4  EXACT INGREDIENTS. tmax/tmin per (phase, flag) are elements of
    Q(alpha) in CLOSED FORM: digit contributions are separable and
    weight signs alternate with position parity, so the extremum is
    caps at every wanted-sign position and zeros elsewhere — legal,
    each cap's predecessor being one of the zeros; only the first
    position feels the flag. The sum is a 2P-window sum over
    1 - eta^2 (a Bellman recursion is NOT valid here: the period-wrap
    multiplier eta is negative at odd P, so stage-wise maximization
    is unsound — the first draft hit exactly that). The conjugate bound B
    need not be sharp: any upper bound gives a superset box, and a
    NO verdict on a superset still certifies. Signs of u + w alpha
    and u + w alpha' are decided by the window's quadratic; alpha' =
    -A1/A2 - alpha makes conjugation an element operation, so the
    B-membership test clears denominators into pure element signs.
D5  WHAT THE VERDICTS MUST BE. The parity law (rule at scanned scope,
    explore_shift_repair.py, explore_limit_column.py): r = 0 mod P
    delay 0, even nonzero residues bounded, odd residues gate. The
    criterion must reproduce it — odd residues are the positive
    control (the derived comb gates must appear as interior cycles),
    r = 0 and even residues must print no interior cycle. The even-P
    even-r one-sided lattice hits (alternating combs at -q_{r-1}
    alpha, explore_parity_derivation.py F6) should appear as cycle states
    sitting AT an interval endpoint: the touch made structural.

THE HAND-ATTACK, SECOND PASS (pre-s3/s4, on paper; the cycle
classification the universal statement reduces to)
----------------------------------------------------------------------
D6  WHAT A CYCLE IS, EXACTLY. Unrolling the edge map, a cycle of
    length mP through eps IS a periodic legal pattern d (period mP)
    with eps = V(d) = sum_{k>=0} d_k theta_{k+r} = S_m/(1 - eta^m);
    the other cycle states are its suffixes' values, all in L once
    V is. The conjugate constraint is FREE: V' = S'_m/(1 - eta'^m)
    with S'_m < 0 for any nonzero pattern and 1 - eta'^m < 0, so
    V' > 0 automatically — the whole cycle condition is the LATTICE
    condition V(d) in L. Corollary (the reduction): a BOX lattice
    point's coding walk has bounded lattice deficits and cannot
    terminate — a terminating coding makes the point a finite sum,
    whose conjugate is negative while box points' is positive — so it
    recurs in the finite box, and cycles exist iff box lattice points
    lie in the shifted VALUE SET: the period quantifier is absorbed.
D7  THE TELESCOPE COMBS. The recurrence identity a_{k+1} theta_k =
    theta_{k+1} - theta_{k-1} (all k, caps included; theta_{-1} = -1,
    p_{-1} = 1) telescopes exactly three pattern families into L:
    C1 (even P, any even r): 1 at even positions — every even
    position has cap 1 since the class phase P-1 is odd — with value
    -theta_{r-1} = tmax; its suffixes sit at every state's tmax (from
    an odd position the comb IS the max tail: 0 first, then teeth).
    C2 (even P, r = 0 only): caps at odd positions, value
    -theta_0 = -alpha = tmin. C3 (odd P, r = 0 only): caps at even
    GLOBAL positions, period 2P (the class phase's global parity
    alternates), threading tmax and tmin states in one loop, values
    1 and -alpha. At r even NONZERO the tmin-side pattern puts the
    class cap A at a shifted-weight cap-1 slot and the telescope
    breaks — and tmin is certifiably NOT a lattice point at every
    scanned cell (its attaining pattern IS periodic legal, so a
    lattice tmin would print as a cycle; s4 prints none), which is
    why only tmax-side cycles exist. At odd P, r even nonzero, BOTH
    extremal telescopes break, and acyclicity certifies neither
    extreme is a lattice point at scanned scope by the same argument. At r = 0 the digit cap equals the weight cap
    at every position, so both classical telescopes survive at both
    parities — the r = 0 column carries 2P endpoint cycle states
    EVERYWHERE (F6), and r = 0 boundedness is anyway a theorem
    (the period shift is the bare coordinate map), so by the
    criterion's sufficiency leg those cells' interior emptiness is
    PROVED, not only certified.
D8  THE EXCESS FRAME (what remains open, sharpened; the frame since
    transported onto the rotated window's aligned problem at foreign
    caps — explore_lattice_avoidance.py D1-D4 — with the statements
    below surviving as the per-parity forms). At even P, even
    r, subtracting a pattern from C1 turns the lattice condition into
    a GAP statement: W = tmax - V(d) = sum w_k |theta_{k+r}| with
    w >= 0, and the universal bounded half is exactly "no periodic
    LEGAL d beyond C1 and the zero pattern has W in L" (the zero
    pattern's W = tmax and V = 0 are lattice — the conjugate sign is
    what excludes eps = 0 from the box; at r = 0 the cap combs join
    the exceptions). At odd P the claim is lattice-emptiness for
    every NONZERO periodic legal pattern. Both are statements about
    the FINITELY many box lattice points per cell (D6), no period
    quantifier left. And LEGALITY IS LOAD-BEARING, not a convenience:
    dropping the cap-after-nonzero coupling admits small witnesses —
    the nonneg patterns (0,1,1,2) at (P,A,r) = (4,2,2) and
    (0,1,1,1,1,2) at (6,2,4), each violating the coupling at its
    period wrap, sum to exactly theta_r (exact-arithmetic check,
    periods P and 2P) — so any proof must consume the coupling, and
    a character or mass argument blind to digit ADJACENCY cannot
    close it.

PREDICTIONS, FIXED BEFORE THE RUN (observables — what the rig PRINTS)
  N1 (positive controls, run FIRST; red voids the run): H self-test;
      the closed-form extremes agree with a 60-position finite-horizon
      DP to the truncation tail; at r = 0 the unshifted extremes are
      the classical telescopes: tmax(0, free) = 1 and tmin(0, free)
      = -alpha exactly.
  N2 (the grid): for P = 2..8, A = 2, 3, 4, r = 0..P-1: the criterion's
      verdict equals the parity law at EVERY cell — GATE exactly at
      odd residues. KILL of the criterion or of the law: any cell off;
      either is a finding.
  N3 (the touch): at even P and even nonzero r, at least one cycle
      state sits AT tmax or tmin (endpoint, one-sided) while interior
      cycle states are zero.
  N4 (stability): doubling B at even- and odd-residue cells leaves
      the verdicts unchanged.
  N5 (the loops; frozen in s3's docstring pre-run): even P,
      even nonzero r — one P-loop, digits alternating 1 at even
      global positions, every state AT its tmax; r = 0 — 2P endpoint
      states at BOTH parities, two P-loops at even P, one 2P-loop at
      odd P; odd P, even nonzero r — nothing.
  N6 (the classification; frozen in s4's docstring pre-run):
      at every even-residue grid cell the cycle set EQUALS the
      applicable telescope-comb deficit orbits of D7, with zero
      interior states.

FINDINGS (run record at the end; every stage green, verdicts exact)
----------------------------------------------------------------------
F1  CONTROLS PASS (N1): H exact at 5 cells; the closed-form extremes
    match the depth-60 finite-horizon DP at every (phase, flag) state
    of 5 cells x 3 strides (2 distinct at P = 2) x both directions;
    at r = 0 the extremes
    are the classical telescopes exactly, tmax(0, free) = 1 and
    tmin(0, free) = -alpha. (The DP control itself had to compute
    theta from a depth-200 convergent in exact fractions — the float
    form q_k alpha - p_k is cancellation garbage past k ~ 40, the
    known float wall.)
F2  EVERY CELL LANDS ON THE PARITY LAW (N2; certificate at scanned
    scope, each cell exhaustive over ALL strings and ALL periods):
    105 cells, P = 2..8, A = 2, 3, 4, r = 0..P-1 — interior cycle
    states exist exactly at the odd residues. So at every scanned
    cell the bounded half is now DECIDED, not enumerated: no legal
    string of any period (aperiodic included) lands a two-sided cut
    at r = 0 or any even nonzero residue.
F3  THE TOUCH IS STRUCTURAL (N3): all 18 even-P even-NONZERO-r cells
    carry exactly P cycle states, every one sitting AT an interval
    endpoint (the alternating-comb family, one per phase), zero
    interior: the one-sided lattice approach exists and is
    extremal-pinned — explore_parity_derivation.py F6's
    touch-without-crossing, now over all periods.
F4  ODD P IS EMPTIER (finding beyond the slate; scope since
    repaired — the first write said "even-r", but the r = 0 column
    carries cycles at both parities, F6): at every odd-P
    even-NONZERO-r cell the box graph carries NO cycle at all. Any
    legal string with infinitely many nonzero digits and a lattice
    star has deficits eventually positive-conjugate and boxed
    (S' -> -infinity makes delta' > 0 whatever the target's conjugate
    sign), so acyclicity says every lattice hit at these cells is a
    FINITE string's exact star — no infinite approach, one-sided
    included. The even-P/odd-P obstruction split named at
    the minting (extremal-tail vs lattice-emptiness) is exactly what
    the cycles show: endpoint cycles at even P, acyclicity at odd P.
F5  STABILITY (N4): doubling the conjugate bound leaves all four
    probed verdicts unchanged.
F6  THE LOOPS ARE THE COMBS (N5 lands at every printed cell): even-P
    even-nonzero-r cells carry the single C1 loop, digits (1, 0)
    alternating, every state AT its tmax, values the -theta_{r+2j-1}
    family; every r = 0 cell carries 2P endpoint states — two
    P-loops at even P (C1 at tmax, C2 at tmin), ONE 2P-loop at odd P
    threading the tmax and tmin halves (C3, digit loop e.g.
    1,0,2,0,1,0 at P = 3); odd-P even-nonzero-r cells print nothing.
    Odd residues, for contrast, are richer than any comb list: at
    (2, 3, 1) the cycle states are the integer MULTIPLES k(1 - alpha),
    k = 1..3, each its own 2-loop — interior at k = 1, 2, the
    endpoint at k = 3 — and (6, 4, 3)
    carries an 11-state branching SCC — the classification below is
    an even-residue fact, not a general one.
F7  THE CLASSIFICATION IS CERTIFIED AT SCANNED SCOPE (N6 lands): at
    all 57 even-residue cells (P = 2..8, A = 2, 3, 4) the cycle set
    EQUALS the telescope-comb deficit orbits — exact state-set
    equality against closed-form witnesses, the orbit walker
    asserting integer coordinates and closure, zero interior
    everywhere. With D6 this pins the universal statement to two
    lemmas with no period quantifier: the even-P excess-gap lemma
    and the odd-P lattice-emptiness lemma (D8).

RUN RECORD: python explore_bounded_half.py — s0..s4, 45 s wall,
memory trivial, ALL STAGES GREEN.

THE DESIGN
----------
Exact end to end: bigint convergents (Cell frame as in
explore_parity_derivation.py), Q(alpha) arithmetic on Fraction pairs
with alpha^2 reduced by the window's quadratic, both embeddings' signs
decided through that quadratic, H and H^{-1} integer. Per cell:
closed-form tmin/tmax over the 2P (phase, flag) states; box
enumeration from interval enclosures (convergents for alpha,
alpha' = -A1/A2 - alpha) then exact membership filters; edges by
digit subtraction with H^{-1} at the period wrap; Tarjan SCC; cycle
states classified endpoint/interior by strict exact signs. Stages:
s0 controls, s1 grid + touch, s2 stability, s3 loop data,
s4 comb-orbit classification; no argument runs all.
Wall-clock: seconds to a few minutes; memory trivial.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_parity_derivation import Cell        # noqa: E402


# ------------------------------------------------------- Q(alpha) exact

class Field:
    """Q(alpha) for a cell: elements are (u, w) Fractions = u + w*alpha,
    alpha^2 = (-A1 alpha - A0)/A2; conjugation alpha' = -A1/A2 - alpha;
    signs in both embeddings via the quadratic."""

    def __init__(self, cell):
        self.c = cell
        self.A2, self.A1, self.A0 = cell.A2, cell.A1, cell.A0
        self.tr = Fraction(-self.A1, self.A2)   # alpha + alpha'

    def add(self, x, y):
        return (x[0] + y[0], x[1] + y[1])

    def sub(self, x, y):
        return (x[0] - y[0], x[1] - y[1])

    def mul(self, x, y):
        # (u1 + w1 a)(u2 + w2 a); a^2 = (-A1 a - A0)/A2
        u = x[0] * y[0] - x[1] * y[1] * Fraction(self.A0, self.A2)
        w = x[0] * y[1] + x[1] * y[0] \
            - x[1] * y[1] * Fraction(self.A1, self.A2)
        return (u, w)

    def conj(self, x):
        return (x[0] + x[1] * self.tr, -x[1])

    def inv(self, x):
        cx = self.conj(x)
        n = self.mul(x, cx)
        assert n[1] == 0 and n[0] != 0
        return (cx[0] / n[0], cx[1] / n[0])

    def scale(self, x, k):
        return (x[0] * k, x[1] * k)

    def sign_real(self, x):
        u, w = x
        if w == 0:
            return (u > 0) - (u < 0)
        num_u, num_w = u.numerator * w.denominator, \
            w.numerator * u.denominator
        # sign of num_u + num_w * alpha (positive common denom)
        return self.c.sign_lin(num_w, -num_u)

    def sign_conj(self, x):
        u, w = x
        if w == 0:
            return (u > 0) - (u < 0)
        # sign of u + w alpha', alpha' the negative root
        x_i, y_i = w.numerator * u.denominator, \
            -u.numerator * w.denominator
        # sign of x_i * alpha' - y_i
        t = Fraction(y_i, x_i)
        if t >= 0:
            return -1 if x_i > 0 else 1
        val = self.A2 * t * t + self.A1 * t + self.A0
        if val == 0:
            return 0
        s = -1 if val < 0 else 1      # f(t)<0, t<0  =>  t in (alpha', 0)
        return s if x_i > 0 else -s


# -------------------------------------------------- per-cell machinery

class Rig:
    def __init__(self, P, A, r):
        self.P, self.A, self.r = P, A, r
        self.cell = Cell(P, A)
        self.F = Field(self.cell)
        self.eta = (Fraction(self.cell.p[P - 1]),
                    Fraction(-self.cell.q[P - 1]))
        self.caps = [A if (i + 1) % P == 0 else 1 for i in range(P)]
        h = self.cell.H
        det = h[0] * h[3] - h[1] * h[2]
        assert abs(det) == 1
        self.Hinv = (h[3] * det, -h[1] * det, -h[2] * det, h[0] * det)
        self.theta = {}
        for k in range(2 * P + 2):
            self.theta[k] = (Fraction(-self.cell.p[k]),
                             Fraction(self.cell.q[k]))
        self.tmax = self.extreme(+1)
        self.tmin = self.extreme(-1)

    # states (phi, z): z = 1 iff previous digit was zero (cap allowed)
    def allowed(self, phi, z):
        cap = self.caps[phi]
        top = cap if z else cap - 1
        return range(0, max(top, 0) + 1)

    def step_state(self, phi, c):
        return ((phi + 1) % self.P, 1 if c == 0 else 0)

    def extreme(self, direction):
        """Exact sup (+1) or inf (-1) of legal tail sums per (phi, z),
        in closed form. Contributions are separable and weight signs
        alternate with position parity, so the optimum is caps at
        every position whose weight has the wanted sign and zeros
        elsewhere — legal, since each cap's predecessor is one of the
        zeros. Only the first position feels the z flag (a blocked cap
        drops to cap-1). The unconstrained sum from any start is a
        2P-window sum divided by 1 - eta^2 (eta^2 > 0 at both
        parities of P)."""
        F, P, r = self.F, self.P, self.r
        want = 0 if direction > 0 else 1     # (k+r) parity of wanted sign
        eta2 = F.mul(self.eta, self.eta)
        one = (Fraction(1), Fraction(0))
        inv1me2 = F.inv(F.sub(one, eta2))
        T = {}
        for phi in range(P):
            for z in (0, 1):
                if (phi + r) % 2 == want:
                    cap = self.caps[phi]
                    c0 = cap if z else cap - 1
                    val = F.add(F.scale(self.theta_abs(phi), c0),
                                self.window_sum(phi + 2, want, inv1me2))
                else:
                    val = self.window_sum(phi + 1, want, inv1me2)
                T[(phi, z)] = val
        return T

    def theta_abs(self, k):
        """theta_{k+r} as an element, any k >= 0, via eta-periodicity."""
        F = self.F
        base = k % self.P
        el = self.theta[base + self.r]
        for _ in range(k // self.P):
            el = F.mul(self.eta, el)
        return el

    def window_sum(self, m, want, inv1me2):
        """sum over k >= m, (k+r) % 2 == want, of cap(k) theta_{k+r}:
        one 2P window exactly, then the geometric factor."""
        F = self.F
        w = (Fraction(0), Fraction(0))
        for k in range(m, m + 2 * self.P):
            if (k + self.r) % 2 == want:
                w = F.add(w, F.scale(self.theta_abs(k),
                                     self.caps[k % self.P]))
        return F.mul(w, inv1me2)

    # ----------------------------------------------------- the box

    def conj_bound_el(self):
        """Element Y*eta with Y = sum cap(i)*(-theta_{i+r}) whose conj
        value is B*(eta'-1); membership eps' <= B is tested as
        conj(Y*eta - eps*(eta-1)) >= 0."""
        F = self.F
        Y = (Fraction(0), Fraction(0))
        for i in range(self.P):
            Y = F.add(Y, F.scale((-self.theta[i + self.r][0],
                                  -self.theta[i + self.r][1]),
                                 self.caps[i]))
        return F.mul(Y, self.eta)

    def in_box(self, phi, z, eps, bscale=1):
        F = self.F
        el = (Fraction(eps[0]), Fraction(eps[1]))
        if F.sign_real(F.sub(el, self.tmin[(phi, z)])) < 0:
            return False
        if F.sign_real(F.sub(self.tmax[(phi, z)], el)) < 0:
            return False
        if F.sign_conj(el) <= 0:
            return False
        lhs = F.sub(F.scale(self.Yeta, bscale),
                    F.mul(el, F.sub(self.eta, (Fraction(1),
                                               Fraction(0)))))
        return F.sign_conj(lhs) >= 0

    def enumerate_box(self, bscale=1):
        F = self.F
        self.Yeta = self.conj_bound_el()
        # interval enclosures
        K = 60
        c = self.cell
        lo, hi = sorted((Fraction(c.p[K], c.q[K]),
                         Fraction(c.p[K + 1], c.q[K + 1])))
        alo, ahi = lo, hi                       # alpha
        cplo, cphi = self.F.tr - ahi, self.F.tr - alo   # alpha'
        def enc(el):
            u, w = el
            vals = [u + w * alo, u + w * ahi]
            return min(vals), max(vals)
        def enc_conj(el):
            u, w = el
            vals = [u + w * cplo, u + w * cphi]
            return min(vals), max(vals)
        rlo = min(enc(self.tmin[s])[0] for s in self.tmin)
        rhi = max(enc(self.tmax[s])[1] for s in self.tmax)
        # B upper: conj(Yeta)/(eta'-1); eta' > 1 always
        ylo, yhi = enc_conj(self.Yeta)
        elo, ehi = enc_conj(self.eta)
        assert elo > 1, "eta' enclosure must exceed 1"
        Bhi = (yhi / (elo - 1)) * bscale
        gap_lo = alo - cphi          # lower bound of alpha - alpha' > 0
        wlo = int((rlo - Bhi) / gap_lo) - 2
        whi = int((rhi - 0) / gap_lo) + 2
        nodes = {}
        for w in range(wlo, whi + 1):
            us = [rlo - w * ahi, rlo - w * alo, rhi - w * ahi,
                  rhi - w * alo]
            for u in range(int(min(us)) - 2, int(max(us)) + 3):
                if u == 0 and w == 0:
                    continue
                for phi in range(self.P):
                    for z in (0, 1):
                        if self.in_box(phi, z, (u, w), bscale):
                            nodes[(phi, z, u, w)] = True
        return nodes

    def edges_from(self, node, nodes, bscale=1):
        phi, z, u, w = node
        out = []
        for c in self.allowed(phi, z):
            # theta_{phi+r} has integer coords (-p, q)
            u2 = u + c * self.cell.p[phi + self.r]
            w2 = w - c * self.cell.q[phi + self.r]
            if phi == self.P - 1:
                hi = self.Hinv
                u2, w2 = hi[0] * u2 + hi[1] * w2, hi[2] * u2 + hi[3] * w2
            z2 = 1 if c == 0 else 0
            nxt = ((phi + 1) % self.P, z2, u2, w2)
            if nxt in nodes:
                out.append(nxt)
        return out

    def classify(self, node):
        """'interior' if strictly inside (tmin, tmax); else 'endpoint'."""
        phi, z, u, w = node
        F = self.F
        el = (Fraction(u), Fraction(w))
        lo = F.sign_real(F.sub(el, self.tmin[(phi, z)]))
        hi = F.sign_real(F.sub(self.tmax[(phi, z)], el))
        return "interior" if (lo > 0 and hi > 0) else "endpoint"

    def verdict(self, bscale=1):
        nodes = self.enumerate_box(bscale)
        graph = {n: self.edges_from(n, nodes, bscale) for n in nodes}
        cyc = cycle_states(graph)
        interior = [n for n in cyc if self.classify(n) == "interior"]
        endpoint = [n for n in cyc if self.classify(n) == "endpoint"]
        return len(nodes), cyc, endpoint, interior


def cycle_states(graph):
    """States lying on some cycle: iterative Tarjan SCC; SCCs of size
    > 1, plus self-loops."""
    index, low, on, stk = {}, {}, {}, []
    result, counter = [], [0]
    for start in graph:
        if start in index:
            continue
        work = [(start, iter(graph[start]))]
        index[start] = low[start] = counter[0]
        counter[0] += 1
        stk.append(start)
        on[start] = True
        while work:
            v, it = work[-1]
            advanced = False
            for nxt in it:
                if nxt not in index:
                    index[nxt] = low[nxt] = counter[0]
                    counter[0] += 1
                    stk.append(nxt)
                    on[nxt] = True
                    work.append((nxt, iter(graph[nxt])))
                    advanced = True
                    break
                elif on.get(nxt):
                    low[v] = min(low[v], index[nxt])
            if advanced:
                continue
            work.pop()
            if work:
                pv = work[-1][0]
                low[pv] = min(low[pv], low[v])
            if low[v] == index[v]:
                scc = []
                while True:
                    n = stk.pop()
                    on[n] = False
                    scc.append(n)
                    if n == v:
                        break
                result.append(scc)
    cyc = set()
    for scc in result:
        if len(scc) > 1:
            cyc.update(scc)
        elif scc[0] in graph[scc[0]]:
            cyc.add(scc[0])
    return cyc


def law(P, r):
    m = r % P
    if m == 0:
        return "B"
    return "G" if m % 2 == 1 else "B"


# ---------------------------------------------------------------- stages

def dp_extreme(rig, direction, horizon=60):
    """Finite-horizon DP over legal strings (exact optimum of the
    truncated problem): the independent check on the closed form.
    theta is computed from a depth-200 convergent in exact fractions —
    q_k * float(alpha) - p_k cancels catastrophically past k ~ 40."""
    c = rig.cell
    alpha_r = Fraction(c.p[200], c.q[200])
    th = [float(c.q[k] * alpha_r - c.p[k])
          for k in range(horizon + rig.r + 2)]
    V = {z: 0.0 for z in (0, 1)}          # value from position >= horizon
    out = {}
    for k in range(horizon - 1, -1, -1):
        phi = k % rig.P
        NV = {}
        for z in (0, 1):
            vals = []
            for cd in rig.allowed(phi, z):
                vals.append(cd * th[k + rig.r] + V[1 if cd == 0 else 0])
            NV[z] = max(vals) if direction > 0 else min(vals)
        V = NV
        if k < rig.P:
            for z in (0, 1):
                out[(k, z)] = V[z]
    return out


def s0_controls():
    print("=" * 74)
    print("S0 CONTROLS: H self-test, closed-form extremes vs finite DP,"
          " classical r = 0 extremes")
    bad = 0
    for (P, A) in ((2, 3), (3, 2), (4, 2), (5, 3), (7, 2)):
        cell = Cell(P, A)
        if not cell.h_selftest():
            bad += 1
            print(f"  FAIL H P={P} A={A}")
        for r in (0, 1, 2 % P):
            rig = Rig(P, A, r)
            for (direction, tab) in ((+1, rig.tmax), (-1, rig.tmin)):
                dp = dp_extreme(rig, direction)
                for (phi, z), v in dp.items():
                    ex = tab[(phi, z)]
                    exf = float(ex[0]) + float(ex[1]) * (
                        (-cell.A1 + (cell.A1 ** 2
                                     - 4 * cell.A2 * cell.A0) ** .5)
                        / (2 * cell.A2))
                    if abs(exf - v) > 1e-6:
                        bad += 1
                        print(f"  FAIL DP P={P} A={A} r={r} "
                              f"({phi},{z}) dir={direction}: "
                              f"closed={exf} dp={v}")
        rig = Rig(P, A, 0)
        F = rig.F
        one = (Fraction(1), Fraction(0))
        alpha = (Fraction(0), Fraction(1))
        t1 = F.sub(rig.tmax[(0, 1)], one)
        t2 = F.add(rig.tmin[(0, 1)], alpha)
        if F.sign_real(t1) != 0 or F.sign_real(t2) != 0:
            bad += 1
            print(f"  FAIL r=0 extremes P={P} A={A}: "
                  f"tmax-1={t1} tmin+alpha={t2}")
    print(f"  {'PASS' if bad == 0 else 'FAIL'}: H exact, closed-form "
          f"extremes match the DP, tmax(0,free) = 1 and "
          f"tmin(0,free) = -alpha at r = 0")
    return bad == 0


def s1_grid():
    print("=" * 74)
    print("S1 THE GRID: criterion verdict vs the parity law,"
          " P = 2..8, A = 2, 3, 4, r = 0..P-1")
    bad = 0
    touch_even = touch_needed = 0
    for P in range(2, 9):
        for A in (2, 3, 4):
            for r in range(0, P):
                rig = Rig(P, A, r)
                n, cyc, endp, inter = rig.verdict()
                v = "G" if inter else "B"
                want = law(P, r)
                ok = v == want
                if not ok:
                    bad += 1
                mark = "" if ok else "   <-- OFF THE LAW"
                print(f"  P={P} A={A} r={r}: box={n} cyc={len(cyc)} "
                      f"endpoint={len(endp)} interior={len(inter)} "
                      f"-> {v} (law {want}){mark}")
                if P % 2 == 0 and r % P != 0 and r % 2 == 0:
                    touch_needed += 1
                    if endp and not inter:
                        touch_even += 1
    print(f"  {'PASS' if bad == 0 else 'FAIL'}: every cell on the law")
    print(f"  touch: {touch_even}/{touch_needed} even-P even-r cells "
          f"carry endpoint cycle states with zero interior")
    return bad == 0


def s3_loops():
    """Print the cycle states and their digit loops as data (the
    universal statement's object). Per cell: each SCC's states as
    exact elements with an endpoint identification (tmax / tmin /
    interior), and the labeled edges inside the cycle set — the digit
    loops the periodic patterns run. Predictions (frozen pre-run):
    even P, even nonzero r — one P-loop, digits alternating 1 at even
    global positions, every state AT its tmax; r = 0 — 2P endpoint
    states at BOTH parities (the two classical full-cap telescopes,
    values 1 and -alpha), two P-loops at even P and one 2P-loop at odd
    P; odd P, even nonzero r — nothing; odd r — interior loops printed
    as data, no structure frozen."""
    print("=" * 74)
    print("S3 THE LOOPS: cycle states + digit loops, per cell")
    cells = [(4, 2, 2), (6, 3, 2), (6, 3, 4), (8, 2, 2),
             (3, 2, 0), (4, 2, 0), (5, 2, 0),
             (2, 3, 1), (3, 2, 1), (6, 4, 3)]
    for (P, A, r) in cells:
        rig = Rig(P, A, r)
        n, cyc, endp, inter = rig.verdict()
        print(f"  --- P={P} A={A} r={r}: box={n} cyc={len(cyc)} "
              f"endpoint={len(endp)} interior={len(inter)}")
        F = rig.F
        for node in sorted(cyc):
            phi, z, u, w = node
            el = (Fraction(u), Fraction(w))
            at = []
            if F.sign_real(F.sub(el, rig.tmax[(phi, z)])) == 0:
                at.append("tmax")
            if F.sign_real(F.sub(el, rig.tmin[(phi, z)])) == 0:
                at.append("tmin")
            tag = "+".join(at) if at else "interior"
            # labeled edges inside the cycle set
            succ = []
            for c in rig.allowed(phi, z):
                u2 = u + c * rig.cell.p[phi + r]
                w2 = w - c * rig.cell.q[phi + r]
                if phi == P - 1:
                    hi = rig.Hinv
                    u2, w2 = (hi[0] * u2 + hi[1] * w2,
                              hi[2] * u2 + hi[3] * w2)
                z2 = 1 if c == 0 else 0
                nxt = ((phi + 1) % P, z2, u2, w2)
                if nxt in cyc:
                    succ.append(f"-{c}-> (phi={nxt[0]},z={nxt[1]},"
                                f"{nxt[2]}{nxt[3]:+d}a)")
            print(f"    (phi={phi},z={z}) eps={u}{w:+d}a [{tag}] "
                  f"{'; '.join(succ)}")
    return True


def comb_orbit(rig, pattern):
    """Exact deficit orbit of a periodic legal pattern: suffix values
    V_D normalized once per period, each asserted integer-coordinated;
    returns the set of (phi, z, u, w) states. Asserts closure
    (V_N returns to V_0)."""
    F, P, r = rig.F, rig.P, rig.r
    N = len(pattern)
    assert N % P == 0
    m = N // P
    T = (Fraction(0), Fraction(0))
    for k in range(N):
        T = F.add(T, F.scale(rig.theta_abs(k), pattern[k]))
    etam = (Fraction(1), Fraction(0))
    for _ in range(m):
        etam = F.mul(etam, rig.eta)
    one = (Fraction(1), Fraction(0))
    V = F.mul(T, F.inv(F.sub(one, etam)))
    states = set()
    eps = V
    for D in range(N):
        assert eps[0].denominator == 1 and eps[1].denominator == 1
        z = 1 if pattern[(D - 1) % N] == 0 else 0
        states.add((D % P, z, int(eps[0]), int(eps[1])))
        eps = F.sub(eps, F.scale(rig.theta[(D % P) + r], pattern[D]))
        if D % P == P - 1:
            eps = F.mul(eps, F.inv(rig.eta))
    assert eps == V, "orbit must close"
    return states


def s4_classification():
    """Certify the cycle classification in closed form at every
    even-residue cell of the grid: the cycle set EQUALS the telescope
    combs' deficit orbits. Predictions (frozen pre-run): even P, even
    nonzero r — the alternating comb C1 (1 at even positions) alone,
    P states; r = 0, even P — C1 plus the odd-position cap comb C2,
    2P states; r = 0, odd P — the 2P-periodic global-parity cap comb
    C3 alone, 2P states; odd P, even nonzero r — no combs, no cycles.
    Every orbit state sits AT an interval endpoint (zero interior)."""
    print("=" * 74)
    print("S4 CLASSIFICATION: cycle set == telescope-comb orbits,"
          " every even residue")
    bad = 0
    cells = 0
    for P in range(2, 9):
        for A in (2, 3, 4):
            for r in range(0, P, 2):
                rig = Rig(P, A, r)
                n, cyc, endp, inter = rig.verdict()
                expect = set()
                if P % 2 == 0:
                    expect |= comb_orbit(
                        rig, [1 if k % 2 == 0 else 0 for k in range(P)])
                    if r == 0:
                        expect |= comb_orbit(
                            rig, [0 if k % 2 == 0 else rig.caps[k]
                                  for k in range(P)])
                elif r == 0:
                    expect |= comb_orbit(
                        rig, [rig.caps[k % P] if k % 2 == 0 else 0
                              for k in range(2 * P)])
                ok = (set(cyc) == expect) and not inter
                if not ok:
                    bad += 1
                cells += 1
                print(f"  P={P} A={A} r={r}: cyc={len(cyc)} "
                      f"comb-orbit={len(expect)} interior={len(inter)}"
                      f"{'' if ok else '   <-- OFF THE CLASSIFICATION'}")
    print(f"  {'PASS' if bad == 0 else 'FAIL'}: {cells} even-residue "
          f"cells, cycle set == comb orbits at every one")
    return bad == 0


def s2_stability():
    print("=" * 74)
    print("S2 STABILITY: doubling the conjugate bound leaves verdicts"
          " unchanged")
    bad = 0
    for (P, A, r) in ((4, 2, 2), (5, 3, 2), (5, 3, 1), (6, 3, 4)):
        rig = Rig(P, A, r)
        v1 = "G" if rig.verdict(1)[3] else "B"
        v2 = "G" if rig.verdict(2)[3] else "B"
        ok = v1 == v2
        if not ok:
            bad += 1
        print(f"  P={P} A={A} r={r}: B x1 -> {v1}, B x2 -> {v2}"
              f"{'' if ok else '   <-- MOVED'}")
    print(f"  {'PASS' if bad == 0 else 'FAIL'}")
    return bad == 0


def main():
    stages = {"s0": s0_controls, "s1": s1_grid, "s2": s2_stability,
              "s3": s3_loops, "s4": s4_classification}
    args = sys.argv[1:] or list(stages)
    ok = True
    for a in args:
        ok = stages[a]() and ok
    print("=" * 74)
    print("ALL STAGES GREEN" if ok else "RED - read the failures above")


if __name__ == "__main__":
    main()
