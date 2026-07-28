"""explore_headed_ladder.py -- the schedule family's ladders have no HEAD,
and every ladder arithmetic actually has does. What the missing ingredient
does to the four laws derived without it.

THE QUESTION. explore_tick_pump.py replaced "the tick grows by a factor b"
with a TICK LADDER -- a set S of exponents the clock may stand at -- and
derived four laws over it: the limit's shape (F5), the degree ceiling (F6),
the stop law (F3, crossed with the dials at F10) and the mixed universe's
min over products (F9). Every ladder it walked is either constant-gap
(S = 1, 1+c, 1+2c, ...) or growing.

But a place's real ladder is neither. explore_head_width.py closes the head:
a place's tick ladder is the orbit of psi(i) = min(p*i, i + e) from 1, with
AT MOST ONE step where psi is not the whole story -- the SPLICE, which sits
on the seat i* = e/(p-1) and exists exactly where f = 1, mu_p is in K_P and
e = (p-1)p^t. So a real ladder has THREE ingredients where the family carries
one:

    S = [1, p, p^2, ..., p^t (= i*), L, L + e, L + 2e, ...],  L = i* + e + w

    (a) the RAMP     1, p, ..., p^t     -- the multiplying regime
    (b) the SPLICE   width w = L - i* - e, zero where no head exists
    (c) the TAIL     constant gap e     -- the only one the family has.

p_step(c) is the tail alone. It is the right ladder for an unramified place
over an ODD prime -- e = 1, and a seat needs e = (p-1)p^t, which at e = 1
means p = 2 -- and for K5's ramified place over 5 (p = 5, e = 2, where
p*1 = 5 exceeds 1 + e = 3, so there is no ramp either). It is the WRONG
ladder for every headed place the corpus has measured, which is nine of the
twenty-four explore_head_width.py reads, and unramified is no defence: a
SPLIT place over 2 sits at e = 1 with the seat at 1 and mu_2 in every
2-adic field, so it carries a head of its own. That is the Q_2 row below,
and it is two of the ninety places the limit corpus walks.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. "The gap", "the
sup gap", "the product", "bounded-gap stops" are the CONSTANT family's
words, and in that family sup gap, tail gap and the recurrent price's own
multiplier are one number. A headed ladder separates them, so every
prediction below is written with them separated or it is not written.

THE DIAL IS GENERATED, NEVER INVENTED, which is the whole gain from
explore_head_width.py: (p, e, w) is read off a local field and psi does the
rest, so a dialled ladder is one a ring HAS. The measured widths imported as
shape (not re-derived here): Q_2 w1, Z[sqrt +-2] w1, K5's place over 2 w2,
Z[i] w3, Z[sqrt -3] w1, Z[2^(1/4)] w2, Z[2^(1/8)] w4. Beside them a
psi-ILLEGAL arm, because a law that only breaks on impossible heads is a law
about the parameterization and not about rings.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 From the head corpus to the schedule family. explore_head_width.py's
    ladder is a LONE place's lambda; the family's is a walker's landing
    rule. explore_tick_pump.py F1 and F11 weld those at HEADLESS ladders --
    F11's 472 readings are what license reading a ring's door off a lone
    place at all. Nothing about a head crosses that weld by inheritance;
    S2 re-reads the item's own gap sequence from the ladder.
 T2 From constant-gap intuition. "sup gap", "tail gap" and "d_deep * gap"
    are the same number in every cell the four laws were measured in. Each
    prediction below names which one it means.
 T3 From the legal arm to the illegal one: nothing. S6 carries no inherited
    expectation, and its whole purpose is that a law breaking only there is
    a different kind of law.
 T4 The widths are IMPORTED as shape. This rig does not re-measure a local
    field; explore_head_width.py owns that and its S4 checks the landings
    against explore_local_clock.py's chart.

THE HAND-ATTACK, on paper before any engine code.

 A. THE ITEM'S OWN GAP SEQUENCE -- the whole mechanism, by induction on
    reachable depth. Under a per-item clock the tick is next_S of the item's
    own exponent (explore_tick_pump.py F5, proved at hand-attack D there), so
    an item at depth x moves to x + gap(x) with gap(x) = next_S(x) + 1 - x.
    From x = 1: every integer in [1, p^t] has next_S at or below p^t, so the
    item climbs the ramp and arrives at exactly p^t + 1 -- one past the seat,
    which is the one depth the ramp cannot land on again. There
    next_S(p^t + 1) = L, so the gap is

        L - (p^t + 1) + 1 = L - i* = e + w,

    paid ONCE. From L + 1 the ladder steps by e and so does the item. So a
    headed ladder gives an item: a ramp of gaps at most e, then EXACTLY ONE
    gap of e + w, then e forever.
    CHECKED BY HAND at two rows before this file existed. (p2, e2, w3), the
    Z[i] ladder S = 1,2,7,9,11: depths 1 -> 2 -> 3 -> 8 -> 10, gaps 1,1,5,2
    -- one gap of e + w = 5. And (p2, e8, w4), S = 1,2,4,8,20,28: depths
    1 -> 2 -> 3 -> 5 -> 9 -> 21 -> 29, gaps 1,1,2,4,12,8 -- one gap of
    e + w = 12.

 B. SO THE HEAD IS EXACTLY WHAT SEPARATES SUP FROM TAIL. sup over all depths
    of gap is e + w, attained at p^t + 1 alone; the tail gap is e. A wide head
    and a wide gap therefore present the SAME longest run for different
    reasons, and the two are told apart by carrying both numbers in
    every row and by running each headed ladder beside BOTH of its headless
    controls: p_step(e), which shares its recurrent price, and p_step(e + w),
    which shares its longest run.

 C. AND THE SPLICE IS A BARRIER THE WALK MUST BUY ITS VEHICLE PAST. A stop
    is the recurrent price sitting below the cheapest unopened item's forever
    (explore_tick_pump.py F10). At a constant ladder the recurrent price is
    d_deep * c from the deep item's first move. At a headed one the deep item
    is cheap on the ramp, then faces d_deep * (e + w) ONCE, and is only worth
    d_deep * e after it. So while openings are cheaper than the splice the
    walk opens instead -- ramping each new degree and abandoning it at
    p^t + 1 -- and it takes the splice only when the least uncovered degree
    has grown dearer than d_deep * (e + w).

 D. HAND-RUN of the S2 cell at the Z[i] ladder, per-item clock, alpha = 1,
    two items at every degree to 400, seed (9, 13), born = {1}. Opens degree
    1 at cost 2; ramps it 2 -> 3 at cost 1; opens degree 1's second slot and
    ramps that; then the splice at degree 1 costs 5 while opening degree 2
    costs 2, so it OPENS. Each new degree d is ramped to exponent 3 at cost
    d and abandoned when 5d exceeds d + 1. Degree 1's splice, at cost 5,
    finally wins the tie against opening degree 5, and the walk then recurs
    at 1 * e = 2 forever. So it STOPS, with the least uncovered degree at
    d_deep * (e + w) = 5 rather than at d_deep * e = 2, and with a STRAND at
    every degree it ramped and abandoned -- in a UNIFORM universe, which
    explore_tick_pump.py F9 needed a MIXED one to produce.
    Same ladder under a GLOBAL clock: the shared tick is 7 after the deep
    item's first ramp step, so every other item's door is 7 and no other
    item is ever cheap to move; the openings run 2, 3, 4 and the splice wins
    the tie at 5. ONE coordinate above exponent 1.

 E. THE CEILING. The finite-tick bound is D <= d_min * (T + 1)/(T - T_prev)
    (explore_tick_pump.py hand-attack E). Along the tail T - T_prev = e and
    T grows, so the ratio diverges exactly as it does at a constant ladder
    and the ceiling stays infinite. At the SPLICE member T = L the previous
    member is i*, so the ratio is (L + 1)/(e + w) -- the one place in the
    whole ladder where the denominator exceeds e. So a head is a one-time
    DIP in the ceiling, and the tightest the bound ever gets.

 F. THE MIXED LAW. explore_tick_pump.py F9's budget is min over seated items
    of f(degree, that item's own tail gap). By C an item only reaches its
    tail gap if the walk paid its splice, so the min should run over CROSSED
    items alone, with d * (e + w) an ADMISSION price to that pool. That is
    the head entering a law's statement rather than perturbing its value.

DISTRUST THE MARGIN. The DERIVED half is A -- an induction on reachable
depths with the arithmetic of psi's ramp under it, and B is bookkeeping on
top of it. The VIBES half is C and D: one hand-run, at one ladder, one
supply, one seed, one schedule, with every tie broken the way this walker
happens to break it. The stop-location prediction rests entirely on it and
is the one to distrust, which is why PR3 names an observable and not a
mechanism.

PREDICTIONS, fixed before any engine code, each naming what the rig PRINTS.
What they mean is weighed after the run.

PR1 THE ITEM'S OWN GAP SEQUENCE. At every psi-legal headed ladder an item
    walking from depth 1 pays gaps of at most e until depth p^t + 1, then
    exactly one gap of e + w, then e forever. What the rig PRINTS: per
    ladder, the (depth, gap) sequence for the first twelve moves, with the
    ramp's end and the splice marked.
    KILL: a splice gap that is not e + w, or more than one gap above e, at
    any legal ladder.

PR2 SUP AND TAIL PART BY EXACTLY THE WIDTH. What the rig PRINTS: per
    ladder, sup gap over all depths, tail gap, their difference, and w.
    KILL: sup - tail differing from w at any legal ladder.

PR3 THE STOP LAW, WITH THE TWO PRODUCTS SEPARATED. Every headed ladder is
    bounded-gap, so it stops under both clocks; and the least uncovered
    degree tracks d_deep * (e + w), the SPLICE, rather than d_deep * e, the
    recurrent price. What the rig PRINTS: per (ladder, clock) the sup and
    tail gaps, the runaway's degree, both products, the least uncovered
    degree, stopped or climbing by the flat-cost proxy AND by openings taken
    in the last stretch, and the two headless controls in the same table.
    KILL: a headed ladder that climbs; or a least uncovered degree sitting
    at the tail product where the two products differ.

PR4 THE LIMIT'S SHAPE. Under a GLOBAL clock exactly one item stands above
    exponent 1 at every headed ladder, as at all seven headless ones. Under
    a PER-ITEM clock the count is not a function of the tail gap: the headed
    (e, w) ladder and the headless gap-e ladder differ. What the rig PRINTS:
    per (ladder, clock) the count above exponent 1, split into the runaway
    (clocked in the walk's second half) and strands.
    KILL: two or more coordinates above exponent 1 at any headed ladder
    under a global clock. None frozen for the per-item half -- the count is
    the observable and the corpus has no prior for it at a headed ladder.

PR5 A HEAD STRANDS IN A UNIFORM UNIVERSE. Under a per-item clock every
    degree the walk ramps and abandons is a strand, and every strand sits at
    depth p^t + 1 -- the ramp's end, where the splice priced it out. What the
    rig PRINTS: per headed ladder, each stranded coordinate with its degree
    and exponent, the ramp's end beside it, and its own splice price.
    KILL: a strand at a depth other than the ramp's end, which would mean
    something other than the splice stopped it.

PR6 THE CEILING DIPS AT THE HEAD. What the rig PRINTS: per headed ladder,
    the finite-tick bound at the ramp's last member, at the splice member
    and at the first three tail members, each with the planted two-item
    menu's verdict at the bound and one degree above it.
    KILL: the planted menu accepting a degree above the bound at any row;
    or the splice member not carrying the smallest bound in its row.

PR7 THE MIXED LAW NEEDS AN ADMISSION PRICE. In a universe mixing headed and
    exact items under a per-item clock, the flat tail minimum is the least
    product over CROSSED items, and no item is in that pool without having
    paid d * (e + w). What the rig PRINTS: per (universe, clock) the flat
    tail minimum, the least product over all seated items, the least product
    over crossed items, the runaway's degree and which ladder it stands on,
    and every strand with its degree, depth and admission price.
    KILL: a flat tail minimum that is not the least product over crossed
    items.

PR8 THE PSI-ILLEGAL ARM. A splice-free ladder at (p2, e2, f1) -- a signature
    where arithmetic GUARANTEES a head, mu_2 lying in every 2-adic field --
    an arithmetic rather than geometric ramp, a splice off the seat, and two
    splices. What the rig PRINTS: the same grid columns as PR3 and PR4, plus
    which of PR1, PR2, PR3 and PR5 hold at each.
    KILL: none frozen. The observable is WHICH laws survive here, since a
    law holding on every legal ladder and breaking only on an illegal one is
    a fact about the parameterization; and one breaking on both is a fact
    about walks.

THE POSITIVE CONTROL (S1, run before any verdict is read). Two instruments,
each against a table it did not write.
  - THE GENERATOR. psi(p = 2, e = 1) must reproduce explore_tick_pump.py's
    exact ladder member for member, and psi(p = 5, e = 2) its gap-2 ladder.
    Those are set identities, so every walker result at them is identical by
    construction rather than by agreement -- the strongest form this control
    has.
  - THE GRID RUNNER. Run at explore_tick_pump.py's own four constant-gap
    ladders it must reproduce that file's filed readings: all four stop
    under both clocks; the least uncovered degree reads 2, 2, 3, 5 at gaps
    1, 2, 3, 5; exactly one coordinate above exponent 1 under a global
    clock; and 1, 1, 3, 6 under a per-item one. A table this rig did not
    write and was not fitted to.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 THE LADDER ENTERS THROUGH TWO NUMBERS, AND A CONSTANT LADDER HAS ONLY
   ONE (rule in range; 7 headed ladders x 2 clocks against their own
   constant-gap controls, 14 of 14 on both readings, plus 4 psi-illegal
   ladders at 8 of 8 on the first). The SUP gap decides where the walk
   STOPS and how many coordinates stand above exponent 1; the TAIL gap
   decides what the runaway PAYS forever. Against the constant ladder of
   its sup, a headed cell agrees on all four aggregate columns -- least
   uncovered degree, runaway count, strand count, fate, at both clocks --
   and DISAGREES on the recurrent budget at every one of the 14, reading
   d_deep * tail where the control reads d_deep * sup. Z[i]'s ladder
   (e = 2, w = 3) stops where gap 5 stops and is priced where gap 2 is
   priced; Z[2^(1/8)] (e8 w4) stops at 12 and is priced at 8.
   SO THE FAMILY WAS AN INGREDIENT SHORT, AND EXACTLY ONE. At a constant
   ladder sup and tail are one number, so no cell in it can say which of
   the two readings takes which -- the head is precisely the separation and
   nothing else. What it is NOT is a new mechanism: given the two numbers,
   every law here is the constant family's, and the ramp's internal shape,
   the splice's position and how many splices there are add nothing (see
   the illegal arm below).
   THE MECHANISM, and it is why both numbers are the item's PRICES rather
   than statistics of the ladder: each is a gap the ITEM LANDS ON and not a
   bound over depths it may skip. An item's reachable depths from 1 climb the ramp to
   exactly p^t + 1, and next_S there is L, so the item pays L - p^t = e + w
   -- the sup -- exactly once (S2, PR1 held at every legal ladder). Asserted
   separately on the illegal arm, where the item's own greatest gap equals
   the ladder's sup at 4 of 4.
   THE ILLEGAL ARM IS WHAT MAKES THE SUP HALF A STATEMENT ABOUT WALKS. A
   reading that held only on psi's orbits would be a fact about the
   parameterization. It holds at a splice-free ladder over a signature
   where arithmetic guarantees a splice, at an arithmetic rather than
   geometric ramp, at a splice three steps ABOVE the seat, and at a ladder
   with TWO overshoots -- where the item pays 5 and then 7 and the cell
   reads as gap 7.

F2 SO THE CORRECTION IS TO THE DICTIONARY, NOT TO THE LAWS: A PLACE HANDS
   THE DYNAMICS e AND e + w, AND THE CORPUS FILES ONLY e (rule in range,
   the 9 headed places of explore_head_width.py F2 against the ladder
   explore_tick_pump.py F1 assigns them). F1 there files the tail gap as
   the ramification index and the constant-gap ladder as what a place of
   ramification index c carries. The tail is right and it is one of the
   two numbers F1 above needs; the sup is the other and is nowhere filed.
   The places measured: K23's two SPLIT places over 2 carry w = 1, so
   their sup is 2 and not 1; Z[sqrt +-2] is 3, K5's ramified place over 2
   is 4, Z[i] is 5, and outside the quadratic range Z[2^(1/4)] is 6 and
   Z[2^(1/8)] is 12. The two coincide at every place with no head -- 15 of
   the 24 places that file reads, and every place of every ring the limit
   corpus itself walks except the three over 2 -- which is why the single
   filed number was never wrong there, only incomplete.
   AND THE ONE FILED CLAIM THIS TOUCHES IS THE SCHEDULE-SIDE ARGUMENT FOR
   THE NUMBER RING'S FLAT SUPPORT, not the result. explore_tick_pump.py
   F10 has "the exact and gap-2 ladders read exactly 1 at all 14 of their
   degree-visible cells, so a number ring keeps its flat support because
   its gap is 1 or 2". A ring's headed places are not at gap 2: they are at
   sup 3, 4 and 5, and the gap-5 cell carries SIX coordinates above
   exponent 1 under a per-item clock. The ring's flat support is measured
   directly and stands -- explore_tick_pump.py F11 walks both rings and
   finds it -- but it stands on that section's ARITHMETIC (the greedy walk
   never opens a wide place from the void, a ramified place's recurrent
   product being N^gap against an unramified N), and not on the
   schedule-side corner, which was reading the wrong ladder. F11's own
   scoping note is the same observation arriving from the other side: "the
   product is what a place charges once its ladder is PERIODIC, and F1's
   own head comes first."

F3 WHAT THE STOP FORMULA MEASURES IS THE BARRIER, NOT THE VEHICLE (rule in
   range; 14 headed cells, the two products distinct at every one). At a
   constant ladder d_deep * sup gap and d_deep * tail gap are one number
   and nothing could tell which the formula meant. A head parts them, and
   the least uncovered degree lands on d_deep * SUP at 14 of 14 and on
   d_deep * tail at none: Z[i] stops at 5 with a recurrent price of 2,
   Z[2^(1/8)] at 12 with a recurrent price of 8. So explore_tick_pump.py
   F3's formula survives verbatim and its READING changes: the stop is set
   by the price the walk must pay ONCE to get its vehicle past the splice,
   and the price the vehicle then pays forever never enters. The walk opens
   degree after degree while the splice is dearer than the cheapest
   opening, and takes the splice at the first degree where it is not.

F4 THE CEILING'S TIGHTEST POINT IS THE HEAD (rule in range; the planted
   two-item instrument at 7 headed ladders x 5 ladder members, the bound
   ATTAINED at 35 of 35 and never exceeded). The finite-tick bound
   f(D, T - T_prev) <= f(d_min, T + 1) is exactly what the planted menu
   accepts at every row. The splice member carries the smallest bound in
   every row -- STRICTLY at six of the seven, and TIED at Q_2, whose e = 1
   puts the seat at 1 so that its ramp has no steps and the member before
   the splice is the seat itself, at the same ratio of 2. At five of the
   seven ladders that bound is d_min itself -- at the splice the walk can
   carry no degree above the least one at all. Along the tail the denominator is e and T grows, so the bound rises
   without limit exactly as at a constant ladder (Z[i]: 1 at the splice,
   then 5, 6, 7), and the ceiling stays infinite. A head is a one-time DIP
   and never a ceiling.

F5 THE MIXED PRODUCT LAW NEEDS AN ADMISSION PRICE, AND NO MEASURED WIDTH
   EXHIBITS IT (rule in range; 6 universes x 2 clocks, the budget equal to
   the least product over CROSSED items at all 6 PER-ITEM cells -- the
   product law is a per-item-clock law and the global cells are not its
   scope, explore_tick_pump.py F9, which the wide universe below shows
   rather than assumes: under a global clock it reads a budget of 122
   against a crossed minimum of 2). An item only
   ever pays its tail gap if the walk bought it past its splice, so
   explore_tick_pump.py F9's min should run over crossed items with
   d * (e + w) the price of admission. At every universe built from a
   MEASURED width the two minima coincide, so F9 as filed is right at every
   width arithmetic has supplied. They part only at a width dialled beyond
   every measured one -- w = 150 at e = 1, product 1 at degree 1 against an
   admission of 151 -- where the all-items minimum reads 1, the
   crossed-items minimum 2, and the budget 2. So the correction is a
   SCHEDULE fact and its arithmetic realizability is not claimed: whether a
   local field carries a width that large is explore_arrival_defect.py F5's
   question (the landing is the avoidance value of the p-power torsion
   constellation) and is not asked here.
   AND THAT CELL IS ALSO PR3 CONFIRMED IN THE NEGATIVE. Under a global
   clock it has not stopped at 120 moves, reading a budget of 122 with
   nothing moving in the flat tail -- which is what F3 predicts, the stop
   sitting at d_deep * sup = 151, beyond the move budget. A ladder does not
   stop late because its gap is unbounded; it stops late because its sup is
   large.

F6 THE GLOBAL LIMIT SHAPE SURVIVES A HEAD; THE PER-ITEM COUNT IS THE SUP'S
   (rule in range; 7 headed ladders, both clocks). Under a global clock
   exactly ONE coordinate stands above exponent 1 at every headed ladder,
   as at all seven headless ones -- explore_tick_pump.py F5's global law
   takes the head without a scratch, and the mechanism is the shared tick:
   after the deep item's first ramp step every other item's door is the
   whole tick and no second item is ever cheap to move. Under a per-item
   clock the count is not a function of the tail gap and IS a function of
   the sup: Z[i] reads 6 where the gap-2 ladder reads 1, and 6 is the gap-5
   ladder's own reading.

F7 PR5 MISSED AND THE MISS IS WHERE THE HEAD ACTUALLY LIVES -- IN THE
   STATE, WHICH THE FOUR LAWS DO NOT READ (rule in range, 7 headed
   ladders). The frozen prediction put every strand at the ramp's END,
   p^t + 1, on the reasoning that the splice is what prices an item out.
   It is wrong because the RAMP'S OWN GAPS RISE: at Z[2^(1/4)] the item
   pays 1, 1, 2, then 6, so an item of high enough degree is priced out at
   the gap of 2 and never reaches the splice at all. Strands sit at depths
   3 and 5 there, and at 3, 5 and 9 at Z[2^(1/8)] -- graded by degree, a
   cheaper item climbing further up the ramp before its next gap outruns
   the budget. A constant-gap ladder puts every strand at depth 2 (the
   hand-attack G(i) reading), so the strand POPULATIONS agree in size with
   the sup-gap control at 14 of 14 while sitting at different depths.
   What survives as the law: a strand sits on the item's own reachable
   path at the first depth whose next move costs at or above the budget,
   and here every one of the 33 strands is priced out STRICTLY, 0 tied,
   over the 6 headed ladders that carry any (Q_2's width of 1 leaves its
   ramp a single depth and it strands nothing) -- where
   explore_tick_pump.py F9's mixed universes carry both kinds.
   SO THE HEAD IS A STATE COORDINATE AND NOT A DYNAMICS ONE. Everything the
   four laws count is the sup gap's; everything about WHERE the counted
   items stand is the ramp's. The corpus has one register that reads the
   state rather than counting it -- the IMAGE (explore_tick_pump.py S4,
   F7) -- and it has never been enumerated over a headed ladder or a mixed
   universe (F8 (ii)). That is where a head would have to show up if it
   shows up anywhere.

F9 AND BOTH NUMBERS ARE THE LONE PLACE'S: A POPULATED RING STATE WIDENS
   THE DOOR PAST THE SUP, WHICH IS WHERE THE SCHEDULE STOPS BEING A RING
   (rule in range; Z[i] walked 60 moves from the void through
   explore_gaussian_runaway.py's own engine, the widening attributed to
   its cause rather than asserted). explore_tick_pump.py F11 checks the
   transfer that everything above rests on -- the engine's door is the
   least r with lambda(P^(e+r)) not dividing the WHOLE STATE's invariant,
   an LCM that can only make a door WIDER -- and reports 472 readings
   with 0 off, concluding that a ring's door in a populated state IS the
   per-item clock of F5. That conclusion is false at the third ring, and
   the refuting number was already printed: explore_gaussian_runaway.py
   records Z[i]'s ramified place stranded at exponent 3 with "its door 7
   and its price 128", where the LONE-place door there is 5 and the price
   32. Two corners held the two halves and neither read the other, F11's
   472 being over the two rings it walks and the Gaussian rig reading its
   7 as a strand price.
   THE MECHANISM IS CROSS-PRIME, and it is why the two rings could not
   show it. Z[i] locks on the INERT place over 3, whose residue field is
   F_9, so its lambda carries q - 1 = 8 -- a 2-part of 2^3 sitting in a
   state invariant otherwise about the place over 2. lambda(P_2^d) reads
   8, 8, 16, 16 at d = 8..11, so the 8 the ladder would have escaped at
   already divides the state and the escape waits for 16 two depths
   later: door 7 from exponent 3, not 5. F11 guessed the risk was "other
   places over the same rational prime"; the actual carrier is a place
   over a DIFFERENT prime, through the residue-field factor.
   SO THE SCOPE OF EVERYTHING ABOVE IS THE SCHEDULE. e and e + w are the
   two numbers a LONE place hands the dynamics, and they are exactly the
   per-item clock's, which is what the whole family is built on. A ring's
   populated door is at or above the ladder's and the gap between them is
   another place's residue field, which no ladder in this family can
   express -- an item's price here depends on its own exponent alone.
   That is a structural limit of the family and not a dial left unturned.

F8 WHAT IS LEFT OPEN. (i) The image over a headed ladder, per F7 -- the
   one register that reads the state. (ii) Whether any local field carries
   a width large enough to separate F5's two minima, which is
   explore_arrival_defect.py's constellation question and not a schedule
   one. (iii) Everything here is the IDEAL world and one supply, one seed
   and one schedule, inheriting explore_tick_pump.py F8 (i) and the dial
   cross's scope; the four laws are re-run at the corner dial and not
   across F10's 112 cells. (iv) The sup half is measured over ladders whose
   sup is ATTAINED on the item's own path; a ladder whose maximising depth
   the item skips is admitted by the family and is not walked here, and
   there the two numbers would not be the item's two prices. (v) F9's
   widening is measured at ONE ring and one state; how far a populated
   door can run above the ladder's, and whether the excess is bounded by
   the state's own residue characteristics, is unasked.

RUN RECORD. One process, CPython, no BLAS. Wall 0.5 s, peak working set
35.8 MB against memwatch.py's 512 MB ceiling. 1166 checks here over 10
psi-generated ladders (7 headed) and 4 psi-illegal ones, with the walker,
the planted ceiling instrument, the mixed-universe runner and both
constant-gap pumps imported from explore_tick_pump.py rather than
re-implemented, and the ring engine from explore_gaussian_runaway.py --
so their own asserts fire underneath these.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction

import explore_gaussian_runaway as GR
import explore_price_schedule as PS
import explore_tick_pump as TP

CHECKS = 0

CAP = TP.LADDER_CAP          # every ladder built to the family's own cap
ITEM_STEPS = 12              # moves of the lone-item walk read at S2
GAP_WINDOW = 256             # depths over which sup gap is read
RING_MOVES = 60              # moves of the Z[i] void walk, well past its lock
WALK_N = TP.WALK_N           # moves per grid cell, the family's own figure
FLAT_TAIL = TP.FLAT_TAIL


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ------------------------------------------------------------ the generators
def psi_orbit(p, e, cap=CAP):
    """The tie-free recursion's orbit from 1 -- the ladder of a place with no
    splice. explore_head_width.py F1: lambda's runs ARE the successive
    differences of the level sequence, and psi is exact wherever no head is
    expected."""
    S, i = [1], 1
    while i < cap:
        nxt = min(p * i, i + e)
        if nxt > cap:
            break
        S.append(nxt)
        i = nxt
    return S


def seat_exp(p, e):
    """t with e = (p-1)p^t, or None. The seat i* = e/(p-1) is a ladder member
    only there, and a splice can only sit on the seat."""
    t, x = 0, p - 1
    while x < e:
        x *= p
        t += 1
    return t if x == e else None


def psi_ladder(tag, p, e, w=0, cap=CAP):
    """A place's ladder as (p, e, w). w = 0 is the splice-free orbit; w >= 1
    puts the head on the seat, at L = i* + e + w."""
    if w == 0:
        return TP.Pump(tag, psi_orbit(p, e, cap), cap)
    t = seat_exp(p, e)
    assert t is not None, "%s: a splice needs a seat, and e is not (p-1)p^t" % tag
    S = [p ** j for j in range(t + 1)]
    x = p ** t + e + w
    while x < cap:
        S.append(x)
        x += e
    return TP.Pump(tag, S, cap)


def profile(pump, upto=GAP_WINDOW):
    """(steps, tail gap, indices of steps above the tail) read off the ladder
    itself, so an illegal ladder is profiled by the same rule as a legal one
    and nothing is taken on the caller's word."""
    steps = [b - a for a, b in zip(pump.S, pump.S[1:]) if b <= upto]
    ok(len(steps) >= 4, "%s: too few steps below %d to read a tail"
       % (pump.tag, upto))
    tail = steps[-1]
    ok(all(s == tail for s in steps[-3:]),
       "%s: the last three steps below %d are %s, so there is no tail gap"
       % (pump.tag, upto, steps[-3:]))
    over = [i for i, s in enumerate(steps) if s > tail]
    return steps, tail, over


