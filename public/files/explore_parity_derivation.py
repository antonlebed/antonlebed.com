"""Why does the parity of r mod P decide a one-class stride? The stride
law's mechanism derived: comb families whose image points land on a cut.

THE QUESTION
------------
At the designed one-class family [0; (1^(P-1), A)^inf] the limit verdict
is a function of r mod P alone: r = 0 mod P reads at delay 0, even
nonzero residues are finite, odd residues gate (explore_shift_repair.py,
explore_limit_column.py P1). The record files the mechanism as a
reading, not a derivation. This rig carries the derivation's checkable
half: explicit comb families, constructed in closed form rather than
searched, whose shifted image points provably accumulate at a CUT of the
window's coding circle — the two-coding points -s*alpha — from both
sides, which forces the two greedy images apart at the fixed position
p_s = min{p : q_{p+1} >= max(s, 2)} while input agreement climbs without
bound. Gating becomes a per-cell exact certificate in integer
arithmetic; the automaton stays the independent verdict instrument.

THE HAND-ATTACK (pre-engine, on paper; index conventions re-derived
from explore_shift_repair.py: 0-based positions, cap(k) = a_{k+1},
digit at cap forces predecessor 0; theta_k = q_k alpha - p_k with
theta_{k+P} = eta theta_k, eta = p_{P-1} - q_{P-1} alpha, |eta| < 1,
sign (-1)^P, eta L = L for L = Z + Z alpha, acting by the integer
matrix H with H theta_k = theta_{k+P} coordinatewise)
----------------------------------------------------------------------
D1  THE FRAME. A shift image's value is its input's shifted weight sum,
    so its circle point is the shifted pseudo-star sum(d_k theta_{k+r})
    mod 1. Input families agreeing ever deeper have image points
    converging to one point; the greedy images differ at a bounded
    position forever iff the images land in different cells at that
    depth forever, and the depth-t cells are arcs with endpoints in the
    cut orbit {-s alpha : s >= 1} — so a gate needs the accumulation
    point to BE a cut and the approach to realize both sides.
D2  PERIODIC COMBS. A cyclic digit pattern c = (c_0..c_{P-1}) repeated
    from position 0 contributes per period j the image star eta^j Psi,
    Psi = sum_i c_i theta_{i+r}; the truncation after M periods misses
    the limit lambda = Psi/(1-eta) by exactly lambda eta^M. The
    limit is in L iff Psi is in (1-eta)L — an integer 2x2 solve against
    I - H — and is a cut iff its alpha-coordinate w is <= -1 (then
    s = -w).
D3  ODD P, ODD r — THE FAMILY. c = 1 at even positions 2, 4, .., P-3
    and 2 at the class P-1 (legal at every A >= 2). In Q = L/(1-eta)L,
    with t_j = F_{j+1} abar - F_j and the two defining relations
    R1: F_P abar = F_{P-1} - 1, R2: (F_{P-1}-1) abar = A + F_{P-2},
    the shifted sum telescopes for EVERY odd r:
    alpha-coefficient 2F_r + F_{r-1} - F_{r+2} = 0 and integer part
    F_{r-1} + F_r - F_{r+1} = 0 leave exactly F_P abar - (F_{P-1} - 1),
    zero by R1. So Psi is in (1-eta)L at every odd r: the comb's image
    limit lambda sits in L, independent of A. Whether lambda's
    alpha-part is <= -1 is checked exactly per cell. Since eta < 0 at
    odd P, the deficit lambda eta^{M+1} ALTERNATES sign: consecutive
    truncations are themselves an input pair agreeing through M periods
    whose images sit on opposite sides of the cut — the straddle is
    free.
D4  EVEN P, ODD r — CLOSED FORM. The class sits at odd positions, so
    every even position has cap 1 and theta_{2j} = theta_{2j+1} -
    theta_{2j-1}. The alternating comb (1 at every odd position) is
    legal; shifted by odd r its image teeth sit at even positions
    r+1+2j and TELESCOPE: partial sums theta_{K+1} - theta_r, so the
    image limit is exactly -theta_r = -(q_r alpha - p_r): THE CUT
    -q_r alpha, s = q_r, at every even-P one-class window and every odd
    r — predicting parting position p_{q_r} (= 1 at r = 1, r - 1 at
    r >= 3). The deficit theta_{K+1} keeps one sign (eta > 0); the
    straddle partner raises the comb's deepest CLASS tooth from 1 to 2
    (legal, A >= 2), adding theta at a position class+r = 0 mod P whose
    theta is positive with magnitude strictly above the deficit by
    index monotonicity — an unconditional straddle, proved.
D5  EVEN r — THE BOUNDED HALF (open, enumerated). No legal cyclic
    pattern of period P or 2P has its image limit in L at any even
    nonzero residue scanned (exact enumeration), except the even-P
    even-r alternating combs whose limit is the cut -theta_{r-1}
    approached from ONE side only (the first write said -theta_r,
    transplanting the odd-r formula; the stage's own prints land at
    -q_{r-1} alpha — since repaired). The universal statement — no comb of
    ANY period — is the derivation's open leg, and the invariant it
    owes cannot be a character of L/(1-eta)L alone: P = 5, A = 3 has
    |L/(1-eta)L| = 21, odd, no Z/2 quotient, yet r = 2, 4 stay bounded.
    (Settled per cell since: explore_bounded_half.py decides the
    bounded half over ALL strings and ALL periods by a cycle test on
    the deficit-walk graph; what survives here is the enumeration's
    role as this rig's own control and the universal-in-(P, A)
    statement, still open there.)

PREDICTIONS, FIXED BEFORE THE RUN (observables — what the rig PRINTS)
  N1 (positive controls, run FIRST; red voids the run): H theta_k =
      theta_{k+P} exactly for k = 0..3P at every grid cell; the exact
      sign machinery agrees with sign(q_k alpha - p_k) = (-1)^k at
      k = 1..30.
  N2 (odd-P zero-sum, the D3 identity as integers): for P = 3, 5, 7,
      9, 11, A = 2..6, every odd r in 1..P-1: (I - H) lambda = Psi has
      an integer solution lambda, and its alpha-part w is <= -1.
      KILL: any cell without a solution or with w >= 0.
  N3 (even-P telescope as integers): for P = 2, 4, 6, 8, 10, A = 2..6,
      every odd r: sum of the comb's shifted weights q equals
      q_{K+1} - q_r (and p likewise) at every truncation depth K
      scanned. KILL: any mismatch.
  N4 (odd-P ladders: gate certificates). For P = 3, 5, 7, A = 2, 3,
      odd r, comb truncations M = 2..12: input agreement depth climbs
      by P per step; the exact sign of (image value + s) alpha - m
      alternates with M; the greedy images of consecutive truncations
      part at p_s once M is past a small burn-in, at every scanned M.
      KILL: signs stop alternating, or parting departs p_s at large M.
  N5 (even-P ladders: gate certificates). For P = 2, 4, 6, A = 2, 3,
      odd r, comb depth K: the pair (comb, comb with deepest class
      tooth raised) agrees to the raised position while the images'
      exact signs around -q_r alpha are opposite and the greedy images
      part at p_{q_r}, at every K scanned. KILL: as N4.
  N6 (bounded half, exact enumeration): at P = 2..8, A = 2, 3, every
      even nonzero residue r, no legal cyclic pattern of period P or 2P
      solves (I - H^L) lambda = Psi with alpha-part <= -1 — except the
      even-P alternating combs, whose deficit signs are printed and
      one-sided. KILL of the enumeration reading: a solution with
      w <= -1 whose deficit alternates.

FINDINGS (run record at the end; every stage green, all prints exact)
----------------------------------------------------------------------
F1  CONTROLS PASS (N1): H exact and the sign rule verified on
    convergents at all 50 grid cells.
F2  THE ODD-P ZERO-SUM IS A CUT AT EVERY CELL (rule at scanned scope;
    N2 lands): all 75 cells (P = 3..11 odd, A = 2..6, every odd r)
    solve (I - H) lambda = Psi in integers with alpha-part <= -1. The
    cut is -q_{r+1} alpha = -F_{r+2} alpha, INDEPENDENT of A, at every
    cell read (s = 2, 5, 13 at r = 1, 3, 5). The sign leg is also a
    paper theorem: every conjugate theta' is negative and |theta'_k|
    increasing, so Psi' < 0 and 1 - eta' < 0 give lambda' >=
    2|theta'_{P-1+r}|/(eta'-1) > 2, while |lambda| < 1, forcing the
    alpha-part (lambda - lambda')/(alpha - alpha') below 0.
F3  THE EVEN-P TELESCOPE IS EXACT (N3 lands): 140 truncations across
    P = 2..10 even, A = 2..6, odd r: the alternating comb's shifted
    weights sum to q_{top+r+1} - q_r and p likewise — the image limit
    is exactly the cut -q_r alpha (theorem; the telescope needs only
    cap 1 at even positions, which is the even-P one-class structure).
F4  ODD-P GATE CERTIFICATES (N4 lands, 12 cells x 11 truncations):
    deficit signs alternate with M at every cell (eta < 0), and the
    consecutive-truncation images part at exactly p_s = r at every
    scanned depth from the first — the designed odd-P parting IS the
    stride, which is the recorded aperiodic W1-W3 signature
    (explore_closure_family.py F2: part = r at 1, 4, 7).
F5  EVEN-P GATE CERTIFICATES (N5 lands, 12 cells x 8 depths): the
    raised-class-tooth pair's images sit on exactly opposite sides of
    -q_r alpha at every depth, parting at p_{q_r} = 1, 2, 4 at
    r = 1, 3, 5 — the r - 1 shape that is e-2's recorded parting
    vector 1, 3, 6 at strides 1, 4, 7.
F6  THE BOUNDED HALF STAYS ENUMERATED (N6 lands): at P = 2..8,
    A = 2, 3, periods P and 2P, every even nonzero r: the only legal
    patterns landing a lattice cut are the even-P alternating combs at
    the cut -q_{r-1} alpha (as the prints say: -1a, -3a, -8a at
    r = 2, 4, 6; the first write bound them to the odd-r formula
    -q_r alpha, since repaired), and their deficit is the single term
    theta_{top+r+1} of fixed index parity — one-sided at every
    truncation printed, and provably: the tail's maximal far-side push
    telescopes to exactly the deficit, attained only in the limit, so
    the reachable set touches the cut without crossing. No two-sided
    hit anywhere (a hit with alternating deficit was the kill; none
    fired).

RUN RECORD: python explore_parity_derivation.py — all six stages,
1.3 s wall, memory trivial, ALL STAGES GREEN.

THE DESIGN
----------
Pure integer arithmetic end to end: convergents p, q as bigints, H
solved from its action on the unimodular pair (theta_0, theta_1),
lattice membership by Cramer, greedy strings and partings on exact
values, and every sign of x alpha - y decided by the quadratic
q_{P-1} X^2 + (q_P - p_{P-1}) X - p_P through its value at y/x (alpha
is its positive root; the rig verifies the sign rule on convergents
first). No floats anywhere. Windows built by explore_shift_repair's
designed(); greedy() imported from the same engine. Stages: s0
controls, s1 = N2, s2 = N3, s3 = N4, s4 = N5, s5 = N6; no argument
runs all. Wall-clock seconds, memory trivial.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
from fractions import Fraction
from itertools import product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_shift_repair import designed, greedy      # noqa: E402


# ------------------------------------------------------------ exact field

class Cell:
    """A designed window (P, A) with exact convergents and sign tests."""

    def __init__(self, P, A, top=400):
        self.P, self.A = P, A
        a = designed(P, A, top)
        self.a = a
        q = [1, a[0]]
        p = [0, 1]
        for k in range(2, top):
            q.append(a[k - 1] * q[-1] + q[-2])
            p.append(a[k - 1] * p[-1] + p[-2])
        self.q, self.p = q, p
        # alpha: positive root of  q_{P-1} X^2 + (q_P - p_{P-1}) X - p_P
        self.A2, self.A1, self.A0 = q[P - 1], q[P] - p[P - 1], -p[P]
        # H from action on the unimodular pair theta_0 = (0,1)... coords
        # (u, w) mean u + w alpha; theta_k = (-p_k, q_k).
        m = ((-p[0], -p[1]), (q[0], q[1]))
        detm = m[0][0] * m[1][1] - m[0][1] * m[1][0]
        assert abs(detm) == 1
        n = ((-p[P], -p[P + 1]), (q[P], q[P + 1]))
        inv = ((m[1][1] * detm, -m[0][1] * detm),
               (-m[1][0] * detm, m[0][0] * detm))
        self.H = (n[0][0] * inv[0][0] + n[0][1] * inv[1][0],
                  n[0][0] * inv[0][1] + n[0][1] * inv[1][1],
                  n[1][0] * inv[0][0] + n[1][1] * inv[1][0],
                  n[1][0] * inv[0][1] + n[1][1] * inv[1][1])

    def h_selftest(self, upto=None):
        h00, h01, h10, h11 = self.H
        upto = upto or 3 * self.P
        for k in range(0, upto + 1):
            u, w = -self.p[k], self.q[k]
            if (h00 * u + h01 * w, h10 * u + h11 * w) != \
               (-self.p[k + self.P], self.q[k + self.P]):
                return False
        return True

    def sign_lin(self, x, y):
        """Exact sign of x*alpha - y, integers x, y."""
        if x == 0:
            return (0 > y) - (0 < y) if y else 0
        t = Fraction(y, x)
        val = self.A2 * t * t + self.A1 * t + self.A0
        # alpha is the larger root and A2 > 0, so f(t) < 0 iff t between
        # the roots; the smaller root is negative, so for t >= 0:
        # f(t) < 0 iff t < alpha.
        if val == 0:
            return 0
        if t < 0:
            # both roots: alpha > 0 > t always
            return 1 if x > 0 else -1
        # t >= 0 sits above the negative root, so f(t) < 0 iff t < alpha
        s = 1 if val < 0 else -1
        return s if x > 0 else -s

    def solve_1mHL(self, L, u, w):
        """Integer lambda with (I - H^L) lambda = (u, w), or None."""
        h = (1, 0, 0, 1)
        for _ in range(L):
            h = (h[0] * self.H[0] + h[1] * self.H[2],
                 h[0] * self.H[1] + h[1] * self.H[3],
                 h[2] * self.H[0] + h[3] * self.H[2],
                 h[2] * self.H[1] + h[3] * self.H[3])
        g = (1 - h[0], -h[1], -h[2], 1 - h[3])
        det = g[0] * g[3] - g[1] * g[2]
        if det == 0:
            return None
        nu = u * g[3] - w * g[1]
        nw = g[0] * w - g[2] * u
        if nu % det or nw % det:
            return None
        return (nu // det, nw // det)


def part_pos(cell, s):
    """p_s = min{p : q_{p+1} >= max(s, 2)}."""
    s = max(s, 2)
    p = 0
    while cell.q[p + 1] < s:
        p += 1
    return p


def image_value(d, q, r):
    return sum(d[k] * q[k + r] for k in range(len(d)) if d[k])


def first_diff(e1, e2):
    n = min(len(e1), len(e2))
    for i in range(n):
        if e1[i] != e2[i]:
            return i
    return n


def odd_comb(P, A, periods):
    """D3's pattern over `periods` periods: 1 at even in-period
    positions 2..P-3, 2 at the class P-1."""
    c = [0] * P
    for i in range(2, P - 2, 2):
        c[i] = 1
    c[P - 1] = 2
    return c * periods


def alt_comb(P, K):
    """D4's pattern: 1 at every odd position below K."""
    return [1 if k % 2 == 1 else 0 for k in range(K)]


