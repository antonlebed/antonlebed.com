"""The one-stream theorem: is the delay of every monotone map of one
signed-digit stream whose derivative peaks at a window corner with
curvature exactly the Lebesgue margin in that derivative, proved by a
region count free of the depth, the reciprocal its second pole?

THE QUESTION. explore_sqrt_delay.py certified the square root
x -> sqrt(s + x), s = M- + P, at the margin law's L* at 150 (cell, P)
pairs, sufficiency the law's theorem and necessity a region scan pair
by pair, and named the proof it owed: the reachable lower endpoints
over the excess region have a quadratic phase, so they equidistribute
and one lands in the dead arc once the region is large enough. This
rig is that proof's check, and the proof is general. Conventions as
there: radix b, digits {-am..ap}, slack rho = am + ap + 1 - b >= 1,
M+- = a+-/(b-1), W = M- + M+, the zone width W - 1 = rho/(b-1); a
prefix u of length n is the box [x_u, x_u + W/b^n], x_u = (u - M-)/b^n;
output cells at depth t and lead o in Z are [(q - M-) e, (q + M+) e],
e = b^(o - t); input depth n = t + c, L = c + o.

THE PROOF, written before the engine (the four passes, condensed).

  1. THE DEAD ARC. In units of e, an image of lower end y and width w
     strictly contains the zone between cells q and q+1 iff
     q + 1 - g' < y + M- < q + 1 with g' = w - (W - 1), the prefix's
     EXCESS: for 0 < g' <= 1, iff the phase {y + M-} lies in the arc
     (1 - g', 1). Death at output depth t is a property of the image
     alone (the cell lemma), so the reader is dead at t iff some prefix
     of length t + c has positive excess and its phase in its arc.
  2. THE HALF-EXCESS REGION. Let f be strictly monotone and C^2 on the
     window, Lam = sup|f'| taken at the corner x = -M- (the mirror
     case by x -> -x), |f'| nonincreasing on an initial segment from
     it. At L the law's excess is g = Lam W / b^L - (W - 1), positive
     exactly below L*. By the mean value theorem the excess of the box
     at offset x from the corner is (W/b^L)|f'(xi)| - (W - 1) for some
     xi in the box. Let Lam_h = (Lam + Lam_law)/2, Lam_law = (W-1) b^L/W
     the law's threshold, X_h = sup{x : |f'| >= Lam_h on [0, x]},
     X_h' = min(X_h, W). The region R_n = {v >= 0 : v + W <= X_h' b^n}
     (v = u - u_min) has every excess >= g/2, count
     N(n) = floor(X_h' b^n - W) + 1 > X_h' b^n - W, so
     b^n < (N + W)/X_h'; and two constants free of n: Delta = g/(2W),
     the range of |f'|/b^L over the region, and kappa = min|f''| over
     [0, X_h'], positive when f'' has one sign there.
  3. THE PHASE EQUIDISTRIBUTES. z(v) = b^(n-L) f_lo(v) + M-, f_lo the
     lower end's argument, has z' = f'/b^L and z'' = f''/b^(n+L). For
     the h-th harmonic van der Corput's inequality in its explicit
     form (Kuipers and Niederreiter, Uniform Distribution of Sequences,
     1974, ch. 2, Theorem 2.7) gives
       |S_h| <= (h Delta + 2)(4 b^((n+L)/2)/sqrt(h kappa) + 3),
     and Erdos-Turan (ibid., Theorem 2.5) gives, for every H >= 1,
       D_N <= 6/(H+1) + (4/pi) sum_{h<=H} |S_h|/(h N).
     With the count bound, B_H(N) := 6/(H+1) + (4/pi) sum_{h<=H}
     (1/h)(h g/(2W) + 2)(4 b^(L/2) sqrt((N+W)/(X_h' h kappa)) + 3)/N
     bounds D_N and decreases in N; N_0 := the least N with
     min_H B_H(N) < a, a = min(g/2, 1/2). Whenever N(n) >= N_0 the arc
     (1 - a, 1) holds a phase, its prefix's excess is >= g/2 >= a, and
     step 1 kills the reader at output depth n - c.
  4. THE ONE-STREAM THEOREM. Under those hypotheses (monotone, C^2,
     |f'| peaking at a corner and nonincreasing on [0, X_h'] from it,
     |f''| >= kappa > 0 there) the reader at lead o is alive at every
     lookahead with b^(c+o) rho >= Lam (am + ap) and dead at every one
     below, from the depth at which the half-excess region holds N_0
     prefixes; the delay is exactly the margin law's L*. N_0 depends on
     (b, L, W, g, X_h', kappa) and never on the depth. Excluded: an
     inflection at the corner (kappa = 0) and an interior maximum of
     |f'|.

THE SPECIMENS. The square root (Lam = 1/(2 sqrt P), |f''| =
(P + x)^(-3/2)/4, increasing, concave) and THE RECIPROCAL
x -> 1/(s + x), s = M- + P (Lam = 1/P^2, |f''| = 2/(P + x)^3,
DECREASING and convex, the range [1/(P + W), 1/P] with its top at the
pole side, the lead o the least integer with 1/P <= M+ b^o, zero or
negative for P at or above 1/M+): the law reads b^L rho P^2 >= am + ap,
so along the pole arm P = 1/((b-1) b^m) the delay rises by TWO per
digit of pole depth where the square root's rose by one per two. The
image of a decreasing map's box [x1, x2] is [f(x2), f(x1)], so the
engine takes the image's ends from the map's direction, and the lead
search runs over Z. The control x -> s + x has kappa = 0 and no region
theorem; its delay is the k = 1 affine clause.

THE SLATE, frozen before the engine.

P-A THE CONTROLS. (i) The shift x -> s + x, s in {1, 2, 6} above M-,
    at every cell of radices 2..5 and L in {-1, 0, 1}: the general
    engine's scan and tree agree with the k = 1 clause. (ii) The
    square root's 150 pairs (the 20 census cells at P = j/(b-1),
    j in {1, 2, 4, 8, 32, 128}, and six cells at P = 1/((b-1) b^m),
    m = 1..5) through the general engine reproduce
    explore_sqrt_delay.py's lead, L*, and its region scan's kill
    (output depth t, input depth n) at L* - 1, that rig's scan called
    as the oracle.
P-B THE RECIPROCAL'S TABLE. L* nonincreasing in P at every cell; at
    the pole arm L* rises by exactly two per m (the law's own
    arithmetic; the square root's one per two digits is the transplant
    it is read against); the lead o <= 0 wherever P >= 1/M+.
P-C SUFFICIENCY. No kill at L* at any reciprocal pair: the scan to its
    budget and the tree to its depth.
P-D NECESSITY. At L* - 1 the region scan kills at every reciprocal
    pair within budget, at n_kill at or past the convexity floor
    n_conc (the least n with the corner box's deficit under g) and at
    or past c + 1; the tree agrees wherever its depth reaches.
P-E THE PROOF'S CONSTANT. N_0 printed per pair for both maps; at every
    certified kill with n_kill - 1 >= max(1, c + 1), the half-excess
    region at depth n_kill - 1 holds fewer than N_0 prefixes (the
    proof promises death at the first depth with N_0, and the scan's
    kill is the least, so the depth before it must fall short).
P-F THE PROOF'S ARITHMETIC. At one depth per pair where the half-excess
    region holds at least 10^4 prefixes, the observed |S_h| for
    h = 1..3 sits at or below van der Corput's bound at the actual
    b^((n+L)/2), and the observed discrepancy D_N at or below B_H(N)
    at the H that set N_0.

KILLS, frozen as what this rig PRINTS.

K1 P-A prints a clause disagreement or an oracle disagreement -> the
   general engine is wrong; nothing below is read.
K2 A kill at the law's L* -> the sufficiency arithmetic is wrong.
K3 A reciprocal pair at L* - 1 with no kill in the excess region at a
   depth where the region holds at least 10^5 prefixes with the corner
   deficit under g/2, the tree surviving -> the law is not the floor
   at the second pole.
K4 The scan and the tree disagree at a depth both reach -> the
   no-strategy step fails, or the straddle candidate is wrong.
K5 A certified kill at n_kill with the half-excess region at n_kill - 1
   already holding N_0 prefixes -> the proof's constant is wrong.
K6 An observed |S_h| above van der Corput's bound, or a D_N above
   B_H(N) -> the cited constants are misquoted and N_0 is unreadable.

POSITIVE CONTROL: P-A whole, read before any reciprocal line.

FINDINGS (entered post-run; every number below sits in this file's
printed output at radices 2..5).

F1 THE CONTROLS HOLD. The shift: 150 of 150 cell-shift-L triples agree
   with the k = 1 clause, scan and tree. The square root: 150 of 150
   pairs agree with explore_sqrt_delay.py on (o, L*, t, n). P-A held;
   K1 never fired.

F2 THE RECIPROCAL'S TABLE. 120 pairs, L* nonincreasing in P at every
   cell; at j = 1 L* is 3 at 18 of the 20 cells, 2 at (3,2,2) and 1 at
   (2,1,1); over the sweep L* runs from 3 down to -13, the lead o is
   at or below 0 at 73 of 120 (down to -7 at (2,1,1), P = 128) and
   the lookahead c* negative at 40 of 120 (down to -6). P-B held.

F3 SUFFICIENCY'S ARITHMETIC. No kill at L* at any of the 300 pairs
   (the scan to its budget, the tree to its depth); at one pole-arm
   pair, (5,4,4) m = 5, neither instrument reached a prefix within
   budget, the print says so, and the law's theorem is the only
   witness there. K2 never fired.

F4 THE RECIPROCAL READS AT THE MARGIN. At L* - 1 the region scan
   certifies 120 of 120: the kill at output depth t from 1 to 8 and
   input depth n from 0 to 10, at n_kill - n_conc in {0, 1, 2, 3}; 14
   kills are the window itself; the excess region holds at most 84
   prefixes at the kill and the half-excess region at most 38. The
   tree agrees with the scan at 141 of the 150 reciprocal pairs, its
   depth short of the kill at 7 and unreached at 2. K3 and K4 never
   fired.

F5 THE POLE ARM IS A RESCALING. 30 pairs, all certified at L* - 1 and
   surviving at L*; L* by m = 1..5 reads [3,5,7,9,11] at (2,1,1),
   [4,6,8,10,12] at (3,2,2) and [5,7,9,11,13] at the other four:
   every step exactly two, as the law says. And the kill moves with
   it whole: at (2,1,1) every m kills at t = 3 and n = m + 3 in an
   excess region of 5 prefixes, at (5,3,3) at t = 2 and n = m + 2 in a
   region of 4. The reason is homogeneity: 1/(P/b^m + x) at x/b^m is
   b^m/(P + x), so the game at pole depth m is the game at depth 0
   with the input read m digits deeper and the output m digits
   larger, L up by 2m exactly; the square root's b^(-m/2) scaling
   gives its one per two digits and its kills repeating at m, m + 2.

F6 THE PROOF'S CONSTANT. N_0 runs from 5.5e4 to 7.6e7 over the
   reciprocal's pairs and from 6.7e4 to 1.3e9 over the square root's;
   the half-excess region at the depth before the kill holds at most
   35 prefixes (square root) and 7 (reciprocal), so N_0 is at least
   5.5e4 times that count at every pair: the proof's depth is never
   approached. K5 never fired.

F7 THE PROOF'S ARITHMETIC. 300 pairs read at N from 10,007 to 46,672
   phases (n from 6 to 21): the observed |S_h| at h = 1, 2, 3 is at
   most 0.11 of van der Corput's bound, the bound itself below N at
   all 900 reads; the observed D_N is at most 0.019, and B_H(N) is
   below 1, the check biting, at 117 of the 300. K6 never fired.

VERDICT. The one-stream theorem holds at both poles: the reciprocal,
decreasing and convex with its range's top at the pole side, reads at
the margin law's L* at all 150 pairs, rising by two per digit of pole
depth by the law and by homogeneity; the necessity proof's constants
survive their numerical check at every pair; and the square root's
delay, a criterion pair by pair before, is the theorem's first
specimen.

RUN RECORD: pure Python, integers for every verdict and floats for the
candidates, the counts and the phases, standard library; under
memwatch, peak commit 44.7 MB against the 512 MB default; wall 156 s
at radices 2..5 (56 s at 2..3). Prints reproduced by:
python prime/code/explore_onestream_delay.py [BMAX]
"""

