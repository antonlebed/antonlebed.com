"""
explore_growth_laws.py — the self-growing tower.

THE QUESTION. The tower is a blueprint: WE chose the primes. Flip it:
let a number system grow itself. A GROWTH LAW = a structural DEMAND on
extensions + a greedy MOVE (state = modulus N; move: N -> N*m with
m >= 2 MINIMAL satisfying the demand). The demands are stated
relationally — none mentions "prime":

  D-IND  independence: the extension splits, Z/Nm = Z/N x Z/m
         (the new window shares zero information with the whole)
         <=> gcd(m, N) = 1.
  D-MEM  new memory: the idempotent count grows <=> omega(Nm) > omega(N)
         (a new stable subsystem / attention mask).
  D-DYN  new dynamics: lambda(Nm) > lambda(N) (a longer universal period).
  D-ORD  new orders: the set of realized unit orders grows.
  D-TRA  transparent growth: N grows, lambda frozen (capacity without
         new dynamics).
  D-RATE optimizer variant: maximize new idempotents per bit within a
         horizon (rate, not threshold).

Which demands grow WHICH towers? Is the primorial tower an attractor
of free growth or a knife-edge choice?

FINDINGS (tier-labeled; run record below; all sections assert).

1. THE LEAST-NEW LEMMA (rule, proved; verified exhaustively N <= 1e5).
   The minimal m >= 2 with gcd(m, N) = 1 is the least prime q NOT
   dividing N. Proof: any 2 <= m < q has all its prime factors < q
   (a factor of m is <= m), and every prime < q divides N by
   minimality of q; so gcd(m, N) > 1, while gcd(q, N) = 1.
   COROLLARY (fields for free): greedy independence can never pick a
   composite — every new channel is a prime FIELD and growth never
   breaks squarefree-ness (a squarefree seed stays squarefree
   forever; a non-squarefree seed keeps its own excess powers —
   growth adds, never repairs), with neither fields nor
   squarefree-ness demanded. The blueprint's field axiom is an
   OUTPUT of minimal independence.

2. THE HEALING RULE (rule, proved by Lemma 1 induction; verified
   seeds 1..100 x 25 steps). From ANY seed, the D-IND trajectory's
   picks are exactly the primes not dividing the seed, in increasing
   order. From seed 1 (or 2, or any primorial) it generates the
   primorial tower exactly; from a damaged/exotic seed it absorbs
   every missing prime in order. The attractor statement lives at
   the level of WINDOW SETS: every trajectory's set of primes read
   converges to ALL primes — while a seed's own defects persist
   (healing adds missing windows; it never removes excess powers).

3. D-MEM == D-IND (rule, proved; verified exhaustively N <= 1e5).
   The minimal m whose product adds a NEW prime factor is the same q
   (same argument), so memory-greedy and independence-greedy grow the
   IDENTICAL tower: two structurally different demands, one attractor.

4. D-DYN IS A MISER (observation, 11 seeds x 40 steps, scan cap 2e4).
   Dynamics-greedy DEEPENS existing windows instead of opening new
   ones: 11/11 seeds lock onto a single prime channel (every pick
   past step 10, through step 40, is a power of one prime — the
   measured scope; no unbounded claim). The lock prime varies with
   the seed — 2-adic from seed 2; 3-adic from 3, 6, 30; 5-adic from
   5, 10, 21, 105, 210; 7-adic from 2310, 30030. Exactly ONE window
   opening occurred in all 440 steps: from N = 21, where deepening 3
   is itself lambda-TRANSPARENT (lambda(9) = 6 already lives in
   lambda via 7-1 = 6 — transparency, applied to a deepening move
   instead of a new prime), the greedy's first pick opens the 5-window —
   and then locks onto 5. The depth fate: dynamics-greed abandons CRT
   breadth entirely and grows a p-adic column. (Answered: the
   lock is proved certain and the basin map computed — the lock-prime
   law, explore_lock_prime.py; the 40-step scope caveat is retired.)

5. D-ORD == D-DYN (rule; realization verified exhaustively N <= 1200).
   In the finite abelian unit group, the set of realized orders is
   EXACTLY the divisors of lambda(N) (verified: 1198/1198 rings,
   N = 3..1200), so a new order appears iff lambda grows: the two
   demands coincide.

6. THE TRANSPARENCY WALL (rule, proved; verified seeds 2..100).
   lambda is monotone along ANY growth (lambda(N) | lambda(Nm):
   channels only deepen, and lambda(p^e) | lambda(p^(e+1))). The set
   {n : lambda(n) | L} is lcm-closed (lambda(lcm) = lcm(lambda)) and
   FINITE (p-1 must divide L so p <= L+1; prime powers bounded), with
   maximum W(L) = prod p^e_max over (p-1) | L. Every transparent
   trajectory stays inside the divisors of W(lambda(seed)), and the
   strict greedy halts at EXACTLY W(lambda(seed)): it cannot stall
   below the wall, because while N < W the least prime factor p of
   W/N is a legal move (Np | W, so lambda(N) | lambda(Np) | lambda(W)
   | L forces lambda(Np) = L). Verified for all
   seeds 2..100 (99/99 halt at the predicted wall; largest specimen:
   seed 73, lambda = 72, climbs to W(72) = 20,174,525,280 in 13 steps
   and dies). Transparent growth is MORTAL.

   THE WALL IDENTITY (verified L <= 12 here; the identity itself is
   self-verified here, the homotopy reading is textbook. Later:
   explore_headroom.py carries the same check to every even L <= 112,
   56/56, because the pointwise tombstones -- the states equal to their
   own wall -- reach lambda = 106 and this range did not cover them):
   for even L, W(L) = denominator(B_L / 2L):

     L        2    4    6    8    10    12
     W(L)    24  240  504  480   264  65520

   These are the image-of-J orders of stable homotopy (textbook
   values: |im J| = Z/24, Z/240, Z/504, ... in pi_3, pi_7, pi_11,
   ...; the denominator formula is the classical von Staudt-Clausen
   refinement used in Adams' J-homomorphism work — attribution at
   memory tier, no primary read this session). The mortality fate's
   tombstones are the stable-homotopy constants.
   Separately (do not fuse): the squarefree KERNEL of W(L) equals
   denominator(B_L) = prod_{(p-1)|L} p (von Staudt-Clausen proper)
   and is the maximal n with a^(L+1) == a for ALL a (prime squares
   break the all-a form at a = p). Both identities verified against
   Bernoulli numbers computed from scratch (exact Fractions,
   Pascal-row recurrence).
   W(odd L) = 2 (lambda(n) is even for n >= 3).

7. D-RATE PICKS THE NEXT PRIME (rule, proved + verified k = 1..6,
   horizon 1000). Among all m <= 1000 from a primorial seed, the
   unique maximizer of (new idempotents) / (bits paid) is the single
   next prime q: a double-opening m = q*q' pays log q + log q' >
   2 log q for 2 doublings (rate < 1/log q), deepening pays for 0.
   The optimizer and the threshold-greedy agree: the primorial path
   is not an artifact of thresholding.

THE THREE FATES (the chart's synthesis). Free growth trichotomizes:
  BREADTH    (D-IND == D-MEM == D-RATE): the primorial tower — immortal,
             healing, all-field squarefree-preserving growth; the
             whole blueprint from the one demand "grow by the least
             piece that shares nothing with what you are". THE
             ONE-DEMAND GENESIS.
  DEPTH      (D-DYN == D-ORD): a p-adic column — immortal (only
             finitely many primes q have q-1 dividing lambda, so a
             lambda-growing move always exists) but single-window at
             every measured step; dynamics-greed abandons breadth.
  MORTALITY  (D-TRA): halts at the transparency wall W(lambda(seed)),
             the im-J / Bernoulli denominators.
The primorial tower is NOT a universal attractor — it is the
attractor of exactly one demand, independence, which is the CRT
axiom itself read as a growth demand. Honest scope: threshold-greedy
laws over ring extensions of Z/N; optimizers sampled at one horizon;
stochastic laws were subsequently charted at
explore_thermal_growth.py (the melting asymmetry); additive moves
and non-cyclic ambients are open. Honest limit: every law here orders its
candidates by SIZE ("least m") — the deleted archimedean place
returns as the cost axis of growth; the non-archimedean cost theory
was subsequently written at explore_size_crystallization.py (the
crystallization split).

RUN RECORD (python explore_growth_laws.py, ~0.5 s, trivial memory):
  S1 least-new lemma: 100000/100000 (m_min == least non-dividing
     prime; every m_min prime)
  S2 healing rule: 100 seeds x 25 steps, picks == missing primes in
     order; all picks prime+coprime (fields for free)
  S3 D-MEM == D-IND: 100000/100000 identical picks
  S4 D-DYN: 11/11 seeds locked (tail = one prime's powers); openings
     1/440 steps (the seed-21 blocked-deepening specimen, confirmed)
  S5 order realization: 1198/1198 rings (orders == divisors of
     lambda)
  S6 D-TRA: 99/99 seeds halt at W(lambda(seed)); wall table above;
     both identities hold for even L <= 12; kernel maximality spot-
     checked (K, 2K, 3K, 5K, 7K)
  S7 D-RATE: 6/6 primorial seeds, unique argmax = next prime
  TOTAL 315,336 checks, exit 0.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
from math import gcd, log2
from fractions import Fraction

CHECKS = 0


def check(cond, msg=""):
    global CHECKS
    if not cond:
        print("FAIL:", msg)
        sys.exit(1)
    CHECKS += 1


# ---------- primes / factorization / carmichael ----------

def sieve(limit):
    is_p = bytearray([1]) * (limit + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(limit ** 0.5) + 1):
        if is_p[i]:
            is_p[i * i:: i] = bytearray(len(is_p[i * i:: i]))
    return [i for i in range(limit + 1) if is_p[i]]

PRIMES = sieve(20000)
PRIMESET = set(PRIMES)


def factorize(m):
    """m -> dict {p: e} (trial division; m <= ~4e8 fine here)."""
    f = {}
    for p in PRIMES:
        if p * p > m:
            break
        while m % p == 0:
            f[p] = f.get(p, 0) + 1
            m //= p
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f


def lcm(a, b):
    return a * b // gcd(a, b)


def lam_pp(p, e):
    """Carmichael lambda of the prime power p^e."""
    if p == 2:
        return 1 if e == 1 else (2 if e == 2 else 2 ** (e - 2))
    return p ** (e - 1) * (p - 1)


def carmichael(factors):
    L = 1
    for p, e in factors.items():
        L = lcm(L, lam_pp(p, e))
    return L


def merge(factors, mf):
    out = dict(factors)
    for p, e in mf.items():
        out[p] = out.get(p, 0) + e
    return out


def least_nondividing_prime(N):
    for p in PRIMES:
        if N % p:
            return p
    raise AssertionError("prime table exhausted")


def divisors(n):
    ds = [1]
    for p, e in factorize(n).items():
        ds = [d * p ** i for d in ds for i in range(e + 1)]
    return sorted(ds)


# ---------- S1 + S3: least-new lemma; D-MEM == D-IND ----------

def s1_s3(limit=100000):
    for N in range(1, limit + 1):
        # D-IND greedy pick: minimal m >= 2 coprime to N
        m = 2
        while gcd(m, N) != 1:
            m += 1
        q = least_nondividing_prime(N)
        check(m == q, f"S1 N={N}: m_min={m} != least non-dividing prime {q}")
        check(q in PRIMESET, f"S1 N={N}: pick {q} not prime")
        # D-MEM greedy pick: minimal m >= 2 adding a new prime factor
        mm = 2
        while all(N % p == 0 for p in factorize(mm)):
            mm += 1
        check(mm == q, f"S3 N={N}: D-MEM pick {mm} != D-IND pick {q}")
    print(f"S1 least-new lemma: {limit}/{limit} PASS (m_min = least "
          "non-dividing prime, always prime)")
    print(f"S3 D-MEM == D-IND: {limit}/{limit} identical picks PASS")


# ---------- S2: the healing rule ----------

def s2(seed_max=100, steps=25):
    for seed in range(1, seed_max + 1):
        expected = [p for p in PRIMES if seed % p][:steps]
        N, picks = seed, []
        for _ in range(steps):
            m = 2
            while gcd(m, N) != 1:
                m += 1
            check(m in PRIMESET and gcd(m, N) == 1,
                  f"S2 seed={seed}: pick {m} not a coprime prime")
            picks.append(m)
            N *= m
        check(picks == expected,
              f"S2 seed={seed}: picks {picks[:5]}... != missing primes in order")
    print(f"S2 healing rule: {seed_max} seeds x {steps} steps PASS "
          "(picks = missing primes in increasing order)")


# ---------- S4: D-DYN trajectories ----------

def s4(seeds=(2, 3, 5, 6, 10, 21, 30, 105, 210, 2310, 30030),
       steps=40, cap=20000):
    total_openings, table = 0, []
    for seed in seeds:
        fac = factorize(seed)
        L = carmichael(fac)
        picks, openings = [], []
        for step in range(steps):
            found = None
            for m in range(2, cap + 1):
                nf = merge(fac, factorize(m))
                if carmichael(nf) > L:
                    found = (m, nf)
                    break
            check(found is not None, f"S4 seed={seed}: no move <= {cap}")
            m, fac = found
            picks.append(m)
            L = carmichael(fac)
        # openings: picks containing a prime that was new at pick time
        fac2 = factorize(seed)
        for m in picks:
            mf = factorize(m)
            if any(p not in fac2 for p in mf):
                openings.append(m)
            fac2 = merge(fac2, mf)
        total_openings += len(openings)
        # lock-on: tail picks are all powers of one prime
        tail = picks[10:]
        tail_primes = set()
        for m in tail:
            tail_primes |= set(factorize(m))
        locked = len(tail_primes) == 1
        lock_p = tail_primes.pop() if locked else None
        table.append((seed, lock_p, openings))
        check(locked, f"S4 seed={seed}: no lock-on, tail primes {tail_primes}")
    print(f"S4 D-DYN: {len(seeds)}/{len(seeds)} seeds LOCK onto one prime; "
          f"openings {total_openings}/{len(seeds) * steps} steps")
    for seed, lock_p, opens in table:
        print(f"     seed {seed:>6}: locks onto p={lock_p}"
              + (f", openings {opens}" if opens else ""))
    # the blocked-deepening specimen: from 21, first pick opens 5
    fac = factorize(21)
    L = carmichael(fac)  # 6
    m = 2
    while carmichael(merge(fac, factorize(m))) <= L:
        m += 1
    check(m == 5, f"S4 specimen: from 21 first D-DYN pick {m} != 5")
    check(carmichael(merge(factorize(21), {3: 1})) == L,
          "S4 specimen: deepening 3 from 21 should be blocked (lambda(9)=6)")
    print("     specimen: from N=21 deepening 3 is BLOCKED (the deepening "
          "is lambda-transparent), greedy opens the 5-window PASS")


# ---------- S5: orders == divisors of lambda ----------

def s5(limit=1200):
    for N in range(3, limit + 1):
        fac = factorize(N)
        L = carmichael(fac)
        Ldivs = set(divisors(L))
        # multiplicative order of each unit, via lambda's divisors
        seen = set()
        Lfac = factorize(L)
        for a in range(1, N):
            if gcd(a, N) != 1:
                continue
            o = L
            for p in Lfac:
                while o % p == 0 and pow(a, o // p, N) == 1:
                    o //= p
            seen.add(o)
        check(seen == Ldivs, f"S5 N={N}: orders {sorted(seen)[:8]} != "
                             f"divisors of lambda {sorted(Ldivs)[:8]}")
    print(f"S5 order realization: {limit - 2}/{limit - 2} rings PASS "
          "(orders == divisors of lambda) => D-ORD == D-DYN")


# ---------- S6: the transparency wall ----------

def wall(L):
    """W(L) = max{n : lambda(n) | L} = prod p^e_max over (p-1) | L."""
    W = 1
    for p in PRIMES:
        if p > L + 1:
            break
        if L % (p - 1) == 0:
            e = 1
            while lam_pp(p, e + 1) != 0 and L % lam_pp(p, e + 1) == 0:
                e += 1
            W *= p ** e
    return W


def bernoulli(n_max):
    """B_0..B_n_max, exact Fractions, Pascal-row recurrence."""
    from math import comb
    B = [Fraction(1)]
    for m in range(1, n_max + 1):
        s = sum(Fraction(comb(m + 1, j)) * B[j] for j in range(m))
        B.append(-s / (m + 1))
    return B


def s6(seed_max=100):
    # lambda monotone under any growth (spot: exhaustive small)
    for N in range(2, 2000):
        for m in (2, 3, 4, 6, 9):
            check(carmichael(merge(factorize(N), factorize(m)))
                  % carmichael(factorize(N)) == 0,
                  f"S6 lambda not monotone at N={N}, m={m}")
    # strict transparent greedy halts at W(lambda(seed))
    halts = 0
    biggest = (0, 0, 0)
    for seed in range(2, seed_max + 1):
        fac = factorize(seed)
        L0 = carmichael(fac)
        Wpred = wall(L0)
        N, steps = seed, 0
        while True:
            found = None
            for m in range(2, 202):
                nf = merge(factorize(N), factorize(m))
                if carmichael(nf) == L0:
                    found = m
                    break
            if found is None:
                break
            N *= found
            steps += 1
            check(Wpred % N == 0, f"S6 seed={seed}: N={N} escapes W={Wpred}")
            check(steps < 200, f"S6 seed={seed}: no halt")
        check(N == Wpred, f"S6 seed={seed}: halts at {N} != W({L0})={Wpred}")
        halts += 1
        if Wpred > biggest[2]:
            biggest = (seed, steps, Wpred)
    print(f"S6 transparency wall: {halts}/{seed_max - 1} seeds halt at "
          f"W(lambda(seed)) PASS (largest: seed {biggest[0]} climbs to "
          f"W = {biggest[2]:,} in {biggest[1]} steps)")
    # the wall identity: W(L) = denom(B_L / 2L), even L <= 12
    B = bernoulli(12)
    row = []
    for L in (2, 4, 6, 8, 10, 12):
        WL = wall(L)
        imJ = (B[L] / (2 * L)).denominator
        check(WL == imJ, f"S6 identity: W({L})={WL} != denom(B_{L}/2L)={imJ}")
        # kernel identity: squarefree kernel of W(L) = denom(B_L) (VSC)
        kernel = 1
        for p in factorize(WL):
            kernel *= p
        check(kernel == B[L].denominator,
              f"S6 kernel: sqfree(W({L}))={kernel} != denom(B_{L})")
        row.append((L, WL))
    for L in (3, 5, 7, 9, 11):
        check(wall(L) == 2, f"S6: W({L}) != 2")
    print("     wall identity W(L) = denom(B_L/2L) (im-J orders) PASS: "
          + ", ".join(f"W({L})={W}" for L, W in row))
    # kernel = max n with a^(L+1) == a for ALL a: property + maximality spots
    for L in (2, 4, 6):
        K = bernoulli(12)[L].denominator
        check(all(pow(a, L + 1, K) == a % K for a in range(K)),
              f"S6: a^{L + 1} != a on kernel {K}")
        for mult in (2, 3, 5, 7):
            n = K * mult
            check(any(pow(a, L + 1, n) != a % n for a in range(n)),
                  f"S6: kernel {K} not maximal (x{mult} still universal)")
    print("     VSC kernel = max universal-exponent n (all-a form) PASS")


# ---------- S7: the rate optimizer ----------

def s7(horizon=1000):
    N = 1
    for k in range(1, 7):
        N *= PRIMES[k - 1]
        q = least_nondividing_prime(N)
        base = len(factorize(N))
        best, best_m, unique = -1.0, None, True
        for m in range(2, horizon + 1):
            gain = len(merge(factorize(N), factorize(m))) - base
            if gain == 0:
                continue
            rate = gain / log2(m)
            if rate > best + 1e-12:
                best, best_m, unique = rate, m, True
            elif abs(rate - best) <= 1e-12:
                unique = False
        check(best_m == q and unique,
              f"S7 k={k}: argmax {best_m} (unique={unique}) != next prime {q}")
    print("S7 D-RATE optimizer: 6/6 primorial seeds, unique argmax = "
          "next prime PASS")


if __name__ == "__main__":
    s1_s3()
    s2()
    s4()
    s5()
    s6()
    s7()
    print(f"\nALL PASS -- {CHECKS:,} checks. The three fates stand: "
          "BREADTH (D-IND=D-MEM=D-RATE -> primorial), DEPTH "
          "(D-DYN=D-ORD -> p-adic column), MORTALITY (D-TRA -> im-J walls).")