# ---------------------------------------------------------------- stages

def s0_controls():
    print("=" * 74)
    print("S0 CONTROLS: H self-test and the exact sign rule on convergents")
    bad = 0
    for P in range(2, 12):
        for A in (2, 3, 4, 5, 6):
            cell = Cell(P, A)
            ok = cell.h_selftest()
            sg = all(cell.sign_lin(cell.q[k], cell.p[k]) == (-1) ** k
                     for k in range(1, 31))
            if not (ok and sg):
                bad += 1
                print(f"  FAIL P={P} A={A} H={ok} sign={sg}")
    print(f"  {'PASS' if bad == 0 else 'FAIL'}: 50 cells, H exact and "
          f"sign(q_k alpha - p_k) = (-1)^k at k = 1..30")
    return bad == 0


def s1_oddP_zero_sum():
    print("=" * 74)
    print("S1 ODD P: (I-H) lambda = Psi solvable with alpha-part <= -1,"
          " every odd r")
    bad = ok = 0
    for P in (3, 5, 7, 9, 11):
        for A in (2, 3, 4, 5, 6):
            cell = Cell(P, A)
            c = odd_comb(P, A, 1)
            for r in range(1, P, 2):
                u = -sum(c[i] * cell.p[i + r] for i in range(P))
                w = sum(c[i] * cell.q[i + r] for i in range(P))
                lam = cell.solve_1mHL(1, u, w)
                if lam is None or lam[1] > -1:
                    bad += 1
                    print(f"  FAIL P={P} A={A} r={r} lambda={lam}")
                else:
                    ok += 1
    print(f"  {'PASS' if bad == 0 else 'FAIL'}: {ok} cells solved, "
          f"every lambda a cut (alpha-part <= -1)")
    return bad == 0


