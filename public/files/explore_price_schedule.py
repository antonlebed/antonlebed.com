"""explore_price_schedule.py -- which PRICING SCHEDULES have a limit with one
deep coordinate, and which do not.

THE QUESTION. A greedy trajectory over the ring of a curve converges to a
divisor with a single infinite exponent over a support that stays flat
forever (explore_greedy_limit.py). Read that proof back and it never touches
the curve. It needs items carrying an integer DEGREE, a global CLOCK that
multiplies by 2 whenever an item is deepened, a PRICE that is degree times
staleness with staleness measured against the clock, and a one-per-degree
FRESH DISCOUNT spendable once. The six rings entered only as a supply of how
many items each degree has, which is why a walker carrying no places at all
reproduces the engine exactly. So the theorem is about a pricing schedule and
not about arithmetic, and the question this rig asks is which schedules it is
about: turn each ingredient into a dial and read where the limit survives,
where its shape changes, and where it dies.

THE SCHEDULE, abstracted. Items carry an integer degree d, with a SUPPLY of
n_d items at degree d. A state seats some items, each at an exponent e >= 1,
and carries a tick T. A degree is COVERED once its fresh discounts are spent
(m of them) and the degrees BORN COVERED are covered from the start -- in the
ring exactly the degree 1, since 2^1 - 1 divides everything. The door at an
item is

  1                   opening an item of an uncovered degree      (FRESH)
  max(1, T + 1 - e)   otherwise                                   (CLOCK)

and the price is f(d, door). A move takes a minimal-price item; a move that
lands an item above the tick sets T <- ceil(b * T). The corner
(f = d * sigma, b = 2, m = 1, degree 1 born covered) is the ring dynamics
with the arithmetic removed, and the abstract world is faithful to the ring
ONLY because the covered degrees are exactly the opened ones together with 1
-- which is a theorem there (Bang's theorem, explore_greedy_limit.py L4) and
a definition here. So the control below is against the exact-divisibility
walker and never against this rig's own reading of itself.

THE DIALS. b, the clock's growth factor, taken rational so that a
non-integer b is reachable and 2 is not privileged by the rig's arithmetic;
alpha, the degree's exponent in f = d^alpha * sigma; the ADDITIVE price
f = d + sigma; m, how many fresh discounts a degree carries; whether the
least degree is BORN COVERED; and the SUPPLY itself, whose least degree
d_min is the only thing about a ring the ideal dynamics can read.

ONE DESIGN CHOICE, since the ring cannot settle it. At m >= 2 a degree can be
uncovered while an item of it is already seated, a state the ring never
reaches -- covering there is a consequence of seating. The discount is given
to OPENINGS only: a seated item is priced by the clock even where its degree
still has a discount left. The alternative -- door 1 for every item of an
uncovered degree, the ring's rule read literally -- makes the first seated
item run away at constant price forever and seats nothing else, which is a
degenerate reading of "discount" rather than a dial. At m = 1 the two agree
on every reachable state, which is what the control certifies.

THE HAND-ATTACK, on paper before any engine code. Every lemma below is the
corresponding lemma of explore_greedy_limit.py re-derived with the dials in.

 L0 THE EXPONENT CEILING. A door of T + 1 - e lands its item at exactly
    T + 1, and T + 1 <= ceil(b * T) for every b > 1 and T >= 1, so a move
    that raises the tick raises it by exactly one multiplication. An item
    clocked when the tick was T_0 sits at T_0 + 1 forever after unless
    clocked again, and every later tick is at least b * T_0, so at tick T
    every exponent is 1 or at most T/b + 1 and therefore
    sigma >= T * (b - 1) / b at every item. The clamp max(1, .) is never
    active on a reachable state of the corner; whether a dial activates it
    is an observable, not an assumption.
 L1 PERMANENCE and L2 THE CEILING ARE ONE CONDITION. An item X clocked while
    an item of degree d_min is unseated prices at most f(d_min, T + 1), and
    L0 puts its price at or above f(d_X, T * (b - 1) / b). Under
    f = d^alpha * sigma that is

      (d_X / d_min)^alpha <= (b / (b - 1)) * (1 + 1/T),

    and the same inequality read after X's own clock is what keeps X
    minimal at every later state. So the asymptotic ceiling is

      d_X <= d_min * (b / (b - 1))^(1/alpha)                    (THE FORMULA)

    -- 2 * d_min at the corner, which is the measured law of
    explore_greedy_limit.py F2 sitting at one corner of a two-parameter
    family. At b = 3 it is 1.5 * d_min, at b = 3/2 it is 3 * d_min, at
    alpha = 2 and b = 2 it is sqrt(2) * d_min. Under the ADDITIVE price the
    same line gives d_X <= d_min + T/b + 1, which GROWS with the tick: no
    ceiling at all.
 L3 THE STEADY STATE is unchanged in form: once an item is the permanent
    clock, every other seated item is dearer at every later state and the
    only competing move is a fresh opening at the least uncovered degree.
 L4 THE LADDER is a definition here rather than a theorem, the covered
    degrees being the opened ones and the born-covered ones by construction.

WHERE THE HANDOVER'S SLATE CRACKS, found by the hand-attack and NOT by the
run. The claim carried in was that the clock's degree is 1 at every b >= 3.
That is the STEADY STATE and it is not the whole story: the finite-T form of
the inequality reads (1 + 1/T) * b/(b-1), which at b = 3 and T = 3 is exactly
2, so a degree-2 clock is admissible EARLY and only loses later. Walking it
by hand at b = 3 over a supply with a rational item: the void ties at price 2
between opening the rational item (door 2) and opening degree 2 fresh; on the
fresh branch degree 2 moves to exponent 2 (T -> 3), degree 3 opens at price 3,
degree 2 clocks to exponent 4 (T -> 9), and THERE it prices 12 against the
unseated rational item's 10 and loses. The ladder then runs 4..9 and the
rational item opens at exponent T + 1 = 10, which is itself a clock move, and
holds forever. So at b >= 3 the clock MOVES -- the settling result of
explore_greedy_limit.py F5 is a b = 2 fact -- and the displaced item is
STRANDED above exponent 1 forever. ONE INFINITE COORDINATE and A FLAT SUPPORT
are two claims, and this is where they come apart. (The stranded shape is the
one the element world reaches by classes, where a second deep place is a
transient the clock strands rather than a coordinate it feeds --
explore_element_limit.py. Here it is reached with no ring at all.)

TRANSPLANT FLAGS, fixed at the freeze.
 1. From the corner to every dial: NOTHING is carried. Each lemma above is
    re-derived with b, alpha and m symbolic, and the two places where the
    corner's "2" was doing work -- the ceiling's T/2 and the degree bound's
    2 * d_min -- are exactly where the dials bite.
 2. From the ideal world to the element world: nothing, and this rig does not
    enter it. A rider raises an exponent with no clock move, which breaks L0
    at its root; the element world is walked by explore_element_limit.py.
 3. The synthetic supplies are ABSTRACT. A supply with no item of degree 1 is
    a legal state of the abstract dynamics and is NOT certified to be any
    curve's place count; what it answers is a question about schedules, and
    the ring question it resembles needs the curve built.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 THE TICK LAW SURVIVES EVERY DIAL. What the rig PRINTS: over every move of
    every branch of every schedule, the count of moves that raise the tick
    and land at exactly T + 1 taking T to exactly ceil(b * T), the count that
    leave the tick alone and land at exponent 1, and the count of times the
    door clamp max(1, .) was active.
    KILL: one move in neither class, or one clamp firing.
PR2 THE ABSTRACT WALKER IS THE RING WALKER AT THE CORNER. What the rig
    PRINTS: at every state of the exact walker's own canonical walk over each
    of the six ring supplies, the two menus as (degree, door, kind) multisets
    with multiplicities, the two covered-degree sets, and the count of states
    compared -- the abstract walker advanced by the EXACT walker's move, so
    no tie convention can make them agree by construction.
    KILL: one disagreement, in cost, in any type's multiplicity, or in the
    covered set.
PR3 THE FORMULA IS THE CEILING. What the rig PRINTS: the planted two-item
    menu -- one stale item of degree D at the stalest exponent L0 allows, one
    unseated item of degree d_min, nothing else in the universe -- swept over
    D and over ticks, per schedule: the largest D the menu accepts as its
    minimum, against the formula's integer value.
    KILL: an accepted D above the formula, or a formula value the sweep never
    reaches at any tick.
PR4 THE CLOCK MOVES AT b >= 3, AND STRANDS AN ITEM. What the rig PRINTS: per
    schedule and supply, per branch, the last step at which a clock move went
    to an item other than the final one, and the census of items left above
    exponent 1 that are NOT the final clock, with their exponents.
    KILL: no branch at b = 3 with a stranded item (the hand-walk above is
    wrong), or one stranded item at the b = 2 corner (F5 is wrong).
PR5 ONE INFINITE COORDINATE SURVIVES EVERY DIAL WITH alpha > 0. What the rig
    PRINTS: per schedule, supply and branch, how many distinct items take a
    clock move in the LAST half of the walk.
    KILL: a branch where that count is two or more, which is a limit with no
    single deep coordinate.
PR6 THE ADDITIVE PRICE KEEPS THE LIMIT AND LOSES THE CEILING. What the rig
    PRINTS: the additive schedule's accepted D in the planted sweep as the
    tick grows, beside the multiplicative corner's at the same ticks.
    KILL: the additive sweep's accepted D bounded as the tick grows (the
    ceiling survives the additive price after all), or a second item above
    exponent 1 in its long walk (the limit does not survive it).
PR7 THE FRESH DISCOUNT SETS THE SUPPORT'S WIDTH AND NOTHING ELSE. What the
    rig PRINTS: at m = 1, 2, 3, the long walk's exponent profile and how many
    items sit at exponent 1 per opened degree.
    KILL: a width other than m at the opened degrees, or a second item above
    exponent 1.
PR8 THE DEGREE-BLIND PRICE HAS NO DEEP COORDINATE. What the rig PRINTS: at
    alpha = 0, the tick over the whole walk, the step of the last clock move,
    how many moves were fresh openings, and every item left above exponent 1.
    KILL: the tick still rising in the second half of the walk, which would
    mean a deep coordinate forms even where the price cannot see a degree.

PR9 IS THE CEILING REACHED, OR ONLY ADMISSIBLE? -- a probe added AFTER the
    first run and frozen before its own, prompted by that run's own print:
    the ceiling instrument accepts degree 2*d_min at every supply, while the
    sweep's clock census reaches it only where d_min is BORN COVERED. The
    suspicion is that the born-covered asymmetry is what makes the ceiling
    reachable -- an item of the least degree that must be bought at the clock
    price is what leaves a cheaper fresh seat at twice that degree -- so the
    ceiling and its attainment are two different ingredients' doing. What the
    rig PRINTS: the clock census with degrees 1 and 2 both born covered.
    KILL: the census at the d_min = 2 supply still reading 2 alone (the
    born-covered set is not what gates attainment), or the census at the
    d_min = 1 supply still reaching 2 (the degree-2 attractor does not need
    its fresh seat).

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 EVERY DIAL BUT ONE KEEPS THE LIMIT, AND THE ONE THAT KILLS IT IS A
   DEGREE-BLIND PRICE
   (proved for the abstract schedule -- L0 to L3, an induction over the move
   model that calls on no computation; and a rule in range, 60 walks of 200
   moves over ten schedules and six supplies). Every schedule whose price
   depends on the degree at all -- the clock's factor b at 3/2, 2, 3 and 4,
   the degree's exponent at 1 and 2, the additive price, one to three fresh
   discounts, and every born-covered set -- reaches a limit with EXACTLY ONE
   item above exponent 1 over a support flat at exponent 1 forever, and one
   item takes the last three clock moves at all 60 rows. The DEGREE-BLIND
   price alone has no deep coordinate: at alpha = 0 every unopened degree
   prices at 1, the ladder never exhausts, and the tick rises twice in an
   opening transient and then stands still for the whole of it. So the
   theorem is not about arithmetic, not about the clock's base and not about
   the discount -- it is about the price being able to tell a cheap item from
   an expensive one, which is what makes the ladder exhaust and the clock
   fire.
   WHAT IS NOT SEPARATED, and the claim is scoped to say so: the clock's
   EXISTENCE as against its BASE. b = 1 is not a value this move model takes
   -- ceil(1 * T) = T, so a landing above the tick never lifts it and there
   is no next state -- so "a growing clock" stays a hypothesis while "which
   growth factor" is a dial like the others. "The limit needs only a
   degree-sensitive price" would be the stronger claim and is NOT measured.

F2 THE DEGREE CEILING IS A FORMULA, AND THE CORPUS'S "1 OR 2" IS THAT
   FORMULA'S CORNER PLUS A COINCIDENCE IN THE SUPPLY
   (proved -- L1 and L2 above; and a rule in range, the planted instrument at
   30 schedule/d_min pairs and three ticks each). The deep coordinate's
   degree is bounded by

     d <= d_min * (b / (b - 1))^(1 / alpha).

   The corner reads 2, 4 and 6 at d_min = 1, 2 and 3 -- exactly 2 * d_min,
   which explore_greedy_limit.py F2 measured over six rings and read as a
   fact about the tower. It is a fact about the SCHEDULE, and every dial
   moves it: 1, 3, 4 at b = 3; 1, 2, 4 at b = 4; 3, 6, 9 at b = 3/2; 1, 2, 4
   at alpha = 2. A SLOWER clock RAISES the ceiling and a steeper degree
   penalty lowers it. Credit where it is due on the first half: the handover
   already carried b/(b-1) for alpha = 1 and a witness of degree 1, so the
   clock's direction is inherited and not found here. What is this rig's is
   the d_min factor, the 1/alpha exponent, the finite-tick form, and running
   b BELOW 2 at all -- where the ceiling rises to 3 * d_min, a region the
   handover's "1 at every b >= 3" never looked at. The fresh discount and the
   born-covered set do not move it at all -- m = 2, m = 3, born-free and
   born-to-2 all read 2, 4, 6.

F3 THE DEGREE-2 ATTRACTOR IS A COINCIDENCE IN THE RING'S OWN SUPPLY (rule in
   range, all 60 rows, the census read per EDGE of the branched stretch so a
   merged branch cannot hide one; found by reading the run and then checked,
   not predicted). The clock census is EXACTLY the void menu's winners: at
   tick 1 a born-covered degree must be bought at f(d, 2) and the least
   fresh degree costs f(d, 1), so the clock's degree is whichever of those
   two wins, and both where they tie. Everything the corpus had measured about
   which degree carries the infinite exponent follows:
     - at FIVE of the six rings degree 1 is born covered and degree 2 is the
       least fresh one, and f(1, 2) = 2 = f(2, 1) EXACTLY. The celebrated
       "degree 1 or 2" is that tie, and the tie needs the least fresh degree
       to be precisely twice the least born-covered one.
     - h5 is the sixth and the one-branch ring, and for the same reason:
       degrees 2 and 3 carry no place, so its least fresh degree is 4, and
       f(4, 1) = 4 loses to f(1, 2) = 2 outright.
       explore_greedy_limit.py F3 measured the single branch and attributed
       it to geography; it is an inequality.
     - take the born-covered set away and the attractor vanishes -- census
       {1} at F_2[x], h5 and g2, the three rings swept, degree 1 now being
       openable at price 1; the law then gives the same at the other three,
       every ring having a degree-1 item.
     - make degree 2 born covered as well and the census reads {1} at the
       rings and {3} at the supply with no item of degree 1, never {2}.
     - at alpha = 2, f(2, 1) = 4 > f(1, 2) = 2 and the attractor dies.
     - and the law DESIGNS a supply that attains the ceiling above d_min,
       which nothing walked before did: give the supply items at degrees 2
       and 4 and none at 1 or 3, and make degree 2 born covered, and the void
       ties at f(2, 2) = 4 = f(4, 1). The census then reads {2, 4} over two
       branches, one deep item apiece and no strand -- degree 4 being
       2 * d_min, the ceiling itself. So the ceiling is SHARP for
       trajectories and not merely for the planted menu, and the condition is
       exactly the tie: the least fresh degree must equal 2 * d_min with
       d_min born covered. At every other schedule that supply reads {2},
       degree 2 being fresh there and winning outright.
   So "the clock's degree is 1 or 2" was two independent facts wearing one
   sentence: a CEILING, which is the price schedule's (F2), and an
   ATTAINMENT, which is the supply's and the born-covered set's. Only the
   first is about pricing.

F4 AT b >= 3 THE CLOCK MOVES AND STRANDS AN ITEM -- ONE INFINITE COORDINATE
   AND A FLAT SUPPORT COME APART (rule in range, the branched sweep at five
   supplies; the mechanism hand-derived before the run). At b = 2 every
   branch settles on its clock at that clock's first move, which is
   explore_greedy_limit.py F5. At b = 3 the settling step reads 1 and 3 at
   F_2[x] and 1 and 2 at the genus-2 supply, and EVERY branch that hands off
   strands EXACTLY ONE item above exponent 1 that is not the final clock, at
   exponent 2 or 4 -- 2 of 3 branches at F_2[x] and 3 of 4 at g2 at b = 3, 1
   of 2 at each at b = 4, none at b = 3/2. Exactly one branch per ring
   escapes, the one whose first clock was already its last. The reason
   is F2 against F3: the void tie still seats a degree-2 item at every b,
   because the tie is a tick-1 fact and the tick is 1 before any clock has
   grown it, while the CEILING at b >= 3 has already fallen to d_min. So the
   item is seated, clocked, and then undercut by the item it was cheaper
   than at tick 1 and dearer than at tick 9. The limit still has one
   infinite coordinate -- the last-3-clocks reading is 1 at all 60 rows --
   but the support is not flat.
   THE STITCH: this is the shape the ELEMENT world reaches by classes, where
   a second deep place is a transient the clock strands rather than a
   coordinate it feeds (explore_element_limit.py). Two different mechanisms
   -- a class orbit there, a ceiling crossing here -- and the same limit
   shape, reached here with no ring, no classes and no riders at all.

F5 THE FRESH DISCOUNT SETS THE SUPPORT'S WIDTH AND NOTHING ELSE (rule in
   range, m = 1, 2, 3 over six supplies). The items at exponent 1 per
   opened degree number m where the supply has m items of that degree -- h5
   reads exactly 2 at m = 2 and exactly 3 at m = 3 -- and fewer where it does
   not, so the width is min(m, the degree's population), which refines PR7 as
   frozen. The degrees opened over 200 moves fall from 191 to 97 to 65 while
   the deep coordinate and the ceiling are untouched. The width-0 entries at
   every supply whose clock was opened FRESH are the off-by-one
   explore_greedy_limit.py F7 files, seen from the other side: the seated
   items are the opened degrees plus one exactly when the clock's degree is
   born covered.

F6 THE ADDITIVE PRICE KEEPS THE LIMIT AND LOSES THE CEILING (rule in range;
   proved for the bound -- L2 with f = d + sigma). Its long walks are
   indistinguishable from the corner's -- tick 512, 191 degrees opened, one
   item at exponent 257 -- while its ceiling instrument accepts degree 6, 34
   and 258 at ticks 8, 64 and 512, growing as d_min + T/b + 1 without bound.
   So the limit's SHAPE and the deep coordinate's BOUNDED DEGREE are two
   theorems, and only the second needs the degree to enter the price
   multiplicatively -- one schedule, two consequences, separated by one dial.

F7 WHAT IS STILL OPEN. Whether any schedule outside this family keeps the
   limit -- a price that is not monotone in the degree, or a clock that grows
   sub-linearly rather than by a factor, neither of which the menu's scan
   rule would even survive as written.
   (HALF SETTLED SINCE, explore_tick_pump.py: the sub-linear clock is a
   TICK LADDER whose gap grows without being multiplicative, and the limit
   SURVIVES it -- one item above exponent 1 at the square and triangular
   ladders under a global clock. The parenthetical above is refuted for
   that half: the scan rule survives as written, being a property of the
   PRICE and not of the clock. The non-monotone price is untouched.) Sharpness above d_min is NOT among the
   open questions: it was, on the first six supplies, where the census
   reached d_min and never 2 * d_min, and the void-menu law then said what
   supply would attain it and the designed supply did (F3).

THE SLATE, read against the run. PR1, PR2, PR4, PR5 and PR6 hit as frozen.
PR7 hit with a refinement: the width is min(m, the degree's population), not
m. PR3 HIT ONLY AFTER ITS OWN CORRECTION, and the correction is worth
recording: as frozen it read the ASYMPTOTIC formula at every tick, and the
derivation it came from carries a (1 + 1/T) factor, so the assert fired at
b = 4 with d_min = 2 at tick 8 -- where the finite-tick bound is 3 and the
formula is 2. The rig now checks the exact finite-tick bound at each tick and
the formula as that bound's limit, plus attainment; at b = 3/2 the bound
holds with EQUALITY, so the floor in the planted exponent decides it tick by
tick and the accepted degree oscillates (3, 2, 3) instead of falling, which
is why monotonicity is not asserted. PR8's kill FIRED AS AN OBSERVABLE and
the inference it was written for is refuted by the same run: the tick does
rise, twice, and then stands still for the whole ladder and resumes only when
the rig's finite degree cap exhausts it -- so the freeze is the LADDER's
doing and the resumption is the CAP's, and a supply with infinitely many
degrees never reaches it. PR9's two kills both missed, but its guess was
wrong in the same breath: making the least degree born covered moves the
census to the least FRESH-openable degree (3), not to twice the least degree
(4), and reading that back across every row is what produced F3.
THE HANDOVER'S SLATE, carried in from the roadmap: "the clock's degree is 1
at every b >= 3" is CONFIRMED for the steady state and REFUTED for the
transient, which the hand-attack found before any code ran. And one debt the
transplant flags understate: flag 1 says nothing is carried from the corner
to the dials, which is true of the INTUITIONS but not of the algebra -- the
b/(b-1) shape of L2 came in with the handover for alpha = 1, and only the
d_min factor, the 1/alpha exponent and the finite-tick form are derived
here.

THE DESIGN, in six sections: the harness first, then the control, then four
that read a dial each.

 S0 THE HARNESS FORCED TO FAIL, run first: the corner control given a
    tripling clock must disagree; the tick law given a doctored landing must
    fire; L0's staleness bound given a doctored state must report the item;
    the stranded census given a doctored state must count the strand; and
    the control's covered-set half, which the corner control does not
    exercise, must part from the exact walker on a schedule that covers no
    degree at birth; and PR5's last-three reading, which carries the whole
    of "one coordinate runs away", must count two when the clocks alternate.
    A check that has never been made to fail is not a check, and a check
    whose two halves share one witness has only been half made to fail. Beside them, two
    checks that are not forced failures and are not printed as any: every
    schedule's price is verified NON-DECREASING in the degree, without which
    the menu's scan rule silently truncates every menu in the rig; and the
    void-menu law is separated on five supplies answered on paper, because a
    law checked only against the census it was read off could agree with that
    census for the wrong reason.
 S1 THE POSITIVE CONTROL (PR2): the abstract walker against
    explore_greedy_limit.py's exact walker at the corner, over the six ring
    supplies, menus type by type and covered set by covered set.
 S2 THE CEILING INSTRUMENT (PR3, PR6): the planted two-item menu. The state
    is an INSTRUMENT and is not claimed reachable -- it isolates the one
    comparison L2 is about, with the fresh ladder and every other item taken
    out of the universe so that nothing else can be the minimum.
 S3 THE BRANCHED SWEEP (PR1, PR3, PR4, PR5, PR9): every schedule against six
    supplies,
    every tie choice followed over the first stretch and each branch
    continued, with the clock census, the settling step, the stranded items
    and L0's violations read per branch. L0 is RECORDED rather than asserted
    away, because a dial breaking it is a result and not a crash; it is
    asserted at the corner alone, where it is proved.
 S4 THE LONG WALK (PR5, PR6, PR7): one canonical walk per schedule and
    supply, far enough for the shape to be read -- the exponent profile, the
    items above exponent 1, and the support's width per opened degree.
 S5 THE DEGREE-BLIND CORNER (PR8), walked at a finite degree cap since its
    menu ties over every unopened degree at once.

Run: `python explore_price_schedule.py`. RUN RECORD (85125 checks, ~3.4 s,
peak 17.3 MB). S0: all six forced failures fired and the void-menu law
separated three distinct answers over five supplies answered by hand. S1: the abstract walker
equal to the exact one in cost, in every type's multiplicity and in the
covered set at 120 states over each of the six ring supplies, every state
advanced by the EXACT walker's move, both ending at tick 256. S2: the planted
instrument at 30 schedule/d_min pairs and ticks 8, 64 and 512, every accepted
degree at or below the finite-tick bound and every multiplicative schedule's
formula attained. S3: 60 rows -- ten schedules against six supplies, 1 to 4
branches carried per row, a count the whole branched stretch sets and not the
void tie alone; the clock census equal
to the void menu's winners at EVERY row, no branch below three clock moves,
one item over the last three clock moves everywhere, L0 violated at no state
of any dial, and, at b = 3 and b = 4, exactly one strand on every branch
that hands off and none on the one branch per ring that does not -- 2 of 3
branches at F_2[x] and 3 of 4 at g2 at b = 3, 1 of 2 at each at b = 4,
nowhere else. S4: 60 walks of 200 moves, exactly one
item above exponent 1 in every one. S5: the degree-blind corner, clock moves
at steps 1 and 2 and then none until the ladder's capacity is spent, where
the clock resumes at once. 1326 clock moves and 17091 fresh moves read, the
door clamp active 0 times.

THE HARNESS, forced to fail rather than trusted (S0, run before any result is
read). The corner control given a tripling clock parts from the exact walker
inside twelve moves; the tick law given an item already above the tick -- the
one state where the door clamps to 1 and the landing is e + 1 rather than
T + 1 -- fires, and the clamp counter registers it; L0's staleness bound
given an item above the exponent it allows names that item and not the legal
one beside it; and the stranded census given a doctored state counts the
strand; and the control's COVERED-SET half, which the first of those does
not exercise -- two menus can part while both walkers still agree on which
degrees are covered -- parts from the exact walker at the void once the least
degree is not born covered; and PR5's last-three reading, given clocks that
alternate between two items, counts two. All six fired. The void-menu law is checked the
other way round,
against supplies whose answers are known on paper -- no fresh degree at all,
the exact tie f(1,2) = 2 = f(2,1), a fresh degree too dear at f(4,1) = 4, the
designed tie f(2,2) = 4 = f(4,1), and the tie broken by alpha = 2 -- with the
guard that those five carry three DISTINCT answers, so agreement cannot come
from the law returning one thing always. Two further checks were rewritten during the run
because they could not fail as first written: PR5 read the distinct items
clocking in the last HALF of the walk, which a fast clock leaves empty, and
now reads the last three CLOCK MOVES with a floor of three asserted per
branch; and the degree-blind walk was read at a fixed move count that ran
past its own ladder, and now runs against the ladder's capacity with the
resumption asserted on the far side of it.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction

import explore_greedy_limit as GL
import explore_coarse_type as CT

CHECKS = 0

DEG_CAP = 600        # the walker's own degree bound, asserted against
CONTROL_N = 120      # states of the exact walk the control compares against
BRANCH_N = 10        # moves over which every tie choice is followed
BRANCH_CAP = 16      # distinct states carried through the branched stretch
SHORT_N = 60         # total moves per branch in the branched sweep
LONG_N = 200         # moves in the single canonical walk of S4
BLIND_CAP = 40       # the degree cap of the degree-blind corner (S5)
CLAMP = [0]          # how many times the door clamp max(1, .) was active
MOVES = {"clock": 0, "fresh": 0}


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ------------------------------------------------------------ the schedule
class Sched(object):
    """A pricing schedule. `price` is the whole of it; `b` grows the clock."""

    def __init__(self, tag, alpha=1, b=2, m=1, born=(1,), add=False):
        self.tag = tag
        self.alpha = alpha
        self.b = Fraction(b)
        self.m = m
        self.born = frozenset(born)
        self.add = add

    def price(self, d, sigma):
        return d + sigma if self.add else (d ** self.alpha) * sigma

    def check_monotone(self, dcap):
        """The menu's scan stops at the first degree whose door-1 price
        already beats the best found, which is sound ONLY because price(d, 1)
        is non-decreasing in d. That is a property of the schedule, so it is
        checked once per schedule rather than assumed -- a price that fell
        with the degree would make every menu in this rig a truncation."""
        for d in range(1, dcap):
            ok(self.price(d + 1, 1) >= self.price(d, 1),
               "%s: price(%d, 1) = %d falls below price(%d, 1) = %d, so the "
               "menu's scan rule is unsound" % (self.tag, d + 1,
                                                self.price(d + 1, 1), d,
                                                self.price(d, 1)))

    def tick_up(self, T):
        """ceil(b * T), exact in rationals so that b need not be an integer."""
        return -((-self.b.numerator * T) // self.b.denominator)

    def ceiling(self, dmin):
        """The largest degree the FORMULA allows a clock at, over a supply of
        least degree dmin: the greatest d with (d/dmin)^alpha <= b/(b-1).
        None where the price carries no positive power of the degree, which
        is where the derivation gives no bound at all."""
        if self.add or self.alpha == 0:
            return None
        r = self.b / (self.b - 1)
        d = dmin
        while Fraction((d + 1) ** self.alpha, dmin ** self.alpha) <= r:
            d += 1
        return d


# -------------------------------------------------------------- the walker
class Walk(object):
    """A state of the abstract dynamics carrying no items' identities: seat[d]
    is the list of exponents of the seated items of degree d, and npl[d] how
    many items that degree has. An item's identity is (degree, slot) -- its
    index in seat[d], which never moves."""

    def __init__(self, npl, sch, tag, dcap=DEG_CAP):
        self.npl = npl
        self.sch = sch
        self.tag = tag
        self.dcap = dcap
        self.seat = {}
        self.opens = {}         # degree -> fresh discounts spent there
        self.opened = []        # degrees opened, in order of first opening
        self.T = 1
        self.step = 0
        self.clocks = []        # (step, degree, slot, tick before, staleness)
        self.capped = 0
        self.bad_l0 = 0         # states carrying an item below L0's bound

    def copy(self):
        s = Walk(self.npl, self.sch, self.tag, self.dcap)
        s.seat = dict((d, list(v)) for d, v in self.seat.items())
        s.opens = dict(self.opens)
        s.opened = list(self.opened)
        s.T = self.T
        s.step = self.step
        s.clocks = list(self.clocks)
        s.capped = self.capped
        s.bad_l0 = self.bad_l0
        return s

    def covered(self, d):
        return d in self.sch.born or self.opens.get(d, 0) >= self.sch.m

    def door(self, d, e, kind):
        if kind == "open" and not self.covered(d):
            return 1
        if self.T + 1 - e < 1:
            CLAMP[0] += 1
        return max(1, self.T + 1 - e)

    def cov_set(self):
        """The covered degrees among those the supply has, for the control's
        comparison against the exact walker's divisibility test."""
        return set(d for d in range(1, self.dcap + 1)
                   if self.npl[d] and self.covered(d))

    def l0_items(self):
        """The seated items whose staleness is below L0's T*(b-1)/b, in
        integers: (T + 1 - e) * b_num < T * (b_num - b_den)."""
        num = self.T * (self.sch.b.numerator - self.sch.b.denominator)
        den = self.sch.b.numerator
        return [(d, i, e) for d, row in self.seat.items()
                for i, e in enumerate(row)
                if (self.T + 1 - e) * den < num]

    def menu(self):
        """(cost, {(degree, door, kind): multiplicity}). The scan stops at the
        first degree whose CHEAPEST conceivable move -- door 1 -- already
        costs more than the best found, which is sound because price(d, 1) is
        non-decreasing in d for every schedule here."""
        best, ties = None, {}
        d = 0
        while True:
            d += 1
            if d > self.dcap:
                self.capped += 1
                break
            if best is not None and self.sch.price(d, 1) > best:
                break
            if self.npl[d] == 0:
                continue
            row = self.seat.get(d, ())
            cands = []
            if self.npl[d] > len(row):
                r = self.door(d, 0, "open")
                cands.append((self.sch.price(d, r), r, "open",
                              self.npl[d] - len(row)))
            for e in row:
                r = self.door(d, e, "move")
                cands.append((self.sch.price(d, r), r, "move", 1))
            for cost, r, kind, n in cands:
                if best is not None and cost > best:
                    continue
                if best is None or cost < best:
                    best, ties = cost, {}
                key = (d, r, kind)
                ties[key] = ties.get(key, 0) + n
        ok(best is not None, "%s: an empty menu" % self.tag)
        return best, ties

    def apply(self, key):
        """Seat the move of type (degree, door, kind). PR1 is checked here, so
        that every move of every branch is read and not only the walks a
        section chooses to follow."""
        d, r, kind = key
        Tb = self.T
        was = len(self.seat.get(d, ()))
        before = dict(((dd, i), e)
                      for dd, v in self.seat.items() for i, e in enumerate(v))
        if kind == "open":
            fresh = not self.covered(d)
            row = self.seat.setdefault(d, [])
            row.append(r)
            slot = len(row) - 1
            if fresh:
                if self.opens.get(d, 0) == 0:
                    self.opened.append(d)
                self.opens[d] = self.opens.get(d, 0) + 1
        else:
            row = self.seat[d]
            slot = next(i for i, e in enumerate(row)
                        if self.door(d, e, "move") == r)
            row[slot] += r
            ok(len(row) == was,
               "%s: a move at degree %d changed the population" % (self.tag, d))
        e2 = self.seat[d][slot]
        after = dict(((dd, i), e)
                     for dd, v in self.seat.items() for i, e in enumerate(v))
        moved = [k for k, e in before.items() if after.get(k) != e]
        ok(all(k in after and after[k] >= e for k, e in before.items()),
           "%s: a move at degree %d displaced or lowered an existing slot"
           % (self.tag, d))
        ok(moved == ([] if kind == "open" else [(d, slot)]),
           "%s: a %s move changed the existing slots %s"
           % (self.tag, kind, moved))
        while self.T < e2:
            self.T = self.sch.tick_up(self.T)
        if self.T > Tb:
            ok(e2 == Tb + 1, "%s: a tick-raising move landed at %d, not %d"
               % (self.tag, e2, Tb + 1))
            ok(self.T == self.sch.tick_up(Tb),
               "%s: a clock move took the tick %d to %d, not %d"
               % (self.tag, Tb, self.T, self.sch.tick_up(Tb)))
            MOVES["clock"] += 1
            self.clocks.append((self.step, d, slot, Tb, r))
        else:
            ok(e2 == r == 1, "%s: a tickless move at door %d landed at %d"
               % (self.tag, r, e2))
            MOVES["fresh"] += 1
        if self.l0_items():
            self.bad_l0 += 1
        self.step += 1
        return d, kind, Tb, self.T


