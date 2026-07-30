"""
THE RESET CORNER -- the forgetful borrow resolved at the knife edge.

The archimedean dial (explore_archimedean_dial.py) located Turing-completeness
at a KNIFE EDGE: universality = an exact ZERO-TEST + a BORROW, and the
tower owns the zero-test natively while deleting the borrow (the
archimedean place). It left ONE corner open: the borrow is graded, and
the FORGETFUL borrow -- RESET (clear a whole window, the general overflow)
-- was not resolved WITH the tower's native zero-test. The dial's reset
row (DFS 1998) is reset-net data: INC + bounded-DEC + reset, NO zero-test.
The OPEN question is the other combination:

    INC + native ZERO-TEST + RESET, NO decrement -- universal or decidable?

If decidable, the tower admits a genuine intermediate archimedean grade: a
SAFE forgetful borrow, a safe-destruction knob (wipe a window, build on
it). If universal, ANY borrow flips the knife edge and it is even sharper.

THE ANSWER (rule, proved + verified S1-S5): DECIDABLE, and stronger --
FINITE-STATE (regular). A borrow grants computational power only if it is
VALUE-READING. RESET is value-BLIND: it zeroes a counter unconditionally,
reading nothing on the way down, so a counter's numeric value is never
observable beyond its zero-pattern. The map alpha(q, v) = (q, sign(v)) is
a BISIMULATION for INC / RESET / ZERO-TEST -- every transition's branch and
result-sign depend only on (control, zero-pattern), never on the value --
so the machine is bisimilar to a DFA on the finite set Q x {0,+}^k
(|states| = |Q| * 2^k). Halting is finite-graph reachability: decidable,
and EXACTLY (bisimulation => the quotient decider is sound AND complete),
settling programs whose naive forward simulation loops forever.

THE KNIFE EDGE, REFINED. The dangerous borrow is not "any down-move" -- it
is the REMEMBERING (value-reading) borrow specifically. The plain
DECREMENT reads the value as it descends (v_i -> v_i - 1 flips the sign iff
v_i was exactly 1), which un-quotients the value and creates unbounded
observable memory; restore it and the SAME sign-quotient goes unsound
(Minsky halts-iff-even: c0 = 2 HALT, c0 = 3 LOOP from the shared node
(control, c0 = +)). The forgetful borrow is a CLIFF DOWN to finite-state,
not the first rung up. "Safe destruction" is real and total: the tower can
wipe a window freely without importing one bit of undecidability.

THE RESET-NETS READING (synthesis, cited). Reset is INERT ALONE. Reset
nets (DFS 1998: INC + bounded-DEC + reset, no zero-test) have UNDECIDABLE
reachability, but the undecidability is JOINT, not reset's alone and not
the decrement's alone: a plain VAS (INC + bounded-DEC, no reset, no
zero-test) has DECIDABLE reachability (Mayr/Kosaraju/Leroux), so it is the
reset that flips it undecidable -- yet strip the decrement (keep the reset
AND add a zero-test, which is MORE than a reset net has) and the whole
thing collapses to finite-state (this script). So neither the reset nor
the plain decrement carries undecidability by itself; the climb needs a
value-reading down-move (the bounded decrement / token consumption)
PRESENT, and reset can amplify one but never supplies it. This isolates
the roles: the value-reading borrow is the active ingredient, reset a
value-blind amplifier that is nothing on its own.

FINDINGS (run record below; every section asserts).

1. THE COLLAPSE (rule, proved + verified S1). For INC / RESET / ZERO-TEST
   (no decrement), alpha(q, v) = (q, sign(v)) is a bisimulation: for a
   battery of programs, concrete runs launched from many value-vectors
   sharing one zero-pattern trace IDENTICAL (control, sign) trajectories,
   and each matches the purely abstract machine that steps on signs alone.
   The corner is finite-state: bisimilar to a DFA on Q x {0,+}^k.

2. THE VALUE-BLIND DOWN-FLIP (rule, verified S2). RESET produces sign
   down-flips (+ -> 0) that a multiply-only world cannot -- but the
   resulting sign is INDEPENDENT of the pre-value (RESET a counter holding
   1, 2, 5, or 100 -> sign 0 every time). The DECREMENT's sign-result is a
   FUNCTION of the value (1 -> 0 flips, 2/5/100 -> + do not). The
   decrement reads the value on descent; reset does not. Down-flips per se
   are harmless; VALUE-READING down-flips are the borrow.

3. THE EXACT DECIDER (rule, proved + verified S3). The quotient decider on
   Q x {0,+}^k (node = (control, sign-pattern); a revisited node certifies
   an infinite loop) decides halting EXACTLY -- sound AND complete by the
   bisimulation -- including reset-oscillator programs whose naive forward
   simulation never terminates (counter cycles 0/1, control never halts).

4. THE DECREMENT BREAKS THE QUOTIENT (rule, verified S4). Restore a plain
   decrement (Minsky halts-iff-even): c0 = 2 HALTs, c0 = 3 LOOPs, yet both
   start at the SAME abstract node (q0, sign c0 = +). A sign-only decider
   sees one node and must answer once -- wrong for one input. Reset
   PRESERVES the quotient (value-blind); the decrement DESTROYS it
   (value-reading). reset != decrement on the dial.

5. THE BOUNDED-THRESHOLD GENERALIZATION (rule, proved + verified S5). Even
   with threshold tests up to a constant T (test v_i >= t, t <= T), the
   corner stays finite-state: min(v_i, T) is a bisimulation invariant
   (saturating INC: min(v+1, T) is a function of min(v, T); RESET -> 0;
   JGE reads min(v, T) >= t exactly for t <= T), quotient Q x {0..T}^k.
   The zero-test is the T = 1 case. The decider settles the loopers.

SCOPE + HONESTY. The finite-state collapse (findings 1, 3, 5) is
elementary once seen: with no decrement, nothing reads a counter's value
beyond its zero-pattern (or its min-with-T under bounded tests), so the
model is a finite automaton -- this is folklore for counter machines
without decrement. The CONTRIBUTION is the LOCATION on the archimedean
dial: the reset corner resolves to finite-state (the safe forgetful
borrow), the VALUE-READING / VALUE-BLIND distinction that sharpens the
knife edge (the dangerous borrow is the remembering one), and the reading
that reset is INERT ALONE -- reset-nets' undecidability is a JOINT
reset+decrement effect (a VAS's reachability is decidable, adding reset
makes it undecidable, DFS 1998; removing the decrement collapses to
finite-state), so neither the reset nor the plain decrement carries
undecidability by itself; the climb needs a value-reading move present,
which reset amplifies but never supplies. Undecidability cannot be run;
the reset-nets and Minsky facts are CITED (DFS 1998; Minsky 1967). What is
run-verified: the bisimulation (finding 1), the value-blind down-flip
census (finding 2), the exact decider incl. loopers (finding 3), the
quotient's unsoundness under a restored decrement (finding 4), and the
bounded-threshold invariant + decider (finding 5).

PREDICTIONS (fixed before the run; adjudicated by asserts only):
  PR1 THE COLLAPSE ......... alpha is a bisimulation; concrete runs from
      value-vectors sharing a zero-pattern trace identical (control, sign)
      trajectories, matching the abstract machine. Finite-state.
  PR2 VALUE-BLIND DOWN-FLIP  RESET down-flips but sign-result constant over
      pre-values {1,2,5,100}; DEC sign-result varies. Multiply-only: 0
      down-flips; reset-oscillator: many.
  PR3 EXACT DECIDER ........ quotient decider correct on the battery incl.
      >= 1 program with no terminating forward simulation.
  PR4 DECREMENT BREAKS IT .. Minsky halts-iff-even: c0=2 HALT, c0=3 LOOP
      from the shared node (q0, +). Sign-quotient unsound.
  PR5 BOUNDED-THRESHOLD .... min(v,T) invariant; decider works with tests
      up to T; T=1 recovers the sign model.

RUN RECORD (python prime/code/explore_reset_corner.py; <1 s; trivial
memory; 1057 checks). SLATE PR1-PR5 all CONFIRMED, no misses. S1: eight
sign-classes across four programs, each collapsing many value-vectors to
one (control, sign) trajectory that matches the abstract machine (RC1 c0=+
: 5 vectors -> 1 trajectory of length 4; the loopers RC2/RC3 agree to the
400-step cap). S2: RESET over {1,2,5,100} -> sign {0} (constant); DEC ->
{0,1} (varies); multiply-only RC2 census up=1/down=0, reset-oscillator RC3
up=167/down=167 (value-blind down-flips). S3: decider exact on the 5-program
battery, 2 of 5 (RC2, RC3) loop forever in naive simulation and are settled
LOOP. S4: EVENODD c0=2 -> HALT, c0=3 -> LOOP?, shared abstract node
(0,(1,)); parity verdict correct c0=0..11. S5: min(v,T) invariant verified
c=0..199 for saturating INC / reset / every test t<=T=3; bounded decider
BT1 HALT, BT2 LOOP on Q x {0..3}^k; T=1 recovers the sign bit.
No pre-run adjudication drafted; verdicts frozen in code, numbers copied
from output.
"""

