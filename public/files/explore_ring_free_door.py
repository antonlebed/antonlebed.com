r"""explore_ring_free_door.py -- which of the door laws are facts about a
number ring, and which hold in any structure where an invariant only
accumulates.

THE QUESTION. The door monotonicity lemma reads: door(Q, e, L) is the
least r with lam(Q^(e+r)) not dividing L, so if L divides L' the set of r
that divide only grows and the least r outside it can only grow with it
(explore_support_growth.py Lemma B). Half of that statement has already
left the ring before the proof starts -- "a divisor set grows under
divisibility" is a fact about a transitive order, not about arithmetic --
and the other half is a HYPOTHESIS, that the place's own exponent is
untouched. So the question is whether the hypothesis is doing ring work
the order half is not; and if it is not, then every law resting on the
lemma rests on an accumulating invariant and the tower CARRIES those laws
rather than causing them. Where a law BREAKS once the ring is deleted, the
break names the exact arithmetic the tower contributes, which is the
better outcome and the one this file is hunting.

WHY THE ENGINE ALREADY ANSWERS HALF OF IT. explore_support_growth.py's
walker is parametric in a MODEL and touches the ring through six names
only -- UNIVERSE, place_norm, place_char, place_key, lam_P, lam_state.
Nothing downstream of those six knows what a number ring is. So a model
that supplies the six from a TABLE runs the same engine over a world with
no ring under it, and the laws can be read off one at a time. This file
writes no dynamics of its own: it imports the walker, the door, the
certificate, the support and race readers verbatim, and varies only the
world.

THE FOUR RING FACTS, isolated so they can be deleted one at a time. Each
is a property a number ring's column table has and an arbitrary table
need not.
  R1 THE COLUMN IS A CHAIN: lam(P^a) divides lam(P^(a+1)), because the
     unit group of O/P^(a+1) surjects onto that of O/P^a.
  R2 THE TICK GAP IS EVENTUALLY BOUNDED: the jump set of a -> lam(P^a) is
     eventually an arithmetic progression of step e_P (Lemma A: lam(P^a)
     = (q - 1) p^k(a) with k eventually arithmetic), so the vehicle's own
     door sequence is eventually periodic and its cost has a finite sup.
  R3 NORTHCOTT: only finitely many places carry norm at most any bound.
  R4 THE FIRST RUNG IS UNDER THE NORM: lam(Q^1) = N(Q) - 1, so the
     residue route's supply v_p(lam(Q^1)) is capped by the norm the walk
     had to pay for.
The claim under test is that Lemma B needs NONE of the four, and that the
four riders the corpus hangs on it need R2, R3 and R4 between them.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. The engine's --
place, norm, lam, door, cost, seated, invariant -- because the claim under
test is explore_support_growth.py's own and the riders are read in its
sections. The word RING appears here only as a property being deleted,
never as a term of the dynamics: the synthetic worlds have places and
ladders and no arithmetic beneath them, which is the whole point. The
clock family's vocabulary (tick ladder, tail gap) enters at R2 only, where
the jump set is the object, and it is flagged as the import it is.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 "The vehicle's doors are eventually periodic" is carried from the
    ring sweep, where the period read 1 at all twelve walks. It is a
    property of the WORLD here, constructed both ways, and never assumed:
    S3 reads the period off the simulated future by the imported
    _period, which returns None where there is none.
 T2 The horizon 500 is explore_support_growth.py's, so a synthetic
    reading sits beside a ring reading without rescaling. Nothing read at
    500 is a statement about infinity unless a certificate carries it.
 T3 The Northcott deletion is realized by a LARGE FINITE universe (600
    places of one norm), not by an infinite one, since the menu iterates
    a sorted universe. So its reading is a RATE over the horizon -- the
    support still growing at move 500 -- and never "the support is
    infinite".
 T4 Cross-supply is read ring-free as v_p(lam(Q^1)) rather than as
    v_p(N(Q) - 1), which is explore_support_growth.py's own reading
    exactly when R4 holds. S5 asserts the two agree on the tabulated
    rings before reading them apart anywhere else.

HAND-ATTACK ON PAPER, before any engine code.
  LEMMA B, RE-PROVED WITH NOTHING UNDER IT. Let r = door(Q, e, L) and let
  L divide L'. For every r' < r, lam(Q^(e+r')) divides L and hence
  divides L'. So no r' < r is outside the divisor set of L', and
  door(Q, e, L') >= r. The proof consults: transitivity of divisibility.
  It does not consult lam's shape, the column's chain property, the
  norm, the characteristic, or the universe. It survives R1-R4 deleted
  together, and it would survive lam taking values in any transitive
  order with a monotone join for the state. So Lemma B is not a fact
  about number rings, and the untouched-exponent hypothesis is not ring
  work either -- it is what keeps the two doors indexed at the same base,
  a statement about the ARGUMENT and not about the object.
  BUT THE SENTENCE THE CORPUS USES IS NOT THE LEMMA. "A place's cost
  never falls while its own exponent is untouched" quantifies over the
  walk's own invariants, and it needs L_t to divide L_(t+1) -- the
  accumulation the lemma takes as its HYPOTHESIS, supplied here by the
  dynamics rather than assumed. The invariant is the lcm of the seated
  lambdas and the move replaces lam(P^e) by lam(P^(e+r)) at one place, so
  the column being a CHAIN is what makes L_t divide L_(t+1) -- SUFFICIENT
  and not necessary, since the lcm of the other seated places can happen
  to carry a factor the moved column drops, which is a coincidence and not
  a law. That is R1, and it is arithmetic: nothing in an order forces a
  ladder to be nested.
  Delete R1 and the invariant can LOSE a prime, more lambdas fail to
  divide it, and a door FALLS -- a place priced back IN, which is the one
  thing the corpus's sentence says cannot happen. So the split to look
  for is finer than the question asked: the lemma is free, its standing
  hypothesis is bought, and R1 is what buys it.
  THE SUPPORT BOUND. A place is seated only by winning the menu, so the
  cost it pays is the walk's own move cost; a door is at least 1 by the
  definition; so cost = N(Q)^r >= N(Q). Consults: the price rule, and
  nothing else. Survives R1-R4 deleted.
  THE CERTIFICATE. C* is a sup over the vehicle's whole future, taken as
  a max over a simulated prefix, and the prefix is only a sup where the
  door sequence repeats. Under R2 it repeats. Delete R2 -- a column whose
  jump set thins, lam(P^a) = 2^f(a) with f jumping at 1, 2, 4, 8, ... --
  and the doors read 1, 2, 4, 8, ..., the cost diverges, and there is no
  sup to certify against. Consults R2. Separately m, the cheapest rival,
  is a min over the places of norm at most C*, and it can EXCEED C* only
  because that set is finite. Delete R3 -- a universe of cheap places
  deeper than the walk can exhaust -- and there is always a fresh
  cheapest rival at the floor price, so m never rises past C*. Consults
  R3.
  THE RACE. The floor prices a supply of k at a seated norm of at least
  p^k + 1, which is p^k | N(Q) - 1 read as a size. Under R4 the supply is
  v_p(N(Q) - 1) < N(Q) <= C, so log_p C caps it. Delete R4 -- lam(Q^1)
  free of the norm -- and a place of norm 2 can carry any supply at all
  while the budget stays at 2. Consults R4, and consults it as the single
  line lam(Q^1) < N(Q); the two exponential rates never enter.
  So the predicted split is: the lemma and the support bound are
  order-theoretic, the certificate is R2 + R3, the race is R4. DISTRUST
  THE MARGIN: the derived halves are the four one-line arguments above.
  The vibes half is that the CONSTRUCTIONS realize the deletions -- that
  a thinning jump set actually produces a walk whose vehicle is that
  column, and that a flat universe actually keeps the walk moving. Both
  are properties of what greedy DOES in a world, not of the world, and
  both are read as observables rather than asserted.

PREDICTIONS, fixed before the engine ran, each naming what the rig PRINTS.
  P1 THE TABULATED RING IS THE RING. For each of the five rings, a model
     whose six names are a TABLE reproduces the imported engine's walk
     step for step over the horizon -- cost, place, door and invariant
     identical at every step, from every one of the sweep's seeds -- and
     its certificate returns the same (vehicle, C*, period, m, verdict).
     A disagreement is an instrument fault and stops the run.
  P2 LEMMA B UNDER NO RING AT ALL. Over the random worlds -- norms
     arbitrary, ladders arbitrary, columns not chains, no characteristic
     structure -- zero door-monotonicity violations over nested pairs
     (L, L * m) built by hand at every place and every exponent the walks
     visit. Reading: the lemma holds where R1-R4 are all false.
  P2b AND THE SENTENCE IT IS USED AS DOES NOT. In those same worlds the
     walk's own invariant chain BREAKS -- at least one step with L_t not
     dividing L_(t+1) -- and at least one place's cost FALLS across a step
     that left its exponent untouched, which is the corpus's sentence
     failing. On the tabulated rings both counts are 0 at all twelve
     walks. Reading: R1 is what the standing hypothesis costs.
  P3 THE CERTIFICATE NEEDS A BOUNDED TICK GAP. In the thinning-jump-set
     world the vehicle's simulated door sequence has no period and its
     max cost over the prefix is strictly larger in the second half than
     in the first (a max still climbing, which is the observable for "no
     sup here"); certified_lock returns None. In the arithmetic-jump-set
     control, built identically but with the jump set an arithmetic
     progression, the period prints and the certificate passes.
  P4 THE CERTIFICATE NEEDS NORTHCOTT. In the flat universe the support at
     move 500 exceeds 400 places and is still gaining over the last
     hundred moves, and certified_lock returns None. In the control -- the
     same ladders over a universe whose norms are distinct and rise -- a
     certificate passes.
  P5 THE RACE NEEDS THE FIRST RUNG UNDER THE NORM. On the tabulated
     rings, v_p(lam(Q^1)) and v_p(N(Q) - 1) agree at every place and
     every rival characteristic, 0 off. In the decoupled world at least
     one walk seats a cross-supply strictly greater than floor(log_2 C),
     the ceiling the budget argument gives -- the race bound false with
     R4 deleted and nothing else changed.
  P6 THE SUPPORT BOUND HOLDS IN EVERY WORLD THIS FILE BUILDS, ring-shaped
     or not, at every walk: max seated norm <= max cost paid. This is
     derived with no hypothesis, so a violation is an engine bug and
     stops the run.

KILL-SHAPES, as observables.
  K1 the tabulated model disagrees with the imported engine: the table is
     not the ring and nothing downstream may be read.
  K2 a door-monotonicity violation prints in any synthetic world: the
     hand proof above is wrong and the descent is answered the other way
     -- Lemma B would be consuming something the table does not carry.
  K3 the certificate PASSES in the thinning world or in the flat one:
     R2 or R3 is not what it consumes, and the certificate's ring input
     is something else this file has not named.
  K4 the certificate FAILS in either control: the deletion is not
     isolated -- the construction broke something besides the property it
     meant to delete -- and neither reading counts.
  K5 no decoupled world beats the log_2 ceiling: the race bound survives
     R4's deletion and its ring input is not the first rung.
  K6 a support-bound violation anywhere: engine bug, stop.
  K7 no random world breaks the invariant chain, or breaks it with no
     cost ever falling: R1 is not reachable by drawing a table and the
     reading needs a construction, so P2b is unread rather than false.

POSITIVE CONTROL (S1, run before any verdict is read): the tabulated
five rings against the imported engine, walks and certificates. Nothing
downstream is read until it prints clean.

THE SECTIONS.
  S1  positive control: the tabulated rings against the imported engine.
  S2  Lemma B over random ring-free worlds.
  S3  R2 deleted: the thinning jump set against its arithmetic control.
  S4  R3 deleted: the flat universe against its rising control.
  S5  R4 deleted: cross-supply against the budget ceiling, with the
      tabulated agreement first.
  S6  the support bound over every world built above.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 THE DOOR MONOTONICITY LEMMA IS NOT A FACT ABOUT NUMBER RINGS
   (theorem, with a reading at 42400 door pairs over 24 worlds carrying no
   ring at all). If L divides L' then every r below door(Q, e, L) has
   lam(Q^(e+r)) dividing L and hence L', so no such r is outside the
   divisor set of L' and door cannot fall. The proof consults transitivity
   of divisibility and nothing else -- not the column's shape, not the
   norm, not the characteristic, not the universe -- so as a THEOREM it
   survives all four ring facts deleted together. What the rig READS is
   narrower and worth stating as such: the filed walker over worlds whose
   columns are independent draws, whose norms stand in no relation to
   their ladders and whose characteristic tags are decorative, which
   deletes R1 and R4 (both asserted false at every world) and leaves R3
   standing, a handful of places being finitely many. R2 and R3 are
   deleted separately
   and one at a time in S3 and S4, where the object under test is the
   certificate rather than the lemma. The untouched-exponent clause is not
   ring work either -- it holds the two doors at the same base, which is a
   statement about the argument.

F2 BUT THE SENTENCE THE CORPUS USES IS NOT THE LEMMA, AND WHAT IT BUYS IS
   THE COLUMN BEING A CHAIN (theorem for the mechanism, measurement for
   the rate: 1386 of 1416 steps break the invariant chain and 311 costs
   fall across 24 worlds, against 0 and 0 across the five rings). "A place's cost never falls
   while its own exponent is untouched" quantifies over the walk's own
   invariants, so it needs L_t to divide L_(t+1) -- which the lemma takes
   as a hypothesis and the DYNAMICS must supply. A move replaces
   lam(P^e) by lam(P^(e+r)) inside an lcm, so the column being a chain is
   SUFFICIENT for the invariant to grow and not necessary -- the other
   seated places can carry a dropped factor by accident. That is
   arithmetic: the unit group of O/P^(a+1) surjects onto O/P^a, and
   nothing in an order forces it. Delete it and the invariant LOSES primes
   at 1386 of the 1416 steps the sweep walks -- the other 30 being exactly
   that accident, which is why the denominator prints beside the count --
   more lambdas fail to divide it, and doors FALL at 311 (place, step)
   pairs: a place priced back IN, which is the one thing the corpus's
   sentence says cannot happen. So the
   credit splits: the lemma is free, its standing hypothesis is bought,
   and the tower's contribution to it is one line about unit groups.

F3 THE LOCK PERMANENCE CERTIFICATE IS THE STOP LAW IN ANOTHER COAT, AND
   IT CONSUMES TWO RING FACTS AT TWO DIFFERENT PLACES (rule, read at two
   constructed deletions each against its own control). C* is a supremum
   over the vehicle's whole future taken as a max over a simulated
   prefix, which is a supremum only where the door sequence repeats. Give
   every column a jump set whose gaps GROW -- 1, 2, 3, 4, ... -- and the
   doors read 46, 47, 48, ... with no period, the cost still climbing over
   the second half of the simulation, and no step of a 500-move walk
   certifies; the same world with the jump set arithmetic certifies at
   step 0 with period 1. That hypothesis is the STOP LAW's own: a bounded
   tick gap. The certificate and the stop law are one fact seen twice, and
   the certificate is where it does its work. The second fact enters
   elsewhere: m, the cheapest rival, exceeds C* only because the places
   under any norm bound are finitely many and a walk can exhaust them.
   Over 600 places at a single floor norm the walk seats a fresh one every
   move -- support 500 at move 500, still gaining 100 over the last
   hundred -- and no step certifies, while the SAME 600 places with the
   same ladder bases and the same jump sets, differing only in carrying
   norms that rise, certify at step 2 with C* = 4 against m = 9. The
   vehicle's own future is IDENTICAL in the two; what Northcott buys is
   not C* but whether a rival is ever forced to be dear. In both deletions
   "nothing certifies" is read over the WHOLE trace at a stride rather
   than at the last place the imported scan reaches -- the narrow scan is
   sound where a walk locks, and a wandering walk is exactly what a
   deletion produces, so a pass at a step the walk then LEAVES would be
   the worse finding of the two. There is none.

F4 THE RACE BOUND IS ONE LINE OF ARITHMETIC AND THE TWO EXPONENTIAL RATES
   NEVER ENTER IT (rule, the agreement read at 87 places and 12 walks over
   five rings, the break at one designed world). The bound reads a supply
   v_p(N(Q) - 1) and caps it by the log of the largest price paid; the
   only ring fact under it is lam(Q^1) = N(Q) - 1, the first rung sitting
   UNDER the norm the walk had to pay for. Read ring-free as
   v_p(lam(Q^1)) the two agree at every ring place and every walk, largest
   supply 3, every one inside its own ceiling. Decouple the first rung
   from the norm -- a place of norm 2 whose lam(Q^1) carries 3^7, seated
   beside a place tagged 3 -- and the supply reads 7 against a ceiling of
   1, at a walk 20 moves long. NOTHING ELSE IS CHANGED, and the section
   ASSERTS it rather than reasoning it off the world's definition: two
   places, and both columns strictly growing chains at every depth walked,
   hence a jump at every rung and constant gaps -- so R1, R2 and R3 all
   stand in it and R4 alone is false. So the
   budget argument's content is not that supply costs exponentially: it is
   that a first rung is cheaper than the place that carries it.

F5 THE SUPPORT BOUND IS FREE (theorem; 41 walks over 34 worlds, 0
   violations). A place is seated by winning the menu, so the cost it pays
   is the walk's own move cost, and a door is at least 1, so that cost is
   at least N(Q). Consults the argmin and the price rule. No world here --
   ring-shaped, chainless, gap-thinning, floor-flat or decoupled --
   violates it, and none could. The reading has one trap the rig walked
   into and the assert caught before any verdict: the bound is over the
   places a MOVE seats, and counting a PLANTED seed as seated raises a
   ceiling above anything the walk ever bought.

WHAT THIS LEAVES. The four riders the corpus hangs on door monotonicity
divide cleanly, and not the way the lemma's own billing suggests. Two of
them -- the lemma and the support bound -- are order-theoretic and would
hold over any accumulating invariant with a price rule, so the tower
CARRIES them. Two are arithmetic, and each names its fact exactly: the
certificate is a bounded tick gap plus Northcott, the race is
lam(Q^1) = N(Q) - 1. The standing hypothesis under all four is the column
being a chain. That is a better outcome than a uniform verdict either way,
and the sharpest piece of it is F3's coincidence: the permanence
certificate's hypothesis IS the stop law's, so two results the corpus
files apart are one hypothesis used twice.
WHAT IS NOT SETTLED: whether an accumulating structure with no ring under
it can be exhibited that a corpus would care about -- every ring-free
world here is BUILT, and a world that arises rather than being drawn is
the reading this file does not have. The deletions are also one at a time
by construction; nothing here reads what two of them do together, and the
chain break is the one deletion that fires in every random world at once.

RUN RECORD. `python explore_ring_free_door.py` (memwatch). One process,
CPython, no BLAS. 48644 checks, 9.0 s wall, peak working set 99.1 MB under
the 512 MB ceiling. S1: 12 walks of 500 moves, traces and certificates
identical to the imported engine's. S2: 42400 door readings over 24
worlds, 0 violations; 1386 chain breaks and 311 cost falls against 0 and 0
on the rings. S3: thinning doors 46, 47, 48, ... no period, no certificate
at any step; the arithmetic control certifies at step 0, period 1. S4:
flat support 500 at move 500 gaining 100 over the last hundred, no
certificate; the 600-place rising control certifies at step 2,
C* = 4 < m = 9. Neither deletion certifies at any step of its whole trace
either -- 50 thinning steps at a stride of 10, 20 flat steps at 25. S5:
87 places with lam(Q^1) = N - 1, 12 walks agreeing, largest supply 3; the
decoupled world reads supply 7 against ceiling 1, with R1, R2 and R3
asserted standing in it. S6: 41 walks, 0
violations. P1, P2, P2b, P3, P4, P5 and P6 all hit; no kill-shape fired,
and the one assert that did fire was the rig's own misreading of which
places the support bound quantifies over.

ONE FIX UPSTREAM, made when S1 would not run. explore_support_growth.py's
menu broke its tie by calling place_key on the (place, door) PAIR rather
than the place. On the filed rings that call lands on a quadratic engine's
key function, which reads the pair as an inert place of norm 1 and returns
a constant that loses every comparison -- so the tie went to the
key-smallest place, which is what a correct tie-break gives over a
key-sorted universe, and the filed numbers were right by accident. A model
whose key is a lookup raises instead. Fixed at the root; the primary
re-runs at 2661 checks with every number unchanged.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from math import gcd

import explore_support_growth as E

CHECKS = 0

HORIZON = E.HORIZON          # 500, the filed sweep's own
RAND_WORLDS = 24             # random ring-free worlds in S2
RAND_PLACES = 14             # places per random world
FLAT_PLACES = 600            # places of one norm in the R3 deletion
SEED0 = 20250609             # the walk is deterministic; only the world is drawn


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def lcm(a, b):
    return a // gcd(a, b) * b


# --------------------------------------------------------- the world
class World(object):
    """A model of the engine's six names built from a TABLE. A place is an
    opaque label carrying a norm, a char tag, a sort key and a LADDER
    callable a -> lam(place^a); the table is filled on demand and cached,
    so a column of any depth costs what its own rule costs and nothing
    else. There is no arithmetic underneath a world: it IS its table,
    which is what makes a ring's properties deletable one at a time."""

    def __init__(self, name, places):
        self.name = name
        self._n, self._c, self._k, self._f = {}, {}, {}, {}
        self._cache = {}
        for pl, norm, char, key, ladder in places:
            self._n[pl] = norm
            self._c[pl] = char
            self._k[pl] = key
            self._f[pl] = ladder
        self.UNIVERSE = sorted(self._n, key=lambda pl: self._k[pl])

    def place_norm(self, pl):
        return self._n[pl]

    def place_char(self, pl):
        return self._c[pl]

    def place_key(self, pl):
        return self._k[pl]

    def lam_P(self, pl, a):
        if a <= 0:
            return 1
        v = self._cache.get((pl, a))
        if v is None:
            v = self._f[pl](a)
            self._cache[(pl, a)] = v
        return v

    def lam_state(self, st):
        L = 1
        for pl, e in st.items():
            L = lcm(L, self.lam_P(pl, e))
        return L


