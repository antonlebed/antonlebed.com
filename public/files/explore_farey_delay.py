"""The Farey table: can a piecewise-affine map within a stated accuracy
of the reciprocal curve read one digit below the curve's own margin,
and at what accuracy does that first become impossible?

THE QUESTION. The segment lemma (explore_segmented_delay.py) prices an
affine piece's clause at a lookahead L by its slope's arithmetic: with
excess g = |s| w / b^L - (w - 1) > 0 the piece is empty iff its lattice
step delta = gcd(p, q b^L) / (q b^L) is at least g and its offset sits
in a closed window of length delta - g. A table-and-interpolate unit
reads below the margin only through a SIMPLE steepest chord, which the
uniform 4-chord reciprocal has at the four symmetric top cells and no
finer table has anywhere. The question minted from it: for the curve
1/(s + x), s = 1 + M-, at the 20 census cells of radices 2..5, and an
accuracy eps = b^-4 over the window, is there a piecewise-affine map
within eps of the curve whose every piece clears the lemma at the
CURVE's L* - 1 and whose kinks are empty — its slopes drawn from the
Farey sequence of the lemma's denominator bound, its breakpoints free —
and at what accuracy does the search first fail? Conventions as in
explore_piecewise_delay.py: radix b, digits {-am..ap}, slack
rho = am + ap + 1 - b >= 1, M+- = a+-/(b-1), w = M- + M+, W = am + ap;
the prefix u at depth n is the box [x_u, x_u + w/b^n],
x_u = (u - M-)/b^n; at lookahead L the depth-n zones are
[(q + 1 - M-), (q + M+)] b^(L-n) and a box kills iff its image strictly
contains one. The curve has sup|f'| = 1 (at x = -M-) so its L* is the
least L with b^L rho >= W, which is 1 at every census cell (W >= b
always, rho >= W never): the target lookahead is L = 0, where the
curve's own excess at its steep end is exactly 1.

THE DERIVATION, before the engine.
  THE ALIVE-ABLE SET. At L = 0 a slope s = -p/q in lowest terms has
  delta = 1/q and g = (pW - q rho) / (q (b - 1)); write e = pW - q rho,
  an integer. The lemma's condition delta >= g is e <= b - 1, the
  offset window has length (b - 1 - e) / (q (b - 1)), and the clause is
  empty outright at e <= 0, i.e. |s| <= rho/W = 1 - 1/w. So the slopes
  a piece may carry at L = 0 are: every rational of magnitude at most
  rho/W (free), and above it exactly the p/q with 1 <= pW - q rho <=
  b - 1, i.e. (q - p) rho >= (p - 1)(b - 1); slope 1 is the boundary
  e = b - 1 at every cell (window of length 0), and no slope above 1
  is alive-able. THE GAP: for numerator p the largest alive-able slope
  is p / (p + ceil((p - 1)(b - 1)/rho)), so nothing is alive-able
  strictly between sigma_gap = max_p of that and 1, and the p = 2
  value 2 / (2 + ceil((b - 1)/rho)) is predicted to be the max
  (corrected post-run: the max over p >= 2; at p = 1 the slope 1/2 is
  alive-able at every cell, W - 2 rho <= b - 1 holding whenever
  rho >= 1, so the gap is (max(1/2, sigma_gap), 1)). A map
  tracking the curve where the curve's slope lies in the gap must
  ZIGZAG between slope 1 and slopes at or below sigma_gap, each piece
  no longer than 2 eps over the slope mismatch.
  THE ROBUST KILL (property). If g is within eps of f on the window
  (sup norm) then over any box [a, a'] the image of g contains
  [f(a') + eps, f(a) - eps] for the decreasing f, since g(a) >=
  f(a) - eps and g(a') <= f(a') + eps and g is continuous. So every
  curve kill — a box whose image strictly contains a zone — with BOTH
  overhangs (zone_lo - f(a'), f(a) - zone_hi) exceeding eps kills
  every eps-approximant too, whatever its pieces. Define eps_rob(cell,
  L) as the largest min-overhang over the curve's killing boxes at L,
  all depths; it is attained at a bounded depth since a depth-n box's
  two overhangs sum to at most the image width less the zone length,
  b^-n (w - (w - 1) b^L), which is b^-n at L = 0 and falls under any
  positive value. No design within eps < eps_rob exists at
  L: THE TRADE HAS A FLOOR, set by the curve and the cell, not by any
  table budget. This inverts the question's premise (marked here as a
  TRANSPLANT from the interpolant runs, where the chord arithmetic was
  the binding constraint because every design sat at the curve's own
  points): the band binds before the lemma does, and the lemma decides
  only above the floor.
  THE SEARCH, above the floor. Breakpoints on the grid of both
  depth-m lattices, (Z - M-) b^-m and (Z + M+) b^-m, so that every box
  end at depth <= m is a breakpoint candidate; slopes in [-1, 0] from
  the alive-able set with q <= 8; the design monotone (all slopes
  <= 0) so the image of any interval is [g(right), g(left)]. A
  depth-first search from the left end takes at each breakpoint the
  slope of farthest reach — the longest piece within the band (a line
  minus the convex curve is concave, so the lower bound is checked at
  the ends and the upper bound at the vertex of a rational quadratic),
  with its piece clause empty (checked exactly over depths to the
  offset cycle), and every box of depth <= m ending inside it alive
  against the values already fixed — and backtracks on failure under a
  node budget. The start value runs over a menu on the lattices
  (M+ + Z) b^-m', the exact-offset condition of a first piece of slope
  1. A complete design is certified by explore_piecewise_delay.py's
  Table at L = 0 (the deep kink clauses the search does not check) and
  read by the engine's scan as a second oracle.

THE SLATE, frozen before the engine.

P-A THE CONTROL. (i) At every cell, for every slope -p/q with q <= 6,
    the Table's piece clause of the affine map -p/q x + d at L = 0 is
    empty for some d on a fine menu iff pW - q rho <= b - 1, and for
    every d iff pW - q rho <= 0. (ii) The uniform 4-chord reciprocal's
    accuracy (its max deviation from the curve) is at least eps_rob at
    each of the four symmetric top cells, and the Table reads it at 0
    there (explore_segmented_delay.py F4).
P-B THE FLOOR. eps_rob(L = 0) > b^-4 at 19 of 20 cells, every cell
    but (2,1,1), where it is below the 4-chord design's accuracy 1/30
    (hand-checked: at (5,4,4) the depth-2 box [-0.92, -0.84] has
    image [0.8621, 0.9259] round the zone [0.88, 0.92], overhangs
    0.018 and 0.006 against 5^-4 = 0.0016; at (2,1,1) the depth-3 box
    [-7/8, -5/8] kills with overhangs 0.023 and 0.014).
P-C THE FLOOR IS SHALLOW. eps_rob(L = 0) is attained at depth <= 4 at
    every cell and is at least b^-3 at 15 or more of the 20 (a guess,
    to be read).
P-D THE LOWER DIGIT. eps_rob(L = -1) >= b^-2 at every cell.
P-E THE SEARCH. At eps = b^-2 a Table-certified design is found at
    16 or more of the 20 cells, the four top cells among them; at
    eps = b^-4 at (2,1,1) only (P-B forbids the rest); at eps = b^-3
    the count of cells above the floor and the count found there are
    the TIGHTNESS reading. Every certified design survives the
    engine's scan at L = 0.
P-F THE GAP. sigma_gap = 2 / (2 + ceil((b - 1)/rho)) at 20 of 20
    cells.

KILLS, frozen as what this rig PRINTS.

K1 P-A prints a disagreement between the alive-able set and the Table
   at any (cell, slope), or a 4-chord accuracy below eps_rob at a top
   cell, or a Table floor other than 0 there -> the control failed;
   nothing below is read.
K2 A Table-certified design at an eps below eps_rob at its cell -> the
   robust kill is wrong.
K3 The engine's scan kills a Table-certified design at L = 0 -> the
   piecewise theorem or this rig's certification is wrong.
K4 (the question's kill, as a print) eps_rob(L = 0) > b^-4 at every cell
   but (2,1,1) -> no design within b^-4 reads at the curve's L* - 1
   there, and the hypothesis — one digit below the field's delay for the
   segment count's price — is dead at four digits of accuracy.
K5 (the two-digit hypothesis's kill) eps_rob(L = -1) >= b^-2 at every cell
   -> the trade has a floor at L* - 2 a digit coarser still.

POSITIVE CONTROL: P-A whole, read before any other line.

FINDINGS (entered post-run; every number below sits in this file's
printed output at radices 2..5).

F1 THE CONTROL HOLDS. The alive-able set agrees with the Table at 240
   of 240 (cell, slope) pairs, both halves; the uniform 4-chord
   reciprocal has accuracy 0.0337 at each top cell (sampled at the
   steepest chord's irrational vertex, so a hair under the sup), above
   eps_rob there (0.0139, 0.0111, 0.0125, 0.0067), and the
   Table reads it at 0 at all four. P-A held; K1 never fired.

F2 THE FLOOR. eps_rob(L = 0) is attained at depth 0..3 at every cell
   (depth 0 at (5,2,3), the root box; 1 at nine cells; 2 at nine; 3
   at (2,1,1)) and runs from 1/150 at (5,4,4) to 1/12 at (4,2,2),
   between b^-6.17 ((2,1,1)) and b^-1.79 in digits. It exceeds b^-4
   at 17 of 20 cells and sits just under it at three, (2,1,1) at 1/72
   and (3,1,2), (3,2,2) at 1/90 against 1/81; it is at least b^-3 at
   12. P-B's count was wrong by two (the guess that every radix-3
   floor clears 1/81 missed by a ninth) and P-C's guess short by
   three; the shape held. K4 fires at 17 cells and not at 20: a
   four-digit table reads below the margin at three cells only.

F3 THE LOWER DIGIT. eps_rob(L = -1) is attained at depth 0 or 1 at
   every cell of radices 3..5 (depth 2 at (2,1,1)) and is at least
   b^-2 at 19 of 20, 1/12 at (2,1,1) against 1/4; the least at
   radix >= 3 is 1/9. P-D missed (2,1,1); K5 fires at 19 cells: at
   two digits of accuracy no design reads at L* - 2 outside radix 2.

F4 THE GAP. sigma_gap = 2 / (2 + ceil((b - 1)/rho)) at 20 of 20:
   (2/3, 1) at the four cells with rho = b - 1, (1/2, 1) at nine,
   (2/5, 1) at three and (1/3, 1) at four. P-F held.

F5 THE FLOOR IS TIGHT WHERE THE SEARCH REACHES. 95 Table-certified
   designs, 95 alive by the engine's scan at L = 0 (K2, K3 never
   fired). On the ladder: at eps = b^-2 a design at 12 of the 15
   cells above the floor, at b^-3 at 4 of 8, at b^-4 at 3 of 3
   ((2,1,1) in 2 pieces, (3,1,2) in 7, (3,2,2) in 4). The bisection
   between the floor and the finest rung found puts the finest
   certified design within 1.5 x eps_rob at 11 of 20 cells — at
   1.00 x at (3,1,2) and (3,2,2), 1.01 at (4,3,3) and (5,1,4), 1.03
   to 1.05 at (2,1,1), (4,1,3), (4,2,2), (5,2,4) — with no failure
   at all recorded between the floor and the finest design at six of
   those; the three cells with a+ < a- and a lead of 1, (4,3,1),
   (5,4,1) and (3,2,1), are the search's worst at 12.8 x, 10.0 x and
   1.9 x, its budget exhausted with no leaf ever rejected, so the gap
   there is the search's and not proved. The designs are the derived
   zigzag: slope 1 alternating with 1/2, 1/3 or 1/4 through the gap,
   the free slopes below rho/W taking the shallow end (e.g. (3,1,2)
   at 1.00 x: 1, 1/3, 1, 1/3, 1, 1/2, 1/4, 1/6, eight pieces). P-E's
   16 missed: the b^-2 rung sits below the floor at five cells, which
   the prediction did not price, and the search failed at three more;
   its other clauses held.

VERDICT. A piecewise-affine map within eps of the reciprocal reads
below the curve's margin only above a FLOOR set by the curve and the
cell alone, eps_rob, the largest min-overhang of the curve's own
killing boxes at L* - 1, attained at depth <= 3 and worth b^-1.8 to
b^-4.1 at radices 3..5 (b^-6.2 at (2,1,1)); below it no table of
any size reads there, and above it the alive-able slopes — free at
or below rho/W, and above it exactly the p/q with 1 <= pW - q rho
<= b - 1, nothing between 2/(2 + ceil((b - 1)/rho)) and 1 — build
a certified design within 5 percent of the floor at 8 cells and
within 50 percent at 11. The segment lemma's trade descends to the
floor and not through it: the delay is a property of the function
and the cell after all, and the table budget buys the stretch
between the margin and the floor.

RUN RECORD: pure Python, exact fractions for every verdict, standard
library; under memwatch, peak commit 117 MB against the 512 MB
default; wall 107 s at radices 2..5 (the control 3 s, the floors
under a second, the searches with their bisections the rest), 0
failures. The rehearsal at radices 2..3 found the breakpoint grid
starting a step inside the window, the start value off it; the slate
stands as written. Prints reproduced by:
python prime/code/explore_farey_delay.py [BMAX]
python prime/code/explore_farey_delay.py [BMAX] --floor   (P-B..P-D only)
"""

