"""The many-stream theorem: does every C^2 map of ANY number of
signed-digit streams that is not affine on the window read at exactly
the Lebesgue margin in its box width rate, the one-stream proof run
along one lattice line of the prefix lattice?

THE QUESTION. explore_onestream_widened.py proves that a C^2 map of one
stream reads at exactly the margin law's L*, the least L with
b^L rho >= Lam (am + ap), unless it is affine on the window: the proof
consumes the map only through a C^2 phase along a line of prefixes
whose second difference has one sign, and the prefix lattice of d
streams has such a line wherever the Hessian is nonzero. The
polynomial entry certified its maps cell by cell (x y, x y + z,
x^2 + y at explore_polynomial_delay.py, the product's split line at
explore_product_necessity.py) and left two fronts open: terms sharing
a variable (x^2 + x y, where the image is no longer the terms' Minkowski
sum and the corner sup need not be attained) and division x/y, two
streams with a pole. One theorem should close both. Conventions as in
the one-stream rigs: radix b, digits {-am..ap}, slack
rho = am + ap + 1 - b >= 1, M+- = a+-/(b-1), W = M- + M+, the zone
width W - 1 = rho/(b-1); a prefix u_i of length n is the box
[x_u, x_u + W/b^n] with x_u = (u_i - M-)/b^n, a d-tuple of prefixes a
box in R^d; output cells at depth t and lead o in Z are
[(q - M-) e, (q + M+) e], e = b^(o - t); input depth n = t + c, and
L = c + o carries the law.

THE PROOF, written before the engine.

  Let f be C^2 on the window [-M-, M+]^d and Lam = sup over the window
  of |grad f|_1 = sum_i |d_i f|, THE BOX WIDTH RATE: for p, q in a box
  of side eps, |f(q) - f(p)| <= sup |grad f|_1 |q - p|_inf <= Lam eps
  (the mean value theorem along the segment, Hoelder), so the image of
  a depth-n box is an interval (a box is connected) of width at most
  Lam W / b^n and the margin law b^L rho >= Lam (am + ap) suffices, as
  it does for one stream: the image never strictly contains a zone, a
  legal digit always exists (the cell lemma), the reader survives.
  Below L* the law's excess g = Lam W / b^L - (W - 1) is positive; let
  Lam_law = (W - 1) b^L / W, Lam_h = (Lam + Lam_law)/2 < Lam, and C the
  component of {|grad f|_1 > Lam_h} (open in the window) holding the
  point where the sup is attained.
  THE DICHOTOMY. If the Hessian vanishes on C then grad f is constant on
  C (C is open and connected), so |grad f|_1 is constant there, equal
  to Lam; a boundary point of C interior to the window would read
  |grad f|_1 = Lam_h < Lam by continuity, a contradiction, so C is the
  whole window and f is AFFINE on it (a constant gradient on a convex
  set). Otherwise the Hessian is nonzero at a point p of C, hence on a
  ball round p. THE BALL, by iteration over the d partials: on the
  current ball, either d_i f vanishes identically (it is then constant
  and drops out of every width) or it is nonzero at some point, and a
  smaller ball round that point has it of one sign; d steps leave a
  ball B in C with every partial of one sign or identically zero and
  the Hessian nonzero at its centre. (The route as first written, "the
  zero sets of the partials are finitely many closed sets with empty
  interior", holds for analytic maps and fails for C^2 ones, whose
  partials can vanish on a patch; the iteration needs nothing of the
  kind.) A nonzero symmetric H at the centre has an integer direction
  e with e^T H e != 0 (e_j if H_jj != 0, else e_j + e_k gives 2 H_jk),
  so a smaller ball has |e^T H e| >= kappa > 0 of one sign; shrinking
  once more, sum_i inf_B |d_i f| > Lam_h (each |d_i f| is continuous
  and their sum at the centre exceeds Lam_h). Call this B.
  ON B: every partial is one-signed or zero, so f is monotone in each
  coordinate on any box inside B, the image's ends sit at the two
  OPPOSITE CORNERS the signs name, and the width, summed along a
  staircase path corner to corner, is at least
  sum_i inf_B |d_i f| (W / b^n) > Lam_h W / b^n: every box in B has
  excess at least g/2 in zone units. Along THE LATTICE LINE u + i e,
  i in Z, the lower end's phase z(i) = b^(n-L) f(x_u + delta + i e/b^n)
  + M-, delta the min corner's offset, is a C^2 function of the real
  variable i with z'' = e^T H e / b^(n+L), one sign, |z''| >=
  kappa / b^(n+L), and z' ranging over Delta = (the range of
  (grad f . e) over B) / b^L. The dead arc: a box's image strictly
  contains a depth-t zone iff its excess g' is positive and {z} lies in
  (1 - g', 1) (the one-stream derivation verbatim, the ends being the
  corners). The count N(n) of line points whose box lies inside a cube
  of half-side r about the centre, the line through the prefix nearest
  the centre (within half a unit of it), is at least
  (2 r b^n - W - 1)/|e|_inf - 1, so b^n <= (N + 1 + (W + 1)/|e|_inf)/X
  with X = 2 r/|e|_inf; van der
  Corput's explicit inequality (Kuipers and Niederreiter 1974, ch. 2,
  Theorem 2.7) bounds every harmonic of the N phases by
  (h Delta + 2)(4 b^((n+L)/2)/sqrt(h kappa) + 3), Erdos-Turan
  (Theorem 2.5) turns them into a discrepancy bound B_H(N) with b^n
  replaced by its bound in N, and at N >= N_0 := the least N with
  min_H B_H(N) < min(g/2, 1/2) some phase sits in the arc and the
  reader is dead at output depth n - c.
  THE MANY-STREAM THEOREM. For a C^2 map of d streams the reader at lead
  o survives at every L with b^L rho >= Lam (am + ap), Lam the sup of
  the gradient's L1 norm over the window, and, unless f is affine on
  the window, is dead at every L below from the depth at which the line
  holds N_0 boxes, N_0 a function of (b, L, W, g, X, kappa, Delta) and
  never of the depth: the delay is exactly L*, whatever d. TRANSPLANTS
  marked: "the ends sit at corners" holds on B only (x^2 + x y has an
  interior minimum over a box straddling x = -y/2), so the engine's
  ends are the exact min and max over the integer box, per map; "the
  corner sup is attained" and "the image is the terms' Minkowski sum"
  are the disjoint-term rigs' and not the theorem's. The scan is the
  instrument and the theorem the guarantee: the kill is expected orders
  before N_0, as at one stream.

THE MAPS AND THEIR LAWS (Lam re-derived per map; each |grad f|_1 is
convex in every coordinate separately, so its sup over any box sits at
a corner, and the sum of the partials' sups over a box equals the sup
of their sum -- the corner of largest magnitude carries both). x y:
Lam = 2 Mh (Mh = max(M-, M+)), the product law. x^2 + y and x y + z:
Lam = 2 Mh + 1, the multiply-add's law. x^2 + x y = x (x + y):
|2x + y| + |x| = 4 Mh at the sign-matched corner of largest magnitude,
the law b^L rho (b - 1) >= 4 ah (am + ap); the image over a box is
exact with the edge minima x = -y/2 beside the corners (max at a
corner: convex in x, linear in y). DIVISION x/(s + y), s = M- + P the
reciprocal rig's convention (explore_onestream_delay.py Recip), so the
denominator D = s + y runs over [P, P + W] and never crosses the pole:
d_x = 1/D, d_y = -x/D^2, Lam = (P + Mh)/P^2 at D = P and |x| = Mh (the
aim's line wrote s where P belongs; the engine's convention is the
reciprocal's), the law b^L rho P^2 >= (P + Mh)(am + ap); the range
[-M-/P, M+/P] fits at lead o iff 1/P <= b^o, negative at the deep pole
sweep values (the output leads); the ends sit at corners (d_x > 0, the
sign of d_y that of -x). The pole sweep P = j/(b - 1), j in
{1, 2, 4, 8}. The lead o is the least in Z with the range inside the
root cell, the law reads in L = c + o, c in Z.

THE ENGINE. A map is a class of: image(us, n) the exact integer ends
of the image over the integer box; approx; the window range for the
lead; law_ok exactly in Fractions; lam; grad_iv and hess_e_iv, interval
bounds of the partials and of e^T H e over a float box (conservative
interval arithmetic); grad and hess_e at a point for the cube's spot
check; the peak corner. The reader for d streams at lookahead c in Z
and lead o: death is a property of the image alone (the cell lemma), so
the certificate is a SCAN over the excess region {sum_i sup_box |d_i f|
> Lam_law}, enumerated recursively with interval pruning (every
straddling box is in it: the width is at most the sup times the side),
the least output depth at which some box strictly contains a zone; the
exhaustive adversary TREE with its moves CONFINED to the region, as
explore_output_comparator.py's was to a constant digit -- a box outside
the region cannot straddle and a descendant's box lies inside its
ancestor's, so the confined adversary loses no kill and a confined
certificate is one for the full game; the bare tree at L* for the
survival. THE CUBE: from the peak corner nudged inward by r, halving r
until the interval bounds over the cube give every partial one-signed,
sum_i inf |d_i f| > Lam_h and inf |e^T H e| = kappa > 0 with e the
map's direction ((1,1) for x y and x y + z, (1,0) for x^2 + y and
x^2 + x y where kappa = 2 either way and the diagonal is longer, (0,1)
for division where d_yy = 2x/D^3); 200 random points of the cube
re-read against the pointwise formulas. THE LINE at depth n: the
prefix whose box centre is nearest the cube's centre, stepped by e
while the box stays inside the cube, counted exactly; the phases along
it read as floats.

THE SLATE, frozen before the engine.

P-A THE ORACLE. x y at lead 0, x^2 + y and x y + z at lead 1, at every
    representable cell of radices 2..5 (the cells and leads
    explore_polynomial_delay.py ran, whose x y census is
    explore_product_delay.py's cell for cell): the scan's kill at
    L* - 1 sits at the output depth equal to that rig's TermGame
    certificate round, run here with its own budget, and the confined
    tree's round equals it wherever the tree reaches; at L* the scan
    and the bare tree find nothing.
P-B x^2 + x y at every cell of radices 2..5 at its least lead:
    Lam = 4 Mh, dead at L* - 1 and alive at L* at every cell.
P-C DIVISION x/(s + y) at every cell of radices 2..5 and P = j/(b - 1),
    j in {1, 2, 4, 8}, at its least lead (the output leading where
    1/P < 1): dead at L* - 1 and alive at L* at every pair.
P-D THE PROOF'S CONSTANT. N_0 printed per pair along the chosen line;
    at every certified kill with n_kill - 1 >= max(1, c) the line at
    depth n_kill - 1 holds fewer than N_0 boxes; at one depth per pair
    holding at least 10^4 line boxes the observed |S_h|, h = 1..3,
    sits below van der Corput's bound and D_N below B_H(N).

KILLS, frozen as what this rig PRINTS.

K1 P-A prints an oracle disagreement -> the engine is not the term
   engine; nothing below is read.
K2 A kill at the law's L* at any pair -> the sufficiency arithmetic
   (the box width rate) is wrong.
K3 A pair at L* - 1 with no kill in the region at a depth where the
   region holds at least 10^5 boxes, the confined tree surviving ->
   the many-stream necessity fails there.
K4 The scan and the confined tree disagree at a depth both reach.
K5 A certified kill at n_kill with the line at n_kill - 1 already
   holding N_0 boxes -> the proof's constant is wrong.
K6 An observed |S_h| above van der Corput's bound, or a D_N above
   B_H(N) -> the cited constants are misquoted and N_0 is unreadable.
K7 A cube whose sampled points contradict its interval bounds (a
   partial's sign, the sum of the infima, kappa), or no cube found at
   a pair -> the map's interval arithmetic is wrong; that pair's P-D
   is unread.

POSITIVE CONTROL: P-A whole, read before any other line.

FINDINGS (entered post-run; every number below sits in this file's
printed output at radices 2..5).

F1 THE ORACLE HOLDS. x y at 13 of 13 cells at lead 0, x^2 + y at 20 of
   20 and x y + z at 20 of 20 at lead 1: the scan's kill at L* - 1 sits
   at the polynomial rig's certificate round at every cell, and the
   confined tree agrees at every cell it reaches; at L* the scan is
   clean and the bare tree survives wherever its first round fits the
   budget. P-A held; K1 never fired. Controls 14.7 s.

F2 TERMS SHARING A VARIABLE READ AT THE MARGIN [theorem, the print its
   check]. x^2 + x y at 20 cells: leads o in {1, 2}, L* in {2, 3}, c* in
   {0, 1, 2}; certified at L* - 1 at 20 of 20 (output depth 1 at 13, 2
   at 6, 3 at 1; two by the window itself at input depth 0), the excess
   region at most 64 boxes, the confined tree at the scan's round at 20
   of 20; surviving at L* at 20 of 20 by the scan and the bare tree.
   P-B held; K2, K3, K4 never fired.

F3 DIVISION READS AT THE MARGIN, ITS LOOKAHEAD THE NUMERATOR'S
   [theorem for the delay; the lookahead's invariance an observation at
   the sweep]. x/(s + y) at 80 pairs: leads from 1 down to -3, the
   output leading at 6 pairs ((2,1,1) at P = 2, 4, 8 and the three
   radix-3 cells at P = 4), L* from 3 down to -1; certified at L* - 1
   at 80 of 80 (output depth 1 at 49, 2 at 24, 3 at 6, 4 at 1), the
   region at most 173 boxes, the confined tree at the scan's round at
   75 and short of it at 5; surviving at L* at 80 of 80 by the scan and
   at 58 by the tree, unreached at the 22 pairs whose first round
   exceeds the budget. The lookahead c* = L* - o is 1 or 2 at every
   pair and never negative while the lead falls to -3: the
   reciprocal's reader emitted before it read at 40 of 120 pairs
   (explore_onestream_delay.py), the divider's never does, the numerator
   stream's partial 1/D costing a lookahead the pole's lead cannot buy.
   P-C held. (The never-negative reading is a property of the law's
   closed forms at every P, with c* = 0 attained at deep pairs:
   explore_divider_lookahead.py.)

F4 THE PROOF'S CONSTANT. A cube at 153 of 153 pairs, the sampled check
   clean (K7 never fired); N_0 from 4.39e4 to 2.52e9 ((4,3,3) at
   P = 8/3); the line at the depth before the certified kill holds 0
   boxes at 151 of the 153 pairs and 1 at two product cells, (4,2,2)
   and (5,2,4): the kill comes at or before the line's first box. 153
   pairs read at N from 10,922 to 48,827 phases: the observed |S_h|,
   h = 1, 2, 3, at most 0.12 of van der Corput's bound, the observed D_N
   at most 0.012, the bound below N for all three harmonics at 150 of
   153 (for one or two at the three deep-pole pairs (2,1,1) P = 8,
   (4,2,2) P = 4/3 and (4,3,3) P = 8/3, where kappa is smallest). K5 and
   K6 never fired; P-D held.

VERDICT. Every C^2 map of any number of streams that is not affine on
the window reads at exactly the margin law's L*, the box width rate its
only parameter: the polynomial entry's two open fronts close under one
theorem, and its certified maps, the square root, the reciprocal and
the divider are the theorem's specimens.

RUN RECORD: pure Python, integers for every verdict and floats for the
region, the cube and the phases, standard library, TermGame imported
from explore_polynomial_delay.py for the oracle; under memwatch, peak
commit 50.9 MB against the 512 MB default; wall 43 s at radices 2..5
(8 s at 2..3). Prints reproduced by:
python prime/code/explore_manystream_delay.py [BMAX]
"""

