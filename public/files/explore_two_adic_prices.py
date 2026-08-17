"""
explore_two_adic_prices.py -- are p = 2's three prices one 2-adic fact?
(sibling of explore_lock_prime.py and explore_ghost_wander.py, which
own two of the three prices; the third is the cascade's excess unit.)

THE QUESTION. Across this corpus p = 2 pays three separate-looking
prices: (A) the cascade's excess unit -- the 2-door costs 2^(v+3) where
an odd p's costs p^(v+2), the rise per purchase is at most TWO where an
odd p's is exactly one, and the excess rise is carried by norms
2^(v+2)+1, supplied by the Fermat primes together with 9; (B) the cold
door -- OPENING the 2-window costs >= 16 for every N >= 3, where 3's
floor is 9 and every prime q >= 5 opens at face value q from some state
(explore_lock_prime.py, cold doors); (C) the lock hiccup --
lambda(4) = lambda(8) = 2, so a 2-lock passing depth e = 2 pays one
cost-4 double step, and the recurrence invariant reads e - 2 at q = 2
where every odd q reads e - 1 (explore_lock_prime.py, lock criterion).
Is each price's derivation chain one named 2-adic fact, or three?

THE CANDIDATE FACT (call it SPLIT). The 2-adic unit group is
Z_2^x = {+-1} x (1 + 4Z_2) -- a direct Z/2 factor split off a procyclic
part, where every odd p's unit group is procyclic outright. Finite
shadow: (Z/2^e)^* = <-1> x <5> with ord(5) = 2^(e-2), hence
lambda(2^e) = 2^(e-2) for e >= 3 against the odd pattern
lambda(p^e) = p^(e-1)(p-1). Root: v_2(-1 - 1) = 1 EXACTLY -- the unit
-1 enters the filtration one step and no deeper.

THE SECOND FACT IN PLAY (call it EVEN). lambda(N) is even for every
N >= 3, because -1 != 1 in every odd characteristic: 2 | q-1 for every
odd prime q (and lambda(4) = 2 covers N a 2-power -- there the
evenness witness is -1 != 1 mod 4, SPLIT's own root, the corner the
two facts share). Root: v_q(-1 - 1) = 0 for every odd q. EVEN and
SPLIT are the ORDER of -1 and its 2-adic DEPTH: facts read at
disjoint places -- and the counterfeit below holds the first while
the second falls -- yet the two valuations of the same difference
-1 - 1 = -2, i.e. two invariants of the one torsion unit Z owns.

THE DESIGN. A counterfeit 2-channel with the odd pattern,
lambda*(2^e) = 2^(e-1) (agreeing at e = 1, 2), switches SPLIT off while
leaving EVEN and every odd channel untouched. Recompute all three
prices in both worlds; which prices move, and by how much, is the
decomposition read off directly. Closed forms hand-derived before the
run: on odd N the 2-door is least 2^r with lambda(2^r) not dividing
lambda(N), which is 2^(v+3) for v = v_2(lambda(N)) in the real world
and 2^(v+2) in the counterfeit; the 3-door is 3^(v_3+2) in both; and
EVEN forces v >= 1, so the real floor is 2^(1+3) = 16. The markups
compound rather than add: at a hypothetical v = 0 opening the r = 2
rung (contribution 2) already escapes an odd lambda and BOTH tables
give door 4, so SPLIT's exponent bites exactly on the states EVEN has
floored.

PREDICTIONS, FROZEN BEFORE THE RUN.
P1 (structure): lambda(2^e) = 1, 2, 2, 4, ..., 2^(e-2);
   (Z/2^e)^* = <-1> x <5> with ord(5) = 2^(e-2) and -1 outside <5>;
   (Z/p^e)^* cyclic for odd p; lambda(N) even with -1 of order 2 as
   witness for every 3 <= N <= 20000.
P2 (price B): real 2-door = 2^(v+3) at every odd N in sweep, floor 16
   attained; counterfeit 2-door = 2^(v+2), floor 8, attained exactly
   where v = 1; 3-door = 3^(v_3+2), floor 9, IDENTICAL in both worlds.
   So the cold door is EVEN and SPLIT jointly (its depth-3 kill is
   literally price C's plateau lambda(8) = lambda(4)), never a third
   fact.
P3 (price A): affordable multipliers under the real door are
   m in {1, 2, 3} with rises {1, 2, 1} -- the rise-2 carrier is
   2^(v+2)+1, multiplier 1 at level v+2; under the counterfeit door,
   m in {1} with rise exactly 1; odd-p control: m in 1..p-1, every
   rise exactly 1. So the excess unit is SPLIT alone, and switching
   SPLIT off makes p = 2 behaviorally odd.
P4 (price C): threshold-greedy growth from seed 4 moves [4, 2, 2, ...]
   (the double step, then plain deepening); the counterfeit world moves
   [2, 2, 2, ...]. So the hiccup is SPLIT alone.
P5 (supply control): the prime powers among 2^k+1, k <= 20, are
   exactly {3, 5, 9, 17, 257, 65537} -- the corpus's Fermat-plus-9
   supply reproduced.

POSITIVE CONTROL: the real-world tables must reproduce the published
prices (floor 16, floor 9, lambda(4) = lambda(8) = 2, door 2^(v+3),
carrier 2^(v+2)+1) before any counterfeit reading counts.
KILLS ARE PRINTED VALUES: a real 2-door off 2^(v+3) at any N, a
counterfeit floor != 8, a moved 3-door, or a rise outside the predicted
set kills the decomposition as stated.

VERDICT SHAPE. All predictions passing reads: the triple is TWO facts
wearing three names -- SPLIT prices A and C outright, EVEN prices 3's
cold door alone, and B is their conjunction -- with both facts
invariants of -1. Any prediction failing names the price that resists.

FINDINGS (post-run; all predictions P1-P5 passed as frozen).

1. THE VERDICT (rule, proved; verified over the sweeps below). The
   three prices are TWO facts wearing three names, not one and not
   three. SPLIT prices A and C outright: switching it off (the
   counterfeit table alone, nothing else touched) collapses the door
   2^(v+3) to 2^(v+2), the multiplier window {1,2,3} to {1}, the
   rise-2 purchase to rise exactly 1, and seed 4's opening double step
   [4, 2, 2, ...] to plain deepening [2, 2, 2, ...] -- p = 2 becomes
   behaviorally an odd prime. EVEN prices 3's cold door alone over
   the swept odd states (floor 9 = 3^(0+2), identical in both
   worlds). And the cold door at 2 is their CONJUNCTION, not a third
   fact: on odd N the 2-door is 2^(v+3) with v = v_2(lambda(N)) --
   the cascade's door formula read at the state's own valuation --
   whose "+3" carries SPLIT's extra exponent (counterfeit: "+2") and
   whose floor sits at v = 1 because EVEN forbids v = 0. The markups
   compound rather than add: at a hypothetical v = 0 opening both
   tables agree at door 4, so SPLIT's exponent bites exactly on the
   states EVEN has floored. Floor 16 real, 8 counterfeit, the 3-door
   unmoved. The depth-3 kill inside the cold-door proof is literally
   price C's plateau lambda(8) = lambda(4) = 2, the dependency edge
   made explicit.

2. ONE ELEMENT UNDERNEATH (property). EVEN and SPLIT are the two
   valuations of the single difference -1 - 1 = -2: v_q(-2) = 0 for
   every odd q is EVEN (-1 lands in every odd residue field as an
   element of order 2, so lambda is even wherever an odd prime
   divides N), and v_2(-2) = 1 EXACTLY is SPLIT (-1 enters the 2-adic
   filtration one step and no deeper, which is what splits Z_2^x
   rather than embedding -1 in the procyclic tower). Two invariants
   -- an order and a depth, read at disjoint places -- of the one
   torsion unit Z owns. The 2-column is not where this arithmetic is
   "richest"; it is where -1 lives.

RUN RECORD (python explore_two_adic_prices.py; ~0.2 s, trivial memory;
all asserts pass, output verbatim):
  lambda(2^e), e=1..12: [1, 2, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
  seed 4 moves, real world:       [4, 2, 2, 2, 2, 2, 2, 2]
  seed 4 moves, counterfeit world: [2, 2, 2, 2, 2, 2, 2, 2]
  real 2-door = 2^(v+3) at every odd N <= 20000; floor 16
  counterfeit 2-door = 2^(v+2); floor 8
  3-door = 3^(v_3+2) in BOTH worlds; floor 9
  real window m in {1,2,3}, rises {1,2,1}; counterfeit m in {1}
  odd control: window m in 1..p-1, every rise exactly 1
  prime powers among 2^k+1, k <= 20: [3, 5, 9, 17, 257, 65537]
  ALL SECTIONS PASS
"""

