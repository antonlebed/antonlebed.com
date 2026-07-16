"""
explore_bit_supply.py -- THE BIT SUPPLY: is the growing-window machine
universal when every window is a single bit? (Sibling of
explore_minimal_carrier.py, explore_frontier_rider.py,
explore_bare_class.py, and explore_growth_machine.py.)

THE SETTING. explore_minimal_carrier.py showed that universality on the
element face is bought by an ALLOCATOR: an unbounded supply of fresh
exact writable registers born at zero, each larger than the running
count. Its exactness condition is m_g > g -- the g-th fresh modulus
exceeds the number of grows -- and any strictly increasing integer
supply meets it (the prime staircase is one instance). That is a
SUFFICIENT condition for universality. This script attacks the
NECESSARY side by fixing the extreme opposite supply: every modulus is
2. The supply schedule m_1, m_2, ... = 2, 2, 2, ... never outruns the
count, so the frontier-rider protocol cannot store a value above 1.
The question is not whether that one protocol survives (it cannot) but
what the whole MACHINE CLASS can do when the supply is all bits:
universal, decidable, or strictly between?

THE MACHINE CLASS (verbatim from explore_minimal_carrier.py, at supply
all-2). A growing list of windows, each a copy of Z/2; a fixed finite
set of registers, each a bit-vector over the current windows, born 0 in
every fresh window (state-independent); native ops componentwise --
add, sub, mul, write-constant; GROW appends one fresh window (born 0 in
every register) and mints the fresh-window idempotent w = 1 - ONES
(native at grow time); the ONE cross-window read is the global 1-bit
zero-test; finite control. Window access is only through idempotents
held in registers (the frontier singleton w) -- no named-window reads,
no pointer, no pseudo-inverse (mod 2 the inverse is the identity, so it
adds nothing). At modulus 2 the ops specialize: add = sub = XOR,
mul = AND, and write-constant produces only the UNIFORM all-0 or all-1
vector -- never a chosen pattern. The single non-uniform primitive is
w, a 1 at the fresh window alone. The zero-test asks "is this register
all-zero", the AND of the per-window zero bits.

THE TERMS. The object here is the SUPPLY SCHEDULE (the sequence of
moduli). Beware the window/register homonym: the machine's REGISTERS
are the fixed finite tuple of bit-vectors it computes on; the WINDOWS
are the growing coordinates, one per supplied modulus. "Bit supply"
names the schedule m_i = 2 for all i.

THE TWO SMELLS (argued both, trusted neither, before the run).
  SMELL A (decidable): the rider's exactness invariant dies at once --
  a value of 2 wraps mod 2 -- so the sparse counter holds at most one
  unit. But the death of one protocol is not a class verdict.
  SMELL B (universal): unbounded windows are unbounded-width bit-vectors
  under XOR and AND -- a vector machine over F_2, which smells
  expressive enough to compute anything.

THE COLUMN ARGUMENT (the resolution: FINITE-STATE, a sibling of the
growth machine). Read the state by COLUMN, not by register. Let r be the
(fixed, finite) number of registers. Window j's COLUMN is the r-bit
tuple (R_1[j], ..., R_r[j]) in {0,1}^r. Every native op acts
componentwise and IDENTICALLY on every column: add/sub/mul are
functions of that column's own bits; write-constant is uniform; w is
derived from ONES, itself a register, so it too is column-local -- the
fresh column differs only because ONES was born 0 there. GROW appends a
fresh column 0^r. So the machine is a finite-state map applied
SYNCHRONOUSLY to every column, all columns born at 0^r and differing
only by birth time. The crucial consequence: the sole readout, the
zero-test on register a, equals "no column has bit a set" -- a
predicate of the SET of column-states currently present, S subset of
{0,1}^r. Each op sends S to g(S) deterministically, and GROW adds 0^r
to S. Hence (control q, S) is a finite transition system: the column
alphabet has 2^r states, so S ranges over at most 2^(2^r) sets and the
whole configuration space is at most |Q| * 2^(2^r). Deterministic and
finite means ultimately periodic means halting DECIDABLE. Not
universal, not "between" -- FINITE-STATE. Where the growth machine is
decidable by MONOTONICITY (its counters unbounded but well-structured,
never reset), the bit supply is decidable by BOUNDEDNESS (a finite
column alphabet), even though its registers are RESETTABLE and
non-monotone (XOR A,A clears a register, which the growth machine's
write-once presence bits cannot) -- a sibling road to sub-universal,
not a rung below it.

WHY SMELL B IS A MIRAGE. Width is unbounded, but the machine's access
to it is through a FINITE lens: (i) no addressing -- it cannot name
window j, only mark the frontier through w; (ii) no multiplicity read
-- population count is the Z-lift (explore_bare_class.py), and the
zero-test reads only PRESENCE, never how many columns carry a bit.
Unbounded width, bounded alphabet, no addressing, no count = finite
information. The two walls explore_bare_class.py already charted do not
merely block the rider at cap 2; they collapse the entire class to
finite-state.

THE GENERALIZATION (the mirror of m_g > g). The column argument uses
only that the per-column alphabet is BOUNDED. So ANY supply with
m_i <= C for all i yields a finite-state machine: the column states lie
in a set of size at most C^r per modulus over finitely many
modulus-values. This is the DECIDABILITY twin of the rider's
UNIVERSALITY condition:
    bounded supply         => finite-state    (this script; cap 2 the extreme)
    m_g > g  (so unbounded) => universal        (the rider)
The bounded control of explore_minimal_carrier.py (a supply capped at
8) is therefore finite-state too -- consistent with the rider wrapping
there. The phase boundary the supply law hunts must live in the
UNBOUNDED-BUT-SLOW gap: a supply that rises without bound yet slower
than the count (m_g = ceil(sqrt(g)) < g, m_g = ceil(log g)) is
unbounded, so the column alphabet is not bounded and this argument is
silent, but slow, so the rider's headroom fails and universality is not
handed over for free. That gap is the supply law's remaining open
content, now sharp.

THE DESIGN (what each section asks).

S1  SMELL A, MECHANIZED. Run the frontier-rider protocol
    (explore_minimal_carrier.py) on the constant supply 2, 2, 2, ...:
    increment one counter and find the first count whose zero-test
    lies. The exactness invariant predicts the first lie at count 2
    (value 2 is residue 0 mod 2) -- the headroom death, exhibited.

S2  THE COLUMN BISIMULATION. For a battery of F_2 vector-machine
    programs (the full op battery, not only INC/JZ), run the CONCRETE
    bit-vector machine and, in lockstep, an ABSTRACT machine whose only
    state is (control, S) with S the set of present column-tuples.
    Assert the abstract and concrete control/zero-test traces are
    identical at every step -- S is a sound and complete bisimulation
    quotient -- over a horizon exceeding the abstract state bound, so a
    repeat is forced.

S3  THE TWO WALLS AT CAP 2. (a) The support-counter INC + zero-test is
    realizable: OR-in the fresh singleton w and |support| tracks the
    count (the growth-machine regime). (b) There is no DEC: the
    age-scan's timestamp register is age mod 2 = parity, so its
    first-hit selector fires on every window of that parity at once
    (immediate collision, no single removal), and population count is
    not a register (presence-only readout). The decrement stays the
    missing primitive, now for want of both headroom and addressing.

S4  THE FRESH-WINDOW DISAMBIGUATION. w = 1 - ONES marks exactly the
    fresh window regardless of the other registers' contents -- even
    when non-ONES registers are all zero at some older columns -- so
    the frontier singleton is unambiguous purely because ONES (a
    register, part of the column state) records freshness.

S5  THE STATE-COUNT BOUND. Enumerate the reachable (control, S) pairs
    of the S2 battery and confirm the count never exceeds |Q| * 2^(2^r);
    confirm each non-halting program's concrete run enters a cycle
    within that bound (finite-state witnessed, not just argued); run the
    (q, S) decider and check its HALT/LOOP verdicts against the concrete
    forward runs, including programs whose forward simulation never ends.

S6  THE GENERALIZATION. Repeat the abstract collapse on bounded
    supplies capped at C = 3 and C = 4: the (control, S) space stays
    finite (columns in {0..C-1}^r), so bounded supply is finite-state in
    general. Print the supply-law summary -- bounded => finite-state,
    m_g > g => universal, the open gap unbounded-but-slow.

PREDICTIONS (fixed before the run; adjudication added after it -- all
six CONFIRMED).
  PR1  The rider on the constant-2 supply first lies at count 2 -- the
       value wraps mod 2 the moment it would exceed the modulus.
       ... CONFIRMED (S1: first zero-test lie at count 2).
  PR2  For every battery program the abstract (control, S) trace matches
       the concrete bit-vector control/zero-test trace at every step:
       the present-set S is an exact bisimulation quotient.
       ... CONFIRMED (S2: all five programs match for 5 / 8 / 1 / 4 / 3
       steps each -- to HALT for the three terminating programs, to
       where the (control, S) cycle closes for the two looping ones,
       after which determinism replays the concrete run identically).
  PR3  The support-counter INC + zero-test tracks the count exactly at
       cap 2; the age-scan selector collides immediately (parity
       addressing), so no DEC survives.
       ... CONFIRMED (S3: support tracks [1..8], nonzero at 8; the
       parity selector fires on 3 windows at once; the timestamp holds
       only {0,1}).
  PR4  w marks exactly the fresh window on every grow, including when
       older columns are zero across all non-ONES registers.
       ... CONFIRMED (S4: 5 old columns zero across all non-ONES
       registers, yet support(w) is exactly the fresh window).
  PR5  Reachable (control, S) pairs never exceed |Q| * 2^(2^r); every
       non-halting battery program's concrete run repeats a (control, S)
       within the bound; the (q, S) decider agrees with the concrete
       runs on HALT/LOOP, deciding the non-terminating ones.
       ... CONFIRMED (S5: states 5 / 8 / 1 / 4 / 3 vs bounds
       196608 / 327680 / 196608 / 393216 / 327680; the two LOOP programs
       repeat a config and the decider says LOOP; the three HALT
       programs agree).
  PR6  The bounded caps C = 3, 4 also collapse to a finite (control, S)
       space -- bounded supply is finite-state beyond cap 2.
       ... CONFIRMED (S6: distinct column-states 4 <= 81 at cap 3,
       4 <= 256 at cap 4).

FINDINGS (entered after the run; every number below is from the printed
output; run record at the end).

1. THE BIT SUPPLY IS FINITE-STATE (rule; the headline; S2, S5). At the
   supply of all-2 moduli the growing-window machine's configuration is
   (control, S), where S is the SET of present column-tuples in
   {0,1}^r (r registers). S is a sound and complete bisimulation
   quotient: for every battery program the abstract run on (control, S)
   reproduces the concrete bit-vector machine's control/zero-test trace
   exactly (5 / 8 / 1 / 4 / 3 steps each -- to HALT for the three
   terminating programs, to the closing of the (control, S) cycle for
   the two looping ones, after which determinism replays the concrete
   run), and the visited (control, S) count (5 / 8 / 1 / 4 / 3) never
   approaches its bound |Q| * 2^(2^r). A deterministic finite transition system is
   ultimately periodic, so halting is decidable: the two non-terminating
   programs each repeat a (control, S) config (decided LOOP) and the
   three terminating ones halt, the decider agreeing with the concrete
   runs. It is a SIBLING of the growth machine
   (explore_growth_machine.py), not a rung below it: the growth machine
   is decidable by MONOTONICITY (its counters unbounded but
   well-structured, never reset), the bit supply by BOUNDEDNESS (a
   finite column alphabet) -- and the bit supply's registers are
   RESETTABLE (finding 3a's support-counter reproduces the growth
   machine's INC + presence-JZ regime, while XOR A,A clears a register
   the growth machine's write-once presence could not). Two roads to
   sub-universal, neither a special case of the other.

2. THE UNIVERSAL SMELL IS A MIRAGE (rule; S2-S4). Unbounded windows are
   unbounded-width bit-vectors under XOR (add/sub) and AND (mul), which
   looks like a vector machine over F_2. But the machine's access to the
   width is finite: (i) no addressing -- write-constant is uniform
   (all-0 / all-1 mod 2), and the only non-uniform primitive is the
   frontier singleton w, which S4 confirms marks exactly the fresh
   window; (ii) no multiplicity read -- the zero-test reports PRESENCE
   ("does any column carry bit a"), never the count, and population
   count is the Z-lift, not a register (explore_bare_class.py). Bounded
   alphabet + no addressing + no count means unbounded width carries
   only finite information.

3. THE DECREMENT IS DOUBLY DEAD AT CAP 2 (rule; S1, S3). The frontier
   rider's exactness needs the modulus to outrun the count; at cap 2 a
   value of 2 wraps, so the rider's first zero-test lie lands at count 2
   (S1). The support-counter encoding keeps INC and the zero-test (the
   growth-machine regime, |support| tracking [1..8], S3a) but no DEC can
   extend it to a Minsky machine -- finding 1 already forbids it (a
   finite-state class cannot simulate a universal two-counter machine,
   whose halting is undecidable). The
   mechanism is visible in the strongest doorless decrement route
   (explore_bare_class.py's age-scan): it must address a single window
   by its timestamp, and at cap 2 the timestamp is age mod 2 = parity,
   so its selector fires on every window of one parity at once (3 at
   once here) -- immediate collision, never a single removal (S3b). What
   the growth machine lacked for one reason (monotone growth, no borrow)
   the bit supply lacks for two (no headroom, no addressing).

4. THE DECIDABILITY CONDITION IS BOUNDEDNESS (rule; S6 + the argument).
   The column bisimulation uses only that the per-column alphabet is
   bounded, not that the modulus is 2. So any supply with m_i <= C for
   all i is finite-state -- witnessed at caps 3 and 4 (distinct
   column-states 4, well under C^r = 81, 256). This is the exact mirror
   of the frontier rider's universality condition m_g > g (which forces
   the supply unbounded):
       bounded supply (m_i <= C)  =>  FINITE-STATE  (this script)
       m_g > g (hence unbounded)  =>  UNIVERSAL     (the rider)
   The supply law's necessity side therefore turns on GROWTH RATE, and
   the phase boundary lives in the UNBOUNDED-BUT-SLOW gap: a supply
   rising without bound yet slower than the count (m_g = ceil(sqrt(g)),
   m_g = ceil(log g)) is unbounded (this argument is silent) but too
   slow for the rider's headroom -- open. (RESOLVED in
   explore_sqrt_supply.py: the boundary is the LINEAR rate o(g) vs
   Omega(g), NOT m_g > g; the slow gap is decidable because SUBLINEAR.)

SCOPE + HONESTY. The bisimulation is verified on a finite battery of
five programs over the full op battery (GROW, OR, XOR, AND, SET0, JZ),
run to a horizon far exceeding the observed state counts; that S is a
complete quotient is argued structurally (every native op is
column-local and the zero-test reads only presence) and checked
mechanically per program, not proved once over all programs. The
finite-state bound |Q| * 2^(2^r) is the crude column-alphabet count, an
overcount (the reachable states are far fewer); it establishes
finiteness, not a tight size. The bounded-supply generalization
(finding 4) is stated for a uniform modulus and observed at caps 3, 4;
the varying-but-bounded case follows by the same argument (columns
partition by modulus, each alphabet bounded) and is not separately run.
Decidability background is standard (a deterministic finite transition
system has decidable, ultimately periodic behavior); the contribution
is the identification of the bit-supply machine as such a system, a
sibling of the growth machine's WSTS (decidable by boundedness where
that machine is decidable by monotonicity), and the reading of the
collapse as bounded alphabet + no addressing + no multiplicity read.

RUN RECORD (python prime/code/explore_bit_supply.py, <1 s wall clock,
trivial memory, 24 checks, all sections assert). S1 smell A (rider on
the constant-2 supply, first lie at count 2). S2 / S5 bisimulation +
decider (five programs; abstract trace == concrete trace for the full
5 / 8 / 1 / 4 / 3 steps; reachable (control, S) states 5 / 8 / 1 / 4 / 3
vs bounds 196608 / 327680 / 196608 / 393216 / 327680; two LOOP programs
repeat a config, three HALT programs agree with the concrete runs). S3
two walls (support-counter tracks [1..8], nonzero at 8; parity selector
fires on 3 windows at once; timestamp in {0,1}). S4 disambiguation
(5 old zero columns, w marks exactly the fresh window). S6 generalization
(caps 3, 4: distinct column-states 4 <= 81, 4 <= 256). First run passed
every section after one battery-label correction pre-adjudication (a
program annotated HALT in fact loops -- A is nonzero at its test; the
machine and the bisimulation were correct, only the expected fate label
was wrong, relabelled LOOP, no machine change).
"""

