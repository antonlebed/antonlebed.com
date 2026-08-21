"""
explore_blind_share.py -- is the sieve's floor the ORDER of the blind class?
The blind-spot theorem (explore_blind_spot_infinite.py) and its lift, the
silent-set theorem (explore_silent_set.py), prove the probe's blind class
V = W(lambda) infinite at every even lambda by a lower bound of order
x / log^2 x. The census under it would not sit still: at lambda = 2 the
normalized count N log^2 x / x reads 1.35, 1.50, 1.67, 1.85 across the
decades to 10^7 and is still rising, and the record left the question
open -- whether the small admissible cofactors, each contributing of
order x / (f log^2 x), sum to a constant or to a growing factor. This
file closes that by proof (the factor grows, and at least as fast as
log x / log log x), states the heuristic that puts the class at a
POSITIVE PROPORTION of the primes, and measures what the proof loses on.

THE SETTING, in the two earlier files' terms. A state is a modulus N,
lambda(N) Carmichael's function, the wall W(L) the largest modulus whose
lambda divides L, the headroom V(N) = W(lambda(N)) / N. For even L the
class of L is the set of primes q = 1 (mod L) with V(q) = W(L); at L = 2
it is the class V = 24, the probe's largest blind class. Its criterion in
divisor terms (explore_silent_set.py S1): with m = (q-1)/L,

    (a) m odd, (b) m prime to every odd door p of L [(p-1) | L],
    (c) m > 1, (d) e f + 1 composite for every even divisor e of L and
        every divisor f > 1 of m with (e, f) != (L, m).

At L = 2: m odd, 3 does not divide m, m > 1, and 2f + 1 composite for
every divisor f of m with 1 < f < m (the door 3 is also the f = 3 case of
(d) whenever m > 3). Call a divisor f of m with 1 < f < m and 2f + 1 prime
a BAD divisor; a prime q > 5 with m odd is in the class iff m has none
(m = 3 is the one exception, excluded by (b)).

THE HAND-ATTACK, on paper before any engine code, and it is a proof.

THEOREM (the blind-share theorem). For every even L the class of L has

    N_L(x) >>_L x / (log x * log log x)

members below x. Hence N_L(x) log^2 x / x -> infinity: the silent-set
theorem's bound is a floor and not the order. No conjecture enters. (The
sum of 1/f over the admissible cofactors diverges on its own and not by
this theorem: every prime p with 2p + 1 composite is one, and the Sophie
Germain primes' reciprocal sum converges by Brun's sieve.)

Proof. Fix even L, let x be large, T = (log x)^C with C = C(L) a constant
fixed at the end, and A = {(q-1)/L : q <= x prime, q = 1 mod L}. Let G be
the elements of A with no prime factor below T (the T-ROUGH ones).

Step 1 (the good set). The sifting density of A is g(d) = phi(L)/phi(L d)
on squarefree d, of dimension 1, with remainders controlled on average by
the Bombieri-Vinogradov theorem at level D = x^(1/2) / (L (log x)^B) --
exactly the silent-set theorem's Step 1, with the sifting range z = T in
place of x^(1/10), so s = log D / log T -> infinity and the linear sieve's
lower bound is the fundamental lemma's:

    |G| = S(A, T) >= (1 - o(1)) X prod_(p < T) (1 - g(p))  >>_L  x / (log x log T),

X = li(x)/phi(L). Every m in G is odd and prime to every door of L (the
doors are at most L + 1 < T), and m > 1 but for the one element m = 1; so
(a), (b), (c) hold on G minus one element, and an m in G leaves the class
only through (d): some even e | L and some divisor f > 1 of m, (e, f) !=
(L, m), with e f + 1 prime. Since m is T-rough, so is f, and so is
g = m / f.

Step 2 (the bad set, an upper bound). Three cases, e fixed among the even
divisors of L (at most tau(L) of them).

Case f < m, f <= x^(1/2). Then g >= T. For each T-rough f with e f + 1
prime, the g counted are at most #{g <= x/(L f) : g T-rough, L f g + 1
prime}; the upper-bound sieve on the two forms g and L f g + 1 -- two
residues removed at every p < T not dividing L, one at p | L (where
L f g + 1 = 1 mod p), one at T <= p < w not dividing f, none at p | f --
gives

    << (x / (L f)) * (1 / log^2 T) * (log T / log w) * prod_(p | f) (1 - 1/p)^(-1)
    << x / (f log T log x),

w = (x / L f)^(1/4) >= x^(1/9), and the last product is 1 + O(omega(f)/T)
because f is T-rough. Summing over f: with R(u) = #{f <= u : f T-rough,
e f + 1 prime}, the same sieve (two residues removed below T, one above)
gives R(u) << u / (log T log u) for u >= T^4, and for T < u < T^4 sifting
only by the primes below u^(1/4) gives R(u) << u / log^2 u, which is
<< u / (log T log u) there too; partial summation then gives

    sum_(T < f <= x^(1/2)) 1/f << (log log x) / log T,

and the case contributes << x (log log x) / (log x log^2 T).

Case f = m, e < L. Then e m + 1 and L m + 1 are both prime with m T-rough:
three forms m, e m + 1, L m + 1 with three residues removed at every
p < T off p | e L (L - e), two at T <= p < w; the count is
<< (x / L) (1 / log^3 T)(log^2 T / log^2 w) << x / (log T log^2 x).

Case f > x^(1/2). Then g = m / f < x^(1/2) and g >= T is T-rough. For each
such g the f counted are at most #{f <= x/(L g) : f T-rough, e f + 1 and
L g f + 1 prime}: three forms, three residues removed at p < T off
p | e L g (L g - e) (L g != e since g >= T > L), two at T <= p < w off
p | g (L g - e), so

    << (x / (L g)) (1 / (log T log^2 x)) prod_(p | L g - e) (1 + 1/p) (1 + O(omega(g)/T)).

Write prod_(p | n) (1 + 1/p) <= sum_(a | n, a squarefree) 1/a and swap
the sums: sum_g (1/g) sum_(a | L g - e) 1/a = sum_a (1/a) sum_(g T-rough,
L g = e mod a, g <= x^(1/2)) 1/g; the progression has modulus a' =
a / gcd(a, L) >= a / L, and the inner sum is << (log x) / (phi(a') log T)
+ (log T) / a' + 1/T by the sieve in the progression above a' T^2, a
trivial bound below it, and g >= T. So the double sum is <<_L (log x) /
log T and the case contributes << x / (log x log^2 T).

Step 3 (the constant). Altogether the bad set is <<_L x (log log x) /
(log x log^2 T), against |G| >>_L x / (log x log T): with log T =
C log log x the ratio is O(1/C), so for C = C(L) large

    N_L(x) >= |G| - |bad| - 1 >> x / (log x * C log log x).       QED

What the theorem does NOT say. It gives no upper bound and no asymptotic.
The loss against a positive proportion is the one factor log log x, and it
sits in one place: the union bound of Step 2 sums, over the T-rough f with
e f + 1 prime, the MEAN number of bad divisors of a T-rough m, which is
sum 1/f ~ (log log x)/log T and grows; the TYPICAL number is bounded, the
mean being carried by the rare m with about twice the usual count of
prime factors (the tilt of Poisson(j) by 2^j is Poisson(2j)). Separating
the two is an Erdos-Kac-shaped second-moment argument this file does not
make.

THE HEURISTIC (stated as conjecture, tier observation for the census). For
a prime q with m = (q-1)/2 the expected number of bad divisors is

    mu(m) = sum_(f | m, 1 < f < m) 1/log(2 f + 1),

dominated by m's SMALLEST divisors: if m's prime factors are p_1 < p_2 <
... with log p_j of order e^j log p_1 (the typical spacing), the divisors
with largest prime p_j number 2^(j-1) and each contributes about
1/(e^j log p_1), a convergent geometric sum of order 1/log p_1. A
Poisson count with a bounded mean is zero with positive probability, so
the class should hold a POSITIVE PROPORTION c of the primes,
N(x) ~ c x / log x; the proportion among the primes with P^-(m) > T
should RISE with T (the mean falls as 1/log T) and fall slowly with x at
fixed T (each new scale of divisors adds a geometrically smaller term).
The census cannot separate c x / log x from slower growth at 10^7 -- the
known figures N/pi(x) = 0.129, 0.118, 0.111, 0.107 fall with shrinking
decrements -- and no constant is claimed. (Settled further in
explore_blind_model.py: the heuristic built as a definite model predicts
this census within 0.3% at every decade, and read on random factored
integers to 10^50 it keeps the normalization below flat there too -- a
positive limit and a slow decay to zero stay unseparated.)

PREDICTIONS, frozen before the engine ran (the heuristic's, read as
observables the rig prints; each a kill if it fails):

  P1 (ordering in T). At each of the decades 10^4, 10^5, 10^6, 10^7, the
     class's share among the primes q with P^-((q-1)/2) > T is strictly
     increasing over T = 5, 7, 30, 100, 300 (T = 5 is the primes with m
     odd and prime to 3 and 5 -- the door 3 and the first bad prime
     divisor; it excludes the one member q = 11, m = 5, so its numerator
     reads N - 1).
  P2 (the mean grows, the proof's loss). Among the primes with
     P^-(m) > 30, the MEAN number of bad divisors increases at each
     decade step, 10^4 -> 10^5 -> 10^6 -> 10^7.
  P3 (the mean is carried by the tail). At 10^7, among the primes with
     P^-(m) > 30, the share with at least one bad divisor is below the
     mean number of bad divisors: the count is over-dispersed, the excess
     sitting in the m with several.
  P4 (the proof's cases). At 10^7, among the bad m with P^-(m) > 30, more
     have a bad divisor f <= sqrt(m) than have every bad divisor above
     sqrt(m): the f > x^(1/2) case is the smaller one.

POSITIVE CONTROL. The divisor criterion against the wall: V(q) computed
from W's definition (the silent-set rig's wall_from) agrees with "m odd,
3 does not divide m, m > 1, no bad divisor" at every prime q <= 10^5 --
zero mismatches -- and the class counts per decade read the blind-spot
record's 159, 1,133, 8,770, 71,419. (The first run asserted 1,132 at 10^5,
a figure back-derived by hand from the record's rounded N log^2 x / x =
1.50; the recorded count is 1,133 and the assertion now reads the record.)

WHAT THE RIG MEASURES. Sieve of Eratosthenes to 10^7 and a largest-
prime-factor table to 5 * 10^6 (the cofactors), bytearray and array('I');
every prime q <= 10^7 with q > 5 and m odd has its divisors enumerated and
its bad divisors counted.

S1 THE CONTROL. The criterion against the wall to 10^5; the class count
   at 10^5.
S2 THE SHARE BY ROUGHNESS. Per decade X: pi(X), N(X), N/pi, N log^2 X / X,
   and N / (X / (log X log log X)) -- the theorem's normalization; then
   for T in {5, 7, 30, 100, 300} the count of primes with P^-(m) > T, the
   class members among them, their share. P1 is read here.
S3 THE MEAN AND THE TYPICAL. Per decade, among primes with P^-(m) > 30:
   the mean number of bad divisors, the share with none, one, two or
   more. P2 and P3 are read here.
S4 THE CASES. At 10^7, among the bad m with P^-(m) > 30: how many have a
   bad divisor f <= sqrt(m), how many have all bad divisors above
   sqrt(m). P4 is read here.

Run: python prime/code/explore_blind_share.py  (estimate: under 1 minute,
under 100 MB).

FINDINGS (from the printed run; 664,579 primes to 10^7, 71,419 class
members; both controls pass; three of the four predictions held and one
missed on a tie).

F1 THE CONTROL. Zero mismatches between the divisor criterion and
   V(q) = 24 at every prime to 10^5; the per-decade counts read the
   record's 159, 1,133, 8,770, 71,419.

F2 THE SHARE (S2). N/pi(x) reads 0.1294, 0.1181, 0.1117, 0.1075 across
   10^4..10^7 and N log^2 x / x reads 1.349, 1.502, 1.674, 1.855 -- and
   under the THEOREM'S normalization, N / (x / (log x log log x)), the
   census reads FLAT: 0.325, 0.319, 0.318, 0.320. The proved lower bound
   fits the census as an order over three decades. The heuristic reads
   this as the slow approach to a positive proportion -- the tail of
   mu(m) beyond the scale x is of order (2/e)^(log log x) = (log x)^(log 2
   - 1), a decay with exponent 0.31 that no census to 10^7 separates from
   1 / log log x -- and the census decides nothing between the two; the
   order stays OPEN between x / (log x log log x) and x / log x.
   The share among the primes with P^-(m) > T:

       T = 5      0.690  0.631  0.595  0.573
       T = 7      0.732  0.671  0.636  0.610
       T = 30     0.902  0.837  0.801  0.772
       T = 100    1.000  0.955  0.884  0.855
       T = 300    1.000  1.000  0.965  0.913

   P1 MISSED as frozen ("strictly increasing in T at every decade"): at
   10^4 the T = 100 and T = 300 cells are 105/105 and 95/95, every such
   prime a member, a tie at saturation. The order holds weakly at 10^4
   and strictly at every decade from 10^5; the reading the prediction was
   written for -- the share rises with T, as a mean falling like 1/log T
   predicts -- stands, and the miss is the frozen wording's. At fixed T
   the share falls with x, the decrements at T = 30 being 0.065, 0.036,
   0.029 per decade, which is what the tail's slow decay predicts and no
   evidence either way on its limit.

F3 THE MEAN AND THE TYPICAL (S3). Among the 30-rough m the mean number of
   bad divisors reads 0.099, 0.164, 0.212, 0.255 -- P2 held, the steps
   0.066, 0.048, 0.044 against the heuristic's (log log x)/log T steps of
   0.065, 0.054, 0.045 -- while the share with none reads 0.902, 0.837,
   0.801, 0.772, with one 0.099, 0.162, 0.189, 0.205, with two 0.000,
   0.001, 0.008, 0.020, with three or more 0.000, 0.000, 0.002, 0.004.
   P3 held: at 10^7 the share with a bad divisor, 0.2285, is below the
   mean, 0.2554 -- the count is over-dispersed and the excess sits in the
   m with several, which is the tail the union bound pays for.

F4 THE CASES (S4). Of the 15,960 bad 30-rough m at 10^7, 10,282 have a
   bad divisor f <= sqrt(m) and 5,678 have every bad divisor above it:
   P4 held, the f > x^(1/2) case the smaller, though not by the 1/log T
   the proof's bound has it -- a ratio of 0.55, read at T = 30 where
   1/log T is 0.29 and the sieve constants are not small.

Run record: 50.1 MB peak working set, 1.3 s wall, under memwatch.
"""