def s2_evenP_telescope():
    print("=" * 74)
    print("S2 EVEN P: the alternating comb's image telescopes to"
          " -theta_r exactly")
    bad = ok = 0
    for P in (2, 4, 6, 8, 10):
        for A in (2, 3, 4, 5, 6):
            cell = Cell(P, A)
            for r in range(1, min(P, 8), 2):
                for K in (4 * P, 8 * P + 1):
                    d = alt_comb(P, K)
                    top = max(k for k in range(K) if d[k])
                    sq = sum(d[k] * cell.q[k + r] for k in range(K))
                    sp = sum(d[k] * cell.p[k + r] for k in range(K))
                    if sq != cell.q[top + r + 1] - cell.q[r] or \
                       sp != cell.p[top + r + 1] - cell.p[r]:
                        bad += 1
                        print(f"  FAIL P={P} A={A} r={r} K={K}")
                    else:
                        ok += 1
    print(f"  {'PASS' if bad == 0 else 'FAIL'}: {ok} truncations, image "
          f"star = theta_(top+r+1) - theta_r exactly (limit -q_r alpha)")
    return bad == 0


def s3_oddP_ladders():
    print("=" * 74)
    print("S3 ODD P GATE CERTIFICATES: alternating exact signs around"
          " the cut, parting at p_s")
    bad = 0
    for P in (3, 5, 7):
        for A in (2, 3):
            cell = Cell(P, A)
            for r in range(1, P, 2):
                c1 = odd_comb(P, A, 1)
                u = -sum(c1[i] * cell.p[i + r] for i in range(P))
                w = sum(c1[i] * cell.q[i + r] for i in range(P))
                lam = cell.solve_1mHL(1, u, w)
                s, mint = -lam[1], lam[0]
                ps = part_pos(cell, s)
                signs, parts = [], []
                prev_img = None
                for M in range(2, 13):
                    d = odd_comb(P, A, M)
                    uval = image_value(d, cell.q, r)
                    # exact deficit sign: cut - truncated star =
                    # H^M lambda, its sign read by sign_lin
                    dv = lam
                    for _ in range(M):
                        dv = (cell.H[0] * dv[0] + cell.H[1] * dv[1],
                              cell.H[2] * dv[0] + cell.H[3] * dv[1])
                    signs.append(cell.sign_lin(dv[1], -dv[0]))
                    if prev_img is not None:
                        e1 = greedy(prev_img, cell.q)
                        e2 = greedy(uval, cell.q)
                        parts.append(first_diff(e1, e2))
                    prev_img = uval
                alt = all(signs[i] == -signs[i + 1] != 0
                          for i in range(len(signs) - 1))
                settled = parts[3:]
                pgood = all(x == ps for x in settled)
                if not (alt and pgood):
                    bad += 1
                    print(f"  FAIL P={P} A={A} r={r} s={s} p_s={ps} "
                          f"signs={signs} parts={parts}")
                else:
                    print(f"  P={P} A={A} r={r}: cut -{s}a, p_s={ps}, "
                          f"deficit signs alternate, partings settle at "
                          f"{ps} (raw {parts})")
    print(f"  {'PASS' if bad == 0 else 'FAIL'}")
    return bad == 0


