"""
explore_blind_adams.py -- the transparency wall as Adams' number, and what
the blind class reads that the Bernoulli denominator does not.

THE QUESTION. The transparency wall W(L) is the largest modulus n with
lambda(n) | L, lambda the Carmichael function: 2 for odd L, and for even
L the product of 2^(v_2(L)+2) with p^(v_p(L)+1) over the odd primes p
with (p - 1) | L. Its closed form at even L, W(L) = denominator(B_L / 2L),
was verified against Bernoulli numbers computed from scratch and read as
an arithmetic coincidence with the order of the image of the
J-homomorphism. Two questions are asked of that reading.

  Q1. Is the coincidence a definition? Adams' number m(t) is the greatest
      common divisor over k of k^N (k^t - 1), N large -- equivalently the
      largest m such that a^t == 1 (mod m) for every a coprime to m. That
      condition on m is exactly lambda(m) | t, so m(t) and W(t) are one
      integer by definition, and the Bernoulli closed form at even t is
      Adams' theorem (J(X) II, 1965; Milnor-Stasheff, Appendix B) rather
      than a fact found here. The test is the gcd computed directly.
  Q2. For a prime q, the sighted probe's whole reading of q is its
      headroom V(q) = W(q - 1) / q, and its Bernoulli shadow is
      D(q) = denominator(B_{q-1}) / q, the product of the odd primes p != q
      with (p - 1) | (q - 1) times 2 (von Staudt-Clausen). Does either
      determine the other? V -> D is the radical, a function. D -> V
      forgets the exponents v_p(q - 1); the question is whether the
      exponents are nonetheless forced by the cohort, or whether a
      positive share of the primes carry a headroom their denominator
      does not fix.

PREDICTIONS, fixed before the run.
  P1. W(L) == gcd_k k^N (k^L - 1) == denominator(B_L / 2L) at every even
      L <= 200, and W(L) == gcd == 2 at every odd L <= 200. A single
      inequality would mean the wall is NOT Adams' number and the reading
      "coincidence" was right.
  P2. rad(V(q)) == D(q) at every prime 11 <= q <= 10^5 (the radical takes
      2^(v_2+2) to 2 and p^(v_p+1) to p).
  P3. D does not determine V: the primes q whose V(q) exceeds the LEAST
      LIFT of D -- V_min(D) = 2^(2+e_2) prod_{p in D odd} p^(1+e_p), with
      e_p = max over r in D of v_p(r - 1), the smallest headroom any prime
      with that cohort can carry -- are a positive share, at least a
      tenth, flat or rising from 10^4 to 10^5. The hand-derived witness
      is the pair q = 29 and q = 137: both cohorts are {2, 3, 5, q}, so
      D = 30 for both, while v_2(28) = 2 and v_2(136) = 3 give V = 240
      against 480. The 2-adic exponent is read by the cohort only through
      5 (4 | q - 1) and 17 (16 | q - 1); nothing in the cohort separates
      8 | q - 1 from 4 || q - 1, so the residue class q == 9 (mod 16) is
      already an eighth of the primes with an unforced exponent unless
      a cohort member r == 1 (mod 8) forces it.
      (P3 was first stated on the least V in the sample's D-fibre. That
      statistic is a function of the sample and not of D -- fibres go
      singleton as x grows, and a singleton fibre "determines" V
      vacuously -- and it printed a FALLING share, 0.074 at 10^4 and
      0.043 at 10^5, failing its own band. The print is kept below as
      the record of the wrong instrument; the least lift is the function
      the question asks about.)

KILLS, as prints. Q1 dies (the coincidence reading stands) on any
inequality in S1. Q2's hypothesis -- that the blind classes are the fibres
of the Bernoulli map -- dies on P3 holding: the classes are the fibres of
L -> W(L), Adams' number, of which the Bernoulli denominator is the
radical.

POSITIVE CONTROL. The Bernoulli numbers are computed from scratch by the
recurrence and their denominators at 2k = q - 1 are checked against the
von Staudt-Clausen product for every prime q <= 200 before D is trusted
at 10^5; the gcd is computed at two exponents N and two ranges of k and
must agree.

FINDINGS (one run).
  F1 (P1 held; property, the wall's definition is Adams'). At every
      L <= 200, W(L) equals gcd_k k^N (k^L - 1) at both (N, K) = (20, 60)
      and (40, 120), and at even L equals denominator(B_L / 2L), 0
      mismatches: 24, 240, 504, 480, 264, 65520 at L = 2..12,
      138181680 at 36, 6666000 at 100, 546612000 at 200. The wall is
      Adams' number m(L) verbatim -- "lambda(m) | L" and "a^L == 1 (mod m)
      for every unit a" are the same condition -- so its Bernoulli
      closed form and its match with the order of the image of J are
      Adams' theorem, not a coincidence found here.
  F2 (P2 held; property). rad(V(q)) = D(q) at all 9588 primes
      11 <= q <= 10^5; the control held at 42/42 primes q <= 201.
  F3 (P3 half held, half refuted; observation). D does not determine V:
      888 of the 9588 primes below 10^5 carry a headroom above the least
      lift of their denominator (V(29) = 240 against V(137) = 480 at
      D = 30 both), 720 of them loose at the prime 2, and 476 of the
      1196 primes q == 9 (mod 16) are loose. The share is positive at
      every range read and FALLING: 0.117 below 10^4, 0.093 below 10^5,
      against the prediction of a tenth or more, flat or rising. The
      reading: an exponent v_p(q - 1) is unforced only while q - 1 has
      no divisor r - 1 with p^j | r - 1 for a prime r, and integers with
      no divisor of shifted-prime form thin out slowly (Ford's
      shifted-prime-divisor theorem gives that thinning for the integers
      at rate (log y)^(-0.086)), so the blind classes are the fibres of
      the Adams map L -> m(L), of which the Bernoulli denominator is the
      radical, and the two maps agree on a share of the primes tending
      to 1 as slowly as that theorem allows. Whether the loose share
      goes to 0 is not proved here.

RUN. python explore_blind_adams.py (under a second, well under 512 MB).
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
from fractions import Fraction
from math import comb, gcd

L_MAX = 200
Q_MAX = 100_000


def ok(cond, msg):
    print(("  ok    " if cond else "  FAIL  ") + msg)
    if not cond:
        sys.exit(1)


def section(t):
    print("\n== " + t)


def sieve(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return s


def v_p(n, p):
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def wall(L, isprime):
    """The largest n with lambda(n) | L, by the definition."""
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


def adams(t, N, K):
    """gcd over 2 <= k <= K of k^N (k^t - 1)."""
    g = 0
    for k in range(2, K + 1):
        g = gcd(g, k ** N * (k ** t - 1))
    return g


def bernoulli(nmax):
    """B_0 .. B_nmax exactly, B_1 = -1/2, by the recurrence."""
    B = [Fraction(0)] * (nmax + 1)
    B[0] = Fraction(1)
    for n in range(1, nmax + 1):
        s = sum(comb(n + 1, k) * B[k] for k in range(n))
        B[n] = -s / (n + 1)
    return B


def cohort(q, isprime):
    """The odd primes p != q with (p - 1) | (q - 1)."""
    L = q - 1
    out = set()
    d = 1
    while d * d <= L:
        if L % d == 0:
            for dd in {d, L // d}:
                p = dd + 1
                if p > 2 and p != q and isprime[p]:
                    out.add(p)
        d += 1
    return out


def rad(n):
    r = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            r *= p
            while n % p == 0:
                n //= p
        p += 1
    return r * n if n > 1 else r


def s1(isprime):
    section("S1  W(L) against Adams' gcd and the Bernoulli denominator, L <= %d" % L_MAX)
    B = bernoulli(L_MAX)
    bad = []
    for L in range(1, L_MAX + 1):
        W = wall(L, isprime)
        a1 = adams(L, 20, 60)
        a2 = adams(L, 40, 120)
        if a1 != a2:
            bad.append((L, "gcd unstable", a1, a2))
        if L % 2:
            if not (W == a1 == 2):
                bad.append((L, W, a1, 2))
        else:
            d = (B[L] / (2 * L)).denominator
            if not (W == a1 == d):
                bad.append((L, W, a1, d))
    print("  L      W(L)    gcd_k k^N(k^L-1)   denom(B_L/2L)")
    for L in (2, 4, 6, 8, 10, 12, 14, 36, 100, 200):
        print("  %-4d %10d %10d %14d" % (L, wall(L, isprime), adams(L, 20, 60),
                                      (B[L] / (2 * L)).denominator))
    print("  mismatches at L <= %d: %d" % (L_MAX, len(bad)), bad[:5])
    ok(not bad, "P1: the wall is Adams' number at every L <= %d, and its Bernoulli form is his theorem" % L_MAX)
    return B


def s2(isprime, B):
    section("S2  the blind class V(q) against its Bernoulli shadow D(q), q <= %d" % Q_MAX)
    # control: the cohort product equals the Bernoulli denominator at q <= 200
    ctrl = 0
    for q in range(11, L_MAX + 2):
        if isprime[q]:
            D = 2 * q
            for p in cohort(q, isprime):
                D *= p
            ctrl += (B[q - 1].denominator == D)
    n_small = sum(1 for q in range(11, L_MAX + 2) if isprime[q])
    ok(ctrl == n_small, "control: denom(B_{q-1}) equals the cohort product at %d/%d primes q <= %d" % (ctrl, n_small, L_MAX + 1))

    primes = [q for q in range(11, Q_MAX + 1) if isprime[q]]
    V = {}
    D = {}
    for q in primes:
        V[q] = wall(q - 1, isprime) // q
        d = 2
        for p in cohort(q, isprime):
            d *= p
        D[q] = d
    radfail = sum(1 for q in primes if rad(V[q]) != D[q])
    print("  primes 11 <= q <= %d: %d" % (Q_MAX, len(primes)))
    print("  rad(V(q)) != D(q): %d" % radfail)
    ok(radfail == 0, "P2: V -> D is the radical, a function")

    fibre_min = {}
    for q in primes:
        fibre_min[D[q]] = min(fibre_min.get(D[q], V[q]), V[q])
    print("  witness: V(29) = %d, V(137) = %d, D(29) = %d, D(137) = %d" % (V[29], V[137], D[29], D[137]))
    shares = []
    for x in (10_000, 100_000):
        ps = [q for q in primes if q <= x]
        loose = sum(1 for q in ps if V[q] > fibre_min[D[q]])
        multi = sum(1 for q in ps if len({V[r] for r in ps if D[r] == D[q]}) > 1) if x <= 10_000 else None
        shares.append(loose / len(ps))
        print("  x = %6d: %5d primes, %5d with V above their D-fibre's least V (%.3f)%s" % (
            x, len(ps), loose, loose / len(ps),
            "" if multi is None else ", %d in a fibre carrying two or more V (%.3f)" % (multi, multi / len(ps))))
    print("  (the fibre's least V is a function of the sample, not of D; the band is read on the least lift below)")

    # the least lift of D: the smallest V any prime with cohort D can carry
    def least_lift(d):
        odd, m, p = [], d // 2, 3
        while p * p <= m:
            if m % p == 0:
                odd.append(p)
                while m % p == 0:
                    m //= p
            p += 2
        if m > 1:
            odd.append(m)
        e2 = max([v_p(r - 1, 2) for r in odd] + [1])
        lift = 2 ** (2 + e2)
        for p in odd:
            ep = max([v_p(r - 1, p) for r in odd] + [0])
            lift *= p ** (1 + ep)
        return lift

    lifts = {d: least_lift(d) for d in set(D.values())}
    shares = []
    for x in (10_000, 100_000):
        ps = [q for q in primes if q <= x]
        loose = [q for q in ps if V[q] > lifts[D[q]]]
        at2 = sum(1 for q in loose if v_p(V[q], 2) > v_p(lifts[D[q]], 2))
        shares.append(len(loose) / len(ps))
        print("  x = %6d: %5d primes, %5d with V above the least lift of D (%.3f), %d of them loose at 2" % (
            x, len(ps), len(loose), len(loose) / len(ps), at2))
    nine = [q for q in primes if q % 16 == 9]
    nine_loose = sum(1 for q in nine if V[q] > lifts[D[q]])
    print("  q == 9 (mod 16): %d primes, %d with V above the least lift (%.3f)" % (len(nine), nine_loose, nine_loose / len(nine)))
    held = shares[1] >= 0.10 and shares[1] >= shares[0] - 0.01
    print("  P3 (predicted at least 0.10, flat or rising): %.3f at 10^4, %.3f at 10^5 -> %s"
          % (shares[0], shares[1], "held" if held else "REFUTED in trend: positive, and falling"))


def main():
    isprime = sieve(Q_MAX + 1)
    B = s1(isprime)
    s2(isprime, B)
    print("\nrun complete; P1 and P2 are asserted, P3 is read off its print")


if __name__ == "__main__":
    main()