import math
import sys
import time
from fractions import Fraction as Fr

import explore_onestream_delay as one
import explore_piecewise_delay as pw

FAILURES = []
QMAX = 8            # the slopes' denominator bound in the search
NODE_BUDGET = 400   # depth-first nodes per (cell, eps)


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


def frac(x):
    return x - math.floor(x)


# ------------------------------------------------------------ the cell

class Cell:
    def __init__(self, b, am, ap):
        self.b, self.am, self.ap = b, am, ap
        self.Mm, self.Mp = Fr(am, b - 1), Fr(ap, b - 1)
        self.w = self.Mm + self.Mp
        self.W, self.rho = am + ap, am + ap + 1 - b
        self.s0 = 1 + self.Mm

    def f(self, x):
        return 1 / (self.s0 + x)

    def tag(self):
        return f"({self.b},{self.am},{self.ap})"

    def boxes(self, n):
        b = self.b
        umin = -self.am * (b ** n - 1) // (b - 1)
        umax = self.ap * (b ** n - 1) // (b - 1)
        bn = Fr(b) ** n
        for u in range(umin, umax + 1):
            a = (u - self.Mm) / bn
            yield u, a, a + self.w / bn


# --------------------------------------------------- the alive-able set

def excess_int(c, p, q):
    return p * c.W - q * c.rho


