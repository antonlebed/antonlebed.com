"""
explore_born_at_zero.py -- THE BORN-AT-ZERO NORMAL FORM: what a
reachable configuration of the growing-window machine can hold, exactly
-- and what that buys the decidability conjecture. (Sibling of
explore_decidable_side.py, explore_sqrt_supply.py,
explore_pending_fires.py.)

THE SETTING. The growing-window machine (the class verbatim from
explore_minimal_carrier.py): windows are copies of Z/m_j with moduli
from the supply, appended by GROW with every register born 0 there;
the native ops (add, sub, mul, write-constant) are componentwise; the
one cross-window read is the global 1-bit zero-test; finite control.
The supply law's sublinear side rests on the born-at-zero principle,
so far ARGUED from the op semantics rather than proved: a fresh
window's post-birth content is a function of constants, the frontier
singleton, and its own born-0 registers. This script mechanizes the
principle's exact form and the reduction it buys.

THE NORMAL FORM (the suffix-evaluation theorem, proved by induction on
the op word; this script is its verifier on randomized programs).
Along any run let w_1..w_t be the op word so far. The content of
register i at a window born at time tau with modulus m is

    E_i(w_{tau+1} .. w_t)  mod  m

where E_i is the free evaluation of the suffix over Z from the
all-zero state. Proof shape: reduction mod m is a ring homomorphism,
write-constant commutes with it, GROW never touches an old window, and
the fresh-window singleton is built from write-constant and a register
(1 - ONES) so it introduces no extra case. Consequences: the registers
carry no information beyond the op word -- a window's whole content is
a function of (the suffix since its birth, its own modulus); two
windows with equal age and modulus are identical forever; the
configuration abstracts to (control state, the set of pairs (column
vector mod m, m)) with every op broadcast to all pairs and GROW
inserting the zero pair -- the reset-broadcast structure, with NO rate
hypothesis. The pool of windows is not writable memory; it is a DELAY
LINE of the op stream, sampled mod the supply.

THE REDUCTION (what the normal form buys). After a run's last grow the
whole configuration lives in the finite space (control states) x
prod (Z/m_k)^r, and between grows the machine has no input at all --
so by pigeonhole the run halts, grows again, or repeats a
configuration within that space's size, and a repeat with no
intervening grow is a sound LOOP certificate (the future from an equal
configuration is equal, and the repeated segment contains no grow
since window counts match and are monotone). Hence the plain decider
-- simulate, answer HALT on halt, answer LOOP on the first no-grow
configuration repeat -- is COMPLETE for every run with finitely many
grows, and deciding halting therefore REDUCES to one residual: on a
tame sublinear supply, is "the run grows infinitely often"
semi-decidable (does every forever-growing program admit a finite
certificate)? Certifiability suffices for decidability -- halt, loop
and growth certificates searched in parallel, one always landing --
and any undecidable supply must have uncertifiable forever-growing
programs; whether decidability conversely forces certifiability is
not claimed. Completeness also makes "grows forever" co-semi-decidable
for free: its complement is exactly halt-or-loop, both found by
simulation. The adversarial-supply result
(explore_pending_fires.py) already shows the certificate cannot be
supply-uniform; the rate boundary's universal side is consistent --
there, certifying infinite growth would decide the simulated machine.

THE UNDERCOUNT (a sharpening of the decidable-side mechanism). The
uniform-window repertoire is wider than "a program constant or t mod
m": a uniform window realizes ANY fixed integer polynomial recurrence
in its age -- Fibonacci via (a, b) := (b, a + b), whose zero-set at
modulus m is the multiples of the rank of apparition alpha(m), and
iterated squaring's 2^(2^s), among all others. The bandwidth argument
never used the narrow enumeration -- only that a fixed window's
content evolves inside the finite space (Z/m)^r under the shared word,
which is the normal form itself -- so the freeze reasoning stands on
the wider class unchanged.

THE DESIGN (findings enter by a separate post-run edit; the kills are
frozen as observables).

S1  THE NORMAL FORM, RANDOMIZED. Random programs (random componentwise
    ops, jumps, tests, grows) on the sqrt, successor, and constant
    supplies; at random checkpoint times, every window's actual column
    is compared against the free evaluation of its own suffix replayed
    from all-zero on a fresh single window of the same modulus.
    KILL (prints as MISMATCH): any (program, supply, time, window)
    where the two differ -- the normal form is false.

S2  THE PLAIN DECIDER. A battery: a halting program, a frozen-pulse
    non-halter (finitely many grows), and a forever-growing program.
    Expected: HALT; LOOP certified within the pigeonhole bound;
    NO-CERTIFICATE at the step cap (the residual class, by design).
    KILL (prints as ESCAPE): a finitely-growing non-halting run that
    passes its pigeonhole bound without halting, growing, or
    repeating -- the reduction's completeness is false.
    POSITIVE CONTROL: the halting program must print HALT and the
    pulse must print LOOP before any other verdict is read.

S3  THE FIBONACCI WITNESS. Freeze windows at moduli 2, 3, 4, 5, reset
    (a, b) := (0, 1) uniformly by write-constants, iterate the
    recurrence; record each window's zero-set of a and the global AND.
    Expected: zero-sets are exactly the multiples of alpha(m) = 3, 4,
    6, 5, and the AND fires with period lcm = 60 -- a uniform-window
    signal outside the "constant or t mod m" enumeration.
    KILL: any zero-set not equal to the multiples of its alpha(m).

FINDINGS (entered post-run, from the printed output).

F1  THE NORMAL FORM HOLDS (rule; the theorem's mechanized check).
    5,571 window-checkpoints across 60 random programs on the sqrt,
    successor, and bounded supplies: 0 mismatches between a window's
    actual column and the free evaluation of its own suffix replayed
    from all-zero at its own modulus. The induction proof is the
    claim's ground; this run is its randomized cross-check.

F2  THE PLAIN DECIDER LANDS AS DERIVED (rule for the battery). The
    halting program prints HALT (step 9); the frozen-pulse non-halter
    prints LOOP at step 39, far inside its pigeonhole bound; the
    forever-growing program prints NO-CERTIFICATE at the 20,000-step
    cap -- the residual class, by design. Both positive controls
    passed before the kill lines were read. No ESCAPE: no
    finitely-growing run outlived its pigeonhole bound.

F3  THE FIBONACCI WITNESS PRINTS (observation, the undercount made
    concrete). At frozen moduli 2, 3, 4, 5 the uniform register's
    zero-sets are exactly the multiples of alpha(m) = 3, 4, 6, 5, and
    the global AND fires at ages 60 and 120 alone -- a period-60
    uniform pulse carried by a signal that is neither a program
    constant nor t mod m. The rank of apparition, the quadratic
    corpus's object, is realizable as a growing-window clock.

RUN RECORD: python explore_born_at_zero.py -> S1 5571 checkpoints 0
mismatches; S2 HALT@9 / LOOP@39 / NO-CERTIFICATE@20000; S3 zero-sets
== multiples of alpha at all four moduli, AND at [60, 120]; VERDICT
all pass, exit 0. Wall under 2 s, memory trivial.
"""

