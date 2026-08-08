"""explore_increment_group.py -- the clock's increment recursion lifted OFF
the ring: what decides, over an arbitrary finite abelian group and an
arbitrary pattern of returned units, whether a coordinate deepens past the
window and then stops.

THE QUESTION. explore_rider_recursion.py settled that the element limit's
rider-fed coordinates are unbounded exactly when their cell sits in the
increment recursion's CYCLE, and found a third kind of coordinate at one ring
only: one whose class lands in the recursion's PRE-PERIOD and never in the
cycle, so it deepens past the transient window and then stops forever. Why
only there is the open end. The suspicion on record is arithmetic on the class
number -- one ring's h is prime, the other's is 15 and has proper subgroups,
so gamma can sit in one. That is a suspicion about a GROUP, and it can be
answered without walking anything, because the recursion needs no ring.

WHAT IS ACTUALLY IN THE RECURSION. Write C for the clock's cell, gamma for its
class, T for the tick, r for the increment. A clock move summons the minimal
representative of -r*gamma and w of its units land back on C, so

    T' = 2T,    r' = T - w,    w = W(-r*gamma),

with W(c) the multiplicity of C in the representative of c -- one non-negative
integer per class, and NOTHING else about the ring enters. So the object is a
finite abelian group G, an element gamma, and a function W: G -> Z>=0. The
sweep is over all three.

THREE REDUCTIONS, on paper before any engine code, and each one is a
prediction below rather than a convenience.

 1. THE ORDER, NOT THE CLASS NUMBER. -r*gamma depends on r only through
    r mod d with d = ord(gamma), and w through it; r' = T - w then needs T
    only mod d. So the state is (T mod d, r mod d) and lives in (Z/d)^2. The
    rig carries it mod h. Every d | h, so mod h is a refinement that cannot
    disagree -- but it can only be the CLASS NUMBER's business if d = h, and
    the suspicion on record is stated about h. This is where it starts to come
    apart: the recursion cannot read h at all.
 2. THE CLASS IS THE RESIDUE. r mod d -> -r*gamma is a bijection from Z/d onto
    <gamma>, since gamma has order exactly d. So "which classes the pre-period
    summons" IS "which residues r takes on the tail", and the whole question is
    a statement about the r-projection of one orbit of one map on (Z/d)^2.
 3. THE TRIVIAL CLASS SUMMONS NOTHING. r = 0 mod d summons the identity, whose
    representative is empty: no rider, no cell, no coordinate. So a tail
    residue of 0 is NOT an escape, and a sweep that counted it would report a
    species that does not exist. ESCAPE means a NON-ZERO tail residue that
    never recurs on the cycle.

THE HAND-ATTACK, at d = 5 -- prime, and the exact order the ring with no such
coordinate carries -- with u(1) = 1 and u zero elsewhere, seeded at (T, r) =
(1, 1). The tick runs 1, 2, 4, 3, 1, ... and

    r: 1, 0, 2, 4, 3, 1, 1, 3, 3, ...

so the state (1, 3) stands at j = 4 and again at j = 8: pre-period 4, cycle 4,
the cycle's residues {1, 3} and the tail's {0, 1, 2, 4}. Residues 2 and 4 are
non-zero and never recur -- an ESCAPE at a PRIME d, which is what the suspicion
says cannot be the story. The same specimen carries a pre-period of 4 where the
six rings never exceed 1. Both are asserted against the engine at S1(b), so
the two headline predictions have a hand-derived witness before the sweep runs
rather than a table to be read afterwards.

WHOSE VOCABULARY. The question arrives in the ELEMENT world's terms -- cells,
classes, riders, the clock -- and the object it is about has none of them: a
group, an element, a pattern of counts. The translation is reductions 1-3 and
it is done ONCE, above; everything after is written in the group's own words,
and the ring vocabulary returns only at S4, where the six rings are read back
in. The one term that could not be reduced away is the CLOCK'S OWN CELL, which
survives as the choice of W -- w is by definition what comes back to C -- and
that is why W is swept as an arbitrary function rather than derived.

TRANSPLANT FLAGS, fixed at the freeze.
 1. From explore_rider_recursion.py: the recursion itself, its seed reading
    (the first clock move past the transient window), and the walk that
    controls it. The walk is used here ONLY to read six realized patterns off
    six rings; no verdict below is read from it.
 2. The sweep quantifies over ALL W, and a law true of all of them can be
    empty. Which patterns a RING can realize is unknown a priori, so every
    census below is printed twice -- once over all patterns, once over the
    patterns satisfying the constraints the six realized ones actually meet --
    and the second is the one a claim about rings may cite. Calling the first
    the answer would be the transplant.

THE SLATE, fixed before any engine code.

 PS1 THE STATE IS THE ORDER'S, NOT THE CLASS NUMBER'S. At every branch of
     every ring, iterating (T mod d, r mod d) with d = ord(gamma) gives the
     same pre-period, cycle length, cycle classes and pre-period classes as
     the rig's (T mod h, r mod h). KILL: any branch where the two differ --
     which would mean the reduction drops a distinction the ring makes, and
     the abstraction is not of this object.
 PS2 THE CYCLE LENGTH IS A MULTIPLE, AND THE RIG'S DIVISOR IS RANGE. The
     tick's own orbit is 2^j T0, so its period -- the multiplicative order of
     2 modulo the odd part of d, or 1 where the tick vanishes there -- must
     DIVIDE the state cycle. Predicted: it divides every cycle in the sweep,
     and the sweep exhibits cycles that are proper multiples of it, so the
     recorded "cycle length divides the order of 2" is a fact about six rings
     and not a law. KILL: a cycle the tick's period does not divide, which
     would break the state map itself; or no proper multiple anywhere, which
     would promote the divisor to a candidate theorem and owe it a proof.
 PS3 THE PRE-PERIOD BOUND IS RANGE. Predicted: the sweep exhibits pre-periods
     over the 2-adic valuation of d plus one -- the bound the six rings never
     exceed -- so that bound too is a range fact. KILL: no orbit anywhere in
     the full enumeration over that bound.
 PS4 A BIJECTION CANNOT ESCAPE (proved, and asserted over the sweep). If d is
     odd and u is injective mod d then (T, r) -> (2T, T - u(r)) is a bijection
     of a finite set, so every orbit is purely periodic, the pre-period is
     empty and there is nothing to escape. Predicted: no escaping orbit in the
     sweep has both. KILL: one that does -- which would mean the engine's
     pre-period is not the map's.
 PS5 THE SUSPECT DIES: PRIMALITY DECIDES NOTHING. Predicted: escapes occur at
     prime d, at d = 5 specifically, for a positive fraction of patterns; and
     the escape rate at prime d is not zero and not obviously below the
     composite rate. So the species is decided by the PATTERN and the SEED,
     never by whether the class number factors. KILL: zero escaping orbits at
     every prime d in the full enumeration, which would promote the suspicion
     to a rule in range and leave a proof to be hunted rather than a kill.
 PS6 THE LAW'S REALIZABLE PART. The six rings' own patterns are read off and
     printed. Predicted: they satisfy u(0) = 0 -- the identity class returns
     nothing -- and their values are bounded by the ring's own largest
     multiplicity; and escapes at d = 5 survive both constraints, so PS5's
     verdict is about patterns a ring could carry and not only about the
     quantifier. KILL: every escaping pattern at d = 5 fails a constraint all
     six realized patterns meet, which leaves the suspicion alive exactly
     where it was asked and makes the sweep's generality its cost.

THE DESIGN: a control in three parts, then three sections.

 S1 THE POSITIVE CONTROL, run before any verdict is read.
    (a) THE REDUCTION AGAINST THE RIG (PS1): every branch of every ring, the
        mod-d state against the mod-h state, on all four outputs.
    (b) THE HAND-ATTACK (PS2, PS3, PS5): the d = 5 specimen above, its orbit
        asserted state by state against the derivation, and its escape and
        pre-period asserted -- so the two headline claims have a witness the
        engine did not choose.
    (c) THE DETECTOR BOTH WAYS: a pattern constructed to escape and one
        constructed not to, asserted to be called correctly, since a detector
        that never fires and one that always fires both read as a census.
 S2 THE SWEEP (PS2, PS3, PS4): every d from 2 to the full-enumeration bound,
    every u: Z/d -> Z/d, every seed whose tick is a power of 2 -- the ticks a
    clock can actually stand at -- and above that bound a sampled census at a
    fixed seed. Pre-period, cycle, and the two bounds tested.
 S3 THE VERDICT (PS5): the escape census by d, prime against composite, over
    all patterns and over the realizable ones.
 S4 THE RINGS READ BACK IN (PS1, PS6): the six realized (d, u, seed) triples,
    where each sits in the census, and the cell-level species against the
    class-level one -- the ring whose coordinate stops, and the ring whose
    pre-period stays inside its own cycle.

THE FINDINGS.

FS1 PS1'S KILL FIRED, AND WHAT IT KILLED WAS THE SLATE'S OWN CONFLATION (rule
    in range -- six rings, all 150 branches). The state carried mod h and the
    state carried mod d do NOT agree on their lengths: at the ring with
    gamma = 0 the fine state still carries the TICK, whose period there is 2,
    while the classes summoned are the identity forever and the coarse period
    is 1. So a pre-period or a cycle LENGTH is a property of the modulus a rig
    chose to carry, not of the recursion. What IS invariant is what every
    verdict is read off -- the cells the cycle summons and the cells the
    pre-period summons -- and those agree at every branch, with the coarse
    cycle dividing the fine one and the two pre-periods equal throughout. The
    equality is asserted rather than reported, because a fine pre-period
    strictly longer than the coarse one would file a cell as BOUNDED that the
    cycle feeds forever; it never happened, so the recorded verdicts stand
    exactly as they were.

FS2 THE RECURSION CANNOT READ THE CLASS NUMBER, AND AT THE RING IN QUESTION
    GAMMA GENERATES (rule in range, six rings). The order of gamma is what the
    recursion sees, and it is 1, 2, 1, 2, 5 and 15 against class numbers 1, 2,
    3, 4, 5 and 15 -- strictly smaller at two of the rings. At the ring the
    suspicion was ABOUT, ord(gamma) = 15 = h: gamma generates the whole class
    group, so the proper subgroup the suspicion appealed to is not where gamma
    sits. The contrast between the two rings that carry riders is 5 against
    15 as ORDERS of a cyclic group, both generated, and no subgroup is in it.

FS3 THE TICK'S PERIOD DIVIDES EVERY CYCLE, AND THAT IS THE ONLY BOUND THAT IS
    A LAW (proved, and asserted over all 4,907,558 orbits swept). The state
    map carries the tick with it, so the tick's own period must divide the
    state's -- 0 exceptions. Both bounds the six rings never exceed fail off
    them, and neither refutation rests on the SAMPLED part: inside the full
    enumeration d = 5 alone -- the prime order one of the rings actually
    carries -- reaches a cycle of 20 against a tick period of 4 and a
    pre-period of 12 against a 2-adic bound of 1. Over the whole sweep the
    extremes are 9x the tick's period (54 against 6 at d = 9) and a
    pre-period of 83 (d = 13). So
    the recorded "cycle divides the order of 2" is the wrong direction of a
    true statement, and the shortness of the six rings' pre-periods is a fact
    about six rings.

FS4 A BIJECTION CANNOT ESCAPE, AND IT IS THE ONLY STRUCTURAL BAR IN THE SWEEP
    (proved; asserted over every escaping orbit). Odd d with u injective mod d
    makes (T, r) -> (2T, T - u(r)) a bijection of a finite set, so every orbit
    is purely periodic and there is no tail to escape from. Nothing else bars
    escape: every d from 3 to 16, prime and composite alike, escapes.

FS5 THE SUSPECT IS DEAD -- THE ORDER'S FACTORIZATION DECIDES NOTHING (rule in
    range, full enumeration at d = 2 to 6, sampled to 16). Escape needs
    neither a composite order nor a proper subgroup: at d = 5 -- prime, and
    the exact order carried by the ring with NO such coordinate -- 28,972 of
    62,500 orbits escape, 46.4%. The rates run 17.3% to 68.5% at prime d and
    59.3% to 91.8% at composite, and the aggregate gap (46.3% against 59.3%)
    is d = 6 dominating the composite side with 99.6% of its orbits: the rate
    tracks d upward, never its factorization. The suspicion needed a zero at
    prime d and gets a plurality.

FS6 WHAT DECIDES IT IS THE SEED AGAINST THE PATTERN, AND THE SEED IS THE ONE
    THING NO ALGEBRA HANDS OVER (rule in range). Escape is exactly: the orbit
    has a pre-period, and some NON-ZERO residue on the tail never recurs on
    the cycle -- non-zero because residue 0 summons the identity class, whose
    representative is empty and which therefore has no coordinate to bound. A
    sweep counting it would report a species that does not exist. Given
    (d, u, seed) the verdict is O(d^2) with no ring, no walk and no limit in
    it -- but THE SEED IS NOT ALGEBRA. d and u are the ring's own constants,
    readable off gamma and the representatives; the seed is the state at the
    first clock move past the transient, and the transient is exactly what a
    walk is for. So the aim this rig was pointed at -- predicting which rings
    carry a bounded coordinate BEFORE walking one -- is not met and cannot be,
    and the reason is the finding rather than a shortfall against it: the
    species is not a property of the ring's algebra at all, which is why no
    fact about the class group was ever going to decide it. What the walk owes
    is one state; everything after is arithmetic. The shape:
    74.8% of orbits have a pre-period at all and 78.1% of those escape, so
    among orbits that CAN escape most do, and the ring with no bounded
    coordinate is the exception rather than the rule.

FS7 THE VERDICT SURVIVES THE REALIZABLE RESTRICTION (rule in range). The six
    realized patterns all return nothing for the identity class and never more
    than 2 units for any class, and both constraints bite hard -- together
    they cut the full enumeration to 0.7% of itself. Escape over what
    survives is 64.9%, and at d = 5 it is 48.3% over 1,620 orbits. The
    hand-attack's own pattern meets both. So the generality is not the
    finding's cost: the escapes at the order the non-escaping ring carries are
    patterns a ring could hold, not artifacts of quantifying over patterns
    none could.

FS8 THE TWO RINGS DIFFER BY WHERE THE TRANSIENT LEAVES THE INCREMENT
    (observation, two rings, complete branch sets). Both seed at a tick of 1
    or a power of it; what differs is the residue. The h = 5 ring seeds at
    r = 1 or 2, residues its own cycle also carries, so 8 of its 20 branches
    take a pre-period and NONE of them escapes -- nothing outside the cycle
    to stop. The genus-2 ring seeds at r = 5, 6 or 7 on 89 of its 120
    branches, residues its cycle never returns to, which is what a stopping
    coordinate needs -- and 77 of those 89 walks print one, the other 12
    being FS9's over-report and not a second mechanism. So "why only there"
    is answered: not the class number, not the group, not a subgroup -- the
    seed.

FS9 THE CLASS LEVEL OVER-REPORTS, AND THE BRIDGE IS A SET IDENTITY (rule in
    range, all 150 branches). A class the cycle never summons again is not the
    same thing as a cell the cycle never feeds again: at 12 of the genus-2
    ring's branches a residue escapes and every cell its class reaches is fed
    by some OTHER class on the cycle, so no coordinate is bounded -- 89
    branches escape at class level against 77 carrying a bounded cell. The
    implication runs one way only, and it is asserted in that direction. What
    holds exactly is the identity: the escaping classes' cells, minus the
    cycle's and minus the clock's own, ARE the bounded coordinates among the
    DEEP PLACES THE WALK PRINTS, branch for branch at every one of the 150 --
    and not one summoned cell fails to be a deep place, so the identity needs
    no remainder term. The comparison is against the walk's own ledger for a
    reason: matching those cells against the recursion's other output instead
    -- the pre-period's cells less the cycle's -- is a TAUTOLOGY, since a
    non-escaping tail residue sits on the cycle and its representative's cells
    are inside the cycle's already, so the subtraction removes exactly the
    difference. That check cannot fail and certifies nothing. This identity is
    what licenses reading the ring-level species off the group-level one, and
    the 12 are what it would have cost to read it off the count instead.

Run: `python explore_increment_group.py`. RUN RECORD (11,839,142 checks,
~105 s, peak 57.8 MB under memwatch -- the six-ring walk is 300 moves on each
of 150 branches and costs most of the wall clock, the sweep itself being
4,907,558 orbits over integer states: 905,558 from the full enumeration at
d = 2 to 6 and 4,002,000 sampled at d = 7 to 16, half of them drawn from the
realizable space directly). S1: PS1's kill fired at the gamma = 0 ring and the
invariant reading is asserted in its place; the hand-attack's nine states
reproduced one by one, with its pre-period 4, cycle 4 and escaping residues
[2, 4]; the detector silent on a pattern WITH a tail whose residue recurs, and
on the proved bijective bar. S2: the tick's period divided every cycle, 0
exceptions; maximum cycle 54 against a period of 6, maximum pre-period 83
against a 2-adic bound of 1. S3: the escape census by d, by primality, and
over the realizable draw. S4: the six realized patterns, all meeting both
constraints, and the class-to-cell set identity holding at every branch.
Slate PS1-PS6: PS1's kill FIRED and is FS1; PS2-PS6 hit. SUPERSEDED at the
run: the slate's reading that the mod-h and mod-d states agree outright, and
its expectation that the two rings carrying riders share an order -- they
carry 5 and 15, and gamma generates at both.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_greedy_image_ec as EC        # the genus 0 and 1 rings
import explore_greedy_image_g2 as G2        # the genus 2 ring
import explore_coarse_type as CT            # the ladder
import explore_element_limit as EL          # the walk, the cells, the door
import explore_rider_recursion as RR        # the recursion this one lifts

CHECKS = 0
FULL_D = 6            # every u: Z/d -> Z/d enumerated at or below this d
SAMPLE_D = 16         # sampled above it, to here
SAMPLE_N = 3000       # patterns sampled per d above FULL_D
SEED = 20250608       # the sampler's seed, fixed so the census is a record


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ------------------------------------------------------- the abstract object
def orbit(d, u, T0, r0, cap=None):
    """The orbit of (T mod d, r mod d) under T' = 2T, r' = T - u(r), as
    (pre-period, cycle length, tail residues, cycle residues). The state space
    is d^2, so the search terminates inside it and the cap is an assertion
    that it did rather than a truncation."""
    cap = cap or (d * d + 2)
    seen, order = {}, []
    T, r = T0 % d, r0 % d
    for _ in range(cap):
        if (T, r) in seen:
            start = seen[(T, r)]
            tail = [rr for _t, rr in order[:start]]
            cyc = [rr for _t, rr in order[start:]]
            return start, len(cyc), tail, cyc
        seen[(T, r)] = len(order)
        order.append((T, r))
        T, r = (2 * T) % d, (T - u[r]) % d
    ok(False, "the state search ran %d steps at d = %d without repeating"
       % (cap, d))


def escapes(d, tail, cyc):
    """The species, at class level: a NON-ZERO residue on the tail that never
    recurs on the cycle. Zero is the identity class, which summons an empty
    representative and therefore no coordinate at all -- counting it would
    report a species that does not exist."""
    return sorted(set(rr for rr in tail if rr % d != 0) - set(cyc))


def tick_period(d):
    """The period of 2^j T0 mod d for T0 a power of 2 -- the multiplicative
    order of 2 modulo the odd part of d, which is 1 when that part is 1."""
    odd = d
    while odd % 2 == 0:
        odd //= 2
    if odd == 1:
        return 1
    o, x = 1, 2 % odd
    while x != 1 % odd:
        x, o = (2 * x) % odd, o + 1
    return o


def v2(n):
    k = 0
    while n % 2 == 0:
        n, k = n // 2, k + 1
    return k


def ticks(d):
    """The residues a TICK can stand at: the powers of 2 mod d, and nothing
    else. A sweep over all T0 would price seeds no clock reaches."""
    out, x = set(), 1 % d
    while x not in out:
        out.add(x)
        x = (2 * x) % d
    return sorted(out)


def patterns(d):
    """Every u: Z/d -> Z/d, as a tuple of d residues."""
    if d == 1:
        yield (0,)
        return
    idx = [0] * d
    while True:
        yield tuple(idx)
        i = d - 1
        while i >= 0 and idx[i] == d - 1:
            idx[i] = 0
            i -= 1
        if i < 0:
            return
        idx[i] += 1


def realizable(d, u, wmax):
    """The constraints the six realized patterns actually meet: the identity
    class returns nothing, and no class returns more than the largest
    multiplicity the clock's cell carries in any representative. Both are READ
    OFF the six rings before the sweep runs and imposed here, never assumed --
    a ceiling written in by hand would be the transplant this rig is guarding
    against."""
    return u[0] == 0 and max(u) <= wmax


# ------------------------------------------------------- reading a ring back
def realized(s):
    """The (d, u, seed) a branch actually carries: gamma's order, the units
    each class of <gamma> returns to the clock's cell, and the state at the
    first clock move past the transient window."""
    _st0, last = EL.settling(s)
    cell, gam = last[0], last[0][1]
    win = RR.window_of(s)
    rows, _c = RR.clock_moves(s)
    past = [row for row in rows if row[0] > win]
    T0, r0 = RR.tick_at(s, past[0][0]), past[0][1]
    d = 1
    while s.GR.scale(gam, d) != 0:
        d += 1
    u = tuple(s.rep[s.GR.negc[s.GR.scale(gam, j)]].get(cell, 0)
              for j in range(d))
    return d, u, T0, r0, cell, gam, past


def main():
    EC.DMAX = G2.DMAX = EL.ENGINE_DMAX
    ladder = CT.build_ladder()

    print("The increment recursion lifted off the ring: T' = 2T, r' = T - w,")
    print("w the units the class -r*gamma returns to the clock's cell. Over a")
    print("finite abelian group that is a map on (Z/d)^2 with d = ord(gamma),")
    print("and the question -- which coordinates deepen past the window and")
    print("then stop -- is whether the orbit's TAIL carries a non-zero residue")
    print("its CYCLE never repeats. No ring, no walk, no limit.")

    shapes = {}
    for L in ladder:
        got, dropped = EL.branches(L, record=False)
        ok(dropped == 0, "%s: the branch sweep dropped %d states, so no column "
           "here is over all branches" % (L.name, dropped))
        shapes[L.name] = [EL.continue_walk(s, EL.WALK_N - EL.BRANCH_N, [0, 0])
                          for s in got]

    # THE REALIZABLE CEILING IS READ, NOT CHOSEN. The sweep's restricted
    # census needs a bound on what a class can return to the clock's cell, and
    # writing one in by hand would price a world no ring is known to inhabit.
    # It is the largest multiplicity the clock's own cell carries in any of
    # the ring's minimal representatives, maximised over the six.
    wmaxes = {}
    for L in ladder:
        wm = 0
        for s in shapes[L.name]:
            cell = EL.settling(s)[1][0]
            wm = max(wm, max(s.rep[c].get(cell, 0) for c in range(s.h)))
        wmaxes[L.name] = wm
    WMAX = max(wmaxes.values())

    section("S1  THE POSITIVE CONTROL")

    print("(a) THE REDUCTION AGAINST THE RIG (PS1) -- AND ITS KILL FIRED")
    print("  The rig carries the state mod h. Every d divides h, so mod h is a")
    print("  refinement -- but the recursion reads only r mod d, and PS1")
    print("  predicted the two agree outright. THEY DO NOT, and the ring that")
    print("  says so is the one with gamma = 0: its state mod h still carries")
    print("  the TICK, whose own period is 2 there, while the classes it")
    print("  summons are the identity forever and its period is 1. So a")
    print("  LENGTH mod h is the state's and not the recursion's output. What")
    print("  the verdicts are read off -- which classes the cycle summons and")
    print("  which the pre-period does -- is the invariant, and that is what")
    print("  is asserted here: the coarse cycle divides the fine one, the")
    print("  coarse pre-period is no longer, and both cell sets agree.")
    print("\n  ring     h   ord(gamma)  branches  pre mod d  pre mod h  "
          "cycle mod d  cycle mod h")
    orders = {}
    for L in ladder:
        rows = set()
        for s in shapes[L.name]:
            d, u, T0, r0, cell, gam, _past = realized(s)
            npre, nc, cyc, cyc_cells, pre_cells = RR.cycle_of(s, gam, cell,
                                                              T0, r0)
            p2, l2, tail2, cyc2 = orbit(d, u, T0, r0)
            ok(nc % l2 == 0, "%s: the fine cycle %d mod h is not a multiple "
               "of the coarse %d mod d, so one of the two states is not this "
               "recursion's" % (L.name, nc, l2))
            ok(p2 <= npre, "%s: the coarse pre-period %d mod d outruns the "
               "fine %d mod h, which a refinement cannot do"
               % (L.name, p2, npre))
            # A STRICTLY LONGER FINE PRE-PERIOD WOULD BE A CORRECTION, NOT A
            # CURIOSITY: the rig files a cell as bounded when the PRE-PERIOD
            # summons it and the cycle does not, so a mod-h tail carrying a
            # residue the mod-d reading has already put on the cycle would
            # over-report the species. Assert equality and let it fire.
            ok(p2 == npre, "%s: pre-period %d mod d against %d mod h, so the "
               "rig's tail is longer than the recursion's and its bounded "
               "cells may include one the cycle feeds forever"
               % (L.name, p2, npre))
            # the classes, not merely the counts: the cycle's summoned cells
            # and the pre-period's are what every verdict is read off, so the
            # reduction has to reproduce THOSE and not two integers.
            cc = {}
            for rr in cyc2:
                for c2, n in s.rep[s.GR.negc[s.GR.scale(gam, rr)]].items():
                    cc[c2] = cc.get(c2, 0) + n
            pc = {}
            for rr in tail2:
                for c2, n in s.rep[s.GR.negc[s.GR.scale(gam, rr)]].items():
                    pc[c2] = pc.get(c2, 0) + n
            # THE SETS AND NOT THE COUNTS, for the reason the kill exposed: a
            # fine cycle that is a proper multiple of the coarse one traverses
            # the same classes more than once, so its multiplicities are its
            # OWN length's and comparing them would fail on the very fact
            # being reported. What a verdict reads is which cells, not how
            # many units one lap puts on them.
            ok(set(cc) == set(cyc_cells), "%s: the cycle summons %s mod d "
               "against %s mod h" % (L.name, sorted(cc), sorted(cyc_cells)))
            ok(set(pc) == set(pre_cells), "%s: the pre-period summons %s mod "
               "d against %s mod h" % (L.name, sorted(pc), sorted(pre_cells)))
            rows.add((s.h, d, p2, npre, l2, nc))
            orders[L.name] = d
        for h, d, p2, npre, l2, nc in sorted(rows):
            n = sum(1 for s in shapes[L.name]
                    if (s.h, realized(s)[0], orbit(*realized(s)[:4])[0])
                    == (h, d, p2))
            print("  %-8s %-3d %-11d %-9d %-10d %-10d %-12d %d"
                  % (L.name, h, d, n, p2, npre, l2, nc))

    print("\n(b) THE HAND-ATTACK (PS2, PS3, PS5)")
    print("  d = 5 -- prime, and the order the ring with NO such")
    print("  coordinate carries --")
    print("  with u(1) = 1 and u zero elsewhere, seeded at (T, r) = (1, 1).")
    print("  The derivation is on paper in this file's header; the engine")
    print("  must reproduce it state by state.")
    hand_u = (0, 1, 0, 0, 0)
    hand_T = [1, 2, 4, 3, 1, 2, 4, 3, 1]
    hand_r = [1, 0, 2, 4, 3, 1, 1, 3, 3]
    T, r = 1, 1
    print("\n  j   T  r")
    for j in range(9):
        ok((T, r) == (hand_T[j], hand_r[j]),
           "the hand-attack reads (%d, %d) at j = %d and the engine (%d, %d)"
           % (hand_T[j], hand_r[j], j, T, r))
        print("  %-3d %-2d %d" % (j, T, r))
        T, r = (2 * T) % 5, (T - hand_u[r]) % 5
    p, l, tail, cyc = orbit(5, hand_u, 1, 1)
    esc = escapes(5, tail, cyc)
    print("  pre-period %d, cycle %d, tail residues %s, cycle residues %s"
          % (p, l, sorted(set(tail)), sorted(set(cyc))))
    print("  escaping residues: %s -- non-zero, and never repeated" % esc)
    ok((p, l) == (4, 4), "the hand-attack's pre-period and cycle are 4 and 4, "
       "and the engine reads %d and %d" % (p, l))
    ok(esc == [2, 4], "the hand-attack escapes at residues 2 and 4, and the "
       "engine reads %s" % esc)
    ok(p > v2(5) + 1, "the hand-attack's pre-period %d is inside the six "
       "rings' own bound, so it witnesses nothing" % p)
    ok(realizable(5, hand_u, WMAX), "the hand-attack's own pattern is outside "
       "the realizable restriction, so it witnesses the quantifier only")

    print("\n(c) THE DETECTOR BOTH WAYS")
    print("  A detector that always fires and one that never fires both read")
    print("  as a census, so one constructed escape and one constructed")
    print("  non-escape are run against it.")
    # THE NEGATIVE CONTROL HAS A TAIL, which is what makes it worth running:
    # u = 0 sends r' to T, so the residues on the cycle are the tick's own
    # orbit -- every non-zero residue at d = 5, since 2 is a primitive root
    # there -- and the seed's residue is among them. So the orbit takes a
    # pre-period of 1 and STILL does not escape. A control with no tail would
    # only show the detector silent where nothing could have fired; this one
    # shows it silent where the rig's own species nearly sits, and it is the
    # shape one of the two rings turns out to have.
    p0, l0, t0, c0 = orbit(5, (0, 0, 0, 0, 0), 1, 1)
    ok(p0 == 1, "the u = 0 pattern at d = 5 from (1, 1) takes a pre-period of "
       "%d against the derivation's 1" % p0)
    ok(sorted(set(t0)) == [1] and 1 in c0, "the u = 0 control's tail residue "
       "is %s against a cycle of %s, so it is not the recurring-residue case "
       "it was built to be" % (sorted(set(t0)), sorted(set(c0))))
    ok(escapes(5, t0, c0) == [], "the detector fires on a tail whose only "
       "residue recurs on the cycle")
    print("  u = 0 at d = 5 from (1, 1): pre-period %d, tail residue %s, "
          "cycle %s" % (p0, sorted(set(t0)), sorted(set(c0))))
    print("  -- a tail that does NOT escape, because its residue recurs: "
          "silent")
    print("  the hand-attack above: escape at %s -- fires" % esc)
    # and the proved bar, at a bijective specimen: odd d, u injective.
    pb, lb, tb, cb = orbit(5, (0, 1, 2, 3, 4), 1, 1)
    ok(pb == 0 and escapes(5, tb, cb) == [],
       "an injective u at odd d gives a bijection, so the pre-period must be "
       "empty, and the engine reads %d" % pb)
    print("  u injective at d = 5 (the proved bar, PS4): pre-period %d, "
          "silent" % pb)

    section("S2  THE SWEEP")
    print("  PS2, PS3, PS4. Every u: Z/d -> Z/d at d up to %d, every seed"
          % FULL_D)
    print("  whose tick is a power of 2 -- the only ticks a clock stands at --")
    print("  and a sampled census above. The tick's own period must divide")
    print("  every cycle; the two bounds the six rings never exceed are")
    print("  tested against the whole enumeration.")
    print("\n  d   patterns  seeds  orbits  tick period  max cycle  "
          "max pre-period  2-adic bound")
    census = {}
    rng = random.Random(SEED)
    for d in range(2, SAMPLE_D + 1):
        tp, bound = tick_period(d), v2(d) + 1
        seeds = [(T0, r0) for T0 in ticks(d) for r0 in range(d)]
        # ABOVE THE FULL-ENUMERATION BOUND THE RESTRICTED CENSUS NEEDS ITS OWN
        # SAMPLE. A pattern drawn uniformly from d^d almost never has every
        # value inside the ring's ceiling, so reading the restricted rate off
        # the same draw would print a rate over a handful of orbits at d = 7
        # and a zero over none at all above it -- a sampling artifact wearing
        # the shape of a finding, which is exactly the failure this rig's
        # second transplant flag names. So the realizable space is sampled
        # directly, and it is a DIFFERENT draw with its own column.
        if d <= FULL_D:
            pats, rpats = list(patterns(d)), None
        else:
            pats = [tuple(rng.randrange(d) for _ in range(d))
                    for _ in range(SAMPLE_N)]
            rpats = [(0,) + tuple(rng.randrange(WMAX + 1)
                                  for _ in range(d - 1))
                     for _ in range(SAMPLE_N)]
        maxc = maxp = 0
        n_esc = n_pre = n_tot = 0
        n_resc = n_rtot = 0
        for src, u in ([(0, u) for u in pats]
                       + [(1, u) for u in (rpats or [])]):
            rz = realizable(d, u, WMAX)
            for T0, r0 in seeds:
                p, l, tail, cyc = orbit(d, u, T0, r0)
                ok(l % tp == 0, "d = %d: the tick's period %d does not divide "
                   "the cycle %d at u = %s, seed (%d, %d)"
                   % (d, tp, l, u, T0, r0))
                e = escapes(d, tail, cyc)
                if e:
                    ok(p > 0, "d = %d: an escape off an orbit with no "
                       "pre-period" % d)
                    ok(not (d % 2 and len(set(u)) == d),
                       "d = %d: an escape at odd d under an injective u, "
                       "which is a bijection and cannot have a tail" % d)
                maxc, maxp = max(maxc, l), max(maxp, p)
                # the two draws are counted into two columns and never into
                # one: the unrestricted census is the first draw's, the
                # restricted one the realizable draw's where there is one.
                if src == 0:
                    n_tot += 1
                    n_pre += 1 if p else 0
                    n_esc += 1 if e else 0
                if rz and (src == 1 or rpats is None):
                    n_rtot += 1
                    n_resc += 1 if e else 0
        census[d] = (n_tot, n_pre, n_esc, n_rtot, n_resc, rpats is not None)
        print("  %-3d %-9d %-6d %-7d %-12d %-10d %-15d %d"
              % (d, len(pats), len(seeds), n_tot, tp, maxc, maxp, bound))
    ok(any(census[d][0] for d in census), "the sweep ran no orbit at all")

    section("S3  THE VERDICT")
    print("  PS5. The escape census: how often a non-zero tail residue never")
    print("  recurs, by d and by whether d is prime. The suspicion on record")
    print("  says the species needs a class number with proper subgroups.")
    print("  The realizable columns at d above %d are a SEPARATE draw from the"
          % FULL_D)
    print("  realizable space, never a filter on the first draw -- a uniform")
    print("  pattern almost never meets the ring's own ceiling, so filtering")
    print("  would print a rate over almost nothing.")
    print("\n  d   prime  draw     orbits  with a pre-period  escaping  "
          "escape rate  realizable orbits  escaping  rate")
    prime_tot = prime_esc = comp_tot = comp_esc = 0
    full_tot = full_pre = full_esc = full_rtot = full_resc = 0
    for d in range(2, SAMPLE_D + 1):
        n_tot, n_pre, n_esc, n_rtot, n_resc, sampled = census[d]
        isp = d > 1 and all(d % q for q in range(2, int(d ** 0.5) + 1))
        print("  %-3d %-6s %-8s %-7d %-18d %-9d %-12.1f %-18d %-9d %.1f"
              % (d, "yes" if isp else "no",
                 "sampled" if sampled else "full", n_tot, n_pre, n_esc,
                 100.0 * n_esc / n_tot, n_rtot, n_resc,
                 100.0 * n_resc / n_rtot if n_rtot else 0.0))
        if d <= FULL_D:
            full_tot += n_tot
            full_pre += n_pre
            full_esc += n_esc
            full_rtot += n_rtot
            full_resc += n_resc
            if isp:
                prime_tot, prime_esc = prime_tot + n_tot, prime_esc + n_esc
            else:
                comp_tot, comp_esc = comp_tot + n_tot, comp_esc + n_esc
    print("\n  over the FULL enumeration (d <= %d), where every pattern is "
          "present:" % FULL_D)
    print("    prime d:      %d orbits, %d escaping, %.1f%%"
          % (prime_tot, prime_esc, 100.0 * prime_esc / prime_tot))
    print("    composite d:  %d orbits, %d escaping, %.1f%%"
          % (comp_tot, comp_esc, 100.0 * comp_esc / comp_tot))
    print("    with a pre-period at all: %d of %d (%.1f%%), of which %d "
          "escape (%.1f%%)"
          % (full_pre, full_tot, 100.0 * full_pre / full_tot, full_esc,
             100.0 * full_esc / full_pre))
    print("    realizable patterns only: %d of %d orbits (%.1f%%), %d "
          "escaping (%.1f%%)"
          % (full_rtot, full_tot, 100.0 * full_rtot / full_tot, full_resc,
             100.0 * full_resc / full_rtot))
    ok(prime_esc > 0, "no orbit at prime d escapes in the full enumeration, "
       "so the suspicion survives as a rule in range")
    ok(census[5][2] > 0, "no orbit escapes at d = 5 -- the order the ring "
       "with no such coordinate carries -- so the suspicion survives where "
       "it was asked")

    section("S4  THE RINGS READ BACK IN")
    print("  PS1, PS6. The six realized patterns, the constraints they meet,")
    print("  and the class-level species against the cell-level one the walk")
    print("  prints. The abstraction is worth what it recovers here.")
    print("  The ceiling the restricted census used is %d, the largest count"
          % WMAX)
    print("  any of these rings returns to its clock's cell in one")
    print("  representative: %s." % sorted(wmaxes.items()))
    print("\n  ring     d  u                 seed (T, r)  pre  cycle  "
          "escaping residues  u(0)=0  max u")
    for L in ladder:
        rows = {}
        for s in shapes[L.name]:
            d, u, T0, r0, cell, gam, _past = realized(s)
            p, l, tail, cyc = orbit(d, u, T0, r0)
            wmax = max(s.rep[c].get(cell, 0) for c in range(s.h))
            ok(wmax == wmaxes[L.name], "%s: a branch carries a largest "
               "multiplicity of %d against the ring's %d, so the ceiling the "
               "sweep used is not this ring's"
               % (L.name, wmax, wmaxes[L.name]))
            key = (d, u, T0 % d, r0 % d, p, l, tuple(escapes(d, tail, cyc)),
                   wmax)
            rows[key] = rows.get(key, 0) + 1
            ok(u[0] == 0, "%s: the identity class returns %d units to the "
               "clock, so the realizable constraint is not the rings'"
               % (L.name, u[0]))
            ok(max(u) <= wmax, "%s: a class returns %d units against the "
               "ring's largest multiplicity %d" % (L.name, max(u), wmax))
        for key in sorted(rows):
            d, u, T0, r0, p, l, esc, wmax = key
            print("  %-8s %-2d %-17s (%d, %d)%s %-4d %-6d %-18s %-7s %d"
                  % (L.name, d, list(u), T0, r0, " " * 6, p, l,
                     list(esc) if esc else "none", "yes", wmax))

    print("\n  THE CLASS-LEVEL SPECIES AGAINST THE CELL-LEVEL ONE. A residue")
    print("  escaping is a CLASS the cycle never summons again; the walk's own")
    print("  species is a CELL the cycle never feeds again. The first implies")
    print("  the second only if the class's cells are not reached by some")
    print("  other class on the cycle, so the two are compared branch by")
    print("  branch rather than one read off the other.")
    print("\n  ring     branches  class-level escapes  cell-level bounded  "
          "branches where they part  summoned but not a deep place")
    for L in ladder:
        n_cls = n_cell = n_agree = 0
        unseen = set()
        for s in shapes[L.name]:
            d, u, T0, r0, cell, gam, _past = realized(s)
            p, l, tail, cyc = orbit(d, u, T0, r0)
            esc = escapes(d, tail, cyc)
            _c, _np, _nc, cyc_cells, pre_cells = RR.cycle_of(s, gam, cell,
                                                             T0, r0)
            # the cells the ESCAPING classes reach, which is what the class
            # level actually predicts once the representatives are put back.
            pred = set()
            for rr in esc:
                pred |= set(s.rep[s.GR.negc[s.GR.scale(gam, rr)]])
            pred -= set(cyc_cells) | set([cell])
            # AGAINST THE WALK'S OWN LEDGER, and not against the recursion's
            # other output. Comparing pred with pre_cells minus the cycle's
            # would be a TAUTOLOGY -- a tail residue that is not escaping sits
            # on the cycle, so its representative's cells are inside cyc_cells
            # and the subtraction removes exactly the difference between the
            # two sets. That check cannot fail and would certify nothing. What
            # can fail is the walk: the DEEP PLACES it actually prints,
            # sorted the way the rider rig sorts them.
            places = set((dd, cc) for dd, cc, _e, _co, _ri
                         in EL.deep_places(s))
            walk_bounded = set(pc for pc in places
                               if pc != cell and pc not in cyc_cells
                               and pc in pre_cells)
            ok(pred & places == walk_bounded, "%s: the escaping classes reach "
               "%s among the walk's deep places and the walk's bounded ones "
               "are %s" % (L.name, sorted(pred & places),
                           sorted(walk_bounded)))
            unseen |= pred - places
            bounded = walk_bounded
            # THE DIRECTION THAT IS A LAW, and it is only one. A bounded cell
            # is fed by some class the cycle never summons again, so it forces
            # an escaping residue; the converse fails, and the branches below
            # are where it fails -- an escaping class ALL of whose cells some
            # other class on the cycle keeps feeding, which leaves no bounded
            # coordinate at all. The set identity above is the bridge; the
            # counts here are what it costs to read one level off the other.
            ok(not bounded or esc, "%s: a cell is bounded with no class "
               "escaping, so the cell level is not the class level's image"
               % L.name)
            n_cls += 1 if esc else 0
            n_cell += 1 if bounded else 0
            n_agree += 1 if bool(esc) == bool(bounded) else 0
        print("  %-8s %-9d %-20d %-19d %-24d %s"
              % (L.name, len(shapes[L.name]), n_cls, n_cell,
                 len(shapes[L.name]) - n_agree,
                 sorted(unseen) if unseen else "none"))
        ok(n_cell <= n_cls, "%s: more branches carry a bounded cell than "
           "carry an escaping class, which inverts the implication"
           % L.name)

    section("SUMMARY")
    print("  %d checks passed." % CHECKS)


if __name__ == "__main__":
    main()
