"""
explore_lcm_wait.py -- THE LCM IS WAITED OUT: in the one-AND clock class
(explore_one_and.py), must every trip exit that depends on the moduli
grown long ago wait out their lcm?

THE SETTING. The class and the exact trip solver of
explore_prime_reader.py: banks of windows over a supply m_g, ops TICK(b,
s) at every window of bank b, PULSE(b, s) at the newest, GROW, and one
TEST reading every window of every bank at zero. A trip starts at a true
read after g grows, every window 0, and runs the lasso u v v ... of its
start state. The prime reader exits at its second TEST iff gcd(C,
m_(g+1)) = 1, C the lcm grown, in pass C ((-C^-1) mod m_(g+1)): its
read of the gcd costs a pass of order C. The question is whether that
cost is the reader's or the class's.

THE HAND ATTACK (before any engine code).
  (1) THE DEEP WINDOWS. Call the windows grown before the trip, all but
      the last of them, DEEP, and C' the lcm of their moduli. No PULSE
      reaches a deep window during the trip (a pulse hits the newest, and
      from the trip's start the newest is window g or later), so every
      deep window of bank b holds the same integer X_b, at every TEST
      position, as it received the same ticks from 0.
  (2) A TRUE READ ON THE DEEP WINDOWS IS AN INTEGER EQUATION OR A LONG
      WAIT. The TEST reads all deep windows zero iff C' divides X_b for
      every b, so iff X_b = 0 or |X_b| >= C'. In a grow-free loop X_b = n_b
      k + c_b at pass k, n_b the net tick of one pass and c_b a program
      constant; so a true read at pass k < (C' - K) / N, K = max |c_b| and
      N = max |n_b| (N >= 1), has X_b = 0 for every b exactly. That set of
      passes is fixed by the program alone: empty, one pass, or every
      pass (n_b = c_b = 0). In the u part, and in a loop holding a GROW
      (which ends by its fourth pass or never past a program constant,
      explore_one_and.py), the ticks are bounded by a program constant, so
      past C' > that constant the deep condition is again X_b = 0.
  (3) SO THE FAST EXIT IGNORES THE DEEP MODULI. Every other window (the
      last pre-trip window and every window the trip grows) reads a
      congruence mod its own modulus, with coefficients the program
      fixes. So every candidate true read at a pass below (C' - K) / N is
      a function of the program and the moduli m_g, m_(g+1), ... of the
      windows past the deep ones; the exit is the least candidate. If two
      supplies agree on those moduli and on the program, and one trip's
      exit falls below both bounds, the other trip's exit is the same
      position at the same pass. A trip whose exit depends on the deep
      moduli exits at a pass >= (C' - K) / N on at least one of them.
  (4) NO CHEAP TRIAL DIVISION. A trip that separates gcd(C', m') = 1 from gcd
      > 1 at a fixed next modulus m' is such a trip, so one outcome waits
      at least (C' - K) / N passes, K and N program constants; on m_g = g
      + 1, C' = lcm(2..g) = e^(g(1 + o(1))), so no trip reads that gcd in
      passes polynomial in g. The read costs time of order the lcm, which
      is the cost of the trial division it would replace.

THE PREDICTIONS (frozen before the run).
  P1 THE FAST-EXIT EQUALITY. For 3,000 random programs (u of 0..4 ops
     with GROWs and pulses allowed, a grow-free loop of 2..7 ops holding a
     TEST, tick and pulse sizes 1 or 2), each run on a pair of supplies
     sharing the last pre-trip modulus and the next four moduli and
     differing in the deep moduli (deep A: the primes 2..p_d, deep B: the
     first d odd primes from 3 times 2 and 4 at two slots, both lcm > 10^6
     and unequal), whenever the A exit's pass is below min((C'_A - K)/N,
     (C'_B - K)/N), the B exit is the same position at the same pass, and
     conversely. Printed as a count of violations: 0.
  P2 THE READ IS PAID. Among the pairs whose exits differ, every one has
     the larger of the two passes at or above its own supply's bound;
     printed as the least ratio pass / bound over differing pairs, >= 1,
     and the count of differing pairs > 0.
  P3 THE PRIME READER'S PRICE. On the planted supplies (deep moduli the
     first d primes, last pre-trip modulus 2^14, next modulus a prime q
     from 10007 or 3 times a deep prime) at d = 5..12, R exits at its second
     TEST exactly at the new prime and its pass there is >= C'.
THE KILLS, as prints: P1's violation count above 0 (the fast exit reads
deep moduli: the derivation is wrong); P2's
least ratio below 1.

THE CONTROLS (run before any prediction is read).
  C1 THE SUPPLY PAIRS DIFFER DEEP AND AGREE NEAR: printed moduli lists,
     C'_A != C'_B, the near moduli equal.
  C2 THE COMPARATOR SEES A DEEP READ. The prime reader R on a pair whose
     next modulus 15 is coprime to deep B's moduli only if deep B holds
     no 3 or 5: the pair must print differing exits (the comparison is
     not blind).
  C3 THE SOLVER against the step engine on 200 random programs at deep
     d = 3 (lcm 30), pass cap 3,000: agreement wherever the step engine
     ends.

RESOURCE ENVELOPE (named before the run): at most ~20 windows per bank,
integers of at most ~60 digits, ~6,500 solver trips; under 30 MB and
under a minute, run under memwatch.

ERRATA TO THE SLATE (marked, found reading the prints against the code;
no prediction's content changes): P1's u has 0..3 ops, not 0..4 (the
generator of explore_prime_reader.py), and deep B is [2, 4] followed by
the odd primes 3..p_(d-1), every slot i >= 3 with i divisible by 3
multiplied by 3, as C1 prints.

PREDICTIONS ADJUDICATED (post-run). P1-P3 CONFIRMED; neither kill fired;
C1-C3 passed before any prediction was read.

FINDINGS (entered after the run; every number is printed output).

1. EVERY EXIT THAT READS THE DEEP MODULI WAITS OUT THEIR LCM (rule,
   argued in (1)-(3) for every program past a program constant; checked
   by the exact solver on 3,000 supply pairs). A true read below pass (C'
   - K)/N is an integer equation on the deep windows and a congruence on
   the near ones, so it ignores the deep moduli: on 1,184 pairs with an
   exit below both bounds, 0 differed. The 428 pairs whose exits differ
   all waited, the least pass/bound 1.000000000004986, so the bound is
   attained up to its constant K.

2. THE PRIME READER PAYS THE CLASS'S PRICE, NOT ITS OWN (observation on
   planted supplies d = 5..12). R exits second at each new prime and
   first at 3 p_d, at passes 8,192 to 70,647,808 times C', the 2^14
   near window multiplying C. So by (4) no one-read trip reads
   gcd(C', m') in passes polynomial in g on m_g = g + 1; coincidence
   trial division costs the lcm it would have divided by.

SCOPE + HONESTY. The argument is for trips from a true read, which is
every trip in the class; the rig's loops are grow-free with u holding up
to three GROWs, and loops holding a GROW rest on explore_one_and.py's
pass bound, argued there, not rigged here. The deep/near split puts the
last pre-trip window with the near ones because pulses before the first
GROW reach it; a read of that one modulus is not an lcm read.

RUN RECORD (python prime/code/memwatch.py
prime/code/explore_lcm_wait.py; 0.5 s wall clock, 11.5 MB peak working
set, 7 checks). C1 d = 8: C'_A 9699690, C'_B 1021020; d = 12:
7420738134810, 401120980260. C2 deep [2, 7, 11, 13] -> second TEST pass
16400384; deep [2, 3, 7, 11] -> first TEST pass 18923520. C3 200
programs, 108 ended within 3,000 passes, 200 agree. P1 1,184 fast, 0
violations. P2 428 differing, least ratio 1.000000000004986. P3 all 16
exits as predicted.
"""