import cmath
import itertools
import math
import random
import sys
import time
from fractions import Fraction as Fr

import explore_polynomial_delay as poly

FAILURES = []
SCAN_KILL, SCAN_SURV, TREE_CERT, TREE_SURV = 400_000, 150_000, 150_000, 40_000
TREE_ORACLE = 2_000_000        # the polynomial rig's own node budget
PHASE_MIN = 10_000
HMAX = 1 << 18
REGION_K3 = 100_000


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


def sgn(x):
    return (x > 0) - (x < 0)


def _psums():
    out = ([0.0], [0.0], [0.0])
    for h in range(1, HMAX + 1):
        out[0].append(out[0][-1] + h ** -0.5)
        out[1].append(out[1][-1] + h ** -1.5)
        out[2].append(out[2][-1] + 1 / h)
    return out


PSUMS = _psums()


# ------------------------------------------------- interval arithmetic
# An interval is a (lo, hi) pair of floats; every operation is
# conservative (the true range lies inside the result).

def iadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def ineg(a):
    return -a[1], -a[0]


def isub(a, b):
    return iadd(a, ineg(b))


def iscale(k, a):
    return (k * a[0], k * a[1]) if k >= 0 else (k * a[1], k * a[0])


def imul(a, b):
    c = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return min(c), max(c)