import cmath
import itertools
import math
import sys
import time
from fractions import Fraction as Fr

import explore_sqrt_delay as sq

FAILURES = []
SCAN_KILL = 1_000_000     # prefixes scanned per pair at L* - 1 (the excess region)
SCAN_SURV = 300_000       # at L*
TREE_CERT = 200_000       # tree node budget at L* - 1
TREE_SURV = 50_000        # at L*
PHASE_MIN = 10_000        # the half-excess count P-F reads the phases at
HMAX = 1 << 18            # the Erdos-Turan harmonic cap in the N_0 search


def _psums():
    """Cumulative sums of h^(-1/2), h^(-3/2), 1/h for h <= HMAX, index H."""
    out = ([0.0], [0.0], [0.0])
    for h in range(1, HMAX + 1):
        out[0].append(out[0][-1] + h ** -0.5)
        out[1].append(out[1][-1] + h ** -1.5)
        out[2].append(out[2][-1] + 1 / h)
    return out


PSUMS = _psums()


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


# ------------------------------------------------------------ the maps
# A map exposes: cmp(C, T, X, N) = sign of C/T - f(X/N) exactly on
# integers; approx(X, N) a float; increasing; fits(b, Mm, Mp, o) the
# range inside the root cell at lead o; law_ok(b, rho, wsum, L) the
# margin law at L, exactly; lam(); dfabs(x), d2abs(x) at offset x from
# the pole-side corner; x_half(lam_h) the offset where |f'| = lam_h.

