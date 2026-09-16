"""
explore_doubling_counter.py -- THE DOUBLING COUNTER: does a counter that
moves its whole value to a fresher window only when full, after growing
until the frontier modulus has doubled, stay faithful on a slow supply?
(Sibling of explore_sqrt_supply.py, whose regress argument it tests, and
of explore_bit_supply.py, explore_minimal_carrier.py.)

THE SETTING. The growing-window machine: registers are columns over a pool
of windows Z/m; the ops are componentwise add, subtract, multiply and
write-constant, one zero-test per register (the AND of its per-window zero
bits), and GROW, which appends a window whose modulus is the supply's next
value, every register born 0 there, handing the program the fresh window's
idempotent (the frontier singleton, 1 - ONES after the grow). Below the
linear rate every exact counter built so far caps: the positional counter
survives iff W_d * m_g >= g, and explore_sqrt_supply.py reads a
value-dependent grow schedule as a regress, "timing the grows needs the
very unbounded counter being built". That no construction escapes is
conjectured.

THE QUESTION. The regress argument prices a counter that grows once per
INC, or on a schedule fixed in advance. A counter can instead time its
grows off its own value while that value is still faithful. Does such a
counter stay faithful, INC and DEC with a truthful zero-test, past every
cap on a slow supply?

THE CONSTRUCTION (machine ops only; the harness reads nothing the program
does not).
  V   the value, supported on ONE window, the pointed one.
  P   that window's idempotent, saved when it was the frontier.
  INC  if zero(V + P) the value is m_P - 1 and the window is FULL: first
       MIGRATE, then V := V + P.
  DEC  (guarded by zero(V) false) V := V - P.
  JZ   zero(V).
  MIGRATE  repeat: GROW m_P times, the count kept by a rider on P's own
       window (C := 0; loop C := C + P, GROW, until zero(C)); then COMPARE
       the frontier F against 2 * m_P by two riders in lockstep, one step
       each, F outlasting when P's rider wraps twice before F's wraps once
       -- until F outlasts; then TRANSFER, loop V := V - P,
       V2 := V2 + F until zero(V), and re-point, P := F, V := V2.
The value never exceeds its window's modulus less one, so the register
holds the true count exactly; the only reads are zero-tests of registers
supported on one or two windows.

THE HAND ATTACK (before any engine code).
  (1) THE REGRESS IS NOT MET. The grows are timed by a rider on the pointed
      window, whose modulus the program never reads, and the stop is a
      comparison of two wraps. Nothing unbounded is needed beyond the value
      already held, which is faithful up to m_P - 1 by construction.
  (2) THE CAP LEMMA IS NOT CONTRADICTED. The value stays below the frontier
      modulus at every step, W_d = 1: the lemma bounds a value by the
      frontier and says nothing about how many grows the program spends.
      The survival condition W_d * m_g >= g carries g = the INC count only
      under one grow per INC.
  (3) THE COST. On the sqrt pole the modulus doubles when the window count
      roughly quadruples, so counting to N spends on the order of 4 N^2
      grows plus N-linear transfers per doubling; on the bit supply no
      window ever outlasts, and MIGRATE runs out of budget at the first full
      window; on a supply that is unbounded but logarithmic the grows run
      exponential in N and the counter stays faithful.
  (4) TWO COUNTERS. Two such registers keep independent pointers, and a
      grow for one is born 0 in the other, so a Minsky machine's two
      counters run side by side.
  TRANSPLANT (marked): "a pointer survives later grows" is read off the
  normal form's born-at-zero clause; it is checked here, not assumed.

THE PREDICTIONS (frozen before the run).
  PD1 On the sqrt pole the counter counts 0 -> 2000 by INC and back to 0 by
      DEC with its zero-test truthful after every op and the harness's true
      count equal to the register's single nonzero entry throughout.
  PD2 Grows spent to reach 2000 sit within a factor 4 of 4 * 2000^2.
  PD3 On the logarithmic supply m_g = max(2, bit_length(g)) the counter is
      faithful 0 -> 12 -> 0.
  PD4 On the bit supply (every modulus 2) MIGRATE exhausts a 10^5-grow
      budget at the first full window, value 1.
  PD5 A two-counter program on the sqrt pole -- B := 3A from A = 300, then
      A := B -- ends with A = 900, B = 0, both zero-tests truthful at
      every step.
THE KILLS, as prints: any op after which the zero-test disagrees with the
true count, or the register's value disagrees with it, on the sqrt pole
within 2000 (kills PD1); PD5's final pair printing anything but (900, 0).
THE CONTROLS.
  C1 BISIMULATION. The sparse engine (a register stored as its nonzero
     windows; exact because the program never writes a nonzero constant and
     the frontier singleton is supported on one window) is run step for
     step beside a dense engine (every register a full list, the frontier
     singleton computed as 1 - ONES exactly as explore_sqrt_supply.py does)
     to value 40 and back, on the sqrt pole; V and P must agree at every
     window after every INC and DEC, and the two engines must grow the
     same number of windows (the scratch registers inside MIGRATE are not
     compared).
  C2 THE CAP REPRODUCED. explore_sqrt_supply.py's rider counter (one grow
     per INC) run on the same sqrt engine must lie at a small value, so the
     supply and the zero-test here are the ones the cap was measured on.
  C3 THE BIT SUPPLY IS PD4, a supply on which the construction must fail.

RESOURCE ENVELOPE (named before the run): the sparse engine computes
each window's modulus on the fly and stores a handful of small dicts; under 100 MB,
under two minutes, run under memwatch.

PREDICTIONS ADJUDICATED (post-run). PD1, PD2, PD3, PD4 and PD5 CONFIRMED;
no kill fired; C1 and C2 passed before any prediction was read. One rig
error preceded the clean run: the first compare stepped P's rider twice
per F step and stopped at its first wrap, which declares m_F > m_P / 2,
and C1's DEC assert caught the lost value.

FINDINGS (entered after the run; every number is printed output).

1. THE DOUBLING COUNTER IS FAITHFUL ON THE SQRT POLE (construction, the
   invariant V < m_P holding by the migrate rule; checked, PD1-PD2). From
   0 to 2000 by INC and back to 0 by DEC, 0 lies: after every op the
   zero-test agreed with the true count and the register's one nonzero
   residue equalled it. Reaching 2000 spent 9424910 grows, 0.589 of
   4 N^2. The one-grow-per-INC rider on the same supply first lies at
   count 3 (C2), so the supply and the zero-test are the ones the cap was
   measured on; the sparse engine agreed with the dense 1 - ONES engine at
   every window after every one of 80 ops over 2120 windows (C1).

2. THE REGRESS DOES NOT BIND. The grows are timed by a rider on the
   counter's own window and stopped by a comparison of wraps, so the
   counter never needs a value it does not already hold faithfully. The
   cap lemma stands as a bound on a value by its frontier; the survival
   condition W_d * m_g >= g is a statement about one grow per INC and
   not about the machine.

3. ANY UNBOUNDED SUPPLY CARRIES IT, NO BOUNDED ONE DOES (PD3-PD4). On
   m_g = max(2, bit_length(g)) the counter is faithful 0 -> 12 -> 0 at
   4194304 grows; on the bit supply MIGRATE exhausts its 10^5 budget at
   value 1, the first full window, as the finite-state pole requires.

4. TWO COUNTERS RUN ON ONE MACHINE (PD5). B := 3A from A = 300, then
   A := B, ends at (900, 0) with every zero-test truthful, 2353551 grows.
   Two faithful counters with INC, DEC and zero-test are a Minsky
   machine's, so the sqrt pole's machine is universal by construction,
   and so is the machine on every nondecreasing unbounded supply. A
   supply unbounded but not monotone needs a compare after every grow,
   since the checks here fall on an arithmetic progression of windows
   (m_g = g at even g and 2 at odd g defeats them at value 1, found by a
   second reader); that variant is explore_unbounded_supply.py, faithful
   on two such supplies, so every unbounded supply is universal. The hand
   attack's (3) is read with that correction.

SCOPE + HONESTY. The counts are observations at the sizes run; the
faithfulness at every size is the construction's invariant, argued in
THE CONSTRUCTION and not machine-checked beyond 2000. The program's
control is finite: two loop flags and a wrap counter bounded by 2. What
this refutes is the conjecture that no construction simulates two
counters below the linear rate; which statements elsewhere rest on that
conjecture is the reading this record hands on.

RUN RECORD (python prime/code/memwatch.py
prime/code/explore_doubling_counter.py; 26.0 s wall clock, 217.3 MB peak
working set against the 512 MB ceiling -- over the 100 MB named, the
dense reference engine keeping every register it creates in C1 -- 7
checks, all sections assert). C1 80 ops, 2120 windows, agree. C2 rider
first lies at 3. PD1 0 lies, 9424910 grows, ratio 0.589. PD3 0 lies,
4194304 grows. PD4 budget exhausted at value 1. PD5 (900, 0), 0 lies,
2353551 grows.
"""