import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_prime_reader import (READER, R_SECOND, is_prime, solve_trip,
                                  step_trip, grow_free_program)

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1
    print("  [ok] " + msg)


def lcm_list(ms):
    c = 1
    for m in ms:
        c = c * m // math.gcd(c, m)
    return c


def supply_of(ms):
    return lambda g: ms[g - 1]


def constants(prog, q=0, nbanks=2):
    """N = max |net tick of v| (at least 1), K = a bound on every |c_b|:
    the sum of |tick sizes| over u and v plus N."""
    from explore_one_and import lasso
    u, v = lasso(prog, q)
    n = [0] * nbanks
    for s in v:
        if prog[s][0] == "tick":
            n[prog[s][1]] += prog[s][2]
    total = sum(abs(prog[s][2]) for s in u + v if prog[s][0] == "tick")
    big_n = max(1, max(abs(x) for x in n))
    return big_n, total + big_n


def pass_of(sol):
    """Pass of a solver result; 0 for a read in u; None for never."""
    if sol[0] == "u":
        return 0
    if sol[0] == "v":
        return sol[1]
    return None


def deep_pair(d):
    primes = [p for p in range(2, 200) if is_prime(p)]
    deep_a = primes[:d]
    deep_b = [2, 4] + primes[1:d - 1]
    deep_b = [3 * x if i >= 2 and i % 3 == 0 else x
              for i, x in enumerate(deep_b)]
    return deep_a, deep_b