CHECKS = 0


def ok(cond, msg=""):
    global CHECKS
    if not cond:
        raise AssertionError("CHECK FAILED: " + msg)
    CHECKS += 1


# ------------------------------------------------------------------ #
# The reset-corner counter machine.
#   Control 0..Q-1 plus "HALT".  instr[q] one of:
#     ("INC",   i, q')             counter i += 1,  goto q'
#     ("RESET", i, q')             counter i := 0,  goto q'
#     ("JZ",    i, q_zero, q_nz)   if counter i == 0 goto q_zero else q_nz
#     ("DEC",   i, q')             counter i -= 1 (>=0)  -- MINSKY ONLY (S4)
#     ("JGE",   i, t, q_ge, q_lt)  if counter i >= t     -- BOUNDED TEST (S5)
# No DEC in the reset corner; it appears only in S4 to break the quotient.
# ------------------------------------------------------------------ #

def sign(c):
    return tuple(0 if x == 0 else 1 for x in c)


def concrete_step(instr, q, c):
    ins = instr[q]
    op = ins[0]
    if op == "INC":
        _, i, qp = ins
        c = list(c); c[i] += 1; return qp, tuple(c)
    if op == "RESET":
        _, i, qp = ins
        c = list(c); c[i] = 0; return qp, tuple(c)
    if op == "JZ":
        _, i, qz, qn = ins
        return (qz if c[i] == 0 else qn), tuple(c)
    if op == "DEC":
        _, i, qp = ins
        c = list(c); c[i] = max(0, c[i] - 1); return qp, tuple(c)
    if op == "JGE":
        _, i, t, qge, qlt = ins
        return (qge if c[i] >= t else qlt), tuple(c)
    raise ValueError("bad op " + op)


