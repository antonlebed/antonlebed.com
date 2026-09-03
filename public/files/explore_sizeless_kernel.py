"""
THE SIZELESS KERNEL: what a scheduler and message passing built on
presence, zero-guards and residue reads ARE, as a transition system.

The question. A kernel is a scheduler and an inter-process channel, and
every real one compares magnitudes: priorities are sorted, deadlines
are compared to a clock, queue lengths are compared to capacities. The
integers read without their size offer a different toolkit: PRESENCE
(a place is seated or it is not), a ZERO-GUARD (a move is enabled or it
is not, and a task that is not enabled waits), a RESIDUE read of a
counter (the clock modulo a period, never the clock's value), and a
one-shot EQUALITY on a rising counter (a rung reached exactly once).
Build the smallest scheduler and channel on those four reads alone, in
a module whose syntax tree is asserted free of magnitude comparison,
drive one workload through it, and ask what kind of machine the kernel
IS: which of its quantities are unbounded, and how its control reads
them. The classes on offer, from the machine reading of the growth
world: the FINITE QUOTIENT (counters that only rise, read by one-shot
tests, decided on control times zero-pattern: explore_growth_machine.py);
a VASS, a vector addition system (counters that rise and fall, read only
through enabledness, never through a branch on zero: coverability
decidable, EXPSPACE); a LOSSY counter machine (counters that may fall on
their own: decidable, not primitive recursive); and MINSKY (a counter
tested for zero with a branch: universal, undecidable). The card's
claim is that the kernel's model lands in a decidable class by design,
so that its safety questions are a tool run rather than a hand proof.

Two corrections made on paper before the engine, both to the card's own
kill-shapes. First, a BOUNDED queue is finite state whatever its
control reads, so "a lossless bounded queue, its free count decremented
and zero-tested" is not a Minsky corner; the corner is an UNBOUNDED
count whose emptiness reaches a control branch, which is a try-receive
or a receive with timeout. Second, a kernel on a finite machine is a
finite-state system, so its safety is already decidable in principle
and the obstacle the incumbents face is state explosion, not
undecidability; the only reading under which "decided by design" says
anything is the PARAMETERIZED model, the kernel with its bounds removed
(unbounded queue capacity, unbounded time), which is what this rig
classifies. The capacity parameter is therefore swept and then set to
infinity.

The design. The kernel keeps a fixed enumeration of seven places (the
seats), each empty or holding a task; a fixed set of channels, each a
count; a tick. Tasks are finite programs over eight instructions:
send(q), recv(q), goto, exit, spawn(prog, else), sleep_mod(d, r) (wait
until tick mod d = r), sleep_until(rung) (wait until tick = rung), and,
in the arms that admit them, trecv(q, else) (receive, or branch on
empty) and if_mod(d, r, else) (branch on the tick's residue). The
scheduler is round robin over the enumeration; a round is one visit to
every seat. Five arms vary the two design choices the hand-attack found
load-bearing:
  A. OBLIVIOUS yield, per-ROUND tick, blocking recv only. A blocked task
     spends its step passing; the tick rises once per round.
  B. Arm A plus trecv, the branchable zero-test.
  C. SKIPPING yield (a blocked task is passed over and spends no step),
     per-STEP tick.
  D. Skipping yield, per-round tick.
  E. Arm A plus if_mod, a branch on the tick's residue, which is finite
     control on its own.
The workload (arm A's, reused by the others): a producer and consumer
over a data channel with a CREDIT channel back (W credits seeded, the
producer receives a credit before each send, the consumer returns one
after each receive and a residue wait, so that it is the slower of the
two and the window fills), a periodic timer task feeding a tock channel that
nobody drains, and a spawner that seats idle children until the table
is full and then exits.

Four instruments.
  1. THE SYNTAX-TREE ASSERTION over the kernel class: no Lt, Gt, LtE,
     GtE; no call to min, max, sorted, heapq, bisect or a sort method.
     The census of what the tree DOES hold is printed: every Compare
     node with its operator and operands, every subtraction.
  2. THE READ CENSUS of the run: every read the kernel performed on the
     workload's behalf, by kind (presence scan, zero-guard pass or fire,
     capacity equality, residue, rung equality, and in arms B and E the
     branch reads).
  3. THE ONE-STEP MONOTONICITY CENSUS, the operational test of the WSTS
     compatibility axiom: for reachable states s and s' = s plus tokens
     on some channels (control equal), every successor of s must be
     covered by a successor of s', under the order "control equal,
     counts componentwise at most", control being the seat table, the
     position and the tick's residue modulo the timers' period. Run on
     the deterministic kernel and on its MAY-PASS relaxation, in which
     an enabled recv may also pass (the task scheduled later), the
     relaxation being the kernel's interleaving over-approximation. A
     violation is printed with the instruction it sits at and the
     coordinate that fails (counts, pc, position, tick).
  4. THE TOOL RUN: Karp-Miller coverability over the relaxed arm A at
     infinite capacity, deciding: is a data-channel count of W, of W+1,
     coverable with credits; is every count coverable without credits
     (the omega verdict); and the tree's size. The kernel's own code
     runs the tree's steps, with omega as a value that is never zero
     and absorbs plus and minus one, so the tool and the kernel share
     one semantics.

Predictions fixed before the run.
  P1. The assertion holds for the kernel class; the Compare census shows
      only Eq, NotEq, Is, IsNot and In; exactly one subtraction, the
      recv decrement.
  P2. Arm A's read census: presence scans from spawn, zero-guard passes
      and fires from recv, residue reads from the timer, no order read;
      at capacity below W the send census shows drops and at capacity
      W and above it shows none: the credit protocol makes the
      drop-on-full queue lossless with no comparison anywhere.
  P3. Max data occupancy is W at every capacity at or above W, and the
      capacity itself below W; the undrained tock channel's occupancy
      grows with the run at infinite capacity and equals the capacity
      otherwise, the drops counted being the coalesced ticks.
  P4. Monotonicity: deterministic A violates, every violation at a recv
      and in the pc coordinate (pass against fire); relaxed A has zero
      violations. Relaxed B violates at trecv, pc coordinate. Relaxed C
      violates, every violation in the tick coordinate. Relaxed D has
      zero. Relaxed E has zero.
  P5. Karp-Miller on relaxed A: with credits, data at least W coverable,
      W+1 not; without credits, data omega; the tree finite and small.
  P6. Arm B hosts the halts-iff-even counter program on a channel as its
      counter: an even seed halts, an odd seed runs to the step bound.
  P7. Arm E turns timing into control: a task that receives a token
      whose arrival time depends on whether a channel was empty, and
      then branches on the tick's residue, ends at different program
      counters for the empty and the non-empty seed, while relaxed E's
      one-step census is zero, so the may-pass tool is sound and blind
      to that test.
  P8. sleep_until on a rung the tick has passed never wakes: the
      one-shot equality is a ratchet and a missed rung is missed for
      good, printed as the sleeping task's pc after the run.
Positive controls, run before any verdict is read: the syntax checker
flags a planted "<" and a planted min() in a sibling snippet; the
kernel's deterministic step agrees with a hand-traced round of the
credit workload; the Karp-Miller tree on the credit system reproduces
the deterministic run's max occupancy W; the monotonicity checker fires
on arm B (its census is arm A's control).

Kill criteria, as prints (the card's three kill-shapes, corrected).
  K1. The assertion fails on the kernel class, or the workload needs an
      instruction the class cannot host: an order read at the first
      rung.
  K2. Relaxed arm A prints a monotonicity violation: the workload forced
      a branchable zero-test on an unbounded count, the Minsky corner.
  K3. Relaxed arm A is monotone only with a drop transition present
      (capacity finite), never at infinite capacity: the class is lossy
      with no finite-quotient core.
A miss on all three names the class VASS with a finite-quotient core
(the seat table, the position, the tick's residue), and the decidable
question is coverability of the may-pass relaxation, sound for the
kernel's safety properties.

Findings (the run's own prints; one design correction first). The
workload as first frozen had a producer and consumer of equal speed,
and under round robin they alternate, so data occupancy was 1 at every
capacity and the credit window never filled; the consumer was slowed by
the residue wait before any verdict was read, and the predictions stand
as written.
  F1. P1 holds. Two classes walked, no forbidden node; the Compare
      census is Eq 29, Is 4, IsNot 3; one subtraction, recv's. The
      planted snippet is flagged twice. The checker fired once during
      the build, on a sorted() over channel NAMES in the state
      accessors, replaced by the fixed channel enumeration: the
      assertion is over the tree, not the author's word.
  F2. P2 and P3 hold. Reads at infinite capacity over 700 steps: 35
      presence scans, 52 zero-guard fires, 21 passes, 60 residue reads,
      no capacity read and no order read. Peak data occupancy is the
      capacity at 1 and 2 (with drops) and W = 3 at 3, 4, 8 and infinity
      (no drops): the credit protocol makes the queue lossless with no
      comparison. The undrained tock channel peaks at the capacity with
      the coalesced ticks as drops (32 at capacity 1) and at 33 at
      infinity; the uncredited producer reaches 26. Bounded spawn: 6 of
      7 seats live after the spawner fills the table and exits.
  F3. P4 holds with the census read in full. Deterministic A violates
      the compatibility axiom 22 times over 1,600 pairs, every one at a
      blocked recv in the pc coordinate (the pass is a zero-guarded
      move); relaxed A, zero. Relaxed B violates at trecv, pc. Arm C
      violates 82 times and the relaxation moves every violation to the
      TICK coordinate: a skipped task spends no tick, a delayed one
      does, so no clock-preserving relaxation is monotone. Arm D, zero.
      Relaxed E, zero.
  F4. The path census, the sharper observable: over 200 pairs each, a
      token more never changes any seat's stutter-free path in A, C or
      D, only its timing; in B it does, at the try-receive's else (2
      divergences, consumer pc 4 against 1); in E it does, at T's branch
      (2 divergences, pc 2 against 3, over 105 pairs).
  F5. P5 holds. Karp-Miller on relaxed A: with credits, data at least 3
      coverable and 4 not, tock omega, 2,378 nodes; without credits,
      data omega and any count coverable, 396 nodes.
  F6. P6 holds: seeds 2 and 4 halt, 3 and 5 loop, on the kernel's own
      try-receive. Scope: one tested channel is a one-counter machine,
      decidable; the Minsky corner is two tested channels, which the
      construction reaches by the same call on a second channel.
  F7. P7 holds. T's branch reads residue 8 when c is empty and 1 when
      c holds a token, and ends at pc 3 against pc 2, while relaxed E's
      one-step census is zero: the branch on the clock's residue turns
      a wait's timing into control, and the may-pass tool cannot see it.
  F8. P8 holds: the late task is seated at its sleep_until forever,
      the on-time task exits.
Tier: rule at the rig's scale (the syntax assertion, the censuses and
the tree are exhaustive over what they enumerate; the class claims
lean on the standard theorems named in the question). Verdict: all
three kill-shapes missed. The kernel's model at infinite capacity is a
VASS with a finite-quotient core (the seat table, the position, the
tick's residue), once its deterministic scheduling is relaxed to "a
task may be delayed a step", and coverability of that relaxation is
the tool run; the relaxation is clock-preserving for the oblivious
scheduler and for the skipping one with a per-round tick, and for no
scheduler that skips against a per-step tick. Two system calls reach the
Minsky corner and none of the workload's waits does: a try-receive, and a BRANCH on the clock's
residue downstream of a wait, the second being the flip-timing channel
of the read surface inside a kernel; a residue WAIT is harmless. The
tool proves only what the relaxation keeps, so a property whose truth
rides on timing is outside it.

Contact, after the run. The class landing is the asynchronous-programs
theorem: a multiset task buffer under a nondeterministic scheduler has
safety verification equal to Petri-net coverability, EXPSPACE-complete,
and a test for the absence of a pending handler makes it undecidable
(Ganty and Majumdar, "Algorithmic verification of asynchronous
programs", ACM TOPLAS 2012, sections 6 and 7.6); their real-time
extension, where a clock advances only when no zero-delay task is
pending, simulates zero tests and is undecidable ("Analyzing real-time
event-driven programs", FORMATS 2009). This rig's own contribution is
the kernel reading: which system calls keep the class, the
clock-preservation of the relaxation by scheduler type, the wait/branch
split on the clock's residue, and the credit protocol as a lossless
drop-on-full queue with no comparison.


Run: python explore_sizeless_kernel.py, seconds, negligible memory.
"""

