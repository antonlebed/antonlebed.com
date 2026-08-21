"""
explore_blind_model.py -- the blind class's order: what the divisor model
predicts, and why the census cannot see it.

THE QUESTION. The blind class at lambda = 2 is the set of primes q > 5 with
m = (q-1)/2 odd, prime to 3, and 2f + 1 composite for every divisor f of m
with 1 < f < m (explore_blind_spot_infinite.py; a divisor f with 2f + 1
prime is a BAD divisor). Equivalently: q - 1 is a multiple of p - 1 for no
prime p outside {2, 3, q}. The class is proved to number
>> x / (log x log log x) below x (the blind-share theorem,
explore_blind_share.py), and a divisor heuristic puts it at a POSITIVE
PROPORTION of the primes: the expected number of bad divisors of a typical
m is a convergent sum over m's smallest divisors, and a count with a
bounded mean is zero with positive probability. The census to 10^7 sides
with neither -- under the theorem's normalization,
N / (x / (log x log log x)), it reads FLAT (0.325, 0.319, 0.318, 0.320
across the decades from 10^4), where a positive proportion would have it
rising with log log x, by 25% across those decades. This file asks what the
heuristic, made a definite MODEL, predicts for that reading: whether the
model reproduces the census where both can be read, and what it says
beyond the census's reach.

THE MODEL (the divisor model, sieve level Z). For a divisor f of m put
n = 2f + 1 and

    rho_Z(f) = [n prime]                    if n <= Z^2 (decided exactly),
             = 0                            if some prime <= Z divides n,
             = min(1, C_Z / log n)          otherwise,

    C_Z = 1 / prod_(l <= Z) (1 - 1/l),

the probability that an integer n with no prime factor below Z is prime,
at the sieve's first order. The model's probability that m is in the class
is

    P_Z(m) = prod_(f | m, 1 < f < m) (1 - rho_Z(f)),

the bad-divisor events taken independent across divisors. The model is
exact wherever every divisor falls in the exact range, and it is the
heuristic with its constants written down: no parameter is fitted.

READING THE MODEL AT SCALES THE CENSUS CANNOT REACH. Beyond 10^7 the
model is read on RANDOM m with known factorization: Kalai's algorithm
draws a uniform integer in [1, N] together with its prime factorization
(a descending chain N >= s_1 >= s_2 >= ... with each s_(i+1) uniform in
[1, s_i], the primes among the s_i multiplied, the product accepted with
probability r/N), at a cost of order log^2 N primality tests per sample.
A shifted prime is not a uniform integer -- an odd prime p divides q - 1
with probability 1/(p-1) against the uniform 1/p, and fails to divide it
with probability (p-2)/(p-1) against (p-1)/p -- so the likelihood ratio of
the shifted-prime law to the uniform one is, up to a constant,

    w(m) = prod_(p | m) (p - 1) / (p - 2),

the Hardy-Littlewood factor of 2m + 1's primality at the primes dividing
m (p = 2 never divides an eligible m). Each sample carries w(m) as its
TILT weight, and the tilted mean is the model's reading on shifted primes.
(The rehearsal at 10^5 ran with the divisibility side alone, p/(p-1), and
read 0.03 above the census at 2.4 standard errors; the non-divisibility
side was the missing half, and the weight above is the one the full run
used.)
Samples with m even, 3 | m, or m = 1 are not eligible and are dropped.

THE TILT ALONE IS NOT ENOUGH, and the first run said so. With w(m) over
every prime factor and no further condition, 20,000 samples at 5 * 10^6
read an exact class share of 0.4539 (se 0.0035) against the census's
0.4297 -- seven standard errors high -- while every MARGINAL matched the
primes within 1%: the distributions of omega(m), of tau(m) and of the
least prime factor (a separate diagnostic over the same samples). What
differed was the share CONDITIONAL on each: at omega = 2 the primes read
0.500 and the tilted samples 0.524, at omega = 3 0.111 against 0.147. The
cause is a correlation the tilt cannot carry: for m = p r with
q = 2 p r + 1 prime, the co-divisor's 2 r + 1 and q are two linear forms
in r, and two forms are prime together more often than independence says
(the twin-prime phenomenon), the excess sitting in the small-prime
residues of 2 m + 1 -- which the model on the actual primes reads
exactly, through its sieve of 2 f + 1 by the primes up to Z, and which a
uniform m lacks. So the sampler is CONDITIONED: a sample is kept only if
2 m + 1 has no prime factor <= Z (the primes' own residue law at those
primes, which also supplies the tilt at every p <= Z), and tilted by

    w_Z(m) = prod_(p | m, p > Z) (p - 1) / (p - 2)

above Z. The unconditioned tilted reading is still printed beside it from
the same sample stream, as the contrast.

HAND-ATTACK. For a typical m the divisors below t number about
(log t)^(log 2), so the model's expected bad count
sum_(f | m) rho(f) is about the integral of d(log t)^(log 2) / log t,
which converges -- the tail beyond scale t is of order
(log t)^(log 2 - 1) = (log t)^(-0.31). So the model's class share among
eligible m should FALL at every scale, converge to a positive limit, and
approach it at the rate (log N)^(-0.31): from 10^7 to 10^100 the factor
(log N)^(-0.31) moves only from 0.42 to 0.18, so most of the remaining
descent lies BEYOND 10^7, and the census's three decades see less than
half of the model's approach. Under such an approach the theorem's
normalization, (share / 4) log log N (a quarter of the primes are
eligible: q = 3 mod 4 and q = 2 mod 3), can read flat for many decades
while the limit is positive -- the flat reading is then the model's own
prediction and decides nothing. The alternative the census could be
showing -- the order x / (log x log log x), the share falling to zero
like 1 / log log N -- is what the model excludes if its own share holds
up at 10^100.

PREDICTIONS, frozen before the engine ran (observables the rig prints;
each a kill if it fails):

  P1 (calibration). At Z = 30 the ratio of the ACTUAL class count to the
     model's predicted count, summed over the eligible m of the primes
     q <= x, lies in [0.90, 1.10] at each of x = 10^5, 10^6, 10^7, and so
     does the same ratio restricted to the 30-rough m (P^-(m) > 30).
  P2 (the tilt). At N = 5 * 10^6, Kalai samples weighted by the tilt give
     an exact class share among eligible m (2f + 1 tested by the sieve)
     within two standard errors of the census's share among eligible m
     at 10^7, and the untilted share differs from it by more than the
     tilted one does. (Frozen for the tilt alone, which MISSED it -- see
     above; re-read on the conditioned sampler, a design change after a
     failed control and not a fresh freeze.)
  P3 (the approach). The tilted model share among eligible m falls at
     every step 10^7 -> 10^10 -> 10^15 -> 10^20 -> 10^30 -> 10^50 ->
     10^100 and still exceeds 0.10 at 10^100 -- a positive proportion,
     not a share on its way to zero. (Re-read on the conditioned sampler
     to 10^50, the 10^100 scale dropped; see above.)
  P4 (the flat census is the model's). The model's reading of the
     theorem's normalization, (tilted share among eligible / 4) times
     log log N, stays within [0.20, 0.45] at every scale from 10^7 to
     10^100. (Re-read likewise, to 10^50.)

POSITIVE CONTROLS, read before any prediction.
  C1 (the model is the truth where it is exact). At Z = 1000 every divisor
     of every m below 5 * 10^5 has 2f + 1 <= Z^2, so the model's predicted
     count at 10^4 and at 10^5 equals the census's (159 and 1,133) exactly.
  C2 (the sampler). At N = 5 * 10^6 the Kalai samples' tilted exact share
     agrees with the census (P2's first clause is this control read as a
     prediction), and their tilted MODEL share (Z = 30) agrees with the
     model's share over the actual primes to 10^7 within two standard
     errors -- which is what licenses reading the sampler's model share at
     the larger N.

WHAT THE RIG MEASURES. Sieve of Eratosthenes to 10^7 (bytearray), smallest-
prime-factor table to 10^7 (array('I'), for the model's small-prime test),
largest-prime-factor table to 5 * 10^6 (the cofactors' factorization).

S1 THE CENSUS AGAINST THE MODEL. Per decade X: eligible m, class members,
   model sums at Z = 30 and Z = 1000, their ratios; the same for the
   30-rough stratum; the mean model bad count. C1 and P1 are read here.
S2 THE SAMPLER AT A CENSUSED SCALE. Kalai samples at N = 5 * 10^6 until
   8,000 conditioned ones are in hand: exact share and model share
   (Z = 30) for the tilt alone over every eligible sample and for the
   conditioned sampler, standard errors. C2 and P2 are read here.
S3 THE MODEL AT SCALE. Kalai samples at N = 10^10, 10^15, 10^20, 10^30,
   10^50 (2500, 1500, 1200, 800, 400 conditioned samples): the
   conditioned model share among eligible m, the tilt-alone share beside
   it, the 30-rough stratum's share, the mean model bad count, and
   (share / 4) log log N. P3 and P4 are read here. (The first run's
   150 samples at 10^100 carried a standard error of 0.033, too wide to
   read, and the scale is dropped.)

Run: python prime/code/explore_blind_model.py  (estimate: about twelve
minutes, the conditioning keeping three samples in ten; under 150 MB).

FINDINGS (from the printed runs: the first with the tilt alone, the
second conditioned; 166,214 eligible primes to 10^7, 71,419 in the class;
C1 and P1 pass in both, C2 fails in both -- by 7 standard errors high
and then 2.2 low -- and of the four predictions one held, one missed on
a single tick inside its noise, and two missed with the control).

F1 THE MODEL IS THE CENSUS (S1, C1, P1). On the actual primes the
   divisor model predicts the class count within 0.3% at every decade at
   Z = 30 -- the ratio actual/model reads 0.9987, 1.0029, 1.0027, 1.0016
   at 10^4..10^7 over all eligible m and 1.0000, 0.9992, 0.9989, 1.0000
   over the 30-rough ones -- and to 0.06% at Z = 1000 (1.0000, 1.0000,
   1.0000, 0.9994), exact at 10^4 and 10^5 as C1 requires. The model's
   mean bad count per eligible m rises 0.67, 0.84, 0.99, 1.09 across the
   decades: the MEAN grows, as the theorem's union bound pays for, while
   the share with none falls only 0.518, 0.473, 0.446, 0.430.

F2 THE SAMPLER (S2, C2, P2). The Hardy-Littlewood tilt alone reads the
   exact class share 0.4547 (se 0.0027) against the census's 0.4297 --
   nine standard errors high in the second run's 33,733 eligible
   samples, seven in the first's 20,000 -- with every marginal matched
   (the paragraph above). Conditioned on 2m + 1 having no prime factor
   below 30, the 8,000 samples read 0.4177 (se 0.0055), 2.2 standard
   errors LOW; the exact and the model shares agree on every sampled
   population to 0.001 (0.4547 / 0.4533, 0.4177 / 0.4186). The
   conditioning carries the co-divisor correlation and slightly over-
   corrects; what remains is of the size of the primes' own 1/log
   density against the sampler's uniform one, not run down here. The
   sampler is read below as an instrument good to 3%, and C2 and P2 are
   recorded as failed at the 2-standard-error line they were frozen at.

F3 THE MODEL AT SCALE (S3, P3, P4). The conditioned share among
   eligible m reads 0.396, 0.359, 0.336, 0.337, 0.308 at 10^10, 10^15,
   10^20, 10^30, 10^50 (se 0.009 to 0.020), the tilt-alone column beside
   it, with four times the samples, 0.420, 0.377, 0.370, 0.348, 0.324,
   falling at every step; P3 missed on the one conditioned tick
   0.3361 -> 0.3369 between 10^20 and 10^30, inside its 0.014 noise. The
   mean model bad count climbs 1.34, 1.60, 1.82, 2.06, 2.34 -- of order
   2 log log N, the divergent mean the theorem's bound pays for -- while
   the share falls by a quarter over 43 decades. The theorem's
   normalization under the model, (share / 4) log log N, reads 0.310,
   0.317, 0.322, 0.357, 0.365 (P4 held): the census's flat 0.32 is the
   model's own prediction through 10^50. Fitted by least squares against
   (log N)^(-0.31) the shares give a positive intercept, 0.18 and 0.17
   of the eligible m by the two columns, and against 1/log log N 0.16
   and 0.15 (4% of the primes either way); fitted as a pure power the
   same points read (log N)^(-0.15) and (log N)^(-0.17), a decay to
   zero. The model's own sample
   separates the two no better than the census does, and the positive
   limit rests on the typical-m argument above and nothing measured.

Run record: second run 608.3 s wall, 89.1 MB peak working set under
memwatch (first run 422.8 s, 89.4 MB); 8,000 / 2,500 / 1,500 / 1,200 /
800 / 400 conditioned samples kept of 33,733 / 10,569 / 6,470 / 5,234 /
3,527 / 1,578 eligible.
"""

