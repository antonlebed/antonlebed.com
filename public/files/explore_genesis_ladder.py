"""
The genesis ladder (the emergence-root seed): capability birthdays --
for each capability, the minimal rung of the primorial trajectory
where it first exists, with the law that decides every row's fate.

Setting: the provenance ladder pins each WALL down to
the minimal structure carrying it; this chart is its mirror -- each
CAPABILITY pinned up to its birth rung on the trajectory R_k = Z/p_k#
(R_0 = Z/1, the degenerate rung: 0 = 1, no distinction). The
instrument is explore_walls_provenance.py's: one row per capability,
each row a claim with its own shape, birthday/deathday, criterion,
witness, tier.

THE FATE RULE (rule, proved -- one line, but it decides every row):
channels only ACCUMULATE along the trajectory (rung k+1 = rung k's
window set plus one prime, nothing ever leaves). Hence a capability's
temporal fate is its QUANTIFIER SHAPE over channels:
 - EXISTS-shaped (some channel carries prime predicate Q): MONOTONE.
   Birthday = rung of the least prime satisfying Q; once born,
   immortal. Finite conjunctions of EXISTS-shaped conjuncts stay
   monotone with birthday = max of the conjunct birthdays. General
   form: any condition inherited by channel SUPERSETS is monotone --
   the chart's multi-channel rows (zero divisors, middle grade) keep
   their witnesses by lifting, x -> (x, 0) or (x, 1).
 - FORALL-shaped (every channel must satisfy Q): ANTI-monotone.
   Deathday = rung of the least prime FAILING Q; once dead, dead
   forever. The small primes are PERMANENT VETOES: whatever 2 or 3
   fails is unreachable at every rung of the tower. The same
   argument covers any condition inherited by channel SUBSETS
   (the cube half of the Fano row): the violating subset, once
   present, is present at every later rung. A conjunction of a
   monotone and an anti-monotone condition is a WINDOW -- born and
   mortal; Fano is the chart's one specimen.
 - Corollary (with the provenance ladder): walls are EXISTS-shaped
   over substructure, so WALLS NEVER HEAL -- each wall's minimal
   carrier + accumulation give it a trajectory birthday and
   immortality. Verified mechanically: every EXISTS-row's boolean
   trajectory is nondecreasing and every FORALL-row's nonincreasing,
   computed per rung, not assumed (S6).

PREDICTIONS (stated before the run; adjudication
recorded per item after the run -- PR1-PR8 all landed):
 PR1 (rule, proved + swept exact): THE BIRTHDAY FORMULA. An element
     of multiplicative order m exists in R_k iff m | lambda(k)
     (property: U(R_k) is a product of cyclic groups C_{p_i - 1};
     achievable orders = divisors of the lcm), so
       birthday(order m) = max over prime powers q^a || m of
                           rung(least prime p == 1 mod q^a),
     where rung(p) is p's index in the prime sequence (q^a = 2 needs
     no special case: the least p with 2 | p - 1 is 3, rung 2).
     Verified: order semantics brute-forced at k <= 5 (achievable
     orders in U(N) = divisors of lambda, computed element by
     element; S2a); formula == direct least-k scan for ALL m <= 200,
     exact (S2b); spot birthdays order 3 -> k=4, order 4 -> k=3,
     order 5 -> k=5, order 8 -> k=7, order 240 -> k=7 (S2c). LANDED.
 PR2 (rule, proved + exhaustive k <= 10): THE ECC RE-TIER. The tower
     split (data = first k-3 primes, parity = last 3) has minimum
     distance EXACTLY 4 = the Singleton bound at EVERY k >= 4, not
     first at k = 7. Proof: codewords agreeing on channel set S
     differ by a multiple of prod(S), and |x - y| < D = p_1...p_{k-3}
     forces |S| <= k-4 (the product of the |S| smallest primes
     already exceeds any smaller budget), so d >= 4; the witness pair
     (0, p_1...p_{k-4}) agrees on exactly k-4 channels, so d = 4.
     Verified exhaustively over ALL differences 1..D-1 via a
     multiples sieve, k = 4..10 (S3a); any-(k-3)-subset
     reconstruction: every (k-3)-subset product >= D, equality
     exactly at the data set itself (S3b); witness attains (S3c).
     What IS born at k = 7 is the RATE CROSSING: (k-3)/k > 1/2 iff
     k >= 7 (S3d). The capability "correct any single channel error,
     reconstruct from any 3 erasures" is born at k = 4. LANDED.
 PR3 (rules + witnesses): THE DEATHS -- every FORALL-row dies in the
     first rungs, permanently. "R is a field" dies at k = 2 (Z/6 has
     zero divisors; S4a). "sqrt(-1) exists" is born DEGENERATELY at
     k = 1 (-1 = 1 in Z/2) and dies at k = 2: -1 is a nonresidue mod
     3, and 3 never leaves -- brute-forced k <= 7, criterion (every
     odd channel == 1 mod 4) k <= 12 (S4b). "U(R) is cyclic" dies at
     k = 3 (U(30) = C2 x C4; the lambda = phi test, k <= 12; S4c).
     LANDED.
 PR4 (rule + witnesses): THE i PAIR -- the deletion in one specimen.
     i as SQRT OF THE CONSTANT -1 (archimedean form: a solution of
     x^2 = -1) dies at k = 2 forever; i as ROTATION (an element of
     multiplicative order 4 -- pure cyclic content) is born at k = 3
     (ord(7) = 4 in Z/30) and is immortal. No order-4 element of
     Z/30 squares to -1 (brute; S4d): the tower keeps the turn and
     discards the square root. LANDED.
 PR5 (witnesses): THE FOUNDING STEPS -- the 0 -> 1 -> 2 -> 3 story,
     formalized. k=0: existence without distinction (Z/1: 0 = 1).
     k=1: the first distinction -- Z/2, the trajectory's only field
     rung, where Boolean logic IS the ring (AND = mul, XOR = add)
     and EXISTS = FORALL (one window). k=2: the first COMPOSITION,
     and its price in the same rung -- first zero divisors (2*3 = 0;
     S5a), first idempotents beyond {0,1} (3 and 4; S5b), first
     hiding (both proper windows of Z/6 leave both signs in every
     fiber -- the archimedean wall's first nonvacuous instance, and
     k=1 has no proper nonempty window subset to hide from; S5c),
     first EXISTS != FORALL (grade-1 element; S5d). k=3: the first
     MIDDLE -- first support grade strictly between the pair (S5d),
     first intermediate order gate (lambda = 4 is the first lambda
     with a divisor strictly between 1 and lambda: gate_2 sits
     strictly between gate_1 = box and gate_lambda = diamond, three
     distinct functions on
     U(30); S5e), first non-cyclic unit group
     (S4c). Composition's price and measurement's depth arrive
     exactly one rung after their prerequisites. LANDED.
 PR6 (rule, mechanized): THE FATE SWEEP. Every EXISTS-row in the
     chart is computed per rung k <= 12 (ECC rows k <= 10) and is
     nondecreasing; every FORALL-row nonincreasing (S6a, S6b).
     LANDED.
 PR7 (classical contact + observation): LINNIK PRICES THE PARAMETRIC
     LADDER. The birthday prime of "order q" (q prime) is the least
     prime == 1 mod q -- the least-prime-in-progression function,
     bounded by Linnik's theorem (p << q^L; contact, not re-proved).
     Computed: the table for all primes q <= 47 (S7a); in this range
     the birthday prime also satisfies p < q^2 at every q (in-range
     observation; the p < q^2 statement in general is an open
     conjecture -- no claim minted). LANDED.
 PR8 (observation, chart-scope): THE SATURATION. Within this chart,
     every mortal row is dead by k = 6 (field 2, sqrt(-1) 2, cyclic
     units 3, the Fano window 6 -- the last death, cited) and every
     qualitative EXISTS-row is born by k = 7 (the rate crossing is
     the top step); after k = 7 the trajectory's births are
     PARAMETRIC (order-m, Linnik-priced) or trajectory events
     (transparency patterns) or capacity. Computed from the sweep
     (S8: birthdays read off the computed rows, not hand-typed; the
     chart's small parametric exemplars order 3/4/5 fall below 7,
     and the parametric family at large is exempt by definition --
     order 19 is born at rung 43) -- a fact of THIS chart, not a
     theorem over all capabilities. LANDED.

Also verified: the lambda spine matches the published sequence
1, 2, 4, 12, 60, 60, 240, 720, 7920, 55440 (explore_lambda_tower;
S1a); transparency birthday k = 6, prime 13 (S1b); the first
length-2 transparency run completes at k = 12 (31 at k = 11, 37 at
k = 12; S1c). The designed-tower control (folded
in): on the tower {2, 5, 13, 17, 29} -- 3 skipped, every odd prime
== 1 mod 4 -- sqrt(-1) is solvable at EVERY rung (brute, all 5
rungs), and the fate sweep is monotone/anti-monotone there too: the
veto knob is computed, not asserted, and the fate rule runs on
accumulation alone, nothing primorial (S9a, S9b).

THE CHART (capability x shape x fate; birth/death = rung index k):

  capability                    shape    fate on the trajectory
  distinction (0 != 1)          --       born k=1 (Z/2)
  field                         FORALL   born k=1, DIES k=2
  sqrt(-1) (the constant)       FORALL   born k=1 (degenerate),
                                         DIES k=2 (3 vetoes, forever)
  zero divisors                 EXISTS   born k=2
  idempotents beyond {0,1}      EXISTS   born k=2
  hiding (sign/size)            EXISTS   born k=2 (first nonvacuous)
  quantifier pair distinct      EXISTS   born k=2
  middle grade (between pair)   EXISTS   born k=3
  intermediate order gate       EXISTS   born k=3 (lambda = 4)
  order-4 element (i as turn)   EXISTS   born k=3
  cyclic unit group             FORALL   born k=1, DIES k=3
  ECC (d = 4, 1-error-correct)  EXISTS   born k=4 (not 7)
  order-3 element               EXISTS   born k=4 (7 == 1 mod 3)
  Fano plane (character cube)   window   born k=5, DIES k=6 -- the
                                         chart's one conjunction row:
                                         a size floor (monotone) meets
                                         the cube condition (anti-
                                         monotone)
  transparency (event)          event    first at k=6 (13)
  ECC rate > 1/2                EXISTS   born k=7 (the top step)
  order-m element               EXISTS   born at the formula's rung;
                                         Linnik prices the family
  non-commutativity             --       STILLBORN: every rung is
                                         commutative (property); the
                                         capability lives one level
                                         up (M_2 floor)

Readings of the chart (the seed's answer):
 - THE EMERGENCE STAIRCASE HAS A TOP STEP: the tower's KINDS of
   structure complete at k = 7 (Z/510510 -- the ECC rung); everything
   later is parametric birth (priced by least-prime-in-AP), trajectory
   events, or capacity. The founding intuition (structure from
   nothing: 0 -> 1 -> 2 -> 3) is literal at the bottom: existence,
   distinction, composition-with-its-price, middle.
 - FATE = QUANTIFIER SHAPE: the graded logic's pair classifies the
   ladder itself -- EXISTS-capabilities are immortal-once-born,
   FORALL-capabilities are mortal-forever, and the tower never
   forgets: 2 and 3 are permanent vetoes (no sqrt(-1), no return of
   cyclicity, no Fano past k=5).
 - THE MIRROR: provenance pins walls DOWN to minimal carriers;
   genesis pins capabilities UP to birth rungs; accumulation makes
   both permanent (walls never heal, births never unbirth).

Classical contacts (named, not re-proved): Linnik (least prime in an
arithmetic progression -- the parametric birthday bound), Dirichlet
(every progression 1 mod m has a prime, so every order-m row is
eventually born), Gauss (U(p) cyclic; U(N) cyclic iff N in
{1, 2, 4, p^a, 2p^a}), Singleton (the MDS bound the split meets).

Provenance (at birth): the fate rule needs only an accumulating
family of coprime windows -- any squarefree tower qualifies, nothing
primorial. The primorial trajectory enters as WHICH primes accumulate
(the vetoes are 2 and 3 because the trajectory starts there; a
designed tower chooses its own vetoes -- a design knob: skip 3 and
sqrt(-1) lives at every rung whose odd primes are all 1 mod 4). The
saturation observation is trajectory-specific.

Run: python prime/code/explore_genesis_ladder.py   (~0.2 s, pure
Python, stdlib only; 26 checks, all PASS)
"""

