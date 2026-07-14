"""
explore_interactive_hand.py -- THE INTERACTIVE HAND AT THE MACHINE LAYER
(the recovery chart's fourth row; descends from explore_second_ruler.py
and explore_ecc_borrow.py; the hand repertoire is the interactive
observer's -- explore_interactive_observer.py -- read at the machine
layer).

THE QUESTION. The interactive observer holds three gifts -- a WATCH, a
PROBE, and a HAND -- and the hand's pushes are known to program the
BASIN: one push re-locks any world onto a chosen column (the universal
rudder), scars are permanent, the phoenix schedules pushes at deaths.
The recovery chart prices re-imports by what they let a machine READ of
a value as it moves. So the last row asks: do pushes change the MACHINE
CLASS -- what fate questions about the machine's control are decidable
-- or only the basin? The two answered doors sharpen the danger cells:
a hand that lets two ladders be COMPARED would smuggle the second-ruler
door (explore_second_ruler.py); a hand that SYNCS a grown window would
smuggle base extension (explore_ecc_borrow.py). The naive suspicion --
"a push is an increment the observer performs, so pushes are inert" --
is right about the moves but silent about the real object: the
INTERACTION is a communication channel, and the question decomposes
into what the hand can read and what the world's readable surface can
CARRY back to the machine's branching.

THE MODEL (the handled machine). Two world faces, matching the two
answered doors:
  DEPTH face   the growth machine: control q, depth vector (v_p), moves
               INC_p (monotone, no decrement), reads = finitely many
               LITERAL atoms v_p >= c (presence is c = 1). A program
               text names finitely many atoms; there is no indirection
               (no register-addressed window names).
  ELEMENT face the codeword machine: element registers x_i in Z/N over
               a growing squarefree window set, channel-local ring ops
               (x + a, x * u, x * 0, masks), GROW with constant births,
               channel reads x mod p = r (literal, finitely many named).
THE HAND: an external agent; between consecutive machine steps it may
apply finitely many PUSHES -- multiplications of the world (INC_p,
composite factors, scars = depth pushes) and, on the element face,
native ops with parameters of its choosing (x *= 0 then x += a writes
any constant: reset-plus-add is a write). A hand is a POLICY, graded by
its read set:
  (H0) BLIND         a fixed schedule, reading nothing (the schedule
                     itself may be an arbitrary infinite object);
  (H1) MACHINE-GRADE reads only what the machine's own repertoire reads
                     (threshold atoms; channel reads);
  (H2) DOOR-GRADE    anything that determines the true virtual value:
                     depth comparisons, lift reads, or full WATCHING
                     since birth (a move-history ledger; note a
                     finite-state watcher cannot track an unbounded
                     counter, by pigeonhole -- door-grade hands carry
                     unbounded state or aperiodic reads).
The class questions, well-posed: fate questions about the MACHINE's
control -- does it reach HALT? -- quantified over hands (does SOME hand
make it halt? does EVERY hand?) or relative to a fixed hand policy.

THE HAND ANALYSIS THE RUN VERIFIES (proofs here; the run checks every
checkable step; Minsky universality is cited, not re-proved):

 1. THE RATCHET THEOREM (depth face): pushes are ABSOLUTELY inert.
    Depths never decrease -- machine INCs and hand pushes only raise --
    so every depth-face read atom v_p >= c is MONOTONE along any run:
    it flips false-to-true at most ONCE, ever. A program with k atoms
    therefore sees its read vector change at most k times in any run
    under ANY hand; between flips the control is autonomous (constant
    reads make a deterministic trajectory, eventually periodic within
    |Q| steps), and a hand-caused flip lands at one of finitely many
    positions of that trajectory. The machine-fate map over ALL hands
    factors through a FINITE branch tree. Corollaries:
    (a) Both game questions are decidable: solve reachability (can the
        hand steer to HALT?) and a safety fixpoint (can the hand keep
        the play halt-free forever?) on the capped-depth quotient
        (q, min(v_p, cap_p)) -- the one-place-threshold quotient of
        explore_archimedean_dial.py, upgraded to a two-player arena.
        Hand pushes commute with the cap and every capped raise is
        realizable, so the quotient is a game bisimulation.
    (b) NO hand -- omniscient, uncomputable, unbounded -- changes the
        depth-face class through pushes: the hand's whole-run influence
        is at most k FLIPS, each a write-once flag whose timing lands
        at one of boundedly many trajectory positions -- a finite
        branch tree, never an unbounded stream. (Flips, not bits: a
        flip's timing is itself machine-visible, so one flag can select
        among several continuations; the influence is finite, not
        literally k binary digits.) Comparisons are exactly the
        NON-monotone reads
        (two ladders leapfrog forever), which is why the second-ruler
        door is a door; without comparison reads in the machine, a
        comparing hand can KNOW the outcome stream but cannot TELL it.
        THE RATCHET WALL: a fixed lexicon of one-shot readables against
        an unbounded outcome stream -- the read-side twin of the
        addressing wall (explore_ecc_borrow.py: finitely many window
        names against unboundedly many windows).

 2. THE PUBLISHING SPLIT (what the world's readable surface carries).
    The bandwidth bound is a property of the READS, not of the hand:
    depth-face atoms are ratchets (one shot each), while element-face
    channel reads are PERIODIC in the register -- re-readable forever.
    A one-register MAILBOX (hand rewrites by reset-plus-add, machine
    re-reads x mod 2) carries an unbounded bit stream. So the same
    protocol -- an omniscient hand publishing zero-test verdicts to a
    door-free control -- dies at test k + 1 on the depth face (flags
    exhausted, the ratchet wall) and runs FOREVER on the element face.
    The face asymmetry, not the hand's knowledge, decides smuggling.

 3. SYNC THROUGH THE HAND (element face): door-grade hands buy FULL
    UNIVERSALITY. A watching hand (it has seen every move since birth,
    so it knows each register's true virtual value c -- route knowledge
    substituting for the aperiodic state read) can sync every grown
    window by ONE native move whose PARAMETER carries its knowledge:
    x += a with a = (c - x) mod N restricted to the newborn window.
    That is base extension performed by the hand -- the third row's
    door with the non-channel-local computation moved into the
    intervener. The door-free machine (growth + ring ops + channel
    reads) plus the syncing hand runs a two-counter Minsky machine
    step-exactly: increments grow-then-add, decrements add N - 1,
    zero-tests read true integer zero because lift = c < N is
    maintained by the hand's corrections. Halting transfers; Minsky
    universality is cited (Minsky 1967). On the element face the
    parameter channel is wide open: universality needs no machine-side
    door at all, only a door-grade READ in the loop.

 4. NO NEW POWER BELOW THE DOOR. (a) A BLIND hand is a schedule of
    state-independent ops, so the freeze lemma of explore_ecc_borrow.py
    applies verbatim with the hand's ops entering the multiplier ledger
    like anyone else's: a window born offset stays offset -- r_p =
    (c - (M/M0) c0) mod p at every step under adds and unit
    multipliers, and since unit multipliers cannot kill c0's class,
    the window never syncs under that repertoire. The remaining
    state-independent ops are the CONSTANT cases the keystone lemma
    covers: x * 0 re-syncs only AT ZERO (rebirth at certified zero --
    erasure, not repair, and native to the machine itself), masks
    likewise write constants. A blind hand mints no exactness the
    machine's own repertoire lacks. (An arbitrary blind schedule read
    back through
    channel reads makes the world an oracle TAPE -- the composite
    relativizes to the schedule's own information; that is an import of
    the schedule, not of any door, and is noted, not claimed, here.)
    (b) A MACHINE-GRADE hand composes away: the product of the machine's
    control with a finite-state channel-reading policy is ONE control
    of the same read grade -- the composite is itself a bare-class
    machine (explore_ecc_borrow.py's open residual), so the hand adds
    no read and no power; its bounded-source syncs die at the
    addressing wall exactly like the machine's own.

 5. BASIN, NOT CLASS (the repertoire graded). The rudder, the scar,
    the heal, the phoenix are all MOVE-ONLY interventions: on the depth
    face their entire machine-readable content is ratchet flips (a
    gcd-scar flips exactly the threshold atoms it crosses -- one
    write-once flag for a fresh 2-scar against a v_2 >= 2 atom, none
    thereafter),
    so they are class-inert by the ratchet theorem while remaining
    basin-programming (one push re-locks any world onto a chosen
    column: the universal rudder and the relock rule, proved in
    explore_interactive_observer.py -- cited for the basin half, not
    re-run). The observer's slogan sharpens: interactively the basin
    map is PROGRAMMABLE, and the machine class is UNTOUCHABLE by
    programming alone.

 6. SYNTHESIS (the chart's unifying statement). Across all four rows
    the class is set by the composite READ SET -- machine plus hand --
    and never by who moves or what is pushed: every door is a READ
    import. The known doors each import an UNBOUNDED APERIODIC read
    stream (depth comparisons; lift certificates / syncs); the
    decidable side's reads are ratchets (eventually-constant streams);
    the one open cell -- the bare element class -- is exactly the cell
    whose reads are unbounded but PERIODIC. The hand changes the class
    precisely when it carries a door-grade read AND the world's
    readable surface can publish the stream (mailbox or move
    parameter); on a ratchet-only surface even an omniscient hand is
    inert. Scope of the iff: the inert direction is proved for
    finite-state hands below the door (section 4; an unbounded-state
    hand is itself a computing agent, and its read-free content is at
    most a relativization) -- on ratchet-only surfaces it is absolute,
    ANY hand whatsoever (section 1). Interaction is a channel, and the
    deleted resource prices its bandwidth.

SCOPE + HONESTY. The ratchet theorem is about the modelled depth face:
literal threshold atoms, no indirection, monotone moves -- the
decidable sibling's own read discipline; adding any non-monotone read
re-opens the second-ruler door and is priced there. The game decider
and its bounded-exhaustive cross-check run on a small battery
(exhaustive over schedules acting within a stated prefix; the decider
itself is exact on the quotient). Section 2's depth-face failure is a
WITNESS of the wall's shape for the natural protocol; the proof that no
protocol works is the ratchet theorem, not the witness. Minsky
two-counter universality is cited, not re-derived; the mailbox and
sync simulations verify step-exactness and halting transfer on witness
batteries. Whether the BARE element class is decidable stays open
(explore_ecc_borrow.py's residual) -- machine-grade hands are shown to
add nothing to it, not to decide it. The relativization of a composite
to an uncomputable blind schedule is standard oracle relativization,
noted for scope. The universal rudder's relock rule and the scar
ledger's basin facts are proved in explore_interactive_observer.py and
cited; this script verifies only their machine-layer grading (ratchet
bits, decider agreement).

PREDICTIONS (fixed before the run):
 P1. On the S1 battery, the game decider's SOME-hand and EVERY-hand
     halting verdicts equal bounded-exhaustive schedule enumeration on
     every machine, and every simulated run shows at most k read-vector
     changes (k = the machine's atom count).
 P2. The depth-face k-flag protocol tracks the Minsky reference for
     exactly the first k tests and its fate diverges from the reference
     on the first seed needing more than k tests (k = 2, 4, 8, seeds
     0..8); the element-face mailbox protocol is step-exact with
     halting transfer on all seeds 0..8.
 P3. The watcher-hand sync runs halts-iff-even step-exactly on seeds
     0..8 and the doubling program (X0 = 5 ends with Y = 10), with
     lift = virtual counter < N at every step and halting transferring;
     the machine itself is door-free throughout.
 P4. Blind-hand batteries: the freeze formula r_p = (c - (M/M0) c0)
     mod p is exact at every step of every schedule and the frozen
     window never syncs; the product machine built from the machine and
     a finite-state channel-grade hand reproduces the composite run's
     world trace exactly.
 P5. A rudder-shaped push schedule applied mid-run leaves every battery
     machine's fate inside the decider's verdicts (EVERY-hand-halt
     implies it halts; no-SOME-hand-halt implies it loops), and a fresh
     gcd-scar flips exactly one threshold atom, a repeated scar zero --
     one ratchet bit, then spent.

FINDINGS (entered after the run; 27/27 checks; all five predictions
confirmed, no misses):

 F1. THE RATCHET THEOREM'S MECHANISM VERIFIED (rule at the battery;
     the theorem itself is the docstring's proof). On all four battery
     machines the game decider on the capped-depth quotient agreed
     exactly with bounded-exhaustive schedule enumeration (SOME-hand
     and EVERY-hand halting both): flag-gated halt (True, False),
     self-flip (True, True), derailable (True, False), double atoms on
     one prime (True, False). The read-vector change count never
     exceeded the atom count k in any of the 11,957 enumerated
     schedule runs (5-step prefix; max 1 of 1, 1 of 1, 2 of 2,
     2 of 2): every readable is a write-once flag, and the fate map
     over ALL hands factored through the finite quotient game.

 F2. THE PUBLISHING SPLIT (rule; witnessed at k = 2, 4, 8 and run
     step-exact on the mailbox). The depth-face k-flag protocol -- an
     omniscient hand publishing zero-test verdicts on one-shot flags --
     tracked the reference for exactly the seeds needing <= k tests
     (0..k-1) and went STUCK at flag exhaustion on seed k (needing
     k + 1), at every tested k. The identical protocol through ONE
     element-face mailbox register (hand rewrites by reset-plus-add;
     machine re-reads x mod 2) ran every seed 0..8 step-exactly with
     halting transferring: control traces equal to the reference at
     every step. The bandwidth is the read surface's property --
     ratchets cap it at the program's atom count, one periodic read
     carries an unbounded stream.

 F3. SYNC THROUGH THE HAND BUYS FULL UNIVERSALITY (rule; simulation
     verified step-exact, Minsky universality cited). The door-free
     codeword machine plus the watching hand (correction adds computed
     from the hand's move ledger) ran halts-iff-even step-exactly on
     seeds 0..8 (traces equal to the direct two-counter run, even
     seeds halt, odd seeds certified looping) and the doubling program
     (X0 = 5 ends at Y = 10), with lift = virtual counter < N at every
     macro step. Base extension performed by the intervener is the
     third row's door with the non-channel-local computation moved
     into the hand; its read enters through a native move's PARAMETER.

 F4. NO NEW POWER BELOW THE DOOR (rule at the batteries). Blind hands:
     the freeze formula r_p = (c - (M/M0) c0) mod p held at every step
     of three 200-op random schedules (adds + unit multipliers) and
     the frozen window never once agreed with the true counter -- a
     blind hand cannot mint exactness. Machine-grade hands: the
     product machine (one control ranging over state PAIRS, driven by
     the same two step tables) reproduced the composite run's world
     trace exactly for 120 steps -- a channel-grade hand is absorbed
     into one bare-class control, adding no read and no power.

 F5. BASIN, NOT CLASS (rule at the battery). A rudder-shaped 2-power
     push injected mid-run left every battery machine's fate inside
     the decider's verdicts (halting runs had SOME-hand true;
     EVERY-hand machines halted; no-SOME-hand machines looped), and a
     fresh gcd-scar flipped exactly one threshold atom while a second,
     deeper scar flipped none: a scar's machine-readable content on
     the depth face is one write-once flag flip, then spent. The basin
     half
     of the repertoire (relock, steering, phoenix scheduling) is
     proved in explore_interactive_observer.py and cited, not re-run.

RUN RECORD. python explore_interactive_hand.py -- sections S1-S4,
27/27 checks, 0.09 s wall clock (subprocess-timed), pure Python,
deterministic (fixed RNG seeds 11/12/13). No prediction was revised;
no harness fix was needed between the design draft and the green run.
"""

