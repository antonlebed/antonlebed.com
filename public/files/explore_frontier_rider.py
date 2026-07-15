"""
explore_frontier_rider.py -- THE FRONTIER RIDER: can a sparse counter
riding the growth frontier assemble the borrow bare? (Sibling of
explore_bare_class.py -- the rig here is that script's, trimmed to
the ops the rider needs; the meadow inverse is kept and instrumented
to certify it is never called. Related: explore_ecc_borrow.py,
explore_growth_machine.py, explore_archimedean_dial.py.)

THE QUESTION. explore_bare_class.py killed the support-counter
construction and left the bare element class hanging on one candidate
lemma: "periodic reads cannot assemble an aperiodic borrow" -- a
finite-control machine over growing windows whose only cross-window
reads are 1-bit zero-tests of channel-local composites would have
decidable halting. This script attacks the lemma's counterexample
face head-on: build a working, exact, unbounded counter -- a borrow
paired with a truthful zero-test -- out of periodic reads alone, with
no base extension, no depth, no named-window residue reads.

THE REVERSAL (the read-stream reading). A periodic read of period p
does not lie below its period: it lies only when the value it reads
CROSSES p (the wrap). "Periodic" and "wrapping" are different
predicates, and the lemma conflates them. What a counter needs is not
an aperiodic read -- it is a supply of periods that outruns its own
value. Growth supplies exactly that: the n-th prime exceeds n, so a
machine that grows one window per increment always has a frontier
prime strictly larger than any count it can have accumulated. The
aperiodicity hunted for is not needed; prime ABUNDANCE is enough.

THE CONSTRUCTION (THE FRONTIER RIDER). Store the counter value v as a
residue in ONE pointed window and keep the register LITERALLY ZERO
everywhere else; ride the pointer forward along the growth frontier.
Every ingredient is certified native by explore_bare_class.py:
  - the fresh-window idempotent w = 1 - ONES (its finding 2),
  - channel-local add/sub/mul and write-constant,
  - the global 1-bit zero-test,
  - born-at-0 growth (the no-door clause itself).
Per counter, two registers: V (the value: v at the pointed window, 0
elsewhere) and P (the pointed window's idempotent). The ops:
  INC: GROW (fresh prime q; everything born 0); w := 1 - ONES;
       refresh ONES; TRANSFER: loop { y := V*P; if zero-test(y) stop;
       V := V - P + w } -- one unit moves per pass, the pointed
       residue counts down to 0 exactly while the fresh residue counts
       up, both below their primes; then P := w; V := V + P.
  DEC (guarded): V := V - P.
  JZ: zero-test(V) -- exact, because V's only support is the pointed
       window and the value there is below the prime: ring zero iff
       integer zero. The zero-test never gets the chance to lie.
THE INVARIANT that makes every read truthful: v never exceeds the
number of INCs, one INC = one grow, and after g grows the frontier
prime is the (3+g)-th prime >= g + 4 > v. The value lives strictly
inside the first period of every read that ever touches it.

THE KEY REVERSAL ON BORN-AT-0. The no-door clause -- windows born at
a constant, never the lift -- was the codeword machine's freeze bug
(explore_ecc_borrow.py: a window born offset makes the zero-test lie
false-nonzero). The sparse encoding turns the same clause into FREE
SYNC: the intended content of every unpointed window IS 0, so a fresh
window is born already correct. "A reset re-syncs at zero alone" is a
limitation for dense codewords and an affordance for sparse ones.

WHY THE KNOWN WALLS DO NOT APPLY (the pre-code hand-attack):
  - The walking pointer needed the prime successor (deleted,
    archimedean). The rider's pointer never walks the interior: it
    jumps only to the FRESH window, and the fresh idempotent is
    native at grow time.
  - Popcount needed the Z-lift. The rider stores a residue, not a
    support size; no cross-window sum is ever formed.
  - Static masks address only the program text's primes. The pointer
    idempotent is a REGISTER, carried forward, not a constant.
  - The age-scan died at the wrap. The rider's invariant keeps every
    value strictly below its window's prime; the first period is the
    only period ever read.
  - The keystone lemma (state-independent base extension is not
    ring-computable) is NOT contradicted: the rider never rebuilds a
    lift residue in a fresh window -- it re-encodes the value in
    UNARY TIME through the zero-test, one unit per pass. What the
    base-extension door sells is O(1) sync; the rider buys the same
    exactness for unary time. If the construction runs, the door's
    content was efficiency, never possibility.

THE MODEL (identical to explore_bare_class.py's, restated). Growing
window list from [2, 3, 5]; registers are residue tuples born at 0 in
every fresh window (state-independent); native ops channel-local;
cross-window reads: the 1-bit zero-test only (the rider uses no
named-window residue reads); finite control -- every unbounded
quantity lives in a register. The CRT lift and true integer counts
appear ONLY in harness verification; machine code never touches them.

THE DESIGN (what each section asks).

S1  THE HAND-WALK MECHANIZED. Cold start, one counter: INC, INC,
    DEC, DEC with full-register asserts at every step (pointer lands
    on 7 then 11, value tracks 1, 2, 1, 0, support never leaks off
    the pointed window, JZ exact at both ends).

S2  THE WRAP CONTROL (the read IS periodic; the rider just never
    crosses it). A fixed-pointer counter -- same rig, no migration --
    increments at window 7: the zero-test must read FALSE at counts
    1..6 and lie TRUE at count 7 (the read's period exhibited
    mechanically). The rider on the same 7-INC schedule keeps its
    value exact with positive headroom. This is also the harness
    control: the rig detects a wrap when one occurs, so zero desyncs
    downstream are the construction's property, not the harness's
    blindness.

S3  THE MINSKY BATTERY. The halts-iff-even two-counter program of
    explore_bare_class.py, seeds 0..10, run on the rider bare --
    step-exact trace comparison against the integer reference within
    the horizon, halting transfer (even seeds halt at the same step;
    odd seeds still running at the horizon on both sides), and the
    invariant (true count < pointed prime, support clean) asserted at
    every step. Seed 8 -- the seed that killed the age-scan -- is in
    range.

S4  THE RANDOM SCHEDULE. 2000 random guarded INC/DEC/JZ ops on two
    counters against the integer reference, exactness and invariants
    asserted after every op, every JZ answer compared.

S5  THE PRICE. The transfer loop's pass count per INC must equal the
    value carried (unary re-encoding, priced exactly); the op census
    must show ZERO meadow-inverse calls and zero named-window reads
    -- the rider uses a strictly smaller battery than the bare model
    allows.

S6  THE VERDICT. Synthesis prints: what the construction, if S1-S5
    hold, does to the candidate lemma and to the class question
    (two exact counters + exact zero-test = a two-counter Minsky
    machine, universal; Minsky 1967).

PREDICTIONS (fixed before the run; adjudication below after it).
  PR1  The rider runs halts-iff-even seeds 0..10 step-exact against
       the reference within the horizon; halting transfers; ZERO
       desyncs -- including seed 8, the age-scan's killer.
       ... CONFIRMED (S3: eleven seeds step-exact, even seeds HALT,
       odd seeds running at horizon 60 on both sides).
  PR2  The true integer count stays strictly below the pointed prime
       at every step of every run (headroom always positive; the
       margin grows, since primes outrun the count).
       ... CONFIRMED (S3: minimum headroom over the battery = 6 > 0,
       seeding steps included -- the dip is value 1 at prime 7;
       invariants asserted at every step of S3 and S4).
  PR3  The wrap control lies TRUE at exactly count 7 on window 7 (the
       read is periodic), while the rider on the same schedule stays
       exact: periodicity of the read and wrapping of the value come
       apart mechanically.
       ... CONFIRMED (S2: counts 1..6 read nonzero, count 7 reads
       zero on the fixed pointer; the rider reads 7 exactly at
       pointed prime 29, headroom 22).
  PR4  The 2000-op random schedule tracks the integer reference
       exactly at every op, every JZ answer correct.
       ... CONFIRMED (S4: 896 INC / 848 DEC / 256 JZ, final X=4 Y=44,
       896 windows grown, frontier prime 6991, zero mismatches).
  PR5  The op census: zero meadow-inverse calls, zero named-window
       residue reads, and transfer passes per INC exactly equal to
       the value carried (the unary price).
       ... CONFIRMED (S5: MINV_CALLS = 0, no named-read op exists in
       the machine class; S4: passes == value carried at all 896
       INCs, 14990 passes total).

FINDINGS (entered after the run; every number below is from the
printed output; run record at the end).

1. THE RIDER IS EXACT (rule; asserted at every executed step; S1-S4).
   The sparse counter -- value as a residue in one pointed window,
   literal 0 elsewhere, pointer re-seated on the growth frontier at
   every INC -- tracks the true integer count exactly: the hand-walk
   (pointer e_7 then e_11, values 1, 2, 1, 0, the old window emptied
   exactly, support never leaking), the halts-iff-even battery seeds
   0..10 step-exact with halting transferring (seed 8, the seed that
   killed the age-scan of explore_bare_class.py, runs clean), and a
   2000-op random guarded schedule with every value and every JZ
   answer correct.

2. THE READ IS PERIODIC AND NEVER GETS TO LIE (rule; S2, S3). The
   zero-test at window 7 lies TRUE at exactly count 7 on a fixed
   pointer -- the read's period, exhibited mechanically -- while the
   rider on the same schedule holds value 7 at pointed prime 29
   (headroom 22) and reads correctly. Over the whole battery --
   seeding steps included -- the minimum headroom is 6 (value 1 at
   prime 7): the invariant (one INC = one grow, and the (3+g)-th
   prime >= g + 4 > any accumulated count) keeps every value
   strictly inside the first period of every read that touches it.
   Periodicity of the read and wrapping of the value come apart: a
   periodic read is EXACT below its period, and growth mints periods
   faster than the machine can count.

3. THE PRICE IS UNARY TIME (rule; S4). Transfer passes per INC equal
   the value carried, at all 896 INCs (14990 passes total): the rider
   re-encodes its counter one unit per pass through the zero-test.
   The base-extension door (explore_ecc_borrow.py) sells the same
   exactness in O(1) per step; the keystone lemma is untouched (no
   lift residue is ever rebuilt -- nothing state-independent computes
   the extension; the rider pays TIME instead). The door's content is
   EFFICIENCY, not possibility.

4. THE BATTERY IS MINIMAL (rule; S5). Zero meadow-inverse calls, zero
   named-window residue reads: the construction uses add, sub, mul,
   write-constant, the 1-bit zero-test, and born-at-0 growth alone --
   strictly less than the bare model allows. Born-at-0, the no-door
   clause itself, is the sparse encoding's free sync: the intended
   content of every unpointed window IS 0, so fresh windows are born
   correct.

5. THE VERDICT (rule; simulation verified step-exact at every point
   probed, two-counter universality cited, Minsky 1967). The rider
   gives two exact unbounded counters with exact zero-tests and
   guarded decrement -- a two-counter Minsky machine, run BARE: no
   base extension, no depth reads, no comparisons, no hand. The bare
   element class is UNIVERSAL, and the candidate lemma ("periodic
   reads cannot assemble an aperiodic borrow") is FALSE as stated:
   the borrow is assembled from periodic reads, born-at-0 growth, and
   prime abundance (p_n > n) alone. No aperiodic stream is imported
   anywhere -- what stands in for the aperiodicity is the prime
   staircase itself, nature-given at the frontier.

SCOPE + HONESTY. The invariant argument (value <= INC count <= grows
< frontier prime) is elementary and stated in full above; the
simulation's correctness is machine-checked at every executed step of
every battery run, not proved once-and-for-all over all programs --
but the construction is program-uniform (INC/DEC/JZ are the same op
sequences regardless of the hosting program), so the batteries
exercise the general mechanism, not program-specific luck.
Universality rests on the classical two-counter theorem (Minsky
1967). The wrap control (S2) doubles as the harness's positive
control: the rig detects a wrap when one occurs, so the zero desyncs
elsewhere are the construction's property, not harness blindness.

RUN RECORD (python prime/code/explore_frontier_rider.py, 1.5 s wall
clock, trivial memory, 20 checks, all sections assert). S1 hand-walk
(9 checks). S2 wrap control (fixed pointer lies at count 7; rider
exact at headroom 22). S3 battery (seeds 0..10, horizon 60, minimum
headroom 6, seeding included). S4 random schedule (2000 ops: 896 INC
/ 848 DEC / 256 JZ; final X=4 Y=44; 896 windows grown, frontier
prime 6991; 14990 transfer passes, price exact). S5 census
(MINV_CALLS = 0; machine methods token-scanned). Two harness
edits post-run: the headroom tracker extended to cover the seeding
INCs (the first run's main-loop-only minimum read 7; the true
battery minimum is 6, at value 1 on prime 7), and S5's battery
summary print upgraded to a mechanical token scan of the machine
methods -- all other values unchanged, 20 checks before and after.
"""

