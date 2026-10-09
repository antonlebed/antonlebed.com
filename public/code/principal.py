"""principal.py -- where a quadratic field's first principal split prime
sits, and why principal split primes run short of their share at small p.

QUESTION. K = Q(sqrt D), D a fundamental discriminant, O its ring. An odd
prime p with chi_D(p) = +1 splits as P Pbar, and P is PRINCIPAL when
P = (alpha); over a real field "principal" means principal as an ideal
(the wide sense) unless the narrow group is named. L_1(D) is the least
odd prime p with chi_D(p) = +1 and P principal. Two questions.
  (a) How far down can L_1 sit? Over an imaginary field is there a floor
      set by |D|, and does a real field have one?
  (b) By Chebotarev in the Hilbert class field the principal split primes
      have density 1/(2h) among all primes, 1/h of the split ones. At a
      finite cut they run SHORT, the more so as h grows. What is the
      shortfall?

THE ARGUMENT (written before the engine).
  (1) THE TEST. The principal form of discriminant D is x^2 + b0 x y +
      c0 y^2, b0 = D mod 2, c0 = (b0 - D)/4, and N(x + y w) is its value
      at (x, y), w = (b0 + sqrt D)/2. A split P over p is principal iff p
      or -p is a value of it (the conjugate place is then principal too),
      iff 4p = |u^2 - D y^2| with u = 2x + b0 y. Over an imaginary field
      the form is definite and the sign is +.
  (2) THE FLOOR. Let D < 0 and P over p principal: 4p = u^2 + |D| y^2.
      y = 0 makes 4p = u^2, so p is a square, which it is not; hence
      y != 0 and 4p >= |D|. At odd D, u = b0 y = y mod 2 is odd with y,
      so 4p >= 1 + |D|. So L_1 >= |D|/4, and >= (|D| + 1)/4 at odd D.
      EQUALITY. At odd D the value at (0, 1) is c0 = (1 - D)/4 = (|D| +
      1)/4, and D = 1 - 4 c0 gives gcd(c0, D) = 1; so if c0 is an odd
      prime it is unramified, represented, hence split and principal,
      and L_1 = c0. At D = 0 mod 4 the floor |D|/4 divides D, so a prime
      there is ramified and never counted, and 4p = |D| is impossible for
      a split p; the floor is not attained. Conversely L_1 is an odd
      prime, so L_1 = (|D| + 1)/4 needs that value to be one. So L_1
      MEETS THE FLOOR EXACTLY WHEN D IS ODD AND (|D| + 1)/4 IS AN ODD
      PRIME. The floor never consults h.
      COROLLARY. No imaginary field with |D| > 4B has L_1 <= B.
  (3) NO FLOOR OVER A REAL FIELD. Take D = m^2 - 12 or m^2 + 12 with m
      odd and 3 not dividing m. Then D = 1 mod 4 (m^2 = 1 mod 8, 12 = 4
      mod 8, so D = 5 mod 8 either way), and with w = (1 + sqrt D)/2 and
      x = (m - 1)/2, N(x + w) = x^2 + x - (D - 1)/4 = (m^2 - D)/4 = +-3.
      D = m^2 mod 3 is a nonzero square, so chi_D(3) = +1, and x + w
      generates a place over 3. So L_1(D) = 3 whenever such a D is
      fundamental, that is squarefree; m^2 -+ 12 is an irreducible
      quadratic in m, so its squarefree values are infinite in number
      (Estermann 1931), and L_1 = 3 at unboundedly large D.
      [CORRECTION, made at the audit and left in place because the
      slate is a frozen record: Estermann 1931 is the case z^2 + k. With
      m = 6n +- 1 the family is an irreducible quadratic in n with no
      fixed square divisor, and its squarefree values have positive
      density by Ricci, Rend. Circ. Mat. Palermo 57 (1933).] A floor in
      terms of D is impossible, and the reason is (1)'s sign: an
      indefinite form takes small values far out.
  (4) THE SHORTFALL (the explicit formula, known in shape). Chebotarev in
      the Hilbert class field H/K, whose group is Cl, is a statement about
      the count PI_C(x) of all prime-ideal POWERS P^k of K with N(P^k) < x
      and class [P^k] = C, each weighted 1/k: its main term is Li(x)/h
      for every C, and its remainder oscillates with no drift, so over a
      POPULATION of fields the level PI_C/(PI/h) averages toward 1. A
      count of degree-1 primes omits three families, and each lands on
      known classes:
        the inert prime ideals (q), norm q^2, are principal: weight 1 per
          inert q < sqrt x, ALL on the trivial class;
        the squares of split places P^2, norm p^2: weight 1/2 at 2[P] and
          2[Pbar], so on the squares 2Cl;
        the ramified prime ideals R, R^2 = (r) principal, so [R] in Cl[2].
      Higher powers are smaller still. So the degree-1 count of a class
      is short by the weight its class receives, and the three families
      give a class weight only if it is TRIVIAL, a SQUARE, or 2-TORSION.
      [CORRECTION, made at the audit, the slate left as frozen: the odd
      powers k >= 3 of split places land on k[P], any class, at weight
      1/k over p < x^(1/k). The engine counts them; "only if" holds for
      the squares and the inert and ramified primes, and G loses the
      sliver of odd-power weight.]
      A class that is none of these (a non-square outside Cl[2]) loses
      nothing and reads LONG after the renormalisation by the realised
      total. Sizes: over p < x the split places number about pi(x), so
      each class nominally holds pi(x)/h; the trivial class loses about
      pi(sqrt x)/2 inert primes plus the share |Cl[2]|/h of the
      pi(sqrt x)/2 weight of split squares, a relative deficit of
          (h + |Cl[2]|)/2 * pi(sqrt x)/pi(x),
      growing linearly in h. Over a real field the same holds in the
      NARROW group Cl+: (q) = q O has a generator of positive norm, and
      P Pbar = (p) and R^2 = (r) likewise.
  (5) THE CLASSICAL INSTANCE. Over Q with the residue classes mod an odd
      prime q: a square l^2 < x is a quadratic residue, so the residue
      classes' prime count is short of the non-residues' by about
      pi(sqrt x)/2 and the non-residue lead, (N - R)/((N + R)/2), is
      about pi(sqrt x)/pi(x); counting prime POWERS with weight 1/k puts
      it back.
  (6) THE STATISTIC. Per field and cut, X_C is the degree-1 count (RAW)
      or PI_C (CORRECTED); the level of a set S of classes is the mean of
      X_C over S divided by the field's total over h. The total is at
      least pi(250) = 53, so the denominator never nears zero. A field's
      levels average to 1 over its h classes, so a cell is read against
      its siblings, never alone. Cells: T the trivial class; A the
      nontrivial classes of Cl[2]; S the nontrivial squares outside
      Cl[2]; G the classes in neither 2Cl nor Cl[2], which (4) says
      receive no weight. Pooled figures are the mean over fields with
      its standard error.

THE ENGINE. Classes are binary quadratic forms (a, b, c), b^2 - 4ac = D:
reduced forms over D < 0; over D > 0 the reduced forms fall into cycles
under the step rho, and a proper (narrow) class is a cycle. A place over
p at a root b of b^2 = D mod 4p is the form (p, b, (b^2 - D)/(4p)), its
conjugate (p, -b, .), and a power P^k the form (p^k, b_k, .) with b_k the
lift of b mod 4p^k. Composition is Dirichlet's; a class's square is read
by composition and checked against the power form.

PREDICTIONS, fixed before the engine.
  K  CONTROLS, read before anything else.
     K1 h(D) = 1, 1, 3, 5, 7, 9, 4, 4, 8 at D = -3, -4, -23, -47, -71,
        -199, -56, -84, -420, and h+(D) = 1, 1, 2, 2, 4, 3 at D = 5, 8,
        12, 40, 60, 229; nine imaginary D with h = 1 in the imaginary
        population's range.
     K2 GENUS: |Cl[2]| = 2^(t - 1) (Cl+ over a real field), t the number
        of primes dividing D, at every field of both populations.
     K3 COMPOSITION: at every field and every split p < 100, the square
        of [P] by composition equals the class of the power form P^2, and
        [P] + [Pbar] is trivial.
     K4 WEIGHTS: at every field and cut, the summed PI_C over classes
        equals the prime-power weight computed from chi_D alone.
     K5 THE TEST: over D < 0 with |D| <= 400 and p < 200, the class
        engine's "P trivial" agrees with a box search for 4p = u^2 +
        |D| y^2.
     K6 THE CLASSICAL RACE (5): over the odd primes q < 400 at x = 10^6,
        the raw non-residue lead pooled over q is positive at 3 standard
        errors or more and within a factor 2 of pi(sqrt x)/pi(x); the
        prime-power count's lead is within 2 standard errors of 0.
  F  THE FLOOR. Over every imaginary fundamental D, -20000 <= D < 0:
     L_1 >= |D|/4 at every field, and L_1 = (|D| + 1)/4 at exactly the
     odd D where that value is an odd prime; no even D meets |D|/4.
  R  NO FLOOR. Every squarefree D = m^2 +- 12 < 10^6, m odd, 3 not
     dividing m, has L_1 = 3, read off the class engine (the place over 3
     wide-principal) and off the explicit element of norm +-3.
  P  THE SHORTFALL, imaginary population: every fundamental D with
     -4000 <= D < 0 and h >= 2; cuts 250, 400, 630, 1000, 2500, 10000.
     P1 G, pooled: raw above 1 by 10 standard errors or more at every
        cut; corrected within 0.01 of 1 at 10000, and the correction
        removes at least 70% of the raw excess at every cut from 630 up.
     P2 At 10000 every (h, cell) with at least 30 fields reads,
        corrected, within 0.03 of 1 or within 3 standard errors of it.
     P3 T at 10000: the raw deficit 1 - level over the (4) prediction
        (h + |Cl[2]|)/2 * pi(sqrt x)/pi(x), pooled, lies in [0.7, 1.3].
     Real population: every fundamental D, 5 <= D <= 16000, with h+ >= 2,
     in the narrow group.
     P4 G, pooled, at 10000: corrected within 0.01 of 1 and at least 90%
        of the raw excess removed. At cuts below 10000 the real cells are
        printed with no prediction.
  THE TRANSPLANTS. P1's 70%, P2's 0.03 and P4's 90% are fixed from a
  neighbouring reading at these populations and cuts, not derived; the
  classes in G and the corrections are (4)'s.
  [SETTLED ON A LATER READ, the argument and slate above left as
  frozen. (4)'s deficit is against the Chebotarev share Li(x)/h; a
  level divides by the realised total, short of Li(x) by about
  pi(sqrt x), so T's level falls short by (4)'s deficit less
  pi(sqrt x)/pi(x), ((h + |Cl[2]|)/2 - 1) pi(sqrt x)/pi(x) to leading
  order, printed beside P3. (6)'s raw total is twice the split primes
  below the cut, about pi(cut), with no floor of 53. K3 and K5 read odd
  p. These hold by construction and are not checks: K4 (the weight sum
  grows in the same branches as the classes), F's bound and even case
  (the search hits only where |D| y^2 <= 4p with y >= 1, y = 0 never
  hitting as 4p is no square, and chi_D filters the even case), and R's
  norm +-3 and chi_D(3) (algebra). R also asserts L_1 < 10^4 over the
  real population, a check added after the slate.]
KILLS, as printed observables: any K line off (nothing below is read);
an F violation or an equality off its criterion; an R member whose place
over 3 is not wide-principal; P1's G corrected level off 1 by more than
0.01 at 10000; a P2 cell outside both bands; P3's ratio outside
[0.7, 1.3]; P4's corrected G off 1 by more than 0.01.

FINDINGS. Every prediction landed: 19/19 checks PASS at the first run,
no kill fired (17/17 since, as the RUN RECORD says).
  K  K1 all fifteen class numbers as named, h = 1 at exactly -3, -4, -7,
     -8, -11, -19, -43, -67, -163. K2 |Cl[2]| = 2^(t - 1) at all 1217
     imaginary and all 4865 real fields. K3 and K5 0 off. K6 over 77
     moduli at 10^6 the raw non-residue lead reads
     0.00180 +- 0.00031 (5.8 se) against pi(sqrt x)/pi(x) = 0.00214, and
     the prime-power lead -0.00042 +- 0.00031 (1.4 se).
  F  The floor is met at 499 of 6079 fields, every one odd with
     (|D| + 1)/4 an odd prime, 0 off. The median L_1 runs 181, 587,
     1163, 2269, 4483 over the |D| bands (0, 1000], (1000, 2500], ...,
     (10000, 20000], each inside the floor's range over its band.
  R  627 squarefree members up to 994021 (13 and 37 counted once each,
     1 + 12 = 25 - 12 and 25 + 12 = 49 - 12), each with its place over 3
     wide-principal, 0 off.
     Over all 4865 real fields to 16000, L_1 < 10000 at every one, and
     the median L_1 runs 7, 11, 11, 11, 11 over the D bands (0, 1000],
     (1000, 2500], ..., (10000, 16000]: 11 from the second band on.
  P  Imaginary, 1208 fields; G on 880:
       cut     250     400     630     1000    2500    10000
       raw     1.1862  1.1453  1.1060  1.0885  1.0567  1.0233
       corr.   1.0128  1.0018  0.9960  1.0002  1.0032  0.9991
     (se 0.0036 to 0.0005 raw), 42.7 se or more above 1 raw at every
     cut, 93% to 104% of the excess removed. At 10000 the 39 readable
     (h, cell) read 0.9715 to 1.0195 corrected, h = 4 to 28; raw T runs
     0.950 at h = 4 down to 0.748 at h = 28. T's raw deficit at 10000 is
     0.2080 against the predicted 0.2245 (ratio 0.926), and against
     (4)'s level deficit, the renormalisation taken off, 0.2041 (ratio
     1.019). At low cuts T is
     the hard zero (raw 0.097 at 250: a field's principal places start at
     |D|/4) and its corrected level there is no prediction.
     Real narrow, 4107 fields; G on 1069:
       raw     1.2103  1.1716  1.1301  1.1043  1.0590  1.0255
       corr.   1.0344  1.0241  1.0166  1.0135  1.0048  1.0009
     84% to 97% removed. The rest is not uniform: k0 reads 0.824
     corrected at 250 and 0.988 at 10000, T 1.068 and 1.005, the other
     cells within 0.035 of 1 at 250 (G 1.0344) and 0.005 at 10000.
  Tiers: (2) a theorem, the equality criterion with it; (3) a theorem,
  its infinitude by Ricci; (4) a property as to where the omitted
  weight lands, and a pattern as to the population means (imaginary
  whole, real to 84-97% with the k0 remainder left open); (5) the
  classical instance, read as the control.

RUN RECORD. 19/19, 10.1 s wall, peak working set 58.6 MB under a memory guard.
Later the checks that held by construction were cut (F's bound and even
case, R's norm and chi_D(3), the two K4 weight sums), K1 asserts the
nine h = 1 fields, R asserts L_1 < 10^4 over the real population, and
the renormalised T prediction and the G ratios are printed: 17/17,
10.2 s, peak commit 54 MB under a memory guard.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import time
from array import array
from math import isqrt
from statistics import mean, stdev

from module_law import check, section, CHECKS

RACE_X = 10 ** 6       # the classical race's cut
RACE_Q = 400           # its moduli: the odd primes below this
FLOOR_D = 20000        # the floor is read over -FLOOR_D <= D < 0
FAMILY_D = 10 ** 6     # the real family m^2 +- 12 is read below this
IMAG_D = 4000          # the imaginary population: -IMAG_D <= D < 0
REAL_D = 16000         # the real population: 5 <= D <= REAL_D
CUTS = (250, 400, 630, 1000, 2500, 10000)
TOP = CUTS[-1]
MIN_CELL = 30          # an (h, cell) is read with at least this many fields


def primes_below(n):
    s = bytearray([1]) * n
    s[0:2] = b"\x00\x00"
    for i in range(2, isqrt(n - 1) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(range(i * i, n, i)))
    return [i for i in range(n) if s[i]]


PRIMES = primes_below(RACE_X)
SMALL = [p for p in PRIMES if p < TOP]
SET_PRIMES = set(PRIMES)


def pi_below(x):
    return sum(1 for p in SMALL if p < x) if x <= TOP else \
        sum(1 for p in PRIMES if p < x)


def squarefree(n):
    n = abs(n)
    for p in PRIMES:
        if p * p > n:
            return True
        if n % (p * p) == 0:
            return False
    return True


def fundamental(D):
    if D in (0, 1):
        return False
    if D % 4 == 1:
        return squarefree(D)
    if D % 4 == 0:
        m = D // 4
        return m % 4 in (2, 3) and squarefree(m)
    return False


def omega(D):
    n, t = abs(D), 0
    for p in PRIMES:
        if p * p > n:
            break
        if n % p == 0:
            t += 1
            while n % p == 0:
                n //= p
    return t + (n > 1)


def kron(D, p):
    if p == 2:
        return 0 if D % 2 == 0 else (1 if D % 8 == 1 else -1)
    r = pow(D % p, (p - 1) // 2, p)
    return 0 if r == 0 else (1 if r == 1 else -1)


ROOT = {}
for _p in SMALL[1:]:
    _t = array("i", [-1]) * _p
    for _r in range((_p + 1) // 2):
        _t[_r * _r % _p] = _r
    ROOT[_p] = _t


def place_b(D, p):
    """b with b = D mod 2 and b^2 = D mod 4p: the place (p, b, .)."""
    if p == 2:
        return next(b for b in range(4) if (b * b - D) % 8 == 0)
    r = ROOT[p][D % p] if p in ROOT else \
        next(r for r in range(p) if (r * r - D) % p == 0)
    return r + p if (r - D) % 2 else r


def form(D, a, b):
    return (a, b, (b * b - D) // (4 * a))


# ---------------------------------------------------------------------------
# classes as forms


def xgcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def compose(f1, f2, D):
    """Dirichlet composition of two primitive forms with a > 0."""
    (a1, b1, c1), (a2, b2, c2) = f1, f2
    if a1 > a2:
        (a1, b1, c1), (a2, b2, c2) = (a2, b2, c2), (a1, b1, c1)
    s = (b1 + b2) // 2
    n = b2 - s
    if a2 % a1 == 0:
        y1, d = 0, a1
    else:
        d, y1, _ = xgcd(a2, a1)
    if s % d == 0:
        y2, x2, d1 = -1, 0, d
    else:
        d1, x2, v = xgcd(s, d)
        y2 = -v
    v1, v2 = a1 // d1, a2 // d1
    r = (y1 * y2 * n - x2 * c2) % v1
    b3 = b2 + 2 * v2 * r
    return form(D, v1 * v2, b3)


def reduce_imag(f):
    a, b, c = f
    D = b * b - 4 * a * c
    while True:
        k = (b + a - 1) // (2 * a)
        b -= 2 * a * k
        c = (b * b - D) // (4 * a)
        if a > c:
            a, b, c = c, -b, a
            continue
        if a == c and b < 0:
            b = -b
        return a, b, c


class Real:
    """Reduction and the cycle step for one D > 0."""

    def __init__(self, D):
        self.D, self.sq = D, isqrt(D)

    def reduced(self, f):
        a, b, _ = f
        s = self.sq
        return 0 < b <= s and 2 * abs(a) + b > s and 2 * abs(a) - b <= s

    def rho(self, f):
        _, b, c = f
        cc, s = abs(c), self.sq
        if cc > s:
            r = (-b) % (2 * cc)
            if r > cc:
                r -= 2 * cc
        else:
            r = s - (s + b) % (2 * cc)
        return form(self.D, c, r)

    def reduce(self, f):
        while not self.reduced(f):
            f = self.rho(f)
        return f

    def cycle(self, f):
        f = self.reduce(f)
        out = [f]
        g = self.rho(f)
        while g != f:
            out.append(g)
            g = self.rho(g)
        return out


class Group:
    """The class group of D < 0, or the narrow class group of D > 0: a
    class is an index, `of` maps a form to it, `mul` composes."""

    def __init__(self, D):
        self.D = D
        self.b0 = D % 2
        self.one_form = form(D, 1, self.b0)
        self.idx, self.rep = {}, []
        if D < 0:
            a = 1
            while 3 * a * a <= -D:
                for b in range(-a + 1, a + 1):
                    if (b * b - D) % (4 * a) == 0:
                        f = form(D, a, b)
                        if f[2] >= a and not (f[2] == a and b < 0):
                            self.idx[f] = len(self.rep)
                            self.rep.append(f)
                a += 1
            self.red = reduce_imag
        else:
            R = Real(D)
            self.red, s = R.reduce, R.sq
            for b in range(1, s + 1):
                if (b - D) % 2:
                    continue
                m = (D - b * b) // 4
                for a in range((s - b) // 2 + 1, (s + b) // 2 + 1):
                    if m % a:
                        continue
                    for f in (form(D, a, b), form(D, -a, b)):
                        if f in self.idx:
                            continue
                        cyc = R.cycle(f)
                        i = len(self.rep)
                        for g in cyc:
                            self.idx[g] = i
                        self.rep.append(next(g for g in cyc if g[0] > 0))
        self.h = len(self.rep)
        self.e = self.of(self.one_form)
        self._mul = {}
        self.dbl = [self.mul(i, i) for i in range(self.h)]
        self.two = {i for i in range(self.h) if self.dbl[i] == self.e}
        self.squares = set(self.dbl)
        self.k0 = self.of(form(D, -1, self.b0)) if D > 0 else self.e

    def of(self, f):
        return self.idx[self.red(f)]

    def mul(self, i, j):
        key = (i, j) if i <= j else (j, i)
        if key not in self._mul:
            self._mul[key] = self.of(compose(self.rep[i], self.rep[j],
                                             self.D))
        return self._mul[key]

    def inv(self, i):
        a, b, c = self.rep[i]
        return self.of((a, -b, c))

    def power(self, i, k):
        out = self.e
        for _ in range(k):
            out = self.mul(out, i)
        return out

    def place(self, p):
        return self.of(form(self.D, p, place_b(self.D, p)))


# ---------------------------------------------------------------------------
# the controls


def section_controls():
    section("K  CONTROLS")
    want = {-3: 1, -4: 1, -23: 3, -47: 5, -71: 7, -199: 9, -56: 4, -84: 4,
            -420: 8, 5: 1, 8: 1, 12: 2, 40: 2, 60: 4, 229: 3}
    got = {D: Group(D).h for D in want}
    ones = [D for D in range(-IMAG_D, 0) if fundamental(D)
            and Group(D).h == 1]
    check("K1 class numbers at fifteen named fields; h = 1 at exactly the "
          "nine imaginary D",
          got == want and ones == [-163, -67, -43, -19, -11, -8, -7, -4, -3],
          f"off: {[(D, got[D]) for D in want if got[D] != want[D]]}, "
          f"h = 1 at {ones}")

    off = 0
    for D in range(-400, 0):
        if not fundamental(D):
            continue
        G = Group(D)
        b0, c0 = D % 2, (D % 2 - D) // 4
        for p in SMALL[1:]:
            if p >= 200:
                break
            if kron(D, p) != 1:
                continue
            box = any(x * x + b0 * x * y + c0 * y * y == p
                      for x in range(-30, 31) for y in range(-30, 31))
            off += box != (G.place(p) == G.e)
    check("K5 'P trivial' agrees with a box search, |D| <= 400, odd p < 200",
          off == 0, f"{off} off")


def section_race():
    section("K6  THE CLASSICAL RACE: residues mod q against non-residues")
    x = RACE_X
    raw, cor = [], []
    for q in PRIMES[1:]:
        if q >= RACE_Q:
            break
        qr = {r * r % q for r in range(1, q)}
        N = R = 0
        Nw = Rw = 0.0
        for p in PRIMES:
            if p == q:
                continue
            if p % q in qr:
                R += 1
            else:
                N += 1
            k, pk = 2, p * p
            while pk < x:
                if pk % q in qr:
                    Rw += 1 / k
                else:
                    Nw += 1 / k
                k, pk = k + 1, pk * p
        raw.append((N - R) / ((N + R) / 2))
        cor.append((N + Nw - R - Rw) / ((N + Nw + R + Rw) / 2))
    pred = pi_below(isqrt(x) + 1) / len(PRIMES)
    mr, sr = mean(raw), stdev(raw) / len(raw) ** 0.5
    mc, sc = mean(cor), stdev(cor) / len(cor) ** 0.5
    print(f"  {len(raw)} moduli, x = {x}: raw lead {mr:.5f} +- {sr:.5f}, "
          f"prediction pi(sqrt x)/pi(x) = {pred:.5f}; prime-power lead "
          f"{mc:.5f} +- {sc:.5f}")
    check("K6 raw lead >= 3 se and within a factor 2 of the prediction",
          mr >= 3 * sr and pred / 2 <= mr <= 2 * pred)
    check("K6 the prime-power lead is within 2 se of 0", abs(mc) <= 2 * sc)


# ---------------------------------------------------------------------------
# the floor, and its absence over a real field


def least_principal_imag(D):
    """L_1 by the completed square alone, searched from p = 3 up."""
    b0, aD = D % 2, -D
    for p in PRIMES[1:]:
        y, hit = 0, False
        while aD * y * y <= 4 * p:
            t = 4 * p - aD * y * y
            u = isqrt(t)
            if u * u == t and (u - b0 * y) % 2 == 0:
                hit = True
                break
            y += 1
        if hit and kron(D, p) == 1:
            return p
    return None


def section_floor():
    section("F  THE FLOOR: L_1 >= |D|/4 over an imaginary field")
    fields = [D for D in range(-FLOOR_D, 0) if fundamental(D)]
    eq_off, tight = 0, 0
    bands = {}
    for D in fields:
        L = least_principal_imag(D)
        prime_c0 = D % 2 == 1 and (1 - D) // 4 in SET_PRIMES and \
            (1 - D) // 4 > 2
        at = 4 * L == 1 - D
        eq_off += at != prime_c0
        tight += at
        band = next(B for B in (1000, 2500, 5000, 10000, 20000) if -D <= B)
        bands.setdefault(band, []).append(L)
    check("F L_1 = (|D| + 1)/4 exactly when D is odd and it is an odd prime",
          eq_off == 0, f"{len(fields)} fields, {tight} meet the floor, "
          f"{eq_off} off")
    lo = 0
    for B, Ls in sorted(bands.items()):
        Ls.sort()
        print(f"  |D| in ({lo:5d}, {B:5d}]: {len(Ls):4d} fields, median L_1 "
              f"{Ls[len(Ls) // 2]:6d}, the floor |D|/4 runs {lo // 4} to "
              f"{B // 4}")
        lo = B


def least_principal_real(G):
    for p in SMALL[1:]:
        if kron(G.D, p) == 1 and G.place(p) in (G.e, G.k0):
            return p
    return None


def section_family():
    section("R  NO FLOOR: L_1 = 3 at every squarefree m^2 +- 12")
    n, off, top, seen = 0, 0, 0, set()
    m = -1
    while m * m - 12 < FAMILY_D:
        m += 2
        if m % 3 == 0:
            continue
        for D in (m * m - 12, m * m + 12):
            if not 0 < D < FAMILY_D or not squarefree(D) or D in seen:
                continue
            seen.add(D)
            n += 1
            top = max(top, D)
            R = Real(D)
            cyc = set(R.cycle(form(D, 3, place_b(D, 3))))
            wide = R.reduce(form(D, 1, 1)) in cyc or \
                R.reduce(form(D, -1, 1)) in cyc
            off += not wide
    check("R every member has a wide-principal place over 3",
          off == 0 and n > 0, f"{n} fundamental D up to {top}, {off} off")


# ---------------------------------------------------------------------------
# the shortfall


def bucket(n):
    """The first cut index with n below the cut, or None."""
    for j, x in enumerate(CUTS):
        if n < x:
            return j
    return None


def counts(G):
    """Per cut, the degree-1 count and the prime-power count of every
    class."""
    h, nc = G.h, len(CUTS)
    raw = [[0.0] * h for _ in range(nc)]
    ext = [[0.0] * h for _ in range(nc)]
    for p in SMALL:
        k = kron(G.D, p)
        if k == 1:
            c = G.place(p)
            cb = G.inv(c)
            j = bucket(p)
            raw[j][c] += 1
            raw[j][cb] += 1
            e, pe = 2, p * p
            while pe < TOP:
                j = bucket(pe)
                ext[j][G.power(c, e)] += 1 / e
                ext[j][G.power(cb, e)] += 1 / e
                e, pe = e + 1, pe * p
        elif k == -1:
            e, pe = 1, p * p
            while pe < TOP:
                j = bucket(pe)
                ext[j][G.e] += 1 / e
                e, pe = e + 1, pe * p * p
        else:
            r = G.place(p)
            e, pe = 1, p
            while pe < TOP:
                j = bucket(pe)
                ext[j][G.power(r, e)] += 1 / e
                e, pe = e + 1, pe * p
    for j in range(1, nc):
        for c in range(h):
            raw[j][c] += raw[j - 1][c]
            ext[j][c] += ext[j - 1][c]
    cor = [[raw[j][c] + ext[j][c] for c in range(h)] for j in range(nc)]
    return raw, cor


def cells(G):
    out = {"T": [G.e]}
    if G.D > 0 and G.k0 != G.e:
        out["K0"] = [G.k0]
    out["A"] = [c for c in G.two if c not in (G.e, G.k0)]
    out["S"] = [c for c in G.squares if c not in G.two]
    out["G"] = [c for c in range(G.h)
                if c not in G.squares and c not in G.two]
    return {k: v for k, v in out.items() if v}


def level(X, S, h):
    return sum(X[c] for c in S) / len(S) / (sum(X) / h)


def pooled(v):
    return mean(v), (stdev(v) / len(v) ** 0.5 if len(v) > 1 else 0.0)


def population(sign):
    """Every field of the population: its group, cells and levels. The
    K2 and K3 controls run field by field."""
    lo, hi = ((-IMAG_D, 0) if sign < 0 else (5, REAL_D + 1))
    rows, genus_off, comp_off, seen = [], 0, 0, 0
    for D in range(lo, hi):
        if not fundamental(D):
            continue
        G = Group(D)
        genus_off += len(G.two) != 2 ** (omega(D) - 1)
        for p in SMALL:
            if p >= 100:
                break
            if p > 2 and kron(D, p) == 1:
                b = place_b(D, p)
                b2 = next(b + 2 * p * t for t in range(p)
                          if ((b + 2 * p * t) ** 2 - D) % (4 * p * p) == 0)
                c = G.place(p)
                comp_off += G.dbl[c] != G.of(form(D, p * p, b2))
                comp_off += G.mul(c, G.inv(c)) != G.e
        seen += 1
        if G.h < 2:
            continue
        raw, cor = counts(G)
        cs = cells(G)
        rows.append({
            "D": D, "h": G.h, "two": len(G.two),
            "raw": [{k: level(raw[j], S, G.h) for k, S in cs.items()}
                    for j in range(len(CUTS))],
            "cor": [{k: level(cor[j], S, G.h) for k, S in cs.items()}
                    for j in range(len(CUTS))],
        })
    name = "imaginary" if sign < 0 else "real narrow"
    check(f"K2 genus: |Cl[2]| = 2^(t - 1) at every {name} field",
          genus_off == 0, f"{seen} fields, {genus_off} off")
    check(f"K3 [P]^2 by composition = the power form; [P][Pbar] = 1 "
          f"({name})", comp_off == 0, f"{comp_off} off")
    return rows


def table(rows, cellnames):
    print("  cut   " + "".join(f"{k:>34s}" for k in cellnames))
    for j, x in enumerate(CUTS):
        line = f"  {x:5d} "
        for k in cellnames:
            r = [row["raw"][j][k] for row in rows if k in row["raw"][j]]
            c = [row["cor"][j][k] for row in rows if k in row["cor"][j]]
            if not r:
                line += f"{'-':>34s}"
                continue
            (mr, sr), (mc, sc) = pooled(r), pooled(c)
            line += f"   {mr:.4f}+-{sr:.4f} -> {mc:.4f}+-{sc:.4f}"
        print(line)


def g_ladder(rows):
    out = []
    for j, x in enumerate(CUTS):
        r = [row["raw"][j]["G"] for row in rows if "G" in row["raw"][j]]
        c = [row["cor"][j]["G"] for row in rows if "G" in row["cor"][j]]
        (mr, sr), (mc, sc) = pooled(r), pooled(c)
        gone = (mr - mc) / (mr - 1) if mr != 1 else float("nan")
        print(f"  G at {x:5d}: raw {mr:.4f} +- {sr:.4f} ({(mr - 1) / sr:5.1f}"
              f" se), corrected {mc:.4f} +- {sc:.4f}, removed "
              f"{100 * gone:5.1f}%  ({len(r)} fields)")
        out.append((mr, sr, mc, sc, gone))
    return out


def section_imag():
    section("P  THE SHORTFALL, imaginary: RAW -> PRIME-POWER levels")
    rows = population(-1)
    print(f"  {len(rows)} fields with h >= 2, |D| <= {IMAG_D}")
    table(rows, ["T", "A", "S", "G"])
    lad = g_ladder(rows)
    check("P1 G raw above 1 by >= 10 se at every cut",
          all((mr - 1) >= 10 * sr for mr, sr, _, _, _ in lad))
    check("P1 G corrected within 0.01 of 1 at 10000",
          abs(lad[-1][2] - 1) <= 0.01, f"{lad[-1][2]:.4f}")
    check("P1 >= 70% of the raw G excess removed from cut 630 up",
          all(g >= 0.70 for _, _, _, _, g in lad[2:]))
    lo, hi = CUTS[0], TOP
    lead = [pi_below(isqrt(x) + 1) / pi_below(x) for x in (lo, hi)]
    print(f"  from cut {lo} to {hi}: G's raw excess falls by "
          f"{(lad[0][0] - 1) / (lad[-1][0] - 1):.1f}, pi(sqrt x)/pi(x) by "
          f"{lead[0] / lead[1]:.1f}, pi(x) rises by "
          f"{pi_below(hi) / pi_below(lo):.1f}")

    j = len(CUTS) - 1
    worst, read = [], 0
    print(f"  (h, cell) at {TOP}, cells with >= {MIN_CELL} fields:")
    for h in sorted({row["h"] for row in rows}):
        rs = [row for row in rows if row["h"] == h]
        for k in ("T", "A", "S", "G"):
            c = [row["cor"][j][k] for row in rs if k in row["cor"][j]]
            if len(c) < MIN_CELL:
                continue
            r = [row["raw"][j][k] for row in rs if k in row["raw"][j]]
            (mr, _), (mc, sc) = pooled(r), pooled(c)
            read += 1
            ok = abs(mc - 1) <= 0.03 or abs(mc - 1) <= 3 * sc
            if not ok:
                worst.append((h, k, round(mc, 4)))
            print(f"    h = {h:2d} {k}: n = {len(c):3d}  raw {mr:.4f}  "
                  f"corrected {mc:.4f} +- {sc:.4f}")
    check("P2 every read (h, cell) corrected within 0.03 or 3 se of 1",
          read > 0 and not worst, f"{read} cells read, off: {worst}")

    pr = pi_below(isqrt(TOP) + 1) / pi_below(TOP)
    d = [1 - row["raw"][j]["T"] for row in rows]
    pd = [(row["h"] + row["two"]) / 2 * pr for row in rows]
    ratio = mean(d) / mean(pd)
    print(f"  T at {TOP}: raw deficit {mean(d):.4f}, predicted "
          f"{mean(pd):.4f}, ratio {ratio:.3f}; corrected T "
          f"{mean(row['cor'][j]['T'] for row in rows):.4f}")
    check("P3 T's raw deficit over (h + |Cl[2]|)/2 pi(sqrt x)/pi(x) in "
          "[0.7, 1.3]", 0.7 <= ratio <= 1.3, f"{ratio:.3f}")
    pl = [((row["h"] + row["two"]) / 2 - 1) * pr for row in rows]
    print(f"  the level's prediction, renormalised by the realised total, "
          f"((h + |Cl[2]|)/2 - 1) pi(sqrt x)/pi(x): {mean(pl):.4f}, ratio "
          f"{mean(d) / mean(pl):.3f}")


def section_real():
    section("P  THE SHORTFALL, real, narrow group: RAW -> PRIME-POWER")
    rows = population(+1)
    print(f"  {len(rows)} fields with h+ >= 2, D <= {REAL_D}")
    table(rows, ["T", "K0", "A", "S", "G"])
    lad = g_ladder(rows)
    mr, _, mc, _, gone = lad[-1]
    check("P4 G corrected within 0.01 of 1 at 10000, >= 90% removed",
          abs(mc - 1) <= 0.01 and gone >= 0.90,
          f"{mc:.4f}, {100 * gone:.1f}%")

    Ls, lo = {}, 0
    for D in range(5, REAL_D + 1):
        if fundamental(D):
            band = next(B for B in (1000, 2500, 5000, 10000, 16000)
                        if D <= B)
            Ls.setdefault(band, []).append(least_principal_real(Group(D)))
    misses = 0
    for B, v in sorted(Ls.items()):
        miss = sum(1 for L in v if L is None)
        misses += miss
        v = sorted(L for L in v if L is not None)
        print(f"  real D in ({lo:5d}, {B:5d}]: {len(v) + miss:4d} fields, "
              f"median L_1 {v[len(v) // 2]:4d}, none below {TOP} at {miss}")
        lo = B
    check(f"R every real field to {REAL_D} has L_1 < {TOP}", misses == 0,
          f"{sum(len(v) for v in Ls.values())} fields, {misses} without")


def main():
    t0 = time.time()
    section_controls()
    section_race()
    section_floor()
    section_family()
    section_imag()
    section_real()
    print()
    print(f"{sum(CHECKS)}/{len(CHECKS)} checks PASS, "
          f"{time.time() - t0:.1f} s")
    if not all(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