def profile(s):
    out = {}
    for row in s.seat.values():
        for e in row:
            out[e] = out.get(e, 0) + 1
    return out


def stranded(s):
    """Items above exponent 1 that are NOT the item the last clock move went
    to -- the shape a flat support forbids."""
    if not s.clocks:
        return []
    last = (s.clocks[-1][1], s.clocks[-1][2])
    return sorted((d, i, e) for d, row in s.seat.items()
                  for i, e in enumerate(row) if e > 1 and (d, i) != last)


def settling(s):
    """The last step at which a clock move went somewhere other than the final
    clock's item, or None where the first clock was already that item's."""
    if not s.clocks:
        return None
    last = (s.clocks[-1][1], s.clocks[-1][2])
    step = None
    for st, d, slot, _, _ in s.clocks:
        if (d, slot) != last:
            step = st
    return step


def late_clocks(s, k=3):
    """How many distinct items take the LAST k clock moves -- PR5's
    observable. Read off the last k CLOCKS and not off the last half of the
    walk, because a fast clock can leave the second half with no clock move
    at all, and a count over an empty window cannot fail."""
    return len(set((d, slot) for _, d, slot, _, _ in s.clocks[-k:]))


# ------------------------------------------------------ S0 forced failures
def s0_forced(supplies):
    """Every check the run leans on, made to fail once."""
    npl = supplies["F_2[x]"]
    fired = []

    # (a) the corner control given a tripling clock -- the menus must part
    exact = GL.Light(npl, "forced")
    w = Walk(npl, Sched("b=3", b=3), "forced")
    seen = False
    for _ in range(12):
        if exact.menu() != w.menu():
            seen = True
            break
        key = sorted(exact.menu()[1])[0]
        exact.apply(key)
        w.apply(key)
    fired.append(("the corner control", seen))

    # (b) the tick law given an item ALREADY above the tick, the one state
    # where the door clamps to 1 and the landing is e + 1 rather than T + 1
    w = Walk(npl, Sched("corner"), "forced")
    w.seat, w.T = {1: [9]}, 8
    clamped = CLAMP[0]
    try:
        w.apply((1, 1, "move"))
        hit = False
    except AssertionError:
        hit = True
    fired.append(("the tick law", hit and CLAMP[0] > clamped))
    CLAMP[0] = clamped

    # (c) L0's staleness bound given an item ABOVE the exponent it allows
    # (T/b + 1 = 5 at tick 8), beside one it allows -- so that the check is
    # shown to separate the two rather than to fire on any state at all
    w = Walk(npl, Sched("corner"), "forced")
    w.seat, w.T = {1: [7], 2: [1]}, 8
    fired.append(("L0's staleness bound", w.l0_items() == [(1, 0, 7)]))

    # (d) the stranded census given a state carrying a strand
    w = Walk(npl, Sched("corner"), "forced")
    w.seat, w.T = {1: [5], 2: [3]}, 8
    w.clocks = [(0, 1, 0, 4, 4)]
    fired.append(("the stranded census", stranded(w) == [(2, 0, 3)]))

    # (e) the control's COVERED-SET half, which (a) does not exercise -- two
    # menus can part while both walkers agree on which degrees are covered,
    # so the two halves need separate witnesses. A walker whose least degree
    # is NOT born covered must disagree with the exact one from the void.
    exact = GL.Light(npl, "forced")
    w = Walk(npl, Sched("born-free", born=()), "forced")
    fired.append(("the covered-set half",
                  w.cov_set() != set(d for d in range(1, DEG_CAP + 1)
                                     if npl[d] and exact.covered(d))))

    # (f) PR5's observable -- the count of distinct items taking the last
    # three clock moves, which carries "one coordinate runs away" and would
    # otherwise be a check that has only ever been seen to pass
    w = Walk(npl, Sched("corner"), "forced")
    w.step = 40
    w.clocks = [(30, 1, 0, 4, 4), (35, 2, 0, 8, 8), (38, 1, 0, 16, 16)]
    fired.append(("PR5's last-three reading", late_clocks(w) == 2))

    for name, hit in fired:
        print("  %-28s %s" % (name, "fired" if hit else "DID NOT FIRE"))
        ok(hit, "the forced failure of %s did not fire" % name)

    # AND ONE HAND SEPARATION, which is not a forced failure and is not
    # printed as one: the void-menu law is checked against supplies whose
    # answers are known on paper, because a law checked only against the
    # census it was READ OFF could agree with that census for the wrong
    # reason. Its non-vacuity guard is that the cases do not share an answer.
    print("  the void-menu law, on supplies answered by hand:")

    def sup(*degs):
        v = [0] * (DEG_CAP + 2)
        for d in degs:
            v[d] = 1
        return v
    cases = [(Sched("corner"), sup(1), set([1]), "no fresh degree at all"),
             (Sched("corner"), sup(1, 2), set([1, 2]), "f(1,2) = 2 = f(2,1)"),
             (Sched("corner"), sup(1, 4), set([1]), "f(1,2) = 2 < f(4,1) = 4"),
             (Sched("b12", born=(1, 2)), sup(2, 4), set([2, 4]),
              "f(2,2) = 4 = f(4,1)"),
             (Sched("a2", alpha=2), sup(1, 2), set([1]),
              "f(1,2) = 2 < f(2,1) = 4")]
    got = [void_winners(s, v) == want for s, v, want, _ in cases]
    for (s, v, want, why), hit in zip(cases, got):
        print("      %-28s expects %-8s %s"
              % (why, ",".join(str(d) for d in sorted(want)),
                 "ok" if hit else "WRONG: %s" % sorted(void_winners(s, v))))
    ok(all(got), "the void-menu law missed a supply answered by hand")
    ok(len(set(tuple(sorted(c[2])) for c in cases)) == 3,
       "the hand cases share too few distinct answers to separate anything")


