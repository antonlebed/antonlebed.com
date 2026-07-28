"""explore_lock_budget.py -- WHY A NUMBER RING'S LADDER STOPS WHEN THE
SCHEDULE SAYS IT CANNOT: the clock that never grows.

THE CONTRADICTION THIS IS ABOUT. Two measured results in this corpus do not
sit together.

 (i) A number ring's greedy trajectory LOCKS. The openings stop, the walk
     re-deepens one recurrent vehicle forever, and the greedy image is
     finite (explore_greedy_image_nf.py F1, over two rings and four belts).
 (ii) The abstract schedule says WHAT CAN STOP A LADDER: a covered set that
     OUTRUNS it. A covering rule fed by the openings themselves never
     manages it, because it is always chasing what it would have to get
     ahead of; only a covered set growing with the CLOCK outruns a ladder
     that climbs by one degree per opening (explore_ladder_stop.py F4).

A number ring's rule is exactly such a fed-by-the-openings rule: its door
is the least r with lambda(P^(e+r)) not dividing the seated set's invariant
(explore_module_law.py door_r), lambda(P^1) is N(P) - 1 at split, inert and
ramified alike, and the invariant is an LCM over the seated places. So a
fresh place is COVERED -- door above 1, no discount -- exactly when
N(P) - 1 divides an LCM the openings feed. Reading that rule over the
rational primes, coverage really does spread (the fraction of primes below
x with p - 1 dividing such an LCM climbs past four fifths by 10^6) but the
ESCAPES DIVERGE: thousands of primes below 10^6 stay uncoverable. On the
schedule's reading the ring's ladder should never stop, and the measured
lock should not exist.

THE QUESTION. Which of the two is wrong, and where exactly? The candidates
carried in were that the lock is not a covering phenomenon at all; that the
toy reading of lambda is too weak; that the measured lock is an artifact of
the engine's capped universe; or that the schedule's "outruns" reading is
too coarse for a supply whose degrees are log-norms.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. "Outruns",
"ladder", "escape density" are all the SCHEDULE's words, and the handover's
own hand-attack -- "at tick T the walk can afford every norm under about
e^(T/2)" -- is written in them. A number ring has no object called T. That
phrase is the transplant to attack first.

TRANSPLANT FLAGS, fixed at the freeze.
 1. From the schedule to the ring: "at tick T the walk affords norms up to
    f(T)". The schedule's budget grows because its staleness accumulates
    against a GLOBAL tick. Whether a ring has any growing budget is the
    thing to measure, not to assume.
 2. From the schedule to the ring: "the ladder climbs". In the schedule the
    least uncovered degree increases without bound. Nothing says a ring's
    cheapest move climbs at all.
 3. From the rational primes to the ring: the density calculation above
    ranges over primes to 10^6. The engines run a universe capped at norm
    2000, so any density read there is a different measurement and is
    reported as such.
 4. From the ideal world to the element world. Everything here is the IDEAL
    world; an element move seats a bundle and is not covered by any of it.
    (SINCE SETTLED, and the argument DOES cover it, by not having to reach
    several places at all. The element tails were already measured flat by
    both rings' own element censuses; what was missing was why. The
    recurrent vehicle's form is a core at its door times the minimal
    representative of the class that power must cancel, so the price
    FACTORS: the first factor is flat by F1's valuation argument verbatim,
    and the second is a table lookup on a finite group, fixed once the door
    is. explore_element_schedule_nf.py F3.)

THE HAND-ATTACK, on paper before any engine code.

 A. THE RING'S PRICE IN THE SCHEDULE'S TERMS. A move at place P seated at
    depth e costs N(P)^r with r = door_r(P, e, L). Taking logs that is
    price(d, sigma) = d * sigma at degree d = log N(P) and staleness
    sigma = r. So the ring IS an alpha = 1 schedule -- as far as the price.

 B. BUT ITS CLOCK IS PER-PLACE. The schedule's staleness is T + 1 - e for a
    GLOBAL T. The ring's door exponent reads only the p-part of L, where
    p = char(P): with V_p = v_p(L) and a split place's
    lambda(P^a) = (p-1) * p^(a-1), the door is the least r with
    e + r - 1 > V_p, i.e. r = V_p - e + 2 whenever V_p >= e - 1. Different
    rational primes have unrelated V_p. There is no global tick anywhere.

 C. SO THE RECURRENT MOVE'S PRICE DOES NOT GROW. Deepening P from e to
    e + r takes the depth to e + r AND takes v_p(L) to e + r - 1, which is
    (new depth) - 1. The next door at P is therefore 1. A recurrent vehicle
    costs exactly N(P) per move, forever, self-correcting after at most one
    expensive move. (The ramified shapes pump on a//2 rather than a - 1, so
    their door can sit at a constant 2 instead; bounded either way, and the
    rig prints the sequence rather than trusting this.)

 D. WHENCE THE LOCK IS A SMALL-NORM CONDITION AND NOT A DENSITY ONE. If the
    walk's cheapest move costs N(P_deep) forever, then every place Q with
    N(Q) < N(P_deep) must be covered hard enough that N(Q)^r > N(P_deep),
    and every place of larger norm is declined by its norm alone whether
    covered or not. That is a condition over a handful of small places. The
    thousands of divergent escapes at 10^6 are irrelevant: an escape costs
    its norm, and the ring never gets richer.

 E. WHAT THAT MAKES THE SCHEDULE RESULT. Not wrong -- scoped. "A covered set
    that outruns the ladder" is one way to stop a ladder that CLIMBS. A
    ladder whose budget never grows needs no outrunning: it stops at the
    first degree it cannot afford. The schedule family cannot express this,
    because a global tick is built into its walker.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 THE RECURRENT PRICE IS FLAT. Over every locking ideal seed of both
    belts, the cost sequence of the recurrent tail is eventually constant,
    and its constant is at most the lock cost. What the rig PRINTS: per
    ring, the distinct tail costs and the maximum over all seeds of
    (last tail cost) / (first tail cost).
    KILL: one seed whose tail cost grows without bound, or grows at all
    after its first TAIL_SETTLE moves.

PR2 THE LOCK DECLINES REAL ESCAPES. At every lock state there EXIST
    uncovered places -- door exactly 1 -- in the engine's universe, and the
    least-norm one costs strictly more than the lock cost. What the rig
    PRINTS: per seed, the lock cost, the least uncovered norm, and the count
    of uncovered places in the universe.
    KILL: one lock state with no door-1 place in its universe, which would
    make the lock a capacity fact rather than a price one.

PR3 THE LOCK IS SETTLED BY THE SMALL PLACES ONLY. At every lock state every
    place of norm below the lock cost has door r >= 2, and the number of
    such places is small. What the rig PRINTS: per seed, that count and the
    largest of them.
    KILL: a lock state with a door-1 place of norm below the lock cost,
    which would mean the menu is not taking its own minimum.

PR4 THE CAPPED UNIVERSE IS NOT DOING THE WORK. Lock costs sit far below the
    engines' MAXP, and the least uncovered norm sits far below it too. What
    the rig PRINTS: the maximum lock cost and the maximum least-uncovered
    norm over all seeds, against MAXP.
    KILL: either quantity within a factor of 2 of MAXP.

PR5 COVERAGE DENSITY IS NOT WHAT STOPS IT. At a lock state the covered
    FRACTION of the universe is small and falls with the norm, while the
    ladder is stopped regardless. What the rig PRINTS: covered counts by
    norm decade at the deepest lock state of each ring.
    No kill -- a measurement frozen as such, read against the density
    reading it is meant to displace.

PR6 THE A/B: THE SCHEDULE'S BUDGET GROWS AND THE RING'S DOES NOT. Along an
    abstract schedule walk the menu's minimum cost grows without bound;
    along a ring's recurrent tail it is flat. What the rig PRINTS: both
    sequences side by side, and the ratio of last to first for each.
    KILL: the schedule's minimum cost is also flat, which would put the
    difference somewhere other than the clock.

PR7 A PER-CLASS CLOCK STOPS THE LADDER INSIDE THE SCHEDULE FAMILY. Give the
    abstract walker one tick per ITEM instead of one global tick, changing
    nothing else, and its ladder stops with uncovered degrees still on the
    supply; with one class for all items it climbs. What the rig PRINTS:
    the opened degrees and the final least-uncovered degree under both,
    over the same supply and schedule.
    KILL: the per-class walker's ladder climbs too, which would mean the
    clock's locality is not the difference.

Predict, from D: the ring's lock costs are small -- single or low double
digits -- and the count of places settling each lock is under ten.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 A NUMBER RING'S GREEDY WALK HAS NO GROWING BUDGET: THE RECURRENT PRICE IS
   FLAT (rule in range; 131 locking ideal seeds over the two rings' norm-40
   belts -- 52 at K5 and 79 at K23 -- 40 tail moves recorded past each lock,
   0 tails non-flat past move 3, 0 tails carrying a TIE anywhere in them so
   that each flat sequence is the lock's rather than one branch's, and every
   settled tail cost at or below its own lock cost). The distinct settled
   costs are 3, 4, 7 and 23 at K5 and
   2, 3, 13 and 25 at K23; the largest (last cost)/(first cost) over all 131
   is 1. The mechanism is a two-line derivation the run confirms rather than
   assumes: deepening P from e to e + r takes the depth to e + r AND takes
   v_p(L) to e + r - 1, which is the new depth minus one, so the next door
   at P is 1 and the vehicle costs exactly N(P) per move forever. The lone
   exception is the shape the hand-attack flagged -- 1 of the 131 locks
   (K5's R2, at cost 4 = 2^2) has a vehicle whose own door is 2, the
   ramified lambda pumping on a//2 rather than a - 1, so its door sits at a
   CONSTANT 2 instead of a constant 1. Flat either way, which is the whole
   of it. (Constant HERE because the rest of the seated set pins its
   valuation; the same place deepening ALONE alternates with period 2 rather
   than settling -- F6, which reads the pumps in isolation. Bounded and never
   growing under both readings, which is all either claim needs.)

F2 SO THE LOCK DECLINES HUNDREDS OF REAL ESCAPES, AND IS SETTLED BY A
   HANDFUL OF SMALL PLACES (rule in range, the same 131 locks, the whole
   universe scanned at each rather than the engine's own scan that stops at
   the menu's minimum). At every lock there are 284 to 302 fresh door-1
   places at K5 and 261 to 292 at K23, out of universes of 306 and 298 --
   the escapes are not merely plentiful, they are almost everything. The
   least fresh uncovered norm is 5 to 41 at K5 and 13 to 29 at K23, against
   lock costs of 3 to 23 and 2 to 25. What has to be covered for a lock is
   the places of norm BELOW the lock cost, and there are 1 to 6 of them at
   K5 and 0 to 7 at K23. The divergence of the escapes is therefore true and
   IRRELEVANT: an escape costs its norm, and nothing in a ring ever makes
   the walk richer.
   PR2 AS FROZEN MISSED, and the miss is the mechanism. It predicted the
   least-norm uncovered place would cost MORE than the lock; the least-norm
   uncovered place is the RECURRENT one itself, at exactly the lock cost --
   its own door staying 1 forever is precisely what pins the price flat.
   Re-read over the FRESH places, which are the escapes a lock declines, the
   observable holds at every seed. PR1, PR3 and PR4 hit as frozen.

F3 COVERAGE DENSITY IS NOT THE MECHANISM, AND THE CAPPED UNIVERSE IS NOT
   DOING THE WORK (observation at the deepest lock of each ring, plus a rule
   in range for the cap). At K5's deepest lock 18 of 306 places are covered
   and at K23's 36 of 298 -- 6% and 12% -- falling from 1.000 in the first
   norm decade to 0.000 above norm 1000 at K5 and 0.045 at K23. The ladder
   is stopped at both. So the handover's density calculation over the
   rational primes was not measuring the mechanism wrongly; it was measuring
   the wrong thing. The engines' universe cap is separately exonerated: the
   largest lock cost over all 131 seeds is 25 and the largest least-
   uncovered norm is 41, both against MAXP = 2000.

F4 WHICH SIDE OF THE CONTRADICTION LOSES, AND IT IS THE SCHEDULE READING
   (rule in range; the two walks run side by side over 40 moves). The
   abstract schedule's menu minimum runs 2, 1, 2, 2, 3, 4, 4, 5, ... to 34,
   a last/first of 17 with the tick at 128; a ring's recurrent tail is 3
   at every one of 40 moves, a last/first of 1. The schedule's staleness
   accumulates against a GLOBAL tick that grows by ceil(b*T), so its
   cheapest move gets dearer and the ladder climbs; a ring's door reads only
   v_p(L) and lands exactly on the exponent it is answering, so its cheapest
   move never gets dearer at all. explore_ladder_stop.py F4 -- "what stops a
   ladder is a covered set that OUTRUNS it" -- is therefore SCOPED rather
   than wrong: it is one way to stop a ladder that CLIMBS. A ladder whose
   budget never grows needs no outrunning; it stops at the first degree it
   cannot afford and stays there. The measured lock stands, and a covering
   rule was never what produced it.

F5 THE INGREDIENT IS THE TICK'S EXACTNESS, NOT ITS LOCALITY -- AND THE
   SCHEDULE FAMILY CAN EXPRESS A RING'S STOP AFTER ALL, ON AN INGREDIENT IT
   HAS NEVER CARRIED
   (SCOPED SINCE, explore_tick_pump.py: the ingredient is the gap's
   BOUNDEDNESS, of which an exact tick is the extreme point gap 1. Constant
   gaps 2, 3 and 5 stop the ladder exactly as gap 1 does, so what this
   finding reads is two points of a spectrum. Its own two cells and every
   number quoted below stand.) (rule in range over a 2x2 grid, 120 moves per cell,
   same supply of two items at every degree to 400 and the same seed). At a
   DOUBLING tick the ladder climbs under both clocks: 115 degrees seated
   under one global tick, 21 under one tick per item, both still climbing at
   move 120. At an EXACT tick -- the tick advancing to max(T, e) rather than
   to ceil(b*T) -- both clocks STOP after seating one degree past the seed,
   with degree 2 still uncovered and door-1 on a supply that never runs out.
   So locality changes how FAST a ladder climbs, by a factor of five here,
   and decides nothing about whether it climbs; overshoot decides that.
   LOCALITY IS STILL WHAT MAKES THE PRICES RING-FAITHFUL, which matters to
   anyone building in this corner rather than to the verdict: a COVERED fresh
   place over a new rational prime costs N(Q)^2 in a ring, because that
   prime's valuation in the invariant is 0 whatever else is seated -- which
   is d*2 in log terms and is what a per-item tick gives, where a global tick
   would charge d*(T+1). So the ring's own corner of the grid is per-item AND
   exact; the global-exact cell stops for the same reason without pricing a
   ring's fresh opens correctly.
   PR7 AS FROZEN MISSED: it named locality, which is the axis the ring makes
   visible but not the one that bites. And HAND-ATTACK E MISSED with it -- it
   read the global tick as built into the walker and concluded the family
   "cannot express this", where what is built in is the LANDING RULE, one
   line of `apply`, and the family expresses the ring's stop as soon as that
   line is the thing dialled. The corner is new because it was unreachable
   from the parameters: b is a growth FACTOR everywhere here, the degree
   ceiling d_min*(b/(b-1))^(1/alpha) diverges as b -> 1, and the walker's own
   `while T < e2: T = tick_up(T)` does not terminate at b = 1, so the exact
   corner is a fifth ingredient built rather than a fourth dialled.

F6 AND THE LOCK/SPRAWL DICHOTOMY IS THAT SAME AXIS, SO THE TWO ARE ONE FACT
   (WIDENED SINCE, explore_tick_pump.py: linear against logarithmic stands,
   and the linear side is the whole CONSTANT-GAP family with the gap equal
   to the ramification index, measured at 90 places. The "table anomaly"
   this finding tolerates below is the principal-unit filtration's predicted
   HEAD, present at exactly the places with p - 1 <= e -- true of these
   places, but not the criterion: explore_head_width.py F2 needs f = 1,
   mu_p in K_P and e = (p-1)p^t.)
   (rule in range; a lone place deepened with nothing else seated, doors read
   at depths 1..24, over both number rings' place kinds and three function-
   field degrees, the function field's pump imported from its own engine).
   DERIVED AFTER THE RUN and checked here -- the slate asked only which side
   of the contradiction was wrong, and this asks why the two worlds sit on
   opposite sides of the axis the answer turned out to be about.
   A number ring's lambda(P^a) carries p^(a-1), so v_p is LINEAR in the
   depth -- and (p^2-1)*p^(a-1) at an inert place, the same shape -- so a
   deepening clears its own valuation by exactly one and the door returns to
   1. Measured, a lone odd split place's and a lone inert place's door is 1
   at all 24 depths in both rings. A function field's carries 2^ceil_log2(a), so v_2 is
   LOGARITHMIC: clearing it needs the depth to reach the next power of two,
   and the door runs 1, 1, 2, 1, 4, 3, 2, 1, 8, 7, ... 16, 15, ... -- growing
   like the depth itself, identically at degrees 1, 2 and 3. The landing is
   exactly the schedule walker's own law, e + r = (the tick) + 1 at the tick
   2^ceil_log2(e), checked at all 24 depths of all three degrees.
   So THE DICHOTOMY IS NOT ABOUT THE RINGS' SUPPLIES OR THEIR CLASS GROUPS OR
   ANY DEPTH OF ARITHMETIC: it is the shape of lambda's own p-part, linear
   against logarithmic, and everything else -- exact tick against doubling,
   flat budget against climbing, lock against sprawl -- follows from that one
   difference. The two exceptions are bounded and change nothing: the
   RAMIFIED shapes pump on a//2 and so alternate with period 2 rather than
   settling at 1 (never growing), and K23's split place over 2 carries a
   table anomaly that costs it one door of 2 before it settles.

F7 AND THE TWO AXES DECIDE DIFFERENT THINGS: EXACTNESS THE LADDER'S FATE,
   LOCALITY THE LIMIT'S SHAPE
   (REFINED SINCE, explore_tick_pump.py: what decides the limit's shape is
   the GAP under a local clock, not locality itself -- a local clock at gap
   1 or 2 keeps one runaway coordinate and at gaps 3 and 5 carries 3 and 6.
   Locality is what makes an item's own gap visible to the price.) (rule in range, the same 2x2 grid read for a
   second observable -- how many seated items stand above exponent 1 after
   120 moves; derived after the run, the freeze having asked nothing about
   the limit). The filed limit theorem is ONE deep coordinate over a support
   flat forever, proved across every dial the four-ingredient sweep could
   reach and reachable at none of these. It SURVIVES the exact tick under
   both clocks -- 1 item above exponent 1, at degree 1 and exponent 121 --
   so a stopped ladder does not cost the limit its shape, and the global
   doubling cell reproduces the filed shape as a control. What BREAKS it is
   the other cell: a PER-ITEM tick that GROWS gives every item its own
   runaway clock, and 32 of the 21 seated degrees' items stand above
   exponent 1 with no flat support at all.
   So locality is not the idle axis F5 leaves it looking like -- it is idle
   for the LADDER and decisive for the LIMIT, and the two questions the
   corpus has been asking together come apart here. A number ring sits at
   per-item AND exact, which is why it keeps both: a stopped ladder and a
   flat support. Everything the corpus has measured about limits lives in
   the two cells that keep the shape, and the cell that loses it has never
   been walked.

F8 WHAT IS LEFT OPEN. (i) Everything here is the IDEAL world. An element
   move seats a BUNDLE and its recurrent vehicle is a product of places, so
   whether an element walk's price is flat is untested -- and it is the one
   world where the lock is already known to do something the ideal world
   cannot (it swallows a tie, explore_greedy_image_nf.py F5).
   (ANSWERED SINCE, explore_element_schedule_nf.py F3: it is flat, and the
   bundle is why the question was mis-framed rather than why it was hard.
   That file pins the recurrent vehicle's FORM, so the price FACTORS -- the
   first factor flat by this file's own valuation argument verbatim, the
   second a table lookup on a finite group and constant once the door is
   fixed. So the element world needs no argument of its own; it is this
   mechanism composed with the rider being a price. The transplant flag
   above was right that the argument covers one place and a move seats
   several, and wrong that it therefore had to reach several.) (ii) The
   exact-tick corner is now a named and unexplored region of the schedule
   family: the limit theorem, the degree ceiling and the image counts are
   all derived at b > 1, and what the IMAGE is at an exact tick is unasked.
   (ANSWERED SINCE, explore_tick_pump.py: the limit survives, the ceiling
   is a geometric ladder's alone and diverges here, and the image is finite
   and small -- 4 limits at gap 1 over one supply, saturating early.)
   (iii) The norm-indexed covering rule that explore_ladder_stop.py F7 named
   as the next target is still buildable but its motivation is spent -- the
   covering rule was not the mechanism, so a norm-indexed one would answer a
   question this run closes.

RUN RECORD. One process, CPython, no BLAS. Wall 0.3s, peak working set
~21 MB across runs against the 512 MB ceiling. 2922 checks here, the two
ring engines
and the schedule walker imported rather than re-implemented. The cost is
set by the universe scan at each of the 131 locks, which is the measurement
that makes F2 a statement about the whole universe rather than about the
menu's own truncated scan.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction

import explore_number_field_lock as K5     # the h = 2 ring
import explore_module_law as K23           # the h = 3 ring
import explore_price_schedule as PS        # the abstract schedule + walker
import explore_greedy_image_ec as EC       # the function field's pump, for S7

CHECKS = 0

SEED_CAP = 40        # generator-product seeds by norm, as the image census
LOCK_R = 10          # consecutive identical vehicles that witness a lock
WALK_CAP = 60        # moves allowed before the lock probe gives up
TAIL_N = 40          # recurrent moves recorded past the lock
TAIL_SETTLE = 3      # tail moves allowed to settle before flatness is read
SCHED_N = 40         # moves of the abstract global-clock walk in the A/B

RINGS = [("K5", K5, "Z[sqrt(-5)], h = 2"),
         ("K23", K23, "Z[w], w^2 = w - 6, h = 3")]


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def show_place(M, pl):
    if pl[0] == 'split':
        return "P%d.%d" % (pl[1], pl[2])
    if pl[0] == 'inert':
        return "Q%d" % pl[1]
    return "R%d" % pl[1]


def show_state(M, st):
    parts = ["%s^%d" % (show_place(M, pl), e)
             for pl, e in sorted(st.items(), key=lambda kv: M.place_key(kv[0]))
             if e]
    return "*".join(parts) if parts else "(1)"


# ------------------------------------------------------------- the ring walk
def step_once(M, st, L):
    """One greedy move, first tie member taken. Returns (cost, vehicle)."""
    cost, ties = M.ideal_menu(st, L)
    pl, r = ties[0]
    return cost, (pl, r)


def apply_move(st, pl, r):
    out = dict(st)
    out[pl] = out.get(pl, 0) + r
    return out


def walk_to_lock(M, seed):
    """Walk greedily until LOCK_R consecutive moves are the same vehicle at
    the same place. Returns (state, L, vehicle place, lock cost, steps) or
    None where no lock is witnessed inside WALK_CAP."""
    st = dict(seed)
    L = M.lam_state(st)
    run_pl, run = None, 0
    for i in range(WALK_CAP):
        cost, (pl, r) = step_once(M, st, L)
        if pl == run_pl:
            run += 1
        else:
            run_pl, run = pl, 1
        st = apply_move(st, pl, r)
        L = M.lam_state(st)
        if run >= LOCK_R:
            return st, L, pl, cost, i + 1
    return None


def scan_universe(M, st, L, ceiling=None):
    """Every place's door and cost at one state. Returns a list of
    (norm, door, cost, place), scanning the WHOLE universe rather than
    stopping at the menu's minimum the way the engine's own scan does."""
    out = []
    for pl in M.UNIVERSE:
        nrm = M.place_norm(pl)
        if ceiling is not None and nrm > ceiling:
            continue
        r = M.door_r(pl, st.get(pl, 0), L)
        out.append((nrm, r, nrm ** r, pl))
    return out


# ------------------------------------------------------ S1 positive control
def s1_control():
    section("S1  POSITIVE CONTROL -- the covered direction and a filed lock, "
            "through the imported engines")

    # (a) lambda(P^1) is N(P) - 1 at every place kind, both rings, which is
    #     what makes "covered" readable as a divisibility test on N(P) - 1.
    kinds = {}
    for name, M, _ in RINGS:
        for pl in M.UNIVERSE:
            lam1 = M.lam_P(pl, 1)
            nrm = M.place_norm(pl)
            ok(lam1 == nrm - 1,
               "%s: lambda(%s^1) = %d, not N - 1 = %d"
               % (name, pl, lam1, nrm - 1))
            kinds[(name, pl[0])] = kinds.get((name, pl[0]), 0) + 1
    print("  lambda(P^1) == N(P) - 1 at every place of both universes:")
    for k in sorted(kinds):
        print("    %-5s %-6s %4d places" % (k[0], k[1], kinds[k]))

    # (b) the covered direction: a fresh place has door 1 exactly when
    #     N(P) - 1 does NOT divide L. Sampled over states an actual walk
    #     reaches, not over invented invariants.
    #     WHAT THIS IS AND IS NOT. Given (a), it is a TAUTOLOGY of door_r's
    #     definition -- door_r's first test is exactly `L % lam_P(pl, 1) == 0`
    #     -- so it certifies the two ENGINES are wired as the docstring reads
    #     them and certifies nothing about the arithmetic. It is kept for that
    #     and reported as that; the load-bearing measurements are S2 onward.
    samples = 0
    for name, M, _ in RINGS:
        st, L = {}, 1
        for _ in range(12):
            for pl in M.UNIVERSE[:60]:
                if st.get(pl, 0):
                    continue
                r = M.door_r(pl, 0, L)
                free = (L % (M.place_norm(pl) - 1) != 0)
                ok((r == 1) == free,
                   "%s: %s has door %d with N-1 | L = %s"
                   % (name, pl, r, not free))
                samples += 1
            cost, (pl, r) = step_once(M, st, L)
            st = apply_move(st, pl, r)
            L = M.lam_state(st)
    print("  door 1 <=> (N(P) - 1) does not divide L: %d (state, place) "
          "samples, 0 off" % samples)
    print("       (a wiring check on the engines, not evidence: given the "
          "line above it is\n        a tautology of door_r's own first test.)")

    # (c) the engines still lock where the filed census says they do.
    locks = 0
    for name, M, blurb in RINGS:
        got = walk_to_lock(M, {})
        ok(got is not None, "%s: the void seed no longer locks" % name)
        st, L, pl, cost, steps = got
        locks += 1
        print("  %-4s void seed locks on %-6s at cost %-4d after %d moves"
              % (name, show_place(M, pl), cost, steps))
    ok(locks == 2, "the control did not lock in both rings")


# --------------------------------------------- S2 the recurrent price (PR1)
def tail_costs(M, st, L, n):
    """The cost, place, door and TIE MULTIPLICITY of each of the next n moves,
    the walk continuing greedily. The multiplicity is carried so that a tail
    can be certified tie-free: a lock is a single recurrent vehicle, and a
    tail with a tie in it is a branch point this walk silently took one side
    of, which would make a flat cost sequence one branch's rather than the
    lock's."""
    out = []
    s, l = dict(st), L
    for _ in range(n):
        cost, ties = M.ideal_menu(s, l)
        pl, r = ties[0]
        out.append((cost, pl, r, len(ties)))
        s = apply_move(s, pl, r)
        l = M.lam_state(s)
    return out, s, l


