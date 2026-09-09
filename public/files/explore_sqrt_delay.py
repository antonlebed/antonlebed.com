"""The square root's delay: is the on-line delay of x -> sqrt(s + x) over
a signed-digit stream the Lebesgue margin in the map's derivative at
the pole-side corner, the pole's distance its only parameter, as it is
for every polynomial of degree two or more?

THE QUESTION. explore_polynomial_delay.py proves THE MARGIN LAW

    b^L rho >= Lip1 (am + ap),   L = lookahead + o,

sufficient for every continuous map of D-streams (radix b, digits
{-am..ap}, slack rho = am + ap + 1 - b >= 1, M+- = a+-/(b-1), the
window [-M-, M+], W = M- + M+), Lip1 the sup of the map's derivative
over the window in window units, and certifies it as the FLOOR for
every polynomial with a term of degree two or more, at every cell
tried. Every map so far was a polynomial. The first map with a POLE is
the square root x -> sqrt(P + M- + x) = sqrt(s + x), whose derivative
1/(2 sqrt(s + x)) is largest at the pole-side corner x = -M-, where
the radicand is the POLE DISTANCE P = s - M- > 0:

    Lip1 = 1 / (2 sqrt(P)),

so the law reads 4 b^(2L) rho^2 P >= (am + ap)^2, exact on integers
once P is rational, and its least L is L*(P): the delay rising by one
for every two digits the pole comes nearer. The question is whether
the reader dies at L* - 1 at every cell, at every P.

THE OBJECT, and two facts the hand attack found that shape the rig.

The shift s is written P + M-, P = S/D rational, "at the window's
scale": P = j/(b-1) for j >= 1 sweeps the radicand's lower end over
the digit unit (s an integer exactly when (b-1) | am + j), and
P = 1/((b-1) b^m) walks it toward the pole a digit at a time. The
range [sqrt(P), sqrt(P + W)] must fit the root cell [-M- b^o, M+ b^o],
so o is the least lead with (P + W)-bar <= M+^2 b^(2o); a cell with
ap = 0 is not representable at any lead (the root is positive).

FIRST, THE DELAY IS NEGATIVE OVER MOST OF THE SWEEP. The lead o is set
by the OUTPUT'S MAGNITUDE sqrt(s), one or more digits for every s at
or above 1, while the map's derivative is under 1/2 as soon as the
radicand clears 1, so the law's L* is 0 or negative there and the
lookahead c = L* - o is negative at every integer s of every cell:
the reader EMITS BEFORE IT READS. explore_polynomial_delay.py's
engine takes c >= 0; this engine takes c in Z, the reader's first
-c emissions read the whole window's image (the input length at
output depth t is max(0, t + c)), and the margin law covers the
negative case as written: at output depth t <= -c the zone is
(W - 1) b^(o - t) >= (W - 1) b^L, so the tightest zone is the law's.

SECOND, THE READER HAS NO STRATEGY, SO THE CERTIFICATE IS A SCAN. For
one monotone stream the image of the prefix box [x1, x2] is
[f(x1), f(x2)], an interval inside the parent cell whenever the
history was legal, so by the cell lemma the reader is dead at output
depth t iff that image STRICTLY CONTAINS a depth-t overlap zone
[(m + 1 - M-) e, (m + M+) e], e = b^o / b^t, whatever the history;
the least such t over all prefixes of length max(0, t + c) is the
adversary's certificate depth, and finding it is a linear scan of the
W b^n integer prefixes at each n rather than a (am + ap + 1)^n game
tree. The rig runs both: the scan as the criterion's instrument, the
tree (explore_polynomial_delay.py's TermGame with the image replaced
and c freed) as the check that the scan's arithmetic and the
no-strategy step agree on this map. Every test is a comparison of a
rational C/T with sqrt(A/N), decided by squaring on integers, and the
straddle test names its candidate zone by a float and decides it
exactly at the candidate and its two neighbours.

THE NECESSITY ARGUMENT'S SHAPE, and the one new step. At L = L* - 1
the law fails by the excess g = Lip1 W / b^L - (W - 1) > 0 in emitted
units. The corner box's image at depth n has width
b^n (sqrt(P + W/b^n) - sqrt(P)) / b^L, which sits BELOW Lip1 W / b^L
by the concavity deficit

    d_n = (W / b^L) (Lip1 - 1 / (sqrt(P + W/b^n) + sqrt(P))),

of order W^2 / (8 P^(3/2) b^(n+L)), and every other box is narrower
still (the derivative falls away from the pole), so NO KILL EXISTS AT
ANY DEPTH n WITH d_n >= g: the kill depth n_kill is at least
n_conc, the least n with d_n < g (property, from concavity). Past
it, the reachable lower endpoints y(u) = b^(n-L) sqrt(P + (u - u_min)/b^n)
over the range of prefixes whose box still exceeds the zone (a fixed
fraction of the window, so b^n of them) have first difference about
Lip / b^L and second difference about -1/(4 P^(3/2) b^(n+L)): the
same concavity that costs the deficit makes the phase quadratic,
and van der Corput's inequality equidistributes it modulo 1 with a
discrepancy of order b^((L-n)/2), so the dead arc of length g - d_n
is hit once b^((n-L)/2) exceeds 1/(g - d_n) by a constant. That is
the argument's shape, not a written proof; the rig prints n_kill
beside n_conc and the kill is read against the concavity floor.

THE SLATE, frozen before the engine.

P-A THE CONTROLS. (i) The squaring comparator against 60-digit decimal
    arithmetic at 3000 random rationals, perfect squares included:
    every sign agrees. (ii) The shift x -> s + x, s an integer, at
    every cell of radices 2..5 and s in {1, 2, 6} with s > M-, at
    L in {-1, 0, 1}: the scan's verdict and the tree's equal the
    k = 1 clause's (explore_polynomial_delay.py ksum_clause_dead with
    b^L a fraction): dead at -1, alive at 0 and 1, at every cell, the
    lookahead c = L - o negative throughout.
P-B THE LAW'S TABLE. L*(P) per cell for P = j/(b-1), j in
    {1, 2, 4, 8, 32, 128}: nonincreasing in j, at or below 1 at j = 1,
    negative at the large j; the lookahead c* = L* - o negative
    wherever s >= 1.
P-C SUFFICIENCY (a theorem; the rig checks its own arithmetic). At L*
    no kill at any (cell, P): the scan to its budget and the tree to
    its depth.
P-D NECESSITY. At L* - 1 the scan finds a kill at every (cell, P) of
    P-B within its budget, at n_kill >= max(n_conc, c + 1), and the
    tree certifies at the same round wherever its depth reaches the
    scan's kill.
P-E THE POLE ARM. At P = 1/((b-1) b^m), m = 1..5, at the six cells
    (2,1,1), (3,1,2), (3,2,2), (4,2,2), (5,3,3), (5,4,4): L* rises by
    one every second m (the law's own arithmetic), the reader survives
    at L* and is certified at L* - 1 at every (cell, m) the scan
    reaches; a survival to the budget with d_n still above g/2 at the
    reached depth is the budget's, printed as such.

KILLS, frozen as what this rig PRINTS.

K1 P-A prints a comparator disagreement, or a shift cell where the
   scan, the tree and the clause do not all agree -> the engine is
   wrong; nothing below is read.
K2 Any (cell, P) prints a kill at the law's L* -> the squaring tests
   are checked first; if they hold, the sufficiency proof is wrong.
K3 A (cell, P) at L* - 1 prints "no kill to depth n" with d_n < g/2
   at that n, and the tree survives to its depth -> the moonshot's
   Lipschitz line is killed at the first map with a pole: a reader
   survives below the margin off the derivative.
K4 The scan and the tree disagree at a depth both reach -> the
   no-strategy step fails for this map, or the scan's straddle
   candidate is wrong; nothing at that cell is read.

POSITIVE CONTROL: P-A whole, read before any square-root line.

THE SECOND FREEZE, written after the radix 2..3 prints and before the
radix-5 run. Radices 2..3: P-A held (27 of 27 shift triples), all 24
(cell, P) pairs certified at L* - 1 with scan and tree agreeing, none
killed at L*. The pole arm at (5,3,3), m = 5 printed K3 by its
letter: no kill to n = 8 at L* - 1 = 3 with d_8 = 0.0079 under
g/2 = 0.085, the tree surviving its 4 rounds. The hand attack named
the excess region and never counted it: a box can straddle only where
its width exceeds the zone, x < X_g = (W / (2 (W - 1) b^L))^2 - P,
and at that cell X_g is about 6e-5, so the region holds 27 prefixes
at n = 8 (measured by the bisection below) against the 5^8 the scan
spent its budget on. The
observable K3 named cannot tell the budget's survival from a
strategy's. Amended, as a property: every kill lies in the region,
so the scan at L* - 1 is restricted to it (its end found by a float
bisection on the width, widened by two prefixes) and deepened until
the REGION holds the budget's count; the tree still searches
everything, so the agreement check now also checks the property.
Prediction: the kill at (5,3,3), m = 5 appears by n = 12, and the
region-scan certifies every pair of the radix 2..5 census. K3 as
re-frozen: no kill in the region at a depth where the region holds at
least 10^5 prefixes and d_n < g/2, the tree surviving.

FINDINGS (entered post-run; every number below sits in this file's
printed output at radices 2..5).

F1 THE CONTROLS HOLD. The squaring comparator: 3000 trials, 0
   disagreements with 60-digit decimal. The shift x -> s + x: 150 of
   150 cell-shift-L triples at radices 2..5 agree with the k = 1
   clause, the scan and the tree together (dead at L = -1, alive at
   0 and 1), the lookahead c = L - o negative throughout. P-A held;
   K1 never fired.

F2 THE LAW'S TABLE. 120 (cell, P) pairs, the 20 census cells at
   P = j/(b-1), j in {1, 2, 4, 8, 32, 128}, every one representable
   at a lead o in {1, 2, 3, 4}. L* is nonincreasing in P at every
   cell; L* = 1 at j = 1 at 19 of 20 cells ((2,1,1) reads 0); L* <= 0
   at 57 of 120 and the lookahead c* = L* - o negative at 65 of 120,
   down to c* = -7 at (2,1,1), P = 128: the reader emits seven
   digits before reading one. P-B held.

F3 SUFFICIENCY'S ARITHMETIC. No kill at L* at any of the 150 pairs
   (F2's 120 and F5's 30): the scan clean to n <= 16 at radix 2, 10 at
   3, 8 at 4, 7 at 5, and the tree surviving its depth at every pair.
   K2 never fired.

F4 THE SQUARE ROOT READS AT THE MARGIN [criterion at the certified
   pairs]. At L* - 1 the region scan certifies 120 of 120: the kill
   at output depth t from 1 to 9 and input depth n from 0 to 6, at
   n_kill - n_conc in {0, 1, 2, 3, 4, 5}, never below the concavity
   floor; 30 of the 120 kills are the WINDOW ITSELF (n = 0, the
   reader dead before reading a digit, at lookaheads c* - 1 <= -1);
   the excess region holds at most 341 prefixes at the kill ((4,3,1),
   P = 8/3) and the region's count at the kill, not its depth, is
   what the law's excess sets. The tree agrees with the scan's round
   at all 120 (its depth reaches every kill); K3 and K4 never fired.

F5 THE POLE ARM. 30 pairs, all certified at L* - 1 inside regions of
   at most 127 prefixes and surviving at L*; L* by m = 1..5 reads
   [1,1,2,2,3] at (2,1,1), [2,2,3,3,4] at (3,1,2), (4,2,2) and
   (5,3,3), [1,2,2,3,3] at (3,2,2) and (5,4,4): one more lookahead
   for every two digits the pole comes nearer, the law's own
   arithmetic. THE KILL IS SELF-SIMILAR IN THE POLE'S DEPTH: at
   (5,3,3) the pairs m = 1, 3, 5 share g = 0.171 and n_conc = 2, 4, 6,
   and kill at n = 5, 7, 9 inside a region of 127 prefixes each time;
   at (3,1,2) m = 1, 3, 5 kill at n = 5, 7, 9 in a region of 22. The
   tree's depth falls short of the kill at 4 of the 30 (the deepest
   pairs of radices 3..5), the scan the certificate there; K4 never
   fired.
   The first freeze's K3 fired at (5,3,3), m = 5 by its letter (no
   kill to n = 8 with d_8 under g/2); the region scan finds the kill
   at n = 9 among 127 prefixes: the survival was the budget's, and
   the observable that separates the two is the region's count.

VERDICT. The first map with a pole reads at the Lebesgue margin in
its derivative at the pole-side corner, 1/(2 sqrt(P)): at every pair
tried the delay is the least L with 4 b^(2L) rho^2 P >= (am + ap)^2,
rising by one for every two digits the pole comes nearer and
NEGATIVE, the output leading the input, wherever 4 rho^2 P exceeds
(am + ap)^2. Sufficiency is the margin law's theorem; necessity is
certified pair by pair, its proof owed by the van der Corput shape
above with the region's count in place of a depth.

RUN RECORD: pure Python, integers and one float per candidate zone,
standard library; under memwatch, peak commit 8.9 MB against the
512 MB default; wall 49 s at radices 2..5 (18 s at 2..3). Prints
reproduced by: python prime/code/explore_sqrt_delay.py [BMAX]
"""