def cross_from(pump, upto=GAP_WINDOW):
    """The least depth at which an item is paying its TAIL gap forever -- one
    above the ladder's last step wider than the tail. Below it the item still
    has a splice in front of it, whatever its current gap happens to be: gap 1
    at depth 1 is not a tail on a ladder whose next step is the head."""
    steps, tail, over = profile(pump, upto)
    return pump.S[over[-1] + 1] + 1 if over else 1


def item_walk(pump, steps=ITEM_STEPS):
    """The (depth, gap) sequence an ITEM pays, from a fresh seat at depth 1.
    Under a per-item clock the tick is next_S of the item's own exponent, so
    this is the item's whole price history (explore_tick_pump.py F5)."""
    out, e = [], 1
    for _ in range(steps):
        g = pump.gap(e)
        out.append((e, g))
        e += g
    return out


# ------------------------------------------------------------- the dialled set
# (label, p, e, w) -- w imported as SHAPE from explore_head_width.py F2/F3.
LEGAL = [("psi 2,1 w0", 2, 1, 0),        # every unramified place
         ("psi 5,2 w0", 5, 2, 0),        # K5's ramified place over 5
         ("psi 2,3 w0", 2, 3, 0),        # Z[2^(1/3)]: a ramp, no seat
         ("Q_2 w1", 2, 1, 1),
         ("Z[sqrt2] w1", 2, 2, 1),
         ("K5ram2 w2", 2, 2, 2),
         ("Z[i] w3", 2, 2, 3),
         ("Z[sqrt-3] w1", 3, 2, 1),
         ("Z[2^1/4] w2", 2, 4, 2),
         ("Z[2^1/8] w4", 2, 8, 4)]