from collections import defaultdict
from itertools import product as iproduct
import random

CHECKS = [0, 0]


def check(name, ok):
    CHECKS[0] += 1
    CHECKS[1] += ok
    if not ok:
        print(f"  FAIL {name}")
    assert ok, name


# ----------------------------------------------------------------------
# S1  THE RATCHET THEOREM: game decider vs exhaustive schedules
# ----------------------------------------------------------------------
# A machine: atoms = [(p, c), ...] threshold reads; prog = {state:
# ('halt',) | ('inc', p, next) | ('br', atom_index, if_true, if_false)}.
# A schedule: tuple of per-step raise dicts {p: amount} applied before
# machine steps 0, 1, ...; after the schedule the hand passes forever.

def atom_vec(atoms, v):
    return tuple(v[p] >= c for (p, c) in atoms)


def caps_of(atoms):
    caps = {}
    for p, c in atoms:
        caps[p] = max(caps.get(p, 0), c)
    return caps


def simulate(prog, atoms, q0, schedule, horizon=500):
    """Run machine + schedule; return (fate, read-vector change count).
    fate in {'halt', 'loop'}; loop is certified by capped-quotient
    repetition once the hand is done (monotone world, finite quotient)."""
    caps = caps_of(atoms)
    named = sorted(caps)
    v = defaultdict(int)
    q = q0
    flips = 0
    vec = atom_vec(atoms, v)
    seen = set()
    for t in range(horizon):
        if t < len(schedule):
            for p, amt in schedule[t].items():
                v[p] += amt
        else:
            key = (q, tuple(min(v[p], caps[p]) for p in named))
            if key in seen:
                return 'loop', flips
            seen.add(key)
        nvec = atom_vec(atoms, v)
        if nvec != vec:
            flips += 1
            vec = nvec
        ins = prog[q]
        if ins[0] == 'halt':
            return 'halt', flips
        if ins[0] == 'inc':
            v[ins[1]] += 1
            q = ins[2]
            nvec = atom_vec(atoms, v)
            if nvec != vec:
                flips += 1
                vec = nvec
        else:
            _, i, qt, qf = ins
            q = qt if vec[i] else qf
    raise RuntimeError("horizon exceeded")