def aliveable(c, Q):
    """The slopes -p/q, 0 < p/q <= 1, q <= Q, whose piece clause at L = 0
    can be empty: e = pW - q rho <= b - 1; sorted steep to shallow."""
    out = set()
    for q in range(1, Q + 1):
        for p in range(1, q + 1):
            if math.gcd(p, q) == 1 and excess_int(c, p, q) <= c.b - 1:
                out.add(Fr(p, q))
    return sorted(out, reverse=True)


def sigma_gap(c, pmax=40):
    return max(Fr(p, p + math.ceil(Fr((p - 1) * (c.b - 1), c.rho))) for p in range(2, pmax + 1))


# ------------------------------------------ the piece clause at L = 0

def piece_alive(c, s, d, xlo, xhi, nmax=40):
    """The affine piece s x + d on [xlo, xhi] at L = 0: empty clause?
    Actual boxes below the full-period depth, a full period above, the
    offset's cycle detected once full (explore_piecewise_delay.py Table)."""
    b, w = c.b, c.w
    g = abs(s) * w - (w - 1)
    if g <= 0:
        return True
    q = s.denominator
    end = -c.Mm if s > 0 else c.Mp
    seen = {}
    for n in range(nmax + 1):
        bn = Fr(b) ** n
        umin = -c.am * (b ** n - 1) // (b - 1)
        umax = c.ap * (b ** n - 1) // (b - 1)
        lo = max(math.ceil(xlo * bn + c.Mm), umin)
        hi = min(math.floor(xhi * bn - c.Mp), umax)
        full = hi - lo + 1 >= q
        us = range(q) if full else range(lo, hi + 1)
        for u in us:
            z = frac(s * (u + end) + d * bn + c.Mm)
            if (z != 0) if g == 1 else (g > 1 or z > 1 - g):
                return False
        if full:
            st = frac(d * bn)
            if st in seen:
                return True
            seen[st] = n
    return True