import decimal
import itertools
import math
import random
import sys
import time
from fractions import Fraction as Fr

FAILURES = []
SCAN_KILL = 1_000_000     # prefixes scanned per (cell, P) at L* - 1
SCAN_SURV = 300_000       # at L*
TREE_CERT = 200_000       # tree node budget at L* - 1
TREE_SURV = 50_000        # at L*


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


# ------------------------------------------------------------ the maps

def cmp_sqrt(C, T, A, N):
    """Sign of C/T - sqrt(A/N); T, N > 0, A >= 0, integers."""
    if C < 0:
        return -1
    if C == 0:
        return -1 if A > 0 else 0
    lhs, rhs = C * C * N, A * T * T
    return (lhs > rhs) - (lhs < rhs)


class Root:
    """x -> sqrt(S/D + x); the box end X/N is compared with C/T by squaring."""

    def __init__(self, S, D):
        self.S, self.D = S, D
        self.name = f"sqrt({S}/{D} + x)" if D != 1 else f"sqrt({S} + x)"

    def cmp(self, C, T, X, N):
        return cmp_sqrt(C, T, self.S * N + self.D * X, self.D * N)

    def approx(self, X, N):
        return math.sqrt((self.S * N + self.D * X) / (self.D * N))

    def hi(self, Mp):
        """The range's top, as a Fraction squared: (S/D + M+)."""
        return Fr(self.S, self.D) + Mp


