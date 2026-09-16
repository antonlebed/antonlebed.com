"""
explore_prime_chain.py -- CHAINED TRIPS READ A WORD: in the one-AND clock
class (explore_one_and.py), a trip whose every exit leaves a true read one
grow later can be chained, so a program walks a word over the supply one
letter per trip. What word do the prime reader and an order reader walk
on m_g = g + 1, and what does that make of halting?

THE SETTING. The class and the exact trip solver of
explore_prime_reader.py: banks of windows over a supply m_g, ops TICK,
PULSE, GROW and one TEST reading every window of every bank at zero; a
true read leaves (control, grow count) and nothing else, and a trip runs
the lasso of its start state to the next true read.

THE QUESTIONS.
  Q1 THE CHAIN. Route every exit of the prime reader R back to its GROW
     through a finite automaton's transition on the exit letter. Is the
     program's run exactly that automaton run over the word w_g = [g + 2
     prime], so that the program halts iff the automaton accepts a prefix
     of the prime characteristic word?
  Q2 THE THREE-EXIT ORDER READER. Does one grow-free loop exit at every
     g, at a composite g + 2 by a third TEST and at a prime by the order
     bit, so that the bit is chainable where the order reader of
     explore_prime_reader.py hangs at every composite?
  Q3 THE BIT ON PRIME PATTERNS. Along twin primes, consecutive primes and
     the two prime-triplet shapes, does every assignment of the order bit
     occur, at counts a fair coin allows?

THE HAND ATTACK (before any engine code).
  (1) A CHAIN IS AN AUTOMATON OVER THE EXIT WORD. At a true read every
      window is 0, so a trip from control q at g grows is fixed by (q,
      g). Take a deterministic automaton A = (S, s0, delta, H) over the
      exit letters and give each state s outside H a copy of the reader,
      GROW first; a TEST reading true in copy s moves to the GROW of copy
      delta(s, letter). Copy s's trip at g reads the same letter as R's
      trip at g, since the ops are R's; so the control after t trips is
      delta*(s0, letter_0 .. letter_(t-1)), and the program reaches H iff
      A accepts a prefix. The solver is exact per trip because every
      trip starts from all-zero windows.
  (2) THE THREE-EXIT READER O3. u = GROW; v = TICK(B, +1), PULSE(B, -1),
      TEST_a, PULSE(B, -1), TEST_b, PULSE(B, +2), TEST_c. The pulses
      cancel over a pass, so at pass k the old windows hold k and the
      newest k - 1, k - 2, k at a, b, c; C = lcm(m_1..m_g), m = g + 2.
      TEST_c solves at k = lcm(C, m) always. At a prime p >= 3, a at C x
      and b at C (2x mod p), x = C^-1 mod p, both below C p, so the exit
      is a iff x < p/2: the bit of explore_prime_reader.py. At a
      composite m that is not a prime power, m | C and a, b are
      unsolvable: exit c at C. At m = p^e, e >= 2, v_p(C) = e - 1 puts p
      | k against k = 1 mod p^e (a unsolvable) and k = 2 mod p^e (b
      solvable only at p = 2, e = 2): exit c at p C except m = 4, exit b
      at pass 6. At g = 0 there is no old window: exit a at pass 1. So
      the O3 word is c at every composite but 4, and the bit at every
      prime but 2.
  (3) HALTING. By (1), halting for R-chains on m_g = g + 1 is the
      question whether a regular language holds a prefix of the prime
      characteristic word, a sentence of the monadic second-order theory
      of (N, <, P). That theory is decidable under Dickson's conjecture
      (the linear case of Schinzel's Hypothesis H), and its unconditional
      decidability is open (Bateman, Jockusch and Woods, J. Symbolic
      Logic 58 (1993), as restated in full text by Berthe, Karimov,
      Nieuwveld, Ouaknine, Vahanwala and Worrell, On the decidability of
      monadic theories of arithmetic predicates, arXiv 2405.07953, §1;
      the 1993 text itself was not opened). A named instance: the
      automaton whose state is the last 3159 letters, halting when they
      hold 447 ones with the window starting past the integer 2, exists
      (2^3159 states, a program constant), and its chain halts iff
      pi(x + 3159) - pi(x) > pi(3159) = 446 for some x >= 2, a failure
      of the second Hardy-Littlewood conjecture pi(x + y) <= pi(x) +
      pi(y) at y = 3159. Hensley and Richards (1973) showed the prime
      k-tuple conjecture refutes that conjecture; the 447-tuple of
      diameter below 3159 is the standard witness, with no counterexample
      known (arXiv 2503.02766, §1, which lists no proven range covering y
      = 3159 at every x). So that one program halts under Dickson's
      conjecture and its halting is otherwise open.
  (4) THE ORDER BIT HAS NO HYPOTHESIS OF ITS OWN. By (2), O3-chains read
      the word over {a, b, c}; halting for them is the monadic theory of
      (N, <, P, B), B the primes with bit 1. The route of (3) would need
      the bit's analogue of Dickson: every admissible prime pattern
      occurs with every bit assignment, infinitely often. No such
      hypothesis is in the literature this rig contacted; Q3 probes its
      first consequence, that no local bit assignment is forbidden.
      Residues mod p + 2 of lcm(1..p + 1) = lcm(1..p - 1) p (times 2 at
      p + 1 a power of 2) share no evident law with the residue mod p,
      so no local constraint is predicted. TRANSPLANT (marked): "the
      bit looks like a coin", imported from generic residues.

THE PREDICTIONS (frozen before the run).
  P1 The recorder chain (A remembering nothing, letter printed) from g =
     0 prints 201 letters equal to [n prime] for n = 2..202.
  P2 On 40 random automata of 2..6 states over {0, 1} with 1 or 2
     halting states, the program's run by the solver agrees with A run
     directly on the prime word: the same halting trip, or the same
     state after 201 trips.
  P3 The window automata at y = 2..8: threshold pi(y) + 1 on windows
     starting past 2 never halts through n = 202 (the second
     Hardy-Littlewood inequality holds there); threshold pi(y) halts
     exactly where the direct scan says, at least one y halting (a
     window of y letters needs an admissible pi(y)-tuple of diameter
     below y, which fails at some y, so no y is predicted to halt).
  P4 The O3 chain from g = 0 prints 201 letters matching (2): c at every
     composite n <= 202 but 4, b at 4, a at 2, and at every prime p <=
     202 but 2 the letter a iff (lcm(1..p - 1)^-1 mod p) < p/2.
  P5 Over primes p <= 30000 (bit by formula, the formula tied to the
     solver by P4 and by explore_prime_reader.py to 2000): every bit
     pair on twin primes and on consecutive primes, and every bit triple
     on (p, p + 2, p + 6) and (p, p + 4, p + 6), occurs, each count
     within 5 sd of the binomial mean for a fair independent coin.
THE KILLS, as prints: P1's line printing a letter that disagrees with
primality at any n <= 202 (the chain dies); P2's line printing a
disagreement count above 0; P5's line printing a pattern count of 0 with
expected count >= 10 (a local bit law, and the bit's Dickson analogue
dies).

THE CONTROLS (run before any prediction is read).
  C1 THE STEP ENGINE CHAIN. The recorder programs for R and O3, run op
     by op with no solver from g = 0 through 7 trips, print the same
     letters and passes as the solver chain.
  C2 THE CHAIN SEES ITS SUPPLY. The R recorder on the sqrt pole m_g =
     max(2, ceil(sqrt g)) prints [m_(g+1) > 1 and coprime to every
     earlier modulus] for g = 0..200, a word that differs from the
     primality word, so the P1 print is not the program's alone.
  C3 THE PATTERN COUNTER SEES A LAW. Fed [p = 1 mod 4] as the bit, the
     twin-prime pair (1, 1) prints count 0 (p and p + 2 are never both 1
     mod 4), and the P5 kill line fires on it.

RESOURCE ENVELOPE (named before the run): at most ~210 windows per bank,
integers of at most ~90 digits, at most ~2,500 solver trips and ~10^7
modular powers; under 50 MB and under a minute, run under memwatch.

ADDED AFTER THE FIRST RUN (marked; the first run's prints met P1-P5).
  P6 A SECOND ENGINE FOR THE BIT. Independent of the congruence solver:
     step one pass of O3's ops at a time, per window kind (old windows
     take the ticks, the newest the ticks and pulses), for passes 1..m,
     and read each window's zero set at each TEST position as the passes
     k <= m where its stepped integer is 0 mod m; combine every window's
     sets with sympy's solve_congruence (enumerating residues where a set
     holds several) and take the least (pass, position). At every prime
     3 <= p <= 2000 its exit letter is a iff the solver's O exits first
     (explore_prime_reader.py's P3 bits), and at every n <= 202 it
     prints P4's letter. KILL: any disagreement printed.
     Envelope: under 100 MB and 3 minutes.

AMENDED BEFORE THE FIRST RUN (marked): P3 first read "threshold pi(y)
halts"; the hand check at y = 8 (four primes in eight integers past 2
need an admissible 4-tuple of diameter 7, and none exists) refuted it
before any print, and P3 was rewritten as above.

PREDICTIONS ADJUDICATED (post-run). P1-P5 CONFIRMED; no kill fired;
C1-C3 passed before any prediction was read. P6 (second run) CONFIRMED,
its kill not fired.

FINDINGS (entered after the run; every number is printed output).

1. A CHAIN OF PRIME READERS IS A FINITE AUTOMATON OVER THE PRIME
   CHARACTERISTIC WORD (rule, argued in (1) for every g; checked by the
   exact solver through n = 202). The recorder chain prints [n prime]
   for n = 2..202, 46 ones and 0 disagreements; 40 random automata of 2
   to 6 states, 6 halting within 201 trips, run as programs exactly as
   they run directly on the word; the step engine prints the solver's
   letters and passes for 7 trips (passes 1, 2, 12, 24, 60, 300, 840).
   The same program on the sqrt pole prints its own word (ones at g = 0,
   4, 16, 36, 100, 144, 50 letters off the primality word). So halting
   for these chains is a sentence of the monadic theory of (N, <, P):
   decidable under Dickson's conjecture, unconditionally open, and by
   (3) one program's halting is the failure of the second
   Hardy-Littlewood conjecture at y = 3159 (argued; the window programs
   were rigged at y = 2..8, where threshold pi(y) halts at 5 of 7 y,
   exactly where the direct scan says, and threshold pi(y) + 1 halts at
   none through n = 202).

2. THE ORDER BIT IS CHAINABLE, AND SHOWS NO LOCAL LAW (rule for the
   reader, argued in (2) and checked through n = 202; observation for
   the statistics). O3 exits at every g: c at the 154 composites but 4,
   and a or b by lcm(1..p - 1)^-1 mod p < p/2 at every prime but 2, 0
   disagreements. Over the 3,244 primes from 3 to 30000 (bit 1 at
   1,637), every bit pair on the 467 twin pairs and the 3,243
   consecutive pairs, and every bit triple on the 114 triplets (p, p +
   2, p + 6) and the 111 triplets (p, p + 4, p + 6), occurs, the largest
   |z| against a fair independent coin 1.63. A second engine, stepping
   each window's ops pass by pass and combining the zero sets with
   sympy's solve_congruence, prints the same letters at every n <= 202
   and the solver's bit at all 302 primes from 3 to 2000 (147 ones, 0
   disagreements; P6). So the Dickson analogue for
   the bit survives its first local test, and no hypothesis naming it
   was found.

SCOPE + HONESTY. Finding 1's automaton reading covers chains whose every
trip is the prime reader's loop; a general one-AND program's trips also
read prime-power letters, g modulo program constants and lcm residues
(explore_prime_reader.py (4), argued), so the class's halting is claimed
only for these chains. The monadic decidability result is BJW 1993 as
restated in arXiv 2405.07953; the original was not read. The
Hardy-Littlewood instance is argued from the automaton's existence and
the cited 447-tuple, whose table this rig did not recompute; a
counterexample's absence is the literature's (arXiv 2503.02766). Finding
2's statistics are toy-scale: to 30000 they rule out a forbidden pattern
at those four shapes and nothing more.

RUN RECORD (python prime/code/memwatch.py
prime/code/explore_prime_chain.py; 2.0 s wall clock, 13.8 MB peak
working set, 11 checks). C1 R 1101010, O3 abbbcac, passes agree. C2
sqrt-pole ones at 0, 4, 16, 36, 100, 144. C3 twins under [p = 1 mod 4]:
00:0 01:229 10:238 11:0, kill fires. P1 46 ones, 0 off. P2 40 automata,
6 halting, 0 off. P3 halting at pi(y) for y = 2..6, not at 7, 8; none
above. P4 a 25, b 22, c 154, 0 off. P5 twins 119/115/127/106; triplet
(0,2,6) 20/14/13/13/13/14/13/14; triplet (0,4,6)
18/11/17/11/15/13/12/14; consecutive 793/813/813/824. Second run with
P6: 8.3 s wall clock, 72.2 MB peak working set, 12 checks; P6 n <= 202
0 off, 302 primes, 147 a, 0 off.
"""