def decide_games(prog, atoms, q0):
    """Exact decider on the capped-depth quotient, hand as a player.
    Returns (some_hand_halts, every_hand_halts)."""
    caps = caps_of(atoms)
    named = sorted(caps)

    def step(q, w):
        """One machine step from quotient state; None = halt."""
        wd = dict(zip(named, w))
        ins = prog[q]
        if ins[0] == 'halt':
            return None
        if ins[0] == 'inc':
            p = ins[1]
            if p in wd:
                wd[p] = min(wd[p] + 1, caps[p])
            return (ins[2], tuple(wd[p] for p in named))
        _, i, qt, qf = ins
        p, c = atoms[i]
        return (qt if wd[p] >= c else qf, w)

    def hand_options(w):
        ranges = [range(w[i], caps[named[i]] + 1) for i in range(len(named))]
        return [tuple(x) for x in iproduct(*ranges)]

    start = (q0, tuple(0 for _ in named))
    # reachability of HALT with a cooperating hand
    frontier, seen, some = [start], {start}, False
    succ = {}
    while frontier:
        node = frontier.pop()
        q, w = node
        outs = []
        for w2 in hand_options(w):
            nxt = step(q, w2)
            if nxt is None:
                some = True
            else:
                outs.append(nxt)
        succ[node] = outs
        for nxt in outs:
            if nxt not in seen:
                seen.add(nxt)
                frontier.append(nxt)
    # can the hand keep the play halt-free forever? greatest fixpoint:
    # LIVE = nodes with a successor in LIVE (halting successors dropped).
    live = set(succ)
    changed = True
    while changed:
        changed = False
        for node in list(live):
            if not any(s in live for s in succ[node]):
                live.discard(node)
                changed = True
    every = start not in live
    return some, every