class Shift:
    """x -> S/D + x, the control: no square root anywhere."""

    def __init__(self, S, D):
        self.S, self.D = S, D
        self.name = f"{S}/{D} + x" if D != 1 else f"{S} + x"

    def cmp(self, C, T, X, N):
        lhs, rhs = C * self.D * N, (self.S * N + self.D * X) * T
        return (lhs > rhs) - (lhs < rhs)

    def approx(self, X, N):
        return (self.S * N + self.D * X) / (self.D * N)

    def hi(self, Mp):
        return None


def least_lead(b, am, ap, fmap):
    """Least o >= 0 with the range inside the root cell [-M- b^o, M+ b^o],
    or None."""
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    if isinstance(fmap, Root):
        if ap == 0:
            return None
        top2 = fmap.hi(Mp)                  # (sqrt(s + M+))^2
        o = 0
        while top2 > Mp * Mp * b ** (2 * o):
            o += 1
        return o
    s = Fr(fmap.S, fmap.D)
    o = 0
    while s + Mp > Mp * b ** o or s - Mm < -Mm * b ** o:
        o += 1
    return o


# ---------------------------------------------------------- the engines

class RootGame:
    """The reading game at lookahead c in Z and lead o: an input prefix
    u of length n is the box [(b-1) u - am, (b-1) u + ap] / ((b-1) b^n);
    the output prefix q at depth t is the cell [(b-1) q - am, (b-1) q + ap]
    b^o / ((b-1) b^t); at output depth t the reader has read
    max(0, t + c) digits, so a negative c has it emit from the whole
    window first."""

    def __init__(self, b, am, ap, c, fmap, o):
        self.b, self.am, self.ap, self.c, self.f, self.o = b, am, ap, c, fmap, o
        self.digits = list(range(-am, ap + 1))
        self.bo = b ** o

    def legal(self, u, n, q, t):
        b, am, ap = self.b, self.am, self.ap
        N, T = (b - 1) * b ** n, (b - 1) * b ** t
        X1, X2 = (b - 1) * u - am, (b - 1) * u + ap
        C1, C2 = ((b - 1) * q - am) * self.bo, ((b - 1) * q + ap) * self.bo
        return self.f.cmp(C1, T, X1, N) <= 0 and self.f.cmp(C2, T, X2, N) >= 0

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
                q1 = self.b * q + p
                if self.legal(u1, n1, q1, t + 1) and self.survives(u1, n1, q1, t + 1, rounds - 1):
                    alive = True
                    break
            if not alive:
                return False
        return True

    def reader_survives(self, rounds):
        return self.legal(0, 0, 0, 0) and self.survives(0, 0, 0, 0, rounds)

    def certificate_depth(self, budget, max_rounds=40):
        """Least round at which the adversary wins, or None if the reader
        survives `depth` rounds, depth the largest r <= max_rounds with
        digits^(r + c) within the node budget. Returns (r or None, depth)."""
        m = len(self.digits)
        depth = max(1, min(max_rounds, int(math.log(budget) / math.log(m)) - self.c))
        for r in range(0, depth + 1):
            if not self.reader_survives(r):
                return r, depth
        return None, depth