import inspect
import random

# ---------------------------------------------------------------- #
# machinery: the bare machine's native ops                          #
# (verbatim from explore_bare_class.py)                             #
# ---------------------------------------------------------------- #

def sieve_primes(n):
    s = list(range(n + 1))
    s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i :: i] = [0] * len(s[i * i :: i])
    return [p for p in s if p]

PRIMES = sieve_primes(60000)

CHECKS = 0
def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1
    print(f"  [ok] {msg}")

# registers are dicts {prime window: residue}
def const(c, windows):
    """Write an integer constant (state-independent, channel-local)."""
    return {p: c % p for p in windows}

def add(x, y):
    return {p: (x[p] + y[p]) % p for p in x}

def sub(x, y):
    return {p: (x[p] - y[p]) % p for p in x}

def mul(x, y):
    return {p: (x[p] * y[p]) % p for p in x}

MINV_CALLS = 0
def minv(x):
    """The meadow pseudo-inverse (channel-local). The rider must never
    need it; the harness counts calls."""
    global MINV_CALLS
    MINV_CALLS += 1
    return {p: (pow(r, -1, p) if r != 0 else 0) for p, r in x.items()}

def born(x, p_new, c=0):
    """GROW's register extension WITHOUT the door: the new window gets
    a constant (state-independent), never the lift."""
    out = dict(x)
    out[p_new] = c % p_new
    return out