import ast
import os
import sys
from collections import Counter

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

SEATS = (2, 3, 5, 7, 11, 13, 17)


class Omega:
    """The Karp-Miller omega: never zero, absorbs plus and minus one."""

    def __eq__(self, other):
        return isinstance(other, Omega)

    def __ne__(self, other):
        return not isinstance(other, Omega)

    def __hash__(self):
        return 7

    def __add__(self, other):
        return self

    def __sub__(self, other):
        return self

    def __repr__(self):
        return "w"


OMEGA = Omega()


class Task:
    __slots__ = ("name", "prog", "pc")

    def __init__(self, name, prog):
        self.name = name
        self.prog = prog
        self.pc = 0


# ---------------------------------------------------------------------------
# THE KERNEL: the syntax tree of everything between these two rules is
# asserted free of magnitude comparison (instrument 1). Control reads
# presence, equality with zero, equality with a constant, residues.
# ---------------------------------------------------------------------------
class Kernel:
    def __init__(self, progs, channels, cap=None, policy="oblivious",
                 tick_mode="round", seeds=None):
        self.progs = progs
        self.channels = tuple(channels)
        self.seated = {p: None for p in SEATS}
        self.count = {q: 0 for q in self.channels}
        for q, n in (seeds or {}).items():
            self.count[q] = n
        self.cap = cap
        self.policy = policy
        self.tick_mode = tick_mode
        self.tick = 0
        self.pos = 0
        self.reads = Counter()
        self.drops = Counter()
        self.peak = Counter()
        self.halted = []

    # --- system calls -----------------------------------------------------
    def spawn(self, name):
        for p in SEATS:
            self.reads["spawn:presence"] += 1
            if self.seated[p] is None:
                self.seated[p] = Task(name, self.progs[name])
                return p
        return None

    def send(self, q):
        if self.cap is not None:
            self.reads["send:capacity-equality"] += 1
            if self.count[q] == self.cap:
                self.drops[q] += 1
                return False
        self.count[q] = self.count[q] + 1
        if not self.count[q] == OMEGA and not self.peak[q] == OMEGA:
            if self.peak[q] == self.count[q] or self.peak[q] + 1 == self.count[q]:
                self.peak[q] = self.count[q]
        return True

    def recv(self, q):
        if self.count[q] == 0:
            self.reads["recv:zero-guard pass"] += 1
            return False
        self.reads["recv:zero-guard fire"] += 1
        self.count[q] = self.count[q] - 1
        return True

    def residue_is(self, d, r):
        self.reads["tick:residue"] += 1
        return self.tick % d == r

    def rung_is(self, rung):
        self.reads["tick:rung-equality"] += 1
        return self.tick == rung

    # --- the scheduler ----------------------------------------------------
    def runnable(self, t):
        ins = t.prog[t.pc]
        op = ins[0]
        if op == "recv":
            return not self.count[ins[1]] == 0
        if op == "sleep_mod":
            return self.tick % ins[1] == ins[2]
        if op == "sleep_until":
            return self.tick == ins[1]
        return True

    def execute(self, p, t, may_pass=False):
        """One instruction of task t at seat p; returns the successor
        set when may_pass (the relaxation), else applies one step."""
        ins = t.prog[t.pc]
        op = ins[0]
        if op == "send":
            self.send(ins[1])
            t.pc = t.pc + 1
        elif op == "recv":
            if self.recv(ins[1]):
                t.pc = t.pc + 1
        elif op == "trecv":
            self.reads["trecv:zero-branch"] += 1
            if self.recv(ins[1]):
                t.pc = t.pc + 1
            else:
                t.pc = ins[2]
        elif op == "sleep_mod":
            if self.residue_is(ins[1], ins[2]):
                t.pc = t.pc + 1
        elif op == "if_mod":
            self.reads["if_mod:residue-branch"] += 1
            if self.residue_is(ins[1], ins[2]):
                t.pc = t.pc + 1
            else:
                t.pc = ins[3]
        elif op == "sleep_until":
            if self.rung_is(ins[1]):
                t.pc = t.pc + 1
        elif op == "spawn":
            if self.spawn(ins[1]) is None:
                t.pc = ins[2]
            else:
                t.pc = t.pc + 1
        elif op == "goto":
            t.pc = ins[1]
        elif op == "halt":
            self.halted.append(t.name)
            self.seated[p] = None
            return
        elif op == "exit":
            self.seated[p] = None
            return
        if t.pc == len(t.prog):
            self.seated[p] = None

    def step(self):
        """One scheduler decision: visit the seat at pos."""
        p = SEATS[self.pos]
        t = self.seated[p]
        if t is not None:
            if self.policy == "skip" and not self.runnable(t):
                self.reads["yield:skip"] += 1
            else:
                self.execute(p, t)
                if self.tick_mode == "step":
                    self.tick = self.tick + 1
        self.pos = (self.pos + 1) % len(SEATS)
        if self.pos == 0 and self.tick_mode == "round":
            self.tick = self.tick + 1

    # --- state as a value, for the analyses -------------------------------
    def get_state(self):
        seats = tuple(None if self.seated[p] is None
                      else (self.seated[p].name, self.seated[p].pc)
                      for p in SEATS)
        counts = tuple(self.count[q] for q in self.channels)
        return (self.pos, seats, self.tick, counts)

    def set_state(self, st):
        pos, seats, tick, counts = st
        self.pos, self.tick = pos, tick
        for p, s in zip(SEATS, seats):
            self.seated[p] = None if s is None else Task(s[0], self.progs[s[0]])
            if s is not None:
                self.seated[p].pc = s[1]
        for q, n in zip(self.channels, counts):
            self.count[q] = n
