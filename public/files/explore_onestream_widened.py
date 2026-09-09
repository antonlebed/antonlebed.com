"""The one-stream theorem widened: does EVERY C^2 map of one
signed-digit stream that is not affine read at exactly the Lebesgue
margin in its derivative, the peak of |f'| anywhere in the window and
no curvature there, the necessity proved on a curved subinterval?

THE QUESTION. explore_onestream_delay.py proves that a strictly
monotone C^2 map of one stream whose |f'| peaks at a window corner
with |f''| >= kappa > 0 on an initial segment from it reads at exactly
the margin law's L*, the least L with b^L rho >= Lam (am + ap),
Lam = sup|f'|: sufficiency by the mean value theorem, necessity by a
region count and van der Corput's inequality, the depth of the kill
bounded by an N_0 free of the depth. The proof consumes the corner
only to count the half-excess region and the curvature only to
equidistribute the phase, so its hypotheses are wider than its
specimens. This rig is the widened theorem's check. Conventions as
there: radix b, digits {-am..ap}, slack rho = am + ap + 1 - b >= 1,
M+- = a+-/(b-1), W = M- + M+, the zone width W - 1 = rho/(b-1); a
prefix u of length n is the box [x_u, x_u + W/b^n], x_u = (u - M-)/b^n;
output cells at depth t and lead o in Z are [(q - M-) e, (q + M+) e],
e = b^(o - t); input depth n = t + c, L = c + o.

THE PROOF, written before the engine.

  Let f be C^2 on the window [-M-, M+], Lam = max|f'|, attained at x*
  (a corner or interior). Sufficiency at every L with
  b^L rho >= Lam (am + ap) is the mean value theorem, as before (C^1
  suffices; the image of a box is an interval since f is continuous,
  and death is a property of the image alone, the cell lemma).
  Below L* the law's excess g = Lam W / b^L - (W - 1) is positive; let
  Lam_law = (W - 1) b^L / W, Lam_h = (Lam + Lam_law)/2 < Lam, and C the
  component of the OPEN set {|f'| > Lam_h} holding x*.
  THE DICHOTOMY. If f'' = 0 on C then f' is constant, +-Lam, on C; an
  endpoint of C interior to the window has |f'| = Lam_h < Lam by
  continuity, a contradiction, so C is the whole window and f is AFFINE
  on it. Otherwise f'' != 0 at a point of C, so |f''| >= kappa > 0 with
  one sign on a subinterval I of C, and on I: every box inside I has
  excess at least g/2 (the mean value theorem, |f'| > Lam_h there), f
  is strictly monotone (the image's ends are the box's ends, in the
  map's direction), and the phase z(v) = b^(n-L) f(x_lo(v)) + M- has
  z'' = f''/b^(n+L) of one sign with |z''| >= kappa/b^(n+L) and z'
  ranging over at most Delta = g/(2W). Steps 1-4 of the corner proof
  run on I verbatim with X := |I|: the count N(n) of boxes inside I
  exceeds |I| b^n - W - 1, van der Corput's explicit inequality
  (Kuipers and Niederreiter 1974, ch. 2, Theorem 2.7) bounds every
  harmonic by (h Delta + 2)(4 b^((n+L)/2)/sqrt(h kappa) + 3),
  Erdos-Turan (Theorem 2.5) turns them into B_H(N) with
  b^n < (N + W + 1)/|I|, and at N >= N_0 := the least N with
  min_H B_H(N) < min(g/2, 1/2) a phase sits in the dead arc.
  THE WIDENED THEOREM. For a C^2 map of one stream the reader at lead o
  survives at every L with b^L rho >= Lam (am + ap) and, if f is not
  affine on the window, is dead at every L below from the depth at
  which I holds N_0 prefixes, N_0 a function of (b, L, W, g, |I|,
  kappa) and never of the depth: the delay is exactly L*. Dropped
  against the corner theorem: the corner, monotonicity on the window,
  a curvature bound on the region, and the k-th derivative test the
  inflection case seemed to need. Every interior peak of |f'| is a
  zero of f'', so "inflection peak" and "smooth interior peak" are
  one case, and the corner inflection excluded before is that case at
  a corner. The affine remainder: a rational slope is the rational-slope
  criterion's at the symmetric sets it reads (explore_slope_proof.py)
  and the k = 1 clause's at slope 1; an irrational slope has phases
  {alpha u / b^L + const}, equidistributed, dead below L* with no N_0
  free of alpha's continued fraction.
  THE FULL EXCESS. At L = 0 a map with Lam = 1 has g = W - (W - 1) = 1,
  and the dead arc (1 - g', 1) is the circle less a point: the identity
  survives at lookahead 0 only because its lattice sits on the excluded
  point, and x - eps x^3 dies at output depth 2 at (2,1,1) for every
  eps in (0, 1/2) by hand (u = 2 at n = 2: phase 1 - eps/16 in the arc
  (13 eps/8, 1)). The TRANSPLANT marked: "small curvature, deep kill"
  is the root's and the reciprocal's, whose excess at L* - 1 was small.

THE SPECIMENS, each dropping a hypothesis. x^2 over a window holding
0 (not monotone on the window; the peak at the corner of larger
magnitude, |f''| = 2) and x^3 (the polynomial entry's open Weyl step:
the corner theorem applies as written, the check is the oracle);
x - x^3/3 (an interior peak at 0, an inflection of f, monotone on
every census window since M+- <= 1, Lam = 1, so L* = 1 at every cell
where the identity reads at 0); sin x (the same shape, transcendental:
the sign of C/T - sin(X/N) decided by a float with a margin and by an
alternating rational series when the float is within 1e-9, exact
because sin of a nonzero rational is irrational); the corner
inflection y - y^3/12 at y = x - M+ (monotone on every window of width
at most 2, the peak at the corner M+ with f'' = 0 there, the corner
theorem's excluded case); x - eps x^3 at eps = 1/3, 1/30, 1/300 (the
full-excess print); and x / sqrt 2 (affine, irrational slope, no
region theorem).

THE SLATE, frozen before the engine.

P-A THE ORACLE. At every representable cell of radices 2..5 with c* >= 1
    (13 for x^2, 20 for x^3), the general engine at lead 0 and
    lookahead c* - 1 prints a scan kill at output depth t equal to
    explore_monomial_delay.py's certificate round, and its own tree's
    round equals it wherever the tree reaches; at c* the scan and the
    tree find nothing.
P-B THE INTERIOR INFLECTION. x - x^3/3 at all 20 cells: L* = 1, the
    k = 1 clause alive at L = 0, the scan kills at L = 0 at every cell
    and nothing kills at L = 1.
P-C THE TRANSCENDENTAL PEAK. sin x at all 20 cells: the same three
    prints.
P-D THE PROOF'S CONSTANT. N_0 printed per pair; at every certified kill
    with n_kill - 1 >= max(1, c*) the curved subinterval at depth
    n_kill - 1 holds fewer than N_0 prefixes; at one depth per pair
    holding at least 10^4 prefixes the observed |S_h|, h = 1..3, sits
    below van der Corput's bound and D_N below B_H(N).
P-E THE CORNER INFLECTION. y - y^3/12 at y = x - M+, all 20 cells,
    reads at L*: dead at L* - 1, alive at L*.
P-F THE FULL EXCESS. x - eps x^3 at (2,1,1), (3,1,2), (5,4,4) and
    eps = 1/3, 1/30, 1/300: the kill at L = 0 sits at output depth
    t <= 2 at every eps, while N_0 rises with 1/eps.
P-G THE IRRATIONAL SLOPE. x / sqrt 2 at all 20 cells: dead at L* - 1
    and alive at L*, no lattice clause consulted.

KILLS, frozen as what this rig PRINTS.

K1 P-A prints a disagreement with the oracle -> the general engine is
   wrong; nothing below is read.
K2 A kill at the law's L* at any pair -> the sufficiency arithmetic
   is wrong.
K3 A pair at L* - 1 with no kill in the excess region at a depth where
   the region holds at least 10^5 prefixes, the tree surviving -> the
   widened necessity fails there.
K4 The scan and the tree disagree at a depth both reach.
K5 A certified kill at n_kill with the curved subinterval at n_kill - 1
   already holding N_0 prefixes -> the proof's constant is wrong.
K6 An observed |S_h| above van der Corput's bound, or a D_N above
   B_H(N) -> the cited constants are misquoted and N_0 is unreadable.

POSITIVE CONTROL: P-A whole, read before any other line.

FINDINGS (entered post-run; every number below sits in this file's
printed output at radices 2..5).

F1 THE ORACLE HOLDS. x^2 at 13 of 13 cells and x^3 at 20 of 20: the
   general engine's scan kills at the monomial rig's round at every
   cell and its tree agrees wherever it reaches (the cube's deepest,
   (5,3,3) at round 6 with g = 0.006, sits past the tree's depth 5 and
   is the scan's, in an excess region of 726 prefixes). The square's
   kills come at output depth 1, 2 or 4 ((4,2,2) at 4), the cube's at
   1, 2, 3 or 6; nothing kills at c*. P-A held; K1 never fired.

F2 THE INTERIOR INFLECTION READS AT THE MARGIN. x - x^3/3: L* = 1 at
   all 20 cells, the k = 1 clause alive at L = 0 at all 20, the scan
   killing at L = 0 at all 20 (output depth 1 or 2, input depth 1 or 2,
   an excess region of at most 15 prefixes) and the reader surviving
   at L = 1 at all 20, scan and tree. P-B held.

F3 THE TRANSCENDENTAL PEAK. sin x: the same three prints at all 20
   cells (kills at output depth 1 or 2, region at most 9); 2,682
   decisions fell to the exact series, 2,618 of them where a cell
   boundary equals a box end and sin x - x is under 1e-9, the other 64
   chance near-ties at output depth 15 and beyond, where the cell grid
   is 3e-5 fine; the series decided every one. P-C held.

F4 THE CORNER INFLECTION. y - y^3/12 at y = x - M+: the range needs the
   lead o = 1 at every cell, so c* = 0; dead at L = 0 at all 20 cells
   (10 of them by the window itself, n = 0), alive at L* = 1 at all 20.
   P-E held.

F5 THE FULL EXCESS. x - eps x^3 at eps = 1/3, 1/30, 1/300: the kill at
   L = 0 sits at output depth 2 at (2,1,1) and 1 at (3,1,2) and (5,4,4)
   at every eps, while N_0 rises tenfold per decade of eps (8.8e4,
   2.2e5, 2.2e6 at (2,1,1)). The kill depth is not a function of the
   curvature: the arc at the full excess is the circle less a point.
   P-F held.

F6 THE IRRATIONAL SLOPE. x / sqrt 2: L* = 1 at all 20 cells, dead at
   L = 0 at all 20 (output depth 1 or 2) and alive at L = 1 at all 20,
   no region theorem and no lattice clause. P-G held.

F7 THE PROOF'S CONSTANT. N_0 runs from 4.4e4 to 5.1e10 (the cube at
   (5,3,3)); the curved subinterval at the depth before every certified
   kill holds at most 34 prefixes (that cube), and none at any pair of
   P-B, P-C, P-E and P-F where such a depth exists: the kill precedes
   the region theorem's first prefix. 102 pairs read at N from 10,031 to 48,826 phases: the
   observed |S_h| at h = 1, 2, 3 is at most 0.11 of van der Corput's
   bound, the observed D_N at most 0.010, and B_H(N) below 1, the check
   biting, at 73 of the 102. K5 and K6 never fired; P-D held.

VERDICT. Every C^2 map of one stream that is not affine reads at exactly
the margin law's L*: the corner, the monotonicity on the window, the
curvature bound and the k-th derivative test were hypotheses of the
specimens, not of the proof. The affine remainder splits by slope:
rational to the rational-slope criterion at symmetric sets, irrational
to the margin at every cell read.

RUN RECORD: pure Python, integers for every verdict and floats for the
candidates, the counts and the phases, standard library; under
memwatch, peak commit 44.3 MB against the 512 MB default; wall 68 s
at radices 2..5 (19 s at 2..3). Prints reproduced by:
python prime/code/explore_onestream_widened.py [BMAX]
"""