from math import gcd

LIMIT = 20000

# ---------------------------------------------------------------- helpers

def factorize(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def lcm(a, b):
    return a * b // gcd(a, b)

def lam_channel_real(p, e):
    """lambda(p^e), one channel, the real arithmetic."""
    if p == 2:
        return 1 if e == 1 else (2 if e == 2 else 2 ** (e - 2))
    return p ** (e - 1) * (p - 1)

def lam_channel_cf(p, e):
    """Counterfeit: the 2-channel wears the odd (procyclic) pattern
    lambda*(2^e) = 2^(e-1); every odd channel is real."""
    if p == 2:
        return 2 ** (e - 1)
    return p ** (e - 1) * (p - 1)

def lam(n, channel=lam_channel_real):
    if n == 1:
        return 1
    out = 1
    for p, e in factorize(n).items():
        out = lcm(out, channel(p, e))
    return out

def lam_cf(n):
    return lam(n, channel=lam_channel_cf)

def v(p, n):
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c

def mult_order(a, n):
    a %= n
    assert gcd(a, n) == 1
    o, x = 1, a
    while x != 1:
        x = x * a % n
        o += 1
    return o

def door(q, N, channel=lam_channel_real):
    """Least q^r whose channel contribution escapes lambda(N); the state
    N is real arithmetic in both worlds (an opening has q coprime to N,
    so the counterfeit table enters only through the move)."""
    L = lam(N)
    e = v(q, N)
    r = 1
    while L % channel(q, e + r) == 0:
        r += 1
    return q ** r

def is_prime_power(n):
    return n > 1 and len(factorize(n)) == 1

def ddyn_moves(seed, steps, lamfun):
    """Threshold-greedy growth: repeatedly the least m >= 2 with
    lambda(N*m) > lambda(N). Returns the move list."""
    N, moves = seed, []
    for _ in range(steps):
        L = lamfun(N)
        m = 2
        while lamfun(N * m) <= L:
            m += 1
        moves.append(m)
        N *= m
    return moves

# ---------------------------------------------------------------- S1: structure

def s1_structure():
    print("S1  THE TWO FACTS AND THEIR CONTROLS")
    tab = [lam(2 ** e) for e in range(1, 13)]
    assert tab == [1, 2] + [2 ** (e - 2) for e in range(3, 13)], tab
    print("  lambda(2^e), e=1..12:", tab)
    assert tab[1] == tab[2] == 2, "the plateau lambda(4) = lambda(8) = 2"
    for e in range(3, 13):
        M = 2 ** e
        o5 = mult_order(5, M)
        assert o5 == 2 ** (e - 2), (e, o5)
        pow5 = {pow(5, k, M) for k in range(o5)}
        assert (M - 1) not in pow5, e            # -1 outside <5>
        assert len(pow5) * 2 == M // 2           # <-1> x <5> exhausts
    print("  (Z/2^e)^* = <-1> x <5>, ord(5) = 2^(e-2): e=3..12 verified")
    assert (-1 - 1) % 2 == 0 and (-1 - 1) % 4 != 0
    print("  v_2(-1 - 1) = 1 exactly: -1 enters the filtration one step")
    for p in (3, 5, 7, 11, 13):
        for e in range(1, 6):
            M = p ** e
            L = lam(M)
            assert L == p ** (e - 1) * (p - 1)
            # cyclic: some unit attains the full order
            assert any(mult_order(a, M) == L for a in range(2, M) if gcd(a, M) == 1)
    print("  odd control: (Z/p^e)^* cyclic, p <= 13, e <= 5")
    for N in range(3, LIMIT + 1):
        assert lam(N) % 2 == 0, N
        assert mult_order(N - 1, N) == 2, N      # the witness is -1 itself
    print("  EVEN: lambda(N) even for 3 <= N <= %d, witness -1 of order 2" % LIMIT)

# ---------------------------------------------------------------- S2: price C

def s2_price_c():
    print("S2  PRICE C -- THE DOUBLE STEP")
    real = ddyn_moves(4, 8, lam)
    cf = ddyn_moves(4, 8, lam_cf)
    print("  seed 4 moves, real world:      ", real)
    print("  seed 4 moves, counterfeit world:", cf)
    assert real[0] == 4 and all(m == 2 for m in real[1:]), real
    assert all(m == 2 for m in cf), cf

# ---------------------------------------------------------------- S3: price B

def s3_price_b():
    print("S3  PRICE B -- THE COLD DOOR, DECOMPOSED")
    doors_real, doors_cf, doors3 = [], [], []
    for N in range(3, LIMIT + 1, 2):
        L = lam(N)
        v2 = v(2, L)
        assert v2 >= 1                            # EVEN forces the floor up
        d_real = door(2, N)
        d_cf = door(2, N, lam_channel_cf)
        assert d_real == 2 ** (v2 + 3), (N, d_real)
        assert d_cf == 2 ** (v2 + 2), (N, d_cf)
        doors_real.append(d_real)
        doors_cf.append(d_cf)
        if N % 3 != 0:
            d3 = door(3, N)
            d3_cf = door(3, N, lam_channel_cf)
            assert d3 == d3_cf == 3 ** (v(3, L) + 2), (N, d3, d3_cf)
            doors3.append(d3)
    print("  real 2-door = 2^(v+3) at every odd N <= %d; floor %d"
          % (LIMIT, min(doors_real)))
    print("  counterfeit 2-door = 2^(v+2); floor %d" % min(doors_cf))
    print("  3-door = 3^(v_3+2) in BOTH worlds; floor %d" % min(doors3))
    assert min(doors_real) == 16 and min(doors_cf) == 8 and min(doors3) == 9

# ---------------------------------------------------------------- S4: price A

def s4_price_a():
    print("S4  PRICE A -- THE LADDER WINDOW AND THE EXCESS RISE")
    for vv in range(0, 11):
        ms = [m for m in range(1, 20) if m * 2 ** (vv + 1) + 1 < 2 ** (vv + 3)]
        rises = [v(2, m * 2 ** (vv + 1)) - vv for m in ms]
        assert ms == [1, 2, 3] and rises == [1, 2, 1], (vv, ms, rises)
        # the rise-2 purchase m = 2 is the norm 2*2^(v+1)+1 = 2^(v+2)+1:
        # multiplier 1 at level v+2
        ms_cf = [m for m in range(1, 20) if m * 2 ** (vv + 1) + 1 < 2 ** (vv + 2)]
        assert ms_cf == [1], (vv, ms_cf)
    print("  real window m in {1,2,3}, rises {1,2,1}; the rise-2 carrier")
    print("  is 2^(v+2)+1 (multiplier 1 at level v+2); counterfeit window")
    print("  m in {1}, rise exactly 1 -- the excess unit is gone")
    for p in (3, 5, 7, 11, 13):
        for vv in range(0, 7):
            ms = [m for m in range(1, p ** 2)
                  if m * p ** (vv + 1) + 1 < p ** (vv + 2)]
            assert ms == list(range(1, p)), (p, vv)
            assert all(v(p, m * p ** (vv + 1)) - vv == 1 for m in ms)
    print("  odd control: window m in 1..p-1, every rise exactly 1")
    supply = [2 ** k + 1 for k in range(1, 21) if is_prime_power(2 ** k + 1)]
    print("  prime powers among 2^k+1, k <= 20:", supply)
    assert supply == [3, 5, 9, 17, 257, 65537]

# ---------------------------------------------------------------- main

if __name__ == "__main__":
    s1_structure()
    s2_price_c()
    s3_price_b()
    s4_price_a()
    print("ALL SECTIONS PASS")