import math
import random
import sys
from array import array

LIMIT = 10 ** 7
DECADES = [10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7]
RECORD = [159, 1133, 8770, 71419]   # explore_blind_spot_infinite.py, the class per decade
ROUGH = 30
Z_MAIN = 30
Z_EXACT = 1000
CONTROL_N = 5 * 10 ** 6
CONTROL_SAMPLES = 8000
SCALES = [(10 ** 10, 2500), (10 ** 15, 1500), (10 ** 20, 1200),
          (10 ** 30, 800), (10 ** 50, 400)]
SEED = 20260821

CHECKS = []


def ok(cond, msg):
    CHECKS.append(("CHECK", bool(cond), msg))
    print(("  ok   " if cond else "  FAIL ") + msg)


def predicted(cond, msg):
    CHECKS.append(("PREDICTION", bool(cond), msg))
    print(("  held " if cond else "  MISS ") + msg)


def section(t):
    print()
    print("=" * 72)
    print(t)
    print("=" * 72)


# ------------------------------------------------------------ the tables

def sieve(n):
    """bytearray s with s[k] = 1 iff k is prime, k <= n."""
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(range(i * i, n + 1, i)))
    return s


def spf_table(n, isprime):
    """SMALLEST prime factor of every k <= n (0 for k < 2): the primes
    written largest first, each smaller one overwriting."""
    t = array("I", [0]) * (n + 1)
    for i in range(n, 1, -1):
        if isprime[i]:
            t[i::i] = array("I", [i]) * len(range(i, n + 1, i))
    return t


