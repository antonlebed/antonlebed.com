"""
explore_minimal_carrier.py -- THE MINIMAL CARRIER: what structure does
the frontier rider actually stand on? (Sibling of
explore_frontier_rider.py -- the rig here is that script's, re-keyed
by window index so moduli may repeat; the pin-to-minimal-carrier
method imitates explore_walls_provenance.py, which pins each
OBSTRUCTION to the least structure carrying it -- this script pins a
CAPABILITY the same way. Related: explore_bare_class.py,
explore_growth_machine.py.)

THE QUESTION. explore_frontier_rider.py settled the bare element
class UNIVERSAL: a sparse counter riding the growth frontier -- value
as a residue in one pointed window, literal zero elsewhere -- runs
two exact Minsky counters with no base extension, no depth reads, no
comparisons. But its carrier was the primorial tower: prime windows,
pairwise coprime, every channel a field, the whole product one ring
Z/N by CRT. Which of those properties does the construction USE? The
suspicion, read off the construction itself: none of them. The
invariant that keeps every read truthful is prime ABUNDANCE alone --
the n-th prime exceeds n, so the frontier window always outruns the
count -- and abundance is not a prime fact: ANY strictly increasing
supply of moduli has m_n > n. If the rider runs unchanged on
composite, pairwise NON-coprime windows, then primality, coprimality,
field structure, and the CRT glue are all certified unused, and the
statement one level below the tower is substrate-free: universality
on the element face is bought by the ALLOCATOR -- an unbounded supply
of fresh exact writable registers born at zero, each larger than the
count it must hold -- and the tower's prime staircase is one INSTANCE
of that supply, not its source.

THE MODEL (explore_frontier_rider.py's, generalized in one place).
A growing list of finite cyclic rings Z/m_1, Z/m_2, ... (the WINDOWS;
moduli from a SUPPLY parameter, repeats allowed, so registers are
keyed by window index); registers are residue tuples born at 0 in
every fresh window (state-independent); native ops componentwise
add / sub / mul / write-constant; ONE cross-window read, the global
1-bit zero-test; finite control. The meadow pseudo-inverse is kept
and instrumented -- on composite windows it is not even total on
non-units, and the rider must never call it. The CRT lift and true
integer counts appear ONLY in harness verification. The rider
protocol (INC = grow + unary transfer + re-point + add 1; guarded
DEC; JZ = zero-test) is verbatim from explore_frontier_rider.py.

THE INVARIANT, restated carrier-free: one INC = one grow, so the
value of any counter never exceeds the number of grows g; if the
supply's g-th fresh modulus exceeds g, every value lives strictly
inside the first period of every read that touches it, and the
zero-test never gets the chance to lie. The condition is m_g > g --
nothing else about the moduli is mentioned.

THE DESIGN (what each section asks).

S1  THE NON-COPRIME TOWER. Supply = the even numbers from 4 (initial
    windows 4, 6, 8; grows mint 10, 12, 14, ...). Every modulus is
    composite, every pair shares the factor 2, no window is a field,
    and the product is NOT any Z/N -- the single-ring CRT reading
    (one ring, many coprime windows) does not exist here.
    The full battery: the hand-walk with per-step register asserts,
    the halts-iff-even two-counter program (seeds 0..10, step-exact
    trace comparison against the integer reference, halting
    transfer), and a 2000-op random guarded schedule with every value
    and every JZ answer checked. Compositeness and pairwise
    non-coprimality of every modulus used are asserted mechanically.

S2  THE SUCCESSOR TOWER. Supply = 2, 3, 4, 5, ... -- the slowest
    strictly increasing integer supply, m_g = g + 4 at the g-th grow
    against a count of at most g. The same battery, plus the headroom
    ledger: the margin (pointed modulus minus true count) should sit
    at a CONSTANT floor -- the supply's fixed slack -- where the
    prime tower's margin grows with the run.

S3  THE BOUNDED CONTROL (what IS load-bearing). Supply = 4, 6, 8,
    then 8 forever (the allocator stalls at capacity 8). One counter,
    INC repeatedly: the construction must desync by wrap, and the
    first zero-test lie must land at count exactly 8 -- the capped
    modulus. The supply outrunning the count is the one property the
    construction cannot do without; this is also the harness's
    positive control (the rig detects the wrap when it occurs, so
    zero desyncs in S1/S2 are the construction's property, not
    harness blindness).

S4  THE CENSUS + THE VERDICT. Zero meadow-inverse calls across every
    tower run (asserted). Synthesis prints the minimal-carrier
    statement and the contrast: the growth machine
    (explore_growth_machine.py) also grows, but its monotone moves
    never mint a writable fresh register -- its native reads are
    write-once presence bits. The rider's universality is bought by
    ALLOCATION: growth as a supply of fresh exact writable registers
    whose capacity outruns the count.

PREDICTIONS (fixed before the run; adjudication below after it).
  PR1  The even tower runs the battery step-exact (seeds 0..10,
       halting transfers, zero desyncs, seed 8 included) and the
       2000-op random schedule exactly, every JZ answer correct --
       with every modulus composite and every pair non-coprime.
       ... CONFIRMED (S1: battery step-exact, halting transfers;
       random schedule 2000 ops exact, 793 INC / 755 DEC / 401 JZ,
       final X=11 Y=27, 793 grows, frontier modulus 1594; all 796
       moduli composite, all even).
  PR2  The successor tower runs the battery step-exact, and its
       minimum headroom over the whole battery (seeding included) is
       exactly 4 -- the supply's constant slack (derived: after g
       grows the frontier modulus is g + 4 and the count is at most
       g, met with equality at every seeding INC), against the prime
       tower's battery minimum of 6 with growing margin.
       ... CONFIRMED (S2: battery step-exact, minimum headroom 4
       exactly as derived).
  PR3  The bounded control's first zero-test lie lands at count
       exactly 8, the capped modulus (value 8 wraps to residue 0).
       ... CONFIRMED (S3: first lie at count 8).
  PR4  Zero meadow-inverse calls in every run: the census confirms
       the construction never touches the one op that composite
       windows lack (inversion of non-units).
       ... CONFIRMED (S4: MINV_CALLS = 0).

FINDINGS (entered after the run; every number below is from the
printed output; run record at the end).

1. THE CARRIER IS ALLOCATION, NOT ARITHMETIC STRUCTURE (rule;
   asserted at every executed step; S1). The identical rider protocol
   runs on the even tower -- moduli 4, 6, 8, ...: every window
   composite, every pair sharing the factor 2, no field anywhere, the
   product not any Z/N (no single-ring CRT reading of this carrier
   exists) -- step-exact on the halts-iff-even battery (seeds 0..10,
   halting transfers) and on a 2000-op random guarded schedule (793
   INC / 755 DEC / 401 JZ, every value and every JZ answer correct,
   793 grows to frontier modulus 1594, all 796 moduli mechanically
   certified composite). Primality, pairwise coprimality, field
   structure, the meadow, and the CRT glue are certified unused.

2. THE SUPPLY CONDITION IS m_g > g, WITNESSED AT CONSTANT SLACK
   (rule; S2). The successor tower -- moduli 2, 3, 4, 5, ..., the
   slowest strictly increasing integer supply -- runs the battery
   step-exact with minimum headroom exactly 4, the supply's constant
   slack (frontier g + 4 against count <= g), met at every seeding
   INC as derived. Where the prime tower's margin grows with the run
   (its battery minimum, 6, is an early dip -- value 1 at prime 7 --
   and the margin widens thereafter, since prime gaps outpace the
   count), the successor tower rides at a fixed floor: abundance is
   the whole requirement, and the thinnest supply that has it
   suffices.

3. THE SUPPLY OUTRUNNING THE COUNT IS LOAD-BEARING (rule; S3). Cap
   the supply at 8 and the first zero-test lie lands at count exactly
   8 -- the value wraps to residue 0 at the capped modulus.
   (Unboundedness is necessary, not sufficient: the working condition
   is m_g > g, which any strictly increasing integer supply meets.)
   The allocator stalling is the one failure the construction owns; this
   is also the harness's positive control (the rig detects the wrap
   when it occurs, so the zero desyncs of S1/S2 are the
   construction's property, not harness blindness).

4. THE VERDICT (rule; S1-S3 + the op census, MINV_CALLS = 0). The
   frontier rider's minimal carrier is an unbounded supply of fresh
   exact writable finite cyclic registers born at zero, each larger
   than the count it must hold (m_g > g), under componentwise ring
   ops and one global zero-test. Universality on the element face is
   bought by the ALLOCATOR; the prime staircase p_n > n is the
   tower's instance of the supply condition, not its source. The
   growth-machine contrast sharpens (explore_growth_machine.py, not
   universal): both grow, but the growth machine's monotone moves
   never mint a writable fresh register -- its native reads are
   write-once presence bits. What growth must mint for universality
   is exact writable capacity.

SCOPE + HONESTY. The invariant argument (value <= grows g < fresh
modulus m_g) is elementary and carrier-free; the simulations are
machine-checked at every executed step of every battery run, not
proved once-and-for-all over all programs -- but the protocol is
program-uniform (INC/DEC/JZ are the same op sequences regardless of
the hosting program), so the batteries exercise the general
mechanism. Universality of two exact counters rests on the classical
two-counter theorem (Minsky 1967), inherited verbatim from
explore_frontier_rider.py; this script adds no new universality
claim, it pins the existing one to its minimal carrier. What stays
tower-specific is everything ELSE the tower's carrier brings: fields
(the meadow), coprimality (the single-ring CRT reading), the prime
lens -- unused by the rider, load-bearing elsewhere.

RUN RECORD (python prime/code/explore_minimal_carrier.py, ~1 s wall
clock, trivial memory, 13 checks, all sections assert). S1 even
tower: hand-walk, battery seeds 0..10 (minimum headroom 9), random
schedule 2000 ops (793 INC / 755 DEC / 401 JZ executed; the other 51
ops were DECs whose JZ guard read zero, each verified a correct zero
answer and skipped; final X=11 Y=27, 793 grows, frontier 1594, 7907
transfer passes), 796 moduli all composite and all even (pairwise
non-coprime). S2 successor tower: hand-walk, battery seeds 0..10,
minimum headroom 4. S3 bounded control: first lie at count 8. S4
census: MINV_CALLS = 0. First run passed all sections. One post-run
harness edit: the S1 non-coprimality check strengthened from an
adjacent-pairs gcd scan to an all-moduli evenness assert (which
certifies EVERY pair non-coprime, not just the sampled ones) — all
other values unchanged, 13 checks before and after.
"""