# ---------------------------------------------------------------------------
# END OF THE KERNEL
# ---------------------------------------------------------------------------


def fresh_seats(k, order):
    for name in order:
        k.spawn(name)


def run(k, steps):
    for _ in range(steps):
        k.step()


# --- instrument 1: the syntax-tree assertion --------------------------------
FORBIDDEN_CALLS = {"min", "max", "sorted", "heappush", "heappop", "bisect",
                   "bisect_left", "bisect_right", "nlargest", "nsmallest"}
FORBIDDEN_ATTRS = {"sort", "heappush", "heappop"}
FORBIDDEN_OPS = (ast.Lt, ast.Gt, ast.LtE, ast.GtE)


def check_tree(src, class_names=("Kernel", "Task")):
    tree = ast.parse(src)
    nodes = [n for n in ast.walk(tree)
             if isinstance(n, ast.ClassDef) and n.name in class_names]
    bad, compares, subs = [], Counter(), []
    for cls in nodes:
        for n in ast.walk(cls):
            if isinstance(n, ast.Compare):
                for op, right in zip(n.ops, n.comparators):
                    compares[type(op).__name__] += 1
                    if isinstance(op, FORBIDDEN_OPS):
                        bad.append(("compare", type(op).__name__, n.lineno))
            elif isinstance(n, ast.Call):
                f = n.func
                if isinstance(f, ast.Name) and f.id in FORBIDDEN_CALLS:
                    bad.append(("call", f.id, n.lineno))
                if isinstance(f, ast.Attribute) and f.attr in FORBIDDEN_ATTRS:
                    bad.append(("method", f.attr, n.lineno))
            elif isinstance(n, ast.BinOp) and isinstance(n.op, ast.Sub):
                subs.append(n.lineno)
            elif isinstance(n, ast.AugAssign) and isinstance(n.op, ast.Sub):
                subs.append(n.lineno)
    return bad, compares, subs, len(nodes)