def locking_seeds(M):
    """(seed, lock data) for every generator-product seed that locks."""
    out = []
    for nrm, m in M.gen_products(SEED_CAP):
        seed = dict(m)
        got = walk_to_lock(M, seed)
        if got is not None:
            out.append((seed, got))
    got = walk_to_lock(M, {})
    if got is not None:
        out.insert(0, ({}, got))
    return out


def s2_recurrent_price(store):
    section("S2  PR1 -- THE RECURRENT PRICE, over every locking seed of the "
            "norm-%d belts" % SEED_CAP)
    for name, M, blurb in RINGS:
        seeds = locking_seeds(M)
        store[name] = {"M": M, "seeds": seeds}
        worst_ratio, worst_tag = Fraction(0), None
        allcosts, nonflat, tied, deep_doors = {}, 0, 0, {}
        for seed, (st, L, pl, cost, steps) in seeds:
            costs, _, _ = tail_costs(M, st, L, TAIL_N)
            cs = [c for c, _, _, _ in costs]
            settled = cs[TAIL_SETTLE:]
            ok(len(set(settled)) >= 1, "%s: an empty tail" % name)
            if len(set(settled)) != 1:
                nonflat += 1
            if any(m > 1 for _, _, _, m in costs):
                tied += 1
            ratio = Fraction(cs[-1], cs[0])
            if ratio > worst_ratio:
                worst_ratio, worst_tag = ratio, show_state(M, seed)
            for c in set(settled):
                allcosts[c] = allcosts.get(c, 0) + 1
            # THE SETTLED DOOR of the recurrent vehicle, which F1's exception
            # is about: it is 1 wherever lambda pumps on a - 1 and a constant
            # 2 at the ramified shape, which pumps on a//2. Keyed by (door,
            # place) so the exception names itself rather than being inferred
            # from two prints read against each other.
            d_last = costs[-1][2]
            k = (d_last, show_place(M, costs[-1][1]), cs[-1])
            deep_doors[k] = deep_doors.get(k, 0) + 1
            ok(max(settled) <= cost,
               "%s: seed %s has a tail cost %d above its lock cost %d"
               % (name, show_state(M, seed), max(settled), cost))
        print("  %-4s %-32s %3d locking seeds" % (name, blurb, len(seeds)))
        print("       tails not flat past move %d: %d; tails with a tie in "
              "them: %d" % (TAIL_SETTLE, nonflat, tied))
        print("       distinct settled tail costs: %s"
              % ", ".join("%d (x%d)" % (c, n)
                          for c, n in sorted(allcosts.items())))
        print("       settled vehicle doors (door, place, cost) x seeds: %s"
              % ", ".join("(%d, %s, %d) x%d" % (k[0], k[1], k[2], n)
                          for k, n in sorted(deep_doors.items())))
        print("       max (last tail cost)/(first): %s   at seed %s"
              % (worst_ratio, worst_tag))
        ok(nonflat == 0,
           "%s: %d seeds have a non-flat recurrent tail" % (name, nonflat))
        ok(tied == 0,
           "%s: %d recurrent tails carry a tie, so their flatness is one "
           "branch's and not the lock's" % (name, tied))
        store[name]["tail_costs"] = sorted(allcosts)


