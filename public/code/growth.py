"""growth.py -- a modulus grown by the cheapest move a demand admits: the
three fates, the wall mortality stops at, the prime the dynamics demand
locks onto, and the two facts about -1 that price the prime 2.

QUESTION. A GROWTH LAW is a structural demand on extensions plus the
greedy move: from the state Z/M, extend to Z/Mm with m >= 2 the least
multiplier the demand admits. The demands are stated without the word
prime:
  independence   Z/Mm = Z/M x Z/m, i.e. gcd(m, M) = 1;
  new idempotents
                 the idempotent count grows, omega(Mm) > omega(M);
  dynamics       lambda(Mm) > lambda(M), lambda the unit group's
                 exponent (the Carmichael function);
  new orders     the set of unit orders the ring realizes grows;
  transparency   M grows while lambda stays fixed;
  rate           among m <= H, maximize the idempotent doublings bought
                 per bit, (omega(Mm) - omega(M)) / log2(m).
What does each demand grow, where does it stop if it stops, and what
decides where it goes?

THE OBJECT. States are positive integers M, carried as factorizations;
lambda(p^a) = p^(a-1)(p - 1) at odd p, lambda(2) = 1, lambda(4) = 2,
lambda(2^a) = 2^(a-2) at a >= 3, lambda of a product the lcm. The WALL
W(L) is the largest M with lambda(M) | L. A trajectory's LIMIT is the
supernatural number it converges to, a product over the primes with
exponents in {0, 1, ..., infinity}, and the three FATES are properties
of that limit: BREADTH, every prime seated; DEPTH, some prime at
infinite exponent; MORTALITY, the limit a finite integer. They are not
a partition; that each greedy law realizes exactly one of them is a
fact about greed.

THE ARGUMENT (written before the engine).
  (1) THE LEAST-NEW LEMMA. The least m >= 2 with gcd(m, M) = 1 is the
      least prime q not dividing M: every 2 <= m < q has its prime
      factors below q, all of which divide M. So greedy independence
      never picks a composite, and from any seed its picks are the
      primes the seed lacks in increasing order (THE HEALING RULE):
      from 1 it is the primorial tower. The least m adding a new prime
      factor is the same q, so new idempotents grows the same tower.
  (2) ORDERS ARE DIVISORS. A finite abelian group of exponent lambda
      realizes exactly the divisors of lambda as element orders, so the
      new-orders demand is the dynamics demand.
  (3) THE RATE ARGMAX. From p_k#, a single new prime q buys one
      doubling for log2 q bits; two new primes q < q' buy two for
      log2 q + log2 q' > 2 log2 q; a multiplier with an old factor pays
      bits for nothing. So the unique maximizer is the next prime.
  (4) THE WALL. lambda(a) | lambda(b) when a | b, and lambda(lcm) =
      lcm(lambda), so {M : lambda(M) | L} is closed under lcm; it is
      finite since (p - 1) | L bounds p and the exponents are bounded.
      Its maximum is W(L) = 2^(v_2(L) + 2) x prod p^(v_p(L) + 1) over
      the odd p with (p - 1) | L, at even L, and W(odd L) = 2. Along a
      transparent walk lambda(M) = L throughout, so the walk stays
      among the divisors of W(L); and it cannot stop below the wall,
      because while M < W(L) the least prime factor p of W(L)/M is
      admissible (Mp | W(L), so lambda(Mp) divides L and is divided
      by lambda(M) = L). So it dies at exactly W(lambda(seed)).
  (5) ADAMS' NUMBER. "lambda(M) | L" and "z^L = 1 (mod M) for every
      unit z" are one condition, so W(L) is the number Adams defined,
      the gcd over the integers y of y^s (y^L - 1) for s large (J. F.
      Adams, On the groups J(X) II, Topology 3, 1965), and his theorem
      gives W(L) = denominator(B_L / 2L) at even L: 24, 240, 504, 480,
      264, 65520 at L = 2..12, the orders of the image of the
      J-homomorphism. This script computes the gcd and the Bernoulli
      numbers from scratch; it uses no homotopy. The squarefree
      kernel of W(L) is the von Staudt-Clausen product
      prod_{(p - 1) | L} p.
  (6) THE WALL OVER F_2[x]. At an irreducible g of degree d the unit
      group of F_2[x]/(g^a) has exponent (2^d - 1) 2^(ceil log2 a):
      the units are F_(2^d)^x times the 1-units 1 + g F_2[x]/(g^a),
      and (1 + u)^(2^j) = 1 + u^(2^j) is 1 at every such u iff
      2^j >= a. So lambda(g^a) | L iff (2^d - 1) | L and a <= 2^(v_2 L), and
          W(L) = prod over d with (2^d - 1) | L of
                 (the product of the irreducibles of degree d)^(2^v_2 L).
      At L = (2^n - 1) 2^v the admissible degrees are the divisors of
      n and W(L) = (x^(2^n) + x)^(2^v). The wall exists over both rings
      for the same reason; its value is the ring's.
  (7) THE DOOR MENU. lambda(Mm) is the lcm of lambda at the prime
      powers exactly dividing Mm, so a lambda-raising m has one prime
      power part q^r that raises lambda alone; the least raising move is
      a prime power, the least at each q being q^r with r its DOOR. With
      a = v_q(M) and v = v_q(lambda): at odd q, a >= 1, the door is v - a + 2 (q - 1
      already divides lambda, and the q-part must pass v); at odd q,
      a = 0, it is 1 if (q - 1) does not divide lambda, else v + 2; at
      q = 2 it is the scan over lambda(2^j) = 1, 2, 2, 4, .... Least
      moves at distinct primes are powers of distinct primes, so they
      never tie:
      greedy dynamics over Z needs no tie-break.
  (8) THE LOCK. Call a least move a DEEPENING (q | M), a FRESH OPENING
      (q coprime to M and to lambda), a GHOST (q coprime to M, q |
      lambda, (q - 1) not dividing lambda), or an opening at FULL PRICE
      (q coprime to M, q | lambda, (q - 1) | lambda, at q^(v + 2), or
      2^(v + 3) at 2). Every pick but a ghost leaves v_q(lambda) =
      a_q - 1 (THE RECURRENCE INVARIANT;
      a_q - 2 at q = 2 once a_q >= 3), which holds q's door at 1, price
      q, from then on, while every other least move is nondecreasing as
      lambda grows and never costs q. So the first pick that is not a
      ghost locks the trajectory onto q. A ghost at a prime q' is legal only while
      (q' - 1) does not divide lambda, which only gets harder, so
      ghosts come in increasing order; and a later ghost divides
      lambda(seed), since the factors a ghost q' adds are factors of
      q' - 1 < q'. So the
      lock falls within omega_odd(lambda(seed)) + 1 picks and the basin
      map seed -> lock prime is computable. A ghost's DOWRY, the
      factors of q' - 1 it adds to lambda, can shut a cheaper lock:
      seed 11 ghosts 5 and locks 7; seed 71 ghosts 5, 7 and locks 17;
      the prime seed 20231, with 20230 = 2 x 5 x 7 x 17^2, ghosts 5, 7,
      17 and locks 19, the bound attained. From 1
      the walk is 3, 9, 27, ...: 2's first door from the void is 2,
      price 4.
  (9) EVERY PRIME IS SOME SEED'S LOCK. For odd q put B = lcm of
      {p - 1 : p <= q} and of l^(c_l) for the primes l < q, c_l least
      with l^(c_l + 2) > q; take a prime P = 1 (mod B), P != 1 (mod
      q), which Dirichlet supplies since q does not divide B. The seed
      qP has lambda = P - 1; q's door is 1, price q (q does not divide
      P - 1); every opening below q is shut ((l - 1) | B) with its least
      move l^(v_l + 2) >= l^(c_l + 2) > q; every other least move costs
      more than q; no ghost fires below q. So the first pick deepens q. At
      q = 2 the seed 2 locks at 2 and no blocker is needed.
 (10) THE COLD OPENINGS. From every M >= 3 lambda is even, so the opening
      at 2 (M odd) costs 2^(v + 3) >= 16 and the opening at 3 (M prime
      to 3) costs 3^(v_3 + 2) >= 9; every prime q >= 5 opens at its
      face value q from lambda = 2.
 (11) THE TWO-ADIC PRICES. Z_2^x = {+-1} x (1 + 4 Z_2), where every
      odd Z_p^x is procyclic: this SPLITTING is the finite fact
      lambda(2^a) = 2^(a-2) at a >= 3. A COUNTERFEIT column at 2 with the
      odd pattern lambda*(2^a) = 2^(a-1), agreeing at a = 1, 2, turns
      the splitting off and leaves the EVENNESS (-1 has order 2 in
      every odd residue field) alone. On odd M > 1 the real 2-door is
      v + 3, the counterfeit v + 2; at M >= 3 prime to 3 the 3-door is
      v_3 + 2 in both. The
      cold opening at 2 is the two together: floor 16 real, 8
      counterfeit. The walk from 4 pays 4 then 2, 2, ... (lambda(4) =
      lambda(8)) and pays 2, 2, ... under the counterfeit. At a
      characteristic p a rise of v_p(lambda) is carried by a norm
      h p^(v_p(lambda) + 1) + 1 cheaper than p's opening at full price:
      h <= p - 1 at odd p, but at 2 that price 2^(v + 3) admits h in
      {1, 2, 3}, and
      h = 2, the norm 2^(v + 2) + 1, raises by two; the counterfeit
      admits h = 1
      only. The two
      facts are the two valuations of -1 - 1 = -2.

DESIGN. Standard library only; one process.
  A  the chart. The least-new lemma over every M <= 10^5 against a
     direct scan; the healing rule, seeds 1..100 x 25 steps; new idempotents =
     independence over M <= 10^5; realized orders = divisors of lambda
     over 3 <= M <= 1200, each order read as the least divisor d of
     lambda with a^d = 1; the rate argmax from p_k#, k = 1..6, over
     m <= 1000; the transparent walk from every seed 2..100.
  B  the wall. POSITIVE CONTROL first, stopping the run when it fails:
     Bernoulli numbers by the exact recurrence, whose denominators
     must match von Staudt-Clausen at every even L <= 200. Then W(L)
     against Adams' gcd at (s, K) = (20, 60) and (40, 120) at every
     L <= 200, and against denominator(B_L / 2L) at every even
     L <= 200; the kernel and W(odd L) = 2 print, the closed form
     making them. Over
     F_2[x]: POSITIVE CONTROL, the exponent law against the unit group
     computed element by element at every g^a of degree <= 9 with
     deg g <= 4 and a <= 5;
     then the closed form of W(L) against brute search over every
     monic of degree <= 10, every L <= 64 whose wall has degree
     <= 10, and every state
     with lambda | L tested for dividing W(L); the special form at
     n <= 4, v <= 2.
  C  the lock. POSITIVE CONTROL, run before section A since every
     section reads lambda, and stopping the run when it fails: the
     formula against the unit group's exponent from element orders,
     every M <= 300. The door menu against the brute least
     lambda-raising m at every M <= 20000; the least moves distinct, a
     print ((7) makes them powers of distinct primes); the least
     move's kind, one of the four of (8), counted. Seeds 1..2000, each
     walked to its lock and 30 steps past it: the first non-ghost pick
     locks, the invariant holds at every step, ghosts increase and
     divide lambda(seed), so number at most omega_odd(lambda(seed)). The
     specimens of (8). The cold openings over the same M. The blockers
     at every prime q <= 47.
  D  the two-adic prices, both tables, odd 3 <= M <= 20000; the 3-door
     in both worlds at every 3 <= M <= 20000 prime to 3, even M
     included, where the counterfeit moves lambda; the carriers'
     rises print, being arithmetic.

PREDICTIONS, fixed before the run (the figures are those of the scripts
this one replaces; the argument above says why each should hold).
  A1 least-new lemma 100000/100000; healing 100/100 seeds; new idempotents =
     independence 100000/100000; orders = divisors at 1198/1198 rings.
  A2 the rate argmax is p_(k+1) at k = 1..6, unique.
  A3 every transparent walk from 2..100 dies at W(lambda(seed)); seed
     73 climbs to W(72) = 20,174,525,280 in 13 steps.
  A4 (added when the claim was widened from greed to every policy)
     every seed 2..100 with W(lambda(seed)) <= 10^5: the states any
     transparent policy reaches, searched over every admissible m, are
     exactly the multiples of the seed dividing W, the only state with
     no admissible move is W, and the longest run has Omega(W/seed)
     moves.
  B1 the control matches at 100/100 even L. W(L) = Adams' gcd at both
     (s, K) at every L <= 200, = denominator(B_L / 2L) at every even
     L; 24, 240, 504, 480, 264, 65520 at L = 2..12, 138181680 at 36;
     kernel = the von Staudt-Clausen product; W(odd L) = 2.
  B2 F_2[x]: the exponent law holds at every tested prime power; the
     closed form matches brute at 44 values of L with 0 lattice
     failures; the special form holds at every (n, v) tested.
  C1 the control holds at 299/299; the menu matches brute at
     20000/20000, costs distinct, kinds exclusive.
  C2 2000/2000 seeds lock at the first non-ghost pick and stay locked
     30 steps, invariant at every step, the wander bound at every
     seed; the largest wander below 2000 is at most 3.
  C3 seed 11 ghosts [5], locks 7; 71 ghosts [5, 7], locks 17; 20231
     ghosts [5, 7, 17], locks 19; seed 1 walks 3, 9, 27; seed 4's
     walk pays 4 then 2.
  C4 cold-opening minima 16 and 9 over 3 <= M <= 20000; every
     5 <= q <= 47 opens at q from lambda = 2.
  C5 the blocker seed locks at q, wander 0, at all 15 primes q <= 47;
     P = 5 at q = 3, 13 at q = 5, 7; 61 at 11, 13; 241 at 17; 2161 at
     19; 23761 at 23; 55441 at 29, 31, 37, 41, 43; 1275121 at 47.
  D1 real 2-door v + 3 and counterfeit v + 2 at every odd M > 1, price
     floors 16 and 8; the 3-door identical in both; the carriers
     under the full-price opening {1, 2, 3} with rises {1, 2, 1} real
     and {1} with rise 1 counterfeit, every odd p <= 50 admitting 1..p - 1 with
     rise 1; the walk from 4 real [4, 2, 2, ...], counterfeit
     [2, 2, 2, ...]; the prime powers among 2^k + 1, k <= 20, exactly
     3, 5, 9, 17, 257, 65537.
A KILL is any printed disagreement in these sections: one of them
refutes the claim that section is named for. (Ruled on a code read:
C1's distinctness, B1's kernel and W(odd L) = 2, C2's wander bound and
D1's carriers hold by construction and print; "kinds exclusive" is
kind()'s if-chain; A4 searches states past W, to 4W.)

FINDINGS. Every prediction landed: 38/38 checks PASS.
  A1 least-new lemma and new idempotents = independence at 100000/100000; the
     healing rule at 100/100 seeds; orders = divisors at 1198/1198
     rings (437,784 units read).
  A2 the rate argmax from p_k#, k = 1..6: 3, 5, 7, 11, 13, 17, each
     unique.
  A3 all 99 transparent walks die at W(lambda(seed)) with no admissible
     m <= 2000 left; seed 73 dies at 20174525280 after 13 steps.
  A4 over the 80 seeds 2..100 with W <= 10^5, searched over every
     move to a state up to 4W, the reachable set is the seed's
     multiples dividing W, W the only dead state, the longest run
     Omega(W/seed), 0 off in each.
  B1 the control 100/100; W(L) = Adams' gcd at both (s, K), L <= 200,
     and = denominator(B_L / 2L) at every even L <= 200, 0 off; the
     table 24, 240, 504, 480, 264, 65520, W(36) = 138181680; the kernel
     the von Staudt-Clausen product at every L; W(odd L) = 2.
  B2 the exponent law at all 26 g^a of degree <= 9 with deg g <= 4,
     a <= 5; the closed
     form the brute maximum at 44 values of L, every state with
     lambda | L dividing W(L); the special form at all 12 (n, v).
  C1 the lambda control 299/299; the menu = brute at 20000/20000,
     costs distinct; the least move's kind: 10967 deepenings, 6782
     fresh openings, 2251 ghosts, no opening at full price.
  C2 2000/2000 seeds lock at the first non-ghost pick and hold 30
     more steps with the invariant; the largest wander below 2000 is
     2, first at seed 71 (the bound's 3 is attained at 20231).
  C3 11 -> [5] -> 7; 71 -> [5, 7] -> 17; 20231 -> [5, 7, 17] -> 19;
     seed 1 walks 3, 9, 27. The full-price kind is not empty. It is
     least only when no prime = 1 (mod q^(v + 1)) lies below its
     price, since such a prime would divide M, lifting v_q(lambda), or
     open at its own face value. At q = 3, v = 2 the candidates 28 and
     55 are composite, and a prime seed P with P = 1 (mod lcm{l - 1 :
     l prime, 5 <= l < 81}), 27 not dividing P - 1, shuts every
     cheaper move: the least such P, 961440481 (least by cascade.py's
     construction, prime by Miller-Rabin, deterministic there), opens
     3 at 81 and locks at 3, the invariant set by the opening itself.
  C4 cold-opening minima 16 and 9; every 5 <= q <= 47 opens at q from
     lambda = 2.
  C5 all 15 primes q <= 47 lock their blocker seeds with wander 0, at
     the recorded P.
  D1 the real 2-door v + 3 and the counterfeit v + 2 at every odd
     3 <= M <= 20000, price floors 16 and 8, the 3-door unmoved at
     every 3 <= M <= 20000 prime to 3, even M included; the carriers
     {1, 2, 3} rising {1, 2, 1} against {1} rising 1, and 1..p - 1
     rising 1 at every odd p <= 47; seed 4 pays [4, 2, 2, ...] real and
     [2, 2, 2, ...] counterfeit; the prime powers among 2^k + 1,
     k <= 20, are 3, 5, 9, 17, 257, 65537.
  Tiers: the chart, the wall (4) and its closed form over F_2[x] (6),
  the door menu, the lock, every prime a lock (9), the cold openings
  (10) and the two-adic prices are theorems, each proved above and
  verified in the ranges printed; the wall being Adams' number is a
  property (one condition, two names), its Bernoulli form Adams'
  theorem, checked here at every even L <= 200.

RUN RECORD. 38/38, 1.8 s wall, 10 MB peak commit under a memory guard. After
the first run the lambda control moved ahead of section A, which reads
lambda first; the second run printed the same 38/38. Review then found
the full-price kind; with its specimen check added the run prints
39/39. A4's three checks, added when the claim was widened to every
policy, print 42/42 in 2.0 s. A code read then made the checks that
held by construction prints (C1's distinctness, B1's kernel and
W(odd L), C2's wander bound, D1's carriers), widened A4's search to 4W
and the 3-door to even M, and made the controls stop the run: 38/38,
2.9 s, 9.5 MB.
"""

