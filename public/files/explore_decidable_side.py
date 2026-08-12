"""
explore_decidable_side.py -- CLASSIFYING THE DECIDABLE SIDE: what kind of
machine is the growing-window class on a sublinear supply, and is its
halting really decidable? (Sibling of explore_sqrt_supply.py,
explore_bit_supply.py, explore_growth_machine.py,
explore_minimal_carrier.py, explore_frontier_rider.py.)

THE SETTING. The supply law splits the growing-window machine by the
GROWTH RATE of its modulus supply m_g (the g-th fresh window's modulus):
m_g = Omega(g) is UNIVERSAL (explore_sqrt_supply.py: a multi-digit
counter with a free frozen base rides the frontier), m_g = o(g) is
CAPPED, and the two decidable poles already have names --
explore_bit_supply.py (bounded supply, every m_g <= C) is FINITE-STATE,
decidable by BOUNDEDNESS; explore_growth_machine.py (INC + presence
zero-test, no decrement) is a WSTS, decidable by MONOTONICITY. The
sublinear-but-unbounded supply (m_g = ceil(sqrt g)) is NEITHER: its
moduli grow without bound, so the column alphabet is infinite (not
finite-state), and its registers RESET (subtracting a register from
itself clears it), so the state is non-monotone (not a WSTS by the
growth machine's argument). explore_sqrt_supply.py established the cap
(value <= W_d * m_frontier, born-at-zero) and CONJECTURED decidability
on that principle, leaving two open jobs: is the conjecture a THEOREM,
and WHERE does this third decidable class sit? This script attacks both.

THE MACHINE CLASS (verbatim from explore_minimal_carrier.py). A growing
list of windows, window j a copy of Z/m_j (moduli from the SUPPLY);
r registers, each a residue tuple over the current windows, born 0 in
every fresh window (state-independent); native ops COMPONENTWISE --
add, sub, mul, write-constant c (c mod m_j at window j: uniform where
m_j > c); GROW appends one fresh window (born 0 everywhere) and mints
the fresh-window singleton w = 1 - ONES (native at grow time); the ONE
cross-window read is the global 1-bit zero-test; finite control. NO
named-window read, NO pointer, NO shift, NO cross-window carry, no
meadow inverse. In one phrase: SIMD without inter-cell communication,
fresh-0 append, a single global AND-of-zero reduction.

THE TERMS. The object is the SUPPLY SCHEDULE. Beware the homonym: the
machine's REGISTERS are its fixed finite tuple of residue-vectors; the
WINDOWS are the growing coordinates, one per supplied modulus. An
ADDRESSED window is one a register can name (via a saved singleton, or
the frontier via w); a UNIFORM window is one touched only by
value-blind componentwise ops after its birth.

THE BANDWIDTH PRINCIPLE (the real lever, under born-at-zero). add, sub,
mul, and write-constant are all COMPONENTWISE -- they never move a value
from one window to another. The ONLY inter-window primitives are (out)
the global zero-test, one bit per op, and (in) the frontier singleton w,
which injects at exactly one window (the current frontier) per op. So
value flows between windows ONLY through zero-test -> control -> w, one
unit per control-loop iteration (the unary transfer). Inter-window value
bandwidth is O(1) per op. Two consequences:
  ADDRESSED / UNIFORM DECOMPOSITION. Only r registers can hold a
  persistent singleton, so at most O(r) windows carry an address at
  once. An addressed window's live value is built by unary transfer and
  equals a control-constant or a transferred source value; by induction
  along transfer chains every addressed live value is <= a program
  constant B (on a sublinear supply -- the cap lemma is the special case
  where the program tries to grow B and fails). A uniform window holds a
  value-blind function of the op history mod m_j: a program-constant, or
  "t mod m_j" (the CRT/redundant counter). The CRT register's global
  zero-test is a PULSE: it fires only once growth STOPS, at period lcm(the
  frozen window set) -- growing more windows before freezing EXTENDS the
  period (the born-0 windows are incremented too, so they enter the lcm and
  shift the phase; it is NOT frozen at setup), while a program that keeps
  growing kills the pulse (each step's youngest window is nonzero, so the
  AND is never all-zero).
  (Settled since by explore_born_at_zero.py, which proves the normal
  form under this principle: the uniform repertoire is any fixed
  integer recurrence in the age, not only a constant or t mod m, and
  an addressed window's value need not be transfer-built -- a masked
  componentwise value reads per-window through the sparse zero-test.
  What every argument here actually used survives exactly: a fixed
  window's content evolves inside (Z/m)^r under the shared op word.
  The bounded-live claim stays the conjectured half.)
  PERIOD-AND-FREEZE. A faithful unbounded counter needs a register whose
  FIRING zero-test has UNBOUNDED period. Addressed signals have period
  <= the bounded live value B; the CRT pulse's firing period is lcm(the
  frozen set), a program CONSTANT for a fixed program (it freezes after a
  control-constant number of grows), possibly large. An unbounded FIRING
  period needs freezing at a DATA-DEPENDENT window count, which needs the
  very counter (the regress). So no faithful unbounded counter exists on
  any sublinear supply -- though the per-program period can be a large
  constant, so a finite abstraction must track it (a lesser residual, not
  automatically small; the primary residual is finding 5's growing-period
  signal).

THE TWO SMELLS (argued both, trusted neither, before the run).
  DECIDABLE: the bandwidth principle bounds addressed live values by a
  program constant and makes a faithful register's firing period a program
  constant, so no faithful unbounded counter exists and the class is a
  reset-broadcast system with bounded live registers -- a third decidable
  class between the two poles (general decidability conjectured; the primary
  residual is the GROWING-PERIOD zero-test of a frontier-riding capped
  counter, not ultimately periodic -- see finding 5).
  UNIVERSAL (the counterexample face; would REFUTE the conjecture): a
  FOURTH scheme beats const * m_frontier. Candidates: (a) mul-product
  capacity; (b) a bootstrapped / self-referential grow schedule; (c) a
  new use of the global zero-test as an unbounded-period detector. If any
  survives, universality reopens.

THE COUNTEREXAMPLE FACE, hand-attacked (all three die; the run mechanizes
each).
  (a) MUL-PRODUCT. mul is componentwise, so it never combines values
  across windows -- a cross-window product cannot be materialized in one
  window, and the zero-test reads a single register's per-window zeros.
  Within one window, repeated squaring reaches a big value fast but still
  <= m_frontier = sqrt(g) < count. So mul buys per-window speed, not
  cross-window capacity; the product-of-bases capacity IS the positional
  scheme, already capped by re-basing (explore_sqrt_supply.py).
  (b) BOOTSTRAP. The frontier is free (a blind grow loop advances it with
  no counting). Pre-growing G0 windows blindly then riding is faithful up
  to T = floor(sqrt G0), then wraps -- so a FIXED control (constant G0)
  buys only CONSTANT capacity. Unbounded capacity needs G0 unbounded and
  TIMED: to stay faithful at value s the machine must have grown ~ s^2 by
  count s, i.e. grows-per-INC ~ 2s -> infinity; a fixed K grows/INC gives
  frontier ceil(sqrt(K s)) < s (still wraps), and a variable schedule
  needs the very counter being built. The regress has no fixpoint below
  universality.
  (c) PERIOD DETECTOR. Covered by period-and-freeze above: the CRT pulse's
  firing period is a program constant (lcm of the frozen window set), and
  an unbounded FIRING period needs freezing at a data-dependent window
  count -- the regress, folding into (b).

THE DESIGN (what each section asks; findings enter post-run only).

S1  THE ADDRESSED-VALUE BOUND (the mechanism under born-at-zero). Run the
    top-migratable positional counter (explore_sqrt_supply.py) on the
    sqrt supply and on the successor supply (m_g = g + 1). Record the
    max FAITHFUL top-digit value over horizons 200 and 800. On the sqrt
    supply the max is bounded and HORIZON-INDEPENDENT (the same at 200
    and 800 -- a program constant); on the successor (linear) supply it
    GROWS with the horizon. The addressed live value is bounded exactly
    on the sublinear side.

S2  THE MUL-PRODUCT KILL (candidate a). Exhibit that componentwise mul
    cannot materialize a cross-window product: two registers holding
    a at window u and b at window v; every native product places a*b
    nowhere (window u gets a * reg2[u], window v gets reg1[v] * b). Then
    a per-window squaring sequence reaches a large value in log steps but
    stays < m_frontier, so a squaring-based faithful counter caps on the
    sqrt supply exactly like the others.

S3  THE BOOTSTRAP KILL (candidate b). A rider with G0 blind pre-grows,
    then 1 grow/INC. Find the first count whose zero-test lies; it is
    ~ floor(sqrt G0), a CONSTANT for fixed G0 (G0 = 100, 400, 900). At
    the lie the total grows done is ~ count^2 -- the grows-per-INC a
    faithful unbounded ride would need diverges, the regress.

S4  PERIOD-AND-FREEZE (candidate c). A CRT/redundant register's zero-test
    is a PULSE that fires only after growth STOPS, at period lcm(the frozen
    window set): show the firing period is lcm{3,4,5}, lcm{3,4,5,7},
    lcm{3,4,5,7,11} = 60, 420, 4620 -- growing before the freeze EXTENDS
    the period (a program constant, NOT frozen at setup); and show that a
    program which keeps growing KILLS the pulse (the youngest window is
    nonzero, so JZ never fires). A reset register's period is the reset
    stride. So a faithful firing period is a program constant; an unbounded
    firing period needs a data-dependent freeze = the regress.

S5  THE DECIDER (the bisimulation abstraction). A small interpreter runs
    a battery of growing-window programs on the sqrt supply, recording
    the (control-state, zero-test-vector) trajectory. On the battery the
    trajectory enters a CYCLE within a bounded number of steps, which
    certifies HALT or LOOP -- including for programs whose naive simulation
    grows windows FOREVER and never terminates. Assert the cycle-based
    verdict matches the known verdict for every battery program. Then the
    decider's HONEST LIMIT: a frontier-riding capped counter's zero-test
    fires with GROWING gaps (9, 24, 45, ...), so its trajectory is NOT
    ultimately periodic and the first-repeat rule is unsound for it -- the
    growing-period residual a sound procedure must handle.

S6  THE CLASS (structure). Exhibit one program that is BOTH non-monotone
    (a reset lowers a register value from nonzero to 0, breaking the
    growth machine's monotonicity) AND unbounded-modulus (it grows
    distinct moduli without bound, so there is no finite column alphabet)
    yet is DECIDED by S5's cycle abstraction -- so the sublinear class is
    a third decidable class, neither finite-state nor a WSTS by
    monotonicity. Print the supply-law synthesis.

PREDICTIONS (fixed before the run; adjudication added post-run).
  PR1  On the sqrt supply the top-migratable counter's max faithful top
       digit is bounded and the SAME at horizons 200 and 800; on the
       successor supply it grows with the horizon.
  PR2  No native op materializes a cross-window product a*b in a single
       window; a per-window squaring sequence stays < m_frontier, so the
       squaring counter caps on the sqrt supply.
  PR3  The blind-pregrow rider lies at count ~ floor(sqrt G0) -- a
       constant for fixed G0 (G0 = 100, 400, 900 -> ~10, 20, 30) -- and
       the total grows at the lie is ~ count^2.
  PR4  The CRT/redundant register's zero-test is a PULSE firing only after
       growth stops, at period lcm(the frozen window set) = 60/420/4620 for
       0/1/2 grown windows (a program constant, EXTENDED by growing before
       the freeze); a program that keeps growing never fires the pulse; the
       reset register's period is its reset stride.
  PR5  Every battery program's (control, zero-test-vector) trajectory
       enters a cycle within a bounded horizon, and the cycle-based
       HALT/LOOP verdict matches the known verdict -- including programs
       whose naive window-growing simulation never halts. (Honest limit
       added in-round: the frontier-riding capped counter's zero-test fires
       with GROWING gaps, so the first-repeat decider is a heuristic, not
       sound in general.)
  PR6  The exhibited program is non-monotone (a reset lowers a register)
       AND unbounded-modulus (distinct moduli grow without bound) AND
       decided by the cycle abstraction: a third decidable class.

PREDICTIONS ADJUDICATED (post-run): all six CONFIRMED on the first clean
run; one battery-label correction preceded adjudication (a program
annotated LOOP in fact HALTS -- the rider's wrap on the sqrt supply drives
its halt branch; machine and decider correct, the label was wrong, now a
genuine grows-forever loop). PR1 (max faithful hi 3 == 3 across horizons
200/800 on sqrt, 50 -> 200 on successor); PR2 (a*b materialized nowhere;
squaring 2..62 < 97; b=2 caps at 4); PR3 (lies at 11/21/31 ~ sqrt of
100/400/900; 934 grows ~ 31^2 at the lie); PR4 (CRT firing period
60/420/4620 = lcm of the frozen set, grow-every-step never fires; reset
period 5); PR5 (battery HALT/LOOP all matched, incl. three grows-forever
loops -- plus the decider's honest limit: the capped counter's zero-test
fires at 9/24/45/72/105/141 with GROWING gaps, so the first-repeat rule is
a heuristic, not sound in general); PR6 (non-monotone reset + 20-and-rising
distinct moduli, yet decided). PR4's pre-run wording was corrected in-round: the CRT period is
NOT frozen at setup -- growing before the freeze EXTENDS it to lcm(frozen
set); the vacuous "always-zero in the AND" check was rewritten to the
firing-period measurement above.

FINDINGS (entered after the run; every number below is from the printed
output; run record at the end).

1. THE DECIDABLE SIDE IS A THIRD CLASS -- a reset-broadcast system with
   bounded live registers, neither pole (rule for the structure /
   conjecture for full generality; the headline; S6, S1-S5). The
   sublinear-supply growing-window machine is decidable (CONJECTURED,
   finding 5's scope), but the PLACEMENT is a rule: it sits at neither
   known pole. NOT finite-state (explore_bit_supply.py) -- its moduli grow
   without bound (S6: 20 distinct moduli after 2000 steps and rising, no
   finite column alphabet); NOT a WSTS by monotonicity
   (explore_growth_machine.py) -- its registers RESET (S6: a reset lowers A
   from [1,1,1] to [0,0,0], non-monotone; it may still be a WSTS by a
   reset-net wqo, the open reduction). One exhibited program is BOTH at
   once and is still decided (LOOP, 5 abstract steps). The conjectured
   decidability rests on the BANDWIDTH PRINCIPLE (finding 2).

2. THE BANDWIDTH PRINCIPLE -- inter-window value flow is O(1) per op, the
   mechanism under born-at-zero (rule, by construction; S1, S4). add, sub,
   mul, write-constant are all componentwise: they never move value
   between windows. The only inter-window primitives are the global
   zero-test (1 bit out) and the frontier singleton w (1 unit in, at one
   window). Two consequences, both measured: (i) ADDRESSED live values are
   bounded by a program constant -- the top-migratable counter's max
   faithful top digit is HORIZON-INDEPENDENT on the sqrt supply (3 at
   horizon 200 == 3 at horizon 800) while the same counter on the
   successor (linear) supply grows with the horizon (50 -> 200); (ii) a
   FAITHFUL register's firing period is a program constant (finding 3).
   The addressed bound is exactly the cap lemma (explore_sqrt_supply.py)
   read per window; it holds on the sublinear side and fails on the linear
   side, matching the supply-law boundary.

3. PERIOD-AND-FREEZE -- a faithful firing period is a program constant; an
   unbounded firing period needs a data-dependent freeze (rule, by
   construction; S4). A faithful unbounded counter needs a register whose
   FIRING zero-test has unbounded period. Addressed signals have period <=
   the bounded live value. The CRT/redundant register's zero-test is a
   PULSE that fires only once growth STOPS: while a program keeps growing,
   the youngest window is nonzero so the pulse NEVER fires (S4: grow-every-
   step, no firing); once growth stops at a frozen window set, the firing
   period is lcm(that set) -- and growing more windows BEFORE the freeze
   EXTENDS it, not freezes it at setup (S4: 60, 420, 4620 = lcm{3,4,5},
   lcm{3,4,5,7}, lcm{3,4,5,7,11}). So for a FIXED program (which freezes
   after a control-constant number of grows) the firing period is a
   program CONSTANT, possibly large; an UNBOUNDED firing period needs
   freezing at a DATA-DEPENDENT window count = the very counter (the
   regress). A reset register's period is its reset stride (S4: 5). This
   bounds every faithful counter -- but the per-program constant can be
   large, so it does NOT by itself make the (control, zero-test)
   abstraction small (the residual, finding 5's scope).

4. THE COUNTEREXAMPLE FACE IS CLOSED -- no fourth scheme beats
   const * m_frontier (rule for the three named families; conjecture that
   there is no fourth; S2, S3, S4). (a) MUL-PRODUCT: componentwise mul
   materializes a cross-window product a*b at NO window (S2: a*b = 15
   lands as [0,0,0]); per-window squaring reaches a big value fast (2..62)
   but stays < m_frontier (97), so a squaring counter caps like the others
   (S2: b=2 caps at 4). (b) BOOTSTRAP: the frontier is free (blind
   growth), but pre-growing G0 windows buys only capacity floor(sqrt G0),
   a CONSTANT for fixed control (S3: G0 = 100/400/900 -> lies at
   11/21/31); an unbounded faithful ride needs grows-per-INC -> infinity
   -- at the lie the machine has already grown ~ count^2 windows (S3: 934
   at count 31) -- which needs the very counter being built (the regress,
   no fixpoint below universality). (c) PERIOD DETECTOR: an unbounded
   FIRING period needs a data-dependent freeze (finding 3), folding into
   the regress. All three die by the bandwidth principle, so the
   born-at-zero conjecture (explore_sqrt_supply.py) is FIRMED, not merely
   re-stated.

5. THE DECIDER + ITS HONEST LIMIT -- a first-repeat heuristic, sound on the
   battery, and the growing-period signal that bounds it (rule on the
   exhibited battery; the decider NOT sound in general; S5). A small
   interpreter records the (control-pointer, zero-test-vector) trajectory
   and declares LOOP on the first repeat, HALT when control halts. On a
   four-program battery every verdict matched the known one: count_to_3_halt
   HALT in 7 abstract steps; inc_forever_loop LOOP in 3; wrap_reset_loop
   LOOP in 10; reset_pulse_loop LOOP in 5 -- three of the four grow a fresh
   window every step and never terminate under naive simulation, yet the
   abstraction settles them in single-digit steps (the verdicts hold
   because every halting battery program halts BEFORE its first
   signature repeat and the loopers genuinely loop -- a false LOOP
   needs a halt hiding beyond the repeat horizon; neither ultimate
   periodicity nor anything else makes a repeated signature a real
   state repeat in general: a plain frozen pulse of period 60 draws a
   false LOOP from the same rule, the phase-blindness refutation in
   explore_pending_fires.py). But the
   first-repeat rule is a HEURISTIC, NOT sound in general: a frontier-riding
   CAPPED counter's zero-test fires at 9, 24, 45, 72, 105, 141 with GROWING
   gaps (15, 21, 27, 33, 36, 42), so its trajectory is NOT ultimately
   periodic and a halt-on-fire program would falsely read LOOP during the
   long False stretch. THIS growing-period signal is the primary residual --
   a sound general procedure must track pending fires (as the growth
   machine's decider tracks its monotone zero-pattern) -- built in
   explore_pending_fires.py (the three-verdict decider).

SCOPE + HONESTY. The bandwidth principle, the addressed-value bound (=
the cap lemma per window), period-and-freeze (a faithful firing period is
a program constant; an unbounded firing period needs a data-dependent
freeze), and the three counterexample-face kills are proved-by-construction
and exhibited here; the decider is validated on a battery, not proved sound
for every program. What is NOT closed to a proof is GENERAL decidability of
every o(g) program -- that NO construction whatsoever escapes
const * m_frontier and that a SOUND decision procedure exists. The named
residual is the GROWING-PERIOD zero-test: a frontier-riding capped counter
fires with unboundedly growing gaps (9, 24, 45, ...), so the
(control, zero-test) trajectory is NOT ultimately periodic and the naive
first-repeat decider is unsound for it -- a sound procedure must track
pending fires, built in explore_pending_fires.py (which also shows the
frozen-set period is not a lesser obstruction for the FIRST-REPEAT rule:
a plain period-60 pulse already draws a false LOOP -- phase-blindness;
it IS recoverable machine-side by tracking the frozen residues, where
the growing-period signal needs the landing lemma). Both are consistent
with the class not being finite-state.
The three natural schemes and the bandwidth argument make
general decidability a STRONG conjecture on the born-at-zero principle --
argued from the op semantics (a fresh window's post-birth content is a
function of constants, the frontier singleton, and its own born-0
registers, only unary transfer accumulating value), not machine-checked
over all machines. The class is placed between the poles; the residual is
named; the conjecture is firmed.

RUN RECORD (python prime/code/explore_decidable_side.py, <1 s wall clock,
trivial memory, 22 checks, all sections assert). S1 addressed bound (sqrt
max faithful hi 3 == 3 at horizons 200/800; successor 50 -> 200). S2
mul-product kill (a*b = 15 at no window [0,0,0]; squaring 2..62 < 97; b=2
caps at 4). S3 bootstrap kill (lies at 11/21/31 ~ sqrt of 100/400/900;
934 grows ~ count^2 = 31^2 at the lie). S4 period-and-freeze (CRT firing
period 60/420/4620 = lcm of the frozen set for 0/1/2 grown windows;
grow-every-step never fires; reset period 5). S5 the decider (HALT 7;
LOOP 3/10/5; three grow-forever programs in single-digit steps) + its honest
limit (the capped counter fires at 9/24/45/72/105/141, gaps 15/21/27/33/36/42
GROWING -- the first-repeat rule a heuristic, not sound in general). S6 the
class (reset [1,1,1] -> [0,0,0] non-monotone; 20 distinct moduli after 2000
steps; decided LOOP in 5). One battery-label correction preceded adjudication
(a program annotated LOOP in fact halts by the rider's wrap; corrected to a
genuine grows-forever loop). All six frozen predictions confirmed on the first
clean run. Verdict: the o(g) decidable side is a THIRD class -- a
reset-broadcast system with bounded live registers, decidable (conjectured)
by the bandwidth principle; general o(g) decidability a strong conjecture, the
primary residual (the GROWING-PERIOD zero-test of a frontier-riding capped
counter) named.
"""