# ------------------------------------------------------------- S1 control
def s1_control(supplies, ring_names):
    """PR2: the abstract walker against the exact one at the corner, advanced
    by the EXACT walker's move at every state."""
    corner = Sched("corner")
    print("  supply    states  menus equal  covered sets equal  final tick")
    for name in ring_names:
        npl = supplies[name]
        exact = GL.Light(npl, name)
        w = Walk(npl, corner, name)
        for _ in range(CONTROL_N):
            c1, t1 = exact.menu()
            c2, t2 = w.menu()
            ok((c1, t1) == (c2, t2),
               "%s: the abstract menu %s differs from the exact menu %s"
               % (name, (c2, t2), (c1, t1)))
            ok(w.cov_set() == set(d for d in range(1, DEG_CAP + 1)
                                  if npl[d] and exact.covered(d)),
               "%s: the abstract covered set %s differs from the exact one"
               % (name, sorted(w.cov_set())))
            key = sorted(t1)[0]
            exact.apply(key)
            w.apply(key)
        ok(exact.T == w.T, "%s: the two walkers ended at different ticks" % name)
        print("  %-9s %-7d %-12s %-19s %d"
              % (name, CONTROL_N, "yes", "yes", w.T))


# ------------------------------------------------ S2 the ceiling instrument
def planted(sch, D, dmin, T):
    """The two-item instrument: one stale item of degree D at the stalest
    exponent L0 allows at tick T, one unseated item of degree dmin, and
    NOTHING else in the universe. Both degrees covered, so neither carries a
    discount. Returns (whether the deep item is the menu's minimum, its
    exponent)."""
    npl = [0] * (DEG_CAP + 2)
    npl[D] = 1
    npl[dmin] += 1
    w = Walk(npl, sch, "planted")
    w.opens = {D: sch.m, dmin: sch.m}
    w.opened = sorted(set([D, dmin]))
    e = int(Fraction(T) / sch.b) + 1
    w.seat = {D: [e]}
    w.T = T
    _, ties = w.menu()
    return any(k[0] == D and k[2] == "move" for k in ties), e


