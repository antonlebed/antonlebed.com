"""
explore_bare_class.py -- THE BARE CLASS: is the door-free element
machine universal or decidable? (Sibling of explore_ecc_borrow.py,
explore_growth_machine.py, and explore_interactive_hand.py.)

THE QUESTION. The recovery chart's open cell. A machine of finite
control over a GROWING squarefree window set, with the FULL native
repertoire -- channel-local ring ops (add, subtract, multiply,
multiply-by-constant), the meadow pseudo-inverse (explore_meadow.py),
the native zero-test, and per-channel reads of NAMED windows -- but NO
base extension: a window born during growth starts at a constant, never
at the CRT lift (the door explore_ecc_borrow.py prices; without it the
machine must climb alone -- external pushes cannot smuggle the door in,
explore_interactive_hand.py). Is THIS machine Turing-universal, or does
it stay decidable like the growth machine (explore_growth_machine.py)?

THE STAKES. Every known door that buys universality back for the
finite-window world is a READ import -- an unbounded aperiodic stream
read from beyond the windows (the recovery chart's unifying statement).
If the bare machine is universal, that law BREAKS: universality with
zero import. If it is decidable, the door-free bulk provably keeps the
sibling dividends (decidable equivalence, canonical forms,
self-certification) -- the bulk-side pillar of the thin-door question.

THE CANDIDATE CONSTRUCTION (the cleverness to probe). The meadow makes
SUPPORT PATTERNS first-class: e = x * x^(-1) (pseudo-inverse) is the
idempotent that is 1 exactly on the windows where x is nonzero --
native and channel-local. Idempotents form a Boolean algebra (AND =
multiply, NOT = 1 - e, OR = e + f - e*f), and UNLIKE the modulus --
which only ever grows -- an idempotent's support CAN go down: e AND
NOT(w) removes a window. So encode two Minsky counters as two
idempotent registers, counter value = |support|:
    INC c:  grow a fresh window w, set e_c := e_c OR w
    DEC c:  remove ONE window from e_c's support
    JZ  c:  the native zero-test (support empty iff e_c = 0)
If this runs a two-counter machine step-exactly, the bare class is
universal. The probe's job is to run the construction where it runs,
locate exactly where it breaks if it breaks, and prove the rig could
SEE universality were it present (the positive control).

THE MODEL (fixed before any run).
  - State: a list of prime windows, initially [2, 3, 5]; registers are
    residue tuples over the current windows.
  - GROW: append the next unused prime; every register is BORN at 0 in
    the new window (state-independent -- the no-door clause; contrast
    base_extend in explore_ecc_borrow.py).
  - Native ops (all channel-local: output at window p depends only on
    inputs at window p): add, sub, mul (elementwise); write an integer
    constant; multiply/add a constant; the meadow pseudo-inverse
    x -> x^(-1) (per window: the field inverse if nonzero, else 0);
    the support idempotent e = x * x^(-1).
  - Cross-window reads: the ZERO-TEST (one bit: is the register 0 in
    every window?) and residue reads at windows NAMED in the program
    text (a fixed finite set).
  - Finite control: no unbounded integers in control state. A loop
    index that grows with the run must live in a REGISTER (and so
    wraps mod p in every window), never in control.
  - Harness discipline: the CRT lift appears ONLY in harness
    verification and in the S6 oracle -- machine code never calls it.

THE DESIGN (what each section asks).

S1  THE SOLE-FOLD CENSUS. Mechanically verify the op battery's
    locality: every native op except the zero-test is channel-local
    (output at p a function of inputs at p alone -- checked by grouping
    exhaustive inputs by their window-p component), the born value is
    state-independent, and the zero-test is the SOLE cross-window read,
    returning exactly one bit = the AND of the per-window zero bits.
    This is the mechanical core of the SOLE-FOLD LEMMA (candidate,
    stated in the analysis below): the only native fold over the
    unbounded window set is the 1-bit zero-test.

S2  INC AND JZ ARE CLEAN. The fresh-window idempotent is native with
    no import: keep a register ONES := constant 1; after a grow, ONES
    is 1 on the old windows and 0 on the new (born at 0), so
    w = 1 - ONES is exactly the new window's idempotent; then refresh
    ONES. Run INC/JZ sequences and check |support| tracks the counter.

S3  STATIC ADDRESSING IS BOUNDED. DEC below a frontier: for a prime p
    NAMED by an integer constant c with p | c, the window idempotent
    w_p = 1 - (c * c^(-1)) is native, and e AND NOT w_p removes window
    p. But a fixed program's constants have a FIXED prime support:
    verify that every mask built from integer constants with prime
    divisors <= C leaves every window > C untouched, so counters whose
    marks outrun C are un-decrementable by static masks. (Dynamic
    constants built in loops -- e.g. 2^A - 1 -- are the S5 escape.)

S4  POPCOUNT IS NOT A REGISTER. The down-move "read |support(e)| as an
    integer, decrement it" needs the population count. |support| is a
    cross-window SUM, defined only through a Z-lift. Mechanically: two
    idempotents that AGREE at a window but differ in |support| force
    any channel-local composite to agree at that window -- so no
    composite g has g(e) = constant(|support(e)|) for all e (the
    constant's residue at the agreeing window would have to differ).
    Popcount-as-a-register is non-native; popcount-as-a-BIT-STREAM
    (one zero-test at a time) is exactly the S5 seam.

S5  THE AGE-SCAN ESCAPE (the loop-of-zero-tests seam, probed head-on).
    The strongest DEC realizer we could design without the door:
    maintain TS := TS + 1 at every grow (so TS at window p is the
    window's AGE mod p -- an unbounded age stored in a finite window
    WRAPS); to DEC, scan upward with a register A := A + 1 and remove
    e AND [TS - A = 0] at the first nonempty hit. The scan terminates
    whenever e is nonempty, removes SOME marked window -- and the
    counter value does not care WHICH window dies, only that exactly
    ONE does. So the escape's sole failure mode is a COLLISION: two
    marked windows p, q with TS_p == a (mod p) and TS_q == a (mod q)
    at the same first hit -- both removed, the count drops by two, the
    next zero-test lies. The probe: (a) run the full Minsky battery
    under the age-scan and record how far step-exactness carries;
    (b) build the collision by hand -- CRT solves for a spin length d
    that puts BOTH marks at TS = 1 simultaneously (the very
    independence that makes channels free makes wraps collide) -- and
    exhibit the desync against the reference; (c) census the collision
    fraction over spin lengths; (d) verify the per-window firing
    predicate is PERIODIC (period p for the additive scan; period
    ord_p(2) for the multiplicative variant 2^A - 1, where marks at 23
    and 89 -- both of 2-order 11 -- collide PERMANENTLY); (e) note the
    machine cannot DETECT a collision (that is S4's popcount).

S6  THE POSITIVE CONTROL. Hand the same rig the base-extension oracle
    (grow-and-extend before each INC, explore_ecc_borrow.py) and run
    the halts-iff-even two-counter program, seeds 0..8: the traces
    must be step-exact against the reference and halting must
    transfer. The rig can SEE universality when the door is present;
    a decidable verdict for the bare machine is then a property of
    the machine, not of the harness.

S7  THE COLLAPSE. With no working DEC, the idempotent machine's
    surviving repertoire is INC + zero-test -- the growth machine's
    regime (explore_growth_machine.py: monotone counter machines are
    well-structured transition systems, halting decidable on the
    finite (control, zero-pattern) quotient; Finkel-Schnoebelen 2001,
    Minsky 1967). Compile a battery of INC/JZ programs to the
    idempotent encoding, run them bare, and check the quotient
    decider's verdicts against the bare runs -- including programs
    whose forward simulation never terminates.

THE ANALYSIS BEHIND THE PREDICTIONS (the pre-code hand-attack).
  - |support| factors through the Z-lift: summing per-window bits
    across windows is base extension in disguise, so the cardinality
    counter does not AVOID the door, it RE-DERIVES it.
  - A walking pointer ("the next window after p") needs the prime
    successor -- an ordering fact living at the deleted archimedean
    place; idempotent pointers cannot walk.
  - THE SOLE-FOLD LEMMA (candidate; S1 verifies its op-battery core,
    the general form stays open): the only native op whose output
    depends on more than a bounded named window set is the zero-test,
    and it returns one bit. Every escape from it needs unbounded
    addressing, a Z-lift, or depth -- all deleted or absent (bare =
    squarefree). If the lemma holds in full, the bare machine is
    INC + zero-test + no borrow, and its halting is decidable by the
    growth-machine theorem. The lemma's live seam is exactly S5: a
    loop of 1-bit zero-tests DOES read across windows; what the wrap
    forces is that every selector it builds reads each window through
    a PERIODIC predicate, while every known door imports an APERIODIC
    stream. "Periodic reads cannot assemble an aperiodic borrow" is
    the missing half -- stated here as the candidate's edge, not
    claimed.

FINDINGS (entered after the run; every number below is from the
printed output; run record at the end).

1. THE SOLE-FOLD CENSUS HOLDS ON THE BATTERY (rule, exhaustive over
   the modelled ops at windows [2,3,5]; S1). Every native op -- add,
   sub, mul, the meadow pseudo-inverse, the support idempotent,
   constants, born -- is channel-local (outputs grouped by the
   window-p input are constant: 30 registers, 900 pairs per binary op,
   no exception), born is state-independent, and the zero-test is the
   SOLE fold: one bit, exactly the AND of the per-window zero bits.

2. INC AND JZ ARE CLEAN AND NATIVE (rule; verified S2). w = 1 - ONES
   after a grow is
   exactly the fresh window's idempotent; the counter register stays
   idempotent through 8 INCs, |support| tracks [1..8], and the
   zero-test is exact at 0 and at 8.

3. STATIC ADDRESSING IS BOUNDED (rule; exhaustive over the stated
   mask set, S3). Constant 7's mask removes
   exactly window 7; all 619 masks built from 20-smooth constants
   below 3000 leave every mark above 20 untouched. A fixed program's
   constants have fixed prime support: static DEC dies once the marks
   outrun the program text.

4. POPCOUNT IS NOT A REGISTER (rule; the locality argument plus the
   enumerated closure, S4). Two idempotents with supports of
   size 1 and 2 agree at window 2; constant(|support|) would have to
   differ there (1 vs 2 mod 2), yet all 399 enumerated channel-local
   composites agree at window 2 on both. |support| is a cross-window
   sum, defined only through the Z-lift: the cardinality counter does
   not AVOID the base-extension door, it RE-DERIVES it.

5. THE AGE-SCAN DIES AT THE WRAP (the headline; rule for the probed
   protocol family, by witnessed desync; S5). The strongest
   doorless DEC we could design -- scan A = 1, 2, ... by register and
   remove the first-hit class e AND [TS = A] -- is GUARANTEED correct
   only while every marked window's age stays below its own prime
   (ages then equal their TS values and are distinct, so the first hit
   is a single window); past the wrap, correctness is schedule luck
   (seed 7 wraps window 7 to TS = 0 and still runs exact -- the wrap
   kills only on a TIE). The plain battery breaks it WITHOUT
   adversarial help: seeds 0..7 run
   step-exact, seed 8 desyncs at step 1 (window 7's age 8 wraps to 1
   and ties window 31's age 1; the first DEC removes both, ref (1,7,0)
   vs bare (1,6,0)). The constructed collision confirms the mechanism:
   d = 55 spins put marks 7 and 11 both at TS = 1, ONE DEC drops the
   counter 2 -> 0, and the next zero-test LIES -- the branch flips
   against the reference. Census: 35/400 spin lengths collide
   (fraction 0.087; first hits 55..61, 132). The firing predicates are
   PERIODIC per window (period 7 at window 7; the multiplicative
   variant 2^A - 1 fires 23 and 89 together PERMANENTLY -- shared
   2-order 11), and by finding 4 the machine cannot DETECT a
   collision. The wrap is the deleted place at the read layer: an
   unbounded age stored in a finite window is age mod p, and the CRT
   independence that makes the channels free is exactly what makes
   the wraps collide.

6. THE RIG SEES UNIVERSALITY (the positive control; verified S6). The
   same harness
   with the base-extension oracle runs halts-iff-even step-exactly on
   seeds 0..8 with halting transferring exactly -- the bare failures
   above are the machine's, not the rig's.

7. THE COLLAPSE (rule; the cited decidability theorem plus agreement
   on the battery, S7). With no working DEC the construction's
   surviving repertoire is INC + zero-test: the monotone-counter
   quotient decider settles the compiled battery (M_A LOOP, M_B HALT,
   M_C HALT, M_D HALT and LOOP) in agreement with the bare idempotent
   runs -- including the two certified LOOPs whose forward simulation
   never ends.

8. THE VERDICT (synthesis; the lemma stays an open candidate). The
   candidate construction
   is DEAD: every down-move route TRIED either re-derives a read import
   (popcount = the Z-lift = base extension; a walking pointer = the
   prime successor = the deleted archimedean order) or collides at
   the wrap; what survives is decidable (finding 7). The CLASS verdict
   stays OPEN at the named residual: the loop of zero-tests genuinely
   reads across windows, but every selector it built here reads each
   window through a PERIODIC predicate, while every known door imports
   an unbounded APERIODIC stream. "Periodic reads cannot assemble an
   aperiodic borrow" is the exact missing half of the sole-fold lemma;
   proved, it would make the bare class decidable -- and the
   read-import law a theorem for the door-free bulk.

SCOPE + HONESTY. The sole-fold census is exhaustive over the MODELLED
op battery at windows [2,3,5], and S4's composite closure is a finite
two-round enumeration -- the mechanical core of the lemma, not its
general form; the general lemma (all programs, all registers) is the
named open residual, and NO class-level decidability is claimed here.
The age-scan kill is a witnessed desync for the probed protocol family
(first-hit selectors from additive and multiplicative scans); that ANY
selector family inherits the periodicity is argued, not proved.
Decidability background: monotone counter machines are well-structured
transition systems with decidable termination (Finkel-Schnoebelen
2001); Minsky machines are universal (Minsky 1967) -- both reached
through explore_growth_machine.py's decider, re-run here on the
compiled battery. (The residual has since settled: the bare class is
UNIVERSAL -- a sparse counter riding the growth frontier evades every
wall censused here, explore_frontier_rider.py -- so the candidate
lemma is false as stated; this record stands as the census of the
walls that construction dodges.)

PREDICTIONS (fixed before the run). Adjudication after it -- four
confirmed, one standing scope statement, one half-miss, the miss in
the thesis direction:
  PR1  INC and JZ are clean and native: grow + OR-in the fresh-window
       idempotent tracks the counter exactly; the zero-test is exact.
       ... CONFIRMED (S2: |support| = [1..8], zero-test exact).
  PR2  Static addressing dies at a frontier: masks from a fixed
       constant set touch only that set's prime divisors, so DEC by
       named masks fails once marks outrun the program text.
       ... CONFIRMED (S3: 619 smooth masks leave marks > 20 untouched).
  PR3  Popcount is not a register: no channel-local composite returns
       constant(|support|) -- the agree-at-a-window exhibit forces a
       contradiction. The Z-lift factoring stands.
       ... CONFIRMED (S4: 399 composites agree at the shared window).
  PR4  The idempotent two-counter construction therefore yields INC +
       zero-test with no borrow: its bare runs are decided by the
       growth-machine quotient (agreement on the S7 battery).
       ... CONFIRMED (S7: decider and bare runs agree on all five).
  PR5  (the honest edge) PR4 kills THIS construction, not the class.
       The named residual: prove the sole-fold lemma in full (a
       well-quasi-order making the bare configuration space a WSTS)
       -- named, not claimed here.
       ... STANDS (a scoping statement, not run-adjudicable).
  PR6  (from the age-scan hand-attack) The age-scan runs the Minsky
       battery step-exactly at SHORT range (fresh primes are large,
       ages are small, no wraps), and dies at the constructed
       collision: a CRT-chosen spin length puts two marks in the same
       first-hit class, one DEC removes both, the branch flips vs the
       reference. The failure lives in the tail -- exactly where
       universality needs the simulation to hold.
       ... HALF MISS. The constructed collision, the 2 -> 0 drop, and
       the branch flip landed exactly as frozen -- but the short-range
       clause was WRONG: seed 8 collides naturally at its FIRST DEC.
       The wrap arrives as soon as a counter's value reaches its
       smallest marked window's prime (seed 7 wraps too, without a
       tie), and at seed 8 it lands on a tie -- no adversarial spins
       needed. The miss strengthens the kill: the escape is weaker
       than predicted.

RUN RECORD (python prime/code/explore_bare_class.py, 0.2 s wall clock
by subprocess timing, trivial memory, 45 checks, all sections assert):
S1 locality census (exhaustive at windows [2,3,5]: 30 registers, 900
pairs per binary op; zero-test = AND over all 30). S2 INC/JZ (8 INCs,
|support| = [1..8]). S3 frontier (constant-7 mask exact; 619 20-smooth
masks < 3000, five marks above 20 untouched). S4 popcount (two-round
composite closure over {e, 1, 7} = 399 composites, all agree at the
shared window). S5 age-scan (seeds 0..8: 8/9 step-exact, seed 8
desyncs at step 1 with selector [7, 31] and TS (age mod p) at the
marks {7:1, 11:7, 13:6, 17:5, 19:4, 23:3, 29:2, 31:1} -- window 7's
true age is 8, wrapped; constructed collision d = 55 at
marks {7, 11}; census 35/400 = 0.087, first hits 55..61, 132;
period-7 pin at window 7; ord_2(23) = ord_2(89) = 11). S6 oracle
control (seeds 0..8 step-exact, halting transfers). S7 decider battery
(five programs, two certified LOOPs outliving a 300-step horizon).
One harness addition post-run: the S5(a) desync diagnosis print
(seed, step, first-DEC selector, mark ages) -- values unchanged, 45
checks before and after.
"""