# ------------------------------------------------------ the robust kill

def box_kill(c, lo, hi, n, L):
    """The best zone strictly inside [lo, hi] at depth n, lookahead L:
    (min overhang, q) or None."""
    scale = Fr(c.b) ** (n - L)
    A, B = lo * scale + c.Mm, hi * scale - c.Mp
    best = None
    for q in range(math.floor(A), math.ceil(B) + 1):
        zlo, zhi = (q + 1 - c.Mm) / scale, (q + c.Mp) / scale
        if lo < zlo and zhi < hi:
            m = min(zlo - lo, hi - zhi)
            if best is None or m > best[0]:
                best = (m, q)
    return best


def robust_floor(c, L, nmax=12):
    """eps_rob at lookahead L: the largest min-overhang over the curve's
    killing boxes; (eps_rob, depth, u, q). Stops once no deeper box can
    beat it."""
    best = (Fr(0), None, None, None)
    for n in range(nmax + 1):
        cap = Fr(c.b) ** (L - n) * (c.w * Fr(c.b) ** (-L) - (c.w - 1)) / 2
        if cap <= best[0]:
            break
        for u, a, a2 in c.boxes(n):
            r = box_kill(c, c.f(a2), c.f(a), n, L)
            if r and r[0] > best[0]:
                best = (r[0], n, u, r[1])
    return best