# battery: (name, atoms, prog, expected (some, every))
LOOP = ('inc', 97, 'LP')  # a harmless spin state body
BATTERY = [
    ("B1 flag-gated halt",
     [(5, 1)],
     {'A': ('br', 0, 'H', 'B'), 'B': ('inc', 7, 'A'), 'H': ('halt',),
      'LP': LOOP},
     (True, False)),
    ("B2 self-flip halts",
     [(2, 3)],
     {'A': ('inc', 2, 'B'), 'B': ('br', 0, 'H', 'A'), 'H': ('halt',),
      'LP': LOOP},
     (True, True)),
    ("B3 hand can derail",
     [(3, 1), (2, 2)],
     {'A': ('br', 0, 'LP', 'B'), 'B': ('inc', 2, 'C'),
      'C': ('br', 1, 'H', 'A'), 'H': ('halt',), 'LP': LOOP},
     (True, False)),
    ("B4 double atoms, one prime",
     [(2, 2), (2, 4)],
     {'A': ('br', 0, 'B', 'A2'), 'A2': ('inc', 3, 'A'),
      'B': ('br', 1, 'H', 'C'), 'C': ('inc', 2, 'B'), 'H': ('halt',),
      'LP': LOOP},
     (True, False)),
]


def schedules_for(atoms, T):
    caps = caps_of(atoms)
    named = sorted(caps)
    per_step = [dict(zip(named, amts))
                for amts in iproduct(*[range(caps[p] + 1) for p in named])]
    per_step = [{p: a for p, a in d.items() if a} for d in per_step]
    return list(iproduct(per_step, repeat=T))