class Root:
    """x -> sqrt(s + x), s = S/D = M- + P."""
    increasing = True

    def __init__(self, S, D, P):
        self.S, self.D, self.P = S, D, P
        self.name = f"sqrt({S}/{D} + x)"

    def cmp(self, C, T, X, N):
        return sq.cmp_sqrt(C, T, self.S * N + self.D * X, self.D * N)

    def approx(self, X, N):
        return math.sqrt((self.S * N + self.D * X) / (self.D * N))

    def fits(self, b, Mm, Mp, o):
        return Fr(self.S, self.D) + Mp <= Mp * Mp * Fr(b) ** (2 * o)

    def law_ok(self, b, rho, wsum, L):
        return 4 * rho * rho * self.P * Fr(b) ** (2 * L) >= wsum * wsum

    def lam(self):
        return 1 / (2 * math.sqrt(self.P))

    def dfabs(self, x):
        return 1 / (2 * math.sqrt(float(self.P) + x))

    def d2abs(self, x):
        return (float(self.P) + x) ** -1.5 / 4

    def x_half(self, lam_h):
        return 1 / (4 * lam_h * lam_h) - float(self.P)


class Recip:
    """x -> 1/(s + x), s = S/D = M- + P: f(X/N) = D N / (S N + D X)."""
    increasing = False

    def __init__(self, S, D, P):
        self.S, self.D, self.P = S, D, P
        self.name = f"1/({S}/{D} + x)"

    def cmp(self, C, T, X, N):
        den = self.S * N + self.D * X                    # > 0 on the window
        lhs, rhs = C * den, T * self.D * N
        return (lhs > rhs) - (lhs < rhs)

    def approx(self, X, N):
        return (self.D * N) / (self.S * N + self.D * X)

    def fits(self, b, Mm, Mp, o):
        return 1 / self.P <= Mp * Fr(b) ** o

    def law_ok(self, b, rho, wsum, L):
        return rho * self.P * self.P * Fr(b) ** L >= wsum

    def lam(self):
        return 1 / float(self.P) ** 2

    def dfabs(self, x):
        return 1 / (float(self.P) + x) ** 2

    def d2abs(self, x):
        return 2 / (float(self.P) + x) ** 3

    def x_half(self, lam_h):
        return lam_h ** -0.5 - float(self.P)