import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_sqrt_supply import Rider, sqrt_supply

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
    "bit": lambda g: 2,
}


class OutOfBudget(Exception):
    pass


class Sparse:
    """The machine with registers stored as {window: nonzero residue}."""

    def __init__(self, supply, budget):
        self.m_of = SUPPLIES[supply]
        self.n = 0              # windows grown
        self.budget = budget
        self.grows = 0

    def mod(self, w):
        return self.m_of(w + 1)

    def grow(self):
        if self.grows >= self.budget:
            raise OutOfBudget
        self.n += 1
        self.grows += 1
        return {self.n - 1: 1 % self.mod(self.n - 1)}

    def add(self, x, y, sign=1):
        out = dict(x)
        for w, b in y.items():
            v = (out.get(w, 0) + sign * b) % self.mod(w)
            if v:
                out[w] = v
            else:
                out.pop(w, None)
        return out

    def zero(self, x):
        return not x


class Dense:
    """The reference: every register a full list, the frontier singleton
    1 - ONES, ONES re-written to 1 after every grow."""

    def __init__(self, supply, budget):
        self.m_of = SUPPLIES[supply]
        self.moduli = []
        self.budget = budget
        self.grows = 0
        self.regs = []          # every live dense register, extended on grow
        self.ones = []

    def grow(self):
        if self.grows >= self.budget:
            raise OutOfBudget
        m = self.m_of(len(self.moduli) + 1)
        self.moduli.append(m)
        for r in self.regs:
            r.append(0)
        self.ones.append(0)
        w = [(1 - o) % mm for o, mm in zip(self.ones, self.moduli)]
        self.ones[:] = [1 % mm for mm in self.moduli]
        self.grows += 1
        return self.track(w)

    def track(self, r):
        self.regs.append(r)
        return r

    def add(self, x, y, sign=1):
        return self.track([(a + sign * b) % m
                           for a, b, m in zip(x, y, self.moduli)])

    def zero(self, x):
        return all(v == 0 for v in x)

    def empty(self):
        return self.track([0] * len(self.moduli))