def straddles(b, am, ap, fmap, o, u, n, t):
    """Does the image of prefix u (length n) strictly contain a depth-t
    overlap zone? The candidate zone m is the largest with
    (m + M+) e < f(x2), named by a float and decided exactly with its
    two neighbours."""
    N, T = (b - 1) * b ** n, (b - 1) * b ** t
    X1, X2 = (b - 1) * u - am, (b - 1) * u + ap
    bo = b ** o
    y2 = fmap.approx(X2, N) * b ** t / bo            # in units of e
    m0 = math.ceil(y2 - ap / (b - 1)) - 1
    for m in (m0 - 1, m0, m0 + 1):
        up = ((b - 1) * m + ap) * bo                  # zone's top, times T
        lo = ((b - 1) * (m + 1) - am) * bo            # zone's bottom, times T
        if fmap.cmp(up, T, X2, N) < 0 and fmap.cmp(lo, T, X1, N) > 0:
            return True
    return False


def region_end(b, am, ap, fmap, o, n, t, umin, umax):
    """The last prefix whose box's image is wider than the zone, plus
    two: widths fall away from the pole, so every kill lies at or
    before it. A float bisection on the width; None if no box is wide
    enough."""
    W = (am + ap) / (b - 1)
    zone = (W - 1) * b ** o / b ** t
    N = (b - 1) * b ** n

    def wide(u):
        return (fmap.approx((b - 1) * u + ap, N) - fmap.approx((b - 1) * u - am, N)) > zone
    if not wide(umin):
        return None
    lo, hi = umin, umax
    if wide(hi):
        return hi
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if wide(mid):
            lo = mid
        else:
            hi = mid
    return min(umax, lo + 2)