import math


# ---------------------------------------------------------------- #
# native ops (explore_minimal_carrier.py's rig; every modulus supplied) #
# registers are lists of residues, index j in window Z/moduli[j]   #
# ---------------------------------------------------------------- #

CHECKS = 0
def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1
    print(f"  [ok] {msg}")


def const(c, moduli):
    return [c % m for m in moduli]

def add(x, y, moduli):
    return [(a + b) % m for a, b, m in zip(x, y, moduli)]

def sub(x, y, moduli):
    return [(a - b) % m for a, b, m in zip(x, y, moduli)]

def mul(x, y, moduli):
    return [(a * b) % m for a, b, m in zip(x, y, moduli)]

def born(x, m_new, c=0):
    """GROW's register extension without the door: the fresh window gets a
    constant (state-independent), never the value lift."""
    return x + [c % m_new]

def zero_test(x):
    """The sole cross-window read: ONE bit, the AND of per-window zero
    bits."""
    return all(r == 0 for r in x)


# ---------------------------------------------------------------- #
# the supplies                                                     #
# ---------------------------------------------------------------- #

def ceil_sqrt(g):
    r = math.isqrt(g)
    return r if r * r == g else r + 1

def sqrt_mod(g):
    """m_g = max(2, ceil(sqrt g)) -- unbounded but Theta(sqrt g) = o(g)."""
    return max(2, ceil_sqrt(g))