import sys

# ---------------------------------------------------------------- VM

ADD, SUB, MUL, WC, GROW, TEST, JMP, HALT = range(8)


def ceil_sqrt(g):
    import math
    s = math.isqrt(g)
    return s if s * s == g else s + 1


SUPPLIES = {
    "sqrt": lambda g: max(2, ceil_sqrt(g)),      # g-th grow: ceil(sqrt g), floored at 2
    "succ": lambda g: g + 1,                     # successor supply
    "const": lambda g: [2, 3, 4, 5][(g - 1) % 4],  # bounded supply
}


class VM:
    """The growing-window machine: componentwise ops, fresh-0 append,
    one global AND-of-zero read, finite (program-counter) control."""

    def __init__(self, prog, supply, r):
        self.prog, self.supply, self.r = prog, supply, r
        self.pc = 0
        self.moduli = []          # modulus per window
        self.births = []          # op-word index at each window's birth
        self.cols = []            # per window: list of r register values
        self.trace = []           # the op word (data-affecting entries)
        self.g = 0                # grows so far
        self.halted = False

    def config(self):
        return (self.pc, tuple(tuple(c) for c in self.cols))

    def step(self):
        if self.halted or not (0 <= self.pc < len(self.prog)):
            self.halted = True
            return
        ins = self.prog[self.pc]
        op = ins[0]
        if op in (ADD, SUB, MUL):
            _, a, b, c = ins
            for j, col in enumerate(self.cols):
                m = self.moduli[j]
                if op == ADD:
                    col[a] = (col[b] + col[c]) % m
                elif op == SUB:
                    col[a] = (col[b] - col[c]) % m
                else:
                    col[a] = (col[b] * col[c]) % m
            self.trace.append(ins)
            self.pc += 1
        elif op == WC:
            _, a, cst = ins
            for j, col in enumerate(self.cols):
                col[a] = cst % self.moduli[j]
            self.trace.append(ins)
            self.pc += 1
        elif op == GROW:
            self.g += 1
            m = self.supply(self.g)
            self.moduli.append(m)
            self.births.append(len(self.trace) + 1)  # born AFTER this op
            self.cols.append([0] * self.r)
            self.trace.append(ins)
            self.pc += 1
        elif op == TEST:
            _, a, target = ins
            bit = all(col[a] == 0 for col in self.cols)
            self.trace.append((TEST,))  # data no-op
            self.pc = target if bit else self.pc + 1
        elif op == JMP:
            self.pc = ins[1]
        else:  # HALT
            self.halted = True