from math import gcd, isqrt
from itertools import combinations

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    status = "PASS" if ok else "FAIL"
    line = f"  [{status}] {name}"
    if detail:
        line += f" -- {detail}"
    print(line)


# ---------------------------------------------------------------- helpers

def sieve(limit):
    is_p = bytearray([1]) * (limit + 1)
    is_p[0:2] = b"\x00\x00"
    for i in range(2, isqrt(limit) + 1):
        if is_p[i]:
            is_p[i * i:: i] = bytearray(len(is_p[i * i:: i]))
    return [i for i in range(limit + 1) if is_p[i]]

ALL_PRIMES = sieve(1_000_000)
PRIMES = ALL_PRIMES[:600]                      # the trajectory's primes
RUNG = {p: i + 1 for i, p in enumerate(PRIMES)}  # prime -> rung index


def lcm(a, b):
    return a * b // gcd(a, b)


LAMS = [1]                                     # LAMS[k] = lambda(R_k)
for _p in PRIMES:
    LAMS.append(lcm(LAMS[-1], _p - 1))


def lam(k):
    """lambda(R_k) = lcm(p_i - 1), i <= k; lam(0) = 1 (Z/1)."""
    return LAMS[k]


def primorial(k):
    v = 1
    for p in PRIMES[:k]:
        v *= p
    return v