import math
import sys
from array import array

LIMIT = 10 ** 7
CONTROL = 10 ** 5
DECADES = [10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7]
ROUGH = [5, 7, 30, 100, 300]
RECORD = [159, 1133, 8770, 71419]   # explore_blind_spot_infinite.py, the class per decade

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


def v_p(n, p):
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def wall(n, fac, isprime):
    """W(n) from its definition; n + 1 must be within the sieve."""
    W = 2 if n % 2 else 2 ** (v_p(n, 2) + 2)
    for d in divisors_from(fac):
        p = d + 1
        if p > 2 and isprime[p]:
            W *= p ** (v_p(n, p) + 1)
    return W


# ------------------------------------------------------------ the class

def profile(q, lpf, isprime):
    """For a prime q > 5: (m, least prime factor of m, bad divisor count,
    has a bad divisor <= sqrt(m)), or None when m is even. Here m = (q-1)/2
    and a bad divisor is f | m with 1 < f < m and 2f + 1 prime."""
    m = (q - 1) // 2
    if m % 2 == 0:
        return None
    fac = factor(m, lpf)
    least = fac[0][0]
    bad = 0
    small = False
    for f in divisors_from(fac):
        if 1 < f < m and isprime[2 * f + 1]:
            bad += 1
            if f * f <= m:
                small = True
    return m, least, bad, small