def iabs(a):
    if a[0] >= 0:
        return a
    if a[1] <= 0:
        return -a[1], -a[0]
    return 0.0, max(-a[0], a[1])


def irecip(a):                 # a[0] > 0
    return 1 / a[1], 1 / a[0]


def isum(ivs):
    lo = sum(v[0] for v in ivs)
    hi = sum(v[1] for v in ivs)
    return lo, hi


# ------------------------------------------------------------ the maps
# A map exposes: d; image(us, n) -> (lo, hi, S), the image's exact ends
# lo/S, hi/S over the integer box of the prefixes; approx(xs) a float
# at a real point; window_range(Mm, Mp) -> (lo, hi) Fractions; law_ok;
# lam(); grad_iv(box), hess_e_iv(box, e) interval bounds; grad(xs),
# hess_e(xs, e) pointwise; peak(Mm, Mp) -> the corner where |grad|_1
# peaks, as floats; e the line direction.

class Product:
    name, d, e = "x y", 2, (1, 1)

    def __init__(self, b, am, ap):
        self.b, self.am, self.ap = b, am, ap
        self.Mm, self.Mp = Fr(am, b - 1), Fr(ap, b - 1)
        self.Mh = max(self.Mm, self.Mp)

    def image(self, us, n):
        b, am, ap = self.b, self.am, self.ap
        N = (b - 1) * b ** n
        X1, X2 = (b - 1) * us[0] - am, (b - 1) * us[0] + ap
        Y1, Y2 = (b - 1) * us[1] - am, (b - 1) * us[1] + ap
        c = (X1 * Y1, X1 * Y2, X2 * Y1, X2 * Y2)
        return min(c), max(c), N * N

    def approx(self, xs):
        return xs[0] * xs[1]

    def window_range(self, Mm, Mp):
        return -Mm * Mp, max(Mm, Mp) ** 2

    def law_ok(self, b, rho, wsum, L):
        return Fr(b) ** L * rho * (b - 1) >= 2 * max(self.am, self.ap) * wsum

    def lam(self):
        return 2 * float(self.Mh)

    def grad_iv(self, box):
        return [box[1], box[0]]

    def hess_e_iv(self, box, e):
        return (2.0 * e[0] * e[1],) * 2

    def grad(self, xs):
        return [xs[1], xs[0]]

    def hess_e(self, xs, e):
        return 2.0 * e[0] * e[1]

    def peak(self, Mm, Mp):
        s = 1.0 if Mp >= Mm else -1.0
        return [s * float(self.Mh)] * 2


