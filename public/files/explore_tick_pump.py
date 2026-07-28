"""explore_tick_pump.py -- THE TICK LADDER: the clock's landing rule as an
ingredient of a pricing schedule, and what it decides.

THE QUESTION. A greedy trajectory's limit, its degree ceiling and its image
have all been derived over a schedule family whose clock grows by a FACTOR:
the tick advances by ceil(b * T) with b > 1. That family cannot reach b = 1
-- ceil(1 * T) = T, so a landing above the tick never lifts it and the
walker's own landing loop does not terminate -- and the corner it cannot
reach is the one a NUMBER RING sits in, where the tick lands exactly on the
exponent it answers (explore_lock_budget.py F5, F6). The corner was reached
there by a second walker with an on/off switch, and everything the corpus
knows about limits, ceilings and images was derived on the other side of it.

So the ingredient itself is what wants dialling, not a flag on it. Replace
"the tick grows by b" with a TICK LADDER: a set S of exponents the clock may
stand at, the clock advancing to the least member of S at or above the
exponent just landed on. Then

    S = every integer      the tick lands exactly       (a number ring)
    S = powers of 2        the tick doubles             (a function field)
    S = powers of b        the b dial of the family, ceil(b*T) from 1
    S = 1, 1+c, 1+2c, ...  a gap bounded by c
    S = the squares        a gap growing like 2*sqrt(e)

-- one ingredient subsuming the clock's base and reaching a corner the base
cannot. Three separate open items are the same question at this object: the
exact-tick corner above; whether a world sits BETWEEN a valuation linear in
the depth and one logarithmic in it; and explore_price_schedule.py F7's own
"a clock that grows sub-linearly rather than by a factor", filed there as
outside the family.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. "The tick grows",
"the ladder climbs", "the budget" are all the FACTOR family's words, and the
filed dichotomy is stated in them -- lock against sprawl, exact against
doubling. A ladder has no b and no growth rate. What it has is a GAP, and
the freeze is written in that word or in none.

TRANSPLANT FLAGS, fixed at the freeze.
 1. From the factor family to the ladder family: "b" and everything indexed
    by it. The degree ceiling, the void-menu law and the strand are all
    derived at a geometric ladder and none is assumed to survive.
 2. From the exact/doubling PAIR to the family: the filed axis is a two-point
    reading of a family with infinitely many points, and "exactness decides
    the ladder's fate" is a hypothesis about the two points measured, not a
    law over the family. It is re-asked here and not inherited.
 3. From the global clock to the per-item one: locality is a second axis and
    the two are crossed, never read off one another.
 4. From the IDEAL world to the element world: nothing. An element move
    seats a bundle, and no section here enters that world.
 5. From lambda to the ladder: the correspondence in A below is a derivation
    about a LONE place deepening alone, which is not a trajectory. It is
    checked against both ring engines and the function field's rather than
    assumed, and it says nothing about a state with several places seated.
 6. From the UNIFORM cells to the MIXED ones (S5 onward): every law this rig
    measures above sits on a walk whose items all share ONE ladder. Nothing
    about a universe of several ladders is inherited -- the budget, the
    runaway count and the stop location are re-derived at G and re-measured,
    and the uniform cells are re-run as S5's own control.

THE HAND-ATTACK, on paper before any engine code.

 A. THE LADDER IS LAMBDA'S JUMP SET. For a lone place deepened with nothing
    else seated, the door at depth e is the least r with lambda(P^(e+r)) not
    dividing lambda(P^e), i.e. the least r with v(e + r) > v(e) for v the
    valuation lambda carries. So the landing sits one above the least JUMP of
    v at or after e, and the tick is that jump:

        S = { a : v(a+1) > v(a) }        v(a) = #{ s in S : s < a }.

    v = a - 1 (a number ring's p^(a-1)) gives S = every integer; v =
    ceil_log2(a) (a function field's 2^ceil_log2(a)) gives S = the powers of
    2; v = a//2 (a ramified shape) gives S = the odd numbers. So the two
    worlds are two ladders, and the filed "linear against logarithmic" is a
    statement about the DENSITY of one set.

 B. THE GAP IS WHAT A LADDER GIVES THE DYNAMICS. Write

        gap(e) = next_S(e) + 1 - e,

    the door of an item at depth e read against its own clock. A clock move
    lands at T_prev + 1 and lifts the tick to T, so the deep item's next door
    is T - T_prev, which is a gap. The recurrent vehicle therefore costs
    d_deep * gap forever, and that is the whole of the walk's budget.

 C. SO BOUNDEDNESS OF THE GAP, NOT EXACTNESS, IS WHAT DECIDES A LADDER'S
    FATE. If gap <= G everywhere then the recurrent price never exceeds
    d_deep * G, no degree above that is ever affordable, and the walk stops
    with the supply still offering openings -- at about d_deep * sup gap,
    which is a formula and not a yes/no. If the gap is unbounded then every
    new record gap affords a new degree and the walk climbs forever. The
    exact ladder is the extreme point G = 1 of the first case, and the filed
    axis reads two points of a spectrum.

 D. AND A PER-ITEM CLOCK CARRIES NO STATE AT ALL. Under one tick per item the
    tick after a landing is next_S(max(T_item, e)) = next_S(e) by induction
    from T = 1, so the tick is a FUNCTION of the item's own exponent. The
    price is then exactly f(d, gap(e)) -- which is a ring's door verbatim --
    and the state is the exponents alone.

 E. THE CEILING WITH THE LADDER AS A PARAMETER. The stalest an item can be at
    tick T_k is T_k - T_{k-1}, having been landed at T_{k-1} + 1; its rival
    is an unseated covered item of the least degree at door T_k + 1. So

        f(D, T_k - T_{k-1}) <= f(d_min, T_k + 1),
        D <= d_min * ( (T_k + 1) / (T_k - T_{k-1}) )^(1/alpha),

    whose limit over a geometric ladder is d_min * (b/(b-1))^(1/alpha), the
    filed formula. Over ANY bounded-gap ladder the ratio diverges, so the
    filed formula's divergence as b -> 1 is not an artefact of a derivation
    that assumed a growing tick: it is what the bound says. What makes it
    vacuous rather than wrong is that its instrument is a two-item menu with
    no cheap recurrent vehicle -- and a cheap recurrent vehicle is exactly
    what a bounded gap leaves standing.

 F. WHICH LADDERS ARITHMETIC ACTUALLY HAS, from the principal-unit
    filtration. (O/P^a)^* = k^* x (1+P)/(1+P^a), and v reads the second
    factor's exponent. In equal characteristic p, (1+x)^p = 1 + x^p sends
    level i to p*i, so the exponent is p^ceil_log_p(a) -- a multiplicative
    ladder, gap unbounded. In mixed characteristic with e = v_P(p), level i
    goes to min(i + e, p*i), which is i + e past the boundary, so the
    exponent is p to about (a-1)/e -- a ladder of constant gap e. So the
    ladders arithmetic realizes are the multiplicative ones and the
    constant-gap ones, with the gap the RAMIFICATION INDEX; a gap that grows
    without being multiplicative is realized by no Dedekind ring. This is a
    derivation, and the sections check only its two measured worlds.

 G. THE MIXED UNIVERSE, where the items do not share a ladder -- the only
    shape in this family a RING has, its unramified places at gap 1 and its
    ramified ones at gap e in one walk. Three steps, on paper.

    (i) AN ITEM'S OWN GAP IS ITS LADDER'S CONSTANT AFTER ONE MOVE. On the
    gap-c ladder S = {1, 1+c, 1+2c, ...} under a per-item clock, where the
    tick is next_S of the item's own exponent (D), gap(1) = 1 and gap(2) =
    gap(2+jc) = c. An item seated fresh stands at e = 1 and its move takes it
    to e = 2, so every later depth it can stand at is 2 + jc -- and the
    ladder's own members, where the gap falls back to 1, are missed by all of
    them. So a wide item's door is 1 exactly ONCE and c forever after. "A
    wide ladder's gap returns to 1 periodically, so a wide item can move
    cheaply at those depths" is true of the ladder as a function of depth and
    false of the walk.

    (ii) SO THE BUDGET IS A MIN OVER PRODUCTS, NOT OVER GAPS. The recurrent
    price of the item (d, c) is f(d, c), so the flat tail minimum should be
    min over items SEATED at the end of f(d, c_item) and the runaway should
    be that argmin. A gap-3 item at degree 1 therefore beats a gap-1 item at
    degree 4, and "the smallest gap decides" is false as stated.

    (iii) HENCE A STRAND, which is a coordinate no uniform cell has. A wide
    item whose first move is affordable while the budget is still loose, and
    whose f(d, c) is above the final budget, moves ONCE and stands at
    exponent 2 forever. So a mixed limit reads: one runaway at the least
    product, plus one stranded coordinate per wide item that got its one
    cheap move in. Same SHAPE as the b >= 3 strand of the factor family and a
    different mechanism -- there the ceiling falls under a seated item, here
    the item's own door widens under it.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 THE LADDER IS THE RING'S OWN. For a lone place of each kind in both
    number rings and at three function-field degrees, the tick read off the
    engine's own door equals the ladder's next member. What the rig PRINTS:
    per place kind, the door sequence to depth 24, the ladder the tick
    sequence names, and its greatest gap.
    KILL: one depth where the engine's tick and the ladder's disagree.

PR2 THE LADDER WALKER IS THE CERTIFIED ONE. At a geometric ladder the walker
    here reproduces the factor-family walker move for move, and at the exact
    and doubling ladders it reproduces the on/off walker. What the rig
    PRINTS: over a canonical walk on each supply, the two minimal costs, the
    two menus collapsed to (degree, door, kind) multisets, the two tick
    sequences and the count of states compared.
    KILL: one disagreement in cost, in any type's multiplicity, or in a tick.

PR3 THE LADDER'S FATE IS THE GAP'S BOUNDEDNESS, AND WHERE IT STOPS IS A
    FORMULA. Over one supply and one seed, every bounded-gap ladder stops and
    every unbounded one climbs; and a stopped walk's least uncovered degree
    tracks d_deep * sup gap. What the rig PRINTS: per (ladder, locality)
    cell, the greatest gap seen, the degrees seated, the least uncovered
    degree, the last menu minima, and stopped or climbing.
    KILL: a bounded-gap ladder that climbs, or an unbounded one that stops.

PR4 THE INTERMEDIATE LADDER SPRAWLS, AND SLOWLY. The square ladder's gap
    grows without bound, so its walk climbs; and it seats strictly fewer
    degrees in the same move budget than the doubling one. What the rig
    PRINTS: the seated-degree count of the exact, constant-gap, triangular,
    square and doubling ladders side by side.
    KILL: the square ladder stopping, or seating as many degrees as the
    doubling one.

PR5 THE LIMIT'S SHAPE, PER CELL. What the rig PRINTS: per (ladder,
    locality) cell, how many items stand above exponent 1 after the walk,
    the deep item's degree and exponent, and whether the support is flat.
    KILL: none frozen -- the filed theorem is proved at a geometric ladder
    with a global clock and this is the first reading of the other cells, so
    the observable is recorded and weighed after the run.

PR6 THE PER-ITEM CLOCK IS A FUNCTION OF THE EXPONENT. At every state of
    every per-item walk, each item's tick equals next_S of its own exponent.
    What the rig PRINTS: the number of (state, item) pairs checked and the
    number off.
    KILL: one item whose tick is not next_S of its exponent, which would mean
    the per-item clock carries state and D is wrong.

PR7 THE CEILING WITH THE LADDER AS A PARAMETER. What the rig PRINTS: per
    ladder and least degree, the largest degree the planted two-item menu
    accepts at three ticks, the finite-tick bound of E at each, and the
    bound's limit where it has one; and beside them the clock census of an
    actual trajectory.
    KILL: the planted menu accepting a degree above the finite-tick bound.

PR8 THE IMAGE AT A BOUNDED-GAP LADDER. What the rig PRINTS: per ladder and
    supply, the number of reachable shapes and the summed orbit size at move
    budgets 4 through 12, so that a constant reads FINITE, a linear one reads
    COUNTABLE and a doubling one reads neither.
    KILL: none frozen -- the count's own shape is the observable, and the
    corpus has no prior for it at a bounded gap.

PR9 THE MIXED UNIVERSE. Over the S2 cell with the ladder attached to the
    ITEM -- gap 1 everywhere, gap 3 everywhere, gap 3 planted at degree 1
    alone, gap 3 planted at degrees 1 to 5, and gap 3 everywhere but degree
    1 -- the budget is the least product and the runaway is its argmin. What
    the rig PRINTS: per (universe, clock) the flat tail minimum, the
    hand-derived least product, the runaway's degree and its own gap, the
    least uncovered degree, how many items stand above exponent 1, and each
    stranded item with its degree, gap and product.
    KILL: a flat tail minimum that is not the least product over the seated
    items; a runaway that is not its argmin; or an item standing above
    exponent 1 whose product is at or below the budget, which would be an
    item priced to move and not moving.

PR10 THE LADDER CROSSED WITH THE FOUR INGREDIENTS. Every image and limit
    reading in this rig sits at one schedule (alpha = 1, m = 1, born = {1}),
    and only F5's global-clock survival is crossed with the old dials (F8
    (ii)). Cross them: 7 ladders x 8 dials x 2 clocks, the b dial absent
    because the LADDER is b. What the rig PRINTS: per cell, stopped or
    climbing and how many items stand above exponent 1.
    KILL: a bounded-gap ladder that climbs at any dial whose price can see a
    degree, or one that stops at the degree-blind price -- the stop law is
    hand-derived from a recurrent price f(d_deep, c), which at alpha = 0 is
    the fresh opening's price too.

PR11 WHETHER A RING STRANDS ITS OWN WIDE PLACE -- the mixed law's one
    arithmetic consequence, testable with the two rings already built rather
    than with a ring of ramification index 3. A ramified place has N = p and
    gap 2, so its product is N^2 against the lock's own recurrent cost. What
    the rig PRINTS: per ring, the lock's vehicle and cost, every place
    standing above exponent 1 at the locked state, every ramified place's
    norm and N^2, whether any ramified place is seated at all, and the same
    reading from a seed that PLANTS a ramified place at exponent 1.
    KILL: a place other than the lock's own vehicle standing above exponent
    1, which is a strand and would put the corpus's flat number-ring support
    at the wrong scope.

Predict, from B and C: the constant-gap ladder at gap c seats about c
degrees past its seed, and the exact one seats one.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 THE TICK LADDER IS LAMBDA'S JUMP SET, AND A NUMBER RING'S GAP IS ITS
   RAMIFICATION INDEX (rule in range: every place of norm at most 200 in both
   rings -- 90 in all, 82 split, 5 inert, 3 ramified -- read at depths 1 to
   24, 0 off; plus three function-field degrees). WHICH HALF IS WHICH, since
   the headline pairs two different kinds of statement: that the ladder is
   lambda's jump set is a DERIVATION from the door rule and would be true of
   any lambda, so it is not what the 90 places test. What they test is that
   the ENGINE's own doors land where that derived ladder says they do, and
   what they then FIND -- the content -- is the second clause, which is
   arithmetic and could have come out otherwise. The tail gap of a place's
   own tick sequence equals its ramification index at 90 of 90: 1 at every
   split and inert place, 2 at every ramified one. The function field's is
   the doubling ladder at degrees 1, 2 and 3 identically, its gap already 16
   by depth 24. So the corpus's "linear against logarithmic" is a statement
   about the DENSITY of one set of integers, and the ladder is the object
   both worlds are instances of.
   AND THE FILED TABLE ANOMALY IS NOT ONE. Three of the 90 places carry a
   HEAD -- a stretch of leading depths whose gap exceeds the tail's -- and
   they are exactly the three with p - 1 <= e, at 90 of 90: K5's ramified
   place over 2 (head of 4 depths, doors 1,1,4,3,2,1,2,1,...) and K23's two
   split places over 2. That is hand-attack F's boundary read off the engine:
   below e/(p-1) the principal units are still SQUARING and above it they are
   STEPPING by e, so a head exists precisely where the residue characteristic
   is small enough for the multiplicative regime to reach depth 1. What
   explore_lock_budget.py F6 files as a table anomaly costing "one door of 2"
   is the mixed-characteristic filtration's own head, and it is predicted
   rather than tolerated.
   CORRECTED BY explore_head_width.py F2: "p - 1 <= e" is a true statement
   ABOUT these 90 places and not a criterion. A head needs f = 1, mu_p in
   K_P and e = (p-1)p^t, and the two conditions part at 8 of 23 places read
   across 20 local fields — including both inert places over 2, which no
   ring here has. The 90 hold because every ring here is quadratic.
   AND THE LADDER THIS SECTION HANDS A PLACE IS THE TAIL ALONE, which is not
   the ladder the sections below read. explore_headed_ladder.py F1 finds
   a walk reading TWO numbers off a ladder -- the SUP gap deciding where it
   stops and how many coordinates stand deep, the tail deciding what the
   runaway pays -- which a constant ladder cannot tell apart. So the tail
   gap is still the ramification index and it is only HALF of what a place
   hands the dynamics: the sup is 2 at K23's two SPLIT places over 2, 3 at
   Z[sqrt +-2], 4 at K5's ramified place over 2, 5 at Z[i], and 6 and 12
   outside the quadratic range.

F2 THE POSITIVE CONTROL (rule in range; 60 states per row, the other walker
   advanced by THIS walker's move so no tie convention can make them agree by
   construction). At the factor ladders b = 2, 3 and 3/2 over two supplies the
   ladder walker and explore_price_schedule.py's agree in cost, in the menu
   collapsed to a (degree, door, kind) multiset, in the tick and in the seats
   at all 360 states; at the exact and doubling ladders under both clocks it
   agrees with explore_lock_budget.py's on/off walker at all 240. So the
   ladder family CONTAINS both certified walkers, and the corner reached
   there by a switch is one member of it.

F3 WHAT DECIDES A LADDER'S FATE IS THE GAP'S BOUNDEDNESS, NOT THE TICK'S
   EXACTNESS -- AND WHERE A STOPPED LADDER STOPS IS A FORMULA (rule in range;
   7 ladders x 2 clocks, 120 moves a cell, one supply of two items at every
   degree to 400 and one seed; the mechanism hand-derived pre-run at C). All
   four constant-gap ladders STOP under both clocks, at gaps 1, 2, 3 and 5,
   with the supply still offering a door-1 opening; all three
   growing ladders climb under both. And the stop location is the derived
   d_deep * sup gap: with the deep item at degree 1 in every stopped cell,
   the least uncovered degree reads 2, 2, 3, 5 against products 1, 2, 3, 5 --
   exact at three of four and floored at the fourth by the born-covered set,
   degree 1 never being fresh-eligible.
   BUT THE STOP IS A TIE AT EVERY GAP ABOVE 1, which the first reading of
   this table missed. The recurrent vehicle costs d_deep * sup gap and the
   least uncovered degree costs exactly itself, so wherever the two coincide
   -- gaps 2, 3 and 5, at both clocks -- that opening sits IN the menu's
   minimum, and the canonical walk declines it by TIE-BREAK and not by price.
   Only the exact ladder refuses outright, 1 against 2. What the tie is worth
   is measured rather than argued: the branch that takes it buys exactly one
   more degree and then refuses strictly, stopping at 3, 4 and 6 against the
   canonical 2, 3 and 5. So the verdict is unchanged and the mechanism is
   not -- a bounded gap stops the ladder within ONE degree of d_deep * sup
   gap on every branch, and "declines a door-1 opening on a supply that never
   runs out" is true of the exact ladder alone.
   SO THE FILED AXIS IS THE EXTREME POINT OF A SPECTRUM. "Exactness decides
   the ladder's fate" (explore_lock_budget.py F5) reads two points of a
   family: gap 1 is one bounded ladder among many, gaps 2, 3 and 5 stop
   exactly as it does, and a ring's own RAMIFIED places are the gap-2 case
   (F1). What is not a spectrum is the verdict -- bounded stops, unbounded
   climbs, with nothing in between at any ladder run.

F4 A WORLD BETWEEN LINEAR AND LOGARITHMIC EXISTS IN THE SCHEDULE AND NOWHERE
   IN ARITHMETIC (rule in range for the first half; a derivation for the
   second). The square ladder's gap grows like 2*sqrt(e) and the triangular
   one's like sqrt(2e): both CLIMB, and under a global clock both climb slower
   than the doubling ladder -- 82 and 61 degrees seated against 115 in the
   same 120 moves. So the corpus's two worlds are two points with a genuine
   middle, and explore_price_schedule.py F7's "a clock that grows
   sub-linearly rather than by a factor" is answered: the menu's scan rule
   survives it and the limit does too (F5).
   PR4'S KILL FIRED, at the per-item clock and not at the global one, and the
   miss is worth more than the hit: there the square ladder seats MORE
   degrees than the doubling one, 26 against 21, reversing the global order.
   A per-item clock prices an item at f(d, gap(e)) with gap read at the
   item's OWN depth (F5), and a doubling ladder's gap returns to 1 at every
   power of two -- so it keeps one cheap vehicle available where a square
   ladder does not, and spends its moves deepening rather than opening.
   "Slower ladder, fewer degrees" is a global-clock statement.
   AND NO DEDEKIND DOMAIN WITH FINITE RESIDUE FIELDS HAS SUCH A LADDER
   (derivation, hand-attack F, checked only at the three worlds this rig
   reads; the finiteness is not a side condition but where lambda is defined
   at all, being the exponent of a finite unit group). (O/P^a)^* = k^* x
   (1+P)/(1+P^a), and the second factor's exponent is what v reads: in equal
   characteristic the p-th power map sends level i to p*i, giving a
   multiplicative ladder; in mixed characteristic it sends i to
   min(i + e, p*i), giving a constant gap e past the head. There is no third
   regime, so a gap that grows without being multiplicative is a design point
   of the schedule with no ring behind it. The lock/sprawl dichotomy is
   therefore the CHARACTERISTIC -- equal against mixed -- and the bounded
   middle between "gap 1" and "gap 1" is ramification.

F5 THE LIMIT'S SHAPE SURVIVES EVERY LADDER UNDER A GLOBAL CLOCK, AND UNDER A
   PER-ITEM ONE IT IS THE GAP THAT SETS THE RUNAWAY COUNT (rule in range, the
   same 14 cells read for a second observable). Under a global clock exactly
   ONE item stands above exponent 1 at all seven ladders -- the exact, the
   three constant gaps, the two sub-multiplicative ones and the doubling one
   -- so the filed limit theorem, proved over the factor family, survives
   every ladder run here, the intermediate world included. Seven instances
   and not the family: no ladder outside this list is walked. Under a per-item
   clock it does not, and what breaks it is graded rather than binary: 1, 1,
   3 and 6 items above exponent 1 at gaps 1, 2, 3 and 5, non-decreasing in
   the gap, and 26 to 39 at the growing ladders.
   SO THE FILED READING REFINES. explore_lock_budget.py F7 has locality
   deciding the limit's shape; what decides it is the gap AT A PER-ITEM
   CLOCK, and locality is what makes the gap visible to the price at all. A
   local clock is not itself the deciding axis either: the gap-3 cell is
   local too and carries three runaway coordinates. (CORRECTED SINCE,
   explore_headed_ladder.py F2: this passage read "a number ring keeps its
   flat support because its gap is 1 or 2", and it does not -- a ring's
   HEADED places stand at sup 3, 4 and 5, and the count above exponent 1
   reads the SUP gap -- the tail deciding the recurrent price instead.
   The ring's flat support is F11's arithmetic, not this cell.) (SCOPED SINCE, F9: those three are ONE runaway and two
   STRANDS -- items carried above exponent 1 and then priced out -- which is
   a distinction "how many stand above exponent 1" cannot make.)
   AND THE PER-ITEM CLOCK CARRIES NO STATE (proved -- hand-attack D -- and
   checked at 8922 (state, item) pairs, 0 off). Every item's tick is next_S
   of its own exponent, so the price is exactly f(d, gap(e)) and the state is
   the exponent multiset alone. That is a ring's door verbatim, and it is
   what lets the orbit-size lemma transfer to the per-item cells at all.

F6 THE DEGREE CEILING IS A PROPERTY OF GEOMETRIC LADDERS ONLY, AND ITS
   DIVERGENCE IS REAL RATHER THAN AN ARTEFACT (rule in range; the planted
   two-item instrument at 7 ladders x 2 least degrees x 3 ladder members, the
   bound ATTAINED at 42 of 42). Hand-attack E's finite-tick bound
   f(D, T - T_prev) <= f(d_min, T + 1) is exactly what the planted menu
   accepts, at every row. Its controlling quantity is the ratio
   (T + 1)/(T - T_prev), and that ratio has a limit at ONE ladder here: the
   doubling one, where it falls 9/4, 17/8, 33/16 toward 2 and the bound reads
   2*d_min -- the filed formula d_min*(b/(b-1))^(1/alpha) reproduced. At
   every other ladder it GROWS: 9, 10, 11 at the exact one, 5, 6, 7 at gap 2,
   and 2, 17/7, 26/9 at the squares. So the ceiling is finite iff the ladder
   grows at least geometrically, which is what "b > 1" was silently carrying.
   The forward half is the seven instances; the CONVERSE is algebra and is
   checked at 8290 ladder steps rather than argued -- R/(R-1) equals
   (T+1)/(T_prev+1) exactly, and a ladder's own growth T/T_prev is never
   below that, so a bounded ratio forces at-least-geometric growth.
   The filed formula's divergence as b -> 1 is therefore not an artefact of a
   derivation that assumed a growing tick: it is the bound's own value, and
   what makes it vacuous is that its instrument is a two-item menu with no
   cheap recurrent vehicle -- the one thing a bounded gap always leaves. The
   canonical continuation's clock census reads {1} at every ladder over both
   ring supplies, far below every bound in the table.

F7 AT A BOUNDED GAP THE IMAGE SETTLES, AND ITS SIZE IS NOT A FUNCTION OF THE
   GAP (rule in range; the readings of the states LIVE at move budgets 4 to
   12, branching on every minimal-cost tie, two ring supplies). Read AT the
   budget rather than cumulatively -- a state passed through on the way is
   not a limit, and a cumulative count carries every transient -- the reading
   SET of all four constant-gap ladders stops MOVING, at both supplies, while
   every growing ladder's set is still moving at budget 12. Over F_2[x]'s
   supply the settled sets have 3, 6, 4 and 4 members at gaps 1, 2, 3 and 5,
   and 5, 28, 90 and 12396 with the supply's item identities put back; over
   h5's, 1, 1, 1 and 2. So the answer to "which tiny" is: finite, settled by
   budget 8, and NOT monotone in the gap -- the gap-2 ladder reaches MORE
   limits than the gap-5 one, which kills the natural reading that a wider
   gap buys a bigger image. Two of the four counts, 3 and 6, are not powers
   of 2 at all, a second and independent witness that the ring's measured 2^t
   is its sample's shape rather than the formula's.
   THE SCOPE, which the column headings do not carry: a SETTLED set is the
   limit set, the support never moving again once the walk locks, so the
   reading a state carries IS the limit it reaches. A moving set is a
   snapshot of states still evolving and is no image at all, which is why the
   growing ladders' figures are reported only as evidence that nothing
   settles.
   PR8 AS FROZEN named the reachable SHAPE count, and the observable was
   replaced before any verdict was read: a shape keeps the deep item's own
   exponent, which a limit forgets, so a shape count moves forever at a
   ladder whose walk has locked and would have read every clock move as a
   new image point.
   AND THE FIRST READING OF THIS SECTION WAS WRONG TWICE, both caught in the
   audit and both worth recording. The count was taken CUMULATIVELY across
   budgets, which carries every pre-lock transient into the image and read 4
   where the exact ladder has 3; and the orbit sum DROPPED the deep item from
   its own block, undercounting by exactly that item's free choice, where
   explore_schedule_image.py's lemma (b) gives a block carrying the deep
   coordinate beside j flat items n_d * C(n_d - 1, j). Neither error was
   visible in the printed shape of the table.

F9 IN A MIXED UNIVERSE THE BUDGET IS A MIN OVER PRODUCTS, SO THE SMALLEST
   GAP DOES NOT DECIDE (rule in range; 5 universes x 2 clocks over the S2
   cell, 120 moves each, the two uniform universes reproducing the S2 cell
   move for move at 480 states -- a regression check on the ladder-per-item
   plumbing, S1b owning the independent control; 2511 (state, item) pairs read
   for the per-item tick on its OWN ladder, 0 off). Under a per-item clock the
   flat tail minimum equals min over seated items of f(degree, that item's own
   tail gap) at 5 of 5 universes, and the runaway is a least-product item at 5
   of 5 -- the argmin where it is unique, and where TWO items tie at the least
   product the walk takes one and the other is exactly the tied strand below.
   What that buys is three readings no uniform cell can give:
     - a WIDE item can hold the recurrent slot. With gap 3 planted at degrees
       1 to 5 and gap 1 everywhere else, the runaway is the GAP-3 item at
       degree 1 at product 3, beating every gap-1 item -- the cheapest of
       which sits at degree 6. "The smallest gap decides" is false; the least
       PRODUCT decides.
     - and one narrow item at the least degree freezes an entire wide
       population: gap 3 everywhere but degree 1 reads budget 1, least
       uncovered 2 and ONE coordinate above exponent 1, which is the uniform
       gap-1 cell's reading exactly.
     - between them, gap 3 at degree 1 alone reads budget 2 with the runaway
       the gap-1 item at degree 2, and BOTH degree-1 items stranded: 3 above
       exponent 1 where the uniform gap-1 universe has 1. So mixing can raise
       the runaway count above the narrow cell's and lower it below the wide
       cell's, and neither is what a gap alone predicts.
   AND A STRAND COMES IN TWO KINDS, which is the tie mechanism a third time
   (F3's stop is the first, F7's tie-branch the second). An item above
   exponent 1 that is not the runaway is stranded at a PRICE where its product
   is strictly above the budget -- stranded on every branch -- and at a TIE
   where it equals the budget, sitting in the final menu's own minimum and
   standing only because the canonical walk breaks the tie elsewhere. The
   split reads 2 priced out and 0 tied at gap 3 planted at degree 1, and 1 of
   each at both universes whose deep item is wide. The first reading of this
   section asserted the strict inequality and the tie fired it.
   AND THE PRODUCT LAW IS A PER-ITEM CLOCK'S. Under a GLOBAL clock the same
   universe reads budget 3 against a least product of 2, because one shared
   tick hides an item's own gap from the price -- which is F5's locality
   reading arriving from the other side, and it is the per-item clock that a
   ring has.
   THE HAND-ATTACK'S OWN CORRECTION, worth recording because it is the
   natural first reading of a wide ladder: its gap does return to 1, at
   every one of its own members -- and an item's reachable depths, 1, 2, 2+c,
   2+2c, ..., miss all of them after the first step. So a wide item's door is
   1 exactly ONCE, and "it can take the cheap move at those depths" is true of
   the ladder and false of the walk (G(i)).

F10 THE STOP LAW AND THE LIMIT SURVIVE THE FOUR-INGREDIENT CROSS, AND THE ONE
   DIAL THAT KILLS THE LIMIT NEEDS A GROWING GAP (rule in range; 7 ladders x
   8 dials x 2 clocks = 112 cells, 120 moves each, one supply and one seed).
   Every image and limit reading above sits at one schedule, which F8 (ii)
   filed as open. Crossed:
     - the FATE is the gap's boundedness at all 98 cells whose price can see a
       degree -- bounded stops, unbounded climbs, at alpha = 2, the additive
       price, two discount counts and three born-covered sets alike. F3's
       verdict is dial-free there.
     - the LIMIT'S SHAPE under a global clock is one runaway at all 49
       degree-visible (ladder, dial) cells. F5 measured the ladder axis at one
       dial and the corpus measured the dial axis at one ladder; the cross is
       neither, and it holds.
     - under a PER-ITEM clock the count above exponent 1 moves with the DIAL
       as well as with the gap: gap 5 reads 3, 6, 7 and 8 at alpha = 2, the
       corner, the additive price and m = 2, and gap 3 reads 2, 3 and 4. So
       F5's "1, 1, 3, 6 at gaps 1, 2, 3, 5" is the CORNER DIAL's reading and
       not a function of the gap. What is dial-free is the number ring's own
       corner: the exact and gap-2 ladders read exactly 1 at all 14 of their
       degree-visible cells, and that survives the whole cross. At the
       degree-blind price the gap-2 ladder reads 61, so it is dial-free over
       the price's degree-visible range and not over the family.
       (CORRECTED SINCE, explore_headed_ladder.py F2: this cell was read as
       carrying "a number ring keeps its flat support because its gap is 1 or
       2", and it does not -- a ring's headed places stand at sup 3, 4 and 5,
       where the gap-5 cell carries six coordinates above exponent 1. The
       ring's flat support is F11's arithmetic; this corner is about gaps 1
       and 2 and about nothing else.)
   PR10'S KILL FIRED AND THE MISS IS THE FINDING. At the degree-blind price
   the exact ladder STOPS and keeps its runaway, while every ladder whose gap
   ever EXCEEDS 1 climbs with ZERO runaways under a global clock -- the three
   constant gaps included, so this is not the bounded/unbounded axis wearing
   another hat. So the filed "the degree-blind price kills the limit" is a
   fact about the DOUBLING ladder it was measured at, and the boundary it
   really has is gap 1: there an opening and the recurrent vehicle cost the
   same, the tie-break deepens rather than opens, and one item runs away
   forever. The two ingredients interact, and this is the first pair here
   that does.
   AND THAT PAIR SHARPENS THE STOP LAW ITSELF, which is the more useful half.
   "A bounded gap stops the ladder" is not a statement about the recurrent
   price alone: a stop is the recurrent price sitting below the cheapest
   unopened item's, FOREVER, so it needs the opening-cost curve to grow
   without bound as much as it needs the recurrent price bounded. The
   degree-blind cells are where the second half is visible, being the only
   ones run whose opening curve is FLAT -- price(d, 1) = 1 at every degree --
   and there a bounded gap does not stop the ladder at all. So the law is a
   COMPARISON of two curves and reads as a property of the gap only over
   supplies whose openings get dearer; every cell of F3 has alpha >= 1, which
   is why the condition was invisible there.
   AND THE FATE'S INSTRUMENT WAS A PROXY ALL ALONG. Every section above reads
   "stopped" off a FLAT COST TAIL; the direct reading is whether the walk
   still OPENS degrees. The two agree at 100 of 112 cells and part at exactly
   the 12 degree-blind cells whose gap exceeds 1, where the cost is flat at 1
   forever while the ladder climbs on openings that cost the same as the
   moves. So the proxy is sound wherever the price can see a degree -- which
   is every cell F3 reads -- and both readings are carried here.

F11 A RING NEVER SEATS ITS RAMIFIED PLACE, AND STRANDS ONE THAT IS PLANTED
   WHERE IT CAN AFFORD ITS ONE CHEAP MOVE (rule in range; both rings walked
   from the void seed to the lock and 40 moves past it, plus one planted seed
   per ramified place). The mixed law's one arithmetic consequence, and it is
   testable with the rings already built.
   (SINCE NARROWED, and the surviving scope is the two rings walked here.
   The first clause is geography, not a law: a third quadratic ring, Z[i],
   seats its ramified place from the void UNPLANTED -- there it is the
   cheapest opening at 4, that ring having no place of norm 3 or 4 at all --
   and then strands it at exponent 3. The STRAND is what generalises, and it
   gains its first unplanted instance. What decides the seating is not the
   product this section prices with: the product is what a place charges
   once its ladder is PERIODIC, and F1's own head -- the leading depths at
   the places with p - 1 <= e -- comes first, so a walk pays the head and
   never reaches the tail the product names. explore_gaussian_runaway.py
   findings 1, 2 and 4.)
   From the void, K5 locks on a split place of norm 3 at cost 3 and K23 on one
   of norm 3 at cost 3; the support is FLAT at both -- one place above
   exponent 1 and it is the lock's own vehicle -- and NO ramified place is
   seated at all in either walk. Plant one and the affordable ones strand: K5
   seeded with its ramified place over 2 locks on a split place of norm 7 at
   cost 7 with the planted place STRANDED at exponent 3 and priced 16 there,
   and seeded with its ramified place over 5, stranded at exponent 2 and
   priced 25. Those two prices are the LONE-PLACE ladder read at the depth
   each strand reached -- 25 is the tame place's N^gap at gap 2, and 16 is the
   wild place's HEAD, whose door of 4 at depth 3 F1 already tabulates -- so a
   strand's price is its own ladder's and not the state's. Each is above the
   lock's own cost, which is what makes a strand permanent rather than a
   snapshot: a lock's recurrent cost is flat, measured 40 moves past every
   lock of the norm-40 belts (explore_lock_budget.py).
   THE THIRD RAMIFIED PLACE DOES NOT STRAND, and grading it separately is the
   point. K23's has norm 23 against a lock at 3, so it cannot afford even the
   ONE cheap move a wide item gets; it ends at exponent 1, flat, having never
   moved. The strand needs the wide item's first move to be affordable while
   the budget is still loose, which is hand-attack G(iii)'s condition arriving
   in arithmetic.
   AND A RING IS THE MIXED-LADDER WALKER RATHER THAN AN ANALOGUE OF ONE (rule
   in range; 472 (place, depth) readings over both rings from the void and
   from every planted ramified seed, 0 off; derived after the run). The
   transfer this whole section rests on was untested: F1 reads a LONE place's
   door, while the engine's door is the least r with lambda(P^(e+r)) not
   dividing the WHOLE STATE's invariant -- an LCM over every seated place,
   which can only make a door WIDER, and other places over the same rational
   prime are exactly where it could. It never does, at any reading here. So
   the per-item clock of F5 is a ring's door in a populated state and not only
   at a lone place, which is what lets the product law be read off a ring at
   all.
   (NARROWED SINCE, explore_headed_ladder.py F9: the 472 readings are over
   the TWO rings this file walks, and the conclusion does not survive the
   third. At Z[i]'s locked state the ramified place's door is 7 where its
   lone-place door is 5 -- a number explore_gaussian_runaway.py had already
   printed, as that strand's price of 128 against 32. The carrier is not
   "another place over the same rational prime" as guessed above but a place
   over a DIFFERENT one: the INERT place over 3 has residue field F_9, so
   its lambda carries q - 1 = 8, and that 2-part swallows the two ladder
   steps the place over 2 would have escaped at. What survives is the
   transfer AT THESE TWO RINGS; in general a populated door is at or above
   the ladder's, with the excess set by another place's residue field --
   which no ladder in the family can express.)
   (AND SETTLED SINCE, explore_populated_door.py F1, F4 and F5. The excess
   has a formula, so the transfer is correctable rather than false: a
   seated place's door is the least r with v_p(lambda(P^(e+r))) > v_p(L),
   which makes the state visible to it as ONE integer. The 472 readings
   above measured the SEATED column and not these two rings -- off that
   column both of them widen too, at 20.0% and 12.6% of their unseated
   readings. And the risk guessed here, other places over the same
   rational prime, is the real second route but fires nowhere: no walked
   state seats two places of equal characteristic, so it needs a state
   the walker cannot build.)
   AND IT DOES NOT TOUCH THE FILED IDEAL LIMIT THEOREM, whose exponent ceiling
   (explore_greedy_limit.py L0) is derived from a tick that DOUBLES: there
   every exponent ever written is 0, 1 or the tick at its own clock plus 1, so
   a strand cannot exist. An exact tick is where it can -- a place seated at
   tick + 1 and never cheap again -- and the two results sit on opposite sides
   of the characteristic.
   SO THE CORPUS'S FLAT NUMBER-RING SUPPORT IS NOT SAFE BECAUSE A RING CANNOT
   STRAND. It is safe because the greedy walk never opens a wide place from
   the void, and that is arithmetic: a ramified place's recurrent product is
   N^gap where an unramified one's is N. The strand is real in the ring the
   moment anything else seats a place cheap enough to move once.
   AND IT PRICES THE RING OF RAMIFICATION INDEX 3, which was wanted as the
   first ring whose universe carries a gap-3 ladder at all. The gap-3 ladder's
   dynamics is measured in the schedule (F9), the stranding is measured in
   arithmetic here, and the product law puts a totally ramified place over 2
   at product 2^3 = 8 against unramified norms of 3 -- so it would not take
   the recurrent slot either. What such a ring adds is a strand at gap 3 in a
   real ring: a curiosity, not a mechanism.

F8 WHAT IS LEFT OPEN. (i) Everything is the IDEAL world; an element move
   seats a bundle and no ladder expresses a rider. (ii) The mixed universes of
   F9 are read at ONE supply, one seed and one dial, and the IMAGE (S4) has
   never been enumerated over a mixed universe -- where a strand is a free
   coordinate the image should pay for, as the factor family's strand is.
   (iii) Whether a ladder that is neither eventually-arithmetic nor
   eventually-geometric -- a random or lacunary one -- keeps any of this is
   unasked, and the family admits them. (iv) The global-clock mixed budget is
   measured and not derived: F9's product law is a per-item-clock law, and
   what a shared tick makes of several ladders has no hand-attack. (v) The
   head law of F1 is checked at the three heads two rings happen to have.

RUN RECORD. One process, CPython, no BLAS. Wall 2.0s, peak working set
32.4 MB against the 512 MB ceiling. 76961 checks here, the two ring engines,
the function field's pump, both certified walkers and the orbit-size formula
imported rather than re-implemented. The cost is set by the branched image
enumeration at S4, which is the only section carrying more than one state.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bisect import bisect_left
from fractions import Fraction

import explore_coarse_type as CT
import explore_greedy_image_ec as EC
import explore_greedy_limit as GL
import explore_lock_budget as LB           # the on/off exact-tick walker
import explore_module_law as K23           # the h = 3 number ring
import explore_number_field_lock as K5     # the h = 2 number ring
import explore_price_schedule as PS        # the factor family + its walker
import explore_schedule_image as SI        # the orbit-size formula

CHECKS = 0

LADDER_CAP = 40000   # the largest tick any ladder is built to, asserted against
DEPTH_N = 24         # depths at which a lone place's door is read
CTRL_N = 60          # states of the canonical walk the control compares
WALK_N = 120         # moves of each cell of the ladder/locality grid
WALK_DCAP = 400      # degrees the grid's supply carries
FLAT_TAIL = 40       # trailing menu minima read for flatness
IMAGE_CAP = 4000     # states carried by the image enumeration, asserted against


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ---------------------------------------------------------------- the ladder
class Pump(object):
    """A TICK LADDER: the exponents the clock may stand at. The clock advances
    to the least member at or above the exponent just landed on, so the ladder
    is the whole of the landing rule. 1 is a member of every ladder here,
    which is what makes the initial tick a legal clock position."""

    def __init__(self, tag, members, cap=LADDER_CAP):
        self.tag = tag
        self.S = members
        self.cap = cap
        assert self.S and self.S[0] == 1, "%s: a ladder without 1" % tag
        assert all(b > a for a, b in zip(self.S, self.S[1:])), \
            "%s: an unsorted ladder" % tag

    def next_at(self, e):
        """The least ladder member at or above e."""
        i = bisect_left(self.S, e)
        assert i < len(self.S), \
            "%s: the ladder ran out at exponent %d, so every tick past it " \
            "would be a truncation" % (self.tag, e)
        return self.S[i]

    def gap(self, e):
        """The door of an item at depth e read against its own clock."""
        return self.next_at(e) + 1 - e

    def v(self, a):
        """The valuation this ladder is the jump set of: #{s in S : s < a}."""
        return bisect_left(self.S, a)

    def max_gap(self, upto):
        return max(self.gap(e) for e in range(1, upto + 1))


