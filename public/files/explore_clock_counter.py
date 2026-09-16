"""
explore_clock_counter.py -- THE CLOCK COUNTER: with write access stripped
to clock ops -- start a clock, tick a bank, nudge the newest clock's
phase, read a bank's all-zero coincidence -- does a counter stay
faithful past every program constant on the sqrt pole? (Sibling of
explore_doubling_counter.py, whose saved pointer it removes, and of
explore_born_at_zero.py, whose normal form reads every window as a
clock.)

THE SETTING. The growing-window machine on a supply m_g (the g-th window
grown has modulus m_g, g from 1). By the suffix-evaluation normal form a
register whose only op is adding the constant 1 holds t - tau mod m at
the window born at tau: a GROW starts a clock at phase 0 in every
register and the register's zero-test is the coincidence of all its
clocks. THE CLOCK MACHINE keeps exactly that and one nudge. A BANK is a
register; the program's ops are
  TICK(b, s)   add s = +1 or -1 at every window of bank b (add ONES),
  PULSE(b, s)  add s at the newest window of bank b only (add the
               frontier singleton of the last grow),
  TEST(b)      bank b is zero at every window (vacuously true before
               any grow),
  GROW         start a clock at phase 0 in every bank,
with finite control. No multiply, no register-to-register add, no
write-constant, so no saved idempotent: the only window a program can
address is the newest one. The doubling counter needs V := V + P with P
an old frontier singleton kept in a register; that op is the one
removed here.

THE QUESTION. Is a faithful counter (INC, DEC, a truthful JZ) buildable
in this class on the sqrt pole m_g = max(2, ceil(sqrt g)), past every
program constant? The line's kill, frozen as a print: a counter that
lies (a JZ answer wrong, or a window of the counter's bank not holding
the true count mod its modulus) at some count below the target.

THE HAND ATTACK (before any engine code).
  (1) AN ALIGNED BANK IS A COUNTER BELOW THE LCM. Call bank A ALIGNED at
      value V when every window holds V mod its modulus. Then TICK(A, +1)
      and TICK(A, -1) keep it aligned at V + 1 and V - 1, and TEST(A) is
      true iff V = 0 mod C, C = lcm of every modulus grown. So INC, DEC
      and JZ are one op each and faithful while V < C. INC detects its
      own overflow: V + 1 >= 1, so TEST(A) true right after INC means
      V + 1 = C.
  (2) A GROW MISALIGNS EVERY NONZERO BANK. The new window is born 0, not
      V mod m. The bank's zero set becomes V = 0 mod C and V = V_birth
      mod m', which excludes 0 unless m' divides V_birth.
  (3) REALIGNMENT NEEDS A SECOND BANK, AND THE PULSE. With a timer bank
      R at zero: loop { if TEST(A) stop; TICK(A, -1); PULSE(A, +1);
      TICK(R, +1) } holds A's newest window at 0 while A's old windows
      count down, so TEST(A) fires exactly when they reach 0, after V
      steps (V < C_old); R now holds V at every window, born 0 at the
      grow and ticked V times, so R is aligned. Then loop { if TEST(R)
      stop; TICK(R, -1); TICK(A, +1) } fires after exactly V steps
      (V < C_new), and A is aligned at V, its new window included.
      MIGRATE = GROW, then that round trip for every counter bank.
      INC = TICK(A, +1); if TEST(A): TICK(A, -1), MIGRATE, retry.
      Every unbounded supply has C_g unbounded (C_g >= max m), so the
      counter is faithful on every unbounded supply; on a bounded one C
      is capped and INC grows forever at V = C - 1.
  (4) THE GROW COUNT IS A CLOSED FORM. Grows happen only at an overflow
      and stop at the first one raising C, so reaching N ends at the
      least g with C_g > N. On the sqrt pole C_g = lcm(2..d) at d =
      m_g: 60 at d = 5, 420 at 7, 840 at 8, 2520 at 9 and 10, 27720 at
      11; the first windows of moduli 9 and 11 are g = 65 and g = 101.
      On the doubling counter the same target of 2000 cost 9,424,910
      grows: capacity here is lcm-growth, exponential in sqrt g, where
      the saved-pointer counter's is the frontier modulus itself.
  (5) ONE GLOBAL AND IS A DIFFERENT CLASS (the line as first worded, not
      rigged here). If the only read is the AND over EVERY bank, then at
      every true read every window of every bank is 0, so the
      configuration at a read is (control, grows) and nothing else: the
      round trip of (3) cannot run, since R holds V != 0 at the moment
      A must be read. Whether that class caps is a proof question: a
      side that forbids is owed a proof, not a rig.
  (6) WHAT IS REMOVED, AND THE ARMS. The distinctive ingredients are the
      pulse and the second bank. Without the pulse the round trip's
      first loop never fires once m' does not divide V; without the
      timer the grow is left misaligned.
  TRANSPLANT (marked): "the round trip returns" is read off the
  aligned-bank arithmetic of (1) at C_old and C_new; it is checked on
  the rig, not assumed.

THE PREDICTIONS (frozen before the run).
  PC1 On the sqrt pole the clock counter (bank A, timer R) runs 0 ->
      20000 -> 0 with 0 lies: after every INC and DEC, JZ is truthful
      and every window of A holds the true count mod its modulus.
  PC2 The grows spent on reaching 2000 and 20000 are exactly 65 and
      101, and every run's final grow count is the least g with
      C_g > N, printed beside it.
  PC3 On the logarithmic supply m_g = max(2, bit_length(g)), faithful
      0 -> 100 -> 0 in exactly 64 grows (C = 420 first at g = 64).
  PC4 On the non-monotone supply m_g = g at even g and 2 at odd g,
      faithful 0 -> 2000 -> 0 in exactly 18 grows (C = 5040 first at
      g = 18, C_16 = 1680).
  PC5 On the bit supply (every modulus 2) a 10^4-grow budget is
      exhausted at value 1.
  PC6 Two counter banks and one shared timer on the sqrt pole: B := 3A
      from A = 300, then A := B, ends at (900, 0) with 0 lies, in 65
      grows.
THE KILL, as a print: any lie printed by PC1 or PC6.
THE ARMS (ingredients removed; each must fail, or the survivors cannot
be credited to the ingredient).
  AX1 NO PULSE: the round trip's first loop without PULSE(A, +1). Hangs
      (a 10^5-step cap printed) at value 1, the first overflow on the
      sqrt pole, since m_2 = 2 does not divide 1.
  AX2 NO TIMER: GROW at overflow and no round trip. Lies within 0 ->
      20 -> 0 on the sqrt pole; predicted first lie a misaligned window
      at INC to 2.
THE CONTROLS (run before any prediction is read).
  C1 BISIMULATION. A dense machine engine -- registers as full lists,
     ONES re-written after every grow, the frontier singleton 1 - ONES,
     TICK as add ONES and PULSE as add that singleton -- runs the same
     program beside the offset engine used for speed (a bank stored as a
     tick total and one birth offset per window), 0 -> 40 -> 0 with the
     timer; both banks agree at every window after every op.
  C2 THE RIG CAN SEE A LIE: AX2 must print one.

RESOURCE ENVELOPE (named before the run): at most 101 windows, three
banks, a few hundred thousand loop steps; under 50 MB, under a minute,
run under memwatch.

PREDICTIONS ADJUDICATED (post-run). PC1-PC6, AX1 and AX2 CONFIRMED; the
kill did not fire; C1 and C2 passed before any prediction was read.

FINDINGS (entered after the run; every number is printed output).

1. THE CLOCK COUNTER IS FAITHFUL WITHOUT A SAVED POINTER (construction,
   the aligned-bank invariant of (1) restored by the round trip of (3);
   checked, PC1-PC5). 0 lies from 0 to 20000 and back on the sqrt pole,
   and on the logarithmic (0 -> 100 -> 0) and non-monotone (0 -> 2000
   -> 0) supplies; on the bit supply the budget is exhausted at value 1.
   The offset engine agreed with the dense 1 - ONES machine on both
   banks at every window and every test over 661 ops and 17 windows
   (C1).

2. THE GROW COUNT IS THE LCM'S (rule, derived in (4); checked at five
   targets). Reaching N spends exactly the least g with lcm(m_1..m_g) >
   N: 65 and 101 on the sqrt pole at 2000 and 20000, 64 on the
   logarithmic supply at 100, 18 on the non-monotone one at 2000, and
   65 for the two-counter run's peak of 900 (PC6). The
   saved-pointer doubling counter spent 9,424,910 grows on 2000, since
   its capacity is one frontier modulus and this counter's is the lcm
   of all of them.

3. THREE BANKS RUN A MINSKY MACHINE (PC6). Two counter banks and one
   shared timer: B := 3A from A = 300, then A := B, ends at (900, 0),
   0 lies, 65 grows, both banks' windows and both zero-tests checked
   after every op. The run is one program; universality of the clock
   machine with one AND per bank on every unbounded supply is the
   construction's, with Minsky's theorem.

4. BOTH INGREDIENTS ARE LOAD-BEARING (AX1, AX2). Without the pulse the
   round trip hangs at value 1 with 2 windows grown; without the timer
   the counter lies, first at INC to 2, 39 lies over 0 -> 20 -> 0. The
   hand attack's (6) is read with a correction found by a second
   reader: without the pulse the first loop fires at the least s with
   s = V mod C_old and s = 0 mod m', so it hangs exactly when gcd(C_old,
   m') does not divide V, returns the true value when m' divides V (s =
   V), and otherwise lands the counter at a wrong value (a third reader's
   correction, checked by brute force over C_old < 40, m' < 20); the sqrt pole's first overflow, C_old = m' = 2 at V = 1, is
   the hanging case.

SCOPE + HONESTY. The counts are observations at the sizes run; the
faithfulness at every size is the invariant argued in (1) and (3). What
is shown is that ADDRESSING is not needed: the banks are still written,
by uniform ticks and a nudge to the newest clock, and read one AND per
bank. The class with a single AND over every bank, (5), is not decided
here; a true read there leaves every bank zero, and whether that caps
every counter at a program constant is not settled here.

RUN RECORD (python prime/code/memwatch.py
prime/code/explore_clock_counter.py; 5.5 s wall clock, 12.0 MB peak
working set, 14 checks, all sections assert). C1 661 ops, 17 windows,
agree. AX2 39 lies, first ('inc', 2), 2 grows. AX1 hangs at value 1, 2
windows. PC sqrt 2000: 0 lies, 65 grows; sqrt 20000: 0 lies, 101 grows;
log 100: 0 lies, 64 grows; alt 2000: 0 lies, 18 grows; bit: budget at
value 1. PC6 (900, 0), 0 lies, 65 grows.
"""

