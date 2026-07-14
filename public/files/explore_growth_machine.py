"""
explore_growth_machine.py -- THE GROWTH MACHINE (THE HUNT chamber
thirteen, P157; sibling of explore_growth_laws.py P143 ..
explore_thermometer_pair.py P156).

THE QUESTION (Anton, P153; ROAD ranking #1): is a demand + intervention
schedule a UNIVERSAL COMPUTER? Scars are write-once registers,
admissibility probes are conditionals, the phoenix is a clocked loop.
The named attack: encode a two-counter (Minsky) machine in window
depths, or FIND THE OBSTRUCTION (reachability in the demand lattice).

ANSWER: the obstruction. The growth machine is NOT Turing-complete; its
halting-shaped question is DECIDABLE. The single missing primitive is
the DECREMENT -- and the decrement is the archimedean CARRY, the
DELETED PLACE (TOWER.md I). The finite-window world is sub-universal
for the same reason the tower has no size.

THE MODEL. A state is a depth vector e: primes -> N (finite support),
N = prod p^e(p). A growth move multiplies N by the least admissible
m >= 2; every chamber-eleven intervention (push, scar, healing,
phoenix) ALSO multiplies N by some m >= 2. So N strictly increases and
the depth vector is MONOTONE non-decreasing along every operation: no
operation lowers a depth (by construction -- growth IS multiplication).
The machine's primitives, read against a counter machine:
  INC(p)          multiply by p (depth(p)++)            -- realizable
  JZ presence(p)  D-IND admits p as a new window iff
                  p does not divide N, i.e. depth(p)==0
                  -- a zero-test on the PRESENCE bit     -- realizable
  DEC(p)          lower depth(p)                         -- NOT realizable
So the growth machine is INC + presence-zero-test, NO DECREMENT.

THE THEOREM (load-bearing). A counter machine with INC and zero-test
but NO DEC has DECIDABLE halting. Counters only rise, so each counter's
zero-test flips 0 -> + at most ONCE; the zero-pattern z in {0,+}^k is
monotone and changes <= k times; the run is a concatenation of <= k+1
segments, each a finite automaton over the control Q with FIXED branch
outcomes -> ultimately periodic -> halting decided on the finite
quotient Q x {0,+}^k. WSTS reading: chamber eight's UPWARD-CLOSURE LAW
(D-DYN's admissible set is upward-closed) is exactly the compatibility
axiom of a WELL-STRUCTURED TRANSITION SYSTEM (Finkel-Schnoebelen); WSTS
have DECIDABLE termination, Turing-completeness needs UNDECIDABLE
halting -- so no WSTS is universal. The growth machine is a WSTS.

THE THRESHOLD. Adding DEC breaks monotonicity: a larger counter behaves
DIFFERENTLY on test-and-decrement, so the (control, zero-pattern)
quotient stops determining the future -- two configs with equal (q,z)
but different magnitudes have different fates. Minsky = INC +
test-and-DEC is universal (halting undecidable, textbook); growth =
INC + JZ, no DEC is decidable. The decrement is the ONE break, and it
is the archimedean borrow -- the window the tower deleted.

FINDINGS (tiers per CLAUDE.md; run record below; every section asserts).

1. THE NO-DECREMENT LAW (rule, proved by construction; verified S1
   exhaustively over the battery). Every growth move and every
   chamber-eleven intervention multiplies N by an integer m >= 2, so
   N strictly increases and the depth vector rises component-wise: no
   operation, growth or hand, lowers any window's depth. Exhaustive
   over B states x the full repertoire (breadth, dynamics, push p^a,
   phoenix inject-2, scar, heal): every op monotone, N_new > N_old, and
   a direct search for ANY op lowering a target depth returns empty.
   The arrow of monotone growth is the deleted place read dynamically:
   there is no borrow.

2. THE THREE PRIMITIVES (rule; verified S2). INC(p) is a push by p --
   depth(p) rises by exactly one, all others fixed. The PRESENCE
   ZERO-TEST is real and exact: p is D-IND-admissible as a new
   independent window iff p does not divide N iff depth(p) == 0 --
   the independence demand IS a zero-test on the presence bit
   (verified over the battery: admissibility == (depth==0), no
   exceptions). DEC is absent (finding 1). So the machine reads as
   INC + presence-JZ with no decrement: conditionals fire, but each
   presence-test flips true->false at most once (write-once), so
   control flow is acyclic per window.

3. THE HALTING DECIDER (the running artifact; rule, proved; verified
   S3). A halting procedure for the monotone counter machine, working
   on the finite quotient Q x {0,+}^k WITHOUT simulating counters to
   the end: it returns HALT or LOOP by DFS over the quotient (the
   zero-pattern only rises, so a repeated quotient node with no
   pending zero-flip is a certified infinite loop). Demonstrated on a
   battery of growth-machine programs -- including ones whose naive
   forward simulation never terminates (unbounded INC loops) yet whose
   fate the decider settles in a handful of quotient steps. "Is the
   demand-lattice target reachable?" HAS a decision procedure.

4. THE TURING THRESHOLD IS THE DECREMENT (rule, proved; verified S4).
   Restore DEC and the same quotient decider goes UNSOUND: exhibited a
   2-counter machine and two initial configurations sharing the same
   (control, zero-pattern) whose fates DIFFER (one halts, one loops) --
   the magnitude the quotient discards now decides halting. Minsky
   machines (INC + test-and-DEC) are universal, halting undecidable;
   the decrement is the exact primitive whose addition breaks
   monotonicity, breaks WSTS compatibility, and lifts the system from
   decidable to universal. Located precisely: the Turing threshold of
   the growth world is the archimedean borrow.

5. COMMUTATIVITY + WRITE-ONCE = THE WSTS ROOT (rule; verified S5;
   frames chamber eight). The structural reason the growth machine is
   sub-Turing: its move monoid is COMMUTATIVE -- N is a product, so
   composition ORDER is invisible to the state (verified order-blind
   over the (state, move, move) battery). Commutative composition is
   Petri-net/VASS territory; a NON-commutative composition (a stack, a
   pushdown) is what universality needs, and the tower's growth is
   abelian. The D-IND presence bit is WRITE-ONCE (once p divides N it
   never re-admits as a new window -- as windows fill, the
   admissible-to-open set only shrinks), the monotone DUAL of chamber
   eight's upward-closure. (The ring-level lambda-growth condition is NOT
   unconditionally upward-closed -- a present odd prime's deepening
   fails to grow lambda when another window already supplies that
   q-power -- so the clean monotone carrier is presence + depth, not
   raw admissibility; chamber eight's law is cited, not re-derived.)
   Commutative + monotone + finite zero-pattern = a well-structured
   transition system; a WSTS has decidable termination; hence not
   Turing-complete.

6. THE WITNESS READING (observation; verified S6; cashes VERTIGO STOCK
   (c), P156). Because state is monotone and route-blind, a growth
   computation's ENDPOINT under-determines its HISTORY: the number of
   schedules (ordered move sequences) reaching a target N is the
   multinomial in the move multiset -- factorial/exponential in the
   move count, all collapsing to one endpoint (route-weight
   cancellation, chamber six, read combinatorially). The growth machine
   computes WITNESS-readably, STATE-deniably: the endpoint certifies
   WHAT (the multiset of moves) but never the ROUTE. Compute you can
   watch but not audit from the result -- the scar ledger's deniability
   split at the level of computation.

7. THE OBSTRUCTION IS THE DELETED PLACE (synthesis -- the chamber's
   headline). Universality needs destructive memory reuse: overwrite,
   decrement, a movable two-way head. Every one is a BORROW -- an
   archimedean carry, the one window the tower deleted (TOWER.md I: size,
   sign, carries, overflow live only at the archimedean place). Growth
   is multiplication with no borrow, so the growth machine is a
   well-structured, sub-Turing, DECIDABLE computer, and its three fates
   are the WSTS classification of runs -- breadth converges to the
   crystal, depth locks to a column, mortality terminates: the three
   decidable long-run behaviors of a well-structured system. The phoenix already
   said it: "does it ever open another window?" IS the Fermat-prime
   question (chamber eleven) -- the machine's behavior is
   number-theoretic-deterministic, not programmable-universal. The
   growth machine is the DELETED PLACE read as computation: subtract
   the archimedean window and you subtract Turing-completeness.

SCOPE + HONESTY. The no-decrement law is by construction (multiply-only)
and verified exhaustively over a finite battery of states x operations;
it is a theorem about the modelled repertoire (breadth, dynamics,
push, phoenix, scar, heal), not a claim that no exotic future
"intervention" could be defined to decrement -- but any such
intervention would have to DIVIDE N, leaving the growth world (the
window depths are exponents in a modulus you build by multiplying). The
monotone-counter decidability is standard (well-structured transition
systems, Finkel-Schnoebelen 2001; Minsky universality and undecidable
halting, Minsky 1967; VASS reachability decidable, Mayr/Kosaraju,
Leroux-Schmitz 2019); the contribution is the IDENTIFICATION of the
growth machine as such a system, the location of the threshold at the
decrement, and the reading of the decrement as the deleted archimedean
place. The richer growth-machine PROBES (the cold-blindness
admissibility tests -- independence, lambda-growth, semisimplicity) do
not lift the verdict: each is a MONOTONE test of the depth vector (a
threshold "depth(p) >= k" or an upward/downward-closed admissibility
condition, never a non-monotone parity), and a finite schedule uses
finitely many thresholds, so the generalized zero-pattern over the
(counter, threshold) pairs is still monotone with boundedly many flips
-- the same finite quotient decides; only a NON-monotone test or a
decrement breaks it. The unbounded-window route to universality (windows
as tape) is argued shut by the same missing primitive: an addressable head needs a
two-way (INC and DEC) pointer, and copy-forward-with-modification needs
a data-dependent loop = a countdown = a decrement (S4 note). The
quotient decider is exact on the modelled machines; it is not a claim
about arbitrary demands with oracles.

FROZEN SLATE (SCRATCH P157). Adjudication -- NO MISSES, all confirmed:
  PR1 no-decrement law ...... CONFIRMED (18 states x repertoire = 342
      ops, all monotone, N strictly grows, decrement search EMPTY)
  PR2 INC + presence-JZ,
      DEC absent ............ CONFIRMED (INC exact; presence-JZ ==
      (depth==0) over 126 tests, no exception)
  PR3 decider settles battery CONFIRMED (M_A LOOP / M_B HALT / M_C
      HALT / M_D[z] HALT / M_D[+] LOOP; the two LOOP verdicts are
      programs whose naive sim never ends)
  PR4 DEC -> quotient unsound  CONFIRMED (halts-iff-even: c0=2 HALT,
      c0=3 LOOP, sharing (q0, zero-pattern [+]); two DECs the only
      monotonicity breakers)
  PR5 commutative + write-once CONFIRMED (128 order-blind triples; 21
      write-once tests) -- superseded the false "D-DYN upward-closed"
      slate item pre-commit (the naive lambda-growth closure is false;
      commutativity is the true WSTS root)
  PR6 schedule count =
      multinomial ........... CONFIRMED (p_k#: 6/24/120/720/5040 =
      k!; 1350 -> 60, 44100 -> 2520)

RUN RECORD (python prime/code/explore_growth_machine.py, <1 s, trivial
memory, 1882 checks): S1 no-decrement (18-state battery x {breadth,
dynamics, phoenix, push p/p^2, scar for p in 2,3,5,7,11, heal} = 342
ops; every op multiplies N and rises component-wise; explicit
decrement search empty); S2 primitives (INC exact on the battery;
presence-JZ == depth-zero over 126 tests); S3 decider (finite quotient
Q x {0,+}^k DFS with zero-pattern-flip regime reset; 5-program battery,
agreeing with forward sim wherever the sim terminates, deciding the two
non-terminating ones); S4 threshold (the halts-iff-even Minsky machine,
c0=2 vs c0=3 sharing a quotient node, opposite fate; DEC the sole
breaker); S5 WSTS root (128 commutativity triples, 21 write-once
tests); S6 witness (schedule multinomials; p_k# = k! routes to one
endpoint). One pre-commit correction, caught by reading the S5 output
against the hand law: the first draft asserted D-DYN deepening was
upward-closed via a vacuous ok(a or True) -- the naive closure is
FALSE (a present odd prime's deepening does not grow lambda when
another window already carries that q-power); replaced by the true
structural root (commutativity) with real asserts.
"""