def s4_evenP_ladders():
    print("=" * 74)
    print("S4 EVEN P GATE CERTIFICATES: the raised-class-tooth pair"
          " straddles -q_r alpha, parting at p_(q_r)")
    bad = 0
    for P in (2, 4, 6):
        for A in (2, 3):
            cell = Cell(P, A)
            for r in range(1, min(P, 6), 2):
                s = cell.q[r]
                ps = part_pos(cell, s)
                rows = []
                good = True
                for KP in range(3, 11):
                    K = KP * P
                    d1 = alt_comb(P, K)
                    # raise the deepest class tooth 1 -> 2
                    top_class = max(k for k in range(K)
                                    if d1[k] and (k + 1) % P == 0)
                    d2 = list(d1)
                    d2[top_class] = 2
                    u1 = image_value(d1, cell.q, r)
                    u2 = image_value(d2, cell.q, r)
                    e1, e2 = greedy(u1, cell.q), greedy(u2, cell.q)
                    pt = first_diff(e1, e2)
                    # point - cut, exactly: star1 = theta_(top1+r+1)
                    # - theta_r and cut = -theta_r, so point1 - cut =
                    # theta_(top1+r+1); run 2 adds theta_(top_class+r)
                    top1 = max(k for k in range(K) if d1[k])
                    sgn1 = cell.sign_lin(cell.q[top1 + r + 1],
                                         cell.p[top1 + r + 1])
                    sgn2 = cell.sign_lin(
                        cell.q[top1 + r + 1] + cell.q[top_class + r],
                        cell.p[top1 + r + 1] + cell.p[top_class + r])
                    agree = top_class
                    rows.append((K, agree, pt, sgn1, sgn2))
                    if sgn1 * sgn2 != -1:
                        good = False
                settled = [t[2] for t in rows[2:]]
                if not good or any(x != ps for x in settled):
                    bad += 1
                    print(f"  FAIL P={P} A={A} r={r} s={s} p_s={ps} "
                          f"rows={rows}")
                else:
                    print(f"  P={P} A={A} r={r}: cut -{s}a, p_s={ps}, "
                          f"pair signs opposite at every depth, "
                          f"partings settle at {ps} "
                          f"(raw {[t[2] for t in rows]})")
    print(f"  {'PASS' if bad == 0 else 'FAIL'}")
    return bad == 0


