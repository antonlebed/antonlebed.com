"""THE SEED'S RUNG -- does a death rung stop every trajectory, or only
one that climbs to it from below?

THE QUESTION. explore_ghost_wander.py and explore_cascade_chars.py walk
the pinned-cap carrier ladder at a characteristic p and certify the
first rung V at which no affordable carrier exists -- the death rung
D(p). Both walks start at V = 1. The conclusion drawn from them is
about TRAJECTORIES: one with a rank-1 place over p locks. But V is
v_p(lambda) of the state, and a seed sets it: a seed whose lambda
already carries p^V0 with V0 > D(p) starts ABOVE the certified death
and never meets it. At p = 3 a seed with V0 = 3 (the prime 109 = 4*27
+ 1 is one) climbs 163 = 2*3^4 + 1, 487 = 2*3^5 + 1, 1459 = 2*3^6 + 1
before it stalls. So the question is whether the death rungs RECUR --
whether there is a dead rung above every start -- and at which p
anything proves it.

THE HAND-DERIVATION (on paper, before any engine code).

  (1) WHAT A DEAD RUNG IS ABOVE p - 3. At odd p, rung V's candidates
      are m*p^(V+1) + 1 for 1 <= m <= p - 1. The exponent identity
      (explore_cascade_theorem.py) makes any proper prime power q^a
      among them have a = ord(q mod p^(V+1)), a | p - 1 and a >= V + 2,
      so above V = p - 3 there is none; odd m give even numbers, prime
      powers only as 2^a, the same identity's case q = 2. So for
      V >= p - 2 the rung is dead iff every EVEN-m candidate is
      composite, and a candidate divisible by a prime q smaller than
      itself is composite.

  (2) A COVERING RECURS. A prime q not dividing p divides m*p^k + 1
      (k = V + 1) exactly when m = -p^(-k) mod q: one class of m per q,
      and that class is periodic in k with period ord_q(p). So a set S
      of primes whose classes cover every even m in [2, p - 1] at ONE
      residue k0 mod L = lcm(ord_q(p) : q in S) covers them at every
      k = k0 mod L, and every such rung at or above p - 2 is dead: a
      dead rung in every window of L consecutive rungs. At odd p the
      rise is at most one a move, so a walk cannot step over a dead
      rung; it stalls on the first one at or above its start.

  (3) THE THREE SMALL CHARACTERISTICS BY HAND.
      p = 3: one even multiplier, m = 2. 2*3^k + 1 = 0 mod 5 iff
        3^k = 2 mod 5 iff k = 3 mod 4. Period 4.
      p = 5: m = 2 and 4. 2*5^k + 1 = 0 mod 3 iff k even; 4*5^k + 1
        = 0 mod 17 iff 5^k = 4 mod 17, and 5 is a primitive root mod
        17 with 5^12 = 4, so k = 12 mod 16. Both at k = 12 mod 16.
        Period 16.
      p = 2: the door is 2^(V+3), the candidates are 2^k + 1,
        2^(k+1) + 1 and 3*2^k + 1 (k = V + 1), and the rise can be TWO.
        k odd puts 3 on the first; 17 divides the second iff k + 1 = 4
        mod 8; 5 divides the third iff k = 3 mod 4. All three at
        k = 3 mod 8. A proper power among them is excluded by
        Mihailescu for the first two (2^j + 1 = q^a with a >= 2 only
        at 9) and by hand for the third (3*2^k + 1 = 5^a forces a even
        and (5^(a/2) - 1)(5^(a/2) + 1) = 3*2^k, only a = 2, k = 3). The
        rise of two needs 2^(V+2) + 1 at the rung below, which at the
        dead rung's predecessor is 2^k + 1, divisible by 3: the walk
        cannot jump the dead rung either. k = 3 itself (V = 2) is
        ALIVE -- 9, 17 and 25 are all prime powers -- so the class
        kills from k = 11 on. Period 8.

  (4) WHERE THE COVERING STOPS. Each q removes about a fraction 1/q
      of the even multipliers, so covering (p - 1)/2 of them from one
      prime set needs roughly prod(1 - 1/q) < 2/(p - 1): the set runs
      past e^(p/4) or so, and its period with it. Covering proofs are
      therefore a small-p instrument; at large p the recurrence is the
      same question as a death rung itself.

THE ENGINE. (A) the walk from every start V0 at p = 2, 3, 5, each rung
taking the affordable carrier that banks the most (the envelope), each
death certified by primality plus exact roots; (B) the covering search
at every odd p below 1000, over primes q < QMAX whose order divides
LMAX, printing the period and the prime set where one is found; (C) at
every covered p, the covered rungs certified dead numerically up to a
ceiling, the covering's own positive control.

PREDICTIONS (fixed before the run).
  S1 (positive control): started at V0 = 1 the walk reproduces the
     published deaths, V = 8 at p = 2, 2 at p = 3, 3 at p = 5, and
     D(17) = 2, D(19) = 1, D(29) = 8 at the odd ones.
  S2: at p = 2, 3, 5 every start V0 from 1 to 300 dies, within 8, 4
     and 16 rungs of its start (the periods of (3)), counting the
     start's own rung.
  S3: the covering search finds periods 4 at p = 3 and 16 at p = 5
     (or shorter), and finds a covering at only an initial handful of
     odd p -- predicted none at p >= 100.
  S4: every covered rung checked in (C) is certified dead.
  KILL, frozen as a print: any start V0 <= 300 at p in {2, 3, 5} whose
  walk has NOT died by rung 400 -- then the three-characteristic lock
  is false as scoped and the page's LOCKS is withdrawn.

RUN RECORD (15/15 checks, 13 s, peak 13.5 MB under memwatch).
  S1 held: V0 = 1 reproduces deaths 8, 2, 3 at p = 2, 3, 5 and
     D(17) = 2, D(19) = 1, D(29) = 8.
  S2 held, and the kill clause does not fire: all 900 starts, V0 = 1
     to 300 at p = 2, 3, 5, die; the longest climb is 8 rungs at p = 2
     (from V0 = 1, the published walk itself), 4 at p = 3 (from V0 = 3,
     the 163, 487, 1459 ladder of the question) and 3 at p = 5. Dead
     rungs are the common case, not the exception: 281, 286 and 289
     distinct deaths are met from the 300 starts.
  S3 MISSED as worded at p = 3: the search's first covering there is
     period 6 by the prime 7 (V + 1 = 1 mod 6), not the period-4
     covering by 5, because the search returns the first residue in k
     order and not the shortest period; the hand coverings of (3) are
     each checked on their own residues and pass. At p = 5 the first
     found is period 10 by 3 and 11. The covering exists at TEN odd
     characteristics, 3, 5, 7, 11, 13, 17, 19, 23, 31 and 37, and at
     none from 41 to 997 -- a floor set by the search's reach
     (q < 2000, orders dividing 5040), not a wall: the prediction of
     "a handful, none at p >= 100" held, and (4)'s e^(p/4) heuristic
     was pessimistic, p = 37 closing with primes up to 67.
  S4 held: 108 covered rungs below 200 (and p = 2's class to 400),
     every one certified dead.
  THE READING (rule, proved by covering at the eleven characteristics
  2, 3, 5, 7, 11, 13, 17, 19, 23, 31, 37; the walks verified from every
  start to 300 at the first three): at these characteristics a dead
  rung sits in every window of the covering's period, a walk at odd p
  cannot step over one and at p = 2 cannot jump one, so EVERY seed
  locks there, whatever exponent it starts with. At the other odd
  p < 1000 the certified death rung D(p) stops exactly the trajectories
  whose exponent at p starts at or below it; a seed starting above it
  is not covered by any certificate this corpus holds, and at large p
  the recurrence is the death-rung question itself.
"""