def in_class(m, least, bad):
    return m > 1 and m % 3 != 0 and bad == 0


# ------------------------------------------------------------ sections

def s1_control(isprime, lpf):
    section("S1  THE CONTROL: the divisor criterion against the wall to %d" % CONTROL)
    mism = 0
    count = 0
    for q in range(7, CONTROL + 1):
        if not isprime[q]:
            continue
        n = q - 1
        V = wall(n, factor(n, lpf), isprime) // q
        pr = profile(q, lpf, isprime)
        crit = pr is not None and in_class(pr[0], pr[1], pr[2])
        if crit != (V == 24):
            mism += 1
        if crit:
            count += 1
    print("  mismatches criterion vs V(q) = 24: %d" % mism)
    print("  class members below %d: %d" % (CONTROL, count))
    ok(mism == 0, "the criterion is the class at every prime to %d" % CONTROL)
    ok(count == 1133, "class count below 10^5 reads the record's 1,133")


def census(isprime, lpf):
    """per-decade accumulators, keyed by decade index."""
    acc = {X: dict(pi=0, N=0, rough={T: [0, 0] for T in ROUGH},
                   bad30=[0, 0, 0, 0], mean30=[0, 0], cases=[0, 0])
           for X in DECADES}
    for q in range(2, LIMIT + 1):
        if not isprime[q]:
            continue
        pr = profile(q, lpf, isprime) if q > 5 else None
        for X in DECADES:
            if q > X:
                continue
            a = acc[X]
            a["pi"] += 1
            if pr is None:
                continue
            m, least, bad, small = pr
            member = in_class(m, least, bad)
            if member:
                a["N"] += 1
            for T in ROUGH:
                if least > T:
                    a["rough"][T][0] += 1
                    if member:
                        a["rough"][T][1] += 1
            if least > 30:
                a["mean30"][0] += 1
                a["mean30"][1] += bad
                a["bad30"][min(bad, 3)] += 1
                if bad:
                    a["cases"][0 if small else 1] += 1
    return acc