def admissible(sch, dmin, T):
    """The largest degree the FINITE-TICK form of L2 allows -- the greatest D
    with f(D, T*(b-1)/b) <= f(d_min, T + 1), in exact rationals. The formula
    is this bound's limit as the tick grows, so the two part company only at
    small ticks, and a run that reads the formula at every tick would be
    reading the wrong statement."""
    lo = Fraction(T) * (sch.b - 1) / sch.b
    cap = dmin * (T + 8)
    D = dmin
    while D <= cap:
        got = D + lo if sch.add else Fraction(D ** sch.alpha) * lo
        if got > sch.price(dmin, T + 1):
            return D - 1
        D += 1
    raise AssertionError(
        "%s at d_min %d, tick %d: the finite-tick bound ran to its cap %d, so "
        "the value returned would be the cap and not the bound"
        % (sch.tag, dmin, T, cap))


def s2_ceiling(schedules, dmins, ticks):
    """PR3 and PR6: the largest degree the planted menu accepts, per schedule
    and least degree, against the finite-tick bound at each tick and against
    the formula in the limit. Acceptance is monotone in D -- the price rises
    with the degree at fixed staleness -- so the scan stops at the first
    refusal, and no sweep cap can pass for a measurement."""
    print("  schedule        d_min  formula   largest D accepted at tick %s"
          "     finite-tick bound" % ", ".join(str(t) for t in ticks))
    for sch in schedules:
        for dmin in dmins:
            got, adm = [], []
            for T in ticks:
                D, acc = dmin, 0
                while True:
                    ok(D <= dmin * (T + 8),
                       "%s at d_min %d: the D sweep ran past its cap at tick "
                       "%d" % (sch.tag, dmin, T))
                    deep, e = planted(sch, D, dmin, T)
                    ok((T + 1 - e) * sch.b.numerator
                       >= T * (sch.b.numerator - sch.b.denominator),
                       "%s: the planted item at degree %d sits below L0's "
                       "staleness at tick %d" % (sch.tag, D, T))
                    if not deep:
                        break
                    acc, D = D, D + 1
                got.append(acc)
                adm.append(admissible(sch, dmin, T))
            f = sch.ceiling(dmin)
            print("  %-15s %-6d %-9s %-24s %s"
                  % (sch.tag, dmin, "none" if f is None else str(f),
                     "  ".join("%d" % g for g in got),
                     "  ".join("%d" % a for a in adm)))
            for g, a, T in zip(got, adm, ticks):
                ok(g <= a, "%s at d_min %d, tick %d: the planted menu accepted "
                   "degree %d, above the finite-tick bound %d"
                   % (sch.tag, dmin, T, g, a))
            if f is not None:
                # the formula is the finite-tick bound's LIMIT, so what is
                # checked is that the bound converges to it and that the menu
                # actually attains it -- never that the accepted degree falls
                # monotonically, which the floor in the planted exponent can
                # break where the bound is tight with equality
                ok(adm[-1] == f,
                   "%s at d_min %d: the finite-tick bound reads %d at the "
                   "largest tick, and the formula says %d"
                   % (sch.tag, dmin, adm[-1], f))
                ok(f in got,
                   "%s at d_min %d: the formula's degree %d is never the "
                   "menu's accepted one: %s" % (sch.tag, dmin, f, got))
            else:
                ok(got[-1] > got[0],
                   "%s at d_min %d: the accepted degree did not grow with the "
                   "tick, so the ceiling survives after all: %s"
                   % (sch.tag, dmin, got))