# --- the workload ---------------------------------------------------------------
def credit_progs(W):
    return {
        "producer": [("recv", "credit"), ("send", "data"), ("goto", 0)],
        "consumer": [("recv", "data"), ("sleep_mod", 4, 0), ("send", "credit"), ("goto", 0)],
        "timer": [("sleep_mod", 3, 0), ("send", "tock"), ("goto", 0)],
        "spawner": [("spawn", "child", 2), ("goto", 0), ("exit",)],
        "child": [("goto", 0)],
    }, {"credit": W}


def uncredited_progs():
    return {
        "producer": [("send", "data"), ("goto", 0)],
        "consumer": [("recv", "data"), ("sleep_mod", 4, 0), ("goto", 0)],
        "timer": [("sleep_mod", 3, 0), ("send", "tock"), ("goto", 0)],
        "spawner": [("spawn", "child", 2), ("goto", 0), ("exit",)],
        "child": [("goto", 0)],
    }, {}


CHANNELS = ("credit", "data", "tock")
ORDER = ("producer", "consumer", "timer", "spawner")
PERIOD = 12


# --- instrument 3: one-step monotonicity -----------------------------------------
def control_of(st, period):
    pos, seats, tick, counts = st
    return (pos, seats, tick % period)


def successors(kfactory, st, relaxed):
    """The successor set of state st: one for the deterministic kernel,
    one or two for the may-pass relaxation."""
    outs = []
    k = kfactory()
    k.set_state(st)
    k.step()
    outs.append(k.get_state())
    if relaxed:
        p = SEATS[st[0]]
        k2 = kfactory()
        k2.set_state(st)
        t = k2.seated[p]
        if t is not None and t.prog[t.pc][0] in ("recv", "trecv") and k2.runnable(t):
            # the enabled receive passes instead: the task is scheduled later
            k2.pos = (k2.pos + 1) % len(SEATS)
            if k2.tick_mode == "step":
                k2.tick += 1
            if k2.pos == 0 and k2.tick_mode == "round":
                k2.tick += 1
            outs.append(k2.get_state())
    return outs