def abstract_step(instr, q, s):
    """Step on the ZERO-PATTERN alone. Defined for INC/RESET/JZ only --
    a DEC has no well-defined sign action (that is the whole point)."""
    ins = instr[q]
    op = ins[0]
    if op == "INC":
        _, i, qp = ins
        s = list(s); s[i] = 1; return qp, tuple(s)
    if op == "RESET":
        _, i, qp = ins
        s = list(s); s[i] = 0; return qp, tuple(s)
    if op == "JZ":
        _, i, qz, qn = ins
        return (qz if s[i] == 0 else qn), tuple(s)
    raise ValueError("op %s not sign-abstractable (a value-reading move)" % op)


# ------------------------------------------------------------------ #
print("S1 -- THE COLLAPSE (alpha is a bisimulation; finite-state)")

# Reset-corner programs (no DEC). Verdicts implied by the abstract machine.
RC1 = {0: ("JZ", 0, "HALT", 1),                 # nonzero -> wipe -> zero -> halt
       1: ("RESET", 0, 0)}                       # ALWAYS halts (<=2 ctl steps)
RC2 = {0: ("INC", 0, 1),                          # grows, never zero again
       1: ("JZ", 0, "HALT", 0)}                   # LOOPS forever
RC3 = {0: ("INC", 0, 1), 1: ("RESET", 0, 2),      # reset oscillator: sign
       2: ("JZ", 0, 0, "HALT")}                   # cycles + -> 0 -> + ; LOOPS
