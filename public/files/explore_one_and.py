"""
explore_one_and.py -- ONE AND OVER EVERY BANK: when the clock machine's
only read is the coincidence of every clock in every bank, what does a
program carry from one true read to the next? (Sibling of
explore_clock_counter.py, whose per-bank AND it replaces by one global
AND.)

THE SETTING. The clock machine of explore_clock_counter.py on a supply
m_g: banks of windows, ops
  TICK(b, s)   add s = +1 or -1 at every window of bank b,
  PULSE(b, s)  add s at the newest window of bank b only,
  GROW         start a window at phase 0 in every bank,
  TEST         every window of EVERY bank is zero (vacuously true
               before any grow),
with deterministic finite control Q, a TEST state branching on the
answer. With one AND per bank that class runs a Minsky machine on every
unbounded supply; here the per-bank read is removed.

THE QUESTION. Does a program in the one-AND class carry anything but
its control state and the grow count across a true read, and how far
can one trip -- the run from a true read to the next -- move the grow
count?

THE HAND ATTACK (before any engine code).
  (1) THE READ FORGETS. At a true TEST every window of every bank is 0,
      so the configuration is (q, g): control state and grow count.
  (2) THE TRIP IS A LASSO. From a true read in state q, every TEST
      until the next true one answers false, so the control path is the
      walk along false edges from q, a word u v v v ... with |u| + |v|
      <= |Q|, fixed by q alone. The trip ends at the first TEST on that
      word reading true, or never. Its ops are fixed; g enters only
      through the moduli the tests are read against.
  (3) A GROWING LOOP ENDS BY ITS FOURTH PASS OR NEVER. Let v hold a GROW
      and a TEST, and let every window grown during the loop have
      modulus > 4|v|. Count passes of v from 1. Fix a bank b and a TEST
      position T in v; n_b is the net TICK on b over one pass. A window
      born at grow position G in pass i holds, at T in pass k, the
      integer (ticks on b from its birth to T) + (pulses on b while it
      was newest); the pulses fall in one stretch of at most |v| ops,
      ending at the next GROW, so for i <= k - 2 the stretch is done and
      the integer is c_G + (k - i) n_b, linear in k - i. (a) If the TEST
      at T reads true in a pass k >= 4, take the windows born at one
      grow position in passes k - 3 and k - 2: their integers differ by
      exactly n_b and each is at most 4|v| in size, below its modulus,
      so both are 0 and n_b = 0; so every bank has n_b = 0. (b) With
      every n_b = 0, the windows born before the loop hold constants
      from pass 2 on (ticks cancel per pass, pulses hit only the newest
      window, and a loop window is newer); windows born in passes <= k -
      2 at position G all hold the integer c_G; windows born in passes
      k - 1 and k hold integers fixed by their position in v; every
      loop window's integer is below its modulus, so it reads 0 iff the
      integer is 0. So the answer at T is the same in every pass k >=
      3. By (a) and (b), a true read at T in some pass k >= 5 forces the
      same read true in pass 4: the first true read falls in a pass <=
      4, or in u, or never.
  (4) SO A TRIP GROWS BOUNDEDLY ONCE THE MODULI PASS 4|Q|. On a supply
      whose moduli tend to infinity, past the grow count g_0 after which
      every modulus exceeds 4|Q|, a trip that ends grows at most |u| +
      4 * (grows in v) <= 4|Q| times; a trip whose v has no GROW grows
      at most |u| times. By (1)-(4) the program's whole memory across
      true reads is its control state and a grow count it advances a
      bounded step per trip and can never lower: what a run does is a
      finite automaton walking the supply's arithmetic one way. Whether
      a halting question in the class is decidable then rides on that
      arithmetic; that is not claimed here.
  TRANSPLANT (marked): "a window's value is an integer below its
  modulus" is the (3) bound read off the op count; on a supply with a
  small modulus inside the loop it fails, and the arm below prints
  what that costs.

THE PREDICTIONS (frozen before the run).
  P1 Over random programs (2 banks, |Q| = 2..6) run one trip each from
     the all-zero configuration at g_start, on the linear supply m_g =
     g + 1 with g_start = 4|Q| and on the sqrt pole m_g = max(2,
     ceil(sqrt g)) with g_start = (4|Q|)^2 (|Q| = 2..4), every trip
     whose loop v holds a GROW and a TEST and ends does so in u or in a
     pass <= 4, the pass cap 12.
  P2 Every ending trip grows at most |u| + 4 * (grows in v) times.
  P3 The walk observed along false reads is the static lasso u v v ...
     of (2) at every step.
THE KILL, as a print: any ending trip printed at a pass >= 5 under P1's
hypothesis, or a grow count over P2's bound.
THE ARM (the hypothesis m > 4|v| removed; it must show a long trip, or
(3)'s bound cannot be credited to it). A1: on the supply m_1 = 1001,
m_g = 2 for 2 <= g <= 2000, m_g = g beyond, from one window grown, the
program u = TICK(A, +1), v = GROW, PULSE(A, -2), TICK(A, +2), TEST ends
its trip in pass 500 with 500 grows (window 1 holds 1 + 2k, zero first
at k = 500; loop windows hold 2(k - i), zero mod 2). A2: the same
program with every loop modulus g + 16 never ends within 600 passes (a
window born in pass k - 1 holds 2 at pass k).
ADDED AFTER THE FIRST RUN (marked; the first run's prints ended no
trip past pass 2 in 44,000 programs, and re-reading (3)(b) at k = 3
sharpens it). With every n_b = 0 the conditions at pass 3 contain those
at pass 2 read as integers (the windows born in passes 2 and 3 carry at
pass 3 the positional integers those born in passes 1 and 2 carried at
pass 2, the pass-1 window adds its c_G, and the old windows are constant
from pass 2), and the answer at pass 3 equals the answer at pass 4; a
true read in pass 4 forces every n_b = 0 by (a). So a first true read
in pass 4 or later is impossible, and the bound is pass 3.
  P4 No trip in P1 or P1b ends in a pass >= 4.
  P5 The bound is attained: with g_start windows grown on the linear
     supply, u = TICK(A, -3), v = TICK(A, +1), PULSE(A, +1), TEST,
     PULSE(A, -1), GROW, PULSE(A, -2) ends in pass 3 (the bulk holds k -
     3; the newest old window k - 3 + 1 - 1; a window born in pass k - 1
     holds -2 + 1 + 1 = 0 at pass k, one born earlier -2 + 1 - 1 + (k -
     i), zero at k - i = 2 only, and it exists first at pass 3).
  P1b A lasso-shaped population (u of 0..3 ops, v of 2..7 holding a GROW
     and a TEST, ops of size 1 or 2, g_start 8(|u| + |v|), squared on
     the sqrt pole) ends no trip past pass 3.
THE CONTROLS (run before any prediction is read).
  C1 BISIMULATION. A dense engine (every window a residue, rewritten by
     every op) and the offset engine agree on the global TEST at every
     TEST op of 200 random programs over 300 ops each, on the sqrt pole
     from zero windows.
  C2 THE RIG CAN SEE A LONG TRIP: A1 must print pass 500.

RESOURCE ENVELOPE (named before the run): at most ~1000 windows, two
banks, a few thousand programs of at most 12 passes; under 50 MB and
under two minutes, run under memwatch.

PREDICTIONS ADJUDICATED (post-run). P1-P5 and P1b CONFIRMED; the kill
did not fire; C1 and C2 passed before any prediction was read. The hand
attack's pass-4 bound was loose by one; P4 and P5 are the correction.

FINDINGS (entered after the run; every number is printed output).

1. ONE GLOBAL AND LEAVES A PROGRAM ONLY ITS CONTROL STATE AND ITS GROW
   COUNT, AND A TRIP MOVES THE COUNT A BOUNDED STEP (rule, argued in
   (1)-(4) with the pass-3 sharpening; checked). No trip whose loop
   holds a GROW and a TEST ended past pass 3: 1,176 such ends among
   21,500 random programs on the linear supply and the sqrt pole
   (every end in u, pass 1 or pass 2), every walk the static lasso and
   every grow count within |u| + 4 grows(v); and 8,727 ends among 41,500
   lasso-shaped programs (8,704 in pass 1, 23 in pass 2), every walk the
   static lasso (the grow bound not checked on that population).

2. THE BOUND IS PASS 3, ATTAINED (P5). The hand-built witness ends its
   trip in pass 3 with 2 grows at g_start 8, 32 and 64. Its v is 7 unit
   ops (the pulse of 2 counted twice), so the hypothesis (loop moduli >
   28) holds at 32 and 64 and not at 8, where the end is outside the
   lemma's scope.
   Random search never reached pass 3, so the witness, not the sweep, is
   the tightness evidence; a second reader's search at loop moduli
   4|v| + 1 reached pass 3 and never pass 4.

3. THE MODULUS HYPOTHESIS IS LOAD-BEARING (A1, A2). With the loop's
   moduli 2 the four-op loop ends in pass 500 after 500 grows; with the
   same loop at moduli g + 16 it has not ended after 600 passes.

The dense and offset engines agreed on 14,547 global TESTs (C1).

SCOPE + HONESTY. The argument covers every program and every supply
whose moduli exceed 4|v| inside the loop, so on a supply tending to
infinity it holds past a program constant; the sweeps are two banks and
at most 11 control states. What it removes is memory: a run is a finite
automaton reading the supply's arithmetic one way, since each trip's
ops are fixed by its start state and its exit is read off moduli that g
names. Whether halting in the class is decidable on a given supply rides
on that arithmetic and is not claimed. The per-bank AND class
(explore_clock_counter.py) is universal with three banks, so the whole
gap between the two classes is whether a bank can be read while another
holds a value.

RUN RECORD (python prime/code/memwatch.py prime/code/explore_one_and.py;
2.8 s wall clock, 13.2 MB peak working set, 32 checks). C1 14547 TEST
ops agree. A1 ended pass 500, 500 grows; A2 not ended at pass 601, 600
grows. P5 pass 3, 2 grows, at g_start 8, 32, 64. Linear |Q| 2..6
growing-loop ends 138, 192, 234, 229, 315, max pass 2, max grows 4;
sqrt |Q| 2..4 ends 11, 19, 38, max pass 1, max grows 2. P1b linear
{1: 8380, 2: 22}, 31598 capped; sqrt {1: 324, 2: 1}, 1175 capped.
"""