class Shift:
    """x -> s + x, the control: kappa = 0, the k = 1 clause its law."""
    increasing = True

    def __init__(self, S, D):
        self.S, self.D = S, D
        self.name = f"{S}/{D} + x"

    def cmp(self, C, T, X, N):
        lhs, rhs = C * self.D * N, (self.S * N + self.D * X) * T
        return (lhs > rhs) - (lhs < rhs)

    def approx(self, X, N):
        return (self.S * N + self.D * X) / (self.D * N)

    def fits(self, b, Mm, Mp, o):
        s, bo = Fr(self.S, self.D), Fr(b) ** o
        return s + Mp <= Mp * bo and s - Mm >= -Mm * bo

    def law_ok(self, b, rho, wsum, L):
        return rho * Fr(b) ** L >= wsum


def least_lead(b, am, ap, fmap):
    """Least o in Z with the range inside the root cell; None if ap = 0."""
    if ap == 0:
        return None
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    o = 0
    if fmap.fits(b, Mm, Mp, 0):
        while o > -200 and fmap.fits(b, Mm, Mp, o - 1):
            o -= 1
    else:
        while not fmap.fits(b, Mm, Mp, o):
            o += 1
    return o


def law_L(b, am, ap, fmap):
    """Least L in Z with b^L rho >= Lam (am + ap), exactly."""
    rho, wsum = am + ap + 1 - b, am + ap
    L = 0
    while not fmap.law_ok(b, rho, wsum, L):
        L += 1
    while fmap.law_ok(b, rho, wsum, L - 1):
        L -= 1
    return L


# ---------------------------------------------------------- the engine