def replay_suffix(trace, birth, m, r):
    """Free evaluation of the op suffix since birth, reduced mod m:
    a fresh single window of modulus m from all-zero."""
    col = [0] * r
    for ins in trace[birth:]:
        op = ins[0]
        if op in (ADD, SUB, MUL):
            _, a, b, c = ins
            if op == ADD:
                col[a] = (col[b] + col[c]) % m
            elif op == SUB:
                col[a] = (col[b] - col[c]) % m
            else:
                col[a] = (col[b] * col[c]) % m
        elif op == WC:
            col[ins[1]] = ins[2] % m
        # GROW after this window's birth, TEST: no effect on it
    return col


# ---------------------------------------------------------------- S1

def s1_normal_form(trials=60, steps=400, r=4, seed=7):
    import random
    rng = random.Random(seed)
    checked = mismatches = 0
    for trial in range(trials):
        sup_name = rng.choice(list(SUPPLIES))
        prog = []
        n = rng.randrange(8, 24)
        for _ in range(n):
            k = rng.random()
            if k < 0.45:
                prog.append((rng.choice((ADD, SUB, MUL)),
                             rng.randrange(r), rng.randrange(r), rng.randrange(r)))
            elif k < 0.60:
                prog.append((WC, rng.randrange(r), rng.randrange(0, 7)))
            elif k < 0.75:
                prog.append((GROW,))
            elif k < 0.88:
                prog.append((TEST, rng.randrange(r), rng.randrange(n)))
            else:
                prog.append((JMP, rng.randrange(n)))
        vm = VM(prog, SUPPLIES[sup_name], r)
        checkpoints = sorted(rng.sample(range(1, steps), 12))
        for t in range(steps):
            vm.step()
            if vm.halted:
                break
            if t in checkpoints:
                for j in range(len(vm.cols)):
                    want = replay_suffix(vm.trace, vm.births[j], vm.moduli[j], r)
                    checked += 1
                    if want != vm.cols[j]:
                        mismatches += 1
                        print(f"S1 MISMATCH trial={trial} supply={sup_name} "
                              f"t={t} window={j} m={vm.moduli[j]} "
                              f"actual={vm.cols[j]} replay={want}")
    print(f"S1 normal form: {checked} window-checkpoints across {trials} "
          f"random programs, {mismatches} mismatches")
    return mismatches == 0


# ---------------------------------------------------------------- S2

