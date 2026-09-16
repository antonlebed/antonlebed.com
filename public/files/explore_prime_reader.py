"""
explore_prime_reader.py -- THE PRIME READER: in the one-AND clock class,
where a true read leaves only control and the grow count
(explore_one_and.py), what does one trip read off the supply m_g = g + 1?
Does a trip read the primality of the next modulus, and is every trip
exit a function of prime-power facts about the next few moduli?

THE SETTING. The class of explore_one_and.py: banks of windows over a
supply m_g, ops TICK(b, s) at every window of bank b, PULSE(b, s) at
the newest window, GROW (a window at phase 0 in every bank), and one
TEST, true when every window of every bank is 0. After g grows on m_g =
g + 1 the moduli are 2..g + 1, and C = lcm(2..g + 1). A trip starts at a
true read, every window 0, and runs the lasso u v v ... of its start
state until a TEST reads true.

THE QUESTIONS.
  Q1 THE PRIME READER R: u = GROW, v = TICK(B, +1), TEST, PULSE(B, +1),
     TEST, PULSE(B, -1). Does its trip end at the second TEST iff g + 2
     is prime, at every g up to 200?
  Q2 THE CONVERSE: is every trip exit a function of prime-power facts
     about the next few moduli and of g modulo program constants, so that
     halting in the class is a finite automaton over the prime-power word?

THE HAND ATTACK (before any engine code).
  (1) A GROW-FREE LOOP IS A LINEAR CONGRUENCE SYSTEM IN THE PASS. With no
      GROW in v, a window of bank b other than the newest holds, at a TEST
      position t of pass k, the integer c + k n_b, n_b the net tick of one
      pass; the newest holds c' + k (n_b + P_b), P_b the net pulse. So the
      TEST at t reads true in pass k iff every window's congruence A k + c
      = 0 mod m holds, each solvable iff gcd(A, m) divides c, and the
      conjunction is one generalized CRT progression k = r mod L or empty.
      The trip exits at the least (k, t) over the positions, and the pass
      runs to C (g + 2), far past any step engine at g = 200: the rig is
      that solver, bisimulated against a step engine at small g.
  (2) THE PRIME READER. At the first TEST of pass k the old windows hold
      k and the newest k (the pulses of earlier passes cancel), so k = 0
      mod C and mod g + 2, least k = lcm(C, g + 2). At the second TEST the
      newest holds k + 1: k = 0 mod C and k = -1 mod g + 2, solvable iff
      gcd(C, g + 2) = 1, iff no prime below g + 2 divides it, iff g + 2 is
      prime; then k = C x with x = -C^-1 mod p in 1..p - 1, below lcm =
      C p. So R exits at the second TEST in pass C ((-C^-1) mod p) when p =
      g + 2 is prime, and otherwise at the first TEST in pass C, or p C
      when g + 2 = p^a with a >= 2 (there v_p(C) = a - 1).
  (3) THE CONVERSE FAILS: THE ORDER READER O. u = GROW, v = TICK(B, +1),
      PULSE(B, -1), TEST, PULSE(B, -1), TEST, PULSE(B, +2). The pulses
      cancel over a pass; the newest holds k - 1 at the first TEST and k -
      2 at the second, the old windows k. Composite g + 2 not a prime
      power divides C, so neither is solvable; g + 2 = p^a, a >= 2, puts
      p^(a-1) | k against k = 1 or 2 mod p^a, solvable only at g + 2 = 4
      (the second TEST, k = 6). At a prime p = g + 2 >= 3 both are
      solvable: k = C x at the first and C (2x mod p) at the second, x =
      C^-1 mod p, so the trip exits at the first TEST iff x < p/2. That
      bit, b(p) = [lcm(1..p - 1)^-1 mod p < p/2], is a residue of the
      lcm, not a fact about which moduli are prime powers; nothing known
      makes it a function of p modulo a constant.
  (4) WHAT A GROW-FREE TRIP READS, argued. Past a program constant every
      |A| and |c| is below every modulus's prime-power content, so
      gcd(A, C) = |A|, the old windows reduce to k = r mod C/d with r and d
      program constants (or to no constraint, or to none solvable), and
      the new windows' congruences mod m_(g+1)..m_(g+h) meet it through
      gcd(C, m) and gcd(m, m') -- prime-power letters of the new moduli and
      g modulo constants -- and through C mod (d m), which fixes where the
      least solutions fall. Comparing positions compares those least
      solutions. So an exit is a function of the letters, g modulo a
      program constant and the residues of C modulo constant multiples of
      the new moduli; (3) shows the last is not removable. A trip whose
      loop grows reads integers below its moduli past a program constant
      (explore_one_and.py), so its exit is eventually independent of g.
  TRANSPLANT (marked): "the bit looks like a coin" is imported from the
  behaviour of generic residues; the rig reads it, it does not assume it.

THE PREDICTIONS (frozen before the run).
  P1 R on m_g = g + 1, g = 0..200: the solver's exit is the second TEST
     iff g + 2 is prime, and its pass is C ((-C^-1) mod p), C, or p C as
     in (2).
  P2 O on m_g = g + 1, g = 0..200: the trip ends iff g + 2 is prime or g
     + 2 = 4; at g = 0 the first TEST in pass 1, at g = 2 the second in
     pass 6, and at a prime p >= 3 the first TEST iff x < p/2, in pass C x
     or C (2x mod p).
  P3 Over primes 3 <= p <= 2000, reading b(p) off the solver's exits (not
     off the formula), for every L in 1..40 there are primes p, p' with p
     = p' mod L and the same letters (prime, proper prime power, other) at
     p - 2, p - 1, p + 1, p + 2 whose bits differ.
THE KILLS, as prints: P1's line printing an exit position that disagrees
with primality at any g <= 200 (the prime reader dies); P3's line
printing an L <= 40 with no differing pair (the converse survives that
key at that L, and (3) does not refute it there).

THE CONTROLS (run before any prediction is read).
  C1 BISIMULATION. On random programs whose loop is grow-free and holds a
     TEST (ops of size 1 or 2), from g_start windows at zero, the solver
     and a step engine agree on (ended, pass, TEST state) wherever the
     step engine ends within its pass cap, and the solver's pass exceeds
     the cap wherever it does not: on m_g = g + 1 at g_start 0..6 and on
     the sqrt pole at g_start 0..30.
  C2 THE STEP ENGINE ALONE runs R and O at g = 0..6 and prints the
     exits (2) and (3) predict, no solver involved.
  C3 THE COLLISION FINDER SEES STRUCTURE: fed [p = 1 mod 4] in place of
     b(p), it must print no differing pair at L = 4 and one at L = 3.

ADDED AFTER THE FIRST RUN (marked; the first run's prints met P1-P3).
  P4 THE PLANTED BIT. On the supply m_(2j-1) = p_j, the j-th prime, and
     m_2j = the j-th prime from 10007 (bit 1) or 2^14 (bit 0), bits drawn
     at random for j = 1..60, R from a true read at g = 2j - 1 exits at
     the second TEST iff bit j is 1: the argument of (2) needs only
     gcd(C, m_(g+1)) = 1, which a new prime meets and a power of 2 does
     not. Printed as a separation count; a miss at any j is a print.

RESOURCE ENVELOPE (named before the run): at most ~2000 windows per bank
with integers of at most ~900 digits; under 100 MB and under a minute,
run under memwatch.

PREDICTIONS ADJUDICATED (post-run). P1-P4 CONFIRMED; neither kill
fired; C1-C3 passed before any prediction was read.

FINDINGS (entered after the run; every number is printed output).

1. ONE TRIP READS WHETHER THE NEXT MODULUS IS PRIME (rule, argued in (2)
   for every g; checked by the exact solver at g = 0..200). R exits at
   its second TEST at exactly the 46 g <= 200 with g + 2 prime, and at
   every g in the pass (2) names, up to C (g + 2) passes. The argument
   reads only gcd(C, m_(g+1)) = 1 with m_(g+1) > 1 (at modulus 1 both
   TESTs solve at pass C and the first wins), so on any supply one trip
   separates a modulus above 1 coprime to every earlier one from one
   that is not: on 60
   planted windows, 36 new primes against 2^14, it separated 60 of 60
   (P4).

2. THE CONVERSE IS FALSE: A TRIP READS A RESIDUE OF THE LCM, NOT ONLY
   PRIME-POWER FACTS (observation for the refuted key, argued in (3) for
   the reading). O ends at exactly the 47 g <= 200 with g + 2 prime or 4,
   and at a prime p >= 3 exits at the first TEST iff lcm(1..p - 1)^-1
   mod p < p/2, at every g as (3) predicts. Read off the solver over the
   302 primes from 3 to 2000 the bit is 1 at 147; for every L from 1 to
   40 two primes agree mod L and in the letters of p - 2, p - 1, p + 1,
   p + 2 and differ in the bit ((23, 47) at L = 1, 4, 12, 24; (19, 139)
   at L = 40). So a trip's exit is not a function of those local letters
   and p mod L at any L <= 40; what a trip reads, by (4), is those
   letters, g mod a program constant and C mod constant multiples of the
   next moduli, and (3) exhibits the last as a bit of its own.

The solver and the step engine agreed on 2,800 trips on m_g = g + 1
(1,722 ending within 4,000 passes) and 1,860 on the sqrt pole (1,020);
the step engine alone printed (2) and (3) at g = 0..6 (C1, C2).

SCOPE + HONESTY. Finding 1's pass formula and Finding 2's bit formula
are proved in (2) and (3) and checked to g = 200; the refutation in
Finding 2 is of one key at L <= 40 over primes <= 2000, and the
stronger claim, that no finite automaton reading the prime-power word
decides the bit, is not printed and not proved: a run reads one bit
per prime at best along its trips, and whether such bits have any
automatic structure is number theory this rig does not touch. (4) is
argued, not rigged. Whether halting in the class is decidable on m_g =
g + 1 is not claimed either way; O alone halts or hangs on the bit's
neighbour, primality, so halting questions in the class reach at least
that far into the primes.

RUN RECORD (python prime/code/memwatch.py
prime/code/explore_prime_reader.py; 6.3 s wall clock, 13.1 MB peak
working set, 21 checks). C1 linear 2800 trips (1722 ended, 1078 capped
at 4000 passes), sqrt 1860 (1020, 840). C2 g=0..6 R passes 1, 2, 12,
24, 60, 300, 840; O passes 1, 2, 6, 12, cap, 120, cap. C3 L=4 none,
L=3 (13, 19). P1 46 second-TEST exits, 0 disagreements. P2 47 ends, 25
at the first TEST. P3 302 primes, 147 ones, first 30 bits
001101001101011000111001010111, no L <= 40 without a pair. P4 36 bits
set, 60 of 60 separated.
"""