class Rng(object):
    """A 32-bit LCG, so a world is reproducible without importing a
    library whose stream could change under us."""

    def __init__(self, seed):
        self.s = seed & 0xFFFFFFFF

    def next(self, n):
        self.s = (1664525 * self.s + 1013904223) & 0xFFFFFFFF
        return self.s % n

    def choice(self, xs):
        return xs[self.next(len(xs))]


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
          61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]


def tabulated_ring(name, M):
    """The ring as a TABLE: every one of the six names read off the
    engine, nothing recomputed. The control world."""
    places = [(pl, M.place_norm(pl), M.place_char(pl), M.place_key(pl),
               (lambda p: (lambda a: M.lam_P(p, a)))(pl))
              for pl in M.UNIVERSE]
    return World(name, places)


def jump_ladder(base, jumps):
    """lam(a) = base^f(a) with f(a) the number of jumps at or below a --
    the ladder as its own jump set, which is the only structure a door
    reads off a column. `jumps` is a callable i -> the i-th jump."""
    def f(a):
        i, k = 0, 0
        while jumps(i) <= a:
            k += 1
            i += 1
        return base ** k
    return f


def thinning(offset):
    """Jumps at 1 + i(i + 1)/2, shifted: gaps 1, 2, 3, 4, ... -- bounded
    nowhere, so a door taken from any exponent grows without bound."""
    return lambda i: 1 + offset + i * (i + 1) // 2