def lpf_table(n):
    """LARGEST prime factor of every k <= n (0 for k < 2)."""
    t = array("I", [0]) * (n + 1)
    for i in range(2, n + 1):
        if t[i] == 0:
            t[i::i] = array("I", [i]) * len(range(i, n + 1, i))
    return t


def factor(m, lpf):
    """prime factorization of m as a list of (p, e), p increasing."""
    out = []
    while m > 1:
        p = lpf[m]
        e = 0
        while m % p == 0:
            m //= p
            e += 1
        out.append((p, e))
    out.reverse()
    return out


def divisors_from(fac):
    ds = [1]
    for p, e in fac:
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return ds


# ------------------------------------------------------------ the model

def small_primes(z):
    return [p for p in range(2, z + 1) if all(p % d for d in range(2, int(p ** 0.5) + 1))]


class Model:
    """rho_Z on divisors; the small-prime test by table where one is in
    range, by trial division otherwise."""

    def __init__(self, z, isprime=None, spf=None):
        self.z = z
        self.z2 = z * z
        self.primes = small_primes(z)
        self.C = 1.0
        for p in self.primes:
            self.C /= (1.0 - 1.0 / p)
        self.isprime = isprime
        self.spf = spf
        self.table_to = len(spf) - 1 if spf is not None else -1

    def rho(self, f):
        n = 2 * f + 1
        if n <= self.table_to:
            if n <= self.z2:
                return 1.0 if self.isprime[n] else 0.0
            if self.spf[n] <= self.z:
                return 0.0
        else:
            for p in self.primes:
                if n % p == 0:
                    return 1.0 if n == p else 0.0
            if n <= self.z2:
                return 1.0
        return min(1.0, self.C / math.log(n))

    def prob(self, m, divs):
        """P_Z(m) and the model's expected bad count."""
        p = 1.0
        mu = 0.0
        for f in divs:
            if 1 < f < m:
                r = self.rho(f)
                mu += r
                p *= (1.0 - r)
        return p, mu