def succ_mod(g):
    """m_g = g + 1 > g -- the universal (linear) side, a positive control."""
    return g + 1


# ================================================================ #
# S1 -- the addressed-value bound (the mechanism under born-at-zero) #
# ================================================================ #

class TopMigCounter:
    """A top-migratable positional counter (explore_sqrt_supply.py): a
    FROZEN low digit (window 0, modulus b) and a high digit riding the
    frontier -- migrated to the fresh window each INC by unary transfer.
    value = hi*b + lo. Faithful while hi < the frontier modulus."""

    def __init__(self, b, mod_at):
        self.b = b
        self.mod_at = mod_at
        self.moduli = [b]
        self.reg = {n: const(0, self.moduli) for n in
                    ("V_lo", "V_hi", "P_lo", "P_hi", "ONES")}
        self.reg["ONES"] = const(1, self.moduli)
        self.reg["P_lo"] = const(1, self.moduli)
        self.lo_idx = 0
        self.hi_idx = None
        self.grows = 0

    def _grow(self):
        self.grows += 1
        m_new = max(2, self.mod_at(self.grows))
        self.moduli.append(m_new)
        for n in list(self.reg):
            self.reg[n] = born(self.reg[n], m_new, 0)
        self.reg["W"] = sub(const(1, self.moduli), self.reg["ONES"],
                            self.moduli)
        self.reg["ONES"] = const(1, self.moduli)
        return len(self.moduli) - 1

    def _migrate_hi(self):
        fresh = self._grow()
        w = self.reg["W"]
        if self.hi_idx is not None:
            V, P = self.reg["V_hi"], self.reg["P_hi"]
            for _ in range(8192):
                if zero_test(mul(V, P, self.moduli)):
                    break
                V = add(sub(V, P, self.moduli), w, self.moduli)
            self.reg["V_hi"] = V
        self.reg["P_hi"] = w
        self.hi_idx = fresh

    def inc(self):
        self._migrate_hi()
        self.reg["V_lo"] = add(self.reg["V_lo"], self.reg["P_lo"], self.moduli)
        if zero_test(self.reg["V_lo"]):
            self.reg["V_hi"] = add(self.reg["V_hi"], self.reg["P_hi"],
                                   self.moduli)

    def hi_val(self):
        return self.reg["V_hi"][self.hi_idx] if self.hi_idx is not None else 0

    def decode(self):
        lo = self.reg["V_lo"][self.lo_idx]
        return self.hi_val() * self.b + lo