class SquarePlus:
    name, d, e = "x^2 + y", 2, (1, 0)

    def __init__(self, b, am, ap):
        self.b, self.am, self.ap = b, am, ap
        self.Mm, self.Mp = Fr(am, b - 1), Fr(ap, b - 1)
        self.Mh = max(self.Mm, self.Mp)

    def image(self, us, n):
        b, am, ap = self.b, self.am, self.ap
        N = (b - 1) * b ** n
        X1, X2 = (b - 1) * us[0] - am, (b - 1) * us[0] + ap
        Y1, Y2 = (b - 1) * us[1] - am, (b - 1) * us[1] + ap
        sq_lo = 0 if X1 <= 0 <= X2 else min(X1 * X1, X2 * X2)
        sq_hi = max(X1 * X1, X2 * X2)
        return sq_lo + Y1 * N, sq_hi + Y2 * N, N * N

    def approx(self, xs):
        return xs[0] ** 2 + xs[1]

    def window_range(self, Mm, Mp):
        return -Mm, max(Mm, Mp) ** 2 + Mp

    def law_ok(self, b, rho, wsum, L):
        return Fr(b) ** L * rho * (b - 1) >= (2 * max(self.am, self.ap) + b - 1) * wsum

    def lam(self):
        return 2 * float(self.Mh) + 1

    def grad_iv(self, box):
        return [iscale(2, box[0]), (1.0, 1.0)]

    def hess_e_iv(self, box, e):
        return (2.0 * e[0] * e[0],) * 2

    def grad(self, xs):
        return [2 * xs[0], 1.0]

    def hess_e(self, xs, e):
        return 2.0 * e[0] * e[0]

    def peak(self, Mm, Mp):
        s = 1.0 if Mp >= Mm else -1.0
        return [s * float(self.Mh), 0.0]


class MulAdd:
    name, d, e = "x y + z", 3, (1, 1, 0)

    def __init__(self, b, am, ap):
        self.b, self.am, self.ap = b, am, ap
        self.Mm, self.Mp = Fr(am, b - 1), Fr(ap, b - 1)
        self.Mh = max(self.Mm, self.Mp)

    def image(self, us, n):
        b, am, ap = self.b, self.am, self.ap
        N = (b - 1) * b ** n
        X1, X2 = (b - 1) * us[0] - am, (b - 1) * us[0] + ap
        Y1, Y2 = (b - 1) * us[1] - am, (b - 1) * us[1] + ap
        Z1, Z2 = (b - 1) * us[2] - am, (b - 1) * us[2] + ap
        c = (X1 * Y1, X1 * Y2, X2 * Y1, X2 * Y2)
        return min(c) + Z1 * N, max(c) + Z2 * N, N * N

    def approx(self, xs):
        return xs[0] * xs[1] + xs[2]

    def window_range(self, Mm, Mp):
        return -Mm * Mp - Mm, max(Mm, Mp) ** 2 + Mp

    def law_ok(self, b, rho, wsum, L):
        return Fr(b) ** L * rho * (b - 1) >= (2 * max(self.am, self.ap) + b - 1) * wsum

    def lam(self):
        return 2 * float(self.Mh) + 1

    def grad_iv(self, box):
        return [box[1], box[0], (1.0, 1.0)]

    def hess_e_iv(self, box, e):
        return (2.0 * e[0] * e[1],) * 2

    def grad(self, xs):
        return [xs[1], xs[0], 1.0]

    def hess_e(self, xs, e):
        return 2.0 * e[0] * e[1]

    def peak(self, Mm, Mp):
        s = 1.0 if Mp >= Mm else -1.0
        return [s * float(self.Mh), s * float(self.Mh), 0.0]


class SquareCross:
    """x^2 + x y = x (x + y): terms sharing a variable. Over a box the
    max sits at a corner (convex in x, linear in y) and the min at a
    corner or at the edge point x = -y/2, y an endpoint, where the
    value is -y^2/4; at scale 2 the half-integers are integers."""
    name, d, e = "x^2 + x y", 2, (1, 0)

    def __init__(self, b, am, ap):
        self.b, self.am, self.ap = b, am, ap
        self.Mm, self.Mp = Fr(am, b - 1), Fr(ap, b - 1)
        self.Mh = max(self.Mm, self.Mp)

    @staticmethod
    def _ends(X1, X2, Y1, Y2):
        """Ends over [X1, X2] x [Y1, Y2] at scale 4 (2X, 2Y integers)."""
        vals = [(2 * X) ** 2 + (2 * X) * (2 * Y) for X in (X1, X2) for Y in (Y1, Y2)]
        hi = max(vals)
        lo = min(vals)
        for Y in (Y1, Y2):
            if 2 * X1 <= -Y <= 2 * X2:
                lo = min(lo, -Y * Y)
        return lo, hi

    def image(self, us, n):
        b, am, ap = self.b, self.am, self.ap
        N = (b - 1) * b ** n
        X1, X2 = (b - 1) * us[0] - am, (b - 1) * us[0] + ap
        Y1, Y2 = (b - 1) * us[1] - am, (b - 1) * us[1] + ap
        lo, hi = self._ends(X1, X2, Y1, Y2)
        return lo, hi, 4 * N * N

    def approx(self, xs):
        return xs[0] ** 2 + xs[0] * xs[1]

    def window_range(self, Mm, Mp):
        cand = [x * x + x * y for x in (-Mm, Mp) for y in (-Mm, Mp)]
        hi, lo = max(cand), min(cand)
        for y in (-Mm, Mp):
            if -Mm <= -y / 2 <= Mp:
                lo = min(lo, -y * y / 4)
        return lo, hi

    def law_ok(self, b, rho, wsum, L):
        return Fr(b) ** L * rho * (b - 1) >= 4 * max(self.am, self.ap) * wsum

    def lam(self):
        return 4 * float(self.Mh)

    def grad_iv(self, box):
        return [iadd(iscale(2, box[0]), box[1]), box[0]]

    def hess_e_iv(self, box, e):
        v = 2.0 * e[0] * e[0] + 2.0 * e[0] * e[1]
        return v, v

    def grad(self, xs):
        return [2 * xs[0] + xs[1], xs[0]]

    def hess_e(self, xs, e):
        return 2.0 * e[0] * e[0] + 2.0 * e[0] * e[1]

    def peak(self, Mm, Mp):
        s = 1.0 if Mp >= Mm else -1.0
        return [s * float(self.Mh)] * 2


