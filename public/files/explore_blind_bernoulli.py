"""
explore_blind_bernoulli.py -- the order of the probe's biggest blind spot,
read through the denominators of the Bernoulli numbers.

THE QUESTION. The blind class V = 24 of the transparency headroom -- the
primes q > 5 whose door cohort {p prime : (p-1) | (q-1)} is exactly
{2, 3, q} (explore_blind_spot_infinite.py, the divisor criterion) -- is
infinite, >> x/log^2 x (the blind-spot theorem), >> x/(log x log log x)
(the blind-share theorem), and the record left its ORDER open between
that floor and x/log x, naming two proof routes and writing neither: a
second-moment bound on the bad-divisor count, or the density of integers
with no divisor in {(p-1)/2}, a sets-of-multiples question. The divisor
model (explore_blind_model.py) argued for a positive proportion of the
primes as a heuristic and could not separate it from a slow decay.

THE WELD, by hand. The von Staudt-Clausen theorem: the denominator of the
Bernoulli number B_{2k} is the product of the primes p with (p-1) | 2k.
Read at 2k = q-1 with q prime, the class condition IS a statement about
that denominator: for every prime q >= 11,

    q in the class  <=>  denom(B_{q-1}) = 6q  <=>  {B_{q-1}} = 1/6 - 1/q.

(q = 5 and q = 7 are the two primes with denom(B_{q-1}) = 6q outside the
class: each has cohort {2, 3, q}, but 4 | 5-1 bumps the wall's exponent
at 2 to W(4) = 240 = 48 * 5, so V(5) = 48, and 3 | 7-1 bumps it at 3 to
W(6) = 504 = 72 * 7, so V(7) = 72. For q >= 11, 4 | q-1 puts 5 in the
cohort and 3 | q-1 puts 7 there, so both clauses the census adds to the
cohort condition are absorbed by the denominator.)

So the sets-of-multiples question the record named is a classical one,
and at the INTEGER level it is answered. Erdos and Wagstaff, "The
fractional parts of the Bernoulli numbers", Illinois J. Math. 24 (1980)
104-112 (read in full): Theorem 2 -- for every epsilon there is T with
#{m <= x : (p-1) | m for some prime p > T} < epsilon x for all x > T;
and Theorem 3 -- for every k, the integers m whose set {p : (p-1) | 2m}
equals that of 2k have POSITIVE asymptotic density. At k = 1 that is the
set {m : denom(B_{2m}) = 6}; their table reads its share near 1/6 for
m up to 5 * 10^4 (2k to 10^5). Ford, "Integers divisible by a large shifted prime" (2016, read in
full) gives Theorem 2's exact order: for y <= x^{1-c} the integers m <= x
with a divisor p-1 > y number x/((log y)^0.086 (log log y)^{1/2}) up to
constants.

THE TRANSFER TO THE PRIMES, by hand -- a proof, its one external tool
named. Write, for T >= 5,
    delta_T = the density among primes of {q : (p-1) does not divide q-1
              for every prime p in [5, T]} -- a residue condition modulo
              L_T = lcm(p-1 : p <= T), so it exists by Dirichlet and
              equals the share of the reduced residues r mod L_T with
              r != 1 mod (p-1) for every such p;
    eps(T)  = limsup_x #{q <= x : (p-1) | (q-1) for some prime p > T,
              p != q} / pi(x).
The class share among primes up to x lies between delta_T(x) - eps_T(x)
and delta_T(x) for every T, so if eps(T) -> 0 the class has a relative
density and it is delta_inf = lim_T delta_T.

Positivity of delta_inf (the prime-measure Behrend). For the prime
measure the valuations v_l(q-1) are independent across primes l -- the
density of primes in a class mod L is 1/phi(L) = prod 1/phi(l^a) -- each
coordinate is a chain, and "no d in A divides q-1" is a DECREASING event
in the valuation vector, so Harris's inequality gives P(avoid A and
avoid B) >= P(avoid A) P(avoid B) for finite sets A, B. Hence
delta_T' >= delta_T (1 - eps(T)) for T' > T, delta_inf >= delta_T
(1 - eps(T)) > 0 once eps(T) < 1, and delta_T >= prod (1 - 1/phi(p-1)) > 0.
Harris alone cannot give the limit: sum 1/phi(p-1) diverges and the
product goes to zero. That product is the union bound's mean, the gap
between it and the class's share is the mean-versus-typical gap the
record named, and only eps(T) -> 0 closes it.

eps(T) -> 0 (the shifted-prime Erdos-Wagstaff). Their three classes, for
q-1 = (p-1) n with p > T, p != q, n >= 2, against L = log log p: (1)
Omega(p-1) < (2/3) L; (2) Omega_p(n) < (2/3) L, the prime factors of n
below p counted with multiplicity; (3) both at least (2/3) L, whence
Omega_p(q-1) >= (4/3) L. Every sieve step is one tool -- Theorem 1.1 of
Pollack, "Nonnegative multiplicative functions on sifted sets, and the
square roots of -1 modulo shifted primes", Glasgow Math. J. 62 (2020)
187-199, Shiu's bound over a sifted set: for f multiplicative with
0 <= f(l^v) <= A^v and f(n) <<_e n^e, and N the integers in (x-y, x]
avoiding at most v residue classes modulo every prime l, nu(l) of them,
    sum_{n in N} f(n)  <<  (y / log x) exp( sum_{l <= x} (f(l) - nu(l))/l ),
for x^a <= y <= x. Our sets are {n : dn+1 prime}, one excluded class per
prime l not dividing d, so exp(-sum nu(l)/l) is the 1/log x of
Brun-Titchmarsh and the primes dividing d return the factor d/phi(d);
the Chernoff-Rankin step is f = z^{Omega_p(n)}, z < 1 for "few prime
factors" and z > 1 for "many".
 (1) f = z^{Omega(n)} on N = {n <= y : n+1 prime} gives sum_{p <= y}
     z^{Omega(p-1)} << (y/log y)(log y)^{z-1}; at z = 2/3, #{p <= y :
     Omega(p-1) < (2/3) log log y} << y/(log y)^{1+d1}, d1 = (2/3) log(3/2)
     - 1/3 = 0.0635 (the shape of Erdos's 1935 bound). Then Brun-Titchmarsh per
     such p: for p <= sqrt(x) the sum of 1/phi(p-1) over few-factor p > T
     is << (log log T)/(log T)^d1; for p > sqrt(x), dyadic in p with
     pi(x; p-1, 1) << x/(phi(p-1) log(x/p)), the total is << pi(x)
     (log log x)/(log x)^d1. Both vanish.
 (2) p <= sqrt(x), d = p-1, X = x/d: f = z^{Omega_p(n)} on {n <= X :
     dn+1 prime} gives << (d/phi(d)) (X/log X)(log p)^{z-1}, so at z = 2/3
     the class-(2) primes q = 1 mod d number << (x/(phi(d) log x))
     (log p)^{-d1}; summed over p > T the share is << sum_{p > T}
     1/(phi(p-1)(log p)^d1) -> 0. For p > sqrt(x), n < sqrt(x) < p and
     Omega(n) < (2/3) log log x; the two-dimensional sieve (the same tool,
     f = 1) bounds #{p <= x/n : n(p-1)+1 prime} by (n/phi(n)) x/(n log^2 x),
     and sum 1/phi(n) over n <= sqrt(x) with Omega(n) < (2/3) log log x is
     << (log x)^{1-d1}, total << pi(x)/(log x)^d1.
 (3) f = z^{Omega_t(n)} at z = 7/6 on {n <= x : n+1 prime} gives
     << pi(x)(log t)^{z-1}, so #{q <= x : Omega_t(q-1) >= (7/6) log log t}
     << pi(x)(log t)^{-eta}, eta = (7/6) log(7/6) - 1/6 = 0.0132, uniformly
     in t <= x; Erdos-Wagstaff's union over t_i = exp(i^{2/eta}) then
     bounds #{q <= x : Omega_t(q-1) >= (4/3) log log t for some t > T} by
     << pi(x)/(log T)^{eta/2}.
So eps(T) << (log T)^{-c} -> 0.

THEOREM (the blind-density theorem). The primes q with V(q) = 24 have a
relative density among the primes, delta_inf = lim_T delta_T, and it is
positive: N_24(x) ~ delta_inf pi(x). The order the record left open
between x/(log x log log x) and x/log x is x/log x; the floor was a floor.
Nothing conjectural enters; the external inputs are Dirichlet's theorem,
Harris's inequality, and Pollack's sifted-set Shiu bound.

THE LIFT TO EVERY EVEN lambda, by hand. The blind class of lambda's own
wall is the primes q = 1 (mod lambda) with W(q-1) = W(lambda) q: within
that progression the conditions are v_p(q-1) <= v_p(lambda) for every p
in lambda's cohort (lambda | q-1 gives >= for free) and (p-1) does not
divide q-1 for every p off it, p != q -- DECREASING events in the
valuation vector, all of them, and the progression itself is a product
measure on shifted chains. So Harris applies as at lambda = 2, the finite
conditions have positive density on their own, and the tail is the same
eps(T), which never looked at lambda. The class of every even lambda has
a positive relative density among the primes.

THE SLATE, frozen before the engine.
  S1 (controls). Exact Bernoulli numbers B_2 .. B_40 by the standard
     recursion, their denominators against the von Staudt-Clausen product;
     then, over primes 11 <= q <= 10^5, the divisor criterion against
     denom(B_{q-1}) == 6 q and against wall(q-1) == 24 q, and q = 7 read
     as the exception: denom(B_6) = 42 and W(6) = 504.
     P1: zero disagreements in all three, and the exception as stated.
  S2 (the integer level). For m <= X = 5 * 10^7, the share of m with
     denom(B_{2m}) = 6 at each decade, the same share among the m that are
     odd and prime to 3 (the only m that can qualify), and beside them the
     class share among the primes q <= 2X+1 that are 11 mod 12 (the
     census's "eligible" primes, 0.42 at 10^7).
     P2: the integer share lies in [0.14, 0.18] at every decade from 10^4
     and does not rise from one decade to the next; every qualifying m is
     odd and prime to 3, so the conditional share is the integer share
     times X over the eligible count (three to within 3/X); the prime
     share is below the conditional share at every decade (the tilt).
  S3 (delta_T against the class). The exact delta_T, by the valuation
     enumeration the independence makes possible, for T up to 199; the
     empirical delta_T(x) at x = 10^8 over the primes in (T, x], for T
     through 10^6; the class share at 10^8; eps_T(x) = the share of primes
     q <= x with (p-1) | (q-1) for some p > T, p != q (the proof's tail,
     non-increasing in T by definition); and the Harris product
     prod (1 - 1/phi(p-1)).
     P3: exact and empirical delta_T agree within 10^-3 at every T both
     are printed for; the Harris product crosses below the class share
     by T = 100.
  S4 (mean versus typical). Over primes q <= x, the MEAN number of primes
     p > T, p != q, with (p-1) | (q-1), beside the PROPORTION of q with at
     least one, at x = 10^6, 10^7, 10^8 and T = 5, 10^2, 10^4.
     P4: the mean grows with x at fixed T (the union bound's divergence);
     the proportion falls with T at fixed x.
  Kill shapes are observables: any disagreement in S1 kills the weld;
  an S3 exact/empirical gap above 10^-3 kills the density computation.

FINDINGS (the run of record below; the prints are the evidence).

  F1 (the weld, property). B_2 .. B_40 by exact recursion have the von
     Staudt-Clausen denominators, 0 mismatches. Over the primes 11 <= q <=
     10^5 the divisor criterion agrees with denom(B_{q-1}) == 6q at every
     prime, and with wall(q-1) == 24q to 2 * 10^4; q = 5 and 7 are the
     two exceptions below 11, denom(B_4) = 30 = 6 * 5 with W(4) = 240 =
     48 * 5 and denom(B_6) = 42 = 6 * 7 with W(6) = 504 = 72 * 7. 1133
     members below 10^5.
  F2 (the integer level, observation). The share of m <= X with
     denom(B_2m) = 6 reads 0.1650, 0.1582, 0.1542, 0.1508, 0.1487 at X =
     10^4 .. 10^7 and 5 * 10^7 -- in [0.14, 0.18] and falling at every
     decade, so Erdos-Wagstaff's "near 1/6" was a reading at 5 * 10^4 and not
     the limit, which their theorem makes positive and this run does not
     estimate. Every qualifying m is odd and prime to 3, so the share
     among those m is three times as large (0.495 -> 0.446), and the class
     share among the primes 11 mod 12 sits below it at every decade, 0.4929
     -> 0.4178, the shifted-prime tilt widening from 0.002 to 0.028.
  F3 (delta_T, observation, with the prime-measure law checked). The
     exact delta_T from the independent valuations and the empirical share
     among primes in (T, 10^8] agree to 5 * 10^-5 at every T <= 199 (0.25,
     0.1875, 0.16875, 0.16108, 0.15533, 0.15144, 0.14505 at T = 7, 11, 23,
     47, 67, 101, 199; 13 and 17 add nothing, 12 | q-1 and 16 | q-1 being
     excluded already by 4). The empirical delta_T continues 0.13706,
     0.13273, 0.12305, 0.11552, 0.10938 at T = 499, 1009, 10^4, 10^5, 10^6
     against the class share 0.10445 among all primes to 10^8 (601,803 of
     5,761,452; N/(x/(log x log log x)) = 0.323, N log^2 x/x = 2.04). The
     proof's tail eps_T(x) -- primes q <= 10^8 with (p-1) | (q-1) for some
     p > T, p != q -- reads 0.808, 0.662, 0.528, 0.443, 0.313 at T = 7,
     101, 10^4, 10^5, 10^6: the theorem's (log T)^-c with c = 0.0066 is
     an asymptotic statement and the census cannot see it. The Harris
     product prod (1 - 1/phi(p-1)) crosses below the class share at T = 23
     (0.0923 against 0.1045) and reaches 0.0018 by T = 10^6: the
     independence bound is not the mechanism.
  F4 (mean versus typical, observation). Over primes q <= x the mean
     number of primes p > T, p != q, with (p-1) | (q-1) grows with x at
     every T -- 4.86, 5.38, 5.82 at T = 5; 2.60, 3.11, 3.54 at T = 100;
     0.72, 1.21, 1.64 at T = 10^4, for x = 10^6, 10^7, 10^8 -- while the
     proportion of q with at least one falls with T at every x (0.847,
     0.663, 0.528 at x = 10^8) and itself still rises with x at T = 10^4
     (0.392, 0.484, 0.528). The mean is the union bound's quantity and it
     diverges; the proportion is the proof's, and at T = 10^4 it has not
     turned over by 10^8.

  What the run says about the theorem: nothing against it and nothing
  for its constant. delta_inf is below 0.109 and positive; the class
  share has fallen 0.4929 -> 0.4178 among the eligible primes over four
  decades with no flattening in sight, which is what a limit reached at
  the rate (log T)^-0.0066 looks like from 10^8.

THE SLATE'S OWN CORRECTIONS, made before any finding was read: P2b was
frozen as "three times the integer share exactly", but the eligible count
below X is X/3 only to within one, so the statistic's algebra allows a
3/X slip (the ratio is 0.4950 against 0.4950 at 10^4 and passes at 3/X);
and eps_T(x) was first coded as delta_T(x) minus the overall share, whose
two populations differ (q > T against all q), rather than as the proof's
own tail, the share of primes with a shifted-prime divisor beyond T -- the
table's eps column is the latter. Neither changed a verdict.

RUN OF RECORD. python prime/code/memwatch.py explore_blind_bernoulli.py:
0 FAIL, 22 s, peak commit 445 MB under the 512 MB default; the uint8
counter peaks at 245 of its 255, a control the run asserts (a first draft
materialized an int64 range of length X, 400 MB, and was killed at 1064
MB; the run above has no such array).

RESOURCES. One sieve to 10^8 + 1 (numpy bool, 100 MB), one uint8 counter
to 5 * 10^7 (50 MB) and one more for the truncations, two boolean masks of
that length, the primes' index array (46 MB); no integer range of length X
is ever materialized; peak estimated under 400 MB; run under memwatch at
the 512 MB default. Wall-clock estimate: under two minutes.
"""