import random

# ---------------------------------------------------------------- #
# machinery: the bare machine's native ops, keyed by window index   #
# (explore_frontier_rider.py's rig; moduli may repeat)              #
# ---------------------------------------------------------------- #

CHECKS = 0
def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1
    print(f"  [ok] {msg}")

# registers are lists of residues, index i in window Z/moduli[i]
def const(c, moduli):
    """Write an integer constant (state-independent, channel-local)."""
    return [c % m for m in moduli]

def add(x, y, moduli):
    return [(a + b) % m for a, b, m in zip(x, y, moduli)]

def sub(x, y, moduli):
    return [(a - b) % m for a, b, m in zip(x, y, moduli)]

def mul(x, y, moduli):
    return [(a * b) % m for a, b, m in zip(x, y, moduli)]

MINV_CALLS = 0
def minv(x, moduli):
    """The meadow pseudo-inverse. On composite windows it is not even
    total on non-units; the rider must never need it. The harness
    counts calls."""
    global MINV_CALLS
    MINV_CALLS += 1
    return [pow(r, -1, m) if r != 0 else 0 for r, m in zip(x, moduli)]

def born(x, m_new, c=0):
    """GROW's register extension WITHOUT the door: the new window gets
    a constant (state-independent), never the lift."""
    return x + [c % m_new]

