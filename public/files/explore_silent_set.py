"""
explore_silent_set.py -- is the silent set infinite at EVERY even lambda?
The blind-spot theorem (explore_blind_spot_infinite.py) proves the
probe's biggest blind class, V = 24, infinite by a sieve, and the silence
identity (explore_premium.py finding 10) makes that class the silent set
at the tower's first even lambda. The record left one level below it open:
whether the same sieve lifts to every even lambda. This file closes that
by proof, and corrects a sentence the record carried on the way.

THE SETTING. A state of the self-growing tower is a modulus N; lambda(N)
is Carmichael's function; the wall W(L) is the largest modulus whose
lambda divides L,

    W(L) = (2 if L odd else 2^(v_2(L)+2)) * prod{ p^(v_p(L)+1)
             : p odd prime, (p-1) | L },

the DOORS of L being the primes p with (p-1) | L, and the headroom of N
is V(N) = W(lambda(N)) / N. A fresh prime q at a state of lambda L -- its
door shut, (q-1) not dividing L -- is SILENT there when the wall grows by
exactly q, W(lcm(L, q-1)) = q * W(L): the import moves lambda and leaves
the headroom untouched. The silence identity: when L | q-1 the lcm is
q-1 and silence reads W(q-1) = q * W(L), which divided by q is
V(q) = W(L), membership in the probe's blind class of the wall. At L = 2
every odd prime has L | q-1, so the whole silent set is the class V = 24.

THE CORRECTION, found while freezing the slate. The record stated the
identity without its qualifier -- "the primes silent at lambda are the
members of the blind class V = W(lambda)" -- where the rig that proved it
restricts to L | q-1. Off that restriction silence is WIDER than the
class: at L = 12 the prime 83 has lcm(12, 82) = 492 and W(492) =
16 * 9 * 5 * 7 * 13 * 83 = 83 * W(12), so 83 is silent, while V(83) = 24
and W(12) = 65520. Unfolded in general, q is silent at L iff
v_2(q-1) <= v_2(L), v_p(q-1) <= v_p(L) at every odd door p of L, and
every divisor d of lcm(L, q-1) with d not dividing L and d+1 prime is
d = q-1. The class is the sub-case L | q-1; the off-class silent primes
only ADD to the silent set, so proving the class's prime part infinite
proves the silent set infinite, and the identity of QUESTIONS the record
drew ("is the silent set infinite" IS "is the class infinite") holds in
the one direction the theorem needs.

THE CLASS IN DIVISOR TERMS (the criterion the rig runs on, derived by
hand and checked against W in S1). Let L be even and q = L m + 1 prime.
Then V(q) = W(L) iff

    (a) m is odd                      [v_2(q-1) = v_2(L)]
    (b) p does not divide m for every odd door p of L   [no bump]
    (c) m > 1                         [m = 1 makes q a door of L already]
    (d) every divisor d of L m with d not dividing L and d < L m has
        d+1 composite                 [the cohort is {q} alone].

Every such d is e * f with e = gcd(d, L) | L and f = d/e | m, f > 1; for
ODD e the number e f + 1 is even and at least 4, composite for free. So
(d) is a finite list of demands on the EVEN divisors e of L:

    e f + 1 composite for every even e | L and every f | m with f > 1,
    e f not dividing L, (e, f) != (L, m).

At L = 2 the even divisor is e = 2 and the list is the blind-spot
theorem's: 2f + 1 composite for every divisor f of m with 1 < f < m.

THE HAND-ATTACK, on paper before any engine code, and it is a proof.

THEOREM (the silent-set theorem). For every even L the primes q = 1
(mod L) with V(q) = W(L) number >> x / log^2 x below x, the implied
constant depending on L; those with (q-1)/L COMPOSITE are >> x / log^2 x
by themselves; and so the silent set at every even lambda is infinite.
At L = 2 this is the blind-spot theorem. No conjecture enters.

Proof. Let x be large, z = x^(1/10), A = {(q-1)/L : q <= x prime,
q = 1 mod L}.

Step 1 (a lower bound, the linear sieve). For squarefree d the elements
of A divisible by d are the primes q <= x with q = 1 mod L d, so relative
to X = li(x)/phi(L) the sifting density is g(d) = phi(L)/phi(L d):
g(p) = 1/(p-1) for p not dividing L and g(p) = 1/p for p | L,
multiplicative and of dimension 1. The Bombieri-Vinogradov theorem
controls the remainders at moduli L d <= x^(1/2) (log x)^(-B), each
modulus being hit by one d, so the level is D = x^(1/2)/(L (log x)^B)
and s = log D / log z -> 5. The Rosser-Iwaniec linear sieve lower bound
(Friedlander-Iwaniec, Opera de Cribro, Theorem 11.12; f(s) > 0 for
s > 2) gives

    S(A, z) = #{q <= x prime, q = 1 mod L, (q-1)/L free of primes < z}
            >= (f(5) - o(1)) X prod_(p<z) (1 - g(p))  >>_L  x / log^2 x,

the product being of order 1/log z by Mertens. Every m counted is
z-rough: odd, coprime to every door of L (all of them at most L+1 < z),
at least z but for the one element m = 1, with at most 9 prime factors.
So (a), (b), (c) hold for all but that one element.

Step 2 (the bad set, an upper bound). A counted q fails (d) only through
an even e | L and an f | m, f > 1, with e f + 1 prime and (e, f) != (L, m);
gcd(m, L) = 1 makes e f not divide L automatic. Case f < m: put g = m/f,
so f and g are both z-rough and at least z. Fix e and g, let y = x/(L g)
>= z and w = min(z, y^(1/8)). The f counted have f, e f + 1 and
L g f + 1 all w-rough (the last two being primes above w), and the
Brun/Selberg upper-bound sieve of dimension 3 gives

    #{f <= y : f, e f + 1, L g f + 1 all w-rough}
        << y prod_(p<w) (1 - rho(p)/p),

rho(p) counting the residues of f mod p hit by the three forms: rho(2) = 1,
and for odd p, rho(p) = 3 unless p | e L g or p | (L g - e), where two
roots coincide and rho(p) = 2 (L g != e, since g >= z > L). The product
is << (log w)^(-3) prod_(p | e L g (L g - e)) (1 + 1/p) << (log w)^(-3)
log log x, and log w >= (log x)/80, so the count is
<< (x/(L g)) (log log x) / log^3 x. Summing over the z-rough g <= x/(L z),
sum 1/g <= prod_(z <= p <= x) (1 - 1/p)^(-1) ~ 10, and over the even
e | L, at most tau(L) of them: << x (log log x) / log^3 x. Case f = m,
e < L: m, e m + 1 and L m + 1 all z-rough, the same sieve at y = x/L with
roots 0, -1/e, -1/L, distinct off p | e L (L - e): << x (log log x) /
log^3 x again. So the bad set is o(x / log^2 x) and the class has
>>_L x / log^2 x prime members below x.

Step 3 (the composite cofactors). Restrict Step 1 to the m with a prime
factor l in [z, x^(1/4)]: for each such l sift A_l = {m in A : l | m},
density g(l d)/g(l), level D/l, s >= 2.5 > 2, so S(A_l, z) >> X/(l log z)
uniformly (the remainders summed over l and d are within
Bombieri-Vinogradov's level, with a divisor-function weight the standard
Cauchy-Schwarz step absorbs). Summing over l, sum 1/l >> log(10/4), each
m counted at most 9 times; m = l itself only for m <= x^(1/4), at most
x^(1/4) of them, and every other m counted is composite. Step 2 applies
unchanged. QED.

What the theorem does NOT say. It gives no upper bound, and the census at
L = 2 (N log^2 x / x reading 1.35, 1.50, 1.67, 1.85 across 10^4..10^7)
says the lower bound may not be the order: a member q = L f r + 1 with f
a small admissible cofactor contributes of order x/(f log^2 x), and
whether sum 1/f over admissible f converges is a divisor-correlation
question this file does not settle. It says nothing about the composite
states of a class, nothing about the order of the off-class silent
primes, and at an ODD lambda there is nothing to say: the silent set is
empty there (the wall's 2-part jumps from 2 to at least 8), which is the
record's premium-at-least-4 clause.

WHAT THE RIG MEASURES. The theorem is proved; the rig's job is the control
that the divisor criterion IS the class, the correction's census, and the
class census per lambda at scales the earlier records never reached, read
against what the proof's mechanism predicts. Sieve of Eratosthenes to
10^7 with a largest-prime-factor table to 10^7, bytearray and array('I'),
estimated under 100 MB and under five minutes before the run (the run
record below has the measured figures). The sweep runs over the even
lambda-VALUES to 60 -- the L with lambda(W(L)) = L, the only L a state
has (14, 26, 34, 38 and 50 are even and are not values: no door realizes
their odd prime) -- though the theorem holds for every even L.

S1 THE CRITERION IS THE CLASS (control). For every L in the sweep and
   every prime q = 1 mod L, q <= 10^5, the divisor criterion agrees with
   wall(q-1) == q * wall(L), the wall computed from its definition; at
   L = 2 the census below 6000 reads 101 / 81 / 20, the record's figures.
   PREDICTION P1: 0 disagreements at every L; 101 / 81 / 20 at L = 2.

S2 THE CORRECTION'S CENSUS. For every L in the sweep and every fresh
   prime q <= 10^5 (door shut), silence from its definition,
   wall(lcm(L, q-1)) == q * wall(L), split by whether L | q-1: the class
   part must match the criterion exactly; the off-class part is counted,
   its least member printed, and gcd(q-1, L) tallied over it.
   PREDICTION P2: the class part matches the criterion, 0 exceptions, at
   every L; the off-class count is 0 at L = 2 and positive at every
   other L in the sweep, the least off-class member being 83 at L = 12
   (the hand witness) and 23 at L = 4.
   S2b (added to the design after S2 first printed, frozen from a hand
   derivation before its engine was written). What an off-class silent
   prime IS: with g = gcd(q-1, L), silence forces v_p(q-1) = v_p(g) at
   every door p of L and at 2, and every door of q-1 other than q to be a
   door of L dividing q-1, hence of g; so W(q-1) = q * W(g), that is
   V(q) = W(gcd(q-1, L)). SILENCE IS BLINDNESS in this form: every prime
   silent at L is a member of the blind class of the wall of the part of
   L it shares, and of the class V = W(L) exactly when L | q-1. The
   converse fails -- 11 has V = 24 = W(gcd(10, 8)) and is not silent at
   8, since 8 * 5 + 1 = 41 is prime -- so blindness to W(g) is necessary
   and not sufficient.
   PREDICTION P2b: V(q) = W(gcd(q-1, L)) for every silent prime q <= 10^5
   at every L in the sweep, 0 exceptions; 11 is not silent at L = 8.

S3 THE CENSUS BY LAMBDA. For every L in the sweep: class members below
   10^5, 10^6, 10^7, split by whether (q-1)/L is prime, the composite
   share by decade, and N_L(x) phi(L) log^2 x / x at 10^7 -- phi(L) being
   the factor the proof's main term carries, the rest of the L-dependence
   a sieve product and the door demands, both of order 1.
   PREDICTION P3: at L = 2 the figures are the blind-spot record's
   (8,770 and 71,419 members, 4,322 and 30,655 with (q-1)/2 prime).
   PREDICTION P4: the composite share rises 10^5 -> 10^6 -> 10^7 at every
   L <= 24 in the sweep (the heuristic count of the composite cofactors
   carries a sum over the smaller prime factor that grows like log log x
   against a prime-cofactor count of fixed order).
   PREDICTION P5: N_L(10^7) phi(L) log^2 x / x lies in [0.5, 4] at every L
   in the sweep.
   S3b (added to the design after S3 first printed, from the hand
   heuristic below). The two L-dependences the proof names, separated:
   the DOOR PRODUCT D(L) = prod over the odd doors p of L of (1 - 1/p) if
   p | L and (1 - 1/(p-1)) otherwise -- the chance that m = (q-1)/L avoids
   p, since q = 1 mod L puts q = 1 mod p already when p | L and leaves q
   uniform on the nonzero residues otherwise; 2 costs nothing beyond
   phi(L), m being odd exactly when v_2(q-1) = v_2(L) -- and the residual
   ratio / D, read against the EVEN-DIVISOR count of L, which is the
   number of compositeness demands a composite cofactor meets. Printed
   per L and summarized by the even-divisor count; no prediction frozen.

S4 THE MECHANISM. For L in {2, 4, 6, 12} and z in {5, 11, 23, 47}: among
   primes q = 1 mod L below 10^7 with (q-1)/L free of prime factors below
   z, the fraction NOT in the class (the bad set of Step 2), and a check
   that every bad one carries an even e | L and an f | m with e f + 1
   prime.
   PREDICTION P6: the bad fraction falls as z rises at every one of the
   four L, and every bad q carries such a pair (0 exceptions -- the
   criterion restated, a control on the bookkeeping).

WHAT WOULD KILL WHAT (observables). P1 dies on one printed disagreement
or a census figure off 101 / 81 / 20. P2 dies on one printed class-part
mismatch, a printed off-class count of 0 at some L > 2 or above 0 at
L = 2, or a least member other than 83 at L = 12 or 23 at L = 4. P2b dies
on one printed silent q with V(q) != W(gcd(q-1, L)), or on 11 printing as
silent at L = 8. P3 dies
on a printed L = 2 figure off the record's. P4 dies on one decade pair at
one L <= 24 whose printed share does not rise. P5 dies on one printed
ratio outside [0.5, 4]. P6 dies on a printed bad fraction that rises
between consecutive z at some L, or on one printed bad q with no pair.
None of them touches the theorem, whose proof is above; a miss on P4 or
P5 would be a miss of a heuristic about the CONSTANTS and would be
recorded as that.

FINDINGS (from the printed run; 664,578 odd primes to 10^7, 25 even
lambda-values to 60, 12 checks of which 10 controls and 2 predictions,
wall 7.5 s, peak working set 92.5 MB under the memory watch).

F1 THE CRITERION IS THE CLASS (control, P1 hit). Over every prime
   q = 1 mod L, q <= 10^5, at every one of the 25 lambda-values the
   divisor criterion and wall(q-1) == q * wall(L) agree, 0 disagreements;
   at L = 2 below 6000 the census reads 101 / 81 / 20.

F2 THE CORRECTION'S CENSUS (P2 and P2b hit). Silence from its definition
   over the fresh primes below 10^5: at L = 2 the 1,133 silent primes are
   the class, 0 off it; at every other L the OFF-CLASS silent primes are
   the MAJORITY -- 820 of 1,262 at L = 4 (least 23), 588 of 1,066 at
   L = 6 (59), 1,011 of 1,168 at L = 8 (29), 914 of 1,049 at L = 12
   (83, the hand witness), 732 of 779 at L = 24, 449 of 456 at L = 60
   (least 839, the class part 7) -- from 55% at L = 6 to 98% at L = 60.
   The class part matches the criterion at every q with L | q-1, 0
   mismatches. What the off-class primes are: V(q) = W(gcd(q-1, L)) at
   every silent q at every L, 0 exceptions, and gcd(q-1, L) = 2 is the
   commonest value everywhere (820 of 820 at L = 4; 393 of 914 at L = 12
   against 229 at gcd 4 and 292 at gcd 6), so most primes silent at a
   state are members of the first class, V = 24, carrying the extra
   demands L's even divisors add. 11 is not silent at L = 8.

F3 THE CENSUS BY LAMBDA (P3 hit; P4 missed at L = 24; P5 missed at
   L = 48 and 60). Class members below 10^7 with the prime-cofactor
   count: L = 2, 71,419 (30,655); L = 4, 24,877 (16,195); L = 6, 27,720
   (20,535); L = 8, 9,187 (7,178); L = 10, 14,859 (9,266); L = 12, 8,303
   (7,962); L = 22, 6,706 (3,772); L = 24, 3,035 (3,018); L = 48, 1,130
   (1,130); L = 60, 1,018 (1,018). The composite-cofactor share at 10^7
   runs from 0.571 at L = 2 down to 0.000 at L = 48 and 60, and it falls
   with the number of EVEN DIVISORS of L -- every demand e f + 1
   composite is one more condition on a composite cofactor's divisors --
   so the multiples of 12 read 0.041, 0.006, 0.007, 0.000, 0.000 (L = 12,
   24, 36, 48, 60) while L = 22, 46, 58, with even divisors 2 and L
   alone, read 0.438, 0.369, 0.413 beside L = 2's 0.571. At L = 24 the
   share is 0.000, 0.000, 0.006 across the three decades, flat where P4
   had it rising: the heuristic counted the cofactors and not the
   demands on them, a miss about the constants at this scale and not
   about the theorem, whose Step 3 is asymptotic. N phi(L) log^2 x / x at
   10^7 runs from 1.855 (L = 2) and 1.778 (L = 58) down to 0.470 (L = 48)
   and 0.423 (L = 60), falling with the DOORS of L -- each door p is a
   prime the cofactor must avoid, a factor (1 - 1/(p-1)) in the sieve's
   product -- L = 60 carrying eight (2, 3, 5, 7, 11, 13, 31, 61) against
   L = 2's two. Neither count alone orders the table: L = 32 with four
   doors (2, 3, 5, 17) reads 0.670 below L = 12 with five (2, 3, 5, 7,
   13) at 0.863. Separated (S3b), the two dependences read apart: the
   door product D -- (1 - 1/p) for a door p | L, (1 - 1/(p-1))
   otherwise, over the odd doors -- puts L = 12 at 0.382 above L = 32 at
   0.352, 3 dividing 12 and costing 2/3 there against 1/2 at 32; and the
   residual ratio / D falls with the even-divisor count at every step of
   its mean, 3.71 at one even divisor (L = 2), 3.35 at two, 2.30 at
   three, 2.27 at four, 1.91 at five, 1.65 at six, 1.26 at eight, the
   ranges at three and four overlapping (2.05..2.55 against 1.71..2.63).
   The band [0.5, 4] was written before the doors were weighed and
   missed by 0.03 and 0.08 at its floor. The L-dependence beyond phi(L)
   is the door product times a factor falling with the even-divisor
   demands, in the directions the proof's product and demand list name
   -- a heuristic about the constants and not the theorem.

F4 THE MECHANISM (P6 hit). Among primes q = 1 mod L below 10^7 with
   (q-1)/L free of prime factors below z, the fraction outside the class
   at z = 5, 11, 23, 47: L = 2, 0.570, 0.390, 0.290, 0.191; L = 4, 0.701,
   0.521, 0.403, 0.295; L = 6, 0.750, 0.600, 0.474, 0.388; L = 12, 0.850,
   0.760, 0.672, 0.604 -- falling with z at every L as Step 2 has it, and
   higher at the L with more demands. Every bad q carries an even e | L
   and an f | m with e f + 1 prime, or a door of L dividing m (65,816 of
   the latter, each at a door not below z since m is z-rough -- 7 at
   L = 6, and 5, 7, 13 at L = 12, which a z of 5 does not sift), 0
   without.

RUN RECORD. The first run's P6 pair check looked only for the demand
(d) and printed 1 bad q with no pair -- q = 43 at L = 6, whose cofactor
7 is a door of L and is killed by the bump rule (b); the check now
accepts either witness and tallies the bumps. The same run printed P4
and P5 as failures; both are predictions about the constants, so the rig
now separates controls (a miss is a FAIL) from predictions (a miss is
printed, counted, and recorded above), and the final line says which.
S2b was added to the design after S2 first printed and before its engine
was written. Estimate before the run: under five minutes and 100 MB;
measured 7.5 s and 92.5 MB.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time
from array import array
from math import gcd, log

CAP = 10 ** 7
SWEEP_TO = 60
FAILS = []
MISSES = []


def ok(cond, msg):
    """a control or a bookkeeping check: a miss is a FAIL."""
    tag = "ok  " if cond else "FAIL"
    print("  [%s] %s" % (tag, msg))
    if not cond:
        FAILS.append(msg)


def predicted(cond, msg):
    """a frozen prediction about the constants: a miss is a finding, not a
    failure of the rig, and is printed and counted as such."""
    tag = "hit " if cond else "MISS"
    print("  [%s] %s" % (tag, msg))
    if not cond:
        MISSES.append(msg)


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
    slice overwrites the marks of the primes before it. factor() divides
    it out repeatedly, which yields the whole factorization."""
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