from fractions import Fraction
from math import comb, gcd, log2

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}"
          + (f" -- {detail}" if detail else ""))


def control(name, ok, detail=""):
    check(name, ok, detail)
    if not ok:
        print("  control failed: run stopped")
        raise SystemExit(1)


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


# ------------------------------------------------------------ arithmetic

def primes_up_to(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


PRIMES = primes_up_to(20000)


def factor(n):
    """Trial division by the primes to 20000, as a {prime: exponent} map:
    exact when what is left past them is 1 or below 4 * 10^8 (a prime
    then), so for every n up to 4 * 10^8 and any 20000-smooth n."""
    f = {}
    for p in PRIMES:
        if p * p > n:
            break
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def is_prime(n):
    return n >= 2 and factor(n) == {n: 1}


def value(f):
    v = 1
    for p, e in f.items():
        v *= p ** e
    return v


def merge_max(a, b):
    out = dict(a)
    for p, e in b.items():
        if e > out.get(p, 0):
            out[p] = e
    return out


def merge_add(a, b):
    out = dict(a)
    for p, e in b.items():
        out[p] = out.get(p, 0) + e
    return out


def divides(a, b):
    """The factorization a divides the factorization b."""
    return all(e <= b.get(p, 0) for p, e in a.items())


def lcm(a, b):
    return a // gcd(a, b) * b


def v2(n):
    return (n & -n).bit_length() - 1


def lam_pp(p, a, counterfeit=False):
    """lambda(p^a) as a factorization. The counterfeit column at 2 wears
    the odd pattern 2^(a-1)."""
    if a == 0:
        return {}
    if p == 2:
        x = a - 1 if (counterfeit or a <= 2) else a - 2
        return {2: x} if x else {}
    out = factor(p - 1)
    if a > 1:
        out[p] = a - 1
    return out


def lam(mf, counterfeit=False):
    out = {}
    for p, e in mf.items():
        out = merge_max(out, lam_pp(p, e, counterfeit))
    return out


def lam_int(M):
    return value(lam(factor(M))) if M > 1 else 1


def wall(L):
    """W(L), the largest M with lambda(M) | L, by the closed form, its
    odd primes the d + 1 over the divisors d of L; L < 4 * 10^8."""
    if L % 2:
        return 2
    assert L < 4 * 10 ** 8
    lf = factor(L)
    divs = [1]
    for p, e in lf.items():
        divs = [d * p ** k for d in divs for k in range(e + 1)]
    w = 2 ** (lf[2] + 2)
    for d in divs:
        if d > 1 and is_prime(d + 1):
            w *= (d + 1) ** (lf.get(d + 1, 0) + 1)
    return w


# ------------------------------------------------------- the least moves

def least_move(q, a, lamf, counterfeit=False):
    """The least q^r, r the door, raising lambda where v_q(M) = a."""
    if q == 2:
        j = a + 1
        while divides(lam_pp(2, j, counterfeit), lamf):
            j += 1
        return 2 ** (j - a)
    v = lamf.get(q, 0)
    if a >= 1:
        assert v - a + 2 >= 1
        return q ** (v - a + 2)
    if not divides(factor(q - 1), lamf):
        return q
    return q ** (v + 2)


def menu(mf, lamf, counterfeit=False):
    """Every least move below the running least, and the least one."""
    best, bq, moves = None, None, {}
    for q in PRIMES:
        if best is not None and q >= best:
            break
        d = least_move(q, mf.get(q, 0), lamf, counterfeit)
        moves[q] = d
        if best is None or d < best:
            best, bq = d, q
    return bq, best, moves


def kind(q, mf, lamf):
    if mf.get(q, 0):
        return "deepen"
    if lamf.get(q, 0) == 0:
        return "fresh"
    if not divides(factor(q - 1), lamf):
        return "ghost"
    return "full"


def step(mf, q, cost):
    r = 0
    while cost > 1:
        cost //= q
        r += 1
    mf = dict(mf)
    mf[q] = mf.get(q, 0) + r
    return mf


def walk_to_lock(seed_f, extra=30):
    """Greedy dynamics from a seed: the ghosts, the lock prime, and
    whether the lock pick and `extra` more steps stay on it with the
    recurrence invariant intact."""
    mf = dict(seed_f)
    lamf = lam(mf)
    ghosts, lock, ok, tail = [], None, True, 0
    while tail <= extra:
        q, cost, _ = menu(mf, lamf)
        k = kind(q, mf, lamf)
        if lock is None:
            if k == "ghost":
                ghosts.append(q)
            else:
                lock = q
        elif q != lock or k != "deepen":
            return ghosts, lock, False, mf
        mf = step(mf, q, cost)
        lamf = lam(mf)
        if lock is not None:
            a, v = mf[lock], lamf.get(lock, 0)
            if lock == 2 and a >= 3:
                ok = ok and v == a - 2
            else:
                ok = ok and v == a - 1
            tail += 1
    return ghosts, lock, ok, mf


def omega_odd(f):
    return sum(1 for p in f if p != 2)


# ------------------------------------------------------------- section A

def section_a():
    section("A  THE CHART: what each demand grows")
    bad_new = bad_mem = 0
    for M in range(1, 100001):
        q = next(p for p in PRIMES if M % p)
        m = 2
        while gcd(m, M) != 1:
            m += 1
        bad_new += m != q
        m = 2
        while all(M % p == 0 for p in factor(m)):
            m += 1
        bad_mem += m != q
    check("A1 least-new lemma: the least coprime m is the least absent "
          "prime", bad_new == 0, f"100000 states, {bad_new} off")
    check("A1 new idempotents picks what independence picks", bad_mem == 0,
          f"100000 states, {bad_mem} off")
    bad = 0
    for seed in range(1, 101):
        M, picks = seed, []
        for _ in range(25):
            m = 2
            while gcd(m, M) != 1:
                m += 1
            picks.append(m)
            M *= m
        bad += picks != [p for p in PRIMES if seed % p][:25]
    check("A1 healing: the picks are the seed's missing primes in order",
          bad == 0, f"100 seeds x 25 steps, {bad} seeds off")
    bad = units = 0
    for M in range(3, 1201):
        lf = lam(factor(M))
        L = value(lf)
        orders = set()
        for a in range(1, M):
            if gcd(a, M) != 1:
                continue
            units += 1
            o = L
            for p in lf:
                while o % p == 0 and pow(a, o // p, M) == 1:
                    o //= p
            orders.add(o)
        bad += orders != {d for d in range(1, L + 1) if L % d == 0}
    check("A1 the realized unit orders are the divisors of lambda",
          bad == 0, f"1198 rings, {units} units, {bad} off")
    rows = []
    for k in range(1, 7):
        M = 1
        for p in PRIMES[:k]:
            M *= p
        have = set(factor(M))
        rates = sorted(((len(set(factor(m)) - have) / log2(m), m)
                        for m in range(2, 1001)), reverse=True)
        rows.append((k, rates[0][1], rates[0][0] - rates[1][0] > 1e-12))
    print("  rate argmax from p_k#, k = 1..6:", [m for _, m, _ in rows])
    check("A2 the rate's unique argmax is the next prime",
          all(m == PRIMES[k] and u for k, m, u in rows))
    bad, spec = 0, None
    for seed in range(2, 101):
        mf, steps = factor(seed), 0
        L = value(lam(mf))
        while True:
            m = 2
            while m <= 2000 and value(lam(merge_add(mf, factor(m)))) != L:
                m += 1
            if m > 2000:
                break
            mf = merge_add(mf, factor(m))
            steps += 1
        bad += value(mf) != wall(L)
        if seed == 73:
            spec = (value(mf), steps)
    print(f"  seed 73 dies at {spec[0]} after {spec[1]} steps")
    check("A3 every transparent walk dies at W(lambda(seed)), no "
          "admissible m <= 2000 left", bad == 0, f"99 seeds, {bad} off")
    check("A3 seed 73 climbs to W(72) = 20174525280 in 13 steps",
          spec == (20174525280, 13) and wall(72) == 20174525280)
    seeds = lat = ends = long = 0
    for seed in range(2, 101):
        L = lam_int(seed)
        W = wall(L)
        if W > 10 ** 5:
            continue
        seeds += 1
        depth, todo, dead = {seed: 0}, [seed], set()
        while todo:
            M = todo.pop()
            moves = [m for m in range(2, 4 * W // M + 1)
                     if lam_int(M * m) == L]
            if not moves:
                dead.add(M)
            for m in moves:
                if depth.get(M * m, -1) < depth[M] + 1:
                    depth[M * m] = depth[M] + 1
                    todo.append(M * m)
        lat += set(depth) == {M for M in range(seed, W + 1, seed)
                              if W % M == 0}
        ends += dead == {W}
        long += max(depth.values()) == sum(factor(W // seed).values())
    print(f"  every transparent policy, {seeds} seeds with W <= 10^5, "
          "states searched to 4W")
    check("A4 the reachable states are the seed's multiples dividing W",
          lat == seeds, f"{seeds - lat} off")
    check("A4 every policy ends at W and only there", ends == seeds,
          f"{seeds - ends} off")
    check("A4 the longest run has Omega(W/seed) moves", long == seeds,
          f"{seeds - long} off")


# ------------------------------------------------------------- section B

def bernoulli(n):
    B = [Fraction(1)]
    for m in range(1, n + 1):
        B.append(-sum(comb(m + 1, k) * B[k] for k in range(m)) / (m + 1))
    return B


def vsc(L):
    """The von Staudt-Clausen product over the p with (p - 1) | L."""
    out = 1
    for p in PRIMES:
        if p - 1 > L:
            break
        if L % (p - 1) == 0:
            out *= p
    return out


def adams(L, s, K):
    g = 0
    for k in range(2, K + 1):
        g = gcd(g, k ** s * (k ** L - 1))
    return g


def section_b_z():
    section("B  THE WALL over Z: Adams' number")
    B = bernoulli(200)
    ok = sum(B[L].denominator == vsc(L) for L in range(2, 201, 2))
    control("B1 control: denominator(B_L) is the von Staudt-Clausen "
            "product at even L <= 200", ok == 100, f"{ok}/100")
    bad_a = bad_b = bad_k = 0
    for L in range(1, 201):
        W = wall(L)
        bad_a += W != adams(L, 20, 60) or W != adams(L, 40, 120)
        if L % 2 == 0:
            bad_b += W != (B[L] / (2 * L)).denominator
        kern = 1
        for p in factor(W):
            kern *= p
        bad_k += kern != vsc(L)
    table = [wall(L) for L in range(2, 13, 2)]
    print("  W(L) at L = 2..12:", table, " W(36) =", wall(36))
    check("B1 W(L) is Adams' gcd at (s, K) = (20, 60) and (40, 120), "
          "L <= 200", bad_a == 0, f"{bad_a} off")
    check("B1 W(L) = denominator(B_L / 2L) at every even L <= 200",
          bad_b == 0, f"{bad_b} off")
    check("B1 the table 24, 240, 504, 480, 264, 65520 and W(36) = "
          "138181680", table == [24, 240, 504, 480, 264, 65520]
          and wall(36) == 138181680)
    print(f"  squarefree kernel of W(L) against the von Staudt-Clausen "
          f"product, L <= 200: {bad_k} off; W(odd L) = 2 at every odd "
          f"L <= 200: {all(wall(L) == 2 for L in range(1, 201, 2))} "
          "(the closed form)")


# ------------------------------------------------- F_2[x] on int encodings
# bit i is the coefficient of x^i: 2 = x, 3 = x + 1, 7 = x^2 + x + 1.

def pdeg(a):
    return a.bit_length() - 1


def pmul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r


def pdivmod(a, b):
    q, db = 0, pdeg(b)
    while a and pdeg(a) >= db:
        s = pdeg(a) - db
        q |= 1 << s
        a ^= b << s
    return q, a


def pdivides(a, b):
    return pdivmod(b, a)[1] == 0


def ppow(a, n):
    r = 1
    for _ in range(n):
        r = pmul(r, a)
    return r


IRR = {}
for _d in range(1, 11):
    _small = [g for e in range(1, _d // 2 + 1) for g in IRR[e]]
    IRR[_d] = [f for f in range(1 << _d, 1 << (_d + 1))
               if not any(pdivides(g, f) for g in _small)]


def pfactor(f):
    out, d = {}, 1
    while 2 * d <= pdeg(f):
        for g in IRR[d]:
            while pdivides(g, f):
                f = pdivmod(f, g)[0]
                out[g] = out.get(g, 0) + 1
        d += 1
    if pdeg(f) > 0:
        out[f] = out.get(f, 0) + 1
    return out


def lam_f2_pp(d, a):
    return ((1 << d) - 1) << (a - 1).bit_length()


def lam_f2(f):
    L = 1
    for g, e in pfactor(f).items():
        L = lcm(L, lam_f2_pp(pdeg(g), e))
    return L


def wall_f2(L):
    """W(L) over F_2[x] by the closed form."""
    A = 1 << v2(L)
    w, d = 1, 1
    while (1 << d) - 1 <= L:
        if L % ((1 << d) - 1) == 0:
            for g in IRR[d]:
                w = pmul(w, ppow(g, A))
        d += 1
    return w


def section_b_f2():
    section("B  THE WALL over F_2[x]")
    bad = tested = 0
    for d in range(1, 5):
        for g in IRR[d]:
            for a in range(1, 6):
                N = ppow(g, a)
                if pdeg(N) > 9:
                    continue
                best = 1
                for u in range(1, 1 << pdeg(N)):
                    if pdivides(g, u):
                        continue
                    o, y = 1, u
                    while y != 1:
                        y = pdivmod(pmul(y, u), N)[1]
                        o += 1
                    best = lcm(best, o)
                tested += 1
                bad += best != lam_f2_pp(d, a)
    control("B2 control: lambda(g^a) = (2^d - 1) 2^ceil(log2 a) at every "
            "g^a of degree <= 9, deg g <= 4, a <= 5", bad == 0,
            f"{tested} tested, {bad} off")
    lam_of = {1: 1}
    for f in range(2, 1 << 11):
        lam_of[f] = lam_f2(f)
    tested = bad = lat = 0
    for L in range(1, 65):
        W = wall_f2(L)
        if pdeg(W) > 10:
            continue
        members = [f for f, l in lam_of.items() if L % l == 0]
        tested += 1
        bad += max(members, key=lambda f: (pdeg(f), f)) != W
        lat += sum(not pdivides(f, W) for f in members)
    check("B2 the closed form of W(L) is the brute maximum over every "
          "monic of degree <= 10", bad == 0 and tested == 44,
          f"{tested} values of L, {bad} off")
    check("B2 every state with lambda | L divides W(L)", lat == 0,
          f"{lat} failures")
    bad = cases = 0
    for n in range(1, 5):
        for v in range(0, 3):
            L = ((1 << n) - 1) << v
            cases += 1
            bad += wall_f2(L) != ppow((1 << (1 << n)) ^ 2, 1 << v)
    check("B2 W((2^n - 1) 2^v) = (x^(2^n) + x)^(2^v), n <= 4, v <= 2",
          bad == 0, f"{cases} (n, v), {bad} off")


# ------------------------------------------------------------- section C

FULL_SEED = 961440481


def is_prime_mr(n):
    """Miller-Rabin at the primes to 41, deterministic below 3.3 * 10^24."""
    if n < 2:
        return False
    d, s = n - 1, 0
    while d % 2 == 0:
        d, s = d // 2, s + 1
    for b in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41):
        if n % b == 0:
            return n == b
        x = pow(b, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def unit_exponent(M):
    L = 1
    for a in range(1, M):
        if gcd(a, M) != 1:
            continue
        o, y = 1, a
        while y != 1:
            y = y * a % M
            o += 1
        L = lcm(L, o)
    return L


def brute_least(mf):
    L = value(lam(mf))
    m = 2
    while value(lam(merge_add(mf, factor(m)))) == L:
        m += 1
    return m


def blocker(q):
    """The least prime P = 1 (mod B), P != 1 (mod q), P != q."""
    B = 1
    for p in PRIMES:
        if p > q:
            break
        B = lcm(B, p - 1)
    for r in PRIMES:
        if r >= q:
            break
        c = 0
        while r ** (c + 2) <= q:
            c += 1
        B = lcm(B, r ** c)
    P = B + 1
    while P % q == 1 or P == q or not is_prime(P):
        P += B
    return P


def section_c():
    section("C  THE LOCK: the door menu and the prime dynamics locks onto")
    bad_b = bad_d = 0
    kinds = {}
    cold2 = cold3 = 10 ** 9
    for M in range(1, 20001):
        mf = factor(M) if M > 1 else {}
        lamf = lam(mf)
        q, best, moves = menu(mf, lamf)
        bad_b += brute_least(mf) != best
        bad_d += len(set(moves.values())) != len(moves)
        k = kind(q, mf, lamf)
        kinds[k] = kinds.get(k, 0) + 1
        if M >= 3 and M % 2:
            cold2 = min(cold2, least_move(2, 0, lamf))
        if M >= 3 and M % 3:
            cold3 = min(cold3, least_move(3, 0, lamf))
    print("  the least move's kind over M <= 20000:", kinds)
    check("C1 the door menu is the brute least lambda-raising m",
          bad_b == 0, f"20000 states, {bad_b} off")
    print(f"  least moves pairwise distinct at {20000 - bad_d} of 20000 "
          "states ((7): powers of distinct primes)")
    check("C1 no least move below 20000 is an opening at full price",
          "full" not in kinds)
    print(f"  cold-opening minima, 3 <= M <= 20000: 2-opening {cold2}, "
          f"3-opening {cold3}")
    check("C4 the cold openings: 2 opens at >= 16, 3 at >= 9, both attained",
          (cold2, cold3) == (16, 9))
    check("C4 every 5 <= q <= 47 opens at q from lambda = 2",
          all(least_move(q, 0, lam({3: 1})) == q for q in PRIMES[2:15]))
    bad, over, wmax, wseed = 0, 0, 0, None
    for seed in range(1, 2001):
        sf = factor(seed) if seed > 1 else {}
        ghosts, lock, ok, _ = walk_to_lock(sf)
        lam0 = lam(sf)
        ok = (ok and lock is not None and ghosts == sorted(set(ghosts))
              and all(lam0.get(g, 0) > 0 for g in ghosts))
        bad += not ok
        over += len(ghosts) > omega_odd(lam0)
        if len(ghosts) > wmax:
            wmax, wseed = len(ghosts), seed
    print(f"  largest wander below 2000: {wmax}, first at seed {wseed}; "
          f"past omega_odd(lambda(seed)) at {over} seeds (the ghosts being "
          "distinct odd primes dividing it)")
    check("C2 the first non-ghost pick locks, 30 more steps stay locked, "
          "the invariant holds, ghosts increase and divide lambda(seed)",
          bad == 0, f"2000 seeds, {bad} off")
    check("C2 the largest wander below 2000 is at most 3", wmax <= 3)
    for seed, g_want, l_want in ((11, [5], 7), (71, [5, 7], 17),
                                 (20231, [5, 7, 17], 19)):
        ghosts, lock, ok, _ = walk_to_lock(factor(seed), extra=3)
        print(f"  seed {seed}: ghosts {ghosts}, lock {lock}")
        check(f"C3 seed {seed} ghosts {g_want} and locks {l_want}",
              ghosts == g_want and lock == l_want and ok)
    check("C3 20231 is prime and 20230 = 2 x 5 x 7 x 17^2",
          is_prime(20231) and factor(20230) == {2: 1, 5: 1, 7: 1, 17: 2})
    mf, states = {}, []
    for _ in range(3):
        q, cost, _ = menu(mf, lam(mf))
        mf = step(mf, q, cost)
        states.append(value(mf))
    check("C3 seed 1 walks 3, 9, 27", states == [3, 9, 27], str(states))
    P = FULL_SEED
    mf = {P: 1}
    lamf = lam(mf)
    q, cost, _ = menu(mf, lamf)
    k = kind(q, mf, lamf)
    ghosts, lock, ok, _ = walk_to_lock(mf, extra=5)
    print(f"  seed {P}: least move {q}^r = {cost}, kind {k}; lock {lock}")
    check("C3 the full-price specimen: the prime seed 961440481 opens 3 "
          "at 81, no prime = 1 mod 27 lies below 81, and it locks at 3",
          is_prime_mr(P) and lamf.get(3) == 2 and (q, cost, k) ==
          (3, 81, "full") and not any(is_prime(n) for n in (28, 55))
          and lock == 3 and not ghosts and ok)
    ghosts, lock, ok2, _ = walk_to_lock({2: 1}, extra=5)
    ok_all = lock == 2 and not ghosts and ok2
    blockers = {}
    for q in PRIMES[1:15]:
        P = blocker(q)
        ghosts, lock, ok, _ = walk_to_lock({q: 1, P: 1}, extra=5)
        blockers[q] = P
        ok_all = ok_all and lock == q and not ghosts and ok
    print("  blockers P by q:", blockers)
    check("C5 every prime q <= 47 is its blocker seed's lock, wander 0",
          ok_all)
    check("C5 the blockers are 5; 13, 13; 61, 61; 241; 2161; 23761; "
          "55441 five times; 1275121", blockers == {
              3: 5, 5: 13, 7: 13, 11: 61, 13: 61, 17: 241, 19: 2161,
              23: 23761, 29: 55441, 31: 55441, 37: 55441, 41: 55441,
              43: 55441, 47: 1275121})


# ------------------------------------------------------------- section D

def section_d():
    section("D  THE TWO-ADIC PRICES: the real column at 2 and a counterfeit")
    bad_r = bad_c = bad_3 = 0
    floor_r = floor_c = 10 ** 9
    for M in range(3, 20001, 2):
        mf = factor(M)
        lamf = lam(mf)
        v = lamf.get(2, 0)
        dr = least_move(2, 0, lamf)
        dc = least_move(2, 0, lamf, counterfeit=True)
        bad_r += dr != 2 ** (v + 3)
        bad_c += dc != 2 ** (v + 2)
        floor_r, floor_c = min(floor_r, dr), min(floor_c, dc)
    for M in range(3, 20001):
        if M % 3:
            mf = factor(M)
            bad_3 += (least_move(3, 0, lam(mf))
                      != least_move(3, 0, lam(mf, True), True))
    check("D1 real 2-door v+3, counterfeit v+2, at every odd 3 <= M <= 20000",
          bad_r == bad_c == 0, f"{bad_r} and {bad_c} off")
    check("D1 price floors 16 real and 8 counterfeit",
          (floor_r, floor_c) == (16, 8), f"{floor_r}, {floor_c}")
    check("D1 the 3-door is the same in both worlds at every "
          "3 <= M <= 20000 prime to 3, even M included", bad_3 == 0,
          f"{bad_3} off")
    ok = True
    for v in range(1, 9):
        for cf, want_m, want_rise in ((False, [1, 2, 3], [1, 2, 1]),
                                      (True, [1], [1])):
            dr = 2 ** (v + 2) if cf else 2 ** (v + 3)
            ms = [m for m in range(1, 64) if m * 2 ** (v + 1) + 1 < dr]
            rises = [v2(m * 2 ** (v + 1)) - v for m in ms]
            ok = ok and ms == want_m and rises == want_rise
    for p in PRIMES[1:15]:
        for v in range(1, 5):
            ms = [m for m in range(1, 2 * p)
                  if m * p ** (v + 1) + 1 < p ** (v + 2)]
            rises = []
            for m in ms:
                n, r = m * p ** (v + 1), 0
                while n % p == 0:
                    n //= p
                    r += 1
                rises.append(r - v)
            ok = ok and ms == list(range(1, p)) and set(rises) == {1}
    print(f"  carriers under the full-price opening, {{1, 2, 3}} rising "
          f"{{1, 2, 1}} real, {{1}} rising 1 counterfeit, 1..p-1 rising 1 "
          f"at odd p <= 47: {ok} (arithmetic)")
    walks = []
    for cf in (False, True):
        mf, pays = {2: 2}, []
        for _ in range(8):
            q, cost, _ = menu(mf, lam(mf, cf), cf)
            pays.append(cost)
            mf = step(mf, q, cost)
        walks.append(pays)
    print("  seed 4 pays, real:", walks[0], " counterfeit:", walks[1])
    check("D1 the walk from 4: real [4, 2, 2, ...], counterfeit "
          "[2, 2, 2, ...]", walks == [[4] + [2] * 7, [2] * 8])
    pp = [2 ** k + 1 for k in range(1, 21) if len(factor(2 ** k + 1)) == 1]
    print("  prime powers among 2^k + 1, k <= 20:", pp)
    check("D1 they are 3, 5, 9, 17, 257, 65537",
          pp == [3, 5, 9, 17, 257, 65537])


def section_control():
    section("POSITIVE CONTROL: lambda, before any verdict reads it")
    bad = sum(unit_exponent(M) != lam_int(M) for M in range(2, 301))
    control("C1 control: the lambda formula is the unit group's exponent, "
            "M <= 300", bad == 0, f"299 moduli, {bad} off")


def main():
    section_control()
    section_a()
    section_b_z()
    section_b_f2()
    section_c()
    section_d()
    print()
    print(f"{sum(CHECKS)}/{len(CHECKS)} checks passed")
    raise SystemExit(0 if all(CHECKS) else 1)


if __name__ == "__main__":
    main()