def zero_test(x):
    """The sole cross-window read: ONE bit, the AND of per-window
    zero bits."""
    return all(r == 0 for r in x)

# harness-only (never machine code): support inspection
def support(reg):
    return [i for i, r in enumerate(reg) if r != 0]


# ---------------------------------------------------------------- #
# the rider on an arbitrary modulus supply                          #
# ---------------------------------------------------------------- #

class Rider:
    """The bare machine plus the rider protocol, carrier-parametric:
    `supply` is any iterator of moduli >= 2 (repeats allowed). The
    first three moduli are the initial windows; grow() takes the
    next. Machine code touches registers only through the native ops
    above; the harness inspects support and true counts from
    outside."""

    def __init__(self, supply, counters=("X", "Y")):
        self.supply = iter(supply)
        self.moduli = [next(self.supply) for _ in range(3)]
        self.counters = counters
        self.reg = {}
        for c in counters:
            self.reg["V_" + c] = const(0, self.moduli)
            self.reg["P_" + c] = const(0, self.moduli)
        self.reg["ONES"] = const(1, self.moduli)
        self.grow_count = 0
        self.transfer_passes = 0  # harness tally of the unary price

    def grow(self):
        """Append the next supplied window; every register born at 0;
        the fresh-window idempotent w = 1 - ONES is native; refresh
        ONES."""
        m_new = next(self.supply)
        self.moduli.append(m_new)
        for n in self.reg:
            self.reg[n] = born(self.reg[n], m_new, 0)
        w = sub(const(1, self.moduli), self.reg["ONES"], self.moduli)
        self.reg["ONES"] = const(1, self.moduli)
        self.grow_count += 1
        return w

    def inc(self, c):
        """INC: grow, transfer the pointed value to the fresh window
        (one unit per pass, stop on the pointed zero-test), re-point,
        add 1. Returns the pass count for the harness's price check."""
        w = self.grow()
        V, P = self.reg["V_" + c], self.reg["P_" + c]
        passes = 0
        while True:
            y = mul(V, P, self.moduli)      # isolate the pointed window
            if zero_test(y):
                break
            V = add(sub(V, P, self.moduli), w, self.moduli)
            passes += 1
        self.transfer_passes += passes
        self.reg["P_" + c] = w
        self.reg["V_" + c] = add(V, w, self.moduli)  # the +1
        return passes

    def dec(self, c):
        """DEC (guarded by JZ, Minsky semantics)."""
        self.reg["V_" + c] = sub(
            self.reg["V_" + c], self.reg["P_" + c], self.moduli)

    def jz(self, c):
        return zero_test(self.reg["V_" + c])

    # ---- harness-only inspection (never machine code) ----
    def value(self, c):
        V = self.reg["V_" + c]
        s = support(V)
        assert len(s) <= 1, f"counter {c} leaked support: {s}"
        return V[s[0]] if s else 0

    def pointed_index(self, c):
        s = support(self.reg["P_" + c])
        assert len(s) <= 1, f"pointer {c} widened: {s}"
        return s[0] if s else None

    def pointed_modulus(self, c):
        i = self.pointed_index(c)
        return self.moduli[i] if i is not None else None