import math
import sys
import time
from fractions import Fraction as Fr

import explore_monomial_delay as mono
import explore_onestream_delay as one
import explore_sqrt_delay as sq

FAILURES = []
SCAN_KILL, SCAN_SURV, TREE_CERT, TREE_SURV = 1_000_000, 300_000, 200_000, 50_000
TREE_ORACLE = 2_000_000        # the monomial rig's own node budget
PHASE_MIN = 10_000
SQRT2 = math.sqrt(2)


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


def sgn(x):
    return (x > 0) - (x < 0)


# ------------------------------------------------------------ the maps
# A map exposes: cmp(C, T, X, N) = sign of C/T - f(X/N) exactly on
# integers; approx(X, N) a float; ends(X1, X2) the arguments of the
# image's lower and upper ends over an integer box; fits(b, Mm, Mp, o)
# the range inside the root cell at lead o; law_ok(b, rho, wsum, L) the
# margin law at L, exactly; lam() = max|f'|; region(lam) the intervals
# of the window where |f'| >= lam; curved(lam_h) a subinterval of the
# peak's component with |f''| >= kappa, as (x1, x2, kappa), or None
# when f is affine.

class Square:
    name = "x^2"

    def __init__(self, b, am, ap):
        self.b, self.am, self.ap = b, am, ap
        self.Mm, self.Mp = Fr(am, b - 1), Fr(ap, b - 1)
        self.side = 1 if self.Mp >= self.Mm else -1
        self.Mh = max(self.Mm, self.Mp)

    def cmp(self, C, T, X, N):
        return sgn(C * N * N - T * X * X)

    def approx(self, X, N):
        return (X / N) ** 2

    def ends(self, X1, X2):
        if X1 <= 0 <= X2:
            return 0, (X1 if -X1 >= X2 else X2)
        return (X2, X1) if X2 < 0 else (X1, X2)

    def fits(self, b, Mm, Mp, o):
        return self.Mh ** 2 <= Mp * Fr(b) ** o

    def law_ok(self, b, rho, wsum, L):
        return Fr(b) ** L * rho * (b - 1) >= 2 * max(self.am, self.ap) * wsum

    def lam(self):
        return 2 * float(self.Mh)

    def region(self, lam):
        r = lam / 2
        out = []
        if r <= self.Mp:
            out.append((r, float(self.Mp)))
        if r <= self.Mm:
            out.append((-float(self.Mm), -r))
        return out

    def curved(self, lam_h):
        r = lam_h / 2
        if self.side > 0:
            return r, float(self.Mp), 2.0
        return -float(self.Mm), -r, 2.0