def arithmetic(step, offset=0):
    """Jumps in an arithmetic progression: the ring's own eventual shape
    (Lemma A, k eventually arithmetic of step e_P)."""
    return lambda i: 1 + offset + i * step


def rand_ladder(rng_seed):
    """A ladder with no shape at all: each rung an independent draw, so
    the column is not a chain, carries no characteristic, and stands in no
    relation to the norm."""
    def f(a):
        r = Rng(rng_seed * 7919 + a * 104729)
        v = 1
        for _ in range(3):
            v *= r.choice(PRIMES[:9]) ** (1 + r.next(2))
        return v
    return f


def free_cross_supply(W, moved, st):
    """explore_support_growth.py's cross_supply with N(Q) - 1 replaced by
    lam(Q^1), which is the same reading exactly where R4 holds (S5 asserts
    the agreement on the rings before reading the two apart anywhere)."""
    chars = set(W.place_char(x) for x, e in st.items() if e)
    out = 0
    for q in moved:
        for p in chars:
            if p == W.place_char(q):
                continue
            out = max(out, E.v_p(W.lam_P(q, 1), p))
    return out


def support_of(st):
    return set(pl for pl, e in st.items() if e)


# The support bound is read at every world this file builds; S6 spends
# the list.
SUPPORT_LOG = []