def covered(t, t2, period):
    if control_of(t, period) != control_of(t2, period):
        return False
    return all(b == OMEGA or (a != OMEGA and a <= b) for a, b in zip(t[3], t2[3]))


def failing_coordinates(t, S2, period):
    """The coordinates on which t fails to be covered, read against the
    successor of s' that comes nearest to covering it."""
    best = None
    for t2 in S2:
        fails = []
        if t[0] != t2[0]:
            fails.append("position")
        if t[1] != t2[1]:
            fails.append("pc")
        if t[2] % period != t2[2] % period:
            fails.append("tick")
        if not all(b == OMEGA or (a != OMEGA and a <= b) for a, b in zip(t[3], t2[3])):
            fails.append("counts")
        if best is None or len(fails) < len(best):
            best = fails
    return "+".join(best)


def monotonicity_census(kfactory, states, relaxed, period, bumps=((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1))):
    viol = Counter()
    pairs = 0
    for st in states:
        for bump in bumps:
            st2 = (st[0], st[1], st[2], tuple(a + b for a, b in zip(st[3], bump)))
            pairs += 1
            S1 = successors(kfactory, st, relaxed)
            S2 = successors(kfactory, st2, relaxed)
            for t in S1:
                if not any(covered(t, t2, period) for t2 in S2):
                    k = kfactory()
                    k.set_state(st)
                    task = k.seated[SEATS[st[0]]]
                    ins = task.prog[task.pc][0] if task is not None else "empty-seat"
                    # the coordinate that fails against the nearest successor
                    coord = failing_coordinates(t, S2, period)
                    viol[(ins, coord)] += 1
    return viol, pairs