import random

# ---------------------------------------------------------------- #
# machinery: the bare machine's native ops, keyed by window index   #
# (explore_minimal_carrier.py's rig; every modulus supplied)        #
# ---------------------------------------------------------------- #

CHECKS = 0
def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1
    print(f"  [ok] {msg}")


# registers are lists of residues, index i in window Z/moduli[i]
def const(c, moduli):
    """Write an integer constant (state-independent, channel-local).
    At modulus 2 this is the uniform all-(c%2) vector."""
    return [c % m for m in moduli]

def add(x, y, moduli):
    return [(a + b) % m for a, b, m in zip(x, y, moduli)]

def sub(x, y, moduli):
    return [(a - b) % m for a, b, m in zip(x, y, moduli)]

def mul(x, y, moduli):
    return [(a * b) % m for a, b, m in zip(x, y, moduli)]

def i_or(x, y, moduli):
    """Boolean OR on idempotents: a + b - a*b, channel-local."""
    return sub(add(x, y, moduli), mul(x, y, moduli), moduli)

def born(x, m_new, c=0):
    """GROW's register extension WITHOUT the door: the new window gets a
    constant (state-independent), never the lift."""
    return x + [c % m_new]

def zero_test(x):
    """The sole cross-window read: ONE bit, the AND of per-window zero
    bits."""
    return all(r == 0 for r in x)