# ------------------------------------------- S3 the lock's universe (PR2-4)
def s3_lock_universe(store):
    section("S3  PR2-PR4 -- WHAT THE LOCK DECLINES: uncovered places, small "
            "places, and the universe cap")
    for name, M, blurb in RINGS:
        seeds = store[name]["seeds"]
        max_cost, max_lu, worst_small, deepest = 0, 0, 0, None
        rows, veh_free = [], 0
        for seed, (st, L, pl, cost, steps) in seeds:
            scan = scan_universe(M, st, L)
            unc = [t for t in scan if t[1] == 1]
            ok(unc, "%s: seed %s locks with no door-1 place at all"
               % (name, show_state(M, seed)))
            # PR2 AS FROZEN reads "the least-norm uncovered place costs more
            # than the lock cost", and it MISSES: the least-norm uncovered
            # place is the RECURRENT one itself, at exactly the lock cost.
            # That is the mechanism rather than a nuisance -- the vehicle's
            # own door stays 1 forever, which is what pins the price flat --
            # so the frozen check is recorded as a miss and the observable is
            # re-read over the FRESH places, the escapes the lock declines.
            if M.door_r(pl, st.get(pl, 0), L) == 1:
                veh_free += 1
            fresh_unc = [t for t in unc if not st.get(t[3], 0)]
            ok(fresh_unc, "%s: seed %s locks with no fresh door-1 place"
               % (name, show_state(M, seed)))
            least_unc = min(t[0] for t in fresh_unc)
            below = [t for t in scan if t[0] < cost]
            bad = [t for t in below if t[1] == 1]
            ok(not bad,
               "%s: seed %s has a door-1 place of norm %s below its lock "
               "cost %d" % (name, show_state(M, seed),
                            [t[0] for t in bad], cost))
            ok(least_unc > cost,
               "%s: seed %s declines a fresh uncovered place of norm %d at "
               "lock cost %d" % (name, show_state(M, seed), least_unc, cost))
            max_cost = max(max_cost, cost)
            max_lu = max(max_lu, least_unc)
            worst_small = max(worst_small, len(below))
            rows.append((cost, least_unc, len(below), len(fresh_unc),
                         show_place(M, pl), show_state(M, seed)))
            if deepest is None or len(below) > deepest[2]:
                deepest = (st, L, len(below), seed, cost)
        store[name]["deepest"] = deepest
        rows.sort()
        print("  %-4s %-32s   MAXP = %d" % (name, blurb, M.MAXP))
        print("       the recurrent vehicle's own door is 1 at %d of %d locks"
              % (veh_free, len(seeds)))
        print("       %-6s %-9s %-8s %-9s %-7s %s"
              % ("cost", "least-fu", "N<cost", "n-fresh-u", "vehicle",
                 "seed"))
        seen = set()
        for r in rows:
            k = (r[0], r[1], r[2], r[4])
            if k in seen:
                continue
            seen.add(k)
            print("       %-6d %-9d %-8d %-9d %-7s %s" % r)
        # THE PRINTED TABLE ABOVE IS DEDUPED, so no range may be read off it:
        # its key omits the fresh-uncovered COUNT, and two seeds sharing a key
        # print once. Every range quoted anywhere comes from these lines,
        # which run over all seeds.
        fu = [r[3] for r in rows]
        nb = [r[2] for r in rows]
        lu = [r[1] for r in rows]
        cs = [r[0] for r in rows]
        print("       over ALL %d seeds (not the deduped table): lock cost "
              "%d..%d, least fresh-uncovered norm %d..%d," % (len(rows),
              min(cs), max(cs), min(lu), max(lu)))
        print("       fresh-uncovered places %d..%d of a %d-place universe, "
              "places below the lock cost %d..%d"
              % (min(fu), max(fu), len(M.UNIVERSE), min(nb), max(nb)))
        print("       max lock cost %d and max least-uncovered norm %d, "
              "against MAXP %d" % (max_cost, max_lu, M.MAXP))
        print("       largest count of places below a lock cost: %d"
              % worst_small)
        ok(max_cost * 2 < M.MAXP,
           "%s: lock costs reach %d against MAXP %d" % (name, max_cost, M.MAXP))
        ok(max_lu * 2 < M.MAXP,
           "%s: least-uncovered norms reach %d against MAXP %d"
           % (name, max_lu, M.MAXP))