# --------------------------------------------------- S3 the branched sweep
def key_of(s):
    return (tuple(sorted((d, tuple(v)) for d, v in s.seat.items())), s.T)


def branches(npl, sch, tag, census):
    """Every distinct state reachable by any tie choice over the first
    stretch. Every EDGE's clock degree enters the census before the states
    are deduplicated, so a branch merged away cannot hide one."""
    root = Walk(npl, sch, tag)
    live = {key_of(root): root}
    for _ in range(BRANCH_N):
        nxt = {}
        for s in live.values():
            _, ties = s.menu()
            for key in sorted(ties):
                s2 = s.copy()
                d, kind, Tb, Ta = s2.apply(key)
                if Ta > Tb:
                    census[d] = census.get(d, 0) + 1
                nxt.setdefault(key_of(s2), s2)
        if len(nxt) > BRANCH_CAP:
            nxt = dict(sorted(nxt.items())[:BRANCH_CAP])
        live = nxt
    return [live[k] for k in sorted(live)]


def continue_walk(s, n, census):
    """The canonical continuation: the least (degree, door, kind) among the
    minimal moves."""
    for _ in range(n):
        _, ties = s.menu()
        d, kind, Tb, Ta = s.apply(sorted(ties)[0])
        if Ta > Tb and census is not None:
            census[d] = census.get(d, 0) + 1
    return s