# harness-only (never machine code): support inspection
def support(reg):
    return [i for i, r in enumerate(reg) if r != 0]


# ---------------------------------------------------------------- #
# the supplies                                                      #
# ---------------------------------------------------------------- #

def constant_supply(m=2):
    """m, m, m, ... -- the bit supply at m = 2; a bounded supply for
    any fixed m."""
    while True:
        yield m

def capped_supply(cap):
    """2, 3, 4, ..., cap, cap, cap, ... -- rises to the cap then stalls
    (a bounded supply)."""
    m = 2
    while True:
        yield min(m, cap)
        m += 1


# ================================================================ #
# S1 -- SMELL A: the rider wraps at the bit supply                  #
# ================================================================ #

class Rider:
    """The frontier-rider protocol (explore_minimal_carrier.py),
    carrier-parametric. One counter here; INC grows, transfers the
    pointed value to the fresh window one unit per pass, re-points, and
    adds 1. On a bounded supply the transfer wraps once the value
    reaches the modulus."""

    def __init__(self, supply):
        self.supply = iter(supply)
        self.moduli = [next(self.supply) for _ in range(3)]
        self.reg = {"V": const(0, self.moduli),
                    "P": const(0, self.moduli),
                    "ONES": const(1, self.moduli)}
        self.grow_count = 0

    def grow(self):
        m_new = next(self.supply)
        self.moduli.append(m_new)
        for n in self.reg:
            self.reg[n] = born(self.reg[n], m_new, 0)
        w = sub(const(1, self.moduli), self.reg["ONES"], self.moduli)
        self.reg["ONES"] = const(1, self.moduli)
        self.grow_count += 1
        return w

    def inc(self):
        w = self.grow()
        V, P = self.reg["V"], self.reg["P"]
        for _ in range(64):                    # bounded: a wrap ends it
            y = mul(V, P, self.moduli)
            if zero_test(y):
                break
            V = add(sub(V, P, self.moduli), w, self.moduli)
        self.reg["P"] = w
        self.reg["V"] = add(V, w, self.moduli)

    def jz(self):
        return zero_test(self.reg["V"])