# ------------------------------------------------------------ the sampler

MR_BASES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
TRIAL = small_primes(200)


def is_prime_big(n):
    if n < 2:
        return False
    for p in TRIAL:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in MR_BASES:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def kalai(N, rng):
    """A uniform integer in [1, N] with its factorization [(p, e)]."""
    while True:
        s = N
        primes = []
        r = 1
        while s > 1:
            s = rng.randint(1, s)
            if s > 1 and is_prime_big(s):
                primes.append(s)
                r *= s
                if r > N:
                    break
        if r <= N and rng.randrange(N) < r:
            fac = {}
            for p in primes:
                fac[p] = fac.get(p, 0) + 1
            return r, sorted(fac.items())


def tilt(fac, above=1):
    w = 1.0
    for p, _ in fac:
        if p > above:
            w *= (p - 1.0) / (p - 2.0)
    return w


def conditioned(m, primes):
    n = 2 * m + 1
    return all(n % p for p in primes)


def wmean(values, weights):
    """weighted mean and its standard error (ratio-estimator form)."""
    W = sum(weights)
    mean = sum(v * w for v, w in zip(values, weights)) / W
    n = len(values)
    var = sum((w * (v - mean)) ** 2 for v, w in zip(values, weights))
    se = math.sqrt(var * n / (n - 1)) / W if n > 1 else float("nan")
    return mean, se