import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1
    print("  [ok] " + msg)


def ceil_sqrt(g):
    r = math.isqrt(g)
    return r if r * r == g else r + 1


SUPPLIES = {
    "sqrt": lambda g: max(2, ceil_sqrt(g)),
    "log": lambda g: max(2, g.bit_length()),
    "alt": lambda g: g if g % 2 == 0 else 2,
    "bit": lambda g: 2,
}


class OutOfBudget(Exception):
    pass


class Hang(Exception):
    pass


class Offset:
    """The clock machine, a bank stored as a tick total t and, per window,
    the tick total at birth less the pulses it took: window w holds
    (t - base[w]) mod m_w."""

    def __init__(self, supply, nbanks, budget):
        self.m_of = SUPPLIES[supply]
        self.moduli = []
        self.t = [0] * nbanks
        self.base = [[] for _ in range(nbanks)]
        self.budget = budget

    def grow(self):
        if len(self.moduli) >= self.budget:
            raise OutOfBudget
        self.moduli.append(self.m_of(len(self.moduli) + 1))
        for b in range(len(self.t)):
            self.base[b].append(self.t[b])

    def tick(self, b, s):
        self.t[b] += s

    def pulse(self, b, s):
        self.base[b][-1] -= s

    def test(self, b):
        t = self.t[b]
        return all((t - x) % m == 0 for x, m in zip(self.base[b], self.moduli))

    def windows(self, b):
        t = self.t[b]
        return [(t - x) % m for x, m in zip(self.base[b], self.moduli)]