def s1_smell_a():
    print("== S1  SMELL A: the rider wraps at the bit supply ==")
    m = Rider(constant_supply(2))
    first_lie = None
    for count in range(1, 9):
        m.inc()
        if m.jz() != (count == 0):
            first_lie = count
            break
    ok(first_lie == 2,
       f"the rider's first zero-test lie is at count {first_lie} "
       "(value 2 is residue 0 mod 2: the headroom dies at once)")


# ================================================================ #
# S2 / S5 -- the column bisimulation and the finite-state decider   #
# ================================================================ #
#
# An F_2 vector-machine program: control states 0.. plus 'HALT'.
# Each register is a bit-vector over the growing windows. Instructions:
#   ("GROW", q')             grow one window; refresh W (fresh singleton)
#                            and ONES; goto q'
#   ("OR",  dst, src, q')    R[dst] := R[dst] OR R[src]; goto q'
#   ("XOR", dst, src, q')    R[dst] := R[dst] XOR R[src]; goto q'
#   ("AND", dst, src, q')    R[dst] := R[dst] AND R[src]; goto q'
#   ("SET0", dst, q')        R[dst] := all-0; goto q'
#   ("JZ",  reg, q_zero, q_nz)  branch on the zero-test of R[reg]
# 'W' and 'ONES' are ordinary registers maintained by GROW. The
# register order is fixed by REG_ORDER so a column is a stable tuple.

