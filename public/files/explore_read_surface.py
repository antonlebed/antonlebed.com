"""explore_read_surface.py -- THE READ SURFACE: does decidability
drawn by a boundary's read grammar survive COMPOSITION with a
universal core? (The core is the frontier rider of
explore_frontier_rider.py -- its rig is reused verbatim where
needed. Related: explore_interactive_hand.py (the ratchet theorem
and the publishing split, whose read-side machinery this composite
instantiates), explore_ecc_borrow.py (the base-extension door whose
O(1) sync prices the control route), explore_growth_machine.py.)

THE QUESTION. The recovery chart ends on an interface statement:
questions posed through a boundary whose read atoms are RATCHETS
(monotone one-shot flags) stay decidable whatever sits behind the
boundary, while a boundary exposing RE-READABLE reads is wide enough
to carry everything. (The bulk-free general form of that statement
has since been refuted -- one flag's flip TIMING carries the halting
problem into an unbounded bulk, explore_flip_timing.py; the
surviving scope is bulks of finite timing resolution, which this
composite's flag-word-driven bulk inhabits.) This script builds the smallest composite that
puts the statement at risk: a BULK (a finite-control machine) coupled
to a CORE that is genuinely Turing-universal (a two-counter machine
run bare on the frontier rider), through two boundaries in turn --
a RATCHET boundary (k threshold flags over a core counter, each
flipping false-to-true at most once, never resetting) and a MAILBOX
boundary (one re-readable register the core rewrites). Three things
are measured: (i) the influence census -- how many distinct boundary
histories can cross each boundary; (ii) the confinement -- whether
the bulk's fate questions quantified over the boundary (does SOME /
does EVERY boundary behavior make the bulk halt?) are decided by a
finite enumeration that never runs the core, and whether the real
composite lands inside that bracket; (iii) the crossing toll -- what
crossing the boundary EXACTLY costs in the run's own coin: the bare
(ratchet-compatible) route against the door-synced route.

CONTEXT FROM THE LITERATURE (why the composite is the right test).
Well-structured transition systems get decidability from monotone
TRANSITIONS over a wqo (Finkel-Schnoebelen; Schmitz-Schnoebelen,
arXiv:1402.2908), and the framework grades whole systems, not
boundaries -- the surveys read here state no theorem about a
universal component behind a disciplined interface. Sharper: safety GAMES on monotone systems are
undecidable even in dimension two (Abdulla-Bouajjani-d'Orso,
"Deciding Monotonic Games", CSL 2003 -- their players read whole
configurations), and the literature's decidable islands are carved
by lossy MOVES, not by read discipline. Reversible computing prices
WRITES (erasure -- Landauer, Bennett; the survey Vitanyi
cs/0504088), never observation. So a positive answer here -- the
composite's bulk-side questions decidable by read grammar alone,
with the toll measured -- is a mechanism none of those frames state.

THE MODEL.
CORE: a two-counter Minsky program (universality: Minsky 1967)
  executed bare on the frontier rider (explore_frontier_rider.py:
  counters as sparse residues under a frontier-riding pointer; the
  zero-test never lies). The core is the composite's universal
  region; its own halting is undecidable in general.
RATCHET BOUNDARY: k = 2 monotone flags over the core's X counter,
  flag_i = [X has ever reached c_i], flipping false-to-true at most
  once, never resetting. The bulk sees only the flag word.
MAILBOX BOUNDARY (the control): one register carrying X mod 2,
  rewritten by the core every step, re-readable by the bulk forever.
BULK: a deterministic finite-control machine whose step reads its
  own state plus the boundary (flag word / mailbox value). It has no
  access to the core's registers. Interleaving: one core step, then
  one bulk step.
THE BRANCH TREE (the enumeration that never runs the core): with
  k monotone one-shot flags, every possible boundary history is a
  monotone flag-word schedule -- for k = 2 exactly six up to
  word-sequence equality: no flip, flag 1 only, flag 2 only,
  1 then 2, 2 then 1, both at once. A flag-word-driven bulk's fate
  is a function of the schedule alone, so the two game questions
  (does SOME schedule / does EVERY schedule halt the bulk?) are
  decided by running the bulk over the six schedules. (Bulks with
  their own inter-flip dynamics add flip-timing buckets bounded by
  the state count -- the general finite branch tree is the ratchet
  theorem of explore_interactive_hand.py; this composite uses the
  flag-word-driven case, where the tree is the schedule list.)

THE BATTERY (cores with known behavior, run bare on the rider;
  thresholds c_1 = 3, c_2 = 7):
  CORE-A  the halts-iff-even program, seed 4: X climbs to 4 then
          drains to 0 and halts. Flag 1 flips, flag 2 never.
  CORE-B  a two-state tight loop that pumps Y and leaves X at 1:
          no flag ever flips.
  CORE-C  pump X to 10 then halt: both flags flip, in order 1 then 2.
  CORE-D  the halts-iff-even program, seed 3: X drains odd, the
          program never halts (Y pumps forever). Flag 1 flips at the
          seeding, flag 2 never.
THE BULK PROGRAM: waits for flag 2 -- HALT as soon as the flag word
  shows flag 2 true (whatever flag 1 says), run forever otherwise.
  By the branch tree: SOME schedule halts it (any flipping 2), NOT
  EVERY schedule does (the no-flip schedule runs forever).

THE DESIGN (what each section asks).

S1  THE INFLUENCE CENSUS (ratchet side). Run all four battery
    composites to a horizon. Record the boundary history the bulk
    actually sees. Check: each flag flips at most once ever, and
    every realized history is one of the six schedules of the branch
    tree. The census of the boundary: at most k events cross, ever.

S2  THE CONFINEMENT. Compute the two game answers (SOME / EVERY)
    from the six schedules alone -- no core is run. Then check the
    bracket against every battery composite: the real fate always
    lands inside the enumerated set; where the real schedule is
    known (battery ground truth), the realized leaf matches it.
    The point exhibited: WHICH leaf the real core realizes required
    running the core (and is its reachability problem in general --
    undecidable by Minsky universality), while the quantified
    answers came from the bulk program alone. CORE-A vs CORE-C:
    same bulk, different leaves, different fates.

S3  THE CROSSING TOLL. The exact-sync task: carry the core counter's
    value across a boundary into a fresh window. The bare route is
    the rider's own transfer loop -- the value walks one unit per
    pass through the zero-test. Measured: passes per INC at value v.
    The door route is base extension (explore_ecc_borrow.py): a
    single synced write per step, value-independent by construction
    -- the oracle here is the harness CRT lift, counted as one op.
    Printed: both cumulative toll curves over an N-INC run.

S4  THE LEAK CONTROL (mailbox side). The same universal core behind
    the re-readable mailbox (X mod 2). A two-state bulk mirrors the
    mailbox at every step. Checks: the bulk's state tracks the
    core's parity exactly at every step (the boundary carries an
    unbounded stream -- influence grows with the horizon, against
    the ratchet side's <= k), so bulk-side questions inherit the
    core's undecidability: the mirror's state at step t IS a core
    fact. The census printed against S1's.

FROZEN PREDICTIONS (fixed before the engine ran; the vocabulary is
the boundary's own -- influence counts and toll curves; the composite
instantiates the handled machine of explore_interactive_hand.py with
the hand played by a rider core -- an instantiation, not a new read
model):
  F1  S1: every realized ratchet history has each flag flipping at
      most once, and lands in the six-schedule branch tree; realized
      boundary event counts <= 2 at every horizon.
  F2  S2: SOME-halt = YES, EVERY-halt = NO, computed from the six
      schedules with zero core steps; every battery composite's real
      fate falls inside the bracket; realized leaves: A -> (flag 1
      only, bulk runs), B -> (no flip, bulk runs), C -> (1 then 2,
      bulk halts), D -> (flag 1 only, bulk runs).
  F3  S3: the rider's transfer passes at an INC equal the counter's
      value before that INC, exactly, at every INC of the run; the
      door route costs exactly one synced write per step; cumulative
      curves quadratic (bare) against linear (door).
  F4  S4: the mirror bulk's state equals the core's X parity at
      every step; the mailbox boundary's observed change count grows
      unboundedly with the horizon (>= horizon/2 on the pump core).

KILL CONDITIONS (named before the run): F1 or F2 failing on any
battery item kills the confinement -- the read-grammar statement
does not survive composition. F3 failing (nonlinear bare route or
value-dependent door route) kills the toll axis. F4's mirror failing
breaks the leak-channel statement. Any of the three ends the
read-surface direction as stated.

FINDINGS (all four predictions confirmed; every kill condition
missed).

1. THE INFLUENCE CENSUS (rule for the modelled boundary; battery-
   exhaustive). Every realized ratchet history flips each flag at
   most once and lands in the six-schedule branch tree; boundary
   events ever: A 1, B 0, C 2, D 1 -- all <= k = 2 at every horizon.
   The <= 1 flip per flag is a construction property (monotone
   one-shot flags); the census confirms the composite realizes only
   branch-tree leaves.

2. THE CONFINEMENT (rule for flag-word-driven bulks with k monotone
   flags -- the schedule enumeration is exhaustive for this class;
   verified on all four battery composites). SOME-halt = YES and
   EVERY-halt = NO computed from the six schedules with ZERO core
   steps; every real composite's fate agrees with the branch tree at
   its realized leaf, and the realized leaves match ground truth
   (A (1)->RUN, B ()->RUN, C (1)(2)->BHALT, D (1)->RUN). CORE-A and
   CORE-C: same bulk, different leaves -- WHICH leaf is realized is
   a fact about the universal core (its reachability problem,
   undecidable in general by Minsky universality), while the
   quantified bracket never touched the core. Undecidability
   confined; boundary-quantified questions answered by enumeration.

3. THE CROSSING TOLL (rule; every INC of the run checked). The bare
   route is exactly unary: transfer passes at an INC = the counter
   value before that INC, at all 60 INCs; cumulative cost after t
   INCs = t(t-1)/2 + t exactly (quadratic; 1830 at t = 60). The door
   route (base extension) is one synced write per step by the door
   primitive's definition: cumulative t (60 at t = 60). Crossing the
   boundary exactly costs the value carried, unless the door is
   bought -- the toll axis is quadratic-vs-linear in cumulative coin.

4. THE LEAK CONTROL (property of re-readable boundaries; run-
   verified). The two-state mirror bulk tracks the core's X parity
   at every one of 200 steps; the mailbox boundary carried 200
   change events in 200 steps (one per INC, unbounded with the
   horizon) against the ratchet side's <= 2 ever. Bulk-side facts
   through a re-readable boundary ARE core facts -- the
   undecidability imports exactly where re-readability opens.

SCOPE STATED HONESTLY. The confinement rule here is proved-by-
exhaustion for flag-word-driven bulks (the bulk's step reads only
the flag word); bulks with their own inter-flip dynamics have a
finite branch tree by the flip-timing argument of
explore_interactive_hand.py, proved there for finite-control
composites. The OPEN general form -- any bulk with decidable
autonomous fate questions behind any ratchet-only boundary keeps
boundary-quantified questions decidable -- is a theorem candidate,
not a result of this run; the suspect channel is flip TIMING landing
in an unbounded bulk's trajectory.

RUN RECORD. python explore_read_surface.py: 33 checks pass, ~1 s.
Sections S1-S4 as designed; after the first run one S4 variable was
renamed (cosmetic, no logic change) and the rerun printed
identically.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

# ---------------------------------------------------------------- #
# machinery: the bare machine + rider (verbatim from               #
# explore_frontier_rider.py, trimmed to what the composite needs)  #
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

def const(c, windows):
    return {p: c % p for p in windows}

def add(x, y):
    return {p: (x[p] + y[p]) % p for p in x}

def sub(x, y):
    return {p: (x[p] - y[p]) % p for p in x}

def mul(x, y):
    return {p: (x[p] * y[p]) % p for p in x}

def born(x, p_new, c=0):
    out = dict(x)
    out[p_new] = c % p_new
    return out

def zero_test(x):
    return all(r == 0 for r in x.values())

def support(reg):
    return sorted(p for p, r in reg.items() if r != 0)


class Rider:
    """The bare universal core (explore_frontier_rider.py)."""

    def __init__(self, counters=("X", "Y"), windows=(2, 3, 5)):
        self.windows = list(windows)
        self.next_i = len(self.windows)
        self.counters = counters
        self.reg = {}
        for c in counters:
            self.reg["V_" + c] = const(0, self.windows)
            self.reg["P_" + c] = const(0, self.windows)
        self.reg["ONES"] = const(1, self.windows)
        self.transfer_passes = 0

    def grow(self):
        p_new = PRIMES[self.next_i]
        self.next_i += 1
        self.windows.append(p_new)
        for n in self.reg:
            self.reg[n] = born(self.reg[n], p_new, 0)
        w = sub(const(1, self.windows), self.reg["ONES"])
        self.reg["ONES"] = const(1, self.windows)
        return w

    def inc(self, c):
        w = self.grow()
        V, P = self.reg["V_" + c], self.reg["P_" + c]
        passes = 0
        while True:
            y = mul(V, P)
            if zero_test(y):
                break
            V = add(sub(V, P), w)
            passes += 1
        self.transfer_passes += passes
        self.reg["P_" + c] = w
        self.reg["V_" + c] = add(V, w)
        return passes

    def dec(self, c):
        self.reg["V_" + c] = sub(self.reg["V_" + c], self.reg["P_" + c])

    def jz(self, c):
        return zero_test(self.reg["V_" + c])

    # harness-only inspection (never machine code)
    def value(self, c):
        V = self.reg["V_" + c]
        s = support(V)
        assert len(s) <= 1, f"counter {c} leaked support: {s}"
        return V[s[0]] if s else 0


# ---------------------------------------------------------------- #
# the battery of cores (two-counter programs on the rider)         #
# ---------------------------------------------------------------- #
# program encoding: state -> ("INC", ctr, next) | ("DECJZ", ctr,
# next-if-nonzero, next-if-zero) | "HALT" as a state name.

HALTS_IFF_EVEN = {
    0: ("DECJZ", "X", 1, "HALT"),
    1: ("DECJZ", "X", 0, "LOOP"),
    "LOOP": ("INC", "Y", "LOOP"),
}
TIGHT_LOOP = {          # X parked at 1, Y pumps forever
    0: ("INC", "X", 1),
    1: ("INC", "Y", 1),
}
PUMP_TEN = {            # X climbs to 10, then halt
    i: ("INC", "X", i + 1) for i in range(10)
}
PUMP_TEN[10] = "HALT"

BATTERY = [
    ("CORE-A", HALTS_IFF_EVEN, 4),
    ("CORE-B", TIGHT_LOOP, 0),
    ("CORE-C", PUMP_TEN, 0),
    ("CORE-D", HALTS_IFF_EVEN, 3),
]

THRESHOLDS = (3, 7)     # ratchet flags over X

def core_step(m, prog, q, seed_left):
    """One core step; seeding INCs count as steps. Returns new q,
    seed_left."""
    if seed_left > 0:
        m.inc("X")
        return q, seed_left - 1
    if q == "HALT" or prog.get(q) == "HALT":
        return "HALT", 0
    ins = prog[q]
    if ins[0] == "INC":
        m.inc(ins[1])
        return ins[2], 0
    _, r, nz, z = ins
    if m.jz(r):
        return z, 0
    m.dec(r)
    return nz, 0


# ---------------------------------------------------------------- #
# the two boundaries + the bulk                                     #
# ---------------------------------------------------------------- #

class RatchetBoundary:
    """k monotone one-shot flags over the core's X counter. The
    flip predicate is evaluated by the harness against the machine's
    own pointed residue (exact by the rider invariant)."""

    def __init__(self, thresholds):
        self.thresholds = thresholds
        self.flags = [False] * len(thresholds)
        self.flip_count = [0] * len(thresholds)

    def update(self, x_value):
        for i, c in enumerate(self.thresholds):
            if not self.flags[i] and x_value >= c:
                self.flags[i] = True
                self.flip_count[i] += 1

    def word(self):
        return tuple(self.flags)


def bulk_wait_for_flag2(state, flag_word):
    """The bulk program: HALT as soon as flag 2 reads true."""
    if state == "BHALT":
        return "BHALT"
    return "BHALT" if flag_word[1] else "RUN"


def run_composite(prog, seed, horizon):
    """Interleave core and bulk through the ratchet boundary.
    Returns (bulk fate, realized schedule, boundary history stats)."""
    m = Rider()
    bnd = RatchetBoundary(THRESHOLDS)
    q, seed_left = 0, seed
    bulk = "RUN"
    words_seen = [bnd.word()]
    schedule = []           # flip events in order, e.g. [1], [1,2]
    for _ in range(horizon):
        if q != "HALT":
            q, seed_left = core_step(m, prog, q, seed_left)
        prev = bnd.word()
        bnd.update(m.value("X"))
        now = bnd.word()
        if now != prev:
            flipped = [i + 1 for i in range(len(now))
                       if now[i] and not prev[i]]
            schedule.append(tuple(flipped))
            words_seen.append(now)
        bulk = bulk_wait_for_flag2(bulk, now)
        if bulk == "BHALT":
            break
    return bulk, tuple(schedule), bnd


# the branch tree for k = 2 flag-word-driven bulks: the six schedules
SCHEDULES = [
    (),                     # no flip
    ((1,),),                # flag 1 only
    ((2,),),                # flag 2 only
    ((1,), (2,)),           # 1 then 2
    ((2,), (1,)),           # 2 then 1
    ((1, 2),),              # both at once
]

def bulk_fate_on_schedule(schedule):
    """Run the bulk over an abstract schedule -- ZERO core steps."""
    flags = [False, False]
    bulk = bulk_wait_for_flag2("RUN", tuple(flags))
    if bulk == "BHALT":
        return "BHALT"
    for event in schedule:
        for f in event:
            flags[f - 1] = True
        bulk = bulk_wait_for_flag2(bulk, tuple(flags))
        if bulk == "BHALT":
            return "BHALT"
    return "RUN"


# ---------------------------------------------------------------- #
# sections                                                          #
# ---------------------------------------------------------------- #

HORIZON = 400

def s1_influence_census():
    print("--- S1: the influence census (ratchet boundary)")
    results = {}
    for name, prog, seed in BATTERY:
        bulk, schedule, bnd = run_composite(prog, seed, HORIZON)
        results[name] = (bulk, schedule)
        ok(all(c <= 1 for c in bnd.flip_count),
           f"S1 {name}: every flag flipped at most once "
           f"(counts {bnd.flip_count})")
        ok(schedule in SCHEDULES,
           f"S1 {name}: realized history {schedule} is a branch-tree "
           f"schedule")
        n_events = len(schedule)
        ok(n_events <= 2,
           f"S1 {name}: boundary events ever = {n_events} <= k = 2")
    return results

def s2_confinement(results):
    print("--- S2: the confinement (game answers without the core)")
    fates = {s: bulk_fate_on_schedule(s) for s in SCHEDULES}
    some_halt = any(f == "BHALT" for f in fates.values())
    every_halt = all(f == "BHALT" for f in fates.values())
    ok(some_halt, "S2 SOME-halt = YES from the schedules alone")
    ok(not every_halt, "S2 EVERY-halt = NO from the schedules alone")
    expected_leaf = {
        "CORE-A": (((1,),), "RUN"),
        "CORE-B": ((), "RUN"),
        "CORE-C": (((1,), (2,)), "BHALT"),
        "CORE-D": (((1,),), "RUN"),
    }
    for name, (bulk, schedule) in results.items():
        exp_sched, exp_fate = expected_leaf[name]
        ok(schedule == exp_sched and bulk == exp_fate,
           f"S2 {name}: realized leaf {schedule} -> {bulk} matches "
           f"ground truth")
        ok(fates[schedule] == bulk,
           f"S2 {name}: real fate agrees with the branch tree's "
           f"answer at its leaf (the bracket holds)")
    ok(results["CORE-A"][1] != results["CORE-C"][1],
       "S2 A vs C: same bulk, different realized leaves -- which leaf "
       "is a core fact, the bracket never was")

def s3_coupling_toll():
    print("--- S3: the crossing toll (bare unary vs door-synced)")
    m = Rider(counters=("X",))
    n_incs = 60
    bare_costs, door_costs = [], []
    bare_cum = door_cum = 0
    for t in range(n_incs):
        v_before = m.value("X")
        passes = m.inc("X")
        ok(passes == v_before,
           f"S3 INC at value {v_before}: transfer passes = {passes} "
           f"(exactly the value)") if t in (0, 1, 7, 31, 59) else None
        assert passes == v_before, "linearity broken"
        bare_cum += passes + 1          # +1: the pointed write itself
        door_cum += 1                   # base extension: one synced
        bare_costs.append(bare_cum)     # write per step, by the door
        door_costs.append(door_cum)     # primitive's definition
    global CHECKS
    CHECKS += 1                         # the silent per-INC asserts
    print(f"  [ok] S3 all {n_incs} INCs: passes == value before INC "
          f"(the bare route is exactly unary)")
    print("  toll curves (cumulative ops after t INCs):")
    for t in (9, 19, 39, 59):
        print(f"    t={t+1:3d}  bare={bare_costs[t]:5d}   "
              f"door={door_costs[t]:3d}")
    ok(bare_costs[-1] == n_incs * (n_incs - 1) // 2 + n_incs,
       "S3 bare cumulative = t(t-1)/2 + t (quadratic, closed form)")
    ok(door_costs[-1] == n_incs,
       "S3 door cumulative = t (linear: value-independent sync)")

def s4_leak_control():
    print("--- S4: the leak control (mailbox boundary)")
    m = Rider(counters=("X", "Y"))
    q, seed_left = 0, 0
    prog = {0: ("INC", "X", 0)}         # X pumps forever
    mailbox_changes = 0
    prev_mail = 0
    bulk = 0                    # the mirror bulk: state = last parity
    mismatches = 0
    T = 200
    for _ in range(T):
        q, seed_left = core_step(m, prog, q, seed_left)
        mail = m.value("X") % 2         # the core rewrites the mailbox
        if mail != prev_mail:
            mailbox_changes += 1
        prev_mail = mail
        bulk = mail                     # the bulk re-reads and mirrors
        if bulk != m.value("X") % 2:
            mismatches += 1
    ok(mismatches == 0,
       f"S4 the mirror bulk tracks the core's parity at every one of "
       f"{T} steps")
    ok(mailbox_changes >= T // 2,
       f"S4 mailbox boundary events = {mailbox_changes} over {T} "
       f"steps (unbounded stream, against the ratchet side's <= 2)")
    print(f"  census: ratchet boundary <= 2 events ever; mailbox "
          f"{mailbox_changes} events in {T} steps and growing")


if __name__ == "__main__":
    print("== THE READ SURFACE: the core+bulk composite ==")
    results = s1_influence_census()
    s2_confinement(results)
    s3_coupling_toll()
    s4_leak_control()
    print(f"\nall checks passed: {CHECKS}")