RC4 = {0: ("RESET", 1, 1),                         # wipe c1, then read it zero
       1: ("JZ", 1, "HALT", 2),
       2: ("INC", 1, 1)}                           # HALTS regardless of start


def concrete_trajectory(instr, q0, c0, limit=400):
    q, c = q0, tuple(c0)
    traj = []
    for _ in range(limit):
        traj.append((q, sign(c)))
        if q == "HALT":
            break
        q, c = concrete_step(instr, q, c)
    return traj


def abstract_trajectory(instr, q0, s0, limit=400):
    q, s = q0, tuple(s0)
    traj = []
    for _ in range(limit):
        traj.append((q, tuple(s)))
        if q == "HALT":
            break
        q, s = abstract_step(instr, q, s)
    return traj


# For each program and each zero-pattern class, many value-vectors -> one
# (control, sign) trajectory, matching the abstract machine.
bisim_cases = [
    ("RC1 c0=+", RC1, 0, [[1], [2], [5], [100], [999]]),
    ("RC1 c0=0", RC1, 0, [[0]]),
    ("RC2 c0=+", RC2, 0, [[1], [3], [42]]),
    ("RC2 c0=0", RC2, 0, [[0]]),
    ("RC3 c0=+", RC3, 0, [[1], [7], [50]]),
    ("RC3 c0=0", RC3, 0, [[0]]),
    ("RC4 c=(+,+)", RC4, 0, [[1, 1], [3, 9], [8, 100]]),
    ("RC4 c=(0,+)", RC4, 0, [[0, 4], [0, 77]]),
]
for name, instr, q0, vecs in bisim_cases:
    trajs = [concrete_trajectory(instr, q0, v) for v in vecs]
    ref = trajs[0]
    for t in trajs[1:]:
        ok(t == ref, "concrete trajectories agree within a sign-class: " + name)
    abst = abstract_trajectory(instr, q0, sign(vecs[0]))
    ok(abst == ref, "concrete (control,sign) run matches abstract machine: " + name)
    print("  %-14s %d value-vectors -> 1 (control,sign) trajectory, len %d"
          % (name, len(vecs), len(ref)))
# The whole abstract state space is finite:
for name, instr in (("RC1", RC1), ("RC2", RC2), ("RC3", RC3), ("RC4", RC4)):
    ncount = 1 + max(ins[1] for ins in instr.values())
    nctl = len(instr)
    ok(nctl * (2 ** ncount) < 10 ** 6, "finite abstract state space " + name)
print("  finite-state: bisimilar to a DFA on Q x {0,+}^k")
print()


# ------------------------------------------------------------------ #
print("S2 -- THE VALUE-BLIND DOWN-FLIP (reset forgets, decrement reads)")


def after_op_sign(op, val):
    c = val
    if op == "RESET":
        c = 0
    elif op == "DEC":
        c = max(0, c - 1)
    elif op == "INC":
        c = c + 1
    return 0 if c == 0 else 1


pre_values = [1, 2, 5, 100]
reset_signs = {after_op_sign("RESET", v) for v in pre_values}
dec_signs = {after_op_sign("DEC", v) for v in pre_values}
ok(reset_signs == {0},
   "RESET is value-blind: sign result constant (0) over pre-values")
ok(dec_signs == {0, 1},
   "DEC is value-reading: sign result varies with pre-value (1->0, else +)")
print("  RESET over pre-values %s -> signs %s (constant: value-blind)"
      % (pre_values, sorted(reset_signs)))
print("  DEC   over pre-values %s -> signs %s (varies: value-reading)"
      % (pre_values, sorted(dec_signs)))