def sample_scale(N, count, rng, model, exact=None):
    """Kalai samples at N until `count` conditioned ones are in hand;
    returns the per-sample records of every eligible m:
    (tilt over all p, tilt above Z, conditioned flag, model prob,
    model mean, rough flag, exact class flag or None)."""
    out = []
    have = 0
    while have < count:
        m, fac = kalai(N, rng)
        if m == 1 or m % 2 == 0 or m % 3 == 0:
            continue
        divs = divisors_from(fac)
        p, mu = model.prob(m, divs)
        rough = fac[0][0] > ROUGH
        cond = conditioned(m, model.primes)
        have += cond
        ex = None
        if exact is not None:
            ex = all(not exact[2 * f + 1] for f in divs if 1 < f < m)
        out.append((tilt(fac), tilt(fac, model.z), cond, p, mu, rough, ex))
    return out


def report(label, recs, N):
    all_w = [r[0] for r in recs]
    a_mean, a_se = wmean([r[3] for r in recs], all_w)
    crecs = [r for r in recs if r[2]]
    ws = [r[1] for r in crecs]
    c_mean, c_se = wmean([r[3] for r in crecs], ws)
    mu_c, _ = wmean([r[4] for r in crecs], ws)
    rough = [r for r in crecs if r[5]]
    if rough:
        r_mean, r_se = wmean([r[3] for r in rough], [r[1] for r in rough])
    else:
        r_mean = r_se = float("nan")
    lll = math.log(math.log(N))
    norm = c_mean / 4.0 * lll
    print("  %-8s eligible %6d  tilt alone %.4f (se %.4f) | conditioned %5d  model share %.4f (se %.4f)"
          % (label, len(recs), a_mean, a_se, len(crecs), c_mean, c_se))
    print("           conditioned: mean model bad count %.3f   30-rough share %.4f (se %.4f, n %d)"
          % (mu_c, r_mean, r_se, len(rough)))
    print("           (conditioned share / 4) log log N = %.3f   [log log N = %.3f]" % (norm, lll))
    return dict(a=a_mean, t=c_mean, t_se=c_se, mu=mu_c, rough=r_mean, norm=norm)