def s5_bounded_enumeration():
    print("=" * 74)
    print("S5 EVEN r: no legal cyclic pattern (period P or 2P) lands a"
          " two-sided cut")
    c53 = Cell(5, 3)
    h = c53.H
    d53 = (1 - h[0]) * (1 - h[3]) - h[1] * h[2]
    print(f"  obstruction control: |L/(1-eta)L| at (P, A) = (5, 3) is "
          f"{abs(d53)} -- odd, so no Z/2 character of the quotient exists")
    viol = 0
    for P in range(2, 9):
        for A in (2, 3):
            cell = Cell(P, A)
            for L in (1, 2):
                W = L * P
                caps = [A if (i + 1) % P == 0 else 1 for i in range(W)]

                def legal(c):
                    return all(
                        c[i] <= caps[i % W] and
                        not (c[i] == caps[i % W] and c[(i - 1) % W])
                        for i in range(W))
                for r in range(2, P, 2):
                    hits = []
                    for c in product(*[range(cp + 1) for cp in caps]):
                        if not any(c) or not legal(c):
                            continue
                        u = -sum(c[i] * cell.p[i + r] for i in range(W))
                        w = sum(c[i] * cell.q[i + r] for i in range(W))
                        lam = cell.solve_1mHL(L, u, w)
                        if lam is not None and lam[1] <= -1:
                            hits.append((c, lam))
                    for c, lam in hits:
                        # deficit sign sequence: H^(L(M+1)) lambda over M
                        sgs = []
                        cur = lam
                        for M in range(1, 7):
                            nxt = cur
                            for _ in range(L):
                                nxt = (cell.H[0] * nxt[0]
                                       + cell.H[1] * nxt[1],
                                       cell.H[2] * nxt[0]
                                       + cell.H[3] * nxt[1])
                            cur = nxt
                            sgs.append(cell.sign_lin(cur[1], -cur[0]))
                        onesided = len(set(sgs)) == 1
                        tag = "one-sided" if onesided else \
                              "ALTERNATES <-- kill"
                        if not onesided:
                            viol += 1
                        print(f"  P={P} A={A} L={L} r={r} c={c} "
                              f"cut -{-lam[1]}a: deficit {tag}")
    print(f"  {'PASS: every even-r lattice hit approaches one-sided'
          if viol == 0 else 'FAIL'}")
    return viol == 0


def main():
    stages = {"s0": s0_controls, "s1": s1_oddP_zero_sum,
              "s2": s2_evenP_telescope, "s3": s3_oddP_ladders,
              "s4": s4_evenP_ladders, "s5": s5_bounded_enumeration}
    args = sys.argv[1:] or list(stages)
    ok = True
    for a in args:
        ok = stages[a]() and ok
    print("=" * 74)
    print("ALL STAGES GREEN" if ok else "RED — read the failures above")


if __name__ == "__main__":
    main()