def sign_flip_census(instr, q0, c0, limit=5000):
    q, c = q0, tuple(c0)
    last = sign(c)
    up = down = 0
    for _ in range(limit):
        if q == "HALT":
            break
        q, c = concrete_step(instr, q, c)
        s = sign(c)
        for i in range(len(c)):
            if last[i] == 0 and s[i] == 1:
                up += 1
            if last[i] == 1 and s[i] == 0:
                down += 1
        last = s
    return up, down


mo_up, mo_down = sign_flip_census(RC2, 0, [0], limit=500)   # INC-only spine
rc_up, rc_down = sign_flip_census(RC3, 0, [0], limit=500)   # reset oscillator
ok(mo_down == 0, "multiply-only spine (RC2): zero sign down-flips")
ok(rc_down >= 10, "reset oscillator (RC3): many sign down-flips")
print("  multiply-only RC2: up=%d down=%d (no borrow, never down-flips)"
      % (mo_up, mo_down))
print("  reset-osc     RC3: up=%d down=%d (reset down-flips, but value-blind)"
      % (rc_up, rc_down))
print()


# ------------------------------------------------------------------ #
print("S3 -- THE EXACT DECIDER (sound AND complete on the sign quotient)")


def decide_reset_corner(instr, q0, c0):
    """Walk the finite quotient Q x {0,+}^k on signs. Deterministic; a
    revisited node certifies an infinite loop. Exact by the bisimulation."""
    q, s = q0, sign(c0)
    seen = set()
    while True:
        if q == "HALT":
            return "HALT"
        if (q, s) in seen:
            return "LOOP"
        seen.add((q, s))
        q, s = abstract_step(instr, q, s)


def run_forward(instr, q0, c0, limit=200000):
    q, c = q0, tuple(c0)
    for step in range(limit):
        if q == "HALT":
            return "HALT", step
        q, c = concrete_step(instr, q, c)
    return "LOOP?", limit


s3_battery = [
    ("RC1 c0=(5)", RC1, 0, [5], "HALT"),
    ("RC1 c0=(0)", RC1, 0, [0], "HALT"),
    ("RC2 c0=(0)", RC2, 0, [0], "LOOP"),   # naive sim never halts
    ("RC3 c0=(0)", RC3, 0, [0], "LOOP"),   # reset oscillator, never halts
    ("RC4 c=(9,3)", RC4, 0, [9, 3], "HALT"),
]
n_nonterm = 0
for name, instr, q0, c0, expect in s3_battery:
    verdict = decide_reset_corner(instr, q0, c0)
    fwd, steps = run_forward(instr, q0, c0, limit=5000)
    ok(verdict == expect, "decider verdict %s for %s" % (verdict, name))
    if fwd == "HALT":
        ok(verdict == "HALT", "decider matches terminating sim: " + name)
    if verdict == "LOOP":
        ok(fwd == "LOOP?", "decider LOOP where naive sim never ends: " + name)
        n_nonterm += 1
    print("  %-13s decider=%-4s  naive-sim=%s" % (name, verdict, fwd))
ok(n_nonterm >= 1, "at least one non-terminating program decided as LOOP")
print("  reset-corner halting DECIDED exactly (%d of %d loop forever in sim)"
      % (n_nonterm, len(s3_battery)))
print()


# ------------------------------------------------------------------ #
print("S4 -- THE DECREMENT BREAKS THE QUOTIENT (Minsky halts-iff-even)")

# A one-counter Minsky machine that HALTS iff c0 is EVEN. Two counters'
# worth of control; DEC is the value-reading borrow.
EVENODD = {0: ("JZ", 0, "HALT", 1),   # c0==0 (even reached) -> HALT
           1: ("DEC", 0, 2),          # c0 -= 1
           2: ("JZ", 0, 3, 4),        # now zero (was odd) -> sink ; else on
           3: ("INC", 0, 3),          # non-halting sink (odd case)
           4: ("DEC", 0, 0)}          # c0 -= 1, loop


def run_minsky(instr, q0, c0, limit=200000):
    q, c = q0, tuple(c0)
    for _ in range(limit):
        if q == "HALT":
            return "HALT"
        q, c = concrete_step(instr, q, c)
    return "LOOP?"