import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_one_and import Offset, apply, linear, sqrt_pole
from explore_prime_reader import is_prime, lcm_to, solve_trip
from explore_prime_reader import ORDER as ORDER_READER
from explore_prime_reader import O_FIRST as O_FIRST_STATE

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1
    print("  [ok] " + msg)


# A reader is its ops after GROW, as (kind, bank, s); TESTs name letters.
R_LOOP = [("tick", 1, 1), ("test", "0"), ("pulse", 1, 1), ("test", "1"),
          ("pulse", 1, -1)]
O3_LOOP = [("tick", 1, 1), ("pulse", 1, -1), ("test", "a"),
           ("pulse", 1, -1), ("test", "b"), ("pulse", 1, 2), ("test", "c")]


def chain_program(loop, nstates, delta, halting):
    """One reader copy per automaton state; returns (prog, start, letter
    of each TEST state, halting program states). Copy s occupies states
    base(s) .. base(s) + len(loop); a halting copy is one sink TEST."""
    width = len(loop) + 1
    base = [s * width for s in range(nstates)]
    prog, letters, halt_states = [], {}, set()
    for s in range(nstates):
        if s in halting:
            q = len(prog)
            prog.append(("test", q, q))
            prog.extend([("test", q, q)] * (width - 1))
            halt_states.add(q)
            continue
        b = base[s]
        prog.append(("grow", b + 1))
        for i, op in enumerate(loop):
            nxt = b + 2 + i if i + 1 < len(loop) else b + 1
            if op[0] == "test":
                letters[b + 1 + i] = op[1]
                prog.append(("test", base[delta[s][op[1]]], nxt))
            else:
                prog.append((op[0], op[1], op[2], nxt))
    return prog, 0, letters, halt_states