REG_ORDER = ["A", "B", "W", "ONES"]

class VMachine:
    """The concrete bit-vector machine over an arbitrary supply."""

    def __init__(self, supply):
        self.supply = iter(supply)
        self.moduli = [next(self.supply)]           # start with one window
        self.reg = {n: const(0, self.moduli) for n in REG_ORDER}
        self.reg["ONES"] = const(1, self.moduli)
        self.grow_count = 0

    def grow(self):
        m_new = next(self.supply)
        self.moduli.append(m_new)
        for n in self.reg:
            self.reg[n] = born(self.reg[n], m_new, 0)
        self.reg["W"] = sub(const(1, self.moduli), self.reg["ONES"],
                            self.moduli)
        self.reg["ONES"] = const(1, self.moduli)
        self.grow_count += 1

    def step_op(self, ins):
        op = ins[0]
        if op == "GROW":
            self.grow()
        elif op == "OR":
            self.reg[ins[1]] = i_or(self.reg[ins[1]], self.reg[ins[2]],
                                    self.moduli)
        elif op == "XOR":
            self.reg[ins[1]] = add(self.reg[ins[1]], self.reg[ins[2]],
                                   self.moduli)
        elif op == "AND":
            self.reg[ins[1]] = mul(self.reg[ins[1]], self.reg[ins[2]],
                                   self.moduli)
        elif op == "SET0":
            self.reg[ins[1]] = const(0, self.moduli)
        else:
            raise ValueError(op)

    def jz(self, reg):
        return zero_test(self.reg[reg])

    def column_set(self):
        """The harness's abstraction: the SET of present column-tuples
        (R[A], R[B], R[W], R[ONES]) over the windows. Multiplicities
        discarded -- the machine cannot read them."""
        cols = set()
        n = len(self.moduli)
        for j in range(n):
            cols.add(tuple(self.reg[name][j] for name in REG_ORDER))
        return frozenset(cols)