def check_invariants(m, ref):
    """Harness: true count == pointed residue (no wrap ever happened),
    true count < pointed modulus (headroom), support clean, pointer a
    genuine one-window idempotent, ONES all-ones."""
    for c in m.counters:
        v_true = ref[c]
        mod = m.pointed_modulus(c)
        v_reg = m.value(c)
        assert v_reg == v_true, f"{c}: register {v_reg} != true {v_true}"
        if v_true > 0:
            assert mod is not None and v_true < mod, \
                f"{c}: headroom violated ({v_true} >= {mod})"
            assert support(m.reg["V_" + c]) == [m.pointed_index(c)], \
                f"{c}: value off-pointer"
        i = m.pointed_index(c)
        if i is not None:
            assert m.reg["P_" + c][i] == 1, f"{c}: pointer not idempotent"
    assert all(r == 1 for r in m.reg["ONES"]), "ONES stale"


# ---------------------------------------------------------------- #
# the reference two-counter machine (halts iff seed is even)        #
# (verbatim from explore_frontier_rider.py)                         #
# ---------------------------------------------------------------- #

PROG = {
    0: ("DECJZ", "X", 1, "HALT"),
    1: ("DECJZ", "X", 0, "LOOP"),
    "LOOP": ("INC", "Y", "LOOP"),
}

def run_reference(prog, c0, horizon):
    q, c = 0, {"X": c0, "Y": 0}
    trace = [(q, c["X"], c["Y"])]
    for _ in range(horizon):
        if q == "HALT":
            break
        ins = prog[q]
        if ins[0] == "INC":
            c[ins[1]] += 1
            q = ins[2]
        else:
            _, r, nz, z = ins
            if c[r] == 0:
                q = z
            else:
                c[r] -= 1
                q = nz
        trace.append((q, c["X"], c["Y"]))
    return trace, q

