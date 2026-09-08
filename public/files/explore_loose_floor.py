"""explore_loose_floor.py -- the loose share against Ford's shape: does the
share of primes whose headroom their cohort does not fix go to zero like the
multiplication-table law, or sit above a positive floor?

THE QUESTION. For a prime q the sighted probe's whole reading is its headroom
V(q) = W(q - 1)/q, W the transparency wall, Adams' number: 2^(v_2(L)+2) times
p^(v_p(L)+1) over the odd primes p with (p - 1) | L. Its cohort is the set of
primes r != q with (r - 1) | (q - 1), the radical of q V(q) read off the
Bernoulli denominator. The cohort fixes an exponent v_p(q - 1) exactly when
some cohort member r has v_p(r - 1) = v_p(q - 1); a prime with an exponent
the cohort does not fix is LOOSE, and the loose share among the primes fell
11.7, 9.3, 8.2, 7.5% across the decades to 10^7 (explore_blind_adams.py,
explore_three_kills.py), five of six loose at the prime 2. The suspicion
carried in: the shape is Ford's law for integers with a divisor in (y, 2y],
(log x)^(-delta) (log log x)^(-3/2) with delta = 1 - (1 + log log 2)/log 2 =
0.086..., which has no free parameter and whose span over 10^4..10^7 is 0.68
against the measured 0.64. This rig asks whether that shape can be the
share's, and prints the 2-adic component one decade further.

THE INCUMBENT, read full-text (Ford, The distribution of integers with a
divisor in a given interval, Ann. of Math. 168 (2008), sections 1.3 and 14).
Ford's shifted-prime results concern H(x, y, z; P), the number of n <= x of
the form q + l, q prime, with a divisor in (y, z]: Theorem 6 bounds it above
by H(x, y, z)/log x once z >= y + (log y)^(2/3), and Theorem 7 bounds it
below at x^a < z = x^b. The loose class is not that object: loose at 2 with
v_2(q - 1) = a is "no divisor d of the odd part m of q - 1, d < m, with
2^a d + 1 prime", a condition on divisors landing in a SET (the shifted
primes of one 2-adic valuation), not in an interval, and the paper states no
result about it. The shape was a transplant from the interval problem with
nothing behind it.

THE HAND-ATTACK, before any engine code.

 L1 THE FLOOR IS ALREADY A THEOREM. The blind-density theorem
    (explore_blind_bernoulli.py) gives every class {q : q == 1 (mod lambda),
    V(q) = W(lambda)}, lambda even, a positive relative density among the
    primes. Take lambda = 8: W(8) = 2^5 * 3 * 5 = 480, so V(q) = 480 says
    v_2(q - 1) = 3 and the cohort's odd members are exactly 3 and 5, with
    v_3(q - 1) = v_5(q - 1) = 0. The cohort's 2-adic exponents are v_2(2) = 1
    and v_2(4) = 2, neither equal to 3, so every member of the class is loose
    at 2. Hence liminf (loose share) >= delta_8 > 0, and any shape tending to
    zero -- Ford's, any power of log -- is forbidden. The same containment
    holds at every even lambda that is itself loose, i.e. carries a prime
    p | lambda with (p - 1) | lambda and no cohort prime r of lambda with
    v_p(r - 1) = v_p(lambda): lambda = 2^a with 2^a + 1 composite, lambda =
    24 (cohort 3, 5, 7, 13 at 2-adic exponents 1, 2, 1, 2 against 3).
 L2 WHICH a CAN BE LOOSE. v_2(q - 1) = a is forced whenever 2^a + 1 is
    prime, since r = 2^a + 1 then sits in every cohort with 2^a | q - 1 and
    v_2(r - 1) = a. So a in {1, 2, 4, 8, 16} is never loose (3, 5, 17, 257,
    65537), and a = 3 is the least loose valuation, the class q == 9
    (mod 16), an eighth of the primes. (Corrected by the run: the Fermat
    prime ITSELF is loose at its own exponent, q = 2^a + 1 having no cohort
    member but q at that valuation; so a in {4, 8, 16} carries exactly one
    loose prime each, and every other prime at those exponents is forced.)
 L3 THE LIMIT EXISTS, BY THE THEOREM'S OWN ROUTE. Within q == 1 (mod 2^a)
    the conditions "v_2(q - 1) <= a" and "(r - 1) does not divide q - 1 for
    every prime r == 1 + 2^a (mod 2^(a+1)), r != q" are decreasing events in
    the valuations of q - 1; the members r > T cost at most eps(T) of the
    primes by the theorem's sieve step, which never looked at the
    condition's shape; the finitely many below T have positive density on
    their own (m == 1 modulo the product of the odd primes <= T meets every
    one); Harris's inequality gives positivity and T -> infinity the density.
    So each a-component converges and the loose-at-2 share converges to
    their sum, dominated by 2^(-a). This is the general-lambda sentence of
    the blind-density block with the off-cohort condition thinned to one
    valuation, recorded as the route; the FLOOR of L1 is what the prints
    lean on.
 L4 WHAT A PRINT CAN AND CANNOT DECIDE. Ford's shape predicts decade ratios
    0.850, 0.884, 0.906, 0.921 from 10^4 to 10^8; an approach to a positive
    limit predicts ratios rising to 1. Five points do not separate the two
    (explore_three_kills.py F2 said so of four), so the kill of the shape is
    L1 and the 10^8 point is a RECORD, read against both.

THE ENGINE. Loose at 2 is computed with no factorization: a prime q is
forced at 2 exactly when q - 1 = (r - 1) k for a prime r != q and an odd
k >= 3, so one pass over the primes r marking (r - 1) k for odd k >= 3 marks
every forced q - 1 and nothing else (k = 1 is r = q itself; an even k changes
the valuation). The cohort test for the lambda = 8 class marks (r - 1) k for
every k >= 2 and every prime r >= 7, so an unmarked L with 3 and 5 not
dividing it and v_2(L) = 3 has odd cohort exactly {3, 5}. Two flag bits in
one uint8 array over L <= 10^8. The integer control marks, for every prime
r == 9 (mod 16), the odd multiples k d of d = (r - 1)/8 with k >= 3: the odd
m left unmarked are those with no proper divisor d such that 8 d + 1 is
prime, the integer statement whose positive density is Erdos-Wagstaff's
argument.

TRANSPLANT FLAGS. (1) Ford's shape: from the interval problem, named above,
killed by L1. (2) The three-kills figures 0.0906, 0.0751, 0.0673, 0.0623 for
the loose-at-2 share are reproduced here by an independent method, never
imported. (3) Nothing from the walker or the schedule corpus enters.

PREDICTIONS, fixed before the run, each naming what the rig PRINTS.

 PR1 THE CONTROL. The loose-at-2 share of the primes 11 <= q <= x at x =
     10^4, 10^5, 10^6, 10^7 reads 0.0906, 0.0751, 0.0673, 0.0623 to four
     decimals (explore_three_kills.py F2), and the loose count among q == 9
     (mod 16) below 10^5 reads 476 of 1196 (explore_blind_adams.py F3).
     KILL: one figure off. The wrong-marking control -- odd k >= 5 instead
     of >= 3 -- must change the share at 10^6, or the marking has no teeth.
 PR2 THE FERMAT ZEROS. The loose-at-2 count at a in {1, 2, 4, 8, 16} is 0 at
     every decade, nonzero at a = 3, 5, 6, 7. KILL: a nonzero count at a
     Fermat exponent.
 PR3 THE CONTAINMENT COUNT. Every prime q <= 10^8 with V(q) = 480 is loose
     at 2: the class count per decade and 0 exceptions. KILL: one exception.
 PR4 THE FLOOR'S SIZE. The lambda = 8 class's share of the primes per decade
     and its share of the loose-at-2 primes; expected a few hundredths of
     the primes. Record.
 PR5 ONE DECADE FURTHER. The loose-at-2 share below 10^8 and its decade
     ratio, against Ford's full shape's 0.921 and the pure power's 0.989,
     and the a = 3 relative share by decade. Expected: the ratio rises above
     the 10^7 one, 0.926. Record, not a kill (L4).
 PR6 THE INTEGER CONTROL. The share of odd m <= y with no proper divisor d
     such that 8 d + 1 is prime, y = 10^3..10^7, and its decade ratios: a
     positive-density set read at machine widths. Record.

RESOURCE. One process, numpy with OPENBLAS_NUM_THREADS = 1; the sieve 100 MB
freed before the flag array's 100 MB; estimate under 60 s, run under
memwatch.

FINDINGS (one run; tiers in brackets; the run record at the bottom). The
control ran first: the marking reproduced 0.0906, 0.0751, 0.0673, 0.0623 to
four decimals, the wrong marking read 0.0690 against 0.0673 at 10^6, and the
divisor method on the 1196 primes q == 9 (mod 16) below 10^5 read 476 loose
at any prime and 472 at 2, the four odd-only members 17497, 52489, 77977,
91961, settling the frozen figure's ambiguity: PR1's 476 counted looseness
at any prime.

 F1 THE FLOOR [theorem by L1; the containment a property, 0 exceptions over
    75,175 class members to 10^8]. Every prime with V(q) = 480 is loose at
    2, the least 137, 569, 809, 857, 1097, 1193. The class is 0.0188,
    0.0164, 0.0144, 0.0138, 0.0130 of the primes at 10^4..10^8 and a steady
    0.207, 0.218, 0.214, 0.222, 0.220 of the loose-at-2 primes, so the floor
    and the share it bounds fall at one rate. Ford's shape is dead as the
    loose share's: the blind-density theorem's delta_8 sits under the
    share at every x, and nothing tending to zero can be its limit.
 F2 THE FERMAT EXPONENTS [rule in range, to 10^8]. Loose at 2 is impossible
    at v_2(q - 1) = 1 and 2, and at 4, 8, 16 exactly one prime each is
    loose, the Fermat prime 17, 257, 65537 itself, whose only cohort member
    at its valuation would be q; PR2's zero was off by that one prime at
    each Fermat exponent (L2 corrected in place). a = 3 carries 230,877 of
    the 341,289 loose-at-2 primes to 10^8, a = 5, 6, 7 the next 54,145,
    26,616, 17,290, and every a from 9 to 21 appears, 16 through 65537
    alone.
 F3 ONE DECADE FURTHER [observation]. The loose-at-2 share reads 0.0592
    below 10^8, decade ratios 0.829, 0.896, 0.926, 0.951 from 10^4; Ford's
    full shape gives 0.850, 0.884, 0.906, 0.921 and the pure power 0.981,
    0.984, 0.987, 0.989. The measured ratios run AHEAD of the shape's from
    10^6 on -- the share flattens faster than the multiplication-table law
    does -- the reading a positive limit predicts, though five points prove
    no limit (L4); the span over 10^4..10^7 is 0.688 for this component
    against the shape's 0.680, the coincidence the suspicion was built on.
    The a = 3 relative share, loose among q == 9 (mod 16), reads 0.483,
    0.395, 0.362, 0.336, 0.321, its decrements 0.089, 0.033, 0.026, 0.015.
 F4 THE INTEGER CONTROL [observation]. The odd m <= y with no proper divisor
    d such that 8 d + 1 is prime are 0.552, 0.490, 0.455, 0.431, 0.413 of
    the odd integers at y = 10^3..10^7, decade ratios 0.888, 0.927, 0.947,
    0.959: a set whose density is positive by Erdos-Wagstaff's argument
    reads, at these widths, exactly the rising ratios the prime share does.

RUN RECORD. python prime/code/memwatch.py prime/code/explore_loose_floor.py:
17 checks, wall 6.8 s, peak working set 453 MB and peak commit 445 MB
against the 512 MB ceiling (the sieve, the flag array and the per-prime
columns to 10^8; numpy's temporaries above the 250 MB estimated).
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import math
import time

import numpy as np

CHECKS = 0
X = 10 ** 8
DECADES = [10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7, 10 ** 8]
DELTA = 1.0 - (1.0 + math.log(math.log(2.0))) / math.log(2.0)


def check(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)
    print("  ok  " + msg)


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def sieve(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if s[p]:
            s[p * p::p] = False
    return s


def ford_shape(x):
    lx = math.log(x)
    return lx ** (-DELTA) * math.log(lx) ** (-1.5)


def loose2_share(xc, kmin, primes_c):
    """The loose-at-2 share below xc with odd k >= kmin in the marking; kmin
    = 3 is the engine, kmin = 5 the wrong-marking control."""
    fl = np.zeros(xc + 1, dtype=bool)
    for r in primes_c:
        d = int(r) - 1
        if kmin * d > xc:
            break
        fl[kmin * d::2 * d] = True
    q = primes_c[primes_c >= 11]
    return int(np.count_nonzero(~fl[q - 1])), len(q)


def loose_by_divisors(L, primeset):
    """The primes p at which L + 1 is loose, by the cohort's divisors: the
    set of p | L with (p - 1) | L (2 included) whose exponent v_p(L) no cohort
    member r != L + 1 attains as v_p(r - 1). Trial factorization; small L."""
    fac = {}
    n = L
    d = 2
    while d * d <= n:
        while n % d == 0:
            fac[d] = fac.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        fac[n] = fac.get(n, 0) + 1
    divs = [1]
    for pp, e in fac.items():
        divs = [x * pp ** i for x in divs for i in range(e + 1)]
    cohort = [x for x in divs if x > 1 and x != L and (x + 1) in primeset]
    out = set()
    for pp, e in fac.items():
        if L % (pp - 1):
            continue
        if not any(v_p(x, pp) == e for x in cohort):
            out.add(pp)
    return out


def v_p(n, p):
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


def main():
    t0 = time.time()
    section("S0  THE SIEVE AND THE MARKINGS")
    is_p = sieve(X)
    primes = np.nonzero(is_p)[0]
    del is_p
    print("  primes to 10^8: %d  (%.1f s)" % (len(primes), time.time() - t0))

    flags = np.zeros(X + 1, dtype=np.uint8)
    for r in primes:
        d = int(r) - 1
        if 3 * d > X:
            break
        flags[3 * d::2 * d] |= 1          # forced at 2 by r: L = (r-1) k, k odd >= 3
    for r in primes:
        d = int(r) - 1
        if 2 * d > X:
            break
        if d >= 6:
            flags[2 * d::d] |= 2          # an odd cohort prime r >= 7 besides q
    print("  markings done  (%.1f s)" % (time.time() - t0))

    q = primes[primes >= 11]
    L = q - 1
    low = L & (-L)
    a = np.rint(np.log2(low)).astype(np.int64)
    fq = flags[L]
    loose2 = (fq & 1) == 0
    class8 = (a == 3) & (L % 3 != 0) & (L % 5 != 0) & ((fq & 2) == 0)

    section("S1  THE CONTROL (PR1)")
    xc = 10 ** 6
    pc = primes[primes <= xc]
    right_n, right_d = loose2_share(xc, 3, pc)
    wrong_n, wrong_d = loose2_share(xc, 5, pc)
    print("  marking with odd k >= 3 at 10^6: %d of %d loose at 2 (%.4f)" % (right_n, right_d, right_n / right_d))
    print("  marking with odd k >= 5 at 10^6: %d of %d loose at 2 (%.4f)" % (wrong_n, wrong_d, wrong_n / wrong_d))
    check(right_n != wrong_n, "the wrong marking changes the share: the comparison has teeth")
    expect = {10 ** 4: 0.0906, 10 ** 5: 0.0751, 10 ** 6: 0.0673, 10 ** 7: 0.0623}
    shares = {}
    for x in DECADES:
        sel = q <= x
        n_all = int(np.count_nonzero(sel))
        n_l2 = int(np.count_nonzero(loose2 & sel))
        shares[x] = (n_l2, n_all)
    for x in (10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7):
        n_l2, n_all = shares[x]
        check(round(n_l2 / n_all, 4) == expect[x],
              "loose-at-2 share below 10^%d is %.4f (three kills: %.4f)" % (round(math.log10(x)), n_l2 / n_all, expect[x]))
    sel9 = (q <= 10 ** 5) & (L % 16 == 8)
    n9 = int(np.count_nonzero(sel9))
    n9l = int(np.count_nonzero(sel9 & loose2))
    print("  q == 9 (mod 16) below 10^5: %d primes, %d loose at 2 (blind adams: 1196 primes, 476 loose at any prime)" % (n9, n9l))
    # the blind-adams figure counts looseness at ANY prime; settle the gap by
    # the divisor method itself, independent of the marking
    small = set(int(v) for v in primes[primes <= 10 ** 5 + 1])
    any_loose = 0
    two_loose = 0
    odd_only = []
    for qq in q[sel9]:
        qq = int(qq)
        kinds = loose_by_divisors(qq - 1, small)
        if kinds:
            any_loose += 1
        if 2 in kinds:
            two_loose += 1
        elif kinds:
            odd_only.append(qq)
    print("  by divisors: %d loose at any prime, %d loose at 2, odd-only: %s" % (any_loose, two_loose, odd_only))
    check((n9, any_loose, two_loose) == (1196, 476, n9l),
          "q == 9 (mod 16) below 10^5: 1196 primes, 476 loose at any prime, %d loose at 2 by both methods" % n9l)

    section("S2  THE FERMAT ZEROS (PR2): loose-at-2 count by a = v_2(q - 1)")
    print("  %-6s" % "a" + "".join("%12s" % ("<=10^%d" % round(math.log10(x))) for x in DECADES))
    amax = int(a.max())
    for aa in range(1, amax + 1):
        row = []
        for x in DECADES:
            row.append(int(np.count_nonzero(loose2 & (a == aa) & (q <= x))))
        if any(row):
            print("  %-6d" % aa + "".join("%12d" % c for c in row))
    for aa in (1, 2):
        check(int(np.count_nonzero(loose2 & (a == aa))) == 0, "no prime loose at 2 with v_2(q - 1) = %d" % aa)
    for aa in (4, 8, 16):
        who = q[loose2 & (a == aa)]
        check(len(who) == 1 and int(who[0]) == 2 ** aa + 1,
              "at v_2(q - 1) = %d exactly one loose prime to 10^8, the Fermat prime %d itself" % (aa, 2 ** aa + 1))
    for aa in (3, 5, 6, 7):
        check(int(np.count_nonzero(loose2 & (a == aa) & (q <= 10 ** 4))) > 0, "loose primes at a = %d exist below 10^4" % aa)

    section("S3  THE CONTAINMENT (PR3) AND THE FLOOR'S SIZE (PR4)")
    print("  %-8s %10s %10s %10s %10s %12s %12s" % ("x", "primes", "loose@2", "V=480", "excep.", "V=480/prim", "V=480/loose"))
    for x in DECADES:
        sel = q <= x
        n_all = int(np.count_nonzero(sel))
        n_l2 = int(np.count_nonzero(loose2 & sel))
        n_c8 = int(np.count_nonzero(class8 & sel))
        n_ex = int(np.count_nonzero(class8 & sel & ~loose2))
        print("  10^%-5d %10d %10d %10d %10d %12.4f %12.4f" % (round(math.log10(x)), n_all, n_l2, n_c8, n_ex, n_c8 / n_all, n_c8 / n_l2))
    check(int(np.count_nonzero(class8 & ~loose2)) == 0, "every prime with V(q) = 480 is loose at 2 (0 exceptions to 10^8)")
    ex = q[class8][:6]
    print("  the least members of the class: %s" % ", ".join(str(int(v)) for v in ex))
    check(int(ex[0]) == 137, "the least prime with V(q) = 480 is 137")

    section("S4  ONE DECADE FURTHER (PR5): the loose-at-2 share and its ratios")
    print("  %-8s %10s %10s %14s %14s %14s" % ("x", "share", "ratio", "Ford full", "pure power", "a=3 rel."))
    prev = None
    prev_x = None
    for x in DECADES:
        n_l2, n_all = shares[x]
        s = n_l2 / n_all
        sel3 = (q <= x) & (L % 16 == 8)
        rel3 = np.count_nonzero(sel3 & loose2) / np.count_nonzero(sel3)
        if prev is None:
            print("  10^%-5d %10.4f %10s %14s %14s %14.4f" % (round(math.log10(x)), s, "-", "-", "-", rel3))
        else:
            ff = ford_shape(x) / ford_shape(prev_x)
            pp = (math.log(x) / math.log(prev_x)) ** (-DELTA)
            print("  10^%-5d %10.4f %10.3f %14.3f %14.3f %14.4f" % (round(math.log10(x)), s, s / prev, ff, pp, rel3))
        prev, prev_x = s, x
    span_m = shares[10 ** 7][0] / shares[10 ** 7][1] / (shares[10 ** 4][0] / shares[10 ** 4][1])
    span_f = ford_shape(10 ** 7) / ford_shape(10 ** 4)
    print("  span 10^4..10^7: measured %.3f, Ford's shape %.3f" % (span_m, span_f))

    section("S5  THE INTEGER CONTROL (PR6): odd m with no proper divisor d, 8d + 1 prime")
    Y = X // 8
    im = np.zeros(Y + 1, dtype=bool)
    r9 = primes[primes % 16 == 9]
    for r in r9:
        d = (int(r) - 1) // 8
        if 3 * d > Y:
            break
        im[3 * d::2 * d] = True
    odd = np.arange(1, Y + 1, 2)
    unmarked = ~im[odd]
    print("  %-8s %12s %12s %10s %10s" % ("y", "odd m", "no divisor", "share", "ratio"))
    prev = None
    for y in (10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7):
        sel = odd <= y
        n_o = int(np.count_nonzero(sel))
        n_u = int(np.count_nonzero(unmarked & sel))
        s = n_u / n_o
        print("  10^%-5d %12d %12d %10.4f %10s" % (round(math.log10(y)), n_o, n_u, s, "-" if prev is None else "%.3f" % (s / prev)))
        prev = s

    section("SUMMARY")
    print("  %d checks passed; wall %.1f s" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