def s1():
    print("S1  THE RATCHET THEOREM: decider vs exhaustive schedules")
    total_runs = 0
    for name, atoms, prog, expected in BATTERY:
        k = len(atoms)
        some_d, every_d = decide_games(prog, atoms, 'A')
        fates = set()
        max_flips = 0
        for sched in schedules_for(atoms, 5):
            fate, flips = simulate(prog, atoms, 'A', sched)
            fates.add(fate)
            max_flips = max(max_flips, flips)
            total_runs += 1
        some_e, every_e = ('halt' in fates), (fates == {'halt'})
        check(f"S1 {name} decider = enumeration",
              (some_d, every_d) == (some_e, every_e))
        check(f"S1 {name} decider = expected", (some_d, every_d) == expected)
        check(f"S1 {name} flip budget <= k", max_flips <= k)
        print(f"  {name}: some-hand {some_d}, every-hand {every_d}, "
              f"max read-vector changes {max_flips} <= k = {k}")
    print(f"  {total_runs} schedule runs enumerated (5-step prefix); "
          "the fate map over ALL hands factored through the finite "
          "quotient game on every battery machine")


# ----------------------------------------------------------------------
# S2  THE PUBLISHING SPLIT: one-shot flags vs a re-readable mailbox
# ----------------------------------------------------------------------
# Reference two-state halts-iff-even walk on one counter (tests counted).