# ------------------------------------------------------------ sections

def s1_census(isprime, spf, lpf):
    section("S1  THE CENSUS AGAINST THE MODEL (the actual primes to 10^7)")
    m30 = Model(Z_MAIN, isprime, spf)
    m1000 = Model(Z_EXACT, isprime, spf)
    acc = {X: dict(elig=0, cls=0, s30=0.0, s1000=0.0, mu=0.0,
                   relig=0, rcls=0, rs30=0.0) for X in DECADES}
    for q in range(7, LIMIT + 1):
        if not isprime[q]:
            continue
        m = (q - 1) // 2
        if m % 2 == 0 or m % 3 == 0:
            continue
        fac = factor(m, lpf)
        divs = divisors_from(fac)
        cls = all(not isprime[2 * f + 1] for f in divs if 1 < f < m)
        p30, mu = m30.prob(m, divs)
        p1000, _ = m1000.prob(m, divs)
        rough = fac[0][0] > ROUGH
        for X in DECADES:
            if q <= X:
                a = acc[X]
                a["elig"] += 1
                a["cls"] += cls
                a["s30"] += p30
                a["s1000"] += p1000
                a["mu"] += mu
                if rough:
                    a["relig"] += 1
                    a["rcls"] += cls
                    a["rs30"] += p30
    print("  %-8s %8s %8s %10s %8s %10s %8s %8s | %8s %8s %10s %8s"
          % ("X", "elig", "class", "model30", "ratio", "model1000", "ratio",
             "mu30", "r-elig", "r-class", "r-model30", "ratio"))
    ratios = {}
    for X, rec in zip(DECADES, RECORD):
        a = acc[X]
        r30 = a["cls"] / a["s30"]
        r1000 = a["cls"] / a["s1000"]
        rr = a["rcls"] / a["rs30"]
        ratios[X] = (r30, rr)
        print("  %-8.0e %8d %8d %10.1f %8.4f %10.1f %8.4f %8.4f | %8d %8d %10.1f %8.4f"
              % (X, a["elig"], a["cls"], a["s30"], r30, a["s1000"], r1000,
                 a["mu"] / a["elig"], a["relig"], a["rcls"], a["rs30"], rr))
        ok(a["cls"] == rec, "class count at %.0e reads the record's %d" % (X, rec))
    ok(abs(acc[10 ** 4]["s1000"] - RECORD[0]) < 1e-9 and abs(acc[10 ** 5]["s1000"] - RECORD[1]) < 1e-9,
       "C1: the Z = 1000 model is exact at 10^4 and 10^5 (%.6f, %.6f)"
       % (acc[10 ** 4]["s1000"], acc[10 ** 5]["s1000"]))
    good = all(0.90 <= ratios[X][0] <= 1.10 and 0.90 <= ratios[X][1] <= 1.10
               for X in DECADES[1:])
    predicted(good, "P1: actual/model ratios at Z = 30 within [0.90, 1.10] at 10^5..10^7, all m and 30-rough")
    a = acc[LIMIT]
    return dict(share=a["cls"] / a["elig"], model_share=a["s30"] / a["elig"],
                rough_share=a["rcls"] / a["relig"], elig=a["elig"])