fate2 = run_minsky(EVENODD, 0, [2])
fate3 = run_minsky(EVENODD, 0, [3])
ok(fate2 == "HALT", "Minsky EVENODD c0=2 halts (even)")
ok(fate3 == "LOOP?", "Minsky EVENODD c0=3 loops (odd)")
# both start at the SAME abstract node -- the sign-quotient cannot separate:
node2 = (0, sign((2,)))
node3 = (0, sign((3,)))
ok(node2 == node3 == (0, (1,)), "c0=2 and c0=3 share the abstract node (q0,+)")
ok(fate2 != fate3, "yet their fates differ -> a sign-only decider is UNSOUND")
# sanity: EVENODD halts iff even, over a range
for v in range(0, 12):
    exp = "HALT" if v % 2 == 0 else "LOOP?"
    ok(run_minsky(EVENODD, 0, [v]) == exp, "EVENODD parity at c0=%d" % v)
print("  c0=2 -> %s , c0=3 -> %s , shared abstract node %s"
      % (fate2, fate3, str(node2)))
print("  the plain decrement un-quotients the value: reset PRESERVES the")
print("  quotient (value-blind), the decrement DESTROYS it (value-reading)")
print()


# ------------------------------------------------------------------ #
print("S5 -- THE BOUNDED-THRESHOLD GENERALIZATION (still finite-state)")

T = 3  # largest constant any test compares against


def capped(c, cap):
    return tuple(min(x, cap) for x in c)


# min(v,T) is a bisimulation invariant under saturating INC / RESET / JGE:
for c in range(0, 200):
    # saturating INC: min(v+1,T) is a FUNCTION of min(v,T)
    ok(min(c + 1, T) == min(min(c, T) + 1, T), "saturating INC invariant")
    # RESET always -> 0
    ok(min(0, T) == 0, "reset invariant")
    # every test t<=T reads min(v,T) exactly
    for t in range(1, T + 1):
        ok((c >= t) == (min(c, T) >= t), "JGE t=%d reads min(v,T)" % t)


def capped_step(instr, q, c, cap):
    ins = instr[q]
    op = ins[0]
    if op == "INC":
        _, i, qp = ins
        c = list(c); c[i] = min(c[i] + 1, cap); return qp, tuple(c)
    if op == "RESET":
        _, i, qp = ins
        c = list(c); c[i] = 0; return qp, tuple(c)
    if op == "JGE":
        _, i, t, qge, qlt = ins
        return (qge if c[i] >= t else qlt), tuple(c)
    raise ValueError("bad op " + op)


def decide_bounded(instr, q0, c0, cap):
    q, c = q0, capped(c0, cap)
    seen = set()
    while True:
        if q == "HALT":
            return "HALT"
        if (q, c) in seen:
            return "LOOP"
        seen.add((q, c))
        q, c = capped_step(instr, q, c, cap)


# a program that needs to see the counter reach 3 (a genuine threshold test)
BT1 = {0: ("JGE", 0, 3, "HALT", 1), 1: ("INC", 0, 0)}   # counts to 3, HALTS
BT2 = {0: ("JGE", 0, 3, "HALT", 1),                       # reset before it
       1: ("INC", 0, 2), 2: ("RESET", 0, 0)}              # ever reaches 3: LOOP
bt_battery = [("BT1 c0=(0)", BT1, 0, [0], "HALT"),
              ("BT2 c0=(0)", BT2, 0, [0], "LOOP")]
for name, instr, q0, c0, expect in bt_battery:
    verdict = decide_bounded(instr, q0, c0, T)
    ok(verdict == expect, "bounded decider %s for %s" % (verdict, name))
    print("  %-13s decider=%s (quotient Q x {0..%d}^k)" % (name, verdict, T))
# T=1 recovers the pure sign model: JGE t=1 is exactly the zero-test negated
ok(min(5, 1) == 1 and min(0, 1) == 0, "T=1 caps to the sign bit {0,+}")
print("  T=1 recovers the sign model; the zero-test is the T=1 threshold")
print()


print("ALL CHECKS PASSED:", CHECKS)