def merge(fa, fb):
    """factorization of a*b from those of a and b."""
    d = dict(fa)
    for p, e in fb:
        d[p] = d.get(p, 0) + e
    return sorted(d.items())


def lcm_fac(fa, fb):
    d = dict(fa)
    for p, e in fb:
        d[p] = max(d.get(p, 0), e)
    return sorted(d.items())


def v_p(n, p):
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def wall_from(fac, isprime):
    """W(n) from its definition, n given by its factorization; n+1 must
    be within the sieve."""
    n = 1
    for p, e in fac:
        n *= p ** e
    W = 2 if n % 2 else 2 ** (v_p(n, 2) + 2)
    for d in divisors_from(fac):
        p = d + 1
        if p > 2 and isprime[p]:
            W *= p ** (v_p(n, p) + 1)
    return W


def carmichael(fac):
    """lambda(n) from n's factorization."""
    lam = 1
    for p, e in fac:
        if p == 2:
            l = 1 if e == 1 else (2 if e == 2 else 2 ** (e - 2))
        else:
            l = (p - 1) * p ** (e - 1)
        lam = lam * l // gcd(lam, l)
    return lam


def lambda_values(upto, lpf, isprime):
    """the even L <= upto with lambda(W(L)) = L."""
    out = []
    for L in range(2, upto + 1, 2):
        fac = factor(L, lpf)
        # W(L)'s factorization from its definition, without factoring W
        wf = [(2, 1 if L % 2 else v_p(L, 2) + 2)]
        for d in divisors_from(fac):
            p = d + 1
            if p > 2 and isprime[p]:
                wf.append((p, v_p(L, p) + 1))
        if carmichael(sorted(wf)) == L:
            out.append(L)
    return out


