"""explore_void_untie.py -- what an exhausted image is when the void tie is
BROKEN, and whether the "+1" that stands between a supply and a number ring
is the tie's doing.

THE QUESTION. A supply of n items at each of the degrees 1..D exhausts to an
image of n^(D-1) * (n + 1) (explore_ladder_stop.py F2). The factor n^(D-1) is
a product over openings; the "+1" is not, and it is exactly what stands
between that image and a number ring's 2^t, which is a pure power. F3 reads
the "+1" as the VOID TIE's -- the deep coordinate having two homes because
f(1, 2) = 2 = f(2, 1) at tick 1 -- and every supply walked so far satisfies
that tie, which is the attainment condition of explore_price_schedule.py F3:
the least fresh degree at precisely twice the least born-covered one. So F3's
reading is an inference across a WIDTH sweep and not a derivation, and the
scope line it wrote says so: capacity exhaustion is ruled out as a lock's
mechanism only on supplies that carry the tie.

THIS RIG BREAKS THE TIE and reads what the exhausted image becomes. If it
becomes a pure product over the openings, then capacity exhaustion goes back
on the table as a candidate for a ring's lock, and F3's scope line is what
gets rewritten.
(THE ANTECEDENT HELD AND THE CONSEQUENT DID NOT, which is this framing's own
error and is left standing as frozen. The image is a pure product, and
capacity exhaustion does NOT go back on the table: a ring's supply never runs
out, so the ARITHMETIC objection this rig removes was never the only one. The
freeze reasoned from a shape to a mechanism in one step, which is the move
its own transplant flag 2 forbids -- see F3.)

THE TIE IS BETWEEN DEGREES, NOT BETWEEN ITEMS, which is the one thing a rig
here can get backwards and the reason a thinner supply is not the probe. F2
records that a supply of width 1 -- no item ties anywhere -- still reaches an
image of 2, the two homes being degree 1 with a flat item above it against
degree 2 with degree 1 left empty. Only the PRICE EQUALITY at tick 1 breaks
the tie, so every family below moves a price and none moves a width.

THE HAND-ATTACK, on paper before any engine code. Throughout, the CORNER
schedule (price = d^alpha * sigma, alpha = 1 unless a family says otherwise,
b = 2, one fresh discount per degree, the born-covered set a dial).

 H1 THE HOMES ARE THE VOID MENU'S WINNERS, and that is a filed law rather
    than this rig's fit. At tick 1 a born-covered degree must be bought at
    f(d, 2) and a fresh one costs f(d, 1); the price rises with the degree,
    so only the least of each kind bids, and whichever wins carries the first
    clock -- a born-covered opening lands at exponent 2 and IS a clock move,
    a fresh opening lands at exponent 1 and its own next move, at the price it
    just paid, is the clock. A tie gives both (explore_price_schedule.py F3,
    `void_winners`). So the deep coordinate's home set is computable from the
    supply and the price alone, and BREAKING THE TIE means making that set a
    singleton.
 H2 AN EXHAUSTED STATE HAS ONE SHAPE PER HOME. Past exhaustion the only move
    ever taken again is the deep item's own re-clock, so the seated set is
    frozen. That is H1 of explore_ladder_stop.py, and it is RE-DERIVED here
    rather than imported, because that one is argued at alpha = 1 with the
    deep item at degree 1 or 2 and two families below sit outside its range --
    (B) runs alpha = 2 and (C) puts the deep item at degree 3. In general,
    past exhaustion the three doors are the deep item's re-clock at
    d_deep^alpha * T/2, a flat item of degree d at d^alpha * T, and an
    unseated item at a covered degree d at d^alpha * (T + 1). Against the FLAT
    items the deep move wins automatically, every one of them sitting at a
    degree ABOVE the deep one, so d^alpha > d_deep^alpha > d_deep^alpha / 2.
    THAT THE FLATS ALL SIT ABOVE is itself a consequence of H1 and not an
    observation about these supplies. A flat item's degree is not born
    covered, and the home is either the least fresh degree -- in which case
    every other fresh degree is above it outright -- or the least BORN-COVERED
    one, and then no fresh degree can sit below it: a fresh degree d_f < d_b
    would bid f(d_f, 1) = d_f^alpha < d_b^alpha < 2 * d_b^alpha = f(d_b, 2)
    and take the home itself.
    The binding comparison is against an UNSEATED item at a covered degree,
    which can sit BELOW the deep one, and there the binding case is the least
    degree the supply carries: it suffices that
    d_deep^alpha <= 2 * d_min^alpha, since then
    d_deep^alpha * T/2 <= d_min^alpha * T < d_min^alpha * (T + 1).
    THAT IS THE DEGREE CEILING ITSELF (explore_price_schedule.py F2, at b = 2:
    a clock's degree is the greatest d with (d/d_min)^alpha <= b/(b-1) = 2), so
    it holds at every family here by the very condition that puts the home
    where it is -- and it holds NON-STRICTLY, which is why the "+ 1" in the
    unseated door is load-bearing: the tied family's second home sits exactly
    at d_deep = 2 = 2 * d_min, where the deep move costs T against degree 1's
    T + 1. Every price scales with T, so a doubling changes no comparison.
    Its shape:
      - the DEEP degree carries exactly one item, the deep one;
      - every other degree the supply has that is NOT born covered carries
        exactly one item, and it is FLAT (exponent 1) -- it was opened at
        door 1 and never moved again, a move costing d^alpha * T against the
        deep item's d_deep^alpha * T/2;
      - every other BORN-COVERED degree is EMPTY -- its door is never 1, so
        its first seat would land above exponent 1 and be a clock move, which
        past the first one only the deep item ever makes.
 H3 SO THE EXHAUSTED IMAGE IS A SUM OVER HOMES OF A PRODUCT OVER OPENINGS.
    Writing n_d for the number of items at degree d, P for the degrees the
    supply has, B for the born-covered ones and H for the homes,

      image  =  SUM over h in H of  n_h * PRODUCT over d in (P minus B minus
                {h}) of n_d

    At a uniform width n over P = 1..D with B = {1} and H = {1, 2} this is
    n * n^(D-1) + n * n^(D-2) = n^(D-1) * (n + 1), which is F2 -- so the
    formula is the filed one generalised, and F2 is its two-home case rather
    than a separate fact. WITH ONE HOME THE SUM HAS ONE TERM AND THE IMAGE IS
    A PURE PRODUCT. That is the whole prediction, and the "+1" is then not a
    property of exhaustion at all but the count of homes.
    WHAT THIS COUNTS IS THE SHAPES H2 ALLOWS, and that every one of them is
    actually REACHED is a separate claim the hand-attack does not make: H2
    bounds the image above, and the rows are what say the bound is attained.
    So a row coming in UNDER the form would refute the reachability and not
    the shape, and the rig prints the count rather than the gap so that the
    two cannot be read as one number.
 H4 THE TIE BREAKS THREE WAYS, and all three are run because a single
    untied family cannot separate "the tie is what does it" from "degree 1 is
    special" or "alpha = 1 is special".
      (A) GAP THE SUPPLY. Degrees {1} and {3..D}, B = {1}. The least fresh
          degree is 3 and f(1, 2) = 2 < f(3, 1) = 3, so the born-covered side
          wins outright and H = {1}. Openings are 3..D, so the image is
          n^(D-1) -- one factor of n short of the tied family's leading term
          because degree 2 is gone, and no "+1".
      (B) STEEPEN THE PRICE. Degrees 1..D, B = {1}, alpha = 2. Now
          f(1, 2) = 2 < f(2, 1) = 4 and H = {1}. Openings are 2..D, so the
          image is n^D. This one moves NO supply at all -- same items, same
          born set as the tied control -- so it is the family that isolates
          the price equality as the cause.
      (C) RAISE THE FLOOR. Degrees {2..D}, B = {2}. Then f(2, 2) = 4 >
          f(3, 1) = 3, so the FRESH side wins outright and H = {3}. This is
          the tie broken in the other direction, and it is the one that
          separates "one home" from "the born-covered degree is the home":
          here the home is a fresh degree, degree 2 is born covered and left
          empty, openings are 3..D of which the home is one, and the image is
          n^(D-2).
      Beside them a NON-UNIFORM width row, which tests H3 as a PRODUCT rather
      than as a power: widths that differ per degree must multiply, and a rig
      that had only ever seen n^k could not tell a product from a power.
 H5 THE POSITIVE CONTROL IS THE TIED SUPPLY ITSELF, and it must reproduce
    F2's filed numbers -- 2 at width 1, 384 at (2, 8), 972 at (3, 6) -- from
    THIS rig's own enumerator and structural checker before any untied count
    is read. A checker that accepts everything would confirm every family
    here, and the tied family is the one row whose answer is already on file.

TRANSPLANT FLAGS, fixed at the freeze.
 1. THE "+1 IS THE TIE'S DOING" READING IS THE PREDICTION UNDER TEST AND NOT
    A PREMISE. It is explore_ladder_stop.py F3's inference from a width
    sweep -- the width sets the base and the "+1" does not move with it --
    and nothing has derived it. H3 derives it here from H1 and H2, and the
    rig is what says whether the derivation is right; a section that assumed
    it would be assuming the answer.
 2. From the schedule's stopped ladder to a RING's lock: NOTHING is carried.
    A number ring locks by a recurrent vehicle in its class dynamics whose
    price is flat (explore_lock_budget.py F4); a supply here exhausts by
    running out of capacity. What this rig can say is whether the exhausted
    image has the SHAPE a ring's number has -- a pure power of the width at
    width 2 -- and that is a licence to re-open a candidate, never a match.
 3. From the ideal world to the element world: nothing, as in both rigs this
    one imports. A rider raises an exponent with no clock move and no dial of
    this family has that shape.
 4. THE SUPPLIES ARE FINITE BY DESIGN, which is the point rather than a
    limitation: capacity exhaustion is the mechanism under test, so a supply
    that never runs out would have nothing to exhaust. What must not be
    assumed is that a chosen budget REACHED exhaustion, so every section that
    reads a state as exhausted asserts it.
 5. Family (B) changes alpha, which moves the DEGREE CEILING as well as the
    tie -- at alpha = 2 the ceiling on a home's degree drops to 1
    (explore_price_schedule.py F2). So (B) breaks the tie and narrows the
    ceiling in one move and cannot separate them; (A) and (C) leave alpha at
    1 and move only the supply, and they are what carry the verdict. (B) is
    kept because it is the only family that moves no supply at all.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 THE HARNESS CAN FAIL. What the rig PRINTS: per forced failure -- a state
    with a second item at an opened degree, a state with an item at a
    born-covered non-home degree, a state whose deep item sits off its home,
    a supply differing in ONE width against a closed form that must move with
    it and leave the home set alone, and the UNMUTATED state, which must be
    accepted -- whether the check fired.
    KILL: one forced failure that does not fire.
PR2 THE TIE LEDGER, PRINTED BEFORE ANY IMAGE COUNT IS READ. What the rig
    PRINTS: per family, the least born-covered degree and its void price
    f(d, 2), the least fresh degree and its void price f(d, 1), the strict
    comparison between them, and the home set -- both as `void_winners`
    computes it and as the number of distinct DEGREES attaining the walker's
    own root menu minimum.
    KILL: an untied family whose home set is not a singleton; or the tied
    control's home set not being {1, 2}; or the two readings of the home set
    disagreeing at any family.
PR3 THE POSITIVE CONTROL REPRODUCES THE FILED NUMBERS. What the rig PRINTS:
    for the tied supply at (n, D) = (1, 6), (2, 8) and (3, 6), the reading
    count from this rig's enumerator against explore_ladder_stop.py F2's
    filed 2, 384 and 972.
    KILL: one row off the filed number.
PR4 THE EXHAUSTED SHAPE IS H2's AT EVERY REACHABLE STATE. What the rig
    PRINTS: per family and budget, the states, the distinct limit readings,
    whether every state opened every openable degree, and the number of
    distinct deep DEGREES seen across the reach.
    KILL: one state whose seated set is off H2 -- a non-home born-covered
    degree seated, a non-born degree carrying other than one flat item, or a
    deep degree outside the home set.
PR5 THE IMAGE IS THE SUM-OVER-HOMES PRODUCT. What the rig PRINTS: per row,
    the home count, the openable degrees, the reading count, H3's closed
    form, and the count's factorisation.
    KILL: one row off the closed form.
PR6 THE HEADLINE -- AN UNTIED IMAGE IS A PURE PRODUCT, AND AT WIDTH 2 A POWER
    OF 2. What the rig PRINTS: per row, the home count against whether the
    reading count is a power of 2, at uniform width 2.
    KILL: an untied width-2 row that is not a power of 2; or the tied width-2
    control being one, which would mean the home count is not what decides
    it.

FINDINGS (tiers below; run record at the bottom). Every section asserts,
including the closed form, which is checked at every row rather than printed
beside it, and the exhausted shape, which is checked at every reachable state
of every row rather than inferred from a count that matched.

F1 AN UNTIED SUPPLY EXHAUSTS TO A PURE PRODUCT OVER ITS OPENINGS, AND THE
   "+1" IS A SECOND HOME AND NOTHING ELSE -- the sum has one TERM PER HOME
   (proved -- H1, H2, H3 -- and a rule in range over 9 families, 0 off the
   closed form: seven untied across 3 independent dials, beside 2 tied
   controls; at ONE fresh discount per degree throughout, m being the one
   ingredient this rig never dials). Seven untied families reach
   128, 243, 64, 64, 81, 48 and 16
   readings, every one of them the product of the widths at the home and at
   the other openings, with no extra factor anywhere. The two tied controls
   reach 384 and 972, the same product carrying a second term. So the
   exhausted image is

     SUM over homes h of  n_h * PRODUCT over the other openings d of n_d

   and explore_ladder_stop.py F2's n^(D-1) * (n + 1) is that formula's
   two-home case at a uniform width, not a separate fact: the "+1" is the
   SECOND TERM of the sum and it is present exactly when the void menu ties.
   THE DECOMPOSITION IS ASSERTED AND NOT INFERRED. At every reachable state of
   every row the home degree carries the deep item alone, every other
   openable degree carries exactly one item and that item is flat, and every
   born-covered degree that is not the home is EMPTY -- so a right count
   reached by some other structure could not pass. The deep degrees seen
   across each reach are exactly the home set, at every row.
   AND THE EMPTY-DEGREE CLAUSE IS RUN WHERE IT IS LEAST OBVIOUS. In eight of
   the nine families the born-covered set sits at the BOTTOM, at or below the
   home, where such a degree is shadowed by the deep item's own. The ninth
   puts one ABOVE it -- degrees 1, 3, 4, 5, 6 with 1 and 5 born covered -- and
   degree 5 is empty at every reachable state there too, the ladder walking
   straight past it: the openings are 3, 4 and 6, and the image is 16 = 2^4
   rather than the 2^5 a rig counting present degrees would predict. So the
   product runs over the OPENABLE degrees and not the present ones, which is
   a distinction no other row here could have made.
   THREE DIALS OF THE SUPPLY AND THE PRICE, AND THE THIRD IS WHAT MAKES THE
   FIRST TWO A LAW rather
   than a fact about degree 1. Gapping the supply (degrees 1, 3..D) leaves the
   born-covered side winning at f(1, 2) = 2 < f(3, 1) = 3; steepening the
   price to alpha = 2 leaves it winning at 2 < 4 with NO supply moved at all;
   and raising the floor (degrees 2..D, degree 2 born covered) hands the win
   to the FRESH side at f(2, 2) = 4 > f(3, 1) = 3, where the home is degree 3,
   degree 2 sits born covered and permanently empty, and the image is still a
   pure product. So what a single home buys is a one-term sum, and which KIND
   of degree holds it buys nothing.
   AND A FOURTH LEVER BREAKS THE SAME TIE, already on file and not run here,
   which is what makes the three above dials rather than an inventory. The
   three are the SUPPLY and the PRICE at a fixed filtration; the FILTRATION
   itself is a lever too, and the multiplicative one breaks the tie deep-ward
   at every base -- a born-covered opening subtracts its own lower rung there,
   q^(2d) - q^d < q^(2d) - 1, so the ceiling stays admissible and is never
   attained (explore_filtration_price.py F2). What that rig reports is a
   CENSUS reading a singleton and one branch with zero strands, which is this
   law's "one home" reached by a lever this rig never touches, and it was
   measured before the law was stated. It is not an image count, so it
   confirms the HOME half and not the product half.
   AND THE PRODUCT IS A PRODUCT AND NOT A POWER, which the uniform rows cannot
   tell apart: the mixed row carries widths 2, 3, 2 and 4 at degrees 1, 3, 4
   and 5 and reaches 48 = 2 * 3 * 2 * 4.
   THE POSITIVE CONTROL RAN FIRST and through this rig's own enumerator and
   structural checker: the tied supply reproduces F2's filed 2, 384 and 972 at
   (n, D) = (1, 6), (2, 8) and (3, 6). The harness is shown to be able to fail
   at five forced checks: three mutations of a genuine exhausted state, one
   supply differing in a single width against a closed form that must move
   with it while leaving the home set alone, and the UNMUTATED state, which
   must be ACCEPTED -- the half a list of rejections cannot show on its own.

F2 SO THE POWER OF 2 IS THE WIDTH'S AND THE HOME COUNT'S, AND THE TIE IS THE
   WHOLE OF WHAT SEPARATED AN EXHAUSTED IMAGE FROM A RING'S NUMBER
   ARITHMETICALLY -- F3 is the second separation, and it is not arithmetic at
   all (a reading
   of F1 across the width-2 rows; 5 rows, and the arithmetic asserted against
   the home count rather than printed beside it). At uniform width 2 the image
   is a power of 2 at every untied row -- 128, 64, 64, 16 -- and is not one at
   the tied control, 384 = 2^7 * 3. explore_ladder_stop.py F3 read the factor
   of 3 as the void tie's and left it as an inference across a width sweep; it is
   the tie's, and the mechanism is that the tie puts a second term in a sum.
   The width still sets the base and now does only that: at width 3 the untied
   rows read 243 = 3^5 and 81 = 3^4, pure powers of the width.

F3 THE SCOPE LINE OF explore_ladder_stop.py F3 IS WHAT THIS REWRITES, AND THE
   REWRITE IS NARROWER THAN THE NUMBERS INVITE (a derivation from F1 and F2
   read against two filed results; no rows of its own). That scope line says
   capacity exhaustion is ruled out as a lock's mechanism only on supplies
   carrying the tie, because 3 * 2^(D-1) is not a power of 2. The ARITHMETIC
   half of that objection is now gone: untie the supply and an exhausted image
   is a power of 2 exactly, which is the shape a number ring's finite image
   has. What does NOT follow is that a ring exhausts. A degree there is a
   LOG-NORM and not a residue degree (which [K:Q] bounds), so the rational
   primes alone make the degree set unbounded: the supply never runs out and
   capacity is not available to it as a stop; its ladder stops because the
   recurrent move's price is FLAT and its tick does not overshoot
   (explore_lock_budget.py F4, F5). So the correction is exactly the scope
   line and not the verdict -- capacity exhaustion is no longer excluded by
   ARITHMETIC, and stays excluded for a number ring by its supply. What the
   arithmetic now points at is the STOPPED ladder rather than the spent one.

F4 WHAT IS LEFT OPEN, and the first is where the arithmetic just moved. A
   ladder stopped against a supply that never runs out gives an image of
   n^2 + 2n = n(n + 2) at a stop at degree 2 (explore_ladder_stop.py F6),
   where the void tie is unbroken as it is here. But the parallel is NOT
   exact, and the difference is the interesting part: that image is THREE
   families over the two homes and not two, F6's first and third both sitting
   at home 1 -- deep at degree 1 with degree 2 empty, or with degree 2 flat --
   because a stop leaves degree 2 OPTIONALLY opened where exhaustion forces
   it. So a stopped image departs from a pure product for two reasons, the
   home count and the optional opening, and breaking the tie can only remove
   one of them. So the question F1 answers for exhaustion is
   open for the mechanism a ring actually has, and the probe is this rig's
   tie-breaks run under that rig's stopping rule -- the two families compose,
   both being dials of the one schedule.
   (SINCE ANSWERED, and the "two reasons" half is REFUTED: they are one
   reason. A stopped ladder stops at the first clock or never, so every
   opening happens at tick 1, where a degree is opened only by attaining the
   void menu's minimum -- which is what a home IS. The optional degree is the
   OTHER HOME, and the tie-break removes both at once: an untied stopped image
   is the home's WIDTH ALONE, and a tied one is a product over the homes with
   the widths above them not entering at all. So this rig's product over the
   OPENINGS and that one's product over the HOMES are two different laws and
   not one formula, and what would join them is a ladder that climbs a while
   before stopping, which no dial at alpha = 1 has. explore_stopped_untie.py
   F1, F2, F4.) The second is the element world,
   untouched here as in both rigs this one imports. The third is that family
   (B) moves alpha, which narrows the degree ceiling as well as breaking the
   tie (transplant flag 5), so it cannot separate them; families (A) and (C)
   leave alpha at 1 and are what carry the verdict, and (B) is kept only
   because it is the one family that moves no supply at all.

RUN RECORD. One process, CPython, no BLAS. Wall 1.0s, peak working set
20.3 MB against the 512 MB ceiling -- it reads 20.1 to 20.3 across runs, the
allocator's noise and not a figure to chase. 3500 checks here, 186056 in the
identified walker and 136 in the identity-free one, both imported. What the
enumeration costs is set by the state count of the exhausted image, which IS
the number being verified -- 972 at the largest row.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_price_schedule as PS
import explore_schedule_image as SI

CHECKS = 0

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
class Family(object):
    """A supply and a schedule, named, with the degrees it carries written as
    a dict degree -> width so that a NON-UNIFORM row is expressible. `tied`
    is what the family is claimed to be and is asserted against the void
    menu, never read from it."""

    def __init__(self, name, widths, sch, tied, budget):
        self.name = name
        self.widths = dict(widths)
        self.sch = sch
        self.tied = tied
        self.budget = budget
        self._homes = None
        # sized to the IDENTITY-FREE walker's bound as well, since the filed
        # void-menu law scans to that one
        self.npl = [0] * (max(SI.DCAP, PS.DEG_CAP) + 2)
        for d, w in self.widths.items():
            ok(1 <= d <= SI.DCAP,
               "%s: degree %d is outside the walker's bound %d"
               % (name, d, SI.DCAP))
            self.npl[d] = w

    def present(self):
        return sorted(self.widths)

    def openable(self):
        """The degrees a fresh discount can ever be spent at: present and not
        born covered. These are the openings the product runs over."""
        return [d for d in self.present() if d not in self.sch.born]

    def homes(self):
        if self._homes is None:
            self._homes = sorted(PS.void_winners(self.sch, self.npl))
        return self._homes

    def form(self):
        """H3: the sum over homes of the product over the other openings."""
        total = 0
        for h in self.homes():
            term = self.widths[h]
            for d in self.openable():
                if d != h:
                    term *= self.widths[d]
            total += term
        return total


def reach(fam, budget=None):
    """Every distinct identified state reachable in `budget` moves by any tie
    choice. The imported enumerator, with the cap asserted against here as
    well so that a truncation cannot pass as a count."""
    states = SI.reach(fam.npl, fam.sch, fam.name, budget or fam.budget)
    ok(len(states) <= STATE_CAP,
       "%s: %d states, over the cap" % (fam.name, len(states)))
    return states


def readings(states):
    return set(s.reading() for s in states)


# ------------------------------------------------------ the structural check
def shape_faults(fam, s):
    """PR4: every way a state can be off H2's exhausted shape, as a list of
    complaints. A LIST rather than an assertion so that the forced failures
    can read it directly -- a checker that only ever raises cannot be shown
    to separate a good state from a bad one."""
    out = []
    homes = fam.homes()
    dp = s.deep()
    if dp is None:
        return ["no clock move has been made, so there is no deep item"]
    if dp[0] not in homes:
        out.append("the deep item sits at degree %d, off the home set %s"
                   % (dp[0], homes))
    byd = {}
    for (d, i), e in s.seat.items():
        byd.setdefault(d, []).append(e)
    for d in fam.present():
        exps = sorted(byd.get(d, []))
        if d == dp[0]:
            if len(exps) != 1:
                out.append("the home degree %d carries %d items, not the deep "
                           "one alone" % (d, len(exps)))
        elif d in fam.sch.born:
            if exps:
                out.append("the born-covered degree %d carries %d items and "
                           "is not the home" % (d, len(exps)))
        else:
            if exps != [1]:
                out.append("degree %d carries the exponents %s, not one flat "
                           "item" % (d, exps))
    for d in byd:
        if d not in fam.widths:
            out.append("degree %d is seated and the supply has no item there"
                       % d)
    return out


def exhausted_faults(fam, s):
    """Every openable degree has been opened. Read separately from the shape
    so that a budget short of exhaustion reports as a budget rather than as a
    shape the family failed."""
    want = set(fam.openable())
    got = set(s.opened)
    if got != want:
        return ["opened %s against the supply's openable %s"
                % (sorted(got), sorted(want))]
    return []


def audit(fam, states):
    """PR4 asserted over a whole reach, returning what PR4 prints."""
    deeps = set()
    for s in states:
        f = exhausted_faults(fam, s) + shape_faults(fam, s)
        ok(not f, "%s: %s" % (fam.name, "; ".join(f)))
        deeps.add(s.deep()[0])
    return deeps


# ------------------------------------------------------- S0 forced failures
def s0_forced(fam):
    """PR1. Each mutation is applied to a genuine exhausted state of the tied
    control, so that what the check is shown to reject differs from what it
    accepts by exactly the mutation."""
    states = reach(fam)
    ok(states, "%s: an empty reach" % fam.name)
    base = None
    for s in states:
        if not (exhausted_faults(fam, s) + shape_faults(fam, s)):
            base = s
            break
    ok(base is not None,
       "%s: no state of the control passes its own shape check, so the forced "
       "failures would have nothing to mutate" % fam.name)
    fired = []

    dp = base.deep()
    flat = [it for it in base.seat if it != dp and base.seat[it] == 1]
    ok(flat, "%s: an exhausted state with no flat item to duplicate"
       % fam.name)

    # (a) a second item at an already-opened degree -- a REAL item of that
    # degree the supply carries and the walk left unseated, so the state
    # differs from the accepted one by exactly one seat and by nothing else
    s = base.copy()
    d = flat[0][0]
    free = next(j for j in range(base.npl[d]) if (d, j) not in base.seat)
    s.seat[(d, free)] = 1
    fired.append(("a second item at an opening", bool(shape_faults(fam, s))))

    # (b) an item seated at a born-covered degree that is not the home
    born_off = [d for d in fam.present()
                if d in fam.sch.born and d != dp[0]]
    if born_off:
        s = base.copy()
        s.seat[(born_off[0], 0)] = 1
        fired.append(("a seat at a born-covered degree",
                      bool(shape_faults(fam, s))))
    else:
        # the control's home IS its only born-covered degree, so this fault is
        # forced on the branch that leaves degree 1 empty -- taken from the
        # reach rather than invented, and reported as the branch it is
        alt = [x for x in states if x.deep()[0] != dp[0]
               and not shape_faults(fam, x)]
        ok(alt, "%s: no second home in the reach, so the born-covered fault "
                "has no witness" % fam.name)
        s = alt[0].copy()
        s.seat[(sorted(fam.sch.born)[0], 0)] = 1
        fired.append(("a seat at a born-covered degree",
                      bool(shape_faults(fam, s))))

    # (c) a deep item off the home set
    s = base.copy()
    off = max(fam.present())
    s.clocks = list(s.clocks) + [(s.step, (off, 0))]
    fired.append(("a deep item off its home", bool(shape_faults(fam, s))))

    # (d) the closed form must be SENSITIVE to the supply. A form returning
    # the same number whatever the widths would pass every row of every
    # section, and the equality it is checked by cannot see that -- so what is
    # forced here is a supply differing in ONE width, which must move it
    bumped = dict(fam.widths)
    d = fam.openable()[-1]
    bumped[d] += 1
    other = Family(fam.name + "+1", bumped, fam.sch, fam.tied, fam.budget)
    fired.append(("the closed form's sensitivity",
                  other.form() != fam.form() and other.homes() == fam.homes()))

    # (e) and the check must ACCEPT the unmutated state, which is the half a
    # list of rejections cannot show on its own
    fired.append(("the unmutated state accepted",
                  not (exhausted_faults(fam, base) + shape_faults(fam, base))))

    for name, hit in fired:
        print("  %-38s %s" % (name, "fired" if hit else "DID NOT FIRE"))
        ok(hit, "the forced failure of %s did not fire" % name)


# -------------------------------------------------------- S1 the tie ledger
def s1_ledger(fams):
    """PR2, and it runs BEFORE any image is counted: a family that silently
    re-satisfied the tie would print the old number and read as a
    confirmation of the wrong thing."""
    print("  family            born  least born  f(d,2)  least fresh  f(d,1)"
          "  comparison  homes      claimed")
    for fam in fams:
        cb = [d for d in fam.present() if d in fam.sch.born]
        cf = [d for d in fam.present() if d not in fam.sch.born]
        pb = fam.sch.price(cb[0], 2) if cb else None
        pf = fam.sch.price(cf[0], 1) if cf else None
        if pb is None or pf is None:
            cmp_ = "one kind only"
        elif pb == pf:
            cmp_ = "EQUAL"
        else:
            cmp_ = "%d %s %d" % (pb, "<" if pb < pf else ">", pf)
        h = fam.homes()
        print("  %-17s %-5s %-11s %-7s %-12s %-7s %-11s %-10s %s"
              % (fam.name, sorted(fam.sch.born),
                 cb[0] if cb else "-", pb if pb is not None else "-",
                 cf[0] if cf else "-", pf if pf is not None else "-",
                 cmp_, h, "tied" if fam.tied else "untied"))
        ok((len(h) > 1) == fam.tied,
           "%s: %d homes against a family claimed %s"
           % (fam.name, len(h), "tied" if fam.tied else "untied"))
        ok((pb == pf) == fam.tied,
           "%s: the void prices %s and %s against a family claimed %s"
           % (fam.name, pb, pf, "tied" if fam.tied else "untied"))
        # and the same home set read off the WALKER's own root menu, which is
        # the observable -- the law above is a formula and could agree with
        # the walker for the wrong reason
        root = SI.IWalk(fam.npl, fam.sch, fam.name, SI.DCAP)
        _, entries = root.menu()
        degs = sorted(set(e[0] for e in entries))
        ok(degs == h, "%s: the root menu's winning degrees %s against the "
                      "void-menu law's %s" % (fam.name, degs, h))


# ------------------------------------------------------ S2 positive control
def s2_control(rows):
    """PR3. The tied supply's filed numbers, from THIS rig's enumerator and
    through THIS rig's structural checker."""
    print("  supply         budget  states  limit readings  filed"
          "  deep degrees")
    for fam, filed in rows:
        states = reach(fam)
        deeps = audit(fam, states)
        got = len(readings(states))
        print("  %-14s %-7d %-7d %-15d %-6d %s"
              % (fam.name, fam.budget, len(states), got, filed,
                 sorted(deeps)))
        ok(got == filed, "%s: %d readings against the filed %d"
           % (fam.name, got, filed))