def ref_minsky(seed, max_steps=10000):
    """Returns (fate 'H'/'L', outcomes list of zero-test booleans,
    control trace)."""
    x, q = seed, 's0'
    outcomes, trace = [], []
    for _ in range(max_steps):
        trace.append(q)
        if q == 's0':
            outcomes.append(x == 0)
            q = 'H' if x == 0 else 's1'
        elif q == 's1':
            x -= 1
            q = 's2'
        elif q == 's2':
            outcomes.append(x == 0)
            q = 'L' if x == 0 else 's3'
        elif q == 's3':
            x -= 1
            q = 's0'
        else:
            return q, outcomes, trace
    raise RuntimeError("ref did not settle")


def flag_protocol(seed, k):
    """Depth-face protocol: an omniscient hand publishes the t-th test
    outcome on one-shot flag t (a fresh threshold atom); the machine's
    finite text carries k flags. Returns ('H'/'L'/'STUCK', tests used)."""
    fate, outcomes, _ = ref_minsky(seed)
    q, t = 's0', 0
    for _ in range(10000):
        if q in ('H', 'L'):
            return q, t
        if q in ('s0', 's2'):
            if t >= k:
                return 'STUCK', t
            zero = outcomes[t]      # the hand pushed flag t iff zero
            t += 1
            q = ('H' if zero else 's1') if q == 's0' else \
                ('L' if zero else 's3')
        elif q == 's1':
            q = 's2'
        else:
            q = 's0'
    raise RuntimeError("protocol did not settle")


class Register:
    """An element register over a growing squarefree window set."""

    def __init__(self, primes):
        self.r = {p: 0 for p in primes}

    def add(self, a):
        for p in self.r:
            self.r[p] = (self.r[p] + a) % p

    def mul(self, u):
        for p in self.r:
            self.r[p] = (self.r[p] * u) % p

    def grow(self, p, birth=0):
        self.r[p] = birth % p

    def read(self, p):
        return self.r[p]

    def is_zero(self):
        return all(x == 0 for x in self.r.values())

    def lift(self):
        n, m = 0, 1
        for p, rp in self.r.items():
            t = ((rp - n) * pow(m, -1, p)) % p
            n += t * m
            m *= p
        return n


def mailbox_protocol(seed):
    """Element-face protocol: the hand rewrites ONE mailbox register
    (reset-plus-add, native ops) with each test outcome; the machine
    re-reads x mod 2 forever. Returns (fate, control trace)."""
    fate_ref, outcomes, trace_ref = ref_minsky(seed)
    mb = Register([2])
    q, t = 's0', 0
    trace = []
    for _ in range(10000):
        trace.append(q)
        if q in ('H', 'L'):
            return q, trace, fate_ref, trace_ref
        if q in ('s0', 's2'):
            mb.mul(0)                    # the hand: reset
            mb.add(1 if outcomes[t] else 0)   # the hand: write the bit
            t += 1
            zero = (mb.read(2) == 1)     # the machine: re-readable read
            q = ('H' if zero else 's1') if q == 's0' else \
                ('L' if zero else 's3')
        elif q == 's1':
            q = 's2'
        else:
            q = 's0'
    raise RuntimeError("mailbox did not settle")


def s2():
    print("S2  THE PUBLISHING SPLIT: one-shot flags vs the mailbox")
    for k in (2, 4, 8):
        completed, stuck_at = [], None
        for seed in range(9):
            fate_ref, outcomes, _ = ref_minsky(seed)
            fate, used = flag_protocol(seed, k)
            need = len(outcomes)
            if need <= k:
                completed.append(fate == fate_ref and used == need)
            elif stuck_at is None:
                stuck_at = (seed, fate)
        check(f"S2 flags k={k} complete iff tests <= k",
              all(completed) and len(completed) == k)
        check(f"S2 flags k={k} first overflow seed stuck",
              stuck_at == (k, 'STUCK'))
        print(f"  k = {k}: seeds 0..{k - 1} tracked exactly, "
              f"seed {k} STUCK at flag exhaustion (needs {k + 1} tests)")
    ok = True
    for seed in range(9):
        fate, trace, fate_ref, trace_ref = mailbox_protocol(seed)
        ok &= (fate == fate_ref and trace == trace_ref)
    check("S2 mailbox step-exact, halting transfers, seeds 0..8", ok)
    print("  one element mailbox: every seed step-exact -- the same "
          "protocol, a periodic read instead of ratchets")