class Counter:
    """The doubling counter, written in machine ops only."""

    def __init__(self, eng, trace=None):
        self.e = eng
        self.trace = trace
        self.P = eng.grow()
        self.V = self.blank()

    def blank(self):
        return self.e.empty() if isinstance(self.e, Dense) else {}

    def _log(self, tag):
        if self.trace is not None:
            self.trace.append((tag, self.V, self.P))

    def migrate(self):
        e = self.e
        while True:
            C = self.blank()                 # grow m_P times
            while True:
                C = e.add(C, self.P)
                F = e.grow()
                if e.zero(C):
                    break
            A, B = self.blank(), self.blank()  # compare F against 2 m_P
            f_outlasts = None
            b_wraps = 0                       # finite control: 0, 1, 2
            while f_outlasts is None:
                A = e.add(A, F)
                B = e.add(B, self.P)
                if e.zero(A):
                    f_outlasts = False
                elif e.zero(B):
                    b_wraps += 1
                    if b_wraps == 2:
                        f_outlasts = True
            if f_outlasts:
                break
        V2 = self.blank()
        while not e.zero(self.V):
            self.V = e.add(self.V, self.P, -1)
            V2 = e.add(V2, F)
        self.P, self.V = F, V2

    def inc(self):
        if self.e.zero(self.e.add(self.V, self.P)):
            self.migrate()
        self.V = self.e.add(self.V, self.P)
        self._log("inc")

    def dec(self):
        assert not self.e.zero(self.V)
        self.V = self.e.add(self.V, self.P, -1)
        self._log("dec")

    def jz(self):
        return self.e.zero(self.V)


def value_of(eng, reg):
    """harness-only: the register's single nonzero window's residue."""
    if isinstance(eng, Sparse):
        assert len(reg) <= 1
        return next(iter(reg.values()), 0)
    nz = [v for v in reg if v]
    assert len(nz) <= 1
    return nz[0] if nz else 0


def run_updown(supply, N, budget):
    e = Sparse(supply, budget)
    c = Counter(e)
    lies = 0
    for k in range(1, N + 1):
        c.inc()
        if c.jz() or value_of(e, c.V) != k:
            lies += 1
    peak_grows = e.grows
    for k in range(N - 1, -1, -1):
        c.dec()
        if c.jz() != (k == 0) or value_of(e, c.V) != k:
            lies += 1
    return lies, peak_grows, e.n