def scan_kill(b, am, ap, c, fmap, o, budget, region=False):
    """The criterion's instrument: the least output depth t at which
    some prefix of length max(0, t + c) straddles a depth-t zone.
    With region=True only the prefixes whose box is wider than the
    zone are scanned (every kill lies there). Returns (t or None, n at
    the kill or the last n fully scanned, prefixes scanned, the
    region's count at that n)."""
    t, seen, last_n, last_cnt = 0, 0, -1, 0
    while True:
        t += 1
        n = max(0, t + c)
        umin, umax = -am * (b ** n - 1) // (b - 1), ap * (b ** n - 1) // (b - 1)
        if region:
            end = region_end(b, am, ap, fmap, o, n, t, umin, umax)
            if end is None:
                last_n, last_cnt = n, 0
                continue
            umax = end
        cnt = umax - umin + 1
        if seen + cnt > budget:
            return None, last_n, seen, last_cnt
        for u in range(umin, umax + 1):
            if straddles(b, am, ap, fmap, o, u, n, t):
                return t, n, seen + (u - umin + 1), cnt
        seen += cnt
        last_n, last_cnt = n, cnt


# ---------------------------------------------------------- closed forms

def lip_law_sqrt(b, am, ap, S, D):
    """Least L in Z with 4 b^(2L) rho^2 (S/D) >= (am + ap)^2, the margin
    law at Lip1 = 1/(2 sqrt(P)), P = S/D."""
    rho, W = am + ap + 1 - b, am + ap
    assert rho >= 1, "the law needs slack"
    L = 0
    while Fr(4 * rho * rho * S, D) * Fr(b) ** (2 * L) < W * W:
        L += 1
    while Fr(4 * rho * rho * S, D) * Fr(b) ** (2 * (L - 1)) >= W * W:
        L -= 1
    return L