# -------------------------------------------------- S3 the untied families
def s3_image(fams):
    """PR4, PR5 and PR6 in one table -- the shape audited per state, the count
    against H3's closed form, and the arithmetic read off it."""
    print("  family            homes  openings              states  readings"
          "  closed form  factorisation  a power of 2")
    for fam in fams:
        states = reach(fam)
        deeps = audit(fam, states)
        got = len(readings(states))
        want = fam.form()
        ok(sorted(deeps) == fam.homes(),
           "%s: the reach's deep degrees %s against the home set %s"
           % (fam.name, sorted(deeps), fam.homes()))
        pow2 = got & (got - 1) == 0
        print("  %-17s %-6d %-21s %-7d %-9d %-12d %-14s %s"
              % (fam.name, len(fam.homes()), fam.openable(), len(states), got,
                 want, factorise(got), "yes" if pow2 else "no"))
        ok(got == want, "%s: %d readings against the closed form %d"
           % (fam.name, got, want))


def s3_arithmetic(fams):
    """PR6 alone, as a claim about the home count and nothing else: at uniform
    width 2 the image is a power of 2 exactly where the home set is a
    singleton."""
    print("  family            homes  readings  a power of 2")
    for fam in fams:
        got = fam.form()
        pow2 = got & (got - 1) == 0
        print("  %-17s %-6d %-9d %s"
              % (fam.name, len(fam.homes()), got, "yes" if pow2 else "no"))
        ok(pow2 == (len(fam.homes()) == 1),
           "%s: an image of %d with %d homes, so the home count is not what "
           "decides the arithmetic" % (fam.name, got, len(fam.homes())))