# ------------------------------------------------------------ the criterion

class Lambda:
    """what the criterion needs of L, computed once."""

    def __init__(self, L, lpf, isprime):
        self.L = L
        self.fac = factor(L, lpf)
        self.W = wall_from(self.fac, isprime)
        self.divs = divisors_from(self.fac)
        self.even_divs = [e for e in self.divs if e % 2 == 0]
        self.odd_doors = [d + 1 for d in self.divs if d + 1 > 2 and isprime[d + 1]]


def in_class(q, lam, lpf, isprime):
    """the hand criterion: q = L m + 1 with m odd, m > 1, no odd door of
    L dividing m, and e f + 1 composite for every even e | L and f | m,
    f > 1, with e f not dividing L and (e, f) != (L, m)."""
    L = lam.L
    m = (q - 1) // L
    if m % 2 == 0 or m == 1:
        return False
    for p in lam.odd_doors:
        if m % p == 0:
            return False
    fdivs = divisors_from(factor(m, lpf))
    for e in lam.even_divs:
        for f in fdivs:
            if f == 1 or (e == L and f == m):
                continue
            d = e * f
            if L % d == 0:
                continue
            if isprime[d + 1]:
                return False
    return True


def bad_pair(q, lam, lpf, isprime):
    L = lam.L
    m = (q - 1) // L
    for e in lam.even_divs:
        for f in divisors_from(factor(m, lpf)):
            if f == 1 or (e == L and f == m):
                continue
            d = e * f
            if L % d == 0:
                continue
            if isprime[d + 1]:
                return (e, f)
    return None


