"""
poles.py -- the pole units read by the many-stream theorem, and the
law that sets their lookahead: the square root, the reciprocal and the
divider, whose lookahead can be negative.

QUESTION. manystream.py reads every C^2 map of signed-digit streams
at the least L with b^L rho >= Lam |I|, Lam the sup over the root box of
the gradient's L1 norm, L = c + o the lookahead plus the LEAD. The
literature's on-line units with a pole -- the square root sqrt(s + x), the
reciprocal 1/(s + x) and the divider x/(s + y) -- are C^2 on the
root box once the pole sits outside it. Three questions. Does the
theorem read them when the lookahead c = L - o is NEGATIVE, the
reader emitting digits before it reads one? What sets the sign of c:
the pole, the dependency structure (a stream multiplied by a function
of the others), or one number of the map? And how do the literature's
published on-line delays sit against the floors the law gives?

THE READER is manystream.py's: streams of the digits D = {-a-, ...,
a+} in radix b, SLACK rho = a- + a+ + 1 - b >= 1, M+- = a+-/(b - 1),
w = M- + M+, |I| = a- + a+; output digits weigh b^(o - t); at
lookahead c the output digit t is committed after n = max(0, t + c)
digits of every stream. The POLE DISTANCE h > 0 places the pole:
s = M- + h, so s + x runs over [h, h + w] on the root box.

THE ARGUMENT (written before this script).
  (1) EVERY L IN Z. For L < o the first o - L output digits are
      committed on the root box alone. The level-t zone has length
      (w - 1) b^(o - t) in absolute units, at least (w - 1) b^L at
      every t <= o - L, and the root box's image is at most Lam w wide,
      so under b^L rho >= Lam |I| no such digit is dead; below the law
      the kill of manystream.py's necessity argument sits at a depth
      n past which nothing changed. And a kill at a coarser level
      implies one at the next: in units of the coarser level a zone
      of length w - 1 holds a whole finer zone of length (w - 1)/b,
      spaced 1/b, whenever
      (w - 1)(b - 1) >= 1, which is rho >= 1. So the theorem holds
      as stated at every L in Z, the lookahead of either sign.
  (2) THE CLOSED FORMS. With Mh = max(M-, M+):
        sqrt(s + x): Lam = 1/(2 sqrt h), range [sqrt h, sqrt(h + w)];
        1/(s + x):   Lam = 1/h^2,        range [1/(h + w), 1/h];
        x/(s + y):   Lam = (h + Mh)/h^2, range [-M-/h, M+/h],
      each partial's modulus largest at the pole corner y = -M-, the
      divider's with |x| = Mh.
  (3) THE LEAD IS THE RANGE'S SCALE. The root tile [-M- b^o, M+ b^o]
      holds [lo, hi] iff b^o >= SIGMA = max(hi/M+, -lo/M-) (a+- >= 1),
      so o = ceil(log_b SIGMA), while L* = ceil(log_b(Lam |I| / rho)).
      Two ceilings differ by less than one more than their arguments,
      so with the RELATIVE GRADIENT Gamma = Lam / SIGMA,
          c* - log_b(Gamma |I| / rho)  lies in (-1, 1):
      THE RELATIVE-GRADIENT LAW. The map enters the lookahead through
      Gamma alone, to within one digit.
  (4) A MULTIPLIED STREAM. For f = x g(y), g > 0 on the root box with
      sup G, the x-partial is g, so Lam >= G, and the range is
      [-M- G, M+ G], so SIGMA = G and Gamma >= 1. With a+- <= b - 1,
      rho <= b - 1 and |I|/rho = 1 + (b - 1)/rho >= 2, so
      c* > log_b 2 - 1 > -1: c* >= 0. At slack 1, |I|/rho = b and
      c* >= 1. The divider has Gamma = 1 + Mh/h, so c* < 2 +
      log_b(1 + Mh/h), and c* <= 2 once Mh/h <= b - 1, which
      h >= 1/(b - 1) grants since Mh <= 1.
  (5) THE POLE UNITS RUN AHEAD. The root has Gamma =
      M+/(2 sqrt(h (h + w))) and the reciprocal Gamma = M+/h, both
      falling to 0 as h grows, so c* falls without bound: the reader
      emits ever more digits before it reads one.
  (6) THE STRUCTURE IS NOT THE VARIABLE. exp(-h y), one stream and no
      product, has Lam = h e^(h M-) and SIGMA = e^(h M-)/M+, so
      Gamma = h M+ RISES with h and c* climbs like log_b h. A stream
      multiplied by a function of the others is one way to hold Gamma
      up, not the only one.

THE DESIGN, frozen before the engine.
  THE PAIRS: the 20 cells b = 2..5, 1 <= a+- <= b - 1, rho >= 1
  (manystream.census), at h = j/(b - 1), j in {1, 2, 4, 8, 32, 128}.
  THE CLOSED FORMS against manystream.Cell's integer loops (law_L,
  lead) at every pair and unit; the root's decided by squaring.
  THE SCANS at L* and L* - 1, L* the LAW'S least L (never raised to
  the lead, unlike manystream.law_of): the reciprocal and the divider
  through manystream.scan with exact images and exact partial
  bounds; the root through a one-stream scan written here, since its
  image is irrational: the box [x0, x1] maps to
  [sqrt(s + x0), sqrt(s + x1)], only boxes with
  4 Lam_law^2 (s + x0) < 1 can kill (the excess region, rational),
  and the zone test asks for an integer strictly inside
  (sqrt(s + x0)/e + M- - 1, sqrt(s + x1)/e - M+), e = b^(L - n),
  decided by an exact floor of sqrt(A)/e plus a rational, by
  squaring. The same one-stream scan is run on the reciprocal as
  its control against manystream.scan.
  THE LAW'S BAND over six families -- sqrt(s + y), 1/(s + y),
  1/(s + y)^2, x/(s + y), exp(-h y), x exp(-h y) -- at the 20 cells
  and h = j/(b - 1), j in {1, 2, 4, 8, 32, 128, 1024, 8192}; the
  exponentials' ceilings in floating point, a pair whose argument sits
  within 1e-9 of an integer printed as a near-tie and not read.
  THE DIVIDER'S DENSE SWEEP: c* at h = j/(b - 1), j = 1..4096, and
  h = q/10, q = 1..1000, at the 20 cells, by the closed forms.
  THE LITERATURE'S TABLE: Ercegovac and Lang, Digital Arithmetic (2003),
  Table 9.1, read in the authors' own chapter 9 slides, gives the
  most-significant-first delays addition 2 (r = 2) and 1 (r >= 4),
  multiplication 3 (r = 2) and 2 (r = 4), division 4, square root 4,
  max/min 0; the slide deriving the multiplier's delay lists
  (r, redundancy factor a/(r - 1), delta) = (2, 1, 3), (4, 1, 2),
  (4, 2/3, 3). Their delta counts operand digits past the result
  digit with operands and result in one format, so it is c at o = 0.
  The product x y's c* at the three digit sets (2,1,1), (4,3,3) and
  (4,2,2) is set beside it.

PREDICTIONS.
  PA the controls, read first: the exact floor of sqrt against
     60-digit decimals at 3000 random rationals, perfect squares
     included, with no disagreement; the one-stream scan and
     manystream.scan give the reciprocal the same verdict and the same
     kill depth at every pair at L* - 1 and L*.
  PB the closed forms equal the loops at all 360 (unit, pair); the
     divider's c* is in {0, 1, 2} at every pair; the root's c* is
     negative at 65 of its 120 pairs (a transplant from the root's
     earlier census), the reciprocal's negative at some pair at every
     cell.
  PC at every (unit, pair) the scan at L* finds no kill and the scan
     at L* - 1 finds one, the negative lookaheads included; the
     deepest output depth at most 9.
  PD the band holds at every (family, cell, h).
  PE the divider: c* >= 0 at every dense pair, >= 1 at every slack-1
     cell, <= 2 at every h >= 1/(b - 1); 0 at some h at every cell of
     slack 2 or more (a transplant: the earlier sweep's zeros lay on
     exactly those ten cells).
  PF exp(-h y)'s c* at j = 8192 exceeds its j = 1 value at every cell;
     the root's and both reciprocals' sit below theirs at every cell.
  PG the product's c* is 2, 1 and 2 at (2,1,1), (4,3,3) and (4,2,2),
     one below the literature's delta at each.

KILLS, as what the script prints.
  K1 a PA line off: the comparator or the one-stream scan is wrong;
     nothing below is read.
  K2 a closed form off a loop: (2) or (3) is wrong.
  K3 a kill at L*, or a pair alive at L* - 1 whose scan ran out of
     region: the first is (1)'s sufficiency, the second necessity
     unread there.
  K4 the band broken at any read pair: (3) is wrong.
  K5 a divider c* below 0 anywhere, or below 1 at slack 1: (4) is
     wrong.
  K6 exp(-h y) not rising at some cell: (6) is wrong.

POSITIVE CONTROL: PA, read before any verdict line.

THE ESTIMATE, a second question put after the record run: is the
literature's one extra multiplier digit (PG) the price of selecting the
output digit from an ESTIMATE of the residual rather than from the
residual itself?

  THE LITERATURE'S CONDITION (Ercegovac and Lang, chapter 9 slides 43-44,
  read at source, their radix, redundancy factor, estimate width and
  delay written here b, Mh, m and L). On the symmetric set {-a, ...,
  a} in radix b, with Mh = a/(b - 1), the multiplier's scaled
  residual is bounded by om = Mh (1 - 2 Mh b^-L), and selection
  constants exist when the residual is estimated to m fractional bits
  iff  T_m(om) >= (1 + 2^-m)/2,  T_m the truncation to m fractional
  bits. The slides tabulate (b, Mh, m, L) = (2, 1, 2, 3),
  (4, 1, 2, 2) and (4, 2/3, 3, 3).
  THE ARGUMENT (written before the engine). T_m(om) <= om and
  (1 + 2^-m)/2 > 1/2, so some m works iff om > 1/2 STRICTLY: om > 1/2
  gives T_m(om) > om - 2^-m, which clears (1 + 2^-m)/2 once
  3 * 2^-m / 2 < om - 1/2. And om >= 1/2 unpacks to
  b^L (2a + 1 - b)(b - 1) >= 4a^2,  the product's law on the
  symmetric set with lead 0. So the least delay the
  condition reaches at any finite m is L* where the law holds
  strictly at L*, and L* + 1 where it holds with EQUALITY. At
  a = b - 1 equality reads b^L = 4: radix 2 at L = 2 and radix 4 at
  L = 1, two of the three published cells.

  PREDICTIONS.
  PH1 (the control) the three published rows satisfy the condition,
      and each fails at L - 1 at its own m.
  PH2 the least L over m <= 64 is L* + 1 at (2,1,1) and (4,3,3),
      where the law holds with equality at L*, and L* at (4,2,2),
      first reached at m = 4.
  PH3 over every symmetric cell of slack >= 1 at radices 2..64, the
      least L over m <= 64 is L* where the law is strict and
      L* + 1 where it is an equality; the equality cells are the two
      of PH2 (a guess, not derived for a < r - 1). The formula's L*
      equals manystream.law_of's c* at the symmetric cells of radix
      <= 5.
  KILLS, as prints.
  K7 a PH1 row off: the condition is misread from the slides; nothing
     below is read.
  K8 a cell whose least L is neither the argument's value nor
     unreached at m = 64: the argument is wrong.
  FINDINGS (entered after the run).
  - PH1 holds: the three published rows satisfy the condition at
    their L and fail at L - 1. K7 did not fire.
  - PH2 holds: om at L* is exactly 1/2 at (2,1,1) and (4,3,3), where
    the least L over every m is 3 and 2, the published values;
    at (4,2,2) om = 11/18 and L = 2 is reached at m = 4, one
    below the published 3 at m = 3.
  - PH3 holds: over the symmetric cells with a <= b - 1 of radices
    2..64 the least L is L* at every strict cell and L* + 1 at the
    equality cells, which are the two of PH2 and no others; the strict cells
    reach L* by m = 8 (m = 2 at 460 cells, 3 at 273, 4 at 138, 5 at 72,
    6 at 44, 7 at 33, 8 at 2). K8 did not fire.
    So the extra digit is the estimate's only where the law is an
    equality; elsewhere a wider estimate reaches the floor.

FINDINGS (entered after the run; every number is a print).
  - PA holds: the exact floor of sqrt agrees with 60-digit decimals
    at 3000 of 3000 rationals, and the one-stream scan with
    manystream.scan on the reciprocal at 240 of 240 (pair, L). K1 did
    not fire.
  - PB holds: the closed forms equal the loops at 360 of 360. The
    root's c* runs from -7 to 0 and is negative at 65 of 120 pairs,
    as the transplant said; the reciprocal's from -6 to 2, negative at
    40 pairs over all 20 cells; the divider's c* is 0 at 5 pairs, 1 at
    75 and 2 at 40.
  - PC holds: all 360 (unit, pair) are alive at L* and dead at
    L* - 1, the 105 negative lookaheads included, every survival at
    L* certified by the excess region running out. The kills sit at
    output depth 1 to 9 for the root (the 9 at one pair), 1 to 8 for
    the reciprocal and 1 to 8 for the divider.
  - PD holds: the band at all 960 (family, cell, h), no near-tie. The
    greatest deviations are 0.999 (the root), 0.876 and 0.893 (the
    reciprocals), 1.000 printed for the divider (a float rounding of a
    deviation under 1, which the check reads as under 1), 0.924
    (exp(-h y)) and 0.952 (x exp(-h y)).
  - PE holds: over 98620 dense pairs the divider's c* runs 0 to 4, at
    most 2 at every h >= 1/(b - 1), at least 1 at every slack-1 cell,
    and 0 somewhere at exactly the ten cells of slack 2 or more.
  - PF holds: from j = 1 to j = 8192, exp(-h y)'s c* rises by 5 to 13
    at every cell; the root's falls by 4 to 12, the reciprocal's and
    1/(s + y)^2's by 5 to 13.
  - PG holds: the product's c* is 2, 1 and 2 at (2,1,1), (4,3,3) and
    (4,2,2), each dead at L* - 1, against the literature's delta 3, 2 and
    3: the published multiplier sits one digit above the floor at all
    three digit sets.
  - PB's loops share each unit's Lam and range with its closed form,
    so PB checks the ceilings and the divider's lead; PC reads Lam
    against the scans.
  - The reciprocal's PC scans ran through the one-stream scan, not
    manystream.scan as the design says. PA shows that the two agree
    at exactly those 240 (pair, L).
  - One change after the first run, no verdict touched. The divider's
    scan at L* - 1 as frozen (manystream.scan over both streams) ran
    out of budget at (2,1,1), h = 128, where the excess is 0.008 of a
    zone. Given more budget it found the kill at output depth 7 but
    passed the 512 MB ceiling. Below the law the divider is now
    searched on the edge |x| = Mh alone (edge_scan): a search for a
    witness, which can only find a kill. Survival at L* is still read
    by the full scan, whose region is empty at the root box.

RUN RECORD: 21/21 checks, 2.1 s, peak commit 14.4 MB under a memory guard;
after an audit (survival at L* read only where the excess region ran
out, PG's kills asserted), 21/21, 2.0 s, 13.8 MB.
"""