def ksum_clause_dead(k, b, am, ap, L):
    """explore_polynomial_delay.py's clause with b^L a fraction: the
    reader of a k-sum is dead at L iff an integer lies in
    ((b^L - k) M+, b^L - (b^L - k) M-)."""
    Mm, Mp, bL = Fr(am, b - 1), Fr(ap, b - 1), Fr(b) ** L
    lo, hi = (bL - k) * Mp, bL - (bL - k) * Mm
    return math.floor(lo) + 1 < hi


def excess_and_conc(b, am, ap, P, L, nmax=60):
    """g = Lip1 W / b^L - (W - 1) at L, and n_conc, the least n with the
    corner's concavity deficit d_n below g (None if past nmax)."""
    W = (am + ap) / (b - 1)
    lip = 1 / (2 * math.sqrt(P))
    g = lip * W / b ** L - (W - 1)
    for n in range(nmax + 1):
        d = (W / b ** L) * (lip - 1 / (math.sqrt(P + W / b ** n) + math.sqrt(P)))
        if d < g:
            return g, n, d
    return g, None, None


def deficit(b, am, ap, P, L, n):
    W = (am + ap) / (b - 1)
    lip = 1 / (2 * math.sqrt(P))
    return (W / b ** L) * (lip - 1 / (math.sqrt(P + W / b ** n) + math.sqrt(P)))


def census(bmax):
    return [(b, am, ap) for b in range(2, bmax + 1)
            for am in range(0, b) for ap in range(0, b)
            if am + ap + 1 - b >= 1]


# ------------------------------------------------------------------ runs