import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

CHECKS = 0
PASS_CAP = 12


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1
    print("  [ok] " + msg)


def ceil_sqrt(g):
    r = math.isqrt(g)
    return r if r * r == g else r + 1


def sqrt_pole(g):
    return max(2, ceil_sqrt(g))


def linear(g):
    return g + 1


class Offset:
    """A bank stored as a tick total t and, per window, the tick total at
    birth less the pulses it took: window w holds (t - base[w]) mod m_w."""

    def __init__(self, m_of, nbanks):
        self.m_of = m_of
        self.moduli = []
        self.t = [0] * nbanks
        self.base = [[] for _ in range(nbanks)]

    def grow(self):
        self.moduli.append(self.m_of(len(self.moduli) + 1))
        for b in range(len(self.t)):
            self.base[b].append(self.t[b])

    def tick(self, b, s):
        self.t[b] += s

    def pulse(self, b, s):
        if self.moduli:
            self.base[b][-1] -= s

    def test(self):
        for b, t in enumerate(self.t):
            for x, m in zip(self.base[b], self.moduli):
                if (t - x) % m:
                    return False
        return True


class Dense:
    """The reference: every window a residue, rewritten by every op."""

    def __init__(self, m_of, nbanks):
        self.m_of = m_of
        self.moduli = []
        self.regs = [[] for _ in range(nbanks)]

    def grow(self):
        self.moduli.append(self.m_of(len(self.moduli) + 1))
        for r in self.regs:
            r.append(0)

    def tick(self, b, s):
        r = self.regs[b]
        for i, m in enumerate(self.moduli):
            r[i] = (r[i] + s) % m

    def pulse(self, b, s):
        if self.moduli:
            r = self.regs[b]
            r[-1] = (r[-1] + s) % self.moduli[-1]

    def test(self):
        return all(x == 0 for r in self.regs for x in r)