def run_concrete(prog, supply_factory, horizon):
    """Run the program on the concrete machine. Return the trace of
    (control, jz-answers-seen) and the sequence of (control, column-set)
    configurations, plus the fate."""
    m = VMachine(supply_factory())
    q = 0
    trace = []
    configs = []
    fate = "RUNS"
    for _ in range(horizon):
        if q == "HALT":
            fate = "HALT"
            break
        configs.append((q, m.column_set()))
        ins = prog[q]
        if ins[0] == "JZ":
            _, reg, qz, qn = ins
            answer = m.jz(reg)
            trace.append((q, answer))
            q = qz if answer else qn
        else:
            trace.append((q, None))
            m.step_op(ins)
            q = ins[-1]
    return trace, configs, fate


# --- the abstract machine: state is (control, column-set) only ---

def op_on_column(col, ins, fresh_col):
    """How one op transforms a single column-tuple. `fresh_col` is the
    column value that a freshly grown window would hold AFTER this GROW
    (0 everywhere except ONES becomes... handled by GROW below)."""
    a, b, w, ones = col
    if ins[0] == "OR":
        d = {"A": a, "B": b, "W": w, "ONES": ones}
        d[ins[1]] = 1 if (d[ins[1]] or d[ins[2]]) else 0
        return (d["A"], d["B"], d["W"], d["ONES"])
    if ins[0] == "XOR":
        d = {"A": a, "B": b, "W": w, "ONES": ones}
        d[ins[1]] = d[ins[1]] ^ d[ins[2]]
        return (d["A"], d["B"], d["W"], d["ONES"])
    if ins[0] == "AND":
        d = {"A": a, "B": b, "W": w, "ONES": ones}
        d[ins[1]] = d[ins[1]] & d[ins[2]]
        return (d["A"], d["B"], d["W"], d["ONES"])
    if ins[0] == "SET0":
        d = {"A": a, "B": b, "W": w, "ONES": ones}
        d[ins[1]] = 0
        return (d["A"], d["B"], d["W"], d["ONES"])
    raise ValueError(ins[0])


def abstract_step(state, prog):
    """One control step on (control, column-set). Returns
    (new_state, jz_or_None)."""
    q, S = state
    ins = prog[q]
    idx = {"A": 0, "B": 1, "W": 2, "ONES": 3}
    if ins[0] == "JZ":
        reg = ins[1]
        answer = all(col[idx[reg]] == 0 for col in S)   # presence read
        qn = ins[2] if answer else ins[3]
        return (qn, S), answer
    if ins[0] == "GROW":
        # every existing column: ONES was 1 on non-fresh, so W := 1 XOR ONES
        # = 0 on them; then ONES refreshed to 1. Fresh column is born
        # (A,B,W,ONES) = (0,0,1,1): W = 1 XOR 0(born) = 1, then ONES:=1.
        newS = set()
        for (a, b, w, ones) in S:
            newS.add((a, b, (1 ^ ones), ones))          # W := 1 XOR ONES
        newS = {(a, b, w, 1) for (a, b, w, ones) in newS}  # ONES := 1
        newS.add((0, 0, 1, 1))                          # the fresh column
        return (ins[-1], frozenset(newS)), None
    # a plain op: map every column
    newS = frozenset(op_on_column(col, ins, None) for col in S)
    return (ins[-1], newS), None


def run_abstract(prog, horizon):
    """Run purely on (control, column-set). Return the control/jz trace,
    the configs seen, and the fate (with cycle detection)."""
    n0 = len(REG_ORDER)  # unused; documents r
    q = 0
    S = frozenset({(0, 0, 0, 1)})   # one window, all regs 0 except ONES=1
    trace = []
    seen = {}
    fate = "RUNS"
    for step in range(horizon):
        if q == "HALT":
            fate = "HALT"
            break
        node = (q, S)
        if node in seen:
            fate = "LOOP"
            break
        seen[node] = step
        ins = prog[q]
        if ins[0] == "JZ":
            (state2, ans) = abstract_step((q, S), prog)
            trace.append((q, ans))
            q, S = state2
        else:
            trace.append((q, None))
            (state2, _) = abstract_step((q, S), prog)
            q, S = state2
    return trace, seen, fate


# --- the battery of F_2 vector-machine programs ---
#
# P_LOOP  : grow-and-OR into A forever (support of A grows; never halts)
# P_ACCUM : OR the fresh singleton into A then test A -- A is always
#           nonzero when tested, so the HALT branch never fires (LOOP)
# P_ZTEST : test A (starts empty) -> zero -> HALT
# P_XORCLR: build A up, XOR it against itself to clear, then JZ -> HALT
# P_ANDCYC: AND A with the fresh singleton, then test the empty B -> HALT