def one_cell(b, am, ap, S, D, label):
    """At P = S/D: the law's L*, the lead, the scan and the tree at
    L* - 1 and at L*. Returns a dict of the prints."""
    P = Fr(S, D)
    s = P + Fr(am, b - 1)
    fmap = Root(s.numerator, s.denominator)
    o = least_lead(b, am, ap, fmap)
    if o is None:
        print(f"  ({b},{am},{ap}) {label}: not representable (ap = 0)")
        return None
    L = lip_law_sqrt(b, am, ap, S, D)
    c = L - o
    # necessity at L* - 1
    g, nconc, _ = excess_and_conc(b, am, ap, float(P), L - 1)
    tk, nk, seen, rcnt = scan_kill(b, am, ap, c - 1, fmap, o, SCAN_KILL, region=True)
    game = RootGame(b, am, ap, c - 1, fmap, o)
    rt, rdepth = game.certificate_depth(TREE_CERT)
    # sufficiency at L*
    ts, ns, _, _ = scan_kill(b, am, ap, c, fmap, o, SCAN_SURV)
    game2 = RootGame(b, am, ap, c, fmap, o)
    rs, rdepth2 = game2.certificate_depth(TREE_SURV)
    ok(ts is None, f"K2 kill at the law's L*={L} at ({b},{am},{ap}) {label}: scan t={ts} n={ns}")
    ok(rs is None, f"K2 tree certifies at the law's L*={L} at ({b},{am},{ap}) {label}: round {rs}")
    # scan against tree at L* - 1
    if tk is not None and tk <= rdepth:
        ok(rt == tk, f"K4 ({b},{am},{ap}) {label} at L*-1: scan kills at t={tk}, tree at {rt} [depth {rdepth}]")
    elif tk is not None and rt is not None:
        ok(rt == tk, f"K4 ({b},{am},{ap}) {label} at L*-1: tree certifies at round {rt} short of the scan's kill t={tk}")
    elif tk is None and rt is not None:
        ok(max(0, rt + c - 1) > nk, f"K4 ({b},{am},{ap}) {label} at L*-1: tree certifies at round {rt} "
                                    f"(n={max(0, rt + c - 1)}) inside the scan's reach n<={nk}")
    if tk is not None:
        ok(nk >= max(nconc if nconc is not None else 0, c), f"P-D ({b},{am},{ap}) {label}: kill at n={nk} "
                                                              f"below the concavity floor n_conc={nconc} or c={c}")
        verdict = f"kill t={tk} n={nk} (region {rcnt})"
    else:
        dn = deficit(b, am, ap, float(P), L - 1, nk) if nk >= 0 else float("inf")
        if dn < g / 2 and rt is None and rcnt >= 100_000:
            ok(False, f"K3 ({b},{am},{ap}) {label}: no kill in the region to n={nk} ({rcnt} prefixes) at L*-1 "
                      f"with d_n={dn:.3g} < g/2={g/2:.3g}, tree survives {rdepth}")
            verdict = f"SURVIVES region n<={nk} ({rcnt} prefixes, d_n<g/2)"
        else:
            verdict = f"no kill in the region to n={nk} ({rcnt} prefixes; d_n={dn:.2g} vs g={g:.2g})"
    print(f"  ({b},{am},{ap}) {label}: o={o} L*={L} c*={c} | L*-1: g={g:.3f} n_conc={nconc} "
          f"{verdict}; tree {rt if rt is not None else 'survives'} [{rdepth}] | "
          f"L*: scan clean n<={ns}, tree survives [{rdepth2}]")
    return dict(cell=(b, am, ap), label=label, o=o, L=L, c=c, g=g, nconc=nconc, tk=tk, nk=nk, rt=rt, rdepth=rdepth)


def control_comparator(trials=3000):
    decimal.getcontext().prec = 60
    rng = random.Random(1212)
    bad = 0
    for i in range(trials):
        N = rng.randint(1, 10 ** rng.randint(1, 30))
        T = rng.randint(1, 10 ** rng.randint(1, 30))
        if i % 3 == 0:                       # a perfect square: C/T = sqrt(A/N) exactly
            C = rng.randint(0, 10 ** rng.randint(1, 15))
            Np = rng.randint(1, 10 ** 12)
            A, N = C * C * Np, Np * T * T
        else:
            A = rng.randint(0, 10 ** rng.randint(1, 30))
            C = rng.randint(-10 ** 5, 10 ** rng.randint(1, 30))
        got = cmp_sqrt(C, T, A, N)
        lhs = decimal.Decimal(C) / decimal.Decimal(T)
        rhs = (decimal.Decimal(A) / decimal.Decimal(N)).sqrt()
        diff = lhs - rhs
        want = 0 if abs(diff) < decimal.Decimal(10) ** -45 else (1 if diff > 0 else -1)
        if got != want:
            bad += 1
    print(f"  comparator: {trials} trials, {bad} disagreements")
    ok(bad == 0, "K1 the squaring comparator disagrees with 60-digit decimal")