import math

# ---------------------------------------------------------------- #
# machinery: the bare machine's native ops                          #
# ---------------------------------------------------------------- #

def sieve_primes(n):
    s = list(range(n + 1))
    s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i :: i] = [0] * len(s[i * i :: i])
    return [p for p in s if p]

PRIMES = sieve_primes(20000)

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

def add_const(x, c):
    return {p: (r + c) % p for p, r in x.items()}

def mul_const(x, c):
    return {p: (r * c) % p for p, r in x.items()}

def minv(x):
    """The meadow pseudo-inverse: per window, the field inverse of a
    nonzero residue, else 0 (explore_meadow.py). Channel-local."""
    return {p: (pow(r, -1, p) if r != 0 else 0) for p, r in x.items()}

def supp_idem(x):
    """The support idempotent e = x * x^(-1): 1 exactly where x != 0."""
    return mul(x, minv(x))

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

# Boolean algebra on idempotents (all channel-local composites)
def i_or(e, f):
    return sub(add(e, f), mul(e, f))

def i_and(e, f):
    return mul(e, f)

def i_not(e, windows):
    return sub(const(1, windows), e)

# harness-only (never machine code): the CRT lift, support inspection
def crt_lift(reg):
    N = 1
    for p in reg:
        N *= p
    x = 0
    for p, r in reg.items():
        x = (x + r * pow(N // p, -1, p) * (N // p)) % N
    return x

def support(reg):
    return sorted(p for p, r in reg.items() if r != 0)


# ---------------------------------------------------------------- #
# the bare machine state (growth + registers, no door)              #
# ---------------------------------------------------------------- #

class Bare:
    """Finite control's world: growing windows, registers born at 0.
    Machine code touches registers only through the native ops above;
    the harness inspects support()/crt_lift() from outside."""

    def __init__(self, reg_names, windows=(2, 3, 5)):
        self.windows = list(windows)
        self.next_i = len(self.windows)  # PRIMES index of next fresh prime
        self.reg = {n: const(0, self.windows) for n in reg_names}
        self.reg["ONES"] = const(1, self.windows)
        self.reg["TS"] = const(0, self.windows)
        self.grow_count = 0

    def grow(self):
        """Append the next unused prime; every register born at 0;
        maintain TS (age mod p) and return the fresh-window idempotent
        w = 1 - ONES (native: ONES is 1 on old windows, 0 on the new),
        then refresh ONES."""
        p_new = PRIMES[self.next_i]
        self.next_i += 1
        self.windows.append(p_new)
        for n in self.reg:
            self.reg[n] = born(self.reg[n], p_new, 0)
        w = sub(const(1, self.windows), self.reg["ONES"])
        self.reg["ONES"] = const(1, self.windows)
        self.reg["TS"] = add_const(self.reg["TS"], 1)
        self.grow_count += 1
        return w

    def inc(self, name):
        """INC: grow, OR the fresh-window idempotent into the counter."""
        w = self.grow()
        self.reg[name] = i_or(self.reg[name], w)

    def spin(self):
        """A grow that marks nothing (the adversary's clock)."""
        self.grow()

    def jz(self, name):
        return zero_test(self.reg[name])

    def dec_age_scan(self, name):
        """The S5 escape: scan A = 1, 2, ... (A is a REGISTER -- it
        wraps mod p per window) and remove e AND [TS - A = 0] at the
        first nonempty hit. Returns the removed selector (for the
        harness's collision inspection)."""
        e = self.reg[name]
        s = age_scan_selector(e, self.reg["TS"], self.windows)
        one = const(1, self.windows)
        self.reg[name] = i_and(e, sub(one, s))  # e AND NOT s
        return s


def age_scan_selector(e, TS, windows, cap=10 ** 6):
    """The scan's first-hit selector, as the machine computes it: only
    native ops on registers; the loop index A is itself a register."""
    one = const(1, windows)
    A = const(0, windows)
    for _ in range(cap):
        A = add_const(A, 1)
        d = sub(TS, A)
        s = i_and(e, sub(one, supp_idem(d)))  # e AND [TS == A]
        if not zero_test(s):
            return s
    raise RuntimeError("age-scan did not terminate within cap")


# ---------------------------------------------------------------- #
# the reference two-counter machine (halts iff seed is even)        #
# ---------------------------------------------------------------- #

PROG = {
    0: ("DECJZ", "X", 1, "HALT"),
    1: ("DECJZ", "X", 0, "LOOP"),
    "LOOP": ("INC", "Y", "LOOP"),
}

def run_reference(c0, horizon):
    q, c = 0, {"X": c0, "Y": 0}
    trace = [(q, c["X"], c["Y"])]
    for _ in range(horizon):
        if q == "HALT":
            break
        ins = PROG[q]
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
    return trace


# ---------------------------------------------------------------- #
# S1 -- the sole-fold census                                        #
# ---------------------------------------------------------------- #

def s1():
    print("S1  the sole-fold census: locality of the op battery")
    W = [2, 3, 5]
    N = 2 * 3 * 5
    all_regs = [{2: a, 3: b, 5: c}
                for a in range(2) for b in range(3) for c in range(5)]
    ok(len(all_regs) == N, "exhaustive register space over windows [2,3,5]")

    unary = [("minv", minv), ("supp_idem", supp_idem),
             ("add_const 7", lambda x: add_const(x, 7)),
             ("mul_const 7", lambda x: mul_const(x, 7)),
             ("not", lambda x: i_not(x, W))]
    for name, f in unary:
        local = True
        for p in W:
            seen = {}
            for x in all_regs:
                key = x[p]
                val = f(x)[p]
                if key in seen and seen[key] != val:
                    local = False
                seen.setdefault(key, val)
        ok(local, f"unary {name} is channel-local (output at p = f(input at p))")

    binary = [("add", add), ("sub", sub), ("mul", mul)]
    for name, f in binary:
        local = True
        for p in W:
            seen = {}
            for x in all_regs:
                for y in all_regs:
                    key = (x[p], y[p])
                    val = f(x, y)[p]
                    if key in seen and seen[key] != val:
                        local = False
                    seen.setdefault(key, val)
        ok(local, f"binary {name} is channel-local")

    # born is state-independent: the new window's value ignores the state
    vals = {born(x, 7, 0)[7] for x in all_regs}
    ok(vals == {0}, "born writes a state-independent constant at the new window")
    # constants are state-independent by construction (no register input)

    # the zero-test: the sole cross-window read, exactly one bit,
    # exactly the AND of the per-window zero bits
    for x in all_regs:
        ok_and = all(r == 0 for r in x.values())
        if zero_test(x) != ok_and:
            ok(False, "zero-test == AND of per-window zero bits")
    ok(True, f"zero-test == AND of per-window zero bits ({N} registers)")
    # and it is NOT channel-local (it reads every window): witness
    x1 = {2: 0, 3: 0, 5: 0}
    x2 = {2: 0, 3: 1, 5: 0}
    ok(zero_test(x1) != zero_test(x2) and x1[2] == x2[2],
       "zero-test output differs on registers agreeing at window 2: it is a fold")
    print()


# ---------------------------------------------------------------- #
# S2 -- INC and JZ are clean (the fresh-window idempotent)          #
# ---------------------------------------------------------------- #

def s2():
    print("S2  INC + JZ: the fresh-window idempotent is native")
    m = Bare(["E"])
    ok(m.jz("E"), "counter starts empty: zero-test true")
    sizes = []
    for k in range(1, 9):
        m.inc("E")
        e = m.reg["E"]
        sizes.append(len(support(e)))
        # the register is a genuine idempotent: e*e = e
        ok_idem = mul(e, e) == e
        if not ok_idem:
            ok(False, "counter register stays idempotent")
    ok(True, "counter register stays idempotent through 8 INCs")
    ok(sizes == list(range(1, 9)),
       f"|support| tracks the counter through 8 INCs: {sizes}")
    ok(not m.jz("E"), "zero-test false at value 8")
    # the fresh-window idempotent construction: w = 1 - ONES after grow
    m2 = Bare(["E"])
    w = m2.grow()
    ok(support(w) == [m2.windows[-1]],
       "w = 1 - ONES is exactly the fresh window's idempotent")
    print()


# ---------------------------------------------------------------- #
# S3 -- static addressing is bounded by the constant set            #
# ---------------------------------------------------------------- #

def s3():
    print("S3  static addressing: masks from constants touch only their")
    print("    prime divisors -- the frontier")
    m = Bare(["E"])
    for _ in range(10):
        m.inc("E")
    marks = support(m.reg["E"])
    frontier_C = 20
    # below the frontier: a named mask works. 7 is a mark and 7 <= 20.
    one = const(1, m.windows)
    c7 = const(7, m.windows)
    w7 = sub(one, supp_idem(c7))          # the window-7 idempotent
    ok(support(w7) == [7], "constant 7 addresses exactly window 7")
    e_after = i_and(m.reg["E"], sub(one, w7))
    ok(support(e_after) == [p for p in marks if p != 7],
       "named-mask DEC removes exactly window 7 below the frontier")
    # above the frontier: EVERY constant with prime support <= C leaves
    # every window > C untouched. Exhaustive over all c whose prime
    # divisors are <= C, up to a large bound (their masks can only
    # address primes <= C).
    high_marks = [p for p in marks if p > frontier_C]
    ok(len(high_marks) >= 5, f"marks outrun the frontier: {high_marks}")
    def is_smooth(c, C):
        for q in PRIMES:
            if q > C:
                break
            while c % q == 0:
                c //= q
        return c == 1
    smooth = [c for c in range(2, 3000) if is_smooth(c, frontier_C)]
    untouched = True
    for c in smooth:
        wc = sub(one, supp_idem(const(c, m.windows)))
        masked = i_and(m.reg["E"], sub(one, wc))
        for p in high_marks:
            if masked[p] != m.reg["E"][p]:
                untouched = False
    ok(untouched,
       f"all {len(smooth)} masks from 20-smooth constants < 3000 leave "
       f"every mark > 20 untouched")
    print("    a fixed program's constant set has fixed prime support:")
    print("    static DEC dies once marks outrun the program text")
    print()


# ---------------------------------------------------------------- #
# S4 -- popcount is not a register                                  #
# ---------------------------------------------------------------- #

def s4():
    print("S4  popcount is not a register (the Z-lift factoring)")
    W = [2, 3, 5, 7, 11]
    # two idempotents agreeing at window 2 with different |support|
    e1 = {2: 0, 3: 0, 5: 0, 7: 1, 11: 0}   # |support| = 1
    e2 = {2: 0, 3: 0, 5: 0, 7: 1, 11: 1}   # |support| = 2
    ok(e1[2] == e2[2], "e1, e2 agree at window 2")
    ok(len(support(e1)) != len(support(e2)), "|support| differs (1 vs 2)")
    # if some channel-local composite g returned constant(|support(e)|),
    # then g(e1)[2] = 1 % 2 = 1 and g(e2)[2] = 2 % 2 = 0 -- but S1's
    # census says every composite of channel-local ops is channel-local,
    # so g(e1)[2] == g(e2)[2]. Contradiction, exhibited numerically:
    want1 = const(len(support(e1)), W)
    want2 = const(len(support(e2)), W)
    ok(want1[2] != want2[2],
       "constant(|support|) must differ at window 2 (1 mod 2 vs 2 mod 2)")
    # channel-locality of composites: brute-force a two-round closure
    # of the op battery over {e, 1, 7}, confirm output at window 2 is
    # identical on e1 and e2 (they agree there)
    def composites(e, W):
        pool = {("e",): e, ("one",): const(1, W), ("c7",): const(7, W)}
        atoms = list(pool.items())
        for rnd in range(2):
            items = list(pool.items())
            for ka, a in items:
                pool[("minv", ka)] = minv(a)
                pool[("supp", ka)] = supp_idem(a)
                for kb, b in atoms:
                    pool[("add", ka, kb)] = add(a, b)
                    pool[("sub", ka, kb)] = sub(a, b)
                    pool[("mul", ka, kb)] = mul(a, b)
        return pool

    pool1 = composites(e1, W)
    pool2 = composites(e2, W)
    ok(set(pool1) == set(pool2), f"{len(pool1)} composites enumerated on both")
    agree = all(pool1[k][2] == pool2[k][2] for k in pool1)
    ok(agree,
       "every enumerated composite agrees at window 2 on e1 vs e2: "
       "no composite returns constant(|support|)")
    print("    |support| is a cross-window sum -- defined only through the")
    print("    Z-lift: the cardinality counter re-derives base extension")
    print()


# ---------------------------------------------------------------- #
# S5 -- the age-scan escape (the loop-of-zero-tests seam)           #
# ---------------------------------------------------------------- #

def run_bare_agescan(c0, horizon):
    """The halts-iff-even program on the idempotent encoding with the
    age-scan DEC. Trace records (control, |supp X|, |supp Y|) -- the
    support sizes read by the HARNESS, not the machine."""
    m = Bare(["X", "Y"])
    for _ in range(c0):
        m.inc("X")
    q = 0
    trace = [(q, len(support(m.reg["X"])), len(support(m.reg["Y"])))]
    collisions = 0
    for _ in range(horizon):
        if q == "HALT":
            break
        ins = PROG[q]
        if ins[0] == "INC":
            m.inc(ins[1])
            q = ins[2]
        else:
            _, r, nz, z = ins
            if m.jz(r):
                q = z
            else:
                s = m.dec_age_scan(r)
                if len(support(s)) > 1:
                    collisions += 1
                q = nz
        trace.append((q, len(support(m.reg["X"])), len(support(m.reg["Y"]))))
    return trace, collisions


def s5():
    print("S5  the age-scan escape: loop of zero-tests, probed head-on")

    # (a) short range: the Minsky battery, seeds 0..8
    exact = []
    diag = []
    for c0 in range(9):
        ref = run_reference(c0, 60)
        bare, coll = run_bare_agescan(c0, 60)
        exact.append(ref == bare and coll == 0)
        if not exact[-1]:
            # for the record: first divergence + the first DEC's selector
            step = next((i for i, (a, b) in enumerate(zip(ref, bare))
                         if a != b), min(len(ref), len(bare)))
            mm = Bare(["X", "Y"])
            for _ in range(c0):
                mm.inc("X")
            s0 = age_scan_selector(mm.reg["X"], mm.reg["TS"], mm.windows)
            diag.append((c0, step, ref[step], bare[step], support(s0),
                         {p: mm.reg["TS"][p] for p in support(mm.reg["X"])}))
    n_exact = sum(exact)
    print(f"    (a) seeds 0..8: {n_exact}/9 runs step-exact vs reference")
    for c0, step, r, b, sel, ts in diag:
        print(f"        seed {c0} desyncs at step {step}: ref={r} bare={b}")
        print(f"        first-DEC selector {sel}; TS (age mod p) at marks {ts}")

    # (b) the constructed collision: two marks, CRT-chosen spin length
    m = Bare(["X", "Y"])
    m.inc("X")
    m.inc("X")
    p1, p2 = support(m.reg["X"])
    ts1 = m.reg["TS"][p1]
    ts2 = m.reg["TS"][p2]
    # want, after d spins: TS at p1 == 1 (mod p1) and TS at p2 == 1 (mod p2)
    # -> both fire at the scan's FIRST iteration: forced double removal
    r1 = (1 - ts1) % p1
    r2 = (1 - ts2) % p2
    # CRT for d == r1 (mod p1), d == r2 (mod p2)
    d = (r1 * p2 * pow(p2, -1, p1) + r2 * p1 * pow(p1, -1, p2)) % (p1 * p2)
    for _ in range(d):
        m.spin()
    ok(m.reg["TS"][p1] == 1 and m.reg["TS"][p2] == 1,
       f"after d = {d} spins both marks sit at TS = 1 "
       f"(windows {p1}, {p2}: the wrap aligns them)")
    before = len(support(m.reg["X"]))
    s = m.dec_age_scan("X")
    after = len(support(m.reg["X"]))
    ok(len(support(s)) == 2,
       f"ONE age-scan DEC removes BOTH marks: selector support {support(s)}")
    ok(before == 2 and after == 0,
       "counter drops 2 -> 0 in one DEC: the count is wrong")
    ok(m.jz("X"),
       "the next zero-test LIES (reads 0, reference holds 1): branch flips")
    print("    (b) the collision is constructible: CRT places both wraps")
    print("        in the same first-hit class -- the independence that")
    print("        makes channels free makes wraps collide")

    # (c) collision census over spin lengths: one machine, peek the
    # selector non-destructively at each spin count
    D = 400
    n_coll = 0
    firsts = []
    mm = Bare(["X", "Y"])
    mm.inc("X")
    mm.inc("X")
    for d in range(D):
        s = age_scan_selector(mm.reg["X"], mm.reg["TS"], mm.windows)
        if len(support(s)) > 1:
            n_coll += 1
            if len(firsts) < 8:
                firsts.append(d)
        mm.spin()
    frac = n_coll / D
    ok(n_coll > 0, f"census: {n_coll}/{D} spin lengths collide "
                   f"(fraction {frac:.3f}); first hits {firsts}")
    print("    (c) collisions recur for a positive fraction of schedules --")
    print("        and S4 says the machine cannot DETECT one (popcount)")

    # (d) the firing predicate is periodic per window
    #     additive scan: [TS == a] at window p has period p in the age
    mm = Bare(["X", "Y"])
    mm.inc("X")
    p1 = support(mm.reg["X"])[0]
    hits = []
    for g in range(2 * p1 + 2):
        hits.append(mm.reg["TS"][p1] == 1)
        mm.spin()
    period_ok = all(hits[i] == hits[i + p1] for i in range(len(hits) - p1))
    ok(period_ok, f"additive firing predicate at window {p1} has period {p1}")
    #     multiplicative variant: [p | 2^A - 1] has period ord_p(2);
    #     23 and 89 share ord = 11 -> permanent collision
    def ord2(p):
        a, v = 1, 2 % p
        while v != 1:
            v = v * 2 % p
            a += 1
        return a
    ok(ord2(23) == 11 and ord2(89) == 11,
       "23 and 89 share 2-order 11: the 2^A - 1 selector fires both "
       "PERMANENTLY -- no schedule separates them")
    print("    (d) every selector the loop builds reads each window through")
    print("        a PERIODIC predicate; the doors import APERIODIC streams")
    print()


# ---------------------------------------------------------------- #
# S6 -- the positive control: the rig sees universality             #
# ---------------------------------------------------------------- #

def base_extend(reg, p_new):
    """THE DOOR (harness oracle; explore_ecc_borrow.py): the new window
    reads the CRT lift of the synced source windows."""
    out = dict(reg)
    src = {p: r for p, r in reg.items() if p != p_new}
    out[p_new] = crt_lift(src) % p_new
    return out

def run_oracle(c0, horizon):
    """Element counters with grow-and-extend before each INC: the
    door-equipped machine of explore_ecc_borrow.py, rerun as control."""
    windows = [2, 3, 5]
    next_i = 3
    X = {p: c0 % p for p in windows}
    Y = {p: 0 for p in windows}
    q = 0
    trace = [(q, crt_lift(X), crt_lift(Y))]
    for _ in range(horizon):
        if q == "HALT":
            break
        ins = PROG[q]
        if ins[0] == "INC":
            p_new = PRIMES[next_i]
            next_i += 1
            windows.append(p_new)
            X = base_extend(born(X, p_new), p_new)
            Y = base_extend(born(Y, p_new), p_new)
            if ins[1] == "X":
                X = add_const(X, 1)
            else:
                Y = add_const(Y, 1)
            q = ins[2]
        else:
            _, name, nz, z = ins
            t = X if name == "X" else Y
            if zero_test(t):
                q = z
            else:
                t = add_const(t, -1)
                if name == "X":
                    X = t
                else:
                    Y = t
                q = nz
        trace.append((q, crt_lift(X), crt_lift(Y)))
    return trace

def s6():
    print("S6  positive control: with the door the rig SEES universality")
    horizon = 100
    all_exact, verdicts = True, True
    for c0 in range(9):
        ref = run_reference(c0, horizon)
        orc = run_oracle(c0, horizon)
        if ref != orc:
            all_exact = False
        if (orc[-1][0] == "HALT") != (c0 % 2 == 0):
            verdicts = False
    ok(all_exact, "oracle traces step-exact (state, X, Y) for seeds 0..8")
    ok(verdicts, "halting transfers: even seeds halt, odd seeds diverge")
    print("    the harness detects universality when the door is present:")
    print("    a bare-machine failure is the machine's, not the rig's")
    print()


# ---------------------------------------------------------------- #
# S7 -- the collapse: the surviving repertoire is decidable         #
# ---------------------------------------------------------------- #

def decide_halting(instr, q0, zero_pattern):
    """The monotone-counter quotient decider
    (explore_growth_machine.py): DFS on (control, zero-pattern);
    zero-pattern flips 0 -> + at most once per counter."""
    q = q0
    zp = list(zero_pattern)
    seen = set()
    while True:
        if q == "HALT":
            return "HALT"
        node = (q, tuple(zp))
        if node in seen:
            return "LOOP"
        seen.add(node)
        ins = instr[q]
        if ins[0] == "INC":
            _, i, qp = ins
            if zp[i]:
                zp[i] = False
                seen.clear()
            q = qp
        else:
            _, i, qz, qn = ins
            q = qz if zp[i] else qn

def run_bare_incjz(instr, q0, seeds, horizon):
    """An INC/JZ program compiled to the idempotent encoding, run on
    the BARE machine (no DEC used at all)."""
    m = Bare(["C0", "C1"])
    names = ["C0", "C1"]
    for i, s in enumerate(seeds):
        for _ in range(s):
            m.inc(names[i])
    q = q0
    for step in range(horizon):
        if q == "HALT":
            return "HALT", step
        ins = instr[q]
        if ins[0] == "INC":
            _, i, qp = ins
            m.inc(names[i])
            q = qp
        else:
            _, i, qz, qn = ins
            q = qz if m.jz(names[i]) else qn
    return "RUNS", horizon

def s7():
    print("S7  the collapse: INC + zero-test bare runs vs the quotient decider")
    M_A = {0: ("INC", 0, 0)}
    M_B = {0: ("JZ", 0, "HALT", 1), 1: ("INC", 0, 0)}
    M_C = {0: ("JZ", 1, 1, "HALT"), 1: ("INC", 0, 2), 2: ("JZ", 0, 1, "HALT")}
    M_D = {0: ("JZ", 1, "HALT", 1), 1: ("INC", 0, 0)}
    battery = [
        ("M_A c=(0,0)", M_A, (0, 0), "LOOP"),
        ("M_B c=(0,0)", M_B, (0, 0), "HALT"),
        ("M_C c=(0,3)", M_C, (0, 3), "HALT"),
        ("M_D c=(0,0)", M_D, (0, 0), "HALT"),
        ("M_D c=(0,5)", M_D, (0, 5), "LOOP"),
    ]
    for name, instr, seeds, expect in battery:
        verdict = decide_halting(instr, 0, tuple(s == 0 for s in seeds))
        fate, steps = run_bare_incjz(instr, 0, seeds, horizon=300)
        ok(verdict == expect, f"decider: {name} -> {verdict}")
        if verdict == "HALT":
            ok(fate == "HALT", f"bare idempotent run halts too ({name})")
        else:
            ok(fate == "RUNS", f"bare idempotent run outlives the horizon "
                               f"({name}: certified LOOP by the quotient)")
        print(f"      {name:14s} decider={verdict:4s} bare-run={fate}")
    print("    with no working DEC the construction is INC + zero-test:")
    print("    the growth-machine quotient decides it "
          "(explore_growth_machine.py)")
    print()


if __name__ == "__main__":
    s1()
    s2()
    s3()
    s4()
    s5()
    s6()
    s7()
    print(f"ALL CHECKS PASS: {CHECKS}")