class Division:
    """x / (s + y), s = S/Dn = M- + P: f(X/N, Y/N) = X Dn / (S N + Dn Y)."""
    d, e = 2, (0, 1)

    def __init__(self, b, am, ap, P):
        self.b, self.am, self.ap, self.P = b, am, ap, P
        self.Mm, self.Mp = Fr(am, b - 1), Fr(ap, b - 1)
        self.Mh = max(self.Mm, self.Mp)
        s = self.Mm + P
        self.S, self.Dn = s.numerator, s.denominator
        self.name = f"x/({self.S}/{self.Dn} + y)"

    def _den(self, Y, N):
        return self.S * N + self.Dn * Y                 # > 0 on the window

    def image(self, us, n):
        b, am, ap = self.b, self.am, self.ap
        N = (b - 1) * b ** n
        X1, X2 = (b - 1) * us[0] - am, (b - 1) * us[0] + ap
        Y1, Y2 = (b - 1) * us[1] - am, (b - 1) * us[1] + ap
        D1, D2 = self._den(Y1, N), self._den(Y2, N)
        # max of x/D: x = X2; D small if X2 > 0, large otherwise
        dh = D1 if X2 > 0 else D2
        dl = D1 if X1 < 0 else D2
        return X1 * self.Dn * dh, X2 * self.Dn * dl, dl * dh

    def approx(self, xs):
        return xs[0] / (float(self.S) / self.Dn + xs[1])

    def window_range(self, Mm, Mp):
        return -Mm / self.P, Mp / self.P

    def law_ok(self, b, rho, wsum, L):
        return Fr(b) ** L * rho * self.P * self.P >= (self.P + self.Mh) * wsum

    def lam(self):
        P = float(self.P)
        return (P + float(self.Mh)) / (P * P)

    def _D_iv(self, box):
        s = float(self.S) / self.Dn
        return s + box[1][0], s + box[1][1]

    def grad_iv(self, box):
        D = self._D_iv(box)
        r = irecip(D)
        return [r, ineg(imul(box[0], imul(r, r)))]

    def hess_e_iv(self, box, e):
        D = self._D_iv(box)
        r = irecip(D)
        r2 = imul(r, r)
        r3 = imul(r2, r)
        dxy = ineg(r2)                        # d_xy = -1/D^2
        dyy = iscale(2, imul(box[0], r3))     # d_yy = 2x/D^3
        return iadd(iscale(2 * e[0] * e[1], dxy), iscale(e[1] * e[1], dyy))

    def grad(self, xs):
        D = float(self.S) / self.Dn + xs[1]
        return [1 / D, -xs[0] / D ** 2]

    def hess_e(self, xs, e):
        D = float(self.S) / self.Dn + xs[1]
        return 2 * e[0] * e[1] * (-1 / D ** 2) + e[1] * e[1] * 2 * xs[0] / D ** 3

    def peak(self, Mm, Mp):
        s = 1.0 if Mp >= Mm else -1.0
        return [s * float(self.Mh), -float(self.Mm)]


# --------------------------------------------------------- the leads

def least_lead(b, am, ap, fmap):
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    lo, hi = fmap.window_range(Mm, Mp)

    def fits(o):
        return lo >= -Mm * Fr(b) ** o and hi <= Mp * Fr(b) ** o
    o = 0
    if fits(0):
        while o > -200 and fits(o - 1):
            o -= 1
    else:
        while not fits(o):
            o += 1
    return o


def law_L(b, am, ap, fmap):
    rho, wsum = am + ap + 1 - b, am + ap
    L = 0
    while not fmap.law_ok(b, rho, wsum, L):
        L += 1
    while fmap.law_ok(b, rho, wsum, L - 1):
        L -= 1
    return L


def excess(b, am, ap, fmap, L):
    W = (am + ap) / (b - 1)
    return fmap.lam() * W / float(b) ** L - (W - 1)


# ---------------------------------------------------------- the engine