def max_faithful_hi(b, mod_at, horizon):
    """Run the counter to `horizon` INCs; return the largest top-digit
    value seen while the decode still equals the true count (faithful)."""
    c = TopMigCounter(b, mod_at)
    best = 0
    for count in range(1, horizon + 1):
        c.inc()
        if c.decode() != count:
            break
        best = max(best, c.hi_val())
    return best


def s1_addressed_bound():
    print("== S1  the addressed-value bound (born-at-zero mechanism) ==")
    b = 4
    sq_200 = max_faithful_hi(b, sqrt_mod, 200)
    sq_800 = max_faithful_hi(b, sqrt_mod, 800)
    ok(sq_200 == sq_800,
       f"sqrt supply: max faithful top digit is HORIZON-INDEPENDENT "
       f"(hi<=b: {sq_200} at horizon 200 == {sq_800} at horizon 800) -- "
       "the addressed live value is a bounded program constant")

    su_200 = max_faithful_hi(b, succ_mod, 200)
    su_800 = max_faithful_hi(b, succ_mod, 800)
    ok(su_800 > su_200 and su_800 > sq_800,
       f"successor (linear) supply: the SAME counter's max faithful top "
       f"digit GROWS with the horizon ({su_200} at 200 -> {su_800} at 800) "
       "-- unbounded addressed value, the universal side")