def solver_chain(prog, start, letters, halt_states, m_of, trips):
    """Trip by trip with the exact solver. Returns (word, passes, final
    control, trips run)."""
    q, word, passes = start, [], []
    for g in range(trips):
        if q in halt_states:
            return word, passes, q, g
        sol = solve_trip(prog, m_of, g, q)
        assert sol is not None and sol[0] == "v", (g, q, sol)
        word.append(letters[sol[2]])
        passes.append(sol[1])
        q = prog[sol[2]][1]
    return word, passes, q, trips


def step_chain(prog, start, letters, m_of, trips, pass_cap=10 ** 6):
    """Op by op, no solver: letters and per-trip passes of v."""
    eng = Offset(m_of, 2)
    q, word, passes = start, [], []
    while len(word) < trips:
        assert prog[q][0] == "grow"
        eng.grow()
        q = prog[q][1]
        loop_head, k = q, 1
        while True:
            op = prog[q]
            if op[0] == "test":
                if eng.test():
                    word.append(letters[q])
                    passes.append(k)
                    q = op[1]
                    break
                q = op[2]
            else:
                apply(eng, op)
                q = op[-1]
            if q == loop_head:
                k += 1
                assert k <= pass_cap
    return word, passes


def recorder(loop, alphabet):
    return chain_program(loop, 1, [{a: 0 for a in alphabet}], set())