class ReaderD:
    """The reading game for d streams at lookahead c in Z and lead o."""

    def __init__(self, b, am, ap, c, fmap, o, lam_law=None):
        self.b, self.am, self.ap, self.c, self.f, self.o = b, am, ap, c, fmap, o
        self.d = fmap.d
        self.digits = list(range(-am, ap + 1))
        self.moves = list(itertools.product(self.digits, repeat=self.d))
        self.W = (am + ap) / (b - 1)
        self.Mm, self.Mp = am / (b - 1), ap / (b - 1)
        self.lam_law = lam_law

    def cell(self, q, t):
        b, o = self.b, self.o
        n1, n2 = (b - 1) * q - self.am, (b - 1) * q + self.ap
        if o >= 0:
            return n1 * b ** o, n2 * b ** o, (b - 1) * b ** t
        return n1, n2, (b - 1) * b ** (t - o)

    def legal(self, us, n, q, t):
        C1, C2, T = self.cell(q, t)
        lo, hi, S = self.f.image(us, n)
        return C1 * S <= lo * T and hi * T <= C2 * S

    def straddles(self, us, n, t):
        """Does the image strictly contain a depth-t zone? The candidate
        zone is named by a float and decided exactly with its
        neighbours."""
        b, ap = self.b, self.ap
        lo, hi, S = self.f.image(us, n)
        yhi = hi / S * float(b) ** (t - self.o)
        m0 = math.ceil(yhi - ap / (b - 1)) - 1
        for m in (m0 - 1, m0, m0 + 1):
            _, top, T = self.cell(m, t)
            bot = self.cell(m + 1, t)[0]
            if hi * T > top * S and lo * T < bot * S:
                return True
        return False

    def prefixes(self, n):
        b = self.b
        return -self.am * (b ** n - 1) // (b - 1), self.ap * (b ** n - 1) // (b - 1)

    def box_float(self, us, n):
        s = float(self.b) ** n
        return [((u - self.Mm) / s, (u - self.Mm) / s + self.W / s) for u in us]

    def in_region(self, box):
        g = self.f.grad_iv(box)
        return sum(iabs(v)[1] for v in g) > self.lam_law

    def region_prefixes(self, n):
        """Generator over prefix tuples of length n whose box meets the
        excess region, pruned by interval bounds on partial tuples."""
        umin, umax = self.prefixes(n)
        window = (-self.Mm, self.Mp)
        s = float(self.b) ** n
        box = [window] * self.d

        def rec(i, us):
            if i == self.d:
                yield tuple(us)
                return
            for u in range(umin, umax + 1):
                box[i] = ((u - self.Mm) / s, (u - self.Mm) / s + self.W / s)
                if self.in_region(box):
                    us.append(u)
                    yield from rec(i + 1, us)
                    us.pop()
            box[i] = window
        yield from rec(0, [])

    def all_prefixes(self, n):
        umin, umax = self.prefixes(n)
        return itertools.product(range(umin, umax + 1), repeat=self.d)

    def scan(self, budget, region):
        """The least output depth t at which some prefix of length
        max(0, t + c) straddles a depth-t zone. Returns (t or None, n at
        the kill or the last n fully scanned, prefixes seen, the count at
        that n)."""
        t, seen, last_n, last_cnt = 0, 0, -1, 0
        while True:
            t += 1
            n = max(0, t + self.c)
            cnt = 0
            gen = self.region_prefixes(n) if region else self.all_prefixes(n)
            for us in gen:
                cnt += 1
                if seen + cnt > budget:
                    return None, last_n, seen, last_cnt
                if self.straddles(us, n, t):
                    return t, n, seen + cnt, cnt
            seen += cnt
            last_n, last_cnt = n, cnt

    # the exhaustive tree, the check on the no-strategy step
    def survives(self, us, n, q, t, rounds, confined):
        if rounds == 0:
            return True
        n1 = max(0, t + 1 + self.c)
        for mvs in itertools.product(self.moves, repeat=n1 - n):
            us1 = us
            for mv in mvs:
                us1 = tuple(self.b * u + x for u, x in zip(us1, mv))
            if confined and n1 > n and not self.in_region(self.box_float(us1, n1)):
                continue
            alive = False
            for p in self.digits:
                if self.legal(us1, n1, self.b * q + p, t + 1) and \
                        self.survives(us1, n1, self.b * q + p, t + 1, rounds - 1, confined):
                    alive = True
                    break
            if not alive:
                return False
        return True

    def certificate_depth(self, budget, confined=False, max_rounds=40):
        m = len(self.moves)
        if m ** max(0, 1 + self.c) > budget:
            return None, 0
        depth = max(1, min(max_rounds, int(math.log(budget) / math.log(m)) - self.c))
        root = (0,) * self.d
        for r in range(0, depth + 1):
            if not (self.legal(root, 0, 0, 0) and self.survives(root, 0, 0, 0, r, confined)):
                return r, depth
        return None, depth


# ------------------------------------------------ the cube and the line

class Cube:
    """The cube B about the peak corner nudged inward by r where every
    partial is one-signed, sum inf|d_i f| > Lam_h and |e^T H e| >= kappa."""

    def __init__(self, fmap, Mm, Mp, lam_h):
        self.f, self.e = fmap, fmap.e
        self.corner = fmap.peak(Mm, Mp)
        self.lam_h = lam_h
        self.ok = False
        Mh = max(Mm, Mp)
        r = Mh / 4
        for _ in range(40):
            c = [ci - math.copysign(r, ci) if ci != 0 else 0.0 for ci in self.corner]
            box = [(ci - r, ci + r) for ci in c]
            if all(-Mm - 1e-12 <= lo and hi <= Mp + 1e-12 for lo, hi in box):
                g = fmap.grad_iv(box)
                signs = [sgn(v[0]) if v[0] > 0 else (sgn(v[1]) if v[1] < 0 else 0) for v in g]
                if all(s != 0 or (v[0] == 0 == v[1]) for s, v in zip(signs, g)):
                    inf_sum = sum(iabs(v)[0] for v in g)
                    hv = fmap.hess_e_iv(box, self.e)
                    kappa = iabs(hv)[0] if hv[0] > 0 or hv[1] < 0 else 0.0
                    if inf_sum > lam_h and kappa > 0:
                        self.center, self.r, self.box, self.signs = c, r, box, signs
                        self.kappa, self.inf_sum = kappa, inf_sum
                        ge = isum([iscale(ei, gi) for ei, gi in zip(self.e, g)])
                        self.delta_range = ge[1] - ge[0]
                        self.ok = True
                        return
            r /= 2

    def spot_check(self, trials=200, seed=1):
        rng = random.Random(seed)
        for _ in range(trials):
            xs = [rng.uniform(lo, hi) for lo, hi in self.box]
            g = self.f.grad(xs)
            if any(s != 0 and sgn(gi) != s for s, gi in zip(self.signs, g)):
                return "a partial's sign"
            if sum(abs(gi) for gi in g) <= self.lam_h:
                return "the sum of the partials"
            if abs(self.f.hess_e(xs, self.e)) < self.kappa * (1 - 1e-9):
                return "kappa"
        return None