HEADED = [r for r in LEGAL if r[3] > 0]


def illegal_ladders(cap=CAP):
    """Ladders psi cannot produce, each with the clause it violates."""
    out = []
    out.append((TP.Pump("no-splice 2,2", psi_orbit(2, 2, cap), cap),
                "the seat is landed at (p2, e2, f1) and mu_2 lies in every "
                "2-adic field, so arithmetic guarantees a splice here"))
    S = list(range(1, 6)) + list(range(8, cap, 3))
    out.append((TP.Pump("narrow ramp", S, cap),
                "an ARITHMETIC ramp; psi's ramp is 1, p, p^2, ... and cannot "
                "step by 1 four times"))
    S = [1, 2, 4, 6] + list(range(12, cap, 2))
    out.append((TP.Pump("late splice", S, cap),
                "a splice three steps ABOVE the seat; psi's only anomalous "
                "step is on the seat"))
    S = [1, 2, 7, 9] + list(range(16, cap, 2))
    out.append((TP.Pump("double splice", S, cap),
                "TWO overshoots; psi is exact up to one step"))
    return out


# ---------------------------------------------------------- the grid harness
def sched():
    s = PS.Sched("alpha=1,b=2,m=1", alpha=1, b=2, m=1)
    s.check_monotone(TP.WALK_DCAP)
    return s