def plain_decider(prog, supply, r, cap):
    """Simulate; HALT on halt, LOOP on first no-grow config repeat,
    NO-CERTIFICATE at the step cap. Returns (verdict, step, bound_ok)."""
    vm = VM(prog, supply, r)
    seen = {}
    last_grow_step = 0
    space_after_grow = None
    for t in range(cap):
        cfg = vm.config()
        if cfg in seen:
            return "LOOP", t, True
        seen[cfg] = t
        g_before = vm.g
        vm.step()
        if vm.halted:
            return "HALT", t, True
        if vm.g != g_before:
            seen.clear()          # repeats only count with no grow between
            last_grow_step = t
            space = len(vm.prog)
            for m in vm.moduli:
                space *= m ** r
            space_after_grow = space
        elif space_after_grow is not None and t - last_grow_step > space_after_grow + 1:
            return "ESCAPE", t, False   # past pigeonhole bound: kills T2
    return "NO-CERTIFICATE", cap, True


def s2_decider():
    r = 3
    # halting program: grow 3, inc a 5 times, halt
    p_halt = [(GROW,), (GROW,), (GROW,), (WC, 1, 1)] + \
             [(ADD, 0, 0, 1)] * 5 + [(HALT,)]
    # frozen pulse: grow 3 windows, ONES := 1, loop {a := a + ONES; test}
    p_pulse = [(GROW,), (GROW,), (GROW,), (WC, 1, 1),
               (ADD, 0, 0, 1), (TEST, 0, 4), (JMP, 4)]
    # forever-growing: loop {grow; a := a + ONES}
    p_grow = [(WC, 1, 1), (GROW,), (ADD, 0, 0, 1), (JMP, 1)]
    ok = True
    for name, prog, expect in (("halting", p_halt, "HALT"),
                               ("frozen-pulse", p_pulse, "LOOP"),
                               ("forever-growing", p_grow, "NO-CERTIFICATE")):
        verdict, t, bound_ok = plain_decider(prog, SUPPLIES["const"], r, cap=20000)
        print(f"S2 {name}: {verdict} at step {t}"
              f"{'' if bound_ok else '  ** PAST PIGEONHOLE BOUND **'}")
        ok = ok and verdict == expect and bound_ok
    return ok


# ---------------------------------------------------------------- S3

def rank_of_apparition(m):
    a, b, n = 0, 1, 0
    while True:
        a, b = b, (a + b) % m
        n += 1
        if a % m == 0:
            return n


def s3_fibonacci():
    r = 3   # a, b, tmp
    moduli = [2, 3, 4, 5]
    prog = [(GROW,)] * 4 + [(WC, 0, 0), (WC, 1, 1)]
    vm = VM(prog, lambda g: moduli[g - 1], r)
    while vm.pc < len(prog) and not vm.halted:
        vm.step()
    N = 130
    zero_ages = [[] for _ in moduli]
    and_fires = []
    for s in range(1, N + 1):
        # (a, b) := (b, a + b) componentwise: tmp := a; a := b; b := tmp + b
        for ins in ((WC, 2, 0), (ADD, 2, 2, 0), (WC, 0, 0), (ADD, 0, 0, 1),
                    (ADD, 1, 1, 2)):
            vm.prog = [ins]
            vm.pc = 0
            vm.step()
        for j, col in enumerate(vm.cols):
            if col[0] == 0:
                zero_ages[j].append(s)
        if all(col[0] == 0 for col in vm.cols):
            and_fires.append(s)
    ok = True
    for j, m in enumerate(moduli):
        alpha = rank_of_apparition(m)
        want = [s for s in range(1, N + 1) if s % alpha == 0]
        good = zero_ages[j] == want
        ok = ok and good
        print(f"S3 m={m}: alpha={alpha}, zero-set "
              f"{'== multiples of alpha' if good else 'KILL: ' + str(zero_ages[j][:8])}")
    print(f"S3 global AND fires at {and_fires} "
          f"(period 60 expected: {'yes' if and_fires == [60, 120] else 'NO'})")
    return ok and and_fires == [60, 120]


if __name__ == "__main__":
    ok1 = s1_normal_form()
    ok2 = s2_decider()
    ok3 = s3_fibonacci()
    print(f"VERDICT: S1 {'pass' if ok1 else 'KILL'}, "
          f"S2 {'pass' if ok2 else 'KILL'}, S3 {'pass' if ok3 else 'KILL'}")
    sys.exit(0 if (ok1 and ok2 and ok3) else 1)