def c1_bisimulation():
    print("== C1 bisimulation: sparse engine against the dense engine ==")
    s, d = Sparse("sqrt", 10 ** 6), Dense("sqrt", 10 ** 6)
    ts, td = [], []
    cs, cd = Counter(s, ts), Counter(d, td)
    for _ in range(40):
        cs.inc()
        cd.inc()
    for _ in range(40):
        cs.dec()
        cd.dec()
    agree = len(ts) == len(td) and s.n == len(d.moduli)
    for (a, vs, ps), (b, vd, pd) in zip(ts, td):
        dense_vs = [vs.get(w, 0) for w in range(len(vd))]
        dense_ps = [ps.get(w, 0) for w in range(len(pd))]
        if a != b or dense_vs != vd[:len(vd)] or dense_ps != pd[:len(pd)]:
            agree = False
            break
    print(f"   80 ops, {s.n} windows grown by each engine")
    ok(agree, "C1: the sparse and dense engines agree on V and P at every "
              "window after every INC and DEC, 0 -> 40 -> 0 on the sqrt pole")


def c2_cap_reproduced():
    print("== C2 the one-grow-per-INC rider caps on the same supply ==")
    r = Rider(sqrt_supply())
    lie = None
    for k in range(1, 200):
        r.inc()
        vals = [v for v in r.reg["V"] if v]
        if len(vals) != 1 or vals[0] != k:
            lie = k
            break
    print(f"   rider's first unfaithful count on the sqrt pole: {lie}")
    ok(lie is not None and lie < 200,
       "C2: the rider that grows once per INC lies at a small count on the "
       "sqrt pole")


def pd_runs():
    print("== PD1-PD4 the doubling counter up and down ==")
    lies, grows, n = run_updown("sqrt", 2000, 10 ** 9)
    print(f"   sqrt pole, 0 -> 2000 -> 0: {lies} lies, {grows} grows to "
          f"reach 2000, ratio to 4*N^2 = {grows / (4 * 2000 ** 2):.3f}")
    ok(lies == 0, "PD1: faithful 0 -> 2000 -> 0 on the sqrt pole")
    ok(0.25 <= grows / (4 * 2000 ** 2) <= 4,
       "PD2: grows within a factor 4 of 4 N^2")
    lies, grows, n = run_updown("log", 12, 10 ** 8)
    print(f"   log supply, 0 -> 12 -> 0: {lies} lies, {grows} grows")
    ok(lies == 0, "PD3: faithful 0 -> 12 -> 0 on the logarithmic supply")
    e = Sparse("bit", 10 ** 5)
    c = Counter(e)
    failed_at = None
    for k in range(1, 10):
        try:
            c.inc()
        except OutOfBudget:
            failed_at = value_of(e, c.V)
            break
    print(f"   bit supply: budget exhausted at value {failed_at}")
    ok(failed_at == 1, "PD4: on the bit supply MIGRATE exhausts its budget "
                       "at the first full window, value 1")


def pd5_two_counters():
    print("== PD5 two counters on one sqrt-pole machine ==")
    e = Sparse("sqrt", 10 ** 9)
    A, B = Counter(e), Counter(e)
    lies = 0
    for _ in range(300):
        A.inc()
    a, b = 300, 0
    while not A.jz():
        A.dec()
        a -= 1
        for _ in range(3):
            B.inc()
            b += 1
        if value_of(e, A.V) != a or value_of(e, B.V) != b or A.jz() != (a == 0):
            lies += 1
    while not B.jz():
        B.dec()
        b -= 1
        A.inc()
        a += 1
        if value_of(e, A.V) != a or value_of(e, B.V) != b or B.jz() != (b == 0):
            lies += 1
    final = (value_of(e, A.V), value_of(e, B.V))
    print(f"   final (A, B) = {final}, {lies} lies, {e.grows} grows")
    ok(final == (900, 0) and lies == 0,
       "PD5: B := 3A from A = 300, then A := B, ends at (900, 0) with every "
       "zero-test truthful")


if __name__ == "__main__":
    c1_bisimulation()
    c2_cap_reproduced()
    pd_runs()
    pd5_two_counters()
    print(f"\nALL SECTIONS PASS ({CHECKS} checks)")