class Reader:
    """The reading game for one stream at lookahead c in Z and lead o in Z."""

    def __init__(self, b, am, ap, c, fmap, o):
        self.b, self.am, self.ap, self.c, self.f, self.o = b, am, ap, c, fmap, o
        self.digits = list(range(-am, ap + 1))
        self.W = (am + ap) / (b - 1)

    def cell(self, q, t):
        """(C1, C2, T): the depth-t cell of prefix q is [C1/T, C2/T]."""
        b, o = self.b, self.o
        n1, n2 = (b - 1) * q - self.am, (b - 1) * q + self.ap
        if o >= 0:
            return n1 * b ** o, n2 * b ** o, (b - 1) * b ** t
        return n1, n2, (b - 1) * b ** (t - o)

    def ends(self, u, n):
        """(Xlo, Xhi, N): the box's arguments whose images are the image's
        lower and upper ends."""
        b = self.b
        X1, X2, N = (b - 1) * u - self.am, (b - 1) * u + self.ap, (b - 1) * b ** n
        return (X1, X2, N) if self.f.increasing else (X2, X1, N)

    def legal(self, u, n, q, t):
        C1, C2, T = self.cell(q, t)
        Xlo, Xhi, N = self.ends(u, n)
        return self.f.cmp(C1, T, Xlo, N) <= 0 and self.f.cmp(C2, T, Xhi, N) >= 0

    def straddles(self, u, n, t):
        """Does the image of prefix u strictly contain a depth-t zone? The
        candidate is named by a float and decided exactly with its two
        neighbours."""
        b, am, ap = self.b, self.am, self.ap
        Xlo, Xhi, N = self.ends(u, n)
        yhi = self.f.approx(Xhi, N) * float(b) ** (t - self.o)     # in units of e
        m0 = math.ceil(yhi - ap / (b - 1)) - 1
        for m in (m0 - 1, m0, m0 + 1):
            top, T = self.cell(m, t)[1], self.cell(m, t)[2]
            bot = self.cell(m + 1, t)[0]
            if self.f.cmp(top, T, Xhi, N) < 0 and self.f.cmp(bot, T, Xlo, N) > 0:
                return True
        return False

    def prefixes(self, n):
        b = self.b
        return -self.am * (b ** n - 1) // (b - 1), self.ap * (b ** n - 1) // (b - 1)

    def region_end(self, n, t, umin, umax):
        """The last prefix whose image is wider than the zone, plus two;
        widths fall away from the pole-side corner. None if none is."""
        zone = (self.W - 1) * float(self.b) ** (self.o - t)
        N = (self.b - 1) * self.b ** n

        def wide(u):
            X1, X2 = (self.b - 1) * u - self.am, (self.b - 1) * u + self.ap
            return abs(self.f.approx(X2, N) - self.f.approx(X1, N)) > zone
        if not wide(umin):
            return None
        if wide(umax):
            return umax
        lo, hi = umin, umax
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if wide(mid):
                lo = mid
            else:
                hi = mid
        return min(umax, lo + 2)

    def scan_kill(self, budget, region=False):
        """The least output depth t at which some prefix of length
        max(0, t + c) straddles a depth-t zone. Returns (t or None, n at
        the kill or the last n fully scanned, prefixes seen, the excess
        region's count at that n)."""
        t, seen, last_n, last_cnt = 0, 0, -1, 0
        while True:
            t += 1
            n = max(0, t + self.c)
            umin, umax = self.prefixes(n)
            if region:
                end = self.region_end(n, t, umin, umax)
                if end is None:
                    last_n, last_cnt = n, 0
                    continue
                umax = end
            cnt = umax - umin + 1
            if seen + cnt > budget:
                return None, last_n, seen, last_cnt
            for u in range(umin, umax + 1):
                if self.straddles(u, n, t):
                    return t, n, seen + (u - umin + 1), cnt
            seen += cnt
            last_n, last_cnt = n, cnt

    # the exhaustive tree, the check on the no-strategy step
    def survives(self, u, n, q, t, rounds):
        if rounds == 0:
            return True
        n1 = max(0, t + 1 + self.c)
        for mv in itertools.product(self.digits, repeat=n1 - n):
            u1 = u
            for x in mv:
                u1 = self.b * u1 + x
            alive = False
            for p in self.digits:
                if self.legal(u1, n1, self.b * q + p, t + 1) and \
                        self.survives(u1, n1, self.b * q + p, t + 1, rounds - 1):
                    alive = True
                    break
            if not alive:
                return False
        return True

    def certificate_depth(self, budget, max_rounds=40):
        """(the adversary's round or None, the depth searched); depth 0
        when the first round alone exceeds the budget."""
        m = len(self.digits)
        if m ** max(0, 1 + self.c) > budget:
            return None, 0
        depth = max(1, min(max_rounds, int(math.log(budget) / math.log(m)) - self.c))
        for r in range(0, depth + 1):
            if not (self.legal(0, 0, 0, 0) and self.survives(0, 0, 0, 0, r)):
                return r, depth
        return None, depth


# ------------------------------------------------- the proof's constants

def excess(b, am, ap, fmap, L):
    W = (am + ap) / (b - 1)
    return fmap.lam() * W / float(b) ** L - (W - 1)


def corner_deficit(rd, n, L):
    """Lam W / b^L minus the corner box's image width in zone units."""
    umin, _ = rd.prefixes(n)
    Xlo, Xhi, N = rd.ends(umin, n)
    w = abs(rd.f.approx(Xhi, N) - rd.f.approx(Xlo, N)) * float(rd.b) ** (n - L)
    return rd.f.lam() * rd.W / float(rd.b) ** L - w


def concavity_floor(rd, L, g, nmax=80):
    for n in range(nmax + 1):
        if corner_deficit(rd, n, L) < g:
            return n
    return None


