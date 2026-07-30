"""explore_ladder_stop.py -- what stops the fresh ladder, and whether a
stopped ladder is enough to make a greedy image finite.

THE QUESTION. The image of a minimal-move policy is sized by three factors:
the MULTIPLICITY at an opening, HOW MANY openings the trajectory has, and how
many of them SURVIVE. The first has had the ring taken out of it -- it is an
orbit count read off a supply of how many items each degree holds
(explore_schedule_image.py). The other two carry the whole cardinality gap:
one limit where nothing ties, a FINITE image where the openings stop, a
continuum where they do not. In the abstract pricing schedule
(explore_price_schedule.py) a degree becomes covered only by being OPENED, so
against a supply with items at every degree the fresh ladder 2, 3, 4, ...
never exhausts and every schedule walked there sprawls. So the question the
orbit count raises against itself: what could stop the ladder, and is a
stopped ladder what makes an image finite?

TWO WAYS TO STOP ONE, and they are different questions.
 (A) CAPACITY. A supply with a TOP DEGREE runs out of fresh capacity: after
     the last degree is opened the ladder is spent and the clock runs alone.
     The schedule family already reaches this regime -- the degree-blind
     corner of explore_price_schedule.py walks it deliberately, and the
     orbit rig's own control sits in it at 40 moves -- but nobody has COUNTED
     there. The orbit sections stop at budgets 8 and 10, well short.
 (B) COVERAGE. The covering rule itself. "An opening covers its own degree
     and nothing else" is the only rule ever run, and it is not the ring's:
     there the test is DIVISIBILITY against the state's own accumulated
     invariant, which can cover many degrees at one stroke. So the covering
     rule is the family's untried ingredient, and a rule that covers fast
     enough could stop the ladder against a supply that never runs out.

THE HAND-ATTACK, on paper before any engine code. Throughout, the CORNER
schedule (price = degree * staleness, b = 2, one fresh discount per degree,
degree 1 born covered) over a supply of n items at each degree 1..D.

 H1 PAST EXHAUSTION THE WALK IS DETERMINISTIC. Once every degree is covered
    the doors are: the deep item at price d_deep * T/2 (its exponent standing
    at T/2 + 1 since its last clock), a flat item of degree d at d * T, and an
    unseated item at a covered degree at d * (T + 1). With d_deep = 1 the
    first is strictly least, and it stays least after the clock doubles, since
    every price in the list scales with T. So the only move ever taken again
    is the deep item's own re-clock.
 H2 SO THE READING SET IS CONSTANT PAST EXHAUSTION while the CONFIGURATION
    set is not. The re-clock raises the one exponent a limit forgets and
    touches nothing else, so at every later budget the reachable states are
    the same limits with a bigger deep exponent. The observable is therefore
    the READING set and not the configuration set, and it must agree as a SET
    and not merely in size.
 H3 AND THE EXHAUSTED IMAGE HAS A CLOSED FORM. Degree 1 is never FLAT: being
    born covered its door is never 1, so every degree-1 seating lands at
    T + 1 and is a clock move. And the deep item's degree is at most
    2 * d_min = 2 (the ceiling of explore_price_schedule.py, at b = 2 and
    price = d * sigma). So an exhausted state is one of exactly two families:

      (i)  deep at degree 1, n ways, beside ONE flat item at each of the
           D - 1 degrees 2..D, n^(D-1) ways;
      (ii) deep at degree 2, n ways, degree 1 empty, beside one flat item at
           each of the D - 2 degrees 3..D, n^(D-2) ways.

    They differ in whether degree 1 is seated at all, so no reading is shared,
    and the exhausted image is

      n^D + n^(D-1)  =  n^(D-1) * (n + 1).

    Two consequences, and the second is why this is worth running. A supply
    with NO ties at all (n = 1) still has an image of 2, the void tie being
    between DEGREES rather than between items. And a two-wide supply gives
    3 * 2^(D-1), which is NOT a power of 2 -- so if the ring's finite images
    are powers of 2, capacity exhaustion is not the mechanism behind them.
    (That last step is the freeze's INFERENCE and F3 narrows it: the factor
    of 3 is the void tie's, which every supply here is built to have, so the
    step holds only where that tie does. Left standing as frozen, since what
    a slate predicted is the record.)
    HOW THIS FORM WAS FOUND, so the run cannot be read as having discovered
    it and the freeze cannot be read as cleaner than it was: a COST probe run
    to choose the enumeration budgets printed the totals at (n, D) = (2, 8)
    and (3, 6), and the form above was derived from the move model afterwards
    to explain them. It is asserted at every row of the grid below, five of
    whose seven rows the probe never ran.
 H4 THE RING'S OWN COVERING RULE CANNOT STOP THE LADDER, and the reason is a
    theorem rather than a measurement. Read as a covering rule, the ring's
    test is that (base^d - 1) divide the accumulated invariant of the seated
    set. BANG's theorem -- the base-2 case of Zsygmondy -- gives 2^d - 1 a
    prime factor that no smaller 2^e - 1 carries, for every d but 1 and 6. A
    prime that enters the invariant only by opening d itself cannot be there
    before d is opened, so no degree but 6 can ever be covered for free, and
    6 needs a SQUARE of 3 that an LCM of smaller terms does not supply. Hence
    two dials, not one: the LCM reading is the ring's, and it frees nothing;
    the PRODUCT reading is strictly more generous and should free exactly 6.
    Either way the ladder opens every degree, and the covering rule is
    exonerated as the thing that locks a number ring.
    (That last clause is where this slate says "the ring" for what is only
    the FUNCTION FIELD's rule -- integer degrees over one base -- and F5
    reverses it: a number ring's degrees are log-norms over residue-field
    orders sharing no base, so the exoneration reaches exactly the world that
    does not lock. Left standing as frozen, the slate's own vocabulary being
    the thing a transplant flag exists to catch and this one having got past
    all five.)
 H5 A RULE WHOSE COVERED SET GROWS WITH THE CLOCK CAN STOP IT. Take "d is
    covered while d <= c * T". The least uncovered degree is then
    floor(c*T) + 1 at price floor(c*T) + 1, against the deep item's
    d_deep * T / 2. At d_deep = 1 the ladder is beaten once c >= 1/2; at
    d_deep = 2 the deep move costs T and the ladder is beaten only once
    c >= 1. So the threshold is branch-dependent, which is the sharpest
    prediction here and the one most likely to be wrong.

THE ONE INGREDIENT THAT DOES NOT TRANSLATE, named at the freeze. The abstract
walker gives the fresh discount to OPENINGS only; a seated item is priced by
the clock even where its degree still has a discount left. The alternative --
door 1 for every item of an uncovered degree -- is not expressible in the
imported move model at all (a discounted deepening would land above exponent 1
without raising the tick, which that walker asserts against), and is argued
degenerate where it is defined. So every claim here about a ladder stopping is
a claim about THAT discount, and at m = 1 -- which is every schedule run
here -- the two readings agree on every reachable state anyway.

TRANSPLANT FLAGS, fixed at the freeze.
 1. From the ring's LOCK to the schedule's stopped ladder: NOTHING is carried.
    A number ring locks by a recurrent vehicle in its class dynamics; a
    schedule stops by capacity or by coverage. They are named as different
    mechanisms and no section here claims they are one. What the rig can say
    is whether either schedule mechanism reproduces the ring's NUMBER.
 2. From the budgets 8 and 10 to the post-exhaustion regime: NOTHING. The
    orbit law was verified only where openings recur, and its argument does
    not read the regime -- but past exhaustion is a regime it has never been
    run in, so it is re-checked at every budget here rather than assumed.
 3. From the ideal world to the element world: nothing, as in the rig this
    one imports. A rider raises an exponent with no clock move and no dial of
    this family has that shape.
 4. The covering rules other than the imported one are ABSTRACT. "Opening d
    covers its multiples" and "d is covered while d <= c * T" are legal dials
    of the schedule family and are not certified to be any ring's rule; the
    cyclotomic pair is the one that is meant to be the ring's, and it is run
    against a theorem rather than against a ring.
 5. The supplies called INFINITE are finite in the rig -- items at every
    degree to a cap far above where the walk reaches. What is asserted is
    that the ladder never came near the cap, so the supply's own top is not
    what stopped anything.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 THE COVERING-RULE WALKER IS THE IMPORTED ONE. What the rig PRINTS: at
    rule "self" over the ring supplies, the number of states at which the
    covering walker's cost, menu and tick were compared against the imported
    identity-free walker's, and the final tick of each. And, past exhaustion
    on a finite toy supply, the identified walker's collapsed menu against the
    identity-free one over 40 moves.
    KILL: one disagreement in cost, in any type's multiplicity, or in a tick.
PR2 THE READING SET IS CONSTANT PAST EXHAUSTION. What the rig PRINTS: per
    supply and per budget past the exhaustion point, the states, the
    configurations, the distinct limit readings, and whether the reading SET
    equals the previous budget's. Every budget also runs the orbit check.
    KILL: two budgets past exhaustion whose reading sets differ; or one shape
    whose configuration count is off its multinomial.
PR3 THE EXHAUSTED IMAGE IS n^(D-1) * (n + 1). What the rig PRINTS: over a
    grid of widths n and top degrees D, the openable degrees, whether every
    reachable state has opened all of them, the reading count, the closed
    form, and the count's factorisation.
    KILL: one row off the closed form.
PR4 THE POWER OF 2 IS THE WIDTH'S. What the rig PRINTS: the same grid read as
    a question about arithmetic -- whether the exhausted image is a power of 2
    at n = 2 and what it is at n = 3 and n = 4.
    KILL: the image a power of 2 at every width, which would mean the width
    is not what sets it.
PR5 WHICH COVERING RULES STOP THE LADDER. What the rig PRINTS: per rule, over
    a supply with items at every degree far past the walk's reach, the total
    fresh opens, the step of the LAST one, the opens in the final third of the
    walk, the final tick, the highest degree opened, and -- at the walk's last
    state -- the cheapest fresh opening the supply still offers against the
    menu's own minimum. The rule "self" is the positive control and must NOT
    stop; "divisors" and the LCM rule must open the same degrees as "self";
    "multiples" must open exactly the primes in range and must not stop; the
    tick rules are read at c = 1/4, 1/2 and 1 on both void branches.
    KILL: no rule stops the ladder; or the control stops; or a stopped ladder
    stopped while the cheapest fresh opening on offer cost no more than the
    move it took, which would be a stop on something other than price.
    ONE OBSERVABLE WAS REPLACED BEFORE ANY VERDICT WAS READ, and it is
    recorded here rather than quietly fixed. The first form was "no fresh open
    in the final third of a long walk", with no price beside it. Under a rule
    whose covered set grows with the CLOCK that is unreadable: the tick
    doubles, so within a dozen moves it passes the supply's top degree, after
    which NO uncovered degree exists at all and a ladder that stopped on price
    prints exactly what a ladder that ran out of supply prints. So the walks
    under those rules are short by design, the price comparison is carried at
    every state, and the existence of something left to decline is asserted at
    every state of every walk.
PR6 THE CYCLOTOMIC RULE FREES ONLY WHAT BANG ALLOWS. What the rig PRINTS: for
    the LCM and PRODUCT readings at bases 2 and 3, the degrees covered without
    ever being opened, within the ladder's own reach.
    KILL: the LCM reading frees anything at base 2; or the PRODUCT reading at
    base 2 frees anything other than degree 6.
PR7 A STOPPED LADDER GIVES A FINITE IMAGE AGAINST AN UNEXHAUSTED SUPPLY. What
    the rig PRINTS: under the stopping tick rule, over supplies of width 1, 2
    and 3 with items at every degree far past the walk's reach, the reading
    count at three budgets, whether the set is constant, the highest degree
    the ladder reached, and the count's factorisation.
    KILL: the reading count still growing at the last budget.

FINDINGS (tiers below; run record at the bottom). Every section asserts,
including the readout of the closed form, which is checked at every row rather
than printed beside it.

F1 A STOPPED LADDER IS ENOUGH TO MAKE A SCHEDULE'S IMAGE FINITE -- ENOUGH AND
   NOT NEEDED -- AND THE OBJECT THAT STOPS IS THE READING AND NOT THE
   CONFIGURATION (proved for the corner
   schedule -- H1 and H2 -- and a rule in range: two supplies at four and
   three budgets past their exhaustion points, the reading sets equal as SETS
   and not merely in size, exhaustion asserted at every one of them rather
   than presumed from the budget, and the orbit law re-checked at every one of
   the seven). Past exhaustion the walk is deterministic: 384 readings at
   every budget from 14 to 20 on a supply of 2 items at each of degrees 1..8,
   and 972 from 12 to 16 on 3 items at each of 1..6. The control walks the
   same two supplies 40 moves, well past their exhaustion points, to ticks of
   8.6e9 and 3.4e10 with the last move costing 2.1e9 -- the ladder spent and
   the clock running alone. The configurations do keep
   moving -- the deep exponent doubles at every step -- so a count of STATES
   would have said the image grows forever where the count of LIMITS is
   constant. That is the same correction the sum over shapes already needed,
   arriving here as the whole difference between a finite image and an
   infinite one rather than as a small overcount.
   ENOUGH AND NOT NEEDED, and the counterexample is one line: only a TIED
   opening multiplies anything, so a supply of ONE item per degree has an
   image of 2 however long its ladder runs, every opening being forced. So
   "stopped" is a sufficient condition on the OPENINGS, and the necessary one
   is about the TIED openings -- the countability gap's own lemma read
   backwards. A derivation and not a row here: an endless ladder has no limit
   this rig can enumerate, which is the whole reason the finite supplies are
   what the sections walk.

F2 THE EXHAUSTED IMAGE IS n^(D-1) * (n + 1), AND FOR H3's REASON (proved --
   H3 -- and a rule in range over 7 (width, top degree) rows, 0 off; 5 of the
   7 never run before the form was derived). A supply of n items at each of
   degrees 1..D reaches 2 limits at n = 1, then 96, 384, 324, 972, 1280 and
   5120. The two terms are the two homes the deep coordinate has -- degree 1,
   beside one flat item at each of the D-1 degrees above it, or degree 2 with
   degree 1 left empty -- which is the VOID MENU's tie counted as an image
   factor. That decomposition is asserted at every reachable state and not
   only inferred from a count that matched: the deep item's degree is 1 or 2
   at all of them, degree 1 carries exactly one item in the first family and
   none in the second, and every other seated item is flat and there is
   exactly one per degree above the deep one. So a supply with
   NO ties at all still has an image of 2: the tie that survives there is
   between DEGREES, not between items, and a rig that counted only
   within-degree multiplicities would have called that image a point.

F3 THE POWER OF 2 IS THE SUPPLY WIDTH'S DOING, AND EXHAUSTION ON A SUPPLY
   CARRYING THE VOID TIE DOES NOT REPRODUCE THE RING'S NUMBER (a reading of
   F2 across widths; 7 rows).
   Only the width-1 row is a power of 2, and it is one by being 2. At width 2
   the image is 2^(D-1)*3, at width 3 it is 3^(D-1)*4, at width 4 it is
   4^(D-1)*5 -- the width sets the base and the "+1" contributes a factor the
   width does not. So the corpus's finite images being powers of 2 is a fact
   about two-way ties and not about the formula, which was the suspicion, and
   reading the width off a schedule prices a ring that would tie three ways
   lower without retiring it.
   WHAT THIS DOES NOT SETTLE, and the scope is narrower than the numbers
   invite. 3*2^(D-1) is not a power of 2, so exhaustion on THESE supplies does
   not reproduce a number ring's 2^t -- but the extra factor is the VOID TIE's,
   the deep coordinate having two homes only because f(1,2) = f(2,1) at tick 1,
   and every supply here is built to satisfy that (least fresh degree at twice
   the least born-covered one, the attainment condition of
   explore_price_schedule.py). A supply WITHOUT that tie exhausts to a pure
   product over its openings and could be a power of 2. So what is ruled out
   is exhaustion on a supply that HAS the void tie, and capacity exhaustion in
   general is not ruled out as a lock's mechanism by anything here.

F4 WHAT STOPS A LADDER IS A COVERED SET THAT OUTRUNS IT, WHICH NO RULE RUN
   HERE KEYED TO THE SEATED SET DOES AND A RULE KEYED TO THE CLOCK DOES, AND
   THE THRESHOLD IS BRANCH-DEPENDENT
   (SINCE SCOPED: "outruns" presumes a ladder that CLIMBS, which every walk
   here has because the tick lands on ceil(b*T) and so overshoots the exponent
   it answers. A tick landing exactly on it stops the ladder with nothing
   outrunning anything, and that is the corner a number ring occupies --
   explore_lock_budget.py F4, F5. Everything below stands as measured, at a
   growing tick.) (rule in range;
   10 walks over 8 rules, against a supply with items at every degree to 4096
   and the walk asserted to stay far below it and to have something left to
   decline at every state). Five rules leave the ladder climbing and three of
   them leave it climbing IDENTICALLY: "divisors" and the LCM reading open the
   same 53 degrees as the imported rule, because the ladder is increasing and
   a rule that covers downward covers only what is already covered.
   "Multiples" is the one that bites without stopping -- it opens exactly the
   51 primes to 233, thinning the ladder and so making the clock fire more
   often, which sends the ladder HIGHER in the same 60 moves (tick 512 against
   128) rather than stopping it. What the five have in common is that such a
   rule is FED BY the very openings it would have to get ahead of -- which is
   the mechanism and not a proof over the whole kind, since a seated-set rule
   covering everything below 2^d would outrun the ladder and no rule like that
   was run. What does outrun it here is a covered set that grows with the
   CLOCK, doubling where the ladder steps by one: at
   "covered while d <= c*T" the ladder is dead at c = 1 on
   both void branches and at c = 1/2 only on the branch whose deep item has
   degree 1 -- the degree-2 branch pays 2*(T/2) = T for its clock and so still
   affords the least uncovered degree, and it opened 8 more degrees where its
   sibling opened none. Measured, the threshold sits in (1/4, 1/2] at deep
   degree 1 and in (1/2, 1] at deep degree 2; derived (H5), it is exactly 1/2
   and 1. A stop is read as a PRICE and not as a silence: at the last state of
   each stopped walk the supply still offered a fresh opening at degree 1025
   or 2049 and the walk took a move costing 1024 instead.

F5 THE CYCLOTOMIC COVERING RULE CANNOT STOP A LADDER, AND BANG'S THEOREM IS
   WHY (a control reproducing a filed theorem, plus a rule in range at 4
   (reading, base) rows). Read as a covering rule, a function field's test is
   that base^d - 1 divide the seated set's invariant. At the LCM reading --
   that world's own, an invariant being an exponent there -- nothing is ever
   covered for free, at base 2 or base 3, which is explore_greedy_limit.py's
   L4 reproduced from the schedule side. At the strictly more generous PRODUCT
   reading exactly ONE degree is freed, degree 6 at base 2, and nothing at
   base 3: 2^6 - 1 = 3^2 * 7 is the one Bang exception whose factors a product
   of smaller terms can supply and an LCM cannot. So the sprawl over a
   function field is now a statement about its COVERING RULE and not only
   about its supply: no accumulation of smaller terms can ever cover a fresh
   degree there, because every one of them carries a primitive prime.
   WHAT THIS DOES NOT SAY, and the boundary matters more than the finding.
   Every row here has INTEGER degrees and a single base, which is the function
   field's shape and not a number ring's: there a degree is a log-norm, the
   test runs over residue fields whose orders are unrelated primes, and
   nothing plays Zsygmondy's part. So the covering rule is exonerated exactly
   where the ladder is known not to stop, and becomes the leading SUSPECT
   where it is known to -- which is the reverse of the reading these rows
   invite and the reason the next question is a norm-indexed supply rather
   than another dial of this one.
   (SINCE REFUTED, in the SUSPECT half only: a number ring's ladder stops
   because its recurrent move's price is FLAT, not because anything covers
   its escapes -- hundreds of door-1 places sit unspent at every measured
   lock, and 6% and 12% of the two universes are covered there. So the
   covering rule is exonerated on BOTH sides of the boundary drawn here, and
   the norm-indexed supply this paragraph names as the next question would
   answer one already closed. The exoneration half above stands.
   explore_lock_budget.py F2, F3, F4.)

F6 A STOPPED LADDER GIVES A FINITE IMAGE AGAINST A SUPPLY THAT NEVER RUNS OUT,
   AND IT IS SMALL (rule in range; 3 widths at 3 budgets each, the reading sets
   equal as sets, the supply asserted to still be offering at degree 33, 129
   and 513 while the ladder sits at 2). Under the stopping rule the image is
   3, 8 and 15 at widths 1, 2 and 3 -- n^2 + 2n, which is the three families a
   ladder stopped at degree 2 can reach: the deep item alone at degree 1, the
   deep item alone at degree 2, or the deep item at degree 1 beside one flat
   item at degree 2. Derived AFTER the run and not before it, the freeze
   having predicted only that the count would stop growing. So finiteness does
   not need a finite supply: it needs the openings to stop, and it is the
   OPENINGS and not the supply that the cardinality question is about.

F7 WHAT IS LEFT OPEN, and the first is the run's own residue and the next
   question. Both stopping mechanisms run here are stated in the schedule's
   vocabulary and neither is a number ring's: a spent supply is a capacity fact
   and a clock-indexed covered set is a dial with no ring behind it. What F5
   leaves is a sharp and cheap target rather than an elimination -- the
   covering rule with a NORM-INDEXED supply, where a degree is a log-norm and
   the test is over residue-field orders that share no base. That it is the
   shape the locking rings actually have is read off their engine and not
   assumed: their door is the least r with lambda(P^(e+r)) not dividing the
   state's invariant (explore_module_law.py door_r), and lambda(P^1) is
   N(P) - 1 at every place kind, so a place is covered exactly when N(P) - 1
   divides that invariant. It is the one shape of covering rule this family
   has never carried, and the cost is a supply and a price rather than a ring
   interface.
   (SINCE SPENT: that target was built as a question and answered without it.
   A ring's stop is not a covering phenomenon, so a norm-indexed covering
   rule would reproduce nothing the ring does; what the two mechanisms here
   missed is a THIRD, the tick that does not overshoot -- explore_lock_budget.py.
   The reading of the ring's door quoted above is confirmed there --
   lambda(P^1) equals N(P) - 1 at all 604 places of the two engines'
   universes -- and it is the CONCLUSION drawn from it that does not hold.)
   The second is the element world, untouched here as
   in the rig this one imports. The third is narrower: the threshold in c is
   derived exactly and measured only to a factor of 2, and a sweep would say
   whether the derivation is the whole of it.

RUN RECORD. One process, CPython, no BLAS. Wall 5.5s, peak working set 42.5 MB
against the 512 MB ceiling. 39637 checks here, 535640 in the identified walker
and 7203 in the identity-free one, both imported. What the enumeration costs is
set by the state count of the exhausted image, which IS the number being
verified -- 5120 at the widest row, which is why the grid stops at width 4.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction

import explore_greedy_limit as GL
import explore_coarse_type as CT
import explore_price_schedule as PS
import explore_schedule_image as SI

CHECKS = 0

LADDER_CAP = 4096    # degrees the unexhausted supplies carry, asserted against
LADDER_N = 60        # moves of a walk under a rule that leaves the ladder
                     # climbing. A rule that THINS it makes the clock fire more
                     # often and so sends it to much higher degrees in the same
                     # number of moves, which is what the supply cap must clear
TICK_N = 12          # moves of a walk under a rule whose covered set grows
                     # with the clock. Short BY DESIGN: the tick doubles, so
                     # past T = LADDER_CAP the supply has no uncovered degree
                     # at all and a stopped ladder and a spent one print the
                     # same thing. Asserted, never assumed
CONTROL_N = 40       # states of the canonical walk the controls compare
STATE_CAP = 60000    # distinct identified states carried, asserted against
_ACC = {}            # memo for the cyclotomic rules' accumulated invariant


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def accumulated(kind, base, opens):
    """The seated set's invariant as a covering rule reads it: the LCM of the
    base^d - 1 over the opened degrees (a function field's own reading, where
    an invariant is an exponent) or their PRODUCT counted with multiplicity
    (a strictly more generous dial)."""
    key = (kind, base, tuple(sorted(opens.items())))
    if key not in _ACC:
        out = 1
        for d, k in sorted(opens.items()):
            t = base ** d - 1
            if kind == "lcm":
                out = out * t // gcd(out, t)
            else:
                out *= t ** k
        _ACC[key] = out
    return _ACC[key]


def primes_to(n):
    sieve = [True] * (n + 1)
    out = []
    for p in range(2, n + 1):
        if sieve[p]:
            out.append(p)
            for q in range(p * p, n + 1, p):
                sieve[q] = False
    return out


# ------------------------------------------------- the covering rule as a dial
class CSched(PS.Sched):
    """A schedule carrying a COVERING RULE beside its price and its clock. The
    rule says what a state covers BEYOND the imported rule (the born-covered
    degrees together with the ones whose discounts are spent), so "self"
    reproduces the imported walker exactly."""

    def __init__(self, tag, rule="self", cbase=2, c=1, **kw):
        PS.Sched.__init__(self, tag, **kw)
        self.rule = rule
        self.cbase = cbase
        self.c = Fraction(c)

    def extra(self, d, opens, T):
        r = self.rule
        if r == "self":
            return False
        if r == "div":                      # opening d covers its DIVISORS
            return any(dd % d == 0 for dd in opens)
        if r == "mult":                     # opening d covers its MULTIPLES
            return any(d % dd == 0 for dd in opens)
        if r in ("lcm", "prod"):            # the cyclotomic divisibility test
            return accumulated(r, self.cbase, opens) % (self.cbase ** d
                                                        - 1) == 0
        if r == "tick":                     # covered while d <= c * T
            return d <= self.c * T
        raise ValueError("no covering rule named %r" % r)


class CWalk(PS.Walk):
    """The identity-free walker with the covering rule in. Everything else --
    doors, prices, ticks, the menu's scan economy -- is the import's, and the
    control certifies that at rule "self" nothing moved."""

    def covered(self, d):
        return PS.Walk.covered(self, d) or self.sch.extra(d, self.opens,
                                                          self.T)

    def copy(self):
        s = CWalk(self.npl, self.sch, self.tag, self.dcap)
        s.seat = dict((d, list(v)) for d, v in self.seat.items())
        s.opens = dict(self.opens)
        s.opened = list(self.opened)
        s.T = self.T
        s.step = self.step
        s.clocks = list(self.clocks)
        s.capped = self.capped
        s.bad_l0 = self.bad_l0
        return s


class CIWalk(SI.IWalk):
    """The IDENTIFIED walker with the covering rule in -- needed only where an
    image is counted under a rule, which is the stopped ladder of the last
    section."""

    def covered(self, d):
        return SI.IWalk.covered(self, d) or self.sch.extra(d, self.opens,
                                                           self.T)

    def copy(self):
        s = CIWalk(self.npl, self.sch, self.tag, self.dcap, self.colour,
                   self.weight, self.track)
        s.seat = dict(self.seat)
        s.opens = dict(self.opens)
        s.opened = list(self.opened)
        s.T = self.T
        s.step = self.step
        s.clocks = list(self.clocks)
        if self.track:
            s.orders = set(self.orders)
        return s


def creach(npl, sch, tag, n, dcap):
    """Every distinct identified state reachable in n moves by any tie choice,
    under a covering rule. The identity-free reach of the imported rig with
    CIWalk in its place; the cap is asserted against, so a truncation cannot
    pass as a count."""
    live = {}
    root = CIWalk(npl, sch, tag, dcap)
    live[root.key()] = root
    for _ in range(n):
        nxt = {}
        for s in live.values():
            _, entries = s.menu()
            for mv in s.choices(entries):
                s2 = s.copy()
                s2.apply(mv)
                nxt.setdefault(s2.key(), s2)
        ok(len(nxt) <= STATE_CAP,
           "%s: %d states at one depth, over the cap" % (tag, len(nxt)))
        live = nxt
    return list(live.values())


def flat_supply(n, hi):
    npl = [0] * (max(hi, PS.DEG_CAP) + 2)
    for d in range(1, hi + 1):
        npl[d] = n
    return npl


def readings(states):
    return set(s.reading() for s in states)


def factorise(n):
    out, d, m = [], 2, n
    while d * d <= m:
        while m % d == 0:
            out.append(d)
            m //= d
        d += 1
    if m > 1:
        out.append(m)
    counts = {}
    for p in out:
        counts[p] = counts.get(p, 0) + 1
    return "*".join("%d^%d" % (p, k) if k > 1 else "%d" % p
                    for p, k in sorted(counts.items())) or "1"


# ---------------------------------------------------------- the ladder walk
def least_uncovered(w):
    """The cheapest degree the supply still offers a FRESH discount at, and
    what that discount costs. None where the supply has no uncovered degree
    left at all -- which is the state past which a ladder that has stopped is
    indistinguishable from a ladder that has run out."""
    for d in range(1, w.dcap + 1):
        if w.npl[d] and not w.covered(d):
            return d, w.sch.price(d, 1)
    return None, None


def ladder_walk(npl, sch, tag, n, high=0, dcap=LADDER_CAP):
    """One branch of the walk, carrying the step of every fresh open and, at
    every state, the cheapest fresh opening the supply still offers against the
    menu's own minimum. `high` takes the GREATEST menu entry for its first that
    many moves, which is how the other void branch -- the one whose deep item
    sits at degree 2 -- is reached; every later move is the least."""
    ok(not any(npl[d] for d in range(dcap + 1, len(npl))),
       "%s: the supply carries items past the walker's degree cap %d, so its "
       "menu scan is a truncation" % (tag, dcap))
    w = CWalk(npl, sch, tag, dcap)
    opens, offers = [], []
    for _ in range(n):
        best, ties = w.menu()
        d, price = least_uncovered(w)
        offers.append((d, price, best))
        keys = sorted(ties)
        w.apply(keys[-1] if w.step < high else keys[0])
        if len(w.opened) > len(opens):
            opens.append(w.step - 1)
    return w, opens, offers


def deep_degree(w):
    return w.clocks[-1][1] if w.clocks else None


def stopped(opens, n):
    """The observable, and it names what the rig reads and not what it would
    mean: no fresh open in the final third of the walk."""
    return not [x for x in opens if x >= (2 * n) // 3]


def free_covered(w):
    """Degrees covered without ever having been opened, WITHIN the ladder's own
    reach -- a degree above the highest one opened has not been offered yet and
    cannot be called free."""
    top = max(w.opened) if w.opened else 0
    return sorted(d for d in range(1, top + 1)
                  if w.npl[d] and w.covered(d)
                  and d not in w.sch.born and d not in w.opened)


# ------------------------------------------------------ S0 forced failures
def s0_forced(supplies):
    """Every check the run leans on, made to fail once."""
    fired = []
    toy = flat_supply(2, 8)

    # (a) the import control, given a walker whose covering rule differs
    try:
        c_import(toy, CSched("forced", rule="mult"), "forced", 8,
                 cross=CSched("self"))
        fired.append(("import", False))
    except AssertionError:
        fired.append(("import", True))

    # (b) the stabilisation, read across the exhaustion boundary rather than
    # past it -- the sets there genuinely differ, so asserting equality fails
    try:
        a = readings(SI.reach(toy, PS.Sched("corner"), "forced", 8))
        b = readings(SI.reach(toy, PS.Sched("corner"), "forced", 14))
        ok(a == b, "the reading set moved")
        fired.append(("stabilisation", False))
    except AssertionError:
        fired.append(("stabilisation", True))

    # (c) the closed form, read against a supply one item wider
    try:
        states = SI.reach(toy, PS.Sched("corner"), "forced", 20)
        check_form(states, 3, 8, "forced")
        fired.append(("closed form", False))
    except AssertionError:
        fired.append(("closed form", True))

    # (d) the exhaustion check, at a budget the ladder has not finished by
    try:
        states = SI.reach(toy, PS.Sched("corner"), "forced", 6)
        check_form(states, 2, 8, "forced")
        fired.append(("exhaustion", False))
    except AssertionError:
        fired.append(("exhaustion", True))

    # (e) the stop observable, asserted of the rule that must not stop
    try:
        _, opens, _ = ladder_walk(flat_supply(2, LADDER_CAP), CSched("self"),
                                  "forced", 30)
        ok(stopped(opens, 30), "the control stopped")
        fired.append(("stop observable", False))
    except AssertionError:
        fired.append(("stop observable", True))

    # (f) the free-coverage reading, against the wrong set
    try:
        w, _, _ = ladder_walk(flat_supply(2, LADDER_CAP),
                              CSched("prod", rule="prod"), "forced", 30)
        ok(free_covered(w) == [], "the product rule freed a degree")
        fired.append(("free coverage", False))
    except AssertionError:
        fired.append(("free coverage", True))

    # (g) the offer guard, on a walk carried past where the tick rule leaves
    # the supply nothing uncovered -- the failure the short walks avoid
    try:
        _, _, offers = ladder_walk(flat_supply(2, LADDER_CAP),
                                   CSched("tick", rule="tick", c=1),
                                   "forced", 40)
        ok(all(d is not None for d, _, _ in offers),
           "the supply ran out of uncovered degrees")
        fired.append(("offer guard", False))
    except AssertionError:
        fired.append(("offer guard", True))

    # (h) the state cap, forced to one state
    global STATE_CAP
    keep, STATE_CAP = STATE_CAP, 1
    try:
        creach(flat_supply(2, 8), CSched("self"), "forced", 4, 20)
        fired.append(("state cap", False))
    except AssertionError:
        fired.append(("state cap", True))
    finally:
        STATE_CAP = keep

    for name, hit in fired:
        print("  %-16s forced to fail: %s" % (name, "yes" if hit else "NO"))
        ok(hit, "the %s check did not fail when broken" % name)


# ------------------------------------------------------------ S1 the controls
def c_import(npl, sch, tag, n, cross=None):
    """PR1: advance the imported walker by the covering walker's own move and
    compare cost, menu and tick at every state. `cross` gives the imported one
    a different schedule, which is how the comparison is made to fail."""
    a = CWalk(npl, sch, tag)
    b = PS.Walk(npl, cross if cross is not None else sch, tag)
    for seen in range(n):
        ca, ta = a.menu()
        cb, tb = b.menu()
        ok(ca == cb, "%s: costs %d and %d part at state %d"
           % (tag, ca, cb, seen))
        ok(ta == tb, "%s: menus %s and %s part at state %d"
           % (tag, sorted(ta.items()), sorted(tb.items()), seen))
        key = sorted(ta)[0]
        Ta = a.apply(key)[3]
        Tb = b.apply(key)[3]
        ok(Ta == Tb, "%s: ticks %d and %d part at state %d"
           % (tag, Ta, Tb, seen))
    return n


def s1_control(supplies, ring_names):
    print("  the covering walker at rule \"self\" against the imported one")
    print("  supply     states compared  final tick  opened")
    for name in ring_names:
        seen = c_import(supplies[name], CSched("self"), name, CONTROL_N)
        w, _, _ = ladder_walk(supplies[name], CSched("self"), name, CONTROL_N,
                              dcap=PS.DEG_CAP)
        print("  %-10s %-16d %-11d %d" % (name, seen, w.T, len(w.opened)))
    print("\n  the identified walker against the identity-free one, the walk")
    print("  carried PAST the exhaustion point of a finite supply")
    print("  supply     states compared  final tick  opened  cost of the last")
    for n, hi in ((2, 8), (3, 6)):
        tag = "n=%d,D=%d" % (n, hi)
        npl = flat_supply(n, hi)
        seen = SI.control(npl, PS.Sched("corner"), tag, CONTROL_N)
        a = SI.IWalk(npl, PS.Sched("corner"), tag, dcap=60)
        for _ in range(CONTROL_N):
            c, entries = a.menu()
            a.apply(a.first_move(entries))
        ok(len(a.opened) == hi - 1,
           "%s: the control walk opened %d degrees, not the %d the supply has"
           % (tag, len(a.opened), hi - 1))
        print("  %-10s %-16d %-11d %-7d %d"
              % (tag, seen, a.T, len(a.opened), c))


# --------------------------------------------- S2 the walk past exhaustion
def s2_stable(grid):
    print("  supply     budget  states  configurations  limit readings"
          "  same set as before  shapes")
    for n, hi, budgets in grid:
        tag = "n=%d,D=%d" % (n, hi)
        npl = flat_supply(n, hi)
        prev = None
        for bud in budgets:
            states = SI.reach(npl, PS.Sched("corner"), tag, bud)
            exhausted(states, hi, tag)
            nsh, ncf, rows = SI.check_orbits(states, SI.supply_of(npl), tag)
            ok(ncf == sum(p for _, _, p in rows),
               "%s: %d configurations against an orbit sum of %d"
               % (tag, ncf, sum(p for _, _, p in rows)))
            rd = readings(states)
            same = "-" if prev is None else ("yes" if rd == prev else "NO")
            print("  %-10s %-7d %-7d %-15d %-15d %-19s %d"
                  % (tag, bud, len(states), ncf, len(rd), same, nsh))
            if prev is not None:
                ok(rd == prev,
                   "%s: the reading set moved at budget %d, %d readings "
                   "against %d" % (tag, bud, len(rd), len(prev)))
            prev = rd


# ------------------------------------------------------- S3 the closed form
def exhausted(states, hi, tag):
    """Every reachable state has spent the whole ladder. Asserted wherever a
    section reads a state as EXHAUSTED, so that "past exhaustion" is checked
    and never presumed by the budget having been chosen large."""
    for s in states:
        ok(len(s.opened) == hi - 1,
           "%s: a state opened %d of the supply's %d openable degrees, so the "
           "budget is short of exhaustion" % (tag, len(s.opened), hi - 1))


def check_form(states, n, hi, tag):
    """PR3: the reading count is n^(D-1) * (n + 1), and it is that for the
    REASON H3 gives -- the two families, which are checked here so that a
    right count reached by some other structure cannot pass."""
    exhausted(states, hi, tag)
    for s in states:
        dp = s.deep()
        ok(dp is not None and dp[0] in (1, 2),
           "%s: the deep item sits at degree %s, above the ceiling of 2"
           % (tag, dp and dp[0]))
        at1 = [it for it in s.seat if it[0] == 1]
        ok(len(at1) == (1 if dp[0] == 1 else 0),
           "%s: degree 1 carries %d items beside a deep item of degree %d, "
           "against the one family or the other" % (tag, len(at1), dp[0]))
        flat = [e for it, e in s.seat.items() if it != dp]
        ok(flat.count(1) == len(flat) == hi - (1 if dp[0] == 1 else 2),
           "%s: %d items beside the deep one, of which %d flat, against the "
           "one per opened degree above it" % (tag, len(flat), flat.count(1)))
    got = len(readings(states))
    want = n ** (hi - 1) * (n + 1)
    ok(got == want, "%s: %d limit readings against a closed form of %d"
       % (tag, got, want))
    return got, want


def s3_form(grid):
    print("  width  top degree  openable  budget  limit readings  n^(D-1)(n+1)"
          "  factorisation  a power of 2")
    for n, hi, bud in grid:
        tag = "n=%d,D=%d" % (n, hi)
        states = SI.reach(flat_supply(n, hi), PS.Sched("corner"), tag, bud)
        got, want = check_form(states, n, hi, tag)
        pow2 = got & (got - 1) == 0
        print("  %-6d %-11d %-9d %-7d %-15d %-13d %-14s %s"
              % (n, hi, hi - 1, bud, got, want, factorise(got),
                 "yes" if pow2 else "no"))


# ------------------------------------------------------ S4 the covering rules
def s4_rules(rules):
    """PR5. The observable is a PRICE COMPARISON and not merely an absence of
    openings: a ladder has stopped when the supply still offers a fresh
    discount somewhere and the walk declines it because the clock is cheaper.
    So every state carries the least uncovered degree the supply has, and a
    walk that runs past the last of those is not read at all -- past there,
    coverage and a spent supply print the same thing."""
    print("  rule            branch  moves  opens  last open at  opens in the"
          " final third  final tick  top degree  cheapest fresh still on"
          " offer  the menu's own minimum  stopped")
    out = {}
    npl = flat_supply(2, LADDER_CAP)
    for tag, sch, high, moves, want, want_deep in rules:
        w, opens, offers = ladder_walk(npl, sch, tag, moves, high=high)
        # the branch is the point of `high`, so it is checked and not hoped
        # for: a walk that meant to sit on the degree-2 deep item and did not
        # would answer the threshold question for the wrong branch
        ok(deep_degree(w) == want_deep,
           "%s: the deep item sits at degree %s, not the %d this branch was "
           "taken for" % (tag, deep_degree(w), want_deep))
        top = max(w.opened) if w.opened else 0
        late = [x for x in opens if x >= (2 * moves) // 3]
        st = stopped(opens, moves)
        ok(top < LADDER_CAP - 4,
           "%s: the ladder reached degree %d against a supply top of %d, so "
           "the supply's own cap is what stopped it" % (tag, top, LADDER_CAP))
        bad = [i for i, (d, _, _) in enumerate(offers) if d is None]
        ok(not bad,
           "%s: from state %d on, the supply had no uncovered degree left at "
           "all, so nothing there distinguishes a stopped ladder from a spent "
           "one" % (tag, bad[0] if bad else -1))
        d, price, best = offers[-1]
        print("  %-15s %-7s %-6d %-6d %-13s %-25d %-11d %-11d %-31s %-23d %s"
              % (tag, "deep@%d" % deep_degree(w), moves, len(w.opened),
                 opens[-1] if opens else "-", len(late), w.T, top,
                 "degree %d at %d" % (d, price), best, "yes" if st else "no"))
        ok(st == want,
           "%s: the ladder %s, against a prediction that it %s"
           % (tag, "stopped" if st else "did not stop",
              "would" if want else "would not"))
        if st:
            ok(price > best,
               "%s: the ladder stopped while a fresh opening at degree %d "
               "cost %d against a menu minimum of %d, so it did not stop on "
               "price" % (tag, d, price, best))
        out[tag] = w
    return out


def s4_compare(walks):
    """The rules that must open exactly what "self" opens, and the one that
    must open exactly the primes."""
    base = walks["self"].opened
    for tag in ("divisors", "lcm base 2"):
        ok(walks[tag].opened == base,
           "%s opened %s, against \"self\"'s %s"
           % (tag, walks[tag].opened[:12], base[:12]))
        print("  %-15s opens the same %d degrees as \"self\"" % (tag,
                                                                len(base)))
    got = walks["multiples"].opened
    want = primes_to(max(got))
    ok(got == want, "multiples opened %s, against the primes %s"
       % (got[:12], want[:12]))
    print("  %-15s opens exactly the %d primes to %d"
          % ("multiples", len(got), max(got)))


# ---------------------------------------------- S5 the cyclotomic exoneration
def s5_free(cases):
    print("  reading  base  opens  top degree  covered without being opened")
    npl = flat_supply(2, LADDER_CAP)
    for kind, base, want in cases:
        tag = "%s base %d" % (kind, base)
        w, _, _ = ladder_walk(npl, CSched(tag, rule=kind, cbase=base), tag,
                              LADDER_N)
        got = free_covered(w)
        print("  %-8s %-5d %-6d %-11d %s"
              % (kind, base, len(w.opened), max(w.opened),
                 ",".join(str(d) for d in got) or "none"))
        ok(got == want, "%s: freed %s, against %s" % (tag, got, want))


# -------------------------------------- S6 a stopped ladder, unexhausted supply
def s6_stopped_image(widths, budgets):
    print("  width  budget  states  limit readings  same set as before"
          "  top degree  cheapest fresh still on offer  factorisation")
    for n in widths:
        tag = "tick c=1, n=%d" % n
        npl = flat_supply(n, LADDER_CAP)
        sch = CSched(tag, rule="tick", c=1)
        prev, last = None, None
        for bud in budgets:
            states = creach(npl, sch, tag, bud, LADDER_CAP)
            rd = readings(states)
            top = max([d for s in states for d in s.opened] or [0])
            # the same guard the ladder walks carry, read BEFORE anything is
            # printed off it: every state must still have an uncovered degree
            # to decline, or the image counted here is a spent supply's and
            # not a stopped ladder's
            ok(all(least_uncovered(s)[0] is not None for s in states),
               "%s: a state at budget %d had no uncovered degree left in the "
               "supply at all" % (tag, bud))
            offer = min(least_uncovered(s)[0] for s in states)
            same = "-" if prev is None else ("yes" if rd == prev else "NO")
            print("  %-6d %-7d %-7d %-15d %-19s %-11d %-24s %s"
                  % (n, bud, len(states), len(rd), same, top,
                     "degree %s" % offer, factorise(len(rd))))
            ok(top < LADDER_CAP - 4,
               "%s: the ladder reached degree %d against a supply top of %d"
               % (tag, top, LADDER_CAP))
            if prev is not None:
                ok(rd == prev,
                   "%s: the reading set moved at budget %d, %d against %d"
                   % (tag, bud, len(rd), len(prev)))
            prev, last = rd, len(rd)
        ok(last is not None and last > 0, "%s: an empty image" % tag)


# ------------------------------------------------------------------- main
def main():
    supplies, ring_names = {}, []
    for L in CT.build_ladder():
        _, npl, _, _ = GL.universe(L)
        supplies[L.name] = npl
        ring_names.append(L.name)

    section("S0  THE HARNESS FORCED TO FAIL")
    for sch in (CSched("self"), CSched("mult", rule="mult"),
                CSched("prod", rule="prod"), CSched("tick", rule="tick")):
        sch.check_monotone(120)
    s0_forced(supplies)

    section("S1  THE POSITIVE CONTROLS")
    s1_control(supplies, ring_names)

    section("S2  THE READING SET PAST THE EXHAUSTION POINT")
    print("  A finite supply's ladder is spent and the clock runs alone. The")
    print("  configurations keep moving -- the deep exponent doubles at every")
    print("  step -- so the observable is the reading SET, compared as a set.")
    s2_stable([(2, 8, (14, 16, 18, 20)), (3, 6, (12, 14, 16))])

    section("S3  WHAT THE EXHAUSTED IMAGE IS")
    s3_form([(1, 6, 16), (2, 6, 16), (2, 8, 20), (3, 5, 14), (3, 6, 16),
             (4, 5, 14), (4, 6, 16)])

    section("S4  WHICH COVERING RULES STOP THE LADDER")
    print("  A supply with items at every degree to %d, so the supply's own"
          % LADDER_CAP)
    print("  capacity is never what stops anything -- asserted per state, and")
    print("  it is what sets the walk lengths, which the moves column carries")
    print("  because a clock-indexed rule outruns the supply within a dozen.")
    walks = s4_rules([
        ("self", CSched("self"), 0, LADDER_N, False, 1),
        ("divisors", CSched("divisors", rule="div"), 0, LADDER_N, False, 1),
        ("multiples", CSched("multiples", rule="mult"), 0, LADDER_N, False, 1),
        ("lcm base 2", CSched("lcm base 2", rule="lcm", cbase=2), 0, LADDER_N,
         False, 1),
        ("prod base 2", CSched("prod base 2", rule="prod", cbase=2), 0,
         LADDER_N, False, 1),
        ("tick c=1/4", CSched("tick c=1/4", rule="tick", c=Fraction(1, 4)), 0,
         TICK_N, False, 1),
        ("tick c=1/2", CSched("tick c=1/2", rule="tick", c=Fraction(1, 2)), 0,
         TICK_N, True, 1),
        ("tick c=1/2 hi", CSched("tick c=1/2", rule="tick", c=Fraction(1, 2)),
         2, TICK_N, False, 2),
        ("tick c=1", CSched("tick c=1", rule="tick", c=1), 0, TICK_N, True, 1),
        ("tick c=1 hi", CSched("tick c=1", rule="tick", c=1), 2, TICK_N, True,
         2),
    ])
    print()
    s4_compare(walks)

    section("S5  WHAT THE CYCLOTOMIC RULE CAN FREE")
    print("  A FUNCTION FIELD's covering test, read as a dial: (base^d - 1)")
    print("  must divide the seated set's invariant. BANG's theorem is what")
    print("  the two readings are being run against -- and a number ring's")
    print("  test is NOT of this shape, its degrees being log-norms over")
    print("  residue-field orders that share no base.")
    s5_free([("lcm", 2, []), ("prod", 2, [6]), ("lcm", 3, []),
             ("prod", 3, [])])

    section("S6  A STOPPED LADDER AGAINST AN UNEXHAUSTED SUPPLY")
    s6_stopped_image([1, 2, 3], (6, 8, 10))

    section("SUMMARY")
    print("  %d checks passed here, %d in the identified walker, %d in the"
          % (CHECKS, SI.CHECKS, PS.CHECKS))
    print("  identity-free one.")


if __name__ == "__main__":
    main()