import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_one_and import Offset, apply, lasso, linear, sqrt_pole

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1
    print("  [ok] " + msg)


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, math.isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def letter(n):
    """'p' prime, 'q' a prime power with exponent >= 2, 'o' otherwise."""
    if is_prime(n):
        return "p"
    for p in range(2, math.isqrt(n) + 1):
        if n % p == 0:
            while n % p == 0:
                n //= p
            return "q" if n == 1 else "o"
    return "o"


def merge(r1, l1, r2, l2):
    """k = r1 mod l1 and k = r2 mod l2, or None."""
    d = math.gcd(l1, l2)
    if (r2 - r1) % d:
        return None
    step = l2 // d
    t = ((r2 - r1) // d) * pow(l1 // d % step, -1, step) % step if step > 1 \
        else 0
    l = l1 * step
    return (r1 + t * l1) % l, l


def solve_one(a, c, m):
    """a k + c = 0 mod m as (r, l), or None."""
    g0 = math.gcd(a % m, m)
    if c % g0:
        return None
    l = m // g0
    if l == 1:
        return 0, 1
    return (-c // g0) * pow((a // g0) % l, -1, l) % l, l


def solve_trip(prog, m_of, g_start, q=0, nbanks=2):
    """Exact trip from every window 0 after g_start grows. Returns
    ('u', state) for a true read in u, ('v', pass, state) for the first
    true read of the loop, ('never',), or None when the loop grows."""
    eng = Offset(m_of, nbanks)
    for _ in range(g_start):
        eng.grow()
    u, v = lasso(prog, q)
    for s in u:
        op = prog[s]
        if op[0] == "test":
            if eng.test():
                return ("u", s)
        else:
            apply(eng, op)
    kinds = [prog[s][0] for s in v]
    if "grow" in kinds:
        return None
    if "test" not in kinds:
        return ("never",)
    n = [0] * nbanks
    p_net = [0] * nbanks
    positions = []
    for s in v:
        op = prog[s]
        if op[0] == "test":
            positions.append((s, list(n), list(p_net)))
        elif op[0] == "tick":
            n[op[1]] += op[2]
        elif op[0] == "pulse":
            p_net[op[1]] += op[2]
    nw = len(eng.moduli)
    best = None
    for idx, (s, tau, pi) in enumerate(positions):
        if nw == 0:
            k = 1
        else:
            sys_rl = (0, 1)
            for b in range(nbanks):
                for w in range(nw):
                    m = eng.moduli[w]
                    newest = w == nw - 1
                    a = n[b] + (p_net[b] if newest else 0)
                    c = (eng.t[b] - eng.base[b][w] + tau[b]
                         + (pi[b] if newest else 0) - a)
                    one = solve_one(a, c, m)
                    if one is None:
                        sys_rl = None
                        break
                    sys_rl = merge(sys_rl[0], sys_rl[1], one[0], one[1])
                    if sys_rl is None:
                        break
                if sys_rl is None:
                    break
            if sys_rl is None:
                continue
            k = sys_rl[0] if sys_rl[0] > 0 else sys_rl[1]
        if best is None or (k, idx) < best[:2]:
            best = (k, idx, s)
    if best is None:
        return ("never",)
    return ("v", best[0], best[2])


def step_trip(prog, m_of, g_start, pass_cap, q=0, nbanks=2):
    """The step engine: ('u', state), ('v', pass, state) or ('cap',)."""
    eng = Offset(m_of, nbanks)
    for _ in range(g_start):
        eng.grow()
    u, v = lasso(prog, q)
    for s in u:
        op = prog[s]
        if op[0] == "test":
            if eng.test():
                return ("u", s)
        else:
            apply(eng, op)
    for k in range(1, pass_cap + 1):
        for s in v:
            op = prog[s]
            if op[0] == "test":
                if eng.test():
                    return ("v", k, s)
            else:
                apply(eng, op)
    return ("cap",)


# R: states 0 GROW; 1 TICK; 2 TEST (first); 3 PULSE +1; 4 TEST (second);
# 5 PULSE -1; 6, 7 sinks.
READER = [
    ("grow", 1),
    ("tick", 1, 1, 2),
    ("test", 6, 3),
    ("pulse", 1, 1, 4),
    ("test", 7, 5),
    ("pulse", 1, -1, 1),
    ("test", 6, 6),
    ("test", 7, 7),
]
R_FIRST, R_SECOND = 2, 4

# O: states 0 GROW; 1 TICK; 2 PULSE -1; 3 TEST (first); 4 PULSE -1;
# 5 TEST (second); 6 PULSE +2; 7, 8 sinks.
ORDER = [
    ("grow", 1),
    ("tick", 1, 1, 2),
    ("pulse", 1, -1, 3),
    ("test", 7, 4),
    ("pulse", 1, -1, 5),
    ("test", 8, 6),
    ("pulse", 1, 2, 1),
    ("test", 7, 7),
    ("test", 8, 8),
]
O_FIRST, O_SECOND = 3, 5


def lcm_to(n):
    c = 1
    for i in range(2, n + 1):
        c = c * i // math.gcd(c, i)
    return c


def reader_expected(g):
    c, m = lcm_to(g + 1), g + 2
    if is_prime(m):
        return ("v", c * ((-pow(c, -1, m)) % m), R_SECOND)
    if letter(m) == "q":
        p = next(d for d in range(2, m + 1) if m % d == 0)
        return ("v", p * c, R_FIRST)
    return ("v", c, R_FIRST)


def order_expected(g):
    c, m = lcm_to(g + 1), g + 2
    if g == 0:
        return ("v", 1, O_FIRST)
    if m == 4:
        return ("v", 6, O_SECOND)
    if not is_prime(m):
        return ("never",)
    x = pow(c, -1, m)
    if x < m / 2:
        return ("v", c * x, O_FIRST)
    return ("v", c * (2 * x % m), O_SECOND)


def grow_free_program(rng, nbanks=2):
    """A random lasso: u of 0..3 ops, v of 2..7 grow-free ops holding a
    TEST, true edges to a sink."""
    nu, nv = rng.randrange(4), rng.randrange(2, 8)
    n = nu + nv
    while True:
        vk = [rng.choice(("tick", "tick", "pulse", "pulse", "test"))
              for _ in range(nv)]
        if "test" in vk:
            break
    kinds = [rng.choice(("tick", "pulse", "grow", "grow", "test"))
             for _ in range(nu)] + vk
    prog = []
    for i, kind in enumerate(kinds):
        nxt = i + 1 if i + 1 < n else nu
        if kind in ("tick", "pulse"):
            prog.append((kind, rng.randrange(nbanks),
                         rng.choice((1, -1, 2, -2)), nxt))
        elif kind == "grow":
            prog.append(("grow", nxt))
        else:
            prog.append(("test", n, nxt))
    prog.append(("test", n, n))
    return prog


def c1_bisimulation():
    print("C1 solver against the step engine")
    rng = random.Random(23)
    cap = 4000
    for name, m_of, starts, count in (("linear", linear, range(0, 7), 400),
                                      ("sqrt", sqrt_pole, range(0, 31), 60)):
        agree = ended = capped = 0
        for g0 in starts:
            for _ in range(count):
                prog = grow_free_program(rng)
                sol = solve_trip(prog, m_of, g0)
                st = step_trip(prog, m_of, g0, cap)
                if st[0] == "cap":
                    capped += 1
                    assert sol[0] == "never" or (sol[0] == "v"
                                                 and sol[1] > cap), (prog, g0,
                                                                     sol)
                else:
                    ended += 1
                    assert sol == st, (prog, g0, sol, st)
                agree += 1
        print("  %s: %d trips agree (%d ended within %d passes, %d capped)"
              % (name, agree, ended, cap, capped))
        ok(ended > 0 and capped > 0, "C1 %s solver matches step engine" % name)


def c2_step_alone():
    print("C2 the step engine alone on R and O, g = 0..6")
    for g in range(0, 7):
        r = step_trip(READER, linear, g, 20000)
        o = step_trip(ORDER, linear, g, 20000)
        eo = order_expected(g)
        print("  g=%d  R %s  O %s" % (g, r, o))
        ok(r == reader_expected(g), "C2 R at g=%d as (2)" % g)
        ok(o == eo or (eo == ("never",) and o == ("cap",)),
           "C2 O at g=%d as (3)" % g)


def differing_pair(primes, bit, L):
    seen = {}
    for p in primes:
        key = (p % L, letter(p - 2), letter(p - 1), letter(p + 1),
               letter(p + 2))
        if key in seen and seen[key][1] != bit[p]:
            return seen[key][0], p
        seen.setdefault(key, (p, bit[p]))
    return None


def c3_finder():
    print("C3 the collision finder on [p = 1 mod 4]")
    primes = [p for p in range(3, 2001) if is_prime(p)]
    bit = {p: p % 4 == 1 for p in primes}
    at4, at3 = differing_pair(primes, bit, 4), differing_pair(primes, bit, 3)
    print("  L=4 %s  L=3 %s" % (at4, at3))
    ok(at4 is None and at3 is not None, "C3 no pair at 4, a pair at 3")


def p1_reader():
    print("P1 the prime reader, m_g = g + 1, g = 0..200")
    bad = 0
    seconds = 0
    for g in range(0, 201):
        sol = solve_trip(READER, linear, g)
        second = sol[0] == "v" and sol[2] == R_SECOND
        seconds += second
        if second != is_prime(g + 2):
            bad += 1
            print("  KILL g=%d exit %s" % (g, sol[:1] + sol[2:]))
        assert sol == reader_expected(g), (g, sol)
    print("  exits at the second TEST: %d; disagreements with primality: %d"
          % (seconds, bad))
    ok(bad == 0, "P1 R's exit reads g + 2 prime at every g <= 200")


def p2_order():
    print("P2 the order reader, m_g = g + 1, g = 0..200")
    ends = firsts = 0
    for g in range(0, 201):
        sol = solve_trip(ORDER, linear, g)
        assert sol == order_expected(g), (g, sol)
        if sol[0] == "v":
            ends += 1
            firsts += sol[2] == O_FIRST
    print("  ends %d, at the first TEST %d" % (ends, firsts))
    ok(True, "P2 O's exits as (3) at every g <= 200")


def p3_bit():
    print("P3 the order bit off the solver, primes 3..2000")
    primes = [p for p in range(3, 2001) if is_prime(p)]
    bit = {}
    for p in primes:
        sol = solve_trip(ORDER, linear, p - 2)
        bit[p] = sol[2] == O_FIRST
    ones = sum(bit.values())
    print("  primes %d, first-TEST exits %d" % (len(primes), ones))
    print("  first 30 bits: %s" % "".join("1" if bit[p] else "0"
                                           for p in primes[:30]))
    missing = []
    for L in range(1, 41):
        pair = differing_pair(primes, bit, L)
        if pair is None:
            missing.append(L)
        elif L in (1, 4, 12, 24, 40):
            print("  L=%d differing pair %s" % (L, pair))
    print("  L with no differing pair: %s" % missing)
    ok(not missing, "P3 no L <= 40 makes the bit a function of the key")


def p4_planted():
    print("P4 the planted bit, R on primes interleaved with planted windows")
    rng = random.Random(29)
    base = [p for p in range(2, 400) if is_prime(p)][:60]
    fresh = [p for p in range(10007, 11000) if is_prime(p)][:60]
    bits = [rng.randrange(2) for _ in range(60)]
    supply = []
    for j in range(60):
        supply += [base[j], fresh[j] if bits[j] else 2 ** 14]

    def m_of(g):
        return supply[g - 1]

    hits = 0
    for j in range(60):
        sol = solve_trip(READER, m_of, 2 * j + 1)
        hits += (sol[0] == "v" and sol[2] == R_SECOND) == bool(bits[j])
    print("  bits set %d of 60; exits separating the bit %d of 60"
          % (sum(bits), hits))
    ok(hits == 60, "P4 R separates a planted prime from a power of 2")


def main():
    c1_bisimulation()
    c2_step_alone()
    c3_finder()
    p1_reader()
    p2_order()
    p3_bit()
    p4_planted()
    print("%d checks" % CHECKS)


if __name__ == "__main__":
    main()