# ---------------------------------------------------------- the search

def band_ok(c, s, d, x1, x2, eps):
    """s x + d within eps of f on [x1, x2] (s <= 0)."""
    for x in (x1, x2):
        if s * x + d < c.f(x) - eps:
            return False
    # (s x + d - eps)(s0 + x) - 1 <= 0 on the interval; concave for s < 0
    A, B, C = s, s * c.s0 + d - eps, (d - eps) * c.s0 - 1
    pts = [x1, x2]
    if s < 0:
        xv = -B / (2 * A)
        if x1 < xv < x2:
            pts.append(xv)
    return all(A * x * x + B * x + C <= 0 for x in pts)


def grid(c, m):
    """Both ends of every depth-m box: the two lattices, the window's
    ends included."""
    pts = set()
    for _, a, a2 in c.boxes(m):
        pts.add(a)
        pts.add(a2)
    return sorted(pts)


def start_menu(c, eps, m, o_c):
    """Start values near f(-M-) = 1 on the lattices (M+ + Z) b^-m',
    inside the band and the root cell, nearest first."""
    vals = set()
    top = c.Mp * Fr(c.b) ** o_c
    for mp in range(0, m + 2):
        bm = Fr(c.b) ** mp
        for off in (c.Mp, Fr(0)):        # a slope-1 first piece needs the first lattice; a free one neither
            k = math.floor((1 - eps) * bm - off)
            while (k + off) / bm <= 1 + eps:
                v = (k + off) / bm
                if 1 - eps <= v <= min(1 + eps, top):
                    vals.add(v)
                k += 1
    return sorted(vals, key=lambda v: (abs(v - 1), v))[:8]