def c1_step_chain():
    print("C1 the step engine chain against the solver chain, 7 trips")
    for name, loop, alph in (("R", R_LOOP, "01"), ("O3", O3_LOOP, "abc")):
        prog, st, lt, hs = recorder(loop, alph)
        sw, sp = step_chain(prog, st, lt, linear, 7)
        vw, vp, _, _ = solver_chain(prog, st, lt, hs, linear, 7)
        print("  %s step %s %s  solver %s %s" % (name, "".join(sw), sp,
                                                  "".join(vw), vp))
        ok(sw == vw and sp == vp, "C1 %s chains agree" % name)


def c2_supply():
    print("C2 the R recorder on the sqrt pole, g = 0..200")
    prog, st, lt, hs = recorder(R_LOOP, "01")
    word, _, _, _ = solver_chain(prog, st, lt, hs, sqrt_pole, 201)
    expect, lin = [], []
    for g in range(201):
        m = sqrt_pole(g + 1)
        c = 1
        for j in range(1, g + 1):
            c = c * sqrt_pole(j) // math.gcd(c, sqrt_pole(j))
        expect.append("1" if m > 1 and math.gcd(c, m) == 1 else "0")
        lin.append("1" if is_prime(g + 2) else "0")
    ones = [g for g in range(201) if word[g] == "1"]
    print("  ones at g = %s; differs from the primality word at %d g"
          % (ones, sum(a != b for a, b in zip(word, lin))))
    ok(word == expect and word != lin, "C2 the sqrt-pole word is its own")