class Region:
    """The half-excess region of a pair at L: its extent X_h', kappa,
    Delta, the count at depth n, and the proof's N_0 with its H."""

    def __init__(self, b, am, ap, fmap, L, g):
        self.b, self.am, self.ap, self.L, self.g = b, am, ap, L, g
        self.W = (am + ap) / (b - 1)
        lam = fmap.lam()
        lam_law = (self.W - 1) * float(b) ** L / self.W
        self.lam_h = (lam + lam_law) / 2
        self.X = min(fmap.x_half(self.lam_h), self.W)
        self.kappa = fmap.d2abs(self.X)                  # |f''| falls away from the corner
        self.delta = g / (2 * self.W)
        self.a = min(g / 2, 0.5)
        self.N0, self.H = self.n0()

    def count(self, n):
        top = math.floor(self.X * self.b ** n - self.W - 1e-9)
        top = min(top, (self.am + self.ap) * (self.b ** n - 1) // (self.b - 1))
        return max(0, top + 1)

    def bound(self, N, H):
        """B_H(N): the sum over h <= H in closed partial sums (PSUMS)."""
        b, L = self.b, self.L
        A = 4 * float(b) ** (L / 2) * math.sqrt((N + self.W) / (self.X * self.kappa))
        s1, s2, s3 = PSUMS[0][H], PSUMS[1][H], PSUMS[2][H]
        s = (self.delta * A * s1 + 3 * self.delta * H + 2 * A * s2 + 6 * s3) / N
        return 6 / (H + 1) + 4 / math.pi * s

    def n0(self):
        """The least N with B_H(N) < a over H; the search stops once a
        doubling of H no longer lowers it."""
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


def phases(rd, reg, n, L):
    """{z(v)} over the half-excess region at depth n, as floats."""
    umin, _ = rd.prefixes(n)
    scale = float(rd.b) ** (n - L)
    Mm = rd.am / (rd.b - 1)
    out = []
    for v in range(reg.count(n)):
        Xlo, _, N = rd.ends(umin + v, n)
        z = rd.f.approx(Xlo, N) * scale + Mm
        out.append(z - math.floor(z))
    return out


def discrepancy(xs):
    xs = sorted(xs)
    N = len(xs)
    return max(max((i + 1) / N - x, x - i / N) for i, x in enumerate(xs))


def check_arithmetic(rd, reg, L, c, label):
    """P-F: the phases at the least depth holding PHASE_MIN prefixes."""
    n = max(1, c + 1)
    while reg.count(n) < PHASE_MIN and n < 60:
        n += 1
    N = reg.count(n)
    if N < PHASE_MIN:
        return f"P-F skipped (region {N} at n={n})"
    zs = phases(rd, reg, n, L)
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
    return f"P-F n={n} N={N}: D_N={D:.3f} vs B={B:.2f}; |S_h|/vdC={','.join(f'{r:.2f}' for r in ratios)} (bound below N at {bites} of 3)"


# ------------------------------------------------------------------ runs

def one_pair(b, am, ap, P, fmap, label, arithmetic=True):
    o = least_lead(b, am, ap, fmap)
    if o is None:
        print(f"  ({b},{am},{ap}) {label}: not representable (ap = 0)")
        return None
    L = law_L(b, am, ap, fmap)
    c = L - o
    g = excess(b, am, ap, fmap, L - 1)
    rd = Reader(b, am, ap, c - 1, fmap, o)
    nconc = concavity_floor(rd, L - 1, g)
    tk, nk, seen, rcnt = rd.scan_kill(SCAN_KILL, region=True)
    rt, rdepth = rd.certificate_depth(TREE_CERT)
    rd2 = Reader(b, am, ap, c, fmap, o)
    ts, ns, _, _ = rd2.scan_kill(SCAN_SURV)
    rs, rdepth2 = rd2.certificate_depth(TREE_SURV)
    ok(ts is None, f"K2 kill at the law's L*={L} at ({b},{am},{ap}) {fmap.name} {label}: scan t={ts} n={ns}")
    ok(rs is None, f"K2 tree certifies at the law's L*={L} at ({b},{am},{ap}) {fmap.name} {label}: round {rs}")
    if tk is not None and tk <= rdepth:
        ok(rt == tk, f"K4 ({b},{am},{ap}) {label} at L*-1: scan kills at t={tk}, tree at {rt} [depth {rdepth}]")
    elif tk is not None and rt is not None:
        ok(rt == tk, f"K4 ({b},{am},{ap}) {label} at L*-1: tree certifies at round {rt} short of the scan's kill t={tk}")
    elif tk is None and rt is not None:
        ok(max(0, rt + c - 1) > nk, f"K4 ({b},{am},{ap}) {label} at L*-1: tree certifies at round {rt} inside the scan's reach n<={nk}")
    reg = Region(b, am, ap, fmap, L - 1, g)
    if tk is not None:
        ok(nk >= max(nconc if nconc is not None else 0, c), f"P-D ({b},{am},{ap}) {label}: kill at n={nk} below n_conc={nconc} or c={c}")
        before = reg.count(nk - 1) if nk - 1 >= max(1, c) else None
        if before is not None and reg.N0 is not None:
            ok(before < reg.N0, f"K5 ({b},{am},{ap}) {fmap.name} {label}: region holds {before} >= N_0={reg.N0} at n={nk - 1} with no kill")
        verdict = f"kill t={tk} n={nk} (excess region {rcnt}; half-excess {reg.count(nk)}, before {before})"
    else:
        dn = corner_deficit(rd, nk, L - 1) if nk >= 0 else float("inf")
        if dn < g / 2 and rt is None and rcnt >= 100_000:
            ok(False, f"K3 ({b},{am},{ap}) {label}: no kill in the region to n={nk} ({rcnt} prefixes) at L*-1 "
                      f"with d_n={dn:.3g} < g/2={g / 2:.3g}, tree survives {rdepth}")
            verdict = f"SURVIVES region n<={nk} ({rcnt} prefixes, d_n<g/2)"
        else:
            verdict = f"no kill in the region to n={nk} ({rcnt} prefixes; d_n={dn:.2g} vs g={g:.2g})"
    pf = check_arithmetic(rd, reg, L - 1, c - 1, f"({b},{am},{ap}) {fmap.name} {label}") if arithmetic else ""
    n0s = f"{reg.N0:.3g}" if reg.N0 is not None else "none"
    print(f"  ({b},{am},{ap}) {label}: o={o} L*={L} c*={c} | L*-1: g={g:.3f} n_conc={nconc} X_h={reg.X:.3g} "
          f"kappa={reg.kappa:.3g} N_0={n0s} [H={reg.H}] {verdict}; tree {tree_word(rt, rdepth)} | "
          f"L*: scan {'reached nothing' if ns < 0 else f'clean n<={ns}'}, tree {tree_word(rs, rdepth2)} | {pf}")
    return dict(cell=(b, am, ap), label=label, o=o, L=L, c=c, g=g, nconc=nconc, tk=tk, nk=nk, rt=rt,
                rdepth=rdepth, N0=reg.N0, rcnt=rcnt, half=reg.count(nk) if nk >= 0 else None, pf=pf,
                ns=ns, rdepth2=rdepth2)


def tree_word(r, depth):
    if depth == 0:
        return "unreached [0]"
    return f"{r if r is not None else 'survives'} [{depth}]"


def control_shift(bmax):
    tot, agree = 0, 0
    for (b, am, ap) in sq.census(bmax):
        Mm = Fr(am, b - 1)
        for s in (1, 2, 6):
            if s <= Mm:
                continue
            fmap = Shift(s, 1)
            o = least_lead(b, am, ap, fmap)
            for L in (-1, 0, 1):
                c = L - o
                pred = sq.ksum_clause_dead(1, b, am, ap, L)
                rd = Reader(b, am, ap, c, fmap, o)
                tk, nk, _, _ = rd.scan_kill(50_000)
                rt, rd_ = rd.certificate_depth(20_000)
                tot += 1
                if (tk is not None) == pred and (rt is not None) == pred and (tk is None or rt == tk):
                    agree += 1
                else:
                    ok(False, f"K1 shift ({b},{am},{ap}) s={s} o={o} L={L} c={c}: clause "
                              f"{'dead' if pred else 'alive'}, scan {tk} [n<={nk}], tree {rt} [{rd_}]")
    print(f"  shift x -> s + x, radices 2..{bmax}: {tot} cell-shift-L triples, {agree} agree with the clause")


def sqrt_pairs(bmax):
    for (b, am, ap) in sq.census(bmax):
        for j in (1, 2, 4, 8, 32, 128):
            yield b, am, ap, Fr(j, b - 1), f"P={j}/{b - 1}"
    for (b, am, ap) in ((2, 1, 1), (3, 1, 2), (3, 2, 2), (4, 2, 2), (5, 3, 3), (5, 4, 4)):
        for m in range(1, 6):
            yield b, am, ap, Fr(1, (b - 1) * b ** m), f"m={m}"


def control_oracle(bmax):
    """The square root's pairs: the general engine against explore_sqrt_delay.py."""
    tot, agree = 0, 0
    for b, am, ap, P, label in sqrt_pairs(bmax):
        if ap == 0:
            continue
        s = P + Fr(am, b - 1)
        old = sq.Root(s.numerator, s.denominator)
        o_old = sq.least_lead(b, am, ap, old)
        L_old = sq.lip_law_sqrt(b, am, ap, P.numerator, P.denominator)
        tk_old, nk_old, _, _ = sq.scan_kill(b, am, ap, L_old - o_old - 1, old, o_old, SCAN_KILL, region=True)
        new = Root(s.numerator, s.denominator, P)
        o = least_lead(b, am, ap, new)
        L = law_L(b, am, ap, new)
        tk, nk, _, _ = Reader(b, am, ap, L - o - 1, new, o).scan_kill(SCAN_KILL, region=True)
        tot += 1
        if (o, L, tk, nk) == (o_old, L_old, tk_old, nk_old):
            agree += 1
        else:
            ok(False, f"K1 oracle ({b},{am},{ap}) {label}: old (o,L,t,n)={(o_old, L_old, tk_old, nk_old)} new {(o, L, tk, nk)}")
    print(f"  the square root against explore_sqrt_delay.py: {tot} pairs, {agree} agree on (o, L*, t, n)")


def run_map(bmax, make, title):
    print(f"\n=== {title}: P = j/(b-1), radices 2..{bmax}")
    rows = []
    for (b, am, ap) in sq.census(bmax):
        prev = None
        for j in (1, 2, 4, 8, 32, 128):
            P = Fr(j, b - 1)
            r = one_pair(b, am, ap, P, make(b, am, P), f"P={j}/{b - 1}")
            if r is None:
                break
            if prev is not None:
                ok(r["L"] <= prev, f"P-B ({b},{am},{ap}): L* rises with P at j={j}")
            prev = r["L"]
            rows.append(r)
    nk = sum(1 for r in rows if r["tk"] is not None)
    print(f"  {len(rows)} pairs; certified at L*-1 at {nk}, no kill within budget at {len(rows) - nk}; "
          f"kills at n_kill - n_conc in {sorted(set(r['nk'] - (r['nconc'] or 0) for r in rows if r['tk'] is not None))}; "
          f"window kills (n=0) {sum(1 for r in rows if r['tk'] is not None and r['nk'] == 0)}")
    print(f"  lookahead c* negative at {sum(1 for r in rows if r['c'] < 0)} of {len(rows)}; "
          f"L* <= 0 at {sum(1 for r in rows if r['L'] <= 0)}; lead o <= 0 at {sum(1 for r in rows if r['o'] <= 0)}")
    print(f"  the excess region at the kill: at most {max((r['rcnt'] for r in rows if r['tk'] is not None), default=0)}; "
          f"the half-excess region at the kill: at most {max((r['half'] for r in rows if r['tk'] is not None), default=0)}; "
          f"N_0 from {min(r['N0'] for r in rows if r['N0']):.3g} to {max(r['N0'] for r in rows if r['N0']):.3g}")
    print(f"\n=== {title}: the pole arm, P = 1/((b-1) b^m), m = 1..5")
    arm = []
    for (b, am, ap) in ((2, 1, 1), (3, 1, 2), (3, 2, 2), (4, 2, 2), (5, 3, 3), (5, 4, 4)):
        Ls = []
        for m in range(1, 6):
            P = Fr(1, (b - 1) * b ** m)
            r = one_pair(b, am, ap, P, make(b, am, P), f"m={m}")
            Ls.append(r["L"])
            arm.append(r)
        print(f"  ({b},{am},{ap}) L* by m=1..5: {Ls}; steps {[Ls[i + 1] - Ls[i] for i in range(4)]}")
    nk = sum(1 for r in arm if r["tk"] is not None)
    print(f"  pole arm: {len(arm)} pairs, certified at L*-1 at {nk}; half-excess region at the kill at most "
          f"{max((r['half'] for r in arm if r['tk'] is not None), default=0)}; the L* check reached nothing "
          f"(scan and tree) at {sum(1 for r in arm if r['ns'] < 0 and r['rdepth2'] == 0)}; "
          f"the tree unreached at L*-1 at {sum(1 for r in arm if r['rdepth'] == 0)}")
    return rows + arm


def main():
    bmax = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    t0 = time.time()
    print("=== P-A (i): the shift control against the k = 1 clause")
    control_shift(bmax)
    print("=== P-A (ii): the square root's pairs, the general engine against the oracle")
    control_oracle(bmax)
    if FAILURES:
        print("\nPOSITIVE CONTROL FAILED; nothing below is read")
        for f in FAILURES:
            print("  ", f)
        return
    print(f"  controls: {time.time() - t0:.1f}s")

    def mk_root(b, am, P):
        s = P + Fr(am, b - 1)
        return Root(s.numerator, s.denominator, P)

    def mk_recip(b, am, P):
        s = P + Fr(am, b - 1)
        return Recip(s.numerator, s.denominator, P)

    print("  cell: lead o, the law's L*, lookahead c* | at L*-1: excess g, the concavity floor, the half-excess region's "
          "extent X_h, kappa, the proof's N_0, the scan's kill (t, n) with the region counts, the tree | at L* | P-F")
    root_rows = run_map(bmax, mk_root, "THE SQUARE ROOT sqrt(s + x)")
    recip_rows = run_map(bmax, mk_recip, "THE RECIPROCAL 1/(s + x)")
    both = root_rows + recip_rows
    bites = sum(1 for r in both if "bound below N at 3 of 3" in r["pf"])
    print(f"\n  P-F: {sum(1 for r in both if r['pf'].startswith('P-F n='))} pairs read, the van der Corput bound below N "
          f"for all three harmonics at {bites}")
    print(f"\nwall {time.time() - t0:.1f}s; failures: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)


if __name__ == "__main__":
    main()