import math
import random
import time
from decimal import Decimal, getcontext
from fractions import Fraction as Fr

import manystream as ms

CHECKS = []
NMAX = 16
BUDGET = 300_000
JS = (1, 2, 4, 8, 32, 128)
JS_BAND = (1, 2, 4, 8, 32, 128, 1024, 8192)


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    tail = f"  ({detail})" if detail else ""
    print(f"  {'PASS' if ok else 'FAIL'}  {name}{tail}")


def least_pow(b, X):
    """The least integer k with b^k >= X, X a positive rational."""
    k = math.log(X.numerator) - math.log(X.denominator)
    k = math.floor(k / math.log(b)) - 2
    while Fr(b) ** k < X:
        k += 1
    while Fr(b) ** (k - 1) >= X:
        k -= 1
    return k


# ---- exact values: a rational, or the square root of one ----

def sqrt_ge(A, y):
    """sqrt(A) >= y, exactly."""
    return y <= 0 or y * y <= A


def vfloor(v, e, c):
    """floor(v/e + c), v = ('q', r) or ('r', A) meaning sqrt(A)."""
    kind, x = v
    if kind == "q":
        return math.floor(x / e + c)
    m = math.floor(math.sqrt(float(x)) / float(e) + float(c)) + 2
    while not sqrt_ge(x, (m - c) * e):
        m -= 1
    return m