class Cube:
    name = "x^3"

    def __init__(self, b, am, ap):
        self.b, self.am, self.ap = b, am, ap
        self.Mm, self.Mp = Fr(am, b - 1), Fr(ap, b - 1)
        self.side = 1 if self.Mp >= self.Mm else -1
        self.Mh = max(self.Mm, self.Mp)

    def cmp(self, C, T, X, N):
        return sgn(C * N ** 3 - T * X ** 3)

    def approx(self, X, N):
        return (X / N) ** 3

    def ends(self, X1, X2):
        return X1, X2

    def fits(self, b, Mm, Mp, o):
        return self.Mp ** 3 <= Mp * Fr(b) ** o and self.Mm ** 3 <= Mm * Fr(b) ** o

    def law_ok(self, b, rho, wsum, L):
        return Fr(b) ** L * rho * (b - 1) ** 2 >= 3 * max(self.am, self.ap) ** 2 * wsum

    def lam(self):
        return 3 * float(self.Mh) ** 2

    def region(self, lam):
        r = math.sqrt(lam / 3)
        out = []
        if r <= self.Mp:
            out.append((r, float(self.Mp)))
        if r <= self.Mm:
            out.append((-float(self.Mm), -r))
        return out

    def curved(self, lam_h):
        r = math.sqrt(lam_h / 3)
        if self.side > 0:
            return r, float(self.Mp), 6 * r
        return -float(self.Mm), -r, 6 * r