class Search:
    def __init__(self, c, eps, m, slopes, budget):
        self.c, self.eps, self.m, self.slopes, self.budget = c, eps, m, slopes, budget
        self.xs = grid(c, m)
        self.N = len(self.xs)
        self.idx = {x: i for i, x in enumerate(self.xs)}
        # boxes of depth <= m ending at each grid point: (n, left index)
        self.ending = [[] for _ in self.xs]
        for n in range(m + 1):
            for u, a, a2 in c.boxes(n):
                if a in self.idx and a2 in self.idx:
                    self.ending[self.idx[a2]].append((n, self.idx[a]))
        self.val = [None] * self.N
        self.nodes = 0
        self.leaf_rejects = 0

    def reach(self, i, s, d):
        """Farthest j with the piece on [x_i, x_j] in the band and its
        clause empty (both monotone in j)."""
        xs, c = self.xs, self.c
        lo, hi = i, self.N - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if band_ok(c, s, d, xs[i], xs[mid], self.eps):
                lo = mid
            else:
                hi = mid - 1
        j = lo
        if j == i:
            return i
        lo, hi = i, j
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if piece_alive(c, s, d, xs[i], xs[mid]):
                lo = mid
            else:
                hi = mid - 1
        return lo

    def shallow_ok(self, k):
        """Every box of depth <= m ending at grid point k alive against
        the fixed values (the design monotone: image = [val k, val left])."""
        c = self.c
        for n, il in self.ending[k]:
            lo, hi = self.val[k], self.val[il]
            if math.ceil(hi * c.b ** n - c.Mp) > lo * c.b ** n + c.Mm:
                return False
        return True

    def rec(self, i, pieces, certify):
        if i == self.N - 1:
            design = self.design(pieces)
            if certify(design):
                return design
            self.leaf_rejects += 1
            return None
        if self.nodes >= self.budget:
            return None
        xs, v = self.xs, self.val[i]
        cands = []
        for s in self.slopes:
            d = v - s * xs[i]
            j = self.reach(i, s, d)
            # shrink to the longest prefix whose shallow boxes are alive
            k = i + 1
            while k <= j:
                self.val[k] = s * xs[k] + d
                if not self.shallow_ok(k):
                    break
                k += 1
            j = k - 1
            if j > i:
                cands.append((j, s, d))
                if j - i >= 2:                       # the half-reach branch
                    cands.append(((i + j) // 2, s, d))
        cands.sort(key=lambda t: (-t[0], -abs(t[1])))
        for j, s, d in cands:
            self.nodes += 1
            if self.nodes > self.budget:
                return None
            for k in range(i + 1, j + 1):
                self.val[k] = s * xs[k] + d
            r = self.rec(j, pieces + [(i, j, s, d)], certify)
            if r is not None:
                return r
        return None

    def design(self, pieces):
        slopes = [p[2] for p in pieces]
        offsets = [p[3] for p in pieces]
        kinks = [self.xs[p[1]] for p in pieces[:-1]]
        return pw.Piecewise(slopes, offsets, kinks, f"farey {len(pieces)} pieces")

    def run(self, v0, certify):
        self.val = [None] * self.N
        self.val[0] = v0
        return self.rec(0, [], certify)


def accuracy(c, design, samples=64):
    """sup |design - f| over the window, exactly: on each piece the
    difference is concave, extreme at the ends or the piece's vertex."""
    cuts = [-c.Mm] + design.k + [c.Mp]
    best = Fr(0)
    for j, (x1, x2) in enumerate(zip(cuts, cuts[1:])):
        s, d = design.s[j], design.d[j]
        pts = [x1, x2]
        if s < 0:
            # d/dx (s x + d - 1/(s0+x)) = s + 1/(s0+x)^2 = 0 -> (s0+x)^2 = -1/s
            r = -1 / s
            sq = Fr(math.isqrt(r.numerator), math.isqrt(r.denominator))
            if sq * sq == r:
                xv = sq - c.s0
                if x1 < xv < x2:
                    pts.append(xv)
            else:
                # irrational vertex: bracket it by a fine sample
                for t in range(1, samples):
                    pts.append(x1 + (x2 - x1) * t / samples)
        for x in pts:
            best = max(best, abs(s * x + d - c.f(x)))
    return best


def search_cell(c, eps, o_c, budget=NODE_BUDGET):
    """The least-piece design found at eps, Table-certified, or None;
    returns (design, nodes, leaf rejects, m)."""
    m = min(max(1, math.ceil(-math.log(float(eps)) / math.log(c.b)) + 1), 4 if c.b > 2 else 6)
    slopes = [-s for s in aliveable(c, QMAX)]
    S = Search(c, eps, m, slopes, budget)

    def certify(design):
        tab = pw.Table(c.b, c.am, c.ap, design)
        return not tab.dead(0)

    for v0 in start_menu(c, eps, m, o_c):
        d = S.run(v0, certify)
        if d is not None:
            return d, S.nodes, S.leaf_rejects, m
        if S.nodes >= budget:
            break
    return None, S.nodes, S.leaf_rejects, m


# ------------------------------------------------------------------ runs

def cells(bmax):
    return pw.cells(bmax)


def curve_lead(c):
    o = 0
    while c.Mp * Fr(c.b) ** o < 1:
        o += 1
    return o


def control(bmax):
    print(f"\n=== P-A the control, radices 2..{bmax}")
    agree = total = 0
    for (b, am, ap) in cells(bmax):
        c = Cell(b, am, ap)
        for q in range(1, 7):
            for p in range(1, q + 1):
                if math.gcd(p, q) != 1:
                    continue
                s = Fr(-p, q)
                e = excess_int(c, p, q)
                some = every = None
                menu = [Fr(k, q * (b - 1) * b ** 2) for k in range(q * (b - 1) * b ** 2)]
                verdicts = []
                for d in menu:
                    f = pw.Piecewise([s], [d], [], f"{s}x+{d}")
                    tab = pw.Table(b, am, ap, f)
                    pieces, _, _ = tab.verdict(0)
                    verdicts.append(not pieces[0])
                some, every = any(verdicts), all(verdicts)
                total += 1
                good = (some == (e <= b - 1)) and (every == (e <= 0))
                agree += good
                ok(good, f"K1 {c.tag()} slope {s}: e={e}, some-d empty {some}, every-d empty {every}")
    print(f"  (i) the alive-able set against the Table: {agree} of {total} (cell, slope) pairs agree")
    import explore_segmented_delay as seg
    n4 = 0
    for (b, am, ap) in [(2, 1, 1), (3, 2, 2), (4, 3, 3), (5, 4, 4)]:
        if b > bmax:
            continue
        c = Cell(b, am, ap)
        f = seg.interpolant(seg.recip_points(b, am, ap, seg.uniform_xs(b, am, ap, 4)), "recip uniform N=4")
        acc = accuracy(c, f)
        er = robust_floor(c, 0)[0]
        tab = pw.Table(b, am, ap, f)
        fl = tab.floor(1)
        ok(acc >= er, f"K1 {c.tag()} 4-chord accuracy {acc} below eps_rob {er}")
        ok(fl == 0, f"K1 {c.tag()} 4-chord Table floor {fl}, F4 says 0")
        n4 += acc >= er and fl == 0
        print(f"  (ii) {c.tag()} uniform 4-chord: accuracy {acc} = {float(acc):.4f}, eps_rob {float(er):.4f}, Table floor {fl}")
    print(f"  (ii) {n4} of the top cells consistent")


def floors(bmax):
    print(f"\n=== P-B..P-D the robust floor, radices 2..{bmax}")
    above4 = shallow = ge3 = ge2m1 = gapok = 0
    rows = {}
    for (b, am, ap) in cells(bmax):
        c = Cell(b, am, ap)
        e0, n0, u0, q0 = robust_floor(c, 0)
        e1, n1, u1, q1 = robust_floor(c, -1)
        sg = sigma_gap(c)
        pred = Fr(2, 2 + math.ceil(Fr(b - 1, c.rho)))
        above4 += e0 > Fr(1, b ** 4)
        shallow += n0 is not None and n0 <= 4
        ge3 += e0 >= Fr(1, b ** 3)
        ge2m1 += e1 >= Fr(1, b ** 2)
        gapok += sg == pred
        ok(sg == pred, f"P-F {c.tag()}: sigma_gap {sg}, predicted {pred}")
        rows[(b, am, ap)] = (e0, e1)
        digits0 = -math.log(float(e0)) / math.log(b) if e0 else float("inf")
        print(f"  {c.tag()} w={c.w} rho/W={Fr(c.rho, c.W)} gap ({sg}, 1): eps_rob(L=0) = {e0} = {float(e0):.5f} = b^-{digits0:.2f} "
              f"at depth {n0} u={u0} q={q0} [b^-4 = {float(Fr(1, b**4)):.5f}]; eps_rob(L=-1) = {float(e1):.4f} at depth {n1}")
    print(f"  eps_rob(0) > b^-4 at {above4} of {len(rows)}; attained at depth <= 4 at {shallow}; >= b^-3 at {ge3}; "
          f"eps_rob(-1) >= b^-2 at {ge2m1}; sigma_gap as predicted at {gapok}")
    return rows


def read_design(c, design, eps, e0, label, stats):
    """Accuracy, K2, the engine's scan (K3); returns the print fragment."""
    b, am, ap = c.b, c.am, c.ap
    acc = accuracy(c, design)
    ok(acc <= eps, f"P-E {c.tag()} {label}: design accuracy {acc} above eps {eps}")
    ok(eps >= e0, f"K2 {c.tag()} {label}: certified design at eps {eps} below eps_rob {e0}")
    o = one.least_lead(b, am, ap, design)
    v = pw.engine_at(b, am, ap, design, o, 0, pw.SCAN_KILL, pw.SCAN_SURV, 0)
    ok(v[0] == "alive", f"K3 {c.tag()} {label}: the engine kills the certified design at L=0: {v}")
    stats["certified"] += 1
    stats["engine_ok"] += v[0] == "alive"
    return acc, o, v[0]


def searches(bmax, rows, bisect_steps=5):
    print(f"\n=== P-E the search, radices 2..{bmax}, slopes q <= {QMAX}, {NODE_BUDGET} nodes per run")
    found = {2: 0, 3: 0, 4: 0}
    above = {2: 0, 3: 0, 4: 0}
    stats = {"certified": 0, "engine_ok": 0}
    ratios = []
    for (b, am, ap) in cells(bmax):
        c = Cell(b, am, ap)
        o_c = curve_lead(c)
        e0 = rows[(b, am, ap)][0]
        line = []
        finest = None          # (eps, design)
        coarsest_fail = None
        for r in (2, 3, 4):
            eps = Fr(1, b ** r)
            if eps < e0:
                line.append(f"b^-{r}: below the floor")
                continue
            above[r] += 1
            t0 = time.time()
            design, nodes, rejects, m = search_cell(c, eps, o_c)
            if design is None:
                line.append(f"b^-{r}: not found ({nodes} nodes, {rejects} leaf rejects, grid depth {m}, {time.time() - t0:.0f}s)")
                if coarsest_fail is None or eps > coarsest_fail:
                    coarsest_fail = eps
                continue
            found[r] += 1
            acc, o, verdict = read_design(c, design, eps, e0, f"eps=b^-{r}", stats)
            finest = (eps, design)
            steep = max(abs(s) for s in design.s)
            line.append(f"b^-{r}: FOUND {len(design.s)} pieces (steepest {steep}, o={o}, acc {float(acc):.4f}, "
                        f"{nodes} nodes, {rejects} rejects, {time.time() - t0:.0f}s, engine {verdict})")
        print(f"  {c.tag()}: " + "; ".join(line))
        # the bisection: between the floor (proved dead) and the finest design found
        hi = finest[0] if finest else Fr(1, b)
        lo = max(e0, coarsest_fail) if coarsest_fail else e0
        if finest is None:
            design, nodes, rejects, m = search_cell(c, hi, o_c)
            if design is None:
                print(f"    bisection: nothing found even at b^-1; skipped")
                continue
            read_design(c, design, hi, e0, "eps=b^-1", stats)
            finest = (hi, design)
        t0 = time.time()
        for _ in range(bisect_steps):
            mid = Fr(math.sqrt(float(lo) * float(hi))).limit_denominator(10 ** 6)
            if not (lo < mid < hi):
                break
            design, nodes, rejects, m = search_cell(c, mid, o_c)
            if design is None:
                lo = mid
            else:
                read_design(c, design, mid, e0, f"eps={mid}", stats)
                hi, finest = mid, (mid, design)
        ratio = float(finest[0] / e0)
        ratios.append(ratio)
        d = finest[1]
        print(f"    bisection ({time.time() - t0:.0f}s): finest design at eps = {float(finest[0]):.5f} = {ratio:.2f} x eps_rob, "
              f"{len(d.s)} pieces, slopes {[str(s) for s in d.s]}; first fail above the floor at "
              f"{float(lo):.5f} = {float(lo / e0):.2f} x eps_rob" if lo > e0 else
              f"    bisection ({time.time() - t0:.0f}s): finest design at eps = {float(finest[0]):.5f} = {ratio:.2f} x eps_rob, "
              f"{len(d.s)} pieces, slopes {[str(s) for s in d.s]}; no failure recorded above the floor")
    print(f"  found at eps = b^-2 at {found[2]} of {above[2]} cells above the floor, b^-3 at {found[3]} of {above[3]}, "
          f"b^-4 at {found[4]} of {above[4]}; {stats['engine_ok']} of {stats['certified']} certified designs alive by the engine's scan")
    if ratios:
        print(f"  the finest design over the floor: ratio {min(ratios):.2f} .. {max(ratios):.2f}, "
              f"{sum(r <= 1.5 for r in ratios)} of {len(ratios)} cells within 1.5 x eps_rob")


def main():
    bmax = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    t0 = time.time()
    if "--floor" in sys.argv:
        floors(bmax)
        print(f"\nwall {time.time() - t0:.1f}s; failures: {len(FAILURES)}")
        return
    control(bmax)
    if FAILURES:
        print("\nPOSITIVE CONTROL FAILED; nothing below is read")
        for f in FAILURES:
            print("  ", f)
        return
    print(f"  control: {time.time() - t0:.1f}s")
    rows = floors(bmax)
    print(f"  elapsed: {time.time() - t0:.1f}s")
    searches(bmax, rows)
    print(f"\nwall {time.time() - t0:.1f}s; failures: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)


if __name__ == "__main__":
    main()