def paths_of(kfactory, st, steps):
    """Per seat, the stutter-free sequence of (task, pc) the seat shows."""
    k = kfactory()
    k.set_state(st)
    paths = [[] for _ in SEATS]
    for _ in range(steps):
        for i, p in enumerate(SEATS):
            t = k.seated[p]
            cur = None if t is None else (t.name, t.pc)
            if not paths[i] or paths[i][-1] != cur:
                paths[i].append(cur)
        k.step()
    return paths


def path_census(kfactory, states, steps, bumps):
    """Does a token more ever change a PATH rather than a timing: for
    each sampled state and bump, every seat's stutter-free path from s
    must be a prefix of its path from s + bump, or the reverse."""
    div = Counter()
    pairs = 0
    for st in states:
        for bump in bumps:
            st2 = (st[0], st[1], st[2], tuple(a + b for a, b in zip(st[3], bump)))
            pairs += 1
            P1, P2 = paths_of(kfactory, st, steps), paths_of(kfactory, st2, steps)
            for i, (a, b) in enumerate(zip(P1, P2)):
                n = len(a) if len(a) <= len(b) else len(b)
                if a[:n] != b[:n]:
                    j = next(j for j in range(n) if a[j] != b[j])
                    div[(a[j], b[j])] += 1
    return div, pairs


def reachable_states(kfactory, steps, relaxed=False, limit=4000):
    """States along the deterministic run, or a BFS of the relaxation."""
    k = kfactory()
    if not relaxed:
        seen = []
        for _ in range(steps):
            seen.append(k.get_state())
            k.step()
        return seen
    start = k.get_state()
    seen = {start}
    frontier = [start]
    while frontier and len(seen) < limit:
        nxt = []
        for st in frontier:
            for t in successors(kfactory, st, True):
                if t not in seen:
                    seen.add(t)
                    nxt.append(t)
        frontier = nxt
    return list(seen)


# --- instrument 4: Karp-Miller -------------------------------------------------------
def karp_miller(kfactory, period, limit=20000):
    k = kfactory()
    root = k.get_state()
    nodes = {root: None}  # state -> parent
    frontier = [root]
    while frontier and len(nodes) < limit:
        st = frontier.pop()
        for t in successors(kfactory, st, True):
            # accelerate against ancestors
            anc = st
            counts = list(t[3])
            while anc is not None:
                if control_of(anc, period) == control_of(t, period):
                    if all(b == OMEGA or (a != OMEGA and a <= b) for a, b in zip(anc[3], counts)) \
                            and any(a != OMEGA and b != OMEGA and a < b for a, b in zip(anc[3], counts)):
                        counts = [OMEGA if (a != OMEGA and b != OMEGA and a < b) or b == OMEGA else b
                                  for a, b in zip(anc[3], counts)]
                anc = nodes[anc]
            t = (t[0], t[1], t[2], tuple(counts))
            if t in nodes:
                continue
            if any(covered(t, u, period) for u in nodes):
                continue
            nodes[t] = st
            frontier.append(t)
    return nodes


def coverable(nodes, period, chan_index, at_least):
    for st in nodes:
        v = st[3][chan_index]
        if v == OMEGA or v >= at_least:
            return True
    return False