def random_program(rng, nq, nbanks=2):
    """State i: ('tick'|'pulse', b, s, nxt), ('grow', nxt) or
    ('test', nxt_true, nxt_false)."""
    prog = []
    for _ in range(nq):
        kind = rng.choice(("tick", "pulse", "grow", "test"))
        if kind in ("tick", "pulse"):
            prog.append((kind, rng.randrange(nbanks), rng.choice((1, -1)),
                         rng.randrange(nq)))
        elif kind == "grow":
            prog.append(("grow", rng.randrange(nq)))
        else:
            prog.append(("test", rng.randrange(nq), rng.randrange(nq)))
    return prog


def false_successor(op):
    return op[2] if op[0] == "test" else op[-1]


def lasso(prog, q):
    """The walk along false edges from q: (u, v) as lists of states."""
    seen, path = {}, []
    while q not in seen:
        seen[q] = len(path)
        path.append(q)
        q = false_successor(prog[q])
    i = seen[q]
    return path[:i], path[i:]


def apply(eng, op):
    if op[0] == "tick":
        eng.tick(op[1], op[2])
    elif op[0] == "pulse":
        eng.pulse(op[1], op[2])
    elif op[0] == "grow":
        eng.grow()


def trip(prog, m_of, g_start, q=0, nbanks=2, pass_cap=PASS_CAP):
    """One trip from the all-zero configuration with g_start windows.
    Returns (ended, pass, grows, lasso_ok): pass 0 means the true read
    fell in u."""
    eng = Offset(m_of, nbanks)
    for _ in range(g_start):
        eng.grow()
    u, v = lasso(prog, q)
    word = u + v
    grows, step, lasso_ok = 0, 0, True
    while True:
        k = 0 if step < len(u) else 1 + (step - len(u)) // len(v)
        if k > pass_cap:
            return False, k, grows, lasso_ok
        want = word[step] if step < len(u) else v[(step - len(u)) % len(v)]
        if want != q:
            lasso_ok = False
        op = prog[q]
        if op[0] == "test":
            if eng.test():
                return True, k, grows, lasso_ok
            q = op[2]
        else:
            if op[0] == "grow":
                grows += 1
            apply(eng, op)
            q = op[-1]
        step += 1