# ------------------------------------------------------------------- main
def uniform(degrees, n):
    return dict((d, n) for d in degrees)


def main():
    corner = PS.Sched("corner")
    steep = PS.Sched("steep", alpha=2)
    floor2 = PS.Sched("floor2", born=(2,))
    born15 = PS.Sched("born15", born=(1, 5))
    for sch in (corner, steep, floor2, born15):
        sch.check_monotone(SI.DCAP + 1)

    tied28 = Family("tied n=2,D=8", uniform(range(1, 9), 2), corner, True, 20)
    tied36 = Family("tied n=3,D=6", uniform(range(1, 7), 3), corner, True, 16)

    section("S0  THE HARNESS FORCED TO FAIL")
    print("  The three state mutations are applied to a genuine exhausted")
    print("  state of the tied control, so what the checker rejects differs")
    print("  from what it accepts by exactly the mutation. The fourth moves")
    print("  the SUPPLY by one width, against a closed form that must move")
    print("  with it and leave the home set alone. The fifth is the half a")
    print("  list of rejections cannot show on its own: the unmutated state")
    print("  must be ACCEPTED.")
    s0_forced(tied28)

    section("S1  THE VOID TIE, READ BEFORE ANY IMAGE IS COUNTED")
    print("  The tie is an EQUALITY BETWEEN TWO PRICES at tick 1. A family")
    print("  that silently re-satisfied it would print the old number and")
    print("  read as a confirmation of the wrong thing, so the comparison is")
    print("  asserted here and the home set is read twice -- off the filed")
    print("  void-menu law, and off the walker's own root menu.")
    fams = [
        tied28,
        tied36,
        Family("gapped n=2,D=8", uniform([1] + list(range(3, 9)), 2), corner,
               False, 20),
        Family("gapped n=3,D=6", uniform([1] + list(range(3, 7)), 3), corner,
               False, 16),
        Family("steep n=2,D=6", uniform(range(1, 7), 2), steep, False, 24),
        Family("floor n=2,D=8", uniform(range(2, 9), 2), floor2, False, 20),
        Family("floor n=3,D=6", uniform(range(2, 7), 3), floor2, False, 16),
        Family("mixed gapped", {1: 2, 3: 3, 4: 2, 5: 4}, corner, False, 14),
        # a born-covered degree ABOVE the home, which every other family
        # leaves untested -- all their born sets sit at or below it. The
        # clause under test is that such a degree is EMPTY too, which is far
        # less obvious there: it is not shadowed by the deep item's own
        # degree, and the ladder walks straight past it
        Family("born above", uniform([1, 3, 4, 5, 6], 2), born15, False, 14),
    ]
    s1_ledger(fams)

    section("S2  THE POSITIVE CONTROL")
    print("  explore_ladder_stop.py F2's filed numbers, reproduced by this")
    print("  rig's enumerator and passed through its structural checker")
    print("  before any untied count is read.")
    s2_control([
        (Family("tied n=1,D=6", uniform(range(1, 7), 1), corner, True, 16), 2),
        (tied28, 384),
        (tied36, 972),
    ])

    section("S3  WHAT AN UNTIED SUPPLY EXHAUSTS TO")
    print("  H3: the image is a SUM over homes of a PRODUCT over the other")
    print("  openings. With one home the sum has one term. The mixed row")
    print("  carries different widths per degree, so a product cannot pass")
    print("  there as a power.")
    s3_image(fams)

    section("S4  THE ARITHMETIC, AT UNIFORM WIDTH 2")
    print("  A number ring's finite image is a pure power of 2. The question")
    print("  is whether the home count is the whole of what stands between a")
    print("  supply's exhausted image and that shape.")
    s3_arithmetic([f for f in fams
                   if set(f.widths.values()) == set([2])])

    section("SUMMARY")
    print("  %d checks passed here, %d in the identified walker, %d in the"
          % (CHECKS, SI.CHECKS, PS.CHECKS))
    print("  identity-free one.")


if __name__ == "__main__":
    main()