def zero_test(x):
    """The sole cross-window read: ONE bit, the AND of per-window
    zero bits."""
    return all(r == 0 for r in x.values())

# harness-only (never machine code): support inspection, true counts
def support(reg):
    return sorted(p for p, r in reg.items() if r != 0)


# ---------------------------------------------------------------- #
# the frontier rider (machine code: native ops + zero-test only)    #
# ---------------------------------------------------------------- #

class Rider:
    """The bare machine plus the rider protocol. Counters live as
    (V, P) register pairs: V holds the value at one pointed window and
    literal 0 elsewhere; P is the pointed window's idempotent. Machine
    code touches registers only through the native ops above; the
    harness inspects support() and true counts from outside."""

    def __init__(self, counters=("X", "Y"), windows=(2, 3, 5)):
        self.windows = list(windows)
        self.next_i = len(self.windows)  # PRIMES index of next fresh prime
        self.counters = counters
        self.reg = {}
        for c in counters:
            self.reg["V_" + c] = const(0, self.windows)
            self.reg["P_" + c] = const(0, self.windows)
        self.reg["ONES"] = const(1, self.windows)
        self.grow_count = 0
        self.transfer_passes = 0  # harness tally of the unary price

    def grow(self):
        """Append the next unused prime; every register born at 0; the
        fresh-window idempotent w = 1 - ONES is native; refresh ONES."""
        p_new = PRIMES[self.next_i]
        self.next_i += 1
        self.windows.append(p_new)
        for n in self.reg:
            self.reg[n] = born(self.reg[n], p_new, 0)
        w = sub(const(1, self.windows), self.reg["ONES"])
        self.reg["ONES"] = const(1, self.windows)
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
            y = mul(V, P)               # isolate the pointed window
            if zero_test(y):
                break
            V = add(sub(V, P), w)       # move one unit old -> fresh
            passes += 1
        self.transfer_passes += passes
        self.reg["P_" + c] = w
        self.reg["V_" + c] = add(V, w)  # the +1
        return passes

    def dec(self, c):
        """DEC (guarded by JZ, Minsky semantics)."""
        self.reg["V_" + c] = sub(self.reg["V_" + c], self.reg["P_" + c])

    def jz(self, c):
        return zero_test(self.reg["V_" + c])

    # ---- harness-only inspection (never machine code) ----
    def value(self, c):
        V = self.reg["V_" + c]
        s = support(V)
        assert len(s) <= 1, f"counter {c} leaked support: {s}"
        return V[s[0]] if s else 0

    def pointed_prime(self, c):
        s = support(self.reg["P_" + c])
        assert len(s) <= 1, f"pointer {c} widened: {s}"
        return s[0] if s else None