# --- main ---------------------------------------------------------------------------------
def main():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    W = 3
    print("=" * 72)
    print("INSTRUMENT 1: the syntax tree of the kernel class")
    bad, compares, subs, ncls = check_tree(src)
    print(f"  classes walked: {ncls}; forbidden nodes: {bad}")
    print(f"  Compare census: {dict(compares)}")
    print(f"  subtractions at lines: {subs}")
    planted = "class Kernel:\n    def f(self, a, b):\n        if a < b: return min(a, b)\n"
    pb, _, _, _ = check_tree(planted)
    print(f"  positive control (planted < and min): flagged {len(pb)} -> {pb}")
    assert not bad, "K1: an order read in the kernel"
    assert len(pb) == 2

    def factory_A(cap=None, progs_seeds=None, policy="oblivious", tick_mode="round"):
        progs, seeds = progs_seeds if progs_seeds else credit_progs(W)

        def make():
            k = Kernel(progs, CHANNELS, cap=cap, policy=policy,
                       tick_mode=tick_mode, seeds=seeds)
            fresh_seats(k, ORDER)
            return k
        return make

    print("=" * 72)
    print("POSITIVE CONTROL: one hand-traced round of the credit workload")
    k = factory_A()()
    # hand trace, W = 3, seats: producer, consumer, timer, spawner, 3 empty.
    # step 1 producer: recv credit fires (3 -> 2). step 2 consumer: recv data
    # passes (0). step 3 timer: sleep_mod(3,0) at tick 0 fires, pc -> 1.
    # step 4 spawner: spawn child seats seat 5, pc -> 1. steps 5,6: child
    # idles, empty seat. step 7: empty seat; the round ends, tick -> 1.
    for _ in range(7):
        k.step()
    st = k.get_state()
    hand = (0, (("producer", 1), ("consumer", 0), ("timer", 1), ("spawner", 1),
                ("child", 0), None, None), 1, (2, 0, 0))
    print(f"  kernel: {st}")
    print(f"  hand:   {hand}")
    assert st == hand

    print("=" * 72)
    print("INSTRUMENT 2 + P2/P3: arm A read census and occupancy by capacity")
    STEPS = 700
    for cap in (1, 2, 3, 4, 8, None):
        k = factory_A(cap=cap)()
        run(k, STEPS)
        print(f"  cap={str(cap):>4}: peak data={k.peak['data']}, peak tock={k.peak['tock']}, "
              f"drops={dict(k.drops)}, halted={k.halted}")
        if cap is None or cap >= W:
            assert k.peak["data"] == W and k.drops["data"] == 0
        else:
            assert k.peak["data"] == cap and k.drops["data"] > 0
    k = factory_A()()
    run(k, STEPS)
    print(f"  reads (cap=inf): {dict(k.reads)}")
    assert "recv:zero-guard pass" in k.reads and "spawn:presence" in k.reads
    assert not any(key.startswith("send:capacity") for key in k.reads)
    seats_live = sum(1 for p in SEATS if k.seated[p] is not None)
    print(f"  live seats after the run: {seats_live} of {len(SEATS)} (bounded spawn)")
    k = factory_A(progs_seeds=uncredited_progs())()
    run(k, STEPS)
    print(f"  uncredited (cap=inf): peak data={k.peak['data']} over {STEPS} steps")
    assert k.peak["data"] > W

    print("=" * 72)
    print("INSTRUMENT 3: one-step monotonicity census (violations by instruction, coordinate)")
    arms = {}
    arms["A oblivious, round tick"] = factory_A()
    arms["C skip, step tick"] = factory_A(policy="skip", tick_mode="step")
    arms["D skip, round tick"] = factory_A(policy="skip", tick_mode="round")
    results = {}
    for name, fac in arms.items():
        states = reachable_states(fac, 400)
        det, pairs = monotonicity_census(fac, states, False, PERIOD)
        rel, _ = monotonicity_census(fac, states, True, PERIOD)
        results[name] = (det, rel)
        print(f"  {name}: {pairs} pairs")
        print(f"     deterministic: {dict(det)}")
        print(f"     relaxed:       {dict(rel)}")
    # arm B: a try-receive consumer
    progsB, seedsB = credit_progs(W)
    progsB = dict(progsB)
    progsB["consumer"] = [("trecv", "data", 4), ("sleep_mod", 4, 0), ("send", "credit"),
                          ("goto", 0), ("goto", 0)]

    def facB():
        k = Kernel(progsB, CHANNELS, cap=None, seeds=seedsB)
        fresh_seats(k, ORDER)
        return k
    statesB = reachable_states(facB, 400)
    detB, _ = monotonicity_census(facB, statesB, False, PERIOD)
    relB, _ = monotonicity_census(facB, statesB, True, PERIOD)
    results["B trecv"] = (detB, relB)
    print(f"  B trecv: deterministic {dict(detB)}; relaxed {dict(relB)}")
    detA, relA = results["A oblivious, round tick"]
    assert sum(relA.values()) == 0, "K2: the workload forced a branchable zero-test"
    assert all(ins == "recv" and coord == "pc" for ins, coord in detA)
    assert sum(relB.values()) > 0 and all(ins == "trecv" for ins, _ in relB)
    detC, relC = results["C skip, step tick"]
    assert sum(relC.values()) > 0 and all(coord == "tick" for _, coord in relC)
    detD, relD = results["D skip, round tick"]
    print(f"  arm D relaxed violations: {sum(relD.values())}")
    print("  path census (does a token more change a seat's path, or only its timing?)")
    BUMPS = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1))
    pathres = {}
    for name, fac in list(arms.items()) + [("B trecv", facB)]:
        states = reachable_states(fac, 400)[::8]
        div, pairs = path_census(fac, states, 60, BUMPS)
        pathres[name] = div
        print(f"     {name}: {pairs} pairs, divergences {dict(div)}")
    assert sum(pathres["A oblivious, round tick"].values()) == 0
    assert sum(pathres["C skip, step tick"].values()) == 0
    assert sum(pathres["D skip, round tick"].values()) == 0
    assert sum(pathres["B trecv"].values()) > 0

    print("=" * 72)
    print("INSTRUMENT 4: Karp-Miller coverability on relaxed arm A (capacity infinite)")
    ci = CHANNELS.index("data")
    nodes = karp_miller(factory_A(), PERIOD)
    print(f"  credited tree: {len(nodes)} nodes")
    for n in (W, W + 1):
        print(f"    data >= {n} coverable: {coverable(nodes, PERIOD, ci, n)}")
    assert coverable(nodes, PERIOD, ci, W) and not coverable(nodes, PERIOD, ci, W + 1)
    ti = CHANNELS.index("tock")
    print(f"    tock omega: {any(st[3][ti] == OMEGA for st in nodes)}")
    nodesU = karp_miller(factory_A(progs_seeds=uncredited_progs()), PERIOD)
    print(f"  uncredited tree: {len(nodesU)} nodes; data omega: "
          f"{any(st[3][ci] == OMEGA for st in nodesU)}; data >= 1000 coverable: "
          f"{coverable(nodesU, PERIOD, ci, 1000)}")
    assert coverable(nodesU, PERIOD, ci, 1000)
    controls = {control_of(st, PERIOD) for st in nodes}
    print(f"  finite-quotient core of the credited tree (distinct controls): {len(controls)}")

    print("=" * 72)
    print("P6: arm B hosts halts-iff-even on a channel counter")
    hie = {"hie": [("trecv", "c", 3), ("trecv", "c", 4), ("goto", 0), ("halt",), ("goto", 4)]}
    for seed in (2, 3, 4, 5):
        k = Kernel(hie, ("c",), seeds={"c": seed})
        k.spawn("hie")
        run(k, 200)
        t = k.seated[SEATS[0]]
        state = "halted" if k.halted else f"looping at pc {t.pc}"
        print(f"  seed {seed}: {state}")
        assert (seed % 2 == 0) == bool(k.halted)

    print("=" * 72)
    print("P7: arm E, a residue branch turns a wait's timing into control")
    # H waits on c, then pings r. H2 pings r once, late. T receives r and
    # branches on the tick's residue. The residue T reads is measured
    # first, per seed, then the branch is set to seed 1's reading.
    def progs_E(r_branch):
        return {
            "H": [("recv", "c"), ("send", "r"), ("goto", 2)],
            "H2": [("sleep_mod", 12, 6), ("send", "r"), ("goto", 2)],
            "T": [("recv", "r"), ("if_mod", 12, r_branch, 3), ("goto", 2), ("goto", 3)],
        }

    def arrival_residue(seed):
        k = Kernel(progs_E(0), ("c", "r"), seeds={"c": seed})
        for n in ("H", "H2", "T"):
            k.spawn(n)
        for _ in range(7 * 20):
            t = k.seated[SEATS[2]]
            if k.pos == 2 and t.pc == 1:
                return k.tick % 12
            k.step()
        return None
    res = {seed: arrival_residue(seed) for seed in (0, 1)}
    print(f"  residue T's branch reads, by c's seed: {res}")
    assert res[0] != res[1]
    progsE = progs_E(res[1])
    outcome = {}
    for seed in (0, 1):
        k = Kernel(progsE, ("c", "r"), seeds={"c": seed})
        for n in ("H", "H2", "T"):
            k.spawn(n)
        run(k, 7 * 20)
        t = k.seated[SEATS[2]]
        outcome[seed] = t.pc
        print(f"  c seeded {seed}: T ends at pc {t.pc}; reads {dict(k.reads)}")
    assert outcome[0] != outcome[1]

    def facE():
        k = Kernel(progsE, ("c", "r"), cap=None, seeds={"c": 1})
        for n in ("H", "H2", "T"):
            k.spawn(n)
        return k
    statesE = reachable_states(facE, 140)
    relE, _ = monotonicity_census(facE, statesE, True, 12, bumps=((1, 0), (0, 1), (1, 1)))
    print(f"  relaxed E one-step violations: {dict(relE)}")
    assert sum(relE.values()) == 0
    divE, pairsE = path_census(facE, reachable_states(facE, 140)[::4], 60, ((1, 0), (0, 1), (1, 1)))
    print(f"  arm E path census: {pairsE} pairs, divergences {dict(divE)}")
    assert sum(divE.values()) > 0

    print("=" * 72)
    print("P8: sleep_until on a passed rung")
    progsR = {"late": [("sleep_mod", 5, 4), ("sleep_until", 2), ("exit",)],
              "ontime": [("sleep_until", 2), ("exit",)]}
    k = Kernel(progsR, ())
    k.spawn("late")
    k.spawn("ontime")
    run(k, 7 * 30)
    late = k.seated[SEATS[0]]
    print(f"  late task: {'still seated at pc ' + str(late.pc) if late else 'exited'}; "
          f"ontime task: {'seated' if k.seated[SEATS[1]] else 'exited'}")
    assert late is not None and late.pc == 1 and k.seated[SEATS[1]] is None

    print("=" * 72)
    print("VERDICT: K1 missed (no order read), K2 missed (relaxed A monotone), "
          "K3 missed (monotone at infinite capacity, no drop transition).")
    print("  Class: VASS with a finite-quotient core; the tool is coverability "
          "of the may-pass relaxation.")


if __name__ == "__main__":
    main()