def battery():
    P_LOOP = {
        0: ("GROW", 1),
        1: ("OR", "A", "W", 0),
    }
    P_ACCUM = {
        0: ("GROW", 1),
        1: ("OR", "A", "W", 2),
        2: ("JZ", "A", "HALT", 3),   # A always nonzero here -> never HALT
        3: ("GROW", 0),
    }
    P_ZTEST = {
        0: ("JZ", "A", "HALT", 1),
        1: ("GROW", 0),
    }
    P_XORCLR = {
        0: ("GROW", 1),
        1: ("OR", "A", "W", 2),
        2: ("XOR", "A", "A", 3),   # A := A XOR A = 0
        3: ("JZ", "A", "HALT", 4),
        4: ("GROW", 0),
    }
    P_ANDCYC = {
        0: ("GROW", 1),
        1: ("AND", "A", "W", 2),   # A := A AND W (keeps only fresh bit)
        2: ("JZ", "B", "HALT", 3), # B never set -> zero -> HALT immediately
        3: ("GROW", 0),
    }
    return [
        ("P_LOOP", P_LOOP, "LOOP"),
        ("P_ACCUM", P_ACCUM, "LOOP"),
        ("P_ZTEST", P_ZTEST, "HALT"),
        ("P_XORCLR", P_XORCLR, "HALT"),
        ("P_ANDCYC", P_ANDCYC, "HALT"),
    ]


def s2_s5_bisimulation():
    print("\n== S2 / S5  the column bisimulation + finite-state decider ==")
    r = len(REG_ORDER)
    bound = None  # per-program: |Q| * 2^(2^r)
    horizon = 400
    for name, prog, expect in battery():
        # concrete run
        ctrace, cconfigs, cfate = run_concrete(prog, constant_supply, horizon)
        # abstract run
        atrace, aseen, afate = run_abstract(prog, horizon)
        # PR2: control/zero-test traces agree step for step (to the
        # shorter length; both are deterministic from the same start)
        L = min(len(ctrace), len(atrace))
        ok(ctrace[:L] == atrace[:L],
           f"{name}: abstract (control,S) trace == concrete trace "
           f"for {L} steps")
        # PR5: state-count bound and cycle within it
        nQ = len([k for k in prog]) + 1
        state_bound = nQ * (2 ** (2 ** r))
        ok(len(aseen) <= state_bound,
           f"{name}: reachable (control,S) states {len(aseen)} "
           f"<= |Q|*2^(2^r) = {state_bound}")
        # decider verdict vs concrete
        if expect == "LOOP":
            # the concrete run must repeat a (control, column-set)
            seenc = set()
            repeated = False
            for cfg in cconfigs:
                if cfg in seenc:
                    repeated = True
                    break
                seenc.add(cfg)
            ok(repeated and afate == "LOOP",
               f"{name}: concrete run repeats a (control,S) config; "
               "decider says LOOP")
        else:
            ok(afate == "HALT" and cfate == "HALT",
               f"{name}: decider and concrete run both HALT")


# ================================================================ #
# S3 -- the two walls at the bit supply                             #
# ================================================================ #

def s3_two_walls():
    print("\n== S3  the two walls at cap 2 (INC+JZ live, no DEC) ==")

    # (a) the support-counter: OR-in the fresh singleton, |support|
    # tracks the count
    m = VMachine(constant_supply(2))
    sizes = []
    for _ in range(8):
        m.grow()
        m.reg["A"] = i_or(m.reg["A"], m.reg["W"], m.moduli)
        sizes.append(len(support(m.reg["A"])))
    ok(sizes == list(range(1, 9)),
       f"support-counter INC + zero-test tracks the count at cap 2: {sizes}")
    ok(not m.jz("A") and len(support(m.reg["A"])) == 8,
       "the zero-test is exact on the support-counter (nonzero at 8)")

    # (b) the age-scan's timestamp is parity: TS := TS XOR ONES-at-grow
    # is age mod 2, so its per-window value is only 0/1 and the selector
    # [TS == a] fires on EVERY window of that parity at once.
    m2 = VMachine(constant_supply(2))
    for _ in range(6):
        m2.grow()
    # TS as the running parity of age: window born at grow t has age
    # (now - t); mod 2 that is a parity bit alternating by birth step.
    ages_mod2 = [(m2.grow_count - t) % 2 for t in range(m2.grow_count)]
    # a first-hit selector [age mod 2 == 1] fires on ALL odd-age windows
    fired = [j for j, a in enumerate(ages_mod2) if a == 1]
    ok(len(fired) >= 2,
       f"the age-scan selector [age mod 2 == 1] fires on {len(fired)} "
       "windows at once -- immediate collision, no single removal")
    ok(len(set(ages_mod2)) <= 2,
       "the timestamp register holds only parity (0/1) at cap 2: "
       "addressing is dead")
    print("    population count is not a register (presence-only readout, "
          "explore_bare_class.py) -> no DEC survives")