def s2_share(acc):
    section("S2  THE SHARE BY ROUGHNESS")
    print("  %9s %8s %7s %6s %8s %8s" % ("X", "pi", "N", "N/pi", "Nlog2/X", "N/(X/LLL)"))
    for X in DECADES:
        a = acc[X]
        L = math.log(X)
        print("  %9d %8d %7d %6.4f %8.3f %8.3f" % (
            X, a["pi"], a["N"], a["N"] / a["pi"], a["N"] * L * L / X,
            a["N"] / (X / (L * math.log(L)))))
    ok([acc[X]["N"] for X in DECADES] == RECORD,
       "the per-decade class counts read the blind-spot record's %s" % (RECORD,))
    print()
    print("  share of the class among primes with P^-(m) > T")
    print("  %9s " % "X" + " ".join("%14s" % ("T=%d" % T) for T in ROUGH))
    p1 = True
    for X in DECADES:
        a = acc[X]
        shares = []
        cells = []
        for T in ROUGH:
            n, k = a["rough"][T]
            s = k / n if n else float("nan")
            shares.append(s)
            cells.append("%6d/%-7d" % (k, n))
        print("  %9d " % X + " ".join("%14s" % c for c in cells))
        print("  %9s " % "" + " ".join("%14.4f" % s for s in shares))
        if not all(shares[i] < shares[i + 1] for i in range(len(shares) - 1)):
            p1 = False
    predicted(p1, "P1: the share rises with T at every decade")