class Dense:
    """The reference: registers as full lists of residues, ONES re-written
    to 1 after every grow, the frontier singleton 1 - ONES."""

    def __init__(self, supply, nbanks, budget):
        self.m_of = SUPPLIES[supply]
        self.moduli = []
        self.regs = [[] for _ in range(nbanks)]
        self.ones = []
        self.w = []
        self.budget = budget

    def grow(self):
        if len(self.moduli) >= self.budget:
            raise OutOfBudget
        self.moduli.append(self.m_of(len(self.moduli) + 1))
        for r in self.regs:
            r.append(0)
        self.ones.append(0)
        self.w = [(1 - o) % m for o, m in zip(self.ones, self.moduli)]
        self.ones = [1 % m for m in self.moduli]

    def _add(self, b, y, s):
        self.regs[b] = [(a + s * c) % m
                        for a, c, m in zip(self.regs[b], y, self.moduli)]

    def tick(self, b, s):
        self._add(b, self.ones, s)

    def pulse(self, b, s):
        self._add(b, self.w, s)

    def test(self, b):
        return all(v == 0 for v in self.regs[b])

    def windows(self, b):
        return list(self.regs[b])


class ClockCounters:
    """Counter banks 0..k-1 and the timer bank k, in clock ops only."""

    def __init__(self, eng, k, pulse=True, timer=True, cap=10 ** 5,
                 hook=None):
        self.e, self.k, self.R = eng, k, k
        self.use_pulse, self.use_timer, self.cap = pulse, timer, cap
        self.hook = hook or (lambda: None)

    def round_trip(self, a):
        e, R = self.e, self.R
        steps = 0
        while not e.test(a):
            e.tick(a, -1)
            if self.use_pulse:
                e.pulse(a, +1)
            e.tick(R, +1)
            self.hook()
            steps += 1
            if steps > self.cap:
                raise Hang
        while not e.test(R):
            e.tick(R, -1)
            e.tick(a, +1)
            self.hook()

    def migrate(self):
        self.e.grow()
        self.hook()
        if self.use_timer:
            for a in range(self.k):
                self.round_trip(a)

    def inc(self, a):
        e = self.e
        while True:
            e.tick(a, +1)
            self.hook()
            if not e.test(a):
                return
            e.tick(a, -1)
            self.hook()
            self.migrate()

    def dec(self, a):
        self.e.tick(a, -1)
        self.hook()

    def jz(self, a):
        return self.e.test(a)