# ---------------------------------------------- S4 the coverage density (PR5)
def s4_density(store):
    section("S4  PR5 -- THE COVERAGE DENSITY AT A LOCK, by norm band")
    for name, M, blurb in RINGS:
        st, L, nbelow, seed, cost = store[name]["deepest"]
        scan = scan_universe(M, st, L)
        bands = [(1, 10), (10, 100), (100, 500), (500, 1000), (1000, 2000)]
        print("  %-4s at the lock of seed %s (cost %d), universe %d places"
              % (name, show_state(M, seed) or "(1)", cost, len(scan)))
        print("       %-14s %-8s %-8s %s" % ("norm band", "places", "covered",
                                             "fraction"))
        for lo, hi in bands:
            inb = [t for t in scan if lo <= t[0] < hi]
            if not inb:
                continue
            cov = sum(1 for t in inb if t[1] > 1)
            print("       [%5d,%5d) %-8d %-8d %.3f"
                  % (lo, hi, len(inb), cov, float(cov) / len(inb)))
        cov = sum(1 for t in scan if t[1] > 1)
        print("       whole universe: %d of %d covered (%.3f), and the ladder "
              "is stopped anyway" % (cov, len(scan), float(cov) / len(scan)))
        store[name]["cov_frac"] = (cov, len(scan))