class CubicPeak:
    """x -> x - x^3/E, |f'| = 1 - 3x^2/E peaking at 0, an inflection."""

    def __init__(self, b, am, ap, E):
        self.b, self.am, self.ap, self.E = b, am, ap, E
        self.Mm, self.Mp = Fr(am, b - 1), Fr(ap, b - 1)
        self.name = f"x - x^3/{E}"

    def f(self, x):
        return x - x ** 3 / self.E

    def cmp(self, C, T, X, N):
        E = self.E
        return sgn(C * E * N ** 3 - T * (E * X * N * N - X ** 3))

    def approx(self, X, N):
        return self.f(X / N)

    def ends(self, X1, X2):
        return X1, X2

    def fits(self, b, Mm, Mp, o):
        return self.f(Mp) <= Mp * Fr(b) ** o and -self.f(-Mm) <= Mm * Fr(b) ** o

    def law_ok(self, b, rho, wsum, L):
        return Fr(b) ** L * rho >= wsum

    def lam(self):
        return 1.0

    def _radius(self, lam):
        return math.sqrt((1 - lam) * self.E / 3) if lam < 1 else -1.0

    def region(self, lam):
        R = self._radius(lam)
        if R < 0:
            return []
        return [(max(-float(self.Mm), -R), min(float(self.Mp), R))]

    def curved(self, lam_h):
        R = self._radius(lam_h)
        rp, rm = min(float(self.Mp), R), min(float(self.Mm), R)
        kap = lambda r: 6 * (r / 2) / self.E    # noqa: E731  |f''| at r/2
        if rp >= rm:
            return rp / 2, rp, kap(rp)
        return -rm, -rm / 2, kap(rm)