def c1_bisimulation():
    print("C1 dense and offset engines, global TEST")
    rng = random.Random(11)
    tests = 0
    for _ in range(200):
        prog = random_program(rng, rng.randrange(2, 9))
        a, d = Offset(sqrt_pole, 2), Dense(sqrt_pole, 2)
        q = 0
        for _ in range(300):
            op = prog[q]
            if op[0] == "test":
                ta, td = a.test(), d.test()
                assert ta == td, (prog, ta, td)
                tests += 1
                q = op[1] if ta else op[2]
            else:
                apply(a, op)
                apply(d, op)
                q = op[-1]
    ok(tests > 0, "C1 %d TEST ops agree" % tests)


def arm_supply(loop_mod):
    def m_of(g):
        if g == 1:
            return 1001
        return loop_mod(g)
    return m_of


ARM_PROG = [
    ("tick", 0, 1, 1),     # u: TICK(A, +1)
    ("grow", 2),           # v: GROW
    ("pulse", 0, -2, 3),   #    PULSE(A, -2)
    ("tick", 0, 2, 4),     #    TICK(A, +2)
    ("test", 5, 1),        #    TEST, false back to GROW
    ("test", 5, 5),        # halt sink
]


def arms():
    print("C2 / A1 small loop moduli; A2 large loop moduli")
    ended, k, grows, _ = trip(
        ARM_PROG, arm_supply(lambda g: 2 if g <= 2000 else g), 1,
        pass_cap=600)
    print("  A1 ended=%s pass=%d grows=%d" % (ended, k, grows))
    ok(ended and k == 500 and grows == 500, "C2/A1 ends in pass 500")
    ended, k, grows, _ = trip(
        ARM_PROG, arm_supply(lambda g: g + 16), 1, pass_cap=600)
    print("  A2 ended=%s pass=%d grows=%d" % (ended, k, grows))
    ok(not ended, "A2 no end within 600 passes")