def silent(q, lam, lpf, isprime):
    """silence from its definition: W(lcm(L, q-1)) == q * W(L)."""
    lf = lcm_fac(lam.fac, factor(q - 1, lpf))
    return wall_from(lf, isprime) == q * lam.W


# ------------------------------------------------------------ the sections

def s1_control(lams, primes, lpf, isprime):
    section("S1 THE CRITERION IS THE CLASS (control)")
    small = [q for q in primes if q <= 10 ** 5]
    total_bad = 0
    for lam in lams:
        bad = []
        for q in small:
            if (q - 1) % lam.L:
                continue
            a = in_class(q, lam, lpf, isprime)
            fq = factor(q - 1, lpf)
            b = (wall_from(fq, isprime) == q * lam.W)
            if a != b:
                bad.append(q)
        total_bad += len(bad)
        if bad:
            print("  lambda = %d: %d disagreements, %s" % (lam.L, len(bad), bad[:5]))
    ok(total_bad == 0, "P1: criterion vs wall(q-1) == q wall(L) over primes "
       "q = 1 mod L, q <= 10^5, every L in the sweep: %d disagreements"
       % total_bad)
    lam2 = lams[0]
    cls = [q for q in small if q < 6000 and in_class(q, lam2, lpf, isprime)]
    safe = sum(1 for q in cls if isprime[(q - 1) // 2])
    print("  lambda = 2 below 6000: %d primes in the class, %d safe, %d not"
          % (len(cls), safe, len(cls) - safe))
    ok(len(cls) == 101 and safe == 81, "P1: 101 / 81 / 20 at lambda = 2")


def s2_correction(lams, primes, lpf, isprime):
    section("S2 THE CORRECTION'S CENSUS (silence from its definition, fresh "
            "primes q <= 10^5)")
    small = [q for q in primes if q <= 10 ** 5]
    mismatch = 0
    off_counts = {}
    least = {}
    not_gcd_blind = 0
    eleven_silent_at_8 = None
    for lam in lams:
        L = lam.L
        n_sil = n_class = n_off = 0
        least_off = None
        gcds = {}
        for q in small:
            if L % (q - 1) == 0:
                continue                       # door open: not a fresh import
            sil = silent(q, lam, lpf, isprime)
            if L == 8 and q == 11:
                eleven_silent_at_8 = sil
            if sil:
                g = gcd(q - 1, L)
                Vq = wall_from(factor(q - 1, lpf), isprime) // q
                if Vq != wall_from(factor(g, lpf), isprime):
                    not_gcd_blind += 1
            if (q - 1) % L == 0:
                if sil != in_class(q, lam, lpf, isprime):
                    mismatch += 1
                n_class += sil
            elif sil:
                n_off += 1
                if least_off is None:
                    least_off = q
                g = gcd(q - 1, L)
                gcds[g] = gcds.get(g, 0) + 1
            n_sil += sil
        off_counts[L] = n_off
        least[L] = least_off
        print("  lambda = %-3d W = %-12d silent: %-5d  in the class (L | q-1): "
              "%-5d  off the class: %-5d  least off %s  gcd(q-1, L) tally %s"
              % (L, lam.W, n_sil, n_class, n_off, least_off,
                 sorted(gcds.items())))
    ok(mismatch == 0, "P2: silence and the criterion agree on every q with "
       "L | q-1 (%d mismatches)" % mismatch)
    ok(off_counts[2] == 0 and all(off_counts[L] > 0 for L in off_counts if L > 2),
       "P2: off-class silent primes: 0 at lambda = 2, present at every other "
       "L in the sweep (%s)" % [L for L in off_counts if L > 2 and off_counts[L] == 0])
    ok(least.get(12) == 83 and least.get(4) == 23,
       "P2: least off-class silent prime 83 at lambda = 12, 23 at lambda = 4 "
       "(read %s, %s)" % (least.get(12), least.get(4)))
    ok(not_gcd_blind == 0, "P2b: V(q) = W(gcd(q-1, L)) for every silent q at "
       "every L (%d exceptions)" % not_gcd_blind)
    ok(eleven_silent_at_8 is False, "P2b: 11 is not silent at lambda = 8 "
       "(read %s)" % eleven_silent_at_8)


def s3_census(lams, primes, lpf, isprime):
    section("S3 THE CENSUS BY LAMBDA (class members to 10^7)")
    members = {}
    p4_bad = []
    p5_bad = []
    rec = {}
    resid = {}
    for lam in lams:
        L = lam.L
        mem = [q for q in primes if (q - 1) % L == 0
               and in_class(q, lam, lpf, isprime)]
        members[L] = mem
        shares = []
        row = []
        for k in (5, 6, 7):
            X = 10 ** k
            cls = [q for q in mem if q <= X]
            pr = sum(1 for q in cls if isprime[(q - 1) // L])
            co = len(cls) - pr
            share = co / len(cls) if cls else float("nan")
            shares.append(share)
            row.append("%d (%d prime-cofactor, share %.3f)" % (len(cls), pr, share))
            if k in (6, 7) and L == 2:
                rec[k] = (len(cls), pr)
        phiL = sum(1 for a in range(1, L + 1) if gcd(a, L) == 1)
        ratio = len(mem) * phiL * log(10 ** 7) ** 2 / 10 ** 7
        print("  lambda = %-3d phi = %-3d below 10^5, 10^6, 10^7: %s;  "
              "N phi(L) log^2 x / x = %.3f" % (L, phiL, "; ".join(row), ratio))
        D = 1.0
        for p in lam.odd_doors:
            D *= (1 - 1 / p) if L % p == 0 else (1 - 1 / (p - 1))
        ne = len(lam.even_divs)
        resid.setdefault(ne, []).append(ratio / D)
        print("      door product D = %.3f over %d odd doors; even divisors %d;"
              "  ratio / D = %.2f" % (D, len(lam.odd_doors), ne, ratio / D))
        if L <= 24 and not (shares[0] < shares[1] < shares[2]):
            p4_bad.append(L)
        if not (0.5 <= ratio <= 4):
            p5_bad.append((L, round(ratio, 3)))
    ok(rec.get(6) == (8770, 4322) and rec.get(7) == (71419, 30655),
       "P3: lambda = 2 reads 8,770 / 4,322 and 71,419 / 30,655 (read %s, %s)"
       % (rec.get(6), rec.get(7)))
    predicted(not p4_bad, "P4: the composite share rises across 10^5, 10^6, "
              "10^7 at every L <= 24 (not at %s)" % p4_bad)
    predicted(not p5_bad, "P5: N phi(L) log^2 x / x within [0.5, 4] at every "
              "L (outside at %s)" % p5_bad)
    print("  S3b ratio / D by the even-divisor count of L (mean over the L "
          "sharing a count):")
    for ne in sorted(resid):
        print("      %d even divisor%s: %d value%s, mean %.2f, range %.2f..%.2f"
              % (ne, "" if ne == 1 else "s", len(resid[ne]),
                 "" if len(resid[ne]) == 1 else "s",
                 sum(resid[ne]) / len(resid[ne]), min(resid[ne]), max(resid[ne])))
    return members


def s4_mechanism(lams, primes, lpf, isprime, members):
    section("S4 THE MECHANISM (the bad set of the proof's Step 2)")
    by_L = {lam.L: lam for lam in lams}
    rising = []
    noe = 0
    bumps = 0
    for L in (2, 4, 6, 12):
        lam = by_L[L]
        memset = set(members[L])
        fracs = []
        for z in (5, 11, 23, 47):
            rough = bad = 0
            for q in primes:
                if (q - 1) % L:
                    continue
                m = (q - 1) // L
                if m == 1 or factor(m, lpf)[0][0] < z:
                    continue
                rough += 1
                if q not in memset:
                    bad += 1
                    if any(m % p == 0 for p in lam.odd_doors):
                        bumps += 1      # a door of L divides m: rule (b)
                    elif bad_pair(q, lam, lpf, isprime) is None:
                        noe += 1
            frac = bad / rough if rough else float("nan")
            fracs.append(frac)
            print("  lambda = %-3d z = %2d: %7d primes q = 1 mod L below 10^7 with "
                  "(q-1)/L free of primes below z, %6d outside the class "
                  "(fraction %.4f)" % (L, z, rough, bad, frac))
        if not all(fracs[i] > fracs[i + 1] for i in range(3)):
            rising.append(L)
    ok(not rising, "P6: the bad fraction falls with z at every L (failing at %s)"
       % rising)
    ok(noe == 0, "P6: every bad q carries an even e | L and f | m with e f + 1 "
       "prime, or a door of L dividing m (%d without; %d door bumps, each at "
       "a door not below z since m is z-rough)" % (noe, bumps))


def main():
    t0 = time.time()
    print("explore_silent_set.py -- is the silent set infinite at every even "
          "lambda? (yes, by proof; the rig is the control and the census)")
    isprime = sieve(CAP)
    lpf = lpf_table(CAP)
    primes = [q for q in range(3, CAP + 1) if isprime[q]]
    print("  tables built: %d odd primes to 10^7, %.1f s"
          % (len(primes), time.time() - t0))
    vals = lambda_values(SWEEP_TO, lpf, isprime)
    print("  even lambda-values to %d: %s" % (SWEEP_TO, vals))
    print("  even non-values: %s"
          % [L for L in range(2, SWEEP_TO + 1, 2) if L not in vals])
    lams = [Lambda(L, lpf, isprime) for L in vals]
    s1_control(lams, primes, lpf, isprime)
    s2_correction(lams, primes, lpf, isprime)
    members = s3_census(lams, primes, lpf, isprime)
    s4_mechanism(lams, primes, lpf, isprime, members)
    print()
    print("  wall %.1f s" % (time.time() - t0))
    if FAILS:
        print("%d FAILED:" % len(FAILS))
        for f in FAILS:
            print("  " + f)
        return 1
    if MISSES:
        print("all controls passed; %d prediction(s) about the constants "
              "missed, recorded in the docstring:" % len(MISSES))
        for m in MISSES:
            print("  " + m)
    else:
        print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