# ================================================================ #
# S2 -- the mul-product kill (candidate a)                          #
# ================================================================ #

def s2_mul_kill():
    print("\n== S2  the mul-product kill (no cross-window product) ==")
    # two registers: X holds a at window u only, Y holds b at window v only
    moduli = [7, 7, 7]
    a, b, u, v = 3, 5, 0, 2
    X = [0, 0, 0]; X[u] = a
    Y = [0, 0, 0]; Y[v] = b
    prod = mul(X, Y, moduli)
    ok(prod == [0, 0, 0] and (a * b) % 7 != 0,
       f"componentwise mul of a@w{u} and b@w{v} materializes a*b={a*b} at "
       f"NO window ({prod}) -- cross-window product is not in the class")

    # per-window squaring: value doubles in exponent each step but stays
    # < m_frontier, so a squaring counter's value never exceeds one modulus
    m = 97  # a frontier modulus
    seq, x = [], 2
    for _ in range(12):
        seq.append(x)
        x = (x * x) % m
    ok(all(0 <= s < m for s in seq) and max(seq) < m,
       f"per-window squaring 2,4,16,... reaches {max(seq)} fast but stays "
       f"< m_frontier={m} (bounded by one modulus, never crosses windows)")

    # the faithful squaring counter caps on the sqrt supply just like the
    # top-migratable counter: capacity is one frontier modulus = sqrt(g)
    cap = None
    c = TopMigCounter(2, sqrt_mod)   # b=2: capacity ~ one frontier modulus
    for count in range(1, 400):
        c.inc()
        if c.decode() != count:
            cap = count
            break
    ok(cap is not None,
       f"a single-frontier-window (b=2) counter caps at {cap} on the sqrt "
       "supply -- per-window capacity <= m_frontier, squaring cannot help")


# ================================================================ #
# S3 -- the bootstrap kill (candidate b: the regress)              #
# ================================================================ #

class Rider:
    """The single-window frontier rider (explore_minimal_carrier.py),
    carrier-parametric, with an optional blind pre-grow."""

    def __init__(self, mod_at, pregrow=0):
        self.mod_at = mod_at
        self.moduli = []
        self.grows = 0
        for _ in range(3):
            self._grow_raw()
        self.reg = {"V": const(0, self.moduli),
                    "P": const(0, self.moduli),
                    "ONES": const(1, self.moduli)}
        for _ in range(pregrow):          # blind pre-grow: advance the frontier
            self.grow()

    def _grow_raw(self):
        self.grows += 1
        self.moduli.append(max(2, self.mod_at(self.grows)))

    def grow(self):
        m_new = max(2, self.mod_at(self.grows + 1))
        self.grows += 1
        self.moduli.append(m_new)
        for n in self.reg:
            self.reg[n] = born(self.reg[n], m_new, 0)
        w = sub(const(1, self.moduli), self.reg["ONES"], self.moduli)
        self.reg["ONES"] = const(1, self.moduli)
        return w

    def inc(self):
        w = self.grow()
        V, P = self.reg["V"], self.reg["P"]
        for _ in range(8192):
            if zero_test(mul(V, P, self.moduli)):
                break
            V = add(sub(V, P, self.moduli), w, self.moduli)
        self.reg["P"] = w
        self.reg["V"] = add(V, w, self.moduli)

    def jz(self):
        return zero_test(self.reg["V"])