class LineRegion:
    """N_0 along the lattice line through the cube: the count bound
    b^n <= (N + 1 + (W + 1)/|e|_inf)/X, X = 2r/|e|_inf."""

    def __init__(self, b, am, ap, L, g, cube):
        self.b, self.am, self.ap, self.L, self.g = b, am, ap, L, g
        self.W = (am + ap) / (b - 1)
        self.cube = cube
        einf = max(abs(x) for x in cube.e)
        self.X = 2 * cube.r / einf
        self.slack = 1 + (self.W + 1) / einf
        self.kappa = cube.kappa
        self.delta = cube.delta_range / float(b) ** L
        self.a = min(g / 2, 0.5)
        self.N0, self.H = self.n0()

    def bound(self, N, H):
        b, L = self.b, self.L
        A = 4 * float(b) ** (L / 2) * math.sqrt((N + self.slack) / (self.X * self.kappa))
        s1, s2, s3 = PSUMS[0][H], PSUMS[1][H], PSUMS[2][H]
        s = (self.delta * A * s1 + 3 * self.delta * H + 2 * A * s2 + 6 * s3) / N
        return 6 / (H + 1) + 4 / math.pi * s

    def n0(self):
        best = None
        H = 1
        while H < HMAX:
            if 6 / (H + 1) < self.a:
                N = max(1, math.ceil(self.W))
                while self.bound(N, H) >= self.a and N < 1e40:
                    N *= 2
                if N >= 1e40:
                    break
                lo, hi = N // 2, N
                while hi - lo > 1:
                    mid = (lo + hi) // 2
                    if self.bound(mid, H) < self.a:
                        hi = mid
                    else:
                        lo = mid
                if best is not None and hi >= best[0] and H >= 8:
                    break
                if best is None or hi < best[0]:
                    best = (hi, H)
            H = H * 2 if H >= 8 else H + 1
        return best if best else (None, None)

    def vdc_bound(self, n, h):
        lam = h * self.kappa / float(self.b) ** (n + self.L)
        return (h * self.delta + 2) * (4 / math.sqrt(lam) + 3)

    def line(self, rd, n):
        """The prefix tuples u0 + i e at depth n whose box lies inside
        the cube, in order of i."""
        b, W, Mm = rd.b, rd.W, rd.Mm
        s = float(b) ** n
        c, r, e = self.cube.center, self.cube.r, self.cube.e
        u0 = [round(ci * s + Mm - W / 2) for ci in c]
        ilo, ihi = -10 ** 18, 10 ** 18
        for ci, ui, ei in zip(c, u0, e):
            if ei == 0:
                if not (ci - r <= (ui - Mm) / s and (ui - Mm) / s + W / s <= ci + r):
                    return []
                continue
            # (ui + i ei - Mm)/s >= ci - r  and  (ui + i ei - Mm)/s + W/s <= ci + r
            a1 = ((ci - r) * s + Mm - ui) / ei
            a2 = ((ci + r) * s + Mm - ui - W) / ei
            lo, hi = (a1, a2) if ei > 0 else (a2, a1)
            ilo, ihi = max(ilo, math.ceil(lo - 1e-9)), min(ihi, math.floor(hi + 1e-9))
        return [tuple(ui + i * ei for ui, ei in zip(u0, e)) for i in range(ilo, ihi + 1)]

    def count(self, rd, n):
        return len(self.line(rd, n))


def phases(rd, reg, us_list, n, L):
    scale = float(rd.b) ** (n - L)
    out = []
    for us in us_list:
        box = rd.box_float(us, n)
        xs = [lo if s >= 0 else hi for (lo, hi), s in zip(box, reg.cube.signs)]
        z = rd.f.approx(xs) * scale + rd.Mm
        out.append(z - math.floor(z))
    return out


def discrepancy(xs):
    xs = sorted(xs)
    N = len(xs)
    return max(max((i + 1) / N - x, x - i / N) for i, x in enumerate(xs))


def check_arithmetic(rd, reg, L, c, label):
    n = max(1, c + 1)
    line = reg.line(rd, n)
    while len(line) < PHASE_MIN and n < 60:
        n += 1
        line = reg.line(rd, n)
    N = len(line)
    if N < PHASE_MIN:
        return f"P-D skipped (line {N} at n={n})"
    zs = phases(rd, reg, line, n, L)
    D = discrepancy(zs)
    B = reg.bound(N, reg.H) if reg.H else float("inf")
    ok(D <= B, f"K6 {label}: D_N={D:.4f} above B_H(N)={B:.4f} at n={n}, N={N}")
    ratios = []
    for h in (1, 2, 3):
        S = abs(sum(cmath.exp(2j * math.pi * h * z) for z in zs))
        Vb = reg.vdc_bound(n, h)
        ok(S <= Vb, f"K6 {label}: |S_{h}|={S:.1f} above van der Corput's {Vb:.1f} at n={n}, N={N}")
        ratios.append(S / Vb)
    bites = sum(1 for h in (1, 2, 3) if reg.vdc_bound(n, h) < N)
    return (f"P-D n={n} N={N}: D_N={D:.3f} vs B={B:.2f}; |S_h|/vdC="
            f"{','.join(f'{r:.2f}' for r in ratios)} (bound below N at {bites} of 3)")


def tree_word(r, depth):
    if depth == 0:
        return "unreached [0]"
    return f"{r if r is not None else 'survives'} [{depth}]"


# ------------------------------------------------------------------ runs

def one_pair(b, am, ap, fmap, label="", o=None):
    if o is None:
        o = least_lead(b, am, ap, fmap)
    L = law_L(b, am, ap, fmap)
    c = L - o
    W = (am + ap) / (b - 1)
    g = excess(b, am, ap, fmap, L - 1)
    lam, lam_law = fmap.lam(), (W - 1) * float(b) ** (L - 1) / W
    lam_h = (lam + lam_law) / 2
    tag = f"({b},{am},{ap}) {fmap.name} {label}".strip()
    rd = ReaderD(b, am, ap, c - 1, fmap, o, lam_law)
    tk, nk, seen, rcnt = rd.scan(SCAN_KILL, region=True)
    rt, rdepth = rd.certificate_depth(TREE_CERT, confined=True)
    rd2 = ReaderD(b, am, ap, c, fmap, o)
    ts, ns, _, _ = rd2.scan(SCAN_SURV, region=False)
    rs, rdepth2 = rd2.certificate_depth(TREE_SURV)
    ok(ts is None, f"K2 kill at the law's L*={L} at {tag}: scan t={ts} n={ns}")
    ok(rs is None, f"K2 tree certifies at the law's L*={L} at {tag}: round {rs}")
    if tk is not None and tk <= rdepth:
        ok(rt == tk, f"K4 {tag} at L*-1: scan kills at t={tk}, tree at {rt} [depth {rdepth}]")
    elif tk is not None and rt is not None:
        ok(rt == tk, f"K4 {tag} at L*-1: tree certifies at round {rt} short of the scan's kill t={tk}")
    elif tk is None and rt is not None:
        ok(max(0, rt + c - 1) > nk, f"K4 {tag} at L*-1: tree certifies at round {rt} inside the scan's reach n<={nk}")
    cube = Cube(fmap, float(fmap.Mm), float(fmap.Mp), lam_h)
    reg = None
    if not cube.ok:
        ok(False, f"K7 {tag}: no cube found")
    else:
        bad = cube.spot_check()
        ok(bad is None, f"K7 {tag}: the cube's sampled points contradict {bad}")
        if bad is None:
            reg = LineRegion(b, am, ap, L - 1, g, cube)
    before = None
    if tk is not None:
        ok(nk >= max(0, c), f"P-D {tag}: kill at n={nk} below c={c}")
        if reg is not None and nk - 1 >= max(1, c):
            before = reg.count(rd, nk - 1)
            if reg.N0 is not None:
                ok(before < reg.N0, f"K5 {tag}: the line holds {before} >= N_0={reg.N0} at n={nk - 1} with no kill")
        verdict = f"kill t={tk} n={nk} (region {rcnt}; line holds {reg.count(rd, nk) if reg else '-'}, before {before})"
    else:
        if rt is None and rcnt >= REGION_K3:
            ok(False, f"K3 {tag}: no kill in the region to n={nk} ({rcnt} boxes) at L*-1, tree survives {rdepth}")
        verdict = f"no kill in the region to n={nk} ({rcnt} boxes)"
    pd = check_arithmetic(rd, reg, L - 1, c - 1, tag) if reg else "P-D unread"
    regs = (f"cube r={cube.r:.3g} e={cube.e} kappa={reg.kappa:.3g} Delta={reg.delta:.3g} N_0={reg.N0:.3g} [H={reg.H}]"
            if reg and reg.N0 else "N_0=none")
    print(f"  ({b},{am},{ap}) {label}: o={o} L*={L} c*={c} | L*-1: g={g:.3f} {regs} {verdict}; "
          f"tree {tree_word(rt, rdepth)} | L*: scan {'reached nothing' if ns < 0 else f'clean n<={ns}'}, "
          f"tree {tree_word(rs, rdepth2)} | {pd}")
    return dict(cell=(b, am, ap), o=o, L=L, c=c, g=g, tk=tk, nk=nk, rt=rt, rdepth=rdepth,
                N0=reg.N0 if reg else None, rcnt=rcnt, before=before, pd=pd, ns=ns, rdepth2=rdepth2,
                cube=cube.ok)