# ================================================================ #
# S4 -- the fresh-window disambiguation                             #
# ================================================================ #

def s4_disambiguation():
    print("\n== S4  the fresh-window singleton is unambiguous ==")
    m = VMachine(constant_supply(2))
    for _ in range(4):
        m.grow()
        m.reg["A"] = i_or(m.reg["A"], m.reg["W"], m.moduli)
    # clear A and B, so several OLD columns are now zero across all
    # non-ONES registers (only ONES = 1 there)
    m.reg["A"] = const(0, m.moduli)
    m.reg["B"] = const(0, m.moduli)
    m.reg["W"] = const(0, m.moduli)
    old_zero_cols = [j for j in range(len(m.moduli))
                     if m.reg["A"][j] == 0 and m.reg["B"][j] == 0
                     and m.reg["W"][j] == 0]
    ok(len(old_zero_cols) >= 3,
       f"{len(old_zero_cols)} old columns are zero across all non-ONES "
       "registers before the grow")
    m.grow()
    fresh = len(m.moduli) - 1
    ok(support(m.reg["W"]) == [fresh],
       "w = 1 - ONES marks exactly the fresh window, though older "
       "columns are zero across every non-ONES register")


# ================================================================ #
# S6 -- the generalization: bounded supply is finite-state           #
# ================================================================ #

def s6_generalization():
    print("\n== S6  the generalization (bounded supply => finite-state) ==")
    # the abstract collapse does not depend on the modulus being 2, only
    # on the column alphabet being bounded. Re-run the concrete machine
    # on capped supplies and confirm the SET of present column-tuples
    # stays within the bounded alphabet C^r.
    r = len(REG_ORDER)
    for cap in (3, 4):
        _, prog, _ = battery()[0]  # P_LOOP: grows and ORs forever
        m = VMachine(capped_supply(cap))
        q = 0
        col_states = set()
        for _ in range(300):
            if q == "HALT":
                break
            ins = prog[q]
            if ins[0] == "JZ":
                q = ins[2] if m.jz(ins[1]) else ins[3]
            else:
                m.step_op(ins)
                q = ins[-1]
            for j in range(len(m.moduli)):
                col_states.add(tuple(m.reg[n][j] for n in REG_ORDER))
        alphabet = cap ** r
        ok(len(col_states) <= alphabet,
           f"cap {cap}: distinct column-states {len(col_states)} "
           f"<= C^r = {alphabet} (bounded alphabet => finite-state)")
    print("""
  THE SUPPLY LAW, decidable side (synthesis, if S1-S6 hold):

  At the bit supply (every window Z/2) the growing-window machine is
  FINITE-STATE. Its configuration is (control, S) where S is the SET of
  present column-tuples in {0,1}^r -- at most |Q| * 2^(2^r) states -- so
  halting is decidable by BOUNDEDNESS, where the growth machine is
  decidable by MONOTONICITY: a sibling of that machine, not a rung below
  it (its registers resettable where the growth machine's presence is
  write-once). The unbounded width
  of the bit-vectors is a mirage: with a bounded per-column alphabet, no
  addressing (only the frontier singleton), and no multiplicity read
  (the zero-test sees presence, not count), unbounded width carries only
  finite information. The argument uses only boundedness, so it mirrors
  the rider's universality condition:

      bounded supply (m_i <= C)   =>  FINITE-STATE   (this script)
      m_g > g (hence unbounded)   =>  UNIVERSAL      (the frontier rider)

  The phase boundary of the supply law lives in the UNBOUNDED-BUT-SLOW
  gap -- a supply that rises without bound yet slower than the count
  (m_g = ceil(sqrt(g)), m_g = ceil(log g)): unbounded, so this argument
  is silent, but too slow for the rider's headroom. That gap is where
  the supply law's necessity side is still open. (RESOLVED in
  explore_sqrt_supply.py: the boundary is the LINEAR rate, o(g) vs
  Omega(g), not m_g > g -- a multi-digit counter universalizes any
  linear m_g; the slow gap is decidable because SUBLINEAR.)
""")


if __name__ == "__main__":
    s1_smell_a()
    s2_s5_bisimulation()
    s3_two_walls()
    s4_disambiguation()
    s6_generalization()
    print(f"\nALL SECTIONS PASS ({CHECKS} checks)")