def supply():
    return dict((d, 2) for d in range(1, TP.WALK_DCAP + 1))


def grid_cell(pump, cls, sch=None, npl=None, n=WALK_N):
    """One (ladder, clock) cell, read for every observable the four laws need.

    The fate is read TWICE -- by the flat-cost proxy every earlier section
    uses and by openings taken in the last stretch -- because
    explore_tick_pump.py F10 found the two part at exactly the cells whose
    opening curve is flat, and a headed ladder is a shape neither reading has
    been run at."""
    sch = sch or sched()
    npl = npl or supply()
    w = TP.PWalk(npl, sch, pump, cls, TP.WALK_DCAP, seed=TP.GRID_SEED)
    mins, tail_opens = [], 0
    for j in range(n):
        best, ties = w.menu()
        mins.append(best)
        _, _, _, _, kind = w.apply(ties[0])
        if kind == "open" and j >= n - FLAT_TAIL:
            tail_opens += 1
    deep = w.deep_items()
    clocked = set((d, slot) for st, d, slot, _, _ in w.clocks if st >= n // 2)
    run = [(d, i, e) for d, i, e in deep if (d, i) in clocked]
    strand = [(d, i, e) for d, i, e in deep if (d, i) not in clocked]
    return {"walk": w, "mins": mins, "flat": len(set(mins[-FLAT_TAIL:])) == 1,
            "opens": tail_opens, "deep": deep, "run": run, "strand": strand,
            "lu": w.least_uncovered(), "seated": len(w.seat)}


def row(tag, ctag, pump, c, sup, tail):
    dd = c["run"][0][0] if c["run"] else (c["deep"][0][0] if c["deep"] else 0)
    print("  %-15s %-9s %-4d %-5d %-7d %-7d %-6s %-9s %-6d %d/%d"
          % (tag, ctag, sup, tail, dd * sup, dd * tail, c["lu"],
             "STOPPED" if c["flat"] else "climbing", c["opens"],
             len(c["run"]), len(c["strand"])))
    return dd


HEAD = ("  %-15s %-9s %-4s %-5s %-7s %-7s %-6s %-9s %-6s %s"
        % ("ladder", "clock", "sup", "tail", "d*sup", "d*tail", "leastu",
           "fate", "opens", "run/strand"))


# ------------------------------------------------------- S1 positive control
def s1_control():
    section("S1  POSITIVE CONTROL -- the generator against two certified "
            "pumps, the grid runner against a filed table")
    print("  (a) psi's orbit must BE the family's own ladders, member for")
    print("      member -- a set identity, so the walker agrees by")
    print("      construction and not by coincidence.")
    for tag, p, e, ref in (("exact", 2, 1, TP.p_exact()),
                           ("gap 2", 5, 2, TP.p_step(2))):
        mine = psi_ladder("psi", p, e, 0)
        print("      psi(p=%d, e=%d) vs %-6s : %s ... (%d members each)"
              % (p, e, tag, ",".join(str(x) for x in mine.S[:8]), len(mine.S)))
        ok(mine.S == ref.S,
           "psi(%d,%d) is not the %s ladder: %s vs %s"
           % (p, e, tag, mine.S[:8], ref.S[:8]))

    print()
    print("  (b) the grid runner at the family's four constant-gap ladders,")
    print("      against explore_tick_pump.py F3 and F5's filed readings.")
    print("      %-8s %-9s %-8s %-6s %-8s %-8s %s"
          % ("ladder", "clock", "fate", "leastu", "filed lu", "above e1",
             "filed"))
    filed_lu = {1: 2, 2: 2, 3: 3, 5: 5}
    filed_deep = {("global", 1): 1, ("global", 2): 1, ("global", 3): 1,
                  ("global", 5): 1, ("per item", 1): 1, ("per item", 2): 1,
                  ("per item", 3): 3, ("per item", 5): 6}
    for c in (1, 2, 3, 5):
        pump = TP.p_exact() if c == 1 else TP.p_step(c)
        for ctag, cls in (("global", TP.GLOBAL), ("per item", TP.PERITEM)):
            cell = grid_cell(pump, cls)
            print("      %-8s %-9s %-8s %-6s %-8d %-8d %d"
                  % (pump.tag, ctag, "STOPPED" if cell["flat"] else "climbing",
                     cell["lu"], filed_lu[c], len(cell["deep"]),
                     filed_deep[(ctag, c)]))
            ok(cell["flat"], "%s/%s: a bounded-gap ladder did not stop"
               % (pump.tag, ctag))
            ok(cell["lu"] == filed_lu[c],
               "%s/%s: least uncovered %s against the filed %d"
               % (pump.tag, ctag, cell["lu"], filed_lu[c]))
            ok(len(cell["deep"]) == filed_deep[(ctag, c)],
               "%s/%s: %d above exponent 1 against the filed %d"
               % (pump.tag, ctag, len(cell["deep"]), filed_deep[(ctag, c)]))
    print("      the runner reproduces a table it did not write.")


# ------------------------------------------ S2 the item's own gap sequence
def s2_item_walk():
    section("S2  PR1, PR2 -- WHAT A HEAD DOES TO ONE ITEM: the ramp, the one "
            "splice, and the tail")
    print("  Under a per-item clock the tick is next_S of the item's own")
    print("  exponent, so the gaps below ARE the item's price history divided")
    print("  by its degree. Hand-attack A: at most e up the ramp, exactly one")
    print("  gap of e + w at depth p^t + 1, then e forever.")
    print("  %-15s %-4s %-4s %-4s %-5s %-5s %s"
          % ("ladder", "p", "e", "w", "sup", "tail", "(depth, gap) from 1"))
    out = {}
    for tag, p, e, w in LEGAL:
        pump = psi_ladder(tag, p, e, w)
        steps, tail, over = profile(pump)
        sup = pump.max_gap(GAP_WINDOW)
        walk = item_walk(pump)
        out[tag] = (pump, p, e, w, sup, tail)
        print("  %-15s %-4d %-4d %-4d %-5d %-5d %s"
              % (tag, p, e, w, sup, tail,
                 " ".join("%d:%d" % g for g in walk[:7])))
        ok(tail == e, "%s: the tail gap reads %d and e is %d" % (tag, tail, e))
        ok(sup - tail == w,
           "%s: sup - tail is %d and the width is %d" % (tag, sup - tail, w))
        big = [g for _, g in walk if g > e]
        if w == 0:
            ok(not big, "%s: a splice-free ladder paid a gap above e: %s"
               % (tag, big))
            continue
        ok(len(big) == 1,
           "%s: the item paid %d gaps above e, not one: %s" % (tag, len(big),
                                                               big))
        ok(big[0] == e + w,
           "%s: the splice gap is %d and e + w is %d" % (tag, big[0], e + w))
        t = seat_exp(p, e)
        at = [d for d, g in walk if g > e][0]
        ok(at == p ** t + 1,
           "%s: the splice is paid at depth %d, not at the ramp's end %d"
           % (tag, at, p ** t + 1))
    print("\n  every legal ladder pays its width exactly once, at the ramp's")
    print("  end, and its tail gap forever after.")
    return out


# ------------------------------------------------- S3 the grid (PR3, PR4, PR5)
def s3_grid(prof):
    section("S3  PR3, PR4, PR5 -- THE STOP LAW AND THE LIMIT'S SHAPE, WITH "
            "THE TWO PRODUCTS SEPARATED")
    print("  Each headed ladder beside BOTH headless controls: gap e, which")
    print("  shares its recurrent price, and gap e + w, which shares its")
    print("  longest run. d*sup and d*tail are the two candidate stop")
    print("  locations, equal at every constant ladder and parted by w here.")
    print(HEAD)
    cells = {}
    for tag, p, e, w in LEGAL:
        pump, p, e, w, sup, tail = prof[tag]
        for ctag, cls in (("global", TP.GLOBAL), ("per item", TP.PERITEM)):
            c = grid_cell(pump, cls)
            cells[(tag, ctag)] = (c, sup, tail, p, e, w)
            row(tag, ctag, pump, c, sup, tail)
        if w:
            for ctrl in (TP.p_step(e) if e > 1 else TP.p_exact(),
                         TP.p_step(e + w)):
                cc = grid_cell(ctrl, TP.PERITEM)
                row("  ctrl " + ctrl.tag, "per item", ctrl, cc,
                    ctrl.max_gap(GAP_WINDOW), profile(ctrl)[1])
    print()
    for (tag, ctag), (c, sup, tail, p, e, w) in sorted(cells.items()):
        ok(c["flat"], "%s/%s: a bounded-gap headed ladder did not stop: %s"
           % (tag, ctag, c["mins"][-8:]))
        if ctag == "global":
            ok(len(c["deep"]) == 1,
               "%s/global: %d coordinates above exponent 1, not 1: %s"
               % (tag, len(c["deep"]), c["deep"][:6]))
    print("  PR3, the stop location, at the ladders where the two products")
    print("  differ -- which is every headed one and no headless one:")
    print("  %-15s %-9s %-7s %-7s %-6s %s"
          % ("ladder", "clock", "d*sup", "d*tail", "leastu", "which"))
    for (tag, ctag), (c, sup, tail, p, e, w) in sorted(cells.items()):
        if not w:
            continue
        dd = c["run"][0][0] if c["run"] else 0
        which = ("d*sup" if c["lu"] == dd * sup else
                 "d*tail" if c["lu"] == dd * tail else "neither")
        print("  %-15s %-9s %-7d %-7d %-6s %s"
              % (tag, ctag, dd * sup, dd * tail, c["lu"], which))
        ok(c["lu"] == dd * sup,
           "%s/%s: the walk stops at %s, and d_deep * sup gap is %d"
           % (tag, ctag, c["lu"], dd * sup))
        ok(c["lu"] != dd * tail,
           "%s/%s: the stop is ALSO at d_deep * tail gap %d, so this row "
           "separates nothing" % (tag, ctag, dd * tail))
    print()
    print("  PR5 AS FROZEN MISSED, and the miss is carried rather than")
    print("  patched: a strand does NOT sit at the ramp's end. The ramp's own")
    print("  gaps RISE (1, 1, 2, 6 at Z[2^(1/4)]), so an item is priced out")
    print("  wherever its next gap first outruns the budget, which is a depth")
    print("  ON the ramp and not its end. What is asserted instead is the")
    print("  reading that survives: a strand sits on the item's own reachable")
    print("  path, and its next move costs at or above the budget -- priced")
    print("  out strictly, or sitting in the final menu's own minimum at a")
    print("  TIE (explore_tick_pump.py F9's two kinds).")
    print("  %-15s %-7s %-8s %-10s %-7s %-9s %s"
          % ("ladder", "ramp+1", "strands", "at depth", "budget", "next cost",
             "priced/tied"))
    for tag, p, e, w in HEADED:
        c, sup, tail, p, e, w = cells[(tag, "per item")]
        pump = prof[tag][0]
        end = p ** seat_exp(p, e) + 1
        reach = set(d for d, _ in item_walk(pump, 24))
        budget = c["mins"][-1]
        deps = sorted(set(x[2] for x in c["strand"]))
        costs = [d * pump.gap(x) for d, _, x in c["strand"]]
        priced = len([q for q in costs if q > budget])
        print("  %-15s %-7d %-8d %-10s %-7d %-9s %d/%d"
              % (tag, end, len(c["strand"]),
                 ",".join(str(x) for x in deps[:6]), budget,
                 ",".join(str(q) for q in sorted(set(costs))[:5]),
                 priced, len(costs) - priced))
        for (d, i, x), q in zip(c["strand"], costs):
            ok(x in reach,
               "%s: a strand at degree %d sits at depth %d, which is not on "
               "the item's own reachable path %s" % (tag, d, x, sorted(reach)))
            ok(q >= budget,
               "%s: a strand at degree %d costs %d to move against a budget "
               "of %d, so it is priced to move and is not moving"
               % (tag, d, q, budget))
    print()
    print("  AND THE HEADED CELL AGAINST ITS OWN gap = e + w CONTROL, which is")
    print("  the reading the two products above were separated to make")
    print("  possible. The four AGGREGATE columns agree with the control; the")
    print("  RECURRENT BUDGET does not, and reads the TAIL instead. So the")
    print("  ladder enters through TWO numbers and a constant ladder, having")
    print("  only one, cannot tell which reading takes which.")
    print("  %-15s %-9s %-15s %-15s %-6s %-7s %-7s %s"
          % ("ladder", "clock", "(lu,run,str)", "ctrl e+w", "same?", "budget",
             "ctrl b", "d*tail/d*sup"))
    for tag, p, e, w in HEADED:
        ctrl = TP.p_step(e + w)
        for ctag, cls in (("global", TP.GLOBAL), ("per item", TP.PERITEM)):
            c = cells[(tag, ctag)][0]
            cc = grid_cell(ctrl, cls)
            a = (c["lu"], len(c["run"]), len(c["strand"]), c["flat"])
            b = (cc["lu"], len(cc["run"]), len(cc["strand"]), cc["flat"])
            dd = c["run"][0][0] if c["run"] else 0
            bud, cbud = c["mins"][-1], cc["mins"][-1]
            print("  %-15s %-9s %-15s %-15s %-6s %-7d %-7d %d/%d"
                  % (tag, ctag, str(a[:3]), str(b[:3]),
                     "yes" if a == b else "NO", bud, cbud, dd * e,
                     dd * (e + w)))
            ok(a == b,
               "%s/%s: the headed cell reads %s and its gap-%d control reads "
               "%s" % (tag, ctag, a, e + w, b))
            ok(bud == dd * e,
               "%s/%s: the recurrent budget is %d and d_deep * tail gap is %d"
               % (tag, ctag, bud, dd * e))
            ok(cbud == dd * (e + w),
               "%s/%s: the control's budget is %d and d_deep * sup gap is %d"
               % (tag, ctag, cbud, dd * (e + w)))
            ok(bud != cbud,
               "%s/%s: the budget agrees with the sup-gap control at %d, so "
               "the two readings are not separated here" % (tag, ctag, bud))
    print("  and the STATE is not the same object either: the strand depths")
    print("  above sit on the ramp, where a constant ladder's sit at depth 2.")
    return cells


# ----------------------------------------------------------- S4 the ceiling
def s4_ceiling(prof):
    section("S4  PR6 -- THE CEILING WITH A HEAD IN THE LADDER")
    print("  The finite-tick bound D <= d_min * (T + 1)/(T - T_prev), read at")
    print("  the ramp's last member, the splice member and three tail members,")
    print("  with the planted two-item menu's verdict at the bound and one")
    print("  above it. Along the tail the denominator is e and T grows, so the")
    print("  ratio diverges; at the splice the denominator is e + w.")
    sch = sched()
    print("  %-15s %-8s %-6s %-9s %-7s %-7s %s"
          % ("ladder", "member", "T-Tprev", "ratio", "bound", "accepts",
             "one above"))
    for tag, p, e, w in HEADED:
        pump = prof[tag][0]
        t = seat_exp(p, e)
        seat = p ** t
        L = seat + e + w
        members = [seat, L, L + e, L + 2 * e, L + 3 * e]
        best = None
        for T in members:
            i = pump.S.index(T)
            prev = pump.S[i - 1] if i else 0
            D = TP.bound_at(sch, pump, 1, T)
            hit, _ = TP.planted(sch, pump, D, 1, T)
            over, _ = TP.planted(sch, pump, D + 1, 1, T)
            mark = "  <- splice" if T == L else ""
            print("  %-15s %-8d %-6d %-9s %-7s %-7s %s%s"
                  % (tag if T == members[0] else "", T, T - prev,
                     str(Fraction(T + 1, T - prev)), D, "yes" if hit else "no",
                     "yes" if over else "no", mark))
            ok(hit, "%s: the planted menu refuses the bound %s at tick %d"
               % (tag, D, T))
            ok(not over,
               "%s: the planted menu accepts %s, one above the bound, at tick "
               "%d" % (tag, D + 1, T))
            if T == L:
                best = D
            elif best is not None:
                ok(D > best,
                   "%s: the bound at tail member %d is %s, not above the "
                   "splice's %s" % (tag, T, D, best))
        n = TP.check_ratio_forces_growth(pump, 400)
        ok(n > 0, "%s: no ladder steps checked for the growth identity" % tag)
    print("\n  the splice member carries the smallest bound in every row --")
    print("  strictly, except at Q_2, whose e = 1 seats the ramp at 1 so that")
    print("  the member before the splice IS the seat, at the same ratio. The")
    print("  tail's grows without bound exactly as at a constant ladder.")


# ------------------------------------------------------ S5 the mixed universe
def s5_mixed(prof):
    section("S5  PR7 -- THE MIXED UNIVERSE: does the product law need an "
            "ADMISSION price?")
    print("  A ring gives its unramified places gap 1 and its headed ones the")
    print("  ladder above, in ONE walk. explore_tick_pump.py F9's budget is")
    print("  the least product d * (that item's own tail gap); hand-attack F")
    print("  says the min should run over items that CROSSED their splice,")
    print("  with d * (e + w) the price of admission.")
    head_tag = "Z[i] w3"
    pump, p, e, w = prof[head_tag][0], 2, 2, 3
    ex = TP.p_exact()
    # A width beyond every measured one, at e = 1 so that the headed item's
    # PRODUCT is the least in the universe while its ADMISSION is out of the
    # walk's reach. It is dialled to SEPARATE two quantities that coincide at
    # every realized width, and it is a schedule probe: whether a ring has a
    # width of 150 is not claimed here, only that psi's SHAPE admits one.
    wide = psi_ladder("wide w150", 2, 1, 150)
    sch, npl = sched(), supply()
    cells = [("all exact", {}, ex),
             ("all headed", {}, pump),
             ("headed at d=1", {1: pump}, ex),
             ("headed at d<=5", dict((d, pump) for d in range(1, 6)), ex),
             ("exact at d=1", {1: ex}, pump),
             ("wide w150 at d=1", {1: wide}, ex)]
    print("\n  the headed ladder is %s: %s ... (p%d e%d w%d), and the last"
          % (head_tag, ",".join(str(x) for x in pump.S[:6]), p, e, w))
    print("  cell carries %s: %s ... , product 1 at degree 1 and admission %d."
          % (wide.tag, ",".join(str(x) for x in wide.S[:4]),
             wide.max_gap(GAP_WINDOW)))
    print("  %-17s %-9s %-7s %-8s %-9s %-8s %s"
          % ("universe", "clock", "budget", "min all", "min cross", "runaway",
             "strands"))
    for utag, assign, default in cells:
        lad = TP.mixed_lad(assign, default)
        for ctag, cls in (("global", TP.GLOBAL), ("per item", TP.PERITEM)):
            wk, mins, moves, seen, off = TP.run_mixed(
                npl, sch, default, lad, cls, TP.GRID_SEED,
                "%s/%s" % (utag, ctag))
            ok(off == 0,
               "%s/%s: %d of %d per-item ticks are not next_S of the item's "
               "own exponent" % (utag, ctag, off, seen))
            budget = mins[-1]
            prods, cross = [], []
            for d, r in wk.seat.items():
                for i, x in enumerate(r):
                    lp = lad((d, i))
                    tl = profile(lp)[1]
                    prods.append(d * tl)
                    if x >= cross_from(lp):
                        cross.append(d * tl)
            run = sorted(moves.items())
            print("  %-17s %-9s %-7d %-8d %-9s %-8s %s"
                  % (utag, ctag, budget, min(prods),
                     min(cross) if cross else "-",
                     "d%d" % run[0][0][0] if run else "-",
                     len([1 for d, r in wk.seat.items()
                          for x in r if x > 1]) - len(run)))
            if ctag == "per item":
                ok(cross and budget == min(cross),
                   "%s/per item: the flat tail minimum is %d and the least "
                   "product over crossed items is %s"
                   % (utag, budget, min(cross) if cross else None))
                ok(min(prods) <= budget,
                   "%s/per item: the all-items minimum %d is ABOVE the budget "
                   "%d" % (utag, min(prods), budget))


# ------------------------------------------------------- S6 the illegal arm
def s6_illegal():
    section("S6  PR8 -- THE PSI-ILLEGAL ARM: ladders no place has")
    print("  A law that only breaks on an impossible head is a law about the")
    print("  parameterization. Each row names the clause of the head criterion")
    print("  (f = 1, mu_p in K_P, e = (p-1)p^t, one splice on the seat) that")
    print("  it violates.")
    for pump, why in illegal_ladders():
        steps, tail, over = profile(pump)
        walk = item_walk(pump)
        big = [g for _, g in walk if g > tail]
        print("\n  %-15s %s" % (pump.tag, ",".join(str(x) for x in pump.S[:7])))
        print("    why illegal : %s" % why)
        print("    steps %s tail %d, gaps above tail on the item's own walk: %s"
              % (",".join(str(x) for x in steps[:7]), tail,
                 ",".join(str(x) for x in big) or "none"))
        print("    %s" % " ".join("%d:%d" % g for g in walk[:7]))
        # the mechanism the sup-gap reading rests on: the ladder's sup over
        # ALL depths is a gap the ITEM actually lands on, so "sup gap" is not
        # a quantity the walk merely bounds -- it is one the walk pays
        ok(max(g for _, g in walk) == pump.max_gap(GAP_WINDOW),
           "%s: the item's own greatest gap is %d and the ladder's sup is %d, "
           "so the sup is a bound the walk never pays"
           % (pump.tag, max(g for _, g in walk), pump.max_gap(GAP_WINDOW)))
    print()
    print(HEAD)
    for pump, _ in illegal_ladders():
        sup, tail = pump.max_gap(GAP_WINDOW), profile(pump)[1]
        for ctag, cls in (("global", TP.GLOBAL), ("per item", TP.PERITEM)):
            c = grid_cell(pump, cls)
            row(pump.tag, ctag, pump, c, sup, tail)
    print()
    print("  AND EACH AGAINST ITS OWN gap = sup CONTROL. On the legal arm the")
    print("  headed cell reads exactly as the constant ladder of its sup gap;")
    print("  whether that survives TWO anomalies, an anomaly off the seat and")
    print("  an arithmetic ramp is what decides whether the reading is about")
    print("  psi's shape or about walks.")
    print("  %-15s %-9s %-16s %-16s %s"
          % ("ladder", "clock", "(lu,run,strand)", "ctrl gap=sup", "same?"))
    for pump, _ in illegal_ladders():
        sup = pump.max_gap(GAP_WINDOW)
        ctrl = TP.p_exact() if sup == 1 else TP.p_step(sup)
        for ctag, cls in (("global", TP.GLOBAL), ("per item", TP.PERITEM)):
            c, cc = grid_cell(pump, cls), grid_cell(ctrl, cls)
            a = (c["lu"], len(c["run"]), len(c["strand"]), c["flat"])
            b = (cc["lu"], len(cc["run"]), len(cc["strand"]), cc["flat"])
            print("  %-15s %-9s %-16s %-16s %s"
                  % (pump.tag, ctag, str(a[:3]), str(b[:3]),
                     "yes" if a == b else "NO"))
            ok(a == b,
               "%s/%s: a psi-illegal ladder reads %s where its gap-%d control "
               "reads %s, so the four aggregate columns are not the sup "
               "gap's off psi's orbits"
               % (pump.tag, ctag, a, sup, b))


# ------------------------------------------- S7 the ladder against a real ring
def s7_ring_door():
    section("S7  THE TWO NUMBERS ARE THE LONE PLACE'S, AND A POPULATED RING "
            "STATE CAN WIDEN THE DOOR PAST THE SUP")
    print("  Everything above is the SCHEDULE's ladder, which a per-item clock")
    print("  makes an item's own function of its exponent. The transfer to a")
    print("  RING is explore_tick_pump.py F11: the engine's door is the least")
    print("  r with lambda(P^(e+r)) not dividing the WHOLE STATE's invariant,")
    print("  an LCM that can only make a door WIDER, and F11 finds it never")
    print("  does at 472 readings -- over the two rings it walks. Z[i] is the")
    print("  third ring and it was walked elsewhere, so this checks the")
    print("  transfer where it has not been checked.")
    pl = ("ram", 2)
    lone = GR.door_r(pl, 3, GR.lam_P(pl, 3))
    pump = psi_ladder("Z[i]", 2, 2, 3)
    print()
    print("  the lone place first, which is the instrument's own control:")
    print("    this file's psi ladder gap at depth 3 : %d" % pump.gap(3))
    print("    the ring engine's lone-place door      : %d" % lone)
    ok(pump.gap(3) == lone,
       "the generated ladder gives gap %d at depth 3 and the ring engine's "
       "lone-place door is %d" % (pump.gap(3), lone))
    st, L = {}, 1
    for _ in range(RING_MOVES):
        _, ties = GR.ideal_menu(st, L)
        q, r = ties[0]
        st[q] = st.get(q, 0) + r
        L = GR.lam_state(st)
    e = st.get(pl, 0)
    wide = GR.door_r(pl, e, L)
    print()
    print("  and now in the LOCKED state, %d moves from the void:"
          % RING_MOVES)
    print("    state %s"
          % ", ".join("norm %d at exponent %d" % (GR.place_norm(k), v)
                      for k, v in sorted(st.items(), key=GR.place_key)))
    print("    the ramified place stands at exponent %d" % e)
    print("    door there, lone place    : %d   price %d" % (lone, 2 ** lone))
    print("    door there, in the state  : %d   price %d" % (wide, 2 ** wide))
    ok(e == 3, "the ramified place stands at exponent %d, not 3" % e)
    ok(wide > lone,
       "the populated door is %d and the lone-place door %d, so this state "
       "does not widen anything" % (wide, lone))
    inert = ("inert", 3)
    lam = GR.lam_P(inert, st[inert])
    v = 0
    x = lam
    while x % 2 == 0:
        x //= 2
        v += 1
    print()
    print("  WHERE THE WIDENING COMES FROM, attributed rather than asserted:")
    print("    the lock is the INERT place over 3, whose residue field is F_9,")
    print("    so its lambda carries q - 1 = 8 -- a 2-part of 2^%d in a state" % v)
    print("    invariant otherwise about the place over 2.")
    print("    lambda(ram2^d) for d = 8..11 : %s"
          % ", ".join(str(GR.lam_P(pl, d)) for d in range(8, 12)))
    print("    8 already divides the state, so the escape waits for 16 at")
    print("    depth 10, and the door from exponent 3 is 7 rather than 5.")
    ok(v >= 3,
       "the inert place's lambda carries only 2^%d, so it cannot swallow the "
       "ramified place's next steps" % v)
    ok(GR.lam_P(pl, e + lone) % (2 ** v) == 0,
       "the lone-place escape at depth %d is not divisible by the inert "
       "place's 2-part, so the widening is not this mechanism" % (e + lone))
    ok(GR.door_r(pl, e, lcm_of(GR.lam_P(pl, e), 2 ** v)) == wide,
       "the inert place's 2-part alone does not reproduce the widened door")
    print()
    print("  so the widening is CROSS-PRIME: it comes from a place over 3,")
    print("  through the residue-field factor, which is why the two rings F11")
    print("  walks never showed it -- neither has a place whose q - 1 carries")
    print("  a 2-part this large.")
    return lone, wide


def lcm_of(a, b):
    from math import gcd
    return a * b // gcd(a, b)


def main():
    s1_control()
    prof = s2_item_walk()
    cells = s3_grid(prof)
    s4_ceiling(prof)
    s5_mixed(prof)
    s6_illegal()
    s7_ring_door()
    section("CHECKS")
    print("  %d checks passed here, over %d legal ladders (%d headed) and %d "
          "psi-illegal ones" % (CHECKS, len(LEGAL), len(HEADED),
                                len(illegal_ladders())))


if __name__ == "__main__":
    main()