def run_rider(prog, c0, horizon, supply_factory):
    """The same program on the rider over the given supply. The
    harness co-runs the integer reference for invariant checks only;
    machine decisions (JZ) come from the rider's own zero-tests."""
    m = Rider(supply_factory())
    ref = {"X": 0, "Y": 0}
    min_headroom = None

    def note_headroom():
        nonlocal min_headroom
        for c in m.counters:
            mod = m.pointed_modulus(c)
            if mod is not None:
                h = mod - ref[c]
                if min_headroom is None or h < min_headroom:
                    min_headroom = h

    for _ in range(c0):
        m.inc("X")
        ref["X"] += 1
        check_invariants(m, ref)
        note_headroom()
    q = 0
    trace = [(q, m.value("X"), m.value("Y"))]
    for _ in range(horizon):
        if q == "HALT":
            break
        ins = prog[q]
        if ins[0] == "INC":
            m.inc(ins[1])
            ref[ins[1]] += 1
            q = ins[2]
        else:
            _, r, nz, z = ins
            if m.jz(r):
                q = z
            else:
                m.dec(r)
                ref[r] -= 1
                q = nz
        check_invariants(m, ref)
        note_headroom()
        trace.append((q, m.value("X"), m.value("Y")))
    return trace, q, min_headroom, m


# ---------------------------------------------------------------- #
# the supplies                                                      #
# ---------------------------------------------------------------- #

def even_supply():
    """4, 6, 8, 10, ... -- every modulus composite, every pair
    sharing the factor 2. No field anywhere; the product is not any
    Z/N."""
    m = 4
    while True:
        yield m
        m += 2

def successor_supply():
    """2, 3, 4, 5, ... -- the slowest strictly increasing integer
    supply."""
    m = 2
    while True:
        yield m
        m += 1

def bounded_supply(cap=8):
    """4, 6, 8, 8, 8, ... -- the allocator stalls at the cap."""
    m = 4
    while True:
        yield min(m, cap)
        m += 2


def is_composite(n):
    return n > 3 and any(n % d == 0 for d in range(2, int(n ** 0.5) + 1))


# ---------------------------------------------------------------- #
# batteries (shared by S1 and S2)                                   #
# ---------------------------------------------------------------- #

def hand_walk(supply_factory, label):
    """Cold start, one counter: INC, INC, DEC, DEC with full-register
    asserts at every step."""
    m = Rider(supply_factory())
    ref = {"X": 0, "Y": 0}
    expect = []
    for op, v in (("inc", 1), ("inc", 2), ("dec", 1), ("dec", 0)):
        getattr(m, op)("X")
        ref["X"] += 1 if op == "inc" else -1
        check_invariants(m, ref)
        expect.append((m.value("X"), m.pointed_modulus("X")))
    vals = [e[0] for e in expect]
    ok(vals == [1, 2, 1, 0], f"{label} hand-walk values {vals}")
    ok(m.jz("X"), f"{label} hand-walk JZ exact at zero")
    return expect

def battery(supply_factory, label, horizon=60):
    """Seeds 0..10 of the halts-iff-even program: step-exact traces,
    halting transfer, invariants at every step."""
    worst = None
    for c0 in range(11):
        ref_trace, ref_q = run_reference(PROG, c0, horizon)
        trace, q, hr, m = run_rider(PROG, c0, horizon, supply_factory)
        assert trace == ref_trace, f"{label} seed {c0}: trace desync"
        assert q == ref_q, f"{label} seed {c0}: halting differs"
        if hr is not None and (worst is None or hr < worst):
            worst = hr
    ok(True, f"{label} battery seeds 0..10 step-exact, halting transfers")
    return worst