def pattern_counts(primes, bit, shape):
    pset = set(primes)
    counts = {}
    n = 0
    for p in primes:
        pts = [p + h for h in shape]
        if all(x in pset for x in pts):
            key = tuple(int(bit[x]) for x in pts)
            counts[key] = counts.get(key, 0) + 1
            n += 1
    return n, counts


def consecutive_counts(primes, bit):
    counts = {}
    for p, q in zip(primes, primes[1:]):
        key = (int(bit[p]), int(bit[q]))
        counts[key] = counts.get(key, 0) + 1
    return len(primes) - 1, counts


def kill_lines(n, counts, width, label):
    """Prints each assignment's count against n / 2^width; returns the
    assignments printing count 0 at expected >= 10, and the largest
    |z|."""
    exp = n / 2 ** width
    sd = math.sqrt(n * (1 / 2 ** width) * (1 - 1 / 2 ** width)) if n else 0
    zero_kills, zmax = [], 0.0
    cells = []
    for i in range(2 ** width):
        key = tuple((i >> (width - 1 - j)) & 1 for j in range(width))
        c = counts.get(key, 0)
        z = (c - exp) / sd if sd else 0.0
        zmax = max(zmax, abs(z))
        cells.append("%s:%d" % ("".join(map(str, key)), c))
        if c == 0 and exp >= 10:
            zero_kills.append(key)
    print("  %s n=%d expected %.1f  %s  max|z| %.2f%s"
          % (label, n, exp, " ".join(cells), zmax,
             "  KILL zero at %s" % zero_kills if zero_kills else ""))
    return zero_kills, zmax


def c3_counter():
    print("C3 the pattern counter on [p = 1 mod 4]")
    primes = [p for p in range(3, 30001) if is_prime(p)]
    bit = {p: p % 4 == 1 for p in primes}
    n, counts = pattern_counts(primes, bit, (0, 2))
    kills, _ = kill_lines(n, counts, 2, "twins mod-4 bit")
    ok((1, 1) not in counts and kills, "C3 the counter fires on a law")


def p1_recorder():
    print("P1 the R recorder chain on m_g = g + 1, n = 2..202")
    prog, st, lt, hs = recorder(R_LOOP, "01")
    word, passes, _, _ = solver_chain(prog, st, lt, hs, linear, 201)
    bad = [g + 2 for g in range(201)
           if (word[g] == "1") != is_prime(g + 2)]
    print("  word %s" % "".join(word))
    print("  ones %d; letters disagreeing with primality: %d%s"
          % (word.count("1"), len(bad), "  KILL at n = %s" % bad if bad
             else ""))
    ok(not bad, "P1 the chain walks the prime characteristic word")
    return word


def run_dfa(nstates, delta, halting, word):
    s = 0
    for t, a in enumerate(word):
        if s in halting:
            return "halt", t, s
        s = delta[s][a]
    return ("halt", len(word), s) if s in halting else ("run", len(word), s)


def program_verdict(prog, st, lt, hs, width, trips):
    word, _, q, t = solver_chain(prog, st, lt, hs, linear, trips)
    if q in hs:
        return "halt", t, q // width
    return "run", t, q // width


def p2_random_automata(pword):
    print("P2 random automata over {0, 1}, 201 trips")
    rng = random.Random(31)
    width = len(R_LOOP) + 1
    bad = halts = 0
    for _ in range(40):
        ns = rng.randrange(2, 7)
        halting = set(rng.sample(range(1, ns), rng.randrange(1, min(2, ns - 1)
                                                              + 1)))
        # make halting rare: route into a halting state from one cell only
        delta = []
        for s in range(ns):
            row = {}
            for a in "01":
                t = rng.randrange(ns)
                while t in halting and rng.random() < 0.9:
                    t = rng.randrange(ns)
                row[a] = t
            delta.append(row)
        prog, st, lt, hs = chain_program(R_LOOP, ns, delta, halting)
        pv = program_verdict(prog, st, lt, hs, width, 201)
        dv = run_dfa(ns, delta, halting, pword)
        halts += pv[0] == "halt"
        if pv != dv:
            bad += 1
            print("  disagree %s %s" % (pv, dv))
    print("  40 automata, %d halting within 201 trips; disagreements %d"
          % (halts, bad))
    ok(bad == 0, "P2 each program runs its automaton over the prime word")