def p_exact(cap=LADDER_CAP):
    return Pump("exact", list(range(1, cap + 1)), cap)


def p_step(c, cap=LADDER_CAP):
    """Constant gap c: the ladder 1, 1+c, 1+2c, ... -- the shape a place of
    ramification index c carries (hand-attack F)."""
    return Pump("gap %d" % c, list(range(1, cap + 1, c)), cap)


def p_geom(b, cap=LADDER_CAP):
    """The factor family's own ladder: T = 1, then ceil(b * T), which is what
    explore_price_schedule.py's walker iterates."""
    S, T = [1], 1
    while T < cap:
        T = -((-Fraction(b).numerator * T) // Fraction(b).denominator)
        if T == S[-1]:
            break
        S.append(T)
    return Pump("factor %s" % b, S, cap)


def p_squares(cap=LADDER_CAP):
    S, k = [], 1
    while k * k <= cap:
        S.append(k * k)
        k += 1
    return Pump("squares", S, cap)


def p_triangles(cap=LADDER_CAP):
    S, k = [], 1
    while k * (k + 1) // 2 <= cap:
        S.append(k * (k + 1) // 2)
        k += 1
    return Pump("triangles", S, cap)


# ---------------------------------------------------------------- the walker
class PWalk(object):
    """The abstract walker with the landing rule made a LADDER and the clock's
    locality a dial. An item is (degree, slot); cls(item) names its clock, so
    a constant cls is the global clock and the identity is one clock per item.

    `lad` gives each item its OWN ladder, defaulting to the one ladder every
    cell before S5 gives the whole walk. It enters at exactly one place -- the
    landing, where the item that just moved advances its clock along its own
    ladder -- because a door reads the tick and never the ladder.

    Deliberately independent of explore_price_schedule.py's walker, which
    asserts the factor family's own invariants at every move -- e2 == T + 1 at
    a clock move, and a landing lifting the tick by exactly one ladder step --
    both of which a general ladder is entitled to break. Everything else --
    the price, the door, the fresh discount, the covered test, the menu's scan
    economy -- is that walker's, and S1 certifies the copy against it."""

    def __init__(self, npl, sch, pump, cls, dcap, seed=(), lad=None, tag=None):
        self.npl = npl
        self.sch = sch
        self.pump = pump
        self.lad = lad or (lambda k: pump)
        self.tag = tag or pump.tag
        self.cls = cls
        self.dcap = dcap
        self.seat = {}          # degree -> list of exponents
        self.opens = {}         # degree -> fresh discounts spent
        self.opened = []
        self.T = {}             # class -> tick
        self.step = 0
        self.clocks = []        # (step, degree, slot, tick before, tick after)
        # is there anything at all past the degree cap? Where there is not, a
        # scan that runs the whole range is COMPLETE rather than truncated,
        # and where there is, the scan MUST exit by its price rule or the menu
        # it returns is a truncation nothing else here would notice
        self.beyond = any(npl.get(d, 0) for d in
                          range(dcap + 1, max(npl) + 1)) if npl else False
        for d in seed:
            self.seat.setdefault(d, []).append(1)
            self.opens[d] = self.sch.m
            self.T.setdefault(self.cls((d, len(self.seat[d]) - 1)), 1)

    def tick(self, key):
        return self.T.get(self.cls(key), 1)

    def covered(self, d):
        return d in self.sch.born or self.opens.get(d, 0) >= self.sch.m

    def door(self, d, slot, e, kind):
        if kind == "open" and not self.covered(d):
            return 1
        return max(1, self.tick((d, slot)) + 1 - e)

    def menu(self):
        """(cost, sorted ties). The scan stops at the first degree whose door-1
        price already beats the best found, which is sound because price(d, 1)
        is non-decreasing in d -- a property of the schedule, checked once per
        schedule and not assumed here."""
        best, ties = None, []
        d, stopped = 0, False
        while d < self.dcap:
            d += 1
            if best is not None and self.sch.price(d, 1) > best:
                stopped = True
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
        ok(best is not None, "%s: an empty menu" % self.tag)
        ok(stopped or not self.beyond,
           "%s: the menu scan ran to the degree cap %d and the supply has "
           "items past it, so the menu is a truncation"
           % (self.tag, self.dcap))
        return best, sorted(ties)

    def collapse(self, ties):
        """The menu as the identity-free factor-family walker reads it: a
        multiset over (degree, door, kind), an opening carrying the whole
        unseated population of its degree."""
        out = {}
        for _, d, slot, r, kind in ties:
            n = (self.npl[d] - len(self.seat.get(d, []))) if kind == "open" \
                else 1
            out[(d, r, kind)] = out.get((d, r, kind), 0) + n
        return out

    def apply(self, mv):
        cost, d, slot, r, kind = mv
        if kind == "open":
            fresh = not self.covered(d)
            row = self.seat.setdefault(d, [])
            ok(slot == len(row),
               "%s: an opening at degree %d took slot %d of %d"
               % (self.tag, d, slot, len(row)))
            row.append(r)
            if fresh:
                if self.opens.get(d, 0) == 0:
                    self.opened.append(d)
                self.opens[d] = self.opens.get(d, 0) + 1
        else:
            self.seat[d][slot] += r
        e2 = self.seat[d][slot]
        c = self.cls((d, slot))
        t0 = self.T.get(c, 1)
        t = self.lad((d, slot)).next_at(max(t0, e2))
        self.T[c] = t
        if t > t0:
            self.clocks.append((self.step, d, slot, t0, t))
        self.step += 1
        return cost, d, slot, r, kind

    def least_uncovered(self):
        for d in range(1, self.dcap + 1):
            if self.npl.get(d, 0) and not self.covered(d):
                return d
        return None

    def deep_items(self):
        return sorted((d, i, e) for d, row in self.seat.items()
                      for i, e in enumerate(row) if e > 1)

    def shape(self):
        return tuple(sorted((d, tuple(sorted(v)))
                            for d, v in self.seat.items() if v))

    def key(self):
        return (self.shape(), tuple(sorted(self.T.items())),
                tuple(sorted(self.opens.items())))

    def copy(self):
        s = PWalk(self.npl, self.sch, self.pump, self.cls, self.dcap,
                  lad=self.lad, tag=self.tag)
        s.seat = dict((d, list(v)) for d, v in self.seat.items())
        s.opens = dict(self.opens)
        s.opened = list(self.opened)
        s.T = dict(self.T)
        s.step = self.step
        s.clocks = list(self.clocks)
        return s


GLOBAL = lambda k: 0
PERITEM = lambda k: k

# the seed the on/off grid of explore_lock_budget.py runs, carried here so the
# two rigs' cells are the same cells: two items already seated at named
# degrees. Without a seed a bounded-gap walk locks at its very first move on
# the least degree, which is a true lock but too degenerate to read from.
GRID_SEED = (9, 13)


# --------------------------------------------------------- S0 forced failures
def s0_forced(sup):
    """Every check the run leans on, made to fail once."""
    fired = []
    sch = PS.Sched("corner")
    try:
        Pump("bad", [2, 3])
    except AssertionError:
        fired.append("a ladder without 1")
    try:
        Pump("bad", [1, 5, 3])
    except AssertionError:
        fired.append("an unsorted ladder")
    try:
        p_exact(cap=8).next_at(99)
    except AssertionError:
        fired.append("the ladder ran out")
    try:
        w = PWalk(sup, sch, p_exact(), GLOBAL, 20)
        w.apply((1, 1, 3, 1, "open"))
    except AssertionError:
        fired.append("an opening took the wrong slot")
    try:
        ok(1 == 2, "the harness itself")
    except AssertionError:
        fired.append("the harness itself")
    print("  forced failures fired: %d" % len(fired))
    for f in fired:
        print("    - %s" % f)
    ok(len(fired) == 5, "only %d of 5 forced failures fired" % len(fired))


# ------------------------------------------ S1a the ladder is the ring's own
def ticks_from_engine(door, depths):
    """The tick a door sequence names: a door r at depth e lands at e + r, and
    the tick is the exponent one below the landing."""
    return [e + door(e) - 1 for e in depths]


HEAD_SPLIT = DEPTH_N // 2    # depths past which the ladder is read as a tail
KIND_E = {"split": 1, "inert": 1, "ram": 2}   # the ramification index of a kind


def ladder_shape(doors, depths):
    """(gaps, tail gap, head length) of a tick sequence: the gap over the deep
    half is the ladder's own, and a HEAD is the leading depths whose gap
    exceeds it -- what hand-attack F predicts below the boundary e/(p-1)."""
    tk = ticks_from_engine(lambda e: doors[e - 1], depths)
    gaps = [t + 1 - e for e, t in zip(depths, tk)]
    tail = max(gaps[HEAD_SPLIT:])
    head = 0
    for i, g in enumerate(gaps):
        if g > tail:
            head = i + 1
    return gaps, tail, head


def name_tail(tk, head):
    """(the ladder the ticks past a head name, its step). An arithmetic tail
    is a constant-gap ladder and names its own step; a doubling one is the
    factor family's and has none."""
    dist = sorted(set(tk[head:]))
    diffs = set(b - a for a, b in zip(dist, dist[1:]))
    if len(diffs) == 1:
        return "gap %d" % list(diffs)[0], list(diffs)[0]
    if len(dist) > 2 and all(b == 2 * a for a, b in zip(dist, dist[1:])):
        return "factor 2", None
    return "unnamed", None


def s1a_lambda_ladder():
    section("S1a  PR1 -- THE LADDER IS LAMBDA'S JUMP SET, read off both "
            "worlds' engines")
    print("  A lone place deepening with nothing else seated: the door IS the")
    print("  staleness, so the tick it lands under IS the ladder's next")
    print("  member, and the ladder's GAP is what the depth-24 sequence names.")
    print("  Read over every place of both rings' universes, not one per kind.")
    depths = list(range(1, DEPTH_N + 1))
    print("\n  %-5s %-8s %-7s %-9s %-9s %-9s %s"
          % ("ring", "kind", "places", "tail gap", "= index", "with head",
             "head predicted by p-1 <= e"))
    for name, M in (("K5", K5), ("K23", K23)):
        by_kind = {}
        for pl in M.UNIVERSE:
            if M.place_norm(pl) > 200:
                continue
            doors = [M.door_r(pl, e, M.lam_P(pl, e)) for e in depths]
            gaps, tail, head = ladder_shape(doors, depths)
            e_idx = KIND_E[pl[0]]
            row = by_kind.setdefault(pl[0], [0, set(), 0, 0])
            row[0] += 1
            row[1].add(tail)
            row[2] += 1 if head else 0
            row[3] += 1 if pl[1] - 1 <= e_idx else 0
            ok(tail == e_idx,
               "%s %s over %d: the tail gap is %d and the ramification index "
               "is %d: %s" % (name, pl[0], pl[1], tail, e_idx, gaps))
            ok(bool(head) == (pl[1] - 1 <= e_idx),
               "%s %s over %d: head of %d against the boundary p-1 <= e being "
               "%s: %s" % (name, pl[0], pl[1], head, pl[1] - 1 <= e_idx, gaps))
            ok(head <= 2 * e_idx + 2,
               "%s %s over %d: an unbounded head of %d depths"
               % (name, pl[0], pl[1], head))
        for kind in sorted(by_kind):
            n, tails, heads, pred = by_kind[kind]
            print("  %-5s %-8s %-7d %-9s %-9d %-9d %d"
                  % (name, kind, n, ",".join(str(t) for t in sorted(tails)),
                     KIND_E[kind], heads, pred))
    print("\n  and the two worlds' named ladders, at one place of each kind:")
    print("  %-5s %-14s %-30s %-14s %s"
          % ("ring", "place", "door by depth 1..12", "ladder", "gap"))
    rows = []
    for name, M in (("K5", K5), ("K23", K23)):
        for tag, sel in (("split, p odd",
                          lambda p: p[0] == 'split' and p[1] % 2),
                         ("inert", lambda p: p[0] == 'inert'),
                         ("ramified, p odd",
                          lambda p: p[0] == 'ram' and p[1] % 2),
                         ("ramified, p = 2",
                          lambda p: p[0] == 'ram' and p[1] == 2)):
            pl = next((p for p in M.UNIVERSE if sel(p)), None)
            if pl is not None:
                rows.append((name, tag,
                             [M.door_r(pl, e, M.lam_P(pl, e)) for e in depths]))
    R = EC.Ring("ladder probe", 1)
    for d in (1, 2, 3):
        key = ("probe", d)
        R.deg[key] = d
        rows.append(("FF", "degree %d" % d,
                     [R.door_r(key, e, R.lam_pp(d, e)) for e in depths]))
    for name, tag, doors in rows:
        gaps, tail, head = ladder_shape(doors, depths)
        tk = ticks_from_engine(lambda e: doors[e - 1], depths)
        named, step = name_tail(tk, head)
        print("  %-5s %-14s %-30s %-14s %d%s"
              % (name, tag, "".join("%d," % x for x in doors[:12])[:-1],
                 named, tail, "  (head %d)" % head if head else ""))
        ok(named != "unnamed",
           "%s %s: the ticks past the head are neither an arithmetic nor a "
           "doubling ladder: %s" % (name, tag, tk))
        if name == "FF":
            ok(named == "factor 2",
               "%s %s: the function field's ticks are not the doubling ladder"
               % (name, tag))
            ok(all(p_geom(2).next_at(e) == t for e, t in zip(depths, tk)),
               "%s %s: the doubling ladder does not reproduce the ticks: %s"
               % (name, tag, tk))
            ok(tail > DEPTH_N // 3,
               "%s %s: the doubling ladder's gap did not grow: %s"
               % (name, tag, gaps))
        else:
            ok(step == tail,
               "%s %s: the tail ladder steps by %s and its gap is %d"
               % (name, tag, step, tail))
            ok(tail <= 2, "%s %s: a number ring's gap exceeded 2: %s"
               % (name, tag, gaps))
            if not head:
                pump = p_exact() if tail == 1 else p_step(2)
                ok(all(pump.next_at(e) == t for e, t in zip(depths, tk)),
                   "%s %s: the %s ladder does not reproduce the ticks: %s"
                   % (name, tag, pump.tag, tk))
    print("\n  Both rings' unramified kinds land the tick exactly; the ramified")
    print("  kind is the constant-gap ladder at its own ramification index;")
    print("  the function field's is the doubling one. The HEADS are where a")
    print("  ring's own residue characteristic is small enough for the")
    print("  principal units to still be squaring rather than stepping.")


# ------------------------------------------- S1b the walker is the certified one
def s1b_walker_control(supplies, names):
    section("S1b  PR2 -- THE POSITIVE CONTROL: the ladder walker IS the two "
            "certified ones")
    print("  Both comparisons advance the OTHER walker by THIS walker's own")
    print("  move, so no tie convention can make them agree by construction.")
    print("\n  against the factor family's walker (global clock):")
    print("  %-12s %-9s %-7s %-9s %s"
          % ("ladder", "supply", "states", "menus", "ticks"))
    for b in (2, 3, Fraction(3, 2)):
        sch = PS.Sched("b=%s" % b, b=b)
        sch.check_monotone(PS.DEG_CAP)
        pump = p_geom(b)
        for name in names:
            npl = supplies[name]
            dnpl = dict((d, npl[d]) for d in range(1, len(npl)))
            a = PWalk(dnpl, sch, pump, GLOBAL, PS.DEG_CAP)
            bw = PS.Walk(npl, sch, "control/%s" % name)
            for _ in range(CTRL_N):
                ca, ta = a.menu()
                cb, tb = bw.menu()
                ok(ca == cb, "%s/%s: costs %d and %d" % (b, name, ca, cb))
                ok(a.collapse(ta) == tb,
                   "%s/%s: menus %s and %s" % (b, name, a.collapse(ta), tb))
                mv = ta[0]
                a.apply(mv)
                bw.apply((mv[1], mv[3], mv[4]))
                ok(a.T[0] == bw.T,
                   "%s/%s: ticks %d and %d" % (b, name, a.T[0], bw.T))
                ok(dict((d, sorted(v)) for d, v in a.seat.items() if v)
                   == dict((d, sorted(v)) for d, v in bw.seat.items() if v),
                   "%s/%s: the seats parted" % (b, name))
            print("  %-12s %-9s %-7d %-9s %s"
                  % (pump.tag, name, CTRL_N, "equal", "equal"))
    print("\n  against the on/off exact-tick walker, over its own grid:")
    print("  %-12s %-9s %-7s %s" % ("ladder", "clock", "states", "agreement"))
    sch = PS.Sched("alpha=1,b=2,m=1", alpha=1, b=2, m=1)
    npl = dict((d, 2) for d in range(1, WALK_DCAP + 1))
    for pump, exact in ((p_exact(), True), (p_geom(2), False)):
        for ctag, cls in (("global", GLOBAL), ("per item", PERITEM)):
            a = PWalk(npl, sch, pump, cls, WALK_DCAP, seed=GRID_SEED)
            b2 = LB.LocalWalk(npl, sch, cls, dcap=WALK_DCAP, exact=exact,
                              seed=GRID_SEED)
            for _ in range(CTRL_N):
                ca, ta = a.menu()
                cb, tb = b2.menu()
                ok(ca == cb and ta == tb,
                   "%s/%s: the menus parted: %s against %s"
                   % (pump.tag, ctag, ta[:3], tb[:3]))
                a.apply(ta[0])
                b2.apply(tb[0])
                ok(a.seat == b2.seat and a.T == b2.T,
                   "%s/%s: the states parted" % (pump.tag, ctag))
            print("  %-12s %-9s %-7d %s" % (pump.tag, ctag, CTRL_N, "equal"))


# ---------------------------------------------- S2 the gap law (PR3, PR4, PR5, PR6)
def run_cell(npl, sch, pump, cls, seed, n=WALK_N):
    w = PWalk(npl, sch, pump, cls, WALK_DCAP, seed=seed)
    mins, peritem_off, peritem_seen = [], 0, 0
    for _ in range(n):
        best, ties = w.menu()
        mins.append(best)
        w.apply(ties[0])
        if cls is PERITEM:
            for d, row in w.seat.items():
                for i, e in enumerate(row):
                    peritem_seen += 1
                    if w.T.get((d, i), 1) != pump.next_at(e):
                        peritem_off += 1
    return w, mins, peritem_seen, peritem_off


def s2_gap_law(pumps):
    section("S2  PR3, PR4, PR5, PR6 -- WHAT A LADDER DECIDES: the gap against "
            "the ladder's fate, the limit's shape, and the clock's state")
    sch = PS.Sched("alpha=1,b=2,m=1", alpha=1, b=2, m=1)
    sch.check_monotone(WALK_DCAP)
    npl = dict((d, 2) for d in range(1, WALK_DCAP + 1))
    print("  supply: two items at every degree to %d -- a supply that never"
          % WALK_DCAP)
    print("  runs out; seed: items already seated at degrees %s; %d moves."
          % (GRID_SEED, WALK_N))
    print("\n  %-12s %-9s %-8s %-7s %-9s %-13s %-9s %s"
          % ("ladder", "clock", "max gap", "seated", "least unc", "last minima",
             "ladder", "above e=1"))
    out, seen, off = {}, 0, 0
    for pump in pumps:
        for ctag, cls in (("global", GLOBAL), ("per item", PERITEM)):
            w, mins, s, o = run_cell(npl, sch, pump, cls, GRID_SEED)
            seen += s
            off += o
            flat = len(set(mins[-FLAT_TAIL:])) == 1
            deep = w.deep_items()
            mg = max(pump.gap(e) for e in range(1, max(
                [e for _, _, e in deep] + [2]) + 1))
            out[(pump.tag, ctag)] = (mg, len(w.seat), w.least_uncovered(),
                                     flat, deep, mins)
            print("  %-12s %-9s %-8d %-7d %-9s %-13s %-9s %d %s"
                  % (pump.tag, ctag, mg, len(w.seat), w.least_uncovered(),
                     ",".join(str(x) for x in mins[-3:]),
                     "STOPPED" if flat else "climbing", len(deep),
                     "(d%d at e%d)" % (deep[0][0], deep[0][2])
                     if len(deep) == 1 else ""))
    print("\n  PR6: %d (state, item) pairs read on the per-item walks, %d with "
          "a tick\n  that is not next_S of the item's own exponent."
          % (seen, off))
    ok(off == 0,
       "%d of %d per-item ticks are not a function of the exponent"
       % (off, seen))
    # PR3: the bounded-gap ladders stop and the unbounded ones do not, under
    # BOTH clocks -- which puts the ingredient on the gap and not on the tick's
    # exactness, of which the exact ladder is one point
    bounded = ["exact", "gap 2", "gap 3", "gap 5"]
    growing = ["squares", "triangles", "factor 2"]
    for tag in bounded:
        for ctag in ("global", "per item"):
            ok(out[(tag, ctag)][3],
               "%s/%s: a bounded-gap ladder did not stop: %s"
               % (tag, ctag, out[(tag, ctag)][5][-8:]))
            ok(out[(tag, ctag)][2] is not None,
               "%s/%s: the stopped walk left no uncovered degree" % (tag, ctag))
    for tag in growing:
        for ctag in ("global", "per item"):
            ok(not out[(tag, ctag)][3],
               "%s/%s: an unbounded-gap ladder stopped" % (tag, ctag))
    # PR4: the square ladder climbs, and under a GLOBAL clock it climbs slower
    # than the doubling one. Its kill FIRED at the per-item clock, where the
    # order reverses, so that reversal is asserted as the measured fact it is
    # rather than left as the absence of a check.
    ok(out[("squares", "global")][1] < out[("factor 2", "global")][1],
       "global: the square ladder seated %d degrees against the doubling "
       "ladder's %d" % (out[("squares", "global")][1],
                        out[("factor 2", "global")][1]))
    ok(out[("squares", "per item")][1] > out[("factor 2", "per item")][1],
       "per item: the square ladder no longer outseats the doubling one: "
       "%d against %d" % (out[("squares", "per item")][1],
                          out[("factor 2", "per item")][1]))
    for ctag in ("global", "per item"):
        ok(out[("squares", ctag)][1] > out[("gap 5", ctag)][1],
           "%s: the square ladder seated no more than the gap-5 one" % ctag)
    # PR5: a GLOBAL clock keeps the filed limit shape at every ladder here,
    # bounded gap or not; under a PER-ITEM clock the count of runaway
    # coordinates is not flat and not binary -- it moves with the gap.
    for pump in pumps:
        ok(len(out[(pump.tag, "global")][4]) == 1,
           "%s/global: %d items above exponent 1, not 1: %s"
           % (pump.tag, len(out[(pump.tag, "global")][4]),
              out[(pump.tag, "global")][4][:6]))
    # over the CONSTANT-gap ladders the gap is a parameter and the count is
    # non-decreasing in it. Over the growing ones the "max gap" column is read
    # over whatever depth that cell happened to reach, so it is a window and
    # not a parameter, and no ordering is asserted across them.
    const = [(out[(t, "per item")][0], len(out[(t, "per item")][4]))
             for t in bounded]
    ok(all(b >= a for (_, a), (_, b) in zip(const, const[1:])),
       "the per-item runaway count is not non-decreasing in a constant gap: %s"
       % (const,))
    grow = [(t, len(out[(t, "per item")][4])) for t in growing]
    print("\n  per-item runaway coordinates, constant gap as a parameter: %s"
          % ", ".join("gap %d -> %d" % g for g in const))
    print("  and at the growing ladders, where the gap is a window and not a")
    print("  parameter: %s" % ", ".join("%s -> %d" % g for g in grow))
    print("\n  where a stopped walk stops, against the hand-derived "
          "d_deep * sup gap -- and WHETHER the stop is a refusal or a TIE.")
    print("  The recurrent vehicle costs d_deep * gap and the least uncovered")
    print("  degree costs itself, so where the product IS that degree the two")
    print("  are the same price and the canonical walk declines by tie-break.")
    print("  The tie branch is then taken and continued, which is the only way")
    print("  to read what the stop is worth.")
    print("\n  %-12s %-9s %-7s %-8s %-8s %-9s %-9s %s"
          % ("ladder", "clock", "d_deep", "sup gap", "product", "least unc",
             "stop is", "tie branch"))
    sch2 = PS.Sched("alpha=1,b=2,m=1", alpha=1, b=2, m=1)
    for tag in bounded:
        pump = next(p for p in pumps if p.tag == tag)
        for ctag, cls in (("global", GLOBAL), ("per item", PERITEM)):
            mg, nseat, lu, flat, deep, _ = out[(tag, ctag)]
            dd = deep[0][0] if deep else 0
            w, _, _, _ = run_cell(npl, sch2, pump, cls, GRID_SEED)
            best, ties = w.menu()
            tie_open = [t for t in ties if t[4] == "open" and t[1] == lu]
            note = "-"
            if tie_open:
                w2 = w.copy()
                w2.apply(tie_open[0])
                mins2 = []
                for _ in range(WALK_N):
                    b2, t2 = w2.menu()
                    mins2.append(b2)
                    w2.apply(t2[0])
                stopped2 = len(set(mins2[-FLAT_TAIL:])) == 1
                note = "%s at %s" % ("STOPS" if stopped2 else "climbs",
                                     w2.least_uncovered())
                # taking the tie buys exactly one more degree and then the
                # refusal IS strict -- asserted, since the whole reading of a
                # bounded gap turns on the ladder not running away here
                ok(stopped2, "%s/%s: the tie branch did not stop: %s"
                   % (tag, ctag, mins2[-8:]))
                ok(w2.least_uncovered() == lu + 1,
                   "%s/%s: the tie branch's least uncovered degree is %s, not "
                   "%d" % (tag, ctag, w2.least_uncovered(), lu + 1))
            else:
                ok(best < sch2.price(lu, 1),
                   "%s/%s: no tie at the stop and yet the least uncovered "
                   "degree costs %d against a minimum of %d"
                   % (tag, ctag, sch2.price(lu, 1), best))
            print("  %-12s %-9s %-7d %-8d %-8d %-9s %-9s %s"
                  % (tag, ctag, dd, mg, dd * mg, lu,
                     "a TIE" if tie_open else "a refusal", note))


# ------------------------------------------------- S3 the ceiling (PR7)
def check_ratio_forces_growth(pump, upto):
    """The algebraic half of "the ceiling is finite iff the ladder grows at
    least geometrically", checked at every ladder member rather than argued.

    With R = (T + 1)/(T - T_prev) the bound's controlling ratio,
    R/(R - 1) = (T + 1)/(T_prev + 1) exactly, and T/T_prev >= (T+1)/(T_prev+1)
    whenever T >= T_prev. So a ratio bounded by R forces every step of the
    ladder to grow by a factor of at least R/(R - 1) > 1 -- which is what
    "at least geometrically" means, and it is the direction the seven measured
    instances cannot supply on their own."""
    n = 0
    for i in range(1, len(pump.S)):
        T, prev = pump.S[i], pump.S[i - 1]
        if T > upto:
            break
        R = Fraction(T + 1, T - prev)
        ok(R > 1, "%s: a ratio at or below 1 at tick %d" % (pump.tag, T))
        ok(R / (R - 1) == Fraction(T + 1, prev + 1),
           "%s: R/(R-1) is %s and (T+1)/(T_prev+1) is %s at tick %d"
           % (pump.tag, R / (R - 1), Fraction(T + 1, prev + 1), T))
        ok(Fraction(T, prev) >= R / (R - 1),
           "%s: the ladder grew by %s at tick %d, below the R/(R-1) = %s its "
           "own ratio forces" % (pump.tag, Fraction(T, prev), T, R / (R - 1)))
        n += 1
    return n


def bound_at(sch, pump, dmin, T):
    """The largest degree the finite-tick form of hand-attack E allows at the
    ladder member T: the greatest D with f(D, T - T_prev) <= f(d_min, T + 1),
    in exact rationals."""
    i = bisect_left(pump.S, T)
    ok(i < len(pump.S) and pump.S[i] == T,
       "%s: tick %d is not a ladder member" % (pump.tag, T))
    prev = pump.S[i - 1] if i else 0
    lo = T - prev
    rival = sch.price(dmin, T + 1)
    cap = dmin * (T + 8)
    D = dmin
    while D <= cap:
        got = D + lo if sch.add else Fraction(D ** sch.alpha) * lo
        if got > rival:
            return D - 1
        D += 1
    return None


def planted(sch, pump, D, dmin, T):
    """The two-item instrument: one stale item of degree D at the stalest
    exponent the ladder allows at tick T, one unseated item of degree dmin,
    and nothing else in the universe. Both degrees covered, so neither carries
    a discount."""
    i = bisect_left(pump.S, T)
    prev = pump.S[i - 1] if i else 0
    e = prev + 1
    npl = dict((d, 0) for d in range(1, PS.DEG_CAP + 1))
    npl[D] = 1
    npl[dmin] = npl.get(dmin, 0) + 1
    w = PWalk(npl, sch, pump, GLOBAL, PS.DEG_CAP)
    w.opens = {D: sch.m, dmin: sch.m}
    w.seat = {D: [e]}
    w.T = {0: T}
    _, ties = w.menu()
    return any(t[1] == D and t[4] == "move" for t in ties), e


def s3_ceiling(pumps, supplies):
    section("S3  PR7 -- THE DEGREE CEILING WITH THE LADDER AS A PARAMETER")
    print("  The planted two-item menu at three ladder members, against the")
    print("  finite-tick bound f(D, T - T_prev) <= f(d_min, T + 1). Its limit")
    print("  is the filed formula d_min * (b/(b-1))^(1/alpha) at a geometric")
    print("  ladder and diverges wherever the gap is bounded.")
    sch = PS.Sched("alpha=1,b=2,m=1", alpha=1, b=2, m=1)
    print("\n  %-12s %-6s %-26s %-26s %s"
          % ("ladder", "d_min", "largest D accepted", "finite-tick bound",
             "ratio (T+1)/gap"))
    for pump in pumps:
        ticks = [t for t in pump.S if 8 <= t <= 600][:3]
        if len(ticks) < 3:
            ticks = pump.S[2:5]
        for dmin in (1, 2):
            got, adm, rat = [], [], []
            for T in ticks:
                D, acc = dmin, 0
                while D <= dmin * (T + 8):
                    deep, _ = planted(sch, pump, D, dmin, T)
                    if not deep:
                        break
                    acc, D = D, D + 1
                got.append(acc)
                adm.append(bound_at(sch, pump, dmin, T))
                i = bisect_left(pump.S, T)
                rat.append(Fraction(T + 1, T - (pump.S[i - 1] if i else 0)))
            print("  %-12s %-6d %-26s %-26s %s"
                  % (pump.tag, dmin,
                     "  ".join("T=%d:%d" % (t, g) for t, g in zip(ticks, got)),
                     "  ".join("%s" % a for a in adm),
                     "  ".join(str(r) for r in rat)))
            for g, a, T in zip(got, adm, ticks):
                # the bound is not merely respected but ATTAINED: the planted
                # menu accepts exactly the degree hand-attack E allows, at
                # every ladder and every tick read
                ok(a is not None and g == a,
                   "%s at d_min %d, tick %d: the planted menu accepted degree "
                   "%d where the bound is %s" % (pump.tag, dmin, T, g, a))
            if pump.tag == "factor 2":
                ok(adm[-1] == 2 * dmin,
                   "%s at d_min %d: the bound reads %s where the filed formula "
                   "says %d" % (pump.tag, dmin, adm[-1], 2 * dmin))
                # a GEOMETRIC ladder's ratio falls toward b/(b-1), and is the
                # only kind here whose ratio has a limit at all
                ok(rat[-1] < rat[0] and rat[-1] > 2,
                   "%s at d_min %d: the geometric ratio did not fall toward "
                   "b/(b-1): %s" % (pump.tag, dmin, rat))
            else:
                ok(rat[-1] > rat[0],
                   "%s at d_min %d: a non-geometric ladder's ratio did not "
                   "grow: %s" % (pump.tag, dmin, rat))
    steps = sum(check_ratio_forces_growth(p, 4000) for p in pumps)
    print("\n  the ratio's own algebra, checked at %d ladder steps over the %d"
          % (steps, len(pumps)))
    print("  ladders: R/(R-1) = (T+1)/(T_prev+1) exactly, and the ladder's own")
    print("  growth T/T_prev is never below it -- so a BOUNDED ratio forces")
    print("  at-least-geometric growth, which is the direction seven measured")
    print("  instances cannot give.")
    print("\n  and the census the CANONICAL CONTINUATION reads, beside it --")
    print("  one walk per row and not the branched sweep, so it is a lower")
    print("  reading of the census and an upper reading of nothing:")
    print("  %-12s %-9s %-9s %s" % ("ladder", "supply", "clock degrees",
                                    "deep item"))
    for pump in pumps:
        for name in ("F_2[x]", "h5"):
            npl = supplies[name]
            dnpl = dict((d, npl[d]) for d in range(1, len(npl)))
            w = PWalk(dnpl, sch, pump, GLOBAL, PS.DEG_CAP)
            for _ in range(WALK_N):
                _, ties = w.menu()
                w.apply(ties[0])
            census = sorted(set(d for _, d, _, _, _ in w.clocks))
            deep = w.deep_items()
            print("  %-12s %-9s %-9s %s"
                  % (pump.tag, name, ",".join(str(d) for d in census),
                     "d%d at e%d" % (deep[-1][0], deep[-1][2]) if deep
                     else "none"))
            ok(census, "%s/%s: no clock move at all" % (pump.tag, name))


# --------------------------------------------------- S4 the image (PR8)
def reading(w):
    """The shape with the deep coordinate's own exponent FORGOTTEN -- what a
    limit records, a divisor carrying no finite exponent at the place it sends
    to infinity. Two states differing only in how far the clock has carried
    its own item reach one limit (explore_schedule_image.py F4)."""
    if not w.clocks:
        return w.shape()
    _, d, slot, _, _ = w.clocks[-1]
    out = {}
    for dd, row in w.seat.items():
        if not row:
            continue
        out[dd] = sorted(-1 if (dd == d and i == slot) else e
                         for i, e in enumerate(row))
    return tuple(sorted((dd, tuple(v)) for dd, v in out.items()))


def image_at(npl, sch, pump, cls, budget, dcap):
    """(distinct limit readings, summed orbit size) reachable in AT MOST
    `budget` moves, branching on every minimal-cost tie. Cumulative, not read
    at the budget alone: a walk that locks reaches the same reading at every
    later budget, and a count read at one budget would report a branch tree's
    WIDTH where the question is how many limits there are.

    The orbit sum weights each reading by explore_schedule_image.py's
    multinomial, which is a lemma about the SYMMETRY of the move model: the
    walker reads an item only through its degree and its exponent, and under a
    per-item clock its tick is a function of that exponent (PR6), so the
    lemma's premise holds at every ladder here."""
    root = PWalk(npl, sch, pump, cls, dcap)
    live = {root.key(): root}
    by_budget = []
    for step in range(1, budget + 1):
        nxt = {}
        for s in live.values():
            _, ties = s.menu()
            for mv in ties:
                s2 = s.copy()
                s2.apply(mv)
                nxt.setdefault(s2.key(), s2)
        ok(len(nxt) <= IMAGE_CAP,
           "%s: %d states carried, above the cap %d"
           % (pump.tag, len(nxt), IMAGE_CAP))
        live = nxt
        seen = {}
        for s in live.values():
            r = reading(s)
            if r not in seen:
                # the sentinel exponent STAYS in the block: the deep item is a
                # seated item whose identity is a free coordinate, so a degree
                # carrying it beside j flat items contributes n_d * C(n_d-1, j)
                # and not C(n_d, j) (explore_schedule_image.py lemma (b)).
                # Dropping it would undercount by exactly the deep item's own
                # choice, and the sentinel is a fibre of size 1 in the
                # multinomial, which is what makes it come out as that factor.
                seen[r] = SI.orbit_size(dict((d, npl[d]) for d, _ in r),
                                        dict(r))
        by_budget.append((step, frozenset(seen), sum(seen.values())))
    return by_budget


def s4_image(pumps, supplies):
    section("S4  PR8 -- THE IMAGE AT EACH LADDER: whether the set of readings "
            "live at a budget STOPS MOVING")
    print("  Distinct readings of the states LIVE at each budget, the deep")
    print("  coordinate's own exponent forgotten -- read at the budget and not")
    print("  cumulatively, because a state passed through on the way is not a")
    print("  limit and a cumulative count would carry every transient. A set")
    print("  that stops MOVING (not merely stops growing) is then the limit")
    print("  set itself, the support never changing again once a walk locks;")
    print("  a set still moving at the last budget is no image at all. Beside")
    print("  it the orbit sum, the same set with item identities put back.")
    sch = PS.Sched("alpha=1,b=2,m=1", alpha=1, b=2, m=1)
    budgets = (4, 6, 8, 10, 12)
    print("\n  %-12s %-9s %-28s %-9s %s"
          % ("ladder", "supply",
             "readings live at %s" % ",".join(str(b) for b in budgets),
             "the set", "with identities"))
    for pump in pumps:
        for name in ("F_2[x]", "h5"):
            npl = supplies[name]
            dnpl = dict((d, npl[d]) for d in range(1, len(npl)))
            rows = dict((s, (r, t))
                        for s, r, t in image_at(dnpl, sch, pump, GLOBAL,
                                                max(budgets), 24))
            counts = [len(rows[b][0]) for b in budgets]
            settled = rows[budgets[-1]][0] == rows[budgets[-2]][0]
            print("  %-12s %-9s %-28s %-9s %s"
                  % (pump.tag, name, "  ".join(str(c) for c in counts),
                     "SETTLED" if settled else "moving",
                     "  ".join(str(rows[b][1]) for b in budgets)))
            ok(counts[0] >= 1,
               "%s/%s: no reachable reading at all" % (pump.tag, name))
            if pump.max_gap(4000) <= 5:
                # SET equality and not count equality: two different reading
                # sets of one size would read as settled on a count alone
                ok(settled,
                   "%s/%s: a bounded-gap ladder's reading set still moved "
                   "between the last two budgets: %s"
                   % (pump.tag, name, counts))
            else:
                ok(not settled,
                   "%s/%s: an unbounded-gap ladder's reading set settled: %s"
                   % (pump.tag, name, counts))


# -------------------------------------------- S5 the mixed universe (PR9)
def mixed_lad(assign, default):
    """A ladder per ITEM, keyed by degree: `assign` names the wide degrees and
    every other degree stands on `default`. Every cell before this one gives
    the whole walk ONE ladder; a ring gives its unramified places gap 1 and its
    ramified ones gap e in the same walk, so a mixed universe is the only shape
    in this family a ring actually has."""
    return lambda key: assign.get(key[0], default)


def tail_gap(pump, upto=64):
    """The gap an item on this ladder pays FOREVER, which is not the gap at
    every depth. A gap-c item's reachable depths are 1, 2, 2+c, 2+2c, ... --
    the ladder's own members, where the gap falls back to 1, are missed by all
    of them after the first step (hand-attack G).

    Only an ARITHMETIC ladder has such a thing: on a growing one max_gap is a
    window over whatever depths were read and not a tail at all, so the
    ladder's own steps are checked rather than the caller trusted."""
    steps = set(b - a for a, b in zip(pump.S, pump.S[1:]) if b <= upto)
    ok(len(steps) <= 1,
       "%s: a tail gap read off a ladder whose steps are not constant (%s) -- "
       "max_gap is a window there and the item pays no fixed gap"
       % (pump.tag, sorted(steps)))
    return pump.max_gap(upto)


def run_mixed(npl, sch, pump, lad, cls, seed, tag, n=WALK_N):
    """The walk, plus which items moved through its FLAT TAIL -- a locked walk
    moves one item there and that item is the runaway."""
    w = PWalk(npl, sch, pump, cls, WALK_DCAP, seed=seed, lad=lad, tag=tag)
    mins, moves, off, seen = [], {}, 0, 0
    for j in range(n):
        best, ties = w.menu()
        mins.append(best)
        _, d, slot, _, kind = w.apply(ties[0])
        if kind == "move" and j >= n - FLAT_TAIL:
            moves[(d, slot)] = moves.get((d, slot), 0) + 1
        if cls is PERITEM:
            for dd, row in w.seat.items():
                for i, e in enumerate(row):
                    seen += 1
                    if w.T.get((dd, i), 1) != lad((dd, i)).next_at(e):
                        off += 1
    return w, mins, moves, seen, off


def s5_mixed(supplies):
    section("S5  PR9 -- THE MIXED UNIVERSE: one walk whose items do not share "
            "a ladder")
    p1, p3 = p_exact(), p_step(3)
    cells = [("all gap 1", {}, p1),
             ("all gap 3", {}, p3),
             ("gap 3 at d=1", {1: p3}, p1),
             ("gap 3 at d<=5", dict((d, p3) for d in range(1, 6)), p1),
             ("gap 1 at d=1", {1: p1}, p3)]
    sch = PS.Sched("alpha=1,b=2,m=1", alpha=1, b=2, m=1)
    sch.check_monotone(WALK_DCAP)
    npl = dict((d, 2) for d in range(1, WALK_DCAP + 1))
    print("  The S2 cell exactly -- two items at every degree to %d, seeded at"
          % WALK_DCAP)
    print("  degrees %s, %d moves -- with the ladder attached to the ITEM. The"
          % (GRID_SEED, WALK_N))
    print("  two uniform rows re-run the S2 cell, checked move for move below.")
    print("\n  the budget is hand-derived as min over SEATED items of")
    print("  price(degree, the item's own tail gap), and the runaway is a")
    print("  least-product item -- a least PRODUCT and not a least gap, with a")
    print("  tie at the least product broken by the walk and the loser stranded.")
    print("\n  %-14s %-9s %-8s %-9s %-8s %-8s %-7s %s"
          % ("universe", "clock", "budget", "predicted", "runaway", "least unc",
             "above 1", "stranded (degree, gap, product)"))
    seen_all, off_all = 0, 0
    rows = {}
    for tag, assign, dflt in cells:
        for ctag, cls in (("global", GLOBAL), ("per item", PERITEM)):
            lad = mixed_lad(assign, dflt)
            w, mins, moves, seen, off = run_mixed(npl, sch, dflt, lad, cls,
                                                  GRID_SEED, tag)
            seen_all += seen
            off_all += off
            budget = mins[-1]
            flat = len(set(mins[-FLAT_TAIL:])) == 1
            seated = [(d, i) for d, row in w.seat.items()
                      for i in range(len(row))]
            prod = dict((k, sch.price(k[0], tail_gap(lad(k)))) for k in seated)
            pred = min(prod.values())
            deep = [(d, i, e) for d, row in w.seat.items()
                    for i, e in enumerate(row) if e > 1]
            run = sorted(moves, key=lambda k: -moves[k])[0] if moves else None
            strand = [(d, i, e) for d, i, e in deep if (d, i) != run]
            rows[(tag, ctag)] = (budget, pred, run, flat, len(deep), strand,
                                 w.least_uncovered(), prod, lad, w)
            print("  %-14s %-9s %-8d %-9d %-8s %-9s %-7d %s"
                  % (tag, ctag, budget, pred,
                     "d%d" % run[0] if run else "-", w.least_uncovered(),
                     len(deep),
                     ", ".join("d%d g%d p%d" % (d, tail_gap(lad((d, i))),
                                                prod[(d, i)])
                               for d, i, _ in strand) or "-"))
    # the uniform universes must reproduce the S2 cell MOVE FOR MOVE. A
    # regression check on the per-item-ladder plumbing and not an independent
    # control -- S1b owns that, certifying this walker against two others --
    # but it is what "the uniform rows are the control" has to mean if the
    # claim is to be checkable rather than eyeballed across two tables.
    for tag, pump in (("all gap 1", p1), ("all gap 3", p3)):
        for ctag, cls in (("global", GLOBAL), ("per item", PERITEM)):
            a = PWalk(npl, sch, pump, cls, WALK_DCAP, seed=GRID_SEED)
            b = PWalk(npl, sch, pump, cls, WALK_DCAP, seed=GRID_SEED,
                      lad=mixed_lad({}, pump), tag=tag)
            for _ in range(WALK_N):
                ca, ta = a.menu()
                cb, tb = b.menu()
                ok(ca == cb and ta == tb,
                   "%s/%s: the uniform mixed cell parted from the S2 cell at "
                   "step %d: %s against %s" % (tag, ctag, a.step, ta[:2],
                                               tb[:2]))
                a.apply(ta[0])
                b.apply(tb[0])
            ok(a.seat == b.seat and a.T == b.T,
               "%s/%s: the uniform mixed cell's state parted from the S2 cell"
               % (tag, ctag))
    print("\n  the two uniform universes reproduce the S2 cell move for move,")
    print("  %d states each -- a regression check on the ladder-per-item"
          % WALK_N)
    print("  plumbing, S1b owning the independent control.")
    print("\n  PR6 again, now per item's OWN ladder: %d (state, item) pairs on "
          "the\n  per-item walks, %d whose tick is not next_S of its exponent "
          "on its own\n  ladder." % (seen_all, off_all))
    ok(off_all == 0,
       "%d of %d mixed per-item ticks are not a function of the exponent"
       % (off_all, seen_all))
    for key, (budget, pred, run, flat, ndeep, strand, lu, prod, lad, w) \
            in sorted(rows.items()):
        tag, ctag = key
        ok(flat, "%s/%s: a bounded-gap mixed universe did not stop: %s"
           % (tag, ctag, budget))
        if ctag == "per item":
            # the whole of PR9: the flat tail minimum IS the least product,
            # the runaway is a least-product item, and every stranded item's
            # product is at or above the budget -- one BELOW it would be
            # priced to move and not moving, which is the incoherent case
            ok(budget == pred,
               "%s: the flat tail minimum is %d and the least product is %d"
               % (tag, budget, pred))
            ok(run is not None and prod[run] == pred,
               "%s: the runaway %s has product %s, not the least %d"
               % (tag, run, prod.get(run), pred))
            # a strand is stranded at a PRICE or at a TIE, and the two are
            # different objects: a product strictly above the budget is
            # stranded on every branch, while one EQUAL to it sits in the
            # menu's minimum and stands only because the canonical walk breaks
            # the tie elsewhere -- the same tie F3 finds at the stop location.
            # So the law is "at or above", and which half each strand is in is
            # read off the final menu rather than asserted.
            _, ties = w.menu()
            tied = set((t[1], t[2]) for t in ties)
            for d, i, e in strand:
                ok(prod[(d, i)] >= budget,
                   "%s: item (d%d, slot %d) stands at exponent %d with product "
                   "%d BELOW the budget %d, so it is priced to move and does "
                   "not" % (tag, d, i, e, prod[(d, i)], budget))
                ok((prod[(d, i)] == budget) == ((d, i) in tied),
                   "%s: item (d%d, slot %d) has product %d against a budget of "
                   "%d and is %sin the final menu's ties"
                   % (tag, d, i, prod[(d, i)], budget,
                      "" if (d, i) in tied else "not "))
    print("\n  what the mixed cells decide, read against the uniform ones,")
    print("  with each strand split by WHY it stands: a product strictly above")
    print("  the budget is priced out on every branch, one equal to it stands")
    print("  by tie-break alone and another branch carries it on.")
    for tag in ("all gap 1", "all gap 3", "gap 3 at d=1", "gap 3 at d<=5",
                "gap 1 at d=1"):
        b, p, run, _, nd, strand, lu, prod, lad, _w = rows[(tag, "per item")]
        priced = [s for s in strand if prod[(s[0], s[1])] > b]
        print("    %-14s runaway d%-3d gap %d, budget %d, %d above exponent 1 "
              "(%d priced out, %d by tie)"
              % (tag, run[0], tail_gap(lad(run)), b, nd, len(priced),
                 len(strand) - len(priced)))


# ------------------------------ S6 the ladder against the four ingredients (PR10)
DIALS = [("corner", dict()),
         ("alpha=2", dict(alpha=2)),
         ("alpha=0", dict(alpha=0)),
         ("additive", dict(add=True)),
         ("m=2", dict(m=2)),
         ("m=3", dict(m=3)),
         ("born-free", dict(born=())),
         ("born-to-2", dict(born=(1, 2)))]


def run_fate(npl, sch, pump, cls, seed, n=WALK_N):
    """A cell read for the ladder's fate DIRECTLY -- how many degrees the walk
    opens in its last FLAT_TAIL moves -- beside the flat-cost proxy every
    earlier section reads it by, and beside which items MOVE in that tail.

    The second distinction is the one "how many items stand above exponent 1"
    cannot make on its own: an item above exponent 1 that is no longer being
    CLOCKED is a strand and not a runaway, and a cell can carry one while
    nothing runs away at all -- which is exactly what a degree-blind price
    leaves behind (its clock fires in the opening transient and never again).

    The runaway is read off CLOCK MOVES in the walk's second half and not off
    moves taken in its last stretch, because on a climbing walk the runaway's
    own moves grow sparse -- a doubling ladder's deep item can go the whole
    last stretch without moving and is running away all the same."""
    w = PWalk(npl, sch, pump, cls, WALK_DCAP, seed=seed)
    mins, tail_opens = [], 0
    for j in range(n):
        best, ties = w.menu()
        mins.append(best)
        _, d, slot, _, kind = w.apply(ties[0])
        if kind == "open" and j >= n - FLAT_TAIL:
            tail_opens += 1
    deep = w.deep_items()
    clocked = sorted(set((d, slot) for st, d, slot, _, _ in w.clocks
                         if st >= n // 2))
    run = [(d, i, e) for d, i, e in deep if (d, i) in clocked]
    return w, mins, tail_opens, deep, run


def s6_dial_cross(pumps):
    section("S6  PR10 -- THE LADDER CROSSED WITH THE FOUR INGREDIENTS: every "
            "limit and image reading so far sits at one schedule")
    print("  alpha, the discount count m and the born-covered set, each dialled")
    print("  against each ladder under both clocks. The b dial is absent because")
    print("  the LADDER is b: the factor family is one row of the ladder axis.")
    print("  The fate is read DIRECTLY -- openings taken in the last %d moves --"
          % FLAT_TAIL)
    print("  beside the flat-cost proxy the earlier sections read it by; and a")
    print("  RUNAWAY is an item still being CLOCKED in the walk's second half;")
    print("  an item above exponent 1 that is no longer clocked is a STRAND,")
    print("  and a cell can carry one while nothing runs away at all.")
    print("\n  %-12s %-11s %-9s %-9s %-11s %-8s %s"
          % ("ladder", "dial", "clock", "fate", "flat cost", "above 1",
             "runaway"))
    npl = dict((d, 2) for d in range(1, WALK_DCAP + 1))
    out, parted = {}, []
    for pump in pumps:
        for dtag, kw in DIALS:
            sch = PS.Sched(dtag, **kw)
            sch.check_monotone(WALK_DCAP)
            for ctag, cls in (("global", GLOBAL), ("per item", PERITEM)):
                w, mins, tail_opens, deep, run = run_fate(npl, sch, pump, cls,
                                                          GRID_SEED)
                flat = len(set(mins[-FLAT_TAIL:])) == 1
                stopped = tail_opens == 0
                out[(pump.tag, dtag, ctag)] = (stopped, flat, len(deep),
                                               len(run), len(w.seat))
                if stopped != flat:
                    parted.append((pump.tag, dtag, ctag))
                print("  %-12s %-11s %-9s %-9s %-11s %-8d %s"
                      % (pump.tag, dtag, ctag,
                         "STOPPED" if stopped else "climbing",
                         "flat" if flat else "moving", len(deep),
                         "d%d at e%d" % (run[0][0], run[0][2]) if len(run) == 1
                         else ("NONE" if not run else "%d of them" % len(run))))
    bounded = ["exact", "gap 2", "gap 3", "gap 5"]
    blind = ["alpha=0"]
    for (ptag, dtag, ctag), (stopped, flat, ndeep, nrun, nseat) \
            in sorted(out.items()):
        if dtag in blind:
            continue          # the degree-blind price is read on its own below
        if ptag in bounded:
            ok(stopped, "%s/%s/%s: a bounded gap did not stop the ladder"
               % (ptag, dtag, ctag))
        else:
            ok(not stopped, "%s/%s/%s: an unbounded gap stopped the ladder"
               % (ptag, dtag, ctag))
    print("\n  the two readings part at %d of %d cells, and at exactly these:"
          % (len(parted), len(out)))
    print("  %s" % (", ".join("%s/%s/%s" % p for p in parted) or "none"))
    ok(all(p[1] in blind for p in parted),
       "the flat-cost proxy and the direct reading part at a dial whose price "
       "can see a degree: %s" % (parted,))
    seeing = [d for d, _ in DIALS if d not in blind]
    glob = sorted(set(out[(p.tag, d, "global")][3] for p in pumps
                      for d in seeing))
    print("\n  runaway coordinates under a GLOBAL clock over every "
          "(ladder, dial)\n  cell whose price can see a degree, %d cells: %s"
          % (len(pumps) * len(seeing), glob))
    ok(glob == [1],
       "the limit's shape does not survive the dial cross under a global "
       "clock: %s" % (glob,))
    print("  and under a PER-ITEM clock, where the gap is visible to the price,")
    print("  the count above exponent 1 -- runaway plus strands:")
    for dtag in seeing:
        print("    %-11s %s" % (dtag, ", ".join(
            "%s:%d" % (p.tag, out[(p.tag, dtag, "per item")][2])
            for p in pumps)))
    print("\n  THE DEGREE-BLIND PRICE, read on its own because its kill is not")
    print("  the ladder's: at alpha = 0 the price is the staleness alone, so an")
    print("  opening and a gap-1 recurrent vehicle cost the SAME and the ladder")
    print("  climbs on price at every ladder whose gap ever exceeds 1. So the")
    print("  stop is a COMPARISON -- the recurrent price against the cheapest")
    print("  unopened item's -- and against a FLAT opening curve, which is what")
    print("  this dial gives, a bounded gap stops nothing.")
    print("  %-12s %-9s %-9s %s" % ("ladder", "clock", "fate", "runaways"))
    for p in pumps:
        for ctag in ("global", "per item"):
            stopped, flat, ndeep, nrun, nseat = out[(p.tag, "alpha=0", ctag)]
            print("  %-12s %-9s %-9s %d"
                  % (p.tag, ctag, "STOPPED" if stopped else "climbing", nrun))
    ok(out[("exact", "alpha=0", "global")][0]
       and out[("exact", "alpha=0", "global")][3] == 1,
       "the exact ladder at a degree-blind price no longer stops with a "
       "runaway: %s" % (out[("exact", "alpha=0", "global")],))
    for p in pumps:
        if p.tag == "exact":
            continue
        ok(not out[(p.tag, "alpha=0", "global")][0],
           "%s: a degree-blind price stopped a ladder whose gap grows" % p.tag)


# --------------------------------------------- S7 the ring's own strand (PR11)
RING_TAIL = 40       # moves read past the lock, as explore_lock_budget reads them
DOOR_N = 60          # states of each ring walk read for the in-state door


def ring_walk(M, seed, tail=RING_TAIL):
    """(locked state, invariant, lock place, lock cost, steps) walked past the
    lock, or None where the seed does not lock inside the imported cap."""
    got = LB.walk_to_lock(M, dict(seed))
    if got is None:
        return None
    st, L, pl, cost, steps = got
    for _ in range(tail):
        c, (p2, r) = LB.step_once(M, st, L)
        st = LB.apply_move(st, p2, r)
        L = M.lam_state(st)
        cost, pl = c, p2
    return st, L, pl, cost, steps


def strand_prices(M, st, L, pl, cost):
    """Each place standing above exponent 1 that is NOT the recurrent vehicle,
    with its own price at the locked state. A strand stands because that price
    is above the walk's flat budget -- the ring's own reading of the same law
    the mixed cells measure, and what licenses reading a strand as permanent
    rather than as a snapshot: a lock's recurrent cost is flat, measured 40
    moves past every lock of the belts (explore_lock_budget.py)."""
    out = []
    for q, e in sorted(st.items(), key=lambda kv: M.place_norm(kv[0])):
        if e <= 1 or q == pl:
            continue
        r = M.door_r(q, e, L)
        out.append((q, e, r, M.place_norm(q) ** r))
    return out


DOORS = []


def s7_ring_strand():
    section("S7  PR11 -- WHETHER A RING STRANDS ITS OWN WIDE PLACE: the "
            "mixed law's one arithmetic consequence")
    print("  A ring is a mixed universe: gap 1 at every split and inert place,")
    print("  gap e at every ramified one (F1). The mixed law says a wide item")
    print("  cheap enough to take its ONE cheap move and too dear to take a")
    print("  second stands above exponent 1 forever. In the ring a place's price")
    print("  is N(P)^door, so a ramified place's recurrent one is N^2 once past")
    print("  its head -- the wild place's head runs wider, and F1 tabulates it.")
    print("\n  %-5s %-16s %-7s %-8s %-24s %s"
          % ("ring", "lock vehicle", "cost", "seated", "above exponent 1",
             "ramified places (norm, N^2)"))
    for name, M, _ in LB.RINGS:
        got = ring_walk(M, {})
        ok(got is not None, "%s: the void seed no longer locks" % name)
        st, L, pl, cost, steps = got
        above = sorted((M.place_norm(q), q, e) for q, e in st.items() if e > 1)
        rams = sorted((M.place_norm(q), q) for q in M.UNIVERSE if q[0] == 'ram')
        seated_ram = [q for _, q in rams if st.get(q, 0)]
        print("  %-5s %-16s %-7d %-8d %-24s %s"
              % (name, LB.show_place(M, pl), cost,
                 len([q for q, e in st.items() if e]),
                 ", ".join("%s^%d" % (LB.show_place(M, q), e)
                           for _, q, e in above) or "(none)",
                 ", ".join("%s N=%d N^2=%d" % (LB.show_place(M, q), n, n * n)
                           for n, q in rams)))
        # the kill, as an observable: a place other than the lock's own vehicle
        # standing above exponent 1 is a strand, and the corpus files these
        # supports as FLAT
        ok([q for _, q, _ in above] in ([], [pl]),
           "%s: the locked support is not flat -- %s stand above exponent 1 "
           "beside the vehicle %s"
           % (name, [LB.show_place(M, q) for _, q, _ in above],
              LB.show_place(M, pl)))
        print("        ramified places seated at all: %s"
              % (", ".join(LB.show_place(M, q) for q in seated_ram) or "NONE"))
        # and the planted witness: the mixed law's condition is that the wide
        # item be seated at all, so plant one and walk from there
        for n, q in rams:
            got2 = ring_walk(M, {q: 1})
            if got2 is None:
                print("        planted %-4s (N=%d): no lock inside the cap"
                      % (LB.show_place(M, q), n))
                continue
            st2, L2, pl2, cost2, steps2 = got2
            e2 = st2.get(q, 0)
            strands = strand_prices(M, st2, L2, pl2, cost2)
            print("        planted %-4s (N=%d): locks on %-5s at cost %-5d, "
                  "the planted place ends at exponent %d %s"
                  % (LB.show_place(M, q), n, LB.show_place(M, pl2), cost2, e2,
                     "-- STRANDED at price %d" % dict(
                         ((s[0], s[3]) for s in strands))[q]
                     if e2 > 1 and q != pl2 else "-- flat, it never moved"))
            # the strand is PERMANENT and not a snapshot exactly because its
            # own price is above the lock's, whose recurrent cost is flat over
            # every tail the belts were read for (explore_lock_budget.py)
            # AND WHETHER THE RING'S DOOR IS THE ITEM'S OWN LADDER AT ALL in a
            # POPULATED state, which F1 checks only for a LONE place. The
            # engine's door is least r with lambda(P^(e+r)) not dividing the
            # whole state's invariant, and that invariant carries every other
            # seated place -- so it can only be WIDER than the lone-place door,
            # and the mixed law transfers exactly insofar as it is not.
            for sq, se, sr, sc in strands:
                ok(sc > cost2,
                   "%s: %s stands at exponent %d priced %d against a lock at "
                   "%d, so it is not priced out"
                   % (name, LB.show_place(M, sq), se, sc, cost2))
    # AND WHETHER A RING'S DOOR IS THE PLACE'S OWN LADDER AT ALL in a POPULATED
    # state, which F1 checks only for a LONE place and which the mixed law's
    # whole transfer to a ring rests on. The engine's door is the least r with
    # lambda(P^(e+r)) not dividing the WHOLE STATE's invariant, and that
    # invariant carries every other seated place, so it can only come out
    # wider. Read at every state of every walk here rather than at the locked
    # one alone, the locked states carrying only a few seated places between
    # them.
    for name, M, _ in LB.RINGS:
        rams = [q for q in M.UNIVERSE if q[0] == 'ram']
        for seed in [{}] + [{q: 1} for q in rams]:
            st, L = dict(seed), M.lam_state(dict(seed))
            for _ in range(DOOR_N):
                for q, e in st.items():
                    if not e:
                        continue
                    DOORS.append((name, LB.show_place(M, q), e,
                                  M.door_r(q, e, M.lam_P(q, e)),
                                  M.door_r(q, e, L)))
                _, (pl2, r2) = LB.step_once(M, st, L)
                st = LB.apply_move(st, pl2, r2)
                L = M.lam_state(st)
    same = [d for d in DOORS if d[3] == d[4]]
    print("")
    print("  and whether a ring's door IS the place's own ladder in a state")
    print("  with others seated -- F1 reads a LONE place, and the engine's door")
    print("  is against the whole state's invariant, so it can only be wider:")
    print("  %d of %d (place, depth) readings agree." % (len(same), len(DOORS)))
    for name, sh, e, lone, full in DOORS:
        if lone != full:
            print("    %-4s %-5s at exponent %d: lone door %d, in-state door %d"
                  % (name, sh, e, lone, full))
    ok(len(same) == len(DOORS) and DOORS,
       "a ring's in-state door parts from its own ladder at %d of %d readings, "
       "so the mixed law's transfer to a ring is approximate"
       % (len(DOORS) - len(same), len(DOORS)))
    print("  So a ring IS the mixed-ladder walker under a per-item clock, and")
    print("  not merely an analogue of one: what the other places contribute to")
    print("  the invariant never widens a door here.")


# ------------------------------------------------------------------- main
def main():
    supplies, names = {}, []
    for L in CT.build_ladder():
        _, npl, _, _ = GL.universe(L)
        supplies[L.name] = npl
        names.append(L.name)

    pumps = [p_exact(), p_step(2), p_step(3), p_step(5),
             p_triangles(), p_squares(), p_geom(2)]

    section("S0  THE HARNESS FORCED TO FAIL")
    s0_forced(dict((d, 2) for d in range(1, 40)))

    s1a_lambda_ladder()
    s1b_walker_control(supplies, ["F_2[x]", "h5"])
    s2_gap_law(pumps)
    s3_ceiling(pumps, supplies)
    s4_image(pumps, supplies)
    s5_mixed(supplies)
    s6_dial_cross(pumps)
    s7_ring_strand()

    section("SUMMARY")
    print("  %d checks passed." % CHECKS)


if __name__ == "__main__":
    main()