import math
from fractions import Fraction

CHECKS = 0


def ok(cond, msg=""):
    global CHECKS
    if not cond:
        raise AssertionError("CHECK FAILED: " + msg)
    CHECKS += 1


# ------------------------------------------------------------------ #
# S0 harness: the growth state, demands, and interventions
# ------------------------------------------------------------------ #

def factorint(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def depth_vec(n):
    """The state: prime -> depth (exponent). N = prod p^depth."""
    return factorint(n)


def carmichael(n):
    """lambda(n) = lcm over prime powers of the local Carmichael value."""
    if n == 1:
        return 1
    L = 1
    for p, a in factorint(n).items():
        if p == 2:
            loc = 1 if a == 1 else (2 if a == 2 else 2 ** (a - 2))
        else:
            loc = (p - 1) * p ** (a - 1)
        L = L * loc // math.gcd(L, loc)
    return L


def primes_upto(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


PRIMES = primes_upto(2000)
PRIMESET = set(PRIMES)


def least_new_prime(n):
    """The breadth (D-IND) greedy move: least prime not dividing n."""
    for p in PRIMES:
        if n % p != 0:
            return p
    raise RuntimeError("ran out of primes")


def d_ind_admits(n, p):
    """Independence demand: p is admissible as a NEW window iff p does
    not divide n -- i.e. the zero-test on the presence bit depth(p)==0."""
    return n % p != 0


def d_dyn_move(n):
    """The dynamics (D-DYN) greedy move: least prime power that grows
    lambda. Returns the move m (a prime power)."""
    lam = carmichael(n)
    best = None
    # scan prime powers p^a in increasing size until one grows lambda
    cand = []
    for p in PRIMES[:80]:
        val = p
        a = 1
        while val <= n * p * p + 10 ** 6 and a <= 40:
            cand.append((val, p, a))
            val *= p
            a += 1
    cand.sort()
    for val, p, a in cand:
        if carmichael(n * val) > lam:
            best = val
            break
    return best


# The intervention repertoire (chamber eleven), each a multiply-by-m:
def op_breadth(n):
    return n * least_new_prime(n)


def op_dynamics(n):
    m = d_dyn_move(n)
    return n * m if m else n


def op_push(n, p, a=1):
    return n * p ** a


def op_phoenix(n):
    return n * 2                       # minimal life support: inject 2


def op_scar(n, p):
    return n * p                       # a permanent write-once mark


def op_heal(n):
    return n * least_new_prime(n)      # add a missing window


# ------------------------------------------------------------------ #
# S1 -- THE NO-DECREMENT LAW (finding 1)
# ------------------------------------------------------------------ #
print("S1 -- THE NO-DECREMENT LAW")

battery = [1, 2, 3, 6, 30, 210, 2310, 4, 8, 12, 9, 72, 30030, 71,
           2 * 3 ** 5, 7 * 11 * 13, 210 * 210, 5 ** 3 * 7]
# verify each op is monotone (depth vector rises component-wise) and
# strictly grows N; and search for ANY decrement
n_ops = 0
decrement_found = False
for i, n in enumerate(battery):
    e0 = depth_vec(n)
    local = []
    local.append(op_breadth(n))
    local.append(op_dynamics(n))
    local.append(op_phoenix(n))
    for p in (2, 3, 5, 7, 11):
        local.append(op_push(n, p, 1))
        local.append(op_push(n, p, 2))
        local.append(op_scar(n, p))
    local.append(op_heal(n))
    for m in local:
        n_ops += 1
        e1 = depth_vec(m)
        ok(m > n, "N strictly grows (%d -> %d)" % (n, m))
        # component-wise monotone: every prime's depth non-decreasing
        for p in set(e0) | set(e1):
            if e1.get(p, 0) < e0.get(p, 0):
                decrement_found = True
            ok(e1.get(p, 0) >= e0.get(p, 0),
               "depth(%d) monotone at N=%d" % (p, n))
ok(not decrement_found, "no operation lowers any depth")
print("  %d states x repertoire = %d operations, all monotone; "
      "N strictly grows; decrement search EMPTY" % (len(battery), n_ops))
print("  the growth world has no borrow: multiply-only => monotone")
print()


# ------------------------------------------------------------------ #
# S2 -- THE THREE PRIMITIVES (finding 2)
# ------------------------------------------------------------------ #
print("S2 -- THE THREE PRIMITIVES (INC, presence-JZ, no DEC)")

# INC(p): push by p raises depth(p) by exactly one, others fixed
for n in battery:
    for p in (2, 3, 5, 7, 13):
        e0 = depth_vec(n)
        e1 = depth_vec(op_push(n, p, 1))
        ok(e1.get(p, 0) == e0.get(p, 0) + 1, "INC(%d) raises depth by 1" % p)
        for q in set(e0) | set(e1):
            if q != p:
                ok(e1.get(q, 0) == e0.get(q, 0), "INC leaves other depths")

# presence zero-test: D-IND admits p  <=>  depth(p)==0
zt_checks = 0
for n in battery:
    for p in (2, 3, 5, 7, 11, 13, 17):
        admit = d_ind_admits(n, p)
        is_zero = (depth_vec(n).get(p, 0) == 0)
        ok(admit == is_zero,
           "presence-JZ: D-IND admits %d iff depth==0 (N=%d)" % (p, n))
        zt_checks += 1
print("  INC(p): push by p, depth(p)++ exactly, others fixed -- verified")
print("  presence-JZ: D-IND-admits(p) == (depth(p)==0) over %d tests -- "
      "exact zero-test on the presence bit" % zt_checks)
print("  DEC: absent (S1) -- machine = INC + presence-JZ, no decrement")
print()


# ------------------------------------------------------------------ #
# S3 -- THE HALTING DECIDER (finding 3, the running artifact)
# ------------------------------------------------------------------ #
print("S3 -- THE HALTING DECIDER (monotone counter machine)")

# A monotone counter machine: control states 0..Q-1 plus 'HALT'.
# instr[q] is one of:
#   ("INC", i, q')            counter i += 1, goto q'
#   ("JZ", i, q_zero, q_nz)   if counter i == 0 goto q_zero else q_nz
# NO DEC. Config = (control q, counters tuple). Decider works on the
# finite quotient (q, zero-pattern) -- zero-pattern only rises.

def run_forward(instr, q0, counters, limit=200000):
    """Naive forward simulation (may not terminate); returns
    'HALT', 'LOOP?'(limit hit), with step count. No full-config dedup:
    counters grow unboundedly, so a repeated config need not exist."""
    q = q0
    c = list(counters)
    for step in range(limit):
        if q == "HALT":
            return "HALT", step
        ins = instr[q]
        if ins[0] == "INC":
            _, i, qp = ins
            c[i] += 1
            q = qp
        else:
            _, i, qz, qn = ins
            q = qz if c[i] == 0 else qn
        # cannot dedupe on full config: counters may grow unboundedly
    return "LOOP?", limit


def decide_halting(instr, q0, zero_pattern):
    """DECIDE HALT/LOOP on the finite quotient. zero_pattern[i]=True
    means counter i is known 0. The quotient node is (q, tuple(zp)).
    A revisited node with no pending zero->+ flip since last visit is a
    certified infinite loop (zero-pattern is monotone: it only loses
    zeros, never regains them, so finitely many flips bound the run)."""
    q = q0
    zp = list(zero_pattern)
    seen = set()
    while True:
        if q == "HALT":
            return "HALT"
        node = (q, tuple(zp))
        if node in seen:
            return "LOOP"        # cycled with fixed zero-pattern
        seen.add(node)
        ins = instr[q]
        if ins[0] == "INC":
            _, i, qp = ins
            if zp[i]:
                zp[i] = False    # a zero counter leaves zero (a flip)
                seen.clear()     # new zero-pattern: fresh regime
            q = qp
        else:
            _, i, qz, qn = ins
            q = qz if zp[i] else qn


# --- battery of monotone programs ---
# M_A: q0: INC(0)->q0.  Naive sim: never halts. Decider: LOOP.
M_A = {0: ("INC", 0, 0)}
# M_B: q0: JZ(0)-> HALT else q1 ; counter 0 starts 0 -> HALT.
M_B = {0: ("JZ", 0, "HALT", 1), 1: ("INC", 0, 0)}
# M_C: q0: JZ(1) -> q1 else HALT ; q1: INC(0)->q2 ; q2: JZ(0)->q1 else HALT.
#   counter1 starts +, counter0 starts 0: q0-> q1 (INC0, now 0-flips) ->
#   q2 -> JZ0 nonzero -> HALT.
M_C = {0: ("JZ", 1, 1, "HALT"),
       1: ("INC", 0, 2),
       2: ("JZ", 0, 1, "HALT")}
# M_D: unbounded INC loop that also tests a never-incremented zero
#   counter: q0: JZ(1)-> HALT else q1 ; q1: INC(0)->q0.  counter1 = 0:
#   HALT at once. counter1 = + : loops forever on q0->q1->q0 (INC 0).
M_D = {0: ("JZ", 1, "HALT", 1), 1: ("INC", 0, 0)}

cases = [
    ("M_A c=(0)", M_A, 0, (0,), (True,)),
    ("M_B c=(0)", M_B, 0, (0,), (True,)),
    ("M_C c=(0,3)", M_C, 0, (0, 3), (True, False)),
    ("M_D c=(0,0) [z1]", M_D, 0, (0, 0), (True, True)),
    ("M_D c=(0,5) [+1]", M_D, 0, (0, 5), (True, False)),
]
expect = {"M_A c=(0)": "LOOP", "M_B c=(0)": "HALT",
          "M_C c=(0,3)": "HALT", "M_D c=(0,0) [z1]": "HALT",
          "M_D c=(0,5) [+1]": "LOOP"}
for name, instr, q0, counters, zp in cases:
    verdict = decide_halting(instr, q0, zp)
    fwd, steps = run_forward(instr, q0, counters, limit=5000)
    ok(verdict == expect[name], "decider verdict %s for %s" % (verdict, name))
    # decider agrees with forward sim where the sim terminates
    if fwd == "HALT":
        ok(verdict == "HALT", "decider matches terminating sim %s" % name)
    if verdict == "LOOP":
        ok(fwd == "LOOP?", "decider LOOP where naive sim never ends: %s" % name)
    print("  %-20s decider=%-4s  naive-sim=%s" % (name, verdict, fwd))
print("  the demand-lattice halting question is DECIDED on the finite")
print("  quotient -- incl. programs whose forward simulation never ends")
print()


# ------------------------------------------------------------------ #
# S4 -- THE TURING THRESHOLD IS THE DECREMENT (finding 4)
# ------------------------------------------------------------------ #
print("S4 -- THE TURING THRESHOLD IS THE DECREMENT")

# Restore DEC: instr ("DEC", i, q') -> if c[i]>0: c[i]-=1 ; goto q'
# (test-and-branch handled via a preceding JZ, Minsky-style).
def run_minsky(instr, q0, counters, limit=200000):
    q = q0
    c = list(counters)
    for step in range(limit):
        if q == "HALT":
            return "HALT", step
        ins = instr[q]
        if ins[0] == "INC":
            _, i, qp = ins; c[i] += 1; q = qp
        elif ins[0] == "DEC":
            _, i, qp = ins
            if c[i] > 0:
                c[i] -= 1
            q = qp
        else:
            _, i, qz, qn = ins
            q = qz if c[i] == 0 else qn
    return "LOOP?", limit


# A machine that HALTS iff counter 0 is EVEN, else loops forever.
# q0: JZ(0)-> HALT else q1     (0 reached with even parity -> halt)
# q1: DEC(0)-> q2              (odd step down)
# q2: JZ(0)-> q_odd else q3    (hit 0 on an odd step -> never halt)
# q3: DEC(0)-> q0             (even step down, back to test)
# q_odd: INC(0)-> q_odd       (spin forever)
EVENODD = {0: ("JZ", 0, "HALT", 1),
           1: ("DEC", 0, 2),
           2: ("JZ", 0, "odd", 3),
           3: ("DEC", 0, 0),
           "odd": ("INC", 0, "odd")}
# two configs with the SAME (control q0, zero-pattern: counter0 = +):
r_even, _ = run_minsky(EVENODD, 0, (2,))
r_odd, _ = run_minsky(EVENODD, 0, (3,))
ok(r_even == "HALT", "Minsky even-counter halts")
ok(r_odd == "LOOP?", "Minsky odd-counter loops")
# both start at (q0, counter0 nonzero) -- the SAME quotient node --
# yet differ: the monotone quotient decider is provably UNSOUND with
# DEC. The quotient node = (control, zero-pattern), zero-pattern[i] =
# (counter i == 0); compute it for both configs and assert EQUAL.
def quotient_node(q, counters):
    return (q, tuple(c == 0 for c in counters))


node_even = quotient_node(0, (2,))
node_odd = quotient_node(0, (3,))
ok(node_even == node_odd, "c0=2 and c0=3 share quotient node")
ok(r_even != r_odd, "yet their fates differ -- quotient UNSOUND with DEC")
print("  Minsky halts-iff-even: c0=2 -> %s, c0=3 -> %s" % (r_even, r_odd))
print("  shared quotient node %s (magnitude discarded)" % (node_even,))
print("  both share (control=q0, zero-pattern=[+]) yet fate DIFFERS")
print("  => the magnitude the quotient discards decides halting:")
print("     with DEC the (q,z) quotient is UNSOUND. Threshold = DECREMENT.")

# sanity: the SAME machine without the two DECs (replace by INC/skip)
# is monotone and the quotient decider applies -- confirm DEC is the
# only non-monotone instruction present.
nondec = [ins for ins in EVENODD.values() if ins[0] == "DEC"]
ok(len(nondec) == 2, "exactly the two DEC instructions break monotonicity")
print("  the two DEC instructions are the only monotonicity breakers")
print()


# ------------------------------------------------------------------ #
# S5 -- COMMUTATIVITY + WRITE-ONCE = WSTS COMPATIBILITY (finding 5)
# ------------------------------------------------------------------ #
print("S5 -- COMMUTATIVITY + WRITE-ONCE (the WSTS root; frames chamber 8)")

# The structural root of decidability is that the growth monoid is
# COMMUTATIVE: N is a product, so composition ORDER is invisible to the
# state -- Petri-net/VASS territory, not a stack. A non-commutative
# composition (a pushdown) is what universality needs; the tower's
# growth is abelian. Verify order-independence of the move repertoire.
chain = [1, 2, 6, 30, 210, 2310, 30030, 510510]
comm_checks = 0
for n in chain:
    for p in (2, 3, 5, 7):
        for q in (3, 5, 7, 11):
            # push p then q == push q then p (state = N, order-blind)
            a = op_push(op_push(n, p, 1), q, 1)
            b = op_push(op_push(n, q, 1), p, 1)
            ok(a == b, "growth monoid commutative (N=%d, %d,%d)" % (n, p, q))
            comm_checks += 1
# D-IND presence bit is WRITE-ONCE (the one-shot zero-test): once p
# divides N, p never re-admits as a new window -- admissibility is
# monotone (true -> false, never back). This is the monotone DUAL of
# chamber eight's upward-closure: as windows fill, the admissible-to-open
# set only SHRINKS (heat can still deepen -- D-DYN's up-closed deepening,
# cited from chamber eight, not re-derived here; the ring-level
# lambda-growth condition is not unconditionally upward-closed, so the
# clean monotone carrier is presence + depth).
wo_checks = 0
for n in chain[1:]:
    for p in (2, 3, 5):
        opened_here = (n % p == 0)
        after = d_ind_admits(n * p, p)      # after multiplying in p
        ok(not after, "D-IND presence WRITE-ONCE: %d gone at N=%d" % (p, n))
        wo_checks += 1
print("  growth monoid COMMUTATIVE over %d (state,move,move) triples --" % comm_checks)
print("    order-blind composition = Petri/VASS, not a stack")
print("  D-IND presence WRITE-ONCE over %d tests: the admissible-to-open" % wo_checks)
print("    set only shrinks -- chamber 8's upward-closure at the presence bit")
print("  commutative + monotone + finite zero-pattern = a WSTS =>")
print("  decidable termination => NOT Turing-complete")
print()


# ------------------------------------------------------------------ #
# S6 -- THE WITNESS READING (finding 6, cashes VERTIGO STOCK (c))
# ------------------------------------------------------------------ #
print("S6 -- THE WITNESS READING (schedules per endpoint)")

def schedule_count(n):
    """Number of ordered one-prime-at-a-time schedules building N by
    multiplication: multinomial (total moves)! / prod(depth_i!)."""
    e = depth_vec(n)
    total = sum(e.values())
    num = math.factorial(total)
    den = 1
    for a in e.values():
        den *= math.factorial(a)
    return num // den, total


for n in [30, 210, 2310, 30030, 510510, 2 * 3 ** 3 * 5 ** 2, 210 ** 2]:
    cnt, total = schedule_count(n)
    ok(cnt >= 1, "at least one schedule")
    print("  N=%-8d moves=%2d  schedules=%d" % (n, total, cnt))
# squarefree primorial p_k#: schedules = k! -- factorial in the window
# count, all collapsing to one endpoint (route-weight cancellation).
for n, kfac in [(30, 6), (210, 24), (2310, 120), (30030, 720)]:
    cnt, _ = schedule_count(n)
    ok(cnt == kfac, "primorial schedule count = k! (N=%d)" % n)
# endpoint under-determines history: state forgets the route entirely.
c1, _ = schedule_count(510510)
ok(c1 == math.factorial(7), "p_7# reached by 7! = 5040 routes, one endpoint")
print("  primorial p_k# reached by k! routes -> one endpoint: the state")
print("  certifies the move MULTISET (what), never the ROUTE (history).")
print("  witness-readable, state-deniable computation (VERTIGO STOCK c).")
print()

print("ALL CHECKS PASS: %d" % CHECKS)