# ----------------------------------------------------------------------
# S3  SYNC THROUGH THE HAND / no new power below the door
# ----------------------------------------------------------------------
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
          59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
          127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181]


class HandledWorld:
    """Door-free codeword machine + a WATCHING hand that syncs newborn
    windows by injecting the correction constant (a native add whose
    parameter carries the hand's route knowledge)."""

    def __init__(self):
        self.S = [2, 3]
        self.X = Register(self.S)
        self.Y = Register(self.S)
        self.cX = 0     # the hand's watch ledger (true virtual values)
        self.cY = 0
        self.next = 2

    def N(self):
        n = 1
        for p in self.S:
            n *= p
        return n

    def grow_and_sync(self):
        p = PRIMES[self.next]
        self.next += 1
        self.S.append(p)
        for reg, c in ((self.X, self.cX), (self.Y, self.cY)):
            reg.grow(p, 0)                     # machine: constant birth
            delta = (c - reg.lift()) % (self.N())
            reg.add(delta)                     # hand: correction add

    def inc(self, reg_name):
        self.grow_and_sync()
        reg = self.X if reg_name == 'X' else self.Y
        reg.add(1)
        if reg_name == 'X':
            self.cX += 1
        else:
            self.cY += 1

    def dec(self, reg_name):
        reg = self.X if reg_name == 'X' else self.Y
        reg.add(self.N() - 1)
        if reg_name == 'X':
            self.cX -= 1
        else:
            self.cY -= 1

    def invariant(self):
        return (self.X.lift() == self.cX < self.N()
                and self.Y.lift() == self.cY < self.N())


def run_handled(prog, q0, x0, max_macro=400):
    """Run a two-counter program on the handled world; returns
    (fate, trace, invariant_held). prog states: ('inc', r, nxt) |
    ('dec', r, nxt) | ('tz', r, if_zero, if_nonzero) | ('halt',)."""
    w = HandledWorld()
    for _ in range(x0):
        w.inc('X')
    q = q0
    trace = [(q, w.cX, w.cY)]
    inv = w.invariant()
    for _ in range(max_macro):
        ins = prog[q]
        if ins[0] == 'halt':
            return 'H', trace, inv
        if ins[0] == 'inc':
            w.inc(ins[1])
            q = ins[2]
        elif ins[0] == 'dec':
            w.dec(ins[1])
            q = ins[2]
        else:
            reg = w.X if ins[1] == 'X' else w.Y
            q = ins[2] if reg.is_zero() else ins[3]
        inv &= w.invariant()
        trace.append((q, w.cX, w.cY))
    return 'L', trace, inv


def run_direct(prog, q0, x0, max_macro=400):
    x, y, q = x0, 0, q0
    trace = [(q, x, y)]
    for _ in range(max_macro):
        ins = prog[q]
        if ins[0] == 'halt':
            return 'H', trace
        if ins[0] == 'inc':
            if ins[1] == 'X':
                x += 1
            else:
                y += 1
            q = ins[2]
        elif ins[0] == 'dec':
            if ins[1] == 'X':
                x -= 1
            else:
                y -= 1
            q = ins[2]
        else:
            val = x if ins[1] == 'X' else y
            q = ins[2] if val == 0 else ins[3]
        trace.append((q, x, y))
    return 'L', trace


HALTS_IFF_EVEN = {
    's0': ('tz', 'X', 'H', 's1'), 's1': ('dec', 'X', 's2'),
    's2': ('tz', 'X', 'l0', 's3'), 's3': ('dec', 'X', 's0'),
    'l0': ('inc', 'Y', 'l0'), 'H': ('halt',),
}
DOUBLING = {
    'd0': ('tz', 'X', 'H', 'd1'), 'd1': ('dec', 'X', 'd2'),
    'd2': ('inc', 'Y', 'd3'), 'd3': ('inc', 'Y', 'd0'), 'H': ('halt',),
}