class Sine:
    name = "sin x"

    def __init__(self, b, am, ap):
        self.b, self.am, self.ap = b, am, ap
        self.Mm, self.Mp = Fr(am, b - 1), Fr(ap, b - 1)
        self.exact_calls = 0

    def cmp(self, C, T, X, N):
        d = C / T - math.sin(X / N)
        if abs(d) > 1e-9:
            return sgn(d)
        if X == 0:
            return sgn(C)
        self.exact_calls += 1
        x, target = Fr(X, N), Fr(C, T)
        term, s, k = x, Fr(0), 0
        while True:                      # alternating, terms decreasing for |x| <= 1
            s_next = s + term
            lo, hi = (s, s_next) if term > 0 else (s_next, s)
            if target < lo:
                return -1
            if target > hi:
                return 1
            s = s_next
            k += 1
            term = -term * x * x / ((2 * k) * (2 * k + 1))

    def approx(self, X, N):
        return math.sin(X / N)

    def ends(self, X1, X2):
        return X1, X2

    def fits(self, b, Mm, Mp, o):
        # sin x <= x on [0, 1] fits every o >= 0; at o < 0, sin x >= 5x/6 > x/b
        return o >= 0

    def law_ok(self, b, rho, wsum, L):
        return Fr(b) ** L * rho >= wsum

    def lam(self):
        return 1.0

    def region(self, lam):
        if lam >= 1:
            return []
        R = math.acos(lam)
        return [(max(-float(self.Mm), -R), min(float(self.Mp), R))]

    def curved(self, lam_h):
        R = math.acos(lam_h)
        rp, rm = min(float(self.Mp), R), min(float(self.Mm), R)
        if rp >= rm:
            return rp / 2, rp, math.sin(rp / 2)
        return -rm, -rm / 2, math.sin(rm / 2)


class CornerCubic:
    """x -> y - y^3/12, y = x - M+: the peak of |f'| at the corner M+
    with f'' = 0 there; monotone on every window of width <= 2."""
    name = "y - y^3/12, y = x - M+"

    def __init__(self, b, am, ap):
        self.b, self.am, self.ap = b, am, ap
        self.Mm, self.Mp = Fr(am, b - 1), Fr(ap, b - 1)
        self.W = self.Mm + self.Mp

    def h(self, y):
        return y - y ** 3 / 12

    def cmp(self, C, T, X, N):
        Y, D = (self.b - 1) * X - self.ap * N, (self.b - 1) * N
        return sgn(C * 12 * D ** 3 - T * (12 * Y * D * D - Y ** 3))

    def approx(self, X, N):
        return self.h(X / N - float(self.Mp))

    def ends(self, X1, X2):
        return X1, X2

    def fits(self, b, Mm, Mp, o):
        return -self.h(-self.W) <= Mm * Fr(b) ** o

    def law_ok(self, b, rho, wsum, L):
        return Fr(b) ** L * rho >= wsum

    def lam(self):
        return 1.0

    def region(self, lam):
        if lam >= 1:
            return []
        r = min(float(self.W), 2 * math.sqrt(1 - lam))
        return [(float(self.Mp) - r, float(self.Mp))]

    def curved(self, lam_h):
        r = min(float(self.W), 2 * math.sqrt(1 - lam_h))
        return float(self.Mp) - r, float(self.Mp) - r / 2, r / 4


class IrrationalSlope:
    name = "x / sqrt 2"

    def __init__(self, b, am, ap):
        self.b, self.am, self.ap = b, am, ap
        self.Mm, self.Mp = Fr(am, b - 1), Fr(ap, b - 1)

    def cmp(self, C, T, X, N):
        A, B = C * N, T * X                 # sign of sqrt2 A - B, T and N > 0
        if sgn(A) != sgn(B):
            return sgn(A) if A != 0 else -sgn(B)
        s = sgn(A)
        return s * sgn(2 * A * A - B * B)

    def approx(self, X, N):
        return X / N / SQRT2

    def ends(self, X1, X2):
        return X1, X2

    def fits(self, b, Mm, Mp, o):
        return o >= 0                        # x/sqrt2 fits at 0; at o < 0 needs 1/sqrt2 <= 1/b

    def law_ok(self, b, rho, wsum, L):
        return 2 * (Fr(b) ** L * rho) ** 2 >= wsum * wsum

    def lam(self):
        return 1 / SQRT2

    def region(self, lam):
        if lam > 1 / SQRT2:
            return []
        return [(-float(self.Mm), float(self.Mp))]

    def curved(self, lam_h):
        return None