def check_invariants(m, ref):
    """Harness: true count == pointed residue (no wrap ever happened),
    true count < pointed prime (headroom), support clean, pointer a
    genuine one-window idempotent, ONES all-ones."""
    for c in m.counters:
        v_true = ref[c]
        p = m.pointed_prime(c)
        v_reg = m.value(c)
        assert v_reg == v_true, f"{c}: register {v_reg} != true {v_true}"
        if v_true > 0:
            assert p is not None and v_true < p, \
                f"{c}: headroom violated ({v_true} >= {p})"
            assert support(m.reg["V_" + c]) == [p], f"{c}: value off-pointer"
        if p is not None:
            assert m.reg["P_" + c][p] == 1, f"{c}: pointer not idempotent"
    assert all(r == 1 for r in m.reg["ONES"].values()), "ONES stale"


# ---------------------------------------------------------------- #
# the reference two-counter machine (halts iff seed is even)        #
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

def run_rider(prog, c0, horizon):
    """The same program on the rider, bare. The harness co-runs the
    integer reference for invariant checks only; machine decisions
    (JZ) come from the rider's own zero-tests."""
    m = Rider()
    ref = {"X": 0, "Y": 0}
    min_headroom = None

    def note_headroom():
        nonlocal min_headroom
        for c in m.counters:
            p = m.pointed_prime(c)
            if p is not None:
                h = p - ref[c]
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
    return trace, q, min_headroom