def vgt(v, e, y):
    """v/e > y, exactly."""
    kind, x = v
    if kind == "q":
        return x / e > y
    return y * e < 0 or (y * e) ** 2 < x


def one_kills(cell, lo, hi, n, L):
    """manystream's zone test on an image [lo, hi] of exact values."""
    e = Fr(cell.b) ** (L - n)
    return vgt(hi, e, vfloor(lo, e, cell.Mm) + cell.Mp)


# ---- the units: s = M- + h ----

class Root:
    name = "sqrt(s + x)"

    def __init__(self, cell, h):
        self.c, self.h, self.s = cell, h, cell.Mm + h

    def law_L(self):
        X = Fr(self.c.I ** 2, 4 * self.c.rho ** 2) / self.h
        return -((-least_pow(self.c.b, X)) // 2)

    def lead(self):
        X = (self.h + self.c.w) / self.c.Mp ** 2
        return -((-least_pow(self.c.b, X)) // 2)

    def loops(self):
        c, L = self.c, -60
        while 4 * Fr(c.b) ** (2 * L) * c.rho ** 2 * self.h < c.I ** 2:
            L += 1
        o = -60
        while c.Mp ** 2 * Fr(c.b) ** (2 * o) < self.h + c.w:
            o += 1
        return L, o

    def image(self, x0, x1):
        return ("r", self.s + x0), ("r", self.s + x1)

    def steep(self, x0, x1, law):
        return 4 * law * law * (self.s + x0) < 1

    def gamma(self):
        h, w = float(self.h), float(self.c.w)
        return float(self.c.Mp) / (2 * math.sqrt(h * (h + w)))


class Recip:
    name = "1/(s + x)"

    def __init__(self, cell, h):
        self.c, self.h, self.s = cell, h, cell.Mm + h
        self.lam = 1 / (h * h)
        self.rng = (1 / (h + cell.w), 1 / h)

    def law_L(self):
        return least_pow(self.c.b, self.lam * self.c.I / self.c.rho)

    def lead(self):
        return least_pow(self.c.b, self.rng[1] / self.c.Mp)

    def loops(self):
        return self.c.law_L(self.lam), self.c.lead(self.rng)

    def image(self, x0, x1):
        return ("q", 1 / (self.s + x1)), ("q", 1 / (self.s + x0))

    def steep(self, x0, x1, law):
        return (self.s + x0) ** 2 * law < 1

    def gamma(self):
        return float(self.c.Mp / self.h)

    def mapping(self):
        s = self.s
        return (self.name, 1,
                lambda B: (1 / (s + B[0][1]), 1 / (s + B[0][0])),
                lambda B: [(-1 / (s + B[0][0]) ** 2,
                            -1 / (s + B[0][1]) ** 2)],
                None)


class Recip2:
    name = "1/(s + y)^2"

    def __init__(self, cell, h):
        self.c, self.h = cell, h

    def law_L(self):
        return least_pow(self.c.b, 2 / self.h ** 3
                         * self.c.I / self.c.rho)

    def lead(self):
        return least_pow(self.c.b, 1 / (self.h ** 2 * self.c.Mp))

    def gamma(self):
        return float(2 * self.c.Mp / self.h)


class Divider:
    name = "x/(s + y)"

    def __init__(self, cell, h):
        self.c, self.h, self.s = cell, h, cell.Mm + h
        self.lam = (h + cell.Mh) / (h * h)
        self.rng = (-cell.Mm / h, cell.Mp / h)

    def law_L(self):
        return least_pow(self.c.b, self.lam * self.c.I / self.c.rho)

    def lead(self):
        return least_pow(self.c.b, 1 / self.h)

    def loops(self):
        return self.c.law_L(self.lam), self.c.lead(self.rng)

    def gamma(self):
        return float(1 + self.c.Mh / self.h)

    def mapping(self):
        s = self.s

        def image(B):
            (x0, x1), (y0, y1) = B
            v = [x / (s + y) for x in (x0, x1) for y in (y0, y1)]
            return (min(v), max(v))

        def partials(B):
            (x0, x1), (y0, y1) = B
            X = max(abs(x0), abs(x1))
            return [(1 / (s + y1), 1 / (s + y0)),
                    (-X / (s + y0) ** 2, X / (s + y0) ** 2)]
        return (self.name, 2, image, partials, None)


def one_scan(cell, unit, L, o):
    """The one-stream scan: least output depth of a kill at L, or None,
    with the boxes read and whether the excess region ran out."""
    c = L - o
    law = cell.lam_law(L)
    D = range(-cell.am, cell.ap + 1)
    level, read = [0], 0
    for n in range(NMAX + 1):
        kept = []
        for u in level:
            x0, x1 = cell.box(u, n)
            read += 1
            if not unit.steep(x0, x1, law):
                continue
            lo, hi = unit.image(x0, x1)
            if n - c >= 1 and one_kills(cell, lo, hi, n, L):
                return n - c, read, False
            kept.append(u)
        if not kept:
            return None, read, True
        if read > BUDGET:
            return None, read, False
        level = [cell.b * u + e for u in kept for e in D]
    return None, read, False


def many_scan(cell, unit, L, o):
    return ms.scan(cell, unit.mapping(), L, o)


def edge_scan(cell, unit, L, o):
    """A witness search for the divider below its law: the x prefix
    held on the edge |x| = Mh, only the y prefixes branching. A kill
    found here is a kill; a survival here reads nothing."""
    _, _, image, partials, _ = unit.mapping()
    c, law = L - o, cell.lam_law(L)
    top = cell.Mp >= cell.Mm
    level, read = [0], 0
    for n in range(NMAX + 1):
        ux = ms.repunit(cell.b, n) * (cell.ap if top else -cell.am)
        kept = []
        for uy in level:
            B = [cell.box(ux, n), cell.box(uy, n)]
            read += 1
            if ms.rate(partials(B)) <= law:
                continue
            if n - c >= 1 and cell.kills(image(B), n, L):
                return n - c, read
            kept.append(uy)
        if not kept or read > BUDGET:
            return None, read
        level = [cell.b * u + e for u in kept
                 for e in range(-cell.am, cell.ap + 1)]
    return None, read


# ---- the sections ----

def pairs():
    for (b, am, ap) in ms.census():
        cell = ms.Cell(b, am, ap)
        for j in JS:
            yield cell, Fr(j, b - 1)


def section_pa():
    print("PA  the controls")
    getcontext().prec = 60
    rng = random.Random(7)
    bad = 0
    for i in range(3000):
        if i % 3 == 0:
            q = Fr(rng.randint(1, 400), rng.randint(1, 60))
            A = q * q
        else:
            A = Fr(rng.randint(1, 10 ** 6), rng.randint(1, 10 ** 4))
        e = Fr(rng.randint(1, 50), rng.randint(1, 50))
        c = Fr(rng.randint(-30, 30), rng.randint(1, 9))
        exact = vfloor(("r", A), e, c)
        z = (Decimal(A.numerator) / Decimal(A.denominator)).sqrt()
        z = z / (Decimal(e.numerator) / Decimal(e.denominator))
        z += Decimal(c.numerator) / Decimal(c.denominator)
        if exact != int(z.to_integral_value(rounding="ROUND_FLOOR")):
            bad += 1
    check("PA the exact floor of sqrt against 60-digit decimals",
          bad == 0, f"3000 rationals, {bad} off")
    off = tot = 0
    for cell, h in pairs():
        u = Recip(cell, h)
        Ls, o = u.law_L(), u.lead()
        for L in (Ls - 1, Ls):
            k1, _, _ = one_scan(cell, u, L, o)
            k2, _ = many_scan(cell, u, L, o)
            tot += 1
            off += k1 != k2
    check("PA the one-stream scan equals manystream.scan on 1/(s + x)",
          off == 0, f"{tot} (pair, L), {off} off")


def section_pb_pc():
    print("PB, PC  the three units at the 120 pairs")
    t0 = time.time()
    loops_off, neg, cstar, negcells = 0, {}, {}, {}
    alive_bad, dead_bad, depth, reads = [], [], {}, 0
    for U in (Root, Recip, Divider):
        neg[U.name], cstar[U.name], depth[U.name] = 0, {}, {}
        negcells[U.name] = set()
        for cell, h in pairs():
            u = U(cell, h)
            Ls, o = u.law_L(), u.lead()
            loops_off += (Ls, o) != u.loops()
            cs = Ls - o
            cstar[U.name][cs] = cstar[U.name].get(cs, 0) + 1
            if cs < 0:
                neg[U.name] += 1
                negcells[U.name].add((cell.b, cell.am, cell.ap))
            for L in (Ls, Ls - 1):
                if U is Divider and L < Ls:
                    k, r = edge_scan(cell, u, L, o)
                    ran_out = False
                elif U is Divider:
                    k, r = many_scan(cell, u, L, o)
                    ran_out = (k is None and r <= ms.BUDGET
                               and ms.scan.reached < ms.NMAX)
                else:
                    k, r, ran_out = one_scan(cell, u, L, o)
                reads += r
                tag = (U.name, cell.b, cell.am, cell.ap, str(h), L)
                # alive at L* only where the excess region ran out
                if L == Ls and (k is not None or not ran_out):
                    alive_bad.append(tag + (ran_out,))
                if L == Ls - 1:
                    if k is None:
                        dead_bad.append(tag + (ran_out,))
                    else:
                        depth[U.name][k] = depth[U.name].get(k, 0) + 1
        print(f"    {U.name}: c* {dict(sorted(cstar[U.name].items()))}, "
              f"negative at {neg[U.name]} pairs over "
              f"{len(negcells[U.name])} cells; kills at L* - 1 by "
              f"output depth {dict(sorted(depth[U.name].items()))}")
    check("PB the closed forms equal the loops", loops_off == 0,
          f"360 (unit, pair), {loops_off} off")
    check("PB the divider's c* in {0, 1, 2}",
          set(cstar["x/(s + y)"]) <= {0, 1, 2})
    check("PB the root negative at 65 of 120 pairs",
          neg["sqrt(s + x)"] == 65, f"read {neg['sqrt(s + x)']}")
    check("PB the reciprocal negative at every cell",
          len(negcells["1/(s + x)"]) == 20,
          f"read {len(negcells['1/(s + x)'])} cells")
    deepest = max(max(d) for d in depth.values() if d)
    check("PC alive at L*, dead at L* - 1, at every (unit, pair)",
          not alive_bad and not dead_bad,
          f"killed at L*: {alive_bad}; alive at L* - 1: {dead_bad}")
    check("PC the deepest kill at output depth <= 9", deepest <= 9,
          f"deepest {deepest}")
    print(f"    {reads} boxes read, {time.time() - t0:.1f} s")


def exp_c(cell, h, times_x):
    """c* and the band deviation of exp(-h y) (times x if asked), in
    floating point; None when a ceiling's argument is a near-tie."""
    lb = math.log(cell.b)
    Mm, Mp, Mh = float(cell.Mm), float(cell.Mp), float(cell.Mh)
    hf = float(h)
    ratio = math.log(cell.I / cell.rho)
    if times_x:
        lam = math.log(1 + Mh * hf) + hf * Mm
        sig = hf * Mm
        gam = 1 + Mh * hf
    else:
        lam = math.log(hf) + hf * Mm
        sig = hf * Mm - math.log(Mp)
        gam = hf * Mp
    X, Y = (lam + ratio) / lb, sig / lb
    if min(abs(X - round(X)), abs(Y - round(Y))) < 1e-9:
        return None
    cs = math.ceil(X) - math.ceil(Y)
    return cs, cs - math.log(gam * cell.I / cell.rho) / lb


def section_pd_pf():
    print("PD, PF  the relative-gradient law over six families")
    worst, broken, ties = {}, [], 0
    first, last = {}, {}
    fams = [Root, Recip, Recip2, Divider, "exp(-h y)", "x exp(-h y)"]
    for (b, am, ap) in ms.census():
        cell = ms.Cell(b, am, ap)
        for j in JS_BAND:
            h = Fr(j, b - 1)
            for F in fams:
                if isinstance(F, str):
                    got = exp_c(cell, h, F.startswith("x"))
                    if got is None:
                        ties += 1
                        continue
                    cs, dev = got
                    name = F
                else:
                    u = F(cell, h)
                    name = u.name
                    cs = u.law_L() - u.lead()
                    dev = cs - math.log(u.gamma() * cell.I
                                        / cell.rho) / math.log(b)
                worst[name] = max(worst.get(name, 0), abs(dev))
                if not abs(dev) < 1:
                    broken.append((name, b, am, ap, j))
                if j == JS_BAND[0]:
                    first[name, b, am, ap] = cs
                if j == JS_BAND[-1]:
                    last[name, b, am, ap] = cs
    print("    greatest |deviation|: " + ", ".join(
        f"{k} {v:.3f}" for k, v in worst.items()) + f"; near-ties {ties}")
    check("PD the band holds at every read pair", not broken,
          f"broken at {broken}")
    for name, sign in (("exp(-h y)", 1), ("sqrt(s + x)", -1),
                       ("1/(s + x)", -1), ("1/(s + y)^2", -1)):
        moves = [sign * (last[k] - first[k]) for k in first
                 if k[0] == name and k in last]
        print(f"    {name}: c* at j = 8192 less c* at j = 1 runs "
              f"{min(sign * m for m in moves)} to "
              f"{max(sign * m for m in moves)}")
        check(f"PF {name} {'rises' if sign > 0 else 'falls'} "
              f"at every cell", len(moves) == 20 and min(moves) > 0)


def section_pe():
    print("PE  the divider's dense sweep")
    t0 = time.time()
    seen, low, high, zero_cells = 0, [], [], set()
    lo_all, hi_all = 99, -99
    for (b, am, ap) in ms.census():
        cell = ms.Cell(b, am, ap)
        hs = {Fr(j, b - 1) for j in range(1, 4097)}
        hs |= {Fr(q, 10) for q in range(1, 1001)}
        for h in hs:
            u = Divider(cell, h)
            cs = u.law_L() - u.lead()
            seen += 1
            lo_all, hi_all = min(lo_all, cs), max(hi_all, cs)
            if cs < 0 or (cell.rho == 1 and cs < 1):
                low.append((b, am, ap, str(h), cs))
            if h >= Fr(1, b - 1) and cs > 2:
                high.append((b, am, ap, str(h), cs))
            if cs == 0:
                zero_cells.add((b, am, ap))
    slack2 = {(b, am, ap) for (b, am, ap) in ms.census()
              if am + ap + 1 - b >= 2}
    print(f"    {seen} pairs, c* from {lo_all} to {hi_all}; zeros at "
          f"{len(zero_cells)} cells; {time.time() - t0:.1f} s")
    check("PE c* >= 0 everywhere, >= 1 at slack 1", not low,
          f"off at {low[:5]}")
    check("PE c* <= 2 at every h >= 1/(b - 1)", not high,
          f"off at {high[:5]}")
    check("PE a zero at every cell of slack 2 or more, none at slack 1",
          zero_cells == slack2,
          f"{len(zero_cells)} cells, {len(slack2)} of slack >= 2")


def section_pg():
    print("PG  the product against the literature's multiplier delays")
    xy = ms.MAPS[2]
    got, kills = [], []
    for (b, am, ap), delta in (((2, 1, 1), 3), ((4, 3, 3), 2),
                               ((4, 2, 2), 3)):
        cell = ms.Cell(b, am, ap)
        lam, o, Ls = ms.law_of(cell, xy)
        k, _ = ms.scan(cell, xy, Ls - 1, o)
        got.append(Ls - o)
        kills.append(k)
        print(f"    ({b}, {am}, {ap}): lead {o}, L* {Ls}, c* {Ls - o}, "
              f"dead at L* - 1 at output depth {k}; the literature's delta "
              f"{delta}")
    check("PG c* = 2, 1, 2, each dead at L* - 1",
          got == [2, 1, 2] and None not in kills, f"read {got}")


def trunc(x, t):
    """x truncated to t fractional bits."""
    return Fr(math.floor(x * 2 ** t), 2 ** t)


def el_om(r, a, delta):
    p = Fr(a, r - 1)
    return p * (1 - 2 * p / Fr(r) ** delta)


def el_ok(r, a, t, delta):
    return trunc(el_om(r, a, delta), t) >= Fr(1 + Fr(1, 2 ** t), 2)


def el_least(r, a, tmax=64, dmax=40):
    """(least delta over t <= tmax, the least t reaching it)."""
    for delta in range(0, dmax):
        for t in range(1, tmax + 1):
            if el_ok(r, a, t, delta):
                return delta, t
    return None, None


def xy_law(r, a):
    """(L*, equality at L*) of r^L (2a + 1 - r)(r - 1) >= 4a^2."""
    L = 0
    while r ** L * (2 * a + 1 - r) * (r - 1) < 4 * a * a:
        L += 1
    return L, r ** L * (2 * a + 1 - r) * (r - 1) == 4 * a * a


def section_ph():
    print("PH  the literature's selection condition at an exact estimate")
    rows = ((2, 1, 2, 3), (4, 3, 2, 2), (4, 2, 3, 3))
    bad = [(r, a, t, d) for r, a, t, d in rows
           if not el_ok(r, a, t, d) or el_ok(r, a, t, d - 1)]
    check("PH1 the published rows hold at L and fail at L - 1",
          not bad, f"off at {bad}")
    for r, a, _, d in rows:
        L, eq = xy_law(r, a)
        dl, tl = el_least(r, a)
        print(f"    ({r}, {a}, {a}): om at L* {el_om(r, a, L)}, law "
              f"L* {L}{' with equality' if eq else ''}; least L "
              f"{dl} first at m = {tl}; published {d}")
    got = [el_least(r, a) for r, a, _, _ in rows]
    check("PH2 least L 3, 2, 2, the last first at m = 4",
          [g[0] for g in got] == [3, 2, 2] and got[2][1] == 4,
          f"read {got}")
    off, unreached, eqs, tneed = [], [], [], {}
    for r in range(2, 65):
        for a in range((r + 1) // 2, r):
            L, eq = xy_law(r, a)
            dl, tl = el_least(r, a)
            if dl is None:
                unreached.append((r, a))
            elif dl != L + (1 if eq else 0):
                off.append((r, a, L, eq, dl))
            if eq:
                eqs.append((r, a, L))
            if dl == L:
                tneed[tl] = tneed.get(tl, 0) + 1
    print(f"    radices 2..64: equality cells (b, a, L) {eqs}; least m reaching "
          f"L* at the strict cells {dict(sorted(tneed.items()))}; "
          f"unreached {unreached}")
    check("PH3 least L = L* strict, L* + 1 at equality", not off,
          f"off at {off[:6]}")
    lawoff = []
    for (b, am, ap) in ms.census():
        if am == ap:
            cell = ms.Cell(b, am, ap)
            lam, o, Ls = ms.law_of(cell, ms.MAPS[2])
            if Ls - o != xy_law(b, am)[0]:
                lawoff.append((b, am))
    check("PH3 the formula's L* equals manystream's c* at radix <= 5",
          not lawoff, f"off at {lawoff}")


def main():
    t0 = time.time()
    section_pa()
    if not all(CHECKS):
        print("\nCONTROL FAILED: nothing below is read.")
        raise SystemExit(1)
    section_pb_pc()
    section_pd_pf()
    section_pe()
    section_pg()
    section_ph()
    print(f"{sum(CHECKS)}/{len(CHECKS)} checks passed, "
          f"{time.time() - t0:.1f} s")
    raise SystemExit(0 if all(CHECKS) else 1)


if __name__ == "__main__":
    main()