# ---------------------------------------------------------- the engine

class GReader(one.Reader):
    """The one-stream reader with the image's ends taken from the map."""

    def ends(self, u, n):
        b = self.b
        X1, X2, N = (b - 1) * u - self.am, (b - 1) * u + self.ap, (b - 1) * b ** n
        lo, hi = self.f.ends(X1, X2)
        return lo, hi, N

    def region_prefixes(self, n, intervals):
        """Prefixes of length n whose box meets one of the open intervals."""
        b, Mm, Mp = self.b, self.am / (self.b - 1), self.ap / (self.b - 1)
        umin, umax = self.prefixes(n)
        out = set()
        for (x1, x2) in intervals:
            lo = math.floor(x1 * b ** n - Mp - 1e-9) + 1
            hi = math.ceil(x2 * b ** n + Mm + 1e-9) - 1
            out.update(range(max(lo, umin), min(hi, umax) + 1))
        return sorted(out)

    def scan_region(self, budget, intervals):
        """The least output depth t at which some prefix of length
        max(0, t + c) meeting the excess region straddles a depth-t
        zone. Returns (t or None, n at the kill or the last n scanned,
        prefixes seen, the region's count at that n)."""
        t, seen, last_n, last_cnt = 0, 0, -1, 0
        while True:
            t += 1
            n = max(0, t + self.c)
            us = self.region_prefixes(n, intervals)
            if seen + len(us) > budget:
                return None, last_n, seen, last_cnt
            for i, u in enumerate(us):
                if self.straddles(u, n, t):
                    return t, n, seen + i + 1, len(us)
            seen += len(us)
            last_n, last_cnt = n, len(us)