import os
import sys
import math
import time
from fractions import Fraction
from itertools import product

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np  # noqa: E402

X = 5 * 10 ** 7          # m ranges over 1..X; q = 2m+1 <= 2X+1
N = 2 * X + 1
FAILS = []


def ok(cond, msg):
    tag = "ok  " if cond else "FAIL"
    print("  [%s] %s" % (tag, msg))
    if not cond:
        FAILS.append(msg)


def section(t):
    print()
    print(t)


# ------------------------------------------------------------ the tables

def sieve_np(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return s


def phi(n):
    r, m, p = n, n, 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            r -= r // p
        p += 1
    if m > 1:
        r -= r // m
    return r


def small_primes(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(range(i * i, n + 1, i)))
    return [i for i in range(n + 1) if s[i]]


def v_p(n, p):
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


# ------------------------------------------------------------ S1

def bernoulli_exact(nmax):
    """B_0 .. B_nmax by the recursion sum_{j<=n} C(n+1, j) B_j = 0."""
    B = [Fraction(1)]
    for n in range(1, nmax + 1):
        s = Fraction(0)
        for j in range(n):
            s += math.comb(n + 1, j) * B[j]
        B.append(-s / (n + 1))
    return B


def vsc_denominator(two_k, isprime):
    d = 1
    for e in range(1, two_k + 1):
        if two_k % e == 0 and isprime[e + 1]:
            d *= e + 1
    return d


def wall(L, isprime):
    W = 2 if L % 2 else 2 ** (v_p(L, 2) + 2)
    d = 1
    while d * d <= L:
        if L % d == 0:
            for dd in {d, L // d}:
                p = dd + 1
                if p > 2 and isprime[p]:
                    W *= p ** (v_p(L, p) + 1)
        d += 1
    return W


def in_class_divisor(q, isprime):
    m = (q - 1) // 2
    if m % 2 == 0 or m % 3 == 0:
        return False
    e = 2
    while e * e <= m:
        if m % e == 0:
            if isprime[2 * e + 1] or (e != m // e and isprime[2 * (m // e) + 1]):
                return False
        e += 1
    return True


def s1_controls(isprime):
    section("S1 CONTROLS: von Staudt-Clausen, and the weld")
    B = bernoulli_exact(40)
    bad = [2 * k for k in range(1, 21)
           if B[2 * k].denominator != vsc_denominator(2 * k, isprime)]
    ok(not bad, "P1a: exact B_2..B_40 denominators = the von Staudt-Clausen "
       "product: %d mismatches %s" % (len(bad), bad[:4]))
    print("  B_2 .. B_12 denominators: %s" % [B[2 * k].denominator for k in range(1, 7)])
    ok(vsc_denominator(4, isprime) == 30 and wall(4, isprime) == 240
       and not in_class_divisor(5, isprime)
       and vsc_denominator(6, isprime) == 42 and wall(6, isprime) == 504
       and not in_class_divisor(7, isprime),
       "P1b: q = 5 and 7 are the exceptions: denom(B_4) = 30 = 6*5 with "
       "W(4) = 240 = 48*5, denom(B_6) = 42 = 6*7 with W(6) = 504 = 72*7, "
       "and both are outside the class")
    dis_b, dis_w, count = [], [], 0
    for q in range(11, 10 ** 5 + 1):
        if not isprime[q]:
            continue
        a = in_class_divisor(q, isprime)
        b = (vsc_denominator(q - 1, isprime) == 6 * q)
        if a != b:
            dis_b.append(q)
        if q <= 2 * 10 ** 4:
            c = (wall(q - 1, isprime) == 24 * q)
            if a != c:
                dis_w.append(q)
        count += a
    ok(not dis_b, "P1c: divisor criterion vs denom(B_{q-1}) == 6q over primes "
       "11 <= q <= 10^5: %d disagreements %s" % (len(dis_b), dis_b[:4]))
    ok(not dis_w, "P1d: divisor criterion vs wall(q-1) == 24q over primes "
       "11 <= q <= 2*10^4: %d disagreements %s" % (len(dis_w), dis_w[:4]))
    print("  class members below 10^5: %d" % count)


# ------------------------------------------------------------ the counter

def build_counter(isprime):
    """cnt[m] = number of primes p >= 5 with (p-1) | 2m, i.e. (p-1)/2 | m,
    capped at 255; for q = 2m+1 prime the self-term p = q is one of them."""
    cnt = np.zeros(X + 1, dtype=np.uint8)
    primes = np.nonzero(isprime)[0]
    t0 = time.time()
    for p in primes[2:]:           # skip 2, 3
        h = int(p - 1) // 2
        if h > X:
            break
        cnt[h::h] += 1
    print("  counter built over %d primes in %.1fs; max count %d" % (len(primes), time.time() - t0, int(cnt.max())))
    ok(int(cnt.max()) < 255, "the uint8 counter never reaches its cap (a wrap at 256 would read as 0)")
    return cnt, primes


# ------------------------------------------------------------ S2

def s2_integer_level(cnt, qs, mq):
    section("S2 THE INTEGER LEVEL: the share of m with denom(B_2m) = 6")
    good = (cnt == 0)
    good[0] = False
    elig = np.zeros(X + 1, dtype=bool)
    elig[1::2] = True
    elig[3::3] = False
    stray = int(np.count_nonzero(good & ~elig))
    qgood = (cnt[mq] == 1)
    qelig = (qs % 12 == 11)
    print("  %-10s %-12s %-14s %-14s" % ("X", "all m", "m odd, 3!|m", "primes 11 mod 12"))
    rows = []
    dec = 10 ** 4
    while dec <= X:
        g = int(np.count_nonzero(good[:dec + 1]))
        ge = g - int(np.count_nonzero(good[:dec + 1] & ~elig[:dec + 1]))
        ne = int(np.count_nonzero(elig[:dec + 1]))
        sel = qs <= 2 * dec + 1
        pg = int((qgood & qelig & sel).sum())
        pe = int((qelig & sel).sum())
        rows.append((dec, g / dec, ge / ne, pg / pe))
        print("  %-10d %-12.4f %-14.4f %-14.4f" % (dec, g / dec, ge / ne, pg / pe))
        dec *= 10
    if dec // 10 < X:
        g = int(np.count_nonzero(good)); ge = g - stray; ne = int(np.count_nonzero(elig))
        pg = int((qgood & qelig).sum()); pe = int(qelig.sum())
        rows.append((X, g / X, ge / ne, pg / pe))
        print("  %-10d %-12.4f %-14.4f %-14.4f" % (X, g / X, ge / ne, pg / pe))
    shares = [r[1] for r in rows]
    ok(all(0.14 <= s <= 0.18 for s in shares)
       and all(shares[i + 1] <= shares[i] + 1e-9 for i in range(len(shares) - 1)),
       "P2a: integer share in [0.14, 0.18] at every decade and non-increasing")
    ok(all(abs(r[2] - 3 * r[1]) < 3.0 / r[0] + 1e-12 for r in rows)
       and stray == 0,
       "P2b: every qualifying m is odd and prime to 3, so the conditional share "
       "is three times the integer share to within 3/X")
    ok(all(r[3] < r[2] for r in rows),
       "P2c: the prime share sits below the conditional integer share at every decade")
    return qgood


# ------------------------------------------------------------ S3

def exact_delta(T, isprime):
    """delta_T as a sum over valuation vectors: P(v_l = a) = 1/phi(l^a) -
    1/phi(l^(a+1)) and P(v_l >= A_l) = 1/phi(l^A_l), independent across l."""
    ps = [p for p in range(5, T + 1) if isprime[p]]
    need = {}
    for p in ps:
        d, l, f = p - 1, 2, {}
        while d > 1:
            if d % l == 0:
                f[l] = v_p(d, l)
                while d % l == 0:
                    d //= l
            l += 1
        need[p] = f
    ls = sorted({l for f in need.values() for l in f})
    A = {l: max(f.get(l, 0) for f in need.values()) for l in ls}

    def P(l, a):
        if a < A[l]:
            return 1.0 / phi(l ** a) - 1.0 / phi(l ** (a + 1))
        return 1.0 / phi(l ** a)

    total = 0.0
    states = 1
    for l in ls:
        states *= A[l] + 1
    if states > 3 * 10 ** 6:
        return None, states
    for vec in product(*[range(A[l] + 1) for l in ls]):
        v = dict(zip(ls, vec))
        hit = False
        for p in ps:
            if all(v[l] >= e for l, e in need[p].items()):
                hit = True
                break
        if hit:
            continue
        pr = 1.0
        for l in ls:
            pr *= P(l, v[l])
        total += pr
    return total, states


def s3_truncations(cnt, isprime, qs, mq, qgood):
    section("S3 delta_T AGAINST THE CLASS SHARE (x = %d)" % N)
    share = qgood.sum() / len(qs)
    print("  class share among all primes q <= %d: %.5f  (%d of %d)"
          % (N, share, int(qgood.sum()), len(qs)))
    xs = float(N)
    print("  N / (x / (log x log log x)) = %.3f;  N log^2 x / x = %.3f"
          % (qgood.sum() / (xs / (math.log(xs) * math.log(math.log(xs)))),
             qgood.sum() * math.log(xs) ** 2 / xs))
    checkpoints = [7, 11, 13, 17, 23, 31, 47, 67, 101, 199, 499, 1009, 10007, 10 ** 5, 10 ** 6]
    cntT = np.zeros(X + 1, dtype=np.uint8)
    cq = cnt[mq].astype(np.int16) - 1          # shifted-prime divisors of q-1, p >= 5, p != q
    harris = 1.0
    pi_list = [p for p in range(5, 10 ** 6 + 1) if isprime[p]]
    i = 0
    prev_eps = None
    mono = True
    crossed = None
    print("  %-8s %-10s %-10s %-10s %-10s" % ("T", "exact", "empirical", "eps_T(x)", "Harris"))
    for T in checkpoints:
        while i < len(pi_list) and pi_list[i] <= T:
            p = pi_list[i]
            h = (p - 1) // 2
            cntT[h::h] += 1
            harris *= 1.0 - 1.0 / phi(p - 1)
            i += 1
        sel = qs > T
        emp = float((cntT[mq[sel]] == 0).sum()) / float(sel.sum())
        eps = float(((cq - cntT[mq] + (qs <= T)) >= 1).mean())   # q <= T: its self-mark sits in cntT
        ex_s = ""
        ex = None
        if T <= 1009:
            ex, states = exact_delta(T, isprime)
        if ex is not None:
            ex_s = "%.5f" % ex
            if abs(ex - emp) > 1e-3:
                mono = False
                print("  exact/empirical gap %.5f at T = %d" % (ex - emp, T))
        prev_eps = eps
        if crossed is None and harris < share:
            crossed = T
        print("  %-8d %-10s %-10.5f %-10.5f %-10.5f" % (T, ex_s, emp, eps, harris))
    ok(mono, "P3: exact = empirical within 10^-3 where both print")
    ok(crossed is not None and crossed <= 101,
       "P3: the Harris product crosses below the class share by T = 100 (at T = %s)" % crossed)


# ------------------------------------------------------------ S4

def s4_mean_vs_typical(cnt, isprime, qs, mq):
    section("S4 MEAN VERSUS TYPICAL: shifted-prime divisors of q-1 beyond T")
    print("  %-10s %-8s %-12s %-12s" % ("x", "T", "mean count", "proportion>=1"))
    means = {}
    props = {}
    for T in (5, 10 ** 2, 10 ** 4):
        cntT = np.zeros(X + 1, dtype=np.uint8)
        for p in range(5, T + 1):
            if isprime[p]:
                h = (p - 1) // 2
                cntT[h::h] += 1
        for x in (10 ** 6, 10 ** 7, N):
            sel = (qs <= x) & (qs > T)
            big = cnt[mq[sel]].astype(np.int64) - cntT[mq[sel]].astype(np.int64) - 1
            means[(x, T)] = float(big.mean())
            props[(x, T)] = float((big >= 1).mean())
            print("  %-10d %-8d %-12.4f %-12.4f" % (x, T, means[(x, T)], props[(x, T)]))
    ok(all(means[(10 ** 7, T)] > means[(10 ** 6, T)] and means[(N, T)] > means[(10 ** 7, T)]
           for T in (5, 10 ** 2, 10 ** 4)),
       "P4a: the mean count grows with x at every T")
    ok(all(props[(x, 10 ** 2)] < props[(x, 5)] and props[(x, 10 ** 4)] < props[(x, 10 ** 2)]
           for x in (10 ** 6, 10 ** 7, N)),
       "P4b: the proportion with at least one falls with T at every x")


def main():
    t0 = time.time()
    print("explore_blind_bernoulli.py -- X = %d, primes to %d" % (X, N))
    isprime = sieve_np(N + 2)
    s1_controls(isprime)
    cnt, primes = build_counter(isprime)
    qs = primes[(primes >= 7) & (primes <= N)]
    del primes
    mq = (qs - 1) // 2
    qgood = s2_integer_level(cnt, qs, mq)
    s3_truncations(cnt, isprime, qs, mq, qgood)
    s4_mean_vs_typical(cnt, isprime, qs, mq)
    print()
    print("%d FAIL(s); %.0fs" % (len(FAILS), time.time() - t0))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