def void_winners(sch, npl, dcap=DEG_CAP):
    """The degrees that can carry a clock, read off the VOID menu alone.

    Found by reading the sweep's own census after the first run and then
    checked against every row, not predicted. At the void the tick is 1, so a
    BORN-COVERED degree must be bought at the clock price f(d, 2) while a
    FRESH one costs f(d, 1); the price rises with the degree, so only the
    least of each kind can win. Whichever wins carries the first clock -- a
    born-covered opening lands at exponent 2 and is itself a clock move,
    while a fresh opening lands at exponent 1 and its own next move, at the
    same price it just paid, is the clock. A tie gives both."""
    cb = [d for d in range(1, dcap + 1) if npl[d] and d in sch.born]
    cf = [d for d in range(1, dcap + 1) if npl[d] and d not in sch.born]
    bids = []
    if cb:
        bids.append((sch.price(cb[0], 2), cb[0]))
    if cf:
        bids.append((sch.price(cf[0], 1), cf[0]))
    ok(bids, "%s: a supply with no items at all" % sch.tag)
    # "only the least of each kind can win" is the load-bearing step, and it
    # holds because the price rises with the degree -- checked here over the
    # kinds' own candidates rather than assumed from the schedule's shape
    for cand, door in ((cb, 2), (cf, 1)):
        for d in cand[1:40]:
            ok(sch.price(d, door) >= sch.price(cand[0], door),
               "%s: degree %d bids %d at door %d, under the least of its kind "
               "at %d" % (sch.tag, d, sch.price(d, door), door,
                          sch.price(cand[0], door)))
    best = min(p for p, _ in bids)
    return set(d for p, d in bids if p == best)