def random_schedule(supply_factory, label, n_ops=2000, seed=11):
    """Random guarded INC/DEC/JZ ops on two counters against the
    integer reference; exactness and invariants after every op."""
    rng = random.Random(seed)
    m = Rider(supply_factory())
    ref = {"X": 0, "Y": 0}
    tally = {"INC": 0, "DEC": 0, "JZ": 0}
    for _ in range(n_ops):
        c = rng.choice(m.counters)
        op = rng.choice(("INC", "INC", "DEC", "DEC", "JZ"))
        if op == "INC":
            passes = m.inc(c)
            assert passes == ref[c], \
                f"{label} price desync: {passes} passes at value {ref[c]}"
            ref[c] += 1
        elif op == "DEC":
            if m.jz(c):
                assert ref[c] == 0, f"{label} JZ lied nonzero->zero"
                continue
            m.dec(c)
            ref[c] -= 1
        else:
            assert m.jz(c) == (ref[c] == 0), f"{label} JZ answer wrong"
        tally[op] += 1
        check_invariants(m, ref)
    ok(True, f"{label} random schedule {n_ops} ops exact "
             f"({tally['INC']} INC / {tally['DEC']} DEC / {tally['JZ']} JZ; "
             f"final X={ref['X']} Y={ref['Y']}; "
             f"{m.grow_count} grows, frontier {m.moduli[-1]}, "
             f"{m.transfer_passes} transfer passes)")
    return m


# ---------------------------------------------------------------- #
# sections                                                          #
# ---------------------------------------------------------------- #

def s1_non_coprime():
    print("\n== S1  THE NON-COPRIME TOWER (even moduli 4, 6, 8, ...) ==")
    hand_walk(even_supply, "even")
    worst = battery(even_supply, "even")
    ok(worst is not None and worst > 0,
       f"even battery minimum headroom {worst} > 0")
    m = random_schedule(even_supply, "even")
    mods = m.moduli
    ok(all(is_composite(x) for x in mods),
       f"all {len(mods)} moduli used are composite")
    ok(all(x % 2 == 0 for x in mods),
       "every modulus even, so every pair shares the factor 2: "
       "pairwise non-coprime")

def s2_successor():
    print("\n== S2  THE SUCCESSOR TOWER (moduli 2, 3, 4, 5, ...) ==")
    hand_walk(successor_supply, "successor")
    worst = battery(successor_supply, "successor")
    print(f"  battery minimum headroom: {worst}")
    ok(worst == 4,
       "successor battery minimum headroom = 4 (the supply's constant "
       "slack: frontier g+4 vs count <= g)")

def s3_bounded_control():
    print("\n== S3  THE BOUNDED CONTROL (supply capped at 8) ==")
    m = Rider(bounded_supply(), counters=("X",))
    true_count = 0
    first_lie = None
    for _ in range(12):
        m.inc("X")
        true_count += 1
        if m.jz("X") != (true_count == 0):
            first_lie = true_count
            break
    ok(first_lie == 8,
       f"first zero-test lie at count {first_lie} = the capped modulus "
       "(the wrap: value 8 is residue 0 mod 8)")

def s4_census_verdict():
    print("\n== S4  THE CENSUS + THE VERDICT ==")
    ok(MINV_CALLS == 0,
       "zero meadow-inverse calls across every tower run")
    print("""
  THE MINIMAL CARRIER (synthesis, if S1-S3 hold):

  The frontier rider's construction and its exactness invariant use
  only: (i) componentwise add / sub / mul and integer constants in
  each finite cyclic ring; (ii) the global 1-bit zero-test; (iii)
  born-at-zero extension by a fresh ring whose order exceeds the
  running count (m_g > g). Primality, pairwise coprimality, field
  structure, the meadow, and the CRT glue are UNUSED -- witnessed by
  running the identical protocol on carriers that lack all of them
  (S1: composite, pairwise non-coprime; the product is not any Z/N).
  The bounded control (S3) shows what is load-bearing: the supply
  must outrun the count (m_g > g) -- a capped supply wraps at its
  cap, and unboundedness alone is necessary, not sufficient.

  Substrate-free statement, one level below the tower: universality
  on the element face is bought by the ALLOCATOR -- an unbounded
  supply of fresh exact writable registers born at zero -- and the
  prime staircase p_n > n is the tower's instance of the supply
  condition m_n > n, not its source. The contrast with the
  growth machine (explore_growth_machine.py, not universal): both
  grow, but its monotone moves never mint a writable fresh register
  -- its native reads are write-once presence bits. What growth must
  mint for universality is exact writable capacity.
""")


if __name__ == "__main__":
    s1_non_coprime()
    s2_successor()
    s3_bounded_control()
    s4_census_verdict()
    print(f"\nALL SECTIONS PASS ({CHECKS} checks)")