def window_automaton(y, thr):
    """State 0 skips the letter at n = 2; state 1 + code holds the last
    up-to-y letters as (length, bits); one halting state. Built by
    exploring reachable states."""
    index = {("skip",): 0}
    states = [("skip",)]
    delta = []
    halting = set()
    i = 0
    while i < len(states):
        st = states[i]
        row = {}
        if st == ("halt",):
            halting.add(i)
            delta.append({"0": i, "1": i})
            i += 1
            continue
        for a in "01":
            if st == ("skip",):
                nxt = ((),)
            else:
                win = (st[0] + (int(a),))[-y:]
                nxt = ("halt",) if len(win) == y and sum(win) >= thr \
                    else (win,)
            if nxt not in index:
                index[nxt] = len(states)
                states.append(nxt)
            row[a] = index[nxt]
        delta.append(row)
        i += 1
    return len(states), delta, halting


def pi(n):
    return sum(1 for j in range(2, n + 1) if is_prime(j))


def p3_windows(pword):
    print("P3 window automata: y letters past n = 2 holding >= threshold")
    width = len(R_LOOP) + 1
    bad = at_pi = 0
    for y in range(2, 9):
        for thr in (pi(y), pi(y) + 1):
            ns, delta, halting = window_automaton(y, thr)
            prog, st, lt, hs = chain_program(R_LOOP, ns, delta, halting)
            pv = program_verdict(prog, st, lt, hs, width, 201)
            dv = run_dfa(ns, delta, halting, pword)
            bad += pv[:2] != dv[:2]
            print("  y=%d thr=%d states=%d program %s at trip %d, direct %s"
                  " at %d" % (y, thr, ns, pv[0], pv[1], dv[0], dv[1]))
            if thr == pi(y) + 1:
                bad += pv[0] != "run"
            else:
                at_pi += pv[0] == "halt"
    print("  thresholds pi(y) halting: %d of 7; mismatches %d" % (at_pi, bad))
    ok(bad == 0 and at_pi > 0,
       "P3 the window programs run their automata, never above pi(y)")


def order_bit(p, c):
    x = pow(c, -1, p)
    return x < p / 2


def p4_o3(trips=201):
    print("P4 the O3 recorder chain on m_g = g + 1, n = 2..202")
    prog, st, lt, hs = recorder(O3_LOOP, "abc")
    word, passes, _, _ = solver_chain(prog, st, lt, hs, linear, trips)
    bad = []
    for g in range(trips):
        n = g + 2
        if n == 2:
            want = "a"
        elif n == 4:
            want = "b"
        elif not is_prime(n):
            want = "c"
        else:
            want = "a" if order_bit(n, lcm_to(n - 1)) else "b"
        if word[g] != want:
            bad.append(n)
    print("  word %s" % "".join(word))
    print("  a %d  b %d  c %d; disagreements with (2): %s"
          % (word.count("a"), word.count("b"), word.count("c"), bad))
    ok(not bad, "P4 O3 exits at every g, the bit at primes, c at composites")


def bits_to(n):
    primes = [p for p in range(2, n + 1) if is_prime(p)]
    bit = {}
    for p in primes[1:]:
        c = 1
        for q in primes:
            if q >= p:
                break
            e = 1
            while q ** (e + 1) <= p - 1:
                e += 1
            c = c * pow(q, e, p) % p
        bit[p] = order_bit(p, c)
    return primes[1:], bit