# ------------------------------------------------------------ S5 the A/B (PR6)
def s5_ab(store):
    section("S5  PR6 -- DOES THE BUDGET GROW? the schedule's walk against a "
            "ring's recurrent tail")
    sch = PS.Sched("alpha=1,b=2,m=1", alpha=1, b=2, m=1)
    sch.check_monotone(60)
    npl = dict((d, 2) for d in range(1, PS.DEG_CAP + 1))
    w = PS.Walk(npl, sch, "AB", dcap=PS.DEG_CAP)
    mins = []
    for _ in range(SCHED_N):
        best, ties = w.menu()
        mins.append(best)
        w.apply(sorted(ties)[0])
    print("  the abstract schedule, alpha = 1, b = 2, two items at every "
          "degree to %d:" % PS.DEG_CAP)
    print("       menu minimum by move: %s ..." % mins[:12])
    print("       ... %s" % mins[-6:])
    print("       last/first = %s, tick T = %d" % (Fraction(mins[-1], mins[0]),
                                                   w.T))
    ok(mins[-1] > mins[0] * 4,
       "the schedule's menu minimum did not grow: %d -> %d"
       % (mins[0], mins[-1]))
    for name, M, blurb in RINGS:
        st, L, pl, cost, steps = store[name]["seeds"][0][1]
        costs, _, _ = tail_costs(M, st, L, SCHED_N)
        cs = [c for c, _, _, _ in costs]
        print("  %-4s recurrent tail from the void seed's lock:" % name)
        print("       move cost by move: %s ..." % cs[:12])
        print("       ... %s" % cs[-6:])
        print("       last/first = %s" % Fraction(cs[-1], cs[0]))
        ok(cs[-1] == cs[-2] == cs[TAIL_SETTLE],
           "%s: the recurrent tail is not flat" % name)