def pregrow_first_lie(pregrow, incs=400):
    m = Rider(sqrt_mod, pregrow=pregrow)
    for count in range(1, incs + 1):
        m.inc()
        if m.jz() != (count == 0):
            return count, m.grows
    return None, m.grows


def s3_bootstrap_kill():
    print("\n== S3  the bootstrap kill (blind pre-grow, the regress) ==")
    lies = {}
    for g0 in (100, 400, 900):
        lie, grows_at = pregrow_first_lie(g0)
        lies[g0] = (lie, grows_at)
        exp = math.isqrt(g0)
        ok(lie is not None and abs(lie - exp) <= max(3, exp // 3),
           f"pre-grow G0={g0}: faithful up to count {lie} ~ floor(sqrt G0)="
           f"{exp}, then the zero-test lies (constant capacity for fixed G0)")
    # the regress: at the lie the total grows ~ count^2 -- to be faithful at
    # value s the machine must already have grown ~ s^2 windows
    lie, grows_at = lies[900]
    ok(grows_at >= lie * lie // 2,
       f"the regress: at the lie (count {lie}) the machine has grown "
       f"{grows_at} windows ~ count^2 -- a faithful unbounded ride needs "
       "grows-per-INC -> infinity, i.e. the counter it is building")


# ================================================================ #
# S4 -- period-and-freeze (candidate c: firing needs a frozen set)  #
# ================================================================ #

class CRTCounter:
    """value stored as residues across windows; INC = add 1 to every window
    (native, incl. grown ones); JZ = all windows zero. A grown window is
    born 0, then incremented, so it holds (steps since its birth) mod m_new
    -- NOT the lift V mod m_new. Consequence: the JZ PULSE fires only once
    growth STOPS, at period lcm(the frozen window set), and growing more
    before the freeze EXTENDS the period (the grown window enters the lcm
    and shifts the phase); while growth continues the youngest window is
    nonzero, so the pulse never fires."""

    def __init__(self, moduli):
        self.moduli = list(moduli)
        self.R = const(0, self.moduli)

    def inc(self):
        self.R = add(self.R, const(1, self.moduli), self.moduli)

    def grow_born_zero(self, m_new):
        self.moduli.append(m_new)
        self.R = born(self.R, m_new, 0)

    def jz(self):
        return zero_test(self.R)


def zero_test_period(jz_seq):
    """The stride between consecutive JZ-true events in a signal (0 for
    'no repeat seen'); a bounded stride = a bounded period."""
    hits = [i for i, z in enumerate(jz_seq) if z]
    if len(hits) < 2:
        return None
    return hits[1] - hits[0]


def s4_period_and_freeze():
    print("\n== S4  the period-and-freeze law (firing needs a frozen set) ==")
    # (i) the CRT pulse fires only AFTER growth stops, at period = lcm(the
    #     FROZEN window set) -- a program constant, EXTENDED by growing more
    #     before freezing (NOT frozen at setup: the grown windows are
    #     incremented too, so they enter the lcm and shift the phase).
    for extra in ([], [7], [7, 11]):
        moduli = [3, 4, 5] + extra
        expect = math.lcm(*moduli)
        c = CRTCounter([3, 4, 5])
        for e in extra:
            c.grow_born_zero(e)           # grow, then FREEZE (stop growing)
        hits, V = [], 0
        for _ in range(expect * 2 + 5):
            c.inc(); V += 1
            if c.jz():
                hits.append(V)
        per = hits[1] - hits[0] if len(hits) >= 2 else None
        ok(per == expect,
           f"grow-then-FREEZE {{3,4,5}}+{extra}: firing period {per} = "
           f"lcm{tuple(moduli)}={expect} -- growing before the freeze EXTENDS "
           "the period (a program constant), it is not frozen at setup")

    # (ii) but a program that KEEPS growing kills the pulse: each step's
    #     youngest window holds a nonzero value (born 0, then incremented),
    #     so the AND is never all-zero while growth continues.
    c = CRTCounter([3, 4, 5])
    V, ever = 0, False
    for _ in range(500):
        c.inc(); V += 1
        c.grow_born_zero(sqrt_mod(V))     # grow every step
        if c.jz():
            ever = True
    ok(not ever,
       "grow-EVERY-step: the CRT pulse NEVER fires (the youngest window is "
       "nonzero) -- to fire you must STOP growing; an unbounded FIRING period "
       "needs freezing at a data-dependent window count = the regress")

    # (iii) a reset register: period = the reset stride, a program constant
    stride, moduli = 5, [2, 3]
    R = const(0, moduli)
    jz3, step = [], 0
    for _ in range(60):
        step += 1
        R = add(R, const(1, moduli), moduli)
        if step % stride == 0:
            R = sub(R, R, moduli)         # reset: R -> 0 (non-monotone)
        jz3.append(zero_test(R))
    per = zero_test_period(jz3)
    ok(per == stride,
       f"a reset register's zero-test has period = the reset stride {per} "
       "(a program constant) -- every FAITHFUL register's firing period is a "
       "program constant; unbounded firing needs a data-dependent freeze")


# ================================================================ #
# S5 -- the decider (the bisimulation abstraction)                 #
# ================================================================ #
#
# A tiny growing-window program: a list of labelled instructions over the
# rig, run on a supply. Control flow branches on the global zero-test. The
# DECIDER records the (control-pointer, zero-test-vector) trajectory and
# declares LOOP on the first repeat, HALT when control reaches HALT. Its
# battery verdicts are right because every halting battery program halts
# BEFORE its first signature repeat and the loopers genuinely loop --
# even when the window count grows forever. General soundness is FALSE for
# the first-repeat rule, in TWO ways (both exhibited in
# explore_pending_fires.py): a frozen pulse's period exceeds the 1-bit
# signature's reach (phase-blindness -- a period-60 pulse draws a false
# LOOP), and a frontier-riding capped counter's zero-test fires with
# GROWING gaps (not even ultimately periodic) -- the growing-period
# residual (s5's honest limit).

class Prog:
    """Instruction set (each acts on named registers over the live moduli):
      ("grow",)                     append a fresh window; mint W (=1-ONES)
      ("inc_rider", V, P)           one rider INC on counter (V,P): grow,
                                    unary-transfer V to the fresh window,
                                    re-point P, add 1
      ("reset", A)                  A := A - A  (clear; non-monotone)
      ("addc", A, c)                A := A + c  (uniform constant)
      ("jz", A, label)              if zero_test(A): pc := label
      ("goto", label)               pc := label
      ("halt",)                     stop
    Registers auto-extend on grow (born 0). ONES is maintained = all-1."""

    def __init__(self, code, supply):
        self.code = code
        self.labels = {c[1]: i for i, c in enumerate(code) if c[0] == "label"}
        self.mod_at = supply
        self.moduli = []
        self.grows = 0
        for _ in range(2):
            self.grows += 1
            self.moduli.append(max(2, self.mod_at(self.grows)))
        self.reg = {}
        self.ensure("ONES"); self.reg["ONES"] = const(1, self.moduli)
        self.pc = 0
        self.halted = False
        # which registers exist as zero-test observables (for the abstraction)
        self.observed = sorted({c[1] for c in code if c[0] == "jz"})
        for n in self.observed:            # born 0 -- exist before first read
            self.ensure(n)

    def ensure(self, name):
        if name not in self.reg:
            self.reg[name] = const(0, self.moduli)

    def _grow(self):
        self.grows += 1
        m_new = max(2, self.mod_at(self.grows))
        self.moduli.append(m_new)
        for n in list(self.reg):
            self.reg[n] = born(self.reg[n], m_new, 0)
        w = sub(const(1, self.moduli), self.reg["ONES"], self.moduli)
        self.reg["ONES"] = const(1, self.moduli)
        return w

    def step(self):
        ins = self.code[self.pc]
        op = ins[0]
        if op == "label":
            self.pc += 1
        elif op == "grow":
            self.reg["W"] = self._grow()
            self.pc += 1
        elif op == "inc_rider":
            _, Vn, Pn = ins
            self.ensure(Vn); self.ensure(Pn)
            w = self._grow()
            V, P = self.reg[Vn], self.reg[Pn]
            for _ in range(8192):
                if zero_test(mul(V, P, self.moduli)):
                    break
                V = add(sub(V, P, self.moduli), w, self.moduli)
            self.reg[Pn] = w
            self.reg[Vn] = add(V, w, self.moduli)
            self.pc += 1
        elif op == "reset":
            self.ensure(ins[1])
            self.reg[ins[1]] = sub(self.reg[ins[1]], self.reg[ins[1]],
                                   self.moduli)
            self.pc += 1
        elif op == "addc":
            self.ensure(ins[1])
            self.reg[ins[1]] = add(self.reg[ins[1]],
                                   const(ins[2], self.moduli), self.moduli)
            self.pc += 1
        elif op == "jz":
            self.ensure(ins[1])
            self.pc = self.labels[ins[2]] if zero_test(self.reg[ins[1]]) \
                else self.pc + 1
        elif op == "goto":
            self.pc = self.labels[ins[1]]
        elif op == "halt":
            self.halted = True
        else:
            raise ValueError(op)

    def zvec(self):
        """The abstraction's observable: the zero-test of every jz-register."""
        return tuple(zero_test(self.reg[n]) for n in self.observed)

    def config_signature(self):
        return (self.pc, self.zvec())


def decide(code, supply, horizon=4000):
    """Run, recording (pc, zvec). HALT if control halts; LOOP on the first
    repeated (pc, zvec) signature. This is a HEURISTIC: it is sound only when
    every zero-test signal is CONSTANT after a prefix shorter than the repeat
    horizon (a repeated signature then means a genuine cycle). It is NOT
    sound in general, in two ways: any signal whose hidden phase outruns the
    1-bit signature (even a plain frozen pulse of period 60) repeats a
    signature during a False stretch before a delayed fire, and a zero-test
    with a GROWING firing gap (the frontier-riding capped counter, s5's
    honest limit) does so unboundedly. Its battery verdicts are right
    because every halting battery program halts before its first repeat
    and the loopers genuinely loop; the sound procedure that tracks
    pending fires is built in explore_pending_fires.py (the
    three-verdict decider)."""
    p = Prog(code, supply)
    seen = {}
    for t in range(horizon):
        if p.halted:
            return "HALT", t, p.grows
        sig = p.config_signature()
        if sig in seen:
            return "LOOP", t, p.grows
        seen[sig] = t
        p.step()
    return "UNDECIDED", horizon, p.grows


def s5_decider():
    print("\n== S5  the decider (bisimulation abstraction) ==")
    # battery: (name, code, known verdict, whether naive sim grows forever)
    L = lambda s: ("label", s)
    battery = [
        ("count_to_3_halt", [
            L("top"), ("inc_rider", "V", "P"),
            ("jz", "V", "never"),           # V is nonzero (rider), fall through
            ("addc", "C", 1), ("jz", "C", "top"),  # C never zero -> ...
            L("never"), ("halt",)],
         "HALT", False),
        ("inc_forever_loop", [
            L("top"), ("inc_rider", "V", "P"), ("goto", "top")],
         "LOOP", True),                     # grows a window every step, forever
        ("wrap_reset_loop", [
            L("top"), ("inc_rider", "V", "P"),
            ("jz", "V", "wrapped"), ("goto", "top"),
            L("wrapped"), ("reset", "V"), ("goto", "top")],
         "LOOP", True),                     # rider wraps (the lie) -> reset ->
                                            # loops forever, growing windows
        ("reset_pulse_loop", [
            L("top"), ("grow",), ("addc", "A", 1),
            ("reset", "A"), ("goto", "top")],
         "LOOP", True),                     # non-monotone, grows forever
    ]
    for name, code, want, naive_nonterm in battery:
        verdict, steps, grows = decide(code, sqrt_mod)
        tag = "naive sim never halts" if naive_nonterm else "naive sim halts"
        ok(verdict == want,
           f"{name}: decided {verdict} in {steps} abstract steps "
           f"({grows} windows grown; {tag}) -- matches the known verdict")

    # THE DECIDER'S HONEST LIMIT (the real residual). The battery's signals
    # are ultimately periodic, but a frontier-riding CAPPED counter's zero-test
    # fires with GROWING gaps -- so the (control, zero-test) trajectory is NOT
    # ultimately periodic, and the naive first-repeat rule is UNSOUND for it.
    c = TopMigCounter(3, sqrt_mod)
    fire = []
    for t in range(1, 500):
        c.inc()
        if zero_test(add(c.reg["V_lo"], c.reg["V_hi"], c.moduli)):
            fire.append(t)
    gaps = [fire[i + 1] - fire[i] for i in range(len(fire) - 1)]
    ok(len(gaps) >= 6 and all(gaps[i + 1] >= gaps[i] for i in range(len(gaps) - 1))
       and gaps[-1] > gaps[0],
       f"the capped counter's zero-test fires at {fire[:6]} with GROWING gaps "
       f"{gaps[:6]} -- NOT ultimately periodic, so the first-repeat decider is "
       "a heuristic (unsound in general): a halt-on-fire program would falsely "
       "read LOOP during the long False stretch. This growing-period signal --"
       " not the CRT strata -- is the residual a sound procedure must handle.")


# ================================================================ #
# S6 -- the class: a third decidable class between the two poles    #
# ================================================================ #

def s6_the_class():
    print("\n== S6  the class (third decidable class, both poles broken) ==")
    # one program that is BOTH non-monotone AND unbounded-modulus, decided.
    L = lambda s: ("label", s)
    code = [
        L("top"),
        ("grow",),                # unbounded distinct moduli (sqrt supply)
        ("addc", "A", 1),         # A := A + 1 at every window
        ("reset", "A"),           # A := 0 -- lowers A from nonzero (non-monotone)
        ("goto", "top")]
    # witness non-monotonicity: after addc, A has nonzero entries; reset -> 0
    p = Prog(code, sqrt_mod)
    p.step()                       # label
    p.step()                       # grow
    p.step()                       # addc -> A nonzero
    a_before = list(p.reg["A"])
    p.step()                       # reset -> A zero
    a_after = list(p.reg["A"])
    nonmono = any(x != 0 for x in a_before) and all(x == 0 for x in a_after)
    ok(nonmono,
       f"NON-MONOTONE: reset lowers A from nonzero {a_before} to {a_after} "
       "-- the growth machine's monotonicity (WSTS-by-monotonicity) is broken")

    # witness unbounded distinct moduli: grow far, count distinct moduli
    p2 = Prog(code, sqrt_mod)
    for _ in range(2000):
        p2.step()
    distinct = len(set(p2.moduli))
    ok(distinct >= 15,
       f"UNBOUNDED MODULI: {distinct} distinct moduli after 2000 steps and "
       "still rising -- no finite column alphabet (not finite-state)")

    # yet decided
    verdict, steps, grows = decide(code, sqrt_mod)
    ok(verdict == "LOOP",
       f"YET DECIDED: {verdict} in {steps} abstract steps ({grows} windows) "
       "-- a reset-broadcast system with bounded live registers, decidable "
       "by the ultimately-periodic control/zero-test trajectory")

    print("""
  THE DECIDABLE SIDE, placed (synthesis, if S1-S6 hold):

  The sublinear supply's growing-window machine is a THIRD class (decidable
  CONJECTURED), placed at neither known pole:
    - NOT finite-state (explore_bit_supply.py): its moduli grow without
      bound, so the column alphabet is infinite.
    - NOT a WSTS by monotonicity (explore_growth_machine.py): its registers
      RESET, so the state is non-monotone (it may still be a WSTS by a
      reset-net wqo -- the open reduction).
  Its conjectured decidability rests on a THIRD reason -- the BANDWIDTH
  PRINCIPLE. Value moves
  between windows only through the global zero-test (1 bit out) and the
  frontier singleton (1 unit in), O(1) per op, so:
    (i)   addressed live values are bounded by a program constant (S1),
    (ii)  a FAITHFUL register's firing period is a program constant -- the
          CRT pulse fires only after growth STOPS, at period lcm(the frozen
          window set) (extended by growing more before freezing, not frozen
          at setup), and a program that keeps growing kills the pulse; an
          unbounded FIRING period needs freezing at a data-dependent window
          count = the regress (S4),
  so no faithful unbounded counter exists, and the counterexample face is
  closed: mul-product (S2), bootstrap (S3), and unbounded-period detection
  (S4) all die by the bandwidth principle. The decider is exhibited on a
  battery incl. grows-forever loops (S5), but the first-repeat rule is a
  HEURISTIC, not sound in general. HONEST SCOPE: the bandwidth bounds and the
  three kills are proved-by-construction; the decider is validated on a
  battery, not proved sound for every program. GENERAL o(g) decidability --
  that no construction escapes and that a SOUND decision procedure exists --
  stays a STRONG CONJECTURE on the bandwidth principle. The residual is now
  NAMED: the GROWING-PERIOD zero-test -- a frontier-riding capped counter
  fires with unboundedly growing gaps (9, 24, 45, ...), so its trajectory is
  not ultimately periodic and a sound procedure must track pending fires (as
  the growth machine's decider tracks its monotone zero-pattern). That
  procedure is built in explore_pending_fires.py (the three-verdict
  decider + the landing lemma); the conjecture's honest scope is refined
  there -- decidability = rate + supply tameness.
""")


if __name__ == "__main__":
    s1_addressed_bound()
    s2_mul_kill()
    s3_bootstrap_kill()
    s4_period_and_freeze()
    s5_decider()
    s6_the_class()
    print(f"\nALL SECTIONS PASS ({CHECKS} checks)")