def c1_pairs():
    print("C1 the supply pairs")
    for d in (8, 12):
        a, b = deep_pair(d)
        near = [7919, 10007, 10009, 12, 10037]
        ca, cb = lcm_list(a), lcm_list(b)
        print("  d=%d deep A %s  deep B %s  near %s" % (d, a, b, near))
        print("       C'_A %d  C'_B %d" % (ca, cb))
        ok(ca != cb and ca > 10 ** 6 and cb > 10 ** 6,
           "C1 d=%d deep moduli differ, near moduli shared" % d)


def c2_comparator():
    print("C2 the prime reader on a pair whose next modulus is 15")
    last = 2 ** 14
    a = [2, 7, 11, 13]
    b = [2, 3, 7, 11]
    ra = solve_trip(READER, supply_of(a + [last, 15]), len(a) + 1)
    rb = solve_trip(READER, supply_of(b + [last, 15]), len(b) + 1)
    print("  deep %s -> %s ; deep %s -> %s" % (a, ra, b, rb))
    ok(ra != rb, "C2 the comparator sees the deep read")


def c3_solver():
    print("C3 solver against the step engine at deep d = 3")
    rng = random.Random(41)
    agree = ended = 0
    for _ in range(200):
        prog = grow_free_program(rng)
        ms = [2, 3, 5, 7, 11, 13, 17, 19]
        m_of = supply_of(ms)
        sol = solve_trip(prog, m_of, 4)
        st = step_trip(prog, m_of, 4, 3000)
        if st[0] != "cap":
            ended += 1
            agree += sol == st
        else:
            agree += sol[0] == "never" or (sol[0] == "v" and sol[1] > 3000)
    print("  200 programs, %d ended within the cap, %d agree" % (ended,
                                                                 agree))
    ok(agree == 200 and ended > 0, "C3 the solver is the step engine")


def p1_p2_random():
    print("P1, P2 random programs on supply pairs")
    rng = random.Random(43)
    violations = differ = fast = 0
    least_ratio = None
    near = [7919, 10007, 10009, 12, 10037]
    for i in range(3000):
        d = 8 + i % 5
        deep_a, deep_b = deep_pair(d)
        ca, cb = lcm_list(deep_a), lcm_list(deep_b)
        prog = grow_free_program(rng)
        big_n, k = constants(prog)
        bound_a, bound_b = (ca - k) / big_n, (cb - k) / big_n
        sa = solve_trip(prog, supply_of(deep_a + near), d + 1)
        sb = solve_trip(prog, supply_of(deep_b + near), d + 1)
        pa, pb = pass_of(sa), pass_of(sb)
        lo = min(bound_a, bound_b)
        if (pa is not None and pa < lo) or (pb is not None and pb < lo):
            fast += 1
            if sa != sb:
                violations += 1
                print("  VIOLATION %s A %s B %s" % (prog, sa, sb))
        if sa != sb:
            differ += 1
            ratios = []
            if pa is not None:
                ratios.append(pa / bound_a)
            if pb is not None:
                ratios.append(pb / bound_b)
            r = max(ratios)
            least_ratio = r if least_ratio is None else min(least_ratio, r)
    print("  3000 pairs: %d with an exit below both bounds, violations %d"
          % (fast, violations))
    print("  pairs with differing exits %d, least pass/bound among them %s"
          % (differ, least_ratio))
    ok(violations == 0, "P1 a fast exit never reads the deep moduli")
    ok(differ > 0 and least_ratio >= 1, "P2 every deep read waits the lcm")


def p3_prime_reader():
    print("P3 the prime reader's price on planted supplies")
    primes = [p for p in range(2, 200) if is_prime(p)]
    fresh = [p for p in range(10007, 11000) if is_prime(p)]
    bad = 0
    for d in range(5, 13):
        deep = primes[:d]
        cp = lcm_list(deep)
        for nxt, new_prime in ((fresh[d], True), (3 * primes[d - 1], False)):
            sol = solve_trip(READER, supply_of(deep + [2 ** 14, nxt]), d + 1)
            second = sol[0] == "v" and sol[2] == R_SECOND
            price = sol[1] / cp if sol[0] == "v" else None
            print("  d=%d next %d: %s at pass/C' %.3f"
                  % (d, nxt, "second" if second else "first", price))
            bad += second != new_prime or price < 1
    ok(bad == 0, "P3 R reads the new prime at a pass >= C'")


def main():
    c1_pairs()
    c2_comparator()
    c3_solver()
    p1_p2_random()
    p3_prime_reader()
    print("%d checks" % CHECKS)


if __name__ == "__main__":
    main()