def s3_mean(acc):
    section("S3  THE MEAN AND THE TYPICAL, among primes with P^-(m) > 30")
    print("  %9s %7s %8s %8s %8s %8s %8s" % ("X", "n", "mean", "P(0)", "P(1)", "P(2)", "P(>=3)"))
    means = []
    for X in DECADES:
        a = acc[X]
        n, tot = a["mean30"]
        mean = tot / n if n else float("nan")
        means.append(mean)
        b = a["bad30"]
        print("  %9d %7d %8.4f %8.4f %8.4f %8.4f %8.4f" % (
            X, n, mean, b[0] / n, b[1] / n, b[2] / n, b[3] / n))
    predicted(all(means[i] < means[i + 1] for i in range(len(means) - 1)),
              "P2: the mean number of bad divisors grows at each decade step")
    a = acc[LIMIT]
    n, tot = a["mean30"]
    share_bad = 1 - a["bad30"][0] / n
    predicted(share_bad < tot / n,
              "P3: at 10^7 the share with a bad divisor (%.4f) is below the mean (%.4f)"
              % (share_bad, tot / n))


def s4_cases(acc):
    section("S4  THE CASES at 10^7, among bad m with P^-(m) > 30")
    small, large = acc[LIMIT]["cases"]
    print("  with a bad divisor f <= sqrt(m):      %d" % small)
    print("  every bad divisor above sqrt(m):      %d" % large)
    predicted(small > large, "P4: the small-divisor case is the larger one")


def main():
    print("explore_blind_share.py -- is the sieve's floor the order of the blind class?")
    print("sieve to %d, cofactor table to %d" % (LIMIT, LIMIT // 2))
    isprime = sieve(LIMIT)
    lpf = lpf_table(LIMIT // 2)
    s1_control(isprime, lpf)
    acc = census(isprime, lpf)
    s2_share(acc)
    s3_mean(acc)
    s4_cases(acc)
    section("SUMMARY")
    for kind, good, msg in CHECKS:
        print("  %-10s %s  %s" % (kind, "pass" if good else "FAIL", msg))
    nfail = sum(1 for k, g, _ in CHECKS if k == "CHECK" and not g)
    nmiss = sum(1 for k, g, _ in CHECKS if k == "PREDICTION" and not g)
    print("  checks failed: %d   predictions missed: %d" % (nfail, nmiss))
    return 1 if nfail else 0


if __name__ == "__main__":
    sys.exit(main())