def s2_sampler(isprime, spf, census, rng):
    section("S2  THE SAMPLER AT A CENSUSED SCALE (N = %d, %d samples)" % (CONTROL_N, CONTROL_SAMPLES))
    model = Model(Z_MAIN, isprime, spf)
    recs = sample_scale(CONTROL_N, CONTROL_SAMPLES, rng, model, exact=isprime)
    ex = [1.0 if r[6] else 0.0 for r in recs]
    ex_u, ex_use = wmean(ex, [1.0] * len(recs))
    ex_a, ex_ase = wmean(ex, [r[0] for r in recs])
    crecs = [r for r in recs if r[2]]
    ex_t, ex_tse = wmean([1.0 if r[6] else 0.0 for r in crecs], [r[1] for r in crecs])
    print("  census share among eligible (10^7): exact %.4f   model %.4f   30-rough exact %.4f"
          % (census["share"], census["model_share"], census["rough_share"]))
    print("  sampled exact share: untilted %.4f (se %.4f)   tilt alone %.4f (se %.4f)   conditioned %.4f (se %.4f)"
          % (ex_u, ex_use, ex_a, ex_ase, ex_t, ex_tse))
    out = report("5e6", recs, CONTROL_N)
    ok(abs(out["t"] - census["model_share"]) <= 2 * out["t_se"],
       "C2: conditioned model share %.4f within 2 se (%.4f) of the census's model share %.4f"
       % (out["t"], out["t_se"], census["model_share"]))
    predicted(abs(ex_t - census["share"]) <= 2 * ex_tse
              and abs(ex_u - census["share"]) > abs(ex_t - census["share"]),
              "P2: conditioned exact share %.4f within 2 se (%.4f) of the census's %.4f, untilted %.4f farther"
              % (ex_t, ex_tse, census["share"], ex_u))


def s3_scale(rng):
    section("S3  THE MODEL AT SCALE (Z = 30, Kalai samples, conditioned and tilted above Z)")
    model = Model(Z_MAIN)
    rows = []
    for N, count in SCALES:
        recs = sample_scale(N, count, rng, model)
        rows.append((N, report("1e%d" % round(math.log10(N)), recs, N)))
    return rows


def main():
    print("explore_blind_model.py -- the blind class's order under the divisor model")
    print("sieve and smallest-factor table to %d, cofactor table to %d" % (LIMIT, LIMIT // 2))
    isprime = sieve(LIMIT)
    spf = spf_table(LIMIT, isprime)
    lpf = lpf_table(LIMIT // 2)
    rng = random.Random(SEED)
    census = s1_census(isprime, spf, lpf)
    s2_sampler(isprime, spf, census, rng)
    rows = s3_scale(rng)
    shares = [census["model_share"]] + [r["t"] for _, r in rows]
    falls = all(b < a for a, b in zip(shares, shares[1:]))
    predicted(falls and shares[-1] > 0.10,
              "P3: conditioned model share falls at every step from 10^7 and exceeds 0.10 at the last scale (%s)"
              % ", ".join("%.4f" % s for s in shares))
    norms = [census["model_share"] / 4.0 * math.log(math.log(LIMIT))] + [r["norm"] for _, r in rows]
    predicted(all(0.20 <= v <= 0.45 for v in norms),
              "P4: the model's (share/4) log log N within [0.20, 0.45] at every scale (%s)"
              % ", ".join("%.3f" % v for v in norms))
    section("SUMMARY")
    for kind, good, msg in CHECKS:
        print("  %-10s %s  %s" % (kind, "pass" if good else "FAIL", msg))
    nfail = sum(1 for k, g, _ in CHECKS if k == "CHECK" and not g)
    nmiss = sum(1 for k, g, _ in CHECKS if k == "PREDICTION" and not g)
    print("  checks failed: %d   predictions missed: %d" % (nfail, nmiss))
    return 1 if nfail else 0


if __name__ == "__main__":
    sys.exit(main())