def s3_sweep(schedules, supplies, names):
    print("  schedule        supply    br  clock degs  from the void  clocks"
          "  settles  strands   last 3  L0 bad")
    for sch in schedules:
        for name in names:
            census = {}
            bs = branches(supplies[name], sch, "%s/%s" % (sch.tag, name),
                          census)
            out = [continue_walk(s, SHORT_N - BRANCH_N, census) for s in bs]
            st = sorted(set(settling(s) for s in out),
                        key=lambda x: (x is not None, x))
            # PER BRANCH, never flattened: a total over branches reads as
            # though one limit carried several strands, and no limit here
            # carries more than one
            per = [len(stranded(s)) for s in out]
            strands = [x for s in out for x in stranded(s)]
            ok(max(per) <= 1,
               "%s/%s: a single branch stranded %d items above exponent 1"
               % (sch.tag, name, max(per)))
            late = max(late_clocks(s) for s in out)
            bad = sum(s.bad_l0 for s in out)
            ok(min(len(s.clocks) for s in out) >= 3,
               "%s/%s: a branch with fewer than 3 clock moves, so the last-3 "
               "reading is short" % (sch.tag, name))
            want = void_winners(sch, supplies[name])
            print("  %-15s %-9s %-3d %-11s %-14s %-7d %-8s %-9s %-7d %d"
                  % (sch.tag, name, len(bs),
                     ",".join(str(d) for d in sorted(census)),
                     ",".join(str(d) for d in sorted(want)),
                     min(len(s.clocks) for s in out),
                     "/".join("-" if x is None else str(x) for x in st)[:8],
                     "%d/%d br" % (sum(1 for x in per if x), len(per))
                     if strands else "0", late, bad))
            ok(set(census) == want,
               "%s/%s: the clock census reads %s and the void menu says %s"
               % (sch.tag, name, sorted(census), sorted(want)))
            ok(late <= 1,
               "%s/%s: %d distinct items took the last 3 clock moves, so no "
               "single coordinate is running away" % (sch.tag, name, late))
            if sch.tag == "corner":
                ok(bad == 0,
                   "corner/%s: L0 was violated at %d states" % (name, bad))
                ok(not strands,
                   "corner/%s: %d items stranded above exponent 1"
                   % (name, len(strands)))