def faithful(eng, bank, v):
    return all(x == v % m for x, m in zip(eng.windows(bank), eng.moduli))


def least_g(supply, N):
    m_of, c, g = SUPPLIES[supply], 1, 0
    while c <= N:
        g += 1
        c = c * m_of(g) // math.gcd(c, m_of(g))
    return g


def updown(supply, N, budget=10 ** 4, **kw):
    e = Offset(supply, 2, budget)
    c = ClockCounters(e, 1, **kw)
    lies, first = 0, None
    for v in range(1, N + 1):
        c.inc(0)
        if c.jz(0) or not faithful(e, 0, v):
            lies += 1
            first = first or ("inc", v)
    grows_up = len(e.moduli)
    for v in range(N - 1, -1, -1):
        c.dec(0)
        if c.jz(0) != (v == 0) or not faithful(e, 0, v):
            lies += 1
            first = first or ("dec", v)
    return lies, grows_up, first


def c1_bisimulation():
    print("== C1 bisimulation: offset engine against the dense machine ==")
    o = Offset("sqrt", 2, 10 ** 4)
    agree, ops = True, 0
    # replay the dense run's op word on the offset engine, compared per op
    log = []
    rec_d = Dense("sqrt", 2, 10 ** 4)

    class Rec:
        def __init__(s, eng):
            s.eng = eng

        def __getattr__(s, name):
            f = getattr(s.eng, name)
            if name in ("grow", "tick", "pulse"):
                def g(*a):
                    log.append((name, a))
                    return f(*a)
                return g
            return f

    cr = ClockCounters(Rec(rec_d), 1)
    for step in [+1] * 40 + [-1] * 40:
        cr.inc(0) if step > 0 else cr.dec(0)
    shadow = Dense("sqrt", 2, 10 ** 4)
    for name, a in log:
        getattr(shadow, name)(*a)
        getattr(o, name)(*a)
        ops += 1
        for b in (0, 1):
            if shadow.windows(b) != o.windows(b) or \
                    shadow.test(b) != o.test(b):
                agree = False
    agree = agree and rec_d.regs == shadow.regs
    print(f"   {ops} ops, {len(o.moduli)} windows; engines agree: {agree}")
    ok(agree, "C1: offset and dense engines agree on both banks at every "
              "window and every test after every op, 0 -> 40 -> 0")