# ------------------------------------------- S6 the per-class clock (PR7)
class LocalWalk(object):
    """The abstract walker with the tick made PER CLASS instead of global --
    the one ingredient the schedule family has never carried, and the shape
    a number ring's door has (its staleness reads the p-part of the seated
    set's invariant, and different rational primes are unrelated).

    Deliberately independent of PS.Walk rather than a subclass: that walker
    asserts the global-clock invariants at every move, and those are exactly
    what a local clock is meant to break. Everything else -- the price, the
    door, the fresh discount, the covered test -- is copied from it.

    An item is (degree, slot); cls(item) names its clock. One class for all
    items reproduces the global walker, which S6 checks against it."""

    def __init__(self, npl, sch, cls, dcap, exact=False, seed=()):
        self.npl = npl
        self.sch = sch
        self.cls = cls
        self.dcap = dcap
        self.exact = exact      # the tick advances to the new exponent itself
                                # rather than to ceil(b * T) -- which is what a
                                # ring's v_p(L) does, and is the second axis
                                # PR7 did not separate from locality
        self.seat = {}          # degree -> list of exponents
        self.opens = {}         # degree -> fresh discounts spent
        self.opened = []
        self.T = {}             # class -> tick
        self.step = 0
        # A SEED, the abstract counterpart of the rings' generator-product
        # seeds: items already seated at named degrees, their degrees' fresh
        # discount spent. Without one an exact-tick walk locks at its very
        # first move on the least degree, which is a true lock but too
        # degenerate to read a mechanism off.
        for d in seed:
            self.seat.setdefault(d, []).append(1)
            self.opens[d] = self.sch.m
            c = self.cls((d, len(self.seat[d]) - 1))
            self.T[c] = max(self.T.get(c, 1), 1)

    def tick(self, key):
        return self.T.get(self.cls(key), 1)

    def covered(self, d):
        return d in self.sch.born or self.opens.get(d, 0) >= self.sch.m

    def door(self, d, slot, e, kind):
        if kind == "open" and not self.covered(d):
            return 1
        return max(1, self.tick((d, slot)) + 1 - e)

    def menu(self):
        best, ties = None, []
        d = 0
        while d < self.dcap:
            d += 1
            if best is not None and self.sch.price(d, 1) > best:
                break
            if self.npl.get(d, 0) == 0:
                continue
            row = self.seat.get(d, [])
            cands = []
            if self.npl[d] > len(row):
                r = self.door(d, len(row), 0, "open")
                cands.append((self.sch.price(d, r), d, len(row), r, "open"))
            for i, e in enumerate(row):
                r = self.door(d, i, e, "move")
                cands.append((self.sch.price(d, r), d, i, r, "move"))
            for c in cands:
                if best is None or c[0] < best:
                    best, ties = c[0], [c]
                elif c[0] == best:
                    ties.append(c)
        return best, sorted(ties)

    def apply(self, mv):
        cost, d, slot, r, kind = mv
        if kind == "open":
            fresh = not self.covered(d)
            row = self.seat.setdefault(d, [])
            row.append(r)
            if fresh:
                if self.opens.get(d, 0) == 0:
                    self.opened.append(d)
                self.opens[d] = self.opens.get(d, 0) + 1
        else:
            self.seat[d][slot] += r
        e2 = self.seat[d][slot]
        c = self.cls((d, slot))
        t = self.T.get(c, 1)
        if self.exact:
            t = max(t, e2)
        else:
            while t < e2:
                t = self.sch.tick_up(t)
        self.T[c] = t
        self.step += 1
        return cost, d, slot, r, kind

    def least_uncovered(self):
        for d in range(1, self.dcap + 1):
            if self.npl.get(d, 0) and not self.covered(d):
                return d
        return None


