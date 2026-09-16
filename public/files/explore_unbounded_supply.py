"""
explore_unbounded_supply.py -- EVERY UNBOUNDED SUPPLY: does the doubling
counter, with its compare moved to after every grow, stay faithful on a
supply that is unbounded but not monotone, where the block-timed original
is defeated at value 1?
(Sibling of explore_doubling_counter.py, whose engine and counter it
imports, and of explore_sqrt_supply.py, explore_bit_supply.py.)

THE SETTING. The growing-window machine of explore_doubling_counter.py:
registers are columns over a pool of windows Z/m, componentwise add and
subtract, one zero-test per register (the AND of its per-window zero
bits), and GROW, which appends a window whose modulus is the supply's
next value, every register born 0 there, handing the program the fresh
window's idempotent. The doubling counter keeps its value V on one saved
window P and, when that window is full, grows in blocks of m_P grows
(counted by a rider on P) and compares the frontier against 2 * m_P only
at the end of a block. On a nondecreasing unbounded supply some block's
frontier outlasts, so every such supply carries two faithful counters.
The compares fall on an arithmetic progression of window indices, so a
supply that is large only off that progression starves the original.

THE QUESTION. Does a compare after EVERY grow carry the counter on every
unbounded supply, monotone or not, and does the block-timed original fail
on a non-monotone one?

THE CONSTRUCTION (machine ops only). As the doubling counter, with
MIGRATE replaced by
  MIGRATE'  repeat: GROW once, F := the frontier singleton; COMPARE F
            against 2 * m_P by two riders in lockstep (F outlasts when P's
            rider wraps twice before F's wraps once) -- until F outlasts;
            then TRANSFER as before and re-point.
A compare costs at most 2 * m_P steps and reads nothing but zero-tests of
registers supported on one window; its riders are scratch registers,
reset before the next compare.

THE HAND ATTACK (before any engine code).
  (1) TERMINATION IS UNBOUNDEDNESS ALONE. The compare is exact (F outlasts
      iff m_F > 2 * m_P, both riders wrapping in lockstep), and it runs at
      every index, so MIGRATE' ends at the first index past the current
      frontier with m > 2 * m_P, which exists exactly when the supply is
      unbounded. No monotonicity is read anywhere.
  (2) THE ALTERNATING SUPPLY, m_g = g at even g and 2 at odd g, walked by
      hand. The counter's first window is g = 1, m_P = 2. The original's
      blocks are 2 grows long, so its compares see g = 3, 5, 7, ..., all
      modulus 2, and it never migrates: value 1 is its ceiling. MIGRATE'
      sees g = 2 (m 2, no), 3 (2, no), 4 (4, no: equal to 2 * m_P is not
      past it), 5 (2, no), 6 (6, yes).
  (3) THE COST. Each migration ends at an index whose modulus exceeds
      twice the old one; on the alternating supply and on the power spike
      supply below that index is at most about 4 * m_P + 2, so reaching N
      spends O(N) grows and O(N^2) compare steps.
  (4) THE SPIKE SUPPLY, m_g = g at powers of two and 2 elsewhere, is
      unbounded with lim inf 2 and its large values on a set of density
      zero: the every-grow compare must find each spike.
  TRANSPLANT (marked): "the frontier singleton after a non-monotone grow is
  still the fresh window's idempotent" is read off the engine's 1 - ONES
  construction on a monotone supply; it is checked here by bisimulation.

THE PREDICTIONS (frozen before the run).
  PN1 On the alternating supply the every-grow counter counts 0 -> 200 by
      INC and back to 0 by DEC with 0 lies (zero-test and register value
      both equal to the true count after every op), spending at most
      8 * 200 grows to reach 200.
  PN2 The same on the spike supply, 0 -> 200 -> 0, 0 lies, at most 8 * 200
      grows to reach 200.
  PN3 Two every-grow counters on the alternating supply, B := 3A from
      A = 100, then A := B, end at (300, 0) with every zero-test truthful.
  PN4 On the sqrt pole the every-grow counter is faithful 0 -> 60 -> 0.
  PN5 On the bit supply (every modulus 2) MIGRATE' exhausts a 10^4-grow
      budget at value 1.
THE KILLS, as prints: any lie printed by PN1, PN2 or PN3; PN3's final pair
printing anything but (300, 0).
THE CONTROLS (run before any prediction is read).
  C1 BISIMULATION. The sparse engine against the dense 1 - ONES engine,
     every-grow counter, 0 -> 20 -> 0 on the alternating supply: V and P
     agree at every window after every INC and DEC, same windows grown.
  C2 THE ORIGINAL IS DEFEATED. The block-timed doubling counter on the
     alternating supply exhausts a 10^4-grow budget at value 1, so the
     supply is one the every-grow compare has to earn.

RESOURCE ENVELOPE (named before the run): small dicts and one dense engine
at a few hundred windows; under 100 MB, under one minute, run under
memwatch.

PREDICTIONS ADJUDICATED (post-run). PN1-PN5 CONFIRMED; no kill fired; C1
and C2 passed before any prediction was read.

FINDINGS (entered after the run; every number is printed output).

1. THE ORIGINAL IS DEFEATED, THE EVERY-GROW COUNTER IS NOT (C2, PN1). On
   m_g = g at even g and 2 at odd g, the block-timed doubling counter
   exhausts its 10^4-grow budget at value 1, while the every-grow counter
   counts 0 -> 200 -> 0 with 0 lies, reaching 200 at 254 grows. The sparse
   engine agreed with the dense 1 - ONES engine at every window after
   every one of 40 ops over 30 windows on that supply (C1).

2. SPARSE SPIKES ARE FOUND (PN2). On m_g = g at powers of two and 2
   elsewhere, 0 -> 200 -> 0 with 0 lies, 512 grows to reach 200.

3. TWO COUNTERS RUN ON THE ALTERNATING SUPPLY (PN3). B := 3A from A = 100,
   then A := B, ends at (300, 0) with 0 lies at 520 grows. With (1) of the
   hand attack, which reads no monotonicity, every unbounded supply carries
   a Minsky machine's two counters; the bounded pole fails at value 1
   (PN5), and the sqrt pole is carried too, 0 -> 60 -> 0 at 8837 grows
   (PN4).

SCOPE + HONESTY. The counts are observations at the sizes run; that
MIGRATE' terminates on every unbounded supply and keeps the value below
its window's modulus is the construction's argument, (1) above, and is
not machine-checked beyond the sizes printed. Two supplies stand in for
the non-monotone ones. The compare's cost is paid in steps, not grows,
so the every-grow counter spends O(m_P) steps per grow where the block
original spends O(m_P) per block.

RUN RECORD (python prime/code/memwatch.py
prime/code/explore_unbounded_supply.py; 0.5 s wall clock, 13.2 MB peak
working set against the 512 MB ceiling, 7 checks, all sections assert).
C1 40 ops, 30 windows, agree. C2 original exhausted at value 1. PN1 0
lies, 254 grows. PN2 0 lies, 512 grows. PN3 (300, 0), 0 lies, 520 grows.
PN4 0 lies, 8837 grows. PN5 exhausted at value 1.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_doubling_counter import (SUPPLIES, Counter, Dense, OutOfBudget,
                                      Sparse, value_of)

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1
    print("  [ok] " + msg)


def is_pow2(g):
    return g >= 2 and g & (g - 1) == 0


SUPPLIES["alt"] = lambda g: g if g % 2 == 0 else 2
SUPPLIES["spike"] = lambda g: g if is_pow2(g) else 2


class EveryGrowCounter(Counter):
    """The doubling counter with a compare after every grow."""

    def migrate(self):
        e = self.e
        while True:
            F = e.grow()
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


def run_updown(cls, supply, N, budget):
    e = Sparse(supply, budget)
    c = cls(e)
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
    return lies, peak_grows


def exhausts_at(cls, supply, budget):
    e = Sparse(supply, budget)
    c = cls(e)
    for _ in range(1, 10):
        try:
            c.inc()
        except OutOfBudget:
            return value_of(e, c.V)
    return None


def c1_bisimulation():
    print("== C1 bisimulation on the alternating supply ==")
    s, d = Sparse("alt", 10 ** 5), Dense("alt", 10 ** 5)
    ts, td = [], []
    cs, cd = EveryGrowCounter(s, ts), EveryGrowCounter(d, td)
    for _ in range(20):
        cs.inc()
        cd.inc()
    for _ in range(20):
        cs.dec()
        cd.dec()
    agree = len(ts) == len(td) and s.n == len(d.moduli)
    for (a, vs, ps), (b, vd, pd) in zip(ts, td):
        if (a != b or [vs.get(w, 0) for w in range(len(vd))] != vd
                or [ps.get(w, 0) for w in range(len(pd))] != pd):
            agree = False
            break
    print(f"   40 ops, {s.n} windows grown by each engine")
    ok(agree, "C1: sparse and dense engines agree on V and P at every window "
              "after every INC and DEC, 0 -> 20 -> 0, alternating supply")


def c2_original_defeated():
    print("== C2 the block-timed original on the alternating supply ==")
    at = exhausts_at(Counter, "alt", 10 ** 4)
    print(f"   original: budget exhausted at value {at}")
    ok(at == 1, "C2: the block-timed counter exhausts its budget at value 1 "
                "on the alternating supply")


def predictions():
    print("== PN1-PN2 the every-grow counter on two non-monotone supplies ==")
    for tag, supply in (("PN1", "alt"), ("PN2", "spike")):
        lies, grows = run_updown(EveryGrowCounter, supply, 200, 10 ** 6)
        print(f"   {supply}: 0 -> 200 -> 0, {lies} lies, {grows} grows to "
              f"reach 200")
        ok(lies == 0 and grows <= 8 * 200,
           f"{tag}: faithful 0 -> 200 -> 0 on the {supply} supply within "
           f"8 N grows")
    print("== PN3 two counters on the alternating supply ==")
    e = Sparse("alt", 10 ** 7)
    A, B = EveryGrowCounter(e), EveryGrowCounter(e)
    lies = 0
    for _ in range(100):
        A.inc()
    a, b = 100, 0
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
    ok(final == (300, 0) and lies == 0,
       "PN3: B := 3A from A = 100, then A := B, ends at (300, 0), no lie")
    print("== PN4-PN5 the monotone and bounded poles ==")
    lies, grows = run_updown(EveryGrowCounter, "sqrt", 60, 10 ** 8)
    print(f"   sqrt: 0 -> 60 -> 0, {lies} lies, {grows} grows")
    ok(lies == 0, "PN4: faithful 0 -> 60 -> 0 on the sqrt pole")
    at = exhausts_at(EveryGrowCounter, "bit", 10 ** 4)
    print(f"   bit: budget exhausted at value {at}")
    ok(at == 1, "PN5: on the bit supply MIGRATE' exhausts its budget at "
                "value 1")


if __name__ == "__main__":
    c1_bisimulation()
    c2_original_defeated()
    predictions()
    print(f"\nALL SECTIONS PASS ({CHECKS} checks)")