class GRegion(one.Region):
    """The curved subinterval I of a pair at L: its length X, kappa,
    Delta, the count of boxes inside it at depth n, and N_0 with its H."""

    def __init__(self, b, am, ap, L, g, x1, x2, kappa):
        self.b, self.am, self.ap, self.L, self.g = b, am, ap, L, g
        self.W = (am + ap) / (b - 1)
        self.x1, self.x2, self.X, self.kappa = x1, x2, x2 - x1, kappa
        self.delta = g / (2 * self.W)
        self.a = min(g / 2, 0.5)
        self.N0, self.H = self.n0()

    def prefix_range(self, n):
        b, Mm, Mp = self.b, self.am / (self.b - 1), self.ap / (self.b - 1)
        lo = math.ceil(self.x1 * b ** n + Mm + 1e-9)
        hi = math.floor(self.x2 * b ** n - Mp - 1e-9)
        lo = max(lo, -self.am * (b ** n - 1) // (b - 1))
        hi = min(hi, self.ap * (b ** n - 1) // (b - 1))
        return lo, hi

    def count(self, n):
        lo, hi = self.prefix_range(n)
        return max(0, hi - lo + 1)

    def bound(self, N, H):
        b, L = self.b, self.L
        A = 4 * float(b) ** (L / 2) * math.sqrt((N + self.W + 1) / (self.X * self.kappa))
        s1, s2, s3 = one.PSUMS[0][H], one.PSUMS[1][H], one.PSUMS[2][H]
        s = (self.delta * A * s1 + 3 * self.delta * H + 2 * A * s2 + 6 * s3) / N
        return 6 / (H + 1) + 4 / math.pi * s


def phases(rd, reg, n, L):
    lo, hi = reg.prefix_range(n)
    scale = float(rd.b) ** (n - L)
    Mm = rd.am / (rd.b - 1)
    out = []
    for u in range(lo, hi + 1):
        Xlo, _, N = rd.ends(u, n)
        z = rd.f.approx(Xlo, N) * scale + Mm
        out.append(z - math.floor(z))
    return out


def check_arithmetic(rd, reg, L, c, label):
    n = max(1, c + 1)
    while reg.count(n) < PHASE_MIN and n < 60:
        n += 1
    N = reg.count(n)
    if N < PHASE_MIN:
        return f"P-D skipped (region {N} at n={n})"
    zs = phases(rd, reg, n, L)
    D = one.discrepancy(zs)
    B = reg.bound(N, reg.H) if reg.H else float("inf")
    ok(D <= B, f"K6 {label}: D_N={D:.4f} above B_H(N)={B:.4f} at n={n}, N={N}")
    ratios = []
    for h in (1, 2, 3):
        S = abs(sum(one.cmath.exp(2j * math.pi * h * z) for z in zs))
        Vb = reg.vdc_bound(n, h)
        ok(S <= Vb, f"K6 {label}: |S_{h}|={S:.1f} above van der Corput's {Vb:.1f} at n={n}, N={N}")
        ratios.append(S / Vb)
    bites = sum(1 for h in (1, 2, 3) if reg.vdc_bound(n, h) < N)
    return (f"P-D n={n} N={N}: D_N={D:.3f} vs B={B:.2f}; |S_h|/vdC="
            f"{','.join(f'{r:.2f}' for r in ratios)} (bound below N at {bites} of 3)")


# ------------------------------------------------------------------ runs

def one_pair(b, am, ap, fmap, label="", o=None):
    if o is None:
        o = one.least_lead(b, am, ap, fmap)
    L = one.law_L(b, am, ap, fmap)
    c = L - o
    W = (am + ap) / (b - 1)
    g = one.excess(b, am, ap, fmap, L - 1)
    lam, lam_law = fmap.lam(), (W - 1) * float(b) ** (L - 1) / W
    lam_h = (lam + lam_law) / 2
    rd = GReader(b, am, ap, c - 1, fmap, o)
    tk, nk, seen, rcnt = rd.scan_region(SCAN_KILL, fmap.region(lam_law))
    rt, rdepth = rd.certificate_depth(TREE_CERT)
    rd2 = GReader(b, am, ap, c, fmap, o)
    ts, ns, _, _ = rd2.scan_kill(SCAN_SURV)
    rs, rdepth2 = rd2.certificate_depth(TREE_SURV)
    tag = f"({b},{am},{ap}) {fmap.name} {label}".strip()
    ok(ts is None, f"K2 kill at the law's L*={L} at {tag}: scan t={ts} n={ns}")
    ok(rs is None, f"K2 tree certifies at the law's L*={L} at {tag}: round {rs}")
    if tk is not None and tk <= rdepth:
        ok(rt == tk, f"K4 {tag} at L*-1: scan kills at t={tk}, tree at {rt} [depth {rdepth}]")
    elif tk is not None and rt is not None:
        ok(rt == tk, f"K4 {tag} at L*-1: tree certifies at round {rt} short of the scan's kill t={tk}")
    elif tk is None and rt is not None:
        ok(max(0, rt + c - 1) > nk, f"K4 {tag} at L*-1: tree certifies at round {rt} inside the scan's reach n<={nk}")
    cur = fmap.curved(lam_h)
    reg = GRegion(b, am, ap, L - 1, g, *cur) if cur else None
    before = None
    if tk is not None:
        ok(nk >= c, f"P-D {tag}: kill at n={nk} below c={c}")
        if reg is not None and nk - 1 >= max(1, c):
            before = reg.count(nk - 1)
            if reg.N0 is not None:
                ok(before < reg.N0, f"K5 {tag}: I holds {before} >= N_0={reg.N0} at n={nk - 1} with no kill")
        verdict = f"kill t={tk} n={nk} (excess region {rcnt}; I holds {reg.count(nk) if reg else '-'}, before {before})"
    else:
        if rt is None and rcnt >= 100_000:
            ok(False, f"K3 {tag}: no kill in the region to n={nk} ({rcnt} prefixes) at L*-1, tree survives {rdepth}")
        verdict = f"no kill in the region to n={nk} ({rcnt} prefixes)"
    pd = check_arithmetic(rd, reg, L - 1, c - 1, tag) if reg else "affine: no region theorem"
    regs = f"I=[{reg.x1:.3g},{reg.x2:.3g}] kappa={reg.kappa:.3g} N_0={reg.N0:.3g} [H={reg.H}]" if reg and reg.N0 else "N_0=none"
    print(f"  ({b},{am},{ap}) {label}: o={o} L*={L} c*={c} | L*-1: g={g:.3f} {regs} {verdict}; "
          f"tree {one.tree_word(rt, rdepth)} | L*: scan {'reached nothing' if ns < 0 else f'clean n<={ns}'}, "
          f"tree {one.tree_word(rs, rdepth2)} | {pd}")
    return dict(cell=(b, am, ap), o=o, L=L, c=c, g=g, tk=tk, nk=nk, rt=rt, rdepth=rdepth,
                N0=reg.N0 if reg else None, rcnt=rcnt, half=reg.count(nk) if (reg and nk >= 0) else None,
                before=before, pd=pd, ns=ns, rdepth2=rdepth2)


def oracle(bmax):
    """P-A: x^2 and x^3 at lead 0 against explore_monomial_delay.py."""
    for d, make in ((2, Square), (3, Cube)):
        cells = [(b, am, ap) for (b, am, ap) in mono.census(bmax)
                 if mono.representable(b, am, ap, (d,)) and mono.monomial_law(b, am, ap, d) >= 1]
        print(f"\n=== P-A: x^{d} at lead 0, {len(cells)} cells against the monomial rig's tree")
        agree = 0
        for (b, am, ap) in cells:
            cs = mono.monomial_law(b, am, ap, d)
            r_or, d_or = mono.KGame(b, am, ap, cs - 1, (d,)).certificate_depth(12, budget=TREE_ORACLE)
            fmap = make(b, am, ap)
            ok(one.law_L(b, am, ap, fmap) == cs, f"K1 x^{d} ({b},{am},{ap}): law L*={one.law_L(b, am, ap, fmap)} != c*={cs}")
            r = one_pair(b, am, ap, fmap, o=0)
            good = r["tk"] == r_or and (r["rt"] == r_or if r["rt"] is not None or r["rdepth"] >= (r_or or 0) else True)
            ok(good, f"K1 x^{d} ({b},{am},{ap}): oracle round {r_or} [{d_or}], scan t={r['tk']}, tree {r['rt']} [{r['rdepth']}]")
            agree += good
        print(f"  x^{d}: {agree} of {len(cells)} cells agree with the oracle on the round")


def run_family(title, make, bmax, cells=None):
    print(f"\n=== {title}, radices 2..{bmax}")
    rows = []
    for (b, am, ap) in (cells or sq.census(bmax)):
        fmap = make(b, am, ap)
        r = one_pair(b, am, ap, fmap)
        r["clause0"] = sq.ksum_clause_dead(1, b, am, ap, 0)
        rows.append(r)
    nk = sum(1 for r in rows if r["tk"] is not None)
    print(f"  {len(rows)} cells; L* values {sorted(set(r['L'] for r in rows))}; the k = 1 clause dead at L = 0 at "
          f"{sum(1 for r in rows if r['clause0'])}; certified at L*-1 at {nk}, no kill within budget at {len(rows) - nk}; "
          f"kills at output depth t in {sorted(set(r['tk'] for r in rows if r['tk'] is not None))}, "
          f"input depth n in {sorted(set(r['nk'] for r in rows if r['tk'] is not None))}; "
          f"survive at L* at {sum(1 for r in rows if r['ns'] >= 0 and r['rdepth2'] > 0)} (scan and tree reached)")
    N0s = [r["N0"] for r in rows if r["N0"]]
    if N0s:
        print(f"  the excess region at the kill: at most {max((r['rcnt'] for r in rows if r['tk'] is not None), default=0)}; "
              f"I at the depth before the kill: at most {max((r['before'] for r in rows if r['before'] is not None), default=0)}; "
              f"N_0 from {min(N0s):.3g} to {max(N0s):.3g}; P-D read at {sum(1 for r in rows if r['pd'].startswith('P-D n='))}")
    return rows


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
    print("  cell: lead o, the law's L*, lookahead c* | at L*-1: excess g, the curved subinterval I, kappa, N_0, "
          "the scan's kill (t, n) with the region counts, the tree | at L* | P-D")
    run_family("P-B x - x^3/3, the interior inflection", lambda b, am, ap: CubicPeak(b, am, ap, 3), bmax)
    sines = []
    run_family("P-C sin x, the transcendental peak", lambda b, am, ap: sines.append(Sine(b, am, ap)) or sines[-1], bmax)
    print(f"  sin: exact series decisions {sum(s.exact_calls for s in sines)}")
    run_family("P-E the corner inflection y - y^3/12, y = x - M+", CornerCubic, bmax)
    print("\n=== P-F the full excess: x - eps x^3 at three cells")
    for (b, am, ap) in ((2, 1, 1), (3, 1, 2), (5, 4, 4)):
        for E in (3, 30, 300):
            one_pair(b, am, ap, CubicPeak(b, am, ap, E))
    run_family("P-G the irrational slope x / sqrt 2", IrrationalSlope, bmax)
    print(f"\nwall {time.time() - t0:.1f}s; failures: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)


if __name__ == "__main__":
    main()
