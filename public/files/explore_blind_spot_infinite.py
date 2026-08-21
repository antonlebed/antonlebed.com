"""
explore_blind_spot_infinite.py -- is the probe's biggest blind spot
infinite? The class V = 24 of the transparency headroom, its prime part
characterized exactly (explore_headroom.py finding 7, explore_premium.py
finding 6) and filed as infinite only if the safe primes are -- the Sophie
Germain question. This file closes that by proof, with no conjecture in it.

THE QUESTION. A state of the self-growing tower is a modulus N; lambda(N)
is Carmichael's function; the wall W(L) is the largest modulus whose
lambda divides L,

    W(L) = (2 if L odd else 2^(v_2(L)+2)) * prod{ p^(v_p(L)+1)
             : p odd prime, (p-1) | L },

and the headroom of N is V(N) = W(lambda(N)) / N, the room a state has to
grow without moving its own dynamics. Two states with one headroom are
BLIND to the probe that reads it, and the biggest blind class in the
census is V = 24: 178 states below 6000, 101 of them prime. The prime
part is a rule, proved: a prime q > 5 has V(q) = 24 iff W(q-1) = 24 q,
iff no prime outside {2, 3, q} has its predecessor dividing q-1 and
3 does not divide q-1. Every safe prime q = 2r+1 with r >= 5 prime is in
it (its doors above lambda(q) = 2r are 3 and q alone), 81 of the 101; the
other 20 -- 239, 443, 647 leading -- have (q-1)/2 composite. The record
filed the class's infinitude as OPEN, with one identified route,
through the safe primes, conjecture-gated, and the non-safe family
unmapped. This file asks the question directly: is the class infinite?

THE CLASS IN DIVISOR TERMS (the criterion the rig runs on, derived by
hand and checked against W in S1). Write q - 1 = 2m. The cohort from the
empty state is {p : (p-1) | (q-1)} minus {2}; the class condition is that
this cohort is exactly {3, q} and 3 does not divide q-1, which forces
v_2(q-1) = 1 since 4 | q-1 would admit 5. So m is odd, 3 does not divide
m, and for every divisor d of 2m other than 1, 2 and 2m the number d+1 is
composite. An odd divisor d > 1 of 2m has d+1 even and at least 4, so it
never admits a prime; d = m is that case. So the whole condition is on
the EVEN proper divisors d = 2e with e | m, 1 < e < m:

    q in the class  <=>  m odd, 3 does not divide m, and 2e+1 is
                         composite for every divisor e of m with 1 < e < m.

When m is prime there is no such e and q is a safe prime; when m is
composite the condition is a finite list of compositeness demands.

THE HAND-ATTACK, on paper before any engine code, and it is a proof.

THEOREM (the blind-spot theorem). The primes q with V(q) = 24 are
infinite; their counting function is >> x / log^2 x. And the NON-SAFE
members -- those with (q-1)/2 composite -- are infinite by themselves,
>> x / log^2 x as well. No conjecture enters.

Proof. Let x be large, z = x^(1/10), and A = {(p-1)/2 : p <= x prime}.

Step 1 (a lower bound, the linear sieve). For squarefree d, the elements
of A divisible by d are the primes p <= x with p = 1 mod 2d, so the
sifting density is g(d) = 1/phi(2d), which is multiplicative and of
dimension 1 (g(2) = 1/2, g(p) = 1/(p-1) for odd p). The Bombieri-Vinogradov
theorem gives the remainders level D = x^(1/2) (log x)^(-B): for every
A > 0 there is B with sum over d <= D of max_(a,d)=1 |pi(x; d, a) -
li(x)/phi(d)| << x (log x)^(-A). The Rosser-Iwaniec linear sieve lower
bound (Friedlander-Iwaniec, Opera de Cribro, Theorem 11.12; f(s) =
2 e^gamma log(s-1)/s for 2 <= s <= 4, positive and increasing to 1 for
every s > 2) then gives, with s = log D / log z -> 5,

    S(A, z) = #{p <= x : (p-1)/2 has no prime factor < z}
            >= (f(5) - o(1)) li(x) prod_(p<z) (1 - g(p))  >>  x / log^2 x,

the product being ~ c / log z = 10c / log x by Mertens. Every m counted
is odd, prime to 3, and has at most 9 prime factors, all >= z.

Step 2 (the bad set, an upper bound). A counted q = 2m+1 fails the class
condition only through a divisor e of m with 1 < e < m and 2e+1 prime.
Put f = m/e; then e >= z and f >= z, both z-rough, and e f <= x/2. For
fixed f let y = x/(2f) >= z and w = min(z, y^(1/8)). The e counted satisfy
three conditions at once -- e, 2e+1 and 2ef+1 all free of prime factors
below w (e being z-rough, the other two being primes exceeding w) -- and
the Brun/Selberg upper-bound sieve of dimension 3 with sifting range
w <= y^(1/8) gives

    N_f = #{e <= y : e, 2e+1, 2ef+1 all w-rough}
        << y prod_(p<w) (1 - rho(p)/p),

where rho(p) counts the residues of e mod p hit by the three forms:
rho(2) = 1, and for odd p, rho(p) = 3 unless p | f (then 2ef+1 = 1 mod p,
rho = 2) or f = 1 mod p (the roots -1/2 and -1/(2f) coincide, rho = 2).
So the product is << (log w)^(-3) prod_(p | f(f-1)) (1 + 1/p)
<< (log w)^(-3) log log x. Since y >= z, log w >= (1/8) log z =
(log x)/80, so N_f << (x/f) (log log x) / log^3 x. Summing over the
z-rough f <= x/(2z),

    sum 1/f  <=  prod_(z <= p <= x) (1 - 1/p)^(-1)  ~  log x / log z  =  10,

so the bad set has size << x (log log x) / log^3 x = o(x / log^2 x).
With Step 1 the class has >> x / log^2 x members below x.

Step 3 (the non-safe members). Restrict Step 1 to the m with a prime
factor l in [z, x^(1/4)]: for each such prime l sift A_l = {m in A :
l | m}, density g(ld)/g(l), level D/l, s >= (1/2 - 1/4)/(1/10) = 2.5 > 2,
so S(A_l, z) >> li(x) / (l log x) uniformly (the remainders summed over
l and d are again within Bombieri-Vinogradov's level, with a divisor
function weight that the standard Cauchy-Schwarz step absorbs). Summing,
sum_(z <= l <= x^(1/4)) S(A_l, z) >> (x / log^2 x) sum 1/l >>
(x / log^2 x) log(10/4), counting each m at most 9 times. A counted m is
l times a z-rough cofactor, and the cofactor is 1 only when m = l itself,
which puts m <= x^(1/4): at most x^(1/4) of the counted m are prime, and
every other one is COMPOSITE. Step 2's bad-set bound applies unchanged,
so the non-safe members number >> x / log^2 x. QED.

What the theorem does NOT say: it gives no lower bound on the safe primes
themselves (the constants in Steps 1 and 3 are not explicit, so the safe
and the non-safe parts cannot be separated by subtraction), and it says
nothing about the 77 composite members, which lie outside the prime
characterization. What it closes is the question the record filed as
conjecture-gated: the biggest blind spot is infinite, and so -- by the
silence identity, SILENCE IS BLINDNESS -- is the silent set at the tower's
first even lambda, lambda = 2, which is this same class. The lift to every
even lambda, the same sieve on the cofactor (q-1)/lambda with the demands
lambda's even divisors add, is explore_silent_set.py's, with the census
per lambda; the lower bound here is a floor, and whether x / log^2 x is
the ORDER is open there.

A note on vocabulary: the suspicion arrived in the record's own terms
(safe primes, the Sophie Germain question), and the first move was to
rewrite the class condition in the divisor terms above, where its own
object -- a rough odd cofactor with a list of compositeness demands --
is what a sieve counts. The conjecture was the record's route and never
the class's.

WHAT THE RIG MEASURES. The theorem is proved; the rig's job is the
control that the divisor criterion IS the class, and a census of the
class at scales the earlier record never reached, read against what the
proof's mechanism predicts. Sieve of Eratosthenes to 10^7 with a
largest-prime-factor table to 5 * 10^6, bytearray
and array('I'), estimated under 40 MB before the run (the run record
below has the measured peak).

S1 THE CRITERION IS THE CLASS (control). For every prime q <= 10^5,
   the divisor criterion agrees with wall(q-1) == 24 q, the wall computed
   from its definition; and below 6000 the census reads 101 primes, 81
   safe, 20 not, the non-safe leading 239, 443, 647.
   PREDICTION P1: 0 disagreements; 101 / 81 / 20; 239, 443, 647.

S2 THE CENSUS BY DECADE. Class members below 10^4, 10^5, 10^6, 10^7, split
   safe / non-safe, with the ratio N(x) log^2 x / x printed.
   PREDICTION P2: the non-safe SHARE rises across the four decades (it is
   0.198 below 6000): the heuristic count of the m = r s members carries
   a sum over the smaller prime factor that grows like log log x against
   a safe-prime count of fixed order x / log^2 x.
   PREDICTION P3: N(x) log^2 x / x stays above 1 at every decade (the
   safe primes alone are near 1.3 x / log^2 x by the Hardy-Littlewood
   heuristic, which counts them as 2 C_2 x / log^2 x and is observed
   below that from below at these scales).

S3 THE MECHANISM. For z in {5, 11, 23, 47}: among primes q <= 10^7 with
   (q-1)/2 free of prime factors below z, the fraction NOT in the class
   (the bad set of Step 2), and a check that every bad one carries a
   proper divisor e with 2e+1 prime.
   PREDICTION P4: the bad fraction falls as z rises, and every bad q
   carries such an e (0 exceptions -- this is the criterion restated,
   so it is a control on the bookkeeping and not a finding).

S4 THE NON-SAFE MEMBERS. Their count by the number of prime factors of
   (q-1)/2 below 10^7, and the least member at each count.
   PREDICTION P5: members with three prime factors exist below 10^7.

WHAT WOULD KILL WHAT (observables). P1 dies on one printed disagreement
or a census figure off 101 / 81 / 20. P2 dies on one decade whose printed
share is below the decade before. P3 dies on one printed ratio at or
below 1. P4 dies on a printed bad fraction that rises between consecutive
z, or on one printed bad q with no such e. P5 dies on a printed count of
0 at three prime factors. None of them touches the theorem, whose proof
is above; a miss on P2, P3 or P5 would be a miss of a heuristic about
the CONSTANTS and would be recorded as that.

FINDINGS (from the printed run; 664,579 primes to 10^7, 71,419 class
members, 7 checks, wall 2.5-5 s, peak working set 72 MB under the memory
watch).

F1 THE CRITERION IS THE CLASS (control, P1 hit). Over every prime
   q <= 10^5 the divisor criterion and wall(q-1) == 24 q agree, 0
   disagreements; below 6000 the census reads 101 / 81 / 20 with the
   non-safe leading 239, 443, 647, 659, 827, 1223 -- the record's figures,
   reproduced from the criterion alone.

F2 THE CENSUS BY DECADE (P2 and P3 hit). Members below 10^4, 10^5, 10^6,
   10^7: 159, 1,133, 8,770, 71,419, of which 113, 668, 4,322, 30,655 are
   safe -- so the NON-SAFE SHARE rises 0.289, 0.410, 0.507, 0.571, and the
   non-safe members outnumber the safe ones from 10^6 on. N(x) log^2 x / x
   reads 1.349, 1.502, 1.674, 1.855, rising; the safe part alone reads
   0.959, 0.885, 0.825, 0.796, FALLING toward its Hardy-Littlewood
   constant from above at these scales rather than from below as the
   prediction had it -- a miss in the heuristic's direction, not in the
   theorem, and the ratio of the class is carried by the non-safe members.

F3 THE MECHANISM (P4 hit). Among primes q <= 10^7 with (q-1)/2 free of
   prime factors below z, the fraction outside the class is 0.570 at z = 5
   (166,214 rough, 94,795 bad), 0.390 at z = 11, 0.290 at z = 23, 0.191 at
   z = 47 (62,454 rough, 11,926 bad), falling with z as Step 2 has it; and
   every bad q carries a proper divisor e of (q-1)/2 with 2e+1 prime, 0
   exceptions. The proof's own z = x^(1/10) is 5.0 at x = 10^7, where the
   bad fraction is 0.57: the o(1) of Step 2 is asymptotic, and at this
   scale the class is 43% of the rough primes rather than almost all of
   them. Nothing here measures the constant.

F4 THE NON-SAFE MEMBERS (P5 hit). By the number of prime factors of
   (q-1)/2, with multiplicity, below 10^7: two, 33,664 (least 239); three,
   6,695 (least 6,959 = 2 * 7 * 7 * 71 + 1); four, 396 (least 93,983);
   five, 8 (least 900,719); six, 1 (9,215,039). Four have (q-1)/2 a prime
   power with exponent >= 2, 410,759 = 2 * 59^3 + 1 the least (the
   factorizations quoted here were re-derived after the run; the print
   names the members and not their factors).

RUN RECORD. The first run's S3 used a table built by slice-assigning each
prime over its multiples in increasing order, which leaves the LARGEST
prime factor in every cell; factor() is indifferent to that (dividing out
the largest prime repeatedly still yields the factorization, and S1's
control against the wall passed), but S3 read the table as the smallest
prime factor and so tested the wrong roughness, printing 664,529 "rough"
primes at z = 5 out of 664,579 and a bad fraction of 0.8925 flat across
z -- every check still passed, the print was what gave it away. The table
is now named for what it holds and S3 takes the least prime factor from
the factorization; the figures above are the corrected run's.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time
from array import array
from math import log

CAP = 10 ** 7
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

def sieve(n):
    """bytearray s with s[k] = 1 iff k is prime, k <= n."""
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(range(i * i, n + 1, i)))
    return s


def lpf_table(n):
    """LARGEST prime factor of every k <= n (0 for k < 2): each prime's
    slice overwrites the marks of the primes before it, so the table ends
    at the largest, which is all factor() needs -- dividing it out
    repeatedly still yields the whole factorization."""
    t = array("I", [0]) * (n + 1)
    for i in range(2, n + 1):
        if t[i] == 0:
            t[i::i] = array("I", [i]) * len(range(i, n + 1, i))
    return t


def factor(m, spf):
    """prime factorization of m as a list of (p, e)."""
    out = []
    while m > 1:
        p = spf[m]
        e = 0
        while m % p == 0:
            m //= p
            e += 1
        out.append((p, e))
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


def wall(L, isprime):
    """W(L) from its definition, for L with L+1 within the sieve."""
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


def in_class(q, spf, isprime):
    """the divisor criterion: q-1 = 2m, m odd, 3 does not divide m, and
    2e+1 composite for every divisor e of m with 1 < e < m."""
    m = (q - 1) // 2
    if m % 2 == 0 or m % 3 == 0:
        return False
    fac = factor(m, spf)
    for e in divisors_from(fac):
        if 1 < e < m and isprime[2 * e + 1]:
            return False
    return True


def bad_witness(q, spf, isprime):
    m = (q - 1) // 2
    for e in divisors_from(factor(m, spf)):
        if 1 < e < m and isprime[2 * e + 1]:
            return e
    return None


# ------------------------------------------------------------ the sections

def s1_control(isprime, spf):
    section("S1 THE CRITERION IS THE CLASS (control)")
    bad = []
    for q in range(7, 10 ** 5 + 1):
        if not isprime[q]:
            continue
        a = in_class(q, spf, isprime)
        b = (wall(q - 1, isprime) == 24 * q)
        if a != b:
            bad.append(q)
    ok(not bad, "P1: criterion vs wall(q-1) == 24q over primes q <= 10^5: "
       "%d disagreements %s" % (len(bad), bad[:5]))
    cls = [q for q in range(7, 6000) if isprime[q] and in_class(q, spf, isprime)]
    safe = [q for q in cls if isprime[(q - 1) // 2]]
    non = [q for q in cls if not isprime[(q - 1) // 2]]
    print("  below 6000: %d primes in the class, %d safe, %d not; non-safe "
          "leading %s" % (len(cls), len(safe), len(non), non[:6]))
    ok(len(cls) == 101 and len(safe) == 81 and len(non) == 20
       and non[:3] == [239, 443, 647], "P1: 101 / 81 / 20 and 239, 443, 647")


def s2_census(isprime, spf, members):
    section("S2 THE CENSUS BY DECADE")
    shares = []
    ratios = []
    for k in range(4, 8):
        X = 10 ** k
        cls = [q for q in members if q <= X]
        safe = sum(1 for q in cls if isprime[(q - 1) // 2])
        non = len(cls) - safe
        share = non / len(cls)
        ratio = len(cls) * log(X) ** 2 / X
        sratio = safe * log(X) ** 2 / X
        shares.append(share)
        ratios.append(ratio)
        print("  x = 10^%d: %d members, %d safe, %d not (share %.3f); "
              "N log^2 x / x = %.3f, safe part %.3f"
              % (k, len(cls), safe, non, share, ratio, sratio))
    ok(all(shares[i] < shares[i + 1] for i in range(3)),
       "P2: the non-safe share rises across 10^4..10^7: %s"
       % ["%.3f" % s for s in shares])
    ok(all(r > 1 for r in ratios),
       "P3: N log^2 x / x above 1 at every decade: %s"
       % ["%.3f" % r for r in ratios])


def s3_mechanism(isprime, spf, primes, memberset):
    section("S3 THE MECHANISM (the bad set of the proof's Step 2)")
    fracs = []
    noe = 0
    for z in (5, 11, 23, 47):
        rough = 0
        bad = 0
        for q in primes:
            if q < 7:
                continue
            m = (q - 1) // 2
            if min(p for p, _ in factor(m, spf)) < z:
                continue
            rough += 1
            if q not in memberset:
                bad += 1
                if bad_witness(q, spf, isprime) is None:
                    noe += 1
        frac = bad / rough if rough else float("nan")
        fracs.append(frac)
        print("  z = %2d: %7d primes q <= 10^7 with (q-1)/2 free of primes "
              "below z, %6d of them outside the class (fraction %.4f)"
              % (z, rough, bad, frac))
    ok(all(fracs[i] > fracs[i + 1] for i in range(3)),
       "P4: the bad fraction falls with z: %s" % ["%.4f" % f for f in fracs])
    ok(noe == 0, "P4: every bad q carries a proper divisor e of (q-1)/2 with "
       "2e+1 prime (%d without)" % noe)


def s4_nonsafe(isprime, spf, members):
    section("S4 THE NON-SAFE MEMBERS by the number of prime factors of (q-1)/2")
    by = {}
    for q in members:
        m = (q - 1) // 2
        fac = factor(m, spf)
        omega = sum(e for _, e in fac)
        if omega == 1:
            continue
        by.setdefault(omega, []).append(q)
    for omega in sorted(by):
        qs = by[omega]
        print("  Omega = %d: %d members below 10^7, least %s"
              % (omega, len(qs), qs[:4]))
    sq = [q for q in members if not isprime[(q - 1) // 2]
          and len(factor((q - 1) // 2, spf)) == 1]
    print("  among them, (q-1)/2 a prime power with exponent >= 2: %d, "
          "least %s" % (len(sq), sq[:4]))
    ok(len(by.get(3, [])) > 0, "P5: members with three prime factors exist "
       "below 10^7 (%d)" % len(by.get(3, [])))


def main():
    t0 = time.time()
    print("explore_blind_spot_infinite.py -- is the biggest blind spot "
          "infinite? (yes, by proof; the rig is the control and the census)")
    isprime = sieve(CAP)
    spf = lpf_table(CAP // 2 + 1)
    primes = [q for q in range(2, CAP + 1) if isprime[q]]
    print("  tables built: %d primes to 10^7, %.1f s" % (len(primes), time.time() - t0))
    members = [q for q in primes if q > 5 and in_class(q, spf, isprime)]
    print("  class members to 10^7: %d, %.1f s" % (len(members), time.time() - t0))
    s1_control(isprime, spf)
    s2_census(isprime, spf, members)
    s3_mechanism(isprime, spf, primes, set(members))
    s4_nonsafe(isprime, spf, members)
    print()
    print("  wall %.1f s" % (time.time() - t0))
    if FAILS:
        print("%d FAILED:" % len(FAILS))
        for f in FAILS:
            print("  " + f)
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