def p5_patterns():
    print("P5 the order bit on prime patterns, primes 3..30000")
    primes, bit = bits_to(30000)
    small = [p for p in primes if p <= 2000]
    agree = all(bit[p] == order_bit(p, lcm_to(p - 1)) for p in small)
    print("  %d primes, %d ones; fast formula matches the lcm at all %d"
          " primes <= 2000: %s" % (len(primes), sum(bit.values()),
                                   len(small), agree))
    kills, zs = [], []
    for label, shape in (("twins (0,2)", (0, 2)),
                         ("triplet (0,2,6)", (0, 2, 6)),
                         ("triplet (0,4,6)", (0, 4, 6))):
        n, counts = pattern_counts(primes, bit, shape)
        k, z = kill_lines(n, counts, len(shape), label)
        kills += k
        zs.append(z)
    n, counts = consecutive_counts(primes, bit)
    k, z = kill_lines(n, counts, 2, "consecutive")
    kills += k
    zs.append(z)
    ok(agree, "P5 the fast bit is the lcm's bit to 2000")
    ok(not kills, "P5 no bit assignment forbidden on the four patterns")
    ok(max(zs) < 5, "P5 every count within 5 sd of a fair coin")


def zero_sets(loop, m_old_list, m_new):
    """Per TEST position: the zero set of every window, by stepping the
    loop's ops pass by pass on two integers (old kind, newest kind)."""
    os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
    import numpy as np
    top = max([m_new] + list(m_old_list))
    positions = [i for i, op in enumerate(loop) if op[0] == "test"]
    old_vals = {i: [] for i in positions}
    new_vals = {i: [] for i in positions}
    x_old = x_new = 0
    for _ in range(top):
        for i, op in enumerate(loop):
            if op[0] == "tick":
                x_old += op[2]
                x_new += op[2]
            elif op[0] == "pulse":
                x_new += op[2]
            else:
                old_vals[i].append(x_old)
                new_vals[i].append(x_new)
    out = {}
    for i in positions:
        ov = np.array(old_vals[i], dtype=np.int64)
        nv = np.array(new_vals[i], dtype=np.int64)
        sets = []
        for m in m_old_list:
            ks = np.nonzero(ov[:m] % m == 0)[0] + 1
            sets.append((m, [int(k) % m for k in ks]))
        ks = np.nonzero(nv[:m_new] % m_new == 0)[0] + 1
        sets.append((m_new, [int(k) % m_new for k in ks]))
        out[i] = sets
    return out


def second_engine_exit(loop, g):
    """O3's trip at g on m_g = g + 1 by the stepped zero sets and sympy."""
    from sympy.ntheory.modular import solve_congruence
    m_old = list(range(2, g + 2))
    sets = zero_sets(loop, m_old, g + 2)
    best = None
    for i, windows in sets.items():
        if any(not zs for _, zs in windows):
            continue
        singles = [(zs[0], m) for m, zs in windows if len(zs) == 1]
        multis = [(m, zs) for m, zs in windows if len(zs) > 1]
        combos = [[]]
        for m, zs in multis:
            combos = [c + [(r, m)] for c in combos for r in zs]
        for extra in combos:
            sol = solve_congruence(*(singles + extra)) if singles + extra                 else (0, 1)
            if sol is None:
                continue
            r, l = int(sol[0]), int(sol[1])
            k = r if r > 0 else l
            if best is None or (k, i) < best[:2]:
                best = (k, i, loop[i][1])
    return best


def p6_second_engine():
    print("P6 the second engine: stepped zero sets and sympy's CRT")
    bad = []
    for g in range(0, 201):
        k, _, letter = second_engine_exit(O3_LOOP, g)
        n = g + 2
        want = ("a" if n == 2 else "b" if n == 4 else "c"
                if not is_prime(n) else
                "a" if order_bit(n, lcm_to(n - 1)) else "b")
        if letter != want:
            bad.append(n)
    print("  n = 2..202: disagreements with P4's letters %s" % bad)
    primes = [p for p in range(3, 2001) if is_prime(p)]
    off = 0
    ones = 0
    for p in primes:
        sol = solve_trip(ORDER_READER, linear, p - 2)
        solver_bit = sol[2] == O_FIRST_STATE
        _, _, letter = second_engine_exit(O3_LOOP, p - 2)
        ones += letter == "a"
        off += (letter == "a") != solver_bit
    print("  primes 3..2000: %d, letter a at %d; disagreements with the"
          " solver's order reader %d" % (len(primes), ones, off))
    ok(not bad and off == 0, "P6 the second engine prints the bit")


def main():
    c1_step_chain()
    c2_supply()
    c3_counter()
    pword = p1_recorder()
    p2_random_automata(pword)
    p3_windows(pword)
    p4_o3()
    p5_patterns()
    p6_second_engine()
    print("%d checks" % CHECKS)


if __name__ == "__main__":
    main()