def c2_and_arms():
    print("== AX2 no timer (C2: the rig sees a lie) ==")
    lies, g, first = updown("sqrt", 20, timer=False)
    print(f"   sqrt pole 0 -> 20 -> 0 without the round trip: {lies} lies, "
          f"first {first}, {g} grows")
    ok(lies > 0, "C2/AX2: the counter without its timer lies")
    print("== AX1 no pulse ==")
    try:
        lies, g, first = updown("sqrt", 20, pulse=False)
        hang = None
    except Hang:
        hang = True
    e = Offset("sqrt", 2, 10 ** 4)
    c = ClockCounters(e, 1, pulse=False)
    at = None
    for v in range(1, 21):
        try:
            c.inc(0)
        except Hang:
            at = v - 1
            break
    print(f"   round trip without the pulse hangs at value {at} "
          f"({len(e.moduli)} windows grown)")
    ok(hang and at == 1, "AX1: without the pulse the round trip hangs at "
                         "value 1")


def pc_runs():
    print("== PC1-PC5 the clock counter up and down ==")
    for supply, N, want in (("sqrt", 2000, 65), ("sqrt", 20000, 101),
                            ("log", 100, 64), ("alt", 2000, 18)):
        lies, g, first = updown(supply, N)
        print(f"   {supply}, 0 -> {N} -> 0: {lies} lies, {g} grows to "
              f"reach {N}; least g with C_g > N = {least_g(supply, N)}")
        ok(lies == 0, f"PC: faithful 0 -> {N} -> 0 on the {supply} supply")
        ok(g == want == least_g(supply, N),
           f"PC: {g} grows, the closed form's {want}")
    e = Offset("bit", 2, 10 ** 4)
    c = ClockCounters(e, 1)
    at = None
    for v in range(1, 10):
        try:
            c.inc(0)
        except OutOfBudget:
            at = v - 1
            break
    print(f"   bit supply: budget exhausted at value {at}")
    ok(at == 1, "PC5: on the bit supply the budget is exhausted at value 1")


def pc6_two_counters():
    print("== PC6 two counters and a shared timer on the sqrt pole ==")
    e = Offset("sqrt", 3, 10 ** 4)
    c = ClockCounters(e, 2)
    A, B = 0, 1
    a = b = lies = 0

    def check():
        return int(not (faithful(e, A, a) and faithful(e, B, b)
                        and c.jz(A) == (a == 0) and c.jz(B) == (b == 0)))

    for _ in range(300):
        c.inc(A)
        a += 1
        lies += check()
    while not c.jz(A):
        c.dec(A)
        a -= 1
        lies += check()
        for _ in range(3):
            c.inc(B)
            b += 1
            lies += check()
    while not c.jz(B):
        c.dec(B)
        b -= 1
        lies += check()
        c.inc(A)
        a += 1
        lies += check()
    print(f"   final (A, B) = ({a}, {b}), {lies} lies, {len(e.moduli)} grows")
    ok((a, b) == (900, 0) and faithful(e, A, 900) and faithful(e, B, 0)
       and lies == 0, "PC6: B := 3A then A := B ends at (900, 0), no lie")
    ok(len(e.moduli) == 65, "PC6: 65 grows")


if __name__ == "__main__":
    c1_bisimulation()
    c2_and_arms()
    pc_runs()
    pc6_two_counters()
    print(f"\nALL SECTIONS PASS ({CHECKS} checks)")