# ------------------------------------------------------- S4 the long walk
def s4_long(schedules, supplies, names):
    print("  schedule        supply    moves  tick   opened  above e=1"
          "  width at opened degrees  profile")
    for sch in schedules:
        for name in names:
            s = continue_walk(Walk(supplies[name], sch, sch.tag), LONG_N, None)
            pr = profile(s)
            above = sorted((d, i, e) for d, row in s.seat.items()
                           for i, e in enumerate(row) if e > 1)
            widths = sorted(set(len([e for e in s.seat.get(d, []) if e == 1])
                                for d in s.opened))
            print("  %-15s %-9s %-6d %-6d %-7d %-10s %-24s %s"
                  % (sch.tag, name, s.step, s.T, len(s.opened),
                     ",".join("d%d:e%d" % (d, e) for d, _, e in above) or "-",
                     ",".join(str(x) for x in widths),
                     ",".join("e%d:%d" % (e, n)
                              for e, n in sorted(pr.items())[:4])))


# ------------------------------------------------- S5 the degree-blind corner
def s5_blind(supplies, names):
    """PR8: alpha = 0, where the price cannot see a degree. The menu ties over
    every unopened degree at once, so the walk is read at a finite cap and the
    observable is the tick."""
    sch = Sched("alpha=0", alpha=0)
    print("  The ladder is what freezes the tick, so the walk is read against")
    print("  the fresh capacity the CAP leaves -- and continued past it, where")
    print("  the clock resumes. A supply with infinitely many degrees never")
    print("  reaches that point, which is what the corner is a statement")
    print("  about; a rig at a finite cap always does.")
    print("  supply    capacity  moves  clock steps       tick  above e=1")
    for name in names:
        npl = supplies[name]
        avail = len([d for d in range(1, BLIND_CAP + 1)
                     if npl[d] and d not in sch.born])
        w = Walk(npl, sch, name, dcap=BLIND_CAP)
        for _ in range(avail + 6):
            _, ties = w.menu()
            w.apply(sorted(ties)[0])
        steps = [st for st, _, _, _, _ in w.clocks]
        above = sorted((d, e) for d, row in w.seat.items()
                       for e in row if e > 1)
        print("  %-9s %-9d %-6d %-17s %-5d %s"
              % (name, avail, w.step, ",".join(str(x) for x in steps), w.T,
                 ",".join("d%d:e%d" % (d, e) for d, e in above) or "-"))
        early = [x for x in steps if x < 3]
        ok(not [x for x in steps if 3 <= x < avail],
           "%s: the degree-blind tick rose at step %s, inside the ladder"
           % (name, [x for x in steps if 3 <= x < avail]))
        ok([x for x in steps if x >= avail],
           "%s: the tick never resumed after the ladder ran out, so the "
           "freeze was not the ladder's doing" % name)
        ok(len(early) <= 2,
           "%s: %d clock moves in the opening transient" % (name, len(early)))


# ------------------------------------------------------------------- main
def main():
    supplies, ring_names = {}, []
    for L in CT.build_ladder():
        _, npl, _, _ = GL.universe(L)
        supplies[L.name] = npl
        ring_names.append(L.name)
    for cut, tag in ((1, "no-1"), (2, "no-1-2")):
        npl = list(supplies["F_2[x]"])
        for d in range(1, cut + 1):
            npl[d] = 0
        supplies[tag] = npl
    # the ATTAINMENT supply: least degree 2, least fresh degree 4 once degree
    # 2 is born covered, so the void menu ties at f(2, 2) = 4 = f(4, 1) and
    # the ceiling 2*d_min is the tie's other member rather than merely an
    # admissible value the planted menu accepts
    npl = list(supplies["F_2[x]"])
    npl[1] = npl[3] = 0
    supplies["no-1-3"] = npl
    sweep_names = ["F_2[x]", "h5", "g2", "no-1", "no-1-2", "no-1-3"]

    schedules = [
        Sched("corner"),
        Sched("b=3", b=3),
        Sched("b=4", b=4),
        Sched("b=3/2", b=Fraction(3, 2)),
        Sched("alpha=2", alpha=2),
        Sched("additive", add=True),
        Sched("m=2", m=2),
        Sched("m=3", m=3),
        Sched("born-free", born=()),
        Sched("born-to-2", born=(1, 2)),
    ]

    section("S0  THE HARNESS FORCED TO FAIL")
    for sch in schedules:
        sch.check_monotone(120)
    s0_forced(supplies)

    section("S1  THE POSITIVE CONTROL -- THE ABSTRACT WALKER IS THE EXACT ONE")
    s1_control(supplies, ring_names)

    section("S2  THE CEILING INSTRUMENT")
    print("  The planted two-item menu: one stale item of degree D, one")
    print("  unseated item of degree d_min, nothing else in the universe.")
    s2_ceiling(schedules, [1, 2, 3], [8, 64, 512])

    section("S3  THE BRANCHED SWEEP")
    s3_sweep(schedules, supplies, sweep_names)

    section("S4  THE LONG WALK")
    s4_long(schedules, supplies, sweep_names)

    section("S5  THE DEGREE-BLIND CORNER")
    s5_blind(supplies, ring_names)

    section("SUMMARY")
    print("  %d checks passed." % CHECKS)
    print("  moves read: %s" % MOVES)
    print("  door clamp active: %d times" % CLAMP[0])


if __name__ == "__main__":
    main()