def s3():
    print("S3  SYNC THROUGH THE HAND / below the door")
    ok = True
    for seed in range(9):
        f1, t1, inv = run_handled(HALTS_IFF_EVEN, 's0', seed, max_macro=30)
        f2, t2 = run_direct(HALTS_IFF_EVEN, 's0', seed, max_macro=30)
        ok &= (f1 == f2 and t1 == t2 and inv)
    check("S3 halts-iff-even step-exact + invariant, seeds 0..8", ok)
    f1, t1, inv = run_handled(DOUBLING, 'd0', 5)
    f2, t2 = run_direct(DOUBLING, 'd0', 5)
    check("S3 doubling X0=5 -> Y=10, step-exact",
          f1 == f2 == 'H' and t1 == t2 and inv and t1[-1][2] == 10)
    print("  door-free machine + watching hand: two-counter runs "
          "step-exact, lift = counter < N throughout (the hand's "
          "correction add is base extension by another name)")

    # blind hand: the freeze lemma survives external ops
    ok_formula, ok_never = True, True
    for rng_seed in (11, 12, 13):
        rng = random.Random(rng_seed)
        S = [2, 3, 5]
        x = Register(S)
        c = 4                               # virtual value at the birth
        x.add(4)
        x.grow(7, 0)                        # frozen window, c0 = 4
        S.append(7)
        c0, M0, M = c, 1, 1
        for _ in range(200):
            if rng.random() < 0.7:
                a = rng.randrange(1, 210)
                x.add(a)
                c += a
            else:
                u = rng.choice([11, 13, 17, 19])   # units mod 210
                x.mul(u)
                c *= u
                M *= u
            want = (c - (M // M0) * c0) % 7
            ok_formula &= (x.read(7) == want)
            ok_never &= (x.read(7) != c % 7)
    check("S3 blind hand: freeze formula exact, 3 batteries", ok_formula)
    check("S3 blind hand: the frozen window never syncs", ok_never)

    # machine-grade hand composes away: product machine = composite run.
    # ONE definition of each agent's step (channel reads only, native
    # ops only); the composite keeps two control variables, the product
    # machine keeps a single control ranging over PAIRS.
    def hand_step(qh, x):
        if qh == 0:
            if x.read(5) >= 3:
                x.mul(11)
                return 1
            return 0
        x.add(7)
        return 0

    def machine_step(qm, x):
        x.add(1 if qm == 0 else 2)
        return (qm + 1) % 2 if x.read(3) == 0 else qm

    def composite_run(steps=120):
        x = Register([2, 3, 5, 7])
        qm, qh = 0, 0                       # two agents
        world_trace = []
        for _ in range(steps):
            qh = hand_step(qh, x)           # hand acts between steps
            qm = machine_step(qm, x)
            world_trace.append(tuple(sorted(x.r.items())))
        return world_trace

    def product_run(steps=120):
        x = Register([2, 3, 5, 7])
        q = (0, 0)                          # ONE control: Q_M x Q_H
        world_trace = []
        for _ in range(steps):
            qh2 = hand_step(q[1], x)        # the same two step tables,
            qm2 = machine_step(q[0], x)     # driven by one pair-state
            q = (qm2, qh2)
            world_trace.append(tuple(sorted(x.r.items())))
        return world_trace

    check("S3 machine-grade hand = one bare control (product trace)",
          composite_run() == product_run())
    print("  blind hands freeze (formula exact, never sync); a "
          "channel-grade hand is absorbed into one bare-class control")


# ----------------------------------------------------------------------
# S4  BASIN, NOT CLASS: rudder-shaped pushes + the scar's ratchet bit
# ----------------------------------------------------------------------
def s4():
    print("S4  BASIN, NOT CLASS")
    ok = True
    for name, atoms, prog, _ in BATTERY:
        some_d, every_d = decide_games(prog, atoms, 'A')
        sched = ({}, {}, {}, {2: 5})        # a rudder-shaped 2-power push
        fate, _ = simulate(prog, atoms, 'A', sched)
        if every_d:
            ok &= (fate == 'halt')
        if not some_d:
            ok &= (fate == 'loop')
        if fate == 'halt':
            ok &= some_d
    check("S4 rudder-pushed fates inside the decider's verdicts", ok)
    atoms = [(2, 2), (5, 1)]
    v = defaultdict(int)
    v[2] = 1                                # the world already holds a 2
    before = atom_vec(atoms, v)
    v[2] += 1                               # a fresh gcd-scar: push 2
    after1 = atom_vec(atoms, v)
    v[2] += 3                               # scar again, deeper
    after2 = atom_vec(atoms, v)
    check("S4 fresh scar flips exactly one atom",
          sum(a != b for a, b in zip(before, after1)) == 1)
    check("S4 repeated scar flips zero (the ratchet bit is spent)",
          after1 == after2)
    print("  pushes reprogram runs, never the decidability; a scar's "
          "machine-readable content is one write-once flag flip")


if __name__ == '__main__':
    s1()
    s2()
    s3()
    s4()
    print(f"\nCHECKS: {CHECKS[1]}/{CHECKS[0]} passed")
    assert CHECKS[0] == CHECKS[1]