GRID_N = 120         # moves of each cell of the clock grid


def s6_local_clock():
    section("S6  PR7 -- WHICH INGREDIENT OF THE RING'S CLOCK STOPS A LADDER: "
            "locality against exactness")
    print("  PR7 AS FROZEN predicted that making the tick PER ITEM stops the")
    print("  ladder. Measured over %d moves it does not -- it slows it. So the"
          % GRID_N)
    print("  axis is separated from the one PR7 confounded it with: whether")
    print("  the tick GROWS past the exponent it is answering (ceil(b*T), the")
    print("  schedule's) or lands exactly on it (max(T, e), a ring's v_p(L)).")
    sch = PS.Sched("alpha=1,b=2,m=1", alpha=1, b=2, m=1)
    # LocalWalk inherits PS.Walk's scan economy -- the menu stops at the first
    # degree whose door-1 price already beats the best found -- so it inherits
    # the obligation too: price(d, 1) must be non-decreasing over the whole
    # degree range this walker scans, or every menu here is a truncation.
    sch.check_monotone(400)
    npl = dict((d, 2) for d in range(1, 400 + 1))
    grid = [("global", "doubling", lambda k: 0, False),
            ("global", "exact", lambda k: 0, True),
            ("per item", "doubling", lambda k: k, False),
            ("per item", "exact", lambda k: k, True)]
    SEED = (9, 13)       # two items pre-seated, so every cell has a wander
    out = {}
    print("\n  seed: items already seated at degrees %s, over a supply of two"
          % (SEED,))
    print("  items at every degree to 400 -- a supply that never runs out.")
    print("\n  'seated' counts DISTINCT DEGREES carrying a seat, which is what")
    print("  compares to a ring's places; the schedule's own 'opened' counts")
    print("  only fresh discounts spent, and degree 1 is born covered, so an")
    print("  exact-tick walk that seats degree 1 and stops reads 0 there.")
    print("\n  %-9s %-9s %-7s %-7s %-14s %-9s %s"
          % ("clock", "tick", "seated", "opened", "last mins", "least unc",
             "ladder"))
    for ctag, ttag, cls, exact in grid:
        w = LocalWalk(npl, sch, cls, dcap=400, exact=exact, seed=SEED)
        mins = []
        for _ in range(GRID_N):
            best, ties = w.menu()
            mins.append(best)
            w.apply(ties[0])
        lu = w.least_uncovered()
        flat = len(set(mins[GRID_N // 2:])) == 1
        # THE LIMIT'S SHAPE at the new dial, which the four-ingredient sweep
        # could not reach: how many items stand above exponent 1. The filed
        # limit theorem is ONE deep coordinate over a support flat forever,
        # and whether that survives an exact tick is the question the corner
        # opens. Read here because the state is already in hand.
        deep = [(d, i, e) for d, row in w.seat.items()
                for i, e in enumerate(row) if e > 1]
        out[(ctag, ttag)] = (len(w.seat), mins, lu, flat, len(w.opened), deep)
        print("  %-9s %-9s %-7d %-7d %-14s %-9s %-9s above-1: %d %s"
              % (ctag, ttag, len(w.seat), len(w.opened), mins[-3:], lu,
                 "STOPPED" if flat else "climbing", len(deep),
                 "(deg %d at exp %d)" % (deep[0][0], deep[0][2])
                 if len(deep) == 1 else ""))
    # The two exact cells must stop and the two doubling cells must not --
    # which puts the ingredient on the tick's GROWTH and not on its locality.
    for ctag in ("global", "per item"):
        ok(out[(ctag, "exact")][3],
           "the %s exact-tick ladder did not stop: %s"
           % (ctag, out[(ctag, "exact")][1][-8:]))
        ok(not out[(ctag, "doubling")][3],
           "the %s doubling-tick ladder stopped" % ctag)
        ok(out[(ctag, "exact")][2] is not None,
           "the %s exact-tick walk left no uncovered degree" % ctag)
        ok(out[(ctag, "exact")][0] < out[(ctag, "doubling")][0],
           "the %s exact tick seated no fewer degrees than the doubling one"
           % ctag)
        ok(out[(ctag, "exact")][0] > len(SEED),
           "the %s exact-tick walk seated nothing new at all" % ctag)
        # THE FILED LIMIT SHAPE -- one item above exponent 1, every other
        # seated item flat forever -- survives the EXACT tick under both
        # clocks, which is what the four-ingredient sweep could not reach.
        ok(len(out[(ctag, "exact")][5]) == 1,
           "the %s exact-tick walk has %d items above exponent 1, not 1: %s"
           % (ctag, len(out[(ctag, "exact")][5]), out[(ctag, "exact")][5]))
    # AND THE OTHER AXIS IS WHERE THE LIMIT SHAPE ACTUALLY BREAKS: a per-item
    # tick that GROWS gives every item its own runaway clock, so the support
    # is not flat at all. The two axes therefore decide DIFFERENT things --
    # exactness the ladder's fate, locality the limit's shape.
    ok(len(out[("global", "doubling")][5]) == 1,
       "the global doubling walk does not reproduce the filed limit shape: %s"
       % (out[("global", "doubling")][5],))
    ok(len(out[("per item", "doubling")][5]) > 1,
       "the per-item doubling walk kept a flat support: %s"
       % (out[("per item", "doubling")][5],))
    ge, pe = out[("global", "exact")], out[("per item", "exact")]
    print("\n  Both EXACT cells seat one degree past the seed and then stop,")
    print("  with degree %s / %s still uncovered and door-1 on a supply that"
          % (ge[2], pe[2]))
    print("  never runs out -- a stop on PRICE, not on silence. Both DOUBLING")
    print("  cells are still climbing at move %d. Locality changes how FAST a"
          % GRID_N)
    print("  ladder climbs; what decides whether it climbs AT ALL is whether")
    print("  the tick overshoots the exponent it is answering. A ring's does")
    print("  not, so a ring's cheapest move never gets dearer.")


DEPTH_N = 24         # depths at which a lone place's door is read
RAM_SETTLE = 5       # depths a ramified door takes to reach its period


def s7_tick_shape():
    section("S7  WHERE THE EXACT TICK COMES FROM: lambda's p-part, linear "
            "against logarithmic in the depth")
    print("  DERIVED AFTER THE RUN, not predicted at the freeze, and checked")
    print("  here rather than argued. The slate asked which side of a")
    print("  contradiction was wrong; this asks why the two worlds sit on")
    print("  opposite sides of the axis the answer turned out to be about.")
    print("  A lone place deepening with nothing else seated, its door read")
    print("  at each depth -- the door IS the staleness, so its growth IS the")
    print("  tick's.\n")

    # THE NUMBER RING: lambda(P^a) = (p - 1) * p^(a - 1), so v_p is a - 1,
    # LINEAR in the depth. Read off the engines, not re-implemented.
    for name, M, _ in RINGS:
        # THE CLEAN LINEAR SHAPE is a split place over an ODD prime, where
        # lambda(P^a) = (p-1)*p^(a-1) exactly. The p = 2 places carry a small
        # table anomaly (lam(2) = lam(3) at K23's split 2), so they are shown
        # separately rather than folded into the claim.
        # INERT is the third kind and pumps (p^2-1)*p^(a-1) -- linear in the
        # depth exactly as the odd split shape is, so its door must be 1 at
        # every depth too. Probed rather than assumed: "both rings' place
        # kinds" is a claim about all three.
        for tag, sel in (("split, p odd",
                          lambda p: p[0] == 'split' and p[1] % 2),
                         ("inert",
                          lambda p: p[0] == 'inert'),
                         ("split, p = 2",
                          lambda p: p[0] == 'split' and p[1] == 2)):
            pl = next((p for p in M.UNIVERSE if sel(p)), None)
            if pl is None:
                continue
            doors = [M.door_r(pl, e, M.lam_P(pl, e))
                     for e in range(1, DEPTH_N + 1)]
            if pl[1] % 2:
                ok(set(doors) == {1},
                   "%s: a lone %s place's door is not 1 at every "
                   "depth: %s" % (name, tag, doors))
            else:
                ok(set(doors[RAM_SETTLE:]) == {1},
                   "%s: a lone split-2 place's door does not settle at 1: %s"
                   % (name, doors))
            print("  %-4s %-12s %-6s door by depth 1..%d: %s"
                  % (name, tag, show_place(M, pl), DEPTH_N,
                     "".join(str(x) for x in doors)))
        # THE RAMIFIED SHAPES pump on a//2, so their door does not settle at
        # 1 but ALTERNATES -- eventually periodic and bounded, never growing,
        # which is the property that matters. (Isolated here, one place with
        # nothing else seated; at a measured lock the other seated places'
        # lambda pins the same door at a constant 2, which is what the S2
        # settled-door census prints.)
        for rm in [p for p in M.UNIVERSE if p[0] == 'ram']:
            rd = [M.door_r(rm, e, M.lam_P(rm, e))
                  for e in range(1, DEPTH_N + 1)]
            tail = rd[RAM_SETTLE:]
            ok(max(tail) <= 2,
               "%s: the ramified door past depth %d exceeds 2: %s"
               % (name, RAM_SETTLE, rd))
            ok(tail == tail[:2] * (len(tail) // 2) + tail[:len(tail) % 2],
               "%s: the ramified door tail is not 2-periodic: %s"
               % (name, tail))
            print("  %-4s %-10s door by depth 1..%d: %s   (2-periodic past "
                  "depth %d, never growing)"
                  % (name, show_place(M, rm), DEPTH_N,
                     "".join(str(x) for x in rd), RAM_SETTLE))

    # THE FUNCTION FIELD: lambda(P^a) = lcm(2^d - 1, 2^ceil_log2(a)), so v_2
    # is ceil_log2(a), LOGARITHMIC in the depth. The engine's own pump, on a
    # Ring carrying one synthetic place of each degree read.
    R = EC.Ring("tick-shape probe", 1)
    for d in (1, 2, 3):
        key = ("probe", d)
        R.deg[key] = d
        doors = []
        for e in range(1, DEPTH_N + 1):
            L = R.lam_pp(d, e)
            doors.append(R.door_r(key, e, L))
        ok(doors[-1] > doors[3],
           "F_2[x] degree %d: the door does not grow with the depth: %s"
           % (d, doors))
        # A door of r at depth e lands at e + r, and the pump's shape puts
        # that at (the tick) + 1 with the tick 2^ceil_log2(e) -- which is
        # exactly the schedule walker's own law, `e2 == Tb + 1` with the tick
        # DOUBLING (explore_price_schedule.py apply, explore_greedy_limit.py).
        # So the function field is the doubling-tick corner by its lambda,
        # the way a number ring is the exact one by its lambda.
        for e in range(1, DEPTH_N + 1):
            tick = 1 << EC.ceil_log2(e)
            ok(e + doors[e - 1] == tick + 1,
               "F_2[x] degree %d at depth %d: door %d lands at %d, not at "
               "the tick %d plus one"
               % (d, e, doors[e - 1], e + doors[e - 1], tick))
        print("  FF   degree %-5d door by depth 1..%d: %s"
              % (d, DEPTH_N, ",".join(str(x) for x in doors)))
    print("\n  A number ring's lambda carries p^(a-1) -- v_p is LINEAR in the")
    print("  depth, so a deepening always clears its own valuation by one and")
    print("  the door returns to 1: an EXACT tick, a flat price, a lock.")
    print("  A function field's carries 2^ceil_log2(a) -- v_2 is LOGARITHMIC,")
    print("  so clearing it needs the depth to reach the next power of 2 and")
    print("  the door grows like the depth itself: a DOUBLING tick, a price")
    print("  that climbs, a sprawl. The lock/sprawl dichotomy and the")
    print("  exact/doubling axis are ONE fact, not two.")


def main():
    store = {}
    s1_control()
    s2_recurrent_price(store)
    s3_lock_universe(store)
    s4_density(store)
    s5_ab(store)
    s6_local_clock()
    s7_tick_shape()
    print("\nALL CHECKS PASS: %d" % CHECKS)


if __name__ == "__main__":
    main()