def census(bmax):
    return [(b, am, ap) for b in range(2, bmax + 1)
            for am in range(0, b) for ap in range(0, b)
            if am + ap + 1 - b >= 1]


def oracle(bmax):
    """P-A: x y at lead 0, x^2 + y and x y + z at lead 1, against the
    polynomial rig's TermGame certificate round."""
    for make, terms, o in ((Product, poly.XY, 0), (SquarePlus, poly.X2_PLUS_Y, 1), (MulAdd, poly.XY_PLUS_Z, 1)):
        cells = [(b, am, ap) for (b, am, ap) in census(bmax) if poly.representable(b, am, ap, terms, o)]
        print(f"\n=== P-A: {make.name} at lead {o}, {len(cells)} cells against the polynomial rig's tree")
        agree = 0
        for (b, am, ap) in cells:
            L_or = poly.lip_law(b, am, ap, terms)
            fmap = make(b, am, ap)
            ok(law_L(b, am, ap, fmap) == L_or, f"K1 {make.name} ({b},{am},{ap}): law L*={law_L(b, am, ap, fmap)} != {L_or}")
            if L_or - 1 - o < 0:
                print(f"  ({b},{am},{ap}): L*-1 below the lead, no game")
                continue
            r_or, d_or = poly.TermGame(b, am, ap, L_or - 1 - o, terms, o).certificate_depth(12, budget=TREE_ORACLE)
            r = one_pair(b, am, ap, fmap, o=o)
            good = r["tk"] == r_or and (r["rt"] == r_or if r["rt"] is not None or r["rdepth"] >= (r_or or 0) else True)
            ok(good, f"K1 {make.name} ({b},{am},{ap}): oracle round {r_or} [{d_or}], scan t={r['tk']}, tree {r['rt']} [{r['rdepth']}]")
            agree += good
        print(f"  {make.name}: {agree} of {len(cells)} cells agree with the oracle on the round")


def summarize(rows, name):
    nk = sum(1 for r in rows if r["tk"] is not None)
    print(f"  {name}: {len(rows)} pairs; leads o in {sorted(set(r['o'] for r in rows))}; L* in "
          f"{sorted(set(r['L'] for r in rows))}; certified at L*-1 at {nk}, no kill within budget at {len(rows) - nk}; "
          f"kills at output depth t in {sorted(set(r['tk'] for r in rows if r['tk'] is not None))}, "
          f"input depth n in {sorted(set(r['nk'] for r in rows if r['tk'] is not None))}; "
          f"survive at L* at {sum(1 for r in rows if r['ns'] >= 0 and r['rdepth2'] > 0)} (scan and tree reached); "
          f"the output leads (o < 0) at {sum(1 for r in rows if r['o'] < 0)}, the reader emits before it reads "
          f"(c* < 0) at {sum(1 for r in rows if r['c'] < 0)}, c* in {sorted(set(r['c'] for r in rows))}")
    N0s = [r["N0"] for r in rows if r["N0"]]
    if N0s:
        print(f"  the region at the kill: at most {max((r['rcnt'] for r in rows if r['tk'] is not None), default=0)}; "
              f"the line at the depth before the kill: at most {max((r['before'] for r in rows if r['before'] is not None), default=0)}; "
              f"N_0 from {min(N0s):.3g} to {max(N0s):.3g}; P-D read at {sum(1 for r in rows if r['pd'].startswith('P-D n='))}; "
              f"cubes at {sum(1 for r in rows if r['cube'])}")


def main():
    bmax = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    t0 = time.time()
    oracle(bmax)
    if FAILURES:
        print("\nPOSITIVE CONTROL FAILED; nothing below is read")
        for f in FAILURES:
            print("  ", f)
        return
    print(f"  controls: {time.time() - t0:.1f}s")
    print("  pair: lead o, the law's L*, lookahead c* | at L*-1: excess g, the cube, kappa, Delta, N_0, "
          "the scan's kill (t, n) with the region and line counts, the confined tree | at L* | P-D")
    print(f"\n=== P-B x^2 + x y, terms sharing a variable, radices 2..{bmax}")
    rows = [one_pair(b, am, ap, SquareCross(b, am, ap)) for (b, am, ap) in census(bmax)]
    summarize(rows, "x^2 + x y")
    print(f"\n=== P-C division x/(s + y) at the pole sweep P = j/(b - 1), radices 2..{bmax}")
    rows = []
    for j in (1, 2, 4, 8):
        for (b, am, ap) in census(bmax):
            P = Fr(j, b - 1)
            rows.append(one_pair(b, am, ap, Division(b, am, ap, P), label=f"P={j}/{b - 1}"))
    summarize(rows, "x/(s + y)")
    print(f"\nwall {time.time() - t0:.1f}s; failures: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)


if __name__ == "__main__":
    main()