import os
import sys
from math import gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_bridge_reach as BR

PASS = []


def ok(cond, label):
    PASS.append(bool(cond))
    print(f"    [{'PASS' if cond else 'FAIL'}] {label}")


def iroot(n, a):
    """Largest r with r^a <= n, integer Newton from the bit length."""
    if a == 1:
        return n
    r = 1 << (n.bit_length() // a + 1)
    while True:
        nxt = ((a - 1) * r + n // r ** (a - 1)) // a
        if nxt >= r:
            break
        r = nxt
    while r ** a > n:
        r -= 1
    while (r + 1) ** a <= n:
        r += 1
    return r


SMALL = [q for q in range(3, 2000) if BR.is_primeZ(q)]


def is_prime_power(n):
    """n = q^a, q prime, a >= 1? Primality plus exact roots, no
    factorization: a composite verdict is a Miller-Rabin witness or a
    small factor with a cofactor that is not its power, so a DEATH
    verdict is a proof."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n & (n - 1) == 0
    for q in SMALL:
        if n % q == 0:
            while n % q == 0:
                n //= q
            return n == 1
        if q * q > n:
            return True
    if BR.is_primeZ(n):
        return True
    for a in range(2, n.bit_length() + 1):
        r = iroot(n, a)
        if r < 2:
            break
        if r ** a == n and BR.is_primeZ(r):
            return True
    return False


def vp(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def door_exp(p, V):
    """The virgin door's exponent: V + 2 at odd p, V + 3 at p = 2 (V >= 1)."""
    return V + 2 if p != 2 else V + 3


def carriers(p, V):
    """Affordable prime-power norms at rung V: n < p^door with v_p(n-1) > V,
    written n = m*p^(V+1) + 1."""
    door = p ** door_exp(p, V)
    base = p ** (V + 1)
    out = []
    m = 1
    while m * base + 1 < door:
        n = m * base + 1
        if is_prime_power(n):
            out.append(n)
        m += 1
    return out


def walk(p, V0, cap):
    """Envelope walk from V0: each rung takes the carrier banking the most.
    -> (death rung, trace) or (None, trace) if still alive past cap."""
    V, trace = V0, [V0]
    while V <= cap:
        hits = carriers(p, V)
        if not hits:
            return V, trace
        V = max(vp(n - 1, p) for n in hits)
        trace.append(V)
    return None, trace


# ------------------------------------------------------------- (A) the walks
print("  (A) THE WALK FROM EVERY START")
print()
for p, want in ((2, 8), (3, 2), (5, 3)):
    d, tr = walk(p, 1, 400)
    print(f"    p = {p} from V0 = 1: trace {tr}, dies at V = {d}")
    ok(d == want, f"S1: p = {p} from V0 = 1 dies at V = {want}")
for p, want in ((17, 2), (19, 1), (29, 8)):
    d, _ = walk(p, 1, 400)
    ok(d == want, f"S1: D({p}) = {want} reproduced (got {d})")

print()
PERIOD = {2: 8, 3: 4, 5: 16}
survivors = []
for p in (2, 3, 5):
    worst, worst_v0, deaths = 0, None, set()
    for V0 in range(1, 301):
        d, tr = walk(p, V0, 400)
        if d is None:
            survivors.append((p, V0))
            continue
        deaths.add(d)
        span = d - V0 + 1
        if span > worst:
            worst, worst_v0 = span, V0
    dead = sorted(deaths)
    print(f"    p = {p}: {len(dead)} distinct death rungs met from the 300 "
          f"starts, first {dead[:8]}; longest climb {worst} rungs "
          f"(from V0 = {worst_v0})")
    ok(worst <= PERIOD[p], f"S2: p = {p} every start dies within "
       f"{PERIOD[p]} rungs (longest {worst})")
print(f"    starts alive past rung 400: {survivors}")
ok(not survivors, "KILL CLAUSE: no start V0 <= 300 at p = 2, 3, 5 "
   "survives to rung 400")

# -------------------------------------------------------- (B) the coverings
print()
print("  (B) THE COVERING SEARCH AT EVERY ODD p < 1000")
QMAX, LMAX = 2000, 5040


def ordmod(a, q):
    a %= q
    k, x = 1, a
    while x != 1:
        x = x * a % q
        k += 1
    return k


def covering(p):
    """A residue k0 mod L at which the classes m = -p^(-k) mod q, q in the
    chosen set, cover every even m in [2, p-1]. -> (L, k0, primes) or None."""
    evens = list(range(2, p, 2))
    idx = {m: i for i, m in enumerate(evens)}
    full = (1 << len(evens)) - 1
    S = [q for q in SMALL if q != p and q < QMAX and LMAX % ordmod(p, q) == 0]
    if not S:
        return None
    reach = sum(-(-len(evens) // q) for q in S)
    if reach < len(evens):
        return None
    masks, orders, pinv = {}, {}, {}
    for q in S:
        orders[q] = ordmod(p, q)
        pinv[q] = pow(p, -1, q)
        tbl = []
        for c in range(q):
            mk = 0
            for m in range(2, p, 2):
                if m % q == c:
                    mk |= 1 << idx[m]
            tbl.append(mk)
        masks[q] = tbl
    L = 1
    for q in S:
        L = L * orders[q] // gcd(L, orders[q])
    cls = {q: [(-pow(pinv[q], j, q)) % q for j in range(orders[q])] for q in S}
    for k in range(L):
        cov, used = 0, []
        for q in S:
            mk = masks[q][cls[q][k % orders[q]]]
            if mk & ~cov:
                cov |= mk
                used.append(q)
            if cov == full:
                Lu = 1
                for u in used:
                    Lu = Lu * orders[u] // gcd(Lu, orders[u])
                return Lu, k % Lu, used
    return None


odd_primes = [p for p in range(3, 1000) if BR.is_primeZ(p)]
covered = {}
for p in odd_primes:
    c = covering(p)
    if c:
        covered[p] = c
print(f"    odd p < 1000: {len(odd_primes)}; a covering found at "
      f"{len(covered)}: {sorted(covered)}")
for p in sorted(covered):
    L, k0, used = covered[p]
    print(f"      p = {p}: every rung V >= {p - 2} with V + 1 = {k0} mod {L} "
          f"is dead, primes {used}")
# S3's periods as frozen are a PREDICTION about the search, scored in the
# run record: the search returns the first residue it meets in k order,
# not the shortest period. The hand coverings of (3) are checked on their
# own residues instead.
print(f"    S3 as frozen: period at p = 3 is {covered[3][0]} (predicted <= 4), "
      f"at p = 5 is {covered[5][0]} (predicted <= 16)")
ok(all((2 * pow(3, k, 5) + 1) % 5 == 0 for k in range(3, 400, 4)),
   "(3) by hand: 5 divides 2*3^k + 1 at every k = 3 mod 4")
ok(all((2 * pow(5, k, 3) + 1) % 3 == 0 and (4 * pow(5, k, 17) + 1) % 17 == 0
       for k in range(12, 400, 16)),
   "(3) by hand: 3 | 2*5^k + 1 and 17 | 4*5^k + 1 at every k = 12 mod 16")
ok(all((pow(2, k, 3) + 1) % 3 == 0 and (pow(2, k + 1, 17) + 1) % 17 == 0
       and (3 * pow(2, k, 5) + 1) % 5 == 0 for k in range(11, 400, 8)),
   "(3) by hand: 3, 17, 5 divide the three p = 2 candidates at k = 3 mod 8")
ok(all(p < 100 for p in covered), "S3: no covering at any p >= 100")

# ------------------------------------------------- (C) the coverings certified
print()
print("  (C) EVERY COVERED RUNG CERTIFIED DEAD, V < 200")
checked, bad = 0, []
for p in sorted(covered):
    L, k0, used = covered[p]
    for V in range(max(1, p - 2), 200):
        if (V + 1) % L != k0:
            continue
        checked += 1
        if carriers(p, V):
            bad.append((p, V))
# p = 2 by its own class, k = V + 1 = 3 mod 8 from k = 11
for V in range(10, 400, 8):
    checked += 1
    if carriers(2, V):
        bad.append((2, V))
print(f"    covered rungs checked: {checked}; alive among them: {bad}")
ok(not bad and checked > 0, "S4: every covered rung is certified dead")

print()
print(f"  {sum(PASS)}/{len(PASS)} checks pass")
if not all(PASS):
    sys.exit(1)