def sweep(name, m_of, g_start_of, sizes, per_size, seed):
    print("P1-P3 on the %s supply" % name)
    rng = random.Random(seed)
    for nq in sizes:
        g0 = g_start_of(nq)
        hist, late, over, bad_lasso = {}, 0, 0, 0
        growing, capped, max_grows = 0, 0, 0
        for _ in range(per_size):
            prog = random_program(rng, nq)
            u, v = lasso(prog, 0)
            kinds = [prog[s][0] for s in v]
            gv = kinds.count("grow")
            ended, k, grows, lok = trip(prog, m_of, g0)
            bad_lasso += not lok
            if not ended:
                capped += 1
                continue
            if grows > len(u) + 4 * gv:
                over += 1
            max_grows = max(max_grows, grows)
            if gv and "test" in kinds:
                growing += 1
                hist[k] = hist.get(k, 0) + 1
                if k >= 4:
                    late += 1
        print("  |Q|=%d g_start=%d growing-loop ends=%d by pass %s; "
              "pass>=4: %d; over bound: %d; capped: %d; max grows: %d; "
              "lasso breaks: %d" % (nq, g0, growing,
                                    dict(sorted(hist.items())), late, over,
                                    capped, max_grows, bad_lasso))
        ok(late == 0, "P1/P4 %s |Q|=%d no growing loop ends past pass 3"
           % (name, nq))
        ok(over == 0, "P2 %s |Q|=%d grows within |u| + 4 grows(v)"
           % (name, nq))
        ok(bad_lasso == 0, "P3 %s |Q|=%d walk is the lasso" % (name, nq))


def loop_program(rng, nbanks=2):
    """A lasso built directly: u of 0..3 ops, v of 2..7 ops holding at
    least one GROW and one TEST, every true edge to a sink."""
    nu, nv = rng.randrange(4), rng.randrange(2, 8)
    n = nu + nv
    sink = n
    while True:
        kinds = [rng.choice(("tick", "tick", "pulse", "grow", "test"))
                 for _ in range(nv)]
        if "grow" in kinds and "test" in kinds:
            break
    kinds = [rng.choice(("tick", "pulse", "grow")) for _ in range(nu)] + kinds
    prog = []
    for i, kind in enumerate(kinds):
        nxt = i + 1 if i + 1 < n else nu
        if kind in ("tick", "pulse"):
            prog.append((kind, rng.randrange(nbanks),
                         rng.choice((1, -1, 2, -2)), nxt))
        elif kind == "grow":
            prog.append(("grow", nxt))
        else:
            prog.append(("test", sink, nxt))
    prog.append(("test", sink, sink))
    return prog, nu, nv


def loop_sweep(name, m_of, per_size, seed):
    """P1b: the lasso population. g_start is 4(|u| + |v|) on the linear
    supply, so every loop modulus exceeds 4|v|; steps of 2 are ops of
    size 2, so the bound read is 8|v|, and g_start doubles."""
    print("P1b loop-shaped programs on the %s supply" % name)
    rng = random.Random(seed)
    hist, late, capped = {}, 0, 0
    for _ in range(per_size):
        prog, nu, nv = loop_program(rng)
        g0 = 8 * (nu + nv) if name == "linear" else (8 * (nu + nv)) ** 2
        ended, k, grows, lok = trip(prog, m_of, g0)
        assert lok
        if not ended:
            capped += 1
            continue
        hist[k] = hist.get(k, 0) + 1
        late += k >= 4
    print("  ends by pass %s; pass>=4: %d; capped: %d"
          % (dict(sorted(hist.items())), late, capped))
    ok(late == 0, "P1b/P4 %s no loop-shaped trip ends past pass 3" % name)


WITNESS = [
    ("tick", 0, -3, 1),    # u: TICK(A, -3)
    ("tick", 0, 1, 2),     # v: TICK(A, +1)
    ("pulse", 0, 1, 3),    #    PULSE(A, +1)
    ("test", 7, 4),        #    TEST
    ("pulse", 0, -1, 5),   #    PULSE(A, -1)
    ("grow", 6),           #    GROW
    ("pulse", 0, -2, 1),   #    PULSE(A, -2), back to TICK
    ("test", 7, 7),        # sink
]


def p5_witness():
    print("P5 the pass-3 witness")
    for g0 in (8, 32, 64):
        ended, k, grows, lok = trip(WITNESS, linear, g0)
        print("  g_start=%d ended=%s pass=%d grows=%d" % (g0, ended, k, grows))
        ok(ended and k == 3 and lok, "P5 g_start=%d ends in pass 3" % g0)


def main():
    c1_bisimulation()
    arms()
    p5_witness()
    sweep("linear", linear, lambda nq: 4 * nq, range(2, 7), 4000, 5)
    sweep("sqrt", sqrt_pole, lambda nq: (4 * nq) ** 2, range(2, 5), 500, 7)
    loop_sweep("linear", linear, 40000, 13)
    loop_sweep("sqrt", sqrt_pole, 1500, 17)
    print("%d checks" % CHECKS)


if __name__ == "__main__":
    main()
