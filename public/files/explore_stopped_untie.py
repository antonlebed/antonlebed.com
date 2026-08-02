"""explore_stopped_untie.py -- the void tie broken under a STOPPED ladder
instead of a spent one, and what a stopped image is a product over.

THE QUESTION. explore_void_untie.py F1 proved the exhausted image is a SUM
OVER HOMES of a product over the openings, and that breaking the void tie
leaves one term. But exhaustion is not a mechanism any ring has: a ring's
supply never runs out (explore_void_untie.py F3), and what the arithmetic
points at instead is the STOPPED ladder -- a covering rule that outruns the
fresh ladder against a supply with items at every degree
(explore_ladder_stop.py F4). There the image at the tied supply is
n^2 + 2n (explore_ladder_stop.py F6), which is THREE families over TWO homes
and not two: a stop leaves the second home's degree OPTIONALLY opened where
exhaustion forces it. So a stopped image departs from a bare home count for
two reasons -- the home count and the optional opening -- and
explore_void_untie.py F4 leaves open which of them a tie-break removes.

THIS RIG RUNS THAT RIG'S THREE TIE-BREAKS UNDER THIS RIG'S STOPPING RULE, and
reads the FAMILY DECOMPOSITION rather than the count. Both families are dials
of the one schedule -- a supply and a price against a covering rule -- so they
compose, and the cost is a section rather than a rig.

THE COUNT IS THE WRONG OBSERVABLE, which is why every section below prints a
decomposition. Two departures are being separated and a single number cannot
separate them; a rig aimed at "is it a pure product" would read a collapse and
a survival as the same answer, and would read the right answer as a miss.

THE HAND-ATTACK, on paper before any engine code. Throughout, the CORNER
schedule (price = d^alpha * sigma, alpha = 1 unless a family says otherwise,
b = 2, one fresh discount per degree, the born-covered set a dial) over a
supply with items at every degree to a cap far above where the ladder reaches,
under the covering rule "d is covered while d <= c * T".

 H1 THE HOMES ARE STILL THE VOID MENU'S WINNERS, and the covering rule does
    not touch them -- but only because it covers nothing at tick 1 that the
    supply has. At T = 1 the rule covers d <= c, so at c <= 1 it can only ever
    cover degree 1, and every family below either has degree 1 born covered
    already or has no item there. That is a FAMILY-BY-FAMILY fact and not a
    property of the rule, so it is asserted per family rather than argued once:
    where it holds, explore_price_schedule.py's `void_winners` reads this
    rig's home set too.
 H2 THE VOID MENU HAS AT MOST TWO HOMES, ONE OF EACH KIND. A born-covered
    degree bids f(d, 2) and a fresh one f(d, 1); price(d, 1) is STRICTLY
    increasing in d at every schedule here, so two fresh degrees can never tie
    and neither can two born-covered ones, and only the least of each kind
    bids at all (`void_winners`). So |H| <= 2, which is why the exhausted
    image's extra term is a "+1" and never a "+2", and it is the ceiling the
    closed form below is a product over.
 H3 A STOPPED LADDER STOPS AT THE FIRST CLOCK OR NEVER, at alpha = 1. Past the
    first clock the deep move costs d_deep^alpha * T/2 and the least uncovered
    degree costs (floor(c*T) + 1)^alpha. At alpha = 1 BOTH scale linearly in T,
    so the comparison c*T + 1 vs d_deep*T/2 has the same verdict at every T
    above the first: the ladder is beaten at once once c >= d_deep/2, and never
    beaten below it. There is no regime where a ladder climbs for a while and
    then stops. (THE VERDICT HOLDS AND THIS ARGUMENT DOES NOT REACH IT, which
    is the slate's own error and is left standing as frozen. Two linear
    functions with different offsets DO cross, and a crossing is exactly the
    regime the step denies; also the fresh side is floor(c*T) + 1 and not c*T +
    1, which this line drops one sentence after writing it. What closes it is
    INTEGRALITY, and F2 carries the completed argument.) At alpha = 2 the fresh
    side grows QUADRATICALLY and the deep side linearly, so any c > 0 stops it
    eventually -- and at c = 1 it stops at once, which is where family (B) is
    run.
 H4 SO EVERY OPENING A STOPPED WALK EVER MAKES HAPPENS AT TICK 1, and a degree
    opened at tick 1 is a degree that attained the void menu's minimum, which
    is a HOME. Hence the optional set is contained in the home set:

      O(h)  =  H  minus  {h}  minus  the born-covered degrees

    -- born covered because such a degree's door is never 1, so its first seat
    lands above exponent 1 and is a clock move, which past the first one only
    the deep item makes (explore_void_untie.py H2, re-derived there for an
    exhausted walk and holding here for the same reason: the deep item's
    re-clock at d_deep^alpha * T/2 beats an unseated item at a covered degree
    at d^alpha * (T + 1) by the degree ceiling, non-strictly at the tied
    family's second home and strictly elsewhere).
    THE CONSEQUENCE IS THE WHOLE PREDICTION: breaking the tie removes the
    second home AND its optional opening in ONE move, because they are the
    SAME DEGREE. The two departures explore_void_untie.py F4 names are not
    independent, and an untied stopped image is the home's width alone.
 H5 SO THE STOPPED IMAGE HAS A CLOSED FORM OVER THE HOMES, and the openings
    do not enter it at all. Writing n_d for the width at degree d,

      image  =  SUM over h in H of  n_h * PRODUCT over d in O(h) of (n_d + 1)

    -- the (n_d + 1) being the optional degree's own choices, EMPTY or one of
    its n_d items. At H = {b, f} with b born covered and f fresh this is
    n_b * (n_f + 1) + n_f = n_b*n_f + n_b + n_f, which at a uniform width is
    n^2 + 2n and is explore_ladder_stop.py F6 recovered as a two-home case.
    Equivalently, and this is the form worth stating:

      image  =  PRODUCT over h in H of (n_h + 1)  minus  1

    at |H| <= 2, the minus one being the state with no deep item at all.
    WHAT THIS SAYS AGAINST THE EXHAUSTED LAW is the finding rather than the
    formula: there the product ran over every OPENABLE degree and every
    width in the supply entered it; here it runs over the HOMES, and the
    widths at every other degree are IRRELEVANT. Two supplies differing only
    above the homes must give the same image, and that is a separating row
    no uniform-width family could produce.
 H6 THE THRESHOLD IN c IS BRANCH-DEPENDENT AND THE TIE-BREAKS MOVE THE BRANCH.
    H3's condition is c >= d_deep/2, and family (C) puts the deep item at
    degree 3, where c = 1 does NOT stop the ladder. So (C) runs at c = 3/2,
    and c = 1 is run there too as a printed NON-stop rather than left as an
    assumption -- a family run at the wrong c prints a ladder that never
    stopped and would read as a refutation of the shape.

 H7 THE TIE BREAKS THE SAME THREE WAYS, plus the two rows the stopped form
    needs that the exhausted one did not.
      (A) GAP THE SUPPLY. Degrees {1} and {3..CAP}, B = {1}, c = 1. The least
          fresh degree is 3 and f(1, 2) = 2 < f(3, 1) = 3, so H = {1}, the
          deep item sits at degree 1 and c = 1 stops it. Predicted image: n.
      (B) STEEPEN THE PRICE. Every degree, B = {1}, alpha = 2, c = 1. Then
          f(1, 2) = 2 < f(2, 1) = 4 and H = {1}. This one moves NO supply at
          all. Predicted image: n.
      (C) RAISE THE FLOOR. Degrees {2..CAP}, B = {2}, c = 3/2. Then
          f(2, 2) = 4 > f(3, 1) = 3, so the FRESH side wins and H = {3}: the
          home is a fresh degree, degree 2 is born covered and empty, and the
          deep item sits at degree 3, which is why c moves. Predicted image: n.
      (D) THE HOMES AT DIFFERENT WIDTHS. The tied supply with n_1 = 2 and
          n_2 = 3, which is the only row that can tell H5's product over the
          homes from a power: predicted 2*3 + 2 + 3 = 11.
      (E) THE SAME ROW WITH THE TAIL CHANGED. n_1 = 2, n_2 = 3 and width 5 at
          every degree from 3 up, against width 1 there. Predicted: 11 both
          times -- the row that says the product runs over the HOMES and not
          over the supply.

THE POSITIVE CONTROL IS THE TIED SUPPLY UNDER THE SAME RULE, and it must
reproduce explore_ladder_stop.py F6's filed 3, 8 and 15 at widths 1, 2 and 3
from THIS rig's own enumerator and structural checker before any untied count
is read.

TRANSPLANT FLAGS, fixed at the freeze.
 1. THE SUM-OVER-HOMES LAW IS PROVED FOR AN EXHAUSTED WALK, where the seated
    set is frozen because there is nothing left to open. A STOP freezes the
    OPENINGS and not the CLOCK, and the clock is the coordinate that law has
    no term for. So nothing of explore_void_untie.py H2 is imported: that the
    seated set stops growing under a stop is RE-DERIVED (H4) and asserted at
    every state, and the deep item's own exponent runs away here as it does
    there, which is exactly what the reading forgets.
 2. From the schedule's stopped ladder to a RING's lock: NOTHING is carried.
    A number ring locks by a recurrent vehicle in its class dynamics whose
    price is flat (explore_lock_budget.py F4); a schedule stops here by a
    covering rule that is a DIAL and is not certified to be any ring's
    (explore_ladder_stop.py transplant flag 4). What this rig can say is what
    SHAPE a stopped image has, never that a ring has it.
 3. From the ideal world to the element world: nothing, as in every rig this
    one imports. A rider raises an exponent with no clock move and no dial of
    this family has that shape.
 4. Family (B) changes alpha, which moves the DEGREE CEILING as well as the
    tie (explore_void_untie.py transplant flag 5) and also moves H3's stopping
    argument from linear-vs-linear to quadratic-vs-linear. So (B) changes two
    things at once and cannot separate them; (A) and (C) leave alpha at 1 and
    are what carry the verdict. (B) is kept because it is the only family that
    moves no supply at all.
 5. The supplies called INFINITE are finite in the rig -- items at every degree
    to a cap far above where the walk reaches. What is asserted, at every
    state, is that the supply still OFFERS an uncovered degree, so a stopped
    ladder and a spent one cannot print the same thing.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 THE HARNESS CAN FAIL. What the rig PRINTS: per forced failure -- a state
    with a second item at the home degree, a state with an item at a degree
    outside the home set, a state whose deep item sits off its home, a state
    with a non-deep item above exponent 1, a supply bumped at a HOME against a
    closed form that must MOVE, a supply bumped ABOVE the homes against a
    closed form that must NOT move, and the UNMUTATED state, which must be
    accepted -- whether the check fired.
    KILL: one forced failure that does not fire.
PR2 THE TIE LEDGER AND THE ROOM THE COVERING RULE LEAVES IT, PRINTED BEFORE
    ANY IMAGE COUNT IS READ. What the rig PRINTS: per family, c, the least
    born-covered degree and its void price f(d, 2), the least fresh degree and
    its f(d, 1), the strict comparison, the home set both as `void_winners`
    computes it and as the walker's own root menu attains it, and whether the
    covering rule covers anything at tick 1 that the supply has.
    KILL: an untied family whose home set is not a singleton; or the tied
    control's home set not being {1, 2}; or the two readings of the home set
    disagreeing; or the covering rule covering a supplied degree at tick 1,
    which would put the home set outside `void_winners`' reach.
PR3 THE POSITIVE CONTROL REPRODUCES THE FILED NUMBERS. What the rig PRINTS:
    for the tied supply at widths 1, 2 and 3 under c = 1, the reading count
    from this rig's enumerator against explore_ladder_stop.py F6's filed 3, 8
    and 15.
    KILL: one row off the filed number.
PR4 THE STOP IS A PRICE AND THE THRESHOLD IS BRANCH-DEPENDENT. What the rig
    PRINTS: per family, at the last budget's states, the cheapest fresh
    opening the supply still offers and its price against the menu minimum the
    walk actually took, the deep degree, and the highest degree ever opened.
    And, for family (C) at c = 1 -- the wrong c for its branch -- the degrees
    it opens instead.
    KILL: a family whose supply has no uncovered degree left, which would make
    a stop indistinguishable from exhaustion; or a stopped family whose
    declined fresh opening costs no more than the move it took; or family (C)
    at c = 1 stopping, which would mean the branch dependence is not real.
PR5 THE FAMILY DECOMPOSITION, WHICH IS THE OBSERVABLE. What the rig PRINTS:
    per family, one row per SHAPE -- the deep degree together with the degrees
    and exponents of every other seated item -- with the readings at that
    shape against H4's predicted count for it.
    KILL: one shape the prediction does not list, one listed shape absent, or
    one shape's count off.
PR6 THE HEADLINE -- AN UNTIED STOPPED IMAGE IS THE HOME'S WIDTH ALONE, AND THE
    PRODUCT RUNS OVER THE HOMES. What the rig PRINTS: per family, the home
    count, the reading count, H5's closed form, and the count's factorisation;
    and the two supplies of (E) side by side, differing only above the homes.
    KILL: an untied row off its home's width; or the two (E) rows differing;
    or the tied control's image equal to its home's width, which would mean
    the home count is not what decides it.

FINDINGS (tiers below; run record at the bottom). Every section asserts,
including the closed form, which is checked at every row rather than printed
beside it, and the decomposition, which is matched SHAPE BY SHAPE at every row
rather than inferred from a total that came out right.

F1 A STOPPED IMAGE IS A PRODUCT OVER THE HOMES AND OVER NOTHING ELSE, so
   breaking the void tie COLLAPSES it to the home's width rather than removing
   one factor of it (a rule in range over 11 families, 0 off the closed form:
   six untied across 3 independent dials, at two widths each, beside 5 tied
   controls; at ONE fresh discount per degree and b = 2 throughout. PROVED at
   alpha = 1 -- H2, H4 and H5 carry no alpha, and H3, which is what H4 needs,
   is derived there and only MEASURED at alpha = 2, where the stop is delayed
   in principle and lands at the first clock at c = 1. So the steep family is a
   row of the rule and not of the proof, which is the same scope its transplant
   flag 4 gives it for a different reason). The six untied families reach 2, 3,
   2, 3, 2 and 3 readings at widths 2 and 3 -- the width at the home degree,
   exactly, with no second factor anywhere -- against the tied controls' 3, 8
   and 15. So

     image  =  SUM over homes h of  n_h * PRODUCT over d in O(h) of (n_d + 1)

   where O(h) is the OTHER homes that are not born covered, and at |H| <= 2
   (H2) that is PRODUCT over h in H of (n_h + 1), minus one. The minus one is
   the state with no deep item, and the (n_d + 1) is the optional degree's own
   menu: empty, or one of its n_d items. AND IT IS A CLOSED FORM ONLY AT A c
   THAT STOPS EVERY BRANCH, which is a condition the form does not carry and
   the threshold's branch dependence (H6) makes non-trivial: at |H| = 2 the two
   homes are b born covered and f = 2b fresh -- an exact tie needs f^alpha =
   2b^alpha, so at alpha = 1 the fresh home is exactly twice the born one
   (explore_price_schedule.py F3's attainment condition, and at alpha = 2 no
   integer pair ties at all) -- and the branch thresholds are then c >= b/2 and
   c >= b. So c >= b stops both and anything in [b/2, b) stops the born branch
   alone, leaving the image INFINITE on the other and the sum with one term
   that is not a count. Every family here runs a c at or above the greater
   threshold and the rig asserts the stop at every state of every reach, so the
   rows are inside the condition; a reader taking the form to a smaller c is
   not. The one measured witness of the gap is on file: at c = 1/2 the tied
   family stops on the degree-1 branch only (explore_ladder_stop.py F4). THE
   PRODUCT RUNS OVER THE HOMES AND NOT OVER THE OPENINGS, which is the whole of
   what separates this from the exhausted law, and it is measured on a row
   built to say so and nothing else: two supplies with n_1 = 2, n_2 = 3 and
   tail widths 1 and 5 at every degree from 3 up reach 11 readings BOTH times.
   Under exhaustion every width in the supply entered the product
   (explore_void_untie.py F1); here every width above the homes is irrelevant,
   because a stopped walk never opens a degree above them. AND THE PRODUCT IS A
   PRODUCT AND NOT A POWER, which no uniform row can tell apart: that same
   mixed row reads 11 = 2*3 + 2 + 3 = (2+1)(3+1) - 1, against the uniform
   width-3 control's 15 = (3+1)^2 - 1. THE DECOMPOSITION IS MATCHED SHAPE BY
   SHAPE and not inferred from a total. The tied control reaches exactly three
   shapes -- deep at degree 1 with degree 2 empty, deep at degree 1 beside one
   flat item at degree 2, deep at degree 2 with degree 1 empty -- at n, n^2 and
   n readings; every untied family reaches exactly ONE, the deep item alone at
   its home, with nothing else seated at any degree. So a right count reached
   by some other structure could not pass, and neither could a shape the
   prediction does not list. THE POSITIVE CONTROL RAN FIRST and through this
   rig's own enumerator and structural checker: the tied supply under the same
   covering rule reproduces explore_ladder_stop.py F6's filed 3, 8 and 15 at
   widths 1, 2 and 3. The harness is shown to be able to fail at seven forced
   checks: four mutations of a genuine stopped state, a supply bumped at a HOME
   against a form that must move, a supply bumped ABOVE the homes against a
   form that must not, and the UNMUTATED state, which must be ACCEPTED.

F2 SO THE TWO DEPARTURES explore_void_untie.py F4 NAMES ARE ONE DEPARTURE,
   AND THE TIE-BREAK REMOVES BOTH IN ONE MOVE (proved at alpha = 1 -- H4, and
   H3 as this finding completes it rather than as the slate froze it; MEASURED
   at alpha = 2, where the steep family stops at the first clock at c = 1 and
   nothing here proves it must -- and confirmed by the decomposition of F1's
   untied rows). That rig read a
   stopped image as departing from a bare home count for two reasons, the home
   count and the degree a stop leaves OPTIONALLY opened, and predicted a
   tie-break would remove one of them. It removes both, and the reason is that
   they are the SAME DEGREE. At alpha = 1 a stopping rule stops the ladder at
   the FIRST clock or never (H3), and the step that closes that is
   INTEGRALITY and not the linearity H3 leans on -- two linear functions with
   different offsets do cross, and a crossing is exactly the window this
   claims does not exist. A clock leaves T EVEN, so d_deep * T/2 is an
   integer, and the deep move at d_deep * T/2 undercuts the least uncovered
   degree at floor(c*T) + 1 exactly when c*T >= d_deep * T/2, which is
   c >= d_deep/2 with no T in it at all: the same verdict at every clock, and
   the first one already carries it. (Checked as well as argued: 0 verdict
   flips across nine clocks over the 192 pairs of c on an eighths grid to 3
   and d_deep to 4.) Every opening a stopped
   walk makes therefore happens at tick 1, where a degree is opened only by
   attaining the void menu's minimum -- which is what a home IS (H4). So the
   optional set is contained in the home set, and a singleton home set has an
   empty one. The rows carry this directly: at the gapped and steep families
   the highest degree ever opened is 0 -- no fresh opening is ever made at
   all, degree 1 being born covered so that its seat is a clock move -- and at
   the floor family it is 3, the home itself.
   WHAT THIS COSTS IS THE STOPPED IMAGE'S SIZE, and that is the finding rather
   than the tidiness. The exhausted image grew with the supply's top degree,
   n^(D-1) * (n + 1) over D-1 openings; a stopped image is bounded by
   (n + 1)^2 - 1 whatever the supply, n being the LARGER home's width, because
   the openings contribute nothing.
   A stop does not merely make an image finite (explore_ladder_stop.py F6): it
   makes it SMALL, and sets it entirely from the void menu -- the multiplicity
   at one or two degrees the schedule fixes before the walk begins.

F3 AND THE ARITHMETIC TEST THAT SEPARATED TIED FROM UNTIED UNDER EXHAUSTION IS
   DEGENERATE UNDER A STOP (a reading of F1 across the width-2 and width-3
   rows; 11 rows, the arithmetic read off the closed form rather than fitted).
   explore_void_untie.py F2 separated the two regimes by a power of 2 at
   uniform width 2: untied images were 128, 64, 64 and 16 and the tied control
   was 384 = 2^7 * 3. Under a stop that test says nothing -- the tied control
   reads 8 = 2^3, a power of 2, and the untied rows read 2. What still
   separates them is width 3, where the tied control reads 15 = 3 * 5 and the
   untied rows read 3. So the "is it a power of the width" reading is a
   property of the EXHAUSTED law and does not travel: at |H| = 2 the stopped
   image is (n+1)^2 - 1, which is a power of 2 at n = 2 by coincidence of
   9 - 1 and not because anything untied.
   WHAT THE SHAPE DOES SAY, at the honest tier and no further. A ring's finite
   image is a power of 2, and under a stop the image is set by the widths at
   one or two degrees the void menu picks. So the shape a stopped schedule
   offers a ring is "the multiplicity at the deep place, plus at most one
   more" -- and transplant flag 2 stands unmoved: nothing here is a ring's
   covering rule, and a schedule that reproduces a ring's NUMBER by dialling
   two widths has reproduced an arithmetic and not a mechanism.

F4 WHAT IS LEFT OPEN. The first is where H3 stops being an argument: it is
   proved at alpha = 1, where the decline condition reduces to c >= d_deep/2
   with no T left in it (F2 -- NOT the linearity the slate leaned on, which is
   the step this file marks as not reaching its own verdict), and family (B)
   shows the quadratic corner stopping at once at
   c = 1 -- but a price whose two sides scale at DIFFERENT rates could leave a
   window where the ladder climbs for a while and then stops, and such a window
   is the one regime in which a stopped image would have openings in it and
   H4's containment would have something to say. No family here has one, and
   the cheap probe is family (B) at a c small enough to delay the stop: the
   image would then run over the degrees opened before it, and the exhausted
   law and this one would be two ends of one formula rather than two laws.
   The second is the element world, untouched here as in every rig this one
   imports. The third is that the threshold in c is derived per branch (H6)
   and measured at two points -- c = 1 stopping the degree-1 and degree-2
   branches and not the degree-3 one, which is the row the floor family runs
   at c = 1 and prints as 8 degrees opened in 12 moves -- so which c stops a
   given home is a formula this rig uses and does not sweep.

RUN RECORD. One process, CPython, no BLAS. Wall 0.3s, peak working set 17.9 MB
against the 512 MB ceiling. 470 checks here, 14707 in the identified walker,
868 in the identity-free one and 547 in the stopped-ladder rig, all three
imported. What the enumeration costs is set by the state count of the stopped
image, which IS the number being verified -- 15 at the largest row, which is
why the supply's cap and not the image is what sets the cost here.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction

import explore_price_schedule as PS
import explore_schedule_image as SI
import explore_ladder_stop as LS

CHECKS = 0

CAP = 2048           # degrees the unexhausted supplies carry, asserted against
BUDGETS = (5, 7, 9)  # moves enumerated. Short BY DESIGN: the tick doubles at
                     # every clock, so past T = CAP / c the supply has no
                     # uncovered degree at all and a stopped ladder prints what
                     # a spent one prints. Asserted per state, never assumed
STATE_CAP = 60000    # distinct identified states carried, asserted against


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


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


# ------------------------------------------------------------- the supplies
def supply(tail, absent=(), over=None):
    """Items at every degree to CAP -- `tail` of them -- with a set of degrees
    ABSENT and a dict of per-degree overrides. The supply is what the ladder
    would climb forever against; the covering rule is what stops it."""
    npl = [0] * (max(CAP, PS.DEG_CAP, SI.DCAP) + 2)
    for d in range(1, CAP + 1):
        npl[d] = tail
    for d in absent:
        npl[d] = 0
    for d, w in (over or {}).items():
        npl[d] = w
    return npl


class Family(object):
    """A supply, a schedule and a covering rule, named. `tied` is what the
    family is CLAIMED to be and is asserted against the void menu, never read
    off it."""

    def __init__(self, name, npl, sch, tied):
        self.name = name
        self.npl = npl
        self.sch = sch
        self.tied = tied
        self._homes = None

    def width(self, d):
        return self.npl[d]

    def homes(self):
        if self._homes is None:
            self._homes = sorted(PS.void_winners(self.sch, self.npl, CAP))
        return self._homes

    def optional(self, h):
        """H4: the degrees a state deep at h can carry a FLAT item at -- the
        other homes, less the born-covered ones, whose first seat is a clock
        move and so is never taken past the first."""
        return [d for d in self.homes()
                if d != h and d not in self.sch.born]

    def form(self):
        """H5: the sum over homes of the product over the optional degrees of
        (width + 1)."""
        total = 0
        for h in self.homes():
            term = self.width(h)
            for d in self.optional(h):
                term *= self.width(d) + 1
            total += term
        return total

    def shapes(self):
        """H4/H5 as a DECOMPOSITION rather than a total: shape -> count, where
        a shape is the deep degree together with the (degree, exponent) of
        every other seated item. Every optional degree is either empty or
        carries one flat item."""
        out = {}
        for h in self.homes():
            opt = self.optional(h)
            for mask in range(1 << len(opt)):
                sub = [opt[i] for i in range(len(opt)) if mask >> i & 1]
                n = self.width(h)
                for d in sub:
                    n *= self.width(d)
                out[(h, tuple((d, 1) for d in sorted(sub)))] = n
        return out


# --------------------------------------------------------------- the reach
def reach(fam, budget):
    """Every distinct identified state reachable in `budget` moves by any tie
    choice, under the covering rule. The imported enumerator with the covering
    walker in its place; the cap is asserted against here as well, so a
    truncation cannot pass as a count."""
    states = LS.creach(fam.npl, fam.sch, fam.name, budget, CAP)
    ok(len(states) <= STATE_CAP,
       "%s: %d states, over the cap" % (fam.name, len(states)))
    return states


def readings(states):
    return set(s.reading() for s in states)


def shape_of(s):
    dp = s.deep()
    if dp is None:
        return None
    return (dp[0], tuple(sorted((it[0], e) for it, e in s.seat.items()
                                if it != dp)))


# ------------------------------------------------------ the structural check
def shape_faults(fam, s):
    """PR5: every way a state can be off H4's stopped shape, as a LIST of
    complaints rather than an assertion, so that the forced failures can read
    it directly -- a checker that only ever raises cannot be shown to separate
    a good state from a bad one."""
    out = []
    homes = fam.homes()
    dp = s.deep()
    if dp is None:
        return ["no clock move has been made, so there is no deep item"]
    if dp[0] not in homes:
        out.append("the deep item sits at degree %d, off the home set %s"
                   % (dp[0], homes))
        return out
    opt = fam.optional(dp[0])
    byd = {}
    for it, e in s.seat.items():
        if it == dp:
            continue
        byd.setdefault(it[0], []).append(e)
    for d in sorted(byd):
        if d == dp[0]:
            out.append("the home degree %d carries %d items beside the deep "
                       "one" % (d, len(byd[d])))
        elif d not in opt:
            out.append("degree %d is seated and is not optional at the home "
                       "%d (optional: %s)" % (d, dp[0], opt))
        elif byd[d] != [1]:
            out.append("the optional degree %d carries the exponents %s, not "
                       "one flat item" % (d, sorted(byd[d])))
    for it, e in s.seat.items():
        if it != dp and e > 1:
            out.append("the item %s stands at exponent %d and is not the deep "
                       "one" % (str(it), e))
    return out


def opened_faults(fam, s):
    """Every opening a stopped walk makes is at a home (H4). Read separately
    from the shape so that an opening off the home set reports as an opening
    rather than as a shape the family failed."""
    bad = [d for d in s.opened if d not in fam.homes()]
    if bad:
        return ["opened %s, off the home set %s" % (bad, fam.homes())]
    return []


def audit(fam, states):
    deeps = set()
    for s in states:
        f = opened_faults(fam, s) + shape_faults(fam, s)
        ok(not f, "%s: %s" % (fam.name, "; ".join(f)))
        deeps.add(s.deep()[0])
    return deeps


# ------------------------------------------------------- S0 forced failures
def s0_forced(fam):
    """PR1. The state mutations are applied to a genuine stopped state of the
    tied control, so what the checker rejects differs from what it accepts by
    exactly the mutation."""
    states = reach(fam, BUDGETS[-1])
    ok(states, "%s: an empty reach" % fam.name)
    base = None
    for s in states:
        if not (opened_faults(fam, s) + shape_faults(fam, s)):
            base = s
            break
    ok(base is not None,
       "%s: no state of the control passes its own shape check, so the forced "
       "failures would have nothing to mutate" % fam.name)
    fired = []
    dp = base.deep()

    # (a) a second item at the home degree -- a REAL item of that degree the
    # supply carries and the walk left unseated, so the state differs from the
    # accepted one by exactly one seat and by nothing else
    s = base.copy()
    free = next(j for j in range(base.npl[dp[0]])
                if (dp[0], j) not in base.seat)
    s.seat[(dp[0], free)] = 1
    fired.append(("a second item at the home degree",
                  bool(shape_faults(fam, s))))

    # (b) an item at a degree outside the home set
    off = max(fam.homes()) + 1
    s = base.copy()
    s.seat[(off, 0)] = 1
    fired.append(("a seat off the home set", bool(shape_faults(fam, s))))

    # (c) a deep item off the home set
    s = base.copy()
    s.clocks = list(s.clocks) + [(s.step, (off, 0))]
    fired.append(("a deep item off its home", bool(shape_faults(fam, s))))

    # (d) a non-deep item above exponent 1 -- the clause that says a stop
    # freezes the seated set and leaves only the CLOCK running, which is the
    # one thing the exhausted law has no term for
    alt = None
    for x in states:
        if not shape_faults(fam, x):
            d2 = x.deep()
            other = [it for it in x.seat if it != d2]
            if other:
                alt = (x, other[0])
                break
    ok(alt is not None,
       "%s: no stopped state with a second seated item, so the strand fault "
       "has no witness" % fam.name)
    s = alt[0].copy()
    s.seat[alt[1]] = 2
    fired.append(("a strand beside the deep item", bool(shape_faults(fam, s))))

    # (e) the closed form must MOVE with a width at a HOME
    h = fam.homes()[0]
    bumped = Family(fam.name + " +1 at a home",
                    supply(fam.npl[CAP], over=dict(
                        (d, fam.npl[d] + (1 if d == h else 0))
                        for d in range(1, 4))),
                    fam.sch, fam.tied)
    fired.append(("the form moves with a home's width",
                  bumped.form() != fam.form()
                  and bumped.homes() == fam.homes()))

    # (f) and it must NOT move with a width ABOVE the homes, which is the half
    # a sensitivity check alone cannot show and is H5's own separating claim
    top = max(fam.homes()) + 1
    tail = Family(fam.name + " +1 above the homes",
                  supply(fam.npl[CAP] + 1,
                         over=dict((d, fam.npl[d])
                                   for d in range(1, top))),
                  fam.sch, fam.tied)
    fired.append(("the form ignores a width above the homes",
                  tail.form() == fam.form()
                  and tail.homes() == fam.homes()
                  and tail.npl[top] != fam.npl[top]))

    # (g) and the check must ACCEPT the unmutated state, which is the half a
    # list of rejections cannot show on its own
    fired.append(("the unmutated state accepted",
                  not (opened_faults(fam, base) + shape_faults(fam, base))))

    for name, hit in fired:
        print("  %-42s %s" % (name, "fired" if hit else "DID NOT FIRE"))
        ok(hit, "the forced failure of %s did not fire" % name)


# -------------------------------------------------------- S1 the tie ledger
def s1_ledger(fams):
    """PR2, and it runs BEFORE any image is counted: a family that silently
    re-satisfied the tie, or one whose covering rule reached into the void
    menu, would print a number that reads as a confirmation of the wrong
    thing."""
    print("  family              c      born   f(d,2)  fresh  f(d,1)"
          "  comparison  homes    root menu  covered at tick 1  claimed")
    for fam in fams:
        cb = [d for d in range(1, CAP + 1) if fam.npl[d] and d in fam.sch.born]
        cf = [d for d in range(1, CAP + 1)
              if fam.npl[d] and d not in fam.sch.born]
        pb = fam.sch.price(cb[0], 2) if cb else None
        pf = fam.sch.price(cf[0], 1) if cf else None
        if pb is None or pf is None:
            cmp_ = "one kind only"
        elif pb == pf:
            cmp_ = "EQUAL"
        else:
            cmp_ = "%d %s %d" % (pb, "<" if pb < pf else ">", pf)
        h = fam.homes()
        # H1: the covering rule must cover nothing at tick 1 that the supply
        # has and the born set does not, or `void_winners` is reading a menu
        # this rig does not walk
        extra = [d for d in range(1, CAP + 1)
                 if fam.npl[d] and d not in fam.sch.born
                 and fam.sch.extra(d, {}, 1)]
        root = LS.CIWalk(fam.npl, fam.sch, fam.name, CAP)
        _, entries = root.menu()
        degs = sorted(set(e[0] for e in entries))
        print("  %-19s %-6s %-6s %-7s %-6s %-7s %-11s %-8s %-10s %-18s %s"
              % (fam.name, fam.sch.c,
                 cb[0] if cb else "-", pb if pb is not None else "-",
                 cf[0] if cf else "-", pf if pf is not None else "-",
                 cmp_, h, degs,
                 ",".join(str(d) for d in extra) or "none",
                 "tied" if fam.tied else "untied"))
        ok(not extra,
           "%s: the covering rule covers the supplied degrees %s at tick 1, "
           "so the void-menu law is not reading this rig's menu"
           % (fam.name, extra))
        ok((len(h) > 1) == fam.tied,
           "%s: %d homes against a family claimed %s"
           % (fam.name, len(h), "tied" if fam.tied else "untied"))
        ok((pb == pf) == fam.tied,
           "%s: the void prices %s and %s against a family claimed %s"
           % (fam.name, pb, pf, "tied" if fam.tied else "untied"))
        ok(degs == h, "%s: the root menu's winning degrees %s against the "
                      "void-menu law's %s" % (fam.name, degs, h))
        ok(len(h) <= 2, "%s: %d homes, against H2's ceiling of two"
           % (fam.name, len(h)))


# ------------------------------------------------------ S2 the stop as price
def s2_stop(fams):
    """PR4. A stop is read as a PRICE and never as a silence: at every state
    of the last budget the supply must still be OFFERING a fresh opening, and
    the walk must be declining it for something cheaper."""
    print("  family              deep degree  top opened  cheapest fresh on"
          " offer  its price  the move it takes  declined")
    for fam in fams:
        states = reach(fam, BUDGETS[-1])
        worst = None
        for s in states:
            d, price = LS.least_uncovered(s)
            ok(d is not None,
               "%s: a state at budget %d had no uncovered degree left in the "
               "supply at all, so a stop cannot be told from exhaustion"
               % (fam.name, BUDGETS[-1]))
            best, _ = s.menu()
            ok(best < price,
               "%s: the walk took a move costing %d while a fresh opening at "
               "degree %d cost %d, so nothing was declined"
               % (fam.name, best, d, price))
            if worst is None or price - best < worst[2] - worst[1]:
                worst = (d, best, price, s)
        d, best, price, s = worst
        top = max([dd for st in states for dd in st.opened] or [0])
        ok(top < CAP - 4,
           "%s: the ladder opened degree %d against a supply top of %d"
           % (fam.name, top, CAP))
        print("  %-19s %-12s %-11d degree %-18d %-10d %-15d %s"
              % (fam.name, sorted(set(st.deep()[0] for st in states)), top,
                 d, price, best, "by %d" % (price - best)))


def s2_wrong_c(fam, moves):
    """PR4's other half: family (C) at c = 1 -- the wrong c for a branch whose
    deep item sits at degree 3 -- must NOT stop, and the rig prints what it
    opens instead."""
    w, opens, offers = LS.ladder_walk(fam.npl, fam.sch, fam.name, moves,
                                      dcap=CAP)
    # PR4 promises the DEGREES it opens instead, not a count of them
    print("  %-19s opens %2d degrees -- %s -- the last at move %d"
          % (fam.name, len(w.opened),
             ",".join(str(x) for x in sorted(w.opened)), opens[-1]))
    ok(not LS.stopped(opens, moves),
       "%s: the ladder stopped at the wrong c, so the branch dependence is "
       "not real" % fam.name)


# ------------------------------------------------ S3 the family decomposition
def s3_decompose(fams):
    """PR5. The observable is the decomposition and not the count, so the
    predicted shapes are matched one by one and a total is never compared on
    its own."""
    for fam in fams:
        states = reach(fam, BUDGETS[-1])
        audit(fam, states)
        got = {}
        for r in readings(states):
            dp = r[0]
            sh = (dp[0], tuple(sorted((it[0], e) for it, e in r[1])))
            got[sh] = got.get(sh, 0) + 1
        want = fam.shapes()
        print("  %s" % fam.name)
        for sh in sorted(set(list(got) + list(want))):
            print("     deep at degree %-3d beside %-22s  %-5s readings, "
                  "predicted %s"
                  % (sh[0],
                     ",".join("degree %d at exponent %d" % x for x in sh[1])
                     or "nothing",
                     got.get(sh, 0), want.get(sh, "-- NOT PREDICTED")))
        ok(set(got) == set(want),
           "%s: the shapes reached %s against the predicted %s"
           % (fam.name, sorted(got), sorted(want)))
        for sh in want:
            ok(got[sh] == want[sh],
               "%s: the shape %s carries %d readings against the predicted %d"
               % (fam.name, sh, got[sh], want[sh]))


def s3_settled(fams):
    """The reading SET must be constant across the budgets, or the image is
    still growing and the decomposition is a snapshot."""
    print("  family              " + "  ".join("budget %d" % b
                                               for b in BUDGETS)
          + "  same set")
    for fam in fams:
        sets = [readings(reach(fam, b)) for b in BUDGETS]
        same = all(x == sets[0] for x in sets[1:])
        print("  %-19s %s  %s"
              % (fam.name, "  ".join("%-9d" % len(x) for x in sets),
                 "yes" if same else "NO"))
        ok(same, "%s: the reading set moved across the budgets, %s"
           % (fam.name, [len(x) for x in sets]))


# ------------------------------------------------------------- S4 the image
def s4_image(fams, filed=None):
    """PR3 and PR6 in one table."""
    print("  family              homes    home widths  readings  closed form"
          "  factorisation  filed")
    for fam in fams:
        states = reach(fam, BUDGETS[-1])
        deeps = audit(fam, states)
        got = len(readings(states))
        want = fam.form()
        ok(sorted(deeps) == fam.homes(),
           "%s: the reach's deep degrees %s against the home set %s"
           % (fam.name, sorted(deeps), fam.homes()))
        f = (filed or {}).get(fam.name)
        print("  %-19s %-8s %-12s %-9d %-12d %-14s %s"
              % (fam.name, fam.homes(),
                 [fam.width(h) for h in fam.homes()], got, want,
                 factorise(got), f if f is not None else "-"))
        ok(got == want, "%s: %d readings against the closed form %d"
           % (fam.name, got, want))
        if f is not None:
            ok(got == f, "%s: %d readings against the filed %d"
               % (fam.name, got, f))
        # PR6's own clause, read off the home count and nothing else
        ok((got == fam.width(fam.homes()[0])) == (len(fam.homes()) == 1),
           "%s: an image of %d at %d homes, so the home count is not what "
           "decides whether the image is the home's width alone"
           % (fam.name, got, len(fam.homes())))


def s4_tail(a, b):
    """PR6's separating pair: two supplies differing ONLY above the homes must
    give the same image, which is what says the product runs over the homes."""
    ga = len(readings(reach(a, BUDGETS[-1])))
    gb = len(readings(reach(b, BUDGETS[-1])))
    print("  %-19s tail width %-3d  %d readings" % (a.name, a.npl[CAP], ga))
    print("  %-19s tail width %-3d  %d readings" % (b.name, b.npl[CAP], gb))
    ok(a.npl[CAP] != b.npl[CAP],
       "the two tail rows carry the same tail, so they separate nothing")
    ok([a.width(h) for h in a.homes()] == [b.width(h) for h in b.homes()],
       "the two tail rows differ at a home, so a shared image would say "
       "nothing about the tail")
    ok(ga == gb, "the tail rows read %d and %d, so the image is not a product "
                 "over the homes alone" % (ga, gb))


# ------------------------------------------------------------------- main
def main():
    corner = LS.CSched("corner c=1", rule="tick", c=1)
    steep = LS.CSched("steep c=1", rule="tick", c=1, alpha=2)
    floor32 = LS.CSched("floor c=3/2", rule="tick", c=Fraction(3, 2),
                        born=(2,))
    floor1 = LS.CSched("floor c=1", rule="tick", c=1, born=(2,))
    for sch in (corner, steep, floor32, floor1):
        sch.check_monotone(64)

    tied = dict((n, Family("tied n=%d" % n, supply(n), corner, True))
                for n in (1, 2, 3))
    gapped = Family("gapped n=2", supply(2, absent=(2,)), corner, False)
    steepf = Family("steep n=2", supply(2), steep, False)
    floorf = Family("floor n=2", supply(2, absent=(1,)), floor32, False)
    floorc = Family("floor n=3", supply(3, absent=(1,)), floor32, False)
    gapped3 = Family("gapped n=3", supply(3, absent=(2,)), corner, False)
    steep3 = Family("steep n=3", supply(3), steep, False)
    mixed = Family("mixed homes", supply(1, over={1: 2, 2: 3}), corner, True)
    mixtail = Family("mixed tail 5", supply(5, over={1: 2, 2: 3}), corner,
                     True)
    wrongc = Family("floor at c=1", supply(2, absent=(1,)), floor1, False)

    untied = [gapped, gapped3, steepf, steep3, floorf, floorc]
    all_fams = [tied[1], tied[2], tied[3]] + untied + [mixed, mixtail]

    section("S0  THE HARNESS FORCED TO FAIL")
    print("  The four state mutations are applied to a genuine STOPPED state")
    print("  of the tied control, so what the checker rejects differs from")
    print("  what it accepts by exactly the mutation. The fifth and sixth")
    print("  move the SUPPLY: one width at a HOME, against a closed form that")
    print("  must move with it, and one width ABOVE the homes, against a form")
    print("  that must NOT -- which is H5's own separating claim run as a")
    print("  forced check. The seventh is the half a list of rejections")
    print("  cannot show on its own: the unmutated state must be ACCEPTED.")
    s0_forced(tied[2])

    section("S1  THE VOID TIE, READ BEFORE ANY IMAGE IS COUNTED")
    print("  The tie is an EQUALITY BETWEEN TWO PRICES at tick 1. The home")
    print("  set is read twice -- off the filed void-menu law and off the")
    print("  walker's own root menu -- and the covering rule is checked to")
    print("  reach none of the supplied degrees at tick 1, without which the")
    print("  filed law would be reading a menu this rig does not walk.")
    s1_ledger(all_fams + [wrongc])

    section("S2  THE POSITIVE CONTROL, BEFORE ANY UNTIED ROW IS READ")
    print("  The tied supply under the same covering rule, against")
    print("  explore_ladder_stop.py F6's filed numbers -- through THIS rig's")
    print("  enumerator and THIS rig's structural checker. It sits here and")
    print("  not beside the image table below because a control read AFTER")
    print("  the rows it certifies is a comparison and not a control.")
    s4_image([tied[1], tied[2], tied[3]],
             {"tied n=1": 3, "tied n=2": 8, "tied n=3": 15})

    section("S3  THE STOP, READ AS A PRICE AND NOT AS A SILENCE")
    print("  At every state of the last budget the supply must still OFFER a")
    print("  fresh opening and the walk must DECLINE it for something")
    print("  cheaper. The row prints the tightest decline of the reach.")
    s2_stop(all_fams)
    print()
    print("  And the threshold is BRANCH-DEPENDENT: the floor family puts its")
    print("  deep item at degree 3, where c = 1 is below the threshold. Run")
    print("  there, the ladder does not stop at all.")
    s2_wrong_c(wrongc, 12)

    section("S4  THE FAMILY DECOMPOSITION -- THE OBSERVABLE")
    print("  A count cannot separate the two departures a stopped image has")
    print("  from a bare home count, so every shape is matched on its own.")
    s3_decompose(all_fams)
    print()
    s3_settled(all_fams)

    section("S5  THE IMAGE")
    print("  The three tie-breaks, at two widths each.")
    s4_image(untied)
    print()
    print("  Then the homes at DIFFERENT widths, which is the only row that")
    print("  can tell a product over the homes from a power.")
    s4_image([mixed])
    print()
    print("  And the same row with the TAIL changed -- the widths at every")
    print("  degree above the homes, which the exhausted law multiplied in")
    print("  and this one must ignore.")
    s4_tail(mixed, mixtail)

    print("\n%d checks here, %d in the identified walker, %d in the "
          "identity-free one, %d in the stopped-ladder rig"
          % (CHECKS, SI.CHECKS, PS.CHECKS, LS.CHECKS))


if __name__ == "__main__":
    main()