def run_walk(W, seed, moves):
    """Walk, then bank the support-bound reading for S6. The bound is over
    the places a MOVE seats -- a planted seed is not bought, and reading
    it as seated is what raises a ceiling above anything the walk paid
    (explore_support_growth.py F1's own slack cases)."""
    tr = E.walk(W, seed, moves)
    mx_norm = max([W.place_norm(pl) for pl in E.moved_places(tr)] or [0])
    mx_cost = max(t[0] for t in tr)
    SUPPORT_LOG.append((W.name, mx_norm, mx_cost))
    return tr


# ------------------------------------------------ S1 the positive control
def s1_control():
    section("S1  POSITIVE CONTROL -- the five rings as TABLES against the "
            "imported engine, walks and certificates, before any verdict "
            "is read")
    print("  A world is its table. If the table is the ring's own six")
    print("  names, the engine must not be able to tell the difference:")
    print("  same trace step for step, same certificate.")
    print()
    print("  %-14s %-7s %-9s %-24s" % ("ring", "walks", "steps", "verdict"))
    worlds = []
    nwalk = 0
    for name, M, rams in E.load_rings():
        W = tabulated_ring(name, M)
        ok(list(W.UNIVERSE) == list(M.UNIVERSE),
           "%s: the tabulated universe is not the ring's" % name)
        steps = 0
        for sname, seed in E.seeds_of(rams):
            a = E.walk(M, seed, HORIZON)
            b = run_walk(W, seed, HORIZON)
            for i, (x, y) in enumerate(zip(a, b)):
                ok(x[0] == y[0] and x[1] == y[1] and x[2] == y[2]
                   and x[4] == y[4],
                   "%s/%s: the table parts from the ring at step %d"
                   % (name, sname, i))
                steps += 1
            ia, ca = E.certified_lock(M, a)
            ib, cb = E.certified_lock(W, b)
            ok(ia == ib and ca == cb,
               "%s/%s: the certificate differs on the table" % (name, sname))
            nwalk += 1
        worlds.append((name, M, W, rams))
        print("  %-14s %-7d %-9d %-24s"
              % (name, len(E.seeds_of(rams)), steps, "identical"))
    print()
    print("  %d walks, %d moves each, traces and certificates identical."
          % (nwalk, HORIZON))
    print("  The engine reads a world through six names and no more, so")
    print("  every deletion below is a deletion of the RING and not of the")
    print("  instrument.")
    return worlds