def factorize(m):
    """m -> list of maximal prime powers q^a || m."""
    out = []
    for q in ALL_PRIMES:
        if q * q > m:
            break
        if m % q == 0:
            qa = 1
            while m % q == 0:
                qa *= q
                m //= q
            out.append(qa)
    if m > 1:
        out.append(m)
    return out


def least_prime_1_mod(n):
    """Least prime p with p == 1 (mod n)."""
    for p in ALL_PRIMES:
        if p % n == 1:
            return p
    raise ValueError(f"sieve too small for {n}")


def birthday_formula(m):
    """max over q^a || m of rung(least prime == 1 mod q^a)."""
    if m == 1:
        return 0
    return max(RUNG[least_prime_1_mod(qa)] for qa in factorize(m))


def birthday_direct(m):
    """Least k with m | lambda(k)."""
    for k, v in enumerate(LAMS):
        if v % m == 0:
            return k
    raise ValueError(f"trajectory too short for {m}")


def unit_orders(N):
    """Multiplicative orders of all units of Z/N (brute force)."""
    orders = set()
    for x in range(1, N):
        if gcd(x, N) != 1:
            continue
        y, o = x % N, 1
        while y != 1:
            y = y * x % N
            o += 1
        orders.add(o)
    return orders


def divisors(n):
    out = set()
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.add(d)
            out.add(n // d)
    return out


# ---------------------------------------------------------------- S1: spine

def s1_lambda_spine():
    print("S1 -- the lambda spine + trajectory events")
    published = [1, 2, 4, 12, 60, 60, 240, 720, 7920, 55440]
    computed = [lam(k) for k in range(1, 11)]
    check("S1a lambda(1..10) matches the published sequence",
          computed == published, f"{computed}")

    transparent = {}  # k -> bool, k >= 2
    for k in range(2, 51):
        p = PRIMES[k - 1]
        transparent[k] = (lam(k - 1) % (p - 1) == 0)
    first = min(k for k, t in transparent.items() if t)
    check("S1b transparency birthday k=6, prime 13",
          first == 6 and PRIMES[5] == 13, f"first transparent k={first}")

    first_run2 = min(k for k in range(3, 51)
                     if transparent[k] and transparent[k - 1])
    check("S1c first length-2 transparency run completes at k=12",
          first_run2 == 12,
          f"k={first_run2} (primes {PRIMES[first_run2-2]}, "
          f"{PRIMES[first_run2-1]})")


# ------------------------------------------------- S2: the parametric family

def s2_birthday_formula():
    print("S2 -- the parametric family: order-m birthdays")
    ok = True
    for k in range(1, 6):
        N = primorial(k)
        if unit_orders(N) != divisors(lam(k)):
            ok = False
    check("S2a achievable unit orders = divisors(lambda), brute k<=5", ok)

    ok = all(birthday_formula(m) == birthday_direct(m)
             for m in range(1, 201))
    deepest_m = max(range(2, 201), key=birthday_formula)
    deepest_p = max(least_prime_1_mod(qa)
                    for m in range(2, 201) for qa in factorize(m))
    ok = (ok and deepest_m == 197 and deepest_p == 3547
          and RUNG[deepest_p] == 497)
    check("S2b birthday formula == direct lambda scan, all m <= 200", ok,
          f"deepest need: m={deepest_m} -> p={deepest_p} "
          f"(rung {RUNG[deepest_p]})")

    spots = {3: 4, 4: 3, 5: 5, 8: 7, 240: 7}
    ok = all(birthday_formula(m) == k for m, k in spots.items())
    check("S2c spot birthdays (3->4, 4->3, 5->5, 8->7, 240->7)", ok,
          str({m: birthday_formula(m) for m in spots}))


# ------------------------------------------------------- S3: the ECC re-tier

def ecc_distance(k):
    """Min distance of the tower-split code at rung k, exhaustive over
    all codeword differences 1..D-1 via a multiples sieve."""
    ps = PRIMES[:k]
    D = primorial(k - 3)
    agree = bytearray(D)
    for p in ps:
        for m in range(p, D, p):
            agree[m] += 1
    max_agree = max(agree[1:]) if D > 1 else 0
    return k - max_agree


def s3_ecc():
    print("S3 -- ECC births: distance 4 at every k >= 4, rate crossing at 7")
    dists = {k: ecc_distance(k) for k in range(4, 11)}
    check("S3a tower-split distance EXACTLY 4, exhaustive k=4..10",
          all(d == 4 for d in dists.values()), str(dists))

    ok = True
    for k in range(4, 11):
        D = primorial(k - 3)
        data_set = tuple(range(k - 3))
        attain = []
        for S in combinations(range(k), k - 3):
            prod = 1
            for i in S:
                prod *= PRIMES[i]
            if prod < D:
                ok = False
            if prod == D:
                attain.append(S)
        if attain != [data_set]:      # minimum attained ONLY at the data set
            ok = False
    check("S3b every (k-3)-subset reconstructs (product >= D, "
          "equality only at the data set), k=4..10", ok)

    ok = True
    for k in range(5, 11):
        w = primorial(k - 4)          # the witness difference
        agree = sum(1 for p in PRIMES[:k] if w % p == 0)
        if agree != k - 4:
            ok = False
    check("S3c witness (0, p_1..p_{k-4}) attains d=4, k=5..10", ok)

    ok = all(((k - 3) / k > 0.5) == (k >= 7) for k in range(4, 31))
    check("S3d rate (k-3)/k > 1/2 iff k >= 7", ok)


# ---------------------------------------------------------- S4: the deaths

def sqrt_minus1_brute(k):
    N = primorial(k)
    return any(x * x % N == N - 1 for x in range(N))


def sqrt_minus1_criterion(k):
    """Solvable iff every odd channel prime is == 1 mod 4."""
    return all(p == 2 or p % 4 == 1 for p in PRIMES[:k])


def s4_deaths():
    print("S4 -- the deaths (FORALL-rows) + the i pair")
    check("S4a field iff k=1 (k <= 6)",
          all(is_prime_ring(k) == (k == 1) for k in range(1, 7)))

    brute = {k: sqrt_minus1_brute(k) for k in range(1, 8)}
    ok_brute = all(v == (k == 1) for k, v in brute.items())
    ok_crit = all(sqrt_minus1_criterion(k) == (k == 1)
                  for k in range(1, 13))
    check("S4b sqrt(-1) solvable iff k=1 (brute k<=7, criterion k<=12)",
          ok_brute and ok_crit)

    def u_cyclic(k):
        N = primorial(k)
        phi = 1
        for p in PRIMES[:k]:
            phi *= p - 1
        return lam(k) == phi
    check("S4c U cyclic iff k <= 2 (lambda = phi test, k <= 12)",
          all(u_cyclic(k) == (k <= 2) for k in range(1, 13)))

    N = 30
    order4 = [x for x in range(1, N) if gcd(x, N) == 1
              and x * x % N != 1 and pow(x, 4, N) == 1]
    ok = len(order4) > 0 and all(x * x % N != N - 1 for x in order4)
    check("S4d the i pair: order-4 born at k=3, none squares to -1",
          ok, f"order-4 elements of Z/30: {order4}")


# ---------------------------------------------------- S5: the small-k births

def support_grade(x, k):
    return sum(1 for p in PRIMES[:k] if x % p != 0)


def s5_births():
    print("S5 -- the founding-step births (EXISTS-rows)")
    def has_zero_div(k):
        N = primorial(k)
        return any(a * b % N == 0
                   for a in range(1, N) for b in range(1, N))
    check("S5a zero divisors born k=2",
          not has_zero_div(1) and has_zero_div(2))

    def idem_count(k):
        N = primorial(k)
        return sum(1 for x in range(N) if x * x % N == x)
    counts = {k: idem_count(k) for k in range(1, 6)}
    check("S5b idempotents = 2^k; beyond {0,1} born k=2",
          all(c == 2 ** k for k, c in counts.items()), str(counts))

    N = 6
    ok = True
    for p in (2, 3):                      # both proper windows of Z/6
        fibers = {}
        for x in range(N):
            fibers.setdefault(x % p, []).append(x)
        for f in fibers.values():
            lo = any(x < N / 2 for x in f)
            hi = any(x >= N / 2 for x in f)
            if not (lo and hi):
                ok = False
    check("S5c hiding's first nonvacuous instance k=2 "
          "(both windows of Z/6 hide the sign; k=1 has no proper window)",
          ok)

    # quantifier pair distinct at k=2; middle grade at k=3
    pair_k2 = any(support_grade(x, 2) == 1 for x in range(6))
    pair_k1 = all(support_grade(x, 1) in (0, 1) for x in range(2))
    mid_k3 = (any(support_grade(x, 3) == 1 for x in range(30))
              and any(support_grade(x, 3) == 2 for x in range(30)))
    # at k=2 thresholds [>=1] and [>=2] are the pair itself
    check("S5d pair distinct k=2; middle grade born k=3",
          pair_k2 and pair_k1 and mid_k3)

    dcounts = {k: len(divisors(lam(k))) for k in range(1, 4)}
    N = 30
    units = [x for x in range(N) if gcd(x, N) == 1]
    def gate(m):
        return tuple(1 if pow(x, m, N) == 1 else 0 for x in units)
    gates = {m: gate(m) for m in (1, 2, 4)}
    distinct = len(set(gates.values())) == 3
    check("S5e intermediate order gate born k=3 "
          "(d(lambda)=1,2,3 at k=1,2,3; gate_1/2/4 distinct on U(30))",
          dcounts == {1: 1, 2: 2, 3: 3} and distinct, str(dcounts))


# --------------------------------------------------- S6: the fate sweep

def has_strict_partial_support(k):
    """Witness-constructed: a grade-1 element exists iff k >= 2.
    k = 1 scanned whole (Z/2: grades are 0 and 1 = full, no strict
    middle); k >= 2 verified on the witness primorial(k-1)."""
    if k == 1:
        return any(0 < support_grade(x, 1) < 1 for x in range(2))
    w = primorial(k - 1)
    return 0 < support_grade(w, k) < k


def has_middle_threshold(k):
    """A threshold quantifier strictly between the pair needs a t with
    1 < t < k (structurally empty for k <= 2) plus witnesses of grade
    1 (separates it from EXISTS) and grade 2 < k (from FORALL) --
    witnesses constructed and their grades verified."""
    if k <= 2:
        return False
    return (support_grade(primorial(k - 1), k) == 1
            and support_grade(primorial(k - 2), k) == 2)


def has_nontrivial_idempotent(k):
    """Witness-constructed: e == 1 mod p_1, 0 mod the rest (CRT);
    verified idempotent and outside {0, 1}. k = 1 scanned whole."""
    N = primorial(k)
    if k == 1:
        return any(x * x % N == x and x not in (0, 1) for x in range(N))
    M = N // PRIMES[0]
    e = M * pow(M, -1, PRIMES[0]) % N
    return e * e % N == e and e not in (0, 1)


def ecc_capability(k):
    """d = 4 code with nonempty data: computed distance at k >= 4;
    below, the data modulus primorial(k-3) <= 1 carries nothing."""
    if primorial(max(k - 3, 0)) <= 1:
        return False
    return ecc_distance(k) == 4


def build_exists_rows(K):
    """Every EXISTS-row computed per rung (witnesses or lambda), never
    a k-threshold literal."""
    return {
        "zero divisors": [not is_prime_ring(k) and primorial(k) > 1
                          for k in range(1, K + 1)],
        "idempotents beyond {0,1}": [has_nontrivial_idempotent(k)
                                     for k in range(1, K + 1)],
        "pair distinct": [has_strict_partial_support(k)
                          for k in range(1, K + 1)],
        "middle grade": [has_middle_threshold(k) for k in range(1, K + 1)],
        "intermediate gate": [len(divisors(lam(k))) >= 3
                              for k in range(1, K + 1)],
        "order-3": [lam(k) % 3 == 0 for k in range(1, K + 1)],
        "order-4": [lam(k) % 4 == 0 for k in range(1, K + 1)],
        "order-5": [lam(k) % 5 == 0 for k in range(1, K + 1)],
        "ECC d=4": [ecc_capability(k) for k in range(1, 11)],
        "rate > 1/2": [(k - 3) / k > 0.5 for k in range(1, K + 1)],
    }


def build_forall_rows(K):
    return {
        "field": [is_prime_ring(k) for k in range(1, K + 1)],
        "sqrt(-1)": [sqrt_minus1_criterion(k) for k in range(1, K + 1)],
        "U cyclic": [lam(k) == phi_val(k) for k in range(1, K + 1)],
    }


def s6_fate_sweep():
    print("S6 -- the fate rule, mechanized (k <= 12)")
    rows_e = build_exists_rows(12)
    ok = all(all(not (row[i] and not row[j])
                 for i in range(len(row)) for j in range(i, len(row)))
             for row in rows_e.values())
    check("S6a every EXISTS-row nondecreasing", ok)

    rows_a = build_forall_rows(12)
    ok = all(all(not (not row[i] and row[j])
                 for i in range(len(row)) for j in range(i, len(row)))
             for row in rows_a.values())
    check("S6b every FORALL-row nonincreasing", ok)


def is_prime_ring(k):
    N = primorial(k)
    if N < 2:
        return False
    return all(N % q for q in range(2, isqrt(N) + 1))


def phi_val(k):
    v = 1
    for p in PRIMES[:k]:
        v *= p - 1
    return v


# --------------------------------------------------- S7: Linnik pricing

def s7_linnik():
    print("S7 -- Linnik prices the parametric ladder")
    table = {}
    ok_formula, ok_sq = True, True
    for q in [q for q in PRIMES if q <= 47 and q > 2]:
        p = least_prime_1_mod(q)
        table[q] = (p, RUNG[p])
        if birthday_formula(q) != RUNG[p]:
            ok_formula = False
        if not p < q * q:
            ok_sq = False
    check("S7a birthday(order q) = rung(least p == 1 mod q), primes q<=47",
          ok_formula, str({q: t for q, t in table.items()}))
    check("S7b birthday prime < q^2 at every q <= 47 "
          "(in-range observation; open conjecture in general)", ok_sq)


# --------------------------------------------------- S8: the saturation

def s8_saturation():
    print("S8 -- the saturation (chart-scope observation)")
    # Birthdays/deathdays READ OFF the computed S6 rows (first True /
    # first False + 1); hiding (S5c, birthday 2 = first proper window)
    # and Fano (dies 6) enter as their recorded values --
    # the chart's small parametric exemplars (order 3/4/5) are included
    # and happen to fall below 7; the parametric family at large is
    # exempt from the saturation claim by definition (order 19 -> 43).
    rows_e = build_exists_rows(12)
    births = {name: row.index(True) + 1 for name, row in rows_e.items()}
    births["hiding"] = 2
    transparent_first = min(
        k for k in range(2, 51)
        if lam(k - 1) % (PRIMES[k - 1] - 1) == 0)
    births["transparency"] = transparent_first
    rows_a = build_forall_rows(12)
    deaths = {name: row.index(False) + 1 for name, row in rows_a.items()}
    deaths["Fano (cited)"] = 6
    expected_births = {"zero divisors": 2, "idempotents beyond {0,1}": 2,
                       "pair distinct": 2, "hiding": 2, "middle grade": 3,
                       "intermediate gate": 3, "order-4": 3, "ECC d=4": 4,
                       "order-3": 4, "order-5": 5, "transparency": 6,
                       "rate > 1/2": 7}
    expected_deaths = {"field": 2, "sqrt(-1)": 2, "U cyclic": 3,
                       "Fano (cited)": 6}
    ok = (births == expected_births and deaths == expected_deaths
          and max(births.values()) == 7 and max(deaths.values()) == 6)
    check("S8a all deaths by k=6, all chart births by k=7 "
          "(the rate crossing is the top step)", ok,
          f"births {births} / deaths {deaths}")


# ------------------------------- S9: the designed-tower control

def s9_designed_tower():
    """The veto-knob claim, computed: on a designed tower that SKIPS 3
    (all odd primes == 1 mod 4), sqrt(-1) lives at EVERY rung; and the
    fate rule runs on accumulation alone -- the same monotonicity holds
    on this non-primorial trajectory."""
    print("S9 -- the designed-tower control (the veto knob, computed)")
    DESIGNED = [2, 5, 13, 17, 29]           # skip 3; odd primes 1 mod 4
    ok = all(p == 2 or p % 4 == 1 for p in DESIGNED)
    N = 1
    for j, p in enumerate(DESIGNED, 1):
        N *= p
        if not any(x * x % N == N - 1 for x in range(N)):
            ok = False
    check("S9a skip 3 and sqrt(-1) lives at every rung (brute, all 5 "
          "rungs of the designed tower {2,5,13,17,29})", ok)

    lams, v = [], 1
    for p in DESIGNED:
        v = lcm(v, p - 1)
        lams.append(v)
    Ns, w = [], 1
    for p in DESIGNED:
        w *= p
        Ns.append(w)
    rows_e = {
        "order-3": [lv % 3 == 0 for lv in lams],
        "order-4": [lv % 4 == 0 for lv in lams],
        "order-7": [lv % 7 == 0 for lv in lams],
        "zero divisors": [n != 2 for n in Ns],
    }
    rows_a = {
        "field": [n == 2 for n in Ns],
    }
    mono = all(all(not (row[i] and not row[j])
                   for i in range(len(row)) for j in range(i, len(row)))
               for row in rows_e.values())
    anti = all(all(not (not row[i] and row[j])
                   for i in range(len(row)) for j in range(i, len(row)))
               for row in rows_a.values())
    check("S9b the fate rule holds on the designed trajectory too "
          "(accumulation is the only ingredient)", mono and anti)


# ---------------------------------------------------------------- main

def main():
    print("THE GENESIS LADDER -- capability birthdays on the trajectory")
    print("=" * 64)
    s1_lambda_spine()
    s2_birthday_formula()
    s3_ecc()
    s4_deaths()
    s5_births()
    s6_fate_sweep()
    s7_linnik()
    s8_saturation()
    s9_designed_tower()
    n_pass = sum(1 for _, ok in CHECKS if ok)
    print("=" * 64)
    print(f"TOTAL: {n_pass}/{len(CHECKS)} checks pass")
    if n_pass != len(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