# ---------------------------------------------------------------- #
# sections                                                          #
# ---------------------------------------------------------------- #

def s1_hand_walk():
    print("--- S1: the hand-walk mechanized (INC, INC, DEC, DEC)")
    m = Rider(counters=("X",))
    ok(m.jz("X"), "S1 cold JZ: an untouched counter reads zero")
    m.inc("X")
    ok(support(m.reg["V_X"]) == [7] and m.reg["V_X"][7] == 1,
       "S1 INC#1: value 1 at the first fresh window (7), nowhere else")
    ok(support(m.reg["P_X"]) == [7], "S1 INC#1: pointer is e_7 exactly")
    m.inc("X")
    ok(support(m.reg["V_X"]) == [11] and m.reg["V_X"][11] == 2,
       "S1 INC#2: value migrated and bumped to 2 at fresh window 11")
    ok(m.reg["V_X"][7] == 0, "S1 INC#2: the old window emptied exactly")
    ok(not m.jz("X"), "S1 JZ at 2: nonzero read correctly")
    m.dec("X")
    ok(m.value("X") == 1 and not m.jz("X"), "S1 DEC: 2 -> 1, JZ false")
    m.dec("X")
    ok(m.jz("X"), "S1 DEC: 1 -> 0, JZ true (register literally zero)")
    ok(support(m.reg["V_X"]) == [], "S1 support clean at zero")

def s2_wrap_control():
    print("--- S2: the wrap control (the read is periodic; the rider "
          "never crosses it)")
    # fixed pointer at window 7, no migration: the naked periodic read
    m = Rider(counters=("X",))
    w = m.grow()                      # fresh = 7
    P, V = w, const(0, m.windows)
    lies = []
    for count in range(1, 8):
        V = add(V, P)
        lies.append(zero_test(V))
    ok(lies[:6] == [False] * 6,
       "S2 fixed pointer: counts 1..6 read nonzero (below the period)")
    ok(lies[6] is True,
       "S2 fixed pointer: count 7 reads ZERO at window 7 -- the "
       "periodic read lies at exactly its period")
    # the rider on the same 7-INC schedule
    r = Rider(counters=("X",))
    ref = {"X": 0}
    for _ in range(7):
        r.inc("X")
        ref["X"] += 1
        check_invariants(r, ref)
    p = r.pointed_prime("X")
    ok(r.value("X") == 7 and not r.jz("X"),
       "S2 rider: 7 INCs read exactly 7, JZ correctly false")
    ok(p - 7 > 0,
       f"S2 rider: headroom positive (pointed prime {p}, value 7)")