def sieve(n):
    m = [True] * (n + 1)
    m[0] = m[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if m[i]:
            for j in range(i * i, n + 1, i):
                m[j] = False
    return [i for i in range(n + 1) if m[i]]


BIG_PRIMES = sieve(12000)


# ------------------------------------------ S2 the lemma with no ring
def random_world(idx):
    """Norms arbitrary, char tags arbitrary, and a ladder whose rungs are
    independent draws -- R1 to R4 all false at once."""
    r = Rng(SEED0 + idx * 1013)
    norms = sorted(set(r.choice(PRIMES[:20]) for _ in range(RAND_PLACES)))
    places = []
    for i, n in enumerate(norms):
        places.append((("q", i), n, r.choice(PRIMES[:8]), (n, i),
                       rand_ladder(SEED0 + idx * 977 + i)))
    return World("random %d" % idx, places)


def _chain_and_falls(W, tr):
    """Two counters over a trace: steps whose invariant is not a multiple
    of the last, and (place, step) pairs whose cost FELL across a step
    that left the place's own exponent untouched."""
    chain, falls = 0, 0
    prev_L, prev_st = tr[0][4], tr[0][3]
    for t in range(1, len(tr)):
        L, st = tr[t][4], tr[t][3]
        if L % prev_L != 0:
            chain += 1
        for pl in W.UNIVERSE:
            e = prev_st.get(pl, 0)
            if st.get(pl, 0) != e:
                continue
            if E.cost_of(W, pl, e, L) < E.cost_of(W, pl, e, prev_L):
                falls += 1
        prev_L, prev_st = L, st
    return chain, falls


def s2_lemma_b(ring_worlds):
    section("S2  LEMMA B WITH NO RING UNDER IT -- door monotonicity over "
            "worlds where the column is not a chain, the norm says nothing "
            "about the ladder, and there is no characteristic at all")
    print("  The lemma, re-proved on paper with nothing under it: if L")
    print("  divides L' then every r below door(L) divides L', so door")
    print("  cannot fall. The rig reads it over nested pairs (L, L * m).")
    print()
    print("  %-12s %-8s %-9s %-10s %-11s" % ("world", "readings", "lemma B",
                                             "chain brk", "costs fell"))
    reads = tot_chain = tot_falls = 0
    for idx in range(RAND_WORLDS):
        W = random_world(idx)
        ok(any(W.lam_P(pl, 1) != W.place_norm(pl) - 1 for pl in W.UNIVERSE),
           "%s: every first rung is N - 1, so R4 is not deleted here and "
           "the world is not as ring-free as the reading says" % W.name)
        tr = run_walk(W, {}, 60)
        n = 0
        for t in range(0, len(tr), 6):
            L = tr[t][4]
            for pl in W.UNIVERSE:
                for e in (0, 1, 2, 3):
                    d = E.door(W, pl, e, L)
                    for m in (2, 3, 5, 7):
                        d2 = E.door(W, pl, e, L * m)
                        ok(d2 >= d,
                           "%s: door fell from %s to %s at %s under a "
                           "MULTIPLE of the invariant" % (W.name, d, d2, pl))
                        n += 1
        chain, falls = _chain_and_falls(W, tr)
        reads += n
        tot_chain += chain
        tot_falls += falls
        if idx < 4:
            print("  %-12s %-8d %-9s %-10d %-11d"
                  % (W.name, n, "clean", chain, falls))
    print("  %-12s %-8d %-9s %-10d %-11d"
          % ("all %d" % RAND_WORLDS, reads, "clean", tot_chain, tot_falls))
    steps = RAND_WORLDS * 59
    print("  The chain breaks at %d of the %d steps walked and not at all "
          "of them:" % (tot_chain, steps))
    print("  the column being a chain is SUFFICIENT for the invariant to")
    print("  grow, never necessary -- the lcm of the other seated places")
    print("  can carry a dropped factor by accident, and at %d steps it did."
          % (steps - tot_chain))
    print()
    print("  And the same two counters over the tabulated rings, where the")
    print("  column IS a chain:")
    rchain = rfalls = 0
    for name, M, W, rams in ring_worlds:
        for sname, seed in E.seeds_of(rams):
            c, f = _chain_and_falls(W, E.walk(W, seed, 60))
            rchain += c
            rfalls += f
    print("  %-12s %-8s %-9s %-10d %-11d"
          % ("5 rings", "-", "clean", rchain, rfalls))
    ok(rchain == 0 and rfalls == 0,
       "the tabulated rings break the invariant chain, which is R1 false "
       "in a number ring")
    return reads, tot_chain, tot_falls, rchain, rfalls


# ------------------------------- S3 the certificate without a bounded gap
def gap_world(name, jumps_of):
    places = []
    for i in range(6):
        places.append((("g", i), PRIMES[i], PRIMES[i], (PRIMES[i], i),
                       jump_ladder(PRIMES[10 + i], jumps_of(i))))
    return World(name, places)


def no_step_certifies(W, tr, stride):
    """The imported certified_lock scans only the steps that move at the
    trace's own LAST place, which is sound where a walk locks and narrow
    where it wanders -- and a wandering walk is exactly what the deletions
    produce. So "nothing certifies" is read over the whole trace at a
    stride, and a PASS at a step the walk later leaves would be worse than
    a narrow scan: it would be the certificate proving a permanence that
    did not happen. Returns the first such step, or None."""
    for i in range(0, len(tr), stride):
        vpl = tr[i][1]
        if E.certificate(W, tr, i)[4]:
            return i, vpl
    return None


def vehicle_future(W, tr, i, moves):
    """The vehicle-only future's doors and costs at step i -- the same
    simulation the certificate runs, read out rather than reduced."""
    vpl = tr[i][1]
    st, L = dict(tr[i][3]), tr[i][4]
    doors, costs = [], []
    for _ in range(moves):
        r = E.door(W, vpl, st.get(vpl, 0), L)
        doors.append(r)
        costs.append(W.place_norm(vpl) ** r)
        st[vpl] = st.get(vpl, 0) + r
        L = W.lam_state(st)
    return vpl, doors, costs


def s3_tick_gap():
    section("S3  R2 DELETED -- a column whose jump set THINS, against the "
            "same world with the jump set arithmetic: what the certificate "
            "buys from a bounded tick gap")
    print("  C* is a sup over the vehicle's whole future, taken as a max")
    print("  over a simulated prefix. The prefix is a sup only where the")
    print("  door sequence repeats, and in a number ring it repeats")
    print("  because the column's jump set is eventually arithmetic.")
    print()
    out = {}
    for label, jumps_of in (("arithmetic", lambda i: arithmetic(1, i)),
                            ("thinning", lambda i: thinning(i))):
        W = gap_world(label, jumps_of)
        tr = run_walk(W, {}, HORIZON)
        i, cert = E.certified_lock(W, tr)
        vpl, doors, costs = vehicle_future(W, tr, len(tr) - 1, 40)
        half = len(costs) // 2
        climbing = max(costs[half:]) > max(costs[:half])
        out[label] = (i, cert, doors[:6], climbing,
                      len(support_of(tr[-1][3])))
        if label == "thinning":
            W_thin, tr_thin = W, tr
        print("  %-11s vehicle %-8s doors %-22s" % (label, str(vpl),
                                                    str(doors[:6])))
        print("  %-11s period %-8s max cost still climbing: %s"
              % ("", str(None if cert is None else cert[2]), climbing))
        print("  %-11s certificate: %s"
              % ("", "PASS at step %d" % i if cert else "none, at any step"))
        print()
    ok(out["arithmetic"][1] is not None,
       "the arithmetic control does not certify, so the deletion is not "
       "isolated and neither reading counts (K4)")
    ok(out["thinning"][1] is None,
       "the thinning world certifies, so a bounded tick gap is not what "
       "the certificate consumes (K3)")
    hit = no_step_certifies(W_thin, tr_thin, 10)
    ok(hit is None,
       "a step of the thinning walk certifies at %s -- and the walk leaves "
       "it, so the certificate proved a permanence that did not happen"
       % (hit,))
    print("  And nothing certifies at ANY step of the thinning walk, not")
    print("  only at the last place the imported scan looks at: 50 steps")
    print("  read at a stride of 10, 0 passes.")
    ok(out["thinning"][3],
       "the thinning vehicle's cost is not still climbing, so the "
       "construction did not delete R2")
    print("  Reading: the certificate consumes R2 -- and R2 is the stop")
    print("  law's own hypothesis, a bounded tick gap, arriving here as")
    print("  the thing that makes a max over a prefix a supremum.")
    return out


# ------------------------------ S4 the certificate without Northcott
def flat_world(name, norms):
    """The two worlds of S4 differ in ONE variable and it is the one being
    deleted: same place count, same ladder bases, same jump sets, and only
    the norm profile -- flat at the floor, or rising -- apart."""
    places = []
    for i in range(FLAT_PLACES):
        b = BIG_PRIMES[700 + i]
        places.append((("f", i), norms(i), b, (norms(i), i),
                       jump_ladder(b, arithmetic(2))))
    return World(name, places)


def s4_northcott():
    section("S4  R3 DELETED -- a universe with no shortage of places at "
            "the floor price, against the same ladders over norms that "
            "rise: what the certificate buys from Northcott")
    print("  m, the cheapest rival, can EXCEED C* only because the places")
    print("  of norm at most C* are finitely many and the walk can exhaust")
    print("  them. Give it a floor it cannot exhaust and m never rises.")
    print()
    res = {}
    for label, norms in (("rising", lambda i: BIG_PRIMES[i]),
                         ("flat", lambda i: 2)):
        W = flat_world(label, norms)
        tr = run_walk(W, {}, HORIZON)
        i, cert = E.certified_lock(W, tr)
        sup = len(support_of(tr[-1][3]))
        sup400 = len(support_of(tr[399][3]))
        res[label] = (i, cert, sup, sup - sup400)
        if label == "flat":
            W_flat, tr_flat = W, tr
        print("  %-8s places %-5d support at move %d: %-4d  gained over the "
              "last 100: %d" % (label, FLAT_PLACES, HORIZON, sup,
                                sup - sup400))
        print("  %-8s certificate: %s"
              % ("", "PASS at step %d, C* = %s, m = %s"
                 % (i, cert[1], cert[3]) if cert else "none, at any step"))
        print()
    ok(res["rising"][1] is not None,
       "the rising control does not certify, so the deletion is not "
       "isolated (K4)")
    ok(res["flat"][1] is None,
       "the flat universe certifies, so Northcott is not what the "
       "certificate consumes (K3)")
    ok(res["flat"][3] > 0,
       "the flat support has stopped growing, so the construction did not "
       "delete R3 over this horizon")
    hit = no_step_certifies(W_flat, tr_flat, 25)
    ok(hit is None,
       "a step of the flat walk certifies at %s, which the walk then "
       "leaves" % (hit,))
    print("  And again at no step of the flat walk rather than at no step")
    print("  the imported scan reaches: 20 steps read at a stride of 25.")
    print("  Reading: the certificate consumes R3, and it consumes it at")
    print("  m rather than at C* -- the vehicle's own future is unchanged")
    print("  between the two worlds; what changes is whether a rival is")
    print("  ever forced to be dear.")
    return res


# --------------------------------- S5 the race without the first rung
def s5_race(ring_worlds):
    section("S5  R4 DELETED -- cross-supply against the budget ceiling, "
            "with the tabulated agreement read first")
    print("  The race bound reads a supply v_p(N(Q) - 1) and caps it by")
    print("  log of the largest price paid. The single ring fact under")
    print("  that is lam(Q^1) = N(Q) - 1: the first rung sits UNDER the")
    print("  norm the walk had to pay for.")
    print()
    n = 0
    for name, M, W, rams in ring_worlds:
        for pl in M.UNIVERSE:
            if M.place_norm(pl) > 60:
                break
            ok(M.lam_P(pl, 1) == M.place_norm(pl) - 1,
               "%s: lam(%s^1) is not N - 1" % (name, pl))
            n += 1
    print("  lam(Q^1) = N(Q) - 1 at %d places over five rings, 0 off." % n)
    worst = 0
    for name, M, W, rams in ring_worlds:
        for sname, seed in E.seeds_of(rams):
            tr = E.walk(W, seed, 60)
            st, moved = tr[-1][3], E.moved_places(tr)
            a = E.cross_supply(M, moved, st)
            b = free_cross_supply(W, moved, st)
            ok(a == b, "%s/%s: the two readings of cross-supply differ "
                       "(%d vs %d)" % (name, sname, a, b))
            C = max(t[0] for t in tr)
            ceiling = C.bit_length() - 1
            ok(b <= ceiling,
               "%s/%s: supply %d over the ceiling %d" % (name, sname, b,
                                                         ceiling))
            worst = max(worst, b)
    print("  The two readings agree at all 12 ring walks, largest supply "
          "%d," % worst)
    print("  every one under its own floor(log_2 C).")
    print()
    W = World("decoupled", [
        (("d", 0), 2, 2, (2, 0), lambda a: 3 ** 7 * 17 ** a),
        (("d", 1), 3, 3, (3, 1), lambda a: 19 ** a),
    ])
    ok(len(W.UNIVERSE) == 2, "the decoupled world is not two places, so "
                             "R3 is not obviously standing in it")
    for pl in W.UNIVERSE:
        for a in range(1, 21):
            lo, hi = W.lam_P(pl, a), W.lam_P(pl, a + 1)
            ok(hi % lo == 0 and hi != lo,
               "%s: the decoupled column is not a strictly growing chain "
               "at depth %d, so R1 or R2 is deleted here too and R4 is not "
               "alone" % (str(pl), a))
    print("  R1, R2 and R3 asserted standing in it: two places, and both")
    print("  columns strictly growing chains over every depth walked --")
    print("  a jump at every rung, so the gaps are constant.")
    tr = run_walk(W, {("d", 1): 1}, 20)
    st, moved = tr[-1][3], E.moved_places(tr)
    C = max(t[0] for t in tr)
    ceiling = C.bit_length() - 1
    sup = free_cross_supply(W, moved, st)
    print("  Decoupled: a place of norm 2 whose first rung carries 3^7,")
    print("  seated beside a place whose char tag is 3.")
    print("  largest price paid %d, ceiling floor(log_2 C) = %d, supply %d"
          % (C, ceiling, sup))
    ok(sup > ceiling,
       "the decoupled world does not beat the ceiling, so the race bound "
       "survives R4's deletion (K5)")
    print("  Reading: the race bound is R4 and nothing else. The two")
    print("  exponential rates never enter it -- delete the one line that")
    print("  puts the first rung under the norm and the budget argument")
    print("  has no purchase, at a walk 20 moves long.")
    return worst, C, ceiling, sup


# ------------------------------------------- S6 the support bound
def s6_support():
    section("S6  THE SUPPORT BOUND OVER EVERY WORLD BUILT ABOVE -- ring-"
            "shaped or not, and under every deletion this file makes")
    worst = None
    for name, mx_norm, mx_cost in SUPPORT_LOG:
        ok(mx_norm <= mx_cost,
           "%s: a seated norm %d exceeds the largest cost paid %d -- the "
           "support bound is false, which is an engine bug (K6)"
           % (name, mx_norm, mx_cost))
        if worst is None or mx_cost - mx_norm < worst[1]:
            worst = (name, mx_cost - mx_norm)
    print("  %d walks over %d worlds, 0 violations. Tightest slack: %s at %d."
          % (len(SUPPORT_LOG), len(set(x[0] for x in SUPPORT_LOG)),
             worst[0], worst[1]))
    print("  The bound is a fact about the argmin and the price rule. No")
    print("  world this file could build was going to break it.")
    return len(SUPPORT_LOG)


def main():
    ring_worlds = s1_control()
    s2_lemma_b(ring_worlds)
    s3_tick_gap()
    s4_northcott()
    s5_race(ring_worlds)
    s6_support()
    print("\n" + "=" * 72)
    print("%d checks, all green." % CHECKS)
    print("=" * 72)


if __name__ == "__main__":
    main()
