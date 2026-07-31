"""explore_headed_image.py -- the four schedule laws all read a ladder's SUP
gap, and the head lives in the STATE. The corpus has exactly one register
that reads a state rather than counting it. Run it over a headed ladder.

THE QUESTION. explore_tick_pump.py derives four laws over a TICK LADDER --
the limit's shape, the degree ceiling, the stop law and the mixed universe's
min over products -- and explore_headed_ladder.py shows each of them is a
function of the ladder's SUP gap, the head being exactly what parts sup from
tail. But that file's F7 found the head is not thereby absent: strands sit at
ramp depths 3, 5 and 9 where a constant-gap ladder puts every one at depth 2,
while the strand POPULATIONS agree with the sup-gap control at 14 of 14. Same
count, different places. So the head is a STATE coordinate that every
counting law is blind to.

The corpus has one register that reads a state: the IMAGE
(explore_tick_pump.py S4/F7), which enumerates the distinct limit READINGS
live at a move budget and finds the constant-gap ladders' sets stop MOVING by
budget 8. It has never been run over a headed ladder -- explore_tick_pump.py
F8 (ii) files it open. This rig runs it there, against both of each headed
ladder's constant-gap controls: the ladder of its SUP, which shares its
longest run, and the ladder of its TAIL, which shares its recurrent price.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. "The gap",
"bounded gap" and "settles" are the CONSTANT family's words, where sup, tail
and the recurrent multiplier are one number; every prediction below names
which of the two it means or it is not written. "Settles" is the image's own
word and means the reading set stops MOVING, never that it stops growing --
a set still moving at the last budget is no image at all.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 From the global clock to the per-item one. explore_tick_pump.py S4 runs
    the image at a GLOBAL clock only, and the head is a per-item phenomenon
    (explore_headed_ladder.py F6: under a global clock exactly one coordinate
    stands above exponent 1 at every headed ladder, as at every headless
    one). So the
    per-item cells are a new parameter value for the CONSTANT-GAP ladders
    too. Their figures are not in the corpus and none is inherited here.
 T2 From the global clock to the per-item one again, at the reading function.
    `reading` forgets the exponent of the item named by the last clock move.
    Under a global clock there is one clock and that item is the runaway.
    Under a per-item clock the last clock mover is the runaway only once the
    walk has locked, and S1c checks that rather than assuming it.
 T3 The widths are IMPORTED as shape from explore_headed_ladder.py's dialled
    set. No local field is re-measured here.

THE HAND-ATTACK, on paper before any engine code.

 A. WHAT A READING IS UNDER A GLOBAL CLOCK. If explore_headed_ladder.py F6
    holds at this walk -- exactly one coordinate above exponent 1 -- and
    `reading` forgets exactly that one, then every other seated item sits at
    exponent 1 and a reading degenerates to the multiset of degrees seated
    plus which degree hosts the sentinel. The global image would then be a
    count of reachable SEATING PROFILES carrying no exponent information at
    all. F6 is measured at 120 moves from a seeded state and this walk runs
    12 from the void, so the count above exponent 1 is PRINTED here rather
    than assumed, and A is conditional on it.

 B. AND THE RAMP STILL REACHES THAT COUNT, THROUGH THE PRICES. price(d, r) is
    d * r. From the void the menu ties at 2 -- degree 1 opens at door 2,
    being born and so carrying no fresh discount, against degree 2 opening at
    door 1. Seat exponent 2 and the global tick becomes next_at(2): 2 on
    Z[i]'s ladder 1, 2, 7, 9, ... but 6 on its sup-gap control 1, 6, 11, ...
    So the headed ladder hands the deep item a door of 1, a price of 1 at
    degree 1, where the control hands it a door of 5. The ramp is a stretch
    of CHEAP deep moves the control does not have, and a cheap deep move
    competes with an opening for the same budget. So a head can reach the
    profile count without ever putting a second coordinate above exponent 1.

 C. UNDER A PER-ITEM CLOCK THE READING IS NOT DEGENERATE, AND THE MEMBERS
    MUST PART. A strand keeps its own exponent -- the reading forgets one
    coordinate and only one -- and explore_headed_ladder.py F7 puts headed
    strands at depths 3, 5 and 9 against the constant ladder's 2. A reading
    carrying an exponent of 3 is one no depth-2 ladder can produce. So the
    MEMBER sets part by construction; what is open is the SIZE.

DISTRUST THE MARGIN. The derived half is A and C -- bookkeeping on the
reading function and on a filed strand census. The VIBES half is B: one
ladder, one supply, one schedule, and the claim that a cheap ramp move
changes which profiles are REACHABLE is arithmetic that has not been run.
PR2 rests on it and is the one to distrust, which is why it names a printed
column and not a mechanism.

PREDICTIONS, fixed before any engine code, each naming what the rig PRINTS.
What they mean is weighed after the run.

PR1 SETTLING UNDER A GLOBAL CLOCK. Every headed ladder is bounded-gap, its
    sup being e + w, so its reading set stops MOVING by budget 12 at both
    supplies exactly as all four constant-gap ladders do. What the rig
    PRINTS: per (ladder, supply) the reading counts live at budgets 4, 6, 8,
    10 and 12, and SETTLED or moving by SET equality of the last two.
    KILL: a headed ladder whose set still moves between the last two budgets.

PR2 SIZE UNDER A GLOBAL CLOCK. The settled size AGREES with the SUP control's
    at every headed ladder and both supplies -- explore_headed_ladder.py F1,
    F3 and F6 all read the sup and nothing else, and the image is one more
    count. What the rig PRINTS: per headed ladder the settled size beside
    both controls' sizes, sup and tail, with the agreement column.
    KILL: any disagreement with the sup control -- the head entering a
    register the four counting laws cannot see.

PR3 MEMBERS UNDER A GLOBAL CLOCK. Stronger than PR2 and separately
    falsifiable: the settled SET equals the sup control's set and not merely
    its size. What the rig PRINTS: set equality, and where unequal the
    members held by one and not the other.
    KILL: equal sizes with unequal members -- the sup deciding the count
    while the ramp decides the content, which is a different claim from
    either PR2 verdict.

PR4 MEMBERS UNDER A PER-ITEM CLOCK. The headed set differs from the sup
    control's, by hand-attack C. What the rig PRINTS: per (ladder, supply)
    set equality, and the depths the strands actually stand at in the final
    budget's states.
    KILL: identical sets at a ladder whose strands are not at depth 2, which
    would mean the reading is not reading the state it is documented to read.

PR5 SETTLING AND SIZE UNDER A PER-ITEM CLOCK. No size is frozen: the
    constant-gap per-item figures are not in the corpus (T1) and there is no
    prior for them. For settling the observable is comparative -- if the
    constant-gap ladders settle and a headed ladder of the same sup does not,
    that is the head breaking the settling law. What the rig PRINTS: the same
    columns as PR1 at budgets 8, 12, 16, 20 and 24.
    KILL: none frozen. WHICH ladders settle is the observable.

THE POSITIVE CONTROL (S1, run before any verdict is read). Three instruments,
each against something this rig did not write.
  - THE FIGURES (S1a). `image_at` is IMPORTED, never re-implemented, and must
    reproduce explore_tick_pump.py F7 verbatim at its four constant-gap
    ladders under a global clock: settled sizes 3, 6, 4 and 4 over F_2[x] and
    1, 1, 1 and 2 over h5, with orbit sums 5, 28, 90 and 12396 over F_2[x].
  - THE LADDERS (S1b). psi(p = 2, e = 1) must BE the family's exact ladder
    and psi(p = 5, e = 2) its gap-2 ladder, member for member. This rig
    builds its own pumps, so the generator is certified here and not
    inherited.
  - THE READING FUNCTION (S1c), which is T2 discharged. Two checks. First,
    the item a reading forgets must be seated ABOVE exponent 1 at every live
    state at every budget -- derivable, since a clock rises only when the
    landing exponent exceeds the tick and the tick is a ladder member, so a
    recorded clock move carries an exponent above 1; it is checked because it
    is the premise the whole reading rests on. Second, under a per-item clock
    the last clock mover must be the RUNAWAY: each final-budget state is
    continued a further stretch under a deterministic least-cost rule, and
    the only item whose clock moves in that stretch must be the one the
    reading forgot.

THE INSTRUMENTS. `image_at`, `reading`, the walker, both constant-gap pumps
and the two supplies come from explore_tick_pump.py; the psi generator and
the dialled width set from explore_headed_ladder.py. This rig adds one
enumerator of its own, `live_at`, which carries the STATES the image only
counts -- certified against `image_at`'s own counts at every cell, so a
divergence in the enumeration is caught rather than reported as a finding.

THE REPAIRED READING, and it is here because S1c FIRED. The control above is
not decoration: run as first written, this rig stopped in S1c, and the
per-item half could not be read at all until the reading function was
rebuilt. The design is recorded here; what the failure MEANS is weighed in
the findings and not in this paragraph.

`reading` identifies the coordinate a limit forgets as the LAST CLOCK MOVER,
an identification it inherited from explore_schedule_image.py's `deep`, whose
walker has a single scalar clock.
Under a global clock that is sound for a reason the function does not state:
a clock rises only when the landing exponent exceeds the tick, so a clock
mover is always seated above exponent 1, and under a global clock exactly one
coordinate ever is (explore_tick_pump.py F5). The identification is therefore
a COROLLARY of one of the four laws, and that law is a global-clock law. So
the repair identifies the forgotten coordinate by what it actually is -- the
item that keeps moving -- rather than by what last moved:

    recurrent(w): continue the walk 2R moves under a deterministic
    least-cost rule and take the items whose clock moves in the SECOND half.
    The set read over the last QUARTER must equal it, or the state has not
    locked and carries no limit reading at all; such states are excluded and
    counted, never read.

    reading_locked(w): the shape with EVERY recurrent coordinate's exponent
    forgotten -- the plural the global-clock function had no need of.

TWO PROPERTIES THE REPAIR OWES, both checked in S1c rather than assumed.
 (i) It must AGREE with the imported `reading` wherever the imported one is
     sound -- at a global clock, every live state, both supplies, every
     ladder. A repair that changed the settled global figures would be a
     different instrument and not a repair.
 (ii) The reading it returns must not depend on which minimal-cost tie the
     continuation happens to break. The continuation is run a second time
     taking the LAST tie rather than the first, and the two READINGS must
     agree -- readings and not runaway identities, since two slots of one
     degree are interchangeable in a reading and need not be in a walk.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 THE IMAGE'S READING FUNCTION CARRIES AN UNSTATED PREMISE, AND THE PREMISE
   IS ONE OF THE FOUR LAWS (rule in range; 46571 live states over 11 ladders
   x 2 supplies x 2 clocks). `reading` identifies the coordinate a limit
   forgets as the LAST CLOCK MOVER, and documents it as "the deep
   coordinate". That identification is the recurrent item at 557 of 557
   global-clock states and at 2089 of 45709 per-item ones -- 4.6%. The reason
   it is sound at a global clock is derivable and the function does not state
   it: a clock rises only where the landing exponent exceeds the tick and the
   tick is always a ladder member, so a clock mover is always seated above
   exponent 1 (checked at 46571 of 46571 states); and under a global clock
   exactly one coordinate is recurrent (557 of 557). So the identification is
   a COROLLARY of explore_tick_pump.py F5, which is a global-clock law, and
   the register inherited it into a function whose name and docstring carry
   no clock at all. The image was not merely unrun at a per-item clock, which
   is what explore_tick_pump.py F8 (ii) files: it would have returned the
   wrong reading at 95% of the states if it had been run there.

F2 AND REPAIRING THE IDENTIFICATION IS NOT ENOUGH, BECAUSE A PER-ITEM STATE
   MOSTLY HAS NO LIMIT TO READ (rule in range; the two extreme tie
   continuations compared at 45709 per-item states). Rebuilt to forget what
   the walk actually carries to infinity, the reading reproduces the imported
   one at 557 of 557 global-clock states -- so it is a repair and not a
   different instrument -- and is TIE-INDEPENDENT at only 5810 of 45709
   per-item ones. A state whose reading moves with a tie still to be broken
   has no limit for any reading function to return: the branching the image
   enumerates at the FRONT continues behind the budget. So what fails at a
   per-item clock is the object and not the instrument, and the honest image
   there is taken over the DETERMINED states with the rest excluded and
   counted.

F3 AND THE HEAD IS WHAT MAKES A PER-ITEM LIMIT DETERMINED -- THE HEAD
   ENTERING THE STATE-READING REGISTER AS WELL-DEFINEDNESS AND NOT AS SIZE
   (rule in range; 14 headed cells against their 14 sup-gap constant
   controls, both supplies). At TWELVE of the fourteen headed cells EVERY
   final state carries a determined limit: 9 of 9, 8 of 8, 8 of 8, 8 of 8,
   6 of 6 and 37 of 37 over F_2[x], 10 of 10, 4 of 4, 16 of 16, 16 of 16,
   4 of 4 and 16 of 16 over h5. At the constant-gap controls that share their
   sup gap almost none does: 2 of 69, 2 of 60, 2 of 54, 2 of 48, 2 of 60 and
   3 of 81 over F_2[x], and 121 of 2048, 121 of 1771, 331 of 4641, 271 of
   3439, 121 of 1771 and 217 of 2465 over h5 -- 2.9% to 4.2% at the one
   supply and 5.9% to 8.8% at the other. That is six of the seven controls
   per supply; the SEVENTH is the gap-12 ladder, which carries 3 states and 2
   states in total and reads 100% of each, too few to be a rate at all.
   So the head does not give the image a different size; it gives the image a
   domain. The two headed exceptions are the widest ladder, (p2, e8, w4) at
   sup 12, whose walk has not locked at the budget at all (0 of 7 and 0 of 1)
   -- which is the stop law's own reading, a sup of 12 stopping at
   d_deep * 12 and so far past 24 moves.
   THE SHAPE OF THE MECHANISM, at OBSERVATION and not derived here: a
   constant ladder gives every item of a degree the same door forever, so an
   item ties with its siblings and which of them runs away is never settled
   by the state; a ramp hands the item that has climbed it a door the others
   cannot match, and a symmetry broken early stays broken. Why the tie
   survives specifically at a constant gap is not proved.

F4 AND THE HEAD PARTS FROM ITS SUP CONTROL AT A GLOBAL CLOCK TOO, WHICH IS
   THE FIRST READING IN THE FAMILY THE SUP GAP DOES NOT ACCOUNT FOR (rule in
   range; 14 headed cells, PR2 and PR3 both killed). explore_headed_ladder.py
   F1, F3 and F6 read the sup gap and nothing else at every one of the four
   laws. The image does not: the settled global size agrees with the sup
   control's at 10 of 14 and the settled SET agrees at 8 of 14. Two cells
   carry the sharpest form of it -- same size, different members: over
   F_2[x], (p2, e2, w2) and (p2, e2, w3) both settle at 4 readings where
   their gap-4 and gap-5 controls also settle at 4, and the headed readings
   carry a coordinate at exponent 3 where the controls carry 2, while seating
   one MORE degree at the same budget. That is read off ONE witness from each
   side -- the rig prints a single member held by the head and not the
   control and a single member held by the control and not the head -- so it
   is what SEPARATES the two sets and not a description of every member.
   It is hand-attack B's arithmetic
   arriving: the ramp hands the deep item a door of 1 where the control hands
   it the whole gap, and the moves that buys are spent both on depth and on
   openings.

F5 WHAT DOES NOT SETTLE IS THE SUP'S DOING AND NOT THE HEAD'S (rule in range;
   PR1's kill FIRED, at 3 of 14 cells: 11 of 14 headed cells settled by budget
   12 against 13 of 14 sup controls). The three that did not are the two widest
   ladders, sup 6 and sup 12, and at ONE of the two supplies the sup-12 CONTROL
   did
   not settle either -- at the other it did, so the control does not excuse
   the ladder everywhere, and what is common to all three misses is the
   ladder's own sup and nothing else. So a
   reading set stops moving on the same clock the walk stops on -- the stop
   sits at d_deep * sup (explore_headed_ladder.py F3), so a wide sup needs a
   budget past it and 12 moves is not one. The settling law is the constant
   family's, unscratched.

F6 AND HAND-ATTACK A'S PREMISE IS FALSE AT THIS WALK, WHICH IS WHY IT WAS
   PRINTED (observation; 14 global-clock cells). A predicted that a global
   reading degenerates to a seating profile, on explore_headed_ladder.py F6's
   one-coordinate law. Two coordinates stand above exponent 1 at five of the
   seven F_2[x] cells here -- the column is the greatest count over any state
   at any budget in the range, not a count at the final one. It is not a
   contradiction of that law -- exactly one of them is RECURRENT at 557 of 557
   states, the other being a strand --
   but a strand's exponent is KEPT by a reading, so a global reading carries
   exponent information after all, which is exactly what F4's two same-size
   cells are made of. F6 there is measured at 120 moves from a seeded state
   and this walk runs 12 from the void; the count above exponent 1 is a
   function of where in the walk it is read.

F7 WHAT IS LEFT OPEN. (Settled in part since: explore_image_domain.py
   answers (i), (ii) and (iii) -- the branching test empties the
   constant-gap domain of gap 2 or wider and confirms the headed cells
   exactly, the mechanism is derived from the door law, and the sup-12
   ladder locks between budgets 60 and 84 with zero ties found; (iv) and
   (v) stay open.) (0) PR4 is CONFIRMED and the confirmation is weak: the
   headed set differs from the sup control's at 14 of 14 cells, but the
   control's set is built from 2.9% to 8.8% of its own states, so two sets
   parting is nearly guaranteed by how few states one of them rests on. F3's
   determined counts are the informative reading and PR4's is not; the
   prediction asked the question the register could answer before the run and
   the run moved it. (i) Determinacy is measured by a NECESSARY condition --
   the first-tie and last-tie continuations agreeing -- so every determined
   count here is an UPPER bound and the constant controls' 2.9% is a ceiling
   rather than a figure. (ii) F3's mechanism is a shape and not a derivation.
   (iii) The sup-12 ladder is unread at both supplies: nothing in the budget
   reaches its lock, and the two cells that would test F3 at the widest head
   are empty. (iv) One schedule, one start (the void), two supplies, one
   degree cap; the seeded start every other cell of the family uses is not
   run here. (v) The image over a MIXED universe is still unrun --
   explore_tick_pump.py F8 (ii) asks for both and this file answers one.

RUN RECORD. One process, CPython, no BLAS. Wall 45.6 s, peak working set
121.1 MB against memwatch.py's 512 MB ceiling. 46609 checks here over 7
headed ladders and 4 constant-gap ones at two supplies and two clocks, with
the image, the reading, the walker, both constant pumps and both supplies
imported from explore_tick_pump.py and the psi generator and dialled width
set from explore_headed_ladder.py -- so their asserts fire underneath these.
The cost is set by the continuation the repaired reading runs per state.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_coarse_type as CT
import explore_greedy_limit as GL
import explore_headed_ladder as HL
import explore_price_schedule as PS
import explore_tick_pump as TP

CHECKS = 0

DCAP = 24                       # degrees the supply carries, the image's own
G_BUDGETS = (4, 6, 8, 10, 12)   # the global grid, explore_tick_pump.py S4's
P_BUDGETS = (8, 12, 16, 20, 24) # the per-item grid; 24 is the enumeration cap
LOCK_STEPS = 24                 # half the continuation the recurrent set reads
GAP_WINDOW = 256                # depths over which a ladder's sup gap is read


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ------------------------------------------------------------ the fixed parts
def sched():
    s = PS.Sched("alpha=1,b=2,m=1", alpha=1, b=2, m=1)
    s.check_monotone(TP.WALK_DCAP)
    return s


def supplies():
    """The two ring supplies the image is already read at, both function
    fields: the rational one, F_2[x], and the genus-one curve ring of class
    number 5, h5. Trimmed to the degrees the walker's cap can scan, as
    explore_tick_pump.py S4 trims them."""
    out = {}
    for L in CT.build_ladder():
        _, npl, _, _ = GL.universe(L)
        out[L.name] = dict((d, npl[d]) for d in range(1, len(npl)))
    return out


def sup_gap(pump, upto=GAP_WINDOW):
    """The greatest door an item ever faces, read off the ladder itself."""
    return max(pump.gap(e) for e in range(1, upto + 1))


def ladder_row(label, p, e, w):
    """A headed ladder with both of its constant-gap controls: the ladder of
    its SUP, which shares its longest run, and the ladder of its TAIL, which
    shares its recurrent price. Both numbers are read off the built ladder --
    nothing is taken from the label."""
    pump = HL.psi_ladder(label, p, e, w)
    steps, tail, over = HL.profile(pump)
    sup = sup_gap(pump)
    ok(sup - tail == w,
       "%s: sup gap %d less tail gap %d is not the width %d"
       % (label, sup, tail, w))
    ok(len(over) == 1,
       "%s: %d ladder steps above the tail, so this is not one head"
       % (label, len(over)))
    return (label, pump, sup, tail, TP.p_step(sup), TP.p_step(tail))


# ------------------------------------------------------- the state enumerator
def live_at(npl, sch, pump, cls, budget, dcap=DCAP):
    """Per budget, the STATES live at exactly that budget, branching on every
    minimal-cost tie -- the same enumeration explore_tick_pump.py's `image_at`
    runs, carried one level less far so the states themselves survive for the
    reading control and the strand census. Certified against `image_at`'s
    counts at every cell rather than trusted."""
    root = TP.PWalk(npl, sch, pump, cls, dcap)
    live = {root.key(): root}
    out = []
    for _ in range(budget):
        nxt = {}
        for s in live.values():
            _, ties = s.menu()
            for mv in ties:
                s2 = s.copy()
                s2.apply(mv)
                nxt.setdefault(s2.key(), s2)
        live = nxt
        out.append(dict(live))
    return out


def forgotten(w):
    """The (degree, slot) whose exponent the reading drops, or None where the
    state has no clock move yet and the reading is the bare shape."""
    if not w.clocks:
        return None
    _, d, slot, _, _ = w.clocks[-1]
    return (d, slot)


def recurrent(w, last=False):
    """The items whose clock moves in the SECOND HALF of a deterministic
    least-cost continuation -- what the walk carries to infinity, as against
    what last happened to move. None where the set read over the last QUARTER
    disagrees, which is a state that has not locked and so carries no limit
    reading at all.

    LOCKED means three things, and the image's own scope sentence needs all
    three -- a settled set is the limit set because the support never moves
    again. So: the recurrent set read over the second half must agree with
    the last quarter; the SUPPORT must not move in that stretch, no opening
    being taken; and every recurrent item must already be SEATED in w. The
    third is not pedantry -- a state two moves from the void has its eventual
    runaway at a degree it has not opened, and reading it as a limit records
    a coordinate the limit does not have and drops the one it does."""
    s = w.copy()
    marks, sizes = [], []
    for _ in range(2 * LOCK_STEPS):
        b = len(s.clocks)
        _, ties = s.menu()
        s.apply(ties[-1] if last else ties[0])
        marks.append(set((c[1], c[2]) for c in s.clocks[b:]))
        sizes.append(sum(len(r) for r in s.seat.values()))
    half = set().union(*marks[LOCK_STEPS:])
    qtr = set().union(*marks[LOCK_STEPS + LOCK_STEPS // 2:])
    if not half or half != qtr:
        return None
    if sizes[-1] != sizes[LOCK_STEPS - 1]:
        return None
    if any(len(w.seat.get(d, ())) <= i for d, i in half):
        return None
    return half


def reading_locked(w, last=False):
    """The shape with EVERY recurrent coordinate's exponent forgotten. None
    where the state has not locked."""
    r = recurrent(w, last)
    if r is None:
        return None
    out = {}
    for dd, row in w.seat.items():
        if not row:
            continue
        out[dd] = sorted(-1 if (dd, i) in r else e for i, e in enumerate(row))
    return tuple(sorted((dd, tuple(v)) for dd, v in out.items()))


def determined(w):
    """The state's limit reading where the state HAS one, else None. Both
    continuations must agree -- first minimal-cost tie and last -- because a
    state whose limit depends on a tie still to be broken is not a limit but
    a branch point, and the image enumerates branch points at the FRONT only.
    Agreement of the two extreme continuations is NECESSARY and not
    sufficient, so the states passing it are an UPPER bound on the determined
    ones and every count built on it is read as such."""
    a = reading_locked(w)
    if a is None or a != reading_locked(w, True):
        return None
    return a


def locked_image(states):
    """(the reading set over the states that HAVE a limit reading, how many
    did, how many did not). A state without one is excluded and counted,
    never read."""
    out, lk, un = set(), 0, 0
    for w in states.values():
        r = determined(w)
        if r is None:
            un += 1
        else:
            lk += 1
            out.add(r)
    return frozenset(out), lk, un


def image_rows(npl, sch, pump, cls, budgets):
    """(counts at the budgets, the set at the last, the set at the one before,
    orbit sums) from the imported instrument."""
    rows = dict((s, (r, t)) for s, r, t in
                TP.image_at(npl, sch, pump, cls, max(budgets), DCAP))
    return ([len(rows[b][0]) for b in budgets],
            rows[budgets[-1]][0], rows[budgets[-2]][0],
            [rows[b][1] for b in budgets])


def settled(last, prev):
    """SET equality and not count equality: two different sets of one size
    would read as settled on a count alone (explore_tick_pump.py S4). An EMPTY
    set is never settled: two empty sets are equal, so a cell where no state
    carries a limit reading at all would otherwise report the strongest
    verdict the column has on the weakest evidence there is."""
    return bool(last) and last == prev


def strand_depths(states, cls):
    """Over the live states, the exponents of the deep items a reading KEEPS
    -- every item above exponent 1 except the one forgotten. Under a global
    clock this is empty wherever the one-coordinate law holds, so it is the
    per-item register. Read off the RECURRENT set, so a state that has not
    locked contributes nothing rather than a mis-attributed exponent."""
    out = set()
    for w in states.values():
        r = recurrent(w)
        if r is None:
            continue
        for d, i, e in w.deep_items():
            if (d, i) not in r:
                out.add(e)
    return sorted(out)


# ----------------------------------------------------- S0 the forced failures
def s0_forced():
    section("S0  THE HARNESS FORCED TO FAIL")
    print("  Every check the run leans on, made to fail once.")
    bad = 0
    try:
        ladder_row("forced", 2, 3, 1)    # e = 3 is not (p-1)p^t, so no seat
    except AssertionError:
        bad += 1
    p = TP.p_step(3)
    try:
        ok(sup_gap(p) == 4, "forced: gap-3 sup read as 4")
    except AssertionError:
        bad += 1
    try:
        ok(settled(frozenset([1]), frozenset([2])),
           "forced: two different sets read as settled")
    except AssertionError:
        bad += 1
    ok(bad == 3, "only %d of the 3 forced checks fired" % bad)
    print("  3 of 3 forced checks fired.")


# ------------------------------------------------- S1a the imported instrument
def s1a_figures(sups):
    section("S1a  CONTROL -- the imported image must reproduce the family's "
            "own filed figures")
    print("  Four constant-gap ladders, global clock, the settled sizes and")
    print("  orbit sums explore_tick_pump.py F7 files. A table this rig did")
    print("  not write and was not fitted to.")
    sch = sched()
    want = {("F_2[x]", 1): 3, ("F_2[x]", 2): 6, ("F_2[x]", 3): 4,
            ("F_2[x]", 5): 4, ("h5", 1): 1, ("h5", 2): 1, ("h5", 3): 1,
            ("h5", 5): 2}
    orbs = {1: 5, 2: 28, 3: 90, 5: 12396}
    print("\n  %-9s %-8s %-24s %-9s %-8s %s"
          % ("supply", "ladder", "live at 4,6,8,10,12", "the set", "size",
             "orbit sum"))
    for name in ("F_2[x]", "h5"):
        for c in (1, 2, 3, 5):
            pump = TP.p_step(c)
            counts, last, prev, sums = image_rows(sups[name], sch, pump,
                                                  TP.GLOBAL, G_BUDGETS)
            st = settled(last, prev)
            print("  %-9s %-8s %-24s %-9s %-8d %d"
                  % (name, pump.tag, "  ".join(str(x) for x in counts),
                     "SETTLED" if st else "moving", len(last), sums[-1]))
            ok(st, "%s/%s: a bounded-gap ladder did not settle: %s"
               % (name, pump.tag, counts))
            ok(len(last) == want[(name, c)],
               "%s/%s: settled size %d against the filed %d"
               % (name, pump.tag, len(last), want[(name, c)]))
            if name == "F_2[x]":
                ok(sums[-1] == orbs[c],
                   "%s/%s: orbit sum %d against the filed %d"
                   % (name, pump.tag, sums[-1], orbs[c]))
    print("\n  8 of 8 settled sizes and 4 of 4 orbit sums reproduced.")


# ------------------------------------------------------- S1b the generator
def s1b_generator():
    section("S1b  CONTROL -- psi's orbit must BE the family's own ladders")
    for p, e, other in ((2, 1, TP.p_exact()), (5, 2, TP.p_step(2))):
        mine = HL.psi_ladder("psi", p, e, 0)
        print("    psi(p=%d, e=%d) vs %-6s : %s ... (%d members each)"
              % (p, e, other.tag, mine.S[:6], len(mine.S)))
        ok(mine.S == other.S,
           "psi(%d,%d) is not the %s ladder" % (p, e, other.tag))
    print("  2 of 2 set identities hold, so every reading at them is "
          "identical by construction.")


# --------------------------------------------------- S1c the reading function
def s1c_reading(sups, rows):
    section("S1c  CONTROL -- what the imported reading FORGETS against what "
            "the walk actually carries to infinity")
    print("  (a) DERIVED, and the premise everything rests on: the item the")
    print("      imported reading forgets is seated above exponent 1, at")
    print("      every live state at every budget and both clocks.")
    print("  (b) THE IDENTIFICATION. The imported reading names the LAST")
    print("      CLOCK MOVER. Against it the RECURRENT set -- the items still")
    print("      moving in the second half of a %d-move continuation. The"
          % (2 * LOCK_STEPS))
    print("      agreement rate is printed per clock; a global clock is where")
    print("      the identification is supposed to be sound.")
    print("  (c) THE REPAIR'S TWO OBLIGATIONS: it reproduces the imported")
    print("      reading at a global clock, and its verdict does not depend")
    print("      on which minimal-cost tie the continuation breaks.")
    sch = sched()
    pumps = ([(lb, pm) for lb, pm, _, _, _, _ in rows]
             + [("gap %d" % c, TP.p_step(c)) for c in (1, 2, 3, 5)])
    seen_a, no_clock = 0, 0
    tot = {TP.GLOBAL: [0, 0], TP.PERITEM: [0, 0]}
    agree_g, tie_ok, tie_n, unlocked = 0, 0, 0, 0
    for name in ("F_2[x]", "h5"):
        for label, pump in pumps:
            for cls, buds in ((TP.GLOBAL, G_BUDGETS), (TP.PERITEM, P_BUDGETS)):
                for states in live_at(sups[name], sch, pump, cls, max(buds)):
                    for w in states.values():
                        f = forgotten(w)
                        if f is None:
                            no_clock += 1
                            continue
                        d, slot = f
                        ok(w.seat[d][slot] > 1,
                           "%s/%s: the reading forgets degree %d slot %d at "
                           "exponent %d" % (name, label, d, slot,
                                            w.seat[d][slot]))
                        seen_a += 1
                        r = recurrent(w)
                        if r is None:
                            unlocked += 1
                            continue
                        tot[cls][1] += 1
                        if r == {f}:
                            tot[cls][0] += 1
                        if cls is TP.GLOBAL:
                            # (c) the repair must not move a sound reading
                            if reading_locked(w) == TP.reading(w):
                                agree_g += 1
                            else:
                                ok(False,
                                   "%s/%s: the repair moved a global-clock "
                                   "reading" % (name, label))
                        else:
                            tie_n += 1
                            if reading_locked(w) == reading_locked(w, True):
                                tie_ok += 1
    print("\n  (a) %d states checked, the forgotten item above exponent 1 at "
          "every one" % seen_a)
    print("      (%d states carried no clock move yet)." % no_clock)
    print("  (b) the last clock mover IS the recurrent set at:")
    for cls, nm in ((TP.GLOBAL, "global "), (TP.PERITEM, "per-item")):
        hit, n = tot[cls]
        print("        %s clock : %d of %d locked states (%.1f%%)"
              % (nm, hit, n, 100.0 * hit / n if n else 0.0))
    print("      %d states were not locked and carry no limit reading."
          % unlocked)
    print("  (c) the repair reproduces the imported reading at %d of %d "
          "global-clock states," % (agree_g, tot[TP.GLOBAL][1]))
    print("      and its reading is TIE-INDEPENDENT at %d of %d per-item "
          "states." % (tie_ok, tie_n))
    print("      The second figure is an OBSERVABLE and not a control: a")
    print("      state whose limit moves with the tie has no limit for any")
    print("      reading function to return, so this measures the object and")
    print("      not the repair. S3 excludes those states and counts them.")
    ok(agree_g == tot[TP.GLOBAL][1],
       "the repair disagrees with the imported reading at a global clock")


# ------------------------------------------- S2 the global image (PR1-PR3)
def s2_global(sups, rows):
    section("S2  PR1, PR2, PR3 -- THE IMAGE AT A HEADED LADDER, GLOBAL CLOCK")
    print("  Each headed ladder beside BOTH of its constant-gap controls: the")
    print("  ladder of its SUP, which shares its longest run, and the ladder")
    print("  of its TAIL, which shares its recurrent price. Read AT the")
    print("  budget and never cumulatively. `above 1` is the greatest number")
    print("  of coordinates above exponent 1 in any live state, which is what")
    print("  hand-attack A is conditional on.")
    sch = sched()
    verdicts = []
    for name in ("F_2[x]", "h5"):
        print("\n  supply %s" % name)
        print("  %-14s %-4s %-5s %-22s %-9s %-9s %-6s %-8s %-8s %s"
              % ("ladder", "sup", "tail", "live at 4,6,8,10,12", "the set",
                 "sup ctrl", "size", "vs sup", "vs tail", "above 1"))
        for label, pump, sup, tail, csup, ctail in rows:
            cells = {}
            for tag, pm in (("head", pump), ("sup", csup), ("tail", ctail)):
                counts, last, prev, _ = image_rows(sups[name], sch, pm,
                                                   TP.GLOBAL, G_BUDGETS)
                cells[tag] = (counts, last, settled(last, prev))
            per = live_at(sups[name], sch, pump, TP.GLOBAL, max(G_BUDGETS))
            hi = max(len(w.deep_items()) for st in per for w in st.values())
            hc, hlast, hst = cells["head"]
            slast, sst = cells["sup"][1], cells["sup"][2]
            tlast = cells["tail"][1]
            vs_sup = ("SET=" if hlast == slast
                      else ("size=" if len(hlast) == len(slast) else "DIFFER"))
            vs_tail = ("SET=" if hlast == tlast
                       else ("size=" if len(hlast) == len(tlast) else "DIFFER"))
            print("  %-14s %-4d %-5d %-22s %-9s %-9s %-6d %-8s %-8s %d"
                  % (label, sup, tail, "  ".join(str(x) for x in hc),
                     "SETTLED" if hst else "moving",
                     "SETTLED" if sst else "moving", len(hlast),
                     vs_sup, vs_tail, hi))
            verdicts.append((name, label, len(hlast), len(slast), len(tlast),
                             hlast == slast, hlast, slast, hi, hst, sst))
    ns = sum(1 for v in verdicts if v[9])
    print("\n  PR1: %d of %d headed cells SETTLED by budget 12; their sup "
          "controls, %d." % (ns, len(verdicts), sum(1 for v in verdicts if v[10])))
    for nm, lb, h, s, t, eq, hl, sl, hi, hst, sst in verdicts:
        if not hst:
            print("    %s/%s: still moving, and its sup control %s"
                  % (nm, lb, "SETTLED" if sst else "is moving too"))
    agree = sum(1 for v in verdicts if v[2] == v[3])
    same = sum(1 for v in verdicts if v[5])
    print("  PR2: the settled size agrees with the sup control's at %d of %d."
          % (agree, len(verdicts)))
    print("  PR3: the settled SET equals the sup control's at %d of %d."
          % (same, len(verdicts)))
    for nm, lb, h, s, t, eq, hl, sl, hi, hst, sst in verdicts:
        if h == s and not eq:
            print("    %s/%s: same size %d, different members -- the head "
                  "holds %s and the sup control %s"
                  % (nm, lb, h, sorted(hl - sl)[:1], sorted(sl - hl)[:1]))
    return verdicts


# ---------------------------------------- S3 the per-item image (PR4, PR5)
def s3_peritem(sups, rows):
    section("S3  PR4, PR5 -- THE IMAGE AT A HEADED LADDER, PER-ITEM CLOCK")
    print("  The clock the head is visible under. The constant-gap columns")
    print("  are new here too -- the image has only ever been read at a")
    print("  global clock -- so no figure in this table is inherited.")
    print("  `strand depths` are the exponents of the deep items a reading")
    print("  KEEPS, over the final budget's states.")
    print("  The REPAIRED reading is what builds these sets, and a state whose")
    print("  limit is not DETERMINED is excluded rather than read: `determined`")
    print("  is how many of the final budget's states carried a limit reading")
    print("  at all, against how many did not.")
    sch = sched()
    cache = {}

    def cell(name, pm):
        k = (name, pm.tag)
        if k not in cache:
            per = live_at(sups[name], sch, pm, TP.PERITEM, max(P_BUDGETS))
            rows_ = [locked_image(per[b - 1]) for b in P_BUDGETS]
            cache[k] = ([len(r[0]) for r in rows_], rows_[-1], rows_[-2],
                        per[-1])
        return cache[k]

    verdicts = []
    for name in ("F_2[x]", "h5"):
        print("\n  supply %s" % name)
        print("  %-14s %-4s %-5s %-22s %-9s %-6s %-8s %-8s %-11s %-11s %s"
              % ("ladder", "sup", "tail", "live at 8,12,16,20,24", "the set",
                 "size", "vs sup", "vs tail", "determined", "sup det",
                 "strand depths"))
        for label, pump, sup, tail, csup, ctail in rows:
            hc, hfin, hprev, hst8 = cell(name, pump)
            sfin = cell(name, csup)[1]
            slast = sfin[0]
            tlast = cell(name, ctail)[1][0]
            hlast, hlk, hun = hfin
            hst = settled(hlast, hprev[0])
            dep = strand_depths(hst8, TP.PERITEM)
            cdep = strand_depths(cell(name, csup)[3], TP.PERITEM)
            vs_sup = ("SET=" if hlast == slast
                      else ("size=" if len(hlast) == len(slast) else "DIFFER"))
            vs_tail = ("SET=" if hlast == tlast
                       else ("size=" if len(hlast) == len(tlast) else "DIFFER"))
            print("  %-14s %-4d %-5d %-22s %-9s %-6d %-8s %-8s %-11s %-11s "
                  "%s vs %s"
                  % (label, sup, tail, "  ".join(str(x) for x in hc),
                     "SETTLED" if hst else ("none" if not hlast else "moving"),
                     len(hlast), vs_sup, vs_tail,
                     "%d of %d" % (hlk, hlk + hun),
                     "%d of %d" % (sfin[1], sfin[1] + sfin[2]),
                     dep or "-", cdep or "-"))
            if hlast and hlast == slast:
                ok(dep == cdep,
                   "%s/%s: identical reading sets over strands at %s against "
                   "the sup control's %s, so the reading is not reading the "
                   "state" % (name, label, dep, cdep))
            verdicts.append((name, label, len(hlast), len(slast),
                             hlast == slast, hst, hlk, hun))
    same = sum(1 for v in verdicts if v[4])
    agree = sum(1 for v in verdicts if v[2] == v[3])
    print("\n  PR4: the settled SET equals the sup control's at %d of %d; the"
          % (same, len(verdicts)))
    print("       SIZE agrees at %d of %d." % (agree, len(verdicts)))
    live = sum(1 for v in verdicts if v[6])
    print("  PR5: %d of %d headed cells carry any locked state at the final "
          "budget," % (live, len(verdicts)))
    print("       and %d of those settled."
          % sum(1 for v in verdicts if v[5] and v[6]))
    return verdicts


# ------------------------------------------------------------------- main
def main():
    sups = supplies()
    rows = [ladder_row(lab, p, e, w) for lab, p, e, w in HL.HEADED]

    s0_forced()
    s1a_figures(sups)
    s1b_generator()
    s1c_reading(sups, rows)
    s2_global(sups, rows)
    s3_peritem(sups, rows)

    section("SUMMARY")
    print("  %d checks here, over %d headed ladders x 2 supplies x 2 clocks,"
          % (CHECKS, len(rows)))
    print("  each beside its sup-gap and tail-gap constant controls.")


if __name__ == "__main__":
    main()