def control_shift(bmax):
    tot, agree = 0, 0
    for (b, am, ap) in census(bmax):
        Mm = Fr(am, b - 1)
        for s in (1, 2, 6):
            if s <= Mm:
                continue
            fmap = Shift(s, 1)
            o = least_lead(b, am, ap, fmap)
            for L in (-1, 0, 1):
                c = L - o
                pred = ksum_clause_dead(1, b, am, ap, L)
                tk, nk, _, _ = scan_kill(b, am, ap, c, fmap, o, 50_000)
                rt, rd = RootGame(b, am, ap, c, fmap, o).certificate_depth(20_000)
                tot += 1
                if (tk is not None) == pred and (rt is not None) == pred and (tk is None or rt == tk):
                    agree += 1
                else:
                    ok(False, f"K1 shift ({b},{am},{ap}) s={s} o={o} L={L} c={c}: clause "
                              f"{'dead' if pred else 'alive'}, scan {tk} [n<={nk}], tree {rt} [{rd}]")
    print(f"  shift x -> s + x, radices 2..{bmax}: {tot} cell-shift-L triples, {agree} agree with the clause")


def main():
    bmax = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    t0 = time.time()
    print("=== P-A (i): the squaring comparator against decimal")
    control_comparator()
    print("=== P-A (ii): the shift control against the k = 1 clause, c negative throughout")
    control_shift(bmax)
    if FAILURES:
        print("\nPOSITIVE CONTROL FAILED; nothing below is read")
        for f in FAILURES:
            print("  ", f)
        return

    print(f"\n=== P-B, P-C, P-D: sqrt(s + x) at P = j/(b-1), radices 2..{bmax}")
    print("  cell: lead o, the law's L*, lookahead c* = L* - o | at L*-1: excess g, the concavity floor n_conc, "
          "the scan's kill (output depth t, input depth n), the tree's round [its depth] | at L*: the scan and the tree")
    rows = []
    for (b, am, ap) in census(bmax):
        prev = None
        for j in (1, 2, 4, 8, 32, 128):
            r = one_cell(b, am, ap, j, b - 1, f"P={j}/{b-1}")
            if r is None:
                break
            if prev is not None:
                ok(r["L"] <= prev, f"P-B ({b},{am},{ap}): L* rises with P at j={j}")
            prev = r["L"]
            rows.append(r)
    nk = sum(1 for r in rows if r["tk"] is not None)
    print(f"  {len(rows)} (cell, P) pairs; certified at L*-1 at {nk}, no kill within budget at {len(rows) - nk}; "
          f"kills at n_kill - n_conc in {sorted(set(r['nk'] - (r['nconc'] or 0) for r in rows if r['tk'] is not None))}")
    neg = sum(1 for r in rows if r["c"] < 0)
    print(f"  lookahead c* negative at {neg} of {len(rows)}; L* <= 0 at {sum(1 for r in rows if r['L'] <= 0)}")

    print("\n=== P-E: the pole arm, P = 1/((b-1) b^m), m = 1..5")
    for (b, am, ap) in ((2, 1, 1), (3, 1, 2), (3, 2, 2), (4, 2, 2), (5, 3, 3), (5, 4, 4)):
        Ls = []
        for m in range(1, 6):
            r = one_cell(b, am, ap, 1, (b - 1) * b ** m, f"m={m}")
            Ls.append(r["L"])
        print(f"  ({b},{am},{ap}) L* by m=1..5: {Ls}")

    print(f"\nwall {time.time() - t0:.1f}s; failures: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)


if __name__ == "__main__":
    main()