def s3_minsky_battery():
    print("--- S3: the Minsky battery (halts-iff-even, seeds 0..10)")
    horizon = 60
    worst_headroom = None
    for seed in range(11):
        rt, rq = run_reference(PROG, seed, horizon)
        bt, bq, hr = run_rider(PROG, seed, horizon)
        assert bt == rt, f"seed {seed}: trace desync"
        assert (bq == "HALT") == (rq == "HALT"), f"seed {seed}: halt mismatch"
        if hr is not None and (worst_headroom is None or hr < worst_headroom):
            worst_headroom = hr
        verdict = "HALT" if rq == "HALT" else f"running at {horizon}"
        print(f"  seed {seed}: step-exact, {verdict}")
    ok(True, "S3 seeds 0..10 step-exact, zero desyncs (seed 8 included)")
    ok(worst_headroom is not None and worst_headroom > 0,
       f"S3 invariant: minimum headroom over the battery = "
       f"{worst_headroom} (> 0 everywhere)")
    evens = [run_reference(PROG, s, horizon)[1] == "HALT" for s in range(0, 11, 2)]
    odds = [run_reference(PROG, s, horizon)[1] == "HALT" for s in range(1, 11, 2)]
    ok(all(evens) and not any(odds),
       "S3 halting transfers: even seeds halt, odd seeds outlive the horizon")

def s4_random_schedule():
    print("--- S4: the random schedule (2000 guarded ops, two counters)")
    rng = random.Random(1729)
    m = Rider()
    ref = {"X": 0, "Y": 0}
    n_inc = n_dec = n_jz = 0
    price_exact = True
    for _ in range(2000):
        c = rng.choice(("X", "Y"))
        r = rng.random()
        if r < 0.45:
            v_before = ref[c]
            passes = m.inc(c)
            ref[c] += 1
            n_inc += 1
            if passes != v_before:
                price_exact = False
        elif r < 0.90 and ref[c] > 0:
            jz = m.jz(c)
            assert jz is False, f"JZ lied nonzero->zero on {c}"
            m.dec(c)
            ref[c] -= 1
            n_dec += 1
        else:
            assert m.jz(c) == (ref[c] == 0), f"JZ lied on {c}"
            n_jz += 1
        check_invariants(m, ref)
    ok(True, f"S4 2000 ops exact ({n_inc} INC / {n_dec} DEC / {n_jz} JZ), "
       f"final X={ref['X']} Y={ref['Y']}, {m.grow_count} windows grown, "
       f"frontier prime {m.windows[-1]}")
    ok(price_exact,
       f"S4 the unary price: transfer passes per INC == value carried, "
       f"all {n_inc} INCs ({m.transfer_passes} passes total)")

def s5_op_census():
    print("--- S5: the op census (what the rider never used)")
    ok(MINV_CALLS == 0,
       "S5 zero meadow-inverse calls: the rider needs no pseudo-inverse")
    print("  [--] named-window residue reads: the Rider class has no such "
          "op -- the zero-test is its only cross-window read (by "
          "construction; see the class body)")
    machine_src = "".join(
        inspect.getsource(f)
        for f in (Rider.grow, Rider.inc, Rider.dec, Rider.jz))
    ok(all(tok not in machine_src
           for tok in ("minv", "supp_idem", "crt_lift", "support")),
       "S5 the rider's battery (machine methods token-scanned): no meadow "
       "inverse, no support inspection, no lift -- add, sub, mul, "
       "write-constant, zero-test, born-at-0 growth only")

def s6_verdict():
    print("--- S6: the verdict (synthesis)")
    print("  Two exact counters with exact zero-tests and guarded")
    print("  decrement run any two-counter Minsky machine, and those are")
    print("  universal (Minsky 1967). The rider is a finite-control")
    print("  machine over growing windows whose only cross-window reads")
    print("  are 1-bit zero-tests of channel-local composites -- the")
    print("  exact machine class of the candidate lemma. If S1-S5 hold,")
    print("  the lemma is FALSE as stated and the bare element class is")
    print("  UNIVERSAL: the borrow is assembled from periodic reads,")
    print("  born-at-0 growth, and prime abundance (p_n > n) alone.")

if __name__ == "__main__":
    s1_hand_walk()
    s2_wrap_control()
    s3_minsky_battery()
    s4_random_schedule()
    s5_op_census()
    s6_verdict()
    print(f"\nALL SECTIONS PASS ({CHECKS} checks)")
